# Jan10 补批 13 项独立准入校准

复核者：`audit_supp_jan06`，非本日日报作者；检查日期：2026-10-07（北京时间）。仅处理 root 指定的 13 个家族；补充窗口仍为 `2026-01-09 ～ 2026-01-09`，原17候选/日期/评分/有效审阅不变。已重读 AGENTS、当前研究与 Report 合同、来源使用说明/每日组、统一 Prompt、ROADMAP 相关主线与本日停点。本文仅校准研究合同 §3 的贡献准入；不授日期、候选证据完成、Books 决定/写入或 DAY 验收，不扩其他日期/Weekly。

实际已读 [supplement §5](./supplement-20261007.md#5-新增33篇exact-v1完整题摘定位原文) 中下列 13 份完整 exact-v1 题摘，不以关键词或来源声望判断。三项决定准入的事实起初含糊，已定点澄清方法：OI-MAS §3.2–3.3、AgentCompress §3.1–3.4 的核心说明/Alg1/必要理论声明、Internal Representations 的 Method 与 Inference Protocol；ResMAS 另定点核 Preliminaries 的扰动/目标及 Framework Overview，收窄“resilience”含义。没有一批全文深审，没有加载此前三项 theory-review。

初始三分：**9 项题摘明确符合、1 项题摘明确关闭、3 项需核心澄清**。后三项澄清后 2 项符合、1 项关闭；最终为 **11 项贡献准入通过、2 项贡献前关闭、0 项仍待准入澄清**。11 是本子任务拟入选家族数，不是已核落窗或已审完的正式新增分母；其必要日期与后续证据由日作者/root继续处理。

## 1. 题摘已明确符合（9）

| exact-v1 材料 | 原有约束或判断 → 原文实际增量 → 需重新考虑的选择 | 准入边界与后续证据对象 |
| --- | --- | --- |
| [2601.05240 — Robust Reasoning as a Symmetry-Protected Topological Phase](https://arxiv.org/abs/2601.05240v1) | 连续表示的噪声可破坏符号操作次序 → Holonomic Network 以非交换群/holonomy 操作承载 variable binding，并给出噪声阈值和长度外推对照 → 应核验保序的代数状态是否可作为这类操作的替代架构，而非只扩大普通序列模型。 | 局部新 operator/条件理论与实验均可准入，不因物理术语排除，也不授“一般语义推理的拓扑保护”或无限 causal horizon。后续只需实际更新规则、扰动模型、训练/测试任务与关键反侧，不能把有限 S10 对照当 LLM 通用能力。 |
| [2601.05239 — Plenoptic Video Generation](https://arxiv.org/abs/2601.05239v1) | 单视角重绘可生成合理视频却不能协调后续视角的随机补全 → camera-guided retrieval 将此前生成的多路视频作为 multi-in/single-out 自回归条件并进行 context scaling/self-conditioning → 生成系统需比较独立采样与携带跨视角条件记忆的方案。 | 增量是检索条件化的跨 view 状态机制，不是新的 Basic/Agibot 成绩；以后核检索规则、误差累积、可见/幻觉区域一致性及成本，预测记忆不能冒充真实几何。 |
| [2601.04694 — ResMAS](https://arxiv.org/abs/2601.04694v1) | 只优化无扰动 accuracy 或事后修复不能保证固定节点/边预算下的容错 → 扰动下的 resilience predictor 指导 topology generator，再固定 topology 按邻接交互优化 prompt → 可把主动容错目标与普通准确率目标分开设计。 | Preliminaries 明确是独立随机 agent 输出扰动、归一化性能曲线面积；不是任意攻击/分布式故障保证。Framework Overview 的受扰目标与拓扑相关 prompt 是具体增量，不以两个熟悉模块相加准入；以后核 F(0)、扰动人口、实际 topology/prompt 对照及 predictor 误差。 |
| [2601.05201 — Mechanisms of Prompt-Induced Hallucination in Vision-Language Models](https://arxiv.org/abs/2601.05201v1) | 多模态输出迎合文本可被误认为视觉证据不足 → controlled over-count prompts 下定位 model-specific attention heads，消融改变 prompt copying/visual correction → 应区分文本条件牵引与视觉错误，并定点验证内部干预的权限。 | 明确 mechanistic 反证，不因 object-counting 小场景拒绝；只支持所测模型/计数人口，不授全部 hallucination 因果或无副作用。后续核 head 定位与消融对照、正常计数/其他能力退步。 |
| [2601.05053 — ROSE](https://arxiv.org/abs/2601.05053v1) | 树式 rollout 更细信用仍可能困在语义重复的局部枝 → 在已采路径上以 semantic entropy 选分叉、epsilon 从 root 重启，并用 length-aware segment advantage → 需比较局部扩枝、全局重启及信用长度权重的联合探索预算。 | 具体分叉/采样/estimator 机制已清楚，不因 MCTS/entropy 是成熟概念关闭；以后核 entropy 的人口与语义 oracle 边界、root 与 branch 的预算、长度权重与真实正确性。 |
| [2601.04954 — Precision over Diversity](https://arxiv.org/abs/2601.04954v1) | 混合 hard/soft 约束被视为泛化所必需 → hard-only 与 mixed 的受限比较把 judge 漏检错误及 reward hacking 作为多样性失效解释 → 数据配方应独立比较 reward qualification 与约束覆盖，不默认更多 soft types 更好。 | 对既有设计判断的具体反证，不能只因“高精度奖励好”是熟悉原则关闭；后续须核 reward/训练预算、hardness/内容混杂、未见指令及 precision/recall 定义，不预授普遍 precision 胜 diversity。 |
| [2601.05230 — Learning Latent Action World Models In The Wild](https://arxiv.org/abs/2601.05230v1) | 缺 action labels 与共同 embodiment 时常用离散 VQ latent action → constrained continuous actions 对 in-the-wild 动作复杂性提供替代，并暴露 camera-relative 局部化及 known-action controller 桥接 → 应比较连续/离散动作接口的可迁移能力和 embodiment 条件。 | 增量是表示/接口选择及明确失效边界，不是把视频模型换机器人场景；以后核约束、latent action 与环境变化的分离、controller 标签与 planning 对照，不能授 universal physical action。 |
| [2601.05073 — Milestones over Outcome / SGVR](https://arxiv.org/abs/2601.05073v1) | 终点正确无法区分偶然答案与有效中间推导 → formal proof engine 产可验证 numeric subgoals，Skeleton Rate 把终点与 milestone 信号分开 → 可核验 verifier-granularity 改变训练信用和评价对象的取舍。 | formal-data/verifier/credit 的具体增量，不因几何 benchmark 或“dense reward”标签排除；以后核 numeric subgoal 与证明有效性的关系、Skeleton Rate 定义、漏洞/混杂与 matched credit 对照，不预授真实推理 faithfulness。 |
| [2601.05075 — SemPA](https://arxiv.org/abs/2601.05075v1) | 固定 prompt embedding 不更新表示，专门改模型又可能牺牲生成 → paraphrase 的 sentence-level preference objective 优化表示，并提出 Plackett–Luce 下 DPO/contrastive 联系 → 可比较生成式 preference 更新与专门 embedding 改造的双用途边界。 | 理论联系与训练替代分支均可核验，不因 DPO/contrastive 熟悉而关；后续核实际 preference/embedding 读出、PL 假设及生成退步对照，不把理论联系自动当 representation 改善或无能力损失证明。 |

上述 ROADMAP 路由仅用于确认项目关系：holonomic 对应模型/学习机制，Plenoptic/latent action 对应 Part III，PIH 对应多模态融合，ROSE/SGVR/precision 对应训练信用与 reward，ResMAS 对应 multi-agent，SemPA 对应 representation/preference objective；尚未进行具体 Books 已有覆盖比较，不据路由制造整合提案。

## 2. 题摘明确关闭（1）

[2601.05111 — Agent-as-a-Judge](https://arxiv.org/abs/2601.05111v1)：single-pass judge 的偏差/不可验证局限 → 原题摘提供 planning/tool/memory/multi-agent 的 developmental taxonomy、应用整理和研究 roadmap → 本材料未新增可核执行机制、具体评价盲区/混杂反证或成立条件，不能改变长期设计判断，贡献前关闭。

关闭依据是本题摘实际增量，而非“综述一律不收”；题摘未呈现必要纠错/安全信号，不为寻找隐藏贡献扩读整篇。保留原始发现身份，不评分、不列已审完正式候选、不索日期史。

## 3. 决定准入的核心澄清（3；本次已解决）

### [2601.04861 — OI-MAS](https://arxiv.org/html/2601.04861v1)：澄清后明确符合

初始题摘只有 state/confidence routing 和数字，generic confidence/模型选择主题不足。定点 §3.2–3.3 恢复具体差额：固定 task-level role/model 配置 → 每轮按当前 query/context 用 role probability 累计质量选角色（含 EarlyStop），再为选中角色选择 backbone；生成后 mean-token log-prob 经调整作为 RL 成本项系数 → 可核“逐轮联合重调度及何时惩罚扩容”的方案，而非只在请求开始选大/小模型。

因此窄准入这条配置更新/训练权重机制，不采“confidence 就是真复杂度/正确性”。方法实际原始位置是 §3.2 与 §3.3 Eq4–5；后续 evidence 应核 cross-model confidence 调整、同一 model pool 和状态更新/停止的真实对照、selector/训练费用。未深读完整实测/Appendix B，不因宣传的省钱数授 Evidence。

### [2601.05191 — AgentCompress](https://arxiv.org/html/2601.05191v1)：澄清后贡献前关闭

初始题摘只给 opening words 难度预测→压缩变体选择，尚不足准入。定点 §3.1–3.3/Alg1 看到：统一 precision 对不同任务浪费 → 前32 tokens 的 pooled encoder/features、普通 complexity predictor 与量化/剪枝/稀疏 policy heads、Gumbel selection、缓存 GPTQ variants及 cost+quality-threshold penalty → 原文仍是成熟路由/压缩/缓存组件用于 research workflows，未在本次核心说明中给出新增 operator、相对已有 routing 的重要有效性边界或可核的新 quality 条件，贡献前关闭。

§3.4 另声明 complexity-error 导出 quality guarantee，但短 proof sketch 未明确 complexity 与各压缩配置质量的关系、优化/泛化条件，不能把该声明当已存在的新增成立条件；本轮不采用其保证，也不因带 theory 标签转为全篇深审。关闭不是“摘要少实验细节”或只因领域应用，而是核到的增量仍停在现成组件组合/局部成绩。原发现与本澄清依据保留，不评分、不要求其日期史。

### [2601.05214 — Internal Representations as Indicators of Hallucinations in Agent Tool Selection](https://arxiv.org/html/2601.05214v1)：澄清后明确符合

初始题摘的 same-forward probe 可能只是普通 activation classifier 换任务，先不以 accuracy 准入。Method/Inference Protocol 恢复：外部多次采样/校验才能判断 tool-call → 同一生成 trace 提取 function-name 首 subtoken、argument-span 均值、closing delimiter 的三域 final-layer features，训练 model-specific binary detector，在实际执行前提出 block/confirm/repair gate → 这是结构化字段定位与校验时点的具体替代接口，可窄准入其取舍。

采用边界：不是一次 AR token forward 就知道完整 tool-call，也不是内部状态拥有外部事实或权限。必要证据应核 reference call/argument canonicalization 标签、可替代正确调用、missing/bypass 无可解析字段时的处理、阈值与误拒/漏检及真实开销；不授“86.4% 即生产可靠”。只澄清方法与 gate 的事实，不把其结果表已全部读完/验证。

## 本子任务结束边界

13 项贡献校准均有具体理由，剩余普通准入澄清 0。符合的11项由日作者按必要日期/评分/证据推进；本文件没有重算原评分，没有修改候选表、Books、LearningState或此前三项理论笔记。两关闭项只保留发现和判断，不冒充正式证据完成。若后来出现具体新增机制/反证，只重开受影响判断；不为证明没有隐藏贡献全读附件或版本史。

## 4. 首批五项必要证据与实际 owner PRE（续任务）

本节在保留以上13项准入记录的基础上，另行核 root 已校准的05240/05239/04694/05201/05053；不将上一节准入完成冒充本节证据完成。恢复时完整重读当前合同与适用来源、Prompt、ROADMAP，按 Daily Research Closure 分开证据、owner、写入、POST 与 DAY；仅读 exact-v1 的必要核心及直接相关评价，不比旧版、不遍历附件。原17候选不变，仅提出本批三维评分和具体差额；没有写 Books、Report 或 LearningState。

### 4.1 ResMAS — 2601.04694v1（2026-10-07 BJT）

- **评分/审阅：2+2+2=6，标准审阅完成。** [exact-v1](https://arxiv.org/html/2601.04694v1) Preliminaries Def1–3/Eq3–5、Methods Eq6 与 topology-aware prompt、Experiments Tables1–2/Figs5–7，另仅取 Appendix 的成本/优化配置。没有实现复现。
- **实际方法与证据：** 每轮各 agent 独立以概率 p 输出随机回复；以 F(0) 归一化的受扰性能面积，而非无扰 accuracy，作为固定节点/边上限下的设计目标。task-aware GCN 预测逐题、五个 p 点的 correctness，再汇聚代理 reward；格式惩罚之外还加 |E|/m。先学图，再由邻居提示及正确→错误/错误→正确的交互样例改提示。三数据集局部图预算表及去除两阶段消融支持该分工；Fig5 换 accuracy 目标使 resilience 略退，明确两目标不等价。
- **反侧/代价：** R 高不保证绝对 F(0) 高，F(0)=0 时公式亦无定义。预测头只有 p≤.8 五点，而面积式含 p=1，正文未清楚解释末点预测，不能授精确 resilience oracle；0.86 tuple test accuracy 不证明未见 topology 的无偏 reward。跨任务/模型仍重新优化 prompt，不是整系统 zero-shot。独立随机回复不覆盖相关故障、攻击或真实设备 outage。GRPO 披露8 A100×12h，prompt 优化按数据集/图配置付费；表格也未隔离所有目标、提示与预算差异。域失配时保留固定小图、独立 verifier 与直接扰动曲线，不由 predictor 放行。
- **实际 owner/提案：** 已读 [Ch82](../../../../../books/part-07-agent/82-multi-agent.md) 单 Agent baseline、communication readout/共同噪声段及“典型拓扑”至 Resource Algebra、协议条件配置的完整邻接。已有正文负责信息增益、coordination tax、图预算和协议身份，**未覆盖受扰面积目标与邻接纠错提示的分阶段设计**。建议在典型拓扑/部署前配置附近窄增机制与上述边界两段，不复述通用“更多 agent 更可靠”；不采泛化容错或 Pareto 最优保证。owner PRE 通过仅为提案，待 root 决定/实际写入及非作者 POST，不授 DAY。

### 4.2 PIH — 2601.05201v1（2026-10-07 BJT）

- **评分/审阅：2+2+2=6，标准及受影响因果边界必要深入完成。** [exact-v1](https://arxiv.org/html/2601.05201v1) §3–6/8，Tables1–4、Fig5；仅定点 AppA 的人口/提取/费用与 AppD 的 mean-ablation 公式。baseline 正确的图像再加 over-count prompt，因此 PIH 是这条条件人口，不是全样本一般视觉错误率。
- **实际差额：** 按误导数字→真计数的纠正率逐头排名，再做 model-specific top-m 联合消融；AppD 是将同一 head 的各 token 输出替为其 token 均值，非简单关头。Table1 同时检查正常计数、prompt match 与 true-count，固定这些头后颜色任务亦改善；§6 将数字/词形的 format 与 content copying 分账。正常计数 Janus 80.32→79.41 仍小退；Qwen 的正确 format-copying 反增，Janus 的 image-reliance 解释也与概括语句不一致，故不采“所有 copying 都减少/所有模型都因更看图改善”。
- **未证明/代价：** 均值替换并不数学保证原激活 magnitude 保留（相反向量可平均为0）；干预改变行为支持有限因果贡献，不唯一定位原头内机制，secondary effects 未追踪。所读方法没有明确独立样本上的 head/m 选择验收；三7B、计数/颜色与首非否定数字解析不证明一般能力无损、自由描述 faithful 或 prompt-correct 任务无害。Fig4 caption 与 §6.2 对 Qwen/Janus 最大变化层编号互换，不写确定层号。白盒选择、全 token 均值的人口/在线可用性与任务回归付费，AppA 总实验200–300 RTX3090 GPUh非零成本。接口不可见或副作用时保留原模型、输入级反事实/grounding与独立行为验收。
- **实际 owner/提案：** 已读 [Ch23](../../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) 表示可读/访问/表达的诊断邻接、OCR-head段，以及“Object Hallucination 需要分开视觉写入与语言读取”至 late/full反事实路径。已有头定位与 prior/write-read 原理，但没有**baseline-correct 条件人口的 prompt 冲突、mean-head 干预及 format/content 分离**这条可核诊断。建议在对象幻觉诊断段窄增一对机制/反侧段，尤其防止“纠正提示数字”等于“视觉路径整体增强”的归因；不另建 owner、不采唯一电路或无损裁剪保证。owner PRE 提案通过，未写书/POST/DAY。

### 4.3 PlenopticDreamer — 2601.05239v1（2026-10-07 BJT）

- **评分/审阅：2+2+2=6，标准及检索/压缩必要边界完成。** [exact-v1](https://arxiv.org/html/2601.05239v1) §3.1–3.3/Eq6–10/Alg1–2，§4.1–4.4/Tables1–4；没有全附件遍历或实现复现。
- **可采实际增量：** 不是一次联合采 N 路，而顺次重绘单一路视角，取此前视频/camera对作条件；Alg1 在同 frame 的 near/far frustum 采点，以两方向视锥包含比例的跨帧均值选 top-k **整段视频**，不是物体无遮挡真 co-visibility。context 从小到大训练，再用模型生成的视频替掉干净条件；同 backbone/data 的 ReCamMaster* 与去 self-condition、progressive、随机 retrieval 的局部对照支持取舍。Basic 的 translation error .54 比 .52 略退，Table4 增 context 超6后 synchronization 也退，不采所有质量/所有长度单调改善。
- **不采/代价：** 一致的幻觉不是真实3D/物理/控制真值。Algo2 的 m 先是选取条数，再在补 source 时递增到 k，后续替换前 m 条会连未选入 context 的条目一起删；k=1 时 l 更新无进展。因此不批准其原样作为任意容量的可执行压缩/终止保证，不需为定点错误扫实现或历史。先保留有界 top-k 单输出分支，超容量不凭伪码无损合并。32 H100、context parallel8、只训attention/camera encoder仍非零成本；Agibot分支5天且不做第二 self-conditioning阶段，不能说两套实测均验证此阶段。训练配对、检索/更长attention、缓存视频和串行重绘均付费；更大视角变化、无重叠或回流错误时保留单视角/短干净context与显式几何验收。
- **实际 owner/提案：** 已读 [Ch25](../../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) persistent memory 完整邻接、Matrix-Game train/rollout gap、HYWorld2 spatial packing与 UCM correspondence 段。**跨view记忆、生成回流与训练扰动主原则已有覆盖，不重复新增。** 真正窄差额是同步整段视频的 frustum-mean retrieval、独立多视角采样改为multi-in/single-out re-rendering，以及 context capacity/融合并非越大越好。建议在 memory检索、无序reference邻接补一条受限替代分支及上述测量权限，不用 HYWorld2 的 spatial packing覆盖/否定这里camera标识的temporal concatenation，也不把它写成 action-conditioned world transition。owner PRE 提案通过；不采 Algo2原样执行/任意容量保证，未写书/POST/DAY。

### 4.4 ROSE — 2601.05053v1（2026-10-07 BJT）

- **评分/审阅：2+2+2=6，标准及采样/公式权限必要深入完成。** [exact-v1](https://arxiv.org/html/2601.05053v1) §3/Eq1–10、§4/§5 Tables1–4/Limitations，仅定点 AppA2 的 ε端点。实测数学、3B–8B，不读所有 case/附件，不复现实现。
- **可采机制：** 全路径生成后，在已有路径上按 top20 token embedding 的加权 cosine 与 vocab entropy 乘积选分叉，以概率 ε从root另采；树节点取经过它的叶子 binary reward 均值，段advantage是两端均值差。其他较长正确分支与最短正确分支分歧后按长度比修正：正A缩小，负A按 `2−ratio^α` 放大负幅度，不是所有A统一乘长度比。这是经验 credit/controller，不是逐token真值。Table2 指标对照、Table4 root/random/信用消融支持有限方案；移除信用同时换GRPO loss，未单独隔离estimator。
- **必要反证/未证明：** Eq2 的全双和有 `SD=−||Σ p_i normalize(e_i)||²≤0`，故 Eq3 非正，非标准非负语义熵；H→0的近确定点也趋0，不由max(SE)认证真正最不确定位置。静态token embedding、截断且未明确重归一化top20概率不是真语义等价oracle。自适应选前缀/共享叶子的条件人口不同于iid rollout，节点均值不是已证明的无偏条件solve probability，Eq9未建立选择law/inclusion校正，不授无偏原policy-gradient。Table1 Qwen的MATH500仍低于TreePO，pass@8不是pass@1；更大α缩短也损pass@8，未给同GPU时间/总tokens的净效率匹配。8 A800、指标计算、branch重采及祖先/终局verifier都付费；不稳时保留独立rollout、普通sequence advantage/已验process verifier。只采用Experimental启发式，不采语义entropy定理或“提高正确且无性能牺牲”。
- **实际 owner/提案：** 已读 [Ch33](../../../../../books/part-04-training-system/33-grpo.md) outcome→细信用的suffix/PRPO/DART完整邻接、语义Segment与ProVer，以及“Rollout Tree分支预算”完整两段。现有树credit/entropy非oracle/预算原则已覆盖，但**embedding加权分叉＋εroot重启、正确兄弟分支分歧后的符号敏感长度校准**未覆盖。建议在DART后增加不依赖tool-hint的具体Experimental替代及公式/人口边界，不在另一处重复通用树搜索原则。owner PRE 提案通过；未写书/POST/DAY。

### 4.5 Holonomic Network — 2601.05240v1（2026-10-07 BJT）

- **评分/审阅：2+1+2=5，标准及受影响理论必要深入完成。** [exact-v1](https://arxiv.org/html/2601.05240v1) Results Figs1–4、Methods 的 synthetic任务、effective-action Eq1–5、geometric Eq6–8、architectures Eq9–10、noise Eq11、训练/float64/initial-state Jacobian Eq12。没有附件遍历、代码或复现。
- **可核机制/有限证据：** 每个离散操作的可学 M 先做 `A=M−Mᵀ`，再 `U=Exp(A)`，输入选择U，向量状态乘U而不加外部forcing；精确算术下保norm、连乘可scan。S3噪声对照仅L5，另S10 swap训练Methods为L5–50，float64测试至5000； normalized RNN、常规RNN/有位置编码Transformer及不同width对照支持这个有限替代分支，但没有等总算力/成熟现代hybrid的普遍胜出。45个swap operator不是通用自然语言推理/无穷历史归档。
- **必要理论反侧：** `||∂h_L/∂h_0||=1` 只保初态敏感性；错误但正交的rotation也满足1，不能证明逻辑读出正确、参数梯度稳定或操作同态。只令每个U落SO(N)未强制其学到exact group multiplication关系，近似错误可随反复组合积累。Eq8有限轨道点间距是metric separation，不由离散点集合推出SO群/球面的互不连通拓扑sector；Eq11为各步Gaussian噪声，有非零尾部且多步累积，有限无错平台不证明无限噪声保护。effective-action 由实状态到spinor、causality到chirality/fermion determinant的桥梁是所读推导额外假设，未从训练网络建立；不采Chern–Simons/RG/anyons、通用hallucination、无限因果horizon或scaling不可能定理。positional/context-dependent attention的加权求和也不等整个Transformer算子交换，有限baseline不足排除order-sensitive reasoning。
- **代价与退路：** 矩阵Exp、每操作参数、自动微分、顺序或矩阵scan、float64及推理renormalization有成本；闭包的精确表达不是有限精度实现验收，未给可批准的端到端GPU/seed统计。规则/表示容量不匹配、误差积累或费用不稳时保留显式symbolic transition、原recurrent/hybrid Attention与历史回读，不用初态Jacobian替任务验收。
- **实际 owner/窄提案：** 已读 [Ch22](../../../../../books/part-02-model/22-long-context.md) “非扩张的状态转移也可以包含旋转”完整邻接及群本体状态/Exp段；另定点Ch4容量/优化/泛化边界。现有Ch22已覆盖非交换/有限群构造、norm非总状态/训练保证、群state闭包与有限精度，**不重复增加“正交群更新更稳”通用机制**。唯一建议差额是旋转段后的一条具体诊断边界：初态isometry与符号orbit的metric margin不能认证操作同态、长期逻辑读出或带逐步噪声的拓扑保护；可连同本稿有限离散input→operator实测作Experimental例证。这比新建拓扑学习主线或把所有数学宣传采入更窄；若root认为该具体反证被现有段足够承载，可Only Report并给上述精确覆盖理由，不能仅因实验小关闭。owner PRE 完成/提案待root决定，不采其强拓扑理论；未写书/POST/DAY。

首批停点（2026-10-07 16:05 BJT实测查时）：**5/5必要证据与实际 owner PRE完成**；均已恢复exact-v1必要HTML，新增access hold 0。四项具体机制提案与Holonomic一条窄诊断边界提案交root决定；本节不预授Books处置/写入、POST、正式新增分母或DAY。以上13项原准入与反证保留；此次没有改原17、Report、Books、LearningState或此前theory-review。

## 5. 余六项必要证据与实际 owner PRE（同日续任务）

仍仅Jan10补充自然日Jan09，保留§1–4与原17。恢复重读AGENTS、Research/Report当前合同、Prompt、来源使用说明/每日组及ROADMAP，本日README与具名题摘/停点；按Daily Research Closure分层，未扩日期/来源，未写共享文件。本节评分针对实际新增命题，owner是提案而非Books写入或DAY验收。

### 5.1 OI-MAS — 2601.04861v1

- **评分/审阅：2+2+2=6，标准与具体owner差额必要审阅完成。** [exact-v1](https://arxiv.org/html/2601.04861v1) §3.1–3.3/Eq2–5，§4–5/Tables1–3，AppB confidence与AppC成本的必要说明；不遍历case或复现。
- **实际机制：** 每轮query/context的角色概率按累计质量选子集，含EarlyStop即停止；再按所选role条件选backbone，不是请求开始的一次模型路由。生成后平均token log-prob经模型近期统计归一化，冷启动用exp再插值，作为训练成本惩罚的单调权重；高confidence更重惩罚，低confidence放松。它改变训练取舍，不是线上由confidence直接签正确结果。L4、θ.3、λ200、temperature0与固定四模型池下，对比query-level MasRouter并有model-router/cost/confidence消融、MBPP→HumanEval转移支持有限替代。
- **反侧/费用：** AppB的percentile scaling/插值未完整参数化，不证明跨tokenizer/任务正确性校准；同为[0,1]不等同正确概率或真实复杂度。去model-router/cost反而略增accuracy而增费用，去confidence更便宜但降accuracy，故不是每组件无代价全面占优；更多轮/更强惩罚有反退。AppC本地GPU调用却以API价格代理成本，3B价格由参数幂律估算，不能称实测GPU省79.78%/生产SLO。A10080G/vLLM同硬件解码并未披露完整并发、precision、GPU总量/训练费用或seed；23.12s仅GPQA单请求。role/encoder/routing、上下文与多模型部署计费，EarlyStop不是独立义务验收，保留硬turn预算与独立verifier；校准/模型池漂移时回固定role/model小池或单Agent。
- **实际owner/提案：** 已读 [Ch82](../../../../../books/part-07-agent/82-multi-agent.md) runtime有界修复、peer探索、离线role相关profile及fleet-confidence的完整邻接。已有query/topology/role能力与错误相关性原则，未覆盖**逐轮role→model重调度和生成后confidence仅调训练成本权重**。建议离线role-profile后窄加Experimental分支与成本代理/停止权限边界，区别离线GT自评与线上log-prob，不能把通用模型路由另写到平台章。owner PRE提案通过，未写书/POST/DAY。

### 5.2 InternalTool — 2601.05214v1

- **评分/审阅：2+1+2=5，标准及字段/评价矛盾必要深入完成。** [exact-v1](https://arxiv.org/html/2601.05214v1) Problem/Method Eq1–3与Inference Protocol、Experimental Setup/Main Results/Tables1–3、Feature Extraction说明。没有运行或读取整份附件。
- **所提机制：** Glaive reference function/arguments规范化后和重新生成call比对作标签；最后层function-name首subtoken、arguments均值、closing delimiter三域拼接的Eq1提出model-specific MLP，在完整AR call生成后决定block/confirm/repair。不需要额外候选采样，不等仅一个AR token forward，不提前知道尚未生成的参数；reference agreement亦非外部真实性/权限标签，替代合法call可能被错标。
- **关键反侧：** Table1标题称hallucination类，数值实际对应Table2 weighted average；GPT-OSS错误类recall是.53，非.86；Llama为.61，Qwen为precision .34/recall .62。正文更高错误召回概括不采；其precision/accuracy也低于多采样基线。Table2 support为全部2411/Qwen2000与所述60/20/20 test身份未桥接，不能认为逐例held-out身份已证。Method默认3d三字段，但训练输入d，Table3推荐全sequence last-layer mean，三域真实评测/投影身份没有明确绑定；不能将mean结果授三字段定位收益。missing/bypass没有可解析字段时Eq1的fallback未定义，也无blocking后真实effect实验。n3 baseline又称5×成本而无真实latency表，不采零/近零开销或实时安全部署。
- **实际owner/处置提案：** 已读 [Ch78](../../../../../books/part-07-agent/78-tool-calling.md) proposal→schema/semantic/authorization邻接和“Tool Necessity与Execution Admission”及internal call-offset sensor完整邻接。该owner已有内部sensor仅提proposal、外部验收/权限独立的命题；通用model-specific hidden-state MLP换成tool任务不再升格通用原则。先准入的三字段/验收时点是具体可核提案，但实际评价未绑定这一字段机制，未证明较现有sensor+显式call验证新增可支持设计取舍，因此建议**仅报告，保留三字段待验证与表格纠正**；不是因实验有限或先前准入被取消。若root需保留窄Experimental接口，最多写“本文提议的三字段特征”，不得绑定headline成绩/已实现高召回/无解析bypass覆盖。新增gap材料需求只限该字段人口/投影与真实漏检、effect-time开销，不索所有数据/历史。当前可用必要源已读完，非access hold，不授Books/POST/DAY。

### 5.3 Precision over Diversity — 2601.04954v1

- **评分/审阅：2+2+2=6，标准与奖励口径/筛选必要边界完成。** [exact-v1](https://arxiv.org/html/2601.04954v1) §2–3/Table1–2/Fig4–5、§4–5/Eq1/Table3–4、Limitations、AppD.2–3与AppE/F必要定义和消融；不读全部附件/实现，不复现。
- **实际增量：** 在22k VerInstruct、77.7% soft/22.3% hard及固定GRPO的有限IF实验里，hard-only可比mixed接近或更好；不能假设扩大judge监督约束种类必然胜于较可靠窄代理。奖励是所有约束判定的乘积；HPPT先pilot（例5epochs）保留曾获正reward的样本，再把每条soft约束限制至一个。Table7逐步消融支持组合局部收益，不证明过滤的是逻辑不可满足任务。Table2的precision和错误类negative recall须分开；AppE的200实例、三专家/争议裁决给有限标签来源，非所有judge真值。
- **不采/费用：** 随机噪声是概率p强制置1的单向false-accept，不是对称翻转或真实judge相关噪声；≤10%并未退化，不能推所有噪声必降。以每条约束数量替“diversity”没有隔离语义覆盖；Table3 hard-only在CFBench/FollowBench及32B平均也不全面胜mixed。§3.2的OOD文字/图注自相矛盾，不采普遍强结论。Attention变化只是观察，Limitations承认缺定量internalization证据，不批准通用meta-skill/基础推理因果证明。pilot零正例可能只是policy/budget不足，过滤引入curriculum/selection bias；每步8.23 vs19.63min约58%仅该32B配置，不含所有pilot/数据/总训练成本。AppD披露7B64 Ascend910b、600steps/8rollouts/TP4但完整precision、32B资源和重复运行未清楚；部分外部baseline仅已发表成绩，非预算匹配。无可靠proxy时仍需judge/人工评价，保留原mixed、困难样本及独立OOD回归。
- **实际owner/窄提案：** 已读 [Ch31](../../../../../books/part-04-training-system/31-rlhf.md) RLHF/RLAIF/RLVR完整邻接、task generation/可靠verifier取舍、test-tier curriculum及Imperfect Verifier；已有confusion profile×rollout预算、可靠性非完整覆盖原则，不重复这些通用命题。建议在Imperfect Verifier后补具体Experimental分支：**IF中pointwise约束可靠性与约束支持分账，pilot-ever-positive admission＋单soft约束可作有偏代理替代，不能由更多约束或training reward授泛化**；这个筛选/监督粒度联动及退路现段没有覆盖。PRE提案交root，未写书/POST/DAY。

### 5.4 Learning Latent Action World Models In The Wild — 2601.05230v1

- **评分/审阅：2+2+2=6，标准与预测/迁移/控制及公式权限必要审阅完成。** [exact-v1](https://arxiv.org/html/2601.05230v1) §3–9/正则定义、Tables1–2/Figs4–12，AppA必要架构开头；不遍历可视化/全部附件，不复现。
- **实际机制与增量：** 冻结V-JEPA2-L frame-causal encoder，inverse由当前/未来帧提出128维动作，joint forward以teacher forcing重建下一latent；比较VQ/codebook reset与稀疏连续（L1及variance/covariance等防退化项）、VAE式噪声瓶颈。野外复杂动作下连续正则允许更宽预测容量，但**最小预测误差不等最可辨/最佳控制接口**。场景拼接测试只排查完整后帧复制的一种极端shortcut，跨视频apply→re-infer循环只检查模型内一致；camera-relative空间局部运动不是共享actuator语义。实际控制需另外用带真实action的DROID/RECON及历史状态训练adapter，action-only可塌到不动，不是全路线免标签。
- **反侧/代价：** 自由度与transfer冲突；量化在简单已知action空间仍工作，规划不全面胜专用V-JEPA2-AC/NWM，DROID H3为有限goal-position协议，不能授真实长期闭环/安全保证。Table2离散cycle ratio更接近1却原预测更差；没有以cycle指标认证物理迁移。noise正则书写为负βKL而文字称prior matching，未明确总损失符号，故不原样授可执行loss/理论信息界；sparsity项亦为经验容量controller非因果辨识证明。静态coefficient不能随每片复杂度校准，模型/数据scale并不均带来planning提升。30k×batch1024、16frame4fps、大冻结encoder和joint网络/decoder/controller/CEM均计费，完整硬件/precision与重复运行统计未披露。不可辨/adapter不稳时保留带校准action的inverse/forward、固定量化小空间、更完整观测与真实环境验收。
- **实际owner/提案：** 已读 [Ch25](../../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) latent预测→outcome、inverse anti-collapse完整邻接、external effect-reference及factorized inverse/forward。已有预测非控制、动作不可唯一恢复/adapter需标签主命题，不重复升格。具体缺口为**野外无共同embodiment时连续容量正则相对VQ的条件替代、camera-relative locality与state-conditioned adapter；容量/循环一致/控制不能按同一指标选最优**。建议inverse anti-collapse后、effect-reference前补窄Experimental分支及简单action VQ退路，不写强loss符号/因果动作保证。PRE完成交root，未写书/POST/DAY。

### 5.5 SGVR — 2601.05073v1

- **评分/审阅：2+1+2=5，标准与奖励对象/验收权限必要深入完成。** [exact-v1](https://arxiv.org/html/2601.05073v1) §2.1–2.4/Eq1、§3/Eq2–5、§4.1–4.3/Tables1–4及mask反侧、Limitations、AppD必要predicate映射/AppE–F配置与checker；不读完整case/全部附件，不复现。
- **实际机制：** TrustGeoGen先验证参考formal skeleton的type/dependency/derivability，再把predicate映成数值子问题（如congruence→长度比1），模型对给定有序slot答值。SR是每题子目标正确率后跨题平均，SC要求每题全正确，CR=dataset SC/SR（SR0时0），并非逐step条件概率或真正因果连贯性。**训练仍把SR汇成一个trajectory reward、一个group-normalized sequence advantage**；不是segment-specific梯度或每次真实工具transition信用。可核差额是形式参考→数字可检查子目标这一监督生产分支和部分成功/全链/末项三分账。
- **关键反侧与成本：** 正确数字不证明生成文字的derivability、没有跳步/猜测或真实internal reasoning；映射本身可能只保留predicate部分条件（如rectangle只检查一处90°）。§6称deterministic numerical checking，而AppF明确GPT-5-nano判equivalence、regex读XML/NOT SURE人工；不能授规则checker零错，训练checker与评价身份桥未完全说明。256train/256test、test长链偏移、Qwen2.5-VL3B/7B的Table4比FA/SC支持有限平均优势，但7B MATH500/LiveBench及某mask配置仍有更强baseline；非所有更密监督/GRPO都胜。受训7B模型测试SR87.7对应SC15.2，未解决全链失败；外部process评价靠LLM judge非形式证书。8H100/BF16/ZeRO3/G8/4096tokens、参考合成/映射/checker与人工争议均计费，训练steps/完整wall-clock与seed未充分披露，不宣称同总预算净收益。无可核子目标/映射覆盖失真时回最终reward、正式证明checker或经校准process verifier，保留原任务成功验收。
- **实际owner/窄提案：** 已读 [Ch33](../../../../../books/part-04-training-system/33-grpo.md) phase-specific/milestone/语义segment/ProVer完整邻接以及Verifiable Process Supervision的claim验收段。已覆盖milestone非因果/过程claim非长trace原则；**不能把本文再写成已有双尺度segment advantage**。建议milestone邻接补Experimental“formal参考骨架→数值slot→SR汇总sequence reward”的替代，明确它改变reward密度/目标而不改变信用粒度；SR/SC/FA不同及numeric agreement非formal proof随段保留。PRE交root；未写书/POST/DAY，必要HTML无access hold。

### 5.6 SemPA — 2601.05075v1

- **评分/审阅：2+1+2=5，标准与PL/能力保持受影响理论必要审阅完成。** [exact-v1](https://arxiv.org/html/2601.05075v1) §3/Eq1–3、§4.1–4.4/Eq4–6/Table2、§5–6/Tables3–6、Limitations及AppA必要配置；不读全部附件/代码，不复现。
- **具体机制：** 用NLI premise作anchor、entailment/contradiction作chosen/rejected，在“保留含义改写”prompt上做reference-relative sequence DPO；LoRA更新生成模型，再用PromptEOL末输入token的最后层hidden state作单句向量，不需要真正生成one-word/CoT、不改双向attention或加embedding分类头。NLI单向entailment不是双向paraphrase等价，属于监督proxy。Eq3/6只是二候选DPO和InfoNCE共享top-rank softmax/Plackett–Luce形式：前者score是policy/reference log-ratio，后者是embedding similarity；**不推出梯度、几何、能力保持或各自目标等价**。没有必需未读理论proof gap。
- **关键对照/未证明：** LLaMA2-7B/3-8B、40–80k子集按STS-B dev挑选，七STS Spearman局部提升支持decoder表示训练替代；Table3并非每slice最佳，超过100k有over-alignment反退。Table6 DPO的GSM8K均退（7B −2.35、8B −3.79），7B DROP −9.21、8B MMLU也退；平均提高不授generative能力无损。作者自建PromptEOL contrastive对照的下降不证明全部contrastive/architecture change必损生成，也未隔离相同所有调参/预算。只有STS而无实际corpus召回/answer support，不授RAG质量或生产吞吐；isotropy/GAR为几何/表面token诊断非语义真值。四RTX5090、LoRA r8/α32、有效batch256/AdamW及模板/模型驻留、encoder适配/索引重编码计费；β、完整precision/wall-clock/独立seed未完整披露，不由0.3%trainable参数授便宜online embedding。
- **实际owner/提案：** 依ROADMAP并已读 [Ch12](../../../../../books/part-02-model/12-embedding.md) token/context/sentence接口分责、[Ch34](../../../../../books/part-04-training-system/34-dpo.md) BT→reference log-ratio及local PL/DAG完整邻接、[Ch76](../../../../../books/part-07-agent/76-rag.md) 检索表示质量/encoder训练适配完整邻接。DPO基本loss/PL及几何非能力原则已覆盖；句向量归Ch76而非token lookup Ch12。Ch76缺**生成policy的语义偏好训练→固定prompt末hidden readout**具体替代，建议表示适配段前后窄Experimental：不直接对向量contrastive，必须共同验STS/实际召回/原生成切片，NLI proxy、模板/revision与全索引更新分账。检索未验不否定这一表示机制，但只能给候选encoder资格而非RAG验收；退路为原PromptEOL、专用contrastive encoder及既有lexical/hybrid。PRE提案交root，不另造DPO章节理论主线；未写书/POST/DAY。

余批停点（2026-10-07 16:24 BJT实测查时）：**6/6必要证据与actual owner PRE完成**；score依次6/5/6/6/5/5。五项窄Experimental提案与InternalTool Only Report提案已逐项交root/日作者；所有处置均待root独立决定，不自授Books写回/POST/正式新增分母/DAY。新增access hold 0，未运行代码或复现实验。原13准入/反证、首5证据、原17及此前theory-review全部保留，本批只写本文件§5；不扩日期/来源、不stage/commit/push。
