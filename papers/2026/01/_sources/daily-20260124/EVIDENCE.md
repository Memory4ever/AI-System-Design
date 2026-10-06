# 本日必要证据笔记（冻结74家族，日级验收通过）

当前有效范围（2026-10-04T11:58:30+08:00）：74候选必要核心作者审阅与root有限独立原源核已完成；15698只达到身份终态隔离，不授正面安全证据。普通扫描/筛选/核心/Books写入待办0；6整合正文/邻接/末注POST通过（15394 Ch28；16093/16192/15655 Ch23；16140 Ch72；15625 Ch33），5已有覆盖、60仅报告、3暂缓，最终逐项处置以本日README为准，root整日Gate已通过，外部/中心隔离不授正面Coverage/Evidence。支持与直接反侧足够即停止，代码未核、实验未复现。以下保留必要原证据；原笔记产生时的root待核/Books待比是非执行快照，不是当前普通待办。15914原5分假设只作被改判历史，不是74候选/最终评分。

## [RCORE](https://arxiv.org/html/2601.16211v1)

当前必要源核：root已实际定点通过采用范围/隔离边界；非全篇证明、代码或复现。

精确v1 §3/4/5/C（core L232–252/290–307/513–532/873–882/1179–1196）：对象/动词共现偏置的seen/unseen受控分离，random ViT/CLIP对象94%、unseen verb1.9%是有限组合人口，不证明所有foundation模型内在因果。旧closed-world限制候选组合和test-label-biased调参掩盖seen overprediction；本稿open-world全verb×object与仅validation调参分别报告，改变组合泛化评估条件而不是单增榜单。VOCAMix用FAME高motion foreground与别物件静态midframe混合、保留verb标签；TORC反向时间features与entropy约束，不保证所有混合语义有效。CutMix/Mixup HM低于baseline，局部Lcos/Lent合用最好，foreground相对全背景仅约.2差额，不授每组件普遍必要。Sth-com79k/161verb/248object、EK10071k/82/228；8V100、3×16×224²frames，CLIPB16+AIMadapter/verb temporalconv/objectavgpool、CoOp prompt，C2C与RCORE同30epoch/bs128/lr5e−4或1e−4/warm3/temp.07；非所有引用baseline重训同协议。precision/inferencebatch/end-to-end成本/seedCI Not Disclosed。2+2+3=7深入必要机制/评价反侧完成，独立复核待办；Books待PLATFORM-EVALUATION-SYSTEM的组合支持与调参隔离具体比较，不把FSP/FCP相关性当唯一因果。

## [PointBridge](https://arxiv.org/html/2601.16212v1)

当前必要源核：root已实际定点通过采用范围/隔离边界；非全篇证明、代码或复现。

仅精确v1 §3/5/C（core L138–164/281–290/847–852），v2 Jan24 02:32Z在截止01Z之后，不迁入本窗：Gemini2.5Flash识别类别但定位不可靠→Molmo7B点→SAM2 mask shrink20%→FoundationStereo depth/calibration/FPS robot-frame points，policy PointNet+BAKU/MiniLM6；是policy points-only，不是整条pipeline无RGB。sim GT mesh投影为相机可见点并1cm Gaussian噪声，MimicGen保持相对EE pose的SE3扩增；匹配观察视角比全物体点更适合本地sim-real，randomcamera帮助不证明任意pose/所有object泛化。遮挡/杂乱、错误VLM或丢失环境context失败，低频限制动态任务。3atomictasks×4objectpairs×5human→每对300 MimicGen/每task1200；45real demos cotrain/3pairs，soft/articulated各20real-only，不硬把错配asset物理sim当有效。FoundationStereo RTX5090 TensorRT单模块10Hz，Ethernet异机整体5Hz；RGBD/QuadroRTX8000整体也5Hz，与depth quality比较不同职责，不能授零shot/全loop15Hz。precision/batch/完整策略成本/seedCI Not Disclosed。2+2+3=7深入必要机制与部署反侧完成，root待核；Books待MULTIMODAL-EMBODIED-VLA具体观察可见性/闭环成本论点，非新point cloud名字缺口。

## [CamPilot](https://arxiv.org/html/2601.16214v1)

当前必要源核：root已实际定点通过采用范围/隔离边界；非全篇证明、代码或复现。

精确v1 §3/4/C（core L130–166/327–331/407–420/710–725）：video latent+Plücker camera进入4block per-pixel3DGS decoder，用rendered depth warp与visibility mask只奖励conditioning已见区域；全GT逐像素reward对新区域的随机合理生成有错误惩罚，blur也可hack reward。Masked MSE+LPIPSλ.5及novel-view训练支持受限几何reward alternative；learned depth/visibility非真值保证，静态3DGS不能表达动态场景，RE10K数据不授任意world dynamics。CogVideoX5B-I2V 8ControlNet blocks/pretrained+zero linear、decoderhidden1024；三阶段Adam lr1e−4/3e−4/1e−5、bs16/32/16、10k/100k/5ksteps。作者decoder8.44GB/.559s对videoVAE43.17GB/5.602s发生在ReFL，旧80GB每iter仅两temporalframe而新可更多frames，不授完全同工作量/全推理10倍；w/oReFL/visibility/novelview反退是有限对照，CFG相近但训练成本更高，不等每组件独立因果。GPUtype/precision/一致frame workload/seedCI Not Disclosed。2+2+3=7深入必要机制/反侧完成，root待核；Books待MULTIMODAL-GENERATIVE-PARADIGMS与WORLD-MODELS观察可见性/未见区域不确定性的职责比较，不采用不完整投影记号为几何保证。

## [IVRA](https://arxiv.org/html/2601.16207v1)

当前必要源核：root已实际定点通过采用范围/隔离边界；非全篇证明、代码或复现。

v1 III/IV/VI（core L80–107/162–169/262–265/281–295）：冻结视觉中间patch cosine→截正normalizeaffinity，在LLM少数层只pool visualtokens并λconvexblend，alternative前置局部结构prior而非新参数/retraining。flatten保留tokenindices不等空间信息数学丢失，cosinesimilarity不是same-object真值/semantic不变保证。LLaRA VIMA80k12%train、20randomseeds；OpenVLA/FLOWER LIBERO原超参只λFLOWER=.2，OpenVLA76.5→77.6作者local；real10episodes每modelsetup匹配、最多5retry仅无法产action，不能当500trials/单shot，oracle detector与无detector两人口不混。RTX6000Ada LLaRA2.00→2.06s并15.8GB同，precision/batch/token数/seedCI全任务overhead Not Disclosed，不能称所有model3%或对无人机/危险控制安全。2+1+2=5标准完成，root待核；仅报告受限frozenvision prior重新注入VLA条件，不授全任务grounding因果。

## [PyraTok](https://arxiv.org/html/2601.16210v1)

当前必要源核：root已实际定点通过采用范围/隔离边界；非全篇证明、代码或复现。

v1 §3.2/4.3/D（core L96–123/245–252/493–542/1458–1474）：pyramidal visualfeatures+language-conditionedLFQ共享binarycodebook、分层token带separator ARalignment，非languagealigned=semantictruth。Eq2将binary{-1,+1} c、q或textembedding直接写KL/entropy，概率化/维度映射未披露，不采用它作为已定义分布或定理/保证；冻结decoder与“decoder randomlyinitialized”implementation句身份不清，保留精确实现缺口而不替作者补公式。局部ablation w/oLaPQ/text/AR/drift重构降，architecture和作者empiric可独立报告，但不授每loss因果/更高PSNR必然video理解正确。Wan2.2LVAE/LoRAr16α32/Qwen2.5VL3B AWQint4/DINOv3reference，128A10080G，30k/60k/180k三stageAdamW1e−5perGPUbs4→2/16+1..96+1frames/至4K；Table1 latencyV10025frames256²另protocol，不把训练集/分辨率总差抹平。trainingprecision/accumulation确值/各对照完全compute/CI Not Disclosed。2+2+2=6标准必要机制/实现冲突边界完成，root待核；仅报告exploratory codec architecture与局部loss组合反側，不采普遍semanticconsistency证明/未披露实现可靠性。

## [Feature-space Smoothing and PSM](https://arxiv.org/html/2601.16200v1)

当前必要源核：root已实际定点通过采用范围/隔离边界；非全篇证明、代码或复现。

v1 §3.2/4.3/5/S7–S9（core L149–179/237–244/483–494/732–765/1033–1077/1280–1299/1351–1378）：先区分featurecosine与decoder输出语义，不能把l2特征证书直接授文本正确/safety。必要公式发现Lemma1写变reference x的selfscore却proof fixed x_c；任意unitencoder fe=+1于(0,1)/−1其余，在0左右S_hat跳Φ(1)−.5及其补，inverseCDF不连续，故原selfscore1Lipschitz普遍命题隔离。S25除||Efe||≤1后cos≥dot只dot非负，负值方向反，general负FCSB不采用；fixed-reference/单位norm/非零期望/positivebound的Corollary需root定点确认，不由作者隐含补条件直接授原命题。实验独立保留LLaVA1.5-7B/OpenFlamingo9B caption100图、ImageNet10class500图（第11shark攻击target），caption/ACC/targetASR是有限攻击协议；ScienceQA应用不展开。PSM需训练purifier+mapper不是所有组件trainingfree，mapper8epochbs16AdamW2e−4；n0=1→16推理.28→2.10s、ACC非单调86.2→89.6(n8)→89.2(n16)，硬件/precision/CI/attackadaptive整体核范围 Not Disclosed，不授攻击穷尽。2+2+3=7深入必要机制/证明边界完成，root争议定点待核；Books暂缓受影响certification保证，局部实验仅报告，不把错误推广成全篇无贡献。

## [LLM-in-Sandbox Elicits General Agentic Intelligence](https://arxiv.org/html/2601.16206v1)

当前必要源核：root已实际定点通过采用范围/隔离边界；非全篇证明、代码或复现。

精确v1 §2.1–2.4/3.1–3.3/4/E（core L116–117/168–178/435–442/485–500/798–802/823–825/935–960/1276/1424–1461），非后来改名版本：documents环境file按需读而非全塞prompt，在same-sandbox两配置average35.6→48.9但Qwen反退，smaller23.7turn wanders→训练后7.0不等工具本身授generalintelligence。context-task outcomeGRPO++ local探索，Qwen4B/30BA3B lr1e−6bs8G8/150与50steps/noKL/temp1topP.8topK20/maxturn100、response65536；不得把markdown/verification phrase增加当faithful推理因果。仅采用context/agent/infra，科学应用subset不展开也不以六领域聚合宣称本项目全任务省token。prefill环境token≠ARdecode成本，DeepSeekQPM .6x反退而MiniMax2.2x，37–51%envtoken/执行<4%作者测量，end2endtoken不能直接linearFLOPs/所有成本；1.1GBbaseimage+runtimepackage与task-specificimage不同生命周期，512×200MB/2TB约5%非真实峰值trace/全DGXserver成本。Docker“ensuresisolation”不授网络/权限/恶意代码安全保证，hardware/precision/batch/concurrency/CI未完整披露，不复现。2+2+3=7深入必要核心完成，root待核；Books需AGENT-CONTEXT/MEMORY与PLATFORM/TOOL exact职责比较，非文件工具新名gap。

## [DistSeal](https://arxiv.org/html/2601.16140v1)

