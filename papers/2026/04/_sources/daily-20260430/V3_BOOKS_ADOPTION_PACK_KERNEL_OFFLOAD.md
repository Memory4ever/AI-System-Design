# 2026-04-30 Books 写前最小采用包：26039 / 26074（作者提案，未获锁）

本文件只给 root 做非作者 `exact-v1 → actual owner` 判定。两项都在未冻结的本日工作集合中；这里没有修改共享 Books，下面的拟正文也不是已采用知识。日期仅依本日公告槽、连续 ID/邻界与原版身份作 04/30 08:00–09:00 北京的有据推断，Submitted/Updated 不是逐篇首发日志。

## 2604.26039v1 RaMP → Ch49 MoE grouped execution

- 必要来源：[官方 exact-v1 §IV-B/D、§V-A–E](https://arxiv.org/html/2604.26039v1)。在同一 MoE batch、同一个 kernel binary 和相同硬件下，实际 expert occupancy histogram 改变可选择的 CTA grid、wave 与 kernel config；不是替换 router 的 token→expert 决策，也不是跨设备 expert placement。论文有限对照为单 H200、vLLM 0.9 eager、顺序请求/重启 server、FP8 MoE；作者端到端 1.30× 不得升级为并发 SLO 或跨硬件速度。
- [Ch49 现有 MoE 段](../../../../../books/part-05-inference-system/49-tensorrt-llm.md)已将 activated-expert 与 token/tile/fabric 成本、当前 routing window 及异步 dispatch table 分账；**缺的只是同一已定 batch 的 histogram 进入本机 CTA grid/config 选择**。应放在“Grouped execution 可以减少逐 expert launches”之后、“MoE Dispatch 应平衡时间”之前，避免将下一节的跨 GPU dispatch 重新命名。
- 拟窄正文：`Grouped GEMM 的 expert 列表和总 token 数仍不足以唯一决定本机 kernel 配置。同一 batch 的 token→expert 结果既决定每个 expert 的有效矩阵高度，也决定空 expert、尾 tile 与可并行的 CTA 波次；当 histogram 从均匀转为集中时，原先按平均 shape 选择的 grid 可能让多数 CTA 空转。Kernel planner 可在 router 输出已冻结后读取这份分布，在同一语义/精度的预校准候选中选择 grid 与 tile，而不修改路由或跨 GPU placement。`
- 紧接代价/回退：`该分支需要统计 histogram、维护 model/layout/dtype/hardware 绑定的 config surface，并把选择开销计入请求关键路径；偏斜不足以跨执行 regime、shape 稳定或候选优势小于 dispatch overhead 时，静态 grouped kernel 仍更可预测。受限单卡顺序服务实验不能证明真实并发、All-to-All 或端到端 SLO 获益。`
- 审阅问题：上述同 batch kernel-config 身份是否已由 Ch49 其它实际段落完整承载？若是应判 Existing，不为一个 actuator 强行写；若否，只在本处写，不延伸 Ch36 的全局 placement。

## 2604.26074v1 DAK → Ch54 host offload

- 必要来源：[官方 exact-v1 §2.3–4.3、§6](https://arxiv.org/html/2604.26074v1)。特定 GPU/互联组合允许 host DRAM 经 TMA 直接读入 SMEM，绕过 HBM staging；按 operation 的 offload 敏感度分配，限制 host-inflight 避免反向拥塞。不是普遍的 host→SMEM 通路。实验限 GH200 NVLink-C2C、RTX 6000 Pro Blackwell PCIe、OPT/Llama 离线批推理、每请求只 decode 32 tokens；PCIe offload ratio 约 40% 以上路径差异收敛。给定 piecewise EB 曲线下的 greedy optimum 不等于一般服务最优。
- [Ch54 层级段](../../../../../books/part-05-inference-system/54-gpu-memory.md)已覆盖 HBM/host/NVMe 容量、预取、staging、readiness 与 bandwidth knee；**未明确 host→SMEM direct path 和 local HBM load 并发时，物理搬运路径本身成为按 operation 选择的 execution plan**。拟放在“扩展层级”现有 host CPU/SSD 总述之后、NAND/CXL 专用路径之前，或 offload 现有 copy/stage 说明之后，以实际邻接复核为准。
- 拟窄正文：`把权重或 KV 下沉 host 后，传统路径仍先把使用部分搬回 HBM，再由算子读入片上缓存；它在没有专门搬运指令、复用率高或 host 链路拥塞时容易验收。在支持相应 TMA 与互联语义的设备上，另一条条件路径可把 host DRAM 的这一部分直接送进 SMEM，让本地 HBM 工作与远端取数重叠。它改变的是一次 operator 的搬运计划，不是增加一层可常驻的缓存。`
- 紧接代价/回退：`运行时须限制在途 host 请求，按 operation 的远端访问敏感度分配 offload 比例，并核 SMEM 占用、链路带宽与等待时间；远端流过多会争用互联，比例升高后 direct/staged 差额可消失。HBM 足够、硬件无该路径、链路较弱或短请求不能摊销控制成本时，原 HBM staging/offload 继续成立。作者离线、短 decode 条件不能外推生产 TTFT/TPOT 或并发尾延迟。`
- 审阅问题：Ch54 最新 peer-tier、LayerSplit、NAND/CXL 路径是否已包含同一 **direct host→SMEM + operation-specific ratio** 选择？若已有则保留报告 Only，勿为名称而加文。
