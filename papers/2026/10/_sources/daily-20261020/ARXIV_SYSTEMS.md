# arXiv systems / multimodal slice — Daily 2026-10-20

窗口：2026-10-19 ～ 2026-10-19，北京时间自然日。检查时间：2026-10-20 +08:00。
责任：只写本文件及 `systems_assets/`；不写 Report、Books、Learning State，不 stage/commit/push。
当前状态：首批 systems 11 项必要 Source 见 §6，七项 RO 见 §7；§8 三项已由准入事实定点补足必要标准 Source（安全/可靠性影响层深入）。均尚待独立证据复核与 Books 判断。§9 是另九个已由 root 完整题摘准入家族的必要 Source，逐项记录实际完成，不把准入或下载当证据完成。

## 1. 发现范围、原件与停止点

主题：DC/AR/PL/OS/PF 的 LLM/GPU/Transformer 训练推理、状态/通信/调度；CV/RO 的多模态基础模型、生成范式、world model、VLA；IR/MA 的 LLM RAG、记忆检索与 Agent 协作。

原始来源均为 `https://arxiv.org/list/cs.<分类>/pastweek?show=2000`。完整 HTML 和可读提取在 `systems_assets/list_<分类>.raw.html` / `.visible.txt`；只浏览 `Mon, 19 Oct 2026` 段，到下一日期标题前停止，提取另存 `.oct19.txt`。完整周列表只是原件，不是逐篇审阅队列；没有审阅其他日期。

| 分类 | 本窗官方段实际范围 | 本次处理 |
| --- | --- | --- |
| DC | 21 of 21 | 相关标题补检；非AI分布式算法不扩池 |
| AR | 12 of 12 | LLM accelerator、memory、compiler相关标题 |
| PL | 4 of 4 | 无明显大模型执行/编译机制命中；代码应用交核心slice |
| OS | `No updates for this time period` | 可确认该分类段无更新，不外推全arXiv零论文 |
| PF | 6 of 6 | operator interference、peak-memory等；cross类先去重 |
| CV | 126 of 126 | 只相关标题补检；医学/农业/天文应用及通用局部视觉不扩池 |
| RO | 68 of 68 | 只world/VLA/foundation相关标题补检；硬件机构/一般控制/SLAM不扩池 |
| IR | 11 of 11 | LLM retrieval/skills；不全扫推荐 |
| MA | 17 of 17 | LLM通信/agent执行边界；不全扫博弈/领域仿真 |

上述数量为分类段条目，不跨类去重，绝不是候选数。辅助搜索三组 `site:arxiv.org "2610" "19 Oct 2026"` 加系统、world/VLA、retrieval/multi-agent词族没有返回结果；不以此作零命中证据。官方 API 主题查询（`query_system`、`query_world`、`query_agent`，start0/max100，submitted Oct15–19仅作发现不作公告资格）与 Advanced 恢复请求失败/受限；当前不能宣称主题查询召回完整。官方段浏览提供独立有界补检。

精确摘要原件统一为 `systems_assets/abs_<ID>.raw.html`，完整可读版 `.visible.txt`；`Title:` 到 `Cite as:` 是完整题摘及评论，含当前版本/withdrawal等信号在原页保留。没有遍历全版本史。每项公告资格取本窗官方段，不用 submitted day 代替公开日。Books 所有权以 ROADMAP 为准，以下 owner 只是核验路由，不是已有覆盖声明。

跨类已交root/core slice去重：23409、22925、22906、22435、23328、23707、22511、23610、22655、22408；不在本slice重复审阅/计数。新增交接 22985 PrismAttention、23787 DLite 由本slice接手题摘。

## 2. 首批 systems 准入（root 完整题摘实核通过）

完整题摘：逐项 `systems_assets/abs_<ID>.visible.txt`。以下都是**候选**而非作者性能被证实。

