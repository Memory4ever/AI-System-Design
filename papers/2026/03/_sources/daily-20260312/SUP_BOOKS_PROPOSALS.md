# 03-12 补查：root 共享 Books 写入建议

## 2603.09616 — MODEL-MULTI-HEAD-ATTENTION

位置：Ch15“Head怎样分化，又为什么会冗余”，剪枝段后、Scalpel段前。下面逐字正文已由root实际写入；非写入者review_mar12实际顺读新127/129、115–159完整邻接及自身340末注并回对v1，POST通过。仅该owner两段窄差额，不是本日日级验收。

BOS 上的注意力概率质量集中只是一个诊断模式，移除某个 head 对当前任务影响小，也不证明它永远没有可训练容量。资源允许时，可以把定点恢复作为 pruning/gating 之外的替代分支：重初始化选中 head 的 Q/K/V 投影，将其 output projection 置零以降低初始残差扰动，再冻结其他参数，只对目标参数短训。[BLOOM 的受限实验](https://arxiv.org/html/2603.09616v1#S3)支持这条方法分支，而不证明所有 sink 都源于同一位置病因或所有被剪 heads 都值得恢复。冻结权重也不冻结共享 residual stream 的输入，目标头改变后，未改头的 attention 行为仍可能漂移，因此干预验收不能只看选中 heads。<!-- source-family:SF-2026-ARXIV-2603-09616 -->

恢复的诊断容量与最终任务效用必须分账：按 BOS mass 阈值重新变“健康”，不等于 held-out 质量、语言分布和真实任务保持。该实验的完整手术只在 BLOOM-1b7 上验证，出现 held-out perplexity 上升和生成语料印记；额外健康头的单 seed、单列瞬时训练 loss 改善也不能签发通用收益。训练语料、阈值、短训预算与全模型回归均有成本，原文斜率公式/表与“高索引斜率更陡”的归因冲突不在这里采用。质量回退或预算无法摊销时，保留原 heads，或继续采用已验证的 pruning/gating 与实际执行路径，而不是用一张 head-health 图替代质量验收。<!-- source-family:SF-2026-ARXIV-2603-09616 -->

拟末注：

- `SF-2026-ARXIV-2603-09616` — Daily `2026-03-12`补查；[exact-v1](https://arxiv.org/html/2603.09616v1) §3、§4.1–4.7、§5.1–5.5/AppendixB–C。2+1+3=6，中心位置归因反侧额外深入；只采用目标QKV重初/output0/gradient mask短训与冻结参数不冻结共享输入的条件分支。health/任务效用分账、held-out与语料印记反侧、单seed与有限模型边界近文；斜率公式/表冲突隔离。C4 validation split用于训练，Table3所谓held-out样本划分未由本轮实现核验，不把局部PPL写作独立泛化认证。未执行代码/复现实验；必要Source/逐字PRE/实际正文与完整邻接及自身末注POST均由非作者review_mar12实际核通过；非日级Gate。

## 2603.09511 — TRAIN-LORA（root已实际写入，非写入者POST通过）

实际位置：Ch30“为什么会节省训练显存”中“精确收益必须拆分weights…workspace”之后、MeSP重算分支之前；前段已说冻结base仍需inputgradient与activation，后段再讲recompute，与此编译期分支不同。下文保留作者原提案，不冒充root逐字版本；root必要Source及actual owner PRE后实际窄写两段，supplement_20260312非写入者已顺读新151/153、128–185完整邻接及自身812末注并回对已读精确原证，actualPOST通过，root末注同步，锁释放；不授DAY。

当端侧设备的约束从 trainable state 转为跨层级驻留与搬运时，低秩参数化还需要进入完整执行图：先把 forward、backward 和 optimizer update 静态表示，再联合 kernel tile 约束与 tensor liveness 安排内存，决定哪些 active tiles 放在局部 SRAM、哪些状态暂驻或搬向外部内存。它利用的是完整训练 step 的可见性，不是冻结基座后取消输入梯度；LoRA 的小矩阵也只是图中的算子，仍须支付布局转换、DMA 与 CPU/accelerator 同步。参数化、图调度与可执行 kernel 因此是三个共同验收对象，而不是按 trainable parameter 比例换算设备吞吐。<!-- source-family:SF-2026-ARXIV-2603-09511 -->

[TrainDeeploy 的受限比较](https://arxiv.org/html/2603.09511v1#S6.SS2)显示，减少梯度状态和外部搬运，仍可能因许多小 GEMM 的低利用率与额外传输，让加速后的 LoRA 略慢于同范围全层更新。该证据是 GVSoC 模拟器中的 FP32、小型视觉 Transformer 与特定 RISC-V/RedMulE 层级，不是实际硅片、LLM 或生产 SLO 验证；batch-8 少样本质量与 batch-1 设备 step 性能也须分账。因而质量、完整峰值内存和目标硬件净时间应一起比较；布局或图调度失配、低秩不满足质量或实际执行没有收益时，保留原 LoRA kernel、较少目标层或已验证的全层更新，不由较小梯度字节数自签低延迟。<!-- source-family:SF-2026-ARXIV-2603-09511 -->

拟末注：

- `SF-2026-ARXIV-2603-09511` — Daily2026-03-12补查；[exact-v1](https://arxiv.org/html/2603.09511v1) §II-B/IV–VI及TablesI–II/Figs5–6。2+2+2=6，TRAIN-LORA完整图/小GEMM执行边界具体差额深入；GVSoC模拟、FP32、CCT0.28M/rank4、8RV32/4FPU/128KBL1/2MBL2/32MBL3/360MHz假定。只采用静态FW/BW/update图联合tiling/liveness与低秩利用率可能反转速度的条件分支；qualitybatch8/50shot/30runs与性能batch1分账，dynamicL3不含weights/input，EuroSATLoRA退步及不同跨框架配置反侧保留。TetriSched/MiniMalloc职责不补实现，未执行artifact/复现或认证实际device/SLO；root必要Source/actual owner PRE通过，root实际写入后的非写入者supplement_20260312正文/完整邻接/自身末注POST通过，不授日级Gate。
