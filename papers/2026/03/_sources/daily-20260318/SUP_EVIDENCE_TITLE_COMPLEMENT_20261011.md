# 官方相关标题补检：必要原证与 Books 判断（增量；进行中）

作者 supp_mar18；20完整 exact-v1 AB/root准入已校准；18日级夹证 reader 实核 PASS，15569/14833具名先稿归属隔离。候选不因访问、争议或 No Change 改分；当前只保存实际完成的必要范围，不授其余普通待办或 DAY。

## 2603.14825v1 — Two Birds, One Projection (TBOP)

贡献是blank-image activation差分的安全/utility共享干预，而非领域指标，拟2+2+2=6。作者实际§3.2/4.1–4.3/5.1–5.2/6.2。finaldecoder最后inputtoken，有限anchor差分D的top-k右SVD向量，h−VkVkᵀh；默认k32，不是k1或全生成步。MMSB20%/MME10%另作anchor，其余validation；LLaVAGuard4-12B判ASR、GPT4.1判MMVet，模型7/13B及其它三backbone有限。Table2ETA LLaVA7B HADES3.47低于TBOP5.48，非全指标Pareto；Table4 utility-only anchor MMSB36.54几乎不改，对照baseline亦38.56vsTable2 38.86不同，不合并精确差额。理想Lemma把semantic h*⊥W作为条件，不能由加性表达自动导出；有限SVD不证找到全nuisance或语义不损。HW/precision/batch/concurrency/SLO与完整校准费未披露，60x图不授普遍端到端加速。拟已有覆盖：actualCh23 116–127明确正交加性分解需假设、校准人口/SVD方向bank与在线投影分责、投影不认证事实语义、rank/负视图/旁侧回归和全费退路。blank-anchor是报告局部验证，不足另抄一套bank机制；不采用ideal全语义保留定理，必要同稿校正条件留报告不正面证明。

14825补充直接反侧：非作者实际官C.3/Table9 L555–564核验，攻击后Perspective/Detoxify平均toxicity分仍约56–78、只小幅下降；表头ASR与正文平均分口径不一致，不能把该均分当攻击成功率或授自适应安全。上述限定Source与actual Ch23 116–128已有覆盖已review_mar17_18独立通过，不授ideal全语义保留。

## 2603.14989v1 — MMSpec

贡献是同throughput不同latency及视觉负载使文字speculation退化的受限反证；拟3+2+2=7。作者实际§3/4.1–4.4/5.1–5.2/A.2–A.3。600条/7来源6subtask，Qwen2.5VL7B和LLaVA1.5-7B/10方法/4A100；mainbatch1、maxnew1024、temp0/.6，各method参数独立；precision/concurrency/SLO未披露，非相同draft训练预算，benchmark不核全部任务输出质量。ViSkip max visual attention阈值控制是否draft，target标准verify仍拥有正确性；attention不是grounding真值，score取得/长度M/当前h_t可得性须计成本。§5 max-A而A3称visualattention ratio，.35probe口径未明确统一，不采为精确复现配方。高视觉步accept较低有局部相关证据，不能认定视觉注意是唯一因果。actualCh48 297–315已承载state proposal budget与targetverify/rollback分责、controller漂移与label/cost；969–976视觉证据负载/动态取证/完整target与prefill费用已有。拟已有覆盖，只用负侧支持已存边界，不新写未披露proxy实现，也不授ViSkip lossless已核。必要Source/NC待reader。

## 2603.15599v1 — SmartSearch

