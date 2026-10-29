# Sep20 补充：LEAP 与跨模态语音蒸馏的必要证据

作者 REPAIR §95 明确确认两必要域未开始、无在途请求，root 接受后首次准备。仅补下列候选的必要机制、直接对照、关键反侧和费用；原准入、各6分及独核§94 Sep19 BJT联合公告日复用，不第三审日门。作者负责唯一非准备者实际采用，再推进当前 Books owner；本文件不授 Books 或整日完成。

## 精确原件与实际范围

2026-10-23 UTC23:44:45～48 两个独立请求实际结束，无仍运行请求：

- [LEAP 2509.14781v1](https://arxiv.org/html/2509.14781v1)，`ROOT_CORE_14781_20261024.raw`/同名 `.request.json`：200/exit0，171056 bytes，SHA256 `94c4009fe00ec898a629b5efb1a07ff90a455dc6538b3b089c1c1cb55948dfa9`。实际完整读 §II～VI、§VIII，含 Tables I～III、必要图 caption；未核所有图像素、实现或复现，不采曲线上未读精确点。
- [Cross-Modal Knowledge Distillation for Speech Large Language Models 2509.14930v1](https://arxiv.org/html/2509.14930v1)，`ROOT_CORE_14930_20261024.raw`/同名 `.request.json`：200/exit0，115788 bytes，SHA256 `aff75ea1078c3974a652bbf6c0783cd3b292c82842df471b5c8761456e84505a`。实际完整读 §2～5 和 Tables1～4；Table1 位于 §1 的排版区域，已单独补读，不误记随§2已读。未听音频、审代码或复现实验。

## LEAP：矩阵切得下，不代表通信与动态计算跟得上

静态权重适合驻留 PIM crossbar，Q/K/V 与 attention score 等运行时数据则随请求改变；论文把 static-weight MM/MVM 放进 RRAM PEs，把 dynamic-dynamic MM、Softmax 和 partial-result aggregation 放进带 SRAM scratchpad 的计算 router。PE/router 成 macro、macro 组成2D mesh，核心增量是把计算、局部存储和通信一起映射，不是所有运算都直接由存储阵列免费完成。

§II 的 `4D²` 与 `5SD+S²` 是所画 attention 布局的数据量近似，不是通用 MHA/GQA/MoE 的完整显存公式；没有逐项 byte/生命周期定义时，不能替代 KV 容量预算。§III 的行列切分会引入 broadcast/reduction，D×D 权矩阵需 ceil(D/C)² arrays。MHA 图对 GQA 通过复制矩阵处理，会改变驻留/复用优势，不能默认为与原生 GQA 执行同费。

空间映射把同一权矩阵限定在邻近矩形、row/column-major 排列，以 coarse X–Y routing 的通信时间估计搜索。其在 2592 个受限候选里接近最低，不是整个映射空间的最优定理；1024²示例的1440配置/20秒与后面2592个 Llama1B 配置不能并成一次相同搜索。时序映射沿 sequence tiling，内循环空间展开、K/V shards 轮转广播；DDMM 的部分 score 还需 reduction，在线 Softmax 累积 rowmax/O，不能把局部 Softmax 当独立概率归一后直接相加。decode 只有新 Q、逐步追加 KV，router pipeline 反而可能闲置；均衡 scratchpad 布局不保证所有算力均衡。

§V 给出双 bank 指令存储、最多两条不冲突 CMD 并发、router FIFOs/IRCU/multicast，是受其数据流约束的调度机制。不是任意图、任意路由或动态请求调度正确性证明；没有核过 Python compiler/hex 或芯片程序实际运行，不写成生产可用 runtime。

**评价权限是合成/估计加指令模拟，不是流片实测。** 数字逻辑在45nm综合/仿真与place-and-route，数字结果再缩放7nm；scratchpad 用 CACTI，RRAM PE 的 area/power 引既有工作。端到端吞吐来自定制 instruction-level simulator。TableI 以 Llama3.2-1B 配置为例，128²/8-bit crossbar、32KB/16-bit scratchpad、64-bit packet/16 MAC；不由8-bit cell推断完整模型与 GPU 数值/质量匹配，未见必要质量/PPL控制或模拟非理想误差验证。

TableIII 在1024 input/1024 output下，Llama3-8B 为202.25 tokens/s，A100 78.36、H100 274.26；13B为120.62，A100 47.86、H100167.51。故所列吞吐低于H100；2.55倍等仅这些配置相对A100的作者模拟报告，不是所有GPU/负载更快。报告功耗 ours10.53W、A100约300W/H100约350W，未交匹配精度、batch/concurrency、GPU软件/版本、host/I/O/装载与整板功耗边界及SLO；不能用芯片估算与GPU平台数字签独立端到端能效优势。

TableII 的数字还有内部不一致：32.37/37.80/90.48 μW相加160.65，但PE标15.08%并不等32.37/160.65；三面积.0864/.0125/.021之和.1199而total印.1181。router表中功耗占56.32%，正文却称75.10%能耗。保原数字及口径冲突，不替作者重排成闭合预算。§VI-D 明确decode吞吐较prefill低4～6倍，瓶颈转到数据移动和IRCU DDMM；64-bit/16-way“near-optimal”只该模拟的探索，不是性能前沿普遍定律。参数规模增大时吞吐亚线性下降还依赖更多空间资源与路由长度，不能称同硬件固定容量强扩展证明。

完整费用包括全部模型驻留/重复权重、scratchpad/KV容量、广播/partial sums/动态MM、软硬映射搜索、指令生成和控制、装载/host与数值校准、独立质量/端到端实机验证。未披者不补测量。有限支持为“权重、动态状态及partial sums的不同驻留/消费方式，需要联合partition、spatial placement与temporal tiling；加快PIM后瓶颈可迁移到router”，不采通用无损recipe、实机倍数或全局最优。

## SpeechKD：旧模态保持与新模态对齐是不同消费者

§2 用文本基座读文本 T1、语音模型读相同文本 T2、语音模型读对应语音 T3，分别比较 T1→T2 与 T2→T3。它给出可复查的诊断分解，而不是仅凭差值唯一识别参数遗忘/语音编码的因果。不同 speech models 的原训练/模板/数据等仍可能共变；Freeze-Omni 的文本行实际缺测，不能把“冻结因此避免遗忘”的论述当本表测得文本不变。Table1 使用非 full AlpacaEval，不能与官方整套数值无条件横比。

§3 的 teacher 为文本模型，student 分别读原文本 Q_t 或 CosyVoice2 从 Q_t 合成的 Q_a；两通道以 gold 或 teacher-generated hard response 作 CE，并可加温度τ²缩放的 KL。文本通道提供旧能力约束，语音通道对齐合成语音条件下的输出，不把teacher文本知识当声学真值。§3 允许输出序列长度不同，却未给 KL 的逐位置对齐/共同前缀、vocabulary映射、mask与归一的完整定义；不能补 teacher-forcing 或 KL 方向作为原文已实施细节。hard-target teacher CE 与 soft-distribution KL 是两个不同监督接口，不把“KD”统一当都需 logits。

§4 用 Qwen2.5-Omni student、Qwen2.5-7B-Instruct teacher，OpenOrca22,456文本/44,753语音样本，2 epochs、lr5e−6、λ.5/τ2。合并通道会增加训练人口/消费预算，未给同总token/更新步的matched重复语音或文本控制，不从合并组的更高分唯一归因“防遗忘机制”。teacher label的正确性、合成语音保义/噪声与真实语音泛化也未独立认证。

直接结果和反侧应一起保留：Table2语音整体base75.08，gold CE71.25，CE+KL74.40；teacher CE75.66、再KL75.76，双通道teacher CE77.19。gold CE可退步，不等 CE 一般无效；加KL也未恢复gold组至base。双通道整体较好但AdvBench99.23低base99.80，teacher CE+KL的OpenBookQA79.56也低teacher CE81.09；总分改善不是每项保持/安全保证。Table3文本整体78.60→78.95→79.86，仍低Table1同teacher82.81，且S2T单通道IFEval57.50低base59.70、两蒸馏组AdvBench99.42低99.80。没有完整重复/CI，微小差不签统计显著或全面恢复。

Table4改用 Kimi-audio toolkit加GPT判分，不是官方regex，不能拼成官方MMAU成绩。S2T+T2T music69.16低base70.36、sound80.48低81.38，Avg74.30亦低S2T单通道74.90；语义通道不自动保持非语言声学任务。再加6181 Clotho AQA是另一个训练预算/人口。最后一行68.01/84.08/74.77的算术均值75.62，印Avg78.95未给另一个权重或分母恢复；仅记录这处聚合未闭，不把75.62冒充官方修正版、不采用78.95作统一改善。原“Sound/Speech同时提升”也未改善music，不把新数据效益归纯双通道算法。

完整费用包括文本teacher生成或logits、TTS合成/保义检查、两通道训练及原backbone/编码器、AQA增量、全部task/judge和保持回归。未披完整参数更新支集、hardware/precision/batch、seq/混合比、teacher缓存/前向、总token/墙钟/费用、API版本与SLO，不补无额外成本或更可靠部署。有限支持为“加模态应分别验旧文本保持、同语义跨模态消费和非语义声学能力，蒸馏目标与数据预算都进入适配身份”；不采参数遗忘唯一因果、所有模态能力同升或闭合KL执行recipe。

两篇各原6/确定候选保持，必要支持与关键反侧足够即停。当前 Books 差额及各自处置仍待作者比较，不以No Change制造或消除上述限制，不为凑整合修改书稿。
