#!/usr/bin/env python3
"""Freeze February denominators and review every retained exact-v1 paper.

This is deliberately independent of Historical Weekly.  Every registered
identity receives either a candidate-denominator decision or a family-specific
pre-denominator closure.  Retention requires an explicit durable AI-System
mechanism or ownership/evaluation-contract delta; broad topical relevance is
not enough.
"""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor, as_completed
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import scripts.rebuild_march_lane_c_full_replay as reviewlib


MONTH = ROOT / "papers/2026/02"
WHOLE_PAPER_WITHDRAWAL_IDS = {"2602.00805", "2602.04816"}
FORCE_REVIEW_IDS = {
    "2602.00805",
    "2602.03295",
    "2602.10090",
    "2602.11686",
    "2602.15513",
    "2602.15763",
    "2602.16313",
    "2602.18914",
    "2602.23200",
}
ARTIFACT_OVERRIDES = {
    "2602.00397": "Not Disclosed — arXiv:2602.00397v1 does not disclose an author implementation repository or exact commit used by this review",
    "2602.00509": "Not Disclosed — arXiv:2602.00509v1 names runtime dependencies but does not disclose an author implementation repository or exact commit used by this review",
    "2602.02027": "Not Disclosed — arXiv:2602.02027v1 does not disclose an author implementation repository or exact commit used by this review",
    "2602.03295": "Not Disclosed — arXiv:2602.03295v1 does not disclose an author implementation repository or exact commit used by this review",
    "2602.10090": "Disclosed author artifact: https://github.com/Snowflake-Labs/agent-world-model; exact manuscript commit/tag Not Disclosed",
    "2602.11686": "Disclosed author artifact: https://github.com/Fizzmy/LAER-MoE-AE; exact manuscript commit/tag Not Disclosed",
    "2602.15763": "Disclosed author artifact: https://github.com/zai-org/GLM-5; exact manuscript commit/tag Not Disclosed",
}

# The generic section selector is deliberately conservative.  These exact-v1
# papers use descriptive headings, so bind each evidence facet to the section
# that actually carries the claim instead of accepting a bibliography,
# appendix expectation, or front-matter paragraph.
reviewlib.SECTION_OVERRIDES.update({
    "2602.03295": {
        "method": [r"3\.3 prefill-only pruning", r"3\.2 stage-aware importance"],
        "evaluation": [r"4\.3 inference speedup", r"4\.2 accuracy"],
        "limitations": [r"7 limitations", r"appendix c robustness"],
    },
    "2602.10090": {
        "method": [r"3\.3\.1 environment", r"a\.3 environment synthesis"],
        "evaluation": [r"6\.1 quality of synthesized environments", r"5\.2 main results"],
        "limitations": [r"^limitations$"],
    },
    "2602.11686": {
        "method": [r"3\.1.*fully sharded expert parallelism", r"3\.2 load balancing planner"],
        "evaluation": [r"5\.2\..*end-to-end performance", r"5\.5\..*ablation"],
        "limitations": [r"7\. discussion"],
    },
    "2602.15513": {
        "method": [r"iii-b human-inspired memory", r"iii-a semantic and physical"],
        "evaluation": [r"iv-a active embodied", r"iv-c ablation"],
        "limitations": [r"v conclusion"],
    },
    "2602.15763": {
        "method": [r"4\.1\.1 asynchronous rl design", r"4\.1\.2 optimizing asynchronous"],
        "evaluation": [r"6\.1\.3 evaluation of agentic", r"6\.2 evaluation of real-world"],
        "limitations": [r"7 conclusion"],
    },
    "2602.16313": {
        "method": [r"3\.1 task composition", r"3\.2 evaluation.*memory-agent"],
        "evaluation": [r"4\.3 main results", r"4\.4 results on interdependent"],
        "limitations": [r"5 conclusions"],
    },
    "2602.18914": {
        "method": [r"3\. constructing the taxonomy", r"3\.4 deriving description standards"],
        "evaluation": [r"5\.2.*real-world validation", r"5\.1.*component contribution"],
        "limitations": [r"7\.2 limitations", r"7\.3 threats to validity"],
    },
    "2602.23200": {
        "method": [r"4\.4 innerq", r"4\.1 quantization scheme"],
        "evaluation": [r"5\.3 latency", r"5\.2 evaluation performance"],
        "limitations": [r"7 conclusion and future work"],
    },
})

