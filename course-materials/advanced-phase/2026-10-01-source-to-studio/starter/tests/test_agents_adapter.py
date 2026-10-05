import copy, io, json, os, unittest
from unittest.mock import patch
from core import load_json
from agents_adapter import BASE, LiveRunError, generate, sse

class FakeTransport:
    def __init__(self,events):self.events=events;self.calls=[]
    def request(self,method,url,body=None,stream=False):
        self.calls.append((method,url,body,stream))
        if stream:return io.BytesIO((''.join('data: '+json.dumps(e)+'\n\n' for e in self.events)).encode())
        return {'id':'sess_mock','data':[]}

def call(name,args,cid='call_1'):
    return {'type':'agent.session.requires_action','session':{'id':'sess_mock','required_actions':[{'type':'function_call','turn_id':'turn_mock','call_id':cid,'name':name,'arguments':args}]}}
def done(sub=None):return {'type':'agent.session.turn.completed','turn':{'id':'turn_mock','subagent_id':sub}}

class AdapterTests(unittest.TestCase):
    def setUp(self):self.source=load_json('source_pack.json');self.good=load_json('good.json')
    def flow(self):return [call('get_source_pack',{}),call('submit_content_package',self.good,'call_2'),done()]
    def test_real_agents_endpoint_contract_and_tools(self):
        t=FakeTransport(self.flow());r=generate(self.source,transport=t);self.assertEqual(r['artifacts'],self.good);self.assertEqual(r['session_id'],'sess_mock')
        body=t.calls[0][2];self.assertEqual(t.calls[0][1],BASE);self.assertEqual(body['environment'],{'type':'none'});self.assertTrue(body['stream']);self.assertEqual(body['agent']['tools'][1]['name'],'submit_content_package')
        self.assertNotIn('api_key',json.dumps(body));self.assertFalse(r['live_tested_during_preparation'])
        results=[x[2]['events'][0] for x in t.calls if x[1].endswith('/events')];self.assertEqual(results[0]['type'],'agent.session.input.tool_result');self.assertTrue(results[1]['success'])
    def test_idle_is_not_success(self):
        with self.assertRaises(LiveRunError):generate(self.source,transport=FakeTransport([{'type':'agent.session.idle','session':{'id':'sess_mock'}}]))
    def test_completed_without_package_fails(self):
        with self.assertRaisesRegex(LiveRunError,'without a validated'):generate(self.source,transport=FakeTransport([done()]))
    def test_submit_before_source_is_rejected(self):
        t=FakeTransport([call('submit_content_package',self.good),done()])
        with self.assertRaises(LiveRunError):generate(self.source,transport=t)
        result=next(x[2]['events'][0] for x in t.calls if x[1].endswith('/events'));self.assertFalse(result['success'])
    def test_unknown_tool_returns_error(self):
        t=FakeTransport([call('publish_everything',{}),done()])
        with self.assertRaises(LiveRunError):generate(self.source,transport=t)
        self.assertFalse(t.calls[1][2]['events'][0]['success'])
    def test_bad_shape_then_tool_retry(self):
        t=FakeTransport([call('get_source_pack',{}),call('submit_content_package',{},'call_bad'),call('submit_content_package',self.good,'call_fixed'),done()]);r=generate(self.source,transport=t)
        self.assertEqual(r['artifacts'],self.good);self.assertFalse(t.calls[2][2]['events'][0]['success']);self.assertTrue(t.calls[3][2]['events'][0]['success'])
    def test_duplicate_call_reuses_saved_result(self):
        t=FakeTransport([call('get_source_pack',{}),call('submit_content_package',self.good,'call_2'),call('submit_content_package',{},'call_2'),done()]);r=generate(self.source,transport=t)
        self.assertEqual(r['artifacts'],self.good);self.assertEqual(t.calls[2][2],t.calls[3][2])
    def test_failed_root_turn_never_passes(self):
        t=FakeTransport(self.flow()[:-1]+[{'type':'agent.session.turn.failed','turn':{'subagent_id':None}}])
        with self.assertRaises(LiveRunError):generate(self.source,transport=t)
        self.assertEqual(sum(m=='POST' and u==BASE for m,u,b,s in t.calls),1);self.assertTrue(any(m=='GET' and '/items?' in u for m,u,b,s in t.calls))
    def test_subagent_completion_is_not_root_completion(self):
        t=FakeTransport(self.flow()[:-1]+[done('sub_1')])
        with self.assertRaises(LiveRunError):generate(self.source,transport=t)
    def test_no_key_no_network(self):
        with patch.dict(os.environ,{'ENABLE_LIVE':'0'},clear=False):
            with self.assertRaisesRegex(LiveRunError,'disabled'):generate(self.source)
    def test_custom_source_contract_rejected(self):
        s=copy.deepcopy(self.source);s['constraints']['video_seconds']=40
        with self.assertRaisesRegex(LiveRunError,'fixed source'):generate(s,transport=FakeTransport([]))
    def test_sse_comments_multiline_and_done(self):
        raw=b': ping\n\ndata: {"type":\ndata: "ok"}\n\ndata: [DONE]\n\n';self.assertEqual(list(sse(io.BytesIO(raw))),[{'type':'ok'}])
    def test_no_raw_exception_secret_in_error(self):
        class Broken:
            def request(self,*a,**kw):raise RuntimeError('SECRET_DO_NOT_ECHO')
        with self.assertRaises(LiveRunError) as caught:generate(self.source,transport=Broken())
        self.assertNotIn('SECRET_DO_NOT_ECHO',str(caught.exception))

if __name__=='__main__':unittest.main()
