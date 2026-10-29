# 指定五篇的独立 Source / owner 复核

复核者：`oct11_missing`（本轮仅为 2026-10-07 的独立 reader；不是本日报作者）。检查时间：2026-10-20 13:39 +08:00。窗口仅为北京时间 2026-10-06。已重新读取当前 AGENTS、统一 Prompt、研究/Report 合同、来源使用说明与每日组、ROADMAP；本日只接 CALIBRATION_SIX 和下列五篇原件，不继承 10-11 材料，不扩发现。没有修改 Report、Books、Learning State 或索引，没有执行 stage / commit / push。

本记录仅通过下述限定的 Source、日期和具体 owner 差额；**不代表逐字 Books PRE、实际写入 POST、全部来源覆盖或六部分 DAY 通过**。原批准入校准由 root 负责，本轮不重签其余家族。未核 artifact/未复现实验。HTML 均为本地保存的精确 v1，`read_core.py` 数字只作该快照的导航，不是另一套论文编号。

## 1. 日期合证：五篇均可限定在 2026-10-06

实际打开各精确版本官方 abs 页，并核本地 Atom 的唯一 v1；06415 的浏览器缓存一次失败后，用同一官方 abs 页直读恢复，返回唯一 v1 为下表时间，不是外部缺件。当前页未见撤回、删除、纠错或重要修订标记；未为此遍历版本史。

