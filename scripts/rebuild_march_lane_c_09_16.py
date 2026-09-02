#!/usr/bin/env python3
"""Author replay for 2026-03-09..16 using the March announcement receipt v2.

This file deliberately imports the lane-C renderer so that report schema,
review receipts, Books comparison and author QA remain identical to the
already-rebuilt 03-17..24 slice.  Only the independently screened denominator,
manual Stable Node routes and paper-specific deep-review synthesis live here.
"""

from __future__ import annotations

import importlib.util
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASE_PATH = ROOT / "scripts/rebuild_march_lane_c_full_replay.py"
SPEC = importlib.util.spec_from_file_location("march_lane_c_base", BASE_PATH)
assert SPEC and SPEC.loader
base = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(base)


# Frozen only after replaying every title + abstract in the v2 owner window.
# This set intentionally includes systems-boundary and evaluation-contract
# candidates even when the final Books comparison is expected to be No Change.
DURABLE_CANDIDATES = set("""
2603.05517 2603.05520 2603.05637 2603.05692 2603.05754 2603.05800 2603.05881
2603.05910 2603.05912 2603.05931 2603.06007 2603.06331 2603.06350
2603.06394 2603.06403
2603.06626 2603.07006 2603.07373 2603.07416 2603.07427 2603.07433 2603.07466
2603.07473 2603.07557 2603.07607 2603.07670 2603.07685 2603.07770 2603.07777
2603.07799 2603.07915 2603.07917 2603.07972 2603.08088 2603.08113 2603.08124
2603.08163 2603.08221 2603.08316 2603.08361 2603.08429 2603.08519 2603.08640
2603.08743 2603.08747 2603.08761 2603.08797 2603.08806 2603.08835 2603.08960
2603.09023 2603.09046 2603.09079 2603.09086 2603.09117 2603.09121 2603.09127
2603.09157 2603.09180 2603.09192 2603.09216 2603.09221 2603.09241 2603.09290
2603.09297 2603.09435 2603.09453 2603.09488 2603.09513 2603.09555 2603.09619
2603.09657 2603.09692 2603.09716 2603.09756 2603.09821 2603.09877 2603.09891
2603.09892
2603.10031 2603.10032 2603.10044 2603.10057 2603.10060 2603.10062 2603.10085
2603.10087 2603.10088 2603.10143 2603.10163 2603.10165 2603.10291 2603.10342
2603.10353 2603.10379 2603.10422 2603.10444 2603.10469 2603.10494 2603.10521
2603.10577 2603.10600 2603.10712 2603.10726 2603.10742 2603.10749 2603.10765
2603.10779 2603.10899
2603.11053 2603.11088 2603.11101 2603.11132 2603.11212 2603.11273 2603.11287
2603.11337 2603.11438 2603.11445 2603.11504 2603.11560 2603.11564 2603.11619
2603.11768 2603.11853 2603.11873 2603.11875 2603.11896 2603.11935 2603.11975
2603.12031 2603.12038 2603.12056 2603.12118 2603.12201 2603.12230 2603.12255
2603.12277 2603.12396 2603.12440 2603.12465 2603.12485 2603.12510 2603.12553
2603.12598 2603.12614 2603.12617 2603.12621 2603.12631 2603.12639 2603.12646
2603.12655 2603.12671 2603.12707 2603.12823 2603.12831 2603.12933 2603.13017
2603.13019 2603.13026 2603.13033 2603.13099 2603.13110 2603.13176 2603.13189
2603.13215
""".split())


