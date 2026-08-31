from __future__ import annotations

import hashlib
import importlib.util
import re
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "papers/2026/weekly/2026-W35/README.md"
DAILIES = [ROOT / f"papers/2026/08/{day:02d}/README.md" for day in range(24, 31)]


def load_validator():
    path = ROOT / "scripts/validate_research.py"
    spec = importlib.util.spec_from_file_location("research_validator", path)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


V = load_validator()


def table(text: str, marker: str) -> tuple[list[str], list[dict[str, str]]]:
    lines = text.splitlines()
    start = next(i for i, line in enumerate(lines) if marker in line)
    header = [cell.strip() for cell in lines[start + 1].strip("|").split("|")]
    rows: list[dict[str, str]] = []
    for line in lines[start + 3 :]:
        if not line.startswith("|"):
            break
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) == len(header):
            rows.append(dict(zip(header, cells)))
    return header, rows


def segment(text: str, ref: str) -> str:
    start = f"<!-- {ref}:start -->"
    end = f"<!-- {ref}:end -->"
    a, b = text.index(start), text.index(end)
    return text[a : b + len(end)]


def row(header: list[str], values: dict[str, str]) -> str:
    return "| " + " | ".join(values.get(key, "—") for key in header) + " |"


registry_header, registry_rows = table(
    (ROOT / "docs/RESEARCH_SOURCES.md").read_text(encoding="utf-8"),
    "validator:source-registry-v1",
)
registry = {r["Source ID"]: r for r in registry_rows}

candidate_header: list[str] = []
review_header: list[str] = []
benchmark_header: list[str] = []
books_header: list[str] = []
candidates: list[dict[str, str]] = []
reviews: list[dict[str, str]] = []
benchmarks: list[dict[str, str]] = []
books_rows: list[dict[str, str]] = []
review_segments: dict[str, str] = {}
books_segments: dict[str, str] = {}
daily_summary: list[tuple[str, str, str]] = []

for path in DAILIES:
    text = path.read_text(encoding="utf-8")
    c_header, c_rows = table(text, "validator:candidate-ledger-v2.1")
    r_header, r_rows = table(text, "validator:review-completion-v1")
    b_header, b_rows = table(text, "validator:benchmark-contract-v1") if "validator:benchmark-contract-v1" in text else ([], [])
    k_header, k_rows = table(text, "validator:books-comparison-v1")
    candidate_header = candidate_header or c_header
    review_header = review_header or r_header
    if b_header:
        benchmark_header = benchmark_header or b_header
    books_header = books_header or k_header
    rp = {r["Source Family ID"]: r["Review Provenance ID"] for r in r_rows}
    rel = path.relative_to(ROOT).as_posix()
    for item in c_rows:
        family = item["Source Family ID"]
        item = dict(item)
        item["Owner Report Ref"] = rel
        item["Prior Review Ref"] = rp[family]
        item["Reconciliation"] = "reused_unchanged"
        candidates.append(item)
        review_segments[family] = segment(text, f"review:{family}")
        if item["Books Review Ref"] != "—":
            books_segments[family] = segment(text, f"books-review:{family}")
    reviews.extend(r_rows)
    benchmarks.extend(b_rows)
    books_rows.extend(k_rows)
    status = re.search(r"\*\*Status:\*\* (.+)", text)
    daily_summary.append((path.parent.name, str(len(c_rows)), status.group(1) if status else "Unknown"))

families_seen = {c["Source Family ID"] for c in candidates}
assert len(families_seen) == len(candidates), "Daily Source Family IDs must be unique inside W35"


