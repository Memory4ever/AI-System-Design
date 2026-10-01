# FineSteer 15488：有限 source→owner 采用提案

作者apr20_resume，未写Books。必要原文[精确v1](https://arxiv.org/html/2604.15488v1) §5.1–5.3/Eq6–15、§6.1–6.5/§9及唯一必要A.1已实际读，详细反证见恢复记录“其后五项有限必要审阅”。`2+1+3=6`，因实际owner缺口深入，不因安全标题普遍Deep。当前Ch72“Privacy 与 Unlearning 都需要输入条件化 Gate”有抑制≠删除、gate漏检、旁路/utility验证，但没有把when判别与how干预分离为可训练的prototype组合；只请求这个差异，唯一owner `PLATFORM-SECURITY`。

拟在该节 activation redirection 段之后、现有“攻击与 unlearning 的所测模型范围有限”之前补两段：

> 输入条件化干预还可以把“何时启动”与“如何改变”分开。一个受限分支先由目标样本建立 mean-centered PCA 子空间，用输入 hidden state 在其上的相对能量作为 gate 线索；再由固定 prototype bank 和训练过的 query/key attention、残差映射，组合当前输入所需的干预，而非给所有请求添加同一向量。prototype 固定不代表整个 controller 无需训练，能量比也不是已校准的有害概率或因果判据；one-class quantile、监督 logistic gate 与直接 soft 能量 gate 是不同方案，不能混作统一实现。
>
> 分离选择与干预可减少无关请求的损伤，却增加样本/子空间构建、controller 训练与每token运算，并依赖概念support可分。保留gate漏检、prototype覆盖不足和adaptive请求压低gate信号的旁路；一个质量指标的改善不能替代truth/安全与utility分别验收。[FineSteer]在三个模型family、3–9B和受测攻击/TruthfulQA上支持有限选择，ablation也有完整方法的truth分低于移除一个组件的切片；不是全指标最优、零成本或开放攻击保证。条件不适用或独立验收失败时保留固定/更轻干预、访问控制或权重级方案，行为抑制不获得删除权。

证据限制：PCA/固定Kmeans bank后WQ/WK、residual MLP需要训练；Eq8/9/15三种gate说明不静默修复。Qwen7B w/o SCS GSM34/full95/base97，但Truth54.77 w/oSCS高于full54.28，w/oMoSE50.86只支持有限取舍。A800每token40.43 vs Alpha40.38非零代价/production p99；113s训练并非快于Alpha70s；BiPO284.7GB为四卡累加不能当单卡峰值。A.1不同task层及soft监督default、§9 adaptive攻击风险原样保留。不拟采用所有speedup、全部攻击排行或“SER识别harm”的普遍主张，因此不展开全附件/复现。

拟新增Review note只指上述必要源、实际位置与独立source→owner及写后真实状态；尚无写锁/独立PASS，不预支整合。其余日20普通审阅继续。
