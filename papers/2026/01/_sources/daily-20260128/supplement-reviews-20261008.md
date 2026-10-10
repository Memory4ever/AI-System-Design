# Jan28 增量必要原证与 Books 比较 — 进行中

## 最新层级（恢复后的实际结果）

新增61已到必要证据/具体Books安全终态：35整合48段16owner、11已有覆盖、9仅报告、6中心争议；全部35实际正文/完整邻接/自身末注 POST与状态轻核已由非作者通过，窄锁释放。下文旧待Source/待Books/待锁/PRE仅拟文为历史阶段；未变有效Source/PRE/POST复用，不代表当前普通队列。原64保护，最终六部分已融入README，V3进行态通过，最终DAY尚待。

原64家族的证据不重写。本文件只记录新60候选中的必要采用命题；下载不是审阅，Owner pending不是Books终态。共同日期口径为精确v1 Submitted在Jan26公告截止前、官方final-ID仅公告后分配规则、Jan27已deposit上界联合确认2026-01-27；不以Submitted、created或Updated单值认定公开。当前68官方AB轻量未见withdrawal/erratum信号，不遍历版本史。

## 恢复后 18730 — Constitution self-evaluation 的选择门

作者实际读 exact-v1 §3.1/Algorithm1、§3.2–3.3、§4.1–4.7/Table2–6、§5.3/Limitations、A.2/Table9、E。整套 constitution 先进入 base prompt，同模型逐 principle 1–5 self-score，任一低于3才做一次合并 critique/revision；这是可错的选择门，不是独立安全 verifier。各500条SafeRLHF/HH-RLHF、GPT4.1mini/Claude3.5Haiku/Mistral7B及GPT4.1judge，原则包含文化/表达等构念；50human验证只是对应Likert/binary一致性，不是危害 ground truth 或攻击部署覆盖。Table5 SafeRLHF 742→3717 tokens，较CA-SelfRefine低但仍5倍base且violation3.450高于其1-cycle1.838；不采免费低overhead。§5.3 自微调后表面提及原则可能骗过self-gate、无revision，直接反側保留；revision自身也能新引violation。MMLU局部退步，Table3 .098与4.2“less than .01”内文冲突不采该精确描述，E统一p=.002未给足计算细节不外推。2+2+2=6，安全与选择门反侧必要深入足够；不授任意constitution、对抗安全或自评真实透明。Books待Ch80具体选择门/监督漂移比较。

## 恢复后 18731 — Meta reward 的 support/query 与困难用户

作者实际读 exact-v1 §3.2、§4.1/Algorithm2/Eq5–15、§5.1.1–5.1.4/Table1、§5.3.1–5.3.5/Table2、§6–7。共享两base reward函数与初始线性weights，inner只以user support适配weights，outer用disjoint query更新initialization及base；困难程度是adapt后query loss，quantile+sigmoid强调高loss，不是识别真值或认证每人公平。PRISM1287过滤用户/平均6dialogs，Reddit仅40高标注annotators，不代表一般稀疏用户；seen/unseen各半、20随机split，RTX A5000/Skywork固定embedding、inner一步/batch2用户。Table2 worst10%仍37.9%左右，去RPO差小且波动，不能授每用户可靠或大幅鲁棒提升；难用户比例过小及batch/γ过大可反退。SynthesizeMe只quarter test人口不同，最小参数数非全费用/端到端SLO；static explicit pairs、动态implicit偏好与policy生成仍future。2+2+2=6，标准Source足够；Books待Ch31共享basis与个体adaptation状态实际差额。

## 恢复后 18734 — 同模型不同特权上下文的 OPD

作者实际读 exact-v1 §3.1–3.2/Algorithm1/Eq6–9、§4.1–4.3/Table2–3、§7、Appendix8.1/Table6。student真实rollout只读problem，teacher在同prefix另读reference solution，再给full-vocab JSD .5或sampled-token logratio；gradient不流teacher。Algorithm“same parameters”与实现冻结initial policy并非相同持续teacher，采用固定initial teacher事实，不补周期刷新。Qwen3-Instruct1.7/4/8B/OpenThoughts math≤30K/8A100/BF16/LoRA64；正文Adam1e-5与附录AdamW2e-5冲突，精确optimizer/LR隔离。1vs8rollout及2Kvs16K明显不同，generatedtokens4–8倍不认证完整teacherforward/logits/memory或墙钟成本；fullvocab更好但峰值memory增加。Table2 1.7B平均30.4<GRPO30.5及部分任务反退，不采全尺度全task胜出。teacher无生成正确性验证，读GT也可能超出能力；需要model/context/target冻结与privileged-use边界，不能称“无外部监督自教”。2+2+2=6，标准Source足够；Books待Ch29自target/privilegedcontext具体差额。

