#!/usr/bin/env python3
"""Materialize fail-closed Daily deltas that lack a persisted body proposition.

The repair keeps exact source identity in Review notes.  Reader-facing prose is
placed before chapter closeout as a conditional mechanism branch, with a hidden
Source Family binding used by the reconciliation ledger.
"""

from __future__ import annotations

import argparse
import csv
import re
from collections import Counter, defaultdict
from pathlib import Path

try:
    from scripts.materialize_books_integration_trace import extract_delta
    from scripts.reconcile_books_integration_semantics import (
        MIN_PERSISTED_PROPOSITION_SCORE,
        best_body_proposition,
        corpus_document_frequency,
    )
except ModuleNotFoundError:  # Direct execution adds scripts/, not the repo root, to sys.path.
    from materialize_books_integration_trace import extract_delta
    from reconcile_books_integration_semantics import (
        MIN_PERSISTED_PROPOSITION_SCORE,
        best_body_proposition,
        corpus_document_frequency,
    )


FORCED_REPAIR = {"SF-FOLD-ONLINE-DEDUP"}

LEGACY_CONDITIONAL_BRANCH_HEADING = "### 经复核仍需显式保留的条件分支"
CONDITIONAL_BRANCH_HEADING = "### 条件化机制分支与共存边界"
LEGACY_CONDITIONAL_BRANCH_INTRO = (
    "下列分支补足主线未能唯一定位的状态、控制权或失败边界。它们不是框架清单：每一段只在所述前置条件"
    "成立时进入设计空间，证据身份与实验限制统一留在章末 Review notes。"
)
CONDITIONAL_BRANCH_INTRO = (
    "主线之外仍存在若干只在特定前提下成立的设计分支。下面按状态与控制权的变化说明它们解决的问题、"
    "新增代价及回退边界；来源身份和实验限制统一留在章末 Review notes。"
)

