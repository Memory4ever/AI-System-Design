# 02-27 首6：精确v1必要命题审阅

原始HTML均为 `V3_CORE_2602.<ID>.raw`，可复核段落为相同ID `V3_BLOCKS_*.md` 的 block。作者只读拟采用命题、关键对照与直接反侧，不把下载正文等同完成阅读；未核实现、未运行代码、未复现实验。日期见 V3_CURRENT_METADATA.json；贡献准入已由 root 独立校准。

最新实际处置：21307/21320/21420/21445已整合并经root非作者PRE及实际正文/完整邻接/自身末注POST通过。具体位置为Ch16 212–214、自身341；Ch33 1577/1594、自身2441/2443；Ch26 824–826、自身1444。三文件窄锁均已释放。21447为具体已有覆盖Ch72 1641–1676及2913–2922，未改书；21368为中心争议终态隔离，不采用。下方拟正文与申请描述保留为实际写前差额依据，不代表仍待写入。六项单项终态不授整日完成。

## 21307 SymTorch — 2+1+3=6，标准→具体gap深入，Experimental

必要原源：[exact-v1](https://arxiv.org/html/2602.21307v1) §4.1、§5.1；blocks 51–73、105–115。PCA将MLP输入/输出降至32/8维，在投影坐标中逐输出symbolic regression，再重建回residual shape；不是从公式可读性推导无损。Qwen2.5-1.5B-Instruct三层7/14/21替换；WikiText2 baseline ppl10.62，PCA+MLP增加3.11，PCA+symbolic增加3.14，identity增加6.97，分别隔离投影损失/近似损失/删层控制。A100 SXM4-80GB、KV cache关闭、100次full forward，8.3%吞吐提升只支持该测量，不是decode/serving SLO。符号搜索成本随变量/operator/data增长，逐输出搜索昂贵；训练与评价同域，跨域退化未测。

Books真实差额：MODEL-FFN Ch16已逐段读1–352；现有STEM静态表、spline重参数化、SPM块乘积均不是“投影降低搜索维度→函数代理→投影误差与代理误差分别核”的近似替换分支。拟在现有SPM段后、`Linear 为什么最终成为 GEMM`前插两段，保留dense/gated回退。相邻Ch15末280–345、Ch17开篇1–95已读，FFN逐位置职责及residual shape不变。申请仅Ch16窄锁。

拟正文：

> 当目标是替换已训好的逐位置函数，而不是改变训练参数化时，也可先把输入和输出投影到较低维坐标，在该坐标中为每个输出拟合有界的符号函数，再重建回 residual stream。这减少了函数搜索的维度，却不保证保留 dense FFN 的表达能力；必须分别对照原层、投影后仍保留原函数、投影后的代理以及删层/恒等路径，才知道质量损失来自压缩还是代理近似。低维表达式可读，也不证明它是模型原先唯一使用的内部算法。
>
> 符号搜索、缓存中间激活和逐输出拟合增加离线成本，变量或算子集合扩大时可能迅速变贵。[受限 MLP 替换](https://arxiv.org/html/2602.21307v1)的投影控制几乎解释了全部 perplexity 增量；三层、同域 WikiText-2、关闭 KV cache 的 full-forward 吞吐不授长序列 decode 或生产 SLO。投影丢失信息、跨域质量退步或端到端成本不合算时，保留原 dense/gated 层；这是一条可验证的近似分支，不是让所有 MLP 变成公式。

## 21320 Tool-R0 — 2+2+3=7，深入，Experimental

必要原源：[exact-v1](https://arxiv.org/html/2602.21320v1) §3–4、Table3角色/冻结/难度消融、§6；blocks20–83、96–101。两角色均起于instruction-tuned模型，“from scratch”不是无已有能力。固定外部spec分布规定domain/context/工具菜单/调用数，Generator输出question/menu/gold calls；format/schema/value词边界检查不认证语义与真实执行。8次Solver MC估难，(.25,.75)区间及Gaussian reward挑中等难题，语义仍由Solver judge代理。生成2k训练题，角色分离、冻结generator、去难度与hard-cliff消融支持有限curriculum控制；已有TaskDistribution和同源验证使“无人工数据”不等无外部先验/真值。

AST工具name/key/value指标不等真实执行安全。Table1与Table2 APIbank baseline19.13/10.13不一致，故不引用该项联合headline；只采用直接角色/难度控制。生成预算/其他curated数据并非等全生命周期成本；小模型self-play饱和、MC采样与judge调用付费。

Books：现Ch33 1584–1590已有proposal/solver/verifier分责及固定题库共存，未写task-spec支持集、MC难度区间和“题目菜单gold一致≠语义真”。此三接口可一段增强该既有论证，不再增加论文小节。待目标Ch33相邻上下文及Ch32/34相关交接读完再申请锁；本条尚未Books完成。

## 21368 Black-Box Reliability — 3+2+3=8，深入，Central Disputed

必要原源：[exact-v1](https://arxiv.org/html/2602.21368v1) §§2.4/4.3/6–7/12–13；blocks60–66、149–156、204–281、511–522。实际central claim为从小校准集反选reliability level并对任意agent部署认证，不是仅成熟fixed-alpha conformal。

1. §6.2 rank score离散且可+∞；§6.4(6.6)明确上界只在no ties，而§7.1无条件继承该上界。例所有有限rank恒1，coverage=1，α=.1，n=500时overcoverage=.1>1/501。普通保守lower bound不因此失效，但vanishing exactness/可靠度解释的核心量词失效。
2. §2.4 α*从同一校准结果反选；固定预先声明α的exchangeable rank论证不能直接给一个数据适配α*的conditional部署置信结论。n+1分母不是对未知Bernoulli模式成功率的高置信下界。
3. §7.3允许p*=0并称S∞仍覆盖；§5定义的集合只含采样候选，§6.2未采到真类时score∞。若p*=0、候选始终仅错误类，则S∞也无真答案；没有把∞明确转成全标签域/拒绝的定义，event `score≤∞`不等真答案进入已采样集合。

故不将外围正确的Hoeffding多数条件或成熟fixed-alpha规则强行拆出Integration。Books状态=Not Adopted；所需重开材料是正式修正以上central量词/∞集合定义及匹配实验协议的原源，不是补下载附件。Ch66709–761已有支持集/exchangeability/label-event共存边界，无此源新正文需求。

## 21420 ACE — 2+1+3=6，标准→具体gap深入，Experimental

必要原源：[exact-v1](https://arxiv.org/html/2602.21420v1) §4 Eq4–14/Algorithm1、§5 Table1–3、§6；blocks48–103、104–176。仅负advantage乘 `1+α softplus(c)`，c为current/reference逐token logratio求平均（实现用长度归一化），正确样本维持原advantage。c=0也增加αlog2，不是“非正c完全不动”。理论明确on-policy、无限样本且stop-gradient分解有residual，不能称精确KL正则等价；不采用更外围variance/quality theorem作普遍收益证书。

5次训练、MATH500、温度.7 top-p.95 n=32采样；Qwen2.5Math7B Pass32 91.3→94.3，DAPO94.6→96.1。AIME只有30题；Llama AIME ACE-DAPO Pass1 .2< .3、Pass2打平，故“所有k所有模型改善”不成立，有限数学实验不证明通用推理边界扩张。参考模型不校准、binary verifier、advantage估计、length等影响权重；增强负更新不消除noise且zero additional compute依赖已有reference logprobs。

Books：Ch33现1574–1578仅generic更强高置信负correction，缺same-negative内具体乘法、均值logratio/stop-gradient与c0反侧。可一段加在该原段后；不能用表明示headline修订旧所有k语气。待窄锁。

## 21445 AutoHorizon — 2+2+3=7，深入，Experimental

必要原源：[exact-v1](https://arxiv.org/html/2602.21445v1) §§3.1/3.4/4/6；blocks27–40、51–65、68–91、95–107。p是预测整个chunk，e是这次执行prefix；无需重训地从action self-attention跨heads/layers平均、row entropy筛选、bidirectional pointer估边界，若双端覆盖合并则执行全p，否则只forward prefix。attention只是e的proposal，不是传感新信息/置信认证。预测p不随缩e改变，成本是更频繁replan和取attention。

π0.5 p10/50与GR00TN1.5 p16；LIBERO每任务25rollouts×3、RoboTwin100×3；实机Franka3 task×10 trial、150微调traj、4阶段solve率不等binary成功率。静态Oracle+与Random及近mean固定值对照支持动态差额。§3.2/6最优公式依赖δc常数、δd=k e log e、L/e整数；integer两候选可能tie，不能采用普遍唯一最优或Attention=true dynamics。原同步/保守短e与controller安全边界继续共存。

Books：Ch26 ActionChunk时间契约816–827及420–437已读，只泛谈H/uncertainty多次采样，未区分p/e和无需额外rollout的attention-proposed prefix。拟在原时间契约后、uncertainty候选前加两段（p/e分账+attention提案/成本文界）。Ch25结尾/Ch27开篇相关交接待读后申请锁。

## 21447 MMA-RAG — 3+2+3=8，深入，Experimental（实测限界）

必要原源：[exact-v1](https://arxiv.org/html/2602.21447v1) §§2–6/Table2–3；blocks13–55、56–102。C1query/C2action/C3retrieval/C4toolreturn/C5response共享独立trust subsystem的固定格式风险summary Φ，每次读取前态及当前artifact/metadata并写新态，避免每关只看当前项；不是精确Bayesian posterior，也不授LLM批准effect。累计summary可漏压/污损，metadata/provenance及确定性sink/arguments仍独立。

Table3 stateful差额56.7→30.3、同stateful多stage43.9→30.3；stateless final-only †56.7没有实测，所以不能称完整实测2×2或已证明super-additive。Table2 B1全配15.7与Table3 ablation30.3不混为同设置。四backbone保护主agent，但trust/judge主体GPT4o同源；人工750审计B3仅85%agreement，不能用整体95%签安全。B4仍63.5%ASR，meanlatency2.59→8.64s=3.34×，全文6.50×是surface factor无权均值不是全流量概率。

Books：Ch72 1641–1676已含trajectory riskstate、2913–2922已有crosssession状态/相关防御。拟Existing或仅把“固定格式跨checkpointsummary压缩及不是posterior”补入现风险state段；不存在全新stateful安全owner，暂不为未见此论文名申请Integration。
