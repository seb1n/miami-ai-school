# Evaluation scope map

Use the companion workbook and `fixtures/workshop_eval_cases.json` for the teaching exercise. The JSON is a case design file, not an OpenAI vendor import format. The full case set is not automatically executed against a live model.

| Case | Implemented evidence |
|---|---|
| 01 Good package | Replay UI; `test_good_end_to_end`, real HTTP export/review/evaluation flow; human factual rubric remains required |
| 02 Unsupported promises | Bad replay; human flags “doubles engagement” and “only ten spots”; regression verifies a changes-requested decision blocks a pass |
| 03 Conflicting source dates | Optional manual/design exercise; arbitrary source-conflict reasoning not implemented |
| 04 Missing CTA dialogue | Optional manual/design exercise; exact-CTA presence check is implemented, missing-source dialogue is not |
| 05 Source injection | Fixed canary + unknown tool + no publisher unit checks; no claim of live model injection resistance |
| 06 Numeric-scope meaning | Human review/design extension; generic semantic interpretation is not automated |
| 07 Length boundary | `test_case_07_x_boundary_240_241`; length-only pass at 240, fail at 241; other hard gates still apply |
| 08 Stale approval | UI version reset; stale version/hash/source tests; concurrent edit tests |
| 09 No publisher | `test_no_publish_route`, mocked unknown-tool rejection; no external publishing integration exists |
| 10 Tool failure | Mocked renderer failure leaves no render receipt; replay retry loads actual matching MP4; no provider outage claim |
| 11 Actual media | Native FFmpeg render, ffprobe metadata test, extracted frame inspection; browser playback still needs instructor preflight |
| 12 Malformed inputs | Source/artifact validation and non-finite-number tests; malformed JSON UI state test |
| 13–14 Extensions | Use the exact companion case descriptions as manual/design work unless adding explicit tests; not represented as executed live evaluations |

Deterministic checks are run only after editorial decisions in the learner UI. Unit tests may exercise gates directly during instructor software preflight. Soft rubric: clarity, audience fit, usefulness, each 0–2; target ≥5/6 with all hard gates passing. Neither high soft score nor machine-check pass authorizes publishing.
