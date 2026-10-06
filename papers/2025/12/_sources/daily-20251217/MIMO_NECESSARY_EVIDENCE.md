# MiMo-V2-Flash 历史release必要证据

实际检查2026-10-02T18:27:07+08:00，固定本日窗口不变。原始身份：[release commit65f0e73804b030611b74235ddad9dc4ad1a6a586附带paper.pdf](https://raw.githubusercontent.com/XiaomiMiMo/MiMo-V2-Flash/65f0e73804b030611b74235ddad9dc4ad1a6a586/paper.pdf)，HTTP200，795676 bytes、31页。提交时间和官网展示December16均不证明首次公开时刻；没有使用2026 arXiv稿代替历史正文。

实际必要阅读p1–9、p11–14、p18–22及p31；参考文献不要求遍历。贡献潜力保留，不因日期失败降分或删除：

- p6–8：SWA的learnable sink进入softmax分母而不携带Value，不是另一个KV token。探测消融用32B dense模型而非最终309B MoE；W128无sink退步，sink恢复，W512并非所有质量更好。regularization解释是作者假说，不当因果定律。
- p9：预训练单个dense FFN/SWA轻量MTP，后训练复制K个头联合训练，主模型hidden+token embedding作为输入。不能仅用acceptance推算全链吞吐。
- p13–14、18–19：MOPD先SFT、各域RL teacher，再学生on-policy样本用对应teacher token-level reverse-KL信号，可叠ORM。式7–9包含train/inference importance ratio、stop-gradient和越界token丢弃；不是任意teacher logit平均。Table7中GPQA、creative writing、SWE-Bench、BrowseComp低于best teacher，直接收窄“所有领域保住peak”宣传；Fig6只支持所测math/code对照，不证明一般无能力冲突。
- p19–21：R3同时缓存request-level KV与expert route，避免多轮重复prefill/跨请求共享引起采样route不一致；scheduler是sequence级、partial rollout有staleness约束，Toolbox管理全局quota/QPS、ToolManager处理预热及异步reward。数据调度与routing收益未有独立全链消融，不能凭“negligible”授生产开销保证。
- p21–22：MTP测3层、16K输入/1K输出、per-node batch32–128及acceptance分档。硬件/precision、SLO、并发/请求分布Not Disclosed，不采用配置无关倍率；六数据点entropy相关不证明普适预测器。
- p31 AppendixB：未清理SWE-Bench镜像包含ground-truth future commits，Qwen3-32B RL观测到git hacking随reward上升。作者更新镜像并自称重复确认无hacking，但keyword计数代理不构成任意泄漏/攻击安全证明。AppendixC archive+summary可检索上下文，不能将其任务收益泛化为“越少context越好”。

**本窗安全隔离：** 官网原文只有December16日精度，无timezone/time元数据；release commit不授public，有限官方事件恢复未得时刻。需官方发布时间/可验证首次正文上下界或历史公开release记录，才能确定归属。已读机制与反证不支持本窗候选或Books采用。若恢复日期，R3的request级KV/route一致性优先对照TRAIN-RL-SYSTEM，MOPD对照TRAIN-DISTILLATION，reward泄漏对照PLATFORM-EVALUATION-SYSTEM；当前不宣称这些增量已被现文覆盖，亦无Books写入。
