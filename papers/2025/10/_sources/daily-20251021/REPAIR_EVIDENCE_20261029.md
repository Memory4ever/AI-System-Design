# 本日精确证据增量

本文件只记录实际读到的域；partial不是全文，下载不等阅读。公开日期原件/联合界另见REPAIR_DATE_BOUNDS，当前摘要不倒签v1。尚无新增实现核验/复现或生产保证。

## 2510.15152v1 Tail-Optimized Caching

2+2+2=6，INFER-KV-CACHE。第一必要由writer完成：请求exact-v1 HTML，22秒到300964/532385 bytes后中止；主文§3/4/5/§6.1–6.3完整已到并实际读，附录proof不作全部认证。§3单层cache、按会话增长、只在到达可增加cache，TTFT对未缓存块近似线性，TEL=sum max(TTFT-xi,0)是阈值超额代理，不等percentile。§4以L+Qhat-xi算TEL-safe预算，先trim再LRU；Qhat不是未来已知prompt，原伪码单次foreach减一与充分trim实际实现的关系不能补造。§5定理依birth/death与Poisson、prompt分布已知、跨会话不复用，不能写普通T-LRU对任意线上trace全局最优。

§6 WildChat/ShareGPT取1000–2000 turns回放，Vicuna7B/single A100/vLLM/TP1/no mixed batching；C=10000约4.8GB Float16。Table1在xi500ms有p90/p95反退，正文也说高阈值可增加平均时延/200ms违规；阈值需与实际SLO/percentile校准。上限百分比不外推concurrency、自由生成、租户隔离或端到端成本。选参与prompt预测、cache bookkeeping、重算与回归费用均不能省。原附录/代码未核，不声称可直接生产替换。

实际owner检查：Ch45 Eviction/Offload正文当前有“少增加未来重算时间”的衰减复用×重算成本段、后接hidden checkpoint恢复；没有显式TEL阈值下的safe trimming与mean/tail反转。此为具体待PRE差额，不用主题相似签已有覆盖。邻接段已读，尚未改书。

## 2510.15231v1 Partial YaRN/VLAT

2+1+2=5，MULTIMODAL-REPRESENTATION。writer实际读精确v1§3、§4、§5、§6、§7及Limitations；主体完整200/271993 bytes。统一输入空间、single audio输入，在audio区域对低频插值/高频外推并缩放旋转幅度，text原坐标保持；text→audio交叉logit仍变，所以保留text位置不等text能力无损。VLAT为每样本抽虚拟源长度再映射到实际音频长度的双向位置增广，不是增加真实内容或声学信息。

SALMONN88与Qwen2-Audio750 tokens/30s均由Whisper分块；YODAS2英文MCQA由Gemini2Flash生成，每长度750题，生成者也参与reference，非独立开放任务评价。v1 Table1/§5明确Whole/Partial胜负随模型/长度变化，按实测2min而非标称30s作伸缩锚点可能更重要；VLAT实验是2min训练/10epoch qkvo LoRA、视频级split，不能与1epoch直接长音频适配混成同预算优越。Whole YaRN在VLAT中diverge是此训练设置观察，不是一般不可能。§7/Limitations说明两个超参选取额外费；MCQA不能充分检验文本保留/生成能力。未采用开放任务无损/免费扩窗/完整runtime加速，未核代码/复现。

实际owner只完成局部检索，尚须读Ch23完整相关位置/邻接，不能先签NC或整合。

## 2510.15339v1 AutoGraph-R1

2+1+2=5，AGENT-RAG。writer实际读精确v1§3/4/§5.1–5.4/§6/7，22秒到289939/454380 bytes后中止，必要主文已完整到达；不是全附录。冻结retriever/generator，只RL训练graph constructor。carrier用judge看gold answer能否由检索triples推得的binary reward；index以gold supporting passages的recall给reward，经triple similarity seed PPR。两者优化不同消费者，不能将图内自洽/下游QA分当来源事实真值。

