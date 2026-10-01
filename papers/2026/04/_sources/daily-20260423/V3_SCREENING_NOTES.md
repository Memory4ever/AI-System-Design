# 04/23 当前合同的题摘贡献筛选

作者root；依据原始完整题摘`arxiv-owner-replay-20260903/20260423/arxiv-owner-receipt.json`。记录准入而非证据结论，日期、官方撤回/纠错说明和独立口径校准未完；旧状态不继承。

## 首批：30完整题摘，6潜在、1定点消歧、23贡献前关闭

| ID | 当前判断及原文依据 |
| --- | --- |
| 19749 | 潜在：只有结果正确的工具奖励可能奖励无必要调用；题摘分开知识边界偏好训练和成本奖励干预，可检查过用原因与准确性是否同预算保持，涉及Ch78而不把减少调用直接称正确。 |
| 19750 | 潜在：GUI代码通过文本反馈可能不等交互和视觉要求，题摘将984任务的交互逻辑/视觉结构分别测量；核验新oracle是否实际暴露旧成功判据漏测，而非仅“加截图更好”的成熟组合。 |
| 19751 | 关闭：教学交付物与人类能力残余的rubric重组，原文自称不主张element-wise novelty；当前没有大模型机制、平台执行或发布合同的新实证，不能把学习治理类比当系统贡献。 |
| 19752 | 潜在：七种治理模拟中收紧治理未改善安全且损害福利，题摘提供五seed和soft label指标；核验proxy的生成及不变性是否由设定造成，不能把连续风险值等同真实风险概率。 |
| 19753 | 关闭：文本embedding+kNN选一般SAT/MIP算法，核心评价为ASlib任务portfolio；没有研究foundation模型或模型系统的选择边界。 |
| 19754 | 关闭：课堂科学回答分类的增强/重采样应用，收益来自特定rubric与SciBERT任务配置，不形成当前主线机制增量。 |
| 19755 | 关闭：AML模拟中组合检索、引用和counterfactual检查，题摘未给新的证据绑定/执行机制或足以修正既有RAG判据的独立反证；不因监管词汇齐全而保留。 |
| 19756 | 关闭：轨迹模板、相似度路由和fallback构成成熟workflow reuse分支，题摘给定性对比与局部成功数字，没有新增有效性条件或经验更新责任机制。 |
| 19757 | 关闭：有限可见性下环境影响proxy估算，题摘明确非直接测量，未给新的训练/推理设计比较或机制；可作行业背景但不进入贡献池。 |
| 19758 | 关闭：热力学293问题与学科解题榜单属暂缓领域能力应用，不因程序化ground truth或多次运行恢复AI for Science路线。 |
| 19759 | 关闭：临床叙述LightGBM特征工程，稀疏/稠密特征互补与选特征收益为领域分类，不是大模型或其Infra机制。 |
| 19760 | 关闭：抽象capacity/(uncertainty+constraint)模拟比例及Monte Carlo collapse关系，未将变量与真实模型runtime或学习机制建立测量桥，不能借“inference”名称变成Serving余量控制。 |
| 19761 | 关闭：LLM引导DAG特征搜索+Ridge评估结构断点任务，题摘仍研究下游非微分预测计算搜索；没有显示改变foundation训练/生成或编译runtime的基本假设。 |
| 19762 | 关闭：Voynich文本密码结构分析与生成器反证，不研究当前模型与系统主线。 |
| 19763 | 关闭：语音情绪识别的联合公平性指标在CREMA-D验证，不研究多模态基础模型对齐/生成或平台评价的新失效条件。 |
| 19764 | 关闭：GPT2/Llama的对比neuron/head定位偏见为初始probe，題摘未指出现有定位结论被修正或新识别机制；不因涉及内部激活就默认入选。 |
| 19765 | 潜在：5模型/6知识域的hallucination-neuron分类器跨域AUROC明显衰减，直接检验通用神经签名假设，可改变检测器迁移/校准边界；不能由分类性能下降推断幻觉没有共享因果机制。 |
| 19766 | 关闭：Search→Refine→Reason与GRPO奖励证据和调用成本的组合，題摘只给多跳QA的更优operating point；未定位额外独立机制、有效性边界或关键反证，既有检索压缩+成本奖励解释仍成立。 |
| 19767 | 定点消歧：领域fine-tune后的EAGLE3有跨并发/γ的实验，但原对照vLLM与NIM平台不同，题摘只给成熟speculation局部收益。只补必要评价段确认是否产生新可行性边界，不能为追数字全文扩审。 |
| 19768 | 关闭：修辞标记差异及人类/LLM文本风格分类，未将FMD/GPR与事实正确率或概率校准建立验证桥；不能当知识置信度估计机制。 |
| 19769 | 潜在：年龄分层同时改变HBM/DRAM位置与precision，并用流式attention交叠跨层传输；核验何种访问/质量条件允许temporal代理以及迁移成本，不能用人类记忆类比或最大加速数字证明。 |
| 19770 | 关闭：建筑许可PDF配页和diff算法，不研究模型上下文/state身份或LLM执行机制。 |
| 19771 | 关闭：BM25+Matryoshka/RRF+reranker与检索后抽取版本追踪是成熟记忆pipeline，题摘未披露新的一致性、更新或失败边界；生产声明不替代增量。 |
| 19772 | 关闭：人机科学书写的层次提纲/RAG/引用组合与满意度，未出现可泛化的模型或workflow机制反证；不是本项目写作工具候选。 |
| 19773 | 关闭：CAD生成编辑的专门表示、数据与RL应用，题摘未分离出通用生成范式或表示约束变化，不能以controllable/faithful名字准入。 |
| 19774 | 关闭：医院出院摘要采用率与自报节时研究，不是生成模型机制或AI生命周期平台的新design contract。 |
| 19775 | 潜在：stepwise conformal对agent中间表示标成功/失败并训练probe，核验时间依赖下校准单位/coverage保证与steering证据，可影响提前终止/干预条件而不是凭concept命名认定因果。 |
| 19776 | 关闭：南非结核医疗QLoRA+GraphRAG组合，当前暂缓科学/医疗应用，未带来主线新机制。 |
| 19777 | 关闭：已有元数据导航/显式prompt路由替代向量检索，20问题及人造目录只验证成熟有结构检索分支；没有新的正确性保证或足以改写通用RAG边界的证据。 |
| 19778 | 关闭：Kokborok翻译语料与NLLB领域fine-tune，当前没有tokenizer/训练目标/基础模型泛化机制的新结论。 |