## 恢复后 18527/18533/18543 — 训练奖励与资源口径

作者实际读18527 v1 §3–5、Tables1–4与训练/稀疏attention必要附录：32K/28.5K训练/1.5K验证、Qwen2.5-7B-Instruct1M、GRPO组5/最多2epoch，各AO/ID/复述/quote/judge奖励改变输出目标，eval prompt亦随各reward格式改变，不是单变量统一prompt对照。Qwen embedding取负例、fuzzy.6及另一个LLM扩大gold只是标签建设，非独立真值。跨域长窗口局部收益不认证longctx替RAG；attention NDCG已高、提升有限且跨recipe相关不足归因，全部稀疏RA下降，Finance AO相对−24.6%大于base−20.8%，最佳压缩平均39.7低于RAG43.8。端到端SLO/硬件完整费用Not Disclosed。2+2+2=6；必要Source到最小支持与关键反侧STOP，Books仍待具体比较。

作者实际读18533 v1 §3–5/Table3、A.1/D成本与训练必要段：离线LLM合成reference/keypoints/keywords和Python CodeEval，在线仅regex/ordered keyword-LCS内容与加权style code执行；原准入“style judge”不能作为采用机制，已纠正但准入保持。LCS相对direct-match局部抑制词面rewardhack，不认证事实、否定、paraphrase或内部faithfulness。10K RL/8rollouts/1epoch与10K或100K SFT/3epoch非同费用；3runs/8A800，0.71%只相对Random training step，$21.36离线合成另计。2+2+2=6；必要Source STOP，Books待Ch31具体差额。

作者实际读18543 v1 §3/4.1–4.4/Table5–7与限制：Qwen2.5VL7B控制8step-distilled FLUX1dev，final all-condition point与连续pair-judge改善不同，final失败减pair权重，格式独立。冷启teacher读取reference images，RL12→8轮数均衡重采样改变人口；训练2round/评估最多3、全multiturn比较非全费用匹配，hardware/precision/端到端费用Not Disclosed。pair消融与reflection指标只有局部增量，第三轮边际下降/工具能力上限/多义query过度反思均保留；0.561−.325为23.6百分点非相对百分比。2+2+2=6；必要Source STOP，Books待实际过程奖励与反思分责比较。

## 恢复后 18554/18572 — 组合与 persona 评价构念

作者实际读18554 v1 §3.1–3.3/4.1–4.3、PA式3及必要rule边界；constraint内容/数量/顺序分层，SCC/PCC/position可诊断不同对象，PA实际是约束通过比例而非all-pass。阈值.5与partial JSON允许局部通过，LLM业务/semantic judge不是法律/事实证书；正文1–10与附录0–10/归一化不明，不采用严格解析或架构原因推测。七model受限合成产品/四writingtask，不授开放全部遵从率。2+1+2=5，测量对象反侧深入；必要Source STOP。

作者实际读18572 v1 §3–6/AppendixC–E：six cues/ten one-attribute English US personas/sevenmodels，名字为统计proxy、history内容未控；显式与history切片可以反向。Spearman聚合排序相关、B1000bootstrap单侧CI检验rho1与ANOVA+Tukey-Kramer pooled allvalidresponses/models分开，不授独立样本或人口因果；高overall相关不证明persona一致。AITA majority不为伦理truth，IB Llama3.3替旧judge未新核资格；正文/附录invalid比例不同不拼。2+1+2=5，测量反侧深入；必要Source STOP。实际Ch66 501–507已承载cue类型/实例/场景身份、跨cue方向反转与统计单位边界，拟已有覆盖仅此最小命题，不称其所有统计配方已有。

## 恢复后 18579/18588/18595 — 图状态与中心理论

作者实际读18579 v1 §3.1–3.4/Algorithms1–3、§4.1–4.3/5.1.2–5.3：冻结crossencoder preMLP latent在已取子图聚合再rerank；邻接候选由query dot与排名/bridge分数扩展，bmax100/BATCH10限制人口，α/β、graph/embedding/head应共同版本。randomwalk非对称Lrw的Tr梯度不直接为PH，故不采用严格denoise推导；0degree/断连失败未证。gpt5mini/nano身份文字冲突不拼。QPT仅retrieval平均，Gemma3-12B/Ollama2步×5对照、35.1−31.4=3.7pp；TR含Recall，MissTR局部相关非内部insight/因果，graph建设另费。2+2+2=6，必要Source STOP，Books待Ch76具体差额。

