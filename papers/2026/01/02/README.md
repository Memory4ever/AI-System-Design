# Daily Research — 2026-01-02

**规范：** V3
**窗口：** 2026-01-01T09:00:00+08:00 ～ 2026-01-02T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-02T21:02:24+08:00

## 1. 结论

元旦延迟公告批次带来多项真正落窗的机制及反证。冻结候选为104个唯一家族，均获具名终态：87项必要证据与Books判断经非作者复核（62项实际整合、20项具体已有覆盖、5项标准仅报告），另1项4分关闭、16项中心/身份口径争议暂缓。关闭和争议不冒充正面Evidence；root日级独立验收已通过，达到合同安全终态。新增论点包括多流残差守恒、通信/检查点恢复粒度、主动迁移schedule前提、proxy recipe干扰、visible memory/training graph分账、受限采样workspace、MoE/audio组件威胁，以及pool/instance身份、条件prompt人口、谱系反馈、单目尺度/重定位边界、共享基容量与局部标签/偏好强度/跨语言干预的测量分责；RLM重要证据只分账external access与subcall收益，地图实验只限定表示信息充分性和曝光/资源预算；私有偏好只保护标签通道，随机历史帧重建不授world state，weight-only旋转代理不自动迁移activation位宽。压缩gate使用不等远程召回已成立，集合选择不凭共享组统计授无偏保证；多轮偏好区分共同演化的用户分支、同状态反事实与step credit。新增长视频编辑segment依赖/插值成本及拟议音视频配对方向测量，不授无限长度稳定或模型物理能力实测。作者数字不外推生产性能、安全或硬件速度保证。

四个主题有界查询的279及147个去重题名分别只作两个Submitted缓冲段的发现线索，不是当天论文数或候选池；语义选出的63+78份完整v1题摘实际读完，141＝30项范围/贡献/撤回前关闭＋7项窗前公开归属＋104项本窗候选终态＋0项普通待办。摘要已读与日期元数据已取均不算Evidence完成；7项窗前公开不是已审旧Report重复，RLM则仅采用本窗具体重要新证据事件。有限来源覆盖及无法恢复的历史切片按§2/§5分开保留，不授全网或旧ID修订零遗漏。

## 2. 来源覆盖

以下是已执行入口的有限历史切片，不声称互联网无遗漏。机构原始字段及失败恢复见[机构记录](../_sources/daily-20260102/INSTITUTION_FIELDS.json)、[有限恢复](../_sources/daily-20260102/INSTITUTION_RECOVERY_1.json)；六组无法恢复的历史部分按§5隔离，不能因当前目录可读而改成“无命中”。arXiv有限题摘筛选与候选处置已收束，旧ID重要修订覆盖限制单独保留。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 官方Research/RSS有限条目，Jan2 10:00GMT的Grove在窗后、Dec22条目在窗前；按RSS时间保留 | 已检查 | 当前有限RSS不能保证已移除历史事件可恢复，不用搜索零命中补保证 |
| SRC-ANTHROPIC | 官方Research序列化Publications有限完整目录；Dec18/19与Jan8之间实际日期切片 | 已检查 | 不外推当前目录为全部历史发布 |
| SRC-GOOGLE-AI | Google Research Jan2026月档9条/Dec2025月档6条均到无pager，最邻近Jan12/Dec18；DeepMind及pubs必要历史入口有限恢复 | 受阻 | 月博客已检查不等于pubs/DeepMind历史首公开已覆盖，未恢复部分不当零命中 |
| SRC-META-AI | Research/global_search首个publication页12条，条目日期非严格排序；目标日期辅助检索忽略过滤 | 受阻 | 无可靠Jan1历史页/分页停止证明，不以新旧混排首屏声称无命中 |
| SRC-QWEN | qwen.ai Research动态shell、旧官方Blog有限日期切片；Dec30 Qwen-Image-2512在窗前 | 受阻 | 当前动态目录的历史发布切片尚未恢复，旧Blog不能替代新Research全部 |
| SRC-DEEPSEEK | 官方mHC公告/精确arxiv v1及延迟批次；Engram Jan12在窗后 | 已检查 | mHC按论文公开区间归属，不把公告仅日历日期造为分钟；其他未披露机制不采用 |
| SRC-MOONSHOT | Kimi Platform Blog有限26条目录，最近旧项Nov7，较旧May2024；限定官方入口核查 | 已检查 | 当前Blog历史删除及GitHub技术通知切片不获全量保证 |
| SRC-TENCENT-HUNYUAN | Research浏览器尝试超时；原JS恢复正确publicList接口，page1 size20、total11已取11，最早Feb3 | 受阻 | 当前11条不是Jan1历史目录；超时与旧切片缺失不作零命中，见HUNYUAN_PUBLICLIST_2.json |
| SRC-ZAI | Research page1 15、page2累计18、hasMore=false停止；原publication createAt与CMS createdAt分开，见[分页记录](../_sources/daily-20260102/ZAI_PAGINATION.json) | 已检查 | 当前有限目录无Jan1原publication项不证明被移除历史/发布说明全量 |
| SRC-BYTEDANCE-SEED | 正确article_type1论文/2博客及locale；2026升序论文首20最早Jan20、2025降序首18最近Dec15，博客2026有限14最早Feb12/2025首18最近Dec24，跨界日期停止 | 已检查 | 无效type0响应不作覆盖；有限首公开列表见SEED_API_RECOVERY.json |
| SRC-BAIDU-ERNIE | 官方Blog首10条日期按Jan8/Dec23包围窗，已达到前窗口日期后停止 | 已检查 | 当前有限列表不证明其他被移除事件 |
| SRC-XIAOMI-MIMO | Paper有限8项Jan8在后/MiMoAudio Sep19在前；Blog15项无日期/More隐藏 | 受阻 | undated Blog历史日期无法恢复，不能由Paper无新项推出全源无命中 |
| SRC-MINIMAX | Blog有限13项以Jan27/Dec23包围窗；AgentTech单页May13 | 受阻 | AgentTech Jan1历史状态未恢复，不据当前晚页宣称当时不存在 |
| SRC-ARXIV | 四主题（模型/训练、执行系统、多模态生成、Agent检索）/12分类，Submitted缓冲Dec30T18Z～Jan2T01Z依次取3/1/1/1页，total222/55/76/62；补Dec29T19Z～Dec30T18Z取2/1/1/1页，total113/26/51/28，每query末页start+实际条数=total后停。分别去重279/147仅作题名线索；[初段](../_sources/daily-20260102/ARXIV_THEME_RAW.json)/[补段](../_sources/daily-20260102/ARXIV_DEFERRED_GAP_RAW.json)。cs.CL December目录仅1250邻近末页相关标题有限補检；141份完整题摘完成筛选，104家族终态 | 受阻 | 有界筛选与普通候选已处理；Submitted不是公开字段，窗前ID重要revision公开切片仍不可恢复见§5，不授零事件/全量覆盖；目录1302条不是队列，失败页不作正面覆盖 |

## 3. 候选与判断

