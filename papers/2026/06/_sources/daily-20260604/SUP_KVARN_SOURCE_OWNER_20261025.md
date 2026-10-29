# KVarN 2606.03458v1：首次必要 / actual Ch45同family / 两段最小PRE

R55准入/当前notice/Jun03联合日证已过，不第三。作者正式拟2+1+2=5：双轴在线KV误差调节与AR评价的具体增量主要在cache单组件，具有长期机制边界；不按2bit/SOTA/代码或已读量加分。actual同family缺口触发深入受影响域。无Book新授/未写，待首次必要Source/score/actualowner/PRE，不预I/DAY。

## 原证与实际读界

https://arxiv.org/html/2606.03458v1 GET exit0，完整原HTML423294字元无trunc，剥标保math annotation完整TEXT61468字元真存`2606.03458v1.fulltext.txt`。实际读§2–3全部、4.1设定/4.1.1、主T1–3完整字段、4.2、A/B/C文字说明、D全部必要设置、E完整限制、H完整Alg1与I/J预算；未核图像像素、完整F淘汰对照/G热图或实现/复现。支持及直接关键反侧足即止，不扩附件队列。

## 必要支持与边界

- §3.1把K重构平方误差拆为norm差平方与按norm缩放的direction项，属于几何恒等式/诊断，不是token-scale唯一因果、端到端质量上界或指数爆炸定理。§2.4/C顶端5%替高精度的KL/MSE差为局部诊断；不同outlier量定义与自然AR不能合并成普遍比例。
- §3.2 pseudo-decode将给定sequence分块，每过b个token写入量化KV，后块latent消费先前量化历史，允许跨层/步累积；它不等自由采样生成/完整serving系统。§3.4/Qwen3-4B局部attention-output重构对照只是代理；原旧反馈循环有效不重写或计作新gap。
- §2.2/3.3：head-channel Hadamard处理通道outlier不足以平衡token幅值；token轴直接Hadamard在线反变换昂贵，故在完整块上交替平衡两个轴variance。单token variance归一可能增channel kurtosis；不是rotation与scaling任一必然全好。H Alg1以logscale/clamp与imbalance最优追踪返回两个scale，有限迭代/实际tile不保所有variance严格相等，更不保证全模型数值等价；本次不采用具体阈值/完整数值recipe。
- chunk满后VarN→RTN→编码，dequant需消费两个轴scale/zero-point。D固定G128、sink128与recent128高精度（IFEval sink32），未满block新token不是已2bit编码。A通道head-wise/RoPE位置文字提供布局说明，不把任意变换跨RoPE/投影折入当普遍等价；不声称实现已核。
- D：Qwen3-4B、Llama3.1-8B-Instruct、Phi4及Phi4reasoningplus，reasoning配置分开；Qwen温度.6/.7、top-p.95/.8、top-k20按任务，Llama.6/.9，Phi4greedy/plus.8/.95/50。MATH500/AIME30/HumanEval164三run Avg@3不是pass@3，IFEval541/max1280、math8K/AIME和code16K上限；不是无长度/解码约束。T1 QwenMATH FP16 82.6±.5→KVarN79.2±.4，T2两模型HumanEval亦低于FP16；T3多项略退，不授near-lossless为普遍结论。标准差不是置信区间/多训练seed。
- Baseline精度与实现不同：KVQuant保1%FP16、PolarK4bit、Turbo社区vLLM3/3bit且首末两层不量化；不能把所有差额当严格等预算单因果。A/B/C仅文字/caption读界，不冒像素或所有ablation全定量。KVarN质量对照优于部分rotation-only方法支持双轴具体分支，但未控制全部kernel/metadata条件。
- D metadata披露内部不齐：前文“zeropoints/scales均8bit”，后effective段写twoFP8scales加oneFP16zero-point/G128=2.25bit；表约2.3。不能拼成已验证统一packed recipe或请求总驻留率，sink/recent、padding与额外状态另计。本稿只要求两轴scale/zero-point身份与实际字节共同验收，不采用2.25精确容量保证。
- 4.2 Qwen4B FP16vLLM生成128token1050ms vs所有层8次normalization1.9ms仅局部计时；I单层16head/d128/G128、4K–32K dequant median差≤1.4%不是全请求/并发收益，GPU仅披500TFLOP FP16/1.8TBs，型号Not Disclosed，不猜硬件。E明确公开servingframework端到端2-bit评价受限、MLA影响未知/无KV的SSM不适用。J作者约50GPUdays复算质量实验，非部署净节省。块重编码、onlineHadamard/VarN、FP16sink/recent、scale/zero-point/padding、dequant与质量回归全费用保留，任务/字节/kernel不合格回退高精度/FullKV。

## Actual owner与最小差额

已读三Book上下文、ROADMAP及Ch44/45/46职责。唯一`INFER-KV-CACHE`，actual `books/part-05-inference-system/45-why-kv-cache-speeds-up.md`已有本family KVarN feedback正文及本人之外的旧source注，必须保原归属与日期，不另建owner。完整相关旧正文承载repeated state feedback、dual-axis/Hadamard泛机制、metadata/effectivebit、MLA/GQA/serving限制，不因题名相同NC，也不重复泛反馈。尚未承载“为何单轴不够/交替variance调节”“块满才编码/两scale伴随驻留、未满tail仍高精度”这个实际lifecycle分支。Ch49拥有通用低比特表示，不在其重复此逐块写入过程。

