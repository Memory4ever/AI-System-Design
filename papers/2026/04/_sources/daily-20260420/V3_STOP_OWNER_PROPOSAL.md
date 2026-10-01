# STOP：并行前缀评分的状态隔离窄提案

作者：apr20_resume。6分（2+2+2），因实际owner缺口定点深入；尚未获source→owner独立采用/写锁/真实写后，不计整合。源：[2604.16029v1](https://arxiv.org/html/2604.16029v1) §3.2与F.2是状态机制owner，§4.1/5.1/5.2、B.3/C.1–4/D/F为评价与直接反证。必要证据见本日v3-reopen-notes最新批。

## actual owner及相邻

MODEL-SAMPLING，Ch20“从请求级Budget到轨迹内Feedback Control”当前已说明checkpoint-relative内部sensor、硬外层资源budget与错误confidence。但其实际段落以单trajectory双向控制为主，尚未解释并行前缀评分时，评估adapter/check token与正常续写状态分离的具体分支。Ch79已有外部evidence/remaining-budget树搜索，本次不重复planning tree；Ch19/45拥有KV存储/物理cache，Ch20只拥有选择时不污染base轨迹的语义边界。拟放在该小节末、下一token sampling小节前，承接singletrajectory并行区别。

## 两段拟正文

单条轨迹的 feedback controller 只决定继续或停止；并行轨迹还需要决定哪些前缀值得支付剩余生成成本。外部 verifier 可以读取文本，接口清晰且不要求修改生成模型，但会重新编码前缀并增加独立模型成本。能读取内部状态时，一个替代分支先由冻结的 generator 生成多条前缀并保留其 KV，再在每个前缀的临时评分分支中追加专用 query token，只在这一步启用评价 adapter 与分类头。评分结束即丢弃临时分支，保留下来的轨迹从原来的前缀状态恢复生成；评价 token 和 adapter 派生状态不成为 base continuation 的已提交前缀。这里的分数估计“给定当前模型、前缀和采样规则后完成正确的概率”，可以用多次 continuation 的成功率训练，却不是证明轨迹逻辑有效的 verifier。

这种状态隔离用新增评分参数、Monte Carlo 监督构造与一次局部 forward，换取少完成一些低价值路径；它没有使评分和训练免费。固定前缀长度会在识别错误的可靠性与已经支付的生成成本之间取舍，错误剪枝还可能删掉后续能自行修正的路径。验收应分别记录初始路径数、保留数、前缀长度、selected-path 平均正确率与最终 query-level success，并把 check、临时 cache、恢复与吞吐影响计入总预算；分数较好、评分时延较低不等于端到端成本一定更低。现有证据支持若干数学、逻辑和受限工具任务的单阶段过滤，不证明经验保留率拟合跨任务普适、attention 图揭示必要推理机制或生产 tail SLO。无法访问内部状态、评价 adapter 漂移或剩余预算不足时，随机保留、固定宽度完成与独立文本 verifier 仍是共存路径。[受限状态隔离与评价证据](https://arxiv.org/html/2604.16029v1)

## 不采用/不写入数字的理由

F Table16单H1007B/b16/prefix2048：verify .20s/.59%，total34.33>33.20、throughput−2.71%；“nearzero”不能写成零端到端成本。B Table11估算8×H100墙钟MC构造43.08–75.93h不是全training GPUh。20B rank2048及更大模型数据支持不同，不称全部module极小。attention可视化不证明logic必要因果，Eq7两任务1.5B经验拟合不作理论定律，竞赛120B的未披露量化/精度不补造。正文仅采用有原文依据的read-only prefix/temporary view机制和失败边界，不声称实现复现。

## 待核

非作者核官方§3.2/F.2与actual Ch20相邻，确认两段确实是该owner机制增量；若现正文已有具体temporary-check/resume分支，则改窄Existing，不为新名字强写。通过后仍需root授窄锁、作者真实写入及独立写后，不预支I。

## 实际写后复核

apr02已完成必要源→actual owner/literal非作者核，root据未变结果授窄锁。作者实际写入后，root顺读Ch20:224～246及Review:491：已有checkpoint/sensor资格→两段临时check分支丢弃、恢复base continuation→Semantic Steering→Parallel Sampling的衔接成立，没有将评价adapter状态提交为生成历史或把MC概率当逻辑验证。额外训练、误剪枝、前缀成本、端到端吞吐可退与替代路径就近保留；Review位于章末、来源和exact-v1清楚。实际写后独立通过，可登记本项真实整合；未签整个Apr20来源/日期或日Gate。Ch20窄锁已释放。