当前必要源核：root已实际定点通过采用范围/隔离边界；非全篇证明、代码或复现。

v1 §4/5.5/6/A/H（core L145–196/567–604/871–880/1364–1371）：posthoc latent watermarker→distill generator或decoder，fixedmessage部署owner不同；可公开替换decoder时decoder-only无法持久，生成器水印又会被LoRA非水印50单类ImageNet例削弱，tradeoff不是防篡改保证。AR quantization会语义改图所以不使用重构loss，pixel discriminator/strength约束不是imperceptibility证明；UViTHDCAE512²与RARXL256²/256tokens1024codebook不同压缩比不直接合并speed。posthoc600kAdam5e−4bs128，RARdistill32GPUbs2048lr1e−5/10ksteps约50GPUh；FID50kImageNetval、bitaccuracy经有限augment不是semanticownership/authentication/全伪造安全。原H写“.82%/.76%”与检测语义尺度有冲突，本文不采用这些数，仅定性forgetting和公开decoder替换边界，precision/GPUtype/inferencebatch/20x计时scope/CI Not Disclosed。2+2+3=7且安全边界深入必要核完成，root待核；Books待Ch72 provenance/watermark改动owner具体差额，不能因已有水印主题直接Existing。

## [ActionMesh](https://arxiv.org/html/2601.16148v1)

当前必要源核：root已实际定点通过采用范围/隔离边界；非全篇证明、代码或复现。

v1 §3.2–3.3/4.2/limitations/C（core L173–226/288–326/843–848）：temporal inflatedattention/RoPE同步预训3D latents，noise-free source t0且无loss/每stepclamp→stageII共享frozenencoder预测reference mesh vertex displacement，保留fixedtopology。相同Gaussian noise perframe仍orientation/geometry不一致为具体反侧，不授sharednoise=jointconsistency；stageI改善CD4D .187→.069但noStageII没有可动画统一拓扑，必须结构输出而非仅metric。固定connectivity不能topologychange，遮挡/坏reference失败，FlashAttention2不改变(NT)^2数学复杂度。Objaverse/internal13200seq16frames，BF16AdamW1e−4wd.01bs96/170ksteps，3min16frames作者claimhardware/推理成本scope/seedCI Not Disclosed；DAVIS真实只qualitative、不授free任意physicalmotion/transfer因果。2+2+2=6标准完成，root待核；仅报告共享latent生成与reference deformation两职责受限alternative，不新增通用物理worldmodel保证。

## [Full-to-Full Masking Curriculum](https://arxiv.org/html/2601.16150v1)

当前必要源核：root已实际定点通过采用范围/隔离边界；非全篇证明、代码或复现。

v1 III/IV（core L85–86/98–107/151–173/575–583）：singleencoder melody+harmony合成1000train/100test，随机chords无harmony-to-harmony依赖，旧randomstage未恢复预期对角而FF全mask早期→逐渐可见形成条件attention；只是map观察不能授attention因果或所有crossmodal模型。HookTheory15440/95–5split及650jazzOOD，3RTX3080AdamW1e−4bs8、200epochs但旧curriculaearlystop/FFlastcheckpoint不等严格training预算，评价诸musicmetrics不是人类听感、未来才listening。temp.2topP.9，原uR10%称固定10calls但remaining10%递进一般不保证10步全解，不采用无条件调用数/端到端speed；HRC直接有旧R10%胜反侧。hardwareprecision/seedCI/实际epochs/token成本 Not Disclosed。2+1+2=5标准必要反侧完成，root待核；仅报告mask课程对有限条件依赖学习的验证，不开展音乐应用、普遍因果或curriculum理论。

## [360Anything](https://arxiv.org/html/2601.16192v1)

当前必要源核：root已实际定点通过采用范围/隔离边界；非全篇证明、代码或复现。

v1 §3.3/4.1–4.4/0C（core L207–221/307–314/338–344/590–609/691–705/1599–1604）：ERP像素先左右各W/8环wrap再VAEencode、裁多余latent，不改DiTsequence长度；traininglatent zero-padding可令无seam像素产latent边界，所以不能仅decoderblending/rotateddenoise治全部来源。Table5 DS image9.92→blended5.29→CLE3.87/video35.52→19.84→13.28支持受限target-boundary修正，非数学seam-free所有VAE/receptivefield，encode额外crop/pad实际预处理非“全pipeline零开销”。FLUXdev Adam5e−5bs51250k/50sample shift3.16，Wan2.1-14B1e−5bs64/20k50sample shift3，同公开data/captionGemini2.5Flash；randomcamera augmentation数据/表较好不授模型真正学geometry因果。81frame/blackborder/physics继承局限，hardware/precision/seedCI/latency/cost Not Disclosed。2+2+3=7深入必要机制/反侧完成，root待核；Books待Ch23 codecboundary/Ch24sampling具体owner比较，非新panorama名gap。

## [SAMTok](https://arxiv.org/html/2601.16093v1)

当前必要源核：root已实际定点通过采用范围/隔离边界；非全篇证明、代码或复现。

v1 §2.1–2.3/3.2/B/D（core L122–133/155–169/187–202/784–790/994–1005/1116–1155）：mask codec以(image,mask)编码而非图像无关ID，SAM2.1Large冻结image/promptencoder、训maskdecoder/RQ256×2不共享；512mask词+start/end扩MLLM vocabulary，仅projection+LLM训、210M量级原209M masks与5M conversations。支持input/output同两离散token接口、nexttoken语言loss但codec仍CE/DICEloss，不说完全无segmentation监督。GRPO reward依据GT codeword匹配/去重TP和未去重分母，不是连续maskIoU reward，近形但不同code仍可能被惩，不授token equality=geometry correctness。RQ1024×4重构.75高但generation77.3低于1024×2的78.3，codec容量与LLM predictability不单调。A10080G、codecbs1024lr4e−5/LLMbs256lr2e−5/GRPO1e−6，不等所有baseline同训练预算；precision/卡数/epoch/推理latency完整decodecost/CI Not Disclosed。2+2+3=7深入必要机制/评价反侧完成，root待核；Books须实际Ch23 region representation与Ch24 code-interface比，不为SAMTok新名字造gap。

## [Explicit State Dynamics for Agents](https://arxiv.org/pdf/2601.16087v1)

当前必要源核：root已实际定点通过采用范围/隔离边界；非全篇证明、代码或复现。

v1 HTML404后PDF原件必要页4–7/10–11实际读：externalVAD经固定VADER近似proxy，firstorderα1或secondorder μ=.8/.95，state经natural-languageprompt反馈；7BAR4bit准确modelidentity/hardware/temperature/batch/contextcost Not Disclosed。单固定25turn哲学扰动→reconciliation、每condition5seeds共20runs，μ.95所有run未恢复、μ.8曲率不同，支持有限state inertia/响应延迟取舍，不授真实情绪/人类persona/safety。所谓stateless无hysteresis“byconstruction”、firstorderα1即时update与stateless数值同而反馈有无不同，不证明纯state memory必要或数学path-dependence独有；恢复时间随外部reconciliation不能只归momentum，不能用five modelseeds当五独立dialogue populations。2+1+2=5标准必要机制/直接反侧完成，root待核；仅报告explicit controller的受限运行现象，不把经典低通/动量公式重命名计理论新贡献。

## [EDIR](https://arxiv.org/html/2601.16125v1)

当前必要源核：root已实际定点通过采用范围/隔离边界；非全篇证明、代码或复现。

v1 §3.2–3.4/4.1/4.4/5/B2（core L204–220/532–537/550–574/952–955）：准入仅旧CIRCO同MLLM text-only优于image+text的模态必要性反侧，不计新15类别排行榜/一般难度提升；平均与model×population结果不能保证所有样本image冗余，更难EDIR不等无shortcut。QwenImageEdit共享源基础修改+distinctchanges生成hardneg，Qwen32B两stage judge过滤且partiallyincorrect仍可能pass；image+文本控制保持source但合成数据/MCG judge非全人类真值。5000queries、225kLoRA Qwen2.5VL7B bs128/2500steps/imgtokens1280/seq1500lr3e−5wd.01/InfoNCE.03；定阈“R1>60或增>20”区分solvable不证明data vs intrinsicarchitecture因果。训练hardware/precision/测试batch/CI/inferencecost Not Disclosed，三condition合成不足生产semantic grounding保证。2+1+2=5标准完成，root待核；仅报告受限CIR评价模态消融，不泛化RAG/所有multimodalembedding。

## [Multilingual Model Merging](https://arxiv.org/html/2601.16127v1)

当前必要源核：root已实际定点通过采用范围/隔离边界；非全篇证明、代码或复现。

v1 §3.2/4.1–4.2/5.1–5.2（core L226–243/268–271/294–297）：同Llama3.1-8B five语言各LoRA r/alpha64、4epochlr2e−5bs8seq8196，summarization3000/其余5000train、500val/test，TIES/DARE/KnOTS已知组合本身不计新。采用local single-language更新节省与跨语言回归风险取舍，不能由summ/reasoningnearparity授merging跨任务无损；Englishsentiment约15point反退、新English+5000重训EN后仍不胜combined而其他三语言也变。Initial并行35%time少不等35%GPUhours少；维护70%成本节省baseline重训全部而非partialCPT，对照workflow不同。DAREdensity1=TIES因不prune不计独立好证据；labelspace解释只是待测hypothesis，3B/8B两点不证明sizeagnostic。hardware/precision/并行设备数量/计费口径/merge+eval成本/seedCI Not Disclosed。2+2+2=6标准完成，root待核；仅报告任务依赖的adapter维护局部经济性与质量反側，非新merging机制或长期保真保证。

## [Mecellem](https://arxiv.org/html/2601.16018v1)

当前必要源核：root已实际定点通过采用范围/隔离边界；非全篇证明、代码或复现。

v1 §3.5/4.1/4.3（core L628–639/657–675/699–713/741）：准入仅MLM-loss下降却posttraining retrieval退步反侧，不保留Turkish/legal配方。ModernBERT-base155M版本v5→v6 MTEB55.76→52.76/Legal47.52→41.89、MLM loss更低；但dataset不断refine且v5改seq1024→2048，虽图声称tokens/validationparity，也不授纯继续训练导致overfit/形态语言特殊因果。单run deterministiccheckpoint不等训练无seed方差；80/20heldout无数据泄露是作者协议而非独立审计。InfoNCE/GISTguide同bs768lr2e−5seq1024局部对照，另一seq256因train99.9%覆盖却retrieval退步，须目标长度而非training分布单定。precision/本项推理hardware/batch/CI与真实索引成本 Not Disclosed，不采normalized ProductionEfficiency=productionready。2+1+2=5标准完成，root待核；仅报告特定checkpoint代理目标与检索职责，不能由领域SOTA授新通用检索机制。

## [Sawtooth Wavefront Reordering](https://arxiv.org/html/2601.16032v1)

当前必要源核：root已实际定点通过采用范围/隔离边界；非全篇证明、代码或复现。

