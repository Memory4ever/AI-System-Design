# 2025-09-11 独立非作者 DAY 复核

复核者：Aristotle（非作者）；作者：Bacon。检查时间：2026-10-06T13:36:00+08:00。

最新结论：**DAY 通过**，2026-10-06T13:59:28+08:00 已完成作者13:49有限返修的差额验收，见§7。下面§1～6保留13:36原未通过依据，不抹去原问题或扩张实际阅读范围。正式状态/计数同步由root验收，本复核不改报告或共享状态。

13:36结论：**未通过，存在可执行的有限返修**。不是因为日期受阻而要求重审全文，也不是否定 Qwen 单项：正式候选 1 个唯一家族 Qwen3-Next 的日期、6 分准入、必要反侧及限定 Books No Change 可通过。最终 DAY 尚需同步下述 A/B/C；不能把这份 checkpoint 当已通过。外部历史/first-public 缺口可按当前合同隔离为安全终态，不授正面 Coverage/Evidence/Books。

唯一写入为本文件。未改报告、Books、共享文件或状态，未 stage/commit/push，未改模型。当前工作树已有 staged/unstaged 研究与 Books 改动，未回退或接管；不把这些既有改动归因于本复核。

## 1. 独立上下文与实际范围

换到单日后重读当前 AGENTS、CODEX_RESEARCH_PROMPT、RESEARCH_CONTRACT、REPORT_CONTRACTS，来源清单使用说明/全部 14 个每日入口/arXiv 主题，ROADMAP owner/阶段边界及最新九月 checkpoint（仅路由）。窗口为 `[2025-09-10T09:00+08:00,2025-09-11T09:00+08:00)`；未加载或审查 01、02、26 的材料。

读完本日 HANDOFF、QWEN_REOPEN、EVIDENCE、SCREEN、INDEPENDENT_CALIBRATION 及正式 README 六部分。复用 root 的有效首批校准，但自己读了下列原始题摘/受影响正文，不拿作者“已读”声明代替独核。

- 两个有限 Atom feed 的身份、请求和返回计数独立解析；浏览其标题。原 SCREEN 潜力段涉及的 102 个唯一身份完整题摘全部读到，包括七首批项、已关闭的 08785 和版本说明中的 08318；不是 102 个正式候选。
- 另读 20 个风险/普通关闭分层样本完整题摘、34 个 supplement 差额题摘、14 个 scoped 未列路由题摘、两批各 12 个含糊/风险/家族核题摘，以及 08151 精确 v1。合计 **195 个唯一 arXiv 身份完整题摘**，其中 **162 个属于两 feed 的 207 身份并集，33 个是原月度有界查漏/定点恢复**。这些数是本次读过的身份，不是当窗新论文数、Evidence 完成数或候选规模。
- 并集其余 45 个仅标题查漏/范围判断，不宣称完整题摘或正文全量审阅；整个分类月表、其他日期、所有附录、全部附件、代码与实验均未全量复核。标题含糊及新发现的安全/设计反证已经定点展开，未把所有领域条目变成队列。
- 正式候选 Qwen 的完整官方正文 Introduction 到 References、精确 config 对象、三幅实际图，以及 Ch22 的 GDN/Hybrid/output gate 相关完整段已独立读；只核必要 owner，未声称审完全部 Books。

## 2. 必须同步的普通返修

### A. 两次 146 返回不是同一身份集合

原件 [scoped](arxiv-scoped.raw) 与 [supplement](arxiv-supplement.raw) 均 start=0、max_results=200、totalResults=146、实际 entry=146，无尾页。按 Atom id 最后路径段再剥版本归并：**交集 85，并集 207，各自独有 61**。请求里的 submitted 区间都是 UTC Sep9 18:00 到 Sep10 18:00；scoped 有 12 分类与第一组主题限制，supplement 没有该分类限制，主题组也不同。

