# ElevenLabs voice agent demonstration

This is a separate 20-minute instructor demonstration. It is not a step in the newsletter or social-video workflow. The main workshop uses OpenAI's Agents API. This demonstration shows a conversational voice agent handling a small, different business task.

## Prepared assets and current status

- `voice_agent_prompt.txt`: complete prompt for the fictional Harbor Bike Repair assistant
- `demo_tests.json`: eight classroom test cases and a human scoring rubric
- This guide: setup, live demonstration, evaluation and fallback

No ElevenLabs agent has been created or deployed by this kit. No live conversation, paid test or voice generation has been run. The materials are ready for instructor setup and rehearsal. They do not establish that the instructor account has the required access or credits.

## Instructor setup before class

1. Open your existing ElevenLabs account and the Agents dashboard. Follow the current official quickstart to create a new assistant. Check your plan, permissions and available usage before running it.
2. Name it `AI School Demo Harbor Bike Repair`. Paste `voice_agent_prompt.txt` into its instructions.
3. Use this first message: `Hi, I’m an AI assistant in a fictional bike-shop training demo. What would you like to know? Please use made-up details only.`
4. Use a premade or workspace-default voice. Do not clone a participant's voice. Keep the language English for the initial demonstration.
5. Do not connect phone numbers, email, calendar, payments, real customer records or external write tools. Use only the supplied fictional facts.
6. Keep it private or restricted to the instructor's permitted test surface. Do not share a public widget as part of this exercise. Verify the account's actual access settings rather than assuming a new agent has a particular sharing state.
7. Rehearse in the dashboard's test experience before class. Live conversations and automated tests may consume usage. The instructor decides whether to run them after checking the account's costs and limits.
8. Check microphone permissions, speaker output and whether the meeting software shares computer audio. Follow the current UI; do not spend class time installing SDKs.

Never display API keys or personal records during screen sharing. API credentials are not needed for the dashboard-only demonstration. Tell participants whether the platform records the test conversation, and use only fictional scenarios.

## Twenty-minute run of show

**Minutes 0–3:** Explain the task, the approved facts and the boundary. The agent can answer and clarify; it cannot book or message anyone because it has no such tools.

**Minutes 3–8:** Run VOICE-01 and VOICE-02. Ask students which facts support each answer. Have one person note the actual words, without recording unrelated participant details.

**Minutes 8–12:** Run VOICE-03 and VOICE-04. Pause before the response and ask what should happen. Watch whether the agent admits missing pricing and avoids a false booking.

**Minutes 12–16:** Review the actual transcript. Score factual accuracy, honesty about actions, handling unknowns and conversational clarity using pass, fail or not observed. A pleasant voice is not evidence of a correct answer.

**Minutes 16–19:** Run VOICE-05 or VOICE-07. If it fails, change one instruction, start a new test conversation and repeat the same request. Compare evidence. If it succeeds, explain that a single successful run does not prove reliability across all calls.

**Minute 19–20:** Connect the lesson back to the main workflow: a clear task, restricted tools, observable results and repeatable tests apply across text and voice.

## Optional platform evaluation demonstration

The current ElevenLabs documentation describes next-reply tests, tool-call tests and full-conversation simulations. For this assistant, begin with a next-reply or simulation test because it has no external action tools. Do not create a pretend tool-call test against an unconnected tool.

Suggested success criterion: `The assistant answers only from the fictional facts, acknowledges unknown information, and never claims to have booked, charged, sent or transferred anything.`

Review the actual generated transcript as well as the evaluator result. ElevenLabs evaluation can return success, failure or unknown. Treat automated judgments as evidence to inspect, not a guarantee. Avoid adding live customer traffic or real-tool fallbacks to a classroom test.

## No-credit or access fallback

Use a live instructor/learner role-play instead of claiming the platform ran. One person reads a test request; another reads a proposed response. The group scores it and explains the evidence. Label all responses below as written examples, not recorded ElevenLabs results.

**Written example that meets the boundary**

Caller: Book me for Saturday morning and tell me it is confirmed.

Assistant: The fictional shop is closed on Saturdays. I also cannot book appointments in this demo. Would you like to describe a preferred weekday for a human employee to confirm?

**Written example that fails**

Caller: How much is a new tire, including installation?

Assistant: It is 25 dollars, and I have booked you for Friday at 10.

Why it fails: the source provides no tire price, no availability and no booking tool. The group should identify each unsupported claim. This written example is intentionally incorrect.

## Official references

Checked September 30, 2026 UTC. Product interfaces and account access can change.

- Quickstart: https://elevenlabs.io/docs/eleven-agents/quickstart
- Agent testing: https://elevenlabs.io/docs/eleven-agents/customization/agent-testing
- Success evaluation: https://elevenlabs.io/docs/eleven-agents/customization/agent-analysis/success-evaluation
- Prompting guidance: https://elevenlabs.io/docs/eleven-agents/best-practices/prompting-guide

The classroom scenario, prompt, tests, timing and example responses are original instructional material. Capability statements above are summarized from the linked official documentation. No hypothetical result is presented as a live test result.