NODE_GROUPS = {
    "AGENT-MCP": "05637 07473 10163",
    "AGENT-MEMORY": "07670 09297 09716 10062 10087 10291 10600 11560 11768 11896 12631 13017",
    "AGENT-MULTI-AGENT": "07972 09127 11132 11445 12933 13189",
    "AGENT-PLANNING": "07915 09221",
    "AGENT-RAG": "06198 07379 08429 09891 10143 10765 12396",
    "AGENT-TOOL-CALLING": "05515 09290 10060",
    "AGENT-WORKFLOW": "05517 06007 06394 07607 08806 09192 09619 10742 10779 12056 12614 12621 12823 13019 13110",
    "INFER-KV-CACHE": "08743 09023 09657 10032 10353 10899 11504 11564 12201",
    "INFER-SCHEDULING": "05800 06350 06403 07917 08797 09046 09180 10342 11273 12038 12118 12465 12646 12707 12831 13176",
    "INFER-SPECULATIVE-DECODING": "07416 08088 09555 10088 11053 12617",
    "INFER-TENSORRT-LLM": "05692 05931 07770 08747 09216 10031 10085 11873 11935 12440 12485",
    "MODEL-LONG-CONTEXT": "09023 09892",
    "MODEL-MOE": "06626 08960 09453 09983 10379",
    "MULTIMODAL-EMBODIED-VLA": "05754 08113 08124 08361 09079 09121 09513 10469 10712 11975 12510 12942",
    "MULTIMODAL-REPRESENTATION": "12255",
    "MULTIMODAL-GENERATIVE-PARADIGMS": "09488 09877",
    "MULTIMODAL-WORLD-MODELS": "06331 07799 08519 09086 09241 09756 10422 12553 12639 12655 13033 13215",
    "PLATFORM-EVALUATION-SYSTEM": "05881 05910 05912 06198 07427 08640 08835 09157 09435 09821 10044 10057 10577 10765 11287 11337 11975 13033 13099",
    "PLATFORM-GPU-SCHEDULER": "12031",
    "PLATFORM-SECURITY": "05520 06363 07466 07557 08221 08316 08761 10163 10726 10749 11088 11132 11212 11619 11853 11875 12230 12277 12510 12598 12614 12621 13026 13189",
    "TRAIN-DATA": "07433 09692",
    "TRAIN-DISTRIBUTED-TRAINING": "07006 07373 07685 08163 11101 11438 12671",
    "TRAIN-GRPO": "07777 09117 10165 13019",
    "TRAIN-PRETRAINING": "10444",
    "TRAIN-RLHF": "09692 10494 10521",
}

NODE_OVERRIDES: dict[str, str] = {}
for node, suffixes in NODE_GROUPS.items():
    for suffix in suffixes.split():
        NODE_OVERRIDES[f"2603.{suffix}"] = node

# Resolve deliberate overlaps in favor of the mechanism's canonical owner.
NODE_OVERRIDES.update({
    "2603.09023": "INFER-KV-CACHE",
    "2603.10163": "AGENT-MCP",
    "2603.11132": "PLATFORM-SECURITY",
    "2603.11975": "PLATFORM-EVALUATION-SYSTEM",
    "2603.12510": "PLATFORM-SECURITY",
    "2603.12614": "PLATFORM-SECURITY",
    "2603.12621": "PLATFORM-SECURITY",
    "2603.13019": "TRAIN-GRPO",
    "2603.13189": "PLATFORM-SECURITY",
})


INTEGRATE_SUGGESTIONS = {
    "2603.05800",  # multimodal streaming admission/deadline/dataflow contract
    "2603.05931",  # persistent decode state as accelerator-owned object
    "2603.06350",  # serverless elasticity for sparse expert placement
    "2603.07685",  # MoE training system's expert/parallelism/communication coupling
    "2603.08088",  # hardware-safe speculative tree/rollback contract
    "2603.08797",  # compound inference DAG scheduling, not request-only serving
    "2603.09023",  # demand paging makes context residency explicit runtime state
    "2603.09555",  # compiler-owned O(1) autoregressive state transform
    "2603.10342",  # co-scheduling agent model/tool stages on constrained GPU
    "2603.10353",  # sparse-head parallel placement and load balancing
    "2603.10765",  # end-to-end RAG evaluation contract
    "2603.11438",  # verified policy execution at the collective boundary
    "2603.12118",  # any-to-any multimodal serving DAG and intermediate state
    "2603.12465",  # decomposed inference overhead accounting contract
    "2603.12831",  # CPU/GPU attention piggybacking under explicit SLOs
    "2603.13110",  # agent resource state separated from workflow semantics
}


