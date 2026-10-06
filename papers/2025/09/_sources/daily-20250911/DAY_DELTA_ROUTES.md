# 11 日 A/B/C 有限返修

作者Bacon；2026-10-06T13:49:18+08:00。依据[Aristotle实际DAY](INDEPENDENT_DAY_REVIEW.md) §2/4/6，只同步未通过差额，不重审有效Qwen、七必要core或Books。35项完整题摘的实际读取者是Aristotle；本作者复用身份/版本/命题未变化的独立题摘判断，不声称本次新读35份全文、实现或复现。

A：本次重新解析原`arxiv-scoped.raw`与`arxiv-supplement.raw`，各146、交85、并207、各独61，无尾页；前者12类主题，后者无该分类限制且不同同义组。207只为submitted-window discovery，不授first-public/当窗候选/审阅完成。宽attention/GPU/agent入口产生领域噪声，仅保留发现缓存；后续重开按DAY §2A四组模型/系统/LLM Agent/多模态语义收窄，不再孤立词扩扫。不重新跑207全文。

B：Meta实际page5止Sep15。Aristotle在2026-10-06T05:35:02Z GET官方results page6，200/275689 bytes，已读Sep8 GRAPE→Sep2 diversity/quality→Aug→Jun13；请求和可见身份原记录保存在DAY §2B。复用该普通来源修复，不拿泛用page6的45-byte unavailable当空列表。

C：08120v1实际FL优化/软件thesis；08318v1才为early-exit full-dataset训练与hard-conditional inference shift、顺序BTS-EE及class-wise CPM校准。08157当前v3的global风险预算/iterative per-agent分配和edge deletion可行性取舍保留潜力，不因传统CBS/GCRL名关闭。EvolKV08315v1原精确probe已存在，补路由。原错误理由保留在DAY，不重新归因未取得日期为无贡献。

## 35 项最小潜力路由

全部只保留题摘所支持的有限机制/边界，不评分、不作为11日确定候选/Books。后续版本不倒填v1，晚ID不倒授日期。必要原公开区间/精确旧版恢复后，只重开对应命题和方法/反侧；以下不是35份全文待办。

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

## 差额复核请求

请Aristotle仅复核以上A/B/C同步与最终README六部分。已有效Qwen/必要core/Books NoChange不重审，Books不改。正式状态仍进行中，本文件不授DAY通过。当前工具没有可寻址的Aristotle消息通道，通知请求在本handoff与当前会话交root转达，不声称已向其发送消息。