# Fresh-context semantic audit: the generic heading scorer is intentionally a
# fallback, not evidence that the selected section carries the requested
# facet.  These exact-v1 papers use descriptive headings (and several PDF
# conversions lose their section numbers), so bind method/evaluation/boundary
# evidence to the section that actually carries the claim.
FRESH_SECTION_OVERRIDES = {
    "2602.00277": {"method": [r"^4 design of ft-hsdp$", r"^4\.1 overview$"]},
    "2602.00328": {
        "method": [r"^3\.2 harvest api and runtime workflow$", r"^3\.1 general harvesting model$"],
        "evaluation": [r"^4\.5 expert offloading results$", r"^5\.4 kv offloader results$"],
    },
    "2602.00612": {
        "evaluation": [r"^5\.1.*syntactic correctness", r"^5\.3.*runtime overhead"],
        "limitations": [r"^6\.2\. threats to validity$"],
    },
    "2602.00748": {"method": [r"^4\.1 framework overview$", r"^4\.2 operatorized remote cache"]},
    "2602.00933": {"evaluation": [r"^5 results and analysis$", r"^5\.1 overall performance$"]},
    "2602.01053": {"limitations": [r"^compute overhead\.$", r"^d\.5 accuracy score deviation$"]},
    "2602.01202": {"limitations": [r"^5 ablation study$"]},
    "2602.01640": {"limitations": [r"^4\.4 benchmark validity and rationality$"]},
    "2602.01665": {
        "method": [r"^4 totally accelerated battle simulator in jax$", r"^4\.1 environmental parameters$"],
        "limitations": [r"^future work$"],
    },
    "2602.01795": {"limitations": [r"^7\.8 ablation study"]},
    "2602.01797": {
        "method": [r"^3 methodology$"],
        "evaluation": [r"^4 experiment result and analysis$"],
        "limitations": [r"^5\.2 limitations$"],
    },
    "2602.02027": {
        "method": [r"^4\.1 overview$", r"^4\.2 neuron-guided decoding$"],
        "evaluation": [r"^5\.2\.1 safety robustness and generalization$", r"^5\.2\.4 efficiency$"],
        "limitations": [r"^limitations and future work$"],
    },
    "2602.02108": {
        "method": [r"^4 the oomb training system$", r"^4\.1 paged memory management"],
        "evaluation": [r"^5\.2 memory, time, and scalability analysis$"],
    },
    "2602.02110": {
        "method": [r"^3\.1 experiment settings$"],
        "evaluation": [r"^3\.2 post-training quantization experiments$"],
    },
    "2602.02499": {"limitations": [r"^d\.2 ablation on rosa symbol width$", r"^6 related work and future plans$"]},
    "2602.02515": {"evaluation": [r"^5\.2 average performance", r"^5\.5 measured perturbation"]},
    "2602.02585": {
        "method": [r"^system design$"],
        "evaluation": [r"^evaluation$"],
        "limitations": [r"^discussion and future work$"],
    },
    "2602.02599": {"method": [r"^4 rap: rope-aligned pruning$", r"^4\.1 step 1"]},
    "2602.02690": {"evaluation": [r"^5\.2 rq1: performance difference", r"^5 experiments$"]},
    "2602.02958": {"limitations": [r"^5\.4 sensitivity test$"]},
    "2602.02987": {
        "method": [r"^5\.1 sli-aware gate-and-route control policy$", r"^4 stochastic control policy$"],
        "evaluation": [r"^6\.3 policy performance", r"^14 additional experiments"],
        "limitations": [r"^6\.3 policy performance", r"^6\.4 the cost of service quality"],
    },
    "2602.03128": {"method": [r"^3\. mafbench: a unified benchmark$", r"^3\.1 memory benchmarks$"]},
    "2602.03580": {
        "method": [r"^design of mcpdiff$"],
        "limitations": [r"^open questions and future directions$"],
    },
    "2602.03632": {
        "method": [r"^3\. the calm approach$", r"^3\.2 self-adaptive query routing$"],
        "evaluation": [r"^5\. results$"],
        "limitations": [r"^7\. threats to validity$"],
    },
    "2602.03782": {"method": [r"^3\.3 the proposed qvla$"], "evaluation": [r"^4\.2 comparison with state-of-the-arts$"]},
    "2602.03974": {"method": [r"^3\.6 uncertainty-guided epistemic control$"], "evaluation": [r"^5\.1 main results"]},
    "2602.04399": {"method": [r"^3\.3 swordsman$"], "evaluation": [r"^overall performance$"]},
    "2602.04448": {"method": [r"^3 rasa$"], "evaluation": [r"^4\.2 main results"]},
    "2602.04870": {"limitations": [r"^4\.3 ablation: head configuration$", r"^4\.4 ablation: separate routing tokens$"]},
    "2602.05523": {
        "method": [r"^3 transformations supported by evolve-ctf$"],
        "evaluation": [r"^5\.1 difficulty of ctf families", r"^5\.4 token usage and reasons for failure$"],
    },
    "2602.05842": {"method": [r"^2\.2 reinforcement world model learning$"], "evaluation": [r"^3\.2 main results$"]},
    "2602.05929": {"evaluation": [r"^4\.3 performance impact of kv-cache compression$", r"^4\.2\.1 average ner"]},
    "2602.06072": {"limitations": [r"^appendix c solver overhead$", r"^4\.3 ablation studies$"]},
    "2602.06454": {"method": [r"^4\.1 overview of relaygen$", r"^4\.3 runtime switching procedure$"]},
    "2602.06499": {"method": [r"^iv-b design overview$", r"^iv-c fcdp-sched"]},
    "2602.06822": {"limitations": [r"^accuracy.efficiency trade-off under different pruning strategies\.$"]},
    "2602.06932": {
        "evaluation": [r"^6 scalability on frontier", r"^5 speculative algorithm exploration$"],
        "limitations": [r"^a\.2 inference-side memory overhead$", r"^4\.2 a trade-off study"],
    },
    "2602.06949": {"limitations": [r"^4\.5 ablations of our design choices$"]},
    "2602.07223": {"evaluation": [r"^5\.2 reasoning workloads with short input", r"^5\.3 reasoning workloads with long input"]},
    "2602.07263": {"limitations": [r"^a\.2 job completion time ablation studies$"]},
    "2602.07397": {"method": [r"^2 sketch and walk$"], "evaluation": [r"^4\.3 efficiency evaluation$", r"^4\.2 accuracy evaluation$"]},
    "2602.07721": {"limitations": [r"^5\.3 ablation studies$"]},
    "2602.08007": {"method": [r"^3\.3 tsr-adam"], "evaluation": [r"^4\.2 main results"]},
    "2602.08005": {"limitations": [r"^b\.5 detailed latency profiling and future optimization$", r"^hyperparameter sensitivity$"]},
    "2602.08404": {"method": [r"^3\.2 delayed caching", r"^3\.3 speculative exploration"], "evaluation": [r"^4\.2 main results$"]},
    "2602.08722": {"limitations": [r"^4\.5 ablation study$", r"^appendix i ablations$"]},
    "2602.08747": {
        "method": [r"^4\. system design$", r"^4\.1 system overview$"],
        "limitations": [r"^7\. applicable to other workload$", r"^5\.4 sensitivity and overhead analysis$"],
    },
    "2602.09316": {"limitations": [r"^4\.2 ablation study$"]},
    "2602.09430": {"method": [r"^3\. sci-vla", r"^3\.2 inference atomic tasks sequence$"], "evaluation": [r"^4\.2\.3 long experimental", r"^4\.2\.4 real environment"]},
    "2602.09578": {"limitations": [r"^9\. discussion$"]},
    "2602.09721": {"method": [r"^2\.2 afd and budget", r"^3\.2 afd dead zone"]},
    "2602.09725": {"limitations": [r"^6\. limitation and discussion$"]},
    "2602.10377": {"method": [r"^3 formulating hardware co-design law", r"^3\.3 performance modeling"]},
    "2602.10615": {"limitations": [r"^5\.2 error analysis and threshold guidance$", r"^7\.3 sensitivity analysis$"]},
    "2602.10718": {"limitations": [r"^4\.3 numerical accuracy$"]},
    "2602.10729": {"limitations": [r"^appendix a simulator design and validation$"]},
    "2602.11224": {
        "method": [r"^3\. agent-diff$", r"^3\.1 agent-diff environments$"],
        "evaluation": [r"^6\.1 model-to-model comparison$", r"^5\.1 experiment setup$"],
    },
    "2602.11291": {"method": [r"^4\.3 pipeline for vla", r"^4\.1 logic world model$"]},
    "2602.11301": {
        "method": [r"^3 architecture overview"],
        "limitations": [r"^7 discussion and conclusion$"],
    },
    "2602.11521": {"method": [r"^4\. pam: system overview$", r"^4\.1 system architecture$"], "evaluation": [r"^7\.2 pam performance$"]},
    "2602.11530": {"evaluation": [r"^v-b user experience", r"^v-c kv cache transfer overhead$"]},
    "2602.11790": {"limitations": [r"^5\.4\. error analysis$", r"^5\.3\. ablation studies$"]},
    "2602.11882": {"method": [r"^quantization implementation details\.$", r"^task and metric\.$"]},
    "2602.11937": {"method": [r"^2 puzzle optimization$"], "evaluation": [r"^4\.1 inference efficiency$", r"^4\.2 accuracy benchmarks$"]},
    "2602.11964": {"evaluation": [r"^5\.1 core results$", r"^5 experiments$"]},
    "2602.12244": {"limitations": [r"^vii conclusion & limitations$"]},
    "2602.12271": {"limitations": [r"^3\.1 approximation error analysis$", r"^3\.4 practical challenges"]},
    "2602.13594": {"limitations": [r"^appendix g accuracy gap$", r"^appendix d ablation"]},
    "2602.13692": {
        "method": [r"^4\.1 program abstraction$", r"^4\.3 scheduling policy$"],
        "evaluation": [r"^5\.2 serving evaluation results$", r"^5\.3 rollout evaluation results$"],
        "limitations": [r"^5\.4 ablation study$"],
    },
    "2602.13933": {"limitations": [r"^4\.4 compression loss analysis$", r"^4\.3 ablation studies$"]},
    "2602.13967": {"evaluation": [r"^5\.1 findings$", r"^5 experimental analysis$"]},
    "2602.13977": {"limitations": [r"^6\.1 ablation on world model", r"^6\.2 ablation on policy"]},
    "2602.14849": {"limitations": [r"^6\.5 robustness and overhead$"]},
    "2602.14516": {"evaluation": [r"^7\.2 experiment results$"]},
    "2602.15112": {"method": [r"^2 researchgym$", r"^2\.2 benchmark construction$"], "evaluation": [r"^4 results$", r"^4\.2 reliability$"]},
    "2602.15654": {"limitations": [r"^inefficacy of instruction defenses\.$", r"^impact of memory evolution mechanisms\.$"]},
    "2602.16246": {"limitations": [r"^system-fact and user-fact ablations\.$"]},
    "2602.16603": {
        "method": [r"^5\.1\. operator-level preemption$", r"^5\.2\. event-driven scheduling$"],
        "evaluation": [r"^6\.2\. end-to-end speedup$", r"^6\.4\. runtime analysis$"],
        "limitations": [r"^6\.4\. runtime analysis$", r"^6\.3\. ablation studies$"],
    },
    "2602.16873": {"method": [r"^4 the adaptorch framework$", r"^4\.3 phase 3: topology routing$"]},
    "2602.16943": {"method": [r"^3\.1 benchmark design$"], "limitations": [r"^6 threats to validity$"]},
    "2602.18007": {
        "method": [r"^2\.2 device-direct communication$", r"^2\.1 cpu-forwarding communication$"],
        "evaluation": [r"^3\.2 performance$", r"^3\.4 correctness$"],
        "limitations": [r"^4\.1 heterogeneity limited to pipeline parallelism$", r"^4\.3 engineering challenges$"],
    },
    "2602.18397": {"method": [r"^3 analyzing vla inference performance with vla-perf$"], "evaluation": [r"^4\.2 baseline", r"^4 evaluation and takeaways$"]},
    "2602.18434": {"limitations": [r"^5\.4 ablation study$"]},
    "2602.18583": {"evaluation": [r"^4\.1 accuracy$", r"^4\.2 latency and cost$"]},
    "2602.18755": {
        "method": [r"^4\.2\. system architecture$", r"^4\.3 tier 1"],
        "evaluation": [r"^6\.2\. end-to-end results$", r"^6\.5\. latency/power model accuracy$"],
        "limitations": [r"^6\.6\. simulation accuracy$", r"^6\.5\. latency/power model accuracy$"],
    },
    "2602.19161": {"limitations": [r"^4\.3 ablation study$"]},
    "2602.19843": {"method": [r"^3\. an mas fault injection", r"^3\.2\. fault injection mechanism$"]},
    "2602.19938": {"limitations": [r"^3\.3 ablation study$"]},
    "2602.20379": {"method": [r"^4 framework overview$", r"^4\.2 metric definitions$"], "evaluation": [r"^8 results and analysis$", r"^8\.7 human alignment"]},
    "2602.20478": {
        "method": [r"^3\. architecture$", r"^3\.1\. tier 1"],
        "evaluation": [r"^4\.2\. scale and growth$", r"^4\.4\. case studies$"],
        "limitations": [r"^5\.3\. threats to validity and future work$"],
    },
    "2602.20656": {"evaluation": [r"^4\.2\. end-to-end performance$", r"^4\.4\. efficiency of tuning$"]},
    "2602.21144": {"method": [r"^iv design$", r"^iv-b intelligent channel-wise"], "limitations": [r"^v-e ablation study"]},
    "2602.21257": {"method": [r"^architecture$"], "evaluation": [r"^evaluation$"], "limitations": [r"^10 limitations and future work$"]},
    "2602.21736": {"limitations": [r"^6\.3\.4 ablation studies$"]},
    "2602.22302": {
        "method": [r"^5\.3 per-turn enforcement$", r"^3\.1 contract structure$"],
        "evaluation": [r"^7\.3 e1: contracted vs\. uncontracted$", r"^6\.5 validation results$"],
        "limitations": [r"^8\.2 limitations$", r"^8\.3 threats to validity$"],
    },
    "2602.22593": {
        "method": [r"^3\. an overview of flying serving$", r"^5\. dynamic scheduler$"],
        "evaluation": [r"^6\.2\. overall performance$", r"^6\.4\. max context"],
        "limitations": [r"^5\.3\.2\. limitations\.$"],
    },
    "2602.22647": {"limitations": [r"^appendix d hardware scaling with high branching factor$"]},
    "2602.22769": {"method": [r"^3 ama-bench$", r"^3\.3 benchmark construction$"], "evaluation": [r"^6\.2 key results$", r"^6\.3 ablation study$"]},
    "2602.22942": {"limitations": [r"^5\. challenges and research questions$", r"^5\.3\. stability"]},
}
reviewlib.SECTION_OVERRIDES.update(FRESH_SECTION_OVERRIDES)