因此 README §1/§2/§5、SCREEN 开头及 HANDOFF 中把补查称“同146/同身份集”的口径需修。207 也只表示这两次提交窗口 discovery 的去重身份，不是 207 个首次公开落窗事件。月表 2509.08000～08840 的 256 个去重标题及 11+37 精确 v1 定点恢复另述，不相加成新论文或已审候选。

已替作者定位并读完差额中的相关/含糊题摘，具体退出见 §4。**08315 EvolKV 已在 11 项精确 v1 probe 中，当前 SCREEN 却无身份/处置**，不能用“已读 probe”代替漏掉的贡献路由。补齐路由即可，不要求 207 篇全文。

两入口确有过宽部分：孤立的 `all:attention`/`all:GPU`/`all:agent` 和无分类限制的 supplement 引入天体、普通网络/医疗预测等。实际宽返回保留为发现缓存，不删除反证。可执行窄修是按下列四组分别限定，再只补本次受影响项；不把所有分类变成队列，也不必为已有可核题摘重新跑全部查询：

| 组 | 查询约束建议（沿用原 submitted 区间，但不得授公开日期） |
| --- | --- |
| 模型 | CL/LG + language/foundation model、MoE、state-space model 等；attention/transformer 与模型架构/训练/上下文语义联合，不用孤立 attention |
| 系统 | DC/AR/PL/OS/PF + language-model training/inference、KV/expert、kernel/runtime；GPU 与模型训练/推理限定联合，不全扫 GPU 应用 |
| Agent | CL/AI/IR/MA + LLM/language model + tool/planning/memory/RAG/evaluation；不单用 agent 扩入全部传统多智能体 |
| 多模态 | CV/RO/LG + VLM/vision-language/foundation/generative model/world model/VLA；正文再核表示、生成或行动的具体增量，保留明确的新命名/理论反例定点查漏 |

### B. Meta 停点需引用真实 page5 → page6

保存的 `meta-publications-page5.raw` 可见主序止于 Sep15；没有 Sep8/Sep2。其 canonical 是 `global_search/?page=5`，真实 Next 指向下列结果页，不是泛用 `/research/publications/?page=6`。

本复核实际补请求：GET `https://ai.meta.com/results/?page=6&content_types%5B0%5D=publication`，User-Agent `Mozilla/5.0`；2026-10-06T05:35:02Z 发起，HTTP 200，275689 bytes。解析可见正文后主序 12 项为 Sep8（GRAPE）、Sep2（语言生成 diversity/quality）、Aug22（confidence）、Aug14（DINOv3）、Aug13（brain/CV convergence）、Aug12（Llama speculative decoding）、Aug5（OMC25）、Aug5（FastCSP）、Aug4（Open DAC）、Jul1（ASTRO）、Jun27（Seamless Interaction）、Jun13（multi-calibration），之后另有 2017～2020 旧项。初次本轮补取也返回 HTTP200/275932 bytes；动态字节差不作为 identity 变化。

这支持 **已检查 page5 Nov18～Sep15，再到真实 page6 Sep8～Jun13** 的有限跨窗停止；不支持“page5本身 Sep24→15→8→2”，也不支持全历史无遗漏。未把旧 pinned 样本日期当排序保证。泛用 page6 曾只返 45 bytes 的 unavailable 文本，不能冒充空列表。

遵守唯一写权限，没有另存新 raw/header；本段保存实际请求、状态、可见身份和停止依据。作者可引用本段同步正式来源行，无需把本次普通补查重新写成外部 hold。

### C. 08120 与 08318 不能混用；新反证不能按领域/日期误关闭

SCREEN 的 `08233、08257、08120` 行把 early-exit calibration 归到 08120。实际 **08120v1 是 Optimization Methods and Software for Federated Learning thesis**；**08318v1 才是 Boosted Training of Lightweight Early Exits**，完整题摘明确 full-dataset branch training 与 hard-conditional inference 的 covariate shift，BTS-EE 顺序训练 + class-wise CPM calibration。分开身份和潜力，版本说明中的 08318 不能代替该处身份修正。

§4 所列新机制/局部负结果需增加有界贡献路由；保留仅基于摘要可支持的潜力。无官方 first-public 不赋本窗分数或 Books。明确普通关闭项已给理由，无需再开全文或无关日期请求。