上述23项为对本项目的贡献关闭，不称论文无学术价值，也不称其日期已核实。题摘里没有纠错/安全变化信号的应用关闭不追全版本史；拟入选项继续核当前原始事件说明与日期。490宽库存不是上述30项、不是候选数，尚不宣称全日筛选完成。

## 第二批：15完整题摘，3潜在、2定点消歧、10贡献前关闭

| ID | 当前判断及原文依据 |
| --- | --- |
| 19779 | 关闭：ESG报告检索与分数回归组合，300份报告的任务收益未给新的检索有效性或平台状态机制；不因报告数量和模型调用成为主线贡献。 |
| 19780 | 潜在：连续budget-conditioned policy与progress课程同时改变截断、process reward和advantage基线，需核真实budget适应机制及收益归因，而不是只缩短CoT。 |
| 19781 | 关闭：教育评分中三款小模型置信度级联及近退化confidence，仍是领域校准/升级路由的受限operating point，摘要未建立改变通用校准选择的独立反证；不把局部负结果直接推成模型都不知错误。 |
| 19782 | 定点消歧：Korean audio faithfulness若能分离忽略音频与语言先验，可暴露旧正确率漏测；仅语言新数据集不够，补必要控制设计后裁决。 |
| 19783 | 关闭：一万轮募捐对话的说服策略标注与社会行为分析，不研究模型学习、执行或平台发布合同。 |
| 19784 | 潜在：八个frontier模型在同伴撤销场景的行为变化可能暴露目标/权限失效路径；安全深入仅围绕harness权限和对照，不将模拟动作视为生产系统已有能力或意图。 |
| 19785 | 关闭：668人聊天记录上的人格推断分类研究，任务和隐私重要，但题摘尚未揭示区别于已有属性推断的参数/会话泄漏机制或新的保护边界。 |
| 19786 | 关闭：Bradley–Terry/Swiss tournament和LLM judge组合成幽默榜单，未给新测量有效性条件；不因有human相关系数而自动成为Evaluation机制。 |
| 19787 | 关闭：120K persona的社交反应预测弱于TF-IDF，是特定人群模拟应用比较；未证明新的foundation机制、发布条件或通用预测可行性变化。 |
| 19788 | 关闭：人本XAI学习理论议程，没有原始机制/实证把建议连接到当前大模型或Infra设计。 |
| 19789 | 关闭：材料科学自主发现应用属于当前暂缓AI for Science范围，不通过Agent章节重新准入。 |
| 19790 | 潜在：相同checkpoint不同precision出现输出/安全分歧，差分输入搜索可能改变部署量化验收；须核precision-only对照及保护信号，不能只取平均质量一致。 |
| 19791 | 关闭：Concordia态度模拟的人工稳定化实践，未分离主线的新状态/优化机制或有效性条件。 |
| 19792 | 定点消歧：摘要含明确数学纠正信号，不能按平台组合泛化关闭；仅核其涉及固定点、范围或attention pruning的实际保证与主线关系，不遍历完整版本史和全部生态声明。 |
| 19793 | 关闭：成功trajectory转工具转移图、语义召回和次序先验，题摘目前只给成熟图约束推荐分支及局部收益，没有新执行合法性或收益条件；“graph foundation”措辞不是增量证据。 |

