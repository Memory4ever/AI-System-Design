#!/usr/bin/env python3
"""Archive a bounded non-arXiv historical replay for 2026-03-01..08.

These sources entered the fixed registry after March, so REPORT_CONTRACTS says
they are not retroactively due in the validator's Required Daily arithmetic.
The parent task nevertheless requires a bounded archival replay.  This script
therefore writes a separate receipt rather than falsifying the machine source
coverage table with non-due rows.
"""

from __future__ import annotations

import hashlib
import json
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXECUTED = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")

SOURCES = {
    "SRC-OPENAI": ["https://openai.com/research/index/"],
    "SRC-ANTHROPIC": ["https://www.anthropic.com/research"],
    "SRC-GOOGLE-AI": ["https://deepmind.google/research/publications/", "https://deepmind.google/models/model-cards/", "https://research.google/pubs/"],
    "SRC-META-AI": ["https://ai.meta.com/research/"],
    "SRC-XAI": ["https://x.ai/news"],
    "SRC-MISTRAL": ["https://mistral.ai/news/"],
    "SRC-QWEN": ["https://qwenlm.github.io/", "https://qwenlm.github.io/qwen-code-docs/en/blog/updates/"],
    "SRC-DEEPSEEK": ["https://www.deepseek.com/", "https://api-docs.deepseek.com/updates"],
    "SRC-MOONSHOT": ["https://platform.kimi.com/blog", "https://github.com/MoonshotAI"],
    "SRC-ZAI": ["https://docs.z.ai/release-notes/new-released", "https://docs.z.ai/llms.txt", "https://github.com/zai-org"],
    "SRC-MINIMAX": ["https://www.minimax.io/"],
    "SRC-BYTEDANCE-SEED": ["https://seed.bytedance.com/en/", "https://seed.bytedance.com/en/public_papers"],
    "SRC-BAIDU-ERNIE": ["https://ernie.baidu.com/blog/zh/", "https://ernie.baidu.com/blog/zh/publication/"],
    "SRC-TENCENT-HUNYUAN": ["https://github.com/Tencent-Hunyuan", "https://github.com/orgs/Tencent-Hunyuan/repositories"],
    "SRC-HUAWEI-NOAH": ["https://noahlab.com.hk/"],
    "SRC-SHLAB": ["https://www.shlab.org.cn/"],
    "SRC-STEPFUN": ["https://www.stepfun.com/research"],
    "SRC-XIAOMI-MIMO": ["https://mimo.xiaomi.com/"],
    "SRC-INCLUSION-AI": ["https://www.inclusion-ai.org/publication/"],
    "SRC-HF-PAPERS": ["https://huggingface.co/papers"],
}

