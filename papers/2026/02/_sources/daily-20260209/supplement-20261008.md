# 2026-02-09 来源遗漏增量补查

执行：supplement_20260209，2026-10-08 12:30～13:06 +08:00。补充窗口：2026-02-08 ～ 2026-02-08；原窗口、原1候选行/评分/日期与连续§4以[supplement-20261008-baseline.md](supplement-20261008-baseline.md)冻结。旧完成及root旧验收不授本轮完成。本次只写本日README与supplement-20261008*，不改Books/LS/索引，不stage/commit/push。

## 有限来源与停止

全部14每日入口实际检查；不扫描每周组，没有新增固定按需清单触发。表外作者TSR代码与Qwen issue由具体命中定点触发，不展开机构GitHub全部项目。

| ID | 本次范围/停点 | 实际观察与限制 |
| --- | --- | --- |
| SRC-OPENAI | Research首屏、RSS只抽Feb06～10事件；[RSS字段](supplement-20261008-tail-fields-2.txt)、[原入口](supplement-20261008-native-tail.json) | 可见相邻Feb06/09无Feb08 RSS条目；RSS外修订不被证明无遗漏。web RSS Unsupported content-type改用直接XML，空响应未用于关闭。 |
| SRC-ANTHROPIC | Research当前首屏、zero-days原文及Feb08域内主题查询；[定点原源](supplement-20261008-specific-date.json)、[查询](supplement-20261008-first-calibration.json) | 没有恢复完整Feb08历史切片；当前zero-days无新Feb08可核更正信号，旧有效审阅不重开。card搜索命中仅Feb06修改说明不深扩。 |
| SRC-GOOGLE-AI | pubs首屏、2026/02 Blog全7日期项、DeepMind page4 Jan/Feb夹窗切片 | Google Blog Feb05/09相邻；DeepMind页4只有月标签，pubs非日期档案。[pubs原件](supplement-20261008-specific-date.json)；Google Feb03/04/05/09/10/11/17标题已有限浏览，不展开研究全目录。历史首次公开/目录外修订仍受限。 |
| SRC-META-AI | Research首屏空提取+Feb08域内主题查询；[原件](supplement-20261008-native-1.json) | 动态历史切片未恢复，受阻；不以零搜索作无发布。 |
| SRC-QWEN | 旧站首屏止Sep23 2025转qwen.ai/blog空提取；root DAY指出有限元数据可恢复后，本日实际GET api/v2/article/retrieval?type=qwen_ai&language=en-US，仅投影40个title+extra.date；[日期](supplement-20261008-qwen-native-dates.json) | 已检查有限40项，Feb03 Coder-Next/Feb10 Image2.0夹Feb08且无该日日签；不展开40body。目录外/删除/改写历史事件仍未证；#2064完整body和唯一bot评论已核，见下。 |
| SRC-DEEPSEEK | 官网首屏无日期后，root DAY指出news原生入口；本日实际打开news并直接HTML投影日期/标题/链接；[原页](supplement-20261008-deepseek-native-dates.json)、[元数据](supplement-20261008-deepseek-html-metadata.txt) | 已检查原页5动态+10研究共15日期项，研究Jan28 OCR2/Feb25 DualPath夹Feb08、动态Dec01/Apr24夹Feb08。只计实际15有日期项，不把ICP/许可证202数字或社交链接算研究。可見“查看全部”未承诺全历史；不深读原15正文，不授未列事件覆盖。 |
| SRC-MOONSHOT | Blog当前26项至Nov2025+Feb08原issue#84 API/body复核；[原件](supplement-20261008-native-1.json)、[issue字段](supplement-20261008-native-fields-3.json) | #84 created/updated均Feb08 03:06:18Z，comments0且正文/采用边界未变，原候选同事件复用。其他命中#986/#921属于Feb02/04请求及后续讨论，不转Feb08候选。当前目录不保证全部历史事件。 |
| SRC-TENCENT-HUNYUAN | Research首查空提取，浏览器恢复63.8s超时；公开POST publicList pageNum1/pageSize12/renderType0/Accept-Language zh；[实际字段](supplement-20261008-native-fields-0.json) | code0,total11,返回11；最近相邻Feb03/13。日期字段是原始publicAt/publishedAt/displayPublishTime，非全历史事件保证；旧en9差异仍保留。早先未过滤content响应被截断，仅保留有效字段快照作为本次依据。 |
| SRC-ZAI | Research当前15卡片首屏；[原件](supplement-20261008-native-1.json) | Feb02 GLM-OCR/Feb11 GLM5相邻，无Feb08卡片；目录外修订仍未覆盖。 |
| SRC-BYTEDANCE-SEED | public_papers首屏1～20/242非目标切片而停止；直接原生get_article_list_v2，count20/order_desc=true/publish_year2026/x-tt-locale US，type1 token60/80、type2 token0；[19项](supplement-20261008-finite-recovery-0.txt)、[尾2项](supplement-20261008-tail-fields-1.txt)、[Blog14项](supplement-20261008-finite-recovery-1.txt) | type1 total82返回19+2,next80/空,尾has_morefalse；type2 total19返回14,has_morefalse。SAGE/Protenix目录均Feb09标签（1770566400000），不新增Feb08事件。仍有19/20与14/19差额，不授完整覆盖。其余日期仅路由/窗外，不逐篇队列。 |
| SRC-BAIDU-ERNIE | Blog第一页10项止Nov2025；[原件](supplement-20261008-native-2.json) | Feb06 ERNIE5与Apr15相邻，无Feb08卡片；不证明目录外修订。 |
| SRC-XIAOMI-MIMO | Paper当前8日期项+Blog15卡片；[原件](supplement-20261008-native-2.json) | 本次Paper已给HySparse Feb03、ARL Mar13（与原无日期快照不同）；无Feb08纸目录卡片。Blog日期仍未恢复，不外推全历史。 |
| SRC-MINIMAX | English全部当前12项、Chinese全部13项与Agent Tech Blog最小索引；[英/Agent](supplement-20261008-title-abstracts.json)、[中](supplement-20261008-native-tail.json) | 英Jan27与Feb12/14，中Jan28与Feb12夹窗。Agent历史日期未恢复；中英日期差异不改变Feb08处置，也不授所有事件覆盖。 |
| SRC-ARXIV | 官方availability表、两轮各四主题日期查询、有限CL/DC列表恢复尝试及AI月首25标题发现；[查询/失败](supplement-20261008-themes.json)、[第二轮/标题](supplement-20261008-bounded-titles.json)、[公告规则](supplement-20261008-first-calibration.json) | Feb08 BJT无常规公告时槽仅作背景。CL/DC Cache miss；AI1～25系月初00053～00574非Feb08切片，立即停止，不读25完整AB或当作本窗/全月队列。第二轮仅返回交通拥堵定价2602.21495（标题明确范围外、且Feb25），不按调度类比收入。没有证明全网/作者网站零发布。 |

