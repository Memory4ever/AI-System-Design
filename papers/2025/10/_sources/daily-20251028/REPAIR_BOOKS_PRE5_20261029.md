# I27–I36：消费R24实际差额的完整窄稿

十项均由sole R24实际owner比较发现；writer不再第二Methods或相同现有论证。完整外邻接见context5；I27/I28在同一原gap按本稿顺序组成两独立段，彼此完整稿也是各自新邻接。每项独立marker/本人注，未经整体PRE不写Books。

## I27 PLATFORM-SECURITY / RL watermark

文件：`books/part-06-ai-infrastructure/72-security.md`；DLM水印完整段后、后处理水印前；顺序I27→I28。

```markdown
学习文字水印时，检测器还可能只学到攻击留下的风格：冻结生成backbone，用语义mapper学习green/red分配，并同时优化原水印、改写及恶意编辑后的检测，必须另放“同样受攻击但从未加水印”的负对照。[受限RL水印分支](https://arxiv.org/html/2510.21053v1#S3)据此分开provenance与hate/paraphrase特征；四项AUC平均不认证所有攻击鲁棒，PPL也不等语义保持。原检测式mean(log p)非正，却与正0.5 reward锚点冲突，不能据印式补成可执行训练recipe。每backbone重训、攻击与负控、检测/质量和独立新攻击回归均付费；符号、质量或攻击人口不合时，保原水印/无水印基线与明确Unknown，不由攻击风格可识别批准来源认证或内容安全。

<!-- source-family:SF-2025-ARXIV-2510-21053 -->
```

```markdown
- `SF-2025-ARXIV-2510-21053`：Daily2025-10-28补Oct27；R9首次必要/R24实际gap，2+2+2=6/安全深入。仅攻击无水印负控与provenance分责，保reward符号冲突/四目标费用，不采数值recipe；未核代码/复现，PRE/SAVE/完整自读/solePOST据本日实际层。
```

## I28 PLATFORM-SECURITY / AlignedIS

文件：`books/part-06-ai-infrastructure/72-security.md`；紧接I27、后处理水印前。

```markdown
音频水印还要面对生成与检测的tokenizer不一致：同一波形再token化后，原token身份可能改变，可先对token embedding聚类，再在较稳定cluster上对齐inverse sampling与检测。[Aligned-IS的受限分支](https://arxiv.org/html/2510.21115v1#S4)中的distortion-free是对secret key期望的分布等式，不保证每条音频无损或必被检出；prefix/ngram、历史去重和key条件也属于身份。Binomial/Hoeffding误报界依独立null/有效code，十三种单通道改动不认证任意相关、组合或自适应攻击。聚类、encoder、key治理、全部生成/检测与独立音质/语义回归均计费；再token化或null条件失配时，保原载体、明确未检出与独立来源证据，不由cluster命中批准音频真实性或法律来源。

<!-- source-family:SF-2025-ARXIV-2510-21115 -->
```

```markdown
- `SF-2025-ARXIV-2510-21115`：Daily2025-10-28补Oct27；R10首次必要/R24实际gap，2+2+2=6/安全深入。仅retokenization与检测单位对齐，保over-key/独立null条件和全费；未核实现/复现，完整PRE/SAVE/自读/solePOST据本日实际层。
```

## I29 PLATFORM-SECURITY / SIC

文件：`books/part-06-ai-infrastructure/72-security.md`；task-conditioned清理段后、分段定位前。

```markdown
重写也可先用固定探针检验指令是否容易穿过，而不每轮依据“已干净”提前退出：在tool output加入已知canary，执行固定次数stateless、无条件rewrite；探针仍在就halt，随后再作全文或可选chunk检测，移除placeholder后才交Agent。[SIC的受限协议](https://arxiv.org/html/2510.21057v1#S3)不让canary消失代替所有原payload已消除，静态ASR为零也不抵消强自适应攻击仍成功的反侧。改写可能损害任务，DoS不在该威胁模型，已授权工具effect仍需独立控制。R轮rewrite、一次检测和k个chunk等额外调用、全部失败/语义回归都付费；探针、语义或净收益失配时，保原证据、可信解析/隔离与有限拒绝，不由无状态或固定轮数签发强安全边界。

<!-- source-family:SF-2025-ARXIV-2510-21057 -->
```

```markdown
- `SF-2025-ARXIV-2510-21057`：Daily2025-10-28补Oct27；R9首次必要/R24实际gap，2+2+2=6/安全深入。仅固定stateless rewrite/canary/halt与effect授权分责，保adaptive15%/DoS未测/语义损伤和R+1+k费；未运行攻击/实现/复现，完整PRE/SAVE/自读/solePOST据本日实际层。
```

## I30 PLATFORM-EVALUATION-SYSTEM / VeriGray

文件：`books/part-06-ai-infrastructure/66-evaluation-system.md`；RAG来源定位段后、综合多文档逐claim前。

