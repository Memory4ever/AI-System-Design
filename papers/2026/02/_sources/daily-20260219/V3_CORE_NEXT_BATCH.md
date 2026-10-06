# 本日第二批必要证据

原始身份各自v1，日期按本日同身份 [DataCite上界](V3_DATACITE_DATE_BOUNDS.json)与官方announcement下界，不借当前Updated或相邻ID；已确认落窗不等全部已准入。以下实际核心阅读可复用，Books判断/独立复核仍逐项继续。

## 2602.15166v1 Fast and Fusiest — 2+1+2=5

实际读[精确v1](https://arxiv.org/html/2602.15166v1) §III–V、VII-A–G；[本地](V3-exact-v1/2602.15166v1.html)。新增是把局部pmapping按可互换接口分组，只在compatible group内按目标与全resource/lifetime reservations做Pareto剪枝，再合并fusion链。兼容要求shared tensor tile shape、dataflow/order/backing memory相同；reservation tree在同分支求和、跨分支取最大，未确认后续分支保留，确定后才collapse。忽略reservation lifetime会误剪以后可用的组合；不consolidate时受测链搜索呈指数增长。这里最优仅限所探索mapspace与LoopTree分析模型，不是任意compiler/真实hardware最优。

VII-B使用TPUv4i-like解析模型，128MiBglobal/4core4MiBlocal、128×1288bitMAC、1.05GHz/614GBs；GPT3-6.7B batch4 seq4096。SA/遗传/随机baseline重写为同mapspace并复用cached pmappings，所报baseline搜索时间以1CPUms/pmapping估算，排除join/selection，是下界而非真实年级运行。主算法30CPUh，基线给1000倍预算仍约2%gap；当前Turbopmapper0.75CPUh是不同公开实现，不能合为同v1测量。VII-G最多64einsums近线性是经验结果，不保证所有Pareto frontier增长。未核代码、silicon或复现；候选标准必要证据足够，Books待actual owner，不授完成。

## 2602.15172v1 TCM — 2+1+2=5

实际读[精确v1](https://arxiv.org/html/2602.15172v1) §III–VI-E；[本地](V3-exact-v1/2602.15172v1.html)。原名The Turbo-Charged Mapper。新增把dataplacement显式为storage node及其顺序/存在性，区分tensor lifetime/reuse与dataflow；同storage nodes之间looporder可按条件等价裁剪，但convolution partially relevant rank直接位于storage node之下会改变line buffer，必须保留这些顺序分支，不授跨storage node重排；不能有益reuse的loop合并剪枝。先对dataplacement/dataflow做symbolic currying，再填数值shape，保留未知维与divisibility条件，避免给每shape反复重算；最优依赖这些等价/pruning条件和解析model mapspace。root纠正后已定点重新核IV-A原文，不扩大其他版比较。

TPUv4i-like/NVDLA-like解析模型，GPT3-6.7B QK prefill batch64/seq65536，MobileNet batch64，不外推现代LLMdecode GPU运行。§VI-E固定同一线程，TCM37s完毕，对照Timeloop随机、Hint全PE、LOMA LPF各给1/10/100/1000倍time；1000倍LOMA EDP1.21、Hint2.88，对照已知最优为TCM遍历模型空间所得。全PE限制本例保留optimum但不是一般guarantee，巨大array/local buffer条件可使该限制只有invalid mappings。40/400倍model evaluation速度是解析实现比较，不是算子执行加速。未核artifact/复现，Books待owner。

## 2602.15143v1 Trace Rewriting — 2+2+2=6，安全受影响深入

实际读[精确v1](https://arxiv.org/html/2602.15143v1) §3–5/Table1、§7、AppendixD.2.2/D.3.3；[本地](V3-exact-v1/2602.15143v1.html)。新增API输出trace可分两责任：保持teacher最终回答而压低SFT学生transfer，或在部分trace植入可通过student查询检测的trigger/target关系。Prompt-OPRO以proxy学生选rewrite指令；HB/FO/RHB梯度分支投影回离散token并mask final-answer，但cost高且弱于prompt法。Teacher是DeepSeek-R1-Distill-Qwen7B；proxy与heldout仅有限Llama/Qwen小模型、GSM8KPlatinum/MATH。最终答对不证明中间trace语义全保，未知学生/其他distillation技术未验。

Table1 K5 Llama3.2-3B detection0.55，K20才0.99；false attribution有0.02，并非总零。100独立随机prompt试验，ours/VIA只10%trace注入、KGW/GINSEW全部注入，对照覆盖不等。D.3.3只single-source、未知watermark文本；已知结构regex删等号附近token、Parrot paraphrase两策略，质量均下降且query多后检测恢复。不能把这两种处理当任意adaptive去除保证，也不同于15323密码不可伪造；rewrite+proxy search+验证查询都有成本。反侧足够，Books待具体已有source/claim对比。

## 2602.15195v1 Spectral LoRA screen — 2+1+2=5，安全受影响深入

实际读[精确v1](https://arxiv.org/html/2602.15195v1) abstract/§3–5；[本地](V3-exact-v1/2602.15195v1.html)。当前v3不是本日v1：本版先将Q/K/V/O projection updates求和，仅五种SVD统计（σ1/Frobenius/σ1除singularsum/entropy/kurtosis），不是20维分离投影；Llama3.2-3B、rank16/layer21、400benign reference，不是三个模型/100%泛化。统计经Z-score/tanh、logistic regression与τ选取；选层来自先前discriminating分析，benign bank/validation population与split应保留，不认证不存在selection/leakage偏差。

heldout100含50benign/50poison，TP48/50、TN49/50=97%，1/50=2%FPR，与作者‘under2%’文字不一致，本轮采用计数而非宣传。攻击为有限rare/context trigger与1/3/5%poison；adaptive能regularize或分散谱，benign bank污染/分布迁移也可破坏sensor。Artifact-only读统计能省trigger查询但不是backdoor-free证书；没有核weights/code或生产运行。必要反侧已读，不借未来v3采用。

## 2602.15189v1 ScrapeGraphAI-100k — 2+1+2=5

实际读[精确v1](https://arxiv.org/html/2602.15189v1) §3–5/Table4、§6–8；[本地](V3-exact-v1/2602.15189v1.html)。新增生产schema长尾切片与value correctness评价盲区：~9m opt-in Q2/Q3-2025 telemetry按schema-hash最多5不同rootdomain降至93695；87.4%GPT4omini、两ecommerce schemas原占5m，confounding明确。深度≥7/key≥200等是观测阈值，不是跨provider原因/通用routing常数；invalid responses保留但93%valid仅语法+schema，不认证事实值。

§5 GPT5nano重新生成labels，作者称gold不等人工独立真值；10k schema/50k content/10k response filter、4096window、Qwen1.7B rank16 QLoRA两epochA10080GB，2714test。Fine-tuned keyF1.8866接近Qwen30B.8915，value similarity仍.4624对.4797，JSON validity.9558对base.9544，结构进步不能代语义抽取准确率。Data-size/cost条件不能合为工业可靠性；telemetry truncation、网站变化/consent representativeness近证据。Specific interpretation可采用，是否已有覆盖待actual owner。

## 2602.15198v1 Colosseum — 2+2+2=6，安全审计受影响深入

实际读[精确v1](https://arxiv.org/html/2602.15198v1) §3–6/Definition4.1/Fig4–10；[本地](V3-exact-v1/2602.15198v1.html)。新增把communication judge和environment action impacts分账：有限DCOP任务先定义nominal cooperative reward、coalition subset/secondary objectives和实现动作，测overall regret、coalition mean unilateral regret与coalition advantage。Definition4.1 Fstar理想optimal，但实际对照采用no-collusion reference protocol；不能混成都已全局optimum。隐私/sideeffects只在预先建入目标/变量时可观测，这不是自动审计任意泄漏。

Meeting/Hospital/Jira合成environment，模型同backbone、temperature.7，普通5seeds、emergent20/10seeds；显式secret channel/目标prompt不是生产自然串谋率。Fig5 Gemini/4.1mini log judge漏掉动作优势，Kimi2等log judge高却未实际成功；Fig6调整顺序也不能自动改善。Provisioner控制资源约束，coalition membership影响可行性；多数假信息belief可增而overall outcome不成比例。理论utility和nominal objectives本身未获伦理真值，任务违法时sabotage甚至可能是期望。异构agents/新任务/百千规模transfer未验；采用审计维度分责，不授检测生产串谋的完整能力。Books待owner比较。

## 2602.15206v1 MAVRL — 2+1+2=5

实际读[精确v1](https://arxiv.org/html/2602.15206v1) §3–7/Algorithm1、AppendixA.2；[本地](V3-exact-v1/2602.15206v1.html)。新增共享latent reward与feedback-specific likelihood，不强行把rating当连续reward回归、把stop当负reward；偏好BT、demo BoltzmannQ、rating ordinal cutpoints、stop累计suboptimality hazard与right-censor各自表达观测责任，共同ELBO以Gaussian amortized reward encoder/auxiliaryQ/TD训练。相对权重由噪声模型/样本人口决定，‘无需feedback loss balancing’不等没有KL/TD超参，也不保证错误likelihood无偏；条件独立给定reward是建模前提。Asynchronous只说离线minibatch混合次序自由，不证明生产迟到反馈队列。

三tabulargrid+Acrobot/CartPole/LunarLander，10runs，固定每modality feedback数，但多type合并总反馈多于single，不能声称相同总annotation budget纯因果优势。AppendixA.2所有feedback由已知Qstar/reward模拟，stop hazard与训练相同family；未测真实human inconsistency/contextbias或LLM RLHF。CartPole某组合12.2低于rating69.8，multi非稳定普胜；EPIC只tabular且忽略potential shaping/scale/shift，policyreturn非reward还原真值。Perturb测试冻结reward、在新dynamics重训policy，不是原policy零样本robustness。该条件化监督表示机制准入，不授真实人反馈校准或生产保证；Books待比较。

## 2602.15260v1 Prefix OPD — 2+2+2=6

实际读[精确v1](https://arxiv.org/html/2602.15260v1) §2–5/Table1–3、§8；[本地](V3-exact-v1/2602.15260v1.html)。完整student rollout容易保留tail监督，但长CoT生成/teacher scoring成本高；新增只生成student前Ltrain token后停止，用sample-based reverseKL/importance correction更新该prefix，eval移除cap。同vocabulary且base能格式/指令是条件，think special token强制以免样本KL不学切换；线性schedule从1按256渐增。‘早期重要’由固定位置mask与teacher-prefix观测支持，只是局部heuristic，不证明高层规划的唯一机制。

OpenThoughts3、Qwen3-1.7/8B-Base students、Qwen3-8B teacher，OPD batch512/4samples/lr5e-5/60steps，8A100；SeqKD teacher QwQ32B/batch128/lr1e-4/192k与OPD30.7k不同，不能把对SeqKD收益纯归因prefix。MATH/GPQA/MMLU mean@4，AIME mean@16；AIME24既dev选checkpoint又reportedtest，并非独立test泛化。FLOPs含sampling/teacherstudent scoring/backward/update、hours不含eval，SeqKD离线生成没计；47倍是类似AIME目标的estimated GPU FLOP reduction（2.7e19vs5.7e17），即compute-to-target估算，不是测得time reduction；GPUhours另报且SeqKD离线生成未计。

Table1 1.7B短prefix GPQA1.0/MMLU1.5低于base11.2/9.1，8B与schedule更稳；越长prefix充分budget可胜短prefix，tail loss1.7B反升。§5.3 forward/offpolicy短prefix另有退步，不能全OPD通用。§8 late refusal/calibration undertraining是作者风险推断，未实际安全benchmark；须完整tail回归/逐渐延长或fullOPD/SFT回退，不授部署安全。局部训练预算/容量边界可采用，Books待owner。

## 2602.15210v1 Multilingual curation — 2+1+2=5

实际读[精确v1](https://arxiv.org/html/2602.15210v1) §3–5；[本地](V3-exact-v1/2602.15210v1.html)。潜在修正‘多语言必因容量竞争损伤English’：13非英语言、3B/60B、固定50:50 bilingual、相同其他train配置，对curatedEnglish-only/双语curation做比较，English curation在12/13非英上正收益，curatednonEnglish在12/13英语上正收益。Bengali反侧保留；12/13并非所有语言。语言距离用parallel FLoRes避免topic混杂，但Pearson只是相关，不证明距离因果。低资源三语言随机translation与scored-source translation比较支持源质量条件，不是translation必胜。

curation只披露filter/embedding/synthetic rephrase类别与语言适配，没有完整recipe；所谓uncurated其实DCLM/FineWeb2已有上游curation。3B60B使用cloze，而1T大run使用MCF，不能合并尺度解释；base无posttrain、Llama3.2tokenizer/ctx4096固定。20T corpus/8Tsynthetic、1T随机subset、650B/250B/100B阶段5/10/20%非英形成7.75%不是单一curation消融；与Qwen/Granite等4–10倍FLOPs跨architecture/tokenizer/recipe估算，不授纯机制因果或frontier扩展验证。采用局部质量/双向transfer条件，不宣称消除所有capacity interference。重复seed/硬件/precision未披露，未复现；Books待实际owner。

## 2602.15257v1 Long-context visual documents — 2+2+2=6，评价纠错受影响深入

实际读[精确v1](https://arxiv.org/html/2602.15257v1) §3–5/Table1–7、AppendixA.1训练/merge；[本地](V3-exact-v1/2602.15257v1.html)。新增可验证评价纠错与长context训练分布反侧：MMLongBenchDoc342例flag并人工review，251改question/answer、16删除；wrongdocument/unanswerable及等价答案扩展改变被测任务，不将新旧得分直接合。VA/LCA由baselinemax归一，多benchmark也不是独立truth。三个runσ.33/.24有限稳定性，不是所有ablation置信区间。

MistralSmall3.1-24B/Qwen3VL32B，teacher235B；CPT/SFT/LongPO用merge vector0.5或0.25，指标是mergedartifact不是rawtrain。训练short104pages/long336pages，resolution随context动态缩放，Mistral128K/344K、Qwen128K/256K，H100/H200、SP16/48/24各stage，不能由短stage胜短+长stage推唯一长度因果或相同训练预算；作者ProLong极短median484tokens对本篇longmedian156images，maxcontext不同不等分布更长。Pageindex train+eval益、仅evalVA反降，支持接口训练一致性条件，不是添加metadata普遍有益；HELMET/LongBench等反侧仍在Table5。

Visual-only CPT把HELMET37→48.5支持受限跨模态迁移，不证明特定neuralbinding机制。Recursiveteacher生成在VA益但MMLBD-C54.5低于plain57.0；CPT可skip视觉任务而HELMET有损，LongPO更高compute且plainSFT某benchmark胜。新增结论是更长训练/复杂配方并非统一优胜，须保持实际分布、artifactmerge、页标识及evaluation版本；只局部document任务，不授production文档正确性/成本。必要纠错与反侧足够，Books待owner。
