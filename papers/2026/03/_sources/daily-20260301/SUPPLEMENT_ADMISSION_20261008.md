# 03/01补查：准入包（独立校准通过）

作者：supplement_20260301。补充窗口仅2026-02-28北京自然日；原1家族、评分、旧窗口和连续§4逐字冻结，旧日期推导和完成标签仅复用、不成为本轮新证明。

四组官方API查询是Submitted Feb28邻域发现，不是公开日证据：语言/学习69（start0返50、start50返19）、系统5、多模态33、Agent38；去重103个身份。相关题名才读完整摘要，明确医学/科学应用、一般领域任务停在标题，16项原始提交日期已是北京时间03/01的arXiv首次事件关闭、不追全文（不排除另有具名更早作者事件）。未扫描Weekly、Live、其他年份/缺失日或全月份库存。

## 全部拟新增贡献潜力（日期未确认，尚非确定候选，不评分）

下列完整题摘均实读自本目录`SUP_ARXIV_TOPIC_*.raw`精确entry。摘要支持潜在增量、不支持实验结论；每项只请求一次必要首公开日，原始页一次恢复后隔离。当前摘要有v2+者不据版本号触发重要修订；是否当前纠错/撤回须轻量检查原页。

| ID | 原有约束 → 原文增量 → 待核选择 |
| --- | --- |
| 2603.00396 | Meta-RL局部任务编码平滑限制外推 → Lie群状态/动作变换及可线性化/连通/紧群条件 → 小导航实验下非局部泛化能否由几何支持 |
| 2603.00412 | 3D-token仅下一词监督可能丢几何 → 中间点云token一致性正则 → 3D表示是否需要额外保真监督 |
| 2603.00429 | 对话自报告可能不等于人格行为 → 三层评估发现记忆放大与对话弱信号不同 → 人格评估不能只看对话的局部证据 |
| 2603.00436 | unlearning破坏邻近知识导致间接攻击 → null忘却影响同时增强邻近知识的Neural Healing/理论保证 → 删除与retain不必等同破坏 |
| 2603.00437 | 新LVLM旧hallucination模式缓解不稳定 → 隐状态跨层diagonal attention内生纠正 → 无外部纠错的视觉grounding设计 |
| 2603.00454 | GFlowNet早前缀信用弱/重放分布移位 → root-anchored吸收suffix备份与submodular replay → 若一般机制成立应重考虑prefix信用；分子应用本身不入范围 |
| 2603.00458 | DiT一跳视频恢复仍重且空间/时间损失冲突 → 3D teacher蒸馏2D+1D时间卷积/双头对抗 → 生成压缩时如何分别保持细节/一致性 |
| 2603.00466 | 多源world prior直接相加视觉不稳 → joint pixel/feature预测、约束退火、inner-guidance → 视频一致性训练的目标调度（不先称action世界模型） |
| 2603.00476 | browser计划-动作间页面可变 → TOCTOU实测与动作前DOM/layout验证 → 确认与执行时的安全边界 |
| 2603.00483 | T2I固定test-time预算不能适应要求 → checklist缺口驱动候选演进与预算 → 语义要求复杂度下动态计算分配 |
| 2603.00486 | 精心token分组可能不必要 → 随机组对照及四个成立条件 → 位置/head多样性/全局感受野/固定模式而非组法复杂度 |
| 2603.00492 | under-observed3D修复不一致/多视点不可扩展 → opacity mixing再蒸馏因果生成 → 与已有观测一致下视点生成的质量/规模取舍 |
| 2603.00498 | 服务微调有害梯度破坏安全 → 平坦loss区+batch样本加权 → alignment与微调阶段联合保持安全 |
| 2603.00510 | visual输入/内部计算语义不清 → EmbedLens分出sink/dead/alive及中层注入 → token/层裁剪是否保留视觉信息 |
| 2603.00511 | 静态视觉RAG引入错证 → 联合隐藏表征classifier控制是否检索 → 内部知识置信与外证接纳 |
| 2603.00512 | query相似度选帧割裂叙事 → wavelet多尺度语义边界预算+MMR → 长视频budget需保留变化结构 |
| 2603.00519 | DiT均匀计算忽略地域收敛差异 → 早期识别+token调度runtime → 区域自适应计算是否维持生成质量 |
| 2603.00529 | caption模型moderation挡不住视觉patch → 7patch universal targeted攻击/俚语绕过 → 图像输入攻击面安全边界 |
| 2603.00539 | review解释可能制造错误纠正 → correct代码误判/详细prompt反而更差，fix作可执行counterfactual → LLM审阅须区分语言理由与测试反证 |
| 2603.00540 | reverse synthesis欠状态因果有效性 → policy硬编译、边界状态、forward轨迹及精确状态验证 → Agent训练数据验证链 |
| 2603.00541 | μP宽深扩展依架构/优化器碎裂 → 统一谱约束及k=1/k≥2转折 → HP迁移参数化条件 |
| 2603.00546 | task类别judge benchmark隐藏判断能力缺口 → length bias/process error等十维与MCTS配对轨迹 → judge训练与评价需能力分解 |
| 2603.00549 | 同目的kernel性能差异使延迟估计失准 → SIMT/config-aware模型支持Triton/attention → GPU预测需kernel身份而非op标签 |
| 2603.00563 | Whisper长音频KV线性增长 → absolute-pos下MHA→MLA并比较encoder/decoder/cross → MLA复用部署边界 |
| 2603.00565 | 单图攻击难破强对齐 → 多图拆语义再由跨图推理重构 → 多图推理安全边界 |
| 2603.00573 | LoRA-MoE专家增多/粗路由开销 → shared低秩core专家与逐token softmerge → PEFT专家容量/参数取舍 |
| 2603.00589 | VAR超分局部attention/残差监督积累错 → SCA结构相关mask+每尺度完整监督 → AR生成跨尺度一致性 |
| 2603.00590 | 理解与生成分开fairness评价掩盖偏差 → 同步IRIS评估揭示generation gap/分裂 → 统一多模态评价协议 |
| 2603.00592 | VLA单布局单任务高成功掩盖忽略语言 → 固定布局语义扰动/增加任务多样性 → 评价的视觉场景混杂 |
| 2603.00600 | 固定感知目标难泛化 → 语言条件6D视点/多层语义几何融合/闭环 → active perception动作接口 |
| 2603.00607 | 多身份硬mask泄漏/变形难 → task-timestep语义窗注入/组级DPO → 身份保持与结构plasticity调度 |
| 2603.00655 | final层特征衰减细视觉 → 层间stateful memory/feedback → cross-layer视觉表示适配 |
| 2603.00683 | speech encoder self-attn二次成本 → polynomial token mixing线性复杂度/BEST-RQ → speech表示效率替代边界 |
| 2603.00686 | synthesis评价只看final → 操作分解与强reasoner弱generator非对称局部证据 → Agent编排中的模型能力分工 |
| 2603.00694 | offroad传感退化破坏caption/planning → task-conditioned可靠模态路由+planning输出 → 恶劣感知下融合控制 |
| 2603.00696 | 连续embeddings反事实不流畅 → 只作guided decoding语义引导 → 可读反事实与模型decision sensitivity |
| 2603.00719 | 长时VLA奖励稀疏/流程约束 → 自动keyframe/latent进度reward/在线人反馈 → laboratory是物理动作实验，不以生物科学应用归入Books |
| 2603.00720 | 多模态LoRA收敛不均 → 两个scale law用rank控制模块收敛/性能 → rank不只表示容量而可协调训练动态 |
| 2603.00579 | 单层analytic FL保留异质性不变却缺表示学习 → closed-form残差块/逐层least squares及理论 → gradient-free表示学习与异质性边界（不因FL名字排除） |
| 2603.02266 | audio TTS越长感知衰减 → CAFE诊断/动态重感知RL → reasoning预算不能无条件替代感知 |
| 2603.06640 | 剪枝unlearning被当安全 → 权重剪枝位置side-channel无数据复活 → concept遗忘与位置泄露 |
| 2603.06652 | final正确不等于视觉过程正确 → perception-aware事实数据/层级process reward → RL的过程grounding |
| 2603.13289 | 多Agent重prefill → decode KV跨Agent复用并局部纠偏 → prefix差异下状态可迁移边界 |
| 2603.13292 | safety/refusal与helpfulness冲突 → 风险visual聚类冷启与动态reward权重 → 跨模态风险/效用仲裁 |
| 2603.00638 | 全局更新干扰稳定偏好、pointwise过窄 → top-confidence/margin控制region的Update/Expand/Add、增量区域LoRA训练/相似度路由 → 明确的动态区域写入粒度/边界扩张与干扰取舍；推荐实验仅局部证据，不泛化其收益 |

