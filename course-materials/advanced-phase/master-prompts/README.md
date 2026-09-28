# Master prompts: from idea to working app

**Version: September 28, 2026. Revised against the original mobile app and Content Studio Codex conversations and project files.**

Start with your idea, customize one prompt, and work through the build with your coding agent. The shared method is **plan → design → clickable interface → test → connect services → release and verify**. The mobile prompt preserves the actual class checkpoints: the browser-local prototype was deployed before authentication and cloud tracking were added. See [what was built in Codex](class-build-notes.md).

## Choose your prompt

| What you want to build | Copy this prompt |
|---|---|
| A mobile-first app following the class's React/Vite prototype, then Supabase and Vercel workflow | [Mobile app master prompt](mobile-app-master-prompt.md) |
| A website, landing page, or web application | [Website and web app master prompt](website-web-app-master-prompt.md) |
| The class Content Studio project, either from scratch or from an existing prototype | [Content Studio master prompt](content-studio-master-prompt.md) |

Each file contains one complete prompt. You do not need to paste all three or combine them with another file.

## How to use them

1. Open the intended project folder in Codex or your coding agent. For a new project, start with an empty folder. For an existing project, keep its files and history.
2. Open the matching prompt. Replace the bracketed fields in **My project**. If you do not know an answer, write `Help me choose`. Choose `None` for features you do not need.
3. Copy the entire text block into your agent. Start with a small first version: one audience, one main task, and three essential features.
4. Review the plan and design options. Select a direction, then let the agent complete the agreed stage and its checks.
5. Test the actual workflow yourself. Read the evidence and unresolved items before moving to deployment.

The prompts default to local work and preparation. Fill in the release fields when you are ready to authorize a GitHub push or preview deployment. A production release, paid service, destructive migration, or app-store submission needs a specific decision. If you already authorized a stage, the agent should continue without repeatedly asking.

## Tools and accounts

- **Coding agent:** Codex or another agent that can inspect and edit your project.
- **Demonstrated mobile frontend:** React, TypeScript, Vite, Tailwind CSS and shadcn. Start with a clickable browser-local MVP, then connect accounts and cloud persistence.
- **Design:** Impeccable when installed and available. If it is missing, the agent should explain that and use a written design system while setup is resolved.
- **Current documentation:** Context7 when available, with official documentation as the fallback. The agent must verify the installed tool's commands instead of copying uncertain transcript wording.
- **Source history:** Git locally, plus a GitHub repository when you are ready to push.
- **Database and sign-in:** Supabase for projects that need persistent user data or accounts. A simple informational website may not need it.
- **Web hosting:** Vercel for the website or web build, with the intended GitHub repository connected.
- **Optional later native development:** Expo and a physical phone. This was discussed as a next step, not used in the demonstrated Vite build. Use Expo Go for compatible Expo projects and a development build when custom native functionality requires it.
- **AI generation:** A configured model provider and an agreed usage budget, only when the product needs live generation. Enter secrets in local or hosted secret settings, never in chat or Git.

Use your own authorized accounts. The instructor's Miami AI School organization is not a required or automatically available student environment.

## What was promised in class

| Transcript time | Commitment | Included here |
|---|---|---|
| 12:05–12:52 | Generic master prompts for a mobile app and a website/web app, customizable for new projects | Mobile and website/web-app prompts |
| 36:50–37:06 | A master prompt for Content Studio as well | Content Studio prompt, including a migration path |
| 38:10–39:23 | Plan, design screens, test and revise, add Supabase and authentication, connect GitHub and Vercel | The shared build method, with the mobile project's actual intermediate deployment retained |

The supplied transcript is the source for these commitments. The mobile and Content Studio prompts were also checked against their original Codex conversations and actual project files. The full conversations, participant details and account identifiers are not included in this public repository. The website prompt generalizes the same method; it is not presented as a third completed class build.

## Clarifications from the demo

A responsive website can work well on a phone without being a native app. Opening an existing website in Expo Go does not convert it into a native app. The mobile prompt makes that choice explicit before building.

Supabase provides backend services, including its database and authentication. A separate custom server may be unnecessary, but having a database does not prove sign-in or user isolation works.

A successful build, a pushed commit, and a working hosted user journey are different results. GitHub pushes trigger Vercel deployments only when the integration and branch settings support them. The agent must verify the actual deployment.

These are reviewed teaching prompts. They have not been executed end to end to produce three new applications. See [technical references and verification notes](references.md).

## Related materials

- [Design, migrate and deploy workbook](../design-migrate-deploy/workbook.md): detailed migration rehearsal and release steps.
- [Session 2 build prompts](../session-02/build-prompts.md): the earlier Sites-based classroom path.
- [Advanced Phase index](../README.md).

The earlier Sites prompts remain useful for that session. This set adds the later Supabase, GitHub and Vercel path demonstrated in class.
