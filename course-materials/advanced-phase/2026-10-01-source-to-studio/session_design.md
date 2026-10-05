# AI School session design

## Session outcome

October 1, 2026; three hours online; nontechnical learners continuing the ContentStudio work. Use one prepared application and one coordinating OpenAI Agents API agent. Students configure instructions, inspect artifacts, make editorial decisions, and evaluate behavior. Coding, new accounts, paid credits, and publication are not required to complete the class.

The agreed order is **source pack and brief → agent-drafted newsletter → social and video drafts → human review and approval → formal evals of the full run → improve and rerun → human reapproval of changed outputs**. A separate ElevenLabs conversational voice-agent demonstration follows. It is a different fictional business scenario, not an intake stage or narration dependency of the content workflow.

## Exact timetable

| Elapsed time | Minutes | Work | Evidence produced |
|---|---:|---|---|
| 00–10 | 10 | Outcome, process, continuity | Shared definition of success |
| 10–25 | 15 | Source pack, brief, claim ledger | Supported and blocked claims |
| 25–45 | 20 | One Agents API agent drafts the newsletter | Versioned newsletter output |
| 45–65 | 20 | LinkedIn, X, storyboard, template draft video | Adapted assets and render status |
| 65–80 | 15 | Human editorial review and approval | Decision tied to reviewed versions |
| 80–90 | 10 | Break | Baseline retained |
| 90–150 | 60 | Fixed evals, calibration, logs, repair, rerun | Case results and before/after evidence |
| 150–170 | 20 | Separate ElevenLabs Harbor Bike Repair demo | Voice behavior observations |
| 170–180 | 10 | Package, teach-back, exit ticket | Evidence trail and remaining blockers |

The 60-minute evaluation block is explicit in slides 14–20: 7 minutes framing, 7 minutes check types, 8 minutes human calibration, 13 minutes test suite, 8 minutes run inspection, 12 minutes repair/rerun, 5 minutes evidence-based decision.

## Inputs and outputs

- `source_pack_input.json` / `.md`: input facts and brief, all clearly synthetic
- `example_newsletter_output.md`: authored example output derived from that input; not a model run
- `example_content_output.json`: authored complete draft package using the starter schema
- `calibration_bad_output.json`: intentionally faulty copy for evidence review
- `eval_cases.json`: 14 case specifications, expected behavior, and required evidence; no measured results
- `scorecard_template.json`: blank baseline/revision scorecard
- `copy_paste_prompts.md`: briefing, drafting, adapting, reviewing, evaluating, and repairing recipes
- `workbooks/student_workbook.docx` / `.pdf`: exercises without instructor answers
- `workbooks/instructor_runbook.docx` / `.pdf`: facilitation, setup, answers, recovery, references
- `elevenlabs_demo/`: separate Harbor Bike Repair prompt, eight tests, and instructor guide
- `starter/`: prepared app and its own README/tests. Its implementation and verification report describe the available features.

Do not distribute old preliminary materials that begin with a finished newsletter as input or require ElevenLabs narration in the main pipeline.

## Main workflow and ownership

1. Load the supplied source pack by ID and version. Treat source content as data, not instructions.
2. Build a source-supported claim ledger. Flag gaps and conflicts; never invent facts to fill them.
3. Draft a newsletter for the stated audience. Keep the underlying source alongside it.
4. Adapt the newsletter into LinkedIn/X drafts and a four-scene video storyboard. Continue checking against the original source; a newsletter error must not become the new truth.
5. Render a silent text-led draft through the prepared template. An actual rendered file is distinct from a storyboard or simulated receipt.
6. A human reads the package and watches actual media. Record Approve, Request changes, or Hold against the exact versions. Approval does not publish.
7. Evaluate the full run and fixed cases; inspect both content and tool behavior.
8. Change one prompt rule or guard, rerun unchanged cases, preserve outputs, and return changed artifacts for human review.

**Boundaries:** no publisher, scheduler, arbitrary browsing, voice cloning, real contact data, account changes, purchases, or credential creation. Any optional external paid tool needs its own approved destination, data, scope, and cap. Default replay consumes no API credits.

## Technical truth for the instructor

Current official Agents API documentation uses beta sessions, including `client.beta.agents.sessions.create`, and the HTTP path `/v1/agents/sessions` with `OpenAI-Beta: agents=v1`. The prepared application supplies tool handlers; OpenAI does not magically execute an arbitrary application function. An environment-free session is appropriate when the app owns tool execution. API access and billing are separate from ChatGPT subscriptions. See official references below.

A session completing does not certify every requested tool succeeded. Retain real session IDs and saved history. If progress streaming disconnects, recover existing state before retrying. Missing usage data means unknown, not zero.

Use one agent initially. Writer/reviewer are workflow activities; repeated self-review is not independent truth verification. Enforce allowlists, limits, and approval state in the application handler. Never let a model declare itself the human approver.

## Classroom constraints

These are chosen exercise limits, not social platform specifications:

