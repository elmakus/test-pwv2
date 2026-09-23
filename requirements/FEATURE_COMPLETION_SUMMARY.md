# Feature Completion Summary

Durable accepted product intent for the managed feature.

When work on a feature reaches successful Project Workflow completion, the project should automatically produce a short completion summary.

The summary must include:
- the most important changes;
- tests that were executed;
- any remaining work or follow-up items.

Accepted output behavior:
- persist the summary as a durable `COMPLETION_SUMMARY.md` artifact inside the completed workstream;
- present the same concise summary to the user as part of the final completion response;
- derive both representations from the same verified completion evidence so they do not diverge.

The durable artifact is intended to preserve an auditable cross-session record while the user-facing rendering provides the immediate completion report.

Exact implementation mechanics remain subject to Project Workflow V2 Definition and Planning.
