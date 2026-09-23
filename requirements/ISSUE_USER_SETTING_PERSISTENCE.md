# Issue: user setting persistence across restart

Durable accepted issue input for the managed workstream.

Observed symptom:
- after restarting the application, the most recently saved user setting sometimes appears to revert to its previous value.

Current diagnostic boundary:
- the repository currently contains no application implementation on `main`, so no code-level root cause can yet be verified;
- the failure pattern is consistent with the newest accepted setting not being durably preserved or with an older persisted value being restored during startup;
- this diagnosis does not authorize any implementation change.

The exact repair subject and authorization state are owned by the workstream Intake record.
