# 2025-10-04 第二批38精确v1题摘准入提案

作者Ptolemy。逐项实际读完整title/abstract/comments及可见history；原件均为本日supplement-20261011/abs-2510.<ID>v1.raw，对应request均200。精确v1不以API latest替代。下列为31P/2C/5N；N是具名普通决定工作，不是外部终态。P仅潜力，不是确认候选，不评分、不授Evidence/Books；submitted区间只发现，不证明Oct03公开。

首24及两U最小核心已另在[SUP_FIRST §3/4](SUP_FIRST_20261011.md)，其作者最终22P/2C可独立校准；OpenAI同事件4分/安全受影响深入/仅报告裁决已同步，不等待此批或14来源。两批62题摘无重叠，旧59有效AB按不变精确身份复用，不因新入口同ID全量重读。

## 1. 逐项提案

| 精确v1原件（2510.） | 判法 | 原约束→实际增量→需改变的选择/限制 |
| --- | --- | --- |
| [01328](supplement-20261011/abs-2510.01328v1.raw) | C | 使用既有score/energy diffusion学习complex Langevin物理分布，并探索该科学问题应用；题摘未提出通用模型训练/系统机制新边界，按AIforScience暂缓，不因quantum标签一概关闭同批表征理论 |
| [01329](supplement-20261011/abs-2510.01329v1.raw) | P | MASK丢中间语义→离散状态配对连续noisy latent作为每步hint→估计器/强度可调mode-cover与mode-seek取舍；不是所有生成任务保证 |
| [01335](supplement-20261011/abs-2510.01335v1.raw) | P | 旧ID benchmark可能过简→known-ID非平凡流形/曲率/噪声，同资源估计更差→表征维数的评价难度与估计条件需重看；QuIIEst是精确v1标题，不以新版HomID名称替代，quantum-inspired不等科学应用排除 |
| [01337](supplement-20261011/abs-2510.01337v1.raw) | P | video latent action未必可辨识→desiderata/不识别来源/entropy-regularized objective条件分析→动作表示离散化选择应绑定识别假设，不授任意video真实action |
| [01345](supplement-20261011/abs-2510.01345v1.raw) | P | SSRL stop-grad/predictor看似经验heuristic→同MI下SDMI交替与JMI联合优化结构约束→需分清目标决定的结构，非综述归类本身准入 |
| [01349](supplement-20261011/abs-2510.01349v1.raw) | P | 标签不变不保证变换分布重要→neural two-sample anisotropy及invariant ridge反例→augmentation/equivariance收益须看测试分布；April2025短workshop先稿触发具名同家族事件差额门，不能自动OLD或由accepted日期推公开 |
| [01350](supplement-20261011/abs-2510.01350v1.raw) | P | 非易失crossbar可泄漏训练权重→Keyed Permutor与Watermark Protection Columns→权重保密与ownership是不同目标/开销；与硬件安全直接相关，不需LLM实验标签，2页决定机制/威胁条件待局部补核，不采under10%为生产保证 |
| [01354](supplement-20261011/abs-2510.01354v1.raw) | P | 通用PI检测不证web-agent检测→显式/隐式文本、可见/不可见图像以及benign类别分开→detector漏检条件须评价；安全反側局部需核分母/检测口径，不读取攻击payload |
| [01375](supplement-20261011/abs-2510.01375v1.raw) | P | runtime RAG带持续依赖→fail-hints每episode一次teacher检索、student去hint蒸馏→runtime检索与训练内化取舍；两基准/模型范围，不把成功率或token宣称普遍化 |
| [01378](supplement-20261011/abs-2510.01378v1.raw) | P | universal score underfit解释太粗→选择性区域拟合与受测干预→生成泛化需区分哪里拟合/哪里不拟合；不是一般越欠拟合越好 |
| [01388](supplement-20261011/abs-2510.01388v1.raw) | P | VLM priors到robot action有接口差异→image diffusion生成path mask，再BC变可执行trajectory→视觉计划与控制分工/标注选择；不授通用collision安全或action-conditioned world model |
| [01399](supplement-20261011/abs-2510.01399v1.raw) | P | 单图realism未控制多脸身份重复/人数→intra-image/cross-sample/count/quality组合奖励及curriculum→多目标生成评价与优化对象需分开；精确v1 DisCo，不采用新版扩写或“annotation-free解决全部identity” |
| [01404](supplement-20261011/abs-2510.01404v1.raw) | P | task success不证kinematic constraint学好→数据大小/质量/曲率的约束manifold测量与硬件case→任务指标与动作约束分责；曲率相关性不确定不删反侧 |
| [01407](supplement-20261011/abs-2510.01407v1.raw) | P | neural codec卷积decode成本→latent低秩操作+VQ的重构接口→编码/解码计算与fidelity取舍；不是成熟低秩关键词本身，必要最小方法核具体是否替换decode；MLForSys2025 comments仅先稿身份门 |
| [01414](supplement-20261011/abs-2510.01414v1.raw) | P | spike/target alignment直觉不总成立→min-norm风险相变/对齐可害及非线性局部验证→泛化解释须绑定c=d/n与spike条件；理论直接主线，不按无LLM关键词关 |
| [01444](supplement-20261011/abs-2510.01444v1.raw) | P | RLVR视图确定输入忽略视觉不确定→raw/noisy policy对称KL bonus+entropy/schedule→input探索信号选择；联合改动不等纯KL因果，精确v1 VOGUE不替最新题名 |
| [01447](supplement-20261011/abs-2510.01447v1.raw) | P | DP-SGD统一硬裁剪损少数群梯度→tanh smooth变换并限sensitivity+adaptive机制→privacy/fairness梯度处理取舍；医疗/tabular仅测量场景，不是领域排除；不授未核统计/DP普遍保证 |
| [01454](supplement-20261011/abs-2510.01454v1.raw) | P | VLM选择不能稳定胜random→attention matrix/gradient联系、proxy top-SVD轨迹聚类均衡选样→数据选择与代理训练成本；数据削减百分比仅对应受测集，不泛化 |
| [01456](supplement-20261011/abs-2510.01456v1.raw) | P | diffusion OOD多forward昂贵→score Jacobian trace+norm/KDE阈值/Hutchinson JVP→检测成本质量取舍；robot复用限共享state/action空间，不授可靠性认证 |
| [01471](supplement-20261011/abs-2510.01471v1.raw) | P | LLM BO高维不确定估计昂贵→LoRA+variational Bayesian last-layer及递归ensemble更新→适配参数与uncertainty推断取舍；不是生物/工程目标指标准入，不授global optimality |
| [01472](supplement-20261011/abs-2510.01472v1.raw) | P | LLM架构探索偏特定latency段→partition search+prompt/architecture co-evolution及zero-cost proxy→搜索覆盖/硬件约束选择；精确v1 PEL-NAS，不用新版LLM-NAS替代 |
| [01478](supplement-20261011/abs-2510.01478v1.raw) | P | discrete/continuous生成分开→codebook categorical posterior与velocity及temperature的VFM桥接→表示路径与不确定控制取舍；不是VQ名词堆叠 |
| [01483](supplement-20261011/abs-2510.01483v1.raw) | N | temporal VLM chunks+持续object KG导航：需核实体跨chunk关联是否新增可核机制/条件，而非成熟VLM+KG只增robot榜单；只补method的association与直接比较，不读全导航附件 |
| [01513](supplement-20261011/abs-2510.01513v1.raw) | C | pretrained models多模型融合→temporal frame-indexed KG+互动学习框架；完整AB只提出既有组件编排/prototype示例，未指出可修正主线选择的新机制/成立条件，不因“KG/memory”自动P |
| [01523](supplement-20261011/abs-2510.01523v1.raw) | N | MetaSynthRAG top-ranked exemplars+evaluator/generator闭环，ecommerce CTR/NDCG不独立准入；需核implicit feedback如何实际改变检索/合成、是否仅成熟iterative refine，补最小method/对照 |
| [01531](supplement-20261011/abs-2510.01531v1.raw) | P | observation-only uncertainty漏内部dynamics信念→info actions验证内部动力学、uncertain-dynamics benchmark→主动信息与控制选择；74%摘要不等普遍或因果收益 |
| [01540](supplement-20261011/abs-2510.01540v1.raw) | P | pairwise偏好弱ranking一致性→diffusion listwise DPO/Plackett-Luce目标→排序监督对象取舍，不授所有指标或reward model稳定性 |
| [01545](supplement-20261011/abs-2510.01545v1.raw) | P | imitation horizon累积error→人工intervention与future bootstrap/覆盖假设→风险覆盖与标签准确度应分开；理论条件不换成真实安全保证，NeurIPS spotlight不是已证同稿公开 |
| [01546](supplement-20261011/abs-2510.01546v1.raw) | P | AR理解与生成token语义不一致→semantic/pixel VQ双对象及BridgeMo融合→表示/生成接口与序列膨胀取舍，不由模型名授统一优越 |
| [01549](supplement-20261011/abs-2510.01549v1.raw) | P | noise-space KL可能漏image drift/reward hacking→image-space score-based KL surrogate+test-time DPO→regularization度量对象；frozen backbone不等没有输出分布改变 |
| [01565](supplement-20261011/abs-2510.01565v1.raw) | P | fixed sequence-parallel degree难适配混resolution/deadline→step-level sequence parallelism及round-based联合packing→GPU时间/质量/SLO调度取舍；精确v1标题TetriServe，不套其他名称或后版扩写 |
| [01569](supplement-20261011/abs-2510.01569v1.raw) | N | inverse列出harms→consequences→safer response后SFT/RL：需核安全反側与训练构造是否改变选择，或仅成熟premortem prompt+榜单；补method与直接utility/safety对照，不读攻击实例 |
| [01578](supplement-20261011/abs-2510.01578v1.raw) | P | 固定clip/warmup忽略scale η∥g∥→per-layer stats power shaping梯度→训练稳定/步长控制取舍；MMAsia accepted只具名先稿门 |
| [01581](supplement-20261011/abs-2510.01581v1.raw) | P | 统一thinking budget过少/过多→attention steps压缩+task difficulty reward学budget→推理成本与难度代理取舍，不用当前后版顶替v1 |
| [01585](supplement-20261011/abs-2510.01585v1.raw) | N | ReSSFormer recurrence/sparse/position-free topology三个组件：需核content-based token topology具体对象/接口或失效条件，不因列“三创新”或单FLOPs数字自动P，也不因组合自动C；MMAsia先稿门与贡献分开 |
| [01586](supplement-20261011/abs-2510.01586v1.raw) | P | 静态安全数据难适应对手→adversarial coevolution+group-mean advantage baseline→内生安全训练取舍；“无added overhead”未核总训练预算不采用 |
| [01591](supplement-20261011/abs-2510.01591v1.raw) | P | text/logit verifier漏hidden变化→hidden-state delta成功/失败centroid非参数比较→verification对象与目标经验依赖；maj64/maj16不同预算不当同成本因果 |
| [01598](supplement-20261011/abs-2510.01598v1.raw) | N | physical RNG与GAN训练/大型模型安全关联：需核具体随机源、PRNG baseline质量/复现、18.6x估计对象；bad PRNG不能代表全部PRNG，不把物理随机性名词授LLM效果。只补比较/威胁条件，非整硬件复现 |

