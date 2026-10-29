# Root 五项最小逐字拟稿

作者拟稿，必要Source/date/owner复用ROOT_REVIEW R7；以下均等待非作者逐字PRE，未写入Books。

## 04753 SAGA

Owner：MODEL-MULTI-HEAD-ATTENTION；Ch15，在GQA“不是发现所有KV heads都相似后的必然终点。”整段后、“一个GQA分组例子”标题前。已读完整MHA/MQA/GQA及参数/cache邻接与Ch14/16交接。现有Hkv将K/V头数绑定，差额是Hk/Hv解耦的模型约束及转换/近似费用。

逐字正文：

K 与 V 的头数还可以分开选择，而不沿用统一的 `H_kv`：当稀疏 Value 聚合已经较便宜，保留较多 Value heads、合并部分 Key heads，可以继续削减 QK 匹配的成本。这是改变模型表示瓶颈的架构分支，不是对任意 GQA checkpoint 的无损 kernel 改写；若两侧 head 宽均为 `d_h`，每层 KV elements 的一般式为 `B*T*(H_k+H_v)*d_h`，前述公式是 `H_k=H_v=H_kv` 的特例。[SAGA 的受限转换](https://arxiv.org/html/2610.04753v1)通过 logit matching 合并 K、同步重排 Q/V/O 并蒸馏，还为稀疏 PV 使用近似阈值；阈值跨步复用和固定候选 buffer 溢出丢项均改变近似语义，内存安全不等数值无损。短序列的阈值/收集开销及 multi-key retrieval 退步必须保留，长序列计时不能替另一长度的质量验收。转换、蒸馏、阈值与布局适配都付费；匹配质量、检索或实际净费用不合格时保留原 GQA/MHA，而不把更少 Key heads 当作普遍更优的终点。<!-- source-family:SF-2026-ARXIV-2610-04753 -->

逐字本人注：

- `SF-2026-ARXIV-2610-04753` — Daily2026-10-07，Oct6自然日；[exact-v1](https://arxiv.org/html/2610.04753v1)必要机制/转换/阈值及短序列、multi-key反侧，2+2+2=6。仅Hk/Hv解耦和近似/转换分责，非无损runtime替换；root R7必要Source/date/owner通过，本稿literal PRE及实际POST另记，未核代码或复现，不授DAY。

## 04204 Clean

Owner：TRAIN-PRETRAINING；Ch28，“Low-rank Pretraining”中“几何指标仍是代理…”整段后、压缩momentum残差段前。已读完整低秩参数/optimizer状态邻接；差额是两侧basis内外按不同粒度保存矩，而非再次声称低秩省内存。

逐字正文：

节省 optimizer state 还可以压缩统计的粒度，而不把整个更新限制在主子空间：用两侧低秩正交 basis 将梯度分成主块、两个单侧块与双侧余块，主块保留细粒度 moments，单侧块汇聚统计，余块保留标量统计后共同重构更新。双侧余块并未丢弃，因而这不同于只训练低秩参数；固定 rank 下状态随矩阵边长增长，也不等于全部训练内存线性增长。[Clean 的受限对照](https://arxiv.org/html/2610.04204v1)还暴露刷新成本：旧主块二阶矩不保留全部跨坐标协方差，basis 更新后的统计搬运只是近似，不能称完整 SOAP 的等价状态。Rank 太低或刷新过频均可退步，所测 C4 loss 也有略弱于 SOAP 的规模。Basis/分块统计、刷新、矩阵运算与学习率搜索全部计费；质量、数值或净墙钟不合适时保留更高 rank、部分状态压缩或原 full-rank optimizer，不用状态字节比例批准全训练加速。<!-- source-family:SF-2026-ARXIV-2610-04204 -->

逐字本人注：

- `SF-2026-ARXIV-2610-04204` — Daily2026-10-07，Oct6自然日；[exact-v1](https://arxiv.org/html/2610.04204v1)两侧basis/four-block moments/transport及rank、refresh反侧，2+2+2=6。余块scalar非丢弃，统计搬运近似，memory/steps非全墙钟；root R7必要Source/date/owner通过，本稿literal PRE与实际POST另记，未核代码/复现，不授DAY。

## 04490 BARQ

Owner：INFER-TENSORRT-LLM；Ch49，现有 additive-codebook E/M 两段后、稀疏高精度残差段前；已读完整assignment/centroid和恢复分工邻接。差额是均衡熵正则软拟合与最终hard编码不继承同一目标。

逐字正文：

码本拟合也可先用带均衡约束和熵正则的 soft assignment 更新 barycenters，再丢弃这份软矩阵，以最近 centroid 的 hard assignment 编码实际权重；均衡的是离线拟合人口，不保证推理 artifact 各码被均匀使用。[BARQ 的条件分析](https://arxiv.org/html/2610.04490v1)中，固定几何与正温度下精确软子问题的下降，不自动成为 hard distortion 下降；从软分配硬化所付的惩罚须被拟合收益覆盖，有限 Sinkhorn 迭代与 mass floor 也不能直接继承精确论证。有限校准、模型和任务中仍有 perplexity 或任务反退，与其他方法相同 index bits 不代表完整 bits-per-value 相同。Sinkhorn、centroid 更新、校准及全部码本/metadata 计费，原文未验证端到端加速；软硬目标失配或质量费用不合格时保留普通 nearest-centroid、原 residual codebook、更高位宽及独立执行验收，不把均衡训练当作无损编码。<!-- source-family:SF-2026-ARXIV-2610-04490 -->

逐字本人注：

- `SF-2026-ARXIV-2610-04490` — Daily2026-10-07，Oct6自然日；[exact-v1](https://arxiv.org/html/2610.04490v1)balanced soft fit/hard encoding及下降条件，2+1+2=5，具体差额深入。正温度精确软目标不授hard下降，有限Sinkhorn/massfloor、任务反退/完整存储费用近文；root R7必要Source/date/owner通过，literal PRE/实际POST另记，未核代码/复现，不授DAY。

## 04403 Saying, Not Knowing

Owner：INFER-TENSORRT-LLM；Ch49“量化验收不能只看平均分”中三层证据及release identity段后、更多诊断成本段前。已读完整该节，差额是按请求复现词面与独立定义词义的配对探测，不重复一般平均分原则。

逐字正文：

逐例质量还可把“能按要求输出某个词”与“能独立解释这个词的意义”配对检查。受限稀有英文词实验观察到词面仍可生成、定义却更易错误，说明输出包含目标字符串不等于该项语义读出保持；这也不证明所有正确用法已经丢失。[Saying, Not Knowing 的对照](https://arxiv.org/html/2610.04403v1)覆盖所测 429 词及模型/量化 recipes，部分 reference 本身是 Q6/Q8，并非统一 FP16；词干/同义词评分和 judge 也可能产生量化相关误差，有限人审不把它变成词义真值。不能由一个 PPL 阈值预测全部语义退化，也不能忽略家族、recipe 和非单调例外。应绑定词项、原定义、词面与词义判据、reference 精度及 evaluator，另付配对调用和人审核验；敏感词义回归时提高精度或保留原模型，不以字符串复现或平均分放行。<!-- source-family:SF-2026-ARXIV-2610-04403 -->

逐字本人注：

- `SF-2026-ARXIV-2610-04403` — Daily2026-10-07，Oct6自然日；[exact-v1](https://arxiv.org/html/2610.04403v1)词面/定义配对及judge、baseline精度/非单调反侧，2+1+2=5。限429英文稀有词、27artifact/13family受限评价，非全部语义删除或通用安全bits；root R7必要Source/date/owner通过，literal PRE/实际POST另记，未核代码/复现，不授DAY。

## 04664 FlashSwin

Owner：MULTIMODAL-REPRESENTATION；Ch23“阶段二：modality-specific encoder + projector”中“当目标以理解为主…”整段后、“新模态已有可用encoder…”前，不拆已有代码块。差额为视觉encoder位置接口与可融合算子的联合改变，非通用Attention kernel owner；Ch22/24交接已读、表示与生成不混。

逐字正文：

视觉 encoder 的空间位置接口也会限制可用的执行路径：窗口内 additive position bias 与 shift mask 便于保留既有模型语义；另一分支改用局部二维 RoPE、overlap stem 并保留 shift mask，让新的窗口算子使用标准 fused attention。[FlashSwin 的受限对照](https://arxiv.org/html/2610.04664v1)因此是表示/训练接口替代，不是原 Swin checkpoint 的无损加速；可融合的低 rank additive-bias 对照也说明不能把所有 additive bias 判为必然不兼容。相同窗口的 matched-compute 与更密 patches 的额外计算要分账，部分分类配置反退、COCO 大窗口有持平，QKV 数值精度也未统一。位置坐标、stem、窗口/mask、重新训练与融合实现须共同验收并计费；质量、兼容性或净成本不合格时保留原 relative bias、已验 additive-bias kernel 或原 encoder，不以局部 kernel 更快批准完整视觉系统加速。<!-- source-family:SF-2026-ARXIV-2610-04664 -->

逐字本人注：

- `SF-2026-ARXIV-2610-04664` — Daily2026-10-07，Oct6自然日；[exact-v1](https://arxiv.org/html/2610.04664v1)local2DRoPE/overlapstem/shiftmask与matched-compute/精度及任务反侧，2+2+2=6。新算子非原Swin无损kernel，保低rank additive分支和训练/patch费用；root R7必要Source/date/owner通过，literal PRE/实际POST另记，未核实现/复现，不授DAY。

## 05793 Topology Backdoor

Owner PLATFORM-SECURITY；Ch72 BackdoorEvaluation的原两段及marker之后、“线索本身也要重新取得…”前，已读其与前Multi-Agent防御完整局部。

逐字正文：

Trigger 还可绑定提示描述的协作拓扑和审阅条件，而不只是任务字符串：在任务字节相同的条件下交叉改变单体/多体及有无人工审阅，再加入拓扑术语 placebo，能检查可疑适配是否只在特定上下文改变行为。[受限后门对照](https://arxiv.org/html/2610.05793v1)支持这种描述条件触发，不证明真实多 Agent 环境会自然触发或所有协作都危险；独立 bandit analyzer 的检出率低于任务专用 checker，广窄信号对照还混入训练量差异。二元审计在 clean control 上也有高假阳性，不能把猜中一次触发叙事当可靠检测器。适配来源、触发邻域、配对任务、真实 effect 与独立审计须共同保存，全部训练/重放和标注计费；覆盖或误报未过时保留来源门禁、受限 capability、人工核验与 Unknown，不由未触发或一次审计批准安全发布。<!-- source-family:SF-2026-ARXIV-2610-05793 -->

逐字本人注：

- `SF-2026-ARXIV-2610-05793` — [exact-v1](https://arxiv.org/html/2610.05793v1)，Daily2026-10-07/Oct6窗，2+2+2=6；§3–6/compute与盲审，提示拓扑×人审/byte匹配/placebo、bandit泛化/高误报边界；root R10必要Source/date通过，literal PRE/实际POST另记，未核实现/复现，不授DAY。

## 04951 LLBPE

Owner MODEL-TOKENIZER；依root实际PRE调位到Ch11“从无状态预处理到会话级增量接口”末、合法切点CPU段后/多语言标题前；BPE规则与runtime/编码兼容在此衔接，不拆离线学习链。

逐字正文：

另一条 GPU 执行分支在固定 merge rules 后，用 array-linked-list 只更新一次合并附近的邻接关系，使单次 merge 修改为常数工作；这并不消除 pair rank 查询、最小候选选择或扫描。[LLBPE 的受限 GPU 分支](https://arxiv.org/html/2610.04951v1)还禁止跨 block 合并，因此字节可无损还原不等于与原 tokenizer 产生相同 token IDs；未验证下游 checkpoint 时不能当兼容替换。CPU pretokenization、IO 与传输仍在完整路径中，A100 上三本英文书的 merge 微基准不授端到端 tokenize 倍数。索引、分块、输入制备、全部选择与搬运都付费；边界改变或完整吞吐不合格时保留原 CPU BPE/既有实现，并先验 token-ID 及模型行为，不以局部更新复杂度批准语义等价。<!-- source-family:SF-2026-ARXIV-2610-04951 -->

逐字本人注：

- `SF-2026-ARXIV-2610-04951` — [exact-v1](https://arxiv.org/html/2610.04951v1)，Daily2026-10-07/Oct6窗，2+2+2=6；§IV–VI array-linked-list/merge与block边界必要层；lossless bytes非tokenID等价，merge微基准非全CPU/IO/transfer路径。root R10必要Source/date通过，literal PRE/实际POST另记，未核实现/复现，不授DAY。

## 04093 SNACK

Owner TRAIN-PRETRAINING；Ch28 dynamic-sparsity状态三段/marker后、硬件pattern段前，完整347–357邻接已读。差额是初始化至梯度一直稀疏物化，不重复已有active-only optimizer状态。

逐字正文：

稀疏状态还需落实到算子实际物化什么：若从初始化起只保存支持集中的权重/索引，forward 与 backward 直接在该 COO 支持上执行，就不必为缺边生成 dense 权重或完整梯度；缺边没有梯度，也不能把这份梯度当自动 regrow 的全梯度依据。[SNACK 的受限对照](https://arxiv.org/html/2610.04093v1)支持 small-batch、高稀疏条件的内存分支，不证明全模型更快；较大 batch 有另一稀疏库适用域，所测 output/gradient 误差约 1e-4 也非 bit-exact。GPT-2 仅部分 projections 稀疏，完整训练仍更慢/耗能，极稀疏全推理也未胜 dense；初始化器差异还限制逐seed对齐。索引、初始化、全部算子与质量回归均计费；内存并非瓶颈、支持需动态增长或净费用不合时保留 dense、成熟稀疏库及原 topology-state 协议，不以省物化批准端到端加速。<!-- source-family:SF-2026-ARXIV-2610-04093 -->

逐字本人注：

- `SF-2026-ARXIV-2610-04093` — [exact-v1](https://arxiv.org/html/2610.04093v1)，Daily2026-10-07/Oct6，2+2+2=6；§3–6初始化/COO/支持梯度与端到端反退，非bitexact/全梯度，省memory非全速率。root R10必要Source/date通过，literal PRE/实际POST另记，未核代码/复现，不授DAY。

## 06026 DBW

Owner INFER-TENSORRT-LLM；Ch49 PTQ/QAT节05329新段后、QAT输入teacher段前。已读该完整局部，差额为SVD component级含0bit的预算与实际多GEMM分工。

逐字正文：

低位权重也可把预算分给 SVD components，而不只给原 channel 或 layer：在固定 block 总预算下学习因子及可微 bit proposal，取整后分配剩余位，0bit 同时删除对应分量。离散 rounding/STE 因而属于校准路径，不是推理时免费寻找最佳 rank。[DBW 的受限对照](https://arxiv.org/html/2610.06026v1)在相同协议下优于所比启发式，但极低 bit 仍远弱完整精度；按 bit 分组执行多个 GEMM 和部分和累加，会让短序列 launch 成本与长序列收益相反。SVD、因子学习、预算校准、packing 与全部 GEMM 都计费，不能由名义 1.61bpw 或局部矩阵速度批准无损模型和全请求加速。分量支持、量化质量或目标长度净费用不合时保留较高位宽、普通 PTQ/低秩分解及原 checkpoint。<!-- source-family:SF-2026-ARXIV-2610-06026 -->

逐字本人注：

- `SF-2026-ARXIV-2610-06026` — [exact-v1](https://arxiv.org/html/2610.06026v1)，Daily2026-10-07/Oct6，2+1+2=5；§2–3/主对照/推理反侧，SVD component0bit/固定预算/rounding-STE与多GEMM长度开销。root R10必要Source/date通过，literal PRE/实际POST另记，未核实现/复现，不授DAY。
