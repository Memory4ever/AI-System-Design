# 本日新增证据（持续完成，不是DAY）

## [Self-Jailbreaking](https://arxiv.org/html/2510.20956v1)

2+2+3=7。writer实际读v1§3–6、方向提取/干预及安全混训必要实验；sole reader R6直接反侧已消费。313条StrongReject、500 thinking-token、答案harmfulness阈值2的ASR与CoT自越狱标签分开；GPT-5-2025-08-07以250对/约8300句人工校准。模型可在全有害题人口中正确识别危险却仍服从，不等混合safe/unsafe真实判别率。机制方向主要来自Qwen base在100 XSTest和5组contrastive prompts，102个自越狱实例上的projection/steering仅提供局部干预证据，不是内部道德真值或所有失败的唯一解释。多任务混入从base重新训练，不是对现有reasoning模型补50条即可通用修复；GPQA/MATH用8000 thinking-token，不能与安全500预算混成同一评估。约37%安全生成仍有自越狱CoT，输出拒答不等内部路径消失；主要英文、未测跨语言。未运行训练/steering，硬件/precision/线上SLO未披露，本文不采用部署性能。拟长期增量是把危险识别、理由生成、最终服从三个资格分开，普通安全混训正文尚未具体承载此边界，提Ch31窄段PRE。

## [ColMAD v1](https://arxiv.org/html/2510.20963v1)

2+1+2=5。原v1题名为 `Towards Scalable Oversight with Collaborative Multi-Agent Debate in Error Detection`。实际§2.1–2.3/§4.1–4.3；不采用current v2题摘新增的consensus-seeking概括。竞争协议中的说服可误导judge；v1协作协议组合quote精确匹配、自审和confidence，理论依赖理想Bayes judge、有限LLR和条件信息增量，不是任意LLM策略均衡保证。三类客观错误检测，源回答GPT-4-0613/Llama2，judge默认等于debater1，温度0、通常两轮；不称完全异源独立核验。F2重recall，与F1分开；结果up to4%相对single-agent、up to19%相对competitive，不借v2 10pp，也不把prompt组合归因单一目标。盲目采纳较弱peer同样可退化，judge位置影响结果，同预算/所有调用费用未完整对齐。Ch82 Peer/Debate及DebateQD具体已有个体胜辩与团队judge正确目标之分、同源非独立证据和单Agent/外部verifier退路，原文具体案例保Daily，拟已有覆盖而不追加理论摘要。writer已读该完整两侧，reader复核最终处置待后到。

## [Reasoning's Razor](https://arxiv.org/html/2510.21049v1)

2+2+3=7。实际§3.1、§3.3–3.6/Limitations；reader R5反侧消费。ThinkOn/Off是相同任务中是否生成reasoning的干预，LRM以empty thinking tags压制不等无损本征开关。保安全prompt/response与RAG hallucination三个标签人口；0.5阈值accuracy/GFPR和按1%FPR选阈值的TPR不是同一操作点。reasoning可改善accuracy却加重错误高分尾部、降低低FPR recall；不泛称所有reasoning均差，CovidQA的QwQ对照反而ThinkOn70.6/Off26.6。口述confidence离散量化可妨碍细阈值，与token读出不是同一仪器；equal-weight ensemble要两路调用，阈值在这些受测人口上的ROC选点不授独立部署FPR。研究仅有限模型/任务，固定prompt/解码/context，未穷尽工具或反思机制；本文不采用速度、硬件或SLO数字。拟Ch66新增“reasoning模式也是score producer identity、平均accuracy与低FPR尾部可反向”的具体分支，不以泛泛阈值原则称覆盖。

## [PBS-Attn](https://arxiv.org/html/2510.21270v1)

2+1+2=5。实际§3.1–3.4/§4.1–4.3及C必要overhead，reader R5反侧消费。Q置换后逆置换、K/V共同置换的恒等只属于未裁剪合法attention；全局置换可能破坏因果结构。分段内按last-query-block估得的重要性排序key，保跨段因果与段内原index mask；这不是改变位置坐标或以新普通三角mask代替原可见性。B128/S256/threshold0.9，Triton permuted-FA，H10080GB；Llama3.1-8B/Qwen2.5-7B-1M、LongBench/v2。只替prefill而decode不变；2.75x为256K TTFT且TP2，512K为TP8，batch/concurrency/precision/SLO未在已采用段披露为Not Disclosed。key排序优于query排序的成本受GQA头数影响，大段聚类较好也增加不可跳过的对角范围；128K重排4%相对block attention、1.3%相对full FA仅该条件。没有执行kernel或复现；质量近dense不等无损。Ch22已有selection/layout/cause分责但没有“先重排分散重要key再按块跳过”的具体可执行分支，拟一段PRE。

## [ParaRNN](https://arxiv.org/html/2510.21450v1)

