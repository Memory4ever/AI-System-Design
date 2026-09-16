#!/usr/bin/env python3
"""Write the date-local Books queue and author checkpoint for 2026-05-07."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPORT = ROOT.parents[1] / "07" / "README.md"
PACKET = ROOT / "exact-v1-review-packet-v3-author-repair.json"
LEDGER = ROOT / "screening-ledger-v3-author-repair.json"

CLOSED_EVIDENCE = {
    "2605.04911": {
        "method": "跨数据集预训练的 tabular Transformer 复用结构先验，再以 dataset-specific decoder 和 query data 生成当前小样本表格数据。",
        "evaluation": "在 14 个真实表格数据集上比较生成质量、记忆/隐私代理指标和下游数据增强效果。",
        "limitations": "需要每数据集 decoder 与 query data；没有形式化 differential privacy 保证，也没有 LLM 数据管线或平台机制实验。",
    },
    "2605.04932": {
        "method": "对 frozen predictor 的动态 covariate shift 建模，以时间域不等式和 Jacobian-velocity bound 导出 drift-aligned tangent regularization。",
        "evaluation": "受控合成实验及 UCI Air Quality、Tetouan 冻结部署数据验证 directional gain/risk volatility。",
        "limitations": "依赖 domination、光滑性及低秩漂移假设；传统预测器实验不能直接证明 LLM release 或监控合同。",
    },
    "2605.04946": {
        "method": "把 training-time BatchNorm 写成依赖 mini-batch centroid 的 switching hyperplane 重排，并分析局部 CPA/ReLU affine-region refinement。",
        "evaluation": "小型 MLP/低维设置检验精确区域计数，高维部分使用局部几何代理。",
        "limitations": "只研究训练期 BatchNorm 与 piecewise-affine 网络；不是 Transformer 常用 LayerNorm/RMSNorm，也没有 LLM 规模证据。",
    },
    "2605.05084": {
        "method": "ORDERED 通过优化 batch 样本顺序降低 MMD/CORAL 域差异估计的随机方差。",
        "evaluation": "模拟实验和两个 DomainBed 图像分类域迁移 benchmark 比较估计方差与目标域准确率。",
        "limitations": "属于图像 UDA 的采样次序优化；没有 LLM workload、训练生命周期或跨系统 owner 的直接证据。",
    },
    "2605.05123": {
        "method": "维护离线训练的候选 policy pool，以 OPE 先验、在线回报预测和 UCB 在有限交互预算内选择、切换并微调策略。",
        "evaluation": "在通用 continuous-control offline-to-online RL 任务上比较预算使用、策略选择和在线改进。",
        "limitations": "没有 RLHF/RLVR、语言策略、生成式 reward contract 或 AI platform 控制面实验。",
    },
    "2605.05151": {
        "method": "在单层 PatchTST 的 post-GELU FFN activation 上训练 0.5x 至 4x dictionary 的 SAE，并做 dominant-latent causal intervention。",
        "evaluation": "八个时间序列预测 benchmark 比较深浅模型、dictionary expansion、inactive features 与干预后的 forecast 变化。",
        "limitations": "结论只覆盖时间序列模型的一个 FFN hook 与所测规模；不能否定 LLM 表征 superposition 或改写 Transformer 通用机制。",
    },
}

# 任何进入 Books 写回队列的候选都必须经过深入审阅；这与分数阈值无关。
BOOKS_DEEP_IDS = {
    "2605.04830",
    "2605.04913",
    "2605.04971",
    "2605.04984",
    "2605.05007",
    "2605.05138",
    "2605.05170",
    "2605.05176",
    "2605.05204",
}

queue = """# 2026-05-07 Books 写回队列

本队列只记录原 34 项剩余 exact-v1 批次中仍需 root 修改共享 Books 的事项。作者 lane 未修改 Books。原 35/35 legacy queue 已落地，不能用它代替本批复核；本批新增 **8 项新增/修订 + 1 项删除 = 9 项**。root 必须按日期顺序写回，并在每项后复核正文主线与相邻章节。

## 1. 2605.04830 — 新增生成期 critical-window 诊断