08157 当前“没有 foundation-model/动作表示机制”不是充分退出理由：实际 v3 题摘为视觉 GCRL 图 + CBS 下，edge deletion 与全局风险预算/迭代 per-agent risk allocation 的可行性、路径长度取舍。可保留模型驱动行动 safety envelope 的有限替代设计问题；不能因传统 planner 名称或未出现 foundation 词就关闭，也不授实际安全保证。未因此恢复所有传统规划条目。

## 3. 正式候选及必要 core 反侧

| 身份/实际阅读 | 独立判断与停止边界 |
| --- | --- |
| Qwen3-Next，官方精确 config、完整正文、prefill/decode/RULER 实际图 | `date=2025-09-10T20:00:00.000Z` 对应 BJT11日04:00，官方对象绑定题名/id/tokenLinks，不是 arXiv submitted 或索引注册补造公开时间。准入 2+2+2=6 可接受；hybrid/稀疏 recipe 多项同变，不能授 3:1 最优或单独因果。正文为当前官方 token 内容，未核 2025 冻结 runtime 实现。 |
| Qwen 图/兼容边界 | prefill 的有限长度相对32B趋势可报，decode4K约3.4而非“所有情况接近4/超过10”。RULER192K为94.0<235B94.5、1M为80.3<84.5，不能授全长度领先。hardware/precision/batch/concurrency/SLO/runtime 未绑定图，Not Disclosed；4GPU运行示例不是图的硬件证明。native262144与1M YaRN分开，static YaRN短序列代价、main分支及Transformers MTP限制保持作者声明性质。 |
| Qwen Books | Ch22 实际491～515的 GDN alpha/beta 衰减/方向写入，765～810的 hybrid 两状态/显式历史/KV代价，850～880的 output gate 与 memory-transition gate 区分承载三项原则。No Change仅授这三项；不声称512专家recipe、MTP release、吞吐分布已有覆盖。Ch21/23邻接开头只核边界。无拟写入，Books增量0。 |
| 08309v1 Hetis：§3.1–3.2/4.1–4.2、§6实现和§7.1硬件受影响段 | head级decode与dense/prefill分工/通信条件有潜力；4A100+4RTX3090+4P100/100Gbps是受测配置，160GPU为模拟。近似Δ=.05筛选不是全局最优；缓存/迁移与SLO不等零成本生产能力。其余消融细节复用 EVIDENCE，不宣称独读全部§7。 |
| 08342v1 MoEpic：§3.1–3.2、§4.1设置与4.4消融 | segment cache与真实router fallback成立为机制描述；Qwen FP16/Mixtral HQQ条件不同，GPU数与完整SLO配置未绑定。随机prefetch/cache及uniform+.5复合消融不能独立归因。未独核完整fixed-point推导、未运行实现。 |
| 08184v1 Selective：PDF pp10～13 §5.2～7 | normalized probability score不是posterior likelihood/BMA。一般Claim1完整证明留future work；未读AppA全部特例证明。单head训练胜构造是必要反侧，不能说多head唯一必要，不能外推现实因果发现。 |
| 08358v1 Toxic：§3、Table2、§4.1～4.2 | Human ParaDetox J=.481，合成同源.428～.459/SST2 .322～.362；该局部反证保留。Human Evaluation实际GPT-4.1 judge；lexical gap是相关性，source支持集变化未隔离，未授“所有synthetic必败”。 |
| 08755v1 AgentGym：完整PDF必要pp9/11～12、Fig7实际像素 | fixed10曲线早升后约150轮坍塌，fixed5较低而稳定，渐增horizon局部更好；不把轨迹观察当credit/variance因果识别或稳定保证。WebArena26 vs22为4pp，低于o3/o4-mini。B.1/B.2精确预算复用作者现有记录，未声称自己读完31～33页。 |
| 08721v1 SAPO：§3.2/Algo1分享接口、§5局部/外部对照、§6异构demo相关段 | retokenize后的own-policy likelihood不等behavior-policy importance correction。1093 vs561.79为累计reward非accuracy；零advantage筛选/预算不同。Qwen3-0.6B无改善、agent min/max不是重复运行CI；未授任意async收敛/抗污染。 |
| 08826v1 RewardDance：§3.1～3.3/4.1、4.4 Tables7～9 | yes-token比较reward依赖reference，best-of-N/ref质量、CoT、pruning分别有成本与混杂。variance不是CI或独立hacking检验。保留局部偏好与输入参数化潜力；未独读全部曲线像素/附录，不采用“解决hacking”。 |
| 08646v1 Secure Plan-then-Execute：§2.1～2.2、§3相关机制、§7.1重规划、A.1实际executor代码 | trusted immutable plan条件不等工具名白名单。single-tool create_react_agent仍接raw past_steps，可变参数/重复调用，write_file示例无sandbox；replanner消费不可信history未独立可信revalidation，immutability条件会失效。安全中心争议保留，不作普通教程关闭；无形式证明/对抗复现。 |
| 08151v1：精确HTML摘要、§II～III | 三层semantic-tree/device-task memory与central teacher减少重复问询，不是参数蒸馏；原关闭的新增机制不足理由可以复用。未声称本复核读完其全部实验。 |

