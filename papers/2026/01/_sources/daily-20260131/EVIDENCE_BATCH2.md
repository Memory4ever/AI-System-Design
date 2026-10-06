# Batch2 必要匹配证据与 Books 提案

本日独立作者；精确 v1 的采用段在 CORE_STANDARD_<id>v1.txt。8 家族的日期原值/区间见 DATES.md；不声称复现或实现已验证。以下处置待 root 必要原源/实际 owner 复核，不把标准完成等同因果证明。

## 2601.22035 — Thinking Out of Order

采用输出 schema 与 decoding/unmask 条件下的 order robustness 反侧，2+1+2=5。§3/4 用同题 CoT-first/Answer-first 及 ReasonOrderQA 1000题四难度算式/秘密整数检索固定知识输入，retrieval F1 是可见 delimiter 段整数集合，不是内部推理真值。§6.1 D2回答在检索前约55% plateau，D4约1%是局部容量边界；§6.2输出长度64→256改变 retrieval 达到.95时刻，不能把长度变化当固定计算干预。§6.3低置信策略69/57.3 vs左到右64/47.2、Qwen91.8/29.4说明相对顺序敏感不等于绝对任务更强。

Appendix A明确 LLaDA8B generation/block/steps=256、A100、temp0；Dream7B temp.1为避免退化，Qwen2.5 7B max512/temp0。模型架构、预训练及生成预算不是严格匹配，不证明 diffusion 因果优于AR。precision、batch/concurrency、wall-clock未披露，SLO不适用此离线质量实验。采用局部 schema×decoder 现象与不足，非强“推理先于输出”解释。

Books拟仅报告：Ch24正文280–316已经把生成位置、confidence commit、budget/refresh及质量退步分开，本文给同题受控反侧，不建立一个可迁移的最优次序或新的生成状态契约。保留作为 decoder/order 联合评价案例，不伪称已有具体 ReasonOrderQA 算法。

## 2601.22031 — CARD

采用 causal attention 下密集 corruption-prefix supervision 与逐块提交接口，2+2+2=6。§3.1–3.4右移目标、soft-tail可腐化区间、按先前mask密度加权；predict original next token from corrupted prefix，不是同位置双向填空。推理 confidence并行接纳，已提交token不remask，完成块可保留KV，达到硬step上限强制填剩余位。模型容量与条件样本数不能因 combinatorial count 就称可学性保证。

§4.1/4.2 1B、FineWeb300B tokens，ARM/MDLM/BD3LM不同kernel/padding等实际差异；ARM平均56.39高于CARD53.23，不能借超过两扩散baseline声称全面优于AR。§5.3/5.4 Table4 full53.21、strict-tail52.5/random51.62/no-weight51.66支持局部消融；Table4 MMLU列名2535与前文2565不一致，不汇总未核细目。110M33B的EMA PPL ARM21.12 vsCARD21.54也不全面优越。Appendix B BF16/FA2/AdamW、33层1536、seq128、1Msteps；文字constant schedule与Table6 cosine冲突，附录 bidirectional 与主文 causal 描述也不一致，保留未决配置，不采用精确训练效率。§5.4 generation batch=128明确，训练硬件与推理完整precision/concurrency/SLO Not Disclosed，不能笼统写batch未披露。Appendix D两qualitative例中硬限4×重复，不把1.7×/4×称生产收益。

Books：root 实际必要源与 Ch24 对照后 PRE 通过，单流 corrupted-prefix 全位置监督与 causal visibility/block commit 三个独立选择确有窄接口差额。已在 Ch24 MARS 段后窄写两段及末注，实际722/724、完整前后及末注经 root 非作者 POST 通过，锁释放；不是以具体配方缺位自动改书，不采 MI 或同 AR 吞吐保证，不授日级 Gate。

## 2601.22030 — PerTA

