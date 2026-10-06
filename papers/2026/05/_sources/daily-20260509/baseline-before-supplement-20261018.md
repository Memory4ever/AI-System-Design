# Daily Research — 2026-05-09

**规范：** V3
**窗口：** 2026-05-08T09:00:00+08:00 ～ 2026-05-09T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-14T20:30:00+08:00

## 1. 结论

本窗没有 arXiv scheduled announcement batch；旧报告据此写成零候选是正确的局部事实，但它只检查了 arXiv，不能满足当前 Daily 合同。补查 13 个每日机构入口后恢复 1 个当窗事件：Baidu 在官方 Blog 发布 ERNIE 5.1，页面 metadata 给出 `2026-05-09T00:00:00Z`，即北京时间 08:00，明确落入本窗。

该发布把三条已经分别存在的路线组合进同一模型生命周期：多维 elastic sub-network、训练/推理/奖励/Agent loop 的全异步解耦，以及多专家 on-policy distillation 后针对高熵任务保留 online RL 分支。它提供的是厂商实现与版本事实，不是独立复现；6% 训练成本、K3 KL 降低 50% 和各项 benchmark 均缺少可复算的完整 workload、硬件、precision、batch、并发和 SLO 合同。本次评分为 `2 + 3 + 2 = 7`，完成深入审阅；对读 Ch21、Ch31 与 Ch33 后判定为已有覆盖，不重复添加版本型正文。

本日报的 Coverage、Evidence 与 Books 判断已闭合，并通过非作者独立复核。动态历史目录的分页缺口已隔离，
没有参与正向证据或“全站绝无更新”断言。

## 2. 来源覆盖

本轮只检查 Daily 来源，不扫描 Weekly 来源。可复用相邻日期的同一历史列表停止点，但不继承旧报告的完成标签。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | Research/News 历史入口与本窗定点检索 | 受阻 | 未恢复可按 24 小时窗口分页的历史目录；不支持“官方绝无更新”的断言，也不支持候选或 Books |
| SRC-ANTHROPIC | Research 历史目录；05-07 条目已在前窗处理，本窗未见独立事件 | 已检查 | 目录只给日期的事件不据此补造时刻 |
| SRC-GOOGLE-AI | DeepMind / Google Research Publications 有界检查本窗与相邻日期 | 受阻 | 历史列表日期粒度和分页停止点不足；隔离为 Coverage limitation |
| SRC-META-AI | Meta / FAIR Publications 的可见历史列表与 arXiv family 交叉核对 | 已检查 | 动态目录只支持本次可见范围；未据此声称全站零遗漏 |
| SRC-QWEN | Qwen Blog / Research 检查本窗与相邻日期；05-07 更新在窗外 | 已检查 | 未见可唯一归属的本窗研究事件 |
| SRC-DEEPSEEK | 官方 `/news/` 历史索引；相邻可见研究事件为 04-24 与 06-24 | 已检查 | 无 |
| SRC-MOONSHOT | Kimi Blog 与 MoonshotAI 官方仓库的本窗定点检查 | 受阻 | 缺稳定的历史分页停止点；不支持零遗漏断言 |
| SRC-TENCENT-HUNYUAN | Hunyuan Research“全部”列表；相邻日级条目为 04-30 与 05-21 | 已检查 | 无 |
| SRC-ZAI | 智谱 Research 列表；相邻日级条目为 04-29 与 05-20 | 已检查 | 无 |
| SRC-BYTEDANCE-SEED | 官方论文目录 API 第 2 页越过本窗；05-09 的 `2605.09233` 是后来回填的 arXiv family，精确 v1 不属于本窗 | 已检查 | `PublishDate` 仅作目录日期，不能覆盖 arXiv 首次公开证据 |
| SRC-BAIDU-ERNIE | ERNIE Blog 目录与 `ernie-5.1-0508-release` 正文；HTML metadata=`2026-05-09T00:00:00Z` | 已检查 | 1 个当窗事件；厂商技术博客没有独立复现或完整 system card |
| SRC-XIAOMI-MIMO | MiMo Papers 可见列表与 Blog 历史入口定点检查 | 受阻 | Blog 缺可复查的历史日级分页；隔离，不支持候选或零遗漏断言 |
| SRC-MINIMAX | 官方 Research/Blog 历史列表；相邻事件为 03-18 与 05-26 | 已检查 | 无 |
| SRC-ARXIV | official scheduled announcement cadence；本窗开始前的 Thursday 20:00 ET batch 已归 05-08，Friday 无 scheduled announcement | 已检查 | raw=0，候选=0；不把 DataCite ingestion 或 later index date 改写成当窗首次公开 |