v1 §2–4/Algorithm4/limitations（core L71–82/243–255/258–280/293–312）：GB10 48SM/24MiBL2作者配置、splitQ streamingKV，工作集≈20MiB起非coldmiss；相邻Q局部iteration交替正逆KV扫描减少reuse distance，非换Attention数学、非L1所有工作负载无用。原CUDA B1/2/4/8配置tile80×80、head64；CuTile tile64²/B8/S128K/head64，同硬件causal及noncausal都减miss、后者61→69TFLOPs与causal41→66TFLOPs，rawCUDA1.3→2.4TFLOPs是另一受控kernel不是CuTile/生产引擎速度。tile128被compiler拆分扰访问模式是直接成立边界，1−1/SM只是所测同步wavefront关联非普遍cache theorem。precision/clock/重复计时CI/完整model/多head生产concurrency/SLO/compiler版本 Not Disclosed；kernel级结果不授端到端/所有GPU/数值误差精确相等。2+2+2=6标准必要机制/反侧完成，root待核；仅报告具体遍历×cache×compiler交互，不为旧sawtooth名字产生Books gap。

## [HyperAlign](https://arxiv.org/html/2601.15968v1)

当前必要源核：root已实际定点通过采用范围/隔离边界；非全篇证明、代码或复现。

v1 §4.2–4.3/5.1/Table1/5.3（core L125–160/228–248/387–415）：latent/timestep/prompt→encoder+decoder生成dynamicLoRA，stepwise/initialonce/piecewise adapter更新取舍，把test-time reward反传摊入训练不是免训练align；Bayes近似不授proxy reward=真实人类分布。SD1.5/FLUX/HPSv2训，Pick-a-Pic/HPD scorematchingregularizer；4H100/50steps CFG7.5/3.5，FLUX base15s对I16/P17/S20，S HPS较高但IR1.251低于P1.280；reward-only CLIP下降直接反侧，不以preferred-data保证杜绝rewardhacking/diversitycollapse。6AI feedback有训练reward同源，userstudy/定性只能相应人口，不授普遍human preference。precision/batch/分辨率/训练预算/计时scope/CI Not Disclosed，BoN20与epsilon20×4是不同资源点，不把300s比较作等预算优越。2+2+2=6标准完成，root待核；仅报告state-specific operator adaptation与局部成本/代理目标边界，不新增通用对齐保证。

## [PhysicsMind](https://arxiv.org/html/2601.16007v1)

当前必要源核：root已实际定点通过采用范围/隔离边界；非全篇证明、代码或复现。

v1 §3.2–3.3/4.1/4.4/5及直接反侧案例（core L287–310/654–655/834–843/2200–2207）：只取foundation/world-model评价，不开展科学应用。paired real/sim rigidbody短≤10s、60fps至4K，VQA选项与video trajectory/lever终态分别测；VLM real较好但generation sim几何较好，支持一个realism/dynamics评估不能替另一人口，不授appearance cause。CoM指标是maskIoU/几何centroid，不是真实质量分布中心；主文自己案例“torque推左沉却GT A balanced”，annotation存在直接冲突，不能由其error总率归物理reasoning错或评判某模型安全。Table n5 std有限作者结果，模型endpoint版本/temperature/seed/输入帧/生成长度精确配置/hardware/precision/batch/cost Not Disclosed，dataset待acceptance发布，无复现。2+1+2=5标准与评价反证必要核心完成，root待核；仅报告局部matched-domain跨任务排序及标签/代理指标边界，不采用全模型缺基本力学/真实因果/机械控制可靠性。

## [TeNet](https://arxiv.org/html/2601.15912v1)

当前必要源核：root已实际定点通过采用范围/隔离边界；非全篇证明、代码或复现。

v1 §4.1–4.2/5.1/5.3–5.7（core L129–150/181–189/214–256/285–321）：冻结Llama3-8B text→hypernetwork一次实例化约40K state-action policy，trajectory只在训练MSE/InfoNCE grounding；同Prompt-DT加HN改善而加规模小幅，支持语言与参数化控制接口的有限alternative。Direct已见multi-task有效但未见meta任务落后；grounding局部改善不是所有任务必须；ML1 50→1600训练task成功.80→.99同时heldout固定10%，域距离也变化，不授纯scale因果。严格offline/Mujoco+MetaWorld，3seeds×每task50rollouts，非真实视觉/机器人验证。9300Hz仅policy作者表、硬件/精度/batch/计时边界/语言编码和权重生成成本 Not Disclosed，不是端到端9kHz重新读指令。2+1+2=5标准必要核心完成，root待核；仅报告实例化控制器与runtime language conditioning的受限替代，不授zero-shot arbitrary任务/安全。

## [The Latency Wall](https://arxiv.org/html/2601.15914v1)

历史非执行记录：已按原AB/§2–4贡献关闭，不评分、不Books；原准入假设/读取保留下方。

v1 §2.1–2.3/3.1–3.2/4（core L58–80/121–148/151–154/177–217）：七情绪UIBVFED avatar对FER2013，off-the-shelf CLIP/SigLIP2与FER-finetunedViT，i7-1265U/32GiB/PopOS22.04 CPU-only五run平均；CLIP-Large avatar22.88%/1730.94ms，ViT-FER27.42%/193.58ms vs human63.64%/189.80ms，支持accuracy与latency必须共同测目标域，不将分类/检测版本差额归架构因果。140ms是作者预设感知/渲染预算，10ms capture/render假设未实测，算53.96+193.58=247.54ms而非实际VR闭环SLO；precision/batch/输入尺寸/threading/编译优化/CI Not Disclosed，未评优化/量化替代，不能称Transformer根本不适合CPU/所有SOTA须GPU。2+1+2=5标准完成，root待核；仅报告具体预训练视觉配置目标域与预算反侧，不作临床疗效/通用domain-shift定律。

## [Progressive Power Homotopy](https://arxiv.org/html/2601.15915v1)

当前必要源核：root已实际定点通过采用范围/隔离边界；非全篇证明、代码或复现。

v1 §2/Assumptions2–5/§4.2–4.3（core L68–90/122–127/151–170/311–324/440–465/477–492）：E[exp(N f)]与Gaussian权重扰动，递增N/缩σ但floor b>0，K×J梯度样本并非原mean objective；global-neighborhood结论须mean optimum与essential-sup optimum同唯一点及严格gap、近极值质量下界、迭代有界。Lipschitz/light tails本身不保证二者同点，不能把这些条件称普通训练自动满足。小梯度极小期望也不能无额外条件直接授位置收敛；未采用其全局训练/complexity保证，不展开无关proof。两层ReLU合成orthonormal teacher、每步30样本/5000test、100experiments同initial、种群K=1/各方法35000iterations，表中k20 n20本法SR4%对SLGHr10%，no universal domination；原proof smooth条件与ReLU实验不等同。hardware/precision/实际算力与配置/CI Not Disclosed，oracle最佳test-iterate不是部署选择。2+1+2=5标准核心与理论适用边界必要核完成，root待核；仅报告限定优化alternative与成本/假设，不进入通用foundation optimizer理论。

## [EvoCUA](https://arxiv.org/html/2601.15876v1)

当前必要源核：root已实际定点通过采用范围/隔离边界；非全篇证明、代码或复现。

v1 §3–6/7（core L229–241/246–265/285–318/321–332/493–509/538/594/615–618）：task与executable evaluator共同合成，exec成功后reward/evaluator差异manualspotcheck；restore错误前state须一致才造correctivepair，semantic-equivalent参考只是匹配假设，firstdivergence≠必然causalerror。RFT budget按局部pass@k及denoise、step-DPO/error-recovery分责，不将data replay与平台100k规模宣传计增量。Qwen3VLThinking8/32B、OpenCUA7/32/72B；OSWorld 50step作者56.7与base41.6、顺序actionspace/coldstart/RFT/DPO/iteration增量非所有等compute消融。temp0仍variance说明GUI环境随机不能把pass@k全归model diversity，但无controlled perturbation不授唯一环境原因。gateway control/data分离/QEMU-KVM+Docker是公开设计而非已核安全/吞吐实现；100k concurrent/一分钟boot未实际trace/workload/hardware，不授生产值。训练hardware/precision/batch/epochs/token成本/CI Not Disclosed；§7 onlineSTEPO仍探索且更新成本高，不视为主模型已完成RL保证。2+2+2=6标准核心完成，root待核；仅报告受限state-consistent supervision与环境噪声评价，不为异步术语或新排行榜造长期差额。

## [Controllable Code Completion](https://arxiv.org/html/2601.15879v1)

当前必要源核：root已实际定点通过采用范围/隔离边界；非全篇证明、代码或复现。

v1 §2.3–4/4.2–4（core L198–218/227–228/587–612）：同prefix/suffix有多unit-test正确实现，ICC功能pass@1与仅正确子集instruction-following分开；SCC AST/type/linecount不验unit-test，不能把二者直接合并成全正确代码率。五模型同ICC去instruction后IF下降而pass@1近不变/个别改善，直接说明unit-test不能替用户实现约束，新排行榜本身不计贡献。2195Python in-filecases，judge Claude3.5与senior developers98%只是10轮子评估，结构检查非全规范语义；多模型greedy1024outputlimit/vLLM、markdownextract。SFT200k synthetic/10gramdecontam，64A10080G Adam3e−5/warm50/bs1024/TP2/context4k，只该任务；fine-tune SCC好但ICC受basepass限制，不授普遍code可靠性、overfit因果或多语言/whole-repo适用。precision/inferencehardware/CI/端到端latency Not Disclosed。2+1+2=5标准完成，root待核；仅报告功能测试与实现指令评价边界，不迁入领域代码配方。

## [Stable-DiffCoder](https://arxiv.org/html/2601.15892v1)

当前必要源核：root已实际定点通过采用范围/隔离边界；非全篇证明、代码或复现。

v1 §3.1.2–3.3/4.1/5（core L177–208/209–237/238–262/1715–1720）：2.5B同compute curriculum AR/AR-styleDLLM/直接BiDLLM，smallblock AR预训练好、block32在转换前排序可反，BiCPT还损block1；采用有限training-context/inference-block条件，不授mask条件就是错误监督或定义TokenReasoningKnowledge已证明真实reasoning。AR→Bi固定attentionmask只warmup corruption、暂去1/u权重，loss/gradspike受控变小，非仅降低lr或FlashAttention kernel新成果。smallblock clip u>=1/B使expectedmasked>=1，仍可能零mask，另force一个token才保证supervision；改变mask/loss sampling不声称精确原ELBO或无偏梯度。Seed-Coder preanneal/packed8192/1.3Tsubsample/block4、SFT继承且packed samples互相可见，非独立样本注意力隔离；warmup效果与weights/drop组成未全独立消融。hardware/precision/batch/lr/实际compute预算数/seedCI及端到端速度 Not Disclosed。2+2+2=6标准必要核心完成，root待核；仅报告该AR→diffusion CPT训练/解码条件，不授全语言模型最佳配方/普适reasoning解释。

## [GOSV](https://arxiv.org/html/2601.15801v1)

当前必要源核：root已实际定点通过采用范围/隔离边界；非全篇证明、代码或复现。

v1 §3.2–3.3/4.1–3/limitations/B/E1（core L123–145/179–193/260–267/334–335/571–573/655–661）：REINFORCE联合Bernoulli head masks而非独立local headscore，zero-vsmeanactivations导致低overlap与不同intervention行为，支持干预选择依赖于patch策略，不证明disjoint自然安全通道或所有安全恰在30%heads。四7/8B openmodels English、100AdvBench train但完整520含train overlap，再313StrongReject外测；单A10080G/Adam.1/500epochs/K32、256输出、three seeds，MiniLM语义目标与HarmBench classifier不同judge不为真值。>30% PPL升而ASR回落可能毁语言能力，不以ASR下降当safety恢复；同语料/预算匹配localgreedy attribution直接因果对照未明，不授必胜global attribution。whitebox介入可绕行为不代表blackbox可攻击，defense未设计；precision/batch/temperature/端到端成本 Not Disclosed。2+2+2=6且安全受影响核心加深完成，root待核；仅报告受限组件干预替代和评价边界，不采用普遍定位/原生平台安全保证或输出任何攻击artifact。

