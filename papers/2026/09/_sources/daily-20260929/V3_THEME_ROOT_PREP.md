# 2026-09-29 Daily：五个 Theme 的作者证据与有限采用提案

窗口：2026-09-28T09:00:00+08:00 ～ 2026-09-29T09:00:00+08:00。作者：sep29_tail_a。本文件仅为作者证据和 literal 提案，不是独立 PRE、实际 Books 写入、POST 或日级验收；这些 Gate 由 root 后续分别处理。

仅处理 root 已按本日官方 New 完整题摘准入的 RTP、MM-ABC、CATok、Signal or Noise、MASTraceBench 五项，不扩池、不比较旧 revision、不搜索其他日期。重新读取 AGENTS、当前 Research/Report 合同、Sources 的使用说明/Daily 组、Prompt、ROADMAP 与当日相关 checkpoint，并读取 Books 的 Project Context、Learning Philosophy、Writing Guide、实际 owner 和必要邻接。以下建议不受读成本、Books 决定或访问状态反向调分；5–6 分标准审阅后，为采用差额定点深入，7 分读到支撑命题和直接反侧足够即停。精确 v1 HTML 可访问，不存在依赖性外部受阻；没有运行作者 artifact、复现实验或修改 Books/Report/LEARNING_STATE。

## 日期、题名、评分与最终作者建议

