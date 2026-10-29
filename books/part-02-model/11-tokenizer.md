# 第11章 Tokenizer

**Knowledge Tree:** Part II 模型：一个 Token 如何变成答案
**Stable Knowledge Node ID:** `MODEL-TOKENIZER`
**Legacy Chapter:** Ch11
**Status:** Draft

**Roadmap Intent:** 文本如何被切成 token，为什么 tokenizer 会影响知识表示、上下文长度和多语言能力。

## 本章要回答的问题

神经网络只能处理有限维张量，真实文本却由开放词汇、Unicode 字符、代码、数字和不断出现的新名字组成。怎样把任意文本稳定地转换为有限词表中的整数序列，又不让词表或序列长度失控？

本章的核心判断是：**Tokenizer 是文本世界与模型计算之间的离散接口。**它不只是预处理工具，而是在 vocabulary size、sequence length、可逆性、多语言覆盖和系统成本之间选择计算粒度。

Tokenizer 的输出止于文本 token ids。id 如何进入连续空间属于第12章；第23章把离散协议扩展到 image/video/audio codec，并增加 modality、timestamp、coordinate 与 codebook identity；训练语料如何清洗、去重和治理属于第27章。文本 tokenizer 与多模态 codec 复用“离散协议”原则，但不共享相同信息损失、序列尺度或 decoder contract。

本章使用 `B` 表示 batch size，`T` 表示 token sequence length，`V` 表示 vocabulary size，`d_model` 表示模型 hidden dimension。

## Part II 的阅读主线

Part I 已经从世界观层面解释模型能力、系统交付与长期约束。从本章开始，我们把模型从黑盒展开，沿一个 token 的生命周期追踪接口与状态：

```text
第11～20章：生成主干

Text
-> Tokenizer ids
-> Embedding + Position
-> Self Attention + MLP
-> Transformer Layer
-> Decoder-only logits
-> KV state + Sampling
-> next token

第21～22章：容量扩展

Dense MLP -> MoE                 参数容量轴
Position + Attention + KV Cache -> Long Context  序列容量轴
```

因此目录顺序不完全等同于一次 forward 的算子顺序。第 11～20 章闭合生成主干；第 21 章回到第 16 章扩展 MLP，第 22 章再汇总位置、Attention 与 KV Cache 的长序列约束。先区分主干与分支，后续才不会把模型结构、生成策略和系统优化混成一条流水线。

## 为什么不能直接按词切分

最符合人类直觉的方案是把每个词作为一个 token。对句子：

```text
AI systems learn patterns
```

可以得到四个词。但真实词汇不是封闭集合。人名、拼写变化、复合词、URL、代码标识符和新术语会不断出现。若为每个词分配独立 id，词表会持续膨胀；若只保留高频词，未登录词只能统一变成 `<unk>`，不同信息被不可逆地压成同一个符号。

另一个极端是按字符切分。字符词表较小，也几乎没有 OOV，但同一段文本会产生更长序列。Transformer 的 Attention 和 KV Cache 成本依赖 token 数，字符级表示会把简单词语拆成很多计算步。

因此需要中间粒度：高频模式保留为较长 token，低频词退化成较短 subword、字符或 byte。目标不是找出语言学上唯一正确的词，而是构造可计算、可覆盖的离散词表。

## BPE：从最小单元逐步合并

Byte Pair Encoding 原本是一种压缩思想，subword BPE 将其用于开放词汇建模。简化训练过程如下：

1. 把训练文本表示为初始符号序列。
2. 统计相邻符号 pair 的频率。
3. 合并最高频 pair，生成新符号。
4. 重复直到达到目标 vocabulary size 或 merge 次数。

下面用一个小例子演示。假设语料为：

```text
low low lower
```

以字符为初始单元，并用 `</w>` 标记词尾：

```text
l o w </w>
l o w </w>
l o w e r </w>
```

高频 pair `l o` 可以先合并为 `lo`，随后 `lo w` 可合并为 `low`。最终可能得到：

```text
low </w>
low </w>
low e r </w>
```

`low` 因为高频获得完整 token，`lower` 仍可由 `low + e + r` 表示。BPE 学到的是语料中的频率结构，不保证 merge 边界与人类词法完全一致。

频率统计在质量相近、接口稳定的语料上便宜且合理；同频片段若有不同的可靠性，离线构词还可以加入外部 quality proxy，而不把频率直接当语义重要性。一条受限分支把 pair 的频率关联、聚合质量与 domain factor 共同交给 merge selector：先固定质量参数训练 merge policy，再用下游目标和 Gumbel-Softmax relaxation 调整质量敏感度与权重，最后以固定参数构造 greedy vocabulary。这里学习的是离线 merge 选择，不是每个请求都调用 PPO；质量代理与聚合规则也不是数据真值，不能自动识别所有噪声。<!-- source-family:SF-2026-ARXIV-2602-06394 -->

额外候选搜索、质量统计、两阶段优化和词表改变后的模型训练都要计价。所称近似最优界另需 monotonicity/submodularity 等条件，原文也明确一般 LM loss 不满足该结构，因而不能把条件 quality-frequency 界写成整个模型目标的最优保证；固定词表的部署路径没有新增 policy 调用，也不表示生命周期成本为零。应分开比较 raw exposure、优化步数、词表构建与下游回归，避免让低质量代理把罕见但真实的片段排除。质量信号不可校准、统计分布变动或净收益不足时，普通 BPE/Unigram 与独立数据清洗仍是清晰基线，而不是必须随之改变 tokenizer artifact。

频率高也可能只是同一仓库反复出现的长名字，并不意味着这个新 token 在其他来源中还能获得足够训练。离线构词可以为每个候选 pair 额外记录它出现于多少个仓库、多少种编程语言：合并后的支持集合是两个父单位支持集合的子集，因此支持计数沿 merge 分支不会增加。一个条件分支据此跳过支持不足的合并，或把频率与来源支持共同用于 merge 优先级；改变的是离线 vocabulary 搜索，而非每个请求的编码过程。导出的固定 merge rules 仍走原 BPE 推理接口，但词表与整数 ID 已改变，必须与新 checkpoint 一起验收。<!-- source-family:SF-2026-ARXIV-2604-14053 -->

来源支持不是质量或语义价值的真值：把阈值推得过高会剪掉真实的专用单位，甚至耗尽可合并分支、无法填满目标词表，也会增加构词时的跳过与统计成本。受限代码实验中更高的未见仓库覆盖、较少的低概率重复失败 token，只说明这套正则在所测统计与小模型上有效；相同训练 token 预算不是相同原文曝光，重复 token 的概率探针也不证明下游代码、安全或幻觉收益。应分别验收来源切片、最终 emission 分布、压缩率、模型行为与生命周期成本；支持统计不可得、专用语义回退失败或收益不能摊销时，普通频率 BPE 与数据治理仍合理，不能为了覆盖数字改变已部署的 token 身份。