# A positive summary is not counterevidence.  These exact-v1 bodies have no
# independent limitations/boundary section; keep the facet explicitly missing
# so downstream claim text narrows instead of treating the conclusion as proof.
LIMITATIONS_NOT_DISCLOSED_IDS = {
    "2602.00269", "2602.00509", "2602.00777", "2602.00879",
    "2602.01237", "2602.01842", "2602.02204", "2602.03203",
    "2602.04448", "2602.04711",
    "2602.03025", "2602.05145", "2602.05929", "2602.07265",
    "2602.07223", "2602.07306", "2602.08798", "2602.09222", "2602.09323",
    "2602.10133", "2602.11513", "2602.12029",
    "2602.12322", "2602.13052", "2602.13653", "2602.13710",
    "2602.14516", "2602.15763", "2602.15809", "2602.15831",
    "2602.19128", "2602.20515", "2602.20656", "2602.21788",
    "2602.22217", "2602.22437", "2602.22663",
}

# The final owner audit routes Parallel Track Transformer to the canonical
# transformer-layer node.  Keep that route and give the evidence renderer the
# same problem/ownership/coexistence lens instead of falling back to another
# chapter.
reviewlib.NARRATIVE_LENS.setdefault(
    "MODEL-TRANSFORMER-LAYER",
    (
        "串行 attention 与 FFN block 的依赖和残差路径最直接，也最容易验证。",
        "跨设备执行把 block 内同步次数、分支合并和 collective placement 变成一等约束。",
        "layer topology、residual merge、activation flow 与 synchronization boundary",
        "单设备或通信不占主导时，标准串行 Transformer layer 仍更简单可靠。",
    ),
)


def frozen_full_text(packet: Path, aid: str):
    """Return the already-frozen exact-v1 full text without using the network."""

    body_dir = packet / "exact-v1-bodies"
    html_path = body_dir / f"{aid}v1.html"
    if html_path.is_file() and html_path.stat().st_size > 1000:
        parser = reviewlib.SectionParser()
        parser.feed(html_path.read_text(errors="ignore"))
        return "HTML", html_path, parser.sections
    pdf_text_path = body_dir / f"{aid}v1.pdf.txt"
    if pdf_text_path.is_file() and pdf_text_path.stat().st_size > 1000:
        return (
            "PDF",
            pdf_text_path,
            reviewlib.pdf_sections(pdf_text_path.read_text(errors="ignore")),
        )
    return None


def review_from_frozen_full_text(row: dict, packet: Path, failed_review: dict) -> dict:
    """Recover a network-blocked review from its previously frozen exact-v1 body."""

    aid = row["arxiv_id"]
    frozen = frozen_full_text(packet, aid)
    if frozen is None:
        return failed_review
    source_kind, body_path, sections = frozen
    overrides = reviewlib.SECTION_OVERRIDES.get(aid, {})
    facets = {}
    for facet in ("method", "evaluation", "limitations"):
        facets[facet] = reviewlib.choose_section(
            sections,
            facet,
            row["title"],
            facet.title(),
            overrides.get(facet),
        )
    digest = hashlib.sha256(body_path.read_bytes()).hexdigest()
    body_rel = str(body_path.relative_to(ROOT))
    source_url = (
        f"https://arxiv.org/html/{aid}v1"
        if source_kind == "HTML"
        else f"https://arxiv.org/pdf/{aid}v1"
    )

    def locator(facet: str) -> str:
        heading, excerpt = facets[facet]
        if excerpt.startswith("Not Disclosed"):
            return (
                f"Not Disclosed — exact-v1 {source_kind} 全文已审计但未提供独立 "
                f"{facet.title()} 章节 [facet={facet}]; {source_url}; {body_rel}; "
                f"sha256:{digest}"
            )
        return (
            f"arXiv:{aid}v1 {source_kind} — §{heading} [facet={facet}]; "
            f"{source_url}; {body_rel}; sha256:{digest}"
        )

    family = f"SF-2026-ARXIV-{aid.replace('.', '-')}"
    disposition = failed_review.get(
        "books_disposition",
        reviewlib.DISPOSITION_OVERRIDES.get(
            aid,
            "Integrate" if aid in reviewlib.INTEGRATE_SUGGESTIONS else "No Change — Existing Coverage",
        ),
    )
    return {
        "source_family_id": family,
        "event_identity": f"paper-v1:{aid}",
        "primary_identifier": f"arXiv:{aid}v1",
        "primary_version": f"arXiv:{aid}v1",
        "title": row["title"],
        "method_evidence_excerpt": facets["method"][1],
        "evaluation_evidence_excerpt": facets["evaluation"][1],
        "limitations_evidence_excerpt": facets["limitations"][1],
        "method_locator": locator("method"),
        "evaluation_locator": locator("evaluation"),
        "limitations_locator": locator("limitations"),
        "artifact_locator": failed_review.get("artifact_locator", "Not Disclosed"),
        "claim_ref": f"claim:{family}",
        "review_ref": f"review:{family}",
        "stable_node_id": row["stable_node_id"],
        "books_disposition": disposition,
        "review_route": failed_review.get("review_route", "standard"),
        "access_status": "accessible",
        "result": "complete",
        "withdrawn": failed_review.get("withdrawn", False),
        "abs_status": failed_review.get("abs_status", 0),
        "current_abs_status": failed_review.get("current_abs_status", 0),
        "current_abs_url": failed_review.get(
            "current_abs_url", f"https://export.arxiv.org/api/query?id_list={aid}"
        ),
        "html_status": 200 if source_kind == "HTML" else failed_review.get("html_status", 404),
        "pdf_status": 200 if source_kind == "PDF" else failed_review.get("pdf_status", 0),
        "source_kind": source_kind,
        "body_path": body_rel,
    }


def apply_frozen_section_overrides(review: dict, aid: str, packet: Path) -> None:
    """Bind audited exact-v1 facets to frozen HTML/PDF sections.

    The shared reviewer correctly downloads and extracts the PDF, but its
    parser currently prefers any non-empty ``html_body`` even when
    ``html_status`` is 404.  Applying every February override from the frozen
    body also makes retries independent of current arXiv throttling.  A
    configured heading that cannot be recovered is an audit failure, not
    permission to synthesize evidence.
    """

    overrides = FRESH_SECTION_OVERRIDES.get(aid, {})
    if not overrides:
        return
    frozen = frozen_full_text(packet, aid)
    if frozen is None:
        raise RuntimeError(f"{aid}: configured section override has no frozen full-text body")
    source_kind, body_file, sections = frozen
    body_rel = str(body_file.relative_to(ROOT))
    digest = hashlib.sha256(body_file.read_bytes()).hexdigest()
    source_url = (
        f"https://arxiv.org/html/{aid}v1"
        if source_kind == "HTML"
        else f"https://arxiv.org/pdf/{aid}v1"
    )
    field_prefix = {
        "method": "method",
        "evaluation": "evaluation",
        "limitations": "limitations",
    }
    for facet, patterns in overrides.items():
        heading, excerpt = reviewlib.choose_section(
            sections,
            facet,
            review["title"],
            facet.title(),
            patterns,
        )
        if excerpt.startswith("Not Disclosed"):
            raise RuntimeError(
                f"{aid}: audited {source_kind} {facet} override did not match any evidence-bearing section"
            )
        prefix = field_prefix[facet]
        review[f"{prefix}_evidence_excerpt"] = excerpt
        review[f"{prefix}_locator"] = (
            f"arXiv:{aid}v1 {source_kind} — §{heading} [facet={facet}]; {source_url}; "
            f"{body_rel}; sha256:{digest}"
        )
    review["source_kind"] = source_kind
    review["body_path"] = body_rel


SIGNALS = [
    re.compile(r"\b(?:kv[- ]?cache|speculative decoding|continuous batching|paged attention|llm serving|inference serving|inference engine|prefill|disaggregated inference|distributed inference|tensor parallel|pipeline parallel|expert parallel|distributed training|checkpointing|gpu memory|memory management|model parallel|gpu kernel|kernel compiler|all[- ]reduce|collective communication|interconnect)\b", re.I),
    re.compile(r"\b(?:mixture[- ]of[- ]experts|moe|linear attention|sparse attention|state space model|long[- ]context|tokenizer|positional encoding|attention sink|ffn sparsity)\b", re.I),
    re.compile(r"\b(?:rlhf|dpo|grpo|pre[- ]?training|post[- ]?training|reward model|reward hacking|policy optimization|preference optimization|data mixing|data curation|data contamination|training stability|quantization|pruning)\b", re.I),
    re.compile(r"\b(?:llm agent|ai agent|agentic|multi[- ]agent|tool[- ]use|tool calling|retrieval[- ]augmented|rag|agent memory|long[- ]term memory|workflow|model context protocol|mcp|planning|reflection)\b", re.I),
    re.compile(r"\b(?:world model|vision[- ]language[- ]action|vla|embodied|multimodal generation|diffusion language|masked diffusion|video generation|native multimodal|multimodal representation)\b", re.I),
    re.compile(r"\b(?:evaluation framework|evaluation protocol|benchmarking agents|llm benchmark|safety benchmark|model provenance|observability|release gate|prompt injection|jailbreak|data poisoning|backdoor|membership inference|unlearning|privacy[- ]preserving.*(?:llm|model)|security.*(?:llm|agent))\b", re.I),
]
WEAK = re.compile(r"\b(?:throughput|latency|efficient|scalable|memory|scheduling|routing|serving|cache|compression|low[- ]rank|lora|alignment|factuality|hallucination|uncertainty|evaluation|benchmark|safety|privacy|governance|provenance)\b", re.I)
DOMAIN = re.compile(r"\b(?:medical|clinical|patient|protein|molecular|materials|wireless|traffic|finance|financial|agriculture|remote sensing|satellite|health|disease|drug|chemistry|power grid|robotic surgery)\b", re.I)
SURVEY = re.compile(r"\b(?:survey|review|position|perspective|dataset)\b", re.I)


