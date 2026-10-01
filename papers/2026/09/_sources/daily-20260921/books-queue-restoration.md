# 09/21 精确 Books 恢复队列

作者 `apr01`，2026-09-27；本单元没有修改共享Books或正式Daily。必要原文与事实边界见 [本日有限证据](./arxiv-evidence-restoration.md)。下列“已有实际正文”与“提案未写”不能混记为全部整合完成；独立采用/写后与日Gate各自验收。

## 三项已有实际正文，等待有限非作者源/正文确认

| 精确 Source Family | Owner / 真实正文 | 作者实际对读 | 当前处置 |
| --- | --- | --- | --- |
| `SF-2026-ARXIV-2609-20830` | `MULTIMODAL-GENERATIVE-PARADIGMS` / [Ch24](../../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)，`Autoregressive 不必等于 Append-only Final Text` | 精确v1 §6–8对现有动作/可变文本/rollback正文，未把可选canvas encoder写为作者实验。 | 实际采用已存在；6分gap深入，待root独立定点验收，不追加重复正文。 |
| `SF-2026-ARXIV-2609-21058` | `INFER-TENSORRT-LLM` / [Ch49](../../../../../books/part-05-inference-system/49-tensorrt-llm.md)，addressable fraction/correctness admission正文 | 精确v1 §2–6对实际operator share、relative oracle及write admission；工程sentinel与作者write fraction分开。 | 实际采用已存在；7分纠错深入，待root非作者核，不按旧Done标签免审。 |
| `SF-2026-ARXIV-2609-21079` | `INFER-SCHEDULING` / [Ch56](../../../../../books/part-05-inference-system/56-inference-scheduling.md)，异构多阶段routing正文 | 精确v1 §2–3对实际root/leaf/模型/freshness/admission；drain模型近似、内部部署范围保留。 | 实际采用已存在；6分gap深入，待root非作者核。 |

## 三项新长期缺口，已实际写回（2026-09-30）

### 21484 HE-Guardrail → PLATFORM-SECURITY

