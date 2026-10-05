# Preparation verification

Prepared 30 September 2026. This report distinguishes executed tests, rendered outputs and untested integration paths.

## Executed successfully

- 39 Python unittest cases across core workflow, mocked Agents API adapter and real in-process loopback HTTP server/client routes. Full names and result: `unit-tests.txt`.
- 10 dependency-free mocked-DOM checks for UI state and action wiring, including disabled live mode, source/draft display, safe literal text, review gating, parse errors, playback-evidence preservation and version reset. `ui-state-smoke.json`. These are not browser layout or actual media-playback tests.
- Python compilation for server/core/adapter/renderer; Node syntax check for `web/app.js`.
- Actual local FFmpeg render, including four captions/scenes and final MP4 concatenation. `media/sample.mp4` measured with ffprobe: H.264, 1080×1920, 30/1 fps, exactly 30.0 seconds, zero audio streams.
- Visual inspection of extracted scene frames; readable caption layout, no clipped lines in the bundled case, persistent synthetic/silent labels. The actual sample MP4 is included; transient extracted QA frames are not packaged.
- Test coverage includes malformed source/artifacts, non-finite values, exact X 240/241 boundary, undefined citations, selected unsupported quote/link/price/statistic patterns, injected canaries, stale source/content/version approval, simultaneous revisions, render failure + safe local retry, actual version ZIP exports and source-read-before-submit.

## Not established

- **Live OpenAI Agents API behavior was not tested.** No credentials were used and no paid model run occurred. Adapter tests use fake event streams and mocked HTTP. Project access, billing, model availability and provider compatibility need an authorized instructor preflight.
- **Real browser layout, media playback and complete UI clicking remain unverified here.** The dot cloud browser refused localhost with `ERR_BLOCKED_BY_CLIENT`. The separately installed headless Chromium test runner then failed at its temporary local socket permission (`Operation not permitted`), including the permitted sandbox retry. No user browser, account, public deployment or security-setting change was used. The supplied `tests/browser_smoke.py` can be run on a compatible teaching machine with Playwright/Chromium already installed and the local server running.
- No model resistance to arbitrary prompt injection, generic semantic truthfulness, other source packs, social-platform acceptance, or publication success is claimed. No publishing tool exists.

## Reading the evidence

“Replay” means authored synthetic fixtures. Test-generated approval state demonstrates workflow enforcement; it is not a human's editorial endorsement. Review every current artifact and complete the workbook rubric in class. The supplied bad newsletter deliberately demonstrates a meaning-level error that mechanical checks can miss.

Python tested: 3.12.14. FFmpeg tested: 7.1.5. Node used only for optional UI-state/syntax tests: 24.19.0. No third-party Python runtime dependencies.
