from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from app.settings_store import SettingsStore


class SettingsPersistenceRegressionTests(unittest.TestCase):
    def test_latest_successful_save_survives_restart_without_changing_other_settings(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "settings.json"
            initial = {
                "theme": "light",
                "language": "pl",
                "notifications": True,
                "custom_threshold": 7,
            }
            path.write_text(json.dumps(initial) + "\n", encoding="utf-8")

            store = SettingsStore(path)
            self.assertTrue(store.save_setting("theme", "dark"))
            self.assertEqual(store.get("theme"), "dark")
            self.assertEqual(store.get("language"), "pl")
            self.assertTrue(store.get("notifications"))
            self.assertEqual(store.get("custom_threshold"), 7)

            restarted = SettingsStore(path)
            expected = dict(initial)
            expected["theme"] = "dark"
            self.assertEqual(restarted.snapshot(), expected)

    def test_interrupted_write_preserves_last_known_good_settings_on_restart(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "settings.json"
            initial = {
                "theme": "light",
                "language": "pl",
                "notifications": True,
                "custom_threshold": 7,
            }
            path.write_text(json.dumps(initial) + "\n", encoding="utf-8")

            store = SettingsStore(path)
            with patch.object(Path, "write_text", side_effect=OSError("simulated interrupted write")):
                with self.assertRaises(OSError):
                    store.save_setting("theme", "dark")

            restarted = SettingsStore(path)
            self.assertEqual(restarted.snapshot(), initial)
            self.assertEqual(restarted.get("custom_threshold"), 7)


if __name__ == "__main__":
    unittest.main()
