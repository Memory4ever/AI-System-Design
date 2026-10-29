# Jan09 增量独立审计 — 2026-10-07

复核者：jan02_new_evidence；非 Report / Books 写入者。本文件为唯一写入范围，不改 README、作者 supplement、Books、索引或 LEARNING_STATE，不 stage / commit / push。本轮只核 Jan09 补充窗口 BJT 2026-01-08 自然日；原 17 家族的日期、评分、有效证据与历史验收冻结，不继承 Jan02 / Jan08 的候选判断，不接下一日。

## 1. 启动、人口与权限

本日重新完整读取 AGENTS、RESEARCH_CONTRACT、REPORT_CONTRACTS、CODEX_RESEARCH_PROMPT、ROADMAP，读取 RESEARCH_SOURCES 使用说明、14 Daily 来源及 Daily 主题恢复规则；最新 checkpoint 只用于路由。实际读取本日 README、supplement、DATE_BASIS 与有限来源停点。使用 daily-research-closure 的 FIRST / necessary evidence / owner / POST / DAY 分离规则，不以作者标签或静态校验替代语义检查。

独立完整读新增 17 份 exact-v1 题名与摘要：03500、03509、03555、03570、03600、03649、03655、03791、03905、03955、03992、04056、04061、04098、04170、04171、04301。其后独立定点读 14 项拟准入的必要方法、关键评价与限制，未声称全文、代码或全部附件审阅。03655、04170、Netomi 为分层负侧，04301 只审必要日期。四主题八页 union 364 标题是辅助发现人口，不是 364 份题摘/正文待审池。

Anthropic Jan08 机构项复用 root 作为非作者的实际独立必要原文与 owner 核：Anthropic L19–24 / PNNL L263–287，Ch72 29–31 与 Ch78 707–728。只采用单次水厂 simulation 中失败后替换已知技术的窄反证；不由 Summer2025 实验时间移文章公开日，不采用三小时/多周通用速度、生产入侵率或安全保证。该项 2+2+2=6 / 深入 / ExistingCoverage。此分批复用不是本审者自称重读了全部机构正文。

## 2. 实际日期独立核

