# 03-25 补查首批准入提案（待独立校准）

仅补2026-03-24北京时间完整自然日。旧候选整行/日期/评分/原窗口与连续§4冻结，baseline保存。四title查询是有限主题发现，submitted buffer仅用于发现，不直接作为公开日期。原字段见 SUP_DISCOVERY_20261012.json；以下完整exact-v1题摘及日期原值见 SUP_FIRST_ABSTRACT_DATE_20261012.json。未授 PRE/POST/DAY。

## 日期依据

arXiv官方 availability 的no-advance与announcement schedule提供该提交批次常规最早公开03-24 BJT08的下界（Friday14 ET之后至Monday14 ET）；arxiv-owned findable DOI registered 为已经公开的上界而非首次公开时刻，秒精度上界加1秒。六拟入选项各自 Submitted/history及registered原字段相互对应，registered均03-24 UTC03:40～04:04，即BJT11:40～12:04，日期区间全落03-24自然日；不生成确切08时刻、不把created/updated等同first-public。没有当前可见撤回标记；v1题摘不被latest标题/结果覆盖。该日期方法待root校准。

## 拟入选

| v1身份 | 约束 → 实际新增 → 改变选择 | 拟分 | owner方向/必要证据 |
| --- | --- | --- | --- |
| 21257 CALVO | remote prefix高命中仍受KV网络loading约束 → loading与GPU计算各自异步推进并把load delay显式计服务成本 → 调度不能只看GPU队列 | 2+2+3=7 | INFER-SCHEDULING，深审load stage及端到端SLO控制/反例，不采用61.67%裸数字 |
| 22206 Chimera | 同构副本假设忽视heterogeneous multi-stage workflow质量/拥塞 → joint semantic confidence、remaining workflow tokens、inflight predicted volume → 把workflow剩余路径纳入routing/queueing | 2+2+3=7 | INFER-SCHEDULING；深审confidence与length模型、等配置baseline及准确率/尾延迟取舍 |
| 22075 AR vs MDLM |范式比较常被数据/预算混杂 → 相同TinyStories/steps/batch/seq/hardware下收敛与diversity-fluency差异 → 不用单一throughput推同等质量成本 | 2+1+2=5 | 标准审阅；MODEL/生成边界，单小数据集不外推长程系统普遍律 |
| 22248 Confidence decoding | 经验confidence并行unmask缺理论效率边界 → entropy-sum threshold与KL采样精度/expected iterations上界 → 低entropy条件何时支持并行提速 | 3+1+3=7 | MULTIMODAL-GENERATIVE-PARADIGMS；深审oracle假设、ε/entropy定义、误差及无hyperparameter宣传边界 |
| 22117 RLVR Direction | sparse变化只看magnitude可能丢符号 → signed Δlogp与token replacement intervention及extrapolation/reweighting → 用direction而非entropy相关挑关键更新 | 2+2+3=7 | TRAIN-GRPO；深审干预对象、预算对照、transfer/失败条件 |
| 21972 Long-horizon RL recipe | reward/algorithm常用统一recipe → TravelPlanner受控五轴显示model scale/difficulty mixture/environment stability交互 → reward和exploration选择按能力/环境条件校准 | 2+2+2=6 | 标准审阅；安全/设计反证若采用加深具体段，不外推1K最优到其他Agent |

## 代表负侧

20397 KV review 完整题摘是五类优化/七部署场景综述，未识别新增反证、控制混杂或具体失效条件修正，不因survey类型一律排除。21354 WRP完整v1题摘将该项目既有工作放入3×3 matrix和研究方向，未披露新的验证机制/具体反证，不能把跨层术语当增量。21408 CGFormer完整题摘是无线信号插值目标及environmental embedding/crossattention的领域指标改善，未支撑foundation/model系统设计增量；不因所有优化理论领域研究都排除。

## 普通下一步

1. root独立准入校准以上六拟入选与三个负侧及日期方法；作者不自授PASS。
2. 其他有限标题仅发现线索，未把所有条目当mandatory全文池。潜在相关者仍须完整题摘后判断；未读不标外部受阻。
3. Anthropic 正确harness-design-long-running-apps dated Mar24核心已读，含sprint pre-negotiated contract、runtime evaluator及按模型移除reset/sprints的具体实验变化；不把新三persona组合本身当增量，待必要日期原字段与贡献处置。无Books写锁或实际写入。

## root独立首批准入校准

2026-10-12实际逐项完整读原JSON九份exact-v1标题、摘要、history与arxiv-owned findable/registered原值；重新打开官方availability的公开过程、不得提前分配ID/DOI及Friday14→Monday20公告表。六潜力项的常规最早公开下界与已有公开上界均在03-24北京时间自然日，足作日归属，不把Submitted、Updated、registered或08点单独冒充首次公开时刻；有具体早稿信号时仍需定点去重，不授互联网无先稿。

六准入理由均指出实际待验证增量：KV loading自治与成本、异构workflow剩余tokens/quality、范式比较的配置边界、entropy累计unmask的假设/误差、signed update干预与利用、reward/scale/environment交互。不是映射节点或组合模块即收；22075的“sole variable”只是待核主张，正文所发现参数与采样差异须约束因果结论，不能为避反证缩池。既定拟分与审阅深度可继续，Books owner/收益仍由必要证据和实际章节决定，未授PRE/POST或DAY。

三个具体负侧支持原EX：20397整理已有KV类别和部署场景，未识别新反证；21354以已有项目结果归纳矩阵和研究方向，不把术语当新机制；21408的radio-map插值/embedding局部提升尚不能改变大模型或其Infra设计。负侧不以survey或领域词机械排除，可读题摘若出现具体系统增量再重开。首批有限准入/日期校准PASS；四查询是有界查漏线索，不变成逐项全读队列，亦不授来源无遗漏。