2+2+3=7。实际§2/2.1/3/4/5.1–5.2、B/C.1关键配置与D.2硬件层次，reader R6反侧消费。非线性递归联立成方程，Newton线性化后解block bi-diagonal系统，backward本身为线性递归可一次parallel reduction；不是所有RNN天然有实用小迭代上界。L步理论终止会抹平并行收益，三次收敛仅作者所测cell成立。dense Jacobian内存O(L d_h²)、乘法O(d_h³)迫使修改GRU为diagonal/LSTM为diagonal-block，损失cell内feature mixing后靠后续MLP补；不称原dense GRU/LSTM无损自动并行。665x只对naive sequential；A100计时CUDA Events20warmups/100次取min，1B生成另timeit五次min，不是SLO。Mamba full-cell对照去gate/conv，blockdiag reducer可能更慢。7B SlimPajama去Books3、Chinchilla tokens，8H100节点/bf16 weights、fp32 gradient/reduction；调LR/WD以SPJ test PPL选点不称完全未参与选择的test，synthetic三seed取best。ParaGRU/ParaLSTM的7B PPL仍高于Mamba2，不能宣称普遍质量优势。HTML的日期宏显示2026、code metadata指内部链接，均不作2025公开日或代码可得性证据；精确arXiv-v1/DOI联合界独立保存，不访问内部code。未核代码或复现。拟Ch22新增“并行训练的约束可从线性性换为可快速收敛/结构化Jacobian”，保原显式history/线性scan分支。

## [MiniMax M2发布](https://www.minimax.io/blog/minimax-m2-en-1748600000)

1+2+1=4，因具体兼容性契约变化定点深入，不用低分免核。writer实际读官方发布正文及Oct27历史README commit `e304e33a34c9f403d2d5bb3e1a7d900ebcbda87c` 的Highlights/全部benchmark注/activation解释/inference尾部，reader R2 current-card反侧只在与historical blob一致的必要段复用。模型230B total/10B active不等只需10B权重内存；Blog明确关键算法后续披露。M2 interleaved thinking要求历史assistant的think原样回传，是此版本的输入兼容约束，不是所有模型都必须保留CoT的通用建议；Blog top_k20、历史card40均保原版本，不拼验证recipe。各benchmark有不同scaffold/step/样本/外部报告星号，8%价/2x速度缺同硬件/precision/batch/concurrency/长度/SLO配置，不授MoE单因果、普适省钱或已部署成功。只报告具体发布与兼容事实，不改变长期知识的通用机制；不因主题相似标已有覆盖，不新增Books段。

## [CodeAdapt](https://arxiv.org/html/2510.20909v1)

拟2+1+2=5，标准核心已读§3/§4.1/4.3–4.5/Limitations。CodeAct循环之外，新增GFL用一题的正确轨迹作另一题one-shot，按跨题utility选择最多每题一例，而非只挑本题答对示例；M6/N5/K2制备90轨迹/任务，verifier与示例选择不等无监督或免预算。最多4分钟/16k output/10turn，8任务/4模型对，Gemini对应比较跨2.0/2.5版本，不能称严格同底座推理开关或有因果隔离的训练成本差。GFL接普通CoT的消融仍较弱，AIME依然可输reasoning model，150trace/200的analysis计数不一致不据此泛化内部元认知。输出token节省不是总input/tool/prompt生成费；未运行代码。拟采用只“示例自己的正确性与其跨题教学效用分开”，待reader准入/Books比较。

## [Clustered missing-response estimation](https://arxiv.org/html/2510.20928v1)

拟2+2+2=6，标准及必要条件已读§2/3/3.1/§4开头/§5–7；不宣称全附录证明核验。每条message权重相等的均值与每用户/树权重相等不同；DR项为`R(Y-mu)/pi+mu`，MAR/positivity、独立clusters及nuisance-rate/cluster-size条件不可省。cluster内相关使方差/rate不是朴素iid，方差按cluster聚合influence而非将所有messages独立bootstrap。sequential设置还须纳历史进缺失模型，未知missing-not-at-random不被DR自动修复。OpenAssistant9808树/81937messages的缺失用logistic模拟，不是实测生产缺失机制；近零propensity不稳定，未标注新模型的transport是未来工作。本文采用有限统计接口与条件，不据sim95%coverage授部署保证，硬件/SLO对该统计命题不适用；待reader及Ch66实际覆盖比较。

## [GLVQ](https://arxiv.org/html/2510.20984v1)

拟2+1+2=5；已读§3/3.1–3.4/§4.1配置、4.4–4.5/Limitations。固定bit allocation后分别学习group lattice basis与companding，rounding整数索引迭代刷新；SDBA明确借用Slim-LLM，不把全部组成均算新机制。固定列group与侧信息/反companding须计成本；小group精度较好但metadata较大，大group相反。A100质量、4090 batch1/2bit吞吐不同评价，混合精度PPL改善伴82.0低于QTIP105.2TOK/s，不授统一提速。原文称7B/4bit payload1.1GB与按7e9*4/8=3.5e9bytes的量纲不符，且2bit70B的权重净码约35GB大于4090显存，原段未给offload条件；这些数字不正面采用，不代作者补方案。初筛后存在具体OpenReview更早全文线索，globalfirst尚待恢复，不先列确定本窗候选或进Books；已读支持保留，不将不确定日期改零。