采用 forget/retain gradient proxy 对 negative task-vector subtraction逐参数缩放，2+1+2=5。§4 forget FT先付训练成本，权重来自 theta0 的梯度比或平方均值梯度代理，不是独立参数重要性真值/完整 Fisher。FQ log p-value 不证明与重训分布等价。§5 TOFU1/5/10%、Llama3.2 1/3B、MUSE News；例1B TV MU.495→Per-grad.556、retainES.207→.376，forgetES.059→.072反而更高，3B也有forget退步。随机/常数权重与proxy样本比例消融支持局部选择效应，不给privacy erasure保证；20%样本结果不等完整E2E成本。硬件、precision、额外FT+proxy+搜索时延和置信区间在采用段未披露，SLO不适用离线参数编辑。

Books拟仅报告：Ch72实际2585–2600已经区分subset/尾部目标、局部参数近似、retain与独立恢复/泄漏验收；本篇提供具体gradient-weighted TV recipe，未能把其一次proxy测量提升为可靠删除资格或普遍预算边界。不称现有正文已写该算法。

## 2601.22028 — CLReg

采用 late-layer forget/retain representation 的 contrastive shaping与output suppression差别，2+1+2=5。§3.1–3.2 mean-pooled特征的paraphrase/dropout正对与forget-retain负对，DPO/InfoNCE加既有unlearning损失；不采用§3.3未核理论为擦除保证。§4.4 Table3/4三几何指标分离，UMAP跨度变化仅诊断，不能认证知识消失；§4.5 last1/4/7/10/13层对照不全指标单调，例如8B SimNPO last13 forget score更高但utility更低。

§4.1–4.3 TOFU3/8B、MUSE7B，10epoch/1e-5；A.2 H100，先调各baseline再独立sweep τ/对称性/loss，不是双方相同总调参预算。关键反侧 Table2 MUSE-News GradDiff PrivLeak -87.85→+99.69（目标0，绝对距离更大），Books retain .59876→.58451，否定“无额外privacy风险/保留不伤”强结论。单seed/precision/batch在采用段未披露，concurrency/SLO不适用离线编辑；增加特征对/调参及训练成本不可作零成本。

Books拟仅报告：Ch72实际2685–2698已经要求 routing/representation/decode多层恢复验收并拒绝probe作为隐藏知识真值。几何受控改变值得留日报，但与privacy反侧并存，不能将本配方升为可认证的永久概念删除机制或“保留分布不动”。不以正文已有一般主题冒称具体CLReg已有覆盖。

## 2601.22020 — ViKeR

采用 unrelated visual inputs 的固定full模型分布作为 token级 regularizer，2+1+2=5。§4以同问题/答案前缀、k张无关图平均teacher概率估计“理想”post-unlearn分布，GA+KL允许token影响非均匀；identity-agnostic理想是假设/代理，不是理论隐私真值。§6 w/oVis/w/oGA/w/oReg直接消融及visual-reference类型说明reference依赖：forget/scene更差、retain/pet误伤保留；λ增大retain改善但forget降低，k<5更不稳。

A.4 LLaVA1.5 7B LoRA rank8/alpha16、冻结vision encoder/projector，AdamW lr5e-6/batch2/1epoch，单80GB A100，三次平均；MLLMU10/15%与CLEAR10%。Table2 CLEAR forget Rec ViKeR .62而NPO .18/IdkPO0；RetainRec原值4.21 vsNPO.80，表头箭头↓却正文将较高值叙述为保留改善，方向冲突未解，不能叫所有指标更强；GIB只是流畅度。具体precision、teacher k额外forward与E2E时间未披露；并发/SLO不适用训练。不会从图中一个key token变小推完整隐私删除。

Books拟仅报告：Ch72现有参数擦除/推理拒答与retain/recovery分账涵盖采用约束，本配方对具体MLLM identity任务的“理想分布”可靠性依赖reference而未变成普遍erase interface。不是领域指标自动准入，也不声称已覆盖具体算法。

## 2601.22002 — Rate-Distortion Optimization for Transformer Inference

精确v1不继承后v5，采用 intermediate task-aware lossy codec 与可append causal hyperprior，2+2+2=6。§3.1因果 W/Y<=i，h产生24D side information、独立monotonic CDF编码Y和W，quant-round STE与rate+CE共同训练；后帧不需要重发前frame hyperprior。不会因确定性层的理论entropy不增就断言更深split编码更容易。§3.2/3.3界不在本次采用，不需读全proof。

