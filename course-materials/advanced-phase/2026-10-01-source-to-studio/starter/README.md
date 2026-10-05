# Source to Studio
## AI School · classroom starter · 1 October 2026

A small local app for a complete content workflow:

**Synthetic source pack → newsletter → LinkedIn/X posts + silent social video → human review → formal checks → revision → review again.**

The standalone ElevenLabs voice-agent demo is separate. This content pipeline has no ElevenLabs dependency and produces no voiceover.

## Start here: no API key

1. Unzip the starter. Open its folder as a project in Codex desktop.
2. Paste this into Codex:

> Open README.md. Start this classroom app in REPLAY mode with `python server.py`. Do not enable live mode, request API keys, install software, call paid APIs, or publish anything. If Python is missing, tell me the exact missing prerequisite and stop. Tell me the local URL when ready.

3. Open **http://127.0.0.1:8765** on the same computer. Keep the terminal running.
4. Choose **Run good replay**. Read the source facts and inspect all four drafts.
5. Under video, choose **Use included MP4** for a reliable no-install path. It loads an already rendered video that exactly matches the fixed source/video fixture. Choose **Render MP4** if FFmpeg is installed and you want to execute the local renderer again.
6. Review the newsletter, LinkedIn and X drafts. Choose **Approve draft** or **Request changes** for each. Play the video to the end, then decide on it too. The app never posts anything.
7. Choose **Run formal checks**. Review failed rules and the human rubric. A deterministic pass is not proof of factual correctness.
8. Choose **Export this version**. The ZIP includes source, artifacts, run history, approval scope, evaluation results and the current MP4 when present.
9. Run the bad replay. Look for invented claims in the newsletter before running formal checks. Request changes. Then choose **Revise to corrected fixture**, inspect version 2, attach/render the MP4 and review again. Repeat the checks.

### Direct commands

Requires **Python 3.10+**. Tested with Python 3.12.14. No pip packages, Node server, paid credits or account required for replay.

```sh
python server.py
```

On macOS/Linux, use `python3` if `python` is unavailable. On Windows, `py -3 server.py` is another option. Stop with Ctrl+C. If port 8765 is busy:

```sh
python server.py --port 8766
```

The server binds only to 127.0.0.1. Do not expose it to the internet or deploy it. It is a single-user teaching app, not an authenticated multi-user production service.

## What replay means

Replay loads **human-authored synthetic fixtures**, not a recorded live API response and not a model generation. The app labels it clearly. Fixed fixtures make the lesson work with uneven credits, access and installation status.

- `fixtures/source_pack.json`: fictional Bright Harbor Lab event, fact IDs F01–F09
- `fixtures/good.json`: a grounded sample package
- `fixtures/bad.json`: same package with subtle invented claims to catch in human review
- `media/sample.mp4`: a real, finished, silent captioned 30-second MP4; no voiceover
- `media/sample_probe.json`: measured output metadata

“Revise to corrected fixture” replaces the package with the known good sample. It demonstrates rerunning the workflow and resetting approvals; it does not ask a model to reason about your edits. Edited source/video scripts cannot reuse a mismatched sample video.

## Version and approval rules

Each run records source and artifact hashes. A source or content edit creates a new version and clears reviews, evaluation results and video association. Earlier versions remain in the exported history. Every API mutation requires the current version, so stale browser tabs cannot approve a newer draft accidentally.

A video script is not a finished MP4. Approving video requires a current video file; the UI also requires playing it to the end. Loading/rendering a video resets its approval. Formal checks unlock only after all four editorial decisions. A “request changes” decision is a valid review, but makes that approval check fail.

Approval scope is **this classroom draft version only**. It is never permission to publish. No publishing tool exists.

## Render your own edited video

The renderer uses the installed **FFmpeg and ffprobe** executables. It runs a fixed typography template, writes captions to local text files, encodes H.264, and checks the actual file. It does not execute model-written shell commands. Output is 1080 × 1920, 30 fps, silent, yuv420p MP4. Four scenes total 30 seconds for the bundled case.

```sh
python render_video.py fixtures/good.json my-video.mp4
```