## [Distilled Decoding 2](https://arxiv.org/html/2510.21003v1)

拟2+1+2=5；实际§3.1–3.3/5.1/5.4–5.5/6/7。以VQ token概率定义embedding空间平滑conditional score，在generator当前clean prefix上逐位置蒸馏；另训fake conditional guidance、交替更新，stop-gradient前缀不等generator全联合梯度直接等价。初始化将teacher头换MLP并GTS调优，两边初始化欠佳可崩；不说随机student即可。ImageNet256类条件、VAR10与LlamaGen256步分别压1步，不是文本AR或T2I已验证。8A800训练计费，one-step仍有FID差，†baseline由DD1引用、*更长训练分开；不抄摘要/正文各模型混合的速度/FID数作统一结果。continuous AR与大T2I是未来方向。具体OpenReview73EcEGo6LQ全文命中/日级早稿权限待恢复，不先授当窗全球first；core不因日期问题抹掉，也不因此继续全附件。

## [Confidence-gated CoT](https://arxiv.org/html/2510.21007v1)

拟2+1+2=5，标准核心实际§3–4/5.1/6/7。先direct答再按score触发CoT，P(True)另一次调用，和partial-reasoning early exit不同；GPT-OSS的direct prompting/effort控制不等Qwen原生同开关。七短答/多选任务、Qwen3 8B/32B与GPTOSS20B，random解析baseline和oracle上界分开；oracle假定direct错才CoT，不是所有CoT都能修复。offline全分布percentile不是online预算保证，后者前20warmupdirect/10顺序重复；10%calibration/epsilon1%/100次MonteCarlo选阈值是目标人口的模拟，不授未知流稳定。Qwen8B整体可能不胜random仍可有局部低成本阈值，更多CoT可过度；计算direct、额外score、CoT与校准均计费，节省reasoning份额不等墙时/线上SLO。待reader准入与实际Books比较，未复现。

## [ZO-FC](https://arxiv.org/html/2510.21019v1)

拟2+1+2=5，实际§3/4.1–4.2/5.1–5.3/6。直接FO→ZO替换多种CL方法失败，冻结backbone的adapter用ZO、最后classifier用FO，将表示稳定与classifier可塑性分工；不把“ZO总不遗忘”当定律。原§3 Taylor省一次项需old-loss驻点/小更新等条件，trace变小也不无条件推出lambda_max下降，Eq7链不采用为一般证明。ViTB16/ImageNet21k、rank5前5blocks、CIFAR100/ImageNetR/DomainNet；Q4/epsilon.001与FO/ZO不同schedule，ZO双forward/queries都付费，强FO基线仍可更高。on-device实际训练与更难fine-grainedCL是未来工作，未运行实现。拟保优化器按参数角色分配及实证负侧，待reader及Ch30/28具体论证比较。

## [xMem](https://arxiv.org/html/2510.21048v1)

拟2+2+2=6，实际§3.1–3.4/§4.1环境与大模型范围/§6.1–6.4。CPU短训练trace不是直接GPU使用量：识别参数/grad/optimizer生命周期，将grad清除对齐zero_grad，重排后交两级round/split/coalesce/cache simulator测segment峰值，不只加tensor大小。主要25模型/约5209runs跨两个小GPU，baseline因依赖用不同PyTorch/CUDA容器，不能将全部差额唯一归因CPU方法。A10040GB大模型仅1.5B/3B/4B且只有DNNMem可比、样本不足不报PEF。CPU/GPU不同workspace/operator/backend可破坏映射，CPU/RAM/profiler大量数据及顺序分析有成本；singleGPU才是当前scope，distributed/allreduce模拟只是方向，CPU未支持FP16则原profile也昂贵，FP8不是现成功能。未核实现/生产调度，MCP是memory conservation potential，不是实际已部署资源节约。待reader及实际memory-owner比较。

## [DR-IKE](https://arxiv.org/html/2510.21059v1)

拟1+1+2=4，关闭所需身份/日期/局部机制已核，另已读§4.1–4.3/§5.1/6必要明确适用限制。新增在既有Copy/Update/Retain prompting里用REINFORCE-trained线性head排序Retain，并以单threshold控制例数；是局部知识编辑实现变体，不将常规utility检索/阈值本身重记基础原则。CounterFact300train/100eval、Llama/Mistral/Qwen、L4，依赖同源相似paraphrase/neighborhood与可得训练编辑标签；阈值适应依赖reward反馈，不能冒充黑盒部署时可见真值/所有query都自适应。原步骤叙述的逐次采样/降序选择差别未核统一recipe，不采用可执行细节。仅报告局部接口，不改长期Books；待reader闭合准入/处置，不因省时间或已有覆盖降分。

## [Shortest-answer selection](https://arxiv.org/html/2510.21067v1)

