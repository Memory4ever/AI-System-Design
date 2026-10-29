# G4整体PRE · 2025-10-29

Writer已全文自读以下四份新增/独立marker/本人注及实际完整必要两肩，含Ch66 PPI完整代码与校正两段、Ch48完整budget代码。不作新首必要；G23564在D理想memory层级之前、原call-scoped之后，无冲突。尚未SAVE，请sole整体PRE。

## 22500 · books/part-06-ai-infrastructure/66-evaluation-system.md

### 完整新增

人工监督不只可提供正标签，也可明确一个不正确类；但把complementary-label agreement换成accuracy，须先声明K类、单一GT与同质均匀wrong-label噪声模型。在该模型、iid与同人口条件下，agreement的线性变换可估准确率，再与原标签估计组合。[受限互补标注分析](https://arxiv.org/html/2510.22500v1)的有限估计可能越出[0,1]，clip便不保原无偏；fixed或独立pilot选择的权重，也不能静默换成同一数据plugin。用oracle生成负标签不是实际人获得superhuman能力，真实多解/相关错误更不继承公式。正/负标签来源、K、权重和目标人口须冻结，额外标注、pilot、估计及独立gold验证全计费。噪声模型、支持或方差不合时，保原可信gold/人工升级与保守区间，不由一项低方差估计取代内容真值或任意负标注正确性。
<!-- source-family:SF-2025-ARXIV-2510-22500 -->

### 本人注/自读

- `SF-2025-ARXIV-2510-22500`：Daily2025-10-29补窗；复用sole精确v1必要及R47实际owner差额，未核实现或复现。complementary-label agreement到accuracy的有限噪声模型与组合权重，不重复PPI人工纠偏。

complementary-label agreement到accuracy的有限噪声模型与组合权重，不重复PPI人工纠偏。

### 实际前肩

`auto-only` 用规模换偏差，`human-only` 用可信度换成本；二者不是只能二选一。若目标是估计一个系统总体质量或两个系统
的 population-level 差异，可把大量自动 metric 视为廉价但有偏的辅助变量，再用同分布抽取的少量人工标签估计并校正
这份偏差。Prediction-powered inference 一类方法因此改变的是 estimator，而不是把 metric 升级为 ground truth：

```text
large unlabeled population + automatic scores
+ smaller representative human-labeled sample
→ estimate metric residual / correction
→ bias-corrected population estimate + confidence interval
```

这条路线获得更高 statistical power 或更少 annotation，却新增 sample-design、metric/human correlated error、
distribution drift 与 interval interpretation 责任。Paired design、unpaired design、parametric 或 non-parametric procedure
不是可互换实现；必须冻结抽样单位、target estimand、配对关系和缺失标签策略。区间描述的是声明 population 与假设下的
系统级估计，不是单条回答正确概率，也不能授权单次高风险 action。Metric 与人工 residual 的关系在新 domain、模型或
prompt distribution 上失效后，必须重新标注和校准；样本很小、目标不可稳定标注或错误高度相关时，保守的人工评估仍成立。

### 实际后肩

二元judge校正还要区分“消偏”与“高效”：直接反演误分类矩阵可校正总体标签率，但judge两类识别率之和接近一时，分母会放大校准误差。若大量judge样本和小量人工样本来自同一iid人口，人工缺失是随机MCAR，样本量比趋于正有限值且参数在interior、judge有正辨别力，一条条件结果把有效影响函数的预测均值加人工residual写法，与最优PPI++和binary MLE联系起来；二元条件均值可用affine形式，此处等价是渐近的，不是有限样本学得权重无条件无偏或任意continuous/ordinal标签同样efficient。<!-- source-family:SF-2026-ARXIV-2601-05420 -->

[有限Arena人类偏好对照](https://arxiv.org/html/2601.05420v1)支持这一二元方差取舍，标签仍是该人口的人类偏好而非客观正确率。非线性连续目标需要相应一致的条件均值模型；selection、judge或人口漂移都会破坏旧校准。因而应记录人工抽样/缺失机制、estimand与n/m，独立验收区间，而不让较窄CI授权单条输出。假设失效或calibration不可靠时，保留代表性人工评估、保守区间及原残差校正。

少量 gold labels 还可以约束 noisy judge 的错误模型，而不只用于估计平均残差。若目标是总体 failure rate，一条条件分支联合估计 failure prevalence 与 judge 的 true/false-positive rates，再以已有校准给出的区间约束 likelihood 优化。区间收窄可减少小样本方差，却把 prior validity 变成额外前提；错误区间会让估计向错误方向偏移，不能因优化器收敛而称作无偏。<!-- source-family:SF-2026-ARXIV-2604-03257 -->

平台因此需要保留区间的来源、gold抽样单位、judge/model身份与目标分布，对约束和无约束估计一起做敏感性检查。这是总体 estimand，不是逐条回答正确率或发布授权。作者少量gold与大量judge标签的同域分类实验支持该方差—偏差分支，不证明跨领域 anchor 可直接迁移；prior失配、标签可比性不足或漂移时，应放宽/移除约束，追加代表性人工标注，回退原有残差校正或human-only评估。

### 实际注尾（保留）

- `SF-2025-ARXIV-2510-22622`：Daily2025-10-29补窗；复用sole已成exact-v1必要支持/反侧，writer已实际读具体结论与owner差额，未核代码或复现。按R40真差额补迁移非互逆、叠加伪迹支配及mask后重定label，区别已有普通模态消融。

## 22733 · books/part-07-agent/76-rag.md

### 完整新增

候选交互还可以进入query向量，而非逐篇重写passage表示：将query与top-20文档列表作为listwise prompt编码成一份向量，再与预计算top-100文档向量评分。[E2Rank的受限接口](https://arxiv.org/html/2510.22733v1#S3)让query依赖候选池、次序与prompt，不能继续当独立query缓存或同原encoder零训练；contrastive加RankNet的训练标签/来源也是身份。PRF超过20的反退提示更多context不必更好，不同训练源与A100上50query局部计时不授全链5倍或生产SLO。建库、候选检索、完整list编码、训练/调参和最终reader都付费；候选支持、顺序敏感或净质量/成本失配时，保原独立query、较简单reranker与实际答案核验，不由向量形式或较少在线pair调用批准事实可靠和免费重排。
<!-- source-family:SF-2025-ARXIV-2510-22733 -->

### 本人注/自读

- `SF-2025-ARXIV-2510-22733`：Daily2025-10-29补窗；复用sole精确v1必要及R47实际owner差额，未核实现或复现。候选list作为query编码上下文，区别原query不变的contextualized passage。

候选list作为query编码上下文，区别原query不变的contextualized passage。

### 实际前肩

不变的文档端还可以只缓存压缩后的模态表示，而不预存完整joint模型的KV：冻结视觉encoder，以learned queries先将视觉tokens压缩，在线再由较小语言网络联合读取它们和当前文字。[EDJE的受限分支](https://arxiv.org/html/2510.06820v1#S3)把离线压缩资产与实时相关性消费分开；冻结视觉不等只训练adapter，固定表示维度也不保证任意分辨率都不增token或保持证据。缓存须绑定encoder、adapter、预处理与来源版本，top-k之外的漏项仍不能由重排恢复。压缩有局部排名反退，蒸馏/不同训练数据量亦非同预算因果；cached-vision下仅joint部分的计时不含视觉编码、建库、I/O与初检，不能移作完整pipeline倍率。全部teacher/压缩和语言网络训练、缓存构建刷新、在线候选评分及reader支持回归都付费；复用率、细节支持或净预算不足时，保更完整视觉tokens、原cross-encoder和原图核验，不由小joint网络与较快在线快照批准无损相关性、充分证据和服务SLO。<!-- source-family:SF-2025-ARXIV-2510-06820 -->

重排若已经用query到文档的attention mass评分，还可以让训练直接监督同一份candidate分数，而不先学生成ID再改读另一种内部量。独立document blocks与共享局部位置使文档state不依赖本次query/候选次序，最终query侧另选少量token参与评分，再在输入候选空间内训练pointer目标并直接排序。独立编码、消费支集与评分目标各有身份；不生成ID只排除了该输出格式错误，不认证相关性或事实支持。

[CompRank的有限对照](https://arxiv.org/html/2606.11700v1)中，均匀片段覆盖可优于文档自身saliency，却有压缩质量损失，更多token亦非单调；长候选表的ID失败反侧限受测训练/解码协议。当前实验仍重算document blocks，预编码query-only时间只是模拟，不含cache存取/驻留/刷新，不能当已交付加速。语料/模型与mask版本、训练、完整编码/检索/评分和reader取证都计费；局部证据稀疏、cache复用或净质量预算不合时，保完整tokens、普通重排与原文核验，不由无ID错误或短online快照签RAG可靠性。
<!-- source-family:SF-2026-ARXIV-2606-11700 -->

### 实际后肩

离线文档资产与在线候选交互也可分成两份表示：先固定passage embeddings，在线为本次候选分配局部ID，用global与masked-local交互产生contextualized passage，再让原query向量评分。[EBCAR的受限分支](https://arxiv.org/html/2510.13329v1)保留了离线编码接口，却不使在线文档state独立于候选集合；同一query换Top-k或加入干扰项，原文档得分仍可能改变，不能把“query未更新”当作ranking invariance。应保存离线encoder/语料/索引、候选集合/顺序与local-ID范围、mask和评分器，训练强制把gold补进Top20的条件不能搬成test时已有正确召回。候选数超过训练支持还可触及ID范围，Top50缓解一项问题也不保证永不退；多positive评价与one-positive训练须分人口。全部建库/刷新、候选检索、joint网络训练/评分与reader原文核验计费，单卡batch1 QPS不是完整服务SLO。ID、候选支持或净质量失配时，保原独立向量排序、完整cross-encoder与原文回读，不由缓存embedding或同维接口批准无损重排、事实支持和全链加速。

<!-- source-family:SF-2025-ARXIV-2510-13329 -->

检索encoder增加expert容量时，还须分开训练时的路由与建库、查询时实际运行的模式。先由共同Transformer产生表示，训练时以带噪top-1选择post-transformer expert，推理却可以继续TOP1或运行ALL再聚合；[SB-MoE的受限分支](https://arxiv.org/html/2510.15683v1)中，这两种variant不是同一份质量/费用合同。稀疏训练不证明ALL推理少算，ALL的收益也不能回签TOP1；改变expert/聚合模式后，document向量、query编码和索引须共同重建或重验，不能只换查询端。更多expert与更大base仍可反退，单seed及不同训练日程不授容量普效。全部训练、文档重编码/刷新、expert驻留与在线检索回归均付费；表示、模式一致性或净预算不合时，保原dense encoder、匹配索引与原文核验，不由稀疏标签或局部排名签发全链加速和事实支持。

<!-- source-family:SF-2025-ARXIV-2510-15683 -->

### 实际注尾（保留）

- `SF-2025-ARXIV-2510-21440`：Daily2025-10-28补Oct27；exact-v1必要层、2+2+2=6，R20通过。仅reader效用/干扰与IR相关性分责，保非拒答强假设、组合交互和全费；未核实现/复现，PRE/SAVE/全自读/solePOST据本日实际层。

## 22876 · books/part-05-inference-system/48-speculative-decoding.md

### 完整新增

异长batch的speculative路径还须让矩形张量布局与每条逻辑prefix同时一致：padding、position/mask、draft/target cache推进、接受长度以及bonus token的物化必须绑定同一序列身份，不能只把张量变contiguous就称协议正确。[受限batch修复分析](https://arxiv.org/html/2510.22876v1)指出这些状态接口与TPS相互影响，但all-match索引/bonus伪代码未闭时不照录完整recipe；非spec batch也可有浮点mismatch，输出不同不能逐个都归给接受算法。分组收益依实际长度分布与受测GPU kernel布局，应同时验output alignment、分布条件和完整吞吐，不把greedy对齐当任意sampling lossless。padding/compaction、概率行、KV写入与全部验证付费；身份、索引或收益不合时，保单序列/较小同长batch及已验target路径，不由矩形batch更快跳过真正联合分布不变量。
<!-- source-family:SF-2025-ARXIV-2510-22876 -->

### 本人注/自读

- `SF-2025-ARXIV-2510-22876`：Daily2025-10-29补窗；复用sole精确v1必要及R47实际owner差额，未核实现或复现。异长矩形layout的padding/position/cache/bonus联合物化，7分设计修正深入而不照未闭recipe。

异长矩形layout的padding/position/cache/bonus联合物化，7分设计修正深入而不照未闭recipe。

### 实际前肩

这里作废的是提交资格及对应错误 prefix 的 KV，不意味着已经计算的辅助 hidden feature 永远不能作为下一轮 proposal 的条件；这种跨轮复用仍须从更正后的 prefix 生成并重新验证，不能把辅助 feature 冒充正确前缀的 target KV。它用额外特征对齐、有限生命周期与 reset 管理换取较好的下一轮草稿；当失效状态难以隔离或收益不足时，丢弃并重算仍是更简单可靠的路径。

把下一轮 draft 与当前 verify 重叠后，还要区分检索 proposal、target-verified guidance 与 committed chain。目标侧可以对检索候选做验证，用更正后的前缀刷新下一轮 draft 的条件；但“来自 target”或使用 causal mask 本身不证明整条 guidance 已符合 greedy 路径。只有在同一更正路径上已逐位置验证的 guidance 才能延伸提交；随机解码发生拒绝时，residual sampling 的 replacement 可能不同于预计算路径，后续 guidance 必须失效，不能绕过重新验证。[受限双侧检索方案](https://arxiv.org/html/2601.05524v1)支持这种状态与权限分层，但其 EM accuracy 不是 token-law 证明，本文不继承全局 lossless 宣称。检索、跨模型同步与状态刷新都增加成本；没有同路径验证依据、过期草稿难以隔离或 overlap 收益不足时，普通 rollback、短 draft 和 target-only 仍是合理回退。<!-- source-family:SF-2026-ARXIV-2601-05524 -->

被target计算过的概率行，也不一定是下一轮可直接采样的target分布：其身份是完整prefix，不是最后一个token相同即可复用。若本轮额外提交了continuation，下一轮所需行必须正好条件于这个新prefix；旧地址的行最多辅助挑proposal。仅评分候选树、沿一条path接受、发出一个continuation且对所选tree条件exact的类别内，保住下一轮root行意味着比完整遍历少接受了token；[这一受限分析](https://arxiv.org/html/2610.29210v1)不是任意verifier或任意跨轮调度的普遍不可能定理。另算当前root行、先抽首token再分配树预算可改变接受效率，却增加target pass和调度成本；双GPU、batch1下能被draft遮住的成本不自动迁移到单卡或高并发。状态地址、未来随机性隔离或重叠费用不能核实，仍保普通树构造与target-only，不以旧row来自target就跳过当前prefix验证。<!-- source-family:SF-2026-ARXIV-2610-29210 -->

### 实际后肩

在单序列CPU执行中，正确的接受规则之外还有图与线程的生命周期成本。draft与target若每轮各自重建context、切线程池或复制候选KV，即使接受长度不变也可能没有净收益；[一个受限实现](https://arxiv.org/html/2610.28671v1)把两张静态图放进共同arena，按依赖顺序复用全部线程，并把尚未提交的KV写入预置scratchpad。只推进已接受prefix的写指针，下一轮覆盖或屏蔽其余slot，可以把物理搬运与逻辑回滚分开，但必须同时维持position、可见mask和模型各自状态身份。该CPU设计不是GPU多租户paging的普遍替代，固定arena也支付容量与并发隔离代价；源论文的单NUMA/AVX2实验和有限KL检查不证明所有sampling、浮点路径或memory安全。模型形状不静态、隔离不足或线程争用抵消收益时，保留普通context与严格重算，并把图切换、draft、verify和rollback一起计时。<!-- source-family:SF-2026-ARXIV-2610-28671 -->

衡量收益时应记录：

```text
accepted_tokens_per_target_step
draft_cost
verification_cost
rollback / scheduling overhead
```

Acceptance rate 高不等于端到端加速一定高。若 draft 自身昂贵、verification shape 低效或 target batch 被打散，节省的 serial steps 可能被额外 work 抵消。

### 实际注尾（保留）

- `SF-2025-ARXIV-2510-15312` — Daily2025-10-21补Oct20；Lorentz R14首次exact-v1§3.2–4/4.1/4.3–5，writer核§3.4拒稿子段仅重新提案，2+2+2=6，图驻留/候选资格差额深入。保Qualcomm12/16/24GB、QNN/mllm、Qwen0.5/1.5B及Llama3.2-3B、CPU/GPU敏感算子、profile贪心与额外校准/状态费用；不采无条件随机采样精确性或SLO，未核实现/复现。

## 23564 · books/part-07-agent/81-workflow.md

### 完整新增

调用上下文还可比活动祖先frames更窄：policy只读取当前函数signature与显式变量namespace，先返回placeholder代码，遇到尚未定义的子任务再递归展开，直到primitive才执行。[ReCode的受限接口](https://arxiv.org/html/2510.23564v1#S3)把计划粒度与执行分开，却会在变量未显式保存时丢掉旧轨迹信息；共享namespace还须有作用域、类型和身份合同。max-depth只限制展开深度，不保证任意Python循环、重试或原子effect终止，traceback重试也不撤销先前副作用。teacher分别生成三范式并筛top40%改变数据质量/人口，较少pair或token不单独识别粒度控制因果；部分任务反退须保。生成/筛选、展开、变量驻留、全部执行与独立tests均付费，状态、权限或预算失配时，保原call-scoped/较完整trace、固定scaffold与外部verifier，不由一棵code tree批准无错执行或通用净省。
<!-- source-family:SF-2025-ARXIV-2510-23564 -->

### 本人注/自读

- `SF-2025-ARXIV-2510-23564`：Daily2025-10-29补窗；复用sole精确v1必要及R47实际owner差额，未核实现或复现。当前signature/显式namespace与placeholder递归展开的更窄policy可见性，区别活动祖先frames。

当前signature/显式namespace与placeholder递归展开的更窄policy可见性，区别活动祖先frames。

### 实际前肩

- interpreting ambiguous intent；
- drafting content；
- proposing plans/tool arguments；
- ranking alternatives；
- diagnosing unstructured failure。

这种组合既保留模型灵活性，又让业务不变量可测试。

程序与模型的边界还可以落到每个函数调用：caller 保存循环、必经检查与终止预算，模型只返回受声明 schema 约束的候选；活动调用读取祖先 frames，已完成子树向上交回摘要，完整 trace 另存而不每次重放全部历史。[受限 call-scoped 设计](https://arxiv.org/html/2606.15874v1#S3)将执行结构与本次可见上下文对应起来，但模型返回值仍会影响程序分支，类型解析成功也不保证判断正确。摘要仍可能丢信息，父层积累的子调用返回、frame 大小与递归深度都须独立限制，不能只凭 DAG 名称签出按深度恒定的 token 预算。调用、摘要、trace 驻留、重试与测试全计费；自生成函数通过现有 tests 也不授全域正确或新的 effect 权限。结构、返回证据或预算不合时，保留固定 scaffold、较完整原文和人工/独立 verifier，必要时停止递归；可探索节点的灵活性不替 caller 的执行、恢复与提交责任。
<!-- source-family:SF-2026-ARXIV-2606-15874 -->

### 实际后肩

上下文组织还决定能用哪一种理想计算模型描述workflow。固定有限alphabet与常量大小的可辨状态，可抽象为finite automaton；严格LIFO且frame alphabet有限的递归记忆，可对应pushdown automaton；只有理想无界且可反复读写的memory才进入Turing-machine层级。[受限acceptor-language分析](https://arxiv.org/html/2510.23487v1)比较的是确定/非确定接受器识别的语言，忽略具体输出和概率，不是实际Agent任务成功、策略最优或现实无限算力证明。有限context与实现中的摘要会改变抽象，模型调用也不自动成为可靠transition oracle；状态/栈接口、预算、解析与恢复都要检验并付费。假设不合时，回到显式有限workflow、bounded frames和独立结果检查，不由理论表达能力批准工具权限、无错执行或可终止性。
<!-- source-family:SF-2025-ARXIV-2510-23487 -->

### 从一次性脚本到平台拥有的可编辑 DAG

自由代码生成适合探索新算子与一次性任务，因为它不要求平台预先拥有完整 operator catalog；但当结果需要被复用、可视化、协作编辑与恢复时，script 不再是足够的状态载体。更稳健的演进是让平台拥有带版本的 canonical DAG，Agent 只提交 typed mutation，backend 在 commit 前验证 schema、引用与无环性，executor 再用 run evidence 验证语义结果，visual editor 与 chat 只呈现同一 graph identity。

这条路线用 operator 生态约束换取可编辑性、审计与恢复；未知算子和短期探索仍可保留脚本分支。Skills 只是可更新的派生操作指南，既不拥有 DAG，也不能绕过平台验证。

### 实际注尾（保留）

- `SF-2025-ARXIV-2510-23487`：Daily2025-10-29补窗；复用sole已成exact-v1必要支持/反侧，writer已实际读具体结论与owner差额，未核代码或复现。按R40真实memory-discipline gap，仅exact-v1 acceptor层级与假设；不回填后版概率trace或认证真实ReAct。