Qwen2.5-3B/7B与Llama1B/3B，GRPO/two H100，fixed Qwen2.5-7B reader/Qwen3-0.6B embeddings；carrier训练无distractors，index有hard negative/15docs，运行两种reward不能算同人口唯一因果。基线同prompt zero-shot constructor，新增RL/重建图/检索和judge费不免费。Table1 Llama1B-ToG的NQ反退，Table2 Llama3B-HippoRAG2的Musique反退；Table4 Qwen7B carrier的HotpotQA Acc98.50→97.53，即使F1升也不支持所有精度无损。DeepseekV3 judge的intrinsic指标不是独立事实审计。未采用普遍fact保真、所有retriever迁移/全SLO或代码已实现。

实际owner：Ch76已承载graph builder proposal与structural-credit不能改provenance，以及固定ranker反馈必须绑定consumer；仍须读完整相关两侧后判断是否还缺carrier/index目标分流，尚未签NC/整合。

## 2510.15041v1 GDGen

2+1+2=5，MULTIMODAL-WORLD-MODELS。writer实际读§4.1/4.2.1–3、Algorithm1、§5.1/5.3及Tables2/3、§6；partial267224/310904，必要主体已到。神经场由rest geometry输出低维handle weights，重建observed deformation后预测各向异性stiffness，以能量/reciprocal regularizer/噪声negative约束动力学，不是只为静态场景画新视图。最低能量本身会退化为零stiffness，1/E是必要额外项；原N(1,0)噪声式和Chamfer下标render不补recipe，regularizer不等exact orthogonality或真实物性可辨识。20帧预测、不同baseline输入/表示能力不全matched；不处理原生collision，须外加penalty，不支持cloth/hair。仅采用observed dynamics到可交互近似状态的接口，不授任意物理真值/安全/全形状泛化。未核像素、实现或复现；完整费用/hardware/precision/concurrency未就所用段披露，不引用性能倍率。

## 2510.15042v1 COLIPRI

2+1+2=5，MULTIMODAL-REPRESENTATION。writer实际读§4.1.1/Table1、§4.2/Table4、§4.3.2/Table6及§7；partial435876/473843，不冒全部附件。长报告与短正负prompt造成条件分布差额，sentence shuffle/LLM shortening作用于训练人口；native zero-shot平均50份已知正/负report embedding，不等无标签zero-shot。生成目标用unmasked headers时，section mask长度可泄露病灶，改为headers前置+固定mask数；与CLIP/MAE联合不保证多目标互补。Table4/6 retrieval上升而probe/native或short分类退步，原文亦承认confounders，故不能把更多目标认证普遍语义更好。这里只采用训练表示与实际consumer/prompt形状须分验的机制/反侧，不采诊疗或全任务优越；设置§3.1/5.1的CT-RATE/NLST与外测配置已W8实际补齐，必要层R15通过；owner比较另行。

## 2510.15047v1 SPA

2+1+2=5，MULTIMODAL-WORLD-MODELS。exact-v1标题Internalizing World Models via Self-Play Finetuning for Agentic RL，与current改名分开。writer读§2/3/§4.1/4.2/4.4/§7；§4.3曾输出不完整，已W8单独完整恢复并经R15关键复核。先自交互收trajectory，却以环境ground-truth替换thought中的current/next状态再SFT，后PPO只优化策略；不是纯自信生成即真实world model。格式与坐标真实分责，随机坐标同格式会collapse，self-belief SFT低于GT方案；SFT去掉状态loss的对照不等唯一因果。Qwen0.5/1.5/3B、Llama1B、三text games不同grid，batch32/8rollouts，RL1000steps；更多SFT epoch额外计算，不用相同RL预算证明同总费。Stochastic/format fragile，不能由显式预测标签或Pass@1提高批准真实环境正确。未核代码/复现。

## 2510.15056v1 Model-changing actions

