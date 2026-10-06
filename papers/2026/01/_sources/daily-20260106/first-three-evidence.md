# Jan06 首批必要证据（root 定点独立复核已完成）

本日窗口为 `[2026-01-05T01:00:00Z, 2026-01-06T01:00:00Z)`。exact-v1 题摘先经 root 准入校准；下述原文已实际打开。root 随后核必要原源与具体 owner：Revati 已有覆盖、FlexSpec 争议安全隔离、FlashInfer 两段 Ch49 实际写后通过；这些单篇结果不代表 Jan06 日级 Gate 或实验复现。

## Revati — https://arxiv.org/html/2601.00397v1

采用命题：复用真实 serving control plane 可以消除手写 simulator 的控制逻辑漂移，但在线到达次序仍需要虚拟时间协调，且计算数值和耗时预测是另外两项假设。§3.2–3.3、§4.1–4.4、Algorithms1–2、§6.1–6.3、§8 为必要范围。Actor 的 predictable future target 驱动 all-actor barrier；Observer 只读 wall-time+offset。min target、timeout 退化与 NCCL barrier 避免跳过已声明依赖，不是任意故障下正确性的外部证明。§4.2 的 timestamp/cooldown J≈500µs 条件不能删除；§4.3 <4MB metadata 真内存、compute virtual pointer/CPU-read fatal 检查区分控制数据与被跳过数值。§3.3 固定输出 token 长度而不按真实 EOS，因此不支持质量或值依赖 routing 的任意真实语义。operator predictor 仍需目标硬件 calibration。

§6 是作者实验：4×H200/NVLink、AMD9334/128core、756GB；Llama3.1-8B TP1、70B TP4、Qwen3-30B-A3B EP2，vLLM/SGLang、chunk512、ShareGPT/Poisson。precision、全输入输出长度、每点request总数与统计重复 Not Disclosed。§6.1称各设置mixed batching，而§6.2又以SGLang默认不mixed解释tail差异，故不把因果归因或headline <5%/5–17×外推。固定20ms/0.5–8QPS消融隔离的是时间协调，不证明新硬件predictor。代码未实际运行。Books 已有覆盖：PLATFORM-EVALUATION-SYSTEM，Ch66 1332–1372 实际拥有 real control-plane/virtual execution、host branch/collective/jitter、predictor 与 fidelity/cost ladder；root 必要原源和该局部对读通过，不制造 diff。

## FlexSpec — https://arxiv.org/html/2601.00644v1

原HTML经 urllib 实际取得；web.open 返回InternalError不等于必要材料不可得。必要位置§IV-A/B/C、Algorithm2、§V-A/B。shared anchor复制base末层，target backbone/head冻结并仅PEFT更新；这不是任意target族或新的embedding/tokenizer均兼容。edge one-time feature-regression+KD训练并未消除分布漂移。

中心争议：Algorithm2用draft token==target argmax验证，再直接sample correction；仅上行draft IDs，未披露概率比接受/残差重采样。TableIV温度1/top-p0.9不能据此证明目标分布无损。§IV-B Eτ≈γK与Alg2的(1+γK)/(Tf+KTm)是不同目标；固定γ的线性分式目标一般只在边界最优，不能证明连续channel状态必然带来内点最佳stride。作者测试含H800/A800/V100云与Orin/Snapdragon/iPhone模拟/RPi端，六任务；网络实测/模拟细节及所有每配置预算尚未完整披露。不能把“32A800”intro与多硬件testbed归为单一配置，也不采用一般性speedup。候选不因争议删除；拟Books暂缓，需精确随机verifier、accepted-length模型与相同quality/通信测量证明才能重开。

## FlashInfer-Bench — https://arxiv.org/html/2601.00227v1

更早原项目说明 https://flashinfer.ai/2025/10/21/flashinfer-bench.html 已实际打开：2025-10-21公开Trace definition/workload/solution/evaluation、真实serving workload及apply+fallback；不再把这条闭环计作Jan06首次机制。

本次正文新增可核验边界集中§3.3及§4.5：deterministic按element tolerance且rejectNaN/Inf；lowprecision用matched ratio而不是放大全局tolerance；sampling用empirical TVD+mask violation fail，有限样本阈值不是全分布证明；isolated subprocess/context teardown与persistent模式是不同保证，默认persistent不能称fullisolation。§3.5 prebuilt dispatch index按硬件/compatibility与workload找已测解、无匹配fallback，正确性只在绑定Definition/inputs上成立。

§4.5 same-kernel fallback隔离apply开销，Llama3.1-8B-Instruct/SGLang、fusedAddRMSNorm h4096、concurrency1/16/64、warmup后四request均值。披露baseline0.0112ms比Gemini0.0160ms快，934ms比939ms快，不能说AI生成解优于native。精确长度/不确定性 Not Disclosed；不据此承诺生产SLO。INFER-TENSORRT-LLM 的 Ch49 learned-kernel admission 原有 numerical/interface 合同，但欠缺随机/确定性验收分离及 context 生命周期边界；两段已获独立 source→owner 许可并实际整合，root 对读正文/前后及源注后写后通过。未运行artifact。