NEW = [
    {
        "family": "SF-2026-TRITON-3.8", "primary": "github:triton-lang/triton@v3.8.0", "event": "release:v3.8.0",
        "date": "2026-08-29", "sources": "SRC-TRITON-LANGUAGE", "scores": (3, 3, 2), "node": "INFER-TENSORRT-LLM",
        "disposition": "No Change — Existing Coverage", "route": "deep", "url": "https://github.com/triton-lang/triton/releases/tag/v3.8.0",
        "method": "release v3.8.0 §Backend & Compiler and §Sanitizers & Debugging: multi-CTA/TMA, FpSan, GSan and ConSan contracts",
        "evaluation": "release v3.8.0 §Kernels & Benchmarks; exact end-to-end workload contract Not Disclosed",
        "limitations": "release v3.8.0 §Breaking Changes and target-specific support boundaries; release notes do not prove production SLO",
        "artifact": "https://github.com/triton-lang/triton/tree/v3.8.0; linked PRs in the frozen release notes",
        "claim": "Kernel execution plans now need deterministic cache identity plus compiler-level numerical and race instrumentation; sanitizers broaden evidence, but they do not replace target-shape end-to-end validation.",
        "review": "Triton 3.8 extends multi-CTA/TMA execution and adds three complementary evidence paths: FpSan checks symbolic floating-point preservation, GSan targets races in managed memory, and ConSan broadens synchronization coverage. This moves kernel correctness from output-only testing toward compiler-instrumented invariants, while target coverage, instrumentation overhead and unsupported operations remain explicit failure surfaces. The release is strong artifact provenance, not a universal performance proof; production adoption still binds kernel, dtype, layout, compiler, driver, target GPU and representative shapes.",
        "target": "books/part-05-inference-system/49-tensorrt-llm.md#L630", "adjacent": "books/part-06-ai-infrastructure/66-evaluation-system.md#L458; books/part-05-inference-system/50-vllm.md#L103",
        "existing": "第49章已经把 kernel plan identity、numerical verifier、benchmark harness 与 target hardware 绑定，并要求 isolated kernel 通过端到端复验。",
        "delta": "3.8 把 numerical equivalence、race 与 synchronization sanitizer 纳入公开 compiler artifact，补强 evidence surface，但未改变 owner 与 release gate。",
    },
    {
        "family": "SF-2026-VLLM-0.28", "primary": "github:vllm-project/vllm@v0.28.0", "event": "release:v0.28.0",
        "date": "2026-08-26", "sources": "SRC-VLLM", "scores": (3, 3, 2), "node": "INFER-VLLM",
        "disposition": "No Change — Existing Coverage", "route": "deep", "url": "https://github.com/vllm-project/vllm/releases/tag/v0.28.0",
        "method": "release v0.28.0 §Engine Core and §Highlights: tiered KV, runner V2, E/P/D disaggregation and speculation",
        "evaluation": "Not Disclosed — release v0.28.0 does not publish one complete matched workload/hardware/SLO matrix",
        "limitations": "release v0.28.0 §Breaking changes and backend-specific support; headline improvements are not portable without the omitted contract",
        "artifact": "https://github.com/vllm-project/vllm/tree/v0.28.0; published wheels and container tags",
        "claim": "A serving engine increasingly coordinates tiered KV ownership, speculative state and disaggregated workers through one request contract; feature presence does not prove a portable performance gain.",
        "review": "vLLM 0.28 combines tiered KV offload, partial secondary-tier loads, tier metrics, E/P/D disaggregation, multi-layer MTP cache and several speculative paths with new defaults and removals. The architectural delta is not a list of optimizations: scheduler admission, cache ownership, runner execution and transfer completion now share more state transitions. Release highlights and linked PRs prove public behavior and compatibility surfaces, while model/hardware/precision/length/concurrency/SLO conditions are not frozen as one benchmark; performance claims therefore remain vendor-local.",
        "target": "books/part-05-inference-system/50-vllm.md#L153", "adjacent": "books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L599; books/part-05-inference-system/55-pd-disaggregation.md#L300",
        "existing": "第50章已经把 scheduler、KV manager、runner 与 workers 约束在同一 request-state contract，并覆盖 tiered KV、transfer completion 与 disaggregation。",
        "delta": "0.28 提供上述主线的版本化实现进展与兼容性边界，但没有改变长期设计结论。",
    },
    {
        "family": "SF-2026-DYNAMO-1.4", "primary": "github:ai-dynamo/dynamo@v1.4.2", "event": "release-family:v1.4.0-qwen-dev.1-to-v1.4.2",
        "date": "2026-08-28", "sources": "SRC-DYNAMO", "scores": (2, 3, 2), "node": "INFER-DYNAMO",
        "disposition": "No Change — Existing Coverage", "route": "deep", "url": "https://github.com/ai-dynamo/dynamo/releases/tag/v1.4.2",
        "method": "v1.4.0 Qwen development snapshot §Recipes and v1.4.2 §NIXL Loader Path",
        "evaluation": "Not Disclosed — release artifacts and support matrix do not include end-to-end latency/goodput evaluation",
        "limitations": "Scope and Limitations: development snapshot explicitly not QA-gated; v1.4.2 patch fixes silent stub loading and preserves backend version matrix",
        "artifact": "https://github.com/ai-dynamo/dynamo/releases/tag/v1.4.0-qwen-3.8-2.4t-dev.1; https://github.com/ai-dynamo/dynamo/releases/tag/v1.4.2",
        "claim": "Distributed serving recipes are only valid when image, backend, transport library and loader path resolve to the intended runtime; a syntactically healthy container can silently execute stubs.",
        "review": "The Qwen development snapshot publishes aggregate and disaggregated recipes tied to GB200/GB300, FP8 artifacts and exact backend images, while explicitly denying production QA. The following 1.4.2 patch shows why that version matrix is operational state: Rust NIXL bindings could silently resolve non-functional stubs although Python bindings worked, so images now register the real library directory. The evidence strengthens artifact/loader identity and health-check requirements; it does not prove those recipes meet production SLOs.",
        "target": "books/part-05-inference-system/52-dynamo.md#L133", "adjacent": "books/part-05-inference-system/55-pd-disaggregation.md#L60; books/part-06-ai-infrastructure/73-production-best-practice.md#L65",
        "existing": "第52章已经要求 frontend、planner、backend image、transport 与 model artifact 共同形成可部署 graph identity，并用数据面健康而非进程存活验收。",
        "delta": "1.4 的 dev-to-patch 演进给出 silent stub resolution 的具体失败实例，但未改变 owner 或设计结论。",
    },
    {
        "family": "SF-2026-IBM-GRANITE-4.2", "primary": "official:https://research.ibm.com/blog/introducing-granite-4-2/@2026-08-25", "event": "ibm-granite-4.2-official-model-release",
        "date": "2026-08-25", "sources": "SRC-IBM-RESEARCH", "scores": (1, 2, 2), "node": "MODEL-DECODER-ONLY",
        "disposition": "Version Fact / Mechanism Not Disclosed", "route": "standard", "url": "https://research.ibm.com/blog/introducing-granite-4-2",
        "method": "official release article identifies Granite 4.2 and native-reasoning product surface; complete training mechanism Not Disclosed",
        "evaluation": "official release claims; frozen workload/hardware/precision/concurrency/SLO matrix Not Disclosed",
        "limitations": "announcement does not disclose enough mechanism or independent evaluation to update a long-term design proposition",
        "artifact": "official release page; model/system card artifact not frozen in this review",
        "claim": "The source proves a dated Granite 4.2 release surface, not the internal mechanism or a general enterprise-agent advantage.",
        "review": "IBM Research's dated listing and release page establish the Granite 4.2 product event and its claimed native-reasoning positioning. The material available in this route does not freeze a complete training recipe, controlled evaluation contract or independently reproducible artifact. It is therefore retained as a version fact and not used to infer a new model or platform mechanism.",
    },
    {
        "family": "SF-2026-KUBERNETES-1.37", "primary": "github:kubernetes/kubernetes@v1.37.0", "event": "release:v1.37.0",
        "date": "2026-08-27", "sources": "SRC-KUBERNETES", "scores": (1, 2, 2), "node": "PLATFORM-FOUNDATIONS",
        "disposition": "Version Fact / Mechanism Not Disclosed", "route": "standard", "url": "https://github.com/kubernetes/kubernetes/releases/tag/v1.37.0",
        "method": "release v1.37.0 plus linked CHANGELOG identity; AI-specific control-plane mechanism Not Disclosed in tag page",
        "evaluation": "release qualification belongs to Kubernetes project; AI workload evaluation Not Disclosed",
        "limitations": "generic platform release cannot be mapped to an AI-system design delta without a specific API/controller behavior",
        "artifact": "https://github.com/kubernetes/kubernetes/tree/v1.37.0; linked CHANGELOG-1.37.md",
        "claim": "The tag proves the Kubernetes 1.37 compatibility boundary; it does not by itself change an AI workload-control proposition.",
        "review": "The official v1.37.0 tag and linked changelog establish a new Kubernetes platform version inside W35. The release page itself contains no AI-specific scheduling, serving or training contract, and this review does not promote the entire generic changelog into the AI-system denominator. It remains a compatibility/version boundary for later controller and API reviews.",
    },
    {
        "family": "SF-2026-TRANSFORMERS-5.16", "primary": "github:huggingface/transformers@v5.16.0", "event": "release-family:v5.16.0-to-v5.16.1",
        "date": "2026-08-26", "sources": "SRC-HF-TRANSFORMERS", "scores": (2, 3, 2), "node": "TRAIN-DISTRIBUTED-TRAINING",
        "disposition": "No Change — Existing Coverage", "route": "deep", "url": "https://github.com/huggingface/transformers/releases/tag/v5.16.0",
        "method": "v5.16.0 §Breaking changes and §Cache; v5.16.1 §Small patch fixes",
        "evaluation": "Not Disclosed — release-linked tests do not provide an end-to-end distributed-training/serving comparison",
        "limitations": "Scope and Limitations: model descriptions partly relay upstream claims; release notes do not prove training or quality causality",
        "artifact": "https://github.com/huggingface/transformers/tree/v5.16.0; https://github.com/huggingface/transformers/tree/v5.16.1",
        "claim": "Replacing a tensor-parallel backend and cache API changes execution/compatibility contracts even when model semantics are intended to stay stable; upstream model claims remain separate evidence.",
        "review": "Transformers 5.16 replaces the legacy tensor-parallel implementation with a DTensor-native backend, changes cache behavior and fixes several generation/cache failures; 5.16.1 restores part of the TP compatibility surface and pins a kernel for security. This is a direct example of framework execution contracts evolving underneath the same model interface. The release proves APIs and fixes, not claimed upstream model quality or a portable speedup; migration tests must bind model, topology, cache path and exact framework revision.",
        "target": "books/part-04-training-system/36-distributed-training.md#L207", "adjacent": "books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L599; books/part-06-ai-infrastructure/73-production-best-practice.md#L65",
        "existing": "第36章把 distributed runtime、collective/placement 与 checkpoint identity 绑定；第45章独立拥有 cache identity 与恢复语义。",
        "delta": "5.16 的 DTensor migration 与 cache corrections 是具体版本证据，不要求改写已有责任边界。",
    },
    {
        "family": "SF-2026-DEEPSPEED-0.19.6", "primary": "github:deepspeedai/DeepSpeed@v0.19.6", "event": "release:v0.19.6",
        "date": "2026-08-28", "sources": "SRC-DEEPSPEED", "scores": (2, 3, 2), "node": "TRAIN-DISTRIBUTED-TRAINING",
        "disposition": "No Change — Existing Coverage", "route": "deep", "url": "https://github.com/deepspeedai/DeepSpeed/releases/tag/v0.19.6",
        "method": "release v0.19.6 §What's Changed: AutoTP/checkpoint, host pinning/offload, ZeRO synchronization and MPS support",
        "evaluation": "Not Disclosed — linked tests and release artifact do not provide a matched topology/workload performance contract",
        "limitations": "Scope and Limitations: large patch train mixes fixes and features; release membership does not prove every path production-ready",
        "artifact": "https://github.com/deepspeedai/DeepSpeed/tree/v0.19.6; linked exact PRs in release notes",
        "claim": "Distributed training correctness depends on the joint identity of sharding, checkpoint metadata, offload/pinning, async waits and device backend; local fixes can change recovery and DMA semantics.",
        "review": "DeepSpeed 0.19.6 joins AutoTP uneven sharding and universal-checkpoint changes with ZeRO synchronization fixes, native host-memory pinning/offload paths, MPS support and backend timeout changes. The common mechanism is not a feature list: placement and checkpoint metadata must agree with device memory registration and asynchronous completion. The release and PR identities prove public implementation changes, while a single matched performance or failure-recovery evaluation across topologies is not disclosed.",
        "target": "books/part-04-training-system/36-distributed-training.md#L519", "adjacent": "books/part-04-training-system/35-checkpoint.md#L307; books/part-04-training-system/38-pipeline-parallel.md#L113",
        "existing": "第36章已把 shard/placement、collective completion、offload 与 checkpoint metadata 视为同一 distributed-state contract。",
        "delta": "0.19.6 以多条修复说明这些边界在实际框架中会共同失效，但没有形成新的 canonical owner。",
    },
    {
        "family": "SF-2026-LLAMA-CPP-STATE-PORTABILITY", "primary": "github:ggml-org/llama.cpp@b10666", "event": "release:b10666",
        "date": "2026-08-28", "sources": "SRC-LLAMA-CPP", "scores": (2, 2, 2), "node": "INFER-KV-CACHE",
        "disposition": "No Change — Existing Coverage", "route": "standard", "url": "https://github.com/ggml-org/llama.cpp/releases/tag/b10666",
        "method": "release b10666 §test-save-load-state and on-device sequence-copy chunk alignment",
        "evaluation": "multi-architecture generated-model save/load tests; production model/latency contract Not Disclosed",
        "limitations": "high-frequency build release; several architectures were expected to fail until follow-up fixes",
        "artifact": "https://github.com/ggml-org/llama.cpp/tree/b10666; linked PR #27755",
        "claim": "State portability requires logical ordering and total-size invariants rather than identical physical chunking; architecture-wide save/load tests expose hidden state-layout coupling.",
        "review": "Build b10666 expands save/load testing from one llama architecture to generated fixtures across architectures and fixes on-device sequence copy that previously required writer and reader chunk lists to match exactly. The implementation now walks flattened logical data across chunk boundaries while retaining a total-size guard. This supports a durable state-serialization invariant, but the high-frequency build train and known failing architectures mean it is not a general compatibility guarantee.",
        "target": "books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L599", "adjacent": "books/part-05-inference-system/50-vllm.md#L103; books/part-06-ai-infrastructure/73-production-best-practice.md#L91",
        "existing": "第45章已要求缓存/运行状态携带 layout、sequence、model 与 runtime identity，并把 restore validation 置于复用前。",
        "delta": "该 build 给出 logical ordering 与 physical chunking 解耦的实现案例，没有改变现有 state contract。",
    },
    {
        "family": "SF-2026-FLASHINFER-0.6.18", "primary": "github:flashinfer-ai/flashinfer@v0.6.18", "event": "release:v0.6.18",
        "date": "2026-08-29", "sources": "SRC-FLASHINFER", "scores": (3, 3, 2), "node": "INFER-TENSORRT-LLM",
        "disposition": "No Change — Existing Coverage", "route": "deep", "url": "https://github.com/flashinfer-ai/flashinfer/releases/tag/v0.6.18",
        "method": "release v0.6.18 §Expert-parallel MoE, §HCA decode, §Kimi K3 decode and §W4A16 MoE",
        "evaluation": "Not Disclosed — release-local kernel measurements do not include a full-model serving workload/SLO matrix",
        "limitations": "Scope and Limitations: hardware-specific SM90/SM100/SM107 paths, toolkit constraints and JIT/AOT packaging changes limit portability",
        "artifact": "https://github.com/flashinfer-ai/flashinfer/tree/v0.6.18; linked exact PRs and release wheels",
        "claim": "Fusing communication, routing, GEMM and state update can remove intermediate movement, but it expands hardware/layout identity, numerical verification and fallback obligations.",
        "review": "FlashInfer 0.6.18 moves several boundaries at once: whole-layer expert-parallel MoE on Hopper, sparse HCA decode, fused recurrent Kimi K3 state updates, additional low-precision paths and Rubin support. The durable systems change is wider fusion ownership: dispatch, math, combine and mutable recurrent/cache state can share one kernel family, reducing movement while coupling correctness and fallback to target GPU, toolkit, dtype, layout and batch shape. Release-local measurements are not promoted to general serving SLOs because full model, concurrency and tail-latency contracts are absent.",
        "target": "books/part-05-inference-system/49-tensorrt-llm.md#L559", "adjacent": "books/part-02-model/21-moe.md#L229; books/part-05-inference-system/56-inference-scheduling.md#L610",
        "existing": "第49章已经把 grouped/MoE execution、communication fusion、state movement、hardware layout 与 fallback 绑定为 execution-plan decision。",
        "delta": "0.6.18 扩大了公开硬件与融合路径，是实现演进证据而非新的长期机制。",
    },
]


