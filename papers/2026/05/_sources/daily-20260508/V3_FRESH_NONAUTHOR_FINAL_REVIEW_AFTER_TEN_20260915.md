# 2026-05-08 V3 fresh non-author final review after ten-item repair

## Verdict

**FAIL — keep `Ongoing`; `final_independent_signoff = false`.**

本轮是未参与十项返修和 root Books 写入的 fresh-context 复核。没有扩展日期、来源或 canonical `619` raw identity，
也没有修改 Books。机械账、当前 151 项 Evidence 与既有 Books 分流可以保留；失败只来自下面的 contribution-gate
false negative，不推倒已通过范围。

## Mechanical and retained-range checks

- canonical 守恒：`619 = 151 retained + 468 pre-denominator closure`；无重复 identity。
- Evidence：151/151 complete，`109 deep + 42 standard`，`Review Pending = 0`。
- Books：`81 Integrate — Applied + 70 No Change — Existing Coverage = 151`。
- 对十个 reopened family 逐项检查 exact-v1 摘要、Evidence 边界、Score、Stable Node 与 disposition；未发现需要返工的
  retained record。
- 另从 Deep/Standard 与 Applied/No Change 分层抽检现有 retained records；问题、机制、evaluation contract、non-proof、
  trade-off 和 fallback 均能支持当前处置。
- `2605.05709`、`2605.05602`、`2605.05676`、`2605.05781`、`2605.06507`、`2605.06643` 六个 root marker
  均唯一、位于各章 `Review notes` 前，owner 与正文语义充分；无需修改 Books。

## Bounded risk-stratified closure challenge

本轮固定检查 24 个 closure：完整复核作者声称已挑战的 11 个 sibling，再从 model/training、multimodal、evaluation/security、
Agent/system 四类高风险 closure 中追加 13 个题摘样本。判断只使用 canonical identity、完整标题与完整摘要；没有为已明确的
准入判断展开全文，也没有把抽检写成 468 项全量验证。

其中 9 项仍可在分母前关闭：`2605.05758`、`2605.05914`、`2605.06318`、`2605.06667`、`2605.05856`、
`2605.05861`、`2605.06052`、`2605.06480`、`2605.06628`。它们当前只提供领域数据集、早期/局部实现或尚不足以改变
本项目长期机制与选择边界的结果。

以下 15 项不能继续沿用“只闭合论文自身任务/模型/数据或局部实现边界”的统一排除理由；完整摘要已经给出可定位的机制、
反证或 evaluation-contract 增量：

| arXiv | 摘要已支持的具体增量 | 建议 owner |
| --- | --- | --- |
| `2605.05662` | jailbreak robustness、文化敏感度和 generation failure 必须分轴；composite safety score 会掩盖相反变化。 | `PLATFORM-EVALUATION-SYSTEM` |
| `2605.05668` | residual update 的几何/熵分析区分 attention 的 subspace reconfiguration 与 FFN expansion，并报告 learned attention 可被噪声替代的反证。 | `MULTIMODAL-REPRESENTATION` |
| `2605.05742` | 线性 logistic regression 已出现 weak-to-strong generalization，且不要求 student/teacher capacity mismatch，直接挑战主流机制解释。 | `TRAIN-RLHF` |
| `2605.06070` | 将 binary preference 改成由 arena capability distribution 推断的连续 offline reward，改变 diffusion preference optimization 的反馈粒度与 reward-model 依赖。 | `TRAIN-RLHF` |
| `2605.06170` | 动态生成 fresh prompt、difficulty-aware sampling 与 Bayesian online aggregation，直接改变 benchmark contamination 和 late-entry ranking 的评价合同。 | `PLATFORM-EVALUATION-SYSTEM` |
| `2605.06201` | 在没有 ground-truth annotation 时以 sufficient/necessary logical consistency 测量 MLLM，并揭示 accuracy 与 consistency 分离。 | `PLATFORM-EVALUATION-SYSTEM` |
| `2605.06509` | 长视频 attention-window 扩展造成 spectral concentration；低秩全局引导与高秩局部重建给出 temporal consistency/detail 的新取舍机制。 | `MULTIMODAL-GENERATIVE-PARADIGMS` |
| `2605.05714` | 将 appearance-entangled VLA 表示改为 object-hand-task relational primitives、task graph 与 relation-conditioned action bottleneck，改变 embodied action representation。 | `MULTIMODAL-EMBODIED-VLA` |
| `2605.05741` | layer-wise confidence trajectory 提供 inference effort sensor，并报告普通 SFT 会降低该 effort、同时损害 in-domain performance 的机制性副作用。 | `PLATFORM-EVALUATION-SYSTEM` |
| `2605.05851` | hypothesis evaluation 与 generation 分离，且局部 Bayesian-like posterior 不外推到未观察区域，修正“能评估即能生成/泛化”的能力判断。 | `WORLDVIEW-LLM-INTELLIGENCE` |
| `2605.06165` | 先生成 final answer、再生成 justification 的 factorization 把 answer latency 与训练监督分开，并在多模型/多 benchmark 上给出受限证据。 | `MODEL-SAMPLING`（相邻 `TRAIN-SFT`） |
| `2605.06183` | PAGE 暴露 adapter gradient energy 集中于单个浅层 FFN down-projection；单点 DomLoRA 改变 adapter placement 的默认设计。 | `TRAIN-LORA` |
| `2605.06324` | 把公开 audit metric 当作可被操纵的 security object，并给出 semantic-envelope repair 与带 annotation/protocol error 的 certificate。 | `PLATFORM-EVALUATION-SYSTEM` |
| `2605.06342` | 将 activation steering 的 utility loss 定位为 query-key attention rerouting，并以 key-orthogonal constraint 保留 focus-token attention。 | `MODEL-SELF-ATTENTION` |
| `2605.06529` | scalar reward 可在 partial observability 下获得近似 outcome 却形成错误 trace；distributional trace prior + KL repair 改变 Agent RL 的验收与优化对象。 | `TRAIN-RLHF`（相邻 `PLATFORM-EVALUATION-SYSTEM`） |

## Exact bounded repair

只重开上述 15 个 family：完成 exact-v1/withdrawal、Score V3、相应 Evidence 深度、唯一 Stable Node、目标及相邻章节对读与
Books Decision。当前 151 项 Evidence、81 个 Applied、70 个 No Change 以及本轮已通过的六个 Books marker 不得重做。
作者上一轮“11 个 sibling 无新增 false negative”的结论不能作为独立 Gate；新 reviewer 在 11 个中已确认 7 个漏收。

15 项返修完成后，另由未参与返修者复核这 15 项和一个新的、规模受限的同错误理由 challenge；在此之前 README 保持
`Ongoing`，不得登记 `Complete`。

