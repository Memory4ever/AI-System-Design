# 04/28 两项 MoE 的非作者有限复核

复核者：root；作者提案：apr02。此页只裁决贡献与 owner，不替代本日日期、全日分母、证据或 Books 写后 Gate。

## 2604.23108v1：保留窄贡献线索

- [官方 exact-v1](https://arxiv.org/html/2604.23108v1) §3.1–3.4、Tables 1/3 实际支持：不同宽度 expert 先按组选择、再在组内打分并全局选 expert；all-size set 让每个设备持有各宽度的一个 expert。静态参数均匀只是 placement 性质；动态计算均衡还依赖组内路由负载。论文用频率/困惑度替代 token difficulty，没有独立语义真值；Table 1 也非相同 total/active 参数或 FLOPs 的单变量比较，Table 3 是路由比例而非生产 GPU 利用率。
- [Ch21](../../../../../books/part-02-model/21-moe.md) 已有总/激活参数、router/placement 分责和负载代理，但没有说明“异宽模型结构与每设备跨宽度组合布局必须联合设计”这一受限分支。主 owner 为 `MODEL-MOE`，训练/推理运行时只交接可执行布局。不应写成精确识别难度或保证均衡。
- 裁决：作者侧保留潜在贡献成立，待 first-public 与日期 Gate 后再定最终评分和 Books 决定；此处不预先计入正式候选。

## 2604.23150v1：保留，但纠正 owner 与机制表达

- [官方 exact-v1](https://arxiv.org/html/2604.23150v1) §3.3.3、§4.1–4.3、§5.2–5.3 实际支持：prefill 逐层 expert activation 与 decode activation 的相关度因模型而异；历史 decode activation 先用于 request clustering，再按 cluster 的逐 expert 使用量把相关 experts 放在更近的节点。这里不是直接用一张 expert-pair 共激活矩阵决定 placement。`.94` 是 DeepSeek-V3 所测 Layer 42、DP8TP8→EP64、500 global batches 的中位归一化 All-to-All 数据量；Llama Maverick 的约 5.5% 仅为所测 layer runtime，padding-to-max 的通信 kernel 吞掉部分数据量收益，均非端到端请求 SLO。
- [Ch56](../../../../../books/part-05-inference-system/56-inference-scheduling.md) 现有 prefill signature→locality routing 段已经承载 request clustering、decoder mapping、load/locality 冲突。该论文可能增加的窄点是：placement 不能只按各 expert 全局热度，要按被分到同一 request cluster 的条件使用量规划节点，并分别验收传输字节与 padding 后层时延。`TRAIN-DISTRIBUTED-TRAINING`/Ch36 不应是主 owner；它处理训练并行，而本论文是分布式 decode。主 owner 候选为 `INFER-SCHEDULING`/Ch56，Ch21 仅 handoff。若现有 Ch56 文本进一步对读发现此条件已被等价表达，可转 `No Change — Existing Coverage`，不能为写 diff 强行重复。
- 裁决：保留潜在贡献、owner 纠正；待 date Gate、最终评分和实际正文差异复核，不预称已整合。