# Manual historical-listing assessment from the official endpoints above.
# Date-only entries are deliberately not assigned to a strict 09:00 window.
ASSESSMENT = {
    "SRC-OPENAI": {"status": "date_only_lead_unowned", "basis": "Official research index lists one 2026-03-04 item, but exposes no publication time or timezone.", "leads": [{"date": "2026-03-04", "title": "Extending single-minus amplitudes to gravitons", "url": "https://openai.com/research/index/"}]},
    "SRC-ANTHROPIC": {"status": "enumerated_no_hit", "basis": "Official research listing has no item dated 2026-03-01..08; next visible March research item is later in the month.", "leads": []},
    "SRC-GOOGLE-AI": {"status": "date_only_lead_unowned", "basis": "Official model-card listing says Gemini 3.1 Flash-Lite was updated 2026-03-03; no exact publication instant. Official publications listing has no 2026-03-01..08 item.", "leads": [{"date": "2026-03-03", "title": "Gemini 3.1 Flash-Lite model card update", "url": "https://deepmind.google/models/model-cards/"}]},
    "SRC-META-AI": {"status": "historical_cursor_incomplete", "basis": "Current official research surface does not expose a stable dated historical cursor sufficient to prove a no-hit window.", "leads": []},
    "SRC-XAI": {"status": "enumerated_no_hit", "basis": "Official news listing has no item dated 2026-03-01..08; visible neighboring items are 2026-02-02 and 2026-04-17.", "leads": []},
    "SRC-MISTRAL": {"status": "enumerated_no_hit", "basis": "Official news listing has no item dated 2026-03-01..08; first visible March 2026 item is 2026-03-11.", "leads": []},
    "SRC-QWEN": {"status": "date_only_lead_unowned", "basis": "Official Qwen Code update log contains entries dated 2026-03-03 and 2026-03-06, but exposes no exact publication instant; they are tooling/version leads, not mechanism evidence.", "leads": [{"date": "2026-03-03", "title": "Qwen Code update", "url": "https://qwenlm.github.io/qwen-code-docs/en/blog/updates/"}, {"date": "2026-03-06", "title": "Qwen Code update", "url": "https://qwenlm.github.io/qwen-code-docs/en/blog/updates/"}]},
    "SRC-DEEPSEEK": {"status": "enumerated_no_hit", "basis": "Official update log exposes no item dated 2026-03-01..08; visible adjacent release entries do not intersect the window.", "leads": []},
    "SRC-MOONSHOT": {"status": "enumerated_no_hit", "basis": "Official dated platform blog exposes no 2026-03-01..08 item; GitHub remains identity/artifact recovery only without a strict-window release lead.", "leads": []},
    "SRC-ZAI": {"status": "enumerated_no_hit", "basis": "Official release notes jump from 2026-02-12 to 2026-03-15; no strict-window release.", "leads": []},
    "SRC-MINIMAX": {"status": "historical_cursor_incomplete", "basis": "Current corporate surface does not expose an enumerable model/research archive for this window; a 2026-03-02 annual-results filing is corporate context, not an AI-system mechanism candidate.", "leads": []},
    "SRC-BYTEDANCE-SEED": {"status": "enumerated_no_hit", "basis": "Official model/blog/publication surfaces expose no model, report or artifact first-public in 2026-03-01..08; neighboring model release is 2026-02-14.", "leads": []},
    "SRC-BAIDU-ERNIE": {"status": "enumerated_no_hit", "basis": "Official ERNIE blog/publications show no dated item in 2026-03-01..08; visible neighboring releases are 2026-02-06 and 2026-04-15.", "leads": []},
    "SRC-TENCENT-HUNYUAN": {"status": "historical_cursor_incomplete", "basis": "Current GitHub organization listing exposes mutable updated-at values, not first-public/release ownership; no exact tagged release was recovered for the window.", "leads": []},
    "SRC-HUAWEI-NOAH": {"status": "historical_cursor_incomplete", "basis": "Official site does not expose a stable enumerable historical publication cursor for this strict window.", "leads": []},
    "SRC-SHLAB": {"status": "enumerated_no_hit", "basis": "Official dated news search has no item in 2026-03-01..08; the neighboring DeepLink mixed-inference item is dated 2026-03-09 and belongs outside lane A.", "leads": []},
    "SRC-STEPFUN": {"status": "historical_cursor_incomplete", "basis": "Official research surface is currently not an enumerable dated archive, so a deterministic historical no-hit cannot be claimed.", "leads": []},
    "SRC-XIAOMI-MIMO": {"status": "historical_cursor_incomplete", "basis": "Official site does not expose a stable dated historical listing adequate for the strict window.", "leads": []},
    "SRC-INCLUSION-AI": {"status": "historical_cursor_incomplete", "basis": "Official publications surface could not be reconstructed as a complete strict-window cursor.", "leads": []},
    "SRC-HF-PAPERS": {"status": "historical_backstop_incomplete", "basis": "Daily Papers is a non-deterministic discovery backstop whose current page does not prove its historical 2026-03-01..08 recommendations; arXiv primary inventory is independently complete.", "leads": []},
}


def fetch(url: str) -> dict:
    request = urllib.request.Request(url, headers={"User-Agent": "AI-System-Design historical source replay/2.1"})
    try:
        with urllib.request.urlopen(request, timeout=25) as response:
            body = response.read(4_000_000)
            return {"url": url, "http_status": response.status, "bytes_captured": len(body), "sha256": hashlib.sha256(body).hexdigest(), "access": "accessible"}
    except Exception as exc:
        return {"url": url, "access": "failed", "error": f"{type(exc).__name__}: {exc}"[:500]}


def main() -> None:
    urls = sorted({url for values in SOURCES.values() for url in values})
    access = {}
    with ThreadPoolExecutor(max_workers=8) as executor:
        futures = {executor.submit(fetch, url): url for url in urls}
        for future in as_completed(futures):
            row = future.result()
            access[row["url"]] = row
    for day in range(1, 9):
        date = f"2026-03-{day:02d}"
        previous = "2026-02-28" if day == 1 else f"2026-03-{day - 1:02d}"
        rows = []
        for source_id, endpoints in SOURCES.items():
            assessment = ASSESSMENT[source_id]
            relevant_leads = [lead for lead in assessment["leads"] if lead["date"] in {previous, date}]
            rows.append({
                "source_id": source_id,
                "registry_effective_date": "2026-08-25",
                "contract_due_for_report": False,
                "archival_replay_requested_by_parent": True,
                "window_start": f"{previous}T09:00:00+08:00",
                "window_end": f"{date}T09:00:00+08:00",
                "endpoints": [access[url] for url in endpoints],
                "assessment": assessment["status"],
                "basis": assessment["basis"],
                "date_overlapping_leads": relevant_leads,
                "denominator_effect": "none_without_exact_first_public_instant_and_durable_mechanism",
            })
        packet = ROOT / f"papers/2026/03/_sources/daily-202603{day:02d}"
        payload = {
            "schema": "non-arxiv-historical-replay-receipt-v1",
            "report_date": date,
            "executed_at": EXECUTED,
            "scope": "Later-effective Required Daily registry sources, replayed as explicit archival supplement outside validator due arithmetic.",
            "completion": "completed_with_strict_window_boundaries",
            "candidate_source_families_added": 0,
            "rows": rows,
        }
        (packet / "non-arxiv-historical-replay-receipt.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
        print(json.dumps({"date": date, "sources": len(rows), "lead_rows": sum(bool(x["date_overlapping_leads"]) for x in rows), "added": 0}))


if __name__ == "__main__":
    main()
