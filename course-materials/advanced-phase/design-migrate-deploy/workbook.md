# Design with intent. Migrate with confidence.

Miami AI School | Content Studio practical workshop | 24 September 2026

Use this workbook with the 34-slide presentation. The first run is a staging rehearsal with synthetic or authorized test data. Production cutover is a separate, reviewed step. These materials do not indicate that any real application has already been migrated or deployed.

## Workshop outcome

Create a deliberate visual design, preserve drafts and private images while moving D1 data into Supabase, and verify the application on a Vercel deployment. The reference code currently uses a Sites/Vinext Worker runtime, D1, ChatGPT identity headers and R2. Reinspect your own checkout rather than assuming it has the same dependencies.

Suggested pacing: setup before class; 10 minutes inventory; 30 minutes design; 40 minutes schema, identity and import rehearsal; 25 minutes runtime and preview; 15 minutes verification and recovery discussion. A real production migration may require additional work outside this lab.

## 1. Setup checklist

- [ ] Access the source repository and create an isolated migration branch.
- [ ] Use the existing lockfile and package manager. Run `node --version`, `npm --version` (or the repo's manager), and `git --version`. Check package.json engines and provider requirements before installing or upgrading Node.
- [ ] Confirm the app starts locally and record its current test/build results.
- [ ] Have GitHub, Supabase and Vercel accounts with access to the intended projects.
- [ ] Create or select a disposable Supabase staging project and two dedicated test users.
- [ ] Install/connect Supabase and Vercel in your coding agent's plugin directory. Complete the provider sign-in and verify the intended team/project. Installation is not proof of authorization.
- [ ] If a directory plugin is not available, use the provider's official MCP setup for your agent. Avoid duplicate connections to the same service.
- [ ] Install Impeccable in the project and verify the skill appears.
- [ ] Prepare authorized source export access or a clearly labeled synthetic fixture. Local development data is not a substitute for a verified live export.

### Plugin and MCP alternatives

Supabase's official endpoint supports project scoping. Substitute the real staging project ref in the client configuration; the placeholder below is not a working endpoint:

```text
https://mcp.supabase.com/mcp?project_ref=YOUR_STAGING_PROJECT_REF&read_only=true
```

Start with read-only inspection. Schema changes require an explicitly authorized write-capable staging connection. A project-scoped connection may not expose account-level project-listing tools; reading table metadata is a valid connection check. Follow the official client-specific authentication instructions.

Vercel's official MCP endpoint:

```text
https://mcp.vercel.com
```

Codex CLI alternative, if the CLI is installed:

```bash
codex mcp add vercel --url https://mcp.vercel.com
```

Claude Code alternative:

```bash
claude mcp add --transport http vercel https://mcp.vercel.com
```

Complete OAuth and verify the team/project. Follow the current provider docs if your client presents a different setup flow. Do not paste access tokens into prompts.

### Design skill

From the project directory:

```bash
npx impeccable install
```

Select your coding agent and project scope. Reload the agent. In Codex, find it through /skills or invoke $impeccable. Review the project hook in /hooks if installed. In Claude Code, use /impeccable. Use the installed skill's help to confirm supported commands. Suggested progression: init, audit, critique, focused implementation, polish. The skill guides decisions; it does not replace browser testing.

### App libraries

Content Studio already includes a shadcn configuration, Tailwind and lucide-react. Reuse them. In a fresh compatible project, follow the official shadcn setup; do not run init over an existing configuration without reviewing what will change.

```bash
# Fresh compatible project only:
npx shadcn@latest init
# Add only components actually needed:
npx shadcn@latest add button input textarea dialog
# Target Supabase client integration, if missing:
npm install @supabase/supabase-js @supabase/ssr
# Optional, only for a specific planned animation:
npm install motion
```

Use the repository's package manager equivalents. Commit the resulting lockfile. Test a small sample before applying new components throughout the app. Server rendering requires the current documented SSR client/session setup, not a browser client reused everywhere.

## 2. Design brief template

**Audience:** Busy founders writing LinkedIn and X drafts.

**Primary flow:** brief -> generate -> edit -> save -> refresh -> reopen.

**Direction:** Editorial workspace. Warm paper, dark green type, restrained terracotta primary action. A compact draft list supports a dominant editor. Real copy replaces generic promises. Icons communicate actions. Avoid adding charts or cards that have no role in the task.

**Tokens to start with:** paper #F4F1E9; ink #173D35; accent #B44D32; spacing 4/8/12/16/24/32/48px; body 16px; heading scale 24/32px; radius 8px. These are proposed design values, not universal rules. Verify rendered contrast and readability. Use one intentional type family and clear weight/size hierarchy.

**Responsive behavior:** At 390px, single-column editor with accessible draft picker. At 1440px, compact list beside the editor. Maintain focus and useful controls at zoomed sizes.

**State coverage:** empty, generating, unsaved, saved, validation error, network failure, expired session. Reduced motion must remain usable.

**Definition of done:** Before/after screenshots at both widths, no unintended overflow, keyboard navigation works, and generate/edit/save/reopen still works. A distinctive brand is not achieved by blindly banning purple, cards or a particular font. Make choices that serve the product.

## 3. Copyable agent prompts

Use one prompt at a time. Read the output and satisfy its checkpoint before continuing. Short versions appear on slides; these are the full instructions.

### Prompt 01: Environment and connection check

```text
Inspect this repository before changing it. Read AGENTS.md, package.json, the lockfile, framework configuration, database schema, authentication code, storage code and deployment configuration. Identify the package manager and supported Node version. Check which design skills, Supabase tools and Vercel tools are actually available. Do not assume installation means authentication succeeded.
Return: current framework/runtime; routes; D1 bindings and tables; object storage; current identity provider; environment variable NAMES only; existing libraries; exact local build/test commands; current Git status. Do not read or print secret values or customer records.
Confirm the intended Supabase project and Vercel team/project using a read-only tool call. For project-scoped Supabase MCP, verify tables or project URL rather than requiring account-level list-projects tools. If unavailable, identify the missing connection and continue the local audit.
Create MIGRATION-PLAN.md with ordered checkpoints for design, backup, schema, identity, data, files, runtime, preview and cutover. Do not change the database or deploy.
```

### Prompt 02: Install the design skill and missing libraries

```text
Check the official Impeccable README and the installed agent's supported skill mechanism. Install Impeccable for this project using its documented installer, selecting only the coding agent I am using. Explain any hook trust prompt so I can review it. Reload the agent if necessary, then verify that the skill appears. Do not claim it is available until the skill can be found.
Inspect components.json and package.json. Reuse the existing component system and icon library. If shadcn/ui is already configured, do not initialize it again. Add only the components needed for our planned editor redesign. Add Motion only if a specific interaction needs it. Use the repository's package manager, review the lockfile changes and run the existing build. Report what was added and how each addition will be used.
```

### Prompt 03: Design audit and direction

```text
Use the installed Impeccable design skill to audit Content Studio in the browser. The audience is a busy founder editing LinkedIn and X drafts. The main task is brief -> generate -> edit -> save -> reopen. Inspect the actual app at 390px and 1440px wide, including empty, loading, error and saved states.
Rank five specific design problems by their effect on this task. Cite the route or component and screenshot evidence. Distinguish hierarchy, spacing, typography, content and interaction issues. Avoid treating a particular font or color as automatically bad.
Propose two coherent visual directions, then recommend one. Use references only for principles, not copied branding. Our proposed direction is an editorial workspace: warm neutral background, dark green text, terracotta primary action, compact draft list, dominant writing area and useful status feedback. Create DESIGN.md with exact tokens, component rules, mobile behavior and a list of approved assets. Do not change the implementation yet.
```

### Prompt 04: Implement one deliberate redesign

```text
Implement the selected direction in DESIGN.md on the draft editor and draft list. Preserve the existing generate, edit, save, refresh and reopen behavior. Give the writing editor the strongest hierarchy and make Save draft the clear primary action. Use realistic sample content, concise labels and one consistent icon family. Apply shared tokens instead of isolated color or spacing overrides.
At 390px, use a single-column flow and an accessible draft picker. At 1440px, use the agreed list/editor composition. Include visible focus, labels, validation, loading, empty, unsaved, saved and failure states. Respect reduced-motion preferences and avoid animation that delays work.
Capture before/after screenshots at both widths, run the relevant existing checks, and exercise the complete draft workflow. Report concrete improvements and any behavior regression. Do not change data access or authentication in this pass.
```

### Prompt 05: Source backup and schema inventory

```text
Prepare a migration rehearsal from the real source environment. Confirm whether D1 is owned in my Cloudflare account or managed by Sites. Confirm the exact source database and environment before exporting. Use documented authorized export access only. A local .wrangler/state database is not a production backup. If managed-source export is unavailable, stop the real migration at that dependency and use a clearly labeled synthetic fixture for the classroom rehearsal.
Create a private backup outside Git with schema, data export, export time, source identifier, checksums, row counts and an object-storage manifest. Test restoration into a disposable local database. Inspect SQLite types, actual value formats, keys, indexes, CHECK constraints and dependencies. Do not run the SQLite dump against Postgres.
Create a per-table and per-column mapping. Preserve draft IDs and content, identify owner mappings, convert timestamps with explicit units/timezone, and flag invalid or ambiguous values. Include generation_requests and draft_images. Decide how to retain or expire operational request ledgers without replaying paid requests. Report blockers and the proposed import order.
```

### Prompt 06: Postgres schema and ownership rules

```text
Using the reviewed mapping, write versioned Postgres migrations for a disposable Supabase staging project. Preserve every required field and relationship, including owner indexes, unique keys, CHECK constraints and draft/image relationships. Keep existing draft IDs as text unless an audited reason requires conversion. Resolve timestamp formats explicitly.
Use Supabase Auth for the workshop target. Map each trusted legacy owner ID to a verified auth.users UUID through a private migration mapping. Do not infer ownership from a display name or an unverified email, and do not transfer ChatGPT passwords or sessions. Quarantine unresolved rows. Document a verified account-claim or administrator reconciliation procedure before real cutover.
Enable RLS on all exposed tables. For drafts, authenticated users can select, insert, update and delete only their own rows. Updates must check both existing ownership and resulting ownership. Create only necessary grants. Keep generation admission and migration maps server-only, with no public Data API access. Review the SQL before applying it to the confirmed staging project. Produce A/B-user and signed-out test cases.
```

### Prompt 07: Transform, import and reconcile

```text
Create a repeatable migration script that reads the private D1 export or restored SQLite database and writes validated UTF-8 CSV or parameterized Postgres inserts. Do not use search-and-replace to translate the SQL dump. Treat all row contents as data. Define null, empty-string, boolean, JSON and timestamp handling explicitly. Preserve stable IDs and text including commas, quotes, line breaks and Unicode.
Import into the confirmed Supabase staging project in dependency order, using a protected server-side migration credential. Never expose that credential to the browser or logs. Make retries safe with a recorded migration run ID and an explicit duplicate/conflict policy; never silently overwrite a newer row. Use a transaction when practical and fail on rejected records.
Produce a reconciliation report: source/target counts per table and mapped owner, IDs, duplicate IDs, orphan links, nulls, timestamp ranges, canonical content hashes and rejected rows. Reset sequences only where integer identities were retained. Record any normalization before comparing hashes. Run the import again on a fresh disposable target to prove reproducibility. Do not proceed while unexplained mismatches remain.
```

### Prompt 08: Move image files and preserve privacy

```text
Inventory all referenced image objects in the source bucket. Database rows contain metadata and object keys; they are not the file bytes. Copy authorized source objects to a private Supabase Storage bucket using a resumable manifest with old key, new key, verified owner, byte count, content type and checksum. Use an ownership-aware destination path such as <auth-user-uuid>/<image-id>. Do not assume an admin upload automatically sets end-user ownership.
Update image metadata only after each copy is verified. Add storage policies that restrict the bucket and authenticated user's path, or an equivalently reviewed ownership model. Serve images through authenticated access or short-lived signed URLs. Test owner A, owner B, signed-out access, missing files and expired URLs. Preserve image-generation idempotency and ensure a retry cannot create an extra paid generation. Do not delete source files during rehearsal or cutover.
```

### Prompt 09: Port the app to the target runtime

```text
Port this Sites/Vinext/Worker application to standard Next.js on Vercel in an isolated branch or checkout. Inspect existing routes first. Replace Worker-only imports, env.DB and R2 bindings, the D1 Drizzle driver, Sites authentication headers and Sites-specific build/start scripts. Preserve business behavior, UI and API contracts where possible. Treat caller-supplied oai-authenticated-user-* headers as untrusted outside the Sites gateway.
Use @supabase/supabase-js and the current @supabase/ssr Next.js integration for browser/server clients and session refresh. Validate identity on the server with the documented method. Use a user-scoped client for ordinary draft CRUD so RLS applies. Keep administrative migration credentials separate. Port the generation admission ledger with atomic reservation and uniqueness guarantees, not an in-memory map. Keep model keys server-only and verify all provider environment variable names against the source.
Update framework scripts/configuration deliberately, add safe .env.example names, generate database types, and test the Next.js production build. Replace or adapt Worker integration tests to exercise the target runtime. Report every platform dependency that remains unresolved.
```

### Prompt 10: Verify authentication and migrated workflows

```text
Against the Supabase staging project, test the application through its actual browser and API paths using two dedicated test users. User A must create, generate, edit, save, refresh and reopen a draft and its image. User B must not read, update, delete or attach A's draft/image even by guessing IDs or bypassing the UI. Signed-out requests must fail safely.
Test forged ownership fields, ownership-changing updates, session expiry, sign-out, failed network requests and a repeated generation request. Retry must not duplicate a paid model/image call. Check the request ledger, logs and data state with redacted evidence. Do not rely on a database-admin query to prove RLS; exercise authenticated user roles.
Run typecheck, lint, relevant automated tests and the production build using the repository's actual scripts. Fix failures, rerun affected checks and return PASS, FAIL or BLOCKED for each workflow.
```

### Prompt 11: Create the Vercel preview

```text
Prepare a Vercel preview deployment for the reviewed branch. Confirm the GitHub repository, branch, Vercel team/project, root directory, standard Next.js framework preset and Node version. Use the connected Vercel tools or documented Git import flow. Configure Preview environment variables for Supabase STAGING only, using the project's environment variable names. Set secrets through the platform, never paste values in chat or commit them.
Configure Supabase Auth redirects for the exact preview callback URL or a narrowly scoped preview pattern. Ensure the preview's email links return to preview. Confirm the intended access setting. Deploy the reviewed commit and report the exact URL, commit and target project. Inspect build and runtime logs, then run the same two-user and draft/image workflow checks on that URL. A successful build is not a completed browser check. Do not promote to production yet.
```

### Prompt 12: Production cutover and recovery plan

```text
Prepare a reviewable production cutover runbook using the verified rehearsal. Name the source/target environments, reviewed application commit, backup, owner mapping and data reconciliation evidence. Confirm production secrets, callback URL, domain and application access policy. Define the write-freeze window and the exact point the target becomes writable.
Before cutover, stop source writes and wait for in-flight generation/image requests to settle. Take the final export and object delta, rerun the proven migration, reconcile data and verify private access. Route traffic to the reviewed Vercel production release only after those gates pass. Resume writes on one system, then verify sign-in, draft create/edit/save/reopen, images and generation on the production URL.
Define rollback separately for application and data. Before target writes, traffic can return to the frozen source after validation. After target writes, freeze again, preserve the target delta and reconcile it before routing back; a Vercel rollback does not restore the database. Keep the source and backups until the agreed retention window ends. Present the concrete plan and any destructive steps for approval before executing production cutover.
```

## 4. Migration command examples

These commands are teaching examples. Substitute audited names and paths, use the approved source/target, and keep data exports outside Git. Never run a destructive migration because a sample says to.

### D1 export under your Cloudflare account

Use the installed Wrangler version in the source project. Create the private backup directory first. Verify the source account/database. Export may block other database requests; schedule appropriately. Virtual-table export limitations may require a separate plan that preserves the original source.

```bash
npx wrangler d1 export DB_NAME --remote --output=./private-backup/d1.sql
```

For Sites-managed databases, first confirm authorized platform export access. Your personal Cloudflare credentials may not expose the managed resource. If access is unresolved, use synthetic data for the lab and record that the real migration is blocked. Do not claim a local .wrangler/state export contains production rows.

### Restore SQLite for inspection

Use an installed sqlite3 client and a fresh disposable filename. The restore is a compatibility check, not the Postgres import:

```bash
sqlite3 ./private-backup/rehearsal.sqlite < ./private-backup/d1.sql
sqlite3 ./private-backup/rehearsal.sqlite 'PRAGMA integrity_check;'
sqlite3 ./private-backup/rehearsal.sqlite 'SELECT count(*) FROM drafts;'
```

Verify every required table and index. Transform through a script that understands the source values. Do not translate SQLite SQL with blind text replacements. Small prepared CSV files can be imported through Supabase's Table Editor; repeatable larger imports should use a script or Postgres COPY tooling.

### Repeatable Postgres application

Use the project's Connect dialog to choose the appropriate direct/session connection for migration tooling. Configure a private psql service called workshop_staging, with credentials stored outside Git. The exact connection depends on network support. Use a reviewed generated migration file:

```bash
psql 'service=workshop_staging' -v ON_ERROR_STOP=1 -f migrations/001_schema.sql
```

Inside psql, an illustrative import into a reviewed staging table:

```sql
\copy migration_staging.drafts FROM './private-backup/drafts.csv' WITH (FORMAT csv, HEADER true);
```

Create the staging table to match the audited columns first. Transform and validate before merging into application tables. A missing CSV value, an empty string and SQL NULL can differ; configure serialization explicitly. Keep migration staging outside exposed API schemas. Import parents before dependent records and preserve keys. Record a run ID and handle conflicts explicitly. For serverless direct SQL at runtime, choose the documented pooling method and compatible driver settings. The main workshop uses Supabase user-scoped APIs for draft CRUD so RLS is enforced.

## 5. Ownership policy teaching example

This example intentionally uses a new disposable table, workshop_drafts. It demonstrates policies only. The actual Content Studio migration must preserve all audited fields, relationships and constraints; do not replace it with this reduced schema. Existing Supabase Auth users are required for owner_id values. Apply to staging after review.

```sql
create table public.workshop_drafts (
  id text primary key,
  owner_id uuid not null references auth.users(id),
  body text not null,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);
create index workshop_drafts_owner_updated
  on public.workshop_drafts(owner_id, updated_at desc);

alter table public.workshop_drafts enable row level security;
revoke all on public.workshop_drafts from anon, authenticated;
grant select, insert, update, delete
  on public.workshop_drafts to authenticated;

create policy "read own" on public.workshop_drafts
  for select to authenticated
  using ((select auth.uid()) = owner_id);
create policy "insert own" on public.workshop_drafts
  for insert to authenticated
  with check ((select auth.uid()) = owner_id);
create policy "update own" on public.workshop_drafts
  for update to authenticated
  using ((select auth.uid()) = owner_id)
  with check ((select auth.uid()) = owner_id);
create policy "delete own" on public.workshop_drafts
  for delete to authenticated
  using ((select auth.uid()) = owner_id);
```

Set owner_id from verified server identity or a user-scoped insert checked by RLS. Never trust a caller-supplied owner ID alone. Implement updated_at changes deliberately. Test A's valid operations, B's guessed-ID operations, signed-out access and attempted ownership transfer through actual authenticated APIs. Admin credentials bypass these policies.

The legacy owner map belongs in a private, non-exposed migration schema. Verify the old account and new account before linking them. For a class fixture, pre-map only instructor-controlled test users. For real users, use a verified claim flow or documented administrator reconciliation. Unresolved rows remain quarantined rather than assigned by guesswork.

Operational ledgers need separate privileges and atomic server-side operations. Port unique keys, reservation logic and idempotency. Do not give browser users general access to generation_requests or allow them to alter their own usage limits.

## 6. Private image migration

Use a manifest with old key, new key, verified owner, bytes, content type, checksum and copy status. Copy actual bytes through authorized source access. A D1 export carries metadata only. Keep the target bucket private; create policies for the intended operations with bucket and owner/path checks. Administrative upload does not prove end-user ownership. Verify the resulting file before linking its metadata. Short-lived signed URLs still need correct authorization when issued. A valid signed URL is a bearer link: anyone who holds it can access that object until it expires. Test signed-out direct access separately from signed-link access; use authenticated delivery if access must be rechecked on every request. Check missing objects and expired URLs. Never make the bucket public to work around a failed ownership check.

## 7. Vercel deployment steps

1. Finish the standard Next.js runtime port and test its production build. A next dependency inside a Vinext project is not proof that its scripts already deploy as standard Next.js.
2. Push the reviewed branch to the authorized GitHub repository. Import it into the intended Vercel team/project and select the correct project root.
3. Confirm framework preset, build command and supported Node version. Remove stale Worker output-directory overrides only after reviewing their purpose.
4. Set Preview variables to Supabase staging. Set Production variables separately. Keep provider keys and administrative credentials server-only. Browser configuration uses the Supabase URL and publishable key with RLS.
5. Configure Supabase Auth site URL and redirect allowlist for the correct environment. Prefer exact production callback URLs. Restrict any preview wildcard to your own deployment namespace.
6. Deploy preview, inspect logs and record the exact URL/commit. Test the deployed browser flow, not just the build result.
7. Review production cutover with the final backup, reconciliation, domain/configuration changes and rollback plan. Freeze source writes for final migration. After promotion, test the exact production URL and resume writes on one system.

CLI alternative, if the Vercel CLI is installed and the project linkage has been reviewed:

```bash
vercel login
vercel link
vercel
# Only after the production cutover gates and authorization:
vercel --prod
```

Git-based deployment is the primary classroom path. CLI deployments use local source, so verify the checkout is clean and matches the reviewed commit before using this alternative. Redeploy after relevant environment changes so the intended configuration reaches the deployment. Vercel access protection and application authentication serve different purposes; confirm the intended audience and private-data access separately.

## 8. Reconciliation and release record

| Check | Evidence to record | Status |
|---|---|---|
| Source backup | Source ID, timestamp, checksum, restore result | Not tested |
| Schema | Reviewed migration files, keys and constraints | Not tested |
| Owners | Verified mappings and unresolved-row report | Not tested |
| Rows | Counts/IDs by table and mapped owner | Not tested |
| Content | Canonical hash comparison and normalization rules | Not tested |
| Relationships | Duplicate/orphan/null checks | Not tested |
| Files | Manifest, checksum, bytes, access checks | Not tested |
| Repeatability | Fresh-target rehearsal result | Not tested |
| Identity + RLS | A/B/signed-out and owner-transfer results | Not tested |
| App behavior | Generate/edit/save/refresh/reopen evidence | Not tested |
| Idempotency | Retried request does not duplicate paid call | Not tested |
| Preview | Exact URL, project, commit and logs | Not tested |
| Production | Write freeze, final delta, URL and smoke test | Not tested |
| Recovery | Source retained; target-delta reconciliation plan | Not tested |

Use PASS, FAIL, BLOCKED or NOT APPLICABLE. Explain each exclusion. A returned URL does not establish that the workflow succeeded. An application rollback is not a database rollback. After new target writes, preserve and reconcile that delta before sending traffic back.

## Slide map

1. Design with intent. Migrate with confidence.
2. The working session
3. Plugins, skills and libraries
4. Before opening the agent
5. Connect Supabase and Vercel
6. Install the design skill
7. Use the smallest useful design stack
8. Prompt 01: inspect the actual project
9. A purposeful workspace
10. Give the agent a design brief
11. A concrete starting token system
12. Prompt 04: redesign one complete flow
13. Design the states people actually see
14. Design review lab
15. The target architecture
16. What Content Studio actually needs moved
17. Choose the correct D1 export path
18. Export, restore and transform
19. SQLite to Postgres: explicit decisions
20. Schema migration and owner mapping
21. RLS is a behavior you must test
22. The ownership policy pattern
23. Prompt 07: rehearse a repeatable import
24. Data reconciliation before cutover
25. Images require a separate migration
26. Replace the platform dependencies
27. Prompt 09: port and verify the app
28. Environment variables on Vercel
29. Deploy the reviewed branch to Vercel
30. Prompt 11: validate the preview URL
31. The live smoke test
32. Production cutover sequence
33. Application rollback and data rollback
34. Your workshop deliverables

## Technical references

Official references checked 24 September 2026. Recheck installation commands and account-specific options before a later class.

- [impeccable](https://github.com/pbakaus/impeccable)
- [shadcn](https://ui.shadcn.com/docs/installation/next)
- [motion](https://motion.dev/docs/react-installation)
- [supamcp](https://supabase.com/docs/guides/ai-tools/mcp)
- [vercelmcp](https://vercel.com/docs/agent-resources/vercel-mcp)
- [d1](https://developers.cloudflare.com/d1/best-practices/import-export-data/)
- [import](https://supabase.com/docs/guides/database/import-data)
- [rls](https://supabase.com/docs/guides/database/postgres/row-level-security)
- [auth](https://supabase.com/docs/guides/auth/server-side/creating-a-client?queryGroups=framework&framework=nextjs)
- [keys](https://supabase.com/docs/guides/getting-started/api-keys)
- [storage](https://supabase.com/docs/guides/storage/security/access-control)
- [redirect](https://supabase.com/docs/guides/auth/redirect-urls)
- [env](https://vercel.com/docs/deployments/environments)
- [next](https://vercel.com/docs/frameworks/full-stack/nextjs)
- [connect](https://supabase.com/docs/guides/database/connecting-to-postgres)
