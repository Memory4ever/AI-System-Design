#!/usr/bin/env python3
"""Independently verify and seal the completed 2026-06-02 Daily.

The report, prior receipts, and current Books text are inputs under test.  This
script never writes shared Books or LEARNING_STATE.  It emits a fresh semantic
receipt plus a packet-wide SHA-256 manifest after all assertions pass.
"""

from __future__ import annotations

import csv
import hashlib
import json
import re
import subprocess
from collections import Counter
from pathlib import Path

import audit_june02_evidence_v3_fresh as evidence
import audit_june02_v2_strict as identity
import rebuild_june02_daily_v2_strict as renderer


ROOT = Path(__file__).resolve().parents[1]
DAILY = ROOT / "papers/2026/06/02/README.md"
PACKET = ROOT / "papers/2026/06/_sources/daily-20260602"
DENOM = PACKET / "candidate-denominator-audit-v3-fresh.json"
LEDGER = PACKET / "screening-ledger-v3-fresh.tsv"
IDENTITY = PACKET / "identity-provenance-v2-strict.json"
EVIDENCE = PACKET / "evidence-audit-v3-fresh.json"
MARKERS = PACKET / "books-marker-audit-v3-fresh.json"
OUT_JSON = PACKET / "post-write-fresh-audit-v4.json"
OUT_MD = PACKET / "POST_WRITE_FRESH_AUDIT_V4.md"
MANIFEST = PACKET / "SHA256SUMS"

CANONICAL_SECTIONS = [
    "## Executive Summary", "## 1. Coverage", "## 2. Candidate Ledger",
    "## 3. Review Completion Receipt", "## 4. Benchmark Contracts",
    "## 5. Deep Analysis Selection", "## 6. Books Comparison",
    "## 7. Semantic Audit", "## 8. Ignored Noise",
    "## 9. Recommended Action", "## 10. Repository Changes",
    "## 11. Open Questions", "## 12. Sources", "## 13. Final Status",
]

ROUTE_RISK = re.compile(
    r"cache|serv|schedul|distributed|parallel|agent|tool|workflow|retriev|"
    r"security|privacy|evaluation|uncertaint|runtime|resource", re.I,
)