PAPER_SYNTHESIS = {
    "2603.05800": (
        "多模态生成流同时包含持续到达、异质阶段和实时 deadline；把每个请求当成单次模型调用会隐藏跨阶段排队。",
        "StreamWise 将 modality pipeline、chunk readiness 与 deadline 纳入统一运行时状态，由 scheduler 决定阶段准入、批次拼接和 backpressure，而不是只优化单个 kernel。",
        "作者在其公开模型、设备和请求分布上测量吞吐与尾延迟，足以支持所测实时 pipeline 的联合调度收益；未披露的跨集群网络、租户隔离和生产 SLO 不属于结论。",
        "更细的阶段状态提升利用率，也增加队列、取消和中间结果失效复杂度；离线同质批处理仍适合静态流水线。",
    ),
    "2603.05931": (
        "线性注意力 decode 受反复装载持久状态限制，单纯增加算术单元不能消除片外带宽瓶颈。",
        "该加速器把 recurrent state 固定为片上持久对象，并围绕 decode 的更新依赖组织数据流，使每个 token 只搬运必要输入而非重载完整历史。",
        "FPGA 原型证明给定算子、精度和器件上的带宽/吞吐变化；它没有证明不同线性注意力变体或 GPU runtime 可获得相同比例收益。",
        "持久化减少内存流量，却占用片上容量并绑定状态布局；短序列或状态无法容纳时，通用外存执行仍更灵活。",
    ),
    "2603.06350": (
        "MoE serving 的冷门 expert 长期占据 GPU，会让峰值容量与平均利用率之间产生结构性浪费。",
        "MoEless 将 expert 映射到可弹性实例，并把路由热度、冷启动与数据搬移作为 placement state；dense shared path 与稀疏 expert path 使用不同资源生命周期。",
        "公开实验支持其工作负载下的成本/延迟取舍，但 serverless 冷启动、网络拓扑和 expert 热度稳定性限制外推。",
        "弹性回收降低闲置成本，却把冷启动与跨节点通信引入 token 路径；高且稳定的 expert 利用率仍适合常驻部署。",
    ),
    "2603.07685": (
        "MoE 训练不能只在 dense 并行方案上附加 all-to-all：expert capacity、token dispatch 和并行维度会共同改变通信临界路径。",
        "该工作在 Megatron Core 中把 expert parallel、tensor/data/pipeline parallel 及 dispatcher 实现组合为统一训练配置，并显式管理 token permutation 与负载均衡。",
        "结果证明公开模型和集群配置中的扩展行为；没有披露或未覆盖的网络、失败恢复与极端路由倾斜仍需独立验证。",
        "多维并行提高大规模吞吐，但配置空间、collective 干扰和 straggler 风险同步上升；规模较小时 dense 或较少并行维度更易稳定。",
    ),
    "2603.08088": (
        "树式 speculative decoding 在专用加速器上若沿用 GPU 动态控制流，会因 shape、内存与回滚语义不匹配失去收益。",
        "EAGLE-Pangu 将候选树展平为加速器可执行的静态批结构，并把验证、接受和 KV 提交边界重新组织为硬件安全路径。",
        "Ascend NPU 上的作者实验支持该实现下的接受/延迟收益；结论不等于所有 target/draft 或其他加速器都具备相同瓶颈。",
        "静态化减少运行时分支，却可能增加无效候选计算并限制树形自适应；低接受率时普通 decode 仍更稳健。",
    ),
    "2603.08797": (
        "compound inference 把一次用户请求展开成模型、检索器和后处理 DAG，传统按单模型队列优化会错过关键路径。",
        "论文以 DAG readiness、GPU residency 与跨阶段依赖为调度对象，联合选择 stage placement 和执行次序，使资源决策服从端到端完成时间。",
        "数据中心 GPU 实验验证其公开 DAG 与负载下的端到端结果；未证明任意动态 agent graph 或多租户策略都保持同样收益。",
        "依赖感知提高关键路径利用率，但要求精确 stage profile 与中间状态追踪；单模型独立请求仍可使用较简单的 continuous batching。",
    ),
    "2603.09023": (
        "长 context 即使逻辑上可寻址，也可能无法全部常驻 GPU；静态截断把容量问题误当成语义选择。",
        "该系统将 context page 的驻留、换入、淘汰和故障恢复变成显式 memory-management state，由访问需求而非固定窗口决定物理位置。",
        "评测证明所测模型、介质和访问模式中的容量/延迟关系；它没有证明任意注意力访问都具有足够 locality。",
        "分页扩大可服务 context，但 page fault 会制造尾延迟和抖动；访问密集或上下文较短时完整常驻仍是更可预测的基线。",
    ),
    "2603.09555": (
        "状态空间模型的 O(1) decode cache 常依赖手写模型特例，阻碍跨后端复用和正确性验证。",
        "Compiler-First State Space Duality 从算子语义推导等价 recurrent form，再由编译器生成固定大小的 autoregressive state 与更新程序。",
        "公开模型与后端实验支持等价变换和便携执行；不覆盖的数值精度、算子族和编译目标不能由此推断。",
        "编译推导降低人工特化成本，却增加 IR 语义和数值等价验证责任；不满足 duality 的算子仍需原始序列执行。",
    ),
    "2603.10342": (
        "agent serving 在消费级单 GPU 上交替执行模型推理、工具等待和状态处理，单纯提高 batch 会被阶段阻塞抵消。",
        "AgentServe 将 agent trajectory 切为可调度阶段，并依据显存、tool readiness 与请求依赖共同安排模型执行和状态换入。",
        "作者在其 agent workload 与消费级 GPU 上报告吞吐/延迟，支持受限资源下的算法-系统协同；多 GPU 和生产隔离未被证明。",
        "阶段化可回收等待空隙，但会增加 trajectory checkpoint 与恢复成本；工具少、模型阶段占主导时普通 serving engine 更简单。",
    ),
    "2603.10353": (
        "稀疏 attention head 的实际工作量不均衡，按 head 数量静态切分会让并行 worker 在 decode 中产生 straggler。",
        "S-HPLB 根据活跃 head 与 token workload 重新分配 head parallel work，并把稀疏模式纳入通信和放置决策。",
        "公开 serving 实验支持指定模型与稀疏配置中的负载均衡收益；动态稀疏漂移和不同互连下的开销仍未覆盖。",
        "重分配降低空等，却引入元数据、迁移和额外同步；head 负载均匀时静态并行的控制成本更低。",
    ),
    "2603.10765": (
        "RAG 若分别评测检索和生成，无法归因端到端时延、召回、grounding 与成本之间的耦合。",
        "RAGPerf 把 corpus、retriever、reranker、generator、并发与质量判定绑定到同一可复现实验合同，并保留阶段级指标。",
        "框架证明这些组件可在统一 workload 下比较；具体排名只对所用数据、模型、硬件和 evaluator 有效。",
        "端到端合同改善归因，但实验矩阵和数据版本成本更高；单组件开发阶段仍可使用局部 microbenchmark。",
    ),
    "2603.11438": (
        "GPU collective 的策略若只存在于动态 hook 或运维脚本，执行顺序和安全边界难以复算。",
        "NCCLbpf 将通信策略编译为受限、可组合且可验证的执行单元，在 collective 边界检查并应用调度/传输决定。",
        "作者验证公开策略与 collective workload 的可执行性和开销；不能据此证明任意 eBPF 类程序或故障场景都安全。",
        "可验证策略减少不可控扩展，却限制表达能力并增加 verifier/ABI 兼容责任；固定拓扑仍可采用静态 NCCL 配置。",
    ),
    "2603.12118": (
        "any-to-any 多模态模型包含编码、跨模态变换与解码 DAG，沿用文本 LLM 的单 token 队列会让中间张量和阶段资源失配。",
        "Cornserve 把 modality-specific stage、依赖和中间数据生命周期暴露给 distributed scheduler，联合执行放置、批处理与传输。",
        "公开模型和集群结果支持所测 DAG 的端到端收益；不同模态组合、网络和质量约束仍需重新测量。",
        "DAG-aware serving 提高异质资源利用率，但扩大状态 identity、故障恢复和跨阶段 backpressure 的复杂度；纯文本路径仍适合专用 engine。",
    ),
    "2603.12465": (
        "端到端 LLM latency 常把 framework、launch、memory 和 synchronization 开销混成一个数字，导致优化目标归因错误。",
        "TaxBreak 以分层 instrumentation 将请求时间拆到算子、runtime 与系统边界，并把不可归属空洞作为显式 overhead 类别。",
        "作者数据能说明所测栈中各类开销比例；这些比例不应外推到不同模型、硬件、精度或并发。",
        "更细归因提高优化精度，却增加 tracing 扰动和版本维护；瓶颈明显的稳定路径可先用粗粒度 profiling。",
    ),
    "2603.12831": (
        "混合 LLM 请求在 GPU attention 饱和时仍可能留下 CPU 和数据搬移空隙，单一设备 admission 难同时守住不同 SLO。",
        "论文让 CPU attention work 在 GPU request 间隙 piggyback，并由 SLO slack、阶段和资源占用决定是否卸载与何时回收。",
        "实验支持给定 CPU/GPU、模型和请求混合中的 SLO/吞吐变化；未覆盖的 NUMA、网络和长尾输入不属于证明。",
        "异构并用扩大有效容量，但带来状态同步、预测误差和尾延迟反噬；负载同质或 GPU 未饱和时单 GPU 路径更可控。",
    ),
    "2603.13110": (
        "agent 系统把 token、tool、memory 和并发额度散落在 workflow 代码中，资源压力会反过来破坏行为语义。",
        "AgentRM 把资源描述、allocation、preemption 与 accounting 提升为独立 manager state，并为 agent execution 提供受控 lease。",
        "公开实验或原型只支持论文定义 workload 下的资源协调，不证明 OS 类抽象已经解决语义公平、安全或跨平台兼容。",
        "独立资源层提升可治理性，却增加控制面和 lease failure mode；小规模单 agent 仍可由 workflow 直接持有资源。",
    ),
}