上述七潜力与安全项均尚未确认 first-public 落窗，**不是8个本窗证据完成候选**。必要反侧已足以禁止当前不当采用；不会为 datehold 预读所有条件性附录。之后拟采用具体命题时才重开缺少的准确段。

## 4. 差额潜力与有限关闭

以下全部实际读完整题摘。尾号默认 2509；保留当前版本，不把 v2/v3 等最新题摘当 v1。仅潜力，无本窗评分/采用/Books；可能合理准入并不等于可信度已验证。

### 应补保留的差额路由

| 身份（当前或精确版本） | 原约束 → 实际增量 → 有限重新考虑的选择 |
| --- | --- |
| 08142v1 | VLM语义通信泄露身份 → private image mask/shared privacy DB/条件重建 → utility与可识别性取舍；只报局部泄露减少，不授隐私消除 |
| 08315v1 EvolKV | uniform/static层KV预算 → task多目标逐层预算搜索 → quality/cache/search成本选择；已在exact probe，不能漏路由 |
| 08344v1 | 适配需全emotion-label说话者数据 → meta-trained SLM few-utterance ICL → 不完整标签下条件适配；不是通用情绪准确保证 |
| 08372v1 | source-free FL依赖复杂聚合/域适配 → frozen VFM backbone局部反侧 → 先核表示而非默认叠控制模块 |
| 08379v1 | speech latent生成质量/速度冲突 → latent bottleneck下diffusion与flow比较 → 条件采样路径选择，非单个新任务分数 |
| 08458v2 FSSM | SSM离散化token相关/累计误差 → first-order-hold状态更新 → 通用状态近似问题；SR应用不抹去该机制，历史采用需exactv1 |
| 08561v1 | nonsmooth manifold/DC稀疏优化难解 → 有条件的l0等价、inexactness criterion/local-curvature线搜/复杂度 → constrained representation/优化选择；不称一般深网收敛 |
| 08570v1 | image/text语义gap/feature dispersion → EM semantic centers+text-guided decoder → 有限融合路径；不采用医学诊断效果或整领域知识 |
| 08575v2 SQLGovernor | whole-query改写代价/正确性 → fragment-wise rewriting+DBMS feedback/rule validation → 局部重写验证边界；非本复核生产保证 |
| 08618v1 CLAPS | text disease prompt的modality ambiguity → modality signature及自动空间prompt → 模态身份在基础模型prompt接口中的作用；模块组合其余部分不另授贡献 |
| 08640v1 RoentMod | 预测正确仍可能shortcut → counterfactual CXR edits并检查未改特征 → 可复用的表示/robustness反侧；不是医疗应用全收入或患者建议 |
| 08689v1 | speech漏指代对象 → gaze/pointing/场景metadata textual augmentation → 模态上下文是否支持coreference；12人结果局部保留 |
| 08696v1 | 少步TTS可能退化 → L1-error校准attention/FFN SmoothCache schedule → 少步数与缓存并非等价加速；保持局部质量反侧 |
| 08699v1 TANGO | 全局3D map/learned controller成本 → foundation RGB topometric+local metric/fallback → 行动闭环的条件替代，不授普遍零样本安全 |
| 08724v1 SWE-Mirror | authentic history数据难扩 → semantic issue mirroring复用可验证gym → 合成任务覆盖与可执行验证条件 |
| 08805v2 BEAMER | 单hypothesis跨尺度在zoom/depth discontinuity失败 → multi-hypothesis beam并入cross-attention → 表示不确定性保留；不把所有dense matching收入主线 |
| 08808v1 ROLex | 新knowledge需重训 → growing expert lexicon检索/生成及subset-focused training → inference-time扩展知识的接口条件 |
| 08863v3 | GeoJSON func API与codegen两路线 → 70tasks下灵活性/稳定性比较 → 有限工具执行设计反证，非97%可靠保证 |
| 09722v1 | test-time增强看似提高识别 → transcription consensus/confidence；grid warp会误导confidence → augmentation与评价校准分账，622记录不否定局部反例 |
| 2510.21714v1 | cross-domain序列field/target interference → decoupled embeddings/target-position representation → 保留表示干扰问题，不采广告GMV或绕回全推荐队列 |
| 2511.05494v1 | 用户unlearning重训成本 → retrieval隔离用户影响并条件生成 → inference路径与base-weight遗忘严格分开；未来ID也不能倒授Sep11首次公开 |
| 09717v1 | audio chatbot有效encoder结构不等对齐 → 2M训练后仍有对齐/creative-task失败 → architectural bias与训练目标边界；具体负面潜力 |
| 08104v1 APML | nearest assignment拥挤/不可微、EMD cubic → temperature-controlled Sinkhorn概率多对一matching/near-quadratic → 表示学习loss的条件取舍；未证明此界用于所有模型 |
| 08122v2 | categorical covariate新levels表示困难 → similar-instance context batch更新CLS → ICL/representation对未见feature-level的条件选择；不是“credibility”安全认证 |
| 08139v2 SCA-LLM | 非text CSI到frozen LLM有domain mismatch → spectral-channel adapter → 模态对齐/有限dynamics预测，不把wireless指标当World Model整体成立 |
| 08160v1 | 多机械臂joint data随规模增长 → single-arm生成+pairwise collision因子/MAPF → factorized生成到闭环约束的设计选择 |
| 10561v1 AVEC | privacy budget/置信度耦合、delegation验证不足 → adaptive DP odometer等方案及hash-only/deterministic gating不可能性论点 → 隐私/验证反侧；position/simulation不能授生产或定理已证 |
| 08436v2 HyperTTA | 退化造成shift → high-confidence entropy驱动仅LN-affine adaptation → test-time无源数据适配的条件，不能因hyperspectral应用自动关闭或授“可靠” |
| 08493v1 | 自动scambaiting有无实际阻断效用 → 实际2600次engagement及seed response较强的分母反侧 → 评估agent操作目标与响应proxy；不授模型安全防护或治骗保证 |
| 08596v1 BioASQ ensemble RAG | 延长context未必改善 → 原摘明示dilution/disorientation → 通用检索上下文负侧；不采用医疗domain结论 |
| 08757v1 SocialNav-SUB | VLM社会/时空理解假设 → 简单rule baseline更好、人类判断不一致 → VLA perception与safety envelope边界 |
| 09721v1 | visual evidence/text policy prior对生成控制不清 → two-branch alignment+modal attention gate/joint objectives → 仅融合控制的有限设计潜力，不采灾害保险业务指标 |
| 2510.06224v1 | 多agent“团队”可用性假设 → 13位early adopters具体error propagation/unproductive loops观察 → 有限运行失败/透明性需求；不是新control算法或通用发生率 |
| 08188v1 ArtifactGen | fidelity好可能不支持augmentation → WGAN/diffusion各自preprocess，二者weak class recovery/utility有限 → 保留conditioning/support与downstream utility分账反例；不声称因果或医学诊断能力 |
| 08157v3 | 高风险edge直接删除会丢可行任务 → global risk预算与迭代per-agent分配 → model-driven行动闭环局部取舍；风险估计/安全证明未授，exactv1与日期另隔离 |

