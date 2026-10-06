# Jan02 优化与局部机制小批（继续中）

只保存已实际读取的必要证据。完整v1题摘不替代标准/深入审阅，日期原值在DATACITE_POTENTIAL.json；共同holiday/no-advance-ID区间必须与同正文前公开信号分开。可选代码未运行，未复现实验。CF-GRPO已独立通过；Youtu-Agent贡献前关闭与HaluNet低分关闭已校准。以下五项必要core、限定证据与具体Books决定均经root实际非作者核：CLoRA/Localized/Vulcan三处具体缺口深入后正文及邻接/末注POST通过；Wavelet具体已有覆盖、FrozenAtoms标准仅报告通过。不授整篇所有主张或日级完成；下面各项原拟处置文字保留过程依据，以此最新实际决定为准。

## [Youtu-LLM — 2512.24618v1](https://arxiv.org/html/2512.24618v1)

同家族以CF-GRPO条件训练人口为拟采用命题，2+2+3=7；作者与root实际核§3.1.1/§4.2.2必要机制、公式、Fig13与限定，非作者Evidence通过。Ch33 2091/2093两段及末注已写入，root实际对读2080–2105前后衔接与末注，POST通过，不等日报完成。

§4.2.2/Fig13实际区分训练policy与快速rollout policy：K(q)为rollout下ratio−1−logratio的期望；整prompt输出group只有K(q)<τ才进入gradient，超阈值整组丢弃。τ=0.01是举例，不能当全任务推荐。原CF-GRPO公式明确在P(Q|K(q)<τ)上求期望：过滤不只修正同一组的importance ratio，还改变哪些prompt进入更新。我的系统推断是应分别记录原prompt人口、拒收率/切片与admitted人口，不能把条件目标称为原人口的无偏优化；这不是作者已证明的部署保证。有限sample的K估计、response/token归约、阈值随policy变化及support不足均未由该公式自动解决。

Fig13及其正文只支持内部math/code设置的局部stability观察：BF16与FP16训练/rollout概率漂移不同，另有consistent sampling分支；不将其外推为FP16总优于BF16、任意kernel匹配或任意task收敛。该受影响小节没有披露硬件型号、group数值、完整rollout长度/batch、重复seed与不确定性，不能靠最终模型的排行榜填补CF消融预算。筛选增加丢样、重采/计算成本并可能系统性排除高漂移prompt，性能收益与prompt难度选择不能混为一个已消除偏差的结论。

§3.1.1补充的tokenizer机制也有具体配额：保留ASCII/非中文base→中文再平衡并移除过长领域词→code/math专门配额。Table3同1B/GQA/80Btoken scratch是控制，但相同token数不是相同bytes/compute，coding并非最好；不把所有后续agent能力归因词表或curriculum，不另计第二个家族/分数。

当前对读Ch33 360–428（prompt admission/隐式curriculum）与policy-staleness旧论证后，已在TRAIN-GRPO owner的policy freshness处融入最小机制桥接：按prompt-level rollout/current KL做整group admission及条件P(Q|K<τ)目标。具体拒收人口、估计/support及成本/回退保留；root必要原源和实际写后通过。

## [Youtu-Agent — 2512.24615v1](https://arxiv.org/html/2512.24615v1)

