#!/usr/bin/env python3
"""Recover and rebuild 2026-07-01..26 Daily V2.1 reports.

This helper deliberately separates discovery recovery from report writeback.
The first stage snapshots OpenAlex records that resolve to an arXiv 2607 DOI
or landing page, then emits a deterministic candidate inventory.  A later
stage may reuse a historical review only after exact identity, version,
locators and claim boundary have been reconciled.
"""

from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import re
import time
import urllib.parse
import urllib.request
from datetime import date, datetime, timedelta, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "papers/2026/07/_sources/datacite-arxiv-recovery-20260701-26"
WEEKLY_ROOT = ROOT / "papers/2026/weekly"

ARXIV_RE = re.compile(r"(?:arxiv[.:/]|arxiv\.)(26(?:06|07)\.\d{4,5})", re.I)
URL_ARXIV_RE = re.compile(r"arxiv\.org/(?:abs|html|pdf)/?(26(?:06|07)\.\d{4,5})", re.I)

# High-recall discovery filter.  It is intentionally broader than a Books
# filter: false positives are closed by scoring, while false negatives would
# silently shrink the candidate denominator.
# Route candidates with an explicit AI-model signal and a mechanism/system
# signal.  Generic words such as "memory", "planning" or "evaluation" are not
# sufficient by themselves; the earlier single-regex prototype admitted
# thousands of unrelated domain papers and therefore did not constitute a
# meaningful candidate denominator.
MODEL_TERMS = re.compile(
    r"\b(?:large language model|language model|\bllm(?:s)?\b|transformer|"
    r"foundation model|multimodal|vision[- ]language|diffusion model|world model|"
    r"vision[- ]language[- ]action|\bvla\b|agentic|ai agent|generative model)\b",
    re.I,
)
MECHANISM_TERMS = re.compile(
    r"\b(?:attention|mixture of experts|\bmoe\b|tokeni[sz]|embedding|long context|"
    r"context window|context engineering|kv(?:-| )?cache|speculative decod|decoding|"
    r"inference|serving|throughput|latency|batching|scheduler|scheduling|gpu|accelerator|"
    r"kernel|cuda|triton|collective|distributed train|parallel(?:ism| training)|"
    r"pipeline parallel|tensor parallel|checkpoint|optimizer|fine-tun|post-train|"
    r"reinforcement learning|\brlhf\b|\bdpo\b|\bgrpo\b|\bppo\b|distillation|"
    r"quantization|spars|compression|image generation|video generation|robot|robotics|"
    r"embodied|multi-agent|tool use|tool-call|retrieval.augmented|\brag\b|agent memory|"
    r"workflow|verifier|uncertainty|hallucinat|evaluation (?:framework|protocol|system)|"
    r"benchmark (?:reliability|validity|contamination)|observability|alignment|"
    r"interpretability|jailbreak|guardrail|data curation|synthetic data|training data|"
    r"model architecture|reward model|credit assignment)\b",
    re.I,
)
STRONG_TITLE_TERMS = re.compile(
    r"\b(?:mixture of experts|\bmoe\b (?:routing|serving|training)|kv(?:-| )?cache|"
    r"speculative decod|distributed (?:training|inference)|inference serving|"
    r"continuous batching|paged attention|pipeline parallel|tensor parallel|"
    r"world model|vision[- ]language[- ]action|\bvla\b|retrieval.augmented|\brag\b|"
    r"agent(?:ic)? (?:memory|workflow|tool|planning|evaluation|serving|system)|"
    r"multi-agent (?:system|workflow|coordination)|multimodal (?:pretraining|generation)|"
    r"diffusion (?:language model|llm)|long[- ]context (?:model|inference|serving)|"
    r"llm (?:serving|inference|training|runtime|system|agent|evaluation)|"
    r"language model (?:serving|inference|training|runtime|system)|"
    r"reward model|credit assignment|context engineering|tool[- ]calling evaluation)\b",
    re.I,
)
FINAL_ROUTE_TERMS = re.compile(
    r"\b(?:llm (?:serving|inference|training|runtime)|language model (?:serving|inference|training|runtime)|"
    r"kv[ -]?cache|speculative decod|continuous batching|paged attention|distributed (?:training|inference)|"
    r"pipeline parallel|tensor parallel|moe (?:serving|routing|training)|"
    r"mixture of experts (?:serving|routing|training)|checkpoint|gpu cluster|gpu scheduling|"
    r"kernel generation|quantization|world model|vision[- ]language[- ]action|\bvla\b|"
    r"agent(?:ic)? (?:memory|workflow|tool|serving|evaluation)|multi-agent (?:coordination|workflow|system)|"
    r"reward model|credit assignment|context engineering|tool-calling evaluation|"
    r"benchmark(?:ing)? (?:the benchmarks|reliability|validity)|hallucination|uncertainty)\b",
    re.I,
)

