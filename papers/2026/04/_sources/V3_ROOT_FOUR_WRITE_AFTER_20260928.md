# 4 月四项 Books 实写的非作者写后复核

检查日：2026-09-28。仅验以下四项实际正文及邻接、源事实边界和 `git diff --check`；不是 04/22 或 04/24 的整日 Gate，也不是实验复现。报告作者分别由 `apr02`（04/22）和 `apr01`（04/24）承担，root 是本次非作者复核者。

| 日期与 Source Family | 原始证据与实际 owner | 写后结论 |
| --- | --- | --- |
| 04/24 `SF-2026-ARXIV-2604-21549` | [官方 exact-v1 PDF](https://arxiv.org/pdf/2604.21549v1) pp. 3–9；`PLATFORM-EVALUATION-SYSTEM` Ch66:1770–1772，章末 Review notes。 | **PASS**。从总体残差抵消、目标重加权失效到支持内条件校准，与原有总体估计和下文 Risk–Coverage 衔接。正文保留可观测分组、重叠、稳定标签条件与有限标注前提；未把个体标签或 AUC 当作目标总体无偏证明。 |
| 04/22 `SF-2026-ARXIV-2604-18933` | [官方 exact-v1 HTML](https://arxiv.org/html/2604.18933v1) §III-B/§IV/§VIII；`MULTIMODAL-EMBODIED-VLA` Ch26:391–393，章末 Review notes。 | **PASS**。两套预备 policy、独立校准、门冻结后重训最终 policy 的状态分工与前文具身记忆自然衔接。误差比只作门标签 proxy，不证明最终 policy 的反事实必要性或物理安全。 |
| 04/22 `SF-2026-ARXIV-2604-18963` | [官方 exact-v1 HTML](https://arxiv.org/html/2604.18963v1) §3–6；`TRAIN-SFT` Ch29:218–220，章末 Review notes。 | **PASS**。固定 teacher 的蒸馏判断向可校准 teacher 分支演进，任务效用、KL 和兼容性目标分账。跨 tokenizer 序列评分未当逐 token 同义或通用 IP 防护。 |
| 04/22 `SF-2026-ARXIV-2604-19033` | [官方 exact-v1 HTML](https://arxiv.org/html/2604.19033v1) §3–6/§7；`TRAIN-PRETRAINING` Ch28:452–454，章末 Review notes。 | **PASS**。将已选更新方向上的局部输出步长与批量残差伪逆分开，保留 trace、方向偏差和线性近似限制；未外推 LLM pretraining、hard KL cap 或无偏 policy gradient。 |

四个 owner 段落均实际存在，Review notes 仍在机制正文之后，未发现本批需修正的事实外推。对应日报的整合计数与书稿证据注释由日期 owner 同步；本记录不代替其来源覆盖、候选分母、余项审阅、最终独立日级验收。
