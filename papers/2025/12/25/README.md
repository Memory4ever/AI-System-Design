# Daily Research — 2025-12-25

**规范：** V3
**窗口：** 2025-12-24T09:00:00+08:00 ～ 2025-12-25T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-02T18:32:39+08:00

## 1. 结论

确认落窗的唯一候选家族1个：Kimi CLI 0.68，评分6分，受影响兼容性与授权路径已完成深入静态审阅。其配置来源、连接执行者和终端动作执行者的差别已融入唯一owner AGENT-MCP 的Ch83，写后独立检查通过。未运行ACP/OAuth或取消测试，不宣称生产可靠性和性能改善。

14每日源的普通可执行发现已收束。实际arXiv相关66身份打开题摘，追加13条线索的可执行题摘判断由独立复核补齐；这些不是79个唯一当窗候选或正文审阅数。必要历史目录、逐ID首公告和部分精确版本有限恢复仍缺，已安全隔离，不用于正面证据、Books、零事件或覆盖通过。本窗没有未处理的普通工作；完成表示达到合同允许的安全终态，不表示历史来源已无遗漏。

ERNIE单条排名宣传、Qwen2511仅内置selected LoRAs的事实均贡献前关闭，root已校准；不借成熟merge原则凑贡献，不因已有Books缩池。

## 2. 来源覆盖

