# Apr24 三项有限非作者采用复核

复核者：`apr02`（非 Apr24 报告作者、未写这三项 Books）。范围仅为作者现有 literal、必要官方 v1 方法与关键评价、ROADMAP owner 和当前实际正文；不是日期、来源覆盖或日级 Gate。未复现实验，未修改 Books 或作者报告。

## 21741 — Hi-WM → MULTIMODAL-EMBODIED-VLA / Ch26

**结论：最窄 source→owner 与 literal 采用通过；仍需授权写入和实际写后复核。**

以 [官方 PDF v1](https://arxiv.org/pdf/2604.21741v1) 为准，实际读 §3.5、§4.1–4.4 和 Table2。HTML 页内日期出现 Aug24，不用它冒称精确 v1 身份；PDF 首页载明 Apr24、arXiv v1 页眉 Apr23。本次只定点恢复版本身份，不由这两个字段独立证明日报归属。

缓存失败前模拟状态、人工短纠正后交还 policy、分支片段与真实示教混合 posttrain 的分工可核实。Ch26 当前 human-online-RL 段负责真实环境中的更新面和 critical-phase handoff，尚未承载把纠正采集移入 learned world model 并复用缓存分支的这一条件路线。作者两段将预测状态与真实环境可回滚性分开、将生成数据与物理事实分开，具体增量成立。

证据限于三任务及所测两类 policy。WMCL 对照没有单独隔离 rollback 的因果收益；有限相关系数不保证全部失败状态可信，PushT 的十分钟边缘覆盖讨论也不应写成全面定量校准。现 literal 已保留真实机器人验收、支持分布、额外训练/人工/发布成本、保守控制与真机纠正回退，未采用模拟成功等同安全或预算估算等同真实部署成本。

## 21632 — To See the Unseen → MODEL-EMBEDDING / Ch12

**结论：条件化 source→owner 与 literal 采用通过；不采用无学习率限定的普遍收缩定理。**

实际读 [官方 HTML v1](https://arxiv.org/html/2604.21632v1) §3–6、AppA 的更新式与 AppE 反例。Ch12 当前 tying 段解释共享布局和参数节省，Padding 段解释输入/loss mask；二者未表达未作为正确 label 出现的输出行仍受 softmax 归一化梯度影响，以及共享行区分度与 copy 读出职责不同。

有限 GD/SGD 的 bounded-feature、小步长和 decay 条件可支撑窄分支，不能由它直接担保 AdamW。未限定学习率的 norm 上界存在简单反例：令特征为零、η=3、λ=1，行差更新为 −2Δ，范数为 2‖Δ‖，而打印界的右侧为 −2‖Δ‖。这只否定未限定版本，不否定实测 collapse 或小步长条件的讨论。

作者 literal 已保留该前提、copy 不自动恢复输入区分度、freeze/reset/diversity 各自职责及 C4 loss 退步，不把 unused-row 相似度当推理失败唯一原因。适合嵌 tying→训练支持→局部干预的原有链路，不需要整表永久冻结或新增论文摘要。

## 21724 — Beyond N-gram / X-gram → MODEL-EMBEDDING / Ch12

**结论：最窄 source→owner 与 literal 采用通过；不采用零执行成本或所有扩容单调改善。**

实际读 [官方 HTML v1](https://arxiv.org/html/2604.21724v1) §4.1–4.5、Algorithm1、§5 的主要配置和反向结果。频率估计→专用高频槽/平衡尾桶→alias 或多路径 hash→causal 局部 extractor→按层 value/residual 注入为可核机制。当前 Ch12 Hashed N-gram 段已有 collision、hot-entry skew 与容量 frontier，但尚未把训练更新频率、row 分配与读出后动态 extractor 联成同一分支。

当层 value 注入与当层 Q/K 不变不能外推后续表示不变。literal 已保留联合 table/hash/extractor/gate 身份、参数与 host/device 搬运成本、2×/4× 非单调与层位参数量混杂；带宽预取估算不当在线 wall-clock 或 SLO 证明。现有静态 lookup 仍作为预算/词法短路风险条件下的简单分支保留。

## 交付边界

三项均是拟采用命题与实际 owner 的有限独立通过，不是已 Integrate；没有共享写锁或实际新正文，本文件不支持计入真实 Books 产出。日期联合依据和日级终核仍由 Apr24 作者/root 完成。正文写入后仅重新读变化段及邻接，不要求重复全部必要源。