2+1+2=5，窄机制潜力；writer实际读§2/3、§4、§5 Lemma1/2及Lemma3 statement/证明开头，partial311497/436703，尾部未读。上下两级分别选择transition kernel与primitive policy，配置有独立成本/episode reset，有限kernel集合及已知reward是实质前提，不是普通动作自然拥有改环境kernel的权限。§3小扰动线性化后(7)未保全(5)概率非负/≤1约束，且对policy共同最优不由固定policy线性化自动convex；Algorithm1上层更新也未显式扣§2定义的C。Lemma2对mu0与value-error用两个infinity norms界内积，遗漏维数/dual norm：uniform mu0与全1误差向量内积1，右侧1/n，故不能采用该普遍误差界及依赖传播保证。采用仅“配置动作/普通动作及配置费分责”的formalization，中心保证争议不自行修论文；不引用性能/最优性。无需为不采用的全部proof扩读。

## 2510.15061v1 Antislop

2+1+2=5，TRAIN-DPO（推理sampler为上下文）。writer实际读§4/5/§6.1/6.3/Table2/§7。完成pattern后回退起始token再降概率与重采，soft escape可放过同token，不是硬安全filter；backtracking使吞吐作者称下降69–96%，不能当免费约束。FTPO只训被拒首token与一组替代token，target/non-target logit MSE分责，不由单点logit tether认证其他上下文分布不变。DPO同pairs但beta/停止与高rank局部LoRA配置，Llama70B需仅lm_head且抑制率更低；Table2 Gemma2k的MMLU/GSM8K/longform下降，不能写无损。creative-writing与模型judge协议不支持一般事实/安全毒性消除；构数据、LoRA与全部重采/评价付费，未核artifact/复现。

## 2510.15068v1 SCJ

2+1+2=5，PLATFORM-SECURITY；安全影响域深入。writer实际读III/IV/V-E/V-F/VI，完整原件179011。只保多图序列会把分散意图重新组合、单图过滤与sequence-aware过滤的消费对象差异，不复制操作提示。1556选中queries、11模型、GPT4评分5/五次取max的ASR不是单次自然流量风险或真实有害行为；同文V-E的PT1数值59.79与62.89口径不明，不合成因果增益。各模型/guards精确快照、生成资源与全部成本未完整披露，图像数与prompt变化亦混杂；TableIII与IV是作者受限过滤对照，不证明所有视觉系统必有同缺陷或guards无用。未查所有图片/代码/复现，不授安全保证。

## 2510.15568v1 Spark Effect：C重开为窄P

2+1+2=5，PLATFORM-EVALUATION-SYSTEM。writer按R7只读§3.1/3.5、§4/5/6：对同一human输出，judge均值10.22超过1–10rubric，与human8.90不同；仅给machine一组clip并不能让human/machine量尺一致，同一judge也不保证跨population bias抵消。这是具体可修正比较的反侧，故旧C理由撤销。六任务/七任务统计自由度与persona八/十计数冲突保留，+4.1/+4.76/+5.69不同分母不混；不采用persona真实创造力/可靠显著提升或生产效果。未知底座/硬件和全部调用预算不补值；只用这份局部越界/裁剪观察，不认证所有统计推断。未核raw telemetry/实现/复现。

## 15495/15843 撤回

DataCite精确DOI原件dates明确Withdrawn：15495为v2 2026-03-25，15843为v2 2025-12-09，arxiv.content/findable；不是仅Other请求。当前官方撤回身份不入选、不评分、不入Books，保历史v1登记与后来撤回各自日期，不把2026/Dec撤回说成Oct20事件。无需再为正面采用读Methods。

## 15416/15429 精确v1准入修正提案

15416当前AB为30adapter/多步composition，但actual v1§3/4/7/8.3仅5adapter、语义prompt路由→已有LoRA调用/General fallback，未展示独立的新选择算法、跨adapter更新/组合语义或受控失效边界；收益主要来自输出更短且不同适配数据，不认证SD/kernel净加速。拟当前P→对应v1 C（不是因小样本/费时关闭）。现有组合用于新domain不够；若后版有具体重要delta另归版本事件。writer已实际核§3/4/7/8.3决定域，不重读无关场景，25queries与hard2/6等冲突不补。