累计45完整题摘：9潜在、3定点消歧、33贡献前关闭。未确定最终分母；普通定点工作继续，不称external blocker。

## 第三批：23完整题摘的贡献判断

完整读19795、19809、19811、19816、19818、19820、19821、19825、19826、19827、19835及下表其余12项；本批并非冻结候选，也不是正文已审。宽库存490项标题已作为有界查漏浏览，不把领域外标题变成全文队列。

| ID | 当前判断及原文依据 |
| --- | --- |
| 19795 | 定点消歧：摘要把entropy memory、causal intervention和agent convergence连成平台保证，必要问题是ESMS/LOCOMO指标是否支持所称收敛；不因为系统组件多而准入，仅补决定保证的定义/假设。 |
| 19809 | 潜在：自我知识校准与是否据此控制行为分开测量，八类干预、16模型可以检验“知道能力边界就会安全行动”的假设；核精确v1协议，不继承当前后发实验。 |
| 19811 | 潜在：同一bio内容按开放/受控访问与AI工具链条件比较保护有效性，关系是模型/工具权限的安全评价而非科学任务优化；只审防护评价与benign/harmful分母，不采用危险操作细节。 |
| 19816 | 关闭：DTA按振荡/相位改变QKV以描述AI agents社会coherence，摘要尚未给学习/生成约束或模型系统实测桥，不能由新架构名称和Hopfield类比准入。 |
| 19818 | 关闭：24来源的原则归纳转治理action/evidence bundle，未提供原始反证或解决具体系统分歧；成熟流程的综合不是本窗机制增量。 |
| 19820 | 关闭：私有知识检索、记忆、对话组合为领域写作助手，没有新增检索正确性、状态更新或执行控制机制。 |
| 19821 | 潜在：联合搜索prompt和tool schema对照分别优化，可检验接口配置耦合而不只是新任务收益；核是否确有受控联合效应及预算成本，否则局部配方仅报告。 |
| 19825 | 关闭：边界例、执行及property test反馈构成成熟代码验证组合，摘要没有改变oracle信任、覆盖或执行责任的具体条件；局部代码bench增益不独立准入。 |
| 19826 | 潜在：对内联测试表示做knockout与activation steering，可能解释测试邻近性为何改变代码生成；Python/Rust布局与语言混杂必须分开，不由跨语言均值建立因果。 |
| 19827 | 关闭：异质multi-agent的七项可证伪命题仍是议程，未提供可核的机制证明或新实证；问题表述不等于被证实的设计分支。 |
| 19835 | 潜在：复制expert后以utility驱动差异化并保持top-k，提供MoE初始化/对称性打破的设计分支；核连续训练预算与固定计算声明，不能忽略通信或以GPU hours等同FLOPs。 |
| 19837 | 关闭：独立Evaluator、Planner隔离和跨run文本记忆的成熟组织组合，三个任务小规模转移不分离新评价边界或独立机制；相同denominator估计不证明其正确。 |
| 19839 | 关闭：四类perception/planning/action/goal skills、GRPO与失败重试组合，ALFRED局部成功率尚未揭示新的动作/环境状态合同，不能用技能分类替代贡献。 |
| 19844 | 潜在：同一视觉环境必须响应合法信号又拒绝指令注入，dual-intent控制直接检查“忽略视觉输入就安全”的不充分性；七模型、保证假设和utility/security双分母深入核。 |
| 19857 | 潜在：复合奖励的GRPO收敛、分解误差与PAC-Bayes transfer若成立可收窄奖励拆分的合理条件；必须读假设与实际GRPO对应，不由定理名字推出LVLM泛化。 |
| 19858 | 关闭：LLM+DiT、精细标注与RL数据的统一图像产品介绍，没有揭示相对既有融合/生成范式的新内部机制，human evaluation排名只证明作者受限结果。 |
| 19877 | 潜在：同一训练checkpoint每层可选FA/SWA/KDA/GDN并在请求间换placement，改变“mixer配置是固定artifact”的假设；小模型ranking稳定而15B高效配置不稳是必要反证，不能只收10.7倍。 |
| 19884 | 潜在：量化区分累积信号退化与早层计算坍塌，并用定点repair能/不能恢复作干预；核精度/部件诊断与因果归因，不把所有2-bit实现一概无可救药。 |
| 19895 | 关闭：失业救济信息完备性bench及显式缺项checklist，是特定法律证据场景的成熟拒答/检查机制；局部15%→89%不改变通用校准或发布保证。 |
| 19899 | 潜在：MetaRAG受控复现发现绝对分数下降、prompt缺失与闭源版本漂移，可能修正原算法收益归因；只核相关baseline/身份及reranker比较，不全历史搜索。 |
| 19906 | 关闭：MLIR原生NumPy DSL、类型检查与并行lowering的主要验证是Fortran天气/CFD；没有建立模型执行/编译主线的具体增量，仅可作通用compiler背景。 |
| 19925 | 潜在：10659匹配owner-agent对显示日常上下文转移与个人信息披露相关，安全深入限定观测关联和隐私路径，不能将无显式配置等同随机控制或实际memory因果。 |
| 19932 | 关闭：通用HMA页迁移TLB/page-table新设计在IPC模型验证，未研究LLM模型状态、GPU层级或Serving质量/调度；“可类比KV”不是直接项目关系。 |