```markdown
来源忠实与外部真实还须分两轴：source没支持的句子，可能可由外部证据核实，也可能错误；语言歧义、无事实与证据不足不能默默压成同一hallucination标签。[VeriGray的受限标注](https://arxiv.org/html/2510.21118v1#S4)将source-only、Out-Dependent、NotSure/NoFact分开，二元评价删去后两类后，分母已不再是全部生成句子。外部搜索和人审是有限证据，不是全球事实oracle，来源支持本身也不认证world truth。全部外证检索、URL/判据留存、歧义仲裁和独立标注均付费；证据或定义不明时，保两轴结果与Unknown人口，不由较低二元致幻率批准全流量事实正确。

<!-- source-family:SF-2025-ARXIV-2510-21118 -->
```

```markdown
- `SF-2025-ARXIV-2510-21118`：Daily2025-10-28补Oct27；R10首次必要/R24实际gap，2+2+2=6/评价深入。exact-v1 412summaries/2044sentences/OutDependent8%，不混v4；仅source faithfulness/world truth/拒判分母，未核实现/复现，完整PRE/SAVE/自读/solePOST据本日实际层。
```

## I31 PLATFORM-SECURITY / AgentBound

文件：`books/part-06-ai-infrastructure/72-security.md`；执行环境containment例后、Training/Evaluation Environment前。

```markdown
工具权限还可从资源提案编译成实际约束：分析依赖/代码提出mount、env与egress manifest，经用户审核后，由Docker和iptables实施，而不让模型自述最小权限即获得执行权。[AgentBound的受限路径](https://arxiv.org/html/2510.21236v1#S3)中的manifest仍需人工核，域名解析后的IP白名单不等HTTP操作/账号/参数授权，安装依赖发生在网络限制前也留下另一阶段。允许端点上的参数劫持、SQL或prompt注入仍可发生，不能从资源隔离推导全部MCP工具安全。依赖分析、安装、manifest审核、隔离运行与真实副作用/回归均付费；资源提案、解析或操作权限不合时，保较窄可信manifest、明确拒绝/人工审批与独立执行环境，不由schema或容器存在批准真实effect。

<!-- source-family:SF-2025-ARXIV-2510-21236 -->
```

```markdown
- `SF-2025-ARXIV-2510-21236`：Daily2025-10-28补Oct27；R12首次必要/R24实际gap，2+2+2=6/安全深入。仅审核manifest→OS资源权能分责，保安装阶段/IP非语义/允许端点攻击与全费；未部署/核实现/复现，完整PRE/SAVE/自读/solePOST据本日实际层。
```

## I32 PLATFORM-EVALUATION-SYSTEM / CorrDim

文件：`books/part-06-ai-infrastructure/66-evaluation-system.md`；R28后仅改位置：在“从目标到证据”内，几何调节已有score完整段/marker后、ProtoBias语义与熟悉度负控段前。完整新邻接见`REPAIR_BOOKS_CONTEXT32_20261029.json`，正文/marker/本人注逐字不变；context5原位保留为历史，不再采用。

```markdown
输出结构也可从完整next-token log-prob轨迹读取，而不只取已选token的surprisal：计算向量间Euclidean recurrence integral在若干尺度的斜率，得到相关维数proxy。[CorrDim的受限实验](https://arxiv.org/html/2510.21258v1#S3)观察到局部退化/异常相关，却不构成Takens对LLM的重构证明，低维或特定人名case也不是已校准事实风险。Scorer、tokenizer/词表、context长度、完整logits、距离精度与尺度须共同保存；词表/低精度化不能静默继承原分数。原方法二次pair数量与词表维运算、驻留和独立校准均计费，黑盒API未必提供接口。支持、尺度或费用不合时，保简单概率/语义指标和独立真标签，不由几何维数签发知识、可靠性或通用低成本检测。

<!-- source-family:SF-2025-ARXIV-2510-21258 -->
```

```markdown
- `SF-2025-ARXIV-2510-21258`：Daily2025-10-28补Oct27；R12首次必要/R24实际gap，2+2+2=6。仅全logprob recurrence读出与校准资格，保O(N²)/词表算量、FP32距离及SEP有限case；未核实现/复现，完整PRE/SAVE/自读/solePOST据本日实际层。
```

## I33 PLATFORM-EVALUATION-SYSTEM / Gibberish speech

文件：`books/part-06-ai-infrastructure/66-evaluation-system.md`；Metric条件PPL段后、语音judge维度段前。

```markdown
语音还可能听起来流畅，却没有合法词/音素内容；强ASR会把这类波形“修复”成正常文字，使后接语言模型失去对原声gibberish的敏感性。[受限SpeechLM测量](https://arxiv.org/html/2510.21317v1#S2)因此把原波形phonotactic validity、SpeechLM分数、转录文本与reference内容保持分账，后者不能由低PPL代替。局部LRS3/生成器与噪声人口、十人125文件校准不授所有语言或流式部署，深层score也未清分全部异常。原声留存、各评分器/转录、人审与独立内容回归均付费；ASR修复、语言或模型支持失配时，回听原声、保明确Unknown与参考对照，不由自然音色或正常转写批准真实内容。

<!-- source-family:SF-2025-ARXIV-2510-21317 -->
```

