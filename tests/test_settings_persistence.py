from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from app.settings_store import SettingsStore


class SettingsPersistenceRegressionTests(unittest.TestCase):
    def test_latest_successful_save_survives_restart_without_changing_other_settings(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "settings.json"
            initial = {
                "theme": "light",
                "language": "pl",
                "notifications": True,
            }
            path.write_text(json.dumps(initial) + "\n", encoding="utf-8")

            store = SettingsStore(path)
            self.assertTrue(store.save_setting("theme", "dark"))
            self.assertEqual(store.get("theme"), "dark")
            self.assertEqual(store.get("language"), "pl")
            self.assertTrue(store.get("notifications"))

            restarted = SettingsStore(path)
            expected = dict(initial)
            expected["theme"] = "dark"
            self.assertEqual(restarted.snapshot(), expected)


if __name__ == "__main__":
    unittest.main()
