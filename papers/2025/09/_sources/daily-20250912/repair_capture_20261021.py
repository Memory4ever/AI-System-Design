"""Bounded primary metadata capture for the Sep11 repair, not semantic review."""

import argparse
import datetime as dt
import hashlib
import json
from pathlib import Path
import re
import time
import urllib.error
import urllib.parse
import urllib.request

BASE = Path(__file__).parent
STAMP = "20261021"


def potential_ids():
    def rows(text):
        return [line.split(" | ") for line in text.splitlines() if line.startswith("| ")]

    original = [re.search(r"2509\.\d{5}", cells[0]).group(0)
                for cells in rows((BASE / "SCREEN.md").read_text())
                if re.search(r"2509\.\d{5}", cells[0]) and "建议关闭" not in cells[-1]]
    recovery = (BASE / "RECOVERY_SCREEN.md").read_text().split("## 60 项潜力", 1)[1].split("## 27 项", 1)[0]
    recovered = ["2509." + re.search(r"\d{5}", cells[0]).group(0)
                 for cells in rows(recovery) if re.search(r"\d{5}", cells[0])]
    supplement = [cells[0].strip("| ")
                  for cells in rows((BASE / "SUP_SCREEN_20261012.md").read_text())
                  if cells[-1].strip("| ") == "P"]
    identities = sorted(set(original + recovered + ["2509.09082"] + supplement))
    if len(identities) != 100:
        raise ValueError(f"Unexpected potential set size: {len(identities)}")
    return identities


def capture(name, params=None, *, url=None, extension=".raw.json"):
    body_path = BASE / f"{name}_{STAMP}{extension}"
    request_path = BASE / f"{name}_{STAMP}.request.json"
    if body_path.exists() or request_path.exists():
        raise FileExistsError(name)
    if url is None:
        url = "https://api.datacite.org/dois?" + urllib.parse.urlencode(params)
    record = {"url": url, "params": params, "checked_at": dt.datetime.now(dt.timezone.utc).isoformat()}
    start = time.monotonic()
    request = urllib.request.Request(url, headers={"User-Agent": "AI-System-Design-research", "Accept": "application/vnd.api+json"})
    try:
        response = urllib.request.urlopen(request, timeout=60)
    except urllib.error.HTTPError as error:
        response = error
    except Exception as error:
        record["error"] = repr(error)
        response = None
    if response is not None:
        with response:
            raw = response.read()
            record.update(status=response.status, final_url=response.geturl(), headers=dict(response.headers),
                          bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest())
        body_path.write_bytes(raw)
    record["elapsed_seconds"] = time.monotonic() - start
    request_path.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n")
    print(name, record.get("status"), record.get("bytes"), record.get("error"), flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=["date100", "discover", "complement", "control", "aliases", "exactv1", "core", "current"])
    parser.add_argument("--ids", nargs="+", default=[])
    args = parser.parse_args()
    if args.mode in ("exactv1", "core", "current"):
        if not args.ids or len(args.ids) > 25 or any(not re.fullmatch(r"2509\.\d{5}", identity) for identity in args.ids):
            parser.error("Provide 1 to 25 explicit Sep2025 identities")
        if args.mode == "exactv1":
            params = {"id_list": ",".join(identity + "v1" for identity in args.ids), "max_results": len(args.ids)}
            capture("REPAIR_EXACT_" + args.ids[0], params,
                    url="https://export.arxiv.org/api/query?" + urllib.parse.urlencode(params), extension=".raw")
        elif args.mode == "core":
            for identity in args.ids:
                capture("REPAIR_CORE_" + identity, url="https://arxiv.org/html/" + identity + "v1", extension=".raw")
        else:
            for identity in args.ids:
                capture("REPAIR_CURRENT_" + identity, url="https://arxiv.org/abs/" + identity, extension=".raw")
    elif args.mode == "date100":
        identities = potential_ids()
        for offset in range(0, len(identities), 20):
            batch = identities[offset:offset + 20]
            query = "(" + " OR ".join(f'doi:"10.48550/arxiv.{identity}"' for identity in batch) + ")"
            capture(f"REPAIR_DATE_B{offset // 20 + 1:02d}",
                    {"client-id": "arxiv.content", "query": query, "page[size]": 100})
    elif args.mode == "discover":
        themes = {
            "MODEL": '(titles.title:("language model" OR transformer OR "mixture of experts")) AND descriptions.description:(attention OR architecture OR training OR optimization)',
            "SYSTEM": '(titles.title:("language model" OR LLM OR GPU)) AND descriptions.description:(inference OR communication OR kernel OR serving OR parallel OR training)',
            "MULTI": '(titles.title:("foundation model" OR "world model" OR "vision language" OR "vision-language-action" OR multimodal OR diffusion OR VLA))',
            "AGENT": '(titles.title:("language model" OR LLM OR agent)) AND descriptions.description:(agent OR retrieval OR memory OR safety OR jailbreak)',
        }
        for name, query in themes.items():
            capture("REPAIR_DISCOVER_" + name,
                    {"client-id": "arxiv.content", "query": query + ' AND registered:[2025-09-10T16:00:00Z TO 2025-09-11T15:59:59.999Z]',
                     "page[size]": 100, "sort": "registered"})
    else:
        def text(terms):
            return f"(titles.title:({terms}) OR descriptions.description:({terms}))"

        lm = text('"language model" OR LLM OR transformer OR "mixture of experts"')
        themes = {
            "MODEL": lm + " AND " + text("architecture OR attention OR optimizer OR training OR alignment OR quantization"),
            "SYSTEM": text('"language model" OR LLM OR GPU') + " AND " + text("inference OR communication OR kernel OR serving OR parallel OR training"),
            "MULTI": text('"foundation model" OR "world model" OR "vision language" OR "vision-language-action" OR multimodal OR VLA') + " AND " + text("representation OR generation OR diffusion OR flow OR action OR training OR fusion"),
            "AGENT": text('"language model" OR LLM OR agent') + " AND " + text("agent OR retrieval OR memory OR safety OR jailbreak OR planning"),
        }
        if args.mode == "aliases":
            themes = {
                "LM": text('LM OR "language models"') + " AND " + text("training OR reinforcement OR confidence OR calibration OR alignment"),
                "VLM": text('VLM OR MLLM OR "vision-language" OR "vision-language models"') + " AND " + text("representation OR evaluation OR reasoning OR navigation OR action OR fusion"),
            }
        if args.mode == "control":
            themes = {"MODEL": themes["MODEL"] + ' AND doi:"10.48550/arxiv.2509.08755"'}
        prefix = {"control": "REPAIR_CONTROL_", "aliases": "REPAIR_ALIAS_"}.get(args.mode, "REPAIR_COMPLEMENT_")
        for name, query in themes.items():
            capture(prefix + name,
                    {"client-id": "arxiv.content", "query": query + ' AND registered:[2025-09-10T16:00:00Z TO 2025-09-11T15:59:59.999Z]',
                     "page[size]": 100, "sort": "registered"})


if __name__ == "__main__":
    main()
