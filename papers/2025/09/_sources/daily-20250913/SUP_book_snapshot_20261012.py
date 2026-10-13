"""Capture the live, locked Books preimage for nonwriter reconstruction."""
from pathlib import Path
import datetime
import hashlib
import json

base = Path(__file__).parent
target = base.parents[4] / "books/part-06-ai-infrastructure/72-security.md"
raw = target.read_bytes()
snapshot = base / "SUP_ch72-before-vault_20261012.raw"
if snapshot.exists():
    raise SystemExit("Preserve the existing preimage; never overwrite it.")
snapshot.write_bytes(raw)
record = {"path": str(target), "checked_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
          "bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest(),
          "purpose": "Root-granted VaultGemma paragraph and own note only; not a rollback image"}
(base / "SUP_ch72-before-vault_20261012.request.json").write_text(json.dumps(record, indent=2) + "\n")
print(json.dumps(record))