## 代表性EX（完整题摘已读；不是因分数、Books已覆盖或小实验关闭）

- 2603.13287 From Stochastic Answers：LLM一次生成可执行规则+precision/coverage筛选；增量落在VCBench创业者筛选的规则分类器组合，未建立相对现有代码生成/验证新的模型或Agent执行机制/归因边界；关闭贡献，日期不穷追。
- 2603.00452 Texterial：gestural文本黏土/植物交互探针与用户mental-model研究，不改变模型学习/推理/Agent执行可靠性机制；范围外。
- 2603.00432 Typological MLM：mBERT/XLM-R词序扰动与lemmatization诊断局限在语言学敏感性，报告已知scrambling影响，没有新的模型训练/表示成立条件；关闭贡献。
- 2603.00431 TARA：biology foundation model taxonomy对齐用于生物分类，ROADMAP暂缓AIforScience，不通过通用representation owner重新引入。
- 2603.00490 LifeEval：实时/自我视角assistive场景与4075 QA、26模型，摘要仅笼统困难，未指出具体混杂/失败路径或能修正评价选择的证据；不因benchmark名字保留。
- 2603.00582 Super Research：300问题/100+检索/1000+网页与审计五维，摘要没有可核验新增机制或实测失效边界，“proxy general competence”是未经支持推广，关闭贡献。
- 2603.00501 WirelessAgent++：operator代码MCTS搜索+无线benchmark，摘要收益仍是领域任务已有workflow optimizer应用，没有辨明可迁移新搜索机制或optimizer失效条件；范围/贡献退出。
- 2603.00638 RAIE原“推荐领域”EX已撤销。root读完整当前Atom摘要发现region增量边界应定点核验；作者一次精确v1方法core确认以下具体潜力，不因领域名或LoRA已有Books关闭。
- 2603.00654 RC-GeoCP：车辆radar/camera协作检测与稀疏传输配额，不是大模型/multimodal foundation表示或VLA控制；不因memory/state词义类比进入。
- 2603.00551 GCL-Sampler：GPU trace graph相似度采样与速度数字，没有当前大模型运行负载/性能选择关系，通用GPU模拟不由kernel owner强行保留。
- 2603.00666 FWeb3：Web3/offchain分离、pluggable aggregation及配置易用性，FL系统拼装没有Foundation训练新机制/可靠性边界。
- 2603.00443 SesaHand与2603.00493 COG：合成手图用于3D重建/单对象姿态估计，未形成多模态基础模型/世界状态/动作闭环新知识链。
- 2603.00482 TokenCom：dual tokenizer/BAN/KAN组合服务无线token通信，只有提升与可行性宣称，没有成立条件或可比资源质量边界，关闭贡献。