拟2+1+2=5，标准核心实际§1–3。parallel5解中选最短，能在无可比较最终答案的coding任务替代self-consistency，不等所有短解较真；三model/400题AIME与LiveCodeBenchv5、temperature1。两解中已正确的长短对、uncertainty词密度与modal-length阈值支持相关现象，不识别内部自信或临界相变。Early stop优势需并发执行且以最先完成等于最短的适用条件核调度；离线五解本身全生成计费，不能仅按留下的短解宣称省全部tokens/墙时。未运行推理，hardware/precision/concurrency/SLO未披露，不作生产性能保证。待reader及sampling-owner比较。

## 窗外恢复：[SRPPO](https://arxiv.org/html/2510.21090v1)

未作为当窗候选评分。原件COLM2025信号后primary OpenReview作者搜索已显示同名同作者Published08Jul2025，非created；最迟当时已有正文事件，不以Oct27 arXiv登记当first-public。已读§3/4.1/4.2/5仅保恢复：reward是冻结SFT/base log-policy比，PPO另采new prompts，不是免示范/免额外forward/独立truth reward；tokenwise变体有length degeneration、overlap与SFT质量影响外推。准确首公开及更早版本恢复属于真实归属日，不在本窗扩查或写Books。API2精确title403失败保留，source UI发布字段的原件恢复仍在本轮定点工作中。

## [PhysVLM-AVR](https://arxiv.org/html/2510.21111v1)

2+2+2=6，writer首必要v1§3–4与限制（txt80–167/310–329）。检测当前证据不足和执行补充观察分开，CLEVR-AVR Genesis三类各10场景的IGR是揭示问题相关物体的simulator oracle，不是完整互信息最优规划器。152k AVR由100k Gemini caption、50k DeepSeek推理和2k Core组成，Core源自640真实UMI轨迹；不是152k真实机器人执行。Qwen2.5-3B/SigLIP、混合数据分阶段训练与全部teacher费保留；删Core和删CoT消融不单独识别caption因果。90.5%不足识别不等最终正确，正文39.1/表39.7差额不合并成精确总数；OpenEQA judge/RoboVQA BLEU不授现实机器人闭环安全或最优动作。拟采用信息不足识别与主动补观察分责，待reader/Ch26实际论证比较。

## [NoisyGRPO](https://arxiv.org/html/2510.21122v1)

2+2+2=6，v1§3–4/5与必要附录配置（txt114–208/328–340/646–694）。带噪图rollout、clean图update与Gaussian prior/semantic reward融合改变训练人口，不将噪声大小当客观CoT质量。Eq1分母是clean old-policy而非实际noisy行为policy，融合不自动补齐importance correction，故不采用无偏policy-gradient推论；零reward方差下印刷归一式未闭，不补成执行recipe。13k MMRLHF/Qwen2.5VL3B7B/G4/8A100，SBERT语义阈值.6/格式及噪声先验均为代理。无validation，全部hyperparameters按MMStar选，不当独立test；3B额外walltime/GPUh、7B峰值显存反增，不能称全部零额外成本。coarse perception下噪声先验可能失配，采用限观测扰动/训练policy身份分账，待reader/Ch33或Ch31实际owner比较。

## [Blockwise Flow Matching](https://arxiv.org/html/2510.21167v1)

2+1+2=5，v1§3/4必要设置与限制（txt88–158/1010–1052/1218–1225）。t从noise到data均匀分6段，各独立小velocity network，只跑当前段；不是sequence block或KV复用。DINOv2语义特征与第二阶段FRN residual近似另有预训练/训练费，跨段共用基点不等完全同velocity。组件表100k训练/250 Euler无CFG与最终246NFE（每段41）分开。ImageNet256条件生成/50k样本，A100 batch32时SF约9.4%、RA约63%runtime变化；摘要2.1–4.9倍是FLOPs而非相同墙时。总参数增多、边界拼接/feature成本与单一模态限制保留，T2I/video未来，不以venue单独反推早稿日。待reader/Ch24具体现有分段/特征复用论证比较。

## [NuSA-CL](https://arxiv.org/html/2510.21175v1)

2+1+2=5，v1§3/4配置/限制必要（txt101–134/160–168/724–729）。每任务SVD并按能量截断，冻结tail bases Un/Vn、只训M使delta=Un M VnT，merge后下任务重算；与只在初始化低秩然后可漂移不同。低能量近似尾空间不是数学零空间，正交主参数空间不证明旧输入输出不变，unseen activation可投尾部。CLIP ViTB16/11MTIL与CIFAR100 10/20/50任务，95%或5shot99%能量、主rmax128与CIFAR附录256不混；重实现baselines预算/encoder控制与fullFT不同算力分开。固定参数/replay-free不是功能记忆无代价，SVD/基重算、长任务序列与LLM推广未证。待reader/Ch30实际覆盖比较，不因vision小模型排除。

## [PLAN](https://arxiv.org/html/2510.21188v1)

