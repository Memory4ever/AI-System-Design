# Kimi-K2-Instruct-0905：发布版本评测边界

作者Mendel。root已校准防Git泄漏/外引基线差异为具体潜力；本次解除技术路由导致的日期/version缺口，不借模型规模或context翻倍倒推贡献。

## 原始事件和精确版本

实际取得官方[Developer Support发布帖](https://forum.moonshot.ai/t/kimi-k2-0905-update/81)的JSON，首帖admin=true、primary_group_name=mission-crew，`created_at=updated_at=2025-09-05T03:30:13.003Z`，即北京时间11:30:13.003，完全落06窗。首帖宣布0905 update，链接Moonshot权重/代码与正式平台，不是普通用户Community发言。使用此官方发布事件，不以HF创建时间`2025-09-03T03:34:36.000Z`或commit时间伪造首次公开。平台Blog午夜日期编码与论坛精确发布事件语义同时保留。

HF官方commits实际返回17项，从2026/01至2025/09/03；停止于返回集合。冻结发布帖之前最近README commit [7152993552508c9f22042b3bb93b5e6acd06ce73](https://huggingface.co/moonshotai/Kimi-K2-Instruct-0905/blob/7152993552508c9f22042b3bb93b5e6acd06ce73/README.md)，原date`2025-09-05T03:07:24.000Z`，不使用当前2026 main。保存KIMI_CARD_715299.md、KIMI_COMMITS.json、KIMI_FORUM_EVENT.json及HF metadata。当前可见事件未见撤回/纠错标记；后续工具模板修复不扩为本窗事件。commit确定内容版本，不单独确定当时公开时间。

为回答0905是否披露新协议，仅定点比较前一日README commit d30fdf66df21ffc62bed9dfde6e33b5ea0292bdc（KIMI_CARD_D30.md）。旧版本无§3新的Git对象剪除和SWE-Dev目标测试删除说明；0905将大表改为五项coding评价并明确披露协议。它证明披露差额，不证明团队此前从未内部采用。temperature映射/native tool parsing已在旧README，故不作为0905新机制。

## 贡献与证据

准入链：仅冻结目标commit的可见文件仍可能让Agent读取其他Git对象或目标测试 → card§3披露每次全测试运行前剪除目标commit不可达对象，SWE-Dev另重写原文件并删测试目标函数的测试 → evaluation identity需要声明完整可读代码状态/测试可见性，而非只写模型与benchmark；外引榜单须分协议解释。

评分`2 + 2 + 2 = 6`：明确评价有效性边界、连接环境与比较、可复用但非新学习理论。因具体泄漏/评价正确性约束深入受影响内容；完整card §§1–5、必要前版差额和事件已核，未运行未公开in-house harness。

采用范围：§3说0905结果为五次独立full-test-set mean±std，Git处理逐run执行；SWE-Dev另删目标测试；除Terminal-Bench用Terminus-2外为SWE-agent衍生in-house harness，Bash/Edit上下文被clamp，system prompt按任务改写。星号基线外引报告/排行榜，非星号作者声称相同条件重测。不把星号结果合并公平排名。

反侧：card宣称“only legitimately available code”的guarantee过强。未披露prune命令、refs/reflog/alternate/worktree/network处理、target tests筛选实现或可重放artifact；无before/after泄漏对照，不能归因分数变化，也不排除预训练见目标答案。Git可达性不是历史可见性的完整定义。采用公开协议和攻击面，不采用全污染消除或实现认证。

仅作为作者结果语境：Verified69.2±.63、Multilingual55.9±.72、Multi-SWE33.5±.28、Terminal44.5±2.03、SWE-Dev66.6±.72（ACC）；5-run std不是SE/置信区间。seed安排、跨模型配对/训练预算未明；0711表内数值不证明0905提升由防泄漏导致。任务集版本、harness源码/commit、clamp数值、评价hardware/precision/batch/concurrency、输入输出budget/SLO均Not Disclosed。部署权重block-fp8不是评价配置。API60–100TPS/100%tool-call宣传不纳收益，格式正确不等于工具语义正确。

## 唯一owner与 root 提案

`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) L250–258已有model×benchmark×harness×environment×scorer、轨迹/adapter等价与环境冻结。差额仅为Git对象数据库及目标测试也是可读环境，外引基线不等价的一般原则已有覆盖，不另堆段落。

建议在“可复现评估身份至少应写成...”之后、“统一harness降低重复建设...”之前自然接入：

> 代码Agent的环境身份还要覆盖它实际能读到的历史和测试，不只是checkout后的文件。目标commit以外的Git对象、refs与目标测试可能提供本不应可见的实现线索；因此应声明目标commit、允许的历史可达集合、对象清理策略及测试可见性，并保存环境artifact。公开card中的逐run剪除不可达对象和SWE-Dev目标测试删除，是这种协议的具体例子，但未公开的清理实现不能证明所有泄漏已消除。外引榜单不能冒充同harness重测，无法对齐时保留各自结果而不做机制因果比较。

必要来源为冻结card§3三个说明段/必要前版差额/官方事件，不需采用模型胜负数字。Ch65资源公平与[Ch67](../../../../../books/part-06-ai-infrastructure/67-monitoring.md)监控聚合不接管此机制，已有质量定义/测量交接保持；[Ch78](../../../../../books/part-07-agent/78-tool-calling.md)可链接环境约束但不重复Evaluation推导。

作者未改Books。root待核官方发布身份/时刻与精确version连接、协议及未证边界，再决定实际写入/邻接和日级复核。若root认为此发布帖不能支持card发布事件，家族回到日期保留项而不是贡献排除；重开条件为同版本官方有时区发布记录或完全落窗区间。