贡献前关闭，不评分。实际§2.3/2.4/3.4主要重呈现Training-Free GRPO的文本经验与AgentLightning/VeRL/Ray REST训练集成；turn-level advantage correction没有足以独立核验的新公式/有效性条件。官方[README_ZH dated news](https://github.com/TencentCloudADP/youtu-agent/blob/main/README_ZH.md)原页L208–214分别记Dec10 AgentLightning/128GPU集成、Nov12 mainbranch及Oct10 Training-Free GRPO、Sep28 auto tool功能；这是功能既有的依据，不是论文首次公开日期。仅较大系统组合/局部训练吞吐数字不足以重新准入。root实际完整题摘和决定性core校准该关闭理由；不采40%速度为统一预算可比保证。

## [HaluNet — 2512.24562v1](https://arxiv.org/abs/2512.24562v1)

候选1+1+2=4，关闭，Books仅报告：single-QA internal embedding/probability自适应多路融合只是局部detector配置，不形成新的跨任务真伪核验或校准保证；confidence不能认证fact。实际created=Jan1T03:14:50Z、registered=03:14:51Z，共同holiday/ID规则只给[Jan1T01Z,03:14:51Z)保守公开区间，完全本窗，未当registered精确公开。root实际完整v1题摘及低分关闭理由校准通过；未授全文性能、实现复现或Books增量。

## [CLoRA — 2512.24603v1](https://arxiv.org/html/2512.24603v1)

2+1+2=5。实际§IV-A–D/V-A/B/D：m模块各学习Q_h^j，共享p对D_h/U_h，ΔW_j=Σ_h D_h Q_h^j U_h，参数(2dr+mr²)p+c对普通2drm+c；节省近似要求r≪d/p<m，rank上界pr非mr。输入identity分支可merge固定投影，不是dynamic router；全因子共享CLoRA#反而较差。SADE的样本无关Frobenius项代理output decorrelation，不授数据真实正交，O(p²d³)计算不免费；93.9%仅正则项GFLOPs差，不是端到端训练加速。ViTB/16 ImageNet21k/VTAB19/800+200再1000train，Adam/batch32/100ep/10warm，LR/WD/α/p搜索/rank8；baseline部分引用原报告或原配置非统一预算。hardware/precision/seed未披露。拟TRAIN-LORA Ch30 161–177现有effective-subspace/target modules缺共享basis与module coefficient分账的小桥接；待root证据/具体gap与窄写锁。

## [Localized Calibrated Uncertainty — 2512.24560v1](https://arxiv.org/html/2512.24560v1)

2+1+2=5。实际§4–7/10.1/10.2：hidden tests定义intent，修复后kept token/line作标签；最小patch近似不唯一、测试不完备、patchability筛选改变人口，测的是某修复合同保留概率非唯一bug/真值。GPT4o/QwenCoder7B在HumanEval+/MBPP+/LiveCodeBench/RepoCod-s，纳入1368/1355非全部attempt。辅助QwenCoder0.5B/7B层embedding→32/64projection→max/mean/4head aggregation→logistic predictor可query任意集合，不改generator；联合token/line/problem loss，30ep Adam.001/dropout.2/5fold。Platt使用目标dataset内部80/20五折，leave-one-dataset-out probe仍需目标域标签，并非zero-shot校准。§10.2承认没有干净heldout/hyperparameter overfit，RepoCod弱；ECE低+BSS近0不等定位有用。multisample另付5个temp.8副本（main temp0）及scaling成本，非probe同预算；hardware/precision/实测latency未披露，不采text0.4 ECE冲突数字。拟Ch66 630–650已有partial-program/多答案与label-relative oracle分责，但未明确repair-kept arbitrary-span calibration与整程序正确不同，待root具体gap/必要源审。

## [Wavelet primitives — 2512.24438v1](https://arxiv.org/html/2512.24438v1)

2+1+2=5。实际§2.4/3.3/4：DWT输入线性分解不推出ViT全latent线性homomorphism，rawsum的CKA/SSIM退化。训练组合primitive CLS的系数，经frozen classification head拟合原图输出；Table2原分类器agreement≠Table1groundtruth准确率或全latent重构，系数多解不确定唯一语义。50k ImageNet1k每类50/60–20–20，frozenViTB/LImageNet21k/Haar或db4，一/两层、100epSGD.001；两层退化、扰动双方均降，非任意语义/robustness保证；hardware/precision/seed未披露。拟具体已有覆盖MULTIMODAL-REPRESENTATION Ch23 63–65可读≠模型能用、101–103 probe/几何不授完整encoder充分性，不称现书包含DWT数学/分类头公式；受限诊断保报告，不复制长期分段验收框架。待root核。

## [Frozen building blocks→planning — 2512.24532v1](https://arxiv.org/html/2512.24532v1)

2+1+2=5。实际§3–5/Table1/directRL及attention对照：ASCII rotation/translation/scale 12k原子SFT后冻结base，rank64LoRA GRPO学≤5step策略；frozen参数不保LoRA后原子行为不变，不是固定executor/真实动力学。Static初图+history与Dynamic每步state更新测不同观测接口；DirectRL同RL设置却无12kSFT预算，不能判相同总训练的唯一因果优势。Qwen2.5-1.5B/A10080GB/Adam1e-5/batch64trajectory/temp1.4→.7/testgreedy，100随机未见任务/距离≤5，terminal+2/step−.1/repeat−.2与greedy-GT shaping；precision/seed未披露，attention相关图不授内部causal。拟仅报告：没有独立验证frozen技能保留或完整匹配训练预算，不足建立可发布skill/policy分责保证；Ch30 14/80–103目标与参数化分账、Ch84 1068–1075新收益/旧能力双验收已是现有约束，不声称新物理知识已吸收。待root具体长期门槛审。

## [Vulcan — 2512.25065v1](https://arxiv.org/html/2512.25065v1)

2+2+2=6。实际§3/4.1/4.2/5.1–5.2：LLM只生成Value scalar/Rank score或有限queue transition，固定scaffolding收state并执行；readonly/signature/scratch/primitives边界≠自然语言constraint，code不获部署权。FullSort/SampleSort/PQ转移维护成本，PQ每访问O(logN)；QT≤5FIFO/LRU与有限ghost保证primitive结构，不自动证明完整policy成本/安全。106CloudPhysics traces first50krequest/15features/Kmeans10clusters；一trace搜索25candidate/round top2，post-eval all含searchtrace非全heldout。QT两cluster100iteration/17baseline/size-agnostic slots≠前bytes13baseline MRR，不能合并收益。Memorytier四app150搜索/ARMS改20windows10s history，不仅score；NUMA emulation非真实CXL/非LLM inference负载。生成API成本与运行维护分账、phase shift重新校准，不授generaloptimal/transfer，代码未跑。拟AGENT-PLATFORM Ch84 883–899 codeproposal/promotion还缺interface固定execution complexity与scaffolding成本的桥接；待root原源/owner窄锁，不另讲cache/tiering算法。
