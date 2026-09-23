# M01-T01 execution evidence — persistence path binding

Input commit inspected: `a945251f80023864ca71abcdea82fd9ad063f4f5`.

## Bound persistence/startup surface

- Startup read: `SettingsStore.__init__` calls `SettingsStore._load_at_startup()` in `app/settings_store.py`; if the durable JSON file exists it is parsed directly, otherwise `DEFAULT_SETTINGS` is copied.
- One-setting write: `SettingsStore.save_setting(key, value)` copies the complete in-memory settings map, updates exactly one key, and serializes the complete updated map.
- Current save-success boundary: `save_setting` writes only `<settings>.pending`, updates in-memory state, then returns `True`. It does not promote the pending file to the durable path used by restart.
- Defaults/migrations: there is no migration path in the fixture. Defaults are used only when the durable settings file does not exist.
- Failed/interrupted write recovery: no recovery/promotion primitive currently exists; restart reads only the durable settings path and ignores the staged pending file.
- Regression surface: `tests/test_settings_persistence.py`.

## Reproduction

The exact fixture was executed with Python unittest discovery before any repair mutation.

Observed result: 1 test run, 1 failure.

The failure is the expected restart regression: after `save_setting("theme", "dark")` returns success, a new `SettingsStore` instance reloads `"theme": "light"` from the unchanged durable file instead of the accepted `"dark"` value. The unrelated `language` and `notifications` values remain present.

## Gate M1

GREEN:
- concrete read/write/startup paths identified;
- false save-success durability boundary identified;
- defaults/migration behavior identified;
- lack of failed-write recovery identified;
- reproducible regression harness identified and observed failing;
- no application mutation performed by this Card.
