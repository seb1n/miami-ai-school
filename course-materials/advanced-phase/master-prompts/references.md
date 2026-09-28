# Technical references and verification notes

**Reviewed: September 28, 2026**

The prompts combine commitments from the supplied class transcript with implementation guidance. They are reusable instructions, not generated application code or a guarantee of deployment. Recheck current documentation when starting a project.

## Sources used

| Source | How it informs the prompts |
|---|---|
| [Expo environment setup](https://docs.expo.dev/get-started/set-up-your-environment/) and [development builds](https://docs.expo.dev/tutorial/eas/configure-development-build/) | Expo Go is suitable for compatible learning projects; development builds support custom native dependencies. Test the selected native runtime and keep store distribution separate from web hosting. |
| [Supabase API keys](https://supabase.com/docs/guides/getting-started/api-keys) | Client publishable keys and privileged server secrets have different purposes. Never expose secret or service-role keys in a browser or mobile bundle. |
| [Supabase row-level security](https://supabase.com/docs/guides/database/postgres/row-level-security) | Database grants and row policies must reflect the actual access model. Verify allowed and denied operations with real user roles. |
| [Vercel Git deployments](https://vercel.com/docs/git) | Connect the repository and confirm Preview and Production branch behavior. Check the deployment associated with the intended source revision. |
| [Impeccable](https://impeccable.style/) | Design skills support both new interfaces and improvements to existing ones. Verify availability in the selected coding agent before claiming to use them. |
| [Context7 documentation](https://context7.com/docs/overview) | Retrieve current documentation for implementation decisions. Use the actual supported setup flow rather than the transcript's uncertain phonetic command. |

Expo, Supabase and Vercel guidance was also checked through Context7. React/TypeScript, Next.js for a fresh web app, and Expo for a native app are recommended starting choices in these prompts, not a claim that the transcript established every framework or package version.

## Review scope

- Matched the three prompt deliverables to the transcript commitments at 12:05–12:52 and 36:50–37:06.
- Preserved the plan, design, interface testing, backend and release sequence described at 38:10–39:23.
- Kept the existing Sites classroom path intact and linked the later migration workbook.
- Included separate checks for data persistence, user isolation, live generation, device behavior and hosted operation where applicable.
- Kept account destinations and credentials out of reusable public instructions.
- Reviewed repository links, formatting and consistency before upload.

No new student application, account, database or deployment was created to validate these prompts end to end. Physical-device testing, live model calls, email delivery and production releases must be verified in each student's project.
