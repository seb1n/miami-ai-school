# Repository import verification

Checked October 5, 2026 for the import of the October 1 teaching kit. These checks supplement the unchanged [preparation evidence](starter/evidence/VERIFICATION.md).

## Completeness and content review

- The source ZIP passed its archive integrity check. No unsafe paths or symbolic links were present.
- All 55 original files were imported with unchanged contents. Every one of the 54 companion hashes in `KIT_MANIFEST.json` matches, as do all 32 entries in `starter/MANIFEST.json`.
- All 16 JSON files parse successfully.
- All 26 presentation slides and both nine-page workbooks were rendered and visually inspected. PDF text and metadata were also inspected.
- Text, code, fixtures, DOCX XML and metadata, PDF text and metadata, and media metadata were reviewed for secrets and private information. No credentials or private participant records were found. Example organizations and their data are explicitly fictional.
- The original font and license, sample MP4, presentation shortcut, editable DOCX files, PDFs and preparation evidence are retained.
- No original kit files were excluded. Verification-generated caches and runtime files were kept outside the repository. The outer ZIP container was not added.
- Repository additions are this verification note, a workshop README and links from the course and code indexes. The macOS `start.command` launcher has executable permission; its content is unchanged.
- All 54 relative links in the changed indexes and new workshop documentation resolve. The diff whitespace check passes except for two pre-existing trailing spaces in the bundled font license, retained to preserve the original file and manifest hash.

## Starter checks

Validation used Python 3.11.0 and Node 24.21.0. Live mode was disabled and provider credentials were removed from the test environment. No dependencies were installed and no provider or paid API calls were made.

From `starter/`:

```sh
env -u OPENAI_API_KEY -u OPENAI_AGENT_MODEL -u OPENAI_BASE_URL \
  -u ANTHROPIC_API_KEY -u ELEVENLABS_API_KEY ENABLE_LIVE=0 \
  python3 -m unittest discover -s tests -v

python3 -m py_compile core.py server.py agents_adapter.py render_video.py
node --check web/app.js
```

- Python suite: 39 tests, 38 passed and one optional FFprobe test skipped. This includes real local HTTP workflow checks and mocked live-adapter checks.
- Python compilation and JavaScript syntax checks: passed.
- The supplied `tests/ui_state_smoke.cjs` checks: 10 passed with its evidence-file writer suppressed to preserve the original preparation record. These use a mocked DOM.
- Direct MP4 container inspection confirmed AVC1/H.264 video, 1080 x 1920 dimensions, a 30-second duration, 900 video samples and no audio track. This checks container metadata, not decoded playback.

## Remaining limits

FFmpeg and FFprobe were unavailable, so no new video was rendered and the optional FFprobe test was skipped. Playwright and Chromium were unavailable, so actual browser interaction and video playback were not rehearsed during this import. Rehearse the supplied browser smoke test and complete workflow on the teaching machine before class.

Live OpenAI Agents API behavior and the separate ElevenLabs demonstration remain untested. These results establish the tested local fixture behavior only. Nothing was deployed, merged into the default branch or published to social accounts during this import.
