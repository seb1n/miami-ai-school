# Design, migrate and deploy

Improve Content Studio's visual design, rehearse a D1-to-Supabase migration, and prepare a verified Vercel deployment. This follow-on workshop assumes an existing application after the first build session.

## Materials

- [Read the workbook on GitHub](workbook.md).
- [Download the HTML workbook](workbook.html), then open it in a browser for the formatted version and prompt copy buttons. GitHub shows the HTML source rather than hosting it as a webpage.
- [Master prompts](../master-prompts/): standalone starting prompts for a mobile app, website/web app, and Content Studio, including the existing-project migration path.

Both versions contain the same workbook, dated September 24, 2026, with 12 complete agent prompts, setup commands, a design brief, an illustrative ownership policy, migration checks and deployment instructions. The workbook accompanies the separate 34-slide presentation; the presentation files are not included in this upload.

## Preparation

- An existing source checkout with a working local baseline and recoverable Git revision.
- Supabase and Vercel account access, with their plugins or official MCP connections configured in the coding agent.
- The Impeccable design skill installed and verified for the project.
- A disposable Supabase staging project, two test users, and synthetic or authorized test data.
- Confirmed source export access before migrating real data.

## Workshop sequence

1. Inspect the project, connect the tools, and verify the environment.
2. Define the visual direction and redesign the draft workflow.
3. Back up D1, translate the schema, map verified owners, and reconcile the import.
4. Move private image files and replace platform-specific runtime dependencies.
5. Deploy a Vercel preview, test the actual workflow, and prepare production cutover and recovery.

Use staging for the first rehearsal. These are teaching materials, not evidence that a live application has been migrated or deployed. Production cutover requires the reviewed plan and its verification checkpoints.