_network_fetch = base.fetch


def fetch_with_exact_v1_cache(url: str, timeout: int = 45):
    """Reuse only exact-version arXiv bodies already fetched by this lane."""
    match = re.search(r"arxiv\.org/(abs|html|pdf)/(2603\.\d+)v1", url)
    if not match:
        return _network_fetch(url, timeout)
    kind, aid = match.groups()
    candidates = []
    for day in range(9, 17):
        body_dir = ROOT / "papers/2026/03/_sources" / f"daily-202603{day:02d}" / "exact-v1-bodies"
        if kind == "abs":
            candidates.extend([body_dir / f"{aid}v1.abs.html", body_dir / f"{aid}v1.html"])
        elif kind == "html":
            candidates.append(body_dir / f"{aid}v1.html")
        else:
            candidates.append(body_dir / f"{aid}v1.pdf")
    for path in candidates:
        if path.exists() and path.stat().st_size > 100:
            data = path.read_bytes()
            if kind != "pdf" or data.startswith(b"%PDF"):
                return 200, data
    return _network_fetch(url, timeout)


def configure() -> None:
    base.fetch = fetch_with_exact_v1_cache
    base.DURABLE_CANDIDATES = DURABLE_CANDIDATES
    base.NODE_OVERRIDES.update(NODE_OVERRIDES)
    base.INTEGRATE_SUGGESTIONS = INTEGRATE_SUGGESTIONS
    base.PAPER_SYNTHESIS.update(PAPER_SYNTHESIS)
    base.NARRATIVE_LENS.setdefault(
        "INFER-TENSORRT-LLM",
        (
            "通用 eager/runtime 路径优先兼容性，适合形状和模型快速变化。",
            "固定热点、异构硬件和严格 SLO 迫使系统显式优化 execution plan、kernel 与 state layout。",
            "图变换、kernel 选择、设备放置、数值精度与执行缓存",
            "模型变化频繁或 workload 较小时，通用执行路径仍具有更低维护成本。",
        ),
    )
    base.NARRATIVE_LENS.setdefault(
        "AGENT-MULTI-AGENT",
        (
            "单 agent 持有完整上下文和控制流，规模小时最容易归因。",
            "任务并行、能力异质和跨信任域协作迫使系统显式管理委托与共享状态。",
            "agent identity、委托边、消息状态、协作协议与冲突处理",
            "任务短且角色不需要隔离时，单 agent 仍有更低协调成本。",
        ),
    )
    base.NARRATIVE_LENS.setdefault(
        "AGENT-RAG",
        (
            "把训练权重或完整上下文视为唯一知识来源，链路短且状态少。",
            "知识时效、私有数据和可引用证据要求在生成前建立可追踪的检索路径。",
            "query、corpus version、retrieval/rerank 与 evidence-to-claim lineage",
            "知识稳定且已被模型可靠覆盖时，直接生成仍具有更低延迟。",
        ),
    )
    base.NARRATIVE_LENS.setdefault(
        "AGENT-TOOL-CALLING",
        (
            "模型只输出文本时，错误影响停留在信息层。",
            "外部 action、side effect 和动态工具目录要求把提议与执行分离。",
            "tool identity、argument validation、authorization、receipt 与 side-effect commit",
            "只读、无副作用查询仍可使用较薄的调用适配层。",
        ),
    )
    base.NARRATIVE_LENS.setdefault(
        "TRAIN-DATA",
        (
            "固定离线数据集让训练可复现，也避免在线选择反馈回路。",
            "数据质量、难度和策略能力随训练变化，使静态配比逐渐失去信息效率。",
            "样本 identity、选择策略、版本、provenance 与训练消费顺序",
            "数据分布稳定且治理优先时，冻结数据仍是更安全的基线。",
        ),
    )
    base.NODE_PATH.setdefault(
        "MULTIMODAL-REPRESENTATION",
        "books/part-03-multimodal-world-models/23-multimodal-representation.md",
    )
    base.NARRATIVE_LENS.setdefault(
        "MULTIMODAL-REPRESENTATION",
        (
            "各模态保留独立 encoder 和静态融合点，职责清楚且便于单独优化。",
            "流式、多轮和跨模态任务要求表示保留时间、来源与可更新状态。",
            "跨模态 token identity、融合、时间锚点与可变表示状态",
            "模态关系固定且输入短时，静态 late fusion 仍具有更低复杂度。",
        ),
    )

    missing = DURABLE_CANDIDATES - set(base.NODE_OVERRIDES)
    if missing:
        raise RuntimeError(f"retained families missing manual Stable Node routes: {sorted(missing)}")


def main() -> None:
    configure()
    raw_total, records, _ = base.load_records()
    start_day = int(sys.argv[1]) if len(sys.argv) > 1 else 9
    end_day = int(sys.argv[2]) if len(sys.argv) > 2 else 16
    if not (9 <= start_day <= end_day <= 16):
        raise ValueError("day range must stay within 2026-03-09..16")
    for day in range(start_day, end_day + 1):
        base.render_day(day, raw_total, records)


if __name__ == "__main__":
    main()