原始固定目录邻接、查询与停止点见[DISCOVERY.md](../_sources/daily-20251225/DISCOVERY.md)，准入过程见[ADMISSION.md](../_sources/daily-20251225/ADMISSION.md)。隔离不是Coverage通过。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [Research](https://openai.com/research/)当前2026，直接403；官方限定12/24及December2025补检 | 受阻 | 原始历史日切片不可得，已隔离；搜索不证明零 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research)前十项2026/See More同列表；另[Alignment Blog](https://alignment.anthropic.com/)December六项到November，原文12/19→12/08邻接 | 受阻 | Alignment切片已恢复；主Research历史分页仍隔离，不互相替代 |
| SRC-GOOGLE-AI | [DeepMind历史Blog page4](https://deepmind.google/blog/page/4/)24项Feb26至Nov25，最新December原文12/23年度回顾；[Google Research](https://research.google/pubs/)2025筛选676项仅年粒度 | 受阻 | Blog本窗邻接已恢复，不当无命中搜索；publications日粒度仍隔离 |
| SRC-META-AI | [Publications page3](https://ai.meta.com/results/?content_types%5B0%5D=publication&page=3)12/26→12/18→12/16，page4较早段；Blog page2 12/18/12/16 | 已检查 | 到达本窗邻接；12/26记录时区未给，留真实归属恢复；不作全站零保证 |
| SRC-QWEN | 迁移提示、[Blog](https://qwen.ai/blog)动态空、公开component有限恢复、官方搜索及[2511官方卡](https://huggingface.co/Qwen/Qwen-Image-Edit-2511)核心段 | 受阻 | 2511贡献前关闭；其余本窗历史目录缺失已隔离 |
| SRC-DEEPSEEK | [主页](https://www.deepseek.com/)及[updates](https://api-docs.deepseek.com/updates)，相邻2026-04-24 V4 / 2025-12-01 V3.2 | 已检查 | 仅可见更新目录范围，不保证全部研究 |
| SRC-MOONSHOT | [Blog](https://platform.kimi.com/blog)26条自2025-11-07至2024；官方org与CLI changelog0.69/0.68/0.67邻接及0.68完整release | 已检查 | 0.68静态证据与Books已核；不外推运行验证 |
| SRC-TENCENT-HUNYUAN | [Research](https://hunyuan.tencent.com/research)公开列表page1/size1000/renderType0返回11/11，最早2026-02-03；浏览器有限失败、官方历史补检与issues线索 | 受阻 | 2025历史未保存，已隔离；用户问题不当新机制 |
| SRC-ZAI | [Research](https://www.zhipuai.cn/zh/research)2026-01-13 / 12-10 GLM-TTS / 12-09 ASR-Nano；[release](https://docs.z.ai/release-notes/new-released)12-22 GLM-4.7 | 已检查 | 两目录分别核查，不互相替代或保证全站零 |
| SRC-BYTEDANCE-SEED | [目录](https://seed.bytedance.com/en/public_papers)公开get_article_list_v2的2025/type1论文18项total94,next20；另type2 Blog实际18项total45,next20，12/24 Prover→12/18→12/16→12/02→11/27及更早段 | 受阻 | 两类目录均查；Prover1.5核心潜在贡献已读，日编码不能授精确首次公开，具名隔离 |
| SRC-BAIDU-ERNIE | [Blog](https://ernie.baidu.com/blog/zh/)第一页2026-01-08 / 12-23 / 12-09，第二页更早，共2页 | 已检查 | 排名负侧已关闭，不将其当机制或全站零证明 |
| SRC-XIAOMI-MIMO | [Paper/Blog](https://mimo.xiaomi.com/) Paper邻接2026-01-08/2025-10-21；Blog15项、V2Flash定点与组件/官方搜索 | 受阻 | Paper段已核；Blog历史日期有限替代仍缺，已隔离 |
| SRC-MINIMAX | [英文](https://www.minimax.io/blog)/[中文](https://www.minimax.cn/blog)12/13项，2026-01-27或28 / 12-23 / 10-27；[Agent Markdown](https://agent.minimax.io/docs/techblog.md)仅2026-05-13 | 已检查 | 当前Agent目录不保证2025完整；M2.1外窗不冒称已审 |
| SRC-ARXIV | language/LLM、系统/多模态154项、Agent/RAG/memory61项提交身份查询；[cs.CL](https://arxiv.org/list/cs.CL/2025-12?show=2000&skip=0)/cs.DC/cs.CV相关标题有界补检；相关66身份abs打开 | 受阻 | 个体首公告与部分精确版本不可恢复，未确日线索隔离，不评分、不作零证明 |
| 表外：[ZDI MimicMotion](https://www.zerodayinitiative.com/advisories/ZDI-25-1032/) | 实际安全触发，GHSA全文→ZDI原披露→Tencent commit定点 | 已检查 | 原始12/01披露；12/24只是GHSA收录，不扩安全库 |

未扫描周级来源。HF卡仅用于已发现事件必要证据，不扫描HF全站。宽列表只是身份线索，不变成全量关闭队列。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Kimi CLI 0.68](https://github.com/MoonshotAI/kimi-cli/releases/tag/0.68) | 2025-12-24T20:40:22+08:00 | 配置来源与MCP连接执行者可分离，Shell仅能力条件下改在客户端执行；需核不同生命周期与授权owner；2 + 2 + 2 = 6 | 深入完成 | 整合：AGENT-MCP [Ch83协议比较的五类契约](../../../../books/part-07-agent/83-mcp.md#协议比较必须拆开五类契约) |

公开时间来自官方API published_at=2025-12-24T12:40:22Z，不采用created_at。首批局部校准不是本日整体验收。

## 4. 证据与知识整合

### [Kimi CLI 0.68](https://github.com/MoonshotAI/kimi-cli/releases/tag/0.68)

精确证据、必要测试与局部Books草案见[KIMI_068.md](../_sources/daily-20251225/KIMI_068.md)。Tag为d5ae5b809d19086db2d823ca6f1997bd68c3db2d。acp/mcp.py转换http/sse/stdio配置，soul/toolset.py由CLI创建FastMCP client/list_tools；并非全部MCP连接/调用移到ACP客户端。真正client执行的是Terminal：local_kaos且terminal capability为真才替换Shell，保留name/schema；create_terminal前仍请求runtime.approval，关联session_id，wait/timeout kill/current_output/finally release。普通cancel后release不证明进程停止。OAuth无token为unauthorized，不进入pending队列；reset只清本地FileTokenStorage，不等于server撤权。

已重新实际对读唯一owner Ch83 Host/Client/Server、五类契约、共享adapter与授权段，及Ch78 effect接口和Ch82/84交接。现有正文具体覆盖协议/凭据/授权分离；局部差额是配置来源、MCP连接执行者、Terminal动作执行者三个维度不能混为client delegation。主线程已在Ch83五类契约的adapter分责之后融入两段：先说明单进程合并职责为何合理，再推导外部客户端改变责任边界，接回能力协商、授权和生命周期。没有新增产品功能清单或第二owner。独立复核者Mill重新请求固定commit源码、对读前后章节并完成写后检查，记录见[实际检查](../_sources/daily-20251225/ROOT_ADMISSION_REVIEW.md#非写入者-postkimi-cli-068--ch83)。公开静态代码不证明生产安全、通用终止或性能；未本地运行ACP/OAuth测试，相关tag测试只验证diff display转换。

Qwen官方卡Showcase第147～151行仅支持选定LoRA内置及产品演示；无新增合入算法、受控收益或新适用边界，贡献前关闭，root独立重读通过。ERNIE排名负侧同样通过局部校准，不给Books“已有覆盖”充数。

已实际读[2025原始官方假日公告](https://blog.arxiv.org/2025/11/21/temporary-changes-to-announcement-schedule-due-to-end-of-year-holidays-2025/)并定点复用[日期恢复原始记录](../_sources/ARXIV_DATE_RECOVERY.md)：指定接收且接受段延期12/28 20EST=12/29 09BJT，归Daily12/30起点；12/31 20EST归January2。它不证明任何具体ID进入批次，不以Submitted补时刻。

## 5. 缺口与下一步

本窗普通可执行待办0。Seed/DeepMind历史Blog追加检查已补正过宽隔离；Kimi必要证据和Books写后检查已通过。以下外部终态保留项不支持正面证据、Books或无遗漏断言；定点重开条件逐项说明如下。

[Seed Prover1.5官方Blog](https://seed.bytedance.com/en/blog/seed-prover-1-5-advanced-mathematical-reasoning-through-a-novel-agentic-architecture)核心说明有工具调用、可复用已核lemma、sketch多信号奖励与递归并行证明的潜在设计增量；未按数学题材排除。列表/正文PublishDate均12/24北京00:00日编码，不足以证明实际上线时刻，且当前正文有后来UpdateTime。精确首次公开范围及必要历史版本为终态保留；暂不评分为确定候选、不采用Books。定点重开条件为对应Blog原始发布feed/公告或可验证上线记录和当年正文，只重开该家族的真实归属日。

本窗终态外部保留：表中OpenAI/Anthropic/Google/Qwen/Hunyuan历史日目录及MiMo Blog历史；arXiv必要首公告/精确版本不明的实际身份详见DISCOVERY.md，包括[MixKVQ](https://arxiv.org/abs/2512.19206v1)、[L4/CascadeInfer](https://arxiv.org/abs/2512.19179v1)、[UCCL-EP](https://arxiv.org/abs/2512.19849v1)、[Odysseus安全反证](https://arxiv.org/abs/2512.20168v1)等。已有限尝试官方入口、主题查询、长月身份表、catchup及字段语义替代，仍不能确认本窗。隔离不用于正面结论、Books、零事件或Coverage/Evidence通过；保留潜在贡献，不降分或删掉。重开条件为该源原始历史分页或逐ID官方new公告/可验证首次公开范围，届时只重开受影响源/ID并继续贡献、精确正文。

窗外：Qwen2511目录12/23且贡献前关闭；MiniMax M2.1 12/23、GLM4.7 12/22只交真实归属日定点，未宣称先前已审。MimicMotion原始ZDI披露12/01及11/18修复commit不是12/24新事件。Meta Safety Alignment目录12/26且时区不明，后续真实归属定点，未移到本窗。

## 6. 复核

复核者：主线程（非报告作者Feynman）；Books写后复核者Mill（agent `01a0fc18-6d14-7b60-9ba1-b6b579aaef3e`，非Books写入者）。
结论：通过

实际范围见[ROOT_ADMISSION_REVIEW.md](../_sources/daily-20251225/ROOT_ADMISSION_REVIEW.md)。

逐行核十四源与实际触发ZDI的停止范围及外部隔离；唯一确定拟入选Kimi的日期、6分与受影响精确实现全部核验。安全触发ZDI原披露和四条安全/反证v1题摘独立读取；额外13条已发现标题补正为具体潜在准入理由，不借日期豁免题摘。追加恢复Seed两类目录、DeepMind历史Blog与Anthropic Alignment切片，补读Seed Prover1.5核心并隔离具名日期，不再把可读目录称外部缺失。普通负侧按排名宣传、模型产品事实两层抽检ERNIE/Qwen两项；未无差别重读66条全部附件，日期隔离项不获得正文证据验收。Ch83两段实际写入由Mill独立定点复核通过。V3结构校验通过；链接和空白另行检查，机器结果不能代替语义依据。