独立重新请求 17 个官方 DataCite DOI 原字段；同时实际重读 arXiv [公告政策](https://info.arxiv.org/help/submit/index.html) 与 [ID 分配规则](https://info.arxiv.org/help/arxiv_identifier.html)。16 个具名 v1 Submitted 均 2026-01-07 且早于 19Z：公告日程给最早 Wed Jan07 20ET（Jan08 01Z）的下界，announcement 时分配且不 advance/backdate 的 ID 规则，与该具名 ID 已存在的 registered 上界合取，同落 BJT Jan08。2026 Jan01/Jan19 假期不改 Jan07 常规批次。这是日级联合推断，不是 Submitted / Updated / registered 任一字段直接等 public，更不授每篇实际公告秒级时刻。必要正文中未见更早作者正文显式公开信号；不扩全网考古。

| exact-v1 | 实际 registered UTC（仅具名 ID 上界） |
| --- | --- |
| 2601.03500 | 2026-01-08T02:39:47Z |
| 2601.03509 | 2026-01-08T02:40:00Z |
| 2601.03555 | 2026-01-08T02:41:14Z |
| 2601.03570 | 2026-01-08T02:41:35Z |
| 2601.03600 | 2026-01-08T02:42:17Z |
| 2601.03649 | 2026-01-08T02:43:25Z |
| 2601.03655 | 2026-01-08T02:43:33Z |
| 2601.03791 | 2026-01-08T02:46:48Z |
| 2601.03905 | 2026-01-08T02:49:33Z |
| 2601.03955 | 2026-01-08T02:50:44Z |
| 2601.03992 | 2026-01-08T02:51:38Z |
| 2601.04056 | 2026-01-08T02:53:08Z |
| 2601.04061 | 2026-01-08T02:53:16Z |
| 2601.04098 | 2026-01-08T02:54:08Z |
| 2601.04170 | 2026-01-08T02:55:51Z |
| 2601.04171 | 2026-01-08T02:55:52Z |
| 2601.04301 | 2026-01-09T02:41:56Z |

03992 Updated(v1)=2026-07-01T00:12:34Z 不作 Jan 公告依据、不抹 Jan 注册、不比较后来 revision。04301 下界与上界跨 BJT Jan08–09，不能由 Jan09 registered / Updated 判窗外：只请求具名 Jan08/09 实际公告或作者原正文公开日一次，未确认前不评分、不计候选、不入 Books。

## 3. 全部 14 新论文必要证据与 owner 判断

以下链接均 exact-v1 HTML；章号和段落位置是本轮实际 owner 邻接，不以抽象 owner 主题替代已有覆盖。三维分不因深审成本、Books 结果、争议或小实验改变。Only Report 保留具体新机制/反侧，但不自动把每个受限 recipe 改成长期书籍分支，亦不声称 exact recipe 已覆盖。

### [03500 SDCD](https://arxiv.org/html/2601.03500v1) — 2+2+2=6，标准，Only Report

实际 §3.1/3.3 Eq1–2、§4.1–4.3/CHAIR 表：patch bijection 保 patch multiset、破坏 arrangement；logits `(1+α)original−αshuffle`，α=2 / β=.1。不是完美语义保持介入，邻域也变化。7B 三模型、POPE/MME/500 COCO captions、max512 / T1 / topP.9；实现同时将两视图 image attention 加 .6，不能把总收益独立归因 shuffle。CHAIR 改善伴 caption F1 下降；projector / resampler 的反侧未隔离所有 architecture 条件。

实际 Ch23 1107–1132 writer/reader 与 1147–1158 外部两输入、late branch。root 同样实际读邻接后定案：exact arrangement-destroyed 视图确为未写的替代，不说“精确 shuffle 已覆盖”；但当前耦合 attention 改动与 architecture 受限比较，不新增近同长期分支，保留局部对照案例于 Report。

### [03509 Programmatic Skill Networks](https://arxiv.org/html/2601.03509v1) — 2+2+2=6，标准，Only Report

实际 §2.1–2.5、§4 setup/4.4、Limitations：executed trace 的 top-down fault / bottom-up patch；成熟度概率 `.9 sigmoid(5(.6−V))+.1` 有 .1 下界，不冻结成熟 skill。refactor parent/child/top5 semantic neighbors、5 canonical cases；最近 3 个受影响任务降超 20% inverse rollback。三 runs、online batch1，部分旧 baseline 后端不匹配，不授形式语义保持或稳定收敛。

实际 Ch80 342–347 candidate lesson / history / held-out / promotion / rollback 分责。概率和极短验证人口是新局部 recipe，不是普适治理新合同；保 Report 实例与失配代价，不声称精确概率实现已覆盖。

### [03555 SCRIBE](https://arxiv.org/html/2601.03555v1) — 2+2+2=6，标准，Only Report

实际 §3.1–3.2、§4、Tables1–2、§6.1–6.3、Limitations：HDBSCAN（fallback kmeans）prototype / checklist→subgoal-skill-span router→0–3 judge；GRPO **.3 process + .7 outcome**，每 1000 steps 重建，固定 anchor 做 prompt-variant calibration。约 10k MATH/ToolACE、Qwen3-4B/Llama3.2-3B、GPT5-mini judge；router holdout 是已标注 taxonomy，不等独立 skill 语义真值。中层表现先出现与相关 AUC 不证明独特必要因果链；cluster/router/judge 漂移和 refresh 成本保留。

实际 Ch31 1041–1055 有限过程信号、542–556 versioned criterion/skill proposal 与 independent promotion、597–621 observation grain / conditional feedback。受限 prototype 人口 recipe 可以报告，未新增独立 reward authority 或稳定学习证书，不能把主题映射当精确覆盖。

### [03570 CPT Concept Learning](https://arxiv.org/html/2601.03570v1) — 2+2+2=6，标准，Only Report

实际 §3.2、§4.1–4.2、Limitations：FICO→BIO target logit gain/loss、500 concepts 与 circuit 相关代理；Qwen3 embedding top/mid/bottom K100、固定阶段预算 5×4 curricula / BIO control。0.7B/1B 主配置的 relatedness / order 反侧不是 causal circuit 或已实现 circuit-aware scheduler。

实际 Ch28 1490–1506 acquisition / retention / transfer、geometry proxy 非因果和 replay fallback。新的观察切片有用，保 Report 条件；不把相关度签为 curriculum oracle，不声称 exact 概念图已写。

### [03600 ALERT](https://arxiv.org/html/2601.03600v1) — 2+2+2=6，安全命题深入，Only Report

实际 §3.1–3.3、§4 Tables2–3、Limitations：FFN pre-product hc/hg 两路独立 VIB；benign/harmful prototypes 的负 L2 距离分别 softmax token 权重后聚合。progressive ablation 支持具体 operator，不只是双 classifier。Layer4 选择看过 AutoDAN 探索人口，“classifier 只 benign/harmful”不等整个框架从未见 attack。三模型/三 attacks，Vicuna XSTest 部分 68–86，不授“全都>90”或未知攻击/生产安全。

实际 Ch72 600–634 model/layer-specific sensor、规则/模型绑定与 independent redteam；这个具体 pre-product operator 并非已写，但仍是受限实验传感替代，没有替代 policy authority / deployment assurance，root 定案 Only Report。

### [03649 SyncThink](https://arxiv.org/html/2601.03649v1) — 2+2+2=6，受影响核心深入，Hold

实际 §3.1–3.4 Eq3–5、§4 setup/Table1、§5.4–5.6、Limitations。`R(</think>)≤τ` 且 `τ=floor(t exp(−λH))`，固定 t,H>0 时增 λ 降 τ、更严格触发；§5.5 却称增 λ 更短/更激进，中心控制方向矛盾。λ=.8 在 heldout MATH500 调节，三个 R1 distill、greedy 单 run，部分 accuracy 降低。answer attention gradient 也是代理，不证明唯一 bottleneck。

保 transition 描述性接口和原 6 分；不选一方猜修，不由动态 trajectory 代作者解决固定公式方向。只重开精确原实现或作者修式与配置，明确 inequality / λ / rank 定义及停止方向；无全附件/所有实验请求，不授可复现控制律、不写 Books。

### [03791 PII cue-controlled](https://arxiv.org/html/2601.03791v1) — 3+2+2=7，深入，Integrate / POST pass

实际 §3.1–3.3 normalized LCS / CRM、§4/§5.1–5.4、Limitations、A5/D/G：NFKC/lower/drop nonalnum，email local/domain 的长度加权 cue，CRM 是 cue<τ 的条件人口；不是逐样本删除 cue 的 do 干预。mC4 known train/heldout 同清洗，560M/1.3B/13B blackbox PT、32 语言 reconstruction 与 25 语言 MIA 不混合；cue-free continuation 和 reconstruction 的 budget / decoding 不混成一协议。强 cue 的 heldout 重建、低 membership 信号不推出不记忆/隐私无风险；不覆盖白盒、专门攻击或后训练 PII。

实际 Ch72 276–309 全新增正文与完整前后：generic identifiability→normalized cue 分层两段→fragment completion。SF-2026-ARXIV-2601-03791 两段实际 POST：采用字符串 overlap / comparable cohort / 低 cue 切片，不称全 cue 消除或配对因果；新增真值/规范化/控制成本、Unknown / provenance / canary / DP fallback，并明确真实敏感输出的风险不因 membership 未识别而消失。owner 正确、exact-v1 源注正确、邻接概念连续；无既有段落丢失，无普适 privacy 保证。

### [03905 World Model as Tool](https://arxiv.org/html/2601.03905v1) — 3+2+2=7，深入，ExistingCoverage

实际 §3.1–3.2、§4.1–4.2/Tables2–4、§5.1–5.2、§6/Limitations。Agent 用 cloned ground-truth simulator，VQA 用 Wan2.1 video，不能合称统一 learned WM。九模型与有限任务，低调用和调用/成败相关不是 causal harm；forced call 局部不自动改善，不推所有 WM 无用。GPT4o 辅助 taxonomy 非独立必要性证书；Decider/Reflector/Memory/RL 是未来建议。Gemini/Claude 未测，simulator 不可横向统一。

实际 Ch78 218–242 utility / cost / risk admission、call→observation→used→outcome，479–502 no-tool/call shell/actual result counterfactual。正是拟采用的负向设计界限，具体已有覆盖成立；不声称本论文精确 benchmark 已有，不增加重复案例。

### [03955 ResTok](https://arxiv.org/html/2601.03955v1) — 2+2+2=6，标准，Only Report

实际 §3.1–3.4、§4 HAR、§5.1/5.4 Tables2–5/Recon-vs-Gen：image/latent 层级 residual 在量化前编码，不把它写成多组 RVQ 的同义词；cross-hierarchy mask、DINO alignment/nested dropout。NTP 后 HAR 分层 group 并行不保层内全部依赖；AR128 step gFID4.56 vs HAR9 step5.53 有质量代价。ImageNet256 主 200/300 epochs 与 ablation30/50 分开；重建改进不签生成质量。

实际 Ch23 236–254 prefix / decoder identity / distortion，Ch24 559–590 少步与依赖/质量/轨迹边界。具体 codec-factorization 耦合 recipe 尚未写，但有限联合训练与 quality tradeoff 是 Report 案例，不把 generic residual 当 exact HAR 覆盖。

### [03992 GPU-NDP MoE Scheduling](https://arxiv.org/html/2601.03992v1) — 2+2+2=6，标准，Only Report

实际 III-A–D、IV-A–D：前两 FFN column / 最后 row TP，联合 GPU/NDP 放置按 activation 与 transfer 平衡，prefill prompt frequency 初始化 decode prefetch。dataset-free 仍消费当前 prompt；驻留上限、fallback 与 DIMM 通信不能省。AttAcc + modified Ramulator2 仿真，batch1 / in-out512 / 四 MoE / 2–6DIMMs；2DIMM TP 单独可退步，非实测物理 runtime。

实际 Ch21 776–799 router / expert choice 与 placement controller、capacity / topology / mapping epoch 分责。具体 NDP 调度 recipe 未写，采用权限局限仿真硬件假设，不由 headline 推服务 SLO 或 universal optimum，保 Report。

### [04056 CoM-DAD](https://arxiv.org/html/2601.04056v1) — 2+2+2=6，标准，Only Report

实际 §3.1–3.4、§4 setup/Tables1–2/efficiency：400k continuous semantic prior / frozen encoders→300k `Proj(r)` prefix + masked token absorbing decoder，paired representation swap / adapters；不是每 step joint evolving latent。OT 名称没有 cost / solver / 最优证明；长短40/64/128/256、budget / BLEU / AR identity 与图引用冲突，不授 headline 5×或理论最优。明确两阶段条件接口仍可解释，不因这部分权限不足抹全部机制。

实际 Ch24 294–340 semantic prior / conditional realization 分责与 freeze / decoder failure。该受限 MASK/prefix/swapping recipe 作为实现案例报告；不把书中通用接口称 exact 实现，不请求未披露全部 OT 证明。

### [04061 CLAP](https://arxiv.org/html/2601.04061v1) — 2+2+2=6，标准，Only Report

实际 III-A–E Eq1–4/Alg2、IV、V-A/C/D：frozen robot ActVAE codebook，video action / nuisance 两支；人视频 positive 是 self-anchor，不能假成 paired robot ground truth。NTP pseudo/gold codes，RF DiT 读 stop-gradient VLM KV，KL reference 只是 regularizer。Astribot chassis/torso locked、14DoF、20seen/20OOD / 其他10trial，human 模仿 gripper、contrastive 有局部反侧；不保任意物理解缠/可执行/安全。IV Qwen3VL vs V-C Qwen2VL/36layers 仅隔离精确 backbone/层位复现，不猜修、不全部否定。

实际 Ch26 1176–1193 video latent supervision / action decoder / controller 分责与 paired/EMA alternatives。具体 codebook anchor 未写，局部 action 迁移 recipe 报告，不由 KL/codebook 或单 3090 latency 签物理安全/SLO。

### [04098 Layer-wise Positional Bias](https://arxiv.org/html/2601.04098v1) — 2+1+2=5，标准，Only Report

实际 §3.1–3.5、§4 setup/4.2、Limitations：normalized within-layer conductance / surface-word aggregation，P10 stride1 剔边界，8文本+1scramble / 四模型；P50两故事改用 Llama1B 非同8B纯 window ablation。lexical scramble 稳定局部 profile 不唯一识别架构因果；RoPE/Phi 不机械称 learned position embedding。last-layer next-token readout 的早层低 attribution 不证明信息不存在、层不必要或长窗压缩安全。

实际 Ch13 214–233 causal visibility / position signal、projection/learning 与 computable≠usable。新短窗诊断切片保 Report，不签 attention 因果，不称 exact conductance recipe 已覆盖。

### [04171 SWE-Agentic Rubrics](https://arxiv.org/html/2601.04171v1) — 2+2+2=6，评价权限深入，Only Report

实际 §2/§3.1–3.3、§4.1–4.2、§5.1.1/5.2/5.3、Limitations：expert 在 repo 调查可用 shell / edit，binary judge 的 patch scoring 不运行 tests，不等 whole pipeline execution-free；最终 ground-truth evaluation 确实执行测试。Sonnet4.5 expert30turn / GPT5-low judge，500 SWE-Verified×16 patches，Qwen32B30 / coder50、T1，verifier 挡 git history/hidden tests。repo/no-repo 同 expert 控制支持 context 条件；100-case utility 是 GPT5-medium 非独立人工，46% overprescriptive，testpass / rubric disagreement 非真实 bug 证书；更强模型与 granularity confounded。RL 是 future，不假称已训练 RL policy。

实际 Ch66 2739–2763 rubric formation/execution/ranking 与 independent executable hidden holdout、task freeze / trace / disagreement。新的 repo-grounded weighted binary recipe 报告，不说 exact recipe 已有；一般 verifier authority 不能重复改成新长期链。

## 4. 分层负侧与有限源停点

[03655 VideoMemory](https://arxiv.org/html/2601.03655v1)：完整 AB 后实际 §3.3 的 entity/attribute/reference-image 三 banks、LLM state matcher、history-conditioned new image 再 append tuple。关闭据未给新的 commit / identity validation / transition 约束或独立改变评价判断的反证，而非模块组合/领域/实验规模。无评分。

[04170 AgentDrift](https://arxiv.org/html/2601.04170v1)：完整 AB 后实际 §2.1–2.2/2.4、§4.4 limits。确有 ASI .30/.25/.25/.20、rolling50 / .75×3、initial20、summary100/50、baseline reset / routing / exemplar 调节，不能写“根本没有 operator 或参数”。贡献关闭只据成熟 taxonomy/composite-index/治理组合，关键效用是 modeled behavioral characteristics 与 synthetic deterministic ground truth，并非真实生产 trace 的独立有效条件；不以负向标题或安全主题直接准入。无评分。

[Netomi Jan08](https://openai.com/index/netomi/)：实际全文 L13–112。GPT4.1 tools / GPT5.2 planning、schema/PII/policy/fallback/traces、并行原则与 throughput，未给新 dependency/cancellation/effect 机制、匹配对照或改变成立边界的反证；贡献前关闭不等这些成熟原则无用。无评分。

实际检查当前 source 表与有限入口/原始本日元数据的边界：14 源均有实际范围与停点，Qwen60 / Hunyuan en9-total9 / MiMo16 nonindex 允许有限停止，不要求无具名线索的整个机构删除历史；Seed82total≠77returned，page80 false 不证明 Jan08 历史0；Google9月条/DeepMind页4、Meta混排页、OpenAI当前8条不是 Jan08 完整 dated catalog。上述必要日级保留及 arXiv 早 ID 未知重要 revision 无阴性覆盖权限；不把 current homepage / empty / search miss / four-theme union 364 当无遗漏。

## 5. 同一接口错因的跨日窄 POST（非候选重审）

按 root 请求实际读 Jan03/04/06 supplement 的 lastUpdatedDate attempt / 四个0返回修正，Jan06 README §1/2/6，以及随后 Jan03 README §2 与 Jan04 README §2/§6 三句 actual 改写。互斥 submittedDate 的 API 改写仍保尝试与 HTTP200/0，但明确旧 revision 阴性权限无效；Jan06 independent incoming identitydiff0 仍只对已交身份比较有效。语义一致通过。仅共同接口范围，不加载/重审三天其他候选、日期评分或日级验收；root 已确认此窄范围停止。

## 6. 当前 gate

FIRST：新增17完整 exact-v1 AB 独立核通过，14 papers 准入、两具体贡献关闭、04301 日期隔离。Necessary evidence：14 papers 全部按分数最低深度及受影响命题深入完成；机构另复用 root 实际深入核。Books：新增15＝1 Integrate（本审者 actual POST pass）＋2 ExistingCoverage＋11 Only Report＋1中心 Hold；不把中心 Hold 降级成贡献前关闭。

DAY 尚未授：已向作者请求窄修 supplement 前表 PII“去掉 cue”因果误读、SCRIBE 权重 .3/.7，以及 AgentDrift 不能断言无参数。待实际读取作者最终六部分、链接/表格/差额与保留范围后再追加最终结论；作者完成状态和机器检查不代该 gate。

### 最终 DAY — 通过至合同安全终态

上段为窄改前的 gate 记录。root 最终窄改 ready 后，实际顺读当前 README 六部分（§1/2、连续32行表、完整§4、§5/6），重读 supplement 新初筛表、SCRIBE 权重及最终停止记录。PII 现在明确 cue 分层/非逐样本 do，SCRIBE 为 .3 process+.7 outcome，AgentDrift 承认实际 ASI/阈值/reset 配方且只关闭成熟组合/模拟有效性范围；新增15最终决定与本文件 necessary / owner / POST 一致。旧阶段“提案/待root”按 supplement 最终段识别为阶段记录，不是未完成证据队列。机构实际原文/owner 的独立审者仍为 root，本审者复用该精确分批核，不冒称亲读机构全部全文。

独立实际检查：README 单连续32候选行，原17行与 git HEAD 对应行字节/order/date/score 完全相等；原§4全文到新增 SDCD 之前的 prefix 完全相等。原行 SHA256 为 `f88606b7bf04277314451598e15dd2a0068154f460d7077cd70397a289f4655f`。新增15＝1实际整合/2具体已有覆盖/11仅报告/1中心争议；旧6整合不重计，当前总实际整合7。新32分母没有加入贡献前关闭或日期待确认身份。未重审原17的有效层。

再运行本日 V3一致性校验通过，README / Ch72限定 diff-check 通过；README33本地链接、supplement1本地链接全部存在，本审计没有断链或尾空白。机器结果只作格式/链接补充，不作语义证书。Books actual diff 仍仅新增上述两段及源注，无既有内容删除；actual 源/owner/完整前后 POST 已独立通过。

本次补充自然日 DAY 通过：全部新增准入必要证据、具体 Books 差额、actual POST、分层负侧、必要日期与14有限来源停止边界形成一致六部分。普通工作0。SyncThink中心控制方向保原6分精确 Hold；04301实际日跨Jan08–09保外部日期隔离、不评分/不计候选；OpenAI/Google/Meta/Seed必要历史切片及早ID未知重要revision等保留项不授0发布、正面Coverage或全网无遗漏。未扩别日/全364摘要/全附件/未具名历史，不核运行实现或复现实验；只保存独有审计文件，未stage、commit、push，停止本日不接下一日。