TraceSIR（2603.00623）一次必要核心已读：精确v1 §3.1式1仅确定性把messages解析成Thought/Action/Observation三元组；§3.2以阈值θ逐field调用tool抽象，保留faithful semantics是描述目标，没有提出新可验证保真约束/丢失诊断信号的成立条件；Table2整体report LLM-judge分数不能单独归因于上述压缩表示。准入决定是现有trace结构化/逐段摘要加三Agent报告流程，在当前读到的具体证据范围未形成新的执行/诊断可靠性机制；具体关闭贡献，而不是因三Agent字样或待审太多退出。原必要core保留SUP_CORE_TRACESIR.raw/txt，§3.1/3.2及Table2就是停止位置，不另读全文/代码/所有附录。

2603.02263 Social-JEPA潜力已撤销：当前官方abs明确作者撤回，v2和v3均标withdrawn。原API题摘仍可见，但不是有效版本证据；SUP_DATE_02263.raw/txt保留排除依据，不评分、不进候选/Books。无需进一步公开日材料；不是将撤回当作访问故障。原提案行仅作为校准误差历史，不采用。

## root准入校准的实际证据层级

root实际完整核读全部原44潜力的当前Atom摘要，以及原14组代表EX/TraceSIR当前摘要、Social-JEPA官方撤回。这里是准入校准，不是全部精确v1 Full Source Review；各材料当前abs日期/信号原件和必要v1方法core分别保存，不混算证据深审。根据信息未变化的题摘复用，不重复请求全部候选全文。RAIE原领域EX有具体误判依据，仅重开该ID，不推翻其余有效准入结果。root进一步实际核RAIE精确v1 §4.1.3、§4.2式3–6与§4.3式9，三编辑动作、带上限半径/中心与adapter路由支持窄潜力/日期隔离，不证明防遗忘或radius可靠。最终全部45潜力、其余13组代表EX、TraceSIR必要§3.1/§3.2与Table2、Social官方撤回以及14源有限范围/六部分差额DAY实际通过；新增确定0、Books新写0，普通待办0，不授全Coverage/Evidence或无遗漏。