## 2. 日期与停止

以上38完整精确v1AB作者已读足；明确P实验可信度待核不因此关，5N需要决定事实尚未读是普通工作。01350/01407及首24安全/反侧的必要局部将独立记录实际章节，不预称已核。

01349的April2025短版需具体旧官方公开身份/共同核心和本v1事件差额；其他accepted/workshop只做具名有限事件门，不全会议/全年扫描。日期查询尚有本日可执行Advanced公告入口/相关原始公开列表检查，不在此预签耗尽或终态。所有P不因submitted Oct01/02落窗、不因旧Books主题或作者read完成直接正式化。

## 3. 实际局部决定核心（2026-10-11，覆盖上段暂判）

以下只为决定准入/保留直接反側，不等正式Evidence或完整论文复核。

- 01350：HTML404保留；[精确v1 PDF](supplement-20261011/pdf-2510.01350v1.raw)两页完整实际读。§II秘密key行映射/triplet swaps与独立不存neural weight的watermark两列；key必须安全保存/轮换。§III明确权重并未训练，只为结构/PPA仿真预定义；§IV 45nm 256×128的current下降8.8%、delay+5.5%、power+9.8%、transistor+2.34%，current不是area或精度。保留窄P：保护/ownership接口与资源取舍有直接主线意义；无攻破实验/安全证明，不能由keyspace或“under10%”称抗提取已经成立、trained RF/MNIST模型精度已核或生产可用。未渲染图取值，仅使用正文给定数字，图像视觉未核。
- 01407：[v1 HTML](supplement-20261011/core-2510.01407v1.raw)完整§3/4实际读。codebook生成低秩矩阵因子并迭代/分patch重构，不是只给既有decoder再加低秩层；不实际执行SVD。可选smoothing convolution仍是主要剩余decode成本，rank/iteration/patch增加bpp；§4是MNIST/CIFAR10/CelebA64、MSE/bpp/MACs，encoder也从CNN变ViT，非同质量同压缩率因果对照。P保留具体decode接口/取舍，不称全端到端成本、卷积彻底消失或任意图像fidelity保持；重构求和平均/index表述亦不照录为已核实现。
- 01399：[v1 HTML](supplement-20261011/core-2510.01399v1.raw)完整§3.2/3.3及§4.3实际读。RetinaFace阈值0.7/ArcFace身份代理；group reward是remove-one对平均相似度影响的sigmoid，不等一般多样性真值。intra/group奖励会少生人数/产生grid，因此加入count/HPS；Krea消融group加入使count 66.2→67.3但仍低于baseline73.6，之后count加入恢复81.1而GIS72.5→68.3，非各指标单调；curriculum主对specialist更有用。P是优化对象/作弊边界与specialist条件，非成熟GRPO名称或98.6单数字，不授真实身份或全部构图已解决。
- 01483：[v1 HTML](supplement-20261011/core-2510.01483v1.raw)实际完整IV-B、VI-D/E及TableIV。跨chunk仅LLM比较text description得[0,1] similarity后threshold，b=8按此benchmark调参；所谓语义vs视觉/no-association消融引用TableIV，表实际列Full KG/retrieval/chunk-wise retrieval而非这三association对照。改C：已读决定方法仍是成熟prompt/阈值关联与KG导航应用，未新增可核通用association机制或明确修正条件。表引错不单独等“无贡献”，也不采用其association胜视觉的主张；日级公开未核，不为此C索取日期。
- 01523：[v1 HTML](supplement-20261011/core-2510.01523v1.raw)完整§3、4.4/4.5实际读。offline top-ranked exemplar、cosine/ANN、MMR、query expand与generator-evaluator按品牌rubric迭代；未披露部署CTR反向训练/动态校准新机制，toprank只是弱监督模板。消融去RAG/去evaluation是在电商领域排名，未指出新的通用可靠性条件。改C为成熟组件领域组合，不是电商领域本身排除。4.5文字clicks/CTR与Table3方向交换、AB亦不同，不采用提升宣传或成本已相抵；不把一个数字冲突自动变模型设计贡献。
- 01569：[v1 HTML](supplement-20261011/core-2510.01569v1.raw)完整§3与5.2实际读，未读危险实例/附录攻击提示。改窄P：teacher结构化harms/consequences/mitigation→SFT/RL训练，并有推理路线数/model scale非单调条件（小模型收益极少、大模型过多路线下降）以及Table3安全/一般推理不同目标。不是premortem名字本身；拟“superlinear/phase transition”只是作者解释，未授规模定律、法律/医疗/金融安全保证。Eq7对reference ratio/clip advantage不等标准GRPO定义，不照录；reward moderation API、能力保持与训练预算受限，不授无safety tax普遍性。
- 01585：[v1 HTML](supplement-20261011/core-2510.01585v1.raw)完整§3与4.6实际读。改窄P：Eq7内容驱动token graph+Eq8跨迭代edge变化正则及recurrent memory/sparse routing接口，非仅列三模块；去SOES消融有局部性能差别但未证任意content-only结构可恢复原序列顺序。成熟sparsemax/top-k/MoE各不作为新算法；选key本身成本/学习order识别与完整部署收益未证，Table3 Relative Change口径不照录，MMAsia先稿门另保留。
- 01598：HTML404；首次PDF虽HTTP200但curl exit28，pypdf报Cannot find Root，未称正文已读。正在单次具名PDF恢复；仍N普通决定项，需要低质量PRNG baseline/“insecure”定义而非整个硬件复现。