贡献是固定预算下粗召回到实际进入context的gold支持坍缩及简单rawpassage路径的反证，拟3+2+2=7。作者实际§3.1–3.6/4Tables3–6/5。rawconversation substring+NER/POS/PRF，可选dense；435M CPUcrossencoder和ColBERT/RRF(.7/.3,k60)，约650ms未绑定完整CPU配置/precision/batch/concurrency/SLO。LoCoMo10conv1540非adversarial四类、LME500六类排abstention，479 inferredgold passages不是客观完美标注；oracleDijkstra单位toolterm成本非全部ingestion/reader费用。rerank+threshold+wordpacking削去gold，98.6→22.5仅其pipeline；Table4 prompt/budget共同改变，Table5为预计算score matrix模拟，3wayfusion/temporal反侧保留，不采普遍+63%。actualCh76 512–590 packing成本/重复/冲突/多样性、597–630 goldrecall固定context和relevance≠sufficiency、126–131证据从可达至实现分阶段，以及1283–1293 ingestion/queryworkspace分支已承载其长期命题。拟具体已有覆盖，不把rawconversation配置外推“结构化memory无用”，不新写启发式αscore公式。必要Source/NC待reader。

## 2603.15183v1 — Token Coherence（争议；Books暂缓）

贡献conditional-access/lazy-invalidation的token传输与authority成本边界，拟2+2+2=6，不因类似MESI关闭。root实际§3/4.1–4.4/5.1–5.3，作者必要核心同范围。网络cache不传artifact≠LLM不消费输入token，§4.4换baseline分母、§4.2仅quiescent、K0仍读metadata不推出消除token节约；AS1无authoritycrash/partition，AS3不允许崩于M，不能授可恢复一致或headline成本。单具名请求同一baseline的网络/模型输入/authoritymetadata完整计费与authority故障恢复协议、对应实际验证；当前Books暂缓，局部protocol描述仅报告，不以成熟原理为EX。待reader核限定notes（root已有实际Source可复用）。

## 2603.15195v1 — Massive Redundancy in Gradient Transport Enables Sparse Online Learning

新增命题是 dense forward 保持、只近似历史 Jacobian transport 的分责，不是普通权重剪枝或 stop-gradient 已有原则；拟 2+2+2=6。作者实际 §2–3、§4关键连续误差对照、copy/adding失败、n256/512、ViT与选择反侧；reader §2–3/4.2–4.4/4.6–4.8/5.1/5.6独核 scoped PASS。full immediate B_t 与 mask J_t 递推、固定 ring/random 循环路径和 ViT 每次重采样 head detach 区分。84%等是 log-space adaptation gap recovery，不是 MSE降幅；n512 fullRTRL数值发散与过参数化使credit不再必需，不能当sparse特有失败；copy/adding没有方法成功且 fullRTRL最差，也不授 sparse 特有因果。UORO的Lorenz反侧、Fisher只在 dense50步后测且时点变动亦保留。硬件/精度/完整训练runtime未披露，masked dense einsum不证n/k吞吐；没有一般无偏或任意方向各向同性定理。actual Ch28 337–351历史influence说明缺这一分责，最小两段PRE已reader逐字正式PASS，待root窄锁。不是论文复现。

## 2603.15590v1 — Effective Distillation to Hybrid xLSTM Architectures

新增同 head 的mLSTM＋SWA512/4sinks/learnedper-head gate及分阶段迁移，拟2+2+2=6。作者实际§3–4.4核心/主预算/反侧；reader§3–4/Limitations/D1–2 scoped PASS。PhaseI仅新增参数MSE且冻embedding/MLP，PhaseII全参数CE.9/KL.1、top256预计算分布；可选同seed域专家按Eq14合并，不借D1印刷20/10权重或B2旧1.3B预算当主配方。四expert各5B总20B vs generalist20B局部可比，但downstream sweep不是独立holdout；STEM合并退化、NIAH长检索反侧和tolerance recovery不授allbehavior lossless。披露8H100、bfloat16操作/FP32gradallgather；H10080GB compile/staticcache的B1/B8微测分prefill/generation，不是vLLM/SGLang并发或SLO。actualCh22 909–940只有逐层保留/完整SSM桥，缺同head两记忆与staged迁移；Ch28 1438–1443 merge/holdout、Ch35 428–439artifact回归已有不重复。两段PRE待确认。

## 2603.15059v1 — Muon Converges under Heavy-Tailed Noise

