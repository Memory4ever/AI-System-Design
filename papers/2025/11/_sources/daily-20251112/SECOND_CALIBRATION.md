# 2025-11-12 第二批准入方向

作者：Noether；2026-10-04本轮实际筛选。本日窗口见 [CURRENT_STOP](./CURRENT_STOP.md)。非作者独立尚未发生。

## 范围与版本

三类窄主题API以`submittedDate:[202511071900 TO 202511101900]`发现可能属于周一公告的材料，不把此字段当公开。模型第一查询总282，仅取start0/max60，见范围过宽后停止，不续全282；收窄题名/形成机制后45条，system9条、multimodal/agent57条各一页取尽。标题用于筛范围/选择必要题摘，不成为所有论文的实验/owner队列。实际 query/收窄见 [第一轮](./12-arxiv-query.json)、[收窄](./12-arxiv-narrow2.json)。

本包16篇**精确v1完整题摘已全部实际读过**：[原XML](./arxiv-exact-v1-batch1.xml)、[真实id_list/执行](./12-batch1-exec.json)。实际entry id 16个后缀均v1，published=updated原值保留；初次发现API的v2/v3/v4不代替本包v1。本包只判断具体潜力，未因日期问题展开全实验，也未因名称缺位查全owner。

公开时间共同缺口：Atom published是首次submitted。实际 [availability](./availability.html) 和本机timezone换算将周一20EST映射本窗起点，周二20EST映射excluded终点，但常规schedule不能补造各篇09:00的精确公开时刻。官方月列表旧2511路由404；ISO2025-11路由返回200但timeout仅276869/2620782 bytes，实际只有月级authors/titles、没有逐日公告头；不用于公开日期或“已读完”证明，也未把1527条转题摘队列。见 [原部分响应](./arxiv-cl-month-index-iso.html)、[执行](./12-native-round4.json)、[纠正入口/停止](./12-native-round5.json)。不重复完整月抓取。最小重开为对应ID的真实官方首公告/公开列表日期及可落窗上下界，或实际作者带时区公告；不是全实验附件。

## 已读后的具体准入潜力

以下均为若日期成立的方向，不是16个确定当窗候选。原题名、完整AB、时间字段集中保留于上述XML；无撤回信号的判断只限当前响应，不声称遍历完整历史。

