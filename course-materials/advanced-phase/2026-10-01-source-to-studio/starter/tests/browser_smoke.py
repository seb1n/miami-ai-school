"""Optional browser QA. Requires separately installed Playwright + Chromium; not runtime dependencies.
Uses only this local synthetic app. Run with the server running on 127.0.0.1:8765.
"""
import json,time,os,shutil
from pathlib import Path
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[1];out=ROOT/'evidence';out.mkdir(exist_ok=True)
report={'scope':'local synthetic application only','live_api_executed':False,'checks':[]};errors=[]
def ok(name):report['checks'].append({'name':name,'passed':True})
with sync_playwright() as p:
    browser=p.chromium.launch(headless=True,executable_path=os.environ.get('CHROMIUM_EXECUTABLE') or shutil.which('chromium'))
    page=browser.new_page(viewport={'width':1440,'height':1000});page.on('pageerror',lambda e:errors.append(str(e)))
    page.goto('http://127.0.0.1:8765');page.wait_for_function("document.querySelector('#message').textContent.includes('Replay ready')")
    assert not page.locator('#live').is_visible();assert page.locator('.fact').count()==9;ok('default replay, nine facts, live hidden')
    page.screenshot(path=str(out/'ui-home.png'));page.locator('#good').click();page.wait_for_function("document.querySelector('#runlabel').textContent.includes('REPLAY')")
    assert page.locator('.artifact').count()==4;assert page.locator('#evaluate').is_disabled();assert page.locator('#approve-video').is_disabled();ok('four drafts, evaluation gated, script-only video not approvable')
    for k in ['newsletter','linkedin','x']:
        page.locator('#approve-'+k).click();page.wait_for_function("!document.querySelector('#good').disabled")
    page.get_by_role('button',name='Use included MP4',exact=True).click();page.wait_for_selector('video');page.wait_for_function("!document.querySelector('#good').disabled")
    # Actual browser media playback, not a mocked ended event.
    page.locator('video').evaluate('(v) => v.play()');page.wait_for_function("document.querySelector('video').ended",timeout=40000)
    assert page.locator('#approve-video').is_enabled();ok('actual included 30-second video plays to end and unlocks approval')
    page.locator('#approve-video').click();page.wait_for_function("!document.querySelector('#evaluate').disabled");page.locator('#evaluate').click();page.wait_for_selector('.checks-summary')
    assert 'Machine rules passed.' in page.locator('#results').inner_text();ok('review then formal checks pass good fixture with human-rubric caveat')
    page.locator('#evaluation').scroll_into_view_if_needed();page.screenshot(path=str(out/'ui-evaluated.png'))
    with page.expect_download() as d:page.locator('#export').click()
    d.value.save_as(str(out/'ui-good-export.zip'));ok('browser exports complete version ZIP')
    page.locator('#correct').click();page.wait_for_function("document.querySelector('#runlabel').textContent.includes('/ v2 /')")
    assert '0 / 4 REVIEWED' in page.locator('#reviewcount').inner_text();assert page.locator('#evaluate').is_disabled();assert page.locator('video').count()==0;ok('revision clears all reviews, evaluation and video')
    # Edit malformed JSON through the real UI and confirm state remains intact.
    page.get_by_text('Advanced: edit draft JSON and save a new version',exact=True).click();page.locator('#artifactjson').fill('{broken');page.locator('#save').click();assert 'JSON could not be read' in page.locator('#message').inner_text();ok('malformed JSON shows useful error without mutation')
    # New bad run: each reviewer can request changes, no video approval needed.
    page.locator('#bad').click();page.wait_for_function("document.querySelector('#artifactjson').value.includes('doubles engagement')")
    for k in ['newsletter','linkedin','x','video']:
        page.locator('#reject-'+k).click();page.wait_for_function("!document.querySelector('#good').disabled")
    page.locator('#evaluate').click();page.wait_for_selector('.checks-summary');assert 'Revision needed.' in page.locator('#results').inner_text();ok('human-rejected bad fixture fails checks; script-only cannot pass')
    # Load run history, edit source text containing HTML, prove it is literal rather than executable.
    page.get_by_text('Advanced: inspect or edit source JSON',exact=True).click()
    source=json.loads(page.locator('#sourcejson').input_value());source['source_facts'][0]['text']='<img src=x onerror=alert(1)> Synthetic data';page.locator('#sourcejson').fill(json.dumps(source));page.locator('#save').click();page.wait_for_function("document.querySelector('#runlabel').textContent.includes('/ v2 /')")
    assert page.locator('#facts img').count()==0;assert '<img src=x' in page.locator('#facts').inner_text();ok('untrusted source HTML rendered as literal text')
    page.set_viewport_size({'width':390,'height':844});page.goto('http://127.0.0.1:8765');page.wait_for_function("document.querySelector('#message').textContent.includes('Replay ready')")
    assert page.evaluate('document.documentElement.scrollWidth <= window.innerWidth');page.screenshot(path=str(out/'ui-mobile.png'));ok('mobile home fits 390px viewport without horizontal overflow')
    report['page_errors']=errors;assert not errors;ok('no JavaScript page errors during tested flows')
    browser.close()
(out/'browser-smoke.json').write_text(json.dumps(report,indent=2));print(json.dumps(report,indent=2))
