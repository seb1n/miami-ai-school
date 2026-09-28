# Mobile app master prompt

**Revised September 28, 2026 after reviewing the actual Codex mobile app project and build conversation.**

This prompt follows the Cobalt habit-app workflow demonstrated in class: **Impeccable design options → choose a direction → clickable frontend MVP → Supabase database → Vercel web deployment → user authentication and cloud tracking**. Customize the idea and features while keeping that staged approach.

The demonstrated app uses **React, TypeScript, Vite, Tailwind CSS and shadcn**, with Supabase and Vercel added afterward. It is an iPhone-first responsive web app. Expo was discussed as a later step for native mobile development; it was not the framework used for this classroom build.

**Class example:** A habit app with counted activities such as 40 morning push-ups and all-day commitments such as staying smoke-free. The selected design was Cobalt Coach, with Today, Progress and You screens. Your project can use a different purpose, name and visual direction.

Replace the bracketed fields, then copy the entire block. Read the [class build notes](class-build-notes.md) for the source-backed sequence and the [start guide](README.md) for setup.

```text
You are my product engineer and design partner in Codex. Help me build a mobile-first application using the staged workflow demonstrated in Miami AI School. Start with design and a clickable frontend, then connect real services. Keep the first version simple and show what actually works at each stage.

MY PROJECT
- App name and idea: [name and one-sentence purpose]
- Audience and problem: [who it helps and why]
- Main journey: [start → action → useful result]
- Three essential features: [feature 1; feature 2; feature 3]
- Out of scope: [features to leave for later]
- Starting folder or repository: [New project / existing project]
- Phone experience: [iPhone first / Android first / both]
- Design references and supplied assets: [references or Help me choose]
- User data to save: [records and progress, or None]
- GitHub destination: [repository and branch, or Not selected]
- Supabase destination: [authorized organization/project, or Not selected]
- Vercel destination: [team/project, or Not selected]
- Email provider: [existing provider or Not configured]
- Authorized stages: [local prototype / backend setup / GitHub push / preview deployment / account integration]
- Budget and constraints: [limits]

1. INSPECT AND PLAN
Read the folder and applicable project instructions before editing. Preserve unrelated work. Identify the actual scripts, package manager and available integrations. Start from an empty folder only when this is a new project.

Use React and TypeScript with Vite, Tailwind CSS and shadcn for this mobile-web classroom path. Use only the components needed; the demonstrated first build used Button, Input, Textarea and Dialog. Preserve a suitable existing implementation. Do not introduce Expo, React Native or Next.js just because the project is called a mobile app. Native conversion is a later, separately selected task.

Use Context7 to resolve libraries and check current documentation; use official documentation if unavailable. Verify current installation commands and compatible versions, preserve a lockfile, and do not invent scripts. Confirm that installed tools are available and connected before claiming to use them.

Write PRODUCT.md with the purpose, audience, mobile-web platform, main journey, scope, assumptions and acceptance checks. Present a concise staged plan. Ask only questions that materially affect the result. Obtain plan approval, then complete each authorized stage without asking again for routine work.

2. DESIGN OPTIONS AND SELECTION
Use the project-installed Impeccable skill. If missing, explain the setup needed and continue product planning; do not claim the skill ran. Produce materially different visual directions for the same main screen. The class compared four: Playful Blocks, Cobalt Coach, Daily Departure and Native Calm. Use those as evidence of the range, not as mandatory styles for every app.

Show the options, recommend one and let me select or delegate the choice. Record the chosen design in DESIGN.md and Impeccable's supported design artifacts. Include color, typography, spacing, controls, navigation and interaction states. Preserve the chosen identity through implementation.

For the habit example, distinguish counted progress from an all-day commitment. A push-up action adds a defined number of reps; an on-track check-in does not mean the whole smoke-free day is complete. Make the target, unit and increment understandable. Use labels such as “Daily goal: 30 minutes” and “Add 5 minutes.”

3. CLICKABLE FRONTEND ONLY
Build the selected design as an interactive mobile-web MVP before adding a backend. Use clearly labeled sample data and browser-local storage for this stage. State that the data stays in that browser and is not tied to an account or synchronized to the cloud. Installing Supabase packages is not backend integration.

For a habit app, implement Today, Progress and You, including counted goals and increments, undo, on-track/setback check-ins, notes, explicit day completion, create/edit/archive/restore, and weekly/daily progress. Adapt the screens and behavior to my approved brief if building a different product.

Support local-calendar daily rollover and retain history. Keep prior target/unit values with historical entries so editing a goal does not rewrite past progress. Exclude notifications, social features, monetization and offline cloud sync unless explicitly selected.

Make the app fill the phone browser, with safe-area spacing, clear touch targets, readable labels and working keyboard behavior. A desktop phone frame is optional presentation styling. Include empty, loading, error and confirmation states, visible focus and reduced motion.

Run the actual build and focused behavior tests. Open the browser and demonstrate the complete journey, refresh persistence, failure behavior and mobile/desktop layouts. Create README.md and project-specific AGENTS.md with real commands. Show the working frontend for review before backend integration.

4. CREATE THE DATABASE AND PREPARE HOSTING
When backend setup is authorized, confirm the correct Supabase organization and project. Use my authorized destination, not the instructor's account by default. Create or reuse the project and prepare migrations. For the habit example use profiles, habits and habit_logs, with stable IDs, verified owners, local dates and historical goal snapshots.

Apply least-privilege grants and row-level security for the actual access model, including read, insert, update and delete. Prevent ownership changes and logs attached to another user's habit. Use atomic writes when habit metadata and daily records must succeed together. Keep new-account data empty and separate from sample browser data.

Prepare Vercel for the Vite app: correct repository, root, build command, dist output and SPA routing where needed. Use browser-safe configuration names such as VITE_SUPABASE_URL and VITE_SUPABASE_PUBLISHABLE_KEY. VITE_ variables are bundled into client code; never put privileged Supabase keys, model credentials or email-provider secrets there.

At this checkpoint report separately: database prepared, frontend still local or connected, hosting prepared, and deployed or not deployed. Created tables do not prove that the UI reads or writes them.

5. SAVE AND DEPLOY THE REVIEWED WEB VERSION
Review the diff, exclude credentials/private data, and create a recoverable commit. Push only to the authorized repository and branch. Confirm Vercel's GitHub connection, production branch and intended audience. Use staging services for previews.

The class deployed the browser-local prototype before adding account integration. If I choose that checkpoint, clearly label its local-only storage. Otherwise proceed to account integration before releasing a cloud-enabled version. Never describe the prototype as a completed account-based application.

Deploy a preview only within my authorized scope. Production release requires explicit authorization for the reviewed candidate. Wait for deployment, match it to the source revision, and check the actual URL. Do not purchase services or change domains without authorization.

6. ADD SIMPLE PER-USER AUTHENTICATION AND TRACKING
When account integration is authorized, use Supabase Auth to add sign-up, sign-in, confirmation handling, session restoration, password recovery and sign-out. The demonstrated implementation used email/password. Keep the approved design and connect the UI to each user's own records.

Use the configured email provider where suitable. Check its delivery restrictions rather than assuming any address can receive confirmation/reset emails. Do not disable confirmation to make a demo pass. Verify real email delivery and successful account flows separately from merely displaying those screens.

Replace browser-local persistence with authenticated cloud reads and writes. Start new accounts empty. Do not silently upload sample habits or merge local records into an account. Clear account state when switching users. Show saved progress only after the database confirms the write; preserve previous state and explain retryable errors on failure. Keep privileged operations server-side and use user-scoped access for ordinary operations.

Test users A and B plus signed-out access through actual application/API paths. Check guessed IDs, forged owners, ownership-changing updates and failed writes. Do not use an admin query to prove isolation. Demonstrate create → track → save → refresh → reopen → sign out → sign in again, plus archive/restore and history. Separate local fixtures from hosted checks. After an authorized update deployment, repeat the journey on its real URL.

7. OPTIONAL LATER NATIVE STEP
The classroom result runs in a mobile browser. If I later request a native app, first assess the React Native/Expo work, reusable logic, new UI and device requirements. Expo Go tests compatible Expo projects; it does not convert this Vite application by scanning a QR code. Use a development build when native dependencies require it. Native-device testing and app-store distribution are separate from this Vercel web deployment.

HANDOFF
Return the actual project path, commands, commit, completed stage, checked URL if any, and PASS/FAIL/BLOCKED evidence. Distinguish approved mockups, clickable frontend, browser-local persistence, database setup, connected accounts, deployed version, hosted verification and email delivery. Do not repeat historic test results as if rerun. List only the remaining steps required for my chosen stage.

Start with project inspection and the plan.
```

See [technical references](references.md). This is a reusable version of the demonstrated build workflow, not a claim that another student project has already passed its checks.