AUTHOR_DEMOTIONS = {
    "2602.00003": "single_domain_method_without_transferable_system_contract",
    "2602.00757": "single_domain_benchmark_without_transferable_contract",
    "2602.01023": "domain_application_without_system_delta",
    "2602.02338": "domain_application_without_system_delta",
    "2602.02494": "domain_application_without_system_delta",
    "2602.02585": "domain_application_without_system_delta",
    "2602.02970": "localized_method_without_ai_system_contract",
    "2602.03028": "domain_application_without_system_delta",
    "2602.04184": "domain_application_without_system_delta",
    "2602.00558": "domain_application_without_system_delta",
    "2602.04566": "domain_application_without_system_delta",
    "2602.10869": "domain_application_without_system_delta",
    "2602.11076": "domain_application_without_system_delta",
    "2602.11790": "domain_application_without_system_delta",
    "2602.13301": "domain_application_without_system_delta",
    "2602.13808": "domain_application_without_system_delta",
    "2602.14033": "domain_application_without_system_delta",
    "2602.14577": "domain_application_without_system_delta",
    "2602.14200": "single_domain_benchmark_without_transferable_contract",
    "2602.14955": "domain_application_without_system_delta",
    "2602.15813": "domain_application_without_system_delta",
    "2602.15859": "domain_application_without_system_delta",
    "2602.15776": "localized_method_without_ai_system_contract",
    "2602.16953": "domain_application_without_system_delta",
    "2602.17739": "domain_application_without_system_delta",
    "2602.17954": "domain_application_without_system_delta",
    "2602.19021": "framework_claim_without_executable_system_contract",
    "2602.20577": "domain_application_without_system_delta",
    "2602.22059": "domain_application_without_system_delta",
    "2602.02035": "non_llm_domain_method_without_ai_system_contract",
    "2602.18291": "non_llm_domain_method_without_ai_system_contract",
    "2602.18415": "hci_measurement_without_ai_system_design_delta",
    # The exact-v1 paper is a localized noisy-PINN pruning method.  A later
    # v2 withdrawal and v3 restoration are revision facts, but neither turns
    # the February v1 into a transferable AI-System execution contract.
    "2602.19967": "localized_quality_or_method_delta",
    "2602.13691": "localized_quality_or_method_delta",
    "2602.14979": "model_release_without_distinct_system_contract",
    "2602.17664": "localized_quality_or_method_delta",
    "2602.21172": "model_recipe_without_distinct_system_contract",
    "2602.21346": "localized_quality_or_method_delta",
    "2602.22638": "single_domain_benchmark_without_transferable_contract",
}


# Fresh-context denominator audit recovered these false negatives.  Explicit
# retention is necessary because several titles use domain-specific language
# even though the exact mechanism changes a durable AI-System contract.
AUTHOR_RETENTIONS = {
    "2602.00286": "MULTIMODAL-GENERATIVE-PARADIGMS",
    "2602.00364": "PLATFORM-SECURITY",
    "2602.00805": "AGENT-RAG",
    "2602.00966": "AGENT-MULTI-AGENT",
    "2602.02499": "MODEL-LONG-CONTEXT",
    "2602.02574": "AGENT-MEMORY",
    "2602.02585": "PLATFORM-MONITORING",
    "2602.04431": "PLATFORM-SECURITY",
    "2602.05780": "TRAIN-DATA",
    "2602.11790": "AGENT-WORKFLOW",
    "2602.14955": "PLATFORM-EVALUATION-SYSTEM",
    "2602.15831": "AGENT-PLATFORM",
    "2602.19762": "INFER-TENSORRT-LLM",
    "2602.21140": "INFER-SCHEDULING",
    # Recovered by the independent full-ledger false-negative audit.  Each
    # abstract names a concrete runtime, control-plane, security, or evidence
    # contract; these are not retained merely for broad AI topical relevance.
    "2602.00269": "INFER-REQUEST-LIFECYCLE",
    "2602.01237": "INFER-SCHEDULING",
    "2602.02589": "PLATFORM-EVALUATION-SYSTEM",
    "2602.02987": "INFER-SCHEDULING",
    "2602.04653": "PLATFORM-SECURITY",
    "2602.04816": "TRAIN-DISTRIBUTED-TRAINING",
    "2602.06502": "INFER-SCHEDULING",
    "2602.07878": "PLATFORM-SECURITY",
    "2602.08060": "INFER-SPECULATIVE-DECODING",
    "2602.08296": "PLATFORM-GPU-SCHEDULER",
    "2602.08585": "INFER-KV-CACHE",
    "2602.08798": "PLATFORM-SECURITY",
    "2602.10133": "PLATFORM-TRACE",
    "2602.10729": "INFER-SCHEDULING",
    "2602.11470": "PLATFORM-SECURITY",
    "2602.11521": "INFER-GPU-MEMORY",
    "2602.11530": "INFER-SCHEDULING",
    "2602.12151": "INFER-SCHEDULING",
    "2602.13692": "INFER-SCHEDULING",
    "2602.16603": "INFER-SCHEDULING",
    "2602.16708": "PLATFORM-SECURITY",
    "2602.22593": "INFER-SCHEDULING",
    "2602.23036": "PLATFORM-EVALUATION-SYSTEM",
    "2602.02204": "INFER-PD-DISAGGREGATION",
    "2602.06547": "PLATFORM-SECURITY",
    "2602.08968": "PLATFORM-EVALUATION-SYSTEM",
    "2602.12544": "PLATFORM-EVALUATION-SYSTEM",
    "2602.14281": "PLATFORM-SECURITY",
    "2602.14849": "AGENT-WORKFLOW",
    "2602.22302": "PLATFORM-SECURITY",
    "2602.22437": "TRAIN-ZERO",
    # Second independent closure replay: every family below was recovered only
    # after a full high-signal scan plus fixed-seed, date/reason/category
    # sampling.  Each abstract exposes a concrete state, data, control,
    # security, or evaluation contract and therefore must reach the candidate
    # denominator before scoring and exact-v1 review.
    "2602.00277": "TRAIN-DISTRIBUTED-TRAINING",
    "2602.00328": "INFER-GPU-MEMORY",
    "2602.00612": "MULTIMODAL-GENERATIVE-PARADIGMS",
    "2602.00933": "PLATFORM-EVALUATION-SYSTEM",
    "2602.01665": "PLATFORM-EVALUATION-SYSTEM",
    "2602.02108": "TRAIN-DISTRIBUTED-TRAINING",
    "2602.02192": "TRAIN-DISTRIBUTED-TRAINING",
    "2602.02455": "PLATFORM-EVALUATION-SYSTEM",
    "2602.02515": "PLATFORM-EVALUATION-SYSTEM",
    "2602.02690": "PLATFORM-EVALUATION-SYSTEM",
    "2602.03128": "PLATFORM-EVALUATION-SYSTEM",
    "2602.03580": "AGENT-MCP",
    "2602.03632": "INFER-SCHEDULING",
    "2602.05145": "INFER-SPECULATIVE-DECODING",
    "2602.05523": "PLATFORM-EVALUATION-SYSTEM",
    "2602.05711": "MODEL-MOE",
    "2602.05765": "TRAIN-DISTRIBUTED-TRAINING",
    "2602.05929": "INFER-KV-CACHE",
    "2602.06072": "INFER-TENSORRT-LLM",
    "2602.06075": "PLATFORM-EVALUATION-SYSTEM",
    "2602.06079": "TRAIN-DISTRIBUTED-TRAINING",
    "2602.06345": "PLATFORM-SECURITY",
    "2602.06454": "INFER-SCHEDULING",
    "2602.06499": "TRAIN-ZERO",
    "2602.06932": "INFER-SPECULATIVE-DECODING",
    "2602.07263": "TRAIN-LORA",
    "2602.07265": "MODEL-MOE",
    "2602.07306": "MODEL-TRANSFORMER-LAYER",
    "2602.07962": "PLATFORM-EVALUATION-SYSTEM",
    "2602.08747": "INFER-SCHEDULING",
    "2602.09323": "INFER-TENSORRT-LLM",
    "2602.09345": "PLATFORM-MULTI-TENANT",
    "2602.09433": "PLATFORM-SECURITY",
    "2602.09578": "TRAIN-DISTRIBUTED-TRAINING",
    "2602.09721": "INFER-PD-DISAGGREGATION",
    "2602.09725": "INFER-KV-CACHE",
    "2602.10238": "INFER-KV-CACHE",
    "2602.10377": "INFER-SCHEDULING",
    "2602.10615": "PLATFORM-EVALUATION-SYSTEM",
    "2602.10915": "PLATFORM-SECURITY",
    "2602.10940": "INFER-TENSORRT-LLM",
    "2602.11224": "PLATFORM-EVALUATION-SYSTEM",
    "2602.11348": "PLATFORM-EVALUATION-SYSTEM",
    "2602.11456": "TRAIN-DISTRIBUTED-TRAINING",
    "2602.11749": "PLATFORM-SECURITY",
    "2602.11964": "PLATFORM-EVALUATION-SYSTEM",
    "2602.12876": "PLATFORM-EVALUATION-SYSTEM",
    "2602.13165": "INFER-SCHEDULING",
    "2602.13255": "AGENT-MULTI-AGENT",
    "2602.13320": "AGENT-MCP",
    "2602.13933": "AGENT-MEMORY",
    "2602.13967": "PLATFORM-EVALUATION-SYSTEM",
    "2602.14038": "AGENT-MEMORY",
    "2602.14516": "INFER-PD-DISAGGREGATION",
    "2602.15112": "PLATFORM-EVALUATION-SYSTEM",
    "2602.15654": "PLATFORM-SECURITY",
    "2602.15809": "PLATFORM-EVALUATION-SYSTEM",
    "2602.15945": "PLATFORM-SECURITY",
    "2602.16246": "PLATFORM-EVALUATION-SYSTEM",
    "2602.16760": "PLATFORM-SECURITY",
    "2602.16873": "AGENT-MULTI-AGENT",
    "2602.16943": "PLATFORM-SECURITY",
    "2602.18007": "TRAIN-DISTRIBUTED-TRAINING",
    "2602.18397": "PLATFORM-EVALUATION-SYSTEM",
    "2602.18583": "PLATFORM-EVALUATION-SYSTEM",
    "2602.18755": "INFER-PD-DISAGGREGATION",
    "2602.18922": "AGENT-CONTEXT",
    "2602.18931": "INFER-SPECULATIVE-DECODING",
    "2602.19938": "MODEL-MOE",
    "2602.20214": "PLATFORM-SECURITY",
    "2602.20478": "AGENT-CONTEXT",
    "2602.20656": "TRAIN-DISTRIBUTED-TRAINING",
    "2602.21144": "TRAIN-TENSOR-PARALLEL",
    "2602.21257": "AGENT-CONTEXT",
    "2602.21447": "PLATFORM-SECURITY",
    "2602.21548": "INFER-PD-DISAGGREGATION",
    "2602.21760": "MULTIMODAL-GENERATIVE-PARADIGMS",
    "2602.21788": "TRAIN-DISTRIBUTED-TRAINING",
    "2602.22158": "TRAIN-CHECKPOINT",
    "2602.22217": "AGENT-RAG",
    "2602.22525": "PLATFORM-SECURITY",
    "2602.22647": "INFER-TENSORRT-LLM",
    "2602.22769": "AGENT-MEMORY",
    "2602.22942": "AGENT-PLATFORM",
    "2602.23005": "AGENT-PLATFORM",
}