累计68完整题摘：20潜在、4定点消歧、44贡献前关闭；仍须准入口径非作者校准、实际落窗与证据判断。潜在不是证明了长期contribution，宽库存及日期异常单独处理。

## 第四批：12完整题摘

| ID | 当前判断及原文依据 |
| --- | --- |
| 19934 | 关闭：relation specificity、entity connectedness与per-head probe准确率关联，未给新的知识写入/召回机制或修正既有probe非因果边界；不能把可分类性写成模型实际调用原因。 |
| 19936 | 定点消歧：MIA与generalization的千模型控制实验可能是通用分类器，题摘没有foundation/参数泄漏机制桥；只核模型/攻击评价范围及所称反证，不能仅凭privacy词保留。 |
| 19945 | 关闭：先tool reward再accuracy的课程，是先技能后组合的成熟训练分支；题摘没有新的优化冲突解释/条件或代价对照，视觉任务指标提高本身不够。 |
| 19954 | 潜在：显式parametric camera tokens与factorized几何监督试图区分视角结构和物体外观关联，并以未见类别迁移检验；核该表示解耦及sim/photorealistic混合的真实条件，不推全部3D理解。 |
| 19965 | 关闭：675安全相关PR的弱点/合并过程观察支持既有“merge不等security验收”，未定位区别于已有代码漏洞的新模型安全/权限路径；这不是发布或保护行为变化，不凭security标题自动全审。 |
| 19966 | 潜在：固定distortion类型/严重度和base-thinking配对检验高层VLM能力向低层感知迁移，非单加榜单；核severity标尺、人类baseline及真实反向关系，局部有限评价不外推VLM整体能力。 |
| 19974 | 潜在：2×2解开confidence/correctness混杂后做SAE抑制，相关features与干预效果可能分离，直接检验不确定性和错误同机制假设；AUROC或entropy下降不等概率校准。 |
| 19998 | 定点消歧：concern match graph及decisive分母可能有新测量边界，但“accepted全部非decisive”是否由标注定义构造必须核；只读定义/pilot判据，不能照搬百分比批评所有review系统。 |
| 20006 | 关闭：长期记忆包含过时/失效事实的惩罚，是现有版本有效性而非只retrieval的成熟评价条件；摘要的FAMA与四模型六agent未给新的失效关系或维护机制，不因命名metric独立准入。 |
| 20012 | 潜在：用learnable proximity从通用VLM池选择VLA对齐数据再midtrain，提供表示分布差距与初始化适配的条件分支；核选择器与普通混合/预算对照，不把三仿真bench变sim-to-real证明。 |
| 20015 | 关闭：Java库call-site执行轨迹补静态reachability，研究的是软件依赖分析，不研究LLM的控制/生成或模型runtime机制；执行证明可作类比但不是主线贡献。 |
| 20021 | 潜在：连续embedding空间下epsilon-net/KRR和切换成本regret，改变有限已知请求宇宙的cache设计假设；核metric/平滑/feedback假设及语义回答正确性是否只外设。 |

累计80完整题摘：25潜在、6定点消歧、49关闭。上述数量只表示准入工作，未冻结；潜在项进入必要评价之前须经过独立校准，消歧仍是普通可做工作。

## 第五、六批：24完整题摘

