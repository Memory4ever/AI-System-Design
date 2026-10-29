# 06-10 第三批必要证据与实际 owner 差额

本文件承接本日独立准入/日期核验（SUP_REVIEW §6）。七处既成整合已由唯一非作者实际 POST 通过，不重复申请。以下只申请具体新增窄位；本文不是 Books 已写或日级验收。

## Still 2606.07878v1（2+2+2=6）

作者实读 exact-v1 §2–3、§5 Discussion/Limitations，reader已独读 §2–5。每 base checkpoint 专训 per-layer forward Perceiver compactor，所有 KV heads 联合读取，冻结 base model；先 inverse-RoPE 输入 key，再在 compact positions re-RoPE，continuation仍用原 prefix offset。可选 bias 实测 β=0。不是同一已训练 compactor 跨 checkpoint 零样本迁移。

Single-pass先完整 Prefill，只节约保留与后续读取；迭代 recurrence 的 retained T/c+ct 是固定 ratio，不是 O(1) memory。8K 训练到128K的1.5%低于 no-context，32K训练39.2%，horizon失配是直接失败证据。MCQ训练/评价、三 training seeds 与 HELMET/iterative 的 single-seed bootstrap不混；LongBench生成另训generation-aligned checkpoint，不能外推任意开放生成/精确回忆。压缩参数/专训数据与 GPU、每层 forward、lookahead buffer及原 Prefill全部计费，未核实现/复现。

actual `INFER-KV-CACHE` Ch45:797–825完整直接上下文已读：805/807已有连续合成、amortized lossy与fallback；809 Attention Matching已有logical length/original RoPE及bias拟合。差额不是泛合成而非selection，而是checkpoint专训forward转换与迭代horizon。建议唯一位置：`SF-2026-ARXIV-2603-27819`完整两段后、以“拟合一块压缩缓存时”起的完整段前；只加下段与本人true-H2 source注：

