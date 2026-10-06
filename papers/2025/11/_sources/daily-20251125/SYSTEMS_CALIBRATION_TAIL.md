# Nov25 系统切片尾部校准

仅从本日原始主题线索定点选四项，不把88标题或宽月表转为逐项全文队列。实际exact-v1完整题摘均在raw-four-systems-exactv1-15.json；其中AMD/PyTorch此前Atom给latest-v2，只用于发现，这里已纠正为v1，不用后来版本补本窗。有限具名日期查询原参数与返回见raw-four-systems-date16.json/raw-four-systems-primary17.json。

## 准备好的AMD单项日期与拟命题

[Training Foundation Models on a Full-Stack AMD Platform](https://arxiv.org/abs/2511.17127v1)明确MI300X/Pollara collective与kernel表征、hardware-aware attention/MLP/MoE sizing及checkpoint reshaping；原先统一并行/模型形状判断→作者给出具体硬件操作区间与通信条件→需重新核并行分组、expert宽度与保存路径。不是仅“又一个模型跑分”或换vendor名称，拟2+2+2=6，标准必要审阅；若准备采用评价/故障归因则定点加深。不采用“frontier生产成熟”“比NVIDIA普遍更好”等宣传。

日期不再只有submitted：实际[AMD原新闻](https://newsroom.amd.com/news/amd-powers-frontier-ai-training-for-zyphra/) L76～86明确本日technical report published today并链接此论文；[作者原公告](https://www.zyphra.com/our-work/zyphra-demonstrates-large-scale-training-on-full-stack-amd-platform-powered-by-ibm-cloud) L23～39明确此次release technical report；[AMD署名正式分发页](https://rss.globenewswire.com/news-release/2025/11/24/3193573/0/en/amd-powers-frontier-ai-training-for-zyphra.html) L67原字段`November 24, 2025 09:01 ET | Source: Advanced Micro Devices, Inc.`，不是转载推定。纽约已EST，分钟精度对应BJT11/24 `[22:01,22:02)` 完全落窗，采用**这个官方report发布公告事件**。不把v1 submitted=`2025-11-21T10:44:02Z`直接当public，也不把公告分钟当arXiv精确首公开。原页完整核心及链接身份在raw-amd-official-release-sparoa18.json。

请root现在独立校准这个日期事件与窄机制方向，无需等其他三项。必要论文审阅下一步只看GPU形状/collective与checkpoint关键对照，Books先比对应owner实际正文，不因vendor名字没有而造diff。

## 其余三项的具体初筛停点

- [NX-CGRA 2511.17235v1](https://arxiv.org/abs/2511.17235v1)：题摘确为edge Transformer软可编程CGRA同时执行linear/nonlinear kernels，潜在增量是受功耗/面积限制下可重构执行分支，不因没有摘要实验配置关闭；但摘要“software programmability”仍需目标式确认实际结构delta，不能借成熟CGRA原则收。submitted=`2025-11-21T13:26:16Z`非public，具名日期查询没有恢复明确作者公告；接受DATE2026标签也非本次公开日。普通下一步为仅方法/关键配置及有限官方日期元字段，不遍历全体系结构分类。
- [Optimizing PyTorch Inference with LLM-Based Multi-Agent Systems 2511.16964v1](https://arxiv.org/abs/2511.16964v1)：v1摘要有exploit-heavy策略与error-fixing协同、优化步粒度与受测性能的条件对照，潜在局部可审增量，不把多agent组合名字或2.88x单数当依据。v2增加的compile对比不能继承。submitted=`2025-11-21T05:37:38Z`非public；精确具名/作者域和仓库日期查询未得可核公告。普通下一步仅必要counterfactual配置/预算和原日期字段。
- [SparOA 2511.19457v1](https://arxiv.org/abs/2511.19457v1)：完整题摘为稀疏/算力强度threshold predictor、依据实时状态的RL CPU-GPU调度、async与batch优化。不能因通用DNN或小模型自动范围外；必须先定点核实际算子/负载是否揭示可复用执行条件，且不把阈值+RL+async组合本身当新增关系。原HTML已恢复，停点只核方法/模型/关键对照，不全读641行。submitted=`2025-11-21T09:45:28Z`非public；首公开尚未确认。

前三项不是确定候选，未评分、未入Books。若必要日期有限原源仍缺，则作为具名外部保留，而非把跨截止上界改成“窗外”或默删潜在贡献。没有反复空查询，没有把资料访问受阻当负面贡献证据。

## 必要审阅与日期停点更新（2026-10-04T16:21:09+08:00）

实际方法/对照响应为raw-tail-method-entry21.json、raw-tail-core22.json、raw-tail-controls23.json和24.json。AMD采用范围进一步收窄为 §III-C 的节点内通信参与者条件：作者 MI300X/xGMI 配置里，子组不继承全节点带宽；训练有反向计算可重叠，长上下文推理缺少该重叠因而选择不同通信。不是所有 AMD 或所有 mesh 的定律。已核 §II-A/B 硬件/rails-only取舍、§III-A/B/C/D 与 §V-C/D；buffer饱和点、kernel shape和checkpoint仅保留必要上下文，不采用全模型领先或10×保存数。§V-B限定Muon为二维，而§V-D优化器分配表述又列卷积/norm等，存在内部不一致；不采用该分配表。仅相邻边界SendRecv也不能证明跨多个rank的大参数安全，本次不将它提升为通用替换AllGather的正确性命题。

实际Books定位 `TRAIN-DISTRIBUTED-TRAINING` Ch36：开篇、L140～157通信模型、L281～333路径/collective合同、L349～391状态与跨vendor分层；Ch35开篇/Ch37开篇和L219～240交接已读。Ch36 L154已明确effective bandwidth受topology/message/concurrency影响，Ch37 L235的“节点内高速域”不是绝对规则。作者建议本项仅报告：xGMI参与者数是具体硬件条件与新局部证据，但现有解释已要求按实际group/topology测量，未发现必须重写长期决策链的缺口。若root判需要更明确的“节点内高速域不保证任意子组相同带宽”，只请求在Ch36通信时间模型后局部限定，不能因vendor或论文名称未见申请整章扩写。独立校准/必要证据与Books判断待root，本项日期已经核，不再列首公开空请求。

NX-CGRA p2～3 §III实际核异构PE/MOB、静态microcode MIMD/VLIW、integer多精度与local RF；不是仅把CGRA原则改名，潜在局部执行分支仍保留。PIKE v1 §3.2/4实际核异步evaluation使elite尚未完成、岛/并行度/repair共同变化，44任务受限suite、H10080GB PCIe、300-query设定和最多5次repair；不把“exploit”理解为安全攻击，也不因Abstract未写torch.compile就声称v1正文没有该对照。没有将后来的v2摘要增量继承。

SparOA §2.2/6.1/6.7～6.8实际核含ViT/Swin的5模型Jetson评价，稀疏与FLOPs两种proxy不能单独替执行测量；文中所谓computational intensity这里定义为绝对FLOPs，并非FLOPs/byte，不能引用为两变量普遍正交。SAC需33～46秒搜索而greedy少于1秒，功率更高但作者每次推理能耗下降，收益有摊销条件；没有采纳形式最优或离散batch梯度保证。

有限日期恢复最终仍不足：NX v1 Updated=2025-11-24T01:37:22Z、created=02:35:50Z；PIKE v1 Updated=2025-11-24T01:18:31Z、created=02:29:28Z；SparOA v1 Updated=2025-11-26T01:00:31Z、created=02:47:53Z。原日期JSON/receipt已保存。前两项只有窗内登记上界，没有首公开下界；后一项较晚上界不证明它一定晚公开。具名官方/作者查询未恢复公告，停止继续空搜索；三项终态日期保留，不进正面候选/Books，重开需精确v1公告、作者首次公开记录或完全落窗的上下界，仅重开本项。
