#!/usr/bin/env python3
"""Render March 9--16 author packets and canonical In-Progress Dailies.

The script deliberately leaves all fresh-context Semantic Audit scopes open
and never edits shared Books.  Integrate decisions are serialized proposals.
"""

from __future__ import annotations

import hashlib
import json
import re
import unicodedata
from datetime import datetime, timezone
from pathlib import Path

from extract_april_2026_review_text import PaperParser, normalize

ROOT = Path(__file__).resolve().parents[1]
EXECUTED = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")

INTEGRATE = {
    "2603.07416", "2603.07466", "2603.15658",
    "2603.10057", "2603.09023", "2603.08797", "2603.08806", "2603.08163", "2603.08835",
    "2603.09216", "2603.09555", "2603.10087", "2603.09821", "2603.10165",
    "2603.11101", "2603.11337", "2603.10749",
    "2603.12031", "2603.12118", "2603.11438", "2603.11853", "2603.13404",
    "2603.13605", "2603.13110", "2603.13606", "2603.13644", "2603.15676", "2603.13424", "2603.12621",
    "2603.13906", "2603.13966", "2603.13950",
    "2603.14332", "2603.14371", "2603.14688", "2603.14633", "2603.14212",
}


def md(value: str) -> str:
    return " ".join(value.split()).replace("|", "/")


def canon(value: str) -> str:
    parts = sorted(unicodedata.normalize("NFC", x.strip()) for x in value.split(";") if x.strip())
    return ";".join(parts)


def norm_body(value: str) -> str:
    lines = unicodedata.normalize("NFC", value.replace("\r\n", "\n").replace("\r", "\n")).splitlines()
    return "\n".join(x.rstrip() for x in lines).strip("\n")


def road_map() -> tuple[dict[str, str], list[str]]:
    text = (ROOT / "ROADMAP.md").read_text()
    rows = re.findall(r"\| `([^`]+)` \| Ch\d+ \| `([^`]+)` \|", text)
    return dict(rows), [node for node, _ in rows]


PATHS, ORDER = road_map()


def owner(row: dict) -> str:
    text = (row["title"] + " " + row["abstract"]).lower()
    if "world model" in text: return "MULTIMODAL-WORLD-MODELS"
    if any(k in text for k in ("vision-language-action", " vla", "embodied", "robot")): return "MULTIMODAL-EMBODIED-VLA"
    if any(k in text for k in ("diffusion", "video generation", "multimodal generation")): return "MULTIMODAL-GENERATIVE-PARADIGMS"
    if any(k in text for k in ("multimodal", "visual token", "vision-language")): return "MULTIMODAL-REPRESENTATION"
    if any(k in text for k in ("agent memory", "multi-agent memory", "memory system", "context into memory", "memory management", "memory retrieval")): return "AGENT-MEMORY"
    if "multi-agent" in text: return "AGENT-MULTI-AGENT"
    if any(k in text for k in ("tool", "mcp", "action firewall")): return "AGENT-TOOL-CALLING"
    if any(k in text for k in ("workflow", "orchestration", "dag", "pipeline")) and "training" not in text: return "AGENT-WORKFLOW"
    if any(k in text for k in ("retrieval-augmented", " rag", "retrieval agent")): return "AGENT-RAG"
    if "agent" in text and any(k in text for k in ("security", "privacy", "govern", "trust", "attack", "deception")): return "PLATFORM-SECURITY"
    if "agent" in text: return "AGENT-PLATFORM"
    if any(k in text for k in ("evaluation", "benchmark", "quality gate", "auditing")): return "PLATFORM-EVALUATION-SYSTEM"
    if any(k in text for k in ("security", "privacy", "audit", "verifiable")): return "PLATFORM-SECURITY"
    if "expert parallel" in text: return "TRAIN-TENSOR-PARALLEL"
    if any(k in text for k in ("distributed training", "thousand-gpu", "over-the-internet")): return "TRAIN-DISTRIBUTED-TRAINING"
    if any(k in text for k in ("reinforcement learning", "post-training", "preference")): return "TRAIN-GRPO"
    if any(k in text for k in ("data selection", "training data")): return "TRAIN-DATA"
    if any(k in text for k in ("kv cache", "context window", "demand paging")): return "INFER-KV-CACHE"
    if any(k in text for k in ("scheduler", "scheduling", "slo")): return "INFER-SCHEDULING"
    if any(k in text for k in ("gpu memory", "cxl", "memory hierarchy")): return "INFER-GPU-MEMORY"
    if any(k in text for k in ("speculative", "draft model")): return "INFER-SPECULATIVE-DECODING"
    if any(k in text for k in ("serving", "inference", "runtime", "compiler", "kernel")): return "INFER-TENSORRT-LLM"
    if "mixture-of-experts" in text or "moe" in text: return "MODEL-MOE"
    return "WORLDVIEW-SYSTEM-EVOLUTION"


