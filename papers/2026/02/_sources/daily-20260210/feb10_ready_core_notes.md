# 02/10 必要证据与独立终裁笔记

这是作者原文审阅及分批独立复核的证据笔记；当前处置见顶部终裁与正式README。旧缓存只复用精确身份、版本及必要位置，不复用旧评分。正常Submitted候选的官方排程/注册上界条件已获非作者复核，各原字段见 `feb10_all_selected_date_raw.json`，保留无更早同正文公开信号条件，不伪造精确公开时刻。笔记不单独授全日完成。

135冻结＝111必要core（36actualPOST+3Existing+72Only）+17低分关闭Only+7中心Disputed；全部单项独立终裁通过，root126+fresh9。普通研究/Books待办0，外部日期/历史切片/中心争议及未采用子命题隔离，不授正面Evidence/Books/无遗漏或性能安全保证。root已实际通过当前六部分日级Gate，正式日报完成。无Books锁/session，不扩池、不重读有效证据/POST、不stage/commit/push、本日作者结束不接下一日。

### 最终有限13项终裁与必要修正

root最后4（06949/06953/06960/06964）标准6仅报告通过；fresh9中06887/06911安全6深入、06914反侧5深入、06850/06871机制5标准，06771/06825/06854/06909局部4关闭，均Only并获root接受。PKA改变反馈依赖和cache、RFDM改变forward noise均值，是实际机制而非只proxy，原4已更正5，不因Only/费时降分。必要评价直接反侧与终裁详见本日README §4。

事实补充：DreamDojo §4.6/T6 FPS singleH100，与RTX5090 teleop分开；AEGPO §5.4 FLUX469→521s/step(+11.1%)、33.5→34.5GB；PKA SubjectCanny F1 .414<.551/CLIP-T .349<.352及threshold丢外围；RFDM默认每Δ3帧更新keyframe，Δ1 ErrAccu .16对Δ3 .07，TF .06优DF .07但ViDreamSim .38劣.35，首帧proxy混motion及val/test15%/5%与5%/15%冲突；Generic clean4M/leaky10M同时改量及人口，74 clean未隔离diversity/feature因果；Tamper A7 BF16已披露，不写precision ND。

## 历史必要证据（旧拟/待/人数不控制恢复）

## 最新单项终处置（覆盖下方历史拟定）

最新：06880/06883/06886与06932/06941/06948六限定Only获root必要原源/关键反側复核，正式122＝102必要core（36actualPOST+3Existing+63Only）+13low+7Disputed，122行V3/限定cached和unstaged实际通过。只7ready+6local待非作者，入口停止；拟135未冻结，无Books锁。不重读全部附件/有效POST，下方历史拟/人数不覆盖此状态。

最新：ScaleEnv/POP/EDS-WDS/CTWA/NanoFLUX root必要原源及直接反侧Only终裁已同步116＝96必要core（36actualPOST+3Existing+57Only）+13low+7Disputed。116行V3与限定cached/unstaged检查实际通过，无Books锁。NanoFLUX §4.5确有约2.5s作者合计E2E估算，不等matched-measured验收；下方旧拟定不覆盖最新终态。仅待有限9ready、6local与最后4明确增量，无新增入口。

最新：CodeSSM5标准Only、SquaredPO/FSL6标准理论Only通过；Steering Identifiability6中心全prompt严格等价保证Disputed/暂缓，不据局部经验换终裁，重开只冻结模型共同ker/非线性精确等价必要证明。已同步111＝91必要core（36POST+3Existing+52Only）+13low+7Disputed，111行机器/限定diff实际通过。无Books锁；下方其拟定为原证据，不覆盖终态。

### 最后四项：必要证据已足，有限入口停止，待root