CORE_CATEGORIES = {"cs.AI", "cs.CL", "cs.LG", "cs.DC", "cs.IR", "stat.ML"}
KEYWORD_CATEGORIES = {
    "cs.CV", "cs.RO", "cs.SE", "cs.CR", "cs.AR", "cs.PF", "cs.OS",
    "cs.PL", "cs.MA", "cs.DB", "cs.NI", "eess.AS", "cs.SD",
}


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def fetch(url: str) -> bytes:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "AI-System-Design historical research; read-only"},
    )
    last_error: Exception | None = None
    for attempt in range(5):
        try:
            with urllib.request.urlopen(request, timeout=300) as response:
                return response.read()
        except Exception as exc:  # network endpoint is known to reset intermittently
            last_error = exc
            if attempt == 4:
                break
            time.sleep(2 ** attempt)
    raise RuntimeError(f"failed after five attempts: {url}") from last_error


def arxiv_id(record: dict) -> str | None:
    values: list[str] = []
    values.extend(str(value) for value in record.get("ids", {}).values() if value)
    primary = record.get("primary_location") or {}
    values.extend(
        str(primary.get(key)) for key in ("landing_page_url", "pdf_url", "id") if primary.get(key)
    )
    for location in record.get("locations") or []:
        values.extend(
            str(location.get(key)) for key in ("landing_page_url", "pdf_url", "id") if location.get(key)
        )
    joined = "\n".join(values)
    match = ARXIV_RE.search(joined) or URL_ARXIV_RE.search(joined)
    return match.group(1) if match else None


def abstract_text(record: dict) -> str:
    inverted = record.get("abstract_inverted_index") or {}
    positioned: list[tuple[int, str]] = []
    for token, positions in inverted.items():
        for position in positions:
            positioned.append((int(position), token))
    return " ".join(token for _, token in sorted(positioned))


def weekly_ids() -> dict[str, str]:
    owners: dict[str, str] = {}
    for week in range(27, 31):
        path = WEEKLY_ROOT / f"2026-W{week:02d}/README.md"
        text = path.read_text(encoding="utf-8")
        for identifier in set(URL_ARXIV_RE.findall(text)):
            owners[identifier] = path.relative_to(ROOT).as_posix()
    return owners


def fetch_openalex() -> list[dict]:
    OUT.mkdir(parents=True, exist_ok=True)
    cursor = "*"
    page = 0
    records: dict[str, dict] = {}
    while cursor:
        page += 1
        query = urllib.parse.urlencode(
            {
                "search": "arxiv:2607",
                "per-page": 200,
                "cursor": cursor,
                "select": (
                    "id,title,publication_date,primary_location,locations,ids,topics,"
                    "keywords,abstract_inverted_index,authorships,created_date,updated_date"
                ),
            }
        )
        raw = fetch(f"https://api.openalex.org/works?{query}")
        payload = json.loads(raw)
        target = OUT / f"openalex-arxiv-2607-page-{page:03d}.json.gz"
        with target.open("wb") as compressed:
            with gzip.GzipFile(fileobj=compressed, mode="wb", mtime=0) as handle:
                handle.write(raw)
        for record in payload.get("results", []):
            identifier = arxiv_id(record)
            if identifier and identifier.startswith("2607."):
                records.setdefault(identifier, record)
        cursor = payload.get("meta", {}).get("next_cursor")
        if not payload.get("results"):
            break
        time.sleep(0.25)
    return [records[key] for key in sorted(records)]