DELTA_OVERRIDES = {
    "SF-FOLD-ONLINE-DEDUP": (
        "在线去重从反复扫描 LSH bucket 演进为持续维护的 HNSW：数据面把文档映射为适配 Jaccard 的 bitmap signature，"
        "索引 owner 负责增量插入与候选搜索，SIMD 和 cached popcount 只优化执行。它用额外索引状态换在线吞吐；证据"
        "只覆盖给定语料、signature 和 reference-label 设置，不能证明跨语言、任意相似度或最终训练质量。"
    ),
    "SF-2026-ARXIV-2606-06818": (
        "异构 accelerator 调度不能只把设备建模成同质卡数：layer variant、设备能力与非抢占执行时间共同决定"
        "可行 placement，scheduler 需要在 accuracy 约束内选择模型变体和设备组合。该机制只在论文给定的 layer/profile"
        "与非抢占假设下成立；profile 漂移时回退静态兼容设备池。"
    ),
    "SF-2026-ARXIV-2606-06888": (
        "数据受限的预训练会反复消费同一 token，普通 scaling law 因而不再只由总 token 数决定。Masked-input"
        " regularization 把重复样本的一部分输入随机遮蔽，以降低记忆化并改变 compute/data 最优点；证据只覆盖作者固定"
        " architecture、optimizer、至多 1.4B 参数和 400M unique tokens，不能外推为任意重复率下的通用最优策略。"
    ),
    "SF-2026-ARXIV-2606-07881": (
        "异步 Pipeline Parallel 允许相邻 stage 在有界 weight inconsistency 下继续推进，以减少同步 bubble；runtime 必须"
        "记录每个 microbatch 读取的 weight version，并用 staleness bound 决定接受、等待或回退同步 schedule。它用更复杂的"
        "版本状态和收敛风险换吞吐，不能把局部 bubble 降低外推成端到端训练收益。"
    ),
    "SF-2026-ARXIV-2606-22804": (
        "长视频理解可把边缘侧压缩记忆与云侧高成本推理分开：边缘持有连续 observation summary，云侧只消费带版本的"
        "摘要与关键片段。压缩降低上传和 Context 成本，却可能丢失 action-relevant transition；不确定或摘要失效时必须"
        "回取原始观测，不能把传输节省当作 world-state fidelity。"
    ),
    "SF-2026-ARXIV-2606-22966": (
        "Imagine-then-Act 把短期 latent trajectory 置于 action 之前，因此 imagined state 也成为可攻击输入。world model"
        "只能提出预测，controller 必须把预测身份、扰动边界和真实 observation reconciliation 分开；想象一致但实机状态"
        "冲突时，以真实观测回滚，不能授予 imagined rollout 执行权。"
    ),
    "SF-2026-ARXIV-2606-28385": (
        "机器人 world-model 评估不能只比较视频感知质量；结构化 evaluator 应分别检查物体、接触、动作阶段和因果 transition，"
        "并保留逐项证据。VLM evaluator 提高诊断粒度，却仍可能继承视觉与语言偏差；高风险结论必须回到 simulator state、"
        "真实传感器或人工标注。"
    ),
    "SF-2026-ARXIV-2607-10599": (
        "多模态融合应分开任务贡献与 observation reliability：贡献 router 用 leave-one-out task degradation 学习某模态是否"
        "有用，独立 uncertainty head 估计逐模态 log variance，再以 inverse-variance 权重校准 fusion gate。它避免把“有用”"
        "误写成“当前样本可靠”，代价是额外反事实监督与校准漂移。"
    ),
    "SF-2026-ARXIV-2607-27782": (
        "长时控制可用通用 reward model 估计平滑 progress，再以 progress delta 与 outcome sign 标记 action chunks，并从"
        "相邻正向轨迹簇寻找局部 correction。它把恢复从整段重规划缩小到局部候选，却受 reward calibration、聚类覆盖和"
        "unsupported failure 影响；没有可靠邻域时必须抑制自动 correction。"
    ),
    "SF-2026-ARXIV-2607-13429": (
        "VLA fine-tuning 可以把 action learning、冻结 teacher 的 representation anchoring，以及同一 observation 下的"
        "language-action alignment 分开优化，从而避免在保留语义先验和学习控制之间二选一。多目标权重失衡仍会抑制动作"
        "适应或保留无关语义，因此必须用 matched control 与 closed-loop outcome 验收。"
    ),
    "SF-2026-ARXIV-2607-14695": (
        "VLA serving 从同步 stop-think-act 演进到异步 observation/action streams 后，controller 必须给 observation、plan 与"
        "action 标注 generation 和 freshness budget。异步可降低等待，却会执行过期意图；freshness 越界时缩短 action chunk、"
        "重规划或回退同步控制。"
    ),
    "SF-2026-ARXIV-2607-14852": (
        "当一次性任务适配无法同时兼顾快速跟随与长期稳定时，可把在线更新拆成快、慢两个时间尺度，并用有界随机回放"
        "约束遗忘；代价是新增适配状态、回放预算与失稳检测责任，旧的静态策略在任务分布稳定时仍更简单可靠。"
    ),
    "SF-2026-ARXIV-2606-22875": (
        "联邦生成模型的 ownership 证据不能只保存最终 watermark 命中；Registry 应把 watermark revision、artifact hash、"
        "client identity、训练/聚合 lineage 与泄露追踪结果绑定。它提高归责能力，却不自动证明法律所有权，也不能让"
        "watermark 检测覆盖未观测的模型变换。"
    ),
    "SF-2026-ARXIV-2606-23546": (
        "训练能耗不能只按参数量或 GPU-hours 估算；roofline 风格模型应把 model size、parallelism、hardware operating point、"
        "利用率与 wall-clock 联合到同一 measurement contract，并与质量边界一起报告。解析模型适合做规划 proxy，真实发布"
        "仍需设备功耗与端到端测量校准。"
    ),
    "SF-2026-ARXIV-2606-22906": (
        "大型代码库的 Context 恢复不应把零散命中直接塞进 Prompt；系统先重建与任务相关的跨文件 path，再对 path 做压缩、"
        "加载和有效期管理。持久 workspace 保存恢复结果，Context 只投影当前需要的部分；path 置信不足时回退更宽检索或"
        "局部代码探索。"
    ),
    "SF-DELIBERATION-EVIDENCE-ATTRITION": (
        "多 Agent deliberation 应被视为 evidence-flow：原子事实最初分散在不同 agent，讨论过程可能传播、合并，也可能"
        "让事实消失。验收不能只看最终共识，而要比较初始 evidence、消息传递和终局保留率；共享更多上下文会增加成本与"
        "同质化，事实缺失时应回到原始证据或独立 verifier。"
    ),
    "SF-2026-ARXIV-2607-19957": (
        "跨请求 cache reuse 不能只凭文本和位置命中；还要验证 causal context provenance、tenant、policy 与状态 revision，"
        "兼容时才允许共享，否则执行隔离重算。更严格身份会降低命中率，却避免把另一个安全域或因果条件下的状态当成"
        "等价前缀。"
    ),
    "SF-2026-VPP": (
        "递增前缀 workload 使后续请求复用更长历史、各 stage 成本持续变化；Prefill runtime 因而需要在已完成 prefix identity"
        "不变的前提下重排 virtual stages。它用 schedule state 和迁移成本换 bubble 降低；重排收益不足或状态不兼容时回退"
        "固定 stage。"
    ),
    "SF-2026-ARXIV-2606-16310": (
        "MLA 的 post-projection QK RMSNorm 可拆为可吸收到权重的静态部分与逐 token/group 动态标量，从而保留 latent-KV"
        " decode path。该变换减少额外状态，却要求数值等价、RoPE 与量化路径共同验证；不满足时继续显式执行 normalization。"
    ),
    "SF-2026-ARXIV-2606-27732": (
        "Diffusion-LM 可用 asymmetric bidirectional sidecar 提供受控右上下文，同时让主干保留可缓存的单向状态。它以"
        "额外 sidecar 参数和融合开销换 parallel correction；若右上下文收益抵不过 cache invalidation 和迭代成本，仍回到"
        "纯 AR 或无缓存的双向分支。"
    ),
    "SF-2026-ARXIV-2608-04074": (
        "KV 压缩可由 attention-preserving transform 与 vector quantization 共同决定位宽，使误差目标从逐元素距离转向"
        "query 实际读取方式。2-bit 结果只覆盖作者给定的 Llama/Qwen/GPT-OSS、A100/H100 与 kernel；joint K/V、生产并发"
        "和未覆盖模型仍需独立验收。"
    ),
    "SF-2026-ARXIV-2606-04929": (
        "多阶段 post-training 的攻击面不止一份数据集：不同攻击者可以分别污染 SFT 与 preference data，checkpoint 又把"
        "隐藏状态传给下一阶段。dataset owner 因此要按阶段保存 provenance，pipeline orchestrator 负责晋级和跨阶段"
        "双验收；单阶段 clean test 不能排除协作 poison。"
    ),
    "SF-2026-ARXIV-2606-25353": (
        "Prefill 可把 weight execution 与 attention state 分成独立放置路径，使权重吞吐和 KV/attention locality 分别优化。"
        "解耦增加跨路径同步与 layout compatibility；收益不足或 state identity 不一致时回退共置执行。"
    ),
    "SF-2026-ARXIV-2606-25426": (
        "三层 cache blocking 与 weight pre-packing 把 Prefill 的数据复用显式映射到目标 cache hierarchy。它以 shape-specialized"
        " packing 和额外 artifact 换内存效率；模型形状、硬件或 precision 变化后必须失效重建，并保留通用 kernel fallback。"
    ),
    "SF-2026-ARXIV-2606-25838": (
        "后端路由器可以依据请求级 confidence 在快速和高质量路径之间选择，但 confidence 只拥有 route proposal 权。阈值需按"
        " workload 校准，并记录 fallback 与 outcome；漂移、低置信或高风险请求回退 canonical backend，不能把 router 自评分"
        "当成正确性。"
    ),
    "SF-2026-ARXIV-2606-25467": (
        "在线编排不能把请求与资源需求拆成两个独立队列；orchestrator 应共同维护请求—资源耦合、admission、降级与 SLO slack。"
        "预测误差会造成错误拒绝或过载，因此 hard cap、aging 和保守 fallback 仍需独立存在。"
    ),
    "SF-2026-ARXIV-2606-26383": (
        "性能监控可用 speed-of-light model 将硬件峰值、数据移动和 workload 参数分解成可校准上界，再用 observed gap 定位"
        "瓶颈。上界是诊断基线，不是生产承诺；模型参数或运行条件未披露、校准失效时回到直接 profile 与端到端 SLO。"
    ),
}