## [DeepVerifier](https://arxiv.org/html/2601.15808v1)

当前必要源核：root已实际定点通过采用范围/隔离边界；非全篇证明、代码或复现。

v1 §4–7（core L151/160–187/190/205–228/374–410）：trajectory摘要→可查源specific claim/subquestion→fresh外部verification→judge/feedback，分别去decomp/verification对照显示错误detect precision高不等recall/任务成功，原groundtruth参考轨迹两human errorpoint重合63%只该annotation人口。GAIA-Web/Claude3.7 samebackbone Table2完整75precision/71.43recall、去verification100precision却14.29recall；测试重试正确→错误持久，DeepSearch best47而10轮44/初41、Browsebest10而最终9，不能称更多verifier迭代单调更好。400WebAggregatorQA baseanswers+正确判断筛选的DeepVerifier-4K为4646prompt-response，不把名称4K当精确数量或合成筛选judge当无误。GPT4.1/Qwen8B有有限迁移，seedCI、hardware/precision/batch/token预算/端到端latency Not Disclosed，完整fresh source和summary成本未同等baseline配平。2+2+2=6标准必要核心完成，root待核；仅报告局部verification颗粒/误否定与反馈预算条件，不把成熟decomposition recipe或排行榜授长期新证明。

## [Demographic Alignment Beyond Marginals](https://arxiv.org/html/2601.15755v1)

当前必要源核：root已实际定点通过采用范围/隔离边界；非全篇证明、代码或复现。

v1 §3.3/4.1/4.3/5.2/6.2/limitations（core L154–174/177–194/225–228/240–244/255–276/311–317）：Phi3mini4k OpinionGPT demographicLoRA vspersona/base，同193WVS questions每item500独立responses/temp.9。Marginal Wasserstein/TV改善与variance外扩不能自动授结构representative；跨十subgroup meanresponse矩阵构question/topic correlation，Table2 persona .625高于Opinion .594而marginal反向，更大topicaggregation排名又变。重要采用范围是**subgroup均值相关**，不是个体jointresponse/covariance，因为每题独立采样且已聚合，作者也自承无法respondent层评估。Reddit/sourcepopulation/English/WVS文化norm限制不可视无偏人类alignment真值，单smallbase/十非intersectional群体不授全模型/全人群偏差。hardware/precision/batch/seedCI/成本 Not Disclosed，permutation/split-half是描述界限不是分布因果。2+1+2=5标准完成，root待核；仅报告marginal指标与群体聚合结构评价职责，不纳survey应用或普遍demographic校准。

## [Spatial Role and Following Diagnostics](https://arxiv.org/html/2601.15780v1)

当前必要源核：root已实际定点通过采用范围/隔离边界；非全篇证明、代码或复现。

v1 §3/4/6（core L69–88/126–136）：Unreal5.5/120frames30FPS、五scene×八variant每class40clips、两background/相机变化，matchedmotion/attacker-role/heading30°控制；固定clothingidentity较好而roleflip/heading仍难，能识别fighting与跟随方向/角色绑定不等。NVILA8B/VideoLlama3-7B/Gemma3-4B/QwenVL7B等两runs，video看fullclip/image均采frame，输出再过BARTmnli label映射；Gemma解释prompt改善部分因为少输出造成classifier猜测，不能归视觉能力；Qwen解释反可害。near50following只合成细角度案例，不授普遍VLM不懂following或safety部署，clothingcue不证明坐标结构唯一必要。hardware/precision/实际采帧数/temperature/batch/CI Not Disclosed；多scene资产变化不等真实街景验证。2+1+2=5标准且风险反侧定点完成，root待核；仅报告参考稳定/输出解析混杂盲区，非安防系统/真实人类风险判断。

## [VideoThinker](https://arxiv.org/html/2601.15724v1)

当前必要源核：root已实际定点通过采用范围/隔离边界；非全篇证明、代码或复现。

v1 §3.1–4/4.1/4.3（core L104–130/167–168/286–306/313–326/365）：caption-only teacher tool trajectory→同interval视频tokens替换并训student直接视觉tool reasoning，突破必须用强video teacher写trace的训练依赖，只保留这种carrier迁移与条件。Qwen235B-A22B/7BVL，CG10k五trajtemp.7，答对筛选但若全错会随机保一条，故trace非正确证明；4H200/3epochs MS-Swift，inference32frames/每帧max32768pixels至多64frames，confidence为answer几何均prob而非校准risk。四benchmark与base7B局部改善，<2min近无益、τ1与moretopk退化；训练预算/字幕工具与baseline不全配平，precision/batch/lr/end2endlatency/seedCI Not Disclosed。2+2+2=6标准完成，root待核；仅报告textual process supervision→visual input接口及有限工具预算取舍，不授faithful reasoning或普遍比72B好/生产成本低。

## [DualShield](https://arxiv.org/html/2601.15729v1)

当前必要源核：root已实际定点通过采用范围/隔离边界；非全篇证明、代码或复现。

v1 III-C/IV-B/D/E（core L148–170/238–245/252–266/316–318）：同HJ value分别做diffusion soft guidance与执行时robustCBVF-QP，采样层偏好不代替action安全约束。只是该generator/planner边界，不将成熟HJ理论当新贡献。QP允许ϵ>=0、cϵ=1e8软化安全不等式，有限罚不能授zero-violation forward invariance；网格HJ相对动力学/最坏boundedcontrol与1s horizon、只three nearest static obstacles进一步限制全场景安全。1:4合成intersection/2HV+20障碍、100trials=10配置×10而非100独立场景，MBD同horizon/warmstart、DualGuard同HJ，0collision/100success只是作者局部经验；实际planner更慢，不把完成行驶时间当compute latency。Xeon8358P离线HJ3h、JAX/Nd100/warm5/samples2000/horizon50/dt.1，precision/batch/实时决策walltime/CI Not Disclosed，无真实vehicle验证。2+1+2=5标准且安全slack定点加深，root待核；仅报告proposal guidance/执行shield局部取舍，不授formal deployment安全保证。

## [BVS](https://arxiv.org/html/2601.15698v1)

当前必要源核：root已实际定点通过采用范围/隔离边界；非全篇证明、代码或复现。