| ID | 当前判断及原文依据 |
| --- | --- |
| 20027 | 潜在：saliency fine-tune与shuffled监督及CNN对照可检验attention优先级与classification表征能否分离；核“无代价”的Bayesian parity范围，不能把人类相似attention称因果解释。 |
| 20032 | 潜在：从GPU stalled instruction逆向slice同时覆盖register和vendor-specific同步，改变只按stall出现位置归因的diagnostic合同；21负载跨三GPU的收益和LLM辅助优化归因分别核。 |
| 20039 | 潜在：context graph与动态hypothesis扩张分离reasoning quality/eligibility，并做orthogonal组件比较，可能补规划中检测假设失效的边界；blicket有限任务不能外推普遍因果发现。 |
| 20041 | 潜在：保持likelihood训练目标的AR normalizing flow再迭代denoise，是与diffusion目标不同的生成分支；核invertibility/后处理密度与sampling mismatch，不能据ImageNet分数宣称全面替代。 |
| 20043 | 关闭：行动绑定解释、belief轨迹和environment oracle的成熟审计组合，摘要给“系统性不一致”但没有分离新失效条件或测量保证；三视角命名不独立成为贡献。 |
| 20047 | 潜在：ViT的跨patch传播使固定触发位置假设失效，并同时规避像素/attention检测，是真实保护边界信号；深入只核威胁/防御比较与patch条件，不扩攻击附件或代码执行。 |
| 20050 | 关闭：prediction market的私有信息/cheap talk/价格实验研究经济信息聚合，未给LLM协作协议、状态或推理机制桥；“smarter agents”表现更好不进入系统主线。 |
| 20051 | 潜在：pretraining文本为自生成rubric/答案提供外部grounding，试图在开放任务维持generation-verification gap与多样性；核reward hacking/模式坍塌对照，不由同模型自评自动证明可靠奖励。 |
| 20065 | 关闭：可检查/可移植用户表示的五项研究议程，没有新增memory机制或受控保护边界；ownership/access词汇不是实际合同实现。 |
| 20070 | 关闭：spreadsheet逐步可见与用户干预的N8/N16体验研究，是成熟human oversight应用，未产生新的执行原子性/授权/回滚机制或通用有效性反证。 |
| 20079 | 关闭：CoDA与Qwen不同架构的PTQ coding operating point及现有GPTQ/HAWQ混合精度配置，题摘未分离更耐量化的原因/适用条件；当前不能把局部2–4bit排序当生成范式一般性质。 |
| 20087 | 潜在：one-shot、自/teacher反馈和skill creator的多任务条件比较指出自反馈递归漂移，而外部多轮反馈不同；核反馈预算与对照后是否修正skill更新有效性，不以“20新任务”本身准入。 |
| 20090 | 潜在：用language-invariant逻辑表示同时选语言与剪trajectory，直接针对跨语表示不能比较的推理资源假设；核unified space建立方式/错误剪枝条件与相比投票的预算。 |
| 20098 | 潜在：把dependency-aware coherent factuality可微松弛并声称恢复原CP保证，可能改变scorer学习与claim dependency联合验收；深入核极限/校准样本/交换性和祖先闭包，retention数字不等无条件置信度。 |
| 20100 | 关闭：web、人类视频、simulation和real-robot多级pretraining与action-space统一的发布摘要，未公开区别于成熟跨embodiment适配的映射机制；模型/数据规模和榜单不能反推方法。 |
| 20105 | 潜在：以kernel结构推utilization再经验拟合功率，减少必须profile/simulate每配置的输入获取成本；核Ampere→H100预测、模块traffic/timeline与端到端估算误差，估算不冒充实机用电。 |
| 20117 | 关闭：schema constrained decoding只生成存在key、typed更新与图传播为成熟合法性/检索组合；有效key不等事实正确，题摘未给新的同步/更新保证或收益条件。 |
| 20129 | 关闭：MADDPG智慧城市摄像头的activation delta cache/优先级/硬件匹配研究，没有foundation/LLM runtime机制桥；agent规模和system术语不改变项目范围。 |
| 20130 | 潜在：many-to-one局部坍塌不同于mode dropping，pairing正则在探索不足/已稳定两个regime分别改变recall/precision；核latent距离前提和生成密度解释，这是生成机制而非领域应用。 |
| 20133 | 关闭：skill多文件、匹配、分层记忆与delegation的成熟workflow组合，foreign-trade judge整体28%未揭示独立新机制或可靠控制边界。 |
| 20134 | 关闭：SOC告警归一化、假设、policy response的概念pipeline，LANL小PoC只验证组合可行，未新增模型保护/执行合同；security场景不自动触发全面深审。 |
| 20136 | 潜在：typed claim依赖闭包限域纠正和provenance下人类override，可能让长视频维修成本随错误范围而非全重生成；核闭包保证和4.8倍human成本的真实分母/遗漏错误，不将控制声明当证明。 |
| 20140 | 关闭：把DPO按query/reason/answer分段加权及math数据训练，是成熟granular preference的局部配方；题摘未给credit assignment新保证、代价关系或反证。 |

