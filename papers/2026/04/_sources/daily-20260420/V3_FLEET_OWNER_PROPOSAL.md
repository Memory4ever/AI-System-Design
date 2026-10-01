# Fleet 有限 source → actual owner 提案

作者：apr20_resume；root已有限采用通过并授窄锁，真实Ch49:91/93两段及Review note已写，锁已释放。root 实际写后已通过，计入本日实际整合但未签整日Gate，见 `V3_ROOT_FINITE_INDEPENDENT.md`。

原始证据：[2604.15379v1](https://arxiv.org/html/2604.15379v1)，实际§3.1/4.1/5.1–5.3/6.1–6.4/Table4–5/8，限制详见本日`v3-reopen-notes.md`“15379 Fleet”。2+2+2=6，真实owner缺口触发必要Deep。Owner `INFER-TENSORRT-LLM`，当前Ch49“从逐Kernel Launch到Persistent Executor”：已实际顺读65–100，已有event tensor/per-SM queue没有partitioned-L2 task placement及last-worker跨die完成链；1720的Chiplet Pool是硬件设计池/执行计划联合搜索，不是该运行时同步责任。

拟在现有event-tensor两段之后、host overhead/TaxBreak之前嵌入以下两段，不改变原来源和其他章节：

> Per-SM queue 的局部性还取决于哪些 SM 实际共享缓存。单 die 的统一 L2 下，平坦任务领取可以继续保持简单；多个 chiplet 各有私有 L2 后，任意领取会把同一 weight tile 的并发访问分散到不同 cache partition。此时 execution plan 可以显式增加 chiplet 级 task：按输出列分配 weight slice，再让 chiplet 内的 workers 先遍历共享同一 weight tile 的 batch tiles，使短暂工作集在同一个 L2 内复用。完成责任也随硬件作用域分层：局部 workers 累积本 chiplet 的完成计数，由最后一个 worker 负责必要的 L2 writeback 和 GPU-scope global event，只有跨 chiplet 的完成条件满足才放行下游 task。局部计数不能被误写成任意 memory model 下都免 fence；不可变 task descriptor、cache partition、可见性操作与事件阈值必须共同成为 plan 的条件。
>
> 这条分支以常驻 scheduler 资源、cache 策略和 task 粒度维护换取局部复用，不是把所有 persistent-kernel 加速归因于 chiplet。受限 [Fleet v1](https://arxiv.org/html/2604.15379v1) 的单 MI350X、Qwen3-8B BF16、64 输入/1024 输出、batch 1～64 decode-only 测量中，8 个 scheduler 占 256 CU 的 3.1%；低 batch 没有额外 weight tile 共享，SiLU fusion 在 CU-task 中也有效。batch 32/64 的 cooperative traversal 对 chiplet-unaware megakernel 为 1.27/1.30 倍、HBM read 为基线的 0.82/0.63，但另一种 M-split 在 batch 64 的 read 反增至 1.20。prefill、tensor parallel、多模型及其他 GPU 并未得到同样证明，短 task、寄存器压力或 tile 窗口不能摊销时，应保留原有 static graph、独立 kernel 或较简单的 persistent plan，并重新测完整请求成本与数值正确性。

root必要源→actual owner/literal通过见`V3_ROOT_FINITE_INDEPENDENT.md`末。本次实写第二段按其要求补入实际§6.2反证：batch64 M-tile18.61ms慢于vLLM约11～12ms，尚未K-split/attention优化；对Mirage改善不证明成熟serving或端到端普遍收益。原提案两段除该必要负对照未变，真实位置Ch49:91/93、Review note1947，作者顺读85–104衔接且scoped diffcheck PASS。root 实际正文与相邻非作者写后 PASS，不等于日级Gate。