新增Hölder/有限p矩下batch与step共同制约理想polar更新；拟2+1+3=6。作者实际§2A1/A2、§4.1–4.3核心式/Th4.1；root独立§2/4Lemma4.1Th4.1/3.3与4.3lower/5momentum，限定Source PASS。Ση=∞、Ση^(1+ν)<∞和Ση/b^((p−1)/p)<∞→liminf gradient norm0，不是参数收敛到point。非零noise且固定batch不能满足所列joint条件，batch扩大计费。有限p矩不证实际heavy-tail；lowerbound C4≥0可取0不足严格Omega，compact rank-r UVᵀ与Stiefel满列口径缺桥。中心strict更快/rank适用性具名争议请求：官方修正证明/非零lower条件及实际缺秩polar定义，不正面采用headline。Books只拟jointbatch条件一段，actualCh28 565–680noise/geometry未承载此具体条件；需readerPRE。

## 2603.15377v1 — Beam Search: Width, Scoring, and Reasoning Selection

新增有限负面证据改变“宽beam总更好”判断，拟3+2+2=7，不因NoChange降分。root实际§3/AppendixA–B/§4Tables1–2/§5trace必要Source；作者必要原method与关键对照采用限定范围。每step k条各扩k形成k²，fulltraceNLL与PRM末步正确性评分不同；temp.7的k1不是greedy。3policy(Qwen2.5-7B/Llama3.1-8B/Mistral7B)、MRBEN5975/10domain/3seed、k≤4、单A100周级预算；precision/concurrency/SLO/实际tokenlength未披露，depth24非tokenmax。PRMk4局部改善不单调，NLL宽beam两模型变差。单正确/同均值错误、iid等方差Gaussian、GEV极值均值近似/Cantelli松界不能认证安全或最优宽度，中心具名请求匹配真实相关候选的有限n宽度结论，不采用理论headline。actualCh20 330–350已承载coverage/selection分责、相关错误与selector失配；本次只用此反证，拟已有覆盖，不新写frontier实现。

## 2603.14851v1 — AutoMoT