AUTHOR_NODE_OVERRIDES: dict[str, str] = {}
for _node, _ids in {
    "AGENT-MCP": "20196",
    "AGENT-MEMORY": "03036 07398 13594 15513 16313 18493",
    "AGENT-MULTI-AGENT": "01797 02035 06038 08847 18291 19843 23258",
    "AGENT-PLANNING": "03255 03974 05279 12244 18694",
    "AGENT-RAG": "04926 10271 12735",
    "AGENT-REFLECTION": "21198",
    "AGENT-TOOL-CALLING": "10986 17046",
    "AGENT-PLATFORM": "21227",
    "INFER-GPU-MEMORY": "00748 03495 11192 21477",
    "INFER-KV-CACHE": "01053 01795 02197 02199 02579 02599 02958 03184 03203 07721 08005 08343 08722 18434 18750 21780 22603 23200",
    "INFER-PD-DISAGGREGATION": "12029",
    "INFER-PREFILL": "20515",
    "INFER-SCHEDULING": "07616 11688 21626",
    "INFER-SPECULATIVE-DECODING": "07223 16052",
    "INFER-TENSORRT-LLM": "01037 03295 06822 10718 11184 19128",
    "MODEL-LONG-CONTEXT": "00397 00777 02195 07397 08382 10021 12675 20732",
    "MODEL-MOE": "00003 00509 00879 04870 07616 08404 09316 11686 11937 17038",
    "MULTIMODAL-EMBODIED-VLA": "00780 03782 04315 04326 05049 09430 10556 12322 13052 13710 14979 18291 18813 19710 20309 21172 21595 21736",
    "MULTIMODAL-GENERATIVE-PARADIGMS": "00268 00508 01842 04399 05305 06028 08404 10116 12271 17664 19161 19163",
    "MULTIMODAL-WORLD-MODELS": "01801 02110 05842 06949 10090 11291 11882 13977 15549 22208 22960 23148",
    "PLATFORM-EVALUATION-SYSTEM": "01640 05249 09130 12691 14337 16313 18415 18940 19843 20379 22663",
    "PLATFORM-SECURITY": "00500 01795 02027 04448 04711 05279 09222 11327 11513 13151 16520 17345 17692 20196 20720",
    "TRAIN-DATA": "14093 16444",
    "TRAIN-DISTRIBUTED-TRAINING": "08007 11543",
    "TRAIN-DPO": "21346",
    "TRAIN-GRPO": "01202 03025 13691 22817",
    "TRAIN-LORA": "22268",
    "TRAIN-PRETRAINING": "16444",
    "TRAIN-RLHF": "01202 02027 03719 04448 05000 05049 06462 07186 07595 08237 08905 12281 13653 13691 13977 15763 19372 21346 22718 23008",
}.items():
    for _suffix in _ids.split():
        AUTHOR_NODE_OVERRIDES[f"2602.{_suffix}"] = _node

# Independent owner audit corrections.  The earlier title-first rules still
# confused the subject of a paper with the subsystem that owns its mechanism.
AUTHOR_NODE_OVERRIDES.update({
    "2602.00397": "INFER-PREFILL",
    "2602.00509": "INFER-SCHEDULING",
    "2602.02027": "MODEL-SAMPLING",
    "2602.03295": "INFER-PREFILL",
    "2602.03560": "MODEL-LONG-CONTEXT",
    "2602.10090": "TRAIN-DATA",
    "2602.11301": "PLATFORM-SECURITY",
    "2602.11686": "TRAIN-DISTRIBUTED-TRAINING",
    "2602.15763": "TRAIN-DISTRIBUTED-TRAINING",
    "2602.08722": "INFER-PREFILL",
    "2602.10986": "AGENT-TOOL-CALLING",
    "2602.12271": "INFER-TENSORRT-LLM",
    "2602.12691": "TRAIN-RLHF",
    "2602.13710": "INFER-TENSORRT-LLM",
    "2602.13977": "MULTIMODAL-WORLD-MODELS",
    "2602.16444": "TRAIN-DATA",
    "2602.19372": "MULTIMODAL-EMBODIED-VLA",
    "2602.20309": "INFER-TENSORRT-LLM",
    "2602.20732": "INFER-KV-CACHE",
    "2602.21227": "INFER-SCHEDULING",
    "2602.22718": "TRAIN-DISTRIBUTED-TRAINING",
    "2602.00269": "INFER-REQUEST-LIFECYCLE",
    "2602.01202": "TRAIN-GRPO",
    "2602.02110": "INFER-TENSORRT-LLM",
    "2602.03255": "PLATFORM-EVALUATION-SYSTEM",
    "2602.03782": "INFER-TENSORRT-LLM",
    "2602.08404": "INFER-TENSORRT-LLM",
    "2602.11882": "INFER-TENSORRT-LLM",
    "2602.12544": "PLATFORM-EVALUATION-SYSTEM",
    "2602.13692": "INFER-SCHEDULING",
    "2602.16603": "INFER-SCHEDULING",
    "2602.22302": "PLATFORM-SECURITY",
})


# Canonical-owner routing is title-first and mechanism-first.  Generic words
# such as "evaluation", "benchmark", "security", or "memory" are evaluated
# only after a stronger state/data/control owner has had a chance to claim the
# family.  This prevents an abstract's related-work prose from owning a paper.
NODE_RULES = [
    ("INFER-PD-DISAGGREGATION", re.compile(r"\b(?:disaggregated|prefill[- /]decode|pd disaggregation)\b", re.I)),
    ("INFER-SPECULATIVE-DECODING", re.compile(r"\b(?:speculative decoding|self[- ]speculative|draft model)\b", re.I)),
    ("INFER-KV-CACHE", re.compile(r"\b(?:kv[- ]?cache|cache eviction|cache sharing|cache compression)\b", re.I)),
    ("INFER-SCHEDULING", re.compile(r"\b(?:scheduling|routing|admission|batching|slo)\b", re.I)),
    ("INFER-GPU-MEMORY", re.compile(r"\b(?:gpu memory|memory management|offload|memory[- ]efficient)\b", re.I)),
    ("INFER-TENSORRT-LLM", re.compile(r"\b(?:kernel|compiler|quantization|pruning|inference engine|serving|throughput|latency)\b", re.I)),
    ("TRAIN-DISTRIBUTED-TRAINING", re.compile(r"\b(?:distributed training|tensor parallel|pipeline parallel|expert parallel|data parallel|all[- ]reduce|collective|federated fine[- ]tuning|100,000 gpus)\b", re.I)),
    ("TRAIN-GRPO", re.compile(r"\b(?:grpo|group[- ]relative|group policy optimization|hierarchy[- ]of[- ]groups)\b", re.I)),
    ("TRAIN-DPO", re.compile(r"\b(?:dpo|direct preference optimization)\b", re.I)),
    ("TRAIN-LORA", re.compile(r"\b(?:lora|low[- ]rank adapters?)\b", re.I)),
    ("TRAIN-RLHF", re.compile(r"\b(?:rlhf|dpo|preference optimization|reward model|policy optimization|alignment)\b", re.I)),
    ("TRAIN-PRETRAINING", re.compile(r"\b(?:pre[- ]?training|training stability|optimizer|gradient|low[- ]precision training)\b", re.I)),
    ("TRAIN-DATA", re.compile(r"\b(?:data mixing|data curation|data contamination|synthetic data)\b", re.I)),
    ("MULTIMODAL-EMBODIED-VLA", re.compile(r"\b(?:vision[- ]language[- ]action|vla|embodied|robot)\b", re.I)),
    ("MULTIMODAL-WORLD-MODELS", re.compile(r"\bworld model\b|action[- ]conditioned", re.I)),
    ("MULTIMODAL-GENERATIVE-PARADIGMS", re.compile(r"\b(?:diffusion language|masked diffusion|video generation|multimodal generation)\b", re.I)),
    ("MODEL-MOE", re.compile(r"\b(?:mixture[- ]of[- ]experts|moe|expert routing)\b", re.I)),
    ("MODEL-LONG-CONTEXT", re.compile(r"\b(?:long[- ]context|context window|sparse attention|linear attention)\b", re.I)),
    ("AGENT-MCP", re.compile(r"\b(?:model context protocol|mcp server|mcp-based|mcp behavior)\b", re.I)),
    ("AGENT-RAG", re.compile(r"\b(?:retrieval[- ]augmented|\brag\b|retrieval augmented)\b", re.I)),
    ("AGENT-MEMORY", re.compile(r"\b(?:agent memory|long[- ]term memor|memory agent|memory system)\b", re.I)),
    ("AGENT-TOOL-CALLING", re.compile(r"\b(?:tool[- ]use|tool use|tool calling|tool description)\b", re.I)),
    ("AGENT-WORKFLOW", re.compile(r"\bworkflow\b|durable execution", re.I)),
    ("AGENT-MULTI-AGENT", re.compile(r"\bmulti[- ]agent\b|agent coordination|agent communication", re.I)),
    ("AGENT-PLANNING", re.compile(r"\b(?:planning|reflection|self[- ]verification)\b", re.I)),
    ("AGENT-PLATFORM", re.compile(r"\b(?:llm agent|ai agent|agentic)\b", re.I)),
    ("PLATFORM-SECURITY", re.compile(r"\b(?:prompt injection|jailbreak|backdoor|data poisoning|membership inference|unlearning|security|privacy)\b", re.I)),
    ("PLATFORM-EVALUATION-SYSTEM", re.compile(r"\b(?:evaluation|benchmark|judge|provenance|reproducib|release gate)\b", re.I)),
]

