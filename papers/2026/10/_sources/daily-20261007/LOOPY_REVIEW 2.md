# Loopy 2610.05265v1 — author evidence and PRE request

Date: exact DOI `arxiv.content`/`findable`, v1 submitted 2026-10-04T14:35:37Z; registered 2026-10-06T04:54:19.000Z. Applicable announcement lower bound Oct6 00:00Z; entire interval BJT Oct6. Exact AB current v1 observed; no withdrawal/correction/earlier-body signal on event page. DataCite raw retained. Score 2+2+2=6; deeper read for shared-depth design counterevidence and packed-path correctness constraint.

Personally read exact-v1 §2.2/§3.1–3.3/§4.1–4.5/Tables1–4, B/B.1/B.2, C.1/C.2/C.3/C.4/C.5 necessary theorem assumptions and proof, D/E. Core original HTML retained (`core-05265v1.raw.html`), necessary rendered source in sixcore1/sixcore2/core4. No code execution or reproduction.

Evidence: fixed shared transformations/quantized weights, full target-depth NLL, nested windows successive halving with cached prior losses. Ranking reversal in §2.2 and C.3 occurs even contractive affine core; construction not an actual LLM contractivity claim. Regret ≤2max epsilon conditional finite fixed pool/set, uniform estimation error not certified by schedule; no held-out/equalcompute guarantee. B.2 targetdepth quality depth controls one run/no uncertainty. §4.3 N10 selection sets, same candidate pool/base/recipe and ordered data per run; calibration cost includes construction, screening, final artifact. B baseline activation symmetry/calibration compute not all matched, failure of adapted baseline not all originals. Recurrent-Llama W4A4 loses versus SpinQuant (PPL42.08 vs41.03, avg32 vs32.5). D H20 decode excludes prefill/init; BF16 KV96slots, eagerFlashSDPA,128generated,10measurements; group128 Loopy vs peroutput baselines; *W4A4 baselines exceed numericaltolerance, W4A8 timedpath fullquality not rerun. Thus no adopted headline throughput, equalbudget universal quality, or live serving claim.

Owner `INFER-TENSORRT-LLM`, Ch49. Actual §粒度与校准 excerpt read 1064–1124; nearest LoopPTQ SF2609.30820 covers stepwise Hessian/reference vs actual trajectory but not full final-loss depth selector/windows-vs-depth screening. Suggested insertion after LoopPTQ two paragraphs and before current partial-quantized curvature paragraph. Ch48/50 only handoff need before mutation (not yet authority). No book write yet.

Exact proposed body:

跨步统计覆盖之后，还要区分“减少校准样本”与“减少被评价的执行深度”。共享量化权重和变换在循环中反复使用时，候选的浅层排序可能与目标深度的最终预测 loss 排序相反；即使每步局部误差较小，也不能批准该候选。可固定目标 recurrent depth，让每个候选完整执行，再逐轮向幸存者分配更多嵌套校准窗口，并复用已经计算的 loss；权重与变换仍跨步共享，动态 activation scale 则可随输入改变。<!-- source-family:SF-2026-ARXIV-2610-05265 -->

[受限全深度选择证据](https://arxiv.org/html/2610.05265v1#S3)支持这条校准接口，不保证逐轮淘汰一定保留最优候选：其 regret 界依赖固定候选集与未被日程自动认证的估计误差，浅层反转也不是所有模型都会发生。较少窗口降低的是准备预算，不是部署时少执行循环；候选构造、筛选与最终 artifact 都计费。有限模型有 W4A4 质量反退，packed kernel 对照还存在数值不一致与实现配置差异，不能把模拟量化质量拼接成等预算 serving 加速。深度、人口或数值路径不相容时，扩大校准、保留更多候选、局部高精度或原浮点回退，并在真正目标执行路径重验质量。
