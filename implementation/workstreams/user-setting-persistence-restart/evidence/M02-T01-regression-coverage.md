# M02-T01 execution evidence — non-destructive regression coverage

Implementation under test remained unchanged during this Card:
- `app/settings_store.py` blob: `3eacea45aae1e0fc224bc5f8850189c6b34be70d`

Test surface updated:
- `tests/test_settings_persistence.py`
- test-only implementation commit: `ca005bd1a44bc931835cdc20a3e3d8e322e31540`

Coverage now encodes:
1. a pre-existing settings set with multiple unrelated values plus an unknown/custom key;
2. changing exactly one setting and requiring the complete set to survive restart;
3. preservation of unrelated/unknown values;
4. simulated interrupted write via `Path.write_text` failure;
5. restart after write failure preserving the last known-good durable set rather than defaults.

Pre-fix execution against the still-buggy application:
- 2 tests run;
- interrupted-write preservation test: PASS;
- successful-save restart test: expected FAIL;
- failure is specifically `theme: light` after restart instead of accepted `theme: dark`;
- unrelated values, including `custom_threshold = 7`, remain present.

Gate M2 result: GREEN for test-first coverage. The regression remains intentionally RED until the behavioral repair Card.
