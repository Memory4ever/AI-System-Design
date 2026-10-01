# W39：通信完成、资源回收与会话复用的有限审阅

**窗口：** 2026-09-20T09:00:00+08:00 ～ 2026-09-27T09:00:00+08:00。
**检查时间：** 2026-09-27T09:50:15+08:00。
**作者：** apr02。
**范围：** 两个 release 家族的具名 correctness / compatibility 主张；未遍历其余功能、全年 PR 或完整发表史。
**状态：** 两项必要来源与具体 Books 差异审阅完成，交 root 做非作者复核与采用裁决。没有实际修改 Books，也不表示 Weekly / Books 已完成。

开始前实际读取当前 AGENTS、Research / Report 合同、统一 Prompt、来源清单相关每周入口、ROADMAP、写作指南与学习理念、PROJECT_CONTEXT，及本周 discovery；再读 Ch36 的 completion、kernel remote-memory、policy publication / direct IPC 与版本化状态论证，Ch35 checkpoint 的提交边界，Ch37 operator / collective 交接。没有以旧报告标签替代证据。

## 1. 准入、日期与最低审阅投入

| 家族 / 当窗事件 | 日期证据 | 相对已有认识的具体增量 | 三维评分 / 实际审阅 | Books 提案 |
| --- | --- | --- | --- | --- |
| `SF-2026-VERL-0-9-1-WEIGHT-REFIT`：[verl v0.9.1](https://github.com/verl-project/verl/releases/tag/v0.9.1) 的 final-ACK / IPC cleanup 修复 | release `published_at=2026-09-20T07:24:43Z`，即09/20 15:24:43+08；tag commit `1876b06d0a3e4e71e06230be10af14492ca8a75b` | 权重已被接收处理，不等于共享映射已经释放；实测表明删除无用GC可暴露被偶然延时遮蔽的回收race。需把最终ACK的释放前提与sender reclaim明确分开 | **3 + 2 + 2 = 7**；深入完成受影响机制、pinned代码和三组反证，不审整个release | `TRAIN-DISTRIBUTED-TRAINING` / Ch36 有窄缺口，建议实际整合后再记“整合”；现在仅提案 |
| `SF-2026-NCCL4PY-0-6-0`：[nccl4py v0.6.0](https://github.com/NVIDIA/nccl/releases/tag/nccl4py-v0.6.0) 的 cooperative session / artifact pairing / launch-event合同 | release `published_at=2026-09-23T17:51:45Z`，即09/24 01:51:45+08；commit `893470119efc83fb6ecd4f9240efcf60c0aef6a3` | 显式销毁缺失可使后续barrier静默不再同步；CuTe生成代码与host runtime / device IR须成套，launch-event本身也有rank/group/lifetime约束。这些是安全复用和版本兼容的调用前提，不是性能宣传 | **2 + 2 + 2 = 6**；实际保护行为 / 发布合同变化触发深入审阅所影响内容 | 同一 owner Ch36，建议与上项形成连贯的completion / lifetime分支；未实际写入 |

评分对象仅是上表的具体命题，不是整个框架或NCCL成熟collective原理。两项准入因具体失效路径和可检查调用条件，不因版本号、名称或能映射章节。

verl [#7873](https://github.com/verl-project/verl/pull/7873)原始公开 `created_at=2026-09-15T13:26:22Z`、`merged_at=2026-09-15T14:25:27Z`，merge `e488469bbf5d62bd921ca41ff746ad90768d2ff3`。这是窗前机制披露，本周事件是包含修复的正式版本发布；不能称本周首次发现ACK算法。报告最终还须由root按此前有效Daily审阅去重：若同一修复已经完成有效审阅，复用机制证据，只保留本次发布采用范围，不重复评分或新增家族。此次有限任务没有独立检查所有Daily去重记录，不能预称已完成跨日去重。

nccl4py是Python / CuTe binding事件，不是当窗首次C++ NCCL 2.32.3发布；release明确device API仍experimental。它与verl的关系是 **Principle Reuse / Layering**：两者独立暴露通信资源生命周期，不是前者直接演进成后者。

## 2. verl：数据回执与释放回执不是同一边界

### 实际阅读的原始证据

- [#7873 What does this PR do / Test / Design & Code Changes](https://github.com/verl-project/verl/pull/7873)：读取问题、A/B/C allocator snapshot、未测路径与具体改动，不扩审全部关联PR。
- [v0.9.1 pinned bucketed_weight_transfer.py](https://github.com/verl-project/verl/blob/1876b06d0a3e4e71e06230be10af14492ca8a75b/verl/workers/rollout/vllm_rollout/bucketed_weight_transfer.py)：实际核 sender末bucket send / recv / finally cleanup、receiver receive_weights / cleanup。
- [必要PR文件差异](https://github.com/verl-project/verl/pull/7873/files)：核 `_ack_pending`、`del weights, tensor`、最终ACK后移、loop变量残留引用及 engine_workers 的 synchronize / empty_cache。

### 旧方案为何看似有效，约束在哪变化

同步bucket传输用ACK串行化sender和receiver，在单一路径中易于推理。但旧实现把最后一个bucket“callback执行并同步结束”当成可以回复的时点，receiver此时仍持有buffer映射。sender收到ACK后删除自己的buffer，CUDA IPC的consumer计数尚未归零，allocation进入limbo而不是立即释放。`ipc_collect()`只能处理计数已归零的条目，`empty_cache()`也不能回收allocator仍认为存活的块。

旧全量Python GC没有收回相关对象，约433ms延迟却给另一个进程留出了释放mapping的时间。因此旧配置的显存结果正确，不证明协议顺序正确；直接删GC的更快路径反而在每轮留下整个2GiB bucket直到下一轮。这里暴露的是跨进程释放次序，不是GC在所有训练路径都无用，更不是无限累积泄漏。

### 状态、控制流与实现

receiver处理bucket后先等待引用它的device操作结束，删除临时weights / tensor引用；非末bucket仍按正常REQ/REP节奏回复，末bucket设置 `_ack_pending`，进入cleanup。cleanup先同步、删buffer映射和SHM view、做现有IPC / allocator清理，再在socket关闭前发送最终ACK。sender收到这个ACK后才进入自己的buffer cleanup。sender还清空async-for残留的name / weight引用，避免最后一个IPC对象被Python循环变量保留。

因此成功路径的ACK被强化为释放边界证据。它不自动提供失败ACK、timeout、任意callback偷偷保留引用的检测，也没有把in-place权重装载变成原子policy事务；现有manifest / revision / poison-rebuild合同仍须保留。engine_workers移除aggressive GC后仍显式同步非阻塞D2H，不能将“删GC”偷换成“删所有同步”。

### 对照、代价与非证明项

作者配置：1节点、Qwen3-0.6B、VeOmni/FSDP2、param与optimizer offload、vLLM TP2、`gpu_memory_utilization=0.6`、GSM8K GRPO、2048MiB bucket。rank0 trainer/sender用torch memory snapshot；各配置5个连续同步轮次、排warmup。**GPU型号、precision、输入/输出长度、有效并发、完整吞吐与SLO：Not Disclosed**；这些不是本次作者声称测量的性能目标，不能补造。

| 作者局部配置 | Snapshot reserved | 未释放bucket | 分配至cleanup结束中位数 |
| --- | --- | --- | --- |
| A：保留GC的baseline | 0.039GiB | 0 | 754.0ms |
| B：只删GC | 4.000GiB | 2048MiB / 每轮 | 275.6ms |
| C：删GC并重排ACK | 0.039GiB | 0 | 324.4ms |

机制证据不只是表格：A的free_requested由ipc_collect归因，B对应地址一直active_allocated并占着额外segment，C由sender `del self.buffer`立即产生释放，ipc_collect无allocator事件。C并非比B每项都快；它以正确释放顺序换取可回收显存，局部中位数也不是端到端训练吞吐或tail SLO。

未测：Megatron、TorchTitan、Automodel、SGLang、SHM、LoRA、多节点、单weight超过bucket的direct路径。PR对direct对象的删除先于ACK是实现上的同类修正，但作者明确小模型没走到该分支；不能写成该路径已实验验证。该评测未由本任务复现。

## 3. nccl4py：复用依赖全组显式收尾与完整artifact身份

### 实际阅读的原始证据

- [0.6.0完整release](https://github.com/NVIDIA/nccl/releases/tag/nccl4py-v0.6.0)：Breaking Changes、Compatibility、Barrier Lifecycle与launch-event；其余ReduceCopy / NVLS / CFT仅识别范围，不扩成候选。
- [pinned barrier.py](https://github.com/NVIDIA/nccl/blob/893470119efc83fb6ecd4f9240efcf60c0aef6a3/bindings/nccl4py/nccl/core/device/cute/barrier.py)：模块docstring32–36及三类session的destroy方法。
- [pinned barrier示例](https://github.com/NVIDIA/nccl/blob/893470119efc83fb6ecd4f9240efcf60c0aef6a3/bindings/nccl4py/examples/cute/05_barriers.py)：LSA / GIN / hybrid各sync后全组destroy、GIN backend gating及示例的API版本提醒。
- [pinned communicator.py](https://github.com/NVIDIA/nccl/blob/893470119efc83fb6ecd4f9240efcf60c0aef6a3/bindings/nccl4py/nccl/core/communicator.py#L403)：launch_completion_event字段403–417及materialize转换。
- [pinned nccl.h.in](https://github.com/NVIDIA/nccl/blob/893470119efc83fb6ecd4f9240efcf60c0aef6a3/src/nccl.h.in#L216)：同一host契约216–221。
- [pinned README](https://github.com/NVIDIA/nccl/blob/893470119efc83fb6ecd4f9240efcf60c0aef6a3/bindings/nccl4py/README.md)：支持Linux、Python>=3.10、对应CUDA major安装extra、show_versions。版本展示不等自动证明runtime / IR成套。

### 必要机制与失效边界

通信library把资源封装为session后，Python对象结束不是device cooperative-group收尾的证明。CuTe LSA / GIN / hybrid session在最后操作之后，每个参与thread须在uniform control flow恰调用一次destroy。LSA与hybrid由此可安全复用同handle/index；官方模块明确，省略可能使后续barrier不再同步，**而不发生挂起**。所以“没deadlock”不能作安全复用验收，不能只由一个thread执行析构，也不能依赖host GC。

这同时放大了ABI / artifact身份压力：0.6.0 host bindings与CuTe API由NCCL2.32.3 headers生成，使用CuTe必须配同版 `libnccl.so` 和 `libnccl_device.bc`，binding不自动检查。安装包版本或成功import不能证明两件artifact一致。旧NCCL2.31.2 device IR在EFA GDA下可导致Gin.put JIT失败，release只将修复归于匹配的2.32.3 IR。示例还明确某GIN入口旧版按值 / 新版指针传参的差异可能造成memory corruption而非链接失败；这支持“兼容不能只看能否链接”的窄机制，不要求本周再审整个历史IR。

launch_completion_event进一步提醒，完成信号本身是有类型、范围和寿命的接口。其官方定义是caller-owned、rank-local、在collective kernel launch completion记录的CUDA event；不是本任务自行推断的整个collective / 数据传输完成证明。要求timing-disabled，禁止interprocess / interop，所有rank同时提供或同时省略，group内每communicator至多1个非空event，并保活到全部queued waits与captured graph executions结束。**CUDA<12.3仍可能记录event，但在launch之前**；不能写成“旧CUDA没有event”或让消费者一律解释成post-launch。

`ThreadScope.THREAD` raw整数3→10是本release版本事实：用enum成员无需改，序列化raw值须更新。它支持类型身份不能任意抹成整数，但单独不是长期机制的评分对象。

### 权限、代价与未证明项

以上证据是官方API / 实现合同，不是性能实验。需要额外显式teardown、uniform参与、caller管理event lifetime，以及部署时核artifact配对；控制面负担上升，exchange范围变化时还要重新验rank一致性。不能反推本任务已经证明错误配对一定在所有机器crash、destroy足以包办所有memory ordering、或event能替代任意completion primitive。

具体hardware、模型、dtype、shape、message长度、batch、并发、SLO和收益数字均没有针对这三条合同披露benchmark；**Not Disclosed / 非本次API语义证据适用的评价维度**，不采用ReduceCopy性能或任意GPU加速宣传。示例需要支持的NVIDIA设备与GIN-capable网络；本任务未执行CuTe、JIT、两节点barrier或错误pairing测试。常规host collective、无需kernel内peer访问的实现仍是简单有效的分支，experimental device path不能无条件替代它。

## 4. Ch36 真实差异与连贯写入建议

### 当前承载了什么

- Ch36「Collective进入计算图后，Completion也成为Autograd语义」已说明async readiness、rank ordering、out-of-place仍有lifetime / alias问题；不能写成此前没有完成概念。
- 「从Collective Call到Kernel内Remote Memory」已有registration、peer、memory lifetime、ordering / completion与failure，但没有cooperative session复用可能静默跳过同步、成套host / device artifact或typed launch-event寿命的具体分支。
- 「通信对象从无类型字节演进为有版本的训练状态」下，direct IPC publication已有manifest / completion receipt、物理device、handle lifetime、部分in-place失败poison / rebuild。
- TensorHub的unpublish / drain和phase overlap的reader quiescence已有“不可在reader退出前更新/复用”的大原则；没有揭示数据callback成功ACK和mapping-release ACK不同、以及GC延迟掩盖IPC limbo这一证据。

因此是**补全已有主线的条件分支**，不是另开“verl使用教程”或“NCCL版本手册”。可将两项合并在Ch36「从Collective Call到Kernel内Remote Memory」之后、进入「从Collective到AI State Transfer」之前，先明确completion契约，再自然引入后文weight-state publication。或在两处原论证就地精炼并互相链接；同一机制仍只有本章owner。

### 最小正文提案（尚未写入）

通信资源的“完成”至少需要区分数据可以被消费、producer可以回收共享存储，以及同步会话可以复用这几个边界。单进程串行调用常将它们重合处理，跨进程alias与kernel内cooperative会话却让参与者的最后引用和控制流成为协议状态。回执必须声明它证明哪一种边界；等待足够久、Python对象被丢弃或没有deadlock，都不能替代这种证明。

在线weight publication中，receiver完成callback并同步device操作，仍可能保留producer buffer的IPC映射。若最终ACK先发，sender删buffer时consumer计数未归零，存储只能进入延后回收状态；额外GC即使没有回收对象，也可能用延时偶然遮住race。安全次序是最后使用结束、receiver释放共享view / 临时引用，再发释放回执，producer才回收；不能为提速先删同步或只缩短GC。已发布的verl修复在指定单节点vLLM bucket路径给出三组allocator对照，但不证明任意callback、后端、多节点或失败路径均满足同一合同。

kernel内会话还须由参与group共同收尾，而不是由host对象析构代理；最后操作后以uniform control flow恰销毁一次，才允许受该API保障的handle / index复用。编译时header、运行时library和device IR也共同定义调用身份，链接成功不表示成套兼容。launch event同样只证明官方定义的阶段，必须保留rank一致性、允许的event类型与所有queued wait / graph consumer的寿命；旧CUDA记录在launch之前的分支不能被下游解释成更强的完成承诺。这些条件提高正确性，也增加控制流、deployment validation和资源管理成本；不需要深度融合的负载仍可使用成熟collective与显式同步。

### 相邻章节交接

Ch35的manifest commit拥有可恢复checkpoint真值，不能用某次IPC释放ACK或launch event替代shard完整性 / 持久提交；本提案不在Ch35重复解释通信cleanup。Ch37只消费Ch36的通信合同来恢复column / row operator结果，不能因降低collective等待把partial sum readiness或rank membership省掉；本提案无需改其矩阵主线。policy epoch publication的最终事务仍由现有Ch36后续weight-state段拥有，本提案不把释放证明变成policy版本完整性证明。

## 5. 安全终态与交接

- 本有限任务两个family均完成必要官方source / pinned实现 / 关键反证与具体owner比较，无缺失primary正文或普通未读方法。
- root仍须非作者核采用命题、跨Daily同事件去重、决定最终Books处置，并实际落实必要正文 / source notes后做写后复核。这里的“建议整合”不能直接改成Books完成。
- 未跑GPU、未复现实验、未测试错误IR / teardown反例；未来若采用更强性能或生产保证，需要对应硬件、负载与失败注入证据，本记录不支持这些承诺。
- 不扩展其余release功能、普通commits或窗前关联PR。必要证据弱于泛化说法时收窄，不因一般原则已出现就丢掉真实race / 静默同步失效证据。
- 唯一写入为本文件；未修改Books、Daily、共享checkpoint，不stage / commit / push。

## 6. 实际 Books 写后独立验收

**复核时间：** 2026-09-27T09:59:39+08:00。
**正文作者：** root。**写后复核者：** apr02（未写此次 Books 正文）。
**结论：** 两项实际章内整合写后通过；本节更新前面“尚未写入”的提案阶段状态，不代替整份 Weekly 的独立 Gate。

实际顺读 [Ch36](../../../../../books/part-04-training-system/36-distributed-training.md) 第304行起新小节「数据可用、存储可回收与同步会话可复用不是同一种完成」的三段、前面的 kernel remote-memory 共存限制，以及后面的 AI state transfer 交接。两个 family marker 实际位于312–313行，Review notes实际位于1599–1600行；不是仅有来源名或“已吸收”标签。

1. **verl：通过。** 306–308行从三个 completion 范围推到 receiver mapping / consumer count / sender reclaim 的顺序，准确对应已核 pinned-v0.9.1 cleanup。正文没有把GC无实际回收误写成所有GC无用，没有把局部延后释放误写成无限泄漏，也没有把释放ACK变成policy原子提交。callback额外引用、timeout、partial load、未测后端 / 多节点 / 大tensor限制贴近机制。Review notes明确09/15 PR先公开、09/20版本发布及作者受限配置、硬件等ND和未复现；没有把本周release改成机制首发。
2. **nccl4py：通过。** 310行把全参与group uniform / exactly-once teardown限制在对应device API所保障的handle/index；静默失去同步不等挂起，与已核barrier.py一致。正文与notes共同保留header / runtime / device-IR成套、binding不自动校验、event类型与rank一致性、queued wait / graph寿命、group每comm至多1个及CUDA<12.3 pre-launch分支。没有把destroy或event泛化成所有data readiness、memory ordering或生产安全的充分保证；experimental / 未运行GPU和JIT的限制仍在notes。
3. **取舍与交接：通过。** 新段承接前文library隐藏约束转为kernel程序责任，并以显式收尾、部署校验、资源管理成本解释复杂度；成熟collective / 显式同步回退仍在正文。Ch35已读的manifest / durable commit主线未变，新段明确保留其owner，不拿通信ACK或launch event替代Checkpoint完整性。Ch37已读的operator / collective分工未变，本次不改column / row语义，也未赋予设备teardown数学结果验收权。后续policy publication的poison / rebuild合同依然拥有in-place失败处理，不被三段替代。

有效必要来源和此前已读相邻内容未改变，复用了第2–4节的精确版本证据，不重读未采用附件或整份release。本次实际新增检查是root写入后的正文 / source notes及相邻连贯性；未执行设备实验、部署或故障注入。root另已报告两项不与09月有效Daily重复身份，日期去重裁决由其汇总；本复核未冒称独立重跑全部Daily。

两项当前实际Books处置均可同步为 **整合：`TRAIN-DISTRIBUTED-TRAINING`，Ch36上述小节**。来源审阅、root非作者准入核与本次非作者实际写后核已分别完成，但到期Weekly其他候选、来源限制和日级/周级最终验收仍归root。apr02只追加本文件，没有修改Books、正式报告或共享状态。
