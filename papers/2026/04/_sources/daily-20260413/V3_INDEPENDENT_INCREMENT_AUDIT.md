# 2026-04-13 有限增量独立核验

复核者：`/root/apr03`；作者：`/root/apr02`。当前合同：V3。此记录只验收本日有限恢复组的来源、采用边界、具体 owner 和实际新增正文，不代替 root 的最终日级来源/日期/分母验收。

实际范围为剩余 6 个恢复家族与新增 19 中的 16 个家族，共 22 个；08580、08701、09168、09173、09181 的未变 root 独立结果复用，不重复读其全文。原始 504 身份不是全文审阅队列。本次不扩 Weekly、不搜索完整版本史、不复审无关附件。跨模型复核未运行：这是有界非交互子任务，采用独立智能体核验。

## 必要来源与处置核验

下表链接均为实际打开的官方精确版本；读取止于采用命题、关键对照及反证。采用论文机制不代表实现复现。

| 家族 | 实际必要证据与 owner 对读 | 独立结果 |
| --- | --- | --- |
| [08554](https://arxiv.org/html/2604.08554v1) | Theorem 2、Methods 的有限字母表/可变阶 n-gram、五符号深度 3/5 例子；描述性 n-shallow 与外部规范规则的深度缺口，不推出 Transformer 训练或部署 recipe。 | 5 分标准、仅报告通过；保留理论增量，不因实验小排除。 |
| [08567](https://arxiv.org/html/2604.08567v1) | §4.1–4.2、§5：多用户私有消息、序列化 sessions、selection F1 与 execution accuracy、privacy/utility 分账；Says/Colon/XML 不提供认证。Ch72 Agent Privacy 轨迹记账、Policy-bound Sensor、Instruction Hierarchy 的实际正文承载采用命题。 | 5 分标准、已有覆盖通过。 |
| [08577](https://arxiv.org/pdf/2604.08577v1) | PDF v1 p4 Theorem 3.1 Eq8 与 [HTML v1](https://arxiv.org/html/2604.08577v1) §3.1 均为 `Psi_eta + rho/eta`，Alg2/AppA.1 一致。§3.2 的均值/标准差上界仅在非负权重条件 Eq13 下 tight；§4 是 Llama3-8B、OpenMath 10k、五数学 benchmark。 | 旧“Eq8 为 rho*eta”的争议无原文依据，必须撤销。可 5 分标准、仅报告；完整 trajectory 的 minibatch DRO 不等任意 OOD 鲁棒保证。 |
| [08579](https://arxiv.org/html/2604.08579v1) | §4.1/4.4–4.6：DINO 768/MiniLM 384、Flickr 1000 图/均值五 caption、kNN15、basis50–100、单 seed；谱相近而 functional basis 不可用。caption-equivalence 的 R1/R5 不同于标准 CLIP 协议。Ch23“统一架构不等于双向可用的统一语义空间”及几何噪声边界实际覆盖。 | 5 分标准、已有覆盖通过。 |
| [08708](https://arxiv.org/html/2604.08708v1) | §4.1–4.3 的 ragged 多 run 轨迹、embedding、PARAFAC2 重构残差；§5 的 AUROC 是排序而非 risk calibration，同错共识仍可能易压缩，拓扑维度不是因果归因。 | 5 分标准、仅报告通过。 |
| [08764](https://arxiv.org/html/2604.08764v1) | §2.4 Eq9/10 都是上界，缺少 tangent 梯度下界，不能推出 Eq11 的 normal/tangent 比率 O(t)。§3 固定早期 activation-PCA proxy、匹配秩 null 与 Table1 的观察不因此失效，但 proxy 不是语义流形或训练干预。 | 5 分标准的受限实验可仅报告；比率保证须明确隔离，不采用到 Books。具体反例见下节。 |
| [09035](https://arxiv.org/html/2604.09035v1) | §IV–VII：短 horizon reward 的遗漏、sigmoid/exponential advantage 倾斜、state-dependent normalizer；理想 true advantage 的结论不等 learned value/world 下每次更新单调。四 MuJoCo、Hopper 反例。 | 5 分标准、仅报告通过。 |
| [09057](https://arxiv.org/html/2604.09057v1) | Motion-conditioned Noise Prior、audio interface、hybrid losses、Tables2–5/AppF；共享 2D 轨迹通过两个不同接口，不证明三维接触因果。实际 Ch24 endpoint→AV 条件分支两段及相邻正文已对读。 | 6 分真实 gap 深入，来源与写后通过。 |
| [09075](https://arxiv.org/html/2604.09075v1) | §4.1–4.2 parser/NLI→lexicographic MaxSMT subset→偏好蒸馏；43380 条训练及 strong-language 失败。Ch72 Policy-as-Data 已实际分开 policy artifact、模型 sensor、确定 enforcement。 | 5 分标准、已有覆盖通过，不将开放语言 parser 升级 ACL。 |
| [09089](https://arxiv.org/html/2604.09089v1) | 方法、Table3/4：一次 prompt safety 分数调 decode bias；k64 wall-clock +38.7%，更频繁代价陡增；安全/功能目标会冲突。Ch72 Learned Security Sensor 实际区分一次检查、生成中持续风险、固定频率替代与 runtime authority。 | 6 分安全深入、已有覆盖通过；不采用固定 bias 为 calibrated risk 或实时守卫。 |
| [09101](https://arxiv.org/html/2604.09101v1) | §3–5.3：frozen CLIP 可由 prompt/meta-network 携后门，白盒 inversion、candidate 含 target、OOD1000、47/50；修复还需 clean labels，阈值不是校准风险。Ch72 可组合 Prompt 的 versioned supply-chain 与 trigger-neighborhood 实际覆盖。 | 5 分安全深入、已有覆盖通过，限定受测 threat model。 |
| [09159](https://arxiv.org/pdf/2604.09159v1) | PDF v1 §4.1–4.5：ODE prefix + stochastic tail、tail-only RL、prefix endpoint 自蒸馏；joint surrogate 不等 terminal marginal entropy，沿路径 time 恒定不推出 state divergence=0。评价省 tail 但仍有 N 候选 Q 选择。 | 5 分标准的受限方法仅报告通过；中心 entropy/全局改进保证隔离，不否定全部实验。 |
| [09222](https://arxiv.org/html/2604.09222v1) | §3 双梯度 band selection、§4.3/4.4 Table2/Figure4：相同 48-band 随机控制、full-band 反例，attack 与 WER/RQS 不单调；四 target 共享 Whisper encoder。Ch72 Sensor Robustness 的 benign task-critical semantics 与 attacked outcome 双分支实际覆盖拟采用验收要求。 | 5 分安全深入、已有覆盖通过；受限 band 反例保留日报，不外推全模态/人耳或安全率。 |
| [09227](https://arxiv.org/html/2604.09227v1) | §3/Alg1、§4/5：low-resolution preview 选 seed/prompt 后 HR 重新跑；D-velocity commutator、短窗口 cached HR 修正，不是 LR upsample 保留同一 HR state。实际 Ch24 两段及邻接已对读。 | 6 分真实 gap 深入，来源与写后通过。 |
| [09244](https://arxiv.org/html/2604.09244v1) | §4.3–4.4、§5.3 Table3：S1+S3=62.2 低于 baseline70；S2+S3=71.5；时间 EMA reuse 缺 semantic 保护会传播误剪。Table2 的 `r=50%` 配置47.5 不等 unpruned48.8，不能混同不同表的 baseline。实际 Ch23 新两段与相邻内容已读，先平滑 salience→按阈值形成候选→融合的顺序已修后再次核；受限反证/成本/静态回退成立。 | 5 分真实 gap 深入，来源与实际写后通过。 |
| [09330](https://arxiv.org/html/2604.09330v1) | §3.2–3.3 的 clean video detach/global pooling→action 单向条件、同步 flow time；§4.2 error<.2“SR”、§4.3 replay、§4.4 20 trials 11 vs7 且合成 pretrain 增预算。Ch25 environment/agent/joint channel 与 counterfactual action support 28–66 行实际覆盖。 | 6 分必要深入、已有覆盖通过；joint 同步不证明 action-conditioned outcome 或物理安全。 |
| [09332](https://arxiv.org/html/2604.09332v1) | §3–5.3、Tables1/4/5/7：冻结 Whistle 已预训 Tatar，20h 是配对适配；英语 recipe 不同、phone BPE113→125、K8 代价。实际 Ch23 encoder/projector→Stage3 交接处两段已对读。 | 5 分真实 gap 深入，来源与写后通过。 |
| [09338](https://arxiv.org/pdf/2604.09338v1) | PDF §3–4.2：500 同题、八模型、one-shot/step/backtrack；completion 与 solve 分开，strong model 的 −5.6/−5.8 只属该协议，不能单归训练激励。Ch79 Search-based Planning 的非单调搜索边界，Ch66 成功事件分层与 harness identity 真实正文覆盖拟采用命题。 | 5 分标准、已有覆盖通过，协议不作 compute-matched 模型能力排名。 |
| [09364](https://arxiv.org/html/2604.09364v1) | §5–7：full-sequence vs last-position 干预、九模型各100合成样本；MAC heuristic/steering 退步/自然图未验。实际 Ch23 Object Hallucination Circuit Probe→VQ 交接两段已对读。 | 6 分真实 gap 深入，来源与写后通过。 |
| [09425](https://arxiv.org/html/2604.09425v1) | §3–7：跨层替换≠删视觉 tokens、mask/position/KV 与输出协议；teacher caption 相似≠human truth。实际 Ch23 两段正确保留短答案退步；协议术语已改为 single-token 答案/multi-token VQA/caption，实际修后正文再次读取确认。 | 5 分真实 gap 深入，来源与实际写后通过。 |
| [09429](https://arxiv.org/html/2604.09429v1) | §3.2–3.5/§4：canonical raxel=d+o 三通道、shared VAE、14B+6B 双分支；Procrustes/center principal point、Plücker codec 混杂。实际 Ch23 camera state 两段及后续 World Model 交接已对读。 | 6 分真实 gap 深入，来源与写后通过。 |
| [09455](https://arxiv.org/html/2604.09455v1) | §4.1–4.2/§5.3 Tables3/4/AppC：self/expert 分流、best expert 门槛、负 advantage shared-prefix stopgrad 而 suffix 继续更新；prefix ratio 不等无偏完整 IS，warmup 预算不同。实际 Ch33 teacher/outcome→phase credit 交接两段已对读。 | 6 分真实 gap 深入，来源与写后通过。 |

## 必须修正的两处判断

### 08577：原“争议”是读取错误，不是论文原式冲突

独立实际打开 HTML 与 PDF v1 后，Eq8 都为 `inf_eta {Psi_eta + rho/eta}`。这与 Alg2 和 Appendix A.1 的 `nu=1/eta` 一致。作者应在候选表、证据段、§5 与 notes 同步撤销原 `rho*eta` 断言，保留改判理由；不要求运行代码或比较全部版本来撤销这个错误。没有普遍 OOD 证据仍可标准完成/仅报告，不能靠虚构公式争议关闭它。

### 08764：两个上界不能直接相除得到比率上界

§2.4 的 Eq9 给 tangent 梯度 `O(G_rms*t)` 上界，Eq10 给 normal 梯度 `O(G_rms*t^2)` 上界。比率结论还需要防止 tangent 期望梯度抵消的下界，而曲率与 activation covariance 假设并未提供它。

具体局部反例：取平滑抛物线 `x=(u,u^2)`、reference 原点、对称小 u 分布，线性层 `W=0`、平方损失标签 `y=-1`，则 backpropagated `g=1`。tangent 的期望梯度为 `E[u]=0`，normal 为 `E[u^2]>0`；几何方向分布和有界曲率不阻止该抵消。因此不采用 Proposition 2.3/Eq11 的普遍梯度比保证。它并不反驳本文用固定 PCA proxy 测得的有限梯度能量，也不证明所有几何分析错误。安全终态可保留局部实验于报告、单独隔离这一理论采用，重开需补充适用的非退化下界或修正定理。

## 有限任务验收与日级交接

作者已在 README 候选表、证据段、§5 和审阅 notes 同步撤销 08577 的错误争议，并保留 08764 的受限测量与缺少下界的理论采用隔离；本次定点复读确认这些修正实际存在，没有因此新增外部材料请求。09425 的 single-token/multi-token 协议术语，以及 09244 的 salience→EMA 平滑→保留候选→融合顺序，均已在实际 Books 正文修正并再次独立通过。

本有限任务的 22 项必要来源/具体 owner 裁决、8 项真实 Books 增量的写后及相邻衔接复核全部完成；作者的 Review notes、候选表和证据段已经同步相应终态。另 5 项未变化的 root 通过结果复用，未扩展成 504 项全文审读或实验复现。

交接时正式日报为 67 个唯一家族、67 个同标题/URL 证据段：33 整合、19 已有覆盖、14 仅报告、1 暂缓；审阅为 37 深入、29 标准、1 争议。此数量不是日级验收结论。原 12 项已有覆盖/仅报告的 root 独立裁决，以及最终来源停点、日期隔离、集合一致性和否定侧校准的日级 Gate，仍由 root 汇总；本文件不预称整日报 Complete。

## 原 12 项必要证据与具体 owner 的最终复核

本节是恢复后新增的独立核验，不重新审读已通过的 33 项 Books 写回或 504 条原始库存。以下 11 项必要原文已实际打开，并读取所采用命题的目标正文；SEA 的精确 PDF 身份问题单独列出，不以作者笔记冒充独立核验。

| 家族 | 实际读取与限定 | 具体处置复核 |
| --- | --- | --- |
| [08974](https://arxiv.org/html/2604.08974v1) | §3–4、§6/Table5：144 配置中 48 降低仅 2 项显著、96 提高仅 8 项显著；23/48 AUROC 下降另列。817 是 TruthfulQA 原始规模，之后有实体答案筛选；test-set min/max 缩放不是正确性概率校准。 | 5 分标准/已有覆盖通过。实际 Ch66 `Continual Update 需要同步推进 Calibration State` 将 model/task-specific calibration artifacts 与 accuracy、coverage 双 Gate 分开；不是只因同属 confidence 主题。 |
| [08976](https://arxiv.org/html/2604.08976v1) | §3–4/Table3–7：Llama3-8B、四域 TriviaQA、Q5_K_M vs f16、7900 GRE/Vulkan；训练 merge 改用 f16，不能推出 Q5 adapter 修复。M-ratio 与 AUROC 排序不同只在该四域，bootstrap 宽区间不证等价。 | 5 分标准/已有覆盖通过。Ch66 EvalSpec、`Evaluation Identity 必须包含 Harness 与 Environment` 和切片 calibration 正文已要求 metric、artifact、scorer 身份及不确定性分账。 |
| [09174](https://arxiv.org/html/2604.09174v1) | §3–4、§6：facet 由 gold/GPT 派生，MNLI entail−contradict 为诊断 proxy；strict/soft/无检索与单次 case 结果不证明内部先验因果。Soft RAG 约 30% case 退化与总体 F1 收益并存。 | 5 分标准/已有覆盖通过。实际 Ch76 `Relevance 不等于 Sufficient Context` 分开 relevance、sufficiency、generation faithfulness，并明确 rater 不是真值、需要校准与再检索/abstain。 |
| [08588](https://arxiv.org/html/2604.08588v1) | §2–3、§4–6/Table1：外部 tree 条件准确率、两 turn、250 样本（thinking 50）；Qwen 单 cost 措辞与 GPT5-mini 的收益不同。SFT 学习外部 p 成本程序，移除 p 后仍会幻造估计。 | 5 分标准/已有覆盖通过，canonical owner Ch66 `Confidence 最终服务于 Risk–Coverage Decision` 的外部风险估计与 wrong/abstain cost；Ch56 risk-budget 调度是相邻交接，不赋模型 truth authority。 |
| [09443](https://arxiv.org/html/2604.09443v1) | §4、§6.2–6.4/AppendixE：853 样本、46 contexts；层数与冲突数共同增加，不能孤立归因 tiers。保序 scalar 扰动改变服从，不证明标签认证。 | 5 分标准/已有覆盖通过。实际 Ch72 `Instruction Hierarchy 必须携带 Authenticated Provenance` 已承载多级 privilege、typed authority/principal/scope/channel、policy engine、effect-time check 与细层级成本。 |
| [09285](https://arxiv.org/html/2604.09285v1) | §3.2/Eq6、§4/AppendixA.1：judge labels 输入 deterministic rule；path intersection 是 set-overlap，不证明有序轨迹合法。三 judge 投票/平均不消除共同偏差，turn1/5/10/15/final 不是所有 turn。 | 5 分标准/已有覆盖通过。实际 Ch66 的五层成功事件、EvalSpec/harness identity 及 `Judge Ranking` 能力/方向偏差/人工 anchor 覆盖采用范围；不声称本 benchmark 本身给 production oracle。 |
| [09175](https://arxiv.org/html/2604.09175v1) | §3–4 的 bounded Top-K、compact C1 manifold/Cβ target、iid squared loss；§5 的 representation-dependent dimension、拟合 smoothness 与小预算 routing 对照。Worst-case capacity bound 与实际 learned router/开放 LM loss 不同。 | 5 分标准/仅报告通过。保留条件理论对象，不把估计 β/d、忽略 log 后的 optimizer 或拟合指数写成 Ch21 工程配置 recipe；没有否定小模型理论的贡献。 |
| [08988 PDF v1](https://arxiv.org/pdf/2604.08988v1) | 当前 HTML/v1 返回 Flywheel 后版内容；官方 PDF 两入口出现读取错误/截断，作者追加 45 秒及一次 240 秒续传仍无 EOF。本复核者对现有截断文件的一次 pdfminer 读取也因 Unexpected EOF 失败，没有读取到可用必要页。旧作者记录只能保留为待核线索。 | 受阻/暂缓的隔离处置通过，不是原版证据通过；不支持正面实验结论、Books 或已有覆盖断言。需官方完整 v1 PDF，或绑定 SEA-Eval 原版题名/版本的作者稿及 §4–5 必要页，届时仅重开本项，不比较全部版本。 |
| [08905](https://arxiv.org/html/2604.08905v1) | §4.1–4.3、§5/Table1–2：adjacent embedding 方向 ACF、net displacement/path length PE 加入 outcome reward。直线路径不是逻辑/事实真值，15.87% tail 与 3σ 声称不一致，非显著 MW 结果不补普遍因果。 | 5 分标准/仅报告通过。只保留受测几何 reward operating point；不把该 proxy 升为 Ch33 causal token credit 或通用 faithfulness 选择规则。 |
| [09000](https://arxiv.org/html/2604.09000v1) | §4、§5.1/5.3/Table2：isolated text diversity 与 entity-connected importance/redundancy 不同；TMR 同时改变读路径。30% compression robot30.7>30.3、web47<47.9；压缩提高 retrieval 次数可能抵消耗时节省。 | 5 分标准/仅报告通过。受限图压缩/检索实验不证明开放长程 memory 保持或服务 SLO；实际 Ch77 retention、read-time restore 和 retrieval/utilization 分账仍成立。 |
| [08644](https://arxiv.org/html/2604.08644v1) | §2–3：1.2B vision+32B LLM、vision GQA 即使无 KV 仍改变 attention 成本；MTP 在比较中关闭，官方与内测基线混合。32k/128k 输出等只是作者配置。 | 5 分标准/仅报告通过。承认具体架构分支的研究事实，不因无消融直接排除；但没有足够证据把榜单归因 GQA/MTP 或作生产吞吐结论，也不为版本公告新增同义 Books。 |
| [08906](https://arxiv.org/html/2604.08906v1) | §3、§8–9、§11：409 fixed bugs 中 273 可分析 repro/config；35 选定源 bug 的 16 transfer；47% 是 bugfix 附 test，不是生产发生率。框架/任务/应用三级定义与来源选择限制保留。 | 6 分标准/仅报告通过。实际 Ch81 `Synthetic Environment 必须先证明可执行，再用于训练` 后的 deterministic transition vs Agent scenario tests 承载大方向；只保留具体 failure templates，不称新通用 oracle。 |

## 日级有限审计范围与结果

实际读取本日报六部分、Apr11 可复用的官方目录停点记录及 Apr13 题摘/证据 notes。14 个 Daily Source ID 均在表中；OpenAI Research、Google Publications、Meta 及 Moonshot/MiMo/MiniMax 指定子入口继续有具名材料恢复条件。既有跨窗停点可复用，不冒称全源重新抓取；空响应、current sitemap 和 News RSS 不代替研究历史覆盖。

实际重新打开 [arXiv 官方公告规则](https://info.arxiv.org/help/availability.html)：永久 ID 在公告时分配，常规 Sun–Thu 20:00 ET；Apr12 20:00 EDT 对应 Apr13 08:00 北京。本次对 67 个候选逐一对账原始身份字段，自己的 v1 元字段均为 `2026-04-13T00:00:13Z` 至 `00:59:35Z`，联合已核连续批次/OAI/公告槽支持报告明确声明的 `08:00～09:00` 推断区间；不把该字段单独定义为公开时间，也不额外要求合同未规定的逐篇成功日志。49 个晚字段身份全部不在正式候选表中，两 Seed 目录/版本冲突保持独立隔离，不因后段例外否定前段所有家族。

正式候选表实际检查为 67 行/67 唯一身份、证据区 67 个同身份标题，最终处置为 33 Integrate/19 Existing/13 Only/1 Blocked/1 Disputed；审阅为 37 深入完成、28 标准完成、1 受阻、1 争议。SEA 原版受阻不计审阅完成。V2 三项加总、审阅深度及 schema 的机器一致性检查通过；机器结果不证明来源语义或发现无遗漏。已通过的 33 项实际正文复核结果及本文件先前 22 项裁决有效复用，不在这次任务重读。

否定侧新增实际打开六篇完整官方 v1 题摘，必要时读核心段：

- [08920](https://arxiv.org/abs/2604.08920v1)：utility-centric retrieval tutorial 组织 relevance/utility 和 context/LLM-dependent taxonomy，没有新受控边界；具体综述关闭，不以已有 Ch76 owner 或 tutorial 类型单独拒绝。
- [09024](https://arxiv.org/html/2604.09024v1)：§3–4 的 image-owner perturbation 只促使被测 MLLM 拒绝，白盒 shadow-query 优化未认证下载者权限；新的隐私应用工作点不等新信息访问保证，关闭理由不把全部隐私/视觉安全排除。
- [09029](https://arxiv.org/html/2604.09029v1)：完整题摘及§2–3 的 compositional allocation/约束 oracle，主要实例化 joint constraint 与 utility 分账；未用“金融领域”拒绝，也未把 oracle 名称当新执行权责。
- [09104](https://arxiv.org/html/2604.09104v1)：§3.4–3.7 的 OSINT credibility/去重、52 评分样本校准；作者明确 incident reports 不是必然真实事故，4.9× 不作生产发生率。具体事件线索/研究议程关闭，不否定数据集价值。
- [09150](https://arxiv.org/html/2604.09150v1)：§3.1–3.3 的 entropy→retrieval/CAD、长度→summary、KL→stop 与 DPO 是既有 proxy 的组合；未验证 entropy 下降即外证可靠，不因方法新名或效率数字自动入选。
- [09189](https://arxiv.org/html/2604.09189v1)：§3 的 self-stated rule audit、UNPREDICTABLE 分母排除及 Absolute benign-compliance 计错；自述与行为不同没有得到 latent policy/可执行权限，具体成熟原则复验关闭。

这六个抽样未发现由共同“没有新 owner/规模小/主题已有”理由造成的新遗漏。其余原始库存、11 个关闭项中未在本轮抽到的五个、全量附件、实验复现及不可得的外部目录不在本轮实际审阅范围；不据六个样本声称全学科召回。作者已将 SEA 的精确版本访问失败写入候选表、证据区和具名材料请求，未据旧笔记采用正面结论；其余 66 项及 33 项 Books 不依赖该材料。普通可执行审阅/Books 待办为 0，具名来源和版本缺口都有定点重开条件。按当前合同允许的安全终态，本轮日级非作者复核通过；由 root 汇总并更新正式报告验收状态，本文件不自行将 README 标为 Complete。
