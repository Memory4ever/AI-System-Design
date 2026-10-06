# Daily Research — 2025-09-18

**规范：** V3
**窗口：** 2025-09-17T09:00:00+08:00 ～ 2025-09-18T09:00:00+08:00
**状态：** 进行中
**Books：** 纳入本次
**检查时间：** 2026-10-06T14:20:00+08:00

## 1. 结论

作者侧本日有限研究ready，等待root独立校准/日级复核；确定落窗候选0、相应证据完成0、Books0，不表示零事件或无遗漏。arXiv超时/429后触发辅助19标题和CL月有界新命名补检，53精确v1完整题摘实际读；14256必要安全反侧窄补后撤回其关闭，现48潜力、5明确关闭，另2明确AI for Science标题暂缓。不是本窗公开论文数或全文队列。MiMo More及Seed论文分页本日已真实窄执行到底，必要历史日期/数组仍隔离。

潜力包括CoT早停/剪枝全成本、embedding训练目标、稀疏歧义神经元、视觉tokenization的时间保真、shutdown instruction失败和组合隐私。Google SLED旧稿/旧代码不重算，新模型验证及Sensible Agent的what/how与两阶段确认代价可能有局部增量，但缺原公开落窗证明。官方RSS将OpenAI scheming Blog明确排到17日报，不把未审事件冒成18日已审重复。没有复现实验、生产保证或共享Books改动。

## 2. 来源覆盖

