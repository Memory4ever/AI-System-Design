# 2026-05-22 遗漏来源补充



## A1 启动与保护边界

- 作者：`/root/supp_may22_author`；启动检查时间：2026-10-20T21:26:13+08:00。
- 实际重读 AGENTS、CODEX_RESEARCH_PROMPT、RESEARCH_CONTRACT、REPORT_CONTRACTS、RESEARCH_SOURCES 使用说明/每日组/arXiv 主题、ROADMAP，以及 LEARNING_STATE 最新路由。独立只补北京时间 2026-05-21 完整自然日。
- 原报告 254 候选整行、日期/评分、原 `2026-05-21T09:00:00+08:00 ～ 2026-05-22T09:00:00+08:00` 窗口与连续原 §4 保留。旧 20260916 非作者最终复核和 Source/POST 不因补窗重做。无既有本轮 SUP；本文件是唯一新增过程记录，root 独立维护 SUP_REVIEW_20261020.md。
- 发现只用日源主题切片及官方精确版本。已有宽库存只作有界相关标题补检；没有全历史逐项关闭。既有 05-21 报告只用于具名同事件去重，不沿用其候选池/评分反推本日。
- 本作者不修改共享 Books、索引、State，不 stage/commit/push。

## A2 首批准入校准包（待 root 独立判断）

实际入口：DataCite 官方 `prefix:10.48550 AND registered:[2026-05-21 TO 2026-05-21]` 与 language-model/LLM/Transformer/Attention/agent/inference/diffusion/GPU/memory/reasoning/token/world-model 主题，保留原件 `SUP_DATACITE_TOPIC_20261020.json`。按题摘语义选择，不以关键词决定准入。相关官方 abs 精确版本实际读完整摘要及当前版本说明。

