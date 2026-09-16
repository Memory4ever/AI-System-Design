#!/usr/bin/env python3
"""Apply six root-owned Books increments from the 2026-05-08 bounded repair."""

from __future__ import annotations

import json
import re
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
QUEUE = HERE / "ROOT_BOOKS_WRITEBACK_QUEUE_BOUNDED_REPAIR_20260915.json"

CONTENT = {
    "2605.05278": (
        "Routing Information 是选择性代理，不是生产阈值",
        "把 router 看成从输入到 expert identity 的随机信道，可以把选择信息量与 expert bank 可达到的 distortion 分开：路由携带的信息越少，控制、索引和潜在通信越容易压缩，但可区分的 expert path 也越少，任务损失下界随之收紧。这个视角补充了 load balance，却不能替代真实 token、capacity、placement 与 collective 测量；information estimator 只提供 workload-specific 选择性信号，scheduler 仍拥有执行决策权。\n\n该分解用可分析代理换取额外分布估计，并会在 expert bank 非有限、连续路由或分布漂移时失真。估计不稳定或系统不满足假设时，应回退现有 load、quality、capacity 和通信合同。`arXiv:2605.05278v1` 只在有限预训练 CNN expert bank、MNIST 与离散选择规则中验证，理论界也较松；它不证明分布式 LLM MoE 存在通用信息阈值。",
    ),
    "2605.05485": (
        "重复 Trace 可以离线编译，但 Solver 仍是受限 Artifact",
        "重复调用 LLM 处理结构稳定、具有精确 verifier 的任务，在线成本高且每次都重新探索。可把多条 reasoning trace 离线归纳为版本化 symbolic solver，在线先运行 solver，未覆盖或验证失败时再调用 LLM；这把部分一次性推理成本转成可复用构建成本。solver 只拥有候选求解权，workflow state、effect commit 与最终正确性仍分别由编排器和 verifier 持有。\n\n编译分支要求保存 DSL、训练 traces、induction 版本、覆盖域和 verifier，并承担 run-to-run 波动、过拟合及错误程序复用风险。任务开放、输入越界或 verifier 不充分时，应回退动态 planning/LLM。`arXiv:2605.05485v1` 只覆盖两个受约束 DSL，且包含 best-run selection；它不证明开放任务可被通用编译，也不证明生成 solver 天然正确。",
    ),
    "2605.05646": (
        "统一 Visual Tokenizer 也可以拆分表示责任",
        "让同一离散路径同时承担 topology、semantic value 与 residual texture，接口最简单，却会让重建细节和抽象语义竞争表示容量与梯度。一个分层责任分支把结构写入 attention relation，把语义写入 value，把高频纹理由独立 residual decoder 恢复；共享 tokenizer 仍是统一 artifact，但其内部 state owner 不再被误认为单一 code。\n\n责任分解可能降低 reconstruction 与 abstraction 的梯度争用，却增加 teacher 依赖、额外 decoder、训练耦合和跨域迁移风险。分解不稳定、额外计算不合算或只需单向任务时，modality-specific encoder 或理解/生成双表示仍合理。`arXiv:2605.05646v1` 只支持作者在同 backbone、数据和 teacher 下的实验，不证明 Q/K–V 分工是唯一因果机制，也不覆盖音频、视频或生产 serving。",
    ),
    "2605.05702": (
        "Construction Artifact 可以派生 Partial Credit，但不能拥有真值",
        "合成多跳任务时，构造过程中的知识图谱 path 原本只是生成中间物；若将其版本化，它既可供 data admission 检查题目是否连通，也可让 reward owner 派生 waypoint partial credit。两条消费路径必须引用同一 construction revision，terminal verifier 继续拥有最终正确性，避免图谱路径同时扮演题目来源、奖励和真值而形成循环自证。\n\n共享 artifact 能密化稀疏 reward，却会把图谱缺口、外部 LLM 抽取错误和答案泄漏同时传播到数据与奖励。path 不可信、含目标泄漏或不能覆盖任务时，应回退 outcome-only reward、固定 curriculum 与独立 terminal verification。`arXiv:2605.05702v1` 只覆盖 Wikidata factoid multi-hop 和近似 waypoint/correctness，不证明开放搜索 Agent 普遍受益。",
    ),
    "2605.06124": (
        "Guidance 可以前移到 Prior，但误差会集中到初始状态",
        "标准 classifier-free guidance 在每个 velocity evaluation 都运行条件与无条件分支，语义清楚但网络求值翻倍。条件 prior 分支把 guidance control 前移到初始噪声分布的均值/方差，用小型 prior 完成一次 steering 后执行单 pass sampling；runtime 由此减少 forward count，却把条件逼近误差集中到 prior artifact、guidance scale 与 sampler identity。\n\n这种替代只在一阶近似和校准范围内接近标准 CFG，并新增 prior 漂移与初始偏差难以逐步修正的风险。guidance scale 越界或质量下降时，应回退 dual-pass CFG，两者可按 workload 共存。`arXiv:2605.06124v1` 的实验限于 MNIST、CIFAR、ImageNet 256、U-Net/DiT-B/2 与单 RTX4090；作者延迟不能外推生产并发或 tail SLO。",
    ),
    "2605.06207": (
        "Codebook Capacity 也可以随位置递增",
        "uniform codebook 让每个视觉 token 使用相同容量，编码、部署和兼容最简单；当序列按 coarse-to-fine 顺序增长时，累计容量可能在早期就跨过数据 uncertainty，后续位置难以继续形成层级。position-indexed schedule 先给早期 token 较小 codebook 表达粗语义，再逐步扩展后续容量承载细节；`position/order/N/K` 因而都进入 representation artifact identity，而不是只记录全局 bitrate。\n\n递增容量可延长层级形成区间，却增加多 codebook 治理、kernel/layout 与训练不均衡，也依赖稳定的顺序语义。序列没有 coarse-to-fine 结构、兼容优先或收益不足时，uniform codebook 仍更合适。`arXiv:2605.06207v1` 只在 ImageNet 256 与作者 tokenizer/AR 设置中验证；entropy-cliff 阈值依赖数据、长度与 codebook，不能外推语言或其他视觉表示。",
    ),
}