root 交接的 fresh Tuesday 29 September 官方 New 题名/家族及本日停点，结合 [arXiv 公告日程](https://info.arxiv.org/help/availability.html#announcement-schedule)，支持首次公开 **2026-09-29T08:00:00+08:00**，在独立窗口内。五项当前 abs 和精确 v1 HTML 均显示 Submitted/版本日为 28 Sep 2026，未见撤回/纠错标记；这个提交日只验证版本身份，不代替首次公开时刻。不将 Cross 分类或同一家族重复计数。

| 精确 v1 的准确题名 | Design Delta + System Reach + Durability | 最终作者建议 |
| --- | --- | --- |
| [Revision, Not Restart: Revisable Visual Plans for Closed-Loop World–Action Models](https://arxiv.org/abs/2609.35439v1) | 2+2+3=7；深入核事实/计划/动作的修订边界 | 窄 I 提案：`MULTIMODAL-EMBODIED-VLA`，保存求解 checkpoint 的未执行视觉计划修订 |
| [MM-ABC: Towards Generalist Mobile Manipulation via Seeing, Coordinating and Imagining](https://arxiv.org/abs/2609.35652v1) | 2+1+3=6；标准后定点核参数化与匹配消融 | 窄 I 提案：同一 Ch26，区分 clean endpoint 输出空间与 flow loss/sampling 空间 |
| [Rethinking Causal Action Tokenization with Conditional Annealing in Flow Matching](https://arxiv.org/abs/2609.35469v1) | 2+1+3=6；标准后定点核 annealing 和直接 decoder 干预 | 窄 I 提案：同一 Ch26，生成阶段绑定的离散 token 顺序；不采用物理因果或语义保全保证 |
| [Signal or Noise? Modality Contribution and Cooperation in Multimodal GraphRAG](https://arxiv.org/abs/2609.35304v1) | 2+1+3=6；标准后定点核 provenance/subset/交互分数 | 窄 I 提案：`AGENT-RAG`；Ch66 只作已有评价合同依赖，不重复整合 |
| [MASTraceBench: Diagnosing Collaboration Gains through Proposal Trajectories in LLM-Based Multi-Agent Systems](https://arxiv.org/abs/2609.34496v1) | 2+1+3=6；标准后定点核初/终 proposal 与聚合诊断 | 窄 I 提案：`AGENT-MULTI-AGENT`，分开创造、传播/保留和聚合损失；CLEARS recipe 仅报告 |

五个 I 是逐项实际 owner 缺口判断，不是每个主题强制改书；独立 PRE 若发现当前共享正文已吸收同一差额，可据实际正文改为 E/仅报告，不改本材料评分，也不把新 benchmark 的整套实验声称为既有覆盖。

## 1. RTP：事实历史不动，修订未执行视觉计划

必要证据：[exact-v1](https://arxiv.org/html/2609.35439v1) §3–§5 的状态表示、Bridge/选择器、matched Fresh+C 和路径消融、主评价及受控 hold；未遍历无关附录。事实历史保留已观测 visual latent、实际 applied controls、proprioception 与原采样时间；encoder 先连续编码再选择历史，不把计划帧塞入事实。当前事实的 packed view/KV 和旧 plan root-relative 坐标分别拥有身份，事实或坐标视图变化须重建事实 KV。新 feedback 比较旧预测的已执行端点与真实新观测，再用实际控制、proprioception 和摘要编码差额。Bridge5/10 从保存的完整 visual solver checkpoint 继续末段，以冻结 velocity 加可训练 residual 修订，已消耗部分不钳成事实，只有未执行前缀返回给 action decoder；retain 模式也按当前事实重新解码动作，不是重放旧 actuator commands。

评价与反侧：训练 residual/feedback 使用行为及视觉监督，只有对应新增模块获梯度；接受器预测视觉与 action 对 fresh reference 的偏差，采用 held-out fresh/fresh 经验阈值及不确定性余量，并非对任务真值或安全的认证。RoboMME 16 任务/800 resets、RMBench 9 任务/900 resets；匹配组固定模型权重、历史/归一化/action 配置，published baseline 不都匹配。paired bootstrap CI 条件于拟合模型，不覆盖训练 seed 不确定性；部分任务退步或 CI 跨零。Fresh+C 控制新增 feedback/监督，residual 是较明确分支；saved-source 与 prefix 对照不支持把所有收益唯一归因 checkpoint。RTP 平均完整调用低于 Fixed10，但 p95 更高（1294 vs 1268 ms）；视觉求解步数下降不等完整闭环 latency 或 physical deadline。固定同步延迟、小 hold 压力和闭环仿真不构成真实机器人安全/生产 SLO。代码/checkpoint 的未来发布承诺不作已核 artifact。

owner 差额：[Ch26](../../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) 的 World-action model、Visual trajectory、Self-editing Action Draft、Admission Action Memoization 和三轴 Action Diffusion 复用已讲计划/事实分离、失效和 controller 权；未讲 **保存 visual solver 路径 → 用真实执行 feedback 修订尚未执行的 plan → 重新解码当前 action**。Ch25 拥有环境预测对象，Ch27 拥有行为/示教来源；这里改变 control-boundary 的计划状态，唯一 owner 为 Ch26。建议紧接 World-action model 的同步/异步生成分支、在 Future-to-Action 因果使用前插入两段，勿放成普通 KV/cache 优化。

### 建议 literal（两段）

每次新观测都重新生成视觉未来，在环境突变或计划身份不完整时最容易审计；但大部分未执行计划仍有用时，完全重启会丢掉已支付的求解工作。一个可修订分支分别保存真实 observation/实际控制/proprioception 的事实历史，以及带 root、原时间坐标、已消耗 frontier 和 solver checkpoint 的视觉 proposal；新观测只更新事实，不把旧预测晋升为历史。反馈比较旧计划已执行端点与真实新状态，让小 residual 从保存的求解阶段修订尚未执行的视觉前缀；动作随后按当前事实重新解码，retain 也不授权重放旧动作。

路径存档、feedback/residual 训练、事实 KV 重建和接受器都增加成本与失配面；checkpoint 不完整、horizon 耗尽或估计偏差过大时恢复 fresh plan。接受器的 visual/action discrepancy 与经验校准只提出 retain/bridge/fresh 选择，不拥有任务正确性或 physical commit 权。[RTP 的有限闭环对照](https://arxiv.org/html/2609.35439v1)支持这种修订接口，但 source/prefix 消融和部分任务区间不足以唯一分配收益，较低 mean 还伴随较高 p95；不把少视觉步骤当 deadline 证明。分布、坐标或反馈失配时保留完整重算、短 chunk 与独立 controller，以真实环境反馈验收行动。

## 2. MM-ABC：输出参数化不等于训练/采样空间

必要证据：[exact-v1](https://arxiv.org/html/2609.35652v1) §3、§4.1–4.5、§6.1–6.3。共同 noisy chunk 下，x-head 直接给 clean endpoint；v-head 的 endpoint 为 `z_t+d(t)g`，两者用同一个 masked endpoint MSE、归一化 inverse-square weight，并从 endpoint 转 sampling velocity。没有 decoder raw-input skip 的受控网络中，velocity 端要在内部表示输入噪声，才能经 endpoint 转换抵消；这是参数化/表示负担的比较，不是宣布 flow objective 不可用。synthetic 模态分配直接给定、clean subspace 维度预先规定，不能说实验已让机器人从观测学会协调。

实际 full model 的 manipulation/body 有各自参数、共享 masked attention；同一 near/far segment 内双向通信，far 可读 near，near 不读 far。稀疏 VLM 多层 feature 注入仍向 backbone 传梯度，不是冻结感知。未来 geometry teacher 只提供 recorded future targets，future queries 不读 action/future images，future branch 和 teacher 在 inference 删除；该部分与 Ch26 training-only foresight 已有覆盖。统一有效 channel/state masks 和具身数据引擎保留报告，不新增另一 owner。

评价与反侧：§3 八个 paired seeds（时间分解指标十六个），同初始化/数据/noise/loss，known basis 允许 Bayes excess-risk 对照；无 raw-input skip、给定 coordination mode 和固定低秩是结论条件。§6.2 同 120k steps、batch64、无 robot-mixture pretrain 的 16 RoboCasa composite-seen 任务中，保留 future branch 的 v-pred 29.2%，full x-pred 32.8%；没有所有组件全因子或 near/far mask 独立对照，不能独归因每个结构。Full 在 WashLettuce 和 ScrubCuttingBoard 等输给受限变体。真机单个 mobile 双臂平台、五任务、每方法同200 demonstrations/任务、20 trials/任务，存在与 π0.5 持平任务；其他模拟的 benchmark-native baseline 不都匹配完整训练。没有 physical safety、跨机器人 SLO 或 x-head 普遍优势证明。

owner 差额：Ch26 的离散/连续 bottleneck、固定点停止、learned endpoint initialization 与 endpoint corrector，分别解释 codec、算多少步、从哪里起步及末端怎么修；当前没有 **网络输出 clean endpoint vs velocity，在同 endpoint loss 下如何改变 noise burden**。MoPA perception 分流/控制耦合、training-only foresight 已在正文，不为 MM-ABC 再堆同义分支。唯一采用参数化这一缺口，建议置于 Ch26 固定点 decoder 两段之后、learned conditional endpoint initialization 之前；Ch25/27 不接管 policy head 的参数化选择。

### 建议 literal（两段）

连续 action flow 的训练 loss、网络输出与 sampling velocity 不必处在同一空间。Velocity head 是自然基线；若 clean action 集中在较低维结构、输入又高度带噪，直接预测 clean endpoint 可让网络输出聚焦动作结构，再由 endpoint 与当前 noisy state 的差转换为求解 velocity。比较两者应固定架构、condition、noise、数据和共同 endpoint loss，而不是把输出参数化的改变混成新的 objective；是否存在 raw-input skip 也影响 velocity head 在内部保留并抵消噪声的负担。

[MM-ABC 的受控合成比较与有限机器人消融](https://arxiv.org/html/2609.35652v1)支持该选择在其低秩、few-step 和网络条件中的价值，不证明所有动作都低秩或 velocity prediction 普遍劣化。合成实验直接给定 arm/body allocation，真实协调仍须从观测学得；full-model 平均改善也有任务退步。Clean head 不移除积分、数据/辅助 teacher 或闭环验证成本，更不授执行安全。结构假设、noise/time 分布或动作质量失配时，保留原 velocity policy、多步 flow 与已验证 controller，按实际任务与完整控制成本选择 head。

## 3. CATok：生成阶段绑定，不升级为物理因果

必要证据：[exact-v1](https://arxiv.org/html/2609.35469v1) §3.1–3.4、§4.1–4.5、§5 Limitations；仅因拟采用阶段顺序补读 Appendix C 的 controlled annealing/architecture ablation、C.1 native-decoder donor-swap/removal。VQ encoder 把完整 continuous chunk 编为固定 ordered codes，decoder 的 flow time 从 noise0→clean1。`κ(t)=floor(tK)`，早期全部 tokens 可读，之后逐步移除前 κ 个条件、只留最后 K−κ 个；早 token 的影响可留在已演进的 noisy action state，后 token 留到更晚阶段提供残差细节。这不是每个离散 token 对应一个物理时间步，也不是前缀立即可安全执行。Tokenizer/decoder 预训后冻结，VLA autoregressive CE 仍更新 backbone；不能把阻断 continuous decoder loss 误写成冻结 VLM 或已保证知识保全。

评价与反侧：Appendix C Table4 A/B 保留 flow/MMDiT、移除 annealing 后 LIBERO 平均从 .959 到 .914；same MMDiT/相近容量的 VQ-VAE random masking 对照仍更低，但不能把 C/D 与 A/B 的全部区别归为 annealing。Native donor-swap/removal 支持受测 decoder 上位置/生成阶段相关影响；三角 support 也由硬 mask 约束，entropy/t-SNE/prefix reconstruction 不构成物理因果、唯一语义或 universal transfer 证明。RoboTwin 50 tasks×20 rollouts；LIBERO/Simpler/有限单平台真机的 backbone、预训来源与任务协议分别解释，不能跨表合成普遍胜率。Main Table1 已有 LIBERO Object/Goal 和部分 Simpler task 不及 FAST/BIN，单平台/有限示教及跨 embodiment 未验限制明确；更多 token 在作者 LIBERO setting 反而退步。没有完整执行 deadline 或机器人安全认证。

owner 差额：Ch26 当前离散 codec bottleneck、粗 planner→连续 refiner、action-facing gradient authority 和 Self-editing Draft 均不是 **将同一 codec 的 token 可见性绑定 flow stage，以形成 ordered information increments**。唯一 owner Ch26，建议在离散 codec LIBERO 对照后、粗 planner→refiner 段之前插入；Ch25 的 transition truth、Ch27 的数据 provenance 不被这一顺序改变。只采用 annealing/干预边界，其他 benchmark/性能 recipe 仅报告。

### 建议 literal（两段）

把连续 action chunk 压成固定离散 codes，便于复用 autoregressive 接口，却不自动给 token 建立可学习的先后语义。一条训练侧分支把 code 的可见性绑定到 flow 求解阶段：noise 起点可读全部 codes，随 time 推进逐步移除前部条件，最后 codes 保留到更晚阶段；早期信息可通过已经演进的 action state 留下影响，后部条件偏向剩余细节。冻结 tokenizer/decoder 后，policy 预测 ordered codes，再由 decoder 还原完整动作。这是生成过程的 coarse-to-fine 分解，不是 token 对应物理时刻或离散前缀自带执行权。

阶段 mask、VQ/codebook 维护与 flow detokenization 增加训练和解码成本，也可能让次序或容量成为新的瓶颈。[CATok 的 matched annealing 对照与 native-decoder swap/removal](https://arxiv.org/html/2609.35469v1)支持受测位置具有阶段相关作用，但部分干预 support 来自结构 mask，不能升级为世界因果或唯一动作语义；更长 code 序列和具体任务还有退步。Frozen decoder 只切断对应 continuous-loss 通路，autoregressive CE 仍可改变 VLM。顺序失配、重构不足、跨 embodiment 未验或预算不合算时，保留普通离散 codec/连续 policy，以真实闭环、原生动作 schema 和独立 controller 验收，不由“causal token”标签签发安全。

## 4. Signal or Noise：支持来源与条件交互分账

必要证据：[exact-v1](https://arxiv.org/html/2609.35304v1) §3–§5.5、§6.1–6.2 的必要总量/切片与 CI、§7–§8 的建议限制。Graph edge 记录支持该 fact 的 evidence chunks 及 modality set；给定 subset 时按 modality intersection 保留有支持的 edge，并只携带选中模态的 evidence，不让被屏蔽来源借多来源 edge 混回 reader。固定过滤→cosine ranking/top20，先过滤再排序，subset 比较不是任意换 retriever。

评价边界：RAG-Anything，两个 long-document DocVQA 共327 documents，严格限 gold 恰两模态的1,051 questions（835+216），每题三个 nonempty subsets×五个 MLLM。没有全四模态人口结论。Contribution 的 SHAPE 归一化分母为 joint performance；cooperation 为 `V(AB)-V(A)-V(B)+V(∅)`。关键反侧：`V(∅)` 是每组最频繁 gold answer 的 constant predictor，并非实际空-context LLM run；负值可表示冗余或干扰，不独立鉴别二者。主要 stratified bootstrap 保留 benchmark/modality pair，100k resamples/95% percentile CI 是 question 样本波动，不是重建 graph、多次模型运行或所有部署的置信保证。Intent 由 LLM 与两个 LLM judges 注解，不是人工 gold；小组不稳。Pooled Image-Layout/Layout-Table CI 可跨零、Image-Table 的小协作主要由一模型驱动，Quantity/Locating 切片改变交互；不能采用“Layout永远无用”“图像一定噪声”或已部署自适应 router。

owner 差额：[Ch76](../../../../../books/part-07-agent/76-rag.md) 多模态覆盖/支配已有 claim modality provenance、image-only/text-only/joint pass，Multimodal Memory Graph 已有 identity 与 structural credit；未写 **多来源 edge 的 subset admission 及仅携带被允许支持 → 明确 baseline 的条件交互测量**。[Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 已承载输入消融、population、scorer与不确定性合同，不重复写这一通用层。采用 Ch76 窄差额，紧接“多模态 Evidence 还要检查模态间的覆盖与支配关系”现有两段，在 Escalation 前；Ch75/77 的 context/persisted state 不接管 retrieval 的 supporting-edge 子集。

### 建议 literal（两段）

把不同模态并入 GraphRAG，可保存跨页关系，但一个 fact 若同时由图、表和正文支持，按 edge 是否存在筛选还可能把被屏蔽模态的 chunks 带回 reader。更可诊断的 admission 为 edge 保存 supporting chunks 及各自 modality，按当前允许 subset 保留仍有支持的 fact，只传递该 subset 内的 evidence；来源身份不因高 contribution 改写。再在同一题目、图和 ranking 配置下比较单模态与 joint subset，把“新增信息贡献”同“组合后的冗余/干扰”分开，而不是默认模态越多越好。

这增加 provenance、重复检索/生成和切片样本成本，edge 提取错误与输入预算仍会混杂结果。[有限两模态 DocVQA 分析](https://arxiv.org/html/2609.35304v1)的交互量还使用各组最频繁 gold answer 作零模态基线，不是实际空context运行；负交互不单独证明 interference，分组 CI 和模型/intent 变化也不支持固定模态淘汰规则。部署 router 仍须独立验证实际质量/成本与 source sufficiency；支持身份不全、切片太小或结构不可信时，回退原页/flat retrieval、单模态反事实和独立 answer gate，不让诊断分数取得事实 authority。

## 5. MASTraceBench：新收益、强提案保留与聚合差额不同

必要证据：[exact-v1](https://arxiv.org/html/2609.34496v1) MASTraceBench/Unified Evaluation Framework/Multi-Layer Metrics、Benchmark Design、Experiments Setup/Results及configuration/CCE反侧。Proposer 产生可独立评分的候选，Function Agent 的 critique/verification 不是评分同类。每题或 dynamic 当前 state decision 保存 proposer 初/终 proposal 与 final MAS answer；CG 比 single task outcome，GAB 比 strongest initial，AR 分 strong/weak 的 refinement，AL 为 strongest final minus aggregated answer 的平均差。AL 不是天然非负；aggregate 若更优可为负。动态 task score 以完整 episode，proposal diagnostics 以 state-conditioned decision，不能压成同一分母。

评价与反侧：六个 cooperative/competitive/static/dynamic task；静态157/235/100 samples，主静态平均三 runs；竞争对固定 Single-Agent 对手，Gomoku/TacticDuel各50 games，Negotiation100 configurations交换先手。Qwen3-32B 共用 backbone、常用三 proposers/一 interaction round，但方法 token cost 不相等；TC 不是 walltime/price。OptionGen 用 LLM judge，其他 proxy/rule scores 也不是任意 open-world truth。CG 优于单次不能证明优于 equal-budget独立采样，更不证明“对话产生新知识”。Observation 是所测强初 proposal 常不再提高、弱 proposal 被抬高且强者可退步，不是普遍定律；Table4 更大团队/更多轮/异构 family 的 improve 与 regress 仍混合。CLEARS 跨 claim evaluation/filter 增加 tokens，w/oCCE 同时移除过滤且降预算，不能独立隔离纯算法收益；Gomoku 最佳 CG 仍属于 Int.Debate。只报告 CLEARS recipe，不把 endorsement 当真实 useful/error oracle。

owner 差额：[Ch82](../../../../../books/part-07-agent/82-multi-agent.md) 当前 Verification/Aggregation 要求与 best single baseline 比、Equal-budget Pareto 约束总预算，Evidence-flow 追踪事实保留，Role/Constraint Survival 验收局部义务；还缺 **strongest initial → per-proposer final → final aggregate** 三层质量账，不能据旧原则说整个新benchmark已经覆盖。唯一 owner `AGENT-MULTI-AGENT`，建议在“并行不是一个旋钮”Evaluation小节成本列表后、条件化机制分支之前插入；Ch81 durability/side-effect state、Ch83 protocol不定义该协作归因。Ch66 的 scorer/population/equal-budget合同继续引用，不重复整合。

### 建议 literal（两段）

协作答案优于单次 baseline，不说明 interaction 创造了新的好解：初始候选中可能已经有更强 proposal，讨论只是传播它，也可能在修订或聚合时丢掉它。对可评分任务应保存同一 query/state 下每个 proposer 的初始和最终候选，再与最终 aggregate 分账：aggregate 是否超过 strongest initial，强/弱初候选各自如何变化，以及 strongest final 与 aggregate 的差额。Critique/verifier 若不产生同类可评分解，不混入 proposer 分母；dynamic episode outcome 与每次 state-conditioned action 诊断也分别报告。

轨迹评分、judge 和 proposal 存储增加成本，strongest initial 是事后 oracle reference，不是线上可获得的正确答案。聚合差额可为负，弱者改善也不能抵消强者退步。[MASTraceBench 的有限六任务研究](https://arxiv.org/html/2609.34496v1)表明这些过程可以被 outcome-only 分数隐藏，但 shared backbone、graded proxy、固定对手和不等 token 预算不构成一般因果归因。仍须与 equal-budget独立采样/单agent、实际 latency 和验证成本比较；score 不可信、任务不能独立评分或协作侵蚀强候选时，保留原 proposal、独立 verifier 和较小系统，不用更多轮或 claim 共识自动授权提交。

## 交接边界

上述五项均完成标准或深入必要作者审阅，来源可达；没有用“普通未读”伪装外部阻塞，也没有为成本调整初定分。实际拟写入差额由 root 独立 PRE 后决定；若获采用，root 写 Shared Books 并由非作者对实际正文及邻接逐项 POST，后续 Report/日期/日级 Gates 独立验收。本文件不宣称本日或任何其他日期已完成。
