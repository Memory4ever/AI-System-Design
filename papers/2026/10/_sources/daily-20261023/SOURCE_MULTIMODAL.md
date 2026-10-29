# Oct23 Daily — multimodal necessary Source slice

只处理 root 指派的八个已完整题摘/准入独核 exact-v1：2610.28801、28827、28858、28954、29229、29232、29380、29408。公开日沿用本日 ARXIV.md 官方 Oct22 BJT cs.CV list mapping [3]/[6]/[11]/[15]/[43]/[45]/[59]/[63]，cross-list 不增家族；提交 Oct20/21 不是公开日。恢复重读 AGENTS、当前研究/Report 合同、Daily 来源入口、Prompt、ROADMAP 与本日路由，不恢复其他日。root 唯一 Report/State/Books writer；本文件只交必要 Source、实际 owner 比较与逐字 PRE，不预授 POST 或日级完成。

八份官方 exact-v1 HTML 已取得，正文提取存同目录 `multimodal-source-2610.<id>-v1.txt`。保存原件不等全部内容已审；下文逐项给实际已读必要域，HTML 数学/表格为文本提取，未运行代码、复现或确认生产能力。评分沿正式准入命题逐项校准，不借成熟原则、Books 决定或工作量加减分。

## V1 — JUICE 2610.28801v1（2+2+2=6；标准必要完成，拟 Ch24 gap）

