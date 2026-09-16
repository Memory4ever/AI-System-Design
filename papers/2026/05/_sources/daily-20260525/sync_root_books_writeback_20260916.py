#!/usr/bin/env python3
"""Synchronize the current 2026-05-25 projection after root Books writeback."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
SOURCE_DIR = Path(__file__).resolve().parent
REPORT = ROOT / "papers/2026/05/25/README.md"
COMPARISON = SOURCE_DIR / "books-comparison-v3.json"
QUEUE = SOURCE_DIR / "root-books-writeback-queue-v3.json"

FAMILIES = {
    "SF-2026-ARXIV-2605-23128": ("MULTIMODAL-EMBODIED-VLA", "books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md"),
    "SF-2026-ARXIV-2605-23482": ("TRAIN-DATA", "books/part-04-training-system/27-data.md"),
    "SF-2026-ARXIV-2605-23562": ("AGENT-MULTI-AGENT", "books/part-07-agent/82-multi-agent.md"),
    "SF-2026-ARXIV-2605-23565": ("TRAIN-PPO", "books/part-04-training-system/32-ppo.md"),
    "SF-2026-ARXIV-2605-23883": ("TRAIN-DATA", "books/part-04-training-system/27-data.md"),
}


def write_json(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


comparison = json.loads(COMPARISON.read_text(encoding="utf-8"))
for item in comparison["items"]:
    if item["source_family_id"] in FAMILIES:
        item["decision"] = "Applied"
comparison["counts"]["Applied"] = 52
comparison["counts"]["Integrate"] = 0
comparison["arithmetic"] = (
    "280 = 52 Applied + 3 Deferred + 0 Integrate + 209 No Change — Existing Coverage + "
    "9 Report Only + 7 Structural Candidate"
)
write_json(COMPARISON, comparison)

queue = json.loads(QUEUE.read_text(encoding="utf-8"))
for item in queue["items"]:
    if item["source_family_id"] in FAMILIES:
        item["status"] = "applied_pending_fresh_review"
queue["root_applied_integration_count"] = 32
queue["pending_integration_count"] = 0
queue["status"] = "root_writeback_complete_pending_fresh_nonauthor_review"
write_json(QUEUE, queue)

text = REPORT.read_text(encoding="utf-8")
text = text.replace(
    "280 = 47 Applied + 3 Deferred + 5 Integrate + 209 No Change — Existing Coverage + 9 Report Only + 7 Structural Candidate",
    "280 = 52 Applied + 3 Deferred + 0 Integrate + 209 No Change — Existing Coverage + 9 Report Only + 7 Structural Candidate",
)
text = text.replace(
    "并新增 **5** 个待 root 串行写回的真实 delta。",
    "；本轮新增的 **5** 个真实 delta 也已由 root 串行写入正文，等待 fresh non-author 核验。",
)
text = text.replace(
    "状态保持 Ongoing，等待 5 项 root 写回与另一位 fresh non-author 终审。",
    "状态保持 Ongoing，仅等待另一位 fresh non-author 对写回正文、边界和整日报告终审。",
)
for family, (owner, path) in FAMILIES.items():
    arxiv_id = family.removeprefix("SF-2026-ARXIV-").replace("-", ".", 1)
    link = "../../../../" + path
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if line.startswith(f"| [{arxiv_id} "):
            lines[index] = line.replace(
                "整合：待 root 串行写回：",
                "整合：当前正文 binding 已存在：",
                1,
            )
            break
    text = "\n".join(lines) + "\n"
    block_pattern = re.compile(
        rf"(<!-- review:{re.escape(family)}:start -->.*?)(Books：)Integrate(；owner={re.escape(owner)}。.*?<!-- review:{re.escape(family)}:end -->)",
        re.S,
    )
    text, replaced = block_pattern.subn(rf"\1\2Applied\3", text, count=1)
    if replaced != 1 and not re.search(
        rf"<!-- review:{re.escape(family)}:start -->.*?Books：Applied；owner={re.escape(owner)}。.*?<!-- review:{re.escape(family)}:end -->",
        text,
        re.S,
    ):
        raise RuntimeError(f"failed to update report block for {family}")

text = text.replace(
    "1. root 按 [`root-books-writeback-queue-v3.json`](../_sources/daily-20260525/root-books-writeback-queue-v3.json) 串行处理 5 个新 Integrate。",
    "1. root 已按 [`root-books-writeback-queue-v3.json`](../_sources/daily-20260525/root-books-writeback-queue-v3.json) 串行完成 5 个新 Integrate；每项均有成对 semantic-body binding，等待 fresh non-author 复核。",
)
text = text.replace(
    "4. root 写回后必须由未参与本轮作者修复的 fresh non-author 复核 Coverage、157 个本轮恢复项、217 个闭包理由、旧 123 项当前投影、全部 Books disposition 与实际 binding，才可把状态改为 Complete。",
    "4. 必须由未参与本轮作者修复与 root 写回的 fresh non-author 复核 Coverage、157 个本轮恢复项、217 个闭包理由、旧 123 项当前投影、全部 Books disposition 与实际 binding，才可把状态改为 Complete。",
)
text = text.replace(
    "其中真正新增待 root 写回为 5 项，owner-day 仍有 97 项隔离。",
    "其中 5 项新增正文写回已经完成，owner-day 仍有 97 项隔离；当前只差 fresh non-author 终审。",
)
REPORT.write_text(text, encoding="utf-8")

for family, (_, path) in FAMILIES.items():
    body = (ROOT / path).read_text(encoding="utf-8")
    start = f"<!-- semantic-body-binding:{family}:start -->"
    end = f"<!-- semantic-body-binding:{family}:end -->"
    if body.count(start) != 1 or body.count(end) != 1 or body.index(start) > body.index(end):
        raise RuntimeError(f"invalid paired binding for {family}")

print("synchronized 5 root Books writebacks; report remains Ongoing pending fresh review")