def clean_delta(family: str, delta: str) -> str:
    if family in DELTA_OVERRIDES:
        return DELTA_OVERRIDES[family]
    text = " ".join(delta.split())
    text = re.sub(r"^新增证据边界：", "", text)
    text = re.sub(r"^当前书稿 diff 已把以下长期机制写入该 owner：", "", text)
    text = re.sub(r"^`[^`]+`\s*路由到\s*`[^`]+`：", "", text)
    text = re.sub(r"^`[^`]+`\s*所定义的源特定机制用于", "", text)
    text = re.sub(r"\s*该 delta 已进入\s*`[^`]+`，正文保留旧方案成立条件、约束变化、代价与下一重压力。?", "", text)
    text = re.sub(r"\s*相邻章节对读：.*$", "", text)
    text = text.strip()
    if not text.endswith(("。", ".", "！", "？")):
        text += "。"
    return text


def insert_repairs(chapter_text: str, rows: list[tuple[str, str]]) -> str:
    if not rows:
        return chapter_text

    # Rebuild the generated branch section as one coherent block. Earlier
    # incremental runs could leave several identical headings in one chapter;
    # preserve the bindings while avoiding a sequence of repair appendices.
    for family, prose in rows:
        pattern = re.compile(
            rf"<!-- semantic-body-binding:{re.escape(family)}:start -->\n.*?\n"
            rf"<!-- semantic-body-binding:{re.escape(family)}:end -->",
            re.S,
        )
        chapter_text = pattern.sub("", chapter_text)
    chapter_text = chapter_text.replace(
        LEGACY_CONDITIONAL_BRANCH_HEADING, CONDITIONAL_BRANCH_HEADING
    ).replace(LEGACY_CONDITIONAL_BRANCH_INTRO, CONDITIONAL_BRANCH_INTRO)
    generated_intro = re.compile(
        rf"{re.escape(CONDITIONAL_BRANCH_HEADING)}\n\n{re.escape(CONDITIONAL_BRANCH_INTRO)}\n*"
    )
    chapter_text = generated_intro.sub("", chapter_text)
    chapter_text = re.sub(r"\n{3,}", "\n\n", chapter_text)

    paragraphs = [
        CONDITIONAL_BRANCH_HEADING,
        "",
        CONDITIONAL_BRANCH_INTRO,
    ]
    for family, prose in rows:
        paragraphs.extend(
            [
                "",
                f"<!-- semantic-body-binding:{family}:start -->",
                prose,
                f"<!-- semantic-body-binding:{family}:end -->",
            ]
        )
    block = "\n".join(paragraphs) + "\n\n"
    anchor = next(
        (
            candidate
            for candidate in (
                "## 本章在知识树中的位置",
                "## 从机制演进到系统设计",
                "## 集成后的机制主线",
                "## 自检问题",
                "## 面试与自检问题",
            )
            if candidate in chapter_text
        ),
        None,
    )
    if anchor is None:
        raise ValueError("chapter lacks a supported closeout anchor")
    return chapter_text.replace(anchor, block + anchor, 1)