### RAIE一次必要core与最小潜力

原件SUP_CORE_RAIE_V1.raw/txt，实际请求2026-10-08T14:03:33Z，精确https://arxiv.org/html/2603.00638v1。只读§4.1.3区域LoRA映射、§4.2.1式3–6编辑策略、§4.2.2式7–8以及§4.3式9路由，判断即停；没有遍历实验、消融、附录、代码或v2方法。

材料不是仅给static cluster一个adapter名字：式3对unit representation和region中心计算softmax置信；式4以top概率p*和top-second marginδ选三种写入状态，高p*/高δ Update，高p*/低δ Expand，低p* Add。Update对中心/半径EMA；Expand扩大球面半径并设Rmax、移动中心；Add先积累低置信buffer再球面k-means构新region/adapter。式7只对受影响区域的set-up∪incremental数据更新区域LoRA、freeze backbone；式8用区域重叠penalty；式9推理按最近中心激活adapter。因此可核验的潜力是把持续更新的写入单位从global/pointwise移到可移动、可扩张、可新增的region，并让更新/路由局部化。组成操作本身（EMA、k-means、LoRA、softmax）是成熟机制，不计其本身新增贡献；新增待核的命题限定为动态区域编辑政策及由它带来的干扰边界，不声称发明新聚类算法或普遍避免遗忘。

当前core也暴露采用限制：softmax置信随区域数变化；radius/overlap正则与adapter训练如何耦合、nearest-center推理是否足够维持区域分离尚需证据。没有因这类可信度/实现细节未核而关闭准入，但日期未证时不进一步绕过date读实验。若必要公开日证实落窗，才按评分核验该精确版本实际机制/评价对照与这些反证；当前新增确定候选仍0、不评分、不进入Books。

## 已知源差额

OpenAI RSS本日实际恢复2/28唯一OP1，与旧有效家族去重；旧必要安全正文不重审，仅当前页轻量信号。混元API total9/list9全为lang=en，仅2/13→4/23相邻窗段无条目；中文动态页两次浏览器只读失败（初建timeout后getState见同URLtab，getTab再次timeout），不授CH历史覆盖。DeepMind100-item RSS已保存root原XML/13:03:37Z记录时间，不充Publication全目录。Seed首20/page1of13新响应为242库存，不能当窗内命中或全部AB队列。所有具体URL/请求时间/stop见SUP_FETCH；每项必要原入口均仅一次，外部保留项按精确材料重开，不再扩扫。