ANCHORS = {
    "2605.05278": ("从 Batch-relative Balance 到 Population Routing State", "before"),
    "2605.05485": ("稳定 Procedure 可以编译为 Skill，但 Workflow State 不能一起隐藏", "under"),
    "2605.05646": ("Rate、distortion 与下游容量必须联合选择", "before"),
    "2605.05702": ("Verifier-backed Synthetic Curriculum 需要双重权威", "under"),
    "2605.06124": ("Conditional Guidance 把 Diffusion 并行策略变成逐 Step 状态", "under"),
    "2605.06207": ("Rate、distortion 与下游容量必须联合选择", "under"),
}


def locate_heading(lines: list[str], anchor: str) -> int:
    idx = next((i for i, line in enumerate(lines) if anchor in line and line.lstrip().startswith("#")), None)
    if idx is None:
        raise SystemExit(f"anchor not found: {anchor}")
    return idx


def insert(text: str, anchor: str, mode: str, title: str, body: str, sf: str) -> str:
    if sf in text:
        return text
    lines = text.splitlines(keepends=True)
    idx = locate_heading(lines, anchor)
    level = len(lines[idx]) - len(lines[idx].lstrip("#"))
    if mode == "before":
        insertion = idx
        sublevel = level
    else:
        insertion = len(lines)
        for i in range(idx + 1, len(lines)):
            match = re.match(r"^(#+)\s", lines[i])
            if match and len(match.group(1)) <= level:
                insertion = i
                break
        sublevel = level + 1
    block = "\n" + "#" * sublevel + f" {title}\n\n{body}\n\n<!-- semantic-body-binding:{sf} -->\n\n"
    lines.insert(insertion, block)
    return "".join(lines)


queue = json.loads(QUEUE.read_text())
if len(queue["items"]) != 6:
    raise SystemExit("expected six queue items")
changed = 0
for item in queue["items"]:
    aid = item["arxiv_id"]
    title, body = CONTENT[aid]
    anchor, mode = ANCHORS[aid]
    path = ROOT / item["owner_path"]
    old = path.read_text()
    new = insert(old, anchor, mode, title, body, item["source_family_id"])
    if new != old:
        path.write_text(new)
        changed += 1
    item["root_status"] = "applied_current_worktree_pending_fresh_non_author_review"
    item["root_writeback_date"] = "2026-09-15"
queue["status"] = "root_writeback_complete_pending_fresh_non_author_review"
queue["root_applied_count"] = 6
QUEUE.write_text(json.dumps(queue, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({"changed": changed, "applied": 6, "status": queue["status"]}, ensure_ascii=False))