作者实际核18588 v1 §4.2–4.3/Eq24/35–39、§5/Eq55–60、§6/Table1与BAARA必要B段，独立反例一致：conditional配对MLE不等混合边缘logmean，empirical consistency为未证等式；differentiability不推出θ-convex；smooth-convex gradient²/(2β)在该条件是suboptimality下界而非式36上界。即使P=Pemp保留所有K modes，也不是strict-subset丢mode/entropy必降。BAARA高entropy主动prune/DMU/DTU已改变目标与容量，高频词比例不认证semanticcollapse，GPT2/BERT1B–3B身份、data/lr/precision/hardware关键设置不足。中心“稳定必崩溃”争议终态隔离，不借成熟loss≠quality原则进Books；冻结候选与潜在2+2+2=6准入保持。精确重开请求：修正配对/边缘桥接、θ几何与式36证明，区分support集中和mode丢失，提供不主动prune的匹配对照及上述实际配置；只重开此命题。

作者实际读18595 v1 §3–5.2、AppendixB–D必要算法/成本/faithfulness，reviewer另核A/F.1–5：SATbackbone给已有可推导literal，LLM从0/1/2antecedents生成新groundedliteral并同LLM commonsense/relevance阈值筛；solver只对加入前提条件entail，不认证新假设truth或翻译忠实。Joint P与全部C一致性不能由各C单独通过推出；票率/weightedconfidence与<25上界内文冲突不采精确recipe。QUAIL unfiltered82→73、CLUTRR correct/incorrect flips与正确答案条件faithfulness不授一般可靠；18.4avgCoT非完整LLM/SAT/prefill预算。2+2+2=6，知识缺口所涉受影响深入，必要Source STOP，Books待Ch79/80具体假设提案与条件推理分责。

## 17676 — Gaze编码与意图

精确v1 §3、§4.1–4.2、§5–6：density为top20%句子，heatmap为词级视觉表示，SVM以4秒26features分类再聚合句子。这是观察→表示粒度→consumer的差额，不是gaze直接等于内心意图。10participants、指定主题的两篇700–800词TOEFL、Gemini2.5Pro与五分之一摘要；sentence指标本身贴近density粒度。Heatmap的ROUGE2局部收益不等semantic指标显著；后续10人三篇within-subject随机方法的低effort报告也不取代显式prompt控制偏好、mind-wandering和Tobii/drift限制。2+1+2=5，标准必要Source足够；可采用不同粒度表示不可互换的局部接口事实。Books具体差异待Ch23比较，非默认覆盖。

## 18157 — Timed entity graph的可回读检索

精确v1 §3、§4setup/4.4、§5/limits：视觉、音频、entity/relations带time及source snippets，SQLite增量写入；查询无结果才逐步放松时间、关键词及关系条件，跨模态子任务共享working memory。抽取/diarization是派生信息，不是真值。EgoLifeQA500MCQ/50小时Jake与manual diarization、VideoMME-long300段30–60min。GPT4.1 BM25→LLMsearch43.9→50.7但125→169sec、172K→571Ktokens；Gemini2.5Pro native在subhour仍好，不授all-long general winner。2+2+2=6，标准必要Source足够。可采用bounded放松资格与可回读身份，不采普遍质量/总成本优势；Books差额待Ch76正文。

## 18345 — Coding trace的观察人口

精确v1 §4、§5.2–5.3与限制：文件config/commit coauthor/branch/PRlabel是不同visibility channels，不自动识别真实model或human oversight。40%以上config-marker repos没有commit，20%ignore config，coauthor取决设置，完整trace可能要认证；AGENTS共享而非Codex独有。作者引用PRArena的Codex86.6/Copilot63.2，在去draft切片中Copilot93.1，说明population gate可能改变ranking；未独核底层数据，不授重现或完整排名。3+1+2=6，评价反证所涉必要深入完成；可采用missing不等unused与draft过滤身份，不采generic adoption因果。Books差额待Ch69/Ch66具体论点。

## 18467 — Offline优化的费用边界