> 若逐request优化合成KV难以摊销，还可为每个base checkpoint专训逐层forward compactor，把原缓存映射到较少的合成条目。输入Key先撤销RoPE，合成后再按compact positions旋转，而后续token仍沿原prefix offset续接；这不是把压缩后的物理长度当原位置，也不是同一compactor跨checkpoint免费通用。[Still的受限分支](https://arxiv.org/html/2606.07878v1#S2)在报告结果中不用额外bias，single-pass仍先完整Prefill；迭代chunk加lookahead只维持固定压缩比，缓存仍随历史增长，并非O(1)状态。训练horizon不足时，重复压缩甚至可低于no-context基线，生成任务也需相应训练分布。专训参数/数据与GPU、逐层转换、buffer和原Prefill都计费；horizon、任务或质量失配时，保更大缓存、原选择/离线拟合与FullKV，不把一次可用的合成状态当无损或无限递归记忆。<!-- source-family:SF-2026-ARXIV-2606-07878 -->

## DRPO 2606.09821v1（2+1+2=5）

作者/reader exact-v1 §3–4、Appendix D必要配置；actual Ch33:2289–2315已完整读。已有“Binary-TV一类连续约束尝试”明确条件机制分支，理论窄E成立，不授实测越界纠正。

Eq10 D=|π−μ|≤1，只有D>δ才负向修正；实测δ=12.5不可能触发。必要定点作者repo恢复已足：`SUP_DRPO_CODE_20261025.json` Git blob 76cabd813d17b74eb4b2dbb66c6d17f8b3422950，`SUP_DRPO_CONFIG_20261025.json` blob 05e2d887fc6c8f418a093ffd375695950ebedc59，及 `SUP_DRPO_README_20261025.json`。已去base64空白解码必要 loss/config/公式：默认epsilon12.5、mu_weighted=true、adaptive_eps=epsilon/old_prob、二次项除以2epsilon，无隐藏倒数换算；README同Eq8/10。当前blob不认证Jun09原实验代码身份，也不解决公式/阈值冲突。reader已独解核对，停止扩全repo。实际纠正归因争议终态隔离，不写Books；精确重开为同版本实验的δ单位/倒数定义、勘误或可对齐代码/config与对应负权重trace，不由一般平滑稳定性替代争议。

## SecureClaw 2606.09549v1（2+2+2=6）

作者/reader实读exact-v1 §2–6；reader独核actual Ch72:2422–2438 read boundary随机HMAC nonce handle、caller/session/TTL/object/sink绑定、summary显式declassification及残余，和1969–1989 canonical typed action→digest/policy/state→short-lived single-use artifact→executor exact effect gate，已具体承载两条责任链。E不只是主题相似，不新增Books。

采用边界：trusted gateway/store/policy/executor与完整mediation是前提；摘要仍可泄漏。629 AgentDojo/496 AgentLeak/2000 ASB不同协议不合并，16/496 plaintext leak、效用误拒与费用保留。29 bypass scenario不证明任意攻击/被攻陷TCB或生产安全；未核实现/复现。只用v1，不借Oct14后v2/v3。

## DCMDP 2606.08779v1（2+2+2=6）

作者实读 exact-v1 §3–6/Appendix A full algorithm；reader独读§3–7/Eq8–11与实际 Ch33:1880–1942，不称reader另读Appendix A。对同一序列在old inference/train backends读取概率，绝对差作为token cost从task advantage扣除；batch平均超过c则增λ、低于则降、投影到界内。不是要求两graph严格bitwise相同。§6 Qwen3-8B FSDP2/30B-A3B Megatron，DAPO-Math17K、G8、8192训练/32768评价、vLLM0.11.0、六数学任务avg@32/4、dense8GPU/MoE32GPU且GPU型号未披露；BF16与BF16train/FP8infer协议分账。c过小λ饱和/阻碍任务、过大退化GRPO，lambda与c搜索及多backend forward费用保留；未给训练seed不确定性，不把rollout K当独立训练重复。Table1 Minerva8B 50.1<51.0，拒“every benchmark胜”。

中心保证不采用：Eq6∀trajectory约束与Eq11 batchmean控制不是同一资格，Eq7 delta_old对theta固定而宣称直接等价advantage shaping不闭；threshold正文触发区间内外反写。只将Eq8–11/Alg1当作者明确给出的sampled-cost/dual启发分支，不授CMDP硬可行/收敛定理或自由探索区域的逐token零penalty。v2轻量信号已实际核：`SUP_ABS_2606.08779v2_20261025.html`，Jun09 07:53:57Z提交，题摘与v1一致且同2122KB、未见具名勘误；只据此不扩全版本史，不断言全文无变化或该次提交即公开。

actual Ch33现有sameweights≠samepolicy、precision graph/scale/kernel与MoE replay，以及samegraph/real lowprecision alignment；差额为接受可测小mismatch并用经验cost调节的替代分支。建议唯一窄位：完整`SF-2026-ARXIV-2610-24914`段后、`semantic-body-binding:SF-2026-ARXIV-2609-22870:start`前（再回到aligned FP8 surrogate边界）。待一次原稿核/root窄授，不自行写：

> 若两端数值路径无法完全统一，另一条有条件的分支不是隐藏差异，而是在同一old weights、同一token序列上测inference/train概率绝对差，把它作为token cost扣入task advantage；再用sampled batch平均与经验容忍预算比较，调节有界penalty权重。[DC-GRPO的受限配方](https://arxiv.org/html/2606.08779v1#S5)允许在任务探索与差异压制之间作经验取舍，但batch均值控制不保证每条trajectory满足硬约束，印式也不足以认证所称Lagrangian等价或收敛。预算过紧会压制学习，过松则几乎回原GRPO；六数学任务的dense/MoE、BF16/FP8结果亦非逐项都胜。双backend重算、cost metadata与阈值/权重搜索都计费，backend或数据变化须重新校准；cost不能预测任务损害、质量回归或身份不可核时，保数值路径对齐、较高精度与原更新基线，不把低平均差异当policy等价。<!-- source-family:SF-2026-ARXIV-2606-08779 -->

## Cold-Start Safety Gap 2606.07867v1（2+2+2=6）

作者/reader已实读 §2–6。SODA 16environment×5scenario×5threat=400，D为已完成regular task数而非token数，8个depth/3seed、七模型四family；真实工具交互与拼接compliant/random/empty history对照分开。外部AgentHarm Opus4.6 judge，ASB ShieldAgent另协议；BFCL200状态task与APIBank207参数匹配。T1各模型D20比D0高，但局部回落；T2 Qwen allrandom/allempty反退；T4 Full Qwen30 BFCL72→68/API87→85、Gemma亦局部退。不得monotonic/anyhistory有效/utility无损。PCA+线性boundary是posthoc可读出关联，无因果干预，不采用激活persona已证机制。

actual Ch66:5128–5167、5427–5455完整已读。Repeated inference现段拥有同一条件反复采样的纵深，缺固定同threat但改变已完成任务history的另一轴。建议在`SF-2026-ARXIV-2602-11786`完整两段后/“部分评测必须预先声明停止…” H2前加一段，避免新H2及重复泛安全警句：

> 同一会话内已完成多少任务，是另一条不能被重复采样次数代替的轴。可固定同一threat与工具环境，先让Agent完成不同数量的正常任务，再比较其安全与合法任务效用；真实interaction生成的history、拼接请求/空或随机response应分别标记，不能把“深度”默认为等token或等wall-clock。[SODA的有限对照](https://arxiv.org/html/2606.07867v1#S2)显示cold-start与较深history可产生不同安全结果，但不是逐点单调、任意前文都有益或效用无损，hidden-state线性可分也不证明persona被因果激活。History制备、工具执行、context与judge成本须全计，任务与judge协议变化仍需重测；无法校准或暖场损害效用时，保fresh-session与stateful双臂、外部权限/效果gate及Unknown，不由暖场安全分数批准部署。<!-- source-family:SF-2026-ARXIV-2606-07867 -->

## CFD 2606.09084v1（2+2+2=6）

作者/reader已读exact-v1 §3–6与B.3预算必要段。严格context wipe与persistent artifact store是threat前提，局部monitor当前request/tool name/args与offline全trace/最终artifact oracle不是同一观测对象。聚合query+benign noise不是完整trace lineage；lineage-tag防御仅future calibrated implementation，不声称已验证。六模型AgentDojo过滤exfiltration子集、三评价run，不授生产频率；Mistral ToA52.83>CFD37.11保留，topology不同turncaps30/25/20不能把差异全归agent数，最终artifact检查还漏transient exposure。未核代码/复现，不扩payload全附件。

actual Ch72:2026–2066完整论证已读：局部动作组合→sequence-level evidence；risk state跨iteration/reset保留；拆分子任务跨委派，source/delegation/memory write/irreversible sink带provenance并在commit前重建上下文。2228–2275又明确同run片段重组不是跨session、`entry→persistence→benign trigger→observable effect`与跨会话carrier identity/lineage。具体机制已承载，拟E而非制造一般provenance重复段。论文仅有界实证/未实现defense与数字反侧保报告，等reader一次E核。

## CausalAgentReplay 2606.08275v1（2+2+2=6）

作者实际读 §2–7，reader独读§2–8。保存s_k完整prompt/schema/history，固定factual prefix，在k对同policy重采action，再run-forward K次；另提供action/observation/context/policy interventions。Hosted provider温度0也不保证重复，报告action-match而非强行确定性。此效应含下游重采，所以早先无关step也可显示总效应；latest CI excludingzero的point-of-commitment仅是此estimand里最后可救run的位置，不是唯一rootcause/直接效应。直接效应仍需common random numbers等控制，当前未做。

单步proportion Wilson与difference bootstrap；MC permutation Shapley+antithetic pairing处理interaction，coalition value不跨permutation缓存以免压零方差；normal approximation CI/预算cutoff与相关随机噪声边界保留。三步植入SCM与AND-failure analytic .91，对应估计.44/.45是有限groundtruth回归，不是开放Agent因果真值。工具mock/reproducible，真实side-effect tools明确outscope；用户自定义Y与judge噪声仍约束结论。未核实现/复现，不将demo当生产能力。

actual Ch66:5388–5432与700–735完整已读，Ch67定点causal/replay/Shapley检索未见该机制：前者已有span/firstcommitment不是rootcause、logjudge改选不等干预；后者TraceElephant已有可见性/后续恢复责任与有限局部hypothesis probe。差额是samepolicy executed-null的下游重采混杂及对应estimand/interaction。reader已确认原稿较后位置更聚焦并通过：唯一在`SF-2025-ARXIV-2509-06822`完整段后、“Failure Catchability…” H3前加下段+trueH2本人注；TraceElephant仅作已有覆盖比较，不用作另一插位。待root窄授：

> 有可重放环境时，还可固定事实prefix，在某step从同一policy重采action，再让后续重新运行，比较多次outcome分布；provider即使温度为零也应另报replay action-match，而不预设确定性。但这种run-forward会连下游关键决定一起重采，早先无关step也可能显示总效应；[CAR的受限分支](https://arxiv.org/html/2606.08275v1#S4)把最后仍可改变outcome的显著step称point-of-commitment，仅定位该estimand中的最后可救位置，不认证唯一根因或直接效应。存在联合失败时，可另用coalition重放的MC Shapley分配贡献，不能把多个单步总效应直接相加；区间近似、随机共因与预算截断仍限制可信度。完整state/随机输入记录、重复rollout、outcome oracle和排列搜索全计费，当前验证只含植入SCM与mock tools；真实副作用不可安全重放、provider身份或oracle不稳时，保离线多候选、人工/确定性复核与Unknown，不由解释图批准线上干预。<!-- source-family:SF-2026-ARXIV-2606-08275 -->