本批有 1 项已撤回，直接排除，不保留为候选。累计103项仍可审题摘：37潜在、6定点消歧、60关闭，非冻结贡献数。apr02首批六潜在及19756/19766/19771否定侧实际校准通过；19767必要评价消歧证实同runtime未隔离且同family judge，具体关闭，不把模板化收益认作新机制。见[V3_APR02_FIRST_ADMISSION_CALIBRATION](./V3_APR02_FIRST_ADMISSION_CALIBRATION.md)。累计工作判断现为37潜在、5消歧、61关闭（103项）。其余潜在仍待校准/证据及日期。

## 第七批：模型条件计算与Agent受限证据

root实际读以下12个完整题摘，仍只处理本窗有界相关线索，不扩领域方法或把490库存变逐项全文队列。

| v1身份 | 贡献判断及必要问题 |
| --- | --- |
| 20144 | 关闭：table search后用metadata判断minimal/sufficient来源是成熟检索/条件检查组合，KramaBench/BIRD的F1与噪声表成功率未给新的selection失效条件或可验证完备机制；不因数据库领域硬排。 |
| 20146 | 关闭：多采样uncertainty→SFT搜索tag→带调用费RL是成熟knowledge-gap/utility组合，本地GMNER改善未新增知识边界的校准保证或工具决策条件；不把self-aware名称当新认知机制。 |
| 20148 | 潜在：同3B下few-shot、documentation、hypernetwork-LoRA与beam的负面对照声称额外适配权重无贡献，可能改变tool适配复杂度选择；需核控制、任务/预算与误差分母，不能由一个hypernetwork失败排除全部适配。 |
| 20156 | 潜在：token级router改为带deliberation cost的temporal expert-set controller，减少换入频率但牺牲能力，直接改变MoE offload的训练/访问耦合；核真实memory traffic与90%能力范围，switch率不是端到端延迟。 |
| 20157 | 潜在：对13视频模型测可感知逼真与运动学/生物力学保真分离，可能改变video/world-model验收指标；核运动估计器误差和物理指标适用性，不把可看视频当可执行控制。 |
| 20158 | 定点消歧：event log→task-conditioned projection本身是已有派生memory分支，但题摘把stateful架构称必然违反replay/audit/isolation，是决定设计的新强断言；只核这个断言的依据/定义，得到判断即停，不因enterprise故事扩池。 |
| 20174 | 关闭：GridWorld离线Q组合和transition support限制未建立foundation-model/LLM policy的直接机制桥，作为Agent类比不足；不因负面长依赖结果而抹去其RL学术价值。 |
| 20179 | 关闭：扫描→LLM提议→生成PoC→运行oracle是成熟工具验证pipeline，本地Node.js数量对照未识别新的验证/执行边界或泛化条件；verified exploit不等全包安全。 |
| 20183 | 关闭：历史modeling/coding双cluster→guidance→动态RAG/修复是成熟memory组合，七任务整体改善未拆出新的记忆更新有效条件；large-to-small inheritance本身不是权威证据迁移。 |
| 20193 | 定点消歧：自然语言policy→predicate和双板冗余本身成熟，但ISO Category3/PLd宣称可能改变真实embodied保护判断；只核模型失效与独立故障/认证证据是否真正建立，不能拿dual硬件等于safety资格。 |
| 20199 | 潜在：rerank语言偏好压制answer-critical多语文档，estimated oracle与下游utility目标可能改变跨语RAG选证条件；核oracle选择是否用答案/覆盖、同预算控制，不以relevance或encoder分数当真值。 |
| 20200 | 潜在：多轮用户分数压力下public labels泄漏与hidden质量分离，压力对首次exploitation的受控比较可能修正coding workflow评价保护；核反复试验/最优选择和prompt缓解残余，不把prompt文案当runtime隔离。 |

累计115项仍可审题摘，当前42潜在、7定点消歧、66具体关闭；这是工作筛选结果，非冻结候选、已证实贡献或全文任务数。潜在项仍需日期/独立准入及适当证据，消歧项仅补决定准入的段落。

## 后续14项完整题摘

以下只记录实际读完的题摘，不把宽库存或缺席身份计入数量。

