# Strategic Plan — Non-destructive user setting persistence

Planning cycle: 1  
Entry subject: `definition:R1|planning-cycle:1`  
Definition source: `safe-user-setting-persistence@2`  
Authorized repair: `repair:user-setting-persistence-nondestructive:v2`

## Objective

Fix the restart regression so the newest successfully saved user setting is restored after restart without losing, resetting, or modifying unrelated settings.

## Accepted authority coverage

The plan preserves every accepted v2 guarantee:
- existing settings remain intact;
- changing one setting cannot alter unrelated settings;
- failed/interrupted writes cannot destroy the last known-good persisted state;
- startup must not perform destructive reset or migration;
- regression coverage verifies the complete settings set across save, restart, and reload.

No new product behavior, schema migration, storage-backend replacement, or settings reset is authorized.

## Strategy

### M1 — Bind the repair to the real persistence path

Before changing persistence behavior, identify the existing application path for:
1. reading settings at startup;
2. writing one changed setting;
3. reporting a save as successful;
4. applying defaults or migrations;
5. recovering from an interrupted/failed write.

Execution Prep must bind implementation work to those concrete files/APIs. If the application implementation is still unavailable, implementation remains blocked rather than inventing framework-specific behavior.

Gate M1:
- the current read/write/startup path is identified from project evidence;
- the failure can be represented by a reproducible test or fixture;
- no mutation has occurred yet.

### M2 — Establish non-destructive regression coverage first

Add or extend tests that begin with multiple pre-existing settings, change exactly one value, persist it, restart/reload, and verify:
- the changed value is the newest accepted value;
- every unrelated setting is byte-/value-equivalent as appropriate;
- no default reset occurred.

Add failure-path coverage appropriate to the existing persistence abstraction:
- simulated interrupted or rejected write leaves the last known-good state readable;
- startup after that failure does not replace it with defaults.

Gate M2:
- the current bug is reproduced or the previously missing safety behavior is demonstrably uncovered;
- tests encode the full v2 guarantees before the behavioral fix is accepted.

### M3 — Apply the smallest compatible persistence repair

Use the application's existing persistence abstraction and backend. Do not introduce a new storage system merely to solve this issue.

The implementation must:
- preserve the complete existing settings state when updating one setting;
- only acknowledge save success after the backend's durable/atomic commit boundary;
- use the backend's existing transactional/atomic replacement primitive where available;
- preserve unknown/unrelated keys or fields;
- avoid destructive schema migration or default reinitialization on normal startup;
- restore the last committed state after restart.

If the existing backend has no safe atomic/transactional primitive, Execution must stop and surface that as a bounded technical blocker rather than weakening the accepted guarantees.

Gate M3:
- implementation changes are limited to the verified persistence/startup path;
- no destructive migration/reset is introduced;
- failure handling preserves last known-good state.

### M4 — Verify restart and failure semantics

Run the narrow regression suite plus the relevant surrounding settings/persistence tests. Verify at minimum:
1. existing settings set -> modify one value -> save -> restart/reload -> full set preserved;
2. save failure/interruption -> restart/reload -> last known-good full set preserved;
3. unrelated settings remain unchanged;
4. defaults are used only under the application's already-authorized missing/first-run semantics, not as recovery from this bug.

If project tooling supports it, run the broader test suite covering startup/settings persistence before completion.

Gate M4:
- all required regression tests pass;
- no known data-loss path remains inside the changed surface;
- observed behavior matches the v2 authority.

## Execution structure

Execution Prep should materialize bounded Cards from these milestones after it can inspect the real application code. A likely decomposition is:
- Card 1: bind persistence path and regression harness (M1–M2);
- Card 2: implement minimal non-destructive persistence fix (M3), dependent on Card 1 evidence;
- Card 3: full verification and restart/failure regression pass (M4), dependent on Card 2 result.

The exact file paths and technical API calls are intentionally JIT-bound to repository evidence so the workflow does not guess an architecture that is not present.

## Risk controls

- No storage-backend replacement.
- No schema reset.
- No destructive migration.
- No blanket overwrite from defaults.
- No partial-settings write that drops unrelated keys.
- No claim of successful save before the durable commit boundary.
- Any incompatibility with the existing backend becomes an explicit blocker, not a silent relaxation of safety requirements.

## Planner audit

Requirement coverage: complete.  
Decision coverage: complete.  
Milestone dependencies: explicit.  
Safety gates: explicit.  
Known limitation: application implementation is not currently present in this consumer repository, so concrete file/API binding is deferred to Execution Prep and must fail closed if still unavailable.

Planner audit result: GREEN.
