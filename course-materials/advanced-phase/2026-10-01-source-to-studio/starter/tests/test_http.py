"""Real loopback HTTP integration; server and client share the same test process."""
import io,json,tempfile,threading,unittest,urllib.request,urllib.error,zipfile
import server
from core import Store
class HTTPTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();server.STORE=Store(self.tmp.name)
        self.http=server.ThreadingHTTPServer(('127.0.0.1',0),server.Handler);self.thread=threading.Thread(target=self.http.serve_forever,daemon=True);self.thread.start()
        self.base='http://127.0.0.1:'+str(self.http.server_port)
    def tearDown(self):self.http.shutdown();self.http.server_close();self.thread.join();self.tmp.cleanup()
    def req(self,path='/api/config',data=None,headers=None):
        h={'Origin':self.base,'X-Classroom-Token':server.CSRF,'Content-Type':'application/json'};h.update(headers or {})
        r=urllib.request.Request(self.base+path,data=None if data is None else json.dumps(data).encode(),headers=h)
        return urllib.request.urlopen(r,timeout=20)
    def action(self,**data):
        with self.req('/api/action',data) as r:return json.load(r)
    def test_http_end_to_end_and_download(self):
        with self.req() as r:config=json.load(r)
        self.assertEqual(config['default_mode'],'replay');self.assertNotIn('api_key',json.dumps(config).lower())
        with self.req('/') as r:self.assertIn(b'Same facts.',r.read());self.assertIn("script-src 'self'",r.headers['Content-Security-Policy'])
        run=self.action(action='create',mode='replay',scenario='good');rid=run['id']
        self.action(action='sample_video',id=rid,version=1)
        for kind in ['newsletter','linkedin','x','video']:self.action(action='review',id=rid,version=1,kind=kind,decision='approved')
        result=self.action(action='evaluate',id=rid,version=1);self.assertTrue(result['evaluations']['machine_checks_passed'])
        with self.req('/export/'+rid) as r:
            self.assertEqual(r.headers['Content-Type'],'application/zip');z=zipfile.ZipFile(io.BytesIO(r.read()));self.assertIn('video.mp4',z.namelist())
        self.action(action='rerun_fixed',id=rid,version=1)
        with self.assertRaises(urllib.error.HTTPError) as e:self.action(action='review',id=rid,version=1,kind='x',decision='approved')
        self.assertEqual(e.exception.code,400)
    def test_http_cross_origin_no_token_and_path_denied(self):
        for h in [{'Origin':'https://other.example'},{'X-Classroom-Token':'wrong'}]:
            with self.assertRaises(urllib.error.HTTPError) as e:self.req('/api/action',{'action':'create'},h)
            self.assertEqual(e.exception.code,403)
        for path in ['/../agents_adapter.py','/agents_adapter.py','/.env','/media/../../README.md']:
            with self.assertRaises(urllib.error.HTTPError) as e:self.req(path)
            self.assertEqual(e.exception.code,404)
        with self.assertRaises(urllib.error.HTTPError) as e:self.req(headers={'Host':'outside.example'})
        self.assertEqual(e.exception.code,403)
