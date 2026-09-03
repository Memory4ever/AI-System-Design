#!/usr/bin/env python3
"""Run the audited semantic-denominator builder with a date-local route file."""

from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
HERE = Path(__file__).resolve().parent


def main() -> None:
    ap = argparse.ArgumentParser(); ap.add_argument("date"); ap.add_argument("routes_json")
    args = ap.parse_args(); compact = args.date.replace("-", "")
    cfg = json.loads(Path(args.routes_json).read_text(encoding="utf-8"))
    spec = importlib.util.spec_from_file_location("semantic_builder", HERE / "rebuild_day_20260715_semantic.py")
    module = importlib.util.module_from_spec(spec); assert spec.loader; spec.loader.exec_module(module)
    module.PACKET = ROOT / f"papers/{args.date[:4]}/{args.date[5:7]}/_sources/daily-{compact}"
    module.REPORT_DATE = args.date; module.RUN_AT = cfg["run_at"]
    module.ROUTES = "\n".join("|".join((aid, *values)) for aid, values in cfg["routes"].items())
    module.STANDARD = set(cfg.get("standard", []))
    module.main()


if __name__ == "__main__": main()