拟仅在旧KVarN三行总结完整段后/Inner-dimension Grouping真H4前加下面原两段及本人trueH2注；保旧段、反馈code与下方inner grouping/2602-23200组，不改旧note。待独核PRE与root具体新授，未写。

### 完整上锚（前侧反馈code一并核读）

静态校准还会遗漏 Decode 的反馈闭环：新 token 的 K/V 是读取已量化历史后生成的，再被量化并参与下一步。
因此 quantizer evaluation 应从一次 tensor reconstruction 推进为 repeated state feedback：

```text
quantized historical KV
→ attention and next hidden state
→ produce new K/V
→ requantize and append
→ repeat under the target generation length
```

Dual-axis normalization、Hadamard rotation 或额外 scale 可以降低某类长尾误差，却增加 metadata、kernel coupling、
mixed-layout migration 与 effective-bit accounting。KVarN 的 2-bit pseudo-decode 实验支持 static error 不能代表
autoregressive accumulation，但没有完整并发、paged sharing、MLA/GQA 与 production SLO；FP16、4-bit 或 mixed
precision 在短输出、kernel 生态不成熟和高精度任务中继续成立。

### 最小原稿（两完整段）

双轴缩放还要说明改变了哪个误差源：在一个 KV tile 内，通道方向旋转能摊平部分 outlier，却不保证每个 token 的幅值被正确重构；只把 token 方差拉齐，又可能加重通道分布的长尾。一个可检验的分支是先作通道 Hadamard，再在完整 token 块上交替平衡 token 与 channel 方差，量化时保存两轴缩放，读取时一并还原。[KVarN 的受限对照](https://arxiv.org/html/2606.03458v1)支持这种幅值误差调节，不是把权重量化的校准解释直接移植到动态 KV；有限迭代的平衡指标和局部 attention 重构也不能为整段自由生成签发无损证书。

这种表示还改变写入 frontier：新 KV 先留在高精度 tail，块满后才归一、量化和编码，读取同时消费已编码块、两轴 scale/zero-point 与仍未编码的近期状态；sink 或 recent 高精度区域不能从实际驻留账中消失。额外缩放的局部归一/解码开销很小，也不等完整 2-bit serving 已验收；部分推理、代码和指令任务仍低于 FP16，且 baseline 的精度与保留窗口并不完全相同。须联合验收块大小、变换位置、metadata dtype、实际字节和目标生成协议，连同重编码、在线变换与回归计费；边界或质量不合格时，保留较高位宽、较宽高精度窗口或 FullKV，不从名义 bit 数承诺净吞吐或任意长输出质量。

### 完整下锚

#### Inner-dimension Grouping 把量化误差与物理读取布局绑在一起

按 outer/token 维分组便于沿现有 cache row 管理 scale，却可能让一次 dot product 读取更多独立量化组和 scale；沿 inner/reduction 维分组可以让计算单元复用 scale、减少 memory access，但同时改变 K/V 的 layout、dequantization 顺序和 kernel interface。更完整的 artifact 还需要区分 K/V 的 hybrid symmetric/asymmetric mode、保留 recent 与 sink token 的高精度窗口，并在 Prefill 时确定 K 的 per-channel normalization。补偿还必须绑定 RoPE 执行顺序：post-RoPE 的 K 缩放需由同坐标 Q 反向缩放补偿；直接折入 pre-RoPE projection 只有缩放与相对旋转 commute（例如每旋转 pair 同 scale）时才保 score，一般 per-channel scale 不具该条件。原稿 §4.3/Alg2 的任意 fold 等价声明不作为数学保证，未核 artifact 也不能据此断言实际实现错误。

这条路线交换的是带宽、scale metadata 与误差分布，不是免费的 bit reduction。inner-dimension grouping 可能只适合一侧 cache 或特定 GEMV/attention kernel；高精度窗口减少 outlier leakage，也占用预算并依赖窗口策略。kernel 不支持、cache sharing/layout conversion 成本过高或任务对低比特误差敏感时，应保留 outer grouping、较高位宽或 FP16。evaluation 必须同时绑定最终质量、effective bits、page/layout、硬件与完整 attention latency。

<!-- SF-2026-ARXIV-2602-23200 -->

### 拟本人true-H2 Review notes注

- KVarN / `2606.03458v1` — Daily2026-06-04补Jun03；[exact-v1](https://arxiv.org/html/2606.03458v1) §2–3、4.1/T1–3/4.2、A/B/C文字、D/E/H/I/J必要，2+1+2=5，实际同family缺口深入。仅双轴方差调节与block frontier/metadata分支；保pseudo-decode代理、FP16质量反退、baseline精度/窗口不同、8bit/FP16zero-point文字不齐不采完整recipe、局部计时非全serving及全费用，不授唯一因果/无损/净吞吐。未核图像像素、全淘汰矩阵、代码或复现；R55准入/Jun03日证有效，待首次必要Source/正式分/actualowner/原两段PRE，无新授/未写，不预I/DAY。
