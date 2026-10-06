# Daily Research — 2025-12-19

**规范：** V3
**窗口：** 2025-12-18T09:00:00+08:00 ～ 2025-12-19T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-02T20:59:07+08:00

## 1. 结论

一项明确落窗的入选家族是 T5Gemma 2 官方 release。共享 embedding 与合并 decoder self/cross attention 改变 encoder-decoder 的参数冗余及归一化边界，并不证明 decoder-only 被普遍替代。独立日期/准入及必要源审已有具名记录；root实际替换Ch18 Encoder-decoder末段为两段，Feynman局部POST，本家族无Books待办。

四组收窄 arXiv 查询分别返回 133、3、31、41 行，跨组身份去重并作官方精确 ID 段有界补检；原130条完整v1处置的记录存在12个遗漏身份，Feynman已具名读题摘/必要正文，现逐一同步，并重开CAMP-VLM/FEAML两项负侧，原ordinary0撤销。具体差额14项已闭环，见[作者补正](../_sources/daily-20251219/AUTHOR_REVIEW_RECONCILIATION.md)。这些是submitted缓冲线索，不是本日公开论文数；潜力与反证保留，first-public未定者隔离，不能以日期失败替代普通阅读。当前普通作者项0，日级非作者核验通过。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | Research 历史入口原恢复失败；具名 12/18 Codex release、精确 22 页 addendum §3/4/5.1.2、 dated Model Spec U18/definitions 已读 | 受阻 | 历史目录与个体公开时刻隔离；可读普通任务已处理，不作零事件断言 |
| SRC-ANTHROPIC | Research 历史列表受限；Alignment Dec19→16→12→8；12/18 Vend 2、wellbeing、Skills 更新及实际触发规范核心/脚注已读 | 受阻 | 日精度未授落窗；wellbeing 更正/Skills 历史版本隔离，不把当前文本当旧快照 |
| SRC-GOOGLE-AI | DeepMind Blog page/4 的 24 项历史邻接段；Google Research 2025 页12条 Dec18→15→12→10→4→3→Nov12；T5官方release与v1 §2/3、Table1–5及Ch18实际整合 | 受阻 | T5无Books待办；Publications历史首公开缺口隔离，非目录覆盖通过 |
| SRC-META-AI | global_search page=3 四项 Dec18 watermark 原始题摘；本日精确邻接段核 identity，MSE 数据页核心亦读 | 受阻 | 四项日精度未授本窗，具体 first-public 恢复条件见原始记录 |
| SRC-QWEN | 原 Blog 迁移前终止 Sep23，迁移后历史入口原始失败；本窗 Qwen3 commitroute 空且无 Next | 受阻 | 原历史列表不可恢复；repo 切片不证明全网无事件 |
| SRC-DEEPSEEK | 本次原目录最新 2026 Sep10/Apr24 → 2025 Dec1 → 更早，已越过 Dec18 邻接段 | 已检查 | 仅该目录有界结果，无全网零事件保证 |
| SRC-MOONSHOT | 原 Blog26项/当前 changelog Nov7 发布/Nov6 版本 → Oct27 → Sep5 → 2024，未见分页；KimiK2本窗repo空 | 已检查 | 只支持指定目录与repo有界观察 |
| SRC-TENCENT-HUNYUAN | 原研究页全部 API 仅 2026 的 11 项；T1/Video1.5/World1.0/WorldPlay本窗official commitroute，无 Next；按逐条时刻过滤，WorldPlay六项本窗 patch 已读 | 受阻 | 研究历史列表及 artifact 公开时刻隔离；commit 不等于 public，响应窗外条目未授本日 |
| SRC-ZAI | 官方 Research page=2 的 18 项，Dec21 GLM4.7 → Dec10/9/8/7，页面无 More | 已检查 | 只支持本段目录观察 |
| SRC-BYTEDANCE-SEED | 官方 Blog 原 year=2025 第0页15项邻接 Dec24 → Dec18 Seed1.8 → Dec16 Seedance → Dec2；论文第0页18项非严格日期序；Seed1.8完整核心已读 | 受阻 | Seed1.8午夜日编码不授上半日公开；精确历史 card 有限恢复失败，隔离不采用 |
| SRC-BAIDU-ERNIE | 原 Blog page1 的 10 项，Dec23 → Dec9 → Nov21，Next 2/2 在更早段 | 已检查 | 无本段新事件断言以外的保证 |
| SRC-XIAOMI-MIMO | 官方 MiMo v2 Flash 精确报告/SpecV2原文身份未变；本窗MiMoV2Flashcommitroute空无Next | 受阻 | 原事件日精度不可授本窗；不重复前日patch、不扩SGLang周源 |
| SRC-MINIMAX | 官方 Blog 当前 12 项，Dec23 → Oct27，越过本窗邻接段 | 已检查 | 仅该 Blog 边界 |
| SRC-ARXIV | 四组 submitted 2025-12-17～18 收窄主题查询，无 Next；官方cs.CL月列表仅2512.15081–16170身份标题段；130精确v1题摘与三个决定准入正文补读已处置 | 受阻 | individualfirst-public 未定者隔离；无月份/提交字段授时刻，不作零事件或覆盖通过 |

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [T5Gemma 2 官方 release](https://blog.google/innovation-and-ai/technology/developers-tools/t5gemma-2/) | 2025-12-19T02:30:00+08:00 | encoder/decoder三处embedding共享，self/cross attention共享投影与联合归一化，重估结构冗余/质量边界；2+2+2=6 | 深入完成 | 整合：`MODEL-DECODER-ONLY` [Ch18](../../../../books/part-02-model/18-decoder-only.md)，Encoder-decoder末两段；root写入、Feynman局部POST |

## 4. 证据与知识整合

### [T5Gemma 2 官方 release](https://blog.google/innovation-and-ai/technology/developers-tools/t5gemma-2/)

官方 Blog JSON-LD `datePublished=2025-12-18T18:30:00+00:00`；`dateModified` 为 2026-03-19，当前文本并非不可变 2025 快照。release 时间只授本事件，不代授 arXiv first-public。

[精确 v1](https://arxiv.org/html/2512.14856v1) §2 已实际读：decoder query 来自自身输入 X，K/V 由拼接的 X 与 encoder H 经共享投影产生，attention logits 联合归一化；mask 同时管理 source 与 target 可见性。这不等价于分别运行两个 softmax 后加总。embedding 三处共享减少参数；仅在每六层 global self-attention 层保留 cross-attention 的实验反而质量下降，不能把减少模块推成无代价压缩。§3 的 UL2 配比、Gemma3 初始化、冻结视觉 encoder、pretraining 无蒸馏与轻量 post-training 已读，必要表格亦已完成。

Table1 架构消融是 Gemma2 初始化、400B tokens、PrefixLM+KD，最终 Gemma3/约2T/UL2 配方不能混写成同一对照。baseline47.8、tie47.7、merge47.5、global-only46.5，未披露 repeats/error bars，不作严格非劣性。Table4/5 的不同后训练、text-only/multimodal及 approximate DocVQA/InfoVQA 不能做单机制归因；pretraining reasoning 有型号均值反而下降。参数节约成立，但端到端推理收益的硬件、precision、batch、concurrency、SLO等 Not Disclosed，不由参数下降推通用加速。

原Ch18基线独立encoder/causal decoder/cross-attention接口合理，但不整项覆盖共享/联合归一化。root现已在唯一owner [MODEL-DECODER-ONLY Ch18](../../../../books/part-02-model/18-decoder-only.md) Encoder-decoder末段局部替换为两段，作者实际读当前50–52行及family末注：共同K/V投影/softmax、global-only反例及400B局部消融边界均保留。相邻Ch17/19交接未转移owner。Feynman非writer局部POST见[独立记录](../_sources/daily-20251219/INDEPENDENT_REVIEW.md)，本家族无Books待办；不授通用加速、全任务非劣性或日级完成。原[提案](../_sources/daily-20251219/BOOKS_T5GEMMA_PROPOSAL.md)保留为实际差额依据。

首批潜力及代表性负侧见 [准入记录](../_sources/daily-20251219/ADMISSION_CALIBRATION.md)，完整题摘处置见 [追加记录](../_sources/daily-20251219/ADMISSION_ADDITIONS.md)，原始边界与有限失败/逐条 artifact 判断见 [来源停止点](../_sources/daily-20251219/SOURCE_STOPS.md)。

## 5. 缺口与下一步

原普通0在12遗漏/两重开未同步时不成立，已撤销；现14项具体补正均写入[作者差额记录](../_sources/daily-20251219/AUTHOR_REVIEW_RECONCILIATION.md)，复用非作者已读exact-v1/必要局部原文，保留反证和隔离身份。当前普通作者项0，T5实际整合/局部POST已落实且无Books待办；非作者已核正式差额并通过日级验收，没有未处理的可执行工作。

本窗终态保留项：个体 arXiv 公告时刻不可由 submitted/OAIupdated 补造，完整题摘potential身份在追加记录中逐项保留；Codex/Vend/Meta四watermark日精度无可支持offset/时刻；wellbeing当前纠错与历史版本、Skills精确旧schema、Seed1.8原card、WorldPlay artifact pushed/public 时刻缺失。各项均不用于正面证据、本窗确定候选、Books、覆盖通过、无遗漏断言或性能/安全保证；重开仅接受具名官方first-public/announcement、完全落窗的公开范围或该精确旧版。具体URL/原始字段与有限失败见来源停止点，一次请求，不再重复同接口。

## 6. 复核

复核者：Feynman（非作者；作者Nash）。
结论：通过

实际检查查询/停止范围、14源本窗邻接、T5 release原日期及精确v1必要方法/评价、Ch18及相邻17/19、40项exact-v1完整题摘、安全/设计反证与分层负侧，并独立读取具名官方安全材料与WorldPlay必要精确patch；范围及未检查部分见[独立记录](../_sources/daily-20251219/INDEPENDENT_REVIEW.md)。实际回查作者14项差额表及正式§1–5，12遗漏均作具体处置、CAMP-VLM/FEAML保留必要局部反证；T5日期/6分窄增量与root实际Ch18两段整合及非writer POST通过。无未处理扫描、准入、必要阅读或Books任务。具名first-public/旧版等缺口不授覆盖通过、零事件或性能/安全保证，只接受原始必要材料定点重开。语义差额已闭合；按用户授权窄修§1/§5旧状态句与终态隔离字段，不改变证据结论，不重复未变化原文。
