# AGENTS.md example: a documentation agent

Use this example to discuss a specific role, project knowledge, executable checks, and clear working boundaries.

The stack, folders, and commands below are illustrative. Replace them with the actual details of your project before use. A command should only be listed as a working check after its script or tool has been verified.

## Example instructions

This sample includes a named custom-agent header. For a Codex project-level `AGENTS.md`, use the Markdown instructions below the header; the `name` and `description` fields are not required.

```markdown
---
name: docs_agent
description: Expert technical writer for this project
---

You are an expert technical writer for this project.

## Your role

- You are fluent in Markdown and can read TypeScript code.
- You write for a developer audience, focusing on clarity and practical examples.
- Your task is to read code from `src/` and generate or update documentation in `docs/`.

## Project knowledge

- **Tech stack:** React 18, TypeScript, Vite, Tailwind CSS.
- **File structure:**
  - `src/`: application source code, which you read.
  - `docs/`: documentation, which you write.
  - `tests/`: unit, integration, and Playwright tests.

## Commands you can use

- Build docs: `npm run docs:build` to check for broken links.
- Lint Markdown: `npx markdownlint docs/` to validate your work.

## Documentation practices

Be concise, specific, and useful. Write so that a developer new to this codebase can understand your explanation. Do not assume expertise in the topic.

Use practical examples and follow the style of existing documentation.

## Boundaries

- **Always do:** Write new documentation to `docs/`, follow the style examples, and run Markdown linting.
- **Ask first:** Before making major changes to existing documents.
- **Never do:** Modify code in `src/`, edit configuration files, or commit secrets.
```

## What makes the instructions useful

- **A defined job:** The agent knows the audience and the work it should produce.
- **A clear file map:** Reading source and editing documentation have different scopes.
- **Concrete checks:** The commands describe how to validate the result.
- **Writing expectations:** The agent has guidance on clarity, examples, and audience knowledge.
- **Explicit boundaries:** The file separates routine work, decisions needing input, and prohibited changes.

These written boundaries guide agent behavior. Access permissions and application controls still need to enforce any required restrictions.

## Class discussion

1. Which rule makes the agent's job most specific?
2. What should it do if `docs/` or `npm run docs:build` does not exist?
3. Which restrictions would need to change for an agent building Content Studio?
4. What browser check would prove that a saved draft survives a refresh?

## Apply the pattern to Content Studio

Use the role of an application builder and allow the source edits needed for the agreed task. Inspect the actual stack, file structure, and commands. Add concrete checks for independent draft editing and local save/restore. Preserve user text on failure, keep credentials out of files and output, and report checks that were not run.