目标merge数也可改为统计选择，而不是事先固定：沿已有BPE顺序，比较接受当前merge前后的unigram拟合与复杂度代价，只在局部准则下降时保留。拒绝父单位会同时使依赖它的后续merge不可形成，因此[这类选择](https://arxiv.org/html/2610.26225v1#S3.SS3)是顺序相关的greedy过滤，不是全局最优词表；后接低效单位refinement、用生成续文补稀疏pair统计，也不使估计分布或语义价值成为真值。较小merge集合可能降低词表压力，却增长序列并明显损害部分阅读任务；低资源切片接近原表现不能推广到高资源或其他workload。应同时验固定token-ID/checkpoint映射、原文覆盖、语言×任务质量与真实训练/服务成本，生成数据、统计、refinement和全部回归均付费；准则欠拟合、罕见单位丢失或净收益不足时，保留原固定预算BPE/Unigram与原artifact，不从较少merge或较高压缩率批准无损热替换。<!-- source-family:SF-2026-ARXIV-2610-26225 -->

编码新文本时，必须使用固定 vocabulary 和 merge rules，不能根据单个请求重新训练。否则同一模型权重会面对不稳定 id 语义。

固定词表与 merge identity，并不要求训练中每次都走同一条切分路径：BPE dropout 可以在既有 merge graph 内随机跳过合并，让同一原文出现多个合法 subword 序列，而不重建词表或重分配整数 ID。应把这种随机性作为训练阶段的输入分布选择，分别验预训练与下游微调是否采用它；[受限低资源对照](https://arxiv.org/html/2605.13436v1)中，两阶段都用的组合通常更强，仅微调时加入反而可能弱于确定切分。部署仍可保确定编码，不能把训练时的多种分段当热换 tokenizer 的授权。固定 token 预算与长度截断下，切分改变也改变原文曝光；较高形态边界 F1、外部形态词表替换与下游质量是不同证据，不能唯一归因“更符合 morphology”。随机编码、预训练、微调重复与回归均付费，部分语言/任务仍反退；阶段、原文覆盖或消费者质量失配时，保留确定 BPE、较弱训练随机性及原 checkpoint，不由某个 dropout 比率批准通用大模型 recipe。<!-- source-family:SF-2026-ARXIV-2605-13436 -->

固定 artifact 仍可有“允许编码”与“允许输出”两份不同集合。一条受限分支保留 BPE merge graph，把输入中不再允许的残留 token 递归拆开，再按未屏蔽的 merge 规则重组；输出侧则屏蔽对应 logits 列，而不重新 merge 已生成的自回归前缀，否则 token 位置与 KV 语义会一起改变。输入重组与输出禁用因而必须分别绑定 vocabulary/mask、merge graph、ID 映射及 checkpoint，不能把它当免费换 tokenizer。[必要方法与反侧](https://arxiv.org/html/2602.04706v1)用语料中的最终 emission 次数与邻接 entropy 筛选候选，二者是 corpus-conditioned proxy，不是语义冗余真值；受限 Latin/C4 证据不能替未改动的非 Latin 路径验收。减少输出候选会改变生成分布，输入拆分也可能增长序列；参数减少、PPL 的 token 单位、生成质量与实际 backend 成本应分账，不能由词表变小或置信分数更高推准确率。mask 配置、长输入质量或实际执行不合要求时，回退原 artifact，保留基本单元与兼容路径，而不追求普遍 plug-and-play 或无损收益。<!-- source-family:SF-2026-ARXIV-2602-04706 -->

## Unigram 与 SentencePiece 的另一条路线

BPE 从小单元开始不断合并；Unigram Language Model 常从较大的候选 subword 集合开始，估计各 token 的概率，再逐步删除贡献较低的候选。对同一字符串，它可能存在多种切分，算法根据整体概率选择路径。

编码器选出一条路径，也不让语言模型在该路径上的likelihood自动等于可见字符串的全部概率。应先固定checkpoint、前缀、词表/解码映射与输出边界、允许长度，再区分单一canonical编码的质量和同一字符串事件下不同合法token路径的聚合；不能把Unigram分词器的路径分数当成语言模型的概率。一条[受限的decoding-free分支](https://arxiv.org/html/2510.20208v1#S4)在有限长度lattice中，围绕canonical路径枚举并批量评分不同token序列：只累加不重复路径时得到所覆盖质量的下界，增加尝试数只有在累计集合包含旧集合时才保证不减，不是无放回采样自动产生无偏marginal估计。长度截断、候选耗尽和重复处理仍会漏质量；完整字符串事件、边界或路径资格未闭时，只报告已评分集合，不补成归一或完整求和保证。构建lattice、全部路径forward和后续候选生成/重排均计费，有限QA中canonical仍常更好，快于另一估计器不等快于普通编码或真实生成。跨切分比较确有需求时才使用这种显式有限聚合；净质量、事件定义或预算不合时，保留固定canonical编码及其明确的tokenlikelihood，不把更大的下界签成更好答案、语义真值或Serving加速。

<!-- source-family:SF-2025-ARXIV-2510-20208 -->

SentencePiece 的系统意义不只是实现某种算法。它可以直接从 raw sentences 训练，不要求先依赖特定语言的空格分词，从而使相同 pipeline 更容易覆盖中文、日文及混合语言。

两条路线的稳定差异是：

```text
BPE      frequent pair merging determines vocabulary
Unigram  probabilistic candidates compete as segmentations
```

具体模型采用哪种实现，需要根据其 tokenizer artifact 核验，不能从模型名称推断。

上述比较其实同时混合了两个变量：优化目标是 compression 还是 segmentation likelihood，搜索方向是 bottom-up merging 还是 top-down pruning。把两轴补成 `2×2` 对照后，受限实验显示 bottom-up search 对 bits-per-byte 的影响可能大于目标本身，而同一 intrinsic 优势不会稳定转化为 BLiMP 类语法收益。长期结论不是“换一种 tokenizer 即可提升模型”，而是 tokenizer 评测必须把 objective、search、vocabulary size、training corpus 与下游 contract 分开；当前证据最多覆盖 1B 模型和五种语言，低资源语言、长上下文与更大模型仍需独立验证。成熟 BPE/Unigram 在 checkpoint 兼容、工具链与下游回归更重要时继续成立。

<!-- source-family:arxiv:2609.19145v1 -->

## Byte fallback 为什么重要

即使 subword 词表覆盖很广，Unicode 仍然是开放组合空间。Byte-level tokenization 或 byte fallback 为任意输入提供最终退路：无法由已有文本 token 表示时，转成底层 bytes。

这样可以避免 `<unk>` 丢失信息，但会产生代价。稀有字符可能展开成多个 byte tokens，序列更长；人类看到的一个字符也不一定对应一个 token。Emoji、组合音标和非拉丁文字尤其容易暴露这个差异。

因此要区分三层：

```text
Unicode text -> encoded bytes -> tokenizer symbols -> token ids
```

字符数、byte 数和 token 数不是同一单位。API 计费、context limit 和 KV Cache 容量通常按 token，而不是用户界面里的字符数。

Tokenizer覆盖还不能只按低fertility或零UNK验收：整词压成UNK会制造很短却不可逆的序列，byte fallback又可在没有UNK时大幅增加长度。[受限script审计](https://arxiv.org/html/2610.24818v1#S5)因此联合报告实际UNK/byte发射比例、tokens/word与覆盖/回读，而不是用一个压缩指标排名；Unicode script也不等语言人口。相同token上限下的可见原文会改变，但由fertility推算的context/KV负担不是已测服务时延或下游精度。文本/normalization、编码、回读与真实任务回归均付费；覆盖或信息保留不足时保byte/subword、原checkpoint与已验语言路径，必要扩词表须连embedding/训练一起重验，不由换tokenizer或更短序列签发免费修复。
<!-- source-family:SF-2026-ARXIV-2610-24818 -->

编码可逆也不等于有限 lookahead 下的边界可辨识。若相同左上下文和当前可见的编码前缀，对应两种需要相反切分的后续内容，确定性边界策略就无法同时正确；合法的 scalar/grapheme 边界目标，也不保证模型已看见足够信息或学会遵守它。[有限编码对照](https://arxiv.org/html/2610.22071v1)用部分 BMP 字符的 UTF-16 低位优先接口改变首符号的可见信息，却仍有跨编码页碰撞；增加 UTF-8 lookahead 也是有效对照，不能据此宣布某种编码普遍更优。比较应固定原文与边界目标，另核删除不合法切点造成的 patch 预算变化；编码、符号表、teacher 与局部 decoder 的重对齐和训练均付费。完整新模型与端到端收益未验时，保留稳定 UTF-8、更多 lookahead 和独立编码合法性检查，不把接口变换当 checkpoint 热替换。<!-- source-family:SF-2026-ARXIV-2610-22071 -->

训练表示与部署输出还可以走另一条分支：同一模型在带 sentinel、互不重叠的符号空间中交替学习压缩代理序列与原始 UTF-8 bytes，先用配对样本建立两种表示的关系，再继续混合 next-symbol 训练；部署只保留 byte 路径，压缩代理不必成为线上 tokenizer。于是训练 symbol 数不能直接当作原始语料曝光量，codec、符号映射、sentinel、混合策略与 checkpoint 共同定义这份训练接口；给定 gold compressed 输入的恢复结果，也不等于正常 byte generation 能力。代理格式制作与配对训练需要准备成本，byte 输出仍可能带来更长 Decode；受限对照中小模型或其他压缩格式有反收益，神经代理恢复也不是无损编码保证。采用前应分别验收 raw exposure、生成质量、编码有效性与端到端成本；代理不合适或 byte 生成代价过高时，纯 byte 训练与 subword 路径仍然合理。<!-- source-family:SF-2026-ARXIV-2602-04289 -->

### Byte 覆盖输入，不自动保证输出合法

Byte-level 模型能为任意输入建立表示，却不意味着任意生成的 byte 序列都能还原为合法 UTF-8。Perplexity 衡量模型给目标序列分配概率的能力；decoder validity 则是一份独立的结构合同。面对稀有或训练中未见的字符，若只逐 byte 采样，局部高概率选择仍可能组合成非法 continuation。

因此 tokenizer/runtime 应持有增量 decoder state，在采样时只放行当前 UTF-8 前缀仍可完成的 byte；模型 logits 只提出候选，不拥有编码协议的合法性。这个 gate 能避免把不可解码输出交给下游，但会限制采样、增加状态和实现复杂度；纯 ASCII workload、只生成已封闭 token，或上层协议已经执行等价强校验时，原来的无状态路径仍更简单。现有证据来自受限规模、多语言语料和结构有效性测试，不能把观测到的失效率外推到所有 tokenizer。

<!-- semantic-body-binding:SF-2026-ARXIV-2606.14122 -->

## Normalization 与可逆性

编码前可能执行 Unicode normalization、大小写转换、空白处理或前缀空格规则。Normalization 可以减少表面变体，却也可能丢失原始差异。

一个 tokenizer 是否满足：

```text
decode(encode(text)) == text
```

取决于 normalization、未知符号和 decoder 规则。许多 byte-level 设计可以对广泛输入做到近似或严格可逆，但不能把可逆性当作所有 tokenizer 的天然性质。

多文字系统共享词表也可先改变文本表示：保留 native script，或先 romanize 再训练相同规模 encoder。转写可能扩大共享 subword support、减少词表压力，却会抹掉同音字符或书写差异；全转 ASCII 与保留 diacritic 的窄转写不是同一 fidelity 接口。不能从更短编码或共享率提高推出所有任务更好；任务所需差异能否恢复，要与 fertility、词表容量及 mono/multilingual 数据控制一起验收。<!-- source-family:SF-2026-ARXIV-2601-05776 -->

[同文档、固定计算的受限比较](https://arxiv.org/html/2601.05776v1)从头训练149M ModernBERT，分开 native/romanized 和 mono/multilingual，在六种文字语言、五任务与五次种子中观察到收益依任务变化。Chinese/Japanese 的 NER 等 script-sensitive 任务退步，保真转写可部分缓解却不消除所有损失；这不是 decoder-only LLM、原词表热替换或无损编码证据。转写、重训与语言×任务回归付费；碰撞不能消歧、fidelity或质量不足时，保留 native script、语言专用路径和 byte/subword fallback，不只为共享率改变 checkpoint 输入协议。

共享词表还可以共享索引而不强迫各语言使用同一套切分：先各自训练分词器，把可信翻译对应项放在相同ID，再以language identity选择分词器，并为全部位置加入语言embedding。[Parallel Tokenizers的受限分支](https://arxiv.org/html/2510.06128v1#S3)把跨语言对应和本地切分分开；只有部分词项对齐，其余同ID仍依赖语言条件消歧，不能把索引相同当上下文词义必然相同，也不能说不同ID必然阻止共享表示。翻译错误、多义碰撞和去重后的ID对应须与词表、语言选择器及checkpoint共同验收，不能热换词表。Fertility或bitext读数改善不保证所有任务收益，原不同学习率与CPT反退也限制唯一归因。全部翻译/回译、词表校验、语言判定/驻留、预训或embedding迁移及逐语言任务回归均付费；对应、语境或净质量不合时，保原共享/语言专用词表与byte/subword fallback，不为更高共享率批准完整语义对齐或无损迁移。

<!-- source-family:SF-2025-ARXIV-2510-06128 -->

词表大小、context positions 与保留的信息也不是同一预算。对音节结构较强的语言，一个替代 codec 把 onset、rime 与 tone 放在同一 position，以三个成分 embedding 的拼接投影形成输入，并用独立 heads 预测完整 tuple；它不是把一个音节扩为三个串行 tokens。训练时同时 mask 完整 tuple，可避免已见成分直接泄露待预测成分，缩小各 head 的词表也不代表缩短了同样比例的语义路径。

文本转音韵 tuple 会遇到多音字、默认读音与同音碰撞，decoder 无法仅从碰撞后的 tuple 恢复被丢掉的字符差异；非支持符号的多位置 fallback 或 UNK 又改变长度与覆盖。中文受控比较检验的是包含转写、输入融合与目标 heads 的完整 pipeline，异质越南语数据不能当纯 tokenizer 因果对照；部分理解与阅读任务还会退步，未测 decoder-only 部署也不能继承结果。选择这一 codec 要联合验收可逆范围、词表/位置成本和目标任务，精度、硬件或运行预算未披露时不补造；遇到不可消歧文本或 unsupported 输入，保留 byte/subword 和可检查的转写回退。 [必要机制与反证](https://arxiv.org/html/2609.21362v1)。<!-- source-family:SF-2026-ARXIV-2609-21362 -->

生产系统必须把 tokenizer 版本与 checkpoint 一起管理。只替换 tokenizer 而保留模型权重，会改变 token id 与 embedding row 的对应关系，即使词表大小相同也可能完全破坏语义。

## Special tokens 是协议，不是普通文本

模型通常需要 BOS、EOS、PAD、UNK 或对话角色等 special tokens。它们属于模型输入协议，用来表达序列开始、结束、padding、角色边界或控制状态。

Special token 的风险在于，它可能在文本层看起来像普通字符串，却在 tokenizer 层被映射成保留 id。系统需要明确：

- 用户能否直接注入 special token。
- chat template 在哪里添加角色和边界。
- padding 是否参与 loss 和 Attention。
- EOS 是否既是训练标签，也是生成终止条件。

这些规则如果在训练、评估和 Serving 之间不一致，会形成隐蔽的 training-serving skew。

### Trusted Control ID 不应属于 Content Tokenizer 的输出空间

仅保留 special-token ID 或清洗对应字符串，仍允许普通内容编码出与控制协议相同的 token sequence。更严格的边界让 content tokenizer 的 codomain 排除 trusted control IDs；chat template/协议层只能在内容编码完成后，通过受信路径注入没有普通 surface form 的 control identifier。`allowed_special`、不可打印字符和字符串转义只能作为兼容层，不能单独证明 role isolation。<!-- source-family:SF-2026-ARXIV-2609-16984 -->

迁移会改变 tokenizer、model 与 template identity，并可能破坏旧 artifact。旧模型不能重训时，应保留严格模板解析、输入转义、role channel 隔离和 adversarial regression；五个 model family 的 probe 不证明任意 tokenizer 或 downstream safety。

## 一个完整的 shape 接口

假设 batch 中有 `B=2` 个句子，padding 后每个句子 `T=4` 个 token：

```text
text batch
-> tokenizer
-> input_ids shape [B, T] = [2, 4]
-> attention_mask shape [B, T] = [2, 4]
```

`input_ids` 中每个值都应满足 `0 <= id < V`。这些整数没有数值距离语义。第12章会用它们索引 embedding matrix，得到 `[B, T, d_model]` 的连续张量。

## Vocabulary 与序列长度的系统权衡

一段文本编码后长度为 `T`。Tokenizer 设计会同时影响后续两类成本。

更大的 `V` 往往能用更少 token 表示高频文本，但会扩大 embedding table 和输出 projection：

```text
embedding parameters = V * d_model
logits shape         = [B, T, V]
```

更小的 `V` 减少词表参数，却可能增大 `T`。标准 dense Attention 的成对关系随 `T^2` 增长，KV Cache 则近似随 `T` 增长。于是 tokenizer 会沿整条系统链传播影响：

```text
Tokenizer
-> sequence length
-> Attention compute
-> KV Cache capacity
-> latency / throughput / cost
```

### Vocabulary 选择要优化整个 Train / Deploy Lifecycle

更大词表可以缩短序列，却扩大 embedding 与 output head；训练阶段和部署阶段对这两类成本的权重不同，batch、硬件、语言和调用量还会移动最优点。tokenizer 因此不是只按训练 perplexity 选定的一次性前处理，而应以训练成本加生命周期推理成本的 workload function 比较。服务规模较小时，简单稳定的旧词表仍可能更优。
<!-- source-family: arxiv:2608.11361v1; semantic-body-binding: tokenizer-lifecycle-cost-function -->

不存在脱离语料和 workload 的“最佳词表大小”。代码、中文、英文、数字和多语言混合流量可能产生完全不同的 token efficiency。

这个选择还会改变输出端的监督单位，而不只是输入端的压缩率。同一段目标文本若被编码成一个整体 token，模型在该位置要完成一次整体分类；若拆成多个 token，目标就分解成依赖先前输出的多次分类。原始样本相同，并不意味着优化器面对相同的预测问题：监督粒度、条件化路径和每个样本包含的 loss 项都会改变。比较 tokenizer 时因此需要同时控制输入与输出的分词方式、loss mask 和训练预算，不能把行为变化全部归因于序列长度或表示容量。

更细的输出粒度可能提供有用的任务分解，也会增加解码步数和状态成本；整体 token 减少步数，却可能要求一次分类承担更多组合关系。这里没有通用的字符级优胜结论。受控小型加法实验只能说明输出监督侧值得独立测量；相同训练步数不等于相同 FLOPs，探针未读出某种中间量也不证明模型没有它。后续位置的 loss 仍可通过共享参数和 Attention 反传，不能把目标被拆分误解成各部分梯度完全隔离。<!-- source-family:SF-2026-ARXIV-2609-01386 -->

### 当 token 进入 Scaling Contract，比较单位必须回到信息量

词表大小、token 数和训练 FLOPs 经常被放在同一张 scaling 表里比较，但 token 不是跨 tokenizer 稳定的计量单位。同一段信息可以被切成不同数量的 token；若直接用 token 计预算，压缩率更高的 tokenizer 会同时改变序列长度、attention 计算、训练样本计数与推理延迟，使“更多训练数据”与“更高编码效率”混在一起。更稳健的做法是把 byte 或另一个可复算的信息单位作为跨模型的 canonical denominator，再把 tokenizer 映射产生的 token 数作为 execution shape。

这并不意味着 byte-level model 总是更优。较大的语义单元仍可能改善局部建模效率；代价是词表参数、稀有单元、跨语言公平性和 fallback 行为都发生变化。系统验收因此要同时报告 bytes、tokens、平均及尾部压缩率，并把这些量交给训练与推理预算模型。旧的 token 计数在同一 tokenizer、同一 normalization 与同一版本内仍然成立；一旦跨 tokenizer 比较，就必须退回稳定的信息单位。

稳定分母之外，还应把 representation 与训练 objective 联合比较：同样的 bytes 换成细粒度单元，AR 与随机 mask 的学习条件并不相同；相同估算 compute 会改变容量和 raw exposure，相同容量/数据又未必同 compute。[受限 byte/BPE 对照](https://arxiv.org/html/2605.12928v1)在这些不同 matching 合同下显示交互，不能把近似长度配平当成逐 batch 同信息，或把超过实测预算很远的拟合交点当成已见平价。AR entropy 对 BPE boundary 的 probe 关联不是唯一因果，朴素按 BPE span 联合 mask 的 byte 变体还退步，诊断因此不自动交付修复 recipe；部分任务的 byte 反胜也否定普遍不可行。ELBO、顺序评分与并行 sampler 的质量须分开，tokenizer、搜索、训练和完整采样均计费，估算 FLOPs 不替真实墙钟。Objective、人口或预算不匹配时，保留原 BPE、原 byte 接口及分项结果，不由较短序列、单一 loss 或外推曲线签发通用编码优胜。<!-- source-family:SF-2026-ARXIV-2605-12928 -->

跨 tokenizer 蒸馏还需要额外的概率接口。Teacher 的一个 token 往往对应 student 的多个 bytes，或者只在某个 byte 边界完成；若直接复制 logits，就把不同事件空间误当成同一标签。系统必须声明 probability mass 如何投影、何时提交一个 teacher token、未闭合 byte prefix 怎样处理，并把映射版本与 teacher/student tokenizer 一起保存。Byte 可以提供稳定的计量分母，却不让 token-level supervision 自动可复用；映射不可靠时，仍应回退 sequence-level distillation 或独立训练。

<!-- source-family:SF-2026-ARXIV-2609-12303 -->

## 从无状态预处理到会话级增量接口

词表固定后，还可以只改变编码过程的执行方式。这里先不改变 token 边界的语义，而是要求增量编码与同一完整编码函数逐 id 等价。

一次性请求中，每次对完整文本重新执行 tokenizer 是合理设计：实现简单、结果容易与模型
artifact 对齐，而且 tokenization 通常不是主导成本。Agent 与长对话改变了这个约束。一次
trajectory 会反复提交“几乎相同的长前缀 + 很短的新后缀”；即使后端能够复用 prefix KV，
前端若仍扫描完整文本，累计 tokenization work 仍可能随会话长度快速增长。优化下游缓存以后，
瓶颈会向上游接口迁移。

不能把旧 token ids 与新后缀的 token ids 直接拼接，因为一般并不满足：

```text
tokenize(prefix) ++ tokenize(delta) == tokenize(prefix ++ delta)
```

Normalization、pre-tokenization 和 subword merge 都可能跨越拼接边界。安全的增量实现因此
不是“缓存一次函数结果”，而是维持一份可验证的会话状态：已有 token ids、它们覆盖的 byte
范围、tokenizer 内容摘要与版本，以及用于判断旧后缀何时重新稳定的边界信息。新文本到来时，
实现只重算受影响的 suffix；只有找到该 tokenizer family 可证明的稳定边界，才复用更早的
结果。找不到边界、版本变化或输入不满足适用条件时，必须扩大重算范围，最终回退到完整的
reference tokenizer。

这把 tokenizer contract 从“对同一文本通常给出相同结果”提升为更强的等价性要求：

```text
incremental_result == frozen_reference_tokenizer(full_text)
```

工程上还需要 sampled shadow verification、mismatch quarantine、显式 fallback reason，以及把
tokenizer state 与 KV state 分开管理。前者体积通常更小，可以在 KV eviction 后继续存在；但
它会新增 session affinity、replication、version invalidation、admission 和 recovery 问题。
当增量很大、tokenizer family 无法提供稳定边界，或 KV prefix 本身已经失效时，无状态完整
编码仍然是更简单、也可能更快的方案。因此增量 tokenization 与 prefix KV reuse 是
`Layering / Dependency`，不是新实现对旧实现的单向替代。

仍需完整编码的新请求不能靠会话缓存加速，但并行切块也必须保持同一离散接口。切点不仅要落在BPE不跨越的pre-tokenizer边界，还要确保它在子块末尾仍成立；不能切开任何special-token字符串，normalization也必须可在此独立执行且不改变归一化后的边界。只有冻结配置满足这些条件时，分块各自编码后的IDs才能按原顺序拼接，BOS等序列级处理只做一次。仅有重叠区域token相同或足够长，不替代这些条件；找不到合格切点就减少并行或完整reference回退。

合法切点还改变CPU服务的不可抢占粒度：长stateless请求拆成chunk，短增量可在chunk结束时进入，而不是等整条长输入完成；session初始化仍可能在home worker整条执行。更小chunk减少阻塞，却增加dispatch、额外worker内存和局部状态管理，池没有专用核时也未必获益。[受限SGLang实验](https://arxiv.org/html/2610.19801v1)区分超长输入被tokenize后拒绝与真正进入GPU的流量；全部长文都需新Prefill时收益会被GPU成本掩盖，不把tokenization提速等同所有TTFT/SLO提升。<!-- source-family:SF-2026-ARXIV-2610-19801 -->

另一条 GPU 执行分支在固定 merge rules 后，用 array-linked-list 只更新一次合并附近的邻接关系，使单次 merge 修改为常数工作；这并不消除 pair rank 查询、最小候选选择或扫描。[LLBPE 的受限 GPU 分支](https://arxiv.org/html/2610.04951v1)还禁止跨 block 合并，因此字节可无损还原不等于与原 tokenizer 产生相同 token IDs；未验证下游 checkpoint 时不能当兼容替换。CPU pretokenization、IO 与传输仍在完整路径中，A100 上三本英文书的 merge 微基准不授端到端 tokenize 倍数。索引、分块、输入制备、全部选择与搬运都付费；边界改变或完整吞吐不合格时保留原 CPU BPE/既有实现，并先验 token-ID 及模型行为，不以局部更新复杂度批准语义等价。<!-- source-family:SF-2026-ARXIV-2610-04951 -->

## 多语言中的隐藏不公平

如果 tokenizer 的训练语料主要来自某种语言，该语言的高频片段更容易获得较长 token；覆盖较少的语言可能被拆得更碎。对于相同语义，不同语言的 `T` 可能不同，从而影响：

- 可放入 context window 的内容量。
- 推理延迟和 token 计费。
- 梯度中各语言的有效位置数量。
- 稀有文字退化到 byte 时的表示难度。

Tokenizer 不能单独决定多语言能力，数据分布、模型容量和训练目标同样重要。但它决定了模型最初看到的离散粒度，因此必须把 token fertility 和语言切片纳入 Evaluation。

### Fertility 是 Language × Domain 的成本与可达性合同

<!-- semantic-body-binding:SF-2026-ARXIV-2605-24718:start -->
全局平均 tokens-per-character 适合快速比较 tokenizer，也保留了单一 vocabulary 的部署简单性；但多语言系统里，同一
平均值会掩盖某些 language × domain 组合产生更长序列、更多注意力计算和更少有效 context。因而 fertility 应按
语言与领域切片进入训练成本、服务预算和输入可达性合同，而不是只作为 tokenizer quality 的一个平均指标。

扩 vocabulary 或 continued pretraining 可能降低高 fertility 语言的 tokenizer tax，却会改变 checkpoint compatibility、
embedding/output head、artifact version 和序列分布。exact-v1 的 25 个欧洲语言与披露 domain/few-shot 实验只能支持
这些切片中的成本差异，不证明 fertility 单独决定任务质量。迁移兼容、实际序列成本或 held-out quality 不通过时，
应保留旧 tokenizer，并用语言路由、context budget 或独立模型路径缓解，而不是无条件重编码全部模型资产。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-24718:end -->
<!-- source-family:SF-2026-ARXIV-2605-24718 -->

### 共享参数不保证跨语言知识能够跨 Token Space 流动

多语言预训练把不同语言放进同一 Transformer，在 token/embedding support 有足够重叠时可以共享统计结构；若两种语言几乎落入互不相交的 token 子空间，参数虽然物理共享，梯度和表示路径仍可能形成知识隔离。Tokenizer identity 因而不仅决定序列长度，也决定哪些跨语言 evidence 有机会在 embedding、attention 和 output head 中相遇。<!-- source-family:SF-2026-ARXIV-2609-19291 -->

扩大共享词元、加入平行/对齐数据或 continued pretraining 可以改善通路，却会改变 fertility、checkpoint compatibility 与语言公平性。作者受控实验不证明 token overlap 是跨语言迁移的唯一原因；语言结构、数据量和 post-training 仍是混杂因素。语义边界或书写系统不适合强行共享时，应保留语言专用路径与显式 alignment，而不是为了共享率破坏可逆性。


## 词表优化：先固定可选择的单位，再比较目标

前面的成本分析说明了为什么要选择词表；下面再区分哪些边界属于搜索空间，哪些指标只是这个空间内的优化目标。增加词表或缩短编码后的序列，都不能跳过模型行为的验证。

词表构建也不必把结构发现与最终压缩放在同一个目标里。一条替代路线先以 MDL、边界熵和 latent morphotactics 发现可复用的内部单位，再按实际省下的 token 次数将它们打包成固定 surface vocabulary；runtime 仍只输出固定 token IDs，不向模型另传 latent 标签。语言证据总量重权可改变内部结构的支持，但不等最终各语言分得相同 embedding 配额。<!-- source-family:SF-2026-ARXIV-2610-12376 -->

[受限多语言 encoder 实验](https://arxiv.org/html/2610.12376v1)支持这两层分责，却不证明 morphology 或 allocation parity 足以带来 outcome parity：最小语料语言的任务收益并未统一成立，更复杂构建还增加搜索与 HMM 成本。单 pretraining seed、有限 encoder 与 fine-tune seed 列表口径差异限制外推。简单 MDL/BPE 在成本或部署稳定优先时仍合理；无论怎样发现词表，下一步仍须先检查 pre-tokenizer 是否已禁止了必要合并。

### Pre-tokenizer Boundary 会形成 BPE 无法补救的硬下界

BPE 只能在 pre-tokenizer 允许合并的边界内学习；如果字符、附加符号或书写单位在此前已被错误切开，后续增加 merge 数量也无法恢复原本应共享的表示。tokenizer 设计因此要先验证语言学边界与 normalization，再优化词表大小和 fertility。旧分词在主流语料上仍可合理，但跨文字系统迁移时必须重新测量不可合并边界。
<!-- source-family: arxiv:2608.26449v1; semantic-body-binding: pretokenizer-boundary-fertility-floor -->

边界确定以后，还可以只改变执行这个边界规则的热路径，而不重新设计分词语义。例如，把特定正则规则编译成按当前与下一个 Unicode 类别分派的扫描器，常见分支直接前进，无法在局部判定的缩写等情况再回退到完整规则。这里保持的是预分词片段及规则优先级；normalization、后续 BPE merge、词表与整数 ID 仍属于各自接口，不能由“文本还原相同”代替回归。有限语料上的逐片段一致性也不证明所有 Unicode、尾部或空输入都已覆盖，更不保证整条模型服务链加速。特殊分支频繁、行为测试不足或输入分布变化时，原正则实现仍是合理基线。这与下面改变离线词表搜索空间的分支不同：前者优化如何执行既定边界，后者改变允许形成哪些单位。
<!-- source-family:SF-2026-ARXIV-2601-05833 -->

固定预分词边界还限制了词表训练能发现的单位：即使语料中两个相邻词经常共同出现，普通BPE也不会跨边界合并。允许superword的一个条件分支先训练完整regular merge顺序，再聚合符合条件的相邻pretoken run，让候选supermerge频数与regular顺序的重放计数竞争；计数相同优先regular merge，使supermerge所需的父token先存在。聚合run可以避免反复保留和扫描全部原文，但候选统计、type/token分布与更新成本仍决定训练效率。

这改变的是**离线词表构建**，不是每个请求自行造词；相同词表集合和merge关系也不保证相同整数ID顺序。切换实现必须核对完整token→ID映射及模型embedding/checkpoint兼容性，不能只比词表大小。[Faster Superword的实验](https://arxiv.org/html/2604.05192v1)限MiniPile及131072词表的CPU训练计时，不证明LLM端到端推理加速。边界稳定、词表已部署或新统计成本无法摊销时，原BPE仍是合理选择。<!-- source-family:SF-2026-ARXIV-2604-05192 -->

允许跨pre-tokenizer边界以后，仍要决定有限词表优先收哪些长组合。统一频率排序在常用短片段上简单合理；若目标是给较少出现的形式结构更多预算，一条条件分支按pattern类型和长度改变merge门槛：一般文本用空格数加一，LaTeX/字母数字结构用字符数的log2作为指数，将基本频率阈值乘以相应的`theta^指数`，其中`0<theta<1`。每轮重编码、重新统计support后再合并，使长结构在较低频率下也可准入；regex分类不是语法正确性验证，新增单位也不自动获得完整语义。这是离线构词的预算选择，不是增加原始语料或允许请求在线改写token身份。

[混合自然语言/LaTeX的受限对照](https://arxiv.org/html/2610.32921v1)在相同10GB语料、近似而非严格匹配的词表（200k与204601）下缩短了LaTeX编码，但SQuAD/DROP相对SuperBPE反而略长；更激进门槛还可把词表推到百万级。压缩配置与下游小decoder使用的配置不同，不能拼成同一个控制实验；后者数学accuracy处于地板，只见BPB改善，BoolQ/CSQA的BPB又变差，不支持数学推理提升或全面无损。应共同保存分类/长度规则、每轮support分母、最终词表/ID与checkpoint，计入构词、较大embedding/output head、重训和真实任务回归；编码长度或CPU tokenization计时不替端到端训练/服务费用。结构比例漂移、词表膨胀或下游质量不合时，保留普通BPE、原superword门槛与稳定artifact，不只为更高supertoken占比迁移模型。<!-- source-family:SF-2026-ARXIV-2610-32921 -->

### 从局部启发式到可审计的全局目标

BPE 与 Unigram 的局部或迭代选择易实现、稳定且兼容成熟 checkpoint，因此仍是生产基线。但当团队要回答“这个 vocabulary 距离指定 compression objective 的最优值还有多远”时，只比较最终 token 数并不够：vocabulary 的优劣始终相对于一套确定的 inference procedure，而不是孤立的词表集合。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-22705:start -->
一种路线先生成与 vocabulary 无关的 split-tree artifact，再规定递归遍历时发出第一个命中 vocabulary 的节点，最后在这套固定 traversal 上用整数规划或近整数的线性松弛选择词表。这样 inference procedure、split-tree revision 与 vocabulary 共同组成 tokenizer identity；改变任一项都可能改变同一字符串的 token IDs，不能只把新词表热替换进旧 checkpoint。

全局选择能减少局部 merge 的目标遗憾，却增加 count table、递归 decoder、LP/IP 求解与随 split-tree 数增长的训练成本；所测英语语料、词表和 1.5B 模型也不证明多语言或下游普遍更优。pre-token boundary、求解成本、行为回归或 checkpoint 兼容性失败时，应保留原 BPE/Unigram，只把全局解作为离线诊断。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-22705:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-22821:start -->
另一条路线把 vocabulary 与 segmentation 写成离散优化问题，再用 convex relaxation 给出指定 corpus 和 objective 下的 lower bound。这个 bound 可以把“似乎已经很好”改写为可检查的 optimality gap，但 solver 只拥有优化证据，不能拥有 tokenizer 的发布决定：rounding 后的词表仍需通过 sample stability、bits-per-byte、多语言切片、下游质量和生命周期成本 Gate。

接近松弛下界不等于语言建模、延迟、公平性或既有 checkpoint 的全局最优。求解与 rounding 增加成本和样本敏感性，intrinsic compression 改善也可能无法稳定转化为 downstream 收益；LP 过大、rounding 不稳或行为切片回归时，仍应保留 BPE/Unigram，把 lower bound 仅用于量化未解释的 compression headroom。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-22821:end -->

## Tokenizer 与 checkpoint 是联合行为接口

相同底层字符串可以存在多种合法 token segmentation。若只验证 detokenized 文本一致，就会误以为模型输入语义未变；实际上 token boundary 会改变 embedding 序列、position、attention path 与生成概率。跨语言实验表明这种脆弱性并不均匀，因此英语上的 segmentation robustness 不能外推为 checkpoint 的普遍性质。

数值序列还可在不换词表的条件下改变展示边界：保留数字值与原顺序，只把每隔若干项的普通delimiter换成另一separator，再让模型读取。[受限SepSeq对照](https://arxiv.org/html/2604.07737v1)表明这种局部格式选择可改变长序列copy/计算行为，但某些小模型或复杂任务反退，不能把替换后的attention代理当作普遍分段隔离定理。值/索引保持与实际token数必须经原parser和tokenizer分别核验；替换可能改变全部Q/K，等长度也不等内部计算等价。Separator、间隔、原序列与checkpoint须一同保存，response变短不表示输入更短或端到端更快；格式搜索、生成与数值校验仍付费。解析、copy或实际任务回归时，保留原delimiter与显式数值工具，不让较流畅的语言回答替代可核的数值交接。<!-- source-family:SF-2026-ARXIV-2604-07737 -->

固定词表使输入与输出共享同一套 token 身份；在线动态 codebook 则让多个不同长度的合并 token 竞争同一文本前缀。输入组合需要保留整个 span 的内容，输出分类又需区分这些前缀竞争者，因此一个共享组合器可能承受不同几何目标；可分开 input/output encoder，并按原始 token span 定义位置，而非只用压缩后序号。合并 digits 等敏感单元还会改变推理质量。动态词表要另报同文本的合法切分概率：只在 canonical prefix 下汇总 target 的多种切分，不等于全文 segmentation 的联合边缘概率。它增加组合、codec 和评分成本；[zip2zip++ 的受限 LoRA 对照](https://arxiv.org/html/2610.13605v1)仍有代码/指令反退，压缩无损只指可还原文本，不授模型质量无损或服务加速。<!-- source-family:SF-2026-ARXIV-2610-13605 -->

模型发布、转换和 serving 验收应把 tokenizer revision、normalization、segmentation policy 与 checkpoint 绑定，并加入“同字符串、不同合法分词”的行为回归。多分词增强可能提高鲁棒性，但会增加训练分布宽度和成本，也未被证明对所有语言与任务都有效。生产中仍应优先固定 canonical tokenizer；只有兼容迁移或容错需求明确时，才承担非规范分词的训练与测试成本。

<!-- source-family:SF-2026-ARXIV-2607-26831 -->

另一种增强不必改变输出监督的 canonical tokenization：保持原 next-token targets，让同一 token 字符串的合法子词分解走额外的 causal encoder，再把辅助表示通过 cross-attention 注入 decoder。这样 canonical target 与随机辅助输入是两份接口，不能把它理解为给旧 checkpoint 热换分词；subtoken sampler、块内/块间顺序、允许读取的因果 mask、auxiliary encoder 与注入位置须共同版本化，embedding 数值关系仍由下一章承接。[Homotokens 的受限分支](https://arxiv.org/html/2601.02867v1)在推理时也使用该采样路径，因此额外 encoder、序列与采样成本不能记成免费 serving 收益。它在高重复训练数据下延迟 overfitting，却不在低重复条件或碎片化词表上普遍获益；小模型的 held-out next-token loss 也不是生成任务准确率。只需稳定 token 接口、缺少训练/推理兼容验证或质量回归失败时，原 canonical 输入与直接 NTP 仍是合理回退，不由相同 decoded string 签发内部计算或行为等价。<!-- source-family:SF-2026-ARXIV-2601-02867 -->

### Vocabulary Adaptation 是 Tokenizer 与 Checkpoint 的联合迁移

替换或扩展 vocabulary 不能只更新分词规则，因为新增 token 的 embedding 与输出参数在旧 checkpoint 中没有身份。Token alignment lexicon 可以用语料或 hidden-state 表示建立 source/target token 对齐，先把旧参数映射为新 vocabulary 的初始化，再用有限 fine-tuning 恢复行为；迁移资产必须同时版本化两个 tokenizer、alignment matrix、初始化方法和训练语料。<!-- semantic-body-binding:SF-2026-ARXIV-2605-13429 -->

这是一种高效初始化而非 training-free transfer。目标词表明显缩小时会丢失旧参数承载的信息，长尾或领域 token 也受对齐语料覆盖限制；现有证据仍需约千步适配且只覆盖所测模型。对齐质量不足时，应回退更长的 continued pretraining、保留旧 vocabulary，或为关键 token 使用显式兼容映射。

映射新embedding之后，还可在共同文本segment上蒸馏后层交互，而不要求两个tokenizer给出相同token数：按两套切分都不跨越的边界合段，以各段末token作为query，再汇总指向每段的attention-weighted value贡献。[受限迁移实验](https://arxiv.org/html/2510.21954v1#S3)冻结主体与重叠embedding，只适配新增输入行；tied输出可复用它，untied则仍有独立LM-head接口。这里匹配的是模型内通信代理，不认证知识已完整迁移；更深或所有层同时对齐也未必更好。共同分段、teacher/student层位、输入输出参数和适配语料需一起版本化，付出teacher前向、蒸馏与新增词表成本；压缩率提高仍可能伴翻译质量退步，不能直接换算为端到端加速。层间对齐、原支持语言或真实费用回归时，保留简单初始化、原词表或更长continued pretraining。
<!-- source-family:SF-2025-ARXIV-2510-21954 -->

新增 item 的选择也应与初始化一起验收，而非先扩词表、再随意平均旧 embedding。一个受限分支用既有模型在词尾位置的中间表示读出来估计词/affix 的可组合性，再将这些 contextualized representations 经映射与汇总构造新增参数初始化，最后通过 embedding-only 的语言适配训练恢复行为。这类读出只提出哪些 item 适合迁移的线索，不证明模型内部已经保存固定词义；item 集合、hidden-state 层/位置、映射与 reduction、输入输出参数和适配数据共同定义迁移资产。<!-- source-family:SF-2026-ARXIV-2604-16656 -->

更长 item 不必然缩短实际序列：HF added-item 优先匹配可能先吃掉一个短片段，破坏原本更好的合并，使某些输入的 token 数反而增加。因此选择阶段要跑真实 tokenizer 执行路径，而不是只比较候选字符串长度；初始化也要连同 BPB、held-out 任务和原支持语言的回归验收。原文有限模型/语言中，FVT 在部分 Latin 切片更好，原先不支持语言及其他质量切片也有退步；表示探针、embedding 适配与额外词表参数均有成本，不能从 fertility 改善推出端到端推理收益。旧 vocabulary、简单组合初始化或更长 continued pretraining 在映射不稳或收益不足时仍合理。<!-- source-family:SF-2026-ARXIV-2604-16656 -->

轨迹中的频繁文本片段也可成为新增词表项，但压缩一个看似重复的action短语，不等于合并了真实环境动作。一条受限分支按word n-gram频次与下一token熵选择候选，最长优先替换为新ID，再训练新embedding与小型LoRA，以共享内容位置上的teacher分布蒸馏恢复模型行为。低熵只反映所采轨迹的可预测性，不推出任意history下转移语义等价；搜索词、实体和参数绑定越具体，越应保留原字符或词元，而不是按频次吞并。<!-- source-family:SF-2026-ARXIV-2605-18597 -->

[有限轨迹词表对照](https://arxiv.org/html/2605.18597v1#S5)将生成token数称为effective horizon，其减少不能认证低层action减少、外部协议可执行或同比端到端延迟；部分任务准确率退步、两KodCode设置峰存略升，静态prompt替换也不是多步动作闭环。轨迹采集、候选筛选、新参数/蒸馏、全部生成与真实工具验证都付费；分布漂移、参数语义或质量/净费用失配时，保留原词表、具体参数和普通tool接口，先独立验解码后的行为，不让entropy gate自签无风险。

固定词表迁移仍为每个新 item 分配离散参数；另一条分支则保留确定的文本切分规则，让开放字节串经过因果局部 encoder，再由组内 cross-attention 计算一个 word-level latent，交给全局 backbone，最后用已移位的 next-word latent 条件化逐 byte decoder。这并非“没有分词”：Unicode、camel case、空白与标点规则仍决定组边界；变化在于不再为所有可能的 word 保存固定查表行。复用旧 backbone 也不是热换 tokenizer，旧 embedding 与 LM head 被新 encoder、connector 和 decoder 替换，必须通过冻结起步与继续训练恢复接口。固定 subword/checkpoint 在无需迁移或兼容验证更重要时仍是合理基线。<!-- source-family:SF-2026-ARXIV-2603-15953 -->

较短的全局序列也不自动成为较快的服务：word 内的 byte 生成可以只走轻量局部环，跨 word 边界才再次调用 backbone，因此一次请求同时持有 byte/word 两种进度与不均匀映射的两份 KV；只有两边都能继续分配，它才可前进。批内等待边界以提高 backbone 利用率，会与输出延迟相冲突，字节层的小参数量也可能伴随更大的 activation。[受限迁移与 serving 说明](https://arxiv.org/html/2603.15953v1)明确报告当前批处理吞吐低于 FLOP-matched tokenizer 模型；bytes-per-backbone-position 是压缩单位，不是端到端收益，任务质量也有反退。迁移训练、规则边界、双状态协调或目标流量回归不合算时，应保留稳定词表与普通生成路径；下面的 dynamic patch 分支则进一步把边界选择本身交给模型。

## Dynamic Byte Patch 把分词边界变成 Runtime State

增量 tokenizer 仍执行冻结的分词规则；下面的分支则连边界的产生方式也改了，因而需要模型配合，不能当作前面增量编码的等价执行优化。

纯 byte-level 表示消除了 OOV，也给跨 tokenizer 计量提供稳定分母；旧方案在短文本、严格 streaming 或实现简单性优先时仍然合理。但生成每个 byte 都走一次全局模型，会把计算步数推向输出字节数。一个有条件的演进是让 dynamic patcher 把可预测的连续 bytes 聚成 variable-length latent，由 global model 按 patch 前进，再让局部 decoder 用 block diffusion 或 self-speculation 并行提出 bytes。

此时 patch 不再只是离线 tokenizer 选择，而是带 byte offset、algorithm/revision 与边界状态的 runtime artifact：tokenizer owner 决定 patch identity，生成范式拥有 provisional masked block，完整 causal verifier 独占提交。若要求 greedy 等价，verifier 必须重新编码候选并只接受到首个 mismatch；这不自动外推到 sampling distribution。更少 global steps 换来 patch drift、固定 block 浪费、额外 re-encode 与 cache invalidation，patch 校准失败或非 greedy 分布需要严格保持时，应回退普通 byte AR 或稳定 subword tokenizer。

[受限证据](https://arxiv.org/html/2605.08044v1)覆盖作者的 architecture、dynamic patch、block generation 与 greedy verification 实验；正文未单列完整 limitations，且没有证明任意 sampling、硬 streaming 或生产 latency/SLO 下都获益。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-08044 -->

动态边界还可以通过训练日程控制，不必始终使用固定压缩目标：让hierarchical byte模型从较低target N起步，warmup后逐渐提高，再以一段平均loss的阈值触发调整。[ATDC的受限机制](https://arxiv.org/html/2605.30080v1#SIV)修改的是路由balancing loss中的软目标；真实Bytes-Per-Innermost-Chunk要另测，既不是N硬上界，也不是由BPIC反馈自动闭环。目标更大仍可能得到更多inner chunks，因而不能由日程终点推算节省FLOPs、吞吐或稳定性保证。阈值来自额外static基线、日程与模型必须一同版本化，byte全长encode/decode、路由/dechunk和实测latent计算全计费；同参数不等同算力，固定byte/token换算也不代表任意语料口径。质量或实际负载反退时保固定N、较小patch与稳定subword路径，不由更低BPB替运行预算签字。<!-- source-family:SF-2026-ARXIV-2605-30080 -->

预测下一 byte 的高熵是 patcher 的困难，不必等于全局计算最值得花的位置。另一条受限路径用离线重复匹配构造新颖性监督，再让只读已见前缀的因果 proxy 提议边界；未来字符串可用于训练 target，不能进入运行时边界决定。[小模型的必要对照](https://arxiv.org/html/2610.22100v1)中，数学答案跨度的 teacher-forced 准确率可以提高而 BPB 变差，code/trace 又未稳定胜过 entropy，不能把跨度恢复当端到端解题能力。边界与模型需联合验收，直接换规则还可能损伤另一答案位置；训练目标 patch 率也不等实际运行预算。Proxy 构建、重训和局部/全局计算均计费，收益须对齐真实 patch 数、任务与成本；新颖性失配或质量回退时，原 entropy、较小固定 patch 与稳定 subword 路径继续合理。<!-- source-family:SF-2026-ARXIV-2610-22100 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-09630:start -->
大 patch 以更短的全局序列换吞吐，在局部规律稳定时简单有效；但若 patch 内的计算必须等到边界才发生，局部信息会形成 patch lag。一个中间分支是在 patch 内按 entropy 或其他可重放条件插入瞬态 scratchpad，让局部状态先聚合已见 bytes，再刷新后续预测所用的 patch context。这样 patch owner 仍决定边界和身份，scratchpad 只改变计算 cadence，不成为可跨请求持久化的 Memory。

这条路径用额外 attention、KV、mask 规则与触发频率控制换取更及时的 patch 内计算；触发过密会吃掉长 patch 的吞吐收益，触发过疏则保留原有 lag。当前证据只支持作者的 byte-level architecture、训练设置和 evaluator，不证明在其他模型、硬件、长度或生产 SLO 下普遍获益。局部状态不稳定、实现缺少可靠 mask 或短 patch 已足够时，应回退较小固定 patch 或稳定 tokenizer。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-09630:end -->

边界可学习时，还要说明梯度究竟优化什么。对 Bernoulli boundary policy 采样分词方案，再以该方案条件下的 byte prediction loss 训练全局模型，score-function estimator 可以把条件 loss 的期望作为边界选择目标；这不同于把随机分词的平均 log-likelihood 当作 marginal log-likelihood，后者在一般情形只有 Jensen 不等式，不能用等号跨过。离散采样避免 straight-through 把边界当连续变量，却增加梯度方差、边界头和 byte decoder 费用；[受限实验](https://arxiv.org/html/2602.13940v1)还使用 discount 与含本样本的 batch baseline，不能授最终估计器无偏。作者的固定估算 FLOPs、有限语料/小模型 loss 对照不等真实硬件吞吐或所有任务更优；边界漂移、训练方差或质量代价过大时，固定 patch 或稳定 subword tokenizer 仍合理。<!-- source-family:SF-2026-ARXIV-2602-13940 -->

<!-- source-family:SF-COMPUTE-OPTIMAL-TOKENIZATION -->

## 工程验证清单

Tokenizer 接入不应只测试一句英文。至少需要验证：

- encode/decode round trip 与 normalization 预期。
- 中文、英文、代码、数字、emoji 和异常 Unicode。
- special tokens、chat template、padding、truncation 和 EOS。
- 与 checkpoint 声明的 vocabulary、id mapping 和配置一致。
- 目标流量中的 token length 分布，而不是只看字符长度。
- tokenizer 版本变化后的离线评估与容量影响。
- 长会话增量路径与 frozen reference 的逐 id 等价、fallback 与 mismatch quarantine。
- tokenizer session state 与 KV Cache 的 identity、lifetime、eviction 和恢复边界。

## 本章在知识树中的位置

```text
Raw text
-> normalization
-> subword / byte segmentation
-> token ids [B, T]
-> Embedding [B, T, d_model]
```

Tokenizer 是 Part II 的入口，也是 Part I 宏观约束第一次落到具体 tensor contract 的位置。它定义模型的离散输入接口，也提前决定了后续参数、Attention、KV Cache 和 Serving 成本的一部分。

本章只拥有 text ↔ token ID。第23章拥有 raw modality ↔ continuous/discrete multimodal representation；把 image code 称为 token 不会让它自动继承文本的可逆性、边界或序列成本。

这份接口会跨 Part 延续：第 27 章在固定 tokenizer 下构造训练 sequences，
第 29 章把 special tokens 与 chat template 纳入 SFT protocol，第 42 章要求
Serving 以同一 tokenizer artifact 还原请求。任一环节独立替换 normalization、
vocabulary 或 role tokens，都会形成 training-serving skew。

## 自检问题

1. Word-level tokenizer 为什么会遇到开放词汇问题？
2. Character-level tokenizer 用什么代价换取 OOV 覆盖？
3. BPE 的 merge 是如何从小语料统计得到的？
4. BPE 与 Unigram 的搜索方向有什么不同？
5. Byte fallback 为什么能减少 `<unk>`，又为什么可能增加 token 数？
6. 为什么替换 tokenizer 会破坏原 checkpoint？
7. Vocabulary size 为什么同时影响 embedding 参数和 Attention 成本？
8. Special tokens 为什么应被视为协议？
9. Tokenizer 如何造成多语言 token efficiency 差异？
10. `[B,T]` 的 token ids 为什么不能直接作为连续数值输入模型？
11. 为什么 `tokenize(A) ++ tokenize(B)` 一般不等于 `tokenize(A ++ B)`？
12. 增量 tokenization 为什么需要 reference equivalence、版本绑定与安全回退？

## 小结

Tokenizer 在无限文本空间和有限模型词表之间建立可复现映射。Subword 方法在词级 OOV 与字符级长序列之间折中，byte fallback 提供开放输入覆盖，special tokens 则建立模型协议。

这个选择会一路影响 embedding 参数、sequence length、Attention、KV Cache、成本和多语言公平性。Tokenizer 不是语言学答案，而是 AI System 的第一份模型接口契约。

到此得到的只是稳定的整数序列，还没有可学习的数值关系。下一章从 one-hot 与查表出发，解释 token id 如何变成连续向量，以及词表变动为什么必须连同输入、输出参数一起考虑。

## Review notes

- `SF-2026-ARXIV-2610-32921` — Daily2026-10-27；exact-v1 §2–7/Table1–5/App.F必要由B唯一首备，2+1+2=5，类型/长度merge门槛的具体预算差额。保约匹配词表、两配置不可拼、数学accuracy地板/通用BPB退步、词表膨胀与全费，不授语义完整、数学推理或端到端加速。未核代码/复现；必要/actualowner/整体PRE与真实SAVE/selfread/solePOST仅据本日唯一reader实际记录，不由本注预签。 R38必要/整体PRE、作者实际SAVE/完整自读与R39唯一actual POST通过，本指定窄位已释放；仅同步既成结果，不重必要/POST或预DAY。

- `SF-2025-ARXIV-2510-06128` — Cicero，Daily2025-10-09补Oct08BJT；[Parallel Tokenizers exact-v1](https://arxiv.org/html/2510.06128v1)A104首次必要§3–4/5.2–5.6决定域/T3/T5/Limitations/Ethics/AppH，2+1+2=5，仅各语言切分/共享ID/语言条件消歧接口深入。保MT61%非全对齐、索引/多义资格、LR混杂/CPT与低资源反退和全费，不采不同ID阻止共享/全语义或无损迁移。未核全追加表/图像素/外部实现或复现，PRE/SAVE/selfread/solePOST仅本日canonical，不以本注预签。

- `SF-2026-ARXIV-2610-24818` — Daily2026-10-21/Oct20；C10必要exact-v1 Source/actual owner/完整PRE由root ROOT-C10-PRE具名通过，按root既授精确窄位保存原单段/唯一marker。保原稿受限人口、直接反侧及全部费用，未核实现/复现；作者完整新增/直接完整两侧及本注自读后待唯一非writer actualPOST，不预生效/DAY。 截至本轮，唯一非writer ROOT-C8/9/10/11-POST actualPOST已实际通过并生效；上述待POST只保历史过程，不再表示当前未完。仅行政同步，不第三核正文/Source。

- `SF-2026-ARXIV-2610-26225` — Daily2026-10-21窗Oct20；exact-v1 §3–6/Limitations/A4–5必要，2+1+2=5。只采local criterion与父子依赖，保budget口径/明显RC退步/迁移runtime缺口及全费；不采公式最优/无损/实测模型缩小，未核代码/复现。core B-R1必要Source/actualowner/完整PRE原样通过，root已授完整source-support成本退路后/固定artifact前原单段及本人注；作者已真实保存并完整自读新增/完整直接两侧及本人注，core B-R4唯一非writer actualPOST已通过，窄位生效释放；仅行政同步既成事实，不第三核。未核代码/复现，不授DAY。

- `SF-2026-ARXIV-2610-22071` — Daily2026-10-17窗10-16；[exact-v1](https://arxiv.org/html/2610.22071v1) §2–5.2/5.6/7必要，2+2+2=6。仅采用可逆合法编码与有限lookahead可辨识性分责，保目标/实际预测区别、跨页碰撞、更多UTF8 lookahead与重对齐全费，不授全模型能力/热兼容。root已核必要Source/PRE并授此单段与本人注窄写；作者已保存并自读，root实际正文/完整直接两侧/本人注POST通过。未核实现/复现，不授DAY。
- `SF-2026-ARXIV-2610-22100` — Daily2026-10-17窗10-16；[exact-v1](https://arxiv.org/html/2610.22100v1) §3–8/五张主表与局限，2+2+2=6。仅采用entropy与compute价值代理分离、离线future目标/在线causal proxy及联合训练边界；保BPB、teacher-forced跨度、code/trace反侧和实际patch预算/费用。root已核必要Source/PRE并授此单段与本人注窄写；作者已保存并自读，root实际正文/完整直接两侧/本人注POST通过。未核实现/复现，不授DAY。

- `SF-2026-ARXIV-2604-14053` — Daily `2026-04-17`来源补充；[SA-BPE exact-v1](https://arxiv.org/html/2604.14053v1) §4.1/Algorithm1、§4.2–4.4、§5.1–5.3/Tables2–4、§6/Limitations，2+2+2=6，source-support离线merge剪枝/优先级与固定runtime接口的具体缺口深入。支持数非quality truth，高阈值耗尽merge/统计成本、100M固定token预算与undertrained probe不能证明raw exposure或下游/安全收益均近正文保留。root R5必要Source/PRE、R6自然日联合资格与窄锁、实际正文两侧非writer POST通过；本注已同步，作者实际读回后由root定点末注回读释放锁，不授DAY；未核实现或复现实验。

- `SF-2026-ARXIV-2610-13605` — [zip2zip++ exact-v1](https://arxiv.org/html/2610.13605v1) §2–5/Eq3–4及Appendix F的canonical-prefix反侧；Daily2026-10-13，2+2+2=6，具体缺口深入。input/output几何、span位置和segmentation评分分责；四模型LoRA/同配置，code/IF反退、敏感digits与gap未闭保留。root必要Source/PRE通过，root实际非writer局部正文/邻接与本注POST通过；未核artifact或复现。

- `SF-2026-ARXIV-2601-05776` — Daily `2026-01-13` 增量；[Romanization exact-v1](https://arxiv.org/html/2601.05776v1) §2–4/6；2+1+2=5，native/roman分支差额深入；149Mencoder/mono-multi控制/fidelity-fertility/中日反侧与费用近文，不授LLM热换词表。jan10_books_audit必要原证/actual owner PRE通过、root授窄锁；作者完整邻接已顺读，root非Books写入者已实际读正文/完整邻接/自身末注，POST PASS；窄锁释放。未核实现/复现，非日级Gate。

- `SF-2026-ARXIV-2601-05833`：[Peek2 exact-v1](https://arxiv.org/html/2601.05833v1)，Daily 2026-01-13；原2+1+2=5，具体行为保持的预分词执行分支缺口深入。必要§3/4与完整 XNLI 片段回归，仅采用7类双scalar分派及缩写回退，不授所有输入等价、生产吞吐或普遍安全保证；硬件未披露，未复现。jan01_v3实际必要原源→owner非作者核通过；正文写后待独立验收。

- `SF-2026-ARXIV-2602-04289`：[Proxy Compression exact-v1](https://arxiv.org/html/2602.04289v1)，Daily 2026-02-06；原2+2+2=6，具体 train-proxy/serve-byte 接口缺口深入。必要§2与§3.1–3.4/3.6及负侧；只采用压缩代理/原始byte混合训练、sentinel与disjoint vocabulary、paired warmup后解除配对而byte-only部署的替代分工。固定symbol预算非同raw exposure，0.5B反侧/gzip失败、compressed-gold oracle非正常生成、准备与byte Decode成本就近保留；不授neural无损、普遍质量或latency优势。root必要原源/Ch11 owner写前通过，root实际126正文单位→train/serve分支→UTF8合法性及422末注POST通过；日级Gate未验，未复现实验。

- `SF-2026-ARXIV-2602-04706`：[LiteToken exact-v1](https://arxiv.org/html/2602.04706v1)，Daily 2026-02-06；原2+2+2=6，具体input merge graph/output emission artifact gap深入。必要机制与评测/配置反侧，保留recursive split/remerge输入、禁输出但不改生成prefix、FI/邻熵的语料人口与长度/质量/backend分账。§6.2 Table4 .25与正文.15、§6.6配置冲突不拼接收益点，不授PPL/confidence=真实准确或免费无损转换；未复现。jan02_v3实际必要source及Ch11:64–139写前核通过，root授窄锁；jan02_v3实际新增正文/前后邻接及末注POST通过，日级Gate未验。

- `SF-2026-ARXIV-2601-02867`：[exact-v1](https://arxiv.org/html/2601.02867v1)，Daily 2026-01-08；原2+1+2=5，canonical-target/aux-input branch具体接口缺口深入受影响知识。必要§3/4/5/Limits及A2/A3；只采用额外因果encoder/首decoder cross-attention与同string子词采样身份，推理同用不记为免费收益。88/244M与额外1M encoder、4A100/4～24h、concatQA next-token loss而非meaningful generation，重复比/fragmented词表反侧保留；不授通用多语/生成准确率或checkpoint热兼容。root必要原源与Ch11 owner写前核通过，实际331正文、323–329 canonical接口与333词表迁移邻接及420末注POST通过；日级Gate未验，未复现实验。

- `SF-2026-ARXIV-2604-16656`：[exact-v1](https://arxiv.org/html/2604.16656v1)，Daily 2026-04-21；§3.1–4、§6.1–6.4/Table1 与 A。只采用 item selection×hidden mapping 初始化及 added-item 优先的短项反收益，不将 readout 视作固定词义证明；FVT Latin、OOD 与适配成本边界保留。apr02 必要 source→当前 owner 独立通过；实际正文及相邻衔接写后非作者复核通过（root），未复现实验。

- [2604.05192v1](https://arxiv.org/html/2604.05192v1)，Experimental；§2–5/Algorithm1，regular顺序重放、supermerge竞争、tie规则与ID重新分配边界。只采用词表训练机制，不将CPU tokenizer训练提速外推为模型训练/推理收益。

- Tokenization as Output Supervision（Status: Experimental）：[arXiv:2609.01386v1](https://arxiv.org/html/2609.01386v1) §2.1/3.1–3.4 将输入与输出 tokenization 解耦、仅在输出侧计算 CE；采用输出监督粒度命题。四层小模型、三位小端加法、十 seeds 不证明通用 tokenizer 优劣；相同步数非同计算量，不采用“未来位没有梯度”或 probe 不可读等于信息不存在的强解释。

- `SF-2026-ARXIV-2602-06394` — Daily `2026-02-10`；[QA-Token exact-v1](https://arxiv.org/html/2602.06394v1) §3.3/§4两阶段、Table2、AppC.7/G.3必要条件与成本。5=2+1+2，external-quality proxy→learned merge→fixed artifact具体gap深入，只采用通用tokenizer受限接口，不纳科学/金融路线或应用收益。一般LMloss非submodular、globalconv/免成本不采用；raw exposure与steps、构建/重训成本和proxy失配回退近正文，未核代码/复现。root必要原源/owner写前通过，root实际L85–100正文邻接及末注445非作者POST通过，锁释放，不授日级Gate。

本轮联章 Review 补充了 Part II 的主干与扩展分支地图。本章仍止于 token ids，不展开 embedding 训练，也不把 tokenizer training 混入 Part IV 的数据治理。后续 Review 应以具体 checkpoint 的 tokenizer artifact 核验 normalization、special-token 和 byte fallback 行为，避免把某个库的默认配置写成通用机制。

Primary-source 校验入口：

- Rico Sennrich, Barry Haddow, Alexandra Birch, "Neural Machine Translation of Rare Words with Subword Units", 2016: https://arxiv.org/abs/1508.07909
- Taku Kudo, John Richardson, "SentencePiece: A simple and language independent subword tokenizer and detokenizer for Neural Text Processing", 2018: https://arxiv.org/abs/1808.06226
- Taku Kudo, "Subword Regularization: Improving Neural Network Translation Models with Multiple Subword Candidates", 2018: https://arxiv.org/abs/1804.10959
- Zhenyu Zhang, Zhichao Cao, "TokTier: Exact Stateful Tokenization for Agentic LLM Serving", 2026（Status: Emerging；作者实验，不外推性能数字）: https://arxiv.org/abs/2607.29678

- `SF-2026-ARXIV-2602-13940` — Daily `2026-02-18`；[exact-v1](https://arxiv.org/html/2602.13940v1) §3–4、必要消融/配置。2+1+2=5，expected conditional loss与离散边界梯度差额深入；Eq9 Jensen等号、discount/batch-baseline最终无偏不采用，固定估算FLOPs非实际吞吐。root必要源/actualowner PRE通过，实际正文/邻接与末注经root非作者POST通过，窄锁释放；未核实现或复现，非日级验收。

- `SF-2026-ARXIV-2603-15953` — Daily `2026-03-19`补`03-18`自然日；[HAT exact-v1](https://arxiv.org/html/2603.15953v1) §3.1–3.4/4.2/6/7.1–7.3.1及直接质量反侧，2+2+3=7。只采用rule-split/learned-word接口、旧backbone适配与byte/word双clock/KV成本；tokenizer-free非无规则，压缩非吞吐，FLOP-matched批处理反退/任务质量反侧近正文。不授热换兼容、普遍质量/加速或生产SLO；未核代码或复现实验。
- `SF-2026-ARXIV-2604-07737` — [exact-v1](https://arxiv.org/html/2604.07737v1) §3–4/Limit必要范围，仅数值/索引保持的delimiter格式分支，保小模型/复杂任务反退、Q/K变化与tokenizer限定，不采严格sink隔离界；response长度非全token/墙钟，未核代码/复现。

- `SF-2026-ARXIV-2610-19801` — Daily2026-10-16窗10-15；[Delta exact-v1](https://arxiv.org/html/2610.19801v1)必要§3.2–3.4/4.1/4.5–4.8/Limit/S2–4，2+2+3=7。只采stateless safe-cut三条件与CPU chunk服务粒度，不把TokTier July2026已有session repair称本次首创；保byteBPE/dropout off/unsupported reference、runtime输入人口和dispatch/内存全费，不授生产恢复/全TTFT保证。root实际必要Source/date/具体owner有效，reader A7/R13逐字PRE通过，root授两段与本人注窄lease；作者已保存并读回，独立reader R14实际正文、完整邻接与本人注POST通过，root已接纳并释放指定窄lease，作者仅行政同步并实际读回。未核代码/复现，不授DAY。

- `SF-2026-ARXIV-2605-13436` — Daily2026-05-15补May14；[exact-v1](https://arxiv.org/html/2605.13436v1)pretrain/finetune阶段对照、T2及morphology必要域由readerR42一次实际Source、作者有限复用；2+1+2=5/Ch11具体差额深入。保10seeds仅FT、maxlen128/token非matched raw exposure、5/10%选择非最优定理、Morph F1采样/外部词表分母及部分任务反退；不授形态唯一因果/通用LM recipe或部署换ID，未核实现/复现。

- `SF-2026-ARXIV-2605-12928` — Daily2026-05-15补May14；[exact-v1](https://arxiv.org/html/2605.12928v1)§4–7/T1/A–B/D–G必要，2+1+3=6，readerR115独核。保raw exposure近似/两matching合同、MDM ELBO非任意sampler精确likelihood、外推非实测、span反退/BoolQ反侧及全费；原FLOPs处方未闭不照算，hardware/precision/seeds/fullwall未足披露。current仅v1，未核实现/复现。

- `SF-2026-ARXIV-2605-18597` — Daily2026-05-20补May19；[exact-v1](https://arxiv.org/html/2605.18597v1) 6分；必要§3–5及A2–4/A10–11/A14/T8；只轨迹ngram词表/teacher恢复，不授外部动作等价或普遍加速。 来源/具体owner/PRE由may20_supp_reader独核，正文仅限A4批准稿；未核代码/运行复现。实际两新段、完整直接邻接及本人note已由非writer R11写后通过，窄位生效释放；非整日验收。

- `SF-2026-ARXIV-2610-04951` — [exact-v1](https://arxiv.org/html/2610.04951v1)，Daily2026-10-07/Oct6窗，2+2+2=6；§IV–VI array-linked-list/merge与block边界必要层；lossless bytes非tokenID等价，merge微基准非全CPU/IO/transfer路径。root R10必要Source/date通过，literal PRE/实际POST另记，未核实现/复现，不授DAY。

- `SF-2026-ARXIV-2605-30080` — Daily2026-05-30补May29；精确Mayv1必要Source、具体owner与逐字PRE见本日SUP A54、reader R91/R95，首次2+1+3=6保持。只采正文限定机制，保反侧/费用与旧路径；未核实现/复现，不授一般安全/真值或性能保证。root已协调授本原单段+本人note精确窄位，作者实际保存，唯一reader R98已实际读完整新增/直接两侧/本人注POST通过并释放，不预日级。

- `SF-2025-ARXIV-2510-20208` — Copernicus，Daily2025-10-25补Oct24BJT；exact-v1 §4/7/8/Limitations，原2+1+3=6，字符串事件/单路径质量具体gap深入。只采用有限lattice不重复路径质量下界与累计集合包含才单调；不授无偏/完整marginal、完整采样recipe、canonical普遍较差或净生成加速。保输出边界/长度/候选耗尽、H100/250QA/150translation/1000路径及全部评分/候选费，未核实现/复现。整体PRE/真实SAVE/全新增与完整邻接/本注自读/sole实际POST仅同日canonical后到真实层，本注不预签。

- `SF-2025-ARXIV-2510-21954`：Daily 2025-10-29补窗；精确v1必要支持/直接反侧已读，未运行代码或复现。新差额是共同segment上attention-weighted V贡献蒸馏，区别已有token参数映射/teacher最终分布；保tied/untied与层深反侧，不授无损热换。