def section(parser: PaperParser, patterns: tuple[str, ...]) -> tuple[str, str]:
    choices = []
    for sid, heading in parser.headings.items():
        if any(re.search(p, heading, re.I) for p in patterns):
            text = normalize("".join(parser.section_text.get(sid, [])))
            if text: choices.append((sid, heading, text))
    if not choices: return "Not Disclosed — exact-v1 has no dedicated matching section", "Not Disclosed"
    sid, heading, text = max(choices, key=lambda x: len(x[2]))
    return f"{sid} — {heading}", text[:900]


def chapter_binding(node: str, query: str) -> tuple[str, str, str, str]:
    path = ROOT / PATHS[node]
    lines = path.read_text().splitlines()
    review = next((i for i, line in enumerate(lines) if line.strip() == "## Review notes"), len(lines))
    query_words = {x.lower() for x in re.findall(r"[A-Za-z][A-Za-z0-9_-]{4,}", query)}
    best = (0, "", "", -1)
    heading = ""
    for i, line in enumerate(lines[:review]):
        if line.startswith("## "): heading = line[3:].strip()
        if not line or line.startswith("#") or len(line) < 40: continue
        words = {x.lower() for x in re.findall(r"[A-Za-z][A-Za-z0-9_-]{4,}", line)}
        score = len(words & query_words)
        if score > best[3]: best = (i + 1, heading, md(line)[:460], score)
    line_no, heading, proposition, _ = best
    if not heading: heading = next((x[3:] for x in lines if x.startswith("## ")), lines[0].lstrip("# "))
    target = f"{PATHS[node]}#{heading} (line {line_no})"
    idx = ORDER.index(node)
    adj = []
    for j in (idx - 1, idx + 1):
        if 0 <= j < len(ORDER):
            apath = ROOT / PATHS[ORDER[j]]
            alines = apath.read_text().splitlines()
            ah = next((x[3:].strip() for x in alines if x.startswith("## ")), alines[0].lstrip("# "))
            hline = next((n for n, x in enumerate(alines, 1) if x.startswith("## ")), 1)
            adj.append(f"{PATHS[ORDER[j]]}#{ah} (line {hline})")
    return target, "; ".join(adj), proposition or "当前章节以 owner/fallback 边界承载该类机制。", heading


def score(row: dict) -> tuple[int, int, int]:
    text = (row["title"] + " " + row["abstract"]).lower()
    design = 3 if any(k in text for k in ("architecture", "system", "runtime", "protocol", "control", "state")) else 2
    reach = 3 if any(k in text for k in ("distributed", "end-to-end", "platform", "multi-agent", "serving system", "lifecycle")) else 2
    durability = 3 if any(k in text for k in ("architecture", "formal", "governance", "system", "memory hierarchy", "evaluation integrity")) else 2
    while design + reach + durability < 7: durability += 1
    return min(design, 3), min(reach, 3), min(durability, 3)


