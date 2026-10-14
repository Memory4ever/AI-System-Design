# GAIA v0.13.0 必要Source／具体owner准备包

## 1. 本次事件、准入和评分

作者Singer；只Nov16新增Nov15 BJT自然日。完整官方release及原JSON身份/公开字段经Dalton本日独核§2通过：v0.13.0、draft/prerelease false、published_at2025-11-14T16:12:16Z＝Nov15BJT00:12:16；不是仓库creation/commit/发现日。只这条线索跨日去重，原lead见[原release JSON](../daily-20251115/SUP_gaiaRelease_20261014.raw)，本日实际[官方release](https://github.com/amd/gaia/releases/tag/v0.13.0)核心L212–271与tag commit8981b65相符；原代码树[本日原件](SUP_gaiaTag_20261014.raw)精确SHA8981b656952328559f30fa2ed9dfb98d4c2ba2d7、truncated=false、419目录对象，只定位必要文件，不全源码队列。

原接口adapter分开、评测转录可能silentfallback→本release新统一inheritance exposure与转录不匹配显式失败→需区分可复用接口与无效测量是否混入有效分数。采用Dalton实际窄评分**2+2+1=5**：DD2局部架构/正确性边界，Reach2跨Agent exposure与evaluation消费，Durability1版本实现；不借成熟failfast/协议术语/AMD声望加分。最低标准；具体评测纠错无论5分均加深该分支及直接反侧，不扩所有PR/AMD。

## 2. 新实际原证与身份限制

2026-10-14本日实际请求均已结束，非legacy。API PR843 HTTP200/19829B却title为`Add claude GitHub actions 1776733682521`，body为code-review workflow、未merged；与release所称转录修复身份不符，**不采用其diff/日期**；[原件](SUP_gaia843_20261014.raw)/[headers](SUP_gaia843_20261014.headers)。PR846 HTTP404/134B，[原件](SUP_gaia846_20261014.raw)/[headers](SUP_gaia846_20261014.headers)，不冒源码核验。具体失败不是所有必要实现不可得。

转精确tag原tree HTTP200/118888B及三个必要raw均200：eval.py147830B、api_agent.py3907B、mcp_agent.py2352B。URLs在各headers请求及下方固定SHA链接可复查。实际只读相关eval函数865–1100/1370–1445/1718–1851及两基类完整文本，不读无关eval/所有419文件。

## 3. 必要机制与反侧（未运行代码）

[精确eval.py](https://github.com/amd/gaia/blob/8981b656952328559f30fa2ed9dfb98d4c2ba2d7/src/gaia/eval/eval.py#L974)／[本日raw](SUP_gaia_eval_20261014.raw)：`_analyze_summarization_results`先读embedded groundtruth；只有没有embedded且存在读入groundtruth、含summaries及metadata.consolidated_from时进入source_file→transcript_id匹配。984–1004按字符串相等或斜杠替换匹配metadata.source_files，第一次命中即停；没有transcript_id时1006–1048日志列可用source/ID和修复提示并raise ValueError，**不取第一个不相关transcript**。1826–1836外层except返回overall_rating.rating=`error`与失败说明，不称整个CLI进程必然退出或全部数据已一致。

直接反侧：groundtruth文件不存在/读失败时仅warn并置None；regular或embedded路径不同；mapped ID存在但不在gt_summaries并未在这一条件抛同样错误，可进入无参考评判；source_file字符串/分隔符匹配非content-digest绑定，重复映射只取首个；题目/GT语义正确、完整映射与生产artifact未验。JSON解析部分恢复/显式fallback另有路径，不能把本release“Remove Silent Fallback”扩大成所有fallback删除。只采用**该consolidated路径无映射→显式测量错误**，不授所有失败无分数、数据绝对正确或评测安全。

[API基类](https://github.com/amd/gaia/blob/8981b656952328559f30fa2ed9dfb98d4c2ba2d7/src/gaia/agents/base/api_agent.py)／[本地](SUP_gaia_api_20261014.raw)完整：ApiAgent(Agent)提供get_model_id/get_model_info/estimate_tokens；说明普通Agent可由process_query接API，mixin为定制。默认model-info8192/4096、字符/4估token只是局部默认，不认证模型实际限制。Docstring提format_for_api但本文件未定义；不据此宣布运行bug，未核整个server路径。[MCP基类](https://github.com/amd/gaia/blob/8981b656952328559f30fa2ed9dfb98d4c2ba2d7/src/gaia/agents/base/mcp_agent.py)／[本地](SUP_gaia_mcp_20261014.raw)完整：继承Agent但要求子类get_mcp_tool_definitions/execute_mcp_tool抽象实现，prompts/resources默认空。**不是仅inherit就生成所有工具语义**；server_info2.0.0不是MCP negotiatedversion保证。CLI为release capability声明，本包不授三transport完全等价/取消/授权/lifecycle。

Code/Python/VSCode与Docker均原release明确PoC；没有同预算性能benchmark、错误率或真实安全对照。Workload仅发布说明/静态局部，不采用吞吐/质量提升；model/hardware/precision/batch/concurrency/SLO/evaluator配置Not Disclosed，接口纠错无性能外推。维护reference映射、显式失败排查/重新执行与接口adapter验证均有工程成本；资格不齐回退原reference独立核验/Unknown、专用adapter和真实effect gate，这是本书工程推断而非GAIA已实施全合同。

## 4. 唯一owner与具体NoChange提案（尚待reader最终接纳）

本family主owner拟`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，采用命题为测量输入/参考身份不匹配不得默默换reference并充有效分数；release exposure是次命题交[Ch83](../../../../../books/part-07-agent/83-mcp.md)，不双主owner。

已actual读ROADMAP全、PROJECT_CONTEXT/LEARNING_PHILOSOPHY/WRITING_GUIDE、相关State和三个owner局部/交接，无Books写。Ch66开头14–31完整对象/四阶段，84资格不核保Unknown，86–90parser失败与真正语义失败分账，294–322 subject/adapter身份，3489–3514 dataset identity/digest/source/schema/expected outputs，3581–3597 EvaluationRun逐样本trace、failure/exclusions、immutable artifacts，4728–4736 unmatched非false及stored label回溯execution/request/stimulus，**已具体覆盖参考绑定与无效测量不能借替代参考授分**。GAIA字符串分支并无新的reference身份证明或普遍正确协议，不因其implementation细节造书稿gap。

Ch83完整88–120：protocolversion/capability/server+tool identity，五维契约/adapter分责及共享typed definition生成adapter不证明stream/cancel/lifecycle/authorization；覆盖本次exposure的可复用范围和泄漏风险。Ch84开头14–93 definition/run/evidence三面、query完成非任务完成、Tool/Environment外部effect与Policy授权；其实际状态/审批责任不由GAIAPoC授代替。三章外部dirty/cached保护未改。

因此提案**已有覆盖No Change，Books写0**，具体主ownerCh66上述论点，Ch83/84仅交接，不是因5分或review省费降准入/改分。请Daltonactual必要静态分支/反侧与具体NC，读完可正式归并本family单篇；无Books锁/无待写内容，无artifact运行或复现/生产保证。本包非整日报DAY。

## 5. 已发生最终单篇独核

已actual读Dalton本日§4–5：必要Source、5分和唯一Ch66具体已有覆盖No Change真实通过，源码outercatch正确定位1826–1836已行政校准。未变原证不重读/第三次审批，不需Books锁/写入/POST；该单篇准入→date→必要Source→owner闭合，非日级DAY。本日其余source/有限title/date与six普通继续。root最新83/132、49待来自Dec13，不含Nov16，不改历史82快照。
