# 2604.25380v1：非作者 source→actual-owner 与写前判定

2026-09-29 对读 [arXiv exact-v1](https://arxiv.org/html/2604.25380v1) §3.1–3.3、§5 Tables 3–7，实际 `AGENT-PLATFORM` Ch84、`AGENT-TOOL-CALLING` Ch78 与 `PLATFORM-EVALUATION-SYSTEM` Ch66 的相邻段。此记录不代替 04/29 全日日期/来源/分母 Gate。

**准入与 owner。** 任务相关界面状态可在两次 post-action 截图间出现并消失；§3 把中断弹窗、短暂引用、动态列表和内容触发事件列为不同评测切片。这改变的是 dynamic computer-use EvalSpec 的 observation sampling、event-time witness 与 replay identity，不是“每个 Agent 都要使用作者 video/clustering/reflection 三模块”的架构要求。Ch84 已有 runtime 的 observation/action 时钟分离，Ch78 已有工具 effect 验收；Ch66 目前只有 **turn 间**外生 mutation log 和一般 pre/post digest，未处理同一 turn 两次动作间的 transient event 漏录。最小长期增量归 Ch66，不能再追加 Ch84 清单。作者 2+2+2=6、Standard 且因具体知识缺口执行必要机制/反证复核，准入有限通过；正式当窗事件归属由日 owner 另核。

**反证与边界。** Table 4 的 DP-only 15.1→17.4 与整框架 22.1 分开；Table 6 却把 `Ours DP` 标 22.1，不能将总增益归视频选帧，相关归因隔离。Table 5 的 Writer/Impress/Thunderbird 反退，Table 6 ContentTrig DP 低于 baseline，排除“更多帧/自适应帧单调更好”。模型、反思器、最大步骤、帧/token/call budget 变动须分别冻结；149 任务/10 应用及作者 benchmark 不证明生产 GUI 安全或所有事件都有 ground truth。拟在 Ch66 加一小段比较 post-action-only、uniform、gated keyframe 与独立 effect verdict，要求 missed-event 与 outcome 分报；无可重放事件真值时不得宣称 temporal coverage。

状态：Source→owner 写前通过，Books 写入/非作者写后未完成；不把本记录当日级 Complete。
