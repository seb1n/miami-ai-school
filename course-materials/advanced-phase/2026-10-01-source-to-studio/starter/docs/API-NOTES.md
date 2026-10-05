# API contract notes

Verified against official OpenAI documentation on 30 September 2026. The adapter was mock-tested; no API credentials or paid live requests were used.

- [Managed Agents API quickstart](https://developers.openai.com/api/docs/guides/agents-api/quickstart): session creation, application key permissions and `OpenAI-Beta: agents=v1`
- [Architecture](https://developers.openai.com/api/docs/guides/agents-api/architecture): managed Codex harness, application-server tools and no-environment sessions
- [Functions](https://developers.openai.com/api/docs/guides/agents-api/tools/functions): `agent.tools`, `required_actions`, function arguments and result submission
- [Sessions](https://developers.openai.com/api/docs/guides/agents-api/sessions): creation, follow-up inputs, saved items and cancellation
- [Events and items](https://developers.openai.com/api/docs/guides/agents-api/sessions/events): root turn outcomes, idle/stream disconnect semantics and saved-state recovery

## Boundaries

The classroom application handles workflow state locally. Live generation creates one managed session for one bounded package. `environment.type=none` intentionally avoids a hosted compute sandbox; custom function handlers run in the application server. The API key exists only in that server's process environment and authenticated HTTP header. It is not sent to the model, exposed by config endpoints or inserted into an agent environment.

Only `get_source_pack` and `submit_content_package` are declared. Unknown tools receive an error, and submission before source-read is rejected. Shape errors can be corrected through another tool call (maximum six calls). All draft content still needs human factual review. The local renderer receives caption text, never executable code from the agent.

POST session creation is never automatically retried after ambiguity. Known session state and one saved-items page are read for recovery context, then cancellation is requested if possible. The app reports uncertainty and retains the session identifier in its error. It does not pretend cancellation is confirmed, resume pending calls across restarts, or delete remote session data automatically. Instructors must inspect remote history if a live failure is ambiguous.

No new credentials are created, installed, configured or transmitted by the delivered preparation process. The live feature remains opt-in for a later authorized instructor test.