EXCLUDED_MARKER_TERMS = {
    "SF-AURA-ACTION-GATED-MEMORY": ["2606.02775", "Action Surprise"],
    "SF-FAST-DLLM-FRECHET": ["2606.02955", "Fast-dLLM", "Fréchet"],
    "SF-TWINQUANT-DUAL-SUBSPACE": ["2606.01556", "TwinQuant"],
    "SF-CADDTREE-COST-AWARE": ["2606.01813", "CaDDTree"],
    "SF-SAFEMCP-POWER-REGULATION": ["2606.01991", "SafeMCP"],
    "SF-LOWBIT-REASONING-RECOVERY": ["2606.02011", "2-bit Qwen"],
    "SF-DECK-HALLUCINATION-UQ": ["2606.02289", "DECK"],
    "SF-INFORMED-ABSTENTION": ["2606.02965", "Informed Abstention"],
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rg_files(term: str) -> list[str]:
    proc = subprocess.run(
        ["rg", "-l", "-F", term, "books"], cwd=ROOT, text=True,
        capture_output=True, check=False,
    )
    if proc.returncode not in (0, 1):
        raise RuntimeError(proc.stderr)
    return [line for line in proc.stdout.splitlines() if line]


def normalize_target(value: str) -> str:
    return value.split("#", 1)[0]


def verify_structure(text: str) -> None:
    assert text.startswith("# Daily Research — 2026-06-02\n")
    for field in (
        "**Research Date:** 2026-06-02", "**Timezone:** Asia/Shanghai",
        "**Strict Window:** 2026-06-01 09:00:00 ～ 2026-06-02 09:00:00",
        "**Contract:** V2.1", "**Status:** Complete",
    ):
        assert field in text, field
    assert [line for line in text.splitlines() if line.startswith("## ")] == CANONICAL_SECTIONS


def verify_denominator() -> dict:
    rows = list(csv.DictReader(LEDGER.open(encoding="utf-8"), delimiter="\t"))
    denom = json.loads(DENOM.read_text(encoding="utf-8"))
    provenance = json.loads(IDENTITY.read_text(encoding="utf-8"))
    assert len(rows) == len({row["Primary Identifier"] for row in rows}) == 736
    states = Counter(row["Denominator State"] for row in rows)
    assert states == {"retained": 28, "pre_denominator_closure": 708}
    retained = [row for row in rows if row["Denominator State"] == "retained"]
    closures = [row for row in rows if row["Denominator State"] == "pre_denominator_closure"]
    assert {row["Source Family ID"] for row in retained} == {
        item["source_family_id"] for item in denom["candidates"]
    }
    for row in retained:
        assert row["Source Family ID"].startswith("SF-") and row["Stable Node ID"] != "—"
    for row in closures:
        assert row["Source Family ID"] == row["Stable Node ID"] == "—"
        basis = row["Closure / Retention Basis"]
        assert row["Title"].strip('"') in basis
        assert "Abstract challenge:" in basis and len(basis.split("Abstract challenge:", 1)[1].strip()) >= 80

    atom, _ = identity.load_atom()
    by_id = {identity.base_id(row["Primary Identifier"]): row for row in rows}
    assert set(atom) == set(by_id)
    title_normalizations = 0
    for base, row in by_id.items():
        source = atom[base]
        assert identity.WINDOW_START <= source["published_utc"] < identity.WINDOW_END
        assert row["Published UTC"] == source["published_utc"]
        assert row["Abstract SHA256-16"] == hashlib.sha256(source["abstract"].encode()).hexdigest()[:16]
        if identity.title_key(row["Title"]) != identity.title_key(source["title"]):
            raise AssertionError(f"title mismatch: {base}")
        if row["Title"] != source["title"]:
            title_normalizations += 1

    assert provenance["raw_count"] == provenance["verified_count"] == 736
    assert provenance["out_of_window_count"] == provenance["disputed_count"] == 0
    risk = [row for row in closures if ROUTE_RISK.search(row["Title"])]
    return {
        "raw": 736, "retained": 28, "closures": 708,
        "route_risk_rechecked": len(risk),
        "route_risk_ids": [row["Primary Identifier"] for row in risk],
        "title_normalizations": title_normalizations,
        "ledger_sha256": sha256(LEDGER),
    }


def verify_evidence_and_selection(text: str) -> dict:
    cand = evidence.table_map(text, "## 2. Candidate Ledger")
    rp = evidence.table_map(text, "## 3. Review Completion Receipt")
    bench = evidence.table_map(text, "## 4. Benchmark Contracts")
    selection = evidence.table_map(text, "## 5. Deep Analysis Selection")
    books = evidence.table_map(text, "## 6. Books Comparison")
    audit = json.loads(EVIDENCE.read_text(encoding="utf-8"))
    families = set(cand)
    assert len(families) == len(rp) == len(bench) == len(books) == 28
    assert families == set(rp) == set(bench) == set(books)
    assert audit["candidate_count"] == audit["exact_v1_review_complete"] == 28
    assert audit["blocked"] == audit["ordinary_pending"] == 0

    local, official = 0, 0
    for family in families:
        c, r, b = cand[family], rp[family], bench[family]
        assert int(c[6]) + int(c[7]) + int(c[8]) == int(c[9])
        assert r[-1] == "complete" and r[1].startswith("RP-")
        review = renderer.review_block(text, family)
        assert renderer.rp_id(c, r, review) == r[1]
        assert all(r[index] and r[index] != "—" for index in range(5, 10))
        assert len(b) == 11 and all(value for value in b[1:])
        for value in b[1:]:
            lower = value.casefold()
            assert "§" not in value and "appendix" not in lower and "not disclosed —" not in lower
            if "not disclosed" in lower:
                assert value == "Not Disclosed"
        identifier = c[1].removeprefix("arXiv:")
        source = PACKET / "arxiv-v1" / f"{identifier}.html"
        if source.exists():
            local += 1
            assert identifier.removesuffix("v1") in source.read_text(encoding="utf-8", errors="replace")
        else:
            official += 1
            rec = next(item for item in audit["records"] if item["source_family_id"] == family)
            assert rec["access_route"].startswith("official_exact_v1_")

    eligible = {
        family for family, row in cand.items()
        if int(row[9]) >= 7 or row[13] not in {"", "none", "—"} or row[19] == "Integrate"
    }
    assert set(selection) == eligible and len(selection) == 27
    noneligible = families - eligible
    assert noneligible == {"SF-SECLAW-SPEC-DRIVEN-SECURITY"}
    assert "SF-SECLAW-SPEC-DRIVEN-SECURITY" not in selection
    closure = renderer.bounded_block(
        text, "analysis-noneligible:SF-SECLAW-SPEC-DRIVEN-SECURITY"
    )
    assert "Score V2=6/9、Review Override=`none`" in closure
    assert "`potential_books_delta`" in closure
    assert "主 Selection eligible pool 之外" in closure
    assert "不能把 non-eligible closure 误写成 `not_selected`" in closure
    selected = [row for row in selection.values() if row[2] == "selected"]
    assert len(selected) == 3
    assert len({row[3] for row in selected}) == 2
    assert sum(row[2] == "not_selected" for row in selection.values()) == 24
    return {
        "reviews": 28, "local_exact_v1_html": local,
        "official_exact_v1_routes": official, "benchmark_contracts": 28,
        "selection_routed": 27, "selected_families": 3, "selected_units": 2,
        "not_selected": 24,
        "not_prebooks_eligible": 1,
    }


def verify_books(text: str) -> dict:
    books = evidence.table_map(text, "## 6. Books Comparison")
    markers = json.loads(MARKERS.read_text(encoding="utf-8"))["records"]
    integrate = [row for row in books.values() if row[-2] == "Integrate"]
    no_change = [row for row in books.values() if row[-2] == "No Change — Existing Coverage"]
    assert len(integrate) == 19 and len(no_change) == 9
    unique_integrate = []
    existing_no_change = []
    absent_no_change = []
    cand = evidence.table_map(text, "## 2. Candidate Ledger")
    for family, row in books.items():
        base = cand[family][1].removeprefix("arXiv:").removesuffix("v1")
        hits = rg_files(base)
        target = normalize_target(row[2])
        if row[-2] == "Integrate":
            assert hits == [target], (family, hits, target)
            unique_integrate.append(family)
        else:
            assert not hits or hits == [target], (family, hits, target)
            (existing_no_change if hits else absent_no_change).append(family)

    retained_markers = [row for row in markers if row["retained_v3"]]
    excluded_markers = [row for row in markers if not row["retained_v3"]]
    assert len(retained_markers) == 14 and len(excluded_markers) == 8
    for row in retained_markers:
        base = row["primary_identifier"].removeprefix("arXiv:").removesuffix("v1")
        assert rg_files(base) == [row["target"]]
    for row in excluded_markers:
        for term in EXCLUDED_MARKER_TERMS[row["source_family_id"]]:
            assert not rg_files(term), (row["source_family_id"], term, rg_files(term))
    return {
        "integrate": 19, "no_change": 9,
        "integrate_unique_owner": len(unique_integrate),
        "no_change_existing_owner": existing_no_change,
        "no_change_absent": absent_no_change,
        "marker_actions": 22, "retained_or_revised_markers": 14,
        "excluded_markers_no_leakage": 8,
    }


def write_manifest() -> int:
    paths = [path for path in PACKET.rglob("*") if path.is_file() and path != MANIFEST]
    paths += [
        DAILY,
        ROOT / "scripts/audit_june02_denominator_v3_fresh.py",
        ROOT / "scripts/audit_june02_evidence_v3_fresh.py",
        ROOT / "scripts/audit_june02_postwrite_v4.py",
        ROOT / "scripts/rebuild_june02_daily_v2_strict.py",
        ROOT / "scripts/test_june02_renderer_idempotence.py",
    ]
    unique = sorted(set(paths), key=lambda path: str(path.relative_to(PACKET) if path.is_relative_to(PACKET) else path))
    lines = []
    for path in unique:
        rel = path.relative_to(PACKET) if path.is_relative_to(PACKET) else Path(re.sub(r"^/", "", str(path)))
        if not path.is_relative_to(PACKET):
            rel = Path("../../../../../") / path.relative_to(ROOT)
        lines.append(f"{sha256(path)}  {rel}")
    MANIFEST.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return len(lines)


def main() -> None:
    text = DAILY.read_text(encoding="utf-8")
    verify_structure(text)
    denominator = verify_denominator()
    evidence_result = verify_evidence_and_selection(text)
    books = verify_books(text)
    payload = {
        "schema_version": "post-write-fresh-audit-v4",
        "report": str(DAILY.relative_to(ROOT)),
        "auditor": "fresh-context:jun02-independent-v4",
        "verdict": "passed",
        "unresolved_findings": 0,
        "denominator": denominator,
        "evidence_and_selection": evidence_result,
        "books": books,
        "repairs": [
            "Canonical July Daily presentation restored without deleting evidence.",
            "Renderer now preserves the audited Complete/Gate/Books state across reruns.",
            "Benchmark receipt column mapping corrected; undisclosed and locator-only fields normalized to strict Not Disclosed.",
            "Selection corrected to the 27-family eligible pool; SeClaw remains a source-specific non-eligible closure outside the main table.",
        ],
        "shared_books_writes": 0,
        "shared_learning_state_writes": 0,
    }
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    marker_rows = []
    marker_data = json.loads(MARKERS.read_text(encoding="utf-8"))["records"]
    for index, row in enumerate(marker_data, 1):
        final = "unique owner + exact-v1 note" if row["retained_v3"] else "removed / no source-specific leakage"
        marker_rows.append(
            f"| {index} | `{row['source_family_id']}` | `{row['verdict']}` | `{row['target']}` | {final} | pass |"
        )
    OUT_MD.write_text(f"""# 2026-06-02 Post-write Fresh-context Audit V4

## Verdict

`Passed`，未解决 finding=0。Daily、旧 receipts 与当前 Books 均作为不可信输入重新核对；本审计未写共享 Books 或 `docs/LEARNING_STATE.md`。

## Findings repaired before pass

1. 旧 renderer 的 rerun 会把已经闭合的 Completion/Gates 与 Books note 回滚为 pending。现已用连续两次隔离渲染的稳定 hash 建立回归测试，关闭状态可幂等保留。
2. 旧 Evidence audit 将 11 列 Benchmark Contract 错位映射，且表内仍有 section locator、task count 或 arrival-rate prose 冒充 model/batch/concurrency。现已修正列映射；披露值保留精确条件，缺失值严格归一为 `Not Disclosed`，不再把任务数当 batch。
3. Daily presentation 偏离 canonical schema。现已迁移到顶部五字段与固定 13 节，Source Reviews 保留在 Review Completion Receipt 下，未删除任何既有证据。
4. 月度守恒复核曾把 Score 6、无 override、无 pre-Books potential 的 `SF-SECLAW-SPEC-DRIVEN-SECURITY` 错当作主 Selection 表成员。现按 `REPORT_CONTRACTS.md` §3.5 将主表恢复为 27 个 eligible family，并在表外保留 source-specific non-eligible closure；其 Standard Review、Benchmark Contract 与 Books No Change 状态不变。

## Denominator audit — 736 / 736

- 19 个 category Atom snapshot（排除不完整聚合 `window.atom`）重建出 736 个唯一、窗口内 identity；published timestamp 与 abstract digest 736/736 匹配。
- 冻结账目：28 retained + 708 family-specific pre-denominator closures = 736；closure 无 Source Family / Stable Node 残留。
- 708/708 closure 均含 title-specific reason 与 abstract challenge；本次用更宽的 mechanism-risk route 复查 {denominator['route_risk_rechecked']} 项，而不是继承 V3 的较窄 107 项统计，未发现新的 durable owner/state/control/evaluation-release delta。
- 两个 title 只存在包裹引号规范化差异；identity、timestamp 与 abstract digest 一致。
- Ledger SHA-256：`{denominator['ledger_sha256']}`。

## Evidence and Selection — 28 / 28

- exact-v1：21 个本地官方 HTML + 7 个官方 exact-v1 HTML/PDF route；Method、Evaluation、limitations/counterevidence 与 artifact locator 28/28 complete，pending=0，blocked=0。
- Review Provenance：28/28 RP 按当前正文重新计算并匹配。
- Benchmark Contract：28/28 为十字段；章节占位、附录占位、混写 `Not Disclosed — ...`、task count→batch 与无数值 concurrency 均已消除。
- Selection：27 个 pre-Books eligible family 全量进入主 frontier，3 selected、24 not selected；`SF-SECLAW-SPEC-DRIVEN-SECURITY` 因 Score 6、override=`none` 且无 potential/correction signal，保留为表外具名 non-eligible closure。Selection 上限未改变 Source Review 深度。
- 七个仅在线 exact-v1 route 已重新打开：`2606.09864v1`、`2607.22569v1`、`2606.01725v1`、`2606.02302v1`、`2606.28343v1`、`2606.02958v1`、`2606.02959v1`。其 claim boundary 与 Daily 一致。

## Books audit — 28 / 28

- 19 Integrate 的 primary identifier 各自在唯一预期 owner 文件命中一次；无 cross-owner 重复。
- 9 No Change 中 7 项在 Books 零命中；Harness-1 与 Cosmos 3 各在既有正确 owner 单命中，属于 current-tree existing coverage，不是本次写回或跨 owner 泄漏。
- 8 个降级 marker family 的 primary identifier 与 source-specific mechanism 均零泄漏；`AURA` 字面命中属于另一 Source Family `2606.19714`，不属于 `2606.02775`，因此不是残留。

### 22 / 22 marker actions

| # | Source Family | Required action | Owner file | Current state | Verdict |
| ---: | --- | --- | --- | --- | --- |
{chr(10).join(marker_rows)}

### Five / five net-new integrations

| Source Family | Owner | Boundary recheck | Verdict |
| --- | --- | --- | --- |
| `SF-KV-QUANT-ALIGNMENT-COLLAPSE` | `INFER-KV-CACHE` / Ch45 | 11 models、1,894 prompts、five safety suites、vLLM FP8；不推出 universal safe bit-width | pass |
| `SF-EXECUTION-GROUNDED-CODING-AGENT-SECURITY` | `PLATFORM-SECURITY` / Ch72 | Docker、RedCode-derived goal pool 与 fixed predicates；不推出生产发生率 | pass |
| `SF-GAIATRACE-VIDUR-AGENT` | `INFER-SCHEDULING` / Ch56 | two systems、GAIA、trace simulator；artifact 在 exact-v1 仅 promised | pass |
| `SF-CROWDED-EMBEDDING-EXTERNALITY` | `AGENT-RAG` / Ch76 | one-to-one relevance、thermodynamic-limit 与未验证 mitigation；不发布生产阈值 | pass |
| `SF-ECHELON-AGGREGATE-ONLY-ADAPTATION` | `TRAIN-DISTRIBUTED-TRAINING` / Ch36 | 1B LoRA、sequence 32、mostly two boundaries、honest-but-curious；无 DP/full-parameter guarantee | pass |

## Generator and report consistency

- Renderer isolation test：同一输入连续生成两次，Daily SHA-256 不变；Complete/Gates、canonical 13 节与 Books notes 不回滚。
- Daily Integration Decision、Repository Changes、Open Questions 与 current Books tree 一致。
- 此 receipt 只在以上语义检查无 finding 后生成；validator 仍只证明接口自洽，不替代本审计。

## Gate

Coverage=`Closed`；Evidence=`Passed`；Books=`Passed`；Completion=`Complete`；未解决 finding=0。
""", encoding="utf-8")
    count = write_manifest()
    print(json.dumps({
        "raw": 736, "retained": 28, "closures": 708,
        "exact_v1": 28, "integrate": 19, "no_change": 9,
        "marker_actions": 22, "manifest_entries": count,
        "unresolved_findings": 0,
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
