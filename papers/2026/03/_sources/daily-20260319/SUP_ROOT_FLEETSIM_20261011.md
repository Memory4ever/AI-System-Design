# 03-19 补查：inference-fleet-sim 必要判断

root 接作者明确尚未审阅的 `2603.16054v1`，仅本19新增03/18自然日。完整题摘/当前官方 history、Comments 已实际读 `SUP_AB_16054_20261011.json`；不是256标题库存的全读，不将后批metadata自动准入。日级夹证字段复用本日保存metadata与首批准入同口径，Submitted不单独充当公开日。

## 准入与必要证据

[exact-v1](https://arxiv.org/html/2603.16054v1)，实际读 §2–3/Eq1–6、§4/T1–9与 §5 必要限制。新问题不是通用 M/G/c 名称：单 engine 配置不能决定多池总容量，解析两矩模型与 request-level DES 是否会对重尾/路由/硬件组合作出不同 SLO 判断。原文提供两阶段规划和具体反例潜力，准入 **2+2+2=6**；评价中心冲突使受影响主张深入，未读 GitHub全部实现或复现实验。

解析阶段联合扫描 split、GPU类型、两池大小，以长度CDF/服务均值与方差估计 TTFT；top-k再由arrival/completion事件仿真检查。GPU W/H/nmax是手校常数，原文目标Llama3-70B single-node TP，A10G/A100/H100配置与不同长度池；LMSYS/Azure只复用长度人口，agent-heavy为合成，不是恢复真实到达序列。Poisson/i.i.d lengths、静态slot上限及线性iteration模型均限制外推，DES不模拟preemption、token batching reorder、speculation、多节点collectives；推测输出长度/TP物理卡数与模型驻留、precision、完整内存预算、真实GPU端到端验证、重复run误差/并发SLO部署资格未闭合。价格为illustrative/profile默认且可改，不采普遍采购排名。

## 中心评价冲突，不写 Books

§3.1 的接受规则明确为 **P99 TTFT≤T**。但 §4.5/Table5 在 T=1000ms 时，CompressAndRoute P99=534ms、99.94%满足，却标“FAIL”，并由此推导 sizing router 应与 production router 不同；另两行495/292ms分别通过。这不能由该声明的P99规则支持，不应自行猜成P99.99、更严SLO或压缩语义质量门。

§4.1/Table1 的LMSYS/100reqs/A100/500ms、8GPU all-A100行标SLO通过；§4.6/Table7同名人口/8GPU all-A100报告longpool2822ms失败。未给足split或配置差异来对齐，不能合并其43%节省与另表拒绝条件。§2Eq4以slot上限摊薄service、§3.1 request级事件模型和§4.2所谓actualarrival sequence亦需明确哪些是假设、哪些真实回放；DES与解析共享profile，不是独立实机正确性验证。直接中心冲突已足够，停止，不为找理由遍附录/旧版。

实际读取 `INFER-SCHEDULING` Ch56 **44–78/190–206**、Ch55/Ch70开篇交接：长度/服务率/容量、预测误差及保守admission、阶段奖励和稳态不授tail均已存在。它们保留，不把现有机制名字当新增差额，也不将中心未成立命题窄写成“DES权威”案例。

建议 **暂缓／中心争议**，不是贡献EX、降分或用已有覆盖消除反证，Books新写0。只请求一次精确重开材料：Table5实际SLO判据与分母、T1/T7各配置/split/人口和simulation预算、request-service/TTFT计量及与实测或独立profile的校准。缺该材料不采用其安全/性能/采购保证；支持读完与日级归属仍须非作者正式复核，本笔记不授DAY。