def fetch_weekly_identities() -> list[dict]:
    """Fetch exact recovery metadata for every arXiv identity in W27..W30."""
    OUT.mkdir(parents=True, exist_ok=True)
    records: dict[str, dict] = {}
    for index, identifier in enumerate(sorted(weekly_ids()), start=1):
        target = OUT / f"openalex-exact-{identifier}.json.gz"
        if target.exists():
            with gzip.open(target, "rb") as handle:
                record = json.load(handle)
        else:
            doi = urllib.parse.quote(f"https://doi.org/10.48550/arxiv.{identifier}", safe="")
            select = urllib.parse.quote(
                "id,title,publication_date,primary_location,locations,ids,topics,keywords,"
                "abstract_inverted_index,authorships,created_date,updated_date",
                safe=",",
            )
            raw = fetch(f"https://api.openalex.org/works/{doi}?select={select}")
            record = json.loads(raw)
            with target.open("wb") as compressed:
                with gzip.GzipFile(fileobj=compressed, mode="wb", mtime=0) as handle:
                    handle.write(raw)
            time.sleep(0.25)
        recovered = arxiv_id(record)
        if recovered != identifier:
            raise RuntimeError(f"identity mismatch for {identifier}: {recovered}")
        records[identifier] = record
        if index % 20 == 0:
            print(f"recovered {index}/{len(weekly_ids())} exact identities", flush=True)
    return [records[key] for key in sorted(records)]


