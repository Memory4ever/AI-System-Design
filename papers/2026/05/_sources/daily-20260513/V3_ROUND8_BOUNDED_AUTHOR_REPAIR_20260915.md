# 2026-05-13 V3 Round 8 限界作者返修

## 范围

本轮只重开独立复核确认的 6 个 false negative：

- `2605.10981`
- `2605.11059`
- `2605.11181`
- `2605.11235`
- `2605.11290`
- `2605.11311`

未扩窗口、未重放来源、未重扫 838 个 identity，也未触碰 191 项 revision/non-owner-route isolation。Round 7 已通过 fresh non-author 写后复核的 83 项 Books 写回保持不变，不重复追加。

## 返修结果

| Source Family | V3 | Review | Stable owner | Books Decision |
| --- | ---: | --- | --- | --- |
| `SF-2026-ARXIV-2605-10981` | 2+1+2=5 | Deep exact-v1（Books Gate） | `TRAIN-DPO` | Integrate；root pending |
| `SF-2026-ARXIV-2605-11059` | 1+2+2=5 | Standard exact-v1 | `TRAIN-PRETRAINING` | No Change — Existing Coverage |
| `SF-2026-ARXIV-2605-11181` | 3+2+3=8 | Forced deep correction | `TRAIN-PRETRAINING` | Integrate；root pending |
| `SF-2026-ARXIV-2605-11235` | 3+2+3=8 | Deep exact-v1 | `TRAIN-GRPO` | Integrate；root pending |
| `SF-2026-ARXIV-2605-11290` | 3+2+3=8 | Deep exact-v1 | `TRAIN-SFT` | Integrate；root pending |
| `SF-2026-ARXIV-2605-11311` | 3+2+3=8 | Deep exact-v1 | `MULTIMODAL-GENERATIVE-PARADIGMS` | Integrate；root pending |

六个 exact-v1 arXiv abstract/HTML 均可访问；截至 2026-09-15 未见官方 withdrawal banner。论文提供的代码链接只作补充，未把未绑定 immutable commit 的仓库当作 exact-v1 实现证明。

## 逐项命题结论

### 2605.10981 — ξ-DPO

SimPO 的 `beta` 不只表达 preference scale，也通过 sigmoid saturation 隐式过滤 high-gap samples；`gamma` 的意义依赖数据集 reward-gap 结构。ξ-DPO 将目标改写为到有界 ratio reward margin 的距离，并用初始 gap quantile 选择 `xi`。这比 Ch34 现有“preference scale 与 optimization scale 解耦”多出 sample-filtering、dataset-gap dependence 和 bounded target 三个命题，需要 root 将其整合到 `TRAIN-DPO`。Appendix A 的 late-stage target-likelihood collapse 保留为 failure boundary。

### 2605.11059 — AdamW Transformer uniform scaling

定理只覆盖 unmasked attention-only、有限训练时间和特定初始化/缩放条件，不证明现实 causal decoder 或 schedule transfer。Ch28 已有命题明确区分数学 scaling limit 与实际训练设计，并覆盖 forward/update scale 以及 weight-decay coupling，因此判定 `No Change — Existing Coverage`，无需 Books 写入。

### 2605.11181 — Muon mechanism correction

Freon 的 quasi-norm operating point、随机 spectrum 的 Kaon 以及 alignment/descent-potential 分解，反驳“精确 LMO 或理想全局几何是所测收益必要原因”。该证据只限 GPT-2/random-feature 范围，不能推出 Kaon 普适或所有矩阵 optimizer 等价；但它足以纠正 Ch28 可能造成的精确几何归因。root 写回应保留 Muon/AdamW baseline，并将机制表述改为可验证的 spectrum suppression、local alignment、descent potential 与 step-size matching。

### 2605.11235 — METIS

METIS 把 curriculum proposal sensor 内化到 policy，通过 recent prompt–variance examples 预测 informativeness，并联合优化 self-judgment reward。去掉 ICL evidence 后的高 parse-failure 是关键反证：policy judgment 不能继承 outcome authority。root 应把这一条件分支接到 Ch33 已有 reward-variance curriculum 命题，并保留 external verifier、random coverage 和 static/external selector fallback。

### 2605.11290 — ReAD

固定 token budget 下 capability 之间存在 saturation、positive transfer 与 harmful spillover；contextual bandit 按 task requirement、student probes、remaining budget 和 recent allocation 重分配 supervision。Ch29 尚未承载 capability-state-aware distillation budget。root 应将其写入 `TRAIN-SFT`，同时保留 taxonomy/probe calibration、delayed attribution 和 safety/privacy inheritance 边界。

### 2605.11311 — Couple to Control

保持每个 initial noise marginal 为标准 Gaussian，并不要求 batch 内 samples 独立；repulsive coupling 可将 gallery diversity 变成 joint-distribution control。Ch24 已把 source/coupling/schedule 作为单路径 generation artifact，但未覆盖固定 marginal、改变 batch joint contract。root 应增加该分支，并保留 independent seeds 在单图、failure isolation 与强复现约束下的适用性。

## 作者 Gate

- Candidate Denominator：`163 retained + 484 closure + 191 isolation = 838`。
- 6/6 完成 exact-v1 审阅、V3 score、Stable owner 与逐命题 Books comparison。
- 1 项 `No Change — Existing Coverage`。
- 5 项进入 root 串行 Books 队列；本作者未修改共享 Books。
- 当日保持 `Ongoing`，不得由本作者自签 Complete。
- 下一步：root 应用 5 项写回，再由不同的 fresh non-author reviewer 完成 post-write semantic audit。

## 限界反证检查

本轮只挑战这 6 项，不重开其余 484 个 closure。

- **False-positive challenge：** 逐项尝试用“只是局部 optimizer/objective、只是理论、只是 benchmark、只是 modality-local”关闭。`2605.11059` 虽仍值得保留为理论边界，但 Books 命题确已覆盖，因此落为 No Change；其余五项分别新增 preference sample-filtering、optimizer 机制纠错、curriculum owner、自适应 distillation budget 与 batch joint-generation contract，不能退回 denominator 前。
- **False-negative challenge：** 检查六项中是否仍有因主题相近而未表达的独立增量。题摘与 exact-v1 对读后，没有发现第七个机制；五项 queue 覆盖了本轮全部未承载命题，`2605.11059` 的假设与非证明边界已在 Evidence 中保留。
- **重复写入 challenge：** Books 全文未出现这六个 exact Source Family binding；五项为新队列，不与 Round 7 的 83 项重复。`2605.11059` 不进入 queue。
- **Owner challenge：** ROADMAP 中五个 Stable Node 均可解析；每项只分配一个 canonical owner。跨章关系只在 queue 中作为 handoff，不创建第二 owner。
- **Post-write semantic boundary：** 本作者只完成 Report/ledger/evidence/comparison/queue 的写后一致性审计；由于共享 Books 尚未写入，不能把本检查表述为 Books post-write review，也不能签 Daily Complete。
