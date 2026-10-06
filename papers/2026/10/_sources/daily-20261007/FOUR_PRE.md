# Four minimal literal PRE proposals

Author oct07_missing. Independent Source/date/score=6/owner differences are in READER_REVIEW; none of the following is yet written. Fixed existing text remains unchanged. Per-item literal PRE, root narrow authority and actual non-author POST remain required.

## ORCA

Owner TRAIN-PRETRAINING; books/part-04-training-system/28-pretraining.md

Anchor and personally read context: 在现有固定全谱两段（包含SF2605-12492 marker）之后、`固定全部 singular spectrum 比只约束最大增益更强`之前。完整optimizer invariant局部已读；Ch27/29交接已读。

Exact proposed single paragraph:

谱约束也可以只在早期塑形，而不作为整个训练的不变量：对矩阵参数暂时加入软正交项，再到 release point 清零这项，恢复原 optimizer，让后期谱自由适配任务；embedding、head 与一维参数仍可采用不同更新规则。[ORCA 的受限阶段对照](https://arxiv.org/html/2610.06116v1#S3)支持这种 early-shaping/later-release 分工，不能由 effective rank 单指标推导整网收敛；持续或晚加约束有终点反退，早期塑形也可暂时提高 loss。Dense 的统一解除比例不能搬到 router-sensitive MoE，后者在原实验按层分阶段解除。Regularizer、解除日程、optimizer state 与额外矩阵运算都须随训练配方保存；token预算、末期LR decay或尺度变化后重验质量和总墙钟，约束限制适配或无净收益时保留原 Muon/AdamW，不把较少token或局部四seed证据外推成通用加速。<!-- source-family:SF-2026-ARXIV-2610-06116 -->

Own source note proposed: Daily2026-10-07 Oct6; exact-v1 necessary domains as READER_REVIEW;2+2+2=6; only adopted interface above with negative conditions and full costs retained; no artifact or reproduction. Independent Source/date passed; literal PRE/root narrow authority/actual POST recorded only when they occur.

## CentriQ

Owner INFER-TENSORRT-LLM; books/part-05-inference-system/49-tensorrt-llm.md

Anchor and personally read context: 在QFlash段及其marker之后、`#### Rotation Scope 与 Quantization Group 必须共同进入 Numeric Plan`之前；完整分布诊断/邻接已读，48/50交接已读。

Exact proposed single paragraph:

旋转前还要检查逐 token 的均值方向：DiT 的 adaLN 条件化可让这个随输入变化的分量无法静态折入 bias，Hadamard 的行和结构又可能把它集中到少数坐标，使均值继续主导量化 range。一条 calibration-free 替代分支先在原 channel 上去均值，只旋转/量化 residual，再以原未量化权重得到的 `W1` 和 compute precision 补回 `mean(x)·W1`；精确的是线性均值分量的代数分解，不是量化后整层无误差。[CentriQ 的必要对照](https://arxiv.org/html/2610.06260v1#S4)还显示，仅 centering 不救 W4A2，percentile clipping 与均值分离共同影响结果；2-bit 只是模拟量化，不能继承 W4A4 实际 kernel 的时间。Mean/scale、rank-1 分支、rotation/padding、weight拟合与kernel均计费，校准自由不等验证自由；分布、clip或真实执行质量失配时，保留代表性校准、原旋转和局部高精度，不用有限DiT结果认证任意视频、位宽或Serving SLO。<!-- source-family:SF-2026-ARXIV-2610-06260 -->

Own source note proposed: Daily2026-10-07 Oct6; exact-v1 necessary domains as READER_REVIEW;2+2+2=6; only adopted interface above with negative conditions and full costs retained; no artifact or reproduction. Independent Source/date passed; literal PRE/root narrow authority/actual POST recorded only when they occur.

## SLOA

Owner TRAIN-LORA; books/part-04-training-system/30-lora.md

Anchor and personally read context: 在Training-Free OPD完整自然段之后、`若只需保留一种生成结构`之前；实际读ACT-Mat/OPD两侧与gauge语义，Ch29/31交接已读。

Exact proposed single paragraph:

为减少上游合并引入的输入漂移，还可沿部分已合并模型的真实执行路径，逐个用当前中间 activation 对齐原任务模型的局部算子，再按预算 rank 分解回合法参数；对适配后的模型先形成完整有效权重，不独立平均任意 LoRA 因子。这让校准状态随合并路径改变，但闭式局部回归和 greedy 顺序不保证整网联合最优。[SLOA 的受限算子对照](https://arxiv.org/html/2610.06415v1#S3)允许在适用的 attention 结构中合成 QK/VO，含 RoPE 的 LLaMA 实验却只合成 VO、Q/K 分别合并，不能跨结构搬用完整 QK 公式。原 rank 已有局部收益，可选扩 rank 仍增加参数、推理内存/计算且 HumanEval 有退步；仅合成一类算子也可退步。统计前向、局部求解、factorization 和回归均计费，初始化/坐标、校准路径或任务支持不符时保留独立模型、data-free 静态合并或原 adapter，而不由 training-free 标签授予通用能力保持。<!-- source-family:SF-2026-ARXIV-2610-06415 -->

Own source note proposed: Daily2026-10-07 Oct6; exact-v1 necessary domains as READER_REVIEW;2+2+2=6; only adopted interface above with negative conditions and full costs retained; no artifact or reproduction. Independent Source/date passed; literal PRE/root narrow authority/actual POST recorded only when they occur.

## HEAR

Owner INFER-SCHEDULING; books/part-05-inference-system/56-inference-scheduling.md

Anchor and personally read context: 在Pythia的预测/反侧两完整自然段之后、`稳定流程的预测可以先准备prefix和副本`之前。完整infrastructure-aware局部已读；Ch55/57及Ch84消费者交接仍需在写前定点读。

Exact proposed single paragraph:

预测工作流之外，还可让 harness 与 engine 显式双向交换 intent、execution requirement、runtime state/capability 与 outcome，并按消息作用域绑定 request、context revision 或 serving instance；协议只定义语义，两层既有策略仍独立决定具体 cache/priority/mode policy。Intent 不是 control，preference 不等 requirement，旧 observation 不等当前 guarantee，accepted 更不等 completed；实际消费时仍核真实 prefix、容量与支持能力。[HEAR 的受限协议/策略对照](https://arxiv.org/html/2610.06597v1#S3)支持这条跨层接口，但缓存重用可伤最大TTFT，100%负载下复合策略吞吐还低于FCFS；Guard不签任意负载hard SLO。Role-to-mode 来自开发期profile后冻结，citation precision/recall仍有下降，aggregate judge相近不证质量等价。消息/状态维护、在线协调与离线profile均计费；状态过期、不支持、净收益或任务回归失败时，返回明确outcome并保留普通请求、反应式缓存/公平调度，不把接口连通授为执行完成或生产保证。<!-- source-family:SF-2026-ARXIV-2610-06597 -->

Own source note proposed: Daily2026-10-07 Oct6; exact-v1 necessary domains as READER_REVIEW;2+2+2=6; only adopted interface above with negative conditions and full costs retained; no artifact or reproduction. Independent Source/date passed; literal PRE/root narrow authority/actual POST recorded only when they occur.