def fetch_datacite() -> list[dict]:
    """Enumerate the DOI ranges that can intersect the July replay window.

    DataCite's ordinary page-number API caps a single query at 10,000 rows.
    Disjoint suffix prefixes keep every query below DataCite's 10k cap.  The
    tail of 2606 is required because the July 1 Beijing window starts on June
    30 at 09:00 and therefore legitimately contains late 2606 submissions.
    """
    OUT.mkdir(parents=True, exist_ok=True)
    records: list[dict] = []
    group_totals: dict[str, int] = {}
    for month, group in (("2606", "2"), ("2606", "3"), ("2607", "0"), ("2607", "1"), ("2607", "2")):
        page = 1
        group_records: list[dict] = []
        while True:
            query = urllib.parse.urlencode(
                {
                    "query": f"doi:10.48550/arxiv.{month}.{group}*",
                    "page[size]": 1000,
                    "page[number]": page,
                    "fields[dois]": (
                        "doi,titles,subjects,dates,descriptions,url,version,relatedIdentifiers"
                    ),
                }
            )
            target = OUT / f"datacite-arxiv-{month}-g{group}-page-{page:02d}.json.gz"
            if target.exists():
                with gzip.open(target, "rb") as handle:
                    raw = handle.read()
            else:
                raw = fetch(f"https://api.datacite.org/dois?{query}")
                with target.open("wb") as compressed:
                    with gzip.GzipFile(fileobj=compressed, mode="wb", mtime=0) as handle:
                        handle.write(raw)
            payload = json.loads(raw)
            page_records = payload.get("data", [])
            group_records.extend(page_records)
            total = int(payload.get("meta", {}).get("total", 0))
            print(f"DataCite {month} group {group} page {page}: {len(group_records)}/{total}", flush=True)
            if not page_records or len(group_records) >= total:
                break
            page += 1
            time.sleep(0.35)
        if len(group_records) != total:
            raise RuntimeError(f"DataCite {month} group {group} incomplete: {len(group_records)} != {total}")
        group_totals[f"{month}.{group}"] = total
        records.extend(group_records)
    identifiers = [datacite_arxiv_id(record) for record in records]
    if None in identifiers or len(set(identifiers)) != len(identifiers):
        raise RuntimeError("DataCite prefix enumeration contains missing or duplicate arXiv identities")
    (OUT / "datacite-group-totals.json").write_text(
        json.dumps(group_totals, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return records


def load_datacite_snapshots() -> list[dict]:
    records: list[dict] = []
    for path in sorted(OUT.glob("datacite-arxiv-26*-g*-page-*.json.gz")):
        with gzip.open(path, "rb") as handle:
            records.extend(json.load(handle).get("data", []))
    identifiers = [datacite_arxiv_id(record) for record in records]
    if not records or None in identifiers or len(set(identifiers)) != len(identifiers):
        raise RuntimeError("canonical DataCite snapshots are absent, incomplete, or duplicated")
    return records


def datacite_value(record: dict, key: str, default=None):
    return record.get("attributes", {}).get(key, default)


def datacite_arxiv_id(record: dict) -> str | None:
    doi = str(datacite_value(record, "doi", ""))
    match = re.fullmatch(r"10\.48550/arxiv\.(26(?:06|07)\.\d{4,5})", doi, re.I)
    return match.group(1) if match else None


def datacite_categories(record: dict) -> list[str]:
    categories: list[str] = []
    for subject in datacite_value(record, "subjects", []) or []:
        if subject.get("subjectScheme") != "arXiv":
            continue
        match = re.search(r"\(([a-z-]+\.[A-Z]{2})\)$", subject.get("subject", ""))
        if match:
            categories.append(match.group(1))
    return sorted(set(categories))


def datacite_submitted(record: dict) -> str | None:
    for item in datacite_value(record, "dates", []) or []:
        if item.get("dateType") == "Submitted" and item.get("dateInformation") == "v1":
            return item.get("date")
    return None


def datacite_text(record: dict) -> tuple[str, str]:
    titles = datacite_value(record, "titles", []) or []
    title = next((item.get("title", "") for item in titles if item.get("title")), "")
    descriptions = datacite_value(record, "descriptions", []) or []
    abstract = next(
        (item.get("description", "") for item in descriptions if item.get("descriptionType") == "Abstract"),
        "",
    )
    return title.strip(), abstract.strip()


def build_datacite_inventory(records: list[dict]) -> dict:
    owners = weekly_ids()
    candidates = []
    category_hits = 0
    for record in records:
        identifier = datacite_arxiv_id(record)
        submitted = datacite_submitted(record)
        if not identifier or not submitted:
            continue
        categories = datacite_categories(record)
        if not (set(categories) & (CORE_CATEGORIES | KEYWORD_CATEGORIES)):
            continue
        timestamp = datetime.fromisoformat(submitted.replace("Z", "+00:00"))
        local_timestamp = timestamp.astimezone(timezone(timedelta(hours=8)))
        if not (
            datetime(2026, 6, 30, 1, tzinfo=timezone.utc)
            <= timestamp
            < datetime(2026, 7, 26, 1, tzinfo=timezone.utc)
        ):
            continue
        category_hits += 1
        title, abstract = datacite_text(record)
        route_text = f"{title} {abstract}"
        included = identifier in owners or (
            bool(FINAL_ROUTE_TERMS.search(title))
            and (
                bool(STRONG_TITLE_TERMS.search(title))
                or (bool(MODEL_TERMS.search(title)) and bool(MECHANISM_TERMS.search(title)))
            )
        )
        if not included:
            continue
        candidates.append(
            {
                "arxiv_id": identifier,
                "source_family_id": f"SF-2026-ARXIV-{identifier.replace('.', '-')}",
                "title": title,
                "submitted_utc": timestamp.isoformat(),
                "first_public_asia_shanghai": local_timestamp.isoformat(),
                "daily_date": (
                    local_timestamp.date() + timedelta(days=1 if local_timestamp.hour >= 9 else 0)
                ).isoformat(),
                "categories": categories,
                "abstract": abstract,
                "weekly_review_ref": owners.get(identifier),
                "included": True,
                "inclusion_basis": (
                    "existing_weekly_review+route" if identifier in owners and FINAL_ROUTE_TERMS.search(title)
                    else "existing_weekly_review" if identifier in owners
                    else "project_system_title_route"
                ),
            }
        )
    candidates.sort(key=lambda item: (item["submitted_utc"], item["arxiv_id"]))
    inventory = {
        "schema": "july-daily-datacite-recovery-v1",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "query": "DataCite DOI prefixes 10.48550/arxiv.2606.[23]* and 10.48550/arxiv.2607.[012]*; exact arXiv subjects and v1 Submitted timestamp",
        "raw_doi_records": len(records),
        "category_window_hits": category_hits,
        "included_candidates": len(candidates),
        "weekly_review_ids_missing_from_window": sorted(
            identifier
            for identifier in owners
            if identifier.startswith("2607.")
            and identifier not in {item["arxiv_id"] for item in candidates}
        ),
        "candidates": candidates,
    }
    raw = json.dumps(inventory, ensure_ascii=False, indent=2, sort_keys=True).encode()
    (OUT / "datacite-candidate-inventory.json").write_bytes(raw)
    return inventory


def build_inventory(records: list[dict]) -> dict:
    owners = weekly_ids()
    result = []
    for record in records:
        identifier = arxiv_id(record)
        if not identifier:
            continue
        title = (record.get("title") or "").strip()
        abstract = abstract_text(record)
        topic_text = " ".join(
            topic.get("display_name", "") for topic in (record.get("topics") or [])
        )
        keyword_text = " ".join(
            keyword.get("display_name", "") for keyword in (record.get("keywords") or [])
        )
        discovery_text = " ".join((title, abstract, topic_text, keyword_text))
        included = (
            identifier in owners
            or bool(STRONG_TITLE_TERMS.search(title))
            or (bool(MODEL_TERMS.search(title)) and bool(MECHANISM_TERMS.search(title)))
        )
        result.append(
            {
                "arxiv_id": identifier,
                "source_family_id": f"SF-2026-ARXIV-{identifier.replace('.', '-')}",
                "title": title,
                "publication_date": record.get("publication_date"),
                "daily_date": (
                    (date.fromisoformat(record["publication_date"]) + timedelta(days=1)).isoformat()
                    if record.get("publication_date")
                    else None
                ),
                "abstract": abstract,
                "topics": [topic.get("display_name") for topic in record.get("topics") or []],
                "keywords": [keyword.get("display_name") for keyword in record.get("keywords") or []],
                "openalex_id": record.get("id"),
                "weekly_review_ref": owners.get(identifier),
                "included": included,
                "inclusion_basis": (
                    "existing_weekly_review+route" if identifier in owners and (
                        STRONG_TITLE_TERMS.search(title)
                        or (MODEL_TERMS.search(title) and MECHANISM_TERMS.search(title))
                    )
                    else "existing_weekly_review" if identifier in owners
                    else "strong_title_route" if STRONG_TITLE_TERMS.search(title)
                    else "model+mechanism_route"
                ),
            }
        )
    inventory = {
        "schema": "july-daily-recovery-v1",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "query": "OpenAlex search=arxiv:2607; exact arXiv identity recovered from DOI/location",
        "records_with_arxiv_2607_identity": len(result),
        "included_candidates": sum(bool(item["included"]) for item in result),
        "weekly_review_ids_not_in_openalex_search": sorted(set(owners) - {item["arxiv_id"] for item in result}),
        "candidates": result,
    }
    raw = json.dumps(inventory, ensure_ascii=False, indent=2, sort_keys=True).encode()
    (OUT / "candidate-inventory.json").write_bytes(raw)
    return inventory


def write_manifest(inventory: dict) -> None:
    snapshot_rows = []
    for path in sorted(OUT.glob("openalex-*.json.gz")):
        with gzip.open(path, "rb") as handle:
            raw = handle.read()
        snapshot_rows.append((path.name, len(raw), sha256(raw), sha256(path.read_bytes())))
    lines = [
        "# 2026-07-01～26 arXiv Recovery Snapshot\n",
        "arXiv API/OAI 在本次运行持续连接重置，因此使用来源注册表为 `SRC-ARXIV` 指定的 "
        "`SRC-OPENALEX` fallback 恢复 identity、date 与 abstract metadata。该快照不会把 OpenAlex "
        "metadata 冒充 primary manuscript；Full Source Review 仍须回到精确 arXiv v1 或可验证的历史 "
        "primary-source provenance。\n",
        f"- Retrieved At: `{datetime.now().astimezone().isoformat()}`",
        f"- arXiv 2607 identities: `{inventory['records_with_arxiv_2607_identity']}`",
        f"- High-recall candidates: `{inventory['included_candidates']}`",
        f"- Inventory SHA-256: `{sha256((OUT / 'candidate-inventory.json').read_bytes())}`\n",
        "## Snapshot Files\n",
        "| File | Raw bytes | Raw SHA-256 | Gzip SHA-256 |",
        "| --- | ---: | --- | --- |",
    ]
    lines.extend(f"| `{name}` | {size} | `{raw_hash}` | `{gz_hash}` |" for name, size, raw_hash, gz_hash in snapshot_rows)
    lines.extend(
        [
            "",
            "## Evidence Boundary",
            "",
            "- OpenAlex only recovers discovery metadata and identity; it cannot support mechanism or benchmark claims.",
            "- A candidate is not complete merely because it appears in this inventory.",
            "- The exact Beijing Daily bucket is reconciled against the primary v1 timestamp whenever arXiv access resumes.",
            "",
        ]
    )
    (OUT / "README.md").write_text("\n".join(lines), encoding="utf-8")


def write_datacite_manifest(inventory: dict) -> None:
    snapshot_rows = []
    for path in sorted(OUT.glob("datacite-arxiv-26*-g*-page-*.json.gz")):
        with gzip.open(path, "rb") as handle:
            raw = handle.read()
        snapshot_rows.append((path.name, len(raw), sha256(raw), sha256(path.read_bytes())))
    manifest_payload = "".join(
        f"{name}\t{raw_hash}\t{gz_hash}\n"
        for name, _, raw_hash, gz_hash in snapshot_rows
    ).encode()
    lines = [
        "# 2026-07-01～26 arXiv / DataCite Recovery Snapshot",
        "",
        "本目录用于恢复官方 arXiv API 持续连接重置时的确定性枚举。DataCite 作为 `SRC-ARXIV` 注册 fallback，只承担 DOI identity、arXiv subject、v1 Submitted timestamp 与 abstract metadata；机制与 benchmark claim 仍由精确 arXiv v1 正文承担。",
        "",
        f"- Retrieved At: `{datetime.now().astimezone().isoformat()}`",
        f"- Enumerated DOI records: `{inventory['raw_doi_records']}`",
        f"- Contract-category records in strict replay window: `{inventory['category_window_hits']}`",
        f"- Frozen AI-System candidate families: `{inventory['included_candidates']}`",
        f"- Candidate inventory SHA-256: `{sha256((OUT / 'datacite-candidate-inventory.json').read_bytes())}`",
        f"- Canonical snapshot manifest SHA-256: `{sha256(manifest_payload)}`",
        "",
        "## Query Partition",
        "",
        "DataCite 普通页码查询的单查询上限为 10,000 条，因此使用互斥 DOI 前缀。`2606.2* / 2606.3*` 覆盖 7 月 1 日窗口可能出现的 6 月尾部 v1；`2607.0* / 2607.1* / 2607.2*` 覆盖其余窗口。每个分区独立闭页，合并 identifier 必须唯一。",
        "",
        "## Snapshot Files",
        "",
        "| File | Raw bytes | Raw SHA-256 | Gzip SHA-256 |",
        "| --- | ---: | --- | --- |",
    ]
    lines.extend(f"| `{name}` | {size} | `{raw_hash}` | `{gz_hash}` |" for name, size, raw_hash, gz_hash in snapshot_rows)
    lines.extend([
        "",
        "## Routing and Evidence Boundary",
        "",
        "- Daily 归档窗口按 `[前一日 09:00, 当日 09:00)`；北京时间 09:00 及以后提交的 v1 归入下一日报告日。",
        "- route filter 要求标题同时体现 AI model 与 system mechanism，或已存在于 W27～W30 的完整 Source Review；垂直应用中偶然出现 Transformer/LLM 不进入分母。",
        "- DataCite metadata 不支持 Standard/Deep mechanism claim。需要较深路由的 family 必须回到 arXiv v1 HTML 或有等价 provenance 的正式全文。",
        "",
    ])
    (OUT / "README.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--fetch", action="store_true")
    parser.add_argument("--fetch-weekly", action="store_true")
    parser.add_argument("--fetch-datacite", action="store_true")
    parser.add_argument("--build-datacite", action="store_true")
    args = parser.parse_args()
    if args.fetch_datacite:
        inventory = build_datacite_inventory(fetch_datacite())
        write_datacite_manifest(inventory)
        print(json.dumps({key: inventory[key] for key in ("raw_doi_records", "category_window_hits", "included_candidates", "weekly_review_ids_missing_from_window")}, ensure_ascii=False, indent=2))
        return
    if args.build_datacite:
        inventory = build_datacite_inventory(load_datacite_snapshots())
        write_datacite_manifest(inventory)
        print(json.dumps({key: inventory[key] for key in ("raw_doi_records", "category_window_hits", "included_candidates", "weekly_review_ids_missing_from_window")}, ensure_ascii=False, indent=2))
        return
    if args.fetch_weekly:
        records = fetch_weekly_identities()
    elif args.fetch:
        records = fetch_openalex()
    else:
        records = []
        for path in sorted(OUT.glob("openalex-*.json.gz")):
            with gzip.open(path, "rb") as handle:
                for record in json.load(handle).get("results", []):
                    if arxiv_id(record):
                        records.append(record)
    inventory = build_inventory(records)
    write_manifest(inventory)
    print(json.dumps({key: inventory[key] for key in ("records_with_arxiv_2607_identity", "included_candidates", "weekly_review_ids_not_in_openalex_search")}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