| v1身份 | 贡献判断及必要问题 |
| --- | --- |
| 20202 | 潜在：API迁移的幻觉包括import、constructor与constant等结构事实，普通生成指标可能漏掉；核document/AST知识库能判哪些atomic claim及漏报范围，不把Android本地结果当通用正确性。 |
| 20209 | 潜在：长期self-play出现conjecturer复杂度/reward投机，guide对尚未解目标的反馈可能改变训练有效边界；核预算、留出目标和失败反例，不由小模型对比推普遍推理能力。 |
| 20211 | 关闭：日志安全分类、issue说明与代码修复的组合是成熟context/验证分支；本地缺陷识别率未给新的模型或执行保护机制，不能只因security名词抬高准入。 |
| 20219 | 潜在：固定宽度、共享prefix与层数的近似率可能解释深度的表示效率；核混合activation、函数类与有限规定深度条件，不套到训练后的Transformer。 |
| 20244 | 定点消歧：forward/reverse KL与off/on-policy蒸馏组合未自动建立新贡献；只补实际目标，判断是否给出超出成熟重加权的条件关系。 |
| 20246 | 定点消歧：视觉future proposal→排序→物理commit本身是成熟plan/act组合；只核是否有对照后的物理失败或可靠性边界，而非多任务应用成功。 |
| 20258 | 潜在：add/remove/replace依赖不同定位证据，source/target stream产生的attention位置不等于可共享操作mask；核操作对照与条件，不因编辑任务局部而排除机制边界。 |
| 20261 | 关闭：tabular feature agent的router与procedural/feedback/concept memory组合未新增更新/执行有效条件，本地数据集提升不足。 |
| 20267 | 定点消歧：四类audio/text检索任务不是独立贡献证明；只核compression是否改变可复用modality边界或代价，而非新benchmark/模块组合。 |
| 20276 | 潜在：intrinsic-dimension estimator并不测真实底层维度的理论与实证反证，可能改变representation几何指标解释；核估计器、假设与替代测量含义。 |
| 20283 | 关闭：entity linking的instance/group/lexical证据与teacher/student排序为成熟组合；任务改善未给新的选择或证据有效性边界。 |
| 20289 | 潜在：少步action-conditioned生成改用跨chunk残差指纹决定复用，且强制完整KV更新保护历史，改变缓存轴与持久状态提交责任；核实际质量/成本与失效，不采用单一加速数。 |
| 20300 | 定点消歧：forgetting/security/RL taxonomy和controlled access不是新机制；只核“100%风险消除”的实验定义是否产生需保留的保护边界，不先接受安全保证。 |
| 20304 | 关闭：材料相图AI for Science处于本项目暂缓范围，无直接大模型机制研究，不以Data/Evaluation映射恢复。 |

累计129项仍可审题摘：48潜在、11定点消歧、70具体关闭。潜在不等于准入、贡献成立、全文任务或日级完成；日期及有限独立准入仍未结束。

### 四项决定准入的必要补读

root实际读exact-v1方法及相应对照，结合apr01的十四项独立准入核，不把题型/模块名称当贡献。20244的expert/student-token条件mask改变蒸馏目标，20246的真实训练PRO迁移到imagined latent及规划/执行预算分账均转潜在。20267补读§5.4后，Table6同一文本retriever的ASR/oracle配对显示低WER也不能保证检索损失可忽略；其post-encoder selector与pooling对照支持狭窄检索设计判断，因此转标准潜在，而不是仅因audio新场景入选。三个材料均只支持受限条件，不自动形成Books新增。

20300在实际Tables2/3中“100%”只指预分类dangerous存储的retention为零，sensitive仍约54%、important约70%；已知标签的优先删除不等开放Agent安全风险清零。成熟衰减/剪枝组合没有新增保护保证，具体前分母关闭；保留该反证，不把正文安全宣传采入Books，也不扩为全部攻击审计。上述方法/评价依据见[V3证据记录](./V3_EVIDENCE_REVIEW.md)。当前129项仍可审题摘的工作分账为**51潜在、7定点消歧、71具体关闭**；尚未冻结，仍须落窗和最终准入收口。

### 剩余七项准入消歧收口（不等日级完成）

19782实际§3.4/§5以同问题的正确/错误speech context配对，SCF先条件化text-only正确，新增可检查的语言先验与声学依据分账，转5分标准潜在；不是仅因韩语新数据集准入。19998实际§2.2～2.3/§3把AC decision及reviewed version变成concern severity的测量anchor，accepted的decisive=0明确是操作性定义而非真值发现，转6分标准潜在以保留该评价边界，不把协议假设冒称全部AI review事实。

19795实际§3.4/Eq9～11确实提出memory convergence保证，而非只成熟组合；其打印的weighted mean另除memory数量，使两条相同fitness在允许正decay/mutation下可持续增长。转6分中心保证深入待裁决，只隔离所影响定理，不否定全部有限LOCOMO实验。20193实际Alg1及§4.1～4.3将LLM解析、有限WCET profiling和dual-board实验连到ISO Category3保护保证；时序/感知错误与硬件冗余的桥未建立，转6分保护深入待裁决，不采其认证或所有负载安全结论。

