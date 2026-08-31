#!/usr/bin/env python3
"""Check or refresh SHA256SUMS-style research manifests.

Manifest path spellings are preserved.  Only the digest is rewritten, and only
when the referenced artifact can be resolved unambiguously from the packet or
repository root.  This keeps presentation-only migrations from silently
invalidating frozen evidence packets.
"""

from __future__ import annotations

import argparse
import hashlib
import re
from pathlib import Path


LINE = re.compile(r"^([0-9a-f]{64})  (.+)$")
ROOT_PREFIXES = {"books", "docs", "labs", "papers", "scripts", "tests"}


def resolve_reference(reference: str, manifest: Path, root: Path) -> Path | None:
    path = Path(reference)
    if path.is_absolute():
        return path if path.exists() else None
    if reference.startswith("./") or reference.startswith("../"):
        candidate = (manifest.parent / path).resolve()
        return candidate if candidate.exists() else None
    if path.parts and path.parts[0] in ROOT_PREFIXES:
        candidate = (root / path).resolve()
        return candidate if candidate.exists() else None
    local = (manifest.parent / path).resolve()
    if local.exists():
        return local
    repository = (root / path).resolve()
    return repository if repository.exists() else None


def process_manifest(manifest: Path, root: Path, write: bool) -> tuple[int, list[str]]:
    changed = 0
    errors: list[str] = []
    output: list[str] = []
    for number, line in enumerate(manifest.read_text(encoding="utf-8").splitlines(), 1):
        match = LINE.fullmatch(line)
        if not match:
            errors.append(f"{manifest}:{number}: invalid SHA256SUMS row")
            output.append(line)
            continue
        recorded, reference = match.groups()
        target = resolve_reference(reference, manifest, root)
        if target is None or not target.is_file():
            errors.append(f"{manifest}:{number}: unresolved or ambiguous path {reference!r}")
            output.append(line)
            continue
        actual = hashlib.sha256(target.read_bytes()).hexdigest()
        if actual != recorded:
            changed += 1
            if not write:
                errors.append(
                    f"{manifest}:{number}: stale digest for {reference!r}: "
                    f"recorded={recorded} actual={actual}"
                )
        output.append(f"{actual if write else recorded}  {reference}")
    if write and changed and not errors:
        manifest.write_text("\n".join(output) + "\n", encoding="utf-8")
    return changed, errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=Path, help="manifest file or directory containing manifests")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()

    target = args.path.resolve()
    manifests = [target] if target.is_file() else sorted(target.rglob("SHA256SUMS*"))
    changed = 0
    errors: list[str] = []
    for manifest in manifests:
        manifest_changed, manifest_errors = process_manifest(
            manifest, args.root.resolve(), args.write
        )
        changed += manifest_changed
        errors.extend(manifest_errors)
    for error in errors:
        print(f"ERROR: {error}")
    action = "refreshed" if args.write else "checked"
    print(f"{action} manifests={len(manifests)} changed={changed} errors={len(errors)}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