FEBRUARY_NARRATIVE_LENS = {
    "AGENT-CONTEXT": ("把当前请求与少量历史直接拼入 prompt，短任务中最透明。", "长链任务、来源异构和上下文预算要求把选择、排序、压缩与失效显式化。", "context item identity、admission、ordering、budget 与 provenance", "输入短且来源单一时直接拼接仍是更可验证的基线。"),
    "INFER-CONTINUOUS-BATCHING": ("静态批次一次性组织请求，离线同质 workload 下吞吐可预测。", "在线请求长度与到达时刻不同，batch slot 必须在 token step 间动态回收和补入。", "request admission、sequence slot、step boundary 与 completion/replacement control", "同长度离线批处理或极低并发时静态 batching 仍更简单。"),
    "INFER-DECODE": ("逐 token 完整执行模型并立即提交，语义最直接。", "受约束生成、动态验证和异构执行使 token proposal、约束状态与 commit 分离。", "decode state、constraint automaton、proposal、verification 与 token commit", "无结构约束且规模较小时普通 greedy/sampling decode 仍是可靠基线。"),
    "INFER-REQUEST-LIFECYCLE": ("把每个请求视为一次独立同步调用，控制流最短且状态边界直观。", "流式输出、取消、重试、多阶段执行和异构模型使请求从函数调用演化为有生命周期的状态对象。", "request identity、admission、phase transition、cancellation、completion 与 evidence receipt", "短时、无流式和无外部副作用的请求仍可保留简单同步路径。"),
    "PLATFORM-MULTI-TENANT": ("每个 workload 独占进程和资源，隔离与归因最清楚。", "共享集群中的不可信 agent、工具调用和突发负载要求细粒度隔离、配额与可观测执行边界。", "tenant identity、resource cgroup、quota、policy enforcement 与 attribution evidence", "高风险或稳定满载 workload 仍可采用独占资源减少共享面。"),
    "TRAIN-CHECKPOINT": ("周期性保存完整训练状态，恢复语义最容易证明。", "大模型状态、远端存储和故障频率使保存、增量化、异步落盘与恢复选择成为系统瓶颈。", "parameter/optimizer/RNG state identity、snapshot lineage、durability 与 restore commit", "状态较小或恢复频率低时完整同步 checkpoint 仍最可靠。"),
    "TRAIN-TENSOR-PARALLEL": ("单设备持有完整算子权重，计算与状态边界最直观。", "单层参数和激活超过设备容量后，算子必须切分并把 collective 嵌入前后向控制流。", "tensor shard identity、collective placement、activation/gradient ownership 与 resharding", "模型能装入单设备或通信昂贵时不切分仍更简单高效。"),
    "MODEL-SAMPLING": ("固定 decoding rule 直接从模型分布采样，状态最少且语义清楚。", "安全、质量或计算预算需要在 token commit 前动态改变候选分布。", "logit transformation、proposal distribution、verification 与 token commit", "模型分布已经满足约束或 exact sampling 更重要时固定 decoding 仍是基线。"),
    "INFER-TENSORRT-LLM": ("通用 eager 执行便于调试且无需额外编译状态。", "模型规模、算子形态和 SLO 使执行计划、精度与 kernel 选择成为主要成本。", "graph lowering、kernel/precision 选择与执行计划版本", "工作负载小、形状动态或调试优先时 eager 路径仍合理。"),
    "INFER-GPU-MEMORY": ("权重与运行时状态常驻单设备，状态最透明。", "容量、带宽和并发超过单设备预算后，放置、迁移与回收成为控制问题。", "权重、KV、临时张量的 placement、lifetime 与迁移控制", "模型可完整驻留且负载稳定时静态常驻仍更简单。"),
    "TRAIN-DATA": ("固定语料与统一采样最容易复现。", "规模、污染、重复和能力目标使数据选择与混合直接改变训练结果。", "样本 identity、混合权重、过滤与 provenance", "窄任务且数据稳定时固定快照仍是可靠基线。"),
    "AGENT-TOOL-CALLING": ("固定函数表与一次调用在短任务中边界清楚。", "动态工具、长链错误和不可信描述要求把 capability、参数与结果身份显式化。", "工具 capability、参数验证、调用结果与授权边界", "固定工具集、单一信任域仍适合简单函数调用。"),
    "AGENT-MULTI-AGENT": ("单 agent 保持单一上下文与控制流，最易归因。", "任务分解、异构能力与并行协作引入通信、共享状态和信用分配问题。", "拓扑、消息、共享状态、路由与停止条件", "任务规模小或共享状态成本高时单 agent 仍更稳健。"),
    "AGENT-PLATFORM": ("应用内 agent loop 上手快且状态较少。", "生产中的多租户、长任务、权限与恢复要求独立平台责任。", "agent artifact、runtime、policy、evidence 与 lifecycle control", "单用户、短时、无外部副作用的任务仍可内嵌运行。"),
    "AGENT-RAG": ("请求到达后同步检索最容易保证 query 与 evidence 对齐。", "长链任务、动态 query 与检索延迟要求显式管理检索、取消和 evidence admission。", "query revision、retrieval result identity、freshness 与 context admission", "一次性问题且检索成本较低时同步 RAG 仍是可靠基线。"),
    "AGENT-REFLECTION": ("一次生成后直接提交最短也最容易复现。", "长链任务与环境反馈使系统需要保存 critique、revision 与停止条件。", "critique evidence、revision lineage 与 termination control", "低风险、可即时验证的短输出仍可直接提交。"),
    "INFER-PREFILL": ("Prefill 对完整 prompt 做 dense forward，语义与实现最直接。", "长输入和异构硬件使 token 选择、并行与带宽成为 TTFT 主约束。", "prompt token、attention work、prefill plan 与 KV materialization", "输入较短或 exact dense attention 必须保留时完整 Prefill 仍合理。"),
    "TRAIN-LORA": ("全参数微调保持统一参数语义，模型较小时最简单。", "参数、显存与多租户 adapter 数量增长后需要隔离可训练增量。", "base weight identity、adapter state、merge 与 serving compatibility", "单任务、资源充足且最终只交付一个模型时全参数微调仍成立。"),
    "TRAIN-ZERO": ("完整复制参数、梯度与 optimizer state 的数据并行最容易理解和恢复。", "模型与 optimizer state 超过单卡容量后，需要在不破坏计算布局的前提下切分持久训练状态。", "参数、梯度、optimizer state 的 shard identity、materialization 与 collective control", "模型可装入单卡或结构化算子不兼容分片时，复制状态仍是更简单的基线。"),
    "PLATFORM-MONITORING": ("人工查看告警、日志与 runbook 在事件量较小时最透明。", "事件规模、跨系统证据和响应时限增长后，triage 的读取、判断与动作必须可追踪。", "signal identity、evidence retrieval、diagnosis state、action proposal 与 human approval", "低频高风险事件仍应保留人工主导路径，自动化只提供可审计建议。"),
}
for _node, _lens in FEBRUARY_NARRATIVE_LENS.items():
    reviewlib.NARRATIVE_LENS.setdefault(_node, _lens)


def semantic_signal(row: dict) -> int:
    title = row["title"]
    abstract = row["abstract"]
    value = 0
    for pattern in SIGNALS:
        value += 3 if pattern.search(title) else (1 if pattern.search(abstract) else 0)
    if WEAK.search(title):
        value += 1
    if DOMAIN.search(title):
        value -= 2
    if SURVEY.search(title):
        value -= 1
    return value


def node_for(row: dict) -> str:
    if row["arxiv_id"] in AUTHOR_NODE_OVERRIDES:
        return AUTHOR_NODE_OVERRIDES[row["arxiv_id"]]
    title = row["title"]
    for node, pattern in NODE_RULES:
        if pattern.search(title):
            return node
    text = title + " " + row["abstract"]
    for node, pattern in NODE_RULES:
        if pattern.search(text):
            return node
    raise RuntimeError(f"retained identity lacks Stable Node route: {row['arxiv_id']}")


