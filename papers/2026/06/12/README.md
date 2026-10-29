# Daily Research — 2026-06-12

**规范：** V3  
**窗口：** 2026-06-11T09:00:00+08:00 ～ 2026-06-12T09:00:00+08:00  
**状态：** 完成
**Books：** 纳入本次  
**补充窗口：** 2026-06-11 ～ 2026-06-11
**窗口说明：** 用户授权仅补遗漏；原小时窗、旧候选日期/评分和有效证据保留，新增材料按前一完整北京时间自然日检查，不迁移旧归属。
**冻结候选日期：** [补查前原档案](../_sources/daily-20260612/baseline-before-supplement-20261026.md)
**检查时间：** 2026-10-26T10:58:32+08:00

## 1. 结论

本轮Jun11自然日增量的扫描、初筛、逐项证据与Books落实已到安全终态，已通过唯一非作者[整日验收DAY§111](../_sources/daily-20260612/SUP_REVIEW_20261026.md)。正式表126家族＝保旧63＋新增63；旧日期、评分、小时窗及有效证据保留，仅GF-DiT章节locator有具名授权纠正。[本日导航](../_sources/daily-20260612/SUP_TITLE_NAV_20261026.json)1221元数据/242宽标题不是逐项队列；98完整题摘经独核为64准入线索/34贡献前N，其中11755纸本/在线日期冲突另隔离，其余63为确定本窗候选。新增63＝57真实SAVE+唯一POST整合、4具体已有覆盖（11552/12280/11672/12369）、2中心争议（11673/11907）；普通研究/owner/书稿写入/POST为0，不把题摘数或入选数说成实证贡献。11722实质重评只修受影响采用层且已§30实际POST，不重计家族。Google Publications/Meta历史目录、七具名归属线索及两中心争议不授正面Coverage/Evidence，均有精确重开条件。下方旧完成结论仅描述原轮有效范围。

表示的“生产—读取—干预”应分责：同一frozen forward里global与ROI读出可保留不同信号，attention重分配也不等得到新感知证据；选择方向、强度或视觉预算均需核实际consumer与旁侧退步。因而局部probe/较少tokens不能签无损、因果身份或安全，原输入与密集/专用读出保留为退路。

评价的reference、任务、候选集合和判分接口会改变结论：human写rubric与model答题、单独与同屏judge、node/path检索与邻域汇聚、functional-pass与追加checker不是同一测量对象。更高均分或一致性不能补独立真值；四项具体NC也据实际正文覆盖停止，没有为了产出改书。

训练与部署仍以可见性和真实反馈为界：局部attention的轨迹适配、事后hint蒸馏、参数belief更新和sim-to-real接触校准可以改变设计，但都增加数据/模型/运行与回归成本；预测、数值提示或经验gate不获得真实状态提交权，完整历史/显式采样、可信simulator、短horizon重观测与人工路径仍按条件共存。

### 旧轮有效结果（保留，不作为新增补查验收）

对本目录 bounded canonical raw bucket 的全部 561 个 identity 已完成 title + complete abstract 准入审计；fresh-context 独立复核将 3 个误收项改为分母前关闭，最终冻结 63 个 Candidate、498 个 family-specific audited Close，满足 `561 raw = 63 Candidate + 498 audited Close`，ordinary pending=0。候选 exact-v1 Evidence Review 与 Books 比较也已独立复核：9 项确有正文增量并已写入 Books，53 项由现有章节覆盖，1 项仅报告。9 条正文均位于首个顶层 `Review notes` 前，具备机制、owner、收益、trade-off、failure、fallback 与证据边界；13 条 trace 日期修正已复验，剩余执行队列为 0。日期 owner 不由 submitted/v1 timestamp、identifier sequence、DataCite created 或 normal cutoff 推导；official historical listing receipt 到位前不执行跨日迁移，该保留限制不阻塞本日报闭环。

当前合同评分已由非作者重新校准，不以已经深读或已经写入 Books 倒推高分。63 项现在分布为 `5 分 × 1、6 分 × 53、8 分 × 9`；既有 exact-v1 深审仍可复用，最低审阅等级按新分数表述。逐项旧分、新分和三维依据见 [current score recalibration](../_sources/daily-20260612/CURRENT_SCORE_RECALIBRATION_20260914.json)。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 官方RSS单响应的Jun10–12 pubDate邻段；Jun11 BJT内Oracle接入、BBVA、EU政策、Ona收购、科学案例为非研究/暂缓范围，明确关闭；不扩读全年 | 已检查 | 无；仅该RSS与主题范围，不授全球零研究 |
| SRC-ANTHROPIC | 官方Research listing第2页24项，Jul28跨Apr23；目标邻段Jun12 Public Record→Jun08N-days/biology，无Jun11 Research项，越界即停 | 已检查 | 无；一次403恢复后未拿失败授零 |
| SRC-GOOGLE-AI | Google June Blog一页Jun12→Jun10；DeepMind具名Jun11 multi-agent safety funding call完整core仅未来研究资助，贡献前关闭；Research Publications已打开但无Jun11日级历史目录 | 受阻 | 仅Publications历史日级目录；Blog已处理。定点有日期原始列表/具名Jun11正文可重开，不授该缺口正面Coverage |
| SRC-META-AI | Research当前HTML及目标日辅助检索；publication的可见CV子集May26→Jul03不能代替全部主题 | 受阻 | Jun11历史日级Research目录未恢复，不能由搜索空结果或可见卡片授零 |
| SRC-QWEN | 官方retrieval的type=qwen_ai及en-US/zh-CN各40articles，无分页；June1→June16→June23跨目标，停止完整响应 | 已检查 | 无；未使用无参数空数组 |
| SRC-DEEPSEEK | 官方Updates单页，Apr24V4→Jul31V4-Flash跨Jun11，无本日列项；不遍普通commits | 已检查 | 无；仅该研究发布入口 |
| SRC-MOONSHOT | Blog当前可见最新2025-11-07；官方GitHub按created排序单响应42仓库、June2026新建0，未将updated改成首公开 | 已检查 | 2026 Blog不是完整档案；只断言上述有限入口结果，不授全源零研究 |
| SRC-TENCENT-HUNYUAN | 首查Research实际公开调用，中文All POST page1/size100/renderType0，code0/total11/list11，May21Hy-MT2→Jul06Hy3，无下一页 | 已检查 | 无；Embodied-R1.5论文另由本日arXiv发现，不因目录未列而丢弃 |
| SRC-ZAI | Research日期首屏Jun16GLM5.2→May20ZCube，越目标即停，不翻更早列表 | 已检查 | 无 |
| SRC-BYTEDANCE-SEED | Papers第1/13页，1–20 of247；Jun11化学反应网络→Jun4→Jun3，目标科学应用范围前关闭，不扫其他12页 | 已检查 | 无；不通过通用owner重新引入AI for Science |
| SRC-BAIDU-ERNIE | Blog首屏最新May09文心5.1，已早于Jun11，不翻更早第2页 | 已检查 | 无 |
| SRC-XIAOMI-MIMO | Paper/Blog导航、官方Model Release的Sep22→Jun02ASR→Apr23，官方route frontmatter双语May30/Jun08/Jun10，无Jun11列项 | 已检查 | 无具名本日日期请求；主机拼写错误TLS已纠正，不作失败授零 |
| SRC-MINIMAX | Blog单目录Jun09MaxProof→Jun01M3，已越Jun11，停止邻段不扩旧正文 | 已检查 | 无 |
| SRC-ARXIV | 合法arxiv.content+registered Jun11 BJT查询2/2页；1221元数据与242宽标题只导航，语义收窄并具名旧候选去重，停止新主题。B1–B5加独立定点补核共98完整题摘经root校准64准入/34N；64精确DOI联合日界已由root/reader §40实际独核限定Jun11 BJT | 已检查 | 仅上述有限主题入口已停止，不授全分类/全网召回；确定候选必要/Books均已安全处置，11755与六跨日线索另隔离，旧归属不搬移 |

本轮实际查询、原字段与停止点见[来源记录](../_sources/daily-20260612/SUP_SOURCE_CHECK_20261026.md)。Google Publications/Meta历史目录限制与普通工作分开，不用于正面证据、Books或“无遗漏”断言。旧轮判定保留在 [`v3-reverse-admission-audit-20260910.json`](../_sources/daily-20260612/v3-reverse-admission-audit-20260910.json) 与 [`denominator-full-semantic-audit-v1.tsv`](../_sources/daily-20260612/denominator-full-semantic-audit-v1.tsv)，不成为本轮候选分母。旧owner audit撤回的单字段日期解释不改变当前合同合法联合上下界规则；本轮不把任何字段改名为官方实际公开时刻。

## 3. 候选与判断

### 本轮补充窗口新增（旧归属不搬移）