```markdown
- `SF-2025-ARXIV-2510-21317`：Daily2025-10-28补Oct27；R12首次必要/R24实际gap，2+2+2=6。仅原声gibberish/ASR修复测量链，保受测人口与全费，不采新语音生成或安全保证；未听全部波形/核实现/复现，完整PRE/SAVE/自读/solePOST据本日实际层。
```

## I34 PLATFORM-EVALUATION-SYSTEM / InterpDetect

文件：`books/part-06-ai-infrastructure/66-evaluation-system.md`；Activation Oracle完整首段后、人读sensor段前。

```markdown
内部feature sensor还要说明它属于谁：让小proxy重读另一模型的输出，再以其attention/FFN特征训练监督分类器，读到的是proxy对文本的反应，不是目标模型真实内部状态。[InterpDetect的受限分支](https://arxiv.org/html/2510.21538v1#S3)在有限FinQA/RagBench人口验证这条路径，ECS/PKS相关不认证目标FFN唯一致幻因果；弱span标签与any-span聚合为whole-response还会改变误报人口。全部head/FFN/vocab投影、弱标签筛选、分类训练和跨model独立校准均计费，不能称无标签或免费黑盒解释。Proxy、任务或标签支持失配时，保外部证据/直接输出指标与Unknown，不由小模型读出批准target内在知识或任意迁移。

<!-- source-family:SF-2025-ARXIV-2510-21538 -->
```

```markdown
- `SF-2025-ARXIV-2510-21538`：Daily2025-10-28补Oct27；R12首次必要/R24实际gap，2+1+2=5。仅proxy sensor/target-state权限、弱span标签和聚合分母，保copyinghead未复现/投影全费；未核实现/复现，完整PRE/SAVE/自读/solePOST据本日实际层。
```

## I35 PLATFORM-SECURITY / Private analytics

文件：`books/part-06-ai-infrastructure/72-security.md`；usage analytics完整段后、公开语料候选前。

```markdown
私有分析也可先隔离原始每份upload的LLM处理，再让DP控制聚合发布，而不先把原始内容交普通服务：以attested binary/config向KMS取得解密权，每upload运行后清内部状态，并用rollback-protected RAFT状态共同约束隐私预算与release。[受限private analytics系统](https://arxiv.org/html/2510.21684v1#S3)的当前DP单位是upload，不是一个用户一周；同人多次上传、Sybil、TEE侧信道与硬件信任仍须另核。TTL只是best-effort，未来H100/TDX或user-week不能倒授当前Gemma/SEV-SNP路径。Attestation、密钥/状态治理、全部隔离推理、DP参数选择与失败恢复都付费；预算持久性、信任或邻接单位未闭时，保较窄发布、原DP聚合与拒绝解密/发布，不由TEE名称批准所有隐私泄漏已消除。

<!-- source-family:SF-2025-ARXIV-2510-21684 -->
```

```markdown
- `SF-2025-ARXIV-2510-21684`：Daily2025-10-28补Oct27；R12首次必要/R24实际gap，2+2+3=7/安全系统深入。仅upload隔离预处理→attested KMS→rollback预算→DP release，保当前upload单位/TTL/Sybil/侧信道和全费；作者部署非本项目部署，未核实现/复现，完整PRE/SAVE/自读/solePOST据本日实际层。
```

## I36 MULTIMODAL-REPRESENTATION / Controlled MI

文件：`books/part-03-multimodal-world-models/23-multimodal-representation.md`；配对signal/nuisance段后、feature模长前。

```markdown
要检验架构能否使用跨模态信息，还可先构造总MI可控、feature布局另可调的人口：从Gaussian prototype经线性mixing得到可算covariance，再为各模态施加连续双射flow，在理论条件下保持MI。[受限controlled-MI构造](https://arxiv.org/html/2510.21686v1#S3)把信息总量与它分布在哪些feature位置分开，非奇异/有限MI及真正双射是前提；数值ODE、量化pixels或有损映射不自动保持精确等式。可算MI也不证明现实语义相关或grounding，类别proxy不等真实传感器。全部构造、flow/solver、数值校验与下游独立任务评价均付费；双射、布局或任务支持失配时，保明确解析小域、原配对数据和独立语义评价，不由信息量可控批准模型已理解或跨现实模态普适。

<!-- source-family:SF-2025-ARXIV-2510-21686 -->
```

```markdown
- `SF-2025-ARXIV-2510-21686`：Daily2025-10-28补Oct27；R12首次必要/R24实际gap，2+2+2=6/理论条件已核。仅Gaussian→mixing→bijective flow的MI/feature布局分责，不扩astrophysics；保数值/量化不自动等价与全费，未核实现/复现，完整PRE/SAVE/自读/solePOST据本日实际层。
```

## 作者整体自读

R24十八项实际比较已整体消费；其中八项既有覆盖不写书。本十稿全文/marker/本人注已自读，context5全直接两侧和I27/I28有序新邻接另读；不预签任何SAVE或POST，仍有W17实际比较及日报待办。