[官方 exact-v1](https://arxiv.org/html/2610.28801v1) §3–4、§5.1/5.3/5.4、Conclusion/limits，另 A.5/D.2 必要预算反侧。图/文各自在冻结 encoder 的连续空间中，以各自 noise level 和 schedule 表示 clean condition 或生成目标；同一 MM-RiT 的双向 joint attention 每次读取两份当前状态，再同时更新，两流不先后锁死。Joint+两方向 conditional 混训覆盖时钟方形内部和边界；joint-only 不见 clean boundary，conditional-only 不见共同 noisy partner。匹配 target 数、blocked exchange 与单 target joint 等对照支持 noisy partner/exchange 的局部作用，不单由双份监督解释，但每个 pretrain config 仅一 run、框架/表示比较连 decoder/normalization/noise 完整 pipeline 一起变，非完全隔离单组件因果。

668M trunk、50k updates、batch4096、38M image-caption 加 Cambrian-7M；最终 2.12B trunk 为60k+15k SFT/batch1024、224²，双向全部模块 SigLIP2 约3.03B、DINO约2.91B，不是整个系统只有2.1B或无预训练知识。相同 guidance GE48.41 对 T2I-only47.86，但后者自调 guidance 可51.23；caption CIDEr88.8 对 AR160.52，CLIPScore接近不是逐字保真，长输出有语法/造词错误。只读本文必要机制，不用 headline 排所有模型。

Maze任务各自5k adaptation、500 maps、两 sampling seeds；16 backbone calls coupled93.7% 对 independent54.6%，但 image-first95.2且配对McNemar p=.017 优于 coupled，不能说共同采样普胜串行。一个coupled call推进双流，independent/sequential预算每流分别花；encoder/decoder calls不计，图11给independent32 calls不是表7预算。VSP55.9k训练maps/每level100test，3–6训练尺寸99.8%、未见更大7/8为94/69；重复move文本丢失仍失败，非通用规划保证。编码/解码训练、冻结模块驻留、task adaptation、全部两流调用/解码与独立一致性检查都付费。

actual Ch24:209–217 已有分层 RGBA/形状–位姿共同去噪及 frozen/generated 角色，却没有图文各自时钟、joint/conditional 支持覆盖与多解 marginal mismatch。唯一 MULTIMODAL-GENERATIVE-PARADIGMS，完整“共同去噪也能处理不同类型的输出…”段及 marker 后、完整“已有粗几何也不一定应当直接变成待去噪的起点…”段前，最小 PRE：

> 图文也可在各自冻结 encoder 的连续空间中共同生成：给两流独立 noise level，clean 流作条件、noisy 流作目标，以 joint 与 conditional denoising 覆盖采样实际经过的内部和边界；每步先读取同一份双流状态再共同更新，避免独立 marginals 各选一个正确却不一致的解。[JUICE 的受限对照](https://arxiv.org/html/2610.28801v1)支持这条无固定先后分支，却不证明普胜顺序生成：所测 maze 的 image-first 仍更好，连续文本也付出精确措辞与长输出质量损失。冻结 encoder/decoder 的已有知识、额外模块、任务适配与全部采样/解码都付费，backbone calls 不等完整成本；词句、跨模态一致性或净预算不可靠时，保留离散文本、较可靠模态优先和独立结果验收，不把 joint 正确率或同一 checkpoint 当成通用推理保证。

## V2 — WorldStream 2610.28827v1（2+2+2=6；标准必要完成，拟 Ch25 gap）

[官方 exact-v1](https://arxiv.org/html/2610.28827v1) §2–7 必要核心完整。这是 learned semantic planning + deterministic procedural/compiler 的显式交互世界，不把 learned physics/dynamics 作为已证。Macro 约束区域组织，Micro 读取真实 sampled geography 与 accepted neighbor commitments；typed distribution 的独立argmax可不满足共同硬约束，bounded resolver在声明可行域联合选项后才编译。100同分布样例从37%到100%仅这些已声明约束，不认证真实生态/任意空间可行。

运动/相机方向候选、ETA与有限 planning/compile 预算形成两个 frontiers，compile subset须已有 accepted plan；required neighborhood 优先。保留 world record R=(geography, accepted plan, boundary commitments, explicit object state, edits, revision, compatible generator/assets)，渲染几何 X=Compile(R) 可evict；dense procedural content先存参数/seed，单对象编辑后 promote explicit state。边界两侧读同 authoritative edge、异步工作带 source revision，commit须 current revision和target仍有效，资源准备后原子安装visible+record；不是让 stale结果覆盖新编辑或只存seed即可无条件重建。未来 intent 与当前 edit 区分。

Three.js/WebGL1920×1080、3 persistent compile workers、required3×3。Planning ablation每variant仅一完整run不估model samplingvariance；100route replay同preparation times/worker limits，但backend readiness排除browserinstallation。80 bilingual fixed-world requests76对，非完整edit–evict–revisit实验；仅10noaction/10unavailable不授开放安全。完整优化compilation前后相同objectrecords只支持该local路径，约3.24× denseforest不是端到端世界生成加速；2threads→2process同warmworkload1.99×另有人口。长期record storage和离屏actor simulation未解决，boundedrender/concurrency不等持久总存储恒定。规划/solver、资产与compile、驻留/安装、编辑检查及重访全部付费，硬件未充分披露不补SLO。

actual Ch25:605–684 的 persistent geometry/address 与1544–1566 reason/execute/render 已分状态职责，未覆盖语义/几何两前沿和 shared-edge+revision record 的重编译交接。唯一 MULTIMODAL-WORLD-MODELS，完整“当前证据只有小规模gameplay…简单动力学或已有simulator…”段后、完整“在规则已声明的交互里，还须约束render之后的反馈…”段前，PRE：

> 可执行世界若要边走边扩展，还须分开语义前沿、几何驻留和已接受的世界记录：先沿预测路径准备计划，再在更近范围编译几何；eviction 只释放实现，重访读取保留的计划、对象变更、边界与兼容 generator/asset 版本。[WorldStream 的受限构造](https://arxiv.org/html/2610.28827v1)让邻 tile 共读已接受边界，后台结果在安装时核 source revision 与当前 target，防止旧编译覆盖新编辑；dense 参数化内容被单独编辑后还须提升为显式对象记录。它没有学得未知物理，有限预算也不使累计记录恒定；route readiness 排除浏览器安装，语言测试未证明完整 edit–evict–revisit。规划、校核、资产、编译、存储与重建均付费，版本、边界或修订不合时保留已接受记录、拒绝旧结果并回到较小区域/显式 simulator，不让可重访画面或 backend 就绪替完整交互签字。

## V3 — DualHeads 2610.28858v1（2+1+2=5；标准必要完成，拟 Ch24 gap）

[官方 exact-v1](https://arxiv.org/html/2610.28858v1) §3、§4.1–4.3、Conclusion 与 Appendix A 直接限制已读。Frozen diffusion feature backbone 上reference head区分 reference与online recomputedprediction，reward head学same-prompt组内external scalar advantage的softlabels；generator反传固定heads的weightedlogits，不需externalreward可微，也不需 teacher score。当前fewstep endpoints先no-grad rollout，再renoise/gridtime并作一次可微generatorprediction；该prediction不是原endpoint，heads又在另一独立noiselevel读它。丢两head后推理仍原fewstepgenerator，无新增head但非训练免费。

最优reference head为 noised reference / noised recomputedprediction density ratio；固定reward head时在该 noisy prediction分布可解释为 reverse-KL 正则 learned-logit reward，非真实externalreward或最终endpoint分布精确KL保证。Optimalheads/固定reward 假设在交替训练不成立，rewardhead随currentgenerator重拟，未给convergence或防hacking保证；等价temperature近似仅unclipped接近.5软标签、advantage尺度，不把 λD/λR 直接当通用物理温度。

SD3.5Medium/Z-Image distill初始化、512² LoRA32/alpha64，main K24/ablationK8、4step无CFG，rewardhead1000stepwarmup，reference池含20step base-generated筛选或Pick-a-Pic；生成/筛选reference和全部rollout/externalreward、heads/冻结backbone梯度与训练约20h每run均付费。OCR .92/GenEval .90为各自训练实验，不把多步40–80NFE异法当同训练预算；Z-Image表有对照1024²与DualHeads512²协议差，EMA一run不足广泛稳定。Reference改NanoBanana图像OCR .92不变但GenEval .90→.73、CLIP也退，说明reference承载reward未管的内容，不是无害质量正则。部分reward/quality指标对旧法仍劣，不授全面更优。

actual Ch24:2340–2347 已有在线expert discriminator与TDM-R1 scalar surrogate，但缺“externalreward softhead + reference density-ratio head”两接口在noised recomputedprediction上的有条件正则解释。唯一 MULTIMODAL-GENERATIVE-PARADIGMS，在完整TDM-R1段及marker后、`### Reward 更新需要先定义采样路径上的 Policy`标题前，PRE：

> 外部 reward 不可微时，还可分别训练两份可微读出：reference head 区分参考图与当前重算预测，reward head 学同 prompt 组内反馈，再让少步 generator 反传二者的加权 logits。[DualHeads 的受限构造](https://arxiv.org/html/2610.28858v1)只在最优 reference head、固定 reward head 等条件下，将加噪重算预测的目标解释为对 reference 的 reverse-KL 正则；这不是最终图像与真实 reward 的精确等价或交替训练收敛保证。Reference 池还会改变 reward 没管的风格、构图与任务准确率，两 head 不能防代理漏洞。参考制备、分组 rollout、外部评分、head/backbone 反传与适配均付费；训练后弃 head 只免新增推理读出。代理、reference 支持或独立质量不合时保留原监督生成、固定 guidance 与可信外部验收，不由少步 reward 上升批准全分布保真。

## V4 — Pair-Free C2R / C2R# 2610.28954v1（2+1+2=5；标准必要完成，拟 Ch24 gap）

[官方 exact-v1](https://arxiv.org/html/2610.28954v1) §3–5 全部必要方法/评价/限制及B.6完整预算。Pair-free仅指不需aligned coarse/real video pairs，仍需四modality各14k pairedimages（GPT-Image2编辑/3D重建简化，1280×720）及389854 realvideos。DINO-R2C以共享可训DINOv3L+四head学real→coarse DINOfeatures，frozenRAE decoder给像素/perceptual监督；同camera homography施于imagepair，逐帧应用仍jitter，只作control、realvideo作时间连贯target。直接给predictedfeatures会夹带actualcoarse推理时无的realistic cues，因此先解码coarseRGB再以同frozen DINO重编码给adapter。RGBbottleneck对照仅illustrative、排出quantitative table，不用图例授全部泄漏已消除或因果幅度。

Wan2.2T2V-A14B两time-routedexperts冻结，分别control/fusionadapters共180.54M，仅占计数28.758B之.63%；该计数包含两expert却排externalencoder/VAE和另训DINO-R2C319.92M，不是全链可训参数或成本.63%。DINO-R2C为24B200/20k steps/batch192/记录4h02m58s，派生97.19GPUh；1B200/BF16/720p预处理81frames39.92fps排model load/transfer/video codec/storageIO，不等最终C2R视频生成速度。全部image制备、R2C与adapter训练、on-the-fly预测/解码重编码、最终完整diffusion均付费；推理弃R2C/RAE不免除已付制备。

真实coarse无pairedrealGT，300eval=三类各100、sameprompts，部分baseline重训同pseudo-data。DOVER/VEFX质量较好但原C2R realism75.50仍高于74.17，VACE flow/camera保持、adaptedEdittoDINO保持更好；同pseudo-data对Editto提升而VACE多数指标退，非普适数据收益。Reference-free proxy/VLM非真实physics，2DstylePCA非分布等价。Abruptpose/motion时model可补中间状态或改节奏而失control，pseudo/actualcoarse域差仍可能坏。

actual Ch24:1953–1967已有“先编辑锚点造pairedvideo→制备退出部署”和异主体motion迁移，但没有“paired监督从video降到image、逐帧造control及feature→RGB→feature部署可见性边界”。唯一MULTIMODAL-GENERATIVE-PARADIGMS，在完整“这条路径没有消除完整成本和运动约束…”段后、完整“外观迁移还可以把共享运动条件与目标外观适配分开训练…”段前，PRE：

> 配对要求还可从视频下放到图像：先用 real/coarse 图像对学习 real-to-coarse 映射，再逐帧处理普通真实视频，构造 coarse control 与原真实目标的伪视频对。训练控制若直接消费预测 features，仍可能偷带实际 coarse 输入没有的真实外观信息；[C2R# 的受限分支](https://arxiv.org/html/2610.28954v1)因此先解码成 coarse RGB、再用部署同一 encoder 重编码，而非让中间表示直接过桥。这个 bottleneck 只有定性反侧，不证明泄漏全消；pair-free 也未免除图像配对、预处理与训练费用。逐帧 jitter、伪/真 coarse 域差及突变动作仍可损害对齐，生成质量与控制分别验收；失配时保可靠成对监督、原 coarse 输入和较保守生成，不将更逼真或 teacher 退出部署授为无损运动、物理真值或免费推理。

## V5 — FrameBlend 2610.29229v1（2+2+2=6；标准必要完成，拟 Ch45 gap）

[官方 exact-v1](https://arxiv.org/html/2610.29229v1) §3–5/Conclusion+Limitations必要完整。Idle短window预填KV不能预知query：上下文可能漏必要/写入无关内容；query到达先沿base每层retrieval选S^l，QTS按某token被多少层选中，提出跨层相同P，一次按时间顺序re-prefill P全部层，再只替换原S^l中对应row，不新增整套P到每层、不重算所有history。HERMES无retrieval时另外querysimilarity只选重算目标、原decodecontext不变。CPU保留观察到的visualtokens避免再跑visionencoder，代价是额外host存储；这不是无损fullcontext KV修复，也非querytoken成为每份旧KV的真实因果历史。

LLaVA-OneVision7B/Qwen2.5VL7B、ReKV/LiveVLM/HERMES、0.5fps输入、K7840=40LLaVAframes；window为每framework/benchmark调优，非自动适配。SingleA10080GB效率，RVS-Ego每题独立读此前所有frames，不是连续多query共享SLO。ReKV idle81.1→32ms/frame却TTFT.17→.93s；LiveVLM.04→.84、HERMES.03→1.04，headline总时延14–59%降不等每次问答更快。总费含queryrecompute，但不推CPU总存储、生产并发/尾延迟；analyticalFLOPs不是墙钟。仅7B尺度。

5bench有局部反退：ReKV movie score3.45→3.41、QwenOVObackward45.3→44.3、LiveVLM EgoSchema60.6→60.5；short-only/recompute-only也混合，合用支持该局部重分预算而非任意多重算必好。RVS用GPT3.5turbo0125 judge不为独立人审；CacheBlend对照samewindow/replacement但selectionplan/额外earlylayers不同，只比较targetselection路径。保留视觉tokens、host传输、selection、re-prefill、decode和调window全计费。

actual Ch45:225–227 已有独立chunk拼KV缺crosscontext与selectivecausalrepair，Ch23:1730后也有clipmemory/queryretrieval；均未覆盖流query未知时主动缩短idlewindow、query后跨层一致token重预填的算费—TTFT迁移。唯一INFER-KV-CACHE，在完整“这种方法节省的不是任意Prefill…局部重算结果才可复用”段后、完整“跨模型复用还多一层表示失配…”段前，PRE：

> 持续视频还可把 contextualization 的预算从 idle time 部分移到 query time：先以短窗口写 KV，问题到达后用各层检索的共同 token 候选，一次按时间顺序重预填这些视觉 tokens，只替换原读取集合中的对应 rows。[FrameBlend 的受限对照](https://arxiv.org/html/2610.29229v1)不是恢复完整历史的 exact KV，而是用查询相关重算换较少日常预填；原视觉 tokens 仍保在 CPU，跨层位置与替换身份也须一致。总处理费下降可伴 TTFT 明显增加，部分问答切片反退；存储、传输、选择、重算与窗口调优全计费。新query依赖、质量或响应deadline不合时，扩大原窗口、保留完整重算/读取与独立答案验收，不由少FLOPs或训练免费签发无损与交互SLO。

## V6 — Think-Capture 2610.29232v1（1+2+2=5；标准必要完成，拟已有覆盖 NC）

[官方 exact-v1](https://arxiv.org/html/2610.29232v1) §3–4.10/Conclusion必要完整。第一stage提querytarget，SAM3 masks与Pi3X points/poses在首frameworldframe聚合，符号object/camera关系连原images供第二stage；最多4frames限制dense估计，少target只减少segmentation/聚合/O(m²)relations，不是densegeometry只算所选物体。约100symbolictokens对raw205，丢失小尺度/continuousdetail，approxmetric不是真实尺度。3D对2Dboxes对照同target/masks，支持该表示接口，但不认证全部gain只来自geometry。

Qwen3VL4B冻结vision，10kMindCube base/tool两screening挑3032disagreement（1927base错tool对、1105相反），排同对/同错；这是该模型/固定prompt相对结果，不是真实有用/误导geometry的客观标签。负例可因geometry错误或integration失败，+2/+1为rawaccuracyreward，加format.5后within-groupnormalize，不直接授负类梯度倍增或uniquecausal机制。4A10080GB/38h≈152GPUh、1600steps/G8/batch16/lr5e-7；retainedframes和全部screening、tool、原图/推理/训练付费。

MindCube名义1050题但rare invalid各run排，不能把该数当实际全分母；MMSIpositional/full分开，ViewSpatial迁移。Coordinate.4m与maskdrop30%受控corrupt改善，不补严重遮挡缺失；<1.6%无target时deterministicimages-onlyfallback，不是校准任意不可靠geometry可拒。Table5累计GRPO/tool/template组合非完整因果factorial；主文未报告重训方差不补。AgibotG1仅asynchronousglobalwaypoint/StarVLAhighfrequencycontroller，21.8sA100pipeline=6.8planning+3.1geometry+11.9stage2；directanswer少40%时53.2对54.4退，4090resident21.5GB非实时推理/全机器人安全证据。

具体已有覆盖：actualCh23:1319主动取证段已区分queryproposal、原观察与evidence sufficiency；1346–1382把taskcontribution与sample可靠性/训练标签分开，1860–1878要求估计geometry的观测/标定支持、保原视图/显式工具fallback。该局部tool+symbolic+disagreementGRPO实验为这些义务的新验证，未提供可直接迁用的校准可靠性/持久坐标机制，故保具体训练人口/鲁棒范围和异步反侧于报告，不添同义书段，不据NC降分或排候选。待reader独核实际owner。

## V7 — AdvFidelity 2610.29380v1（2+1+2=5；标准必要完成，拟 Ch24 窄 gap）

[官方 exact-v1](https://arxiv.org/html/2610.29380v1) §3–4.4/Conclusion必要完整。LeapAlign ReFLfewstep路径可微taskreward外加frozenDINOv2CLS+onlineMLP fidelityreward；当前generator从moderatelynoisedreference用1–2steps重建negative，配对BT学reference>reconstruction，wholeimage/randomcrops同CLShead，不是patch-token真值。t∈{.3,.5}只该构造。相似content降低unrelatedpositive/negative风格语义捷径但不精确保内容，也不隔离全部artifact；nonstationaryhead交替更新无全局收敛/防rewardhack证明，兼容GRPO仅提议，实测是LeapAlign。Thresholdcombinedreward margin不是分别每项质量达标。

FLUX1dev从原base启动4/8step无CFG、fullgen和discriminator分别lr1e-4/5e-5、4Dupdates/Gupdate；HPDv250ktrain400test，fidelityreference50k为已HPS对齐LeapAlign的50step生成图，不用其score/trajectory仍使用其已付RL/生成知识，single-stage不等全家族无teacher费。GenEval50ktrain/553test×4generated，reference5k原base50steps；既有realdata亦可作reference。Virtualdressing QwenImageEdit2511 1000webpairs/124test，trainGT同时DINOtasktarget+fidelityref，Gemini3.5Flash三次重判同图的mean±std不是三次训练/生成replicates或人审。已发RTDMD模型跨训练prompt/reward，作者另sameprotocol重训才窄比；不据不同训练总预算/stepNFE签生产加速。

Cumulative ablation frozen/unpaired→online→targetanchor→paired支持该配置逐项条件增量，不是完整factorial唯一因果；换targetanchor还有部分UR退。8stepHPD多数proxy好仍有MixGRPOImageReward更高；HPSv3会给artifact-laden图误导高分，仅reference不当主质量证据。所需gradientdiscount、threshold、crops/全图、reference制备、online重建及多次Dupdate/所有rollout均付费。主文未披露可直接用的硬件/端到端wallcost，不补；noDMD不代表没有已训练参考模型/参考生成费或proxy局限，不把使用reference样本混称直接消费teacher score/trajectory的蒸馏。

actualCh24“Expert图像监督还可以随当前policy样本更新discriminator…”完整段已有在线监督与scalar/ReFL分路，未有same-reference的noise reconstruction负例以降低contentshortcut。唯一MULTIMODAL-GENERATIVE-PARADIGMS，完整Expert段/2602.12155marker后、完整“少步且确定的生成路径还可以把终态反馈移交给可微surrogate…”TDM-R1段前，PRE：

> 在线 fidelity discriminator 的负例还须控制内容捷径：可把同一高质量 reference 加适量噪声，再由当前 generator 重建，训练其原图优于重建图，并用随机 crop 放大局部瑕疵。[AdvFidelity 的受限对照](https://arxiv.org/html/2610.29380v1)以此减少不相关图像间风格、语义差异的干扰，却没有证明重建内容完全不变或分数等于真实保真；reference 选取、在线负例与头部更新共同限定目标。配对重建、参考制备、crop、全部 discriminator 更新及 rollout 反传均付费，单阶段与少步不抹去已对齐参考模型的成本；代理或内容失配时保原监督、固定可靠反馈与独立质量检查，不由更高 reward 或一个对抗 head 批准无瑕疵。

## V8 — LiveAct 2610.29408v1（2+2+2=6；标准必要完成，拟 Ch25 gap）

[官方 exact-v1](https://arxiv.org/html/2610.29408v1) §3–4/Conclusion，以及D–E和F1–2直接condition/attribution/causal反侧。共同visualstate中，对每agent用description-conditionedsoftgate只调query；每个control dimension单独保schema文字+同步scalar affine modulation作KV，每agent独立crossattention再sumresidual，不先改共享X也不把gate当supervisedmask/真实identity。数值index、visualrecipient与control含义三者不等价，动作值本身不能绑定视觉agent。每latent只读对应4rawframes，globalindex随KV推进，TFcleanhistory→selfrolloutDMD保持同HAI。

6sources17951trajectories/119.54h，108heldout81frameclips（每trajectory1，seed0），Wan2.2TI2V5B/fullDiT+HAI训练、frozenT5/VAE、每agent12dims，10kteacher/6kcausal/700DMD、FSDP、batch16/24，DFake每5步才Gupdate+EMA，4latents/chunk、4NFE无CFG。Baselines3个releasedcheckpoint未同data重训、ActionParty同budget但nativeinterface扩连续值、WanToFight作者reimplementation给identitycrops，故主对比不隔离架构因果；ablation同data/budget/seed更窄。SGAA flatMLP同时删perdimtokens/schema/modulation，F2 ID/addition/shuffleschema必要对照已读，只支持该familiar source语义接口，不授任意unseen schema/agent数。

ActionF1/NRMSE来自只用realtrainingclip训的smallCNN inverse evaluator，非真实执行。AttrAcc只计两agentcommands有差的frames/pairs，intendedassignment比swap更小error，tie.5，按frame→clip→source等权；.898/.942不是每frame物体identity人工正确率，也不认证physicalcausal。17.70FPS仅单GPU512×448、未给GPU型号/完整firstchunkdeadline，TF1.66→DMD17.70还改CFG5→none与50→4steps，非纯因果mask加速。DMDrobotNRMSE.430teacher/.473TF→.558、Attr.969/.970→.942反退，不能均值掩盖控制损失。全部schema编码、peragentattention、全DiT/teacher/fakescore/rollout、KV与decoder计费；video不是机器人action或安全权限。

actualCh25:738–770已有固定subjectslots/agentaxis与hub通信，226后actionschema文字化与SCOPE局部响应，但缺共同画面中“query绑定谁”与“KV保每个control语义+值”的两侧接口。唯一MULTIMODAL-WORLD-MODELS，完整首段“多主体控制首先取决于observation的归属形态…”/2604.02330marker后、`semantic-body-binding:SF-2026-ARXIV-2605-28816:start`及其“单主体WorldModel只需要一条…”完整段前，PRE：

> 共同画面的异构控制还须把接收者与变量含义分开：用 agent 描述对 visual queries 作软空间调制，每个 control dimension 则保自己的 schema 文字，并由同步数值调制成 KV；各 agent 读取同一未修改状态后再合并控制残差。[LiveAct 的受限对照](https://arxiv.org/html/2610.29408v1)支持这个双侧接口，不把 stream index 当物体身份、也不把同一 tensor 位置当跨任务同义。Gate 不是显式 mask，inverse-model 的 swap attribution 也不是真实执行证据；迁移到少步 causal rollout 后机器人控制仍可退。Schema/时钟、逐主体 attention、teacher/rollout 训练、KV 与完整解码均付费，单 GPU FPS 不认证互动 deadline；绑定、语义或质量不稳时保固定主体/专用 action schema、短生成段与显式 simulator，由真实 controller 验收动作，而不让联合画面取得物理与安全权限。

八项必要 Source/实际owner/拟处置已完成，V6具体NC、余七个窄PRE均提交reader；这里不代独核或root实际落书/POST。没有代码运行、论文复现或日级完成声明。