精确v1 §3.2–3.3、§4/5.1–5.2/6.1–6.3、§9：33K真实Internet trajectories过滤SFT与top2/bottom2 DPO仅成熟recipe；offline optimizer不调用API并不让Internet生成免费。在线8B warm-start GRPO50steps约$350、20–30min rate-limit是作者该API人口局部费用条件。Qwen3-8B/Serper/Jina/DeepSeekV3.1 summary与六bench、judge pass1；16–128Kcontext和model-size对照不能将2K与858条数据的异人口结果归因quality。2+2+2=6，标准必要Source足够；可保留在线探索与离线优化不同费用边界。Books具体长期差额待Ch31；不因标准身份直接授Only。

## 18631 — Tool接口变化的训练资格

精确v1 §2.3–4、§3.2–3.3、B.3：format所有step硬门；toolquality0–4分层按turn平均，作者提出正确答案完整奖励、错误答案可获tool部分credit，但§2.3 accuracy1与A.4 accuracy4及加权式未清楚推出一致数值保证，不复制实现。随机tool/argument names与Gemini2.5Flash语义paraphrase改变接口而非新底层功能。Qwen2.5VL7B冻结vision tower/projector；TC cutoffs与TG8Kprompt/20Kresponse/batch32、group std-normalization无KL。Table3及正文实际重读确认：推理引入TC未见A*使navigation44.83→62.33却verification94.2→80，保留task反退；Jigsaw对TC unseen但TG含alltask，不把这一切片称全新任务泛化。2+2+2=6，标准Source足够，可采用tool-schema perturbation资格与asymmetric reward接口；Books差额待Ch78/Ch33。

## 18692 — VLA几何辅助与运行时

精确v1 §4.1–4.2、§5.3–5.5：Qwen2.5VL/actionexpert共享attention+block-causal MoT、flow chunk50；depth queries投影到LingBotDepth token以L1alignment。Actionexpert有不同shardgroups，FSDP/HSDP、FP32reduce/bf16storage+comm与Flex/compile。matched π-like架构/localbatch32的FSDP2vsOpenPI-DDP不等同一通信策略；不照录全尺度throughput为生产SLO。RoboTwin50tasks/2500clean与25000random，depth局部2.06/1.34点支持训练接口而非solegeometry因果。2+1+2=5，标准必要Source足够。可采用depth-token辅助接口，Books差额待Ch26；运行时成熟recipe仅报告，不能把整个报告因小时数纳入。

## 17172 — Contextual demographic审计

作者实际读v1 §3、§4.1–4.3/必要Table3、§6，与peer必要Source一致：SG仅48条且未做SG style/PBI；CRG1320条以gender/age/stance/theme/U.S.region组合。OR/WEAT与formality/emotion分类及agency+certainty+imperative PBI只是语言proxy，不是实际说服。可采用context-conditioned审计人口及指标构念差异，不能授SG→CRG style/persuasion amplification。GPT Table3 p=.075却*与图例p<.05冲突，隔离该显著结论。GPT4o default、Llama3.3-70B/MistralLarge2411 temperature.7/max300；没有intersectional/跨topic/realbehavior验证。2+1+2=5，安全/construct所涉必要深入，Books待具体Ch66比较。

## 17705 — DDR表示比值

作者实际读v1 §2.1–3.1、§4–6，peer已必要Source独核：同token长度/位置对齐的input maxchord distance除output maxchord distance，是特定text pair局部比值，不是全域Lipschitz或semantic truth。500文学摘录1/2/3词同长synonym/random替换，没有human semantic验证；EMD在每种原生score scale上解释，raw DDR和cosine的EMD不同单位，不照录数量级差为质量倍率。可采用同一context表示的input/output扰动对照与消费者条件；可变长度/generalretrieval只是future。2+1+2=5，标准必要Source足够，Books待Ch12具体比较。

## 17471 — Continuous patch循环

作者实际读v1 §3.1–4.3/6.3/7.1–7.4/9相关限制，与peer必要Source一致：已有patch重跑PoV的crash-side与newpatch subsumes stored PoVs的patch-side两阶段去重，worker内静态质量偏好、不同provider并行、FCFS收敛以减少throttle/worker耦合。Alg1L7/11 NOT ResolvedByPatch与正文相反，隔离精确谓词，不发布为验证实现。91%仅successful子集，84/92 success是plausible/testpass非correct；final42submitted/31correct以及unintended14中10不正确说明PoV/test权限。systemd broken symlink使coordinator初始化失败、漏3漏洞，provider ensemble不授无单点可靠性。2+2+2=6，安全/运行约束必要深入；Books待Ch81具体controller/dedup与旧授权论点比较。

## 17915 — Graph belief传播