首批四项已完成非作者准入/必要证据/actual owner/PRE及真实SAVE后的唯一POST（[独核§1–7](../_sources/daily-20260612/SUP_REVIEW_20261026.md)），均为实际整合；日期为合同联合界限定的arXiv v1公告日，不是全球首公开证明。四项[精确日期原字段](../_sources/daily-20260612/SUP_DATACITE_EXACT_B1_20261026.jsonl)与[必要证据/反侧/actual owner/唯一稿](../_sources/daily-20260612/SUP_NECESSARY_B1_20261026.md)可复查。其后全部确定候选已滚动完成，最终逐项处置见下表与独核§110；首批结果本身不替整日验收。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Soft-Prompt Tuning for Fair and Efficient LLM Benchmark Evaluation](https://arxiv.org/html/2606.12117v1) | 2026-06-11 | 格式噪声会改变base模型排序；小预算soft-prompt适配与closed/open知识proxy分责，不能由更高分断言纯知识恢复；2 + 2 + 2 = 6 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 指定两段已SAVE且root唯一实际POST通过（§4） |
| [ICA Lens: Interpreting Language Models Without Training Another Dictionary](https://arxiv.org/html/2606.11722v1) | 2026-06-11 | 对非高斯compact coordinates保读/写映射及不稳尾部；匹配预算probe/TPP只支持有限比较，不取代overcomplete SAE或行为因果；2 + 1 + 2 = 5 | 深入完成 | 整合：WORLDVIEW-REPRESENTATION，[Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) v1真实POST §4保历史；current-v2受影响采用层已局部修正，root唯一§30实际POST恢复关闭，不拼跨版身份/排名 |
| [Learning What to Say to Your VLA: Mostly Harmless Vision Language Action Model Steering](https://arxiv.org/html/2606.12299v1) | 2026-06-11 | 语言反馈与是否介入分责；有害类校准只在指定条件下控制切换，保留平分/非严格阈值反例，不授任意OOD无害或物理安全；2 + 2 + 3 = 7 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA，[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) 指定两段已SAVE且root唯一实际POST通过（§7） |
| [APT: Action Expert Pretraining Improves Instruction Generalization of Vision-Language-Action Policies](https://arxiv.org/html/2606.12366v1) | 2026-06-11 | 在VLA语言失衡下先学VA prior再引语言；分阶段初始化与stop-gradient不是同一责任，stage2仍会联合改写先验；2 + 2 + 2 = 6 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA，[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) 指定两段已SAVE且root唯一实际POST通过（§7） |
| [Teaching Diffusion to Speculate Left-to-Right](https://arxiv.org/html/2606.11552v1) | 2026-06-11 | 将bidirectional drafter的uniform CE改为position decay/首错auxiliary与joint-prefix surrogate，实际接受与target语料收益须分账；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：INFER-SPECULATIVE-DECODING，[Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md) expected-prefix survival/continuation目标及target-regenerated CE基线正文；root §9实际必要/owner通过 |
| [Reroute, Don't Remove](https://arxiv.org/html/2606.12412v1) | 2026-06-11 | selected完整block、deferred hidden identity旁路后fullpool重新竞争；与保原位置的不可逆pruning分开验预算；2 + 2 + 2 = 6 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION，[Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) DocPrune后两段真实SAVE，root唯一POST §12通过 |
| [Redesign MoE Routers with Manifold Power Iteration](https://arxiv.org/html/2606.12397v1) | 2026-06-11 | 用expert Gram作用与norm retraction耦合router行，固定矩阵方向不授moving expert语义/收敛；2 + 2 + 2 = 6 | 深入完成 | 整合：MODEL-MOE，[Ch21](../../../../books/part-02-model/21-moe.md) 唯一稿PRE §13通过，真实SAVE后root唯一POST §14通过 |
| [On The Effectiveness-Fluency Trade-Off In LLM Conditioning: A Systematic Study](https://arxiv.org/html/2606.12234v1) | 2026-06-11 | 目标注入与非目标流畅/重复/IF分报，外部PPL与组合均值相关不能代逐条校准；2 + 2 + 2 = 6 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) CLaS后指定两段真实SAVE，root唯一POST §20通过 |
| [Fast Speech Foundation Model Distillation Using Interleaved Stacking](https://arxiv.org/html/2606.11766v1) | 2026-06-11 | 成长student的相对层位/固定teacher锚与受监督索引联动，不由相似性授函数恒等或全任务优势；2 + 1 + 2 = 5 | 深入完成 | 整合：TRAIN-SFT，[Ch29](../../../../books/part-04-training-system/29-sft.md) 共享projector段后两段真实SAVE，root唯一POST §20通过 |
| [A Fast Locality Simulator for GEMM Design-Space Exploration on Multi-Chiplet GPUs](https://arxiv.org/html/2606.11716v1) | 2026-06-11 | 固定placement仍可由CTA traversal经private L2改变跨片流量，functional bytes不等timing/power；2 + 1 + 2 = 5 | 深入完成 | 整合：INFER-GPU-MEMORY，[Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md) Chiplet首段后两段真实SAVE，root唯一POST §20通过 |
| [Holding the FP8 Quality Ceiling at 8-Bit Weights and Activations: INT8 and GGUF Post-Training Quantization of Ideogram 4.0 for Consumer GPUs](https://arxiv.org/html/2606.12280v1) | 2026-06-11 | 同seed质量与参考一致性分开，FFN保护/选择重叠和无fused kernel不加速的受限反侧；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：INFER-TENSORRT-LLM，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) 粒度校准、敏感层干预、逐例质量/参考与真实kernel正文；root §19实际必要/owner通过 |
| [Attention by Synchronization in Coupled Oscillator Networks](https://arxiv.org/html/2606.12059v1) | 2026-06-11 | 固定query anchors的理想球面等衡与shifted-cosine归一是另一算子；非零驱力/初值条件不授有限时间物理部署；2 + 1 + 2 = 5 | 深入完成 | 整合：MODEL-SELF-ATTENTION，[Ch14](../../../../books/part-02-model/14-self-attention.md) WTA后原两段及本人注已SAVE，root唯一§25实际POST通过/窄位释放 |
| [CORE-Bench](https://arxiv.org/html/2606.11864v1) | 2026-06-11 | 代码检索从snippet转repo-state，pre-change过滤与edit/support相关性分责，agent标签不证完备；2 + 1 + 2 = 5 | 深入完成 | 整合：AGENT-RAG，[Ch76](../../../../books/part-07-agent/76-rag.md) corpus-state段后原两段及本人注已SAVE，root唯一§25实际POST通过/窄位释放 |
| [Higher-Order Token Interactions via Quantum Attention](https://arxiv.org/html/2606.11673v1) | 2026-06-11 | 有限精度单层表达/局部与all-to-all梯度边界须按同一函数族与编码核验；2 + 2 + 2 = 6 | 争议 | 暂缓：Match族到monomial缺reduction、泛化upper非failure lower及basis-loading/训练encoder身份差；root §24安全H通过，不改Books |
| [Bridging the Morphology Gap: Adapting VLA Models to Dexterous Manipulation via Intent-Conditioned Fine-Tuning](https://arxiv.org/html/2606.12109v1) | 2026-06-11 | 粗手关节经FK aperture代理接独立dexterity diffusion head，两阶段接口与真实接触充分性分责；2 + 2 + 2 = 6 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA，[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) latent-goal binding后原两段真实SAVE，root唯一§30实际POST通过 |
| [Kuramoto Attention: Synchronizing Self-Attention on the Torus](https://arxiv.org/html/2606.11585v1) | 2026-06-11 | identity-value phasor的切向更新与signed gate，固定A解释不授完整自适应层能量下降；2 + 1 + 2 = 5 | 深入完成 | 整合：MODEL-SELF-ATTENTION，[Ch14](../../../../books/part-02-model/14-self-attention.md) signed归一后原两段真实SAVE，root唯一§30实际POST通过 |
| [VOID: Defeating Unauthorized Mimicry in Latent Diffusion Models](https://arxiv.org/html/2606.12263v1) | 2026-06-11 | 发布图像的VAE uncertainty/CFG双代理输入防护与未来适应者边界，非绝对语义抹除；2 + 2 + 2 = 6 | 深入完成 | 整合：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) WAF后原两段真实SAVE，root唯一§34实际POST通过 |
| [DrivingAgent: Design and Scheduling Agents for Autonomous Driving Systems](https://arxiv.org/html/2606.12236v1) | 2026-06-11 | sensor event-time/profile与未来帧激活由确定性执行器验资格，compute FPS不代全链deadline；2 + 2 + 2 = 6 | 深入完成 | 整合：AGENT-PLATFORM，[Ch84](../../../../books/part-07-agent/84-agent-platform.md) Nalar后原两段真实SAVE，root唯一§35实际POST通过 |
| [MultiToP: Learning to Patch Visual Tokens to Mitigate Hallucinations in Video Large Multimodal Models](https://arxiv.org/html/2606.11792v1) | 2026-06-11 | 保位置/数量的共享patch替换，训练答案attention代理不代局部证据真值；2 + 2 + 2 = 6 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION，[Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) recoverable routing后原两段真实SAVE，root唯一§35实际POST通过 |
| [World Pilot: Steering Vision-Language-Action Models with World-Action Priors](https://arxiv.org/html/2606.12403v1) | 2026-06-11 | 冻结WAM的future latent residual与粗trajectory prefix分别消费，两路prior不是真实未来；2 + 2 + 2 = 6 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA，[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) 07931后原两段真实SAVE，root唯一§39实际POST通过 |
| [UniIntervene: Agentic Intervention for Efficient Real-World Reinforcement Learning](https://arxiv.org/html/2606.12372v1) | 2026-06-11 | 停滞proxy触发、memory高value目标与独立recovery proposal分责，F1不代恢复成功；2 + 2 + 2 = 6 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA，[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) Fleet后原两段真实SAVE，root唯一§39实际POST通过 |
| [Ambient Diffusion Policy: Imitation Learning from Suboptimal Data in Robotics](https://arxiv.org/html/2606.12365v1) | 2026-06-11 | 按noise time限定P/Q数据资格而非全time权重或整条过滤；2 + 2 + 2 = 6 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA，[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) 05737后原两段真实SAVE，root唯一§39实际POST通过 |
| [Path convergence in diffusion models](https://arxiv.org/html/2606.12161v1) | 2026-06-11 | 同起点/噪声的有限经验diffusion路径耦合与metric边界；2 + 2 + 2 = 6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS，[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) 原两段真实SAVE，jun12_review_finish唯一§44实际POST通过 |
| [DAM-VLA: Decoupled Asynchronous Multimodal Vision Language Action model](https://arxiv.org/html/2606.12105v1) | 2026-06-11 | 各模态history/buffer与action clock分责，100Hz不等replan；2 + 2 + 2 = 6 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA，[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) 原两段真实SAVE，jun12_review_finish唯一§44实际POST通过 |
| [Adaptive Multi-Resolution Procedural Knowledge Compression for Large Language Models](https://arxiv.org/html/2606.12203v1) | 2026-06-11 | skill/target绑定的多分辨率前缀与银参考预算接口；2 + 2 + 2 = 6 | 深入完成 | 整合：AGENT-CONTEXT，[Ch75](../../../../books/part-07-agent/75-context.md) 原两段真实SAVE，jun12_review_finish唯一§44实际POST通过 |
| [InternVideo3: Agentify Foundation Models with Multimodal Contextual Reasoning](https://arxiv.org/html/2606.12195v1) | 2026-06-11 | 多模态GQA转latent时QK-Norm近似、模态latent与恢复条件；2 + 2 + 2 = 6 | 深入完成 | 整合：MODEL-KV-CACHE，[Ch19](../../../../books/part-02-model/19-kv-cache.md) 原两段真实SAVE，jun12_review_finish唯一§51实际POST通过 |
| [Re-evaluating Confidence Remasking in Masked Diffusion Language Models](https://arxiv.org/html/2606.12232v1) | 2026-06-11 | 强unmask基线下remasking边际与shadow近似/flipflop诊断；2 + 2 + 3 = 7 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS，[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) 原两段真实SAVE，jun12_review_finish唯一§51实际POST通过 |
| [Selection Integrity for LLM Graph Memory: An Accumulability Criterion for Information-Flow-Blind Retrieval](https://arxiv.org/html/2606.12290v1) | 2026-06-11 | 未返回的低信任结构亦可改selected set，内容IFC与选择来源分责；2 + 2 + 3 = 7 | 深入完成 | 整合：AGENT-MEMORY，[Ch77](../../../../books/part-07-agent/77-memory.md) 原两段真实SAVE，jun12_review_finish唯一§51实际POST通过 |
| [CHORUS: Decentralized Multi-Embodiment Collaboration with One VLA Policy](https://arxiv.org/html/2606.12352v1) | 2026-06-11 | 共享policy权重与每机器人本地执行分离，局部可见/时序条件；2 + 1 + 2 = 5 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA，[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) 原两段真实SAVE，jun12_review_finish唯一§52实际POST通过 |
| [Beyond Fully Random Masking: Attention-Guided Denoising and Optimization for Diffusion Language Models](https://arxiv.org/html/2606.12273v1) | 2026-06-11 | 完整completion图提出available-mass顺序与hubweight，训练特权分责；2 + 2 + 2 = 6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS，[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) 原两段真实SAVE，jun12_review_finish唯一§52实际POST通过 |
| [Exploration Structure in LLM Agents for Multi-File Change Localization](https://arxiv.org/html/2606.11976v1) | 2026-06-11 | 行为必需-v-PR触及的gold对象可让同预测F1排序翻转；2 + 1 + 2 = 5 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 原两段真实SAVE，jun12_review_finish唯一§58实际POST通过 |
| [WorldReasoner: Evaluating Whether Language Model Agents Forecast Events with Valid Reasoning](https://arxiv.org/html/2606.11816v1) | 2026-06-11 | 历史retrieval gate-v-参数cutoff proxy与hindsight-v-calibration分离；2 + 2 + 2 = 6 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 原两段真实SAVE，jun12_review_finish唯一§58实际POST通过 |
| [Tail-Aware Adaptive-k: Query-Adaptive Context Selection for Retrieval-Augmented Generation](https://arxiv.org/html/2606.11907v1) | 2026-06-11 | query自适应tail切点的knee/reflection/CVM中心接口；2 + 2 + 2 = 6 | 争议 | 暂缓：AGENT-RAG，原式内部knee与反射/稳定性保证不闭，jun12_review_finish §56独核H，不进入Books |
| [When Does Language Matter? Multilingual Instructions Reveal Step-wise Language Sensitivity in Vision-Language-Action Models](https://arxiv.org/html/2606.11906v1) | 2026-06-11 | English轨迹离线梯度reference与在线hidden邻域step介入分责；2 + 2 + 2 = 6 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA，[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) 原两段真实SAVE，jun12_review_finish唯一§59实际POST通过 |
| [Phase Transitions in Attention: A Bayesian Theory of Copy Head Emergence](https://arxiv.org/html/2606.12058v1) | 2026-06-11 | 受控copy模型两模式竞争与attention归一化改变转变阶数；2 + 1 + 3 = 6 | 深入完成 | 整合：WORLDVIEW-LLM-INTELLIGENCE，[Ch8](../../../../books/part-01-worldview/08-why-llms-show-intelligence.md) 原两段真实SAVE，jun12_review_finish唯一§71实际POST通过 |
| [Beyond representational alignment with brain-guided language models for robust reasoning](https://arxiv.org/html/2606.11893v1) | 2026-06-11 | 外部参考映射读数与去截距写目标、label纠错权限分离；2 + 1 + 3 = 6 | 深入完成 | 整合：WORLDVIEW-REPRESENTATION，[Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) 原两段真实SAVE，jun12_review_finish唯一§71实际POST通过 |
| [IAPO: Input Attribution-Aware Policy Optimization for Tool Use in Small Multimodal Agents](https://arxiv.org/html/2606.11652v1) | 2026-06-11 | teacher/actor输入块梯度代理分布匹配作为额外工具训练监督；2 + 2 + 2 = 6 | 深入完成 | 整合：AGENT-TOOL-CALLING，[Ch78](../../../../books/part-07-agent/78-tool-calling.md) 原两段真实SAVE，jun12_review_finish唯一§72实际POST通过 |
| [Dummy Backdoor as a Defense: Removing Unknown Backdoors via Shared Internal Mechanisms for Generative LLMs](https://arxiv.org/html/2606.11648v1) | 2026-06-11 | 已知dummy作为同攻击目标下未知trigger清理proxy；2 + 2 + 3 = 7 | 深入完成 | 整合：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) 原两段真实SAVE，jun12_review_finish唯一§72实际POST通过 |
| [Improving Cross-Format Robustness in Language Models with Multi-Format Training](https://arxiv.org/html/2606.11643v1) | 2026-06-11 | source-item对齐的any-v-all格式breadth/consistency及扩样预算；2 + 1 + 2 = 5 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 原两段真实SAVE，jun12_review_finish唯一§72实际POST通过 |
| [Can Open-Source LLM Agents Replace Static Application Security Testing Tools? An Empirical Assessment](https://arxiv.org/html/2606.11672v1) | 2026-06-11 | 相对Bandit reference的定位/类别match与potential-FP人口不等漏洞真值；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) reference资格、未列gold保Unknown和条件分母正文，reader §67具体NC通过、不改书 |
| [From Prompts to Tokens: Internalizing Causal Supervision in Vision-Language Model for Multi-Image Causal Reasoning](https://arxiv.org/html/2606.11745v1) | 2026-06-11 | 先绑定latent节点身份再监督关系边，oracle图不代因果发现；2 + 2 + 2 = 6 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION，[Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) 原两段真实SAVE，jun12_review_finish唯一§76实际POST通过 |
| [TacCoRL: Integrating Tactile Feedback into VLA via Simulation](https://arxiv.org/html/2606.11743v1) | 2026-06-11 | sim后训练需joint-response与policy-facing触觉校准及real anchor；2 + 2 + 2 = 6 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA，[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) 原两段真实SAVE，jun12_review_finish唯一§76实际POST通过 |
| [CompRank: Efficient LLM Reranking via Token-Level Compression and Decoding-Free Scoring](https://arxiv.org/html/2606.11700v1) | 2026-06-11 | 独立doc state、query消费支集与同attentionmass候选监督分责；2 + 2 + 2 = 6 | 深入完成 | 整合：AGENT-RAG，[Ch76](../../../../books/part-07-agent/76-rag.md) 原两段真实SAVE，jun12_review_finish唯一§76实际POST通过 |
| [Architecture-Aware Reinforcement Learning Makes Sliding-Window Attention Competitive in Math Reasoning](https://arxiv.org/html/2606.11634v1) | 2026-06-11 | 局部attention需同可见性轨迹/RL适配，conversion后退不证能力天花板；2 + 2 + 2 = 6 | 深入完成 | 整合：MODEL-LONG-CONTEXT，[Ch22](../../../../books/part-02-model/22-long-context.md) 原两段真实SAVE，jun12_review_finish唯一§85实际POST通过 |
| [Information-Theoretic Decomposition for Multimodal Interaction Learning](https://arxiv.org/html/2606.11614v1) | 2026-06-11 | 单模态与组合候选分路、component读出不等真实PID；2 + 2 + 2 = 6 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION，[Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) 原两段真实SAVE，jun12_review_finish唯一§85实际POST通过 |
| [When is Your LLM Steerable?](https://arxiv.org/html/2606.11599v1) | 2026-06-11 | 同已实现早prefix双前向预测干预剂量并排序候选；2 + 2 + 2 = 6 | 深入完成 | 整合：WORLDVIEW-REPRESENTATION，[Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) 原两段真实SAVE，jun12_review_finish唯一§85实际POST通过 |
| [AVIS: Adaptive Test-Time Scaling for Vision-Language Models](https://arxiv.org/html/2606.11576v1) | 2026-06-11 | 视觉token与rollout预期预算分阶段分配、概率身份需校准；2 + 2 + 2 = 6 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION，[Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) 原两段真实SAVE，jun12_review_finish唯一§85实际POST通过 |
| [4DP-QA: Scalable QA for 4D Perception in Vision Language Models](https://arxiv.org/html/2606.11568v1) | 2026-06-11 | 固定query相机重投影提供物体/相机运动参照系对照；2 + 1 + 2 = 5 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION，[Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) 原两段真实SAVE，jun12_review_finish唯一§92实际POST通过 |
| [GraphInfer-Bench: Benchmarking LLM's Inference Capability on Graphs](https://arxiv.org/html/2606.11562v1) | 2026-06-11 | neighborhood汇聚任务与node/path lookup、hard结构-v-prose评分分责；2 + 1 + 2 = 5 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 原两段真实SAVE，jun12_review_finish唯一§92实际POST通过 |
| [HERO: Hindsight-Enhanced Reflection from Environment Observations for Agentic Self-Distillation](https://arxiv.org/html/2606.11559v1) | 2026-06-11 | causal rollout与事后future局部hint在原action监督边界分离；2 + 2 + 2 = 6 | 深入完成 | 整合：TRAIN-SFT，[Ch29](../../../../books/part-04-training-system/29-sft.md) 原两段真实SAVE，jun12_review_finish唯一§92实际POST通过 |
| [Counterexample Guided Learning in the Large using Reasoning Agents](https://arxiv.org/html/2606.11521v1) | 2026-06-11 | symbolic counterexample cluster与外部Equiv判等分责；2 + 2 + 2 = 6 | 深入完成 | 整合：AGENT-REFLECTION，[Ch80](../../../../books/part-07-agent/80-reflection.md) 原两段真实SAVE，jun12_review_finish唯一§92实际POST通过 |
| [Steering Where to Listen: Instruction-Based Activation Steering Redirects Temporal Attention in Large Audio-Language Models](https://arxiv.org/html/2606.11400v1) | 2026-06-11 | 同音频instruction contrast改变时间attention的受限定位读出；2 + 1 + 2 = 5 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION，[Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) 原两段真实SAVE，jun12_review_finish唯一§93实际POST通过 |
| [Task-Aligned Stability Analysis of Vision-Language Models for Autonomous Driving Hazard Detection](https://arxiv.org/html/2606.11889v1) | 2026-06-11 | embedding几何drift与固定task margin/clean-relative flips分账；2 + 1 + 2 = 5 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 原两段真实SAVE，jun12_review_finish唯一§93实际POST通过 |
| [PLUME: Probabilistic Latent Unified World Modeling and Parameter Estimation for Multi-Finger Manipulation](https://arxiv.org/html/2606.11396v1) | 2026-06-11 | 参数belief粒子与action-conditioned预测联合flow、采样防坍塌；2 + 2 + 2 = 6 | 深入完成 | 整合：MULTIMODAL-WORLD-MODELS，[Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) 原两段真实SAVE，jun12_review_finish唯一§96实际POST通过 |
| [Overcoming State Inertia in Full-Duplex Spoken Language Models via Activation Steering](https://arxiv.org/html/2606.11386v1) | 2026-06-11 | 双流首词切换proxy与onset触发短干预、完整回答分验；2 + 2 + 2 = 6 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION，[Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) 原两段真实SAVE，jun12_review_finish唯一§96实际POST通过 |
| [Beyond Third-Person Audits: Situated Interaction Auditing for User-Centered LLM Bias Research](https://arxiv.org/html/2606.12247v1) | 2026-06-11 | 同请求interlocutor profile条件与第三方群体审计人口分开；2 + 1 + 2 = 5 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 原两段真实SAVE，jun12_review_finish唯一§101实际POST通过 |
| [Are LLMs Bad at Moral Reasoning?](https://arxiv.org/html/2606.11635v1) | 2026-06-11 | human写rubric-v-model答题不对称及标准改写estimand变化；2 + 1 + 2 = 5 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 原两段真实SAVE，jun12_review_finish唯一§101实际POST通过 |
| [Should LLM Agents Decide in Social Simulations? Comparing Finite-State and LLM-Based Decision Policies](https://arxiv.org/html/2606.12369v1) | 2026-06-11 | 明确Markov policy与LLM selector的分布及费用负对照；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖：AGENT-TOOL-CALLING，[Ch78](../../../../books/part-07-agent/78-tool-calling.md) 实际“随机策略需要真正的Sampler State”三段已承载，reader§97具体NC，不改书 |
| [A Scalable PyTorch Abstraction for Multi-GPU Gaussian Splatting](https://arxiv.org/html/2606.11390v1) | 2026-06-11 | aggregate device把分片/events/CPUfallback交operator backend；2 + 2 + 2 = 6 | 深入完成 | 整合：TRAIN-DISTRIBUTED-TRAINING，[Ch36](../../../../books/part-04-training-system/36-distributed-training.md) 原两段真实SAVE，jun12_review_finish唯一§103实际POST通过 |
| [How Seemingly Inconsequential Design Choices Dictate Performance of LLMs in Pathology](https://arxiv.org/html/2606.12407v1) | 2026-06-11 | 四输入因素改变同模型baseline差额，探索/择优与heldout分账；2 + 2 + 2 = 6 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 原两段真实SAVE，jun12_review_finish唯一§106实际POST通过 |
| [MPC-Patch-Bench: Security-Aware LLM Code Patch for Multi-Party Computation](https://arxiv.org/html/2606.11416v1) | 2026-06-11 | F2P/P2P之后数值oracle与安全规则的检查人口分离；2 + 1 + 2 = 5 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 原两段真实SAVE，jun12_review_finish唯一§106实际POST通过 |
| [Frozen Foundation-Model Embeddings Discard Small-Lesion Signal in Chest Radiography: Implications for Pre-Deployment Evaluation](https://arxiv.org/html/2606.11606v1) | 2026-06-11 | same-frozen-forward的global-v-oracleROI pooling局部信号可读性；2 + 1 + 2 = 5 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION，[Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) 原两段真实SAVE，jun12_review_finish唯一§109实际POST通过 |
| [On the Limits of LLM-as-Judge for Scientific Novelty Assessment](https://arxiv.org/html/2606.12071v1) | 2026-06-11 | author-anchor与独立-v-同屏judge、逐维/逐judge best-of-five分责；2 + 2 + 2 = 6 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 原两段真实SAVE，jun12_review_finish唯一§110实际POST通过 |
| [Which Models Are Our Models Built On? Auditing Invisible Dependencies in Modern LLMs](https://arxiv.org/html/2606.12385v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“We introduce ModSleuth, an agentic system that recursively reconstructs LLM dependency graphs from public artifacts with source-grounded evidence.”，该机制在 TRAIN-DATA 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：TRAIN-DATA，[owner](../../../../books/part-04-training-system/27-data.md)；正文锚点：Data lineage 是训练可复现性的前提 |
| [Muse Spark Safety & Preparedness Report](https://arxiv.org/html/2606.12429v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《Muse Spark Safety & Preparedness Report》关闭或降池；完整摘要显示“In this report, we first present evaluations for catastrophic risk domains under Meta's Advanced AI Scaling Framework, along with the evidence that informed our launch decision.”。该增量直接改变 PLATFORM-SECURITY 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；正文锚点：从资产与信任边界开始 |
| [ToolSense: A Diagnostic Framework for Auditing Parametric Tool Knowledge in LLMs](https://arxiv.org/html/2606.12451v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《ToolSense: A Diagnostic Framework for Auditing Parametric Tool Knowledge in LLMs》关闭或降池；完整摘要显示“We introduce \textbf{ToolSense}, an open-source LLM-powered diagnostic framework that takes any tool catalog as input and automatically generates three benchmarks: a Realistic Retrieval Benchmark (RRB) with queries at three ambiguity tiers, an MCQ probing benchmark, and a QA probing benchmark.”。该增量直接改变 AGENT-TOOL-CALLING 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：AGENT-TOOL-CALLING，[owner](../../../../books/part-07-agent/78-tool-calling.md)；正文锚点：Tool Contract |
| [Influence Factors on RAG Poisoning](https://arxiv.org/html/2606.12469v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“However, this reliance on retrieved content introduces vulnerabilities to poisoning attacks, in which adversarial documents can manipulate both the retrieval process and the generated outputs.”，该机制在 AGENT-RAG 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：AGENT-RAG，[owner](../../../../books/part-07-agent/76-rag.md)；正文锚点：RAG 安全必须覆盖完整状态生命周期 |
| [SAIGuard: Communication-State Simulation for Proactive Defense of LLM Multi-Agent Systems](https://arxiv.org/html/2606.12474v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 3 + 2 + 3 = 8；原筛选把《SAIGuard: Communication-State Simulation for Proactive Defense of LLM Multi-Agent Systems》关闭或降池；完整摘要显示“To address this, we propose a proactive defense framework for MAS security, namely a Simulation-aware Interception Guard (SAIGuard).”。该增量直接改变 PLATFORM-SECURITY 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 深入完成 | 整合：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；正文写入与独立 post-write audit 已完成 |
| [ReCal: Reward Calibration for RL-based LLM Routing](https://arxiv.org/html/2606.12479v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《ReCal: Reward Calibration for RL-based LLM Routing》关闭或降池；完整摘要显示“To address these issues, we propose \textbf{ReCal}, a \textbf{\underline{Re}}ward \textbf{\underline{Cal}}ibration framework for RL-based LLM routing.”。该增量直接改变 INFER-SCHEDULING 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：INFER-SCHEDULING，[owner](../../../../books/part-05-inference-system/56-inference-scheduling.md)；正文锚点：Model Routing 与 Test-time Scaling 必须结算同一个 Budget |
| [DynamicPTQ: Mitigating Activation Quantization Collapse via Residual-Stream Dynamics](https://arxiv.org/html/2606.12487v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“To characterize this behavior, we introduce Jump Ratio and Historical Feature SNR.”，该机制在 INFER-TENSORRT-LLM 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：INFER-TENSORRT-LLM，[owner](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；正文锚点：量化为什么不自动带来加速 |
| [ITME: Inference Tiered Memory Expansion with Disaggregated CXL-Hybrid Memories](https://arxiv.org/html/2606.12556v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“In this paper, we propose ITME (Inference Tiered Memory Expansion), which leverages a CXL-hybrid memory to present a massive, TB-scale byte-addressable remote memory expansion.”，该机制在 INFER-GPU-MEMORY 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：INFER-GPU-MEMORY，[owner](../../../../books/part-05-inference-system/54-gpu-memory.md)；正文锚点：Weights 与 KV 的联合 HBM 预算：可提交的运行时精度页 |
| [Arbor: Tree Search as a Cognition Layer for Autonomous Agents](https://arxiv.org/html/2606.12563v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《Arbor: Tree Search as a Cognition Layer for Autonomous Agents》关闭或降池；完整摘要显示“Prior autonomous optimization systems operate on isolated targets with stateless evaluation.”。该增量直接改变 AGENT-WORKFLOW 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：AGENT-WORKFLOW，[owner](../../../../books/part-07-agent/81-workflow.md)；正文锚点：State Machine 是基本模型 |
| [Beyond Attack Success Rate: Examining Trigger Leakage in Vision-Language Agentic Systems](https://arxiv.org/html/2606.12586v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 3 + 2 + 3 = 8；原筛选把《Beyond Attack Success Rate: Examining Trigger Leakage in Vision-Language Agentic Systems》关闭或降池；完整摘要显示“In this work, we formalize the failure of trigger precision as "trigger leakage": inputs that are visually or semantically close to the intended trigger and therefore inadvertently activate the attacker-specified behavior.”。该增量直接改变 PLATFORM-SECURITY 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 深入完成 | 整合：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；正文写入与独立 post-write audit 已完成 |
| [Strategic Decision Support for AI Agents](https://arxiv.org/html/2606.12587v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《Strategic Decision Support for AI Agents》关闭或降池；完整摘要显示“We propose a framework for strategic decision support for AI agents through an optimization problem that minimizes support usage subject to controlling a counterfactual missed-support error: the probability that the agent acts alone on instances where support would have materially improved its output.”。该增量直接改变 AGENT-PLANNING 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：AGENT-PLANNING，[owner](../../../../books/part-07-agent/79-planning.md)；正文锚点：先校准不确定性，再决定行动、询问或探索 |
| [Keep Policy Gradient in Charge: Sibling-Guided Credit Distillation for Long-Horizon Tool-Use Agents](https://arxiv.org/html/2606.12634v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《Keep Policy Gradient in Charge: Sibling-Guided Credit Distillation for Long-Horizon Tool-Use Agents》关闭或降池；完整摘要显示“We introduce Sibling-Guided Credit Distillation (SGCD), which uses distillation for bounded credit weighting rather than as a competing actor loss.”。该增量直接改变 TRAIN-GRPO 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：TRAIN-GRPO，[owner](../../../../books/part-04-training-system/33-grpo.md)；正文锚点：从一个终局标量到 Typed Credit：Reward 必须匹配决策边界 |
| [Eidola: Modeling Multi-GPU Network Communication Traffic in Distributed AI Workloads](https://arxiv.org/html/2606.12638v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《Eidola: Modeling Multi-GPU Network Communication Traffic in Distributed AI Workloads》关闭或降池；完整摘要显示“In this work, we introduce Eidola, a scalable extension to the gem5 simulation framework that enables detailed modeling of inter-GPU communication traffic.”。该增量直接改变 TRAIN-DISTRIBUTED-TRAINING 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：TRAIN-DISTRIBUTED-TRAINING，[owner](../../../../books/part-04-training-system/36-distributed-training.md)；正文锚点：从静态通信配置到受验证的 Collective Policy |
| [Evoflux: Inference-Time Evolution of Executable Tool Workflows for Compact Agents](https://arxiv.org/html/2606.12674v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《Evoflux: Inference-Time Evolution of Executable Tool Workflows for Compact Agents》关闭或降池；完整摘要显示“We introduce Evoflux, an inference-time evolutionary search method that treats compact tool use as the repair of executable tool workflows.”。该增量直接改变 AGENT-WORKFLOW 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：AGENT-WORKFLOW，[owner](../../../../books/part-07-agent/81-workflow.md)；正文锚点：Release 与 Optimization 必须共享 Workflow Identity |
| [M*: A Modular, Extensible, Serving System for Multimodal Models](https://arxiv.org/html/2606.12688v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“Here we present M*, a universal serving system for efficient serving of composite AI models.”，该机制在 INFER-KSERVE-TOPOLOGY 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：INFER-KSERVE-TOPOLOGY，[owner](../../../../books/part-05-inference-system/53-kserve-llm.md)；正文锚点：组件与 Ownership |
| [SMSR: Certified Defence Against Runtime Memory Poisoning in Persistent LLM Agent Systems](https://arxiv.org/html/2606.12703v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“We present Signed Memory with Smoothed Retrieval (SMSR), the first defence with a certified robustness bound for this setting.”，该机制在 PLATFORM-SECURITY 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；正文锚点：从资产与信任边界开始 |
| [Smarter Saboteurs, Better Fixers: Scaling & Security in Linear Multi-Agent Workflows](https://arxiv.org/html/2606.12709v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《Smarter Saboteurs, Better Fixers: Scaling & Security in Linear Multi-Agent Workflows》关闭或降池；完整摘要显示“Attackers may leverage prompt-injection or jailbreaking to sabotage individual agents within MAS workflows, but the interaction between model scaling and system-level resilience remains poorly understood.”。该增量直接改变 PLATFORM-SECURITY 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；正文锚点：从资产与信任边界开始 |
| [PI-Hunter: Automated Red-Teaming for Exposing and Localizing Prompt Injections](https://arxiv.org/html/2606.12737v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“We propose PI-Hunter, an automated agentic auditing framework for proactive vulnerability exposure in LLM agents.”，该机制在 PLATFORM-SECURITY 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；正文锚点：从资产与信任边界开始 |
| [Prefill Awareness in Large Language Models](https://arxiv.org/html/2606.12747v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 3 + 2 + 3 = 8；原筛选把《Prefill Awareness in Large Language Models》关闭或降池；完整摘要显示“If AI models can recognize and act on the fact their prior assistant messages have been inserted or edited, the effectiveness and validity of these methods could be compromised.”。该增量直接改变 PLATFORM-EVALUATION-SYSTEM 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；正文写入与独立 post-write audit 已完成 |
| [Detecting Functional Memorization in Code Language Models](https://arxiv.org/html/2606.12764v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 3 + 2 + 3 = 8；原筛选把《Detecting Functional Memorization in Code Language Models》关闭或降池；完整摘要显示“We formalize this through a counterfactual framework, comparing target models (exposed to specific code) against reference models (not exposed) and requiring functional equivalence only for the target.”。该增量直接改变 TRAIN-DATA 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 深入完成 | 整合：TRAIN-DATA，[owner](../../../../books/part-04-training-system/27-data.md)；正文写入与独立 post-write audit 已完成 |
| [Rigel: Reverse-Engineering the Metal 4.1 Tensor Compute Path on the Apple M4 Max GPU](https://arxiv.org/html/2606.12765v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“We present Rigel, an empirical characterization of this path on a single Apple M4 Max (a pre-neural-accelerator generation).”，该机制在 INFER-TENSORRT-LLM 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：INFER-TENSORRT-LLM，[owner](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；正文锚点：量化为什么不自动带来加速 |
| [ProPlay: Procedural World Models for Self-Evolving LLM Agents](https://arxiv.org/html/2606.12780v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《ProPlay: Procedural World Models for Self-Evolving LLM Agents》关闭或降池；完整摘要显示“We introduce ProPlay, a procedural world model that supports procedure-level preplay, where agents can rehearse future procedural paths using the learned world knowledge.”。该增量直接改变 AGENT-PLANNING 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：AGENT-PLANNING，[owner](../../../../books/part-07-agent/79-planning.md)；正文锚点：从目标到状态图 |
| [The Containment Gap: How Deployed Agentic AI Frameworks Fail Public-Facing Safety Requirements](https://arxiv.org/pdf/2606.12797v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“We ask whether the frameworks used to build these systems provide architectural-level structural safety guarantees.”，该机制在 PLATFORM-SECURITY 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；正文锚点：从资产与信任边界开始 |
| [LoHoSearch: Benchmarking Long-Horizon Search Agents Beyond the Human Difficulty Ceiling](https://arxiv.org/html/2606.12837v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《LoHoSearch: Benchmarking Long-Horizon Search Agents Beyond the Human Difficulty Ceiling》关闭或降池；完整摘要显示“To address this, we introduce LoHoSearch (Long-Horizon Search Agents), a challenging benchmark comprising 544 human-verified questions across 11 domains.”。该增量直接改变 PLATFORM-EVALUATION-SYSTEM 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；正文锚点：Evaluation Identity 必须包含 Harness 与 Environment |
| [HarnessBridge: Learnable Bidirectional Controller for LLM Agent Harness](https://arxiv.org/html/2606.12882v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；完整摘要确认其研究 learnable bidirectional harness projection，属于 LLM Agent runtime 范围，因此保留 Candidate。 | 标准完成 | 已有覆盖：AGENT-WORKFLOW，[owner](../../../../books/part-07-agent/81-workflow.md)；现有 state-machine、compiler/executor 与 learned transition 合同已经覆盖该局部实现。 |
| [SENTINEL: Failure-Driven Reinforcement Learning for Training Tool-Using Language Model Agents](https://arxiv.org/html/2606.12908v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《SENTINEL: Failure-Driven Reinforcement Learning for Training Tool-Using Language Model Agents》关闭或降池；完整摘要显示“We propose SENTINEL, a failure-driven reinforcement learning framework that turns the Solver's rollout failures into targeted training tasks.”。该增量直接改变 TRAIN-DATA 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：TRAIN-DATA，[owner](../../../../books/part-04-training-system/27-data.md)；正文锚点：Data lineage 是训练可复现性的前提 |
| [MAStrike: Shapley-Guided Collusive Red-Teaming on Multi-Agent Systems](https://arxiv.org/html/2606.12918v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 3 + 2 + 3 = 8；原筛选把《MAStrike: Shapley-Guided Collusive Red-Teaming on Multi-Agent Systems》关闭或降池；完整摘要显示“We propose MAStrike, a closed-loop framework for collusive red-teaming in hierarchical MAS.”。该增量直接改变 PLATFORM-SECURITY 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 深入完成 | 整合：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；正文写入与独立 post-write audit 已完成 |
| [MARS: Margin-Adversarial Risk-controlled Stopping for Parallel LLM Test-time Scaling](https://arxiv.org/html/2606.12935v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 3 + 2 + 3 = 8；原筛选把《MARS: Margin-Adversarial Risk-controlled Stopping for Parallel LLM Test-time Scaling》关闭或降池；完整摘要显示“Based on this observation, we introduce MARS, a margin-adversarial stopping rule that estimates which active traces are likely to change their answers and stops once the leader remains safe under a conservative bound on future vote movement.”。该增量直接改变 INFER-SCHEDULING 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 深入完成 | 整合：INFER-SCHEDULING，[owner](../../../../books/part-05-inference-system/56-inference-scheduling.md)；正文写入与独立 post-write audit 已完成 |
| [Multi-Turn Reasoning When Context Arrives in Pieces: Scalable Sharding and Memory-Augmented RL](https://arxiv.org/html/2606.12941v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《Multi-Turn Reasoning When Context Arrives in Pieces: Scalable Sharding and Memory-Augmented RL》关闭或降池；完整摘要显示“To make such training scalable, we introduce a low-cost sharding pipeline that converts single-turn QA datasets into multi-turn fragmented-information episodes, eliminating the need for hours of manual annotation.”。该增量直接改变 AGENT-MEMORY 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：AGENT-MEMORY，[owner](../../../../books/part-07-agent/77-memory.md)；正文锚点：Consolidation 与 Forgetting |
| [Learning What to Remember: A Cognitively Grounded Multi-Factor Value Model for Agentic Memory](https://arxiv.org/html/2606.12945v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《Learning What to Remember: A Cognitively Grounded Multi-Factor Value Model for Agentic Memory》关闭或降池；完整摘要显示“We propose a multi-factor memory value function V(m)=\sum_i w_i f_i(m) over seven interpretable factors (emotional intensity, goal relevance, value alignment, self/user relevance, task utility, reliability, and usage history) drawn from cognitive psychology, whose weights are learned from a downstream objective by a gradient-free optimiser, and whose single scalar uniformly controls encoding depth, forget risk, and retrieval rank.”。该增量直接改变 AGENT-MEMORY 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：AGENT-MEMORY，[owner](../../../../books/part-07-agent/77-memory.md)；正文锚点：Consolidation 与 Forgetting |
| [Maestro: Workload-Aware Cross-Cluster Scheduling for LLM-Based Multi-Agent Systems](https://arxiv.org/pdf/2606.12950v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“We present Maestro, a workload-aware scheduling system designed for LLM-MAS serving under strict GPU budgets.”，该机制在 INFER-SCHEDULING 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：INFER-SCHEDULING，[owner](../../../../books/part-05-inference-system/56-inference-scheduling.md)；正文锚点：Model Routing 与 Test-time Scaling 必须结算同一个 Budget |
| [ScaleAcross: Designing Multi-Data-Center Infrastructure for Geo-Distributed AI Training](https://arxiv.org/html/2606.12963v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《ScaleAcross: Designing Multi-Data-Center Infrastructure for Geo-Distributed AI Training》关闭或降池；完整摘要显示“Such deployments introduce system-level challenges arising from synchronization-intensive communication, cross-site data exchange, and wide-area latency constraints.”。该增量直接改变 TRAIN-DISTRIBUTED-TRAINING 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：TRAIN-DISTRIBUTED-TRAINING，[owner](../../../../books/part-04-training-system/36-distributed-training.md)；正文锚点：跨地域电力约束会把全局同步改成层级且有陈旧度的聚合 |
| [Trajectory-Level Redirection Attacks on Vision-Language-Action Models](https://arxiv.org/pdf/2606.12978v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“To find such prompts, we introduce an on-policy prompt search method that uses rollouts to discover perturbations whose closed-loop behavior tracks a target task while satisfying the command-preserving constraints.”，该机制在 MULTIMODAL-EMBODIED-VLA 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：MULTIMODAL-EMBODIED-VLA，[owner](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；正文锚点：Training-only Foresight 不是 Persistent World State |
| [The Illusion of Multi-Agent Advantage](https://arxiv.org/pdf/2606.13003v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“To isolate these failures from limitations inherent to task structure, we introduce a diagnostic synthetic dataset tailored for MAS featuring explicit task decomposition, context separation and parallelization potential.”，该机制在 AGENT-MULTI-AGENT 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：AGENT-MULTI-AGENT，[owner](../../../../books/part-07-agent/82-multi-agent.md)；正文锚点：Message 不是 State |
| [EA-WM: Event-Aware World Models with Task-Specification Grounding for Long-Horizon Manipulation](https://arxiv.org/pdf/2606.13053v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“We introduce EA-WM, an event-aware world-model framework that augments frozen visual-feature dynamics with task-specification-grounded event prediction and verification.”，该机制在 MULTIMODAL-WORLD-MODELS 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 Identity correction：raw inventory 题名《EV-WM: Event-Verified World Models for Long-Horizon Robotic Manipulation》不是 v1 authority；官方 exact-v1 题名为《EA-WM: Event-Aware World Models with Task-Specification Grounding for Long-Horizon Manipulation》，Evidence 只按 v1 复验。 | 标准完成 | 已有覆盖：MULTIMODAL-WORLD-MODELS，[owner](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)；正文锚点：从平均预测误差到分层的 Rollout Admission |
| [The Emergence of Autonomous Penetration Capabilities in Large Language Model-Powered AI Systems](https://arxiv.org/html/2606.13079v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《The Emergence of Autonomous Penetration Capabilities in Large Language Model-Powered AI Systems》关闭或降池；完整摘要显示“Within this broader red-line scenario, autonomous penetration represents a core enabling capability and subtask: the ability of LLM-powered AI systems to independently conduct adversarial operations against a target server without human intervention, identify and exploit vulnerabilities, and obtain unauthorized access or control.”。该增量直接改变 PLATFORM-EVALUATION-SYSTEM 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；正文锚点：Evaluation Identity 必须包含 Harness 与 Environment |
| [Scale Buys Interpolation, Structure Buys a Horizon: Certified Predictability for Equivariant World Models](https://arxiv.org/pdf/2606.13092v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“A world model's average error says nothing about whether a particular prediction can be trusted, or for how long.”，该机制在 MULTIMODAL-WORLD-MODELS 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 Identity correction：raw inventory 题名《Certified World Models: Predictability Across Configuration, Horizon, and Resolution》不是 v1 authority；官方 exact-v1 题名为《Scale Buys Interpolation, Structure Buys a Horizon: Certified Predictability for Equivariant World Models》，Evidence 只按 v1 复验。 | 标准完成 | 已有覆盖：MULTIMODAL-WORLD-MODELS，[owner](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)；正文锚点：从平均预测误差到分层的 Rollout Admission |
| [G-Long: Graph-Enhanced Memory Management for Efficient Long-Term Dialogue Agents](https://arxiv.org/html/2606.13115v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《G-Long: Graph-Enhanced Memory Management for Efficient Long-Term Dialogue Agents》关闭或降池；完整摘要显示“To address these limitations, we propose G-Long, a graph-enhanced framework that utilizes a fine-tuned small Language Model (sLM) for structured triplet extraction and associative retrieval, significantly reducing operational costs.”。该增量直接改变 AGENT-MEMORY 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：AGENT-MEMORY，[owner](../../../../books/part-07-agent/77-memory.md)；正文锚点：Consolidation 与 Forgetting |
| [EvoBrowseComp: Benchmarking Search Agents on Evolving Knowledge](https://arxiv.org/html/2606.13120v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《EvoBrowseComp: Benchmarking Search Agents on Evolving Knowledge》关闭或降池；完整摘要显示“In this paper, we introduce EvoBrowseComp, an evolving benchmark of 400 English and 400 Chinese contamination-free complex questions synthesized via live-web traversal.”。该增量直接改变 PLATFORM-EVALUATION-SYSTEM 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；正文锚点：Evaluation Identity 必须包含 Harness 与 Environment |
| [MiniPIC: Flexible Position-Independent Caching in <100LOC](https://arxiv.org/html/2606.13126v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《MiniPIC: Flexible Position-Independent Caching in <100LOC》关闭或降池；完整摘要显示“We present Minimalistic PIC (MiniPIC): a minimal, flexible and fast vLLM design built from two ingredients: positional-encoding-free KV cache and user-controlled cache-reuse primitives.”。该增量直接改变 INFER-KV-CACHE 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：INFER-KV-CACHE，[owner](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)；正文锚点：任意 Chunk 复用必须先修复 Position 与 Conditioning Seam |
| [Iterative Visual Thinking and the Self-Correction Mirage in VLM Grounding](https://arxiv.org/html/2606.13156v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《Iterative Visual Thinking and the Self-Correction Mirage in VLM Grounding》关闭或降池；完整摘要显示“A natural way to bring this to spatial grounding is visual self-correction: the model predicts a bounding box, sees it rendered on the image, and refines it over several steps.”。该增量直接改变 PLATFORM-EVALUATION-SYSTEM 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；正文锚点：Evaluation Identity 必须包含 Harness 与 Environment |
| [Getting Better at Working With You: Compiling User Corrections into Runtime Enforcement for Coding Agents](https://arxiv.org/pdf/2606.13174v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“We introduce Test-time Rule Acquisition and Compiled Enforcement (TRACE), a drop-in skill-layer pipeline for coding-agent runtimes that mines user corrections, rewrites them as atomic rules, and compiles them into runtime checks that must pass before an agent completes future tasks.”，该机制在 AGENT-WORKFLOW 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：AGENT-WORKFLOW，[owner](../../../../books/part-07-agent/81-workflow.md)；正文锚点：State Machine 是基本模型 |
| [MemRefine: LLM-Guided Compression for Long-Term Agent Memory](https://arxiv.org/html/2606.13177v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《MemRefine: LLM-Guided Compression for Long-Term Agent Memory》关闭或降池；完整摘要显示“However, as interactions accumulate, the memory store grows without bound and fills with redundant entries that inflate storage cost and degrade retrieval by crowding out the most useful evidence.”。该增量直接改变 AGENT-MEMORY 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：AGENT-MEMORY，[owner](../../../../books/part-07-agent/77-memory.md)；正文锚点：Consolidation 与 Forgetting |
| [LLM-as-an-Investigator: Evidence-First Reasoning for Robust Interactive Problem Diagnosis](https://arxiv.org/html/2606.13220v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《LLM-as-an-Investigator: Evidence-First Reasoning for Robust Interactive Problem Diagnosis》关闭或降池；完整摘要显示“However, when users provide incomplete descriptions or plausible but unverified explanations, LLMs may prematurely align with these assumptions and propose solutions before collecting sufficient evidence.”。该增量直接改变 AGENT-PLANNING 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：AGENT-PLANNING，[owner](../../../../books/part-07-agent/79-planning.md)；正文锚点：从目标到状态图 |
| [From Uncertain Judgments to Calibrated Rankings: Conformal Elo Estimation for LLM Evaluation](https://arxiv.org/html/2606.13221v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 3 + 2 + 3 = 8；原筛选把《From Uncertain Judgments to Calibrated Rankings: Conformal Elo Estimation for LLM Evaluation》关闭或降池；完整摘要显示“LLM-as-a-judge offers a cheaper alternative, but judge scores carry systematic errors - such as position bias, self-preference, or intransitivity - that can strongly miscalibrate the resulting rankings.”。该增量直接改变 PLATFORM-EVALUATION-SYSTEM 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；正文写入与独立 post-write audit 已完成 |
| [SkillCAT: Contrastive, Assessment-Augmented and Topology-AwareSkill Self-Evolution for LLM Agents](https://arxiv.org/html/2606.13317v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《SkillCAT: Contrastive, Assessment-Augmented and Topology-AwareSkill Self-Evolution for LLM Agents》关闭或降池；完整摘要显示“We propose SkillCAT, a framework that decomposes this process into three stages. (1) Contrastive Causal Extraction (CCE) samples multiple trajectories per task and contrasts same-task success/failure pairs to find the evidence that explains outcome differences. (2) Assessment-Augmented Evolution (AAE) replays each candidate patch on source-task clones, retains only those that do not damage task outcomes, and then merges the retained patches hierarchically. (3) Topology-Aware Task Execution (TTE) compiles the evolved skills into routable sub-skill topologies, so that inference loads only task-relevant capability nodes.”。该增量直接改变 AGENT-WORKFLOW 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：AGENT-WORKFLOW，[owner](../../../../books/part-07-agent/81-workflow.md)；正文锚点：Trial Evidence 不能直接提交为 Workflow Revision |
| [Can I Buy Your KV Cache?](https://arxiv.org/html/2606.13361v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 1 + 2 = 5；原筛选把《Can I Buy Your KV Cache?》关闭或降池；完整摘要显示“Every agent re-runs prefill, the most compute-intensive step a large model takes, over identical text, only to rebuild a key-value (KV) cache identical to the one the agent before it just built.”。该增量直接改变 INFER-PREFILL 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 仅报告：INFER-PREFILL；exact-v1 尚不足以授权长期 Books 正文变化 |
| [Who Pays the Price? Stakeholder-Centric Prompt Injection Benchmarking for Real-world Web Agents](https://arxiv.org/html/2606.13385v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《Who Pays the Price? Stakeholder-Centric Prompt Injection Benchmarking for Real-world Web Agents》关闭或降池；完整摘要显示“To capture these properties, we introduce StakeBench, a stakeholder-centric benchmark that systematically categorizes and attributes harm in real-world web agent systems for online shopping.”。该增量直接改变 PLATFORM-SECURITY 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；正文锚点：从资产与信任边界开始 |
| [MiniMax Sparse Attention](https://arxiv.org/pdf/2606.13392v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“We introduce MiniMax Sparse Attention (MSA), a blockwise sparse attention built upon Grouped Query Attention (GQA).”，该机制在 MODEL-LONG-CONTEXT 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：MODEL-LONG-CONTEXT，[owner](../../../../books/part-02-model/22-long-context.md)；正文锚点：方案究竟移动了哪个瓶颈 |
| [Accelerating Speculative Diffusions via Block Verification](https://arxiv.org/pdf/2606.13426v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“In this work, we introduce a novel scheme that efficiently implements the original speculative sampling mechanism for diffusion models.”，该机制在 MULTIMODAL-GENERATIVE-PARADIGMS 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：MULTIMODAL-GENERATIVE-PARADIGMS，[owner](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；正文锚点：Draft、Verify 与 Correct 不是同一件事 |
| [CQC-RAG: Robust Retrieval-Augmented Generation via Cross-Query Consistency](https://arxiv.org/html/2606.13438v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《CQC-RAG: Robust Retrieval-Augmented Generation via Cross-Query Consistency》关闭或降池；完整摘要显示“To address these limitations, we propose a Cross-Query Consistency Hypothesis: correct answers tend to maintain high confidence across semantically equivalent but syntactically diverse queries, whereas noise-induced hallucinations exhibit unstable confidence under such query variations.”。该增量直接改变 AGENT-RAG 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：AGENT-RAG，[owner](../../../../books/part-07-agent/76-rag.md)；正文锚点：Online Retrieval Pipeline |
| [Toward Instructions-as-Code: Understanding the Impact of Instruction Files on Agentic Pull Requests](https://arxiv.org/pdf/2606.13449v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“For better agent efficiency, developers create instruction files that guide the AI-agents, including how to navigate the project, locate the right components, run tests, respect best practices, and more.”，该机制在 AGENT-PROMPT 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：AGENT-PROMPT，[owner](../../../../books/part-07-agent/74-prompt.md)；正文锚点：Prompt 生命周期 |
| [Budget-Constrained Step-Level Diffusion Caching](https://arxiv.org/pdf/2606.13496v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“In this work, we propose BudCache, which inverts this formulation: rather than letting per-step error thresholds dictate the runtime cost, we fix the compute budget in advance and search for the cache policy that best preserves the final output.”，该机制在 MULTIMODAL-GENERATIVE-PARADIGMS 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：MULTIMODAL-GENERATIVE-PARADIGMS，[owner](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；正文锚点：Draft、Verify 与 Correct 不是同一件事 |
| [GF-DiT: Scheduling Parallelism for Diffusion Transformer Serving](https://arxiv.org/pdf/2606.13501v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“We present GF-DiT, a policy-programmable runtime for elastic DiT serving that dynamically adapts the parallelism of running requests according to workload demands and service objectives.”，该机制在 INFER-SCHEDULING 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：INFER-SCHEDULING，[owner](../../../../books/part-05-inference-system/56-inference-scheduling.md)；正文锚点：迭代生成与流式会话需要显式 Progress State |
| [Multiagent Protocols with Aggregated Confidence Signals](https://arxiv.org/html/2606.13591v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《Multiagent Protocols with Aggregated Confidence Signals》关闭或降池；完整摘要显示“We introduce three protocols that produce a final answer along with a single aggregated confidence by first transforming raw confidence signals to make them comparable across models, then combining them via soft voting or a probability fusion we call Bayesian fusion.”。该增量直接改变 AGENT-MULTI-AGENT 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：AGENT-MULTI-AGENT，[owner](../../../../books/part-07-agent/82-multi-agent.md)；正文锚点：Message 不是 State |
| [See What I See, Know What I Think: Dense Latent Communication Across Heterogeneous Agents](https://arxiv.org/html/2606.13594v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 3 + 2 + 3 = 8；原筛选把《See What I See, Know What I Think: Dense Latent Communication Across Heterogeneous Agents》关闭或降池；完整摘要显示“Motivated by this, we propose dense alignment for heterogeneous KV-cache communication via a lightweight cross-model cache transformation and two-phase training: reconstruction followed by generation.”。该增量直接改变 AGENT-MULTI-AGENT 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 深入完成 | 整合：AGENT-MULTI-AGENT，[owner](../../../../books/part-07-agent/82-multi-agent.md)；正文写入与独立 post-write audit 已完成 |
| [Reward Modeling for Multi-Agent Orchestration](https://arxiv.org/html/2606.13598v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；完整摘要确认其研究 multi-agent orchestration reward modeling，属于 LLM multi-agent 范围，因此保留 Candidate。 | 标准完成 | 已有覆盖：AGENT-MULTI-AGENT，[owner](../../../../books/part-07-agent/82-multi-agent.md)；现有 dynamic topology、credit、critical-path reward 与 role obligation 已覆盖该局部训练配方。 |
| [AgentBeats: Agentifying Agent Assessment for Openness, Standardization, and Reproducibility](https://arxiv.org/pdf/2606.13608v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“Most benchmarks rely on fixed, LLM-centric harnesses that require heavy integration, create test-production mismatch, and limit fair comparison across diverse agent designs.”，该机制在 PLATFORM-EVALUATION-SYSTEM 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；正文锚点：Evaluation Identity 必须包含 Harness 与 Environment |
| [One Polluted Page Is Enough: Evaluating Web Content Pollution in LLM Recommenders](https://arxiv.org/pdf/2606.13610v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《One Polluted Page Is Enough: Evaluating Web Content Pollution in LLM Recommenders》关闭或降池；完整摘要显示“We introduce FORGE (Fake Online Recommendations in Generative Environments), which locally rewrites real products in a frozen set of retrieved web pages into fake ones and measures how often the LLM recommends the fake product, across 225 real products in 15 categories and 5 consumer scenarios.”。该增量直接改变 PLATFORM-SECURITY 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；正文锚点：从资产与信任边界开始 |
| [Valid Inference with Synthetic Data via Task Exchangeability](https://arxiv.org/html/2606.13629v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 3 + 2 + 3 = 8；原筛选把《Valid Inference with Synthetic Data via Task Exchangeability》关闭或降池；完整摘要显示“In this work, we propose statistical principles for using synthetic data in scientific research with provable validity guarantees.”。该增量直接改变 PLATFORM-EVALUATION-SYSTEM 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；正文写入与独立 post-write audit 已完成 |
| [Recursive Agent Harnesses](https://arxiv.org/pdf/2606.13643v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“We name and study the pattern between these two lines of work, where the recursive unit is a full agent harness with filesystem tools, code execution, and planning rather than a model call with no tools.”，该机制在 AGENT-WORKFLOW 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：AGENT-WORKFLOW，[owner](../../../../books/part-07-agent/81-workflow.md)；正文锚点：State Machine 是基本模型 |
| [HyperTool: Beyond Step-Wise Tool Calls for Tool-Augmented Agents](https://arxiv.org/pdf/2606.13663v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“We introduce \textbf{HyperTool}, a unified executable MCP-style tool interface that changes the model-visible unit of tool execution.”，该机制在 AGENT-TOOL-CALLING 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：AGENT-TOOL-CALLING，[owner](../../../../books/part-07-agent/78-tool-calling.md)；正文锚点：Tool Contract |
| [EvoArena: Tracking Memory Evolution for Robust LLM Agents in Dynamic Environments](https://arxiv.org/pdf/2606.13681v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“To address this gap, we introduce EvoArena, a benchmark suite that models environment changes as sequences of progressive updates across terminal, software, and social domains.”，该机制在 AGENT-MEMORY 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：AGENT-MEMORY，[owner](../../../../books/part-07-agent/77-memory.md)；正文锚点：Consolidation 与 Forgetting |

## 4. 证据与知识整合

### [Soft-Prompt Tuning for Fair and Efficient LLM Benchmark Evaluation](https://arxiv.org/html/2606.12117v1)

本轮作者已读exact-v1 §3–4及A.9，必要证据与唯一稿见[首批证据](../_sources/daily-20260612/SUP_NECESSARY_B1_20261026.md#12117--soft-prompt-tuning-for-fair-and-efficient-llm-benchmark-evaluation)。小预算soft-prompt是训练干预；格式、内容与选项likelihood分责，但开放题judge不能完全分离，soft-prompted post-trained reference亦不是真实知识oracle。root已实际必要/actual owner/PRE通过；作者在Ch66指定位置真实SAVE两段及本人注并完整自读邻接，root[唯一实际POST §4通过](../_sources/daily-20260612/SUP_REVIEW_20261026.md#4-12117--11722-唯一实际-post-通过)。本项整合完成，不代整日验收。

### [ICA Lens: Interpreting Language Models Without Training Another Dictionary](https://arxiv.org/html/2606.11722v1)

本轮作者已读exact-v1 §3/6/9，见[首批证据](../_sources/daily-20260612/SUP_NECESSARY_B1_20261026.md#11722--ica-lens-interpreting-language-models-without-training-another-dictionary)。非高斯compact basis的读取与pseudoinverse回写不同，p95 fallback保不稳尾部；匹配probe预算与splits不等完整行为因果，大N时SAE可更好。作者在Ch5指定肩部真实SAVE两段及本人注并完整自读，root[唯一实际POST §4通过](../_sources/daily-20260612/SUP_REVIEW_20261026.md#4-12117--11722-唯一实际-post-通过)，这是exact-v1实际历史检查。

后续补齐[current事件标记](../_sources/daily-20260612/SUP_CURRENT_EVENT_MARKERS_20261026.md)发现v2明确“substantially revised/comprehensive re-evaluation”；作者依root窄授完成[受影响采用层首次必要](../_sources/daily-20260612/SUP_NECESSARY_B1_20261026.md#11722-current-v2仅受影响采用层定点恢复)。v2改变raw-norm预处理、50iter/population-v-component稳定性与probe/TPP feature身份，并非仅扩模型；未明确宣布v1数据错误/撤回，不能判全v1无效，也不拼跨版预算排名。root§27实际原件/actual owner/PRE通过，作者仅替原第二段与本人注、保第一段，root唯一§30实际POST恢复关闭。v2提交原字段换算为Oct20 BJT，只是窗外revision恢复线索，不等已核公开日、不自行授其他Daily owner，不改Jun11归属或重复评分；不采用新版性能/全模型行为保证，未核实现/复现。

### [Learning What to Say to Your VLA: Mostly Harmless Vision Language Action Model Steering](https://arxiv.org/html/2606.12299v1)

本轮作者已深入读exact-v1 §4–6/App7.2，见[首批证据](../_sources/daily-20260612/SUP_NECESSARY_B1_20261026.md#12299--learning-what-to-say-to-your-vla)。采用的最小命题为语言反馈policy、是否切换的improvement head与controller分责；有限有害类校准不授任意OOD无害。原公式以score≥harmful分位数执行而未说明ties，九个有害校准score及test score全0、alpha=.1即给出FPR1反例；该争议严格隔离于数学保证，不否认作者局部经验结果。actual owner为MULTIMODAL-EMBODIED-VLA；作者在Ch26指定肩部真实SAVE并自读，root[唯一实际POST §7通过](../_sources/daily-20260612/SUP_REVIEW_20261026.md#7-12299--12366-唯一实际-post-通过)，仅整合受限接口与经验取舍。

### [APT: Action Expert Pretraining Improves Instruction Generalization of Vision-Language-Action Policies](https://arxiv.org/html/2606.12366v1)

本轮作者已读exact-v1 §3–4/E.6，见[首批证据](../_sources/daily-20260612/SUP_NECESSARY_B1_20261026.md#12366--apt)。先训练VA动作prior再注语言的初始化分支不等永久梯度隔离；stage2会联合更新，Bayesian factorization非实际独立证明。Goal-Pos反退、数据/结构混杂和push-after-grasp/跳过关盒直接反侧保留；actual owner为MULTIMODAL-EMBODIED-VLA，作者在Ch26指定位置真实SAVE并自读，root[唯一实际POST §7通过](../_sources/daily-20260612/SUP_REVIEW_20261026.md#7-12299--12366-唯一实际-post-通过)。

### [Teaching Diffusion to Speculate Left-to-Right](https://arxiv.org/html/2606.11552v1)

作者必要读exact-v1 §4–6.5，[具体证据与actual owner](../_sources/daily-20260612/SUP_NECESSARY_B2_20261026.md#11552--teaching-diffusion-to-speculate-left-to-right)。三种drafter loss控制位置衰减、argmax-gold首错和prefix marginal乘积，后者不是任意随机p/q verifier的真实接受概率。target-regenerated语料本身的uniform CE收益及训练/checkpoint差异不能混归loss；K超训练范围、系数与下游反侧保留。Ch48已有expected-prefix survival/continuation、只改drafter loss不改accept/commit及target语料baseline分账，新增首错auxiliary留作受限recipe；root[§9具体已有覆盖通过](../_sources/daily-20260612/SUP_REVIEW_20261026.md)，不为制造diff改书。未核代码/复现。

### [Reroute, Don't Remove](https://arxiv.org/html/2606.12412v1)

作者必要读exact-v1 §4–5/Tables1–4、A.3–A.4/B.1–B.2，[限定证据/owner/唯一稿](../_sources/daily-20260612/SUP_NECESSARY_B2_20261026.md#12412--reroute-dont-remove)。保留原hidden的identity旁路与后层fullpool重入，不是恢复已删信息；keep-index pruning、更早route/schedule、额外TFLOPs/KV及无wallclock保证分开。原Table4百分比口径不一致，不沿用为新增性能数。Ch23 DocPrune与merge恢复网格之间已真实保存两段，root[唯一POST §12通过](../_sources/daily-20260612/SUP_REVIEW_20261026.md#12-12412-唯一实际-post-通过)；未核代码/复现。

### [Redesign MoE Routers with Manifold Power Iteration](https://arxiv.org/html/2606.12397v1)

作者必要读exact-v1 §3–6/直接消融，[证据与唯一稿](../_sources/daily-20260612/SUP_NECESSARY_B2_20261026.md#12397--redesign-moe-routers-with-manifold-power-iteration)。仅采用expert Gram作用+norm retraction的router耦合，固定矩阵/局部小更新不授moving expert精确收敛，Fig1 shape/transpose和拼接式不闭，不默补literal实现。normalize-only、10iter降质增费与11B MBPP反退、固定权重折叠的适用边界保留。root §13实际必要/actual Ch21/两段PRE通过，作者已真实SAVE指定肩部与trueH2注并读回完整两侧，root[唯一实际POST §14通过](../_sources/daily-20260612/SUP_REVIEW_20261026.md#14-12397-唯一实际-post-通过)；未核代码/复现，不预签DAY。

### [On The Effectiveness-Fluency Trade-Off In LLM Conditioning: A Systematic Study](https://arxiv.org/html/2606.12234v1)

作者实际采用root[§15首次必要包](../_sources/daily-20260612/SUP_REVIEW_20261026.md#15-12234-一次必要首备交作者接-actual-owner)，不第二Methods；[actual owner与唯一稿](../_sources/daily-20260612/SUP_NECESSARY_B2_20261026.md#12234--必要首备直接采用非第二methods)另由作者完成。外部PPL低重复/高复杂风格的双向混杂、judge把复述prompt误作IF与guardrail缺分保留；48模型×干预组合均值相关非逐样本校准，不授TTR真值、base/IT的alignment因果或异人口SFT/steering匹配预算排名。Ch66已真实SAVE，root唯一POST §20通过；未核代码/复现。

### [Fast Speech Foundation Model Distillation Using Interleaved Stacking](https://arxiv.org/html/2606.11766v1)

作者实际读exact-v1 §3/4.1–4.4，[必要证据/owner/唯一稿](../_sources/daily-20260612/SUP_NECESSARY_B2_20261026.md#11766--fast-speech-foundation-model-distillation-using-interleaved-stacking)。每阶段均匀复制并紧插原层，固定teacher锚而更新student受监督索引；不是函数恒等或层语义因果，Full-L2L/任务/schedule反侧保留，不由训练表局部速度授净成本/推理收益。Ch29共享projector段后已真实SAVE，root必要/PRE §17及唯一POST §20通过；未核代码/复现。

### [A Fast Locality Simulator for GEMM Design-Space Exploration on Multi-Chiplet GPUs](https://arxiv.org/html/2606.11716v1)

作者实际读exact-v1 II–IV，[必要证据/owner/唯一稿](../_sources/daily-20260612/SUP_NECESSARY_B2_20261026.md#11716--a-fast-locality-simulator-for-gemm-design-space-exploration-on-multi-chiplet-gpus)。固定RR placement下CTA traversal仍可经private L2改变remote bytes，shape-neutral和坏layout反退保留；MI300X-like/lockstep functional模型不是硬件timing或能耗，CPU模拟器用时不当GPU速度。Ch54 Chiplet段已真实SAVE，root必要/PRE §18及唯一POST §20通过；未核代码/复现。

### [Holding the FP8 Quality Ceiling at 8-Bit Weights and Activations: INT8 and GGUF Post-Training Quantization of Ideogram 4.0 for Consumer GPUs](https://arxiv.org/html/2606.12280v1)

作者实际读exact-v1 §3–7/Tables1–3，[具体证据与actual Ch49覆盖](../_sources/daily-20260612/SUP_NECESSARY_B2_20261026.md#12280--holding-the-fp8-quality-ceiling)。采用same-seed质量-v-reference分责、FFN保护局部消融与无fused INT8 kernel不加速；参考是FP8不是BF16，200prompt单seed/bootstrap不证明等价，保护N从评价50子集选择有重叠。OCR近零地板、CLIP家族judge与Q4_K更高standalone分但更偏reference皆不授文字高质量/通用consumer优势。Ch49已有敏感层干预、校准人口与物理kernel/逐例质量验收，root §19具体已有覆盖通过，不改书；未核代码/复现。

### [Attention by Synchronization in Coupled Oscillator Networks](https://arxiv.org/html/2606.12059v1)

实际必要§2/3 Theorem2与直接退化条件/§4.1–4.4/5，见[证据、actual Ch14与原两段稿](../_sources/daily-20260612/SUP_NECESSARY_B2_20261026.md#12059--attention-by-synchronization-in-coupled-oscillator-networks)。仅固定anchor、非零h且非反极初值的理想等衡；正coupling能相消，有限窗口未全部收敛，语言仍逊softmax，无高维硬件/实机能耗支持。root §22实际必要/owner/PRE通过，原两段及trueH2注已真实SAVE并完整自读，root唯一§25实际POST通过/窄位释放；不预日级验收。

### [CORE-Bench](https://arxiv.org/html/2606.11864v1)

实际必要§3/4与Limitations，见[证据、actual Ch76与原两段稿](../_sources/daily-20260612/SUP_NECESSARY_B2_20261026.md#11864--core-bench)。pre-PR状态过滤、edit与support两目标差额可采用；跨级corpus/query/标签密度共变不授单因素因果，agent/ensemble与allowlist不证标签完备或patch正确。root §23实际必要/owner/PRE通过，原两段及trueH2注已真实SAVE并完整自读，root唯一§25实际POST通过/窄位释放；未核代码/复现。

### [Higher-Order Token Interactions via Quantum Attention](https://arxiv.org/html/2606.11673v1)

实际必要§3–5/7与B.1–B.4，见[中心保证争议与有限实验](../_sources/daily-20260612/SUP_NECESSARY_B2_20261026.md#11673--higher-order-token-interactions-via-quantum-attention中心保证争议)。经典Match_k存在匹配族下界不直接约束构造的fixed-support monomial，需明确桥；generalization上界变宽不证明失败下界；basis-loading witness与训练reupload encoder不同。局部2design/浅层/局部cost的梯度条件不授all-to-all RZZ；后者实测gradient退化、ring高阶能力与butterfly有限拟合反侧均保留，不宣告所有量子构造或有限实验无效。root §24独立实际核争议、actual Ch15/Ch14采用边界通过，原6保持，中心保证H/Books暂缓安全隔离。重开仅需同一函数族reduction、正确学习结论和一致encoder或明确收窄定理，不无限检索全部引用。

### [Bridging the Morphology Gap: Adapting VLA Models to Dexterous Manipulation via Intent-Conditioned Fine-Tuning](https://arxiv.org/html/2606.12109v1)

实际必要§3/4/5，见[InDex证据与反侧](../_sources/daily-20260612/SUP_NECESSARY_B2_20261026.md#12109--index)。先适配action expert输出粗关节，经FK压aperture为γ，再固定VLA另训dex diffusion head；不采“上层直接只吐scalar”或γ是真实意图/接触充分状态。四任务各100成功示教/100评测仅仿真；基线表间不拼唯一因果，conditional grasp分母、紧装配停滞、所有标定/训练/推理与回归费用保留。root§28必要/actual owner/PRE，作者Ch26 binding后原两段SAVE，root唯一§30实际POST通过；未核代码/复现，不授实机安全。

### [Kuramoto Attention: Synchronizing Self-Attention on the Torus](https://arxiv.org/html/2606.11585v1)

实际必要§2–4/Table1–2，见[受限torus证据](../_sources/daily-20260612/SUP_NECESSARY_B2_20261026.md#11585--kuramoto-attention-synchronizing-self-attention-on-the-torus)。只有raw phasor identity-values的圆周均值切向更新有正弦耦合恒等；signed gate可排斥，dense gates与FFN仍跨坐标。fixed-A局部方向不授完整state-dependent能量下降，raw-angle FFN亦非严格torus函数。小字符任务五seed/匹配参数非同算力，1M及5M均值/方差反侧和全费保留，无速度优势。root§29必要/actual owner/PRE，作者Ch14 signed归一后原两段SAVE，root唯一§30实际POST通过；未核实现/复现。

### [VOID: Defeating Unauthorized Mimicry in Latent Diffusion Models](https://arxiv.org/html/2606.12263v1)

实际必要§3–5/6.1/6.6–6.7/7.2/Ethics/AppD，见[完整限定证据](../_sources/daily-20260612/SUP_NECESSARY_B2_20261026.md#12263--void)。发布图像的微扰只在受限surrogate优化VAE不确定性与噪声差离散代理；std零容非零常量，不授guidance必零或不可移除噪声。Table10保护/transfer/utility有取舍，完整VAE/UNet适应明确削弱保护；特定高费用非未来安全下界，无human-subject不可见证明。root§31必要/owner/PRE，作者Ch72 WAF后原两段真实SAVE，root唯一§34实际POST通过；全费/合法用途与consent边界在正文，未核代码/复现。

### [DrivingAgent: Design and Scheduling Agents for Autonomous Driving Systems](https://arxiv.org/html/2606.12236v1)

实际必要§3–5/Table1–2，见[时间接口与反侧](../_sources/daily-20260612/SUP_NECESSARY_B2_20261026.md#12236--drivingagent)。profile经离线检查/probe/训练gate，运行LLM仅提计划；sensor event-time、cache有效性及future-frame activation由确定性逐帧路径核验。compute FPS未计加载/端口通信，dense稳定性非单调、全配置仍逊部分确定性对照，不由仿真/平均吞吐授实车deadline或安全。root§32必要/owner/PRE，作者Ch84 Nalar后原两段真实SAVE，root唯一§35实际POST通过；未核代码/复现。

### [MultiToP: Learning to Patch Visual Tokens to Mitigate Hallucinations in Video Large Multimodal Models](https://arxiv.org/html/2606.11792v1)

实际必要§3–4/AppA及直接B1–B2，见[patch接口证据](../_sources/daily-20260612/SUP_NECESSARY_B2_20261026.md#11792--multitop)。冻结consumer、same-count共享patch替换与训练答案attention rank分责；部署无gold/teacher图，比例平方罚非hard budget。No-rank仍优vanilla、强约束/部分理解与适配切片反退，DeepStack需额外merge-group兼容；每生成token近似延迟不签全请求SLO。root§33必要/owner/PRE，作者Ch23 recoverable routing后原两段真实SAVE，root唯一§35实际POST通过；未核代码/复现。

### [World Pilot: Steering Vision-Language-Action Models with World-Action Priors](https://arxiv.org/html/2606.12403v1)

实际必要§3–5/Table1–6，见[两类prior与直接反侧](../_sources/daily-20260612/SUP_NECESSARY_B2_20261026.md#12403--world-pilot)。冻结WAM仍在线额外forward，latent residual与trajectory single-prefix不同于pixel/flow初始化；VLA/fusion仍训练。部分本体/布局、原任务与RoboCasa反退，真机四任务每setting20trials、混合baseline人口不授普遍优势；WAM覆盖外两prior会一起失准，全部训练/在线与回归费用保留。root§36必要/owner/PRE，作者原稿SAVE，root唯一§39实际POST通过；未核代码/复现，不授真实未来或控制安全。

### [UniIntervene: Agentic Intervention for Efficient Real-World Reinforcement Learning](https://arxiv.org/html/2606.12372v1)

实际必要§3/4/6及直接AppB/C1/D–H，见[proxy、memory与恢复证据](../_sources/daily-20260612/SUP_NECESSARY_B2_20261026.md#12372--uniintervene)。成功轨迹时间/失败0标签只是proxy，不是真实风险；过去高proxy endpoint不证明当前可达。No-memory几乎不变offline F1却降在线SR，IR是人工接管step比、仍有人控；81→88为7pp而非8.6pp。阈值/记数recipe不闭不照抄，原精确版本封面/月日差不迁归属，全部费用与支持边界保留。root§37必要/owner/PRE，作者原稿SAVE，root唯一§39实际POST通过；未核代码/复现。

### [Ambient Diffusion Policy: Imitation Learning from Suboptimal Data in Robotics](https://arxiv.org/html/2606.12365v1)

实际必要§3–9限定理论/数据采样/评价及AppD/F，见[time-dependent数据资格](../_sources/daily-20260612/SUP_NECESSARY_B2_20261026.md#12365--ambient-diffusion-policy)。P全time、Q只支持的高/低噪time与全局weight/filter不同，推理sampler不改。Gaussian/谱拟合不授真实条件分布同一，观察shift未解；§7.4 tmin0与§6 union不闭，不采用完整literal recipe。更足target时low-noise可无益/反退，tower相对高度非通用SR，best checkpoint/trial区间非训练seed保证且更多Q训练计全费。root§38必要/owner/PRE，作者原稿SAVE，root唯一§39实际POST通过；未核代码/复现，不授物理安全。

### [Path convergence in diffusion models](https://arxiv.org/html/2606.12161v1)

采用exact-v1的同起点/噪声的有限经验diffusion路径耦合与metric边界。Gaussian bridge含起点分母；一维median尺度不证L2/高维速率，固定τ排序/小步外推仍可能overshoot，非通用已训练sampler。 完整必要位置/直接反侧及actual owner见[B3本项](../_sources/daily-20260612/SUP_NECESSARY_B3_20261026.md#12161--path-convergence-in-diffusion-models)；唯一稿真实SAVE后经非作者§44实际POST通过，不代表日级完成，未核代码/复现。

### [DAM-VLA: Decoupled Asynchronous Multimodal Vision Language Action model](https://arxiv.org/html/2606.12105v1)

采用exact-v1的各模态history/buffer与action clock分责，100Hz不等replan。训练仍100Hz对齐，主replan约5.5Hz；vision/action实际微调，async alone低于X25，不能独归异步或授真机安全。 完整必要位置/直接反侧及actual owner见[B3本项](../_sources/daily-20260612/SUP_NECESSARY_B3_20261026.md#12105--dam-vla-decoupled-asynchronous-multimodal-vision-language-action-model)；唯一稿真实SAVE后经非作者§44实际POST通过，不代表日级完成，未核代码/复现。

### [Adaptive Multi-Resolution Procedural Knowledge Compression for Large Language Models](https://arxiv.org/html/2606.12203v1)

采用exact-v1的skill/target绑定的多分辨率前缀与银参考预算接口。stage3仍适配共享LoRA，full-text银参考可错，预算更多不单调，模拟tool observation不验证真实执行权限。 完整必要位置/直接反侧及actual owner见[B3本项](../_sources/daily-20260612/SUP_NECESSARY_B3_20261026.md#12203--adaptive-multi-resolution-procedural-knowledge-compression-for-large-language-models)；唯一稿真实SAVE后经非作者§44实际POST通过，不代表日级完成，未核代码/复现。

### [InternVideo3: Agentify Foundation Models with Multimodal Contextual Reasoning](https://arxiv.org/html/2606.12195v1)

采用exact-v1的多模态GQA转latent时QK-Norm近似、模态latent与恢复条件。保token不保原head KV，输入相关RMSNorm不能一般静态合并；需校准/CPT/longctx训练，不是无损codec或serving SLO。 完整必要位置/直接反侧及actual owner见[B3本项](../_sources/daily-20260612/SUP_NECESSARY_B3_20261026.md#12195--internvideo3-agentify-foundation-models-with-multimodal-contextual-reasoning)；唯一稿真实SAVE后经非作者§51实际POST通过，不代表日级完成，未核代码/复现。

### [Re-evaluating Confidence Remasking in Masked Diffusion Language Models](https://arxiv.org/html/2606.12232v1)

采用exact-v1的强unmask基线下remasking边际与shadow近似/flipflop诊断。deep hidden仍带原token、shadow加长序列；短block/greedy收益小且不一致，随机分支coverage反侧不证明所有修订无用。 完整必要位置/直接反侧及actual owner见[B3本项](../_sources/daily-20260612/SUP_NECESSARY_B3_20261026.md#12232--re-evaluating-confidence-remasking-in-masked-diffusion-language-models)；唯一稿真实SAVE后经非作者§51实际POST通过，不代表日级完成，未核代码/复现。

### [Selection Integrity for LLM Graph Memory: An Accumulability Criterion for Information-Flow-Blind Retrieval](https://arxiv.org/html/2606.12290v1)

采用exact-v1的未返回的低信任结构亦可改selected set，内容IFC与选择来源分责。authenticated返回fact不免结构channel；双图replay只是authority event，原型edge-tail剔除非通用taint，良性结构亦有用，不授开放安全。 完整必要位置/直接反侧及actual owner见[B3本项](../_sources/daily-20260612/SUP_NECESSARY_B3_20261026.md#12290--selection-integrity-for-llm-graph-memory)；唯一稿真实SAVE后经非作者§51实际POST通过，不代表日级完成，未核代码/复现。

### [CHORUS: Decentralized Multi-Embodiment Collaboration with One VLA Policy](https://arxiv.org/html/2606.12352v1)

采用exact-v1的共享policy权重与每机器人本地执行分离，局部可见/时序条件。关键队友视觉可见/已知role是条件；严格同步仍需centralized，大延迟差失配，部分得分不等完整成功或ToM。 完整必要位置/直接反侧及actual owner见[B3本项](../_sources/daily-20260612/SUP_NECESSARY_B3_20261026.md#12352--chorus)；唯一稿真实SAVE后经非作者§52实际POST通过，不代表日级完成，未核代码/复现。

### [Beyond Fully Random Masking: Attention-Guided Denoising and Optimization for Diffusion Language Models](https://arxiv.org/html/2606.12273v1)

采用exact-v1的完整completion图提出available-mass顺序与hubweight，训练特权分责。一次完整图固定、可见集重排；attention非正确性/credit，SFT/RL任务和块长有反退，近匹配forward非全预算或fastdecoder提速。 完整必要位置/直接反侧及actual owner见[B3本项](../_sources/daily-20260612/SUP_NECESSARY_B3_20261026.md#12273--agdo)；唯一稿真实SAVE后经非作者§52实际POST通过，不代表日级完成，未核代码/复现。

### [Exploration Structure in LLM Agents for Multi-File Change Localization](https://arxiv.org/html/2606.11976v1)

采用exact-v1的行为必需-v-PR触及的gold对象可让同预测F1排序翻转。单Ansible/持久session，curated排tests而PR含tests/changelog；checkout不对称、nudge单run不显著，不授并行独优或patch成功。 完整必要位置/直接反侧及actual owner见[B3本项](../_sources/daily-20260612/SUP_NECESSARY_B3_20261026.md#11976--exploration-structure-in-llm-agents-for-multi-file-change-localization)；唯一稿真实SAVE后经非作者§58实际POST通过，不代表日级完成，未核代码/复现。

### [WorldReasoner: Evaluating Whether Language Model Agents Forecast Events with Valid Reasoning](https://arxiv.org/html/2606.11816v1)

采用exact-v1的历史retrieval gate-v-参数cutoff proxy与hindsight-v-calibration分离。120题/525模型题pair人口不相同，KER命中hindsight非因果真值；search高于graph、selected confidence非完整向量校准，不授预测能力。 完整必要位置/直接反侧及actual owner见[B3本项](../_sources/daily-20260612/SUP_NECESSARY_B3_20261026.md#11816--worldreasoner-evaluating-whether-language-model-agents-forecast-events-with-valid-reasoning)；唯一稿真实SAVE后经非作者§58实际POST通过，不代表日级完成，未核代码/复现。

### [Tail-Aware Adaptive-k: Query-Adaptive Context Selection for Retrieval-Augmented Generation](https://arxiv.org/html/2606.11907v1)

exact-v1 §3/Eq1–7/Algorithm1、§4/Table1–3及AppA/B中心争议保留。排序score递减而x递增，使原d=(y−x)/√2严格递减、argmax只能首点；等score又零分母。原z=s−l≤0与所称GPD反射不闭，weighted mixture posterior也不由未加权density crossing给出；ε0均匀尾的scale仍随阈值变，不能无条件继承Oε稳定。有限wiki answer-string proxy及局部费用照留，不宣布所有实测无效；[原证/反例](../_sources/daily-20260612/SUP_NECESSARY_B3_20261026.md#11907--tail-aware-adaptive-k-query-adaptive-context-selection-for-retrieval-augmented-generation中心机制争议)。reader §56中心H通过，不改Books、不降N或零分；有一致更正knee/reflection/CVM及其有效条件，或与原实测对应的明确机制，才定点重开。

### [When Does Language Matter? Multilingual Instructions Reveal Step-wise Language Sensitivity in Vision-Language-Action Models](https://arxiv.org/html/2606.11906v1)

精确v1采用English轨迹离线梯度reference与在线hidden邻域step介入分责。保纯仿真、部分语言all-step更好、τ未披露/EN回归未证及完整费用，不授物理安全。 必要位置/直接反侧/actualowner详见[B3本项证据](../_sources/daily-20260612/SUP_NECESSARY_B3_20261026.md)；原唯一两段真实SAVE后，jun12_review_finish §59实际POST通过。未核实现/复现，不代本日验收。

### [Phase Transitions in Attention: A Bayesian Theory of Copy Head Emergence](https://arxiv.org/html/2606.12058v1)

精确v1采用受控copy模型两模式竞争与attention归一化改变转变阶数。保宽度/正则/无mask与iid条件、Adam低loss cluster筛选/SGLD混合，不授统一LLM定律或无预警。 必要位置/直接反侧/actualowner详见[B3本项证据](../_sources/daily-20260612/SUP_NECESSARY_B3_20261026.md)；原唯一两段真实SAVE后，jun12_review_finish §71实际POST通过。未核实现/复现，不代本日验收。

### [Beyond representational alignment with brain-guided language models for robust reasoning](https://arxiv.org/html/2606.11893v1)

精确v1采用外部参考映射读数与去截距写目标、label纠错权限分离。只采用LLM改进分支；已知原错/人对label核验不等在线无标签，原正确可翻错、旧任务亦退，不授共同认知机制。 必要位置/直接反侧/actualowner详见[B3本项证据](../_sources/daily-20260612/SUP_NECESSARY_B3_20261026.md)；原唯一两段真实SAVE后，jun12_review_finish §71实际POST通过。未核实现/复现，不代本日验收。

### [IAPO: Input Attribution-Aware Policy Optimization for Tool Use in Small Multimodal Agents](https://arxiv.org/html/2606.11652v1)

精确v1采用teacher/actor输入块梯度代理分布匹配作为额外工具训练监督。gradient-times-embedding非标准IG/因果credit；两turn/额外teacher预算、强teacher及λ反退，不批准工具权限。 必要位置/直接反侧/actualowner详见[B4本项证据](../_sources/daily-20260612/SUP_NECESSARY_B4_20261026.md)；原唯一两段真实SAVE后，jun12_review_finish §72实际POST通过。未核实现/复现，不代本日验收。

### [Dummy Backdoor as a Defense: Removing Unknown Backdoors via Shared Internal Mechanisms for Generative LLMs](https://arxiv.org/html/2606.11648v1)

精确v1采用已知dummy作为同攻击目标下未知trigger清理proxy。TAC非因果，跨目标几乎无效、keywordASR与LoRA剪枝身份/效用边界保留，不授未知自适应安全。 必要位置/直接反侧/actualowner详见[B4本项证据](../_sources/daily-20260612/SUP_NECESSARY_B4_20261026.md)；原唯一两段真实SAVE后，jun12_review_finish §72实际POST通过。未核实现/复现，不代本日验收。

### [Improving Cross-Format Robustness in Language Models with Multi-Format Training](https://arxiv.org/html/2606.11643v1)

精确v1采用source-item对齐的any-v-all格式breadth/consistency及扩样预算。先split后改写、三改写投票非独立题，matchedinstances非tokens，BBH/Targeted反退；原5保持且反侧深入。 必要位置/直接反侧/actualowner详见[B4本项证据](../_sources/daily-20260612/SUP_NECESSARY_B4_20261026.md)；原唯一两段真实SAVE后，jun12_review_finish §72实际POST通过。未核实现/复现，不代本日验收。

### [Can Open-Source LLM Agents Replace Static Application Security Testing Tools? An Empirical Assessment](https://arxiv.org/html/2606.11672v1)

唯一必要首备由reader §60完成并由作者完整采用；仅固定prompt/逐文件Snitch、三repo及Bandit参照，partialmatch和conditional potentialFP不签真实recall/FPR或所有Agent能力上限。Ch66实际reference资格、历史concern未列保Unjudged与真实输入缺陷/条件分母已承载这一采用边界，见[B4具体NC](../_sources/daily-20260612/SUP_NECESSARY_B4_20261026.md)；reader §67具体已有覆盖通过，保原5、局部作者观测和预算限制，不改Books、不降N，未核代码/复现。

### [From Prompts to Tokens: Internalizing Causal Supervision in Vision-Language Model for Multi-Image Causal Reasoning](https://arxiv.org/html/2606.11745v1)

实际必要§3/4/AppB1/C/D/E/F1，详见[B4本项](../_sources/daily-20260612/SUP_NECESSARY_B4_20261026.md)。采用先绑定latent节点身份再监督关系边，oracle图不代因果发现；保component标签与节点身份绑定、CELLO zero-shot/时延反侧，不授真实SCM因果。实际owner MULTIMODAL-REPRESENTATION Ch23，唯一原两段及本人注真实SAVE，jun12_review_finish §76实际完整新增/两侧/本人注POST通过；不宣称代码核验或实验复现。

### [TacCoRL: Integrating Tactile Feedback into VLA via Simulation](https://arxiv.org/html/2606.11743v1)

实际必要§3/4/AppA/B1–3/C/D，详见[B4本项](../_sources/daily-20260612/SUP_NECESSARY_B4_20261026.md)。采用sim后训练需joint-response与policy-facing触觉校准及real anchor；保normal-taxel非shear/fullforce、BC系数与warmstart反侧，不授真实安全。实际owner MULTIMODAL-EMBODIED-VLA Ch26，唯一原两段及本人注真实SAVE，jun12_review_finish §76实际完整新增/两侧/本人注POST通过；不宣称代码核验或实验复现。

### [CompRank: Efficient LLM Reranking via Token-Level Compression and Decoding-Free Scoring](https://arxiv.org/html/2606.11700v1)

实际必要§3/4/5/Table1–2、AppA1–3/B/E/Table4/F，详见[B4本项](../_sources/daily-20260612/SUP_NECESSARY_B4_20261026.md)。采用独立doc state、query消费支集与同attentionmass候选监督分责；保均匀覆盖/压缩反退与模拟preencoded分解非实装cache加速，不授检索等于证据真值。实际owner AGENT-RAG Ch76，唯一原两段及本人注真实SAVE，jun12_review_finish §76实际完整新增/两侧/本人注POST通过；不宣称代码核验或实验复现。

### [Architecture-Aware Reinforcement Learning Makes Sliding-Window Attention Competitive in Math Reasoning](https://arxiv.org/html/2606.11634v1)

实际必要§3/4/5/Limit及A1.3–4/A2.2–3，详见[B4本项](../_sources/daily-20260612/SUP_NECESSARY_B4_20261026.md)。采用局部attention需同可见性轨迹/RL适配，conversion后退不证能力天花板；保长输入检索反退、来源轨迹同时改善SA、最大batch不同，不授不需长期状态。实际owner MODEL-LONG-CONTEXT Ch22，唯一原两段及本人注真实SAVE，jun12_review_finish §85实际完整新增/两侧/本人注POST通过；不宣称代码核验或实验复现。

### [Information-Theoretic Decomposition for Multimodal Interaction Learning](https://arxiv.org/html/2606.11614v1)

实际必要§3/4/6.1–3/7.1–2，详见[B4本项](../_sources/daily-20260612/SUP_NECESSARY_B4_20261026.md)。采用单模态与组合候选分路、component读出不等真实PID；保信息lowerbound非语义可识别性、类留出/三modal协议不同，不授无损/OOD保证。实际owner MULTIMODAL-REPRESENTATION Ch23，唯一原两段及本人注真实SAVE，jun12_review_finish §85实际完整新增/两侧/本人注POST通过；不宣称代码核验或实验复现。

### [When is Your LLM Steerable?](https://arxiv.org/html/2606.11599v1)

实际必要§2–5/E/F/G/H，详见[B4本项](../_sources/daily-20260612/SUP_NECESSARY_B4_20261026.md)。采用同已实现早prefix双前向预测干预剂量并排序候选；保固定prefix不等自然无干预因果，漏succ与token费用不含全前向，不授安全编辑。实际owner WORLDVIEW-REPRESENTATION Ch5，唯一原两段及本人注真实SAVE，jun12_review_finish §85实际完整新增/两侧/本人注POST通过；不宣称代码核验或实验复现。

### [AVIS: Adaptive Test-Time Scaling for Vision-Language Models](https://arxiv.org/html/2606.11576v1)

实际必要§3–5/AppA2/B1–4/D，详见[B4本项](../_sources/daily-20260612/SUP_NECESSARY_B4_20261026.md)。采用视觉token与rollout预期预算分阶段分配、概率身份需校准；保二值阈值事件置信非单轨迹p、多类投票非binary证明与墙钟反侧，不授无损理解。实际owner MULTIMODAL-REPRESENTATION Ch23，唯一原两段及本人注真实SAVE，jun12_review_finish §85实际完整新增/两侧/本人注POST通过；不宣称代码核验或实验复现。

### [4DP-QA: Scalable QA for 4D Perception in Vision Language Models](https://arxiv.org/html/2606.11568v1)

实际reader§77必要与§86实际owner/PRE，详见[本项限定证据](../_sources/daily-20260612/SUP_NECESSARY_B4_20261026.md)。采用固定query相机重投影提供物体/相机运动参照系对照；保fixed-reference只是2D监督，替换比例/realgeometry反退，完整费用与退路仍在，不宣称实现核验/复现。唯一owner MULTIMODAL-REPRESENTATION Ch23，原两段/本人注已真实SAVE并由jun12_review_finish §92完整新增/两侧/注实际POST通过。

### [GraphInfer-Bench: Benchmarking LLM's Inference Capability on Graphs](https://arxiv.org/html/2606.11562v1)

实际reader§78必要与§87实际owner/PRE，详见[本项限定证据](../_sources/daily-20260612/SUP_NECESSARY_B4_20261026.md)。采用neighborhood汇聚任务与node/path lookup、hard结构-v-prose评分分责；保Table6不支持GNN每task皆优、格式/额外node与parser分母，完整费用与退路仍在，不宣称实现核验/复现。唯一owner PLATFORM-EVALUATION-SYSTEM Ch66，原两段/本人注已真实SAVE并由jun12_review_finish §92完整新增/两侧/注实际POST通过。

### [HERO: Hindsight-Enhanced Reflection from Environment Observations for Agentic Self-Distillation](https://arxiv.org/html/2606.11559v1)

实际reader§79必要与§88实际owner/PRE，详见[本项限定证据](../_sources/daily-20260612/SUP_NECESSARY_B4_20261026.md)。采用causal rollout与事后future局部hint在原action监督边界分离；保future泄漏/不可用动作与无符号JSD不证因果credit，完整费用与退路仍在，不宣称实现核验/复现。唯一owner TRAIN-SFT Ch29，原两段/本人注已真实SAVE并由jun12_review_finish §92完整新增/两侧/注实际POST通过。

### [Counterexample Guided Learning in the Large using Reasoning Agents](https://arxiv.org/html/2606.11521v1)

实际reader§80必要与§89实际owner/PRE，详见[本项限定证据](../_sources/daily-20260612/SUP_NECESSARY_B4_20261026.md)。采用symbolic counterexample cluster与外部Equiv判等分责；保finite cluster/repair预算与Single反侧，不授普遍CEGIS完备，完整费用与退路仍在，不宣称实现核验/复现。唯一owner AGENT-REFLECTION Ch80，原两段/本人注已真实SAVE并由jun12_review_finish §92完整新增/两侧/注实际POST通过。

### [Steering Where to Listen: Instruction-Based Activation Steering Redirects Temporal Attention in Large Audio-Language Models](https://arxiv.org/html/2606.11400v1)

实际§3–6/Table1，详见[本项限定证据](../_sources/daily-20260612/SUP_NECESSARY_B4_20261026.md)。采用同音频instruction contrast改变时间attention的受限定位读出；保GTduration窗口/覆盖率非IoU，AF3部分位置direct更好，完整费用与退路仍在，不宣称实现核验/复现。唯一owner MULTIMODAL-REPRESENTATION Ch23，原两段/本人注已真实SAVE并由jun12_review_finish §93完整新增/两侧/注实际POST通过。

### [Task-Aligned Stability Analysis of Vision-Language Models for Autonomous Driving Hazard Detection](https://arxiv.org/html/2606.11889v1)

实际§2–4/AppA，详见[本项限定证据](../_sources/daily-20260612/SUP_NECESSARY_B4_20261026.md)。采用embedding几何drift与固定task margin/clean-relative flips分账；保flip非独立hazard FPR/FNR，不采作者局部bound为通用certificate，完整费用与退路仍在，不宣称实现核验/复现。唯一owner PLATFORM-EVALUATION-SYSTEM Ch66，原两段/本人注已真实SAVE并由jun12_review_finish §93完整新增/两侧/注实际POST通过。

### [PLUME: Probabilistic Latent Unified World Modeling and Parameter Estimation for Multi-Finger Manipulation](https://arxiv.org/html/2606.11396v1)

实际§3–5/AppA/C/E/F/G，详见[本项限定证据](../_sources/daily-20260612/SUP_NECESSARY_B4_20261026.md)。采用参数belief粒子与action-conditioned预测联合flow、采样防坍塌；保likelihood/OOD heuristic非校准后验，valid条件距离与组件反退，完整费用与退路仍在，不宣称实现核验/复现。唯一owner MULTIMODAL-WORLD-MODELS Ch25，原两段/本人注已真实SAVE并由jun12_review_finish §96完整新增/两侧/注实际POST通过。

### [Overcoming State Inertia in Full-Duplex Spoken Language Models via Activation Steering](https://arxiv.org/html/2606.11386v1)

实际§3–7/AppA/B/F/H/I，详见[本项限定证据](../_sources/daily-20260612/SUP_NECESSARY_B4_20261026.md)。采用双流首词切换proxy与onset触发短干预、完整回答分验；保IWOR非知觉因果、长span/false-trigger与普通FDB反侧，完整费用与退路仍在，不宣称实现核验/复现。唯一owner MULTIMODAL-REPRESENTATION Ch23，原两段/本人注已真实SAVE并由jun12_review_finish §96完整新增/两侧/注实际POST通过。

### [Beyond Third-Person Audits: Situated Interaction Auditing for User-Centered LLM Bias Research](https://arxiv.org/html/2606.12247v1)

实际§3/4/Limit/Ethics/B3/B4/B6，详见[本项限定证据](../_sources/daily-20260612/SUP_NECESSARY_B5_FN_20261026.md)。采用同请求interlocutor profile条件与第三方群体审计人口分开；保总体effects小/跨模型反向，name代理与judge不授社会真值，完整费用与退路仍在，不宣称实现核验/复现。唯一owner PLATFORM-EVALUATION-SYSTEM Ch66，原两段/本人注已真实SAVE并由jun12_review_finish §101完整新增/两侧/注实际POST通过。

### [Are LLMs Bad at Moral Reasoning?](https://arxiv.org/html/2606.11635v1)

实际§3–7/Table1–5，详见[本项限定证据](../_sources/daily-20260612/SUP_NECESSARY_B5_FN_20261026.md)。采用human写rubric-v-model答题不对称及标准改写estimand变化；保matched/nearby不证规范等价，capture非连贯/行动能力，完整费用与退路仍在，不宣称实现核验/复现。唯一owner PLATFORM-EVALUATION-SYSTEM Ch66，原两段/本人注已真实SAVE并由jun12_review_finish §101完整新增/两侧/注实际POST通过。

### [Should LLM Agents Decide in Social Simulations? Comparing Finite-State and LLM-Based Decision Policies](https://arxiv.org/html/2606.12369v1)

实际§3–5/Table1–2，详见[本项限定证据](../_sources/daily-20260612/SUP_NECESSARY_B5_FN_20261026.md)。采用明确Markov policy与LLM selector的分布及费用负对照；保same-context构造非每步固定realizedcontext，reference非真实人类，完整费用与退路仍在，不宣称实现核验/复现。实际Ch78 sampler三段及Ch81 runtime policy已具体覆盖，reader§97 NC通过，原5不变，不执行准备稿。

### [A Scalable PyTorch Abstraction for Multi-GPU Gaussian Splatting](https://arxiv.org/html/2606.11390v1)

实际§3/5/A1–4，详见[本项限定证据](../_sources/daily-20260612/SUP_NECESSARY_B5_FN_20261026.md)。采用aggregate device把分片/events/CPUfallback交operator backend；保fixedbatch slowdown、A4仅一diffusion，不授所有模型透明scaling，完整费用与退路仍在，不宣称实现核验/复现。唯一owner TRAIN-DISTRIBUTED-TRAINING Ch36，原两段/本人注已真实SAVE并由jun12_review_finish §103完整新增/两侧/注实际POST通过。

### [How Seemingly Inconsequential Design Choices Dictate Performance of LLMs in Pathology](https://arxiv.org/html/2606.12407v1)

实际必要§3–5/C2/D1，详见[FN限定证据](../_sources/daily-20260612/SUP_NECESSARY_B5_FN_20261026.md)。采用四输入因素改变同模型baseline差额，探索/择优与heldout分账；保72cell仅100探索、相关ANOVA非显著检验/同评选择乐观，CPTAC185与PANDA/混合尺度反退，所有制备/运行/校准/独立回归费用与退路仍在。唯一owner PLATFORM-EVALUATION-SYSTEM Ch66，原两段/本人注真实SAVE，jun12_review_finish §106新增/完整两侧/本人注实际POST通过；未核实现或复现，不外推临床/科学产出、密码学安全或生产SLO。

### [MPC-Patch-Bench: Security-Aware LLM Code Patch for Multi-Party Computation](https://arxiv.org/html/2606.11416v1)

实际必要§3.3–5/Limit/AppA/C/F，详见[FN限定证据](../_sources/daily-20260612/SUP_NECESSARY_B5_FN_20261026.md)。采用F2P/P2P之后数值oracle与安全规则的检查人口分离；保checker拒绝非已证漏洞率、loop reveal需权限/语义、有限oracle与context排除，所有制备/运行/校准/独立回归费用与退路仍在。唯一owner PLATFORM-EVALUATION-SYSTEM Ch66，原两段/本人注真实SAVE，jun12_review_finish §106新增/完整两侧/本人注实际POST通过；未核实现或复现，不外推临床/科学产出、密码学安全或生产SLO。

### [Frozen Foundation-Model Embeddings Discard Small-Lesion Signal in Chest Radiography: Implications for Pre-Deployment Evaluation](https://arxiv.org/html/2606.11606v1)

实际必要§2.4–2.6/3.10/4.8，详见[FN限定证据](../_sources/daily-20260612/SUP_NECESSARY_B5_FN_20261026.md)。采用same-frozen-forward的global-v-oracleROI pooling局部信号可读性；保oracleROI不是部署proposer，AUC非固定误报保证/不证全信息删除，共享人口与小stratum，所有制备/运行/校准/独立回归费用与退路仍在。唯一owner MULTIMODAL-REPRESENTATION Ch23，原两段/本人注真实SAVE，jun12_review_finish §109新增/完整两侧/本人注实际POST通过；未核实现或复现，不外推临床/科学产出、密码学安全或生产SLO。

### [On the Limits of LLM-as-Judge for Scientific Novelty Assessment](https://arxiv.org/html/2606.12071v1)

实际必要§4–7/A3，详见[FN限定证据](../_sources/daily-20260612/SUP_NECESSARY_B5_FN_20261026.md)。采用author-anchor与独立-v-同屏judge、逐维/逐judge best-of-five分责；保重构参照非唯一真题、各judge赢家未必同一候选、专家反向/分歧与7.2反侧，所有制备/运行/校准/独立回归费用与退路仍在。唯一owner PLATFORM-EVALUATION-SYSTEM Ch66，原两段/本人注真实SAVE，jun12_review_finish §110新增/完整两侧/本人注实际POST通过；未核实现或复现，不外推临床/科学产出、密码学安全或生产SLO。

以下保留原63候选的旧轮有效证据，末Books/semantic audit的9I/53NC/1仅报告不代表本轮新增分布。

### [Which Models Are Our Models Built On? Auditing Invisible Dependencies in Modern LLMs](https://arxiv.org/html/2606.12385v1)

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：模型卡不足以表达递归 training dependencies；provenance 应以 artifact identity 和 operation-centered edges 递归解析生成、过滤、judge 与 selection 关系。

**State / data / control owner。** `TRAIN-DATA` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.12385v1 §4 Evaluation; §5 Findings` 支持 `Public-artifact dependency reconstruction across target LLMs`；模型 `Agentic ModSleuth plus audited model artifacts`；硬件 `Not Disclosed — document analysis workload`；精度 `Not applicable`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.12385v1 §3 Design of ModSleuth`；counterevidence locator：`arXiv:2606.12385v1 Appendix A verification; Appendix D disclosure gaps`。

**Trade-off / failure / coexistence / evolution。** 递归发现提高 lineage 但受公开文档缺失和 entity resolution 错误限制；它是 audit evidence，不是完整 SBOM guarantee。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-12385:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.12385v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-12385:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-04-training-system/27-data.md`，Review notes 前正文锚点 `Data lineage 是训练可复现性的前提` 已承载长期命题；source 仅作受限证据。

### [Muse Spark Safety & Preparedness Report](https://arxiv.org/html/2606.12429v1)

**问题与机制。** 原筛选把《Muse Spark Safety & Preparedness Report》关闭或降池；完整摘要显示“In this report, we first present evaluations for catastrophic risk domains under Meta's Advanced AI Scaling Framework, along with the evidence that informed our launch decision.”。该增量直接改变 PLATFORM-SECURITY 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`5.1 Evaluation Methodology`；可采用的最小机制命题是：In this report, we first present evaluations for catastrophic risk domains under Meta's Advanced AI Scaling Framework, along with the evidence that informed our launch decision.

**Evaluation proof。** `1.3 Evaluation Setup; 4.1 Primary Behavior Evaluation; 5 Content Safety Evaluations`；exact-v1 披露：In this report, we first present evaluations for catastrophic risk domains under Meta's Advanced AI Scaling Framework, along with the evidence that informed our launch decision.

**Limitations / non-proof。** `未定位独立 limitations；边界由 exact-v1 披露 workload 推得`；We therefore release Muse Spark as the underlying model of Meta AI. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `PLATFORM-SECURITY` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-06-ai-infrastructure/72-security.md`，Review notes 前正文锚点 `从资产与信任边界开始` 已承载长期命题；source 仅作受限证据。

### [ToolSense: A Diagnostic Framework for Auditing Parametric Tool Knowledge in LLMs](https://arxiv.org/html/2606.12451v1)

**问题与机制。** 原筛选把《ToolSense: A Diagnostic Framework for Auditing Parametric Tool Knowledge in LLMs》关闭或降池；完整摘要显示“We introduce \textbf{ToolSense}, an open-source LLM-powered diagnostic framework that takes any tool catalog as input and automatically generates three benchmarks: a Realistic Retrieval Benchmark (RRB) with queries at three ambiguity tiers, an MCQ probing benchmark, and a QA probing benchmark.”。该增量直接改变 AGENT-TOOL-CALLING 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`3 The ToolSense Framework; 5.5 Cross-Architecture Validation; Appendix H Cross-Architecture Probing Results`；可采用的最小机制命题是：We introduce \textbf{ToolSense}, an open-source LLM-powered diagnostic framework that takes any tool catalog as input and automatically generates three benchmarks: a Realistic Retrieval Benchmark (RRB) with queries at three ambiguity tiers, an MCQ probing benchmark, and a QA probing benchmark.

**Evaluation proof。** `3.3 Free-form Evaluation and Internalization Score; 4 Experimental Setup; 5 Results`；exact-v1 披露：Yet these benchmarks use verbose, fully-specified queries, and their evaluation applies constrained decoding that restricts outputs to valid token paths, neither reveals whether the model actually understands its tools.

**Limitations / non-proof。** `Limitations`；We open-source the ToolSense framework and the ToolBench diagnostic benchmarks at https://github.com/SAP/toolsense. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `AGENT-TOOL-CALLING` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-07-agent/78-tool-calling.md`，Review notes 前正文锚点 `Tool Contract` 已承载长期命题；source 仅作受限证据。

### [Influence Factors on RAG Poisoning](https://arxiv.org/html/2606.12469v1)

<!-- claim:SF-2026-ARXIV-2606-12469:start -->
`Influence Factors on RAG Poisoning` 的 exact-v1 问题边界来自 `https://arxiv.org/html/2606.12469v1`：Retrieval-Augmented Generation (RAG) systems enhance large language models by grounding responses in retrieved documents from external knowledge sources at inference time.

机制与 owner：Treat RAG poisoning as an interaction among retriever, top-k, chunking, database composition and generator, using a factorial design instead of a single attack rate. 状态/数据/控制 owner 固定为 `AGENT-RAG`；Method 锚点是 `§3 Methodology`。它相对旧路径的变化不是多一个分数，而是把原先隐含在 prompt、静态规则或全局预算里的决定变成可记录、可验证、可回退的状态转换。

Evaluation proof：`§4 Results and Discussion` 只证明 `432-factorial grid over aligned 100-question HotpotQA/MS-MARCO subsets, retriever, top-k, chunking and database composition` 上、`llama-4-scout-17b-16e-instruct; openai-gpt-oss-120b` 条件下的报告指标。hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed — measured outcomes and experimental thresholds are not production SLOs`。未披露字段保持 Not Disclosed，不由模型名、加速比或实验阈值反推。

Trade-off、failure、共存与演进：The 432 configurations use two curated 100-question subsets and two generators; factor effects are evidence for that grid, not universal retriever ordering. 反证/外推边界在 `§5 Conclusions`；因此旧方案保留为低状态成本、证据不足或不满足论文前提时的共存分支。
<!-- claim:SF-2026-ARXIV-2606-12469:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-07-agent/76-rag.md`，Review notes 前正文锚点 `RAG 安全必须覆盖完整状态生命周期` 已承载长期命题；source 仅作受限证据。

### [SAIGuard: Communication-State Simulation for Proactive Defense of LLM Multi-Agent Systems](https://arxiv.org/html/2606.12474v1)

**问题与机制。** 原筛选把《SAIGuard: Communication-State Simulation for Proactive Defense of LLM Multi-Agent Systems》关闭或降池；完整摘要显示“To address this, we propose a proactive defense framework for MAS security, namely a Simulation-aware Interception Guard (SAIGuard).”。该增量直接改变 PLATFORM-SECURITY 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`3 Methodology`；可采用的最小机制命题是：To address this, we propose a proactive defense framework for MAS security, namely a Simulation-aware Interception Guard (SAIGuard).

**Evaluation proof。** `4 Experiment; 4.1 Experiment Setup; Appendix C Detailed Experiment Setups`；exact-v1 披露：Experiments across diverse topologies and attack scenarios show that SAIGuard reduces attack success rates while maintaining MAS utility, outperforming reactive defenses.

**Limitations / non-proof。** `Limitations`；Experiments across diverse topologies and attack scenarios show that SAIGuard reduces attack success rates while maintaining MAS utility, outperforming reactive defenses. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `PLATFORM-SECURITY` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `Integrate` → `books/part-06-ai-infrastructure/72-security.md`，Review notes 前正文锚点 `Multi-Agent 防御要在消息传播前模拟状态偏移` 已完成写入并通过独立 post-write audit。

### [ReCal: Reward Calibration for RL-based LLM Routing](https://arxiv.org/html/2606.12479v1)

**问题与机制。** 原筛选把《ReCal: Reward Calibration for RL-based LLM Routing》关闭或降池；完整摘要显示“To address these issues, we propose \textbf{ReCal}, a \textbf{\underline{Re}}ward \textbf{\underline{Cal}}ibration framework for RL-based LLM routing.”。该增量直接改变 INFER-SCHEDULING 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`4 The Proposed Framework: ReCal`；可采用的最小机制命题是：To address these issues, we propose \textbf{ReCal}, a \textbf{\underline{Re}}ward \textbf{\underline{Cal}}ibration framework for RL-based LLM routing.

**Evaluation proof。** `5 Experiments; 5.1 Experimental Setup; 5.2 Main Results`；exact-v1 披露：Experiments on seven datasets demonstrate that ReCal consistently improves routing performance, and training stability over baselines.

**Limitations / non-proof。** `Limitations`；Code is available at https://anonymous.4open.science/r/ReCal. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `INFER-SCHEDULING` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-05-inference-system/56-inference-scheduling.md`，Review notes 前正文锚点 `Model Routing 与 Test-time Scaling 必须结算同一个 Budget` 已承载长期命题；source 仅作受限证据。

### [DynamicPTQ: Mitigating Activation Quantization Collapse via Residual-Stream Dynamics](https://arxiv.org/html/2606.12487v1)

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：4-bit activation/KV PTQ 需要观察 residual stream 的 phase-wise jump，并对关键相位采用 mixed precision，而非只做静态 rotation smoothing。

**State / data / control owner。** `INFER-TENSORRT-LLM` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.12487v1 §4 Experiments; §4.9 efficiency` 支持 `Perplexity, zero-shot QA, reasoning and efficiency across dense/MoE LLMs`；模型 `Multiple dense and MoE PTQ backbones`；硬件 `Disclosed in §4.2; exact accelerator remains paper-bound`；精度 `W4A4/KV4 with phase-aware higher precision`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.12487v1 §3 Method; §3.3 policy`；counterevidence locator：`arXiv:2606.12487v1 §7 Discussion; no dedicated limitations section`。

**Trade-off / failure / coexistence / evolution。** mixed precision 减少 collapse 却削弱全 4-bit memory/throughput 收益；新 backbone 需重新 calibration。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-12487:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.12487v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-12487:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-05-inference-system/49-tensorrt-llm.md`，Review notes 前正文锚点 `量化为什么不自动带来加速` 已承载长期命题；source 仅作受限证据。

### [ITME: Inference Tiered Memory Expansion with Disaggregated CXL-Hybrid Memories](https://arxiv.org/html/2606.12556v1)

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：长 context state 可跨 GPU/host/CXL-hybrid/NVMe 构成 byte-addressable tier，并利用 model-weight/prefix access 可预测性做 multi-tier DMA prefetch。

**State / data / control owner。** `INFER-GPU-MEMORY` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.12556v1 §5 methodology; §6 evaluation` 支持 `Weight and KV offload across GPU, host, CXL and NVMe-oF tiers`；模型 `LLM inference configurations disclosed in §5.1`；硬件 `SK hynix CMM, PCIe Gen5 NVMe SSDs and FPGA prototype`；精度 `Not Disclosed`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.12556v1 §3 CXL-Hybrid Architecture; §4 ITME`；counterevidence locator：`arXiv:2606.12556v1 §8 Conclusion; no dedicated limitations section`。

**Trade-off / failure / coexistence / evolution。** 扩容降低 HBM pressure，却增加预取错误、fabric contention 和硬件成本；不可预测 KV access 仍需普通 paging。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-12556:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.12556v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-12556:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-05-inference-system/54-gpu-memory.md`，Review notes 前正文锚点 `Weights 与 KV 的联合 HBM 预算：可提交的运行时精度页` 已承载长期命题；source 仅作受限证据。

### [Arbor: Tree Search as a Cognition Layer for Autonomous Agents](https://arxiv.org/html/2606.12563v1)

**问题与机制。** 原筛选把《Arbor: Tree Search as a Cognition Layer for Autonomous Agents》关闭或降池；完整摘要显示“Prior autonomous optimization systems operate on isolated targets with stateless evaluation.”。该增量直接改变 AGENT-WORKFLOW 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`3 Methodology; 3.1 Problem Formulation; 3.3 Multi-Agent Architecture`；可采用的最小机制命题是：Prior autonomous optimization systems operate on isolated targets with stateless evaluation.

**Evaluation proof。** `4 Experiments; 4.2 Main Results`；exact-v1 披露：Prior autonomous optimization systems operate on isolated targets with stateless evaluation.

**Limitations / non-proof。** `5 Limitations; 6 Discussion and Future Work`；Arbor generalizes to multiple generations of hardware platform, and run-to-run variance is within 2 percentage points demonstrating that the method is hardware-agnostic and reproducible. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `AGENT-WORKFLOW` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-07-agent/81-workflow.md`，Review notes 前正文锚点 `State Machine 是基本模型` 已承载长期命题；source 仅作受限证据。

### [Beyond Attack Success Rate: Examining Trigger Leakage in Vision-Language Agentic Systems](https://arxiv.org/html/2606.12586v1)

**问题与机制。** 原筛选把《Beyond Attack Success Rate: Examining Trigger Leakage in Vision-Language Agentic Systems》关闭或降池；完整摘要显示“In this work, we formalize the failure of trigger precision as "trigger leakage": inputs that are visually or semantically close to the intended trigger and therefore inadvertently activate the attacker-specified behavior.”。该增量直接改变 PLATFORM-SECURITY 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`§2 Threat Model; §3.2 Trigger Leakage; §§4.1–4.3 controlled probe and boundary supervision`；可采用的最小机制命题是：In this work, we formalize the failure of trigger precision as "trigger leakage": inputs that are visually or semantically close to the intended trigger and therefore inadvertently activate the attacker-specified behavior.

**Evaluation proof。** `§5 Agentic Workflow Evaluation`；exact-v1 披露：Current evaluations on such backdoors focus on clean accuracy and attack success rate (ASR), metrics that capture whether a trigger works, but not whether an attack is actually "precise" -- i.e. whether it triggers hidden behaviors only when intended.

**Limitations / non-proof。** `未定位独立 limitations；边界由 §2 attacker capability 与 §5 workload 推得`；Current evaluations on such backdoors focus on clean accuracy and attack success rate (ASR), metrics that capture whether a trigger works, but not whether an attack is actually "precise" -- i.e. whether it triggers hidden behaviors only when intended. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `PLATFORM-SECURITY` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `Integrate` → `books/part-06-ai-infrastructure/72-security.md`，Review notes 前正文锚点 `Backdoor Evaluation 必须测 Trigger 邻域` 已完成写入并通过独立 post-write audit。

### [Strategic Decision Support for AI Agents](https://arxiv.org/html/2606.12587v1)

**问题与机制。** 原筛选把《Strategic Decision Support for AI Agents》关闭或降池；完整摘要显示“We propose a framework for strategic decision support for AI agents through an optimization problem that minimizes support usage subject to controlling a counterfactual missed-support error: the probability that the agent acts alone on instances where support would have materially improved its output.”。该增量直接改变 AGENT-PLANNING 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`exact-v1 central method section`；可采用的最小机制命题是：We propose a framework for strategic decision support for AI agents through an optimization problem that minimizes support usage subject to controlling a counterfactual missed-support error: the probability that the agent acts alone on instances where support would have materially improved its output.

**Evaluation proof。** `5 Experiments; Appendix B Additional Experimental Results`；exact-v1 披露：At the population level, we show that the optimal policy is a threshold rule on the value of support.

**Limitations / non-proof。** `6 Limitations and Future Work`；Experiments across these settings show that our method reliably controls the target error while substantially reducing support usage in practice. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `AGENT-PLANNING` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-07-agent/79-planning.md`，Review notes 前正文锚点 `先校准不确定性，再决定行动、询问或探索` 已承载长期命题；source 仅作受限证据。

### [Keep Policy Gradient in Charge: Sibling-Guided Credit Distillation for Long-Horizon Tool-Use Agents](https://arxiv.org/html/2606.12634v1)

**问题与机制。** 原筛选把《Keep Policy Gradient in Charge: Sibling-Guided Credit Distillation for Long-Horizon Tool-Use Agents》关闭或降池；完整摘要显示“We introduce Sibling-Guided Credit Distillation (SGCD), which uses distillation for bounded credit weighting rather than as a competing actor loss.”。该增量直接改变 TRAIN-GRPO 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`exact-v1 central method section`；可采用的最小机制命题是：We introduce Sibling-Guided Credit Distillation (SGCD), which uses distillation for bounded credit weighting rather than as a competing actor loss.

**Evaluation proof。** `5 Experiments; 5.2 Main results`；exact-v1 披露：Direct self-distillation can supply a denser signal, but in our experiments it can also destroy tool use by rehearsing teacher behavior without identifying which actions the verifier rewards.

**Limitations / non-proof。** `Limitations`；Dynamic sampling produces mixed successful and failed sibling rollouts; an external LLM summarizes their contrast into a training-only credit reference; and detached teacher/student divergence reshapes GRPO token advantages. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `TRAIN-GRPO` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-04-training-system/33-grpo.md`，Review notes 前正文锚点 `从一个终局标量到 Typed Credit：Reward 必须匹配决策边界` 已承载长期命题；source 仅作受限证据。

### [Eidola: Modeling Multi-GPU Network Communication Traffic in Distributed AI Workloads](https://arxiv.org/html/2606.12638v1)

**问题与机制。** 原筛选把《Eidola: Modeling Multi-GPU Network Communication Traffic in Distributed AI Workloads》关闭或降池；完整摘要显示“In this work, we introduce Eidola, a scalable extension to the gem5 simulation framework that enables detailed modeling of inter-GPU communication traffic.”。该增量直接改变 TRAIN-DISTRIBUTED-TRAINING 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`exact-v1 central method section`；可采用的最小机制命题是：In this work, we introduce Eidola, a scalable extension to the gem5 simulation framework that enables detailed modeling of inter-GPU communication traffic.

**Evaluation proof。** `4. Results; 5. Case Study: SyncMon; 5.4. Case Study Summary`；exact-v1 披露：Our results show that Eidola provides a flexible and scalable platform for studying inter-GPU communication and supports architectural exploration in modern distributed GPU systems.

**Limitations / non-proof。** `未定位独立 limitations；边界由 exact-v1 披露 workload 推得`；Our results show that Eidola provides a flexible and scalable platform for studying inter-GPU communication and supports architectural exploration in modern distributed GPU systems. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `TRAIN-DISTRIBUTED-TRAINING` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-04-training-system/36-distributed-training.md`，Review notes 前正文锚点 `从静态通信配置到受验证的 Collective Policy` 已承载长期命题；source 仅作受限证据。

### [Evoflux: Inference-Time Evolution of Executable Tool Workflows for Compact Agents](https://arxiv.org/html/2606.12674v1)

**问题与机制。** 原筛选把《Evoflux: Inference-Time Evolution of Executable Tool Workflows for Compact Agents》关闭或降池；完整摘要显示“We introduce Evoflux, an inference-time evolutionary search method that treats compact tool use as the repair of executable tool workflows.”。该增量直接改变 AGENT-WORKFLOW 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`3 Method; A.4 Heuristic fallback method`；可采用的最小机制命题是：We introduce Evoflux, an inference-time evolutionary search method that treats compact tool use as the repair of executable tool workflows.

**Evaluation proof。** `4 Results and Analysis`；exact-v1 披露：These results show that execution-grounded search is more reliable under scarce teacher-trace budgets.

**Limitations / non-proof。** `Limitations`；These results show that execution-grounded search is more reliable under scarce teacher-trace budgets. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `AGENT-WORKFLOW` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-07-agent/81-workflow.md`，Review notes 前正文锚点 `Release 与 Optimization 必须共享 Workflow Identity` 已承载长期命题；source 仅作受限证据。

### [M*: A Modular, Extensible, Serving System for Multimodal Models](https://arxiv.org/html/2606.12688v1)

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：复合多模态模型的 serving contract 应从固定 stage DAG 演进为 model graph + named walks，显式支持 seq/parallel/loop/dynamic-loop/stream 与 component placement。

**State / data / control owner。** `INFER-KSERVE-TOPOLOGY` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.12688v1 §4 Evaluation; Appendix I reproducibility` 支持 `BAGEL, Qwen3-Omni, Orpheus and V-JEPA2 composite workloads`；模型 `BAGEL-7B, Qwen3-Omni-30B-A3B, Orpheus-3B, V-JEPA2`；硬件 `Single 4×H100 node or 8×H200 node`；精度 `Model-specific; not normalized as one precision`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.12688v1 §3 Walk Graph; §§3.1–3.3`；counterevidence locator：`arXiv:2606.12688v1 Appendix H Limitations`。

**Trade-off / failure / coexistence / evolution。** 通用 graph runtime 减少 glue code，却把 state machine、placement、tensor transport 与 per-component batch 变成新控制面；专用引擎仍可能更简单。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-12688:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.12688v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-12688:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-05-inference-system/53-kserve-llm.md`，Review notes 前正文锚点 `组件与 Ownership` 已承载长期命题；source 仅作受限证据。

### [SMSR: Certified Defence Against Runtime Memory Poisoning in Persistent LLM Agent Systems](https://arxiv.org/html/2606.12703v1)

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：Persistent memory poisoning 的 certified boundary 必须在 write-time 做 cryptographic provenance，并在 query-time 对 authenticated adversary 做 randomized ablation 与 verdict aggregation。

**State / data / control owner。** `PLATFORM-SECURITY` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.12703v1 §VII Evaluation` 支持 `15 enterprise scenarios; 3,150 repeated plus 450 production-scale trials`；模型 `Persistent RAG-agent configurations; second-agent generality check`；硬件 `Not Disclosed`；精度 `Not Disclosed`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.12703v1 §III threat model; §§IV–VI impossibility/SMSR/certificate`；counterevidence locator：`arXiv:2606.12703v1 §VIII Discussion; provenance-key and smoothing assumptions`。

**Trade-off / failure / coexistence / evolution。** HMAC 阻止 unsigned injection 不处理合法凭据滥用；smoothing 增加多次 retrieval/inference 成本且证书依赖 threat bound。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-12703:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.12703v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-12703:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-06-ai-infrastructure/72-security.md`，Review notes 前正文锚点 `从资产与信任边界开始` 已承载长期命题；source 仅作受限证据。

### [Smarter Saboteurs, Better Fixers: Scaling & Security in Linear Multi-Agent Workflows](https://arxiv.org/html/2606.12709v1)

**问题与机制。** 原筛选把《Smarter Saboteurs, Better Fixers: Scaling & Security in Linear Multi-Agent Workflows》关闭或降池；完整摘要显示“Attackers may leverage prompt-injection or jailbreaking to sabotage individual agents within MAS workflows, but the interaction between model scaling and system-level resilience remains poorly understood.”。该增量直接改变 PLATFORM-SECURITY 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`3 Methodology`；可采用的最小机制命题是：Attackers may leverage prompt-injection or jailbreaking to sabotage individual agents within MAS workflows, but the interaction between model scaling and system-level resilience remains poorly understood.

**Evaluation proof。** `3.2 Four Experimental Configurations; 3.4 Models, Benchmark, and Evaluation; 4 Results`；exact-v1 披露：Our experiments across scales of two open-weight model families on the HumanEval benchmark reveal a compliance-correction symmetry: larger models are far more likely to faithfully execute malicious instructions, with the control-to-malicious performance drop reaching 53.7pp at 27B in uncorrected pipelines.

**Limitations / non-proof。** `5.1 Limitations and Future Work`；However, appending a lightweight terminal Fixer stage collapses this to 0.6pp and restores statistical parity with control-level performance, demonstrating that strictly linear collaboration structures can be viable and resilient to adversaries at this scale, and suggesting that the brittleness previously attributed to linear topology may stem from a lack of correction. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `PLATFORM-SECURITY` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-06-ai-infrastructure/72-security.md`，Review notes 前正文锚点 `从资产与信任边界开始` 已承载长期命题；source 仅作受限证据。

### [PI-Hunter: Automated Red-Teaming for Exposing and Localizing Prompt Injections](https://arxiv.org/html/2606.12737v1)

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：Prompt-injection red team 应从 attack-success search 扩为 source-aware test construction、feedback evolution、verification 与 localization，输出可修复 attack surface。

**State / data / control owner。** `PLATFORM-SECURITY` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.12737v1 §4 Experiments; Appendices B–D` 支持 `Multiple agent benchmarks, architectures, attacks and defenses`；模型 `Agent and evaluator models disclosed in §4.1`；硬件 `Not Disclosed — hosted model hardware`；精度 `Not Disclosed`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.12737v1 §3 PI-Hunter; §§3.1–3.3`；counterevidence locator：`arXiv:2606.12737v1 §4.4 ablations; §5 Conclusion; no dedicated limitations section`。

**Trade-off / failure / coexistence / evolution。** 更广 exposure 不等于防御；搜索受 mutation/evaluator repertoire 约束，held-out attacks 与 runtime enforcement 仍必要。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-12737:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.12737v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-12737:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-06-ai-infrastructure/72-security.md`，Review notes 前正文锚点 `从资产与信任边界开始` 已承载长期命题；source 仅作受限证据。

### [Prefill Awareness in Large Language Models](https://arxiv.org/html/2606.12747v1)

**问题与机制。** 原筛选把《Prefill Awareness in Large Language Models》关闭或降池；完整摘要显示“If AI models can recognize and act on the fact their prior assistant messages have been inserted or edited, the effectiveness and validity of these methods could be compromised.”。该增量直接改变 PLATFORM-EVALUATION-SYSTEM 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`§3 Measuring Prefill Awareness; §4 Prefill Awareness in Agentic Settings`；可采用的最小机制命题是：If AI models can recognize and act on the fact their prior assistant messages have been inserted or edited, the effectiveness and validity of these methods could be compromised.

**Evaluation proof。** `§§3.2–3.3; §§4.1–4.3; Appendices A–C`；exact-v1 披露：Safety-relevant studies of language models, including alignment and jailbreaking evaluations and AI control protocols, often rely on prefilling model outputs.

**Limitations / non-proof。** `§5.1 Limitations; Appendix B.4 Formatting Artifacts`；We recommend that model developers track this capability in frontier systems. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `PLATFORM-EVALUATION-SYSTEM` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `Integrate` → `books/part-06-ai-infrastructure/66-evaluation-system.md`，Review notes 前正文锚点 `Prefill 是 Harness 输入，不是模型自然历史` 已完成写入并通过独立 post-write audit。

### [Detecting Functional Memorization in Code Language Models](https://arxiv.org/html/2606.12764v1)

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：Code training-data audit 必须检测 functional equivalence，而不能只依赖文本 overlap；应以 exposed target 对未 exposed reference 做 counterfactual execution comparison。

**State / data / control owner。** `TRAIN-DATA` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.12764v1 §4 Results; Appendices A–C/E` 支持 `Python function-signature continuations with execution-based and LLM-judge functional comparison`；模型 `OLMo-3-32B midtrained target versus pretrained reference`；硬件 `Not Disclosed`；精度 `Not Disclosed`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.12764v1 §3 Counterfactual functional memorization`；counterevidence locator：`arXiv:2606.12764v1 §4 result scope; no dedicated limitations section`。

**Trade-off / failure / coexistence / evolution。** execution 更接近语义但覆盖有限输入；LLM judge 是受 operating point 约束的 proxy，不能替代 license/provenance evidence。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-12764:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.12764v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-12764:end -->

**V3 Books Decision。** `Integrate` → `books/part-04-training-system/27-data.md`，Review notes 前正文锚点 `Code Memorization 要验证功能，而不只验证文本` 已完成写入并通过独立 post-write audit。

### [Rigel: Reverse-Engineering the Metal 4.1 Tensor Compute Path on the Apple M4 Max GPU](https://arxiv.org/html/2606.12765v1)

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：Low-precision backend contract 必须通过 checksum/provenance microbench 分离 interface support、真正加速、accumulator width、execution rail 与 fragment layout。

**State / data / control owner。** `INFER-TENSORRT-LLM` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.12765v1 §§4–8 measurements and fused-kernel result` 支持 `Metal 4.1 matmul2d microbenchmarks and fused GEMM+bias+GELU`；模型 `Metal Performance Primitives tensor path`；硬件 `Single Apple M4 Max GPU`；精度 `fp8 E4M3, fp16, accumulator ≥fp32 evidence`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.12765v1 §3 Methodology; §§4–8 characterization`；counterevidence locator：`arXiv:2606.12765v1 §10 Discussion and limitations`。

**Trade-off / failure / coexistence / evolution。** 单芯片逆向结果不能外推其他 Apple generations；fp8 在该硬件省 footprint 而非提高吞吐。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-12765:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.12765v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-12765:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-05-inference-system/49-tensorrt-llm.md`，Review notes 前正文锚点 `量化为什么不自动带来加速` 已承载长期命题；source 仅作受限证据。

### [ProPlay: Procedural World Models for Self-Evolving LLM Agents](https://arxiv.org/html/2606.12780v1)

**问题与机制。** 原筛选把《ProPlay: Procedural World Models for Self-Evolving LLM Agents》关闭或降池；完整摘要显示“We introduce ProPlay, a procedural world model that supports procedure-level preplay, where agents can rehearse future procedural paths using the learned world knowledge.”。该增量直接改变 AGENT-PLANNING 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`3 Methodology`；可采用的最小机制命题是：We introduce ProPlay, a procedural world model that supports procedure-level preplay, where agents can rehearse future procedural paths using the learned world knowledge.

**Evaluation proof。** `4 Experiments; 4.1 Experimental Setting; 4.2 Results`；exact-v1 披露：Experiments on public benchmarks show that ProPlay consistently improves environment understanding and self-evolution capability over strong baselines.

**Limitations / non-proof。** `4.4 Discussion; Limitations`；Self-evolving agents are expected to improve through interaction without external supervision, but this remains difficult in partially observable environments where agents must explore actively, learn from limited feedback, and decide when to trust prior experience. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `AGENT-PLANNING` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-07-agent/79-planning.md`，Review notes 前正文锚点 `从目标到状态图` 已承载长期命题；source 仅作受限证据。

### [The Containment Gap: How Deployed Agentic AI Frameworks Fail Public-Facing Safety Requirements](https://arxiv.org/pdf/2606.12797v1)

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍合理；该 exact-v1 改变的是：containment 必须在 perception/reasoning/execution/memory 边界分别绑定 validated write、policy gate 与 runtime monitor，而不能从 framework availability 推断 secure-by-default。

**State / data / control owner。** `PLATFORM-SECURITY` 持有该机制的 authoritative state 与 control decision；论文项目名不取得跨章节 owner。跨 owner handoff 必须绑定 identity、version、failure 与 fallback semantics。

**Evaluation：proof / non-proof。** Method locator 为 `arXiv:2606.12797v1 §2.3 Six Containment Principles; §3 Audit Methodology`；evaluation locator 为 `arXiv:2606.12797v1 §§4–5 Compliance Matrix and Experimental Validation`；counterevidence locator 为 `arXiv:2606.12797v1 §3 point-in-time audit limitation; §5.5 Limitations of Lightweight Containment`。证据只支持作者披露的 workload/model/hardware/metric，不证明生产 SLO 或跨模型、跨硬件普遍优越。

**Trade-off / failure / coexistence / evolution。** 三框架点时审计与合成 welfare agent 只证明结构缺口可被触发；regex validator 不是通用安全证明，framework 版本漂移需要重审。

<!-- claim:SF-2026-ARXIV-2606-12797:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.12797v1` 的 exact-v1 正文与本 report benchmark contract；later version/artifact 不参与本结论，ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-12797:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-06-ai-infrastructure/72-security.md`，Review notes 前正文锚点 `从资产与信任边界开始` 已承载长期命题；source 仅作受限证据。

### [LoHoSearch: Benchmarking Long-Horizon Search Agents Beyond the Human Difficulty Ceiling](https://arxiv.org/html/2606.12837v1)

**问题与机制。** 原筛选把《LoHoSearch: Benchmarking Long-Horizon Search Agents Beyond the Human Difficulty Ceiling》关闭或降池；完整摘要显示“To address this, we introduce LoHoSearch (Long-Horizon Search Agents), a challenging benchmark comprising 544 human-verified questions across 11 domains.”。该增量直接改变 PLATFORM-EVALUATION-SYSTEM 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`exact-v1 central method section`；可采用的最小机制命题是：To address this, we introduce LoHoSearch (Long-Horizon Search Agents), a challenging benchmark comprising 544 human-verified questions across 11 domains.

**Evaluation proof。** `3 Experiments; 3.1 Experimental Settings; 3.2 Main Results`；exact-v1 披露：Our evaluation demonstrates that even the strongest model achieves only 34.74% accuracy, and existing context management strategies (best +6.8%) yield far smaller gains than on prior benchmarks.

**Limitations / non-proof。** `Limitations`；Our evaluation demonstrates that even the strongest model achieves only 34.74% accuracy, and existing context management strategies (best +6.8%) yield far smaller gains than on prior benchmarks. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `PLATFORM-EVALUATION-SYSTEM` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-06-ai-infrastructure/66-evaluation-system.md`，Review notes 前正文锚点 `Evaluation Identity 必须包含 Harness 与 Environment` 已承载长期命题；source 仅作受限证据。

### [HarnessBridge: Learnable Bidirectional Controller for LLM Agent Harness](https://arxiv.org/html/2606.12882v1)

**问题与机制。** 原筛选把《HarnessBridge: Learnable Bidirectional Controller for LLM Agent Harness》关闭或降池；完整摘要显示“We introduce HarnessBridge, a lightweight learnable harness controller that parameterizes the agent--environment interface as a bidirectional projection.”。该增量直接改变 AGENT-WORKFLOW 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`3 Method`；可采用的最小机制命题是：We introduce HarnessBridge, a lightweight learnable harness controller that parameterizes the agent--environment interface as a bidirectional projection.

**Evaluation proof。** `4 Experiments; 4.1 Experiment Setup; 4.2 Main Results`；exact-v1 披露：On Terminal-Bench~2.0 and SWE-bench Verified, HarnessBridge matches or surpasses strong specialized harnesses while substantially reducing token usage and trajectory length, and generalizes from smaller generators to larger commercial models.

**Limitations / non-proof。** `Appendix E Limitation`；Large language models are increasingly deployed as agents for long-horizon tasks, yet their performance is shaped not only by model capability and environment design, but also by the harness that mediates agent--environment interaction. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `AGENT-WORKFLOW` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-07-agent/81-workflow.md`。其 bidirectional projection 是既有 harness state machine、compiler/executor 与 learned transition 合同的一种局部实现，不形成新的长期 owner、handoff 或 release contract。

### [SENTINEL: Failure-Driven Reinforcement Learning for Training Tool-Using Language Model Agents](https://arxiv.org/html/2606.12908v1)

**问题与机制。** 原筛选把《SENTINEL: Failure-Driven Reinforcement Learning for Training Tool-Using Language Model Agents》关闭或降池；完整摘要显示“We propose SENTINEL, a failure-driven reinforcement learning framework that turns the Solver's rollout failures into targeted training tasks.”。该增量直接改变 TRAIN-DATA 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`3 Method; 3.1 Problem Formulation; 3.2 Framework Overview`；可采用的最小机制命题是：We propose SENTINEL, a failure-driven reinforcement learning framework that turns the Solver's rollout failures into targeted training tasks.

**Evaluation proof。** `4 Experiments; 4.1 Experimental Setup; 4.2 Main Results`；exact-v1 披露：These results demonstrate that model failures provide an effective and scalable source of targeted training signal for improving tool-using language model agents.

**Limitations / non-proof。** `Limitations`；These results demonstrate that model failures provide an effective and scalable source of targeted training signal for improving tool-using language model agents. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `TRAIN-DATA` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-04-training-system/27-data.md`，Review notes 前正文锚点 `Data lineage 是训练可复现性的前提` 已承载长期命题；source 仅作受限证据。

### [MAStrike: Shapley-Guided Collusive Red-Teaming on Multi-Agent Systems](https://arxiv.org/html/2606.12918v1)

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍合理；该 exact-v1 改变的是：多 Agent red-team 要把 agent marginal safety contribution、coalition selection 与 role-aware collusive perturbation纳入同一 closed loop。

**State / data / control owner。** `PLATFORM-SECURITY` 持有该机制的 authoritative state 与 control decision；论文项目名不取得跨章节 owner。跨 owner handoff 必须绑定 identity、version、failure 与 fallback semantics。

**Evaluation：proof / non-proof。** Method locator 为 `arXiv:2606.12918v1 §§3–4 Shapley-guided coalition attribution and MAStrike`；evaluation locator 为 `arXiv:2606.12918v1 §5 experiments across hierarchical MAS environments`；counterevidence locator 为 `arXiv:2606.12918v1 §6 discussion/limitations and benchmark threat-model scope`。证据只支持作者披露的 workload/model/hardware/metric，不证明生产 SLO 或跨模型、跨硬件普遍优越。

**Trade-off / failure / coexistence / evolution。** Shapley 估计与因果诊断增加 calls 且依赖任务分布；合成 coalition 攻击不提供生产发生率，也不覆盖未知 topology。

<!-- claim:SF-2026-ARXIV-2606-12918:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.12918v1` 的 exact-v1 正文与本 report benchmark contract；later version/artifact 不参与本结论，ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-12918:end -->

**V3 Books Decision。** `Integrate` → `books/part-06-ai-infrastructure/72-security.md`，Review notes 前正文锚点 `Collusive Red-team 要从节点扩展到 Coalition` 已完成写入并通过独立 post-write audit。

### [MARS: Margin-Adversarial Risk-controlled Stopping for Parallel LLM Test-time Scaling](https://arxiv.org/html/2606.12935v1)

**问题与机制。** 原筛选把《MARS: Margin-Adversarial Risk-controlled Stopping for Parallel LLM Test-time Scaling》关闭或降池；完整摘要显示“Based on this observation, we introduce MARS, a margin-adversarial stopping rule that estimates which active traces are likely to change their answers and stops once the leader remains safe under a conservative bound on future vote movement.”。该增量直接改变 INFER-SCHEDULING 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`§2 Margin-Adversarial Risk-controlled Stopping; Appendix B derivation`；可采用的最小机制命题是：Based on this observation, we introduce MARS, a margin-adversarial stopping rule that estimates which active traces are likely to change their answers and stops once the leader remains safe under a conservative bound on future vote movement.

**Evaluation proof。** `§3 Experiments; Appendix E Full experimental results`；exact-v1 披露：Across three reasoning models and three competition-math benchmarks, MARS saves 25-47% of self-consistency tokens and 14-29% on top of DeepConf Online, a strong confidence-weighted baseline that already filters and truncates weak traces, while matching the accuracy of the corresponding full-budget baselines.

**Limitations / non-proof。** `Appendix F Limitations & Broader impacts`；Across three reasoning models and three competition-math benchmarks, MARS saves 25-47% of self-consistency tokens and 14-29% on top of DeepConf Online, a strong confidence-weighted baseline that already filters and truncates weak traces, while matching the accuracy of the corresponding full-budget baselines. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `INFER-SCHEDULING` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `Integrate` → `books/part-05-inference-system/56-inference-scheduling.md`，Review notes 前正文锚点 `Parallel Voting 的提前停止必须覆盖未完成 Trace 的最坏移动` 已完成写入并通过独立 post-write audit。

### [Multi-Turn Reasoning When Context Arrives in Pieces: Scalable Sharding and Memory-Augmented RL](https://arxiv.org/html/2606.12941v1)

**问题与机制。** 原筛选把《Multi-Turn Reasoning When Context Arrives in Pieces: Scalable Sharding and Memory-Augmented RL》关闭或降池；完整摘要显示“To make such training scalable, we introduce a low-cost sharding pipeline that converts single-turn QA datasets into multi-turn fragmented-information episodes, eliminating the need for hours of manual annotation.”。该增量直接改变 AGENT-MEMORY 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`3 Methodology`；可采用的最小机制命题是：To make such training scalable, we introduce a low-cost sharding pipeline that converts single-turn QA datasets into multi-turn fragmented-information episodes, eliminating the need for hours of manual annotation.

**Evaluation proof。** `4 Experimental Setup; 5 Results`；exact-v1 披露：We show that this Lost in Conversation degradation can be substantially mitigated by training models to maintain a compact rolling memory instead of attending to a growing history.

**Limitations / non-proof。** `Limitations`；Training only on sharded GSM8K, our memory-augmented policy significantly improves multi-turn accuracy and generalises zero-shot to harder math and out-of-domain long-context QA. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `AGENT-MEMORY` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-07-agent/77-memory.md`，Review notes 前正文锚点 `Consolidation 与 Forgetting` 已承载长期命题；source 仅作受限证据。

### [Learning What to Remember: A Cognitively Grounded Multi-Factor Value Model for Agentic Memory](https://arxiv.org/html/2606.12945v1)

**问题与机制。** 原筛选把《Learning What to Remember: A Cognitively Grounded Multi-Factor Value Model for Agentic Memory》关闭或降池；完整摘要显示“We propose a multi-factor memory value function V(m)=\sum_i w_i f_i(m) over seven interpretable factors (emotional intensity, goal relevance, value alignment, self/user relevance, task utility, reliability, and usage history) drawn from cognitive psychology, whose weights are learned from a downstream objective by a gradient-free optimiser, and whose single scalar uniformly controls encoding depth, forget risk, and retrieval rank.”。该增量直接改变 AGENT-MEMORY 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`Method`；可采用的最小机制命题是：We propose a multi-factor memory value function V(m)=\sum_i w_i f_i(m) over seven interpretable factors (emotional intensity, goal relevance, value alignment, self/user relevance, task utility, reliability, and usage history) drawn from cognitive psychology, whose weights are learned from a downstream objective by a gradient-free optimiser, and whose single scalar uniformly controls encoding depth, forget risk, and retrieval rank.

**Evaluation proof。** `Experiments`；exact-v1 披露：We make a methodological point: on LongMemEval, scoring goal relevance against the held-out evaluation question saturates gold-evidence retention at \approx 0.98 -- this measures retrieval, not forgetting.

**Limitations / non-proof。** `Discussion; Limitations`；The substrate is open-source; all experiments run on a single CPU with no API calls. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `AGENT-MEMORY` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-07-agent/77-memory.md`，Review notes 前正文锚点 `Consolidation 与 Forgetting` 已承载长期命题；source 仅作受限证据。

### [Maestro: Workload-Aware Cross-Cluster Scheduling for LLM-Based Multi-Agent Systems](https://arxiv.org/pdf/2606.12950v1)

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍合理；该 exact-v1 改变的是：LLM-MAS serving scheduler 必须持有 workflow/stage identity、output-length与memory预测、分层weight cache/elastic memory、跨集群routing及全局workflow priority。

**State / data / control owner。** `INFER-SCHEDULING` 持有该机制的 authoritative state 与 control decision；论文项目名不取得跨章节 owner。跨 owner handoff 必须绑定 identity、version、failure 与 fallback semantics。

**Evaluation：proof / non-proof。** Method locator 为 `arXiv:2606.12950v1 §§3–4 Maestro design and hierarchical scheduling`；evaluation locator 为 `arXiv:2606.12950v1 §§5–6 prototype and trace-driven evaluation`；counterevidence locator 为 `arXiv:2606.12950v1 No dedicated limitations section — evaluation scope and prediction/cold-start boundaries are stated in §§5–6`。证据只支持作者披露的 workload/model/hardware/metric，不证明生产 SLO 或跨模型、跨硬件普遍优越。

**Trade-off / failure / coexistence / evolution。** 预测误差、模型 churn 与跨集群网络会破坏局部最优；单集群或静态 model set 下简单队列/固定部署仍更可验证。

<!-- claim:SF-2026-ARXIV-2606-12950:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.12950v1` 的 exact-v1 正文与本 report benchmark contract；later version/artifact 不参与本结论，ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-12950:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-05-inference-system/56-inference-scheduling.md`，Review notes 前正文锚点 `Model Routing 与 Test-time Scaling 必须结算同一个 Budget` 已承载长期命题；source 仅作受限证据。

### [ScaleAcross: Designing Multi-Data-Center Infrastructure for Geo-Distributed AI Training](https://arxiv.org/html/2606.12963v1)

**问题与机制。** 原筛选把《ScaleAcross: Designing Multi-Data-Center Infrastructure for Geo-Distributed AI Training》关闭或降池；完整摘要显示“Such deployments introduce system-level challenges arising from synchronization-intensive communication, cross-site data exchange, and wide-area latency constraints.”。该增量直接改变 TRAIN-DISTRIBUTED-TRAINING 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`2.2 Scalability Limitations of Legacy VLAN Architectures; 6.4 Emulation and Evaluation Frameworks`；可采用的最小机制命题是：Such deployments introduce system-level challenges arising from synchronization-intensive communication, cross-site data exchange, and wide-area latency constraints.

**Evaluation proof。** `5 Experiments; 6.4 Emulation and Evaluation Frameworks`；exact-v1 披露：Results provide insights into traffic distribution, resilience, and infrastructure behavior in geo-distributed AI environments, highlighting the potential of reproducible multi-data-center infrastructure frameworks for scalable distributed AI training.

**Limitations / non-proof。** `2.2 Scalability Limitations of Legacy VLAN Architectures`；Results provide insights into traffic distribution, resilience, and infrastructure behavior in geo-distributed AI environments, highlighting the potential of reproducible multi-data-center infrastructure frameworks for scalable distributed AI training. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `TRAIN-DISTRIBUTED-TRAINING` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-04-training-system/36-distributed-training.md`，Review notes 前正文锚点 `跨地域电力约束会把全局同步改成层级且有陈旧度的聚合` 已承载长期命题；source 仅作受限证据。

### [Trajectory-Level Redirection Attacks on Vision-Language-Action Models](https://arxiv.org/pdf/2606.12978v1)

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍合理；该 exact-v1 改变的是：VLA 安全测试必须把 prompt 视为跨闭环复用的 trajectory control input，并以最终物理 outcome 而非单步 action/文本相似度判定 redirection。

**State / data / control owner。** `MULTIMODAL-EMBODIED-VLA` 持有该机制的 authoritative state 与 control decision；论文项目名不取得跨章节 owner。跨 owner handoff 必须绑定 identity、version、failure 与 fallback semantics。

**Evaluation：proof / non-proof。** Method locator 为 `arXiv:2606.12978v1 §§3–4 command-preserving trajectory-redirection threat model and search`；evaluation locator 为 `arXiv:2606.12978v1 §5 simulation and hardware experiments`；counterevidence locator 为 `arXiv:2606.12978v1 §6 limitations and fixed-policy/environment threat-model boundary`。证据只支持作者披露的 workload/model/hardware/metric，不证明生产 SLO 或跨模型、跨硬件普遍优越。

**Trade-off / failure / coexistence / evolution。** on-policy search成本高且依赖可 rollout 环境；有限任务与硬件结果不证明任意 VLA 可攻击，也不取代 action/runtime safety envelope。

<!-- claim:SF-2026-ARXIV-2606-12978:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.12978v1` 的 exact-v1 正文与本 report benchmark contract；later version/artifact 不参与本结论，ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-12978:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md`，Review notes 前正文锚点 `Training-only Foresight 不是 Persistent World State` 已承载长期命题；source 仅作受限证据。

### [The Illusion of Multi-Agent Advantage](https://arxiv.org/pdf/2606.13003v1)

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍合理；该 exact-v1 改变的是：MAS 评价应固定计算预算并显式检查 task decomposition/context separation/parallelism；增加 agents 或自动生成复杂 topology 不构成优势。

**State / data / control owner。** `AGENT-MULTI-AGENT` 持有该机制的 authoritative state 与 control decision；论文项目名不取得跨章节 owner。跨 owner handoff 必须绑定 identity、version、failure 与 fallback semantics。

**Evaluation：proof / non-proof。** Method locator 为 `arXiv:2606.13003v1 §§2–3 comparison protocol and diagnostic task structure`；evaluation locator 为 `arXiv:2606.13003v1 §4 SAS/MAS cost-normalized evaluation and deconstruction`；counterevidence locator 为 `arXiv:2606.13003v1 §5 limitations and benchmark/task-family scope`。证据只支持作者披露的 workload/model/hardware/metric，不证明生产 SLO 或跨模型、跨硬件普遍优越。

**Trade-off / failure / coexistence / evolution。** 现有 Ch82 已拥有 task coupling、coordinator headroom、agent-count non-monotonicity 与 single-agent fallback；该论文仅作为受限证据，不重复追加。

<!-- claim:SF-2026-ARXIV-2606-13003:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.13003v1` 的 exact-v1 正文与本 report benchmark contract；later version/artifact 不参与本结论，ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-13003:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-07-agent/82-multi-agent.md`，Review notes 前正文锚点 `Message 不是 State` 已承载长期命题；source 仅作受限证据。

### 分母前关闭（保留审计轨迹）：AI Peer Review Presentation-only Revisions

独立复核结论：该 family 的对象是 AI for Science 中的论文评审操纵；当前范围明确暂缓该阶段，以下作者侧审阅轨迹不计入 Candidate 或 Books。

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍合理；该 exact-v1 改变的是：AI reviewer release gate 必须加入 evidence-invariant presentation counterfactual，防止固定方法/结果仅靠 framing 改写评分。

**State / data / control owner。** `PLATFORM-EVALUATION-SYSTEM` 持有该机制的 authoritative state 与 control decision；论文项目名不取得跨章节 owner。跨 owner handoff 必须绑定 identity、version、failure 与 fallback semantics。

**Evaluation：proof / non-proof。** Method locator 为 `arXiv:2606.13044v1 §§3–4 adversarial-repackaging threat model and attack`；evaluation locator 为 `arXiv:2606.13044v1 §5 three-reviewer evaluation and strategy ablations`；counterevidence locator 为 `arXiv:2606.13044v1 §6 limitations and reviewer/paper-sample scope`。证据只支持作者披露的 workload/model/hardware/metric，不证明生产 SLO 或跨模型、跨硬件普遍优越。

**Trade-off / failure / coexistence / evolution。** presentation counterfactual 会增加评测成本且可能把正常清晰度改善误判为攻击；75.1% 是特定 reviewer/sample 结果，不是通用常数。

<!-- claim:SF-2026-ARXIV-2606-13044:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.13044v1` 的 exact-v1 正文与本 report benchmark contract；later version/artifact 不参与本结论，ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-13044:end -->

**V3 Books Decision。** `Pre-denominator Close — Not applicable`；保留审计轨迹但不计入 Candidate、Books 分布或 root 写入队列。

### [EA-WM: Event-Aware World Models with Task-Specification Grounding for Long-Horizon Manipulation](https://arxiv.org/pdf/2606.13053v1)

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍合理；该 exact-v1 改变的是：world-model planning 的 imagined future 必须解码为 task-grounded event/predicate state，再用progress/semantic/physical/uncertainty verifier决定 action proposal 是否可执行。

**State / data / control owner。** `MULTIMODAL-WORLD-MODELS` 持有该机制的 authoritative state 与 control decision；论文项目名不取得跨章节 owner。跨 owner handoff 必须绑定 identity、version、failure 与 fallback semantics。

**Evaluation：proof / non-proof。** Method locator 为 `arXiv:2606.13053v1 §§3–4 EA-WM event-aware model and task-specification grounding`；evaluation locator 为 `arXiv:2606.13053v1 §5 navigation/manipulation evaluations`；counterevidence locator 为 `arXiv:2606.13053v1 §6 limitations and task/predicate coverage`。证据只支持作者披露的 workload/model/hardware/metric，不证明生产 SLO 或跨模型、跨硬件普遍优越。

**Trade-off / failure / coexistence / evolution。** predicate schema 增加标注、decoder 与 calibration 成本；有限 manipulation/navigation 任务不证明开放世界 predicate 完整或物理可靠。

<!-- claim:SF-2026-ARXIV-2606-13053:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.13053v1` 的 exact-v1 正文与本 report benchmark contract；later version/artifact 不参与本结论，ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-13053:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-03-multimodal-world-models/25-multimodal-world-models.md`，Review notes 前正文锚点 `从平均预测误差到分层的 Rollout Admission` 已承载长期命题；source 仅作受限证据。

### [The Emergence of Autonomous Penetration Capabilities in Large Language Model-Powered AI Systems](https://arxiv.org/html/2606.13079v1)

**问题与机制。** 原筛选把《The Emergence of Autonomous Penetration Capabilities in Large Language Model-Powered AI Systems》关闭或降池；完整摘要显示“Within this broader red-line scenario, autonomous penetration represents a core enabling capability and subtask: the ability of LLM-powered AI systems to independently conduct adversarial operations against a target server without human intervention, identify and exploit vulnerabilities, and obtain unauthorized access or control.”。该增量直接改变 PLATFORM-EVALUATION-SYSTEM 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`3 Methods`；可采用的最小机制命题是：Within this broader red-line scenario, autonomous penetration represents a core enabling capability and subtask: the ability of LLM-powered AI systems to independently conduct adversarial operations against a target server without human intervention, identify and exploit vulnerabilities, and obtain unauthorized access or control.

**Evaluation proof。** `2.3 Evaluation targets; 3.3 Details of the experimental setups; 4 Results`；exact-v1 披露：However, existing evaluations often employ opaque methodologies, rely on unrealistic or overly simplified penetration-testing scenarios, or provide LLMs with excessive prior knowledge and task-specific guidance, and cannot accurately capture the extent to which modern AI systems can autonomously perform this core capability within broader high-impact cyberattack scenarios.

**Limitations / non-proof。** `2.2 Related works and limitations; 5 Discussion`；To address these limitations, we construct a new autonomous penetration evaluation framework consisting of two components: target servers and agent scaffolding. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `PLATFORM-EVALUATION-SYSTEM` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-06-ai-infrastructure/66-evaluation-system.md`，Review notes 前正文锚点 `Evaluation Identity 必须包含 Harness 与 Environment` 已承载长期命题；source 仅作受限证据。

### [Scale Buys Interpolation, Structure Buys a Horizon: Certified Predictability for Equivariant World Models](https://arxiv.org/pdf/2606.13092v1)

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍合理；该 exact-v1 改变的是：world-model rollout 的可信边界应由 configuration/horizon/resolution certificate 与自我 abstention 表达，不能由平均预测误差替代。

**State / data / control owner。** `MULTIMODAL-WORLD-MODELS` 持有该机制的 authoritative state 与 control decision；论文项目名不取得跨章节 owner。跨 owner handoff 必须绑定 identity、version、failure 与 fallback semantics。

**Evaluation：proof / non-proof。** Method locator 为 `arXiv:2606.13092v1 §§2–4 equivariance, orbit-transfer and Lyapunov certificates`；evaluation locator 为 `arXiv:2606.13092v1 §5 synthetic/learned/public-model evaluations`；counterevidence locator 为 `arXiv:2606.13092v1 No dedicated limitations section — certificate assumptions, held-out divergence cross-check and abstention boundary in §§2–5`。证据只支持作者披露的 workload/model/hardware/metric，不证明生产 SLO 或跨模型、跨硬件普遍优越。

**Trade-off / failure / coexistence / evolution。** exact/approximate equivariance与局部 Jacobian assumptions 限制证书；失配时必须 abstain/re-observe，不能把 candidate horizon 当安全保证。

<!-- claim:SF-2026-ARXIV-2606-13092:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.13092v1` 的 exact-v1 正文与本 report benchmark contract；later version/artifact 不参与本结论，ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-13092:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-03-multimodal-world-models/25-multimodal-world-models.md`，Review notes 前正文锚点 `从平均预测误差到分层的 Rollout Admission` 已承载长期命题；source 仅作受限证据。

### [G-Long: Graph-Enhanced Memory Management for Efficient Long-Term Dialogue Agents](https://arxiv.org/html/2606.13115v1)

**问题与机制。** 原筛选把《G-Long: Graph-Enhanced Memory Management for Efficient Long-Term Dialogue Agents》关闭或降池；完整摘要显示“To address these limitations, we propose G-Long, a graph-enhanced framework that utilizes a fine-tuned small Language Model (sLM) for structured triplet extraction and associative retrieval, significantly reducing operational costs.”。该增量直接改变 AGENT-MEMORY 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`3 Methodology; 3.1 Framework Overview; 4.5 Systematic Comparison on Diverse Memory Architectures`；可采用的最小机制命题是：To address these limitations, we propose G-Long, a graph-enhanced framework that utilizes a fine-tuned small Language Model (sLM) for structured triplet extraction and associative retrieval, significantly reducing operational costs.

**Evaluation proof。** `4 Experiments; 4.1 Experimental Setup; 4.2 Main Results on Response Generation`；exact-v1 披露：Extensive experiments across diverse benchmarks demonstrate that G-Long achieves state-of-the-art performance in both response generation and memory retrieval, yielding performance gains of up to 9.8% in response quality on MSC and 40.8% in retrieval recall on LME, while significantly minimizing computational overhead.

**Limitations / non-proof。** `Limitations`；While Large Language Models (LLMs) have advanced open-domain dialogue systems, maintaining long-term consistency remains a challenge due to inherent limitations in long-context reasoning and the inefficiency of processing extensive raw text. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `AGENT-MEMORY` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-07-agent/77-memory.md`，Review notes 前正文锚点 `Consolidation 与 Forgetting` 已承载长期命题；source 仅作受限证据。

### [EvoBrowseComp: Benchmarking Search Agents on Evolving Knowledge](https://arxiv.org/html/2606.13120v1)

**问题与机制。** 原筛选把《EvoBrowseComp: Benchmarking Search Agents on Evolving Knowledge》关闭或降池；完整摘要显示“In this paper, we introduce EvoBrowseComp, an evolving benchmark of 400 English and 400 Chinese contamination-free complex questions synthesized via live-web traversal.”。该增量直接改变 PLATFORM-EVALUATION-SYSTEM 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`exact-v1 central method section`；可采用的最小机制命题是：In this paper, we introduce EvoBrowseComp, an evolving benchmark of 400 English and 400 Chinese contamination-free complex questions synthesized via live-web traversal.

**Evaluation proof。** `2.4 Evaluation Protocol; 3 Experiments; 3.1 Experimental Setup`；exact-v1 披露：Search Agents -- large language models augmented with search tools -- have intensified the need for future-proof evaluation benchmarks.

**Limitations / non-proof。** `Limitations`；It establishes a scalable paradigm for auto-updatable, high-difficulty benchmarking that keeps pace with both evolving world knowledge and advancing agent capabilities. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `PLATFORM-EVALUATION-SYSTEM` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-06-ai-infrastructure/66-evaluation-system.md`，Review notes 前正文锚点 `Evaluation Identity 必须包含 Harness 与 Environment` 已承载长期命题；source 仅作受限证据。

### [MiniPIC: Flexible Position-Independent Caching in <100LOC](https://arxiv.org/html/2606.13126v1)

**问题与机制。** 原筛选把《MiniPIC: Flexible Position-Independent Caching in <100LOC》关闭或降池；完整摘要显示“We present Minimalistic PIC (MiniPIC): a minimal, flexible and fast vLLM design built from two ingredients: positional-encoding-free KV cache and user-controlled cache-reuse primitives.”。该增量直接改变 INFER-KV-CACHE 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`3 Methods`；可采用的最小机制命题是：We present Minimalistic PIC (MiniPIC): a minimal, flexible and fast vLLM design built from two ingredients: positional-encoding-free KV cache and user-controlled cache-reuse primitives.

**Evaluation proof。** `4 Experiments`；exact-v1 披露：On 2WikiMultihopQA, MiniPIC with interleaved scheduling improves prefill throughput by 49% over baseline vLLM, reduces cached-span time-to-first-token by up to two orders of magnitude, preserves the linear prefill scaling of uncached spans, and incurs only 5.7% worst-case overhead.

**Limitations / non-proof。** `5 Discussion and Related Work`；On 2WikiMultihopQA, MiniPIC with interleaved scheduling improves prefill throughput by 49% over baseline vLLM, reduces cached-span time-to-first-token by up to two orders of magnitude, preserves the linear prefill scaling of uncached spans, and incurs only 5.7% worst-case overhead. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `INFER-KV-CACHE` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-05-inference-system/45-why-kv-cache-speeds-up.md`，Review notes 前正文锚点 `任意 Chunk 复用必须先修复 Position 与 Conditioning Seam` 已承载长期命题；source 仅作受限证据。

### [Iterative Visual Thinking and the Self-Correction Mirage in VLM Grounding](https://arxiv.org/html/2606.13156v1)

**问题与机制。** 原筛选把《Iterative Visual Thinking and the Self-Correction Mirage in VLM Grounding》关闭或降池；完整摘要显示“A natural way to bring this to spatial grounding is visual self-correction: the model predicts a bounding box, sees it rendered on the image, and refines it over several steps.”。该增量直接改变 PLATFORM-EVALUATION-SYSTEM 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`3 Method`；可采用的最小机制命题是：A natural way to bring this to spatial grounding is visual self-correction: the model predicts a bounding box, sees it rendered on the image, and refines it over several steps.

**Evaluation proof。** `4 Experiments; 4.2 Main Results; 4.4 Qualitative Results`；exact-v1 披露：We show this gain is a measurement mirage.

**Limitations / non-proof。** `4.5 Limitations`；Self-verification confidence correlates only weakly with correctness (r about 0.22), and a counterfactual overlay shows the loop reacts to the presence of a rendered box rather than its correctness. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `PLATFORM-EVALUATION-SYSTEM` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-06-ai-infrastructure/66-evaluation-system.md`，Review notes 前正文锚点 `Evaluation Identity 必须包含 Harness 与 Environment` 已承载长期命题；source 仅作受限证据。

### [Getting Better at Working With You: Compiling User Corrections into Runtime Enforcement for Coding Agents](https://arxiv.org/pdf/2606.13174v1)

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍合理；该 exact-v1 改变的是：用户 correction 只有被编译为 atomic rule 与 pre-completion runtime check 才能跨 session 成为 enforcement；memory lookup 仍只是 preference evidence。

**State / data / control owner。** `AGENT-WORKFLOW` 持有该机制的 authoritative state 与 control decision；论文项目名不取得跨章节 owner。跨 owner handoff 必须绑定 identity、version、failure 与 fallback semantics。

**Evaluation：proof / non-proof。** Method locator 为 `arXiv:2606.13174v1 §§3–4 TRACE rule acquisition and compiled enforcement`；evaluation locator 为 `arXiv:2606.13174v1 §5 ClawArena/MemoryArena-derived evaluation`；counterevidence locator 为 `arXiv:2606.13174v1 §6 limitations and simulated-user/task-distribution scope`。证据只支持作者披露的 workload/model/hardware/metric，不证明生产 SLO 或跨模型、跨硬件普遍优越。

**Trade-off / failure / coexistence / evolution。** 自动抽取可能误编译或过度约束，需 version/supersession/disable；模拟用户结果不证明真实用户长期满意度。

<!-- claim:SF-2026-ARXIV-2606-13174:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.13174v1` 的 exact-v1 正文与本 report benchmark contract；later version/artifact 不参与本结论，ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-13174:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-07-agent/81-workflow.md`，Review notes 前正文锚点 `State Machine 是基本模型` 已承载长期命题；source 仅作受限证据。

### [MemRefine: LLM-Guided Compression for Long-Term Agent Memory](https://arxiv.org/html/2606.13177v1)

**问题与机制。** 原筛选把《MemRefine: LLM-Guided Compression for Long-Term Agent Memory》关闭或降池；完整摘要显示“However, as interactions accumulate, the memory store grows without bound and fills with redundant entries that inflate storage cost and degrade retrieval by crowding out the most useful evidence.”。该增量直接改变 AGENT-MEMORY 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`3 Method; 3.1 Problem Formulation`；可采用的最小机制命题是：However, as interactions accumulate, the memory store grows without bound and fills with redundant entries that inflate storage cost and degrade retrieval by crowding out the most useful evidence.

**Evaluation proof。** `4 Experimental Setup; 5 Experimental Results and Analysis; Appendix F Category-wise LoCoMo Results`；exact-v1 披露：Across multiple memory frameworks and long-term conversation benchmarks, MemRefine consistently meets target budgets while preserving downstream performance and outperforming rule-based baselines under tight budgets.

**Limitations / non-proof。** `Limitations`；To this end, we then propose MemRefine, an LLM-guided framework that, since surface similarity poorly reflects factual value, uses similarity only to propose candidate pairs and defers delete, merge, and preserve decisions to an LLM judge based on factual content, iterating until the budget is met. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `AGENT-MEMORY` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-07-agent/77-memory.md`，Review notes 前正文锚点 `Consolidation 与 Forgetting` 已承载长期命题；source 仅作受限证据。

### [LLM-as-an-Investigator: Evidence-First Reasoning for Robust Interactive Problem Diagnosis](https://arxiv.org/html/2606.13220v1)

**问题与机制。** 原筛选把《LLM-as-an-Investigator: Evidence-First Reasoning for Robust Interactive Problem Diagnosis》关闭或降池；完整摘要显示“However, when users provide incomplete descriptions or plausible but unverified explanations, LLMs may prematurely align with these assumptions and propose solutions before collecting sufficient evidence.”。该增量直接改变 AGENT-PLANNING 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`4 Methodology`；可采用的最小机制命题是：However, when users provide incomplete descriptions or plausible but unverified explanations, LLMs may prematurely align with these assumptions and propose solutions before collecting sufficient evidence.

**Evaluation proof。** `3 Case study; 5 Experimental Results; 5.2 Evaluation Pipeline and Experimental Settings`；exact-v1 披露：We use a three-agent evaluation pipeline in which a Problem-Solution Extractor Agent converts solved threads into structured cases, a Ground-Truth Evaluator Agent simulates the user while hiding the known solution, and the tested assistant attempts to recover the solution through dialogue.

**Limitations / non-proof。** `未定位独立 limitations；边界由 exact-v1 披露 workload 推得`；The results show that the proposed approach identifies the problem more accurately than direct prompting and reasoning-only baselines, while its evidence-first protocol helps reduce user-induced conversational bias. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `AGENT-PLANNING` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-07-agent/79-planning.md`，Review notes 前正文锚点 `从目标到状态图` 已承载长期命题；source 仅作受限证据。

### [From Uncertain Judgments to Calibrated Rankings: Conformal Elo Estimation for LLM Evaluation](https://arxiv.org/html/2606.13221v1)

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍合理；该 exact-v1 改变的是：LLM-judge ranking 需要先把 per-battle score difference校准为 win probability，再对 judge-human Elo residual做 split-conformal interval。

**State / data / control owner。** `PLATFORM-EVALUATION-SYSTEM` 持有该机制的 authoritative state 与 control decision；论文项目名不取得跨章节 owner。跨 owner handoff 必须绑定 identity、version、failure 与 fallback semantics。

**Evaluation：proof / non-proof。** Method locator 为 `arXiv:2606.13221v1 §§3–4 probabilistic Bradley-Terry and conformal Elo`；evaluation locator 为 `arXiv:2606.13221v1 §5 LMArena held-out-model evaluation`；counterevidence locator 为 `arXiv:2606.13221v1 No dedicated limitations section — marginal-coverage/exchangeability and judge-distribution boundaries in §§3–5`。证据只支持作者披露的 workload/model/hardware/metric，不证明生产 SLO 或跨模型、跨硬件普遍优越。

**Trade-off / failure / coexistence / evolution。** conformal interval只给交换性条件下边际 coverage，不消除 position/self-preference/intransitivity，也不替代关键 release 的 human audit。

<!-- claim:SF-2026-ARXIV-2606-13221:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.13221v1` 的 exact-v1 正文与本 report benchmark contract；later version/artifact 不参与本结论，ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-13221:end -->

**V3 Books Decision。** `Integrate` → `books/part-06-ai-infrastructure/66-evaluation-system.md`，Review notes 前正文锚点 `Judge Ranking 要同时校准局部比较与全局区间` 已完成写入并通过独立 post-write audit。

### 分母前关闭（保留审计轨迹）：Agentic AI Adoption and Software Architecture

独立复核结论：该 family 测量 AI coding adoption 后的软件架构结果，不改变大模型或 LLM Infra 的 state/data/control ownership、运行机制或 evaluation/release contract，以下作者侧审阅轨迹不计入 Candidate 或 Books。

**问题与机制。** 原筛选把《Mining Architectural Quality Under Agentic AI Adoption: A Causal Study of Java Repositories》关闭或降池；完整摘要显示“Yet causal evidence on their effect on software architecture is scarce.”。该增量直接改变 AGENT-WORKFLOW 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`5.2 A Methodological Lesson for Density-Normalized Mining Outcomes`；可采用的最小机制命题是：Yet causal evidence on their effect on software architecture is scarce.

**Evaluation proof。** `4 Results`；exact-v1 披露：The complete replication package, including the curated 151-repository monthly panel, is publicly available.

**Limitations / non-proof。** `5 Discussion; 6 Threats to Validity`；The complete replication package, including the curated 151-repository monthly panel, is publicly available. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `AGENT-WORKFLOW` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `Pre-denominator Close — Not applicable`；保留审计轨迹但不计入 Candidate、Books 分布或 root 写入队列。

### [SkillCAT: Contrastive, Assessment-Augmented and Topology-AwareSkill Self-Evolution for LLM Agents](https://arxiv.org/html/2606.13317v1)

**问题与机制。** 原筛选把《SkillCAT: Contrastive, Assessment-Augmented and Topology-AwareSkill Self-Evolution for LLM Agents》关闭或降池；完整摘要显示“We propose SkillCAT, a framework that decomposes this process into three stages. (1) Contrastive Causal Extraction (CCE) samples multiple trajectories per task and contrasts same-task success/failure pairs to find the evidence that explains outcome differences. (2) Assessment-Augmented Evolution (AAE) replays each candidate patch on source-task clones, retains only those that do not damage task outcomes, and then merges the retained patches hierarchically. (3) Topology-Aware Task Execution (TTE) compiles the evolved skills into routable sub-skill topologies, so that inference loads only task-relevant capability nodes.”。该增量直接改变 AGENT-WORKFLOW 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`Method; Problem Formulation`；可采用的最小机制命题是：We propose SkillCAT, a framework that decomposes this process into three stages. (1) Contrastive Causal Extraction (CCE) samples multiple trajectories per task and contrasts same-task success/failure pairs to find the evidence that explains outcome differences. (2) Assessment-Augmented Evolution (AAE) replays each candidate patch on source-task clones, retains only those that do not damage task outcomes, and then merges the retained patches hierarchically. (3) Topology-Aware Task Execution (TTE) compiles the evolved skills into routable sub-skill topologies, so that inference loads only task-relevant capability nodes.

**Evaluation proof。** `Experiments; Experimental Setup; Main Results`；exact-v1 披露：We evaluate SkillCAT on widely-used agent benchmarks, including SpreadsheetBench, WikiTableQuestions, and DocVQA, and further assess cross-model and out-of-distribution generalization.

**Limitations / non-proof。** `未定位独立 limitations；边界由 exact-v1 披露 workload 推得`；We propose SkillCAT, a framework that decomposes this process into three stages. (1) Contrastive Causal Extraction (CCE) samples multiple trajectories per task and contrasts same-task success/failure pairs to find the evidence that explains outcome differences. (2) Assessment-Augmented Evolution (AAE) replays each candidate patch on source-task clones, retains only those that do not damage task outcomes, and then merges the retained patches hierarchically. (3) Topology-Aware Task Execution (TTE) compiles the evolved skills into routable sub-skill topologies, so that inference loads only task-relevant capability nodes. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `AGENT-WORKFLOW` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-07-agent/81-workflow.md`，Review notes 前正文锚点 `Trial Evidence 不能直接提交为 Workflow Revision` 已承载长期命题；source 仅作受限证据。

### [Can I Buy Your KV Cache?](https://arxiv.org/html/2606.13361v1)

**问题与机制。** 原筛选把《Can I Buy Your KV Cache?》关闭或降池；完整摘要显示“Every agent re-runs prefill, the most compute-intensive step a large model takes, over identical text, only to rebuild a key-value (KV) cache identical to the one the agent before it just built.”。该增量直接改变 INFER-PREFILL 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`4 Method`；可采用的最小机制命题是：Every agent re-runs prefill, the most compute-intensive step a large model takes, over identical text, only to rebuild a key-value (KV) cache identical to the one the agent before it just built.

**Evaluation proof。** `6 Experiments`；exact-v1 披露：We frame the resulting agent-native prefill CDN and leave lossless KV compression and a cross-party payment layer as the open problems.

**Limitations / non-proof。** `7 Discussion: a prefill CDN for the agent economy; 8 Limitations`；Every agent re-runs prefill, the most compute-intensive step a large model takes, over identical text, only to rebuild a key-value (KV) cache identical to the one the agent before it just built. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `INFER-PREFILL` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `Only report`；该 exact-v1 仅支持受限案例，尚不足以改变长期 Books 机制链，不创建正文或 trace 采用链。

### [Who Pays the Price? Stakeholder-Centric Prompt Injection Benchmarking for Real-world Web Agents](https://arxiv.org/html/2606.13385v1)

**问题与机制。** 原筛选把《Who Pays the Price? Stakeholder-Centric Prompt Injection Benchmarking for Real-world Web Agents》关闭或降池；完整摘要显示“To capture these properties, we introduce StakeBench, a stakeholder-centric benchmark that systematically categorizes and attributes harm in real-world web agent systems for online shopping.”。该增量直接改变 PLATFORM-SECURITY 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`exact-v1 central method section`；可采用的最小机制命题是：To capture these properties, we introduce StakeBench, a stakeholder-centric benchmark that systematically categorizes and attributes harm in real-world web agent systems for online shopping.

**Evaluation proof。** `3.3 Evaluation Metrics; 4.2 Main Results; Appendix F Automated Evaluation Protocol and Annotation Guidelines`；exact-v1 披露：Evaluating four deployable agent-backbone configurations across 3,168 attacked runs, we find substantial and heterogeneous vulnerabilities: no attack objective is reliably resisted by current LLM-based web agents, and outcomes span four qualitatively distinct modes.

**Limitations / non-proof。** `B.4 Attacker Limitations; Appendix I Limitations and Future Directions`；These patterns are missed by conventional attack-centric, single-metric evaluation, underscoring the need for stakeholder-aware assessment of LLM-based agents in real-world deployments. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `PLATFORM-SECURITY` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-06-ai-infrastructure/72-security.md`，Review notes 前正文锚点 `从资产与信任边界开始` 已承载长期命题；source 仅作受限证据。

### [MiniMax Sparse Attention](https://arxiv.org/pdf/2606.13392v1)

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍合理；该 exact-v1 改变的是：blockwise sparse attention 要把 per-GQA-group index branch、exact selected-block attention 与 GPU-efficient Top-k/KV-outer execution共同设计。

**State / data / control owner。** `MODEL-LONG-CONTEXT` 持有该机制的 authoritative state 与 control decision；论文项目名不取得跨章节 owner。跨 owner handoff 必须绑定 identity、version、failure 与 fallback semantics。

**Evaluation：proof / non-proof。** Method locator 为 `arXiv:2606.13392v1 §§3–4 MiniMax Sparse Attention architecture and kernels`；evaluation locator 为 `arXiv:2606.13392v1 §5 long-context/model evaluation`；counterevidence locator 为 `arXiv:2606.13392v1 §6 limitations and disclosed model/hardware scope`。证据只支持作者披露的 workload/model/hardware/metric，不证明生产 SLO 或跨模型、跨硬件普遍优越。

**Trade-off / failure / coexistence / evolution。** Ch22 已有 MSA 机制、GQA group selection 与受限实验边界，并含 exact family citation；不重复追加。

<!-- claim:SF-2026-ARXIV-2606-13392:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.13392v1` 的 exact-v1 正文与本 report benchmark contract；later version/artifact 不参与本结论，ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-13392:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-02-model/22-long-context.md`，Review notes 前正文锚点 `方案究竟移动了哪个瓶颈` 已承载长期命题；source 仅作受限证据。

### [Accelerating Speculative Diffusions via Block Verification](https://arxiv.org/pdf/2606.13426v1)

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍合理；该 exact-v1 改变的是：diffusion model 的 speculative block proposal 必须由 target-model block verifier统一 commit/rollback，才能把并行候选与 exact output distribution 分开。

**State / data / control owner。** `MULTIMODAL-GENERATIVE-PARADIGMS` 持有该机制的 authoritative state 与 control decision；论文项目名不取得跨章节 owner。跨 owner handoff 必须绑定 identity、version、failure 与 fallback semantics。

**Evaluation：proof / non-proof。** Method locator 为 `arXiv:2606.13426v1 §§3–4 speculative diffusion block proposal and verification`；evaluation locator 为 `arXiv:2606.13426v1 §5 image-generation evaluation`；counterevidence locator 为 `arXiv:2606.13426v1 §6 limitations and model/sampler/hardware scope`。证据只支持作者披露的 workload/model/hardware/metric，不证明生产 SLO 或跨模型、跨硬件普遍优越。

**Trade-off / failure / coexistence / evolution。** 大 block 提升并行度却放大 rejection与临时 state；有限 DiT/sampler 结果不证明任意 diffusion workload 加速。

<!-- claim:SF-2026-ARXIV-2606-13426:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.13426v1` 的 exact-v1 正文与本 report benchmark contract；later version/artifact 不参与本结论，ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-13426:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md`，Review notes 前正文锚点 `Draft、Verify 与 Correct 不是同一件事` 已承载长期命题；source 仅作受限证据。

### [CQC-RAG: Robust Retrieval-Augmented Generation via Cross-Query Consistency](https://arxiv.org/html/2606.13438v1)

**问题与机制。** 原筛选把《CQC-RAG: Robust Retrieval-Augmented Generation via Cross-Query Consistency》关闭或降池；完整摘要显示“To address these limitations, we propose a Cross-Query Consistency Hypothesis: correct answers tend to maintain high confidence across semantically equivalent but syntactically diverse queries, whereas noise-induced hallucinations exhibit unstable confidence under such query variations.”。该增量直接改变 AGENT-RAG 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`3. Methodology`；可采用的最小机制命题是：To address these limitations, we propose a Cross-Query Consistency Hypothesis: correct answers tend to maintain high confidence across semantically equivalent but syntactically diverse queries, whereas noise-induced hallucinations exhibit unstable confidence under such query variations.

**Evaluation proof。** `2.2. Discriminative Answer Evaluation; 4. Experiments; 4.1. Datasets and Evaluation Metrics`；exact-v1 披露：Semantically equivalent queries with different syntactic forms may lead to different retrieval results, while irrelevant or misleading documents can further induce hallucinated answers.

**Limitations / non-proof。** `未定位独立 limitations；边界由 exact-v1 披露 workload 推得`；Existing multi-path reasoning methods improve robustness by sampling multiple candidate answers and applying voting- or confidence-based selection, but they still face two limitations: diversity is often injected through uncontrollable decoding randomness, and answer evaluation is usually confined to a single query-induced evidence view. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `AGENT-RAG` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-07-agent/76-rag.md`，Review notes 前正文锚点 `Online Retrieval Pipeline` 已承载长期命题；source 仅作受限证据。

### [Toward Instructions-as-Code: Understanding the Impact of Instruction Files on Agentic Pull Requests](https://arxiv.org/pdf/2606.13449v1)

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍合理；该 exact-v1 改变的是：repository instruction 文件是可执行 control surface；评价必须区分规则存在、被读取、进入 context、被遵守与最终 outcome。

**State / data / control owner。** `AGENT-PROMPT` 持有该机制的 authoritative state 与 control decision；论文项目名不取得跨章节 owner。跨 owner handoff 必须绑定 identity、version、failure 与 fallback semantics。

**Evaluation：proof / non-proof。** Method locator 为 `arXiv:2606.13449v1 §§3–4 instructions-as-code taxonomy and instrumentation`；evaluation locator 为 `arXiv:2606.13449v1 §5 repository/coding-agent experiments`；counterevidence locator 为 `arXiv:2606.13449v1 §6 limitations and harness/model/repository scope`。证据只支持作者披露的 workload/model/hardware/metric，不证明生产 SLO 或跨模型、跨硬件普遍优越。

**Trade-off / failure / coexistence / evolution。** 更强 instruction 提高一致性也会固化陈旧约束、扩大 context与冲突；观察到 compliance 不证明 effect correctness。

<!-- claim:SF-2026-ARXIV-2606-13449:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.13449v1` 的 exact-v1 正文与本 report benchmark contract；later version/artifact 不参与本结论，ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-13449:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-07-agent/74-prompt.md`，Review notes 前正文锚点 `Prompt 生命周期` 已承载长期命题；source 仅作受限证据。

### [Budget-Constrained Step-Level Diffusion Caching](https://arxiv.org/pdf/2606.13496v1)

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍合理；该 exact-v1 改变的是：diffusion serving cache 应把 denoising step、state identity 与误差预算绑定，在 step-level reuse 与 recompute 间动态选择。

**State / data / control owner。** `MULTIMODAL-GENERATIVE-PARADIGMS` 持有该机制的 authoritative state 与 control decision；论文项目名不取得跨章节 owner。跨 owner handoff 必须绑定 identity、version、failure 与 fallback semantics。

**Evaluation：proof / non-proof。** Method locator 为 `arXiv:2606.13496v1 §§3–4 step-level diffusion caching mechanism`；evaluation locator 为 `arXiv:2606.13496v1 §5 quality/latency evaluation`；counterevidence locator 为 `arXiv:2606.13496v1 §6 limitations and model/workload calibration scope`。证据只支持作者披露的 workload/model/hardware/metric，不证明生产 SLO 或跨模型、跨硬件普遍优越。

**Trade-off / failure / coexistence / evolution。** cache hit以漂移和额外 metadata换算力；阈值绑定模型、prompt与scheduler，分布漂移时必须回退完整 denoising。

<!-- claim:SF-2026-ARXIV-2606-13496:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.13496v1` 的 exact-v1 正文与本 report benchmark contract；later version/artifact 不参与本结论，ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-13496:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md`，Review notes 前正文锚点 `Draft、Verify 与 Correct 不是同一件事` 已承载长期命题；source 仅作受限证据。

### [GF-DiT: Scheduling Parallelism for Diffusion Transformer Serving](https://arxiv.org/pdf/2606.13501v1)

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍合理；该 exact-v1 改变的是：Diffusion Transformer serving 应联合管理 request phase、denoising-step work、cache locality 与 batch admission，而非套用自回归 token scheduler。

**State / data / control owner。** `INFER-SCHEDULING` 持有该机制的 authoritative state 与 control decision；论文项目名不取得跨章节 owner。跨 owner handoff 必须绑定 identity、version、failure 与 fallback semantics。

**Evaluation：proof / non-proof。** Method locator 为 `arXiv:2606.13501v1 §§3–5 abstraction, group-free collectives and implementation`；evaluation locator 为 `arXiv:2606.13501v1 §6 Evaluation`；counterevidence locator 为 `arXiv:2606.13501v1 §4.2 ordering scope; §6 experimental setup, baselines and failure boundaries (especially §§6.5–6.6); no dedicated Limitations section`。证据只支持作者披露的 workload/model/hardware/metric，不证明生产 SLO 或跨模型、跨硬件普遍优越。

**Trade-off / failure / coexistence / evolution。** phase-aware batching降低空洞但增加 prediction/state migration；作者 workload 的吞吐/延迟不构成生产 SLO。

<!-- claim:SF-2026-ARXIV-2606-13501:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.13501v1` 的 exact-v1 正文与本 report benchmark contract；later version/artifact 不参与本结论，ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-13501:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-05-inference-system/56-inference-scheduling.md`，Review notes 前正文锚点 `迭代生成与流式会话需要显式 Progress State` 已承载长期命题；source 仅作受限证据。

### [Multiagent Protocols with Aggregated Confidence Signals](https://arxiv.org/html/2606.13591v1)

**问题与机制。** 原筛选把《Multiagent Protocols with Aggregated Confidence Signals》关闭或降池；完整摘要显示“We introduce three protocols that produce a final answer along with a single aggregated confidence by first transforming raw confidence signals to make them comparable across models, then combining them via soft voting or a probability fusion we call Bayesian fusion.”。该增量直接改变 AGENT-MULTI-AGENT 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`3 Methods; 3.3 Confidence Calibration Methods`；可采用的最小机制命题是：We introduce three protocols that produce a final answer along with a single aggregated confidence by first transforming raw confidence signals to make them comparable across models, then combining them via soft voting or a probability fusion we call Bayesian fusion.

**Evaluation proof。** `4 Experimental Setup; 4.1 Evaluation; 5 Results`；exact-v1 披露：Analyzing two estimators, sequence probability and self-report, alongside parametric and non-parametric calibrators, we find that calibration improves F1 for both estimators while AUARC is less reliant on it.

**Limitations / non-proof。** `7 Limitations`；We evaluate six homogeneous and heterogeneous debating pairs per benchmark, across five benchmarks and four task types, spanning a range of model capabilities and sizes. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `AGENT-MULTI-AGENT` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-07-agent/82-multi-agent.md`，Review notes 前正文锚点 `Message 不是 State` 已承载长期命题；source 仅作受限证据。

### [See What I See, Know What I Think: Dense Latent Communication Across Heterogeneous Agents](https://arxiv.org/html/2606.13594v1)

**问题与机制。** 原筛选把《See What I See, Know What I Think: Dense Latent Communication Across Heterogeneous Agents》关闭或降池；完整摘要显示“Motivated by this, we propose dense alignment for heterogeneous KV-cache communication via a lightweight cross-model cache transformation and two-phase training: reconstruction followed by generation.”。该增量直接改变 AGENT-MULTI-AGENT 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`4.2 Architecture Design: Heterogeneous Dense Cache Alignment`；可采用的最小机制命题是：Motivated by this, we propose dense alignment for heterogeneous KV-cache communication via a lightweight cross-model cache transformation and two-phase training: reconstruction followed by generation.

**Evaluation proof。** `5 Experiments; 5.1 Context-aware Results; 5.2 Context-unaware Results`；exact-v1 披露：Across all six directions of {Qwen3-4B, 8B, 14B} and six in-domain and out-of-domain benchmarks, our method outperforms prior heterogeneous baselines, matches or exceeds text communication in context-aware settings at roughly 2 to 3 times lower compute, and remains effective in context-unaware transfer where prior methods collapse.

**Limitations / non-proof。** `未定位独立 limitations；边界由 exact-v1 披露 workload 推得`；Across all six directions of {Qwen3-4B, 8B, 14B} and six in-domain and out-of-domain benchmarks, our method outperforms prior heterogeneous baselines, matches or exceeds text communication in context-aware settings at roughly 2 to 3 times lower compute, and remains effective in context-unaware transfer where prior methods collapse. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `AGENT-MULTI-AGENT` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `Integrate` → `books/part-07-agent/82-multi-agent.md`，Review notes 前正文锚点 `Latent Communication 只能压缩 Payload，不能隐藏 Identity` 已完成写入并通过独立 post-write audit。

### [Reward Modeling for Multi-Agent Orchestration](https://arxiv.org/html/2606.13598v1)

**问题与机制。** 原筛选把《Reward Modeling for Multi-Agent Orchestration》关闭或降池；完整摘要显示“We propose Orchestration Reward Modeling (OrchRM), a self-supervised framework for evaluating orchestration quality without human annotations.”。该增量直接改变 AGENT-MULTI-AGENT 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`3 Methodology`；可采用的最小机制命题是：We propose Orchestration Reward Modeling (OrchRM), a self-supervised framework for evaluating orchestration quality without human annotations.

**Evaluation proof。** `4 Experiments; 4.1 Experimental Setup`；exact-v1 披露：Code will be available at https://github.com/Wang-ML-Lab/OrchRM.

**Limitations / non-proof。** `Appendix A Limitations and Broader Impact`；Multi-Agent Systems (MAS) built on Large Language Models (LLMs) require effective orchestration to coordinate specialized agents, yet training such orchestrators is hindered by limited supervision and high computational cost. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `AGENT-MULTI-AGENT` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-07-agent/82-multi-agent.md`。其 self-supervised intermediate-artifact reward model 是既有 dynamic topology、typed credit、critical-path reward 与 role obligation 的局部训练配方，不形成新的长期机制链。

### [AgentBeats: Agentifying Agent Assessment for Openness, Standardization, and Reproducibility](https://arxiv.org/pdf/2606.13608v1)

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍合理；该 exact-v1 改变的是：Agent benchmark 应把 task/environment/evaluator protocol做成可部署 assessment contract，并保存run identity、submission与verdict lineage。

**State / data / control owner。** `PLATFORM-EVALUATION-SYSTEM` 持有该机制的 authoritative state 与 control decision；论文项目名不取得跨章节 owner。跨 owner handoff 必须绑定 identity、version、failure 与 fallback semantics。

**Evaluation：proof / non-proof。** Method locator 为 `arXiv:2606.13608v1 §§3–4 AgentBeats protocol and platform`；evaluation locator 为 `arXiv:2606.13608v1 §5 benchmark deployment/case-study evaluation`；counterevidence locator 为 `arXiv:2606.13608v1 §6 limitations and supported environment/protocol scope`。证据只支持作者披露的 workload/model/hardware/metric，不证明生产 SLO 或跨模型、跨硬件普遍优越。

**Trade-off / failure / coexistence / evolution。** 平台统一降低接线成本却扩大 evaluator/control-plane TCB；可运行 benchmark 不证明 judge、任务或环境代表真实生产。

<!-- claim:SF-2026-ARXIV-2606-13608:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.13608v1` 的 exact-v1 正文与本 report benchmark contract；later version/artifact 不参与本结论，ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-13608:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-06-ai-infrastructure/66-evaluation-system.md`，Review notes 前正文锚点 `Evaluation Identity 必须包含 Harness 与 Environment` 已承载长期命题；source 仅作受限证据。

### [One Polluted Page Is Enough: Evaluating Web Content Pollution in LLM Recommenders](https://arxiv.org/pdf/2606.13610v1)

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍合理；该 exact-v1 改变的是：web-connected Agent 的安全评测必须冻结污染时间线与 attacker publishing budget，测量 retriever/index/reader 怎样把公开内容变成控制输入。

**State / data / control owner。** `PLATFORM-SECURITY` 持有该机制的 authoritative state 与 control decision；论文项目名不取得跨章节 owner。跨 owner handoff 必须绑定 identity、version、failure 与 fallback semantics。

**Evaluation：proof / non-proof。** Method locator 为 `arXiv:2606.13610v1 §§3–4 content-pollution threat model and benchmark`；evaluation locator 为 `arXiv:2606.13610v1 §5 retrieval/agent attack evaluation`；counterevidence locator 为 `arXiv:2606.13610v1 §6 limitations and web-corpus/model cutoff scope`。证据只支持作者披露的 workload/model/hardware/metric，不证明生产 SLO 或跨模型、跨硬件普遍优越。

**Trade-off / failure / coexistence / evolution。** 污染 benchmark会随搜索索引与网页变化而漂移；有限页面与模型不能给真实攻击发生率，source trust/authorization仍需独立控制。

<!-- claim:SF-2026-ARXIV-2606-13610:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.13610v1` 的 exact-v1 正文与本 report benchmark contract；later version/artifact 不参与本结论，ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-13610:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-06-ai-infrastructure/72-security.md`，Review notes 前正文锚点 `从资产与信任边界开始` 已承载长期命题；source 仅作受限证据。

### [Valid Inference with Synthetic Data via Task Exchangeability](https://arxiv.org/html/2606.13629v1)

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍合理；该 exact-v1 改变的是：synthetic-data inference 必须把 generator、selection/filter与downstream sample视为同一随机过程，并检验 task-level exchangeability 后才报告置信区间。

**State / data / control owner。** `PLATFORM-EVALUATION-SYSTEM` 持有该机制的 authoritative state 与 control decision；论文项目名不取得跨章节 owner。跨 owner handoff 必须绑定 identity、version、failure 与 fallback semantics。

**Evaluation：proof / non-proof。** Method locator 为 `arXiv:2606.13629v1 §§2–4 task-exchangeability framework and estimators`；evaluation locator 为 `arXiv:2606.13629v1 §5 synthetic-data experiments`；counterevidence locator 为 `arXiv:2606.13629v1 §6 limitations and exchangeability/model-generator assumptions`。证据只支持作者披露的 workload/model/hardware/metric，不证明生产 SLO 或跨模型、跨硬件普遍优越。

**Trade-off / failure / coexistence / evolution。** 有效区间依赖 exchangeability/independence 近似；generator drift、adaptive filtering与leakage会破坏 coverage，点估计不能替代。

<!-- claim:SF-2026-ARXIV-2606-13629:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.13629v1` 的 exact-v1 正文与本 report benchmark contract；later version/artifact 不参与本结论，ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-13629:end -->

**V3 Books Decision。** `Integrate` → `books/part-06-ai-infrastructure/66-evaluation-system.md`，Review notes 前正文锚点 `Synthetic Evidence 只有在 Task Exchangeability 成立时才能进入推断` 已完成写入并通过独立 post-write audit。

### [Recursive Agent Harnesses](https://arxiv.org/pdf/2606.13643v1)

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍合理；该 exact-v1 改变的是：recursive harness improvement 必须把 harness revision当受控 artifact，以相邻 revision、fixed evaluator与rollback做局部搜索。

**State / data / control owner。** `AGENT-WORKFLOW` 持有该机制的 authoritative state 与 control decision；论文项目名不取得跨章节 owner。跨 owner handoff 必须绑定 identity、version、failure 与 fallback semantics。

**Evaluation：proof / non-proof。** Method locator 为 `arXiv:2606.13643v1 §§3–4 recursive harness search and revision protocol`；evaluation locator 为 `arXiv:2606.13643v1 §5 controlled task evaluation`；counterevidence locator 为 `arXiv:2606.13643v1 §6 limitations and evaluator/harness-search scope`。证据只支持作者披露的 workload/model/hardware/metric，不证明生产 SLO 或跨模型、跨硬件普遍优越。

**Trade-off / failure / coexistence / evolution。** Ch81 已有 recursive harness self-improvement、durable workflow与terminal verifier；不复制论文特定 search recipe。

<!-- claim:SF-2026-ARXIV-2606-13643:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.13643v1` 的 exact-v1 正文与本 report benchmark contract；later version/artifact 不参与本结论，ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-13643:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-07-agent/81-workflow.md`，Review notes 前正文锚点 `State Machine 是基本模型` 已承载长期命题；source 仅作受限证据。

### 分母前关闭（保留审计轨迹）：Autonomous Scientific Discovery Environment Engineering

独立复核结论：该 family 的对象是 autonomous scientific discovery；AI for Science 当前明确暂缓，且其 proposal-validation-promotion 结构已是通用 workflow 合同，以下作者侧审阅轨迹不计入 Candidate 或 Books。

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍合理；该 exact-v1 改变的是：Agent 自改进需要把 candidate skill/workflow artifact、evaluator result与promotion gate分离，失败 proposal不得直接覆盖运行时。

**State / data / control owner。** `AGENT-WORKFLOW` 持有该机制的 authoritative state 与 control decision；论文项目名不取得跨章节 owner。跨 owner handoff 必须绑定 identity、version、failure 与 fallback semantics。

**Evaluation：proof / non-proof。** Method locator 为 `arXiv:2606.13662v1 §§3–4 EurekAgent self-improvement loop`；evaluation locator 为 `arXiv:2606.13662v1 §5 benchmark evaluation`；counterevidence locator 为 `arXiv:2606.13662v1 §6 limitations and task/evaluator scope`。证据只支持作者披露的 workload/model/hardware/metric，不证明生产 SLO 或跨模型、跨硬件普遍优越。

**Trade-off / failure / coexistence / evolution。** Ch81/80 已有 proposal→validation→promotion与self-improvement边界；论文结果保留 Daily evidence，不形成第二 owner。

<!-- claim:SF-2026-ARXIV-2606-13662:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.13662v1` 的 exact-v1 正文与本 report benchmark contract；later version/artifact 不参与本结论，ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-13662:end -->

**V3 Books Decision。** `Pre-denominator Close — Not applicable`；保留审计轨迹但不计入 Candidate、Books 分布或 root 写入队列。

### [HyperTool: Beyond Step-Wise Tool Calls for Tool-Augmented Agents](https://arxiv.org/pdf/2606.13663v1)

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍合理；该 exact-v1 改变的是：tool granularity 是 interface design变量：平台应在细粒度 primitive与复合 tool之间联合评估planning burden、权限面、失败定位与复用。

**State / data / control owner。** `AGENT-TOOL-CALLING` 持有该机制的 authoritative state 与 control decision；论文项目名不取得跨章节 owner。跨 owner handoff 必须绑定 identity、version、failure 与 fallback semantics。

**Evaluation：proof / non-proof。** Method locator 为 `arXiv:2606.13663v1 §§3–4 HyperTool decomposition/composition method`；evaluation locator 为 `arXiv:2606.13663v1 §5 tool-use experiments`；counterevidence locator 为 `arXiv:2606.13663v1 §6 limitations and benchmark/tool-library scope`。证据只支持作者披露的 workload/model/hardware/metric，不证明生产 SLO 或跨模型、跨硬件普遍优越。

**Trade-off / failure / coexistence / evolution。** 粗粒度减少 calls 却扩大authority/隐藏 side effects；细粒度可审计但增加 planning 与 latency，不存在通用最优粒度。

<!-- claim:SF-2026-ARXIV-2606-13663:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.13663v1` 的 exact-v1 正文与本 report benchmark contract；later version/artifact 不参与本结论，ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-13663:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-07-agent/78-tool-calling.md`，Review notes 前正文锚点 `Tool Contract` 已承载长期命题；source 仅作受限证据。

### [EvoArena: Tracking Memory Evolution for Robust LLM Agents in Dynamic Environments](https://arxiv.org/pdf/2606.13681v1)

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍合理；该 exact-v1 改变的是：evolving environment 的 memory 不应只保存最新摘要，而应保存 patch/update history，让状态变化、evidence capture 与 chain-level recovery可评测。

**State / data / control owner。** `AGENT-MEMORY` 持有该机制的 authoritative state 与 control decision；论文项目名不取得跨章节 owner。跨 owner handoff 必须绑定 identity、version、failure 与 fallback semantics。

**Evaluation：proof / non-proof。** Method locator 为 `arXiv:2606.13681v1 §§3–4 EvoArena and patch-based EvoMem`；evaluation locator 为 `arXiv:2606.13681v1 §5 terminal/software/social-preference evaluations`；counterevidence locator 为 `arXiv:2606.13681v1 §6 limitations and domain/model/task-chain scope`。证据只支持作者披露的 workload/model/hardware/metric，不证明生产 SLO 或跨模型、跨硬件普遍优越。

**Trade-off / failure / coexistence / evolution。** patch history提高可追踪性却增加 context/compaction冲突；小幅平均收益不证明所有长期任务优于快照/事件日志。

<!-- claim:SF-2026-ARXIV-2606-13681:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.13681v1` 的 exact-v1 正文与本 report benchmark contract；later version/artifact 不参与本结论，ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-13681:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-07-agent/77-memory.md`，Review notes 前正文锚点 `Consolidation 与 Forgetting` 已承载长期命题；source 仅作受限证据。

### Books / semantic audit

`Integrate=9`，`No Change — Existing Coverage=53`，`Only report=1`，另有 3 项经独立准入复核改为分母前关闭。作者侧 proposal 与独立 Gate 的最终覆盖清单见 [`v3-independent-candidate-books-gate-20260911.json`](../_sources/daily-20260612/v3-independent-candidate-books-gate-20260911.json)；独立写后结果见 [`v3-independent-post-write-audit-20260911.json`](../_sources/daily-20260612/v3-independent-post-write-audit-20260911.json)。`books_removal_queue=0`，13 条 trace 日期修正均已完成并复验，remaining queue=`0`。

## 5. 缺口与下一步

普通研究、来源扫描/初筛、必要审阅、actual owner、Books写入及唯一POST待办为0；63确定新增家族已逐项处置为57I/4具体NC/2中心H，所有已授窄位均释放。唯一非writer jun12_review_finish已完成[DAY§111](../_sources/daily-20260612/SUP_REVIEW_20261026.md)整日验收，作者仅同步最终保存；不恢复新主题/日期，不把导航清空视为完成标准。以下精确外部/中心保留项不授正面Coverage/Evidence，材料到达后只定点重开。

两项中心争议保留精确隔离：[11673](https://arxiv.org/html/2606.11673v1)需补实际Match函数族到monomial表示的桥、与failure下界同向且满足basis/encoder条件的有效证明或明确更正；现有泛化upper不能替failure lower，不否定其所有局部表达实验或全部quantum路线。[11907](https://arxiv.org/html/2606.11907v1)需明确更正knee/反射/CVM定义及一致有限条件，或提供直接检验同一受争机制的有效实验；现原式的单调首点/反射零值/尺度问题未闭，不把有限字符串proxy收益当理论保证。二者均不入Books、不支撑性能/安全结论，只重开受影响证明与采用层，详见各项§4和必要原件。

新增逐篇进度：12059/11864经root唯一§25、12109/11585及11722恢复层经root唯一§30实际POST通过；11673中心保证争议已独核H终态，不改Books。64项current abs Comments/显式alerts已实际轻量检查，root全表实际读，见[原记录](../_sources/daily-20260612/SUP_CURRENT_EVENT_MARKERS_20261026.md)；11722显式重评信号已限定处理，不以旧POST覆盖新信号，也不因重开重计家族。其余版本/会议/页数变化不自动触发全版重审，不复取日期或扩扫描。

必要历史目录的外部保留项涉及Google Research Publications与Meta的Jun11日级档案：当前Blog或过滤子集不能证明全主题当日目录；可接受替代材料为有日期官方列表、具名Jun11原始正文或可读当日目录快照。取得后仅重开该源/事件；在此之前不用于正面证据、Books、无遗漏或性能/安全保证，详见[真实停止点](../_sources/daily-20260612/SUP_SOURCE_CHECK_20261026.md)。MiMo正确官方route资源已恢复目标邻段，不遗留由错误主机拼写造成的日期请求。

具名归属保留另含[Acoda11755](https://arxiv.org/html/2606.11755v1)：arXiv公告联合界仍为Jun11，但同publisher精确DOI10.1145/3774748.3793624的published-print为Apr12、online/PublicationHistory为Sep09。不能以会议日或晚online抹去paper-specific print。完整[原记录](../_sources/daily-20260612/SUP_ACODA_PUBLISHER_DOI_20261026.json)及reader§64保留；须publisher纸本/正文实际可用性日期或明确更正消歧后，只重开该项。当前不评分、不列确定当窗/窗外已审重复、不入Books，不算贡献N/中心H。

独立来源抽检另补七个具名完整题摘，见[原件](../_sources/daily-20260612/SUP_EXACT_ABSTRACT_FALSE_NEGATIVE7_20261026.jsonl)，root已实际校准5准入/2贡献前N；新5日期原字段经reader§40实际独核通过，五项必要/actualowner/实际Books与唯一POST均已完成（§103/106/109/110），不是新增主题扫描。六个具名日期恢复线索则为[RoVE11275](https://arxiv.org/abs/2606.11275v1)、[PermDoRA11262](https://arxiv.org/abs/2606.11262v1)、[On-device RAG11257](https://arxiv.org/abs/2606.11257v1)（现有可能公告界跨Jun10–11 BJT），[Calibration Drift11211](https://arxiv.org/abs/2606.11211v1)、[ProcessThinker11209](https://arxiv.org/abs/2606.11209v1)与[Compatibility-Aware Fine-Tuning11206](https://arxiv.org/abs/2606.11206v1)（Apr→Jun11）。导航字段不足限定Jun11，不先列确定候选、不评分/Books或记N/已审重复；需要直接有日期官方v1公告/列表、早期原始正文或可复查历史原件，原字段和定点重开位置见[来源记录末节](../_sources/daily-20260612/SUP_SOURCE_CHECK_20261026.md)。

以下旧轮保留/执行队列说明仅描述原63候选范围，不代替上述新增工作：

终态保留项：official historical arXiv listing/announcement receipt 尚未取得；定点重开条件：未来取得可改变公开日期 owner 的官方 listing evidence；该缺口不用于正面证据、Books 或无遗漏断言。

1. 9 条 Books body writeback 与 13 条 trace 日期修正均已完成；正文 marker、章节位置、长期机制链和报告映射已由非写作者独立复验，执行队列为 0。
2. official historical arXiv listing/announcement receipt 仍是保留的来源边界；在其到位前不执行跨日迁移，也不把该外部证明缺口伪装成当前日期的执行 pending。
3. 若未来取得相反的 official listing evidence，只重开受影响的日期 owner reconciliation，不推翻本次冻结的 Candidate denominator。

### 旧轮 Repository Changes（历史范围）

- 更新 2026-06-12 Daily 与 `_sources/daily-20260612` 下的 V3 Gate、proposal、reconciliation 和独立写后审计 artifact。
- 复验并最小重排 `27-data.md`、`56-inference-scheduling.md`、`66-evaluation-system.md`、`72-security.md`；`82-multi-agent.md` 的现有落点无需重排。
- 未修改 Candidate denominator、`docs/LEARNING_STATE.md`、其他日期或月级 audit。

## 6. 复核

复核者：root（§1–39）；jun12_review_finish（§40起，唯一续接非writer）。结论：通过；逐项与全部真实Books写后、唯一整日[DAY§111](../_sources/daily-20260612/SUP_REVIEW_20261026.md)均已实际验收。98完整AB＝64准入线索/34贡献前N，不称64实证贡献；64的arXiv公告联合原字段经root/reader§40实际核验，11755纸本信号另由§64隔离，故63确定新增。57实际I、4具体NC、2中心H的逐项证据/owner/采用均完成至[唯一review§110](../_sources/daily-20260612/SUP_REVIEW_20261026.md)，11722受影响修订层已恢复，不重计家族。34明确N按来源/主题/理由分层抽检与false-negative定点纠正在§8/21及本日原始记录，未把宽列表114剩余标题造全量审阅队列。旧63逐字行/原小时窗与旧§4连续有效层已§100独核保护，GF仅§48/52具名locator例外，无第三旧池Methods。最终V3、本地引用与限定working diffcheck记录另附，机器通过不替来源/证据/Books语义整日验收；该DAY由唯一非writer实际完成，作者仅行政同步。

作者终存机械检查（2026-10-26）：V3校验通过；126正式行/新增63无重复，新增身份与current64去11755集合相同；本地文件引用无缺失，57I各owner在真实H2 Review notes前均有唯一正文marker及本人注。旧63行与原小时窗均保留，旧§4仅归一GF具名locator后连续逐字一致；限定working diffcheck通过。这些检查不证明源已读、结论正确或整日语义通过，最终DAY已由唯一非writer在§111实际执行通过，作者未自签。

### 旧轮复核（保留历史有效范围）

当前来源再认证复核者：\`june_11_20_recert\`（独立于原报告作者）。当前合同来源再认证补齐十三个官方 Daily 源；未发现需恢复的独立候选，原 Candidate/Evidence/Books 结论保持不变。

复核者：Candidate/Books Gate `/root/june_11_12_independent_gate`；独立 post-write audit `/root/june_11_12_postwrite`
结论：通过

- 3 项误收已关闭；9 条 Books 正文与 13 条 trace correction 已逐条复验。独立审计发现并修复了案例先于通用基线的章节顺序问题，并将 synthetic-data inference 的 owner 校正为 `PLATFORM-EVALUATION-SYSTEM`；未改变 Candidate denominator 或长期结论。
- 机器校验：`validate_research.py`、`check_report_v3.validate`、JSON/算术/URL 与身份去重、marker 唯一性、Review notes 边界和 `git diff --check` 均通过。机器结果不替代上述语义复核。
