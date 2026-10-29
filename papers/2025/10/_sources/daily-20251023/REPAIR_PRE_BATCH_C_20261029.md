# Batch C 完整PRE

writer Locke；sole reader Chandrasekhar。五项均2+1+2=5，实际新长期差额触发必要深入，尚未写入。各只一完整段/独立marker/本人注，原正文/他注/原marker保留，不锁全章。原件/边界见EVIDENCE、R19；owner与直接邻接/相邻章开篇交接实际已读。注只加唯一H2 Review notes后，reader整体核包括磁盘注邻接，不预签SAVE或POST。

## C1 MENTOR / TRAIN-GRPO / Ch33

文件：`books/part-04-training-system/33-grpo.md`。已有query参照与最终outcome，没有工具**集合**替代整条轨迹的模仿粒度；不归Ch29一般SFT。Ch32概率比率/Ch34偏好分类职责不变。

### 完整前邻接

多轮检索的监督还可以显式包含query改写参照，而不只奖励最终答案：对生成的每次query，与训练可见的human或teacher改写计算词面F1并取匹配proxy，再与当前turn整条检索—回答轨迹的终局分数共同训练。[ChatR1的有限对照](https://arxiv.org/html/2510.13312v1)把query意图与回答结果分开提供，却不让词面匹配成为部署时真实用户意图、语义faithfulness或每次search的独立因果credit；摘要中的逐turn反馈也不能改写成每个工具动作都有独立真值。应保历史/原问题、参照改写来源、query与召回文档、reward聚合和turn边界，分别验词面、真正支持与最终答案；teacher改写是训练特权，线上仍须由原query/证据和用户需求验收。3B/7B、E5base/top3与最多两call的受限训练仍有任务反退，reasoning更长不证明规划机制。参照制备、全部检索与rollout/判分、训练和多轮回归均计费，未披露总时延不补净速度；改写支持、历史或质量失配时，保原问题/已验改写、可靠outcome与可追溯检索，不由wordF1或终奖批准真实意图恢复、全步骤正确和低成本交互。

<!-- source-family:SF-2025-ARXIV-2510-13312 -->

### 完整新增与marker

教师参照也可以只约束用了哪些工具，而不强迫学生复制每个中间动作：分别奖励与教师工具集合一致、最终答案与受gold核验的教师答案一致，以及调用实际可执行。[MENTOR的精确首版](https://arxiv.org/html/2510.18383v1)在所测训练中采用严格集合匹配，不能用后版的柔性描述替换本版规则；同集合仍可能参数、顺序和观察不同，可执行也不证明语义正确或副作用安全。这种粒度让工具选择有参照而执行路径保留自由，但会继承教师选择偏差，并支付教师采样、全部工具/验证与RL训练费。有限数学工具训练及跨任务对照还有反退，不授通用工具最优；教师、执行反馈或质量不可靠时，保留可信outcome、原工具协议或完整verified trace，不由过程匹配批准真实任务与权限。

<!-- source-family:SF-2025-ARXIV-2510-18383 -->

### 完整后邻接

有参考答案却没有可靠 outcome verifier 时，一个受限分支是在 sampled CoT 后 teacher-force 参考答案，用当前 policy 给它的似然作 reward，而不是另外采样答案再判断对错。整段概率、log-probability、平均 token 概率与平均 token log-probability不是中性的单位换算：整段概率会因长参考序列变得极小，长度归一则改变不同题目与答案长度的相对权重；平均 token 概率也不是整段正确概率。参考答案的覆盖与质量仍限制监督，不能把较高似然当作所有有效答案的接受率。额外 forced forward、数值稳定性和答案长度分布都须进入 reward contract；可靠 verifier 可得时，原 outcome reward 仍更直接。[受限 reward 对照](https://arxiv.org/html/2602.03979v1)。<!-- source-family:SF-2026-ARXIV-2602-03979 -->

### 本人注

本人注：`SF-2025-ARXIV-2510-18383` — Locke，Daily2025-10-23补Oct22；exact-v1 §3.3/4.1/5.2/限制必要，2+1+2=5，仅工具集合而非全trace与答案/执行三reward权限差额深入。保v1 strict集合/后版不可倒填、teacher/gold来源、执行非语义安全、OOD反退和全部调用/训练费；未核实现/复现。整体PRE/SAVE/全自读/sole actualPOST仅本日实际层。

## C2 ICD / AGENT-CONTEXT / Ch75

文件：`books/part-07-agent/75-context.md`。现有固定demo反复伪标，不含跨request扩pool、当前student答复与异步teacher的不同消费时点。Ch74只条件输入、Ch76检索机制，在线工作集owner仍75。

### 完整前邻接

它把上下文选择推进到 self-conditioned refinement，却会放大早期错标，可能收敛到语义一致但任务错误的
fixed point，并以 `O(iterations × demonstrations)` 的 model calls 换取修正机会。原始 demonstrations 仍是
authority，pseudo-label vector 只是可丢弃视图；真实 label、Memory 或 source artifact 不能被它覆盖。CIRCLE
只在其 open-world multimodal ICL 设置中支持该机制，不证明 LMM 普遍优于 VLM 或迭代一定提高真实 taxonomy。

### 完整新增与marker

示例工作集也可以沿请求流扩展，而不更新学生权重：先以学生输出entropy决定是否检索已有demo，仍不确定时异步请求教师标注，将通过筛选的示例写入pool供后续请求使用；当前回答与未来pool更新因此是两个不同事件。[ICD的受限多模态对照](https://arxiv.org/html/2510.18117v1)用多次教师一致和跨模态匹配筛选，但一致/相似与低entropy均不是真实正确率，不能把稍后得到的教师答案说成本次回答已被纠正。应保存示例来源、教师/encoder版本、可见请求次序、写入资格与失效条件；pool会继承错标和漂移，检索、demo prefill、教师多次调用及驻留均计费。无参数更新不等零蒸馏成本，碳排proxy也不是完整服务实测；示例失配或预算不足时，隔离派生pool、保可信固定demo与原学生/显式教师路径，独立验收当前答案。

<!-- source-family:SF-2025-ARXIV-2510-18117 -->

### 完整后邻接

### Semantic Policy 与 Recoverable Bookkeeping 应分 Owner

短 research loop 把 candidate、已读证据、importance、verification 和 budget 全留在 transcript 中，透明但会随
horizon 溢出。更长 search 可以让 policy 只决定 search/read/curate/verify/stop，把候选池、全文 store、证据图、
verification cache 与 renderer degradation 交给 harness：

### 本人注

本人注：`SF-2025-ARXIV-2510-18117` — Locke，Daily2025-10-23补Oct22；exact-v1 §4–5/A.4.1必要，2+1+2=5，当前回答/未来异步教师demo写入差额深入。保三次一致/entropy/相似非truth、SigLIP替换基线、派生pool漂移与教师/检索/prefill全费；不采实测全碳或服务SLO，未核实现/复现。整体PRE/SAVE/全自读/sole actualPOST仅本日实际层。

## C3 LDDM / MULTIMODAL-GENERATIVE-PARADIGMS / Ch24

文件：`books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md`。已有AE→latent prior→discrete decoder；新稿是连续latent与token各自加噪、联合或先后两channel采样，区别于共享route mixture。Ch23拥有codec，Ch25拥有环境转移，不改变归属。

### 完整前邻接

分层表示减少部分生成步数，却会新增 reconstruction loss、跨阶段漂移和 decoder 幻觉。作者实验不证明连续 latent 对所有文本任务更优；latent 失真、decoder 不忠实或联合校准失败时，应回退纯 masked diffusion、更多 steps 或自回归解码。arXiv:2605.23605v1
<!-- semantic-body-binding:SF-2026-ARXIV-2605-23605:end -->

### 完整新增与marker

共享latent也可以与离散token共同走去噪过程，而不只先生成一份固定条件：分别给连续latent与token加噪，令两channel联合预测，或先把latent去噪完再条件化token更新。[LDDM精确首版](https://arxiv.org/html/2510.18114v1)以共享随机条件缓解逐位置factorized reverse的部分依赖压力，不等于条件化后真实位置必独立，也不是任意并行生成质量的不可能定理。训练需限制latent幅度以免通过放大信噪比规避目标，实际忽略端点/改变权重的loss亦不继承理想tight ELBO恒等式。编码器、两个channel全部求值与latent驻留均计费，少token steps不能漏掉latent采样；有限短文本的外部生成PPL/entropy不认证真实似然或任务质量。latent失真、联合训练或总预算失配时，保留单channel、顺序条件路径及原AR/多步sampler，不从更强联合表达批准无损与免费少步。

<!-- source-family:SF-2025-ARXIV-2510-18114 -->

### 完整后邻接

## Cache、rollback 与 exactness

### 双向生成中的 Cache 是可变状态，不是只读前缀

diffusion 或 masked refinement 会反复修改序列两侧，传统只追加 KV cache 的不变量不再成立。复用稳定 affix 可以减少重算，但 request-specific anchor 与被更新位置必须重新计算，并把 timestep、mask 和版本纳入 cache identity。错误地沿用自回归前缀语义会产生静默污染；保守全重算仍是低复用或高变化率下的正确基线。
<!-- source-family: arxiv:2608.26140v1; semantic-body-binding: bidirectional-affix-cache-mutability -->

### 本人注

本人注：`SF-2025-ARXIV-2510-18114` — Locke，Daily2025-10-23补Oct22；writer exact-v1 §3.1–3.2支持、reader R19 §2.3/3.2/5关键反侧，2+1+2=5。仅continuous latent/token双channel联合/先后采样差额深入，不倒填后版discrete latent；保factorized NELBO界范围、实践端点/权重差、unitnorm与latent额外64steps、LM1B短文本代理及全费。未核实现/复现，不授通用tight likelihood/少步保证；PRE/SAVE/全自读/sole actualPOST仅本日实际层。

## C4 Planned Diffusion / MULTIMODAL-GENERATIVE-PARADIGMS / Ch24

同一文件；新稿是AR先提出语义span计划，再异步隔离生成/同步，而非只选固定block宽或一般plan→tool。

### 完整前邻接

固定 block size 只是策略之一。工作负载变化时，最优 size 可能依赖 entropy、prompt、硬件、batch 和 SLO。

### 完整新增与marker

块划分还可先成为模型产生的计划：用AR路径提出各span的主题与长度，随后让同一模型在隔离的span内双向去噪、跨span异步推进，到同步边界才重新共享完成内容和缓存。[Planned Diffusion的受限分支](https://arxiv.org/html/2510.18087v1)把全局组织与局部并行分开，不证明计划中的语义独立为真，也不能在span未定时把其双向KV当稳定prefix。计划/长度错会截断内容或多付padding，较密交互版本更慢却可能质量更好；生成步数的关键路径比例不是墙钟倍数。教师标注、计划、全部denoise、同步和缓存重建均计费，Dream7B/四H200的均值延迟与AlpacaEval质量取舍不授等质量服务SLO。依赖强、长度失准或净质量预算不合时，回退较短顺序块、更多同步或AR，不让格式合法的计划批准独立提交。

<!-- source-family:SF-2025-ARXIV-2510-18087 -->

### 完整后邻接

视频的时间分块也可以不取统一长度，而先用训练轨迹的动作变化给片段划分长度，再分别训练长度专家，由部署时的文字与当前视觉预测下一段该用哪个专家。[受限长视频分支](https://arxiv.org/html/2509.21790v1)以动作幅度和夹爪变化构造离线标签，不代表线上会读取未来动作；反过来，只见过去视觉和文字的router也没有获得可查询动作干预的环境转移接口。这里长度决定生成模块及边界，不是token置信提交门，动作标签的启发式阈值也不认证语义动作已经完整。分类正确率须与独立长轨的边界误差累积、视觉延续及动作后果分别验收；更长固定块仍有画质分项反退，变长与多专家的联合收益又未隔离同容量/等预算控制。只激活一个专家不等只保存一份权重，四套专家训练、标签制备、router、换入驻留及完整生成回归都计费；误路由、单位/动作分布变化或净预算不合时，保留固定块、单专家与较短生成段，不由视频指标或分块名称批准物理因果、闭环成功或通用实时。

### 本人注

本人注：`SF-2025-ARXIV-2510-18087` — Locke，Daily2025-10-23补Oct22；writer exact-v1 §4.1–4.4支持/reader R19 §5/6关键反侧，2+1+2=5，AR语义plan→async隔离span→sync/cache差额深入。保独立假设非真、dense质量/时延取舍、长度/pad/epoch/LCWR人口与全费；不授等质1.81x、全任务去barrier或生产SLO。未核实现/复现；PRE/SAVE/全自读/sole actualPOST仅本日实际层。

## C5 MoT-VLA / MULTIMODAL-EMBODIED-VLA / Ch26

文件：`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md`。已有冻结动作主链+视觉旁路，不含冻结通用语言generalist与运动domain expert分工、运动hidden直接条件动作而不逐token解释。仅新增该条件接口，不宣通用推理被因果保留。

### 完整前邻接

Mediator 会增加 token、参数和训练不稳定面，也可能在数据不足时形成新的信息瓶颈。作者的零样本 sim-to-real 实验只覆盖少量导航场景，未披露完整 hardware、precision、control frequency 与 safety SLO；因此它支持一种 experimental interface，而不证明 direct fusion 普遍失效。

### 完整新增与marker

动作条件也可由专门的运动表示分支产生，而不要求通用语言主干逐token写出推理：保留冻结generalist，另训domain expert，经声明的global/local attention mask交换条件，再让一次双向读取形成的运动hidden states条件化动作生成。[MoT-VLA的有限对照](https://arxiv.org/html/2510.18337v1)区分通用语义与运动适配，却不使mask成为语义独立证明，hidden可读或motion token分高也不认证物理动作有效。主实验两份模型的参数/前向、motion监督、动作去噪与真实controller都要计费，不能拿较小版本的局部时延代表14B主配。相异预训/示教预算和有限模拟/实机不授唯一mask收益或原语言能力全保；运动条件幻觉、任务退步或控制预算不足时，保留原VLM/action head、较窄运动适配与短chunk重观测，由独立controller决定执行，不让快的隐式推理取得物理安全权。

<!-- source-family:SF-2025-ARXIV-2510-18337 -->

### 完整后邻接

动作消费者也可以保留两份并行条件，而不把原始视觉语言状态全部压进一组queries：让每层action latent分别cross-attend相应层的Raw状态、以及可训练action queries与proprioception，再与action自身的self-attention拼接后继续更新。[VLA-Adapter的受限分支](https://arxiv.org/html/2509.09372v1#S3)仅在Raw支路乘零初始化的tanh系数，另一条件保持直接读取；这个系数可为负，不是可信度概率或最优条件认证，初始Raw贡献为零也不保证训练后保留原动作或语言行为。默认LoRA更新与冻结backbone只训练query/head应分开验收，同层身份、输入相机/标定、动作schema和训练权限须共同绑定。双条件在所测任务的平均更好，单层仍可在子任务反胜；全部层状态驻留、两路视觉读取、query/head训练和闭环回归均付费，chunk内多步吞吐不当每次新观测的控制频率。支持、质量或预算失配时，保留直接读取、query-only或完整原策略与独立低层controller，不由小backbone、无机器人预训练或learned gate批准物理安全。
<!-- source-family:SF-2025-ARXIV-2509-09372 -->

### 本人注

本人注：`SF-2025-ARXIV-2510-18337` — Locke，Daily2025-10-23补Oct22；exact-v1 §3.1–3.3/4.1–4.3采用相关段必要，2+1+2=5，冻结generalist/运动expert与单次hidden动作条件差额深入。保14B主配/1B时延不混、训练预算/非唯一mask因果、运动token非物理truth和双主干/动作/controller全费；未核实现/复现，不授原语言全保或安全。PRE/SAVE/全自读/sole actualPOST仅本日实际层。