| v1身份 | 原约束 → 实际增量 → 可能改变的选择 |
| --- | --- |
| 2511.05811 MOSS | FP8 group scaling内积维反量化与在线max reduction成本 → global高精度/local幂二两级microscaling、权重预测调整scale → 精度与scale更新成本取舍；7B、BF16对照与up to34%只是作者初值，尚未读实验配置。潜在训练低精度owner，不按框架名归类。 |
| 2511.06010 MoSKA | 相同共享上下文反复memory-bound GEMV → unique/shared分离、跨请求共享attention GEMM并以稀疏attention及异构执行支持 → 高sharing workload下改变KV/计算路径；538.7x不外推一般LLM serving。 |
| 2511.06029 Lethe | prefill压缩不足以解释reasoning长decode累积 → layer redundancy预算、多轮RASR结合recency及变化attention relevance → 需要decode阶段质量/吞吐边界；2.56x只作者AB，不授SLO。 |
| 2511.06605 DMA Collectives | DMA大消息并发收益不代表小消息可用 → MI300X下调度/同步延迟分解与优化，小消息原all-gather4.5x/all-to-all2.5x慢 → collective offload必须按消息尺度选择。**当前名DMA-Latte不倒灌v1题名或v1实验**。 |
| 2511.06174 LUT-LLM | 单batch端侧算术执行受限 → activation-weight coquantization、centroid search与2D lookup及缓存时空安排 → memory-based FPGA设计分支；定制Qwen3 1.7B/AMD V80与MI210/A100不同设备不当通用GPU胜出。 |
| 2511.06134 Maestro | exploration与synthesis混合导致错误共识/credit混杂 → 中央/执行角色拆分，CLPO decision policy gradient与rationale listwise loss → 真正目标函数分离方向，不只给既有流程换名。 |
| 2511.06411 SofT-GRPO | soft-thinking随机性/embedding支持使直接GRPO不足 → Gumbel-Softmax与重参数化policy gradient → soft连续表示训练路径；Pass@1平均+.13%/Pass@32+2.19%不能混为单样本稳增。 |
| 2511.07317 RLVE | 固定题目过易/过难使学习信号消失 → 环境程序化可验证reward与动态difficulty、400手工环境 → 训练环境广度和预算取舍；3.37% vs .49%/>3x compute对照待核，不因局部1.5B关闭。 |
| 2511.07372 Curriculum Tree | curriculum有效性经验缺必要条件 → uniform-branching/states-conditioned树、相邻stage complexity条件下指数→多项式sample/oracle成本 → 可修正课程效果成立条件，不能外推一般LLM。 |
| 2511.07378 Length Generalization | 长CoT训练长度外推未解释 → synthetic state-tracking代数结构、attention concentration/retrieval robustness与recursive self-training保证 → 模型长度泛化条件；NeurIPS full-version说明触发必要会议身份核查，不能只用submitted归属。 |
| 2511.07482 AAPP | input-dependent dynamic pruning保留计算却破坏alignment circuits → 对alignment-critical circuit做适应保护、matchedcompute拒答变化 → 需要核正确拒答/过度拒答及quality，不从50% refusal直接授安全保证。重要安全反侧保留。 |
| 2511.06212 RAG-targeted attack | 流量分析/设备缓解依赖retrieved描述 → meaning-preserving word级poison使GPT5Thinking缓解具体性和实用性退化 → 是局部RAG证据链反侧，不能泛化全部IoT或LLM。评价rubric/judge范围待核，日期问题不抹掉此潜力。 |
| 2511.06606 SPUR | mono输入缺空间方向/距离 → FOA四通道rotation-aware listener-centric表示+adapter与sim/real spatialQA → 多模态表示保留空间参照；通用audio不退化与ablations只摘要声明。 |
| 2511.06136 OCWM/DLPWM | 对象分解/视觉OOD更好不必控制更好 → reconstruction/prediction好但policy逊DreamerV3，interaction latent drift → 具体world representation到policy稳定性反侧，不外推LLM控制。 |
| 2511.07416 PhysWorld | video像素motion直接retarget忽略physics → 视频→physical world重建、object-centric residualRL → visual生成与可执行动作间physical grounding；真实机器人zero-shot仅作者任务范围，无安全/全物理保证。 |
| 2511.07399 StreamDiffusionV2 | offline throughput batching不足online frame deadline → SLO batching/block scheduler、rollingKV/motion noise与denoise/layer pipeline → interactivevideo latency/scale共同约束；14B/1.3B四H100、0.5s firstframe、58.28/64.52FPS各绑定模型，不将near-linear变无条件保证。 |

## 需要非作者定点校准

请root分配Ohm/Carver核本包准入理由、精确v1边界及重要反侧；评分/证据深度待方向校准，不为了处置改分。日期仅有限原恢复，不授Books。未核范围：16篇方法/实验全文、现有Books owner、其他普通含糊题摘和来源尾项。先准备即交，本日普通工作继续。

## 后续精确日期/事件恢复（2026-10-04本轮）

MoSKA先前简称query出现同名噪声，本轮仅一次完整题名查询恢复[SK hynix官方原publication](https://research-user.skhynix.com/publications/detail/seq/115)，实际打开原L55–66：`Oct 31, 2025`、同题名/IEEE CAL DOI，unique/shared序列、GEMV→GEMM、MoE sparsity、disaggregated hardware及538.7x均已披露，与本包v1完整AB无已识别新增差额。原日期无TZ，不补精确first-public时刻；整个该日期在本窗前，**本次arXiv首次提交不能再当新公开事件**。改判仅事件归属/去重，不关闭机制潜力或展开全实验/其他月份。实际query与原页见[最后精确查询](./12-trigger-exact-last.json)、[官方原记录](./12-moska-old-original.json)。请独立核此新增日期/去重依据，其余15项方向与原字段不变。