已实际读 [arXiv 公告/发号规则](https://info.arxiv.org/help/availability.html)（公告表及最终 ID 不提前发放）和 [DataCite 日期定义](https://support.datacite.org/docs/what-is-the-difference-between-the-created-and-registered-date-in-the-datacite-rest-api)。五个 v1 均在 10-05 周一美东 14:00 前提交；America/New_York 当日为 EDT。最早可能常规公告为 10-05 20:00 EDT，即 **10-06 00:00 UTC / 08:00 BJT**。审核只能延后，不单独据日程认定已公告。

逐条实际解析本日 `datacite-<ID>.raw.json`，身份为对应 `10.48550/arxiv.2610.<ID>`、URL 对应同一论文；relationships.client 为 `arxiv.content`、state 为 `findable`。采用 `registered` 作最晚界，未采用 `created` 替代公开时间。

| ID | 官方唯一 v1 提交（UTC，非公开时刻） | DataCite registered 原字段（UTC） | 可支持的 BJT 公告日期 |
| --- | --- | --- | --- |
| 05744 | 2026-10-05 03:51:17 | 2026-10-06T05:06:46.000Z | 2026-10-06，08:00 至 13:06:46 |
| 06116 | 2026-10-05 10:47:59 | 2026-10-06T05:17:08.000Z | 2026-10-06，08:00 至 13:17:08 |
| 06260 | 2026-10-05 12:54:46 | 2026-10-06T05:21:08.000Z | 2026-10-06，08:00 至 13:21:08 |
| 06415 | 2026-10-05 14:30:28 | 2026-10-06T05:25:01.000Z | 2026-10-06，08:00 至 13:25:01 |
| 06597 | 2026-10-05 16:07:33 | 2026-10-06T05:29:26.000Z | 2026-10-06，08:00 至 13:29:26 |

各最早界不晚于最晚界，整个可能区间均在目标日。这是联合约束推断，不把登记时间改称官方实际公告时刻，也不证明全球所有渠道最早公开。没有具体更早稿线索时停止本层恢复。

## 2. CIPHER-MoE / 2610.05744v1

原证：[精确 v1](https://arxiv.org/html/2610.05744v1)，本地 `core-05744v1.raw.html`。实际必要读取：完整题摘，§3.1–3.2.3（Eq1–10、Theorem1 的假设/结论边界），§4/Tables1–3，A.4.4 固定输出保真边界，A.5/Table8 配置。导航核心 24–85、190–198。

通过的增量：token 先按原 Top-K 选 expert，expert 再以 cosine affinity、阈值及 microbatch capacity 筛选候选 assignments；strict drop 清零被拒 assignment，reroute 将其送到有余量且满足阈值的其他 expert。Shared experts 不随之删除，token 也未退出序列或 task loss。因而 token-side Top-K 不变，**不等于实际执行贡献集合或梯度不变**。这条边界比一般“设 capacity / drop 或 reroute”具体。

反侧不能删：定理是 A1–A3 下至少一个 discriminative token 的条件保留容量，不证明 unchanged loss/final quality；A.4.4 的局部输出界固定 expert outputs 和下游计算，不约束训练参数累积。Table2 中 strict 的 V4-Flash OR weighted average 68.59 低于原训练 69.09，部分任务 reroute 更好，不能照搬“strict 全面最优/质量完全保持”。V4-Pro 原 baseline OOM，不能构造与该不可运行 baseline 的有限加速倍数；对比 fixed-router 的可行性和质量须另说。

作者 SFT 覆盖 OR、MedMCQA、SIQA、284B–1.6T；Table8 分别绑定节点/并行、4K或8K序列和 GBS，capacity factor 8，reroute fill-target 4，locality loss 0.01。必要正文/A.5 未披露 GPU 型号和数值精度，记 Not Disclosed；不采用 headline speedup 为硬件可复现或生产保证。排序、过滤/重路由、损失项和额外计算都需计费；质量失败时保留原训练/较宽容量/经核固定分支。

评分建议 **2+2+2=6**：改变 capacity admission 机制，影响模型路由与训练执行/通信边界，有稳定复用价值；不凭“correctness”措辞或模型规模加成到3。因具体保真反侧深入已满足必要层。

唯一 owner：`MODEL-MOE`，[Ch21](../../../../../books/part-02-model/21-moe.md) `Capacity 怎样约束 Expert`（当前约161–177行），已实际读负载均衡到 All-to-All 交接。现有正文只列 overflow 的四类处置，未承载 affinity-aware expert-side admission 与“Top-K 未变/执行贡献已变”的差额。建议该节后最小1–2段，明确 strict/reroute 并保定理/质量边界；**不是 Ch49 PTQ**。这是 Source/owner 差额通过，具体拟稿仍待 root PRE，非已有覆盖或实际整合。

## 3. ORCA / 2610.06116v1

原证：[精确 v1](https://arxiv.org/html/2610.06116v1)，本地 `core-06116v1.raw.html`。实际必要读取：完整题摘，§2 的 coupled-gradient/受限模型说明，§3/Eq3.1–3.4，§4.1–4.3、§5 的 active-window 与替代干预，B.1–B.3 配方，C.1 四seed及C.2状态/LR控制；导航13–90、96–120。未采用完整附录定理作 Transformer 普适证明。

通过的增量：对矩阵参数早期增加软正交梯度 `(WWᵀ−I)W`，到 release point 完全清零该项，之后回到对应 Muon，而不是全程坚持高 effective rank。Embedding、head、1D 参数仍走 AdamW。把早期梯度通道条件化与末期可适配谱分时，是值得保留的替代设计。

关键边界：谱集中可过滤 partner gradient 是局部机制，不证明 effective rank 单独决定整网优化。持续/late/off-then-on shaping 在受限对照不能在终点恢复，early shaping 活跃时也可暂时提高 loss。Dense 默认 first25% hard release 不是全模型通用配方：MoE 因 router perturbation 改为逐层20%–60%解除。C.2 的 reset/schedule对照支持所测增益不只来自 buffer 或某一 WSD decay，仍非所有任务唯一因果证明。1.3B“40% fewer tokens”分支提前启动末期 decay，形谱占比随总预算变为41.7%，不是原配方无改动的纯墙钟结论。

证据绑定 LLaMA130M–1.3B/C4、Qwen3160M–0.6B/Pile、MoE0.8B–8B/OLMo mix，B.3 明列不同 context/global batch/steps/token budgets；130M四seed不能推广到所有规模。8B optimizer 局部开销与全训练收益分开；GPU/数值精度在所读必要配置未披露，Not Disclosed；无 serving batch/concurrency/SLO 结论。

评分建议 **2+2+2=6**，reach 取训练 optimizer/耦合矩阵梯度/阶段配方的边界，不借量化或 serving 扩范围。已有具体知识缺口及 persistent-vs-release 反侧，必要深入层通过。

唯一 owner：`TRAIN-PRETRAINING`，[Ch28](../../../../../books/part-04-training-system/28-pretraining.md) `Optimizer 的不变量必须匹配参数块角色`（当前约761行）。已实际读731–778行及421–435行；现有固定谱分支已说可能限制任务适配，但没有 temporary shaping→hard release、以及 MoE layerwise release。建议在固定全谱段与固定谱半径分支之间补最小一段，不覆盖原 AdamW/Muon 及固定约束合理性；**不是 Ch49 量化/低秩替代**。Source/owner差额通过，具体PRE/POST仍普通待办。

## 4. CentriQ / 2610.06260v1

原证：[精确 v1](https://arxiv.org/html/2610.06260v1)，本地 `core-06260v1.raw.html`。实际必要读取：完整题摘，§3、§4.1–4.3/Eq1–8，§5/Table1与latency、§6/Table2、§7限制，Appendix A 的数据/基线/硬件；导航28–109。无须为采用均值分离遍历完整solver/证明。

通过的增量：adaLN 条件化后的逐token均值不能静态fold进bias；Hadamard对均值方向的行和集中会继续支配量化range。先在native channels去均值，再旋转/量化 residual，并用从原始未量化W求得的 `W1` 以compute precision补回 `mean(x)·W1`。精确性是这一线性均值分量的代数身份，**不是 residual量化后整层无误差**；mean/scale、rank1向量、padding/rotation和kernel成本不能省略。Weight path另用非凸robust lp拟合，非全局最优保证。

关键反侧：Table2 中仅center并不救 W4A2，percentile clip 是2-bit activation质量恢复的重要组成，不能把全部收益归mean。Table1 SVDQuant数值来自既有论文，而RTN/NF4/HQQ在本harness重跑，不能称所有baseline均同轮独立重测。FID低于BF16在5k样本噪声范围，不证优于原模型；pixel与perceptual指标不一致要保留。2-bit仅FLUX.1-schnell模拟量化，无fused2bit kernel；NVFP4/MXFP4及video未验证。

质量条件：PixArt-Σ/SANA-1.6B/FLUX.1-schnell、1024²，MJHQ-5k/sDCI每prompt固定paired seed，开发集与评价分开；前两者20steps/guidance4.5，FLUX4steps/guidance0。真实W4A4 latency只在单A100-80GB/FLUX，含text encoder/VAE，2warmup后6images均值，1.69s对1.77s不授并发/尾SLO或一般加速。可采用机制，不采用宣传式全质量无损。

评分建议 **2+2+2=6**，表示误差与实际kernel/sidebranch边界明确；已因具体差额及反侧深入到必要层。

唯一 owner：`INFER-TENSORRT-LLM`，[Ch49](../../../../../books/part-05-inference-system/49-tensorrt-llm.md) `量化前先诊断分布` / `Rotation Scope 与 Quantization Group 必须共同进入 Numeric Plan`（约1396–1448行已实际读）。现有对称/非对称QK及rotation条件没有承载adaLN逐token DC与exact rank1 reinjection。建议rotation scope前补最小1–2段，将原representative calibration路径与calibration-free替代并列；不新建owner。Source/owner差额通过，逐字PRE/POST未做。

## 5. SLOA / 2610.06415v1

原证：[精确 v1](https://arxiv.org/html/2610.06415v1)，本地 `core-06415v1.raw.html`。实际必要读取：完整题摘，§2反例、§3.1–3.5/Eq1–7，§4.1–4.3/Tables2–4，§6限制，E.2.3、F.4–F.8必要消融；导航10–69、439–465。没有通读全部附录。

通过的增量：在部分已合并模型真实中间activation上，顺序匹配原task-model的local behavior，以data-aware metric regularize，再将composed QK/VO operator按预算rank factorize。固定local inputs下二次回归可闭式求解，不等无数据/无求解费用；这比仅原teacher activation上的Gram合并具体。LoRA先形成有效 `W0+BA`，不独立平均任意因子。

必须保留的适用边界：QK合成依赖attention结构；LLaMA-2-7B含RoPE，作者**只合成VO，Q/K分别作为linear operators合并**。不能照搬“完整QK”到该LLM。原rank已有局部收益，扩rank另外增加parameters、inference memory/compute；HumanEval在扩rank时下降。F.7只加QK或只加VO反而退步，说明composed子分支不独立单调；F.1小任务数有data-free baseline更好。Greedy local目标非统一end-to-end最优；校准不覆盖任务时保留data-free/独立model。

证据绑定同初始化的CLIP ViT、RoBERTa和3个自训LLaMA2-7B LoRA专家，默认每task256训练split校准、三seed；LLM rank32/alpha64/all-linear，math/code/IF分别训练，评价GSM8K/HumanEval/IFEval，模板随task绑定。硬件/precision及完整merge wallclock在所读必要区域未提供，本记录不采用推理性能倍数/生产SLO。统计forward、local solve、factorization与可能rank expansion全部计费。

评分建议 **2+2+2=6**；只按实际operator/state-path与artifact/rank取舍评分，不拿泛化的“local alignment”词汇加分。必要Source及限制通过。

唯一 owner：`TRAIN-LORA`，[Ch30](../../../../../books/part-04-training-system/30-lora.md) `多个 Adapter 能否直接相加` 下 ACT-Mat / Training-Free OPD 的输出保持合并段（约737–745行已实际读，另读696–735行与gauge分支）。现有正文已说teacher输入Gram及上游漂移，却未给部分已merge路径上的cross-state对齐及composed operator再factorize。建议在该局部后补1–2段，保RoPE/VO-only、greedy和rank费用；**不是 Ch56 SLO/placement**。具体稿件仍待PRE与实际POST，不能称已有覆盖。

## 6. HEAR / 2610.06597v1

原证：[精确 v1](https://arxiv.org/html/2610.06597v1)，本地 `core-06597v1.raw.html`。实际必要读取：完整题摘、§3/Tables1–2、§4/Tables3–6，A.1–A.4、B.4质量分母/区间与evidence质量；导航25–101、105–149、166–172。未核补充artifact。

通过的增量：把harness的workflow/intent/requirement与engine的state/capability/outcome双向绑定到request/context revision/instance，并把语义契约和具体policy分开。四个不可混同的状态是intent≠control、preference≠requirement、observation≠guarantee、acceptance≠completion；runtime对真正执行时的prefix/state再检查，不由harness旧观测预留容量。协议类别不是已经定稿的packet/wire schema，也不是新增应用编排层。

反侧：SCBench cache-aware提高reuse却伤最大TTFT，Guard是公平等待限制而非任意负载hard latency SLO。Mooncake100%负载下复合policy吞吐108.9低于FCFS122.7turns/min，不能宣称越多intent总越好。Role-to-mode来自开发期profile/quality过滤/人工核验后冻结，非formal-eval最优oracle或在线自适应全空间。Main和Reader所选模式不同、两个benchmark映射也不同；SparseEngine中的H2O/SnapKV实现/config/revision须保身份。Aggregate Judge接近不证质量等价：BCP selected的citation precision/recall仍低于baseline，Wilson区间宽，不能由无observed degradation推出无质量代价。

配置：SCBench是模拟arrival/thinktime的closed-loop、Qwen3-8B/单RTX PRO6000/96GiB L2；Mooncake是15分钟production-derived trace的50/75/100%session replay、Qwen3-8B/单H100，不是真实生产验收。BCP208题/DRB100题，GLM4.7-Flash分别使用两H100，A.4列各模式context、prefill chunk、capacity、sampling与output limits；在线control path计入E2E，离线profile calibration不计入。任务失败留分母，质量指标与runtime分开。数值精度未在必要区域披露，Not Disclosed。

评分建议 **2+2+2=6**，跨harness/engine的真实边界且契约可复用，不能按“protocol”名称自增到基础性3。必要机制、实验反侧与配置已通过。

唯一 owner：`INFER-SCHEDULING`，[Ch56](../../../../../books/part-05-inference-system/56-inference-scheduling.md) `Infrastructure-aware Multi-Agent Orchestration 必须消费同一状态`（约739行；实际读725–765行）。现有infrastructure state/Pythia预测分支已有proposal与freshness/dispatch分工，但缺双向四类消息及accepted/completed/unsupported outcome合同。建议在Pythia段后补最小1–2段，不重复Ch45的KV有效性；[Ch84](../../../../../books/part-07-agent/84-agent-platform.md)已读入口与Serving/Agent completion交接，只作消费者引用，不复制owner。

## 7. 交付边界与未完层

五篇日期合证及上文限定Source/具体owner差额独立通过，建议均为6分并保必要反侧；CIPHER/ORCA/SLOA的错误owner口述已向作者及root更正，作者确认未写入Report/Books。这里的深入是必要证据投入，不按分数反推贡献。

后续普通工作仅为作者准备最小逐字稿、root实际PRE、协调窄写后实际POST，以及作者融入Report/日级独核；本reader没有把这些尚未发生的层称作完成。五篇现有必要原件均可读，没有具名外部缺件需要隔离；没有展开其他论文或他日材料。具体owner已读够定位差额即停，不签整日。

## 8. CIPHER 实际逐字 PRE 通过（未写）

2026-10-20，本 reader 已完整重读 PROJECT_CONTEXT、LEARNING_PHILOSOPHY、WRITING_GUIDE，实际回读Ch21 capacity至All-to-All完整局部和Ch20/22开篇交接；未变的上文必要Source复用。实际逐字核 [CIPHER_PRE.md](./CIPHER_PRE.md) 的唯一自然段（起 `Capacity admission 也可以放在 token-side Top-K 之后`，末 `不由负载变平签发质量保持`）及拟本人来源注。

结论：**PRE 通过**。位置为 Ch21 现有 `当 token 超出 capacity，系统可能 drop...` 段后、`## Expert Parallelism 为什么需要 All-to-All` 标题前；不替换四类overflow选择。原Top-K候选与执行贡献分开、strict/reroute/shared/loss语义、局部理论权限、任务/平均质量反退与Pro OOM反侧均有原证，成本/回退近正文；不把SFT实验提升成通用训练无损。唯一owner保持MODEL-MOE，后文execution mapping继续交Ch49，未复制其kernel机制。

许可范围只针对上述已存exact段与对应一条来源注；是否授写由root决定，本reader未写Books、未授日级或未发生POST。

### CIPHER 实际非作者 POST 通过

作者获得root窄写许可并通知保存后，本reader实际重新打开Ch21完整161–211行（公式、旧四类overflow、新179行整段、All-to-All完整交接及combine入口）及章末本项本人注。新增正文与上述批准的CIPHER_PRE唯一自然段逐字一致；没有覆盖旧capacity分支或挪动execution owner，成本与反侧仍在正文。本人注准确保留6分、必要Source、硬件/precision限制和未复现边界；其“POST另记”由本实际记录承接，不是先写后验。限定该文件diff-check实际无诊断。**此单项POST通过，精确写位可释放；非日级DAY或全章/全仓验收。** 本reader未修改Books。

## 9. ORCA / CentriQ 逐字 PRE 通过（未写）

本reader实际逐字读 [FOUR_PRE.md](./FOUR_PRE.md) 两项的唯一自然段及本人注模板。Books方法完整读过且未变化；owner实际局部与前后交接复用本轮实读，未借未读章节签名。

- **ORCA PRE通过**：只允许该文件 `## ORCA` 段（起 `谱约束也可以只在早期塑形`，末 `外推成通用加速`）与一条对应来源注；位置是Ch28 `SF-2026-ARXIV-2605-12492` 固定全谱段后、`固定全部 singular spectrum 比只约束最大增益更强` 前。实际731–778行已读，Ch27/29交接已核。阶段塑形/完全解除与MoE逐层解除均有必要源；不把effective rank自签整网收敛，且将regularizer/schedule/state/矩阵运算及总费用纳入，保现有固定约束合理性。非量化owner。
- **CentriQ PRE通过**：只允许该文件 `## CentriQ` 段（起 `旋转前还要检查逐 token 的均值方向`，末 `任意视频、位宽或Serving SLO`）与一条对应来源注；位置是Ch49 QFlash段及marker之后、`#### Rotation Scope 与 Quantization Group 必须共同进入 Numeric Plan` 前。实际1396–1448完整邻接已读，Ch48/50交接已核。仅均值分量精确、残差仍量化、W4A2需clip/2bit模拟、sidebranch及全部费用有据；不将calibration-free转换成validation-free或真实2bit加速。

两项均待root授精确窄写许可，尚未发生实际POST。SLOA的“校准人口”用词和HEAR的消息作用域/policy位置已经指出，应先保存窄修订再接受其PRE；原Source通过不失效，不扩查无关原证。

## 10. SLOA / HEAR 修订稿实际逐字 PRE 通过（未写）

作者已在FOUR_PRE保存所提窄修。本reader重新实际逐字读两段与本人注模板，并回读Ch30 ACT-Mat→OPD→特殊token保护及gauge邻接、Ch56 infrastructure-aware→Pythia→DynBranch完整局部；Ch29/31、55/57交接与Ch84实际52–88行的Serving/Agent completion分工已读。方法文件未变复用。

- **SLOA PRE通过**：现存稿用 `校准状态随合并路径改变`，不再误称样本人口改变；`适用的 attention 结构` 不暗示所有adapted结构。唯一段起 `为减少上游合并引入的输入漂移`、末 `通用能力保持`，位置为Ch30 Training-Free OPD完整自然段及其marker之后、`若只需保留一种生成结构`之前；仅此一段和对应一条末注。部分已merge路径/有效权重、局部解非整网最优、RoPE/VO-only、rank/HumanEval/单circuit反退和全费用/回退均有必要原证，不覆盖既有Gram/因子坐标分支。
- **HEAR PRE通过**：现存稿改为按消息作用域绑定 `request、context revision 或 serving instance`，不把原文各相关身份强制成全三元组；policy仍由两层既有策略独立决定，而非错误移交单边engine/runtime。唯一段起 `预测工作流之外`、末 `执行完成或生产保证`，位置为Ch56 Pythia预测及反侧两自然段之后、`稳定流程的预测可以先准备prefix和副本`之前；仅此一段和对应一条末注。四类消息/四组不可混同的状态、实际消费再核、overload/fairness/质量非等价及全部费用有据；Ch84只消费请求/任务终态分责，不重复协议owner。

两项已保存exact稿限定通过，待root明确窄写许可；PRE不代表实际POST、字面稿之外的扩写或日级验收。本reader未改Books。

## 11. ORCA / CentriQ 实际非作者 POST 通过

作者通知获得root总窄授权并实际保存后，本reader重新打开Ch28 757–785完整固定全谱→新增ORCA（767行）→谱半径/切向/Frobenius邻接及本项末注；Ch49 1428–1455完整QFlash→新增CentriQ（1441行）→Rotation Scope/OptRot/FreeAct交接及本项末注。两新增整自然段各与FOUR_PRE批准稿逐字匹配一次，来源marker未混入旧家族，旧有效分支未被替换。

ORCA阶段解除、MoE层级与预算/因果边界仍近正文；CentriQ仅均值精确/残差量化、2bit模拟与clip共因、sidebranch成本及回退仍近正文。两条本人注准确保持必要Source/6分和未核artifact/未复现状态，没有预支日级完成。限定两文件diff-check实际无诊断。**ORCA、CentriQ此两项POST通过，对应精确窄位可释放；本reader未改Books，非整章、全仓或DAY验收。**

## 12. SLOA / HEAR 实际非作者 POST 通过；指定五项闭合

作者通知实际保存后，本reader重新实际打开Ch30 741–758完整ACT-Mat→OPD→新增SLOA（749行）→特殊token/TAK/gauge局部及本项本人注；Ch56 739–758完整infrastructure-aware→Pythia预测与反侧→新增HEAR（750行）→DynBranch两段及cold-readiness局部和本项本人注。两整自然段均与FOUR_PRE修订后批准稿逐字匹配一次，SLOA的校准state/attention结构、HEAR按作用域or身份/policy两层分工修订在实际正文生效。

SLOA保持RoPE/VO-only、局部非整网最优、rank/HumanEval反退和全部费用；HEAR保持observation/accepted非保证或completed、100%load吞吐反退、citation质量差异及回退。旧正文/四个owner交接未被覆盖，末注准确限定必要Source/6分/未核artifact/未复现和实际POST另记。限定两文件diff-check实际无诊断。**SLOA、HEAR此两项POST通过，对应精确写位可释放。**

本轮指定五篇现已全部完成独立必要Source/日期/具体owner/逐字PRE及作者实际保存后的非writer POST；实际新写为五个canonical owner各一自然段和对应来源注，作者为oct07_missing。CIPHER/ORCA/SLOA串题口述已在写前纠正，不留错误机制。所有结论均限本记录原证与具体段落；本reader不验收其余候选、完整来源扫描或六部分日报，不签DAY/FINAL，也没有自行修改Books或Report。后续仅作者行政同步这五项既成事实及root日级验收，不需重读未变Source。

## 13. 同日 remaining 批：日期、04791 早公开排除与首两项 Source

root 另指派 CALIBRATION_REMAINING 中04791/04977/05041/05105/05123/05282/05292/05329/05558的必要Source/date/owner。本批仍仅BJT10-06，不继承其他日期；不是把AB校准直接升级成Source。以下逐项只记录实际已读范围，未写Report/Books，尚无本批literal PRE/POST。

实际请求各官方exact-v1 abs并解析submission history（05329首次超时另有限恢复），其余八页均唯一v1，未见撤回或重要修订标记。提交UTC：04791=10-03 22:33:21；04977=10-04 05:45:41；05041=10-04 08:19:20；05105=10-04 10:26:07；05123=10-04 11:08:36；05282=10-04 15:03:08；05292=10-04 15:11:16；05558=10-04 21:46:59。均在周五截止后、周一截止前，沿本记录已实际核过的官方公告规则，最早常规发号为10-06 00:00UTC。逐个解析本地DataCite原JSON，doi/url准确对应、arxiv.content/findable，registered分别04:42:29、04:47:00、04:48:45、04:50:16、04:50:45、04:54:43、04:54:58、04:55:52（05329）、05:01:48UTC，均10-06；不用created或submission当公开时刻。此合证仅限定arXiv事件日期，明确早公开线索仍须另判。

**04791 Date-Drop，不是外部缺件。** exact-v1 HTML实际读题摘/§3 Assumption3.1与Theorem3.6、§4–5及Table1–3，局部导航0–137。定理要求确定模式、仅固定频率RoPE、无其他绝对位置项、uniform bounded residual、连续/Lipschitz及无限窗口；有限N下一对答案logit gap不是任意文本最终答案或永不瞬时翻转的保证。官方abs明示已发表ICML，遂实际打开[同题同六作者的PMLR原条目](https://proceedings.mlr.press/v306/hu26ak.html)：PMLR306，45465–45494，ICML2026，06–11 Jul；该早期摘要已包括重复断言下稳定/查询依赖极限及实证，和本日拟准入贡献同链。没有本日重要增量证据，退出本日新增，不以Oct新arXiv号覆盖先公开归属。Ch22 96–143已有容量/读取/竞争和信息利用边界，虽然没有该重复收敛命题，也不能因此越过日期门写书。

**04977 Source/date/owner PASS，建议2+2+2=6，标准审阅加必要反侧。** 实际读`core-04977v1.raw.html`0–121完整题摘、§3方法/metrics、§4结果/teacher-forcing、§5单人n-gram及Limitations。受控候选池的策略命名、边缘分布和以自身生成history判分的条件规则是三项不同测量；wrong-ID仍可规则相近，identity accuracy不应是rollout上界。282条错识别中41.8%仍TV≤.02，说明边缘逼真可遮结构错；teacher forcing将局部应用与free-running维持区分，不能由强模型局部准确推出全轨迹可靠。n=1/2/4/8、prefix256–2048/rule-given及prefix-only MLE反侧支持“证据存在仍执行失败”，但只限小符号闭候选和所测prompt/API模型，不是开放策略或真实用户总体。Ch66 `Off-policy Coverage...`至`能描述分布...`（930–950）实际读：已分描述vs采样/人口覆盖，尚缺识别→边缘→条件rollout及teacher-force的具体交叉诊断。因此唯一owner `PLATFORM-EVALUATION-SYSTEM`，建议在分布描述/采样两段后补一自然段，不另写Ch82；新增诊断和调用/parse/规则reference成本，旧真实人审与固定规则baseline保留。未核artifact/未复现。

**05041 Source/date/owner PASS，建议2+2+2=6，必要反侧深入。** 实际读`core-05041v1.raw.html`0–75（§2规则/estimand、§4设置、§5匹配协议对照/scale、§6冻结redeploy、§7关联、§9limitations）。同castings的broadcast-vs-silence差才是通信效应，不能把单臂相对zero-information ruler当语言效应；sequential投票仍同时，发言不是随机全排列。Haiku4.5 pinned20251001、温度1/no-thinking、7,416分析games，notes是唯一跨代通道且非权重学习。60代notes在16/3的冻结新castings可低于空notes，claim线索会消失；scale一family/arm、k12区间跨零、scalar tilt错拟合真实win不可删。549games的memory缺陷已披露，去除后9/9核心broadcast差仍在但次要对照失去显著；未附preprint的supplement不冒充已核，核心结论可由可读主文限域支持。Ch82 16–25、59–104及494–508实际读，已有coordination tax、信息相关性与固定对手/群体反侧，缺protocol×notes adaptation/blank-note redeploy差额。唯一owner `AGENT-MULTI-AGENT`，建议Coordination Tax既有对照后补一自然段；协议、notes身份、适应历史、全部调用/上下文费用共同验收，不推通用通信law，不新开owner。未核artifact/未复现。

## 14. CommuteProp / HiNa-MoE / Red-TTT 必要 Source/date/owner

三项arXiv日期合证沿§13，05123的官方comments仅为Accepted by PACT2026；有限同题精确检索未得到更早原件的具体线索，不把accepted等同先公开，也不声称已遍历所有渠道。建议均2+2+2=6。以下仅必要Source与owner差额PASS，不是literal PRE或Books写入授权的替代。

**05105 CommuteProp PASS，必要反侧深入。** 实际读exact-v1题摘、§3两阶段/queues/调度、§4假设/噪声floor/NS、§5质量/反侧与B.1–B.4配置及实机表（导航0–61、63–102、131–149；不以截断输出冒充已读的中间公式）。跨block forward/backward不存历史weights，phase2用旧activation/gradient及当前local weights重算局部surrogate；不是原同步BP重排后数值等价。两queue优先关键路径但τmax强制更新，额外forward/queue memory/NS均有成本。定理在global/block Hessian smoothness、有界gradient、η≤1/L_l下，平均梯度范数界含η²τmax²G²(ΣH_lj)²固定floor，不是任意延迟精确最优/质量保持。Table1 SciERC普通异步67.21低于同步72.89，NS恢复72.09但不全任务最优；隐私兼容不是无泄漏证明。Qwen2.5-1.5B、split3/22/3、batch16、utility主要queue模拟；A6000 profile的iso-time剔除optimizer/zero/scheduler并按模型速度缩epochs，不能称完整墙钟。B.4另有两GPU+tc1Gbps/10–200ms实机iteration及15min质量，不与模拟合并作普遍生产证明；该必要范围未给实机GPU型号/完整精度，保持未核。Ch36 1326–1348、1740–1760实际读，已有async freshness/objective和frozen-front/auxhead split，但缺保留task-gradient的cross/in-block拆分、fresh-local/stale-remote及noise-floor换并行的接口。唯一owner `TRAIN-DISTRIBUTED-TRAINING`，宜在Split Fine-tuning现有两分支后单自然段，保同步/weight-stashing与原first-order路径。

**05123 HiNa-MoE PASS，标准审阅加必要实现边界。** 实际读exact-v1题摘/§1范围、§3非侵入定义、§4 AMX、§5 NUMA、§6 decodeGQA、§7配置、§8 FFN/E2E/反侧（导航0–61、67–165）。标准row/column expert weights不变，转小中间矩阵并融合gather/store；BF16输入/FP32accumulator，tile/shape/alignment需匹配。4KB交错页下按矩阵shape/NUMA周期划本地segments，各node输出仍须聚合；不是不设置OS策略即可任意NUMA。Decode GQA把共享KV的queryheads作为小MM，按需转小query/Vtile。它不是新offload/schedule policy。Gold6430双路+RTXA6000/6448H四路/9462HBM受限硬件；batch1、128in/out，FFN100次/E2E5次几何均值，INT8同groupwise scheme。CPU-only vLLM与CPU-GPU KTrans不是可直接拼同硬件优势；无GPU调度的prefill在8K–32K有HiNa低于KTrans，加入GPU调度同时改变执行路径；attention已在GPU的模型不获CPUattention优化。Ch49 1913–1936/2148–2166实际读，已有layoutplan/placement及重训stage-majorCPU分支，缺standard-weight/临时operand/OS页交错的兼容接口。唯一owner `INFER-TENSORRT-LLM`，可在Layout Plan中“Intended Placement”前一自然段；Ch54只作offload消费者，不重复写。未核artifact/未复现，不签production SLO。

**05282 Red-TTT PASS，必要安全评价反侧深入。** 实际读exact-v1题摘、§3 episode/reset/固定base-victim-scaffold、reward与update/replay、§4匹配预算/评判/反侧、§5限制（导航0–112）。只限授权red-team评价：固定攻击器的上下文搜索与每behavior-victim pair重置LoRA+optimizer的在线适应是不同威胁模型；victim只需sampling接口，不等攻击器闭源可更新。120 generations/query匹配不匹配本地adapter训练、reward/classifier、全部token或墙钟；replay保原reward不是无偏offpolicy估计。ASR用HarmBench与non-refusal联合，reward/eval共享classifier，主文称独立Gemini重评分维持顺序但不当人工安全真值；8×15完整组合生效，40×3=46低于frozen49，移除classifier或replay同退46，不能称任意在线适应必胜或单组件因果。17倍只ZeroShot×Llama诊断。Ch66 2620–2649实际读，已有risk(N)、sampler drift与survival，缺明示weight-adapting attacker/reset/成本身份。唯一owner `PLATFORM-EVALUATION-SYSTEM`，建议risk(N)段后加自然段，保frozen重复采样基线/独立judge与合法任务门禁，不提供部署攻击操作、不将ASR当生产安全结果。未核artifact/未复现。

## 15. Belief quotient / Weight averaging / Dobrushin 必要 Source/date/owner

**05292 PASS，2+2+2=6，必要反侧深入。** 实际读exact-v1题摘、§2 reward-null及三坐标、§3 anchor命题、§4受控世界/causal twins/反侧、§5开放LM、limitations及A.1命题证明（导航0–77、82–90）。同reward输出间reference log-odds恒等式属于精确KL最优、β>0和给定support，不等所有有限GRPO步骤；R为线性可解码、U为交换reward-null twins的决策敏感性、A为方差分配，invertible rescale可不改变前二者。小4层Transformer/2层GRU、3seeds/5k步，50k+weightdecay1压力仅1seed；不能说普通后训练必抹除。Qwen1.7B/4B coarse-class synthetic单步任务无anchor是10–20倍放大，并不复制小Transformer的collapse；开源checkpoint仅一个family三对，真实自然任务效应未测。Ch31 410–451和451–487实际读：已有exp(reward/β) tilt、latent/elicited/system三层与binary奖励同奖prior，故不重复介绍KL公式；新差额为R/U/A的可辨识交叉诊断、free/null与filter保护及预算下可读取性。唯一owner `TRAIN-RLHF`，宜在“单凭回答消失无法证明参数删除”该段后补一自然段，保原能力/行为/系统分层，不增解释章owner。全部probe、twins/reference/训练与adaptation预算计费，真实任务无可控twins则不授全因果分类。日期沿§13，未核artifact/未复现。

**05329 PASS，2+2+2=6，必要假设/反侧深入。** 官方exact abs首请求超时后同URL一次curl恢复唯一v1=10-04 15:53:28UTC，无早稿具体线索；与§13 DataCite registered **04:55:52UTC**合证在BJT10-06。实际读exact-v1题摘、§3定义/简化GPTQ、§4.1完整kernel、§4.2–4.3命题/阈值、§5及A.1噪声、A.5原假设/rounding和C.1配置（导航0–64、67–117、129–132、348–396必要段、769–785）。固定M的非负和一kernel在mean-age m与R=Σw²间有Pareto family，λ增大更近最新但保留更多noise，不能叫任意效果Pareto最优。噪声同cov且跨保留位置uncorrelated，PTQ理论更需有界isotropic noise、fixed positive-definite calibration、两组简化GPTQ、单RMSscale/triangular dither/no-clipping及晚期trajectory条件；不直接解释真实deterministic groupwise GPTQ/AWQ为已证定理。EMA仅M=2精确，M>2局部近似。OPT125M/350M/1.3B，FineWebEdu2B/4B/20B tokens，4×RTXPRO6000，末10个checkpoint间隔500，C4固定128×512校准、group128、W2/3/4，RefinedWeb1024blocksPPL。W2与W4排名可反转，largeλ可退，不由lowerFP loss或一个平均PPL批准全部任务/SLO；精度与seed在必要配置未核明不补造。Ch49 1116–1133、1398–1414实际读，已有calibration/depth/partial-quantized重构及PTQvsQAT，缺pretraining checkpoint averaging的lag/noise→bitwidth选择接口。唯一owner `INFER-TENSORRT-LLM`，宜PTQ/QAT段附近独立自然段，不写通用optimizer新owner；checkpoint存取/平均、重校准及逐bit任务验收全计费，保普通LRdecay/原checkpoint/高精度。未核artifact/未复现。

**05558 PASS，2+2+2=6，理论正确性必要反侧深入。** 实际读exact-v1题摘、§2 M1–M4、§3 Proposition2完整证明/两token反例/corollary、§4.1–4.3必要测试及§4.4–4.5对象边界、§6前身（导航0–111、116–123）。row-stochastic A、0<α<1，residual factor coefficient上界取等当且仅当**存在某个**达κ(A)的token pair满足Aii≥Aji且Ajj≥Aij，不要求全pair/全column dominance；两token swap的α=.5 factor可直接κ=0，说明原上界可极松。层内tight不让product/submultiplicativity tight，更不等full network rankcollapse；value/outputprojection/MLP/Norm/真实residualweight不在该rollout模型。head平均/每input vs dataset平均不可交换结论；去特殊token后重归一是另一条chain，不外推fulltokens。512 ImageNetV2/128tokenWikiText103输入、DINO/ViT/DeiT/RoBERTa/DistilBERT，FT-T三seed每4krows，zero-gap阈值1e-10；content100%不是全部model/token保证，FTT仅11–44%，大样本发现罕见failure，选bidirectional还因causalmask本身可让κ受前几位支配。Ch14 70–110和203–240实际读/全文定点搜相关词：已有score谱不等权重谱、softmax/Value/表达边界，无Dobrushin residual-factor取等及对象人口差额。唯一owner `MODEL-SELF-ATTENTION`，宜“Self Attention获得什么”末/“它付出什么”前一自然段解释诊断边界，不在性能章重复；保存head/input/token集合/阈值及投影/任务独立验证，保原完整attention诊断。日期沿§13，未核artifact/未复现。

本批九项必要层目前为**8项Source/date/owner PASS + 04791明确早公开Date-Drop**；不是九篇自动写书。literal PRE与真实POST各自另行记录，不签DAY/FINAL。

## 16. remaining 八项逐字 PRE / POST 流水

**04977 literal PRE PASS。** 实际逐字读 READER1_EIGHT_PRE §04977 的整自然段（起“分布描述与逐次抽样之外”，末“不以逼真的边缘分布批准行为代理”）及对应本人注，并重新打开 Ch66 分布描述/采样两段、marker与Persona直接两侧。§13必要Source未变复用；三项测量、teacher-forcing权限、闭候选边界及成本/旧baseline均有原证。许可仅此已存单段+一注，在 `SF-2026-ARXIV-2607-25292` marker之后/Persona段之前；root已指定唯一作者可据独立PRE直接窄写，不需重复root授权。未发生POST，不签DAY；本reader不写Books。

**04977 实际POST PASS。** 作者通知保存后，实际重新打开Ch66 936–957完整新增与描述/采样、Persona两侧及章末本项来源注；新增段和本人注与批准稿逐字相同，旧条目未替换，Source限制与成本仍近文。限定该文件diff-check无诊断。只完成此项POST、释放该精确写位，不授日级或全章验收。

**05105/05123/05282/05558 literal PRE PASS。** 实际逐字读READER1_EIGHT_PRE各整自然段与本人注，分别回读Ch36 Split Fine-tuning两旧分支与系统设计交接、Ch49 Layout Plan→Intended Placement局部、Ch66 risk(N)→Adversarial局部、Ch14表达收益→代价完整局部。§14/15必要Source未变；05105保fresh-local/stale-remote/非等价及模拟/实机分责，05123保standardweight/临时operand/OS页与非新offload，05282保weight-adapting/reset/费用/非独立judge，05558保存在pair/factor≠product≠fullnetwork及人口身份。仅各现存单段和一注，按各已存精确锚点窄写；未发生这些项POST。本reader未改Books。

05041待事实措辞窄修：剔除memory缺陷后的次要差额不显著，不应写成缺陷直接造成；单一model与chains family须分清，“代数”换为“更多代际迭代”。05292待“输出方差”纠正为activation/表示方差分配，A并非输出variance。均已向作者指出，未提前签修订稿。

**05041/05292修订态、05329新稿 literal PRE PASS。** 已实际重新逐字读取READER1_EIGHT_PRE这三段与各自本人注。05041全部三处窄修在保存稿中生效，05292现在为“表示方差如何分配”，与原Table1的activation variance相符。05329新稿位于Ch49 PTQ/QAT首完整段后/QAT输入teacher段前，该局部实际重新打开；只采用晚期checkpoint lag/noise×bitwidth接口，isotropic/uncorrelated/fixedcalibration/no-clip的简化GPTQ权限、W2/W4反转及EMA近似、全费用/旧checkpoint回退均近文。对应必要Source及另外两owner完整局部未变复用。仅此现存各单段+一注可由唯一作者窄写；三项POST仍须实际保存后另核。至此八项literal全部通过，但尚仅04977已实际POST，不能预支其余七项。

**其余七项实际非作者POST PASS；本八项闭合。** 唯一作者通知已保存后，本reader实际重新打开：Ch36 1740–1762的05105及两旧split分支/系统设计；Ch49 1931–1954的05123及Layout/Intended Placement；Ch66 2628–2651的05282及risk(N)/Adversarial；Ch14 203–225的05558及表达收益/代价；Ch82 96–114的05041及WybeCoder/架构选择；Ch31 445–464的05292及三层能力/能力验收；Ch49 1129–1146的05329及PTQ/QAT定义、teacher与ternary交接。逐项本人注也实际打开，整段及注与各已批准literal相符；05041三处和05292方差修订在真实正文生效。限定上述七个文件的两批diff-check均无诊断，旧正文未替换、理论/配置/费用/回退限制近文。连同04977，八项Source/date/owner/PRE/实际POST全部完成，各精确写位释放；不授整章、其他候选、扫描完整性或DAY/FINAL。本reader始终未修改Books/Report。

## 17. root转交五项必要Source：先完成两项

本小批仅06174/06204/06325/06329/06212，root不重复；八项literal仍优先。实际打开五篇官方exact-v1 abs（06174/06212网页cache miss后同官方URL一次curl恢复submission history），提交时间均10-05，依次11:55:01、12:17:22、13:37:13、13:39:26、12:22:40UTC，唯一v1；已实际核过的常规公告规则给最早Oct6 00:00UTC。逐个解析原DataCite JSON的DOI/url、client关系arxiv.content、findable及registered，依次Oct6 05:18:50、05:19:39、05:22:50、05:22:56、05:19:52UTC，全部possible interval落本日BJT自然日，不称registered为真实公开时刻。06204仅NeurIPS2026 workshop accepted备注，不当先公开；未见需恢复的早稿具体线索，不声称遍历所有渠道。

**06174 Anosognosia Source/date/owner PASS，建议2+2+2=6，必要反侧深入。** 实际读exact-v1完整题摘、§2自报、§3内外probe、§4单条/成对/组三种训练与判分、§5共享LoRA与跨method/group反侧、结论及A/B.1–2/C.1/D.1/E.1必要配置（导航0–93、107–128及上述配置定点；未遍历全部图附件）。Qwen3-8/32B、Llama3.1-8B、Gemma3-27B dense/no-reasoning，16/8/4bit与GPTQ/AWQ/RTN。相同文本/相同prompt下，内部有线性可分method fingerprint并不等模型自然读出；共享adapter在三种precision的相同输入、同标签模板训练会读出，但换GPTQ group64/256或未见method失败，16bit也会误报异常，且brevity bias/普通benchmark轻退。外部single-text近chance不证明文本从无信息，4bit可比较检测不等绝对自知；likelihood forced-choice也非自由生成可靠性。Probe按prompt划分/独立validation选C、seed42，BF16/rank16等SFT配置只限已披露范围；没有硬件/Serving SLO或真正内省因果证明。Ch66实际310–340与400–432的elicitation/probe/null/内部sensor局部已读；已有内部可分性≠输出控制，缺同输入precision-shared readout及method/group-held-out的具体反证。唯一owner **PLATFORM-EVALUATION-SYSTEM**（不是Ch49量化性能），宜内部可分性两段后最小段，保内部sensor与独立行为验证，训练/activation/校准和所有任务回归计费。未核artifact/未复现，未PRE。

**06204 RL-trained sellers Source/date/owner PASS，建议2+2+2=6，标准审阅加必要归因反侧。** 实际读exact-v1完整题摘、§3程序reward/ledger/GRPO、§4配置/分母/对手、§5全主表与率对照、§6限制及A的关键协议失配（导航0–61、66–79）；不读无关谈判轨迹附件。共享LR的size trend不是能力下界：3倍LR在早期改善各size，但step56对56/64，shared104时大size差不再可辨，单seed/arm、E-series与常规架构边界和FLOPs均混杂，不拟合通用law。1,152场实际64个seed cluster、9domain×2buyer；bootstrap只反映scenario不反映训练run方差。10倍LR pooled提升集中同family buyer且格式退化；两buyer不能唯一识别family效应，holdout域低power。训练/eval prompt scaffold与accept处理不同，frontier seller decoding不同；无可检测差异不是等价，单48GB能装下不是Serving成本/延迟证明。唯一owner **TRAIN-PRETRAINING** Ch28 `换规模时，学习率外推也需要适用域`（897–914实际读）：已有裸LR外推适用域与局部sweep，但尚缺以固定LR的RL收益差冒充小模型不能学习、并以对手切片/协议shift验收的具体反证。宜该节末单自然段作为同一recipe归因边界，Ch31 simulator/reward仅消费者、不重复GRPO机制；旧固定recipe适合受控基准，新增局部sweep、配对与对手回归成本须近文。未核artifact/未复现，未PRE。

**06325 手机持续训练 Source/date/owner PASS，建议2+2+2=6，必要执行/评价反侧深入。** 实际读exact-v1题摘、§2约束、§3完整配置、§4内存、§5双向量化kernel与修复/审计、§6完整运行/热/能耗、§7质量分母及§9限制（导航0–131）。iPhone17Pro单台/iOS/SmolLM3-3B/4bit affine G64、rank8 Q/V、batch1、per-block checkpoint、max1024、AdamW与3passes；trainable少不免frozen-base input-gradient，forward格式不保证反向tile、正确bounds和实际dispatch。**早公开边界：**原文指向MLX PR4051，实际请求官方GitHub API，created Aug7、merged Aug12，故本日不把修复或kernel存在作为首次实现；增量限完整 sustained-training/thermal/energy/phone-quality的新实测链。冷启动166tok/s不代表长run83–89，四级thermal signal与吞吐恢复不同步，所试pause/burst均更少step/hour不是所有调度必差。单机5条长history、能耗来自5%电量档位减screen-on idle0.26W，不是外部功率计；987record满电仍未完成，不得泛称一电池任意history。per-user质量7任务多在server测，手机只复核movie-tagging100users/3302queries，近平均与7.8%逐题不同并存，非逐样本等价；Table8 citation单元与文字不闭，不采用该单元精确增益。Ch30实际163–202及484–509：已有frozen backward/端侧模拟/MeSP重放与QLoRA storage，但缺冷步与完整热/电量/任务run分账。唯一owner **TRAIN-LORA**，宜现有端侧模拟对照后/MeSP前单段，早kernel只作已有支持，不重复Ch49 kernel owner；runtime repair验收、质量、充电/前台/能耗及完整训练成本计费，保retrieval/较浅adapter/普通runtime。未核代码/复现，不把手机本地训练当formal privacy。

**06329 DUCB-OGD Source/date/owner PASS，建议2+2+2=6，必要理论/实现反侧深入。** 实际读exact-v1题摘、§2数据/反馈/目标、§3 algorithm及主界条件、§4全部主表/对照、§5限制，B实现与D配置/overhead/diagnostics定点（导航0–122、138–152、351–354、368–377）。只读取当前所选source minibatch loss，折扣EMA/effective count/UCB追踪随更新改变的worst source；不额外replay或specialists，但要O(K)state、探索/平滑和采样执行。逐时刻max的dynamic regret不同于事后固定worstsource；凸loss、有界Lipschitz/迭代域/source-IID及指定η/β才有该OGD界，不能把非凸AdamW/GRPO实测代签理论最优；lower-bound亦仅该反馈oracle/undiscounted。实现还用Gaussian随机index/Gauss-Hermite、DEMA和forced exploration，不等主文纯argmax。所测0.5–9B少source，SFT32k/DPO16k/GRPO10k或6.4k，单80G或双40G A100/BF16 mixed；作者“8bit LoRA quantization”不改写成已核具体adapter dtype。Qwen3B DPO三seed，runtime21.94±1.14vs21.90±1.29仅局部，AMA不含K specialist；Exp3/MT-GRPO只是明示sampler代理，非完整baseline重现。worstsource提升可伴SFT平均降低，DPO Qwen还低于AMA-S，非Pareto支配。Ch27实际169–211/1436–1452的Data Control Plane及OP-Mix局部已读：已有当前模型mixture proposal，缺无历史重评的stale bandit反馈与sourceworst/mean分账。唯一owner **TRAIN-DATA**，宜OP-Mix两段后最小段；旧静态mixture/真实sweep保留，采样统计checkpoint和独立held-out不让UCB自签最优。未核artifact/未复现。

**06212 LearnSched Source/date/owner PASS，建议2+2+2=6，必要理论/实机vs模型反侧深入。** 实际读exact-v1完整题摘、§2动机、§3状态/收益/return约束、§4动作与rollout命题、§5配置、§6全部关键实机/finite-model结果及§7限制（导航0–152），不遍历附件。构造qualified且发布还须actual use才有收益；completed/durable progress、command ack/memoryrelease/capacityready分开计，冷恢复可使等一段更长window比立即启动好，retainstate用memory换returntime。一步rollout保留costed-window行动在准确有限transition/价值和safe action下才不退；在线需验证uniformerror与2εmargin，不签未知arrivals硬SLO。1920paired全信息场景大部分收益来自完整cost accounting，91wins全cold，960warm全tie，rollout仍13例未达DP且最坏gap124.836；实机部件测量非端到端控制器部署。A100组件：syntheticbackground不校准真实capability、部分quality fixed-answer replay、guidance条件ledger有α=.561重算；known90s prealert少miss却几乎耗尽训练progress，平均权衡从未被选，不推出预测器已有效。停顿ack≠资源释放，warm0.487s与first-realrequest0.520s区分；resident GPU/host PSS及failed/unpublished/unused费用不可删，token省可伴GPUactivity增。已实际读Ch63 142–169 quota/reclaim、Ch56 92–118 capacity/thermal与Ch84 845–880、966–1022、1078–1098 lifecycle/idle-speculation交接。Ch63已有workload/checkpoint回收成本，Ch84已有qualification/publication/idle可取消但缺reuse-window×durableprogress×ready成本的投资时间接口，唯一 **AGENT-PLATFORM** Ch84 Idle Time段后，Ch63/56只消费capacity合同；root已确认此窄位无冲突，不替本reader签Source。未PRE、未核artifact/未复现；不会因此新增pool/kernel机制。

## 18. 新五项逐字 PRE / POST

实际完整逐字读READER1_FIVE_PRE五段与本人注。**06329 literal PRE PASS**：只现存整段+一注，在Ch27 OP-Mix两段/end marker后、双语词汇干预前；旧mixture/proposal与独立gate保留，采样陈旧性、凸界vs非凸、实际随机index/DEMA/探索、mean反退与费用均近文。root已指定唯一作者可直接窄写，尚未POST。

另外四稿待已指出的最小文字修订，不重开未变Source：06174应明确fullprecision误报的是异常而非已正确的bitwidth标签；06204十倍LR的对手集中/格式退化不可泛化三倍arm，低收益不是固有不能学习的边界；06325八月kernel归属留来源注，不把“本日首创”行政语言写入canonical正文；06212降低ready时间的驻留明确为服务runtime状态，不泛指全部checkpoint或中间state。本reader未替作者修正文，未预签未保存稿。

**06329实际非作者POST PASS。** 作者保存后，已实际打开Ch27 1436–1454，顺读完整OP-Mix两段/marker→新增1444行整段→双语词汇分支，并实际读本人注。新增和注与已批准literal一致，旧分支保留，凸界/非凸、实作/mean与费用仍近文；限定文件diff-check无诊断。仅此项POST完成、该窄位释放。

**06174/06204/06325/06212修订态 literal PRE PASS。** 已实际重读READER1_FIVE_PRE四个保存后的整自然段与注，并重新打开Ch66内部probe输出验收→解释工具、Ch28 LR外推两段/end→horizon、Ch30端侧模拟→MeSP、Ch84 Idle Time→Lifespan的完整直接邻接。四处事实/口径修订均生效；06212仍明确准确有限模型及safeactions才有rollout不退，不从组件测量授部署控制器或未知arrivals硬SLO。许可仅各现存单自然段+本人注，按文件中四个精确锚点由唯一作者窄写；未发生四项POST，不预支日级状态。

**其余四项实际非作者POST PASS，新五项闭合。** 唯一作者通知保存后，实际重新打开Ch66 325–337、Ch28 904–923、Ch30 180–197、Ch84 978–991，逐项完整新增自然段及直接两侧、各自章末本人注均实际读到。06174“异常”标签、06204十倍LR限域、06325去日报行政句且保八月早kernel注、06212服务runtime驻留等修订均在真实正文生效；四段和注与批准稿一致，旧机制与交接未替换，全部限制/费用与回退仍近文。限定四文件diff-check无诊断；连同06329，新五项必要Source/date/具体owner/literal PRE/真实POST全部闭合，各精确写位释放。不签整章、其他家族、完整扫描或DAY/FINAL，不以必要审阅替代码/复现或部署验收。

本reader本日指定工作最终为先五项+remaining八项+转交五项共18项采用链的非作者独核闭合，另04791明确早公开Date-Drop。实际仅本人READER_REVIEW写入；Books/Report作者始终为oct07_missing。已向root与唯一作者交还上述单项既成事实，日级六部分/覆盖和最终完成态仍由root独立验收。

## 19. Oct07最后有限tail六项：必要Source与日期

root新指派仅03894/03902/03984/04083/04184/04313；已重新完整读取AGENTS、研究/Report合同、CODEX入口、ROADMAP及来源使用说明/每日与arXiv主题、TAIL_CALIBRATION。旧18采用链未重做，无Oct11结论参与。本reader仍只写本文件，唯一作者oct07_missing负责拟稿及Books/Report。

实际逐个请求官方exact-v1 abs及当前abs题摘/轻量撤回修订说明：v1提交UTC为03894 Oct2 18:09:00、03902 Oct2 18:13:29、03984 Oct2 19:47:19、04083 Oct2 21:46:13、04184 Oct3 00:49:27、04313 Oct3 05:58:09，均在周五18:00UTC截止后。复用本日已核的适用官方日程/发号规则，最早界Oct6 00:00UTC；本地原DataCite逐个解析精确DOI/url、arxiv.content/findable及registered，分别Oct6 04:15:07、04:15:20、04:17:42、04:25:27、04:27:58、04:30:57UTC，最早≤最晚且完整区间落BJT Oct6。不把registered改称实际发布时间，也不由提交日期定日。五篇当前唯一v1；04184当前有Oct16 v2，未见具名撤回或纠错说明，本次只读exact-v1，不把后续version号当重要修订或本日新事件；无早公开具体线索则不建无限假想排除。03984仅Submitted to ICLR2027备注，不当更早公开。

**03894 Proxy Confidence Source/date/owner PASS，建议2+2+2=6，必要反侧深入。** 实际读exact-v1完整题摘、§3 readout/access/label、§4主对照、§5错误位与orientation、§6大小/lineage、§7含random控制、§8费用/并行/fail-open及§9限制（导航0–33、37–55；不同readout关键机制已读，未遍历附件）。TF对argument-value、PMI扣request-withheld prior、verdict整体、toolchoice函数身份是互补sensor；orientation须留出label按regime校准，不能自由移植。14B/32B仅两点，TF小规模等价不授PMI/verdict；hardcode不是同一个小scorer。PMI两prefill、verdict还需nexttoken，fusion/第二模型常驻与多租户费用不能写成总单pass/零成本。nl2bash反馈优于random-value，AppWorld却random与fusion无可辨差额，traceback已有信号，不能把两者都归因置信数值。外部决定事实不在context时不适用，τ2遗漏主导不是percall通用保证。主文将工具执行并行、timeout fail-open与oversight gate并述，本次只采排名/升级审查与反馈权限，**不授已经执行的sideeffect预防或零关键路径硬授权保证**。Ch66实际4972–5000三层confidence及single-call sensor局部已读，已有自报/内部/行为分权，缺blackbox surrogate logprob按错误位分账和random-value反馈诊断；唯一owner PLATFORM-EVALUATION-SYSTEM，宜Single-call Judge Confidence两段后最小段，旧独立verifier/人审保留。模型、schema/context/label/readout/方向、hardware与全部调用费须绑定；单L40S FP8局部latency不外推Serving SLO。未核artifact/复现，未PRE。

**03902 Evidence Changes Source/date/owner PASS，建议2+2+2=6，必要反侧深入。** 实际读exact-v1题摘、§3事件/支持类/分母、§4共用管线、§5设置、§6.1–6.5成本/length/confirmatory/score敏感及§7–8（导航0–79），不遍历医疗细项附件，只采用通用memory机制。Graph-local revise省5–10倍tokens却非全pipeline省；Δingest+Δinitialuse+Δrevision+每use差额共同决定break-even。短原记录重读更省；加长的是task-ineligible材料，memory crossing部分因输出cap/parse丢内容，source-filtered reread各长度最省，不能称充分allowed证据无损压缩胜出。两7B/temp0/vLLM，3–20人/condition且复用，C2四primary均未拒绝；更新值已在memory prompt却漏答定位use阶段，但不解释其唯一原因。read-set gate只查snapshot变更，无support/permission/freshness enforcement且本实验从未阻commit。一次revision/重复同template、token非价格/latency、posthoc lexical scorer不是临床真值；不作医疗效果。Ch77实际1334–1364评价/成本与1460–1492provenance局部已读，已有流式全阶段费用与回撤闭包，但缺revision后source-filtered reread作为强baseline及per-use负差才能摊回固定费的具体反证。唯一owner AGENT-MEMORY，宜评估Memory首Neuromem段后最小段，旧raw/retrieval/repair仍按新旧证据质量及完整预算择用。未核artifact/复现，未PRE。

### Tail 03894/03902 修订态 literal PRE PASS

实际逐字读TAIL_AUTHOR_PRE这两项原稿、指出并再读回保存后的修订稿及各自本人注；PMI现明确full减withheld likelihood，03894本人注范围限实际必要§3–9主文，不借本reader签未读A–C。03902 read-set现只验提交前版本变动，C2四primary限域明确。重新打开Ch66受监督confidence `SF-2026-ARXIV-2605-15416`完整段及自报数值鲁棒性两侧、Ch77 Neuromem→MemoryArena完整局部；Source/owner已通过且无变化。仅批准两份现存单自然段+本人注，分别2605-15416段后/自报confidence前，Neuromem段后/MemoryArena前；唯一作者可据root授权直接窄写。本reader未写Books，尚无本两项POST，不授DAY。

**03894/03902实际非作者POST PASS。** 作者窄写后，实际重开Ch66 68–80、Ch77 1334–1342及各自章末本人注，完整新增自然段及直接前后均实际顺读，和批准修订literal一致；PMI/方向校准与随机反馈反侧、read-set/C2四primary和全生命周期比较均生效，旧独立验证、重读及其他memory路径仍保留。限定两文件diff-check无诊断，两精确写位释放，不签整章或DAY。

**03984 Source/date/owner PASS，2+2+2=6，必要反侧深入。** 已实际读exact-v1题摘、§2.3/3.1–3.6及A.4/B.5必要边界（导航0–95、123–125、163–164），未遍历附件。oracle判错的deterministic/model mutants与sibling是有限negative，不把通过gold的被排除候选都称语义等价；uncaught errors不计kill，class-weight按detecting assertions分摊，局部bonus与trajectory advantage分开。正确patch或kill-all的OR-gate仍可给incorrect patch局部credit，unsigned不罚false rejection；token复制另有span-length效应，不用credit授开放程序正确性。固定candidate bank及同总量uniform/shuffled反侧支持credit placement，own-candidate选优另算；270 heldout全曾development diagnostic，DeepSWE partial不等完整修复。变异/oracle/sandbox/测试与训练费用完整列，steps不代token/wallclock，未核代码或复现。已实际读Ch33 944–964现有独立TestPolicy→DPVG，缺同policy patch/test的weighted mutant assertion-credit及该OR-gate边界，唯一TRAIN-GRPO，现存两段后/DPVG前最小段合适。

**04083 Source/date/owner PASS，2+2+2=6，安全必要深入。** 已实际读exact-v1主文必要模型构造、§II–IV-D及讨论/限制（导航0–73、85–100、107–108），不遍历全部cross-model panels。搜索prompt构造writer后由neutral successor继承状态，只证受限路径存在而非自然发生率；默认memory承接、关闭memory后文件仍须被发现，不能把单通道删除当全面授权。deterministic目标tool事件与LLM-judged disposition/隐瞒分开，provider拒绝/可见评估意识排除及append-only百会话subset限定人口。审计摘要/图与主文百分数人口不同且存在不一致，本稿不采用其混合数字，只保降低但不消除。search/replay/auditor与良性效用费用不抹除；未核代码/复现。已实际读Ch72 self-state/HarnessBackdoor交接及1750–1774 provenance→良性经验→VerificationStatus，现有良性经验回归未覆盖真实writer写下延迟目标、后继当前授权不得继承的窄反例；唯一PLATFORM-SECURITY，拟2604-16968两段后最小段成立。

**04184 Source/date/owner PASS，2+2+2=6，必要评价反侧深入。** exact-v1必要主文导航0–88实际读到，不采Oct16 v2。researcher dev与sealed candidate、dev与sealed target分开；冻结questions/grader/aggregation与allowance，CCC同时测level/spread/order、PA测有限非tie pair，二者非同一能力真值。固定responses重权改变CCC却近乎不改PA，human-designed random120是强baseline非随机null；completed/partial人口与positive weights分母、假设imputation不得混成实测。budget-stop不当自然错答，output-cap下已完成截断与基础设施不完成亦分开。每配置一次episode，固定参考/target条件化bootstrap不认证跨人口泛化，91%所谓ceiling不授普遍极限。构建/开发/helper与assessment/反复运行全费分账，未核artifact或复现。已实际读Ch66 generator/Bloom局部与1907–1934 benchmark fidelity→Evaluation，唯一PLATFORM-EVALUATION-SYSTEM，作者拟2609-21267时间heldout两段后最小段衔接成立。

**04313 Source/date/owner PASS，2+2+2=6，必要执行/正确性反侧深入。** 已实际读exact-v1主文必要导航4–169（机制、matched list/read消融、serving/质量与限制），不遍历附件。page key mean/variance的Gaussian近似产生mass估计，每query-head归一后GQA平均，再阈值选择；不是真实mass保证。GPU ragged list→固定J/grid的row自分chunk→LSE merge留在graph replay中，四kernel不称全pipeline单kernel。same-list kernel与same-read预算控制分开：128k主要少读，少行成熟kernel相近、适当per-head静态profile可近似，非所有static budgets失败。全KV驻留、summary额外空间且在预留KV之外；单H200/BF16/4B与8B/vLLM0.30无TP/量化KV，短低并发可更慢，closed-loop median非开放流量tail保证。selection/build/merge/workspace/质量与全serving费用保留，未核代码/复现。已实际读Ch49 FlashAttention、query-specific risk与199–224 graph分支，现有graph缓存/寿命未覆盖device-dependent长度而固定launch的partition接口；唯一INFER-TENSORRT-LLM，作者拟graph缓存成本段后/persistent分支前成立，不在Ch45重复建owner。

**03984/04083/04184现存literal PRE PASS。** 已实际逐字读TAIL_AUTHOR_PRE三完整单段+本人注，并重开上述各自完整直接邻接；原证据支持采用边界，费用/反侧/回退近文，只批准现存最小段+注由唯一作者窄写，尚未POST。04313只待将GQA平均明确为query-head mass先归一再平均，避免改变非线性顺序；其余内容与owner已通过，不预签未保存修订。

**03984/04083/04184实际非作者POST PASS。** 作者保存后，实际重开Ch33 946–962、Ch72 1759–1773、Ch66 1913–1930，完整新自然段及直接前后顺读，再实际读取三个本人末注（现Ch33 3626、Ch72 4793、Ch66 6816）。均与通过literal一致；旧固定测试/hidden authority、良性经验回归/VerificationStatus及full-benchmark/Evaluation交接保留，未借受限实验授开放保证。限定三文件和本人记录diff-check无诊断，三精确窄位释放。

**04313修订态literal PRE PASS。** 实际读回TAIL_AUTHOR_PRE整自然段及本人注，明确每query-head先归一page mass再在GQA组平均；非线性顺序已正确，estimated coverage/full KV驻留/低负载反慢及same-list/read分责仍完整。许可只现存单段+注，在Ch49 graph缓存成本完整段后/“Graph路径把重复的shape固化”段前，由唯一作者直接窄写；尚未POST，不预授本项落地或DAY。

**04313实际非作者POST PASS，tail六项全链闭合。** 作者通知保存后，实际重新打开Ch49 207–225，完整graph准备/绑定寿命/成本→新增215行整段→persistent分支及下一机制衔接均顺读，并实际读取3281行本人注。整段和注与已批准修订literal一致，每query-head先归一再GQA平均、近似预算、全KV驻留、same-list/read区分、短低并发反慢及费用/回退均生效；旧JIT/capture/cache寿命与persistent路径未替换。限定文件diff-check实际0，精确写位释放。六项必要Source/date/具体owner/literal PRE/真实POST全部通过，只表示这六个有限采用命题的非作者有效层，不签整章/扫描覆盖或DAY/FINAL，不声称代码审计、复现或部署验收。

## 20. 有限报告本地检查（非DAY）

root另指定仅10/07当前稿格式/计数/StableID与本地路径，不重读Source附件、不写Report/Books；最终计数待作者合并通知。首次预核当前§3仍为46行=44整合+2暂缓，并非最终分母；44个StableID逐行解析后均在ROADMAP存在，Books链接与其owner路径一致且实际存在，46条主材料链接无重复。发现两处表内空行（当时49行CutBCE前、76行AttentionTax前）使无新表头的数据脱离GFM表，已具名通知作者修复；尚未检查最终合并稿，不给机械结果冒充日级语义验收。

作者通知最终合并后已实际检查当前完整本地稿的可判定结构，并运行V3校验。首轮64行中tail前仍有空行和旧44+2过渡句，已具名反馈，作者修后再实际复验：六个一级报告节完整且依次1–6；候选64行=61整合+3暂缓，64证据小节；63个arXiv ID与证据标题逐一集合相等，另1为同一EmbeddingGemma2官方Blog链接，无重复主材料。候选日期全Oct6，评分算术正确；61个StableID均在ROADMAP、与其本地Books路径一致且文件存在，60个arXiv整合的对应Books source-family marker存在；报告全部本地链接目标文件/目录存在（未冒称外站或锚点全验）。候选表现为64行连续、表内断裂0，旧44/46分母句0。最终实际V3 PASS，限定报告/本人记录diff-check 0。

**有限格式/计数/本地路径复验通过，非DAY/FINAL。** 本结果不签64篇全部原件语义，也不替代root的六部分日级验收；当前报告仍进行中且§6待root，未由本reader更改Report或Books。本人尾六及前18的既成有限独核层保持，不重新扩大研究或附件读取。