def plan(root: Path, ledger: Path) -> dict[str, list[tuple[str, str]]]:
    with ledger.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    prepared = []
    corpus_items = []
    for row in rows:
        date = row["report_date"]
        report = root / "papers" / "2026" / date[5:7] / date[8:] / "README.md"
        delta = extract_delta(report, row["source_family"])
        chapter_text = (root / row["owner_path"]).read_text(encoding="utf-8")
        prepared.append((row, delta, chapter_text))
        corpus_items.append((delta, chapter_text))
    frequency, document_count = corpus_document_frequency(corpus_items)
    repairs: dict[str, list[tuple[str, str]]] = defaultdict(list)
    for row, delta, chapter_text in prepared:
        family = row["source_family"]
        score, heading, _ = best_body_proposition(delta, chapter_text, frequency, document_count)
        already_bound = f"semantic-body-binding:{family}:start" in chapter_text
        if score < MIN_PERSISTED_PROPOSITION_SCORE or not heading or family in FORCED_REPAIR or already_bound:
            repairs[row["owner_path"]].append((family, clean_delta(family, delta)))
    return repairs


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument(
        "--ledger",
        type=Path,
        default=Path("papers/2026/_sources/books-integration-audit-2026-06-08/integration-reconciliation.tsv"),
    )
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve()
    ledger = args.ledger if args.ledger.is_absolute() else root / args.ledger
    repairs = plan(root, ledger)
    changed = []
    family_count = 0
    for relative, rows in sorted(repairs.items()):
        path = root / relative
        before = path.read_text(encoding="utf-8")
        after = insert_repairs(before, rows)
        if after != before:
            changed.append(relative)
            family_count += sum(
                1 for family, _ in rows if f"semantic-body-binding:{family}:start" not in before
            )
            if args.write:
                path.write_text(after, encoding="utf-8")
    print(("updated" if args.write else "would update") + f": {len(changed)} chapters, {family_count} families")
    for relative in changed:
        print(relative)


if __name__ == "__main__":
    main()
