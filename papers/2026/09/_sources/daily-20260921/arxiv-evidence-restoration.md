# 09/21 arXiv 有限证据恢复

本文件记录本次实际阅读，不继承旧“25篇完成”。首发来源为 Mon21 官方可见批次；更早同族例外另列。未复现实验，单篇准备不等于日级 Gate。Ch72 判断前补读了项目背景、学习理念、写作指南及Ch71/73相关交接。

## 2609.21484v1 — HE-Guardrail

- 来源：[官方 v1 HTML](https://arxiv.org/html/2609.21484v1)；实际读 III-A/B（Eq1–7）、III-C/D必要实现、IV-A/B/C/D。根任务已独立校准完整题摘，正文采用尚待非作者复核。
- 评分：`2+2+2=6`；真实保护行为变化深入例外；Evidence：作者方法/受限实验，不是普遍密码学防泄漏保证。
- 新约束：HE隐藏输入和输出，使服务方无法明文判guard。密文gate选模型输出或refusal；近似sign/CKKS的非零gate仍能泄露被压制token坐标，作者再加gated随机noise。Pre-guard双模型packing与intra-guard复用隐状态是不同成本路径。
- 边界：semi-honest server，恶意client仅选择输入但遵守HE协议；目标Llama3-8B、CKKS/desilofhe、两H200、输入2048/预算200。LlamaGuard一请求两lane令容量改变，不能把额外guard当免费。单次噪声示例没有建立任意重复查询下不可恢复界；decision一致性也不是guard语义正确性。
- 实际Books差异：Ch72“隐私不是一个开关”已有FHE/MPC明文边界与代价，未有密文response-return控制及近似gate残余分支。建议在该节两段后补条件分支，保留明文gate适用区间及复杂度；不得写“已阻断所有泄漏”。目前为**待协调的精确书稿提案**，尚未实际整合。

## 2609.21515v1 — ServeGuard

- 来源：[官方 v1 HTML](https://arxiv.org/html/2609.21515v1)；实际读§3 setup、§5 Theorem1–4、§6/6.1 Theorem6–7、§7、§9及对应numerical范围说明。根任务已独立题摘校准，正文采用尚待非作者复核。
- 评分：`2+2+2=6`；保护合同深入例外。具体命题是公开linear monitor的盲子空间，非一般后门不存在。
- 机制：LoRA read factor `A=C M` 令新增value update `B A`不读取`ker M`；ZK验证committed relation，package绑定write factor/层身份；持权重consumer对实际served bytes做integer-lattice admission。base残余保留，head-local与joint-Q/K monitor范围不同。
- 边界：编码恒等式不自动覆盖浮点matmul；Q/K/O/MLP不在该value-path证书内；hash hiding、soundness与challenge条件分开。公开base预处理、证明、load-check均有成本；不具备可信监测范围/装载完整性时，来源验证与behavior red-team仍共存。
- 实际Books差异：Ch72“从文件哈希到可执行来源链”已有provenance、host sandbox与行为probe，却缺monitor-relative的adapter结构约束→证明→actual-byte admission分工。建议紧接“模型文件本身也不能只靠provenance...”段落作替代分支，不替代普通安全Gate。当前**待协调书稿提案**，不冒称实际写入。

## 本次重新对账的既有三项

| 精确来源 | 实际阅读与正文位置 | 作者侧处置 / 尚缺 |
| --- | --- | --- |
| [Reviser20830v1](https://arxiv.org/html/2609.20830v1) | §6–8必要动作/训练/限制；Ch24“Autoregressive 不必等于 Append-only Final Text” | 实际已写机制保留，2+2+2=6深入gap例外。动作历史trunk与可变canvas别混同：KV/rollback为工程identity推断，实验未用canvas encoder。待根任务非作者源/body核。 |
| [Kernel addressability21058v1](https://arxiv.org/html/2609.21058v1) | §2–6必要operator share/oracle/exploit；Ch49 addressable fraction与scale-invariant correctness正文 | 实际已写机制保留，3+2+2=7深入纠错。写出比例、相对误差/不变量与工程sentinel加强区分；不把A100/BF16局部scope升级生产。待根任务非作者源/body核。 |
| [DLB21079v1](https://arxiv.org/html/2609.21079v1) | §2–3实际root/leaf探测、在线模型、离散/流式routing；Ch56异构routing正文 | 实际已写机制保留，2+2+2=6深入gap例外。drain proxy是近似，内部部署不是通用SLO。待根任务非作者源/body核。 |

## 2026-09-30必要证据接续（不以摘要替代）

### 2609.20845v1 — ZENDAYA

精确[官方HTML](https://arxiv.org/html/2609.20845v1)的§2–3固定/流式日程、§5/Table3–4、AppendixE/TableA3和Limitations已实际读。暂定`2+2+2=6`标准，真实Books对照待做。可见prefix闭式日程、单调attention mask和先到达才可用的window长度输入共同给条件化因果保证；固定日程依赖输入总长估计，不自动成为端到端实时保证。流式Corollary1使用arrived horizon与前window信息预测长度；异步到达只是证明，作者只测window-synchronized。

29M decoder、4层/768/8 heads、冻结CLIP-B32/C3D/Whisper-base，TensorFlow单T4、各语料截断与greedy EOS，不能外推大模型或live service SLO。wait-k与ZENDAYA的长度head训练职责并不完全对称；learned adaptive policy未head-to-head。流式为single run，Table4 test-clip bootstrap不包含optimization noise。AppendixE三seed明确推翻Table2 ActivityNet原最佳gamma与“全sweep优于baseline”的说法：适宜区域移到0.4–0.7，性能幅度顺序也反转；LibriHeavy差距在seed spread内。保留这些修正，不把闭式预算定理写成所有语料质量收益。

### 2609.20888v1 — Elastic Threshold Attention

精确[官方HTML](https://arxiv.org/html/2609.20888v1)的§3.1–3.3/4、§5.2/5.3/5.8/Table4、AppendixG与K已读。暂定`3+2+2=7`深入设计反证，owner/写入决定待核。post-RoPE query预测threshold；训练multiplicative sigmoid把sub-threshold logit收缩到0，留下exp(0)背景floor，推理hard pruning改softmax support，二者非精确等价。G.1的饱和近似需要logit充分远离threshold，单有S≥tau不足；G.2的126M/C4/1024实验top1match80.29%、relative L2 shift22.77%只给局部alignment，不证明任意query/长上下文保持输出。

K.1 full-covariance Cantelli与finite-population条件是条件化上界；K.2实际kernel用diagonal variance surrogate，作者明言quantile estimator且有false negatives，不能把surrogate当certified maximum。GQA物理HBM搬运按query-head block union，不按单head sparsity算收益；all-pruned top1 rescue只是数值防护，不恢复全部语义。Table4/H100-SXM80GB/FP16、Hq32/Hkv4/dim64、64K–512K计kernel+chunk reduction+metadata。质量所在约38%head-density点固定block b64，不同batch/length配置为0.72–1.12倍dense速度；这里不是不同block width比较。2.5倍来自10%head-density/coarser b128的另一点，不能拼成同质量收益。from-scratch1.45B/42B-token训练与未来7B–70B计划分开，未独立复现。该条件由root必要源独立核纠正，actual Ch14及正式Report已经采用修正后的条件。

### 2609.21525v1 — IncentRL（重开后贡献关闭）

精确[官方HTML](https://arxiv.org/html/2609.21525v1)§1–4.1实际读；root独立§1/方法核通过关闭。固定finite discounted MDP、full-support q给bounded outcome-KL cost；uniform q偏好outcome entropy而非必然predictability。Prop1 value-loss≤beta*Cmax/(1-gamma)，Prop2需unique optimal-action gap及严格weight界，ties可在任意正beta分离；Prop3是discounted累计cost的large-weight极限，非贪心瞬时KL。§1明言这些是standard bounded-reward perturbation而非新general-MDP理论。MiniGrid distance sigmoid proxy不等calibrated outcome law；Beta外循环fresh PPO search不是Bayesian posterior，缺simpler-distance/KL-specific信息匹配对照。关闭原因是没有在成熟原则之外建立额外长期机制，不是按小模型、无LLM或成本拒绝。

## 其他单篇实际必要阅读（仍未终态）

- QuAKE21407v1已读§2–3 state-space/后验/solver handoff、§4.1与Table1/Fig4。1024校准/不重叠5000评价、SVDQuant W4A4、20步DPM-Solver++及四类所测模型；FID/KID相对full-precision参考而非真实数据，FLUX/PixArt部分ImageReward退步。A10040GB/BF16 CPU-offload影响成本比较，不能采用泛称无额外延迟。Ch24旧freshness/covariance论证不能直接作为Kalman-history改写的完整覆盖；校准/消融成本必要段及最终处分仍待，不假造完成。
- Drift21113v1已读§3–5关键EAP/patching与cross-task实验。EAP为一阶代理；作者有corrupted activation intervention，不能误说全无干预，但不能据此承诺完整因果真值。Books位置仍待Ch29/Ch5具体命题比较。
- OmniVChat21465v1 HTML失败后，实际从[官方PDF v1](https://arxiv.org/pdf/2609.21465v1)读到p1–7，52页总数可核。§2的reply/reference来自accepted rendered audio-video，不能用生成script作ground truth；§3 tier-gate依赖评分与fixed reference-history final-turn评价，human probe360只single-turn、不测live interruption。§4.1是Qwen3-Omni-30B-A3B Thinker/GSPO/LoRA64/1000iter、每32input×4reply；这不自动证明native路径latency收益。后续取p8–10连续两次HTTP读取在7,340,032字节截断，方法已可得，reward/结果仍普通恢复待办；不得写整篇无法访问。
- TinyCeNN21139v1、WeightIsOver21849v1、DiaVLo22008v1、MDL22043v1各必要机制/反例已经实际读到，具体locator与限制在[补漏裁决](./arxiv-title-abstract-screening.md)，当前不能依据部分读取自动给Books Existing/Integrate。
- MintAct22083v1必要§3.4.1–3.4.3/Table2、§4.3/Table6–7已读。实际Ch33现有mixture control缺消费quota/生产背压分权，已形成[精确Books提案](./books-queue-restoration.md)；待非作者必要源/owner与真实写回，不把量化修正或混合控制冒充同一合同。
- 其余题摘准入信号仍须必要证据与真实owner判断，不因本文件存在而标完成。

## 2026-10-01 有限接续：20849 SPARE

[exact-v1 HTML](https://arxiv.org/html/2609.20849v1) §2–4/Tables1–2/Fig2–3/§5实际读到必要范围，`2+1+2=5`标准审阅。潜在增量是训练期sequence-initial register对齐final conclusion的SBERT embedding，而非“用了audio CoT”或榜单；REG只读先前context、后续token不能读REG，训练aux目标和部署forward分开。§2.4部署同时撤REG/projection head，不把训练期target embedding当推理可用oracle。SALMONN13B（Whisper/BEATs/Q-Former/Vicuna）、160k train/40k validation AF-Think/Youtube8M、MMAU/MMAR、SFT/MuToR对照；硬件、精度、训练步数、匹配总搜索预算 Not Disclosed，表中±的重复单位未说明，§4.3的six random seeds只明确用于attention分析，不补成表1六次独立训练。

必要反证：Table2原叙述把两个多register variant概括为55.43，但真实Chapters summary为52.18±8.95，Multi-conclusion为55.43±.12；两者都不是单register的稳定替代。λ=3有更大方差，不能“robust”升级任意λ。回答attention更偏音频是观察，不是音频反事实/patching干预；SBERT最终答案目标并不验证答案由音频支持，不能据权重图唯一证明audio grounding或排除文本shortcut。zero added inference head/token是设计事实，未测生产latency/SLO。

日期定点已读[ISCA同题作者正式页](https://www.isca-archive.org/interspeech_2026/bonzi26_interspeech.html)与官方conference首页：会议为Sep27–Oct1，页面没有单篇首次上线时间。Accepted本身不证明更早首发；当前同题/作者身份核实，但不能将会期当上线时刻，也不因此更改Mon21官方公告归属。若取得正式页更早公开archive，只重开该family日期。

actual Ch23:501–503 的PEARL两段已具体承载“完整含答案专家轨迹只作训练期表示目标、部署撤预测token/工具恢复普通前向、匹配隐状态不证明环境状态/实际执行”。SPARE从工具轨迹hidden目标换成最终答案SBERT目标，REG隔离读写确是本材料具体配方，但其长期训练/推理分工与目标非ground-truth边界可由此承载；attention解释新增证据不采用为因果。作者倾向 E承载该长期分工、局部recipe/benchmark仅报告而不重复写书，已交root校准，**尚未独立最终判定**；若root认为mask单向aux supervision仍有独立长期缺口，再仅补该缺口，不因已读成本关闭或偷换为I。

2026-10-01 root 独立必要§2.2–2.4/Table2及 actual Ch23 PEARL对读通过，终判 E：仅采用 train-only answer-target、部署撤aux≠真实执行这一长期分工；REG单向mask为具体recipe，不新增普遍原理，attention仅观察不采因果。`2+1+2=5`标准完成，无需Books diff。

## 2026-10-01 20844 最小准入纠正

[exact-v1](https://arxiv.org/html/2609.20844v1)必要决定准入范围为§4/Algorithm1、§5 DetailedSettings与Table3。失败trace的URL扩展上下文可能缺答案支持，方法用同题成功trace的compact evidence补入，保留困难干扰而非仅重放成功例；同总RL steps对照显示移LongQA至末、去KL、去失败QA的不同取舍，具备可核验的目标切换/困难样本增量。此前题摘“只有数据换长/指标”的拟关闭不足，改为窄准入 `2+1+2=5`标准，不自动深入或改书。各配置三次evaluation并非三次训练；same steps未等价same tokens/tools/训练compute；successful final answer也不能证明每条展开网页都支持，URL重访/64–128K截断可改变证据。仅据上述确定准入，训练预算/评价条件与 actual owner 处置仍普通待办，不把初筛补读记为全部审阅完成。

## 2026-10-01 21407 QuAKE：校准/理论/成本必要范围补齐

本轮直接补读 exact-v1 §4.1–4.2/B.3/AppendixC–F，与已有效§2–3/Eq1–33原文结合，作者必要停止点已齐，拟`2+2+2=6`、因真实长期gap深入。§3估计的是同当前quantized轨迹latent状态上所需的full-precision denoiser-output window，不是原full-precision整条采样轨迹的真state；posterior同时修正window里的当前和历史entry给原solver。AppendixD以x₀-domain/log-SNR Lagrange extrapolation构成affine transition，startup只有valid entry、history不足减阶，不把未观察槽位当真实历史。

AppendixC每step/channel聚合spatial位置，FP轨迹同latent状态配对FP/quantized输出校准gain/bias/observation variance和process residual；broadcast参数后按element独立修正，不估crosschannel/crossspatial covariance。B.3非Gaussian仍LMMSE需finite second moments、噪声相互及跨时间不相关、与initial state不相关和校准状态模型成立；不是任意误差下完整Bayesian optimality，也不认证quantized rollout分布仍满足FP校准关系。离线同时运行两个denoiser与1024样本有成本，全文必要设置未给该校准总时长/多次独立训练不确定性，记Not Disclosed，不拿“不改网络”当零预算。

§4全部修正方法同W4A4 SVDQuant backbone、同calibration/eval/sampler/noise/20步；TAC/QDrift是作者重实现非官方核验。AppendixE仅主backbone量化、VAE/encoder原精度、模型分辨率/CFG不同；Fig4单A10040GB单image，BF16用了CPU offload，只支持quantized-with/without corrector的局部额外开销比较，不归因全部BF16→quantized加速给QuAKE。0.25MiB是FLUX calibrated statistics，不称全部posterior/runtime峰值。FID/KID相对FP生成，不是真实数据分布；AppendixF UniPC的FLUX/sDCI KID QDrift .168优于QuAKE .180，不能延续全solver/每cell最优宣传，IR也有退步。采用method/history-consistency分工及反证，不给通用quality guarantee。

actual Ch24:1383 freshness 与1387–1389 reverse-covariance/Lanczos只承载state agreement及reverse-kernel covariance，不是量化输出window的posterior修正。真实增量/两段提案在 [Books队列](books-queue-restoration.md#2026-10-01-21407量化-observation-与-solver-history-共同修正)，root独立source→owner/写锁仍待，不改当前日报完成数。

## 2026-10-01 第二组局部准入与标准处置准备

**22068 CodeMidas**：[exact-v1](https://arxiv.org/html/2609.22068v1)Method§3.1–3.3实际读，构造任务不依issue/commit，从public entrypoints/observable outcomes取scope，剥selected core保shared dependencies，reference保原程序。声明未规定的细节只验约束，不固定private structure/措辞/顺序；private assertion无behavior substitute则reject。隐藏verifier仅grading注入；cleanup清compiled/cache/原tests，还须执行一致性检查。这是source-only数据生成选择而非仅成熟模块组合，作者确认窄准入`2+1+2=5`，必要filters/预算/对照仍普通待办；不作原程序oracle完备/规模归因保证。root已纠正拟关闭理由，当前不默认deep。

**20850 MME-Safety**：[exact-v1](https://arxiv.org/html/2609.20850v1)§3.3/4.1–4.3/Table2/Fig4及limitations实际定点读。RelR/HR/conditional AHS/RefR与composite，aux IdR/RsnR/AltR unweighted DIS、自报modality usage共同作profile；CoT/size比较有不同版本/架构混杂，不证明reasoning导致普遍防御破坏。§4.3的H-H并非最易攻击、M-H有更高harmful输出，但没有固定实例只改stealth的受控干预，不识别filter机制。root独立§3/4.3/Fig4核后确认前代SIUO已建立跨模态benign/harmful，当前新增分层profile未给新的跨模态控制成立边界，故具体贡献前关闭通过；不是benchmark一律拒收，不评分、不进入候选/Books。

**21139 TinyCeNN**：[exact-v1](https://arxiv.org/html/2609.21139v1)前轮IV–VII与本轮VIII–IX补核。逐层当前student校准、接受层冻结/失败rollback、NLL与局部表示四门并验为具体localconversion；作者明确不是新sequence mixer。forced-accept SmolLM2 layer3因果实验、component ablation/threshold/multi-seed/full Qwen anchors仍future work；Qwen四任务每50仅200项28.5–32%vs30%只是sanity、非rank优势，reference kernels更慢，研究wrapper use_cache=False不作runtime加速。actual Ch49:1300–1316 Learned Kernel candidate→bounded fragment/verifier→registry/rollback，以及1350–1352 correctness vs interface identity分账可承载一般admission原则；但不宣称四个CeNN gate已经被书完整实现。作者拟标准`2+1+2=5` Only：这是局部结构转换案例/未完成因果及运行性能，不改变当前长期部署选择，不因小模型或已读成本关闭。待root必要源/真实owner有限peer。

**21849 Weight Is Over**：[exact-v1](https://arxiv.org/html/2609.21849v1)前轮§3–5必要源复用，本轮Table1/§4/§5/Table3再核。共享Qwen tokenizer、冻结FLUX.2-klein transformer/VAE，0.6Bencoder+187Mtranslator posthoc拟合4Bfeatures；小translator语义漂移/塌缩，24PartiPrompts matchedseed LPIPS/CLIP并非全语义验收。Table1BF16 PyTorch/MPS timing与CPU attention fallback，Table3 RTXPRO6000Blackwell/TensorRT-RTX/1024²/4步不可合并。4B BF16与0.6B+translator BF16总时延均.47s、step105ms，VRAM15.1→10.6GB，encoder不在critical path；FP8/NVFP4的.34/.27s主要transformer路径，不能归给translator。缺多独立训练/大prompt覆盖/并发SLO。actual Ch23 encoder/projector:55–66及Ch24多artifact/近似reference原则只是接口与验收，不等于这个recipe已有覆盖；作者拟`2+1+2=5`标准Only：posthoc替换有局部资源数据，但未形成跨条件新的稳定选择边界，不为该pipeline operating point再改书。待root必要源/actual有限核。

**22008 DiaVLo**：[exact-v1](https://arxiv.org/html/2609.22008v1)§4.1–4.3及本轮§5/§6.1–6.2实读。SK由IETrans生成后human verify/expand、专家修正；RK由self-rationale抽取，真实internal fidelity仍future work，遮蔽/DML不能授予完整内部groundtruth。四VLM7–8B/四受限切片、两A10/default/greedy/max256；520workers每sample单annotator，初始1996丢242≈12%因空输出/不遵指令，coverage不能省略。阈值依encoder、人工600pairs；100random splits的median causal estimate不等100训练seed。actual Ch66:148–151来源provenance/受控cue/self-report分工及714–718 cue interventions不证隐藏真实因果链，承载该采用边界；诊断recipe仅报告，拟`2+1+2=5` E仅指self-report与权威reference角色，不声称书涵盖所有SK/RK分类。待root有限peer。

**22043 MDL**：[exact-v1](https://arxiv.org/html/2609.22043v1)前轮§3/5/必要Tables与本轮§6 limitations/§7。正交三signal编码、heuristic calibration/fouractions为局部controller，不学新参数不等零预算；geometry不认证reliability或grounding，overall hallucination高于RAG而risk-weighted改善，high relevance高risk117项decision55.6%、Active residual8%反证近零普遍保证。matched任务/coverage/action人口须分开，系统只披露作者0.14ms路径非任意模型服务SLO。actual Ch76:318–325 geometry必须最终任务验收、729–740 prior/authority/confidence分权已有明确命题，但不能给其四action配方Existing。拟`2+1+2=5`标准Only：heuristic配置与局部operating point不建立新的可迁移控制条件，保留负侧，不因只‘框架’拒准入。待root必要源/actual有限peer。

### 2026-10-01 上述四项 root 终判（替代提案）

DiaVLo E通过，只采用actual Ch66:148–151/714–718的authority/self-report分工，不是全recipe；MDL标准Only通过，保未校准heuristic、整体/risk-weighted异向及提取预算。TinyCeNN标准Only通过但理由修正：已测layer3 NLL通过而局部NMSE/cos失败是有效观察，不以未来forced-accept实验抹除；actual Ch17:361–395已经分别拥有干预、相似与任务评估，四阈值转换尚未给新质量/运行选择边界，不用whole4gate Existing。

Weight作者原Only判断漏掉§4/Fig3明确fit/non-fit取舍，已受影响重开深入、仍5分不为I改分。作者fresh补读Fig3，root必要源→actual Ch54:311/348–366核与literal通过，批准精确窄锁后实际Ch54:368/370两段写回；root独立读364–374与source marker，写后PASS、释放锁。真正采用命题是非critical组件占用可改变整个pipeline working set，适当释放encoder可避denoiser paging；96GB全fit时streaming更慢，2Wmax+Amax不是通用下界。40×限定作者4070Ti12GB/1024²/4-step配置的denoising latency，translator24prompt只受限质量、扩大建议不冒充已测；相同BF16总.47s不变，Table1 MPS与Table3 Blackwell/TRT不合并。最终I，不继承旧Only，也不重做无关附件。

## 2026-10-01 CodeMidas 必要证据与实际终判

[22068v1](https://arxiv.org/html/2609.22068v1) §3.1–3.4、§4–5.2/AppA必要支持及反证完成。public entrypoint与observable scope在没有issue/commit/tests时提供任务来源；原实现只定义声明固定的reference行为，未规定细节只验constraint，不能转behavior的private assertion拒收。清理compiled/cache/oldtests后fresh两次base fail、四次reference pass，四solver review查假阳/假阴，adversarial rollout查泄漏shortcut，frontier有成有败只适配training，不能判断全过/全败原因或verifier完备。§4 MiMoV2.5 GRPO32×32binary、prompt8192/response516096/500turn/staleness8等作者配置；§5.1 high-quality1k/3k/5545与vanilla8k同config/step0–70却联合改变cleaning/consistency/three filters，无独立组件归因，也非tokens/tool/construction模型预算匹配。§5.2 verification行为+4.2pp CI1.8–6.6是matched task/checkpoint关联；exploration+.7 CI−1.9–3.7、draft+1.95 CI−.04–3.96不采稳定收益。训练/构造GPU精度总预算未披露，未复现实验。

root必要primary与actual TRAIN-DATA Ch27:480–535确认真实gap，5分因gap深入，不为I改分。精确fail→pass后/Builder前两段已获锁并实际Ch27:532/534写回；root鲜读523–545，publicscope/reference、private拒收/canonical、fresh-start、适配非真值与整包归因边界均写后PASS，锁释放。原PR/Builder/PolicyRelative邻文保留，source marker唯一。正式可计I，不等于日Gate。

## 2026-10-01 当前三单元：source→actual owner 的有限提案

**Drift21113** [exact-v1](https://arxiv.org/html/2609.21113v1)，`3+1+2=6`设计反证深入。§3–5、必要AppF/Table5–6与AppJ/Table8实际读到停止。四base GPT2small/Qwen2.0.5B/Llama3.2.1B/Llama2.7B，六数据集(SST2/Yelp、SQuAD/CoQA、KDE4/Tatoeba)，每type30k，fullFT不同batch/epoch/length、bf16 single A10080G约14GPUh；不是同task/model恒预算比较。attention KL/logit-lens decodability与EAP一阶edge score分开，top400 corrupted activation intervention比随机400损伤大，不能说全无干预。不同task corruption severity不等；输出head probe不能推出早层没有信息或core capabilities未受损。24异类task pairs的overlap/degradation相关不是全部独立样本，AppJ保护shared组件的两model九pair恢复是更强局部证据，但relative gain不等pp、缺seed/不确定性，冻结更多参数亦改变capacity/optimization，不证明唯一中介或安全模块。

actual WORLDVIEW-REPRESENTATION Ch5:182明确可迁移几何/局部行为作用/任务泛化分别验收，190–214 correlation/prediction/causation与localized intervention階梯，230–232充分性非唯一/跨任务外推限制已经承载拟采用的三对象分账；不说现有书已写过EAP全部数据。作者拟窄E，只采用drift/readout、局部干预重要性与跨task transfer不可互推；具体局部实验/冻shared修复配方仅报告，待root必要peer，未正式完成。

**L0-MoE21672** [exact-v1](https://arxiv.org/html/2609.21672v1)，`2+1+2=5`标准必要§2–4/Limitations/AppA.2已读。CCM BGE-M3语义聚类+重排为expert形成提供domain人口；samebase冻结nonMLP、hard-concrete gate逐步retention收缩，独立FFN之后router/experts token联合训练，两loop domain-distance×domain-cyclic batch不是部署按domain直选。30Btokens/21sampling iterations/64experts/2.8Bactive，却总23.3B；Table4 8experts总4.8B/4.6× MMLU50.9，64总23.3B/2.5× MMLU70.4，资源/quality不只active count。FSDPZeRO3 noCPUoffload、所有baseline SGlang，但模型不同训练/retention和baseline预算、speed batch/length/hardware未充分披露，不将same engine作端到端公平证明。Table3CCM/kmeans/dynamicbatch/四替代compression有局部对照；same-domain curriculum与token routing exposure bias、expert差异未独立测/冗余、70B未测，作者futurecode不当实现已核。

actual MODEL-MOE Ch21:629–631 joint route形成条件人口≠预定义domain、641独立compatible experts/shared coordinate/router校准及深层feature exposure、651–666domain-selectable module需要objective/population/deployment合同，已经承载拟采用expert形成与runtime routing/部署语义分工。作者拟窄E，只覆盖独立formation/shared interface/额外router exposure验收；L0/CCM各公式、64expert/局部speed数字不是全recipe Existing，待root有限必要peer。

**BrainAPI21299** [exact-v1](https://arxiv.org/html/2609.21299v1)，`3+2+2=7`设计纠错深入；§6–7与§11.1–11.7必要已读。Gatekeeper49templates/69instances/180objects外部原verdict；scalar grammar仅3/49，bounded All/Any+membership28/49，37/42五exemption错需per-element condition（不是whole-object guard），后42/42只encodablefragment19admit23deny，另9case因casefold/nestedquantification未测。10对alternatives20trials说明selection≠admission，Gatekeeper更广且正确不能声称优越；decision artifact10/10rederive仅其record不是policy/真实execution全验证。Cedar differential CLI由作者cross-product请求，defaultallow向defaultdeny/permit-and-no-forbid须显式polarity和conjunctive guard；crossentity字段比较24/35statement不支持、仅8/35conditions能编码。81requests78agree中71denials全对、allows7/10，三timed允许被保守拒绝；不将deny-heavy aggregate当可用性。context/ranking未评，多步regulatedworkflow未实证。

actual AGENT-PLATFORM Ch84:46–49/489–511有typed primitive/独立policy/reference monitor及effect-algebra形式范围；695–707列identity/authority，却没有跨backend default polarity、量词元素guard scope与supported fragment迁移的具体失效链。作者拟I在Policy与Agent Identity列举后/NIST句之前两段（未获锁，不写）：

> 把不同 backend 的规则接入同一 policy layer，还必须保留默认判决、量词作用域和组合优先级。Admission 的 default-allow 与 authorization 的 default-deny 不能只换字段名：允许规则在前者可能没有改变判决，而后者通常还要求存在 permit 且没有 forbid。对每个 collection element 的豁免也不能移为整个 capability 的 guard；否则同一文字规则会改变允许集合。先声明受支持 fragment，对无法表达的聚合、嵌套或跨对象关系显式拒绝或交原 backend，再以外部允许和拒绝样本分别校验。
>
> 一个受限 prototype 的跨域测试暴露了 scalar grammar 与 default polarity 的缺口；Gatekeeper fragment 修正后42个样本一致，不证明49条原策略都可编码，Cedar的81请求总体78一致又掩盖了10个允许请求中的3个被错拒。保守拒绝只限制误放，并不拥有可用性；标签仍依赖 reference implementation，context/ranking与多步 execution 尚未实测。迁移因而支付规则编码、版本与差分回归成本；语义不相容时保留既有 controller、人工审批或只读 fallback，不凭决策 artifact 的可重算性证明真实 effect 已受完整治理。

三项均已source/actual最低必要对读。2026-10-01 `sep22_resume_v3` 非作者有限核已通过21113与21672的上述窄E：直接核精确v1必要方法/干预反证与实际Ch5/21，仅采用三对象分账、expert形成/共同接口与部署语义分工，不为整个配方给Existing。21299仍待独立采用裁决；以上不是日级Gate。

2026-10-01 root必要v1 source→actual/literal及实际写后通过：Brain Ch84:711/713两段已落实，default polarity已限定为所用backend，不泛化全部admission；element guard/fragment与外部reference、allow-deny分账均保留，unique SF与exact-v1 URL绑定，窄锁释放，正式计I。

## 2026-10-01 DLD-RL20844 必要审阅与数据owner差额

[exact-v1](https://arxiv.org/html/2609.20844v1) DLD方法/Algo1、Experiment Settings、Tables1–4/ablations必要实际读。Search Serper top10 snippets、Visit Jina另summarizer，重新fetch同URL展开fullcontent；successful/failed两种trace均保留、failed expanded corpus补同题successful compact evidence而非注入gold answer，q/a*保持原任务。正确答案reward只是sufficiency线索，参数记忆/偶然猜对仍可使其不充分；再fetch的web修订身份与摘要/原webpage支持关系需保存，不能声称URL相同语义必然不变。DR→no-tool LongQA→DR切换objective/availability，warm reference冻结KL.005约束tooluse遗忘，不能声明不遗忘保证。

DR-Venus4B-SFT与Qwen3.5.9B DR-SFT、REDSearcher queries，batch8×8、same total RLsteps不等相同tokens/网页/模型judge/summary/构造预算。DeepSeekV4Flash训练/评价同judge潜在共享误差；每benchmark三次test不是三次独立训练。DR150turn/128K/max9.6K perturn、Long128K/max32K，中间截断first64K+last64K；硬件/precision/totalsteps/pairedcompute未给。Table3 noKL提高Long却降DR，移Long最后Long更高DR更低，除failedQA都退，支持这组目标/人口tradeoff不证明唯一中介。Table4 BrowseComp **Avg Search反而两backbone均增加**56.62→57.22/47.96→49.57，只similar-search比下降和Visit次数升，不照录fewer queries/省工具成本。百万token1.5M仅100URL构造长度，主训练64–128K，不当百万token能力验证。61.6%是强LM分类1000错误的related diagnostic，不是机制因果归因。

actual TRAIN-DATA Ch27:412–430有evidence graph/search trajectory合验、494–499有failure label分层，987–989有entropy-based支持与distractor构造，但没有工具rollout重新编为无tool长输入QA、failed噪声人口补同题successful证据后的任务对象变化；Ch29:988–996有证据链拒答/答案目标而不是DLD目标切换。作者拟5分因真实data gap深入I，不重复维护GRPO loss：Ch27 search lineage/source24850之后、Synthetic API State标题之前最多两段。拟写如下，**未获锁**：

> 同一搜索轨迹还可被重新编成另一种训练对象：把 compact snippets / Visit summaries 展开为对应页面全文，保留原问题与答案，但移除交互工具，让模型直接在长输入中定位并组合证据。失败轨迹保留较难的噪声人口；若补入同题成功轨迹的 compact evidence，则补证负责可回答性，不把失败动作变成示范 target。新的样本应绑定 rollout、页面修订、摘要与补证来源，答案正确或 URL 相同均不能单独证明展开后的 evidence 足够且忠实。
>
> 这个转换以网页恢复、长输入 token 与额外训练阶段换取原工具 RL 较少获得的长上下文监督。作者 DR→LongQA→DR 的同总 RL-step 对照中，去掉中段 KL 或把 LongQA 留在最后会提高部分长输入结果、却损伤搜索任务；目标切换和最终 realignment 因而应分别验收，不给普遍不遗忘保证。测试重复不是训练重复，同 steps 也未匹配构造、token 与工具总预算；可疑网页、补证不可靠或 tool-use 回归时，保留原人工/可重放数据、直接工具 RL 与独立证据审查，不以最终答案 reward 代替 lineage Gate。

2026-10-01 root必要v1 source→actual/literal及实际写后通过：DLD Ch27:432/434两段已落实，接source24850后/Synthetic API前，failed补证/重新展开lineage、目标切换/KL、预算与fallback均保留；unique SF与exact-v1 URL绑定、窄锁释放，正式计I。当前官方abs的Submitted Aug5原值仅是提交字段，不替代本日Mon21 New公告归属。

## 2026-10-01 OmniVChat21465 必要PDF恢复与窄采用提案

[exact-v1 PDF](https://arxiv.org/pdf/2609.21465v1)直接大文件/分段读取有限失败后，官方 `export.arxiv.org/pdf/2609.21465v1` 成功取得11,067,399bytes完整52页，后续必要p8–10、D.3 p23、E.1–E.3 p25–26已实际读；**不是外部blocked、不是全52页无差别审阅**。前p1–7方法证据合法复用。采用版本仍v1，不用current替代。

方法参考来自accepted rendered audio/video而非原script；fixed-referencehistory multi-turn仅评分final targetturn，不构成live rollout/interrupt。Training Eq4 rubric+format.5+efficiency.1+style.5，word/Chinesechar计length不是token；within-input minmax效率、equal .5会group中心化消去；format恒1没梯度，不据存在term归因收益。Table1 no-eff Mean.697/Human.691反高于full.652/.632，但word36→99/RE18.38→7.12，是质量/简洁tradeoff；no-style Mean.661/Human.632与style.788保反向，不采全reward各自均改善。

Qwen3Omni30B/3Bactive Thinker+LoRA64α256325M，冻结vision/audio；GSPO noKL,32×4,1000iter,1e−6,2FPS≤16frames/clip，prompt11072/reply1024 budget排除34/5600trainrow不得省略分母。560dev选940，synthetic heldout2800无trainvideo重叠，Human360真实录制只有12singleturn类别/30各、全Chinese，caption需人工修speech漏项62/360。共同textjudge/rubric生成不消除共有偏差，Human不测multi/liveSLO。E.3 ablation同1000config但checkpoint选择可见eval子集不完全同，hardware/precision/完整sampling construction wallclock未披露，不外推latency。

D.3 六judge同固定Gemini3.7回复，仅2773/2800全部valid用于paired；pooled与Table1perreplymean不同。κ.532–.845、fullgated agreement65.8–88.7%，0.01differences对boot/regrade尺度要比，不能把共享judge说成humantruth。D.4 single/multi独立sample，不能认多轮因果衰退；recordedrank不由syntheticrank唯一决定。

作者拟`2+1+2=5`标准窄E：MULTIMODAL-REPRESENTATION Ch23:21–41 content/modality/coordinate/artifact identity与丢失信息须绑定raw/transform版本；PLATFORM-EVALUATION-SYSTEM Ch66:277–280 cohort→render→prompt→call→annotation identity、375–378 history作为独立干预对象，已承载参考依据实际render和固定history条件人口的长期分工。不能宣称书已有完整Studio/reward recipe；tier gate/效率/style实现及局部数据仅报告，不重复写书。该E不以topic为据，若root认为accepted-render reference相对原script仍有独立长期缺口则只补差额。2026-10-01 07:21：sep22_resume_v3独立亲读该exact-v1必要机制/关键反侧与上述实际owner，窄E通过并同步正式日报；只采用本段明确命题，recipe与局部数字不作整篇覆盖。

## 2026-10-01 CoVer21208 / ArenaFlow21378 必要范围

两项完整exact-v1题摘准入已root独立PASS，本段是其后必要证据，不是重开其他inventory。

**CoVer21208** [exact-v1](https://arxiv.org/html/2609.21208v1)，暂`2+1+2=5`标准，actual新机制缺口若确认再深入受影响。§3–4/Limitations、B.6、C.3/Tables9–11、D.4与E.4关键反证实际已读。single-policy coder/tester co-train：coder的y由GT tests fraction定义，tester用pass-vector与y的pluginMI且Cov>0 gate；constantpass/anti-discriminative归零，binary y early低entropyvsgraded不是无GT verifier。三filter invalid/inputstring/executioncolumn，后者仅当前m candidates的行为非重复；invalid不足k会重新入尾，不能说全部test永远valid。所有K候选需执行才能知道profile，选择不省这部分execution。

Qwen2.5.7B/14B，CodeContests≤difficulty2 split4.5ktrain/239eval，其余四bench只eval/CF去重；m16/K32/k16，350steps/2B200，1e−6/KL.01/clip.2/temp1/topP1。Table3 same m×K budget但k16rewardvs全部K32，不是定k随机抽样纯控制；Table4 A1替换pass-rate/A2 binary/A3coder-only同steps不等总compute。B.6 CoVer7B72GPUh vs coder-only46GPUh（35.94vs33.50），14B96GPUh，不zerooverhead；4evalseed和twoindependenttrainingrun明确分开。C.3最高passbucket GTcorrect86.8%非correctness证书，E.4 aliasingbug通过16全部selected但GT4/8失败，问题是缺copy→update→query深度非列重复。baseline有backbone/publicbudget差别、precision未给、deterministic sandbox5s/512MB、OOD/GUI/distributed不在支持范围。

**理论重要nonproof**：D.4方差式需共同variance/相应相关结构，删去ρ=1重复不能独自证明任意剩余集合平均MI-estimator相关更低；distinct binary execution columns也不等Ihat彼此独立。它改变tester群组reward人口，单testMI估计仍以m codes为sample，而不是k tests。离散plugin无binning不等有限sample偏差消失；不采原文“any policy严格降方差/no bias correction/零开销”普遍表述。原本文公开机制与局部对照仍可支持受限选择，未据此把全部经验结论删掉。

actual TRAIN-GRPO Ch33:470–479说明tests specification/heldout/adversarial，497–511有verifier相关性/非完美oracle，但没有**可学习test producer应按GT锚定的区分信息而非passrate奖励**的机制；拟I在heldouttests段之后/GroupSize标题之前两段，待root有限necessary/owner裁决及锁：

> Verifier 本身由 policy 生成时，奖励 test 的通过率会诱使它只出容易通过的题。一个有外部测试锚点的分支先用 GT test 的部分通过比例衡量候选代码，再奖励 generated test 的 pass/fail 向量对该比例的区分信息，并用正 covariance gate 排除“更错的代码更易通过”的反向信号。Code producer 和 test producer 可以共享参数，却不能共享正确性自签权；有限 GT suite 仍定义训练锚点，测试信息量也只相对于当前候选人口。
>
> 先生成较大 pool、执行后按输入与行为列去重，可以改变 tester 更新人口，而不会消除完整 pool 的生成和 execution 成本。不同列不保证独立或完整语义覆盖，不能由去重推出任意有限样本的严格方差下降；作者的非退化16-test suite仍漏掉需要多步操作才能暴露的aliasingbug。实测 co-training 增加总GPU预算，matched steps并非matched compute；人口或锚点失配时保留fixed GT tests、独立adversarial tests和coder-only分支，最终代码仍须按部署任务重新验证。

**ArenaFlow21378** [exact-v1](https://arxiv.org/html/2609.21378v1)，`2+2+2=6`标准，§3–4/AppB必要实际读。Tournament preference r→group-centered A；judge定位winning rounds的pivotalsteps，用expdepth/withintrajectorymax归一g，仅A>0时加A*g，不能说每winner每step必获positive强化。Depth是启发可靠性指标，nontransitive偏好/seed/greedy anchor可能改变先后，不causalimportance。All16rollouts共用retrievedskills，judge归因每query累计再在retrievedset居中z，runningmeanU/n≥5且U<0退activepool；没被归因相对mean可负，不等skill错误/事实删除。Memory元skill由finalchampionpairwise summaries合并/versionreplace，utility和semantic truth分账。

Qwen3.8B/Qwen3Max、120steps Adam1e−6、8H20、8groups×16rollouts/top3skill，ArenaRL directRL，其他coldstart+RL不同训练起点；samebackbone/judge不能抹去SFT成本。Table3组件拿掉/均匀depth有局部减益，非全部budget匹配；AppB N16/G8成本表1.97Mtoken/248calls/1h22 vsArenaRL1.52M/240/1h16是作者此设置，不当完整120step aggregate未说明单位。200pair/3human majority F1step79.5/skill76.1，是判断一致不是反事实/causal验收；未给独立trainseed/CI/precision/完整外部API成本。top3最佳→top6降43.6、utilityweight过大降，不能通用固定k/.2。DeepResearchBench100任务跨22域不意味着科学应用扩本项目范围，本项只处理Agent学习机制。

actual TRAIN-GRPO Ch33:193–213局部credit proposal与verifier方向分权，AGENT-MEMORY Ch77:142–148 content-level credit≠causal truth/写入authority及609–636 trajectory→versioned Skill/evaluation/admission，已承载拟采用**judge credit只能调节优化/skill写读proposal，不证明pivotal因果或skill真值**。作者倾向窄E（非wholeArenaFlow公式已有），具体depth/positive-A倍率/居中utility recipe与局部对照仅报告；若root认为relative preference→正向局部credit的条件仍是未覆盖长期分支，再只补该差额。必要证据已齐，均待root独立finitepeer，未计正式完成。

## 2026-10-01 CommitFlow21908 / AutoViewMem21940 必要范围与实际差额

两项exact-v1完整题摘准入由root独立PASS。本轮补齐当前方法与评价停止点，未扩大发现池；提交时间仍只是原始字段，归属沿官方Mon21公告而非Submitted18Sep。

**CommitFlow21908** [exact-v1](https://arxiv.org/html/2609.21908v1)正式题名 *CommitFlow: Semantic Commitment Verification and Local Correction for Long-Horizon Robot Manipulation VLA Execution*；暂`2+1+2=5`。III-A–D、IV-A–E已实际必要读。Frozen base生成H动作chunk proposal，SCM用RGB-D metric与GRU历史预测stage/event/holding/support等，与adapter声明前提/维护条件比较；required unmet或violated只扣住dependent动作，Correct优先于Keep。规则标签/condition BCE不是环境因果或开放感知正确性。BoundaryFlow按当前状态与base action训练专家残差，六joint兼容arm的uncentered SVD低秩r12/K10，cmax tanh界只归一动作坐标，不是物理伤害界；Correct mask不修改受保护通道，nominal无修正。RGC以offline成功calibration P95 relation region、短prefix FK预测和ordered gain候选选最小预测可行值，必须fresh实际观测确认才能cross checkpoint；无可行解hold/recompute，不全局最小干预/形式安全。

11 RoboTwin每task100随机trial；TableI只十共同任务75.9 vs53.2为22.7pp，TableII十一任务72.8 vs49.4不同分母。III observer1971frame/6streams MacroF1仅分类，非commit安全；TableIII six-task Fresh+Ours80 vsFreshBase66.8/FreshIK69，但IK Cabinet61→57。跨base LingBot ObjectScale96→93，不普遍改善。IV-C regrasp局部恢复109/238、100/150与最终成功43/238、70/150分别记，不把localrelation修好说成整体完成；更大alpha Cabinetovershoot20.4mm。IV-D sameinteraction换对象只重绑relation，head不变两task；IV-E实机两task各100trial50→63、40→50，无独立重复seed/CI、hardware/precision/训练与在线成本完整披露。Comparator训练人口不同，冻结base不等无额外训练。复杂接触/避障/regrasp/全局规划不由局部residual补出。

actual MULTIMODAL-EMBODIED-VLA Ch26:759–781已有postcondition→next-skill readiness/accept-repair-abort与controller evidence，382–397有freshobs验证subgoal pop，1218–1222有前提authority placement；这些不是新贡献。具体差额是**在单一action chunk内只hold依赖effect的通道/时段、冻结base余进度与局部relation residual修正并行，并在真正cross时用fresh evidence再验**，不是笼统commit一词。作者拟5分因gap深入I，仅在readiness通用contract两段后/训练控制语义漂移段前两段，待root必要source→owner/literal及窄锁：

> Next-skill readiness 还可细化到一个 action chunk 内部：对当前阶段必须建立或维持的物理关系声明 commitment，只扣住依赖未成立效果的动作通道或时段，让仍有效的基础动作继续。冻结的 base policy 仍提出剩余动作；独立 monitor 用当前观测检查关系，局部 correction 只修改获准通道，预测可行的短 prefix 也不能替代跨越抓取、接触或释放 checkpoint 时的 fresh evidence。这样把“阶段名称已经切换”与“所需效果真正成立”分开，不把 monitor 分类准确率当作环境真值。
>
> 一个受限分支以当前状态和 base action 为条件学习低秩 residual，再从有序候选中选最小预测可行 gain；这只是给定 relation/calibration 与候选集下的局部选择，不是全局最小干预或物理安全证明。作者 fresh-base 对照支持局部修复，却有更大 gain 过冲、个别任务退步与 regrasp 已恢复但最终失败；代价是 correction 训练、观测与在线校准，冻结 base 不等零训练成本。关系误判、无可行候选或复杂接触超出修复范围时，hold 并重新观测、回退原 controller/全局重规划或人工接管，不能用局部成功签发完整任务完成。

**AutoViewMem21940** [exact-v1](https://arxiv.org/html/2609.21940v1)正式题名 *AutoViewMem: Self-Configuring Orthogonal Views for Conversational Long-Term Memory*；暂`2+1+2=5`。§3.1–3.2、4.1–4.4/Tables1–4及局部case实际已读。每50chunks提10候选view（name/slots/extraction instruction），exactinstruction去重/e5归一embedding，DPP uniformq选K10偏diversity、每seed top30neighbor由LLM归成canonicalinstruction。作者明确orthogonal是实用lowoverlap非数学正交；view非互斥，同span可多projection，每item保source/timestamp/tag。query只统一dense topK，speakerpool合并/tokenbudget；同provenance仅first occurrence计metric，不拿多视图复制充coverage。离线texthashdups、similarity≥.9 graph/components递归阈值至.999只是候选，LLM按contain/complement/independent决定merge，冲突/时间变化/具体detail保留；不是cosine自动裁真值。

LoCoMo1540Q/200–400turn、PersonaMem32k589MC；Qwen3.8B/14B/e5basev2/temp0/max8192，验证调hyperparam但准确split/重复seed/CI/hardware/precision/全部写时模型调用预算未给。Table3 fixedqueryK30 fulljudge.837 vsSingle.774、randomDPP.777、noConsolid.801，支持局部write organization，不证明同生命周期预算或唯一机制；DPP和consolidation一起改变bank人口。Table1 Qwen14 FullHistory.868反高于Auto.853；Qwen8 relation fact/mention与tracking也有旧方法更强，不采用全能力最优。Fig2 token对照不是wallclock。Table4 football tentative interpretation有raw支持，仍不把emotion/value/goal projection升级成已核事实。

actual AGENT-MEMORY Ch77:324–338已有late query constructor/tri-granularity；454–457已有derived preference/materializedview lineage，497–511有Add/Update/Delete与resolver分权。这些未承载**按重复interaction先归纳写入schema、选互补抽取指令，再统一index而不增加query routing**的placement选择；不只是把已有summary重命名view。作者拟5分因gap深入I，在tri-granularity段后/旧Consolidation说明前最多两段，待root必要source→owner/literal与窄锁：

> Memory schema 也可以由重复 interaction 在写入前归纳，而不必固定一种 summary 或等 query 到来才构造：先收集候选 slot/extraction instructions，选择低重叠、互补的指令集合，再按它们把同一 evidence 写成多个可回指 projection，统一进入常规索引。它把部分 semantic disentanglement 成本移到写时，避免必须增加读时 router；embedding diversity 只是选择启发，不是语义正交、独立或事实正确性。同一 source span 的多份 projection 在覆盖统计与读取合并时仍应按 provenance 去重。
>
> 这条分支增加候选归纳、抽取与离线 consolidation 调用，并随 schema、用户与模型变化承担重建成本；相似度只提出可合并候选，时间冲突、具体细节与不可相互包含的事实不能因向量相近自动删除。受限同 query-budget 消融支持组织收益，却未匹配整个写读生命周期预算，部分能力和较大 backbone 的完整历史仍更强；低频写入、短会话或 schema 已稳定时，固定 summary/raw history 继续合理。抽取或合并无法回指原记录时保留原始 evidence 与旧索引，不把目标、情绪或偏好 projection 直接晋升为权威事实。

两项均仅作者必要source/actual提案，尚未独立终判或写入，不能计入正式22完成。

## 2026-10-01 SafeStage21223 / DRT21675 标准必要与具体采用范围

Root最小决定准入5分核已PASS，本轮补标准必要支持/反证；两项不是重新发现的家族。

**SafeStage21223** [exact-v1](https://arxiv.org/html/2609.21223v1) *SafeStage: Evaluating Safety Before, During, and After Vision-Language-Conditioned Robot Manipulation*，`2+1+2=5`。The Benchmark/Lifecycle Taxonomy、Task Construction/EvaluationMetrics、ExperimentalSetup/Validation/Results/Limitations必要完整实际读；中段截断的Setup另定点恢复。97scenarios=27initial/40execution/30final，每task至少一个safecompletion和directunsafecompletion；按最早安全应改变behavior的stage归属，不多计后续同一失败的效应。ISH compare targetcommit/resolve，approach/grasp不必commit；ETS按对象角色判接触/clearance/region而非任何contact即bad；FSH成功后robotpose固定、继续sim5s检查support/orientation/residualmotion/邻物。五frame initialbaseline/contact>.1N+多frame等tasksubset用episode timestep换窗口，privilegedstate只scorer读。

SR/VR/SSR/USR用同一全rollout分母，SR=SSR+USR；lowVR可能不行动/未到风险，USR/成功分母又是不同conditionalratio。RoboLab GPUPhysX120Hz、DROID Franka7DoF/Robotiq8D绝对joint+binarygripper15Hz，π.5/GR00TN1.7/DreamZero/Cosmos3Nano无本benchmarkFT、原camera/actionchunk不同，完整policy比不是架构isolated。每task×policy×prompt3预定scene seed×10rollout，50–90s horizon，表±为3scene的sampleSD而非trainingseed/CI。三prompt目标不变；default聚合SR33.74/SSR9.84/USR23.90、genericSSR10.11、specificSR22.02/SSR5.91/VR71.56，specific更少unsafe成功不能称更安全。240 renderedepisodes80/stage blindhumanlabelsprecision95.81/recall98.77/F197.26只是视觉一致性、不physicalgroundtruth。只sim、privilegedthresholds/fidelity、无真实damage/noise/actuator/tactile；GPU型号/precision/全部运行成本未给。风险概念不由论文命名赋普遍规范权限。

actual Ch26:738–781有sim→real ladder/独立controller/组合readiness，Ch66:2553–2555已有阶段witness，2554前有同分母成功∩安全用途要求；拟采用的差额仅**native goal首次为真后的显式稳定性观察窗口与firstcriticalstage归属**，不把通用成功≠安全重写当新I。作者拟5真实gap深入I在Ch26 Evaluationladder尾/Readiness标题前两段，待root必要source→owner/literal及窄锁：

> Native goal 首次为真也未必是物理评测结束：物体可能稍后滚落、失去支撑，或令邻近对象继续运动。EvalSpec 应显式声明 goal event、控制动作停止方式、post-completion observation horizon 与稳定性谓词，再把 task success 和安全交集用同一 rollout 分母报告。若一个初始依赖错误继续导致碰撞与不稳定终态，可按最早应改变行为的阶段归类，同时保留后续 effects，避免把一条失效链算成多个独立失败；这是一种诊断约定，不是内部推理归因。
>
> 一个受限模拟 benchmark 在 native success 后固定机器人姿态继续观察五秒，暴露成功谓词遗漏的延迟风险；这个窗口、privileged state 与阈值只属于其场景，不能继承为真机安全保证。更多安全文字也未必提高 safe success，低 violation 可能只是未行动或没走到风险阶段；应并列成功、安全交集、违规和条件成功分母。持续观察增加仿真/传感器和重放成本，观察期不足、状态不可测或物理效应更慢时应延长并重新标定、补独立控制器/人工检查，不让终态成功替代完整 safety envelope。

**DRT21675** [exact-v1](https://arxiv.org/html/2609.21675v1) *DRT: Dense Reasoning Trace for Efficient and Grounded Multimodal Reasoning*，`2+1+2=5`标准。§3–4/AppendixA–B/D.1–2/E/F必要实际读。visual/think[priors]/answer区分文本中的观察、推导、答案，symbolicconnector密度；GPT5.1把200kVisionR1Cold Mulberry解成trace，sameGPT5.1生成与correctanswer+visualfidelity+logicalfaithfulness判PASS的reference，8936image+5788textRL；这仍是模型judgement，不自动实现三维真值或因果faithfulness。Qwen235B judge匹配reference steps/unsupportedmatchedhall/effective/deepsteps，format规则+.1或−1/15tokensegmentpenalty；main正确.9/错才partial.8，hallratio乘(1−.5ratio)，bonus.3/.12并乘referencecomp，cap4/difficulty6–9或10–18，不把bonus当causalcredit或guaranteedgrounding。另解法与granularity可different仍judgebias。

Qwen3VL8BInstruct visual frozen/alignertrainableLM全FT：32H10080G约50h、seq16384/global32/dynamicbatch800earlystop369455processed；RL16A10080G约120h/512batch/G16/200step/1e−6/KL.01/promptreply2048，235Bjudge额外cost未完全归账，precision/seed/CI未给。五bench macroT1DRTRL67.2 vsStandard65.9、206.9vs1139.8tokens；MathVista76.8<77.2/GSM94.3<95.2，不逐task全胜，SFTonly61.7<65.9。Table2bonus平均66.1→67.2但Video44.8→43.7/length170.4→206.9，reward组合取舍非各维均改。TeacherGPT5.1又作为4671evaluationtrace/stepjudge，不能称无sharedbias独立humantruth；GTstepcount只是difficultyproxy。D.1 singleA10080G/vLLM/concurrency64，DA128例外不与DRT完全恒并发；latency mean end-to-end/QPS，非P99/SLO，precision未给。E changingrewardmodellocalnotproofwhycausal；14B66.2距67.2恰1.0非严格小于1；F只sequentialchain未branchgraph。无runtime因果probe不抹除有效局部accuracy/resource观察。

actual TRAIN-GRPO Ch33:193–213 processcredit与verifiercorrect方向分账、尤其多模态judge看不到图像或解析受影响不能证明grounding；PLATFORM-EVALUATION-SYSTEM Ch66:714–718 rationale对标签一致≠faithful/hiddenchaintruth，148–151权威provenance不归selfreport。作者拟窄E只采用**compact/reference agreement与视觉/推导正确性不能互证，judged过程credit是训练signal而非真值**；三parttrace/partialreward/bonus局部recipe和Table1工作点仅报告，不说现有书有wholeDRT，也不因未重复recipe关闭贡献。若root认为observation/deduction分离压缩构成未承载长期分支，可只核该差额再定I。必要源与actual对照已齐，待非作者有限裁决，未计正式完成。

2026-10-01 root必要v1 §3.1–3.3/奖励Eq/Table1与actual Ch33:193–215有限裁决：judge caveat的窄E成立，但未承载typed压缩及错误答案reference-completeness credit，改为5分因最小长期gap深入拟I；原证据/反侧保留，不采用whole recipe。拟在既有process-credit子集排序的代价/fallback段后、“一条回答包含候选集合时”之前两段；未获窄锁、未写。literal：

> 多模态过程的压缩还应先区分视觉观察、背景先验、推导与最终答案的权限，再选择紧凑字段和符号连接。格式可解析只证明这些陈述能被定位，不证明图像支持观察、先验适用或推导有效。一条受限训练分支将压缩trace与reference steps对齐：最终答案错误时仍按参考推导的完成程度给部分credit，并对unsupported匹配步骤折扣；这提供局部训练信号，不把reference agreement、步骤数量或紧凑表示升级为正确性、视觉grounding或token级因果贡献。
>
> 这种选择用teacher生成/过滤reference、额外step judge和解析预算换取短trace；shared teacher/verifier偏差和不同解法的粒度会进入credit。DRT的受限整体结果减少输出长度，但MathVista、GSM等单项反退，辅助bonus又增加长度且有切片退步，不能归因每个压缩或奖励组件均有效。应同时验收最终答案、视觉依据、过程支持与含judge的总成本；reference不可靠、压缩丢失必要证据或任务回归时，保留完整trace审查、outcome-only或可靠process verifier，而不只优化格式与长度。

2026-10-01 root必要源→actual/literal及实际写后通过：DRT Ch33:207/209两段已落实在process-credit fallback后/集合分账前，保typed证据角色、reference partial-credit非grounding、judge成本/单项反退及fallback；unique SF与exact-v1 URL绑定、窄锁释放。正式计深入I，不把原judge caveat E扩大为全recipe，不代日Gate。

## 2026-10-01 Next-turn21187 / ODU21392 必要证据与采用边界

**21187** [exact-v1](https://arxiv.org/html/2609.21187v1) *When Better Turns Do Not Make Better Agents: Diagnosing the Gap Between Next-Turn Metrics and Workflow Success*，`2+1+2=5`标准必要§3–4/Limitations完成。130proprietaryworkflow→GPT5双角色1800conversations，Claude4.5Opus与Gemini2.5Pro均同意后1027（删773）；5834train/664valid/542heldoutturns来自84heldoutconversations，无conversation snippet重用，不证明workflow独立holdout。四base Qwen3 4/14B/Gemma3 4/12B同样本五epochfullFT，但硬件/precision/tokenlength/LR/compute/seed/CI未给。Goldhistory ROUGE/turnjudge、166exactnormalizedfunction/args、84 own-history deterministic-user replay+invaliderror最多2retry、holisticGemini0temp分别是不同对象。实际table toolworkflow分母77，不混84：SFTQwen4B3/77、14B8/77=10.4%，其余0；holistic四种皆0/77，不能称全部84客户任务皆零。Gold allturn全四升，tool exact Gemma4B3→0反降。Exactrefcall+golduserturn可能拒合法路径/低估真实互动，同judge用于datafilter与评测有共有错误；结果是受限诊断不是生产失败概率。

actual PLATFORM-EVALUATION-SYSTEM Ch66:1218–1240明确goldhistory isolated与agentgenerated cumulative分别验收且允许替代合法路径，1379–1385到达state与conditionalsolve分开。拟窄E：**从正确历史预测下一动作≠自主建立/维持历史后的workflow成功，文字/工具/终局不可互授**，并非全五协议/五epochrecipe已有。局部精确判分与比例只报告；必要source/actual已齐待root有限peer，不计正式完成。

2026-10-01 `sep22_resume_v3` 非作者直接核exact-v1 §3.1/3.2/Table1/§4/Limitations与actual Ch66:1218–1240，窄E通过；84 conversation与77 tool-workflow、8/77及Gemma4B反侧保留，不把五epoch或五协议整个recipe称已有覆盖。此结果只终处置21187，不签日级Gate。

**ODU21392** [exact-v1](https://arxiv.org/html/2609.21392v1) *Omni Demand Understanding: A Benchmark for Contextual User-Intent Inference in Multimodal Interaction*，`2+1+2=5`，§3–5/D.1–3/E.2/E.4必要实际读。只评分finaluserclip，earlierassistanttext/媒体前文给定，不live闭环。M1 demand binarymacroF1同时positive/negative，M2–5只有positive；FTR是negative分母；M2 keypointhit参考(mediahumanverified) structuredintent+context，非整scene成功；主Avg scene.15/.6/.1/.1/.05、E2pointweighted不同，不合并。Scripts Qwen3.7Max/textonlydiscriminator筛utterance可推意图，不等renderedmedia exclusivechannel；1801synthetic+277humanrecorded/30actors，actualmedia重建labels/manualverification不script真值。Source/addressee错误可将背景播放/非助手收件人的语句升成demand，不能从词面question/imperative签发意图。

14native AO/12AV接口分开、GPT5.4ASRbaseline未排名，Qwen3.6Flash mainjudge；14模型11FTR>50的题摘只是对应集不全部署。Bestmodel AV63.4M2/40.6FTR，SeedAO78M2却80.7FTR，两个对象不可互推。Synthetic/recorded5modelmatched语言ChineseAV slice不同人口，Gemini表现升/QwenThink−7.6且FTR+11.1，不一律domain恶化。E2三judges重评1060commonpositive3956points，source recoverability.996–.998只referenceannotation可重构，不physicallytrue；storedoutputrank3system稳定不全部14，abscoverage范围.029–.041且没有新inference。E4 paired200=160positive40negative/ChineseEnglish各半，sameGemini3.1Pro temp0/topP1/max8192/onecandidate，Givenreferenceintent/context（非answer/keypoints）导致103preferred/80ties/17other；85.8%是103/120decisive，不是所有200。Nodemandtext60→15、demand silent12→1局部支持demand信息有用，不证明learnedgate可在线获得oracle。主native hardware/precision/完整调用与重复run预算未披露，无liveSLO/causalchannelknockout，judge稳不补这些。

actual MULTIMODAL-REPRESENTATION Ch23:728–730已有memory/hidden trigger/timeproposal与runtimeauthority，AGENT-PLATFORM Ch84:566–568是spoken/playback/call/task寿命分离；不是**可回答的语句因来源/收件人不对仍不构成demand、判是否应答与positive内容恢复分母分离**的评测合同。作者拟5因该gap深入I，owner PLATFORM-EVALUATION-SYSTEM Ch66连续交互/多轮history干预段后（当前375–378后/下一个标题前）两段，待root source→owner/literal/窄锁，不借通用模型trigger概念硬给E：

> 音视频交互的评测还应先判断“这句话是否向 assistant 提出了 demand”，再评价“应当回应什么”。可回答的疑问、命令或抱怨可能来自播放媒体、背景说话者，或发给另一个收件人；良好转写和正向请求的内容恢复都不能证明它应被受理。将 demand/no-demand 检测与 negative 场景的 false-trigger rate 分开，内容关键点、定位与转写仅在正向人口评价，并保存媒体、历史、source/addressee 与参考意图 identity，不能把不同分母压成一个响应质量结论。
>
> 一个受限 benchmark 用实际媒体重建并人工核对意图，发现高内容恢复仍可伴随大量 false trigger；给同一输入附参考 demand annotation 改善回应和沉默选择，但这是 oracle 信息干预，不证明线上模型已经拥有相同 gate。固定历史最后一轮测试、合成/真人录制切片与文本 judge 稳定性也不是持续双向服务的 SLO 或全部用户意图真值。该诊断增加 no-demand 样本、标注与复核成本；来源、收件人或意图不明时，应澄清或交显式 turn-taking/router，保留直接响应的低风险接口，不从文本措辞自动升级成执行授权。

## 2026-10-01 Entropy20824 / SURE20846 有限必要结果

**20824** [exact-v1](https://arxiv.org/html/2609.20824v1) *Can Small Language Models Know What They Don’t Know? Semantic Entropy as a Confidence Signal for Sub-3B Parameter Models*，`2+1+2=5`标准。§3–5/7.1必要实际读：七approach分别tokensignal/earlystop/router、N5 semantic多样本，MCQletter/booleanexactcluster，自由text bagtokencosineagglomerative.85；15heldoutcalib只正确样本平均H设τ不是概率/风险校准，若无correct样本处置未给。七pair四family且expert1.5–4B，AppleSilicon无quant，20–50/testcell、T.7/topP.95/max128/**top-k20 logits计算entropy**；Eq1确写after softmax normalization，但实际实现是否另作top-k重归一未核，top-k对象不等fullvocab，不能从此把32/35nearzero外推所有SLM fullvocab intrinsicblind。32/35身份中同small不同expert会共享base人口且Table2记录多pair，不35独立model/dataset条件。Table3 SemRt胜13/35且Gemma一致错误时entropy不触发/多task退，semantic不truth；Table4 cross组同时换expert质量/参数比，不隔离architecturalfamily因果。640tokens vs2–120base、N5+expert总增算，未全wallclock/energy/SLO/precision/seed/CI；差<10pp不能确立significance。仅作局部资源/accuracy诊断，不宣称通用routing保证或省算。

actual PLATFORM-EVALUATION-SYSTEM Ch66:2078–2086将semanticentropy/tokenprob等features与calibratedcorrectness分账，2213–2219有correlatedwrong/lowentropy不truth，508–512明确riskforecast/router/solver分权与falliblesolver退路。拟窄E采用这三对象及resolver能力需另验；N5/τ/local数字是报告配方，不宣称wholeentropy方法已覆盖，也不因tiny模型关闭。2026-10-01 07:21：sep22_resume_v3独立亲读该exact-v1必要机制/关键反侧与上述实际owner，窄E通过并同步正式日报；只采用本段明确命题，recipe与局部数字不作整篇覆盖。

**SURE20846** [exact-v1](https://arxiv.org/html/2609.20846v1) *Rewarding Efficient Reasoning Improves Abstention on Underspecified Tasks in Reasoning Models*，`2+1+2=5`因central冲突深入受影响；§3/5/6/7及AppA.4/C必要已读，恢复了截断setup/Discussion相关段，不无差别human附件。QuestBench GSMQ删variable paired/GSM8K answerable，AbstentionBench20sources mixedreason、input≤2048、各500test；train60%unanswerable40%answerable disjointtest，但已发布bench contamination可存在。Qwen3-4BThinking/Phi4mini/Nemotron3nano4B，LoRA QV r8α16/Adam1e−4/64/G8/4096/T.6(Q/P)或1(N)，前两200step/N50gradientearlystop不跨model恒步；硬件/全APIjudge/precision/independenttrainingseedND。Qwen30B3B judge accuracy/abstention/sentence，A.4作者700sentencelabelbalancedacc.87非真实内知；AppC训练process只first1000token而完整generation4096，noEOSr0另有长度selection。95%bootstrap是test不trainingrepeat。

**精确central争议**：§6.1 Eq2正αeff=.5乘Eq3 `e=(n−k)/n`，n total句/k firstmissing句。固定k>0时∂e/∂n=k/n²>0，固定n时∂e/∂k=−1/n<0；最大化奖励直接倾向**延长n/提前k**，不是文中称“decreasing n or increasing k”。正向式不能解释声称“发现缺信息后立即停”；GRPO groupcentering不翻转同accuracy样本排序。n/k处理与first1000截断可能影响实际实现，但原文没有提供相反符号纠正，不能自行补造 `1−e` 或negativeα。经验Table1 SURE unanswerable662/base1432、answerable766/base1183及长度penalty202/235，answerability accuracy SURE−.012 vsnaive−.136是有效受限观察，不因公式错删除；上界humanRT与LMtoken不同且importance点奖/文本prompt不同，不证明同认知机制。作者事后认为internaloptimalreasoning结构仅speculation。限定English/freegeneration≈4B/GRPO/judge在线与prompt依赖，未验证安全abstention/clarification真实效果。

实际Ch33:404–418有长度shaping/truncation与verifier权，Ch66:2163–2178 riskcoverage、1962缺必要条件时澄清，不可用这些掩盖新reward方向冲突。2026-10-01 root 非作者亲读exact-v1 §6.1 Eq2–3及紧随优化解释，确认正αeff=.5与e=(n−k)/n的方向冲突；不自行补1−e。因此暂缓**central process效率因果主张**，本次为精确争议终态，不正面采用到Books、不记E或贡献关闭。Table1有效受限经验与原实验配置保留，不支持奖励立即停的因果保证。仅在官方纠正符号、精确实现确认实际objective或匹配控制到达时，定点重开本节；未读其他普通项不因此标blocked，亦非日级通过。

## 2026-10-01 LogicTrack21492 / 视觉地理隐私21363 必要证据与局部提案

**LogicTrack21492** [exact-v1](https://arxiv.org/html/2609.21492v1) *LogicTrack: Auditing Reasoning Trajectories of Large Language Models with Formal Logic Solvers*，`2+1+2=5`，因actual owner局部差额拟深入采用；§2–3、AppA.1–2/B.2–3已实际读，不遍历其余prompt附件。每步包含premises/implicit commonsense/derived fact，GPT4o-mini自动形式化为SMT断言，由Z3核验蕴含/反驳；fidelity另由GPT4o-mini检查原premises（不可从query搬事实）、补充常识是否可接受、联合一致性。SBR加权fidelity与verify，unknown有部分分值；这不是对原自然语言和世界事实的独立形式证明，自动翻译/补充前提仍可能共有judge错误。§3主文VU称restricted answer accuracy，B.3精确定义却是**全部examples中正确且ρ=1的比例**，非verified subset上的条件accuracy；VWA为mean(ρ×correct)，UR为mean(1−ρ)，不混分母。

AppA.1 step阈值.8/累计均值.5、每位置最多2次重生；都失败时highest SBR **force-forward**保证搜索进展，beam全剪时也恢复best候选，MCTS能返回best partial。因此执行到终局不代表每步通过，更不能将final answer correct签成整链verified。A.2 6000条SFT筛final正确且syntax/semantic核验、负步必须与正步共享prefix，加入backtrack token，LoRA32/α64/bf16/2epochs/effective16；撤掉solver后的SFT不继承证明权限。推理7models/8bench、T.7/max10240、A10040/80G或equivalent/API，同prompt不等额外formalizer、solver与tree搜索预算匹配；精确全成本/独立train seed/CI未给。

Table1的133/168改善是相关model×task×metric比较，不是168独立实验，Gemini FOLIO OA79.31→77.59/Llama48.28→45.69等反侧保留。Table2 Llama SolverOnly UR7.89优于Both9.89，Both OA63.60低于FidelityOnly63.97，beam OA65.44高于Main63.60；不写所有指标/搜索全胜。SFT较高OA但较低VWA，训练与推理核验是不同对象。评测复用相同形式化/solver流程，无独立natural-language fidelity ground truth，不以机械verify改善证明高风险可信。

actual `AGENT-REFLECTION` Ch80:42–64已有feedback independence与修复≠失败归因，表中deterministic solver标高独立；`PLATFORM-EVALUATION-SYSTEM` Ch66:3603已有静态policy翻译须验证，但未承载**逐步自动添加前提的证明权限与预算force-forward的verified/unresolved分流**。拟窄I位于Ch80该feedback表后、现有“但反馈带来一次成功”之前，以下两段待非作者源→actual裁决/锁，未写不计完整处置：

> Deterministic verifier 的高独立性只覆盖它实际收到的对象。把自然语言推理逐步翻译成逻辑断言时，solver 可以检查给定前提是否蕴含结论，却不能顺带证明翻译忠实、补入的常识为真，或这些前提确实来自原任务而非待证明答案。应保留原文、所选历史前提、额外假设与形式化版本，把 translation/fidelity 审核和 solver result 分账；auto-formalizer 或同模型 judge 仍是可错的提案者，机械有效不等整条自然语言推理可信。
>
> 搜索的停止策略还可能改变“verified”的含义。低分步骤可以触发定点重生、回退或保留已核前缀；若有限重试耗尽后为了进展选最高分候选强制前进，或返回未完成路径，应明确交付 unresolved 结果，不能继承逐步通过的标签。LogicTrack 的受限实验同时出现最终正确率与核验率不同方向的变化；形式化、judge 和搜索调用增加成本，离线蒸馏backtracking轨迹也不把solver证明迁移到无solver模型。高风险路径不能强制前进时应停止或升级，普通可容错任务仍可使用有明确未决标记的尽力搜索。

2026-10-01 root 非作者必要源→actual seam/literal通过，授Ch80仅这两段窄锁；作者实际写入Ch80:58/60，独立source-family绑定。root随后fresh读取两段及feedback表→归因handoff邻接，实际写后PASS，窄锁释放。前提/翻译分账、force-forward/partial unresolved、无solver SFT不继承证明与高风险停止/成本均在正文；本项I完成，不自签日级Gate。

**21363** [exact-v1](https://arxiv.org/html/2609.21363v1) *Hiding in Plain Sight: A Diffusion-based Mitigation of Geolocation Privacy Leakage in Vision–Language Models*，`2+2+2=6`安全/知识缺口深入；III-A/IV、V-A–E、VI-A与AppD/E.3/E.7/G必要已实际读。防御对象是发布者有权处理、拟公开的照片，不采真实个人位置识别、不保存攻击prompt。供应商拒答与发布前内容变换是不同控制点：SD2Base reverse diffusion以GeoCLIP GPS-aligned surrogate steering高层地理线索，辅以TV/edge保持结构；须已有GPS或另估位置，不是无成本纯匿名化。50采样steps、30步扰动/15优化；optional inpainting正文IV-B提SAM而AppD用CLIPSeg RD64，未核实现，不将二者视为同一已验证部署。

原五API/temp0/default reasoning的Dox3/Street人口与阈值分别保留：Dox 1km-level错误识别率仍非零、粗粒度200/750km泄漏很高；Table I/II不是全model/threshold全胜，Street GPT5 Ours MED362.166低于GeoShield397.635，200/750km准确率Ours34.34/62.63高于其32.32/56.57，不照录“均最高错误/最佳隐私”。VRR是可解析输出比例，AED/MED与各threshold使用的缺答处理/共同response人口未充分明示，不把拒答率和距离错误揉成匿名保证。V-E4090 per-image122.15s/2.669GB对16.85s/1.416GB、38.02s/1.531GB两baseline，不同优化预算不是等成本；低VRAM不等线上吞吐/SLO，batch/multiGPU/earlystop仍建议。

VI-A强适应评估限定Dox3最脆弱150图切片；AppE.7 TableXV aggregation后multi-model仍10%在1km/80%在200km/100%在750km，7.01×AED增加不是泄漏消失；GeoVista 200km仍60%。多图III/VI正文说25-meter、E.7说25km，50组×3图但表格分母/过滤人口交代不足，保留范围冲突，不自行改成一致受控protocol。AppE.3 COCO caption GPT5+LLM judge9.83/10、CLIP top1/3不变、moderation85.71→84.29是局部utility，样本量/CI/盲测未充分给，不证明“所有用途内容不失真”。G承认文字细节、cropping/迭代查询/white-box与其他PII边界、无certified guarantee。视觉质量专家均分也不是通用imperceptibility证明。

actual `PLATFORM-SECURITY` Ch72:175–207有text-span Policy-bound Sensor与learned text anonymization的attacker/utility分账，但未承载**发布前高层视觉地理线索修改相对refusal/pixel过滤的控制点变化、距离粒度与残余泄漏分开验收**。拟窄I在learned anonymization末、Privacy Leak Probe标题前两段，待非作者源→actual裁决/锁，未写不计完整处置：

> 图像还有不依赖显式PII字段的隐私线索：建筑、地形和环境组合可能泄露位置，供应商拒答并不消除公开内容本身的信息。发布者可以在上传前针对已知或估计位置改变高层视觉表示，而不只删除metadata或遮住文字；GPS-aligned surrogate引导的diffusion变换是一个受限分支。此时变换器拥有内容提案，隐私验收必须同时保留攻击者、距离粒度、可解析输出、位置误差与下游用途，不能从平均距离变大签发匿名化结论。
>
> 这一选择用生成计算和可能的语义失真换取所测攻击人口上的泄漏降低，不是跨模型或适应攻击的保证。现有受限结果仍有近距离命中与大量粗粒度泄漏，聚合评估也有样本范围冲突；图像caption、分类和moderation的局部变化不能代表审计或其他用途无损。发布前应独立核对细节/utility与多个距离阈值，GPS估计不稳或隐私代价不可接受时回退遮蔽、降粒度、访问限制或不发布；明确字段和低延迟路径继续使用确定性redaction，而不把生成式变换作为默认替代。

## 2026-10-01 VLA-Scope21246 / Outcome Geometry21659 必要审阅与具体已有覆盖提案

**VLA-Scope21246** [exact-v1](https://arxiv.org/html/2609.21246v1) *VLA-Scope: Shift-Aware Failure Prediction for Vision-Language-Action Models*，`2+1+2=5`标准。III-A–C/IV-A–F/V实际必要读：初始化image/text均池8192D分别训练binary OOD/type两个LR，τ=.5过gate才给risk、ID没有risk不是成功；type在rollout中固定，不检测后来发生的shift。14 decoded action前缀统计（controller clipping/scaling之前）+7type+执行action前observation所得4096D hidden从10:k累计均值/PCA32组成53D共享LR，预测最终simulator预算内成败，不是实测物理进展或因果失败解释。标准化/PCA/分类只在train tasks，prefix1/(T−10)每rollout等总权，samepolicy冻结。

OpenVLA LIBERO-Spatial10tasks/224RGB、10settling+220policycap、1900initial=500ID+1400OOD=751success649failure；leave-one-task-out十折，内部heldout形成training-side type预测避免标签直接偷渡。ActProbe/SAFE samefold/checkpoint/rollout/labels但representation/动作前后scale与调参不同，neural3seed而LR固定；非同模型所有预算均齐。RTX4090D/EPYC9754/18vCPUquota/PyTorch2.2CUDA11.8、OpenVLA BF16/neuralFP32、transformers4.40.1。IVB监督binary .9454优于ID-onlycos1NN .8176但前者用了OODtrain，非纯算法受控对比。OOD各type均两种成败、Layout failure27.5%/Camera77.5%，type≠个体failure，200Language type全对但binary只170入gate。全部OOD step60 .8497；conditional gate1184 .8534排除了216，含45failure无risk，不能用conditionalAUC签全路径。

IVC从step10–60同1400人口AUC .6852→.8497可支持积累观察有用；晚步成功退出，step200只7success，时钟/人口变了。Retrospective progress百分比用最终T求位置，不线上可知时间。current step60TPR70.72/FPR12.52，evercross-before60失败recall83.51/成功falsealarm50.73，不能混同一个operating point。IVD删累积representation .7906，删action .8344；full相对删action降低FPR但TPR也72.11→70.72、删gripper反提高，非每feature必需/全指标胜。IVF action feature分解只解释scorechange不是failurecause；最大局部变化可向下、低risk时稍后仍失败。

CPU warmcached-inputbatch1 .608/.893ms只是特征、PCA/classifier计算，排除了policy capture/loading/I/O/simulation；初次representation+gate捕获另2.15ms、SAFEcapture .56ms，不能报端到端.893ms。没有实机repair/安全继续、在线停止干预评测或新task开放世界校准，不从sensor推荐升级成actuator授权。

actual `MULTIMODAL-EMBODIED-VLA` Ch26:373–377明确偏离名义与任务failure两级不同对象及二级不继承前级FPR；776–784已有history-conditioned finite-horizon failure predictor/标签horizon与policy identity/无安全truth；`PLATFORM-EVALUATION-SYSTEM` Ch66:508–512风险测量、求助policy与resolver实际结果分账。拟窄E只采用**shift标签不决定执行失败、历史risk是有限horizon传感器而非state truth与继续权限，级联gate错误需分别验收**，不是整53D/PCA/LR或everalarm协议已覆盖；局部gate人口与clock数字仅报告。若非作者认为current/everalarm时钟有须新增的具体长期知识，定点只重开该差额，不按全篇强行E，也不删有效作者证据。2026-10-01 07:21：sep22_resume_v3独立亲读该exact-v1必要机制/关键反侧与上述实际owner，窄E通过并同步正式日报；只采用本段明确命题，recipe与局部数字不作整篇覆盖。

**21659** [exact-v1](https://arxiv.org/html/2609.21659v1) *Outcome-Conditioned End-Effector Geometry Across Vision-Language-Action Policies*，`2+1+2=5`标准。III–VI/VII必要全部实际读，不读references。四pipeline Spatial10tasks×20state×3template×5nominalvisuallevels各3000/共12000episode，每cell一个执行；Object另3000只有π0.5不复制四policy结果。clean600config/2400episode/3600pair、SS2588/SF923/FF89相依，state-block而非pairbootstrap2000rep固定10tasks，controls20partnerseeds重复使用轨迹不能独立pairCI。实际state/pose/commands轨迹是simulator观察，只有位置DTW omitsorientation/contact/force，不trackingerror/任务truth。按每5records采样、distance除LX+LY不是warpingpathlen，初始化/arc-length/centering/50pointnormalizedtime/bands九表示是不同测量identity，不合成一个effect size。

OpenVLA/UniVLA external224、OFT/π0.5两视+proprio256，cadence1/1/8/5，deterministictoken/L1与stochasticT.75P.9/flow不同；checkpoint/training/预处理不齐。nonzero腐败seed hash含policy、未存realizedseed/queryimage；sameoperatorlevel非同realizedcorruption，无hardware/precision/latency/完整budget披露。sameoutcome≠samegeometry：cleanSSmedian.0120/SF.0380但分布overlap不可当分类阈值；FF薄且64/89同pair，换representation/SF–FF能反转。III-D samepartnerstate/commonstate controls修正task/state解释、原轨迹anchor字母序有方向；2584matched差值median.0021不同于median差.0023。独立repeat1200/fivefixedseeds，成功资格条件下cross-policy仍超过withinrerun .0082（blockCI），不只是抽样随机性，但非所有政策互换保证。

IV-D SS<SF方向九表征稳，比例2.53–6.13不能固定效应尺度；72controlwindow存活3503pair、samecohort fullcontrast约.026变.01007约39%，留survivalselection，不failureonsetclassifier。Endpoint/duration是outcome后果，mechanicaladjustment非causalconfoundcontrol且collinearVIF17.1/11.9/10.1，残余正系数是spec-dependentassociation，不归因policymechanism。示教500normalizedtime reference未matchstate/训练setmembership，scale相近非statisticalequivalence。V压力L3ranking换、L1OpenVLA反升（非单调），allSpatialL4<.014；same nominal像素mask占面积不同，非同strength。L3SS223内195与clean共同/28新，conditionalpopulation转移需共同support再比较，不能把幸存几何当全原始population robust。wholecode/data仅uponpublication承诺，未核artifact复現。

actual `MULTIMODAL-EMBODIED-VLA` Ch26:703–707明确trajectorygeometry sensor不successsemantics/monitor不commit，Evaluation ladder:742–761明确pose similarity只是局部与真机outcome分别验收；`PLATFORM-EVALUATION-SYSTEM` Ch66:177–187冻结evaluation对象identity、1379–1385到达population与从该状态求解分开。拟窄E只采用**位置几何相近不证明executionquality、语言grounding或policy互换，输入/表征/人口身份不能被同success分数抹平**；DTW层级、SS对比与controlrecipe是局部报告，不说这些已在正文完整覆盖。方向稳但比例变化的受限证据保留，不因已有主题关闭贡献；若非作者判断conditionaltrajectory比较须新增owner段，仅沿III-E/IV-D–F/V-B有限核。2026-10-01 07:21：sep22_resume_v3独立亲读该exact-v1必要机制/关键反侧与上述实际owner，窄E通过并同步正式日报；只采用本段明确命题，recipe与局部数字不作整篇覆盖。

## 2026-10-01 Latent Steering21662 / Judge Panel21277 有限必要结果

**21662** [exact-v1](https://arxiv.org/html/2609.21662v1) *When Steering Fails in Latent Reasoning: A Latent-to-Language Transition Gap*，`2+1+2=5`标准；§2.1/3/4（含Table1/Fig2定义）必要实际读。Llama3.1-8B与Llama2-7B各explicit/COCONUT-style五continuous-thought同ProSQA训练lineage，但非相同权重，reasoningmode不单独隔离。sentiment/TruthGen/TwinViews13k三个stance对象、layer16 CAA direction在generationstart/末latent前配对±1/5/10，heldout decodability与direction-estimation分开。SR由LLMjudge/n200cell、次tokenstance概率差不采样、normalized displacement n100politics三者分账，judgefree不等token集合/stance测量通用有效。C3.1 λ10 displacement11.93/13.43而outputmargin sentiment5.20/.15、politics2.10/.02、truth1.50/.07支持局部hidden移动≠输出控制；正文概括latent保1–5%不能跨两family，Llama2 truth .17/.30约56.7%、sentiment2.62/10.24约25.6%，不照录为一致比例。stricterevaluator缩小SRgap，保judge依赖反侧。

§3 decodabilityAUROC .842–1/.859–1说明可读不是使用；finalnorm+LMhead logits作者核与nativeexact一致，JS transition相对within归一C3.1 14.77–24.22/C2 5.61–7.32，不自动证明训练缺lexical监督是唯一cause。末位unitdirection paired ±λ output oddgain减26.6–70.2×/9.4–13.7×是所测task/direction/位置，有pairedbootstrap但seed/inferenceprecision/HW/fullcost/judgeidentity与完整质量过滤细节未给，不推wholelatent能力较差。Discussion明确superposition未observed/manipulated、transition-awarefix未来工作，训练权重和后续路径混杂，保真实诊断、不编造修复成功。

actual `WORLDVIEW-REPRESENTATION` Ch5:190–214的证据阶梯明确decodability→localizedintervention→downstreamchange分别证明，182–186跨contexttranslation/behavior作用/泛化分开，230–232参数internal恢复≠activationrelay≠endtoend行为。拟窄E采用**可读信号、局部表示位移与下游语言控制是三个对象，局部操作成立不自动跨读出接口**；不说书已有COCONUTtransition实验或所有family1–5%现象。正文所提训练因果和具体修复只报告未决，无必要Books差额，2026-10-01 07:21：sep22_resume_v3独立亲读该exact-v1必要机制/关键反侧与上述实际owner，窄E通过并同步正式日报；只采用本段明确命题，recipe与局部数字不作整篇覆盖。

**21277** [exact-v1](https://arxiv.org/html/2609.21277v1) *How Many Humans Is a Judge Panel Worth?*，`2+1+2=5`，因actual owner测量差额拟深入采用；§3.1–3.5/4.1–4.5/4.8–4.9/Limitations、AppC.4已实际必要读。32models/10providerfamilies×ChaosNLI MNLI-m/SNLI/αNLI各1000items由humanentropytercile抽/seed42，每item100humanlabels只是empiricaltarget h非无错truth。temperature0/oneusermsg/no system/labelonly，requestedID非provider版本authentication、percalltimestamps未存，95994/96000parseable含6placeholder，不抹掉failedresponses。硬件/precision/API完整cost未披露，非equalcallbudget新aggregation算法或人力替代部署。

Eq1onehot−h residual保均值；normalizedGram C unitdiag/PSD/positive energies，PR=k²/tr(C²)忽略相关符号与memberenergies。νH由conditionalindependent draws Cat(h) MC12rep+finitegrid2–128/首bracket线性插值匹配PR；只同targetcurve保ranking、不保证equalaccuracy/cost。νMSE=J/E，其中J=mean(1−||h||²)，E=mean||panel frequency−h||²；J/E遇E0或J0不能照常有限定义。Prop1 E=Ω/k² Σλj bj（bj为energyweighted averagingdirection在eigenvectors的对齐），谱值之外energy/方向改变误差；代入eigendecomp即可核，不新estimator。AppC.4可实现hardlabels、equalenergies/zero mean/非负correlation，C(A)两2-blocks PR2/E1/4；C(B)=.5I+.5 11ᵀ eigen2.5,.5,.5,.5 PR16/7/E5/16，谱多样性↑却分布恢复↓，无需负correlation或meanbias。另同谱PR2但E1/4和0说明orientation不可抹掉。

Table3 νH4.24/6.46/6.50与νMSE2.30/3.75/3.44是不同matchedtarget，非可通用校准倍率/一般humanreplacement。54139 panels、150372additions/task共享member/items非独立replicates；itemhalf500/500与1%descriptivefilter非新人口validation或有效utilitythreshold。αNLI PR-vs−E相关.223–.419，经energy缩放升.937–.960是改target不是因果控制；halfrank .370–.554弱。γco中心化variance share43.8/33.7/35.9不是bias/majorityerror；Eq13须同时保mean displacement和totalvariance。锚小M实验仍从full h模拟，不能证明仅5–10humanlabels即可部署。majorityagreement68.6/86.5/93.0只SNLI超bestindividual，与频率MSE目标不同。Limitations明确没有未来models扩容界、全部分析随机流/可执行复現未全交付，不称已复現。

actual `PLATFORM-EVALUATION-SYSTEM` Ch66:2380–2392已要求按mean/ranking/decision分解raterbudget、共同bias不因扩panel消失；2394后annotationdistribution≠normrubric，969评分稳定≠独立发现。但**同一个judgepanel的spectral residual等效人数与distribution-recovery等效人数可以方向冲突，equalenergies/nonnegative correlations亦如此**未在actual承载，不能用泛“多样性不等正确”作wholeE。拟5因明确gap深入I，Ch66 Rater预算旧段后/“Judge还可能在两个不同目标间切换”前，两段待非作者source→actual裁决/锁：

> “这个judge panel相当于几个人”必须先说明匹配什么。若要保留人群分歧，可将每位judge的标签与同一经验annotation distribution作残差；谱的participation ratio描述这些残差方向有多少，而panel标签频率与人群分布的误差是另一目标。把二者各自匹配到条件独立的人类参考抽样，可能得到不同有效人数；该匹配依赖题目人口、参考估计、表示及抽样规则，不是通用的人力替代率，更不授予事实真值。
>
> 即使成员误差能量相同且相关非负，提高谱多样性也可能增大分布恢复误差：归一化谱统计丢掉能量和平均方向的对齐，后者仍决定ensemble输出。应同时保存member error energy、相关结构、人群参考及聚合后的实际目标误差，再按目标评估新增成员；majority label正确率、频率恢复和中心化共同方差不能互换。此审计增加人工参考、逐项votes和计算预算，有限人类标签也会给所有残差加入共同估计误差。低风险固定rubric仍可使用小panel；参考不足或新增成员改变人口时，保留原评测并补独立标注，不能仅凭一个“有效维度”自动扩容或发布。

## 2026-10-01 Shared-fault21155 / EvoPilot21257 受影响纠错必要包

**21155** [exact-v1](https://arxiv.org/html/2609.21155v1) *Same World, Different Knowledge: When Isolated Audits Misjudge World-Model Repairs*，`3+1+2=6`设计反证深入；III–VII、VIII-D与AppA-B必要实际读。固定plant/任务/planner/weights/pairedscene&wind，只改变交付的信息，不改变真实mass/thrust；区分truth→estimate fidelity和channel缺失availability，记录consumer/延迟/update/errorcorrelation。DCC只扰动traininginputs不改physicaltargets、同model内architecture/data/loss/budget匹配，不能跨WM-A17k10epochs与WM-U35k30epochs称容量预算齐。IsaacSim singlequadrotor/20Hz、history12/horizon20、MPPI512candidate、planningcore42Hz排除了perception/stateest/windreconstruction；targetflightcomputer型号/precision/wholelatencyND。7150physicalepisodes+14891windpool、disjointgeometrylibraries，但trajectory-trainedwindmodule selection70indices与evalwindstream重用，另70–99unseenwind30subset；referenceGRU用独立randomcollection避免该耦合。

100heldoutobstacle scenes、success距goal.5m以内12s/contactcrash。couplederror m~=(1+e)m/T~=(1−e)T，±.1隐含accel −18%/+22%非两个independent10%deploymentnoise；DCCindependently±20%uniform/window固定是robustnessassumption不是实机distribution。WM-A69→8在+.1/DCC65三modelseeds，而correct noisy/delayedstate时DCC66<73、nominalcost不能只报原exactstate无显著loss；不检测差异非equivalence。pairedscene withinseedavg后bootstrap/sign/McNemar，conditionaltrainedcheckpoints不等独立task泛化CI。

VII-A TableIV是新增决定性反证：same downstream/predictor/planner fixed，referenceGRUcorrect67/DCC57.3；只corruptreconstruction baseline49.3/DCC56(+6.7pp)，samecalibration给reconstruction+predictor baseline67/DCC56(−11pp)，三reconstructionseeds同方向，CIs[3,11]/[−17.3,−5.3]。终点dist allpair共享−孤立差+.31m CI[.11,.54]；time只共同success、不混分母。DOB同nominalmap/availableactions、invertiblewindmap时instantunfilteredidentity a0(η)+Bηwraw=aobs，是residual吸收calibration误差，不真实wind唯一识别；lowpass/horizon/learnedresidual后不必成立。TableVI full20steprollouterror并无detectedisolated→shared改善，closedloop与analyticinstantaccel分开。负offsetseed0点估仍DCC低但methodpreferences不显著（sharedp.057），不能称所有offsetrepair一定反转。p*59%等仅two-conditionscenario break-even不是field faultprob；fixedsinglequadrotor/nominaldrag良好匹配/模拟exact或syntheticstate，不外推生产。Code/artifact统计审计将releasewithpaper，不声称已复現。

actual `MULTIMODAL-WORLD-MODELS` Ch25:36–66已有environment/agent/joint预测channel与action-support边界，76–80有inverse/forward共享误差的一致性警告，147–157有modelmismatch/modularinterfaceerror；未承载**同一错误源到多个consumer产生补偿，使isolated repair排序相对真实共享路径反转**。拟窄I在“在谈State之前”现有channel说明末、goal/configuration分解段之前两段，待非作者源→actual/锁，不计22：

> World Model 的预测channel还必须声明信息如何到达各个consumer。训练时的真值参数，部署时可能成为带偏差估计；另一条缺失channel也可能由历史状态与已执行动作重建。重建器没有消除依赖，而是把依赖移到它自身使用的calibration、normalization和动力学路径。应固定真实环境、policy/planner与权重，分别扰动单个consumer和共享source的所有读取点，再比较预测响应及配对closed-loop结果；只降低某个局部误差不足以决定repair值得部署。
>
> 共享误差还可能被重建残差吸收，与下游nominal model偏差互相补偿；只修一条路径可能破坏原组合。受限quadrotor研究中，抗不确定训练在孤立重建错误下更好，却在同源错误进入重建器与预测器时更差。瞬时可逆的残差恒等式只是补偿路径，不证明真实扰动被识别、长horizon精确抵消或所有误差符号同样成立。组合审计增加shared-fault、nominal和闭环试验成本；没有可靠配对或路径覆盖时，保留原组合并缩短预测horizon、回到真实观测和保守controller，不能凭isolated benchmark直接替换重建器。

**EvoPilot21257** [exact-v1](https://arxiv.org/html/2609.21257v1) *Verify, Don’t Trust: Agentic Model Development for Video Discovery Retrieval at Scale*，`3+2+2=7`纠错深入；§4.1–4.7/5.1–5.5/6必要实际读（含恢复截断的5.2controlevolution段）。human批准每roundcontrast/commonbase/dates/allowedfields，skill+typedadapter拥有执行过程而非evidenceadmission；artifact提取effectiveconfiguration与两armattestation配对verify、缺必需证据failclosed，再human metricsemantics审核。Spec readonly但非cryptoimmutable，reusekey checkpoint/code/data/publishsettings排除纯eval字段，不重复因arbitraryskill不具独立新机制而打分；具体纠错对象是declared不等realizedfunnel。

VDD37day/7directions/20approvedrounds/68metricconfigs不是workflowattemptdenominator，完整retainedcohort9rounds、29terminal=27scientific2OOM/71logicalstages（22trainattempt20success/22publish/27eval），excluded11欠operationfields保scientificcontext不补造lostattempt。科学roleClaudeOpus4.7/4.8、readonlyHaiku、concurrency通常3≤5；localpreflight40m/remoteworkflow1–3h；token/precision/GPUoccupancy/全部budget未披露，97h是九roundsumorchestratorwallclock，不head模型trainingcost。Artifactreuse depth省约5GPUh仅局部记录，不分摊所有campaigncost。

§5.3 primitive−22pp两armdeclare(P,K)=(3000,600)，实际controlK3000/treatK600，不能归interactionhead。human查明+extremeK1probe及两处truncation修复先发生，automaticeffectivedepth/evaluatoridentitygate仅poststudyhardening；5.2十clean/faultpairedfixtures全部admit/block是replay非prospectiveincidentprevention或fieldrecall。修复后+4.8pp还换base，bundled不headcause；matchedsamecheckpoint/evalK3000 controlheadOffP3000/treatheadOnP6000 +3.20pp，是selectedoperatingpoint，不把head与candidate预算普遍独立。Offline ±.36pp是两publication poolshuffle operationaltolerance，不CI/statisticalequivalence。Online7day account随机1:1/regressionadjusted7daypreperiod、VDDsessionGSRR分母非offlineclickhit分母，+0.66%relative估计只selectedmodeltreatment，不EvoPilotcausal收益。US/CanadaVDDsubset、每armassignedtensmillions但preciseeffectiveN/CI/guardrails不retained；default持续serving非另一次causaleffect。依赖trustedextractor/artifact/humanmetricsemantics，未controlledrandomizedautoresearchbaseline或crossorgvalidation；这些边界不会删除真实funnel归因纠错。

actual `PLATFORM-EVALUATION-SYSTEM` Ch66:175–211已冻结model/harness/environment/scorer身份、保trajectory/componentreceipts防错误模型归因；`AGENT-PLATFORM` Ch84:945–966配对model/harness与demonstration/evaluator校验，不承载**scientific证据单位是实际两arm authorizedcontrast，不是两个各自完成且配置声明相同的run**。拟窄I Ch66 EvaluationIdentity原三段末（“一次聚合分数”之后）、“理解和生成共用backbone”之前两段，待非作者裁决/锁：

> 自动模型开发还应把comparison而非run作为科学证据单位。两个run都成功、有最终metric且声明配置相同，仍可能实际走过不同candidate funnel或evaluator revision。先冻结commonbase、数据窗口、允许的treatment字段与metric semantics，再从两侧terminal artifacts提取realized配置和谱系，检查未受treatment影响的stage是否等价；缺少必要证据的pair不准入，不能用另一variant成功补齐。Agent方案、memory教训和self-report只能指导执行，不拥有比较成立的权限。
>
> 数字存在但比较失配，是invalid measurement；OOM或缺data partition是operational failure；只有actual treatment成立的non-improvement才能成为模型负面证据。EvoPilot的受限案例把原−22pp归因追到输出深度失配，修复后的bundled retest、matchedlineage ablation和online随机结果仍各有不同estimand；post-study mutation通过不倒填为当时自动阻止了故障。配对提取、版本维护和人工语义审查有成本，旧的稳定专用脚本仍可保留；无法从可信artifact提取或semantics有争议时，隔离该comparison并定点补证，不按workflow完成率签模型改进。

## 2026-10-01 GameLogicBench21562 / StochasticSQL21133 有限必要包

**GameLogicBench21562** [exact-v1](https://arxiv.org/html/2609.21562v1) *GameLogicBench: Evaluating Coding Agents on Runtime Game Logic with Tick-Level State Assertions*，`2+1+2=5`标准；§2–3、4.1/4.4/4.6/4.7与主文Limitations已实际必要读。72个Godot4.4/GDScript任务（Atom21/Combo28/Repo23）、403 scenarios/1451 testcases；公开preview与hidden judge检验相同已声明要求，不把隐藏case当未知任务合同。固定tick/state assertions覆盖并发、重入、时间伸缩的合法调用，最终状态正确不替代中途invariant。construction从约200 ideas到122 complete再由三annotators筛为72；proper实现与behavior-preserving alternate应通过，缺能力naive/mutant应失败，这同时审计接受与拒绝两侧，不让某一实现选择变成答案真值。

§4.6仅36-task audit/666 mutants：terminal-only逃逸236（35.4%），preview-only508（76.3%）；488个原FAIL submissions在两弱协议下分别64（13.1%）与418（85.7%）变PASS，mean solve抬升8.9/58.1pp，不是全72个任务统一因果效应。未做mutant validation的judge使127/666 mutants逃逸，24缺check/19tasks；修复使三个solutions、两个tasks/三个models由PASS变FAIL，而proper/alternate仍过，不证明oracle普遍完备。§4.4只对三个配置重复三次：Qwen均值pass@1 45.37/pass@3 62.50/worst-run27.78、σ4.24；GLM34.72/48.61/22.22、σ3.67；Kimi34.72/51.39/15.28、σ3.67。不能将同suite重复或pass@3当部署可靠性。

§4.1主结果20 model–scaffold配置单sample、solve egress sealed、judge network disabled；CC2.1.177/Codex0.144.1/OpenCode1.17.18、High effort/3600s绑定该run。最佳配置52.78%不是单模型能力，scaffold改变同模型结果；vendor priced API cost不是全构造/执行端到端成本或本日价格，hardware/precision与生产SLO未披露。§4.7 five paired Repo tasks开放network允许四次upstream retrieval/reuse，人工确认；只支持该五题输入条件变化，不外推全部排行榜污染。Limitations明确只deterministic gameplay logic，不测art/player experience；Godot-only/permissive upstream genre、有single-container无network-sync。未核公开code实际运行、不复现实验。

actual `PLATFORM-EVALUATION-SYSTEM` Ch66:1412–1426已有checkpoint-specific state assertions、动态mutation与terminal artifact分权，1637–1646已有冻结predicates、deliberate mutations、请求变化/未请求preservation两侧oracle审计与不完备fallback。拟**窄E**采用“途中invariant与terminal结果分别检验，verifier需正确实现接受和错误变体拒绝”的既有命题；不声称现有书覆盖tick-level game recipe、403 scenarios或全部mutation构造。局部Godot recipe与榜单仅报告，无Books diff必要；2026-10-01 07:21：sep22_resume_v3独立亲读该exact-v1必要机制/关键反侧与上述实际owner，窄E通过并同步正式日报；只采用本段明确命题，recipe与局部数字不作整篇覆盖。

**StochasticSQL21133** [exact-v1](https://arxiv.org/html/2609.21133v1) *The Stochastic Shift: A New Evaluation Paradigm for Text-to-SQL with AI Operators*，`3+2+2=7`纠错深入；§2–6（包括4方法与5.1/5.2精确评价）实际必要读。AI.IF/NLfilter让确定关系逻辑和概率/语义判断处在同query；不同prompt可改变边界样本返回行，即使作者人工判为relaxed-equivalent，EX仍拒；缺DISTINCT或UNION ALL在当前无重复DB上又可能同结果而误收。两类错误不同，不能把全query精确执行相等作为唯一正确性定义，也不推出EX在所有SQL无效。

§4实际SQL Splitter是few-shot LLM，不是已验证AST translator；示例以WHERE TRUE抽出结构、单独抽AI输入/判词，再执行reference/generated完整query与两组件。Autorater读取问题/schema/query/拆分/results，以overall/relational/AI三个1–5分与>3阈值解释；“independent”只指不由strict EX决定，不证明其model/data/semantic oracle独立。§5.1同Gemini3.1-pro-preview/Vertex默认T1/topP.95/topK40、无random seed承担generation/split/autorating；structured output只保schema，不保证split忠实、relational equivalence或AI语义真值。manual生成正确性标签作为作者reference，标签量/重复一致性/外部盲审与operator canonical accuracy未充分披露。

SemBench55 queries/5 scenarios涵盖text/image/audio与多个系统，本文只BigQuery/ThalamusDB，所以不能把Table1全当55×两engine；各engine明确query N未直接列出，不能用百分比倒推出遗漏/人为补足分母。作者人工生成正确率70%/80%，Table1框架accuracy97.2%/93.3%，EX52.8%/26.7%；框架BigQuery TNR90.9%仍误收，Thalamus TPR91.7%仍误拒。无重复draw/CI/独立seed，不给总体正确性或安全保证。Explain&Compare/Miniature&Mull文本baseline另加相同execution数据控制信息差，但模板/分解/模型judge共源仍可能解释收益，未拆各模块独立因果；增加execution数据可使baseline更差，说明prompt冲突而非更多证据必增可靠。完整及split执行/LLM调用额外成本、hardware/precision/end-to-end latency/生产SLO未披露。§6语义等价范围、data-dependent错误、closed/open world与unanswerable/cost是未解决边界，不倒填成框架已具备能力。未核code或复现。

actual Ch66:600–608的三oracle角色区分partition/校准/独立语义真值；1104–1106已有set/multiset、NULL/sort/time-out执行合同，但没有**同一query内确定关系判据与AI语义判据分层，且分解器本身须忠实性审计**。拟窄I `PLATFORM-EVALUATION-SYSTEM` Ch66现Text-to-SQL set/multiset段后、Benchmark compression前≤2段；不改原多重性/三oracle知识owner，不自动申请整章，未获root锁未写。两段literal待独立必要源/owner判断：

> SQL含AI predicate后，正确性不能只绑定一次完整结果相等。Join、aggregation与重复行语义仍有确定关系合同，而AI prompt的relaxed equivalence和边界样本输出需要另一个语义判据；相同查询意图不一定得到相同行，当前fixture结果相同也不能证明DISTINCT等运算无关。可以分别提取关系结构与AI组件，保存完整及组件执行结果，再按明确目标语义评价；拆分器和autorater各拥有自己的忠实性与标签错误，不能自行认证user intent。
>
> 作者在受限BigQuery/ThalamusDB案例中观察到这两侧误判，并用LLM拆分/分层评分改善对人工标签的吻合，但共享模型、无seed重复、小而未明列的engine分母及剩余误收误拒不支持通用正确性保证。更多execution与judge调用增加成本，prompt差异也可能改变真实AI决策而非只引入噪声；遇到复杂SQL、拆分失真、语义标准争议或分布变化时，保留原关系测试、独立人工/执行复核与abstain，不用一次分层高分发布任意AI query。

## 2026-10-01 Designer22086 / CompositionalWM22055 有限必要包

**Designer22086** [exact-v1](https://arxiv.org/html/2609.22086v1) *Evolving Procedural Memory from User Traffic for Agentic Graphic Design*，`2+2+2=6`标准；§3–6/AppD–F/K必要实际读。frozen solver只更新SKILL.md：Widening以canonical uncovered subtask重复kmin3提mint，对no-skill baseline；Deepening以每retrieved skill共同失败计数m2、s=.7completeness+.3aesthetic/τ.6提rewrite，对incumbent。粗归因只负责提案/排序，不证明哪skill导致失败；拒rewrite递增counter、可升级whole rewrite/explore，拒mint保留gap occurrences，不丢proposal/rejected snapshots。每轮50新graded records触发、cap50 selected skills，成败EMA观测值不参与selection/routing。

Replay固定prompt、retrieved assets/upstream state，两arm在same batch fresh rerun，presentation-order swap/relative wins避部分judge drift。主文§3.3/Eq1按prompt的多context多数并要求无prompt lost且至少one won；AppF/Eq5则按record r阈值.5±δ、不得任何record regression，未充分给δ/具体contexts/rollouts budget和prompt↔record归并的统一实现，不能声称两式等价、实际每context零退步或完整gate实现已核。Deepening四prompts=2good+2bad，mint从cluster不按score选；这是局部样本门，不是全流量non-regression证书。pairwise可降低漂移/位置偏差，不消除同family偏好、shared judge error或solver noise，也未证明same-batch drift严格共模相消。

§4五rounds1406 nonoverlap traffic/LLM variants→1869 graded trajectories、76→139skills；231 rewrite proposals reject100/commit131，136 mint reject67/commit69，净63受6retire/merge影响，不把所有attempt都成功。200 human-authored briefs与evolution disjoint但五rounds反复同test，不等五独立generalization cohorts。R4 completeness≥.3为90%<base94%，≥.9仍+7pp；作者解释mint错检邻近brief但没有单独因果消融这个原因。AppD进化reward与报告metric同frozen Graphic-Eval；decompose3–10requirements+met/partial/notmet与PNG视觉score不是真实文档/工具路径验证。AppK无人reward labels/human study尚计划、用户prompt/trajectory/internaltest因保密不公开，不把数据治理声明当独立审计。

§5 matched200 unseen prompts/one batch，cold/rewrite/new/full completeness68.62/69.02/69.79/74.04，full win58.5% p=.025为一个比较，非每axis独立因果、多重检验校正或长期无退步。new139 vsrewrite76的容量/检索描述混杂、组合收益只支持该bank contrast；+28% prompt tokens相对Base、full比cold少token不等离线evolution/replay零成本。Opus4.6/Sonnet4 Bedrock low-think caps2000/5000，Qwen3.6-27B vLLM8A100/65K，900s cap；precision/seeds/repeatedsolver量及总evolution成本未披露。外部8×300 prompts、一般T2I quality只successful generations：Qwen DPG SR44→28.7/quality90.11→86.91，Opus DPG SR89.3→84.7且quality提高；mean successful-generation latency+3.4–6.2%不包含失败/离线成本，不生产SLO。specialdesign GPT5.4两order win总体有升、Qwen GraphicBench49%，不宣称全slice改善。§6明确frozenmodel强默认策略/perception/fine geometry/长程序与局部gate的限制。

actual `AGENT-MEMORY` Ch77:129–141提案/事实owner分权、626–638独立heldout/rollback与1603–1605局部skill证书不自动覆盖新检索家族；`AGENT-PLATFORM` Ch84:1058–1062双gate及1062后matched WITH/WITHOUT目标skill评估、1091–1097 library-time/promotion/currentrun旧revision，承载**更新提案与晋升分权、matched局部有效性不授权全流量**。拟窄E仅此采用，不宣称whole widen/deepen recipe或prompt/record零退步已覆盖/成立；该例的R4反证与局部组合recipe只报告。2026-10-01 07:21：sep22_resume_v3独立亲读该exact-v1必要机制/关键反侧与上述实际owner，窄E通过并同步正式日报；只采用本段明确命题，recipe与局部数字不作整篇覆盖。

**CompositionalWM22055** [exact-v1](https://arxiv.org/html/2609.22055v1) *Benchmarking World Models for Continual Learning on Compositional Tasks*，`2+2+2=6`实际长期差额深入；III-A–E/Algorithm1、IV-A–B/Fig3–5/TableIII/V必要实际读。MetaWorld六sim curricula各由primitives到terminal composition，shared9-channel（三camera）+7Dproprio/action4D，action axis保持scene，perception axis“approximately”固定action，full两者同时；各轴两suite不同任务，不能当同一个fixture正交因子干预。return用failure0/scripted oracle100归一、BWT lower代表less forgetting/FWT只末composition相对scratch学习速度；oracle是sim参考、不生产truth或全axis generalization。shared taskagnostic encoder/dynamics持续更新，每task新的reward/termination/value/policy heads，旧head冻结回读current backbone，避免把policy/reward训练与dynamics复用混为一件事。

III-E用FT/ER5%历史raw transitions/EWC diagonalFisher/PackNet25%remaining free，对DreamerV3和TD-MPC2原生训练差异保留。PWM继承TD-MPC2每task加K3dynamics experts、旧experts frozen、router访问active experts；不断加capacity不和固定budget等价。scratchencoder PWM≈TD-MPC2；diagnostic用所有tasks expert demos先autoencoder训练并冻结，**两模型同checkpoint**，此时平均PWM BWT3.85/FWT36.18 vsTD-MPC2 34.97/38.11，保遗忘但未提高复用速度；fulltask privileged数据和新expert capacity不能归入无特权在线优势。Fig3三random seeds/minmax非CI，参数/compute未控制、单modelsize/K、sim10^5–10^6steps/task，hardware/precision/tokens/完整训练与推理成本未披露。网站附加curves/metricdefs不承载这里采用命题的必要新增证明，未核附件/实现，不称复现。

TableIII axis均值跨四CL methods，TD-MPC2 perception FWT−1.88、full1.54而Dreamer11.79/15.54；作者将其归因decoder recon vsdecoderfree目标但未控制所有architecture/training差异，不当独立loss因果。IV-B路由在Reach/Grasp/BinPnP大体符合reuse结构，PnPBlock/full temporal composition不符；task-conditioned fixedrouter缺阶段适应是作者解释，未独立测试state-router修复。13/14 expert top-preference稳定只是观察；Fig5 prior-only、新-only、uniform对fullmixture既测closedloopreturn也openlooplatent fidelity：prior BinPnP近baseline、Reach/DrawerPnP有return但fidelity跌，new-only/uniform差。其说明部分实际reuse而不是routing权重自证，但不证明唯一component因果或任何时间组合均可成立。V明确sim/reset/dense reward/oraclenormalized affordance，realrobot与稳定非privileged representation仍未来。

actual `MULTIMODAL-WORLD-MODELS` Ch25:155–159模块化/interfaceerror、219–220encoder漂移/representation≠control、754–756action algebra composition与780–784 training-only privilege分别存在；没有**连续学习时旧expert冻结仍受公共encoder变化影响，需matched encoder对照分开保存/复用/新容量，action/perception组合拆诊断**。拟窄I在Ch25可复用dynamics module末、原2606.16489绑定前两段；不重构knowledge tree、不修改既有actor/background分解，root窄锁未授未写，literal：

> 连续学习中的“保留了旧模块”还不等于“旧模块仍收到原来的状态语义”。若所有dynamics experts共享一个继续更新的observation encoder，冻结expert不能阻止输入latent漂移；适应新任务的收益也可能来自新增容量，而非复用。可以把持续学习的dynamics/encoder与每任务reward/policy heads分开，再分别构造保持场景的action组合、近似保持动作的perception组合和两者变化的任务，测先前能力保存与末任务相对scratch的学习速度。
>
> 受限MetaWorld诊断中，持续增长的expert bank只在双方共用“已看全task demos”的冻结encoder时大幅减少遗忘，而forward transfer没有超过单体；scratch encoder下优势消失。路由权重相符只是线索，prior/new-only与uniform消融还需同时看latent fidelity和闭环return。冻结表示、额外专家与回放都有训练/容量成本，特权预训练不是无先验在线解法；表示不稳、阶段组合关系不足或预算不能增长时，保留单体/回放基线与真实任务验证，不从固定router推普遍无遗忘或物理安全。

## 2026-10-01 Proxifield20889 / FOCAL21228 有限必要包

**Proxifield20889** [exact-v1](https://arxiv.org/html/2609.20889v1) *Proxifield: Decentralized Multi-Agent Communication through Semantic Proximity*，`2+2+2=6`因actual长期差额深入。§3/Eq4–12、§4–6、A.2–3/B/D/E.1必要实际读。每round各agent生成message/provisionalaction/rationale/needs/addressee，再由text embeddings的need-match、plan-align、information-complementarity与explicit address造有向图；need edge从请求方→可能知道者，reply反向。addr优先并受cap，三semantic score取max而非加权sum，λ=.90/.85/.80人工设非learned/calibrated、Cin3。global降序/idtie-break在sender k/receiver Cin内选，coverage可超sender k、不超Cin；不能给每sender k严格调用/总Nk边界，coverage也依赖可用可行edge。所有o/memory/proposals被router读并batched embed再全pair比较，这是确定路由而非无全局协调依赖；不需LLMplanner不等router无state/通信成本，pair score工程上仍随候选pairs增长，不声称作者实现已测复杂度。

recipient同一call评价所有inbox/结构reply Accept/Reject/Counter；只有**非空且全部routed recipient有reply并Accept**才能跳过final LLMcall，reject/counter/missing/no recipient走本地commit，counter advisory不binding。sendercommit仍policy输出、同步apply环境，不是Byzantine quorum/真实副作用exactly-once/独立safety证书。每round2N–3N generativecalls另计embedding/每5step递归summary，旧edge不继承；小于2peer退直接action。

DSSE sim离散searcher/scout与team-size同时扩grid/sites/survivors，HiddenBench固定共享误导事实+私有正确事实、3/4agents，无Star以免central直接得allprivatefacts破构造。Qwen3.5 35BA3B/122BA10B/397BA17B OpenRouter no-reasoning/T.3/maxout5000、Starorchestrator恒397/输出cap随N扩；shared compression/T.2/faithfulness与boundedblackboard5N calls，Star2N+1，并非等调用/等总tokens对照。五prespecifiedmatched seed控制env/factorder/dropout不控制provider sampling；hardware/precision/end-to-end latency/SLO未披露。122模型所有protocol较35差，不支持普遍size单调；Hidden35 shared.77>Proxi.63，而397 k1.79/k2.81>shared.78，显示routing依赖表达needs/peer评价能力，不所有尺度winner。k2 DSSE几乎无益、额外调用有成本；无fourlane/component独立消融或其他先进decentralized baseline，不唯一归因某lane。

N5/25/50 scaling仅DSSE；permanentdropout每agent独立q→hazard、taskworkers跨protocol同dropout但Starorchestrator额外可离线、且要求至少2taskworkers活着，非无条件q law或任意network故障。q.8 Proxi保73.6%自身no-faultreward vsStar38.8/shared58.3，五runs/60of100survivors不作真实可靠性保证；router/embeddingservice故障、延迟丢包、Byzantine/恢复join未测。API response_usage近似黑箱有variance、不包括完整engineering/embedding/总criticalpath保证；Hidden比naive Discussion贵2–4×，不可只叫低成本。§6仅一个scaling/faultenv与modelgap限制。

actual `AGENT-MULTI-AGENT` Ch82:186–210 runtime process-risk触发有限topology mutation、211–224 peer posterior delegation；现有未承载**每round基于need/plan/complementarity deterministic重建有cap的peer proposal graph，与最终actioncommit分权**，不是同一error-triggeredstructure repair或learnedcapabilityselector。拟窄I在peerselector解释末、CommunicationBudget标题前两段；不改Workflow effect owner。root锁未授未写，literal：

> 动态协作还可以不等待故障才改拓扑，而按每轮当前信息需求重建有界通信图。各Agent先给行动proposal、信息needs与可选addressee，router用需求与peer观测/记忆的匹配、计划相似及信息互补来分配边；direct address优先但不绕过receiver容量。确定图选择不需要额外LLM planner，却仍消费全局候选metadata、embedding与pair比较；coverage补边若允许超sender预算，成本证书必须保留这个例外。
>
> 图只控制这次谁看见哪份proposal，peer reply只是行动选择证据：非空接收集合全部Accept可以省一次本地生成，但missing/reject/counter应回本地决策，不因语义相似或共识取得真实effect授权。Proxifield的受限sim结果显示needs表达与基模型能力、团队规模和permanentdropout会改变选择收益；比较调用预算不等、全局router故障未测，也不证明Byzantine或真实网络可靠性。关键证据丢失、不可逆动作或SLO不允许多轮时，保留固定workflow、可读handoff与独立verifier。

**FOCAL21228** [exact-v1](https://arxiv.org/html/2609.21228v1) *FOCAL-VLA: Subtask-Guided Geometry Distillation and Implicit World Modeling for Vision–Language–Action Models*，`2+2+2=6`标准，III-A–D/Eq1–7、IV-A–C/TablesI–IV/V必要实际读。π.5/PaliGemma当前多view/instruction/proprio C，8geometry与8motion queries各只读C/本组，action同时读C+两组；semantic subtask text的causal LM loss只塑形shared C，C/geometry/motion/action不读teacher semantic targets。部署没有teacher/futureframes/masks/subtask标签，仅当前C生成两组latents，不能把名为implicit world的feature当运行时真实未来。

VGGT完整currentviews前向，offline Qwen3VL8+手写subtask+sim/GroundedSAM2 wholeentity masks（不gripper）**只在pooling选择patch覆盖**，validviews平均+train-onlymean/std归一MSE；不是teacher只看ROI或数学独立场景外信息。Track4World完整current+Kfuture跨全actionchunk不在subtaskboundary截断（RoboCasaK10/H50），currentmask选source-index-zero/global temporal-aggregator256D feature，SmoothL1β1；不是直接预测重建pointtrajectory或在futuremask挑未来对象。不剪cross-subtaskfuture背景，错误boundary/mask可给有偏target，未来信息是训练privilege。

LIBERO40tasks×50episodes，policy10steps/action；RoboCasa Atomic24Human50/3views/50chunk执行25replan/50episodes每task；full RoboCasa63.4 vs同train/evalπ.5 55.2。其余simulation baselines来自不同cited来源/reimplementations不全matched；LIBERO97.9 vsπ.5 96.9，Goal97.8<98.0、Long95<Track4Action95.8，不alltask优胜。Franka+单fixed Orbbec/350successfuldemonstrations50–150pertask/10Hz/640×480，四tasks各20trials、同initial-layoutdistribution但不披露pairedidenticalseed/repeatedtraining/CI；47.5→63.8作者限定成功顺序/终态，小样本遮挡仍失败，不安全保证。

8A10080GB/endtoendAdamW、sim30k updates/batchLIB256/Robo128、real16k/b256/nativeofficialseeds不等多seed重复，precision/部署HW/latency/offlineteachercache总成本未披露。RoboCasa同protocol消融full63.4、noGeo60/noMotion59.6、task-union61.9/fullimage58.7、supervision-only58.5：direct conditioning与局部scope有作者局部增量，但removequery+loss捆绑、λ/预算及annotation作用不独立，1.5pp不有CI，不给唯一3D/dynamics因果。mask/teacher只训练带离线预算、annotations/targetquality/跨embodiment未验，未核code/复现实验。

actual `MULTIMODAL-EMBODIED-VLA` Ch26:71–88已承载taskobjectmask/privileged3Dteacher与部署移除/非geometrytruth；285–291已承载training-onlyfuture feature/point-motion target、runtime删aux和latent≠persistent/action-conditioned environment state。拟**窄E**采用这两个直接实际命题，由该current/未来teacher交接证据限定；subtaskpooledtarget、两query直接conditioning及其受限消融作为recipe仅报告，不声称wholeFOCAL已覆盖。若独立复核认为“currentmask读取future-enriched feature/直接conditioning而非auxonly”是新必需选择，可仅重开此差额，不以此重新全篇/别日扫描；2026-10-01 07:21：sep22_resume_v3独立亲读该exact-v1必要机制/关键反侧与上述实际owner，窄E通过并同步正式日报；只采用本段明确命题，recipe与局部数字不作整篇覆盖。

## 2026-10-01 MT-WAM21474 双流必要包


[exact-v1](https://arxiv.org/html/2609.21474v1) *MT-WAM: Reorienting the One-Pass Predictive Representation Toward Action Generation*，`2+2+2=6`因actual选择差额深入。III-A–F/Eq1–6/Fig2–3、IV-A–C/TablesI–VII/V/AppA–B必要实际读。Fast-WAM onepass currentreference→videoKV供action；MT两content-identical reference copies在positionencoding前相同、ref互相attention/不读noisedfuturevideo，futurevideo可读两ref但action不读futurevideo。后M10 blocks另copy tail（不是整个新expert），motion/visual streams从同branch-reference hidden初始化、learnable embeddings/各FFN不同且跨stream attention禁止，无Topk/router/balance；video/action/branchjointtrain，VAE/textencoder frozen。

CoTracker3均匀grid源点以f0为零测future2D cumulative displacement，P未来帧含horizonendpoint、γVAEcompression归一；padded/invisible mask但staticvisible nearzero仍valid，不直接metric3D/contact。DINOv2ViTB14 futurepatchcosine目标不含f0，frame mask/各samplecamera归一，motionMSE与featurecos loss不用flowtime；video/action retainedflowmatch各time独立。**motion tokens直接条件action且收action+motionloss，visual tokens不作为actioncondition，却经reference计算与joint梯度塑形sharedbackbone**。因此no visualKV不等visual branch没用；预测head部署删、currentvideo/motion cache每replan各一次，actiondenoise复用，skipfuturevideo的前向可见性来自mask，不是未来target部署仍可读。

Wan2.2TI2V5B初始化video/actionexpert（shape不合线性interpolate/widthscale、actioninout随机），8A100/ZeRO1/bf16/AdamW，λvideo/action1,motion.5,feature.25。LIBERO10epochs16h/b96；RoboTwinCleanRand5ep4days/b48；Clean2Rand stage1五ep4days50Clean+500Randomvideo/task也trainbranch，stage2五ep18h仅50Cleanpaired/b48，**无Random action不等未见Random视觉**；real400demo10ep17h/b48。TableVI32actionchunks/33obswindow/2–3camera绑定设置，trainingtimes不表明所有baseline端到端总成本等量或额外teacher/precache免费。predictive teacher额外预算/motionvisibility错误仍在train成本与bias，未核code/复现。

IV LIBERO98.2 vsFast97.6仅+.6pp/Object−.8；LIBEROPlus10030variants/7axes73.66 vs49.86，而Joint68.41是不同future-generationbudget，其他WAM/baselines额外pretrain/初始化不全matched；RoboTwin50tasks每Clean/Random100trials，CleanRand93.22 vs91.83；Clean2Rand19.4Random仍大幅低Clean75.56，HALO26.4/Bagel20.5反胜且pretrain不同，不allwin/无视觉先验泛化。UR5单双臂/RealSenseD405四tasks×100trials、400demo同initialconfigs/随机两背景、77.8 vsFast67，π.5 74.5别pretrain；未披露多seedCI/paired不确定区间/physicalrisk，不安全SLO。

IV-C关键one-attention-rule control维持two streams/objectives/参数：让action再读visualtokens73.7→70.9，六axis降而Noise+1.9；**额外training signal有益≠其tokens应进入actioncondition**。removevisualstream73.7→68.8改变branch/objective/容量，不单loss因果；depthM5/10/20互换shared/copy参数，M10总体优而M5Robot/M20LightNoise优，无普遍depth单调。M20总体比M10低1.5，不把M10称验证最优或单一梯度干扰机制。没有repeatedtrainingCI，不把2.8/4.9pp说统计显著。

TableV同singleRTXPRO6000 96GB inferenceconfig，Fast296.325ms/3.736949TFLOPs，MT313.480/5.142984，+5.79%latency/+37.63%FLOPs换该qualitypoint；Joint503.729/30.672534又含futurevideo路径，不叫同质量等算力加速。测时端到端boundary/precision/repetition/P99/持续controlSLO未给，平均forward不授权deadline。V一backbone/UR5/2Dtarget与更长任务/embodiment未验、teacher运动feature不等因果世界状态保留。

actual Ch26:265–281三类future通路/gradient目标与干预，285–291trainingonlyforesight≠persistentstate已读；尚未承载**同一auxstream的训练收益和直接条件化收益可以方向相反，需两种控制分别决定部署保留对象**，非仅“target不是truth”既有边界。拟I `MULTIMODAL-EMBODIED-VLA` Training-only Foresight三段后（291之后）、futurevelocity分支前≤2段，root必要peer/窄锁尚待，未写。literal：

> 训练期有用的预测stream，不一定应成为action head的额外条件。一个可诊断分支保留共享current-observation context，让motion与visual-feature目标分别通过隔离的stream训练；motion tokens可供action直接读取，visual-feature目标则只经训练梯度塑形共享backbone。应分别控制“删除这个监督/处理分支”与“保留它但改变action可见性”，不能把前者的收益自动转成后者的部署读取权。
>
> MT-WAM的受限同参数/目标attention对照中，删除visual分支降低整体成功率，保留分支却让action再读visualtokens也降低整体成功率，说明两种选择不是同义；单个Noise切片仍反向改善，未建立普遍禁用规律。额外copytail、teacher targets和训练预算换来不生成futurevideo的轻量路径，缓存只按当前replan重建；图像2Dmotion与feature监督不构成物理状态真值。分布变化、辅助目标冲突或延迟超界时，回退原directpolicy/较短chunk或经验证的同步路径，以真实闭环结果而非latent预测分数决定动作可用性。
## 2026-10-01 ZYT-World21712 有界必要证据与投影接口差额

[ZYT-World: A Real-Time Controllable World Model for Closed-Loop Autonomous-Driving Simulation exact-v1](https://arxiv.org/html/2609.21712v1)。已具名完整题摘的混合projection、causal与memory机制保留，本次没有新发现。公开身份复用本日official Mon21 cs.CV New，原题名记录第369行；公开时钟为09/21 08:00 BJT，不拿Submitted当公告。拟`2+2+2=6`，实际采用长期接口差额则深入受影响范围；尚未独立采用或计正式35。

§2.4/3.1–3.6：四fisheye+三pinhole保native T×h×w grid与semantic camera slot，不按batch位置猜view。cross-view只同latent时刻合并、不用异projection网格2D RoPE；physical overlap mask保24/42有向inter-view pairs，不是总attention FLOPs减少43%。共6D unnormalized Plücker字段，pinhole/cylindrical unprojection不同、可表达>180°后向ray；common field dimension不强迫common encoder，按slot分projection-family adapter。ray/layout对齐目标token grid需d·s·k=32、因果时间packing首帧重复后续四帧不取平均；dense camera与layout在noisy stream加入，clean history不直接读该condition。全局AdaLN另读同相邻pose增量的planar tx/ty/yaw，roll/pitch/vertical不是显式条件，不能称完整6DoF已控制。

§2.4/3.6记忆：4DGS从同real capture渲染安全约束alternative path作memory、原实拍为target，近百万pairs避免game-engine appearance却不消除rendered-memory→real-memory域差异。3空间+1近时reference、20m/45°等为数据侧选择，只有frontwide/narrow直读memory、其他经current-view attention传播；relative pose/time身份与rolling KV不同，static/place提案不是真实persistent state。§7.2.2 Table2固定40step sampler但两checkpoint分别训练、249scene/1743viewstreams/72frame single split无CI；FID略退11.64→11.72，不能说每项改善或独立memory因果。§7.3.3无standalone quantitative revisit benchmark，只qualitative remembered details。

§4.1–4.6/7.2.3：clean-history TF→causal CD→self-rollout DMD；teacher/scorers可读full7view/future、student只因果history，后续RigCritic训练fullrig discriminator+LPIPS，不是部署几何verifier。无条件clean历史与有条件当前noisy流分开，prune检查token/12step误差1e−5只该计算配置，不任意精度保证；训练T21latents/8.1s，推理bounded W7/S3/sink+recent和globalposition延伸76latents/30s。三AR operatingpoints分别训练，不是同checkpoint采样步消融；1step多数teacher质量指标退，2/4step分别有优势。§7.3.4/5 RigCritic改善和30s两例仅定性，没有大规模长期稳定、policy-level闭环或安全保证。

§5.3.5/6.4/7.1–7.3/8只核必要成本/评价权限：AR-phase training加速不归pretraining、local speedup不可相加。39.6×是generator first-latent同40step teacher一latent基线，不是fullclip比较；107.7×是另Fig2 generator-only timing，4FPS是另W8A8/fusion/twoGPU engine operatingpoint，不互换为closedloop SLO。TinyVAE fixedlatent reconstruction与generated-latent质量不同，char_sim仍.3334<Wan.4715，不用LPIPS概括全部文本保真。作者图像/运动/检测/Sampson proxies明确不代policy-level评价，未核code或复现，无实机安全采用。

actual `MULTIMODAL-REPRESENTATION` Ch23:691–705已有query-view ray geometry/raxel与独立camera conditioning共存，尚未承载**共同ray field维度与projection-family encoder权限分开、保持native grids后跨view只共享时刻和几何身份**；Ch25:510–573已承载history vs retrieved references、memory use因果审计与causal selfrollout，不能将整memory/distillation重复当新I。拟唯一Ch23 query-view ray两段后、只读mesh pipeline分支前≤2段；只投影接口机制，不写整训练/引擎recipe，不宣称adapter收益已独立证明。root有限采用裁决待办，无窄锁未写。literal：

> 多视角共享射线字段，不一定要共享同一个condition encoder。pinhole与超广角fisheye可以都用六维Plücker接口，但各自的unprojection和方向统计仍不同；保留原生pixel/token grid，再按semantic camera identity分派投影族adapter，可以避免仅凭相同shape让backbone猜测相机类型。跨视图attention可在同一latent时刻合并不同长度的tokens，以标定射线和view identity建立联系，而不把不同投影网格的二维位置直接视作可比；全局ego-motion与逐像素几何也应各自保留来源与职责。

> ZYT-World给出这种混合rig的受限实现，用额外adapter、标定/pose处理与overlap mask换取原生视图接口；训练与推理时的投影族、语义slot和token-grid packing应一致，这是由接口推得的验收要求，不是论文已证明任意标定都可靠。现有评价没有独立隔离投影族adapter收益，生成/几何代理和定性长rollout也不证明物理闭环安全。标定、projection dispatch或packing不可靠时，保留独立相机处理、已有显式几何接口或受限重标定，不把共有字段维度当作encoder可互换的证据。

## 2026-10-01 MACE21533 内容组合与消费格式的交互差额

[MACE: Memory-Agent Co-Evolution with Adaptive Memory Graphs for Multi-Agent Systems exact-v1](https://arxiv.org/html/2609.21533v1)。原具名题摘准入不重新发现；本日Mon21 New身份/时钟复用，`2+2+2=6`因实际长期gap深入受影响范围。实际读§4–6、AppA.1、B.1–3/B.5、D.6–7、E.1–4；不遍历其他附件、未核code/复现，未计完整处置。

决定性§4/Fig1c/AppA.1：C1按currentneed相关性选unit，C2额外保support/complementary unit；各composition固定后分别呈guide/checklist，保相同事实/constraints/receiving agent/insertion/token allowance，每task跑四pairings。S1–S4由执行前complete/partial inputs×local/cross-experience需求分组。S1 guide C1约82>C2约76，checklist C1约59<C2约78，是受限交互而非只换template的总体数字。Fig1d memory library/rules固定，contextwise Fixed保初始pair；Separate分别平均composition跨format、format跨composition后各自选择；Joint更新每个pair。每calibrationtask提供四pairing全部outcomes、三policy共享历史，heldoutprobe不回更新。192calibration时Joint约85/Fixed78/Separate75，支持该校准集保留配对信息，不证明仅观察已选单路径也能同样在线学习；未披露此诊断的独立重复/CI和全部校准调用预算，不称统计显著/无额外探测。

§5.2–5.5：functional graph cell保内部dependency/source，外层support/conflict等links另存；TopBt按unit数、再每agent render tokenbudget b控制，不是总全生命周期token硬cap。role/stage/currentstate匹配后patch记录content/mode/format/timing/strength/placement/source；成败trace须绑定usedunits、patch和下游outcome。Eq12只对usedunits将共同trace return做EMA，不识别每unit单独causalcredit；同outcome写unit与配对偏好不能说明unit内容更真实。AppD.6–7先prediction/scoring、后写gold-derivedfeedback/scorer-only gold，read-before-write保证当前query不直接读当前答案，但不证明任意未来任务无共享gold/contamination或production truth。

§6/AppB/E对照/负侧：local Direct/MAGMA/SAGE/MACE共享preparedfiles/parser，MMLU首153非imported G-MAS seed42-500，hidden配置/rawpredictions缺失的imported行不作controlledcomparison。4728queries八任务指标不同，single-run row/未披露backbone精确identity、hardware/precision/温度/seed重复和完整维护预算；多domain宏均值不等普遍任务能力。T2 memory/Coupler/feedback消融总体下降，但LCB v6删MemGoG/Composer/Coupler/feedback/fixedmode都高于full49.14（50–54.29），不说每组件每task必要。

Table3 Direct/MACE paired runtime，MACE4calls/6.87K tokens/11.06×relativecost/1.36s perquery vsDirect1call/.60K/.22s，不能只报比SAGE2.41s快或把relativecost当当前价格/部署SLO。T3mean/total4728批评估不含完整历史构建/全部校准成本，未签尾延迟。EQ4 network/memory噪声变化受限，timeout retry/failopen空patch不是容灾完备；换MACEbackbone还用固定Direct/SAGE reference不等matched三模型胜，噪声与budget有另子集分母，不能互并主表。

actual `AGENT-MEMORY` Ch77:243–269已有selection proxy/outcome feedback不是单条因果credit；330–332已有writer/reader按不同modelprofiles适配，1525等rendering必须版本化。尚未承载**同一内容组合在两种消费格式中的排序可反转，边际composition score与format score丢配对交互**。拟唯一Ch77 Fact State与Retrieval-policy State的tradeoff尾、Memory retrieval evaluation identity首段前≤2段，避免与AutoView21940的Consolidation前seam冲突；不重写全MemGoG或joint训练recipe。有限非作者source→actual/literal未过，不写Books。literal：

> 记忆selector的效用还可能与消费方式相互作用。即使来源事实、receiving agent、插入时机与token预算不变，同一组证据作为guide或checklist呈现，也可能改变两种内容组合的优劣。应保留“所选unit集合×消费配置”的配对identity及结果，而不只分别维护unit/composition的边际分数和format的边际分数；这些分数拥有选择权，不拥有事实真值或单条记忆的因果贡献。

> MACE的受限四配对对照出现组合排序反转；在固定库与共享反馈下，按配对更新比独立边际更新的heldoutprobe结果更好。但每个校准任务观察四种配对，额外探测预算、有限重复与context人口限制都须保留，不能外推为只观察当前已选配置的无成本在线最优。写回同一trace return也不证明所有usedunits贡献相同。配对记录与探测增加调用、token和维护成本；支持稀薄、人口或reader变更时，回退已验证的固定组合/呈现，先做匹配对照再改策略，不以聚合分数自动晋升。

## 2026-10-01 OpenMAS-GCom21527 有界诊断与窄已有覆盖提案

[OpenMAS-GCom. A Diagnostic Benchmark for Graph-enhanced Multi-Agent Systems exact-v1](https://arxiv.org/html/2609.21527v1)。既有Mon21 New身份与公告时钟复用，不将Submitted18Sep当公开时刻，不新增发现。`2+1+2=5`标准必要审阅：实际读§2.2、3.1–3.4、4的组织/role/message/worker对照、AppA.4–A.8及B.5–B.6；A.9只偶然呈现部分表，不声称完整读完、不遍历全补充结果或代码。新增证据是相近baseline分数不能预测污染/worker失效退化、accuracy冠军不等单位token冠军，若成立会改变选拓扑的验收对象，不是仅有17配置排行榜。

§2.2/3.3对比完整执行：共同任务、backend、prompts、decode/routing、stopping与预算上限，固定上限不等实际calls/tokens/latency相同。Degree-preserving directed edge swap保持节点/角色/入出度/edgecount，拒selfloop/重复/无效role连接；node removal同时删角色及incident edges，并未隔离prompt角色与资源/拓扑因素。Info按eligible upstream items换成格式有效但错误的候选，比例不是实际下游采纳比例；A.4/A.6 trace另记是否reach/adopt/correct/ignore。Worker k=0–4停在指定点，保last valid shared state及配置retry/fallback/reroute，不证明任意故障恢复。3.4与A.6保配置hash、parser/rawprediction、实际执行边/node、retry与成本，组织配置不等实际运行trace。

§4局部对照与关键反侧：degree rewiring平均81.88→70%时74.99，退化6.89pp而非相对6.89%；No critic81.30、No specialist78.30，MMLU-Pro删critic还改善，不证明critic普遍有益。MAD85.30/VeriMap85.50 baseline相近，80%错误消息后44.41/54.59，支持局部error absorption差异，不唯一归因verification模块。GoT84.22→四worker失败76.80、AutoGen83.82→73.80，不等matched recovery-enabled/disabled恢复实验。Complex400 frozen tasks上GoT EM50.25最高却用26.47K tokens/45.46s；AutoGen23.50/3.39K的EM-per1K约6.93高于GoT约1.90，且不同方法不能共享单一部署SLO。评分严格检查字段/值/引用/checkpoint/checksum；parser失败与内容失败分账，reference程序不是开放世界真值。

AppA.8不统一统计权限：s221为3×500任务样本的mean/SD，r152与m3 run-seed/backup-seed SD但run数未记，e34为.70数据/.30方法的加权经验估计而组件样本数未披露，b100为二项SE假设，不能全部当训练重复或paired CI。精确backbone/hardware/precision及完整构建预算未披露，不从接口协议推导全量独立复现。B.5只是revision/config对齐的reimplementation validation protocol；B.6把budget-matched single/iterative/independent controls、preserve-node/edge role replacement、rewire output reachability/scheduling/schema验证、matched recovery on/off和task/template paired bootstrap列作后续工作，不能倒填为已执行的归因控制。

actual `AGENT-MULTI-AGENT` Ch82:58–98已具体把task-topology matching与baseline headroom、error absorption/amplification、success-per-token/critical path连成同一验收链，并明确共同工具/prompt/总reasoning预算的domain dependence；`PLATFORM-EVALUATION-SYSTEM` Ch66:171–184冻结architecture/protocol/runtime/workflow subject identity。拟窄E仅采用**baseline accuracy≠错误吸收/worker失效下完整执行质量，质量最优≠资源效率最优，预算上限≠实际资源记录**，不是全四干预recipe已有覆盖。局部差异/角色曲线和后续缺控制只报告，未发现必须改正文的长期gap；仍待非作者source→actual裁决，不计完整处置、不申请Books锁。

## 2026-10-01 批A实际写入待非作者写后

root已必要source→fresh actual/literal通过并授Ch26三个窄锁。作者实际写MT21474:293/295、Safe21223:763/765、Commit21908:785/787各两段，独立exact-v1 link/SF、旧邻接保留，限定diffcheck通过。MT实际第二段已分开remove-visual改变容量/目标与保两stream/参数/目标的attention可见性对照。仅记录实际写入，三处仍待root非作者写后，正式完成38不因已写自动增加。

07:51 root非作者实际亲读三新段及相邻路径写后PASS，必要源复用，三位置锁释放。保teacher预测/物理truth、safe-success分母与两种visual对照不同权限；正式41=23深入/17标准/1D、21I/17E/2Only/1D。上段待写后是作者提交时快照，现已闭合三单篇，不代日级Gate。

## 2026-10-01 Queueing20957 三参数近似与容量/延迟目标分账

[An Approximate Queueing Model of LLM Inference Serving for SLO-Driven Autoscaling exact-v1](https://arxiv.org/html/2609.20957v1)。本日既有官方Mon21 New/公告归属复用，不按Submitted17Sep改窗；既有完整题摘准入`2+1+2=5`，本轮标准必要IV–X已实际读，不遍历Appendix A/B或代码，不声称解析证明/实现复现。原增量是iteration-cost/occupancy近似驱动TTFT与ITL容量选择，并实测“用ITL校准throughput不等约束ITL”；不只记录headline误差数字。

IV/V关键条件：Poisson arrivals、输入/输出独立并以均值代替每request、同质mean-field batch。α为iteration overhead，β为token compute，γ为KV read/write时间；有效prefill stage c(i)是tokenbudget耦合的近似、非runtime实际chunk数。各stage均权平均得到T(i)=α+iδ，state-dependent birth/death service rate只在ρ<1稳态，mean occupancy再近似prefill/ITL/TTFT；TTFT含queue+prefill+firstdecode，不能当request tail分布。周期重估meanarrival不捕获周期内burst/correlation，作者明确bursty等待/TTFT倾向乐观；饱和周期又从fit排除，不能由解析发散自动证明能守所有SLO。

VI/VII：H100 vLLM、Llama3.1-8B/Qwen2.5-14B，4×4 meanlength64/256/1024/4096、每request独立uniform[x/2,3x/2]。每sweep删throughput-saturating和最高两Poisson rate，只112/model、共224light–moderate点；B256/M8192。Nelder-Mead jointfit这些TTFT/ITL points，4.6/7.9% ITL与13.6/15.8% TTFT为mean absolute deviation/mean measurement，不是heldout预测保证、逐request百分位或CI。β/γ的硬件数量级合理性是aggregate fit解释，不等kernel profiling已复核；precise运行dtype未充分明示，BF16仅物理检查口径。初fit多observations避免把queue delay全算α，后sliding window以上个fit初始化、饱和周期不收；窗口/计算与漂移代价不能省略。

VIII–X实际控制/反侧：模型collector/tuner/analyzer/actuator只测同H100 replica sizing，accelerator-assignment实现路径未测。IX只是把WVA decode-throughput analyzer sizing/defaults接同collector/directactuator，不比较完整WVA。Llama8B/vLLM0.21.0/H100 oneGPU/replica、prefix cache关、B256；两44min固定shape/Poisson-ramp四倍profile，同controller image/config/loadseed，每arm单次、63/64 cycles。30s measurement加采集/actuation约42s完整周期；TTFT target50/ITL25与另一200/13由模型选绑定点，不全业务目标。原文TableV的7/127 vs27/128是cycle mean超某target的union，cycle P90仍非请求P90；throughput arm少4%/28%meanreplicas是明确成本取舍。ITL-bound两arm无standing queue但active occupancy更高可超ITL，观测ITL参与供给估计不授未来target约束。单run/no variance、固定shape、同周期online calibration与lightload条件保留，不从127周期当127独立实验，不说forecast startup已做（X未来方向）。总工程/控制器耗时、完整dtype、生产请求tail/多峰/突发/general hardware条件未证实。

actual `INFER-SCHEDULING` Ch56:43–68已把throughput/goodput与TTFT/TPOT SLO及predicted queue+service admission分开，386–390明确同slot数量不等iteration work/KV cost，649–656已把容量/预测/ready与SLO验收分账。拟窄E采用**decode capacity足够或ITL用于校准不等未来延迟目标满足，active batch可在无queue时增加iteration latency；近似容量proposal仍须实际SLO验收**。三参数方程/均值Markov配方和该单次成本取舍仅报告，不说全部modeling已有覆盖；若独立复核认定occupancy均值与tail目标的差额必要，则仅受影响owner重开，不自行补书。当前作者必要source→actual齐，待非作者有限采用，不计完整处置。

## 2026-10-01 批B实际写入待非作者写后

root必要source→actual/literal独立通过，仅授四Ch66窄锁；作者真实各两段：Evo21257:216/218、ODU21392:391/393、SQL21133:1118/1120、Judge21277:2410/2412。独立exact-v1 link/SF、旧机制/邻接保留，限定diffcheckPASS；comparison admission/operation failure、oracle intent非live gate、shared splitter与judge权限、PR/MSE目标反向均在实际正文。已送root写后核，本条不增加正式41。

08:16 root实际亲读上述四项新段与相邻交接并复用定点necessary source，写后独立PASS、四Ch66锁释放；正式45=27深入/17标准/1D、25I/17E/2Only/1D，上段提交快照不覆盖此实际结果。仍不是日级Gate。

## 2026-10-01 RBS20971 有界几何救援与双mask差额

[RBS-Attention: Radius-Bounded Sparse Prefill for Long-Context Large Language Models exact-v1](https://arxiv.org/html/2609.20971v1)。既有本日Mon21 New/公告与完整题摘准入复用，不扩来源。`2+1+2=5`原标准；本轮§3–5/7、A.1严格density匹配及E.1–3关键界/反例已实际读，因actual明确选择器差额深入受影响内容，不遍历B/C/D/代码，也不声称全系统复现。

Method/E：block centroid c、max L2 radius r给任意key的qᵀk≤qᵀc+||q||r；用当前prompt/layer/KVhead radius median→P90归一β，β<1的attenuated rescue是风险score、不是upper bound，K={−u,u}/q=u可直接反证。rP90>median才给该表达，必要范围未核退化quantile实现，不替作者补ε规则。base和rescue分别用query-block sumexp/各自max的relative threshold，再union forced sink/window/recent；某block radius uplift抬高全branch threshold可让未降score的别block退出，rescue-only不保base，双mask才保持base候选。L2与Quest box两个合法界无统一tightness顺序，rotation invariance不等任务质量最优；即使full upper bound+TopK也不保证真正global-key或attention-mass保留。执行只对retained causal keys做token dot/softmax，不dense exact，不改KV驻留或宣称decode已加速。

§3.3/4：selector O(N²d/B)及scores O(M²)/可选token-centroid O(NM)workspace仍可能二次，metadata O(Md)不能概括peak。实际density计全部valid causal pairs/两mask overlap与forcedblocks去重，threshold不是固定TopK或exact预算；固定threshold到不同prompt/layer density会变。main H100 Qwen3MoE FP8/vLLM0.10.0/FA2.8.3 timing16K–256K；A100 controlled sameprefillbackend/B128、MoE TP2/denseTP4因shard限制，不混两平台latency或官方Quest decode性能。128K 20.65×standalone、11.92×vLLMattention、5.97×TTFT三个边界不同，default operatingpoints未同density；短context可接近/低于dense，runtimequantile与selector成本不免费。

§5/A1/E反侧：nominaltargetTable1 density不同，A1新增accuracy-only points才within.10pp，不能配另threshold的latency。5.34%RBS80.28 vsMInference76.87/Flash74.73支持局部预算取舍；130 RULER diagnostic同backend/B128/density5.3左右76.67 vs73.63/72.41/73.71，但between-method paired bootstrap差区间含0，不称显著或唯一组件因果。denseQwen RULER88.65<89.52/LongBench.376<.394，MoE.370<.388；InfiniteBench部分task与dense/其他sparse反退。LongBench503quality的density只60 selector-only样本，RULER按每task/length一个样本，非整个accuracy集精确预算。Video1000/32frames仅质量，H100 MoE速度不外推dense或VLM；P99/concurrency/genericSLO、完整calibration/peakworkspace测量未在本轮采用范围独立核，不采实现可部署保证。

actual `MODEL-SELF-ATTENTION` Ch14:276–286已有support/normalization与统计近似不保output，但尚未承载**为救援某block提升score会抬高relative threshold并删原base候选，保留两mask再union才把救援增量与原相关性选择分开**。Owner是通用support选择而非Ch45 KV驻留；唯一拟seam在hierarchical support总结后、“可训练 gate”之前≤2段。几何score/dual-mask局部新选择够窄I提案，不纳整个RBS recipe，待root source→actual/literal及窄锁。literal：

> 粗粒度support选择还要防止block平均值掩盖少量重要key。质心可用低成本表示平均相关性，块内最大半径则提示它可能漏掉的局部偏差；完整L2半径能给单个key logit上界，但按分位数衰减半径后只剩风险分数，不能继承这个界或dense输出保证。救援分数逐block增加并不意味着原候选都会保留：若按全branch最大值设相对阈值，某block的提升也会抬高别block的入选门槛。

> 因此可以分别阈值化base relevance与rescue risk，再合并两mask和明确的保留窗口，让救援只增加选择、不会静默覆盖base集合。RBS的受限同backend/实际density对照支持这一选择，但小诊断集差区间包含零，未证明唯一组件因果或普遍质量保持；相同threshold也不承诺相同cardinality。半径统计、两路score/union与workspace都有成本，块大半径不等当前query真相关，prefill结果不授权decode收益。保留不足或selector成本、质量回归失配时，放宽预算并重新校准，或回dense/fixed support；KV驻留与实际kernel收益仍交缓存/runtime独立验收。

## 2026-10-01 三窄E独立通过与C实际提交

root非作者必要source→actual通过Arena21378、OpenMAS21527、Queueing20957：Arena仅process credit/admission≠causal truth/写入权；OpenMAS仅task/topology/error absorption与质量、资源账，B6未来controls不倒填；Queueing仅capacity/ITL calibration≠未来SLO与无queue仍有active-occupancy成本。正式48=27深入/20标准/1D，25I/20E/2Only/1D。均非whole recipe Existing，前段待采用是过程快照。

C source→actual/literal已root通过并授两Ch25与一Ch23精确位置，作者实际各两段SharedFault21155 Ch25:68/70、Compositional22055 Ch25:165/167、ZYT21712 Ch23:695/697，独立exact-v1 link/SF、限定diffcheckPASS。旧16489 semantic-body-binding保紧邻旧module，22055在其后/Goal前，避免旧源误绑定；已明确告root请求该seam定点复核。三处实际写后尚待非作者，不计正式整合。

## 2026-10-01 Test-Time Communication21032 有界必要证据与进展共享提案

[Scaling Discovery through Test-Time Communication exact-v1](https://arxiv.org/html/2609.21032v1)。既有官方Mon21 New/08:00 BJT公告身份与准入`2+1+2=5`复用，不新增发现；必要§2、3.1–3.3关键评价、3.4与AppA.1/A.6实际已读完。3.3.1具体压缩配方、无关数据/实现与AppB指数界证明未读、不采用。只处理模型工程搜索中的验证/共享机制，不把任务领域扩成AI for Science。新增命题是并非分解独立子任务也能共享可累积中间进展，但只有已验证状态可转移且保留多样续搜时，通信才有该选择价值；不是多Agent通信必胜。

§2：相同CLI agents/shared container与私有context/scratch；append-only numbered-slot广播与共享approaches/counterevidence/scores，atomic mkdir防slot碰撞、候选promotion时filelock/recheck。Measured improvement/replication等adoption与保持meaningful variation都是prompt instructions，不是harness自动语义gate；MNIST recheck与严格更好后promotion仍由agent实施，不能从filelock推验证正确性。hidden scorer与agent-accessible numerical/level feedback角色分开。

§3.4教学模型令X_ij为agent i从阶段j继续搜索时间，独立best=min_i sum_j X_ij，共享每阶段突破=sum_j min_i X_ij；后一不大于前一只在continuation难度仅依赖stage、无成本可转移、transfer后fresh independent searches条件下成立，不是实测开放Agent定律。iid exponential/指数完成概率分离与g有效独立组均为pedagogical assumptions，论文也明确非指数期望时间加速；本轮不采用AppB界。通信导致herding、错误进展或有干扰的共享state就破坏该理想比较。Terminal89全任务、four solo/two team trials：pass@1 52.53、pass@2 62.36、team@2 60.67；未完成赋0，max是整benchmark trial/batch最大，非逐task挑不同team。Official verifier在执行后，largest-eigenval只核eigenvector/不核dominant、mailman public只subscription而漏official另外要求；中间局部check不能证明整体正确。team共享一终态，pass@2保两独立终态并oracle selection，不能唯一归因结果差于feedback或herding；作者明确descriptive small-trial/no precise gap/causal estimate。

§3.1 ARC25 public games Sonnet4.6，64solo/20team trial每game、k3/5独立peragent native actionbudget；solve全部关卡、furthest、RHAE不同目标，best@k有限pool无放回估计。Main team约2倍output tokens但最终accuracy匹配独立更多tokens只是该budget/任务曲线；低≤400K/agent反而独立先领先coordination tax。只SB26/LP85两favorable games做matched-total-action控制，action budget不计reasoning/read-only tools，不当总compute或全25game因果控制；team小budget.2×each匹配solo1×又输。18game furthest有改善、7game反退，许多仍全失败，不外推通用能力或SLO。

§3.2 polyomino固定score70hiddencases，3h60solo/20team3，72h12solo/仅two team4/model，图是trialpool最高轨迹非mean/CI/典型恢复概率；长期72h最高又低于3h另设置，不能说horizon收益单调。§3.3 MNIST96h/gzip9 code+weights/99.4accuracy门后1957 vs3160bytes局部结果，早期100Ktokens coordinator tax；此处不采用compression recipe。A.1资源明确：ARC solo/team均4CPU8GiB，packing均2CPU6GiB、不随workers倍增；MNIST team4 CPU12/32GiB vssolo3/8，每worker3threads、共享A100，1000MiB/agent是自我遵守，400MiB allocator不是GPU总显存硬cap；模型服务推理另账。Terminal per-task resource配置共享不乘workers、runtime timeout与verifier separate/no uniform horizon。各protocol并非同一种全资源匹配，team superiority不按peragentcap冒充总端到端预算公平；共享锁、verification、推理、容器CPU/memory与最终oracle选择分别记账。

actual `AGENT-MULTI-AGENT` Ch82:58–98已有coordination tax/task-topology与budget/headroom，105–114列decomposable任务条件，130–142分live redirect与跨run晋升，312–324有shared state owner/commit而非共享传闻。尚未明确**同一不可独立分解的搜索任务，可以按已验证可转移的连续改进共享checkpoint；终态可评估不等中途可识别真实进展，best@k和team的一终态/多候选资源条件不同**。拟窄I在coordination-tax总结“关系属于Direct Evolution”之后/“Agent数量应由边际信息价值”之前≤2段，故5分深入仅受影响机制与反证；不采用指数定律、prompt-certified验证或全实验recipe。仍待非作者必要源→actual/literal裁决、无锁未写。literal：

> 任务不能拆成互不依赖的子任务，也不意味着多个探索者只能独立跑到终点。若中间改进能由可访问的verifier辨认、状态可转移且接收者仍保留不同搜索方向，可以让不同agent在连续阶段提供突破，再从共同的已核checkpoint继续；这不同于事后从k条完整轨迹选最好一条。把“每个agent完成各阶段后取最小总时长”换成“各阶段分别取最早突破再相加”，只在阶段难度、无损转移和独立续搜假设下才有比较意义，不构成语言Agent的普遍加速定律。

> 终态有grader不保证中途反馈忠实：局部测试可能确认一个要求，却漏掉整个任务的其他约束；共享一份终态还会失去独立候选的oracle选择机会。受限通信研究里team优于单次，却未超过Terminal-Bench独立best@2，不能仅凭少量trial唯一归因feedback或herding。重复验证、共享artifact锁、模型tokens和容器资源都有成本，prompt要求复核不等harness强制gate；必须保留完整任务验收及资源分账。进展不可辨认、转移改变任务状态或共享使搜索同质化时，独立best-of-k、顺序单agent和显式人工/确定性检查仍是合理分支。

## 2026-10-01 08:41 C/D与追加实际写后闭合

root非作者C三source→actual/literal及实际新两段/邻接写后PASS：SharedFault21155 Ch25:68/70、Compositional22055 Ch25:165/167、ZYT21712 Ch23:695/697；原16489 semantic-body-binding紧邻旧module、22055独立SF在其后/Goal前合理，不需移动。随后D四/RBS/CoVer/TTC七必要源→actual/literal通过并独立实际写后PASS：AutoView21940 Ch77:344/346、MACE21533 Ch77:273/275、Proxifield20889 Ch82:230/232、TTC21032 Ch82:97/99、VisualGeo21363 Ch72:212/214、RBS20971 Ch14:284/286、CoVer21208 Ch33:485/487。所有精确锁释放，旧机制/fallback保留；低重叠非正交、配对非单unit因果、receiver预算例外、保护残余、衰减半径非界、列去重非独立/严格低方差、prompt非harness与共享资源/Terminal反侧都已在actual正文。

正式58=37深入/20标准/1中心D，35实际I/20窄E/2Only/1D；D不计Evidence通过，138 provisional尚未日级冻结。尚可执行80身份保存在唯一作者停点，不增加发现入口、不重读本段已完成附件。作者本轮V3与限定diffcheckPASS只机械接口，来源/准入终态和全日非作者Gate仍普通未完。

## 2026-10-01 理论有限组：21126 / 21001 / 21422 / 21656

仅复用本日已具名、已校准的准入与官方Mon21 New归属，不增加发现。作者必要证据与fresh actual对照完成后，root已独立必要source→actual/literal通过并授权四窄锁；四项实际各两段写入后，root进一步亲读新段及邻接、写后PASS并释放锁：21126 Ch49:458/460、21001 Ch5:131/133、21422 Ch5:143/145、21656 Ch25:858/860。四项为实际窄I，正式终处置由58增至62；此处下文拟插点/literal保留为支持采用的证据，不再表示未写。原5分标准项因实际长期差额深入仅受影响命题，不改准入评分、不遍历全附件。最低范围与未读范围如下。

### 21126 Layerwise Decoupling — 归一化不等于迭代轨迹等价

[Layerwise Decoupling for Stable Structured Sparsification of Fully Connected Layers exact-v1](https://arxiv.org/html/2609.21126v1)，`2+1+2=5`。实际读§2–4（Theorems1–3/Cor4及所附证明、Algorithms1/3）、§5.3完整对照、§5.5 OPT必要评价、§6限制与§9配置；§3截断的degree-dependent normalization句已定点补齐。§5.2全部恢复实验、PINN及App7–8未读、不采用。正齐次激活的function-preserving gauge允许inner增大/outer变小而改变单边惩罚，归一化augmented inner row再罚outer column阻此自由度。p=1全局最优等价的joint项是特定φ((a²+b²)/2)，**不是实验incoming-row Group Lasso同目标**；p≠1须变换φ。层内定理rest-frozen/full-loss，不给整个深网全局最优或有限迭代保证。

实际Alg3每block只归一一次，与Alg1每步project的约束不同；penalty70%/其后局部及最后全网无正则FT，drop后不revive。30paired synthetic seed的尺度对照将归一化与layerwise角色分开：once/noNorm/every-epoch及optimizer交换保各自scheduler/prox/grid，不能唯一归因decoupling；every-epoch失稳、noNorm某些质量较好均保留。OPT1.3B ReLU/固定checkpoint，128条512-token WikiText2训练calibration/20%validation，30ranking+40reconstructionepochs，每batchprox，五replicates不是五独立模型训练；matched steps不是matched step cost。accuracy全24块依预算删、controllability六块独立strength sweep不同对象；joint oracle test-median envelope非可部署调参。80%预算SSS91.5ppl优于本法114.2，dense14.62；~32GPUh/replicate、未测wallclock收益、GELU/gated不满足该齐次理论。code仅可按请求提供、未核实现/复现。

actual `INFER-TENSORRT-LLM` Ch49:442–460已有局部敏感度/混合重构/Fisher/protected-set与物理artifact分账，未说明同函数neuron gauge改变单边结构惩罚、归一化选gauge及global-optimum equivalence≠finite trajectory。拟在13287两段末→“剪枝artifact还需把importance score与protected set”前两段，保原pattern/kernel旧线；不是整配方或runtime提速I。literal：

> 局部结构惩罚还要先决定参数尺度代表什么。对正齐次激活，放大一个神经元的输入行、相应缩小输出列，可以保持模型函数不变，却改变只罚输出列的代价；不能把更小的列范数直接解释为更不重要。一个受限分支先把输入行连同bias归一，再对输出列施加组惩罚，以消除这项尺度自由度，并在相邻两层、其余网络冻结的子问题中筛选神经元。其全局最优与特定joint惩罚的等价，只说明目标的最优函数关系，不等于两种有限优化过程会走同一轨迹；实验中的incoming-row Group Lasso也不是该等价定理的同目标对照。

> 实践中只在每块开始归一一次、再进行梯度与proximal更新，和每步重新投影的约束算法不同；受限对照中频繁归一反而失稳，删除后的恢复还依赖额外fine-tuning。归一规则、惩罚窗口、物理删行列与恢复预算因此都属于剪枝artifact的身份，参数/FLOPs减少仍不证明kernel或请求提速。现有ReLU/OPT1.3B证据在激进预算也有质量反退，不能搬到不满足正齐次性的GELU或gated FFN；条件或质量门未通过时，保守剪枝、独立目标对照和稠密权重仍应保留。

### 21001 MCR² Limits — 同支持域near-optimal不等exact-optimal

[On the Limits of Maximal Coding Rate Reduction for Out-of-Distribution Generalisation exact-v1](https://arxiv.org/html/2609.21001v1)，`3+1+2=6`设计反证深入。实际读§2–5、AppB.4完整Proposition B.1/proof与AppE配置；不采用无关完整推导/代码。balanced binary、unitnorm R²、C=Y与S=Y xor Bernoulliδ模型，sharp coding optimum Jstar明确；environmental encoder gap Γa(δ)=½log(1+a²δ(1−δ)/(1+a))，fixed source-optimal head riskδ。正噪声完整支持时environmental **仅任意近最优**，反转后风险1−δ；exact global optimum+unrestricted source-optimal classifier反而所有该族target risk0（B.1），不可将摘要“同最优”泛化。noiseless exact optimum失败需support变化。same support不控制shift大小，反例density ratio随δ→0无界。

共享coding operator inner最优可exact成立，outer仍near-optimal；反转coding objective和marginal representation相同，但label assignment变化，target coding diagnostic用target labels不是无标签部署sensor。Waterbirds是随机ResNet18/128维/seed42、50epochs/constant effective LR（scheduler未step）+frozen logistic probe，2897不均衡两组combined accuracy46.84非全test、不均权平均；saliency只encoder gradients/两个例，非机制干预。精确run硬件/版本/log Not Disclosed，未复現，不以此证明梯度一定选失败encoder。追加class-conditional TV控制需要额外信息，与scalar coding相同不同。

actual `WORLDVIEW-REPRESENTATION` Ch5:92–137已有shift/shortcut与representation gap不代泛化，但没有coding geometry反转保持不变、near/exact/support三情形和shared inner optimum边界。拟在“训练图像中背景与标签高度相关…”之后/原21692 geometric-binding前≤2段；旧equivariance仍适用，不否定所有invariance。literal：

> 即使训练目标显式鼓励类间表示分离，也未必固定这些方向在部署环境中的标签意义。受限的coding-rate反例里，稳定特征与环境相关特征都能映射到两条正交方向；当环境相关性反转，编码目标和表示的边缘分布可以不变，固定source classifier却把原先常正确的对应关系读反。要求一个coding operator在多个训练环境都最优，也只约束几何变换的inner目标，不能单独保证encoder的预测关系稳定；目标几何、固定读出和跨环境质量仍需分别验收。

> 这条反证必须保留精度与支持边界：在正噪声、完整source支持的有限模型中，失败encoder只是任意接近全局最优，精确最优配合不受限的source-optimal classifier反而可保持零目标误差；精确最优也全错的例子改变了支持域。同支持域还允许罕见输入变成主流，不能冒充小shift保证。构造证明的是coding近最优不足，不证明真实优化器一定选该解；额外class-conditional稳定假设、语义保持干预或跨环境验证都有成本，未验证时仍回退切片、反事实和真实OOD行为测试。

### 21422 Brownian Heads — 固定表示的诊断不能抵消选择成本

[Brownian Heads for Deep ReLU Representations: Activation Mass and the Cost of Same-Sample Selection exact-v1](https://arxiv.org/html/2609.21422v1)，`2+1+2=5`，因actual缺口拟仅受影响深入。实际读§2–5、AppA.3固定定理与A.5/A.6 threshold-chaos/union上界证明。Brownian Kq=(||u||q+||v||q−||u−v||q)/2，head RKHS norm≤B、fixed realized pair(S,z) conditional empirical RC的sharp范围B√(M/2n)至B√(M/n)；M只trace、offdiagonal决定精确值。sample-selected z的该conditional identity仍真，但population conditioning会漏选择event。union须保representation supremum，threshold traces/range envelope控制其quadratic process；family在aux signs之前固定，**不是训练看aux signs**。q1非负final ReLU、q2双signed projected traces、finite common m/finiteness/measurability条件保留；sample-dependent random class仍须另行population论证。

同mass所有n/2-subset候选的fixed RC随n衰减，union可常数；上下界matching只worst empirical capacity非minimax excess-risk/同时所有architecture。§4 exact constructions deterministic非independent experiments，adapter固定n500三datasets×five paired seeds largestfamily union/fixed1.40/min1.338为受控selection支持而非n-rate实验；frozen ResNet transfer不测end-to-end选择项、不证明普遍head优越。没有移植成现代LM泛化界，未核完整AppC/D/实现、未复現。

actual `WORLDVIEW-REPRESENTATION` Ch5:129–137几何诊断≠泛化、145–151压缩/heldout只一般分账，未承载same observed sample选representation时conditional fixed-head bound漏union selection成本。拟在“因此，模型学到了正确特征…”之后/“记忆与泛化”标题前≤2段，与MCR窄seam不重叠。literal：

> 表示诊断还要区分“固定一种表示后训练读出”与“用同一批样本选择表示再训练读出”。对一种受限Brownian kernel head，固定表示的activation mass给出经验复杂度的尺度；即使表示从该样本学来，这个条件化的经验恒等式仍成立。问题出在把它直接升级为整个选择过程的泛化界：候选表示的supremum必须保留，候选threshold traces可以增加选择自由度。一个等mass有限构造中，每个固定候选的复杂度随样本数下降，整族复杂度却不下降；因此压低同一mass不等于消除了选择成本。

> 这条边界属于Brownian terminal geometry及披露的ReLU、head norm和trace-envelope条件，不是任意Transformer的风险公式；最坏经验容量也不是minimax预测误差。若表示与head使用同一数据选型，必须记录候选族与选型数据，另做selection-aware分析或独立held-out验证；选择成本的测量与额外数据有代价。受限实验只展示固定mass下的union gap，冻结特征上的小幅head收益不能代替端到端学习证明；约束未核时保留普通训练、数据切分和任务验收，不把一个低复杂度诊断自动当成泛化证书。

### 21656 Beyond Gaussian Worlds — geometry与positive-pair谱共同限定恢复

[Beyond Gaussian Worlds: Latent Geometry Matters for JEPAs exact-v1](https://arxiv.org/pdf/2609.21656v1)，`2+1+2=5`。HTML官方404，官方PDF1,215,918bytes/25pages已恢复；web截图入口失败后本地Poppler仅render必要printedpp6–7并视觉核Def4.1/Thm4.3–4.4公式，未以失败关闭。实际读§3–7、AppE.2 forward proof必要段；不声称全附录/代码已核。observations g须a.s.injective且measurable inverse；stationary intrinsic Langevin pair、connected properly embedded manifold、smooth positive centered-isotropic p、self-adjoint discrete spectrum。Def4.1 density restriction/embedding Laplacian/complete first nonconstant coordinate eigenspace三条件，exact h#p=p+alignment optimum→orthogonal Q preserving M；仅exact匹配下近optimal excess/谱间隔控制L²恢复，不是finite MMD实训定理。球面较Gaussian更紧只fixed linear-mode correlation、优势随dimension趋大消退，非uniform sphere总更好。

§6 oracle latent-probe validation选α（seed0）、另seed1–3 test，matched/mismatched targets ambient dimension不同；finite penalty approximation及mismatched stress不直接验证population theorem。§6.1/Table1环面10runs中5successful才报.996，另5为.597±.187；§7又称2/3，口径不一致，**不采用成功比例结论**。high-dimension又更换SIGReg/product-MMD，Matérn控制只原文说明、未读全A.2，故不以headline数字支撑唯一geometry因果。code仅upon-acceptance承诺、未核实现/复現。窄采用理论geometry分工，不采完整empirical配方或部署保证。

actual `MULTIMODAL-WORLD-MODELS` Ch25:854–856拥有现2605.26379 Euclidean additive-noise/Gaussian可识别边界，但“非Gaussian…会造成错误同一化”不能被读成非Gaussian必不可识别；当前实际缺intrinsic pair+target geometry相容的非Euclidean替代分支。拟在26379一段/marker之后→Counterfactual Identification标题前≤2段，不删原Euclidean条件。literal：

> 上述Gaussian条件属于Euclidean潜变量与相应正样本动力学，不应升级为所有表示几何的唯一恢复路线。若潜在方向或周期状态生活在嵌入流形上，正样本也须沿其内禀动力学生成；在论文规定的平稳与谱条件下，还须观测可逆、精确target分布匹配、潜分布符合该流形上的Gaussian-potential限制、嵌入Laplacian相容且ambient坐标构成完整最慢非恒定谱空间，alignment最优还可恢复该状态，只剩保持该流形的正交变换歧义。球面均匀分布提供一种满足条件的非Euclidean分支；选Gaussian或球面target因此是在选几何先验，不是无条件防collapse开关。

> 近最优恢复还依赖linear与nonlinear谱模式的间隔，并继续要求精确分布保持，不能直接把有限batch、有限权重的MMD训练当成定理前提已满足。几何匹配的实验也有局部优化失败，oracle潜变量probe选超参数不等部署拥有真值；更复杂的target regularizer增加成本，未知或不可逆观测、错误pair动力学及非平稳环境仍需保留原observation、非线性belief与实际任务验证。Euclidean Gaussian路线在原约束下仍合理，新分支只放宽几何选择，不证明表示就是完整可控制的world state。

## 2026-10-01 下一有限组：20842 / 20980 / 20974

只处理此前具名准入，不新增发现。理论四实际写后已root独立PASS，正式62（41深入/20标准/1D；39I/20E/2Only/1D），余76普通。以下三项作者必要证据/actual对照已完成，待非作者采用核；两拟I未获锁、未写、不增加62。

### 20842 COAL-SQL — coverage与当前失败分权，窄E拟案

[COAL-SQL: Coverage-Guided Augmentation and Failure-Driven Learning for Text-to-SQL Post-Training exact-v1](https://arxiv.org/html/2609.20842v1)，`2+1+2=5`标准。实际读§3、§4.1/4.2完整核心（初次截断的selection/construction与§4.2.3 retrieval/rerank已定点补齐）、§5.1/5.3/5.5/5.6；未读全部§5.2/5.4、附录/实现，不采用其全榜收益。SQL skeleton保留操作/嵌套而mask schema/literal，从seed之外固定pool按embedding distance提出结构覆盖，再在训练DB instantiate，parse/exec非空/skeleton/LLM语义gate分权。1−cos不保证metric triangle inequality，未采用一般K-center最优性；稀疏孤立过滤会漏rare结构。在线八rollout的SolveNone由格式×执行全无成功定义，不等所有组无reward差异：format本身仍可区分。

step侧累积失败buffer达64时每GRPO step至多消费一次SFT，teacher可读gold SQL、terminal execution只验答案非trace忠实。epoch侧按唯一task key集合聚合gold-skeleton相邻练习，跨失败共享1024全局quota而非每失败quota，error-aware cap与普通retrieval fallback并存；静态覆盖、当前step监督补丁、下一epoch分布提案有不同人口/身份。6500初始pool与6144 unique练习不等总token/teacher预算；8H20/320 GRPOsteps/Qwen2.5Coder7B与Llama3.1 8B、Qwen3.6-35BA3B合成/teacher/judge共享误差。full64.9 BIRD DEV对RLonly63.2、step63.8、随机augment64.4、随机epoch64.3是单协议分项；Spider noepoch85.4反而高于full85.3，没CI/独立训练seed。教师每acceptedexample7.67calls、36.8k input/4.1k output，23.47h训练；<.02%仅CPU retrieval非全teacher/SFT成本。15.1%与.86 SolveNone初始口径不合并。semantic84.7%及200条质量评分实际LLMjudge非人工验证；lexical contamination check非语义无污染证明。

fresh actual `TRAIN-DATA` Ch27:572–599已具体分source/feature/executable coverage→current-policy failure→独立verifier及feedback bias，611–628结构桶/代表选择与rare-tail风险，987–1007 current-policy selector/nonoracle proxy；`TRAIN-GRPO` Ch33:434–436已具体全错→教师SFT/mixed→相对强化/全对跳过与teacher/covariance成本。拟**窄E**仅采用“结构多样性不等当前可学习难度、failure selector不是真值、全错监督注入与相对强化分流”三现有命题，非整个coverage/step/epoch配方已有。buffer64/全球quota/具体双时钟调度与局部SQL结果只报告；它们尚未形成超出这三条的独立成立条件，故不为组合recipe制造diff。若非作者判双时间尺度存在实际长期缺口，应定点重开该命题，不关候选、不缩未读池。

### 20980 ForeTac-VLA — 真实未来训练条件与线上预测条件交接

[ForeTac-VLA: A Forecasting-Based Tactile-Vision-Language-Action Model for Contact-Rich Robotic Manipulation exact-v1](https://arxiv.org/html/2609.20980v1)，`2+1+2=5`，actual长期差额拟仅受影响深入。实际读III–V完整核心架构/forecast/training/setup/TablesI–II/robustness/failure/limits，不读实现附件。当前两指7×4 taxel、过去10step绝对值及相对首帧变化，tactile/VL双向crossattention；预测5/10/15/20未来步的触觉变化，加回当前实测形成future tokens，**这些预测tokens实际进入action prefix**，非只aux loss。前75%训练让action读GT future tactile，末25%改为自身forecast，没有独立课程消融或通用exposure-bias保证。60Hz、UR7e/2F85/TSF85与两D455，280demo、60ksteps，单96GB RTX PRO6000 Blackwell；precision/端到端latency/forecastloss详细权重未披露。

每模型4task×20trials=80，full95% vs single-cross/forecast81.25及无forecast80%，但无forecast时bidirectional实现退化为single，**并非独立2×2 factorial**，不能把全joint增益唯一归forecast/课程。normalized taxel跨horizon/sensor MAE6.48e−3不证明接触状态/安全；暗光80%和clutter81.25%相较95%仍退，单传感器/embodiment与固定offset、无CI/多训练seed，误抓/滑落/器件损坏反侧保留。

actual `MULTIMODAL-EMBODIED-VLA` Ch26:249–283已有future-to-action可见性、provisional prediction/current controller权威和FutureKV freshness，285–300明确aux-only/MT未来stream不该自动进入action与privileged future训练。尚缺**确实线上消费future tactile的分支中，GT→forecast输入分布交接须单独验收**。拟在现Future-KV边界末（“显式video…纯direct VLA…仍合理”）之后/Training-only Foresight标题前两段，与旧未来信息分账自然衔接。literal：

> 未来监督还有一条实际进入动作条件的触觉分支，不能与训练后删除的辅助decoder混称。当前触觉读数与历史变化可以先预测短期触觉增量，再加回当前实测、作为action head的额外prefix；这里预测值是拟议未来证据，不是传感器已确认的接触。若早期训练让动作读取真实未来触觉、后期才切换为自身forecast，就同时改变了条件输入的producer与误差分布，必须单独验收这项交接，而不能仅凭预测MAE或完整模型success声称动作已能承受线上预测误差。

> 这种路线增加触觉encoder、forecast计算与课程训练成本；无forecast时融合结构也可能退化，故有无模块的成功率不能自动拆成各模块的独立收益。受限实机结果仍有暗光、clutter和接触失败，平均normalized taxel误差也不是安全或deadline证书；课程比例没有独立消融。预测失准、传感器身份变化或延迟超界时，应重估future horizon、缩短chunk或回退经验证的当前触觉/direct policy，真实接触观测与low-level controller仍拥有执行权。

### 20974 Attention-Aware Routing — 冻结attention权重不代表routing无法影响注意力行为

[Attention-Aware Routing: Coupling Routing and Attention in MoEs exact-v1](https://arxiv.org/html/2609.20974v1)，`2+1+2=5`，actual长期差额拟仅受影响深入。实际读§3–8与Limitations主方法/训练/三模型/layerwindow消融/attention作用与部署限制，不读实现/所有附件。基础hidden-state router旁加入最近M attention weights的head均值；time窗口和DFT/log-magnitude视图分别aux linear，再由hidden+view sigmoid gates混合原logits。gate是learned weighting而非校准置信率；原Eq3/4分视图维度记法不完全一致，不宣称代码shape已核。router-only SFT训练原router/A/G，冻结所有attention/expert权重；OLMoE1Bactive/7Btotal、16layer/64expert/top8，Tulu3约220K/seq512/batch1024、五seed；Qwen3.6 math为三seed，不能都称五seed。layer9–15等只是模型局部配置。

OLMoE GSM51.99→55.36±.74，但各任务有反退；alllayer AAR-T MMLU−2.1pp均值，提前层加路由损检索、移深层恢复，不给“早层只检索/深层只推理”的普遍职责。window20–40局部最优，Table3 caption all-layer vsbody S9–15不统一，未采用一般window规律。修改layer l router可使下一层sink改变，但sink必要性/唯一reasoning机制未干预测试，wronganswer长度与sink相关不是因果；token/char尾长混口径不用SLO。显式materialize attention weights使active层无法直接用FlashAttention，未测端到端wallclock/SLO；作者所谓linear auxiliary overhead不当整attention线性成本保证。相同router-only SFT baseline有助控制训练路径，但extra aux参数/训练与本体架构不同仍不全matched budget。

fresh actual `MODEL-MOE` Ch21:42–61基础Wrh/Top-k，399–411分别负载与价值teacher、外部dense feature指导与budget/mismatch，413后global/localbalance分账；未说明**在线attention-history可另一路产生expert logits及冻结attention参数下仍经路由输出改变后层attention**，也未有其retrieval/FlashAttention tradeoff。拟在外部dense feature teacher两段末/Global Balance小标题前两段；不迁移teacher段、不写全架构recipe。literal：

> 路由信号也可以来自当前token刚形成的attention history，而不只来自hidden-state投影或外部teacher。一个受限分支把最近attention权重的时间窗口和频域视图变为辅助expert logits，以学习gate与原router logits混合；gate表示可训练权重，不是可靠性已经校准的概率。即使attention与expert参数被冻结，只更新router也会改变expert输出，进而改变后层hidden state与attention行为；“参数未更新”因此不等于“该计算路径的行为没有被干预”。

> 这条耦合既可能帮助局部推理，也可能损伤检索：在受测模型中，全部层接入与仅深层接入出现不同任务取舍，不能把layer depth当成普遍功能分界，attention sink与收益相关也未证明其必要因果作用。额外视图、gate和权重materialization增加成本，所测实现的active层不能直接沿用FlashAttention；较短错误回答不证明端到端SLO改善。任务回归、窗口失配或内核成本超界时，应保留原hidden-state router、减少接入层位，并以matched任务切片与实际执行开销决定是否启用。

## 2026-10-01 后续有限组：20831 / 20942 / 20892

承接此前具名准入，不增来源。三项作者必要证据与fresh owner对照完成，仍待独立采用核；不计正式62，不获锁不写。

### 20831 Recursive Language Models — 可表达正确规则不保证选择它

[Recursive Language Models Generalize Out of Domain exact-v1](https://arxiv.org/pdf/2609.20831v1)，`2+1+2=5`，长期差额拟受影响深入。HTML404后官方PDF34pages成功恢复，local /private/tmp/sep21-rlm.eyCnpm/20831v1.pdf。实际读§2–7主理论/实验、Theorem8完整主文proof、G.2–G.5必要配置/shortcut反侧；未读完整D/E证明或代码、不声称simulation实现已核。same recursive executions/nexttokenlabels，只改flat/fulltrace vs activeframe观测。Π幂等且target=g∘Π；local-rule consistency→只在已有visiblecontext的equivalent set保证，不涵盖真正新子问题。MDL选最短consistent rule，CoT模拟constant depth/param overhead限定causal hardattention/product-gated FFN与legal递归prefix、编码语言有限精度/可数模型；IID同distribution realizable界只constantfactor，不证明现实梯度优化必选MDL。

Theorem8 strict code-length shortcut gap比最短localrule小→必须不Π-invariant，proof以fhat∘Π可行反证；strictgap只是充分非必要（ties/其他consistent choice亦会失效）。不是只因为递归名字、token更短或“看少总更好”。共享6layer/6head/d384/GELU，但RM2K≈10.65M与CoT4Kpositiontable slightly moreparams、oneexpression变多个RMrows，不能称allcompute/tokenmatched；IID RMbatch64/CoT32、timeout/bestval、smallsizes3seeds/larges1seed，length/depth先各达到ID99%而非相同steps。fixedseed42池500K/Table1各3100eval，sixplantedshortcut各300ID/300OOD，不通用自然LM。far length>5L RM76.4仍降；仅framewidth≤115subset85.0不能替全量。G.5明确剔除两反例：rootframe欠定时RM亦失败；rootpayload能invertiblyrecoverhidden shortcut时RM也能学shortcut。isolated view必须仍足够定义真实目标且切断shortcut泄漏，无完整硬件/precision/wallclock披露，不外推安全/长上下文SLO。

fresh `WORLDVIEW-REPRESENTATION` Ch5:79–90已有neural executor组合/可表达≠可学长度、显式trace signpost与算法faithfulness，129之后一般shortcut和coding反证；缺**同trace改变可见frame即可限定hypothesis与等价context转移**的学习机制。拟旧25800长度学习两段/marker之后→“有限轨迹还要区分答案正确与遵循指定算法”前两段，不碰root刚通过的MCR/Brownian。literal：

> 可表达正确规则仍不足以保证训练会选择它，输入可见性本身也在限定学习问题。同一份递归执行轨迹可以让模型读完整trace，或每步只读当前子任务frame、返回时仅交回结果；若真实目标确实只由该frame决定，后一种观测约束就排除了对外部trace线索的依赖。受限MDL反例中，比正确局部规则更短的完整trace shortcut可以拟合训练，却在熟悉子任务换了外层context时答错；单纯扩大覆盖、保留可表达性，不会自动消除这种选择偏好。

> 该保证只覆盖训练已见的局部context所形成的等价集合，不覆盖全新子问题，更不等于现实optimizer执行MDL或递归普遍胜过CoT。若局部frame已丢掉定义答案的必要信息，隔离本身会失败；若parent payload仍能反解隐藏shortcut，分帧也未切断它。受测合成任务的多frame训练、position窗口和训练步数并非全compute匹配，长frame仍会退步；需要跨任务的信息时仍保留完整context，但应另测周边context干预、实际结果和必要信息边界，并计入stack/runtime与轨迹构造成本。

### 20942 Recursive AI Review — narrow E，评价分布漂移不等真质量

[When AI Reviews Train AI Reviewers: Scientific-Judgment Collapse and Mitigation exact-v1](https://arxiv.org/html/2609.20942v1)，`2+1+2=5`标准。实际读§2–3完整机制与结果，AppA/B/D/G过滤/embedding/生成/限制，不读所有C搜索或代码。M0=Llama3.1-8B-Instruct→2018–23 official reviews M1，各M2同M1初始化，2024每paper三reviews中0/1/2/3由M1生成，标签33/66是1/3、2/3。仅一个recursive step，sharedconfig不等保证过滤后各arm总acceptedtokens相等：AppA600chars/repeat/parse/yearform/strict<64K各同标准，但长度/acceptance可变。官方review不是纯human/truth，主controlled改变explicit M1 exposure不是allAIassistance。LoRA r64/α128/dropout.05、3epochs/BF16/FlashAttn2/64K、batch1+accum16，M1lr2e−5/M2lr2e−6；GPU硬件/总tokencompute/训练seeds未披露。heldout2000paper跨年均排training，三独立generation并非三独立training seeds。

四M2 rating mean非单调：0%5.30→33%5.85→100%5.70，故不是一般leniency shift；rating SD/entropy与samepaper semanticpair-distance/corpusspread各不同对象，samepaper .159→.142与centroidspread .609→.579为embedding proxy非真实论证质量。JinaV3 L2norm全37681reviews max5940未truncated；corpus先average后renormalize，不能合并rawreview距离。generation temp.6/top-p.95/max4096，malformed最多10retry、invalid score excluded，需保可评分人口偏置。

TrustReviewer用2018–25另single-stagecurated112743/1.9Btokens并paired lasttokenactivation steering，非上述recursive实验的单变量防治对照；5000calibration+100validation不eval，reference机构review不真值。lastlayer α.15提高rating至少匹配任一official的exact73.85→75.40，但MAD1.077→1.079略坏、samepaperdiversity略降，不叫全面修复；三generationSD不是training稳定性。先paper-derivedvalidreview/contentjudgment，只考察基础模型数据feedback/测量，不恢复AI for Science应用主线。

fresh `TRAIN-DATA` Ch27:334–355已具体corpus vsparameter recursion、samebase-reset与部署inheritance差别、supplier/mixture/humananchor分轴及direction/distance/perplexity/diversity/downstream共同测量、encoder依赖与真实继承回核；`PLATFORM-EVALUATION-SYSTEM` Ch66既有reference/judgeagreement≠quality命题。拟**窄E**只采用“recursive exposure的几何/多样性变化须与真实quality及参数继承分账”，此controlledone-step为受限验证，不称已有全部steering/过滤recipe或评价数字；literal无额外长期差额，不申请Books写锁。若independent认为官方AI污染角色已有章节不足只重开该具体命题。

### 20892 WM-VS — 下一状态相似与动作误差收缩不是同一训练目标

[WM-VS: Progress-Aligned World Models for Closed-Loop Visual Servoing exact-v1](https://arxiv.org/html/2609.20892v1)，`2+1+2=5`，actual长期差额拟受影响深入。实际读III–VI完整方法/全部必要评价及反侧。frozen DINOv2/Mask2Former targetassociation→causaltracking，32×32×33→256latent；离线mutualnearest/RANSAC current−goal二维位移/logscale/wrappedangle四signedcoordinates，trainingfixedσ归一，不将state只压成四维。Stage1 action-conditioned nextlatent加当前/预测next errorhead监督；Stage2冻结worldmodel，policy以BC锚日志行为、pred-next error对日志结果作local alignment，并在K3policy-imaginedrollout中对ρ.9收缩budget hinge。作者明确policyaction≠logaction，日志next-error**不是严格onpolicy outcome label**；rollout contraction只在learnedmodel内，不稳定性定理。

部署policy≈5Hz、插值commands≤30Hz，无在线rolloutoptimization；RGB-only固定E2H Gemini2+RealMan7axis，1000trajectory按700/150/150split、训练≤5000epochs/earlystop200，precision/hardware/总wallclock/多训练seed未披露。AprilTag不进入训练label/policy，但进入采集endpoint可见性screen、external evaluator与stop supervisor，不能叫endtoend无marker依赖。每方法30trial，ever达到relativeinitial cornererror10% 30/30，lastvalid达到25/30；后者stop由normalizedtagerror50updates不降/30frames失踪驱动，lastvalid不是全部末端物理状态。bestpose统计只converged；near-goalrebound只25retained条件人口。Future-error ablation只λf0保currenterror/allstage2/gain，retention83.33→26.67；BC-only删除三policyterms、all-error删除监督+policyservo+onlinegain，不把两bundle给各独立因果credit。BC-only nonincrease68.8%反高于full63.3%，strictdecrease却低，不以local sign“稳定”。五帧平滑30trajectory learnedvsAprilTag correlation只是外部图像误差对照；zero-shot两3Dobjects bestTCP45.66/31.88mm非finalretention，morematches≠rotationobservability充分，不能外推任意target或正式Lyapunov保证。

fresh `MULTIMODAL-WORLD-MODELS` Ch25:925–931用dynamicrelevance改善control-relevant observation supervision，1158–1162 modalityprediction≠controlsufficiency，269–287 imaginedrollout偏差/uncertainty；没有**给action-conditioned预测nextlatent再解码signed task-error并训练实际policy consequence**的受限替代目标。拟Ch25现distribution-regularizer段（“Queue越大…latent对planning/control sufficient”）之后/Imagined rollout标题前两段，保appearance、latentprediction和原rollout风险。literal：

> 对窄目标控制，预测下一状态还可以被要求保存动作后相对目标的误差方向，而不只复现一个相似latent。一条受限分支从可靠对应关系构造signed位移、尺度和转角坐标，让当前与预测next latent都能读出这些任务误差；再冻结world model，用示范动作约束policy，并让短期imagined policy rollout减少所预测的误差。表示仍可保留丰富观察与历史，任务坐标只是组织progress的接口，不是全部控制状态。

> 这里的收缩发生在learned model中，不是物理闭环稳定性证明；policy提出的动作不同于日志动作时，日志next-error只能在BC邻域内提供局部对齐，不能冒充其真实on-policy结果。受限实机结果也区分曾到达goal region与最后仍保持，额外error监督、rollout训练、特征对应及外部验收都有成本。目标对称或对应失准、模型误差累积、执行频率变化时，保留普通next-state/BC分支，缩短horizon并用真实反馈验收，而不是由低latent loss或预测收缩授予执行权。


## 2026-10-01 CaLR20981 central 争议定点包

[CaLR: Causal Latent Revision for Robust Diffusion Reasoning exact-v1 HTML](https://arxiv.org/html/2609.20981v1)与[同版本PDF](https://arxiv.org/pdf/2609.20981v1)，此前`2+1+2=5`准入保留；中心理论/机制冲突触发仅受影响深入。实际读§3–4完整主方法/理论/配置/评价/消融、AppC必要证明与PDF printedp4/p11；PDF12pages位于 /private/tmp/sep21-calr.WgquPY/20981v1.pdf，p4/p11本地render并视觉核Eq3/4/14/15，不是HTML转换猜测。AppB训练配置借PDFp11实际核，不遍历代码/无关附录。

原机制：teacher从reasoning chain抽primitive/依赖CTM三值L×L，inner以counterfactual target的task loss+L2求δ*，outerL1惩罚其noncausal投影，再以implicit differentiation/CG求参数梯度。可支持“teacher图为proposal、训练外层penalty”描述，但不支持其已认证causal truth、strict allow-only更新或恒定decoding/O(w)总内存保证。必要冲突如下：

1. §3.1称M=0 neutral保diffusionprior，§3.2 Eq4却以P(M)=I[M≠1]将M=0和−1同列受罚。soft finiteλ penalty仍不是hard mask；L×D latent perturbation与L×L topology如何投影未定义，不自行补广播/transport。
2. 同PDFp11 AppC LemmaC1 Eq14以δmasked=δ*⊙P(M)声称模拟causal multiplexer，紧接Eq15又说M(k,j)=1才active。按Eq4代入，允许边的P=0被抹掉，非允许边P=1反被保留；作为update mask与所称allow-only方向冲突，**不自行改为1−P**。Eq3将P用于违规惩罚本身可以合理，这不修复AppC更新证明。
3. §3.5把inner argmin/implicit parameter-Jacobian的线性系统与一次latent逻辑gate执行等同，未给solver iteration/condition-number/accuracy成本，O(1)decoding-round不等O(1)总计算。主ProofEq12–13直接设定正确gate输出/擦除，未从实际inner能量和softpenalty推出；L×L CTM与L×D latent仍实际保留，不能据“有效维度width”证明总storage O(w)。隐函数条件是unique localminimum/invertible Hessian，不是任意nonconvex目标都成立，更不认证teacher图。
4. §4数值/人口并不统一：Table1 GSM8K88.20，§4.2文字58.36，ablationα3为76.82；main默认GSMmax256，AppB却512（其他multiple-choice32）；主StageI teacher extraction，ablationP.I叫dynamic scheduler未给同一映射。w/oP.II Sudoku81.35反高于α4full78.64，不能称去causalalignment“全指标largest退步”。AppB single seed42/16A10040GB，LoRA128/自身lr2e−5、ARlr2e−4且Sudoku10vs8epochs，非全compute/训练matched；precision、CG实际容差/iteration预算、teacher身份/构图成本未披露。保原reported局部结果但不整合headline或合并为同协议。

作者central暂缓D已获sep22_resume_v3非作者独立PDFp3/4/11文字与实际p4/p11 PNG交叉确认，并root接受按该争议证据终态隔离；不是因访问失败或降分关闭。保留候选/局部bilevel alignment思路与实验，隔离strictcausal/convergence/optimal-memory核心保证，未实际Books采用、不称E或Evidence正面通过。重开仅需作者/official勘误给统一penalty-vs-update mask、CTM到latent明确映射、inner/solver及训练/部署target权限与比较协议；若只纠正理论却局部mechanism可独立支持，再定点source→actual差额，不扩大附件。sep22_resume_v3继续有限20995/21018/21022组；正式Report仍我写、未自签日Gate。

本轮六项最新终态覆盖前文“拟/未锁/未写”过程词：20842/20942必要source→fresh actual由root窄E PASS；20980 Ch26:285/287、20974 Ch21:413/415、20831 Ch5:86/88、20892 Ch25:271/273实际各两段、root亲读新段及邻接写后PASS，四锁释放。加CaLR central D，正式69（45深入/22标准/2D；43I/22E/2Only/2D），剩69普通；准入/来源终态及日级Gate未完成。未把单篇或marker检查升级日级通过。

## 2026-10-01 Voice-Light20995 / MAGIC21018 / Feedback21022 actual 闭合

三项 exact-v1 必要源→fresh actual owner由sep22_resume_v3独立亲读，root批准精确窄锁；作者真实各两段apply_patch，sep22随后亲读actual与邻接，纠正checkpoint/评价人口后最终写后PASS，root收到并释放三锁。非日级Gate；未读代码/未复现。

### [Voice-Light: A Full-Duplex Cascaded Voice Agent with Causal Turn-Taking and Speculative Generation](https://arxiv.org/html/2609.20995v1)

`2+2+2=6`，公开执行/消费commit差额深入。peer实际§3–11重点§7 privatecandidate/lexicalrevision/promotion、generation/sampleposition stale rejection、每80ms browser rendered-range ACK投影durablehistory、bridge先关闭TTS再awaittool，及§6/8/10反侧。浏览器rendered不等user理解/任务effect；duck/pause可逆不撤回已renderedprefix，未校准turn-taking head不能当成功概率。历史lockedV1 checkpoint step3500是11conv/1673候选/37HOLD，不是3500samples；不替代部署checkpoint step750 validation-only。V2未过gate/testsealed。36turn/3session/1operator热态serverPCM758ms非heard/populationSLO；9promoted/4nonpromoted难度混杂，不认846ms因果收益。
fresh Ch81 Continuous-time旧plan/pendingaction/watermark/interrupt只涵一般执行恢复，未承载client消费ACK/私有PCM晋升差额；actual `AGENT-WORKFLOW` [Ch81:874/876](../../../../books/part-07-agent/81-workflow.md) 两段接原Continuous-time末→Testing前，generation/cancel/rebase+renderedhistory、成本/边界与保守fallback已真实写。作者初稿曾把3500/750误作样本数，独立post发现后已硬纠正，实际终判PASS，不能把该旧错误当有效source结论。

### [MAGIC: Marginal-Guided Compression with Optimal Transport for Efficient Visual Document Retrieval](https://arxiv.org/html/2609.21018v1)

`2+1+2=5`，真实长期gap受影响深入。peer实际§3–5/Prop1、B2–4/B6、D1–2：未来MaxSim winner-demand组织source marginal，target-balanced soft entropicOT再Lloyd readout，保持在线fixedcompressedMaxSim。Prop1 unitvectors/‖q‖≤1/真实population w下只bound期望positive score decrease，**不bound绝对误差/虚增、ranking或recall**。离线1000querytokens可能仅几十queries，估计w不覆盖rare intents；softbalance不等finalhardcluster等大。B6same2kpages/ColQwen2.5、fp32d128decimalMB、oneH20batch1穷举、1000queries×5；per-page encoder/demand/OT/readout成本不等globaldictionary/端到端RAG/QPS，Table1 mildr.1 TabF/InfoQ反侧，r.01 Avg71.04 vsTable2 full70.71协议未统一不拼。
fresh Ch76:352–371原只有indexbudget/rebuild与hardMaxSim梯度，缺query-demand transport差额；actual `AGENT-RAG` [Ch76:369/371](../../../../books/part-07-agent/76-rag.md) 两段接indexbudget末→hardMaxSim前，sourceweighted/targetbalanced、population vs估计、rare/rebuild/transport成本与source/fullfallback已写，peer实际postPASS。keep-ratio含义改为“较宽保留向量预算仍有反退”，不混为低压缩率。

### [Catch Me If You Can: Real-Time Feedback Denoising for Responsive VLAs](https://arxiv.org/html/2609.21022v1)

`2+1+2=5`，真实handoff gap受影响深入。peer实际§3–5、A1–3必要训练/反侧/实机路径：冻结已收敛GR00T/VLM-DiT，慢planner finaldenoise前交nearfinalchunk、actionfeatures每chunkcache，每tick新hand-view为对应action做最后velocityupdate；非每tick全planner/非独立fastpolicy/非完成action后残差。chunk原本合理假设，静态Object仿真95.5vs97.5反侧、近接触不可恢复；真实50demos/20rollouts每任务。约2msfeedback≠physicalpath：camera62+IPC4/other总71.01ms，10Hzcontrol、slow每16chunk=.625Hz，无intrachunkreplan。Table2uniformarrival Tupdate+RΔt/2是分析非实测SLO；同GR00Tplanner双视角/fast只hand-view，FiS异horizon/LoRAfreeze非纯架构对照，GPU/precision未披露不补。
fresh Ch26:1051–1060 fastproprio/slowvision仅timestamp/commit，不含nearfinaldenoise交接；actual `MULTIMODAL-EMBODIED-VLA` [Ch26:1071/1073](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) 原Fast/slow两段+2607-26055后→知识树前两段已写，真实与仿真人口分开，保safetyguard/densereplan/缩chunk/stop为工程fallback而非paper保证，peer实际postPASS。

## 2026-10-01 当前四项必要 source→actual 小包（等待非作者采用，不计正式72）

root已转sep22有限独立核21039/21054/21081/21096；作者未获本组Books写锁。既有准入复用，不扩来源/附件。下面actual owner/literal只为有限采用判断，不自签独立PASS；无I配额。

### [21039 Stiefel-AdamW: Geometry-Aware AdamW for Linear Factorization Blocks](https://arxiv.org/html/2609.21039v1)

`2+1+2=5`，作者实际§3–6/Alg1/Th4.2/Prop4.3/T1–4拟采用机制及直接反侧。W=BA，一factor AAᵀ=I、另B自由；ambient coordinatewise Adam moment先adaptive再project tangent/retract。GL(r) fiber缩至compactO(r)，fixedW任意因子blowup被限制，不保证变化中W/任意lr轨迹稳定。**entrywiseAdam仍有正交基底依赖**，非gauge-invariant optimizer。Th4.2严格凸Euclideanextension/有界B与梯度、AMSGradmax、β1递减、alignment/noWD等条件不授真实AdamW LLM普遍收敛；本次不采用该保证，也不遍历全部证明附件。Alg1 gradient标注/transpose形状不清不认实现已核。GPT2E2E5epoch/b8/r4部baseline引用；ViTBaseCIFAR10r32/64/128五初始化50epoch/b64lr1e−3无scheduler；Mistral7B4bit/r16/bf16+fp32optimizer/b8部分borrowedbaseline，GLUE平均89.57但多singlemetric更低，无全面优势。GPT2pretrain正文7000 vsT3caption6000迭代冲突不采精确预算，13.8GB同peak不是吞吐优势；Qwen2Wiki103100M/b16×acc2/20k/fiveseeds局部。QRretraction有明显质量退步，projection/retraction有成本，precision/hardware已披露范围不能拼多个任务结论。
fresh `TRAIN-LORA` Ch30:165已有effective-rank与耦合optimizer取舍，563–575因子gauge/QR/SVD聚合但不解释**约束一个factor的行正交/尺度以收束fixed-W compactfiber与preconditioner旋转不变分权**。拟窄I在effective-rank段+12123SF后→targetmodules前两段：
> 同一低秩增量 BA 可以由 BR 与 R⁻¹A 表示；因此有效rank之外，optimizer还会面对不改变权重却把一个因子放大、另一个缩小的自由度。一个替代分支约束A的行正交，让B承载幅度：A的adaptive方向投影到切空间后retract，B仍用普通更新。这样把固定权重的非紧尺度自由度收束为紧的正交旋转，针对的是因子失衡而非删除低秩表达空间。
> 紧fiber不等整个训练轨迹稳定，也不让entrywiseAdam对剩余旋转不变；真实任务的weight变化、学习率、目标和retraction仍需验收。受限理论另要求凸性、有界量及特定moment规则，不能认证一般LoRA/AdamW收敛。约束更新支付projection/retraction，某些retraction及任务切片仍退步；原LoRA已稳定或几何预算不足时保留普通因子训练、受控缩放和实际质量回归，不从局部可用学习率推出全模型安全。

### [21054 Physically Based Rendering in the Latent Space](https://arxiv.org/html/2609.21054v1)

`2+1+2=5`，作者实际§4–6.7/7，拟latentphysicalcontrol差额深入受影响内容。**已知3Dgeometry/materialtypes/emitter/camera**，不是从单图恢复未知scene；SD3.5VAE16chan128²对应1024²，signedemit/BSDF+flatresponse+occlusion贡献，scene参数按encodedreference单view拟合再训练scene-specific residualrefiner（renderlatent+normal/depthbuffers→卷积residual），不跨scene通用。BSDF/sign实现由positive/negativecomponents解释，HTML称planned，当前官方abs已列GitHub链接，本轮未核代码。Eq6正文称只shaded，但V定义visible=1而公式乘V，精确occlusion gating方向未齐，不自行1−V；**不采用该精确式或物理能量保证**，保局部signed/features/residual设计。MC潜空间线性估计即便无偏，nonlinearrefiner/decoder最终有bias，非unbiasedRGB。五knownscenes/table1累加ablation，Cornell Obj flat.338→加occlusion.261是局部改善但不作独立因果，多个slice基本提升；单view附近更佳，Lampextremelight偏差，noise大refiner救不了。3000scene+3000refiner/RTX4090 Cornell5+5min非每query成本，precision/seed/CI未披露；Fig8仅Lamp frame30 move_camera equalMSE，latent终点42–84×快，decodedRGB却6–35×慢因decoder，不外推所有场景/端到端diffusion。SDSteapotdemo非完整3D生成产品。
fresh `MULTIMODAL-GENERATIVE-PARADIGMS` Ch24:47–55已有重构≠生成、819–825已有decoder总成本，但缺**物理模拟进入VAE latent必须改signed/边缘响应+residual而非继承RGBenergy解释**。拟窄I OutputDecoder标题前≤2段，若peer认为只是recipe且无差额可Only，不强I：
> latent可以不只由神经denoiser产生：已知几何、材质类型、光源和相机时，物理模拟也能提出待解码的特征。不过VAE通道包含有符号值、边缘强调和非辐射式遮挡响应，不能把RGB能量规则原样搬入。一个受限分支在同一scene中拟合有符号transport及额外响应，再由单view训练的residualrefiner修补latent与几何buffers对应的误差；几何/光照控制属于scene接口，最终颜色与细节仍由refiner/decoder决定，不是latent值获得物理真值。
> 该分工把模拟约束与codec残差分开，却要支付每scene校准、path sampling和refiner训练；未知scene重建及跨scene泛化未验证。线性latent估计无偏不保证非线性refine/decode后的RGB无偏，错误响应式也不能冒充物理保真。受限equal-error例在latent终点省时、解码RGB却因decoder更慢，因此必须先声明输出终点；细节混叠、极端光源或换codec失败时保留RGBpathtracing后encode、重新校准scene或原神经生成分支，不由局部render速度授予端到端优势。

### [21081 Loopjacking: Hijacking Human-in-the-Loop Approval](https://arxiv.org/html/2609.21081v1)

`2+2+2=6`，安全信号深入；作者实际§2–7全部必要机制/阳阴/控制/限制，不取全archive或部署复现。真实审批A→完整sinkB，完整display、materialmismatch、reachableactor、productownedconsumption、consequentialsink、无equivalentdirectauthority六必要条件，不把pendingmutable/A2A coordination本身叫漏洞。Agno七具名release阳性、2.5.5 directB可过故不合格，不补中间range或vendorfix；LangGraph12release只inmemory+customAuth允许非approver sharedpendingupdate，denyupdate安全，Postgreslicense未测。OpenClaw2026.2.23/24完整shellvector阳/修paired，laterMayadvisoryduplicate仅作者证据和解非formalvendor决定。OpenAIordinaryfunctionpercallSDK0.22.0/.22.2同IDrawinvocation变B被canonicalfingerprint拒，两组3/3非allSDK安全/stickyalwaysapprove或alltrustedfields可伪造。脚本审批先断言A、不测human理解/deception/prevalence；deterministicfixtures/syntheticcred/mockledger/oneoperator不是普遍发生率，safecontrol保A不只拒B。
拟**窄E** `PLATFORM-SECURITY` actualCh72:2775–2785 trusted反向渲染approvalview与effectreceipt、2253–2263 deliveryfence请求revision/actionscope+完整descriptor一次grant/fresh原子consume，具体承载“可信展示对象和effect-time授权绑定必须一致，grant不能靠resume/ID自动扩权”。product证据新增可修正使用者经验但无新长期制度，版本/range/六条件taxonomy仅报告，**不wholeLoopjackingE**；Ch84humanconsent只是交接不复制机制，不申请Books锁。

### [21096 Detecting Hallucination in LLMs: Tracing the Topological Signatures of Impaired Context Sharing](https://arxiv.org/html/2609.21096v1)

`2+1+2=5`标准，作者实际III–VI/TI–II必要方法/评价/反侧。attention图mutualoutgoingness两degree和10/50/90quantiles、jointentropy与可选selfattention建linearprobe，fullFRCpenalty与entropy仅uniformextrema反向关联**非逐实例等价或因果bottleneck**。四模型7/8/Phi4/32B、TruthfulQA817/NQ3610、temps.1/1、Eagerattention；GPT4judge+manual100promptagreement87–92%且严格任何minorunsupported算全responsehallucinated，subjectlabel非绝对truth。原baselineEigenScore改不做promptrewrite、temp.5采多response，不叫完全相同原baseline；方法需要attentionmaterialization/linearprobe训练，linearfeatures低复杂度不含全pipeline latency/hardware/precision成本。Phi/Qwen无general diffusepattern，Qwen3-32B TruthfulQA t1 ours73.53<lap75.17，Mistral多个slice<EigenScore；q90偶有反退、不claimallhead/family方向。知识缺口/benignattention sinks与病理contextsharing不可分，singleturnEnglishshortQA、不causalreasoning/longform/multiturn部署验证；未披露当前probe严格split/多trainingseed/校准需明确不能推部署risk证书。
拟**窄E** `PLATFORM-EVALUATION-SYSTEM` freshCh66:2098–2133 rawfeatures→可靠label/独立split/deploymentslicecalibration/概率与排序分权，1931–1947 graphagreement不truth及higherauthority外部verifier，具体承载“attention topology只是受模型/协议条件化的诊断feature而非factuality或原因”。新FRCfeature组合/量化效果仅报告，不称现有正文含全probe，也不把主体关联扩成causal解释；无新Books锁。

## 2026-10-01 下一四项 author necessary→actual 包（21137/21172/21181/21183，未获写锁）

已有题摘准入复用，仅读拟采纳机制、直接控制/关键反侧与fresh actual owner；不将四项自动I或全recipe进入书。不计正式74、无新发现，等待root有限采用。

### [21137 A Multi-Engine Dataflow for MoE Decoding on Scratchpad-Based Tensor Accelerators](https://arxiv.org/html/2609.21137v1)

`2+2+2=6`，实际长期executiongap深入必要。作者亲读§3–5.5/5.7与必要§5.6边界，Eq1–3/T2–6/PSUM反例，未code/Appendix全部。gate/up=shared codebook+expert-privateVQ J +sharedLR D/expertC；投影input到codebook与D只一次并在scratchpad存z/T，每expert按J gather+Creroute。sharedB/D先routing期间DMA、inputprojection同时privateJ/C DMA、tensorLR与GpSimd VQ并行，down原BF16只有其privateweights在gate/up期间DMA；不能任意down也共享input（p_e不同）。cross-expertgather batching与LR/VQ jointPSUM避免重复store，down stationary/accumulation位置offlinepermodelprofile。
实测AWS Trainium3 TP4/8physicalNeuronCore-v4 LNC2，SDK2.31/NKI.5，B1 autoregressivedecode五models，排compile/load；同prompt generate19/64/110tokens，two warmup+24runmedian slope hostTPOT，10kbootstrapCI（非全trainseed或trafficSLO）。原dense AWS NxDI只Qwen/Gemma production、其他三ported，KD originalBF16teacher frozen+top256renormalizedlogitsKL+CE，仅B/D/C训练J及otherweights冻结，10k256token初始化/训练与32×512WikiTextdisjoint，恢复PPL不等alltask无损；zero-shotQwen仍至3.2pp退步。NMSE低于LR-only但VQ-only4bits可更好，substitution/storage与latency需分别核。equalstorageGemma更少HBM3.9%却selection199%/TPOT变差；QwenVQonly4bits比denseBF16更慢，nativeMX4/8也因layout转换慢；downPSUM单step3.22×却wholeTPOT6.278→6.432退步。engineuniontime不能相加当criticalpath，sharedscratchpad/codebooks/KD和sync成本仍在；不开源位置不等复现。
fresh `INFER-TENSORRT-LLM` Ch49:890–892 productLUT+formatconsumer、894–896共享packedternary但无**共享格式DMA可routing前/期间、routing后shared input projection与private格式供给分拆/异engineoverlap/PSUM局部与全图争用**。拟窄I在LUT两段末→ternary分支前≤2段：
> MoE在同一token上给多个experts同一输入，还允许把格式的共享工作与路由后私有工作分开。一个scratchpad分支让gate/up由共享码本和低秩basis加expert-private索引/系数组成：先把input投影成码本读出表及低秩特征，再按路由取private部分。共享格式传输可与router并行，private加载可与共享投影并行，lookup与dense correction又可分配给不同engine；down输入已expert-specific，不能直接继承同样复用。
> 这不仅减少bytes，也重排哪些工作暴露在criticalpath，却支付scratchpad驻留、gather、格式校准/蒸馏和跨engine同步。相同bits下更细VQ可少搬bytes却增加selection而比BF16更慢；单步PSUM累加变快也可能占用共享bank、使整decode变慢。受限Trainium结果不证明GPU/任意batch同样成立，PPL恢复不等所有任务无损；profile/质量不通过时保留原dense或常规量化路径，分别验收格式、kernel与完整请求成本。

### [21172 TierKV: Long-Context On-Device LLMs via Predictive Multi-Tier KV Caching](https://arxiv.org/html/2609.21172v1)

`2+2+2=6`，实际aheadplan gap受影响深入。作者亲读§3–4/Alg1–2、§5.1–5.5/T4/6–12与§7，5.1–5.2初始truncate后已用官方精确节补齐；不全code/附录或新增设备论文。prefill已算hidden按logitentropyweight fingerprint、localhistorykNN输出length均值，预测totalL→sequence-position exactTier0/SVDTier1/fullrankflashTier2及offlineperlayerrank选择；“free predictor”只无额外backbone pass，不免hidden提取/entropy/history/search/calibration。twoA6000≤20min/model256B/layer校准，online<.1s/request仍有成本。fidelity用benchmark低维regression、Eq9balancedlatency/memoryline与feasiblepolygon相交候选不证明一般linear目标全域最优，Alg1可行性loop未显式Mbuf，不能授通用OOM/fidelity证书。保不准预估时excessfullrankTier2只无新增压缩，但旧Tier1失真与flash/H2D成本不消失；prefixreuse/hybrid仍future。
执行Keysblock SRAM重构/RoPE、V先latentweightedaccumulate末投影，exact/compressed共online归一；Alg2公式省略online-rescale细节，不认任何实现bitwise/fullKV等价。disk→RAM可与perlayerKreconstruct重叠，host→GPU1.66GB/s不隐藏，Kscorecritical vsVfinalprojection不同槽位，rank选择与overlapcost协同而非所有latency相加。OnePlus12 Snapdragon8Gen3/Adreno75012GB(~6.8GBappbudget)/FP16B1原checkpoint，不同frameworkkernel/auto-tune bundle不把prefill提升归只predictor。decode llama比平均.71×/全部多数更慢：Llama1B6→4.3，Smol4.6→1.9；Table8Qwen2.5MMLU/ARC/GSM−7/−6.6/−7pp，Llama1B GSM−5.3pp非无损。multi-turnfrozenwarmup五fact×3seed×3length45总体，75%rank matchesFP16局部91.1，50%rank73.3<91.1；不是futurequery普遍保全。Table6cap还受trainedlength/≥1toksec，不把容量增长当语义长context能力。600requests over3.3%/under5.9%仅localhistoryworkload，thermal/flash/uncertainty/tailSLO未证。
fresh `INFER-KV-CACHE` Ch45:706–726仅reactivehotset/coldtier recall/drift，623二维token/rank与layeredcompression仍无**decode前lengthproposal驱动exact/approximate/fullflash位置预算**。拟原recall风险末“只在其模型…taxonomy”后→多SSD段前≤2：
> 分层也可以在decode开始前规划，而不等hotset发生缺页。prefill已形成的hidden与本地历史可提出未来输出长度，再以设备预算和离线质量/成本profile共同选择exact位置、低秩resident区与full-rank flash区。预测只拥有容量proposal；runtime仍记录位置/格式、projectionrevision与transfer完成，压缩区按block重构key、在latent中累计value后统一归一，不能把三tier各自结果无条件相加。
> 长度估错时把超额位置放入full-rank coldtier，可避免为新增位置继续压缩，却不修复resident区失真或消除I/O。质量regression与平衡线候选也不是任意请求的最优/fidelity证书；hidden提取、history维护、校准、重构与flash/H2D成本必须计入。作者mobileB1中decode及部分质量仍退步，prefix复用尚未验证；短输出、history冷启动、精确引用或tail预算紧时保留静态FullKV/既有tier，硬预算由实际runtime验收而不是预测均误差背书。

### [21181 Implicit Rule Induction with Test-Time Task Embeddings in ARC-like Tasks](https://arxiv.org/html/2609.21181v1)

`2+1+2=5`，author实际§3–4.4/5与T1–2/Fig5必要规则与执行反侧；未遍历A–E可选例子。jointFullTTT embedding偏初始/与trainbasis漂移但solver能力仍高；先freezebackbone仅embeddingTTT，再freezeembedding训backbone，把任务定位与执行适配拆开。retrieval对train任务duplicate含memorization、多embedding可能同解/失败trainembedding非true；ConceptARC16meta概念不是完整rule，fivefold8train/2test每concept。LUCD15classes(4commutingatoms≤2组合)与Moves121bounded10×10位移、1train+10testtask/rule、10train/testpairs/task规则可独立probe：classification100%仍不是未知规则，MovesRMSETable1为2.12且sameTTTdynamicsprobe校准变.44，不能拼协议。
ARC1train400→publiceval400，OriginalFull pass1/2 48.8/53.8 vsEmbedFull49.5/55.2，noCI/multipletrainseeds/equalTTTsteps总compute/hardware/precision当前必要主文未披露不补；只embed13.0/17.2低而≤8multiembedsearch14.8/18.5加cost；ConceptARC按pair显著高于task严格3pair，不混。OOD最近距离不能可靠预测成功，manual80balancedconceptannotations只35/36.3%localagreement；Movesconvexhull interpolation不extrap、horizontal/vertical全atoms无composition训练仍不能compose，+3与+1embedding相加/迭代activation不能获+4——可解码几何不授新算子。因而采用分开规则定位/实际执行且冻结interface，非“学到了通用符号规则”。
fresh `WORLDVIEW-REPRESENTATION` Ch5:79已有frozenexecutor仅搜索programlatent与可表达/搜索/行为分账，40/194–214已有probe阶梯，但无**先在固定backbone校准任务latent再冻结它更新executor**的stagehandoff；若独立认为仅具体分账可E则明确该窄命题，不whole2stage覆盖。作者拟I接programlatent79后→lengthgenerality81前两段：
> 任务表示在测试时可被优化，不表示模型已经归纳并执行了新规则。若backbone与task embedding同时变化，embedding可能迁出训练坐标而backbone仍靠自身改动解题；一个可诊断的替代分支先固定backbone只适配embedding，让任务定位发生在共同接口，再冻结该embedding更新backbone。这样能分别检查表示中可读的规则与后续执行适配，代价是两阶段搜索和额外测试训练，不把近邻检索当唯一规则身份。
> 规则标签或可控generator允许分别测probe与最终任务；重复train任务的检索仍含记忆，概念标签也未必定义完整算法。受限网格实验中，漂亮的embedding几何可支持已训练范围插值，却不能自动叠加未学操作或外推新位移，逐pair成功也不保证整任务所有pairs通过。因而应保留冻结接口、严格任务结果和训练覆盖检查；预算或规则未知时沿用joint适配/直接执行验证，不由线性可读或二维图授予OOD泛化。

### [21183 I’ll Keep an Ear Out: Teaching AudioLLMs Proactive Audio Assistance](https://arxiv.org/html/2609.21183v1)

`2+1+2=5`，实际learnedeventgap受影响深入。作者实际§3–5/1table/streaming/I2ablation。Qwen2Audio7B+Whisperlargev3约8Btotal、16kHz128mels/pool40ms/token；不宣称allbackbone迁移已测。two specialinterrupt/silent，四supervision机会：I1无关→相关onset、I2整窗口相关但未通知（补错过onset）、S1无关、S2相关且history已有notice去重。reactiveclassifySFT→proactive balancedNI=NS（silent subsampling），LoRAr8α32/drop.1/AdamWlr5e−4 10epochs/b384seq2048/6H100fixedseed，5foldESC50 evaluation不等5trainseed。
ESC502000clean5sec50classes的99.6F1/100S2 vsnoISM10.1S2；Epic44kitchen zero-shotnohistory S2**未测**，P51.9/onset96.7/F167.5，但S1仅10.1、I2 41.2/class34.5vsaudioSOTA53.8，不采“结构domaininvariant/只数据错普遍framework已解决”。Streaming400×15s固定5–10srelevant、rolling5s/fullhistoryupdatedinterrupt、fadedconcat，平均onset3.5s非randomonset/rawrealwearable/heardSLO，不DHHuserstudy。I2增加约10pp仅ESC局部，未给baseline相同trainingbudget/CI/precision/physicalinputthroughput/部署费用，史中“已通知”仍需runtime真实投递/消费回执，modeltoken不等effect。
fresh `MULTIMODAL-REPRESENTATION` Ch23:736–739 compression+hiddenstate timingtrigger无I1miss→I2sustain/opportunity与S2historynotice distinction，326–344encoder/fusion/interruptauthority与runtimecommit保留。拟窄I long/shortmemorytrigger两段+25621end后→统一attention段前≤2：
> 主动响应不仅需要一个触发分数，还要让训练看见“为什么现在应该响或保持沉默”。面对同一watch-out意图，可区分无关转相关的onset、已经相关但尚未通知的持续窗口、完全无关，以及相关但通知已在history中四种机会。分别监督interrupt与silent，让错过onset后仍可补发，同时避免每个重叠窗口重报；这不是把声学分类准确率直接换算成通知能力。
> history中的已通知标记必须来自runtime真实交付状态，而非模型自称；表示与决策仍不拥有播放/取消commit权。事件样本构造、history更新和领域校准增加成本；cleanclip上的去重高分未证明噪声域同样成立，后者无关silence和持续召回仍低且未测history去重。固定onset拼接流的平均延迟不等实际device或用户效用保证；分布不匹配或重复/漏报超预算时保留外部eventrouter、显式确认及保守阈值，而不是让silent token替代交付验收。


## 2026-10-01 六处actual写后与窄E最新终判（正式80，普通58）

sep22_resume_v3已独立必要source→fresh actual核21039/21054/21081/21096：前两项窄I随后实际亲读Ch30:159–184（新169/171）、Ch24:807–839（新817/819）两段及两侧写后PASS，A可训练行正交与fixed-W/noninvariance边界、knownscene/signed residual/RGB反慢与Eq6隔离均真实保留；两锁释放。21081/21096仅具体采用命题窄E通过，不whole taxonomy/feature recipe。三处草稿/权限修正已实际同步：factor不是冻结、Cornell累加消融非独立因果、HTML planned vsabs GitHub未核代码，不新增artifact队列。

root独立必要source→actual/literal后实际亲读21137 Ch49:894/896、21172 Ch45:728/730、21181 Ch5:81/83、21183 Ch23:741/743及前后，四actual写后PASS，四锁释放。共享格式DMA/router并行不称input projections在routing前；PPL恢复非任务无损、tier fullrank overflow不修已压失真/平均prefill非decode、jointlatent/executor分阶段不授OOD、history通知是真runtime工程交接非paper自证送达均实际保留。exactlink/SF独立，旧正文不删，六文件scoped diffcheck PASS；这不是日Gate。

正式80=55深入完成/23标准完成/2中心争议；52实际I/24具体E/2Only/2D。138 provisional未最终冻结，普通58只既有具名准入，无新发现。peer下一4=21190/21216/21220/21227，root下一4=21242/21251/21264/21267，author下一4=21268/21284/21293/21340；各必要机制/直接反侧→实际差额，I无配额，其余普通续跑。

## 2026-10-01 author 下一四必要 source→actual（21268/21284/21293/21340，待独立采用）

仅既有具名准入，精确v1必要方法/直接关键反侧；主源均官方HTML实际取读，无新发现/无全附件。未获这四的Books锁、不计正式80；后续21190/21216/21220/21227的peer有效笔记另同步不重复。

### [21268 Edit-VAR: Taming Visual Autoregressive Model for Precise Video Editing](https://arxiv.org/html/2609.21268v1)

`2+1+2=5`，确认long-term离散控制差额拟深入。实际§3–5/T1–2及必要B实现、I效率、L失败（不全附录）：编码source多scale token、source prompt forcedecoding缓存其token概率/cross-attn；edit-pass不做连续inversion。Eq2 b=max(gamma−p_src(source),0)，以p_edit(source)+b对editargmax择token，source/edit概率同一token支持变化不是logit插值；gamma0不加bias仍可能argmax选source，gamma2才必保source。crossattention source-side anchor作为空间proxy，scale/token sigmoid让early保全而late foreground可改；Sstop25后不缓存source概率/attention、gamma0自由生成，以减少fine纹理绑定原motion。final两scale以前一scale residual范数插值选keep，36blocks固定同indices，被剪token绕QKV/attn/FFN但input仍进logitshead，保持lattice不保证信息。
InfinityStar8B、81frames480p/BF16/oneA800/Ubuntu22/Pytorch2.7.1/CUDA12.8/fixed seed41/all160案例（四type各40）、同SAM2 evalregion masks、15人50case盲评分；未多seed/CI/实时SLO。Table2无prune .979/.980对50% .972/.976 alignment反退、LPIPS .172→.176；matchedrandom50% .235说明selection相对，不无损。85→64s是有decouple的两pass1.33×，130→64合两改动2.04×，source编码/decoder完整成本未明确拆，不把two-phase当全部系统。结构大改/删除/布局/inpainting不适用，模糊prompt失败，backgroundmatch≠allconstraint。
fresh actual `MULTIMODAL-GENERATIVE-PARADIGMS` Ch24:1363–1371已probability nudging/mask/quantrepair，但没有support-drop条件token替换/late-source release。拟旧14591 marker后→固定长度Diffusion标题前≤2段：
> source-token约束可以保留未指定区域，却也会把原运动的细纹理带入新视频；并非约束越强就越忠实。离散coarse-to-fine分支直接编码source、缓存source条件下指定token的概率，在edit-pass比较同一token的支持变化，再与edit argmax竞争；attention与scale只调局部保留容忍度，不拥有区域真值。较早scale固定结构，较晚scale撤除source约束让细节重生，这不同于对全部logits做固定nudging或重新反演连续轨迹。
> 这要付source forward、概率/attention缓存和校准成本，也可能因错误anchor或释放过早损伤保留区域。前一scale residual可以提议最后高分辨率scale的计算mask，被剪token仍进入输出头而非变成已经验证的内容；同预算随机剪枝反侧支持局部选择，但更快配置仍有质量下降。固定backbone/seed/短片对照不认证任意编辑或完整请求SLO；大结构变化、mask失配或质量回归时，回原生成器、显式局部编辑/inpainting或更高保留预算，不由two-pass提速授背景无损。

### [21284 Authorization Revocation for Long-Running AI Agents: Root-Scoped Quiescence under Delegation and Asynchronous Execution](https://arxiv.org/html/2609.21284v1)

`3+3+2=8`保护深入，实际§3全部A1–A11、§4/5全部必要cut/support/channel/verdict、§6.1 reference、§7–8实证/边界、AppA.3 Theorem10/11完整proof，未代码/未真实provider。cut只是issuer原子停止新增/扩权，不是跨provider瞬时fence；已authorized carrier在sinkbarrier前（即使cut后）可accepted，须same-local-order typed pre-fence receipt和closed future-use/instance/lineage，settlement不新commit。support antichain{{A},{B}}允许独立B但实际selectedA必须exact-operation/envelope/current-witness atomicrebind，{{A,B}}不能删A当B独立；子孙不得按ancestry自动inherit。完整manifest是assurance前提，不可“checker通过→没有隐藏sink”；每个leaf同cut/epoch/profile/frozenprecutSEND frontier。SEND/terminalACK token projection精确multiset相等+acceptedcarrier covered，而不是不同typed records相等或总counter抵消；locallyQ不globalQ。已知open/postbarrier/完整scan证明无receipt为N；missing/stale/opaque/conflict为U；只有全覆盖/fences/localQ/channels才Q。Theorem10依A1–A9，不证明存在部署adapter；liveness另A10–11eventual evidence/fair finite drain，无界partition只保nonpositive。
§7/8作者provider-free durablefileledger真实childprocess+inert typed sink，17登记cases/44语义改后重hash mutations checker（未本轮执行），remote MCP/A2A/OAuth仅logical shape不vendorconformance；checker只能serializedevents，外部物理undo/goalcomplete/independent-rootstop不保证。几项results编号HTML异常不据此改证明，采用实际明确命题。
fresh `PLATFORM-SECURITY` Ch72:1406–1419已有EffectBound单Kafka路径/lease以及不能把cut当排空，但缺root共用carrier的alternative/conjunctive支持+跨leaf token闭合。拟EffectBound两段末→x402 binding start前两段：
> 多provider撤权不能把root ledger中的cut当作所有sink已停止。cut只冻结旧root的新增/扩权，每个sink还须在自己的commit顺序中安装barrier；传播期间已接收的旧请求须有精确pre-fence receipt并关闭未来派生，已承诺效果的结算不因撤权自动撤销。共享carrier的授权也不是root名称集合：独立备选支持可经当前witness原子重绑定保留同一operation/envelope，必须同时满足的支持则不能删除一项洗成独立权限。
> provider局部空闲还可能遗漏跨cut消息，因此声明须绑定完整manifest与同cut/epoch/profile，各leaf的SEND和terminalACK按唯一token投影精确配对，accepted接收者也需覆盖；总数相等不够。已知活路径是未静默，缺fence/不透明endpoint/冲突是无法判定，不能被timeout或agent自报转成完成。覆盖、认证、原子fence/rebind与durablemonotonicity都是前提，登记模拟sink不能认证真实adapter；该机制增加scan/ledger/receipt及等待成本，缺完整mediated边界时保留未完成、收窄scope或人工隔离，不宣称physicalundo或所有进程停止。

### [21293 GameASG-Bench: Benchmarking Autonomous Software Generation for Game Development](https://arxiv.org/html/2609.21293v1)

`2+1+2=5`标准完成拟窄E，实际§2–4/6/T1–9（不附件全trace）。predeclaredtarget/game-spec/tdd；agent实现reset/loadScenario/input/getSnapshot，但prepare必须legalreachable不能直接给待测outcome，接口绑定真实renderedstate。L1sourcepattern非gamebehavior、L1fail不skipL2；P0/P1 required，P2额外，P1 NOT_APPLICABLE当前runner未禁会缩分母，strictsuccess只是当前applicable合同非完全需求真值。47tasks32二维15三维/1221checks，manual独立reference47/47+positivecontrols；每task/config只一次cleanworkspace、Chromium1280×800、CC2.1.206/Codex.153.4 bundles非纯model对照。highestmeanL2 93.2≠strict26/47，计划47分母包含交付/评估失败；预算30/60/120 evaluated10/32/47，conditional70/40.6/38.3与planned14.9/27.7/38.3不混。efforthigh19 vsmax18一次run且max所有check更好，不能通用最佳effort因果；两harness都18但交集10，各8/21neither，不同coverage/resource。真实input＋preparedscenario会暴露分开selftests漏掉的combinedoperation，interface snapshot不是游戏真值自证。
拟`PLATFORM-EVALUATION-SYSTEM` 窄E只source declaration/check-mean/strict-contract三对象分账：actualCh66:50–74 runtime/contract/semantic/outcome交集、1660–1668CompoundArtifact predicates与verifier双侧/冻结合同非任何下游等价具体承载。game接口实现/scenechecks及完整recipe仅报告，版本/榜单/单run结果不改长期选择。不会称全GameASG机制已覆盖；若root发现combined-operation具体gap应明确限定重开，不按领域排除。

### [21340 Conformal Privacy Auditing: Calibrated Re-identification Attacks with Statistical Guarantees](https://arxiv.org/html/2609.21340v1)

`2+2+2=6`privacy约束深入：作者实际§3–5/Th5.2/Cor5.3完整assumptions与proofsketch、§6–7.1/Limitations。declared finitepool/attacker knowledge/querymode/samplingbudget/independentperexample randomness，APS cumulative score可pseudoposterior/empiricalfrequencies；splitquantile转set的marginal含truth coverage，不是每例posterior或实际识别概率。1/max(1,|C|)明言proxy非reID概率/DP；大集合不认证对未知攻击者安全、小集合也不等singlewinner概率1/|C|。openworld须conditionalinclusion下exchangeability，再总体≥(1−rho)(1−alpha)；topKmissing不是conformal failure，不能只报条件覆盖。changedrelease/attacker/prompt/model/websnapshot重校准，Threatconfig外不转移。
TAB1268 profiles K2/3 direct近singleton vsK1全pool，LLMclues K2 top1更低/.715却median20，非所有增强攻击更强；WikiBio1000/500 Llama减集合Qwen无明显，TextWash各类ncal=ntest100 matched；fiction K50 miss.16 cond1/uncond.84，K200 miss0cov.97。Drift TAB.965→.923/Blog.940→.835，不普遍固定nominal；APS并非唯一最好（rankmatchedmed179 vsAPS189）；n50/100/150cov.962/.957/.927，3split .951±.037不是确定riskcert。每例samplingm1→10与pool索引/calibration成本另计，主文未hw/precision/完整cost不补；membership只是future，不能说已验。
fresh`PLATFORM-SECURITY` Ch72:199–214只filter/anonymization attacker/utility scope，Ch66:600/623–625已有一般conformal/重复score但无**re-ID candidate miss与ambiguity proxy≠识别风险**的发布取舍。拟Ch72 learned-anonymization末→visualprivacy段前≤2：
> 删除PII或降低某次attack top1之后，仍要问给定外部知识能把身份缩到多小的候选集合。一个审计分支冻结candidatepool、attacker/querybudget与发布分布，用独立校准数据把其排序或samplefrequency转成包含真身份的ambiguity set；其coverage是声明人口上的边际统计性质，集合大小只是该攻击的残余候选数。1/集合大小不是重识别概率，更不是每篇文本的隐私保证，不能由大集合替发布者签发匿名化。
> 候选库漏真身份与set校准漏覆盖是两种故障，必须同时报pool miss、inclusion条件覆盖和总体覆盖；增加辅助知识、换prompt/model或rewrite后重校准。索引、反复采样、标注calibration和多威胁配置增加预算，局部有限pool不能覆盖未知攻击者。匹配预算下有的LLM线索只扩大噪声，drift还会破原coverage；证据不足时保留确定性遮蔽、缩发布范围/访问控制或不发布，不把经验ambiguity转换成DP或通用安全阈值。


## 2026-10-01 正式96有限同步

正式96=70深入/24标准/2中心争议；67实际I/25具体E/2Only/2D。此处仅追加16个已通过本轮独立必要源→fresh owner与15实际写后的单篇结果；其余42普通保持未完，不继承宽目录/旧Complete。精确v1与Mon21归属沿本日官方身份有效证据，各采用命题/未决边界未变；没有全附件/代码运行或跨日扫描。

### [21190 SWE-Proof: Can Language Models Resolve Real-World Issues with Machine-Checked Proofs?](https://arxiv.org/html/2609.21190v1)

2 + 1 + 2 = 5，实际长期差额深入，逐函数proof与整个issue行为覆盖/axiom/patch correspondence三外部接缝分权。必要 primary：§2–5/T1–3、E.3–E.4、F.4/H.3；sep22_resume_v3本轮独立实际源核，不是仅题摘或作者self-pass。known-correct patch仅离线构造特权；提供spec可能泄露localization/H.3超issue条件，Claim1依赖soundness/admissibility与I-P等价，§5明确非证明。Axiom fuzzing、Docker shadow与adversarial tests只给反证搜索；85→58.2为26.8百分点非相对26.8%。自写spec不改善，main单repetition，不能认证自动忠实intent。

最终 整合：PLATFORM-EVALUATION-SYSTEM Ch66:1585/1587。sep22_resume_v3实际亲读新两段与相邻论证写后PASS，unique SF-2026-ARXIV-2609-21190/exactlink、旧binding/代价/反证/fallback保留，锁释放，scoped diffcheck PASS。非独立全日Gate。

### [21216 Fewer Steps, Better Actions: Rethinking Flow-Matching Inference for VLA Policies](https://arxiv.org/html/2609.21216v1)

2 + 1 + 2 = 5，实际长期差额深入，冻结few-step candidate后demo监督endpoint residual直接执行，不是改初始状态。必要 primary：§3.1–3.3/§4.1–4.7/§5、A1–A3/TI–VII；sep22_resume_v3本轮独立实际源核，不是仅题摘或作者self-pass。prefix KV、candidate/source noise输入corrector，target=a*−sg(aθ)，backbone/AE冻结且不rerunAE；跨NFE复用不等跨backbone。Smol无noise独立checkpoint反更好，不能认证noise必要；13/50任务退步，Hard差−.56pp CI[−2.71,1.64]。额外residual forward/训练、A10080/40两个panel不能拼，b1/SDPA无compile的同步p50只model-forward不含执行。

最终 整合：MULTIMODAL-EMBODIED-VLA Ch26:174/176。sep22_resume_v3实际亲读新两段与相邻论证写后PASS，unique SF-2026-ARXIV-2609-21216/exactlink、旧binding/代价/反证/fallback保留，锁释放，scoped diffcheck PASS。非独立全日Gate。

### [21220 Safe Real-Time Policy Steering via Noise-Space Trajectory Optimization for One-Step Generative Policies](https://arxiv.org/html/2609.21220v1)

2 + 1 + 2 = 5，实际长期差额深入，在线noise particle搜索保policy函数image，不授Gaussian先验或实际安全。必要 primary：III–VI/Eq3–10/Alg1/TI–IV；sep22_resume_v3本轮独立实际源核，不是仅题摘或作者self-pass。shell-radius penalty只限范数。Alg1旧A检查→更新x→重算返回action无freshcheck，旧候选通过不保新候选；π(x)=x,c=x−.2≤0,dim1,λ=η=1,x=.1经reggrad−.396更新.496即反例（字面工程分析，未核代码）。空feasible fallback未给。fullH成本/短Te早停、NFE1不含particles/多轮gradient，real10trials仍2collision，fresh-return验收/failclosed属工程要求。

最终 整合：MULTIMODAL-EMBODIED-VLA Ch26:977/979。sep22_resume_v3实际亲读新两段与相邻论证写后PASS，unique SF-2026-ARXIV-2609-21220/exactlink、旧binding/代价/反证/fallback保留，锁释放，scoped diffcheck PASS。非独立全日Gate。

### [21227 Hallucination-R1: Robustness-Oriented Paraphrase Generation for Factual Consistency](https://arxiv.org/html/2609.21227v1)

2 + 1 + 2 = 5，实际长期差额深入，meaning/diversity先稳定，再在原答对QA人口制造failure pressure。必要 primary：§3–7/T1–4/Limitations、A1–A4/C1–C5/E/F；sep22_resume_v3本轮独立实际源核，不是仅题摘或作者self-pass。DeepSeekV3 meaning gate非严格等价；human500pairs/100questions83%与LLM87.46%只是各通过率非pairagreement/消bias。ER/WER限original-correct，而后续SFT未同样过滤，不能称纯知识稳定因果。T4 AnyAcc全下降而RobustAcc上升。Diversity squarednorm非标准cos，单例/空retained边界未认证，8A800仅generator训练不等全SFT预算。

最终 整合：TRAIN-DATA Ch27:321/323。sep22_resume_v3实际亲读新两段与相邻论证写后PASS，unique SF-2026-ARXIV-2609-21227/exactlink、旧binding/代价/反证/fallback保留，锁释放，scoped diffcheck PASS。非独立全日Gate。

### [21242 SafeStyle: Calibrated Style Residual Injection for Controllable Style-Leakage Trade-off in Diffusion Stylization](https://arxiv.org/html/2609.21242v1)

2 + 1 + 2 = 5，实际长期差额深入，style支持方向保留、内容衰减/粒度放置/总norm cap三权分开。必要 primary：§2–3/Eq1–5、ablation/stress；root本轮独立实际源核，不是仅题摘或作者self-pass。Us方向移除后orth内容基、overlap↑α↓非语义解耦；fine/mid/coarse residual汇总后cap，ηλγ只relativefeature-change。Dc不同reference appearances与sets一次复用适配边界未解，不造universal。SDXL/InstantStyle冻结，50ref20prompt/24×10stress/9baseline同seed/1RTX4090；SemLeakCLIP差是代理，cleanstyle0leak丢style、cap降DINO，成本precision/steps/SLO ND。

最终 整合：MULTIMODAL-GENERATIVE-PARADIGMS Ch24:123/125。root实际亲读新两段与相邻论证写后PASS，unique SF-2026-ARXIV-2609-21242/exactlink、旧binding/代价/反证/fallback保留，锁释放，scoped diffcheck PASS。非独立全日Gate。

### [21251 Geometry-Aware Diffusion Guidance via Curvature-Adaptive Tubular Correction](https://arxiv.org/html/2609.21251v1)

2 + 1 + 3 = 6，实际长期差额深入，normal一阶/tangent曲率二阶非抵消预算与实际目标acceptance分权。必要 primary：§2/§4 Theorems2–4/Eq8–14/Alg1、§5.3–5.4/CFG；root本轮独立实际源核，不是仅题摘或作者self-pass。host prior不变；regular levelset+tubular+thirdderivative下rN+.5K rT²≤R与高阶余项，learnedscore/Jacobian不是真manifold。Armijo period>1 reuse不是每stepaccept。Armijo-alone强而full更好、不唯一geometry因果；同100FFHQ4090 N1000 memory3612/time132 vsDPS3490/38，N200time26不是同预算gratis。COCO1000固定promptseed SD2.1局部CFG非posterior/semantic保证；AIscience extension不采用。评分Durability3限有限geometry/acceptance选择长期界，不扩大reach。

最终 整合：MULTIMODAL-GENERATIVE-PARADIGMS Ch24:414/416。root实际亲读新两段与相邻论证写后PASS，unique SF-2026-ARXIV-2609-21251/exactlink、旧binding/代价/反证/fallback保留，锁释放，scoped diffcheck PASS。非独立全日Gate。

### [21264 Programming AMD XDNA NPUs with Open-source Compiler Tools: A FlashAttention Case Study](https://arxiv.org/html/2609.21264v1)

2 + 1 + 2 = 5，实际长期差额深入，三memory domain独立roofline决定score驻留及fusion停止条件。必要 primary：§4.1–4.4/§5.1–5.3/§6.1–6.6/§7；root本轮独立实际源核，不是仅题摘或作者self-pass。scoresDDR→MemTile→computeTile，QK同DMA/V另路/cascade；instruction-count attainable ceiling非hardwarepeak。XDNA1stagedcomputeboundfusion益小，XDNA2highridge需tilelocal，compiler/buffering同步混杂非纯fusion；BF16IO与内部bfp16cast分开。attention时间含dispatch/softmax，numerator只GEMM；warm10/20 minimum非tail，Gaussianvariance误差/相关性不证wholeLLM任务无损。

最终 整合：INFER-TENSORRT-LLM Ch49:765/767。root实际亲读新两段与相邻论证写后PASS，unique SF-2026-ARXIV-2609-21264/exactlink、旧binding/代价/反证/fallback保留，锁释放，scoped diffcheck PASS。非独立全日Gate。

### [21267 Efficient Benchmarking in Production: A Study of an Evolving LLM Agent](https://arxiv.org/html/2609.21267v1)

2 + 2 + 2 = 6，实际长期差额深入，fixedweighted/adaptiveIRT重构/historical cache三支控制和证据不同。必要 primary：§2/§3.2–3.4/§4–7；root本轮独立实际源核，不是仅题摘或作者self-pass。574runs52days/cal287(D1–28)→heldout287(D29–52)，valid≥80%reference只valid人口/519题。Fisher selected rawmean非fullscore；gpIRTbias/d用cal切分不偷heldout。固定难度虽非accuracy最佳却并行/predictable；自适应顺序依赖/cachefreshness代价分开。IRTcluster局部劣random，1day14runs仅成熟窗口，5familytransfer有限；绝对/排名fidelity不互换，历史replay非生产延迟，HWprecisionconc/evaluator ND。

最终 整合：PLATFORM-EVALUATION-SYSTEM Ch66:1130/1132。root实际亲读新两段与相邻论证写后PASS，unique SF-2026-ARXIV-2609-21267/exactlink、旧binding/代价/反证/fallback保留，锁释放，scoped diffcheck PASS。非独立全日Gate。

### [21268 Edit-VAR: Taming Visual Autoregressive Model for Precise Video Editing](https://arxiv.org/html/2609.21268v1)

2 + 1 + 2 = 5，实际长期差额深入，source token支持drop条件替换与late-release不同于固定logit nudging。必要 primary：§3–5/T1–2、B/I/L必要机制/效率/failure；root本轮独立实际源核，不是仅题摘或作者self-pass。Eq2 b=max(gamma−p_src(source),0)，p_edit(source)+b对editargmax；gamma0无bias不必改token、2必保。Sstop25后自由细节，attention只区域proxy。末2scale residual提议同mask剪QKV/attn/FFN但仍logitshead。InfinityStar8B81frames480p/BF16/1A800/seed41/160cases，prune50%alignment.972/.976低无prune.979/.980，85→64只decoupled两pass，130→64联合改动不单因；大structure/edit失败，未生产SLO。

最终 整合：MULTIMODAL-GENERATIVE-PARADIGMS Ch24:1379/1381。root实际亲读新两段与相邻论证写后PASS，unique SF-2026-ARXIV-2609-21268/exactlink、旧binding/代价/反证/fallback保留，锁释放，scoped diffcheck PASS。非独立全日Gate。

### [21284 Authorization Revocation for Long-Running AI Agents: Root-Scoped Quiescence under Delegation and Asynchronous Execution](https://arxiv.org/html/2609.21284v1)

3 + 3 + 2 = 8，实际长期差额深入，root cut/local sinkbarrier与备选/合取support、跨leaf token闭合分权。必要 primary：§3 A1–A11/§4–5/§6.1/§7–8、A.3 Th10–11完整proof；root本轮独立实际源核，不是仅题摘或作者self-pass。cut冻结issue/expand非远程瞬时fence；postcut prebarrieraccepted要local-orderpre-fence receipt/futurelineage闭合。{{A},{B}}当前witness exact-operation/envelope原子rebind非自动B，{{A,B}}不得删A洗权限。完整manifest是assurance前提非checker证明；samecut/epoch/profile SEND=ACK唯一tokenprojectionmultiset非总counter；已知blocker N、opaque/conflict U、局部Q不global。Th10 A1–9与liveness A10–11分开；provider-free child/fileledger17cases/44mutations未本轮run，不vendorMCP/A2A/OAuth/physicalundo。

最终 整合：PLATFORM-SECURITY Ch72:1422/1424。root实际亲读新两段与相邻论证写后PASS，unique SF-2026-ARXIV-2609-21284/exactlink、旧binding/代价/反证/fallback保留，锁释放，scoped diffcheck PASS。非独立全日Gate。

### [21293 GameASG-Bench: Benchmarking Autonomous Software Generation for Game Development](https://arxiv.org/html/2609.21293v1)

2 + 1 + 2 = 5，标准，source declaration/check mean/strict applicable合同分账，不wholegame接口。必要 primary：§2–4/§6/T1–9；root本轮独立实际源核，不是仅题摘或作者self-pass。L1pattern非behavior/L1fail不skipL2，legalprepare不得直接给outcome；P1 NOT_APPLICABLE当前runner缩合同非whole需求。47tasks/1221checks/ref47positive，一次cleanrun/config；93.2mean≠26/47strict，预算planned47/evaluated10/32/47分母不同。两harness18各交10/各8/21neither，high19/max18单run非因果。仅Ch66交集/冻结predicate及双侧oracle已承载，game接口与配方仅报告不造diff。

最终 已有覆盖：PLATFORM-EVALUATION-SYSTEM Ch66:50–74/CompoundArtifact。root实际对读五成功交集/CompoundArtifact冻结谓词与双侧oracle通过，只三对象分账窄E；没有声称whole接口/游戏方案已有覆盖，无Books新写。非独立全日Gate。

### [21340 Conformal Privacy Auditing: Calibrated Re-identification Attacks with Statistical Guarantees](https://arxiv.org/html/2609.21340v1)

2 + 2 + 2 = 6，实际长期差额深入，候选pool miss与marginal ambiguity set/个体重识别风险分开。必要 primary：§3–5/Th5.2/Cor5.3 assumptions/proofsketch、§6–7.1/Limitations；root本轮独立实际源核，不是仅题摘或作者self-pass。declaredpool/attacker/querybudget/releaseddistribution/exchangeability下APS伪posterior/频数→marginal truthsetcoverage；1/max(1,card)proxy非probability/DP。openworld conditionalinclusion+missrho总体≥(1−rho)(1−alpha)，不可报cond替global。K50 miss.16/cond1/global.84 vsK200miss0/.97；driftTAB.965→.923/Blog.940→.835/LLM帮助不uniform，cal50/100/150非单调。索引/多采样校准成本、未知attacker不涵盖，membershipfuture/HWprecisionND。

最终 整合：PLATFORM-SECURITY Ch72:212/214。root实际亲读新两段与相邻论证写后PASS，unique SF-2026-ARXIV-2609-21340/exactlink、旧binding/代价/反证/fallback保留，锁释放，scoped diffcheck PASS。非独立全日Gate。

### [21346 IntBMoE: Integrating Block-Level Conditioning into Expert Composition for Full-Participation Mixture-of-Experts](https://arxiv.org/html/2609.21346v1)

2 + 1 + 2 = 5，实际长期差额深入，参数参与/实际block执行/派生materialization三预算。必要 primary：§3 Eq3/§4.1–4.7 Eq4–16、§5.6/T3–4/A3；root本轮独立实际源核，不是仅题摘或作者self-pass。token-independent codebook每层全基底有符号组合两路径，token仅topkblock；非f(sumW)=sumf、每基底语义/非零贡献不保。cache只fixedweights/config共用，updates重新合成，小E派生cache可能更大；18layerMiniPile1epoch1.523B/15Mheldout parameter-matched仍整模块/route，ImageNetcache非LLMruntime/通信/SLO。

最终 整合：MODEL-MOE Ch21:109/111。root实际亲读新两段与相邻论证写后PASS，unique SF-2026-ARXIV-2609-21346/exactlink、旧binding/代价/反证/fallback保留，锁释放，scoped diffcheck PASS。非独立全日Gate。

### [21358 FAN: Foresight Action Normalization for Continual Adaptation of Vision-Language-Action Models](https://arxiv.org/html/2609.21358v1)

3 + 2 + 2 = 7，实际长期差额深入，归一化统计固定身份与physical-range覆盖分账。必要 primary：III Eq2–4/IV 3C/8traj预校准、V T1/width2.5反例；root本轮独立实际源核，不是仅题摘或作者self-pass。state/action联合非action-only；未来demo不用，motion预任务同统计冻结training/replay/inverse。过宽放大physicalerror，BI1 ANSII97.2>FAN95.7，部分BWT负，4stream10rollout不普遍安全。改stats而weight固定改变action不将所有forget归weights；nextembodiment范围新校准/联合policy验收。

最终 整合：MULTIMODAL-EMBODIED-VLA Ch26:69/71。root实际亲读新两段与相邻论证写后PASS，unique SF-2026-ARXIV-2609-21358/exactlink、旧binding/代价/反证/fallback保留，锁释放，scoped diffcheck PASS。非独立全日Gate。

### [21362 Beyond Atomic Tokens: Factorizing Syllables for Language Model Pretraining](https://arxiv.org/html/2609.21362v1)

2 + 1 + 2 = 5，实际长期差额深入，音节component词表/position/信息可逆三预算。必要 primary：§3–4 Eq2/8/11–14、§5.1–5.3/T1/§7.2 T15–18；root本轮独立实际源核，不是仅题摘或作者self-pass。onset/rime/tone并列一个position，concatprojection/完整tuplemask三CEhead不漏分量。Chinesephrase lookup/default/polyphony与同音碰撞不可逆，多位fallback/UNK。Chinesecontrolled全pipeline非纯tokenizer，Viheterodata，WSC/OCNLI/CMRC部分反退，decoder-only未测/HWprecisionSLO ND。

最终 整合：MODEL-TOKENIZER Ch11:146/148。root实际亲读新两段与相邻论证写后PASS，unique SF-2026-ARXIV-2609-21362/exactlink、旧binding/代价/反证/fallback保留，锁释放，scoped diffcheck PASS。非独立全日Gate。

### [21369 ProTracer: Proprioception-Guided Failure Diagnosis in Robot Manipulation](https://arxiv.org/html/2609.21369v1)

2 + 1 + 2 = 5，实际长期差额深入，offline earliest-failure onset与终态分类/在线guard不同权限。必要 primary：III sensorSign+PELT/modalHamming/greedyframebudget与规则narrative、V TI–V；root本轮独立实际源核，不是仅题摘或作者self-pass。retrospective整段+最终fail，不含恢复transient；MAE只correctlydetected failure、binary高非onset准；长horizonMAE变差/reflection50→100不更好，GPT5judge说明不因果proof/规则不保sensortruth。运行alarm不同信息budget，CPD/VLM/annotation、采样漏/timeout成本须分账。

最终 整合：MULTIMODAL-EMBODIED-VLA Ch26:791/793。root实际亲读新两段与相邻论证写后PASS，unique SF-2026-ARXIV-2609-21369/exactlink、旧binding/代价/反证/fallback保留，锁释放，scoped diffcheck PASS。非独立全日Gate。

## 2026-10-01 正式100有限同步

新增4唯一家族均明确owner差额深入，sep22_resume_v3独立精确source→fresh actual/pre及真实两段/邻接写后PASS；root授权四窄锁已释放。累计100=74深入/24标准/2争议，71I/25E/2Only/2D；普通38，不等source最终冻结或日Gate。

### [21383 Prediction Dynamics in Depth-Recurrent Language Models](https://arxiv.org/html/2609.21383v1)

2 + 1 + 2 = 5，实际差额深入。必要精确v1：固定候选margin/终点诊断与prefix检验、A1–A2。当前唯一winner a、g_b=s_t,a−s_t,b>0、δ=s_T−s_t、u_b=δ_b−δ_a，终点严格保留当且仅当每个g_b−u_b>0；共同平移不改比较，osc(δ)只给最坏相对变化，不能最大update配最小gap宣称实际翻转。δ读取未来，是completed-trajectory诊断非online stopper，答案保留非真值；固定多选/quarter grid T32vs4不外推开放生成，prefix quotient逊mean-centering，2.54%高于2.5%目标不作有限样本保证。A1–A2固定revision的32题F3与独立128题F1不同人口，Huginn/Ouro BF16 recurrence/FP32 head、5000whole-question bootstrap，几何百分点不是执行latency。

最终整合：MODEL-TRANSFORMER-LAYER Ch17:570/572。peer独立必要source→fresh owner/literal及真实两段/邻接写后PASS；唯一SF/旧body/限制/fallback保留，锁释放，限定diffcheck PASS，不是日Gate。

### [21400 A Scene Language Model for Open-Vocabulary Scene Mapping](https://arxiv.org/html/2609.21400v1)

2 + 2 + 2 = 6，实际差额深入。必要精确v1：text-state/ADD–EDIT–REMOVE方法、受限mapping/检索评价与G2.3/G3。对象label/description/world position为text state，pose/depth选可见entries、RGB→ADD/EDIT/REMOVE与2Danchor回投3D；每对象独立corruption训练修订，未提及保持。文本丢细节、有限纠错误触正确entry，同A100 mapping843/965ms高于258/275ms约三倍，memory较小不是更快；机器人移动≥.5m才处理frame，不逐frameSLO/动态长期安全。point-in-box与原IoU协议分开，pose uncertainty/移动人更多duplicate。Jetson BF16/NVFP4 vLLM.19与FP8 v.13不能纯归precision。

最终整合：MULTIMODAL-WORLD-MODELS Ch25:396/398。peer独立必要source→fresh owner/literal及真实两段/邻接写后PASS；唯一SF/旧body/限制/fallback保留，锁释放，限定diffcheck PASS，不是日Gate。

### [21423 DENSE: Distilling Agent Trajectories into Evidence-Grounded Shortcut Trees for Self-Refinement](https://arxiv.org/html/2609.21423v1)

2 + 2 + 2 = 6，实际差额深入。必要精确v1：子目标树/repair方法、same-source/reset对照、A3/B2。连续action–observation子目标nested tree，只同parent压缩重复attempt并保source，后继recovery重审issue；完成分支压缩/unfinished展开obligation，构建动作保留供fresh重建，derived analyst判断非hidden verifier或FS事实。固定同run0信息源，posthoc outcome仅评价端，recipient环境/context重置；3重复TerminalBench只same-task retry，privilegedVF修复更多但丢历史成功。A3 7308outcomes/1782仅completedcalls，未知usage不补0；B2明确run0+feedback+rerun合计2.96USD，36.6%只feedback+run1相对run0，不说论文无总cost或完整workflow同等省。

最终整合：AGENT-MEMORY Ch77:436/438。peer独立必要source→fresh owner/literal及真实两段/邻接写后PASS；唯一SF/旧body/限制/fallback保留，锁释放，限定diffcheck PASS，不是日Gate。

### [21432 GVPO++: Group Variance Policy Optimization for LLM Post-Training and On-Policy Distillation](https://arxiv.org/html/2609.21432v1)

2 + 1 + 2 = 5，实际差额深入。必要精确v1：V-B新OPD公式/证明、V-C符号反例、VII实验。每response正f、partition存在且same support，P∝exp(f logπ)，P_student=P_teacher仍指向原π相等；中心化f log(student/teacher)平方损失消prompt partition ratio，不需token对齐但需共同response/scoring/support。无importance ratio因为不同loss，不是离线无偏原PG；global zero-loss不保有限参数/样本/截断decoder或Adam收敛。长度f=|y|^-alpha最佳随teacher变化。V-C student>teacher却log比<0符号反向不采；仅新OPD，不重复NeurIPS2025 GVPO核心。VII各法LR三值grid/k4/256prompt及mini256/2epochs，OPD seed/HWdtype完整成本未披露，不移借旧10seeds。

最终整合：TRAIN-GRPO Ch33:924/926。peer独立必要source→fresh owner/literal及真实两段/邻接写后PASS；唯一SF/旧body/限制/fallback保留，锁释放，限定diffcheck PASS，不是日Gate。

## 2026-10-01 作者有限提案 21450 / 21482（普通待采用）

### 21450 — Understanding LLM Quantization through Activation-Guided Compensation and Orthogonal Residuals

2 + 1 + 2 = 5，标准必要源后确认具体owner差额，拟受影响深入，未获锁/未Books、未计formal。INFER-TENSORRT-LLM；Ch49 ResComp原始目标两段/SF2604-07955末之后→per-token gate补偿之前。作者实际读exact-v1 §3/§4.1–4.6/§5–6，B.1 Theorem1完整证明 Eq41；固定P、Z=XP、V=WP^-T，量化A=Ztilde−Z，Vstar^T=V^T−Ztilde†AV^T。精确J=||Ztilde(Vtilde−Vstar)^T||F²/T+||(I−Π)AV^T||F²/T，Π=ZtildeZtilde†；固定输入下正交残余不由任意weightchoice消除，unrestricted最优不意味着lowbit可实现。作者明确CoreQ full-columnrank先例，不能说投影恒等式首次新发现；这里只保与actual原始target不同的compensable/orthogonal职责。CO+regular不是新的精确加项，是上界分解启发；L2缩放来自Frobenius/CauchySchwarz放宽、L∞另放宽，实践fullX代Xreg。理论dynamic per-token uniform无clipping，W4A4KV4实验clip.9/.95/GPTAQ128WT2train/scaling512不能照搬无clipping证书。8模型1–13B更低PPL非所有6task最好：Llama3.2-3B低SpinQuant1.09pp；RTN10候选top3GPTAQ与WT2val选择增加calibration预算，100seeds子采样不等部署SLO，未核code/复现、HW完整runtimeND。

拟≤2段 literal：

固定原始浮点输出后，还要问输入量化误差中哪些部分能由本层权重补偿。冻结校准输入及变换，记量化后的输入矩阵为 Z̃，它的列空间投影为 Π；相对于最小二乘补偿权重，输出误差可精确拆成落在该列空间中的权重拟合误差，以及与其正交的输入残余。后者对这个固定输入矩阵不能靠继续改变权重消除；前者的无约束最优也未必落在低比特可表示集合内。因此补偿搜索与改变输入表示是两种自由度，不应把所有残余都交给更宽的权重搜索，也不把一次最小二乘解当作低比特无损保证。

选择输入变换时，persistent outlier 与普通通道统计可分别进入残余上界；据此选择符号旋转和缩放，是界引导的校准分支，不是精确误差再多出两个独立项。L2 与最大幅度缩放来自不同放宽，实际以完整输入近似普通通道统计也须另验；无 clipping 的理论条件不能静默继承给带 clipping 的实验。更低 perplexity 并未使所有任务准确率更好，候选旋转、teacher/scoring 与补偿筛选均付校准成本，低位模拟结果不证明目标 kernel 更快。统计失配、下游质量回退或执行成本不合适时，保留原始目标补偿、较简单变换与更高精度。 [必要机制与反证](https://arxiv.org/html/2609.21450v1)。<!-- 拟source-family:SF-2026-ARXIV-2609-21450；非actual写入 -->

### 21482 — Adaptive Rollout Truncation Based on Epistemic Uncertainty for Efficient Offline World Model Training

2 + 1 + 2 = 5，标准必要源后确认具体owner差额，拟受影响深入，未获锁/未Books、未计formal。MULTIMODAL-WORLD-MODELS；Ch25 Imagined rollout的Biased Dreams两段与SF2604-25416后→Computer-use imaginedUI前。作者实际读exact-v1 III/IV/V/VI/VII、TablesI–II、AppA/B/E/F；这是训练期gradient-depth curriculum而非部署planning-gate。sharedGRU+5bootstrapMLP或MCdropout10pass，50single-step warmup+10full32；hmin4后batchmean epistemic≥T首次stop，仅已生成步收gradient。anchor@k是阈值参照horizon不是actual长度；warmup末10次median/≥3runs均值frozen同reportedseeds。ANYmalD31 250segments max200 mean192≈6M45obs12actions/Ant6000×1000约6M105/8；offlinePPO行为走向更强policy非onlineRL。segment-level .1val，32history+32forecast stride32/zscoretrain-only。Fixed32 RMSE32 .314、160 .429/3250steps，Fixed8 .274/.458/1090，Adaptive2 .288/.389/924（三seed）；短期不是最好。AppE含GRUhistoryFLOPs Fixed32 60.2PF vsAdaptive18.0但前者ownconvergence后者fixed32accuracy，不是纯同停点GPUtime。AppF明确无coverage calibration，来自每seedadaptive运行的scripted length replay复现withinseednoise，不能将unique uncertainty causal收益外推；schedule oracle是post-run非deployablemanual。MCdropout参数对lengthgrowth敏感，额外uncertainty/head/candidate/warmup开销须计；HWprecision与真实physicsSLO未披露。

拟≤2段 literal：

不确定性还可调节训练课程，而不拥有部署时的动作放行权。固定很长的自回归训练 horizon 会把预算花在尚不可靠的深层预测上；一个替代分支先做单步与完整 horizon 的 warmup，再冻结由这些训练运行估计的阈值，在 batch 平均 epistemic 分歧首次越界时截断，保留最小展开长度。只有实际生成的深度收到梯度，因此它改变的是训练样本的深度分布与课程；阈值参照的 anchor horizon 不是每次实际展开长度，训练期停止也不等于 planner 对真实未来作了风险认证。

这一阈值是自校准启发式而非 coverage 证书。较短固定 horizon 的短期误差可更低，adaptive 路线的远期改善应与不同 horizon 的指标、训练停止点和重复运行分别比较；额外 ensemble/dropout、warmup、历史编码及逐步预测都付费，steps/FLOPs 减少不自动等于墙钟或控制 SLO。按已完成 adaptive run 回放相同长度课程可重现近似收益，限制了‘只有在线不确定性才带来增益’的归因。训练分布或 estimator 改变时需重新校准课程与 held-out 长展开；共同偏差、课程失准或质量回退时，固定/预设 horizon 仍是合理训练分支，部署继续接受真实观测与独立 controller 验收。 [必要机制与反证](https://arxiv.org/html/2609.21482v1)。<!-- 拟source-family:SF-2026-ARXIV-2609-21482；非actual写入 -->

## 2026-10-01 作者有限提案 21449 / 21455（普通待采用）

### 21449 — ME-Dex 1.0: Bringing Heterogeneous Tactile Sensing into World Action Modeling

2 + 2 + 2 = 6，必要范围后确认拟受影响深入。MULTIMODAL-EMBODIED-VLA；Ch26 ForeTac20980两段末之后→Training-only Foresight heading前。作者实际读exact-v1 §3.1–3.5/§4.1–4.5 Tables1–5/§5；30layervideoWan2.2-5B3072/action1024/tactile512三expert，中间H-Bridge共享attn投影兼容，早晚独立；独立每modal噪声/σ,currentcondition clean,futureGT trainonly,jointflow推理读未来tac latent不是独立forecastprefix。异构normal+2tangent3×H×W/deadzone/asinh/normclip、canonical左/右finger/palm/observedmask；unobserved不同observedno-contact。冻结deterministictactileAE contact+force+transition/per-source归一化，source-specific forceMAE不跨平台直接比较。Engine simulationactionreplay加sensor相同window是模拟标注不真physical。RoboTwin27500CleanRandom50tasks另2500Clean→Random；DexJoCo1100demo11tasks/ManiFeel50each4singletrain，单trainingseed；DP-T/pi quoted/DECOofficial发布非uniformretrain。T1VA86.90Random→TacCond89.54→FullJoint90.60→HBridge91.92，不能各独立唯一因果；zero-current91.74接近observed91.92仍保tac训练/未来预测。FastTac小好piTac57.66<60.74；DexPhoto48<DECO76、ManiGear60<66。realSO101/PX/Xynova只qualitative不新量化闭环；§5明确高频触觉localfeedback未来工作，当前chunk间obs/replan。hardwareprecisionconcurrency/end2endSLO未披露，不借video30层训练推安全。actual现FuturetoAction/ForeTac有预测prefix与教师切换，缺三modal jointgeneratedfuturetouch和observedmask的接口角色。 未获锁/未Books，不计formal。

拟≤2段 literal：

未来触觉还可以与视频、动作共同生成，而不是先完成一个 forecast 再把它加到 action prefix。一个条件分支把当前图像、proprioception 与触觉作为共同条件，为未来 video、tactile state 与 action chunk 设置独立噪声与各自 flow 目标，只在中间层交换兼容表示。触觉接口需同时保存 canonical hand region、有效节点和时间身份：未观察到某区域不同于观察到但无接触，模拟回放补出的力场也不同于实机读数。共同生成的未来接触只是 action proposal 的内部证据，不能晋升为已发生的物理事实；这条分支也不等于训练后删除触觉 decoder 的 auxiliary supervision。

joint stream 增加触觉编码、未来采样、共享 attention 与配对数据生产成本，不能只以当前触觉是否输入拆解其因果作用。受限实验中，归零当前触觉仍保留触觉训练与未来预测，成功率接近完整输入；若干外部 tactile 条件基线和具体任务还退步，单 seed 与不同训练来源不支持普遍增益。跨布局的重构误差必须按源归一化分别解释，真实机器人的可视化不替代量化闭环或高频 feedback 验证。当前路线仍在 chunk 间更新观测与重规划；触觉身份/预测失准、接触突变或额外采样超预算时，保留当前触觉/direct policy、短 chunk 与独立 controller，不由未来触觉生成自授安全。 [必要机制与反证](https://arxiv.org/html/2609.21449v1)。<!-- 拟source-family:SF-2026-ARXIV-2609-21449；非actual写入 -->

### 21455 — CompAdapt

2 + 1 + 2 = 5，必要范围后确认拟受影响深入。MULTIMODAL-GENERATIVE-PARADIGMS；Ch24 Physics-aware video SF2609-13006:end后→复杂视觉Plan heading前。作者实际读exact-v1 §3.1–3.5 Eq1–14、§4.1–4.3 Tables1–4、AppB/C/E/G（必要parser/成本与耦合反例，非全D/H）；10D2Dcentroid/v/rotation/scale/area+mass，dualQwenparser motionseq12types/parameterdecoding separated numericverbatim vsadjectiveslabels vsabsentnone+deterministic sampling(AppB)非估计真质量。Eq6同initial state displacement加massmask，只有disjointcomponents exact/严格交换，coupled pure rolling v=ωr不可；temporal chainingterminalstate→nextinit，threshold contact separatelylearnedelastic2bodyjump resetsstate不通用contactmechanics。trajectory+warppatchrotation/scale与adaptiveblendWanMove生成解耦，不是guaranteedphysicalallfeatures。PriorMatching12pretrainmodule最低referenceMSE再L2anchorregularized100epoch5e-3AdamW/84frame;reference1of10其余9/5referencechoices，first28→84only12/34drop<.02，near22 .888/mid5 .854/far5 .515/adversarial2 .730。C saturationg980 PIS约.83但trajectoryerr爆，PIS只invariantstd/mean不是轨迹正确与真law辨识；三publicvideosSAM2tracking/derivedreference不能无跟踪偏。G pure rolling .784–.794 vsuncoupledslope .978–.982是additive边界，不采Eq3.4 guaranteedphysics。单RTXA6000/fixedrandomseeds非multi-seed；code/dataset releaseuponacceptance未核artifact，完整render steps/dtype/latencySLO ND。AppB2000parserlabel accuracy不是真实质量数值准确。actual13006 kinematicplan/localgradientrouter只proposal，不含continuous parallel/sequential和contact jump分开的generator接口。 未获锁/未Books，不计formal。

拟≤2段 literal：

可控视频中的 kinematic plan 还要区分并行分量、时间串接与离散接触，不能把多个动作名称直接当作可相加的物理定律。一个受限生成分支先把文字分成 motion sequence 与数值/定性参数，再由各运动模块提出同一初始状态下的位移；作用于不相交状态分量时可相加，顺序动作则以上段终态作为下段初态，接触时另用有质量条件的跃迁模块重置状态。轨迹再指导视频 latent 的局部旋转/缩放与有界混合；文字解析、动力学候选与外观生成拥有不同的误差来源，不由渲染流畅补齐参数或接触正确性。

这种可组合接口限定在二维、少量运动类别与简单两体接触。平移/旋转存在滚动约束时独立相加仅是近似，稠密接触、关节链与超范围动力学不获保证；从一个跟踪轨迹选择近似 prior 并正则微调也不能识别通用物理法则。受限评价中，运动 invariant 可较稳定而轨迹误差已经爆增，较远结构偏移与部分早期窗口外推明显失败，因此应把 invariant、轨迹和视觉质量分开验收。解析、tracking、prior 搜索、适配与 latent 调制都付费，公开视频的派生轨迹也不是无误差真值；耦合强、标注/参数不可靠或预算不足时，回到可信 simulator/人工轨迹、较简单运动条件或普通生成，不从局部一致性分数签发物理保真。 [必要机制与反证](https://arxiv.org/html/2609.21455v1)。<!-- 拟source-family:SF-2026-ARXIV-2609-21455；非actual写入 -->

## 2026-10-01 正式108有限同步

新增root4与peer4均实际窄写且对应独立写后PASS，八锁释放。108=82深入/24标准/2争议、79I/25E/2Only/2D，普通30；精确v1必要source→fresh owner/pre与post范围如下，不等整日验收。

### [21483 Weave: Fine-Grained Dynamic SM Scheduling in an MoE Megakernel for Compute-Communication Overlap](https://arxiv.org/html/2609.21483v1)

2 + 2 + 2 = 6，actual长期gap受影响深入。必要精确源：routing后SM/chunk方法、硬件profile与受限prefill评价。dispatch不chunk，comm完成dispatch后steal GEMM、combine全SM；dispatch远端token去重不等combine贡献合并。K上升小GEMMthroughput跌，α/throughput依硬件profile。4H10080G SXM NVSwitch EP4 BF16 batch1 ShareGPT2/4/8K prefill（消融16K），配置距实测最优平均8.2%，1.33E2E≠2.89layer；未验decode/SLO/恢复，codeuponacceptance不是复现。

最终整合：INFER-TENSORRT-LLM Ch49:119/121。root独立必要source→fresh owner/pre与实际两段/邻接写后PASS；uniqueSF/exactlink、旧binding及限制/fallback保留，锁释放，限定diffcheckPASS，不是日Gate。

### [21502 Adaptive World Memory 3D Foundation Model for Scalable 3D Mapping, Localization, and Rendering](https://arxiv.org/html/2609.21502v1)

2 + 1 + 2 = 5，actual长期gap受影响深入。必要精确源：GRU/runtime regulator方法、Apartment消融及五条真实轨迹。GRU reset/update先候选M，sigmoid temporal×spatial二次blend非校准prob/严格零更新；decoder本帧point/pose在最终memory融合前，不称所有head用finalM。active M/keyframe/pose/pointmap/Gaussian，inactive保留/低overlap新anchor/globalSL4校正另owner；detached geometryconfidence不真值。单RTX4090/五轨迹平均ATE非每条最好，precision/controlSLO ND。

最终整合：MULTIMODAL-WORLD-MODELS Ch25:404/406。root独立必要source→fresh owner/pre与实际两段/邻接写后PASS；uniqueSF/exactlink、旧binding及限制/fallback保留，锁释放，限定diffcheckPASS，不是日Gate。

### [21509 The Communication Bottleneck: A Round-Trip Study of Tree-Structured Expression Serialization in Language Models](https://arxiv.org/html/2609.21509v1)

2 + 1 + 2 = 5，actual长期gap受影响深入。必要精确源：树表达式serialization/符号oracle、guard分母与受限16×16实验。2450表达式16model greedy/no thinking，原符号oracle只相同接口；完整suite guardfail0、missing/duplicate另记。任一成功非文本无歧义/全部失败非独立sender错误，guardfalse-negative抬高score不是保守下界；73.6% fault归因不采。same-semantic树拓扑微调与fewshot跨域不能泛transfer，共享oracle范围保。

最终整合：PLATFORM-EVALUATION-SYSTEM Ch66:728/730。root独立必要source→fresh owner/pre与实际两段/邻接写后PASS；uniqueSF/exactlink、旧binding及限制/fallback保留，锁释放，限定diffcheckPASS，不是日Gate。

### [21514 Skel-WAM: A Hand-Skeleton-Conditioned World Action Model for Human-to-Robot Manipulation Transfer](https://arxiv.org/html/2609.21514v1)

2 + 2 + 2 = 6，actual长期gap受影响深入。必要精确源：III共同keypoint/三expert分阶段方法，Tables2–3/OOD反侧。human估计与robotURDF/标定拓扑坐标/valid/time不同producer，human无robotactions；actionhead训练读GTfuture/部署generated。额外human/阶段/训练预算混杂，sim任务及backgroundOOD反退。8A800训练，real13frames384²stride6/73steps、simstride3/37steps，30Hzaction非video/keypoint/actionfull采样SLO，precisionconcurrencyND。

最终整合：MULTIMODAL-EMBODIED-VLA Ch26:485/487。root独立必要source→fresh owner/pre与实际两段/邻接写后PASS；uniqueSF/exactlink、旧binding及限制/fallback保留，锁释放，限定diffcheckPASS，不是日Gate。

### [21521 VidOmni-Bench: A Benchmark for Fine-Grained Video Understanding via Spatio-Temporal Event Verification across Complexity and Duration](https://arxiv.org/html/2609.21521v1)

2 + 1 + 2 = 5，actual长期gap受影响深入。必要精确源：§3–4/B3–4/C1/D1–2。negative来自五captioner自然错误非gold规则hardnegative；timestamp错位≠事件不存在/重复随视频重新核。500video/五复杂度/多时长，pair macroF1；5annotator pool但每pair至少2/作者裁定、κ.50不真值；30video certificate限定，不拼T6/T8不同帧预算成matched因果，更高帧率不单调/audio效果相反。

最终整合：PLATFORM-EVALUATION-SYSTEM Ch66:570/572。sep22_resume_v3独立必要source→fresh owner/pre与实际两段/邻接写后PASS；uniqueSF/exactlink、旧binding及限制/fallback保留，锁释放，限定diffcheckPASS，不是日Gate。

### [21523 What Must Survive? Exact Task-Information--State Frontiers for Resource-Sufficient Learning](https://arxiv.org/html/2609.21523v1)

2 + 1 + 2 = 5，actual长期gap受影响深入。必要精确源：§2 Th2.2 proof/Cor2.3/2.4/Th2.5proof、§3.1/§5。完整x可见、有限线性任务/≤Kadvice先state后具体task、continuousenc/dec单位球最坏精确p*=minpartitionmaxstackedrank。私有子空间直和等维才闭式，continuouscoordinate不是finitebit/KV/learnability；approx上下界group大小/singularvalues，strongNP-hard分组，固定keys有限query attention非自由continuation淘汰算法。

最终整合：MODEL-LONG-CONTEXT Ch22:448/450。sep22_resume_v3独立必要source→fresh owner/pre与实际两段/邻接写后PASS；uniqueSF/exactlink、旧binding及限制/fallback保留，锁释放，限定diffcheckPASS，不是日Gate。

### [21543 From Retrieval to Recognition:How Vision--Language Models Become OCR Specialists](https://arxiv.org/html/2609.21543v1)

2 + 2 + 2 = 6，actual长期gap受影响深入。必要精确源：§3–6/AppA/B/D/Fig9–10关键counter。自由生成prefix replay，只合法未截断/完整reference匹配且有imageevidence tokens，independentpage split/layer matchedrandomhead controls。Qwen2/3VL2B top20大部分保留不证明features/circuit全部不变，deployprompt共同改变；Qwen3base table非全面胜random/文本非单调。固定QK/attention Vpatch仅logit差不翻winner，mass/Vdiffnorm未match不单独充分。

最终整合：MULTIMODAL-REPRESENTATION Ch23:790/792。sep22_resume_v3独立必要source→fresh owner/pre与实际两段/邻接写后PASS；uniqueSF/exactlink、旧binding及限制/fallback保留，锁释放，限定diffcheckPASS，不是日Gate。

### [21561 On Repulsive and Attractive Teachers: Separating Correctness from Behavior in Self-Distillation](https://arxiv.org/html/2609.21561v1)

2 + 1 + 2 = 5，actual长期gap受影响深入。必要精确源：§3–6/A2–3/B1–3。balancedreverseKL algebra消student半logcorrect/incorrect，sharedstyle能否取消另验；actual sampled-token generalizedJSD非精确sameformula。Qwen3-4B数学288/Anagrams400，仅incorrectrollout且group双context/frozenEMA0/noGRPO；repulsion激活但不胜thinkingbaseline后lengthcollapse，Anagrams已thinkingattraction也有增益/tokenpoolshuffle反侧。mean@4非pass@4，trainseed/HWdtypeND。

最终整合：TRAIN-GRPO Ch33:1022/1024。sep22_resume_v3独立必要source→fresh owner/pre与实际两段/邻接写后PASS；uniqueSF/exactlink、旧binding及限制/fallback保留，锁释放，限定diffcheckPASS，不是日Gate。

## 2026-10-01 正式120有限同步

新增12实际I均非作者源→actual/pre及post通过，12窄锁释放；120=94深入/24标准/2中心争议、91I/25E/2Only/2D，普通18。前面未获锁/未写为提案历史快照，本节是这些家族的唯一当前处置。不等source最终冻结或日Gate。

### [21449 ME-Dex 1.0: Bringing Heterogeneous Tactile Sensing into World Action Modeling](https://arxiv.org/html/2609.21449v1)

2 + 2 + 2 = 6；具体owner差额/保护深入。必要exact-v1：§3.1–3.5/§4.1–4.5 Tables1–5/§5。30layervideoWan2.2-5B3072/action1024/tactile512三expert，中间H-Bridge共享attn投影兼容，早晚独立；独立每modal噪声/σ,currentcondition clean,futureGT trainonly,jointflow推理读未来tac latent不是独立forecastprefix。异构normal+2tangent3×H×W/deadzone/asinh/normclip、canonical左/右finger/palm/observedmask；unobserved不同observedno-contact。冻结deterministictactileAE contact+force+transition/per-source归一化，source-specific forceMAE不跨平台直接比较。Engine simulationactionreplay加sensor相同window是模拟标注不真physical。RoboTwin27500CleanRandom50tasks另2500Clean→Random；DexJoCo1100demo11tasks/ManiFeel50each4singletrain，单trainingseed；DP-T/pi quoted/DECOofficial发布非uniformretrain。T1VA86.90Random→TacCond89.54→FullJoint90.60→HBridge91.92，不能各独立唯一因果；zero-current91.74接近observed91.92仍保tac训练/未来预测。FastTac小好piTac57.66<60.74；DexPhoto48<DECO76、ManiGear60<66。realSO101/PX/Xynova只qualitative不新量化闭环；§5明确高频触觉localfeedback未来工作，当前chunk间obs/replan。hardwareprecisionconcurrency/end2endSLO未披露，不借video30层训练推安全。actual现FuturetoAction/ForeTac有预测prefix与教师切换，缺三modal jointgeneratedfuturetouch和observedmask的接口角色。

最终整合：MULTIMODAL-EMBODIED-VLA Ch26:301/303；采用命题仅future video/touch/action联合stream与observed mask明确producer而非预测真值。root独立必要source→fresh owner/pre及真实两段/邻接写后PASS，uniqueSF、旧binding/全部直接反例/fallback保留，窄锁释放；未复现或签生产保证，scoped diffcheck PASS，非日Gate。

### [21455 CompAdapt: Adaptable Composite Motion Modeling for Physics-Consistent Text-to-Video Generation](https://arxiv.org/html/2609.21455v1)

2 + 1 + 2 = 5；具体owner差额/保护深入。必要exact-v1：§3.1–3.5 Eq1–14、§4.1–4.3 Tables1–4、AppB/C/E/G（必要parser/成本与耦合反例，非全D/H）。10D2Dcentroid/v/rotation/scale/area+mass，dualQwenparser motionseq12types/parameterdecoding separated numericverbatim vsadjectiveslabels vsabsentnone+deterministic sampling(AppB)非估计真质量。Eq6同initial state displacement加massmask，只有disjointcomponents exact/严格交换，coupled pure rolling v=ωr不可；temporal chainingterminalstate→nextinit，threshold contact separatelylearnedelastic2bodyjump resetsstate不通用contactmechanics。trajectory+warppatchrotation/scale与adaptiveblendWanMove生成解耦，不是guaranteedphysicalallfeatures。PriorMatching12pretrainmodule最低referenceMSE再L2anchorregularized100epoch5e-3AdamW/84frame;reference1of10其余9/5referencechoices，first28→84only12/34drop<.02，near22 .888/mid5 .854/far5 .515/adversarial2 .730。C saturationg980 PIS约.83但trajectoryerr爆，PIS只invariantstd/mean不是轨迹正确与真law辨识；三publicvideosSAM2tracking/derivedreference不能无跟踪偏。G pure rolling .784–.794 vsuncoupledslope .978–.982是additive边界，不采Eq3.4 guaranteedphysics。单RTXA6000/fixedrandomseeds非multi-seed；code/dataset releaseuponacceptance未核artifact，完整render steps/dtype/latencySLO ND。AppB2000parserlabel accuracy不是真实质量数值准确。actual13006 kinematicplan/localgradientrouter只proposal，不含continuous parallel/sequential和contact jump分开的generator接口。

最终整合：MULTIMODAL-GENERATIVE-PARADIGMS Ch24:1258/1260；采用命题仅不相交并行位移、时间串接与接触jump的组合接口分权。root独立必要source→fresh owner/pre及真实两段/邻接写后PASS，uniqueSF、旧binding/全部直接反例/fallback保留，窄锁释放；未复现或签生产保证，scoped diffcheck PASS，非日Gate。

### [21450 Understanding LLM Quantization through Activation-Guided Compensation and Orthogonal Residuals](https://arxiv.org/html/2609.21450v1)

2 + 1 + 2 = 5；具体owner差额/保护深入。必要exact-v1：§3/§4.1–4.6/§5–6，B.1 Theorem1完整证明 Eq41。固定P、Z=XP、V=WP^-T，量化A=Ztilde−Z，Vstar^T=V^T−Ztilde†AV^T。精确J=||Ztilde(Vtilde−Vstar)^T||F²/T+||(I−Π)AV^T||F²/T，Π=ZtildeZtilde†；固定输入下正交残余不由任意weightchoice消除，unrestricted最优不意味着lowbit可实现。作者明确CoreQ full-columnrank先例，不能说投影恒等式首次新发现；这里只保与actual原始target不同的compensable/orthogonal职责。CO+regular不是新的精确加项，是上界分解启发；L2缩放来自Frobenius/CauchySchwarz放宽、L∞另放宽，实践fullX代Xreg。理论dynamic per-token uniform无clipping，W4A4KV4实验clip.9/.95/GPTAQ128WT2train/scaling512不能照搬无clipping证书。8模型1–13B更低PPL非所有6task最好：Llama3.2-3B低SpinQuant1.09pp；RTN10候选top3GPTAQ与WT2val选择增加calibration预算，100seeds子采样不等部署SLO，未核code/复现、HW完整runtimeND。

最终整合：INFER-TENSORRT-LLM Ch49:934/936；采用命题仅固定量化输入列空间中可补偿误差与正交不可消残余分账。root独立必要source→fresh owner/pre及真实两段/邻接写后PASS，uniqueSF、旧binding/全部直接反例/fallback保留，窄锁释放；未复现或签生产保证，scoped diffcheck PASS，非日Gate。

### [21482 Adaptive Rollout Truncation Based on Epistemic Uncertainty for Efficient Offline World Model Training](https://arxiv.org/html/2609.21482v1)

2 + 1 + 2 = 5；具体owner差额/保护深入。必要exact-v1：III/IV/V/VI/VII、TablesI–II、AppA/B/E/F。这是训练期gradient-depth curriculum而非部署planning-gate。sharedGRU+5bootstrapMLP或MCdropout10pass，50single-step warmup+10full32；hmin4后batchmean epistemic≥T首次stop，仅已生成步收gradient。anchor@k是阈值参照horizon不是actual长度；warmup末10次median/≥3runs均值frozen同reportedseeds。ANYmalD31 250segments max200 mean192≈6M45obs12actions/Ant6000×1000约6M105/8；offlinePPO行为走向更强policy非onlineRL。segment-level .1val，32history+32forecast stride32/zscoretrain-only。Fixed32 RMSE32 .314、160 .429/3250steps，Fixed8 .274/.458/1090，Adaptive2 .288/.389/924（三seed）；短期不是最好。AppE含GRUhistoryFLOPs Fixed32 60.2PF vsAdaptive18.0但前者ownconvergence后者fixed32accuracy，不是纯同停点GPUtime。AppF明确无coverage calibration，来自每seedadaptive运行的scripted length replay复现withinseednoise，不能将unique uncertainty causal收益外推；schedule oracle是post-run非deployablemanual。MCdropout参数对lengthgrowth敏感，额外uncertainty/head/candidate/warmup开销须计；HWprecision与真实physicsSLO未披露。

最终整合：MULTIMODAL-WORLD-MODELS Ch25:299/301；采用命题仅epistemic截断改变训练gradient-depth课程不授部署认证。root独立必要source→fresh owner/pre及真实两段/邻接写后PASS，uniqueSF、旧binding/全部直接反例/fallback保留，窄锁释放；未复现或签生产保证，scoped diffcheck PASS，非日Gate。

### [21573 Micro-Collaborative Poisoning: A Distributed Attack on RAG Systems](https://arxiv.org/html/2609.21573v1)

2 + 2 + 2 = 6；具体owner差额/保护深入。必要exact-v1：多片段联合方法、双数据库实验与DPAR/OLS边界。这项检查增加联合阅读、支持关系与 provenance 维护成本。受限攻击实验中的 DPAR 是启发式 proxy，OLS 关联不构成通用 detector 或 defense 证书；top-k 增大也不总是更安全，不能只用一个成功率决定检索预算。应沿 exposure、selection、use 到 answer effect 分别记录攻击路径，并用真正独立的支持与 utility 回归复测。组合证据不可信或风险无法隔离时，回退单一可信来源、缩小 Context 或人工核对，而不是从局部正常文本推定联合安全。

最终整合：AGENT-RAG Ch76:849/851；采用命题仅joint-context与来源独立性补局部passage检查盲区。root独立必要source→fresh owner/pre及真实两段/邻接写后PASS，uniqueSF、旧binding/全部直接反例/fallback保留，窄锁释放；未复现或签生产保证，scoped diffcheck PASS，非日Gate。

### [21576 GestureFAR: Streaming Co-Speech Gesture Generation with Flow Autoregression](https://arxiv.org/html/2609.21576v1)

2 + 1 + 2 = 5；具体owner差额/保护深入。必要exact-v1：head-only distillation与cached conditioning方法、BEAT2质量/FGD冲突。one-NFE 只计该 head，不包含 AR、decoder、buffer 与条件缓存成本。训练缓存的条件与部署自产生的 motion history 可能失配，须另验 streaming 累积误差及端到端延迟；BEAT2 的受限主 speaker 结果不认证任意角色、时长或实时 SLO，FGD 两表的尺度冲突也不拼接为同一质量点。缓存身份或生成质量不成立时，应刷新条件、增加 head 求值或保留原多步 sampler；较轻 head 不自动获得整个 pipeline 的质量与时延保证。

最终整合：MULTIMODAL-GENERATIVE-PARADIGMS Ch24:361/363；采用命题仅causal AR历史与continuous flow head预算/蒸馏分别验收。root独立必要source→fresh owner/pre及真实两段/邻接写后PASS，uniqueSF、旧binding/全部直接反例/fallback保留，窄锁释放；未复现或签生产保证，scoped diffcheck PASS，非日Gate。

### [21594 HyperParallel-FSDP: Topology-Aware Fully Sharded Training with Layout-Driven Muon on Ascend SuperPods](https://arxiv.org/html/2609.21594v1)

2 + 2 + 2 = 6；具体owner差额/保护深入。必要exact-v1：module-boundary layout及双mode方法、一步gradient/16Ascend60-step评价。这种分工把语义检查和 hot path 成本分开，却增加 compiler、边界 coverage 与 fallback 的维护。opaque 域、具体 collective 或尚未支持的布局不能因同一 plan 就标已验证；一步 gradient 对照和 16 Ascend 上有限 60-step 运行，也不证明所有 optimizer 状态 bitwise 一致或长程收敛等价。不同 mode 的速度对照不能把全部差异唯一归因于原生 DTensor metadata。边界无法表达、梯度/状态不符或收益不足时，保留验证执行、显式通信与成熟分布式 runtime。

最终整合：TRAIN-DISTRIBUTED-TRAINING Ch36:634/636；采用命题仅同module placement plan的验证DTensor与生产local/compiled collective双mode。root独立必要source→fresh owner/pre及真实两段/邻接写后PASS，uniqueSF、旧binding/全部直接反例/fallback保留，窄锁释放；未复现或签生产保证，scoped diffcheck PASS，非日Gate。

### [21605 Trading Depth for Time in Recurrent Transformers](https://arxiv.org/html/2609.21605v1)

2 + 1 + 2 = 5；具体owner差额/保护深入。必要exact-v1：continuous thought appended position方法、parallel-training/sequential-decode与compute反例。训练可以并行 refinement，decode 却按这些连续位置顺序展开，二者的依赖图和实际成本不能互换。block application 数不等 FLOPs、KV 占用或 latency：同 block count 的物理加深仍可更好，vanilla baseline 也未按全部训练 FLOPs 匹配；分别训练的 K 不授予推理时任意切换预算。受限结果只支持参数容量与内部计算的一个取舍。串行等待、cache 增长或质量回退时，固定深层、原共享 loop 或可审查的显式 CoT 仍合理，不能把 continuous thought 写成免费计算。

最终整合：MODEL-TRANSFORMER-LAYER Ch17:501/503；采用命题仅continuous thought追加位置/KV与same-position recurrence是不同计算/状态预算。root独立必要source→fresh owner/pre及真实两段/邻接写后PASS，uniqueSF、旧binding/全部直接反例/fallback保留，窄锁释放；未复现或签生产保证，scoped diffcheck PASS，非日Gate。

### [21619 Calibrating Teacher--Student Discrepancy for On-Policy Distillation](https://arxiv.org/html/2609.21619v1)

2 + 1 + 2 = 5；具体owner差额/保护深入。必要exact-v1：§2–4 Eq1–11/T1–3、A2/A6/A8/A9 T12–13。这个区间来自有限 prompts，不是统计覆盖保证、token correctness verifier 或知识/风格的可识别分解；放宽系数和 probe 内容会过滤有用信号，reference-solution probe 在受限结果中甚至低于初始 student。两组 Qwen 数学训练的平均收益与全局优势缩放、同稀疏度随机 mask 对照提供局部支持，但强 TSD 阈值对照已接近该结果，未披露跨训练 seed 不确定性，不能据此签发“只学能力”的因果结论。每 token 两次额外 teacher 评分并非免费：同硬件计时只在较小 teacher pair 更快，30B teacher 两种 student 反而更慢，长度变化也参与总成本。probe 不可信、保留量过小或端到端预算不合算时，保留普通 OPD、已验证的其他选择性监督或不更新；正确性仍由独立 outcome/holdout 验收。

最终整合：TRAIN-GRPO Ch33:1026/1028；采用命题仅有限teacher prompt干预区间与student超区间差额监督。sep22_resume_v3独立必要source→fresh owner/pre及真实两段/邻接写后PASS，uniqueSF、旧binding/全部直接反例/fallback保留，窄锁释放；未复现或签生产保证，scoped diffcheck PASS，非日Gate。

### [21650 SynthDemo-RL: Breaking the Zero-Reward Barrier in VLA Adaptation with LLM-Guided Synthetic Demonstrations](https://arxiv.org/html/2609.21650v1)

2 + 1 + 2 = 5；具体owner差额/保护深入。必要exact-v1：III–IV Tables/provenance及V真实路径。这种覆盖来自额外 ground-truth pose/depth/segmentation、LLM 失败后调参、轨迹筛选与 SFT；fixed PPO compute 不是整个 pipeline 等预算。SynthDemo-RL 的 57 个 perturbed LIBERO-PRO 任务中，直接 PPO 在所给预算下救回原先未观察成功的 27 项中的 10 项，synthetic SFT 则三 seed 都取得每任务至少一次成功；coverage 仍随 50 次 trial 和成功次数门槛变化，初始化覆盖与最终收益的相关性没有隔离难度与整套介入。SFT 会降低部分原已解任务，RoboTwin 的 place_cup 又未获 RL 增益；人化 teacher 运动并未消除 SFT gap。Teacher synthesis 和 PPO 都依赖目标仿真，真实 closed-loop 初试失败后，四条件各 20 次 open-loop 只证明匹配初态的轨迹可执行，不证明闭环迁移或安全。无可靠仿真/成功支持时保留人工示教、离线数据或保守策略，并分别验收数据成本、target coverage、训练回归与真实闭环。

最终整合：MULTIMODAL-EMBODIED-VLA Ch26:232/234；采用命题仅privileged成功示范覆盖作为RL初始化不同于teacher在线正则。sep22_resume_v3独立必要source→fresh owner/pre及真实两段/邻接写后PASS，uniqueSF、旧binding/全部直接反例/fallback保留，窄锁释放；未复现或签生产保证，scoped diffcheck PASS，非日Gate。

### [21677 GUARD: Natural Forgetting in Large Reasoning Models via Guided Answer-Reasoning Distillation](https://arxiv.org/html/2609.21677v1)

2 + 2 + 2 = 6；具体owner差额/保护深入。必要exact-v1：§3–5/T1–6/A1–3/B1/C1–4。改写审核、checkpoint 选择和蒸馏都付出额外离线成本，top-k 重新归一的 forward KL 也不等于完整词表行为不变。有限 R-TOFU/STAR 与两种 distilled LRM 中，分块/完整 safe-exit 对照支持联合约束 reasoning 与答案，但改写审计仍有残余披露和幻觉，改写、选点与主要质量 judge 复用了同类模型；小规模人审与跨 judge 一致只校准对应输出切片。攻击改写、jailbreak、多轮后仍有残余泄漏，retained reasoning 切片也会退化，其他方法在部分 forgetting 指标更强，不能称全面占优或永久删除。应分别测 reasoning/answer 披露、结构质量、unsupported substitutes 与 retained utility；NFRS/格式 gate 不替代内容恢复攻击，域外或证据不足时保留访问限制、独立再测或重训，不用连贯拒答签发 erasure。

最终整合：PLATFORM-SECURITY Ch72:2456/2458；采用命题仅non-disclosing reasoning/boundary safe-exit行为替代不是知识擦除证书。sep22_resume_v3独立必要source→fresh owner/pre及真实两段/邻接写后PASS，uniqueSF、旧binding/全部直接反例/fallback保留，窄锁释放；未复现或签生产保证，scoped diffcheck PASS，非日Gate。

### [21686 CIPL: A Channel-Aware Framework for Recoverable Privacy Leakage in LLM Agents](https://arxiv.org/html/2609.21686v1)

2 + 2 + 2 = 6；具体owner差额/保护深入。必要exact-v1：§3–6 Eq1–6/Prop2/T2–4、C4(T-C7)、E1–3。Canonical exact matching 阴性也可能只是未恢复完整 unit，而可用敏感值已出现；补充盲化于 provider/attack 标签的 reference–visible-output 人审，区分无恢复、部分有用与操作等价的完整恢复，但 semantic layer 只有在确实包含 exact recovered set 时才有集合支配关系，不能凭名称给普遍 recall 保证。作者五 provider、有限查询与分层 200 输出审计支持该局部盲区，不代表所有流量的泄漏频率；naive dump 在 RAG 上可超过主 recipe，provider/表面/检索设置也会改变排序。完整事件定义要求 U 非空，而公开 CER 汇总式省了该 guard，不能据此宣称空选择 trial 实现已正确；工程验收应另核 empty-selection/extractor 行为并保留 Unknown，而非补造作者修复。审计增加敏感 trace、标注与组合攻击成本，不能转换成 DP、自然发生风险或部署安全证书；边界不可校准时缩可见通道、访问范围或不发布，并在相同 observation contract 下重测。

最终整合：PLATFORM-SECURITY Ch72:321/323；采用命题仅selected units与observer recoverability、any/full/unique泄漏分母分账。sep22_resume_v3独立必要source→fresh owner/pre及真实两段/邻接写后PASS，uniqueSF、旧binding/全部直接反例/fallback保留，窄锁释放；未复现或签生产保证，scoped diffcheck PASS，非日Gate。


## 2026-10-01 作者有限提案 21888 / 21899（普通待采用）

### 21888 — Detecting Pretraining Data in Large Language Models from a Free-Energy Perspective

2 + 1 + 2 = 5，实际长期gap拟受影响深入；PLATFORM-SECURITY。拟seam：Ch72 MembershipSignal原10830两段末→Transformation family之前（当前下一内容须fresh定位）。作者已实际读精确v1必要范围§3/§4.1–4.4 Th1–2/§5.1–5.4/§6、AppA/B必要全证明、D2/E1与H少量明确反侧。C=L−λH。Th1 random iid train/member-vs-fresh模型、interiorpopulation optimum/经验smooth/global近opt与EΔH=0才保positiveexpectedgap；不是LLMoptimizer已有保证。Th2 fixedλ、VarΔH>0/CovΔLΔH>0时0<λ<2Cov/Var减少Var，λ*=Cov/Var；lowerVar不自动AUROC/TPR普遍更好。ETD实际FOS firstoccurrence token aggregation不自动继承全position理论。D2 fixedλ.5未fitlabels、无eval cutoff拟合；§5.3用eval-label回顾估moment不是已部署calibration。时间split Wiki/Stack域混杂，MIMIR同Piletrain/test较严；H Table10 WikipediaPythia12B ETD59.0低MinK++60.3；DMmath各规模ETD60.7–63不及PPL67.2–67.3。E1 GPTNeo1.3B56train55heldout/16epochs112updates/fixedseed+10000bootstrap仅controlled exposure，灰盒logits/access必要、HWdtype/runtimeND。actual低loss identifiability与control已有，不含entropy controlvariate的条件边界；拟窄I不是freeenergy物理机制/全detectorE。 未获锁/未Books/未formal，普通待采用。

拟≤2段literal：

低 loss 的可识别性审计之外，membership sensor 还可用相关的预测 entropy 调整分数，而不把 entropy 单独当成员证据。固定文本和模型读取，令分数为 loss 减去 λ 倍 entropy；若 member–nonmember entropy gap 的均值为零，且 loss gap 与 entropy gap 的协方差为正，适当正 λ 可保持平均 gap 并减少 gap 方差。它是有条件的 nuisance correction：零均值、协方差、同一 token 聚合与 attacker access 必须分别成立，不能从‘减掉 entropy’推定训练暴露已可识别。

理论的随机训练、平滑/近最优及 population 条件不是实际 LLM 的优化证书；方差降低也不保证任意 score distribution 的 AUROC 或低 FPR recovery 改善。实际 first-occurrence token 聚合、固定 λ 与时间/同来源对照仍要单独验证，受限 MIMIR 的部分来源/规模不如普通 loss 或其他基线，受控继续训练只说明对应 exposure 切片。额外 logits、entropy 读取和 corpus/control 校准付费，不是有语料身份的合规 verdict；条件不可核、模型/语料变更或信号失准时，保留原始 loss、matched controls、provenance/canary 与 Unknown，而不由一个较高总体 AUC 断言某文本进入过训练集。 [必要机制与反证](https://arxiv.org/html/2609.21888v1)。<!-- 拟source-family:SF-2026-ARXIV-2609-21888；非actual写入 -->

### 21899 — ExpBoN: Exponential-Noise Best-of-n for Efficient Test-Time LLM Alignment

2 + 1 + 2 = 5，实际长期gap拟受影响深入；MODEL-SAMPLING。拟seam：Ch20 ParallelSampling coverage/selection两段末→query-local distribution sharpening前。作者已实际读精确v1必要范围§2/§3.1 Th3.1–3.2/§4 Alg1 Th4.1/§5.1–5.2/§6、7.1 Lemma7.1及Th3.1proof、7.5Th4.1proof、7.7implementation。有限X/iidbaseP和独立Exp1 score r/λ+E、有限n law(1−ρ^n)Ptilt+ρ^nQ，ρ=1−EPexp((r−rmax)/λ)。hit>=rmax/λ条件exacttilt不是全finiteNexacttilt；random independentorder+Exp overshoot memoryless firsthit earlyexit与fullmax marginal同。Alg1 L1–14ONLY采样定理，L15–20GSI rewardthreshold gate/fallback不在同lawproof。GSIclippedimportanceβr+min(d,C)改变原target，finiteTV残差+τC非n→∞消掉clipbias，πB≪πS support。C95pct.45 from60cal64candidate不是unclippedratio upperbound，但是clippedscorevalidceiling；alln候选先生成earlyexit省PRM/baseevaluation不省draftgeneration。2A10040 vs1A10080/QwenMath1.5/7B与Qwen3 1.7/14B，PRM7B/thinkingdisabled，400MATH排cal/400MMLUSTEM/272Minerva3vs2seeds；estimated2Ntokens含fallback/refetch/PRM不同wallclock PERSTEP不init，n16~18%wallclock vs39%compute不能45%都speed。vLLM.24cachecoldrefetch计预算但未核code/生产SLO。actualparallel coverage/selection有，不含finitecandidate stochasticlaw与noisy-hit条件授权earlyexit，拟窄I不 wholeGSI。 未获锁/未Books/未formal，普通待采用。

拟≤2段literal：

候选 selection 还可以明确选择后的分布，而不只报告较高 reward。对有限 response support 上独立采自同一 base 的 n 个候选，在每个 reward/λ 上加独立 exponential noise 后取最大，得到的是目标 reward-tilted 分布与残余分布的有限-n mixture；n 有限时不能直接叫精确 tilted sampling。若 noisy score 越过真实 reward 上界导出的阈值，则 hit 分支恰好具有 tilted law；按独立随机顺序扫描并取第一个 hit，可利用 exponential overshoot 的 memorylessness 提前结束评分，无 hit 时仍需完成候选评分与选择。

这些权限依赖有限 support、独立样本/噪声、真实 score 上界与固定评分规则，不是任意 judge threshold 的提前停止保证。加入截断的 draft–target likelihood ratio 会改变目标，更多候选只能缩小有限-n误差，不能消掉 clipping bias；另加 reward gate 或 base fallback 也不自动继承前面的 sampling law。候选若已全部预生成，提前退出省的是 target/reward 评分而非这些生成；受限实验的 token-compute估计与每步墙钟也有不同分母。support、上界或成本不可靠时保留完整候选评价、标准 BoN/target sampling，正确性仍由独立 verifier 验收，不用分布定理证明所有任务质量或免费提速。 [必要机制与反证](https://arxiv.org/html/2609.21899v1)。<!-- 拟source-family:SF-2026-ARXIV-2609-21899；非actual写入 -->

## 2026-10-01 正式134：本次十四项实际终处置

### [21740 Sandwich-Residuals: Parameter-Efficient Test-time Adaptation of World Models](https://arxiv.org/html/2609.21740v1)

2 + 1 + 2 = 5；真实owner缺口深入。必要exact-v1：frozen JEPA四接口residual/最近五步one-step及Red-Density/Cube反例。采用仅冻结JEPA接口的residual适配与校正表示目标分账。

更换整个 transition model 的代价高时，也可在冻结的 JEPA 接口前后加入小 residual adapters，保留原编码与预测路径。一个 test-time 分支用最近五步经验作 one-step 适配，以经当前 encoder 校正后、stop-gradient 的目标表示监督预测；这个目标不是 raw physical truth。冻结参数不截断对输入/adapter 的梯度，planner、预测器和真实观测仍有不同身份；episode 切换时重置适配状态，并保留所假定的稳定 proprioceptive 接口，不能跨任务静默继承残余。

局部残余把更新限制在较少参数，却仍支付梯度、缓存、适配与规划成本，参数高效不等总 compute 更低。受限 Sandwich-Residuals 结果中，Red-Density 与 Cube 仍有反例，不支持任意变化都可由这组接口吸收或通用稳定闭环。表征目标可能随 adapter 移动，one-step 改善也不证明长 horizon 校准。观测身份、身体状态或适配质量失配时，应回到冻结基座、更短预测与真实观测，而不是以较小更新签发物理模型正确性。

最终整合：MULTIMODAL-WORLD-MODELS Ch25:274/276。root独立必要source→fresh owner/PRE与真实两段/邻接POST PASS；旧机制/全部关键反证保留、SF唯一、锁释放。局部实验不作全域或生产保证。非全日日Gate。

### [21748 World Modeling in Transformers](https://arxiv.org/html/2609.21748v1)

2 + 1 + 2 = 5；真实owner缺口深入。必要exact-v1：map probe/causal teleport/localization/legal move/goal compass及Taxi深远OOD。采用仅地图可解码、定位、局部合法与目标方向需分别验收。

采样出的动作不稳定，也不能单独证明模型没有地图。诊断至少分开 map 是否可解码、地图信息是否通过干预改变行为、当前 localization、合法移动与 goal direction。一个受限 Transformer 研究用 causal teleport 与连续位置干预拆这些对象，再将 affordance packing 约束局部合法性；packing 不能补齐位置真值或目标 compass。好地图被读出、模型知道自己在哪、并能持续按图行动，是不同成立条件。

有限 Taxi 分布外实验在更深更远位置、包括未训练位置 99 上暴露这些分离，连续正确位置输入只用于诊断，不是已部署传感器。模型大小与 map 可读性、采样行为之间的局部差异不形成“小模型普遍更好”的结论；受限 probe 与干预也不证明所有环境拥有同一坐标。位置/地图审计、行为干预与约束编码付费，localization 不可信时应回真实观测、显式地图和合法 action gate，不用可解码的 latent 自动认证导航。

最终整合：MULTIMODAL-WORLD-MODELS Ch25:68/70。root独立必要source→fresh owner/PRE与真实两段/邻接POST PASS；旧机制/全部关键反证保留、SF唯一、锁释放。局部实验不作全域或生产保证。非全日日Gate。

### [21787 Compact but Moving: Intervention-Relevant Geometry in Recurrent World Models](https://arxiv.org/html/2609.21787v1)

2 + 1 + 2 = 5；真实owner缺口深入。必要exact-v1：§5及A9–A14 factual Jacobian chain/moving image、GRU rank4/LSTM rank6与全幅反例。采用仅future-response低rank局部image不授固定closed latent。

即使只关心影响未来观测的方向，低 rank 也不等于一个固定、closed latent state。沿 factual Jacobian 链提取对 future response 有作用的局部 image，可把一次 intervention 放在这个子空间，再在后续状态重启分析；后续 factual 演化不继续注入同一 counterfactual 修正，因此相关子空间会移动。它描述局部线性干预的可达方向，不校准有限幅度响应，也不能把所有状态投进一个固定低维模型。

这种诊断增加 Jacobian、SVD、重启与未来观测成本。受限两对象 GRU 的 rank-four 结果与 LSTM 的 privileged counterfactual anchor rank-six 是不同设置；全幅干预的部分失败阻止把局部 rank 解释成任意幅度或任意 recurrent state 的缩维保证。子空间漂移、局部线性近似失效或未来响应无法核验时，应保留较完整 latent、缩小干预或回到真实观测；表示压缩、因果方向和响应大小仍需分别验收。

最终整合：MULTIMODAL-WORLD-MODELS Ch25:72/74。root独立必要source→fresh owner/PRE与真实两段/邻接POST PASS；旧机制/全部关键反证保留、SF唯一、锁释放。局部实验不作全域或生产保证。非全日日Gate。

### [21793 CASCADE Against Jailbreaks: Combination Across Stages with Controlled Attack-Defense Evaluation](https://arxiv.org/html/2609.21793v1)

2 + 2 + 2 = 6；真实owner缺口深入。必要exact-v1：rewrite/filter顺序、utility top-k筛选攻击、matched population与资源边界。采用仅串行rewrite不交换、组合子集比较不认证全局Pareto。

单个 safeguard 的验收也不能直接继承给其组合。对输入先 rewrite 再 filter，与先 filter 再 rewrite 可能产生不同的候选和拒答；这不是 OR-combined guards 的并列语义。一个受限组合评价分支先按 utility 选择 top-k 配置，再在这些配置上开展攻击，明确保存处理次序、模型版本和共同输入，使性能比较不被流程差异掩盖。它只比较入选子集，不认证全配置空间的 Pareto 最优或通用组合收益。

ASR 与 utility 若来自不同模型人口，就不能拼成一个质量—安全点；少数 modern model 的 matched 回归也只支持局部结论。Parameter count 只是资源 proxy，不是 VRAM，H100 平均时间不是 tail SLO，单轮攻击不覆盖 adaptive、多轮或全部威胁。组合新增 rewrite、guard、校准与攻击成本，某些处理次序还会降低 utility 或扩大攻击面。规则稳定、风险隔离时成熟单 guard 仍是较清楚的低成本分支；跨域或组合退化时缩回已验收路径，并保留确定性 enforcement。

最终整合：PLATFORM-SECURITY Ch72:551/553。root独立必要source→fresh owner/PRE与真实两段/邻接POST PASS；旧机制/全部关键反证保留、SF唯一、锁释放。局部实验不作全域或生产保证。非全日日Gate。

### [21942 When Should a Failing Robot Ask? Initiating Corrective Human-Robot Dialogue from Audited Sensor Evidence](https://arxiv.org/html/2609.21942v1)

2 + 1 + 2 = 5；真实owner缺口深入。必要exact-v1：III–VII/A/C/F、sensor shuffle/held-out、25校准与35–36测试及改措辞反例。采用仅观测可诊断性、model可利用性与人的答复权限分层。

失败时是否询问人，不应直接由最终 failure label 或模型自报 confidence 决定。先按 failure family 审计哪些当前传感器真的提供诊断信息：固定已知注入原因，隔开 simulation runs，以 label shuffle、未见视角/外观及严重度迁移检查 classifier 是否走了捷径；高准确率只展示该观测里有可用信号，低平台不证明任何模型都无法恢复。再在独立 calibration failures 测当前 model 的诊断准确率，连同正确/错误 repair、读取自有 sensor 与打断人的代价比较 act、sense、ask。可诊断性属于观测，能否利用属于该模型；人答复的可靠性与理解能力又是第三层，不得用最强 sensor classifier 的准确率替 model 决策。

这个审计和代价参考来自注入式 tabletop 仿真，部分 grasp 原因本就不被 renderer 描绘；六种受限 VLM 的选项顺序、遗漏 force telemetry 与融合退化表明，问人率不能单独当可靠自知。模型可从 telemetry 受益但仍远低于 classifier，且一条 token-logprob 通道有局部选择价值，不能推广为所有 confidence 必然无用。校准仅 25、test 35–36 episodes/family，成本是指定单位、oracle 只作离线参照；脚本人答复不随问句变化，换非菜单措辞后部分 model 收益大跌，未验证真实多轮对话或物理恢复。额外 sensor 读取、审计与校准付费，model/环境/成本改变须重测；无法判断或状态已危险时先停到可信 safety checkpoint，再使用显式人工/保守流程，不让统计最优参考授予安全执行。

最终整合：MULTIMODAL-EMBODIED-VLA Ch26:811/813。sep22_resume_v3独立必要source→fresh owner/PRE与真实两段/邻接POST PASS；旧机制/全部关键反证保留、SF唯一、锁释放。局部实验不作全域或生产保证。非全日日Gate。

### [21948 GALA: Geometry-Aware Latent Action Modeling for Vision-Language-Action Model Pretraining across Embodiments](https://arxiv.org/html/2609.21948v1)

2 + 2 + 2 = 6；真实owner缺口深入。必要exact-v1：III–V Eq1–13/TI–V及官方appendix A–F必要三页。采用仅共享bimanual几何transition监督与native action head分权。

两帧 RGB 的 latent action 可以保留场景位移，却未必保留细指 articulation；直接把异构点云并入码本，又可能把 morphology 和坐标当动作语义。一条训练侧分支将 human 重建手形与 robot kinematics 产生的 end-effector 点云转为有有效性标记的局部几何，联合编码两手 start–goal transition，并让同一 geometric code 结合各手初始几何重建其后继；对成对端点施加一致几何扰动，forward/backward 共用 encoder/codebook/decoder，但不强加两方向 code 为互逆。视觉码保留 scene dynamics，几何码提供 articulation 监督，冻结 tokenizer 后由 bridge targets 塑形 VLM。下游共享 action expert 仍通过 embodiment-specific head 输出各自原生 action space，human 派生状态也不是 robot 控制命令，共享码本不能代替动作 schema 和 controller 验收。

手部重建、URDF/MJCF 状态转换、pair normalization、validity 与双流训练增加成本，也会继承几何误差或丢失任务证据；motion probe 和三类跨 embodiment retrieval 只检验局部可读信息，不证明 universal action semantics。受限 GR-1-only 对照同数据/优化预算支持该分支，但 UEMR 同时移除三个设计，不能隔离唯一收益；多 embodiment 训练又同时增加 batch 与步数，不能把对 GR-1-only 的增益全归因于数据可迁移性。四项 XHand 真机各 50 次只支持所测闭环，部分 baseline 还读不同相机且 backbone 不同，平均领先不代表全面优越或物理安全；附录对 Stage-2 监督 token 数的正文/表口径不一致，不继承精确该配置为已验证实现。几何/坐标失配、码语义不稳或预算不足时保留 RGB latent、显式原生 action labels 或独立 embodiment policy，重新做动作闭环与回归，而不是以重建/retrieval 分数授权执行。

最终整合：MULTIMODAL-EMBODIED-VLA Ch26:200/202。sep22_resume_v3独立必要source→fresh owner/PRE与真实两段/邻接POST PASS；旧机制/全部关键反证保留、SF唯一、锁释放。局部实验不作全域或生产保证。非全日日Gate。

### [21888 Detecting Pretraining Data in Large Language Models from a Free-Energy Perspective](https://arxiv.org/html/2609.21888v1)

2 + 1 + 2 = 5；真实owner缺口深入。必要exact-v1：§3/§4.1–4.4 Th1–2/§5.1–5.4/§6、AppA/B必要全证明、D2/E1与H少量明确反侧。采用仅loss–entropy条件control-variate而非membership裁决。

低 loss 的可识别性审计之外，membership sensor 还可用相关的预测 entropy 调整分数，而不把 entropy 单独当成员证据。固定文本和模型读取，令分数为 loss 减去 λ 倍 entropy；若 member–nonmember entropy gap 的均值为零，且 loss gap 与 entropy gap 的协方差为正，适当正 λ 可保持平均 gap 并减少 gap 方差。它是有条件的 nuisance correction：零均值、协方差、同一 token 聚合与 attacker access 必须分别成立，不能从‘减掉 entropy’推定训练暴露已可识别。

理论的随机训练、平滑/近最优及 population 条件不是实际 LLM 的优化证书；方差降低也不保证任意 score distribution 的 AUROC 或低 FPR recovery 改善。实际 first-occurrence token 聚合、固定 λ 与时间/同来源对照仍要单独验证，受限 MIMIR 的部分来源/规模不如普通 loss 或其他基线，受控继续训练只说明对应 exposure 切片。额外 logits、entropy 读取和 corpus/control 校准付费，不是有语料身份的合规 verdict；条件不可核、模型/语料变更或信号失准时，保留原始 loss、matched controls、provenance/canary 与 Unknown，而不由一个较高总体 AUC 断言某文本进入过训练集。

最终整合：PLATFORM-SECURITY Ch72:250/252。root独立必要source→fresh owner/PRE与真实两段/邻接POST PASS；旧机制/全部关键反证保留、SF唯一、锁释放。局部实验不作全域或生产保证。非全日日Gate。

### [21899 ExpBoN: Exponential-Noise Best-of-n for Efficient Test-Time LLM Alignment](https://arxiv.org/html/2609.21899v1)

2 + 1 + 2 = 5；真实owner缺口深入。必要exact-v1：§2/§3.1 Th3.1–3.2/§4 Alg1 Th4.1/§5.1–5.2/§6、7.1 Lemma7.1及Th3.1proof、7.5Th4.1proof、7.7implementation。采用仅finite-n mixture与conditional hit授权提前停止评分。

候选 selection 还可以明确选择后的分布，而不只报告较高 reward。对有限 response support 上独立采自同一 base 的 n 个候选，在每个 reward/λ 上加独立 exponential noise 后取最大，得到的是目标 reward-tilted 分布与残余分布的有限-n mixture；n 有限时不能直接叫精确 tilted sampling。若 noisy score 越过真实 reward 上界导出的阈值，则 hit 分支恰好具有 tilted law；按独立随机顺序扫描并取第一个 hit，可利用 exponential overshoot 的 memorylessness 提前结束评分，无 hit 时仍需完成候选评分与选择。

这些权限依赖有限 support、独立样本/噪声、真实 score 上界与固定评分规则，不是任意 judge threshold 的提前停止保证。加入截断的 draft–target likelihood ratio 会改变目标，更多候选只能缩小有限-n误差，不能消掉 clipping bias；另加 reward gate 或 base fallback 也不自动继承前面的 sampling law。候选若已全部预生成，提前退出省的是 target/reward 评分而非这些生成；受限实验的 token-compute估计与每步墙钟也有不同分母。support、上界或成本不可靠时保留完整候选评价、标准 BoN/target sampling，正确性仍由独立 verifier 验收，不用分布定理证明所有任务质量或免费提速。

最终整合：MODEL-SAMPLING Ch20:310/312。root独立必要source→fresh owner/PRE与真实两段/邻接POST PASS；旧机制/全部关键反证保留、SF唯一、锁释放。局部实验不作全域或生产保证。非全日日Gate。

### [21941 End-to-End Hard-Label Cryptanalytic Model Extraction Using Efficient Sign Recovery](https://arxiv.org/html/2609.21941v1)

2 + 2 + 2 = 6；真实owner缺口深入。必要exact-v1：§2–3.7/Prop1/Alg1/T2、§4.1–4.3/T3。采用仅已恢复局部map与competitor signature下分离hard-label sign。

只返回 class label 缩小了输出面，却不自动消除模型结构泄漏。在已知架构、可自适应查询任意输入的 fully-connected ReLU 威胁模型中，decision boundary 与 activation boundary 的交会仍提供局部几何证据；一个分支复用已收集的交会点及两侧 normal，用已恢复前层的局部线性 map 和竞争神经元的 signature 区分目标的 on/off side，进而恢复 sign。投影判断需要活动竞争项被覆盖、span/rank 与非零系数等条件，替代 cosine 估计另依赖分布假设；这是特定表示的恢复机制，不是任何 hard-label API 都能被同样重建。查询预算须分别记取点、signature、sign 与纠错，不能把 sign 阶段复用数据的零新增查询记成整个 extraction 免费。

前层误差、未恢复项、不可达权重和伪 signature 会传播；按 normal-span violations 迭代修正只是有限数值程序，不能升级为完整参数精确恢复。受限 MNIST/Fashion-MNIST 的宽16、4/6隐藏层实验先支付数十亿至数百亿取点查询，仍排除 dead/almost-dead neurons，persistent 分支未测；高 agreement 来自指定 standard-Gaussian 输入，不证明全输入、自然数据或大型语言模型等价。Hard labels 本也不能唯一识别共同 logit 平移/缩放，故参数精度与指定分布上的行为 fidelity 要分开。防护继续在实际接口、输入能力与全阶段跨身份预算上验收，保留 access control、受限输出与人工调查，不因局部恢复成功或单一查询率断言普遍可盗取/不可盗取。

最终整合：PLATFORM-SECURITY Ch72:2854/2856。sep22_resume_v3独立必要source→fresh owner/PRE与真实两段/邻接POST PASS；旧机制/全部关键反证保留、SF唯一、锁释放。局部实验不作全域或生产保证。非全日日Gate。

### [21960 Schedule optimization for tau-leaping in masked discrete diffusion](https://arxiv.org/html/2609.21960v1)

2 + 1 + 2 = 5；真实owner缺口深入。必要exact-v1：Alg1–2/§2.2/§3 Cor1/§4 Th2及AppB/C必要证明/§5–6。采用仅learning与factorization KL分账及profile schedule成立条件。

并行提交还要区分 predictor 没学准与 sampler 把联合分布拆开两种误差。即使每个未知位置的条件分布都精确，同一轮在只看已提交 token 的条件下独立填多个位置，仍可能丢失块内依赖。一条受限 tau-leaping 分支按与 token 值独立的随机 ordered partition 分块，将 learning error 与平均条件 total correlation 分开；两者之和上界最终输出 KL，perfect predictor 时 factorization term 等于保留 partition 的 joint KL，不能反推它就是最终 KL 或必然的非零输出误差。依赖 profile 描述随机已揭示集合下的剩余条件相关，并给出 finite-K schedule 的精确 factorization objective，使预算优先分到相关性更强的阶段，而非仅凭 sampler 名称或每轮 token 数选步数。

最优 stationarity 不自动保证唯一解：shooting/bisection 要另有单调条件；profile 随长度一致收敛到连续严格正极限、且使用固定递增光滑 schedule 时，优化只改变 N/K 的 leading constant。特定退化的 exchangeable-mixture profile 才展示同 logarithmic 步数下不同 factorization 阶，不能转成通用 LM 质量定律；随机块大小也不等同固定逐位置计划。完整 profile 要付离线估计与优化成本，模型条件误差、有限样本及 coefficient 差分会污染它，toy exact-target 检查不是已部署语言模型或真实 latency/SLO 证据。profile、独立分块或成本条件不成立时保留原 confidence schedule、固定块或逐位置 sampler，并以实际输出质量、生成预算与墙钟独立验收。

最终整合：MULTIMODAL-GENERATIVE-PARADIGMS Ch24:238/240。sep22_resume_v3独立必要source→fresh owner/PRE与真实两段/邻接POST PASS；旧机制/全部关键反证保留、SF唯一、锁释放。局部实验不作全域或生产保证。非全日日Gate。

### [22005 Abstention and Noise Filtering: Two Missing Primitives of Softmax Attention](https://arxiv.org/html/2609.22005v1)

2 + 1 + 2 = 5；真实owner缺口深入。必要exact-v1：query零option/valuegate机制及FineWebEdu/projection attack反例。采用仅abstention与noise filtering算子尺度/失效不同。

允许 no-op 之外，Attention 还须区分没有支持证据与存在低质量证据。一个条件分支给 query 增加显式零输出 option，让它可以不把全部质量分给输入；另一条分支按 value 的特征选择性抑制噪声。前者的零 option 可形成精确 abstention，但把 value gate 当作 routing 再归一化会丢失原来的总质量 Z，不能直接视为同一个聚合算子。Query 选择与 value 过滤拥有不同职责，也不由两者名称推出完整输入已经被忽略。

更强过滤会损失有用证据：受限 FineWeb-Edu 模型中的 norm gate 在较多 junk 时反而退步，投影对齐的攻击又可绕过特征过滤。模型规模、训练切片与有限 seed 不认证任意 pretrained Transformer，未测吞吐也不支持更高生产效率。零 option、特征门与旧 null/sink 都应按相同任务、预算及可观察输出验收，并计新增参数、校准和 kernel 成本；判断失准时保留成熟 softmax、显式 null 与外部输入检查，不能用一个 gate 自签鲁棒性。

最终整合：MODEL-SELF-ATTENTION Ch14:260/262。root独立必要source→fresh owner/PRE与真实两段/邻接POST PASS；旧机制/全部关键反证保留、SF唯一、锁释放。局部实验不作全域或生产保证。非全日日Gate。

### [22041 $λ$-Controlled GRPO: Turning Flow-Matching Ratio Instability into a Budgeted Resource](https://arxiv.org/html/2609.22041v1)

2 + 2 + 2 = 6；真实owner缺口深入。必要exact-v1：Gaussian ratio/mean reduction、LambdaNormT/detached λ/ESS及GenEval反例。采用仅真实条件律ratio与训练budget surrogate分账。

限制 replay 年龄仍未控制 ratio 的数值尺度。在同一可逆 Gaussian 转移族、同条件和 drift 身份下，可比较 current/old 条件律；但对 D 维项作 mean reduction 不是原始 likelihood ratio，不能悄悄继承它的概率解释。一条受限训练分支用时间相关的 LambdaNorm surrogate，把 detached λ 作为只衰减的预算控制量，限制过大更新信号。它改变的是训练中的 proxy 尺度与阻尼规则，而不是证明旧轨迹已满足当前 trust region。

选择 λ、校准 surrogate 与监测 ESS 增加成本；启发式有效样本量不认证 support、无偏或训练安全。作者 single-seed pilot 与 GenEval 退步的反例只支持局部稳定性/质量取舍，不能将 ratio 数值更温和写成所有任务更优。应分别保留真正条件律、归一化 convention、阻尼前后信号及总采样/更新成本；失配、质量下降或 proxy 无法校准时，缩短 replay、增加当前采样或回退已验收目标，不让预算参数替代独立 outcome 验收。

最终整合：TRAIN-GRPO Ch33:1224/1226。root独立必要source→fresh owner/PRE与真实两段/邻接POST PASS；旧机制/全部关键反证保留、SF唯一、锁释放。局部实验不作全域或生产保证。非全日日Gate。

### [22048 Available Guardrails: Certifying Selective Prediction across ML Systems](https://arxiv.org/html/2609.22048v1)

2 + 1 + 2 = 5；真实owner缺口深入。必要exact-v1：独立IIDcert与固定ordering连续partition DP及held-out选择收益。采用仅certificate validity与finite-data availability不同。

独立认证还要区分证书若获得时的 validity，与有限数据预算下能够获得证书的概率。先冻结 predictor、分组、threshold 与 score，再在独立 IID certification 数据上验收；候选规划端可按预期 support 配置选择性 prediction，但不能反过来修改认证端观察到的结果。一个受限 DP planner 只在固定 group ordering 的连续分块及 rounded expected support 上求解，不能据此宣称任意语义分组的全局最优；具有不同语义或风险责任的组也不能为了通过率任意合并。

规划、选点与独立 certification 各付数据成本。受限 held-out 改善主要来自 selection，不证明结构化 family 本身普遍更强；较高取得证书的机会也不降低证书原来绑定的分布、预测器与条件。部署 shift、分组或阈值变化后，旧证书不能直接复用，应取得 fresh labels、重新认证或 abstain。数据不足时保留简单固定 groups、人工升级与明确未认证，而不是以 planner 的 expected support 代替实际风险证据。

最终整合：PLATFORM-EVALUATION-SYSTEM Ch66:3009/3011。root独立必要source→fresh owner/PRE与真实两段/邻接POST PASS；旧机制/全部关键反证保留、SF唯一、锁释放。局部实验不作全域或生产保证。非全日日Gate。

### [22056 Predictable Failure in Multi-Hop Retrieval: Score-Distributional Confidence Scoring and Abstention](https://arxiv.org/html/2609.22056v1)

2 + 1 + 2 = 5；真实owner缺口深入。必要exact-v1：top5gold support/ANNfeatures、§5.3CWAR/§8Bayesbest争议与MuSiQue校准。采用仅support completeness与answer正确分权/CWAR争议不采用。

联合 threshold 之外，还可先问当前 retrieval 是否提供完整证据，而不是直接预测答案正确。一个受限 multi-hop 分支将 top-5 是否包含完整 gold support 作为训练 target，用九项 ANN score-distribution features 和 query length 建立较便宜的 confidence gate；再按 retrieval regime 检查 feature 的有效性。它只决定继续检索、交给 answerer 或 abstain 的 proposal，不让 support label 取得 answer correctness 或 source truth 的权限，换 corpus、retriever 与 hop 结构须重验。

Logistic 输出并不天然 calibrated，有限 MuSiQue 上的 MLP、tie 与 ECE 对照也不是所有 query 的风险证书。不能采用‘经验 CWAR 必随 threshold 单调’、空选择集合默认风险零，或将 Bayes 最佳规则的结论直接授予训练得到的 scorer；这些断言不由局部 feature 效果补齐。标注完整 support、校准 gate 与维护 regime 增加成本，需并报 coverage、support completeness、answer quality 与实际 retrieval/生成预算。目标或校准不可信、域移或 evidence 不全时，回退扩大检索、独立 verifier、已有联合校准/abstention，而不由廉价分数签发安全回答。

最终整合：AGENT-RAG Ch76:544/546。root独立必要source→fresh owner/PRE与真实两段/邻接POST PASS；旧机制/全部关键反证保留、SF唯一、锁释放。局部实验不作全域或生产保证。非全日日Gate。

## 2026-10-01 最后作者两项必要source→actual提案（未写/待独立采用）

### [21827 RheoSampling: Resolving the One-Hot Dilemma in Stochastic Dynamic-Tree Speculative Decoding](https://arxiv.org/html/2609.21827v1)

2 + 2 + 2 = 6，真实知识差额深入；必要源停止：§3.1–3.3/Alg1、§4 Th1/3、§5.1–5.4/Table2/AppendB sparse支持与C1–4全部关键losslessness/slot proof。

m≥1 proxy=min(q_m,z)≥q_(m+1)、constant in Y但是constant alone不足；sample-before-fill固定第m+1slot；global score产品/shallower→left tie祖先闭合，C4固定保留父/前k equivalence→新slot决定性，后sampletail不变。Verification 用actual tempered tail不是treeproxy；min1p/qtilde及positive residual，samplepruned则target补足。m0正文q1+epsilon vs C3 z=1身份不一致且epsilon未给≤1，不采用其普遍祖先monotone/全m保证。3targets6tasks各80题，A6000/EAGLE3原checkpoint/noFT/tree60depth8/3seedsT1，Llama τ5.04→5.25 vs速度2.84→2.93不同分母；m1局部最好/低T优势收窄/m≥3stochasticpruned；Top128仅91.0%massFull100%，4.84vs4.89AAT/Full18.8msPyTorchnative未优化，不完整QoS。HWprecision未披露precision，不补。actual22098 only generalpre-draw/无放回与selectionbias，没有proxy与realproposal dualrole必要rankingbound，窄gap支持I拟两段。不采用OT approximate‘almostalways’为普遍优势，无code复现。

实际INFER-SPECULATIVE-DECODING Ch48，窄插点：22098旧树合同两段末→37532 shape binding前；拟I未授锁未写，不自签。

拟两段：

树形选择并非只能在确定性 top-k 与完全随机扩展之间二选一。一个受限混合分支先保留 top-m，再从归一化 tail 抽一个 token，最后补不重复的高概率候选；供树排序的 proxy 与用于 target 验证的真实 proposal 必须分开。对 m≥1，取 proxy=min(q_m,tail mass)，既不依赖抽到的身份，又不小于最高 fill 概率，使 sampled slot 固定在 fill 前。按 path proxy 裁树还须保持祖先闭合与明确 tie order；单说 proxy 与 token 独立不够，低于 fill 的 proxy 仍会让是否保留取决于抽中谁。验证先按真实 tail 执行接受/正部残余，再处理确定性点，不能拿排序分数冒充抽样概率。

这条受条件构造的 lossless 论证不授予任意事后剪枝。正文 m=0 的 q_1+ε 与附录基例的 z=1 未统一，不继承该分支的全域保证；树排序用原概率、抽样/验证经温度处理时也必须保存各自身份。受限 A6000、三个 target、六项任务的三 seed 结果支持小幅 accepted-length 与速度收益，但低温下收益收窄，更多 deterministic slots 会剪掉随机探针。稀疏概率实现又牺牲 tail 覆盖，完整词表 PyTorch 对照未作同等优化；排序、采样、真实 proposal 重构与 KV commit 都有成本。边界或测量无法核实、温度/模型改变或收益不足时回到原 chain/top-k/target-only，不以理论精确性认证任务真值或生产 SLO。

### [21858 Watermarkable Multi-Draft Speculative Sampling via Poisson Processes](https://arxiv.org/html/2609.21858v1)

2 + 2 + 2 = 6，真实知识差额深入；必要源停止：§3–5/Alg1–4/Def4.3/Prop4.4/Th5.1、A4Alg6–7/ThA5–6完整有限实现proof、B1acceptance完整proof/C1.1stopping-time全proof/C2definitions、§6/Limitations与D1、D5(T14–15)必要population/计时/quality。

每context keyed Poisson base过程，target P映射first arrival始终emit；Q MPFR list相同process mapped有iidQ marks可能重复，mergecontext multiplicity。targetwinner在draftset才continue，否则emitwinner后stop；原定目标law由context-independentidealExp clocks链式证明，不要求Psupport⊆draft但各对referenceμ AC。finiteKsupportAlg6 K×BExp arrivals选topB exakt iid；A6只有idealindepclocks证明PRF实keypseudorandom不真独立。Th5.1在singlecontextiidQ list acceptance下界≠totalrate/latency。sharedkey/fullcontext/randomness相同时tokenchain由target侧定义、drafter改变stoplength非content；statement仅commonpositive supportτ给conditioning，非普通PRNGseed顺序消耗自动不变。Watermarkunbiased是keys/randomness marginal非每fixedkey纯target；detector依赖key/prefix不是法律provenance/adaptive attack resistance。MainT1 caption Llama3.1 vsD1/D4正文Vicuna secondpair未统一，窄采用不拼该身份；D1 float16 singleH100 topk50topp1T1max128/1000prompts/多seeds但mean±std acrossprompts vsmain3seeds口径不要替换。D5 .990minpair notactualalloutputsbyteidentical，LPPLparity不是distributionproof。当前couplingbookkeeping slightlyslow作者承认，通信/水印/efficiency根本tradeoffunclear。No fullcode inspection/reproduction，不採每B‘breakingno-go’普遍结论。freshactual经典qratio/residual/targetlaw有，缺targetkeyedsampler独立draftstop角色及多Poissonarrival预算，拟I精确机制Ch48不复制Ch72水印审计。

实际INFER-SPECULATIVE-DECODING Ch48，窄插点：ExactAcceptance经典residual两段末→LosslessVerification heading前（与21827树接缝不重叠）；拟I未授锁未写，不自签。

拟两段：

保持 target 分布之外，带 key 的采样还需要让 drafter 只决定推进长度，不决定 watermark 可见的 token。一个条件分支按完整 context 索引共享 Poisson clocks，将同一底层过程分别映射到 target 与 draft 分布；target 的第一个 winner 始终提交，只有它也在 draft 的多候选集合内时才沿树继续，否则提交该 target token 后结束本轮。候选可重复，合并后的 context 还须保留 multiplicity。理想的跨 context 独立 clocks 下，固定 target、keyed randomness 与初始 prefix，已到达的输出链由 target 侧决定，drafter 影响 stopping time；这比用接受来源决定 key 更清楚，也不同于把一个普通随机 seed 按不同执行顺序消耗。

精确性相对于所声明的 processed target law，并以独立 clocks 和完整 context 身份为条件；key 的伪随机实现与浮点行为还需另外验收。有限 support 可为每 token 生成 B 次 arrival 再选最早 B 个，支付约 support×B 的 clocks、树验证与水印 bookkeeping；单 context 的 acceptance 下界不证明总体吞吐。Unbiased watermark 是对随机 key/source 的边缘性质，不是每个固定 key 都等同无水印输出，也不证明任意改写攻击或法律归属。受限摘要/解释任务的检测与 drafter 替换对照不认证所有模型，实际输出一致性也未达到逐字全等；论文承认耦合记账开销。支持、key/context 复现或端到端收益不成立时保留普通 rejection sampler/target-only，安全审计另按第72章的 observation contract 验收。


## 2026-10-01 原普通两项与负侧两项有限采用提案（非最终冻结）

原6负侧样本实际4误关（21953/21629/21749/21259）＋2具体关闭（21468/20873）；只恢复受影响机制。21259由peer必要源→actual Ch66:441–445窄E通过，整CogGym配方不称已有。21749 peer已完成必要source/actual/literal PRE拟I，另待锁/POST；6样本不冒称全原negative。正式134不变，原4+此4必须终处置后冻结。

### [21983 SkelWAM: A Skeleton-Guided World-Action Model for Zero-Shot Cross-Embodiment Manipulation](https://arxiv.org/html/2609.21983v1)

2 + 2 + 2 = 6；已确认实际长期差额深入。必要停止：root实际exact-v1 §III–V/TableII；作者fresh归一化/协方差→privileged3D邻接。

25D六centerline15offset/TCP3/rot6/jaw共同视觉/action；机器人视觉遮罩背景补齐同canonical空间；future仅训练；source统计/weights冻结≠target标定/decoder零工程。rigid保priorbodyintent+measuredTCP/jaw，continuum还orientation≠fullbody真值。w/oA同时w/oD混杂、wrist43.0近43.3；1k simulation/source467，真机仅3任务定性，43.3不授普遍zero-shot。HWprecision/SLO ND，无code复现。

实际MULTIMODAL-EMBODIED-VLA 21358两段及23731联合协方差段之后→Privileged 3D Teacher heading前；拟I未写，待非作者PRE/具体锁。

冻结 source policy 并不自动使异构机器人共享 action space。一个受限分支把 arm centerline、TCP pose 与 jaw 状态编码成共同的 25 维接口，并将视觉中的机器人移除、补齐背景，使 observation 与 action targets 落在同一 canonical 空间；当前观测形成条件，future geometry 只用于训练。共享模型产生的是这一几何接口的 proposal，target embodiment 的标定、kinematic decoder 和 controller 再负责将它转换成可执行命令；无 target-task 示教或权重更新，不等于没有 target 工程。它与共享手部骨架监督是不同分支，不能把某一 body layout 的先验静默当作真实观测。

受约束解码还须保留哪些身体自由度来自先验、哪些由传感器更新：rigid 分支保留 body intent 并消费 TCP/jaw，continuum 又保留 orientation，这不是完整 body state 的现场恢复。有限仿真对照中，视觉与 action canonicalization 的去除存在联合混杂，wrist 分支也接近主结果；少量真机定性任务不证明任意 embodiment 的零样本成功或安全。source 统计、几何 schema、target calibration 和 decoder revision 必须一同绑定，decoder/反馈与物理约束有独立验收成本；坐标失配、反馈不足或超出运动范围时，保留原 embodiment policy、显式 retarget、重新标定及 safety controller，不以共享表示授权执行。

### [21996 A Lie Detector Test for Language Models: Reading Knowledge a Model Won't Reveal](https://arxiv.org/html/2609.21996v1)

2 + 2 + 2 = 6；已确认实际长期差额深入。必要停止：root实际exact-v1 §3.2 Eq1–3/§4–5；作者fresh16890→运行期身份邻接。

PIRcorrect-minusdecoys，honestcorrect定义标签；部署assay需该模型basecheckpoint，referencefree≠无候选标签基准；freeform来自elicited+deployed样本，peak/divergence不同对象；steeringsufficient非necessary，necessitynegative；单seed strictrotation样本条件；anti-probe保capability让readout失效，insample保证撤回。静默不可分neverknown/removed，无永久erasure。

实际PLATFORM-SECURITY 16890三层验收两段末→运行期身份、监控与Effect Boundary heading前；拟I未写，待非作者PRE/具体锁。

三层验收还可以增加一个受条件的内部识别 assay：在模型拒绝报告答案时，用正确候选与 decoys 的表示差形成方向，再比较当前模型对这些候选的内部反应与其 base checkpoint。标签来自 honest-correct 行为，free-form 的候选仍须由 elicitation 或部署输出构造；reference-free 只是不读取外部 reference model，不代表无候选、标注或基准。该 assay 区分公开报告与有限候选的内部 recognition，peak 与 divergence 也分别记录；它不能把 probe 分数直接变成隐藏知识真值。

方向 steering 可改变输出只支持局部充分性，necessity 对照未通过，故不能称唯一 knowledge circuit。受限单 seed、严格选样的 concealment/unlearning 实验支持两者可能表现不同，但 anti-probe 更新可保留能力而使 readout 失效；静默阴性无法分辨从未学会与真正删除，已撤回的 in-sample 保证也不继承。维护 base identity、构造候选、内部读取和跨攻击评价都有成本；换模型或访问权限不足时应保留 Unknown、替代恢复攻击和独立任务评价，必要时重训或限制访问，不由 detector 阴性签发永久 erasure。

### [21629 Extending Decoupled Attention to Dense Prediction and Masked Training for Multi-Channel Images](https://arxiv.org/html/2609.21629v1)

2 + 1 + 2 = 5；已确认实际长期差额深入。必要停止：exact-v1完整摘要/§3.1–3.2 Eq1–7/§4协议/§5.2对照与mask-ratio反例。

纠正原仅microscopy/science拒收：independentmask保留后同compactindex不再同grid身份，genericattention接口实际变化。equal-k二channelHungarian squaredgridcost；多channelstarreference C−1 assignments仅starcost精确非allpairjoint；randomref平衡perchannelerror mean.87不变；row/Hilbert平均距离改善不解释质量、sharemask100%对应但失diversity，heavy.75趋同。ViTS16/RTX3090/sixlimitedtasks，precision/seed/latencyND；不复现。重要反证：原§5.2‘shared retainedpatch必自身因0distance最优’不成立：同一行A{0,2},B{2,3}，匹配0→2,2→3成本5，小于0→3,2→2成本9。只不采用此普遍自配保证，必要pairing机制可局部I。

实际MULTIMODAL-REPRESENTATION Shared self-attention第一段末→选择fusionpoint稳定原则前；拟I未写，待非作者PRE/具体锁。

同一个 compact token index 未必还代表同一空间位置。多通道图像按 channel 分开 spatial attention、再在对应位置跨 channel 交互，可以减少联合 attention 的规模；但独立 patch masks 会使各 channel 留下不同位置，直接按压缩后的索引对齐就破坏了这个接口。一条训练侧分支保留原 grid coordinates，在等数量可见 patches 间用一对一最小平方距离 assignment 建立共同索引；多 channel 通过一个 reference 分别配对，把 joint 问题改成 star cost。它精确求解的是这一受限成本，不是所有 channel 间的联合最优，更不等于语义对象已匹配。

reference 随样本随机化能平衡各 channel 的对应误差，却不降低整体平均位移；共享 mask 虽保持精确位置对应，又减少独立遮罩的多样性。有限 ViT-S 与六项分类/分割任务的对照显示，单独降低平均距离不足以解释收益，重遮罩时共享方案也趋近；不能把它推广成所有 fusion 的质量定律。平方距离目标本身不保证每个共同保留 patch 都匹配自身，故不继承原文该普遍断言。assignment、坐标与 mask 身份维护增加训练成本，本文未给生产 latency/SLO；几何条件不成立、求解成本过高或收益不足时，保留共享 mask、固定遍历或完整联合 attention，并另验匹配误差与下游任务。

### [21953 Racer: Role-Aligned Competence Estimation for Human-AI Routing](https://arxiv.org/html/2609.21953v1)

2 + 1 + 2 = 5；已确认实际长期差额深入。必要停止：exact-v1完整摘要/§2.2–2.6/§3.1–3.9 Prop1–3/Th1–2完整主文证明、§4.1–4.7/T3–7/AppendF与G1必要目标/更新协议。

纠正原医疗humanAI仅应用拒收，query+classrole正确率对象和coherentrelabelinvariant接口实际新增。Γ=P(M=Y|X,Y=y,C),q=sumηΓ依赖Y⊥C|X；BCE只conditionalgivenU，sufficiency另条件；routing softmax不是q。equal-role/query-near pooledcorrectness/sharedMLP,no absoluteclass embedding，support0fallbackglobal(.5empty)。Thregret0-1noadditionaldefercost非AURSBAC/budgetranking。jointtraining头梯度隔离≠sharedfeature/calibration不变；sparseB/K负收益、Path highBIFD ECE更低但utility弱，CIFAR nominalOOD保持populationlaw非真shift，pairedcellsdependent/descriptive；realgroundtruth二readeragreementmaskeddisagreement非clinicaltruth，CheXpertselectedexperts calibration不同人口。noinference significance/codewillrelease/HWprecisionSLO ND。

实际PLATFORM-EVALUATION-SYSTEM 12002/12101两source marker及校准限制段之后→22170重复pairwise段前；拟I未写，待非作者PRE/具体锁。

Route/defer 的分数还要区分‘倾向把任务交出去’与‘该专家对当前 query 有多大正确率’。一个受限接口在每个候选 class role 下，只从该专家 context 中相同 role、与 query 接近的已标注正确/错误实例汇聚证据，再由共享的 competence head 估计条件正确率；不用绝对 class embedding，使 labels、专家预测与 classifier posterior 一起重命名时保持一致。无同 role 支持则回退 global context accuracy，不能把零证据解释成可靠低风险。再按 classifier 的 class posterior 汇总专家正确率，才能与模型自己的正确率在同一对象上比较；augmented routing softmax 的 deferral coordinate 不是这个概率。

这一分解依赖 context 不额外改变 query 的 label posterior；case mix 含信息时须另估 context-conditioned posterior。Proper loss 只在 population 最优处恢复给定 summary 的正确率，summary 是否充分、有限训练及跨域校准仍要验证；共享 encoder 更新也会改变 competence 读出，stop-gradient 不保证整体预测不变。有限实验中稀疏 context 可使路由差于 classifier baseline，更低 ECE 也不必有更高 routing utility；nominal synthetic OOD 与真实专家的同伴一致性不能升级为人群漂移或真实事实保证。标注、context 检索、两侧校准和维护 role identity 都有成本，0–1 无额外 deferral cost 的 regret 结论不授任意预算/风险最优；支持不足或概率不可比时，回到固定路由、独立人工/规则及明确 Unknown。


## 2026-10-01 最终142冻结快照（待非作者日级Gate）

**当前更新：sep22_resume_v3于2026-10-01T13:42:53+08:00最终非作者日级Gate通过，正式Daily完成，全部普通待办0。** 上述标题保留原冻结阶段锚点，以下单篇“非日级Gate”仅限定单篇POST职责，不覆盖本行最终结论。142/116/24/2及112/26/2/2已实际计数，最终V3、本地链接和限定diff检查通过；终态保留仍不支持正面证据、Books或无遗漏。

来源/贡献筛选已到安全终态，仅保留具名历史外部限制。最后普通必要source/Books为0；最后八个家族均已获得必要source→fresh owner独立采用，七实际I的两段及双侧POST通过，一项标准窄E通过。最终142逐行计数=116深入完成/24标准完成/2中心争议，112实际I/26具体E/2Only/2D；两D不计Evidence通过、不正面Books。此前134摘要108/24为呈现计数误差，实际§3已是109深入/23标准/2D；本轮不改变其评分、证据范围或采用命题。最终候选136 arXiv+6机构，139信号不是全文义务；原138provisional因具名负侧四误关修正为142，不预设配额。

本轮分层negative样本6：21953角色/query估计、21629独立mask对应、21749图/搜索scope、21259采样/描述estimand四误关具体重开；21468成熟verified loop领域使用、20873领域XOR证明沿成熟certifying discipline且无新模型/执行机制两关闭通过。没有重扫其余475题名/附件，不称全部negative全审。旧Negative行已纠正，未变的首批独立校准/必要证据/实际Books结果按身份/版本/采用命题复用。

### [21827 RheoSampling: Resolving the One-Hot Dilemma in Stochastic Dynamic-Tree Speculative Decoding](https://arxiv.org/html/2609.21827v1)

2 + 2 + 2 = 6；深入完成；整合 `INFER-SPECULATIVE-DECODING` books/part-05-inference-system/48-speculative-decoding.md `251/253`。root独立必要source→fresh owner及实际两段/邻接POST PASS，锁释放；非日级Gate。

必要停止：§3.1–3.3/Alg1、§4 Th1/3、§5.1–5.4/Table2/AppendB sparse支持与C1–4全部关键losslessness/slot proof。

m≥1 proxy=min(q_m,z)≥q_(m+1)、constant in Y但是constant alone不足；sample-before-fill固定第m+1slot；global score产品/shallower→left tie祖先闭合，C4固定保留父/前k equivalence→新slot决定性，后sampletail不变。Verification 用actual tempered tail不是treeproxy；min1p/qtilde及positive residual，samplepruned则target补足。m0正文q1+epsilon vs C3 z=1身份不一致且epsilon未给≤1，不采用其普遍祖先monotone/全m保证。3targets6tasks各80题，A6000/EAGLE3原checkpoint/noFT/tree60depth8/3seedsT1，Llama τ5.04→5.25 vs速度2.84→2.93不同分母；m1局部最好/低T优势收窄/m≥3stochasticpruned；Top128仅91.0%massFull100%，4.84vs4.89AAT/Full18.8msPyTorchnative未优化，不完整QoS。HWprecision未披露precision，不补。actual22098 only generalpre-draw/无放回与selectionbias，没有proxy与realproposal dualrole必要rankingbound，窄gap支持I拟两段。不采用OT approximate‘almostalways’为普遍优势，无code复现。

### [21858 Watermarkable Multi-Draft Speculative Sampling via Poisson Processes](https://arxiv.org/html/2609.21858v1)

2 + 2 + 2 = 6；深入完成；整合 `INFER-SPECULATIVE-DECODING` books/part-05-inference-system/48-speculative-decoding.md `119/121`。sep22_resume_v3独立必要source→fresh owner及实际两段/邻接POST PASS，锁释放；非日级Gate。

必要停止：§3–5/Alg1–4/Def4.3/Prop4.4/Th5.1、A4Alg6–7/ThA5–6完整有限实现proof、B1acceptance完整proof/C1.1stopping-time全proof/C2definitions、§6/Limitations与D1、D5(T14–15)必要population/计时/quality。

每context keyed Poisson base过程，target P映射first arrival始终emit；Q MPFR list相同process mapped有iidQ marks可能重复，mergecontext multiplicity。targetwinner在draftset才continue，否则emitwinner后stop；原定目标law由context-independentidealExp clocks链式证明，不要求Psupport⊆draft但各对referenceμ AC。finiteKsupportAlg6 K×BExp arrivals选topB exakt iid；A6只有idealindepclocks证明PRF实keypseudorandom不真独立。Th5.1在singlecontextiidQ list acceptance下界≠totalrate/latency。sharedkey/fullcontext/randomness相同时tokenchain由target侧定义、drafter改变stoplength非content；statement仅commonpositive supportτ给conditioning，非普通PRNGseed顺序消耗自动不变。Watermarkunbiased是keys/randomness marginal非每fixedkey纯target；detector依赖key/prefix不是法律provenance/adaptive attack resistance。MainT1 caption Llama3.1 vsD1/D4正文Vicuna secondpair未统一，窄采用不拼该身份；D1 float16 singleH100 topk50topp1T1max128/1000prompts/多seeds但mean±std acrossprompts vsmain3seeds口径不要替换。D5 .990minpair notactualalloutputsbyteidentical，LPPLparity不是distributionproof。当前couplingbookkeeping slightlyslow作者承认，通信/水印/efficiency根本tradeoffunclear。No fullcode inspection/reproduction，不採每B‘breakingno-go’普遍结论。freshactual经典qratio/residual/targetlaw有，缺targetkeyedsampler独立draftstop角色及多Poissonarrival预算，拟I精确机制Ch48不复制Ch72水印审计。

### [21983 SkelWAM: A Skeleton-Guided World-Action Model for Zero-Shot Cross-Embodiment Manipulation](https://arxiv.org/html/2609.21983v1)

2 + 2 + 2 = 6；深入完成；整合 `MULTIMODAL-EMBODIED-VLA` books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md `75/77`。root独立必要source→fresh owner及实际两段/邻接POST PASS，锁释放；非日级Gate。

必要停止：root实际exact-v1 §III–V/TableII；作者fresh归一化/协方差→privileged3D邻接。

25D六centerline15offset/TCP3/rot6/jaw共同视觉/action；机器人视觉遮罩背景补齐同canonical空间；future仅训练；source统计/weights冻结≠target标定/decoder零工程。rigid保priorbodyintent+measuredTCP/jaw，continuum还orientation≠fullbody真值。w/oA同时w/oD混杂、wrist43.0近43.3；1k simulation/source467，真机仅3任务定性，43.3不授普遍zero-shot。HWprecision/SLO ND，无code复现。

### [21996 A Lie Detector Test for Language Models: Reading Knowledge a Model Won't Reveal](https://arxiv.org/html/2609.21996v1)

2 + 2 + 2 = 6；深入完成；整合 `PLATFORM-SECURITY` books/part-06-ai-infrastructure/72-security.md `2560/2562`。root独立必要source→fresh owner及实际两段/邻接POST PASS，锁释放；非日级Gate。

必要停止：root实际exact-v1 §3.2 Eq1–3/§4–5；作者fresh16890→运行期身份邻接。

PIRcorrect-minusdecoys，honestcorrect定义标签；部署assay需该模型basecheckpoint，referencefree≠无候选标签基准；freeform来自elicited+deployed样本，peak/divergence不同对象；steeringsufficient非necessary，necessitynegative；单seed strictrotation样本条件；anti-probe保capability让readout失效，insample保证撤回。静默不可分neverknown/removed，无永久erasure。

### [21629 Extending Decoupled Attention to Dense Prediction and Masked Training for Multi-Channel Images](https://arxiv.org/html/2609.21629v1)

2 + 1 + 2 = 5；深入完成；整合 `MULTIMODAL-REPRESENTATION` books/part-03-multimodal-world-models/23-multimodal-representation.md `286/288`。root独立必要source→fresh owner及实际两段/邻接POST PASS，锁释放；非日级Gate。

必要停止：exact-v1完整摘要/§3.1–3.2 Eq1–7/§4协议/§5.2对照与mask-ratio反例。

纠正原仅microscopy/science拒收：independentmask保留后同compactindex不再同grid身份，genericattention接口实际变化。equal-k二channelHungarian squaredgridcost；多channelstarreference C−1 assignments仅starcost精确非allpairjoint；randomref平衡perchannelerror mean.87不变；row/Hilbert平均距离改善不解释质量、sharemask100%对应但失diversity，heavy.75趋同。ViTS16/RTX3090/sixlimitedtasks，precision/seed/latencyND；不复现。重要反证：原§5.2‘shared retainedpatch必自身因0distance最优’不成立：同一行A{0,2},B{2,3}，匹配0→2,2→3成本5，小于0→3,2→2成本9。只不采用此普遍自配保证，必要pairing机制可局部I。

### [21953 Racer: Role-Aligned Competence Estimation for Human-AI Routing](https://arxiv.org/html/2609.21953v1)

2 + 1 + 2 = 5；深入完成；整合 `PLATFORM-EVALUATION-SYSTEM` books/part-06-ai-infrastructure/66-evaluation-system.md `260/262`。root独立必要source→fresh owner及实际两段/邻接POST PASS，锁释放；非日级Gate。

必要停止：exact-v1完整摘要/§2.2–2.6/§3.1–3.9 Prop1–3/Th1–2完整主文证明、§4.1–4.7/T3–7/AppendF与G1必要目标/更新协议。

纠正原医疗humanAI仅应用拒收，query+classrole正确率对象和coherentrelabelinvariant接口实际新增。Γ=P(M=Y|X,Y=y,C),q=sumηΓ依赖Y⊥C|X；BCE只conditionalgivenU，sufficiency另条件；routing softmax不是q。equal-role/query-near pooledcorrectness/sharedMLP,no absoluteclass embedding，support0fallbackglobal(.5empty)。Thregret0-1noadditionaldefercost非AURSBAC/budgetranking。jointtraining头梯度隔离≠sharedfeature/calibration不变；sparseB/K负收益、Path highBIFD ECE更低但utility弱，CIFAR nominalOOD保持populationlaw非真shift，pairedcellsdependent/descriptive；realgroundtruth二readeragreementmaskeddisagreement非clinicaltruth，CheXpertselectedexperts calibration不同人口。noinference significance/codewillrelease/HWprecisionSLO ND。

### [21749 GraphSkillEvo: Evolutionary Optimization of Graph-Structured Agent Skills](https://arxiv.org/html/2609.21749v1)

2 + 1 + 2 = 5；深入完成；整合 `AGENT-WORKFLOW` books/part-07-agent/81-workflow.md `1045/1047`。sep22_resume_v3独立必要source→fresh owner及实际两段/邻接POST PASS，锁释放；非日级Gate。

必要停止：§2.1/3.1–3.2、§4(T1/T2)、§5.1–5.3(T3/T4)、B.2/B.3/Alg1 validator。

peer独立necessary/fresh owner/literal PRE PASS，graph stripping保guidance/nodeinstructions五任务均退、mutation/crossover matchedbudget3repeats；validschemanotcommit/LiveMath退/ALFWorldcost更高/重生成无固定cap

### [21259 CogGym: Towards Large-Scale Comparative Evaluation of Human and Machine Cognition](https://arxiv.org/html/2609.21259v1)

2 + 1 + 2 = 5；标准完成；已有覆盖 `PLATFORM-EVALUATION-SYSTEM` books/part-06-ai-infrastructure/66-evaluation-system.md `能描述分布，不等于逐次调用会从该分布采样`。sep22_resume_v3独立必要source→fresh owner窄命题采用 PASS，无Books新写；非日级Gate。

必要停止：exact-v1 fullabs、§2/3 sharedEML renderer/modelprompt/同trialIDs、§4 replication/limitations、E.1–E.2关键counter/F必要。

原无internalmechanism关闭错误；Gemini10-run sampling vs verbalized同spec提供分布对象反证，Gemma5→50固定prompt/temp/trials只稳定mean。15replication521study participations非521uniquepeople；reference172exports/179eligible差异不合ceiling。actualCh66该标题两段确覆盖窄命题，整CogGym schema/模型taxonomy/内部认知非E。peer必要source→actual PASS，无运行/代码复现。

全日Coverage只支持合同有界入口/主题处理，历史Replacement原批次、12748v2公开时刻、Google动态目录及已删MiMo提交等保留范围不支持无遗漏/正面证据。恢复条件与正式六部分§5保持一致。sep22_resume_v3已于2026-10-01T13:42:53+08:00完成非作者日级Gate并通过；最终142与普通0成立，正式Daily同步完成态，不由作者自签。