def closure(row: dict) -> tuple[str, str]:
    text = row["title"] + " " + row["abstract"]
    if DOMAIN.search(row["title"]):
        return "domain_application_without_system_delta", "该工作把模型用于特定领域，但摘要未改变可迁移的 state/data/control owner 或 evaluation/release contract。"
    if SURVEY.search(row["title"]):
        return "survey_or_dataset_without_contract_delta", "该综述、观点或数据集未形成新的可执行系统机制或长期责任边界。"
    if not any(pattern.search(text) for pattern in SIGNALS):
        return "no_ai_system_mechanism_signal", "title+abstract 未出现可归属到 AI System 长期机制的状态、数据流、控制流或证据合同变化。"
    return "localized_quality_or_method_delta", "虽与 AI 研究相关，但公开摘要只显示局部质量/任务方法增量，不足以进入长期 AI System 候选分母。"


def score(row: dict) -> dict:
    title = row["title"]
    signal = semantic_signal(row)
    design = 3 if signal >= 7 else 2
    reach = 3 if re.search(r"\b(?:distributed|platform|serving|workflow|multi[- ]agent|world model|infrastructure|runtime|gpu|security)\b", title, re.I) else 2
    durability = 2 if SURVEY.search(title) or re.search(r"\bbenchmark\b", title, re.I) else 3
    return {"design_delta": design, "system_reach": reach, "durability": durability, "total": design + reach + durability}


def sha_ids(ids: list[str], report_date: str) -> str:
    """Bind even an empty candidate set to its owning Daily window."""
    canonical = report_date + "\n" + "\n".join(sorted(ids))
    return "sha256:" + hashlib.sha256(canonical.encode()).hexdigest()


def load_full_row_reopen_overlay() -> None:
    """Keep the core replay aligned with the later 12,520-row fresh audit."""

    from scripts.audit_february_2026_full_row_semantics import configure_evidence

    configure_evidence(sys.modules[__name__], reviewlib)