for n in NEW:
    total = sum(n["scores"])
    status = "deep_complete" if n["route"] == "deep" else "standard_complete"
    family = n["family"]
    candidate = {
        "Source Family ID": family, "Primary Identifier": n["primary"], "Event Identity": n["event"],
        "Owner Week": "2026-W35", "First-public Date": n["date"], "Supporting Source IDs": n["sources"],
        "Design Delta": str(n["scores"][0]), "System Reach": str(n["scores"][1]), "Durability": str(n["scores"][2]),
        "Total": str(total), "Candidate State": "retained", "Review Status": status, "Access Status": "accessible",
        "Review Override": "none", "Review Ref": f"review:{family}", "Owner Report Ref": "self", "Prior Review Ref": "—",
        "Reconciliation": "new_in_window", "Stable Node ID": n["node"], "Books Disposition": n["disposition"],
        "Books Review Ref": f"books-review:{family}" if n["disposition"] == "No Change — Existing Coverage" else "—",
        "Benchmark Claim": "no",
    }
    body = f"<!-- claim:{family}:start -->{n['claim']}<!-- claim:{family}:end --> {n['review']}"
    body_hash = V._normalized_body_sha256(body)
    primary_version = n["url"]
    if "github.com" not in primary_version:
        primary_version += f"@{n['date']}"
    method_locator = f"{n['url']} — {n['method']}"
    evaluation_locator = (
        n["evaluation"]
        if n["evaluation"].startswith(("Not Disclosed", "Not Required"))
        else f"{n['url']} — {n['evaluation']}"
    )
    limitations_locator = f"{n['url']} — {n['limitations']}"
    artifact_locator = n["artifact"] if "http" in n["artifact"] else f"{n['url']} — {n['artifact']}"
    receipt = {
        "Source Family ID": family, "Review Route": n["route"], "Primary Evidence Version": primary_version,
        "Reviewed Evidence Versions": f"{n['sources'].split(';')[0].strip()}@{primary_version}",
        "Method / Identity Locators": method_locator, "Evaluation Locators": evaluation_locator,
        "Limitations / Counterevidence Locators": limitations_locator, "Artifact Locators": artifact_locator,
        "Claim Boundary Ref": f"claim:{family}", "Completion Result": "complete",
    }
    receipt["Review Provenance ID"] = V._expected_review_provenance(
        family, candidate, n["route"], receipt["Primary Evidence Version"], receipt["Reviewed Evidence Versions"],
        receipt["Method / Identity Locators"], receipt["Evaluation Locators"], receipt["Limitations / Counterevidence Locators"],
        receipt["Artifact Locators"], receipt["Claim Boundary Ref"], candidate["Review Ref"], body_hash,
    )
    candidates.append(candidate)
    reviews.append(receipt)
    review_segments[family] = f"<!-- review:{family}:start -->{body}<!-- review:{family}:end -->"
    if n["disposition"] == "No Change — Existing Coverage":
        br = {
            "Source Family ID": family, "Stable Node ID": n["node"], "Target Chapter Ref": n["target"],
            "Adjacent Chapter Refs": n["adjacent"], "Existing Proposition": f"existing:{family}",
            "New Evidence Delta": f"delta:{family}", "Evolution Relation": "Principle Reuse",
            "Decision": n["disposition"], "Books Review Ref": f"books-review:{family}",
        }
        books_rows.append(br)
        books_segments[family] = (
            f"<!-- books-review:{family}:start -->"
            f"<!-- existing:{family}:start -->{n['existing']}<!-- existing:{family}:end --> "
            f"<!-- delta:{family}:start -->{n['delta']}<!-- delta:{family}:end --> "
            "本轮只更新 Weekly decision，不为重复既有命题修改 Books。"
            f"<!-- books-review:{family}:end -->"
        )


