# LongFlow 2603.11504v1：必要 Source / 具体 owner PRE

作者 mar14_supplement。首包完整题摘、有限入口与Mar13日级arXiv日期已由root校准，不重复。评分 **2+2+2=6**：当前query/value贡献与per-step固定slot的融合路径改变评分critical-path成本；跨utility估计、kernel和cache布局；近似/数值/质量边界可复用。不借已有FullKV或通用“proxy非真值”计分。最低标准审阅，因明确owner缺口及理论反侧深入必要局部；独立Source/PRE尚待root，不先改Books。

## 精确原件与实际范围

[v1 HTML](https://arxiv.org/html/2603.11504v1)，保存 `SUP_CORE_11504.raw/.txt`，身份与获取时间见 `SUP_CORE_FIRST_MANIFEST_RESULT.json`。实际读§2–4/Table1/Fig1–3/Limitations及决定性Appendix A.1–A.3、Algorithm1/Fig5 caption；原HTML数学alttext由 `inspect_source.py`展示。未读所有references或核代码/复现，不比较全版本史。

§3.1–3.2/Eq2–6：先把“全未来logit”不可得目标缩为下一步attention输出删除误差，再以当前query替代未来query，最后忽略删除带来的softmax分母变化；采用 `alpha_i * ||v_i||_1` 最小者，不存历次query/累计attention。§3.4/Fig2以query长度1的Decode路径，把本轮 `exp(score_i)*v_i` 同时供output accumulator和L1 reduction，求最小slot；下步用新KV覆盖上一轮选出的slot。prefill超预算先用SnapKV，故不是同一公式解决全prefill。

## 不能照录的保证与可采用边界

1. **贡献向量不是精确删除误差。** Appendix A.1 Eq12–14已有删除后的权重renormalize关系。由其式代数得到（我的推导，不冒称作者新定理）`o - o_without_i = alpha_i/(1-alpha_i) * (v_i-o)`。若单维 `v_i=0, alpha_i=0.9`，剩余一个 `v_j=1, alpha_j=0.1`，原output=0.1、删i后=1，差为-0.9，而LongFlowScore(i)=0：选最小alpha×value-norm不保证选到低attention项。§3.3的remainder界 `2V*alpha/(1-alpha)`仅在实际被删除项alpha小且V有界时支持，作者“tokens很多”或“我们淘汰低attention”不足以保证此前提。Eq7–8分析的是squared L2，Eq6最终L1排名亦不自动由它推出一致最优排名。保留工程启发式，不授global/next-step最优或token无用。
2. **相邻cosine不是任意query保证。** Eq10与AppendixA.2显式假设unit-normalized queries，并乘max key norm；Fig5仅Qwen3-8B layer10/head10、MATH500 100samples的前100tokens均值。不能推广全部层头、长horizon、tool/topic突变或query尺度。Limitations直接保留这些失效场景。
3. **fused不等免费或无临时状态。** §3.4删safe-softmax running maximum、改FP32 exp以避免overflow；Algorithm1确实 `exp(S)` 累加，无max rescale。FP32扩大指数范围但仍有限，不能签成无条件数值安全；这里只保留需要有界score/检测与稳定路径的设计要求，未执行kernel且不声称当前发生过NaN。Algorithm1 line7明确长度t-1的temporary S_loss，line29存score，末尾normalize/argmin；不存历史统计不等“无任何aux storage”，尤其不能直接认定所有该状态驻留SRAM。L1/min reduction、mask/slot index、固定容量及数值guard都要计价。static slots也不自动兼容shared prefix的原地写权限或多租户page管理。

## 必要评价与反侧

§4.1：DeepSeek-R1-Distill-Llama-8B与Qwen3-0.6/1.7/4/8B，output16K、budget2400/3200；H2O/VATP一半heavy一半recent，A10040GB。主表八benchmark样本量30/30/40/198/1318/500/272/675。数学/GPQA这里只是通用推理质量评估，不开展AI-for-Science领域研究。

Table1具体反侧：Qwen3-8B FullKV AIME24/25=60/46.67，LongFlow budget2400=36.67/26.67（分别约23.33/20pp回退），budget3200=50/26.67；MATH Full92.6→88/89.8。DeepSeek MATH83.4→79.8。R-KV多处质量更高。因此平均“negligible/minimal”不能抹平逐任务下降，较小AIME人口又不支持稳定普遍差距，采用局部质量/成本工作点而非不损质量保证。

§4.4/Fig3 throughput仅Qwen3-1.7B，单A10040GB，input512/output16K，budget3200，各方法分别增batch至OOM；LongFlow每步压缩、其他每128步。因此11.8×FullKV/~4×其它混合了最大可容纳batch、动态内存与不同刷新策略，不是同batch/同并发/同SLO内在kernel倍率。Fig1 Qwen3-8B/b128/cache3200同每步evict的H2O vs fused operator局部attention47→8ms更接近局部operator对照，但不能外推end-to-end11.8×或生产可靠性。

whole-model precision、sampling/evaluator具体配置、在线到达/并发、tail-SLO、重复seed/CI：Not Disclosed（FP32 softmax不是整个模型precision）。本地伪代码可核，不等artifact实现/显存占用或真实复现。

## 当前 owner 与差额

唯一owner `INFER-KV-CACHE`：[Ch45](../../../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)。实际读现正文约505–580完整workload-aware eviction/temporal continuity→rank vs refresh→capacity段，以及704–768 learned/future oracle路线；邻章Ch44逐token/小矩阵访存开头和Ch46动态batch语义开头。当前已覆盖attention proxy非causal、query continuity可能失效、token淘汰不等physical page、ranking/refresh分离；这部分不重复写。具体缺口：**当前query下value贡献proxy与删除renormalization的差别，及把当前估计/slot选择并入固定容量Decode operator的路径与数值成本**。不能只列paper名、说省HBM或重述通用continuity。

建议root窄写：在Ch45现 `Attention-pattern classification…temporal mechanism`段后、`即使总预算不变…`段前，插两段，不改既有marker归属：

> 当长输出要求每步检查容量，保存一串历史query或累计attention也会成为critical-path状态。另一条training-free分支只取当前query，将每个token的attention weight乘value向量的L1 norm作为保留proxy；以相邻query近似未来读取，再把score reduction与attention输出一起计算。它估计的是便宜的当前贡献，不是精确删除损失：去掉一项还会重新归一化其余权重，实际输出变化为 `alpha_i/(1-alpha_i) * (v_i-o)`。小value而高attention的项可能分数很低，却强烈改变分母；低proxy不能据此证明低attention或可安全删除，L1排序也不自动继承squared-L2目标的最优性。
>
> 在固定容量、query长度1的Decode里，可让下一步新KV覆盖本轮选出的slot，并在一个operator内复用未归一化value贡献，减少独立扫描与历史统计。融合仍支付L1/min reduction、mask和临时score/slot状态；论文伪代码也保留score vector。若为融合省去safe-softmax的max rescale，FP32扩大范围却不保证任意logit不溢出，需保留有界输入、异常检测或稳定kernel回退。固定slot不拥有共享prefix的原地覆盖权限；相邻query漂移、质量回归或数值/布局不兼容时，FullKV、低频刷新和稳定attention路径继续成立。单卡各自增batch至OOM的吞吐对照只支持对应容量工作点，不能当同并发加速或在线SLO认证。

拟note：`2603.11504v1 §3/Eq2–10、Appendix A Eq12–15、Algorithm1与Table1/Fig3支持当前贡献proxy/fixed-slot融合路线；保留分母反例、L1与L2差别、临时score state/FP32稳定性、逐任务质量和max-batch混杂。未核代码/复现/在线SLO。` 独立Source/PRE通过后才由root实际写入，作者随后做非writer POST。