四主题第一轮共同前缀`site:arxiv.org "2026" "Feb 8"`，分别：(transformer OR language model OR mixture of experts OR reinforcement learning)、(multimodal OR world model OR vision language OR diffusion OR VLA)、(inference OR GPU OR kernel OR distributed training OR KV cache)、(agent OR planning OR tool calling OR RAG OR memory)。第二轮共同前缀`site:arxiv.org/abs/ "8 Feb 2026"`，分别：(LLM OR Transformer OR reasoning OR optimization)、(multimodal OR video OR VLA OR world model OR diffusion)、(serving OR inference OR GPU OR communication OR accelerator)、(agent OR memory OR retrieval OR planning)。每轮只读工具实际返回，不追加无限分页/90天catchup。机构日期查询按first-calibration.json四组原域限定Feb08，排名与搜索日期不充当公告证据。

## 具名筛选及首批准入独立校准

1. **TSR-Adam 2602.08007v1**：完整题摘实际读于[core-fields](supplement-20261008-core-fields.json)；主线范围为foundation-model data-parallel同步，潜在准入理由：单边低秩通信仍传O(rn)、refresh峰值可能主导 → 双边UᵀGV r² core同步、低维moment、randomized-SVD refresh与embedding专用rank/schedule → 需要重新考虑带宽受限优化器的通信/状态与峰值预算。只根据摘要判断潜在贡献，未采用13×/25×性能或理论结论。官方[v1] Sun Feb08 15:23:09 UTC是Submitted。作者[repo](https://github.com/DKmiyan/TSR-Adam) createdJan28；[有限4提交](supplement-20261008-finite-recovery-2.txt)Jan28及May07，[Jan28 README](supplement-20261008-finite-recovery-3.txt)已有TSR训练示例但无论文正文/Feb08发布声明。Git提交/仓库创建不证明论文首次公开，也没有本窗新artifact事件。当前只缺公开日期，隔离、不评分/不深审/不Books。需要作者同稿公开正文日期或官方公告批次；到达后只重开此材料身份/日期，确认Feb08才正式候选。数据注册及ArXivSignals Feb10线索不当原始日期证据。
2. **MoE Survey 2602.08019v1**：完整题摘[title-abstracts](supplement-20261008-title-abstracts.json)仅扩展MoE综述到去中心化/领域应用/挑战；未新增具体机制、有效性条件或修正设计选择的验证/反证，因此贡献前关闭。期刊2025引用与Submitted Feb08均不影响这一理由，不为不采用项追查日期/深审。
3. **Qwen #2064**：由机构查询触发，完整[API/body](supplement-20261008-tail-fields-0.txt)createdFeb06 18:47:34Z=BJT Feb07，用户称图像编辑过饱和与UI选项消失，但无可核模型/配置对照、原因或新增修复机制。当前唯一[评论](supplement-20261008-qwen-comment.txt)为Mar09 inactive bot，未出现本窗新纠错/安全/机制事件。不是忽视负面结果，而是未形成可改变系统选择的局部证据；贡献前关闭并记窗前身份。
4. **Kimi #84**：原确定家族，同created/updated/body/0评论，原安全限定审阅与仅报告有效，复用而不增加家族。#986 hooks为旧请求、后续PR1131在Feb14；#921原Feb04网络故障疑问，未发现Feb08新机制，窗前/窗后身份线索不扩本日。

root已实际读1/2完整题摘，2026-10-08首包校准通过：TSR具体通信潜在增量成立，但日期先行隔离；MoE扩覆盖综述关闭成立；Sunday无常规批次只作发现背景，不能证明作者未发布。当时其余源/六部分待root独立DAY，不借此首包授全部完成；最终结果见下。

## 日级终态

确定新增候选0，原1保持，候选表合计1；没有新Source深入/标准审阅或新Books决定，因为唯一潜在增量尚未过日期门。TSR与机构历史缺段终态隔离，不支持Coverage/Evidence/无遗漏；原SAGE留原窗口记录，本次只关注Feb08自然日不要求精确时刻，当前作者目录Feb09不能被搬入补窗。首轮DAY指出Qwen/DeepSeek可执行有限入口，已本日实际恢复40/15元数据并更新以上源处置，非复用其他日回执。root（独立于supplement_20260209）实际读全部六部分/14源/四主题停止、TSR/MoE完整题摘、原#84未变API/body、Qwen40和DeepSeek15原日期，独立DAY通过；未知公开日隔离不借Submitted/Sunday授0，原冻结/新0/Books0、无PRE/POST新对象。普通可执行待办0，完成仅本日，不接下一日；目录外与日期保留不授全Coverage。

本轮实际完成态V3、75个本地引用missing0、原候选行/窗口/连续整个§4逐字cmp0、限定cached/unstaged diff-check0。语义验收由root独立DAY承担，机器通过不授源日期或实验结论。未stage、commit、push。