- **动作 / Owner：** 新增；`MULTIMODAL-GENERATIVE-PARADIGMS`，`books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md`。
- **旧命题：** 现有正文比较 AR、diffusion、iterative correction 的 factorization、state、cache 与 commit，但默认全程 conditioning/global communication 的计算角色一致。
- **最小增量：** 增加一条诊断分支：用 conditional/unconditional 与 global/approximately-local score gap，再用 windowed intervention 验证何时 conditioning 与 global denoising 真正 load-bearing；它用于调度/架构假设，不授予动态跳过的正确性。
- **证据边界：** exact-v1 只测 ImageNet DiT-XL 与 SD3-medium；截断 attention 不是严格 local denoiser；并发 critical windows 是经验观察，不是普适定理。
- **相邻衔接：** 前接 iterative correction 的可变状态；后交 Part V execution/scheduling，runtime 必须另验 quality、latency 与 commit。

## 2. 2605.04932 — 删除范围外来源的专属绑定

- **动作 / Owner：** 删除；`PLATFORM-EVALUATION-SYSTEM`，`books/part-06-ai-infrastructure/66-evaluation-system.md`。
- **旧命题：** “IID benchmark 不能直接外推 deployment drift”是成立的一般原则；其后 Jacobian-sensitive bound 两句及 `SF-JACOBIAN-...` marker 专属于该来源。
- **最小改动：** 保留 IID→shadow/canary 的长期原则，删除将传统 frozen predictor 的低秩 drift theorem 当作 LLM release 机制证据的专属两句与 source-family marker；不要影响紧随其后的 intervention side-effect 段。
- **证据边界：** exact-v1 是传统预测器、低秩动态 covariate shift 与强 domination/光滑性假设；没有 LLM workload、模型生命周期或平台 release gate 的直接实证。
- **相邻衔接：** 与前文 invariance、后文 intervention side-effect 保持连续；通用 drift 原则可由现有 evaluation contract 自身承担。

## 3. 2605.04956 — 补齐 Kernel 评价的四段失败分类

- **动作 / Owner：** 修订；纠正 owner 为 `PLATFORM-EVALUATION-SYSTEM`，`books/part-06-ai-infrastructure/66-evaluation-system.md`，而非执行引擎。
- **旧命题：** Ch66 已要求 shape/dtype/layout/alias/determinism 等语义门先于性能，但没有明确区分 compile、semantic correctness、hardware efficiency 与 portability。
- **最小增量：** 在现有 Kernel 评价段补四段 failure taxonomy，并说明 iterative repair 可能提高 compile/correctness 却降低 speed；性能只对通过同一语义门的 artifact 比较。
- **证据边界：** 176 tasks、15 categories、六 GPU 与五种方法均为作者 benchmark；microbenchmark speedup 不等于端到端模型收益，测试通过也不是形式证明。
- **相邻衔接：** Evaluation 拥有 workload/verdict；Ch49 只拥有 kernel/execution-plan 实现与 fallback，不重复 benchmark 正文。

## 4. 2605.04971 — 分离 Residual coherence 与非线性 symmetry breaking

- **动作 / Owner：** 新增；`MODEL-TRANSFORMER-LAYER`，`books/part-02-model/17-transformer-layer.md`。
- **旧命题：** Ch17 已分别解释 residual、normalization 与 nonlinearity，但没有把跨层方向连续性拆成 gradient coherence 与 rotational symmetry breaking 两个责任。
- **最小增量：** 增加受限机制说明：residual 提供跨层梯度相干，非 rotation-equivariant 的非线性打破等价方向；rotation-equivariant 反例说明“有非线性”本身不充分。
- **证据边界：** 因果证据主要来自 toy MLP 与 34M Transformer；大模型快照只展示相关几何，不证明训练动力学或普适层级定律。
- **相邻衔接：** 前接 attention/MLP/residual 的组合；后交 Decoder-only 堆叠，不把几何连续性写成能力来源。

## 5. 2605.05066 — 写入长上下文不可能三角

