# Visual-ERM 13224：本17必要证据与受限差额

root 仅处理03-17补03-16自然日，复用本日完整v1题摘/日期校准，不扩来源或调整旧候选。2+2+2=6，渲染消费者奖励的具体长期接口缺口深入。实际读[exact-v1](https://arxiv.org/html/2603.13224v1)§3–4/Eq1–10/T1–5/A1–4及直接反侧B1/B3–6；未核代码、复現或定性图像。不是把 benchmark 名称或泛 reward hacking 计增量。

## 支持与边界

代码候选先由任务renderer转可见图，再由pair-image generative judge报告位置/类别/严重度；distillation同时使用编辑负例与实际模型错误，训练RM再供GRPO和修订。可渲染分与视觉差异分是两路，奖励max归一的实际集合/时序未闭合，不据此补全数值recipe。可见相同不证明底层数据/代码语义或任意交付可维护性；引用图也不是独立现实真值。

Qwen3-VL-8B RM/默认policy、VinciCoder第二policy；RM三类共340K/3epochs/B32/lr1e-5，RL11K/40K/10K/B256/G8/lr1e-6。核心表支持受限收益，但Qwen SVG的DINO综合71.0高于Visual-ERM68.3，TA加RSR78.1低于不加79.0；四轮反思比三轮退步，部分VQA切片也降。弱平均/演示不支持必要充分、全面优胜或免费迭代。judge换模型仅限同prediction的错误匹配，相关分不依赖matcher；标注、训练、RL和评测来自同底层数据源，独立切分/污染身份未完整披露。硬件、精度、runtime精确版本、完整输入输出长度/并发/SLO、重复训练CI、renderer规格/失败fallback与所有制备/调用成本未齐；不授公平总预算、生产或复现。

## owner 与逐字 PRE（未写、待独立复核）

实际 Ch31 多目标/rubric分工261–283，特别是文本judge不能重新看原图的边界；Ch66 artifact渲染/原生编辑及Ch33组内算法职责已有。唯一 `TRAIN-RLHF`，新增命题是将奖励的观察位置由文字/抽象相似度移至renderer后的实际消费者视图，并保留渲染有效与内容差异两个判据，不新增第二评测/GRPO owner。拟插原format-decoupled两个段落之后、adaptive controller之前：

> 若目标是重建图表、表格或向量图，文字结构匹配还会漏掉消费者真正看到的间距、数值和形状。另一条奖励分支先将候选代码或 markup 渲染，再让视觉 judge 比较参考图与输出图，生成位置、类型和严重度反馈；这些反馈可用于训练，也可指导有限轮修订。可渲染性与内容相符必须分开，视觉总分既不是代码语义真值，也不能批准原生对象可编辑。[受限渲染奖励对照](https://arxiv.org/html/2603.13224v1)还显示不同任务/基础policy的代理排序会反转，不能由一个均值选择所有任务的reward。<!-- source-family:SF-2026-ARXIV-2603-13224 -->

> Renderer、参考图、错误分类、标注与judge版本应随奖励保留，原生结构及独立任务结果另验；教师合成错误与实际policy错误须覆盖不同人口，教师一致也不等视觉真值。制备、渲染、judge生成、额外修订与训练均计费，更多反思可能退步，组内或任务级归一也会改变奖励尺度。观察资格、参考对象或净收益不成立时，保留已校准的结构/相似度指标、固定预算和独立人工检查，而不是以“可解释反馈”宣称消除hacking或充分保证质量。<!-- source-family:SF-2026-ARXIV-2603-13224 -->

静态来源注拟稿：`SF-2026-ARXIV-2603-13224` — [exact-v1](https://arxiv.org/html/2603.13224v1)§3–4/A/B3–6；只采用renderer后观察/两路reward及反馈接口，保SVG对照、反思退步、共享数据/归一与全成本边界。不授必要充分、代码语义、所有任务优胜、复现或生产保证。

## 非准备者必要 Source / PRE（resume_mar17）

压缩恢复实际重载本日合同、来源分组、ROADMAP及本日停点。独立读取v1§3–4/Eq1–10/Tables1–5、A1–4/B1/B3–6的拟采用接口与直接反侧，实际Ch31 255–279完整奖励观察/format分工→controller邻接、Ch66渲染/原生结构及Ch33算法边界。两逐字PRE与静态注通过：renderer后观察、可渲染/视觉差异分责和有限修订是新差额；不采Eq7归一集合/时序的精确recipe。保Qwen SVG DINO71.0优于68.3、RSR TA79.0→78.1、三/四轮81.1→80.7等反退。共同数据源、三模型注释和实际人工consolidation不证明独立truth；共享教师/判分及完整费用/运行配置边界保留，不冒全部附件/像素、代码或复现。

root随后授Ch31两段及静态注窄锁；作者按逐字PRE写入，未新增动态验收身份注。actualPOST须由非writer root执行后才能计实际整合，尚不授DAY。

## 非写入者 actualPOST（root）

实际回读 Ch31 251–294 完整 rubric/format → renderer → adaptive controller → gradient-space 邻接，以及章末本人1471与SteerRM邻注；新275/277逐字等于通过的两PRE，唯一来源注准确保留精确v1与采用边界。正文把奖励观察对象的变化接回类型判据，未将render success、视觉相似、原生编辑或语义真值混同；反侧、费用与回退位于机制旁。没有过程身份注追加或其他family改写。actualPOST PASS，Ch31窄锁释放，允许本family计实际整合；不代替整日日级验收。