实际请求/原响应与停止依据见[FETCH](../_sources/daily-20250918/FETCH.md)及本日18*.json；只声明保留切片，不授全站/全学科召回。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | Research403；官方RSS本日HTTP200共1247item按UTC本窗过滤0，具名scheming核心核原00:00 GMT窗外 | 已检查 | 仅RSS/具名发布切片；不是全站修订无遗漏 |
| SRC-ANTHROPIC | 本日Research Next JSON恢复172 publication，保留publishedOn，UTC09/17 01～09/18 01过滤0 | 已检查 | 仅保留Research切片，不保证删除历史 |
| SRC-GOOGLE-AI | Research/Pubs/DeepMind原入口；官方9月Blog实际page1十二标题至Sep11越下界，SLED/Sensible核心与原身份定点核 | 受阻 | Blog切片可读，日期无TZ；Pubs/DeepMind历史公告未恢复，page2失败不记已读 |
| SRC-META-AI | 本日Research连接重置，严格Sep17主线官方补检无结果即停 | 受阻 | 无原历史分页/公告，不能记零论文 |
| SRC-QWEN | 本日Blog及新page_config API独立HTTP200原60date配置；只筛UTC17T01→18T01为0，NextSep10T20Z/TTS21T20Z夹窗 | 已检查 | 本日原capture，不继承其他日coverage或将60正文排队 |
| SRC-DEEPSEEK | 本日主站updates实际404；官方API文档Change Log HTTP200，实际Sep22→Aug21越下界停止 | 已检查 | 保留更新切片没有本窗条目，不授全机构历史完整性 |
| SRC-MOONSHOT | 本日Platform原Blog日期序列Sep16计费/Sep5更新已越下界 | 已检查 | 有限保留Blog，不以当前仓库证明历史修订 |
| SRC-TENCENT-HUNYUAN | Research shell与正确publicList POST全部9条当前记录 | 受阻 | API最早2026不能支持9月历史“全部”；不伪0研究 |
| SRC-ZAI | 本日Research真实page2累计18/hasMorefalse，最早Dec07 | 受阻 | 没保存9月切片，不能用当前release替代论文目录 |
| SRC-BYTEDANCE-SEED | type2/year2025/token0真实15/49，非置顶跨Aug21/Jul14按下界止；type1真实0/20/40/60/80，80 has_more=false/next空 | 受阻 | Blog有限窗已处理；papers total94仅20返回旧06/12 SwiftSpec，其他缺数组，非0或94全筛 |
| SRC-BAIDU-ERNIE | 本日Blog page1/2，Sep12PLAS/Aug14FastDeploy越下界，prev-only停 | 已检查 | 仅技术Blog切片，不授代码所有历史事件 |
| SRC-XIAOMI-MIMO | 本日Paper8条Sep19Audio/Jun4VL夹窗；本日两async chunks实际200，Blog15完整title/desc与8+7状态展开读至末尾，无额外分页 | 受阻 | More已执行，原Blog数组没有date，Paper不能授Blog历史覆盖 |
| SRC-MINIMAX | 本日原US12至Oct27、CN13至Jan15、Agent当前one2026；只读原保留日期切片 | 已检查 | CN实际跨本窗下界，撤回过宽历史缺口；不授删除历史/所有仓库覆盖 |
| SRC-ARXIV | 12分类主线主题API20秒超时；系统窄查100上限实际429；CL月重试1–2000/2214，相关ID区段13400–14400标题补查36精确v1 | 受阻 | 无官方历史日公告/首公开关系；月ID/提交/收录不授窗口，未全量题摘/全文处理库存 |
| 补检：[Hugging Face](https://huggingface.co/papers/date/2025-09-18) | API失败后一次页面十九标题，十七相关/含糊身份回原域，curl十秒超时不反复 | 已检查 | 只身份恢复，不授first-public或arXiv覆盖 |
| 表外：[Apollo](https://www.apolloresearch.ai/science/stress-testing-deliberative-alignment-for-anti-scheming-training) | 误旧路径404保留；正确science原页HTTP200/核心实际读，antischeming.ai具名关联 | 受阻 | companion日期无TZ/新事件关系未明；不把同家族已有公开机制重算本窗事件 |

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |

没有已确认落窗可列的候选；不提前给日期未核材料评分。潜力身份与精确重开位置见§5，不以空表宣称无贡献。

## 4. 证据与知识整合

[53个精确题摘筛选](../_sources/daily-20250918/DISCOVERY_SCREENING.md)与[首批校准交接](../_sources/daily-20250918/FIRST_BATCH.md)区分发现阅读、准入潜力和必要深审。主体方法/消融尚未读足，不称审阅完成。13677决定准入的auto-prompt细节另定点读了persona free-performance/evaluator筛选，保留共同judge循环与预算问题；14254 HTML404后原abs/v1完整摘要已恢复，不能报题摘不可得。

安全与设计反证不因局部证据关闭：14260 shutdown指令位置/未完成任务影响协议；13625 DP长生成必须核adjacency/accountant；14223线性训练时序只来自已知顺序六集1B模型，不能恢复任意真实训练史；13990/14004/14093的减少tokens须计查询答案、跨链相似度及Best-of-N全成本。以上没有取得本日首公开证明，不进入正面采用链。

14256 covert广告关闭撤回：精确v1必要§2.5–2.6、§3.2–3.4/Table1及§4实际窄补，原stealth metric可受未插广告影响；CrossEncoder Table1 F1 0.511与结论测试F1 0.9901的协议关系未说明，不照录高分授检测可靠性，也不直接判失实。保留安全分数/插入人口/检测口径的潜力，日期仍隔离，root定点校准。14142 MARS2完整题摘重新核后只目录/排行增量的关闭保持；不是关闭其未读方法。[精确窄交接](../_sources/daily-20250918/NARROW_SOURCE_SAFETY_HANDOFF.md)保留新证据位置与实际停止。

SLED的2411.02433v1与repo News支持旧稿/代码2024已公开，Blog新Gemma3/GPT-OSS验证不能只凭“now”当新代码，也不能因机制旧而自动排除新局部验证。Sensible Agent核心/官方Pubs完整摘要支持what/how与建议→确认的互动代价潜力；十人局部结果不是排除理由，28.5s与16.4s说明努力下降不等于更快。两者日期仍无TZ，未评分/采用。原材料见18core0/18specific/18sensible/18sensibleidentity.json。

Books正面拟增量0，实际写入0；必要公开归属缺失先隔离，不声称已经读实际owner或已有覆盖。日期取得、准入校准及证据独核后再按研究合同§6比较唯一owner实际论点和邻接，由root落实自然段落，作者不写共享Books。

## 5. 缺口与下一步

作者本日普通扫描/题摘已停在真实有界位置，root首批校准与最终日级独核仍普通待办。外部保留项不支持候选、Books、无遗漏或性能/安全保证，不以假定日期结束。

- arXiv48潜力精确v1逐项在[发现表](../_sources/daily-20250918/DISCOVERY_SCREENING.md)及[具名关闭撤回](../_sources/daily-20250918/NARROW_SOURCE_SAFETY_HANDOFF.md)，原HTML/14254v1-abs.raw为重开位置。缺真实公告/作者原始首发或完全落窗区间；submitted/DOI注册/HF收录不能替代。取得后只重开该家族日期/校准及必要方法反侧；shutdown、隐私、steering、HILL、训练时序和covert检测口径须定点风险复核，不把未读方法称已完成。
- [Google SLED](https://research.google/blog/making-llms-more-accurate-by-using-all-of-their-layers/)与[Sensible Agent](https://research.google/blog/sensible-agent-a-framework-for-unobtrusive-interaction-with-proactive-ar-agents/)：原Sep17/Sep18日期无TZ，博客事件与旧论文/代码关系不同；需原feed/带TZ元数据或原公开区间支持落窗，随后核新验证/确认成本的具体协议。原URL/www各二十秒超时与RSS失败已实际执行；不要求人为补秒。
- DeepMind/Pubs、FAIR、Hunyuan、ZAI9月Research、Seed-paper、MiMo Blog和arXiv主题公告：缺历史原数组/公开日期，实际停止见§2/FETCH及本次窄交接。Seed已真实80末页、MiMo已展开15，不能继续写未执行分页，但缺历史数组/日期仍不授覆盖。接受目标窗原归档/API正文及公开字段；shell/2026接口/空搜索不作历史阴性，只重开受影响源。MiniMax中文有限切片已跨下界，不保留过宽缺口。

窗外归属：OpenAI scheming Blog由本日RSS原`Wed, 17 Sep 2025 00:00:00 GMT`确认09/17 08:00，归17日报，不能移动到18。17日恢复其未审工作，不在本日报扩大窗口或称已审重复。Apollo companion仅同日无TZ且未见明确新修订，缺独立新事件证明时不重算已有公开机制；新重要变化到达再窄重开对应事件。

## 6. 复核

复核者：待root（非作者）。结论：未通过（首批校准/日级独核尚未实施），作者Tesla不能自授完成。

请先核主题边界、真实429/超时及月标题非队列，再核53题摘的48潜力、5关闭及两科学标题分层样本，全部安全/纠错/设计反证和日期隔离，尤其14256具名关闭撤回；SLED/Sensible增量与OpenAI窗外归属单独核。Books无采用不等于已有覆盖。V3/限定diff-check只是结构检查，不能替代语义验收；未改共享Books/月README/LEARNING_STATE，未stage/commit/push。
