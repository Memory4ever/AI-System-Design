# 04/28 arXiv 首批 30 条：有限非作者准入口径复核

范围：独立读取 `arxiv-owner-replay-20260903/20260428/arxiv-owner-receipt.json` 中本批 30 条完整题摘，对照作者 [`V3_ARXIV_ADMISSION_BATCH1.md`](./V3_ARXIV_ADMISSION_BATCH1.md)。仅为项目范围与贡献准入校准，不是 945 条全体、日期逐篇归属、证据审阅、Books 写后或日级 Gate。库存摘要可能受后版污染；仅以下具名疑点定点重开官方 v1 必要段，不声称其余 25 条已获 exact-v1 证实。

## 双向结论

作者的 16 条“继续”——`22778/22782/22783/22871/22879/22888/22891/22981/22985/23036/23046/23051/23073/23099/23108/23121`——均有可指向原题摘的主线机制、控制/评价边界或反证，**作为待证据候选方向可继续**，并非已确认结论或必然 Books 新增。尤其 `22778` 的谱相关/剪枝消融不能凭题摘叫训练因果定律；`22782` 的“无信息损失”与 `22888` 的 response-conditioned “执行前”检测需要实际时序/预算验证；`22891` 的“等质”配对若无独立 gold 仍是代理；`23099` 的无偏/有界结论取决于 surrogate 与采样前提。保留它们是核实这些差异，而不是接受 headline。

`23080` 的“继续核贡献”正确，不能因通用 P2P 术语直接关。官方 [v1 PDF §2–5](https://arxiv.org/pdf/2604.23080v1) 具体区分 node churn 与 agent warm/cold churn，并把 routing success 与有 deadline 的 usable availability 分账。不过当前 [Ch84](../../../../../books/part-07-agent/84-agent-platform.md)「Agent Discovery 是可修复的路由状态」已有该家族 `SF-2026-ARXIV-2604-23080` 的双 churn、readiness、Kademlia/gossip 与 SimPy 限制。若日期及证据通过，可判 `No Change — Existing Coverage`；**现有正文不是贡献前排除理由，也不能重复写书**。

13 条前分母关闭中，`22881/22893/22906/22935/23001/23002/23049/23056/23058/23069/23102/23139` 的最终方向可保持，但其中 `22881/22893/23069` 理由应收窄如下；**`22901` 当前关闭理由不足，需定点重开贡献判断**。这不是自动把它加入冻结分母。

## 具体修正

| 家族 | 非作者依据与建议 |
| --- | --- |
| [`2604.22901v1`](https://arxiv.org/html/2604.22901v1) | **重开准入判断，不先保留。** 官方 §3.3/Alg.1 不是仅把已有固定缓存搬到时间序列：half-spectrum token、累计残差 KV、event-intensity 触发的选择性刷新与周期 probe/error-feedback 形成一条可核的 diffusion 执行路径；§4 的 fixed schedule/no-feedback/no-energy 对照也试图区分这些责任。现 [Ch24](../../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) 已写 trajectory-conditioned selective refresh、误差预算与 drift 校准，所以它可能只是该原则在**频域时间序列**的有界实例。原关闭理由要求证明可迁移到图像/音频/视频，构成不必要的跨模态硬门槛。下一步仅比较“频域半谱 + probe-feedback 是否改变已有 cache-validity/refresh 选择”，并核 5 组 time-series（含 ECG/金融/NASA/climate）、固定步数、KV 与端到端成本；若无独立设计差异，再以前述 Ch24 具体既有命题关闭。不得以 2.2× 推大模型多模态服务收益。 |
| [`2604.22893v1`](https://arxiv.org/html/2604.22893v1) | 可关闭，但理由不能只说“经济定价”。原文 §3/§5.6 确实测试 proxy leave-one-source-out gain 对训练收益排序，属于 TRAIN-DATA 边界信号；然而实验是每域 12 训练例、6 域内验证例、4 source shards 的 smoke run，固定/校准 ensemble 的平均 Spearman 仅 0.483/0.431，而 proxy 单独 0.986；§5.5 大规模、多尺度与过滤实验多以计划表述。当前 [Ch27](../../../../../books/part-04-training-system/27-data.md) 已要求固定 checkpoint/compute、proxy proposal 与 held-out/full-training gate。此文尚未给足以改变该验收选择的独立证据，Merkle/定价组合也不是新训练目标；应以这条具体比较作前分母关闭，不能说“完全没有训练贡献主张”。 |
| [`2604.22881v1`](https://arxiv.org/html/2604.22881v1) | 可关闭但不要以“推荐领域”本身拒绝。§4 的 GPU page/CPU chunk、pinned DMA、双缓冲与局部性替换针对 HSTU 逐用户、跨请求可复用的巨大状态，属于真实服务机制；[Ch45](../../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) 已有 tiered recoverable KV、物理页/批量传输、host-device 有效性和成本分账。该文没有证明新的 LLM/Agent 状态 identity 或改变已有 tier 选择；作者的 3.1×/98.5% 是推荐负载，不外推 LLM Serving。用“既有机制 + 特定负载与 Page-Chunk operating point”作关闭理由更准确。 |
| [`2604.23069v1`](https://arxiv.org/html/2604.23069v1) | 维持关闭，但作者标注的反向抽检点已定点核。§3 Alg.1 用 LLM 估计父边、BFS 祖先保全；§3.3 将 pytest/unittest feedback 写成 passed/failed/unknown/superseded，禁止 failed/superseded 节点再当 parent。当前 [Ch77](../../../../../books/part-07-agent/77-memory.md) 已有 action-observation dependency 的 construction/retrieval 分账、superseded/history 分离与 dependency-closure 失效。论文没有独立证明该父边为真实因果或比既有结构化 memory 多一个可验证一致性不变量；滑窗比较不隔离图与反馈标签的贡献。可将这些具体约束写成前分母关闭，而不是泛称“已有 graph memory”。 |

其余关闭项中，`22935` 是未见可执行威胁覆盖/对照的 ASIC+eFPGA 方案，不把架构愿景当安全保证；`23001` 是 VLA 数据/评测议程综述，不因提到主线节点而保留；`23002` 的科学 autoformalisation 仍落当前暂缓的 AI-for-Science 应用，语义漂移观察未单独隔离出一般 Agent 接口；`23049` 的 HITL 四维分责仍是现有审批/角色/通道原则，题摘无新增跨 Agent 一致性失败证据；`23139` 的 GNN 网络拥塞缓存不能仅因 GPU/RPC 名词迁移为 LLM 通信。`23056/23058/23102` 的原具体范围关闭可维持。以上均非论文无学术价值的判断。

本审计没有纠正/撤回整日日期推断，也未取得 30 篇逐项公开日志。作者只需修本批受影响的 `22901` 准入与三条前分母理由；无需重扫 945 条或无差别读取其全文。后续候选仍须逐项 exact-v1、日期和必要证据，不能由本次口径 PASS 直接计分或称日报完成。