15429旧“based-on/汇编即可C”提案被R15明确拒绝，已由W12/R18真实决定证据取代：大学完整PDF20/21页（印刷6/7）恢复四章Origins，与Ch1.2四类贡献逐项对应SIGIR2023、CIKM2024、RecSys2024及LOOP2503.00897。后三精确原paper DOI均findable/arxiv.content，registered分别2024-07-30、2024-05-10、2025-03-04，均给本窗前公开最晚界；大学award Oct13不是公开日。未辨本次汇编事件新增delta，R18据具名更早原paper同意关闭此事件，而非因thesis体裁排除。未审原paper不冒已审，有具体新增章节/修订只重对应事件。

## W10 writer后组精确v1必要包

以下均读本日REPAIR_BODY精确v1，非当前摘要、实现或复现。只采用所列必要主体，不冒完整附录；未披露配置不补值。分数均2+1+2=5，15455/15596为实际跨执行边界2+2+2=6。此处先保存真实证据，Books仍须实际owner比较，中心争议不由分数/关闭池掩盖。

- **15388 SWFP**：§4、5.2/T1、5.4/6。JKO局部flow块配soft critic，有限粒子旧位置并行更新，区别精确无穷小JKO。印出的平方W2三角界少系数：距离1+1的平方4并不≤1+1=2，故不能从该步批准并行有限训练单调/稳定保证。T1 offline局部CalQL59>SWFP57，非全胜；有限控制任务、critic/采样/flow训练预算绑定，不授通用LLM/RL保证。HTML266164/277034部分；中心界限隔离，具体flow方案仍有潜力。
- **15414 MARS(v1，非当前MARSHAL)**：§3、4.1、4.5/T3–4、6。按角色先积累回报再归一与按token/turn归一改变长度权重，不能把v1式当一般无偏GAE；混入格式/长度/游戏内奖励，不是纯终局目标。Qwen4B有限双人游戏/1000局，跨游戏与消融单格有反退，不证明通用合作。辅助尺度冲突不自行修复；训练/多agent rollouts全计费。
- **15425 ParaFormer(v1，非当前TeamFormer)**：§4/Alg1、5.1/5.3/5.5。并行branch均读x0、聚合器渐进更新，是换计算结构而非原顺序层免费并行。存在性UAT不等有限宽度训练收敛、原函数等价；300epoch/CIFAR/Fashion/ViT12或24、8A6000最多6rank，架构/硬件预算同时改变。PF1分支精度反退，不采用all-depth-unneeded或统一倍率；渲染算法训练/推理语义不完整，不补实现。
- **15455 CORE**：§3全、4.1、4.2/T1–2成本尾段、6。本地看到全UI，按布局block择送cloud并按需增补，subtask/history仍可能泄露、最终可能全送；不是DP/执行安全。exposure指标以same-action/same-screen匹配人口，Qwen-Max敏感元素标签非真实泄露真值。Honor/Pixel/Android9或13、GPT4o20241120、本地7–9B量化Ollama/4090D；成功率低于全cloud，media/payment有不减暴露格。少cloud推理不等净速：端到端DroidTask1.52–1.61×、AndroidLab1.49–1.66× baseline时延；cloud token还可1.10–1.15×。全部本地推理/交互/隐私回归付费，不采“减少上传即安全”。HTML178260/395489部分，必要主体已到。
- **15456 temporal-causal PRM：更早正文，非本日首次事件。** 首读§2/3/§4初段后，官方精确v1页首明确“peer-reviewed version ... PMLR236:643–664,2024，请引proceedings”，出版方同名/四作者/相同摘要及正文下载记录已定点核实：[PMLR](https://proceedings.mlr.press/v236/corazza24a.html)，01–03 Apr2024。raw为REPAIR_EARLIER_15456_PMLR_20261029.html。此已知更早正文优先于arxiv联合日界；本次无具名重要修订信号，不计Oct20候选、不评分/Books，不为未采用实验重全篇。不能称其无贡献，也不移到其他Daily处理。
- **15516 KD dataset size**：§3、4.1/4.2T1、5.1T2/5.2/5.3、7。κ区分student/teacher数据比例；同student配置下larger-teacher成本另付，2/3数据KD可更低效。label smoothing不能解释全部KD，不等推翻一切平滑理论；vision/language CKA差异只相关，FOOD有退步。Languini-GPTmini/CIFAR人口与全部teacher/student训练成本绑定，不采任意任务KD必优或普遍缩数据。
- **15545 Token-Timing**：§4、5.1T1/5.2.3/5.2.5、Limitations、A.1–3已到部分。DTW多对多对齐不自动给proposal pushforward概率，MapProbabilities未闭；Alg2拒绝后直接采target q，而附录为residual(q-p)+，不是同一无损算法。二元p=(.8,.2),q=(.2,.8)时印出算法输出(.32,.68)≠q。保候选对齐接口，中心精确分布保证争议隔离，不补改作者算法。25pairs/480生成及不同model默认decoding不等matchedSLO；CPU重分词/DTW/同步费用不免，TLI有更优pair，不采lossless净速。
- **15596 PRISM**：III/IV/V-A1–2，完整187570bytes。DAG算子Gaussian/serial方差和/parallel CDF乘积依独立性，pipeline MonteCarlo不补相关jitter保证。64H200实测验证与64k+采样/20rank投影分开；KS20.8%和mean.85%为不同误差指标。节点p95放置与kernel方差削减是模拟反事实，不是实际部署收益，internalschedule/normalizedRTT限制外部审计。可保variance-criticalpath设计判断，不能签all-scale分位保证。
- **15647 Critic-LLM-RS**：Sx3、Sx6 datasets/baselines/对照、多轮与调用时间。冻结LLM，BERT critic消费用户history预测item评分再反馈，区别只自评但不等真实偏好；MovieLens/Book各10k用户80/10/10分割，20history+1item；无真实rating的评价使用Oracle，不冒真实用户验证。额外轮次不再增益；只计LLM invocation排除critic不等wholeloop预算。训练critic、全迭代与独立用户评价均付费，不能据更多推荐分签真实偏好/通用agent可靠性。
- **15679 HEADER**：IV-A完整/IV-C privileged reward/V-A至C与T1。给新节点固定localcommunity，局部密图+全局疏图、softguideposts，再A*/Dijkstra/TSP；不是全部构图/寻路线性。GT map训练reward，GT不是线上权限；单调距离假设不证明全目标等价。RTX4080/16h/16env，Scout/Ouster1m/s/1Hz，人工屏蔽楼梯/边界不授自主安全，gap减少50%不等绝对准确率。图/感知/规划/重训费用均保留。
- **15683 SBMoE**：III、IV setup/T1、V关键/VI/VII，完整223898bytes。post-transformer检索表示专家，top1训练，推理有TOP1/ALL两个variant；所述all-experts仅ALL分支，二者索引/质量/费用分别验，索引身份需重建，不把稀疏训练说线上少算。小DRM收益/大Contriever反退、epoch20/30/CS10和单seed42，不认证同预算普胜。100k activated docs为语料阈值非per-query计算，TinyBERT专家数也非越多越好。只支持受限检索表示容量取舍。
- **15691 factors/news**：3.2完整、S4/A3.C4、A1/A2。独立predictor后按上一步误差softmax目标/逆KL训练router；训练用r不等推理泄漏r。A1明确额外假设p与ζ独立，正文命题没有显式列出；不能指控作者完全无假设，也不能在共因输入/残差下一般应用该方差式。A1还承认mixture与standalone残差不同，A2只是均匀prior/固定方差条件的ELBO解释。DeBERTa/LoRAr4、2A100/10epoch/b32/4k、商业NA/EU/EM新闻、2023–24 holdout、月度回报，无滚动重训；只采解耦训练条件，不采因果稳定/投资收益建议或普遍优越。
- **15700 ProofOptimizer**：§2/3.1/3.2、4.1/4.2、5.2。验证后更短candidate/expert iteration与test-time参数更新分开，145k有效proof/307k前训/32B teacher成本不是无训练数据。印出reward(|y|-|x|)/|x|对valid更短为负而invalid0，与最大化冲突，中心RL recipe争议，不擅自改号。@1提升可伴@32多样性崩塌，executionrepair不胜重采、短proof仍可能更慢；heartbeats排除imports非wholewallclock。Lean仅证明固定statement，不授NL题意或所有执行加速。
- **15728 RLAF**：§4/5、6/7关键完整，warehouse106–144另补。DFA加权subgoal/distance或teacherQ造偏好，再rankingreward/TD3；ranking不认证数值reward误差，policybound依coverage/误差/探索等额外前提。四grid与MountainCar/warehouse合成全观测，不是实仓；warehouse12维、6×8、5步骤，所谓realistic不等现实验证。动态只部分环境更优；teacher/启发式权重/训练仍付费，不采reward-free、partialobservable或部署安全。
- **15731 diffusion sinks**：§4/T1、5/8。diffusion模型的sink位置会随denoising变，平均归一A∈[0,1]却印阈值epsilon3，未澄清不能补完整检测recipe。T1firstsink Dream GSM8K .82→.79为3pp而非全<1%；10sinks LLaDA .76→.55/MMaDA .54→.37，不能把sink视免费可删。因果/并行解释是hypothesis，MMaDA复现失败/不同模型初始化预算保留，不授所有无用attention或通用裁剪。
- **15804 truth encoding**：§3/4/5.1–3/6。一个共同truth-bit造两个事实共现，正交embedding/均匀attention/单层norm下特定W可线性分离并调预测confidence；不等真实LM天然独立真值。§4已单独完整恢复：无norm时无相同separator，ρ1且学习QK后反会忽略context，syntheticρ1不再出现，是明确边界。5seed合成训练、balanced probe/ρ.99训练人口不同；CounterFact128/LLama3-8B/layer11/α3只是受限steering；MAVEN falsearticle聚类有styleconfounds，不签全语料truth方向/因果事实性。
- **15831 VISTA**：§2完整2.2另补、§4开头/4.1关键。保原prompt、生成多个variant、incumbent进入双向tournament；visual/audio/context各normal/adversarial/meta critic再改prompt，换序冲突判tie不消除judge偏差/循环偏好，不认证真质量单调。Gemini2.5flash-preview0520+Veo3preview；MovieGen100/内部多scene161；5轮每轮30video，VSR++等按视频数匹配但不等judge总费用。训练免费不等test-time免费；未采用未到达humanstudy/附录/普适安全。必要有限机制/对照与直接反侧足以保受限P，不把同judge自动评估当独立人类偏好。
- **15862 PokeeResearch**：§3/4/5全、完整main。研究/验证循环允许tool失败后继续，RLOO true-onpolicy多样本反馈；selfverification不是外部证据，AI semanticjudge给gold并非impartial真理。Qwen2.5-7B-Instruct、MiroRLGenQA/140step/b64/k8/100turn/32768context，无KLentropy；10bench每125(GAIA103)，1228题/4threads，Gemini2.5FlashLite mean@4非pass@4。Table1优于作者所列7B但基线Base/Instruct选优、tools有异，不证明每个component因果或同总预算。原例selfverifier对已有正确回答的措辞反复未增证据，更不能把自检通过当实际独立验真。全部搜索/读取摘要/验证/训练付费；不回签当前摘要的更强能力或跨系统净收益。