- **动作 / Owner：** 新增；`MODEL-LONG-CONTEXT`，`books/part-02-model/22-long-context.md`。
- **旧命题：** Ch22 已列 KV、固定递归状态、压缩与检索分支，但缺少统一说明为何三者不能同时获得长度无关计算、固定状态和随历史增长的 exact recall。
- **最小增量：** 用 OSP/有限精度信息容量给出设计边界：系统必须在 compute、state capacity 与 exact retrieval contract 中至少放松一项；随后把 attention、SSM/compression、external retrieval 写成条件分支而非胜负排名。
- **证据边界：** 经验只覆盖 d=64、2-layer synthetic associative recall；random KV 是 worst-case，常数、近似/分布化 recall 与结构化数据会改变 operating point。
- **相邻衔接：** 前接 MoE/long-context 的模型状态；后 handoff Ch42–45 的 prefill/decode/KV runtime 成本。

## 6. 2605.05138 — 增加可执行、可反证 World Hypothesis 分支

- **动作 / Owner：** 新增；`MULTIMODAL-WORLD-MODELS`，`books/part-03-multimodal-world-models/25-multimodal-world-models.md`。
- **旧命题：** Ch25 已覆盖 latent dynamics、imagined rollout 与 planning coupling，但可解释/可反证的 symbolic world state 较弱。
- **最小增量：** 加入 executable world hypothesis：由 action/observation history 构造程序化 transition model，先对历史 transition replay 验证，再用于 provisional rollout；真实环境继续拥有 commit authority。
- **证据边界：** ARC-AGI-3 25 个公开游戏、主要每局一次 fresh run、仅解出 7 个；固定 API/公开环境可能产生 harness prior，代码执行还需要 sandbox。
- **相邻衔接：** 前接 latent model 的可修订 state，后交 Ch26 physical-action loop 和 Agent planning；程序 prediction 不能替代真实 environment transition。

## 7. 2605.05176 — 补充 Attention-as-Featurizer 的构造性 ICL 路径

- **动作 / Owner：** 新增；`MODEL-SELF-ATTENTION`，`books/part-02-model/14-self-attention.md`。
- **旧命题：** Ch14 解释内容路由与加权聚合，但没有展示 nonlinear ICL 可如何分解为 attention feature construction 与后续在线求解。
- **最小增量：** 增加构造性理论分支：attention 生成 polynomial/spline feature，后续层完成 least-squares；强调这是存在性/误差界解释，不是对预训练 LLM 内部算法的观测结论。
- **证据边界：** 假设 polynomial/spline approximability、特定 sum-based heads 与合成 regression；三 seed 数值实验不支持通用 ICL 机制断言。
- **相邻衔接：** 前接 Q/K/V 聚合表达力，后交 Ch17 多层组合与非线性；不把 featurizer 机制塞入推理 runtime。

## 8. 2605.05189 — 容量必须绑定读取判据

- **动作 / Owner：** 新增；`MODEL-LONG-CONTEXT`，`books/part-02-model/22-long-context.md`。
- **旧命题：** Ch22 讨论记忆容量与召回，却容易把 d² 参数量误读为与读取 contract 无关的容量数字。
- **最小增量：** 区分 top-1 winner-take-all 的 extreme-value `n log n` 压力与 listwise/Tail-Average Margin 的候选集 contract；降低门槛来自改变 correctness 定义，不是免费精确容量。
- **证据边界：** 只对 linear memory、isotropic Gaussian associations 和论文准则成立；TAM 渐近依赖 leave-one-out/postulates，小-tail 回到 top-1 仍是 conjecture。
- **相邻衔接：** 紧接不可能三角中的 exact recall 定义，并 handoff retrieval/rerank 层说明 listwise 候选仍需后续 verifier。

## 9. 2605.05204 — 为少步 Diffusion 增加 On-policy Self-distillation 分支

- **动作 / Owner：** 新增；`TRAIN-SFT`，`books/part-04-training-system/29-sft.md`。
- **旧命题：** Ch29 已说明 teacher-forced SFT 的 distribution mismatch 与遗忘，但没有少步 diffusion 连续适配中 inference-step 能力被普通 SFT 损伤的分支。
- **最小增量：** 增加 student-owned few-step rollout + same-model privileged multimodal teacher：student 只读文本、teacher 读目标图像与 prompt，在 student trajectory 上蒸馏；保留 vanilla SFT 与重新 distill 的 fallback。
- **证据边界：** 作者设置约 4× FLOPs、2× iteration time；依赖 encoder/base model 的 in-context teacher 能力，teacher 在 multimodal condition 下失败即无有效监督；不外推所有 diffusion/LLM tuning。
- **相邻衔接：** Ch24 拥有生成范式与 step-distilled inference state，Ch29 只拥有 adaptation objective/data path，避免双写机制。