1. **LT2，2605.20670v1**：[官方题摘与版本](https://arxiv.org/abs/2605.20670v1)。v1 2026-05-20T03:36:44 UTC；现有 v2 为 05-22，未见撤回标记，不混入本次 v1。全文待审。原约束：looped Transformer 叠加 full attention 保留平方历史成本 → 实际新增：循环在线性 attention 中迭代精炼记忆、在 sparse attention 中扩展有效感受野，并对比 GDN+DSA/Full+GDN 混合 → 需重新判断 recurrence 与 attention 选择是否独立。若日期合证通过，拟入现有 `MODEL-LONG-CONTEXT` 主线，尚不评分或声称 Source 完成。
2. **DuplexSLA，2605.20755v1**：[官方题摘与版本](https://arxiv.org/abs/2605.20755v1)。v1 2026-05-20T05:54:08 UTC；当前 v2 06-11，未见撤回标记。完整摘要的增量不是一般 full-duplex：共同 160ms chunk 时间线上联合连续用户音频、离散助手音频和 rate-limited action text，使 planning/tool emission 不必停止语音 → 需要比较 native 多模态同步表示与外部级联交接。拟入 `MULTIMODAL-REPRESENTATION`；不由摘要宣称工具执行安全/真实时延/因果收益。日期须合证，全文待审。
3. **代表性同事件去重**：HeadKV 2605.20600v1、HRM-Text 2605.20613v1、PulseCol 2605.20813v1、EqR 2605.21488v1，在 `papers/2026/05/21/README.md` 已有精确 v1 候选和证据段，当前仅定点核身份，不新增候选、不改评分或归属。
4. **范围排除**：`2605.20628 Divide-Prompt-Refine`（biomedical abstract generation）、`2605.20644 Design for Manufacturing`（aeroengine pipe routing）、`2605.21485 EvoStruct`（antibody CDR design）。标题已明确为领域应用或暂缓 AI for Science，没有具名纠错/安全信号，不为处置无影响的日期另追材料。

下一步：root 校准首两项准入；作者完成日源有限检查及相关标题补检、日期合证、单篇必要 Source 后即时送复核。当前未授日级完成。

## A3 LT2 必要 Source 与差额（prepared，待非作者）

原件已保存 `SUP_CORE_2605.20670v1_20261020.html`；[exact-v1](https://arxiv.org/html/2605.20670v1)。实际读取 §2.1–2.3、§3.1–3.5、Appendix A.4/B.1/B.2.2/C。日期原件 `SUP_DC_2605.20670_20261020.json` 为同 DOI、`arxiv.content`、`findable`、registered `2026-05-21T02:08:40.000Z`；官方 v1 唯一提交 May20 03:36:44Z → EDT日程最早公告 May21 00:00Z，整个可能区间均为北京时间 May21。该组合不是实际公开时分秒或全球首公开证明。

准入命题评分 `2+2+3=7`：有限循环下 mixer/state 的计算、保留容量及有效传播并非相互独立；不采用摘要层无条件“linear-time、rank-T、窗口Tw即有效回读”强保证。

- 机制：共享同一物理层栈固定T次；增加per-loop residual；GDN定长recurrent state与DSA显式KV/top-k读取不同，DSA不因稀疏读取而变成常数内存。Appendix B.1的单位key/β∈[0,2]/α∈[0,1]是算子范数条件；相同keys不增秩，正交keys是特殊构造，未证learned keys独立。
- 关键反侧：§2.2称窗口拓扑可达范围O(Tw)，B.2.2自己区分topological reach与surviving influence；uniform-attention/residual convex-mixture代理下有效horizon可不随T增长，不能把可达性当真实长程检索能力。理论代理不证明所有learned residual都会饱和。
- 实验：§3.1/Appendix C 在0.6B/1.3B、FineWeb-Edu100B tokens、T=4、4096训练长度，按参数/数据配比比较；参数随mix略异，不是matched完整算力。§3.2单H10080GB，1k–32k、batch1/2/4/8，FA2/fusedGDN，不能外推端到端服务SLO；Appendix C的训练attention kernel为FA3，不与推理设置混用。运行precision、并发、SLO未明确披露，不把训练bf16填到推理。
- v1内部Table2、§3.1正文和Table3/4存在PPL/均分不一致（如Full+GDN Table2 62.89，正文61.39；GDN+DSA Table2 60.73，Table4 59.23）。不采用精确效率/能力Pareto排序，隔离为作者数值修正请求；这不否定可读架构与可达/影响的逻辑区别。§3.5 RetNet divergence说明循环并不普遍稳定；A.4 ACT因优化与ragged halting困难未用于主预训，不能当自适应停止已验证。

Books差额：已加载ProjectContext/学习方法/写作指南及ROADMAP；对读Ch22的`共享全局历史与增加计算深度可以分别设计`（YOCO-U）、GatedDeltaNet/outputgate、固定hybrid段及Ch21/Ch23交接。既有正文有循环global-KV开销，但未承载“循环mixer的拓扑可达≠残留有效影响、loop数与cache/state分别计费”这一窄点。拟唯一owner `MODEL-LONG-CONTEXT`，在该标题下、现YOCO-U首段之前插两段。未授lease，不写。

逐字窄稿：

> 重用参数不等于重用同一份历史状态。若把共享层栈执行多轮，每轮仍需按其 mixer 合同维护状态：线性 Attention 保存固定形状的递推摘要，稀疏 Attention 可以只读少量位置，却仍保留随长度增长的完整 KV。选择循环次数时应同时核算重复计算、各轮 state/cache 与精确回读能力，不能仅用参数量或稀疏读取数说明容量成本。[受限循环模型研究](https://arxiv.org/html/2605.20670v1)进一步提示，mixers 的布局与循环步数必须共同验收，而不是先认定循环免费、再独立挑选 Attention。
>
> 多轮局部传播还要区分拓扑可达与实际影响：窗口路径能够经过更多跳到达远处，不代表旧信息在多次平均、残差捷径与压缩后仍可读。不能由拓扑直接给出有效影响界，须检验实际权重、残差、训练与召回；论文附录的固定影响范围代理已有反例，不能用来证明普遍衰减。同样，多次低秩更新只有在更新方向提供新自由度时才可能增加表达能力。循环会新增稳定性、状态身份与执行开销，有限模型的数值排序又有报告不一致，不能据此批准普遍能力/吞吐收益。远程精确回读、质量或净预算失配时，保留较少循环、完整历史或已验固定 hybrid；局部传播与全局访问的分工仍需单独设计。<!-- source-family:SF-2026-ARXIV-2605-20670 -->

拟本人注：`SF-2026-ARXIV-2605-20670`，Daily2026-05-22补查；exact-v1 §2–3、AppA.4/B/C；2+2+3=7。仅采用loop/mixer/state计费与拓扑/有效影响区分，隔离Table2/正文/Table3/4数值不一致、learned-key独立及通用稳定/ACT/SLO；作者原证prepared，待root非writerSource/PRE及实际POST。

root新增具体反证与修复：B.2.2的T无关effective horizon不采用。在其uniform causal w=2、residual α=.95代理内，单步位移概率p=.025，多轮位置服从Binomial(T,p)；T400距离10影响约.1267、T1000距离25影响约.0805，均大于.01，却超过所称约3.07固定horizon。窄稿已改为不由拓扑推effective界；理论/数值强主张继续隔离，7分不变。root仅授本标题后两段及本人末注窄lease，待保存后真实POST。

入口修正：首个DataCite UTC日期查询只作线索，不能声称覆盖北京时间全天；现重取精确UTC `May20T16:00:00Z～May21T15:59:59Z`，对应BJT May21。前两次大响应超时/不完整，不计覆盖完成。

## A4 DuplexSLA 必要 Source/日期/窄稿（prepared）

[exact-v1](https://arxiv.org/html/2605.20755v1) 本地`SUP_CORE_2605.20755v1_20261020.html`，实际读取§2.1–2.6、§3.3–3.4、§4、§5及AppendixC。`SUP_DC_2605.20755_20261020.json`同DOI/arxiv.content/findable，registered `2026-05-21T02:10:41.000Z`；v1May20 05:54:08Z→最早May21 00Z，整个区间落BJTMay21，未把登记时间冒充公开时刻。评分`2+2+3=7`，对应native同步表示的新消费/调度取舍，不评分一般授权原则。

§2给出160ms chunk、用户2×80ms因果连续features、助手TA4（text anchor+4×40ms音频码）以及每chunk最多10个action text tokens；超额延至后续chunk，10是硬件部署预算，不是不可变结构常数。§3.3 FIFO组织多action，§3.4双侧ASR监督补足TA4 anchor没有准确发声时戳的问题。7B Step-Audio2-mini初始化，约500k h CPT+1.92M text，约50k h定向posttrain，不能把全部收益唯一归于第三通道。

关键评价是自建2100例（1200turn/900tool，三tool pattern各300），50个车舱/家居tool schema；§5.1 function+arguments匹配、emission时间与成功执行不同。Table5 avg tool accuracy Duplex85.56%<cascade91.33%，multi75%<89.33%，avg emission delay0.64s vs2.77s。只说明该评价里的延迟/正确性取舍，不照录§5.4“matches accuracy”。Table6/7相同输入/接口不完全匹配，closed API backchannel label不可见；不批准普遍领先、尾延迟SLO或生产控制安全。实际硬件、precision、并发、完整训练重复/置信界未披露；不填造，不要求可选代码复现才可采用接口。

Books对读Ch23现有full-duplex时间身份与interrupt-frontier、TADA/TASTE、SilentThought以及Ch24交接；现有正文未完整承载“在共同chunk钟上为语音和结构action分别保留预算、spill跨chunk使完整action另有完成时点”的窄点。唯一owner `MULTIMODAL-REPRESENTATION`，拟在`实时全双工系统中，用户音频、视频、文本与 assistant 输出会并发到达`段之后插两段，未获lease不写。

逐字窄稿：

> 共享时间身份还可以进入模型的输出表示，而不只由外部队列补记：在同一个固定 chunk 上接收因果用户音频、生成助手语音，并另设有速率预算的文字动作通道；后者承载转录、交互控制、计划片段和结构化工具调用。[一条受限语音分支](https://arxiv.org/html/2605.20755v1)以160ms chunk、独立语音布局和每chunk最多10个动作文字token实现这种接口，超额文字顺延后续chunk。固定钟为各通道提供对应位置，却不使text anchor天然成为准确发声时间；训练中的双侧转录对齐和实际decoder预算仍是必要条件。
>
> 动作文字与语音分账可避免长JSON占满当前语音块，却增加跨块积压、完整动作识别与时间对齐责任。10-token预算必须随实际硬件和decoder重验，不能由结构名称推出每块实时完成；动作发射、参数匹配与外部操作成功也不是同一件事。有限自建评价里，更短的tool-call发射延迟伴随低于级联基线的平均及多动作正确率，且训练配方与接口同时变化，不授第三通道的唯一因果或通用SLO。时序、质量或副作用核验不足时，保留独立转录/级联、等待完整调用和保守turn-taking；表示层只交付带来源和时间的proposal，执行授权仍由工具与runtime承担。<!-- source-family:SF-2026-ARXIV-2605-20755 -->

拟本人注：`SF-2026-ARXIV-2605-20755`，Daily2026-05-22补查；exactv1 §2–5/AppC，2+2+3=7。采用共同chunk钟与音频/action预算分离，保留spill/双ASR、tool精度退步和ND运行配置，不授执行安全/普适实时；prepared，待非作者Source/PRE/实际POST。

## A5 日期修正后的发现入口

精确UTC/BJT窗口查询原件`SUP_DATACITE_TOPIC_20261020.json`已完整解析：191个主题线索，page1/totalPages1，未把所有命中变成待关队列。注册字段是发现，不自动证明公告/首次公开。相关旧候选只按精确身份定点去重，其余范围先于贡献；仍继续官方本窗相关标题补检、必要摘要与当窗资格。

## A6 第二批准入校准（完整题摘实际读，日期/必要Source未预签）

以下来自A5精确窗口主题线索，不继承旧Daily池；旧05-21只核精确重复。每项目前只证明可进一步核验的具体增量，拟候选分数待准入后记录。

| 精确v1 | 原约束 → 原文具体增量 → 设计/解释变化 | 拟owner |
| --- | --- | --- |
| [20683 LTC](https://arxiv.org/abs/2605.20683v1) | embedding层压缩在bi-encoder有效不保证cross-reranker有效 → 中间层adaptive pooling及层位消融 → 检索压缩位置需绑定交互阶段，不照搬embedding压缩 | AGENT-RAG |
| [20708 DAR](https://arxiv.org/abs/2605.20708v1) | DiT残差加法固定累计 → 按denoising时步学习非增量式、而非单调不增的跨层历史聚合 → 残差路由是与生成目标并存的设计轴；训练iteration不等完整成本 | MULTIMODAL-GENERATIVE-PARADIGMS |
| [20752 GaussianDream](https://arxiv.org/abs/2605.20752v1) | VLA模仿缺显式几何/演化监督 → train-only当前3D与未来flow辅助head，部署只保prefix → 区分几何学习信号与在线world-model预测，不能将移除heads称运行时规划 | MULTIMODAL-EMBODIED-VLA |
| [20873 PlanningBench](https://arxiv.org/abs/2605.20873v1) | 固定任务集难隔离planning结构难度 → constraint-driven生成/instance checklist与确定解reward比较 → 验证器/难度定义本身影响训练和评价，不以多任务清单准入 | PLATFORM-EVALUATION-SYSTEM |
| [20950 SPpruner](https://arxiv.org/abs/2605.20950v1) | 只留query对齐主体会割裂关系 → saliency与semantic分数相加选focus后邻域context聚合 → 视觉压缩需比较主体与关系信息责任 | MULTIMODAL-REPRESENTATION |
| [21171 FTerViT](https://arxiv.org/abs/2605.21171v1) | 只三值encoder留下全精度周边决定compact模型总量 → patch/LayerNorm也三值并上MCU → 量化产物边界不止主体matmul | INFER-TENSORRT-LLM |
| [21312 Frontier](https://arxiv.org/abs/2605.21312v1) | monolithic/平均成本模拟可反转SLA选择 → 按角色worker、scheduler-batch-engine与stateful请求模拟PD/AF拆分 → 模拟 fidelity要按目标决策和资源分账验收 | INFER-SCHEDULING |
| [21347 IG](https://arxiv.org/abs/2605.21347v1) | 逐trace诊断漏群体模式 → scout/investigator在trace population提假设并连证据 → corpus sampling与grounding/下游修复评价须分开 | PLATFORM-TRACE |
| [21446 LostFog](https://arxiv.org/abs/2605.21446v1) | 干净输入解释稳定不代表退化传感可靠 → 同场景8类perturbation检查CoC与轨迹，另有CoC开关对照 → 解释一致性可诊断但相关性不签发安全 | MULTIMODAL-EMBODIED-VLA |
| [21466 StreamEdit](https://arxiv.org/abs/2605.21466v1) | data-to-data多步编辑与few-step生成不相容 → frozen streaming生成的dual branch/self-attn bridge/cross-attn源条件 → 编辑条件与采样路径需分别验收 | MULTIMODAL-GENERATIVE-PARADIGMS |
| [21470 AgentJIT](https://arxiv.org/abs/2605.21470v1) | 每步截图后LLM调用为串行关键路径 → 生成代码plan+tool条件验证+latency分布MonteCarlo排程 → 计划编译与运行依赖/状态验证分工，不由speedup准入 | AGENT-WORKFLOW |
| [21472 Stream3D](https://arxiv.org/abs/2605.21472v1) | frozen逐视图生成不一致/全历史增长 → 固定frame budget、evidence score选择历史条件 → constant cross-chunk frame memory不等完整3D状态固定或truth | MULTIMODAL-REPRESENTATION |
| [21489 CARV](https://arxiv.org/abs/2605.21489v1) | 每个noise样本都付昂贵上游费用 → 同一上游结果多noise重采样+IS/分层 → 方差下降只在MC为瓶颈时转成质量，single-step低variance不改善FID的负结果值得保留 | MULTIMODAL-GENERATIVE-PARADIGMS |
| [20402 MXFP4](https://arxiv.org/abs/2605.20402v1) | 把量化误差看成单一noise → scale/deadzone/grid三部分与RL训练路径区分 → 不能让一种修正/熵代理认证全部训练路径 | TRAIN-RLHF |
| [21235 LamPO](https://arxiv.org/abs/2605.21235v1) | scalar组优势丢relational权重 → pairwise reward gap×sequence-confidence + 可选ROUGE-L → 必须隔离pairwise权重与新增dense reward的归因 | TRAIN-GRPO |
| [20530 AgentAtlas](https://arxiv.org/abs/2605.20530v1) | 单success列隐藏控制/轨迹错误 → taxonomy-aware/blind协议让label menu影响显现 → 排名可能由prompt与评分轴驱动，synthetic1342不是独立真实基准 | PLATFORM-EVALUATION-SYSTEM |
| [20201 ProxyCoT](https://arxiv.org/abs/2605.20201v1) | full-context长推理差而短proxy可解 → 在proxy上RL/teacher出链再full-contextSFT grounding → 教师可见性/上下文长度与部署检索不能混同 | TRAIN-SFT |

以上是当时题摘准入准备，不是最终候选清单；随后逐项核官方页面的结果覆盖本表：21235已由官方撤回/移除，明确排除且不评分；20201实际v1提交Apr6，May21登记联合界跨日，资格尚待定点恢复。不能以相邻ID或本题摘曾在库存出现签日或签Source。原件ABS已保存，必要HTML随单篇准备继续送root。

## A7 首两项实际写后层

root SUP_REVIEW R4已实际非writer核LT2修复后两段（含DSA精确范围）、Duplex两段、完整局部邻接与两本人注，通过并释放窄位。作者仅行政同步既成POST事实并读回；2项真实整合，不授其余17或DAY。旧README仍未改，原候选254整行hash（原46–299）`ec0e819fb0b50f4bda03df056d35841919610ce8475e398e2addb720ac9febac`，连续原§4 hash `3b167ad0777f9adbcf2f874df8c6a190958f63b5c49eb3c0e90e2e86d98c7e5c`，后续融入只在旧块之后新增。

## A8 Frontier 必要 Source/owner/逐字PRE（prepared）

原件`SUP_CORE_2605.21312v1_20261020.html`，[exact-v1](https://arxiv.org/html/2605.21312v1)，实际读§3.1–3.4、§5.1–5.3/Tables4–6、§7。候选增量`2+2+3=7`。DataCite原件`SUP_DC_DEEP4_20261020.json`见同ID登记字段；v1May20 15:40:18Z在18Z前→最早May21 00Z，必要日期待root逐项合证，不用同批其他ID代签。

机制：control按角色worker显式连prefill→KV transfer→decode与AFD activation依赖，MoE combine等最慢rank；execution adapter改变scheduler-visible block、实际padding batch和token commit，而不是乘静态speedup；fidelity用请求长度分布/专家负载特征预测kernel，分别kernel-only与launch-inclusive。dummy-profile扣activation/NCCL/graph非KV占用后决定block预算，再让admission/preemption回馈下轮。stateful reasoning固定per-round token plan+tool delay、affinity/prefix复用，不是模拟agent语义。

评价：两台各8H800SXM、NVLink400GB/s/NDR400Gb/s，vLLM0.10.2V1；Llama3.1-8B/Qwen3-30B、Step3-316B AFD；prefill2048/256、decode256/2048、balanced1024/1024与SharedGPT。算子BF16/FP8，运行配置依行，不能跨行合并；metric是request TTFT/TPOT（默认P95）及workload E2E makespan，不把后者当P95。MTP接受率强制0.3/0.7，Table6误差上界11.28%，不是任意acceptance忠实；AFD为inhouse离线标定，只重点吞吐，1024GPU是simulation不是实际大集群验证。§7明确vLLM中心、CPU overhead预测不稳，测量侵入需隔离；不能以<4%平均吞吐误差签任意尾SLO或成本最优。

Books已读Ch56开篇token-state/四层决策与相关profile/SLO段、Ch55/57交接；缺少用“scheduler→batch→cost→memory admission反馈”检验模拟器的具体链，拟唯一`INFER-SCHEDULING`，在`只优化其中一层，可能把瓶颈推给下一层。...`段后、`目标函数不止吞吐`之前两段。未获lease不写。

逐字窄稿：

> 检验调度方案的模拟器，也必须保留这条状态反馈链，而不只把请求长度换成平均执行时间。可以按prefill、decode、attention或FFN角色连接完成与传输事件，让scheduler先决定batch，再由kernel/通信模型给出本轮代价，更新KV余量、token进度与下一轮准入。CUDA Graph既改变padding形状又移除launch开销，prefix hit改变待计算块，speculation改变验证与提交进度；若只乘一个静态加速系数，这些变化就不会反馈到排队和抢占。[受限模拟器研究](https://arxiv.org/html/2605.21312v1)将它们放回同一闭环，是为了检验某项调度选择，而不是让模拟替runtime承诺服务。
>
> 校准也须跟随影响决策的变量：相同总token数可以有不同请求长度分布，相同MoE容量可以有不同专家负载，权重之外的activation、通信workspace和graph占用也会改变可用KV块数。应分别核算kernel与host开销、通信依赖、容量和整段请求结果，并披露超出profile支持的切片。小集群实测、离线标定和更大集群模拟不是同一级证据；强制acceptance或预定tool延迟也不是实际模型行为。新增profile、模拟与维护费用仍计入选择，CPU开销/后端或流量漂移时回到实机测量、保守余量和已验队列，不用平均误差给尾SLO、所有框架或大规模部署签保证。<!-- source-family:SF-2026-ARXIV-2605-21312 -->

拟本人注保H800/vLLM0.10.2V1、profile-closed-loop、MTP强制acceptance/AFD离线与CPU限制、未实机复现；prepared待rootSource/日期/PRE及实际POST。

## A9 CARV 必要 Source（prepared）

[21489v1](https://arxiv.org/html/2605.21489v1)，本地CORE21489；实际§3.1–3.2/Eq12–17、§4.1–4.3/T1–4、§5、D.2.1–D.2.3/F.1。增量`2+1+3=6`，因具体负结果可能修正已有蒸馏解释深入必要域，不为处置降低/提高分数。v1May20 17:59:52Z在18Z cutoff前；同DOI findable/arxiv.content registeredMay21 02:28:01Z（DC_DEEP4），联合界整段BJTMay21。

机制：昂贵upstream render/encoder/generator固定一次，在同一结果上对独立(t,noise)重复K次；总方差里across-input项仍随R而非RK下降。Importance proposal须有p/q修正与支持；用loss显式weight近似梯度norm需相关假设，不能把每任务当同一最佳proposal。分层inverseCDF只是取样设计，离散grid snapping的精确无偏recipe本轮不采用（正文混连续/离散）；不以有界说明代实现已核。

比较对象是固定teacher下每单位wall-clock的梯度方差与下游质量，不是采样速度。SDS SD2.1/NeRF/InstantNGP/threestudio、30prompts×3seeds、CLIP代理；ECM是baseline曲线插/外推到同variance的成本比，不是生产加速。DMD2 DiT-XL/2/ImageNet256、A100、baselineR8K1约.38s/iter，K16约.59s，5seeds；T3/F26–27能下降variance而matchedwallclock FID无改进。D.2.3明确generator-input diversity解释仅consistent、非严格matched；auxiliary/bilevel机制没有被唯一识别，不能把负结果诊断写成已证因果。teacher drift、输入variance主导、不同render/denoise费用会使增益消失，额外variance sweep也付费。precision/concurrency/SLO未披露，不外推在线服务。

拟Books唯一`MULTIMODAL-GENERATIVE-PARADIGMS`：需要对读具体蒸馏/预算段后决定；当前Source先送非作者，不等其余材料，尚不预签已有覆盖或真实整合。

root A6校准：16项具体贡献准入有效，FTerViT仅条件准入须读patch/normalization新算子决定增量，不以组件总内存或MCU部署本身入选；DAR non-incremental已修为非增量式聚合，不误作单调不增。准入不是必要Source/Books通过，不继承通用权限/费用口号评分。

### A9b CARV 具体owner与逐字PRE（未写）

已对读Ch24 Few-step Distillation、统一成本模型及ParallelProgress/ActiveCompute，邻章Ch23表示与Ch25world-model交接仍不承接teacher梯度估计。既有正文有teacher/critic计费与独立质量gate，未承载“同一昂贵input上重复noise不能增加input多样性，降低gradient variance未必改善matchedwallclock质量”的具体替代分支。唯一owner`MULTIMODAL-GENERATIVE-PARADIGMS`，拟`一个统一的成本模型`成本清单之后、`Parallel Progress 与 Active Compute`标题前两段。

逐字窄稿：

> 训练时的teacher求值还要把“新输入”与“同一输入的新噪声”分开计数。若昂贵render、encoder或student forward的结果可以在当前更新内复用，就能在它上面重复抽取扩散时步和噪声，先平均teacher信号，再沿同一上游图反传；这只削减给定输入后的条件方差，不增加不同输入或视点的覆盖。重新分配时步采样还须保留目标分布支持和相应权重，不能用更偏的proposal悄悄改训练目标。[有限固定teacher研究](https://arxiv.org/html/2605.21489v1)把输入次数、噪声次数、方差与实际费用分账，而不是将所有teacher调用视为可互换的样本。
>
> 这种复用是否值得取决于两道门：上游与denoiser的边际费用，以及梯度方差是否真是下游质量瓶颈。单步蒸馏的有限对照中，更低梯度方差并未改善同wall-clock的FID；输入多样性、辅助目标和交替更新是尚未唯一识别的解释，不是由负结果已证明的因果。方差曲线插算出的等效compute也不等训练或服务加速，额外测量、内存驻留、重采样与teacher费用仍需承担。teacher漂移、输入覆盖不足或真实质量不改善时，保留独立input采样、原训练估计器和已验多步teacher，以同预算质量作决定，不由variance更小批准蒸馏更好。<!-- source-family:SF-2026-ARXIV-2605-21489 -->

本人注拟保§3/§4/D2/F1、A100/DiTXL2/ImageNet256/5seed、固定teacher/ECM估算与matchedtime负结果；6分但具体owner差额深入。未获lease不写。

## A10 AgentJIT 必要 Source/owner/PRE（prepared）

原件[21470v1](https://arxiv.org/html/2605.21470v1)，local CORE；实际§3.1–3.3/Alg1–2、§4、§5、§6及H。`2+2+3=7`。v1May20 17:54:27Z→最早May21 00Z；同DOI findable/arxiv.content registeredMay21 02:27:35Z（DC_DEEP4），联合界落BJTMay21。

方法：预先从成功trace合成可复用工具代码，离线收集DOM element时延分布；online多个code plan→manifest pre/post/type检查与CFG cost（LLM调用+循环惩罚γ10）→最低cost计划；另MonteCarlo比较serial、分task并行及first-of-k hedge，后两者都有开销。不是一次生成代码就免观察，也不是MCP规范本身证明状态语义。§3.1写post_i⊆pre_next而Alg1用s⊇pre；Alg1状态只union post不删除被替代事实，无法据此认证任意非单调DOM状态变更。因此静态检查/原子副作用/任意安全保证不采用，缺省optional runtime predicate不能补成真实强验证。

37任务/5个simulated网站（REAL27、WebArena10），每配置3trials；REAL每app3原任务+6手制，使serial/parallel/hedge最优各3，非自然任务人口，WebArena仅planner。基线BrowserUse+cache与JIT差异可分但模型/tool接口仍不同，headline10.4x不普适。H基础设施与模型、offline tool合成25–90min+trace25–45min（并发可20–30）计入；fixed策略能在特定模型更快/准，Oracle最低latency并非最好accuracy。UI更新/随机反爬会失效并fallback泛工具，未验desktop/mobile；只比较受测online路径，不授真实生产吞吐/SLO或外部操作安全。

Books对读Ch81编译执行/SQL优化段及Ch80/82交接：已有“编译不产真值、动态代理下推”等论点，但未具体承载“缓存工具代码计划与element-latency分布分别形成两级缓存，按serial/partition/hedge比较实际执行安排”的分工。拟唯一`AGENT-WORKFLOW`，在SQL编译与局部声明式子程序段之后、下一个现有标题之前两段。prepared未写。

逐字窄稿：

> 面向反复访问的同一应用，编译还可以分成两级缓存：从已有成功轨迹合成带类型及前后状态声明的工具代码，再独立保存界面元素交互的时延分布。在线先生成若干代码计划，按模型调用、循环和工具费用选出候选，再根据预测的元素使用比较串行、任务分割并行或冗余竞速的执行安排。这里复用的是受版本约束的代码与统计，而不是缓存一次计划的成功结论；[有限Web原型](https://arxiv.org/html/2605.21470v1)提供这种计划选择与执行排程分开的路线，不把编译名称变成最优性或正确性证书。
>
> 缓存代码会继承旧DOM假设，时延分布也会随环境变化；前后条件若只累加事实而不表达旧状态失效，就不能认证非单调的界面转换，静态通过之后仍须独立核实际结果。冗余竞速还可能重复产生外部副作用，最低预期延迟不替代隔离、幂等与提交资格。离线合成/采样、全部候选、冗余执行及失效重建都计费，受测任务中固定策略亦可在某一质量或延迟轴更好；不能把人工平衡任务集上的online均值推广到新应用。缓存或观测失配时回到重新观察、泛工具与串行执行，只将仍可验证的局部计划继续下推。<!-- source-family:SF-2026-ARXIV-2605-21470 -->

本人注拟保manifest包含方向/union-state反侧、task人口/离线费用/DOMstale/未核真实执行；prepared待rootSource/owner/PRE及实际POST。

## A11 LTC 与 Stream3D 必要 Source（prepared）

### 20683 LTC

`2+1+2=5`，local CORE20683精确v1，实际§3、§4/4.1/4.2、Fig1–4/Table1与总结。Adaptive-average pooling只在选定中间层压邻近token，前层保原query-document交互；listwise保instruction/query并用document mask禁止跨doc合并，之后更新position/mask。Qwen3-0.6B-Base28层pointwise与Mistral7B32层listwise（20docs/step10覆盖BM25top100）；MSMARCO训练三epoch，pointwise CE、listwise LM+ListMLE/LoRA16；DL19/20/BEIR6，L40S测QPS。不是training-free：zero-shot压缩在激进早层会严重退步。ArguAna所有rerank低于BM25，较强压缩有quality反退，轻压缩regularization只是解释假设；不存在普遍最佳中间层或无损保证。硬件之外batch/precision/concurrency/SLO未披露，无法将QPS换真实尾延迟。拟仅报告：本项5分局部部署工作点与具名训练/层位证据，未据其扩大长期通用最佳布局；不冒称Books已覆盖。若root认定特定先交互再压缩需进Ch76则定点对读。

### 21472 Stream3D

`2+1+2=5`，local CORE21472精确v1，实际§3/Alg1、§4.1–4.4/Tables1–3。固定prior与一次warmup attention提议per-token view evidence，以token-wise top-D保存score+frameID，再按占槽计数选全局top-K frames；每chunk full multi-view生成用freshnoise/按view加权velocity。D是每token历史深度，K是当前消费bundle，不是同一个预算；必须仍能取得selected原frame/feature，`2QD scalars`不包含图像/feature及生成驻留。固定prior避免评分随生成noise漂移，不使attention成几何真值。历史slot分数单调不证明global-K bundle对每个token或3D质量单调，聚合换frame可丢某个token唯一证据；不采用“不能退化”强保证。

H100/SAM3D，DA3估pose/depth，GSO/NAVI stream100frames；main设D1/K8，T3 highlighted D5/K8与主数值接近，设置口径有张力不把两者混用。D3/D5/D7和K4/8/16非每指标单调；T1 NAVI appearance各分项实际均ours最佳，原准备中“baseline分项更好”系作者误读已删除，不制造反侧。多视input/生成费、warmup、原frame与memory更新都计费，未披露precision/batch/并发/SLO，不能从score/index矩阵推出整服务常量内存。拟仅报告：5分对应受限缓存选择器，固定noise/索引与consumer分工有价值，但不将未验证质量单调或完整constant memory当长期结论；本次不声称已有覆盖。必要的原文强保证反例提交root复核，不能以低分免除。

## A12 DAR 与 GaussianDream 必要 Source/具体 Books 判断（prepared）

### DAR 20708v1

实际CORE §3、§4.1–4.2/Eq1–7、§5.1–5.5/T1–4、AppendixC/F，`2+1+2=5`；因具体cross-depth/timestep布局差额补owner/PRE。v1May20 05:07:15Z→最早May21 00Z→同DOI arxiv.content/findable registeredMay21 02:09:33Z（BATCH13），联合界整段BJTMay21。不是non-increasing，是不再单一running residual固定累计的非增量聚合；对历史sublayer输出RMSNorm作keys，static、显式time injection或input-dependent动态query作softmax混合，chunk仅保过去末层summary+当前rawsources，final aggregator又额外开放最后chunk原输出。空间式省略token人口不等整训练内存常量。

ImageNet256/SiT-XL2，batch1024/bf16/H20；重训SiT/REPA，50k samples、默认250NFE，CFG1.5分别看ODE/SDE。dynamic751M非static675M，SiTPlus虽匹配参数仍不同训练iteration；8.75x是iterations不是wallclock，baseline单step对照未给。Table1SDE+CFG static2.23反低于SiT2.06；§5.3把Table2误指Table3，不影响可读time ablation但不能混数值。§5.5给定log成本的极小点不证明真实FID最优chunk或模型随深度必增益，不采用该理论外推；大规模QwenImageDMD只初步，不采用普遍主干/后训收益。probe、gategradient与cosine是诊断，不唯一证明梯度机制。

Ch24已实际对读每轮主干选择、register双流与内部latent人口段（173–188）及Ch23/25交接。既有正文未说明同一DiT内按noise时刻重选历史layer输出；唯一`MULTIMODAL-GENERATIVE-PARADIGMS`，拟卷积/DiT共存段之后、register双流之前一段（未授lease不写）：

> 即使保留同一Attention主干，层间路由也可与外层去噪schedule分开设计：不再只把所有旧输出以单位系数累加成一条residual stream，而让当前层以历史子层输出为来源，经归一与softmax选取混合；query可显式读取noise时刻，也可从当前带噪表示中提取这份条件。为控制驻留，较早层可压成chunk summaries，当前chunk保留原输出，但summary本身也丢失细节。一个[有限DiT分支](https://arxiv.org/html/2605.20708v1)提供这条按深度与noise时刻选择历史的路线，不把非增量聚合误写成单调不增。它增加来源activation、路由及训练费用，最佳chunk和query不能脱离artifact照搬；较少训练iterations、可解码time或更平滑梯度不等完整费用或质量普胜，部分guidance/sampler配置仍由原SiT更好。表示、质量或净费用失配时保留固定residual、原skip结构和已验采样器，不以一个代理成本极小点给真实FID或大模型扩展签保证。<!-- source-family:SF-2026-ARXIV-2605-20708 -->

### GaussianDream 20752v1

实际CORE §3.1–3.4/Eq1–11、§4.1–4.4/T1–4、AppC–F；`2+1+2=5`，具体已有覆盖判断深入。v1May20 05:51:30Z→最早May21 00Z→registeredMay21 02:10:36Z（BATCH13）；联合界BJTMay21。三时点t-10/-5/当前由VGGT/TGE读成1024prefix；当前Gaussian重建+future center displacement辅助head只训练用，future复用非位置属性；policy仍消费当前观测/语言/state与prefix，不在线render/plan。AppC监督来自DAv2或simdepth、RAFT/Farneback+intrinsics backprojection，valid mask不消除伪深度/flow偏差，也未使当前prefix成为真实3D状态。训练有两stage+额外teacher/heads，移除head不等在线无encoder/TGE费。

LIBERO每任务50demo/50trials，RoboCasa Human50/24task/每task50trials；exact-v1平均52.6%（不混v2摘要54.8）。GeoPredict Doors/Drawers75.1>65.2、Others62.4>52.0，LIBEROLingBot平均98.5>98.4；无普胜。AppE/F双camera/leader-follower但realtrial分母、hardware inference GPU/precision/batch/SLO未披露，34.4→50.0不足安全保证；单分量ablation未控制全部资源或唯一因果。

拟具体已有覆盖`MULTIMODAL-EMBODIED-VLA` Ch26：`Privileged 3D Teacher 可以留在训练期...`192–209已承载几何teacher/pseudo target塑形表示、部署移除head≠实时几何；`Future-to-Action...`585–594及16666机制段明确future训练信号/在线future必要性/因果使用三分。Gaussian当前+未来Gaussian heads是该分工受限验证，拟采用命题未迫使改原接口或结论，不复制Gaussian专名/1024布局入正文；不是仅凭主题映射判已有覆盖。待root实际Source与两具体原段复核，尚不预签。

## A13 SPpruner 20950v1 必要 Source（prepared）

实际CORE §3.1–3.5/Eq1–7、§4.1–4.7/T1–7/Fig3–4、AppA与B3，`2+1+2=5`，原理论强保证具体反证深入。日期v1May20 09:37:53Z→May21 00Z→registeredMay21 02:15:18Z（BATCH13），整段BJTMay21。FIM是minmax norm+query cosine之和（修准入表“×”符号，不是乘法）；focal topK后CASSM用与focal平均相似/候选差异及query关系补context，SRS调stride，免重训。因不能由规范化特征相似推出真实关系保留，本轮只认可有限两阶段selector，不用bio-inspired命名给其解释权。

§3 Eq6 stride∝δ但AppA Eq11 stride∝1/δ，正文与证明方向不一致；AppA只在预先假定Hausdorff-Lipschitz的模型上重述subset距离界，既未验证真实位置敏感Transformer满足该set假设，也未从FIM/SRS证明任意token距保留集的小ε，不能采用无损或理论保留保证。22bench，LLaVA1.5/Next7B、Qwen2.5VL32B质量与7B计时分开；Table4只是prefill，MMStar50.7<原62.9，Table6video部分分数下降，与§4.4lossless直接冲突。预算/层位/focal8局部调参，不能写普遍最优；GPU/precision/batch/concurrency/SLO未在本必要域披露，不填造。额外norm/cosine/scan与原视觉encoder费保留。

拟仅报告：准入的新context恢复启发在受限workpoint有对照价值，但方向不一致阻止采用准确SRSrecipe，set假设不支持长期无损结论；本轮不把该算法写为新通用结构保证，也不冒称现有Books完整覆盖。若恢复一致Eq6/11和实际index/position实现，再定点重开selector设计；理论强保证的具体反证请root独核。

## A14 Insights Generator 21347v1 必要 Source/owner/PRE（prepared）

实际CORE §3.1–3.6/Alg1、§4.1–4.4/T1–2、§5.1–5.3，`2+2+3=7`。精确v1May20 16:13:53Z→May21 00Z→registeredMay21 02:24:40Z（BATCH13），联合界BJTMay21；后续版本不自动计本日修订。Scout在样本提假设，Investigator跨population结构化extract/compare并返回confirmed/refuted/inconclusive，orchestrator决定迭代与停止；schema cache有null、value、correlation，短traceID联结原记录，raw trace工具可读不等直接全量塞context，提取与汇总仍可能错。

LLM judge Opus4.6，HLE250/SSB296、每方法三report，union-gold来自同一所有系统产物聚类，不独立完整gold；coverage IG91低于Trace2Skill97，却pairwise更好，不能以一平均轴普胜。人类干预主评价SSB250holdout、每arm6人×3runs、blind分配/固定工具与时间；IG57.4 vs43.2与SEM支持该小人口效用，不普遍人类或新域保证。12专家/23insights评分4.25/4.22无显著差，不能用LLMjudge替人类确认。自动patcher各report系统终点.81–.84接近，purepatcher.8→.58只是该轨迹反侧，trials不足未给全部方差。一次分析均$76/48min vs其他$23–38/20–37min，约6runs；不是免费智能观测或生产SLO。

已对读Ch69 Sampling、root-cause/repair（224–252）与Ch68/70交接，现有跨trace manifold是异常定位，不是“样本发现假设→同corpus验证→独立下游修复效用”的两层评价差额。唯一`PLATFORM-TRACE`，拟`从 Linear Trace 到 Root-cause Graph`前两段，未授lease不写：

> 调查对象变成整个人口时，还应把“在哪些trace里发现模式”和“用哪些trace检验模式”分开：先由样本提出可反驳假设，再通过结构化提取与cohort比较返回支持、反驳或未决，并让每项结论能映回原trace身份。Schema统计与短ID降低上下文和引用负担，却不使缺失值、提取结果或成功/失败标签变成无偏真值；同一corpus里的再次检验也不是独立外部验证。[有限群体诊断系统](https://arxiv.org/html/2605.21347v1)采用这种发现与调查分工，而不是用读过更多轨迹或生成更长报告证明根因。
>
> 诊断报告还须接受两种不同验收：证据与覆盖评价检查它是否说对，独立下游任务检查它是否帮助人或patcher改善系统。把各分析器输出汇成union参考能比较相对覆盖，却不能恢复所有未发现模式；LLMjudge偏好、人类评分与实际修复收益也可能不一致。有限专家干预的收益仍受小人口、任务域与固定时间预算限制，自动patcher的终点接近也不证明某种角色分解全面更好。抽样、提取、全部模型调用、验证、存储与修复回归均计费；证据不足、population漂移或净效用不合时保留人工抽检、固定cohort与原scaffold，不由分析器自行标记confirmed批准生产修改。<!-- source-family:SF-2026-ARXIV-2605-21347 -->

## A15 官方负面信号与资格纠错

- `2605.21235v1 LamPO`：当前官方ABS119/136/170/180–181实际载withdrawn/removed。管理员说明submitter无权同意license、authorship disputed并redacted。按合同撤回版本不准入、不评分、不进入Books；A6历史题摘准备只作纠错轨迹，不留作候选。PDF网页解析虽可读，localHTML/PDF为移除页面或404，不再为其恢复附件，也不以原方法作正面证据。全部现有SUP_ABS exact-v1本次实际检索withdrawn/removed/retract，仅此项命中；不是全站无标记保证。
- `2605.20201v1 ProxyCoT`：实际ABS v1为Apr6 16:44:17Z，不是旧发现元数据所示May19；提交最早公告界与May21登记跨日，需官方May21公告/同身份正文公开证据才能列确定本窗候选。方法§3–7已实际读可保恢复证据，但不先评分/用Books采用绕过日期门，不无限追全球渠道。

## A16 LTC 修正后的具体差额/PRE（未写）

root实际Ch76 Reranking635–686和Ch75/77交接，未有先query-doc交互再中间层邻token池化、listwise文档边界与layer×ratio×training联合条件。5分但已确认具体缺口深入，取消A11仅以“没有通用最佳层”为Only理由。首句`Retriever 优化高 recall...`之后/原图对重排段之前拟一自然段：

> 交互式reranker的压缩位置不能直接照搬独立embedding encoder：可以先让query与document在较完整序列上交互，再在选定中间层平均池化相邻token，缩短后续层的工作集；listwise仍需保留指令、query和各文档边界，禁止一次池化跨文档混合，并同步调整mask与位置。一个[有限重排对照](https://arxiv.org/html/2605.20683v1)比较层位、压缩率与训练：较晚的轻压缩可以只在推理启用，激进的早压缩却明显损害未适配模型，不能把bi-encoder的入口压缩条件平移到cross-reranker，也不宣称所有配置必须重训或存在通用最佳层。池化、adapter/位置处理、训练和完整候选重排都计费，部分语料甚至由原BM25更好；排序质量、输入身份或净时延失配时，保留较晚/较轻压缩、原完整reranker与初检路径，另验最终证据支持，不以少tokens或局部QPS认证端到端SLO。<!-- source-family:SF-2026-ARXIV-2605-20683 -->

## A17 MXFP4 20402v1 必要 Source/具体已有覆盖（prepared）

实际CORE §3.1–3.3/Eq1–3、§4.1–4.3/Eq4–5、§5.1–5.3/Eq6–10、§6.1–6.2/T1–3；`2+2+2=6`，理论路径归因未闭需深入受影响域。v1May19 18:59:26Z在18Z后→最早May21 00Z→registeredMay21 02:02:19Z（DEEP4），联合界BJTMay21。以ideal连续scale的Q*定义scale/DZ/grid三项，DZ与其余点对点不交，scale/grid有cross-term；三个component norms不能直接加成总MSE。固定该定义的grid不随actualscale精度变，不等任何更改量化器后的不可降误差地板。

§4将Q输出当γ乘原/理想层输出、STE跨层norm视为未归一乘积，并未由block rounding/attention/residual/LN Jacobian推出；δ非中心sum与正文两侧围绕1的梯度ratio也不一致，不采用指数梯度误差界、zero-mean grid只改temperature、dense/MoE冗余唯一因果。方法是QDQ emulation不是native W4A4性能；MBS缩scale、OF两次residual量化（额外存储/计算）、AQN额外Gaussianweights noise，不把成熟修正再发明。GSM8K/Qwen2.5-3B(2H100/FSDP2/4samples)与Qwen3-30B-A3B(8H100/Megatron/2samples)，GRPO batch64/maxresponse1024，TIS dense5/MoE2，dense TIS2下修正会collapse；不同模型不能隔离expert routing因果。Table2完整stack210s/step>baseline156，Table3 549>420，较小qualitygap不等净加速；repeats/CI及生产SLO未披露。

Books实际Ch31 838–847已经同身份marker20402，正文明确rollout分布/rewardranking/update误差分路径、局部高精度回退与量化质量gate，随后TRACE段承载局部量化误差小≠两路径更一致。拟采用命题由该正文真实承载，不复制三分法及未闭强推导；已有正文旧“exact-v1 §5–6分解/§7实验”定位不准（当前v1分解§3，实验§6），仅请求root核准窄纠正出处定位，不计新增整合。原有效机制段不重写，不把同identity出现在Books当本日事件已去重。

## A18 Lost in Fog 21446v1 必要 Source/owner/PRE（prepared）

实际CORE §3.1–3.4、§4.1–4.3/T1–9、§5/5.1–5.2；`2+2+2=6`，解释代理失效具体反证深入。v1May20 17:34:02Z→May21 00Z→registeredMay21 02:27:01Z（BATCH13），联合界BJTMay21。AlpamayoR1/Qwen3VL10B、1996clip×8合成同步camera扰动、64waypoint/6.4s openloop；CoC exact-match改动与clean-vs-perturb L2相关，不是碰撞率。重复clip相关性与8 attack聚合不能当15968独立事故样本；4级noise拟合不是校准生产线性风险律。强noise下unchangedCoC仍偏移8.6m，paired-clean不是部署可得reference；temporal/surrogate监控只是未来方案。

CoC开关是max512tokens vs1token，保samecheckpoint/seed但改变计算与生成budget，不能签解释因果改善；cleanbaseline是constantvelocity不是learnedplanner。A10040G resident/precomputed扰动8–15s/sample远非10Hz真实服务；precision/batch/concurrency/SLO ND，约60GPUh主+ablation与真实传感/回归费用保留。Table9无preprocess经Bonferroni显著，总体平均改善与mild组更坏可并存，不据此推荐alwaysdenoise。

已读Ch26`从语言推理到 One-step Meta-action`完整1108–1118及Ch25/27交接，原段有proposal≠commit与Think控制，但未有“clean配对解释一致性不能迁移在线、稳定语言仍失知觉”的具体诊断反侧。唯一`MULTIMODAL-EMBODIED-VLA`，拟meta-action前两段后/原251224426诊断段之前一段（未写）：

> 若用语言解释监控感知退化，还要区分离线配对信号与部署可得证据：同一场景的clean/受扰动两次预测可以比较解释是否改变，再与轨迹偏移联合切片；上线却通常没有那份clean参照，跨帧比较也同时改变场景，不能直接复用离线检测率。[有限驾驶压力测试](https://arxiv.org/html/2605.21446v1)中，严重退化下解释不变仍伴较大轨迹偏移，语言流畅或一致不等感知可靠；把解释输出上限从512token改为1的对照还改变计算budget，不能独占解释的因果作用。合成单帧/open-loop偏移不是碰撞率或闭环安全，拟议temporal/surrogate monitor仍需单独验证；采集、扰动、双路推理、参考保存和真实控制回归均付费。参照缺失、感知异常或时限不合时，保留原传感质量检测、重新观测、降速/停止与独立controller，不让一致的自述签发物理提交。<!-- source-family:SF-2026-ARXIV-2605-21446 -->

## A19 AgentAtlas 20530v1 Source/具体差额/PRE（prepared）

实际CORE §4/6/7.1–7.4/8，`2+1+2=5`，label-menu测量差额深入。v1May19 22:05:12Z→May21 00Z→registeredMay21 02:05:20Z（BATCH13）整段BJTMay21。只采用同1342个synthetic items在taxonomy-aware/blind两prompt下的诊断协议，不采用引用的外部排行榜当本文实测。684control/400trace/258security由单Opus4.7生成gold、无人类校准；blind是substring+Haiku fallback，mapper正确率未测，菜单消失与输出映射同时变。8model×3split×2mode单run，三轴排名不一致不等真实deploy选择；security rarelabels n3/n7不作分项可靠率，step exact/±1边界未定不采用。localvLLM与闭API配置混合、hardware/precision/batch/SLO ND，数据/推理/mapper与独立标签审计均计费。

Ch66已读114–121参考/rubric偏差及rating/classification白盒干预、Ch65/67交接。旧段研究judge的readout/格式，未明确closed-menu给被评诊断模型答案空间线索与blind映射这个额外scorer。唯一`PLATFORM-EVALUATION-SYSTEM`，拟现格式敏感circuit完整段后/形式验证前一段（未写）：

> 诊断能力的评价还要把“给出类别菜单”和“自由发现问题”分开：在相同trace或任务状态上，一路提供封闭label集合，另一路只收自由文字，再独立审查把文字映回类别的规则。前者缩小答案空间，后者新增parser或mapper，两路差额不全是模型失去诊断能力。[有限协议演示](https://arxiv.org/html/2605.20530v1)同时显示prompt模式和评价轴会改变排序，却由单一生成器给gold、未有人类校准且mapper误差未测，不能把合成标签agreement叫真实控制可靠率。应保存菜单、输出、映射失败、gold来源与各轴人口，额外生成、推理、fallback和独立标注均付费；映射或标签未验时保留配对原输出、人工核验与Unknown，不按单一aware分数或拒绝率批准部署。<!-- source-family:SF-2026-ARXIV-2605-20530 -->

## A20 PlanningBench 20873v1 Source/具体差额/PRE（prepared）

实际CORE §3.1–3.6、§4.1–4.2/T1–5、AppC/F，`2+2+2=6`，可验证训练数据与评价反馈具体差额深入。v1May20 08:10:15Z→May21 00Z→registeredMay21 02:13:28Z（BATCH13），整段BJTMay21。task/constraint taxonomy→采约束→Generator出题+checklist→Responder作答→Critic检验；当前responder全过才向medium/hard调概率，bounded countprojection并不保证difficulty可跨模型比较。所谓automaticverifier是GPT-oss120B promptjudge，不是所有实例形式solver；20人审batch86.15%无需/小改、13.85%改source，不能由无discard断言全正确。467eval，Qwen30BA3B responder，Allpass与Avgpass测不同事件。

train300items/GRPO batch128×50epochs/8rollouts，lr2e-6/KL.001；同size不等同token/出题/人审预算。HumanAuthored与SynNotDetOptimal改变整套分布，不独立识别determinateoptimum唯一原因；SynNotDetOptimal在InverseIFEval退步是反侧，其他迁移只受限支持。同judge训练与评价有共同偏差；hardware/precision/seedcount/CI/SLO本必要域未披露，不填造。含temporal/stateful任务不等真实环境执行。

Ch66开篇EvalSpec、49动态interviewer/53压力搜索、形式spec后置条件已实际对读：有题/判题身份，但未将当前solver通过后改constraint组合与同checklist成为训练reward放同一链。拟唯一`PLATFORM-EVALUATION-SYSTEM`，在interviewer独立marker之后/现两阶段pressure search前一段（未写）：

> 测试集也可由约束空间生成，而不只向固定题库增补条目：先声明任务模板、资源/时间/状态约束与instance checklist，再用当前responder的全通过信号提出更难的约束组合；部分通过率、整题全通过与指定最优目标应分别记录。同一checklist若又供RL训练奖励，出题、难度反馈和reward的误差就会耦合，[有限规划数据研究](https://arxiv.org/html/2605.20873v1)里的promptjudge并不因此成为形式solver。更确定的目标与较好迁移只是受限整套数据对照，不能把不同数据人口的差额唯一归给最优解收紧；通过当前responder也不是跨模型共同难度。模板/约束、全部生成和critic、人审修正、rollout与独立holdout均计费；规范歧义、judge或迁移失配时保留固定人工/solver可核题集、原reward与未参与难度反馈的评价，不让自动全过自行批准题目或模型。<!-- source-family:SF-2026-ARXIV-2605-20873 -->

## A21 StreamGVE 21466v1 Source/具体差额/PRE（prepared）

实际CORE §3.1–3.3、§4.1–4.5/Eq1–10、§5.1–5.5/T1–2，`2+2+2=6`，条件与sampler接口差额深入。v1May20 17:52:10Z→May21 00Z→registeredMay21 02:27:29Z（BATCH13），整段BJTMay21。该v1标题与正文StreamGVE，latest改StreamEdit不静默替换。source固定cleanendpoint按每step共享noise加噪，target由cleanprediction再加噪；source不是自己的反演轨迹。selfattention中Q/K随timeblend，current/previous keys保两branch身份，sourceKV延到低noise，trigger-word crossattention差生source/targetunionmask并boost。sourcevelocity与known interpolationvelocity差仅启发guidance，不是target真实error；AMNmask不当真实背景分割，不照录Eq8分母索引/精确samplingrecipe（Eq2中(1-t)索引亦不整齐）。firsteditedframe是额外条件，非自动无用户信息。

SF/LongLive frozen、singleA100，standard15steps/long5，NFE=2×(steps+1)还需cleanpasses，免训练≠一份forward。FiVE100video/420editpairs，部分baselineH100officialnumbers，firstframe产生时间不计，不能以T1秒帧跨硬件归因或签实时。T2去SAB FiVEAcc67.74>full51.94但background明显坏，去SOG53.58>51.94，清楚是编辑自由/保真取舍非全指标优胜。long21cases/20participants只局部偏好，duration/scene变换边界与precision/batch/concurrency/SLO ND。未核代码/看全部视频，不把文字图注写成已观测输出。

Ch24 117–139具体cleanhistory/少步训练与现编辑参考条件段已对读，未有把原视频作为逐step重新加噪source、与target共享noise但保持不同endpoint的fastediting路线。唯一`MULTIMODAL-GENERATIVE-PARADIGMS`，拟2604-10103完整marker后/14382 teacherhistory段前一段（未写）：

> 流式生成器还可把原视频当作每一步都重新构造的条件，而不先反演它再沿原轨迹编辑：source分支从固定clean帧与本轮noise插值，target分支从自己的clean预测与同一noise继续；分别保存两路历史，再让source/target的Q、K混合及低noise阶段的sourceKV为生成提供约束。两路noise共享不使endpoint相同，trigger-word attention提出的编辑mask也不是物体真值。[有限少步编辑分支](https://arxiv.org/html/2605.21466v1)因此把sampler接口与条件注入分开验收，而不保证编辑区外严格不变。它仍支付双路求值、clean pass/KV、mask及可能的首帧编辑；少NFE不等实时，移除保真约束还能提高编辑成功代理却损坏背景。原文跨硬件秒帧和未计首帧制备不能证明净加速，sourcevelocity残差也不认证target真实误差；保真、编辑语义或预算失配时，保留较强原条件、较多步数/原编辑器与逐段回看，不把流式或免训练名称当无限稳定与无损证书。<!-- source-family:SF-2026-ARXIV-2605-21466 -->

## A22 有界标题查漏尾的准入校准包（发现封口；R20/R22校准已通过）

A5精确窗口191主题标题实际浏览；对两原Report做精确ID查询，有75个ID出现、116未出现。这只是去重定位，75未做本轮重审，116不构成全量逐项关闭队列。对其中32个可能改变生成、表示、训练或系统判断的具名标题实际读了完整官方exact-v1题摘（相应SUP_ABS原件），不继承旧日论文池。`decode_json(<>)`曾因list context误消费后两文件，输出0dup无效；已以先scalar读取修正为75/116，不把失败计数当结果。

新增潜在贡献继续核验（尚未评分/签日）：

| v1 | 原约束 → 实际增量 → 需重考虑的选择 |
| --- | --- |
| 20364 TTCW negative | 固定14维审阅输出受reasoning target干扰 → 同任务reasoning/非reasoningSFT比较出现parse/repetition失败 → 解释监督与结构输出目标可能不一致；仅文学领域增分不足，拟采用的是协议反侧 |
| 20624 AVIS | 整段inverse solver首包延迟/多VAE一致性费 → AR分chunk且Flash只首chunk做measurement consistency → 生成历史连续与逐chunk观测一致性不能互保 |
| 20209 NaP | diffusionpolicy逐步testtime gradient贵 → RL直接选prior输入noise，训练真实env反馈 → 约束费用从采样内迭代移到训练/支持域；v1Apr15，日期跨日未过不先列候选 |
| 20251 ProcBench | outcome漏processdefects → 统一trajectory+calibrated risk scorecard → 校准后风险与缺失观察/原始缺陷可区分；v1May18，日期跨日未过 |
| 21372 AutoScale | 固定real/synthetic混合域偏 → GraphRAE表scene、ClusterGA重权、闭环NavSim反馈检索 → 混合人口随验证更新的过拟合和费用需分账 |
| 21131 UniT | 在线单frame/离线多view接口割裂 → groupAR、anchorfree关系与queueKV、scaleadaptive loss → 组粒度、历史淘汰和米制尺度分别校验 |
| 21059 PairwiseModalities | 只有成对数据不保证联合latent可识别 → 给可识别条件、partialalignment/minimal latent与crossmodal recomposition → 无完整多向配对时哪些共享因素仍可迁移 |
| 20433 SOTA | 普通tri-modal attention不约束attention边际 → force/pose subqueries与visualpatch entropyOT、显式marginals → 空间选择结构prior不同于真实接触语义 |
| 20674 CoMET | 新模态常默认端到端适配 → 冻结encoder+PCA+TFM，CLStoken失配用PALpool → 消费接口/数据尺度可使不微调成为有对照分支 |
| 21130 VersusQ | pointwiseVQA分数随dataset尺度 → pairwise连续signedmargin与marginGRPO → 排序与幅度/跨域标度不可互签 |
| 21261 STiTch | composedcaption多带reference无关细节、pointpair漏多对应 → latent transition+双向settransport检索 → caption修订与matching支持分别检验 |
| 20777 AttriStory | 人物identity保持不等属性绑定 → earlylatent attention attribute-object loss及分开attributebench → 属性关系与人物一致性是不同gate |
| 21090 TextSculptor | 合成target常改背景/字形 → 程序render/composite配对、OCR+VLM+背景多轴评价 → 数据对应与最终字形/编辑区域分责 |
| 20942 CRS | roadQA语义推理与图结构脱节 → recursivegraphqueries产生可追踪CoT/QA → label traceability与真实路况/数据监督接口区别 |
| 20502 EncMin2L | 单encoder覆盖不了各shift → ID-only specialization诊断+twolevelmin/校准p组合 → 多encoder的校准与共错不是一个AUROC |
| 20551 WeiToP | retrievaldescriptor压缩不减frontencoder费 → 以aggregation importance自蒸馏earlytokenpruner → descriptor和feature费分开，可按部署预算调压缩 |

有决定准入含糊者，只补决定机制的核心后停止：20717 E-ReCON interleaved10T/28Tadder与CNN/SNNbitcell，需说明是否形成foundation计算主线新约束而不是器件数字；21081MusicalAttention需核metadata怎么改变一般attention，不以音乐指标或新feature列表入选；20977P-SWA需核diagonalwavefront依赖/codec边界是否为可迁移生成接口，不以codec单数字入选。其余13个完整题摘明确排除，另列20618一个标题级关闭（不在32份完整题摘之内）；共14个身份的具体层级和理由如下，供root分层抽检：

- 20254TableQA：TGN三module与PIP列/行prompt把已有structuredread分步，没有新可执行语义、验证机制或既有失效界；20618COAgents同样只路径搜索agent框架/局部routing，未建立foundation主线改变（后者标题明确，未称完整摘要已审）。21027EnterpriseAPI把intent/权限/query/图表做policyaware串接，90usecases指标不揭新执行机制。
- 21442torchtune：当前题摘只modularity/hackability/builders/recipes及与框架性能，未指出既有公开library之外的新机制或可比条件下新tradeoff；不因论文首次归档重计早已公开library事件。21404十二paperdisclosure audit五field/schema/codebook是成熟复现要求的一次singleauditor盘点，未给控制变量下的结论修正或新评价机制，低disclosure不等不可信；不以高缺项率本身准入。
- 20532RBF：edge surrogate与HPC simulation异步更新在农业CFD应用，未说明新的模型/训练资源控制机制或主线外基本突破，不能以inference/latency标签重引科学应用。21299条件句人类pragmatics/四语言比较是语言认知任务差异，不提出模型形成/系统设计可核增量。
- 20818Ego4D：OSGNet候选后MLLMrerank为已有两阶段组合，冠军名次不签新机制。20809annotationguideline迭代moderation为NER已有流程复用，无明示新机制或反常条件。20584QwenSafe为AppleCRD应用的合成QA+SFT/DPO，descriptor分类指标不建立通用表示/对齐新机制。
- 20577Mahjax：Riichi规则全向量JAX环境与GPUrollout并行，题摘未提出新并行/状态语义或foundation学习边界；不是因游戏题材排除，而是只平台化已有向量执行和steps数。20370Clove：JVM对象hotness/relocation服务通用CXLmanagedruntime，未形成foundation训练/推理内存的直接证据或主线外基本突破。20467HornLogic：triplet anchor重复term、难度平衡/hardmining是既有训练策略在逻辑embedding应用，未揭新的学习原理/适用界。20194parallelconceptual：语义chunk并行+证据合并是成熟workflow，仅声称指标未改变执行/验证机制；v1Apr4日期无必要再追。

以上排除无当前可见withdrawal/设计纠错信号；32个官方ABS实际检查相关标记与v1记录无withdrawn命中，非全站无标记断言。必要Source只按root校准后的具名潜在机制继续，不把32或116全部转全文。

## A23 Hy-MT2 结构打包 Source/具体owner/PRE（prepared）

实际LIST_SCRIPT的点击函数调用`B(`/research/${e}?langVersion=${y}`)`，选择器`j(e)=e.customUrl||e.id`；zh列表id100041的customUrl为空。因此原文真实路由为`https://hunyuan.tencent.com/research/100041?langVersion=zh`，不是由文章ID猜测URL。下方PRE的基础路径随实际写入同步带上该query；正文恢复来自同一官方publicDetail API，不声称浏览器已成功呈现。

原件`SUP_HYMT2_DETAIL_20261020.json`为实际publicDetail中文id100041，官方当前body全文读；`SUP_HUNYUAN_API_ZH_20261020.json`zh total11/list11与en9/list9，真实script说明POST/publicList参数pageNum1/pageSize20/renderType0（全tab），研究列表Apr30→May21→Jul6夹窗。display1779346800、published1779340747、public1779357326均北京时间May21；updated1781525719为Jun15，只标当前官方说明，不冒称May21逐字史。root R17已实际结构打包准入，`2+1+2=5`；因具体表示支持约束差额深入，不以440MB/1.5x评分。

Quantization中Sherry限定每4个ternary权重恰一zero、余三非零sign：4种zero位置×8种sign组合=32码态，可固定5bits/4weights；这是改变可表示集合，不是无约束3^4=81态被无损塞入5bits，也不保证相对原float无损。官方公开SEQ2bit/QAT+动态KLteacherconfidence是另外训练细节，未核精确weightrecipe，不混packing5bit权重本体与scales/embedding/head总驻留。正文只有A15对HyMT1.5Q4的1.5x及440MB claim，模型/精度同时变、prompt/length/batch/precisionfullpath/SLO ND，不采用纯packing因果或nativeSIMDkernel已验；量化质量退步尤其instruction约束，学徒/教师/多stage训练也付费。当前正文无withdrawal/errata说明，updated不是自动重要revision或首次公开新日。

已实际读Ch49 1190–1245存储/执行分账、250623025三值pack5trit-vs2bit、低位LUT/条件加减及Ch48/50交接，现有无约束ternary packing不承载“先约束每组可用模式，换规则短码”的特定自由度。唯一`INFER-TENSORRT-LLM`，拟现250623025独立marker后/非均匀centroids段前一段（未授lease不写）：

> 更规则的短码也可由训练时限制可表示模式换来，而不只优化已有三值串的打包：若每四个权重必须恰有一个零，其余仅取正负，则零位置四选一、三位sign共有八种，整组只有32种状态，能用固定5bit表示。这个1.25bit只对受约束的权重组成立；任意四个三值权重有81种状态，不能沿同一码表无损保存。[一份官方量化说明](https://hunyuan.tencent.com/research/100041)提供这种结构化支持与规则打包的分支，不等于全部张量、scale和kernel都只花1.25bit。它需要相应QAT/蒸馏和质量回归，也增加解码、scale、未量化算子与布局兼容责任；官方跨模型/精度的有限端侧速度比较不识别单一打包收益，某些指令约束在低位下仍退步。结构支持、质量或净执行费用不合时，保留普通三值/较宽code、成熟低位或高精度路径，不以较小码空间批准完整模型常驻或SLO。<!-- source-family:SF-2026-HUNYUAN-HYMT2 -->

## A24 每日14源有限停止点与发现封口

检查跨2026-10-20～21，始终仅补北京时间2026-05-21；以A22为最后一批具名准入包，之后不扩无具体遗漏线索的第二轮尾检。当前还需处理的A22决定性核心、必要Source与Books不是新发现扫描。以下是本轮实际入口与停止，不复用旧Report的“已检查”授本窗完整覆盖；无条目不等不存在，无历史切片不等不适用。

| 来源 | 实际入口、读到哪里及停止 | 本轮结果/隔离 |
| --- | --- | --- |
| SRC-OPENAI | Research当前页及定点May21官方检索；geometry原文May20且科学应用不纳。May21 AdventHealth仅客户采用/流程，Academy课程和ChatGPT功能清单未披露本项目新机制。原HTML访问异常，不算恢复历史Research目录。 | 检索受限：May21研究目录历史切片未恢复；不以产品/客户报道证明研究无遗漏。 |
| SRC-ANTHROPIC | Research当前10项；历史query参数e45d281a_page=3被忽略，未冒称第3页。另相关alignment/interpretability日期May7/8及Jul，GlasswingMay22窗外。 | 检索受限：May21历史Research列表未恢复。 |
| SRC-GOOGLE-AI | Research pubs实际1–15/11626，2026 facet421仅数量不是已读421；DeepMind当前Research/News为Oct/Sep。两域带May21日期的定点检索未恢复目标历史切片。 | 检索受限：不能由当期首页/年度facet签May21完整覆盖。 |
| SRC-META-AI | research当前web空，publications原始连接reset；定点May21检索未恢复官方历史列表。 | 检索受限：历史列表缺口，不作零命中。 |
| SRC-QWEN | 旧qwenlm入口重定向qwen.ai，旧Blog最新Sep2025、新Blog动态未提取；定点May21表达查询未恢复目标列表。 | 检索受限：2026目标日Research/Blog切片。 |
| SRC-DEEPSEEK | 当前官方研究/新闻列表实际日期Apr24→Jul31，Research可见Feb25→Jun24；May21状态事故不是模型研究发布。有限可见目录止于跨窗相邻项。 | 已检查该可见研究/新闻切片；不声明所有历史网站/发布渠道无遗漏。 |
| SRC-MOONSHOT | platform.kimi.com/blog实际109行，最新Nov7 2025后向旧，不覆盖2026；具名官方GitHub May21线索2336/2337/2339/2340为日常memory/session、hooks、viewer、referenceimplementation issue，不当新研究机制。 | 检索受限：May21正式模型/研究发布切片未恢复；不扩普通issue队列。 |
| SRC-TENCENT-HUNYUAN | 首查Research；真实浏览器尝试超时，随后实际加载JS恢复POST publicList，zh page1/20/renderType0 total11/list11，en9/list9；Apr30→HyMT2 May21→Jul6夹窗。publicDetail id100041恢复官方全文，实际路由见A23。 | 已检查此全tab有界API列表，新增HyMT2；当前body Jun15更新，不冒称May21逐字史或全历史清单保证。 |
| SRC-ZAI | 官方zh/research实际可见Jun16→May20 ZCube→Apr29，有限列表夹过May21；后续一次timeout不抹去先前成功。 | 已检查此可见研究目录切片，无新增May21项；不扩全站。 |
| SRC-BYTEDANCE-SEED | en/public_papers首页20项/13页末May26；page=2参数被忽略。实际script给API get_article_list_v2，article_type1/count20/page_token20/order_desctrue、x-tt-localeUS，BOUNDARY_API原件20项首CharonMay16，May26→May16夹窗无May21。Research/Blog当前仅5项，Jul31/20/8/7及undatedRealtime。 | 论文相邻页边界已检查；Blog May21历史切片检索受限，不由论文页替代Blog。 |
| SRC-BAIDU-ERNIE | ernie.baidu.com/blog/zh实际page1列May9/Apr30/Apr15→Nov21 2025，page2为更旧；在跨窗后停止，不扩全GitHub。 | 已检查该Blog有限列表，无May21新增；非全机构无遗漏。 |
| SRC-XIAOMI-MIMO | 当前Paper8条Jun29→Mar13→Feb3→Jan8→更旧，夹窗；Blog15标题未给日期、More未恢复历史页，May21检索无确定材料。 | Paper有限列表已检查；Blog日期/历史切片检索受限。 |
| SRC-MINIMAX | 英文Blog实际13项，Oct19→May27/26→Mar18→2025，夹窗；中文重定向的局限不覆盖英文已读结果。 | 已检查该有限Blog列表，无May21新增；不对未触发普通项目提交扩扫。 |
| SRC-ARXIV | 原API/export多次未恢复；正确2026-05月列表既有LG仅前2000未到May21，CL/CV未取回。后试2605路径8218bytes实际404，纠正为无效URL（不是bot或访问阻断）；四类2026-05正确路径有限重试仍0bytes timeout。DataCite精确registered UTC May20 16:00～May21 15:59:59主题查询191/page1of1为补检；标题有界浏览、A6/A22具名题摘，不变成191或116全文队列。 | 主题补检和精确日期合证有效；官方目标日分类相关标题浏览未恢复、定点Proxy/NaP/Proc跨日公开日不足仍隔离。不得称分类/全学科Coverage通过。 |

必要日期可用合同同日联合界，不因为上述分类列表失败否定已经逐项核实的同日合证。跨日三项Proxy20201、NaP20209、Proc20251仅保潜力与精确重开条件；非当前确定候选、非零命中、非正面证据。没有特定早稿线索时不追“全球最早公开”的假想渠道。此次封口仍须root独核准入/来源范围和本日DAY，作者不自行授完成。

## A27 AVIS20624v1必要Source/具体owner/PRE（prepared）

实际CORE §4全/Alg1、§5全/T1–3、AppA证明/B1配置/C4matchedbackbone。2+2+2=6，具体guidance资格gap深入。v1May20 02:16:30Z→May21 00Z→TAIL18 registeredMay21 02:07:35Z，同ID/arxiv.content/findable整段BJTMay21。CG测量初始化→encode/re-noise t0=.1/K2，latent3帧chunk；Flash首chunk逐step decode/CG/encode，其余仅KV+同measurement初始化。AppA界只比较两共享noise模型轨迹，未保证目标轨迹最终为真实chunk；δ是前块errors均值，递归仍可放大，不采用additivecontext项→跨chunk不乘性增长/稳定保证。81frames/100Pexels、4090，主480×854与B1资源480×832不补同配置；CG初始化5/50/100次、DDS5次及VAE/KV全费。H100独立，未授实时。T2deblur等保真/多任务FID旧法更好；T3更多K反退PSNR，C4只单SR matchedbackbone。未核代码/全部视频，precision/并发/SLO/seedCI ND。

Ch24 334–351 complete progressiveguidance06656→FMRG现段只管理同t likelihoodrefinement，无measurement初始化和随后按chunk跳guidance的特定分支。唯一MULTIMODAL-GENERATIVE-PARADIGMS；拟06656独立marker后/FMRG前一自然段（未授不写）：

> 观测约束还可分配到不同chunk，而不只分配到同一denoising步的内环：先按已知measurement/operator求粗一致估计，编码并加少量噪声作为每块起点；首块继续作观测修正，后块则主要读取已生成prefix，省去逐步VAE与修正。一个[有限视频恢复分支](https://arxiv.org/html/2605.20624v1)提供这种初始化与后续guidance分账的工作点，但自产KV不是新观测，初值较一致也不保证去噪后的帧仍满足measurement。其Lipschitz差界只比较受限模型轨迹，前块误差仍能经context递归传播，不能把加法项解释为无限稳定；较多步数与更强感知质量也可能牺牲像素保真。初始化CG、codec、全部采样与KV均计费，跨模型/分辨率的速度不签完整服务；观测残差、长时漂移或净费用失配时，恢复逐块/周期观测校正、较短片段与原solver，分开验收观测一致、感知质量与全部延迟。<!-- source-family:SF-2026-ARXIV-2605-20624 -->

## A28 P-SWA20977v1必要Source/具体owner/PRE（prepared）

实际CORE §3.1–3.2/§4.1–4.3/T1–3，2+1+2=5，依赖/codec概率接口gap深入。v1May20 10:06:23Z→May21 00Z→TAIL18 registeredMay21 02:15:58Z，同ID/arxiv.content/findable整段BJTMay21。重复s×s循环移位mask令每s条diagonal同step；decodedhyperprior Q/skip与pastdecodedSpatialModule1 K/V通过accumulator初始化，channel下三角mix+shift另保组因果。Spatialselfattention当前step可见而accumulator不可见的Fig2区别不混成可读未传输真实symbol；不发布未经代码核验的完整entropy-code recipe。s4/N4的实际16AR步骤非4，改mask不变模型size/perpixelcost原断言不推广复杂度免费，分辨率增加仍处理更多tokens。

训练OpenVid1M、冻结DCVC-DC featuretransform/ImageNet、12epoch256crop+2epoch可变512、batch8/AdamW，测试96frames/GOP32/UVG-MCLJCV-HEVCB。T1mixedP-SWA301ms>DCVCfp16273且hardware ND，noncontiguousreads/scatters使少MACs不等少墙钟，6.5GB/8.5GB限给定配置。T3Iweight10让Irate改善4.5%而Prate退2.8%，DCVC P-frame优势仍大；背景quantizationnoise是解释性个例，非已证唯一原因。不采36%泛化、lossless质量或任意视频drift-free；未核代码/像素/复现。

Ch24 Ising顺序20394完整两段与next-patch14041完整段实际读，现有不含固定重复空间mask、显式已传sideinfo初始化及channel分责。唯一MULTIMODAL-GENERATIVE-PARADIGMS，拟14041完整段后/表示是否易预测问题前一自然段（未授不写）：

> 并行组也可由重复空间依赖图定义，而不只切相邻patch：把空间位置按循环移位mask排成多条wavefront，同组并行预测；组起点读取已解码的side information与过去邻域，再把空间组数和channel组的自回归分开。一个[有限熵模型分支](https://arxiv.org/html/2605.20977v1)以此避免把channel都扩成tokens挤压每token容量，却仍支付sideinfo传输、空间与channel多轮、cache及非连续访存；四个空间组乘四个channel组是十六轮，不是四轮或常数总工作量。解码时可见的条件必须与encoder一致，同步隐藏状态不能偷读尚未传输的符号；本文不据示意mask签完整codec等价性。较少MACs仍可比高效低精度旧路径更慢，偏重I帧也会损坏P帧码率。依赖、实际码率/质量或总执行费不合时，保留原顺序、较温和分组与已验codec，不让局部并行直接批准任意生成器的无损加速。<!-- source-family:SF-2026-ARXIV-2605-20977 -->


## A26 TTCW20364v1必要Source/具体owner/PRE（prepared）

实际CORE §3/Validation/Table2、§4/Table3、§5/Limitations完整。2+1+2=5，固定协议反侧与具体gap深入。v1May19 18:16:58Z在cutoff后→最早May21 00Z→TAIL18同DOI/arxiv.content/findable registeredMay21 02:01:26Z，整段BJTMay21。263911rows来自Gemma再生4–8kwords故事、两个reviewer与GLM synthesis；无human，50stories×14metrics不是700独立故事，faithfulness503/coherence143/relevance681。4/8BQwen+LoRA64/128/lr2e-4/4L40S/temp0；nonreason16k vsreason32k改变context/训练targets，epoch/完整train-token/截断/seed/CI未披露，不称预算匹配或归因思考本身。14metric任一缺/错整份parse失败，nonreason训8B1/4B.9998 vsreason训thinkingon .8708/.8592；关thinking后8B.988而4B.427，推理开关不能代替监督人口验收。ScoreAcc其实exp(-MAE)，BERTScore是合成reference相似非人审质量，手工错误实例支持leak/repetition/incomplete类型，不证明全部parse失败唯一原因。

当前Ch29实际完整270–287：01702区分答案正确与轨迹值得模仿，16819对齐行动接口，均未表达训练含reasoning×推理mode交叉下固定report协议反向失败。Ch28/30交接已读。唯一TRAIN-SFT，拟01702完整段后/16819接口段前一自然段（待root实际PRE，不写）：

> 轨迹是否值得模仿，还须与最终输出协议分别验收：在必须交齐固定字段的任务里，可交叉比较训练target是否包含reasoning与推理时是否开启thinking，同时单列完整parse率、字段误差和内容质量。一个[有限结构化审阅对照](https://arxiv.org/html/2605.20364v1)中，加入reviewer轨迹后出现泄漏、重复和缺字段；训练后关闭thinking只恢复部分模型，另一个模型反而更差，说明解码开关不能代替监督与协议的配对回归。该对照同时改变目标长度与context上限，且reference完全由模型合成，不能据此断言reasoning本身有害或人类评价质量下降。教师生成/合成校验、全部监督tokens、训练与独立parser/内容审查均计费；轨迹或格式不兼容时，保留可信直接report示教、原输出协议和经核验的推导，不让较长解释或一个乘积总分批准任务可靠性。<!-- source-family:SF-2026-ARXIV-2605-20364 -->

R20准入已通过，其余尾批仅按已批准十项+CoMET决定核心继续，不扩发现。R21真实GVE/Hy两项POST已通过，当前13真I，本人注待纯行政同步，不第三Source。


## A25 尾批决定性核心/日期原件（不扩发现）

18条精确DataCite原件TAIL18已实际核meta.total18/totalPages1，全部state=findable、client=arxiv.content。registered原字段：20364 May21T02:01:26Z；20717 02:09:47；20624 02:07:35；21081 02:18:24；20251 01:58:40；21372 02:25:15；21261 02:22:36；21131 02:19:33；21130 02:19:32；21090 02:18:36；21059 02:17:53；20977 02:15:58；20942 02:15:06；20777 02:11:12；20674 02:08:46；20551 02:05:49；20502 02:04:40；20433 02:03:04。与各自ABS唯一v1核对，May19 EDT cutoff后～May20 cutoff前的最早界May21 00Z到上述登记界整段BJTMay21；20251May18 v1跨日，不能截取登记日，保留而不先算候选。20209Apr15同理。

条件项只补决定准入核心：
- 20717 E-ReCON exact-v1 §II-C完整：10T fulladder引用已有[4]，与28T逐级交错恢复passlogic电压；§II-A/D的AND-ReRAM/bitserial为CNN/SNN器件与常规映射，未呈foundation执行新接口/可靠性条件或主线外基本突破。拟贡献前关闭，不以65nm、模型小或CNN标签排除。
- 21081 MusicalAttention exact-v1 §4.1–4.3完整：六事件embedding与bar/key/tempo元信息；limitedprevious/sameattribute的手工mask来自音高/节拍/乐器规则。未呈可改变一般attention理解的机制/有效界，拟贡献前关闭；不是因音乐领域本身排除。
- 20977 P-SWA exact-v1 §3.1–3.2完整：重复s×s循环移位mask令空间相隔diagonal同step，decodedhyperprior作Q/skip、已解码邻空间作K/V初始化；将s空间与Nchannel组分开，避免channel作token使序列N倍和d受限。该依赖与model-capacity分责非普通codec指标换场景，拟准入必要审阅；没有读完主评价前不授加速或普遍常数工作量。

上述核心原件均SUP_CORE同IDv1；待root独立准入。7个早已真实POST的本人注只行政同步既成R9/R13/R15/R17并实际读回，未改变机制或发第三Source。README现为进行态，旧254/连续§4未碰，不把原Complete当本轮验收。

## A29 CoMET20674v1必要Source/具体owner/PRE（prepared）

R22决定核心准入有效，另实际完整§6/Table1–3与AppA1 compute；不遍历无关附件。2+1+2=5，黑盒consumer反馈pooling差额深入。v1May20 03:43:19Z→May21 00Z→TAIL18 registeredMay21 02:08:46Z，同ID/findable/arxiv.content整段BJTMay21。PAL support当前pooled/query单token→TFM输出分布→相对经验labelprior的logJSD分数→ridge线性θ→softmax池化，三次randomsplit；PCA只fit pooledsupport，query同变换，不反传consumer但仍拟合adapter。Alg1不写PCA而脚注实际每次有PCA；不照抄维度不明完整recipe。先局部4×4→2×2→1×1、文本按sqrt长度反权重，qmax500k/λ10k、temperature图.5/文1、pool128维与通常256分清。

Table2五seeds、best-validation iteration计时是累计fit到该轮，非固定无选参；正文nohyperparamtuning不抹去选轮。Table3PAL在Petfinder各模态均退，PF-All42.60<44.38，Wine/Jigsaw原TTT/TabSTAR更高；单模态pooler不一定保其他模态的互补信息，JSD大非语义真值或正确性。CoMET L40S/64–256GBRAM，MM-PFN/TabPFN H100/256GB，不跨硬件签净时延；所有encoder/PCA/tokenqueries/回归/TFM前向与独立验证均费，precision/batchconcurrency/SLO ND。不是无训练/泛化免费。

Ch23 214–222完整ReLope supervisedrouting及learned-inputquery13710两段实际读，缺不用反传consumer、以其输出拟合已有token pooler的特定适配接口。唯一MULTIMODAL-REPRESENTATION，拟13710完整费用/回退段后/ModalityCollapse前一段（未授不写）：

> 若下游consumer不能反向传播，已有token的聚合仍可借它的预测反馈拟合，而不必更新主干：先以当前pooler构成support，将另一半样本的单token送入同一consumer，把预测分布相对经验label prior的偏移当pseudo score，再用ridge回归拟合线性softmax池化器；PCA仅在support拟合并同样变换query。一个[有限黑盒适配分支](https://arxiv.org/html/2605.20674v1)因此区分冻结参数、可调用预测和可学习读出，免反传不是免拟合；偏离prior也不是真正有用语义或正确答案的认证。分模态单独聚合还可能抹掉互补信息，部分多模态任务比原CLS/mean更差，需用held-out consumer质量选择。编码、单token查询、PCA/回归、多轮重分与完整预测均付费；支持分布、score或互补信息不合时，保原CLS/mean、可信监督readout或可反传adapter，不以较少可训练参数批准无损与低总延迟。<!-- source-family:SF-2026-ARXIV-2605-20674 -->

## A30 AutoScale21372v1必要Source/具体owner/PRE（prepared）

实际CORE §4全/Alg1/Eq1–8，§5全/T1–4/§6、AppA3模型训练；2+2+2=6，实际mixture消费边界gap深入。v1May20 16:36:26Z→May21 00Z→TAIL18 registeredMay21 02:25:15Z，同ID/findable/arxiv.content同BJTMay21。GraphRAE历史8+未来4帧polyline只为离线scene数据索引，不偷作部署观测；GMM64cluster，成对历史train/eval轮次差拟合ridge clusterperformance，RBF跨cluster，EG提出mixture，从较优旧点评估起不保证无drift。Eq5对max r(w)的非active区仍写γ项；Eq7gain分母为0/负值未guard；更关键δcluster配额计算后retrieval全局topB Eq8仅softboost，不保证实际集合达到proposedmixture，故不采用完整梯度/约束最优recipe。

85kreal/384ksynthetic、20k独立calibration反复供5round控制；剩pool50k/100k，8A800/100epoch/bs512/2048×512无LiDAR，两planner与NAVSIM-v2 navtest12146/navhard244→4164有限simulation，不等真实道路。last10ckpt平均非10独立seed，独立seed/CI ND。T1增加100k使DiffDrive S1/EC等反退，T3各轴并非全优；四ablations小数差无CI不授单模块唯一原因。每轮从头训练、SimScale合成、GraphRAE/聚类/metric标签与评估/检索全费，少synthetics不签净compute；不采用‘representation proximity确保迁移’或闭环安全。

Ch27 176–224全部actual读，已有loss predictor17066不含由跨轮实际mixture-评价差预测cluster响应、再检索成实际集合的接口。Ch26/28交接已读。唯一TRAIN-DATA，拟17066完整段后/AlignPrune前一自然段（未授不写）：

> 配比controller还可用多轮“实际训练集合—独立calibration表现”拟合cluster响应，而不是把当前高loss直接当需求：先以场景表示聚类，再由历史轮次的mixture差与性能差估计局部响应，提出新cluster权重，并据此检索具体合成样本。一个[有限闭环数据分支](https://arxiv.org/html/2605.21372v1)提醒这里存在两份分布：controller提出的比例与检索后真正进入trainer的集合；全局top-k的soft boost不保证满足cluster配额，需保存实际manifest而不能沿拟议比例报告收益。反复调用同一calibration又增加过拟合风险，代理梯度、相似度与较好旧起点不证明真实性能单调。生成池、表示/聚类、所有重训/检索和独立holdout都计费，较少样本不是更少总算力；响应估计、人口或费用失配时，保留静态/分层mixture、原真实数据与有限预算重新验证，不由模拟闭环批准真实部署可靠性。<!-- source-family:SF-2026-ARXIV-2605-21372 -->

## A31 PairwiseModalities21059v1必要Source/具体owner/PRE（prepared）

实际CORE §3/4/5全部/T1–3、AppA.1完整block proof与rank lemma；不采用A.2更强component theorem、不扩其全部证明。2+2+3=7深入。v1May20 11:44:01Z→May21 00Z→TAIL18 registeredMay21 02:17:53Z，同ID/findable/arxiv.content同BJTMay21。A1单模态/联合generators smooth invertible，A2邻居关于targetshared的Jacobians stacked fullcolrank/ΣA' A正定，不是图连通本身。AppA.1由相同pairdistribution作coupling恒等、微分时保持estimatedneighborlatent不依targetprivate的步骤依强结构/支持条件；末尾inversefunctiontheorem只得local inverse，不能直接当全局h逆或任意factor-level语义识别。这里不发布全局identifiability/全迁移定理，只采用局部rank条件与学习/consumer接口分责，不以摘要‘sufficientreliabletransfer’正面背书。

StageI AE(reconstruction+contrastive)、新modal→target partialasymmetric binarymask，StageII decoder surrogateinput接冻结Qwen3Omni30BA3B；私有因素不强推shared，maskactivecount预设而非已识别真语义。760kpointcaption+43kTVL，仅pair监督；78M适配vs9.5MMLP不是等容量，PointLLM/ShapeLLM与TVL多baseline为引用数据、GPTjudge非human。T3去StageI/II/rec/align是有限pipeline对照，不证明上述定理条件在真实embedding成立；冻结参数不证新输入保持旧行为。硬件/precision/seedCI与完整预算本必要域ND，编码/decoder/两stage训练/mapper/全部消费和回归均费。

Ch23当前05462完整段与15868完整后段、Ch22/24交接已读复用；05462以已知factor子集/link和结构矩阵约束分解，不含pair-only数据与接回frozenconsumer的两层资格。唯一MULTIMODAL-REPRESENTATION，拟05462完整段后/15868前两自然段（未授不写）：

> 数据仅按模态成对出现时，还须分别问“邻居是否共同观察到全部共享方向”和“学得的码能否接回目标consumer”。一个[受限pair-only分支](https://arxiv.org/html/2605.21059v1)用邻居对target共享因素的Jacobian堆叠满列秩表达前者；这依赖可逆生成模型和足够的局部变化，不是图连通就能恢复语义，局部可逆也不能自动升级为全局或逐factor识别。训练可先用各模态重建与pairwise contrastive保留信息，再对新模态只选与目标相关的部分，经目标decoder重组成surrogate输入；不把所有私有因素硬拉进共享坐标。
>
> 表示对齐与consumer兼容仍是两道验收：重建/contrastive小不证明目标模型会正确读取，部分mask也不是真实因素标签；冻结主干只保参数，不保证新输入路径或旧能力无损。有限3D/tactile对照中的不同adapter容量、合成配对和judge人口不支持通用迁移或零遗忘。配对谱系、mask/encoder/decoder身份、两stage训练和所有consumer回归均计费；可逆/rank支持、目标读出或净质量失配时，保真实配对、原专用encoder与晚期融合，必要时补目标监督，不以理论可识别名称批准未经检验的新模态。<!-- source-family:SF-2026-ARXIV-2605-21059 -->

## A32 EncMin2L20502v1必要Source/具体owner/PRE（prepared）

实际CORE §3–7完整/Alg1/T1–5/Prop1–2证明，2+1+3=6，联合误报/统计强保证反侧深入。v1May19 21:18:49Z→May21 00Z→TAIL18 registeredMay21 02:04:40Z，同ID/findable/arxiv.content整段BJTMay21。三encoder CLIP/DINOv2/ResNet，各norm/rawfork六VPscoreMLP，IDval CDF→forkmin→再CDF→crossmin→IDjointquantile。Prop1 iidUniform才Beta，withinforkρ.92/cross.17–.39不是独立；§6最终s uniform与τrescale声称不成立。Prop2 sameτ集合包含真，但非同FPRpower：ID两独立uniform、α.05，singleτ.05、minτ=1-√.95≈.02532，OODU1=.04/U2=.9时single检出min不检出。保具体反例，不替其修公式后授保证。经验CDF/同val重复拟合不等有限样本conformal或shift后FPR，10Rademacher probes+ODEtol1e-5仅估计LL不是exact。

50k/10k CIFAR ID10%val、32→224三frozenencoder，六MLP共285M训练至500epoch/earlystop，monolithic强加blockdiag且647M容量不证明所有联合模型必劣。IDdiagnostics仍用classlabel/syntheticcorruptions，noOOD labels不等无label；六相关fork的ρ/n不足不签普遍预测力。T3ours低最佳single/kNN多个轴、T4SVHN .806<single.903、T5删encoder能改善另轴，反对普遍power继承。硬件/precision/并发/完整latency/独立seedCI ND；三encoder/六ODEdensity、训练、calibration与未知域回归全费，不以参数少2.3×签净费。

当前Ch66 score→calibration→threshold13821完整段与15416完整后段实际读，已有只单selector，不含多sensor逐层min导致联合阈值改变的具体反侧。Ch65/67交接可复用。唯一PLATFORM-EVALUATION-SYSTEM，拟13821完整段后/15416前一自然段（未授不写）：

> 多个sensor联合告警时，单路校准分也不能直接共用原阈值：可先把各路分数映到同一ID参考分位，组内取最小值后重新校准，再对组间最小值按联合误报预算选阈值。一个[有限多encoder分支](https://arxiv.org/html/2605.20502v1)采用这条两层组合；同一阈值下“任一路告警则联合告警”的集合包含，并不保证同FPR下继承最强检测力，因为维持联合FPR通常需要更低阈值。独立uniform两路、α=.05时，单路阈值.05而min阈值约.0253，分数.04/.9可被前者检出却被后者漏掉；相关sensor更不能照用独立Beta零分布，最终min也不是uniform。编码、各density求值、联合校准与独立shift回归都付费，少参数和较好AUROC不替误报、漏报或完整费用验收；相关性、人口或未知shift失配时，保留单路/简单联合基线、真实误报测量与Unknown，不让组合告警自授开放环境可靠性。<!-- source-family:SF-2026-ARXIV-2605-20502 -->

## A33 UniT21131v1必要Source/具体owner/PRE（prepared）

实际CORE §III全部/Eq1–13与§IV全部/TII–XI，2+2+2=6，几何group可见性/坐标gauge与缓存gap深入。v1May20 13:04:34Z→May21 00Z→TAIL18 registeredMay21 02:19:33Z，同ID/findable/arxiv.content同BJTMay21。group内双向、group间causal，G1 online/GN offline需等待整组，不将Eq2右侧当任意完整未来条件联合分布的恒等分解。anchorfree relativepose loss/head与queue缓存分责，不再固定首帧不等不需任何旧场景信息；固定Q只界attention读取/缓存，参数/输出pointmap与全部历史资产另算。scaleadaptive训练relative+localabsolute/geometric normals，不保证在线任意场景metric scale；GT与全序列depthnorm为训练期，不偷接部署。

21个metricdatasets、VGGTinit/frozenDINO、80kiter/518res、随机G1–24、64H100×>7天、bf16；ablation244res/60k另域。单4090/448×224/50frames，G1 Q1 20.41FPS6.7GiB与full13.38/9.1质量/预算不同，非同质量加速；T XI stride-drop仍ATE.046>full.045，FIFO.057，丢历史有真实代价。T VII全modal原MapAnything平均rank更好、T IX加入concat改善metric却image-onlyscaleinvariant从.040退.045；T X shuffle也局部退。NRGBD50–500长实验先150帧offline再online/Q150有未来withininitialgroup等待；不授无限稳定/整请求实时/物理坐标真值。种子CI/并发SLO ND，训练、全部frames、optionalmodal校准与pointmap/pose消费均费，未核像素/实现或复现。

实际Ch23 159–178完整fisheye/pointfeature高分辨率15923与后multilingual交接，现有无按同步group读取、relativegauge解除首帧锚与queue淘汰三者分责。Ch22/24交接复用。唯一MULTIMODAL-REPRESENTATION，拟15923完整段后/当前‘若消费者需要可命名、可人工纠正的属性…’概念瓶颈段前一自然段（未授不写）：

> 连续几何表示还可以把同步视图组作为可见性单位：组内双向交换、组间只读已到达观测，改变组大小就改变等待与上下文，而不只是调一个batch。一个[有限几何分支](https://arxiv.org/html/2605.21131v1)再用相对camera关系替代固定首帧坐标锚，使旧KV可以按queue淘汰；这是解除参考frame依赖，不是证明旧场景细节已无用。固定Q限制活跃attention历史，较短queue仍会增加pose误差，offline初段后接online也须支付初段等待；相对几何与训练期absolute约束不自动认证新场景米制尺度。多组/多模态训练、sensor标定、全部编码与点图输出均计费，更多modal或更强约束也有局部退步；同步、scale、历史覆盖或净费用失配时，保较长历史、显式已标定reference和原offline/streaming路径，不由anchor-free或固定缓存批准真实世界状态与行动安全。<!-- source-family:SF-2026-ARXIV-2605-21131 -->

## A34 SO-TA20433v1必要Source/具体owner/PRE（prepared）

实际CORE §III–VIII完整/Eq6–17/TI–III与三task结果，2+2+2=6，显式OT边际与merge读出gap深入。v1May19 19:29:21Z→May21 00Z→TAIL18 registeredMay21 02:03:04Z，同ID/findable/arxiv.content同BJTMay21。force/pose给两个subqueries及rowγ，patchcolβ均匀49分，cosinecost、5次Sinkhorn，Σ_l Π_lp=βp；若直接等权sum subquery messages会退化均匀patchpool，乘γmerge保非均匀条件读出。不能沿原文‘any conditioning-independent merge必均匀’外推，固定非均匀merge亦可非均匀；γ再乘使总mass依γ变化，不当原始模态贡献。LOO ratio为置零后contextualized变化/归一，非causal重要度；heatmap只patchgate，不contacttruth。

TW8/TH16/10Hz/ResNet18-GN、1DUNet、混精/EMA、RTX6000Pro4000epoch×8192/约22h、4070TiSUPER推理均费；CA单query与OT两subquery+rowhead不等完全隔离OT最优性，concat总参数表69/81口径不补统一。peg198demo/约200rollouts、visualshift165/200vs87/200仅该设置；BCM396demo/200rollout7timeout、erase199demo/166of200成功，success-only time不包失败。cutoff12s的1000episodes是对single-attempt bootstrap simulation不是1000真实重置实测，不采physicalreset iid/99.5%保证。16.2ms平均inference不等尾deadline/总10Hz安全，5N独立阈值与阻抗loop保留，未核代码/全部图像素/复现。

实际Ch26 98–112完整条件消费28740两段/activecamera22461后段，原有模态分路attention但无显式row/column质量约束下merge坍成均匀池的接口。唯一MULTIMODAL-EMBODIED-VLA，拟28740完整两段末marker后/22461主动视角前一自然段（未授不写）：

> 接触条件还可约束视觉聚合的质量分配，而不只给每个patch一个独立softmax分数：由force/pose生成多份subquery及其row supply，让每个patch另受column capacity约束，再用条件相关的merge读取transport messages。一个[有限三模态分支](https://arxiv.org/html/2605.20433v1)中，column均匀时若直接等权加总各row，视觉读出会退回均匀池化；边际与最后merge必须一起设计，不能只把OT名称换进attention。条件权重和置零token后的变化均不是真实接触区域或原模态因果贡献，额外subquery/merge也使对照不只改变solver。传感同步/归一、Sinkhorn、完整策略训练和闭环回归均付费，有限成功率与平均forward不认证尾deadline；视觉扰动、长尾接触或时限失配时，保原concatenation/attention、较短动作chunk与独立力阈值/阻抗controller，不以heatmap或离线重启模拟签发物理安全。<!-- source-family:SF-2026-ARXIV-2605-20433 -->

## A35 VersusQ21130v1必要Source/具体owner/PRE（prepared）

实际CORE §3全部/Eq1–14、§4.1–4.4/T1–2、AppA/B/D；2+2+2=6，pairmargin→aggregate与rationale读出gap深入。v1May20 13:03:17Z→May21 00Z→TAIL18 registeredMay21 02:19:32Z，同ID/findable/arxiv.content同BJTMay21。MOS差监督signedcontinuousmargin，regplaceholder hidden→MLP非数字NTP；rationale policyGRPO+同rollout marginMSE梯度，MC同时更新reghead、GRPO对照frozenhead，故优势不唯一归coupling结构。LSQ在pairgraph最小化incidence差残差且sumscore0只去globalshift；需graph连通，5Nedges/avgdegree10本身不保证连通，模态/域间scale也未自动校准。

Qwen3VL4B+SlowFastR50 frozen，8visual/64motiontokens，18kSFT pairs/60kGRPOprompts×4rollout；主文warmup1epoch而AppB2epoch不补统一。A80080G：SFT8卡、GRPO1×8rollout+3×8opt/bs48，额外teacherGemini3Pro rationale、全部比较/编码/求解均费，5N比较平均10邻不等一次video评分。AppA sparsecurve是相对final相关差.005停止，不证真MOS误差或跨scale可比。T1KoNViD/LIVEVQC SRCC低VQAThinker，T2reasonSFT YT-Gaming .710<no-reason.760，MC YT.774<GRPO.779、W4K PLCC .670<.680；seedCI/precision/并发SLO ND。MOSbias/disagreement与引用baseline保留，未核完整实现/复现。

Ch66 551–588 complete FuScore(mean/width/group-rank)段及anchorcandidatepool两段已读，不承载signedmargin的graphLSQ与regreadout/rationale更新分工。Ch65/67交接可复用。唯一PLATFORM-EVALUATION-SYSTEM，拟06969 FuScore完整段后/00223 anchorpool首段前一自然段（未授不写）：

> 相对判断还可以同时监督方向与差额，而不只给win/lose：让比较文本后的连续head预测同一量表上的pair margin，再在稀疏比较图上以least-squares汇总这些带符号差值，并用零均值去掉整体平移。一个[有限视频质量分支](https://arxiv.org/html/2605.21130v1)同时以rationale奖励与margin回归更新读出，避免把数字token的粗刻度当连续差额；但图不连通时零均值不足以固定分量间位置，少量边和相关性趋稳也不认证真实质量或跨域绝对scale。该研究的GRPO对照还冻结回归head，不能把全部收益唯一归辅助梯度，加入reasoning或耦合更新均有局部反退。MOS/教师解释、配对图/采样、全部rollout/编码与求解都付费；差额、连通支持或新域校准不可靠时，保原逐项分、可信anchors、人工比较与并列/无结论，不由anchor-free名称批准任意候选池和量表可比。<!-- source-family:SF-2026-ARXIV-2605-21130 -->

## A36 STiTch21261v1必要Source/具体owner/PRE（prepared）

实际CORE §3/Eq1–9、§4.1–4.3/T1–5、AppendixA Alg1/D1–3/H必要域；2+1+2=5，query/candidate集合读出gap深入。v1May20 14:51:29Z→May21 00Z→TAIL18 registeredMay21 02:22:36Z，同ID/findable/arxiv.content同BJTMay21。MLLM采K5captions，CLIPcaption与modificationembedding凸混α.45，后者只是启发式，不证明f(m)=y-x，不用heatmap声明删除真实无关语义；候选gallery每图M10crop/flip。CT两方向独立softmax对相似度加权cost，不是共享plan满足双边marginals的balancedOT，也不是Shannon/校准posterior。Eq6缺1/K和1/M期望归一、Eq9括号不整，不发布所有K/M可比的精确distance recipe；固定K/M下有限ranking仍可讨论。

singleA6000/Qwen2VL7B/CLIP-L或OpenCLIPbigG，3randomseeds只报mean无CI；除FashionIQ训练free复现外多baseline引用原论文，不同MLLM/CLIP预训混杂。T2FashionIQSTiTch39.12/59.43低SEIZE43.05/65.85，T1CIRRsubsetR1 .7356<SEIZE.7415；部分GeneCIS focus也低。α过强过弱/更多aug与caption不授普遍单调，gallery多视预编码约M-1倍memory按作者H原口径保留但实际总bytes需另算；3.5s/query不包括完整离线gallery制备/部署SLO。不明确多对象+短修订会指错目标，FashionIQ单GT漏正例不能反过来把所有未命中判正确。训练free不免MLLM多次调用/encoding/全gallery对齐/参数验证，未核像素/代码/复现。

Ch23 120–129完整multi-view kernel/CLIPbinding/SMA facilitycoverage与后content-style段已实际读，已有集合coverage不承载对caption集合与candidate增强集合做独立双向softmatching及与balancedOT的边际差异。唯一MULTIMODAL-REPRESENTATION，拟12872 SMA完整段后/content-style双encoder首段前一自然段（未授不写）：

> 集合读出还可在caption侧和candidate侧分别保留多个提案，而不先把每侧平均成一点：从同一参考图与修订条件采多份描述，再与候选图的多份增强逐对比较，按caption到image与反方向的条件softmax汇集cost。一个[有限组合检索分支](https://arxiv.org/html/2605.21261v1)采用这种双向softmatching；两个条件分布不是满足共同双边边际的同一OT plan，也不因称作distribution就成为校准后验。将修订文本embedding混入caption只是抑制参考偏置的启发式，不能当真实视觉位移或语义删除。多对象/含糊指令仍可选错，增强和混合更强也未必改善每个排名；全部caption调用、gallery多视编码/驻留、paircost与参数验证均付费。候选身份、描述支持或净预算不可靠时，保原单描述/全局相似、可信人工修订与简单集合聚合，不让training-free或更丰富提案批准无损检索与跨用途概率解释。<!-- source-family:SF-2026-ARXIV-2605-21261 -->

## A37 收齐态与机器检查（DAY待root）

本日只补BJT2026-05-21，发现按A22/A24封口，未接他日或新增尾检。冻结28新增＝27精确arXiv v1＋Hy-MT2，全部必要Source/date/贡献与具体Books判断已有root R1–34独核：24项真实新增整合／2具体已有覆盖（GaussianDream/MXFP4）／2仅报告（Stream3D/SPpruner）。24项各一次实际非writer新增全文/完整直接两侧/本人注POST均通过，指定窄位释放。作者仅同步R21/R24/R25/R26/R28/R29/R31/R32/R34已发生事实并实际读回，不第三次Source/POST。未核代码/完整artifact、复现实验或生产SLO，不采用原文已限定的强保证。

当前README六部分已收齐：282家族＝原254＋新28；224深入＋58标准，Books76整合＋148已有覆盖＋58仅报告。新增5～6分只因具体差额或强断言反侧深入，不因工作量改分；LamPO当前官方撤回/删除不候选分书，FTerViT与其他具体贡献前关闭留原记录。三个跨日必要资格（Proxy20201/NaP20209/Proc20251）与九个固定来源历史切片受阻各精确隔离、留恢复条件，不支撑正面证据、Books、完整Coverage或无遗漏。

真实HEAD原报告逐字保存为同日 `baseline-before-supplement-20261020.md`，原件与副本sha256同为`969ea7a621f38cdd130a3052b1c61a87bacf91801b1e7ef57d5fd11982e39913`，用于工具支持的冻结旧日期，不由当前字段反造快照。原254逐行（含换行）仍`ec0e819fb0b50f4bda03df056d35841919610ce8475e398e2addb720ac9febac`；从旧§4标题至原structured-links末尾加两换行仍`3b167ad0777f9adbcf2f874df8c6a190958f63b5c49eb3c0e90e2e86d98c7e5c`。旧小时窗/日期/评分不迁移。

首轮V3因未引用冻结档案报254条旧日门错误，且固定必查来源不允许仅标“检索受限”；按既有scripts/README接口补冻结引用、将九行结果准确记受阻，未改validator/旧行。重跑V3通过；限定cached/unstaged diff-check通过。当前README317本地引用/49路径全存在；逐字基线260引用按原README位置解释，相对路径未改写，原上下文核对全存在。最初把移动后的档案位置当链接基准所报missing不是真实原引用缺失，已纠正核算；不称档案重定位后自身链接天然可点击。

原254与旧§4实际冻结保持；28项普通Source/Books写入待办0。此段原为交付DAY/FINAL前过程态；现root R35实际完整六部分DAY、R36实际2026-10-21T09:19:18+08:00保存态有限FINAL均已通过，日期ownership与全部指定窄位释放。作者仅行政同步已发生事实，不第三次原证/Books审阅。原文件所有并发修改保留，本方未stage/commit/push、不改共享索引/State/合同。