| ID / 原文 | 旧约束→原文增量→改变的选择 | 路由 / 尚待证据 |
| --- | --- | --- |
| [23064 BaGuaLu-2](https://arxiv.org/abs/2610.23064) | MoE expert负载变化使静态activation余量浪费或OOM→按batch精确建模并动态provision→是否必须用最坏负载静态预留、以及何时重算/卸载 | TRAIN-DISTRIBUTED-TRAINING；必要方法/预算对照尚待 |
| [23047 DIFFLET](https://arxiv.org/abs/2610.23047) | Trainium2固定shape AOT与变长/step cache冲突→共享编译backend、head分核、device probe+host cache、resident process→AOT程序与动态cache控制的职责边界 | INFER-TENSORRT-LLM；不能把重载权重基线收益归因attention |
| [22863 KV Residency](https://arxiv.org/abs/2610.22863) | Agent调用间保留时间远长于GPU计算→生产trace估算、量化降级与驱逐/placement对照→KV应按跨调用residency而不只request内batch管理 | INFER-PD-DISAGGREGATION / INFER-GPU-MEMORY；代理Llama布局非真实501TB部署 |
| [22890 MailRail](https://arxiv.org/abs/2610.22890) | 高rank密度让每rank信用槽不足→共享node credit pool主动incast控制→credit所有权从rank升为node、避免接收方重新分配阻塞 | TRAIN-DISTRIBUTED-TRAINING；合成/trace replay非完整MoE训练 |
| [22769 One Communicator, Three Vendors](https://arxiv.org/abs/2610.22769) | 按row线性时间拆负载及旧异构加速结论→真实三vendor启动floor、GPU共享与transport纠错→异构split与benchmark隔离前提需修改 | TRAIN-DISTRIBUTED-TRAINING；纠错强制深入，读共享GPU与计时反证 |
| [22731 Accelerated Dataflow](https://arxiv.org/abs/2610.22731) | streaming以数据移动与固定worker并行调度推理→prefix-aware batch+engine反馈/异构pool autoscale→流式调度需消费engine状态，不只backlog | INFER-SCHEDULING / PLATFORM-GPU-SCHEDULER；对照配置待核 |
| [23503 HBFSim](https://arxiv.org/abs/2610.23503) | 扩展容量常只以带宽评估→LLM语义+flash更新/耐久模拟→HBM留KV、HBF写入寿命而非DRAM替代带宽即足够 | INFER-GPU-MEMORY；simulation，不是实HBF硬件 |
| [22877 BS-Spec](https://arxiv.org/abs/2610.22877) | draft模型/KV另存与固定精度→从同一BFP bit-plane构draft，weight/KV precision按workload校准→draft存储、精度和专用datapath联选 | INFER-SPECULATIVE-DECODING；硬件/quality条件待核 |
| [22579 MemLLM](https://arxiv.org/abs/2610.22579) | 预计算RAG KV转移跨PCIe形成IO wall→SSD内完整attention、稀疏重算/查询融合、SRAM reduction→少搬KV还是将attention下推storage | INFER-GPU-MEMORY；模拟器与端到端基线待核 |
| [23767 TileDRAM](https://arxiv.org/abs/2610.23767) | compute侧tile布局不能指定CU-local3D DRAM placement→compiler-visible tile-to-DRAM layout按访问序列评估→memory placement成为编译选择且无需新ISA | INFER-TENSORRT-LLM；trace replay收益与3090地址开销分开 |
| [23086 PairSight](https://arxiv.org/abs/2610.23086) | 单任务compute/memory标签不能预测共享干扰→双operator共同memory-path行为预测→SM隔离不等于memory-path隔离 | PLATFORM-GPU-SCHEDULER；六DNN含LLM局部条件待核 |

初稿代表拟排除快照（当时已读完整题摘；**后三项已由§8正文核验推翻，不是当前排除结论**）：23724 ArchAgent 是分层LLM+确定analytic evaluator在混合AI/HPC场景组合，摘要没有足够新执行机制/评价边界；22716 CMM-MP 本篇为通用CXL+Ethernet memory pooling，实测Valkey/DiskANN，LLM只在companion引用；23072 ScaleRAN 把precreated Green Context梯度分区及预测控制用于RAN deadline；22520 Soft Errors 题摘给injector+failure taxonomy。初稿对三者局部机制/诊断价值判断不足，后续准入及Source以§8为准。

## 3. 第二批 multimodal / RO 完整题摘初筛（等待root校准）

以下保留题摘初筛时的快照：“拟P”只表示增量可能改变明确选择；“拟C”表示当时未过门槛，不以模型/模块新颖或指标提高本身作为贡献。每行完整原文摘要均见 `systems_assets/abs_<ID>.visible.txt`。当时尚未读正文/评分/做Books决定；后续root校准见§5，实际Source见§7～9及其它owner的材料，不用旧快照覆盖后续进展。

| ID | 初判 | 具体旧判断→实际增量→待判断的选择 |
| --- | --- | --- |
| 23854 MFlow | 拟P | 像素diffusion常把x0优于velocity看成固定选择→主方向上学习混合，偏好随容量/表示变化→参数化要随容量重选；不以ConvRefiner常规模块为入选理由 |
| 23795 PPMem | 拟P | 持久3D记忆通常point-cloud高成本→7参数plane联合RGB预测、融合后depth回条件→在平面占优场景是否可用紧凑几何状态替代逐pixel记忆 |
| 23542 MIST | 拟P | 低hidden-change reveal分常解释遗忘→分开scene setup、transition execution、reveal→未执行的状态变化不能诊断为memory忘记 |
| 23531 PONDER | 拟P | masked生成随机/置信顺序不可纠错→冻结generator时学习fill/remask策略及budget扩展→推理顺序/重开已填变量是独立优化对象 |
| 23423 Momentum | 拟P | 静态image/point记忆无法推进视外动态→同步8-camera rig graph更新与interaction解耦→持久world state应含视外动态时间推进，而不只是历史缓存 |
| 23324 CatchUp | 拟P | deferred视觉token可后续恢复即以为无损→oracle揭示stale depth state，邻token transition估计补齐→re-admission需补状态演化，不能仅保留原token |
| 23279 XiaomiLens | 拟P | text-only reasoning不约束所访问region→共享visual patch与LLM mask-latent状态联合解码并监督→是否用可解码region latent替代无空间归因的text CoT |
| 23263 SCALE | 拟P | guidance-free等于模仿CFG且受其上限→real/self-generated prediction contrast并重参训练→单forward guidance目标可不以CFG为teacher |
| 22975 Sink-Sparse | 拟P | DiT attention每step动态dense→小离线集静态sink+pooledKV补支→importance支持是否跨generation复用，适用mask稳定边界待核 |
| 22957 QART | 拟P | query-independent/fixed-budget视觉token→query-support重构精度控制recurrent token分配→预算按证据保真自适应，不只固定压缩率 |
| 22499 JAVIS | 拟P | speech/face串联或独立输出引延迟/同步瓶颈→sharedLLM joint head统一音画表示、双stream→同步语义与实时输出是否共享生成状态 |
| 23615 HIJP | 拟P | latent-world规划需每次搜索action序列→hindsight inverse塑造goal表示且action-transition一致→测试时是否能用inverse/predictor交替替代搜索；限四task |
| 23566 TRACO | 拟P | 静态target attack监督不随已到达state变化→execution-driven重建监督+progress selection→VLA攻击成功不能只看固定target matching；安全受影响需深入 |
| 23378 ActiveAlign | 拟P | 先主动看再执行看似无害→首frame分布从46.3降11.5且matched-state/data controls→VLA训练需匹配active-perception终点分布 |
| 23372 IMEP | 拟P | memory消融成功率证明task事实被用→ULP/procedure噪声与fact-preserving替换、motor分离→必须验证事实特异因果，不能由success-rate差归因memory |
| 23334 LAW | 待校准 | WAM缺高层subtask progress→hybridVLM value fusion、prefix-of-failure监督→若可证明局部value对长程failure credit有独立收益才保留；“语言动作世界统一”本身不够 |
| 23156 ORD-WM | 拟P | 自由预测object latent会形变漂移→vector-neuron geometry latent上解析施加SE3→刚体场景可分离persistent geometry与pose transition |
| 23018 VLA-Fabric | 拟P | multi-arm常joint policy/任务分配→完整per-arm VLA之间context/latent/action多处交互跨backbone重实例化→team扩展不必破坏local action所有权；收益归因待核 |
| 22951 MambaAct | 待校准 | flow-VLA每denoise重复token cross-attn→prefix压成conditioning、Mamba action mixer→若只常规换backbone+参数减少则不保留，需核固定prefix与比较是否形成明确质量/latency取舍 |
| 22576 Embodiment Guidance | 拟P | frozenVLA跨body需示范/更新→source/target成功chunk classifier guidance、locked-wrist harmful反例→冻结policy可由少量calibration引导但不可行运动/coverage会反转收益 |
| 22556 RePlanMem | 拟P | memory-write常外部salience→对齐相邻action chunk共同future的分歧作事件触发→bounded memory可由policy自身修订信号驱动；尚未证明闭环task收益 |
| 22471 Embodied Intelligence | 拟P | benchmark高success易当实用embodied能力→统一ICL/步数后差距与world-clock原型、8body部署gap→必须绑定demo/实际elapsed控制预算，不以模型名或SOTA为贡献 |
| 23856 VGC | 拟C | synthetic distorted/consistent pair+flow做posthoc视频几何refiner；现题摘不充分区分常规数据/局部模块收益与新生成机制边界 |
| 23751 MTEdit | 拟C | packed-canvas采多turn轨迹减少drift，但题摘只给新数据生成组合及任务收益；若正文有controlled rollout比较能修改drift成因才重开 |
| 23677 PhysRepair | 拟C | generate/diagnose/local repair加experience流程；未见改变新状态或因果正确性保证，不能把causal constraints名称当新机制 |
| 23374 MOSS-Image | 拟C | 单流5B DiT+prompt enhancement与长文本/布局bench；题摘未披露足够训练机制，new recipe/模型发布不自动准入 |
| 23269 Ranger | 拟C | text定位、交叉核验image、crop后生成是可解释流程，暂不足证明新执行/检索可靠性条件；只给任务指标不能入选 |
| 23662 Metareasoning | 待校准 | SMDP joint action commitment/solver预算是真机制但一般robot planner，是否直接支持foundation control-path边界待定，不能因没有LLM实验机械排除 |
| 23396 AWAM | 拟C | virtual camera trajectory+world query+fixed-memory action fusion是已有组件pipeline；须有imagined observation有效性/替代策略边界才重开 |
| 23271 NestedVLA | 待校准 | hypernetwork生成task action-expert参数替代merging，可能具体修正skill consolidation冲突/存储选择；需区分普通task-conditioned参数生成与可复用新边界 |
| 23127 BeJEPA | 待校准 | dynamic predictor+successor压缩未来替代长rollout，可能重要time-horizon取舍；只global-pose指标还不够，需核联训/summary独立作用 |
| 23053 Model-to-Policy | 拟C | stochastic-kernel统一VLA/WAM解释与两实例，无新design evidence；不把符号统一当机制增量 |
| 23002 MAP | 待校准 | 统一Cartesian partial constraints为masked-action inpainting可能改变控制接口，但multi-mask/RePaint是否只应用已有生成技术待核 |
| 22496 RAX | 待校准 | 无demonstration/primitives/value的online code探索与verified-skill复用可能改变经验生成/skill持久化边界；摘要的emergent能力/跨body数字不足证明 |
| 23769 PRIME | 拟C | 跨trajectory最短路去除示范时间单调进度假设有局部reward机制，但摘要仅precision tasks，尚未说明对foundation策略/学习机制的直接增量；需校准不按小实验排除 |

## 4. IR / MA 完整题摘初筛（等待root校准）

| ID | 初判 | 具体理由 |
| --- | --- | --- |
| 23056 Thought Blocks | 拟P | latent消息表示不等于构造无需AR→一次生成fixed-size continuation KV state、区分表示/构造→agent通信延迟应计消息构建序列，可能可编译trajectory-to-state |
| 22899 Provable Authority | 拟P | identity/signature不证明当前交易授权→exact transaction digest、atomic capacity reservation、single-use sender-bound commit credential→运行时授权必须在commit并发边界重新判定；whitepaper不是已部署保证 |
| 22882 Cooperation Without Adaptation | 拟P | self-play合作分数被当适应能力→零风险、prompt、fixed partner/population composition干预→模型行为/合作要区分incentive response与fair-share模式；限CRG协议 |
| 23541 Humanity Last Choice | 拟C | GEO策略编辑空间是混杂但当前只是taxonomy+protocol呼吁，无具名controlled re-evaluation证据，不能把综述归纳升级设计修正 |
| 22797 ReRankID | 拟C | 推荐item SID-only ranking及rationale不faithful，属于通用推荐非本slice大模型RAG检索生命周期；交root确认不误路由 |
| 22703 NoveltyScope | 拟C | BM25+dense RRF+prosecutor/defender等角色与quote检查常规组合，50样本MAE不足新机制/可靠性条件；科学论文助手也不借道AIforScience |
| 23186 Code Skill Server | 拟C | incremental harvest/index+retrieval serving 993skill与代码指标，不说明新检索/执行/升级语义；不能因skill主题自动收 |
| 23092 Herm | 待校准 | abstract描述通用非理想channel多agent symbolic encoding，没有明确LLM系统/主线机制身份；需定点判其是否只是MARL网络通信 |
| 23078 Crypto A2A | 拟C | DID/credential/TLS/CBOR/ZKP/monitoring通用组合和survey，没具体互操作/授权新语义或实际攻击反证；不得把安全关键词当强制全文队列 |
| 22674 Gossip Agents | 待摘要 | 首次请求timeout；重试在途，外部缺失不当零 |

## 5. 必要证据进度与未处理范围

首11项本轮必要正文实读完成，精确版本、实际阅读段、反证和拟采用边界见 §6；不是独立复核通过或 Books 完成。正文 HTML 优先；22863/22769 的 `.raw.html` 实为 PDF 原字节，旧 `.visible.txt` 是错误的二进制文本解码，**不可作为实读证据**。本轮使用 pypdf 从保留原件机械提取为 `.extracted.txt`，带原 PDF 页码；以下页码均指这些原页，不把提取本身算完成。

后批 root 已实读校准 MM 除23279需定点判其region新增条件之外的10项、RO11项、IR的23056/22899/22882，并同意23662/23271/23127/23002/22496/23769按具体潜在增量进入必要Source。§3～4保留最初完整题摘初判及原理由，以上校准覆盖其中“待校准”状态；LAW与MambaAct不因常规模块名自动收或排。后批尚未扩Source。23724排除校准通过；22520需核硬件错误诊断增量，22716需核设备暴露语义，23072需核AI侧隔离/干扰，不因未给数字/非LLM负载直接排除。23279及这些具名点核尚可继续执行，不隔离为外部缺口。

正式Report/Books及独立验收由root负责；本slice不宣称日报完成。

## 6. 首11项必要 Source 实读（待 root 独立复核）

共用口径：公告归属沿用 §1 的官方 `Mon, 19 Oct 2026` 原段，正文页头的15/16 Oct是提交标识，不取代公开日期。以下精确正文均为 `2610.<ID>v1`；作者数据/模拟不等独立复现。评分对象为下述最窄新增命题，顺序为 Design Delta + System Reach + Durability。Books 只给唯一 owner 的处置建议，未声称已有覆盖、授锁或实际写入。未披露的性能字段不得自行补齐。

### 6.1 [23064 BaGuaLu-2](https://arxiv.org/html/2610.23064v1)

- 实读：`systems_assets/html_23064.visible.txt` §II-B、III～V、VI-A～D，尤其§V-A deferred planning、Algorithm1/2、§V-B correctness；未遍历参考文献。评分 **2+2+2=6**，标准完成，额外读了重排正确性条件以限定采用。
- 增量：不把MoE routing skew仅作为算力负载处理，而在warmup累积/1F1B释放的实际时序下分配micro-batch activation budget。router尚未执行不能准确预知本batch expert需求；warmup把实际超额反馈给后批，steady phase在gate后expert前可回退full MoE recompute。roofline先为算子提供recompute/offload/quantize候选，再用减内存最多的greedy逐项选择；共享tensor所有consumer的精度/设备要一致，否则量化多副本或offload后GPU副本未释放会反增/不省内存。不是全局最优求解证明。
- 双batch DP只保各类前缀顺序，依赖scheduling-point barrier，并要求 **x−y>2（PP>2）**，否则前批offload与后批recovery可能同属一个batch，不满足四类独立。不得外推到浅PP或任意异步schedule。
- 对照：128～12,288 GPU；厂商/具体GPU型号 **Not Disclosed**，每卡64GB HBM、BF16峰值480TFLOPS、节点8卡/400GB/s、跨节点4×400Gbps。GLM系32层188B～1041B，TableII逐项parallel配置；所有系统起点共用balanced-load离线parallel计划。Megatron-Kuai扩MoE内存模型，AdaPipe只开adaptive recompute；baseline OOM后调整静态策略重启，报告含机器cold-start、不含人工响应。因而1.14×/1.13×均值包含避免OOM恢复及其他细粒度/重排收益，不能归为纯动态budget收益。
- Fig11分拆静态细粒度1.16×、动态增量1.05×、重排再1.13×；model预测平均误差1.56%；runtime决策<10ms/iteration，对照iteration>18s。训练quality/收敛、不同精度activation策略的误差累计、公开独立复现 **未证明**；每个规模实际run时长、全局batch等如未给不可补造。
- owner建议 `TRAIN-DISTRIBUTED-TRAINING`（Ch36）：若现文仅静态activation余量，可补“gate可见性→pipeline累积budget→共享tensor mitigation一致性→PP依赖条件”的短论证。Ch35 checkpoint只交接OOM恢复代价，不迁移该机制所有权。

### 6.2 [23047 DIFFLET](https://arxiv.org/html/2610.23047v1)

- 实读：`systems_assets/html_23047.visible.txt` §3～7.5、§6 recovery及相关Table4/5边界；评分 **2+2+2=6**，标准完成。采用静态编译与动态控制分界，不采用框架通用性宣传。
- 方法：fixed-shape/device程序与host采样/cache决策分离；joint attention须只计一份replicated text且padding同时从softmax分子/统计排除。Ulysses换成head分片后用valid-key interval；Ring对text/各visual片分别返回未归一化sum/max/denominator并联合归一化，而不是相加已softmax输出。Ring当前不支持text padding，是明确未实现边界。
- step cache的device probe只算投影与首block归一化/modulation，input–output aliasing保留feature，host只收scalar决定skip；不必为每种动态skip重编完整denoiser。offline校准的可预测性重要：Wan probe拟合R²仅0.13，不因便宜就有效；未披露生产质量/SLO保证。
- 条件：单 `trn2.3xlarge` / Trainium2，96GiB HBM，LNC2=4逻辑core，124GiB host；torch2.9.1 / torch-neuronx2.9.0 / compiler2.26 / NxD0.19 / NKI0.5；默认BF16 TP4缓存关。五模型不同官方/降规格形状及guidance见Table1，LTX-2因不支持batch2而无CFG、且只第一stage。prompt/seed42/checkpoint/shape在同模型比较固定。
- 归因：same pipeline换SDPA才隔离NKI kernel（step1.24～4.28×）；resident对warm standalone的1.49～3.35×大部是省process/weight load，不是attention新算法。**Wan resident1245s反慢于standalone974s**，因常驻权重挤掉device VAE改host decode（约520s vs126s）。NxDI在FLUX step271ms与本法270ms基本相同，E2E差来自loader。
- 可行性/质量：Wan81帧SDPA超5M指令；Ulysses额外DMA rings只差43MiB导致load失败，TP2相关program在124GiB host编译OOM。cache同call数对fewer-step保真更好，但PSNR/LPIPS只对本模型uncached基准、16prompt（Wan5）；并非全任务质量评估。back-to-back芯片节流25～30%，测量前idle90s；Wan cache-off更受节流，超skip理论上限不全归cache。resident request仅3/5次，standalone/compile单次。
- owner建议 `INFER-TENSORRT-LLM`（Ch49）：补编译产物固定shape与host动态状态的边界，并把padding/replicated text归一化、device/host编译内存及resident component capacity列为执行计划有效性条件。多模态采样原理仍由Ch24拥有。

### 6.3 [22863 Understanding KV Residency](https://arxiv.org/pdf/2610.22863v1)

- 实读：`systems_assets/pdf_22863.extracted.txt` 原页1～2、6～7、12～20（§2.3、§4～5.7），含观测/估算/replay分界；评分 **3+2+2=7**，深入完成，需 Books 判断。未实读/复现未公开production trace。
- 实测是四个M365 workload 2026-06末～08初窗口的调用/缓存token/时间/部署字段；Code是event而非call，排除其byte/placement分析。把所有model投到Llama-2-70B geometry（80层/8KVheads/128dim/fp16，327680B/token）只是统一估算，**501.8TB不是实际GPU HBM部署**。所有session first-to-last、lifetime peak常驻且全region逻辑池的故意悲观ceiling；current-context busiest-hour47.0TB是另一分母。
- 同日多调用间state长时间idle，简单“全live都留”不是合理默认：Research完整trace一小时idle cap令ceiling501.8→140.8TB、重建4.07%→4.53%；这个收益和10%预算实验不同，不混算。10%47TB的pooled replay上LRU62.9%、FNU31.1%、int4 MRR13.6%；MRR保持同LRU victim序降低precision而非销毁，以容量换hit，不是胜过Belady等大小对象最优定理。**2%预算FNU67.60%反优MRR72.92%**；加入quant metadata后MRR14.99～19.25%，非固定13.6%。
- 关键未计：int4对agent长程质量、promotion/dequant/transfer latency均未测且被视作fp16 hit；host-tier流量可达1026.1TB/hour=285GB/s，不能说offload免费。预算跨replica pooled，实际per-replica碎片/路由可能更差，FNU对可变size对象也只是clairvoyant heuristic。
- deployment locality另加不可由eviction修掉的floor：同一176007call、cache key从session扩为(session,deployment)，无限内存first-touch5.4%→20.2%。观测89%→29%reuse与placement连续性相关，不是routing干预因果；Chat受composition混杂，部署ID不暴露worker细节。migration/affinity/接口仅研究方向，trace generator是planned release，不声称公开实现已核。
- owner建议 `INFER-GPU-MEMORY`（Ch54）：新增“跨调用state residency由liveness/precision/placement共同约束，call内paging不足”的命题与replay边界；Ch55只交接routing/跨deployment可用性，避免把Agent语义memory与KV副本混同。

### 6.4 [22890 MailRail](https://arxiv.org/html/2610.22890v1)

- 实读：`systems_assets/html_22890.visible.txt` §III～V-E，尤其§IV-C信用池、§V-B截断口径及§V-D trace不含compute；评分 **2+2+2=6**，标准完成。
- 增量：当receiver buffer/rank数小于1 slot，固定rank-pair信用会使活跃sender缺额；把credit accounting移到node-pair shared pool，让同node活跃rank使用其它rank释放的quota，减少receiver跨rank重分配往返。credit仍绑定真实receive slots；buffer reserve失败产生backpressure，send延迟队列受send pool上限，用户必须poll receive才能进展、无独立quiescence保证。独立MPI communicator承载credit return，node计数128B padding防false sharing；不是仅加更大buffer。
- 主实验Dane CPU集群，2×56-core Xeon8480+、OPA/PSM2、OpenMPI4.1.2/GCC10.3.1，通常64rank/node、4KiB datagram，rank8credit/pair vs node512credit/pair，credit half-used时返还。**不是GPU/RDMA/MoE端到端训练实测**。synthetic incast无compute，YGM Reddit/triangle仅通信trace replay；Lynx OPX补实验只测rank flow control，不能用于证明node池跨fabric收益。
- 128MiB/rank高incast中无控制基线600s截断，goodput用received bytes/time而controlled用完整完成含tail；1132×是在4096:1这一不同统计但作者认为保守的比较，不当一般MoE速度。12.8MiB/rank完整runtime的另一实验可到4431×，不合并两个数字。uniform histogram50trial、首个warmup去掉，node overhead−6.7%～+4.8%；node并非各负载必优rank。
- 证实node池在这些通信模型中更有效利用credit且降低control traffic；未证明GPU kernel融合、训练quality、lossless fabric全栈deadlock-freedom或任意rank skew下的吞吐保证。可复用的是“信用所有权粒度须与共享capacity、rank密度相容”，不是free credit通用安全定理。
- owner建议 **`TRAIN-DISTRIBUTED-TRAINING`（Ch36）**。初稿`TRAIN-COMMUNICATION`不是ROADMAP Stable ID，本轮已修正。把信用粒度/进展条件放collective/dispatch通信约束处，保留尚无MoE实证边界。

### 6.5 [22769 One Communicator, Three Vendors](https://arxiv.org/pdf/2610.22769v1)

- 实读：`systems_assets/pdf_22769.extracted.txt` 原页1、11～17（§7 correction、§8 launch geometry/MI100 floor及其tuned解释、§9 split），同时定点原页7～8的linear prediction/计时定义。评分 **3+2+2=7**；纠错强制深入，已完成受影响条件，未全面比较旧稿/所有新实验。
- 受影响原判断：companion eight-rank A100+CPU run声称A100 local13.54ms、Gatherv22.3ms及相对linear8.1×。本稿Table4保持rerun kernel hash/torch2.8/Triton3.4/mpi4py4.1.2，原job没kernel hash及GPU sampler，故不能声称精确重建原故障占比。same script rerun A采到**1GPU/4PID**、10.51ms compute；B排除default transport后4GPU2.33ms/2.5～2.9ms Gatherv；C显式pre-Python绑定4GPU但default transport仍13.9ms Gatherv。两个独立混杂：GPU sharing和transport，不能只修device binding就认为communication benchmark有效。
- CUDA可能在MPI_Init先初始化导致后设CUDA_VISIBLE_DEVICES无效只是作者**未证实机制假设**，未定位哪个MPI component。clock解释也弱（1s采样常在work结束后）；C及B-rank0的2.97ms未完全解释。CPU6.3～6.9ms floor在各组保留，不因A100纠错一并撤销。
- 原异构实跑条件N=8192、D=64、B×H=2；A100/MI100为fp32、CPU为fp64。local compute与barrier后Gatherv分开计时，后者不包含等最慢rank的barrier等待；初次9rank约6.8s wall time受编译主导，不能当steady-state异构attention时间。
- 新边界：w∝1/t仅在time与rows线性才适合minmax split。A100 B×H×ceil(r/64)、108SM预测波次，20repetition扫描128～3456row平坦，3520/6976阶跃验证，非“每调用overhead”。MI100旧6row约600ms floor主要来自key loop；加大tile并未验证latency-chain猜想，worker10→64及key chunk并行才大降。tuned6row14.6ms、8192row574ms，**95×A100只适用于8192row此kernel/config**，不能作为vendor普遍性能。
- tuned kernel全输出对reference≤5e−8；但tuned异构ensemble **未重跑**，minmax/1t新split收益为computed非measured。最优split仍可给某device零row，是当前kernel时延floor与目标 makespan的结论，不是排除异构资源的普遍规则。CPU/MI100共享并发、通信run variation仍存在，不能把单次comm时间当可靠常量。
- owner建议 `TRAIN-DISTRIBUTED-TRAINING`（Ch36）：纠正“rate-based异构切分天然负载均衡”的适用条件，用rank→physical UUID/PID绑定、timer/barrier定义与transport为实测前提，再引入tile/wave/floor下非线性minmax。若书稿存在依赖旧8.1×结论须定点纠正；不能由本稿替代整套异构训练结果。

### 6.6 [22731 Accelerated Dataflow](https://arxiv.org/html/2610.22731v1)

- 实读：`systems_assets/html_22731.visible.txt` §2.3～5.1.3、§7 discussion/open challenges；评分 **2+2+2=6**，标准完成。
- streaming key是exactly-once最小不可随意并行单位；用户system-prompt/category分组提高KV局部性，但hot-key sharding必然牺牲局部性换parallelism。engine可自行batch，不等worker可按GPU利用率扩缩：VRAM预分配、num_requests_running上升不代表完成capacity。worker报告完成速率、并发和trailing30min P90来估计容量，backend再按active/dispatchable key及backlog knob扩缩；依赖keys合理sharding与分布近似均匀，不是任意skew稳定证明。
- CPU/GPU pool独立max、允许CPU端预处理准备GPU batch，read以memory threshold backpressure停止；long startup、stockout、failover和IPC零拷贝仍open。不能从AsyncDoFn描述就声称exactly-once故障注入已验证。
- 对照Qwen2.5-7B-Instruct-AWQ/vLLM，OpenOrca/Dolly，prefix消融固定Dataflow8×A100/12vCPU84GB worker；Dolly hit约50→80%，低load grouping反增延迟；图吞吐/延迟由BigQuery rows与Little定律估算，非全真实端到端tail。autoscale100max T4/4vCPU30GB、max input512/output64/context4096、2h sinusoid，51.1%GPU-hour reduction的heterogeneous实验tail反而较高，不将所有改善并写。GPU-only独立autoscale实验42.4%GPU-hours及71%peak latency更正面。
- Flink比较保留其target-util0.7、16slot/4core、默认downscale1h；25vs峰值100GPU、582vs3804s peak queueing属于该配置+prefix/scaling组合，不是证明框架本质75%更省。未给更多seed/uncertainty、混合长输出/多model/任意key skew生产SLO。
- owner建议 `INFER-SCHEDULING`（Ch56）：补“外层stream scheduler应消费内层engine完成capacity而非预分配利用率；key locality与sharding需同时约束”的设计选择。Ch63只交接heterogeneous池，避免把一般ETL功能纳入长期主线。

### 6.7 [23503 HBFSim](https://arxiv.org/html/2610.23503v1)

- 实读：`systems_assets/html_23503.visible.txt` §3.1～3.5、§4.1/4.3/4.4、§5 limitations；评分 **2+2+2=6**，标准完成。采用“mutable KV写入flash引入耐久与layout约束”，不把模拟吞吐当实硬件结论。
- 闭环frontend再生成weight/KV访问、scheduler收到memory time后改变batch；policy显式分running KV/weights/retained prefixes，host FTL的表和GC占HBM，read/program/erase在同timeline，优于单bandwidth容量模型的具体增量。page/extents可保持plane并行、block映射把256page压同plane可令decode4.2～4.3×慢，故地址粒度与并行度不能混为一谈。
- 校准仅现成A100/H200 operator和pinned-memory copies、scheduler对vLLM0.26的282batch一致；64held-out layer平均误差5.8%/5.0%，最大41.8%；全request batch平均10.2%/5.8%。HBM4/HBF **无硬件校准**，30参数组18个assumed，4μs read/75μs program、16plane、100k P/E均不是产品已验证值。
- case为单accelerator8stack（HBM48GiB/2TBps与HBF512GiB/1.5TBps），H200 compute延伸到>16batch。Llama3.1-70B8bit weights/BF16KV、Qwen3-235B-A22B FP8/BF16KV；后者route是uniform seeded synthetic非production。3种输入输出、代表batch32；大多只一decode step/每sequence7tokens及prefill window，latency case不含GC干扰，不是长时间serving/TP/PP实测。
- HBM-first runningKV、HBF-readmostly weights在超容量cyclic scan下优于LRU/FIFO，因为后者每step重填几乎全working set；不能外推所有cache策略不如placement。write-back-on-eviction比eager drain减少1.2～1.6×写、性能within1.5%，支持“短命KV不要提前刷flash”。estimated24～83months绑定借自Llama3.3-70B published489outputtok/s、5000/500input-output、24×7、100kP/E与perfectwear；Qwen亦借同token rate，绝非实际寿命保修。
- owner建议 `INFER-GPU-MEMORY`（Ch54）：把capacity tier选择扩展到data mutability/flash write amplification/endurance与plane并行；保留只有公开假设simulator支持的条件，不纳模拟speedup为生产硬件事实。

### 6.8 [22877 BS-Spec](https://arxiv.org/html/2610.22877v1)

- 实读：`systems_assets/html_22877.visible.txt` §III-A～D、§IV、§V-A/B/D及TableIII～VII；评分 **2+2+2=6**，标准完成。
- 同一BFP shared-exponent/bit-plane-major target存储，draft只读weight/KV高位，分别按batch/context权重作precision pair离线calibration/运行时PLT查询；没有独立draft权重副本，不代表零临时draftKV。key按channel group需未满group临时buffer，value按token；accepted token才进入persistent state。低bit节省要有选择性bit-plane内存与LUT bit-serial datapath配合，不可直接推为普通GPU收益。
- 3B/8B/14B在HumanEval/GSM8K/MBPP acceptance用于γ5～8选择γ7；target实际压成BFP9 weights/KV、activationBF16。spec验证保持的是这个target而非原BF16 exact distribution；GSM8K BF16→BFP9：77.7→77.8、84.5→85.5、91.4→91.0%，仅此不证明泛任务无损/统计显著。
- 28nm333MHz synthesis/DesignWare+CACTI SRAM+Ramulator2 HBM2 trace-cycle模型，非tapeout/实GPU E2E；QuantSpec本是GPU kernel，被作者映射到自制multiprecision systolic baseline，SPEQ也同memory hierarchy，area各异。1.62～1.92×等是modeled effective throughput对BF16 systolic AR，含target compression+SD+新datapath，不称现有GPU直接1.9×。作者有BFP16/BFP9/FIGLUT与分组件消融，但没有production arrival/concurrency/SLO。
- owner建议 `INFER-SPECULATIVE-DECODING`（Ch48）：补“共享draft存储的收益条件要一起固定target表示、bit-plane可取性、draft W/KV precision及hardware执行”，不要把一般quant-spec memory ratio原则算成该paper原创；Ch49仅交接BFP执行表示。

### 6.9 [22579 MemLLM](https://arxiv.org/html/2610.22579v1)

- 实读：`systems_assets/html_22579.visible.txt` §IV～V-A、V-D/E、VI-A～C与VII，另核§II-C selective recomputation定义；评分 **2+2+2=6**，因核心渐近宣传有直接反证，实际加深而不降分缩池。Source有限机制完成，**O(1)与部署完整性主张不采用/保争议**。
- 采用：precomputed文档KV的cross-document缺失按CacheBlend约15%token重算，host做projection/FFN、SSD做全attention；把recompute-target与query行合成Q_fused、按jagged mask保持因果、同一NAND pass处理，per-channel Elastic-SIMD和SRAM online-softmax merge消除反复搬完整KV及内部DRAM partial-reduction traffic。原precomputedKV不改，query-specific KV out-of-place追加；不是重新发明CacheBlend或exact全prefill等价。
- 必须收窄：§IV-B写Q_fused包含约15%N HKVD targets，还需host-recomputed KV subset及O_fused传输；首layerKV还要读回host。**固定重算比例ρ下这些至少随ρN增长，故本文“整个attention PCIe O(1)、与context length完全无关”的宣传由所述数据流不能推出**。1MB SRAM能容某evaluated shape/tiling，不证明任意N constant total bytes。只采用“不重复传全部全层KV，且融合减少重读”的局部IO结果；不写近零PCIe普遍结论。
- 证据：16nmFPGA prototype提cycle/power（不是完整SSD）、Jetson OrinNX16GB实测host kernel/PCIe，再SimpleSSD整合；可用memory人为限8GB。FP16 OPT/SmolLM2六model、8RAG数据、default top5/15%recompute。mean4.06×vs GPU-FullCompute、4.18×vs GPU-PreCompute属于该simulation stack；ablation1.80×base、再1.11×fusion/1.82×perchannel/1.12×SRAM依序。TriviaQA accuracy/F1差<0.3%与浮点重排相符，但不是所有数据准确性或已量化uncertainty证明。长answer和KV fully memory-resident会缩小收益，iterative retrieval须chunk先最终确定。
- 部署另有内部未核链路：TableIII Linux5.15，§VII又称所用io_uring NVMe passthrough需Linux5.19；V-E描述dma-buf kernel driver和custom vendor command，但§VII说不需kernel modification。可选代码未实核，不将GPUDirect/PyTorch端到端成品视已验证。若要采用“无需kernel改动/全零拷贝可部署”，需准确kernel/module、command path与真实device trace。
- owner建议 `INFER-GPU-MEMORY`（Ch54）：只整合“KV不只可offload字节，必要attention可下推，但要保重算/因果/总IO账本”的机制及上述ρN反证。Claim O(1)不入书；不因该反证删除其实际fusion/dataflow增量。

### 6.10 [23767 TileDRAM](https://arxiv.org/html/2610.23767v1)

- 实读：`systems_assets/html_23767.visible.txt` §3～5核心、§6全部、§8、仅为适用条件读AppendixA.8；评分 **2+2+2=6**，标准完成，未遍历其余附录推导。
- 新控制变量：保留controller address mapping，把tile→domain/row/column的GF(2) layout暴露给compiler。tile signature包含shape/stage/warp、operand/stride/dtype和**有序**访问；source-order前驱差是否落row-reuse kernel决定intrinsic row-hit，用有限catalog/greedy找布局，经injectivity/alignment/aperture/legal binding约束后PLAN–BIND–APPLY降为普通shift/mask/XOR地址。不是新ISA，也不是对任意layout全局最优证明，形式subspace-selection借自Rotaru而非本篇原创。
- 适用条件A.8：序列在admitted tile instances中复现、请求形成/事件顺序保持，live coordinate可injective线性表示，mapping在live image上满足affine/rank/byte-offset条件。source-order优化不是FR-FCFS实际服务顺序定理；实际性能必须由controller replay检查。
- 108MoEFFN GEMM trace在oneCU+paired3DDRAM stack Accel-Sim/Ramulator2，baseline/final固定logical trace、organization、closed-row初态和refresh/precharge，仅变placement；8tier16bank/OpenRow/FR-FCFS。75.7→15.2%pooled row conflict，1.77×geomean只属这些replay；6trace×6organization的2.20×另集合，不并计。没有整模型端到端inference、更无实3DDRAM吞吐。
- RTX3090只测地址生成额外0.17%geomean、P95 0.57%/max4.93%；不是实3090有同样1.77×收益。offline synthesis median349s/227MB，需signature复用摊销。general attention/convolution、跨CU协调和physical3D验证都是future work。
- owner建议 `INFER-TENSORRT-LLM`（Ch49）：补“compute layout之外，物理memory placement也可编译，但必须绑定可复用有序signature与目标mapping契约”，并标明trace simulation与地址开销实测不同验证层。

### 6.11 [23086 PairSight](https://arxiv.org/html/2610.23086v1)

- 实读：`systems_assets/html_23086.visible.txt` §II～IV全部，含TableI/II与co-runner/feature消融；评分 **2+1+2=5**，标准完成。增量是双operator交互证据与预测输入条件，非“sharedmemory有干扰”这一成熟原则。
- libsmctrl按TPC pair mask隔离SM，register/sharedmem/L1/warp scheduler分开，但L2/DRAM/interconnect共享。T_share(p,q)/T_solo(p)的分母固定相同SM数，才隔离“少SM”与“并置额外慢”。compute/memory二分类不能描述同类operator方向性/目标差异；固定目标SM时变co-runner仍可变慢，需要两侧operator级连续信息。
- 730k sample、52k experiment、每设定30run，按experiment80/10/10分train/val/test；6model ResNet50/101/MobileNetV2/BERT/Llama3.2-1B/3B，A100-SXM4-40GB。4.3%HP MAPE是全体测试，**Llama subset10.3%**，并非所有LLM4.3%。co-runner token去除HP4.3→7.7%、LP2.4→6.7%；换peroperator compute/memory连续util仍4.3%，故不能声称“只有memory-path counters才可预测”或专用nonlinear tree唯一有效（MLP亦4.3%）。
- unseen Llama完全不适应时HP30.2%、100new experiment/pair continuedtrain后13.5%，All9.1%；不是开箱泛化4.3%。输入仍需新model counters及各TPC latency profile；query5.3μs是16CPUcore批1k amortized，不是单次scheduler walltime。最长window composition16op→24～96op另400experiment/80asymmetric支持有限近似，无实际scheduler SLO收益/大于2任务、多GPU/MIG隔离保证。
- owner建议 `PLATFORM-GPU-SCHEDULER`（Ch63）：把SM资源分区和memory-path干扰预测分开，说明“同一SM份额、双方operator连续状态、profile/适应成本”的有效性条件；部署调度收益仍未实证。

首11下一步：root独立核以上关键段/评分与反证，再逐项比较现有owner具体论点作Books处置。本slice未写Books、Report、Learning State；未stage/commit/push。

## 7. RO 七项必要 Source 实读（2026-10-20 恢复轮）

本节仅本 agent 被分配的七项；23378/23372/22576/23566由root处理，不重复。每项精确版本 `2610.<ID>v1`，HTML原件与可读提取在 `systems_assets/html_<ID>.raw.html` / `.visible.txt`。窗口资格仍取§1官方Oct19公告段，不把v1页上的提交日期当首次公开日。

### 7.1 [23615 HIJP](https://arxiv.org/html/2610.23615v1)

- 实读§3、4.1～4.6、6及定点A.3（CEM配置/计时口径）；评分 **2+2+2=6**，标准必要Source完成。不是首次提出hindsight或inverse dynamics；新增是goal端梯度与预测动作→forward model组合训练及其对照。
- 随机anchor和未来offset，把同一已执行即时动作配不同未来goal；inverse MAE的梯度流经current和goal encoder，不只训练head。把预测动作送入forward predictor，MSE对齐**下一步**stop-gradient latent（不是远goal），直接约束推理时递归使用的inverse→predictor组合。predictor还受真实动作transition loss与SIGReg正则训练，不能把组合一致性视作独立防collapse办法。
- ViT-Tiny从零训、context3，H=5个model step、每步含5环境动作，一次执行25环境步再观测。四模拟任务TwoRoom/Reacher/PushT/OGCube，LeWM公开offline数据；同起终点、每task-tier50episode，K10/25/50/75与budget25/50/100/100。原生sim success而非latent距离阈值；overall86.8% vs INTACT81.9%，但Reacher均值81.5%低于INTACT85.0%，TwoRoom99.5%低于GCBC100%，不写各任务均胜。
- 关键消融在另12组合（不含near100%TwoRoom）full82.5%；endpoint-only71.7、goal stopgrad78.5、无consistency76.0、禁止consistency更新predictor78.3、同表征换CEM69.3。支持具体训练/推理链，非普遍inverse一定优search。速度1.9～16.5×是RTX4090、50episode单vectorized batch、matched replanning calls、CEM300candidate×30iteration×H5；不是单机器人控制频率或对所有预算最优search的比较。
- 已证明局部数据/固定horizon上质量与计算选择可改；未证明长程组合、adaptive horizon、OOD多峰未来goal下单动作监督唯一性或真机实时安全。owner建议 **`MULTIMODAL-WORLD-MODELS`（Ch25）**：补“训练只拟合action和forward各自正确，不确保二者组合在imagined rollout正确”；Ch26仅交接25步open-loop执行与反馈周期约束。

### 7.2 [23334 LAW](https://arxiv.org/html/2610.23334v1)

- 实读§3.1、3.4～3.5、4.1、§5.5，定点Algorithm1、real数据B.2及completion标签定义（附录C）；MoTE细节仅作上下文、不采用其全部性能归因。评分 **2+2+2=6**，标准完成。采用的是subtask-local value的独立实验，不以统一language/action/world名字准入。
- episode失败不应令此前已完成subtask全取零。各成功subtask终止动作reward1，其余0；chunk在首次semantic boundary截断，之后动作mask；只有同subtask存在下一recorded chunk且未terminal才bootstrap。最终failed subtask不添positive、未执行subtask不作样本。101bin categorical critic/HL-Gauss、γ.99/EMAτ.005；不向未来subtaskbootstrap，因此估计的是**当前局部目标**，不是episode最终成功概率。
- 先训planner/state及独立WAM，再冻结后训value adapter；Qwen3-VL-2B frozen backbone，LoRA planner/state64、value128。value仅recorded chunks，不含WAM sampled候选；sim failure占样本25%，从成功演示回放注入missed grasp/early release/placement等task-specific扰动后人工语义过滤。real每task300trajectory、共900，保留成功与失败并人工标semantic boundaries；不是无标注自动发掘subtask reward。
- §5.5专门五个多subtask RoboTwin任务、clean/rand：no value88.20%、episode-supervision87.90%、local90.80%，故episodecritic不保证比无critic好。该局部对照支持保留失败prefix正监督，但**未单独隔离“多了prefix正样本”与“semantic truncation/不同target”各自因果**，未做所有50task或全部真机的value独立对照。不把整框架94.21%或65%真机全部归value。
- WAM每次32候选、3denoise，value保top8/T1，position/gripper加权、quaternion Markley平均；并非已验证fusion候选始终可执行。completion异步携timestamp+subtask instance，丢旧结果避免错推进，但无严格deadline/误判安全保证。completion label借人工区间内累积motion进度≥.995，不是物理成功通用判据。
- owner建议 **`MULTIMODAL-EMBODIED-VLA`（Ch26）**：semantic boundary同时改变credit assignment和控制状态推进，补失败episode中的成功prefix不应被终局标签抹掉及人工边界/候选分布外推限制；训练RL章节只交接成熟TD形式、不重复owner。

### 7.3 [23156 ORD-WM](https://arxiv.org/html/2610.23156v1)

- 实读§3.1～3.4、4.1～4.4、6，定点B trajectory split；评分 **2+2+2=6**，标准完成。
- SAM3 masks+多view RGB-D回投/合并object pointcloud，中心平移与SO(3)-equivariant VN geometry latent分开；预测每object SE(3)，直接旋转每个3D latent vector并更新center，fixed object不动。保形来自限制变化族为刚体，不是学到守恒律。和每步自由预测latent相比，防止shape漂移；和普通latent先变换pointcloud再encode相比，省每rollout重编码。Decoupled Geo.+Pose也保形且更快，但预测误差较高，作者以reference-frame ambiguity解释，**未证成唯一原因或不能修正canonical frame**。
- LIBERO四suite40task+1000push trajectories，object assets LIBERO/RoboCasa；trajectory级90/10避免同trajectory相邻transition泄漏。Table2 avg约170step，full surfaceCD4.729mm vs自由VN预测131.600；shapeCD0是构造保证（数值<.05mm），不可当独立物理预测成功。B1/B8 rollout784/6179FPS是latent model吞吐，不含每实际控制观测的SAM/depth/encode代价。
- 真机Franka Research3/三校准D435、FoundationStereo depth；pushing每candidate8step，RTX3090每MPC重规划55.4/115.7/269.9ms（64/256/1024candidate），成功定义final位置<2cm，对应10/70/90%。不将小规模budget曲线变成全任务90%，正文此表未给trial总数，不能补造置信区间。
- 明确限制：floating/fixed rigid、低动态position control，不支持hinged/articulated/deformable；mass/friction/contact隐含于数据，未观测物理参数相同外观不能区分；SE(3)不约束nonpenetration/contact。owner建议 **`MULTIMODAL-WORLD-MODELS`（Ch25）**：状态变化族先验既可阻止错误漂移，也会排除真实形变；保形与动力学/接触正确性要拆开，Ch26只接MPC观测计算时延。

### 7.4 [23018 VLA-Fabric](https://arxiv.org/html/2610.23018v1)

- 实读§3～7，定点实验设计与fixed-weight removal定义；评分 **2+2+2=6**，标准完成。保留local完整policy/action ownership，而非把multi-arm总action维度随团队统一放大。
- shared semantic/Common、peer latent K/V供local query、action intent三处接口；SingleVLA最终readout线性融合，π0.5改成prefix融合、peer prefix KV与denoise中gated residual peer attention。三种功能可重实例化，不是所有架构必须交换同tensor。两个task32run架构探索，200dev选checkpoint+200disjoint paired eval；Common-first优于从头全开，AVG/RAW及Linear/Transformer无一致全胜，选RAW+KV+Linear是简洁可复用选择，不是已证最优通信图。
- Independent是无交互train+test；All-off是已训Full推理时移除，后者有分布移位，不能将下降全解释为交互不可替代。same roles跨Eagle2/π0.5支持接口转植，未证明混合异构policy直接互通。
- 三/四臂模拟：Stack3 independent90.5→Full91.0（分解任务近无收益）；Frame3 67.5→79.5、Frame4 9.5→89.5；Arch4 0→5仍远不可靠。物理四task每task50demonstration、每setting25trial，Basket3 72→88、Relay3 16→56、Relay4 40→72、Frame4 36→60。随共同对象/交接时序耦合收益变大，不以arm数代替依赖强度。
- 当前homogeneous、fixed-role≤4arms、静态图；无变动team/hardware网络延迟、跨policy表示时钟语义对齐、实际通信带宽/latency定量及碰撞安全保证。owner建议 **`MULTIMODAL-EMBODIED-VLA`（Ch26）**：团队action ownership与共享信息边界可分开，但接口必须对齐语义、生成阶段及反馈时序；不是通用multi-agent communication benchmark。

### 7.5 [22951 MambaAct](https://arxiv.org/html/2610.22951v1)

- 实读§III、IV-A1～3、IV-B、V；评分 **2+2+2=6**，标准完成。采用“prefix一次压缩→反复denoise仅轻量条件”的质量/资源选择，不把换Mamba当充分贡献。
- VLM prefix一次投影，44visual/16language分段pool+4learned global-query tokens再pool成条件vector；四block Mamba3 expert29.7M取代311.5M Transformer，每block FiLM scale/shift/gate跨10denoise复用，action/time每步仍重算。省重复prefix cross-attention，不声称压缩保留全部空间细节或Mamba状态跨真实policy query自动记忆。
- π0.5同初始checkpoint/full-model joint fine-tune30k step,batch16,H100 BF16；LIBERO3train seeds17/27/42，每task50trial/eval seed7，H10/denoise10/execute5。success96.72±.14→97.80±.43%；seed42 latency prefix40.76→46.61ms增加，denoise160.26→56.40ms，E2E228.6→107.6ms。不是全模块都快，其他论文speedup不同hardware/setting不可横排。
- 2×2 mixer/interface消融同context compressor：gated Mamba98.4 vs size-matched gatedTransformer85.7，cross-attn Mamba96.7 vsTransformer75.6，支持此recipe下压小expert选择；但gate专家30M vscrossattn17–18M，gate质量优势**不能纯归conditioning形式**。Transformer更快74.22ms但质量差，Mamba不是最低延迟唯一winner。
- LIBERO-Plus总79.7 vs78.7，但noise73.5<77.4。真机两UR5task，每task112demo/28ID+52OOD，real H50/execute30@30Hz/RTX5090；报告normalized success给中途成功0.5分，不能读成完整任务二元成功率。OOD tube76.9→82.7、nut86.5→95.2需带partial-credit口径；E2E含I/O/通信等，sim与真机不可混hardware。real仅空间shift，token pruning/denoise compression组合未测。
- owner建议 **`MULTIMODAL-EMBODIED-VLA`（Ch26）**：把一次感知条件构建与重复动作求解的成本分开，条件压缩/复用换质量是可调设计面；Ch24仅接flow求解重复性，不复制具体VLA资源选择。

### 7.6 [22556 RePlanMem](https://arxiv.org/html/2610.22556v1)

- 实读§3.1～3.7、4.1～4.3.4、5，定点B detector episode-level split；评分 **2+2+2=6**，标准完成。
- consecutive chunk按已经执行H步对齐相同未来K−H动作：上次final[H:K] vs此次pre-write[:K−H]；修订可能标记新观测重要，而不只应当抑制的动作噪声。10feature还含detached top-view feature差，故非纯action-only detector。差分/EMA/causal moments只用q前统计，Mahalanobis+per-task CDF共享percentile门槛；训练前5–10%warmup不写memory，inference统计冻结，首query无overlap signal。
- event≠write：W3历史window+FIFO内容complete-link δ.01聚类，选未被memory代表的新簇最新frame，一次可0/1/多写；robot mask仅相似度比较，存原图。实际写入后再跑policy；无写入免第二inference。distributedSFT仍整microbatch第二个可微final pass，prewrite/detector无梯度，不应声称训练完全按event节省同等compute。
- RQ2 19task OpenVLA-OFT/π0.5，K8,H1/4，每task-policy-regime50closedloopepisode，episode级70/10/20，XGBoost/CatBoost/LSTM **用sim phase labels监督**且val选F1阈值；ROC-AUC.981–.997是此detector实验，不能直接赋给不依赖keyframe标签的因果Mahalanobis部署规则。event_recall@1容许相邻query匹配，不是逐帧全对。
- RQ3 RememberColor cue写入/保留：95percentile阈值π<20%、OpenVLA0%，80percentile48/85%；加clustering OpenVLA50episode100%cue写入/保留，robot mask令336→169writes、186→19evictions，仍50/50保留。**100%是信息保留率，不是完成任务成功率或独立memory质量增益**。real仅recorded trajectory offline replay，无真机闭环任务成功提升证据。
- 长phase清楚的task才测；H4可漏短事件，渐变无峰；policy错误也会大修订，不等semantic事件识别。新task需新校准与阈值，无zero-shot普适保证，未给全runtime wallclock/latency预算。owner建议 **`MULTIMODAL-EMBODIED-VLA`（Ch26）**：memory-write signal、novelty selection、真正利用memory的控制收益是三层证据，支持前两层但不替第三层结论。

### 7.7 [22471 Has GPT-6-Astra Achieved Embodied Intelligence?](https://arxiv.org/html/2610.22471v1)

- 实读§2.1～2.4、3.1～3.2、4.1～4.3，定点§5.2～5.3的持续世界示例/benchmark边界；仅检索附录model interface识别，不遍历各benchmark全部表。评分 **3+2+2=7**，针对评价条件/实际控制边界深入完成，需Books判断。确切稿件v1，文中GPT-6-Astra label不是冻结服务snapshot；不同真机任务effort high/max，未核提供商实际路由/运行日志，不能写成独立复现。
- protocol不是零样本统一比较：weights固定，但训练demonstrations被预处理为task guidance、数值motion/visual references、executable helpers与recovery组成的frozen package；test不改package，各episode新session、不跨episode迁移。1×与10×固定init/config、后者同episode继续而非reset，state与不可逆后果保留；BEHAVIOR不扩10×、RoboLab没training故无ICL。ICL提升SIMPLE四common tasks70.8→90.8，是局部支持，不把package各组件因果逐项证实。
- 标准步预算外推到10×测的是额外交互/纠错可用性，不是相同时间/成本SOTA。LIBERO-Long++约1Mtoken/近1h，Ultra约9M/近2h，RoboDojo extended>3h平均；token含约98%cached input，“1M≈$1”仅作者粗估，不当现价。对额外预算仍失败的episode，任务不可逆/依赖和遗失已有progress构成真正边界，不能把“更多思考”作为必然修复。
- controlled RoboDojo harness：standalone baseline15.56%、VLA6.91%、openloop5.83%、closedloop23.61%/7.664Mtokens；review4动作25.83%/2.796M；ICL+closedloop54.17%/19.335M。说明closedloop验证与review粒度是质量/成本联选，不是hierarchy天然优；不同ICL组合review L2，不把混合配置全差只归memory。固定chunk4降至11.39%，adaptive20.00%/1.146M，非chunk越长越好。
- 真机8platform不用demonstration package但有human-written schemas/joint/camera/safety priors，某些task含grasp guidance/script；通常60minwallclock+emergency-stop人，human判实际结果，非自主安全证明。rigidpickplace17/18、plug0/11、mobile9/23不可混同同质任务率；cloth criterion跨platform不统一。G1约90%时间deliberation、单manipulation>1h，不能叫实时visuomotor。持续世界household示例会在推理期间继续动作/加热，stale observation、fridge300–765s未关、tap溢出等只证实失败模式；prototype不是已标准化/大样本验证的新benchmark。
- owner建议 **`MULTIMODAL-EMBODIED-VLA`（Ch26）**：评测必须显式绑定demonstration信息、恢复预算、world clock、验证/安全停止；控制反馈需要以实际contact/support/constraints验收，不由语言自述或最终单状态替代。Ch25仅交接持续世界与旧观察失效，不迁移整个评测。

## 8. 三个代表项：准入后必要 Source（2026-10-20 后续轮）

以下初稿拟排除均经正文定点推翻，先准入、后在本轮补齐有限必要Source并评分；旧定点结果与不确定性保留。原件同 `html_<ID>.raw.html`，均v1。没有复现、运行实现或扩展到companion论文。

### 8.1 [22716 CMM-MP](https://arxiv.org/html/2610.22716v1) — 准入

- 本轮实读补齐§III～IV必要接口、VI、VII-A～C、VIII，评分 **2+2+2=6**，标准完成。采用load/store暴露、device内翻译与coherence责任边界，不采用“industry-first”或通用TCO收益。

- 实读§II、III-A～C关键地址/transport语义、IV host接口、VII-B局部设备表。相对RDMA显式remote calls/host stack，device把CXL.mem普通load/store翻译为Ethernet pool请求，以Type3 NUMA暴露整个pool；PAMT 4Kentry、可配置1～64GB段。不是只把Valkey迁到大内存：**CPU可寻址capacity、设备内地址/可靠传输与软件共享一致性责任分离**是具体主线。
- §IV明确共享host access atomicity不含执行顺序，host cache/data coherency由上层out-of-band同步处理；不能宣传“全pool透明cache-coherent共享”。mpctl offline/online预定义memmap段，也不是应用无感任意字节动态扩缩。
- 设备Gen5x8/2×200Gbps/48GB，MLC本地530ns、remote无switch1911ns/有switch2725ns（NUMA0），五remote aggregate读23.1GB/s；RDMA64B read2.27/3.17µs与MLC load不是完全同API统计。初次定点待核的应用容量/NUMA放置控制、失败/共享同步及复现条件已按下文补核，不能凭这组数字宣称LLM收益。owner建议 **`INFER-GPU-MEMORY`（Ch54）**：memory tier的CPU可见性与共享一致性不能混同GPU HBM或GPU可直接访问；Ch63仅交接host资源池所有权。
- 补核对照：两Granite Rapids双socket主机（64/144core/socket、512/256GB DDR5），4standalone+2host-attached共6device/288GB、200Gbps switch/MTU9100，Ubuntu24.04/kernel6.8.0-101。MLC本地1device、remote5device bandwidth与64B RDMA/8MB bulk不等同端到端应用比较；cache/locality与software path均可能改变结果。GSAT24h无检出错误只支持该run，不证明传输拥塞、packet-loss/timeout、node故障或共享cache一致性全正确。
- Valkey value64～4096B、YCSB A–F只是本机/MP-L/MP-R比较；没有给逐run不确定性、Valkey版本、完整client concurrency/容量放置比例，不能泛化“remote仅30%开销”。DiskANN明确SIFT1M、单CPU core、所有memory经ramdisk、不同search-list L；MP-R约3×SSD是**ramdisk/SSD比较**，不是GPU RAG/LLM端到端。共享mode仅描述、未给跨host共享一致性/竞争压力实验。
- 已支持设备将network memory普通load/store化且额外network hop有代价，未支持动态细粒度任意分配（VIII列future）、GPU-direct/XPU互联（future）、故障迁移/应用无改动等于无系统配置/跨hostcoherence。后续若采用这些扩展须有新原始证据；有限命题不依赖这些未测部分，因此不作访问受阻。

### 8.2 [23072 ScaleRAN](https://arxiv.org/html/2610.23072v1) — 准入

- 本轮补读§IV-B～E、V-A/B公式与conformal校准、VI-A～E、VII，评分 **2+2+2=6**；因deadline保证/非抢占反例关系到安全约束，实际深入受影响层，有限Source完成。

- 实读§III、IV-A/D/E、VI-B/D/E；明确AI共置有实测，不再以RAN应用排除。预建Green Context profile ladder+MPS，共享控制块，worker每inference/LDPC iteration同步旧stream再切新profile；合作式边界，不是抢占正在执行kernel。
- DGX Spark48SM、11profile（RAN4～44步4）、cuPHY0.5ms deadline；VI-E真共置为ResNet18/152、3/10/40层MLP宽1024/2048，**LLM只有Fig2单workload SM-scaling，不是LLM共置SLO实证**。ResNet152E2E6.39ms仍近ResNet18deadline率，wide40layerMLP更坏；反证“推理总时延长就必然干扰”——kernel相对slot持续时间与SM footprint共同决定换profile可用性。
- proactive conformalP99 deadline99.96%、SM regret4.80 vs比例控制99.95%/8.69支持特定trace配置，但未由此得到硬实时保证；初500slot校准、余9500eval×8trace。初次定点待核的profile切换timer、nonpreemptive tail、漂移/quantile覆盖及capacity/AI吞吐已按下文核实或限定为未证明。owner建议 **`PLATFORM-GPU-SCHEDULER`（Ch63）**，不是RAN知识专章。
- 校准/计时补核：train105trace×3000slot×11profile=3,465,000samples；eval8个新trace各先500slot校准后9500slot。LDPC35iteration且禁early termination，CPU从launch到slotcomplete计时含runtime/sync，不等全部RAN链路/最终无线deadline。GBDT lleaves60µs为batched predictor成本，未给精确batch/每次完整profile切换tail；不把60µs视作全autoscaler最坏时延。
- Eq13把disjoint train/cal/test的split-conformal coverage表述成保证，但未证明时序traffic exchangeability、共置干扰分布稳定、或基于预测反复选择profile后的conditional deadline率；**本文评阅推断：边际residual覆盖不自动成为adaptive policy的硬SLO**。正文VI-E也直接给wide MLP时deadline下降，构成“SM分区即deadline隔离”的反例；本轮有限采用该反例，不将GC当MIG式memory隔离。
- 额外边界：实际library每inference/LDPC iteration才同步旧stream，正文泛称kernel launch boundaries不是已实现任意kernel抢占；IV-E明确逐kernel透明拦截仍future。one RAN+one AI、只SM不分memory、公开代码仍considering；相同SM下wide/longkernel与内存带宽效应未完全因果隔离。支持“资源分配计划必须服从正在运行任务的交还边界”，不支持任意AI模型0.5ms可保证切换。

### 8.3 [22520 Soft Errors](https://arxiv.org/html/2610.22520v1) — 准入

- 本轮补核§3.1/3.2的位注错定义、§4完整evaluation、§5.1～5.4/§6；评分 **2+2+2=6**；因silent corruption诊断/可靠性边界实际深入受影响层，有限Source完成。采用故障表型与组件/任务条件，不采用真实硬件发生率、安全保证或“首次”宣传。

- 实读§3～5核心（不遍历引用）：LLMEI以tensor位重解释+bitwise mask改参数，AIME2024三DS-R1-distill及LiveCodeBench多个coder/Llama；BER10^-12～10^-4、每配置10trial/pass@1，4×A80080GB+3×A600048GB。实际新增是低BER下输出可语法通顺但逻辑损坏，高BER才易token崩溃，以及task/component故障表型不同，不能仅靠garbled output识别硬件错。
- §5代码task约10^-9后corrupted outputs转token category I，数学task过渡较缓；注意这是**受损输出类型分母**，不是全输出100%损坏阈值。self_attn/mlp更早锐降、embedding相对保留，但同BER不同组件参数/bit数不同，不能推出等注错数下纯组件因果或部署中ECC优先级最优。
- 仅软件参数注错，未测真实SRAM时空分布、瞬态activation持续时间、ECC后现场错误概率；原文“首次soft error导致hallucination”不采用，已有相关fault研究不能被静默抹去。初次定点待核的bit位/dtype/注错粒度、baseline及taxonomy/uncertainty已按下文补核披露不足；BER→设备时间风险不可直接转换。owner建议 **`PLATFORM-PRODUCTION`（Ch73）**：silent numerical corruption可先表现为仍通顺但错误的输出，生产验收不能仅监控NaN/崩溃；Ch67只交接可观测性，不新设hallucination硬件章。
- 补核发现的未披露项必须保留：float32/int32只作为§3.2实现例子，所有被测checkpoint实际dtype/quant、具体bit位分布、注错后持续范围、prompt/输出token上限、每model精确benchmark版本/题数、taxonomy标注员/自动规则及一致性均未充分给出。正文code deterministic/few-shot、math identical prompts/settings是声明，不补造实际配置。10trial仅报平均pass@1，未给confidence/variance，3,200GPU小时不是归因可靠性的替代。
- 数学与代码用不同model集合，因此“代码比数学更易崩溃”的观察混有task/model confounding；同BER不同size/matrix参数量不同，总翻转数不同；也未把无fault已有logical error与新增logical corruption做可复查paired分类混淆表。故不能据本稿证明一个新输出错误必由硬件造成、embedding保护无用、或某BER就是生产崩溃阈值。
- 实际可采有限结论：受控bit扰动能在语言仍有效时改变任务正确性，输出错误类型随注错强度/model/component条件改变；故“语法/崩溃监测通过”不足以排除数值损坏。具体检测/重试/冗余/ECC策略的灵敏度、故障定位与成本尚未实证，不能把taxonomy当已部署诊断器。未披露部分是未证明边界，不删除候选，也不假称可访问的正文受阻。

## 9. 另九个 AB 准入家族：有限必要 Source

本节沿用 root 已完成的题摘准入，不重新扩池。精确版本原件统一 `systems_assets/html_<ID>.raw.html`，可读提取 `.visible.txt`；下列实际读段才算本轮 Source。评分顺序同合同（Design Delta/System Reach/Durability），独立复核及 Books 处置仍归 root。

### 9.1 [23056 Thought Blocks](https://arxiv.org/html/2610.23056v1)

- **2+2+2=6，标准必要 Source 完成。** 实读§3.1～3.4、4.1/4.2正文、4.3～4.5、5；为核确切teacher target和速度/内存口径，定点读B.1.2/B.1.3、B.4，不遍历全部模板或附表。
- 旧 latent communication 虽免文本，却仍先执行 latent rollout 才有可传KV；本文分开“传什么”和“如何生成”。R是prefill边界每层hidden，C是Activation Beacon压缩prefix KV；B个learned slots cross-attend R生成embedding，再带C经过一次**causal frozen-backbone rendering**得到每层KV。不是零计算、不带prefix、也不是把所有block positions做无依赖并行解码；一次forward仍有causal attention。
- 训练teacher从相同(R,C)做latent AR，固定hidden→input对齐，decode-stage Beacons抽出B个KV位置；writer用KV平方误差+hidden辅助loss，backbone/Beacon固定。B=4、ratio2；标准teacher horizon最多12、larger-slot试验96。78,207 synthetic/benchmark train examples，作者声明不用test traces；跨任务/新backbone泛化不由此证明。
- 同backbone/roles/agents，Latent-MAS是隔离构造差异的关键对照；四agent下12→3communication passes，平均E2E2.5×、accuracy -0.72pp，是有限accuracy/latency选择，不是推理链等价定理。Zero/Random E将11配置平均79.64降73.44/71.06，R-only61.28、C-only67.16，支持内容与addressable-prefix的联合贡献，不能仅凭多几个latent slots解释。
- B4→32 accuracy类别macro81.12→82.59但KV随B增加；不要将该macro与ablation全配置平均79.64混成同一统计口径。所谓KV-load是**tensor形状×element-size解析估算**，非profiler测得HBM/PCIe流量；8.35MB平均、比latent85.7%下降只在该代理口径成立。
- latency是单visible RTX A6000 48GB、batch1，host wallclock前后CUDA同步，含prompt/tokenization/prefill/state-transfer/finaldecode；不是跨机器网络/吞吐/在线P99。offlineBeacon/teacher/writer训练仍有成本。只证共享backbone顺序链和既定QA/reasoning；异构模型、复杂通信图、tool长程及可审计文本仍future。
- owner建议 **`AGENT-MULTI-AGENT`（Ch82）**：在通信状态表示之后增加“状态尚未物化时的构造成本”，将训练期轨迹蒸馏与推理期一次KV写入分清。Ch75只引用prefix依赖边界；不新增latent论文独立owner，不称普遍可删除推理过程。

### 9.2 [22899 Provable Authority](https://arxiv.org/html/2610.22899v1)

- **2+2+2=6；安全影响层深入，必要 Source 完成。** 实读§2.3～2.10、3、4～6、7.1～7.3、8.1～8.3及9相关机制对照；这是协议设计，不是已实测支付系统。页面末“Experimental support, please view build logs”是arXiv HTML通用页脚，**不是论文实验支持**。
- 历史delegation记录不可变≠当前可执行。ARP/version/status解析现时权限；session eligibility/SAC仅能提案/API，**rail adapter必须拒绝SAC支付**。确定性控制面先canonicalize、逐transaction policy/status/approval检查、原子reserve capacity，再发短时single-use EAC，绑定sender/session key、audience、exact digest、reservation、status epoch、expiry；adapter从实际rail instruction独立重算digest并consume。这是具体“提案权限≠commit authority”接口，不把基本leastprivilege归为原创。
- 摘要之外必要细节：digest schema必须规定decimal/currency/time/Unicode/null/order/version，物质字段变化须新decision/reservation/approval/EAC；两个$4k争同剩余$5k靠serialized reservation，不是各自签名防止超支。step-up人必须有**独立组织权限**且批准同digest，不扩agent站立授权。即时证据与旧grant分离，offline status只在最大staleness内可接受。
- 关键反侧/失效：提交后timeout是unknown，不是blind retry；按idempotencykey/railref查询reconcile。旧ledger事件不overwrite，settled后return另linkedevent。现有fiat rail未普遍原生接EAC，依赖preflight/gateway/partner adapter；不是写个token就控制任意外部bank接口。EAC consume与submission的recoverable/atomic路径是**规范要求**，未给跨故障分布式事务实现或实测exactly-once证明。
- 本稿无形式化安全证明、attack测试/benchmark或真实部署吞吐；不采用标题“Provable”作为效果保证。protected key仍可被合法workload内恶意代码调用；issuer/KMS/rail compromise、source错误、authorizedperson被骗/串谋、允许的stale窗口以及有效但被诱导的不可逆结算均明确残余风险。组织配置policy的正确性不由BRE deterministic自动保证。
- owner建议 **`AGENT-TOOL-CALLING`（Ch78）**：把tool proposal、session capability、具体effect的commit权限以及重试unknown state分开，用digest+reservation+consume作为带条件协议案例。Ch72安全只交接trust/TOCTOU/issuer边界，不把payment合规建议扩成新主线，不称消除prompt injection或fraud-proof。

### 9.3 [22882 Cooperation Without Adaptation](https://arxiv.org/html/2610.22882v1)

- **3+2+2=7；设计反证深入，必要 Source 完成。** 实读§3.1～3.3（含payoff/selection定义）、4.1正文与4.1.2、4.2.1/4.2.2、4.3、5及limitations，不遍历Supplement。反证“self-play合作率=对激励/伙伴可靠适应”，不主张所有LLM完全不适应。
- 六席e40、10round、action0/2/4、target120，失败以p丢savings；welfare-optimal symmetric benchmark在p=.5切换，不是唯一equilibrium。零贡献始终是一个equilibrium，作者不声称subgame-perfect；p0及outcome settled后的贡献是更强dominated-action证据，避开riskaversion可解释低正risk贡献的问题。
- 5provider production-model面板、3950games、每cell10games，unit是game而非独立seat；95%gamebootstrap/permutation。固定五script partners、10modelpairs×1～5seatcomposition、risk与prompt控制分别干预。goal句能改变p0行为，neutral wording/remove hints不足；**partner/mixed/selection仅baseprompt**，不能把goal干预结论直接移植过去。
- 固定partner1000games仅186完全bestresponse且都为fairshare，settled后Qwen/Grok仍浪费；另有模型会见settled后停，说明有限适应确实存在。Gemini自play全成功不保证单Qwenreplacement稳定：11/30成功；把recorded Qwen末轮0改2能算术救回92%failed mixed tables是**事后固定他人动作counterfactual，非实际干预**。partner开局非randomized，相关变化不能认作causal最佳反应。
- 选择为基于estimated composition payoffs的rare-mutation Fermi过程β1，N6→30同时变table sampling与fixation dynamics，非只换scoring metric、也非真正训练更新权重。N6 .9风险selected47%target vsuniform76%；大population在中高risk换winner，weakselection/删candidate不稳定。不能当通用“选低贡献必然坏”定律。
- 局限：英语单游戏五模型、per-cell10、无显式runningpool可能有算术错；同席block固定令position/composition混杂，riskneutral福利口径和rareentry假设；goal仅一个措辞且无group-payoffgoal对照。行为选择不证明内部reasoning/动机，value问答正确也不证明行动会用；零宽bootstrap不等确定性。
- owner建议 **`AGENT-MULTI-AGENT`（Ch82）**：协作验收增加独立的incentive、partnercomposition、settled-action与individual/group welfare轴，保留selfplay只在同质条件的合理性。Ch66只交接评测口径，不将合作行为直接外推生产agent工具安全。

### 9.4 [23662 Learning Robot Metareasoning](https://arxiv.org/html/2610.23662v1)

- **2+2+2=6；安全/理论条件影响层深入，必要 Source 完成。** 实读§II～V（SMDP、bound假设与proof、PPO训练）、VI实验设置/三域结果及VII，不把没有验证的理论假设当实机保证。
- 核心不是泛称adaptive compute：一次h决策同时买h×dt的solver时间并承诺同长度open-loop action。state、旧h、正在执行的plan及planner统计（ESS、time-to-infeasibility、observed-model mismatch）作为预算输入；没有另找reflex低层。chunk内discountedreward求和，bootstrap用γ^h，按环境经过时间而非决策次数比较。公式GAE写γ^h×λ（不是(γλ)^h），不替作者静默改写。
- objective equivalence只是对同一执行轨迹按不重叠interval重新分组的恒等，不证明learnedpolicy全局最优。deviation bound需reward对state Lipschitz、uniform单步W1 mismatch δ、nominal dynamics Lipschitz，且继承上一轮计算时预测初态偏差e0；B(h)单调给可容忍h的上界。**未实测/估计这些常数形成在线shield**；goal indicator/collision/contact的非光滑性也不能默认满足Lipschitz。Proposition1另需exactadvantages、exactsurrogatemaximization，普通有限sample/clipped PPO训练不由此获得实证单调/安全保证；本轮不采用该保证。
- A10040GB、ROS2/JAX/MJX；navigation dt.1s、cable .02s、PushT .04s；MPPI/CEM随h改变horizon及sample/population，不等于仅多几次同问题迭代，monotonic-improving solver是前提而非任意planner性质。2×128 MLP+PPO，2500×2048epochtransitions；未给逐h实际tail latency/deadline分布，不能外推VLA大模型实时部署。
- fixed-h全扫描是主要对照；navigation300episodes，去plannerstatistics success低12pp；cable20episodes learned80%成功、fixed均失败（该cable是simulation，勿称真飞行）。DJI RoboMaster为地面实机例子，不把全部图表当hardware trial。PushT16matched600step验证中恒选h8，终态误差与bestfixed相同，支持**无可利用预算变化时adaptive不必优于静态**。success-conditionedreturn/harshness会偏袒低成功baseline，文中主return包含失败。
- owner建议 **`MULTIMODAL-EMBODIED-VLA`（Ch26）**：动作chunk与并行planner共享同一物理时间预算，反应频率/状态漂移进入质量取舍；保留静态h在nominal无disturbance场景合理性。Ch79只引用metareasoning路由；不作为新安全控制器或PPO定理收录。

### 9.5 [23271 NestedVLA](https://arxiv.org/html/2610.23271v1)

- **2+2+2=6，标准必要 Source 完成。** 实读§3.1～3.5、4.1/4.2、4.3正文、4.4、AppC storage及Hlimitations；不遍历诊断附表。
- 同π0.5 base独立FlowSDE微调三个**benchmark级skill**（MW/ManiSkill/CALVIN），差分top-K10% per-module mask+α1.1。只对0.40B actionexpert训练task-ID hypernetwork；3.21B VLM仍按task保存稀疏delta。2D参数patch按type/layer/坐标寻址，共享trunk+per-taskembedding/LoRA/outputhead生成**已知task的参数**再合成base，非按语言即时zero-shot技能发现，也非静态加权aggregate。
- 所谓无需expert routing指生成后是普通VLA，无runtime MoE；仍必须提供task ID、取对应VLMdelta/mask。generator约430M、每task有largeoutputhead，M增大会涨存储；加入新skill需扩taskembedding/head并retrain，未证incremental稳定或规模无关成本。simulationonly无实机；不采用“continual learning”或任意机器人转移已成立。
- storage明确32-bitcheckpoint分母；1base +三taskmask约.09 +VLMkeptvalues约.27 +generator约.12=1.48≈1.5×，不是单个1×模型或所有delta已吸收。当前只3skills；不把存储ratio等同活跃GPU峰值、切换开销、latency或throughput实测。
- static/dynamicmerge同设对照，作者报平均66.7%对strongest25.6%，三域采用不同指标（MW/MA success_once，CA五子任务chain success_at_end）平均不能当统一任务成功概率。3seeds typicalstd±2.7。MW37.9 vs原task72.3；10%maskedGT仅48.4、20%60.2，表明压缩预算已损失大量但仍余约10.5pp生成误差，不能说gap完全非capacity。所谓GTmask ideal是此重建recipe参考，不是所有same-mask learnedvalue策略的数学upperbound。
- ablation：task-specifichead贡献大，额外LoRA可删且loss更低（97%paramcost），所以不能把每个“nested”部件都说必要。正文§3 Eq3/4将z定义含α却Eq5再外乘α；§4.3提standardizedloss与§3简化loss也未完全展开一致。**记录记号/实现细节待核，不凭公式手算倍增重建或冒称实现复现**；有限命题只用明确的actiongeneration/VLMresidual分界和报告对照。
- owner建议 **`MULTIMODAL-EMBODIED-VLA`（Ch26）**：data-silo技能合并的冲突可以从“选已有delta值”转成“条件生成actiondelta”，代价是taskID和未压入generator的VLM残差仍长驻；需与已有adapter/merge边界比较，不另立skillpaper专章。

### 9.6 [23127 BeJEPA](https://arxiv.org/html/2610.23127v1)

- **2+2+2=6，标准必要 Source 完成。** 实读§3.1～3.4、4.1正文/4.2～4.4；定点A.4理论条件、C.1/C.2训练/观察接口与B的causalbias，未遍历全部实验附件。
- 身体+worldanchor同一256维latent，Dynamic做goal-independent单步action→nextlatent监督；Successor按collectiongoal做discounted future embedding TD summary。线性goal-similarity下V=〈S,zg〉，actor通过一跳Dynamic再Successor求行动梯度，避免把整段远期rollout显式递归展开；successorfeature/JEPA基本概念不是本稿原创。
- **并非完整future distribution**；expectedembedding压掉多模态/时序细节。将E[S(z_next)]近似为S(D(z,a))不是一般交换律，A.4证明需latent Markov且nextlatent deterministic、保持reward/policy必要信息、固定encoder/policy/exactpredictors。本文只支持受控结构分解与经验质量，不称任意stochasticworld的精确长程替代。
- 训练privilegedbodykinematics、replay+retargetedmotionprior/physicalpenalties；部署historyencoder蒸馏为proprioception/rootestimate/history，非训练和部署同可观测。无downstreamtaskreward≠无motiondata/物理目标/训练。2kclips4.78h，goalprior在data中；真实UnitreeG1 root来自LiDAR+FAST-LIO，不是visionfree无需定位。
- 关键对照为comparablecapacity mergedpredictor、stopeitherencodergradient、Dynamic-onlyMPC。Table2 meanrootxy full.642m vsmerged1.348、Dynamic-only1.004，支持局部物理监督和长程continuation分工；不直接证明任意任务泛化/最优控制。训练双方共享encoder，故并非各模块完全独立。
- successor proximity不精确指定“何时到达”：同frozenweights额外短rollout residualMPC用referenceclock/root/wrist几何cost改善lag，AMASS94.8→21.2ms、LAFAN97.2→51.0ms（simulation50Hz selected20ssegments），代价是boundedgradientsearch、模型误差及horizon。不是声明已删除所有rollout；远程价值用summary、局部时间精度仍用rollout。Rootrefinement的pastobservation/predictionbias EMA是causal correction，不读futuretruth。
- G1kickrecovery/起身/goal-switch是展示sequence，未给足够repeatedtrials/uncertainty证明robustness率；tSNE/PCA及linearreadout不能证明完整几何保真。未见明确部署MPC时延/硬件tail，50Hzsimulation接口不等所有部署实时验收。
- owner建议 **`MULTIMODAL-WORLD-MODELS`（Ch25）**：长程expectedfeature摘要与单步可控后果分开，同时保留摘要不含精确时间/多模态信息的边界；Ch26只接世界定位与短程执行精度。不是把successor替代所有动态模型或通用worldfoundation已实现。

### 9.7 [23002 MAP / Robotic Spatiotemporal Editing](https://arxiv.org/html/2610.23002v1)

- **2+2+2=6，标准必要 Source 完成。** 实读§3.1～3.5、4.1～4.3（含Table1）、5；为核进度、mask预算、composition和实机边界，定点Supplement1.5、2.2/2.4/2.6 deploymenttips、3.1/3.5，不遍历其它附表。
- 2Dpoint/flow、3Dpoint、orientation/keypose/gripper统一为referenceprogress×7Cartesianaction的部分scalar+binarymask，image-space输入需先映到actionframe；未指定与指定0靠mask分开。learnedprogress选局部window，2Dconv128feature连visual/proprioception做diffusion条件；不是直接把progress浮点当rowindex。多mask训练含structured/empty/random，LIBERO random→structured两阶段。
- 可接受新mask组合的**接口统一**不等于可靠执行所有constraint：Mix0（dense2Dflow+1pose+3points）未进训练，compatibleoverlap才可OR，重叠值冲突无已实现解算保证；foundationflow/VLA兼容仍future。反侧不能因表示新颖消失。
- STC同backbone/training条件；Table1是top-three checkpoint picks口径，MW/ManiSkill为separatepolicy、LIBERO共享multitask；IP92.67/64.67%，不把前者当跨taskgeneralist。simulationreference由demo mask获得，LIBERO fixed100testtrajectories产reference；现实上游参考的可获得性/误差不是同实验。
- RePaint每noiselevel用相应noisedreference覆盖已知值、最后cleanoverwrite，只对**sampledcommand数值**严格；不证明tracking/kinematics/碰撞安全。Table1 CE降低.023→.014、.045→.026时SR **92.67→80.04、64.67→51.33**，所以“任意控制不损完成率”不成立，应明确accuracy/taskutility取舍。
- 同visible-ratio不等信息量：3Dmask约3rT、random7rT；预算匹配另用1.4T标量数且离散近似，勿拿ratio曲线当严格equalbudgetcausal证据。CE是每constraint到trajectory任一点min distance，不能验证正确顺序/指定时间；normalizedCE也非mm。PickCube固定checkpoint100trials learnedprogress83% vsclock67%、CE.02912vs.03983支持该set的alignment，非证明progress通用正确。
- FrankaR3双camera15HzabsoluteEEcommands、task-specificpolicies；真实物理误差mean44.3mm/7.8°不是精密强约束通过。单个latepointSR<30%：localwindow在靠近该stage前看不到参考；部署tips要求smooth/monotonicprogress、限制backwardjump并区分progresscomplete/taskcomplete。离示范分布/互相冲突reference仍可失败，不能称任意时空编辑已解决。
- owner建议 **`MULTIMODAL-EMBODIED-VLA`（Ch26）**：把生成器条件分解为“给定哪些动作坐标、在什么任务阶段生效”，保留softcondition/hardoverwrite/真实执行三层差别；Ch25只引用上游partialreference接口，不把RePaint已有机制称新原创。

### 9.8 [22496 RAX / Scaling Online Exploration](https://arxiv.org/html/2610.22496v1)

- **3+2+2=7；实机安全/自主性影响层深入，必要 Source 完成。** 实读§3.1～3.5、4.1/4.2、5.1、5.3.1/5.3.3/5.3.4、5.5/6；必要定点§8～10.2 interface/evaluation、13汇总口径、14实机总设置/14.2与14.2.1的故障/感知限制/14.5结局，不遍历全任务附件。
- frozen codingagent通过SDK/MCP探索，把confirmedmanualtool-success转为observations→perception/planning/verification的Python闭环程序；preconditions/`Unsure`异常把超出适用域交回agent；跨session保存带执行证据、条件和版本的skill，不改modelweights。“可执行记忆+验收后复用”是有限增量，不把CodeasPolicies/基本skilllibrary说成新概念。
- backend隔离不可由agent改driver/controller，提供PD/OSC/wholebodytracker、IK/motionplanner等helpers、calibratedRGBD和operatorarm/disarm及limits；preview仅robotmodel/部分静态结构，不含全部taskobjects。task-specificgeometry/plan由agent写，但**并非无预训练控制器/无工具文档/零人类先验**。Humanoid主结果有3teleopactiondemonstrations且可剪gait；无action对照增加explorationbudget后均值81.9，但若干wholebodytask仍低10～16.6pp，不能沿用摘要“所有实验零actiondemo”。
- §10明示ClaudeCode/Opus5.5、部分Codex/GPT6、xhigh，Gemini3.8Flash允许$10/session；这是作者标签，不补造可复现snapshot。isolatedcontainer无network、工具远程执行；exploration有budget/新layout、train/test分离。冻结bundle新scene独立rehearsal计入budget，testfreshcontainer无agent/edits/retries/不回传结果；另agent-in-loop从frozenworkspace初始化，二者不能混报。
- 编译确可减少在线deliberation：airfryer首success72.3mininference→program18sec，robot2.9→2.5min；Bandu6pieces→7pieces任务不完全相同，17.2min→10sec外部overhead而robot9.3→10.9min。只比selectedsuccesses/含初探索和后成熟代码，非同budget因果A/B、亦非总E2E同倍加速。simulationloadingcar仍>1hourenvironment执行。parallelCodex32budget14.2→9.2h且score66.4vs65.6，Claude单48/多32budget不同；不能全称严格2×samebudget性能提升。
- memory/reuse §5.5是真实module调用和增量修正：bucket/box约25/1200line改动，但仍有banana桥接代码、chair失败后4cm修正；不是完全frozenzero-shot复用。paper-towel两wet-run stain去除但散纸还需supervisedscript，不能称完整自主清理闭环。
- 安全反侧必须随采用：airfryer10runs中run2elbow撞camera触safetystop、run4/5/8需resume、run8还有agentrecovery；仅6/7/9/10cleanunattended。camera撞后reportedpose没变，agent做3.5mmregistration修正并弃另一camera；depth近<30cm不可靠、edgepixel有背景混入。joint/workspaceguard不等scene安全；后补guard是经历collision后改代码，不是预先证明。
- +37.4 **pp**是5benchmark各largestbudget对strongestlearnedmodel平均，Dex只5bimanual、LIBEROPro不用更强codingagentASPIRE作摘要基准；非匹配探索成本/架构消融的纯增益。实机以notes/frame/自身传感判定的少量case，Bandufinal7/7无intervention不抹去operatorreset/gripper重启/移动不可达piece/提示改变对齐策略。无安全失效率CI或fleet无遗忘证明。
- owner建议 **`MULTIMODAL-EMBODIED-VLA`（Ch26）**：高层探索生成可复用可执行程序、stagechecks与独立unattended验收如何把推理从每步移到失败/新条件边界；Ch77只交接repository记忆、Ch78接effectguard。保留low-levelcontrol/传感器/人为reset/自主program与agent监控的分层，不将安全或跨embodiment无成本扩展写成已证。

### 9.9 [23769 PRIME](https://arxiv.org/html/2610.23769v1)

- **3+2+2=7；设计反证深入，必要 Source 完成。** 实读§III-A～C、IV-A～E（各核心table/诊断/ablation）、V及-B训练参数；不遍历-C图集。
- demonstration晚时刻不必更接近成功：保留轨迹相邻edge，再以TCP/两fingerposition proximity和multi-viewDINOv3视觉相似门控跨trajectoryedge；cost为TCP位移+α×gripper差，以goalterminal成功标记为终点Dijkstra求remainingpathcost。对本轨迹可因另一demo有更短可达continuation而降低距离，也可给overshoot/backtrack负progress，打破按time强制单调的标签。
- nearestvisualeuclidean并非物理可达保证。原文“guaranteeingtransferability”过强：20新trajectory、每条平均>200crossedges、环境不变one-stepreplay仅99.4%feasible，<3°objectrotation仍falsepositive；图依赖coverage/threshold、别名/hiddenstate/不可逆状态可能造shortcut，真实manifoldgeodesic只是近似。history/velocitystate扩展future。
- 核心对照§IV-E PegHard：full70%，unitcost33.3、去configgate26.7、no-graphEuclidean56.7；Drawer96.7/90/53.3/33.3。支持connectivity、geometrycost、pathstructure联合，不证明DINO表征天然满足可达等价。threshold太保守30、太激进53.3，合理区间也非自动最优选择；top-K/邻接稀疏实现不补造。
- realPiper-X四tasksdemo20/30/50/50、每policy30randomtrials，π0.5base；各progresslabel统一Qwen3VL estimator及相同prioritizedpolicytraining避免只换backbone，仍少量trial无置信区间。diagnostic为collector另选120stagepairs+120localprecisionpairs/30experttrajectorysmoothness，local92.5vsbest70%，是人工精选有限set非随机总体；未披露多标注员一致性，不称groundtruth普遍充分。
- online先MSE拟合distance再Δdistance+successbonus，offline用clippedprogress/temperature加权BC采样，非所有差分都变RL。Δdistance未由discountpotentialshaping定理证明最优policy不变；onlineestimator误差/奖励hack未系统测试。simulationExpandedManiSkill扩大15×15→15×40cm/对象，2Mstep、末1M每25k评估3seed：67.4±5.6vs60.8±6.1 InD、35.3±3.1vs31.1±1.5OOD；10.9/13.5%是relative，不是pp。
- RTX3090上300kframesencoding2893sec、graph19.08sec为offline构建，未披露可扩到任意数据规模/在线latency；四episodes后某Episode0 distance稳定不等新state泛化收敛。有限采用“进度标签需反映有效可达距离，不以示范时间代物理进展”，不采用图绝对安全或真实最短可行path已证明。
- owner建议 **`MULTIMODAL-EMBODIED-VLA`（Ch26）**：示范含回退时，时间progress会奖励无效甚至倒退动作；跨trajectory可达近邻图给任务局部的非单调progress监督。Ch25只交接statealiasing/可达性边界；不把Dijkstra或successor已有概念列作新原理。

§9九家族本轮均有精确v1原件与必要Source读段，未遇真正必要材料不可访问；访问成功不是结论成立，争议/未披露项均在上文保留。此处仅宣告本slice证据阅读完成，**不宣告独立复核、Books判断或Daily闭环**。