## 已有正文或仅报告（无需 root 写回）

- 已有 exact-v1 正文：2605.04901、2605.04913、2605.04984、2605.04992、2605.05007、2605.05090、2605.05170。
- 已有覆盖：2605.04808、2605.04897、2605.04920、2605.04972、2605.04995、2605.05003、2605.05058、2605.05185、2605.05191。
- 仅报告：2605.05026、2605.05103、2605.05115、2605.05134。
- scope recheck 后关闭：2605.04911、2605.04932、2605.04946、2605.05084、2605.05123、2605.05151；其中只有 2605.04932 已发现错误 Books 专属绑定，已列删除项。
"""

checkpoint = """# 2026-05-07 V3 作者侧完成 checkpoint

状态：**原 34 项剩余批次的作者侧证据与 Books comparison 已完成；报告仍进行中**。尚待 root 执行共享 Books 写回，并由新的非作者 reviewer 验收全日状态。不得把本 checkpoint 或机器校验当作 Daily Complete。

## 唯一账本

- 窗口：2026-05-06 09:00 至 2026-05-07 09:00 Asia/Shanghai。
- active screening ledger：**548 = 137 retained + 410 pre-denominator closure + 1 withdrawn**。
- active exact-v1 packet：**133 Source Review complete + 4 Disputed + 0 pending**。
- 原 143 候选中有 6 项经 exact-v1 scope recheck 关闭：2605.04911、2605.04932、2605.04946、2605.05084、2605.05123、2605.05151。已读证据和逐项理由保留，没有用降分或删除痕迹逃避审阅。
- 撤回 2605.04356 只保留最小排除身份。

## 保留争议

- 2605.04069：LAWS 未控制后缀/LayerNorm validity boundary。
- 2605.04243：credal interval 的诊断解释越过其 coverage 前提。
- 2605.04295：ACSE 叙述混淆两个条件概率。
- 2605.05029：证明外推、角度叙述与实验 grid 计数存在冲突。

四项均保持 `Disputed / 暂缓`，不进入 Books，不因其存在把普通 Source Review 写成 blocked。

## 作者侧结果

- 34 个旧 pending 的 exact-v1 HTML/PDF 均已取得并定点阅读核心方法、关键评价与直接限制；无材料请求。
- 本轮 34 项中，28 项保留候选完成 Evidence、评分校准和 Books comparison；6 项移入具体 pre-denominator closure。
- 评分收窄包括 2605.04971、2605.05003、2605.05115、2605.05191；没有把主题广或能类比多个章节当作 Reach/Delta。
- root 写回队列：**9 项**，含 8 项新增/修订与 1 项错误来源删除。作者未修改共享 Books、月索引或 LEARNING_STATE。
- 本 checkpoint 不重新认证 34 项批次之外的旧 Books disposition；非作者 reviewer 仍需把日报表中的既有处置与当前正文逐项对齐。

## 下一步

