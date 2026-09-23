# L09 N-CHATGPT topology acceptance

The exact product oracle is the complete byte content of `topology-n-chatgpt.txt`.

Accepted S2 content:
`topology-n: GOOD
`

Initial S1 content is:
`topology-n: BAD
`

This qualification uses two fresh top-level ChatGPT contexts.

The first fresh context begins from an independent pending review of S1. If that review rejects S1 and the Card remains valid, the same context may perform the bounded correction and freeze a new S2 subject. Because that context then materially repaired S2, it must not independently review S2; it must leave an exact pending review obligation and stop only for the fresh independent context required by the review contract.

The second fresh ChatGPT context begins from that durable pending S2 review. If the exact S2 subject is independently GREEN, GREEN is not a verdict-only stop: the same context finalizes the Card deterministically and continues routing until the next real workflow stop.

Main in each top-level ChatGPT context is the sole Project Workflow durable-state writer. Keep one Card throughout. Review history is append-only. Runtime/model/session identity is not canonical Project Workflow state.