此表冻结为104个唯一候选家族，含16项中心/身份争议隔离及1项低分关闭；不计30项前关闭与7项窗前公开。公开区间统一含起点、不含终点，下面均为北京时间。原值、精度及共同推定依据见§4；注册仅给上界，不给精确首次公开分钟。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [mHC: Manifold-Constrained Hyper-Connections](https://arxiv.org/html/2512.24880v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:22:20+08:00 | unconstrained多流混合→双随机residual carry及有限误差→区分恒定均值方向守恒与全网稳定；2+2+3=7 | 深入完成 | 整合：MODEL-TRANSFORMER-LAYER，[Ch17](../../../../books/part-02-model/17-transformer-layer.md)几何约束桥接 |
| [Reliable and Resilient Collective Communication Library for LLM Training and Serving](https://arxiv.org/html/2512.25059v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:26:38+08:00 | NIC故障整job rollback→chunk完成/ACK及多NIC迁移→重考transport恢复粒度；2+3+3=8 | 深入完成 | 整合：TRAIN-DISTRIBUTED-TRAINING，[Ch36](../../../../books/part-04-training-system/36-distributed-training.md)elastic前恢复链 |
| [MSched: GPU Multitasking via Proactive Memory Scheduling](https://arxiv.org/html/2512.24637v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:16:38+08:00 | reactive paging→已知launch预测working-set及迁移排程→重考capacity/prefetch管理边界；2+3+3=8 | 深入完成 | 整合：INFER-GPU-MEMORY，[Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md)reserve/template/page-ready |
| [Can Small Training Runs Reliably Guide Data Curation? Rethinking Proxy-Model Practice](https://arxiv.org/html/2512.24503v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:13:29+08:00 | 同recipe不一定公平→data-dependent最优及排序逆转→修正proxy评价协议；3+2+3=8 | 深入完成 | 整合：TRAIN-DATA，[Ch27](../../../../books/part-04-training-system/27-data.md)data mixture交互 |
| [Understanding LLM Checkpoint/Restore I/O Strategies and Patterns](https://arxiv.org/html/2512.24511v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:13:40+08:00 | 大buffer microbench不能代tensor checkpoint→alignment/coalescing及restore allocation→改变IO可比单位；3+2+2=7 | 深入完成 | 整合：TRAIN-CHECKPOINT，[Ch35](../../../../books/part-04-training-system/35-checkpoint.md)async/commit后IO粒度 |
| [Modeling Language as a Sequence of Thoughts](https://arxiv.org/html/2512.25026v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:25:48+08:00 | rolling句向量仍有递归祖先梯度→visible容量与credit horizon分账→重考detach/reset成本；2+2+3=7 | 深入完成 | 整合：MODEL-LONG-CONTEXT，[Ch22](../../../../books/part-02-model/22-long-context.md)历史压入state末尾 |
| [Diffusion Language Models are Provably Optimal Parallel Samplers](https://arxiv.org/html/2512.25014v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:25:30+08:00 | frozen写入与revision在受限uniform-even-parity sampler分离→临时输出槽回收workspace→区分步数/空间/每步深度；3+2+3=8 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS，[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)保守unmask后 |
| [Many Minds from One Model: Bayesian Transformers for Population Intelligence](https://arxiv.org/html/2512.25063v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:26:44+08:00 | token探索与跨trajectory扰动不同→每sequence固定norm噪声→核局部多样性和likelihood条件；2+2+2=6 | 标准完成 | 仅报告：有限探索未确立posterior/selection可靠性及共同预算，不改长期采样论证 |
| [Large language models and the entropy of English](https://arxiv.org/html/2512.24969v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:24:24+08:00 | length/单位/语料与模型条件共同改变entropy proxy→重考长依赖归因；2+2+2=6 | 标准完成 | 已有覆盖：MODEL-LONG-CONTEXT，[Ch22](../../../../books/part-02-model/22-long-context.md)信息负荷/条件分账；不声称已覆盖true entropy数学定律 |
| [RepetitionCurse: Measuring and Understanding Router Imbalance in Mixture-of-Experts LLMs under DoS Stress](https://arxiv.org/html/2512.23995v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:01:24+08:00 | 重复输入expert集中是否变device straggler取决placement→修正training-balance外推；2+3+3=8 | 深入完成 | 整合：MODEL-MOE，[Ch21](../../../../books/part-02-model/21-moe.md)placement合同后 |
| [Breaking Audio Large Language Models by Attacking Only the Encoder: A Universal Targeted Latent-Space Audio Attack](https://arxiv.org/html/2512.23881v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T10:58:45+08:00 | decoder不可见不取消encoder梯度灰盒能力→跨输入目标转录与effect分离→补组件威胁条件；2+2+3=7 | 深入完成 | 整合：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)run/旧isolated测试交接 |
| [Jailbreaking Attacks vs. Content Safety Filters: How Far Are We in the LLM Safety Arms Race?](https://arxiv.org/html/2512.24044v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:02:35+08:00 | base ASR不等完整input/output filter对象→漏检、benign误拒和成本分账；3+2+3=8 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)组合次序/共同模型人口；原Pass和单位错误只限定本论文 |
| [Safe in the Future, Dangerous in the Past: Dissecting Temporal and Linguistic Vulnerabilities in LLMs](https://arxiv.org/html/2512.24556v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:14:43+08:00 | language×framing改变安全切片且方向不一致→反对单平均及内部因果外推；2+2+3=7 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)平均值/切片/sameprompt相关性 |
| [Scaling Open-Ended Reasoning To Predict the Future](https://arxiv.org/html/2512.25070v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:26:54+08:00 | 未来信息不能靠模型自述cutoff排除→offline snapshot与resolution筛选→限定数据/预测评价身份；2+2+2=6 | 标准完成 | 已有覆盖：TRAIN-DATA，[Ch27](../../../../books/part-04-training-system/27-data.md)953–957逐transition cutoff及snapshot旧路；不声称覆盖联合reward的通用最优性 |
| [Efficiently Estimating Data Efficiency for Language Model Fine-tuning](https://arxiv.org/html/2512.24991v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:24:55+08:00 | low-confidence gradient cosine预测task curve→核预算诊断成立条件；2+1+2=5 | 争议 | 暂缓：线性n与log2 AUC测度前后冲突，不能据未确定目标推荐标签预算；见§5重开条件 |
| [VLN-MME: Diagnosing MLLMs as Language-guided Visual Navigation agents](https://arxiv.org/html/2512.24851v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:21:39+08:00 | CoT/reflection局部负收益→核spatial state/control与预算归因；2+2+3=7 | 争议 | 暂缓：D4可replan与D8 log-only冲突，不认证reflection控制或失败根因；见§5重开条件 |
| [Encyclo-K: Evaluating LLMs with Dynamically Composed Knowledge Statements](https://arxiv.org/html/2512.24867v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:22:02+08:00 | 可变question不消除statement污染→pool/instance两阶段identity→重新划分refresh与gold边界；2+1+2=5 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)dataset governance两阶段身份 |
| [Youtu-LLM: Unlocking the Native Agentic Potential for Lightweight Large Language Models](https://arxiv.org/html/2512.24618v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:16:10+08:00 | rollout/current drift整组筛prompt改变P(Q\|K<τ)人口→importance correction与admission分账；2+2+3=7 | 深入完成 | 整合：TRAIN-GRPO，[Ch33](../../../../books/part-04-training-system/33-grpo.md)async policy freshness |
| [LoongFlow: Directed Evolutionary Search via a Cognitive Plan-Execute-Summarize Paradigm](https://arxiv.org/html/2512.24077v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:03:22+08:00 | feedback按parent-ID归属而非近邻文本→plan/summary谱系与fast-fail/full evaluator分层；2+1+2=5 | 深入完成 | 整合：AGENT-PLANNING，[Ch79](../../../../books/part-07-agent/79-planning.md)搜索反馈归属 |
| [RANGER: A Monocular Zero-Shot Semantic Navigation Framework through Contextual Adaptation](https://arxiv.org/html/2512.24212v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:06:36+08:00 | 不finetune仍需offline bank尺度与可重定位起点→限定VLM controller成立条件；2+1+2=5 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA，[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)VLM-conditioned controller |
| [RSAgent: Learning to Reason and Act for Text-Guided Segmentation via Multi-Turn Tool Invocations](https://arxiv.org/html/2512.24023v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:02:05+08:00 | reasoning segmentation保正确中间状态而不模仿随后失败→核历史反馈和预算饱和；2+1+2=5 | 标准完成 | 已有覆盖：TRAIN-SFT，[Ch29](../../../../books/part-04-training-system/29-sft.md)142–150/566–578失败历史与正确prefix，不声称覆盖IoU公式 |
| [HaluNet: Multi-Granular Uncertainty Modeling for Efficient Hallucination Detection in LLM Question Answering](https://arxiv.org/abs/2512.24562v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:14:51+08:00 | 单QA多信号融合的局部detector配置，无新跨任务真伪核验；1+1+2=4 | 已关闭 | 仅报告：不足改变长期verification/校准选择，不把confidence作事实证明 |
| [Collaborative Low-Rank Adaptation for Pre-Trained Vision Transformers](https://arxiv.org/html/2512.24603v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:15:49+08:00 | 独立模块因子→共享basis与模块Q分账→重考容量/参数及固定merge取舍；2+1+2=5 | 深入完成 | 整合：TRAIN-LORA，[Ch30](../../../../books/part-04-training-system/30-lora.md)173/175共享基容量 |
| [Localized Calibrated Uncertainty in Code Language Models](https://arxiv.org/html/2512.24560v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:14:49+08:00 | 整程序正确不等repair-kept任意span事件→patchability/目标域校准分账；2+1+2=5 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)652/654局部修复标签 |
| [Exploring Compositionality in Vision Transformers using Wavelet Representations](https://arxiv.org/html/2512.24438v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:11:57+08:00 | 分类head可拟合不证明全latent线性组合或模型已用→限定representation诊断；2+1+2=5 | 标准完成 | 已有覆盖：MULTIMODAL-REPRESENTATION，[Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)63–65/101–103读出/模型使用分账 |
| [From Building Blocks to Planning: Multi-Step Spatial Reasoning in LLMs with Reinforcement Learning](https://arxiv.org/html/2512.24532v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:14:09+08:00 | frozen base与GRPO adapter分离→核原子行为保持/观测接口/总训练预算；2+1+2=5 | 标准完成 | 仅报告：有限ASCII确定性变换未验证技能保留或相同总预算，不授可发布skill/policy分责保证 |
| [Vulcan: Instance-Optimal Systems Heuristics Through LLM-Driven Search](https://arxiv.org/html/2512.25065v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:26:47+08:00 | 任意source proposal→typed Value/Rank/有限queue与固定scaffold分责→分开搜索/执行成本；2+2+2=6 | 深入完成 | 整合：AGENT-PLATFORM，[Ch84](../../../../books/part-07-agent/84-agent-platform.md)891/893受限策略接口 |
| [ResponseRank: Data-Efficient Reward Modeling through Preference Strength Learning](https://arxiv.org/html/2512.25023v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:25:43+08:00 | 偏好方向外的comparison强度rank→局部单调假设/额外标签与失败proxy分账；2+1+3=6 | 深入完成 | 整合：TRAIN-RLHF，[Ch31](../../../../books/part-04-training-system/31-rlhf.md)97/99 BT后强度测量 |
| [Iterative Deployment Improves Planning Skills in LLMs](https://arxiv.org/html/2512.24940v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:23:43+08:00 | valid trace筛选的SFT/RL等价需conditional归一化与参数继承身份→核部署循环；2+2+3=7 | 争议 | 暂缓：Prop2缺Zpi/Zbeta且M_n与fixed-base训练矛盾，不采用完整等价/部署泛化；见§5 |
| [Triangulation as an Acceptance Rule for Multilingual Mechanistic Interpretability](https://arxiv.org/html/2512.24842v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:21:26+08:00 | 同predicate稳定与swap sufficiency分开→translated patch distortion/cue falsifier验收；2+1+2=5 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)2803/2805 proposed干预合同 |
| [Compute-Accuracy Pareto Frontiers for Open-Source Reasoning Large Language Models](https://arxiv.org/html/2512.24776v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:19:54+08:00 | 匹配分析compute观察accuracy前沿→核饱和/长度/配置混杂与真实成本；2+2+2=6 | 标准完成 | 仅报告：19跨model配置不识别fixed-checkpoint causal horizon/可部署早停，不把FLOPs当latency |
| [Recursive Language Models](https://arxiv.org/html/2512.24601v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:15:46+08:00 | 重要新证据非首次：model/task×no-subcall对照→external access与递归收益分账→重考子调用及端到端预算；2+2+3=7 | 深入完成 | 整合：AGENT-CONTEXT，[Ch75](../../../../books/part-07-agent/75-context.md)247/249外置原文与subcall独立收益 |
| [Dynamic Large Concept Models: Latent Reasoning in an Adaptive Semantic Space](https://arxiv.org/html/2512.24617v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:16:09+08:00 | variable concept pooling/μP改变粒度→核token读取current concept的完成条件与预算→不能自动授因果NTP；2+2+3=7 | 争议 | 暂缓：pool含完整segment而current概念可读取，未披露shift/completion；见§5 |
| [Thinking on Maps: How Foundation Model Agents Explore, Remember, and Reason Map Environments](https://arxiv.org/pdf/2512.24504v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:13:30+08:00 | topology不保存所有metric/order且曝光不等资源预算→工程表征使用与自主memory形成分账；2+2+3=7 | 深入完成 | 整合：AGENT-MEMORY，[Ch77](../../../../books/part-07-agent/77-memory.md)39/41任务信息类型/coverage-stop边界 |
| [OptRot: Mitigating Weight Outliers via Data-Free Rotations for Post-Training Quantization](https://arxiv.org/html/2512.24124v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:04:29+08:00 | weight第四矩代理不等activation误差→data-free旋转步骤与bit-regime反例分账；2+3+3=8 | 深入完成 | 整合：INFER-TENSORRT-LLM，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)1139/1141 rotation scope开头 |
| [Improved Bounds for Private and Robust Alignment](https://arxiv.org/html/2512.23816v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T10:57:17+08:00 | observed BT likelihood经RR改变→污染/隐私顺序与c缩放风险不同→限定label-only alignment；2+3+3=8 | 深入完成 | 整合：TRAIN-RLHF，[Ch31](../../../../books/part-04-training-system/31-rlhf.md)101/103 BT强度后 |
| [Pretraining Frame Preservation in Autoregressive Video Memory Compression](https://arxiv.org/html/2512.23851v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T10:58:04+08:00 | 压缩端点不等任意旧帧可检索→random-position重建/高频及总pretrain分账；2+2+3=7 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS，[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)89/91历史压缩尾 |
| [Probing the Limits of Compressive Memory: A Study of Infini-Attention in Small-Scale Pretraining](https://arxiv.org/html/2512.23862v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T10:58:19+08:00 | gate使用不等远程召回→训练支持/LR/depth反例→限制memory有效依赖范围；2+2+3=7 | 深入完成 | 整合：MODEL-LONG-CONTEXT，[Ch22](../../../../books/part-02-model/22-long-context.md)543/545固定状态交接 |
| [Joint Selection for Large-Scale Pre-Training Data via Policy Gradient-based Mask Learning](https://arxiv.org/html/2512.24265v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:07:52+08:00 | 单样本quality不等集合diversity→不放回mask联合目标→分块与完整curation预算分账；2+2+3=7 | 深入完成 | 整合：TRAIN-DATA，[Ch27](../../../../books/part-04-training-system/27-data.md)246/248过滤后 |
| [Do Large Language Models Know What They Are Capable Of?](https://arxiv.org/html/2512.24661v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:17:12+08:00 | multi-step/ICL重要新证据（非首次），旧single-step之外的新决策与多步测量→profit/calibration/ranking及active/forward-filled人口分账；2+2+3=7 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)2301/2303风险–覆盖末 |
| [MCPAgentBench](https://arxiv.org/html/2512.24565v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:14:55+08:00 | mock/gold序列指标不等实际effect→替代合法plan与测试权限分账；1+2+2=5 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)367–380/1252附近legal acceptance/mock contract；非TEFS公式已写 |
| [Understanding and Steering the Cognitive Behaviors of Reasoning Models at Test-Time](https://arxiv.org/html/2512.24574v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:15:08+08:00 | head词法probe读出不等正确干预→局部projection与独立verifier/成本副作用分账；2+1+2=5 | 标准完成 | 已有覆盖：MODEL-MULTI-HEAD-ATTENTION，[Ch15](../../../../books/part-02-model/15-multi-head-attention.md)282/284；PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)3780/3989附近；非keyword/PCA recipe已写 |
| [MultiRisk: Multiple Risk Control via Iterative Score Thresholding](https://arxiv.org/html/2512.24587v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:15:26+08:00 | first-trigger互斥成本改变下游人口→联合阈值与loss界分责→不混为残留unsafe率；2+2+3=7 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)2305/2307；仅设计分账，D5递归保证步骤隔离 |
| [MUSIC: MUlti-Step Instruction Contrast for Multi-Turn Reward Models](https://arxiv.org/html/2512.24693v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:17:57+08:00 | chosen/rejected用户随自身history演化→trajectory preference非同状态动作反事实→terminal标量不自动授step credit；2+1+2=5 | 深入完成 | 整合：TRAIN-RLHF，[Ch31](../../../../books/part-04-training-system/31-rlhf.md)146/148 preference-data人口漂移后 |
| [AMAP Agentic Planning Technical Report](https://arxiv.org/html/2512.24957v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:24:08+08:00 | 固定selector不跟能力变动→当前policy reward均值/方差调整学习人口→核能力相对选择与额外采样成本；2+1+2=5 | 标准完成 | 已有覆盖：TRAIN-DATA，[Ch27](../../../../books/part-04-training-system/27-data.md)560–610当前checkpoint rollout与retain/revise/retire；非mean×variance公式已写 |
| [ROAD: Reflective Optimization via Automated Debugging for Zero-Shot Agent Alignment](https://arxiv.org/html/2512.24040v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:02:29+08:00 | 失败日志导出规则更新→结构化prompt仍需独立验证和执行权限→不把YES文本当runtime guard；2+1+2=5 | 标准完成 | 已有覆盖：AGENT-PROMPT，[Ch74](../../../../books/part-07-agent/74-prompt.md)125–164规则scope/validation；AGENT-REFLECTION，[Ch80](../../../../books/part-07-agent/80-reflection.md)40–120反馈/修复假设与权限 |
| [Subsecond 3D Mesh Generation for Robot Manipulation](https://arxiv.org/html/2512.24428v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:11:43+08:00 | 无纹理mesh不满足render消费者→几何注册与sensor metric anchor分工→表示质量不替定位/动作验收；2+1+2=5 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA，[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)69校准几何后 |
| [From Inpainting to Editing: A Self-Bootstrapping Framework for Context-Rich Visual Dubbing](https://arxiv.org/html/2512.25066v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:26:48+08:00 | cleanreference注入与目标旧唇形冲突→校准噪声stage adapter→分开context收益与编辑训练support；2+1+2=5 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS，[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)135 reference条件后 |
| [PhyGDPO: Physics-Aware Groupwise Direct Preference Optimization for Physically Consistent Text-to-Video Generation](https://arxiv.org/html/2512.24551v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:14:36+08:00 | group preference目标与权重条件本应绑定→PL概率/符号/upper-bound条件冲突→中心推导暂不采用；2+2+2=6 | 争议 | 暂缓：合法group概率、Eq9符号及Eq8/10条件链待澄清，不宣称全部实测无效 |
| [What drives success in physical planning with Joint-Embedding Predictive World Models?](https://arxiv.org/html/2512.24497v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:13:20+08:00 | 同样multistep长度不等相同训练→target index/context来源与detach改变credit→明确rollout训练身份；2+2+3=7 | 深入完成 | 整合：MULTIMODAL-WORLD-MODELS，[Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)317/319展开训练身份 |
| [FlowBlending](https://arxiv.org/html/2512.24724v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:18:41+08:00 | 全程大模型→同接口离线capacity schedule→区分求值次数与单步容量/切换成本；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS，[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)513 capacity schedule |
| [Are First-Order Diffusion Samplers Really Slower? A Fast Forward-Value Approach](https://arxiv.org/html/2512.24927v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:23:25+08:00 | 一阶当前状态求值→lookahead位置/time近似→分开理想implicit、iterations/NFE与真实成本；2+1+2=5 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS，[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)154 FM执行后 |
| [Counterfactual VLA: Self-Reflective Vision-Language-Action Model with Adaptive Reasoning](https://arxiv.org/html/2512.24426v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:11:40+08:00 | meta error诊断→GT预填配对/teacher与mask→训练介入不等runtime Think gate可靠；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA，[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)628 meta-action后 |
| [EchoFoley: Event-Centric Hierarchical Control for Video Grounded Creative Sound Generation](https://arxiv.org/html/2512.24731v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:18:51+08:00 | 整体condition不可局部recompose→事件state/独立segment生成mix→分开编辑能力、定位事实与全链成本；2+1+2=5 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS，[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)1173事件路由后 |
| [Let It Flow: Agentic Crafting on Rock and Roll — Building the ROME Model within an Open Agentic Learning Ecosystem](https://arxiv.org/html/2512.24873v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:22:10+08:00 | token/turn credit粒度→interaction chunk discount与筛选、teacher prefix replay→分开联合ratio和训练起点权限；2+2+2=6 | 深入完成 | 整合：TRAIN-GRPO，[Ch33](../../../../books/part-04-training-system/33-grpo.md)1371 credit lifecycle前 |
| [SpaceTimePilot: Generative Rendering of Dynamic Scenes Across Space and Time](https://arxiv.org/html/2512.25075v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:27:02+08:00 | frame index与动画时间混同→source/target camera/time双身份→限定retime支持与估姿真值边界；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS，[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)1177相机条件后 |
| [VIPER: Process-aware Evaluation for Generative Video Reasoning](https://arxiv.org/html/2512.24952v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:24:00+08:00 | 终帧目标不评价过程→采样集∃goal/∀constraint→分开连续轨迹、生成过程与tool执行；2+1+2=5 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)602视频生成评价 |
| [More Than Bits: Multi-Envelope Double Binary Factorization for Extreme Quantization](https://arxiv.org/html/2512.24545v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:14:28+08:00 | inner rank不解除幅度envelope约束→multi-envelope分自由度→分开fixedmask近似与实际执行成本；2+1+2=5 | 深入完成 | 整合：INFER-TENSORRT-LLM，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)936/938 ternary前 |
| [PackKV: Reducing KV Cache Memory Footprint through LLM-Aware Lossy Compression](https://arxiv.org/html/2512.24449v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:12:13+08:00 | 量化后codec与GEMV消费耦合→K/V contraction不同方向→分开误差、buffer/frontier与真实Serving成本；2+2+2=6 | 深入完成 | 整合：INFER-KV-CACHE，[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)658/660 MosaicKV后 |
| [Dream2Flow: Bridging Video Generation and Open-World Manipulation with 3D Object Flow](https://arxiv.org/html/2512.24766v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:19:40+08:00 | 视频状态变化不等动作→metric flow/controller分责→核RGB-D尺度锚与执行；2+2+3=7 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA，[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)400/402 |
| [From Sequential to Spatial: Reordering Autoregression for Efficient Visual Generation](https://arxiv.org/html/2512.24639v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:16:41+08:00 | raster串行→overlap ring/历史修正→明确newedge mask与mutable cache权限；2+2+3=7 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS，[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)61/63 |
| [Taming Hallucinations: Boosting MLLMs' Video Understanding via Counterfactual Video Generation](https://arxiv.org/html/2512.24271v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:08:00+08:00 | paired两域→L1优势proxy重权→不把proxy等权当真实gradient均衡；2+2+2=6 | 深入完成 | 整合：TRAIN-GRPO，[Ch33](../../../../books/part-04-training-system/33-grpo.md)469/471 |
| [RAGPart & RAGMask: Retrieval-Stage Defenses Against Corpus Poisoning in Retrieval-Augmented Generation](https://arxiv.org/html/2512.24268v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:07:56+08:00 | 分片表示身份→embed-before-mix/top-p聚合→多数决策保证不自动迁移；2+2+2=6 | 深入完成 | 整合：AGENT-RAG，[Ch76](../../../../books/part-07-agent/76-rag.md)867/869 |
| [Real-world Reinforcement Learning from Suboptimal Interventions](https://arxiv.org/html/2512.24288v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:08:24+08:00 | human不总最优→dispersion调statewise模仿容忍→分支持域/量纲/安全保证；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA，[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)248/250；uniform κ局部争议隔离 |
| [Constrained Language Model Policy Optimization via Risk-aware Stepwise Alignment](https://arxiv.org/html/2512.24263v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:07:49+08:00 | nested risk token目标→stepwise cost/temperature映射→中心符号与派生loss不一致；2+2+3=7 | 争议 | 暂缓：Eq10/12成本符号、reward温度与Eq13–15派生身份待修订，不否全部实测 |
| [SenseNova-MARS: Empowering Multimodal Agentic Reasoning and Search via Reinforcement Learning](https://arxiv.org/html/2512.24330v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:09:25+08:00 | 两级advantage normalizer→同G非零std后二级identity/公共常数→中心批级纠尺度贡献待澄清；2+2+2=6 | 争议 | 暂缓：有效group/mask/epsilon/实现定义需解释新增作用，不以tool组合替代中心增量 |
| [VLA-RAIL: A Real-Time Asynchronous Inference Linker for VLA Models and Robots](https://arxiv.org/html/2512.24673v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:17:29+08:00 | 异步chunk接口→局部时间对齐/C2接合→连续command不等时间真值或物理硬限；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA，[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)655 |
| [Figure It Out: Improving the Frontier of Reasoning with Active Visual Thinking](https://arxiv.org/html/2512.24297v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:08:37+08:00 | source crop到生成diagram→teacher suitability训练调用激励→分hypothesis来源与反事实证据收益；2+1+2=5 | 深入完成 | 整合：AGENT-TOOL-CALLING，[Ch78](../../../../books/part-07-agent/78-tool-calling.md)214 |
| [Mirage: One-Step Video Diffusion for Photorealistic and Coherent Asset Editing in Driving Scenes](https://arxiv.org/html/2512.24227v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:06:58+08:00 | 压时feature不保逐帧配对→最后两upsampling层注入2D detail→限定decoder接口、训练与回退；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS，[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)863/865 Output Decoder条件接口 |
| [CorGi: Contribution-Guided Block-Wise Interval Caching for Training-Free Acceleration of Diffusion Transformers](https://arxiv.org/html/2512.24195v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:06:12+08:00 | 整block旧output抹当前residual→module增量与interval锚点/局部ATTN refresh→限定缓存对象；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS，[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)1078/1080 |
| [Guiding a Diffusion Transformer with the Internal Dynamics of Itself](https://arxiv.org/html/2512.24176v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:05:45+08:00 | 双路径求值→同noise/time受训中间与最终readout外推→分参照误差与训练权限；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS，[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)1169/1171 |
| [DiffThinker: Towards Generative Multimodal Reasoning with Diffusion Models](https://arxiv.org/html/2512.24165v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:05:29+08:00 | image solution→可解析输出与task evaluator分责→不由固定NFE授内部search或正确性；2+2+2=6 | 标准完成 | 已有覆盖：MULTIMODAL-GENERATIVE-PARADIGMS，[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)typed parser与生成预算 |
| [Training Report of TeleChat3-MoE](https://arxiv.org/html/2512.24157v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:05:17+08:00 | 同packed length不等可见token-pair cost→按EoD subsequence组成重分样本→区别样本与layer调度；2+2+2=6 | 深入完成 | 整合：TRAIN-PIPELINE-PARALLEL，[Ch38](../../../../books/part-04-training-system/38-pipeline-parallel.md)264 |
| [Taming Preference Mode Collapse via Directional Decoupling Alignment in Diffusion Reinforcement Learning](https://arxiv.org/html/2512.24146v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:05:01+08:00 | proxy优化人口自变→冻结G学条件再冻结条件学G→评分instrument与policy参数权限分阶段；2+2+2=6 | 深入完成 | 整合：TRAIN-RLHF，[Ch31](../../../../books/part-04-training-system/31-rlhf.md)799 |
| [GARDO: Reinforcing Diffusion Models without Reward Hacking](https://arxiv.org/html/2512.24138v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:04:49+08:00 | proxy/aux相对差选择KL人口、reset改变锚点→分开selected population与reference identity；2+2+2=6 | 深入完成 | 整合：TRAIN-RLHF，[Ch31](../../../../books/part-04-training-system/31-rlhf.md)286 beta后 |
| [Activation Steering for Masked Diffusion Language Models](https://arxiv.org/html/2512.24143v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:04:57+08:00 | projection重复于reverse step→干预scope与拒答/内容/utility分责；2+1+2=5 | 标准完成 | 已有覆盖：MODEL-MULTI-HEAD-ATTENTION，[Ch15](../../../../books/part-02-model/15-multi-head-attention.md)279–284白盒子空间；PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)688–690同人口测量 |
| [Unified Embodied VLM Reasoning with Robotic Action via Autoregressive Discretized Pre-training](https://arxiv.org/html/2512.24125v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:04:31+08:00 | action codec仍需连续FM求解→QA/grounding反侧→分开tokenizer预算与闭环成功；2+2+2=6 | 标准完成 | 已有覆盖：MULTIMODAL-EMBODIED-VLA，[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)151–164 codec/refiner预算与freshness |
| [GeoBench: Rethinking Multimodal Geometric Problem-Solving via Hierarchical Evaluation](https://arxiv.org/html/2512.24119v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:04:22+08:00 | path绑定六MC gold→合法替代证明/parser/CoT预算分责→限定过程评价权限；2+2+2=6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)367–410合法acceptance/过程oracle/paired output事件 |
| [Autoregressivity in the Latent Space of a GP-VAE Language Model: An Empirical Ablation Study](https://arxiv.org/html/2512.24102v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:03:58+08:00 | K→diag(K)消融与same GP regularization身份未统一→中心相关性归因待澄清；2+1+2=5 | 争议 | 暂缓：精确train prior/KL/采样covariance及对应结果身份，不断言实现必错或全部实测无效 |
| [CEC-Zero: Zero-Supervision Character Error Correction with Self-Generated Rewards](https://arxiv.org/html/2512.23971v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:00:51+08:00 | thresholded相似度/簇共识作为label-free reward→核无偏语义目标条件；2+1+2=5 | 争议 | 暂缓：margin/purity不足以支持Lemma1无偏等价及依赖证明，不进入Books |
| [iCLP: Large Language Model Reasoning with Implicit Cognition Latent Planning](https://arxiv.org/html/2512.24014v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:01:51+08:00 | 离散LP前缀与显式CoT交替→codec/扩词表/checkpoint接口及总token分账；2+2+2=6 | 深入完成 | 整合：MODEL-DECODER-ONLY，[Ch18](../../../../books/part-02-model/18-decoder-only.md)279 |
| [AHA: Aligning Large Audio-Language Models for Reasoning Hallucinations via Counterfactual Hard Negatives](https://arxiv.org/html/2512.24052v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:02:46+08:00 | caption偏好标签与真实acoustic支持/独立评价分开→限制hallucination归因；2+2+2=6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)572–600输入支持与annotation/judge代理边界 |
| [Efficient Context Scaling with LongCat ZigZag Attention](https://arxiv.org/html/2512.23966v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:00:43+08:00 | 结束checkpoint校准选层再rewind训练→selection/即时转换/retrain三身份分账；2+2+2=6 | 深入完成 | 整合：MODEL-LONG-CONTEXT，[Ch22](../../../../books/part-02-model/22-long-context.md)800 |
| [Improving Multi-step RAG with Hypergraph-based Memory for Long-Context Complex Relational Modeling](https://arxiv.org/html/2512.23959v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:00:34+08:00 | query-local实体集合/update/merge改变下一retrieval范围→分派生关系与原事实支持；2+2+2=6 | 深入完成 | 整合：AGENT-MEMORY，[Ch77](../../../../books/part-07-agent/77-memory.md)360 |
| [Energy-Tweedie: Score meets Score, Energy meets Energy](https://arxiv.org/html/2512.23818v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T10:57:20+08:00 | Gaussian mean不足非Gaussian score→固定posterior/noise匹配加权残差→重考denoising接口；2+2+3=7 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS，[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)137/139噪声接口 |
| [Learning to Feel the Future: DreamTacVLA for Contact-Rich Manipulation](https://arxiv.org/html/2512.23864v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T10:58:22+08:00 | tactile空间对齐/未来条件→核draft-action预测与两次policy训练身份；2+2+2=6 | 争议 | 暂缓：W/F、hidden/CLIP及L_W目标/配对未明，不采预测训练因果链 |
| [Max-Entropy Reinforcement Learning with Flow Matching and A Case Study on LQR](https://arxiv.org/html/2512.23870v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T10:58:30+08:00 | proposal importance-weighted FM→核support/密度与policy理论权限；2+2+3=7 | 争议 | 暂缓：literal argmax与proof argmin冲突，隔离对应收敛链不否Alg2实测 |
| [The Drill-Down and Fabricate Test (DDFT): A Protocol for Measuring Epistemic Robustness in Language Models](https://arxiv.org/html/2512.23850v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T10:58:03+08:00 | compression×连续fabrication协议→核触发人口与支持丢失身份；2+2+2=6 | 争议 | 暂缓：compression/实际trigger分母/HOC定义不明，不采robustness或内部机制实证 |
| [A Test of Lookahead Bias in LLM Forecasts](https://arxiv.org/html/2512.23847v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T10:57:59+08:00 | forecast泄漏代理→交互回归识别条件→核线性残差与成员真值权限；2+2+3=7 | 争议 | 暂缓：Eq6与合法模型反例冲突，不采用中心iff识别链或成员proxy真值 |
| [Adversarial Lens: Exploiting Attention Layers to Generate Adversarial Examples for Evaluation](https://arxiv.org/html/2512.23837v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T10:57:45+08:00 | 中层替token与再生成可能变义→攻击候选与独立gold分责；2+1+2=5 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)1634–1638/886–889语义保持及独立gold；非已有lens算法 |
| [Large Language Models Are Poor at Signaling Their Ignorance When Given Irrelevant Context](https://arxiv.org/html/2512.23836v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T10:57:44+08:00 | 顺序负窗口反复暴露→first-positive条件人口→分开单次拒答与多窗口早停权限；2+2+2=6 | 深入完成 | 整合：AGENT-RAG，[Ch76](../../../../books/part-07-agent/76-rag.md)489 sufficiency后 |

| [Implicit score matching meets denoising score matching: improved rates of convergence and log-density Hessian estimation](https://arxiv.org/html/2512.24378v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:10:32+08:00 | score函数拟合不足导数拟合→高阶Sobolev/noise条件→分开函数/导数/solver误差；2+2+3=7 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS，[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)192 score敏感性后 |
| [Score-based sampling without diffusions: Guidance from a simple modular scheme](https://arxiv.org/html/2512.24152v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:05:10+08:00 | SLC条件子抽样替反向扩散→uniform误差及oracle预算→核版本/条件权限；2+2+3=7 | 争议 | 暂缓：v1 header Dec30/body Aug24 2026身份冲突，不采用当时正文定理/新runtime |
| [On Exact Editing of Flow-Based Diffusion Models](https://arxiv.org/html/2512.24015v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:01:53+08:00 | 三速度差分分state/condition→校正目标须保identity边界→核exact reconstruction权限；2+1+2=5 | 争议 | 暂缓：条件算子/位移与state目标未明，literal零编辑校正仍产生偏移；不否全部实测 |
| [Constraint Breeds Generalization: Temporal Dynamics as an Inductive Bias](https://arxiv.org/html/2512.23916v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T10:59:33+08:00 | 输入耗散与网络积分不同接口→跨编码/非单调局部转移→限定architecture与memory取舍；2+2+2=6 | 标准完成 | 仅报告：受限编码/integration敏感性未给foundation统一选择规则，非用小模型/局部自动排除 |
| [DriveExplorer: Images-Only Decoupled 4D Reconstruction with Progressive Restoration for Driving View Extrapolation](https://arxiv.org/html/2512.23983v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:01:07+08:00 | rendered dynamic-mask/pseudoimage进入denoiser→proxy条件与生成伪真值分责；1+2+2=5 | 标准完成 | 已有覆盖：MULTIMODAL-GENERATIVE-PARADIGMS，[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)1207相机训练条件/proposal与预算；非已有mask算法 |
| [Rethinking Dense Linear Transformations: Stagewise Pairwise Mixing (SPM) for Near-Linear Training in Neural Networks](https://arxiv.org/html/2512.23905v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T10:59:18+08:00 | 成对级联投影替dense→pairing/stage-depth限制容量及kernel反转→分开operator表达与执行成本；2+1+2=5 | 深入完成 | 整合：MODEL-FFN，[Ch16](../../../../books/part-02-model/16-feed-forward-mlp.md)206 GEMM前；隔离联合质量/速度headline |
| [How and Why LLMs Generalize: A Fine-Grained Analysis of LLM Reasoning from Cognitive Behaviors to Low-Level Patterns](https://arxiv.org/html/2512.24063v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:03:02+08:00 | 终局准确掩盖操作行为→behavior任务与辅助提示人口→核实际scorer身份；2+2+2=6 | 争议 | 暂缓：explicit self-check与final-boxed-only评价冲突，隔离行为/SAE因果/安全权限 |
| [Fantastic Reasoning Behaviors and Where to Find Them: Unsupervised Discovery of the Reasoning Process](https://arxiv.org/html/2512.23988v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:01:15+08:00 | step残差SAE发现与干预→风格/正确性及readout标签分责；2+1+2=5 | 标准完成 | 已有覆盖：MODEL-MULTI-HEAD-ATTENTION，[Ch15](../../../../books/part-02-model/15-multi-head-attention.md)279–284 sensor/verifier与副作用；PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)SAE source-label权限 |
| [T2VAttack: Adversarial Attack on Text-to-Video Diffusion Models](https://arxiv.org/html/2512.23953v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:00:25+08:00 | prompt扰动/flow降低代理→条件等价、baseline-success人口与motion质量分账；2+2+2=6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)4120–4127反事实/proxy结构及stored-stimulus/人口；非已写逐词search算法 |

| [RainFusion2.0](https://arxiv.org/html/2512.24086v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:03:34+08:00 | block均值仅筛support→窗口邻接/首帧强制角色与归一化分责→核稀疏质量和执行边界；2+2+2=6 | 标准完成 | 已有覆盖：MODEL-SELF-ATTENTION，[Ch14](../../../../books/part-02-model/14-self-attention.md)284–300支持选择/normalization、base-rescue与required-mask union；局部首帧/3D recipe留报告 |
| [Graph-Based Exploration for ARC-AGI-3 Interactive Reasoning Tasks](https://arxiv.org/html/2512.24156v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:05:16+08:00 | training-free tried-state/action与frontier局部探索→核LLM必要性的受限反证与预算人口；2+2+2=6 | 标准完成 | 仅报告：局部探索recipe/非全预算匹配LLM对照不足改变通用规划选择；hash/partial-state与fulltrace已有，但不称本算法已覆盖 |
| [PipeFlow: Pipelined Processing and Motion-Aware Frame Selection for Long-Form Video Editing](https://arxiv.org/html/2512.24026v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:02:09+08:00 | 全帧编辑成本→segment inversion/edit依赖与跳帧重建/overlap→重考长视频局部支持和排程预算；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS，[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)1452 segment编辑依赖/插值与dense回退 |
| [PhyAVBench: A Challenging Audio Physics-Sensitivity Benchmark for Physically Grounded Text-to-Audio-Video Generation](https://arxiv.org/html/2512.23994v1) | 2026-01-01T09:00:00+08:00 ～ 2026-01-01T11:01:23+08:00 | 音画同步不验物理变量响应→paired single-factor与现实均值差方向→限定测量分账；2+2+2=6 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)4066 成对方向协议；proposed非全面模型评价 |

## 4. 证据与知识整合

共同日期证据：[官方holiday公告](https://blog.arxiv.org/2025/11/21/temporary-changes-to-announcement-schedule-due-to-end-of-year-holidays-2025/)明确accepted Dec29 14ET～Dec31 14ET发表于Dec31 20ET，即Jan1 09BJT；[官方availability规则](https://info.arxiv.org/help/availability.html)明确identifier不能advance提供且不backdate，与实际已创建/注册的DOI共同给公开上界。按原始created秒精度保守取下一秒作为exclusive upper，不把Submitted、Updated或registered视作首次公开。原字段见[111份实际元数据](../_sources/daily-20260102/DATACITE_POTENTIAL.json)、[补恢复四份](../_sources/daily-20260102/DATACITE_RECOVERED_4.json)、[mHC原值](../_sources/daily-20260102/MHC_DATE.json)。已有更早同正文公开优先，相关7项已按[前公开原始链接](../_sources/daily-20260102/PRIOR_PUBLICATION.md)排除本窗首次公开，不声称旧报告已审。UniAct仅有窗前机制公开上界，不据此宣称v1全部实验窗前；RLM本窗事件另列重要新证据而非首次。

### [mHC: Manifold-Constrained Hyper-Connections](https://arxiv.org/html/2512.24880v1)

必要§4.1/4.2/5.4只支持理想双随机carry保存恒定均值方向，非所有差异方向或全网Jacobian保证；有限Sinkhorn有误差，多流状态/访存不是免费。root作者写入Ch17，jan01非作者必要证据及实际写后通过，详见[mHC证据](../_sources/daily-20260102/MHC_SOURCE_REVIEW.md)。

### [Reliable and Resilient Collective Communication Library for LLM Training and Serving](https://arxiv.org/html/2512.25059v1)

§4 completion/ACK/same-buffer、§5/6故障排程、§8.1–8.3限定fault domain；发送端退首个未完成chunk、接收端回最后确认进度，不写双方退同一位置。GPT-3 2.7B非32.7B，未实跑公开代码。Ch36实际增量及非作者写后已通过，必要配置见[第一批证据](../_sources/daily-20260102/EVIDENCE_BATCH_1.md)。

### [MSched: GPU Multitasking via Proactive Memory Scheduling](https://arxiv.org/html/2512.24637v1)

§5/6已知template/双CE/page-ready，不是未知未来OPT；working-set reserve和pointer chasing fallback保留。consumer GPU不是HBM，UM thrashing的倍率不和resident路径混比。Ch54实际正文及末注root写后通过，见[第一批证据](../_sources/daily-20260102/EVIDENCE_BATCH_1.md)。

### [Can Small Training Runs Reliably Guide Data Curation? Rethinking Proxy-Model Practice](https://arxiv.org/html/2512.24503v1)

§3逆转、§5定理/precision lower bound、§6及D.1.2支持data-dependent recipe交互而非特定数据普遍最佳；32×H10080GB已披露，代码未复现。Ch27实际两段与邻接root通过，见[第一批证据](../_sources/daily-20260102/EVIDENCE_BATCH_1.md)。

### [Understanding LLM Checkpoint/Restore I/O Strategies and Patterns](https://arxiv.org/html/2512.24511v1)

§3.2粒度、3.4 direct/cached与3.5 restore allocation分开；混合O_DIRECT写/buffered读没有改进且最多3倍差，不能由小读microbench推荐混合路径。Ch35实际两段root通过，见[第一批证据](../_sources/daily-20260102/EVIDENCE_BATCH_1.md)。

### [Modeling Language as a Sequence of Thoughts](https://arxiv.org/html/2512.25026v1)

§3.1–3.3/4.1–4.4 Table1/B/C.1/§5：visible rolling容量有限，递归训练祖先仍可更长；detach/reset改变credit horizon并影响PPL/cost，非免费删activation。小WikiText对照不外推工业scale/inference速度或已解决reversal curse。Ch22实际两段root必要源/写后通过，见[第二批证据](../_sources/daily-20260102/EVIDENCE_BATCH_2.md)。

### [Diffusion Language Models are Provably Optimal Parallel Samplers](https://arxiv.org/html/2512.25014v1)

§2–4及必要证明：uniform even-parity采样、L=n无extra workspace、固定深度poly-size AC0及每轮given-state位置独立；一般构造O(log d)不是d增长时固定深度。revision临时state不是最终输出，步数/空间/每步计算非hardware速度。Ch24实际两段root必要源/写后通过，见[第二批证据](../_sources/daily-20260102/EVIDENCE_BATCH_2.md)。

### [Many Minds from One Model: Bayesian Transformers for Population Intelligence](https://arxiv.org/html/2512.25063v1)

§3–7/limitations每sequence缓存norm扰动的有限探索成立；majority reward不等truth，参数mean/noise rollout的likelihood一致性未证明，TTRL peak不等稳定优势。仅报告处置经root通过，见[第二批证据](../_sources/daily-20260102/EVIDENCE_BATCH_2.md)。

### [Large language models and the entropy of English](https://arxiv.org/html/2512.24969v1)

Eq1–5、语料及训练B/C区分cross-entropy/code length/model conditional entropy与真实英语entropy；相关不因果。已有覆盖只指Ch22 length/content/unit/model条件分账，不称覆盖特定code-length命题；root必要源及NoChange通过，见[第二批证据](../_sources/daily-20260102/EVIDENCE_BATCH_2.md)。

### [RepetitionCurse: Measuring and Understanding Router Imbalance in Mixture-of-Experts LLMs under DoS Stress](https://arxiv.org/html/2512.23995v1)

§3.3/Eq3–4/4.1/4.2/4.3/5.3分开router模拟、本地kernel与remote平均TTFT；无法由remote异常识别隐藏MoE、EP规模、tail SLO或服务停机。placement缓解只有模拟建议，无完整防御保证。Ch21实际两段root写后通过，见[安全四项](../_sources/daily-20260102/EVIDENCE_BATCH_3_SAFETY.md)。

### [Breaking Audio Large Language Models by Attacking Only the Encoder: A Universal Targeted Latent-Space Audio Attack](https://arxiv.org/html/2512.23881v1)

§3/4/5 Tables1–2/6支持target-specific通用数字waveform与encoder梯度能力；转录不是command effect，无跨decoder或物理播放实证，不同loss的优化吞吐不能拼等成功预算优势。Ch72实际两段root写后通过，见[安全四项](../_sources/daily-20260102/EVIDENCE_BATCH_3_SAFETY.md)。

### [Jailbreaking Attacks vs. Content Safety Filters: How Far Are We in the LLM Safety Arms Race?](https://arxiv.org/html/2512.24044v1)

Eq8 Pass只filter未检出、不含Judge harmful成功indicator；Table4 s/sample与正文ms/sample冲突，故不采用成本/安全优势。Ch72共同模型人口、处理次序、阈值及正常utility另验已承载设计选择，不以错误口径发明普遍定律。root必要源及NoChange通过，见[安全四项](../_sources/daily-20260102/EVIDENCE_BATCH_3_SAFETY.md)。

### [Safe in the Future, Dangerous in the Past: Dissecting Temporal and Linguistic Vulnerabilities in LLMs](https://arxiv.org/html/2512.24556v1)

§3/4矩阵/6及audit：同60goal×language×framing不能按1440 iid；Hausa方向不普遍，complex-interference内部机制未证明。Ch66实际language/safety slice和sameprompt相关性覆盖，root原源/NoChange通过，见[安全四项](../_sources/daily-20260102/EVIDENCE_BATCH_3_SAFETY.md)。

### [Scaling Open-Ended Reasoning To Predict the Future](https://arxiv.org/html/2512.25070v1)

§3–7/H使用offline月快照而非在线时间过滤；训练resolution日期heuristic和test的Grok筛选1000→302改变人口，Accuracy+Brier只支持内部局部行为。Ch27 953–957已具体承载time-cutoff执行、snapshot旧路及timestamp/teacher偏差，不声称覆盖未知的普适最优reward。root必要原源与具体已有覆盖通过，见[评价批次](../_sources/daily-20260102/EVIDENCE_BATCH_4_EVALUATION.md)。

### [Efficiently Estimating Data Efficiency for Language Model Fine-tuning](https://arxiv.org/html/2512.24991v1)

§3.1线性n AUC公式与§4 log2描述冲突；32-label LoRA-gradient proxy的受测曲线和跨task回归不提供唯一预算或跨model系数。必要机制/评价/反证已作者和root实际读，因中心口径暂缓预算采用，不缩池或冒充已有覆盖，见[评价批次](../_sources/daily-20260102/EVIDENCE_BATCH_4_EVALUATION.md)。

### [VLN-MME: Diagnosing MLLMs as Language-guided Visual Navigation agents](https://arxiv.org/html/2512.24851v1)

§4.1–4.4/D4/D8的replan与log-only语义不一致；cached图上四视图navigation、selected loop slice及oracle改指令对照不能证明真实连续控制或唯一内部根因。root已核原矛盾；已读不等中心claim成立，暂缓reflection控制与因果采用，见[评价批次](../_sources/daily-20260102/EVIDENCE_BATCH_4_EVALUATION.md)。

### [Encyclo-K: Evaluating LLMs with Dynamically Composed Knowledge Statements](https://arxiv.org/html/2512.24867v1)

§3/5.2/6将statement pool与question instance分开，五seed排序稳定不证明免污染，position非paired及thinking budget不同保留。具体长期gap已融入Ch66 2907/2909两段及末注，root必要原源、实际2896–2924前后与末注POST通过，见[评价批次](../_sources/daily-20260102/EVIDENCE_BATCH_4_EVALUATION.md)。

### [Youtu-LLM: Unlocking the Native Agentic Potential for Lightweight Large Language Models](https://arxiv.org/html/2512.24618v1)

采用限§4.2.2/Fig13 CF-GRPO prompt-level K估计→整组admission→条件P(Q\|K<τ)目标；不授原人口无偏、普遍FP16优势或全模型能力因果。Ch33 2091/2093两段及末注实际整合，root必要原源与2080–2105衔接POST通过，见[优化批次](../_sources/daily-20260102/EVIDENCE_BATCH_5_OPTIMIZATION.md)。

### [LoongFlow: Directed Evolutionary Search via a Cognitive Plan-Execute-Summarize Paradigm](https://arxiv.org/html/2512.24077v1)

§4.1.1/Algorithm1及5.4限同parent-ID反馈复用与局部/完整评价分层，summary不是causal事实；MAP-Elites组合/科学奖牌不计增量。Ch79 177/179两段及末注实际融入搜索边界，root必要原源与165–185正文/末注POST通过，见[core记录](../_sources/daily-20260102/CORE_ADMISSION_3.md)。

### [RANGER: A Monocular Zero-Shot Semantic Navigation Framework through Contextual Adaptation](https://arxiv.org/html/2512.24212v1)

§IV–VI尤其VI-C限单目offline bank的camera-height尺度与initial relocalization前提，不采正文/表冲突SR；有限HM3D单floor与G1配置非任意陌生场景安全。Ch26 141/143两段及末注实际融入controller，root必要原源及132–154正文/末注POST通过，见[core记录](../_sources/daily-20260102/CORE_ADMISSION_3.md)。

### [RSAgent: Learning to Reason and Act for Text-Guided Segmentation via Multi-Turn Tool Invocations](https://arxiv.org/html/2512.24023v1)

§3/4.3必要控制支持历史失败不模仿、正确中间mask/prefix复用及8turn饱和，不承诺更多tool更好。Qwen2.5-VL7B/SAM2large训练预算与baseline不全匹配，hardware/precision未披露。Ch29 142–150/566–578实际已有窄论点，root必要原源和具体coverage限定通过，不追加局部segmentation reward配方，见[core记录](../_sources/daily-20260102/CORE_ADMISSION_3.md)。

### [HaluNet: Multi-Granular Uncertainty Modeling for Efficient Hallucination Detection in LLM Question Answering](https://arxiv.org/abs/2512.24562v1)

single-QA multi-signal detector有局部选择，但不构成新的真伪verifier或通用校准机制；身份/落窗与1+1+2=4关闭经root完整题摘校准，不授性能或代码审阅，见[优化批次](../_sources/daily-20260102/EVIDENCE_BATCH_5_OPTIMIZATION.md)。

### [Collaborative Low-Rank Adaptation for Pre-Trained Vision Transformers](https://arxiv.org/html/2512.24603v1)

§IV/V共享D/U与module Q，p(2dr+mr²)及rank≤pr不能免容量取舍；SADE Frobenius只是sample-free代理，93.9%正则项GFLOPs非端到端收益。5分具体长期缺口深入，Ch30 173/175正文及802末注root实际POST通过，见[优化批次](../_sources/daily-20260102/EVIDENCE_BATCH_5_OPTIMIZATION.md)。

### [Localized Calibrated Uncertainty in Code Language Models](https://arxiv.org/html/2512.24560v1)

§4–7/10定义intent/test/minimal-patch-kept标签；任意span保留不等整程序正确，patchability筛选及target-domain Platt必须单列。无cleanheldout、ECE低不等区分有用，多副本另付成本。5分具体缺口深入，Ch66 652/654及末注root实际POST通过，见[优化批次](../_sources/daily-20260102/EVIDENCE_BATCH_5_OPTIMIZATION.md)。

### [Exploring Compositionality in Vision Transformers using Wavelet Representations](https://arxiv.org/html/2512.24438v1)

§3.3/4原rawsum退化与learned readout支持受限head输出拟合，不授全latent homomorphism/唯一语义或真实分类改善。Ch23 63–65/101–103实际承载可读≠模型能用和probe/geometry的充分性边界；root必要原源与具体已有覆盖通过，不声称现书覆盖DWT公式，见[优化批次](../_sources/daily-20260102/EVIDENCE_BATCH_5_OPTIMIZATION.md)。

### [From Building Blocks to Planning: Multi-Step Spatial Reasoning in LLMs with Reinforcement Learning](https://arxiv.org/html/2512.24532v1)

§3–5的12k原子SFT/frozen base+rank64 GRPO adapter只支持有限ASCII确定性变换。冻结base不保adapter后的原子行为，Static/Dynamic观测不同、DirectRL不含12k同总预算，attention关联非因果。root必要原源与标准仅报告通过：不足建立技能保持/可发布规划分责保证，见[优化批次](../_sources/daily-20260102/EVIDENCE_BATCH_5_OPTIMIZATION.md)。

### [Vulcan: Instance-Optimal Systems Heuristics Through LLM-Driven Search](https://arxiv.org/html/2512.25065v1)

§3/4.1/5.1–5.2 fixed scaffolding只让LLM写Value/Rank或有限queue transition，signature/primitives非完整安全/成本证明；搜索trace与heldout分账，NUMA模拟不授CXL/LLM部署。6分具体缺口深入，Ch84 891/893正文及末注root实际POST通过，见[优化批次](../_sources/daily-20260102/EVIDENCE_BATCH_5_OPTIMIZATION.md)。

### [ResponseRank: Data-Efficient Reward Modeling through Preference Strength Learning](https://arxiv.org/html/2512.25023v1)

§2/5/8/D1–3排序comparison utility difference，strata不保证局部单调，RT真实失效、Stated小增益不显著、Random不迁移与Agree额外四标签保留。6分测量缺口深入，Ch31 97/99 BT后正文及末注root实际POST通过，未授downstream policy收益，见[反馈批次](../_sources/daily-20260102/EVIDENCE_BATCH_6_FEEDBACK.md)。

### [Iterative Deployment Improves Planning Skills in LLMs](https://arxiv.org/html/2512.24940v1)

§2/A.2的M_n继承与每代fixed-base LoRA口径不同；A.1 Prop1仅固定on-policy binary trace-gradient重写，Prop2 conditional ratio一般缺Zpi/Zbeta，不能补造完整多epoch RL等价。root已实际核中心争议安全暂缓，未写Books、不作正面Evidence，见[反馈批次](../_sources/daily-20260102/EVIDENCE_BATCH_6_FEEDBACK.md)。

### [Triangulation as an Acceptance Rule for Multilingual Mechanistic Interpretability](https://arxiv.org/html/2512.24842v1)

§2–4/6提出predicate-preserving family与predicate-swap source的不同角色，跨语言mapping/patch distortion另验，necessity/sufficiency/stability/cue falsifier均预注册；proposed protocol非已证实成功，重复干预不自动iid。5分具体缺口深入，Ch66 2803/2805正文及末注root实际POST通过，见[反馈批次](../_sources/daily-20260102/EVIDENCE_BATCH_6_FEEDBACK.md)。

### [Compute-Accuracy Pareto Frontiers for Open-Source Reasoning Large Language Models](https://arxiv.org/html/2512.24776v1)

§3/4.3–4.4/5的19跨model/config点用含KV/vocab的分析FLOPs，不含HBM/EP/runtime成本；未匹配fixed-checkpoint预算干预，长失败trace的关联不认证earlystop控制或MoE因果优势。root原源与6分标准仅报告通过：未建立可部署预算选择的长期新结论，见[反馈批次](../_sources/daily-20260102/EVIDENCE_BATCH_6_FEEDBACK.md)。

### [Recursive Language Models](https://arxiv.org/html/2512.24601v1)

REPL/递归接口与depth1/no-subcall机制在2025作者datedblog已公开，不计本窗首次；本窗v1新增Qwen/CodeQA/OOLONG-Pairs的model/task反证经root原源和旧dated稿定点比对确认重要新证据。§2.1–2.2/§3 Table1 Obs2/4/5/§5表明Qwen去subcall在CodeQA/BrowseComp更好，另两信息密集任务有收益，external access不等recursion收益；root/child配置、样本人群/evaluator、同步与API成本尾保留，不授10M可靠性或硬件总成本。Ch75 247/249与末注root实际正文/邻接POST通过；[本批证据](../_sources/daily-20260102/EVIDENCE_BATCH_7_STATE.md)、[窗前原稿](../_sources/daily-20260102/RLM_PRIOR_PRIMARY_CACHE.md)。

### [Dynamic Large Concept Models: Latent Reasoning in an Adaptive Semantic Space](https://arxiv.org/html/2512.24617v1)

§3.3.2 Eq7、§3.4–3.5 Eq11–14、§4.1 Eq17与§6.1的完整segment pooling/current j(t)未交代shift或completed-concept；concept causal mask与repeat_interleave不能独自排除pool内部未来依赖。root核中心争议暂缓，未验证实现泄漏、不推荐因果NTP或compression最优；正文August24,2026与v1/DOI字段、R目标及预算口径冲突保留，不补造一致。7分/已读机制保留、不作正面Evidence、不入Books，详[本批证据](../_sources/daily-20260102/EVIDENCE_BATCH_7_STATE.md)。

### [Thinking on Maps: How Foundation Model Agents Explore, Remember, and Reason Map Environments](https://arxiv.org/pdf/2512.24504v1)

必要PDF §3.2.3/4.1.1/4.2.1–2/Table4/§5.5支持任务需要的connectivity/metric/direction/chronology分责；工程化符号地图的使用不证明自主形成内部memory，每POI至少一次coverage-stop不等step/token预算。不同表征/推理阶段不是同总budget，bits表不授实际序列化/硬件成本或NSM普遍最优。Ch77 39/41及末注root原源/actual owner/正文邻接写后通过，详[本批证据](../_sources/daily-20260102/EVIDENCE_BATCH_7_STATE.md)。

### [OptRot: Mitigating Weight Outliers via Data-Free Rotations for Post-Training Quantization](https://arxiv.org/html/2512.24124v1)

§3–5必要机制/反例只支持权重第四次矩旋转代理、data-free学习步骤权限及W4A8/W4A4/RTN选择反转；constrained LDL的局部界不授ordinary LDL或整网质量，后续GPTQ仍需calibration，不采吞吐。Ch49 1139/1141及末注root实际正文/FreeAct邻接写后通过，详[本批证据](../_sources/daily-20260102/EVIDENCE_BATCH_8_COMPRESSION_SELECTION.md)。

### [Improved Bounds for Private and Robust Alignment](https://arxiv.org/html/2512.23816v1)

§2–5及相关B/C归约限二元BT labels/realizable bounded reward；RR observed likelihood、c缩放及CTL/LTC条件均值偏差和平方误差不同，offline/online的支持/污染假设不同，不授文本隐私或神经argmin。Ch31 101/103及末注root实际正文/前后score例子写后通过，详[本批证据](../_sources/daily-20260102/EVIDENCE_BATCH_8_COMPRESSION_SELECTION.md)。

### [Pretraining Frame Preservation in Autoregressive Video Memory Compression](https://arxiv.org/html/2512.23851v1)

§3/4必要方法/对照限随机任意历史位置重建、低res与高频residual路径；equal AR steps不等equal totalpretrain，PSNR/外观/运动不同人口，ELO排除严重artifact不授无限continuousshot或worldstate。Ch24 89/91及末注root实际正文/Helios至Diffusion衔接写后通过，详[本批证据](../_sources/daily-20260102/EVIDENCE_BATCH_8_COMPRESSION_SELECTION.md)。

### [Probing the Limits of Compressive Memory: A Study of Infini-Attention in Small-Scale Pretraining](https://arxiv.org/html/2512.23862v1)

§3–5/Table1及§6–9：retrieve-before-update与head gate使用是可观察机制，不证明有效远程retrieval或其因果收益。300M/FineWeb median418、padded length、LR对照不一及FT depth失败必须共同解释支持范围；不从0.4%>8192倒推全部≤1024，不将单depth改善外推为所有位置。Ch22 543/545及末注root实际正文/邻接写后通过，详[本批证据](../_sources/daily-20260102/EVIDENCE_BATCH_8_COMPRESSION_SELECTION.md)。

### [Joint Selection for Large-Scale Pre-Training Data via Policy Gradient-based Mask Learning](https://arxiv.org/html/2512.24265v1)

§2–4/6/7.2：单样本quality加总与集合diversity是不同目标，固定S不放回mask联合选择提供具体机制；分块丢跨块关系、proxy质量及总curation成本仍有限制。§6共享group mean/scale推导不授无条件无偏、低variance或全局最优；只采用受限stochastic set selection，不把selector速度当总训练收益。Ch27 246/248及末注root实际正文/邻接写后通过，详[本批证据](../_sources/daily-20260102/EVIDENCE_BATCH_8_COMPRESSION_SELECTION.md)。

### [Do Large Language Models Know What They Are Capable Of?](https://arxiv.org/html/2512.24661v1)

原2025-07-13作者页已公开single-step并明说future multi-step/ICL，本窗只计后两实验的新证据事件。v1§4–6/A/C.1/D.1/F的挑选50%能力人口、历史后profit与AUROC不同步及SWE499/70call提前提交forward-fill支持测量分账，不授内部rational解释/规模律。Ch66 2301/2303及末注root实际正文与邻接POST通过，详[本批证据](../_sources/daily-20260102/EVIDENCE_BATCH_9_MEASUREMENT.md)。

### [MCPAgentBench](https://arxiv.org/html/2512.24565v1)

v1§3–5中180手工task/uniquegold与GPT4o mock、TFS set及TEFS gold顺序支持具名call-format评价，不验真实effect/auth/state/recovery或替代合法plan。Ch66 367–380已有typed trace/effect/acceptance sets，1252附近已有mock替换/integration-state测试，root实际必要源/具体覆盖通过；不将TEFS或per1k单位冲突冒称正文已覆盖。详[本批证据](../_sources/daily-20260102/EVIDENCE_BATCH_9_MEASUREMENT.md)。

### [Understanding and Steering the Cognitive Behaviors of Reasoning Models at Test-Time](https://arxiv.org/html/2512.24574v1)

v1§3–5/B/C.2：keyword step probe为lexical proxy，feature split/同名calib评价与PCA/norm方向不授真实认知因果；模型/任务质量-token反例、不同调参阶段与未披露runtime收窄收益。Ch15 282/284已有whitebox局部projection/sensor/独立verifier/校准与副作用，Ch66对应decodable≠steering因果及fallback；root必要源与具体coverage通过，不追加重复正文、不声称含该exact recipe。详[本批证据](../_sources/daily-20260102/EVIDENCE_BATCH_9_MEASUREMENT.md)。

### [MultiRisk: Multiple Risk Control via Iterative Score Thresholding](https://arxiv.org/html/2512.24587v1)

v1§2 Eq1/§4/§5/D.2–D.6/§6/B/C只支持first-trigger provider成本及上游改变下游人口的联合阈值设计分账，不把它当残留unsafe率。Condition5.7仅给V的界，D5用正Vmin当乘indicator的L下界，未触发L=0；隔离该δ与具体递归保证权限，不授全部理论被反证，不自动用零下界补全证明。Ch66 2305/2307及末注root实际窄修/邻接POST通过；经验min/max、有限500cal/test及固定abstain也不授开放部署安全。详[本批证据](../_sources/daily-20260102/EVIDENCE_BATCH_9_MEASUREMENT.md)。

### [MUSIC: MUlti-Step Instruction Contrast for Multi-Turn Reward Models](https://arxiv.org/html/2512.24693v1)

v1 Alg1、§3.1–3.4/4.1–4.3/6限定branch-user共同演化与terminal reward对象；不把完整对话差异当同一外部state只替换一次动作，也不直接分配tool-step credit。固定脚本便于控制但牺牲交互，匹配反事实或独立用户人口评价是不同可用选择；simulator/teacher judge及追加数据/生成预算保留边界。Ch31 146/148两段与末注经root必要源及实际正文/邻接POST通过，5分因具体trajectory-pair知识缺口深入受影响内容。详[本批证据](../_sources/daily-20260102/EVIDENCE_BATCH_9_MEASUREMENT.md)。

### [AMAP Agentic Planning Technical Report](https://arxiv.org/html/2512.24957v1)

v1§2.4–3.3区分当前policy采样的reward mean/variance与静态teacher funnel，核全池每题8轨迹的预算及rubric/动态teacher权重权限；不将variance当epistemic真值或Travel指标改善授普遍保证。Ch27 560–610确已承载按当前checkpoint rollout判断sweet spot、更新retain/revise/retire及selector/generator/verifier分责，root必要源与具体coverage复核通过，不重复追加该领域recipe。详[本批证据](../_sources/daily-20260102/EVIDENCE_BATCH_10_DESIGN.md)。

### [ROAD: Reflective Optimization via Automated Debugging for Zero-Shot Agent Alignment](https://arxiv.org/html/2512.24040v1)

v1§3.1–3.3/Alg1与6.4把failure日志用于规则提案，但同D重复比较和YES文本均不构成独立验收或确定性执行guard。Ch74 125–164已有scope/validation与formal spec非行为保证，Ch80 40–120已有独立反馈、修复假设、预算/回退及权限边界；root必要原源/具体已有覆盖通过，不追加领域决策树recipe。详[本批证据](../_sources/daily-20260102/EVIDENCE_BATCH_10_DESIGN.md)。

### [Subsecond 3D Mesh Generation for Robot Manipulation](https://arxiv.org/html/2512.24428v1)

v1II-C/III-B/E、IV-C及V-A只支撑textureless表示与render消费者兼容性、单目shape和真实metric anchor的分责；25YCB/10runs不授开放抓取或subsecond全链性能。Ch26 69及末注root实际正文/邻接POST通过，5分因具体知识缺口深入受影响机制，不重复RANSAC教程。详[本批证据](../_sources/daily-20260102/EVIDENCE_BATCH_10_DESIGN.md)。

### [From Inpainting to Editing: A Self-Bootstrapping Framework for Context-Rich Visual Dubbing](https://arxiv.org/html/2512.25066v1)

v1§3/C.1/C.3/F四设置支持完整paired reference与编辑噪声目标的交互，editor/inpainting并非同一条件。stage区间训练/合成数据与adapter付费，D/E模型规模与耗时未统一，不授通用三阶段律或25秒同质量。Ch24 135及末注root实际正文/邻接POST通过，5分具体gap深入；详[本批证据](../_sources/daily-20260102/EVIDENCE_BATCH_10_DESIGN.md)。

### [PhyGDPO: Physics-Aware Groupwise Direct Preference Optimization for Physically Consistent Text-to-Video Generation](https://arxiv.org/html/2512.24551v1)

v1Eq2/3分母不含winner，所谓PL概率可大于1；Eq9两行符号不等，Eq10/default的正α仍可给γ<1/α，不满足Eq8条件。root实际核必要原公式和默认参数，中心推导安全终态暂缓；不自行修公式后授原训练链成立、不宣称全实测无效，8H100/BF16和LoRA事实不替group目标的新贡献。重开需作者合法概率/符号/权重条件澄清与精确实现loss身份。详[公式原文与反证](../_sources/daily-20260102/EVIDENCE_BATCH_11_INTERFACES.md)。

### [What drives success in physical planning with Joint-Embedding Predictive World Models?](https://arxiv.org/html/2512.24497v1)

必要§3–4、§5.1/5.2与B reproduction/multistep variants绑定target时间index、真值/自产context、detach与gradient path；作者报告错误并重训，未独立代码验证。两步到更长不单调，DROID ActionScore不等实机成功，step/搜索episode不等完整墙钟成本。Ch25 317/319及末注root实际原源、正文与邻接写后通过；[本批必要证据](../_sources/daily-20260102/EVIDENCE_BATCH_10_DESIGN.md)。

### [FlowBlending](https://arxiv.org/html/2512.24724v1)

exact-v1 §3.3/§4–6及直接质量反例深入支持capacity而非NFE的阶段分配；DINO/FID与同latent velocity差只提议离线切换，LDL的FVD反例阻止全部质量保持宣传。latent/time/condition兼容、重新校准、双模型驻留/switch费用与block成本非全链SLO落实Ch24 513，旧步数/蒸馏分支保留。root必要原源/具体owner与实际正文/前后/末注POST通过，未运行代码。必要对照见[批次原记录](../_sources/daily-20260102/EVIDENCE_BATCH_12_13_GENERATION.md)。

### [Are First-Order Diffusion Samplers Really Slower? A Fast Forward-Value Approach](https://arxiv.org/html/2512.24927v1)

exact-v1 §3.1/Alg1、§3.2 Assumption1/Theorems3–4与§4–5/Table4，因具体求值位置/cost gap深入受影响内容；lookahead估下一状态/time，理想implicit非部署oracle，平滑/网格/近似条件不自动授实际NN。有限步存在原solver更好对照，iterations、NFE/cache与真实成本分账融入Ch24 154，未遍历全附录证明或复现。root必要原源/owner与actual POST通过，不授普胜/硬件速度；必要原式/反例见同批记录。

### [Counterfactual VLA: Self-Reflective Vision-Language-Action Model with Adaptive Reasoning](https://arxiv.org/html/2512.24426v1)

exact-v1 §3.3–3.4/§4 Tables2–3及教师prompt，因training intervention/runtime gate缺口深入：同场景自由与GT预填各六rollouts，teacher实际看真值，错误首meta前缀不模仿，再混入no-Think人口。64A100/BF16/batch64/300k与额外教师/200K CF预算仅为作者设置；强制推理/AvgADE反侧保留，六mode离线驾驶轨迹非闭环实车安全。Ch26 628落实诊断/teacher/Think gate权限与controller fallback；root必要源/owner、实际正文/邻接/末注POST通过，未运行代码。必要原式、权重和对照见同批记录。

### [EchoFoley: Event-Centric Hierarchical Control for Video Grounded Creative Sound Generation](https://arxiv.org/html/2512.24731v1)

exact-v1 §6.1/B.2 execution/B.3/B.4支持事件state→独立segment生成与mix的实际消费接口，不只是when/what/how schema。因具体长期gap深入，Ch24 1173承载局部retime/regenerate与声学耦合、定位proposal、多个外部API/calls/混音预算及整体/人工fallback。自动100与human50×6评价人口分开；Temp/Timb/Vol平均文字与sum式、音色参考身份争议保留在[必要原记录](../_sources/daily-20260102/EVIDENCE_BATCH_12_13_GENERATION.md)，不采用这些数字。root必要原源/owner、实际正文/邻接/末注POST通过，未运行代码，不授真实声源/实时全链或质量保证。

### [Let It Flow: Agentic Crafting on Rock and Roll — Building the ROME Model within an Open Agentic Learning Ecosystem](https://arxiv.org/html/2512.24873v1)

exact-v1 §3.2.4.1–4/Eq5–7、rollback/anchor和§3.3.1因具体credit gap深入：同chunk权重不证明同token因果贡献，几何均值ratio非完整chunk联合概率比，backend mismatch mask改变学习人口。teacher prefix replay改变训练起点，不是部署可得事实；reset/teacher/rollout成本与组合对照不识别单模块因果。Ch33 1371接历史reference/current-sample后自然进入Immediate lifecycle，root必要原源/owner及正文/邻接/末注actual POST通过；必要原式和评价配置见同批记录，未运行代码、不授无偏off-policy或配方整体保证。

### [SpaceTimePilot: Generative Rendering of Dynamic Scenes Across Space and Time](https://arxiv.org/html/2512.25075v1)

exact-v1 §3.3 Eq3/time compressor/Table5与camera protocol反侧因具体animation-time gap深入。source/target各自camera/time身份、RGB到latent时钟压缩、temporal warp/合成grid support融入Ch24 1177；原position index不能兼任动画时间，不授任意4D一致、persistent world state。估姿/首两位置scale alignment非metric真值，synthetic retime与real-camera评价人口分开，训练/数据费用及fallback保留。root必要原源/owner与实际正文/邻接/末注POST通过，未运行代码，必要原式与反侧见[原批记录](../_sources/daily-20260102/EVIDENCE_BATCH_12_13_GENERATION.md)。

### [VIPER: Process-aware Evaluation for Generative Video Reasoning](https://arxiv.org/html/2512.24952v1)

exact-v1 §4.1 Eq2与§5/Table4因具体generated-process量词gap深入：OC存在goal帧、PC全采样帧满足constraint，联合接受限相同采样集合。采样率变化OC非单调、50 purposeful人审切片不估部署hacking率，309条/16任务与1fps/GPT5judge范围保留。Ch66 602衔接生成评价器→caption verification，采样合同不替tool receipt、内部reasoning或连续全片真值。root必要原源/owner及actual POST通过，未运行代码，同批缓存保必要反侧。

### [More Than Bits: Multi-Envelope Double Binary Factorization for Extreme Quantization](https://arxiv.org/html/2512.24545v1)

exact-v1 §3.2/§4.1–4.4/Theorem4.2、Eq12/Table1因factor-envelope具体gap深入。fixed sign后幅度envelope秩一与inner rank自由度不同，fixedmask TSVD只授factor近似，adaptive-mask ADMM不继承全局保证；l²项/metadata及更大l PPL退步阻止二值天然加速或整模型resident bits宣传。Ch49 936/938接共享格式成本后→ternary路径前，root必要原源/owner及actual正文/邻接/末注POST通过，未跑代码或复现；必要反侧见[原记录](../_sources/daily-20260102/EVIDENCE_BATCH_11_INTERFACES.md)。

### [PackKV: Reducing KV Cache Memory Footprint through LLM-Aware Lossy Compression](https://arxiv.org/html/2512.24449v1)

exact-v1 III-B–D/III-C、IV-E/IV-F因quant后codec与K/V消费方向具体gap深入。lossless只相对量化后整数，paired reorder保位置/mask对应，buffer完成再推进frontier；K warp点积与V atomic聚合不能共用无条件数值/布局承诺。replay collectedKV MatVec微基准不含全Prefill/softmax/请求SLO，独立多实例不证明TP/跨节点；编码/metadata与质量阈值仍付费。Ch45 658/660融入MosaicKV→mixedsparse主线，root必要源/owner和实际POST通过，未运行代码，同批保必要设置与反例。

### [Dream2Flow: Bridging Video Generation and Open-World Manipulation with 3D Object Flow](https://arxiv.org/html/2512.24766v1)

exact-v1 III/IV-B–F及H/I/J，metric flow需初始RGB-D/投影/scale anchor，仍经接触/动力学controller。有限样本/goal-image人口、形变遮挡/grasp与3–11分钟预处理不授实时或普适安全。Ch26 400/402实际融入中间计划论证，root必要原源/owner及正文/前后/末注POST通过，未运行代码或复现实验，见[原记录](../_sources/daily-20260102/EVIDENCE_BATCH_11_INTERFACES.md)。

### [From Sequential to Spatial: Reordering Autoregression for Efficient Visual Generation](https://arxiv.org/html/2512.24639v1)

exact-v1 §3/Eq1/Algorithm1/NAM/TPT和Tables1–4，overlap crop/ring并行与历史修正不同mask；Eq1非token joint exactness，mutable prefix不继承append-only KV。非fullfactorial、moreSteps反侧及未披露硬件/并发阻止倍率或cache免费宣传。Ch24 61/63与旧representation ordering论证自然衔接，root必要原源/owner及actual POST通过，未运行代码，见[原记录](../_sources/daily-20260102/EVIDENCE_BATCH_11_INTERFACES.md)。

### [Taming Hallucinations: Boosting MLLMs' Video Understanding via Counterfactual Video Generation](https://arxiv.org/html/2512.24271v1)

exact-v1 §4.2/Eq6/8/9、§5 Tables3–4/B.10–15，L1优势proxy与binary/format条件分账；Eq9/B10乘G、B15除G冲突保留，同G可能消去不否全部实测，token长度/reduction/score-gradient仍改变真实贡献。Ch33 469/471在DrGRPO后融入统计单位主线，root必要源/owner与正文/前后/末注POST通过；未运行代码，见[原记录](../_sources/daily-20260102/EVIDENCE_BATCH_14_INTERVENTION.md)。

### [RAGPart & RAGMask: Retrieval-Stage Defenses Against Corpus Poisoning in Retrieval-Augmented Generation](https://arxiv.org/html/2512.24268v1)

exact-v1 §3.1–3.2/§4/§6–7，只采用独立embed后组合与多候选权限；single-poison mix/benign一致性是分析假设，mask probe依赖initial support与预算。retrieval ASR/SR不验answer安全，贴题假事实非truth detector。Ch76 867/869实际放在生命周期安全论证下、Span取证前；root必要源/owner及搬移后POST通过，未运行代码，见[原记录](../_sources/daily-20260102/EVIDENCE_BATCH_14_INTERVENTION.md)。

### [Real-world Reinforcement Learning from Suboptimal Interventions](https://arxiv.org/html/2512.24288v1)

exact-v1 IV Eq3–12、V-A–F/VIII Eq18–22，intervention-only Gaussian dispersion是训练proxy；norm/std、squared norm/average std与variance版本分开。Eq20→22错误方向仅隔离uniform κ KL保证，不否全部实测；八任务/two embodiments与有限operator/扰动、critic/reward/SOP成本不授物理安全。Ch26 248/250受限online RL段后实际融入，root必要原源/owner及actual POST通过，未运行代码，见[原记录](../_sources/daily-20260102/EVIDENCE_BATCH_14_INTERVENTION.md)。

### [Constrained Language Model Policy Optimization via Risk-aware Stepwise Alignment](https://arxiv.org/html/2512.24263v1)

actual exact-v1 IV-B–D/V/A-C/B-C，Eq10固定λ内层成本减项与(1+λ)β温度，与Eq12正cost指数/错置reward温度冲突；两action固定λ=β=1、reward零、cost0/1反例分别给highcost .37754/.62246，不授任意d的λ*=1。Eq13–15 BT/SRR派生权限因此暂缓，非全部实测无效。2H10080GB/BF16/3epoch和公开Beaver基线/轻量LoRA配方人口不同；129/83生成judge与569风险识别F1不认证罕见灾难风险。root必要中心原式实际核并通过7分隔离，见[必要原式与反例](../_sources/daily-20260102/EVIDENCE_BATCH_14_INTERVENTION.md)。

### [SenseNova-MARS: Empowering Multimodal Agentic Reasoning and Search via Reinforcement Learning](https://arxiv.org/html/2512.24330v1)

exact-v1 §3.2 Eq2–4/§4.1/4.3 Table3，组内先标准化再全batch标准化；同G、非零variance及人口std时第二级恰identity，同sample-std时只改公共常数，不自动纠正prompt相对尺度。mask/sharding/epsilon/零组实现未披露，指标不能解除中心定义冲突；8B RL与7B SFT+RL预算分开，不否全部实测，也不以搜索工具组合补造另一个贡献。root必要原式/T3实际核并通过6分隔离，见[原定义记录](../_sources/daily-20260102/CORE_ADMISSION_3.md)。

### [VLA-RAIL: A Real-Time Asynchronous Inference Linker for VLA Models and Robots](https://arxiv.org/html/2512.24673v1)

actual exact-v1 IV-B–D/Eq8–14/Algorithm1与V/VI，chunk方向对齐proxy和双quintic端点/中点接合只授command C2，不授观测时间真值、速度/加速度硬限或tracking/safety。G1/RTX4080Laptop、20trial与成功时间口径、表SR冲突保留，不采用精确跨model差或噪声内因；同步/低层controller仍负责实际执行。Ch26 655及1764末注root必要原源/owner及正文/前后actual POST通过，未运行代码，见[原记录](../_sources/daily-20260102/CORE_ADMISSION_3.md)。

### [Figure It Out: Improving the Frontier of Reasoning with Active Visual Thinking](https://arxiv.org/html/2512.24297v1)

actual exact-v1 §3.1–3.3/Eq9及§4.3/Table2，Python生成hypothesis image不是裁剪已有world evidence；correct/exec/teacher suitability是不同label。s=0正确执行draw仍正reward，不能说已惩罚无效调用；嵌套去ARM/去图消融不隔离独立因果，extra teacher与多轮预算保留。Ch78 214与899末注root必要原源/owner及正文/邻接POST通过，5分具体gap深入受影响内容，未跑代码，见[原记录](../_sources/daily-20260102/CORE_ADMISSION_3.md)。

### [Mirage: One-Step Video Diffusion for Photorealistic and Coherent Asset Editing in Driving Scenes](https://arxiv.org/html/2512.24227v1)

actual exact-v1 §3.2.1/Eq2与Tables2–4限定最后两frame-aligned upsampling层的2D detail/3D temporal分工；不能提前注入尚混合多帧的层，不证明原skip读取未来或整管线onlinecausal。GTlatent替代、阶段非factorial与数据独立效应保留，detail encoder、feature驻留和adapter训练计成本。Ch24 863/865及1722末注root必要原源/owner与实际正文/邻接POST通过，6分具体gap深入，未运行代码，见[原记录](../_sources/daily-20260102/EVIDENCE_BATCH_14_INTERVENTION.md)。

### [CorGi: Contribution-Guided Block-Wise Interval Caching for Training-Free Acceleration of Diffusion Transformers](https://arxiv.org/html/2512.24195v1)

exact-v1 §3.2–3.4/Eq2–6、Tables1–3限定增量缓存与current residual、相邻锚点CKA和warmup block-specific ATTN集合；不是整block output替换或已测因果贡献。质量/速度非单调，校准/驻留/refresh付费。Ch24 1078/1080与末注1731必要原源、owner及实际正文邻接POST root通过，6分具体gap深入；未运行代码。详[本批证据](../_sources/daily-20260102/EVIDENCE_BATCH_15_GUIDANCE.md)。

### [Guiding a Diffusion Transformer with the Internal Dynamics of Itself](https://arxiv.org/html/2512.24176v1)

exact-v1 §3.2/Eq3–5、§4.1–4.3/Eq6–7及Tables2–4将受训中间readout作为同forward弱参照；训练目标/stopgrad/EMA与推理外推权限分开。共享误差、强度/heads非单调及额外训练成本保留，不授任意checkpoint插件或manifold真值。Ch24 1169/1171与末注1732必要原源、owner及实际POST root通过，6分具体gap深入。

### [DiffThinker: Towards Generative Multimodal Reasoning with Diffusion Models](https://arxiv.org/html/2512.24165v1)

exact-v1 §3/4、A.1与B/C失败支持受限visual solver→parser替代，未验证内部parallel search。FM/SFT/GRPO非matched训练预算，版本及候选judge成本分账。Ch24 739–746的native image/provisional→typed parser→task evaluator及156步数/NFE/真实成本实际承载采用边界，root必要原源/具体已有覆盖通过；不追加局部grid recipe，也不称本文全部机制已有。

### [Training Report of TeleChat3-MoE](https://arxiv.org/html/2512.24157v1)

exact-v1 §4.2 L251–254只采用同packed shape的document组成成本与完整样本重分，不授dense mask必省FLOPs或孤立MFU/PP归因。Ch38 264与437末注接per-layer profile再接HAPMoE；root原源、owner及实际POST通过，6分具体gap深入，保人口/EoD/optimizer提交及backend校准成本。

### [Taming Preference Mode Collapse via Directional Decoupling Alignment in Diffusion Reinforcement Learning](https://arxiv.org/html/2512.24146v1)

exact-v1 §4.2/Eq5–10、Tables1–2/B.2/D.1–D.2只授两阶段参数权限，不授全部人类偏好纠正。3000+20步骤、有限blind人口及非单调结果保留，不能只用第二阶段称训练便宜。Ch31 799与1195末注在deployment-error后融入instrument分责；root必要源、owner及实际POST通过，6分具体gap深入。

### [GARDO: Reinforcing Diffusion Models without Reward Hacking](https://arxiv.org/html/2512.24138v1)

exact-v1 §4.1–4.3/Eq7–8、§5/Tables1–2及A.1支持batch-relative proxy/aux差选择KL惩罚人口与hard-reset改变reference身份，不证明human truth、累计base KL界或无reward hacking。部分aux同时参与评价，LoRA alpha/r披露冲突保留，硬件/precision/部署SLO未披露，未运行代码。Ch31 286与1198末注把两身份及成本/独立评价/冻结reference回退融入beta论证；6分具体gap深入，root必要原源、owner及实际正文/邻接/末注POST通过。详[必要证据](../_sources/daily-20260102/EVIDENCE_BATCH_16_LATENT_CONTROL.md)。

### [Activation Steering for Masked Diffusion Language Models](https://arxiv.org/html/2512.24143v1)

exact-v1 §3.1–3.2/Eq7–9/Alg1、§4/Table1/Fig5–6及§5支持白盒局部投影，不授安全/utility保持。LLaDA8B、128 harmful+128 harmless训练、64 heldout HarmBench；关键词拒答、Guard2安全标签与空短输出分开。Ch15 279–284已承载子空间干预/校准/副作用及独立verifier，Ch66 688–690已承载同人口拒答与内容测量；root必要源/具体已有覆盖通过，不称原章包含逐step算法。

### [Unified Embodied VLM Reasoning with Robotic Action via Autoregressive Discretized Pre-training](https://arxiv.org/html/2512.24125v1)

exact-v1 IV-C Eq2–5及V-D/TableIII，连续FM detokenization仍消费求解预算；ERIQ QA与grounding不等闭环成功。matched1200示教/每setting50rollout保反侧，不授codec重构或高QA直接保证安全。Ch26 151–164已实际承载codec/FM费用、离散planner/连续refiner与freshness；root必要源/具体已有覆盖通过，未运行代码。

### [GeoBench: Rethinking Multimodal Geometric Problem-Solving via Hierarchical Evaluation](https://arxiv.org/html/2512.24119v1)

exact-v1 §3.2六MC及提供proof path gold、§4 evaluator/C.1/C.4支持path-conditioned过程评价，不替代所有合法证明或内部因果。1021题/76构型、八名博士gold核验与五名human测试人口分开，CoT/直接index解析及预算不同；Ch66 367–410已具体承载legal acceptance、过程oracle和paired output事件。root必要源/具体已有覆盖通过；只保该受限案例，不称path gold已写入正文。

### [Autoregressivity in the Latent Space of a GP-VAE Language Model: An Empirical Ablation Study](https://arxiv.org/html/2512.24102v1)

exact-v1 §4.2替换prior K→diag(K)，§4.3/5.4.2却说明same GP regularization；需要区分训练prior/KL与仅sampling covariance身份，中心归因暂缓。conditional decoder PPL与AR marginal PPL、clip cap8/beta约.35及有限WikiText长续写人口保留，不断言实现必错或全部实测无效。root必要原源及5分中心终态隔离通过；精确恢复条件见下节，详[本批必要证据](../_sources/daily-20260102/EVIDENCE_BATCH_16_LATENT_CONTROL.md)。

### [CEC-Zero: Zero-Supervision Character Error Correction with Self-Generated Rewards](https://arxiv.org/html/2512.23971v1)

exact-v1 §3 Eq4–6/§4 Assumption1、Lemma1实际核。合法alpha=1时，valid pair的cos=.95、gamma=.1、delta=.2、tau=.7、beta=.5满足margin并可满足cluster purity，却给reward=5/6而真值Z=1；purity也只保证存在全valid簇，非largest簇。root实际原式及反例复核通过，只隔离exact unbiased/equivalent semantic objective和依赖该步的保证，不否全部经验结果，不借PPO应用替代中心门槛。原必要记录见[CORE_ADMISSION_3](../_sources/daily-20260102/CORE_ADMISSION_3.md)。

### [iCLP: Large Language Model Reasoning with Implicit Cognition Latent Planning](https://arxiv.org/html/2512.24014v1)

exact-v1 §4.2–4.3/§5/Tables1–3的六slot/2048码本LP tokens仍与显式CoT交替；教师/codec/LoRA/扩词表预算独立保留。MATH总token超过ZeroCoT而TheoremQA降低，7B正文370.2与表270.2冲突不采用；聚类/readout不授faithfulness。6分具体接口gap深入，Ch18 279/411末注与266–295邻接已由root必要原源、owner及actual POST通过，未运行代码。详[必要core与owner](../_sources/daily-20260102/CORE_ADMISSION_3.md)。

### [AHA: Aligning Large Audio-Language Models for Reasoning Hallucinations via Counterfactual Hard Negatives](https://arxiv.org/html/2512.24052v1)

exact-v1 §4.2–4.4/§5/Tables1–3/§8/A/B实际读，caption生成chosen/negative与十名听音志愿者核负例分账；evaluation复用audio-question pairs未给足独立split身份，不自动判全部泄漏也不授in-domain独立泛化。外部任务局部提升、ESS退步与同义词误罚保留；BF16/LoRA16/alpha32/8epoch不授全链预算公平或内在acoustic能力因果。root必要原源及具体Existing通过：Ch66 572–600实际承载输入支持与标注/judge代理边界，不称已有整套AHA/DPO公式。详[必要core](../_sources/daily-20260102/CORE_ADMISSION_3.md)。

### [Efficient Context Scaling with LongCat ZigZag Attention](https://arxiv.org/html/2512.23966v1)

exact-v1 §1 Calibration/Training、§2–3/Table1冻结end-midtrain只校full/sparse系数，选50%替SSA后rewind midtrain起点重新训练。selection权重与发布权重不混，1sink+7×128只限SSA；540B token/YaRN/SFT/DPO/RFT与LongEval退步分账，不授即时转换无损或整网固定成本。6分具体checkpoint身份gap深入，Ch22 800/780–811邻接及1257注root necessary-source/owner与actual POST通过，未复现。详[必要core与owner](../_sources/daily-20260102/CORE_ADMISSION_3.md)。

### [Improving Multi-step RAG with Hypergraph-based Memory for Long-Context Complex Relational Modeling](https://arxiv.org/html/2512.23959v1)

exact-v1 §3.3–3.6/§4.2–4.3/§5.2–5.4/Tables2–3的entity anchors、local邻域/global补集、update描述与merge并集界定检索支持。未知vertex插入不授事实，构图/多调用/删除成本独立保留；有限steps/chunks近似预算非全生命周期matched，merge局部反退不隐去。6分具体scope接口gap深入，Ch77 360/343–372与2026注root必要原源、owner及actual POST通过，未运行实现。详[必要core与owner](../_sources/daily-20260102/CORE_ADMISSION_3.md)。

### [Energy-Tweedie: Score meets Score, Energy meets Energy](https://arxiv.org/html/2512.23818v1)

exact-v1 §2.1–2.2/§3–4/Eq12–13/17/20、§5.4.1、§6及A.2支持固定posterior measure求noise-score期望；β/Σ需与noise law匹配，Gaussian β2仅mean充分，非Gaussian通常需posterior加权残差。训练参数支持、Monte Carlo与积分误差独立付费，二维有限seed/importance近似不授全域质量或通用reverseSDE。7分必要源/owner及实际Ch24 137/139、DDPM前后与1758注已root非作者POST通过，未运行代码。详[必要core](../_sources/daily-20260102/CORE_ADMISSION_3.md)。

### [Learning to Feel the Future: DreamTacVLA for Contact-Rich Manipulation](https://arxiv.org/html/2512.23864v1)

exact-v1 §3/表1必要路径显示先draft action条件future tactile再二次policy，但W/F预测器与encoder、LLM hidden/CLIP身份前后不明，L_W target/horizon/draft训练配对不足以核预测训练→因果收益/精确实现链。6分保留，root必要原源及Ch26 321–346对读后中心暂缓；不否有限接触实验，不用现有触觉主题抹争议。详[必要core及精确未决](../_sources/daily-20260102/CORE_ADMISSION_3.md)。

### [Max-Entropy Reinforcement Learning with Flow Matching and A Case Study on LQR](https://arxiv.org/html/2512.23870v1)

exact-v1 III-B–D/Theorem2/Algorithm2及A-A necessary读：proposal支持/importance权重和density求值有效接口仍保留；正文literal argmax squared loss却与proof argmin及empirical差≤0冲突。target/proposal N(0,1)、finite常velocity{0,c}反例使literal输出选c、endpoint W2²=c²不趋零，符合所述平滑/矩条件；只隔离此定义的收敛保证，不授Algorithm2最小化全部失效。7分中心终态root必要原式/反例复核通过，不入Books。详[原式及假设](../_sources/daily-20260102/CORE_ADMISSION_3.md)。

### [The Drill-Down and Fabricate Test (DDFT): A Protocol for Measuring Epistemic Robustness in Language Models](https://arxiv.org/html/2512.23850v1)

exact-v1 §4.3–4.5/§5/§6实际核：planned1800/complete与turn5 only18%触发的实际人口未释；compression实际变换/每级gold支持未定义；HOC max不是无需单调性的first failure。三judge一致不等gold，two-system仅functional拟议解释。6分中心终态root定点必要核通过，不采用compression→robustness/人口或内部机制实证，也不否拟议sequential protocol。详[必要core](../_sources/daily-20260102/CORE_ADMISSION_3.md)。

### [A Test of Lookahead Bias in LLM Forecasts](https://arxiv.org/html/2512.23847v1)

exact-v1 Eq2–6/B.1把FWL线性残差换成conditional expectation，未建立等价。合法μ/ε独立N(0,1)、L独立Bernoulli(.5)模型，非奇异regressor covariance给交互系数0但Eq6 RHS=.25；只隔离literal中心识别及iff，不否数据相关或所有forecast。LAP低logprob几何均值不等成员真值，body日期/残差版本保留。7分中心安全终态root实际原式/反例通过，不进Books。详[必要原式](../_sources/daily-20260102/CORE_ADMISSION_3.md)。

### [Adversarial Lens: Exploiting Attention Layers to Generate Adversarial Examples for Evaluation](https://arxiv.org/html/2512.23837v1)

exact-v1 §3.1–3.3/Table1–3/结论支持中层候选替换与续生成接口，不证语义保持或独立真值。单Llama8B、75tuple、位置/层搜索及grammar/semantic退步限定实验；Ch66 clean/noisy twin1634–1638与verifier886–889实际承载gold重核和变义隔离，非已包含lens算法。5分标准必要源/具体Coverageroot通过，未复现。详[必要core](../_sources/daily-20260102/CORE_ADMISSION_3.md)。

### [Large Language Models Are Poor at Signaling Their Ignorance When Given Irrelevant Context](https://arxiv.org/html/2512.23836v1)

exact-v1 §2/§3/Figures5–7限定BM25/Wikipedia/KILT三QA数据集及单Gemini1.5Pro的negative-before-first-positive人口；排序与window数同时改变暴露，不能授所有无答案问题或全模型幻觉率。6分具体gap深入，Ch76 sufficiency后489一段及1424注已root实际正文/邻接POST通过；保visited预算、非独立和supportgate/完整证据回退，未运行评价。详[必要core](../_sources/daily-20260102/CORE_ADMISSION_3.md)。

### [Implicit score matching meets denoising score matching: improved rates of convergence and log-density Hessian estimation](https://arxiv.org/html/2512.24378v1)

exact-v1 Assumption3.1/Lemma3.2(ii)/Definitions3.3/3.6/Theorem3.7及必要Jacobian路径，函数L2误差需要额外高阶Sobolev/噪声/模型类条件才能控制导数；未授所有autodiff/无维数代价或全ODE质量。7分，Ch24:192函数/导数/solver一段与1762注root必要源/owner和实际188–197邻接POST通过，未运行实现。详[必要原式与解释性反例](../_sources/daily-20260102/CORE_ADMISSION_3.md)。

### [Score-based sampling without diffusions: Guidance from a simple modular scheme](https://arxiv.org/html/2512.24152v1)

精确v1 §2–4/Discussion支持阅读SLC子问题、条件score与uniform误差传播的拟议模块，但header Dec30,2025和body Aug24,2026身份真实冲突，不先授当时正文定理或新runtime。7分必要机制已读保留，root实际身份核为本窗终态暂缓，不进Books、不扩版本史。原式/oracle/earlystop条件详[必要core](../_sources/daily-20260102/CORE_ADMISSION_3.md)。

### [On Exact Editing of Flow-Based Diffusion Models](https://arxiv.org/html/2512.24015v1)

exact-v1 Eq12–18/Alg1的条件算子未定义，明确位移目标与源state比较：初始零编辑DeltaV0时literal校正仍产生2η²Δt²xsrc偏移，不支持error-free/exact identity。5分中心安全暂缓root实际原式/反例通过；保三velocity局部双差分与PIE实测，不断言代码必错。相同steps不等三NFE总成本，CLIP/SSIM反侧不抹去。详[精确原式及重开范围](../_sources/daily-20260102/CORE_ADMISSION_3.md)。

### [Constraint Breeds Generalization: Temporal Dynamics as an Inductive Bias](https://arxiv.org/html/2512.23916v1)

exact-v1 §2/A.3.2训练设置把输入Duffing delta与网络LIF beta分成不同接口；volume contraction不保证逐方向/语义收缩，同width/评测次数不等参数或训练预算相等。原6分标准仅报告经root必要源/现state稳定边界对读通过：保跨编码/非单调敏感性案例，未有可迁foundation系统的统一选择规则，不用CV相关授内因或借成熟state原则加分。详[设置/负侧](../_sources/daily-20260102/CORE_ADMISSION_3.md)。

### [DriveExplorer: Images-Only Decoupled 4D Reconstruction with Progressive Restoration for Driving View Extrapolation](https://arxiv.org/html/2512.23983v1)

exact-v1 §3–5的动态mask/BCE reference为GroundedSAM，pseudoimage/mask编码concat到SVD，生成→pseudoGT再训显引ReconDreamer；2H20/150kVDM+每次20kGS，EUVS画质指标/消融不授真实几何或驾驶闭环。5分标准具体已有覆盖root必要源和Ch24相机训练1207正文通过：重建render条件/proposal非geometry truth/预算与独立验收已实际承载，非声称mask公式已有。详[必要core及具体owner](../_sources/daily-20260102/CORE_ADMISSION_3.md)。

### [Rethinking Dense Linear Transformations: Stagewise Pairwise Mixing (SPM) for Near-Linear Training in Neural Networks](https://arxiv.org/html/2512.23905v1)

exact-v1 §3–4/§9.1/9.3–9.5支持P/L约束的结构容量分支、O(nL)及CPU窄宽kernel crossover，不授任意dense权重无损或GPU/Large-LM普胜。B32/B256、NLL/BPC与1000/800steps冲突只隔离联合质量/速度口径；5分因具体operator gap深入，Ch16:206/199–213与342注已root必要原源、实际正文/邻接POST通过，dense/旧GEMM路径保留。详[必要core](../_sources/daily-20260102/CORE_ADMISSION_3.md)，未运行代码。

### [How and Why LLMs Generalize: A Fine-Grained Analysis of LLM Reasoning from Cognitive Behaviors to Low-Level Patterns](https://arxiv.org/html/2512.24063v1)

exact-v1 §3.1诊断要求正确答复和explicit self-check，但A.1称所有评价只读final boxed answer；这些scorer身份不一致，不能从radar/profile或权重统计授behavior保留、SAE因果与安全保证。6分中心安全暂缓root实际必要原源通过；不否有限终局任务表现，SFT/RL nominal horizon不等匹配总rollout compute。详[原句/设置/重开范围](../_sources/daily-20260102/CORE_ADMISSION_3.md)。

### [Fantastic Reasoning Behaviors and Where to Find Them: Unsupervised Discovery of the Reasoning Process](https://arxiv.org/html/2512.23988v1)

exact-v1 §3.2/4.2–4.4/5将delimiter step残差作SAE与方向projection，行为标签/次数和信心风格不等正确性/faithfulness；top3方向需额外搜索选择成本，AIME一题差不证明noninferiority。5分标准，root必要core及现Ch15 sensor→intervention proposal、独立verifier/副作用fallback和Ch66 SAE source-label/因果权限实存通过，具体已有覆盖，非声明原书含recipe或dictionary recovery定理。详[必要core](../_sources/daily-20260102/CORE_ADMISSION_3.md)，未运行代码。

### [T2VAttack: Adversarial Attack on Text-to-Video Diffusion Models](https://arxiv.org/html/2512.23953v1)

exact-v1 III-A–C/IV-A–D/IV-F：SentenceTransformer/WordNet不授exact condition等价，四模型baseline-success交集是selected人口；总estimated-flow减少可能来自缩小对象/背景，不必是全视频时序推理失败。每次query为完整视频生成，80query变体另付成本。6分标准必要源及actual Ch66:4120–4127语义反事实/proxy触发结构、stored stimulus与人口约束root通过，具体已有覆盖；局部逐词算法留报告，不授Hunyuan rewrite内因或全部视频失效。详[必要设置/反侧](../_sources/daily-20260102/CORE_ADMISSION_3.md)。

### [RainFusion2.0](https://arxiv.org/html/2512.24086v1)

exact-v1 §3.1–3.4/Eq5–8、§4/Table1：block均值只筛support，selected blocks另做完整attention/online normalization；首帧query全读与首帧key全保是两个角色，3D permutation要保position/文本身份。窗口实现原称details later、TopN轴口径不明确，不补造实现。NPU型号/precision/batch/frame count未披露、质量指标非全胜，不授跨硬件或无损。6分标准必要source与Ch14:284–300实际support selection/normalization、base-rescue/required-mask union合同root通过，具体已有覆盖；首帧/3D局部recipe不构成必须新增Ch24的长期缺口。详[稀疏/探索证据](../_sources/daily-20260102/EVIDENCE_BATCH_17_SPARSE_SEARCH.md)，未运行代码。

### [Graph-Based Exploration for ARC-AGI-3 Interactive Reasoning Tasks](https://arxiv.org/html/2512.24156v1)

exact-v1 Methods/Alg1、Results/Discussion及B：tried-state/action、frontier最短路与visual priority是局部training-free recipe。4K交互cap下nonLLM五run median对官方LLM一次aggregate、未重跑；不等全部内部/训练/调用预算匹配。reset漏标导致livelock为作者报告，不独立代码验证。6分标准仅报告，root必要原源及处置通过；反证可限定这个评价，但未确定可迁移的模型规划选择规律，hash/partial-state、canonical/fulltrace已由Ch79承载，普通reset实现bug不自动升级长期机制。详[必要原源与反侧](../_sources/daily-20260102/EVIDENCE_BATCH_17_SPARSE_SEARCH.md)，不授graph普遍优越。

### [PipeFlow: Pipelined Processing and Motion-Aware Frame Selection for Long-Form Video Editing](https://arxiv.org/html/2512.24026v1)

exact-v1 §4.1–4.4/§5.3/§8.1–8.3/§10：同segment inversion必须完成才能edit，跨段可重叠；SSIM/flow选帧后RIFE重建和overlap另付质量/资源成本。75 prompt-video、RTX3090/512²/16–350frames/20FPS为有限作者配置，长视频DMT分组估算不作完全同task独立基准。Eq7–9时间口径及图像CLIP作prompt alignment不采用；dense keyframes质量反侧、强结构编辑/插值限制保留。6分具体gap深入，Ch24:1452/1766及前后实际POST经root通过；不授无限长度、零通信或Serving SLO，未运行实现。详[必要core](../_sources/daily-20260102/CORE_ADMISSION_3.md)。

### [PhyAVBench: A Challenging Audio Physics-Sensitivity Benchmark for Physically Grounded Text-to-Audio-Video Generation](https://arxiv.org/html/2512.23994v1)

exact-v1 III-B/IV-C Eq1–6/IV-D：paired prompt只改一个factor，现实多样本均值embedding差与生成差比较方向。CPRS不测幅度；正比例缩放可同分，零差应Unknown，encoder方向不识别内部物理推理，同步另测。IV-D明确全面模型评价留待future release，拟议协议不是模型失效实测。6分具体测量gap深入，root必要源/owner及Ch66:4066/5312实际正文/邻接/末注POST通过，保现实reference/encoder/配对预算和observable fallback。详[必要core及原式](../_sources/daily-20260102/CORE_ADMISSION_3.md)，未运行代码。

## 5. 缺口与下一步

已隔离的本窗中心争议：24991精确AUC定义/实现（linear-n vs log2）未统一，单AUC也不识别唯一curve；重开需要作者澄清或对应实现及独立真实learning-curve校准，不采用预算推荐、不进入Books。24851的D4/D8是否让reflection影响实际动作未统一；重开需要可核执行实现/作者澄清，并在固定状态与匹配推理/step预算下复查控制对照。24940的conditional normalizer与参数继承身份冲突，重开需要修正Prop2或明确假设、真实训练基座/累计pool实现及独立任务预算控制，不采完整RL等价/部署泛化。三项已读必要原源及争议经root核，不作正面Evidence、生产性能或因果保证；它们不是未审普通待办。

另DLCM24617中心争议已root核：恢复需要精确版本实现或作者澄清sampling/pool完成时机及shift/completed-concept，并复核作者date冲突；暂不采用causal NTP与通用压缩/μP最优。不把未决推断写成已验证泄漏。这是第四项中心终态保留，不作正面Evidence。

MultiRisk24587的D5证明步骤局部隔离：需要作者修订或有效零loss下界/补偿项及完整递归证明才能重开算法保证；当前只采用已核first-trigger人口/行为成本分账。该未决权限不冒充保证通过，也不撤销有效机制证据或宣称全理论失败。

PhyGDPO24551为第五项中心终态保留：只隔离Eq2–14 group概率/符号与权重条件的训练推导权限，重开需作者修订或明确合法目标、权重域和精确实现一致性；不授全部实验无效、不以LoRA事实替代此门槛。

普通可执行研究/Books工作：无。141＝30前关闭＋7前公开＋104冻结候选终态＋0普通待办；Rain为具体已有覆盖、Graph为标准仅报告、PipeFlow/PhyAV正文及邻接/末注root实际POST通过，UniAct已由原Pages成功发布与exact-sha正文定点核为窗前机制公开。本日整体独立验收已通过，剩余外部保留项仅按具名条件定点重开；见[STOP](../_sources/daily-20260102/STOP.md)。

Lookahead23847为第十三项中心终态保留：重开需修正线性投影/条件残差和识别假设、校准成员proxy或作者精确版本澄清及对应结果；只恢复该识别链，不等待全部金融数据或扩查所有附件，不作投资建议。

RSA24263与MARS24330为第六/七项中心终态保留：RSA重开需精确版本勘误/实现澄清cost符号、reward温度与派生BT/SRR loss，MARS需真实group/mask/epsilon/sharding定义解释二级归一化的新作用，均不自行修原文后授贡献、不入Books、不否全部有限实验。

GP24102为第八项中心終态保留：重开只需精确版本的训练prior、KL/clip与采样covariance身份及其对应结果/预算协议或作者澄清。现不能采用“只改latent correlation”的因果归因、不进入Books；有效局部实验保留，不要求全部附件或断言原实现必错。

CEC23971为第九项中心终态保留：重开需修正版reward threshold/cluster定义、精确实现及相应结果或作者澄清，使无偏/等价目标与实际假设一致。当前不采用Lemma1及依赖此步的保证，不进入Books，不要求其余附件或宣称全部实测无效。

DreamTac23864、ISFM23870、DDFT23850是第十至十二项中心终态保留：分别只请求W/F与backbone身份、L_W target/horizon/draft训练配对及对应结果；literal优化方向修订/实现与定理路径假设一致；compression实际texts/每级gold支持、trigger实际分母及正确HOC语义。可接受作者精确版本修订、可核实现及对应结果，定点重开各自预测训练链、理论输出或协议评价；不等待这些外部澄清阻塞其余普通工作，不宣称全文/全部实测无效。

24152与CVC24015为第十四/十五项版本身份/中心保留：前者只请求能证明当时body的原始版本或作者更正，重开精确事件身份/定理权限；后者只请求明确[DeltaV|xsrc]条件算子、state/位移目标与步因子及对应实现/结果或勘误。均不正面进入Books、不否所有局部实测，不扩完整版本史/全附件。

Behavior24063为第十六项中心保留：只请求真实behavior scorer/judge定义、对应结果人口与预算，或精确版本修订以统一self-check与boxed-only合同；定点重开测量权限，不要求全部SAE附件，不否所有实验。

外部历史限制按以下六组保留，不用于候选、Books或“无遗漏”断言；已检查的有限博客/当前目录部分不因此失效，也不替代缺失历史部分。当前可用入口与有限替代已执行到记录中的停止位置，不继续用相同失败探针等待历史页面恢复。

- Google：已读Research的2026年1月9条/2025年12月6条月档至无pager，但[pubs年份入口](https://research.google/pubs/?year=2026)实际fetch失败，[DeepMind Research](https://deepmind.google/research/)只恢复当前栏目，未得到本窗首公开/版本事件切片。恢复需带首公开日期及论文身份的官方历史目录、公告或具名作者正文；只重开本窗pubs/DeepMind事件，月博客不重扫。
- Meta：[Research](https://ai.meta.com/research/)及有限global_search首个publication页12条未建立严格日期次序，辅助日期过滤未生效，不能越过混排首屏推断Jan1无事件。恢复需可核官方本窗公告/论文首公开字段与对应分页停止位置；仅重开这个历史发布缺口，不把全年检索结果转成队列。
- Qwen：[Research](https://qwen.ai/research)实际只返回动态shell；旧[官方Blog](https://qwenlm.github.io/)的Dec30项在窗前，但不能覆盖新目录的历史迁移/删除。恢复需原Research历史列表响应或带时间与正文身份的官方发布页；只处理落本窗事件，shell内非publication日期不用于归属。
- Hunyuan：[Research](https://hunyuan.tencent.com/research)浏览器恢复超时；从原JS恢复[publicList](https://api.hunyuan.tencent.com/api/blog/publicList)，请求pageNum=1/pageSize=20/renderType=0取尽total=11，当前最早项Feb3，已到当前列表末而非Jan1历史末。恢复需当时Research快照/官方原公告，或能返回历史项及publicAt身份的列表；不能将当前11条或publishedAt/displayPublishTime机械当历史首公开，重开只限缺失本窗。
- MiMo：[Paper/Blog](https://mimo.xiaomi.com/)恢复Paper8项，Jan8在窗后、MiMoAudio Sep19在窗前；Blog15项无日期、More隐藏，没有可用历史分页/首公开字段。恢复需具名Blog原文的publication字段或官方历史列表含日期/停止依据；现有Paper判断保留，不能由其无新项授Blog无命中。
- MiniMax：[Blog](https://www.minimax.io/blog)有限13项以Jan27/Dec23包围本窗，但[Agent Tech原Markdown](https://agent.minimax.io/docs/techblog.md)只有2026-05-13单项，不揭示Jan1时的目录状态。恢复需该技术栏目本窗历史快照或具名官方原技术公告；不能用晚页日期宣称栏目当时不存在，已检查Blog不重扫。

另arXiv本次实际API查询只有submittedDate缓冲，不含lastUpdatedDate query前缀；不能由它证明窗前ID的本窗重要修订为零。该历史修订公开列表恢复限制隔离，不支持无遗漏，恢复需本窗带版本身份的官方announcement/archive切片或具名作者revision事件；只审具名实质修订，不扩旧库存。普通待办为0并不使这些外部限制获得正面覆盖权限。

窗外首次公开线索见PRIOR_PUBLICATION；恢复相应真实归属或具体重要修订才定点重开，不扩Jan02、不顺带重跑会议/2025全库。

## 6. 复核

复核者：root（本日报非作者）；mHC Books由root作者、jan01非作者复核。

结论：通过

2026-10-02，本窗达到合同安全终态。root实际顺读最终六部分，核验104终态/141互斥分区、14个每日源实际停止范围、公开区间及具名负侧抽检范围；复用已逐项通过的必要原源、具体owner与62项实际POST。104个冻结家族中87项必要证据/Books处置、1项4分关闭、16项已读中心/身份安全暂缓及7项窗前公开均完成独立处置，普通待办为0。16项中心/身份及六机构历史切片、arXiv旧ID修订覆盖限制仍隔离，不授正面Evidence、性能/安全保证或无遗漏；日级完成不代表这些未决主张已证实。

明确排除的30项按范围/仅组合/无新成立条件分层抽检15项：root实际完整题摘核24986/24856/24653/24613/24609/24407六项；完整题摘及决定性core核24615/24461/25072/24373/24331/24098/24000/24149八项；24713实际官方withdraw说明一项，删除正面链路且不评分。其他15项（24580/24314/24231/24120/24092/24087/24058/24008/23977/23941/23927/23880/23844/24310/24210）作者题摘已读但未作root逐篇原源抽检，不称全量排除验证。理由与精确范围见[首批](../_sources/daily-20260102/ADMISSION_CALIBRATION.md)和[补段](../_sources/daily-20260102/GAP_ADMISSION.md)；领域、小模型、理论或旧Book主题均非自动拒绝依据。

机器校验：冻结表validator及限定diff-check通过；104行/104唯一ID与104证据小标题一致，六部分齐全；104公开区间均完全落窗且exclusive upper与实际created秒精度下一秒一致。本地链接逐路径组件核大小写均通过，62项整合各有唯一实际通过源注（局部保证保留项和历史日Gate待验措辞不当作POST未过）。机器通过不是语义验收；日期目录仅README，未stage、commit或push，运行前dirty/staged保留。