**DreamDojo06949，6=2+2+2标准，拟Only。** [v1](https://arxiv.org/html/2602.06949v1) §3.3.1–4/Eq3–8、§4.1–7/T2–7实际必要源读。两帧VAE瓶颈32维proxy含未来frame，重建/KL不认证唯一action因果；target action MLP首层reset后全部权重finetune，不是latent天然grounded。chunk4/relative action/temporal差分局部可执行替代；data skill由GPT估算、scene表/正文口径不同，不采largest全面召回。700M latent model400k/b256，Cosmos2B/14B pre140k/b1024/256H100，post50k/b512/128H100；action对照pre50k/post25k同step但不是净资源同预算。T2 latent不胜MANO/retarget全部指标；T3更多data Counterfactual SSIM/LPIPS有反侧，T6 student PSNR/SSIM/LPIPS均降，T7 Counterfactual LPIPS .232→.234。self-forcing滑窗12/35→4denoise、student13–49frames截窗teacher监督不授无限horizon正确。50背景edit样本12人偏好不独立物理真值，20scene水果policy相关和10scene五checkpoint+externalvalue非通用simulator认证；RTX5090 teleop不自动归属T6 FPS相同测量HW，precision/batch/SLO/净模型价值成本与独立seedCI ND。有限跨embodiment/蒸馏工作点Only，不造新WorldModel长期因果保证/缺口。

**DAWN06953，6=2+2+2标准，拟Only。** [v1](https://arxiv.org/html/2602.06953v1) §3.1–2/4.1–3/Alg1、§5.1–3/T1–2/AppA原源必要读。last4layer attention去sink/diag/threshold形成每step依赖proxy，anchor放宽induced阈值、greedy conflict独立集（不是maximum最优独立集），不认证真实条件独立或生成同分布。观测consistency以最终decoded output为参照非外部任务correct；attention sink标记不能保证剔除真实依赖。H10080G、len256/block32（KLASS例外bestblock），LLaDA8/1.5与Dream7B；baseline default对比HumanEval选τedge/induced/sink，τlow按16model×benchmark逐项调，不是同search预算或独立holdout。T1 DreamGSM accuracy反退、LLaDA1.5 math/MBPP反退，LLaDAHumanEval TPS108.99低LocalLeap109.8；T2去CBS质量更高，len/block/threshold显式quality-speed取舍。precision/batch并发/SLO/CI与取attention/graph净cost ND，不授headline质量不损普保。局部dependency-guided unmask替代Only，不新增通用joint正确性机制或Books。

**InftyThink+06960，6=2+2+2标准，拟Only。** [v1](https://arxiv.org/html/2602.06960v1) §3.1–3.3/Eq1–8、§4.1–2/T1、§5.1/T2–3与AppH1–2最低配置实际读，不遍历全理论proof。Qwen4B生成cold-start summary、特殊token/SFT3epochs，GRPO同trajectory reward/adv共享全轮、max5训练和max10评估，不是无界完成保证；summary边界由模型选，端任务reward不认证每摘要事实。8/32H200两模型RL1000/500step b128/G8/lr1e-6，同steps非同teacher/总token预算，vanilla train30720 vs迭代每轮10240，eval32k vs每轮8k×10 cap。8H200 TP1/DP8 Semaphore1024，temp.7/p.95×32采样不是32独立训练；CompassVerifier7B correctness代理和PRIME训练timeout判0分开。T2冷启动AMC fixed/random更高，不采alwaysadaptive；T3外summary冷启动更好/RL更差支持有限policy相容而非内部语义真值。T+E精度低于T，latency合所有round但无same-compute/cold-startteacher摊销/SLO验收。precision/独立seedCI ND；不授O(nℓ²)为全服务cost、信息瓶颈理论普保，有限summary/continuation训练Only，不按缺此配方增Books。

**GenerativeMetaModel06964，6=2+2+2标准，拟Only。** [v1](https://arxiv.org/html/2602.06964v1) §2.1–3/§3.1–2/T1–2、§4.1–3/图4、§5.1–2/T4与AppB1/C2–3/C5必要读。单token residual的无条件flow MLP prior；先steer再加噪/20step denoise，非真实manifold精确投影或语义不变保证。FineWeb1B/中层Llama1B l7与8B l15；b4096/lr5e-5/单A10080GB最长5.6天，mixed precision未给格式，baseline SAE维度/预算不同。FD50k来自训练activations、低二维PCA和Gaussian moment不能认证alljoint分布；2048 OWT heldout ΔLM loss非任务保留真值。500SAE×5指令/3persona×20题及100 sentimentprefix由LLM评分，C2 1k扩评用sentimentclassifier+同LLM NLL，仍有限fluency/concept代理非relatedcontrol/OOD保证。113test probing有train筛512/val选/neuron搜索成本，1D可分不认证内部causal；loss scaling仅compute-efficient envelope/大steer r≥1，B1 multi-layer更差FD .66 vs .55，不授一切layer/范围无结构假设。20step净推理成本/serving配置CI ND。新增learned-prior局部干预替代可Only，不能仅owner缺此recipe造长期gap；不执行有害persona生成。

### 第九小批：最小必要证据已足，待root

**Aurora06932，6=2+2+2标准，拟Only。** [v1](https://arxiv.org/html/2602.06932v1) §2/Eq1–2、§3.1–3.3/Eq3、§4.1–2、§5.1/§6/T1、AppA1–3与B1–2实际必要读。SGLang验证产生accepted/rejected branches与hidden/logits，经GPU RPC供独立draft learner，再lazy sync；拒绝分支同target分布KL监督不是外部任务真值，正文称reverse KL但写KL(target||draft)的方向命名冲突保留。条件代理accept length不独自授净服务收益：sync48–1600 sweep中频繁同步反降throughput，图注48与正文80最佳口径不合；lookahead5 discard增益小，10仅Llama coding局部。Qwen8B/H100，BF16+FP32、AdamW、b8、最大2048、TTT5；frontier FP8四H200+额外训练GPU，per-request TPS含prompt+output不是aggregate容量/同GPU预算，Qwen BS32反退。A2缓存隐藏态与logit非零内存/传输，topK/32k词表有条件，不授所有backend无改动或atomic hot-swap；40k与表44k、T1 FP8与App表BF16口径保留。SLO/实际同步p99、同成本capacity/seedCI ND。局部shadow learner可行性与服务反侧值得记录，不把缺此recipe当长期gap，不新Books。

**Endogenous Resistance06941，6=2+2+2必要设计反侧深入，拟Only。** [v1](https://arxiv.org/html/2602.06941v1) §2.1–3、§3.1–6与AppA3.4–5实际必要读。38 explain-how prompts、过滤约半SAE词表、逐feature/模型阈值及每token持续steer；明确verbal restart由Claude Haiku切段、LLM评分同topic，不认证隐式自纠错或外部真值。26 OTD来自正确/打乱prompt-response差异，约半不符合预期方向；clamp26的局部干预与三组频率/幅度匹配random同prompt/seed控制支持有限因果贡献，不能唯一meta-cognitive机制或免疫证明。Llama70B layer33/SAE50与其他模型设置不同，不归因纯scale。meta-prompt/SFT主要增加尝试频率，条件成功率不提升；uniform10boost与逐feature校准分母不同，强boost退为重复。LoRA32/alpha16/BF16/4epochs、38原题synthetic混比10–90%、checkpoint重校阈值非等原steer量/holdout任务证据，硬件/完整teacher与校准成本ND。保留持续干预下有限恢复与残留偏题，不授SFT提高真实monitoring，局部有限协议Only，不新增Books机制。

**Agentic Uncertainty06948，6=2+2+2必要评价反侧深入，拟Only。** [v1](https://arxiv.org/html/2602.06948v1) §2.1–2、§3.1–6/T1–2与§5实际必要读。100随机SWE-bench Pro任务，三模型同family solver/uncertainty但不同prompt、mini-swe-agent read-only不看test；pre任务/repo、mid按最终总轨迹25/50/75%选点（不是可上线已知停时）、post已apply patch。成功用benchmark tests，非reviewer自评。有限负侧：pre/post AUROC区间重叠不授普遍前验更佳；中途confidence降不等区分失败。adversarial降confidence的校准和信号须分账：GPT近uniform shift/AUROC不增，Platt的ECE.01未披露独立校准切分不能作为跨任务保证；Gemini/Claude差分两两p=.18/.09不显著。bug-find平均23.4步/.52$ vs12.7/.23$非免费，100中最少22positive、无行为rollout停止/人工路由策略实测。硬件/precision/完整trajectory token-budget及独立seedCI ND；不授去人工/自动accept安全。该有限提示评价反证Only，不造通用自评失效全称或新增Books。

### 第八小批：最小必要证据已足，待root

**ProtoPurify06887，6=2+2+2安全必要深入，拟Only。** [v1](https://arxiv.org/html/2602.06887v1) §3/4.2–5/Alg2–4、§5.1/T2与§6.1–3/T6/AppA必要读。已知base和同架构paired clean/backdoor训练才建离线vectorpool，target w对base而非无先验malicious-only；cosine挑prototype、lower-m均值/方差阈值找boundary，再SVD抑制prototype高投影singularcomponent，不认证其唯一backdoor因果或所有benign留存。Llama3-8B/Mistral7B、五分类+ChatBackdoor；main四attack与AB六口径保留。T2多行ASR>10%，EmotionVPI Llama CDA.949→.861；T6clean.910→.894/.928→.902不是零副作用。adaptive只有限pre-amplification1.2与两个prototype knowledge条件，不认证所有自适应敌手；α>1 utility collapse。离线pool训练+5–10min/model含SVD不free，hardware/precision/训步与净pool/seedCI ND；不按BDaaS名称授生产。具体局部抑制可Only，paired差额不授安全可识别性，不新增Books。

**TamperBench06911，6=2+2+2安全/评价反側必要深入，拟Only。** [v1](https://arxiv.org/html/2602.06911v1) §3.1–5/4.1–3/5、A2.1/A3/A4/A6.3/A7必要读。新增每model×attack调参后utility约束下最坏harm测量，有限21个.6–8B与五Llama3-8B防御，不是全开权重安全定理。40trial Optuna只fine-tuning，embedding因成本约3A100hours/model未sweep；A7 completion-only/AdamW/BF16/checkpointing/2048，search表HTML字段未展开不补造。utility140 MMLUPro/5shot-CoT且10%相对drop是代理，A4跨16checkpoint与MATH弱相关；10response/condition人审有限，StrongREJECT是convincingness/specificity而非事实正确或真实harm uplift。同一评估上择极值未授独立test/全utility留存；TARuntampered.16vs.44及去utility约束时ReFAT归零直接反侧，不能把低hazard只判强安全。模型family统计差不确定、netcost/seedCI/生产SLO ND。不执行attack/复制payload。具体finite评估反证可Only，不按已有攻击/critic原则造Books新gap。

**Task complexity06914，5=2+1+2必要设计反側深入，拟Only。** [v1](https://arxiv.org/html/2602.06914v1) §3.1–4.2与A5/T1–2必要读。hiddenstate norms/rank、topk5SVD与每位置twohiddenMLP的可恢复性不是执行因果；CLIP后随机删visualtokens，在synthetic count至200时50%删就大退、75%接近零，与多数token count probe好不能合并为‘都可独立供decoder使用’。‘attention specialization’及只改text更佳只是解释/设计推断，未做对应单因素因果训练。Molmo7B-O全模块LoRA16/32，六数据各3epoch/8H100/b32、base5e-5/vision2e-6/proj1e-5，任务输出/保语言captionpopulation不同，不能只归因complexity；GQA row三模型.94/.93/.95都低baseline.97，W2≈chance，不授复杂数据普遍收益。precision/probe完整训练预算/seedCI/净SVD+probecost ND；不给基于norm/rank的通用无损压缩率或新长期guarantee，不改Books。

### 最后六处准入事实/局部差额：有限停止提案，待root

四local项不是因费时降分，评分仅实际局部实现，不计成熟budget/attention/feedback原则。各为1+1+2=4，最低关闭Only，不采用headline性能。**AEGPO06825** [v1](https://arxiv.org/html/2602.06825v1) §3/Eq5–6与§4.1–2：绝对attention entropy差不是KL；batch median划高低组并分8/16、全轨迹Top4峰branch，是已有RL rollout的具体proxy替换，尚无新的budget最优/learning-value定律。原完整AB和T1有限1000prompt局部对照保留，不授净训练免费/普遍加速。**PKA06850** [v1](https://arxiv.org/html/2602.06850v1) §3.2/Eq2–4/3.3：condition-only self-attention使首步KVcache可用，图像位置只看对应spatial token、keyword阈值.2并将上一步mask用到下一步，是明确局部interaction替代；one-to-one softmax不变成原dense等价，依赖位置对应与mask时效，CSAS shifted logitnormal改变采样人口。不采10x/5.1x或任意条件无损。**SEMA06854** [v1](https://arxiv.org/html/2602.06854v1) §3.3/Eq8–9及§4.1必要安全角色：非自适应攻击script训练改用intent-alignment×risk/detail reward；生成脚本不读victim回复但训练真实执行victim与GPT4.1mini judge，80%AdvBench训练且全520主表与159HarmBench范围分清。具体局部reward不建立独立安全判断/免反馈训练，保留judge与数据角色边界而不采ASR。只读方法/角色，不执行攻击、不复制payload。**RFDM06871** [v1](https://arxiv.org/html/2602.06871v1) §3.2/Eq4–6/Alg1：将previous predicted frame移入forward noise均值，不仅concat条件，确有具体local residual替代；保留同帧监督、顺序预测误差传播与帧数扩展不等总cost恒定，不采matchedcompute/所有长视频质量。

两决定性项有具体局部增量，拟1+1+2=4关闭Only而非主题拒绝：**AEGIS06771** [v1](https://arxiv.org/html/2602.06771v1) 缓存`feb10_admission_06771_v1.json`实际§4.1–2：随当前/原concept-center变化做一步AET更新、layerwise parameter penalty与冲突时gradient修正，是具体生成模型erasure实现；借用fast adversarial training/PR/投影不计额外耐久分，参数接近原θ不证明未关联concept保持，retention-data-free只不另取retention集，不等无监督/无重学风险。必要安全保证不正面采用，不因AB只框架名直接排除。**GenericTSF06909** [v1](https://arxiv.org/html/2602.06909v1) 缓存`feb10_admission_06909_v1_ablation.json`实际§5.1–2：real+synthetic、leakyTSMixup对74非leakedcase与depth-vs-width局部消融，是具体baseline设计差额；不能把通用data多样性/更大预算原则打高分，排23测试只消除已知直接leak并非证成唯一feature-learning因果，必要配置尚未标准核，不授controlled-allvariables/SOTA或全Transformer规律。不因time-series应用排除模型架构/训练研究。

各Submitted/Updated原字段实际核`feb10_all_selected_date_raw.json`：06771 Feb06 15:27:42Z、06825 16:09:50Z、06850 16:39:10Z、06854 16:44:57Z、06871 16:56:30Z、06909 18:01:44Z；registered分别Feb09 02:49:52/02:51:06/02:51:42/02:51:48/02:52:11/02:53:03Z，无已知删除/撤回信号；按已核官方排程/ID规则条件包络入本日，不将Submitted/Updated当正文精确公开。未加载其他日期或扩大查漏。六项决定性事实已足够停止；提案若过，则来源入口不再增身份，候选清单可冻结，剩余只本日已明确增量的10篇必要证据及独立复核，不是150正文队列。

### 第七小批：仅必要方法与直接反側，待root

**DeVA06880，6=2+2+2，实际更新/成本反側必要深入，拟限定经验Only。** [exact-v1](https://arxiv.org/html/2602.06880v1) §3.1–3.3/Alg1–2、§4必要假设/Th4.12/4.15、§5/T2与AppE实际读。新增方差因子与scale-invariant方向分离、矩阵旋转基row/column代理；Kronecker期望分解与稳定eigenbasis条件不能推出实际EMA精确协方差。Alg2末行缺Eq14的回转，不静默修复为已核实现；矩阵smoothness及自适应权重说明亦不直接授praktical有momentum全局收敛。理论只零momentum/unbiased有界variance、batch=T和eta=1/sqrtT。Single A10040GB；NanoGPT T2 loss3.271对Muon3.305但16.49s对10.72s，表头ms/1ktokens与行s矛盾保留，不授端到端更快。主文270/274M、FineWeb-Edu与AppE276M/FineWeb10B口径不同，不合并；AppE b49152/lr.001/WD.1/beta1/2/3=.95/eigenfreq10及warmup60%披露，precision/seedCI/部署SLO/净搜索ND。新增局部优化替代可报告，不为owner未有此配方造长期缺口；理论与伪代码受影响子命题不采用。

**ViT plasticity06883，5=2+1+2，必要设计反側深入，拟Only。** [exact-v1 PDF](https://arxiv.org/pdf/2602.06883v1) §3/4/5.1–2、AppC.1–4与D.2/T6必要部分实际读；HTML不可用后只定点PDF而非52页全遍历。平均输入变化率P(f)是输入敏感度代理，不是参数更新adaptability的因果定理；LN Prop1须同位置跨输入mean/std相同，ImageNet像素归一化不证明embedding后满足。MHA bounded token/image energy与FFN operator norm给上界，不以不同上界大小证明实际P排序。经验12800 pretrain图像对downstream、FC2 zero-pad输入的测量人口与真实中间activation不等；保留有限测量排序。ViTBase86M/224²/11分类，MHA/FC1/FC2各28M可训对LN18K，SGD momentum.9/noWD/cosine/b512/clip1，4LR×3seed、4k–20ksteps，验证选checkpoint后test；不是matchedmemory。T6 GaussianNoise LN2更高，Cifar10/100 FC1更高，Sketch FC2更高，MHA平均与FC1差.07未显著，不能授MHA所有任务最好/低smooth必更好；默认FP32只memory表，实际hardware/全runtime精度/测量+搜索净成本ND。保留局部模块选择证据，不改Books通用适应保证。

**Prompt Reinjection06886，6=2+2+2，prompt信息/因果解释必要反側深入，拟Only。** [exact-v1](https://arxiv.org/html/2602.06886v1) §3–5/Eq8–11、§6/T1–7、AppB.2/C/D必要方法/对照实际读。CKNNA/PCA及固定MLP五token类别499train/54test、一次denoise、Adam1e-4/b64/50epoch只测有限recoverability，不证明所有prompt语义丢失或image-only loss唯一因果。等长minimal-pair浅层残差介入支持有限属性传递；LN统计回锚+COCO5K一次SVD Procrustes校准后推理注入，training-free不等无校准/搜索成本。H200，1024²，SD3/3.5分别28steps CFG7，FLUX/Qwen50steps CFG3.5/4；w=.025与origin1/2/2/30由本消融择优，Qwen搜索不充分、SD3.5 target表含origin2的文本边界保留。T2 FLUX PickScore与Qwen CLIP下降，T3 QwenOther下降；w=.1部分大幅退化。T7 SD3每targetblock2.118→2.291ms和rotation8.83%FLOPs不授全模型E2E小开销，FP16/BF16仅memory估算、实际runtimeprecision/batch/多seedCI ND。可报告局部推理干预，不把统计回锚授生成稳定/全信息保持，也不因owner无该配方改书。

最新：Watermark6标准Only、NES6必要安全深入Only、R-Align6必要反側深入Only经root实际必要源通过同步107＝88必要core（36POST+3Existing+49Only）+13low+6Disputed。无新Books，下方拟为原证据，不覆盖终裁。

最新：NanoQuant6标准Only、Grokking5必要反侧深入Only通过；F-GRPO6窄概率/评价差额深入整合，root实际Ch33两段/邻接与末注POST通过。正式104＝85必要core（36POST+3Existing+46Only）+13low+6Disputed，锁释放；下方三项拟为历史，不覆盖终裁。其他ready尚待root，不授日级Gate。

最新：SLR5标准Only、Graphon-PaI6标准理论Only、DAGVul6必要安全/设计反侧深入Only已获root实际必要源终裁并同步正式101＝82必要core（35POST+3Existing+44Only）+13low+6Disputed，无新Books。下方该三项待root为作者原提案，不覆盖终态。

最新：root七项必要源/反侧与七项低分最低关闭通过，TaS贡献前关闭通过。正式98＝79必要core（35POST+3Existing+41Only）+13low+6Disputed，无新Books。下方待root均历史提案，当前仅续最后有限31增量/4局部与2决定性。

最新：root必要原源/反侧终裁ThinkProprio5标准Only、Latent Rethinking6标准Only、Degradation5必要反侧深入Only、Echoes5必要反侧深入Only、Overlap5标准Only、FairJudge4关闭Only均通过，正式84＝72必要core（35POST+3Existing+34Only）+6low+6Disputed。下方六项拟定只保留作者证据，不覆盖终裁。无新Books/Existing，普通工作只限已校准具体增量与决定性事实，非全部日期身份。

最新：root实际AgentCPM-Explore06485 §2.4/3.3局部receiver-policy原源终裁5标准Only通过；DAIReS06532 method/Meta/Discussion贡献前安全排除复核通过，不计候选或评分、不新增外部请求。正式78终处置＝67必要core（35POST+3Existing+29Only）+5low+6Disputed。下方两项“待root”为保留提案，不覆盖此终裁。

最新：root实际LIBERO-X III-B/IV-A/B与SPARC §5/6/T2/3终裁均6标准Only；正式77终处置＝66必要core（35 actualPOST+3Existing+28Only）+5low+6Disputed，无新Books。下方LIBERO/SPARC“拟”为作者原证据，不覆盖此终裁；有限入口停止/实际候选冻结与日级Gate尚未授。

## 当前有限准入校准（不是正文队列）

### 末批第六组三项必要源 ready（待root）

**EDS/WDS06849，5=2+1+2；保证反侧必要深入，拟限定经验Only。** [exact-v1](https://arxiv.org/html/2602.06849v1) §3–5.5/Alg1、A4/A6实际读。采样网格由经验entropy积分/反函数替代uniform；需非负rate与严格增累计，τ-leaping段内rate近似不授任意sampler exactness。uniform有限total-EPR bound与masked奇异分开；A4Eq25是两积分乘积sqrt界，改成积分sqrt(AHna)只称实用proxy，没有推出该更小量仍为严格W1上界，不能采普遍最优transport。NFE不计离线1024时间格×64/1024训练样本校准；主文文本1024sample与A6表64冲突保留。OWT三预训模型1024×1024/GPT2Large生成PPL，EDS在SEDD反差、MDLM64NFE后局部好；无JYS-compatible MDLM/CIFAR参照，不授全SOTA覆盖。硬件/precision/seedCI/校准摊销成本ND。有限schedule替代可报告，不用entropy命名授语义信息/质量普保；无新Books。

**CTWA06869，6=2+2+2；受影响保证必要深入，拟限定条件/经验Only。** [exact-v1](https://arxiv.org/html/2602.06869v1) §3/4.1/4.3/5/6及B1–2必要源已读。分布空间KL近端tilt的一阶covariance law与共享θ更新不同；Fisher/natural方向需可逆、positive margin及小步长，clipping需distortion界，简单cov(r,w)不等普通Adam/共享θ无退步。Lemma4.4内积仅≥0未足抵非零二阶误差，不采零margin的有限步guarantee；Th6.5还需boundedscore/non-saturation/token-gradient对齐且μ正，scalarized收敛不保各objective。EMA cov阈值调整lambda是下一步诊断controller非硬约束。Math500三小Qwen、accuracy/clarity二值规则与length代理；4L40/FSDP/vLLM、90epoch/b32/K16/1024in-out/lr1e-6、GRPOclip.2/KL.001，MGDA与Lagrangian KL0不同。B1明确部分baseline accuracy更高，以balanced描述不称全部普胜；precision/独立seedCI/控制器净成本ND，不采negligible证明。只限定理论条件与有限控制替代，不自动新增多目标长期guarantee或recipe gap。

**NanoFLUX06879，6=2+2+2标准，拟Only。** [exact-v1](https://arxiv.org/html/2602.06879v1) §4.1–4.5/T2–7及C/D/T10–11必要源实际读。逐阶段head/dim/SSmerge/staticLN、ResNet T/4 hybrid RoPE/PTD，再以冻结denoiser前三层prompt-state蒸馏T5；superweight解释是假说非因果。训练480k双caption再teacher生成/recaption、多阶段调step4→8→10，不同模型参数与生成步数不是iso-quality/budget；C每阶段80epoch+20E2E、48H100×10h/iteration。PTD全时质量反退，textcodec T6 DPG/Geneval下降与T5多指标低于teacher，OneIG排text/reasoning两项不称完整能力保留。§4.2 block数/原depth文字不一致与主文2.4/结论2.3B保留，不抄广headline。S25U/SM8750Hexagon、512²/10step，T7 denoise与T5Large15ms/VAE160ms分账；precision/batch/冷启与峰memory/CI ND，非任意手机SLO。新增有限视觉蒸馏/资源工作点可报告，非一般表示同一性/质量守恒，无新Books。

### 末批第五组三项必要源 ready（待root）

**Steering-Identifiability06801，6=2+2+2受影响保证必要深入；拟限定经验Only，中心强保证隔离待root。** [exact-v1](https://arxiv.org/html/2602.06801v1) §3–6/8及B2–3决定性条件已读，不遍历全部识别proof。A3仅rank≥k，不保证固定θ的共同非零ker；B2承认只有dimN≥1才成立，effective-rank小不等exact-null。B3重参数同时换后续权重，不能证明原冻结模型的两个vector严格同output；random orthogonal于v不等属于kerJ，词汇/句长φ近似相同不等完整分布相等。Qwen2.5-3B层12/2048与Llama3.1-8B层16/4096，三trait/50pair/100heldout×10generation、5/10扰动seed及formality四strength，实际6.3只有限score接近，不采“任意α/所有prompt严格同分布”。§8明确lexical heuristic、local linear与ICA/RIP/multienvironment成本，新增可靠识别方案未实证；hardware型号/precision/全search成本CI ND。不因局部保证问题推倒有限经验，但不正面采用Prop1原普遍保证、不写Books；是否中心Disputed由root判定。

**ScaleEnv06820，6=2+2+2标准，拟Only。** [exact-v1](https://arxiv.org/html/2602.06820v1) §4.1–4.2/5.1–5.4/T1–5、AppA/B2/C实际必要源已读。schema/code/tests同生成链，success/rejection检查可修tool或DB；BFS扩依赖并执行、Oracle BoN16估feasibility及LLM过滤不等全部可行路径/独立真值。DB终态规则与动态ID/文字例外为有限可验证task设计，不授生成环境真实正确性。Qwen3-8B/32B、1024/2048 rollout、48steps/lr1e-6，16domain约50tool/5–20tables；AppB2披露每domain约546k、每task93.2k token，不能称零生成/净teacher成本。相同1024task的domain数量比较未配平难度/生成成本；T1 32B Airline48持平，T3去EV也去迭代修复，t-SNE不证明污染排除或独一机制。四次pass不是生产guarantee；hardware/precision/seedCI/净预算ND。局部生成与规则验证取舍可报告，未新增独立执行正确性/长期外部事实机制，拟Only，不因recipe未列造gap。

**POP06822，6=2+2+2标准，拟Only。** [exact-v1](https://arxiv.org/html/2602.06822v1) §3.1–3.4/4–5/T2–7与A1–2实际必要源已读。prefill分R/C/P、decode仅C重选，P永久不恢复；两阶段up/gate再selected-down计算不是免费mask。FFN-only保留attention、较高FFN sparsity对齐总参数；A1混称FLOPs，不能授匹配全部成本。A6000、quality b10 LLM/b1VLM，T5 Llama2-7B128input/128output CUDA event有限E2E：40%时POP2.21s慢于PP2.14；T6全channel重选质量更好但开销更大，γ .1仅所选取舍，2.85%分母是dense FFN非整服务。A2 baseline C4 2k×1024/4096、Týr FineWeb1k×4k，POP无离线校准仍有在线prefill/候选成本；T2/3质量非普保。precision/latency batch/并发SLO/独立seedCI ND，不采摘要1.29×为通用E2E。新增局部三分执行替代可报告，未建立一般后续token安全裁剪/新生产合同，拟Only无Books。

### 末批第四组三项必要源 ready（待root）

**CodeSSM06774，5=2+1+2标准，拟Only。** [exact-v1](https://arxiv.org/html/2602.06774v1) §3–5/T1/6及AppA4实际读。12层双向S4D、每方向single kernel跨channel共享，DirectProbe AST/DFG heldout nearestcluster与FFT centroid/LHFR显示fine-tune任务相关变化；阈值按所见profiles定、缺RoCoder末两层不收敛，不能认作完整机制因果。新增局部highfreq CNN k3/group8，同时减11层抵参数，以及8/1024kernel同时变capacity；8先small-data多kernel搜索后重训，非只隔离频率/no额外预算。A4四A10080GB/Wiki128/b256三天→1.8M issue10epoch→1.8Mcode256/b64/lr5e-5/cosine-warm300，所用预训少于旧CodeSSM；1024kernel SQA76.01低于baseline76.08，8局部最好不授所有域/SSM比Transformer普优。precision/fine-tune完整配置/seedCI/净搜索资源ND。可以报告条件诊断与局部替代，不把频率观察升级所有SSM状态能力/因果新合同，拟Only不因小编码器拒绝。

**SquaredPO06788，6=2+2+2标准理论，拟Only。** [exact-v1](https://arxiv.org/html/2602.06788v1) §3.1–3.2/4/5/T1–2/Limitations、AppB必要源实际读。continuous f/C1正域/边界导数极限−∞是DPO-inducing条件，general divergence不要求convex；same BT pairloss可以来自只对in-sample regularize的目标，不等全响应状态保持。Lemma2 unique min c≤1及outside高reward假设才推出in-sample缩减；argmin≥1仅抵抗此最优解退化必要选择，不保证optimizer或所有winner不降。Squared(logratio)对应β/ratio，实际exp差clip50防数值overflow非无限理论同物。Llama3-8B/TLDR92.9k、LoRA16/32/.05、lr5e-7/b64/len2048/β.01/AdamW4epoch、BF16/4A10040GB，512val GPT4、AE用gpt4o/10seeds errorbars；seed是否独立training不额外断言。T1首epoch DPO反好、T2 DPO略优、AppC1 STEM反側，winner仍降只更少，不授能力/安全保留。onlylimited理论条件与实例，不因nonconvex新命名造长期gap；中心guarantee限定最优抽象，拟Only。

**FSL06797，6=2+2+2标准理论，拟Only。** [exact-v1](https://arxiv.org/html/2602.06797v1) §3.1–3.2/4/5/6实际必要假设与结论读。feature linear regression/independent Gaussian noise/iid one-pass/zero init；hypercontractive与powerlaw spectrum/target、noise-dominant/stability小LR、SDE FSL只是采用前作模型，不是本轮LLM实证保证。Th4.1在固定N/允许LR上界变分：easy s≥1−1/β powerdecay exponent2β−1、hard prolongedstable+vanishingtail；Th5.2–3 fractional尾γ capacity α=min(β,γ+1)、边界logfactor，exactoptimalshape≠只取得optimalrate。Th6.3 discretekernel与源/容量约束：easy匹配minimax、hard只one-pass SGD最优不是全estimator minimax；γ条件与constant需保留。硬件/precision/LLM训练预算不适用此理论命题，不能据kernel条件发生产schedule，无全proof认证/普遍cosine失败；Ch28有warmup/decay依optimizer/budget及有限校准，新增条件taxonomy暂未改变实际长期LLM配方选择，拟Only，不因AIforScience affiliation排除纯模型优化理论。

### 末批第三组三项必要源 ready（待root）

**Watermark06754，6=2+2+2标准理论，拟Only。** [exact-v1](https://arxiv.org/html/2602.06754v1) §3–5/6、AppA/C4/D5实际必要读。固定hash/detector的token-level期望score优化，不是联合/sequence最优power；hard约束每g、soft约束对G平均，新增PPL方案的quality只是代理。D5 iid连续score/有限一阶moment/finiteΣ/feasible条件只证明“存在”support1 optimal，不是所有soft方案必然确定；主文措辞更强，隔离不采。重复prompt固定key下diversity与平均无distortion不同；1000ELI5×200token、Llama3.1-8B16bit/temp.7/topk50、Qwen3-30B8bit PPL，100prompt×100重复的trigramSelfBLEU/固定TPR.95及1%FPR有限测量，非semantic diversity/改写抗性保证。C4caption Ministral、method Llama的identity冲突保留，accuracy三任务平均不授每项普保；硬件/净求解hashcost/seedCI ND。Ch72 L1048附近已明确平均key/message不认证条件质量，固定key重复维度是更细评价，但当前未改变实际来源归属或可靠性机制；拟Only，不叫exactExisting/新Books缺口。

**NES06759，6=2+2+2安全必要深入，拟Only。** [exact-v1](https://arxiv.org/html/2602.06759v1) §2.1–2.4/3.1–3.2/4.1–4.2/6/T2及AppD实际读。新增recent-view/undo仍在editbuffer/LSP依赖和transactional替换缺安全配置的有限failure路径，不执行攻击/不复制payload。CodeQL top1000Java→手工构造410独立cases，Zeta每场景10重复→4100，不当4100独立project；黑盒四IDE120case单次→480，case不matched model/检索/预算、reload只是作者清history非因果控制认证。T2各vector非所有模型更差（Zed编辑历史0、commercial autojump较低）；无suggestion不能认证修复，但debounce与用户低警觉属作者归因/问卷，未分离受控UX因果。blackbox精确IDE/model版本、hardware/precision/fullinput-output/budgetCI ND，不能将Jan2026版本事实外推current或所有NES，亦不据JSD授显著无变化。既有context provenance/effect审核原则不等此实例exactExisting；局部版本测量未建立新runtime enforcement/外部回执契约，拟Only，不按安全词/owner缺配方造gap。

**R-Align06763，6=2+2+2必要设计反侧深入，拟Only。** [exact-v1](https://arxiv.org/html/2602.06763v1) §2–5/T1–5/AppC/D实际读。label-correct∧MetaRM-rationale-aligned是具体诊断/训练分解，gold rationale由Gemini3Pro conditionedlabel或整合人审生成；同teacher产gold又评、GPTOSS120B训练meta选择对GeminiF1，不能认证真实内部causalreason或普遍soundness。AppC只53 HelpSteer3/Qwen14B label-correct样本人审，不授全benchmark可靠率。8/14B RM PPO同hyperparameter声明不等同总teacher/runtime预算；下游Qwen8B、Arena prompts+Step3-VL10B固定reference/+1−1与动态lengthpenalty，净teacher成本/hardware/precision/lrstepsseedCI ND。T4RAlign8 IF26.9低于RLVR30.3/base32、14B coding49.4低于RLVR50.1，且多项base更高，不能称能力保留或所有域赢；§5.3相关含自己训练family，不识别唯一rationale因果/外推保证，§5.2恢复数值与列名文字冲突不采。新增有限evaluator与配方可报告，但未支持长期审计真值机制或比既有critic/trace分账更强权限，拟Only不造gap。

### 末批第二组三项必要源 ready（待root）

**NanoQuant06694，6=2+2+2标准，拟Only。** [exact-v1](https://arxiv.org/html/2602.06694v1) §3.1–3.3/4.1–4.6/T2–7、AppC/E必要配置与反侧实际读。双binary低rank factor与两channel scale；KFAC-diagonal预补偿→ADMM/SVID→STE→冻结binary后全局scale/logits蒸馏，属具体PTQ工作点，不授global optimum。128×2048 WT2校准、各重建8epoch/400ADMM步/seed0/H10080GB，WT2 PPL存在校准任务重叠；QAT结果/训练量引用不同，baseline checkpoint bytes部分由公式估算，不是实装公平资源比较。T3/T4/T6/T7 PPL改善≠zero-shot普保、低成本≠同质量；最低bit大量准确率损失，局部精度/补偿消融非单调。AppE两段packed uint32解码：GEMV FP16/BF16非TensorCore、GEMM走TensorCore，两次factor中间量与rank不免费；128input/512batched-output、batch1 decode/不同batch GEMM、TX2/3050/A100/H100，PyTorch BF16/FP16参照不授任意engine/SLO收益。存储模型含FP16scale假定，训练precision/完整搜索与生产净cost/CI ND；不采ADMM单调到全局最优。Ch49既有binary-factor、inner-rank与执行开销边界不是此PTQ exactExisting；局部训练配方不自动新长期gap，拟Only。

**Grokking06702，5=2+1+2必要设计反侧深入，拟Only。** [exact-v1](https://arxiv.org/html/2602.06702v1) §2.1–2.4/3.1–3.2/4/5Limits及AppC必要方法/反侧实际读。mod-add p113、单层128宽/4head/MLP512、fullbatch10kepoch/AdamW lr.001-wd1、5seeds；LN置MLP或QKV有路径差异，10k内未泛化不证明永久失败。readout scale与lr联动调η0/α²后原趋势反转，wd也随η改变；MSE-SGD比例与CE/AdamW近似分开、epsilon及训练阶段条件不授全部LLM相同动力学。MLP scaleSR只是观察，不是反传处理；prelogit ER谱相关、5seed取min聚合压slingshot不当普通平均/唯一因果。hardware型号/precision/CI/完整search成本ND，小模型反证不因toy拒绝，但仅受限优化与评价混杂判断；无新一般LN或可执行可靠合同，拟Only。

**F-GRPO06717，6=2+2+2标准必要理论/设计反侧，拟Only或真实窄差额待root。** [exact-v1](https://arxiv.org/html/2602.06717v1) §2.1–4.3/5.1–5.5/T1–2及AppF2/H/I实际读。iid二值reward中active mixed与指定rare-correct未采到是不同事件，tailmiss=(1−τ)^N−(μ−τ)^N−(1−μ)^N；categorical-softmax一阶/线性更新不推广sharedθ长期LLM。focal(1−X/N)^γ用成功率proxy，不观测实际rare mass，不认证稀有正确模式保留。39202过滤训练样本、16H100/FSDP2、10epoch/256GB/64minibatch/lr1e-6、γ .5/1/2以best-math-pass1选择；noKL、长度3072/8192、AdamW/一次PPOepoch等并不等全部调参净预算。AppF2训练256prompt×800base-rollout正确轨迹按length-normalized NLL取top1%=1263，是fixed proxy非穷尽稀有解；AppI 1024生成→256 paired50k重采不等独立training seed。N2/8/32 pass1与pass256非单调、F8 math pass1低于GRPO32、KL math pass256更高，不能授普遍兼得；precision/独立seedCI/净costND。实际Ch33 L319–338已有group混合稳定/成功率与随机coverage，L185–203已有unsampled负侧和RewardingRare簇；尚需root判断“mixed只使update可用、不认证rare-correct覆盖”是否真正长期增量，而非把局部focal缺章转gap。未申请写锁/未写Books。

### 末批首三项必要源 ready（待root）

**SLR06665，5=2+1+2标准，拟Only。** [exact-v1](https://arxiv.org/html/2602.06665v1) §3.1–3.3/4.1–4.5/Limits/AppA1/T1实际读。共享架构pre/post checkpoint区间整层恢复，CRC单token已知valid set的条件entropy与valid mass分开；20prompt×两类、qmin=.9×post而非任意quality保持。A100不batch搜索30/45/60min，search非零成本；proxy-soup 21个alpha搜索非同搜索数量。三7–9B、固定min-p.1/T1、100writing×32、40QA×128，GSM8K仅各模型greedy失败100题×64，不授全任务推理收益。Gemini2.5Pro judge/canonicalization可能漏未列正确答案，embedding diversity不是正确性。T1多项poem/story与Gemma joke质量下降，Early/Late恢复仅QA对照，不能称所有行为定位同层或安全保留；max4096/QA64，precision/seedCI/全搜索与生成净costND。局部可选checkpoint干预不改变长期posttraining或可靠性合同，不因缺配方造gap、不冒充Existing，拟Only。

**Graphon-PaI06675，6=2+2+2标准理论，拟Only。** [exact-v1](https://arxiv.org/html/2602.06675v1) §3.2/4.1–4.4/5.1–5.2/6.1–6.4实际读。one-hidden-layer/squared loss/固定label与Gaussian初始化；factorised saliency收敛依d,n共同增长、bounded row profile、neuron CDF、conditional iid edge noise与稳定threshold；SNIP entry影响渐消是近似桥梁，GraSP此处magnitude变体非原signed任意结构。UAT限active k坐标、正measure rectangle/edge floor与αn p^k→∞，不是全ambient能力或算法一定找对任务feature。NTK lazy与λmin>0、i.i.d.S，yᵀK^-1y/路径上界不自动准确率/硬件加速；n4096 binaryCIFAR10代理，高density≥.7 curves接近或反转及过集中spectral collapse保留，hardware/precision/全训练资源ND。条件理论贡献不因非LLM排除，未将宽limit授实际foundation剪枝新保证；有限asymptotic taxonomy/边界可报告，暂无可直接改变长期可执行选择的增量，不自动Books。

**DAGVul06687，6=2+2+2必要安全/设计反侧深入，拟Only。** [exact-v1](https://arxiv.org/html/2602.06687v1) §3.1–3.3/4.1–4.5/T3/4/6与必要Limits实际读。rootcause/verdict分账有具体评价增量，但semantic-preserving实为g++编译+三LLM多数非执行等价证明；GPT5 MATCH judge只抽200 MISMATCH（10.9%）人审，3%不能授全池precision/recall。T3 vulnerable要求label+MATCH、patched却将falsepositive+MATCH重归TN，非普通同分母F1。DAG source/intermediate/sink与parent-order/closure是结构规则，final reward仍DeepSeekR1对gold judge，不认证program causal truth；gold生成也给groundtruth，regex/similarity过滤不排leakage。8157 SFT3epochs→2178/4096筛RL2epochs/rollout16，多阶段成本非同预算；8A80040GB，precision/seedCI/完整lr/batch与净成本ND。T4 Claude hinted扰动反更好、T6 DAG-only局部弱于CoT，保留非单调。具体diagnostic/训练替代不足通用可靠审计或proof-carrying执行机制，不新Books、不因安全主题自动gap/全proof。

### 新准入三项最低必要审阅 ready（待root）

**SiTok06602，拟5=2+1+2标准Only。** [exact-v1](https://arxiv.org/html/2602.06602v1) §2.1–4/3.1–3.4/T1/3–5实际读。mel50Hz/128bin→stack4/12.5Hz、VQ32dim/65536EMA、16层causal encoder/4层CTC/16层noncausalFM decoder、Vocos24KHz；直接CTC transcript监督取代额外ASR语义encoder是局部低rate双用途条件。intro L73作者明确披露2 million hours of speech data；方法另一处省略单位，保留作者申报而非独立数据核验；一epoch约450ksteps/AdamW8e-5/32kwarmup。SeedTTS-test-en whisper/WavLM/UTMOS、DASB与1B ASR/LibriSpeech-testclean，T2baseline部分借外部数不全同训练。去CTC WER33vs4.06，CTC过大也反退、XL重建改善但ASR/SV反侧、6.25Hz collapse与R+D-only decoder WER5.73保留；TokenCFG/WER改善伴SIM下降、额外forward成本，不授普遍兼得。shortcut RTF未披露绑定硬件/precision/batch/全部训练搜索净cost/seedCI，不采用E2Eheadline或全理解生成保证。Ch23 L180–196已有语义约束/重建分账与双路径共存，非SiTok exactExisting；该局部CTC+FM/codec工作点不改变长期表示合同，不因未写此配方造gap，拟Only。

**HuMI06643，拟5=2+1+2标准Only。** [exact-v1](https://arxiv.org/html/2602.06643v1) II-A–C/IV-A–D/V/VIII、必要AppE/F实际读。unscaled人类taskpose+IK preview；previous scheduled target锚actionchunk减lag反转、blind pelvis/feet只relative reference displacement防global drift。IV-C换actual EE参照75%(15/20)→40%(4/10)、IV-Dabsolute pelvis75%(15/20)→0/10为具体局部接口反侧，样本量不同、single G1平台/控制器task-specific、追踪依赖texture/light不授所有机器人稳定/安全。高层Diffusion5Hz、controller50Hz，F双224图/20Hz观测/48actionhorizon、200epoch/b256/10denoisestep/lr3e-4；E teacherprivileged→DAgger student25步history/10waypoints2s、reset与speedrandomization额外训练。hardware/precision/独立seedCI/完整sim+示教净成本ND，20有限rollout不授99%生产。Ch26 L106–132已有多时标proposal/controller与body calibration/漂移停机分责，但不是此接口exactExisting。该受限scheduled-vs-observed trade-off是局部替代，尚不支持长期安全或一般参照规则改写；拟Only，不因robot-free/小scale排除也不自动gap。

**CineScene06959，拟5=2+1+2标准Only。** [exact-v1](https://arxiv.org/html/2602.06959v1) §4.1–3/5.1–4/T1–3实际读。20pano-view/VGGT image+camera features加和、resize/project后与noisyvideo/sceneimage concat；需desired camera但不需source显式cam，fixedFoV不推广varyingintrinsics。首context固定、其余shuffle针对ordered-position shortcut；context-vs-VGGTloss给dynamicforeground局部反側，不授隐式3D真值/世界persistentstate。internalT2V/10kstep/b16/lr5e-5、384×672/77frame/50采样步、300heldout/50OOD；samebackbone重实现contextbaselines但不同3D/camera baseline设置。T3ordered matchingpixels4673.67>shuffled4617.51、progressive RotErr2.5757<shuffled2.6825，非所有metric单调；T1CLIP-T弱于FramePack，10.17×速度未绑定硬件/precision/全VGGT成本/CI不采用。原static/dynamic decomposition与生成condition设计是有限配方，不转长期可执行3D一致性或安全机制，拟Only、不造recipe gap/不复查全附件。

### 已准入四项必要审阅 ready（待root，不自批）

**Confundo06616，拟6=2+2+2安全必要深入Only。** [exact-v1](https://arxiv.org/html/2602.06616v1) §3–6.3/6.5及T2实际读；只审fragment/query-shift命题，不执行攻击或复制payload。作者假设攻击文档被ingest、不可查询target；Qwen3-.6B/三个surrogate embedding、40token单注入、target bge-small/Qwen3或Llama3-8B、chunk128/top3。训练random split只取prefix/suffix较高reward，不证明每fragment都有效/任意chunk安全；hallucination reward ROUGE阈值与substring target、sentiment classifier不是语义真值。6.2 chunk较大稀释攻击、unseen query83→74与paraphrase88→73反侧保留；T2去Pipeline91retrieval/62vs59ASR、去其它目标同时改语义/流畅度，不唯一归因chunk机制。warmup8sample/temp.7/minmax+GRPO；hardware/precision/全部steps/独立repeatCI/净训练与targetsearch成本ND。具体负侧成立但仅有限测量，不授通用防线失败/无需上传条件，不按Ch72未写此recipe造gap；拟Only无Books。

**TrapSuffix06630，拟6=2+2+2安全/保证受影响深入Only。** [exact-v1](https://arxiv.org/html/2602.06630v1) §3–5.3/7、T1–3必要源已读。random-vs-trap hinge排序/线性安全项/gradient attraction及nonrefusal-safe对比是局部训练防线；不从这些loss授成功攻击必含fingerprint。ASR实际定义为harmful AND evade tracing，不能称伤害率<.01%；T2仍124真实jailbreak/109traced，Probe仅1/5 traced，trace≠block。80thpercentile文字与实设α0、GCG25prompt/adaptive100%trap blacklisting产生0WithTraps/0trace且未成功，不证明未来trace必然；FPR是攻击者停止误判，不是benign用户falsealarm。三模型LoRA8/alpha16/dropout.05/q/v/40epochs/lr5e-5/4A4048GB，JBB100和Dolly15k；GPT4o judge>5、utility三benchmark非逐能力/外部安全，precision/seedCI/完整净成本ND。canonical iterative suffix限域、非semantic攻击保证，模型adaptation付成本。只保留有限经验不采inevitable/硬trace保证、不造Ch72配方gap，拟Only。

**PACT06650，拟5=2+1+2安全必要深入Only。** [exact-v1](https://arxiv.org/html/2602.06650v1) §3.1–3.3/4.1–4.4/T2–5/Limits及G实际读。self-distill→global先判/earlyexit→user Label2Action为训练出的CoT序列，非法global设置只通过adversarial训练样本映射REJECT，非独立runtime hardgate；原nonoverridable/100%一致性与G+/S .833直接不授全局安全。Qwen3-8B/573435样本、自分类/自响应，CoSApien200去21partial/PACT-test5361内部生成customlabel随机mapping、三judge安全多数/两judge helpfulness非独立真值。GUIDE较REJECT安全下降而helpful升、woCoT也改变reasoning/data，不授唯一因果；Limits明确taxonomy灰区、label/chain injection及串行error，CoTtoken成本尚待优化。G给8H80080GB/lr1e-5/3epoch、temp0/top-p1/top-k1/max5k；precision/seedCI/净总成本ND。局部control经验不改变硬权限/执行责任长期原则，拟Only无Books。

**SameAnswer06652，拟5=2+1+2必要设计反侧深入Only。** [exact-v1](https://arxiv.org/html/2602.06652v1) §3–5/T2–4/7–8/Limits和A system/setup实际读。loglikelihood选option与五末layer probe位置分开，predicted-topmargin不是correctmargin；output不变而drift观察不证明latent“先于flip”或后续fragility因果。semantic/random/box同geometry可分部分overlay因素，R→W/W→R并存；control drift只是随机其他images非语义边界，Dirichlet差与失败相关不认证空间信息丢失。POPE blank近全No，扰动FP减伴recall损，不授去languagebias唯一因果/通用收益。四disjoint3500 subsets不等四seed，A固定seed0；单A10080GB FP16/b4、32B四A100，MMMU表847与3000同split计数不静默统一，净probe/搜索成本ND。局部VLM质量/内部geometry反证支持报告，未建立新可执行robustness验收或修复机制，不冒充Existing/未列配方gap，拟Only。

### 末批六个局部4分关闭提案（待root）

均按完整AB具体新增局部实现评1+1+2=4，不借成熟principle加分；原日期字段保存在`feb10_all_selected_date_raw.json`，此前官方v1身份/版本说明已实核，没有可见撤回标记。未标准实证/未核实现，不采用性能headline；本日统一公告下界Feb09 01Z，右界各registered秒+1。06714 PrefIx submittedFeb06 14:02:42Z/registeredFeb09 02:48:31Z：interaction-as-tool、31偏好与UX judge为局部benchmark，未新增可靠偏好治理边界。06806 RAIGen submitted15:54:41Z/registered02:50:40Z：MSAE频率+distinctiveness的rarity score是局部合成替代，不授罕见能力因果；后May/Jun版本窗外。06862 inventory ParaX/official AdaRoute为同family，submitted16:50:38Z/registered02:51:59Z：shared parameter centers/input router的局部PEFT，不授跨任务无干扰，May v2窗外。06924 LEIA submitted18:18:13Z/registered02:53:23Z：error-subspace classifier logits为局部鲁棒替代；v2 Feb09 02:55:15Z提交的最早公告恰在本窗终点，不纳此重要修订。

06795 rubric-gen，submittedFeb06 15:51:52Z/registeredFeb09 02:50:25Z：[exact-v1](https://arxiv.org/html/2602.06795v1) §4.1–2/5.3 L144–222已实际核20%gold预算决定性事实。200错误trace由Claude3.5Sonnetv2产rubric、NovaLite逐item judge；所有模型先用1.6k gold SFT，RL1.4k、20%只该RL子集而非全部gold/teacher成本。Qwen3-4B/1epoch/1e-6、RL8A10040GB、response5k/10k、highest-val checkpoint及shorttrace penalty同时变化；math rubric15.2低于VR16.1，coding complete20不等correct2.5。不能把相同预算标签或20%外推全训练降本；新增实现仍局部4，不为补字段再读全附录。

06942 Turkish pretraining，submittedFeb06 18:41:14Z/registeredFeb09 02:53:48Z：[exact-v1](https://arxiv.org/html/2602.06942v1) §6.4.1–2 L696–710实际核matchedbudget必要事实。WordPiece vocab2k–128k、5/20/80GB，全部BERT配置在Alldata、TPUv2-8/1M steps/seq128、packing；fragmentation改变walltime，不是matchedparameters便同compute。受控corpus/tokenizer诊断是局部实现条件，不因Turkish或小模型拒绝；尚未建立新的普适资源选择边界，拟4关闭，不采equal-E2E-budget收益。

### 决定性方法事实（已读即停止准入核；待root裁决）

06593 AgentStepper，[v1](https://arxiv.org/html/2602.06593v1) §3.3.4/3.4/T1 L174–200：四个LLM/tool前后断点，可改prompt/response/args/results；逐tool git commit只workspace记录，传统debugger/liveediting的局部应用，无新副作用恢复/可靠性条件，拟贡献前关闭。06623，[v1](https://arxiv.org/html/2602.06623v1) §3.3–4.3 L134–223：masking classifier毒性标签、normalized gradient SVD、h−βPh；W0(I+A)包含性/Ph=0 locality为成熟线性代数，不自动行为/安全保持；具体新增未改变原安全判断，拟贡献前关闭，不全proof深审。

06602 SiTok，[v1](https://arxiv.org/html/2602.06602v1) §2.1–4/T1/3/§3.3.4 L80–132/155–209：mel/FΜ/VQ组合不单独加分；12.5Hz单码本低rate加CTC直接transcript而非额外ASR encoder、去CTC的intelligibility严重反退及大模型reconstruction/understanding非单调，具体低rate双用途取舍可准入，拟5标准继续必要配置/反侧。06643 HuMI，[v1](https://arxiv.org/html/2602.06643v1) II-A/B/C L98–137：human unscaled task pose+IK preview；tracking lag下以上一scheduled target而非executed pose锚actionchunk、blind keypoints仅relative chunk防漂移是具体接口增量，拟5标准必要反侧，不将capture+hierarchy本身当贡献。

06724 TaS，[v1](https://arxiv.org/html/2602.06724v1) §3.2/4/Alg1 L129–203：Pending/N-A、ExpandRows/PopulateCells、DB Append/Update与LLM CheckSaturation只显式表组织，没有新的事务一致性/恢复可靠机制，拟贡献前关闭。06843，[v1](https://arxiv.org/html/2602.06843v1) §3.1–2/4.2 L64–110/134–155：已给完整算式/量词句、数字1–9的activation与PCA/SVCCA/Procrustes观察，非计算/任务切换因果；几何观察可局部贡献，拟4关闭，不采no-interference/计算机制，不因小模型或数学范围拒绝。06959 CineScene，[v1](https://arxiv.org/html/2602.06959v1) §4.1–3 L112–141：VGGT/camera融合concat不借分，但ordered pano shortcut→首image固定其余shuffle以及context-vs-loss的dynamic反侧支持具体condition-factor选择，拟5标准继续必要评价/边界。

06718 GhostCite，[v1](https://arxiv.org/html/2602.06718v1) §3.2–3.3 L168–195必要method已读：GROBID→SQLite title cache→DBLP→Scholar/Search→Qwen3Flash reparse→Levenshtein θ.9 maxmatch是成熟存在性级联，不核claim support；现象统计/问卷非受控模型因果，安全错误信号不足新可靠性机制，拟贡献前关闭待root。06836既有concaveNE的人群社会策略应用与06923科学定律发现本次暂停，root实际完整AB排除通过；原证据保留，不借通用owner绕入。

**Degradation06586，拟5=2+1+2标准Only。** exact-v1 III-A/B、IV-A–D/TI–II实际读。ResNet18/128d、CIFAR10/100，central1000epoch与CL 500+250/500+150+150/500+4×100不是等全部训练量；batch512/lr.5、buffer200/800、100epoch linear eval。NCI保isotropy而随experience降accuracy、SupCP高isotropy未同优；IsoScore* regularization在CIFAR10五experience有几何读数升而准确率大退，也有TI/II有限轻改善与std内例外。非单一isotropy因果或所有regularizer失败，hardware/precision/repeats数量/净成本ND。负侧准入不因小模型关闭；实际Ch12 L296–322几何诊断/能力分账已读，不叫exact-Existing，局部continual迁移反证拟Only，无新长期机制差额。

**Echoes06600，拟5=2+1+2标准Only。** exact-v1 §3.1–3.3/4.1–4.3/T1/4/5与必要A4实际读。Echo-free条件分布是形式定义，实际raw-vs-trim pertoken/suffix gap不是其Z或行为距离；错误组suffix收益反更大，likelihood不等正确。同prefix50%/同seed插提醒vs不插，base无收益；paired teacher traces编辑/删echo后gold筛选、175vs136训练tokens非等tokenbudget，Deepseek GSM8K ED退于normalSFT。vLLM/temperature0、7k SFT同step非同tokens，hardware/precision/numeric训练配置/全teacher成本ND；A4 first32word QwenEmbedding0.6B+32hidden MLP、GPT4.1/similarity标签及200人审，只识别EOP非correctness，不能授准确span/predicate oracle。attention相关与局部提醒干预不识别唯一middle-layer原因；限定数学echo作为可尝试替代，不新增通用context可信性判断，拟Only。

**Overlap06627，拟5=2+1+2标准Only。** exact-v1 §2.1–2.4/3/T1–3/4及必要AppJ1/2实际读。sqrt-density/BC/Hellinger是已知几何，新q=sqrt(r)一阶surrogate/clipping/penalty；absolute continuity/supportoverlap、nearq1展开与finite normalized advantage限定，不等任意tail界或globalmonotonic。MuJoCo/DM9seed，Procgen25M/3seed/25episodes；Ant/cartpole/TRPO或PPO反更好，Procgen混合/penalty敏感。AppJ大epsilon/LR可BPPO崩而PPO成功，文称MountainCar、T9/10标CartPole的身份不一致保留，不用数值跨环境推广。训练hardware/precision/fullstepbudget/净耗时ND；未LLM实证不否认优化主线理论关系，也不据控制实验授LLM质量/安全。Ch32既有ratio/clip/referenceKL分责不等此具体替代Existing；拟Only，不造geometry recipe gap。

**ThinkProprio06575，拟5=2+1+2标准Only。** exact-v1 HTML §3.2–3.4/4.1/4.3–4.4/5/T6–8实际读。原题摘名称State-Grounded Visual Token Selection，HTML同v1题名为Embodied Visual Reasoning，记标题差异不重算家族。[-3,3]/256bins复用词表末端，instruction+proprio引导视觉vote，Gumbel/STE与均值globaltoken；selector O(Nv²D)，非大token通用免费。FLOWER/Florence2、50k步、4090/bfloat16/双相机/4动作steps、5评估runs；T6无globaltoken性能反退，T8instruction-only/proprio-only保留率不同，非等budget因果隔离。T4 VRAM略增、T3并非LIBERO均分最好，T5包括selector/VLM/action但不含真实通信/controller deadline。5分局部受控state-entry/selection增量不建立新安全或表示权责；Ch26已有观测/action闭环但不冒充exact-Existing，无新Books提案，真实AppD仅preliminary未采全任务泛化。

**Latent Rethinking06584，拟6=2+2+2标准Only。** exact-v1 §2.1–2.3/3/T1/4实际读。64latent/2层prior encoder、8层decoder/hidden1024/w64；非amortized Gaussian local posterior在base noise空间16步Adam，Gibbs-style生成自己的trace再最大ELBO、30轮按likelihood择最终trace。384/385k GSM8K-Aug精确主文385k、0.2B从scratch，baseline数引MARCoS非本轮同训练实现；30轮非同inferencebudget，训练hardware/precision/globalbatch/seedCI/E2E ND。§4明确clean demonstrations依赖，likelihood不是correctness或独立verifier，不能据后验fitting称必然selfcorrect/理论全局收敛，formal cognitive解耦非脑机制证明。该局部state优化/解码路径支持额外计算替代，不改变Ch20独立验证/输出commit原则，不造latent recipe gap；拟Only、不用小模型排除。

**FairJudge06625，拟4=1+1+2关闭Only。** root完整AB准入通过具体point/pair跨mode监督，作者再次核官方exact-v1题摘/版本史，SubmittedFeb06 11:35:32Z、registeredFeb09 02:46:27Z；没有可见withdrawal，Jun30 v2不当本窗重要修订。该材料新增judging dataset与curriculum SFT-DPO-GRPO实现，crossmode supervision是局部judge训练替代；不借静态judge不可靠/一致性≠正确性成熟原则增加Design/Reach。4分关闭不照录debiased/一致性或大模型性能宣传，不等标准实证完成；资源声称acceptance后发布不授当前实现已核，不新增Books。待root关闭终裁。

完整题摘原记录为本目录 `inventory.json` 的 `identities[]`，字段 `arxiv_id/title/abstract/source_url`；AB12/13仅当时14项读取批次简称，不另建重复raw。root实际完整题摘准入通过06575主动proprio-query、06584可优化latent buffer、06586非平稳几何反侧、06600受控EOP、06616分片/查询shift、06625跨mode监督、06627overlap尾部替代、06630trap/fingerprint、06650分层策略、06652输出/表示负侧。尚未统一评分：只评实际新增命题，局部可0–4关闭，安全/具体设计反证仅深入受影响内容。06593/06602/06623/06643只核决定性增量，不因方法组合或小模型预拒。

**AgentCPM-Explore06485决定性提案。** exact-v1 §2.2–2.4/3.1/3.3–3.5实际读，复用 `feb10_admission_06485_v1.json` 最小方法缓存。DELLA融合、环境/format/极端长度过滤不单独构成新增原理；摘要“holistic”不自动准入。具体receiver-policy训练intent与task reward共同优化summary消费接口可校准准入，拟2+1+2=5标准Only：fixedagent换strongsummary GAIA60.1→61.1/62.1小幅、summary SFT58.1→60.4及joint RL63.9未独立隔离intent因果。summary不带原问题以避免代答；原问题59→69不是干净受控接口收益。8A800 BF16 SFT/context128K/4epoch、RL32A800 FSDP2/mixedprecision与train/infer presence差别，passK有限oracle多尝试不授97%生产、能力ceil/inference-stability因果。待root必要源/贡献终裁，不预先计候选。

**DAIReS06532决定性提案。** exact-v1 method L87–188、Results190–198、Meta202–241、Discussion245–258实际读，复用 `feb10_admission_06532_v1.json`。最小PC/补空间线性投影，L188作者明确不是ECC；每测试子集新PCA，不授校验码检测保证。meta任务明确why/choose词约束诱导重复，200句与template50/sample300及300T5类分开；无自然事实gold、长度/重复匹配负对照或可校准FPR/TPR，ForestCover inbound低一致反侧保留。安全排除提案为贡献前关闭：poison和诱导文本两个场景的成熟投影应用未建立新的统一检测/因果诊断机制，非要求普遍定律、非因小模型或论文公式争议全家族Disputed。等待root必要原源独立排除复核，不计正式候选或安全认证。

## 以下为保留历史单篇论据

**LIBERO-X06556，6=2+2+2标准，拟OnlyReport。** [exact-v1](https://arxiv.org/html/2602.06556v1) III-A/B、IV-A–D/TII–IV及必要AppB/C/D1原源实际读。MuJoCo/VR MetaQuest3/20Hz，100scene600task2520 smooth-success示教；累计L1local→L2larger→L3topology→L4attributes/unseen→L5semantics并非单因素独立干预，不能从每级落差唯一识别内部spatial/logic机制。任务10rollouts、初态保存、time1.1×人均操作；放宽时间仍有提升且长horizon差，非统一deadline保证。五官方checkpoint各自SFT预算不同：OpenVLA150k/b8/lr5e-4/LoRA32/8process且FiLM禁用，pi0单A100LoRA b32 chunk50、pi0.5四A100full b256 chunk10/30k，X100k/b16/BF16，GR00T60k/b32/acc4/单GPU型号ND；其余precision、seedCI/总训练/真实时延ND。旧LIBERO约90与新L1低不能只归因benchmark盲区，训练/scene/predicate也改变；AppD1 ExactIn z阈值与Upright/Side角度代理不授真实稳定/接触安全。TableI自列2026.01 release非可核首公开，按本日官方原Submitted/registered包络不移归属。Ch26现task/sensor/action/controller与成功/near-miss/期限分责可解释但非本累计benchmark Existing；该有限压力测量与预算/predicate反侧支持局部评价，不证明通用盲区量化或新的独立能力验收机制。保留具体负侧准入、拟Only，不因不同模型/小规模关闭或自动写recipe gap。

**SPARC06566，6=2+2+2标准，拟OnlyReport。** [exact-v1](https://arxiv.org/html/2602.06566v1) §3.1–3.2/4.1–4.2/5.1–5.2/T1–3、6.1–6.2与必要AppA2/A3/T4/A7实际读。IRD先出bbox/points，再以原图+crop重prompt；Qwen3VL/Molmo2 4B/8B、256/512/full与V*/HRBench、XLRS OOD proxy，greedy不授绝对OOD。WBF temp.7/N4/8/IoU.5合并、非重叠全保留，更多crop和第二次读取付费，Molmo2-8B full/512有负侧，不采普遍monotonic/200×E2E。oracle overlap试验不等实际localizer真值，A2紧框漏context/过大低res失细节，proposal不拥有充分性。实际§6是成功trace筛选23k/14k、专用LoRA SFT仅IRD启用，**非摘要RL**，冻结reasoning weights不认证新输入下行为无回归；Molmo2-4B负侧保留。主文2epoch而T4为5epoch不统一，rank16/alpha32/lr2e-4/b32acc4/16bit/context2048、Qwen8B单A10080GB约12h/Molmo约双成本；inference硬件/precision/最长生成/seedCI/完全E2E与teacher成本ND。实际Ch23 L479–485已有lowres全局+crop取证/proposal-sufficiency/预算回退，不是此WBF/LoRA recipe exact Existing；有限二阶段搜索与隔离adapter未建立新的通用视觉权责/可靠预算规则。拟标准Only不造recipe缺口；不外推brain circuits因果或原分布exact KV复用，未核artifact/复现。

最新：World-VLA-Loop/HyPER/LogicSkills/MaliciousSkills/MERGE/SeeUPO必要原源获root非作者终裁OnlyReport，DREAM实际Ch76 L1166/1168、邻接1156–1179与末注1463 POST通过、锁释放；正式75终处置＝64必要core（35 actualPOST+3Existing+26Only）+5low+6Disputed。下方“拟/待核/未授锁”为过程论据不覆盖此终裁。可执行仅明确准入LIBERO-X/SPARC必要审阅与少量决定性准入事实，有限入口停止/实际候选冻结及日级Gate待核，不遍历日期150或496库存；不复读已有效证据。

JADE06486、UATS06493和GRASP06495已获root实际必要原源终裁：5标准Only、6标准Only、6安全必要深入Only，正式同步后68终处置；34POST/3Existing/20Only、5low/6Disputed，无新增Books。剩余ready仅World-VLA-Loop/DREAM-BRIDGE；普通必要审阅仅明确准入HyPER/LogicSkills/恶意Skills/MERGE/SeeUPO/LIBERO-X/SPARC及已具具体增量的待判项，不以混合剩余身份数安排全文队列。

AST06671、FCDP06499、DualMap06502已获root实际必要原源/采用复核：AST与DualMap标准OnlyReport，FCDP标准实际Existing；正式同步后为62终处置，34实际POST不变，不新改书。

最新：Hourglass06471与Efficient-LVSM06478标准OnlyReport、GC2PO06475中心Disputed终态安全隔离获root实际必要原源终裁，已同步65正式终处置；34POST/3Existing/17Only、5low/6Disputed，不新写Books。下方三项“拟”为保留作者论据，现已终裁。

### 后续单项 ready：World-VLA-Loop06508 / DREAM-BRIDGE06526（待root）

**MERGE06552，6=2+2+2标准，拟OnlyReport。** [exact-v1](https://arxiv.org/html/2602.06552v1) III-A–D/Eq4–10/Alg1–2、IV-A/C/D/TI/VI/VII与IV-E/F必要反侧实际读。G按同源component把任务模型分组，组内WA/TA/Ties/BC后range收缩才8bit量化；offlineRF+NSGAII搜performance/storage，再用户先选G，三层MLP task-router让相同chain输入batch。不是任意新输入在线重新merge，也非模型无标签整合：search看validation labels、router最多每task1000/30epochs/lr5e-4；训练免费仅不联合重训source。单RTXA6000/48GB、pop20/300real eval×5search runs mean±sd；ViTB/L、RoBERTa/GPT2/IA3-T03B有限tasks，非因小模型拒收。TI G1/G2/G3按performance/storage代表点而非同storage/equalquality比较；G2 PEFT仍有单task低于EMR，8bit存储式计metadata非峰HBM，source训练/离线search及routerfeatureforward/等待batch/runtimeE2Ecost ND。F granularity/surrogate局部支持，E组件co-occurrence不是MLP/attention语义所有权因果。Ch30 actualL583–595 component/proposal/组合再评价能解释，但非此exactlibrary Existing；新离线搜索/有限bank recipe尚未改变通用坐标/发布或E2E运行设计规则，拟仅报告，不把未写配方当gap。

**SeeUPO06554，6=2+2+2，必要理论保证/实际配置差异深入，拟OnlyReport并隔离未采用保证。** [exact-v1](https://arxiv.org/html/2602.06554v1) §3.1–4.2/Eq3–9、§5.1–5.3/T2–5及AppA2必要条件/B Eq24–33实际读。virtual turn policies逆序更新、teamreward-centered优势、已更新suffix重要性比修正；实际turn samples/no-op pad共享θ、PPOclip .2/batch normalization。理论需要accurate advantage、连续compact邻域/argmax等，B固定单turn替换且后续已更新并冻结，与§4.2共享θ桥梁未证明；Eq8累计不同时点suffix ratios不自动等于最新θ的联合后续policy，不能授真实训练全局optimal/monotonic或无critic必稳。不同group mean含本sample与batch统计只为有限配方，不能当独立无偏oracle。Qwen2.5/3-14B、AppWorld/BFCLv4 avg/pass@4、max10turn、batch32/rollout8/lr1e-6/KL.002/75或50epochs、8H20-96GB（PPO16），相同samples≠相同GPUtime，T3每step约1.2–1.9×，precision/decoding长度/seedCI/全采样cost ND。T4reverse局部胜，不证明全球收敛；T5无normalize低于group/batch且group一项更高，理论与经验不得合并。Ch33 actualsequence reward/token与PRL suffix参考身份分责不是本逆序recipe Existing；方法局部训练分支及受限反侧未建立可移植唯一顺序或数学保证，拟Only，不自动写长gap。只接受同version共享policy到独立turn条件/ratios一致的必要说明或相容artifact，届时定点重开§4.2/Eq8与对应保证；当前不因缺全proof/code阻塞经验限定处置。

**LogicSkills06533，5=2+1+2标准，拟OnlyReport。** [exact-v1](https://arxiv.org/html/2602.06533v1) §3–5.3/T1、Limitations、AppB/C/D/T3实际必要读。FO2无identity、固定controlled-English/noncelexicon、600symbolization/600validity/300countermodel；Z3检查formal gold与输出，GPT4o抽取/repair是上游接口，不授原自然语言或模型内部推理。Qwen3跨三项好、CoT长7.5×只相关；English/nonce近同非无semantic heuristics因果保证。Llama3.2-3B单epochLoRA100k/100k/200k：task提升而validity −4.3/−6.4/−5.7，联合训练增加数据，非同budget的单机制归因。AppD100样本GPT4o元评+人审5flag/随机10unflag，98–99%只有限抽取audit，非独立全量准确率。API Jul–Aug2025，精确APIrevision/hardware/precision/解码预算/seedCI与微调完整配置ND。Ch79实际L157–173已有formal solver/semantic与解析分责，非此具体subskill实验Existing；有限行为差异和负迁移不建立模型内没有符号推理或强制形式化的普遍结论。保留负侧贡献，仅报告，不因逻辑理论/小模型排除。

**Malicious Agent Skills06547，6=2+2+2安全必要深入，拟OnlyReport。** [exact-v1](https://arxiv.org/html/2602.06547v1)实际标题为Malicious Agent Skills in the Wild: A Large-Scale Security Empirical Study，与库存引号标题同family；§3.1–3.5、§3.6验证段/§5.4/伦理及AppA3/D/F/J1/J3/K实际必要读，不抄/执行攻击例子、不打开payload。January两community registry计98380（合并是否去重ND），static4287→dynamic762→两作者rating≥2的157，非全池真实malice率或安全的其余负样本。Ubuntu22.04/Python3.10/Node18与F的Python3.11不一致保留；fakecredentials/2GB/60s/3–5输入，GPT5.2生成测试、AMD EPYC64core256GB/72h局部成本，未核artifact。AppJ的balanced300从原confirmed150+static-negative150(12replace)，5fold与FP计数不授自然prevalence precision/recall；static-negative pool无全覆盖，J3 dormant93.2%与missed1.9%不认证精确整体下界。库存100%removed与正文147/157=93.6%不一致，采用实际正文且不把removal当独立groundtruth。字段/指令风险、shadow behaviors与短sandbox漏触发为作者有限测量反证，非新的hard effectgate；Ch72 actualL249/621 sandbox/观察未命中不授安全可解释但非exactrecipe Existing。限定仅报告局部事实，未采用99.6%/全ecosystem/exhaustive或攻击类别因果安全保证，不以未列Skills配方造Booksgap。

**HyPER06527，6=2+2+2标准，拟OnlyReport。** [exact-v1](https://arxiv.org/html/2602.06527v1) §3.1–3.3/Eq1–6、§4.1–4.5/T2–4、AppA7–18/D clean-cache/E1–4/F1–3必要理论反侧/G T7实际读。confidence为竞争token负log均值而非正确概率；四动作None/SingleToken/Branch/MultiToken与固定手工权重，T64、η.4、reuse λ.1、length/conf .6/.4。SingleToken Gumbel扰当前token两遍expert路由/惩罚复用，再confidence混logits；D deterministic clean proposal历史KV共享，只有当前token随机，保的是cache不随K复制，不授所有memory/latency或原分布等价。第二遍使用先前route usage而不是独立采样；未核实现。main Smax80、warmup16取top10阈值，baseline初宽1.5×对齐Ninst而T2 token实际不同；对DeepConf部分多token换quality，K扩expert按K effective-token计，不据pathcount称同E2Ecompute。四MoE×8dataset、official评分，硬件/precision/maxlength/主decode完整参数/seed及±定义/真正latency ND；E2只温度.5/.7/.9。T3 manual HMMT同quality且不同cost；G强制step-tree负侧局部不是任意search必败。F1错误多数toy可靠，但F2 Eq35的frequency n_a并非跨answer常量，TopK不能消掉，不采用IS/Bayes最优保证；无必要追完整proof。实际Ch79 L210–270已有branch budget/uncertainty非oracle、critic与真实cost分账；Ch21路由诊断非正确性，无exact recipe Existing。新增hand-controller/单tokenroute多样性与有限比较未改变长期选择/可靠性接口，拟仅报告，不把新recipe自动变gap。

**World-VLA-Loop，6=2+2+2标准，拟OnlyReport。** [exact-v1](https://arxiv.org/html/2602.06508v1) §3.1–3.3/§4.1–4.5/T1–5、§5/A1–2/B实际读。35k ManiSkill/23任务的成功与near-success动作数据，CosmosPredict2 action embed+joint latent reward MSE；reward与video共骨干不是独立真实observer。80–100轨迹适配/约50成功训OpenVLA，imagined RL→真实policy rollout添数据；第二轮worldmodel仍从ManiSkill初始化、policy从同baseSFT开始，非一次持续online权重更新。T2每task20validation outcome，reward>.9；T3模拟500rollout、真实Franka/D435/10Hz单任务30rollout，Fig4“realworld”曲线实际simulator。T4去near-success改变人口，rewardhead消融局部支持目标联合正则，Qwen3VL同frames未任务适配，非无混杂因果；>200frames未测，§4.5实际rewardhacking失效保留。H100 node24frames约7s、50update约30h，precision/nodeGPU数/seedCI/净物理成本ND。Ch25 L309–324已有模型被policy利用漏洞、真实刷新/短horizon与06219分责，非本rewardhead recipe exact Existing。有限joint/data增量未建立新的真实闭环验收或泛化规则，拟OnlyReport不借“co-evolving”词造长期gap。

**DREAM/BRIDGE，6=2+2+2，必要评价反证深入，拟Ch76窄评价增量（尚未授锁，不写）。** [exact-v1](https://arxiv.org/html/2602.06526v1) §3.1–3.2/T1–3、§4/§5、AppB1–4/T10–15、E/F/H、I反侧和J/K必要原源实际读。两Llama3.3-70B temp0/R2 opposing→agreement自动标/disagreement三人多数，人审history可能anchoring，T1只non-escalated bAcc，非全任务95.2%；B3 consensus再延五轮spurious不单调减，heterogeneity/更多agent也不普遍好。700query-chunk专家gold与3657query/25retriever top10池分开；296053先经三LLM全判irrelevant过滤至116622，4056分歧人审，不能授filtered negatives无漏。20/25排名变化表明冻结qrel漏标能偏向旧pool；十randomorder leave-one-pool趋稳不授未来全retriever无偏。Hit@10增加但I的nDCG多数下降，不能由新gold直接授系统改善；RAGAlign包括共同失败，相关性不证明真实knowledge因果。T24 L40S48GB×1/4 BF16；generator主文3.3-8B与J4/图3.1-8B冲突保留，GPT4o二元judge版本已报；B2只147样本API价/latency，不含人审与全pool成本。实际Ch76 L1158–1164 corpus/transformation已分retrieval/generation，但未承载qrel由旧检索池生成且未judged≠irrelevant这一测量身份；Ch66一般negative audit非该retrieval attribution差额。拟只融入Ch76此段后：冻结corpus同时保存judged pool/unknown、在将检索失败归因模型知识前定点补未标topK并复验排名/归一分母；保留pool覆盖与judge成本/残余Unknown。不是追加DREAM配方或认为未列某recipe即gap，源/owner待root实核。

### 本轮 ready：JADE06486 / UATS06493 / GRASP06495（待root，不自批）

**JADE，5=2+1+2标准，拟OnlyReport。** [exact-v1](https://arxiv.org/html/2602.06486v1) §3.1–3.6/Eq3/9–12、§5.1/T3/§5.4、AppG人审和§7限制实际读。expert skill选择与LLM生成checklist分开：q相同不保证LLM输出确定；claim检索验证后按dependency低于阈值置零，Eq9也门控负权flaw，不授全score单调安全。BizBench150；GPT5-0807 judge、Google search/url verifier、三次运行，180 reports/30tasks/6models/5experts，人审去高低后均三分。完整JADE相关性上升但仍约15pp inflation，版本/全verification成本与seedCI ND；exact正文未出现库存摘要DR.BENCH，不移植其结论。Ch66 rubric与judge校准实际段能解释但不是该配方具体Existing。有限taxonomy/生成checklist/依赖可靠性尚不建立新的跨域release机制，拟仅报告，非按商业/小样本排除，也不因owner少一配方立gap。

**UATS，6=2+2+2标准，拟OnlyReport。** [exact-v1](https://arxiv.org/html/2602.06493v1) §4.1–2/§5.1–3/§6.1–3、AppA/B证明、D/E/T2和F1–3反侧实际读。MC-dropout PRM均值/方差先筛选、竞争候选再评价，softmax分配verification/expansion预算；RL controller在同policy/PRM组合训练，正确性减cost奖励。Prop4.1需固定OOD概率及每次错误固定终局损失，非任意T真实accuracy cliff；Prop4.2/AppB需iid无偏bounded posterior与增长Kt，不能据dropout自动认证。每candidate相同K的共同UCB bonus不改变该轮均值排序，非部署探索保证。MATH500/AIME24、五policy/三PRM、max256、K0=7、dropout .07–.10；A100校准56token/b4的571ms生成vs32ms PRM转换18:1 cost，不等逐组合E2E。F1去uncertainty也改变feature/valuation，不是唯一因果；T2某配置H-UATS低于DoRA，precision/逐budgetCI/全训练成本ND。Ch79 L246–270已有value/uncertainty/剩余预算及critic成本，不是该算法exact Existing；局部受限PRM proxy校准未改变长期预算/真实verifier接口，拟仅报告，不因公式假设限制撤准入，也不全附件审阅。

**GRASP，6=2+2+2安全必要深入，拟OnlyReport。** [exact-v1](https://arxiv.org/html/2602.06495v1) §3/§5.1–4/§6.1–3/§7.2–3/T3/5、AppB/T7–8与C/T9实际读；正文题为Subgraph Reconstruction Attacks…，库存Graphs Don't Stay Secret…不视为新家族。query-only、已有服务权限/目标身份的一跳typed关系恢复，10query预算，非授权绕过或自然风险率；未执行攻击、不抄prompt。两个各5000doc KG、每图50个degree≥5目标、四chat models；GraphRAG top10entities/relations，chunk1500/overlap100，context12000/output2048/temp0；regex失败才LLM postprocess，P/R/F1人口与baselines格式不同。ID/decoy扰乱字段不等hard-releasegate；T5 GPT4-mini叠ID比单Decoy F1更高，Qwen则降低，故不授普遍composition。utility为同库100doc生成200QA的ROUGE-L，非语义/安全保持；precision/hardware/seedCI及全攻击成本ND。Ch72 observer/unit分账与RAG敏感关系边界能解释，非exact配方Existing；局部prompt防线失败与decoy经验不建立新保密机制，拟仅报告保留安全反证，不自动新增两段。

### 已核单项：AST06671 / FCDP06499 / DualMap06502

### 后续 ready：Hourglass06471 / GC2PO06475 / Efficient-LVSM06478（待root，不自批）

**Hourglass，5=2+1+2标准，拟OnlyReport。** exact-v1 §3/Eq2–5、§4/T1–5与AppA1.1/A1.4/T7已实际读。SwiGLU压缩再展开子块有独立residual，K内部深度与L全层深度不同；参数匹配时需联合dm/dh/K/L，非只倒置FFN形状。T1固定dm/L/attention，质量小幅近同；T3/4 reallocation同时改变dm/attention与FFN，不能唯一归因于hourglass；1B K1/20层而非原16层。T4局部验证PPL较好并非所有downstream更好，T5增K也增67M→175M参数，不授同budget深度最优。A1同OLMo2 Stage1顺序、seed6198、2.5/7/16/21Btokens、RTX6000Ada/B200、AdamW+CE/softmax辅助loss，seq2048/4096；precision、kernel/latency/E2Ecost及repeatCI ND，FLOPs仅nonembedding，搜索预算不匹配。Ch16实际L34–76把expand解释为常见非线性feature支路而非必要定理，L192–208已分相同预算/训练轨迹及结构参数少不等快；并非exact-hourglass Existing。局部参数再分配对照支持可选shape，而“不必固定扩张比”未形成新的长期唯一选择；拟仅报告，不因小模型拒收，也不以局部recipe未列出而加深/写书。主文举例43.19→42.16与T1实际36.441不一致，本轮采用T1原表、不静默修文。

**GC2PO，5=2+1+2，拟中心争议终态隔离，必要命题深入。** exact-v1 HTML §3.1–3.3/Eq3–8/Th3.1–2、§4.1–2与T1，以及官方10页PDF对应p5–7和末页refs已实际读。末token latent加g_m扰动，以answer-distribution稳定及norm比构造episode reward，surprise权重分配到token后truncated-mean组归一再反映射；正常outcome均分episode仍在，并非移除正确性监督。Th3.1将稳定+energy保持授block-identification，Th3.2需noncausal tangent span/B6却口述最优causal policy convergence；高norm常量/answer-insensitive方向不能由给出的norm比排除，条件不能从sametopic多rollout推出。主文所引B3/B6证明、实际g_m实现F及q(answer|latent)操作均未在HTML/PDF出现，PDF实际10页止于refs；不能证原设计process-valid或理论保证，也不自行修假设。4kNumina或919AIME、1.5B/7B、A100、lr1e-6/b256/weights.9/.8，表内结果仅作者描述，训练/搜索预算、M与perturb量、precision、q评估cost/seedCI ND，1.2x图不补实现。只接受精确版本B/F必要段或相容artifact/勘误后重开§3.2及依赖causal保证，当前不正面Evidence、不Books；Ch33现有representation credit proxy不等此具体算法已有覆盖。缺失是限定必要事实，不继续遍历全附件或全版本。

**Efficient-LVSM，6=2+2+2标准，拟OnlyReport。** exact-v1 §2.3–2.7/§3.1–3.6/T2–6及AppC/D/T7/E/T8/G已实际读。每input view独立intra-attn，各层target self/cross读相应input layer；REPA仅训练teacher，不授inference免费训练。固定pose/image/weights下input K/V可独立reuse、新input只encode它，target与cross读取仍付费，T8总latency随views上升不授totalmemory常数。T2 res256品质全面低于LVSMdec-only，res512 PSNR更高但LPIPS更差；T4/T6/T7配置/质量也不同，headline非质量等价。AppC scene2+1天/object3+2天、64A10080GB，ablation6+6于2A10010h；同层宽不等同参数（199vs177M），D mask86M/MMDiT164M不可当同预算独立机制归因，precision/latencyhardware/batch与repeatCI ND。Ch23 cross-read/状态identity可解释但并非此view-role/co-refinement exact Existing；局部NVS proof-of-concept不建立通用多模态或可更新场景state合同，拟仅报告、不将所有新双流配方视作confirmed长期gap，也不移入World/VLA真环境保证。

**AST，5=2+1+2标准，拟OnlyReport。** 官方exact-v1 §4.1/§5.1–2/T3–4/§5.4已实际读；原机制缓存`feb10_admission_06671_v1.json`保留。Python CodeXGLUE清洗后30227/2771/3097，Llama3.1-8BInstruct 4bit、LoRA16/alpha16/.05、AdamW8bit、lr5e-5、3epochs/window5000、约50k tokens/update，单A6000，beam4。NIT比SBT短且近同quality；rawCode更短而quality相当，缺lexical的Preorder反侧最差。不是等总tokens或等walltime预算，结构与lexical信息不同，§5.4还承认pretraining重叠未排除；训练时长/总tokens口径不静默解释为全pipeline成本，seed/CI、AST preprocessing与推理成本ND。局部负侧修正“显式结构必然值得token”直觉，非小模型拒收、非全部code任务。Ch74 L28–44信任结构与L111–122评价token成本不具体承载此representation实验，不写Existing；该有限输入人口下结论未形成通用结构选择规则，拟仅报告、不新增Books。

**FCDP，6=2+2+2标准，拟实际Existing。** exact-v1 IV-C–E/Algo1、V-A–E/T4–7与VI-A已实际读；existing exact cache `exact-v1-bodies/2602.06499v1.html`，未新增raw。forward AG后host cache、backward每GPU取node shard并intra AG，trainable step后dirty、frozen一次AG保持clean；GPU利用阈值动态placement、NUMA pinned buffers与专stream，gradient RS仍跨节点。4node×8A40/48GB、双EPYC/512GB、100GbpsEDR+pairNVLink/PCIe4、DS0.16.2/Torch2.3、GPT2XL衍生10–30B/SQuAD、FP16activation/gradient+FP32master，fullFT microbatch8与max-batch两协议分开；LoRA r8 QKVO于2node另测，非fullFT headline。precision前文motivation有bf16而主eval明确FP16，不混用。通信体积T7未给对应模型、seq/total optimization/quality/seed与recovery ND，不授全部HBM实际恰好W/G或带宽不敏感普遍保证。`TRAIN-ZERO` Ch39 actual L263–269：正文已具备per-node完整generation host cache、activeGPU shard、optimizer/gradient ownership/prefetch可见性与DRAM/NUMA/PCIe/coherence代价，并直接绑定SF06499及相同配置边界，末注L384。此与本次核心采用命题逐点同一，不借泛Offload称Existing；frozen/trainable dirty具体recipe仅局部报告，不自动gap或新两段。现有正文保留不重复写书。

**DualMap，6=2+2+2标准，拟OnlyReport。** exact-v1 §2.3/§3.2–3.4/§4.1–4.3、A1.2/A2.1–3/A3必要内容已实际读；existing exact cache`exact-v1-bodies/2602.06502v1.html`。prefix hotness tree按rho延伸/合并hash key，固定两候选，在SLO约束内保affinity而非逐请求MinTTFT，正收益待请求仅迁往另一候选，ring局部重映射。PoTC均匀随机每请求选择不适用于同prefix反复同pair；A1.2原文明认nonuniform热点，所以不授负载定理或无条件两次miss界（eviction/动态key除外）。8实例/Ascend910B4/32GB7B或B3/64GB14B、1.5TBhost/FP16、1M/.5Mtokencache、TTFT5s、90%goodput；Mooncake首4k/8k trace保持并scaledarrival，inputcap20480/10240，warm500排除。Conversation14B ablation隔离SLO及rebalance局部收益；32实例/overhead仅Vidur模拟不冒充实测，decodeSLO/seed/CI与控制开销全pipelineND。Ch52 L167–205已有locality-vsqueue、逐请求churn与finite-period candidateplan，但并非此动态prefix双hashpair recipe全覆盖；有限重复trace和估计TTFT不能授general topology/SLO保证。该实验支持可选局部router而非新通用state/scheduling合同，拟仅报告，不按recipe缺位提confirmedgap、不写Books。

root已实际核REBEL/D-Legion/GRP/DriveWorld/AgentCPM的必要原源，五项OnlyReport通过并同步正式证据；Steering Ch31实际L502/504及末注1252 POST通过，锁释放。正式59终处置、34真实POST；AST5标准负侧准入待必要证据/Books终裁，FCDP/DualMap标准必要审阅继续。旧潜在身份与冻结候选分开，无共同全文队列。

纠偏恢复：有效33POST保留，正式UNO/PEPO已同步；REBEL06248 root actual §3/4.1–4.2/AppE Sample50核后5分安全必要深入OnlyReport终裁通过，无新增Books。AST06671同门槛改判5标准负侧准入，EvoMAS06511/TraceCoder06875原源必要事实核后贡献前具体关闭获root通过。DriveWorld06521/AgentCPM06540必要标准提案已送root，均拟OnlyReport；下面旧potential人数不表示已准入分母或正文队列。

06521标准5（2+1+2），actual§3.1–3.3/4.1–4.3/T4–7已读，旧method/refinement缓存复用，新增必要评价由官方exact-v1 HTML直接读。双future BEV+simulator监督reward权重action-head、冻VLM/denoiser，不授预测一致即真实物理。T4 stage3 nuScenes2/3s只有−.01/−.02，NAVSIM不同baseline/reward；T7“去feature监督”实际inference N(0,5)扰latent，不是训练loss删除，不能隔离feature监督因果。NAVSIM3view256×1024/ResNet34/b16/lr1e-4/3×20epoch/8H20约120h；nuScenes6view640×384/SwinT/b1/lr7e-5/3×24epoch/8H20约93h；precision/seedCI/E2Ecost ND。Ch25实际transition/score/真实observer分责及imagined bias已可解释但非该recipe全覆盖，局部proxy未改变长期设计选择，拟OnlyReport不加泛gap。

06540标准5（2+1+2），actual§2.3.1–2/T1/3.1–3.3.4/T5/AppA4/A6.1decision/A6.2/B1已读。Qwen235Bteacher强制12expansion，Qwen32B终report judge找最高score draft重标Terminate，decision reward匹配reference0/1非客观saturation；pruned/rawtraj SFT T5局部quality更高但监督token不同，不授停止optimality/净效率。forced15曲线与deploymentcap12分开，RL6–15文字不默修。MiniCPM8B/33kSFT1200traj lr1.5e-5b32四epoch、atomic5150/300traj rollout8/200step、pipeline500 rollout4/50step、8A100共2+2+4day；precision/repeatCI/fullteachersearchcost ND。Ch29监督位置与Ch79预算/完成证据不是该recipe实际Existing，judge-defined停止标签局部经验拟OnlyReport不加通用停止配方。官方exact HTML，未新建raw/无Books锁。

最新49行＝39必要core终态（31actualPOST/2Existing/6Only）+5低分关闭+5centerDisputed，normal150中48正式+8preclose，94ordinary，12earlyhold分开。DiSPO实际Ch33 L2269/2271/邻接2258–2277/note2741 rootPOST通过、锁释放，理论子命题仍精确隔离不授Evidence。49行V3+限定cached/unstaged diff-check通过，不授日级Gate。

06248 REBEL 5（2+1+2）安全必要深入ready拟OnlyReport待root。原raw `_method.json` §3 threat/score、`_evaluation.json` §4.1 forgetting/relearning对照、§4.2 calibration/schedule、AppE Sample50。只采benignproxy/relearning不能排序adaptive recoverability的局部negative，不采全部unlearning仅表面或真实危险能力恢复。max4220candidate与Leak1000非matchedbudget，knownhiddenanswer/Qwen7B hackerjudge、TOFU1B与WMDP8B/100MCQ/logits访问与generationjudge分开；manualauditN/FP率ND，AppE unknowntruth-refusal→fakebookjudge实际FP，不把qualitative‘noFP’推总体。Ch72 L2593–2607 suppression/erasure与有限恢复observer、1316–1318搜索访问/预算已实际比较；局部测试不升级擦除证书，不记泛Existing。hwprecision/targetdecode/fullcostND，未读attacktemplates/无关qualitative危害材料/未运行代码。精确日期SubmittedFeb05 22:54:56Z/registeredFeb09 02:37:36Z，按共用条件范围右端+1s。

06256 steering specificity 6（2+2+2）安全/具体Ch31 gap定点ready待root。原raw `_method.json` §3、`_baselines.json` §5/Table2、`_evaluation.json` §4/6/7/AppC；OOD target efficacy不等relatedcontrol-under-OOD。withcontrol训练/选择仍ID安全近baseline而shiftcontrol跌；Table2 safety=1−HarmScore，不给ComplianceRate反号，Llama8B基线.55/Δ−.19至−.30，headline35–55%是相对baseline不是55pp。四models五methods、256train/100val/α.5–4/alllayers/last5positions、500test/25staticprefix×100harmful=2500相关cells/3runs/RTX2080各15GPUh；precision/完整decode/fullcostND。SSVQwen MMLU−.29/GSM−.17，无统一最好；PCA单Qwenlayer20不因果。NQSwap conflicting/none/distractor接口已核，不借全部Table4数值；Ch31 L498–500非目标regression未拆unrelated能力/relatedIDcontrol/samecontrolunderOOD，拟两窄段不泛Existing。staticcontrol/小幅或关闭/权重级退路，不授所有steering必然失败/生产安全。日期SubmittedFeb05 23:14:05Z/registeredFeb09 02:37:47Z，按共用条件包络右端+1s。无Books锁。

06239 PEPO 6（2+2+2）必要S3/Alg1–2、finiteS4/Lem4.2–4与S5/T1–2/A1.1–2/4–5已实际读，原raw `feb10_core_06239_v1_method.json` 与 `_necessary.json`。二元BT无法两方向同时下估→tie mass+disjointpolicy训练→whole-response min/上界tiepenalty，unknownπdata下受限comparatorsupport；Ch34 L259–285仅一般distribution/overopt/freshcoverage，拟具体gap待根，不写Books。boundedreward/logratio/BT/balancedrepeatedpairs/Llog|X||A|/stateactiontieupperbound条件不套actual常数α.1/L2–4/tokenmin greedy；AppA1.4明说token理论不hold，localnormalize不自动给wholetrajectorytilt exact，不采用该exactclosedsolution。A1.5原min rejection divergence→acceptance0/16trialcap/A100约80h，meanstd变target；sharedbackbone多adapter仍多forward，GPU4时间1/4非全成本节省，L>3toy慢。UltraFeedbackmulti-generator/805AlpacaEval/Llama70Bjudge、LoRA16alpha16/BF16/AdamW1e-5/seed42/GH200+A100；ND完整E2E/生产SLO。只核采用条件不全AppE/F证明，未核代码/复现。

最新正式48行：38必要core终处置（30真实POST整合/2具体Existing/6Only）+5低分关闭+5中心Disputed，正常150中47正式+8贡献前关闭，95普通未裁决，不冻结；12早期日期hold分开。06451 actual Ch23 L71/73、邻接59–83/末注1135 rootPOST通过，锁释放；06454 actual source及Ch56 L262–280具体Existing通过；06453 Eq14–16/variance/缺AppD算法中心争议终态通过，不写Books。06671/06875 actual最低决定性段与root4分pre-denominator关闭通过，06909 ablation待root。48行V3及本日report/source/Ch23限定cached与unstaged diff-check通过，工具不替日级验收。

06462 DiSPO 6分必要§3–5/Alg1及S2.2/A1.1原raw norm已读，拟采用fixed-state cachedlogit多全填branch/terminalreward仅新filledtokens经验接口；Theorem normalizedsurrogate与main branchπold/exp(Elog)未建立一致，不采unbiased/全objectiveexactness。Main current throughput约.4baseline与额外reward/surrogate成本、SFTCountdown/多Z反退留正文；LoRA128alpha64/AdamW5e-6wd.1clip.2/4H10094GB/batch6accum4/256tokens，任务update3800/5000/7700/6600，seed/precision/全配置ND。AppB主文binaryreward与format/correct/fraction口径分开，未核实现/复现。Ch33 diffusiontrajectorybalance不是fixed-stateaction对照；gap采用/必要争议终裁待root，不自批。理论只读采用相关A1.1，不全proof。

06155标准5（2+1+2）必要方法/关键评价/反侧已读，拟OnlyReport待root：`feb10_decisive_06155_v1.json` §3–5.2、`feb10_core_06155_v1_remaining.json` §5.3/6、`feb10_core_06155_v1_diversity.json` AppE。已有生成seed/image/h标签训练proxy，部署先筛seed再denoise，区别于仅生成后filter；同LeNet赋label/置信度又验证，confidence logits/probabilities口述不齐，不采自然语义真值/可逆性保证。70k seeds生成后balance35160、fresh5100由同h核；53.42% highconfidence vs20.31% unconditional是选择人口，LDA监督probe不证天然语义结构。AppE仅每类10张/CFG3视觉比较，无严格diversity或净成本。Ch24 L1229 prior steering与L706 lowresolution preview筛seed不同，但此局部classifier-defined接口不强写泛原则。

06470 UNO标准5（2+1+2）必要方法/关键评价/反侧及具体Ch77 gap提案待root：`feb10_decisive_06470_v1.json` §3.1–3.3、`_route.json` §3.4–3.6/Alg1/§4.1、`feb10_core_06470_v1_evaluation.json` §4.3/5.1–2。低gap→Expert DPO+NLL并由simulatedwinrate留checkpoint，否则/高gap→Critic训练与runtime回答/反馈/修订，outlier回base；Ch77 L627–657已有external→weight不可逆/teacherconsolidation，未有failedweight→critiquepath选择。只采用分责不采noisequality/Bayes条件保证，Ward variance-increment不是diameter。LongLong prefilter recall0、cost savings按训练数据少，不是总GPU；fullUNO额外calls不借UNO-Single inputtoken图。simulateduserlogs、baseLLM judge3次、BLEU.05过滤、τ.45/γ.53、LoRA64/drop.05/lr5e-4/8epochs；hwprecision/fullcostND，不授恶意噪声/长期安全。

06549 AdverISF标准5（2+1+2）一般学习机制必要原文已读，root必要源/Ch5核后OnlyReport通过，非科学应用范围关闭：`feb10_core_06549_v1_generic.json` §3.3–3.4/4.1–4.4与AppA1.1–3。joint-vs-shuffled WGAN-GP+残余递归，无separationlabels但有target监督，noise含useful/spurious；λ>1伤预测，GP不证已独立/唯一puresemantic。strictgain依赖首层遗漏/后层capacity，不采trained必达。实际AppC1–4在官方HTML定点读到：s13Gaussian→randomMLP拆3/5、γ.2、x随机线性mix，未给独立noise-shiftprotocol；10seeds，AEP70%Joint<VIB/Concrete500<VIB/InfoR。纠正此前CIFAR全负概括：Joint N100/200/300 .280/.321/.361>InfoR .262/.320/.357；TwoStage N200/300也更高，N100相等；仅N500/1000两variant均低于InfoR。two-stage首40%冻第二层后冻第一层、critic2和ablation6/3、随机KLcoeff也变训练；hwprecision/净costND。Ch5 L67–116已有目标相关invariance与shift边界，不把本局部recipe记泛Existing，不走科学S4.5。标准必要安全终处置仅报告，不授trained严格独立/唯一因果或普适优势。

06443 TrajAD root实际核S3.SS3/4/5/6.1/6.3–4及Ch80 L137–161，5分标准OnlyReport终裁通过。现36必要core终处置＝29 POST整合+1Existing+6Only；正式45行另5低分关闭/4中心争议，普通尚未0。06451已按root窄锁实写Ch23 L71/73、邻接63–81/note1135，actualPOST待root，不先计整合。06453中心配方冲突提案待根，06454/06462主方法与关键评价已读，必要配置/理论对象定点核。

### 2602.06451v1 — BrokenBind（5分标准必要已足，具体gap提案）

5=2+1+2，新增只跨dataset缺modality时pivot-pseudoinverse双路径pseudo embedding训练接口，不为成熟CyCLIP/LoRA加分。actual§3 Eq2–12/Alg1及§4–5全部必要method/eval/counter已读，raw feb10_core_06451_v1.json。D1(a,b)/D2(b,c)中b为pivot，per-batch Moores-Penrose停止gradient而每batch重算；X-mod与X-data双pseudo路径Fro约束后进入contrastive，同时沿用CyCLIP geometry symmetry。Pseudo不是实际恢复的缺模态观测，batch-wiseindex/维度与pivotconditioning须核，fixed stopgrad不能证明数值稳定或biasfree；不能把Mixup推广出wholefeaturespace当高维缺模态真值。

§4两/三dataset隐藏targetmodal检索mAP，不是rawsignal生成；作者因Recall低改用mAP应保留口径，不采全部bias消除。冻结pretrainedencoder backbone+projector先linearprobe后LoRA，AdamWlr5e-4/wd.2/50epochs，前25consistency后25MOX；newstage成本不可消失。IB/LB/VCLIP+CLAP/TVL、AVE/MSRVTT、SUN/NYU、FLIR/LLVIP、ObjF1.0/real，各dataset原样本关系是真实配对而非全无pair。Table9 linearprobe only/LoRA only均差于顺序联合，收益非MOX独有；w/oFro/w/oCons/w/oMOX局部消融支持配方依赖，tSNE不证明真实target重建。Raremodality尤其text-tactile仍low；hardware/precision/batchrank/β/独立seedCI/全部cost ND，未核artifact或复现。

Ch23 actualL63–69 English-caption map/GPA已要求对应同一批样本，尚无两dataset只共享pivot的pseudo训练接口，邻Ch22/24交接已读。拟Ch23该共同参考两段后另两相接窄段：缺配对集合时双path pseudo约束/停止inverse梯度，distinct原encoder/真实pair训练与全scope；病态pivot/偏移会放大错位、无观测truth，projector/LoRA/新loss成本及原encoder/真实paired/纯共同map退路近正文。root必要source/owner待核，不先写Books；若只局部recipe不改变长期可OnlyReport但不是主题Existing。

### 2602.06446v1 — CORE（中心争议终裁已通过）

5=2+1+2，root actual原metric L278–342、结果365–424与AppA885–951终裁中心Disputed隔离。SCR同unrelated人口定义与Table3accuracy/5.3mean37.6不对应，answerletter→relationmapping未披露，selfreport independentconfidence非normalizedlogits，无明确None出口；不授架构因果/校准/Existing/Books。只接受同题ID+letter→relation/SCR逐项分母、selfreport读取/必要负控制后定点重开，不请求allcode。raw feb10_core_06446_v1_conflict.txt，HTML404但primaryPDF文本足，不是全文未读或外部Blocked，未授复现/visualQA。

06221 actual Ch66 L423/425/note4392 root POST通过，锁释放；当前29真实Books整合、35必要终处置。前述06218 POST通过保持，正式43行尚未冻结。下方历史提案不覆盖本实际状态；未授整日Gate。

06218 actual Ch23 L838/840/note974正文与邻接root POST通过，锁释放；当前28真实Books整合、34必要证据终处置。06221实际Ch66 L423/425/note4392已按批准窄位写，非作者POST待核；不授日级完成。下方06218“拟定/待核”为历史，采用边界不变。

最新27处实际Books POST通过：新增06180 Ch23 L182/184、06205 Ch23 L67/69、06208 Ch30 L119/121、06219 Ch25 L314/316；root实际核必要源/owner及新增正文、前后邻接与末注，窄锁全部释放。前三十二core加06219后共33必要证据终处置，正式报告新增06219仍需同步，不是冻结分母；06218/06221及其他已准入普通工作继续。下方拟定/待核仅过程历史，不覆盖本更新。

最新23处实际Books POST通过：06422 Ch33 L255–274/末注2711、06394 Ch11 L85–100/末注445由root实际顺读正文/邻接/末注后PASS；两窄锁释放。06409安全必要深入OnlyReport通过，不采用可上传pixel路径/未披露防御与T5base。正式37行尚未冻结，下一15项获准入而非Evidence通过。

### 2602.06443v1 — TrajAD（标准必要完成，拟OnlyReport）

5=2+1+2。实际§3–6全部method/eval及§7必要范围已读，raw `feb10_core_06443_v1.json` S3.SS3/S4.SS1/S4.SS2/S5/S6.SS1–4。AgentBank过滤seeds后控制注入step，强模型强制延续错误生成negative并标注该注入位置；balanced63,484 pairs/13tasks，500人工分层100/domain局部review。注入step标签不自动是自然失败最早causalcriticalstep，syntheticcompletion非真正environment执行，10%每task样本split未声明seed-pair分组隔离。SFT Qwen3-4B QLoRA8/16、PagedAdamW8bit、A10080GB；epoch/batch/context/temperature/重复run/完整cost ND，不采普遍trustworthy或必要模型规模结论。

JEM同时index exact+difflib RatcliffObershelp>.2文本相似，非语义oracle；没有恢复执行/rollback副作用验证。留Embodied-domain OOD detection接近fulltrain但localization下降，50k→60k反退、8B不优不证明scale一般无效。Ch80 L137–161实际earliest evidence-backed criticalstep→boundedrootcause→repair/state及offline不能恢复externalstate已有具体采用接口；本项只新增受控perturb/process-supervision数据与局部训练经验，不能将其未实测rollback当新执行机制。拟OnlyReport而非泛主题Existing，不重复成熟诊断/rollback原则赚Books。准入未撤、实际5分标准必要已足，root source/owner终裁待核。

### 2602.06221v1 — BenchMarker（标准必要/repair gap提案）

5=2+1+2。实际§2–4、§7/8与AppA4/A5及A11相关口径已读；raw `feb10_core_06221_v1.json` `[id=S4.SS3]`/`[id=S4.SS5]`/Table6、`feb10_core_06221_v1_config.json` `[id=A1.SS4]`/`[id=A1.SS5]`/`[id=A1.SS11]`。工具webmatch只证明online出现/近重复，不知真实training membership；choices-only还检查推断stem是否匹配，否则将可重建题目混成shortcut。19项education rubric的风格不是普遍任务错误，若noisyinputs是目标应保留干净/噪声分账。作者按GPT初始预测分层up-to10flawed/10not构造人工validation，不是随机真实prevalence；一作者/metric、第二作者每metric50random（writing每rule50），agreement84/84/min85非全部doubleblind真值。

§4.3 filtered/no-flaw与sameN random100seeds排名可变，但未匹配difficulty/construct，非修复因果质量保证。§4.5 Table6原repair再次judge：GoldenSwag multiplecorrect18→4但grammatical68→79；MMLUPro implausible7→17、multiplecorrect10→22，支持改一类缺陷时其它axis反退，不给未经人工重新验收的修复承诺。§7工具主要flag给human或discard，而rewrite只是本节case/future方向，不能说完整remediation已实现。默认API参数/single run/24h限时；<8B单RTxA6000、更大8×RTXA5000，endpoint版本列出但temperature/precision/fullcost ND，未核代码/复现。A11 contamination mapping将partial_match/no_match称flawed与主文含义冲突，不自行修recipe；不采用具体webmatch分类/严格contamination结论，拟采用repair独立反侧不依赖此映射。

Ch66 L414–433有MCQ顺序/安全候选/CoT读数；L916–919 variant→semantic verifier+gold twins未说repair会新增多正确答案并改变ranking人口。拟MCQ选项顺序段后两短段：item quality axes与answer uniqueness复验；repair后保原题/版本和分轴judge+human反侧，同N重排不是同difficulty，对照未过保留原题/flaggedslice/人工裁定。具体gap采用待root必要原source/owner；不重复成熟‘judge不是truth’原则借分。

### 2602.06218v1 — Cross-Modal Redundancy（必要证据/owner提案）

6=2+2+2：已有线性子空间投影可能删除目标重叠 → matching image-caption共训SAE并加normalized-code cosine/trace regularizer，再按两模态code二阶能量比划分atoms → 提供learned-basis mask分支，但能量/重建与真实语义保留不同。实际§3–6与AppC/E/H/I/J/K必要段已读即停；raw `feb10_core_06218_v1.json` Eq1/§3、`feb10_core_06218_v1_CEK.json` C toy/E/K、`feb10_core_06218_v1_metrics.json` E.2.2/H、`feb10_core_06218_v1_mask.json` I Tables9–11/J/K。操作目标要求matching pairs，不采“不需instance matching”广义claim；β soft不等exactisoenergy或nonlinearICA可辨，τ=.05 bridge支持是被测dataset的code能量proxy，不是trueconcept。

AppC特意构造等价embedding的双D/Z toy与isoenergy成立/违例；iso时Aligned W.184/cos.52仍非perfecttruth，违例plain.197/.83 vsAligned.185/.81无普遍优越。AppE稳定seed/bimodality/FDA只是proxy；E.2.2完整SAE reconstruction作为mask前baseline，不是originalencoder。AppI LAION/COCO六encoder mask召回下降，LAION CLIP r@1 .882→.760而center .898，COCO meanavg −.052；ImageNet有mixedresults，不能将gap缩小当无损。MainTable1 reconstruction CLIP MSE .141→.163/R2 .859→.837，β过大alwayson/degenerate。AppK constant candidate projection才能rankinginvariant，adaptive Δm能翻转排名；orthogonality单独不足，不采主文无条件Prop1或零norm简化。H queryarith/FashionIQ小收益与OOD KNN阈值不证明语义恢复。所有SAEs 1M matching LAION/exp8/l0=20、六dualencoders；crossattention非适用、β选择按reconstruction预算，hardware/precision/完整训练搜索/seedCI ND；未核实现/复现。

当前Ch23 L838几何净化已有text SVD→image非目标正交补，而Ch5 superposition只一般SAE/因果边界，没有pair-regularized learned codebasis与能量mask/排名条件接口。拟Ch23该段后两短段：pairedcodes→energyselector，与硬几何正交补不同；mask改下游population且不保证任务保留，pair/SAE/search成本、center/原embedding/conditionread退路近正文。必要采用命题为具体owner差额，待root原source/owner定核与窄锁，不纳无损/trueconcept或全证明。

### 2602.06180v1 — STACodec（标准必要证据已读，具体owner缺口待核）

6=2+2+2；实际新增不是一般semantic/acoustic分层，而是§2.1.2 Eq6将RVQ首层index指定为外部SSL K-means token，Eq7码向量仍可训练、后续层补声学残差；§2.2 Eq12量化前SPD从acoustic encoder预测teacher index，替代推理SSL路径。§2.3两阶段90K codec+160K joint，离散选择反传细节Not Disclosed，不推导其实现。实际读取§3.1–3.4与§4.1–4.3/Tab1–2即停；raw `feb10_core_06180_v1.json` 标记 `[id=S2.SS1.SSS2]` / `[id=S2.SS2]` / `[id=S4.T1.5.1.11]` / `[id=S4.T2.5.1.2]`。

LibriSpeech960h/50Hz/D128/8×1024，WavLM layer23 K1000与HuBERT layer9 K1024身份不能互换；单A6000/b32，原STA280K vsSPD250K非等总训练预算，baseline多为官方checkpoint、HASRD仅paper报告。Tab1 STA→SPD PESQ3.62→3.51、WER9.35→15.39、IC74.21→64.31；250M/30GFLOPs是去teacher估算，不是runtime/SLO。Tab2 noSTA3.88/40.62 vsSTA3.58/9.27显示重构换语义，不授两者同时无损；code usage1000句不是disentanglement证明。未核artifact/复现，precision/总成本/独立种子统计Not Disclosed。

Ch23当前“分层残差表示”L168–176只说前层粗语义后层细节；L244–257 source侧路/两独立流/phone-tone残差是不同接口，未承载semantic identity约束index但codevector自由这一差额。拟L176后两窄段，保留外部teacher与普通RVQ退路、SPD预算/质量回退，并由Ch24消费codec identity不重复生成目标。具体gap若获root核，采用命题定点深入；当前不写Books、不宣称Evidence已获独立通过。

06393 MuCo Ch23 L509–525与末注1093 actual POST通过；06427 BridgeNav Ch26 L226–239及末注1808、06412 SureLock Ch24 L571–589及末注1816 actual POST通过。21个真实Books整合均获非作者POST，锁已释放。06440五分安全深入OnlyReport、06413六分中心争议隔离通过；06441按原五分中心争议/暂缓，局部Eq8作者事实仅报告描述，CE方向/θfor保持不授正面Evidence或Books，精确重开不要求全代码。

## 新就绪批次（采用/owner待独立核）

### 2602.06219v1 — Coupled Local and Global World Models for Efficient First Order RL

6=2+2+2；必要实际§III-A–F/Eq1–6/Algo1与§IV-A–E/TabI–II/§V（本篇原文含罗马小节，不误称第3算法新数学）。DMO decouple本身承自先前方法；新增可核接口是global diffusion生成pixel rollout、每step重新encode该global observation并由local RSSM提供latent Jacobian/learnedreward梯度，local继续用当前policy生成的global数据更新。局部训练目标继承global/reward误差，不等真实动力学或无偏梯度；“一步accuracy”不充分证明导数accuracy。Algo1/globalreward只作local/value目标、gradient不穿imageencoder，不静默修Eq3 reward loss无log与return记号，不采用可执行公式保证。raw `feb10_core_06219_v1.json` `[id=S3.SS2]`/`[id=S3.SS5]`/`[id=S3.SS6]`。

§IV真实Flexiv 5Hz delta/100Hz插值及Go2 5Hz/50Hzcontroller，PushT4hplay/globalcontext4帧，Cube12hplay+intentbutton/96帧，RLprefill32帧不是samecontext。PPO Cube H128vsDMO64不同budget（避免PPO approachreward重复hack）；NoDiffusion只换forward模型，不隔离更大模型/历史/reward所有因素。PushT10tries，PPO正常1/10而宽松criterion4/10；Cube轨迹N3，替换low-levelcontroller展示有限transfer且BC也保持，不授所有跨robot。hardware/precision/完整离线pretrain+onpolicyrefreshcost/seedCI未披露，未核artifact/复现；unsafe行为、安全率未评价，结论safeproxy不采用。

Ch25 L304–324 Imaginedrollout已有prediction误差/targetcontext/gradientpath身份，尚无高保真forward与廉价onpolicy local backward两个模型分责。拟在该小节第一段后两短段，明确learned world/reward bias与derivative验收、总成本/有限对照及短rollout/真实observation/simulator退路；Ch26仅消费controller，不重写。标准必要范围已足，specificgap采用待root原source/owner复核与Ch25窄锁，不授正面实验或普遍样本效率。

### 2602.06205v1 — Multi-Way Representation Alignment

5=2+1+2，标准必要范围已实际§3.1–3.4/§4.1–4.5与AppA1/C1–2/E，按具体多模型接口缺口定点深入；raw `feb10_core_06205_v1.json` 与必要suffix `feb10_core_06205_v1_geometry.json`，精确 `[id=S3.SS2]`/`[id=S3.SS4]`/`[id=A1.SS1.p2.1]`/`[id=A5.SS0.SSS0.Px5.p1.2]`。Matched N身份、多encoder先standardize/必要PCA到共同维度，GPA每模型正交map进共同参考；其cycle/isometry只限此坐标，不恢复原PCA丢失信息。GCPA共享row-normalized residualMLP朝样本consensus校正，angular soft trust penalty不是硬约束，AppE明说非正交后cycle不必保持，不采用标题的统一exactness。

Actual trainfit/testeval，MASSIVE Kmeans五seed但表mean±std跨10models非独立run CI；TED按ordered pair Avg/worst，correspondence75%各语种shuffle，GPA跌幅有时更小、GCPA绝对结果更好。AppA1 small weak anchors时GCPA能强化错误对应；强CLIP pivotal与caption平均是Flickr8k前提。AppC1–2 sweep说明平均drift/权重灵敏度，未披露完整MLP/optimizer/hardware/precision/totalfitcost，不写O(M)总runtime或无损。未核实现/复现。

Ch23 L63–65承载固定English双空间小map；L824–828几何诊断/正交删除不承载多space共同参考→sharedcorrector这一取舍。拟在前一分支后两短段，交代M个坐标map减少pair身份但不保证低总成本、对应噪声/非线性cycle回退GPA/pair/原encoder；不把matureGPA重新记作新数学，新增对象是共同接口与几何校正条件。需root必要源/owner核与Ch23空锁后才写。

### 2602.06208v1 — Emergent Low-Rank Training Dynamics in MLPs with Smooth Activations

5=2+1+2，标准实际§2–5及AppF1–2必要，raw `feb10_core_06208_v1.json` `[id=S3.Thmtheorem2]`/`[id=S3.Thmtheorem3]`/`[id=S3.Thmtheorem4]`/`[id=S3.Thmtheorem5]`、suffix `feb10_core_06208_v1_init.json` `[id=A6.SS1]`/`[id=A6.SS2]`。定理限whitened data、K<d/2、m≥d、两层固定full-row-rank W2、平方误差GD、bounded一/二导且φ(0)=0、小semi-orth初始化/步长、残差界和另假设gradient几何衰减及spectral gap。受限结论是初始化导出的block外每step受ρ(t)约束，不等W1本身永远rank2K、所有训练存在固定rank或Transformer/Adam保证。Approx lowrankgradient与subspacealignment都需，不能只靠一次SVD普遍成立。

§5 Eq10从初始化W与一次first-layergradient估S_big、传播到首尾basis，basis仍训练，不是冻结LoRA base。FashionMNIST4layer/GELU或SiLU/fullbatchGD1500epoch、5trials，matched同hyperparams不是各配方最优；VGG16缩pool7→3、ImageNetbackbone与新head，CE/SGDmom250epoch/A100，classifier-only 2K仍5–10% gap且更慢；AppF2 4K改善仍2–3% gap。F1角度失败是局部SiLU实验，不写45°普遍阈值。SVD/初始gradient/更多epoch计费，precision未披露，未核实现/复现。

Ch30 L115–128 factor optimizer谱与冻结随机scaffold没有此task-conditioned initialization geometry→可训练窄网络；拟scaffold小标题前两段，以受限可构造分支解释rank不能只凭分类K/局部gradient承诺，保留fullparameter与原LoRA任务回归。当前不授整合；若root确认owner差額才按此命题gap深入，不扩全proof或抬分。

### 2602.06409v1 — VENOMREC（安全必要证据就绪，待root）

拟6=2+2+2，具体joint-feature poison与融合安全反侧必要深入。实际§3攻击者可控UGC/user-interactions而victimweights私有；§4.1 publicCLIP/T5 surrogate joint-centroid exposure alignment、4.2/4.3每轮重算token/patch saliency并交替feature-vector/greedytext编辑；§5.1–5.4 Tables1–3及utility/ratio反侧。VIP5 frozenT5small/CLIPViTB32预提取features+PEFT，Amazon三集8:1:1。视觉迭代直接改projectedfeature v，不证明可渲染上传pixel poison；attention rollout/融合相近只定位proxy，不证明真实consensus因果。

Table3 Tab→Img→Txt→interactive为累计预算/重新优化人口，未独立控制循环次数和search成本；FID36–43/Rouge/CLIP一致非人眼imperceptibility或可信来源。部分ρ提高会损utility，不采用统一无损/ERheadline。exactHTML AppendixA1–A5空标题，必要exactPDF p12尾也只有标题，raw见feb10_core_06409_pdf_appendix_raw.txt；不能声称T5base或defensivefilter已核。hardware/precision/seed/searchbudget/temp/outputcap/SLO ND，未核artifact/复现。

Ch72 assets/provenance与sensorcorroboration现有责任边界，不是该joint training poison实验；Ch23 fusion一般互补不直接证明该负侧已被承载。拟OnlyReport局部feature-space作者观察：可提醒融合agreement不是独立corroboration，但成熟provenance原则不再写书。实际raw-upload路径/等searchbudget、必要防御与T5base材料未公开不能升级真实生产attackclaim；root终处置待核，不因缺附录撤准入或降分。

### 2602.06422v1 — TurningPoint-GRPO（必要证据就绪，owner待核）

6=2+2+2拟标准后specific credit gap深入。实际§4/§5 Eq5–10/Def4.1/5.1、§6.1–6.3 Tables1/2/Fig4/6/7及AppB/C/D必要。缓存SDE中间latents，以ODE continuation的终点reward差作为increment，再对sign-selected turningpoint换终局-minus-prefix aggregated reward；每step独立group归一。ODE/SDE边际同分布不证明ODE是条件均值或unbiased/causalcredit，AppC只验证给定selection符号/幅度身份，不授唯一delay原因。AppD按positive/negative agg平衡、删小magnitude又改有效人口，故非无条件hyperparameter-free配方。

SD3.5M LoRA/512、trainT10/test40/G24、32H20，同配置作者重实现FlowGRPO，AppB perpromptadv、β.0004/.0001与reward版本。主table含KL，Fig4/6/7去KL不能拼一组guarantee；window8好而4退、α.4/1退为直接反侧。700vs2300step不是totalcompute，额外ODE/reward调用计费，Figure6时间局部但完整配置/precision/seed/SLO ND，定性无hack不能授已排除hack。未复现。

Ch33 L257–265当前innerQ/value→inneradv需critic，L2240–2253 trajectorybalance是另一目标，未ODE-completed-endpoint差额+terminal替换的无critic分支。拟L265后两窄段，保留branch的训练only/signselection/population/成本与原terminal reward、可靠critic退路；Ch24仅handoff生成path语义，不复制。待root必要source/owner/授锁。

### 2602.06394v1 — QA-Token（必要标准/owner差额就绪，待root）

5=2+1+2，通用quality-aware vocabulary接口而非领域应用指标；实际§2–4/§5 Tables1–4/§6及必要AppC.6–7/G.3/H.1/H.4短段，缓存feb10_core_06394_v1.json、06394_v1_conditions_config.json。原普通频率merge不能分辨同频不同质量→PMI-ratio×aggregated quality^α×domainfactor，先固定adapt参数做PPO merge候选，再Gumbel下游调α/weights、最后固定greedy词表；不是每请求PPO。q来自外部domainproxy/可学权重非真值，geomean和arithmeticmean不同，quality过滤可能丢稀有真实pattern。§4 sequential两阶段不自动满足simultaneous two-timescale；AppC.7明说LMloss一般非submodular，1−1/e只另条件quality-frequency对象且−K/δ误差可能无信息，不采全LM最优/PPOglobalconv/zerooverhead保证。

§5 10runs/95%CI/WelchHolm为作者声明，Table2质量/RL/参数消融支持所测局部设计非所有noisycorpora。§6 METAGENE7B等1.7Traw exposure不等steps；stepmatched额外17.6%raw又改预算，不合并为无成本收益。另一foundation对象是1.2B（不是7B finance），下游2层LSTM/PPO；H.4描述chronological/walkforward/historicalquality，不将收益转成金融建议。G.3 A100 Stage1 30–36/Stage2 20–24GPUh vsCPU5–10minBPE，freqtable4GB/peak16GB，部署固定词表并不免除质量统计/构建/模型重训成本；precision/inputlength/fullfoundationtraininghardware/seed/SLO ND，无artifact/复现。当前Ch11 L58–110 BPEfrequency/searchobjective对照未qualityproxy→learnedmerge→fixedartifact接口；拟BPE frequency说明后两段与参数/外部quality失配回退，Ch12 embedding仍owner-ID映射，不复制。根采用/授锁待核；不要求全部C/E proof。

### 2602.06412v1 — SureLock（待root采用/owner）

6=2+2+2拟标准后specific Ch24永久lock gap深入。实际§2 Alg1/Thm1、§3 Tables2–4、§5limits、AppC/D必要段；缓存feb10_core_06412_v1.json与06412_v1_CD.json。unmasked confidence+localKL→永久停Q/FFN+每层缓存K/V保attendable，monotone与revocable选择不同。正文active=unmasked-notlocked与Alg1 allnotlocked不一致，不采用这具体集合配方/代码已核。Thm1 A1无remask、A2 nolock future逐位置KL几何tail、A3logitsmooth+A4 logsoftmax；只比较固定row nolock与frozenrow，不证明其它active行经staleKV影响已控或ARexactness。AppC16MTBench平均KL曲线不能证逐row/ futuretail，AppD先expectedemb而非argmax/sample，global全j差额转local需κratio有界、常数不只weights，不从低localKL授全网语义。

LLaDA8BBase/Instruct、WikiText103/Llama3-8B GenPPL与MTBench singleturn GPT4o judge、B4/Ng64–512/ε5e-4或5e-3/temp0CFG0为局部评价。短Ng64/128PPL退步（Table2可1.31×），MTBenchmean近不变不能证明逐题等价；Ng64/B1无runtimegain，irregularcache/packing偏离GEMMFLOPs。selection surrogate k.8未调优不授真实dLLMcache优胜；硬件/precision/seed/SLO ND，本次不采用1.73×通用headline。Ch24 §跨步分布不稳定性已有refresh/reopen，但未permanent compute-deactivation/仍KVattendable这一不可逆选择；拟其后COVER前两段，原全量revision/允许重开退路保留。

### 2602.06441v1 — MOX（待root安全/采用）

拟5=2+1+2，局部parameter-edit component不借整个deletion生命周期分；安全/longterm gap必要深入。实际§2.3 Eq4/5/8、§3主要table/ablation/α敏感/cost、AppB配置与AppCproof，缓存feb10_core_06441_v1.json。新alternative是memorize forgetset同时retain predictionKL→以θref−α(θmem−θref)外推新的weightartifact；negative taskvector本身既有，不计新增。θmem retainKL约束非θfor约束，局部NTK近似不证明遗忘/共享能力。原CE定义logp与AppC正CE不一致、Eq5negativeNPO objective可非lowerbounded、targetEq9人口写retain，不静默修纸面具体loss；暂不采用这些争议子命题。AppC额外stepsize/Lsmooth/PL/dataentropy/realizability只给θmem的受条件GD终点，非θfor与有限step/no-collapse，avgKL高非delta-collapse等价。

Phi1.5B/Llama2-7B/TOFU与MUSE，AppB AdamW b32、参考5epochs后同LR1e-5或2e-5 unlearning，单A100/H100或4×4090可运行而非锁定实际硬件。α.5/1/2/4/8有限grid/last-epoch，momentum.675；retainedutility在极端α下降，GD+KL局部优势并非所有deletion任务。3weights storage vsNPO2、CPUoffload/transfers/训练/调参另计，43TFLOPs/sample与2.5/4.7s没有完整SLO配置。precision/完整epochsteps/seed/长度ND，未复现，未授永久擦除/合规。Ch72 L2611–2675现deletion probe/retainedutility完整却无retain-constrained memorization direction→negative edit路径，采用/OnlyReport待root判断。

### 2602.06440v1 — TrailBlazer（待root安全/OnlyReport核）

拟5=2+1+2，安全受影响必要深入。实际exact-v1 §3/§4.1–4.2 Tables1–6及Limitations，缓存feb10_core_06440_v1.json。新state把K=4/5的prompt embedding、heuristic response四features、reward与mutator ID交attention selector；五mutators、Vicuna参考cosine reward及helper借RLbreaker，不计新增。AdvBench520拆364/156、HarmBench159/51，四指定11–20B模型，A6000；统一test target query预算50、GPT4o严格10/10，但QPS只成功攻击条件，失败预算、helper/judge调用与offline训练18K–24K秒另计。Table1 HRL/AHRL两分支局部支持history效用，transfer有Llama→GPT-oss反例，prompt-rephrase防线甚至局部提高攻击成功不能推全部防线无效。precision/temp/cap/seed/SLO ND，未复现/生产攻击。Ch72 L703–750 run subject/history/query budget与paired-confounding分工已有，但无此局部攻击实证；拟OnlyReport而非泛主题Existing，不制造成熟state原则新写。

### 2602.06413v1 — AR Stability（中心主张待root终裁）

拟6=2+2+2，理论中心与owner判断必要深入。实际§3定义/proof、§4.4–4.5、§5.1–5.5及真正App B.1–B.8；缓存feb10_core_06413_v1.json与feb10_core_06413_v1_A3.json（后一文件名历史，实际B段）。补proof后撤销‘所有TV证明无效’疑点：B明示balanced prior，Bayes平均advantage=TV，uniformeta<1下指数条件推导成立。主文posterior-at-state不是同对象；noise/finitecapacity不自动给strict contraction，B.8架构系数留未来。Synthetic unique sequence无中间feedback，landmark提供independently solvable子任务；branch-free的backward/sticky噪声是人为设计。TextWorld同(room,actionset)cache模型输出，只改变reset+inphase edge dedup，未拆两项或测eta/advantage；不能推AR本质必然cliff/DAG必要/无额外信息reset恢复。Ch79 L140–204 plan feasibility/executor/search/currentstate分工未承载这必然性，拟中心Disputed不正面Existing/Books。仅接受一致统计对象与实际decoding严格收缩条件、reset额外信息/控制机制及独立对照后定点重开，不扩版本史。硬件/precision/temp/完整trials/代码可核性ND。

### 2602.06427v1 — BridgeNav（标准必要证据就绪，owner待核）

准入已root通过，5=2+1+2，实际§3.1–3.5/§5 Tables2/3、AppC localgrid/AppD/F必要反侧。上游P2P先到近邻，h10观察→5waypoints；target bbox near/far监督与future RAFT flow top10%区域重建分工，训练aux decoder推理删除。Stage1 bbox，Stage2冻结backbone/intent训waypoint+regionrecon+instrbool，运动magnitude非目标salience/动作cause。Table3保留dynamic tokens只删recon监督，SR.1m29.20→33.82/.3m86.55→89.55/TR10.69→9.77局部支持aux目标，其他模块联合对照不证独因。Qwen2.5VL3B shared baseline重训，A*和MoGe localgrid形成derived GT；§4实际55K streetview trajectory/instruction与Wan2.1合成视频、20K近入口manualbbox不是实机trial独立证据。AppD8H20/5h/b64后128H20/48h/b256，A10>5Hz仅报告未充分配置；precision/seed/真机trial数/执行SLO ND。低分辨/畸变退步，quadruped未证明humanoid/碰撞保证。Ch26 L224–230已有full future feature reconstruction/action interface，但未motion-region目标选择分支；拟其后两窄段，仅分开aux target与physical transition，保留full reconstruction/显式action/controller退路，root owner/采用待核。

### 2602.06393v1 — MuCo

exact-v1 HTML404、两次urllibPDF406，但web PDF必要文本可读，缓存`feb10_core_06393_pdf_method.json`、`pdf_excerpt1.json`、`pdf_eval.json`。实际PDF§3–4 Eq3–8/Fig2–4、§5.1–5.3 Tables3/5–8；截图入口两次报contenttype不支持，不称视觉验证/代码复现。拟6=2+2+2：query图像+同图多query的独立causalstream、target纯文本独立stream共享图像编码；每turn抽embedding并只排sameimage其他positive，不把Nk个相关pairs说Nk独立images/样本。Forward未来不可见与training laterturn gradient回流不同；singlepair阶段用maskedcounterpart生成后turn作额外监督，只initialembedding测试，非testtime偷看gold。

Table6通过去priorhistory mask使每turn只image+owntext（57.3/68.4 vs58.2/69.5）支持局部history分支，不授无限context/generalcoherence。Table7无logitmask FT31.1/30.9 vs69.2/69.5说明自增pairfalse-negative，而pretrain影响小；不是每个sameimage答案都等价。Table5固定M3T 5M、7pairs/1024images但batch7168baseline更多image，PFLOPs估算且representation/negative人口共同改变，不授相同independentbatch/E2E7倍或低3%wallclock。

Qwen2VL2B/7B、frozenvision/LLMLoRA64alpha64、32A10080GB/1epoch/global1024/τ.02/LR5e-5，M3T合成35Mpairs与caption/Qwen2VL7B成本、50%wordmask/turnshuffle保留。Table2本文51.6/56.6与正文54.2/58.7不一致，不采用M-BEIRheadline。precision/seed/optimizer细节/部署SLO ND。Ch23 contrastiveloss/negative population与L107 causal→bidirectional旧分支并未承载此causalstream多turn+mask，拟InfoNCE负例段后两段（位置待root），保留ordinarysinglepair/真实holdout，必要源/owner待核。

### 2602.06373v1 — ReBeCA

缓存 `feb10_core_06373_v1.json`，实际§3/§4.1–4.2/§5.1–5.2、Limitations/Ethics与AppA必要配置。拟6=2+2+2，reflection stage-specific行为干预与联合干预负侧，贡献不借一般‘相关不等因果’。CESR每步20sample后选最大semantic cluster的centroid；GPT5/人工抽frequency>5%二元行为，GES/五fold CVLL选择结构。ICP式stage仅随机20fold分四组、ANOVA/Levene mean/variance p>.05/effect<.06，不是实际外部环境干预、conditional independence或无latent confounding证明；typicalbranch选择、judge标签和fold非拒绝仍有替代解释。

50 AIME上的2×2 prompting只强调选定feedback/refine行为，未证明只改变目标行为或compliance；caption‘excl.’与强调正文不静默解释为删除。各Qwen3规模响应不同，联合两行为mean12.75低于baseline13.25且不如单behavior，CochranQ omnibus p.013非所有pair因果。四规模bnb4bit/800 MATH&translation轨迹，hardware/temp/outcap/训练seed ND，无实现/复现。拟保留‘分时点behavior提案与单项/联合对照’接口，拒绝causal hierarchy已识别/无confounding/普遍提升。Ch80 L62修好≠原因和L267 pairedreflection-vs-retry承载一般分解，未此step-specific joint反退；拟L62后两段，root必要源/owner待核，不写Books。

### 2602.06375v1 — Difficulty-Estimated Policy Optimization

缓存 `feb10_core_06375_v1.json`，实际§3.1–3.2/§4.1–4.3/Table1–2与Fig6–7。拟5=2+1+2。BERT从rawquestion估current actor Avg@k和归一PPL，BCE+distill+ranking，100step不filter warmup后在rollout前筛极端。Avg reward不是GRPO中心化advantage，预测极端不证明将来group真零variance；原Eq9 harder题却要求更高Avg@k符号/方向含糊、§4‘isolated’warmup与§3 actor仍GRPO口径不同，未披露可重放filter threshold，不采用exactselector配方。

16/32H100、Qwen2.5 1.5/7B、Verl/vLLM、1000step/b128/G8/LR1e-6；eval32samples/temp1/topp.95。Table2 total DEPO125.65 vsGRPO121.85秒，DAPO211.69，columns非简单串行求和，不宣称freeoverhead；等steps不等generatedtokens或总qualitycost。DAPO-MATH17K极端少时改善弱，ranking过强丢≈50%数据后quality退步，误拒学习机会/多样性与BERT/PPL更新成本保留。seed/precision/inputoutcap/SLO ND，未复现。Ch33 L126真实zero groups和L316–330 onlinecurriculum未current-estimator warmup-before-rollout分支，拟zero-group后两段（不重复一般sensor）；root必要源/owner待核。

### 2602.06385v1 — Uniform Spectral Growth and Convergence of Muon in LoRA-Style Matrix Factorization

缓存 `feb10_core_06385_v1.json`（必要方法/理论prefix）与`feb10_core_06385_v1_suffix.json`（§6后半/§7）；实际§3–6必要定义/Thm5.7/6.2/Prop6.7及§7/§8限制。拟6=2+2+2：分别orthogonalize两个factor仍在受限product上形成近似同步sqrt谱动力学，改变optimizer×parameterization解释，不由Muon名望/一般rank借分。单矩阵½||AB−Y||²由identity Hessian简化，A0/BγGaussian、smallβ/γ、active modes且t∈[τ,T]；实际Thm5.7是sqrt(di)近unit而非原singularvalue常速。最小先到只在这些条件，过多rank可能把不需要方向一并长出伤generalization。

Tβ smoothed analytic flow与exactT/离散NS/momentum不同。Thm6.2 almostall-init全局min或factor-norm∞，无已知GF守恒；boundedness是额外条件，localrate需distincttargetsingularvalues且已converge；l2正则另改变objective。不授离散Muon全LLM收敛。RoBERTa/SST2与LLaMA3.2-1B/Alpaca q/v rank8只是谱观察；toy60×70/r5/η.01/γ1e-3不是质量E2E。必要claim不采数值性能，hardware/precision/seed/SLO未披露，无复现。Ch30 L109–113有初始化/LR尺度但无factor optimizer→product谱条件，拟其后两段；root必要源/owner待核。

## 2602.06204v1 — Learning Rate Scaling across LoRA Ranks and Transfer to Full Finetuning

缓存 `feb10_core_06204_v1.json`。实际§4.1–4.2、§5.1–5.4关键评价/§6限制、A.2.1/A.3必要尺度假设、A.6 FFT条件、B.1–B.3/B.6–B.8必要配置。拟5=2+1+2：具体factor初始化/有效multiplier的rank-LR与FFT必要迁移条件；Reach只微调组件，不计通用调参或所有LoRA生命周期。

原式W+αBA，α是有效multiplier而非PEFT lora_alpha；Init[A] A随机var1/n、B0，Init[B] B随机var1/r、A0。有限t、bounded forward/backward、single-sample与无momentum SignSGD代理，加A3 B/h Gaussian独立简化。Init[A], α=r^-γ给η Θ(n^-1/2 r^-(1−γ)/2)，α1是r^-1/2不是1/r；α1/r则rank invariant但A feature长到n^.5。Init[B], α1给ηn^-1且feature O1，与FFT同阶只必要不充分，不能移用相同有限常数或证明所有AdamW轨迹。

实验AdamW β.9/.999、decay.01、clip1、5%warmup+cosine，单seed42，log2 grid，分别选择training EMA-loss/validation NLL或accuracy、RL final reward及diffusion FID；峰值有限grid相邻≈2×不等精确规律。RoBERTa-large FFT最佳略低，额外classifier固定1e-3仍可耦合；不同architecture/objective不授直接最优迁移。B2 PEFT s=α*r/use_rsloraFalse，常数α1要lora_alpha=r，α1/r要lora_alpha1，不能混淆rslora。4×H200单node、BF16/TF32；LLaMA1B/Tulu1024 b32，Qwen3B/OpenThoughts8192 b8，ViT224 b512、RoBERTa128 b32，VL b32长度未披露，SD512 b8，GSM8k output1024 b8；部署concurrency/SLO不适用，本次不采用训练倍数或A6000实测。未核代码、未复现。

Ch30 `TRAIN-LORA`当前L109已要求matched LR-search，但未解释初始化与有效scale确定不同rank规律，以及FFT只必要迁移条件；拟接此段后两短段。29/31监督/偏好接口只交接，不重复写generaloptimizer；待root核原源/采用/窄位，不改Books。

## 2602.06195v1 — DeDPO: Debiased Direct Preference Optimization for Diffusion Models

缓存 `feb10_core_06195_v1.json`。实际§4/Prop1–2/Thm1、§5.1必要配置、§6/Table2–4/Fig3、supp formalproof必要假设/符号与randomization段。拟5=2+1+2，因具体Ch34监督校正接口及理论冲突必要深入；尚待root采用判断。

Eq8为all-pool pseudo loss均值，加代表性labeled的true−pseudo loss correction；Prop1需要两个pseudo均值对应相同人口，实践随机抽高质标签，不代表少量任意审校set可去全域bias。Prop2标注target被n/nl放大可越出[0,1]，它是估计器而非概率本体；标签稀少增方差。§4.4明确selftraining违反g独立训练人口条件，校正可能overfit0，frozenVLM优先。正式supp θ改为logit function/L2，不是diffusion网络权重收敛；需要独立nuisance、boundedlogits、propensity-rate和VC/ERM假设。

原Eq5/Eq18把BCE第二项写正号，与Eq21 σ−w/正Hessian不一致；不能静默修原式，不采用作者bias-free-training、网络权重速率或fully-labeled理论upperbound。有限机制只保留代表性loss校正与independence/selftraining边界，是否可以正面采用待root核；中心子命题需有限隔离。Table3 SD1.5 Qwen21.69→21.66、XL CLIP22.45→22.44，与文字always改善不一致；不删除反側。App称15independent test runs，不明示15training seeds/随机初始化因此不给训练稳健性保证。

SD1.5/XL、FiFA5K/HPDv2、25%human75%pseudo、Qwen2.5VL7B/CLIP/selftraining；SD1.5 1000steps AdamW1e-7 globalb128、2GPU/accum8，SDXL100steps Adafactor2e-8；GPU型号/precision与SDXL完整batch NotDisclosed。20DDPMSolver++/CFG7.5，PartiPrompt1632 PickScore/Aesthetic，HPSv2 3200/四类；自动reward proxies不等独立humanalignment。增加pseudo/true/correction计算，selftraining有两个额外forward，预算不免费。Ch34 L236–240现有时间标签自举，不是代表性control-variate式校正，拟此后两窄段接口/边界，不改Books。

## 已校准低分关闭与后续待核（不覆盖原AB）

## 2602.06283v1 — SOCKET（核心完成，采用待核）

缓存 `feb10_core_06283_v1.json`，实际§4.1–4.2/Algo1–3、§5.1–5.3关键假设与Lemma5–6/Remark7、§6.1–6.2及AppD scoring伪码。拟6=2+2+2，具体选择/执行接口缺口和理论实践冲突定点深入。Key硬hash到每table一个bucket，querytanhprojection向2^P corners softmax赋概率，对全部N keys累积bucketprob×valueNorm后TopK；不授sublinear免扫。Theorytarget angularkernel、samplingaggregation，Zmin/bucketoccupancy假设及fixedP τ→0，不是practicaldeterministicTopK或exactQK；Lemma5同mean variance界不证明differentmean软硬通用方差比较，Lemma6 Gaussian独立key/orthogonalprojection/smallsignal也非任意trainedKV。Algo3明确exp(hashscore)weight与§4.2/5所说subsetexactstandardsoftmax冲突，具体最终weight实现未核，不静默修正。

质量LLaMA3.1-8B/3.2-1B/Qwen3（8B与3B正文口径不一致），contextfull、QA+decode sparse，sink/local128，AVG排除PassageCount；authorrecommendedbaselinehyperparameters非matchedsearch。Figure3速度LLaMA2-7B单layer、batch1 decode-only A100/H200，不采1.5×LLM E2E/生产SLO；hashindex/prefill和cache metadata单计。precision/output/concurrency未披露。新增gradedqueryrank接口不是attentionexact，Ch22当前trainedNSA/indexer与posthoc selector不同，拟此链窄补，待root采用/owner，不改Books。

## 2602.06286v1 — Validating Elicited Beliefs（核心完成，采用待核）

缓存 `feb10_core_06286_v1.json`；实际§3.1–3.2/Prop3.3/Remark3.4/Prop3.6/IIA、AppA1、§4、§5主要test/counter、§6。拟5=2+1+2，具体decision-sufficiency接口gap定点深入。u仅(a,θ)、ε独立(x,θ,p)、A=g(p,ε)前提下，A不独立θ|p可否证任何u下的reportedbelief解释；pass不证明truebelief，随机action+randomp反例仍过。binary monotonic需IIA，方向可增或减；不把diagnose-positive的单向slope普遍化。不能由拒绝null唯一归因为‘撒谎’或非理性，而忽略context-dependentutility/noise等假设。

四诊断数据只用作通用输出/行动测量population，不采medical指导；200cases×5repetitions，GPT5high/min/DeepSeekR1/LLaMA4，CMIk3/500bootstrap95CI、CatBoostOOS nested(p,θ)/(p,x,θ)，somedeviation<1%，12/16残余仍显著是有限协议结果。prompt/p-persona变化重要；两Bayesnet未公开不授复现，理论与已有公开方法不被该附件阻塞。hardware/precision/deploybatch/concurrency/SLO未披露/不适用，不采performance。Ch66 L4115–4118 belief/action/outcome仅general三层，拟添该条件否证接口，Ch79只handoff，待root锁。

## 2602.06291v1 — Consequence-Based Utility（核心完成，采用待核）

缓存 `feb10_core_06291_v1.json`。实际§3/§4.2–4.4/§5必要反侧、§6、§7.1–7.2、§8与C。拟5=2+1+2，具体oracle不足时的neighborhoodtransfer评价gap深入。fixed(Q,C)作ICL，邻题verifiedaccuracy平均作为utility，不是原题truthoracle；Faculty最多两邻题、compactreference且$600/package。判原pool有人expert手验，rank/AUC而非probcalibration；abstract425/正文630/192=70+122与9candidate×70数量不合，避免输出统一population结论。

SamebackboneCBU/LLMjudge各64rollouts，RM仅1、GenRMdummysecondresponse+RoPE延长；reasoningmax16k、温度只recommended，硬件/precision未披露，tokens±15%非严格matchedtotalcost。112pickeddisagreement集GPT5pro初标+PhD核，说明conditionalsample不唯一cause。8rollouts误差相对64-reference不是真值精度保证。RealMath consensuslabel非independentgold，DaftMath easy邻题CBU85.58<judge93.51；太easy/hard都失辨别，构造随model变化。§8未测真正open问题；v verifier接口定义/compacttruth不足实现复核，不授deterministic部署。Ch66拟judge邻题utility两窄段、甜区/构造和共源成本，science仅test对象不采science发现，待root采用/owner。

06266 RQA3=1+1+1：3600R1-distill hidden trajectory repetition/laminarity仅complexity proxy，未新增有效stop/budget校准。06275 RoPELIME4=2+1+1：固定closedoutput/open surrogate RoPE locality、SparseK/NLL拟合局部替代未建立closedfaithfulness新边界。06300 BPU4=1+1+2：fixedweight linear/LN→conv适配局部lowering，未添通用编译保证。三者原AB/root独立校准通过，条件日期落窗，OnlyReport，非小模型/视觉排除。06337 CauGym4=1+1+2仅定向posttrain人口/五既有配方，无新失效条件，root完整AB关闭校准通过，不采reliable robust。原AB身份/dates保留inventory/all_selected_date_raw。

06283 SOCKET、06286 elicitedbelief、06291ConsequenceEval潜在保留，必要正文已取得，正在实际读，不标完成。06317 Condensate精确无损claim须深核；06319 graphbench5潜在；06339VLA结构6潜在；06341HiWET仅决定性对象准入；06345AP2即使低分仍须实际安全runtime/TTL生命周期定点深入。root已实际对应六AB校准，无全pool自动5/6分。

## 2602.06130v1 — SWIRL

缓存 `feb10_core_06130_v1.json`。实际§3.1–3.3两phase目标/条件、§4setup/必要eval/baseline/§4.5、B1/A4reward-hack/A7长horizon人口。拟6=2+2+2，因理论与实际recipe边界定点深入；新增是冻结FWM/IDM交替reward接口，不计一般world-model principle。

PhaseI以frozenIDM的logQ(z|x,yhat)奖励FWM生成可辨转移，PhaseII以frozenFWM的logP(y|x,z)奖励IDM恢复实际观测；两者分别约束可辨与data fidelity。CMI下界对frozenIDM/data成立，不识别唯一物理action；ELBO身份还要求prior=reference及β1，B1非迭代/LLM配置β.1，不能以GRPO归一化advantage/有限优化授exact coordinate ascent或全局一致。迭代VLM配置未另给β值，不推定其为1。

无actionlabel仅RL阶段：Liquid先400K编辑监督warmup，LLM先半数episode含actions SFT，另一半丢actions后RL。singleturn judge4.36→5.06属Liquid7B/Aurora具体协议，文本BLEU/BERTScore/ROUGE不是实际API执行；longhorizon最多T6但N随task完成/失败filter，重复self-improve不更好；sharedweights后轮退。不采‘纯无标签全生命周期’、‘真实因果dynamics’或各headline百分比。A4 uniqueness/长度/GPT2PPL仅排除短cipher的有限线索，不排rewardhack或隐式共同捷径。

B1 VLM FWM32×H200/IDM8×H200，LLM8×GraceHopperGH100；StableTool prompt8126/output4096，其他4096/4096，rollout64或16，temp.7/topP.96；迭代VLMtemp.75。部署batch/concurrency/SLO及precision Not Disclosed，不采用latency。Ch25 L255–257具体inverse-dynamics anti-collapse不是双phase state-only互验；拟在此后窄补可辨/data fidelity双责任和labelwarmup/β条件，待root核，不改Books。

## 2602.06127v1 — Compressing LLMs with MoP: Mixture of Pruners

原文缓存 `feb10_core_06127_v1.json` 的 `[0].text`。实际读§3.2/3.3、§4.1–4.4/Table1–3及结论必要反侧。拟5=2+1+2：等参数预算深宽混合是具体压缩机制，Reach只压缩组件；Durability只预算匹配搜索空间，不计成熟剪枝/缓存原理。

§3.2每步先选一个完整层、重算该层当前参数数，width分支以等量参数删除匹配；保留末两层、AMP head/neuron规则借自旧方法。可选proxy路径在两候选短LoRA后评分，丢弃短更新而保留对应未更新剪枝模型，最终才完整恢复。关键§4.1.1：PPL60.84、random60.83±0.43，后续实际采用random降低metric计算成本；不能将复杂选择器写成收益来源。Figure2同pipeline混合优于单轴支持联合搜索空间；三seed不构成robustness guarantee。

LLaMA7B仅校准，LLaMA2-7B/3-8B文本与LLaVA1.5-7B多模态；Alpaca恢复LoRA（文本r32/α10，多模态r8/α16）、AdamW3e-4、b16两epoch。§4.2大部分baseline复用他文预算，不能合并为严格matched端到端排名。§4.3 RTX4090，LLaMA2-7B，输入12/输出128、batch1、20runs弃10warmup，余10墙钟；precision、concurrency、SLO Not Disclosed。2.21→1.36秒只受测40%条件，未采用通用39%改善或energy保证。§4.4文本恢复在受测VLM任务改善，仍有明显能力损失；不授通用跨模态恢复。

具体owner候选 `INFER-TENSORRT-LLM` Ch49 L469–489已有mask目标/保护集/执行验收，但没有深宽等参数匹配与random≈proxy这项反侧。拟在稀疏段前窄两段；尚待root原源/评分/写前核，未改Books。

## 2602.06161v1 — COVER

缓存 `feb10_core_06161_v1.json`。实际§5.1–5.3、§6.1–6.5、AppB.1–4。拟6=2+2+2：新增双视图cache/verification接口跨sampler与attention-state，不计成熟cache原则；因exactness宣称定点深入。

mask seed input后drafting仍读前步seed KV；verified seed自己的diagonal改回mask计算的KV。单row校正 `r=1+α(expδ−1)`，减旧diagonal value、加新diagonal value并renormalize，AppB只在固定Q及off-diagonal KV单attention层成立。它不证明全网络causal leave-one-out、AR target distribution exactness或无间接泄漏。Keep/Replace/ReMask依threshold，最多B15，seed不能连续选；uncertainty/incoming/outgoing attention仅选择proxy。§6.5 KV drift Spearman .540–.716 mean.637是相关，不是稳定性保证。

LLaDA8B系列/Dream7B、4H200、greedy/temp0、block64、输出256/512，相对one-token baseline，concurrency/SLO Not Disclosed；不采11.64×通用speed。w/oKV同时去override与diagonal，不能单独归因diagonal；remask百分比分母COVER有replace、baseline没有，不能直接拼合。权重不变也不授推理路径无新content风险。Ch24 `MULTIMODAL-GENERATIVE-PARADIGMS` Self-revision具体provisional/revision-budget已有，但没有双视图self-diagonal机制；拟在普通provisional段前窄两段，待root写前核，未改Books。

## 2602.06181v1 — Uncertainty Drives Social Bias Changes in Quantized Large Language Models

官方exact-v1 abs/HTML现题名与旧DataCite标题Investigating…不同，同ID/作者/Submitted；原字段标题不覆盖。缓存 `feb10_core_06181_v1.json`。实际§3.2–3.4、§4.1–4.5、§6、A6/A9/A10/A11必要对象。拟5=2+1+2，因安全评价负侧定点深入。十模型五PTQ/13英语biasdatasets，closed-choice为length-normalized likelihood，open为greedy；paired1000permutation/bootstrap、FDR.05。受测aggregate不变仍逐例双向flip，subgroup可能相抵，不能授所有bit4劣于bit8或通用安全precision。

A6由单人盲标400responses且按detectedchange分层，Guard部分PPV40–55%、NPV88%只该采样人口；absolute open-ended flip可能含误报。A11 Qwen.5B/5322selectedBBQ，SimPO与EntropyMax还改weights/preferences，entropy相关/干预不证明唯一cause。vLLM/L40S或H100、4096input，512output或FMT10K每turn150；batch/concurrency/SLO Not Disclosed，不采用吞吐。

拟已有覆盖：Ch49“量化验收不能只看平均分”L1049–1061实际已承载aggregate→perexample→drift/slice、artifact/evaluator身份及非安全保证；新增实验证据未给更强可验证precision策略。待root核Existing，不改Books。

## 2602.06183v1 — To 2:4 Sparsity and Beyond

缓存 `feb10_core_06183_v1.json`。实际§3/Algo1–3、§3.2、§4/§5.1–5.2及关键表/微核反侧。拟6=2+2+2：forward/backward六FFN GEMM按operand选择weight2:4或activationVenom，具体布局与trainingobjective跨边界；不计一般稀疏原则。

SquaredReLU自然activation sparsity，W1列cluster、token router与batch行permutation使邻接tokens共pattern；W1/W2转置soft-threshold，activation优先Venom。源文cosine/L2文字与伪代码差异保留，不声称逐行实现已核。训练H200，LLaMA3-1B/7B DCLM；warmup1000后sparse在前/dense在后，1B30k+30k，7B10k+38k。Table4激进sparse退步，恢复预算model-specific；平均loss最近100steps，无多seed不确定性，不授全任务无损。

headline1.4–1.7×不是实测完整training E2E；§3.2/§5.1为FLOPs/roofline+microkernel算式，Table2 1.352/1.387与正文1.37也不完全一致，不采倍数保证。pack/router/permutation、PP摊销与假定通信overlap需另计，Blackwellscatter/gather消除permutation只是作者推断非实测。拟Ch28 `TRAIN-PRETRAINING` Dynamic Sparsity段后窄补sparseoperand/physicalpattern与dense-recoveryphase分工；待root核写锁，未改Books。

## 2602.06154v1 — MoSE

缓存 `feb10_core_06154_v1.json`。实际§2.2–2.4、§3必要对照/transfer、§5及A1calibration配置。拟5=2+1+2：nestedexpert prefix切片与full/random双宽训练、router概率→widthmapping为局部MoE替代，不计一般条件计算原则。

上投影列/下投影行按width共享prefix；每batch全宽+randomwidth双forward，成本不免费。Selectedexpert probabilities经γ次方normalize，Γ分配后clip并.05离散；clip后不授严格总Γ预算。γ在OWT50batches×b6，SGD.01，base/router冻结，perbudget校准后freeze；有限文中没有给离散切片的梯度实现，不能说实现已核。GPT2 55M/322M/1B、OWT3–15Btokens，A100x4 DDP，LM/零样本；MFLOPs/token不是实测latency，precision/concurrency/SLO Not Disclosed。LAMBADAtransfer有accuracy波动；初训嵌入多宽，posttraining弹性未验证，self-speculation/Agent仅未来应用。

拟Ch21 `MODEL-MOE` 当前异宽group L253与elasticpath L257之间，具体区分‘切同expert prefix’与‘去不同宽度expert组’，可仅报告γ实验配方；待root核Evidence及具体owner差额，未改Books。

## 2602.06317v1 — The Condensate Theorem（中心争议，待独立终裁）

缓存 `feb10_core_06317_v1.json`；实际§2 Def1–2/Theorem1/Corollary2–3、§3.1–3.5、§4、§5/Table4、§6.1/6.5/6.6、§7、§8.2与CodeAvailability必要raw。拟6=3+1+2，新增全AR无损/固定support及总线性复杂度主张直接冲突现有attention解释，需深入反证，不以小模型或proprietary排除。

Def2只在anchor/local/trueQK TopK上重新softmax；Theorem1把cosine=1.0及唯一manifold当普遍恒等，§2末称按QK选择‘exact by construction’。§3实际GPT2Medium/Large同prompt greedy共1500+token匹配，仅支持披露轨迹argmax匹配，不等attention vector恒等；cosine1.000既有显示精度也不识别向量norm。Table1/2在anchor/local65上仍有12.2%→4.2%tail，这不是完整TopK集合的质量表，不能偷换为所用97集合反证数，但证明mass接近本身不等零tail；§5把>99%mass当mathematicalidentity的推导仍不足。有限精度可能使部分tail下溢或输出相同，却没有必要precision/rounding条件、证明及误差界。

§4明确每query对全K计算QK需O(n)scan，又把总算量写O(n(W+k))；selection成本未包括在总claim。§7把‘所保留KV逐项精确复制’推为lossless selective deletion/≈97cache，但query-dependent未来TopK如何在删历史后恢复未解释；不能从局部操作exact推整个模型/状态exact。RTX4090Laptop16GB、PyTorch2.5/Triton3.6、b1、8heads×64、W64/k32，precision/多请求/concurrency/SLO及完整模型E2E未披露。OOM比较用平方外推、公开仅慢reference/validation，全部speedbenchmarkproprietary，未核代码/实现，不采用headline或复现。

拟整体中心争议暂缓，有限greedy/mass观察不写Books。Ch22当前L62 exactdense对比、L205–218稀疏访问图改变、L340选择器扫描成本及L107–115finite-state exactrecall已承载相关责任，但不能给争议家族正面Existing/Evidence。只接受精确勘误/充分finiteprecision等价证明、含QK-selection/KV生命周期的完整复杂度与必要可核artifact后重开上述子命题；不请求全部附件或无限版本diff。待root独立必要原源/终裁。

## 2602.06341v1 — HiWET（决定性对象，贡献前关闭待校准）

缓存 `feb10_core_06341_v1.json`；实际§III L134–150、IV-A L151–184、IV-B L190–198。world-frame commander将EEF/base状态转structured base/frame subgoals，低层proprio policy输出PD jointtargets；upperbody KMP reference+residual、lowerbody absolutejointtarget。新增是humanoid whole-body tracking controller的局部接口/运动学配方，没有foundation/VLA表示、模型条件生成或新的模型安全适用边界；不是因RL/RO、机器人或World暂停而排除。只为对象准入读到这些段即STOP，不声称评价无价值或已读全文；待root关闭校准。

## 2602.06339v1 — Why Do VLA Models Hallucinate?（必要命题就绪，采用待核）

缓存 `feb10_core_06339_v1.json`；实际III环境/latenthead定义、IV-A Ass3/9/Lemma10/Ass11/Thm12、IV-B Def13/Lemma14/Thm15–Cor16、VI限制、A1拓扑短证明与B1必要tubevolume段、D-A受控对象/训练评价。拟6=2+2+2，新增条件性action-generation几何边界跨actionhead与physicalconstraint接口，非借用一般‘生成不等安全’原则。

在fixedstate、pathconnected开放latent、全支撑密度positive且连续totaldecoder下，若同时覆盖断开的safecomponents且其间是openforbiddenzone，seam原像非空open→非零unsafe mass。不是所有VLA在任意场景必hallucinate；discrete/mixedmode/gating改变前提。Thm12另需Gaussianlatent、BR局部Lipschitz、2Wmargin/in-ballmass与tailq(R)，因此W/L比较只在同假设下，不能由实测proxy推出全局L或架构排名。Precision Def13 compactC1 k<d manifold与小δtube，Lemma14把safeprob上界写tubevol×densitybound；Thm15另需C1、boundedprior、finite-to-one、nonsingularJacobian，满足小δ质量须局部densityconcentration（fold/contract），并非完整VLA训练收敛或controller保证。Finite-stepDDIM/Flow并非一概diffeomorphism；只在该另假设满足时才能用Cor16。

VI明确deterministicdynamics，perception/partialobservation/memory/stochasticity抽象掉；horizon product是成熟局部风险复用，不加分，本次拟不采用verification-amplification全部rate。D-A2DGaussianlatent、two flow/diffusion同4×256MLP/LN/SiLU、AdamW2e-4、b2048/100ksteps，每seed1M采样/b4096；L用2048truncatedGaussian点finite-diff.01proxy，不是certifiedL。seed个数/硬件/precision/SLO未披露，不声称真实robot风险率或实现复现。Ch26当前VLA段L166–173的localGaussian形状/FAN已提示多峰抹平，却无connectedlatent→disconnectedsafe支持的结构前提与thin-contact density边界；拟其后两短段连接离散mode/局部refinement与低层controller，不授新模型/安全部署。25预测owner/27训练数据只handoff，待root采用/窄锁。

## 2602.06319v1 — GrAlgoBench（标准核心，owner待核）

缓存 `feb10_core_06319_v1.json`；实际§2.1–2.3/§3.1–3.3及AppE必要合同。拟5=2+1+2，新增fixedtopology增文本vs扩graph两测量与selfverification局部反侧，不因benchmark格式拒绝，也不由宽长上下文原则借分。9graph任务、6nodes档每格50、2700原题；§3.1另三任务各50graph固定80nodes/200edges，仅改nodename length得到4k–64k，控制topology难度但改了lexicalrepresentation，不能归纯token数量/内部memory机制。Judge分类300ER样本/三编程学生subset一致未给全量groundtruth因果。

§3.2按wait/but/so等entropyword分段，Qwen2.5-72B与gold定位首次正确/各段selfverify及发现旧错；只在已有正确答案response算outcomeefficiency。有限<30%selfverify有效和>0.88首次正确前tokenratio是conditionaltrace观察，不由judge标注和相关性证明‘selfverify主要cause’；无stop/interventionablation。AppE每题k8、部分R1/V3/GPT5/Gemini仅k4，pass@k/cons@k分母不直接排名；temp.6/topp.95/minp0/outcap32768、boxedexactstringmatcher。3.3代码tool在三task两level局部改变execution路径/成本，不授普遍工具胜模型。硬件/precision/deploybatch/SLO与total成本未披露；必要主张读足即停，未核代码/复现。拟有限评价结论仅报告或具体Existing待owner核，不能写新通用思考stoprule。

## 2602.06345v1 — Zero-Trust Runtime Verification for Agentic Payment Protocols（安全深入，处置待核）

缓存 `feb10_core_06345_v1.json` 从本日已有exact-v1-bodies/2602.06345v1.html只读提取；实际§3 threat/TCB、§4/Algo1、§5.1/5.3–5.5.3、§6.1–6.4。拟4=1+2+1仍必要安全深入：newlocal AP2-style gate配方，signature/context/nonce成熟原则不加durability。TCB可信、keys不可破、strongconsistent SetNX为前提；nonce首次使用后TTL=Δt阻replay仅该window，algorithm未验证futuretimestamp、时钟容差扩大后state期限等必要情况，不授nonce check与downstream effect exactlyonce。

§5.5.2原load10kTPS仅10秒，TTL5/30/60/300，平台是trace完成后的有限entry，不能外推为并发inflight数约束。持续activeentries随rate×retentionwindow，虽不随无限history增长，却不是peakconcurrency；§6.2用60秒‘仅severalMB’也未给entryschema/replication。平均3.8/3.720ms只PythonHTTP→mockbackend simulation，CPU/硬件/cryptoalgorithm/precision/concurrency/seed/SLO未披露；threeattack/四gateconfigs为作者模拟，不授官方AP2缺陷或生产100%安全。作者原仅引Google2025AP2announcement，无specrevision；一次官方spec route恢复404，不展开协议版本history。Intent/promptinjection、TCB compromise与sidechannel明确excluded，‘不改format’与newnonce/contexthash字段兼容未具体锁version，保持未采用。拟Books仅报告（局部模拟/中心storage夸大无新可信机制）；Ch72现paymentboundary及AgentTool/idempotency原论证待具体对照，root采用待核。

## 2602.06346v1 — FlowConsist（root采用通过，Ch24已写待POST）

缓存 `feb10_core_06346_v1.json`；实际§3/4.1–4.2、§5必要消融/CFG反侧、AppA方差身份与B配置。6=2+2+2。普通singlepoint FM条件均值身份不能保证totalderivative平方等价，额外Tr(JΣJᵀ)参数相关；但当前Ch24 L434已具体承载，不重复写。Eq7仍有conditional监督，只把JVP方向换F diagonal marginal，Σ非零不自动强迫所有J为零；Thm3积分残差不授范数单调。新增采用Eq10–11 real F diagonal/fake G自产clean重加噪双估计器与stopgrad整流角色；Eq9标量logdensityratio缺score梯度记号不静默修作exactKL定理。

SiT131M/676M、ImageNet256；B/2 pretrained300K，XL/2 REPA初始化，b256/Adam1e-5/β.9,.95/EMA.9999、80/200epochs/50k评价samples。Best FID各CFG搜索，highCFG整流后diversity下降/FID退步；aux G/自产/CFG×2NFE成本不删。硬件/precision/seed/SLO ND、无实现或实验复现。root必要源/owner差额通过，Ch24 L436/438实际两段、末注1804已写待actualPOST；其余drift势函数/SnapFlow原分支保留。

## 2602.06355v1 — Di3PO（采用/owner待核）

缓存 `feb10_core_06355_v1.json`；实际§3.1–3.2/4/5.1–5.2。拟5=2+1+2。正确词/扰动20%字符词同一次diptych生成，Canny或middle split成pair，Gemini验证背景/有字与confidence>70，300pair；源模型需要diptych能力，负例必须符合目标模型错误分布。新增是控制非目标视觉context的配对接口，不是普遍训练sample效率或exactgradient targeting。

原Eq4符号/weight展开有歧义，Eq5从同noisy pixel推共享network参数梯度相消不成立；跨regionattention/convolution耦合，生成/VLMfilter不授pixelperfect。Table2有backgroundvariation DPO及winningSFT，2000heldout×4生成seeds、1000bootstrap不是多trainingseed；8TPUv4/b16/900steps/Adam3e-8、50denoise/CFG7.5，SDXL/SD3局部OCR评价，precision/resolution/SLO ND。Imagen3 teacher/synthetic验证调用和选择偏差另计，无实现/复现。Ch34 L273–275已有generatorgap但未此samegeneration视觉配对分支，拟其后两段；root必要原源/owner待核，不写Books。

## 2602.06358v1 — SHINE（采用/owner待核）

缓存 `feb10_core_06358_v1.json`；实际§3.2–3.4/4/5.1–5.4、AppA reshape/B2生成验证/B5–6必要成本/C2架构。拟6=2+2+2：frozenbase+MetaLoRA从每层M memory提取，M≈rD/H是容量设置非无损定理，M2P沿layer/token双向交替，再reshape全层targetLoRA；Figure2明确extraction与parametergeneration两阶段，singleforward不授完整仅一次base调用。Base/Meta/Memory/M2P/generatedadapter角色分开，无testtimeoptimizer不等无训练成本。

Qwen3-8B/Meta128/generated8/M148/4M2P/context1150，8A100/AdamW，6B预训练加MQA/1QA；Qwen-Flash生成+同model验证不是独立gold。Table1F1 55.6vsICL69.4、multi-turnhistory变长反退，lowPPL不授完整source召回；.3s局部amortizable、FLOPs/scalarcount估计不授生产SLO。precision/batch/concurrency/seed ND，未核代码/复现。Ch30 L702生成低维适配原则、L497–512 source派生identity已承载一般边界，但无多层双轴M2P interface，拟L702后两短段；root待必要源/owner核，不写Books。

## 2602.06359v1 — OGS（安全/gap必要读，采用待核）

缓存 `feb10_core_06359_v1.json`；实际§3.1–3.5/Algo1/§4、AppA1–4、§5setup/ablation、B/D1–3。拟6=2+2+2。SmallNavigator+固定400generalanchor的几何选择domain/replaycluster→Target普通LoRA为接口增量；不是projectionoptimizer，也不采用naturallysafe。Nearorth absolutecos可微负，finiteη曲率、anchor平均/stale及rawgradient≠AdamW有效update均限制保护。AppA2最大dot与normalizedcos排序非等价（除非norm另限定），proof无domain目标；Eq8 general对fixedanchorConf不直接证明对recentdomain冲突。

Algo1多episode每Navigatorstep重算与Target动态state，不支持singlepass+rho忽略policy成本；AppA4Spearman.4–.7只是posited/局部，非scaleinvariant保证。A10080GB/LoRA16/alpha32/AdamW2e-4/b8effective64/3epochs，seed/precision/maxlength/PPOepisodebudget ND；24.5hvs1.6h只selectionphase，不采E2E/nooverhead。w/oReplay/general反退保留、matched10%token预算仍不等总compute，无实现/复现。Ch27 L1027OPUS currenteffectiveupdate及L1013 generalupdateconstraint未此Navigatortransfer+fixedanchor datafilter分工，拟OPUS后两短段；optimal/safety/cost子命题隔离，root待采用/owner核。

## 2602.06366v1 — 贡献前决定性关闭（root实际通过）

缓存 `feb10_core_06366_v1.json`；实际F/G结构L78–104、render/collision/intent反馈L120–139。已有topdown trajectory→outcome/concerns/建议，G objectxy/rotationdelta→collisionawareplacement→render→sameG修意图；只preliminary场景闭环demo，无agentretraining、新selector机制或可迁移新失效条件。Collision-valid不等intent可达的边界是成熟区分，不借通用feedback/schema分数。root实际原段核通过pre-denominator closure，不列候选/不评分/不只因未做普遍证明拒绝；对象判断已够即STOP，不扩附件。