无法恢复的历史目录停止点已作为终态限制隔离：它们不支撑候选、Books 或“无遗漏”断言；若未来获得目标时段的官方归档，只重开相应来源与日期。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [ERNIE 5.1 Officially Released](https://ernie.baidu.com/blog/posts/ernie-5.1-0508-release/) | 2026-05-09T08:00:00+08:00 | 把 elastic sub-network、四子系统异步 RL 与 multi-teacher OPD/online-RL 分流组织为同一模型生命周期；`2 + 3 + 2 = 7` | 深入完成 | 已有覆盖：TRAIN-GRPO [Ch33](../../../../books/part-04-training-system/33-grpo.md)；相关边界见 MODEL-MOE [Ch21](../../../../books/part-02-model/21-moe.md) 与 TRAIN-RLHF [Ch31](../../../../books/part-04-training-system/31-rlhf.md) |

## 4. 证据与知识整合

### [ERNIE 5.1 Officially Released](https://ernie.baidu.com/blog/posts/ernie-5.1-0508-release/)

**身份与日期。** 官方页面的可见日期为 2026-05-09，HTML 同时披露 `published_time/datePublished=2026-05-09T00:00:00Z`；换算为北京时间 08:00，落在本日报左闭右开窗口。它是 Baidu 的模型发布与技术博客，不是独立论文或复现实验。

**旧方案为何合理、约束如何改变。** 为每个规模单独预训练、让 rollout 与 update 同步共置、再按 SFT→混合 RL 串行后训练，最容易保持模型身份、样本 freshness 和故障边界。但多规模部署、长 horizon Agent RL 和多领域能力融合会分别带来重复训练成本、阶段空转与目标互相干扰。

**机制与状态所有权。** 官方说明把 ERNIE 5.0 的深度、expert capacity 与 Top-k sparsity 作为可采样的 sub-network matrix，再抽取 ERNIE 5.1；这使 sub-network configuration 成为模型 artifact identity，而不是 runtime 随意关闭层或专家。RL 部分以 RL Controller 为控制中心，将 training、inference、reward 与 agent loop 分开部署和扩缩，通过网络数据组件连接；trajectory 的 policy/router/precision lineage 仍必须在 trainer admission 前一致。后训练再把领域 experts 并行训练，通过 student on-policy samples 与 token-level reverse KL 做多教师能力合并；对于 high-entropy chat/creative tasks，官方明确保留 online RL，而不把 distillation 当作统一解。

**评价与边界。** 页面报告约 1/3 total parameters、约 1/2 active parameters、相对“同规模模型”约 6% pre-training compute、R3 的 K3 KL divergence 降低 50%，以及若干 Arena/AIME/GPQA 等结果；但对照模型、训练 token、硬件、precision、batch、并发、SLO、完整 ablation 与独立 evaluator 均未完整披露。因而这些数字只能作为厂商版本主张，不能被提升为通用成本或稳定性结论。FP8 operator 统一也不证明训推 bitwise 一致；异步解耦会新增 stale trajectory、queue backpressure、partial failure、跨池资源公平与 controller single-point-of-failure。模型规模固定、RL horizon 短或 freshness 比利用率更重要时，独立模型与同步共置仍是可验证的旧路径。

**Books 对读。** Ch21 已用 ERNIE 5.0 技术报告承载 elastic depth/width/sparsity 的模型边界；Ch31 已区分 on-policy distillation、teacher reliability、reverse-KL mode pressure 与 high-entropy 任务的替代分支；Ch33 已把 rollout service、trainer-owned policy epoch、reward/environment evidence、freshness admission、异步队列和 phase-aware resource scheduling 组织为同一控制链。此次发布提高这些路线已被整合到一个厂商模型生命周期的可信度，但没有提供足以改变现有 owner、fallback 或 evaluation contract 的新增公开证据，因此判定 `No Change — Existing Coverage`，不为了留下产品版本制造 Books diff。

## 5. 缺口与下一步

- **后续触发：** 若获得本窗受阻机构入口的官方历史归档，只重开对应来源与日期；当前没有 Review Pending 或 Books 写回队列。
**终态保留项：** Google AI、OpenAI、Moonshot 与 MiMo 的历史日级目录/分页停止点未完整恢复；这些限制不支持正面证据、Books 或无遗漏断言。
**定点重开条件：** 若取得目标窗口的官方归档快照、带精确发布日期的官方索引
或可唯一定位到本窗的原始发布链接，只重开相应来源与 Source Family，不重跑已闭合的 ERNIE 证据链。

## 6. 复核

复核者：`/root`（非作者 fresh-context 复核）；详见 [V3 独立终审](../_sources/daily-20260509/V3_INDEPENDENT_FINAL_AUDIT.md)。

结论：通过

窗口、候选身份、评分、证据边界和 `No Change — Existing Coverage` 均已逐项核验。`validate_research.py`、
本地 Markdown 链接与 `git diff --check` 通过；机器检查未被用来替代语义判断。