If FFmpeg is absent, keep using the included matching MP4. Installation is optional; get your instructor's approval and use [FFmpeg's official download guidance](https://ffmpeg.org/download.html). Builds must include drawtext and libx264. The font is bundled with its license. Short captions are limited to eight wrapped lines per scene to avoid clipping.

## Optional live managed Agents API

**Not needed for class completion. Disabled by default. Implemented against official docs and tested with mocks, but no live paid run was made during preparation.** Project access, model availability, billing and current API compatibility must be verified by the instructor before a live demo. A ChatGPT/Codex subscription is not assumed to cover API usage.

The adapter uses the actual managed **OpenAI Agents API** at `/v1/agents/sessions`, with `OpenAI-Beta: agents=v1`. OpenAI runs the Codex harness and keeps the session. It is not a Responses API wrapper, the separate Agents SDK, or legacy Agent Builder.

For this simple content task, the agent uses `environment: {"type":"none"}`. Function tools run in this application server:

1. `get_source_pack` returns the fixed synthetic facts. The handler enforces source-read before submission.
2. `submit_content_package` accepts schema-valid drafts for human review.
3. The application handles `agent.session.requires_action` and sends `agent.session.input.tool_result` to the session events endpoint.
4. A successful root `agent.session.turn.completed` plus a validated content package is required. Idle/closed streams and subagent completion do not mean success.
5. Local rendering, human approvals and formal evaluation remain separate application phases.

The live adapter deliberately accepts only the bundled source contract. Before extending it to arbitrary sources/constraints, change the prompts/validation and add tests. It never claims to regenerate a custom source in replay.

### Instructor setup, only when you choose live

The instructor must independently authorize/manage API access and project spend controls. If needed, create an application key yourself in the [OpenAI project dashboard](https://platform.openai.com/api-keys), with `api.agents.read`, `api.agents.write` and `api.responses.write` permissions, per the official quickstart. Never paste a key into chat, source files, browser fields, recordings or the agent's sandbox. Do not share one key with the class.

Set **OPENAI_API_KEY** in the application server's environment through your approved secret entry method. The app deliberately has no key-entry form or automatic .env loader. Set **ENABLE_LIVE=1** only when you are ready, and optionally **OPENAI_AGENT_MODEL** (default `gpt-6-astra`, as in the verified official quickstart). Restart the server. The UI then shows **Run live Agents API** and asks for confirmation that a run can incur charges. The server requires that explicit acknowledgement as well.

A time/call limit is a safety guard, not a guaranteed dollar cap. Configure the project's own spending controls. The application never prints keys or raw HTTP error bodies. It logs only allowlisted event metadata. On an uncertain failure it reads the known session and first items page, requests cancellation, and reports the session ID. It never blindly repeats the paid create request. Inspect saved session/items before deciding on another run. Recovery is deliberately conservative rather than an automatic resume engine.

## Student Codex prompts

### Learn the architecture
> Explain this project's flow to a nontechnical person. Show me which parts are deterministic app code and which part would call the managed OpenAI Agents API. Keep live mode disabled. Do not change any files yet.

### Improve a draft safely
> Help me revise the newsletter in the app's draft JSON using only its source facts. Keep the exact synthetic label and CTA. Do not invent quotes, outcomes, prices or links. Explain why the old approvals must reset when I save a new version.

### Repair one failure
> Read the exported run.json. Choose one failed deterministic check. Explain the issue, propose the smallest content or code change, and add a regression test. Do not enable live mode or publish. Run the affected tests before you call the change complete.

### Add an evaluation case
> Add one fixed test for an unsupported factual claim that our current checks miss. Tell me whether the check is deterministic or needs a human rubric. Do not present a phrase detector as proof of truth. Keep the existing cases and rerun all tests.

## Instructor preflight

- Unzip a fresh copy on the actual teaching machine. Run `python -m unittest discover -s tests -v`.
- Start the app and verify the local page loads. Replay is the default and live button is absent.
- Run good fixture, use the included MP4, play it fully, make all four decisions, run checks, export ZIP.
- Run bad fixture; catch the invented “doubles engagement” and “only ten spots” claims in human review. These demonstrate the limits of mechanical checks.
- Revise to corrected fixture, observe v2 and all approvals reset, render/load the matching video, review again and rerun checks.
- Confirm included sample MP4 plays without sound. If local rendering is needed, run a render and inspect all four scenes.
- Keep a copy of the sample video and prepared package outside the running app in case the classroom network or laptop fails.
- Do not use the live adapter on stage until an authorized instructor has independently tested one small paid run and verified the result. Replay is the default contingency.

## Tests and evidence

```sh
python -m unittest discover -s tests -v
python -m py_compile core.py server.py agents_adapter.py render_video.py
```

The fixed suite covers happy replay, human rejection, revision/reapproval, source changes, malformed input, non-finite numbers, missing/unknown citations, injected-instruction canaries, stale versions/hashes, concurrent edits, renderer failure and retry, export contents, and mocked Agents API events/tool flow. `evidence/` contains the actual preparation results and limitations. Test results prove only the tested behavior; no result implies a live model or provider passed.

## Files

| File | Purpose |
|---|---|
| `server.py` | Loopback server and workflow endpoints |
| `core.py` | Data validation, version history, approval gates, deterministic checks |
| `agents_adapter.py` | Optional managed Agents API session/function adapter |
| `render_video.py` | Fixed local FFmpeg renderer |
| `web/` | Plain HTML/CSS/JS browser interface |
| `fixtures/` | Source, good/bad samples and fixed cases |
| `media/` | Finished sample, measured metadata, bundled font/license |
| `tests/` | Offline unit/integration tests; API uses mocks |
| `runs/` | Your new local runs (created at launch; excluded from delivery) |

## Honest limits

- This is a classroom starter, not production security, identity, audit or publishing infrastructure.
- Human rubric scores are recorded in the companion workbook; app review notes can retain reasoning. A deterministic score cannot establish semantic truth.
- X length uses Python Unicode code-point count, not all platform-specific URL/emoji weighting rules. Fixture text is below the classroom cap.
- The live adapter's paid-provider behavior is untested. Beta APIs can change. Consult [API notes](docs/API-NOTES.md).
- No generative video, voice cloning, narration, music, stock footage, social account connection, automatic posting or paid media provider is used.
- The app exports drafts even if rejected, with their status. Exporting is not approval.