1. root 按 `BOOKS_WRITEBACK_QUEUE.md` 逐项串行写回，并核对正文前后衔接。
2. root 同步日报 Books 位置/Repository Changes，保持四项争议隔离。
3. 新的非作者 reviewer 检查来源日期、scope recheck、28 项 evidence boundary、三维评分、Books 实际落点及相邻章节。
4. reviewer 通过且 validator/link/diff/worktree 范围通过后，才可把日报状态改为完成。
"""

(ROOT / "BOOKS_WRITEBACK_QUEUE.md").write_text(queue)
(ROOT / "V3_RECERTIFICATION.md").write_text(checkpoint)

# 被移出候选分母不等于没有审阅：把 exact-v1 的方法、评价和直接限制
# 同时保留在证据包与身份账本，避免后续只剩一句 scope closure。
packet = json.loads(PACKET.read_text())
packet["status"] = "Remaining 34-item exact-v1 author batch complete; this batch's root writeback and new non-author review pending"
for item in packet.get("superseded_closed_items", []):
    evidence = CLOSED_EVIDENCE.get(item.get("arxiv_id"))
    if evidence:
        item["exact_v1_scope_review_evidence"] = evidence
PACKET.write_text(json.dumps(packet, ensure_ascii=False, indent=2) + "\n")

ledger = json.loads(LEDGER.read_text())
ledger["status"] = "Remaining 34-item author batch complete; root Books writeback and new non-author review pending"
for item in ledger.get("identities", []):
    evidence = CLOSED_EVIDENCE.get(item.get("arxiv_id"))
    if evidence:
        item["exact_v1_scope_review_evidence"] = evidence
LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n")

# 修复作者脚本早期生成的全角右括号链接，并同步当前真实交接状态。
report = REPORT.read_text()
report = report.replace(".md））", ".md)）")
report = report.replace(
    "当前工作分母为 **548 = 137 候选 + 410 关闭 + 1 撤回排除**，不是 143 项全文完成；新增项没有继承旧自动脚本的完成状态。",
    "当前工作分母为 **548 = 137 候选 + 410 关闭 + 1 撤回排除**；候选证据状态按本轮 exact-v1 审阅重算，不继承旧自动脚本的完成状态。",
)
report = report.replace(
    "Books 比较逐项完成，仍有 8 项新增/修订及 1 项错误来源删除需要 root 串行写回",
    "本轮 34 项中的 28 个保留候选已逐项完成 Books 比较，仍有 8 项新增/修订及 1 项错误来源删除需要 root 串行写回",
)
report = report.replace(
    "| SRC-ARXIV | 548身份；官方batch+DataCite初始+ID/version交叉 | 未完成 | 143候选；current OAI revision不等于owner gap |",
    "| SRC-ARXIV | 548身份；官方batch+DataCite初始+ID/version交叉 | 未完成 | 137候选；current OAI revision不等于owner gap |",
)
report = report.replace(
    "因此不能把当前状态写成“只等 reviewer”，更不能 Complete。",
    "因此当前只等待 root Books 写回与新的非作者 reviewer；两者完成前不能 Complete。",
)
report = report.replace(
    "作者整改目前真实范围为28项重开+44项高风险题摘扩查、3项误收反转、全部 retained 的评分校准；105项已重新整理可定位机制/评价/限制，4项争议，34项待审阅。",
    "作者整改真实范围为 28 项重开、44 项高风险题摘扩查、3 项误收反转，以及全部 retained 的评分校准；最终为 133 项 Source Review 完成、4 项争议、0 项待审。",
)
report = report.replace(
    "状态保持进行中，必须完成作者剩余工作后再交新的非作者复核。",
    "状态保持进行中，待 root Books 写回后再交新的非作者复核。",
)
report = report.replace(
    "本报告仍为“进行中”：只差 root Books 写回和新的非作者语义复核，不得把作者自检或 validator 当作最终通过。",
    "本报告仍为“进行中”：至少还需 root Books 写回和新的非作者语义复核；本轮队列只覆盖原 34 项剩余批次，不得把作者自检或 validator 当作整日最终通过。",
)
report = report.replace(
    "作者侧 exact-v1 证据与 Books comparison 已结束：**133 完成 / 4 争议 / 0 待审**；活跃分母 **137**。无材料受阻。下一步只执行 date-local 队列中的 8 项新增/修订与 1 项删除，再由未参与本轮写作的 reviewer 检查日期、准入、证据边界、评分、Books 实际落点与相邻衔接。完成前状态保持进行中。",
    "原 34 项剩余批次的 exact-v1 证据与 Books comparison 已结束；全日 Evidence 账面为 **133 完成 / 4 争议 / 0 待审**，活跃分母 **137**，无 exact-v1 材料受阻。本批先执行 date-local 队列中的 8 项新增/修订与 1 项删除；新的非作者 reviewer 还需核对全日既有 disposition 与实际 Books，完成前状态保持进行中。",
)
lines = []
for line in report.splitlines():
    if any(f"/{arxiv_id}v1)" in line for arxiv_id in BOOKS_DEEP_IDS):
        line = line.replace("| 标准完成 |", "| 深入完成 |")
    lines.append(line)
report = "\n".join(lines) + "\n"
REPORT.write_text(report)

print("wrote queue, checkpoint, closure evidence, and report handoff fixes")