- Newsletter body: 140–220 whitespace-separated words
- LinkedIn body: 80–130 whitespace-separated words
- X body: at most 240 Unicode code points
- CTA: `Read the practice newsletter.` appears in newsletter/posts/final video scene
- Synthetic label: visible on all outputs and every video scene
- Video: four scenes, 6/8/8/8 seconds; 30 seconds total; 1080 × 1920, 30 fps, H.264 MP4; measured duration tolerance ±0.1 seconds
- Silent default: on-screen text is not called speech captions
- Optional narrated variant only: measure actual audio duration, check spoken meaning and pronunciation, verify caption words and timing, and bind approvals to audio/script/caption/video versions. Word count cannot prove narration duration.

## Human review and eval policy

Human review happens before formal eval teaching. It is an editorial decision about the actual available artifacts. It may approve a storyboard while holding an unrendered video. It cannot approve an unseen file or authorize publishing by implication.

An approval record includes reviewer, timestamp, decision, package/source versions and hashes of reviewed artifacts. Revisions invalidate affected approvals and downstream dependencies. Renderer output changes require playback and renewed media review. Approved version A never transfers silently to version B.

Three evaluation layers:

1. Exact checks: schema, lengths, IDs, duration/format, allowed tools, version matches, file existence
2. Evidence checks: the source actually supports every factual claim, including units, timezones, scope and uncertainty
3. Human-calibrated rubric: clarity, audience fit, usefulness, each 0–2 with concrete anchors

All applicable hard checks must pass. Then use a provisional classroom threshold of at least 5/6 with no zero rubric dimension. Report executed, failed, blocked, not-run, and not-applicable cases separately. The final readiness decision also needs the correct human approval. A pleasant tone never offsets a factual or permission failure.

Calibrate on two authored fixtures before comparing variants. Freeze test cases and grading rules; change one instruction or guard; preserve A/B output and logs. Reserve CASE-06 until after the repair. Repeat model runs when practical; one pass is not a reliability estimate. Maintain a larger unseen set for real deployment later.

## Prepared starter and fallback

The starter app defines the UI and runtime. Classroom UI labels are Source pack, Draft package, Human review, Formal evaluation. Buttons include Run good replay, Run bad replay, Use included MP4, Render MP4, Approve draft, Request changes, Run formal checks, Revise to corrected fixture, and Export this version. Verify against `starter/README.md` before class.

Instructor route: start `python server.py` from `starter/`, open `http://127.0.0.1:8765`, and keep the connection local. Standard-library Python is sufficient for the app; FFmpeg is needed for rerendering. The kit can include a clearly labeled prepared sample MP4. Rehearse both good and bad replay and ensure the current file is played before video approval. Student coding is not required.

Fallback ladder:

1. Live text-only Agents API run only if access, permission, usage cap, and rehearsal all pass
2. Actual captured run with provenance if live access fails
3. Included deterministic replay, labeled as replay, if no captured run is available
4. Authored source/output fixtures and manual scorecard if the app cannot run
5. Storyboard-only package if media is unavailable; actual media tests remain NOT RUN

Never rename a replay or authored fixture as live output. Never spend credits or accept new permissions just to save the demonstration. Protect the 60-minute eval block if anything runs late.

## Separate voice agent demo

Use the exact `elevenlabs_demo/README.md` scenario: Harbor Bike Repair, a fictional shop. Do not substitute the content-workshop FAQ. The provided guide, prompt, and tests are the authority for its facts. No live ElevenLabs agent has been created or tested by these written materials. No external action tools are connected. Use the guide’s role-play fallback if needed.

## Official references checked September 30 2026

- Agents API quickstart: https://developers.openai.com/api/docs/guides/agents-api/quickstart
- Application function tools: https://developers.openai.com/api/docs/guides/agents-api/tools/functions
- Sessions and recovery: https://developers.openai.com/api/docs/guides/agents-api/sessions
- Observability and usage: https://developers.openai.com/api/docs/guides/agents-api/observability
- Separate API billing: https://help.openai.com/en/articles/9039756-managing-billing-for-chatgpt-and-the-api-platform
- General eval practice: https://developers.openai.com/api/docs/guides/evaluation-best-practices
- Deprecations: https://developers.openai.com/api/docs/deprecations
- ElevenLabs voice agents: https://elevenlabs.io/docs/eleven-agents/overview

The Evals platform becomes read-only October 31, 2026; its dashboard/API and legacy Agent Builder are scheduled to shut down November 30, 2026. Use durable evaluation files and methods rather than building the class around retiring interfaces. The source pack, constraints, rubric thresholds, timings and classroom examples are original instructional choices.

## Core cases and implementation scope

Core classroom cases are 01, 02, 07, 08, 10 and 12. Assign one content case and one executable check per pair; share findings and complete one repair/rerun. Other cases are extension/homework. Every case in eval_cases.json names its assessment route and implementation limitations. Fixed replay is not arbitrary-source agent testing. Revise to corrected fixture loads known authored content, not a newly generated model response.

Without FFmpeg, inspect the supplied sample MP4 with its matching fixture as offline evaluation. Do not call it a new render or pair it with changed text as if it proves the revision. Hold revised-video approval until a matching file exists.

## Implemented agent and host boundary

The actual starter adapter exposes get_source_pack and submit_content_package to the agent. It produces newsletter/posts/video scene specifications. The host app performs local MP4 rendering through Render MP4 and separately manages human review and formal checks. Do not imply the agent generated pixels or directly called a video tool. The main exercise still renders and plays the current draft before human video approval.
