# MuproCL / MANZANO 有限必要证据

Singer A200/A201确认两项只有题摘、准入和日门，无Methods首读、CORE或在途请求；root明确接受后首次捕获并准备下列必要域。日期、原评分和README仍由Singer维护。本文件不是Books决定或独立验收。Singer作为唯一另一角色回实际原域采用后，Sartre复用已闭角色链，不第三相同证据；尚未采用时不称已闭。

## MuproCL — 2509.16011v1

- 原件：[HTML](https://arxiv.org/html/2509.16011v1)、[raw](ROOT_CORE_MUPROCL_16011_20261024.raw)、[请求](ROOT_CORE_MUPROCL_16011_20261024.request.json)。GET UTC2026-10-24T08:21:24.991802至08:21:26.183707，200/exit0，246059B，SHA256 `7f026c2287b499d24ce80d6df9ee0a4255002b004312d67a34ef49f44dcc9851`。
- root实际完整读§2.1/2.2、式1–6，§3.1–3.4、完整表1–3/F2文字caption及§4；未看图像素、代码或运行实验。所需机制、直接单目标/模板对照、原型数反侧和费用已足，不以整份相关工作/附件为配额。

**改变的接口。** 原有随机可训练classifier可随任务漂移，冻结PLM单语义目标提供稳定先验但一词多义或多视觉形态可能冲突。这里让Qwen2-7B-Instruct提出类别不同义项/视觉形态，再用同一CLIP-B/32文本encoder嵌入；去非视觉义项、cosine>.95去近重复，以farthest-point和覆盖增量阈值.2选至每类最多4个。语义向量保持冻结，视觉encoder训练；每类先对多个inner-product作LogSumExp，再跨类别计算原分类loss。它改变监督target集合及其读出，而不是检索真实类别定义、逐输入调用LLM或新增稀疏expert routing。

**不能补成保证。** prompt是模型提出的先验，不是真实词义/标签审定；非视觉筛除和coverage gain具体执行定义未完整闭合，不补默认规则。式5没有除以每类K，K按类可变；若相同相似度为a，原式分数为a+log(K)，存在原型数量与语义覆盖混杂。原文没有给固定K/归一聚合对照以独立识别“更多正确语义”的唯一贡献；不能悄悄改成log-mean-exp。冻结target也不冻结视觉features，replay/旧类判别与所有CL机制仍需验收。

**实际证据和反侧。** CIFAR100单数据集，B=C=10/5/2、固定类顺序、每类20 exemplars，六CL基线；CNN160epoch/task、SGD lr.1/momentum.9/b128、80/120衰减，DyTox500epoch/Adam及后20epoch balanced finetune。不同backbone/方法预算不能直接排名归因。表1是本协议作者结果，±未明确重复次数/统计定义，不冒训练CI或任意顺序泛化。LUCIR表2中纯80模板ensemble的forgetting35.1优于full35.6，尽管full Avg/Last62.6/48.3优于61.6/47.8；去disambiguation/expansion各使Avg下降，也没有让所有指标同时最好。表3 K4→8 Avg62.6→62.5、Last48.3→48.2，而forgetting35.6持平；K16 Avg61.4下降但forgetting35.3反而更低，不是“过多原型使所有指标退化”。表1 DyTox B10 forgetting33.0→22.1是10.9百分点；IL2M Avg57.8→63.4是5.6百分点，不混相对百分比。

**成本与选择。** Qwen提议、过滤/选样、CLIP文本编码及固定原型驻留、更多类别内similarity/aggregation、全部encoder/CL训练、replay和独立旧新类评价均计费。训练墙钟/硬件/precision/峰memory/端到端SLO未披，不由轻量或冻结推净降本。可共存的退路为单类别固定目标、模板ensemble或原CL classifier；先独立审定目标语义、比较同预算准确率/遗忘/原型数偏置，再决定是否采用多目标。不预NC或必须入书。

## MANZANO — 2509.16197v1

- 原件：[HTML](https://arxiv.org/html/2509.16197v1)、[raw](ROOT_CORE_MANZANO_16197_20261024.raw)、[请求](ROOT_CORE_MANZANO_16197_20261024.request.json)。GET UTC2026-10-24T08:23:06.332135至08:23:06.958163，200/exit0，258151B，SHA256 `243a14576704a35de0c115eb41ff37392e8a820d3a94ad80dd2e79f642644011`。
- root实际完整读§3.1/3.2、§4.1/4.2三阶段、F3/4文字caption，§5.1–5.3/表1及F5/6直接caption、§5.4.2/完整表3、§5.4.3及§6；§5.3所内置完整表2也实际读。未看曲线/质例像素、§5.5编辑专门实现、代码或复现，不将未核编辑扩展纳入本命题。

**机制与状态。** 同一ViT后接两个adapter：STC3×3将42×42×1024重排为14×14×9216，再映到LLM宽度；连续支路供I2T，离散支路另经FSQ、64K码供T2I。共享encoder不等两表示数值相同或已无损对齐。Tokenizer阶段以300M decoder随机取一adapter作next-token训练，全参数可训，之后弃该小decoder。Unified LLM阶段冻结vision encoder与discrete adapter以固定图像词表，扩64K embedding；理解输入continuous、监督text，生成目标discrete ids、只对image token CE，text:image loss=1:.5。不得误写为全部tokenizer/continuous adapter永久冻结，也不把FSQ码直接当自然语言token。

统一AR先预测高层text/image序列，独立flow-matching图像decoder再消费离散条件从Gaussian noise生成pixels；该decoder训练冻结encoder/adapters。改变的是表示来源与两个生成阶段的分工，不是单一LLM直接diffuse pixels、取消AR或凭共同encoder保证语义/细节一致。连续/离散adapter、固定tokenizer/词表、AR checkpoint及pixel decoder需一同版本化，这是系统推断，不冒论文已实现全部兼容性检查。

**直接对照及不成立的强结论。** 表1用1B unified LLM比较pure-discrete/dual-encoder/hybrid，消融不做continued pretrain。Pure-discrete复用相同encoder/discrete weights，理解text-rich62.3对hybrid73.3，支持本条件下量化输入有损；但GenEval77持平、DPG80.9反高于hybrid79.9、WISE35持平，正文“全部任务都更好”不成立。Dual使用内部MagViT2/FSQ64K、压缩8、128而非256输入以取256tokens，较差结果不能独立证明异构语义空间是唯一因果。Unified/single-task比较缩短单任务步数以匹配相应可见token数量，不是匹配总计算；F5caption仍明示理解轻退、generation一项退，3B理解差<1不等零冲突/统计等价。无需为该受限结论读全质例。

Scaling 300M/1B/3B/30B固定decoder.9B，但30B因预算只训练约半数tokens；不是compute-optimal或严格同数据控制。图像decoder.9/1.75/3.52B增大，结构完整提升、instruction近持平、审美下降；GenEval/DPG近饱和、WISE仅局部改善，不授全维支配。表3 Manzano3B/30B GenEval overall均.85、WISE.46→.54，30B color-attribute.65低3B.71、Time.50低.51；专用Qwen-Image overall .87/WISE.67仍高于其.85/.54。跨模型数据、rewriting、参数和预算不匹配，不把竞争性结果当统一架构唯一因果/全球SOTA。800 prompts、每例3内部评者、匿名随机次序支持该有限人评协议，不替外域或生产质量；seedCI/完整prompt重复与独立去污染未披。

**全部费用。** 预训image理解2.3B pairs/1.7B interleaved documents、generation1B pairs，continued理解24M等为作者所述数据人口，非独立无重合审计。Unified mix40/40/20、通常1.6T/30B.8T tokens，continued83B，SFT41/45/14；DreamO单独训练过拟合的观察后加90K及4M Flux合成，不能把合成目标视真值或假定改动无费。Vision预训、300M tokenizer训练、全部授权/过滤/recaption/合成、AR训练、独立decoder256分辨率400Kstep再512/1024/2048各100K、AR图像token采样与完整flow采样及全部驻留、评价均计费。正文总体提30B+3B decoder，配置实为3.52B，不拿标称“30B模型”当全部驻留参数。实际硬件/precision、采样steps/NFE、并发/输入输出长度/端到端墙钟和SLO未披，不授更小更快或免跨模块同步。量化、细节或任务冲突失配时保留continuous理解、独立tokenizer/专用生成器、独立扩缩pixeldecoder与原混合目标，并分别验理解、语义token和最终图像。

以上两项只交必要证据与反侧，不改旧日期/原5与6分、不预owner或Books结果；当前原件请求均已结束。