这里 **35 个差额/改判身份** 要保留题摘支持的最小潜力，非35项deep/fulltext待办。其中晚分配ID、当前修订及领域实验一律不移入11日候选。后续评分仍可按实际主张关闭，不能用日期 unknown、既有主题或负面结果本身关闭。

已有窗外/更早家族线索 08222v1（ExRAP的memory validity/exploration与temporal consistency）、08753v2（DSM alignment/delay）、08809v1（CAI consistency proxy与oracle accuracy）完整题摘也已读。有实际机制/评价问题，原更早家族身份恢复需求合理；目前不称“已有有效审阅”去重、不授first-public，更不创建另一日报。CAI的consistency correlation不是无oracle真值证明。

### 可有限关闭的差额和抽检层

| 分层/已读样本 | 退出依据，非统一标签排除 |
| --- | --- |
| 新任务/模块流程：08090、08400、18108、08215、08380、08865 | code prompt mining、wireless evolution设想、多角色loop、CodeBERT/GPT组合、AML模块、malware TraceRAG题摘未给改变执行正确性或泛化解释的具体新条件。08380的privacy/可信与08865的检测指标不授安全保证；当前可关闭的只是该原文增量，不是其领域无价值。 |
| 编译/硬件/网络：08135、08207、08608、08727 | 普通network elastic admission、Aurora HPC配置/standard benchmark、baseband MCU、crypto assembly SecSep；实际约束不绑定本次model计算/执行主张。08727的stack秘密跟踪机制真实存在，关闭是本项目关系不足，不是否认安全贡献。 |
| 领域建模/既有生成或NLP：08128、08205、08289v3、08612v3、08776、09726、10555v2、18115 | 社交参与、speech RPCA、WSOD、ABSA、CSI entropy coding、proof verbalization、clinical dataset/CLIP、time-series图模块：题摘未建立拟长期保留的foundation/生成/表示成立条件或评价反证，具体新业务指标不够。不是按模型大小关闭。 |
| 评价/综述/立场：08216、08269v7、08087v2、09723v3、08302、08345、08621、08712、08827v3 | retrieval四指标比较未指出解释盲区；LLM优化/healthcare评估/自动驾驶综述与一般局限尚无新的具体校正证据；psychometric nomological network属于测量领域应用，writing/ad任务相关性/指标未建立一般confound。最新survey版不冒充v1深审。 |
| 一般CV/医疗应用：08265、08586、08234、08338、08442、08228 | HyMamba scan模块、CNN/ViT有限data指标、灰度channel replication、patient-case retrieval、cortical trajectory sphere-U-Net、optical sensor reconstruction：题摘新增停在本领域task/既有模块适配，没有§4对应的通用机制问题。08586的theory标题不能代替摘要实证；不授clinical reliability。 |
| 暂缓科学/行业决策：08303、08535、08820、08310、2510.15896、08731 | oil-palm/LHC/chemical discovery/microgrid resilience/ED staffing/SDE portfolio的当前增量面向领域发现或决策，不借Agent/Data主线绕回。各自安全/理论词已读，不把领域控制声明采用为模型系统安全。 |
| 风险/理论立场：08200、08009、08835、08592、08463 | CyberArena部署故事无新模型执行条件；LFAI批评借既有misalignment并提出尚未验证benchmark/控制；opacity哲学区分、interpretability倡议、fact-checking attack survey未提供当前可采用的新机制/实证反例。不能把关闭改写成已验证law-alignment、隐私或防护。 |
| 传统planning边界：08859、08460、08312 | robot task allocation、reach-avoid herding、telecom reference architecture的当前题摘没有模型学习/动作表示或新的LLM执行成立条件。与08157具体budget可行性差额区别处理，不凭CBS/传统身份统一退出。 |
| 原四代表：08151v1、08203、08489、08827 | v1 central memory、semantic-unit/microservice原型、detector/segment/inpaint/caption组合及survey：新增不足理由可复用；四人/小例子/主题已有不是理由。 |

