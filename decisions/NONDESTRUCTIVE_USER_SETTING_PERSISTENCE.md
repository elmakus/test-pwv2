# Decision: non-destructive user setting persistence

Source scope: `safe-user-setting-persistence@2`.
Authorized repair: `repair:user-setting-persistence-nondestructive:v2`.

Accepted guarantees:
- all existing user settings are preserved;
- updating one setting does not modify unrelated settings;
- an interrupted or failed write cannot destroy the last known-good persisted state;
- startup does not perform a destructive reset or migration of settings;
- regression coverage verifies the whole settings set across save, restart, and reload.

The concrete storage, write, migration, and recovery mechanism is intentionally not selected here. Strategic Planning must choose an implementation consistent with these guarantees and the available application architecture.