第二批当前33P/4C/1N（原38不重加计数），等待root actual准入校准；N01598未完不预授终态。01335完整AB已足以说明known-ID同资源评价反側，不因量子标签另扩全文。其他明确P的可信度不能用追加全文义务倒退为N。

## 4. 01598具名恢复与N关闭

第二次本地PDF仍curl exit28且不可解析，未伪称成功下载；不重复同路径。改用web读取[原官方精确v1 PDF](https://arxiv.org/pdf/2510.01598v1)，实际读§2.2～2.4、§3及§4 system段（pp4～10），未审附录。原两次不完整响应与requests保留。

改窄P：16-MTJ+FPGA的raw entropy受漂移/相关污染，XOR/Toeplitz处理后输入GAN；IS遗漏类内重复而LPIPS可见差异。18.6x只class6相对raw-MTJ，不是对所有PRNG或LLM；“insecure”是LPIPS<0.3相似对计数，不是实际攻击。LFSR基线低质，未控现代CSPRNG；NIST通过不等应用安全，gigabit扩展是估计非16-cell实测。不采确定性必导致黑盒攻击/安全保证。具体输入随机源质量与模型评价对象边界可保留，成熟hash或器件标签不独立准入。

第二批最终34P/4C、N0；只是作者贡献校准提案，待root，日级公开/必要先稿门仍未证，不评分或授Evidence。前段33P/4C/1N为过程，不能作为当前未读外部阻塞。

## 5. 已收到的独核与具名安全局部

root独核§5实际完成第二38全AB及所列必要core，34P/4C通过；01598另live官方v1 pp4～10实际独读，作者复用不再整PDF恢复。通过只准入潜力层，不授Oct03公开/Evidence/Books。

作者另实际读两个安全相关必要局部，不改变P：

- 01549 [MIRA v1](supplement-20261011/core-2510.01549v1.raw)完整§4/§5.1/§6：输出image分布约束替代noise-space约束，KL本身intractable，Eq4/Algorithm1用score-norm difference做代理；45prompt/900base-image CMMD与brightness/darkness只是局部漂移/目标失真，不是人类安全真值。作者允许代理估计小负数、承认tightness未正式分析/复杂OOD可退化；不把surrogate当精确KL，不外推sampler-portable即可全sampler有效。未读附录推导/算法证明、未视觉判断生成图，完整证明仍不授。
- 01586 [AdvEvo-MARL v1](supplement-20261011/core-2510.01586v1.raw)完整§4/§5.3：分离agent backbones与role组内均值baseline；global最终benign可能掩盖localunsafe，双层reward对象为具体失效边界。组baseline包括自身return，未在本段证明unbiased，不能套标准action-independent baseline保证。安全/utility权重训练半程翻转，dynamic attacker与isolated/joint comparisons可能预算/过程混杂；diversity与robustness共变不是因果证明，不采“collaborative行为只由joint training产生”或未见attack泛化已证。只读方法和上述反側，不扩attackpayload附件。
