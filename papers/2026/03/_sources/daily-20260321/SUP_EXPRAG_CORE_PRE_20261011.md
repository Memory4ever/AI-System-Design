# ExpRAG 18272：必要原证、实际 owner 与最小整合稿

root 仅准备 03-21 补 03-20 自然日。本稿不是日期确认、Books 已写或日级验收；author 需非准备者核必要原证、日期和实际 owner 后再授写。

## 1. 采用身份与准入

[arXiv:2603.18272v1](https://arxiv.org/abs/2603.18272v1)，[精确 HTML](https://arxiv.org/html/2603.18272v1)。官方历史 v1 submitted 03-18 20:45 UTC 是提交而非公告；本日必要公开日期仍由作者核已有有限公告/公开夹证，不凭提交日自行移入。当前页 v2 不作为本窗技术证据；未见官方撤回/纠错标记不等全版本审计。

单独 SFT 与部署时附加经验不一定让 actor 学会消费记忆 → 用同一 retrieval pipeline 构造训练 Context，固定 bank、只监督 action tokens → 重新评价消费能力与记忆人口迁移的耦合。建议 `2+2+2=6`；跨训练/读取边界计 Reach，不把通用 provenance 原则计 Delta。涉及实际长期缺口时深入采用必要内容，不遍历无关附件。

## 2. 实际必要证据及反侧

root 实际读 v1 §3、§4.1–4.4/Tables2–4、§5.1、B.3–B.6/Table7–8、F/Table17；不声称代码、实验复现或全部附录审阅。

- §3：离线 raw trajectory bank，含 scripted expert 的成功/失败，静态每 episode 或动态每 step 检索；system memory block 分成功/失败，multi-turn observations=user、actions=assistant。SFT 只取成功训练轨迹，并仅监督 assistant tokens；不是把失败动作也作为正确 target。新任务仍在固定环境 dynamics 内，存在可搜集的目标任务参考轨迹前提，不是零目标经验。
- §4.3/Table2：动态替换 memory 会清除 KV 并重编码，也改变查询/序列化；不能把差异全归刷新频率。ALFWorld hard/all-index K4 的 static65.03→dynamic55.74 是直接反侧。推理 Table2 三 seed 不转授所有训练实验的独立重复。
- §4.4：训练和推理都 static K2/JSON；四 instruct checkpoints，在 easy train 上比较普通 LoRA、推理附加 ExpRAG、ExpRAG-LoRA，ALFWorld9/ScienceWorld29 epochs。Table3 匹配目标任务 bank 下多项 hard success 提升，但 Gemma ScienceWorld hard 的4.7低于普通 LoRA6.3与推理检索7.8；Qwen ALFWorld easy84.9也低于普通 LoRA86.3。Table4 去除 bank/换 easy bank 后严重退步，部分低于普通 LoRA；“未见任务”不等没有目标任务 demonstrations。
- §4.4.1 延长训练/validation loss 与 task success 解耦是观察，作者明确没有机制解释；不把 checkpoint 扫描授通用越训越泛化。
- §5.1：scripted failures 不等模型自生错误；read-only memory 不验证持续自主 write/consolidation，也不支持后来版本的 own-failure learning。
- B.4/6：TorchTune、单 A10080GB、bf16、rank8/alpha16/dropout.1、assistant-only CE、greedy T0；ALF max50动作，Science各类按 expert 步数设50–150；concurrency/SLO及全生命周期预算未披露。
- F/Table17：Ministral3-8B/ALFWorld134 episodes，K2 prompt3096.7、29.8steps、总generation2927.81s vs noRAG489.6/48/2769.59s；更少动作不是更低总时长。训练更长 Context、轨迹收集、embedding/index、retrieval、KV重编码和生成费用须另分，不授全部成本对齐。

## 3. 实际知识 owner 与差异

`AGENT-MEMORY` / Ch77：已实际顺读 350–420 的 raw/summary、JitMem query-conditioned constructor 与 CRL 双可变 extractor/actor 交接；邻章 Ch76、78 的入口分责已读。既有 CRL 拥有学习写经验，尚未明确 read-only bank 下学习消费经验与部署人口错配这一简单基线，因此不是仅主题相似的 NC。Ch29 通用 assistant-only SFT、Ch76 检索索引仍由其现有 owner 拥有，不重复其推导。

最小插入：Ch77 现有 JitMem 段之后、`当消费经验的 actor 本身也持续训练时`之前；两段形成固定 bank 的 consumer 学习 → 可变 writer/actor 的后续压力，保留原段。

## 4. 待独核的逐字正文与末注

保存原始经验、再按任务构造 Context，仍不保证执行模型会使用它。一个更简单的训练分支先固定只读 trajectory bank，把与部署相同的检索结果放进训练 Context，只监督当前轨迹的 action tokens；bank 可以保存带结果标签的成功与失败示例，训练 target 却仍只来自成功轨迹。这把“有什么经验可读”和“actor 是否学会消费经验”分开，而不是让历史成功认证新动作。检索人口、格式、训练与消费者版本须一同保存；未在参数训练中出现的任务若已有匹配示范，也不能称为完全没有目标任务经验。<!-- source-family:SF-2026-ARXIV-2603-18272 -->

学习消费会增加训练 Context 和部署 memory 的耦合。[有限只读经验对照](https://arxiv.org/html/2603.18272v1#S4)在固定文本环境中观察到收益，也看到部分模型/任务退步，以及移除或错配经验后比普通 LoRA 更差；scripted expert 的失败不证明模型能可靠复用自己的错误。每步刷新还会替换原推理依据、清除 KV 并重编码，减少动作步数也不等总生成时间下降。轨迹收集、embedding/index、检索、训练和重新编码均付费；缺少匹配示范、记忆漂移或预算不足时，保留无该 bank 的 actor、静态读取或原始轨迹回读，不把这条消费训练分支当成自主持续写记忆的验证。

末注：`SF-2026-ARXIV-2603-18272` — [ExpRAG exact-v1](https://arxiv.org/html/2603.18272v1) §3–4/Tables2–4、§5.1、B.3–6及F/Table17；仅固定只读 bank 的消费训练/部署人口、assistant-only 成功target与动态 Context/KV成本边界。目标任务示范可用性、Gemma/空bank/错配反侧、scripted failure不等自生错误与全费用限制保留；不采通用OOD、持续write、zero-target-experience、越训越泛化或v2新结论。未核代码/复现。

## 5. resume_mar18 非准备者必要 Source / 日期 / actual owner / PRE 裁定

2026-10-11，独立恢复当前 AGENTS、适用每日/来源/Report 合同、统一 Prompt、ROADMAP 与本日停点；仅本 03-21 补 BJT03-20。实际读 exact-v1 §3–4/Tables2–4、§5.1、B.3–B.6/Tables7–8 与 F/Table17，原两段逐字 PRE / 静态末注；actual Ch77 完整342–426及末五行，Ch76 / Ch78 开篇交接。结论：必要 Source、具体差额与原两段 PRE / 静态注有限 **PASS**，不是写后 POST 或 DAY。

原证确为固定只读轨迹库、成功/失败 memory 分标签、仅成功轨迹 assistant action target；训练与读取同 pipeline 的消费学习可独立于 CRL 的可变 writer/actor 采用。现 JitMem407只训练 constructor、CRL409–411共同更新经验与消费者，未明确此固定 bank 的简单消费基线及错配退路。拟位 JitMem 后/CRL 前顺承，唯一 owner `AGENT-MEMORY` 成立，保原两段与相邻论证，不为 SFT / embedding 再设 owner。

直接反侧已实际回对：动态刷新清 KV 且同时改变 query/key serialization，不能归因频率本身；ALF hard K4 static65.03→dynamic55.74；Gemma Science hard4.7低于普通 LoRA6.3与 **LoRA(with ExpRAG)7.8**（不是纯推理 ExpRAG 的6.3）；Qwen ALF easy84.9低于普通 LoRA86.3。空库/错配人口可退过普通 LoRA，scripted failures 不验证自主自生错误，未训练任务仍可能有目标示范。F/Table17的134 episodes、Ministral3-8B / ALFWorld K2总生成2927.81s高于No RAG2769.59s，不能用29.8<48步授更低总时长；这些均不需改原有限 PRE。Table4部分普通推理参考格与Table3未齐，不采用全表精确一致/全模型增益；未核代码/复现或无关附件，不授自主持续写入、通用 OOD 或零目标经验。

日期原件：[官方 DataCite](https://api.datacite.org/dois/10.48550/arXiv.2603.18272) 实际 `created=2026-03-20T02:08:46.000Z`、`registered=2026-03-20T02:08:47.000Z`、`state=findable`、`published=2026`；v1 Submitted03-18T20:45:04Z / Updated03-20T00:15:38Z / Available2026-03，v2 Submitted08-31 / Updated09-01。同本批公告 ID / 官方 schedule 的日级夹证支持 arXiv 事件 BJT03-20 的限定归属，不把 Submitted 或 Updated 自行等同精确首公开，不授别处从未先发；官方当前身份/历史未给具体先稿或撤回信号，v2不作本窗证据。保持2+2+2=6。下一步由 root 独立窄写后，本人一次非writer实际正文/完整邻接/本人静态注 POST；未写前不计整合。

## 6. resume_mar18 非 writer 实际 POST

root 实际窄写后，本人一次独立顺读 Ch77 完整393–423：原query-conditioned/raw/成本/JitMem→新增409/411两段→原CRL双可变actor/extractor与异构reader交接；并实际读2189–2201完整本人静态源注及邻注。新增两正文与2201末注逐字回原已通过PRE各唯一；支持固定bank训练消费接口、成功target与失败memory分责，人口错配/自生错误/动态KV/全部费用反侧及旧路径保留，不授自主持续write或无目标示范。原CRL、JitMem与其他family未被替代，static仅必要来源/边界、无动态验收身份。实际 nonwriter POST 正式有限 **PASS**，限定git diff --check无输出；没有重读无关附件、代码/复現或DAY授权。已通知root释放该Ch77窄锁，正式报告仅在root接纳后归并实际I。