恢复作者resume_mar18实际读[exact-v1](https://arxiv.org/html/2603.14851v1) §3.1–3.3、§4.1–4.4/Tables4–5及必要模型设置。新增是冻结慢理解encoder的逐层场景KV与快action expert当前KV joint attention，并以落后0.5–1秒的历史RGB场景状态训练异步专家；它给快慢分工一个可复查的有限staleness实例，而非一般模块组合。拟2+2+2=6，保留已校准潜力，不以现有覆盖关闭准入。

UE为冻结Qwen3VL4B、AE约1.6B从头训练，8A100是训练设备，不能当推理hardware。NuSync约80.1K数据构造与一般理解/动作数据不同；四历史RGB、当前RGB/BEV及跨模态条件联合使用，不把联合attention归因于单一cache。Table5同步平均L2 .322/单步延迟.38秒、异步.326/.05秒只支持该局部质量/时延取舍，不等闭环sensor-to-actuation deadline；推理硬件、precision、batch、concurrency、SLO在必要段Not Disclosed。Backbone fine-tuning使planning分18.2→67.8，但Tally81.4→52.4、Info89.3→50.2，反证通用语义保持不是免费；这不是全部fine-tuning必坏或冻结必优。CARLA/Bench2Drive闭环与nuScenes开放循环协议分开，不授实路安全或统一计算预算下的因果加速。训练expert、场景编码/刷新、cache与同步全部付费。

实际owner比较：Ch26 922–941的Fast-Slow正文已承载低频read-only per-layer语义状态/高频expert、episode/instruction/observation/refresh identity、训练与部署staleness一致、刷新/jitter/取消成本和controller安全责任；后续SaiVLA/AR-VLA接口亦区分tensor层级和采集时间。现文不是只有相似标题，而是已解释本次拟采用的分责和失败链。KV concat与0.5–1秒采样是本实验实现点，不足另立通用recipe；拟MULTIMODAL-EMBODIED-VLA已有覆盖。必要Source与actualNC待非writer核，不冒作artifact/实验复现或DAY。

## 2603.14892v1 — PromPrune

resume_mar18实际[exact-v1](https://arxiv.org/html/2603.14892v1) §3.1–3.4、§4.1–4.3/Tables1–6、AppB/C必要范围。新增固定视觉token总预算内，按每图E矩阵的归一化奇异值平方entropy经sigmoid把预算分给CLS saliency与DPP coverage；Qwen无CLS改global average，不是自适应总token数量。拟2+1+2=5。1000LLaVA图校准μ（CLIP .42/Qwen .5744）和τ=.02的局部配置、700 GPT4o annotation群组关联不提供逐图复杂度真值或校准外保证；SVD、Gram/greedy selection和校准都计费。

LLaVA1.5/LLaVANeXT/Qwen2.5VL受测7B、单A40/lmms-eval；precision、request batch、concurrency及SLO必要段Not Disclosed。Table4同64tokens的相对quality由93.6到96.1支持局部取舍，不授无损；Table5 SQA上FPS68.9/FL69.1高于DPP68.8，DPP不普遍优胜；NeXT crop预算仍非已证最优。Table6同320tokens/FLOPs5.02T/KV160MB，Prefill402.7ms却慢于Div388.5/Vis321.1，低于dense516.3不意味着各替代方法或完整decode都更快。

actualCh23 604–634已有固定全局预算→content/redundancy分配→具体selector、整数守恒/下限/校准失配回退、覆盖与局部排序不能互代及DPP只为代理的具体链。按单图谱entropy分两selection配额是该链的局部实现/验证，未发现可采用的独立稳定缺口；拟MULTIMODAL-REPRESENTATION已有覆盖，不抄μ/τ作通用recipe。必要Source与actualNC待非writer核。

## 2603.14938v1 — FARDrive

resume_mar18实际[exact-v1](https://arxiv.org/html/2603.14938v1) §3.2–3.4、§4.1–4.3/Tables1–3及关键预算/反侧。拟2+2+2=6：随机历史horizon后，第二阶段在当前时刻用α将生成latent和GT混合，令后续frame条件读取整个混合history，把训练上下文从纯GT移向自身rollout人口。它重新锚定有限训练误差而非任意sensor/OOD噪声恢复；空间VAE1×32×32、historyKV及同帧control condition cache分责，不能混为无代价持久物理state。

nuScenes1000场景、850/150、SD3MMDiT3.7B；8训练AR帧到229生成帧为离线视觉rollout，不是闭环安全驾驶。Table3 H200和未具名NPU、六view576×1024的每迭代latency/NFE取舍：1step .84秒/FID25.94，20steps3.36秒/FID11.92；关闭KV20steps8.15秒，而FVD80.53对使用KV82.78仍有反退，不采用全质量不变。precision、实际request batch/concurrency、SLO及匹配总训练预算在必要段Not Disclosed；缓存创建/驻留与两阶段训练计费，不合并不同AR单位/NFE的headline。

actualCh25 679–684已有真实历史到部署自产history的分布差异、分别扰动context、自生成结果回写下一段memory、误差反馈与短horizon保守回退；723–756已有causal few-step、self-rollout distill及真实观测reconcile。GT/generated混合是该训练人口转换的有限实现点，未改变现文实际分责；拟MULTIMODAL-WORLD-MODELS已有覆盖，保留当窗机制潜力与全部反侧，不以成熟组合为EX。必要Source与actualNC待非writer核。

## 2603.15432v1 — Gym-V（原队列标签SafetyGym，只指此family）

resume_mar18实际[exact-v1](https://arxiv.org/html/2603.15432v1) §3.1–3.5、§4.1–4.3/Figs4–6/Table4必要范围；必要全文find未见H100或batch size具体运行配置，§4将additional training details延期到supplement，不拿general batch_size接口变量补真实训练批量。拟3+2+2=7：固定底层dynamics，只改变rules/captions/history wrapper会改变视觉RL可学习性，修正仅按algorithm排序的解释。reset/step agent-key dict、规则/obs/output parser、不耗环境步的tool wrapper与RayServe heterogeneous scorer是公开系统接口，不证明其已核实现或全部reward保真。

采用12single-turn+4multi-turn、Qwen2.5VL7B三算法的有限研究。作者称相同compute/hyperparameter，但完整steps/训练hardware/precision/batch及重复seed预算Not Disclosed，不能授matched全生命周期因果。history recent3为上2obs/action对、recent5为上4对，不是3/5张全历史；rules多数有益而Minesweeper去rules更高；caption四任务改善不能证明像素感知已增强，因为添加state描述改变信息权限。Table4 Geometry→Algorithmic−1.1、FrozenLake→2048−2.7保留，不授普遍正transfer/推理层级。179/202环境正文口径不一致，不强造全库存分母，所采用16环境实验单独限定；负reward也非accuracy负数。

actualCh66 230–261已有state可见性vsrules已知的配对测量、history/prompt/信息披露混杂、完整subject身份与protocol wrapper非中性/obs serialization及semantic equivalence；4202–4204另已有scaffold独立intervention。拟采用的测量对象与干预责任已有实际承载，GymV提供局部视觉训练反证而非新的通用RL算法或完整平台协议；拟PLATFORM-EVALUATION-SYSTEM已有覆盖。必要Source与actualNC待非writer核，不授DAY/全套环境/代码验证。

## 2603.15271v1 — Flash-Unified

resume_mar18实际[exact-v1](https://arxiv.org/html/2603.15271v1) §3.1–3.5、§4.1–4.3/Tables1–5核心/全部直接消融反侧。拟2+2+2=6：同一unified weights按理解/生成任务制作不同static FFN mask，保留full path，并在生成时按clock切full/pruned；统一模型不要求统一稀疏artifact。逐神经元置零的DPG/MME敏感度是specialization诊断，actual mask用Wanda weight×activation，生成首图与理解20MME calibration两人口，不把诊断Δ当实际I。高input/output cosine只是layer skip proxy：周期full refresh后缓存skiplist；生成wholehidden与理解lasttoken测量对象不同。CFG分阶段、diffusionhead末层前hidden缓存、understanding浅层inverse Vnorm tokenprune仍各有误差与费用，组合不证明orthogonal无干扰。

Showo2 1.5/7B、PyTorch/A10080GB、lmms-eval/GenEval/DPG有限协议。Table1理解MME1620.5→1560.5、MMStar56.6→48.3，即使MMMU样本latency1.71→.96秒也非无损。Table2 7B GenEval.76→.72、22.74→11.82秒；1.5B .73→.71也有代价。Table5移除layerpruning时DPG85.33/2.91秒，完整84.12/2.80秒，前者质量更高但较慢；不是2.91/2.80倍。另w/oAdaptive83.42/3.92秒才是同时输质量/速度的该组合例，不把两个反侧混并。precision、requestbatch/concurrency、SLO及完整校准费用必要段Not Disclosed；training-free不等calibration-free，首图/20样本不证明任意任务人口可迁移或通用神经元专用性。root指出单位后作者实际Table5定点回核/窄修，Source/PRE限定通过。

actualCh49 529–547已有calibration objective/geometry/clock与可执行稀疏artifact，Ch24 821已有生成阶段capacity schedule，Ch23 1123–1128是训练时模态容量/梯度authority而非部署模式路径。现文具体缺口是同weights的任务模式→不同mask并保留full回退的交付身份；拟唯一INFER-TENSORRT-LLM最小一段，生成clock只交接Ch24，不重复layercache/visualselector配方。逐字PRE在SUP_REMAINING_OWNER_PRE，未授写锁；必要Source/owner/PRE待核。

## 2603.14948v1 — WorldDrive

resume_mar18实际[exact-v1](https://arxiv.org/html/2603.14948v1) §3.1–3.4、§4.1–4.5/Tables1–7关键模型、评价与反侧。拟2+2+2=6：共享frozen visual/motion representation后，训练期由trajectory-conditioned world generator为候选动作产生future target，future queries学latent对齐与BT preference，部署不跑diffusion，而从当前scene/candidate特征直接预测未来latent供critic。不是原文已实现线上真实counterfactual truth，也非仅预测分支训练后全删除。256Kmeans motionanchors+offset、3DCausalVAE、frozen encoder/planner/FAR不同阶段；oracle best6是ceiling而非可部署计划。

Phase1 nuPlan+nuScenes、16A100/batch32；Phase2 NAVSIM、8RTX3090/batch256/50epochs，FAR再10epochs冻结planner。A800单设备53ms对PWM850ms为不同pipeline，precision/request batch/concurrency/tail SLO必要段Not Disclosed，不能授全部匹配费用或production deadline。VAE/vision/motion逐步累计84.9/85.8/86.9不隔离全部交互与训练预算；FAR traj-only87.0时TTC94.3低于baseline94.7，future88.1不证明全指标支配。NAVSIM非反应式pseudo闭环与nuScenes开放循环不同，不授真实道路安全。Table7视频FVD131.7仍高于DriveWM122.7，视觉质量不证明候选critic校准，teacher gen/label/alignment/extra training与部署decoder/critic全部计费。

actualCh25 357–375已有显式imagined rollout/模型漏洞与真实观察责任；953–965已有training-only特权塑形及部署移除预测分支，Ch26 443–469已有future teacher/directpolicy或保留predictedchange token，但未承载“付费teacher候选rollout→蒸馏为部署latent forecast→critic”的分工。拟唯一MULTIMODAL-WORLD-MODELS两小段，动作提交仍交Ch26/真实controller，不复制生成主干和policy算法。逐字PRE在SUP_REMAINING_OWNER_PRE，未授写锁；必要Source/owner/PRE待核。

## 2603.14923v1 — Directional Routing（中心争议，Books暂缓）

拟2+1+2=5，保候选不降分删池。作者§2Eq1/2、§3mechanism、§5/7/8关键评价；reader必要§2–8独核争议隔离PASS。全sequence meanpool得同一r用于所有token，§8明确whole-sequence，未披露prefix-only/只promptpool契约；causal attention mask不自行认证router因果可见性。不是已证明leak；当前必要桥不足，不能正面采causal PPL/cache兼容。unitnorm directions亦非正交（均角75.9°），Eq2不等精确正交投影。1264手写tokens、单训练run、417vs433M非parammatched、MC一胜多退，仅局部报告；seq1024吞吐−13.7%/short128−109%反侧保留。单请求actualrouter可见性实现与prefix-only重新PPL/stepwise生成同协议，Books暂缓。

## 2603.15042v1 — DetShare（当前同家族标题 Vitamin-E；中心争议，Books暂缓）

拟3+2+2=7；author实际§4.1–4.5/5/6关键成本及反侧，reader同范围独核隔离PASS。RCK/stream依赖未披露instruction-block暂停、CTA寄存器/PC等状态协议；dirtyfootprint/reachableclosure未披露缺页迁移/alias并发一致；globalECC/MMU后缺恢复state来源/fencing/faulttest。launch不变不排除intrakernel非确定性，§6也非bitwise语义验收。局部BurstTPOT违例17.77→9.58非0、TTFT4.33→6.37反侧、12%preempt成本，不授strict guarantee。单请求实际暂停/恢复与跨GPU恢复state机制＋故障/同语义验收协议；PLATFORM-GPU-SCHEDULER/Ch63暂缓，不从外部API推不可能性。官方当前DOI实体title=Vitamin-E、arxiv.content/arxiv/findable/active/URL本family；官abs同一v1历史Mar16 09:48:34，首次arxiv日级夹证17已reader核，不用v4正文救v1。