def main() -> None:
    load_full_row_reopen_overlay()
    retained_rows: list[tuple[Path, dict]] = []
    day_ledgers: dict[str, dict] = {}
    for day in range(1, 29):
        packet = MONTH / "_sources" / f"daily-202602{day:02d}"
        inventory = json.loads((packet / "inventory.json").read_text())
        rows = []
        for identity in inventory["identities"]:
            row = dict(identity)
            signal = semantic_signal(row)
            if row["arxiv_id"] in AUTHOR_RETENTIONS:
                node = AUTHOR_RETENTIONS[row["arxiv_id"]]
                row.update({
                    "screening_decision": "retained",
                    "screening_status": "candidate_denominator",
                    "reason_code": "fresh_context_false_negative_recovered",
                    "screening_reason": "fresh-context audit confirmed a durable mechanism, ownership, or evaluation-contract delta that the first lexical screen missed; exact-v1 determines the final boundary.",
                    "stable_node_id": node,
                    "score_v2": score(row),
                })
                reviewlib.NODE_OVERRIDES[row["arxiv_id"]] = node
                retained_rows.append((packet, row))
            elif row["arxiv_id"] in AUTHOR_DEMOTIONS:
                row.update({
                    "screening_decision": "closure",
                    "screening_status": "pre_denominator_closure",
                    "reason_code": AUTHOR_DEMOTIONS[row["arxiv_id"]],
                    "screening_reason": (
                        f"{row['title']}：exact-v1 author audit 未显示可迁移的 AI System "
                        "state/data/control owner 或 evaluation/release contract 变化；主题相关或单领域结果不足以 retain。"
                    ),
                })
            elif signal >= 5:
                node = node_for(row)
                row.update({
                    "screening_decision": "retained",
                    "screening_status": "candidate_denominator",
                    "reason_code": "durable_system_delta_requires_exact_v1",
                    "screening_reason": "title+abstract 显示可能改变长期 AI System 机制、ownership 或 evaluation contract；exact-v1 决定最终边界。",
                    "stable_node_id": node,
                    "score_v2": score(row),
                })
                reviewlib.NODE_OVERRIDES[row["arxiv_id"]] = node
                retained_rows.append((packet, row))
            else:
                code, reason = closure(row)
                row.update({
                    "screening_decision": "closure",
                    "screening_status": "pre_denominator_closure",
                    "reason_code": code,
                    "screening_reason": f"{row['title']}：{reason}",
                })
            rows.append(row)
        ids = [row["arxiv_id"] for row in rows if row["screening_decision"] == "retained"]
        ledger = {
            "schema": "screening-ledger-v2.1-independent-author",
            "report_date": inventory["report_date"],
            "registered_identities": len(rows),
            "full_semantic_screened": len(rows),
            "candidate_denominator": len(ids),
            "pre_denominator_closed": len(rows) - len(ids),
            "denominator_id": sha_ids(ids, inventory["report_date"]),
            "selection_contract": "durable mechanism/ownership/evaluation delta; topical relevance alone rejected",
            "fresh_context_false_positive_false_negative_audit": "pending_independent_reviewer",
            "identities": rows,
        }
        day_ledgers[inventory["report_date"]] = ledger
        (packet / "screening-ledger-author.json").write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n")

    reviews: dict[str, dict] = {}
    for day in range(1, 29):
        prior_path = MONTH / "_sources" / f"daily-202602{day:02d}" / "exact-v1-review-packet.json"
        if not prior_path.exists():
            continue
        prior = json.loads(prior_path.read_text())
        for review in prior.get("items", []):
            aid = review["primary_identifier"].split(":", 1)[1].removesuffix("v1")
            if aid not in FORCE_REVIEW_IDS and (review.get("result") == "complete" or review.get("withdrawn")):
                reviews[aid] = review
    with ThreadPoolExecutor(max_workers=8) as pool:
        futures = {
            pool.submit(reviewlib.review_one, row, packet): (packet, row)
            for packet, row in retained_rows
            if row["arxiv_id"] not in reviews
        }
        for future in as_completed(futures):
            packet, row = futures[future]
            try:
                review = future.result()
            except Exception as error:
                family = f"SF-2026-ARXIV-{row['arxiv_id'].replace('.', '-')}"
                review = {
                    "source_family_id": family,
                    "event_identity": f"paper-v1:{row['arxiv_id']}",
                    "primary_identifier": f"arXiv:{row['arxiv_id']}v1",
                    "primary_version": f"arXiv:{row['arxiv_id']}v1",
                    "title": row["title"],
                    "stable_node_id": row["stable_node_id"],
                    "books_disposition": "Blocked / Unverified",
                    "review_route": "standard",
                    "access_status": "blocked_external",
                    "result": "blocked",
                    "withdrawn": False,
                    "error": f"review worker exception: {type(error).__name__}: {error}",
                }
            if review.get("result") != "complete" and not review.get("withdrawn"):
                review = review_from_frozen_full_text(row, packet, review)
            if row["arxiv_id"] in WHOLE_PAPER_WITHDRAWAL_IDS:
                review["withdrawn"] = True
                review["result"] = "complete"
            reviews[row["arxiv_id"]] = review

    for day in range(1, 29):
        report_date = f"2026-02-{day:02d}"
        packet = MONTH / "_sources" / f"daily-202602{day:02d}"
        ledger = day_ledgers[report_date]
        day_reviews = [
            reviews[row["arxiv_id"]]
            for row in ledger["identities"]
            if row["screening_decision"] == "retained"
        ]
        node_by_id = {
            row["arxiv_id"]: row["stable_node_id"]
            for row in ledger["identities"]
            if row["screening_decision"] == "retained"
        }
        score_by_id = {
            row["arxiv_id"]: row["score_v2"]["total"]
            for row in ledger["identities"]
            if row["screening_decision"] == "retained"
        }
        for review in day_reviews:
            aid = review["primary_identifier"].split(":", 1)[1].removesuffix("v1")
            node = node_by_id[aid]
            review["stable_node_id"] = node
            review["review_route"] = "deep" if score_by_id[aid] >= 7 else "standard"
            prior, changed_constraint, ownership, coexistence = reviewlib.NARRATIVE_LENS[node]

            apply_frozen_section_overrides(review, aid, packet)

            # Fresh-context evidence audit corrections.  These locators bind
            # the claim to the exact-v1 section that actually carries it;
            # bibliography hits and "expected results" are not evaluations.
            if aid == "2602.03295":
                digest = re.search(r"sha256:[0-9a-f]{64}", review.get("method_locator", ""))
                suffix = f"; {digest.group(0)}" if digest else ""
                base = "https://arxiv.org/html/2602.03295v1; papers/2026/02/_sources/daily-20260205/exact-v1-bodies/2602.03295v1.html"
                review["method_locator"] = f"arXiv:2602.03295v1 HTML — §3 Method; §3.3 Prefill-Only Pruning for Efficient Inference [facet=method]; {base}{suffix}"
                review["evaluation_locator"] = f"arXiv:2602.03295v1 HTML — §4 Experiments; §4.2 Accuracy; §4.3 Inference Speedup; §4.4 Ablation [facet=evaluation]; {base}{suffix}"
                review["limitations_locator"] = f"arXiv:2602.03295v1 HTML — §7 Limitations; Appendix C Robustness to Representation Mismatch [facet=limitations]; {base}{suffix}"
                review["source_kind"] = "HTML"
                review["body_path"] = "papers/2026/02/_sources/daily-20260205/exact-v1-bodies/2602.03295v1.html"
            elif aid == "2602.00509":
                digest = re.search(r"sha256:[0-9a-f]{64}", review.get("method_locator", ""))
                suffix = f"; {digest.group(0)}" if digest else ""
                base = "https://arxiv.org/html/2602.00509v1; papers/2026/02/_sources/daily-20260204/exact-v1-bodies/2602.00509v1.html"
                review["method_locator"] = f"arXiv:2602.00509v1 HTML — §4 System Design [facet=method]; {base}{suffix}"
                review["evaluation_locator"] = f"arXiv:2602.00509v1 HTML — §6 Experiments [facet=evaluation]; {base}{suffix}"
                review["limitations_locator"] = f"Not Disclosed — exact-v1 HTML has no dedicated limitations section; §7 Conclusion does not replace counterevidence [facet=limitations]; {base}{suffix}"
                review["limitations_evidence_excerpt"] = "Not Disclosed — exact-v1 full text 未提供可定位的独立 limitations 章节；§7 Conclusion 仅总结正向结果，不能替代 counterevidence。"
            elif aid == "2602.10090":
                digest = re.search(r"sha256:[0-9a-f]{64}", review.get("method_locator", ""))
                suffix = f"; {digest.group(0)}" if digest else ""
                base = "https://arxiv.org/html/2602.10090v1; papers/2026/02/_sources/daily-20260212/exact-v1-bodies/2602.10090v1.html"
                review["method_locator"] = f"arXiv:2602.10090v1 HTML — §3.3.1 Environment [facet=method]; {base}{suffix}"
                review["evaluation_locator"] = f"arXiv:2602.10090v1 HTML — §6.1 Quality of Synthesized Environments [facet=evaluation]; {base}{suffix}"
                review["limitations_locator"] = f"arXiv:2602.10090v1 HTML — §Limitations [facet=limitations]; {base}{suffix}"
            elif aid == "2602.11686":
                digest = re.search(r"sha256:[0-9a-f]{64}", review.get("method_locator", ""))
                suffix = f"; {digest.group(0)}" if digest else ""
                base = "https://arxiv.org/html/2602.11686v1; papers/2026/02/_sources/daily-20260214/exact-v1-bodies/2602.11686v1.html"
                review["method_locator"] = f"arXiv:2602.11686v1 HTML — §3.1. FSEP: Fully Sharded Expert Parallelism [facet=method]; {base}{suffix}"
                review["evaluation_locator"] = f"arXiv:2602.11686v1 HTML — §5.2. End-to-End Performance [facet=evaluation]; {base}{suffix}"
                review["limitations_locator"] = f"arXiv:2602.11686v1 HTML — §7. Discussion [facet=limitations]; {base}{suffix}"
            elif aid == "2602.15763":
                digest = re.search(r"sha256:[0-9a-f]{64}", review.get("method_locator", ""))
                suffix = f"; {digest.group(0)}" if digest else ""
                base = "https://arxiv.org/html/2602.15763v1; papers/2026/02/_sources/daily-20260219/exact-v1-bodies/2602.15763v1.html"
                review["method_locator"] = f"arXiv:2602.15763v1 HTML — §4.1.1 Asynchronous RL Design for Agentic Training [facet=method]; {base}{suffix}"
                review["evaluation_locator"] = f"arXiv:2602.15763v1 HTML — §6.1.3 Evaluation of Agentic Abilities [facet=evaluation]; {base}{suffix}"
                review["limitations_locator"] = f"arXiv:2602.15763v1 HTML — §7 Conclusion; no isolated async-RL infrastructure ablation disclosed [facet=limitations]; {base}{suffix}"

            if aid in LIMITATIONS_NOT_DISCLOSED_IDS:
                body_rel = review["body_path"]
                body_file = ROOT / body_rel
                body_digest = hashlib.sha256(body_file.read_bytes()).hexdigest()
                source_kind = review.get("source_kind", "HTML")
                source_url = (
                    f"https://arxiv.org/html/{aid}v1"
                    if source_kind == "HTML"
                    else f"https://arxiv.org/pdf/{aid}v1"
                )
                review["limitations_locator"] = (
                    f"Not Disclosed — exact-v1 {source_kind} has no independent limitations or "
                    f"counterevidence section; a positive conclusion does not replace that facet "
                    f"[facet=limitations]; {source_url}; {body_rel}; sha256:{body_digest}"
                )
                review["limitations_evidence_excerpt"] = (
                    "Not Disclosed — exact-v1 full text 未提供可独立定位的 limitations 或 "
                    "counterevidence；正向 Conclusion 不作为该 facet 的替代证据。"
                )

            method_section = review.get("method_locator", "Not Disclosed").split(" [facet=", 1)[0]
            evaluation_section = review.get("evaluation_locator", "Not Disclosed").split(" [facet=", 1)[0]
            limitation_section = review.get("limitations_locator", "Not Disclosed").split(" [facet=", 1)[0]
            review["problem"] = (
                f"`{review['title']}` 是否在 `{node}` 中改变已有状态、数据或控制责任；"
                f"旧路径仍成立于：{prior}"
            )
            method_disclosed = not method_section.startswith("Not Disclosed")
            evaluation_disclosed = not evaluation_section.startswith("Not Disclosed")
            limitations_disclosed = not limitation_section.startswith("Not Disclosed")
            review["method_text"] = (
                (f"exact-v1 的 `{method_section}` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 {ownership}。"
                 if method_disclosed else
                 f"exact-v1 未披露可独立定位的方法章节（`{method_section}`）；本 Review 不以该缺口支持 {ownership} 的已实现机制。")
                + f"触发约束是：{changed_constraint}"
            )
            review["evaluation_text"] = (
                (f"公开验证定位在 `{evaluation_section}`；" if evaluation_disclosed else
                 f"exact-v1 未披露可独立定位的 evaluation（`{evaluation_section}`）；因此不声称经验收益。")
                + "已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。"
            )
            review["limitations_text"] = (
                (f"限制或反证定位在 `{limitation_section}`。" if limitations_disclosed else
                 f"exact-v1 未披露独立 limitations（`{limitation_section}`）；这意味着审阅必须缩小主张，而不是把缺口当作反证。")
                + f"新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：{coexistence}"
            )
            review["claim_boundary"] = (
                f"只支持 {review['primary_version']} 实际披露的机制与实验。"
                + (f"方法定位为 {method_section}；" if method_disclosed else "方法 facet 未独立披露，不据此声称已实现机制；")
                + (f"验证定位为 {evaluation_section}；" if evaluation_disclosed else "evaluation facet 未独立披露，不声称经验收益；")
                + (f"边界定位为 {limitation_section}。" if limitations_disclosed else "独立 limitations 未披露，因而采用更窄主张。")
                + "不外推生产 SLO、多租户、跨硬件或长期可靠性。"
            )
            # A manuscript identity is not an implementation artifact.  Bind
            # disclosed repository/project URLs when present; otherwise state
            # the precise non-disclosure instead of using a generic template.
            body_path = ROOT / review.get("body_path", "")
            body_text = body_path.read_text(errors="ignore") if body_path.exists() else ""
            artifact_urls = sorted(set(re.findall(
                r"https?://(?:github\.com|gitlab\.com|huggingface\.co)/[^\s\"'<>)}]+",
                body_text,
                re.I,
            )))
            artifact_urls = [
                url for url in artifact_urls
                if not re.search(r"github\.com/(?:arXiv/html_feedback|brucemiller/LaTeXML)", url, re.I)
            ]
            if aid in ARTIFACT_OVERRIDES:
                review["artifact_locator"] = ARTIFACT_OVERRIDES[aid]
            elif artifact_urls:
                review["artifact_locator"] = (
                    "External link observed in exact-v1 body: " + artifact_urls[0].rstrip(".,;")
                    + "; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence"
                )
            else:
                review["artifact_locator"] = (
                    f"Not Disclosed — {review['primary_version']} does not disclose a public repository, "
                    "release, commit, or executable artifact used by this review"
                )

        withdrawn = {review["primary_identifier"].split(":", 1)[1].removesuffix("v1") for review in day_reviews if review["withdrawn"]}
        if withdrawn:
            for row in ledger["identities"]:
                if row["arxiv_id"] in withdrawn:
                    row.update({
                        "screening_decision": "closure",
                        "screening_status": "pre_denominator_closure",
                        "reason_code": "withdrawn_primary_source",
                        "screening_reason": "arXiv exact identity 明示 withdrawn；按合同清除 selected/score/Review/Books 痕迹。",
                    })
                    row.pop("score_v2", None)
                    row.pop("stable_node_id", None)
            kept = [
                row["arxiv_id"] for row in ledger["identities"]
                if row["screening_decision"] == "retained"
            ]
            ledger["candidate_denominator"] = len(kept)
            ledger["pre_denominator_closed"] = len(ledger["identities"]) - len(kept)
            ledger["denominator_id"] = sha_ids(kept, ledger["report_date"])
        day_reviews = [review for review in day_reviews if not review["withdrawn"]]
        (packet / "screening-ledger-author.json").write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n")
        (packet / "exact-v1-review-packet.json").write_text(json.dumps({
            "schema": "exact-v1-review-packet-v2.1",
            "report_date": report_date,
            "candidate_count": len(day_reviews),
            "withdrawn_pre_denominator": sorted(withdrawn),
            "complete_count": sum(review["result"] == "complete" for review in day_reviews),
            "blocked_count": sum(review["result"] != "complete" for review in day_reviews),
            "items": sorted(day_reviews, key=lambda review: review["primary_identifier"]),
        }, ensure_ascii=False, indent=2) + "\n")
        print(json.dumps({
            "date": report_date,
            "raw": ledger["registered_identities"],
            "retained": ledger["candidate_denominator"],
            "withdrawn": len(withdrawn),
            "complete": sum(review["result"] == "complete" for review in day_reviews),
            "blocked": sum(review["result"] != "complete" for review in day_reviews),
        }))


if __name__ == "__main__":
    main()
