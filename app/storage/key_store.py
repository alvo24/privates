import json
from pathlib import Path


class KeyStore:
    def __init__(self, path: str = ".keys.json") -> None:
        self.path = Path(path)
        if not self.path.exists():
            self.path.write_text("{}", encoding="utf-8")

    def save(self, platform: str, account_id: str, payload: dict) -> None:
        records = self._read_all()
        records.setdefault(platform, {})[account_id] = payload
        self.path.write_text(json.dumps(records, indent=2), encoding="utf-8")

    def _read_all(self) -> dict:
        return json.loads(self.path.read_text(encoding="utf-8"))
