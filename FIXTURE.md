# Disposable persistence fixture

This repository fixture exists only to complete the PWv2 Android L02/L03 live validation path.

It supplies the previously missing application input for the active issue workstream:
- startup reads from `app/settings_store.py`;
- one-setting writes use `SettingsStore.save_setting`;
- the current implementation intentionally reproduces the reported restart regression;
- `tests/test_settings_persistence.py` is the reproducible regression surface.

The fixture commit is external test input, not the accepted repair. It intentionally leaves the regression failing so the active PWv2 workstream must diagnose/implement/review the authorized non-destructive repair itself.
