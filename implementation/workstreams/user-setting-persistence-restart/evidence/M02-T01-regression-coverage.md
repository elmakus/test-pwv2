# M02-T01 execution evidence — non-destructive regression coverage

Implementation under test remained unchanged during this Card:
- `app/settings_store.py` blob: `3eacea45aae1e0fc224bc5f8850189c6b34be70d`

Test surface updated:
- `tests/test_settings_persistence.py`
- final test-only implementation commit for this Card: `028bd2d70fe26192f62346abc807ea8df5dc9693`

Coverage now encodes:
1. a pre-existing settings set with multiple unrelated values plus an unknown/custom key;
2. changing exactly one setting and requiring the complete set to survive restart;
3. preservation of unrelated/unknown values;
4. simulated failure while writing the staged file;
5. simulated failure while atomically promoting the staged file to the durable path;
6. restart after either failed write stage preserving the last known-good durable set rather than defaults.

Pre-fix execution against the still-buggy application:
- 3 tests run;
- interrupted staged-write preservation: PASS;
- successful-save restart durability: expected FAIL;
- atomic-promotion failure behavior: expected FAIL because the buggy implementation never attempts a promotion primitive;
- the restart failure is specifically `theme: light` instead of accepted `theme: dark`;
- unrelated values, including `custom_threshold = 7`, remain represented.

Gate M2 result: GREEN for test-first coverage. The two RED cases are intentional pre-fix evidence and define the M3 acceptance surface.
