# AI School October 1 teaching kit

For Burhan Sebin. Thursday October 1, 2026, online from 6–9 PM Eastern (3–6 PM Pacific).

## Start here

1. Open the editable presentation: https://docs.google.com/presentation/d/1xhMii-OrRbqJPFya5wGuzj-F-oCdk8-0QMGGsYCcJy4/edit
2. Read workbooks/instructor_runbook.pdf and classroom_checklist.md before class.
3. Give learners workbooks/student_workbook.pdf (or its editable DOCX), the source pack and the starter. Keep the instructor answer key with you.
4. Launch the starter in default replay mode. From the starter folder, run `python server.py` (or `python3 server.py`), then open http://127.0.0.1:8765. Python 3.10 or newer is required. Ask Codex to help launch it using starter/README.md if needed.
5. Rehearse one good run and one bad run. Use the matching included MP4 if FFmpeg is unavailable. Follow the workbook's review, evaluation and revision sequence.

## The agreed lesson

The OpenAI Agents API drafts a newsletter from an approved source pack, then drafts social posts and video scenes. The classroom host app renders a short silent MP4. Students make a human editorial decision, then evaluate the entire run, change one rule and repeat. Changed outputs require new review.

The ElevenLabs conversational voice-agent demonstration is separate. Its fictional repair-shop scenario, complete prompt, eight tests and a no-credit role-play fallback are in elevenlabs_demo/. It is not a narration step inside the newsletter workflow.

## What is included

- Editable Google Slides presentation with 26 slides, teaching notes and sources; presentation_offline.pdf is the checked PDF backup
- Nine-page student workbook and nine-page instructor runbook, each in editable DOCX and PDF
- Copy-and-paste prompt pack, classroom checklist and 180-minute session plan
- Explicitly synthetic source pack, authored good/bad examples and a drafted-newsletter example
- Fourteen evaluation cases, six core classroom cases, blank scorecard and calibration answers
- Runnable starter with source code, tests, good/bad fixtures, version-bound review, export, optional managed Agents API adapter and a real 30-second sample MP4
- Separate ElevenLabs demonstration guide and prompt

## Important status and limits

Replay uses instructor-authored synthetic fixtures. It does not call a model and is not a captured successful API run. All event details in the practice pack are fictional. No social content has been published.

The starter passed 39 Python tests, including real local HTTP workflow tests, and 10 mocked-DOM state tests. Its actual sample MP4 is H.264, 1080×1920, 30 fps, exactly 30 seconds and silent. It includes visible synthetic labels. The rendered workbook pages and all native Google Slides renders were checked.

A real browser UI/media-playback rehearsal remains necessary. Browser execution in the build environment was blocked, so mocked-DOM checks do not establish complete browser behavior. See starter/evidence/VERIFICATION.md and the supplied browser smoke test.

The optional live Agents API adapter was mock-tested only. No account credentials or paid API requests were used. Before enabling live mode, the instructor must verify project access, model availability, permissions, billing and a real successful run. Keep keys in the server environment only, never in student handouts, browser code or shared chats. Default replay is available if live access fails.

The ElevenLabs agent has not been created, published or live-tested. The guide contains the ready-to-use configuration and rehearsal script; the instructor must set up an authorized account/test agent and check microphone/audio/usage, or use the supplied role-play fallback.

## Folder guide

- workbooks/: student and instructor documents
- starter/: runnable classroom application, fixtures, sample video, tests and API notes
- elevenlabs_demo/: separate voice-agent demo materials
- source_pack_input.*: the starting evidence, not a prewritten newsletter
- example_newsletter_output.md and example_content_output.json: authored output examples
- calibration_bad_output.json: intentionally flawed teaching example
- eval_cases.json and scorecard_template.json: test design and evidence records
- copy_paste_prompts.md: prompts for the guided work

Teaching thresholds and timing are classroom choices, not production-readiness guarantees. Preserve source evidence and human review when adapting the workflow to a real business.
