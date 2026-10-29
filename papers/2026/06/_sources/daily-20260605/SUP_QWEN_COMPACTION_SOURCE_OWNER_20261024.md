# Qwen Jun04 compaction：单篇必要Source / actual owner / 最小PRE提案

**当前R37–38纠正（优先于下方原准备态）：** 作者已实际取回并读两官方PR完整English body/事件字段，保存SUP_QWEN_PR4599_20261024.json及SUP_QWEN_PR4688_20261024.json。4599 created May28 11:05:36Z、updated=merged May29 08:20:14Z；4688 created Jun02 03:41:37Z、updated=merged Jun03 01:23:01Z，均早于补窗。两body已含本项全部压缩机制，Jun04 Blog无独立新增机制/重要修订或评价；因此撤销本轮候选/原拟6分及PRE请求，不入Books。下文评分、literal和PR“可选”的说法只保留为此前读取/判断记录，不再有效，不用免责声明绕过first-public。原PR另有multi-turn丧失verbatim-tail、microcompact仍清media、resume未验证和transcript pointer未接限制；不把作者自报测试当本reader运行。更早事件仅留窗外恢复线索，不补跑其他日期/旧Report。重开本窗须具名Jun04独立新增原证；其他十四准入/日证及I8不变。

作者supp_20260605_author，2026-10-24。实际采用reader R33–36：两机构Jun04日历家族及13篇精确v1准入/联合日证已通过，五后版混用限定不挪回。此项只用[官方Jun04 Blog](https://qwenlm.github.io/qwen-code-docs/en/blog/updates/weekly-update-2026-06-04/)，本地SUP_QWEN_JUN04_20261024.html（479066 bytes）；官方页显示2026-06-04且末端last updated September4，采用当前原说明描述的该事件，不声称June04原页面逐字未修改，也不从Blog日历签两release同日。无withdrawn/correction信号。R35已核日期，不第三AB/date。

## 评分与必要域

2+2+2=6。Design Delta=2：具体user-boundary split失败到summary＋显式恢复的替代接口；Reach=2：跨summary、文件、图像与后续执行消费；Durability=2：恢复保真/状态身份的可复用边界。不给普通新版本、9节/5文件/3图常数或厂商声誉加分。因恢复语义知识缺口深入相关必要域，不等同整份release/所有PR已审。

实际完整读官方Compression Rewrite核心、其前ComputerUse deferred/permission/lifecycle段和直接恢复承诺；其他UI/Feishu/IME/运行优化只定位，不进本项命题。原代码/测试未读未运行，所有实现事实只为作者公开说明，不签代码已核或真实复现。PR4599/4688为可定点恢复的公开实现链接，不是本结论缺失必需附件；不对“全部恢复准确/auto-recover plan”作采用保证，故不展开整PR。

### 支持：原旧路径为何触边

旧路径按字符长度拟分前70%摘要、后30%原文，但实际要至少两条user message才能找到split point。单user长GUI任务虽累积许多工具回合仍不满足；fallback把原user prompt及screenshots一起替成text summary。问题不是模型窗口不够大或所有比例错误，而是切分单位与任务轨迹结构不匹配，并使视觉证据失去inline可见性。

### 支持：原新接口是什么

新说明为9节structured summary，Section6要求逐字引每条user话语；最近5文件size-adaptive恢复，小文件fresh-read全内容，大文件仅路径；最近3图加turn index/source tool/args元数据再可见。文件路径不等文件内容，摘要不等pixels；参数是该实现预算而非通用最优。/compress focus仅摘要指引，不能替代原意保留或工具权限。

### 直接反侧与证据权限

- 公开说明没有该改动的控制组、任务成功率、样本/重复/CI、模型及硬件/输入长度、token/时延/SLO或完整重试费用；这些均Not Disclosed，不能写“不会失忆/零损恢复/已解决所有长任务”。无需为不采用的宣传数字找额外benchmark。
- 最近N仅保部分历史；重读disk返回当前文件，不自动重建先前观察版本；引用大文件仍要授权回读。旧截图有turn/tool来源不证明当前GUI未变，更不保证坐标能直接复用。这些是基于原接口的项目推断，非作者额外实验结果。
- 原说明ComputerUse为deferred schema、首次permission dialog后后续调用直通；macOS权限/服务生命周期是另一控制面。恢复用户话语或图像不得重新授予权限、自动重放动作或把外部工具内容升为用户指令。本文不评该permission设计的普遍安全，也不把框架一确认等于所有动作安全。
- summary生成、图像编码、磁盘回读、重新prefill和后续验证都付费，未给全轨迹节省；可保原history/近期完整视图、按需回读和新的live observation。支持与关键反侧已足，当前停止。

## actual owner 差额

实际读Ch75开头/Context assembly、175–278的working-state与视觉artifact组、287–400压缩/原文/commit组及Ch74/76开头交接；ROADMAP、三公共Books上下文与2026路由已读。`AGENT-CONTEXT`唯一owner，Ch75 `## Context Compression 的损失`。

现有“摘要可能丢exception/否定/数字/provenance”及原文是事实/summary只是视图，已有general loss/恢复原则；视觉artifact组解释ledger、active slots、raw可回读，SWE观察删减保system/user与近期tool。它们没有解释**单user多tool轨迹让user-boundary split没有合法分割点**，也未将压缩时原指令、live-file重读与历史图像三个恢复对象分开。因此不是只加Qwen例名或常数的覆盖重复，建议最小两段；不改Ch74软prompt或Ch76检索机制，不触发结构候选。若非作者判现有段已具体覆盖，可改具体NC而不造diff，但须指出实际完整承载段。

## PRE literal（尚无root授写/未SAVE/I/POST）

完整前锚：

> 目标不是最短，而是保留对未来决策充分的信息。摘要可能丢失 exception、否定、数字和 provenance；递归摘要还会累积漂移。

拟新增两段：

按用户轮切分历史，在多轮对话里容易保住近期原文，却未必适合只有一条用户指令、随后执行许多工具回合的长任务：若切分器要求至少两条用户消息，找不到边界后的纯摘要退路就可能同时移走原始意图与截图。一个恢复分支将摘要和显式回填分开：用户话语逐字保留，近期小文件从磁盘重读、大文件只提供回读路径，近期图像再附上产生它的回合、工具与参数。这里恢复的是不同类型的consumer输入，不是用一份文字摘要替代全部视觉和执行状态。

[Qwen Code的公开压缩改动](https://qwenlm.github.io/qwen-code-docs/en/blog/updates/weekly-update-2026-06-04/)支持这项具体失效与替代接口，但没有受控质量或全轨迹成本对照；最近若干文件/图像的预算也不保证充分。磁盘重读可能得到新版本，旧截图带来源仍不等当前界面，路径存在也不等内容已读；恢复时须核版本、补live observation，并由原控制面重新检查动作权限，不自动重放旧动作。摘要、回读、图像编码、重新prefill及验证均计费；保真或预算不合时保留较完整近期history与可回读原文，不把恢复成功当作信息无损、当前状态或生产可靠性证明。<!-- source-family:SF-2026-QWEN-CODE-COMPACTION-0604 -->

完整后锚：

> 词法minification也有同一边界：删除注释、改名或缩进即使保留部分程序运行语义，也可能丢掉修复线索，或让模型按压缩格式输出而无法匹配原文件。[受限SWE修复对照](https://arxiv.org/html/2606.01326v1#S4)出现输入减少而解决率下降，dedent另有补丁缩进失败；全bench主结果却排除了dedent，不能把全部退步归它。统一tokenizer计数只是代理，小样本变换消融也不等全人口因果。变换、原文映射、所有重试与测试都计费；格式或质量回归时保留原源码/注释、较轻删减与独立测试，不由parser语义或更少token自签消费者无损。<!-- source-family:SF-2026-ARXIV-2606-01326 -->

仅此插位提案；本人true-H2 Review notes可在获新授后记本来源/6分/必要域/未核实现与控制对照边界，不动他人注。当前交非writer必要Source/actualowner/PRE，未签I或DAY，未写Books/State/index。