2+1+2=5，v1§3/4与限制必要（txt97–151/163–188/486–493）。每任务冻结互异标准输入坐标A、只训B；对未分配坐标施一阶近似minmax扰动并按最后50步敏感性分配下一A，不是仅普通正交LoRA初始化。有限可分配basis会耗尽，不授无限CL容量。原文Ai^T Aj=0对不同行标准basis一般不成立（行正交应Ai Aj^T）；即使参数Frobenius正交也不保任意旧输入不受扰，Eq12求和上界S/s未闭，不代修执行recipe。ViTB16/ImageNet21k+1k或iBOT，三视觉CL数据、K/V LoRA，rho.01，缺显式正向backward transfer与其他架构未证。仅采用未来坐标配置/当前鲁棒更新分账，待reader/Ch30实际论证比较。

## [UDCG](https://arxiv.org/html/2510.21440v1)

2+2+2=6，v1§3–7/Limitations必要（txt112–187/563–645）。单passage的non-abstention概率乘相关性正负标签，再学位置权重或用无位置gamma，改变“IR relevance足以预测RAG”的测量接口；DE分数明确继承既有工作。假设相关passage不会让模型答错未获普遍证明，non-abstain不是正确概率；learned版须每k重训，无位置版也要选gamma。六LLM/五英文QA，Claude3.7标相关、Gemini2判语义，单passage需logits，黑盒API不适用；NQ训练1200/test500，评价context人为50%有相关证据，其他四域迁移不是生产风险。top25选5的oracle重排不等已部署retriever，少distractor效果/消融支持受限相关性，不授因果完整拆分或硬性能节约；原复杂度论证忽略cache/实际实现，不用于墙时。全部标注、概率、重排/生成费保留，待Ch76实际论证与reader。

## [PhysWorld](https://arxiv.org/html/2510.21447v1)

2+1+2=5，v1§3.1–3.3/4.1/4.3/5必要（txt92–205/292–303/411–416）。由短视频校准MPM twin，再按PartField语义相似协方差/Nystrom扰动粒子物性，比无结构随机扰动多保同part相关；合成500 episodes/scene训GNN，冻结GNN再用真实观测调物性。不是从视频唯一识别真实物性或GNN严格遵守守恒。1–10秒单场景视频按帧7:3切分，100–150nodes/7messagepasses；MPM每帧400substeps、反传仅末10+clip，未见完整hardware/precision/SLO。未见动作GT的future以美学/平滑/主体一致代理，不认证物理真值；新动作/长rollout误差与sim-to-real仍在。采用物性扰动结构与模拟/快速模型校准分责，不沿用全部规划/机器人实效，待Ch25实际覆盖。

## [UTR](https://arxiv.org/html/2510.21448v1)

1+1+2=4，关闭层已读题摘与§3.2–3.4必要（txt120–180）。将RTG embedding/current state/previous action拼为单token，另用已有causal gated depthwise conv，降低局部DecisionTransformer序列开销；这是固定offline-control接口的实现变体，不把一般concat/短context局部性重复计基础新原理。简化linear predictor/相同norm/iid/协方差假设的upper-bound比较不等实际非线性Transformer泛化更好，sigmoid也无任意大输入绝不饱和保证；不采用其普遍理论或实时声明。确定当窗仅报告局部接口，未向LLM/VLA无根据推广，不因Books/工时改分；待reader校准。

## [MRO](https://arxiv.org/html/2510.21473v1)

2+1+2=5，v1§4.1–4.3/5.1–5.4/A.1/C.1/C.3必要（txt137–245/667–669/850–862/1019）。对DLM并发补token再逐token重mask验证、AR PPL与终局任务reward，并按denoise steps分组降打分频率；不是直接改掉条件独立采样或证明全部reasoning相关因果。test-time四分支选择用majority pseudo-gold，RS/RL另有真实任务标签；validation每50步选best，LLaDA8B/s1/DeepScaleR+Countdown/Sudoku。额外verify/AR scorer/beam/训练与原分组超参均付费，较少denoise不等全调用省时；RL中去PPL的MRO-v4可更好。§4.3非负中间reward直接写成potential difference与无条件均值不变/方差必增未闭，不采用这些普遍保证或可执行方程recipe；仅采用多种一致性proxy/终局真值/打分频率分账，待Ch24/31 owner与reader。

## [Foresight Guidance](https://arxiv.org/html/2510.21512v1)

2+2+2=6，v1§3.1–3.2/4.1/ablation/Limitations（txt128–190/419–423/708/2035–2037）。将conditional guidance分成校准与unconditional采样，早期较长一致区间+多次fixedpoint，而非仅增guidance scale。golden path为经验定义，local contraction需谱半径<1/合适初点；manifold资格实际用小步经验，非已严格满足。SDXL等图像模型/DrawBench/Pick-a-Pic/Geneval/Parti，NFE50/150预算不可混，CLIP/偏好/aesthetic均proxy；过大区间或过多迭代可退化/离流形，全部双路网络/重复调用计费，不授全局收敛/所有scheduler/净Serving速度。待Ch24实际比较与reader。

## [Code-ensemble popularity trap](https://arxiv.org/html/2510.21513v1)

