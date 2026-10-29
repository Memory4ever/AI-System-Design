# 2026-01-20 现有 Daily 遗漏增量补查

作者：supp_jan20。仅处理北京时间 2026-01-19 完整自然日；保留原 README 时间窗口、66 家族的日期、评分和有效审阅。运行前原文保存在 `baseline-before-supplement-20261008.md`。不创建新日期，不读取旧 Weekly，不 stage/commit/push，不写学习状态或索引。本记录是补查原始依据与停点，不替代 README 六部分或非作者日级验收。

## 来源、日期与去重依据

四个有界主题查询使用 Submitted Jan15 19UTC～Jan16 19UTC 作为发现 buffer：learning-valid 135/135、system-valid 36/36、multimodal-valid 93/93、agent-compile-valid 83/83。这些数字是查询命中，含跨查询重复，不是当天公开论文或候选数。原 `query-learning.xml` 返回48140宽库存，与请求边界不符，废弃为覆盖证据，不送入全文队列。相关标题补检只利用已取得清单定位可能遗漏的机制；CL 月列表只用于 identity/title，首2000/2168不宣称完整分类覆盖。

首批13个完整 exact-v1 题摘已由作者与 root 实际独立校准；10潜力项先核日期及去重。官方 [availability schedule](https://info.arxiv.org/help/availability.html) 对 Thu14～Fri14 美国东部时间的 submission 规定 Sunday20 公开（BJT Jan19），final arXiv ID 在公告流程分配；10项官方 DOI deposit 保留相应 final-ID 与 v1 Updated Jan19T01UTC、registered Jan19T02UTC 的可核最晚公开上界。因此用公告日程下界＋final-ID 公共分配＋当日官方 deposit 上界联合核定日期 Jan19，不把 Submitted 或 DataCite 注册单独当公开证明，也不追分钟。root 实际读官方日程、MLK说明并 parse10份dateJSON，确认这批落窗。MLK Jan19 假日只影响 FriJan16 14ET 后至 TueJan20 14ET 的下一 cohort；官方说明保留 `supplement-20261008-mlk.html`。不改原66项日期。

ARC Prize 2025（2601.10904v1）同技术报告的关键结果已在作者官方 Dec5 [results analysis](https://arcprize.org/blog/arc-prize-2025-results-analysis)公开。作者实际读 v1 核心与官方旧文，没有发现拟采用命题的额外增量，作为同事件恢复线索不新计，不暗示 Dec5 Daily 曾有效审阅。其余9项未与原候选同家族。第二批24完整 exact-v1 题摘已读并由 root 校准；11063在本日原 SCREENING39已有同事件有效排除，不能以改名/关键词推翻它；仅具体新执行协议或原文反侧才定点重开。

## 首批9项必要证据与当前 Books 处置

以下均为 [精确 v1 HTML](https://arxiv.org/html/2601.10873v1) 及同名本地 `supplement-2601.<id>v1.html/.txt`，未核 artifact、未运行或复现实验。核心/对照/反侧支持与限制足够即停，不无差别读附件或比较全版本史。

### 2601.10873 — Unit-Consistent (UC) Adjoint

2+1+2=5。已读§2–6与AppA–C必要数学、C7–9和D边界。采用同函数不同参数坐标影响 optimizer trajectory/metric：W=D W′E，给定尺度的canonical update映回 W−ηD²GE²，是预条件替代分支。正齐次ReLU允许相应gauge，残差耦合约束尺度；LN/BN/softmax/tanh/sigmoid不允许任意全网gauge，bias、conv与optimizer-state须处理对应尺度。没有完整Transformer/normalization替代对照，不采作者“普通transpose反传错误”“物理意义”“BN只是patch”的价值判断。候选准入校准通过；具体Ch4 gap深入，root必要原证已核，Ch4实际111/113与自身note，root必要原证/owner PRE及actual103–125 POST通过、窄锁释放；负梯度/optimizer后与连续流前交接已核。

### 2601.10922 — DCVLR data curation

2+1+2=5，标准完成，root认可仅报告边界。实际读 Methods4–5、Results6、Discussion/limitations8、Tables2–3。固定Qwen2.5-VL7B上16次随机答案采样定义k；moderate为0≤k≤8，含0。固定1k与3 training seeds对比，moderate .491±.002、super-hard .472±.023、easy .440±.024；overall38.4→46.0 vs Walton10k46.7不能写全面胜出。LiveXivTQA占7913/16640主导总体，不是新独立验证；1k plateau不证明固定tokens/FLOPs最佳预算。多样性/CoSyn负结果限定同设置。可核局部curation证据而非完整训练成本/普遍数据策略，Books仅报告。

### 2601.10962 — Transient SGD dynamics

2+1+2=5。实际读§II1–7/III与AppA2必要证据。MNIST1000、两层MLP、20runs及matched初始化下，排除发散、100%训练收敛；flatness为前10 Hessian特征值几何均值，不是参数不变指标。zero-error cluster/Jaccard及线性barrier不能排除所有非线性连接。经验“首次loss<.1”与toy simulation最后basin switch是不同freeze定义。two-valley quasi-adiabaticτx≪τy、HessianalignedGaussian局部SDE、小步长解释；噪声弱化特定选择又延迟冻结，有限早期basin决定不可缩成“SGD长期平衡偏好平谷”。不授LLM/Adam/通用schedule。root必要原证/owner PRE与actual131–160及自身note POST通过；Ch4实际145/147在batch noise后，普通稳定性/吞吐解释共存，锁释放。

### 2601.11022 — Geometric quantile test-time adaptation

2+1+2=5。已读Methods3–4、Results5.1–5.3及必要theory。固定classifier，训练6.2M input decorruptor，以source quantile/reference feature和CPU target feature memorybank匹配；不是source-data-free或无状态单query。Figure3明确marginal匹配仍可class permutation；Theorem4要求regularity、reconstructability、finite second moment、absolute continuity、identifiability及local good initialization，不用经验增益认证假设。CIFAR10/100/TinyImageNet severity5及ResNet18/CCT/CVT/ViT-lite局部设置；SoTTA更新权重、协议不同。H100上10k source512dim/b128 quantile模块570MB约2ms/batch；整体1.44→2.03s/epoch、peak765→1429MB，不是无成本或生产inferenceSLO。具体Ch5 gap深入，root必要原源/owner PRE与actual145–157及自身note POST通过；正文151/153承接coding反证到self-distillation，锁释放。

### 2601.11207 — LoRA as Oracle

2+2+2=6，安全诊断边界深入。实际§3全部必要Eq10–40、§4/5、Tables1–2及§4.5。冻结W允许LoRA梯度/轨迹，不是black-box纯query。membership用更新范数时间均值μ/标准差σ，E=μ/(||W||+ε)，C=σ/(μ+ε)时间变异；backdoor另用class syntheticproxy、更新方向偏移、MAD、跨trial rank，不混两sensor。ViT MNIST/GTSRB recall.40/F1.57；DenseMNISTBlendtop1.20、VGGCIFAR100WaNet.40；已知target rank≠是否clean保证，无clean FPR闭合。Eq18 expert score、dynamic pivots与完整校准recipe未闭合；T2captionASR混targetrank，不当attack success rate。16GB未披GPU/time，W功率非总energy，frozenbackbone仍有完整forward/neededgradient。root实际必要原源＋Ch72 membership邻接PRE，并实际POST修正时间变异/方向混淆后通过。整合 `PLATFORM-SECURITY` Ch72正文309/311，现有loss/canary/Unknown共存；自己的Review note3210已记录实际POST，锁释放。不授LLM/生产安全/SOTA。

### 2601.11334 — Information theoretic representation rate

2+1+2=5，标准完成，root认可仅报告。已读§3–5.4、Discussion与AppA/B必要定义。采用具体finiteprecision representation alphabet的R=q log2|Z|/n、sourceentropy/measurementnoisebits框架；bijective signal regression、stationaryergodic/iid AEP、n足够大、training data足够等假设。AppA典型集cardinality只证明code存在，不授有限模型learnability/optimizer可达；噪声I(X;Y) operational capacity受定义条件，不等同实际LLM容量阈值。作者将LLM应用列未来研究；不以一般信息论词汇倒推该文更大贡献，Books仅报告。

### 2601.11435 — Heavy-tail decentralized optimization

2+2+2=6，具体Ch36差额深入。已读§3/4/5/7、Algorithm1/Theorem1/Figures2–3。固定强连通rowstochastic图π偏置→PullDiag对角校正gradient tracker＋每update K轮混合＋normalized tracker direction，不是momentum。Assumptions smooth/lowerbound、unbiased、p∈(1,2]有界centralmoment；sample与comm nearoptimal随机iterate期望stationarity，不是walltime、动态/异步/任意噪声。PTB六层TXL512hidden8heads/ff2048/drop.2/seq35/b20/n8exp/n16ring，LR调参；K topology代价、强连通exp图增K无进一步收益近文。root实际必要原源/actual owner PRE＋正文79–98与note1822 POST通过。整合 `TRAIN-DISTRIBUTED-TRAINING` Ch36正文87/89，位于compressed/adaptive gossip后、SeedFlood前；自身notes已记实际POST，锁释放。

### 2601.11442 — Map2Thought

2+1+2=5，具体Ch23差额深入。已读§3/4、Tables1–3。视频pipeline估计centroid/AABB/roomscale，grid20与metric→确定box/vector操作，不是物理truth。额外检测/分割/重建：Detic每10帧、GroundingDINO/pi3/SAM2/MoGe2估计，frozen2DCLIP/3DCUT3R融合/SFTLoRA，不把所有成本视为已controlled。Table3同25% predicted+CoT58.8、prednoCoT54.0、noMap54.0、GT73.7；全量61.0vs60.9且RelDir69.8vs80.5退步，不授通用优势。半数据body59.5不照abstract59.9。root实际必要原源/owner PRE＋正文718–738与note1207 POST通过。整合 `MULTIMODAL-REPRESENTATION` Ch23正文724/726，metadata接口后/位置编码前；自身notes已记实际POST，锁释放。

### 2601.11517 — Explanations across reasoning models

2+1+2=5，拟可靠性gap深入。已读Methods2/Results3全部必要含T4、AppA2。五LRM（NRR1.5B/OpenT7B/GPTOSS20B/QwQ32B/DAPO32B），MedCalc100(seed42)与20instructiontasks×5examples（8old12new）100例。o4-mini04-16生成transferexplanations再stripanswerlabel，不保证不泄答案或内部faithfulness；sentenceensemble3candidate/15tokens以低perplexjudge增加调用费。Consistency含consistentwrong。T4DeepseekGRPOself.11→.18、transferacc.30→.29而consistency.11→.39，明确稳定不等于正确。15researchers×10medicalquestions各5与4种组合rating是感知评价，不是actualuser solving/faithfulness。Ch8具体gap深入，root必要原源/owner PRE与actual150–187及自身note POST通过；正文174/176的Reliability→explanation接口交接已核，锁释放。

## 第二批准入校准后的定点范围

24完整AB均已读，root实际独立准入校准。八明确潜力与11035/11262有限决定事实补读后，第二批正式新增10家族，日期联合证据与原66定点去重完成；以下逐项记必要支持/反側和实际Books处置，不因AB读取算证据完成。

决定准入的有限core已补：11035 detector×generator/VBench盲点与11262端到端蒸馏成本进入5标准Only；10905/11421/11161/11292/11063按具体成熟组合或主线关系不足关闭，root实际核验沿用，不重复相同审读。11401传统MARL critic与11491经典extractive Ising无实质主线关系，范围关闭。其余七项完整题摘具名理由见下表；不因地方场景一概拒，也不用候选4分替代贡献门。

## 第二批必要证据与处置（校准后）

以下均 exact-v1，HTML优先；10918 HTML404后用同版本PDF抽取，不用后来版本结论。十项与本日原66无同家族重复。15份决定事实/潜力项dateJSON的v1 Updated均Jan19T01UTC、registered均Jan19T02UTC，完整题摘Submitted均在前述公告cohort；沿用官方下界＋final-ID分配＋deposit公开上界联合核日，不用单注册。20项新增候选的当前官方abs页已实际轻量检查Comments与撤回/纠错说明；看到发表/版本标注，无影响采用的具名撤回/纠错信号，不遍历全版本史。

### 2601.10836 — One Model, Many Behaviors

2+1+2=5；标准完成，root已实际必要core与Ch66 628–639批准已有覆盖。§3–5：固定ResNet50/ImageNet，56训练recipe×21 OOD detector与近/远/极端/synthetic八组OOD。IDaccuracy不是OOD能力单调代理，model-method交互及错误ID人口揭示训练recipe的影响；不是56独立模型种子的统计定律。§3.1“无需OODcalibration”与后文用heldout ID/OOD选择method超参不能合为无标签生产gate；仍有单架构、训练与调参预算及shift局限。Ch66实际628–639已讲固定representation身份和detector分账，root确认已有覆盖，不将topic相似当覆盖证据。

### 2601.10918 — Neural Induction of Finite-State Transducers

2+1+2=5；标准完成，root必要原证批准受限仅报告。PDF §3、§4、§6关键消融、§8/9：CRP字符串对齐、one-layerElman RNN谱约束与下一字符输出、gold/syntheticinput采样，标准化hidden后kmeans、多数transition、threshold剪枝及冲突split，最终minimize FST。新产物替代为有限regular string transduction，而非任意RNN/LLM精确等价证书；未观察/低频边会丢、right-context任务差，objective消融不是所有dataset受益。最大语言validation sweep约A100一天，OSTIA有1天截停；专家对比只限定其任务。有限可解释执行产物不直接改变本书基础模型状态压缩选择，拟仅报告。

### 2601.10930 — Where to Touch, How to Contact

2+2+2=6；具体Ch26接口差额深入，root实际必要源/owner PRE通过；正文141/143、完整133–153与note1498实际POST通过，锁释放。III–VIII、IX限制、Fig10：理论contact-intention含contactpoint与object subgoal；实际policy不回归SE3，而选离散keypoint与w_pos/w_ori终端cost权重。高层object-frame geometry/goalflow/clearance，低层ComFree-MPC采用已有contactmodel实时执行；三组robot-specific参数调校不算高层重训练，也不是无embodiment适配。40×RL决策步改善仅约2×底层控制步，end2end额外reward/world-frame输入非纯架构隔离。实机Franka stick、同训练STL字母每10/cube25，100HzMPC/500HzOSC/40Hzvision；I跟踪失效，关键依赖准确pose/有限keypoints，不授多指、任意本体或安全。Ch26实际112–159 hierarchical及800–821 contactfeedback邻接已读，拟contact-cost接口放subgoal与低层分权论证中。

### 2601.11035 — Your One-Stop Solution for AI-Generated Video Detection

2+1+2=5；标准完成，仅报告。root实际准入事实校准通过。§2、§3.1/3.2 Finding2：H264一致化后，32帧sample取前8、256²crop；I3D/DeCoF/UnivFD在各T2V generator训练与交叉测试，最佳训练源/最易检测源依detector而变，不能由VBench生成质量排序代签。内容/压缩/训练budget等未全部被因果隔离，不以31/33/1500规模或所有VLM失败宣传准入。这里新增有限评价盲点，非通用检测部署或内容真实性保证，Books仅报告。

### 2601.11087 — PhysRVG

2+1+2=5；具体Ch25长期差额深入，root必要原证/owner PRE及actual正文136/138、完整邻接128–151和自身note1312 POST通过，锁释放。§3/4、Tables2/3与AppB/F/G：SAM2提取轨迹、GT trajectory offset与碰撞邻帧代理，差group加FlowMatching Mimicry，否则GRPO Discovery；修正有限探索时难样本无好reward/全参塌陷，不是strictphysicsguarantee。Wan2.2TI2V5B→5context帧V2V、10M视频+700手选/约50holdout、stage1全参16ksteps/stage2LoRA250/G20/b640/32H20。LoRA/FT/FT+RL/FT+MD对照支持局部训练分支，matchedGPUhours只为特定超参对比；不授所有baseline总预算同等。AppG换色/多球/shape错误未被轨迹reward惩罚；单seed可视和V2V强context不证明action-conditioned worldtruth。Ch25 actual128–157旧simulator/learnedmodel/hybrid邻接已读，拟反馈仲裁分支和truth负側近正文。

### 2601.11096 — CoDance

2+1+2=5；具体表示对应差额深入，root必要原证/owner PRE通过；作者正文724/726、完整718–736与自身note1211写后已读，POST发现feature unbind对象误写，按原§3.2改为pose encoder输出的pose features，root实际正文724/726、完整718–731及note1211修正后POST通过，锁释放。§3.2/3.3/4.1–4.3：训练随机pose平移/缩放、pose encoder 输出的 pose features 平移复制解除强pixelbinding，再用subject/count text与SAMmask分开语义/空间rebind；mask-only会组合不同人的碎肢。Wan2.1DiT14B冻结+LoRA/新encoders，额外10kT2V、20multi-subject与quantitative SOLO声明不当完全隔离。20新bench、8单人baseline强制multi与缺原生multiartifact局限；human identity .88低于AnimateX.96，不采全面最优。Unbind/mixdata推理旁路不代表mask/text/poseencoder免费，也不保证任意count/identity。Ch23 actual709–738状态metadata邻接已读，拟位置与subject对应的不同身份责任分支，不堆生成模型名。

### 2601.11170 — CLASSLA-web 2.0 iterative crawling

2+1+2=5；标准完成，root必要原证批准受限仅报告。§3、§5.2/5.3：七个SouthSlavic nationalcorpora，2–3年recrawl后4gram/MinHash近重合阈值.7；textnew约81.77%/73.09%，URL-overlap与text-overlap七点in-sample Pearson.908及linearproxy不能作跨域通用recrawl公式。新旧pipeline同时改变near-dup normalization、topdomain人工过滤与topics，不把差额全归时间；top250domain分类污染不证明LLM-origin比例。当前官方项目引用2026论文，2024采集不是2024公开，不无依据挪日。局部语言/crawl快照上下文，不新增普遍质量pipeline，拟仅报告。

### 2601.11210 — VidLeaks

2+2+2=6；安全边界深入，root实际必要源/owner PRE通过；正文313/315、完整305–324与note3214实际POST通过，锁释放。§3/4、§6.2、§7/8核心与Discussion：纯生成query以TopK空间语义anchors和多query邻帧/首帧语义稳定性作为两个sensor；监督classifier、已确认nonmember reference、query-only access不能混校准。Q2–5，query-only AnimateDiff/Mira/InstructVideo AUC82.92/77.66/97.01而TPR@1%FPR12.6/5.1/62.28；source dataset member标签与Panda70M nonmember有分布混杂，弱blind VideoCLIPclassifier不是全部因果排除。Caption/CLIP/多生成费和snapshot/fusion权重校准限制保留，不采theoreticalupperbound/训练身份司法证据/阴性安全；cfg±.5/steps±1轻扰不是完整defense。Ch72 actual285–323已有loss/position/entropy/adapter轨迹但无video-output temporal sensor，拟增窄分支。

### 2601.11262 — Lyrics-Aligned Audio Embeddings

2+1+2=5；标准完成，仅报告。root实际准入事实校准通过。§3/4/5.4/5.5：ASR转录/textteacher生成lyrics空间，Whisperencoder+attentionpool/MLP以pointcos和pairwiseMSE蒸馏，去除autoregressive decoder但不去vocal detection/segmentation。200随机DiscogsVI tracks，端到端6.07→1.90s、forward.22s，仍主要受前处理；31.9M vsByteCover202.3M/CLEWS196.8M不是全设置SLO。训练singleA5000/24GB/b128三epoch约33h，不能作为已披inference hardware；runtime precision/batch/concurrency/SLO Not Disclosed。三个retrievaldataset仅保留82.76%/81.95%/85.29% vocal tracks，SHS100k ByteCover更好、lyrics改变/parody/instrumental失败；proprietaryvocalfilter与catalog限制重现。有限质量/端到端成本边界仅报告，不升级全音频表示范式。

### 2601.11460 — Semantic-Geometric Task Graph-Representations

2+1+2=5；标准完成，root必要原证批准受限仅报告。IV/V B–D：scenegraph encoder无actionlabel，三次messagepass+temporalattention；两个decoder分别消费globaltaskcontext/objects及time-aligned pastactions，semanticnext/future与framehorizon分开。KIT/own两个bimanual human数据，leaveonesubjectout、四seed；baselinefeature access不同不隔离MP架构因果，高framehorizon accuracy可重复current却错semanticprogress。Robot frozen encoder/adapted decoder finetune必需，实机10trials与预定义primitive checker，简单动作仅feasibility，motion→MPC未实现。当前评价反侧有价值但受限任务/graph配方，不授VLA一般选择；root必要原证批准受限仅报告，不新增书稿。

## 第二批贡献门前排除

root必要原证定点事实校准确认10905（传统RBF/AE worldmodel+Shapley VM/Nutanix/K8s负载，无直接模型执行机制）、11421（HOI/affordance→task generation/专家可行过滤及SR/PSR更多任务，没有新诊断轴）、11161（既有GMM known/unknown labelspace与source/EMA双L2anchors局部配方）、11292（近似8bit乘法器库/布局搜索、固定ResNet18模拟，无新低比特执行协议）关闭；11063旧本日有效同事件排除与实际Sequence/Fallback/blackboard组合一致，不因v2改名转新事件。11401传统MARL critic、11491传统Ising抽取摘要无主线直接关系。七项局部10802/10819/10921/11045/11076/11301/11322保留完整AB，按具体recipe/annotation/local模块不足准入关闭，不给候选4分来代替贡献门。最后七项具名原增量已在下表展开，不以本段泛称替代分层抽检材料。

最后七项的具体题摘理由（不把材料数扩大为全文队列，决定事实若被独立复核反驳只重开受影响项）：

| exact-v1 ID | 具名实际题摘增量与关闭理由 |
| --- | --- |
| 10802 ICONIC-444 | 新工业图像444类/near–far OOD类别、4task/22detector baselines；数据扩容，题摘未提供新评价混杂/失效证据或模型机制，不以3.1M规模准入。 |
| 10921 RobuMTL | weather perturbations选择已有层级LoRA/MoE适配；局部多任务recipe/域内指标，不借成熟inputrouting原则计新SystemReach。 |
| 11045 DAGR-VQA | globalregister加入CNN形成动态saliency再作temporal quality预测；组合和域内分数/FPS不支持可定位表示/执行取舍反側，视频质量应用映射不足。 |
| 10819 outside-in Sparse4D | worldcoords/occlusionReID/COSMOS风格增强是基础设施摄像任务适配；TensorRT MSDA只称优化插件/2.15×64stream，没有具名新的kernel执行选择或可比质量预算条件，黑箱数字不授权机制。 |
| 11301 SAMannot | SAM2人机标注、instanceID、barrier-frame lock/refine和mask-skeleton prompt是本地标注工具工作流；题摘processinglayer未给出可定位内存执行/新可靠性条件，格式/UI成果不作基础模型机制。 |
| 11076 A3D | assembly affordance geometry+interactionfeedback调整双臂support，当前题摘贡献限任务配方，未指明新反馈协议/状态职责或原决策失效条件；不是因‘机器人’本身排除。 |
| 11322 logic situational-awareness | CV/logic组合挑fine-tune并解释VLM输出，题摘未给出逻辑验证错误/成立条件、评价/训练边界的实际增量，不能把justification当可靠性保证。 |

## 第三批准入校准与唯一新增候选

agent/compile主题查询83/83已停止；只对10个含糊相关标题完整读exact-v1-c.xml，root独立实际AB校准，未把83条抽为逐项全文池。11286一项新增；其余贡献前关闭，不评分。11007/11286 v1官方deposit Updated Jan19T01UTC、registered Jan19T02UTC与前述公告/finalID联合落窗；11702 v1 Updated/registered Jan21跨界，不作为当窗日期证明。Submitted buffer不纠正这个跨界。

### 2601.11286 — XChoice

2+1+2=5，标准完成，仅报告提案级评价轴。实际§3/§4/§5.2/§6、AppD/F：对人和LLM决策用同constrained行为模型拟合factor/constraint参数，而非只看outcome；4307 ATUS样本/四activities，snapshots gpt4o2024-08-06、Claude3.7-20250219、Qwen2.5-72B/Llama3.3-70B/DeepSeekV3。模型form/normalization、遗漏变量与heterogeneity限制估计，不直接读取内部偏好；mild covariate/resampling shifts不保证真实大regime漂移或再query后稳定。

打印§4.2/4.3 share=θ_jᵀX/Σθ_kᵀX与θ_Other=0使Other预测share=0，却Other观测均值349/1440非零，必要estimator身份未闭合。root明确允许提案级5仅报告，全部参数rank、模型alignment优劣、robustness与RAG改善子命题隔离，不作正面证据或进入Books。定点重开只需可核的reference normalization、实际predictor/estimator实现或作者澄清，不反复审公式/完整附件。数字实验不能反推内部因果/规范偏好；本次提案Only不采用该组数字。

### 第三批贡献前关闭记录

- 11702 PASTA：root/作者实际§4.4–4.6，paragraph schema、cardsection×article LLM relevance筛选、pairwisejudge、semanticbatch/caching成熟组合的领域pipeline；未建立可验证新coverage/可靠性条件或可比quality-cost边界，不把44.9%skip当truth。最小core关闭已获root确认，跨Jan19/21必要date不再影响处置；不为它另追公告或申请材料，不作窗内候选。
- 11007 AdaMARP：root/作者实际§3.1.3/Algorithm1，roles/history上switch/add/pick只是sceneappend、profileinstantiate与speaker选择；单Actor负责全部nonuserrole，RP message/style数据配方无新执行一致性/权限/可靠性协议，关闭已获root确认。
- 11675 MetamerGen：gist/fixation双stream DINOdiffusion以人类same/different metamer/视觉心理为终点，题摘未改变当前模型/执行主线判断，范围关闭，日期未核不影响处置。
- 11287 Seek and You Shall Find：HCI searchtips/受控implementation，实时LLM adaptivity仍愿景，不纳模型系统机制。
- 11182 Knots to Knobs：已有SAE插入collaborativefiltering autoencoder的地方迁移/推荐steering，不凭LLM来历建立直接主线增量。
- 11358 Zonotope：物理sensor RLola传统boundedmonitor，不是基础模型runtime，不能以runtime关键词映射本书。
- 11049 biasedhumanprediction：完整AB再次发root核完；六认知任务/对人预测的域内行为模拟，无可定位模型机制/执行判断新轴，范围关闭。
- 11238 LLM-PRF：LLM semanticfilter之后RM3组合改善，题摘无新quality/cost成立条件或反側，不凭retrieval映射进入候选。
- 11412 searchsimtaxonomy：综述measure taxonomy/四dataset相关性，题摘未可指認新评价盲点，不以分类/规模准入。

## 机构补查原件与停止位置

保存inst-a/b/c、search-a/b/c/d、inst-recovered检索输出，以及seed.html/page10.html、ernie.html、deepseek.html、minimax-llms.txt/minimax-techblog.md。确切切片/停止已融入README来源表。OpenAI/Anthropic历史翻页、Google日归属、Meta/Qwen/Hunyuan动态目录、Seed不支持静态page参数、MiMo未日期Blog与MiniMax旧tech文章均不支撑历史完整覆盖；已用当前可用原始入口/日期主线补检，原有界浏览器timeout/锁屏限制保持，不无尽重试。目标日邻接目录或具名原始公告可重开对应源；辅助检索负结果不证零事件。DeepSeek更新页与MiniMax现行techindex本次实际恢复，不继承旧timeout为事实。

## 当前停点（更新）

README六部分已融入补查，新增20家族与原66去重，11深入+9标准必要支持/反側已读足。Books11整合（8owner）+1已有覆盖+8Only；root11项整合actualPOST全部通过，11096 Ch23 feature unbind对象修正后正文724/726、完整718–731和自身note1211已独立核验，全部窄锁释放。已有POST自己的源注已更新真实通过状态，不以过程停点重复投入。最终日级尚未通过，不自行授DAY。

三批13+24+10题摘已独立准入校准，必要决定事实与候选原证复核沿用root实际结果。四主题learning135/system36/multimodal93/agent-compile83均单页到total停止；月列表只相关title/identity，错误48140库存不作覆盖或队列。机构历史切片、旧8日期异常及PruneRAG/GeminiProbes中心争议明确隔离；XChoice全部参数/robustness子命题不采用，仅提案Only。最后七个局部AB排除具名理由已展开，供root最终分层判定，不扩全文池。原66表行与baseline逐行完全相同，原窗口完全相同，原66证据39989字符连续块完整保留；最后POST同步后本地链接0缺失，单一连续候选表、V3/限定diff --check复跑通过，作者READY供非作者DAY，未自行更改完成状态。
