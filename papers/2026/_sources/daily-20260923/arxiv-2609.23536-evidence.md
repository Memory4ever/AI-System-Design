# 2609.23536v1 定点证据审阅：低精度 Pipeline 的显式状态合同

- 身份：Genlang Chen、Junyi Zhu，*Explicit State and Resource Contracts for Low-Precision Pipeline Parallel Training under Captured Graphs*，`arXiv:2609.23536v1`，[官方摘要/版本史](https://arxiv.org/abs/2609.23536)、[精确 v1 HTML](https://arxiv.org/html/2609.23536v1)。访问日 2026-09-23。
- 日期：`v1 Submitted` 09-20 10:27 UTC；[09-22 官方 `cs.DC/new` 公告](https://arxiv.org/list/cs.DC/new)列为 New submissions 第 15 项。按[arXiv 公告规则](https://info.arxiv.org/help/availability.html)，arXiv 公开事件是 09-23 08:00 北京时间，投稿时间不是公开时间；作者更早在外部公开的可能尚未完全排除。
- 归属：`TRAIN-PIPELINE-PARALLEL` Ch38；相邻 Training distributed runtime/communication 章节只作 handoff。旧 Ch38 已写 stage schedule、activation lifetime、weight version 和 boundary send/recv completion，但没有把 FP8 hidden state、非 LIFO retained work、捕获图固定地址下的资源世代与 cache freshness 组合成独立执行合同。

## 为什么旧接口不够

普通计算图只描述显式 tensor 边，单纯 CUDA Graph 以固定虚拟地址重放可降低 launch 开销；同步 1F1B 在同构 full-backward 下较容易把资源生命周期与栈次序绑定。FP8 delayed scaling 持有 amax history、scale 和 quantized-weight cache；split-backward 把 dI 与 dW 分开并可能让 dW 乱序延后，固定地址再次代表不同 microbatch。若只依赖单一依赖 token，既无法命名所保留的 backward work，也无法证明 cache 对应当前 optimizer 版本或 caller stream 读到已经完成的结果。

§III 将四种关系分开：hidden scaling 的 effect token 提供数值更新顺序；逻辑 `TapeKey(epoch,stage,microbatch,chunk,invocation)` 与物理 `TapeRef(slot,generation)` 防止重用地址的 ABA/错绑；weight/cache epoch 在 optimizer commit 后强制刷新；caller→graph 和 graph→caller 双向事件构成完成边界。dI 更新 backward scale 一次并留下 dW 任务，dW 按相同代际消费，两个 consumer 完成才释放 tape。checkpoint 只在 quiescent optimizer 边界保存持久数值状态；graph/event/tape 等进程局部资源重建而非序列化旧地址。静态 scale 或即时 dW 不需要同样的状态面，旧方案在这些约束下仍成立。

## 证据与代价

- §IV 描述 TorchTitan GraphPP + NVIDIA Transformer Engine 2.18 的实现路径，逻辑 identity/资源代际检查在物理动作之前、成功之后才提交 transition；未披露可访问的独立代码仓库 URL，正文中的“artifact 含 JSON 报告/脚本”不等于本次已复核代码。不能将论文声称的 bitwise parity 说成我们独立复现。
- §V 将 correctness 与性能分开：同模型参数和数据序列、AdamW、FP8 recipe，比较 loss、gradient、optimizer、scale、cache version 与冷重启；两种 H800 PCIe、RTX 5880 Ada 单节点设置。性能关注 seq=256、microbatch=1 的细粒度 overhead-dominated 工作负载，而非长序列 compute-bound LLM 训练。作者报告 H800 捕获路径相对 native eager 的完整 step 1.82–2.79×，但初始 n=3、独立复测 n=2 分列；不能外推端到端大模型训练加速。
- 静态图和梯度 arena 容量按 microbatch 数线性增长；hidden=4096 的捕获方案相对 native eager 峰值多 3.357/4.437 GB，setup 至 break-even 约数十步。direct gradient placement 避免 dW 拷贝，但要求绑定稳定地址并增加预留。ZB-V 不总比 Interleaved 快，选择依工作负载。
- §VI 限制：TE 完整 delayed-scaling 状态有实测，TorchAO 只验证 stage interface；未验证跨节点 InfiniBand、TP/EP、PP=4 ZB-V；checkpoint 不改变拓扑且必须在安静边界。那些不是“已经支持”的结论。

## 初步 disposition

已读 Method/控制流、实现、匹配评价与 limitations，非作者独立复核认为本窗准入、精确版本与 Ch38 差异成立（Design Delta 3、System Reach 2、Durability 2，合计 7）。已把状态所有权与共存边界嵌入 Ch38 的 1F1B 后，并按复核意见修正单 token 失效归因及同步/异步 handoff；非作者写后语义复核通过。作者更早在外部公开的可能未完全排除；若发现更早 primary 发布，应回拨 owner 日，不以投稿时间机械移出。