2+1+2=5，v1§3.3–3.9/4.2.1–4.2.5/5（txt255–286/333–398/765–812/838–866）。模型互补的oracle候选池不等有限10条输出可实现收益；按代码相似性共识会选共同错误，greedy diversity与token-confidence排序是不同读出。十model五family各10beam候选，HumanEvalJava164/Defects4J525单函数/LiveCodeBench454，最后只选10但全部100生成及两两评分/各模型logprob都付费。plausible=编译+tests非真实正确，旧benchmark污染未排尽；diversity在LCB某组还比naive少9，不能宣称永远胜。byte归一不自动校准跨modelconfidence，闭源无logit不可用。待Ch82或Ch20实际覆盖与reader。

## [HeadPursuit](https://arxiv.org/html/2510.21518v1)

2+1+2=5，安全干预受影响深入；v1§3/4.1–4.2/5.1–5.2/Limitations（txt98–119/147–166/205–225/260–268）。SOMP用固定unembedding字典多样本稀疏拟合head输出、按解释方差选head，与单样本LogitLens不同；sign inversion/放大还改变后续间接贡献，不证明唯一存储concept。Mistral7B/TriviaQA训练与test分离、Llama抽RTP/TET词、RoBERTa毒性与heldout词双指标；十组同layer/count且排除所选头的random，有限H10080GB。MLLM分类/Caption加词伴CIDEr损失，alpha5为质量权衡，不是无副作用；线性/字典覆盖偏差保留。降低词/分类器毒性不授防越狱或全部安全，不核实现/复现，待Ch15实际覆盖与reader。

## [Co-Sight](https://arxiv.org/html/2510.21557v1)

2+2+2=6，v1§3.1–3.2/4.1–4.4/5.1（txt97–225/227–248/280–289/328–331）。对依赖节点剪枝、重复中间量anchor、仅分歧处审计，再汇总tool/notes/facts；这是选择验证位置的执行分支，不仅多agent组合。**同base不同temperature的一致可能共同错**，重复量升“verified”不认证truth，facts URL/一致性不是独立证据；无分歧错误可完全漏审。成本按冲突数只针对后续audits，前置全trace生成/比较/解析/工具都付费，论文未给足硬件/precision/token/预算SLO，GAIA/HLE跨系统榜不可归因同成本。Gemini2.5Pro控制与SimpleQA component ablation支持局部组合，不授安全关键部署；摘要93.8与ablation91.2人口分开。待Ch82实际差额与reader。

## [Human-hand VLA pretraining](https://arxiv.org/html/2510.21571v1)

2+2+2=6，v1§3/4/5.2–5.3/6（txt153–224/244–253/296–310/313–340/455–459）。相机/手3D重建后在world wrist-speed minima切原子动作、轨迹overlay给GPT4.1，1M/26M frames是推断标签不是真实机器人commands；重建/MLLM噪声保留。PaliGemma2-3B+DiT，102D相对手动作+valid masks，causal action-denoise防尾padding泄前，映射robot关节仍须1.2k teleop finetune。8H100预训2日/微调8小时，四桌面任务主要单手；47环境396物体的距离与23人30场景rank不是闭环成功率，细粒度切/overlay消融350k子集不等全部因果。可保数据粒度/坐标/动作资格分责，双手长horizon/多视角触觉未来；待Ch26具体owner与reader。

## [Foley Control](https://arxiv.org/html/2510.21581v1)

1+1+2=4，题摘/§2.1及§3.1–3.3必要（txt55–145）。冻结V-JEPA2与StableAudioOpen，在既有text cross-attention后插video cross-attention/轻量MLP与pool，属于已知冻结骨干跨模态adapter的一项具体audio接口变体；原核心未给超出此分支的新一般机制/资格条件。43倍数据等宣传不作同预训练底座/质量条件下净省计算，冻结权重不等输出完全不受新支路影响。仅报告局部架构，不把可换任意encoder写成零重训保证；待reader低分关闭校准，不因sound领域或Books排除。

## [Chunk-GRPO](https://arxiv.org/html/2510.21583v1)

2+2+2=6，v1§4/5.1/5.3/6（txt127–217/368–417）。按相对L1动态预设denoise chunks，clipping作用于chunk geometric-mean ratio而非逐step，训练仍用同一terminal advantage；不把它称已恢复每step真实因果credit或严格joint-path importance sampler。FLUX1dev/HPDv2.1/HPSv3，名义T17而[2,3,4,7]和16对应末无随机step排除，配置身份保留。optional半chunk采样偏高noise可改善偏好却GenEval.69降.67，非全质量改进；HPSv3训练/评价同proxy，ImageReward为另读出。所有rollout/reward/训练费保留，fixed boundaries非在线自适应；待Ch33实际差额与reader。

## [Doc-Researcher](https://arxiv.org/html/2510.21603v1)