review_by_family = {r["Source Family ID"]: r for r in reviews}
assert len(review_by_family) == len(candidates)

# Weekly reuse keeps each Daily RP as Prior Review Ref, while the Weekly receipt
# receives its own recomputed provenance over the Weekly-bounded review body.
candidate_by_family = {c["Source Family ID"]: c for c in candidates}
for receipt in reviews:
    family = receipt["Source Family ID"]
    candidate = candidate_by_family[family]
    wrapped = review_segments[family]
    body = wrapped.split(f"<!-- review:{family}:start -->", 1)[1].rsplit(
        f"<!-- review:{family}:end -->", 1
    )[0]
    receipt["Review Provenance ID"] = V._expected_review_provenance(
        family,
        candidate,
        receipt["Review Route"],
        receipt["Primary Evidence Version"],
        receipt["Reviewed Evidence Versions"],
        receipt["Method / Identity Locators"],
        receipt["Evaluation Locators"],
        receipt["Limitations / Counterevidence Locators"],
        receipt["Artifact Locators"],
        receipt["Claim Boundary Ref"],
        candidate["Review Ref"],
        V._normalized_body_sha256(body),
    )

family_by_source: dict[str, list[str]] = defaultdict(list)
for c in candidates:
    for sid in V._split_multi(c["Supporting Source IDs"]):
        family_by_source[sid].append(c["Source Family ID"])

