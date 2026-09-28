# What was built in Codex

**Source review: September 28, 2026**

The class compared two projects: a new mobile-first habit app and an existing Content Studio undergoing design improvements and migration. The prompts now use the original Codex conversations and project files alongside the transcript. The first mobile prompt had been written from the transcript without inspecting the project, so it offered an unnecessarily broad choice of mobile stacks. This revision grounds the default path in the demonstrated build.

## Mobile app: actual build sequence

| Step | Instructor's request or choice | Result recorded in the project |
|---|---|---|
| 1. Install design tooling | Install Impeccable for Codex in the project | Project-local design skill available |
| 2. Explore the habit app | Show different styles; target iPhone first; use quitting smoking and 40 morning push-ups as examples | Four concepts: Playful Blocks, Cobalt Coach, Daily Departure and Native Calm |
| 3. Choose a direction | Go with the designer's pick | Cobalt Coach selected and recorded in the design system |
| 4. Build the first version | Make a clickable MVP with frontend design only; use needed shadcn components | React/TypeScript with Vite, Tailwind and shadcn; browser-local persistence; no connected backend |
| 5. Prepare services | Create the habit database in the authorized Supabase organization and prepare Vercel | Profiles, habits and habit logs with ownership rules; hosting configuration ready; UI still using local storage |
| 6. Publish the prototype | Commit, push and deploy | Initial web deployment of the browser-local MVP |
| 7. Add accounts | Add simple per-user authentication and store habits and tracking | Supabase sign-in and private account persistence connected to the existing interface; updated web deployment |

The transcript's later summary describes the general method. The actual project conversation adds the intermediate states, especially the first deployment before account integration. Students can keep that prototype checkpoint or choose to finish authentication before their first release.

## Concrete product lessons

- **Counted habits:** goals, units and increments are separate. Users can add progress and undo a tap. Completion follows the target.
- **All-day commitments:** “Still on track” and “Had a setback” are check-ins. Completing the day is a separate action.
- **Three main screens:** Today for action, Progress for history, and You for account controls.
- **History:** changes to today's goal must not rewrite previous days' recorded targets and units.
- **Data ownership:** each account starts empty and owns its records. Browser demo data is not automatically uploaded to a new account.
- **Honest saves:** the connected app reports saved progress only after the database confirms the write.
- **Scope:** notifications, social features and offline cloud synchronization were outside the demonstrated first version.

These are concrete examples for the habit app. Students should keep the method while changing the screens and data to fit their own product.

## Web app and future native work

The inspected PRODUCT.md identifies the implemented platform as web. The manifest and hosting configuration confirm a Vite app, not an Expo/React Native app. “iPhone first” describes the intended experience and design proportions in this build.

Expo Go and eventual app-store distribution were discussed in class as next steps. They require a suitable native implementation and testing workflow. They were not completed by creating the Vercel web deployment.

## Content Studio: existing product, design and migration

The instructor explicitly retained a **private, single-founder workspace** and chose Impeccable's **code-first** workflow. The three layout options were The Guided Studio, The Margin Notebook and The Reading Room. The instructor selected The Margin Notebook, then requested a polish pass and a commit, push and deployment of that design.

The existing product used React/TypeScript in a Sites-managed Vinext/Worker runtime, with draft data in D1 and optional private image bytes in R2. Its workflow included two generated draft options, a large editor, a collapsible brief, a saved library and manual review. Save changes, Save as new and direct Save draft were distinct actions. A new generation or direct option save preserved the open editor. Review status never posted to social networks.

The design release and migration were separate tracks. The migration work prepared Supabase schema and ownership rules, source-owner reconciliation, repeatable imports, private image handling and a standard Next.js runtime in an isolated checkout. The Vercel candidate targeted a separate protected staging project, with staging-only settings and explicit callback handling.

This was more work than the new habit app because existing data, identities, image files, generation-request history and runtime integrations had to be preserved. A fresh Content Studio can start directly with the target stack; an existing one must inspect and reconcile those dependencies before switching services.

The inspected records distinguish the released Sites design from migration rehearsal, local target-runtime verification, deployment attempts and remaining hosted checks. They do not establish a fully verified production migration. The master prompt retains those checkpoints instead of treating the transcript's closing remarks as proof that every hosted flow passed.

## How the website prompt relates

The website/web-app prompt is the reusable counterpart promised during the session, not a record of a third demonstrated build. It uses the same product context, design comparison, selected design system, clickable frontend, service integration and verification process. It chooses Vite for an appropriate browser app or Next.js when server-backed behavior calls for it, and preserves a suitable existing stack.

## Evidence and limits

The source review covered the actual Codex user requests, design choices, implementation summaries, current source and the isolated Content Studio Next.js checkout. It did not rerun either app or modify application code, databases or deployments. Earlier local checks and deployment receipts are not new verification results.

The original project documented a remaining limitation around successful hosted sign-up, confirmation/reset email delivery and password changes. Students must test their own account and email flow before describing onboarding as verified.

The public course material intentionally omits private repository access details, local machine paths, account IDs and credentials. See [technical references](references.md) for framework documentation and [the start guide](README.md) for using the prompts.
