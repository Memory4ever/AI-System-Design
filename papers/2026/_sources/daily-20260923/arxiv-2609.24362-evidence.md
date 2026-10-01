# VLM-in-Sandbox — 2026-09-23 定点证据

- Source Family：`SF-2026-ARXIV-2609-24362`。
- Primary：[arXiv 版本记录](https://arxiv.org/abs/2609.24362)、[exact-v1 HTML](https://arxiv.org/html/2609.24362v1)。官方 `cs.AI/recent` 将 v1 放在 2026-09-22 公告批次；`abs` 的 09-21 提交时间不能当作公开时间。公告批次属于本日报窗口，未观察到撤稿或更早作者原始发布；这不是穷尽所有渠道的证明。
- 准入与评分：图像证据“持久存在”与“进入下一模型请求”是不同状态；此前 Ch75 有通用 Context/Artifact 分权，但没有图像像素可见性的具体转换。Design Delta 2、System Reach 2、Durability 3，合计 7。
- 机制：§3.1–3.4、Appendix A.1。Docker sandbox 生成 crop/mask/overlay 等图像；Image Ledger 为输入和生成图像记录 ID、文件路径、来源及父子关系；非活跃的 inline payload 可被驱逐而文件保留。模型调用 `Promote(asset,focus|aux)` 才使某幅图像成为下一次请求的可见像素。Compiler 从任务、最近三轮、旧轮次 deterministic recap、ledger 和两槽 active visual context 重新组装 prompt；Promote 不做图像处理，也不删除原始证据。
- 旧方案与代价：append-only 自动回灌在短任务可读、实现简单；长轨迹重复占用视觉 token 并可能淹没关键细节。仅存文件避免成本但缺少模型可用的回读入口。Ledger + slot 增加状态管理、错误引用、错选与解释错误；显式选择也不等于视觉证据真实可靠。
- Evaluation contract：§4.1 的四个 VLM、七项**静态图像** benchmark、6,350 个样本，完整方案相对 append-only 的准确率是作者设定下的结果；GPT-4.1-mini 对 append-only 有 302 rescue / 142 regression，不能只报净增。§4.2 的 GPT-4.1-mini 三项 benchmark、1,260 样本 compiler-matched `2×2` 比较，将可见性选择与保留上限分开：完整方案相对 auto-all 准确率 +1.83 个百分点、总 token -18.6%；同为两槽的模型显式选择相对自动 recent-2 只 +0.63 个百分点，区间跨零。最大的 token 改善来自有界保留，不得写成 Promote 单独必然提高正确率。
- 系统边界：§5.1 的 fixed-trace replay 只证明请求规模行为，不证明闭环成功；§5.2 的 prefix-cache 延迟实验限 Qwen3.5-9B、vLLM、8×H20、TP8、并发 1、同三项 benchmark 1,260 样本。工具化推理总体仍比单次 Vanilla VLM 贵；不外推 API 成本、生产尾延迟或 SLO。§6 仅评估静态图片，视频是未来工作；Appendix D 有中间视觉证据解释错误而最终答案正确的反例。
- Books：`AGENT-CONTEXT` Ch75 已有原文/派生视图/模型可见状态的通用主线，本次只补视觉 artifact 的具体生产—保留—提升—编译转换及受限比较；Ch77 Memory 和 Ch78 Tool 不拥有这些可见性语义。独立审阅者 `sep23_independent` 核日期、准入、对照与证据边界，并已完成 Books 写后复核；按反馈将“退出槽即释放”收窄为“生成图像退出槽后可驱逐”。