v1 §3–4（core L87–147/148–175）：采用拟审的是图像局部benign并不蕴含组合/重建后安全与只选择原本会refuse的人口，而非具体攻击指令。原paper称GPT-5 Jan12及Gemini1.5Flash Jan15 2026生成图片；Table1 JSR98.18/95.45%、MIDOS vsrandom81.82/98.18皆依赖未明的真实imagegenerator和toolchain，不能授这些model的安全失败率、内部attention因果。有限官方能力核查：Google原[models说明](https://ai.google.dev/gemini-api/docs/models/gemini?hl=sl)历史索引列gemini-1.5-flash输出Text，官方[Jan2025 app更新](https://blog.google/feed/gemini-app-model-update-january-2025/)区分Gemini2.0与Imagen3，与论文直接native imagegeneration身份不符；不擅自替作者猜App/Imagen路由。两judge全同意不是human policy真值，样本由GPT拒绝筛选并不代表普遍人口，temperature/endpoint/precision/hardware/batch/成本/重复runs Not Disclosed。2+2+2=6且安全核心定点加深；中心实验身份争议待root实际核，暂缓正面证据/Books。重开只需该Jan事件具体endpoint/modelIDs、UI/API实际imagebackend/tool routing与逐样本条件，不要求全安全附件或生成任何有害artifact。

## [Agentic Uncertainty Quantification](https://arxiv.org/html/2601.15703v1)

当前必要源核：root已实际定点通过采用范围/隔离边界；非全篇证明、代码或复现。

v1 §3/4/AppendixA3.3（core L118–143/257/338–351/441–452/817–844/877–908）：confidence+理由随history保留，低confidence触发N3/最多D3 reflection，仍不足才恢复fullbuffer，已有memory/reflection原则不计原创。局部UAM-only/UAR-only/full与有限h对照显示过程metadata和fullhistory可改变失败/预算取舍；min/last/avg trajectoryconfidence是不同聚合，不是probability真值，min随步数改变不保证global-success可靠性。ALFWorld/WebShop max50steps、DeepResearch100、GPT5.1/4.1/4o/Gemini2.5/Qwen235/DeepSeek3.1、open H200 vLLM，System1temp0/System2.7、τvalidation .8–.95，标准.85/research.95。UAM ECE好≠full全指标都好，UAR BS好≠因果解决epistemic而非aleatoric；相同action归一string或judge等价不是真实计划语义证明。成本图是平均APIcalls不是token费用/端到端walltime，反射spikes与<7B自信表达退化限制；precision/batch/length/concurrency/seedsCI Not Disclosed，Gemini judge并非无偏。2+1+2=5标准完成，root待核；仅报告局部风险metadata保留/回读预算条件，不把forward/inverse新名称或榜单写成长期新原则。

## [FlexLLM](https://arxiv.org/html/2601.15710v1)

当前必要源核：root已实际定点通过采用范围/隔离边界；非全篇证明、代码或复现。

v1 III–VI（core L173–183/212–233/307–382/390–412）：HLS模板允许prefill token/weight并行与decode block reuse，hybrid temporalreuse/spatialFIFO组合，SpinQuant boundary rotation移除、INT8attention/INT4其他linear及lmhead为硬件完整integerpipeline。只Llama3.2-1B，U280304/292MHz实际board测、V80300MHz为RTL/P&R后从U280缩放估计；A100 BF16 HF与INT4GPTQ-Marlin vLLM非同SpinQuant/质量配置。WikiText2 BF16 PPL8.94vs原SpinQuant13.3/改12.68说明质量仍有差，非无损加速。长prefill短decode[1024,256] GPU优、长decode[512/1024,2048] FPGA优势，1.29x end2end/3.14x tokenJ只U280作者特定配置；V80数字不称实测。HMT压缩改变模型state/质量，64K理论noHMT>1h不是实际等质量加速，采样power只board/non-systemfull。batch/concurrency/tailSLO、vLLMversion/CI Not Disclosed。2+2+2=6标准完成，root待核；仅报告该smallmodel的质量/硬件实现边界，不外推普遍GPU替代或生产吞吐。

## [CompliantVLA](https://arxiv.org/html/2601.15541v1)

当前必要源核：root已实际定点通过采用范围/隔离边界；非全篇证明、代码或复现。

v1 III-B/IV/V/VI（core L152–183/236–244/319–347/368–372）：冻结VLM结合图像/语言/force做contactphase与impedance建议，实时force α∈[.2,1]修stiffness，low-level damping计算不依赖VLM实时推理。新增采用force-constrained原VLA成功率与限制，不把传统VIC组合本身计突破：八LIBERO/ManiSkill contact任务Pi0/RDT1B/OpenVLA-oft、30N过阈值终止，4RTXA6000，平均9.86→17.29%只该安全定义，不混原benchmark成功率。真人实物多数任务失败，唯一较易push成功还截actionchunk前两步与clip输出，故不能把force下降当真实部署成功/普遍safety guarantee，也不把VLM当highfrequencycontroller。temporalforcecalibration、网络/API延迟、precision/batch/CI、VLM单组件与force修正独立消融 Not Disclosed；作者明示API成本/频率限制。2+2+2=6标准且安全反侧定点加深完成，root待核；仅报告所限局部safety评价/执行分责，不将此配方当长期闭环安全证明。

## [Continual Panoptic Perception](https://arxiv.org/html/2601.15643v1)

当前必要源核：root已实际定点通过采用范围/隔离边界；非全篇证明、代码或复现。

v1 IV-B–D/V-B/D5/D8（core L108–160/214–215/722–723/858–865）：同sharedencoder的mask/text分支仍会分别漂移，以旧model与当期数据contrastive/instance distill及cross-modal consistency约束，caption协助segmentation pseudo labels。采用局部跨task旧/新class取舍，不把通用KD/组合或remote-sensing应用计新原则。FineGrip15-5/15-2、ADE20K/COCO、MaskFormer/Mask2Former ResNet101、2A800/PyTorch2.1/CUDA12.7、lr.01poly/每CL步90epochs；CPP SAPL旧/全部改善却新类退，CPP+新/全部改善而旧/背景caption小退，consistent alignment不能自动等于全旧能力保持。CPP+与CPP backbone也不同，S/RQ解释自相混乱不采用一般机制因果；oldmodel更可信是假设不是真值/校准。exemplar-free仍用新数据、teacher产物，非datafree/隐私保障。800²计额外多分支成本，precision/batch/端到端SLO/seedCI Not Disclosed。2+1+2=5标准必要核完成，root待核；仅报告该受限multitask稳定/可塑冲突，非所有基础模型continual guarantee。

## [PersonaSwitch](https://arxiv.org/html/2601.15708v1)

当前必要源核：root已实际定点通过采用范围/隔离边界；非全篇证明、代码或复现。

v1 §3.1–3.2/实验（core L107–121/306–324/356–372）：两个固定zero/role prompts从同一个已选prefix各自greedy生成到双换行，按step平均top1−top2 probability gap选择下一步，不是raw logit或已校准confidence。五benchmark、Llama3.2-3B/3.1-8B/Gemma2-2B，random/lowgap及token/step/whole granularity对照，step优而token差，支持受限commit粒度选择；persona不添加事实只是规范假设，prompt可能改变prior，不授semantic invariance。两路额外forward未与预算完全配平，hardware/precision/batch/端到端latency/CI Not Disclosed。2+1+2=5，标准必要核心与root独立核通过；仅报告局部粒度取舍，不把该配方写成通用安全控制。

## [MoLLIA](https://arxiv.org/html/2601.15773v1)

当前必要源核：root已实际定点通过采用范围/隔离边界；非全篇证明、代码或复现。

v1 method/ablation/implementation（core L138–161/177–189/246–263/354–395）：五7–9B LLM logits与采样一致性训练XGBoost、50初始标注及σ.9 sparse pseudo；δ.001同时低概率class作负标签，old-iteration learner与committee disagreement对CE下权α.5，避免当batch learner泄漏，不是校准概率。AGNews/IMDB/TREC/PubMed分类、A40 DistilBERT/RoBERTa max128、40epochs/earlypatience10、每轮50、lr5e−5，negative/discrepancy去除有局部退化；false negative按全label-space分母不是class条件安全界。2+1+2=5标准及root独立核通过；仅报告局部负监督/伪标签冲突处理，不能外推全领域ensemble优势或风险保证，未作临床采用。

## [Cross-Embodiment Latent Control](https://arxiv.org/html/2601.15419v1)

当前必要源核：root已实际定点通过采用范围/隔离边界；非全篇证明、代码或复现。

v1 II-B/D/E、III-A/C/D、V（core L79–100/135–164/166–176/329–354/417）：借用contrastive retargeting，新增五body segments的共享latent与embodiment-specific embedding，以human cVAE latent displacement生成EE目标控制。四robots训练sharedcore，三新robots只训adapter；whole-body同setup对照腿部映射差，segment恢复视觉相似，可报告跨形体局部替代。HumanML3D29224motions/4Mposes+URDF FK均匀采样robotposes，A4000/PyTorch Adam1e−3 batch1e5，1000初始/目标每robot只rightarm评估。TableIII TIAGO1.14cm，故不照录所有平台sub-cm；约100Hz未明确计时hardware/precision/batch/tail，15分钟adapter不是完整zero-shot新robot。无手部/复杂contact、安全collision保证、所有动力学迁移或全体robot闭环普适性；variance/seed/总trainbudget Not Disclosed。2+1+2=5标准完成，root待核；仅报告受限kinematic latent/adapter分责，不把control frequency当部署SLO。

## [MiRAGE](https://arxiv.org/html/2601.15487v1)

当前必要源核：root已实际定点通过采用范围/隔离边界；非全篇证明、代码或复现。

v1 §3/4.2–3/5.2.2/limits（core L245–269/286–312/389–394/457–485/493–498）：生成与verifier同proprietary Gemini2.5Flash/GPT5mini、多hop/description成熟配方不计新贡献。采用有限新反侧：finance2/14docs ablation，description-only与image+description总体指标接近，image-only visual grounding更高但faithfulness较低；QA包含图像不保证必须看图，1093finance QA仅84multimodal，description使图冗余只是作者hypothesis，不授已辨识因果。visual grounding/faithfulness/hops采用LLM/VLM judge未人类独立验收，JSD_topic不是任务真实性，成本高未定量。hardware/precision/batch/temperature/contextlimits/端到端latency Not Disclosed。2+1+2=5标准完成，root待核；仅报告表示泄漏/visual necessity与overall QA指标分责，不采用q-bio应用或泛RAG配方。

## [Lasagna](https://arxiv.org/html/2601.15507v1)

当前必要源核：root已实际定点通过采用范围/隔离边界；非全篇证明、代码或复现。

v1 §3.1/4.1/4.4/4.5/limits（core L148–166/278–288/325–341/363–414/420）：type/IO/timestep区分条件与noisytargets，joint composite/background/foreground+effects denoising支持三mask模式。新增可编辑层carrier与原图编辑对照，不仅新dataset/SOTA；242samples、单object背景/影子效果，同object layer编辑加入effects与只分割object对照，报告局部视觉一致性而非真实物理规律。DiT/T5，512²batch6/1024²batch1、AdamW1.2e−5/2k warmup/20kiterations、DDIM50；正文noise ε目标与称flow matching表述不一致，不据此采用精确FM推导。FID/CLIPFID及GPT4o评分无盲human/多seedCI，joint与single任务的全训练预算匹配未明，不能把synergy归因独立组件。hardware/precision/latency/concurrency Not Disclosed，尚不支持多交互object一遍生成。2+1+2=5标准完成，root待核；仅报告可编辑layer representation的受限替代，不授coherent joint samples数学保证。

## [AdversaRiskQA](https://arxiv.org/html/2601.15511v1)

当前必要源核：root已实际定点通过采用范围/隔离边界；非全篇证明、代码或复现。

v1 §3.2.2–3/§4.2：falsepremise detectability（纠正/反驳前提）与longform factuality F1@K=8不是同一指标；六model与Qwen3-30B长回答subset，H100/temp0/max8192、GPT5不能设temp例外。GPT5curation/GPT5mini评分同family不授无偏，human90–95%只stratified部分，invalidresponse剔除改变分母不能直接排序。longform adver/nonadver无显著统一下降，不是“注入无害”：law反向更好同时事实数6.4→8.1，长度/采样不配平；最小效应/CI不足不授统计等价。precision/batch/concurrency/modelinputlength/SLO Not Disclosed。2+1+2=5标准完成，root待核；仅报告falsepremise辨认与剩余fact正确性职责，不采用高风险专业意见。

## [Scope-union KG-RAG](https://arxiv.org/html/2601.15429v1)

当前必要源核：root已实际定点通过采用范围/隔离边界；非全篇证明、代码或复现。

v1 §III-E/IV-B/V/limits：同question人口、prompt/zero-shot/temp0/.2/.5，NoRAG/两scope/联合KG六配置；Llama8B更宽union Probe1 macroF1 .85→.65、Probe2 .50→.40是局部直接反侧，三replicates/Welchtest统计力有限。Probe2由相同KG交集造题，representation/canonicalization/filter与corpus内容共同改变，不把反侧独立归因给graph breadth、也不以“大模型参数知识更强”解释被证实。retrievaldepth/reranker固定无搜索，hardware/precision/batch/length/concurrency/SLO Not Disclosed，后续更强ranking可改变选择。2+1+2=5标准完成，root待核；仅报告固定retrieval条件的scope/union负侧，不纳医学应用、不把通用precision-first计新贡献。

## [Pairwise Causal Text Evaluation](https://arxiv.org/html/2601.15479v1)

当前必要源核：root已实际定点通过采用范围/隔离边界；非全篇证明、代码或复现。

v1 §III-2/IV/V/limits：12textual slices显隐、句内外、单/多pair，detect存在关系与extract全部关系不等；八annotatorsκ>=.758、只100%同意样本，题目选择可能偏。promptvalidation/test disjoint，seed4000/temp.7/bs64，top-k写.7含义未清，不用这种配置称可复現。DeepSeek detection领先而extraction回退，missing约60%被作者归预算截断；不授模型内因果能力排名。§IV4称Hungarian但实际逐最高未匹配pair移除为greedy，不是globalassignment，bandmapping不能当校准概率；scoring/最佳prompt/单testpass限制所有exactscore采用。文本断言因果不是现实干预causaldiscovery，clinical阅读优势不采用。hardware/precision/outputbudget/SLO Not Disclosed。2+1+2=5标准并定点核指标反侧完成，root待核；仅报告multi-pair输出预算与detection/extraction分责，非泛新taxonomy。

## [False-premise Natural Questions](https://arxiv.org/html/2601.15674v1)

当前必要源核：root已实际定点通过采用范围/隔离边界；非全篇证明、代码或复现。

v1 §§2/3.1/4/AppD：GooglePAA 202medicationqueries随机DFS max10、两trials，4012uniquequestions非directpatient独立轨迹；536由GPT5+mini同意A/B问题，10models、无extrasystemprompts。评价是response纠正/neutralize premise且不添错，不是普通answer truth；近似正确fact/disclaimer不能代替纠正前提。GPT5humanagreement分类75%、response85%，training/validation约60平衡但judge同family/selecthighconfidence限制真实人口率/模型排序；不以16.1/7.5%直接作任意人群风险。sequence错误率相关不授因果传播。temperature/precision/hardware/batch/length/concurrency Not Disclosed/default，§4最高>90%不能叫安全。2+1+2=5标准且必要风险反侧完成，root待核；仅报告旧完备问题评价遗漏的premise审查，不提供诊疗建议或医学应用recipe。

## [Holistic Trajectory Calibration](https://arxiv.org/html/2601.15778v1)

当前必要源核：root已实际定点通过采用范围/隔离边界；非全篇证明、代码或复现。

v1 §§2/3.1–3.2/A2.2/A2.6/A4：48logprob cross-step/stability/position/structure features→监督logistic，不用finaltoken或globalmean替代过程。500例以内、GAIA165、GPQA448，八任务，smolagents/CodeAct、GPT4.1/4o及开源models，Gemini2.5Pro final-label与human90–95%agreement，不是真值无误。5foldstratified/seed42，α15grid按平均fold ECE/BS/AUROC选，nestedholdout未明确；HLE ECE.031/BS.09只作者局部，不能证明随意domain校准。MMLU→MATH/HLE迁移退化是关键反侧，outputstructure也影响transfer；full48 vs组合有补充信号，但logistic权重不授causalreason/faithful诊断。理论信息更多仅在nestedfeature/Bayesoptimal假设下，48压缩特征不自动满足，不采用理论strictdominance或onlineguarantee。hardware/precision/LLMbatch/长度/concurrency/SLO Not Disclosed，<1ms只classifier非生成成本。3+2+2=7深入窄命题完成，root待核；Books比finalconfidence与执行过程归因边界。

## [Steering Neural Metrics](https://arxiv.org/html/2601.15809v1)

当前必要源核：root已实际定点通过采用范围/隔离边界；非全篇证明、代码或复现。

v1 §§3/4.2/5/限制：500FLORESparallelpairs学layer vector/map、冻Llama3.1-8B/Bloom7B/Aya8/32B或COMET pooledembedding。八language摘要human1–5annotators，源test400、1/3故意破坏，评价coherence/completeness Pearson不是correctness；oracle按同test挑各language bestρ/σ，无dev，不能称可部署普遍提升。LlamaSpanish .15→.20只是oracle相关，nearzero baseline的>100%相对增益不单报。尤其正ρtowardEnglish平均害、负ρawayEnglish常益，French亦可能改善，不授Englishpivot因果保证/semanticpreservation。hardware/precision/batch/length/concurrency/SLO Not Disclosed。2+1+2=5标准完成，root待核；仅报告冻结judge内部representation干预的局部潜力与选择偏差反侧。

## [Iterative Amortized HVAE](https://arxiv.org/html/2601.15894v1)

当前必要源核：root已实际定点通过采用范围/隔离边界；非全篇证明、代码或复现。

v1 §§2/3.1/Table1/§4：线性FFT可分reconstruction将decoder gradient局限到频带子集，amortized初始化后局部refine是新增结构替代；只有linearlydecomposablesignals，不直接推广所有diffusion。CIFAR10 L30同weights，2080Ti/Keras3.10/TF2.19/XLA、λ.001β1：hybrid25 MSE17.86/.156s vsamortized18.27/.051s，是质量增加成本而非总35x；35x是deep-model iterative不同architecture局部计时。多seed/CI/precision/batch/concurrency Not Disclosed；MRI只作为secondcomplexsignal不采用clinical性能。Eq7/Algo1的+logN与minusgradient不支持文字NLL/MAP：L0μ0σ1时z→(1+λ)z；root实际确认，只隔离MAP/回manifold子命题，implemented sign未核，不私修公式，实验不被当证明该推导。2+1+2=5标准并对争议加深完成；仅报告linearsplit局部经验，root实验待核。

## [Decoupled Decision Transformer](https://arxiv.org/html/2601.15953v1)

当前必要源核：root已实际定点通过采用范围/隔离边界；非全篇证明、代码或复现。

v1 §§4/5/6/7.2：RTG历史差分是pastreward，冗余需reward不另提供belief信息且windowhistory是充分统计量；finitecontext/一般部分观测不由其“standardPOMDP”一句保证。新选择是2k observation/action tokens代替3k，并把currentRTG单独adaLN注入finalhidden；training每step仍有RTG条件标签，不是完全删除reward。d3rlpy同GPT/4seeds×100rolloutsD4RL，RTG-mask blockedDT只是小增益、不如DDT，Hoppermedium68.3→99.4局部；2048三法.93无差显示边界，二层adaLN也可回退。§7.2自承隐藏oraclegoal/observablehistory外reward及表征学习时pastreturn可能有益，不能授任意Transformer删conditioningtoken。hardware/precision/batch/lr/totaltrainbudget/walltime Not Disclosed，3k→2k是结构计算估算非生产speedup。2+1+2=5标准完成，root待核；仅报告conditionalinformation与attentiontokenallocation替代，不采用普遍RTG冗余证明。

## [Scaling RAE](https://arxiv.org/html/2601.16208v1)

当前必要源核：root已实际定点通过采用范围/隔离边界；非全篇证明、代码或复现。

v1 §3.1–3.3/Appendix训练配置：SigLIP2So400M、Qwen2.5-1.5B、256 visual tokens、224分辨率、linear FM/50Euler；base noise shift沿有效维度，不计新理论。受控without/with shift GenEval23.6→49.6、DPG54.8→76.8。新增反侧是+0.28B宽head在0.5B DiT增11.2GenEval，>=2.4B收益饱和；τ=.2 decoder noiseaug15k前有效，120k后近无益。不能由scale关联断言width为唯一原因，head也增加参数，未多seed/CI；TPUv5p128/v6e64、globalbs2048、AdamW两optimizer，encoder/LLM固定但骨干scale改变，不授所有RAE无需head/augmentation。3+1+3=7，深入拟采用负面边界完成，root待核；Books比较只看低容量补丁与扩大后noise schedule职责，不为新recipe造gap。

## [Distracting Token Pruning](https://arxiv.org/html/2601.16065v1)

当前必要源核：root已实际定点通过采用范围/隔离边界；非全篇证明、代码或复现。

v1 §3/§4.1/§4.3–4.4/AppA.2：frozenSpatialVLA3B/Nora3B/UniVLA9B；prompt→visual relevance构important region、action→visual attention对外域过阈值剪枝；UniVLA因causal顺序改cosine而非相同attention语义。每checkpoint单组层/topk/τ/Gaussian跨任务固定。SIMPLER Spatial29.2→37.5/Uni68.7→74.0，random_all/random_unimportant/noGaussian有反侧；单3090用于Spatial/Nora，UniA100，未端到端latency/precision/多seedCI，不当低成本部署证明。MannWhitney p<.001只是按episode成败分组关联，不证明一般视觉attention致败；α最优/entropy推断不采用，不展开无关证明。2+2+3=7深入必要核心完成，root待核；Books只比较冻结模型对任务无关视觉输入干扰的条件。

## [Affective gate_proj](https://arxiv.org/html/2601.15906v1)

当前必要源核：root已实际定点通过采用范围/隔离边界；非全篇证明、代码或复现。

v1 §4.2/§5.1–5.2/Table1–2/§8：module-wise参数幅度不作为因果结论；frozen base逐模块继承、固定训练budget独立adapt得到gate_proj局部优势，adding down/全attention反而下降。AffectGPT Qwen1.5/7/14/32B等观察，非情感GSM8K更新更多up_proj是对照。摘要destructive necessity未见独立清零/匹配伤害实验细节，故不采用necessary/所有情感编码都在gate；训练hardware/precision/batch/lr/seed/CI Not Disclosed，不把96.6%性能/24.5%参数比当walltime。benchmark仍有限、只finetuning不涉及pretraining形成。2+1+2=5标准完成；仅报告模块局部可迁移性和negative interaction，不授安全/普遍情感理论，root待核。

## [Cosmos Policy](https://arxiv.org/html/2601.16163v1)

当前必要源核：root已实际定点通过采用范围/隔离边界；非全篇证明、代码或复现。

v1 §4.1–4.3/§5.3/§6/AppA4.2：CosmosPredict2-2B WanVAE video latent直接插normalized/duplicatedproprio/action/value，无新codec；conditional masks分policy/world/value，value标签实为MonteCarlo returns，“state”是camera/proprio observation近似、只s及s'无history/多时刻预测。648policyrollouts修world/value（505已有+143新增），两难ALOHA任务best8、每branch3future×5value；8H100共4.9s/chunk，+12.5平均taskcompletion局部结果不是任意robot或dynamic环境保证。直接5denoise policy单H100 .61s/chunk，10步.95、1步.16不混为plannerlatency；fullfinetune64H100/40ksteps/globalbs1920 LIBERO。无aux/scratch同steps消融只1.5/3.9point差，fromscratch真实抖动可能损robot停止进一步测验。3+2+2=7，深入必要机制/失败/成本完成，root待核；Books比video prior→action/state/value joint carrier，不授真值、全可观测MDP或实时安全。

## [RAGCrawler](https://arxiv.org/html/2601.15678v1)

当前必要源核：root已实际定点通过采用范围/隔离边界；非全篇证明、代码或复现。

v1 §§V/VI/讨论/IX-C：新增是累积已泄露回答的全局KG→normalized新entity/relation收益+topological deficit→TopKsoftmax anchor，非每轮stateless抽取；真实CMG不可观测，heuristic不继承adaptive-submodularity近似保证。四随机1000doc受害subset，BGE/GTE、Llama3.1-8B/CommandR7B/Phi4/GPT4omini；sameDoubao或Qwenattacker，1000query上限、k10。coverage只non-refusal，semanticfidelity是encodercos非逐字重建/真实信息全恢复。k5约28%→k20>60%，queryrewrite下NFC73.8→85.4，故单query看似benign/rewrite不能保全局累积预算；这不是所有生产RAG失守结论。无KG消融仅文字职责分析而非完整定量模块因果，0.33–0.53美元漏hosting/victimservice/全pipelinecost，不授零成本；provenance defense建议未实际验证。3+2+2=7安全受影响内容深入完成，root待核；Books比较累计泄露状态与单次权限/guardrail分责。

## [Medical Confidence Gradient](https://arxiv.org/html/2601.15645v1)

当前必要源核：root已实际定点通过采用范围/隔离边界；非全篇证明、代码或复现。

v1 §3.1–3.3/§4.1–4.4/限制：完整信息static ranking不能外推证据累积，窄2+1+2=5准入。DDXPlus由GPT4.1转dialogs、MediTOD按turn贡献过滤、MedQA删MCQoptions，>10turn/sentence筛171/231/181例；1%(单条)/20/40/60/80/100%同病例生成，信息次序/随机sampling配平未披露。Llama3.1/GPT4.1 size/precision/hardware/temperature/seed未足披露，27方法用六量级accuracy/confidencePearson/Spearman与correct-vs-wrong AUROC/AUPRC，不是概率calibration。Entropy同LlamaMedQA相关.905/AUROC.766但DDXPlus.14/.501；这同时改变数据、tokenization和format，不单因少信息。CoTCE MediTOD Spearman.086说明verbalized也非普适。原normative充分信息/真实诊疗多解判断、MedConf RAG配方、agent主动澄清可靠性不采用。标准必要窄核心完成，root待核，仅报告有限评价协议反侧。

## [Dualformer](https://arxiv.org/html/2601.15669v1)

当前必要源核：root已实际定点通过采用范围/隔离边界；非全篇证明、代码或复现。

v1 §3.1–3.2/§4.1–4.2及supplement850–853：depth-specific frequency bands读取QKV，再pad/IFFT重建输入后仍做vanilla Attention；这是QKV前置filtering的Alternative Branch，不是替换attention kernel或新发现lowpass理论。层间high→low与α<1/N时uniformpartition防频谱空洞是具体组件选择。8长时序数据，lookback96、horizons96/192/336/720，三次运行（不补造seed），HFS不同band消融；不授language causal attention/全模型highfreq保证。harmonic lowerbound仅连续series分解period L=mτ且λ>4，不用于Transformer全局频谱。Traffic/Electricity batch32、其他256，lr.0001/Adam/cosine、three-epoch early-stopping而非总三epochs，NVIDIAA10040GB；单配置不外推generic hardware效率。2+1+2=5，必要标准核心与root重新核窄准入/源通过；仅报告depthband QKV前置filtering，不为同名算法缺位强造Books差额。

## [CoFi-Agent](https://arxiv.org/html/2601.15676v1)

当前必要源核：root已实际定点通过采用范围/隔离边界；非全篇证明、代码或复现。

v1 §3.2–3.6/§4.1–4.6/§5.4：cloud prompt gate读所有initial summaries，约62%只是tool escalation，不能称其余请求无cloud。Qwen2-Audio-7B FP16、Whisper-small共单RTX6000 24GB warm模拟edge gateway；GPT4o temperature0，MMAR1000、batch1，RTT p50 15/p95 45ms。同always-on ASR 51.7%/11.058s，adaptive53.6%/9.617s；局部average end-to-end含tool/network/cloud，非手机功耗或尾SLO。easy-case ASR噪声只有限定性诊断，gate的hedging误升级/自信幻觉漏升级没有校准保证；>1min短event被heuristic ROI跳过、低SNR ASR错和外部知识问题反侧保留。raw audio不上传不等于隐私认证，transcript仍可能敏感。model input/output长度、cloud硬件/precision/concurrency/SLO Not Disclosed。2+2+2=6，必要标准核心已读，root待有限核；仅报告配置内总成本/质量反侧，不把local-first成熟流程本身计新贡献。

## [UniPic 3.0](https://arxiv.org/html/2601.15664v1)

当前必要源核：root已实际定点通过采用范围/隔离边界；非全篇证明、代码或复现。

v1 §4.2–4.3/§5.1–5.3必要核心：Qwen-Image/Qwen2.5VL/VAE/MMDiT latent concat与shape metadata继承既有设计，不计novel sequence贡献；拟窄增量是保留FM线性schedule直接推导CM目标，避免TrigFlow时间/输入输出重参数化引入额外梯度项，finite difference ε=.005，再DMD reverse-KL fake-score LoRA近似。338k composition+381k edit，full-param80k steps/globalbs64/lr1e−4，CM10k bs256/lr1e−6，DMD10k bs64、teacher CFG6。200作者HOI MultiCom-Bench split100 2–3ref/100 4–6ref；QwenImage2509在更多ref退化，数据、架构和training预算共同改变，没有loss/schedule直接ablation或multiseed。12.5x是100→8采样步比，不是同质量端到端walltime，蒸馏仅qualitative图，不授无损。hardware/precision/inference batch/concurrency/latency/lengthSLO Not Disclosed。拟2+1+2=5，必要核心已读但最终贡献准入待root定点核，不把未证schedulevariance归因升为保证；若许可则仅报告探索性有限替代设计。

## [Memorization Dynamics in Knowledge Distillation for Language Models](https://arxiv.org/pdf/2601.15394v1)

当前必要源核：root已实际定点通过采用范围/隔离边界；非全篇证明、代码或复现。

精确PDFv1页头Jan23；HTML日期宏与后续网页显示不用于混版。§2/§3/§6：主设置Pythia-12B teacher→1.4B student，同架构CE baseline，FineWeb July2025 1M个256-token样本；KL温度2，lr5e−5，cosine；teacher3epochs，student/baseline4epochs，比较同分布validation perplexity。Discoverable memorization是50-token前缀后50-token贪心完全一致，不是任意membership inference或隐私定义。主表student .07% vs baseline .17%，PPL17.31 vs17.69；teacher-specific是teacher与student共同抽出的样本再排除baseline，18/1955=.9%，不等于所有teacher信息没有迁移。三seed/data-order联合的baseline排除法仍受测量定义影响。§6hard/soft对照揭示teacher-difficult部分更易迁移，不以整体低memorization声称teacher-specific风险消失；T上升降低此抽取而与某些MIA趋势不同。2+2+3=7，深入完成；root实际核PDF必要段通过。Books普通待办：只比较teacher-specific迁移与抽取定义，不能写蒸馏普遍隐私保证。

## [Martingale Foresight Sampling](https://arxiv.org/html/2601.15482v1)

当前必要源核：root已实际定点通过采用范围/隔离边界；非全篇证明、代码或复现。

v1 §4.1–4.3/§5.1–5.5/Table3/§7/AppendixA：rollout估计条件期望，伪码score=F_t−F_(t−1)；候选相对最佳deficit阈值mean+λσ，earlystop ε1e−6。Doob分解及bounded submartingale convergence不保证有限MC估计校准、confidence=correctness或正确解永不剪掉。Table3固定beam8、λ.8，以score组件替换得ReClor64→65.2/MATH37.2→38.2，估计FLOPs下降1.47/1.48；两RTX3090、vLLM.9.1、PT2.7、temp.7，主搜索rollout8。6nP FLOPs估算不是端到端wall time；precision、batch、concurrency、输入输出长度、SLO均Not Disclosed，六结构化任务不足以外推长输出。2+1+2=5，因理论正确性主张冲突深入受影响内容而非降分规避。窄search-score/停止tradeoff通过root；仅报告，不把经验估计授为正确性保证。

## [MARS](https://arxiv.org/html/2601.15498v1)

当前必要源核：root已实际定点通过采用范围/隔离边界；非全篇证明、代码或复现。

v1 §3.3–3.4/§4/算法/Table2：θ=.9时低margin允许draft runner-up；ratio实为第二logit/第一logit，不是概率比，亦不对加性logit平移不变。作者明确lossy；不能宣称目标分布无损或通用校准稳健。H10080GB，≤32B单卡、较大8卡，对应EAGLE3 draft，K7/topk10/temp1，无额外draft-pruning。主表Llama3.3-70B平均4.76x是相对AR，EAGLE3为4.40x；HumanEval用pass@4、GSM8K用final EM。Table2 Qwen3-32B的K6/9/12/15与温度.2～1有真实accuracy回退与不单调，质量恢复98.1～100%不等于无损。precision、batch、concurrency、长度、SLO Not Disclosed；代价包含draft和target验证，未授生产throughput。3+2+2=7，深入完成，root核算法/配置/表通过；Books普通待办只比较近似接受的质量预算与exact验证边界。

## [Parallelism and Generation Order in Masked Diffusion Language Models](https://arxiv.org/html/2601.15593v1)

当前必要源核：root已实际定点通过采用范围/隔离边界；非全篇证明、代码或复现。

v1 §4/§5/A6/A7：8 MDLM、58bench的generation-order研究；AFP=n/存在finalization的步数，忽略没有finalization的步数，故不是wall time。τ与表面顺序比较、并行ties仍影响它，不声称指标完全解耦。LLaDA2-Flash100B math/code高τ>.8而重复题AFP5～7x、τ近0；不同checkpoint/pretraining和模型默认optimal配置未控制，不能单独归因AR/MDLM架构。CTC对一次conditional-product投影的KL恒等可采用，但不是最终iterative quality保证。A7 A.2/A.3及no-slowdown隔离：影响系数仅j≠i，frozen位置自依赖被忽略；L=1无更新时α0却identity kernel，多吸收态，不收缩。state-dependent selection不由block-conditional独立保证P*不变。root实际核并确认此反例，无需遍历其他proof。3+2+3=8，窄经验/局部CTC深入完成，隔离子命题不作为证据或Books。Books普通待办：只比较factorization、并行和commit顺序的压力。

## [When Sharpening Becomes Collapse](https://arxiv.org/html/2601.15609v1)

当前必要源核：root已实际定点通过采用范围/隔离边界；非全篇证明、代码或复现。

v1 Eq3/Th2.2/AppB427–448：作者定义finite batch Jhat=Σc_i logπ_i−βKL(π||ref)，却推出ref exp(c_i/β)。实际奖励导数c_i/π_i，对w=logπ的KL导数还含π因子与归一化依赖；负c_i可令目标无界。root定点独立数学复核确认。Th2.2、GD几何和依赖它的semantic-coupling因果保证均不采用；不是降分或贡献排除，不要求全篇证明复核。原3+2+3=8中心增量仍是sampling/coupling理论边界，保留中心争议；实验普通待办，只有独立实验证据可收窄经验结论。Books暂缓该争议命题，恢复条件为与真实训练目标一致的推导/勘误及对所需假设的证据。

现已实际读§2.4/§3/§4核心：固定Cat/Persian/Siamese四维embedding softmax SGD、只Persian500steps，varygroup与embeddingoverlap的held-out退化是人工控制例，不证明LLM实训普遍collapse机制。IAC只对positive乘(G−|S+|)^α（α1）；DLC用CE训练memory network再从policy logits减μmemory logits。32H200、DeepScaleR40.3k、Qwen3-4/8/14B、globalbatch64、G8、AdamW lr1e−6、2000steps，每50step择peak。baseline相同reward/samplingbudget，不等于DLC相同compute；作者明确memory同步采样无kernel支持时5x rollout overhead。六mathbenchmark PASS@8/AVG@8，14Bpeak PASS均值77.03→78.81，未给此比较seed CI，checkpoint选峰引入选择偏差；precision、序列长度、concurrency、SLO Not Disclosed。可仅报告positive reweighting与decoupled sampler的局部quality/cost结果；推导争议仍独立终态隔离，待root实验有限复核。

## [Beyond Fixed Psychological Personas](https://arxiv.org/html/2601.15395v1)

当前必要源核：root已实际定点通过采用范围/隔离边界；非全篇证明、代码或复现。

v1 §3–5/限制（core lines330–418）：127问题=77GlobalOpinionQA+50dilemma，六archetype+baseline七条件；GPT4o/Llama3.1-8B/Qwen2.5-14B共2667回答。all-mpnet-basev2语义相似度的archetype区别F2.18、p.054，不授“所有模型天生无state”。同GPT4o baseline答案，在七framing下三个RM（DeBERTa/Skywork8B/ArmoRM8B）评分出现方向翻转，distress ArmoRM d+.76而Skywork−1.12，framing可解释7～30%variance。state-invariance是作者规范性前提，不证明真实用户偏好必须相同；心理状态来自文字表达，subreddit/受众/年代/三posts门槛混杂。不得把评分变化外推实际RLHF训练失效或人的普遍状态比例。2+2+2=6，标准必要证据已读；仅报告局部model/RM条件，尚待root证据复核。

## [Not Your Typical Sycophant](https://arxiv.org/html/2601.15436v1)

当前必要源核：root已实际定点通过采用范围/隔离边界；非全篇证明、代码或复现。

v1 §4–6/Table4：100 TruthfulQA二元互斥候选、用户/朋友身份及前后位置排列、每prompt50重复temp0。§4.2写Gemini2.5Flash，摘要/结论称Pro，保留配置身份冲突，不以最新11模型扩大本窗证据；其余4o/Sonnet3.7/MistralLarge2411。two-friends control有Gemini/Mistral recency6.95/3.11%，4o/Claude不显著；zero-sum用户stake条件Claude/Mistral anti-sycophancy，换成非zero-sum又变化。说明评价符号受stake与位置影响，不证明RLHF导致moral remorse（作者明确猜测原因待验证）。temp0重复不保证独立，binomial显著性只在其假设下成立；部分gold答案本身有语义歧义。2+1+2=5，标准完成；仅报告配置内评估混杂而非普遍模型排序，root待复核。

## [Tracking the Limits of Knowledge Propagation](https://arxiv.org/html/2601.15495v1)

当前必要源核：root已实际定点通过采用范围/隔离边界；非全篇证明、代码或复现。

v1 §3/§5/§6/Table3–4/限制：1500样本WIKI/CODE/MATH各500，10次atomic probing，以GPT5mini判correct modal response为known；Append/Append-T/FT-CK/MeLLo，KAS1/10/100/500。AP答案、FKE所有atomic facts entailment、HP两者交集区分“用了事实”与“推理正确”。§6.3明确FKE与HP分离，不能由faithful API usage推出function correctness；Qwen3-1.7B WIKI Append KAS1 HP83.6→KAS50022.2，更多facts非总有益。token/计算预算未全同，不能据此宣称longthinking普遍有害；KAS也改变distractor/contextlength，attention失效只是作者解释。GPT5mini辅助生成与判分有judge循环，quality check平均94.3% factual/88% necessary并非完美，作者称“guarantee”不采用。英文静态snapshot，未验证agent/multimodal/temporal更新；o4mini与4.1mini共享知识/架构仅假说。3+2+3=8深入必要证据已读，root待复核，Books待比Ch66/Ch76具体已有论点。

## [ViT Registers and Fractal ViT](https://arxiv.org/html/2601.15506v1)

当前必要源核：root已实际定点通过采用范围/隔离边界；非全篇证明、代码或复现。

v1 §3/§4/Table1–2：保留regular-token全attention，新增4-summary与CLS，summary局部双向连到所辖patch、summary相互可见；17新增tokens固定，ViT-S/16 ImageNet1k、256分辨率、90epochs。sincos2d register77.68、summary77.61、fractal mask77.57；NoPE72.93→73.09仍低。回224、4～59新增token收益仅baseline76.92±.13的一两SD；新增token位置编码和fractal结构本地不显著。不能由语言causal mask NoPE直接推出视觉summary-mask可替代位置编码，也不证明所有register无效。模型scale、输入mask施加位置、预训练目标/图像对称性同时不同，原因只是假说，非因果定位。2+1+3=6，标准完成；局部负面结果而非只报告SOTA，root待复核，仅报告适用边界。

## [PRISM](https://arxiv.org/html/2601.15540v1)

当前必要源核：root已实际定点通过采用范围/隔离边界；非全篇证明、代码或复现。

v1 §2/§3/§4，不混入后来OpenWebText/MCR2重写。差分signal−λnoise attention、Q=K=V dictionary、overcompleteR2、两组RoPE base31415/3183；π比例仅作者明确Conjecture，finite-head softmax到coding-rate梯度是近似，严谨mean-field与non-resonance界仍列future work。TinyStories8层50M、RTX4090、20ksteps、batch32、context512、AdamW lr6e−4、warmup1k、cosineλ.01→.1；validation≈1.55对外部GPT2 22M和Gemma曲线，parameter/budget并不配平，无单组件ablation/多seed不确定性，图attention不能证明head的causal semantics。不得称同预算优于GPT2、已证明π消除noise或100B稳定性。2+1+2=5，标准必要核心完成，仅报告探索性替代设计和边界；无已证长期理论缺口，root待复核。

## [VIOLA](https://arxiv.org/html/2601.15549v1)

当前必要源核：root已实际定点通过采用范围/隔离边界；非全篇证明、代码或复现。

v1 §3/§4.1–4.4/Table2–3/限制：annotation20～100，Qwen2VL7B/VideoLLaMA3-7B/Qwen3VL8B/LLaVA-Video7B，InternVideo2 embeddings；1fps最多32帧，8demonstrations各16帧。density/uncertainty平衡选择，expert ICL生成pseudo-label，token-confidence最高5%入pool，retrieval score similarity^(1−τ) confidence^τ，prompt显式区分GT/pseudo provenance并将近邻GT放最后。Table3相同池/预算：DriveAct16.1→retrieval17.6→prompt24.3→both26.4，Xsports单retrieval16.5→15.0反侧；不是置信度filter总有益。Table2 uncertainty-only EgoSurgery30.7，balanced51.9；其他generic视频数据也有效，不采用诊疗结论。95percentile不是calibratedaccuracy，encoder shift可能破坏density/retrieval；VideoICL baseline被改成20label池因此结论限lowbudget协议。2+2+2=6，标准完成，root待复核；仅报告局部数据选择/provenance实验，不把成熟组件组合本身授普遍新机制。

## [DFSU](https://arxiv.org/html/2601.15595v1)

当前必要源核：root已实际定点通过采用范围/隔离边界；非全篇证明、代码或复现。

v1 §3–5/Table3/§7：FlanT5Large inverter从target末位置log-probs重建文本；entity-swap surrogate、few-shot privacy mask，freeze base只LoRA，J=utility CE−privacy CE。data-free仅指不使用被注入的具体PII样本，仍重用PII syntactic templates，且inverter训练需要文本/logit pairs；不称无任何训练数据。Pythia160/410M/1.4B，500合成PII各10～100重复，WikiText/MNLI注入6epochs、bf16；inverter410M上30epochs bs256复用于家族；LoRA MLP rank4 α32，10epochs effectivebs16。oracle为同PSCU用真实PII而非所有unlearning SOTA。Table3模块变体EHit<1.6%；β5高遗忘但PPL爆炸、高rank有collapse，100surrogate privacy趋饱和而MNLIutility仍下降。白盒logits前提；有限synthetic exposure与extraction测量不构成formal privacy/DP/retraining equivalence，也不以MNLI叫reasoning能力完整保留。2+2+2=6，安全/隐私采用边界深入完成受影响内容；仅报告实验可行性，不授“strong privacy guarantee”。root待复核。

## [YuFeng-XGuard](https://arxiv.org/html/2601.15588v1)

当前必要源核：root已实际定点通过采用范围/隔离边界；非全篇证明、代码或复现。

v1 §3.1.2/§3.2–3.4/§4.1/§4.3/§4.4/§6.2：synthetic add/expand/narrow policy反事实→fresh teacher response→独立verifier过滤，classify-then-explain SFT。reserved vocabulary first-token risklabel/probabilities，category thresholds后可以停止或继续解释；risk detection与product policy不同，解释只条件于已选label，非faithful causal reason保证。Qwen3-8B可DP；0.6B distillation未经历DP/RL，不外推相同policyflexibility。prompt/response thresholds.5/.8，custom ecommerce F1.91、scopeadapt.75；不是普遍safety保证，policy清晰且consistent为前提。2M同子集SFT/GRPO对照：explain-first multilingual74.19→79.34但classify-first提升不一致，最终部署选择SFT-only。不能由需后置解释推出其改善前置判别、亦没有实测latency/SLO；hardware/precision/batch/concurrency/length Not Disclosed，smallmodel低延迟只设计动机。3+2+2=7深入完成，root待核，Books仅比较分层输出与判别/解释/策略契约。

## [DeepASMR](https://arxiv.org/html/2601.15596v1)

当前必要源核：root已实际定点通过采用范围/隔离边界；非全篇证明、代码或复现。

v1 §III-B/C、§V、§VI-C：Qwen2.5-.5B→ASR/FSQ S3 discrete语义style tokens，24layer/16head/1024 flowdecoder吃target speaker mel；token soft factorization不等于严格style/timbre独立，七pairedspeaker tSNE仅诊断。200kh internal250ksteps→Emilia+ASMR1000h finetune，8A100动态23000frames、accum2；WER Whisper、WavLM similarity、Gemini2.5Pro style、12听众MOS不同协议不能直接合并。crossstyle arbitrarysinglefemale prompt会identitybleed：N2A WER12.27/SIM.27；virtual50 neighborpool WER6.53/SIM.41，real50为11.19/.42。混normal数据N2A WER15.20→6.53，counter显示style-only忘normal能力；预算/seed CI未齐，不将visualization授causaldisentanglement或syntheticpool授formalprivacy。2+2+2=6标准完成，root待核，仅报告ASR-codec/跨style局部条件。

## [Fission-GRPO](https://arxiv.org/html/2601.15625v1)

当前必要源核：root已实际定点通过采用范围/隔离边界；非全篇证明、代码或复现。

v1 §3.3/§4.1/§4.4–4.6/限制，仅BFCLv4不导入v2 TAU等。失败trajectory+诊断feedback作为correctivecontext，LIFO新错误buffer→G'重采样GRPO；错误simulator Qwen3-32B从2k teacher标注训练，**输入含groundtruth toolcall**，仅训练模拟监督，不能称真实环境runtime总有oracle。630traininginstances、8H80080GB、Verl lr1e−6/bs8/G8/temp.95/topk50，prompt12800/response4096。BFCLmulti-turn允许20retry；staticfeedback8B+1.25pp、dynamic4B再+3.62pp及234globalsteps固定trigger频率反侧，可采用对“只有scalarpenalty足够”的局部修正。额外rollout/32Bsimulator成本未等walltime，总steps同非总compute同；LIFO是更接近on-policy而非严格无偏，singlebenchmark不授所有tool权限/错误安全。3+2+2=7深入必要核心完成，root待核，Books只比训练中error-branch监督，不把GTsimulator包装部署能力。

## [Predictive Coding and Information Bottleneck for Hallucination Detection](https://arxiv.org/html/2601.15652v1)

当前必要源核：root已实际定点通过采用范围/隔离边界；非全篇证明、代码或复现。

v1 §4/§5/§6/§7.1：uptake loglikelihood差近似，不是完整distribution KL；NLI/paraphrase stress/conflict与claim-conditioned多reason traces Jaccard rationalization；监督RF featurestack。HaluBench200、50/50balance，unsupervisedAUROC.8017、IMPROVED RF.8669；不得直接与Lynx/LLMjudge不同数据/accuracy指标相比。作者R信号“无效”的解释是falseclaim-conditioned rationale仍一致，但未展示单独R剔除定量ablation、随机seed/明确train-test切分或LLM/NLI提取全成本，故仅保留该风险假说及有限探测性能。5ms/1000x/#75data只计轻分类器对外部数字，不能授production端到端saving；高uptake只说明用了context、不证明context真。2+1+2=5标准完成，root待核，仅报告：rationale一致性不授真值，普遍因果/效率结论未证。

## [Event-VStream](https://arxiv.org/html/2601.15655v1)

当前必要源核：root已实际定点通过采用范围/隔离边界；非全篇证明、代码或复现。

v1 §4/§5/§6：frame encoder连续监测semantic drift、motion与f_(t−1)→f_t预测残差，阈值触发event memory/decoder；MLP predictor训练后freeze，因此“withoutretraining”指不用重训VideoLLM而非无任何训练。同VideoLLM-Online encoder、LLaMA3-8B、2fps，RTX6000Ada约17fps处理；OVO平均17.73→28.15是该受控配置。Ego4D只选四段102～120min、GPT5双向A/B没有人类结果，局部0.05～0.08s/token与ablationFull.093s不能外推无限流/尾SLO。eventduration、伪boundary与missedevent、模型precision/batch/concurrency/input-outputlength Not Disclosed；full三cue在customGPT5winrate68.1优于去cue，cache/decoder/inference改动共同作用，不单因“真实event”。3+2+2=7深入必要核心完成，root待核，Books只比较event-admission/sampling/cache与decoding职责，不以小样本授unbounded稳定。