- 精确正文：[v1 HTML](https://arxiv.org/html/2609.21484v1)，必要III-A/B/C/D、IV-A/B/C/D已读；`2+2+2=6`，保护深入例外。独立题摘准入root已校准，独立必要源/拟采用核尚待。
- 实际owner：[Ch72](../../../../../books/part-06-ai-infrastructure/72-security.md) `隐私不是一个开关，而是明文边界的重新分配`。其现文给FHE/MPC可见性与成本，但未给密文guard输出控制及近似门残余这一分支。
- 最小插入：隐私明文边界论证后，条件化解释 encrypted input令server无法明文检查→密文response/refusal gate→近似gate残余与噪声代价；同处保留协议遵守、重复查询未证及guard语义不自动正确。该提案不是替换既有明文安全Gate。
- **状态：Applied / root非作者写后通过。** root已独立核必要III/IV并授权Ch72此窄段；2026-09-30实际写入`隐私不是一个开关`原两段后。保留近似残余、gated noise、协议遵守与重复查询未证，source-family marker唯一；本轮实际段落与前后handoff定点核通过，不等于日级Gate。

### 21515 ServeGuard → PLATFORM-SECURITY

- 精确正文：[v1 HTML](https://arxiv.org/html/2609.21515v1)，§3/5/6/7/9必要对象已读；`2+2+2=6`，保护深入例外。独立题摘root通过，必要源/拟采用尚待。
- 实际owner：[Ch72](../../../../../books/part-06-ai-infrastructure/72-security.md) `从文件哈希到可执行来源链`，紧接“模型文件本身也不能只靠provenance...”这一段。当前有来源/behavior probe，没有monitor-relative结构证明与装载bytes责任的分离。
- 最小插入：特定public monitor的不可见通道→受限read factor→承诺/证明→actual served-byte admission，明确base residual、浮点路径、未认证模块与公开monitor范围。旧provenance/行为probe/sandbox仍有用途。
- **状态：Applied / root非作者写后通过。** root已独立核§5–7/9并授权此窄段；2026-09-30实际写入Ch72 provenance/behavior probe之后。指定fixed-point monitor与value/read path，base floor保留，admitted bytes到actually executed kernel明确在proof/attested boundary之外。本轮实际段落与前后handoff定点核通过，不将结构证书升级为全部后门安全，不等于日级Gate。

### 22083 MintAct → TRAIN-GRPO

- 精确正文：[v1 HTML](https://arxiv.org/html/2609.22083v1) §3.4.1–3.4.3、Table2、§4.3/Table6–7必要段已读；`2+2+2=6`，真实机制缺口深入例外。独立准入/必要证据尚待。
- 实际owner：[Ch33](../../../../../books/part-04-training-system/33-grpo.md) `Rollout 变成服务`前的“多个领域共用异步服务后，快环境还会淹没慢环境”段。当前只给显式mixture control，未解释effective mixture与filter率的耦合，以及消费/生产两侧谁控制什么。Ch32已有ratio/PPO，Ch34拥有离线偏好，不复制objective。
- 精确插入提案：域的有效训练贡献取决于生成速度和mixed-outcome group率；trainer消费域标签组时按integer quota接纳，而producer读取累计admitted counts/q后暂停快域，避免已生成后丢弃。配额阻塞时bounded wait放松cap是另一终态，会偏离预设混合而非永久保证同比分布。freshness/importance修正属于另一对象，不能用mixture control替代。
- 边界：作者只联合mobile/desktop与Qwen3-VL 2B/4B/8B，表6的最终模型在某域退步；没有独立消融证明quota/backpressure各自因果收益，不采SLO/硬件未披露的速度数字。固定同步/单域在混合稳定时仍较简单。
- **状态：Applied / root非作者写后通过。** root已独立核Table2/§3.4.3、无独立消融及实际owner并授权此窄段；2026-09-30实际写入Ch33原mixture control段后。采用消费quota、生产admitted-count/q背压和bounded-wait偏离终态，未采用速度headline；本轮实际段落与前后handoff定点核通过，不等于日级Gate。

## 其他工作不伪装成采用

QuAKE、representation drift、L0-MoE、BrainAPI、TinyCeNN、WeightIsOver、DiaVLo、MDL与OmniVChat均已有至少部分必要原文/精确消歧，但真实长期增量、最低投入或最终Books disposition未闭合。它们不是共享Books等待锁的完成项，也不是材料受阻终态。更多题摘工作见 [补漏裁决](./arxiv-title-abstract-screening.md)，不因此queue有六项就宣称本日仅六候选或本日完成。

## 2026-09-30 20874：已备必要证据→真实 owner 提案

[2609.20874v1](https://arxiv.org/html/2609.20874v1)，`2+2+2=6`；长 actuation delay 的独立因素/复杂 predictor 反证及实际知识缺口，深入必要范围。已读 III/Eq1–3/III-A variants、IV-A–D、V、VII，II-C capacity/topology 输入也已读；精确训练/运行与反例见 [作者停点](V3_AUTHOR_RESUME_20260930.md#本次必要证据260920874v1)。未独立复现实验。

真实 owner 为 `INFER-SCHEDULING` [Ch56](../../../../../books/part-05-inference-system/56-inference-scheduling.md)。已对读该章 routing/placement/cold-readiness 的 actual body：vPod 说明 loading/readiness 进入 admission；Pythia 说明角色前瞻与预测漂移；复合 graph warmup 说明预测 ready 不能代实际 ready。这些不等于本材料的容量控制因素分离：token-aware demand、向未来 startup horizon 看、有限 uncertainty margin 与 plant-state observation 不是同一干预。没有现有 actual 论点解释在所测重尾 bursts 下，复杂 Kalman predictor 并未稳定改善 EWMA 的 cost–SLO frontier。故不是主题 E。

拟在 Ch56“流程可预测之外，复合服务还要显式建模各模型的cold readiness”及其代价两段后、Parallel Voting 小节前，补以下两个连贯段（尚未写入，待 root 必要源核与窄锁）：

> Ready 的身份核对之外，容量何时开始增加还受启动时延限制：若只在当前排队已经增长后扩容，新副本到达时负载可能已经过去。一个预测式分支先把 Prefill/Decode 的 token demand 换成已校准的副本容量，再朝实际启动 horizon 前看；预测器、lookahead、有限 uncertainty margin 与实际运行/等待状态应作为不同控制因素分别验收，不能把它们合成一个“更智能扩容”的分数。Controller 只提出未来 replica target，新副本真正 ready 后才进入路由，误差 margin 则支付额外常驻容量。
>
> 更复杂预测器并不自动有更好的 cost–SLO 取舍：受限重尾 burst 模拟中，Kalman 并未相对 EWMA 稳定占优，平稳负载的固定容量仍可能更便宜；复杂模型是否值得使用要看 startup horizon、观测和 margin 的配对消融。作者五 seed 模拟的 absolute TTFT 对另一 simulator 有约两倍偏差，真实 A100/vLLM/Qwen2.5-7B 测试又只以 running+waiting demand 与人工 60 秒启动延迟验证 lookahead timing，没有复现完整 token-decomposed policy。因此该证据支持分开测试控制因素，不给异构、PD 拆分或生产 SLO 保证；预测不稳、容量 premium 过大或 horizon 失配时，保留反应式扩容、保守 pool 与 admission 降载。

上述 runtime-ready 交接是与现有正文衔接的工程要求，不假称该论文交付了原子路由发布协议。拟采用局部反证，不把 KF 的局部劣势写成普遍无用。source-family marker 将只绑定新增两段，不覆盖旧 Pythia/graph warmup。

## 2026-10-01 20845：可见 prefix 日程不等于 runtime 时间授权

[20845v1](https://arxiv.org/html/2609.20845v1)，`2+2+2=6`；已读必要 §2–3/§5/Table3–4/AppendixE及Limitations，确认 Ch23 的具体长期缺口后深入受影响内容。actual `MULTIMODAL-REPRESENTATION` 的 Streaming Multimodal Identity 已承载 timestamp/revision/interrupt frontier、memory/trigger 与 runtime commit 分责，却未承载“单调可见 prefix 是可选择的 attention 日程、其长度预测和 arrived horizon 条件不能互换”的机制。不是单凭流式主题给 I。

拟在 Ch23 `Streaming Multimodal Identity 不止是 Token Type` 首段之后、25621 memory/trigger binding之前两段，待 root 必要证据/拟采用与窄锁：

> 表示可以早于完整输入形成，但模型此时允许读取多少 prefix 是另一项选择。一个闭式日程分支用输出进度、输入长度估计和预算参数构造单调 attention mask；它只决定每一步可见哪些已到达输入，不拥有物理到达时钟、回复提交或打断权限。固定日程依赖总长估计；流式变体以 arrived horizon 和上一窗口信息更新长度预测，因果性保证以这些输入确实先到达为前提，不能将“mask不看未来”写成端到端 deadline 已满足。
>
> 这条路径增加长度 head、预测漂移和预算校准，也可能因等待不足漏证或等待过多延迟。作者 29M/四层 decoder 配冻结 CLIP/C3D/Whisper、单 T4 的实验只覆盖 window-synchronized 到达；异步到达属于条件证明，没有实测 live service。wait-k 的长度 head 职责不完全对称，流式 single run 的 test-clip bootstrap 不覆盖训练噪声；三 seed 修正还改变 ActivityNet 的最佳预算区域，LibriHeavy 差距落在 seed spread 内。因此采用可见 prefix 与实际到达的分工，不采用跨任务统一质量优胜；预测不稳或 deadline 不可验时，保留 wait-k、完整输入或外部 turn-taking，runtime 仍负责 commit/cancel。

源支持模型日程与有限反证；runtime权限交接沿已有owner，是工程衔接，不称作者已交付相应状态机。尚未写 Books、不算单篇独立通过。

## 2026-10-01 20888：soft gate 与 hard support 的算子差额

[20888v1](https://arxiv.org/html/2609.20888v1)，`3+2+2=7`，设计反证深入；§3–4/§5.2/5.3/5.8/Table4/AppendixG/K必要实读保留。actual `MODEL-SELF-ATTENTION` Ch14 `Sparse Support 与 Value Normalization 是两步决策` 已解释 support selector→normalizer 分工，但没有“logit乘soft gate的exp(0)背景floor与推理hard pruning改变support，训练/执行并非同一算子”的具体差额。Ch45/49拥有实际KV/HBM/kernel成本，这里只保留验证交接，不再另造第二owner。

拟在 Ch14该小节18753 binding之后、稀疏连接跨层补全小节之前两段，待 root 必要证据/拟采用与窄锁：

> 可训练 gate 还不一定等价于部署时的 support 删除。一种阈值分支从 post-RoPE query 预测 threshold，训练时把低分 logit 乘以 sigmoid，使其趋向零；softmax 中零 logit 仍贡献 exp(0)，并没有被删除。推理 hard pruning 则改变归一化 support。只有离 threshold 足够远等额外条件下，饱和近似才可能合理；仅 score 超过 threshold 不足，all-pruned 的 top-1 rescue 也只是数值兜底，不能恢复全部被删语义。模型验收应分别检查训练算子、部署算子和最终行为，不能由保留率宣称 exactness。
>
> Block skip 的理论界也须与实际统计量区分：full-covariance 的条件上界不等于用 diagonal variance surrogate 得到的 quantile estimator，后者仍会 false negative。GQA 下一个 KV block 是否搬运取决于共享它的 query-head union，不能按单 head 稀疏度直接兑现 HBM 节省。作者 H100/FP16 kernel 表中，约38% head-density 的质量点在不同块宽仅约0.72–1.12倍 dense，2.5倍来自另一稀疏点；局部 soft/hard alignment亦不证明任意query质量。因此阈值预测、metadata/chunk reduction和训练成本都要计入，质量或实际收益不成立时回 dense/fixed support；真实缓存与kernel执行继续交第45/49章。

采用的是算子/理论surrogate/实际成本分账及局部反证，不是把参考kernel测量称生产端到端收益。尚未写 Books、不算单篇独立通过。

## 2026-10-01 21407：量化 observation 与 solver history 共同修正

[QuAKE21407v1](https://arxiv.org/html/2609.21407v1)，`2+2+2=6`长期gap深入。§2–3与本轮§4/B.3/C–F必要支持/反证已实际作者核到停止。actual `MULTIMODAL-GENERATIVE-PARADIGMS` Ch24“加速后的输出必须与未加速轨迹建立一致性边界”和22723 reverse-covariance两段，没有量化observation→输出window posterior→solver handoff机制；reverse-kernel covariance改善和denoiser-output估计是不同对象。拟在22723 end之后、“已Finalize的diffusion block”标题之前窄两段，待root source→owner与lock：

> 量化又会把当前去噪器输出的偏差写入多步 solver 的历史。只修当前输出，仍可能让它与已有history不一致；另一分支把solver需要的整段输出window作为待估state，以平滑轨迹外推作prior、当前量化输出作observation，递归更新当前及历史entry，再把posterior mean交原solver。它不把采样latent改为另一个环境真state，也不改变原solver的数值更新定义；开头history不足时只返回有效entry、降低外推阶数，不能填造过去观察。
>
> 这条路径支付offline FP/quantized配对校准、posterior state与在线filter成本。按step/channel聚合并逐element修正省掉crosschannel/spatial covariance，却依赖这种共享统计关系；非Gaussian的LMMSE结论还需要有限矩、噪声相互/时间不相关等条件，不是任意量化误差下的Bayesian保证。作者W4A4/20步和两种solver结果主要测对FP生成的分布差，不保证真实质量，部分ImageReward退步且UniPC有cell不最优；单image BF16 CPU-offload比较也不能证明普遍加速。校准轨迹与部署状态偏离、滤波失稳或成本不值得时，保留原quantized solver、更高精度/密集求值及local correction；既有freshness/完整reference仍负责一致性验收。

0.25MiB仅calibrated statistics，不当全部运行内存；校准总成本/生产SLO未披露，不写headline。未写共享Books，也未把作者source停止点当独立通过。

## 2026-10-01 root 独立采用与实际写后（替代上述提案停点）

Root独立必要源→actual owner及实际正文/邻接通过：既有三项20830 Ch24、21058 Ch49、21079 Ch56不重复写；20874实际 Ch56:653/655，20845实际 Ch23:723/725，20888实际 Ch14:284/286，21407实际 Ch24:1392/1394，各两段SF独立绑定，不覆盖旧source。后三段采用root纠正：fixed全输入length head与stream arrived-prefix分开；ETA质量点fixed b64的不同batch/length .72–1.12倍而非不同block width，b128/10%/2.5倍为另一点，gate≈1指数近似不证明output误差；QuAKE估同quantized x处FP输出而非FP原轨迹，LMMSE二阶/不相关假设不作通用Bayes最优。Root写后复读实际限制/代价/fallback，四窄锁可释放。正式Report已同步这些完成单篇，不等于整日报完成。

SPARE20849 exact-v1 §2.2–2.4/Table2与 actual Ch23 PEARL的train-only answer-target/部署撤aux不证真实执行分工由root独立核通过，终判 E不新增Books；REG只读mask与局部配方仅报告，不声称现有书已经覆盖其全部方法。

## 2026-10-01 Weight / CodeMidas actual与三单元后续

Weight21849v1 5分真实gap深入I，actual INFER-GPU-MEMORY Ch54:368/370两段，root必要源→owner及364–374写后通过、锁释放。Source Fig3 fit/non-fit、40×具体denoising配置、24prompt受限质量、双缓冲配置非下界、全fit反慢均保留。CodeMidas22068v1 5分真实gap深入I，actual TRAIN-DATA Ch27:532/534兩段，root必要源/owner/literal及523–545写后通过、锁释放；publicscope/reference/private assertion与fresh-start/整包filter归因保留，PR/Builder/PolicyRelative邻接不动。

Tiny21139 Only/Dia22008窄E/MDL22043 Only非作者必要源→actual裁决已同步正式Report，不新增书稿。Brain21299拟Ch84 Policy/Identity两段I（**未授权**）、Drift21113拟Ch5三对象分账窄E、L0-MoE21672拟Ch21 formation/router分工窄E；必要源/实际owner/Brain literal见evidence末，等待root有限采用裁决，不是普通工作受阻或日Gate完成。
