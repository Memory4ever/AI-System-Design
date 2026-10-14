# Daily Research — 2025-09-27

**规范：** V3
**窗口：** 2025-09-26T09:00:00+08:00 ～ 2025-09-27T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-06T19:52:41+08:00

## 1. 结论

本窗入选1个发布家族：function-call output支持图片/文件，精确原帖版本1与时间落窗。root已实际单项独核准入2+1+1=4、关闭进一步长期采用，仅报告provider载荷类型变化；最终日级复核范围见§6。AARP教育合作核心已读后关闭，root代表关闭校准有效。

14每日源已在本日重新执行，保留真实有界停点。arXiv原API429/重试超时保留；相同4分类+LM的12位提交发现查询已实际HTTP200两页100+34/total134后停，完整134题摘已读，20具体关闭、114仅日期潜力，不评分/采用，不把submitted当first-public。21个明确安全/保证信号的精确v1必要方法与直接反侧已按具体位置补足/复用，未将题摘称证据通过、未扩其余114全文。月表1–2000/2214仅题名线索，非队列。另A*理论潜力2509.22626v1已有root题摘校准、日期隔离。新增范围与最终DAY已由root独立核验通过；不声称零事件/无遗漏，不改共享文件。

## 2. 来源覆盖

所有原响应在[本日_sources](../_sources/daily-20250927/)，实际UTC执行时间/URL见[fetch-log](../_sources/daily-20250927/fetch-log.json)。仅metadata跨窗，不加载窗外正文作本日证据。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 原RSS1247项按本窗pubDate解析，AARP06GMT落窗；核心读完关闭。实际搜索触发工具output原帖，JSON恢复created_at/updated_at/version1 | 已检查 | 当前Function calling文档不是2025历史快照，不倒填其余兼容性 |
| SRC-ANTHROPIC | Research Flight重新解析，172唯一slug记录（去重后），原publishedOn保留于[解析](../_sources/daily-20250927/anthropic-publications.json)，无本窗字段 | 已检查 | 只支持实际数组范围，不授互联网无事件 |
| SRC-GOOGLE-AI | `/blog/2025/09/`实际首12条Sep30至Sep11，目标Sep26没有record，越窗停；pubs正确category2025/language model3页1–37/37，年份不是first-public；DeepMind原RSS实为gzip XML，现实际解压解析100项，最早Nov5；另两个RSS路径404 | 受阻 | Google论文原公开日/DeepMind目标历史目录未恢复；不是返回HTML或空RSS，当前订阅截断不能覆盖9月 |
| SRC-META-AI | Research仅title，Blog真page1–3，页3普通尾部Aug/Jul2025后停，featured/旧文使排序非单调；本日raw分别保留 | 受阻 | Research历史目录及Blog非单调历史覆盖不能认证 |
| SRC-QWEN | 旧Hugo首屏跨窗停；本日本地实际API `qwen.ai/api/page_config?code=research.research-list` 200，非时间排序完整60项数组逐一检查原date，无本窗项；[原JSON](../_sources/daily-20250927/qwen-api.json)、[元数据](../_sources/daily-20250927/qwen-api-metadata.json)、[执行](../_sources/daily-20250927/narrow-qwen-agent-fetch.json) | 已检查 | 只支持此实际数组，不授全部历史发布/修订无遗漏 |
| SRC-DEEPSEEK | 官方news侧栏18项至2024；Sep22与Sep29夹窗，实际读取metadata，不审窗外正文 | 已检查 | 限官方news侧栏，不是研究全史 |
| SRC-MOONSHOT | Kimi Blog26条metadata，2024至2025Nov，Sep16/Sep5均窗前，无More | 已检查 | 限当前官方目录 |
| SRC-TENCENT-HUNYUAN | 首查Research；正确publicList POST pageNum1/pageSize100/renderType0，code0/totalNum9/list9，public/display字段均2026，原值保留；本子代理浏览器不受支持 | 受阻 | 当前9条不授2025历史覆盖，未伪称浏览器核过 |
| SRC-ZAI | Research真page1/page2，Flight数组15/18；hasMoretrue→false，最早Dec2025；release notes Sep30/Aug11夹窗 | 受阻 | Research目标历史缺口，createAt不充first-public |
| SRC-BYTEDANCE-SEED | type2/year2025/page0/count20返回15/49/hasMoretrue，去pin后降序最早Jul15跨窗停；type1总94无列表，实际page20仅1条SwiftSpec | 受阻 | Blog有限范围已处理；paperAPI不完整，不记94条零命中 |
| SRC-BAIDU-ERNIE | 原RSS18项实际解析（16posts+2导航sentinel），本窗无pubDate，Oct16/Sep12夹窗 | 已检查 | 限官方Blog/RSS范围 |
| SRC-XIAOMI-MIMO | 首页与实际home1/home2 chunks：8papers、15blogs，More只展开同数组；paperSep19/Oct21夹窗；routes chunk实际恢复日期metadata，含undated | 已检查 | undated当前Blog/全部历史不授覆盖，不读当前正文 |
| SRC-MINIMAX | EN12/CN13可读cards，CN到Jan15，Oct27/Jan15夹窗，无More；Agent Tech Blog本日实际200，完整可读目录仅2026-05-13一篇，官方llms.txt全索引同样仅该技术文章，无历史分页后停；[Agent文本](../_sources/daily-20250927/minimax-agent-text.json)、[索引](../_sources/daily-20250927/minimax-agent-index.txt)、[请求](../_sources/daily-20250927/narrow-qwen-agent-fetch.json) | 受阻 | 公司Blog有限范围已处理；当前Agent目录不授2025覆盖，需目标历史目录或具体本窗原事件 |
| SRC-ARXIV | 原12分类API429/一次retry timeout；原retry已12位，非14位。相同4分类+LM复合12位提交发现查询200，start0/100、max100返回100+34/total134后停；134完整题摘已读，20关闭/114日期潜力，21必要安全/保证精确v1方法及反侧记录于[请求/筛选与证据位置](../_sources/daily-20250927/NARROW12_SCREENING.md)。cs.CL月表1–2000/2214仅补题名；advanced公告仍仅年月 | 受阻 | 此主题发现查询已处理，逐篇first-public仍未确认；API当前版本非一律v1，不据submitted归日、不授全类/首次公开覆盖或21项独核通过 |
| 表外：[OpenAI Developer Community](https://community.openai.com/t/images-and-files-as-function-call-outputs/1360081) | 搜索触发仅该原帖JSON及身份恢复，必要Function calling官方说明，未扫论坛 | 已检查 | 原帖仅支持发布事实，完整2025 schema未取得/未采用 |
| 补检：[web search](https://www.google.com/) | Sep26/2025-09-26/Sep26+inference，实际domains限定官方机构/arXiv，结果有community噪声，原[search](../_sources/daily-20250927/search.json)；不以搜索无命中证明无事件 | 检索受限 | 辅助索引只负责发现；回原帖/精确v1后判断 |

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Images and files as function call outputs](https://community.openai.com/t/images-and-files-as-function-call-outputs/1360081) | 2025-09-27T00:53:38.546+08:00 | 文本/JSON结果不能直接返回多模态artifact → 新支持图片/文件tool output → observation载荷选择改变；2+1+1=4（Design Delta/System Reach/Durability） | 已关闭 | 仅报告：provider接口支持类型的版本事实，不提供新的通用授权/正确性机制，不改Books |

唯一tool-output准入、AARP代表关闭与A*题摘校准及本日独立复核已通过。日期潜力不列确定候选；本窗外部保留不代表正面Coverage/Evidence通过。

## 4. 证据与知识整合

### [Images and files as function call outputs](https://community.openai.com/t/images-and-files-as-function-call-outputs/1360081)

采用原帖post1837147/version1，created_at与updated_at同为`2025-09-26T16:53:38.546Z`，未用搜索显示日期推定。原[JSON](../_sources/daily-20250927/tool-output-post.json)全文核心是tool function可返回images/files而不仅JSON/text。发帖者Edwin Arbus的OpenAI角色由其原自述与官方ack恢复；当前staff=false/Regular原值保留，不把论坛管理员标志当当时雇佣/发布权限证据。

必要读取当前官方[Function calling](https://developers.openai.com/api/docs/guides/function-calling)“Formatting results”：文字结果与image/file对象array有不同representation。该当前文档并非2025精确快照，因此不采用当前模型名、完整字段、兼容范围或安全行为作当时事实。没有benchmark、实际API执行、SDK代码核验或生产可靠性证据。

实际读`AGENT-TOOL-CALLING` [Ch78](../../../../books/part-07-agent/78-tool-calling.md)10–55：environment observation回到Context、tool identity/version与typed output/error schema、executor负责validation/authorization。新发布只落在某provider允许的载荷版本，没有新的普适权限/正确性机制，故仅报告而非强造Books增量；不是按“原原则未变”排除实际发布贡献。交接见[CALIBRATION_HANDOFF](../_sources/daily-20250927/CALIBRATION_HANDOFF.md)。

## 5. 缺口与下一步

可执行普通待办0。唯一发布的有限结论与Books仅报告已独立裁定；两页134题摘筛选及21项必要边界的实际复核范围见§6。下述本窗终态保留项不支持正面证据、Books或无遗漏断言；具名原材料到达后定点重开，不把取得全文当成当窗证据通过。

外部隔离：2509.22626v1 [Learning Admissible Heuristics for A*: Theory and Practice](https://arxiv.org/abs/2509.22626v1)完整题摘已读，CEA constrained training及PDB/ReLU width-depth sample-complexity有理论潜力；Rubik小任务不是机械排除理由。提交原`Fri,26Sep2025 17:51:26 UTC`不等于公开，未评分/采用。需官方逐篇公告或原作者公开正文完全落窗区间，只重开该家族；[精确原记录](../_sources/daily-20250927/ASTAR_RECORD.json)。2509.22526 Event Generator Tuning中心为neutrino/GENIE物理模型，范围暂缓，不以robustness词入选。

arXiv完整134题摘为114潜力/20具体关闭，身份、原日期与21项精确v1必要边界见[NARROW12_SCREENING](../_sources/daily-20250927/NARROW12_SCREENING.md)。旧单次停止是root当时技术路由，不是用户禁止覆盖，尾34现已补齐；不说API全不可达。逐篇first-public、Google/DeepMind、MetaResearch、Hunyuan、ZaiResearch、Seedpaper、MiniMax Agent历史限制依§2原响应作本窗外部终态保留，不评分、不进Books，不支持正面Coverage/Evidence、零事件/无遗漏。可接受重开为具体原正文/原公告完全落窗区间及受影响命题精确版本，或对应有限历史目录；仅窄补相应身份/来源，不扩其他日/月/Weekly。

tool-output完整2025 schema未取得但不影响当前仅发布事实的最低命题；需要主张当时具体兼容性/实现时必须恢复Sep精确官方文档或release artifact再重开，不借当前说明倒填。

## 6. 复核

复核者：root（非本日作者）。

结论：通过

root复用本日有效tool-output原帖version1/time、当前文档权限及Ch78裁决；实际核两页查询/停止、14源请求与恢复。对21项安全/保证材料分别定点读取精确v1威胁权限、分母、局部干预或保证条件，并核作者必要位置记录；不声称独立遍历21份全文或接受全部证明。SysVec无绝对安全、incoherent计SAFE、CFG省略约束/unsat回退、exchangeable batch与条件校准等反侧继续隔离，不进入Books。

完整题摘抽检首15关闭中的职业Agent、教育综述、bin-packing与WMT四项，以及尾五项medication/narrative/AutoPK/corpora/AI-Noether；后五为全部新增关闭，其他首批11关闭未另行无差别重读。范围关闭不能外推临床安全，局部机制与负面结果没有因题名或小模型被排除。114日期潜力不计当日论文、不转全文队列。正式唯一家族4分/仅报告，Books修改0；外部来源及公告缺口不支持无遗漏。

本日V3 schema/consistency校验通过；2份本日Markdown本地引用无缺失，限定路径diff-check无空白错误。机器检查不能替代语义验收；未stage/commit/push。
