# October 1, 2026: Source to Studio

Complete teaching kit for the three-hour Miami AI School workshop. Learners turn a synthetic source pack into a newsletter, social drafts and a silent video, then review, evaluate and revise the work. The separate ElevenLabs voice-agent demonstration has a no-credit role-play fallback.

Begin with [START_HERE.md](START_HERE.md) for the lesson sequence, editable presentation link and original preparation notes.

## Teaching materials

| Material | Files |
|---|---|
| Presentation | [26-slide PDF](presentation_offline.pdf) · [Editable presentation shortcut](OPEN_PRESENTATION.url) |
| Student workbook | [PDF](workbooks/student_workbook.pdf) · [Editable DOCX](workbooks/student_workbook.docx) |
| Instructor runbook and answer key | [PDF](workbooks/instructor_runbook.pdf) · [Editable DOCX](workbooks/instructor_runbook.docx) |
| Facilitation | [Session design](session_design.md) · [Classroom checklist](classroom_checklist.md) · [Copy-and-paste prompts](copy_paste_prompts.md) |
| Source pack | [Markdown](source_pack_input.md) · [JSON](source_pack_input.json) |
| Authored examples | [Newsletter](example_newsletter_output.md) · [Content package](example_content_output.json) · [Intentionally flawed package](calibration_bad_output.json) |
| Evaluation | [Cases](eval_cases.json) · [Scorecard template](scorecard_template.json) · [Calibration answers](calibration_examples.json) |
| Local classroom app | [Starter instructions](starter/README.md) · [Source and tests](starter/) · [Sample MP4](starter/media/sample.mp4) |
| Separate voice demo | [Guide](elevenlabs_demo/README.md) · [Agent prompt](elevenlabs_demo/voice_agent_prompt.txt) · [Tests](elevenlabs_demo/demo_tests.json) |

## Run the starter locally

Requires Python 3.10 or newer. Replay uses only the Python standard library and the included synthetic fixtures; it needs no account, API key or package installation.

From this workshop folder:

```sh
cd starter
python3 server.py
```

Open <http://127.0.0.1:8765> on the same computer. Keep live mode disabled. Choose **Run good replay**, then **Use included MP4** to follow the complete offline workflow. See the [starter README](starter/README.md) for Windows commands and the review, evaluation, revision and export steps.

This is a local, single-user classroom starter. It must not be exposed to the internet or deployed as a production service. Optional live API and ElevenLabs behavior has not been verified by this repository import. An instructor must separately authorize and test any paid use.

## Archive provenance

Imported from `AI_School_Oct1_Complete_Teaching_Kit.zip` on October 5, 2026. The archive is 956,662 bytes and its SHA-256 is `d6a0905ade01fd0cd5a0f5815cac8fc1c79016c4f5536ee16d2f3c87b1efa182`.

All 55 original files are included with unchanged contents. The archive's outer folder was replaced by this dated workshop folder, preserving every relative path within the kit. [KIT_MANIFEST.json](KIT_MANIFEST.json) records the 54 companion files; the manifest itself is the 55th file. The macOS launcher has its executable permission enabled.

The [original starter evidence](starter/evidence/VERIFICATION.md) remains unchanged and describes preparation-time results and limitations. See [IMPORT_VERIFICATION.md](IMPORT_VERIFICATION.md) for checks performed during this repository import.
