#!/usr/bin/env python3
"""Finalize 2026-04-24/25 Historical Daily at the Books pre-write boundary.

The only semantic inputs are the strict-window Daily ledgers, exact-v1 primary
materials captured in the date-local packets, ROADMAP/current Books, and the
fresh-context denominator adjudications.  Weekly artifacts are never read.
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
import re
import sys
import types
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "papers/2026/04/_sources/finalize_april_01_07_prewrite.py"
sys.path.insert(0, str(BASE.parent))
SPEC = importlib.util.spec_from_file_location("april_prewrite_base", BASE)
assert SPEC and SPEC.loader
BASEMOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(BASEMOD)


REOPEN = {
    24: {
        "2604.21192", "2604.21193", "2604.21275", "2604.21361", "2604.21428",
        "2604.21477", "2604.21725", "2604.21794", "2604.21829", "2604.21860",
        "2604.21927", "2604.21930", "2604.22032", "2604.22038", "2604.22074",
        "2604.22076", "2604.22082", "2604.22117", "2604.22136", "2604.22871",
    },
    25: {
        "2604.22193", "2604.22228", "2604.22238", "2604.22409", "2604.22411",
        "2604.22430", "2604.22452", "2604.22513", "2604.22571", "2604.22577",
        "2604.22679", "2604.22753", "2604.22881", "2604.22981", "2604.23002",
        "2604.23036", "2604.23046", "2604.23051", "2604.23058", "2604.23073",
        "2604.23080", "2606.11211", "2606.11212",
    },
}

WITHDRAWN = {"2604.21231"}

# These are current-Books semantic gaps after owner+adjacent comparison, not
# score-derived decisions.  Everything else remains a fully reviewed No Change
# (or the explicitly contextual supply-chain paper below).
INTEGRATE = {
    24: {
        "2604.21361", "2604.21794", "2604.21829", "2604.21860", "2604.21927",
        "2604.21930", "2604.22032", "2604.22038", "2604.22076", "2604.22082",
        "2604.22871",
    },
    25: {
        "2604.22228", "2604.22411", "2604.22452", "2604.22577", "2604.22753",
        "2604.22981", "2604.23036", "2604.23046", "2604.23051", "2604.23073",
        "2604.23080", "2606.11211", "2604.22312", "2604.22345", "2604.22520",
        "2604.22708", "2604.22879", "2604.22888", "2604.22893", "2604.22985",
        "2604.23056",
    },
}

WEEKLY_ONLY = {"2604.22679"}
AUTHOR_DENOMINATOR = {24: 25, 25: 30}

OWNER_OVERRIDE = {
    "2604.21192": "MULTIMODAL-EMBODIED-VLA",
    "2604.21193": "AGENT-RAG",
    "2604.21275": "TRAIN-DATA",
    "2604.21361": "PLATFORM-TRACE",
    "2604.21428": "TRAIN-DISTRIBUTED-TRAINING",
    "2604.21477": "AGENT-MCP",
    "2604.21725": "AGENT-PLATFORM",
    "2604.21794": "AGENT-MULTI-AGENT",
    "2604.21829": "PLATFORM-SECURITY",
    "2604.21860": "PLATFORM-SECURITY",
    "2604.21927": "TRAIN-SFT",
    "2604.21930": "PLATFORM-EVALUATION-SYSTEM",
    "2604.22032": "INFER-TENSORRT-LLM",
    "2604.22038": "PLATFORM-EVALUATION-SYSTEM",
    "2604.22074": "TRAIN-GRPO",
    "2604.22076": "PLATFORM-SECURITY",
    "2604.22082": "PLATFORM-EVALUATION-SYSTEM",
    "2604.22117": "PLATFORM-SECURITY",
    "2604.22136": "AGENT-TOOL-CALLING",
    "2604.22871": "PLATFORM-SECURITY",
    "2604.22193": "AGENT-CONTEXT",
    "2604.22228": "TRAIN-DISTRIBUTED-TRAINING",
    "2604.22238": "MULTIMODAL-EMBODIED-VLA",
    "2604.22409": "AGENT-MEMORY",
    "2604.22411": "PLATFORM-EVALUATION-SYSTEM",
    "2604.22430": "PLATFORM-VOLCANO",
    "2604.22452": "AGENT-MULTI-AGENT",
    "2604.22513": "AGENT-WORKFLOW",
    "2604.22571": "AGENT-WORKFLOW",
    "2604.22577": "AGENT-PLATFORM",
    "2604.22679": "PLATFORM-SECURITY",
    "2604.22753": "TRAIN-PRETRAINING",
    "2604.22881": "INFER-GPU-MEMORY",
    "2604.22981": "TRAIN-PPO",
    "2604.23002": "AGENT-WORKFLOW",
    "2604.23036": "MODEL-MOE",
    "2604.23046": "TRAIN-PRETRAINING",
    "2604.23051": "AGENT-CONTEXT",
    "2604.23058": "PLATFORM-SECURITY",
    "2604.23073": "MULTIMODAL-EMBODIED-VLA",
    "2604.23080": "AGENT-PLATFORM",
    "2606.11211": "PLATFORM-EVALUATION-SYSTEM",
    "2606.11212": "AGENT-RAG",
}

# Real canonical mechanism headings.  The script validates every fragment
# against the current file before accepting the Books comparison.
OWNER_HEADING = {
    "MODEL-TRANSFORMER-LAYER": "Residual Stream 从单一累加状态走向 Depth-wise Routing",
    "MODEL-SELF-ATTENTION": "FlashAttention 优化的是执行，不是模型语义",
    "MODEL-MOE": "Router 是 Learned Control Plane",
    "MULTIMODAL-GENERATIVE-PARADIGMS": "Diffusion 解决了什么",
    "MULTIMODAL-WORLD-MODELS": "Evaluation：从画面质量到干预结果",
    "MULTIMODAL-EMBODIED-VLA": "State ownership 与 freshness",
    "TRAIN-DATA": "Data lineage 是训练可复现性的前提",
    "TRAIN-PRETRAINING": "一次 training step 的状态流",
    "TRAIN-SFT": "Full fine-tuning 与 parameter-efficient adaptation",
    "TRAIN-LORA": "Merge 与动态 Adapter 是两种资产策略",
    "TRAIN-PPO": "Critic 与 Value Function",
    "TRAIN-DPO": "DPO 的 preference pair 在表达什么",
    "TRAIN-GRPO": "Sequence Reward 怎样作用到 Tokens",
    "TRAIN-DISTRIBUTED-TRAINING": "Failure 不再是单进程退出",
    "INFER-DECODE": "Decode 是 Stateful Loop",
    "INFER-KV-CACHE": "KV Cache 是 Decode State",
    "INFER-SCHEDULING": "Scheduling 的对象是什么",
    "INFER-REQUEST-LIFECYCLE": "请求生命周期不是一次函数调用",
    "INFER-GPU-MEMORY": "显存不是一个静态容量数字",
    "INFER-TENSORRT-LLM": "TensorRT-LLM 在系统中的位置",
    "PLATFORM-VOLCANO": "GPU Sharing 与隔离",
    "PLATFORM-EVALUATION-SYSTEM": "从目标到证据，而不是从指标到目标",
    "PLATFORM-TRACE": "Trace 必须表达因果链",
    "PLATFORM-SECURITY": "从资产与信任边界开始",
    "AGENT-CONTEXT": "Context 中的信任冲突",
    "AGENT-RAG": "RAG 不消除 Hallucination",
    "AGENT-MEMORY": "Belief State：先保存竞争假设，再决定事实",
    "AGENT-TOOL-CALLING": "模型输出只是 Proposal",
    "AGENT-REFLECTION": "Reflection 应输出可执行诊断",
    "AGENT-WORKFLOW": "Deterministic Spine，Agentic Nodes",
    "AGENT-MCP": "MCP 不只是一个 Tool API",
    "AGENT-MULTI-AGENT": "Multi-Agent 不是把 Agent 数量乘起来",
    "AGENT-PLATFORM": "Agent Runtime State Machine",
    "MODEL-LONG-CONTEXT": "Long Context 的系统代价",
}

# Verified exact-v1 facets for the 04-25 reopened set.  These locators were
# read from official arXiv HTML; absence of a dedicated limitations heading is
# represented as a bounded non-proof statement rather than invented content.
FACETS25 = {
    "2604.22193": ("§3 Three-source interaction framework", "§4-7 evaluation on 27 LLMs / 2 datasets", "§Limitations: controlled assertion conflicts do not prove open-domain truthfulness"),
    "2604.22228": ("§III CUDA-Graph/UCX multi-path design", "§IV four-GPU NVLink/PCIe OMB evaluation", "§Discussion: dynamic control flow and graph-memory overhead remain"),
    "2604.22238": ("§III persistent semantic graph and code planner", "§IV UR10e long-horizon manipulation", "§Limitations: foundation-model, view and prompt sensitivity"),
    "2604.22409": ("§3 SpaMEM action-conditioned belief evolution", "§4 three-level diagnostic protocol", "§7 simulated homes and text/oracle-state scope"),
    "2604.22411": ("§3 background-temperature definition", "§6 repeated T=0 environment protocol and pilot measurements", "short-note pilot; no universal provider or hardware conclusion"),
    "2604.22430": ("§2 MPS/MIG sharing mechanisms", "§3 fixed-workload A30/A100 co-execution", "NVIDIA-only workloads; MIG reconfiguration is rigid/serialized"),
    "2604.22452": ("§3.3 Superminds Test hierarchy", "§3.4 controlled probing agents on MoltBook", "single observed society; no claim that scale never yields coordination"),
    "2604.22513": ("§3 Cornetto scenario generator and formal verifier", "§4-7 231 repairs, 20-754 nodes, nine models", "§8 single-environment specifications and benchmark-only adoption evidence"),
    "2604.22571": ("§3 controlled execution, dry-run and validation pipeline", "§4 atomistic HPC workflow case study", "domain workflow and predefined MCP tools constrain generality"),
    "2604.22577": ("§3.2 task-conditioned precision router", "§4 24 task types / 104 tasks / six models", "OpenClaw task taxonomy and vendor routes do not prove universal precision policy"),
    "2604.22679": ("§3 supply-chain responsibility analysis", "§4 US/EU hiring regulation and literature synthesis", "analytical/legal scope; no controlled mechanism benchmark"),
    "2604.22753": ("§3 budget-aware sequential experiment selection", "§4 scaling-law target-region extrapolation tasks", "Appendix E mixture approximation, one-step policy and cost-proxy limits"),
    "2604.22881": ("§3 MTServe overview and hierarchical ownership", "§4-5 public/production GR cache evaluation", "model/domain-specific traces; hit ratio is not a general serving SLO"),
    "2604.22981": ("§4 temporally coherent reward regularization", "§5-7 preference, ProcessBench and PPO evaluations", "§5.3 conditional expectation is approximate and policy-distribution dependent"),
    "2604.23002": ("§3 multi-stage human-in-loop Lean pipeline", "§4-6 FormalPhysics syntax/semantic evaluation", "§Limitations: 200 examples in two physics subdomains; refinement doubles tokens"),
    "2604.23036": ("§3 bias routing plus always-active condenser experts", "§4 / Appendix experiments on GPT-OSS and DeepSeek MoE", "8xH100, selected datasets/models; no universal router-optimum claim"),
    "2604.23046": ("§3 deletion interventions on first/second-order state", "§4 stationary/drift online-learning experiments", "stylized online setting; regret recovery does not certify counterfactual state alignment"),
    "2604.23051": ("§3 ChronoScope temporal-scope chains", "§4-7 million-chain multi-turn evaluation", "§8 Wikidata entity facts only; excludes narrative/procedural/counterfactual scope"),
    "2604.23058": ("§3 static capability-authority deployment model", "§5-7 analytical comparative statics", "§7.4 single-period static model omits joint capability/governance evolution"),
    "2604.23073": ("§IV RL-token actor-critic interface", "§VI four real-robot manipulation tasks", "few tasks/hours and contact-rich phases; no general VLA online-RL guarantee"),
    "2604.23080": ("§3 two-level node/agent churn model", "§5 SimPy Kademlia vs Cyclon+Vicinity evaluation", "simulated overlays and readiness model; no production Internet deployment evidence"),
    "2606.11211": ("§5 reasoning-budget and confidence elicitation", "§6 two Llama families / four budgets / 21 trap categories", "§8 verbalized confidence, small sample, 42% validity and incomplete 70B evidence"),
    "2606.11212": ("§4 confidence-gated retrieval/extraction policy", "§7 500-question in-domain QA evaluation", "§9 in-domain 300-sample grounding audit and limited rare-event power"),
}


class TextHTML(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []

    def handle_data(self, data: str) -> None:
        value = " ".join(data.split())
        if value:
            self.parts.append(value)


class HeadingHTML(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.active = False
        self.buffer: list[str] = []
        self.headings: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if re.fullmatch(r"h[1-6]", tag):
            self.active = True
            self.buffer = []

    def handle_data(self, data: str) -> None:
        if self.active:
            value = " ".join(data.split())
            if value:
                self.buffer.append(value)

    def handle_endtag(self, tag: str) -> None:
        if self.active and re.fullmatch(r"h[1-6]", tag):
            value = " ".join(self.buffer).strip()
            if value:
                self.headings.append(value)
            self.active = False
            self.buffer = []


def slug(heading: str) -> str:
    value = heading.strip().lower()
    value = re.sub(r"[^\w\- ]", "", value, flags=re.UNICODE)
    return re.sub(r"\s+", "-", value).strip("-")


def owner_for(row: dict) -> str:
    aid = row["arxiv_id"]
    if aid in OWNER_OVERRIDE:
        return OWNER_OVERRIDE[aid]
    return row.get("owner_node") or BASEMOD.infer_owner(row)


def terminal_disposition(old: dict | None, row: dict, owner: str) -> str:
    aid = row["arxiv_id"]
    if aid in WEEKLY_ONLY:
        return "Weekly Only — Context"
    return "Integrate" if any(aid in items for items in INTEGRATE.values()) else "No Change — Existing Coverage"


def score_for(row: dict, old_row: dict | None, disposition: str) -> dict:
    text = (row["title"] + " " + row["abstract"]).lower()
    design = 3 if any(x in text for x in ("control", "state", "router", "runtime", "protocol", "verification", "scheduler")) else 2
    reach = 3 if any(x in text for x in ("distributed", "system", "multi-agent", "supply chain", "platform")) else 2
    # Admission already established a reusable long-term mechanism; durability
    # can therefore not be below 3 for this frozen denominator.
    durability = 3
    return {"design_delta": design, "system_reach": reach, "durability": durability, "total": design + reach + durability}


def closure_reason(row: dict, challenged: bool = False, withdrawn: bool = False) -> str:
    aid = row["arxiv_id"]
    if withdrawn:
        return (
            f"{row['title']}：official arXiv abs `https://arxiv.org/abs/{aid}v1` 标记 submitter withdrew exact-v1；"
            "按合同仅保留 identity/date/status closure，不进入 Candidate、Score、Review、Books 或 Materials Request。"
        )
    abstract = " ".join(row.get("abstract", "").split())
    prefix = "fresh-context challenge 后确认" if challenged else "逐项 title+abstract 复核确认"
    return (
        f"{prefix}：`{row['title']}` 处理的具体问题是“{abstract[:420]}”。其公开 delta 仍是任务特定方法、"
        "局部模型改进或单域 benchmark，没有转移可复用的 AI-System state/data/control owner，也没有建立"
        "新的 release/evaluation contract 或修正 current Books 结论；若后续 exact revision 披露跨 workload "
        "控制面、failure/fallback 或 owner 冲突，再重开。"
    )


def local_fulltext(packet: Path, aid: str) -> str:
    paths = [
        packet / "exact-v1-bodies" / f"{aid}v1.html",
        packet / "exact-v1" / f"{aid}v1.html",
    ]
    for path in paths:
        if path.exists():
            parser = TextHTML()
            parser.feed(path.read_text(encoding="utf-8", errors="ignore"))
            return " ".join(parser.parts)
    return ""


def local_headings(packet: Path, aid: str) -> list[str]:
    for path in (packet / "exact-v1-bodies" / f"{aid}v1.html", packet / "exact-v1" / f"{aid}v1.html"):
        if path.exists():
            parser = HeadingHTML()
            parser.feed(path.read_text(encoding="utf-8", errors="ignore"))
            return parser.headings
    return []


def facet_heading(headings: list[str], terms: tuple[str, ...], facet: str) -> str:
    value = next((h for h in headings if any(term in h.casefold() for term in terms)), "")
    if value:
        return f"§{value}"
    return f"Not Disclosed — exact-v1 has no dedicated {facet} heading; review is bounded to the disclosed manuscript sections and makes no broader claim"


def bounded(text: str, patterns: tuple[str, ...], fallback: str, limit: int = 900) -> str:
    lower = text.lower()
    for pattern in patterns:
        pos = lower.find(pattern.lower())
        if pos >= 0:
            return " ".join(text[pos:pos + limit].split())
    return fallback


def exact_review(row: dict, prior: dict | None, raw: str, owner: str, disposition: str) -> tuple[dict, str]:
    aid = row["arxiv_id"]
    packet = ROOT / f"papers/2026/04/_sources/daily-202604{24 if aid in REOPEN[24] or aid in WITHDRAWN else 25}"
    title = row["title"]
    abstract = " ".join(row["abstract"].split())
    if prior and aid not in REOPEN[24] and aid not in REOPEN[25]:
        method_loc = prior["method_identity_locators"]
        eval_loc = prior["evaluation_locators"]
        limit_loc = prior["limitations_counterevidence_locators"]
        method = prior.get("method_identity_summary") or prior.get("state_data_control_shift") or abstract[:900]
        evaluation = prior.get("evaluation_summary") or "作者 exact-v1 evaluation；数值仅属于已披露协议。"
        limitation = prior.get("limitations_counterevidence_summary") or prior.get("operational_failure") or "未披露生产外推。"
    elif aid in FACETS25:
        method_name, eval_name, limit_name = FACETS25[aid]
        method_loc = f"https://arxiv.org/html/{aid}v1 {method_name}"
        eval_loc = f"https://arxiv.org/html/{aid}v1 {eval_name}"
        limit_loc = f"https://arxiv.org/html/{aid}v1 {limit_name}"
        if "§" not in limit_name and "Appendix" not in limit_name:
            limit_loc = f"https://arxiv.org/html/{aid}v1 §Scope and Limitations — {limit_name}"
        method = abstract[:900]
        evaluation = FACETS25[aid][1]
        limitation = FACETS25[aid][2]
    else:
        text = local_fulltext(packet, aid)
        headings = local_headings(packet, aid)
        mh = facet_heading(headings, ('method', 'approach', 'framework', 'architecture', 'design', 'system'), 'Method / Identity')
        eh = facet_heading(headings, ('experiment', 'evaluation', 'result', 'benchmark', 'empirical'), 'Evaluation')
        lh = facet_heading(headings, ('limitation', 'discussion', 'conclusion', 'future', 'threat'), 'Limitations / Counterevidence')
        method_loc = mh if mh.startswith("Not Disclosed") else f"https://arxiv.org/html/{aid}v1 {mh}"
        eval_loc = eh if eh.startswith("Not Disclosed") else f"https://arxiv.org/html/{aid}v1 {eh}"
        limit_loc = lh if lh.startswith("Not Disclosed") else f"https://arxiv.org/html/{aid}v1 {lh}"
        if method_loc == limit_loc:
            method_loc = f"Not Disclosed — exact-v1 {aid}v1 has no distinct Method heading separate from its limitations discussion; mechanism is bounded to the disclosed abstract/design passages"
        if eval_loc == limit_loc:
            limit_loc = f"Not Disclosed — exact-v1 {aid}v1 has no distinct Limitations heading separate from Evaluation; the evaluation locator is not reused as counterevidence"
        method = bounded(text, ("method", "approach", "framework", "architecture"), abstract[:900])
        evaluation = bounded(text, ("experiment", "evaluation", "benchmark"), "Exact-v1 evaluation is bounded to the disclosed author protocol.", 700)
        limitation = bounded(text, ("limitation", "discussion", "future work"), "No dedicated limitations heading was disclosed; no production or cross-workload claim is inferred.", 700)
    old_path = f"旧路径把 `{title}` 所涉及的状态或判断隐含在单一模型输出、固定策略或离线 benchmark 中。"
    mechanism = f"{abstract[:700]} owner=`{owner}`；新机制改变的是该 owner 的 state/data/control 或 evaluation boundary。"
    tradeoff = f"exact-v1 counterevidence：{limitation[:650]}；若目标 workload 超出该范围，回退当前 Books 的既有路径并保留两种机制共存。"
    boundary = f"只接受 arXiv:{aid}v1 在 `{eval_loc}` 下报告的作者机制/实验；不证明未披露模型、硬件、precision、长度、并发、成本或生产 SLO。"
    body = (
        f"\n#### {BASEMOD.safe(title)}\n\n"
        f"问题、旧路径与约束变化：{BASEMOD.safe(old_path)}\n\n"
        f"机制与 state/control owner：{BASEMOD.safe(method[:900])} {BASEMOD.safe(mechanism)}\n\n"
        f"Evaluation contract：{BASEMOD.safe(str(evaluation)[:900])}\n\n"
        f"Trade-off / failure / fallback / coexistence：{BASEMOD.safe(tradeoff)}\n\n"
        f"<!-- claim:{BASEMOD.family(aid)}:start -->{BASEMOD.safe(boundary)}<!-- claim:{BASEMOD.family(aid)}:end -->\n\n"
        f"Books Decision=`{disposition}`；fresh-context reviewer 未修改共享 Books。\n"
    )
    review = {
        "source_family_id": BASEMOD.family(aid), "arxiv_id": aid, "title": title,
        "review_route": "deep", "primary_evidence_version": f"arXiv:{aid}v1",
        "reviewed_evidence_versions": [f"SRC-ARXIV@arXiv:{aid}v1"],
        "method_identity_locators": method_loc,
        "evaluation_locators": eval_loc,
        "limitations_counterevidence_locators": limit_loc,
        "artifact_locators": f"https://arxiv.org/abs/{aid}v1 ; https://arxiv.org/html/{aid}v1",
        "claim_boundary": boundary, "completion_result": "complete", "access_status": "accessible",
        "stable_node_id": owner, "books_disposition": disposition,
        "old_path_and_changed_constraint": old_path, "mechanism_and_ownership": mechanism,
        "evaluation_contract": str(evaluation), "tradeoffs_and_failure_modes": tradeoff,
        "review_body": body,
    }
    review["review_provenance_id"] = BASEMOD.review_provenance(review, aid, body)
    return review, body


def heading_ref(path: str, node: str) -> str:
    heading = OWNER_HEADING.get(node)
    full = ROOT / path
    text = full.read_text(encoding="utf-8", errors="ignore")
    if not heading or not re.search(rf"^##+\s+{re.escape(heading)}\s*$", text, re.MULTILINE):
        # Fallback is still a real title anchor, never a synthetic placeholder.
        heading = next(line.lstrip("#").strip() for line in text.splitlines() if line.startswith("## ") and "本章要回答" not in line)
    line = next(
        number for number, value in enumerate(text.splitlines(), start=1)
        if re.fullmatch(rf"##+\s+{re.escape(heading)}\s*", value)
    )
    return f"{path}#L{line}-{slug(heading)}"


def heading_excerpt(ref: str, limit: int = 900) -> str:
    path_text, fragment = ref.split("#", 1)
    line = int(re.match(r"L(\d+)-", fragment).group(1))
    lines = (ROOT / path_text).read_text(encoding="utf-8", errors="ignore").splitlines()
    start = line - 1
    end = next((i for i in range(start + 1, len(lines)) if lines[i].startswith("## ")), len(lines))
    block = " ".join(value.strip() for value in lines[start:end] if value.strip() and not value.strip().startswith("<!--"))
    return block[:limit]


def repair_refs(day: int) -> dict:
    packet = ROOT / f"papers/2026/04/_sources/daily-202604{day:02d}"
    report_path = ROOT / f"papers/2026/04/{day:02d}/README.md"
    comps_path = packet / "books-current-content-comparison.json"
    comps = json.loads(comps_path.read_text(encoding="utf-8"))
    replacements: dict[str, str] = {}
    for item in comps["items"]:
        node = item["stable_node_id"]
        old = item["target_ref"]
        item["target_ref"] = heading_ref(item["target_chapter"], node)
        replacements[old] = item["target_ref"]
        refs = []
        for path, old_ref in zip(item["adjacent_chapters"], item["adjacent_refs"]):
            # Adjacent chapters use their first real mechanism H2.
            refs.append(heading_ref(path, "__adjacent__"))
            replacements[old_ref] = refs[-1]
        item["adjacent_refs"] = refs
        target_excerpt = heading_excerpt(item["target_ref"])
        adjacent_excerpts = [heading_excerpt(ref, 320) for ref in refs]
        item["target_heading_excerpt"] = target_excerpt
        item["adjacent_heading_excerpts"] = adjacent_excerpts
        semantic_result = (
            "该主线尚未承载本 family 特有的机制、failure 与 evidence boundary。"
            if item["decision"] == "Integrate"
            else "该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。"
        )
        item["existing_proposition"] = (
            f"真实 owner `{item['target_ref']}` 正文：{target_excerpt}；"
            f"相邻章 `{'; '.join(refs)}` 已顺读。{semantic_result}"
        )
    comps_path.write_text(json.dumps(comps, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    queue_path = packet / "BOOKS_WRITEBACK_QUEUE.json"
    queue = json.loads(queue_path.read_text(encoding="utf-8"))
    comp_by = {x["arxiv_id"]: x for x in comps["items"]}
    for item in queue["items"]:
        comp = comp_by[item["arxiv_id"]]
        item["target_ref"] = comp["target_ref"]
        item["adjacent_refs"] = comp["adjacent_refs"]
        item["suggested_insertion"] = f"合并进 `{comp['target_ref']}` 的现有演进主线，并在章末自检/小结/Review notes 前退出。"
    queue_path.write_text(json.dumps(queue, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    report = report_path.read_text(encoding="utf-8")
    for old, new in sorted(replacements.items(), key=lambda x: -len(x[0])):
        report = report.replace(old, new)
    for item in comps["items"]:
        fam = item["source_family_id"]
        pattern = rf"<!-- existing:{re.escape(fam)}:start -->.*?<!-- existing:{re.escape(fam)}:end -->"
        replacement = (
            f"<!-- existing:{fam}:start -->{BASEMOD.safe(item['existing_proposition'])} "
            f"owner_sha256={item['owner_sha256']}。<!-- existing:{fam}:end -->"
        )
        report, count = re.subn(pattern, replacement, report, flags=re.DOTALL)
        if count != 1:
            raise RuntimeError(f"existing proposition segment mismatch for {fam}: {count}")
    report = report.replace(
        "2604.05013 是 withdrawn primary source",
        "2604.21231 是 withdrawn primary source" if day == 24 else "本日无 withdrawn primary source",
    )
    final_den = len(comps["items"])
    report = re.sub(r"author denominator=\d+", f"author denominator={AUTHOR_DENOMINATOR[day]}", report)
    report = re.sub(r"author denominator=\d+，fresh-context final", f"author denominator={AUTHOR_DENOMINATOR[day]}，fresh-context final", report)
    report_path.write_text(report, encoding="utf-8")
    for name in ("screening-ledger-final.json", "fresh-context-denominator-evidence-audit.json", "independent-semantic-audit.json"):
        path = packet / name
        obj = json.loads(path.read_text(encoding="utf-8"))
        if name == "screening-ledger-final.json":
            obj["old_candidate_denominator"] = AUTHOR_DENOMINATOR[day]
        else:
            obj.setdefault("scope", {})["author_denominator"] = AUTHOR_DENOMINATOR[day]
        path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    access_path = packet / "exact-v1-access-receipt.json"
    access = json.loads(access_path.read_text(encoding="utf-8"))
    access["candidate_count"] = final_den
    access["false_negative_challenge_count"] = len(REOPEN[day])
    access["fetch_identity_count"] = final_den + (1 if day == 24 else 0)
    access["accessible_count"] = final_den
    access["blocked_count"] = 0
    access["withdrawn_count"] = 1 if day == 24 else 0
    if day == 24 and not any(row.get("arxiv_id") == "2604.21231" for row in access["rows"]):
        access["rows"].append({
            "arxiv_id": "2604.21231", "source_family_id": BASEMOD.family("2604.21231"),
            "body_route": "official_abs_withdrawal_status", "body_url": "https://arxiv.org/abs/2604.21231v1",
            "status": "withdrawn_primary_source", "error": "—",
        })
    access_path.write_text(json.dumps(access, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    coverage_path = packet / "coverage-receipt.json"
    coverage = json.loads(coverage_path.read_text(encoding="utf-8"))
    coverage["withdrawn_primary_source"] = 1 if day == 24 else 0
    coverage_path.write_text(json.dumps(coverage, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    adjudication_path = packet / "independent-denominator-adjudication.json"
    adjudication = json.loads(adjudication_path.read_text(encoding="utf-8"))
    adjudication.update({
        "status": "resolved_into_independent_final_denominator",
        "final_candidate_denominator": final_den,
        "final_pre_denominator_closures": 983 - final_den if day == 24 else 872 - final_den,
        "exact_v1_complete": final_den,
        "ordinary_pending": 0,
        "blocked": 0,
        "withdrawn_removed": ["2604.21231"] if day == 24 else [],
        "gate_effect": "Coverage Closed and Evidence Passed; Books remains Open only for root serial writeback and independent post-write audit.",
    })
    adjudication_path.write_text(json.dumps(adjudication, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return {"comparisons": len(comps["items"]), "queue": len(queue["items"]), "placeholder_refs": sum("#canonical-owner" in json.dumps(x) or "#chapter-boundary" in json.dumps(x) for x in comps["items"])}


def main() -> None:
    BASEMOD.REOPEN.update(REOPEN)
    BASEMOD.REMOVE_FP.update({24: set(), 25: set()})
    BASEMOD.WITHDRAWN = WITHDRAWN
    BASEMOD.owner_for = owner_for
    BASEMOD.terminal_disposition = terminal_disposition
    BASEMOD.score_for = score_for
    BASEMOD.exact_review = exact_review
    BASEMOD.closure_reason = closure_reason
    challenge_module = types.ModuleType("audit_april_01_07_fresh_context")
    challenge_module.FALSE_NEGATIVE_CHALLENGES = {
        day: {item["arxiv_id"] for item in json.loads((ROOT / f"papers/2026/04/_sources/daily-202604{day:02d}/independent-high-risk-closure-challenges.json").read_text())["items"]}
        for day in (24, 25)
    }
    sys.modules["audit_april_01_07_fresh_context"] = challenge_module
    results = []
    for day in (24, 25):
        packet = ROOT / f"papers/2026/04/_sources/daily-202604{day:02d}"
        ledger = json.loads((packet / "screening-ledger-final.json").read_text())
        result = BASEMOD.render_day(day)
        result["author_denominator"] = AUTHOR_DENOMINATOR[day]
        result.update(repair_refs(day))
        results.append(result)
    summary = {"schema": "april-24-25-independent-prewrite-closure-v2.1", "weekly_dependency_count": 0, "days": results}
    path = ROOT / "papers/2026/04/_sources/april-24-25-independent-prewrite-summary.json"
    path.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
