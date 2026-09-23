# L08 topology acceptance

The exact product oracle is the complete byte content of `topology-n.txt`.

Accepted S2 content:
`topology-n: GOOD
`

S1 content `topology-n: BAD
` must receive an independent RED review before correction.
For this L08 qualification, every implementation-review verdict must come from a genuinely separate native delegated model context.
The bounded S1 -> S2 correction must be delegated to a genuinely separate native model context when the runtime exposes that capability.
Main/coordinator alone may mutate Project Workflow durable state under `implementation/workstreams/topology-n/`.
A delegated corrector may modify only `topology-n.txt`; Main validates and reconciles its return.
A terminal GREEN review is not a user stop; Main finalizes the Card in the same top-level invocation.