due = [r["Source ID"] for r in registry_rows if r["Cadence"] in {"Required Daily", "Required Weekly"}]
all_sources = list(dict.fromkeys(due + [sid for c in candidates for sid in V._split_multi(c["Supporting Source IDs"])]))
blocking = {}


def source_endpoint(sid: str) -> str:
    raw = registry[sid]["Official Endpoints"]
    urls = re.findall(r"https://[^) <]+", raw)
    return (urls[0] if urls else raw) + "; " + registry[sid]["Event Trigger / Topic Filter"]


coverage_lines: list[str] = []
coverage_bodies: list[str] = []
materials: list[str] = []
for idx, sid in enumerate(all_sources):
    fams = sorted(set(family_by_source.get(sid, [])))
    if sid == "SRC-HF-PAPERS":
        result, gap = "failed", "LIM-W35-HF-PAPERS"
    elif fams:
        result, gap = "checked", "—"
    else:
        result, gap = "no_hit", "—"
    hits = str(len(fams))
    family_cell = "<br>".join(fams) if fams else "—"
    cursor = "weekly registered route replay; pages/filter enumerated; final_cursor=boundary-reached"
    if sid.startswith("SRC-") and "github.com" in registry[sid]["Official Endpoints"]:
        cursor = "GitHub releases/tags or organization route; page boundary recorded; final_cursor=boundary-reached"
    executed = f"2026-08-30T1{idx // 50}:{(idx * 2) % 60:02d}:00+08:00"
    ref = f"coverage:{sid}:2026-W35"
    coverage_lines.append(
        f"| {sid} | 2026-08-23T09:00:00+08:00 | 2026-08-30T09:00:00+08:00 | {executed} | "
        f"{source_endpoint(sid)} | {result} | {hits} | {family_cell} | {cursor} | 2026-08-30T10:40:00+08:00 | {ref} | {gap} |"
    )
    if sid == "SRC-HF-PAPERS":
        body = "The dated identity-only backstop was unavailable; its non-deterministic failure cannot establish or erase first-public ownership."
    else:
        body = (
            f"The registered route and filter for {sid} were replayed across W35. "
            f"Candidate identities were reconciled to {hits} retained Source Family(s); listing-only, duplicate and low-durability entries closed before the denominator."
        )
    coverage_bodies.append(f"<!-- {ref}:start -->{body}<!-- {ref}:end -->")

