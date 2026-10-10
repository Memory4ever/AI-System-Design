# Jan14 MI-PRUN / PRISM 独立必要复核 delta9（2026-10-08）

复核者：review_jan15_delta，非作者。仅root授权07212 /07224，本日适用合同/背景/ROADMAP与停点已于delta8恢复重读，复用未变上下文。固定BJTJan13自然日补充窗，原17及原窗口不动；不加载Jan17、不重复其T3S。未写Books/Report/LS/索引，未stage/commit/push；无DAY。

两项完整题摘实际读本日五份increment-abstracts-*-20261007.json对应行，均有具名潜在贡献。必要原证分别increment-necessary-core-2601.07212v1-20261008.json（完整§3/Alg1/§4；输出分两片重叠读，不把半段当完成）、increment-necessary-core-2601.07224v1-20261008.json（完整§2/3/4/限制）。不遍历全附件，不核artifact/复现；疑点只沿拟采用命题深入。

日期复用本日已核公告/ID上下界并读increment-date-bounds-rest-20261007.json两行：07212 v1 Updated Jan13 02:04:44Z→registered03:57:30Z；07224 02:05:31Z→03:57:46Z，只归BJTJan13，不以Submitted或register独证。独立轻读当前abs：07212 v1、07224 v2/Apr12/ACL2026 Main，未见具体撤回/纠错说明；仅采用精确v1，不比较全版本。

## 07212 MI-PRUN — 2+1+2=5 / 中心争议终态边界 PASS

原有逐block剪枝忽略连删组合；Fast-Block-Select以单块负MI预排序，在prune/alternative池内构造同长度contiguous候选，按单块sum粗排后只测有限topK的首in/末out MI，再选conflict-free组合。这是实际候选组合接口，准入不因理论未知/局部实验弱而取消，不用降分或改成Existing避开中心问题。

§3.2 Eq2–4比较的是DPI上界，作者紧接着明确actual组MI可反向；不能将上界次序证明actual组重要性排序。§3.1却把output完全由input决定解释为最大MI/最小功能变换，这与普通确定性block关系不相容。独立数学参照：H~Bernoulli(.5)，F(H)=H与F(H)=1-H均I(H;F(H))=1，而固定下游任务目标H时，一者保答案、一者翻转；故MI不独自认证可删除性。这不是作者实测LLM反例，也不替作者设定隐藏坐标离散化、噪声、随机变量或估计器。连续hidden变量的MI更须定义测量模型，不能默认有限精确值。

实际已读§3/4必要核心未明确actual hidden-MI estimator及其population/量化或噪声，也未闭合ConflictFreeSelect可执行选择目标/全局求解。停止P不再变化与作者未观察振荡只支持其设定中的观察，不签全球最优、所有预算必收敛或稳定性理论。并不声称全理论错误或所有结果无效。

Table1允许有限局部报告：Qwen7B平均65.36略高Short65.13，但RTE71.84低于80.87；Llama13 Winogrande59.59低于64.17；dense更强，其他pruner删的结构/ratio并非完全相同。WikiText/Alpaca calibration、model/sequence/search及全部费用绑定；未披露hardware/precision/repeated runs/实际端到端latency，不采加速普遍结论或未核图数。

Actual Ch17:369–425完整邻接实际读，379–415已有几何诊断≠删除/顺序协议与完整回归。这个通则存在不能绕过本篇中心争议授Existing。MI重要性/执行准则不作为正面方法证据、不进Books、不支撑性能/无遗漏保证；有限table保原限定，正式处置为暂缓/争议。定点重开需求：exact-version actual MI随机变量/estimator及有效scope、可核conflict-selection实现，或不依赖该MI重要性论证的可比删除干预；不泛请求全论文/全历史。中心争议隔离可作本窗终态，不将普通尚未读完混为隔离。

## 07224 PRISM — 2+1+2=5 / Ch29 单段最小 PRE PASS

§2–3在冻结初始化模型上用gold reference的valid-response平均NTP loss，一次backward而无optimizer update；对7L个Attention/FFN projection矩阵取Frobenius norm，再以Gini/CV/kurtosis浓度的corpus median，把低分给SFT、高分给RL。这改变训练目标和有效人口，而不只是同一objective下换样本质量权重；有限机制准入清楚。

checkpoint/gold/context/valid-token reduction/matrix grouping决定probe身份；norm浓度不是全部方向或optimizer effective update。矩阵大小与参数化可能影响比较，high concentration不认证唯一知识冲突、RL不可替代或参数更新安全。median的≤/>含ties时并非必然精确50:50；static初始化评分不会在SFT后自动成为当前状态诊断。§4逆路由、magnitude对照只给限定训练配置反侧，非认知重构唯一因果/跨域50%最优或Pareto保证。限制明确未测大模型、动态刷新及一般开放域。

Qwen3/Llama3.1-8B、ALFWorld/WebShop、三seed mean限定人口。Table1 OOD Gini Pick75低于GiGPO90、Clean89.74低于GRPO92.31；Table3 Random已经3.07×，Gini3.22×，大部分相对fullRL预算差不能全归selector。8A10080G、probe的1m48s/2m16s加SFT/RL总费都保；不采用backward内存≈forward、half-data=half-total-compute或headline通用省费。

Actual Ch29:686–730和Ch27:1103–1144完整邻接实际读。Ch29:709–711已有初始policy outcome人口与SFT/RL有效监督区别，但无frozen gold-gradient浓度驱动跨训练目标人口的分支；Ch27几何selector只拥有admission、不拥有objective，故不能在那里重复新增objective-routing论证。唯一owner为TRAIN-SFT /Ch29，不在Ch33重复GRPO信用公式。

最小采用：当前711的outcome人口/成本回退后、713泛化总结前一短段。保普通mixed SFT→RL在人口/目标稳定时简单；给frozen probe→matrix concentration→median两目标人口接口；近文写代理身份/参数化、ties/static漂移、非认知真值、随机与OOD负侧、全部probe+SFT+RL费用；回退random/mixed/fullSFT/fullRL与held-out验证。不添认知理论、新标题、完整训练recipe或第二owner。root协调Ch29单段+自身注锁，作者无锁不写；source PRE可先于共享锁释放完成，实际写后由本复核者POST，不计PRE为整合。

## 停点

07212争议终态范围可同步；07224窄PRE已报root等锁/写后复核。本轮不授POST或DAY、不扩大未prepared批次。支持与决定反侧均足以给上述最小结论，其他当日普通工作由主流程独立路由。

### 07224 actual POST（后续，覆盖历史待写状态）

root授PRISM Ch29单段/自身注窄锁，作者实际写后，本复核者独立读新正文713、完整697–729邻接及自身末注1373。原outcome条件人口→frozen GT梯度浓度跨目标人口→泛化限制衔接成立，未改原有KD或outcome有效边界。正文近文保checkpoint/GT/context/reduction/matrix grouping/median ties、尺寸/参数化/static状态、非knowledge-conflict或RL必需、OOD负侧/随机相近预算、probe+SFT+RL全费与替代回退，无认知真值/Pareto/计算保证；自身注保精确v1和必要边界。actual POST PASS，已通知root释放此项Ch29窄锁，可计1实际整合；不授artifact/复现或DAY。root另允许只接07200/07411/07645逐篇ready必要材料，尚未准备的集合不扩。