2+1+2=5，v1§3.1–3.3/4.3/5.2–5.6（txt81–96/287–313/336–355/1272–1318/1381–1394）。layout/bbox可追溯证据与text/visual hybrid、summary/chunk/page/full按query选择；新增评价盲区是document召回不等layout证据召回及多轮收益边际递减，不将MinerU+多agent组合名当新原理。M4DocBench158专家题/304文档6177页，Qwen32B/235B、DeepSeekR1等，96k截断longcontext与不同工具成本不完全可比，50.6不是可归因“必须多agent”的证明。Planner消融同时去文档筛选/粒度选择，不能拆独因果；一次deep解析2.5h换research期省费需摊销，4h search/2hplanning/2hgeneration与总体说法分开。摘要2009/ACM2018为模板残留不作公开日。待Ch76实际覆盖与reader。

## [Modest-Align](https://arxiv.org/html/2510.21606v1)

2+1+2=5，v1§3.2–3.3/4设置/4.3/Limitations（txt184–220/266–287/337–353/479–491）。弱正pair下在frozen单模态latents上加Gaussian并平滑target，保contrastive软目标而不让一个可疑positive承载全部确定性；新增采用限该已测条件，不重记一般noise/label-smoothing发明。原first-order Taylor写出梯度平方penalty并不一般成立（Gaussian二阶期望依Hessian trace），不采用普遍防collapse证明。DINOv2/BGE和Fusemix matched encoders、309024GB/3.5M/10k batch，gridsearch sigma.01/alpha.1；预训练底座全费与CLIP400M从头训不可直接比较600倍。更干净pair/大scale未知，retrievalrecall非校准概率；待Ch23实际比较与reader。

## [Generalised Flow Maps](https://arxiv.org/html/2510.21608v1)

2+1+2=5，v1§3.1–3.3/§4设置与SO3/Poincare反侧/6（txt125–210/229–235/448–457）。fewstep flow-map移到Riemannian几何须用exp/log、tangent projection、metric distance和differential，不能直接Euclidean线性interpolation；三self-distill目标实际stopgrad/JVP是实现资格，不是训练任意网络即理论唯一最优。光滑wellposed流、所用exp/log域与数值求解前提保留，不授权cut-locus任意全局唯一或离散量化无误差。采用通用生成机制，不扩蛋白/RNA/earth应用；只用SO3合成/Hyp几何对照，NLL无统一winner、Poincare部分目标underfit，低NFE与训练JVP/flow代价分开。待Ch24具体owner与reader。

## [Huxley-Godel Machine](https://arxiv.org/html/2510.21614v1)

2+2+2=6，v1§2/3.1–3.3/4.1–4.3/6（txt105–211/257–272/298–309/356–360）。当前agent分数不等后代改进潜力，按clade success/fail估CMP扩展、另policy评估单agent-task，再异步调度；不是形式证明自改安全或通用Godel最优。theory只有terminalutility、repeatable trials、proof免费、每mod固定单位费；empirical加权历史均值不是trueCMP oracle，selection bias/共享后代依赖仍在。matched初始agent/800eval，SICA45%budget后反复错误不可当全预算公平胜；8000full500与SWE-Lite93overlap另filtered，跨LLM不是同模型泛化。allocatedCPUh不等全部API/token净费，无项目代码执行/复现，待Ch80实际差额与reader。

## [Epipolar video preference](https://arxiv.org/html/2510.21615v1)

2+1+2=5，v1§3/4.1/4.5/F（txt77–133/240–246/717–719）。同prompt内部SIFT/RANSAC Sampson error排序训FlowDPO，加temporal variance防静态捷径；经典几何只在static scene/dynamiccamera的对应前提有效，不能跨场景绝对比较或授dynamic物体世界物理正确。Wan2.1-1.3B、24k/30k合成视频约1980A6000GPUh、LoRA64/alpha128再4A6000训2日，reference禁adapter省权重不省forward。400视频/偏好与重建/几何代理分开，Gemma扩prompt、配对过滤都付费；non-diff reward不意味着RL原则不可行，DPO是选择非理论必要。待Ch24/25实际owner与reader。

## [CoD counterfactual distillation](https://arxiv.org/html/2510.21631v1)

2+1+2=5，v1§2–4/Discussion/Limitations（txt78–155/176–190/530–540）。固定few-shot总量用k/2原例+k/2经teacher验证翻label的LLM反事实，补decisionboundary而非全随机数据；教师与生成器调用/全量teacher训练非免费标签。closest CFE无保证，翻teacher不等语义真label；linear/FIM结论不从scalar p(1-p)较大无条件推出任意xx^T的Loewner严格支配，不采该普遍证明。Hausdorff界需精确匹配、双边全boundary epsilon覆盖/小扰动/compact等，不由少量实样自动成立。六binary文本任务/DeBERTa100M→44/22M、Qwen1.5→.5B、五run均值std；generative sequence未来，teacher偏差继承保留。待distillation owner具体比较与reader。

## [FlowSynth](https://arxiv.org/html/2510.21667v1)

2+1+2=5，v1§2/3.3/4.1–4.3必要（txt56–150）。预测Gaussian velocity均值/方差NLL，依预测方差采多条trajectory并用跨note CLAP一致性/文本目标选；相比仅point velocity新增有界uncertainty-guided search接口，不只是新乐器场景。学习方差不是已校准epistemic uncertainty，逐步随机velocity无自动原FM marginal等价，temperature极值动机不授最优schedule；variance下限/clip仍需验。NSynth305979/1006instrument/4秒，8A100/batch32 each/500ksteps，dopri5“16steps”非全部自适应NFE。CLAP同时条件/selector/评价存在proxy耦合，no-search文本CLAP可更差；N8/16/32全生成/选择费与实时SLO未闭。采用限probabilistic readout/选择代价，待Ch24实际论证与reader。