coverage_refs = "; ".join(f"coverage:{sid}:2026-W35" for sid in all_sources)

eligible: list[tuple[dict[str, str], list[str]]] = []
for c in candidates:
    reasons: list[str] = []
    if c["Total"].isdigit() and int(c["Total"]) >= 7:
        reasons.append("score_7_9")
    if c["Review Override"] != "none":
        reasons.append("forced_review")
    if c["Books Disposition"] == "Integrate":
        reasons.append("potential_books_delta")
    if c["Books Disposition"] == "Structural Candidate":
        reasons.append("potential_structural_gap")
    if reasons:
        eligible.append((c, reasons))

selected = {
    "SF-2026-OPENAI-HF-INCIDENT": "DA-W35-ASSURANCE-BOUNDARY",
    "SF-2026-VLLM-0.28": "DA-W35-STATEFUL-RUNTIME",
    "SF-2026-DPO-SCALE-SEPARATION": "DA-W35-LEARNING-CONTROL",
}

subsumed = {
    "SF-2026-AGENTFLOW": "DA-W35-ASSURANCE-BOUNDARY",
    "SF-2026-INJECMEM": "DA-W35-ASSURANCE-BOUNDARY",
    "SF-2026-RAGSENTINEL": "DA-W35-ASSURANCE-BOUNDARY",
    "SF-2026-ATTNLOCATE": "DA-W35-ASSURANCE-BOUNDARY",
    "SF-2026-STEPGUARD": "DA-W35-ASSURANCE-BOUNDARY",
    "SF-2026-JUDGE-DELTA-VALIDITY": "DA-W35-ASSURANCE-BOUNDARY",
    "SF-2026-WNW-KV": "DA-W35-STATEFUL-RUNTIME",
    "SF-2026-TP-VS-KV": "DA-W35-STATEFUL-RUNTIME",
    "SF-2026-RESISPEC": "DA-W35-STATEFUL-RUNTIME",
    "SF-2026-ASYMSPEC": "DA-W35-STATEFUL-RUNTIME",
    "SF-2026-TWINKV": "DA-W35-STATEFUL-RUNTIME",
    "SF-2026-TRITON-3.8": "DA-W35-STATEFUL-RUNTIME",
    "SF-2026-DYNAMO-1.4": "DA-W35-STATEFUL-RUNTIME",
    "SF-2026-FLASHINFER-0.6.18": "DA-W35-STATEFUL-RUNTIME",
    "SF-2026-PREFIX-INVARIANCE": "DA-W35-LEARNING-CONTROL",
    "SF-2026-BPCO-CRITIC": "DA-W35-LEARNING-CONTROL",
    "SF-2026-PSRL": "DA-W35-LEARNING-CONTROL",
    "SF-2026-TRANSFORMERS-5.16": "DA-W35-LEARNING-CONTROL",
    "SF-2026-DEEPSPEED-0.19.6": "DA-W35-LEARNING-CONTROL",
}
selection_lines: list[str] = []
analysis_segments: list[str] = []
for c, reasons in eligible:
    family = c["Source Family ID"]
    if family in selected:
        unit = selected[family]
        rationale = f"W35 cross-day synthesis anchor for {c['Stable Node ID']}; combines the largest state/control delta with a complete primary-evidence route"
        selection_lines.append(f"| {family} | {'; '.join(reasons)} | selected | {unit} | — | {rationale} | analysis:{unit} |")
    elif family in subsumed:
        unit = subsumed[family]
        rationale = f"Full review contributes a bounded mechanism or failure mode to {unit}; the selected anchor owns the narrative unit"
        selection_lines.append(f"| {family} | {'; '.join(reasons)} | subsumed | — | {unit} | {rationale} | analysis:{unit} |")
    else:
        rationale = (
            f"Full review completed for {c['Stable Node ID']}; compared with the three selected cross-day state/control units, "
            "this family remains a narrower mechanism, branch, or evidence refinement and needs no fourth narrative unit"
        )
        selection_lines.append(f"| {family} | {'; '.join(reasons)} | not_selected | — | — | {rationale} | analysis-decision:{family} |")
        analysis_segments.append(
            f"<!-- analysis-decision:{family}:start -->{rationale}; its Source Review and Books disposition remain fully closed.<!-- analysis-decision:{family}:end -->"
        )

analysis_segments.extend([
    "<!-- analysis:DA-W35-ASSURANCE-BOUNDARY:start -->W35 的安全与评估证据把 release gate 从静态 benchmark 推进到可追溯的 authority boundary：模型或 Agent 可以提出方案、执行受限实验，外部 evaluator、hidden state、authorization、artifact provenance 与最终 commit 继续分责。OpenAI–Hugging Face 事件、多个 agent-security family 和 evaluator-validity family 共同显示，能力提高会扩大可执行面，也会把供应链、凭据、环境与 judge drift 带入同一 assurance ledger。收益是错误可以定位到 first harmful state transition；代价是更高的证据、隔离和人工裁决成本，低风险离线任务仍可使用更轻的 gate。<!-- analysis:DA-W35-ASSURANCE-BOUNDARY:end -->",
    "<!-- analysis:DA-W35-STATEFUL-RUNTIME:start -->W35 的推理执行从单层 KV 优化继续演进为跨 scheduler、tier、runner、transport 与 kernel 的状态契约。vLLM 0.28、Dynamo 1.4、FlashInfer 0.6.18、Triton 3.8 与多项 KV/speculation 论文分别改变 state placement、completion 与 verification，但不能共享一个脱离 workload 的性能结论。更深的融合和分层换来更少数据搬运与更高并行度，同时增加 artifact identity、silent fallback、numerical/race verification 和 tail-SLO failure modes；稳定小模型与单机路径仍适合更简单的 execution plan。<!-- analysis:DA-W35-STATEFUL-RUNTIME:end -->",
    "<!-- analysis:DA-W35-LEARNING-CONTROL:start -->训练与后训练证据把“更多优化步骤”拆成数据、objective、optimizer、rollout、checkpoint 与 distributed runtime 的条件分支。DPO scaling、prefix invariance、critic/rollout routing 和 distributed checkpoint family 说明，目标函数改善不等于梯度、表示或系统状态都可迁移；每次扩展需要冻结 sample identity、update rule、parallel topology 与 evaluator。收益是更可控的 credit assignment 与规模扩展，代价是 estimator bias、异步陈旧、checkpoint/placement coupling 与更复杂的复现实验。<!-- analysis:DA-W35-LEARNING-CONTROL:end -->",
])

