# Daily Research — 2026-06-06

**规范：** V3
**窗口：** 2026-06-05T09:00:00+08:00 ～ 2026-06-06T09:00:00+08:00
**窗口说明：** 用户明确保留旧候选日期、评分与原小时窗，仅补遗漏；旧完成声明不代替本轮验收。
**补充窗口：** 2026-06-05 ～ 2026-06-05
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-25T17:02:29+08:00

## 1. 结论

旧轮 Kimi Code 0.11.0 的日期、评分和有效证据保持。本轮按 Jun05 北京时间自然日补遗漏，当前21个唯一family均已获得本次处置：15个实际整合、5个具体已有覆盖、1个ADWM中心争议隔离。QCFuse与2604.08585同family的重要扩展不双计；CMTF是root实际writer，不冒记本人SAVE。SET跨worker graph资源重绑定、OneStep训练time采样替代与Deopt的CPU源结构简化均已实际写后通过；WebMCP/RiskStates/HarnessFix不为通用原则或实现命名制造Book差额。ADWM的target-law与实际估计器两条中心冲突保原证据，不降分/删候选或正采OPE能力。Hunyuan当前All API已为本日真实恢复，撤销该路径仅因空壳而受阻的过时判断。R37完整日级独核通过，有限来源与具名终态保留均到安全终态，不代表全部原始源或论文主张获证。[作者记录](../_sources/daily-20260606/SUP_AUTHOR_20261025.md)保真实交接。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 本轮官方[RSS](https://openai.com/news/rss.xml)解析至Jun05BJT目标及两侧，Jun04UTC12:00后下一条Jun08UTC00:00；[ORG B2](../_sources/daily-20260606/SUP_ORG_20261025.md) | 已检查 | 本范围无条目；不声称删除稿/所有历史修订穷尽 |
| SRC-ANTHROPIC | 本轮从公开SeeMore脚本恢复[真实page2](https://www.anthropic.com/listing/research/default/2)，24项Jul28–Apr23跨目标日；Jun08→Jun05chemist→Jun03，止page2；[ORG B2](../_sources/daily-20260606/SUP_ORG_20261025.md) | 已检查 | 唯一当日chemist按AIforScience暂缓范围关闭，不扩后续分页 |
| SRC-GOOGLE-AI | GoogleResearch Jun05 AgenticRAG核心及具体Ch76 NC经R17；DeepMind真实[Page2](https://deepmind.google/blog/page/2/)Jun09→Jun03相邻原文日期已B5/R21核，止第2页；Research pubs的官方URL不可达/HTTP空体见ORG B4 | 受阻 | Blog已读目标范围stop有效；缺Jun05带日期publication原始列表/可读快照，不作pub零事件或全面覆盖证据，仅该目录定点重开 |
| SRC-META-AI | 本轮官方research动态目录0行，exact-date补检仅how-to/creative非研究；[ORG B1/B3](../_sources/daily-20260606/SUP_ORG_20261025.md)实际浏览器不可用 | 受阻 | 缺Jun05带日期官方研究历史列表；不沿用旧小时窗SIRA记录授补充窗口覆盖 |
| SRC-QWEN | 当前合法[article retrieval](https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US)，`type=qwen_ai/language=en-US或zh-CN`各40项、无分页字段；本轮root读[原始响应与调用依据](../_sources/daily-20260607/SUP_SOURCE_CHECK_20261025.md)，Jun01→Jun16跨Jun05，无目标项 | 已检查 | 仅当前中英研究目录，不含删除稿；旧空参数/2025配置不再作为此入口受阻或零命中依据 |
| SRC-DEEPSEEK | 本轮原首页更多实际到[news](https://www.deepseek.com/news/)，研究Jun24→Feb25、动态Sep10→Apr24；API目录Jul31→Apr24；[ORG B3](../_sources/daily-20260606/SUP_ORG_20261025.md) | 已检查 | 当前目录目标邻段无事件，不作所有渠道/删除稿保证 |
| SRC-MOONSHOT | 本轮平台Blog当前尾至2025、官方org无日期curated Research；本窗KimiCode旧有效与KimiCLI1.47迁移/errorbrief具体N，ORG B1/B4 | 受阻 | 已读发布范围有限stop；缺Jun05研究带日期历史目录，不由当前项目列表授全研究零 |
| SRC-TENCENT-HUNYUAN | 官方[All API](https://api.hunyuan.tencent.com/api/blog/publicList) `pageNum=1/pageSize=100/renderType=0`，补核官方`accept-language:zh`原响应code0/total11/list11；root逐行核display/published/public日期，Jul06→May21跨Jun05，无目标项；[中文原件](../_sources/daily-20260607/SUP_HUNYUAN_ALL_ZH_20261025.json.gz) | 已检查 | B6先前9项仅英语All，不冒充中文全部；当前有限目录不授删除稿/其他渠道或严格首公开时刻保证 |
| SRC-ZAI | 本轮官方research Jun16→May20、release notes Jun16→Apr07目标两侧，止各相邻段；ORG B1 | 已检查 | 当前两目录未见Jun05；不遍历普通commit或宣历史revision穷尽 |
| SRC-BYTEDANCE-SEED | 本轮Publication第1页Jun11→Jun04；五个Blog category已实际读过Jun05两侧，URL/stop见[ORG B3](../_sources/daily-20260606/SUP_ORG_20261025.md) | 已检查 | 目标目录无Jun05条目，不扩全部246论文 |
| SRC-BAIDU-ERNIE | 本轮Blog May09→Apr30及官方ERNIE repo/release，唯一release经API核为2025-06-30非本窗；[ORG B3](../_sources/daily-20260606/SUP_ORG_20261025.md) | 已检查 | 当前可读入口未见Jun05事件，不扫普通commits |
| SRC-XIAOMI-MIMO | Paper Jun29→Mar13；已恢复官方Blog route日期May30→Jun08→Jun10，另实际读[Model Release](https://mimo.mi.com/docs/en-US/updates/model)单页Sep22→Jun02 ASR→Apr23，越过Jun05无目标项 | 已检查 | 部分CSR正文仍仅壳，不冒已读机制；模型日期已由可读官方release目录补齐，不再保留未知当日发布请求 |
| SRC-MINIMAX | 本轮中文Blog Jun09→Jun01目标邻段；agent techblog全页只Sep/Oct，有限英文date补检未恢复不同事件；[ORG B3](../_sources/daily-20260606/SUP_ORG_20261025.md) | 已检查 | 依据当前可读中文研究目录；techblog历史删除/旧稿不作穷尽保证 |
| SRC-ARXIV | [模型主题NAV](../_sources/daily-20260606/SUP_MODEL_DISCOVERY_20261025.md)87标题单页无next只导航；[有限发现](../_sources/daily-20260606/SUP_FINAL_DISCOVERY_20261025.md)日界差额0、系统/Agent28、多模态9均单页无next，官方DC仅05495–06438邻段，IR月页无日组即止。R29/R31具名题摘/date/准入及本轮必要差额已处理，不扩大87/整月为逐项队列 | 已检查 | 仅上述主题/有限标题范围，R37有限停止/具名差额独核通过，不宣全分类召回；05254与06556公开日期跨窗隔离不支撑本日覆盖，05633官方撤回排除 |

机构各行记录本轮真实范围；受阻历史目录不支持覆盖或无遗漏断言，恢复只重开具名目录/日期，不以反复访问空壳代替证据。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Kimi Code 0.11.0](https://github.com/MoonshotAI/kimi-code/releases/tag/%40moonshot-ai/kimi-code%400.11.0) | 2026-06-05T18:26:45+08:00 | 层级 sub-skill discovery 与固定 subagent timeout 把 capability lookup 与 delegation budget 显式化；2+1+2=5 | 标准完成 | 已有覆盖：`AGENT-PLATFORM` — [章节](../../../../books/part-07-agent/84-agent-platform.md) |
| [WorldFly](https://arxiv.org/abs/2606.06147v1) | 2026-06-05 | 历史条件reactive策略在遮挡/急转下受限，video/action双分支coupled flow给出需核验的联合预测替代；2+2+2=6 | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA` — [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)，共享求解时钟非物理控制时钟窄段，R3唯一实际POST通过 |
| [RH+](https://arxiv.org/abs/2606.05511v1) | 2026-06-05 | PIM行映射/row-cycle可遮蔽power间隔，需先定位实际memory瓶颈再改命令布局；2+1+2=5 | 深入完成 | 整合：`INFER-GPU-MEMORY` — [Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md)，R6唯一actualPOST通过 |
| [Tangram](https://arxiv.org/abs/2606.06302v1) | 2026-06-05 | head-group页/静态预算与AOT使nonuniform逻辑压缩兑现物理回收，但postcompression形状不等峰值；保原2+2+2=6 | 深入完成 | 整合：`INFER-PAGED-ATTENTION` — [Ch47](../../../../books/part-05-inference-system/47-pagedattention.md)，R8唯一actualPOST通过 |
| [NVSHMEM](https://arxiv.org/abs/2606.05951v1) | 2026-06-05 | GPU发起与真实进度路径分离，collective作用域/team同步资源限制多CTA并发；保原3+3+3=9 | 深入完成 | 整合：`TRAIN-DISTRIBUTED-TRAINING` — [Ch36](../../../../books/part-04-training-system/36-distributed-training.md)，R10唯一actualPOST通过 |
| [Vortex](https://arxiv.org/abs/2606.06453v1) | 2026-06-05 | paged对象携带sequence/page映射跨operator传播，auxstat身份须独立于KV共享核验；保原3+3+2=8 | 深入完成 | 整合：`INFER-PAGED-ATTENTION` — [Ch47](../../../../books/part-05-inference-system/47-pagedattention.md)，R12唯一actualPOST通过 |
| [RedKnot](https://arxiv.org/abs/2606.06256v1) | 2026-06-05 | chunk换prefix后的headwise有效性/repair责任不同，位置对齐不等上下文恢复；保原3+3+3=9 | 深入完成 | 整合：`INFER-KV-CACHE` — [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)，R14唯一actualPOST通过 |
| [QCFuse本次扩展](https://arxiv.org/abs/2606.05875v1) | 2026-06-05 | 重要修订：与2604.08585同family的扩展事件，独立span标签校准anchor与层预算；不重复评分，旧05875六分仅保历史字段 | 深入完成 | 整合：`INFER-KV-CACHE` — [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)，R16唯一actualPOST通过；不双算早稿与本事件 |
| [Google Agentic RAG](https://research.google/blog/unlocking-dependable-responses-with-gemini-enterprise-agent-platforms-agentic-rag/) | 2026-06-05 | 相对旧binary sufficiency，具体gap反馈驱动rewrite/跨源再检索；2+2+2=6 | 标准完成 | 已有覆盖：`AGENT-RAG` — [Ch76](../../../../books/part-07-agent/76-rag.md)，R17实际gap/范围/停止与预算退路具体NC通过 |
| [Consistency Training Along the Transformer Stack](https://arxiv.org/abs/2606.05817v1) | 2026-06-05 | 内部MLP/attention target分责及干预可见位置/多轮clean对应条件；2+2+2=6 | 深入完成 | 整合：`TRAIN-SFT` — [Ch29](../../../../books/part-04-training-system/29-sft.md)，R20必要/PRE→A27真存/自读→R22唯一actualPOST通过 |
| [VSRAQ](https://arxiv.org/abs/2606.05688v1) | 2026-06-05 | PTQ校准把原选值/排序/有限边界分别约束，不以重构接近代替路由稳定；2+1+2=5 | 深入完成 | 整合：`INFER-TENSORRT-LLM` — [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)，R23必要/PRE→A29真存→R24唯一actualPOST通过 |
| [SlidingServe](https://arxiv.org/abs/2606.05933v1) | 2026-06-05 | 当前最大可行chunk不等两轮效率最优，batch共同完成约束风险anchor选择；2+2+2=6 | 深入完成 | 整合：`INFER-SCHEDULING` — [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md)，R25必要/PRE→A31真存→R26唯一actualPOST通过 |
| [Steering Vectors are an Adversarial Attack Surface](https://arxiv.org/abs/2606.05958v1) | 2026-06-05 | 不改checkpoint的辅助文本/向量派生一致不证明runtime行为安全；2+2+2=6 | 深入完成 | 整合：`PLATFORM-SECURITY` — [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，R27必要/PRE→A33真存→R28唯一actualPOST通过 |
| [ToolChoiceConfusion](https://arxiv.org/abs/2606.06284v1) | 2026-06-05 | nominal合同/goal路径当前frontier菜单，不以可执行代当步有用；2+1+2=5 | 深入完成 | 整合：`AGENT-TOOL-CALLING` — [Ch78](../../../../books/part-07-agent/78-tool-calling.md)，R30必要/PRE→writer root真存→R32唯一actualPOST通过 |
| [WebMCP](https://arxiv.org/abs/2606.06387v1) | 2026-06-05 | 动态presence与metadata framing改变发现/调用连续身份；2+2+2=6 | 标准完成 | 已有覆盖：`AGENT-MCP` — [Ch83](../../../../books/part-07-agent/83-mcp.md)，R35实际metadata/update/tool-set/browser principal/effect分责具体NC通过 |
| [SET](https://arxiv.org/abs/2606.05495v1) | 2026-06-05 | 预备graph跨worker窃取须重绑buffers、stream末完成才归还；2+1+2=5 | 深入完成 | 整合：`INFER-TENSORRT-LLM` — [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)，R33必要/owner→真实保存→R34唯一POST通过 |
| [Let It Be Simple: One-Step Action Generation](https://arxiv.org/abs/2606.05737v1) | 2026-06-05 | 保velocity/CFM而向noise端偏训练time，支持条件与horizon限制单步替代；2+1+2=5 | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA` — [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)，R33必要/owner→真实保存→R34唯一POST通过 |
| [From Reward-Hack Activations to Agentic Risk States](https://arxiv.org/abs/2606.06223v1) | 2026-06-05 | latent activation与下一action风险用entropy/context校准，非单调反例限制单信号；2+1+2=5 | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` — [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，R35实际sensor人口/step/干预分责具体NC通过 |
| [HarnessFix](https://arxiv.org/abs/2606.06324v1) | 2026-06-05 | trace+code归一step证据→flaw/spec→受限patch与目标/回归双验收；2+2+2=6 | 标准完成 | 已有覆盖：`AGENT-PLATFORM` — [Ch84](../../../../books/part-07-agent/84-agent-platform.md)，R35实际fault-localized patch/回归/fixed consumer/promotion双gate具体NC通过 |
| [Autoregressive Diffusion World Models for OPE](https://arxiv.org/abs/2606.05558v1) | 2026-06-05 | Agent/WM因果交替与policy-guided transition提供OPE替代，但exact-target桥和实际估计器冲突；2+2+2=6 | 争议 | 暂缓：`MULTIMODAL-WORLD-MODELS` — [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)，R35中心反例与隔离通过，不正采/不入Books；具体重开条件见§5 |
| [LLM-Based Porting of Optimized C++ to CUDA](https://arxiv.org/abs/2606.06063v1) | 2026-06-05 | CPU向优化结构可先简化再GPU移植，Direct-3及成功条件反侧限定采用；2+1+2=5 | 深入完成 | 整合：`INFER-TENSORRT-LLM` — [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)，R35必要/owner→真实保存→R36唯一实际POST通过 |

当前21个已准入唯一family均已处置：实际整合15、具体已有覆盖5、中心争议隔离1。争议项不是正面Evidence通过；不因同family不同事件双计，也不覆盖任何旧候选评分。

## 4. 证据与知识整合

### [Kimi Code 0.11.0](https://github.com/MoonshotAI/kimi-code/releases/tag/%40moonshot-ai/kimi-code%400.11.0)

官方 release 支持实验性 sub-skill inventory/consolidation、built-in skill 命令与固定 30 分钟 subagent timeout；它只证明公开版本行为，不证明层级划分正确、超时恢复完整或跨 workload 的收益。`AGENT-PLATFORM` 已要求 capability/skill identity、activation、evaluation 与 lifecycle，`AGENT-MULTI-AGENT` 已要求 delegation timeout/handoff，因此 No Change。其余采样参数和 UI patch 作为版本事实关闭。

arXiv 空分母仍由月份级 DOI/announcement owner 对账与本日 0-row packet 支持；撤回家族没有残留正向采用链。

以上连续证据块原样保护，仅说明旧轮原小时窗判断，不作本轮自然日零命中结论。新增证据按本轮作者记录继续；官方撤回版本仍不入选、不评分、不写Books。

### [WorldFly](https://arxiv.org/abs/2606.06147v1)

精确v1必要§3–7/A–B及关键反侧、正式6分与实际owner对照见[必要包](../_sources/daily-20260606/SUP_WORLDFLY_SOURCE_OWNER_20261025.md)。为实际长期窄gap加深读足共享noise/物理time、primitive解码及消融/延迟反侧，不以分数强制停在摘要式标准审阅。[独核R1–R3](../_sources/daily-20260606/SUP_REVIEW_20261025.md)已分别通过准入/联合日证、必要/原PRE与唯一实际写后复核；作者按root本轮新窄授实际保存Ch26共享时钟至primitive授权边界单段并完整自读，实际I1生效。局部模拟、重训消融或不相容延迟/Hz口径不外推为因果、真实控制安全或实时能力；其余本日来源与候选普通工作不因此完成。

### [RH+](https://arxiv.org/abs/2606.05511v1)

精确v1 §II–VI必要机制、功率/row-cycle区分与直接反侧见[必要包](../_sources/daily-20260606/SUP_RH_SOURCE_OWNER_20261025.md)。正式5分，但对瓶颈解释修正与实际Bookgap加深审阅；原多channel时序/局部聚合未闭、浮点累加非逐bit等价、Attention/KV剩余费用及模拟非芯片/服务SLO均保正文。[R5–R6](../_sources/daily-20260606/SUP_REVIEW_20261025.md)必要/收窄PRE及唯一actualPOST已通过，root新窄授后真实保存Ch54两段/本人注并完整自读，新增I2生效，不授整日完成。

### [Tangram](https://arxiv.org/abs/2606.06302v1)

保原6分与原候选归属，原有效机制摘要复用；旧NC摘录为idle-HBM借用而非head-group分页，不能沿用。必要缺层、actualCh47唯一owner与受限KV双份/groupmax/page/transient/reserve、profile/CTA/全费边界见[本次必要包](../_sources/daily-20260606/SUP_TANGRAM_SOURCE_OWNER_20261025.md)。[R7–R8](../_sources/daily-20260606/SUP_REVIEW_20261025.md)必要/原两段PRE及唯一actualPOST通过，作者按root本轮fresh窄授真实保存并完整自读，实际新增I3生效，仅行政同步不第三研究。

### [NVSHMEM](https://arxiv.org/abs/2606.05951v1)

精确v1必要域与原9分、actual Ch36小gap见[必要包](../_sources/daily-20260606/SUP_NVSHMEM_SOURCE_OWNER_20261025.md)。[R9–R10](../_sources/daily-20260606/SUP_REVIEW_20261025.md)通过必要/原两段PRE及唯一actualPOST，作者A13真实SAVE与完整自读已闭，新增I4生效。主要分析3.3.9与引用文档3.5.19分开；GPU发起不等CPU-free，特定on-stream多CTA须满足拓扑/算法与team同步资源条件。保全费、remote反侧/timeout、GIN转述非本次重跑及显式完成，不授所有版本、训练step或SLO。这里只行政采用既成结果，旧归属不搬。

### [Vortex](https://arxiv.org/abs/2606.06453v1)

Vortex精确v1必要/原8/actual Ch47小gap见[必要包](../_sources/daily-20260606/SUP_VORTEX_SOURCE_OWNER_20261025.md)；R11原两段PRE→A16真实SAVE/完整自读→R12唯一actualPOST已闭，新增I5生效。只分页对象跨operator metadata与auxstat身份，不重复Ch49编译；保batch/shape支持、approxTopK有损、质量预算、channel表文矛盾与费用，不授prefix统计自动共享、无损或服务SLO。仅行政采用，未授整日完成。

### [RedKnot](https://arxiv.org/abs/2606.06256v1)

本次[必要包](../_sources/daily-20260606/SUP_REDKNOT_SOURCE_OWNER_20261025.md)保原9与旧有效机制/条件；R13必要/actual Ch45小gap/原两段PRE→A18真实SAVE与完整自读→R14唯一actualPOST已闭，新增I6生效。只headwise PIC有效性与repair责任，不以位置对齐证明上下文恢复；shallow-global/segment聚合未闭不照录recipe，FFN为token选择，micro/未集成布局的服务切片/容量投射分开，offline准备和全费保留。未核代码/复现，不授无损、跨机或服务SLO。

### [QCFuse本次扩展](https://arxiv.org/abs/2606.05875v1)

与2604.08585同family的重要扩展事件，不新增家族或重复评分。[事件包](../_sources/daily-20260606/SUP_QCFUSE_EVENT_20261025.md)及R15事件/受影响必要/actual Ch45单段PRE、A20真SAVE/完整自读、R16唯一actualPOST已闭。旧Knorm/单层主机制保留，新增span-label固定预算证据校准；coverage非最终质量、三个预算分责、Top3默认/Top1消融未闭和offline/完整PIC全费俱在。不借当前repo后续扩充回填本精确事件，非全局首公开或SLO保证。本窗需要的事件已整合，不再列普通待办。

### [Google Agentic RAG](https://research.google/blog/unlocking-dependable-responses-with-gemini-enterprise-agent-platforms-agentic-rag/)

[本项必要/具体NC包](../_sources/daily-20260606/SUP_GOOGLE_RAG_20261025.md)区分旧binary sufficiency与本次Reason/Feedback→rewrite/跨源检索；正式6/必要/实际Ch76已有覆盖已R17通过，不新I、不改书。该章实际gap状态/micro-query/独立sufficiency gate与scope/critique/stop、预算退出已承载本次机制；有界是项目采用边界，不冒充Blog已实现最大轮数或预算合同。FramesQA作者多组件对照/LLMjudge不隔离sufficiency因果增益，不采宣传无遗漏/审计或性能保证。

### [Consistency Training Along the Transformer Stack](https://arxiv.org/abs/2606.05817v1)

[必要包](../_sources/daily-20260606/SUP_CONSISTENCY_SOURCE_OWNER_20261025.md)限定exact-v1 §3–7及D/E/H/I直接反侧；正式6分，R19日证/准入、R20必要/actual Ch29小gap与原两段PRE、A27真存/完整自读、R22唯一actualPOST已闭。只采attention-only适配下内部读出分责、后置prefill对matched prompt因果不可见与多轮无逐一clean参照；不等adapter永远零梯度。跨威胁负迁移、选中patch/in-sample人口、能力表文口径差额及全费限界保留，未核图像素/代码或复现；I8为进度，不授整日完成。

### [VSRAQ](https://arxiv.org/abs/2606.05688v1)

[必要包](../_sources/daily-20260606/SUP_VSRAQ_SOURCE_OWNER_20261025.md)限定exact-v1 §3–6/式1–18/表1–5与caption；正式5分，R23必要/actual Ch49 gap和原两段PRE→A29真存/完整自读→[R24唯一actualPOST](../_sources/daily-20260606/SUP_REVIEW_20261025.md#r24--vsraq-05688唯一actual-post)已闭，I9生效/窄位释放。只离线value/原选次序/有限boundary目标，不是新runtime算法；保组件反退、Jaccard非输出/安全、2/3bit future、未披露运行条件与全费，不授无损或生产SLO。未核图像素/代码/复现，不第三已核层。

### [SlidingServe](https://arxiv.org/abs/2606.05933v1)

[必要包](../_sources/daily-20260606/SUP_SLIDINGSERVE_SOURCE_OWNER_20261025.md)限定exact-v1两轮预算/Alg1–2与关键表/直接反侧，正式6分；R25必要/actualCh56最小gap/原两PRE→A31窄授真存/完整自读→[R26唯一actualPOST](../_sources/daily-20260606/SUP_REVIEW_20261025.md#r26--slidingserve-05933唯一actual-post)已闭，I10生效/窄位释放。有限两轮搜索不等全局最优，入batch不等TTFT保护，保tail反退/过期降级、预测均值非尾界与全请求/运行资源资格、数字口径差额及全费；未核图像素/代码/复现，不授硬SLO或公平保证。

### [Steering Vectors are an Adversarial Attack Surface](https://arxiv.org/abs/2606.05958v1)

[必要包](../_sources/daily-20260606/SUP_STEERING_SOURCE_OWNER_20261025.md)限定exact-v1核心与关键反侧，正式6分；R27必要/actualCh72小gap/原单PRE→A33真存/完整自读→[R28唯一actualPOST](../_sources/daily-20260606/SUP_REVIEW_20261025.md#r28--05958唯一actual-post)已闭，I11生效/窄位释放。派生一致与良性属性不足以授安全；绑定文本/向量与模型、层/强度/应用协议，保弱stealth combo、norm反侧、有限judge/投影残余、符号/费用口径差额和全费。未核图像素/代码/证书实现，不授普遍防御或生产SLO。

### [ToolChoiceConfusion](https://arxiv.org/abs/2606.06284v1)

[必要包](../_sources/daily-20260606/SUP_CMTF_SOURCE_OWNER_20261025.md)限定exact-v1 §3–9/Alg1/T1–4，正式5分；R30必要/actualCh78单PRE→**writer root** fresh窄存→[R32唯一actualPOST](../_sources/daily-20260606/SUP_REVIEW_20261025.md#r32--cmtf-06284唯一actual-post)已闭，I12生效。nominal变量/goal路径不认证真实因果、删除effect或权限；保单gold/单tool/mock六步/四API人口、fullpath成功持平及未验recovery/全费，未核图像素/代码/复现。jun06_continue仅行政同步，不虚记本人SAVE。

### [WebMCP](https://arxiv.org/abs/2606.06387v1)

[必要/实际Ch83具体NC](../_sources/daily-20260606/SUP_WEBMCP_SOURCE_OWNER_20261025.md)限定第三方script已获执行权限后的presence/metadata威胁，保timing表与概括不齐、字段对照混杂、proxy模拟origin gate及baseline只限制sink不消除误选；不授完整browser安全或防御充分。R35正式6/必要与实际Ch83的description更新失效、tool-set/update admission、browser principal/调用时序及effect gate具体已有覆盖通过，不新I。

### [SET](https://arxiv.org/abs/2606.05495v1)

[必要与owner包](../_sources/daily-20260606/SUP_SET_ONESTEP_SOURCE_OWNER_20261025.md#set-260605495v1)实际读§3–5/Alg1–3与T1–2，正式5分并为小gap加深。R33通过后真实保存Ch49完整rolling费用段之后/Moira之前，只补graph跨worker窃取后的buffer重绑定与完成callback回收；R34唯一实际POST通过，I13生效。保queued executable/in-flight更新隔离未闭、steal遍历非全O(1)、六workloads与单/多stream基线差和全费，不授LLM服务净加速/并发安全。

### [Let It Be Simple: One-Step Action Generation](https://arxiv.org/abs/2606.05737v1)

[必要与owner包](../_sources/daily-20260606/SUP_SET_ONESTEP_SOURCE_OWNER_20261025.md#one-step-action-260605737v1)实际读§3–5/A/B/D/E/F，正式5分并为小gap加深。R33通过后真实保存Ch26完整MM-ABC组后/learned初始化前，训练time采样分支不同于既有fixed-point/probe、endpoint head/初始化/corrector；R34唯一实际POST通过，I14生效。保条件均值可平均不兼容动作、高noise伤多步/过强反退、长horizon/state/replanning人口与真机5trial边界；step数不等实际执行或deadline。

### [From Reward-Hack Activations to Agentic Risk States](https://arxiv.org/abs/2606.06223v1)

[必要/实际Ch66具体NC](../_sources/daily-20260606/SUP_RISK_HARNESS_SOURCE_OWNER_20261025.md#risk-states-260606223v1)保episode-grouped CV、环境标签与activation/entropy/context分责；explicit-exploit上context不普胜、mixed adapter行为不单调、WebShop只有saved predictor、steering不等完整防御。R35正式5/必要与内部sensor/deployment-slice/step/Observe-Locate-Intervene实际正文承载通过，不为再添feature组合或安全警句制造diff，不新I。

### [HarnessFix](https://arxiv.org/abs/2606.06324v1)

[必要/实际Ch84具体NC](../_sources/daily-20260606/SUP_RISK_HARNESS_SOURCE_OWNER_20261025.md#harnessfix-260606324v1)实际读III–VI/TII–VI与AppWorld例，正式6分。HTIR来源/控制流/effect证据、归层flaw/spec与双验收是实际实现；LLM归因非oracle、flaw减少仍依归因、relative改善不等百分点、相同base不等同预算。R35实际Ch84 fault-localized patch/section regression/fixed-backbone与promotion双gate具体已有覆盖通过，不新I。

### [Autoregressive Diffusion World Models for OPE](https://arxiv.org/abs/2606.05558v1)

[必要与中心争议包](../_sources/daily-20260606/SUP_ADWM_SOURCE_DISPUTE_20261025.md)保6分与准入，不因反证删候选。§4.1/C删掉behavior-policy分母后仍宣精确恢复target law，单步两action反例可复算；主文policy-loglik gradient/累计reward与Alg2 success-bank cosine gradient/max cosine估计不一致，不能拼作已验证OPE。局部rank/五epsilon控制、单次WM训练与300GPUh边界仍保留；R35直接核C式19–23/Alg2确认两条中心冲突与隔离，不入Books、不授正向OPE能力，不把已读争议称访问失败或普通未读。

### [LLM-Based Porting of Optimized C++ to CUDA](https://arxiv.org/abs/2606.06063v1)

[必要与owner包](../_sources/daily-20260606/SUP_DEOPT_SOURCE_OWNER_20261025.md)实际读III–VI/TI–II，R35正式5/必要与具体Ch49小gap通过，已原单段真实保存于完整CuIR end后/MoE H3前并完整自读；R36唯一非writer实际POST通过，I15生效。只补CPU结构先简化再GPU迁移这一替代，非现有保GPU源结构的CuIR；保Direct-3是performance非feasibility等预算控制、成功条件median与失败率/总搜索费分开、kernel/model反退，GH200/event timing不含传输/验收。

## 5. 缺口与下一步


本窗无剩余可执行工作。R37完整日级独核通过；R34/R36全部实际写后、R35三个具体NC与ADWM中心争议隔离直接采用。Hunyuan官方All恢复已为本日实际执行，空壳不再作为该路径受阻理由；没有普通未读Methods、日期解析或已知具名AB差额，不扩87/NAV或整月队列。

以下为本窗具名终态保留项，均不用于正面证据、Books或无遗漏断言，不授正面Coverage/Evidence/Books Gate或零命中保证；定点重开条件为下列原始材料到达，仅重开指定项：

- **Flash-WAM 2606.05254v1公开日期未定**：最早Jun04公告界至Jun05 registered跨BJT日，缺官方Jun04/05带日announcement或其他适用原始公开界；此前registered/current-v2不解该界，未评分/不入本窗确定候选/不入Books。
- **Robots Need More than VLA and World Models 2606.06556公开日期未定**：原联合界跨Jun05–08，缺该精确v1带日官方公告或适用更窄公开界；不判定窗外，也不以题名主题关联正采，重开仅此日期资格。
- **ADWM 2606.05558v1中心争议**：缺作者精确勘误/可核实现解释behavior density与target-law、实际guidance/value两条冲突及匹配baseline/GT；R35已读反例成立，不是访问故障或尚未审阅。保6分/候选但不正采OPE收益/安全、不入Books。
- **SRC-GOOGLE-AI / Google Research publications Jun05历史目录**：官方pubs URL不可达/HTTP空体，Blog有限stop不替publication；缺带日期官方原始列表/可读历史快照或具名当日发布，恢复只重开该目录/事件，不否定已核RAG。
- **SRC-META-AI / Jun05研究历史目录**：research动态提取0行，有限补检只how-to/creative非研究；缺带日期官方历史列表/原发布或可读快照，不以搜索无结果作零研究。
- **SRC-MOONSHOT / Jun05研究历史目录**：平台Blog尾止2025、官方org为无日期curated Research；已核Kimi版本事实不等研究目录覆盖。缺带日期研究列表/原发布或可读快照，只恢复缺失研究层。

**05633 AnswerPresence撤回关闭**：官方当前notice说明实验分析错误动摇核心，按R29不入选/不评分/不入Books，不把v1绕回正向链；不是外部保留请求。

R38定点恢复Qwen合法中英retrieval、Hunyuan中文All与MiMo日期入口；上述原始响应按Jun05日期独立检查，不复用其他日报的零候选结论。候选/Books与原窗口未变，当前保留项为六项，先前B6英语9项与空接口失败只保历史观察，不再作为这些可恢复入口的受阻依据。

## 6. 复核

复核者：`jun06_post_reader`本轮分批独核R1–32、root作为非本批必要包/报告作者独核R33–37（范围见[原记录](../_sources/daily-20260606/SUP_REVIEW_20261025.md)）；旧`fresh-context:canonical-owner-empty-denominator`仅保留未变化旧层。

结论：通过

全部21拟入选family的AB/date/准入与必要/处置已逐项核；实际POST R3/6/8/10/12/14/16/22/24/26/28/32/34/36及具体NC R17/35、ADWM争议R35直接复用。代表排除05564/R1、05781/R4；有撤回信号的05633由R29全核，范围外chemistry/生医WorldModels及机构非研究样本分层检查，未声称其余87/28/9标题全题摘排除。R37核当前六节/14每日来源、候选与21证据段、实际Books结果及八具名终态保留；有限0/28/9停止复用R29真实live独核，具名差额已由R31/35闭，不因未另存完整JSON补造题名或重抓。Hunyuan B6九行原字段经root实际读回/复算，本次当前All恢复通过，不认证删除稿/其他渠道无事件。完整日级验收通过，无剩普通工作；终态保留仍不授正面Coverage/Evidence/Books或无遗漏/性能安全保证。最终V3、JSON、本地链接及限定diffcheck通过，仅证明格式/一致性，不替代上述语义独核。
