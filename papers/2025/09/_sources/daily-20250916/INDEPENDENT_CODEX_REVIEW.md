# Codex 发布单项独立校准与证据判断

复核者：root，非本日作者；本记录只授单项判断，不授整日完成。

实际解析本日原 OpenAI RSS 的 release 条目：`Mon, 15 Sep 2025 10:00:00 GMT`，北京时间15日18:00，落16日默认窗口。实际读取[官方发布正文](https://openai.com/index/introducing-upgrades-to-codex/) GPT-5-Codex、CLI、cloud、Code review 与安全段落；明确排除页面标注的9月23日 API 更新。没有把提交、系统卡的另一个事件或后来的更新合并到本次发布。

准入通过，`2+2+1=5`。统一投入可能无法同时照顾短交互和长任务 → 原发布披露员工流量短/长 token 十分位的投入变化方向相反 → 评价部署时应分切片核预算与质量，不用一个节省数字决定全部任务。这是特定版本的经验观察，不是自适应控制器已公开或普遍最优的证明。

标准审阅通过，采用范围限于公开版本事实和评价边界。原文十分位按模型生成 tokens（包括 hidden reasoning 与 final output）排序，不等于预先配对的同一任务难度档；对照和独立不确定性不足以识别某个隐藏算法的单独因果。SWE-bench分母从477改为500，旧分数不直接拼接。长运行个例不是 durability/SLO，container caching 的局部中位收益不是新缓存算法的证据。默认 sandbox/network restriction 与人审建议不能授生产安全。硬件、precision、batch/concurrency、控制器与训练细节未披露，不补造。

Books 决定：**仅报告，实际新增正文0**。实际顺读 Ch81“Workflow 可见性也会改变 Serving 优化空间”及完整窄 Orchestrator–Engine 接口、Long-running 与 External Events；Ch75“Context Compression 必须保留执行状态”正文和后续约束。现有正文区分 workflow 的 budget/state/permission 与 engine 的 admission/KV/completion；发布没有披露新的预算分配机制、恢复协议或 compaction 正确性依据。短/长投入观察本身可保留在本日报，但不能把未公开机制写成新长期设计，也不能给现有 durable state 正文追加一个不证明它的案例。不是以 Books 已覆盖为由撤销准入，不宣称所有版本观察均已由书稿承载。

必要安全变更已经在该 release 的实际核心范围审阅；系统卡属于另一个窗外事件。本日其余安全/反侧、来源停点、分层排除和最终六部分尚待独立 DAY。未核 CLI 实现、未运行实验、未改 Books。