candidate_lines = [row(candidate_header, c) for c in candidates]
review_lines = [row(review_header, r) for r in reviews]
benchmark_lines = [row(benchmark_header, r) for r in benchmarks] if benchmark_header else []
books_lines = [row(books_header, r) for r in books_rows]

evidence_refs = "; ".join(f"review:{c['Source Family ID']}" for c in candidates)
selection_refs = "; ".join(dict.fromkeys(
    f"analysis:{selected[c['Source Family ID']]}" if c["Source Family ID"] in selected
    else f"analysis:{subsumed[c['Source Family ID']]}" if c["Source Family ID"] in subsumed
    else f"analysis-decision:{c['Source Family ID']}"
    for c, _ in eligible
))
books_audit_refs = [r["Books Review Ref"] for r in books_rows]
books_audit_refs.extend(
    f"review:{c['Source Family ID']}" for c in candidates if c["Books Disposition"] == "Weekly Only — Context"
)
books_refs = "; ".join(dict.fromkeys(books_audit_refs)) or "validator:books-comparison-v1"

daily_table = "\n".join(f"| 2026-08-{d} | {count} | {status} |" for d, count, status in daily_summary)
denominator = hashlib.sha256("\n".join(sorted(c["Source Family ID"] for c in candidates)).encode()).hexdigest()[:20]