作者实际读v1 §4.1–4.4/5.1–5.2/Tables3–4/B.2–B.3，与peer必要Source一致：LLM局部belief(label,evidence)/inbox，deterministic controller扩图和changed→reactivate neighbors；final frontier相对discovered graph，不是已证明真正原因。Completeness、sound-policy、connectivity是强条件。Alg22比较全B但damping只label flips，同label evidence文字变化不被k-thresh阻断；B.3独立max-visits5硬预算可采用，不采O(min(kthresh,kmax)|V|)/guaranteed semantic fixedpoint。35ITBench×3/同model controller-only对照支持局部revision增量；不同raw tools与ContextContract聚合不控制全部context，GPT/Kimi输入tokens反而更高，不含reasoning/wallclock。judge entityaliases/reason语义分数不是真实修复部署。2+2+2=6，实际controller长期缺口待Ch79/81具体比较才决定是否深入整合。

## 18491 — Binary safety与fine diagnosis

作者实际读v1 §3/4.2、§5.1–5.3/Table4–5、§6.1/8.2；peer实际全必要位置通过。binary trajectory unsafe强表现不能签发risk-source/failure-mode/harm可靠诊断；FG4B最优failuremode仍32.4%。500safe/unsafe均分、taxonomy合成/工具不重叠split、4judge majority易273/难227、易20%human抽查难双审，是该诊断人口，不是真实部署coverage。FGextra监督未budgetmatch。§6 explicit followingQian的targetloglik Drop/Hold，full-context项在相加中相消；不采内部因果necessity/sufficiency或safe-execute授权。2+1+2=5，安全所涉必要深入足够；Books待Ch66实际binary/诊断分界，非新taxonomy机制。

## 18261 — New-task Fisher硬mask

作者实际v1 §2/3.1–3.4/4.1–4.2与Tables2–3，peer已准入core独核：用新task data经验diagonal Fisher估计→quantile binarymask→输出neuron按input connections聚合→raw gradient逐元素mask，与oldtask Fisher softpenalty不同。Eq4 topα与α=.7“保top30%”及Table2走向冲突，不采用精确mask比例；冻结rawgradient不保证AdamW真实step受限或oldtask不遗忘。Qwen2 .5B/1.5B/7B、TRACE-OP与General average，不把General无样本的优势当通用遗忘证书；αtradeoff与两个aggregation消融局部支持。新增FIM计算/mask费用无统一测得全链速度。2+1+2=5，标准必要证据足够；实际机制差额待Ch29长期抗遗忘与optimizer条件比较。

## 18393 — Privileged字幕融合/音频蒸馏

作者实际v1 §3.1–3.2/4.1–4.4/5.1–5.3 Table2–3，peer已准入core独核：audio局部QFormer聚合形成query，对Donut视觉KV cross-attend；teacher多模态、student音频-only WhisperLargeV3冻结encoder/decoderLoRA，以共同vocab的CE pseudo-label+softKL蒸馏。视觉中人为embed字幕并按goldinterval中帧/裁audio严格对齐，不是自然盲ASR/OCR独立真值。source-video隔离split、中文57小时/英文33或37小时内文不一致，未采统一英文hour；teacher训练fusion/decoder与distill阶段不再fine-tune teacher分开。window64只该slice更好，Table2 student WER10.08→9.86且teacher4.33，不能授小teacher全能力无损搬迁；约5%fusion latency无完整硬件/协议不采生产SLO。2+1+2=5，标准Source足够；Books待Ch23具体query方向与privileged-training/runtime-signal差额，不因subtitle gold来源说无机制。

## 18771 — Typed search/control与write-age memory

作者实际v1 §3.1–3.5/4.1–4.3/5.2/5.5/AppA实现，peer准入core独核：Decompose自然语言dependency traces、Retrieve新文档、Memory旧事实、Conclusion环境summary分责；只prompt自然语言prereq order，不授enforced DAG。S=(trace,context,memory)，memory fact+source/writeTime，更新仅write/add改变recency，capacity保newest不是read-based LRU；training空mem/no跨episode，inference optional跨question保留。Qwen2.5 3/7B、Wikipedia2018 5.9M/100词passages、top5、GRPO4rollouts/3epochs/batch2/16K输出；6datasetsetup与结论7dataset文字不同，不采总数宣传。w/o各组件局部不能等budget归因全部结构，capacity20默认/2Wiki7B capacity15最佳不代表全任务最优；memory reuse次数不是事实正确/总cost。2+2+2=6，标准Source足够；Books待Ch77/79现有typedstate与eviction具体差额。
