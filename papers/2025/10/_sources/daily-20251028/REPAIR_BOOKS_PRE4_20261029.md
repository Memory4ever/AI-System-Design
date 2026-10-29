# I21–I26 完整窄稿

仅以下单段/独立marker/本人注；完整直接两侧见context4，必要层复用R20，未经整体PRE不写Books。

## I21 MULTIMODAL-GENERATIVE-PARADIGMS / GFM

文件：`books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md`；Any-step两段后、一步质量档位前。

```markdown
少步flow map迁往旋转、双曲空间等非Euclidean状态时，跳转还必须服从几何：以exp/log构造路径，用切空间投影、metric距离和differential定义目标，而不能把坐标线性插值直接当合法状态转移。[Generalised Flow Maps的受限分支](https://arxiv.org/html/2510.21608v1#S3)依赖光滑、well-posed的流和所用exp/log有效域；cut locus、全局唯一性、离散实现误差不能由局部目标自动解决。不同self-distill目标还要求相应stop-gradient/JVP接口，SO3/Poincare对照并无统一NLL赢家。全部几何运算、teacher/自蒸馏训练、JVP与数值回归计费，低NFE不等低墙时；有效域、几何或预算不合时，保原数值solver、较短跳转与已验Euclidean表示，不由任意步数名称签发任意空间的精确全局流。

<!-- source-family:SF-2025-ARXIV-2510-21608 -->
```

```markdown
- `SF-2025-ARXIV-2510-21608`：Daily2025-10-28补Oct27；exact-v1必要层、2+1+2=5，R20通过。仅Riemannian flow-map几何/微分接口与域，不扩AIforScience应用；保各目标反退和全部几何/JVP费用，未核实现/复现，完整PRE/SAVE/自读/solePOST据本日实际层。
```

## I22 AGENT-REFLECTION / HGM

文件：`books/part-07-agent/80-reflection.md`；参数adaptation边界段后、Feedback来源节前。

```markdown
若改的是Agent程序，搜索还要区分当前版本得分与它产生更好后代的潜力：维护版本谱系，以clade内后代成功/失败估计继续扩展的价值，再把预算分给值得探索的祖先，而不只复制当前最高分者。[Huxley-Godel Machine的受限分支](https://arxiv.org/html/2510.21614v1#S3)中的经验clade均值不是已知真实改进概率；选择偏差、共享后代与任务重叠会影响它，理论的terminal utility、可重复试验、免费证明和固定修改费也不是开放工程环境默认条件。代码诊断、全部失败版本、后代试验/验证及模型API均计费，allocated CPU时数不能代完整费用。谱系估计、独立任务或执行安全未验时，保原版本、固定预算局部修复和可信测试/人工审批，不由后代高分批准自改安全、形式最优或普遍持续改进。

<!-- source-family:SF-2025-ARXIV-2510-21614 -->
```

```markdown
- `SF-2025-ARXIV-2510-21614`：Daily2025-10-28补Oct27；exact-v1必要层、2+2+2=6，R20通过。仅当前fitness/后代潜力与谱系预算分责，保理论oracle条件、测试重叠和API全费；未核执行/实现/复现，PRE/SAVE/完整自读/solePOST据本日实际层。
```

## I23 MULTIMODAL-GENERATIVE-PARADIGMS / Epipolar preference

文件：`books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md`；metric-geometry完整末段后、可微视频反馈前。

```markdown
几何反馈也可以不用另训物理判别器，而在同prompt生成的视频之间，以特征对应和RANSAC估计的epipolar误差提出偏好，再用temporal variance抑制静止捷径。[受限epipolar preference分支](https://arxiv.org/html/2510.21615v1#S3)只在静态场景、运动相机及可靠对应下赋予单一fundamental matrix意义；独立运动物体、非刚体和跨prompt绝对误差不能继承相同资格。DPO是消费这些排序的一种选择，不是不可微reward只能这样优化；更低几何代理也不认证真实动力学。全部视频生成/筛选、特征匹配、偏好训练与reference forward及独立几何/外观回归都付费。静态前提、对应或最终质量不合时，保原监督生成、可信多视几何与独立检查，不把经典几何公式当通用物理真值。

<!-- source-family:SF-2025-ARXIV-2510-21615 -->
```

```markdown
- `SF-2025-ARXIV-2510-21615`：Daily2025-10-28补Oct27；exact-v1必要层、2+1+2=5，R20通过。仅条件epipolar偏好/静态捷径/最终资格，不采单F泛化动态物体或DPO必要论；保生成/过滤/reference全部费用，未核实现/复现，完整PRE/SAVE/自读/solePOST据本日实际层。
```