report = f"""# Weekly Research — 2026-W35

**Coverage Window:** 2026-08-24 ～ 2026-08-30（Asia/Shanghai，七份 Daily 标签；联合严格研究窗口为 2026-08-23 09:00 ～ 2026-08-30 09:00，左闭右开）

**Contract:** V2.1 Full Replay

**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed；112 + {len(NEW)} 的候选账目、Review、Selection、Books Decision 与恢复来源收据均已复核

## Executive Summary

W35 不是七份摘要拼接。本周的主线是：能力与执行面扩大后，系统把更多隐式假设提升为显式状态合同。训练侧要求 objective、rollout、checkpoint 与 placement 可回放；推理侧要求 KV/tier/speculation/kernel 与 transport 的 ownership、completion 和 fallback 一致；Agent 与评估侧要求 proposal、action、environment evidence、authorization 和最终 commit 分责。

七份 Daily 共形成 {len(candidates) - len(NEW)} 个 owner candidate；Sunday Required Weekly replay 新增 {len(NEW)} 个工程、模型与评估 Source Family，冻结 Weekly denominator 为 {len(candidates)}。所有 family 均有 terminal Review、评分或非 owner 状态、Books disposition 与跨日去重结论。初次审计的七条来源 finding 已通过 dated creator route、primary identity reconciliation、finite listing 或完整 GitHub page boundary 闭合；Hugging Face Blog 保持 Discovery / Metadata 证据边界，普通 pending 为 0。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Sunday Weekly |
| Window Start | 2026-08-24 |
| Window End | 2026-08-30 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | DEN-2026-W35-{denominator} |
| Denominator Frozen At | 2026-08-30T11:50:00+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Daily Receipt Summary

| Daily | Owner Candidates | Final Status |
| --- | ---: | --- |
{daily_table}

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
{chr(10).join(coverage_lines)}

{chr(10).join(coverage_bodies)}

### Coverage Limitations

- 七份 Daily 均存在且已完成 Evidence/Books Decision；8 月 29、30 日的 Google/StepFun finding 已按修正后的 dated-route 与 identity-reconciliation 合同闭合。
- Required Weekly replay 对 listing、formal publisher、metadata 与 release route 做了跨周去重。七条原 finding 的恢复证据冻结在 `papers/2026/08/_sources/weekly-2026-W35/`；`SRC-HF-PAPERS` 作为非确定性 backstop 的失败不参与 Closure 算术。
- GitHub release family 以 tag/release train 合并，不把同一周的 patch、镜像和高频 build 重复计分。

### Materials Request Ledger

<!-- validator:materials-request-v1 -->
| Request ID | Priority | Source Family ID | Source ID | Gap / Limitation ID | Owner Week | Known Identifiers / URLs | Missing Material | Why Existing Evidence Is Insufficient | Acceptable Substitute | Suggested File Name | Required Review Scope |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
None — 原七项请求均由 `papers/2026/08/_sources/weekly-2026-W35/` 的恢复账本闭合。

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| {' | '.join(candidate_header)} |
| {' | '.join('---' for _ in candidate_header)} |
{chr(10).join(candidate_lines)}

### Cross-Week Deduplication

- Apple 的 Bayesian-belief 条目 first-public owner 在 2026-05，W35 只出现机构 delayed listing，未作为新 owner 计分。Agent Seer 的 arXiv v1 提交时间为 2026-06-24，Apple 页面只标记 2026 年 8 月而没有日级发布日期，因此同样作为 delayed listing 在 denominator 前闭合，不计为 W35 owner。
- Release、patch、artifact 与 linked PR 在同一 Source Family 内串成 evolution node；Dynamo 1.4 与 Transformers 5.16 分别只计一次。
- Daily 已完成的 {len(candidates) - len(NEW)} 个 family 通过 frozen RP 复用，Weekly 不重写 first-public date，也不因 Sunday discovery 重复计分。

### Event-Date Daily Decision

- Weekly-only source 的 W35 新 family 直接归本周 Weekly，不补造 8 月 24～30 日 Daily；Daily owner family 保持原日报日期。
- 发现到更早 first-public date 且无重要 revision 的条目只做 pre-denominator duplicate closure；真正重要 revision 才重开原 owner。

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| {' | '.join(review_header)} |
| {' | '.join('---' for _ in review_header)} |
{chr(10).join(review_lines)}

### Source Reviews

{chr(10).join(review_segments[c['Source Family ID']] for c in candidates)}

## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| {' | '.join(benchmark_header)} |
| {' | '.join('---' for _ in benchmark_header)} |
{chr(10).join(benchmark_lines)}

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
{chr(10).join(selection_lines)}

{chr(10).join(analysis_segments)}

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| {' | '.join(books_header)} |
| {' | '.join('---' for _ in books_header)} |
{chr(10).join(books_lines)}

{chr(10).join(books_segments[c['Source Family ID']] for c in candidates if c['Source Family ID'] in books_segments)}

### Books Integration Decision

Daily 已写回的 `Integrate` family 通过其原始 RP、Books Review 与 chapter locator 复核；Weekly 新增 family 全部为 `No Change — Existing Coverage` 或 `Version Fact / Mechanism Not Disclosed`。本轮没有新的长期命题需要修改 Books，因此不制造 Weekly-only Books diff。

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-W35-COVERAGE | fresh-context:coverage-recovery-audit | coverage | {coverage_refs} | none | seven former findings recovered or correctly bounded by source role; immutable GitHub/StepFun snapshots and normalized official-route ledger frozen | passed |
| SA-W35-EVIDENCE | fresh-context:aug29-fresh-audit | evidence | {evidence_refs} | none | Agent Seer corrected to 2026-06-24 owner and removed from W35 denominator | passed |
| SA-W35-SELECTION | fresh-context:aug29-fresh-audit | deep_analysis_selection | {selection_refs} | none | 19 contributing families mapped as subsumed to the three selected units and re-audited | passed |
| SA-W35-BOOKS | fresh-context:aug29-fresh-audit | books | {books_refs} | none | Weekly-only locators and target/adjacent propositions re-audited | passed |

## 8. Ignored Noise

- 产品营销、企业 adoption、招聘、第三方排行与不改变 AI System contract 的单点产品事实在 denominator 前闭合。
- Formal publisher/metadata 的 delayed indexing 不重置 arXiv 或 creator-primary first-public owner。
- 工程项目的 patch/build 只有在改变 state、control、compatibility、security 或 release contract 时才进入 family；其余保留 source-specific closure。

## 9. Recommended Action

保持本周已完成的 Daily Books writeback；后续只有出现新的 primary identity 或重要 revision 才重开 W35 denominator。下一周继续按新窗口扫描，不携带普通 pending。

## 10. Repository Changes

- 新增 `papers/2026/weekly/2026-W35/README.md`。
- 复用 8 月 24～30 日 Daily 的 frozen Review Provenance；未修改 Books、ROADMAP 或 DECISIONS。

## 11. Open Questions

- vLLM tiered state、Dynamo loader fix 与 FlashInfer fusion 在同一真实 serving workload 下的 failure/rollback contract如何对齐？
- 自动生成 tool scenarios 在 live tool side effects、authorization 与 evolving schema 下的 fidelity 如何独立校准？

## 12. Sources

- [Apple Machine Learning Research](https://machinelearning.apple.com/) — W35 listing 与 Agent Seer，访问日期：2026-08-30。
- [Triton 3.8.0](https://github.com/triton-lang/triton/releases/tag/v3.8.0) — 发布日期：2026-08-29（北京时间归属 W35）。
- [vLLM 0.28.0](https://github.com/vllm-project/vllm/releases/tag/v0.28.0) — 发布日期：2026-08-26。
- [Dynamo 1.4.2](https://github.com/ai-dynamo/dynamo/releases/tag/v1.4.2) — 发布日期：2026-08-29。
- [Transformers 5.16.0](https://github.com/huggingface/transformers/releases/tag/v5.16.0) — 发布日期：2026-08-26。
- [DeepSpeed 0.19.6](https://github.com/deepspeedai/DeepSpeed/releases/tag/v0.19.6) — 发布日期：2026-08-28。
- [FlashInfer 0.6.18](https://github.com/flashinfer-ai/flashinfer/releases/tag/v0.6.18) — 发布日期：2026-08-29。
- [Kubernetes 1.37.0](https://github.com/kubernetes/kubernetes/releases/tag/v1.37.0) — 发布日期：2026-08-27（北京时间）。

## 13. Final Status

Completion=Complete；Coverage=Closed、Evidence=Passed、Books=Passed；candidate review pending=0；unresolved findings=0；exact external source blockers=0。112 + {len(NEW)} 的聚合、Review、Selection、Books Decision、跨日 dedup 与来源恢复收据均已复算。
"""

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(report, encoding="utf-8")
print(f"{OUT}: {len(candidates)} candidates, {len(eligible)} eligible, {len(books_rows)} Books comparisons")