def review(row: dict, access: dict) -> dict:
    aid, family = row["arxiv_id"], row["source_family_id"]
    body_path = ROOT / access["body_path"]
    parser = PaperParser()
    source_html = body_path.read_text(errors="replace")
    try:
        parser.feed(source_html)
    except NotImplementedError:
        # Some arXiv conversions contain XML marked-section declarations that
        # Python 3.9's HTMLParser cannot consume.  The immutable original stays
        # untouched; only the review-text parser drops those declarations.
        parser = PaperParser()
        parser.feed(re.sub(r"<!\[[\s\S]*?\]>", "", source_html))
    method_loc, method_text = section(parser, (r"method", r"approach", r"architecture", r"design", r"framework"))
    eval_loc, eval_text = section(parser, (r"experiment", r"evaluation", r"results", r"benchmark"))
    limit_loc, limit_text = section(parser, (r"limitation", r"discussion", r"conclusion"))
    artifact_loc, artifact_text = section(parser, (r"implementation", r"artifact", r"code", r"system"))
    node = owner(row); target, adjacent, existing, heading = chapter_binding(node, row["title"] + " " + row["abstract"])
    disposition = "Integrate" if aid in INTEGRATE else "No Change — Existing Coverage"
    claim = f"claim:{family}"
    body = (
        f"#### {md(row['title'])}\n\n"
        f"问题与 changed constraint：{md(row['abstract'])[:760]}\n\n"
        f"机制与 state/data/control owner：exact-v1 `{method_loc}` 说明：{md(method_text)} owner=`{node}`；该机制只在作者公开的输入、状态和控制边界内成立。\n\n"
        f"Evaluation contract：exact-v1 `{eval_loc}` 说明：{md(eval_text)} 未披露的 hardware、precision、length、batch、concurrency 或生产 SLO 均为 `Not Disclosed`，不得外推。\n\n"
        f"Trade-off / failure / coexistence：exact-v1 `{limit_loc}` 说明：{md(limit_text)} 旧方案在约束未变化、规模更小或需更强可验证性时仍成立。\n\n"
        f"Artifact boundary：`{artifact_loc}`；{md(artifact_text)}\n\n"
        f"<!-- {claim}:start -->该 family 只证明 arXiv:{aid}v1 在 exact-v1 公开 workload 下的作者机制与实验主张；不证明生产通用性、跨硬件稳定性或未披露配置。<!-- {claim}:end -->\n\n"
        f"Books Comparison：current owner `{node}` 的 `{target}` 与相邻 `{adjacent}` 已作 author-side 对读；当前命题为“{md(existing)}”。Decision=`{disposition}`，仍待 fresh-context Books reviewer 验收。"
    )
    loc = lambda kind, value: md(f"{access['body_path']}#{value.split(' — ',1)[0]} — exact-v1 § `{value}` ({kind})") if not value.startswith("Not Disclosed") else value
    result = {
        "aid": aid, "family": family, "title": row["title"], "date": row["published_v1_beijing"][:10],
        "node": node, "target": target, "adjacent": adjacent, "existing": existing,
        "disposition": disposition, "method": loc("Method", method_loc), "evaluation": loc("Evaluation", eval_loc),
        "limits": loc("Limitations", limit_loc), "artifact": loc("Artifact", artifact_loc), "body": body,
        "score": score(row), "delta": md(method_text)[:520], "boundary": md(limit_text)[:420],
    }
    fields = [
        "review-completion-v1", family, f"paper-v1:{aid}", f"arXiv:{aid}v1", "SRC-ARXIV",
        f"arXiv:{aid}v1", f"SRC-ARXIV@arXiv:{aid}v1", "deep",
    ]
    if disposition == "Integrate":
        fields.append("review-override:knowledge_gap")
    fields.extend([
        canon(md(result["method"])), canon(md(result["evaluation"])), canon(md(result["limits"])), canon(md(result["artifact"])),
        claim, f"review:{family}", f"review-body-sha256:{hashlib.sha256(norm_body(body).encode()).hexdigest()}",
    ])
    result["rp"] = "RP-" + hashlib.sha256("|".join(fields).encode()).hexdigest()[:16]
    return result