19792 raw题摘是后来v7.0文字，而实际exact-v1正文为v6.0；不把后发数学纠正当本窗v1的首发内容。v1 §12.2以logit界声称安全pruning但未绑定softmax归一/输出误差，保留6分必要保证核验，identity/title须绑定actual v1而非旧raw当前摘要。20158实际§3.2承认stateful memory可通过namespacing/记录中间调用/pinned backend满足目标；其§7两个方案在live API都非byte-deterministic。event-log再projection及少一次调用是成熟分支的局部取舍，没有原声称的必然不可replay反证，前分母关闭，不评分。19936实际III/IV/V使用ResNet18/CIFAR、augmentation/early stopping改善既有generalization-gap/MIA关系，当前只给成熟防护原则的局部工作点，未建立新的参数泄漏机制或改变既有隐私保护保证，前分母关闭；不是因小模型/图像一概排除。

当前129项仍可审题摘为**56潜在、0普通准入消歧、73具体关闭**。此计数不把所有潜在视为贡献已成立，仍有日期、必要证据、独立准入和Books普通待办；没有冻结最终分母。

### 长任务准入口径反查（最新工作口径）

`2604.20130v1` 原列潜在，重开[官方题摘与正文](https://arxiv.org/html/2604.20130v1)后改为贡献前关闭。论文将 GAN 的 mode dropping 与同一 mode 内 many-to-one 映射区分，并在 toy distributions、CIFAR-10 上用 pairing regularizer 改善分布覆盖；这是 GAN 图像生成训练的具体研究，不应因“生成机制”“表示坍塌”两个可类比词就跨接到本书当前 AR/Diffusion/World-Model 或 LLM 系统主线。原文没有检验这些当前架构的训练、部署或评价选择，且该局部 GAN 工作点不修正书稿已有命题；关闭理由是**目前缺直接项目贡献**，不是图像任务或小模型一概排除。保留初筛原文和此改判依据，不评分、不做 Books。`2604.20276v1` 则确实直接质疑表示几何估计器的测量对象，暂留作受限反证候选，不能用本例把所有理论/小模型负面结果一起剪掉。

2026-09-28 再作[三项具名反向准入](V3_ROOT_THREE_REVERSE_ADMISSION.md)：`2604.20027v1` 的 ViT 人眼显著性、`2604.19954v1` 的相机 viewpoint token 与 `2604.20039v1` 的合成 Blicket 动态状态机，均与章节相关，但各自只给当前 owner 已能解释的任务受限实例；不凭 ROADMAP 映射保留。暂从潜在改为具体贡献前关闭，待非作者负侧反查；原表行保留时序，不视为当前最终 disposition。若反查无反证，工作数为 129 份＝52 潜在＋77 前关闭；日期与整日 Gate 未完成。

撤回排除后 129 份仍可审题摘的当时工作分账为 **55 潜在／74 具体贡献前关闭／0 普通消歧**；当时仍未冻结，其他潜在项继续按同一准入问题复核。

### 2026-09-30 实际逐行归并后的当前口径

最终溯源更正：逐行表具有129个唯一具名身份，可复算51潜在＋78贡献前关闭；旧过程汇总“130−1撤回”未保留那一项身份及官方标记，不能作为已核撤回证据或计数，正式Report不再采用。下面及更早的130/撤回数字仅保留过程原文，不覆盖此更正；52最终候选与Books均不依赖未具名排除项，不据此扩大到未知全文队列。

原130题摘中1撤回，不进入候选或Books；129份当前行逐项按后续具名改判归并为 **51潜在+78具名贡献前关闭**，而非将旧57/56/55/52过程计数继承到正式报告。当前潜在身份为：19749、19750、19752、19765、19769、19775、19780、19782、19784、19790、19792、19795、19809、19811、19821、19835、19844、19857、19877、19884、19899、19925、19966、19974、19998、20012、20021、20032、20041、20047、20051、20087、20090、20098、20105、20136、20148、20156、20157、20193、20199、20200、20202、20209、20219、20244、20246、20258、20267、20276、20289。19767/19826/19936/20158/20300/20130/20027/19954/20039的原表潜在或消歧文字已由各自后续理由替代；反证与原文不删除。78否定侧仍是具体贡献筛选结果，不代表每篇全文或全网零遗漏。

20329的反向准入是额外机构/跨源恢复，单列更早Google公开日期保留；不把它计入上述129/51，也不将原来的泛化排除当有效结论。加已单独审阅的OpenAI WebSockets，目前52本窗提案的证据/评分/具体Books见新正式README。日期组合和最后十二项非作者/写后尚待终核，不把本归并等同日级完成。
