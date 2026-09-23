from __future__ import annotations

import json
from pathlib import Path


DEFAULT_SETTINGS = {
    "theme": "light",
    "language": "pl",
    "notifications": True,
}


class SettingsStore:
    """Small JSON-backed settings store used only by the PWv2 live fixture.

    The current save path intentionally reproduces the reported restart bug:
    it stages the newest settings and reports success before promoting the
    staged file to the durable settings file.
    """

    def __init__(self, path: str | Path) -> None:
        self.path = Path(path)
        self._settings = self._load_at_startup()

    def _load_at_startup(self) -> dict[str, object]:
        if not self.path.exists():
            return dict(DEFAULT_SETTINGS)
        return json.loads(self.path.read_text(encoding="utf-8"))

    def get(self, key: str) -> object:
        return self._settings[key]

    def snapshot(self) -> dict[str, object]:
        return dict(self._settings)

    def save_setting(self, key: str, value: object) -> bool:
        updated = dict(self._settings)
        updated[key] = value

        # BUG FIXTURE: the write is only staged. The durable file used on
        # restart is never replaced, even though success is returned.
        pending = self.path.with_name(self.path.name + ".pending")
        pending.write_text(
            json.dumps(updated, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        self._settings = updated
        return True