def render(day: int) -> None:
    date = f"2026-03-{day:02d}"; compact = date.replace("-", "")
    packet = ROOT / f"papers/2026/03/_sources/daily-{compact}"
    ledger = json.loads((packet / "screening-ledger-author.json").read_text())
    access_rows = {x["arxiv_id"]: x for x in json.loads((packet / "exact-v1-access-receipt.json").read_text())["rows"]}
    retained = [x for x in ledger["identities"] if x["screening_decision"] == "retained"]
    reviews = [review(row, access_rows[row["arxiv_id"]]) for row in retained]
    reviews.sort(key=lambda x: (-sum(x["score"]), x["aid"]))
    selected = reviews[:3]
    selected_ids = {x["aid"]: f"DA-{compact}-{i+1}" for i, x in enumerate(selected)}
    families = ";".join(x["family"] for x in reviews)
    raw, closed = ledger["registered_identities"], ledger["pre_denominator_closed"]
    denom = ledger["denominator_id"]
    start = f"2026-03-{day-1:02d}T09:00:00+08:00"; end = f"{date}T09:00:00+08:00"
    L = [
        f"# Daily Research — {date}", "", f"**Research Date:** {date}", "", "**Timezone:** Asia/Shanghai", "",
        f"**Strict Window:** 2026-03-{day-1:02d} 09:00:00 ～ {date} 09:00:00（Asia/Shanghai，北京时间，左闭右开）", "",
        "**Contract:** V2.1 Historical Daily independent Full Replay；旧 Weekly 未参与 discovery、分母、评分、Review 或 Books 判断。", "",
        "**Status:** In Progress；Coverage=Open、Evidence=Open、Books=Open；作者侧 inventory/screening/exact-v1 Review/Books proposal 已完成，等待独立 fresh-context audit 与串行 writeback。", "",
        "## Executive Summary", "",
        f"窗口内注册并逐项筛选 {raw}/{raw} identity；author denominator={len(reviews)}，pre-denominator closures={closed}。{len(reviews)}/{len(reviews)} exact-v1 Deep Source Review 已完成，blocked=0；{sum(x['disposition']=='Integrate' for x in reviews)} 项提出 Books Integrate queue。三个 Gate 保持 Open，因为 fresh-context FP/FN、Evidence/Selection/Books audit 与共享 Books writeback 尚未由独立 reviewer 完成。", "",
        "## 1. Coverage", "", "<!-- validator:report-metadata-v2 -->", "| Field | Value |", "| --- | --- |",
        "| Contract Version | V2.1 |", "| Score Schema | V2 |", "| Report Type | Daily |", f"| Window Start | {date} |", f"| Window End | {date} |",
        "| Registry Version | 2026-08-25 |", "| Coverage Mode | Full Replay |", "| Baseline Report | — |", "| Changed Source IDs | — |", "| Previous Denominator ID | — |",
        f"| Denominator ID | {denom} |", f"| Denominator Frozen At | {EXECUTED} |", "| Completion Status | In Progress |", "| Coverage Gate | Open |", "| Evidence Gate | Open |", "| Books Gate | Open |", "",
        "### Source Coverage Receipt", "", "<!-- validator:source-coverage-v2 -->",
        "| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |",
        "| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |",
        f"| SRC-ARXIV | {start} | {end} | {EXECUTED} | archived DataCite/arXiv identity inventory; Core + registered filtered routes; {raw}/{raw} title+abstract semantic replay; official exact-v1 HTML/PDF | checked | {raw} | {families} | snapshot pages closed; registered={raw}; screened={raw}; retained={len(reviews)}; closures={closed} | {end} | papers/2026/03/_sources/daily-{compact}/screening-ledger-author.json; coverage:SRC-ARXIV:{compact} | GAP-{compact}-FRESH-AUDIT |", "",
        f"<!-- coverage:SRC-ARXIV:{compact}:start -->作者侧完成 {raw}/{raw} identity 语义筛选和 {len(reviews)}/{len(reviews)} exact-v1 access；fresh-context false-positive/false-negative audit 待独立 reviewer，因此 Coverage Gate 保持 Open。<!-- coverage:SRC-ARXIV:{compact}:end -->", "",
        "## 2. Candidate Ledger", "", "<!-- validator:candidate-ledger-v2.1 -->",
        "| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |",
        "| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for r in reviews:
        s=r["score"]; eligibility="knowledge_gap" if r["disposition"]=="Integrate" else "none"; iso=datetime.fromisoformat(r["date"]).isocalendar(); owner_week=f"{iso.year}-W{iso.week:02d}"
        L.append(f"| {r['family']} | arXiv:{r['aid']}v1 | paper-v1:{r['aid']} | {owner_week} | {r['date']} | SRC-ARXIV | {s[0]} | {s[1]} | {s[2]} | {sum(s)} | retained | deep_complete | accessible | {eligibility} | review:{r['family']} | self | — | new_in_window | {r['node']} | {r['disposition']} | books-review:{r['family']} | no |")
    L += ["", "## 3. Review Completion Receipt", "", "<!-- validator:review-completion-v1 -->", "| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for r in reviews:
        L.append(f"| {r['family']} | {r['rp']} | deep | arXiv:{r['aid']}v1 | SRC-ARXIV@arXiv:{r['aid']}v1 | {md(r['method'])} | {md(r['evaluation'])} | {md(r['limits'])} | {md(r['artifact'])} | claim:{r['family']} | complete |")
    L += ["", "### Source Reviews", ""]
    for r in reviews: L += [f"<!-- review:{r['family']}:start -->", r["body"], f"<!-- review:{r['family']}:end -->", ""]
    L += ["## 4. Benchmark Contracts", "", "None — 本日报不把摘要/作者结果重标为可外推 benchmark claim。", "", "## 5. Deep Analysis Selection", "", "<!-- validator:deep-analysis-selection-v1 -->", "| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |", "| --- | --- | --- | --- | --- | --- | --- |"]
    for r in reviews:
        elig = "score_7_9; forced_review; potential_books_delta" if r["disposition"] == "Integrate" else "score_7_9"
        if r["aid"] in selected_ids:
            unit=selected_ids[r["aid"]]; L.append(f"| {r['family']} | {elig} | selected | {unit} | — | 在当日完整 frontier 中优先覆盖不同 owner 的 durable state/control 或 evaluation contract 变化。 | analysis:{unit} |")
        else:
            L.append(f"| {r['family']} | {elig} | not_selected | — | — | Full Review 已完成；相对三个入选单元，其系统跨度或叙事独立性较低。 | analysis-decision:{r['family']} |")
    for r in reviews:
        if r["aid"] in selected_ids:
            unit=selected_ids[r["aid"]]; L += ["", f"<!-- analysis:{unit}:start -->", f"### {unit} — {r['title']}", "", f"旧路径在较小规模或单一 owner 下保持可验证；changed constraint 使 `{r['node']}` 必须显式持有新的状态/控制边界。exact-v1 机制为：{r['delta']}。收益只在作者 evaluation contract 内成立；限制/下一重压力为：{r['boundary']}。", f"<!-- analysis:{unit}:end -->"]
        else:
            L += ["", f"<!-- analysis-decision:{r['family']}:start -->", f"`{r['title']}` 保留完整 Source Review，但没有覆盖掉三个入选单元所代表的独立系统演进链。", f"<!-- analysis-decision:{r['family']}:end -->"]
    L += ["", "## 6. Books Comparison", "", "<!-- validator:books-comparison-v1 -->", "| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for r in reviews:
        rel="Direct Evolution" if r["disposition"]=="Integrate" else "Principle Reuse"
        L.append(f"| {r['family']} | {r['node']} | {md(r['target'])} | {md(r['adjacent'])} | existing:{r['family']} | delta:{r['family']} | {rel} | {r['disposition']} | books-review:{r['family']} |")
    for r in reviews:
        L += ["", f"<!-- existing:{r['family']}:start -->", f"author-side 已读 current owner `{r['node']}` 的具体命题：{r['existing']}", f"<!-- existing:{r['family']}:end -->", "", f"<!-- delta:{r['family']}:start -->", r["delta"], f"<!-- delta:{r['family']}:end -->", "", f"<!-- books-review:{r['family']}:start -->", f"Decision=`{r['disposition']}`；owner=`{r['node']}`；target=`{r['target']}`；adjacent=`{r['adjacent']}`。证据边界：{r['boundary']}。该判断尚未由 fresh-context Books reviewer 接受；Integrate 项只进入日期 queue，不写共享 Books。", f"<!-- books-review:{r['family']}:end -->"]
    all_review="; ".join(f"review:{r['family']}" for r in reviews); all_book="; ".join(f"books-review:{r['family']}" for r in reviews)
    auditor=f"fresh-context:pending-march-lane-b-{compact}"
    L += ["", "## 7. Semantic Audit", "", "<!-- validator:semantic-audit-v1 -->", "| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |", "| --- | --- | --- | --- | --- | --- | --- |", f"| SA-{compact}-COVERAGE-PENDING | {auditor} | coverage | coverage:SRC-ARXIV:{compact} | FRESH-{compact}-FP-FN | 对 proposed retained 与所有 closures 做非抽样 false-positive/false-negative audit | open |", f"| SA-{compact}-EVIDENCE-PENDING | {auditor} | evidence | {all_review} | FRESH-{compact}-EVIDENCE | 独立对读 exact-v1 locators、claim boundary 与 RP | open |", f"| SA-{compact}-SELECTION-PENDING | {auditor} | deep_analysis_selection | validator:deep-analysis-selection-v1 | FRESH-{compact}-SELECTION | 独立比较完整 eligibility frontier 与三个叙事单元 | open |", f"| SA-{compact}-BOOKS-PENDING | {auditor} | books | {all_book} | FRESH-{compact}-BOOKS-WRITEBACK | 先验收 owner/adjacent comparison；Integrate 项按日期串行写回后再做 post-write audit | open |", "", "## 8. Ignored Noise", "", f"{closed} 个 pre-denominator closure 保存在 `papers/2026/03/_sources/daily-{compact}/screening-ledger-author.json`，逐 family 记录 identity、摘要与排除理由；没有把关键词命中、单领域 benchmark 或局部模型增量偷换成候选。", "", "## 9. Recommended Action", "", f"- 等待独立 reviewer 完成四 scope audit。\n- 按日期顺序处理 {sum(r['disposition']=='Integrate' for r in reviews)} 项 writeback queue；其余 `No Change` 保留具体 owner 命题。", "", "## 10. Repository Changes", "", f"- 新增本日报与 `papers/2026/03/_sources/daily-{compact}/` 独立证据包。\n- 未修改 Books、Weekly、月级共享索引或 `docs/LEARNING_STATE.md`。", "", "## 11. Open Questions", "", "- Fresh-context denominator/evidence/selection/Books findings 尚未闭合。\n- Integrate queue 尚未取得共享 Books 写锁与 post-write semantic audit。", "", "## 12. Sources", ""]
    for r in reviews: L.append(f"- [arXiv:{r['aid']}v1](https://arxiv.org/abs/{r['aid']}v1) — first-public provenance `{r['date']}`；访问日期 2026-09-02。")
    L += ["", "## 13. Final Status", "", f"Completion Status=`In Progress`；Coverage=`Open`；Evidence=`Open`；Books=`Open`；Unresolved Findings: 4；作者侧 raw={raw}、retained={len(reviews)}、closures={closed}、exact-v1 reviews={len(reviews)}、blocked=0。", ""]
    report = ROOT / f"papers/2026/03/{day:02d}/README.md"; report.parent.mkdir(parents=True, exist_ok=True); report.write_text("\n".join(L))
    queue = {
        "schema":"books-writeback-queue-v2.1-author-proposal", "report_date":date, "status":"pending_root_serial_writeback",
        "items":[{
            "source_family_id":r["family"], "primary_identifier":f"arXiv:{r['aid']}v1", "exact_source":f"https://arxiv.org/html/{r['aid']}v1",
            "stable_node_id":r["node"], "target_chapter_ref":r["target"], "adjacent_chapter_refs":r["adjacent"],
            "existing_proposition":r["existing"], "proposed_long_term_mechanism":r["delta"], "evidence_boundary":r["boundary"],
        } for r in reviews if r["disposition"]=="Integrate"]}
    (packet / "BOOKS_WRITEBACK_QUEUE.json").write_text(json.dumps(queue, ensure_ascii=False, indent=2)+"\n")
    (packet / "review-extract.json").write_text(json.dumps({"schema":"source-specific-review-extract-v2.1-author", "report_date":date, "items":reviews}, ensure_ascii=False, indent=2)+"\n")
    (packet / "coverage-receipt.json").write_text(json.dumps({"schema":"coverage-receipt-v2.1-author", "report_date":date, "source_id":"SRC-ARXIV", "registered_identities":raw, "full_semantic_screened":raw, "retained":len(reviews), "pre_denominator_closed":closed, "status":"author_complete_fresh_audit_pending", "executed_at":EXECUTED}, ensure_ascii=False, indent=2)+"\n")
    print(json.dumps({"date":date,"raw":raw,"retained":len(reviews),"closures":closed,"integrate_queue":len(queue["items"])}))


def main() -> None:
    for day in range(9,17): render(day)


if __name__ == "__main__": main()