原 SCREEN 风险/反证集合也完整读到：08000/08004/08008/08010/08016/08022/08031/08058/08075/08089/08146/08182/08195/08217/08255/08329/08380/08416/08449/08469/08480/08483/08484/08486/08494/08538/08541/08593/08604/08638/08653/08660/08682/08683/08709/08726/08729/08738/08750/08755/08775/08777/08803/08804/08812/08814/08818/08824/08825/08829/09731/09732/09734/09735/13332/13333/13334/18111/18113/18118/18119/18122，及上述必要core项。保留局部偏差/误拒绝、DP/恶意server审计、judge/annotation统计、跨任务UE失效、morpheme proxy无显著MT收益、tree理解高但分类退步、med-LM记忆隐私等原负侧；没有发现支持因datehold删掉这些潜力的理由。题摘保留不等于每项原claim已可信、安全成立或无重要修订。

## 5. 14 来源 finite 检查与六部分边界

| 来源 | 实际独核停止范围/结论 |
| --- | --- |
| OPENAI | RSS1247项/760851bytes解析；Sep9T10Z与Sep11T14Z夹窗。有限RSS没有本窗项，不授删除/未列研究覆盖。 |
| ANTHROPIC | Next.js push字符串解析恢复172unique publication；Sep5到Sep15，不把库存变全文队列。 |
| GOOGLE | Research月页1→2/2共13；Sep11 cascades官方核心与linked2405.19261 identity核，v1May29 2024/v2Oct21，当前未见新方法/实验/纠错，可贡献关闭，不是已审重复。DeepMind3→4→5，Sep17/22/25 JSON-LD为窗外，非日期标签造时刻。 |
| META | Blog1→3；publication5→真正6按§2B补足。须修正式行，不授全目录无遗漏。 |
| QWEN | 精确官方config及101627bytes正文/三图按§3；旧首页夹日期不是完整目录。 |
| DEEPSEEK | 官方updates Aug21→Sep22/29有限切片可用。 |
| MOONSHOT | 平台Blog15项主序Sep16→Sep5；未扫完整GitHub，无具体新release触发。 |
| HUNYUAN | 正确host POST page1/size100/render0返回9=total9，均2026；错误host404与浏览器超时记录复用。未自称重做浏览器；2025目录仍外部hold，不是0。 |
| ZAI | 新page2/3原响应及派生文本实际比对，均18可见项，Aug2026→Dec7 2025/没有更多；release-notes实际Sep30→Aug11→Aug8→Jul28。重复分页已执行，Research2025历史仍隔离，不授Coverage。 |
| SEED | BlogAPI15/49/has_more，page0非pinned Oct23→Aug21→Jul跨窗，pin Sep9不作为唯一停点；type1 US/CN total94/has_more但无条目数组，论文历史外部hold，不记0。 |
| ERNIE | 真实1→2/2，Sep12→Aug14，无本列表落窗项。 |
| MIMO | Paper8（Sep19→Jun4/May12）；Blog15 undated/More历史未恢复。只授实际切片，历史Blog隔离。 |
| MINIMAX | EN12末Oct27，CN13末Jan15；EN?page2相同12项，非两语言均跨窗。正式行宜明示分列端点，历史分页/Agent仍hold。 |
| ARXIV | 两feed union207/无尾页，月ID带256，exact probes11+37；先审贡献，再隔离首次公开。CV/RO传输截断、CL2000/2214不是整月覆盖，未授官方日batch。 |