## I24 TRAIN-SFT / CoD

文件：`books/part-04-training-system/29-sft.md`；teacher数据成本段/marker后、程序student段前。

```markdown
固定蒸馏样本总量时，也可把部分名额留给决策边界附近的输入：保留一半原例，让LLM提出另一半反事实，再由teacher确认其标签发生翻转，训练较小student。[CoD的受限对照](https://arxiv.org/html/2510.21631v1#S3)新增的是输入边界覆盖，不是teacher翻转就获得真实语义标签；最近反事实、全边界覆盖和跨生成任务迁移都未由有限二分类实验建立。标量`p(1-p)`较大也不单独推出带`xx^T`的Fisher矩阵普遍支配，不把该印刷论证当无条件样本效率定理。Teacher全量训练/前向、LLM造例与验证翻转、失败例筛除及student训练均付费。反事实有效性、覆盖或总预算不合时，保可信原例、普通KD/直接监督和独立真标签，不由少量边界样本批准无偏迁移或完整边界恢复。

<!-- source-family:SF-2025-ARXIV-2510-21631 -->
```

```markdown
- `SF-2025-ARXIV-2510-21631`：Daily2025-10-28补Oct27；exact-v1必要层、2+1+2=5，R20通过。仅固定k的反事实边界补样/teacher验证权限，保FIM方向与Hausdorff全boundary前提不自动成立和全费；未核实现/复现，完整PRE/SAVE/自读/solePOST据本日实际层。
```

## I25 MULTIMODAL-GENERATIVE-PARADIGMS / WorldGrow

文件：`books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md`；masked schedule基本段后、region并行段前。

```markdown
已知/未知边界也能组织静态三维场景，而不只填固定序列：把空间切成重叠block，以邻块为条件inpaint，先生成coarse layout，再细化结构与SLAT外观，按遮挡重聚合多视特征并适配scene decoder。[WorldGrow的受限分支](https://arxiv.org/html/2510.21682v1#S4)中，单换aggregation反而退步，说明object prior迁到scene仍需decoder联合训练；可沿XY继续扩块不保证全局一致、任意垂直扩展或无限质量。它没有action-conditioned动力转移，静态画面不能冒称第25章的可用world model。全部场景制备、codec/生成器训练、重叠重生成、块数存储与完整场景回归均付费，单block时间不等任意大场景deadline。跨块布局、遮挡或预算不合时，保有限场景、较大共同上下文与独立几何检查，不由unbounded名称批准物理、全局语义或无限扩展。

<!-- source-family:SF-2025-ARXIV-2510-21682 -->
```

```markdown
- `SF-2025-ARXIV-2510-21682`：Daily2025-10-28补Oct27；exact-v1必要层、2+1+2=5，R20通过且按机制纠正唯一owner为Ch24。仅静态3D重叠inpaint/scene decoder适配，保单换aggregation退化、XY与总费用，不采action dynamics/unbounded保证；未核实现/复现，PRE/SAVE/完整自读/solePOST据本日实际层。
```

## I26 MULTIMODAL-GENERATIVE-PARADIGMS / MRO

文件：`books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md`；SDE-consistent完整段后、metric-geometry节前。

```markdown
去噪时更频繁地评分，还须区分过程代理与终局资格：对当前预测计算一致性/任务proxy，可帮助安排搜索和reward调用，却不能把每个中间分都当新增独立真值。[MRO的受限分支](https://arxiv.org/html/2510.21473v1#S4)在搜索中用majority pseudo-gold，训练真label另属不同权限；减少打分频率也不等取消条件采样或所有生成费。将非负reward写成potential差，并不能在边界/条件未闭时直接继承均值不变或方差必增的结论，故只保留评分调度设计，不采用该普遍理论recipe。全部候选、proxy、终局评价与训练/搜索回归均计费；代理、累计目标或质量失配时，保完整终局reward、固定频率与原sampler，不由过程分更高批准答案正确或净省算。

<!-- source-family:SF-2025-ARXIV-2510-21473 -->
```

```markdown
- `SF-2025-ARXIV-2510-21473`：Daily2025-10-28补Oct27；exact-v1必要层、2+1+2=5，R20通过。仅proxy/终局资格/评分调度分账，不采未闭potential/方差recipe；保pseudo-gold/真实label权限与全费，未核实现/复现，完整PRE/SAVE/自读/solePOST据本日实际层。
```

## 作者整体自读

六份完整新增、独立marker、本人注和完整前后段均已读。WorldGrow只写静态生成owner；BachVid/FlowSynth已有具体论证覆盖另见coverage稿，不为凑段数整合。此稿不授DAY。
