# Final Close handoff

Date: 2026-09-23
Workstream: topology-n-chatgpt
State: terminal pre-integration package

Integration target refresh: `main` at `a31047259c92a7c6a6054a1b9bf618fc0f6ac69a`.
The target is unchanged from the workstream creation base and the branch is ahead with no target-side divergence.

Accepted implementation:
- commit `d9a99ec3d835234bfe4baa10974386bbc0ff50ab`;
- `topology-n-chatgpt.txt` blob `3a446f6d934b2e63c0466e9f7b2bb596fa416268`;
- exact bytes `topology-n: GOOD\n`;
- frozen M01-T01 result: commit `124a2945dcc7e28e3f7de64f53b48a9d0e41a6d1`, blob `482bfb90e65bd5d9735ae09cb2e59999e11004b4`;
- M01-T01-R01 remains append-only RED;
- M01-T01-R02 independent review is GREEN with evidence at `implementation/workstreams/topology-n-chatgpt/evidence/M01-T01-independent-review-R02.md`.

`TASK_BOARD.toml` revision 3 has the single M01-T01 Card `done` with the exact frozen result and both review attempts preserved.

Close refresh verification:
- exact reviewed product blob and behavior are unchanged;
- Project Workflow V2 `tools/close_contract.py` classifies GREEN review coverage as `reuse_green_review`;
- merge-tree against refreshed `main` is conflict-free;
- `git diff --check` is clean;
- exact byte readback is GREEN;
- repository regression suite is GREEN 3/3;
- production router routes the terminal board to `close`;
- temporary verification checkout is clean after test artifacts are removed.

The complete known recovery package is present on the source branch before integration: workstream identity/provenance, Task Board, stable Card, exact result, authority, S1/S2 evidence and both append-only review attempts/evidence.

Immediately before merge, reread the exact PR head/base and current `main`. After merge, recover from the target-side package plus immutable PR/merge evidence; do not require the source branch for correctness.
