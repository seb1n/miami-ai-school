# Session 2: Content Studio build prompts

Copyable prompts for **Session 2: Build and Publish**, presentation version 3.

Start from an empty folder named `content-studio`. Use one coding agent at a time. The main classroom path uses Codex and ChatGPT Sites. Claude Code can implement in the same Sites-compatible project, then hand it back to ChatGPT Sites for publishing.

These are the complete versions of the prompts shown on the slides. Each prompt includes a pass check. Prompt 14 is the workbook extension for a controlled update after launch. The student application still needs to be built and tested.

## Quick navigation

- [Initial project prompt](#prompt-01-initial-project-prompt)
- [The goal prompt](#the-goal-prompt)
- [Environment audit](#prompt-00-environment-audit)
- [02: Scaffold and local preview](#prompt-02-scaffold-and-local-preview)
- [03: Project instructions](#prompt-03-project-instructions)
- [04: Interface and brief form](#prompt-04-interface-and-brief-form)
- [05: Durable draft storage](#prompt-05-durable-draft-storage)
- [06: Real draft generation](#prompt-06-real-draft-generation)
- [07: Editing and the saved library](#prompt-07-editing-and-the-saved-library)
- [08: Failure handling](#prompt-08-failure-handling)
- [09: Verification and fixes](#prompt-09-verification-and-fixes)
- [10: Design refinement](#prompt-10-design-refinement)
- [11: Release candidate](#prompt-11-release-candidate)
- [12: Publishing](#prompt-12-publishing)
- [13: Hosted verification and audience](#prompt-13-hosted-verification-and-audience)
- [14: A controlled update](#prompt-14-a-controlled-update)

## Before you begin

Install the current ChatGPT desktop app, Node.js LTS and Git. Open the correct project folder, sign in and confirm Sites access. Real in-app generation also requires a configured API account, model access and a usage budget. Enter credentials through the local environment or hosted secret settings, never in chat or Git.

If API credentials are unavailable, use explicitly labeled demo fixtures and leave the live-generation check incomplete. Sites features depend on the account and workspace. Do not treat a local app as a deployed Site.

## The goal prompt

Use `/plan` first to agree on the scope. After approving the plan, use this goal in Codex. Pause it during class discussion when needed. In Claude Code, use Plan mode and the same completion criteria without assuming Codex slash commands are available.

```text
/goal Build and verify Content Studio locally so a user can create two drafts, edit one, save it, refresh and reopen it. Keep API keys on the server and use the agreed Sites-compatible architecture. Finish with passing checks and a browser demonstration. Do not deploy until the publishing exercise.
```

## Build sequence

Run Prompts 00 through 13 in order. Read the result and satisfy the pass check before moving on. The publishing prompts deliberately separate saving a version, deploying it, and choosing its audience.

## Prompt 00: Environment audit

```text
We are starting the first build session for Miami AI School. This folder should be empty. Inspect it before editing. Report the current folder, operating system, Node.js and npm versions, Git availability, and whether a local browser preview can run. Check the current Sites requirements and whether @Sites is available in this account. Do not print credentials or scan unrelated folders. List missing prerequisites with the official installation link and one verification command for each. Do not scaffold the app yet.
```

**Pass check:** The folder is correct. Node, npm and Git respond. Sites is available or the instructor knows it is blocked.

## Prompt 01: Initial project prompt

```text
You are my product engineer for a hands-on Miami AI School build. We are starting with an empty folder named content-studio. Build a Content Studio for a founder who wants to turn a clear brief into LinkedIn or X drafts, edit them, save them, and reopen them later.

Use React and TypeScript with the current ChatGPT Sites-supported starter. Keep the deployment compatible with Sites from the beginning. Use a server endpoint for model calls and Sites D1 for durable records. Do not choose infrastructure that requires a separate hosting service. Use sample content only. Do not post to social networks. Do not publish the Site yet.

First propose a concise plan with the screen structure, data fields, build stages, exact checks for each stage, and any account or credential dependency. Identify the installed starter's actual commands rather than inventing scripts. Save the agreed product brief in docs/project-brief.md. Wait for me to approve the plan before implementing the app.
```

**Pass check:** A specific plan covers the user journey, storage, generation and hosting. No hidden account requirement remains.

## Prompt 02: Scaffold and local preview

```text
@Sites Prepare the approved Content Studio project in this folder using the current supported starter and its documented runtime. Create the minimum React and TypeScript application, install the required dependencies, and configure local development. Keep the Site private and unpublished. If a hosted project must be registered, explain the account requirement and keep its default restricted access.

Add a clear heading and a simple placeholder page. Inspect package.json and record the actual development, build, typecheck and test commands in README.md. Add missing validation scripts only if they are needed. Run the production build and open the local preview. Initialize Git if needed, exclude dependencies, build artifacts and secrets, and create an initial local commit after checking its contents. Do not push to GitHub or deploy.
```

**Pass check:** The page opens locally, the build passes, and a clean local baseline exists.

## Prompt 03: Project instructions

```text
Create a concise root AGENTS.md for Content Studio. Inspect the real starter and package scripts first. Include: role and product purpose, actual stack and folder map, exact development/build/typecheck/test commands, code and content style, testing expectations, Git workflow, and boundaries.

Always: preserve editable drafts, validate user input, keep model credentials on the server, check record ownership for every storage operation, and verify changed behavior. Ask first: adding paid services, changing the agreed architecture, deleting existing records, or publishing. Never: expose secrets, send content to social networks, invent successful checks, or treat demo fixtures as live AI output. Mark missing commands as pending instead of pretending they exist.

Use plain Markdown without agent front matter. Keep it specific to this repository. For Claude Code, add a CLAUDE.md containing @AGENTS.md on its own line. Summarize the instructions and verify that the selected coding agent can read them.
```

**Pass check:** Instructions match actual files and commands. Both tools can use one maintained rule set.

## Prompt 04: Interface and brief form

```text
Implement the first usable Content Studio screen. Use an editorial design with off-white background, deep plum text, violet primary action and restrained coral accents. Show a clear page title and one main action: Generate drafts.

The brief has topic (required, up to 300 characters), audience (required), channel (LinkedIn or X), tone (Practical, Warm or Bold), key points (required, up to 2,000 characters), and optional call to action. Use visible labels and inline validation. Preserve the form when a validation error occurs.

Provide a draft workspace and a saved library area. On narrow screens, stack them in reading order. Build empty, loading and error states before connecting the real model. Temporary fixtures must say Demo output. Do not claim live AI generation yet. Open the preview, inspect desktop and 390px mobile width, and report what works.
```

**Pass check:** The form is usable with keyboard and mobile. Empty submission shows clear errors without losing input.

## Prompt 05: Durable draft storage

```text
Add durable draft storage using the Sites-supported D1 binding. Inspect the starter's database approach before editing. Create a migration for drafts with id, owner_id, topic, audience, channel, tone, key_points, call_to_action, body, status, created_at and updated_at. Status is draft or reviewed.

Use the current supported authenticated identity mechanism and verify it in the deployed runtime. Do not trust an owner_id supplied by the browser. Enforce ownership on create, list, read, update and delete. Add a local development identity mechanism only if documented, and prevent it from working in production.

Implement save, list, reopen, edit and confirmed delete. Show success only after the server confirms the write. Keep unsaved text if a request fails. Apply the local migration, then demonstrate that a saved draft survives refresh and reopening. Keep hosted migration and publishing separate until the release stage.
```

**Pass check:** A saved draft survives refresh. Another user cannot read or change it. Failure preserves unsaved text.

## Prompt 06: Real draft generation

```text
Connect Generate drafts to a server endpoint using the OpenAI Responses API and the current official SDK or supported HTTP request. Read OPENAI_API_KEY only from server environment secrets. Use a configurable model available to my API account. Do not expose keys in browser code, logs or Git. Tell me the environment variable names and where I must enter values, never ask me to paste a key into chat.

Validate the brief on the server. Require the authenticated user, enforce a configurable per-user request limit and input/output size limits, and prevent duplicate submissions. Ask the model for exactly two distinct drafts with body and angle. Ground the text only in the brief, flag missing facts, and do not invent dates, prices or testimonials. Validate the returned structure before displaying it.

Show progress while generating, allow retry after a failure, and preserve existing drafts. Handle timeout, missing key, rate limit and malformed output separately. Run one live smoke test only after I configure credentials and authorize API usage. If credentials are missing, show Setup required and keep a clearly labeled demo mode separate.
```

**Pass check:** A configured account produces two real drafts. The key stays on the server. Errors preserve the brief.

## Prompt 07: Editing and the saved library

```text
Complete the draft workflow. Let the user edit either generated draft, see a character count, copy the exact edited text, and save it. Use a workshop target of at most 280 characters for X and 1,200 characters for LinkedIn. Label these as our writing targets, not platform maximums. Show a warning when the target is exceeded, but do not silently truncate text.

The library lists title/topic, channel, status and last updated time. Support search by topic or body and filtering by channel. Reopening a record must load the stored body. Editing an existing record updates it without creating an accidental duplicate. Deleting requires confirmation. Marking a draft reviewed changes its status but never posts it. Verify edit, copy, save, reopen, search and delete with sample content.
```

**Pass check:** The exact edited text survives save and reopen. Copy matches it. Reviewed has no external publishing effect.

## Prompt 08: Failure handling

```text
Review and improve failure behavior without changing the product scope. Check an empty brief, very long input, repeated clicks, slow generation, model failure, interrupted save and refresh with unsaved edits. Add visible states and recovery actions. Preserve useful input after each recoverable error and make focus move to meaningful feedback.

When generation fails, offer retry without inventing substitute AI output. When save fails, keep the current body and say it is unsaved. Disable repeated requests while one is active. Add a warning before leaving with unsaved edits where the browser supports it. Demonstrate each case with a deterministic test or a controlled fixture that is excluded from production behavior.
```

**Pass check:** Failures are visible and recoverable. No silent data loss or fake success remains.

## Prompt 09: Verification and fixes

```text
Verify the complete Content Studio workflow. First read the real package scripts and AGENTS.md. Run the production build and available static checks. Add focused tests for required-field validation, response parsing, ownership enforcement, save/update behavior and error recovery. Use deterministic provider mocks for automated checks, and identify them as mocked.

In the browser, enter the workshop brief, generate two drafts with the configured live API, edit one, copy it, save it, refresh, reopen it and delete a separate test draft. Check mobile at 390px, keyboard navigation, loading feedback and one failed request. Confirm two identities cannot access each other's records. If account access prevents a live test, mark it blocked rather than passed.

Fix failures in scope. Return a concise table: check, evidence, pass/fail/blocked. Distinguish local verification from hosted verification. Do not deploy.
```

**Pass check:** Evidence covers the whole journey. Blocked checks remain visible.

## Prompt 10: Design refinement

```text
Inspect the actual local Content Studio at desktop and mobile widths. Improve the visual hierarchy and interaction clarity while preserving working behavior. Make the brief and main action easy to locate, make draft text comfortable to edit, reduce unnecessary borders and repeated containers, and give the library a clear secondary role.

Use consistent spacing, accessible contrast, readable labels, visible focus and helpful empty states. Keep the agreed color palette. Do not add new features or placeholder statistics. Compare before and after, then rerun checks affected by the changes.
```

**Pass check:** The primary action is obvious. Mobile and keyboard operation still work.

## Prompt 11: Release candidate

```text
@Sites Prepare a reviewable release candidate for Content Studio. Inspect current changes, run the production build and relevant tests, and verify Sites runtime compatibility. Check for credentials, demo-only shortcuts and unfinished placeholders. List required hosted environment variables and database migrations without exposing secret values.

Update README.md with setup, actual commands, data behavior, limitations and the exact demo sequence. Update AGENTS.md if commands or folders changed. Commit the reviewed source locally and save a Sites version associated with that source. Report the version identifier and commit. Do not deploy it yet and do not broaden access.
```

**Pass check:** A saved version, commit and test summary identify exactly what will be published.

## Prompt 12: Publishing

```text
@Sites Deploy the reviewed Content Studio version identified in the previous step. Before deployment, confirm the required hosted secrets and identity configuration are present without displaying their values. Apply the reviewed database migration using the supported workflow. Keep access restricted to me for the initial deployment.

Deploy the exact approved version, wait for completion and report the production URL, version and current audience. Open the URL and check the page and server-backed workflow. If deployment fails, report the actual failure and fix it before claiming success. Do not automatically enable public access or invite people.
```

**Pass check:** Deployment succeeds and the actual hosted URL works for its owner.

## Prompt 13: Hosted verification and audience

```text
Verify the deployed Content Studio using its production URL. Test generation, editing, saving, refresh and reopen against the hosted services. Confirm the hosted database and credentials work and test an unauthorized visitor. Record whether each check used a live service or a fixture.

Then show me the Site URL and current audience, and ask which available audience to use: named invited viewers, eligible workspace members, or public access. Explain any account restriction briefly. Apply only my selected audience and verify from that visitor's perspective. If private visitors cannot be tested from this session, give the recipient a precise check and mark it pending. Do not claim that the link is public merely because deployment succeeded.
```

**Pass check:** The chosen visitor can use the app. Access and data isolation behave as intended.

## Prompt 14: A controlled update

```text
Add one small improvement to Content Studio: a tone filter for the saved library. Preserve existing draft records and the generation workflow. Update tests affected by the change, run them, review the diff, and save a new Sites version without deploying. Compare it with the current live version. Report what will change, what passed, and the candidate version. Wait for my publish decision.
```

**Pass check:** A new candidate exists while the current live site remains unchanged.

## Recovery prompt: a reproducible bug

```text
Observed problem: [what happened]
Steps: [exact actions]
Expected result: [what should happen]
Actual result: [visible behavior or error]

Reproduce the issue and identify the cause. Make the smallest fix that preserves working behavior. Repeat the original case and the complete edit/save/reopen journey. Report the evidence and anything not tested. Do not deploy as part of this fix.
```

## Demo mode when API access is unavailable

```text
Keep live generation disabled until I configure the API. Provide a clearly labeled Demo mode with deterministic fictional examples for interface and storage testing. Never show those fixtures as live AI results. Keep the real provider interface separate so credentials can enable it later. Mark live-generation verification as blocked.
```

## Final handoff

Record the project location, actual run commands, source commit, checks and evidence, blocked checks, saved Sites version, production URL if deployed, and current audience. Preserve the distinction between local, saved, deployed and verified.