所有到期14行存在；无每周组扩扫。Hunyuan/ZAI/Seed论文/MiMoBlog/MiniMax历史/arXiv first-public 属外部保留，不用于候选、Books或无遗漏/性能/安全保证；不以DataCite登记、API published、submitted或日历schedule冒充首次公开。恢复官方正文/announcement或完全落窗的有据区间后仅重开相关身份。

六部分逐项：§1候选1/Books0及局部反证边界可保留，discovery146改207并区分查漏；§2修Meta/arXiv口径及MiniMax语言端点；§3唯一Qwen、日期和评分可通过；§4三个机制NoChange有实际owner，不授图普适因果/安全；§5区分本次普通A/B/C与隔离外部hold，不把普通未同步工作写安全终态；§6应汇总本次实际非作者检查/未覆盖与返修结果，不能提前把本记录改成通过。其余日期潜力不是正式候选，不能为保证终态删掉。

## 6. 机器检查与局部复核停点

当前正式 README 的 `validate_research.py --report` 已通过1份V3；限定 README/本日_sources 的 diff-check 已通过。正式 README 与本记录的本地 Markdown 目标均存在，fence配对有效；新增本记录的 no-index whitespace check 无错误输出，35行潜力路由计数已独立核对。结构通过不替代以上语义返修，不修无关既有 staged 内容。

