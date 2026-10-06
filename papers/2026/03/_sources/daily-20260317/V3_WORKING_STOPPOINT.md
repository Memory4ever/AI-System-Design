# 2026-03-17 V3 唯一停点

窗口：2026-03-16T09:00:00+08:00 ～ 2026-03-17T09:00:00+08:00。执行：2026-10-02。作者 mar02；状态完成，root非作者日级Gate通过。独立重读 AGENTS、当前研究/报告合同、Daily 来源/主题、统一入口、ROADMAP 与本日旧停点；Weekly 未加载。旧材料[原报告](./V3_LEGACY_REPORT.md)仅保留证据，不继承1405分母、30候选、NoChange 或 EffectiveDate。

## 来源实际停止

- OpenAI：实际 curl 官方 `https://openai.com/news/rss.xml`、Ruby REXML 完整解析1242项，只提取 Mar15–17日期邻接行。compensation=`Tue, 17 Mar 2026 00:00:00 GMT`（BJT08，落窗）；Codex Security=`Mon, 16 Mar 2026 00:00:00 GMT`（BJT08，左界前）；mini/nano、Japan Teen Safety Blueprint=`Tue, 17 Mar 2026 10:00:00 GMT`（BJT18，右界后）。后两者未审为本日重复。
- Anthropic：当前 Research web58行；随后实际curl解析HTML Sanity `publishedOn`+title March9记录：Mar31T22:17Z Australia、Mar24T10:41Z Learning curves、Mar23T23Z Science Blog/Long-running/Vibe physics三篇、Mar13T10:15Z diff、Mar6T10:30Z Mozilla/Mar6T00Z CVE、Mar5T19:59:21.508Z labor。9条实际跨本窗，无Mar16–17记录；只此Research可见切片，不外推全News历史。
- Google：实际 Research March Blog 第1页204行12条，March16 superconductivity 科学应用范围关闭；March17 CheckUp/乳腺筛查同属临床应用范围，不以 Evaluation owner 重新引入。第2页web恢复失败后，独立对读[已实际保存的原始2条metadata](../daily-20260305/V3_OFFICIAL_RECOVERY_12.md)，Mar6 SpeciesNet/Mar4 Bayesian均窗外，不继承05判断。DeepMind News 第3页302行24卡片、6个March标题（26 FlashLive/Harmful manipulation、25 Lyria、17 Cognitive、10 AlphaGo、3 FlashLite），仅作查漏；Cognitive见D18。pubs实际1–15/11569、2026筛选372，不能恢复Mar16–17完整历史切片，隔离H1。
- ZAI：实际 Research175行15卡片，Mar15 GLM5Turbo→Apr1 GLM5VTurbo跨本窗；未外推所有发布无遗漏。
- arXiv：`show=200` web Cache miss不是充分阻塞依据；实际curl原响应7428B的title为 **Invalid show value. Valid values: 25, 50, 100, 250, 500, 1000, 2000**。合法 `https://arxiv.org/list/cs.DC/2026-03?skip=0&show=250` 实际412295B，title=`Distributed, Parallel, and Cluster Computing Mar 2026`，h2=`Authors and titles for March 2026`，**Total of346 entries /1–250**，15042membership实际存在；没有日级heading，因此月归档身份不能当Mar17公告批次。cs.LG合法首250实际400779B，skip1750/show250实际395476B，title/h2同为March月归档；这不是全月审阅。20EDT→次日08BJT；本窗可能含Mar16 Mon20EDT公告，不把Submitted/ID月份/DOIcreated当本窗公开时刻。
- Meta：Research实际0行不能授覆盖；Blog页1/2实际270/308行、10+12个非日期排序卡片，Mar26/27、Mar10/11与Feb跨窗。有限Blog切片停止；Research窗口出版切片隔离H2。
- Qwen：实际只读 `https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US` 返回articles40，原始extra.date/title对读：Mar19 MaxPreview→Mar30 Omni、Feb16 Qwen3.5，无本窗行；没有exposed total/pagination，限这40条，不保留动态故障。
- DeepSeek：`/en/news/`实际39行、curl109872B；HTML Next props恢复完整posts16（2026Sep10/Apr24→2025Dec1/Sept29/Sept22/Aug21/May28/Mar25/Jan20/Jan15→2024Dec26/Dec10/Nov20/Sept5/Aug2/Jul25）。实际发现并读9467B脚本 `https://www.deepseek.com/_next/static/chunks/app/%5Blocale%5D/news/page-bd765c90dd4eb584.js`，News切换为 `N=u?w:w.slice(0,4)`、Research `d=s?g:g.slice(0,10)`；Research数组最新Jun24→Feb25→Jan28→Jan12→2025Dec31/Dec2，跨窗。hidden News现已实际恢复，不继承他日gap，不授全机构无遗漏。
- Moonshot：Kimi `/en/blog/`155行19卡片，Jul16→Apr20→Feb9→2025无本窗可见行。15031触发官方[Attention-Residuals repo](https://github.com/MoonshotAI/Attention-Residuals)定点身份核：当前4commits，API created_at=`2026-03-15T13:29:15Z`、pushed_at=`2026-03-17T06:23:11Z`、当前public、releases0；创建/作者commit/当前public不证明首公开，归D7而非新家族。
- Hunyuan：观察到的只读 `https://api.hunyuan.tencent.com/api/blog/publicList`，renderType0/pageNum1/pageSize20实际code0、totalNum11/returned11；paired publishedAt/displayPublishTime原值转BJT：Feb3/Feb13→Apr23显示（实际published Jun24）/Apr30→May21→Jul6/21→Aug11/28→Sept22。两字段角色不互换；11行无March，不外推全机构历史。
- ZAI发布说明：`https://docs.z.ai/release-notes/new-released`165行，当前Aug26→Apr7→Feb12/Feb3等跨窗可见章节，无March；和Research15条为有限停止，不授全部ViewMore。
- Seed：只读public API type1/publish_year2026/order_desc=false/count20/page_token20实际total82、返回14、next40/has_moretrue；Feb27→Mar1→Mar12/15→Mar16 MoDA→Mar21–26跨窗，停止不扩82库存。type2/token0返回9、total23/next20/has_moretrue，Feb12–14→Apr1/9→以后跨窗。MoDA原published=`1773590400000`（BJT Mar16T00:00，日级字段）与完整摘要实际核，不能据此强定首次公开，D6。
- Baidu：`https://ernie.baidu.com/blog/zh/`68行10卡片，May9/Apr30/Apr15→Feb6/Jan29→2025Nov21，停止页1（Next2/2为旧切片），无本窗可见行。
- MiMo：首页338行Paper8（Jun29→Mar13 Tangram→Feb3）、Blog15无日期；curl58220B及实际脚本4752.2908c99e.js743278B恢复原路由 `/blog/mimo-v2-pro`、`/blog/mimo-v2-omni`。两原路由web不可读、curl15063/15066B只有JS壳且无日期字段；Flash-safety前置日期2025Dec18，不当本窗。仅上述两个必要原入口/本窗dated Blog切片为H3，不把未知More全库存成队列。
- MiniMax：Blog76行12卡片，Aug→Mar18 M2.7→Feb14Forge→2025Oct；AgentTechBlog15行仅标题，llms.txt48行仅guide/techblog索引，无Mar16–17历史快照。有限Blog停止；必要AgentTechBlog本窗切片H4。

arXiv主题API实际均start0，submittedDate=[202603130000 TO 202603162359]仅发现窗口邻接线索（Submitted非公开）：系统cs.DC/AR/PL/OS/PF+(LLM/GPU/Transformer/inference/training) max50实际49/49标题；模型Agent cs.CL/LG/AI/IR/MA+ti(agent/memory/attention/language/reasoning/training) max50实际50/310；多模态cs.CV/RO+ti(world/foundation/VLA/diffusion/multimodal/vision-language-action) max40实际40/139；优化cs.CL/LG+ti(pretraining/optimization/MoE/quantization/cache/RL/distillation) max40实际40/80。范围外标题可停，潜在增量完整题摘见下；不是179项全题摘/全文审，也不追310/139/80剩余队列。辅助搜索限定Mar16同主题若干查询，只回原始exact-v1；搜索无命中不授零论文。

## 贡献前具名关闭 / 首批校准待送

N1 [Equipping workers with insights about compensation](https://openai.com/index/equipping-workers-with-insights-about-compensation/)：官方核心L23–32完整读到；劳动市场使用分类与薪酬领域 WorkerBench，未提出模型训练/执行新机制或新评价可比性条件，局部OEWS数值吻合不足改变本项目主线。分类隐私叙述仅厂商分析权限说明，不授隐私机制或安全保证。贡献前关闭、不评分、不改Books。原报告链接未据此展开，因为决定准入已明确。

N2 Google [When Correct Is Not Safe](https://research.google/pubs/when-correct-is-not-safe-can-we-trust-functionally-correct-patches-generated-by-code-agents-2/)：完整官方abs L119–122与[ACL原metadata](https://aclanthology.org/2026.acl-long.707/)July2026/abs L57–60及[2510.17862v1](https://arxiv.org/abs/2510.17862v1)完整题摘+唯一Oct15v1历史实际读。功能正确却引入漏洞是明确安全反证，原2025身份不抹去其贡献；本次当前年度pubs只是later ACL record，无独立本窗新event/新mechanism披露，不冒称当窗已审duplicate。root需核当前安全说明后裁决这一关闭。

N3旧拟关闭已纠正：不能以没有新实证拒绝理论评价protocol。作者与root均实际读Cognitive Blog L255–283及[官方PDF](https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/measuring-progress-toward-agi/measuring-progress-toward-agi-a-cognitive-framework.pdf) p1完整摘要/§3 p4–5：逐faculty、same instructions/tools条件、代表性人类分布percentile与jagged profile改变aggregate benchmark的比较对象，作为D18潜在规范方案，不声称已验证AGI。PDF封面Mar16、Blog Mar17均day-only不是first-public timestamp；仅核日期，不扩32页全文。

root首批实际校准：5篇exact-v1完整题摘/history通过potential；N1原核心和N2当前Google安全摘要+2025v1身份已实际通过贡献前关闭。后批实际7篇15031/15589/15530/14633/14851/14972/15618题摘/history通过潜在增量，不授性能或安全保证。其余仅作者记录未冒称root已审。

## 首批潜在线索（日期先核，未评分）

完整exact-v1题摘与history实际读：

- [14745 CAMD](https://arxiv.org/abs/2603.14745v1)：采样coverage/难度/残余risk理论→posterior coverage、evidenceweight、sequentialBayesian预算，potential评价/推理取舍；Submitted=`2026-03-16T02:31:03Z`。
- [15042 DetShare](https://arxiv.org/abs/2603.15042v1)：透明unmodifiedkernel与tail确定性张力→GPUcoroutine+light迁移、TPOT-first，potential资源机制；摘要数字不授保证。Submitted=`2026-03-16T09:48:34Z`；后来v2Mar17T08:51:40Z、v3Apr3、v4Aug5，不与本窗v1混合。
- [15125 MEMFLOW](https://arxiv.org/abs/2603.15125v1)：memory retrieval控制流+跨任务持久影响MCFA，potential安全反证；Submitted=`2026-03-16T11:21:30Z`，后来v2May9/v3Jun5非本窗修订。
- [13289 RelayCaching](https://arxiv.org/abs/2603.13289v1)：decode→prefill同文本KV相容及prefix偏差的layer/token稀疏重算，potential；Submitted=`2026-02-28T04:46:28Z`，不是首次公开。
- [13319 LightningRL](https://arxiv.org/abs/2603.13319v1)：dLLM高并行轨迹RL+perreward归一化/正确轨迹NLL/TPFawarefilter，potential；Submitted=`2026-03-04T11:43:19Z`，v2Jul31窗外，搜索Submitted日期不决定首公开。

实际DataCite只核exactDOI3项原值（REST查询其他结果不采用）：14745 created/registered=`2026-03-17T04:22:32Z`，v1 Updated=`2026-03-17T01:44:51Z`；15042 created=`2026-03-17T04:29:27Z`、registered04:29:28Z、v1Updated02:05:42Z；13289 created/registered=`2026-03-17T03:48:13Z`、v1Updated00:03:07Z。Available只有`2026-03`。前三created上界全部晚于本窗BJT09，Updated字段不等公开正文证明；仍缺具体原始公告batch或作者稿首次公开，未将其计入确定候选/深审/Books。

## 日期终态：23潜在家族，未评分、未进入确定候选

以下完整exact-v1题摘均实际读；Cognitive仅上述官方core/PDF必要段，Anole额外窄读§II-B/IV及直接baseline反证。REST DataCite一次exactDOI OR查询total14/14、另安全4/4；`created`/`registered`和v1 `Updated`只是原始登记字段，不当正文公开时间。时刻均Z；括号R为registered仅与created不同时列。Available仅2026-03。官方[availability](https://info.arxiv.org/help/availability.html)实际读L170–199：通常Sun–Thu20Eastern、可延迟1–4天或更久、ID按首次公告分配；本窗常规Mon16公告最早Mar17BJT08，但下表登记上界晚于BJT09，不能据此补成08。早Submitted也不能排除moderation后公告。

| 身份/精确版本 | 原始Submitted v1 | created（R） / Updated v1 | 具体潜在增量与受限采用方向 |
| --- | --- | --- | --- |
| D1 [14745 CAMD](https://arxiv.org/abs/2603.14745v1) | Mar16T02:31:03 | Mar17T04:22:32 / 01:44:51 | coverage posterior/evidenceweight/sequential预算；不授risk guarantee |
| D2 [15042 DetShare](https://arxiv.org/abs/2603.15042v1) | Mar16T09:48:34 | Mar17T04:29:27(R28) /02:05:42 | GPUcoroutine/context迁移+TPOTfirst；v4 VitaminE不混采 |
| D3 [15125 MEMFLOW](https://arxiv.org/abs/2603.15125v1) | Mar16T11:21:30 | Mar17T04:31:24 /02:10:51 | memory retrieval→controlflow跨任务MCFA；不授通用攻击率 |
| D4 [13289 RelayCaching](https://arxiv.org/abs/2603.13289v1) | Feb28T04:46:28 | Mar17T03:48:13 /00:03:07 | decode/prefill KV兼容与prefixlayer/token稀疏重算 |
| D5 [13319 LightningRL](https://arxiv.org/abs/2603.13319v1) | Mar4T11:43:19 | Mar17T03:48:56 /00:05:24 | perreward normalization/正确轨迹NLL/TPFfilter；不借一般RL原则评分 |
| D6 [15619 MoDA](https://arxiv.org/abs/2603.15619v1) | Mar16T17:59:55 | Mar17T04:43:05(R06) /02:40:02 | sequenceKV+depthKV及非连续布局计算；Seed日级字段非firstpublic |
| D7 [15031 Attention Residuals](https://arxiv.org/abs/2603.15031v1) | Mar16T09:32:21 | Mar17T04:29:12(R13) /02:04:33 | input相关depthweights/blockcache/PP两阶段；repo创建非公开证明 |
| D8 [15589 LEXI](https://arxiv.org/abs/2603.15589v1) | Mar16T17:48:30 | Mar17T04:42:22(R23) /02:38:34 | BF16指数Huffman无损、onfly多lane/NOC LUT端口；不授芯片实测 |
| D9 [15530 DUET](https://arxiv.org/abs/2603.15530v1) | Mar16T16:56:01 | Mar17T04:40:59(R04:41:00) /02:35:20 | hybrid SSM/Attention prefill/decode分专用package；DACaccepted不定首次公开 |
| D10 [14633 When Scanners Lie](https://arxiv.org/abs/2603.14633v1) | Mar15T22:08:16 | Mar17T04:19:58 /01:37:19 | 固定攻击/output而evaluator扰动导致ASR归因变化；安全测量反证 |
| D11 [14851 AutoMoT](https://arxiv.org/abs/2603.14851v1) | Mar16T05:50:31 | Mar17T04:25:01 /01:52:37 | fast/slow jointattention及async频率；不采v3后来修订 |
| D12 [14972 TakeVLA](https://arxiv.org/abs/2603.14972v1) | Mar16T08:33:48 | Mar17T04:27:50(R51) /02:00:57 | pre-takeover语言监督与重构场景RL；TTC非安全保证 |
| D13 [15618 DeepVision](https://arxiv.org/abs/2603.15618v1) | Mar16T17:59:54 | Mar17T04:43:04 /02:40:00 | 深层visualconditioning+actionguidedpruning；v2SubmittedMar17T16:04:49窗外 |
| D14 [13606 NCCL EP](https://arxiv.org/abs/2603.13606v1) | Mar13T21:28:22 | Mar17T03:55:48(R49) /00:26:34 | unified Dispatch/Combine deviceAPI、LL direct/HT aggregation路径；未核现实现 |
| D15 [15202 L-Metric](https://arxiv.org/abs/2603.15202v1) | Mar16T12:43:32 | Mar17T04:33:12(R13) /02:14:32 | prefilltokens×batch scheduling score和调参抵消条件；非普遍无调参 |
| D16 [15183 Token Coherence](https://arxiv.org/abs/2603.15183v1) | Mar16T12:20:06 | Mar17T04:32:45(R46) /02:13:46 | derived artifact lazyinvalidate/conditionalread；不授MESI比喻为正确性证明 |
| D17 [15699 Time as Energy Proxy](https://arxiv.org/abs/2603.15699v1) | Mar16T08:26:57 | Mar18T02:14:49(R50) /02:26:54 | API runtime能耗代理与localcounterpart身份；PerComcomment非首公开 |
| D18 [Cognitive Framework](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/measuring-agi-cognitive-framework/) | PDFcover2026-03-16；BlogMar17day-only | 精度不足；有限curl SSL_ERROR_SYSCALL、bytes0 | matchedtools/instructions逐faculty人类percentileprofile；规范proposal非validatedAGI |
| D19 [13435 CtrlAttack](https://arxiv.org/abs/2603.13435v1) | Mar13T08:05:50 | Mar17T03:51:50 /00:13:00 | 低维velocityfield→temporal displacement扰动I2V状态；不把低FID当可靠worldstate |
| D20 [15417 TTRL Amplification](https://arxiv.org/abs/2603.15417v1) | Mar16T15:28:59 | Mar17T04:38:17(R18) /02:27:38 | selfconsistency reward放大基模型安全/恶意行为及reasoningtax；不是只报道jailbreak |
| D21 [13026 PISmith](https://arxiv.org/abs/2603.13026v1) | Mar13T14:34:54 | Mar16T01:55:56(R57) /00:52:07 | sparse reward→entropy collapse、adaptiveentropy/advweight redteam；上界BJT09:55晚于左界，可能Sun公告BJT08在窗前 |
| D22 [13782 Navigation Heads](https://arxiv.org/abs/2603.13782v1) | Mar14T06:26:11 | Mar17T03:59:52(R53) /00:38:46 | frozen heads deviation sensor→RL rollback；44.6% detection/11.7%FPR非safetyauthority |
| D23 [15046 AnoleVLA](https://arxiv.org/abs/2603.15046v1) | Mar16T09:57:45 | Mar17T04:29:32.000(R33.000) /02:06:07 | 窄core L81–154明确state/delta→vision→language因果顺序、末token单forward continuous chunk、velocity→acceleration两阶段；不只是SSM主题映射 |

日期请求每家族仅此一处：D1–17/D19–23分别需要该exact-v1首次公开正文的原始announcement timestamp/实际日级batch+正文可取上界，或有可核验首次发布元数据的作者稿/官方项目事件；完整区间必须落本窗，否则定点转真实归属日。月表当前只有月份，未恢复日级header；DataCite created越截点，不能推出准确20EDT批次或提前公开。D6允许Seed原发布详情first-public字段代替；D7允许官方repo首次公开记录（不是commit/push）代替；D9/D17接受作者原venue全文first-public记录，非accepted/封面年份。D18需要该Blog或PDF原发行timestamp/timezone或封闭落窗区间，封面不够。没有可执行新的官方精确入口时停止，不深审不可落窗正文；终态隔离不支持候选、Evidence、Books、覆盖/无遗漏或性能安全保证。恢复只重开上表具体identity/date，不重跑月库存。

## 有限负侧与未审范围

N4 [MER-Bench15020v1](https://arxiv.org/abs/2603.15020v1)：完整题摘L16–19/historyL27实际读；新meme重评任务和MLLMjudge四维情感/结构分解，未新增judge有效性、噪声/归因/资源边界条件；不是因为benchmark或领域题材一律排除，按本篇具体增量贡献前关闭，不评分、不为不影响处置追日期。

Anole旧拟常规SSM组合负理由经窄core被推翻：上述D23替代之。§V-B L179–180实际写baseline有原论文引用，不能据parameter近似称matched backbone attribution；本日仅准入消歧，不计Evidence完成。

范围层标题样本：Google Research Mar16 superconductivity、Mar17 breast screening/CheckUp是科学/临床应用暂缓；arXiv搜索15100 NSCLC clinical prognostic、15093 wireless beam domain未作为新基础模型机制，未声称已读所有正文。原始宽API只作有界title查漏，剩余310/139/80、月表346及旧1405均未逐项题摘/全文审，不能授全量负侧/无遗漏。

## 历史目录终态 / 下一步

H1 Google pubs2026筛选372的Mar16–17相关publication历史切片无法从current1–15/11569定位；需官方date-bounded原始导出或历史分页定位，重开pubs本窗而非全年度。H2 Meta Research0行：需本窗可读官方研究publication列表，重开Research入口（Blog22可见行判断保留）。H3 MiMo仅已观察的V2Pro/Omni两个Blog原路由与本窗dated archive：需可读核心及date字段/历史切片，不能把JS壳记零命中。H4 MiniMax AgentTechBlog只标题：需本窗官方techblog dated列表/原始快照，保留Blog12停止，不扩guide站。上述具体历史切片无法授完整coverage，终态隔离不支持候选/Books/无遗漏；当前无需再次普通browser转交或广泛新入口追查。

H5 Seed type2/count20/token0只有当前可见9/total23,next20/has_more=true；未返回身份/日期隔离，不支持全部Blog/本窗无遗漏。需官方本窗切片或差额解释，重开type2本窗而非无限分页；不复制他日count100的14/19判断。

普通待办0；正式README完成同步。root实际完整读六部分与本停点，核14来源/有限查询/全部23身份日期记录/隔离条件，日级Gate通过；首批12arxiv+Cog和N1/N2/N4实际窄审保持有效，余10家族没有被root全题摘/全文审，不授所有23Evidence。确定候选0/Books0；V3 validator/限定diff-check/本地引用通过，完成态重跑。D1–23/H1–5不用于正面Coverage/Evidence、Books或无遗漏/安全保证。共享Books没有写入/锁，不新增 LS/索引，不 stage/commit/push。本日不再扩查，按root新分配独立换03/20。