§4.1–4.3 GPT2Small124M/OpenWebText，split3/6/9，独立λ重训点不是原checkpoint无损压缩；高λ会diverge并改LR。B.4 bf16训练A40，1024tokens、累积480samples；估计率与真实arithmetic code不到1%差仅作者报告。§4.3模型16bit表示为raw基线，最低PPL点230.16BPT，CPU+GPU codec .348ms/token，Deflate .672而Zstandard .022更快。Appendix C同1000 validation、2080RTXTi entropy net+i9-9900K单核coder；37.77Mbps交点假9%协议overhead的估算，不是真实网络SLO。batch/concurrency、E2E/request/token流实现及confidence未披露，不作线速保证。

Books：root 实际必要源及 Ch55 L104/541 对照后 PRE 通过；lossy activation 的 joint body/codec 与可追加 hyperprior 确有接口差额。已实际读 Ch54 memory capacity→Ch55 split/state transfer→Ch56 quality/SLO scheduling handoff，在 Ch55 activation reference/residual 后窄写两段及末注；正文、前后及末注经 root 非作者实际 POST 通过，锁释放，不授日级 Gate、无损、37.77Mbps线上或E2E加速。

## 2601.21996 — Mechanistic Data Attribution

采用 localized emergence window内data intervention改变可解释head出现时刻，2+1+2=5。§3.2 unit-scoped EKFAC approximate influence、top≤10%复制/gradient-mask、random/global-TDA controls；§4.1/4.2四Pythia14/31/70/160M由scratch重训并密checkpoint（E.1沿官方config）。最终saturation仍形成heads，不推出永久remove或训练成功原因唯一。

§5.4同期ICL信号随data干预变化，却显式承认latent confound；更重要原文定义 ICLScore=L500-mean(L0:50) 又称positive代表late loss降低，符号解释内部不一致。本次不采用“ICL改善量”或data→head→ICL中介因果强断言，只保留head emergence受干预及这一未决。§6.3 finite templates小量好、100k natural超过synthetic且插入密度效应是局部反侧，diversity exhaustion只解释假说。实际GPU/precision/额外EKFAC/多模型训练总成本、statistical repeats在采用段未披露，不声称便宜到可生产泛用。

Books拟仅报告：Ch4 L35–58区分人选择数据/目标及representation capacity/optimization/generalization，但没有本unit-specific方法。当前证据只能改作者受限head的出现时间；局部head分数、符号未决ICL metric与最终saturation不能承担新的通用学习链。保留机制干预案例与反侧，不把它升为scale-invariant curriculum或唯一能力原因。

## 2601.22027 — CAR-bench

采用缺工具/缺信息下任务成功与行为consistency分开、premature action/implicit fabrication区分，2+1+2=5。§3.3成功是6criteria AND，最终31state/intermediate action及policy LLM评分权限不同；§3.4 pass-any vs all是已知aggregation，不单独评分为新指标。§4/5同模型任务切片，缺tool/info比理想base暴露额外失败，不引入汽车应用性能主线。

100base/90hallucination/50disambiguation，5trials，多模型thinking预算2048，temp0尽可能但Claude/GPT5thinking1与Qwen.6例外，Gemini2.5Flash user simulator。仅GPT5 failure人工核 user sole-source导致all5下降6/9/8个百分点，simulator误差未由独立真实用户消除。原文多处 Pass@3/5 与 Pass^3/5百分比交错，故不采68%→36%当同k精确配对，也不并入确定deploy比较。§5 latency22.7s/.11$ 是100base一run调用级近似，硬件/服务器流量/完整SLO未披露，约10ktooldefs+3kpolicy同计；不得宣传线上成本。

Books拟仅报告：Ch66实际L53–75成功交集与trace/outcome分别定义，Ch72 effect-gate仍由外部确定性控制；本篇是一个含missing-information的具体盲点评价载体，不改变该权限链，作者也说明production规则冗余与agents自己检查不同。保留consistency/user-sim污染反侧，不声称已有正文有本benchmark。