## [WorldGrow](https://arxiv.org/html/2510.21682v1)

2+1+2=5，v1§4/5.1/5.3/6（txt147–211/287–297/417–429/453–456）。3Dblock overlap inpaint分coarse layout/fine refinement/SLAT appearance，occlusion-aware aggregation须和scene decoder一起训；单换aggregation反退，不能把object prior直接换场景即无损。3425curatedhouses/120kfine38kcoarse，TRELLISXL、VAE100k/inpaint200k、50steps；A100每block20s与10×10约30min/13GB是有限作者配置。unbounded仅可继续扩XY，不保无限全局一致/vertical扩展/physics，可见global质量评测91人10scene不是全部scene真值；固定genericprompt等同当前无语义control。块数总存储/重叠重生成/全部训练费保留，待Ch25具体覆盖与reader。

## [BachVid](https://arxiv.org/html/2510.21696v1)

2+1+2=5，v1§3.2–3.5/4.1/4.3/Limitations（txt122–173/195–254/302–325/344–348）。先生成identityvideo、cache部分层KV/attentionoutput，分别foreground匹配与background同坐标，按目标位置重编码key RoPE后注入后续video；没有外部reference不等不付identity生成/存储/匹配代价。原Eq14将logmask写softmax后，不能代修成已核执行recipe或正确概率；采用限布局/位置和前背景复用分责。CogVideoX40组×5prompt，DeepSeek构题/CLIP+SAM2/ArcFace/VBench代理，layer/timing由启发式消融选，early/late不稳定；效果不证明任意相机/新角色适用，referenceimage输入不支持。内存/匹配/重复denoise全费，未核kernel/实现/复现，待Ch24实际差额与reader。

## [DeepAgent / ToolPO](https://arxiv.org/html/2510.21618v1)

2+2+2=6，v1§3.3–3.5/4.3/5.4–5.6（txt136–165/706–761/873–893）。模型显式fold动作→auxiliary LLM并行压episodic/working/tool三JSON后替换rawhistory，与按工具需求在线检索分工；结构JSON不保语义无损或真实工具结果。ToolPO全局终奖adv给全部generatedtoken，工具/折叠adv只加相应tokenmask，是trajectory actionreward聚合，不是每次call独立因果credit；LLM模拟API不等真实world状态/权限。QwQ32B+Qwen2.5-32Baux、64H20、8rollouts/batch64/100steps/max32768，部署max81920/额外VQA32B全部计费；去fold/模拟器/credit消融支持有限组合，不给同时去机制的差额唯一因果。moreactionlimit与更好score不认证同成本、部署可靠或任意tool规模，压缩关键细节仍可能丢失。待reader/Ch75或Ch78唯一实际差额，不重复两处整合。

## [Private policy optimization sample complexity](https://arxiv.org/html/2510.21060v1)

2+2+2=6，隐私边界深入；exact-v1§2–6（txt73–326）、H/I（1658–1703）实际必要支持与直接反侧。动态on-policy后续数据依赖先前policy，不能把预固定(x,y)邻接直接搬入；定义N个各出现一次的user/prompt，fresh batch one-pass，单unit的私有PrivUpdate经adaptive parallel composition保护最终policy/JDP，N=mT。**仍是item-level，不是反复出现真实用户的user-level保护**；换成multi-pass/同prompt重复rollout不能不重做会计就继承。PG需bounded loggradient/Hessian与reward界，FOSP再经Fisher非退化/compatible transfer条件才到global gap；lower-order privacy项只在相应精度/维数/epsilon条件下，非所有PO。NPG用private regression oracle与coverage C，general exponential机制统计成立不保计算高效；高维corollary表面去d，W因Gaussian噪声仍可随sqrt(d)长，作者明确未来改分析，不采用dimension-free普遍保证。

主理论是bandit简化，非完整一般MDP/LLM PPO实证；H实际CartPole两层64hidden、100epochs/batch10/gamma.99、3seeds，DP-NPG epsilon5平均478.73/SD28.05对NPG492.90/10.04，不把best epoch494.70当final或不损质量。H的advantage normalization及有限神经实验不自动满足全部定理，未核实现/accountant；硬件/precision/LLM长度/生产SLO为Not Disclosed/不适用本理论。全部fresh unit、reward/trajectory、private solver/噪声和独立效用回归计费，无LLM规模结果不影响采用真实privacy-unit/one-pass条件。Current abs为v3/2026May13、AcceptedNeurIPS，无撤回/勘误标记或具体同家族更早正文链接；只采用v1，不用venue推更早，不为假想全渠道反证无限搜索。待sole准入/受限Evidence校准与actual Ch72比较，不授Books/SAVE。