**作者下一步只需 A（207身份口径与35条最小潜力路由）、B（Meta真实5→6来源同步）、C（08120/08318及08157退出修正），并在正式六部分说明实际非作者范围。** 未要求新增全文下载、重跑整月或改Books。作者同步后，最终差额复核只检查这些变动/新证据和最终六部分；已有效的 Qwen、七潜力core、风险反侧与普通分层样本不重复审阅。当前没有授权替作者修改报告或状态，故本文件保留未通过。

## 7. 13:59 有限返修最终 DAY

复核者：Aristotle（非作者）；结论：**通过**。对象为作者Bacon的13:49:18正式README、SCREEN/HANDOFF修正及新增[35路由](DAY_DELTA_ROUTES.md)。本轮重读当前合同后，仅核 A/B/C 与正式六部分；没有重读已有效 Qwen/七必要core、重新下载全文或扩大月表。

- A：原两feed再次独立解析，各146，交85/并207/各独61；35条身份、版本、有限命题逐行与§4相同，比较结果35/35一致。正式§1/2/3/5均明确submitted discovery而非first-public/候选/全文分母；月带256和11+37定点恢复另述。过宽入口只保留缓存，四主题窄重开约束已引用；没有新增整类队列或错误删减负面结果。
- B：正式Meta行引用真实page5 Nov18～Sep15，再到本复核实际GET的results page6 Sep8～Jun13；调用时间/HTTP200/275689bytes与§2B一致。未把page5伪称跨至Sep8/2，也未把45-byte unavailable当零列表。MiniMax EN12/CN13端点亦已分列。
- C：08120 FL thesis与08318 early-exit calibration分开，08315 EvolKV已补，08157改保留global风险预算/可行性反侧。35项读取角色明确为Aristotle、作者复用有效题摘判断，不冒称作者新读全文或已授v1历史结论。
- 六部分：唯一正式候选仍Qwen家族1/6分，Books0增量，三项NoChange的实际owner与图/native/YaRN/runtime边界未变。全部arXiv潜力与历史缺口/08646中心安全争议仍隔离，不用于正面Evidence/Books、Coverage保证或“无遗漏”。§5无新的可执行研究待办；§6保留真实前次未通过及当前等待差额核的进度，而未作者自授DAY。
- 机器：本轮 `validate_research.py --report papers/2025/09/11/README.md` 通过1份V3；README、SCREEN、HANDOFF、DAY_DELTA_ROUTES及本记录本地链接目标均存在、fence配对有效；限定范围 `git diff --check` 无错误。机器检查不替代语义结论。

通过表示当日约定来源、候选/风险及Books处置已到安全终态，不授被隔离历史来源或first-public缺口的正面Coverage/Evidence。正式README仍为作者返修ready的“进行中”，由root同步最终复核/状态/计数并验收；本复核只更新这个独立记录，未改报告、Books、State或索引，未stage/commit/push。之后材料到达，仅重开受影响身份。
