# Daily Research — 2026-01-23

**规范：** V3
**窗口：** 2026-01-22T09:00:00+08:00 ～ 2026-01-23T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-08T05:17:43+08:00
**窗口说明：** 用户明确只补已有2026日报遗漏；原窗口、候选日期/评分与有效审阅保持，原验收仍作为历史有效结果，不代替本轮补查验收。
**补充窗口：** 2026-01-22 ～ 2026-01-22

## 1. 结论

本窗保留五条经独立原源与写后复核的知识差额：variance调制与正交化顺序不可交换；dLLM训练policy与推理sampler分账；固定action/observation的CoT-only判分干预；批内positionwise compact与跨请求KV复用分开；普通安全/utility不替代contextual privacy。已分别窄写Ch28、Ch24、Ch66、Ch43、Ch72，非作者root实际顺读新增段、前后邻接和末注POST通过（后两处位置/population合并问题已局部修正）。

原运行有效结果：独立从本日原始来源重建，未沿用旧Daily/Weekly判断。107个相关/含糊exact-v1完整题摘（78初查+29有界相关标题补检）已终处置：候选冻结50个唯一家族，26标准完成、18深入完成、6低分关闭；Books5整合、45仅报告。48个贡献前关闭只保留原始筛选依据，9个日期保留项不计候选。普通待办0，来源历史/日期不足与Eq10子命题已精确隔离；非作者root已批准完整日级语义验收。本窗完成不授这些隔离项正面Coverage/Evidence/Books或无遗漏保证。

本轮独立补查：原50保持，新增5=4paper+1Jan22artifact，均5分标准必要审阅；总55唯一家族、Books原5整合保持，新增5仅报告、0新增改书。新增读取19完整exact-v1AB、15贡献前关闭；14源有限检查与具体缺段见下，非作者root已实际读六部分并授予本轮DAY通过；外部保留项不支持正面Coverage/Evidence或无遗漏。

## 2. 来源覆盖

本窗来源按现有官方入口及下列有限历史切片处理；“已检查”仅覆盖声明的主题/列表段，不表示全站无遗漏。穷尽当前可用入口而无法恢复的历史材料已隔离到§5，不支撑候选、Books或完整覆盖保证。[最初入口及有限恢复原记录](../_sources/daily-20260123/official-entry-0.txt)、[后续入口](../_sources/daily-20260123/official-entry-1.txt)、[有限恢复](../_sources/daily-20260123/official-recovery.txt)。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | Research/News日期限定主线检索及[官方news RSS](https://openai.com/news/rss.xml)目标切片：Jan21产品/教育→Jan22 Scaling PostgreSQL（RSS12:00GMT），Jan22 usage/Praktika00:00GMT在起点前；Scaling核心MVCC/read replicas/write offload/PgBouncer/cache locks/load shedding为成熟DB机制，未给新模型/AI执行边界，贡献关闭 | 已检查 | 无新增可采用研究；不采厂商规模/五个九保证，不外推全互联网 |
| SRC-ANTHROPIC | Research及Constitution官方Jan22核心规范/训练说明；AI-resistant technical evaluations官方Jan21全文与实际linked original_performance_takehome警告commit（Jan22 01:10Z、merge01:11Z） | 受阻 | Constitution贡献关闭，不为日期再建队列；evaluation测试修改警告的首次public时刻未成立，已精确隔离 |
| SRC-GOOGLE-AI | DeepMind/Research日期限定切片：Jan22 D4RT指向Dec首公开2512.08924；intent-decomposition指EMNLP2025既有工作，当前公告核心未建立本窗实质delta；Research publications仅year筛选 | 受阻 | Blog相关事件已贡献关闭/窗外线索；publications目标历史窗口列表仍不可恢复，隔离，不授零命中 |
| SRC-META-AI | Research空提取/相关publications访问受限及一次本窗日期主题补检；只恢复Jan8 MRAS/Jan28 AI-basics等窗外线索 | 受阻 | 目标历史研究切片缺失；有限入口已耗尽，不以搜索首页证明全覆盖 |
| SRC-QWEN | Blog静态停Nov2025、官方Qwen3-TTS Jan22 release/PyPI0.0.2（07:53:27.513643Z）与repo/HF有限恢复；2601.15621v1 Submitted03:51Z对应Jan23 09BJT excluded endpoint | 受阻 | release与技术正文首次public包络未全成立；repo commit/created不等public。仅保留事件，不把窗外arXiv回填当窗正文；历史Blog切片也隔离 |
| SRC-DEEPSEEK | 官方news可见Jan12 Engram→Jan28 OCR2相关日期切片读到Jan12 | 已检查 | 此切片无Jan22新事件；不外推其他未列发布 |
| SRC-MOONSHOT | Platform Blog当前26条（0–25），最新Nov7/6 2025→May29 2024；官方GitHub日期主题有限补检 | 受阻 | 当前列表不能证明Jan22历史全列表；不循环全repo/全历史，隔离 |
| SRC-TENCENT-HUNYUAN | 首查Research及“全部”恢复；作者与root浏览器均超时/reset，官方GitHub与本窗主题日期有限补检 | 受阻 | 未取得目标历史All列表，当前可读不等历史完整；本轮明确停止重试 |
| SRC-ZAI | Research首查/有限恢复两次超时；官方new-released notes可读Jan19 GLM4.7 Flash及官方GitHub有限补检 | 受阻 | Research目标历史切片无法恢复，隔离，不以release notes替代全部研究目录 |
| SRC-BYTEDANCE-SEED | Research可见Jan27→Dec2；public_papers实际page1/13、1–20of242仅Aug18→May14，另官方GitHub日期补检 | 受阻 | page1不足覆盖Jan且Next没有可复查目标链接；未逐项审242篇。目标窗口页列表隔离 |
| SRC-BAIDU-ERNIE | Blog page1实际Jan29→Jan15→Jan8→Dec23→Nov21，下界已越过本窗，旧page2不扩；官方repo有限补检 | 已检查 | 此日期切片无Jan22事件，不授全站/未列材料召回 |
| SRC-XIAOMI-MIMO | Paper实际Jan8→Feb3目标邻接；Blog15个无日期标题/More未形成可复查历史切片，官方repo有限补检 | 受阻 | Paper切片已检查；Blog目标日期/历史列表不可恢复，隔离 |
| SRC-MINIMAX | EN Blog完整可见Jan27→Dec23；中文对应Jan28→Dec23，已到本窗下界；Agent Tech Blog目标主题有限首查，无实际next历史链接，不采用猜测?page2 | 已检查 | 此官方dated catalog无Jan22新研究事件；不称未列artifacts或全站无遗漏 |
| SRC-ARXIV | 原生list/API406后Computer FOS+registered Jan22～Jan23 00:59:59Z线索；language-training/multimodal-agent/systems三组title查询55/94/36条均page-size100一页止；跨组去重。原生月目录仅作title查漏线索：cs.CL/cs.CV各前1–2000、cs.DC的1–270；只看当窗恢复的final-ID段2601.14260～15288相关标题，补29完整题摘到该下界停止，绝非全月/整类题摘队列。总107完整exact-v1AB：50候选、48贡献关闭、9日期隔离；当前官方abs/comments/直接marks实际核，不扩完整版本史 | 已检查 | 原生入口受限与非全分类召回边界保留；9拟相关事件缺首次公开包络隔离，不授其Evidence/Books；[查询原值](../_sources/daily-20260123/datacite-scoped-results.json)、[排除依据](../_sources/daily-20260123/screening.md) |

本轮补查（2026-10-08）另按 Jan22 完整自然日执行以下14源有限切片记录；原表是原运行记录，继续保留，不以其完成措辞代替本轮验收。[补查原始入口](../_sources/daily-20260123/supplement-official-daily.txt)、[有限恢复](../_sources/daily-20260123/supplement-catalog-stops.txt)、[本轮筛选与日期权限](../_sources/daily-20260123/supplement-screening.md)。

- SRC-OPENAI：Research/News有限日期主题恢复，RSS恢复XML并只取Jan21–23邻接；Jan22三个原始核心（PostgreSQL、Praktika、Work usage）贡献前关闭；Jan23 Codex loop仅窗外恢复线索。结果：已检查；限制：RSS初次403/文本解析失败不当零；成功恢复见[RSS](../_sources/daily-20260123/supplement-openai-rss.json)，不授全站召回。
- SRC-ANTHROPIC：Jan22 Constitution核心规范与训练解释实际读，缺新增受控机制；Jan21 AI-resistant及Jan22警告只复用原有效身份/隔离，不扩大repo。结果：受阻；限制：原警告first-public缺口仍隔离；Constitution不因机构/价值规范准入。
- SRC-GOOGLE-AI：Jan22 D4RT核心指向Dec2512.08924既有首次公开家族，没有新delta；publications只有year过滤，停止动态恢复。结果：受阻；限制：publications目标Jan22历史切片缺失，不把传播页当新paper。
- SRC-META-AI：Research提取0行，一次Jan22主题日期恢复未形成可核历史段。结果：受阻；限制：目标历史研究列表仍缺，空响应不证明零事件。
- SRC-QWEN：旧blog重定向后静态停Sep2025，qwen.ai Jan22页空；官方repo NewsJan22与PyPI0.0.2 wheel/date可核。结果：受阻；限制：新artifact接口边界入选；Blog历史段及技术论文首公开保留项仍隔离，不把Jan23论文前移。
- SRC-DEEPSEEK：当前主页列V4/V3.2等身份、news入口返回初始API页不是完整历史news；原Jan12→Jan28已核段有效复用。结果：受阻；限制：当前主页/误入初始news页不提供新Jan22研究覆盖；不重开原有效结论，不授全站零事件。
- SRC-MOONSHOT：Platform Blog当前latest Nov7/6 2025、有限日期主题恢复；不扫全GitHub。结果：受阻；限制：Jan22历史列表缺段，当前旧列表不是完整target archive。
- SRC-TENCENT-HUNYUAN：Research0行；浏览器初次timeout/reset，随后本子任务不支持IAB可见性，有限主题恢复后停止。结果：受阻；限制：All历史列表未得；不反复等待，不以当前页零提取作零命中。
- SRC-ZAI：Research首查成功恢复dated切片Feb2→Jan19→Jan13，越过目标下界。结果：已检查；限制：仅本dated research切片无Jan22条目；原未恢复目录记录保留为历史事实，不外推全机构发布。
- SRC-BYTEDANCE-SEED：public_papers page1/13、1–20of242仅Aug18→May14，停止无目标页链接的分页；原Research Jan27→Dec2段去重复用。结果：受阻；限制：page1不覆盖Jan22，论文目录目标页缺口保留，未逐项处理242条。
- SRC-BAIDU-ERNIE：Blog新访问timeout，有限日期恢复未形成新段；原Jan29→Jan15→Jan8 dated切片有效复用。结果：受阻；限制：原限定切片判断保持；此次新访问失败不称新增覆盖，不遍历repo。
- SRC-XIAOMI-MIMO：Paper Jan8→Feb3目标邻接复核；Blog15个无日期标题，More不形成可核历史段。结果：受阻；限制：Paper限定切片已处理；Blog目标日期/历史列表仍缺，不读无日期晚期材料。
- SRC-MINIMAX：EN Blog Jan27→Dec23、CN邻接及Agent Tech Blog有限首查，dated catalog已越过目标下界。结果：已检查；限制：本目录无Jan22主线新研究，不称未列artifact/全站无遗漏。
- SRC-ARXIV：原生Jan月CL前25/API本窗Submitted发现cachemiss；Computer FOS+本自然日registered发现三主题18/94/36、148 appearances/139unique、一页/no next；旧身份定点去重，19完整exact-v1AB作实际相关/含糊筛选，不将139变逐项队列。结果：受阻；限制：4新paper公开日由schedule/final-ID+同日deposit上界联合核定；原早Submitted8hold保持。注册独立非公开证明，元数据新版本不回填v1；[发现原值](../_sources/daily-20260123/supplement-discovery.json)。

## 3. 候选与判断

下表为冻结50个唯一材料家族，后续改判须有新证据或具体误判依据。公开时间是由官方公告规则与 final-ID DOI registered 支持的包络，不是 Submitted 或 registered 的精确 public 时刻。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Variance-Adaptive Muon: Accelerating LLM Pretraining with NSR-Modulated and Variance-Scaled Momentum](https://arxiv.org/abs/2601.14603v1) | 2026-01-22T09:00:00+08:00 ～ 2026-01-22T10:46:14+08:00 | 原矩阵正交动量不逐元素适应噪声→variance normalization-before-orthogonalization改变更新geometry→比较pre/post路径而非仅调全局scale；2+1+2=5 | 深入完成 | 整合：TRAIN-PRETRAINING [Ch28](../../../../books/part-04-training-system/28-pretraining.md) |
| [The Flexibility Trap: Why Arbitrary Order Limits Reasoning Potential in Diffusion Language Models](https://arxiv.org/abs/2601.15165v1) | 2026-01-22T09:00:00+08:00 ～ 2026-01-22T11:04:46+08:00 | 任意揭示顺序未必增加推理探索→高不确定fork可能被绕过、固定AR policy用于GRPO仍可parallel推理→分开训练概率归因与sampler交付；2+1+2=5 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Gaming the Judge: Unfaithful Chain-of-Thought Can Undermine Agent Evaluation](https://arxiv.org/abs/2601.14691v1) | 2026-01-22T09:00:00+08:00 ～ 2026-01-22T10:53:23+08:00 | 轨迹自述可混入判分依据→actions/observations固定而CoT-only改写仍改judge结果→冻结输入权限并测删除CoT的recall代价；2+2+2=6 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [VisTIRA: Closing the Image-Text Modality Gap in Visual Math Reasoning via Structured Tool Integration](https://arxiv.org/abs/2601.14440v1) | 2026-01-22T09:00:00+08:00 ～ 2026-01-22T10:42:26+08:00 | 同题text/image与OCR输入对照→先分解感知与推理，不把合成渲染差距归因scale；2+1+2=5 | 标准完成 | 仅报告：局部证据与采用限制见 §4 |
| [On the Generalization Gap in LLM Planning: Tests and Verifier-Reward RL](https://arxiv.org/abs/2601.14456v1) | 2026-01-22T09:00:00+08:00 ～ 2026-01-22T10:42:49+08:00 | 等价name/format与VAL reward干预仍未跨domain→保留planning泛化反侧；2+1+2=5 | 深入完成 | 仅报告：局部证据与采用限制见 §4 |
| [Towards Execution-Grounded Automated AI Research](https://arxiv.org/abs/2601.14525v1) | 2026-01-22T09:00:00+08:00 ～ 2026-01-22T10:44:25+08:00 | execution-grounded idea reward提高均值却丢探索多样性→分开执行有效性、search与RL；2+1+2=5 | 标准完成 | 仅报告：局部证据与采用限制见 §4 |
| [Search over Self-Edit Strategies for LLM Adaptation](https://arxiv.org/abs/2601.14532v1) | 2026-01-22T09:00:00+08:00 ～ 2026-01-22T10:44:35+08:00 | 最佳/最差self-edit archive仍collapse→不能把自改写多样性当适应保证；2+1+2=5 | 标准完成 | 仅报告：局部证据与采用限制见 §4 |
| [QMC: Efficient SLM Edge Inference via Outlier-Aware Quantization and Emergent Memories Co-Design](https://arxiv.org/abs/2601.14549v1) | 2026-01-22T09:00:00+08:00 ～ 2026-01-22T10:44:59+08:00 | outlier bit-width与MRAM/ReRAM通道联动→量化误差和器件噪声共同选资源；2+1+2=5 | 标准完成 | 仅报告：局部证据与采用限制见 §4 |
| [Self-Blinding and Counterfactual Self-Simulation Mitigate Biases and Sycophancy in Large Language Models](https://arxiv.org/abs/2601.14553v1) | 2026-01-22T09:00:00+08:00 ～ 2026-01-22T10:45:04+08:00 | 原history内redaction不等于fresh盲context→分开正确脱敏调用和模型自主调用；2+1+2=5 | 标准完成 | 仅报告：局部证据与采用限制见 §4 |
| [MAS-Orchestra: Understanding and Improving Multi-Agent Reasoning Through Holistic Orchestration and Controlled Benchmarks](https://arxiv.org/abs/2601.14652v1) | 2026-01-22T09:00:00+08:00 ～ 2026-01-22T10:47:27+08:00 | whole-plan MAS按任务依赖/验证对照→委派不是所有问题的预算最优；2+1+2=5 | 标准完成 | 仅报告：局部证据与采用限制见 §4 |
| [Say Anything but This: When Tokenizer Betrays Reasoning in LLMs](https://arxiv.org/abs/2601.14658v1) | 2026-01-22T09:00:00+08:00 ～ 2026-01-22T10:52:37+08:00 | 非injective detokenization影响replacement probe→区分输出字符与token身份；2+1+2=5 | 深入完成 | 仅报告：局部证据与采用限制见 §4 |
| [NeuroFilter: Privacy Guardrails for Conversational LLM Agents](https://arxiv.org/abs/2601.14660v1) | 2026-01-22T09:00:00+08:00 ～ 2026-01-22T10:52:39+08:00 | 单turn隐私分类遗漏trajectory位移→按角色/数据访问定义activation sensor；2+2+2=6 | 深入完成 | 仅报告：局部证据与采用限制见 §4 |
| [INFA-Guard: Mitigating Malicious Propagation via Infection-Aware Safeguarding in LLM-Based Multi-Agent Systems](https://arxiv.org/abs/2601.14667v1) | 2026-01-22T09:00:00+08:00 ～ 2026-01-22T10:52:49+08:00 | 只替换攻击源漏已感染relay→分开源替换与感染回复修复；2+1+2=5 | 深入完成 | 仅报告：局部证据与采用限制见 §4 |
| [Mirai: Autoregressive Visual Generation Needs Foresight](https://arxiv.org/abs/2601.14671v1) | 2026-01-22T09:00:00+08:00 ～ 2026-01-22T10:52:55+08:00 | output MTP与internal 2D foresight对照→training目标位置不等于推理未来可见性；2+1+2=5 | 标准完成 | 仅报告：局部证据与采用限制见 §4 |
| [LaVR: Scene Latent Conditioned Generative Video Trajectory Re-Rendering using Large 4D Reconstruction Models](https://arxiv.org/abs/2601.14674v1) | 2026-01-22T09:00:00+08:00 ～ 2026-01-22T10:52:59+08:00 | 硬depth render条件可烘焙几何错误→考虑对齐时间layout的软latent条件；2+1+2=5 | 标准完成 | 仅报告：局部证据与采用限制见 §4 |
| [AdaTIR: Adaptive Tool-Integrated Reasoning via Difficulty-Aware Policy Optimization](https://arxiv.org/abs/2601.14696v1) | 2026-01-22T09:00:00+08:00 ～ 2026-01-22T10:53:29+08:00 | 效率奖励能反转correctness advantage→保留accuracy主项与受限效率clip；2+1+2=5 | 深入完成 | 仅报告：局部证据与采用限制见 §4 |
| [DARL: Encouraging Diverse Answers for General Reasoning without Verifiers](https://arxiv.org/abs/2601.14700v1) | 2026-01-22T09:00:00+08:00 ～ 2026-01-22T10:53:35+08:00 | 无verifier探索以reference-token-prob reward→只作reference-aligned branch而非正确性保证；2+1+2=5 | 标准完成 | 仅报告：局部证据与采用限制见 §4 |
| [PCL-Reasoner-V1.5: Advancing Math Reasoning with Offline Reinforcement Learning](https://arxiv.org/abs/2601.14716v1) | 2026-01-22T09:00:00+08:00 ～ 2026-01-22T10:53:58+08:00 | offline ±reward乘length-normalized likelihood→只局部objective，不授online稳定性优势；1+1+2=4 | 已关闭 | 仅报告：局部证据与采用限制见 §4 |
| [HERMES: KV Cache as Hierarchical Memory for Efficient Streaming Video Understanding](https://arxiv.org/abs/2601.14724v1) | 2026-01-22T09:00:00+08:00 ～ 2026-01-22T10:54:10+08:00 | query-agnostic分层KV与summary pooling→background预填充和query TTFT分账；2+1+2=5 | 标准完成 | 仅报告：局部证据与采用限制见 §4 |
| [AQAScore: Evaluating Semantic Alignment in Text-to-Audio Generation via Audio Question Answering](https://arxiv.org/abs/2601.14728v1) | 2026-01-22T09:00:00+08:00 ～ 2026-01-22T10:54:16+08:00 | audio问答目标Yes logp替代整体embedding→局部alignment probe非truth证明；1+1+2=4 | 已关闭 | 仅报告：局部证据与采用限制见 §4 |
| [Render-of-Thought: Rendering Textual Chain-of-Thought as Images for Visual Latent Reasoning](https://arxiv.org/abs/2601.14750v1) | 2026-01-22T09:00:00+08:00 ～ 2026-01-22T10:54:48+08:00 | 视觉render教师转continuous latent→压缩代价必须绑定accuracy目标；2+1+2=5 | 标准完成 | 仅报告：局部证据与采用限制见 §4 |
| [Mechanism Shift During Post-training from Autoregressive to Masked Diffusion Language Models](https://arxiv.org/abs/2601.14758v1) | 2026-01-22T09:00:00+08:00 ～ 2026-01-22T10:54:59+08:00 | AR转masked后task-specific circuit重叠不同→局部机制诊断非架构因果；1+1+2=4 | 已关闭 | 仅报告：局部证据与采用限制见 §4 |
| [What Makes Low-Bit Quantization-Aware Training Work for Reasoning LLMs? A Systematic Study](https://arxiv.org/abs/2601.14888v1) | 2026-01-22T09:00:00+08:00 ～ 2026-01-22T10:58:06+08:00 | zero-RL低bit collapse而KD warmup可恢复→校准初始化/数据和训练路径；2+1+2=5 | 深入完成 | 仅报告：局部证据与采用限制见 §4 |
| [Language-Coupled Reinforcement Learning for Multilingual Retrieval-Augmented Generation](https://arxiv.org/abs/2601.14896v1) | 2026-01-22T09:00:00+08:00 ～ 2026-01-22T10:58:17+08:00 | 跨语言shared reward与wrong-cluster penalty→同问题语言间credit单独记账；2+1+2=5 | 标准完成 | 仅报告：局部证据与采用限制见 §4 |
| [SynPerf: A Hybrid Analytical-ML Framework for GPU Performance Prediction](https://arxiv.org/abs/2601.14910v1) | 2026-01-22T09:00:00+08:00 ～ 2026-01-22T10:58:37+08:00 | analytic瓶颈与ML residual跨GPU预测→只在披露operator/config support内选硬件；2+1+2=5 | 标准完成 | 仅报告：局部证据与采用限制见 §4 |
| [TIDAL: Temporally Interleaved Diffusion and Action Loop for High-Frequency VLA Control](https://arxiv.org/abs/2601.14945v1) | 2026-01-22T09:00:00+08:00 ～ 2026-01-22T10:59:30+08:00 | 缓存macro intent+实时micro motion→行动频率与感知新鲜度分开验收；2+1+2=5 | 标准完成 | 仅报告：局部证据与采用限制见 §4 |
| [TempViz: On the Evaluation of Temporal Knowledge in Text-to-Image Models](https://arxiv.org/abs/2601.14951v1) | 2026-01-22T09:00:00+08:00 ～ 2026-01-22T10:59:38+08:00 | temporal correctness独立subject/quality且caption负相关→自动judge需temporal切片；2+1+2=5 | 标准完成 | 仅报告：局部证据与采用限制见 §4 |
| [CorpusQA: A 10 Million Token Benchmark for Corpus-Level Analysis and Reasoning](https://arxiv.org/abs/2601.14952v1) | 2026-01-22T09:00:00+08:00 ～ 2026-01-22T10:59:40+08:00 | 10M corpus NL2SQL truth路径→分开SQL执行一致与源事实/问题语义；2+1+2=5 | 标准完成 | 仅报告：局部证据与采用限制见 §4 |
| [Obscuring Data Contamination Through Translation: Evidence from Arabic Corpora](https://arxiv.org/abs/2601.14994v1) | 2026-01-22T09:00:00+08:00 ～ 2026-01-22T11:00:44+08:00 | Arabic contamination避开English signal→翻译不能当去污染，probe非membership证明；2+1+2=5 | 标准完成 | 仅报告：局部证据与采用限制见 §4 |
| [RadixMLP -- Intra-batch Deduplication for Causal Transformers](https://arxiv.org/abs/2601.15013v1) | 2026-01-22T09:00:00+08:00 ～ 2026-01-22T11:01:10+08:00 | prefix-path token在单forward compact→positionwise去重与sequence-mixing边界分开；2+1+2=5 | 深入完成 | 整合：INFER-PREFILL [Ch43](../../../../books/part-05-inference-system/43-prefill.md) |
| [LogicScore: Fine-grained Logic Evaluation of Conciseness, Completeness, and Determinateness in Attributed Question Answering](https://arxiv.org/abs/2601.15050v1) | 2026-01-22T09:00:00+08:00 ～ 2026-01-22T11:02:03+08:00 | attributedQA连接路径与再推断→completeness/conciseness/一致性不能混同entailment；2+1+2=5 | 标准完成 | 仅报告：局部证据与采用限制见 §4 |
| [Memory Retention Is Not Enough to Master Memory Tasks in Reinforcement Learning](https://arxiv.org/abs/2601.15086v1) | 2026-01-22T09:00:00+08:00 ～ 2026-01-22T11:02:54+08:00 | gated重写利Tmaze但伤retain任务→memory retention不唯一决定任务能力；2+1+2=5 | 深入完成 | 仅报告：局部证据与采用限制见 §4 |
| [Auditing Language Model Unlearning via Information Decomposition](https://arxiv.org/abs/2601.15111v1) | 2026-01-22T09:00:00+08:00 ～ 2026-01-22T11:03:29+08:00 | base/unlearned隐藏信息分解→白盒残余decodability不是黑盒泄漏/删除认证；2+1+2=5 | 深入完成 | 仅报告：局部证据与采用限制见 §4 |
| [CLEANER: Self-Purified Trajectories Boost Agentic Reinforcement Learning](https://arxiv.org/abs/2601.15141v1) | 2026-01-22T09:00:00+08:00 ～ 2026-01-22T11:04:12+08:00 | error-context correction移入purified-prefix→必须重算policy logprob与prefill成本；2+1+2=5 | 深入完成 | 仅报告：局部证据与采用限制见 §4 |
| [BayesianVLA: Bayesian Decomposition of Vision Language Action Models via Latent Action Queries](https://arxiv.org/abs/2601.15197v1) | 2026-01-22T09:00:00+08:00 ～ 2026-01-22T11:05:33+08:00 | vision捷径可忽略language，posterior/prior辅助分支→语言利用与推理接口分开；2+1+2=5 | 深入完成 | 仅报告：局部证据与采用限制见 §4 |
| [Privacy Collapse: Benign Fine-Tuning Can Break Contextual Privacy in Language Models](https://arxiv.org/abs/2601.15220v1) | 2026-01-22T09:00:00+08:00 ～ 2026-01-22T11:06:06+08:00 | paired access-norm隐私退步、另一良性SFT安全/效用保持→独立contextualprivacy gate；2+2+2=6 | 深入完成 | 整合：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [PROGRESSLM: Towards Progress Reasoning in Vision-Language Models](https://arxiv.org/abs/2601.15224v1) | 2026-01-22T09:00:00+08:00 ～ 2026-01-22T11:06:12+08:00 | progress/mismatch共同评价→高unanswerable准确率可由false rejection获得；2+1+2=5 | 深入完成 | 仅报告：局部证据与采用限制见 §4 |
| [Metadata Conditioned Large Language Models for Localization](https://arxiv.org/abs/2601.15236v1) | 2026-01-22T09:00:00+08:00 ～ 2026-01-22T11:06:29+08:00 | URL-only与alltags/tokenmatched及missing-region反侧→metadata非地域缺失补足保证；1+1+2=4 | 已关闭 | 仅报告：局部证据与采用限制见 §4 |
| [The Effect of Scripts and Formats on LLM Numeracy](https://arxiv.org/abs/2601.15251v1) | 2026-01-22T09:00:00+08:00 ～ 2026-01-22T11:06:51+08:00 | 仅换digits/scripts/formats能损arithmetic→surface grounding与运算分开测；2+1+2=5 | 深入完成 | 仅报告：局部证据与采用限制见 §4 |
| [RayRoPE: Projective Ray Positional Encoding for Multi-view Attention](https://arxiv.org/abs/2601.15275v1) | 2026-01-22T09:00:00+08:00 ～ 2026-01-22T11:07:25+08:00 | ray深度/uncertainty进入RoPE→位置encoding需保留相机已知与近似边界；2+1+2=5 | 标准完成 | 仅报告：局部证据与采用限制见 §4 |
| [StableWorld: Towards Stable and Consistent Long Interactive Video Generation](https://arxiv.org/abs/2601.15281v1) | 2026-01-22T09:00:00+08:00 ～ 2026-01-22T11:07:34+08:00 | 早clean-frame保留抑drift但阻scene switch→cache容量与reference可靠性分开；2+1+2=5 | 深入完成 | 仅报告：局部证据与采用限制见 §4 |
| [Walk through Paintings: Egocentric World Models from Internet Priors](https://arxiv.org/abs/2601.15284v1) | 2026-01-22T09:00:00+08:00 ～ 2026-01-22T11:07:38+08:00 | painting到egocentric video的SCS/adapter局部对照→受限生成recipe不证明world dynamics；1+1+2=4 | 已关闭 | 仅报告：局部证据与采用限制见 §4 |
| [Iterative Refinement Improves Compositional Image Generation](https://arxiv.org/abs/2601.15286v1) | 2026-01-22T09:00:00+08:00 ～ 2026-01-22T11:07:41+08:00 | 相同G/E调用budget迭代critic优于parallel部分切片→不等同总compute/latency匹配；2+1+2=5 | 标准完成 | 仅报告：局部证据与采用限制见 §4 |
| [Towards Understanding Best Practices for Quantization of Vision-Language Models](https://arxiv.org/abs/2601.15287v1) | 2026-01-22T09:00:00+08:00 ～ 2026-01-22T11:07:42+08:00 | ViT/LLM/QFormer bits与GPTQ/AWQ任务反转→量化选择绑定任务与组件；1+1+2=4 | 已关闭 | 仅报告：局部证据与采用限制见 §4 |

| [LFS: Learnable Frame Selector for Event-Aware and Temporally Diverse Video Captioning](https://arxiv.org/abs/2601.14594v1) | 2026-01-22T09:00:00+08:00 ～ 2026-01-22T10:46:02+08:00 | 固定frame预算不保证temporal覆盖→同K16取消stratified低于uniform→把软训练权重与硬采样覆盖条件分开；2+1+2=5 | 标准完成 | 仅报告：局部条件／评价反侧，必要证据及不改书理由见 §4 |
| [3D Space as a Scratchpad for Editable Text-to-Image Generation](https://arxiv.org/abs/2601.14602v1) | 2026-01-22T09:00:00+08:00 ～ 2026-01-22T10:46:13+08:00 | 直接render/edit会丢orientation与identity→3D scratchpad转depth及crop-identity独立条件→分开可编辑几何和最终图像质量；2+1+2=5 | 标准完成 | 仅报告：局部条件／评价反侧，必要证据及不改书理由见 §4 |
| [Probing Prompt Design for Socially Compliant Robot Navigation with Vision Language Models](https://arxiv.org/abs/2601.14622v1) | 2026-01-22T09:00:00+08:00 ～ 2026-01-22T10:46:41+08:00 | 增加系统prompt不必改进动作→naive低于无system且语义分数不等action accuracy→分开语言回答和离散动作评价；2+1+2=5 | 标准完成 | 仅报告：局部条件／评价反侧，必要证据及不改书理由见 §4 |
| [Reconstruction-Anchored Diffusion Model for Text-to-Motion Generation](https://arxiv.org/abs/2601.14788v1) | 2026-01-22T09:00:00+08:00 ～ 2026-01-22T10:55:40+08:00 | CFG语义对齐不等重建质量→对前一motion预测重建所得残差另做REG→分别选择文本guidance和额外重建预算；2+1+2=5 | 标准完成 | 仅报告：局部条件／评价反侧，必要证据及不改书理由见 §4 |
| [Towards Holistic Modeling for Video Frame Interpolation with Auto-regressive Diffusion Transformers](https://arxiv.org/abs/2601.14959v1) | 2026-01-22T09:00:00+08:00 ～ 2026-01-22T10:59:50+08:00 | 连续AR插帧可积累误差→强低帧率全video条件允许独立skip后bridge→重置采样须绑定已知未来keyframes；2+1+2=5 | 标准完成 | 仅报告：局部条件／评价反侧，必要证据及不改书理由见 §4 |

| [HiNS: Hierarchical Negative Sampling for More Comprehensive Memory Retrieval Embedding Model](https://arxiv.org/abs/2601.14857v1) | 2026-01-22T09:00:00+08:00 ～ 2026-01-22T10:57:19+08:00 | hard-only/删easy不必优于混合→联合sampling configuration局部反侧→比较比例、数量与曝光而非仅提高hardness；2+1+2=5 | 标准完成 | 仅报告：不采negative类别因果/自然比例最优，实际受限对照见 §4 |

上述44项限定准入、必要证据与Only/4分关闭处置均已由非作者root实际顺读§4并复核；15013/15220窄写及局部修正POST通过。尾5（14594/14602/14622/14788/14959）的限定必要证据/Only处置亦经root实际逐段核验，加HiNS抽检改判共50项；日期与分层排除汇总及日级语义验收已通过。全部 exact-v1 official abs 页面已核身份、comments 与直接 notice 信号；没有遇到官方 withdrawn/erratum 标记。15141/15286 的 correction 匹配是摘要方法词，非勘误公告。只核当前事件，不遍历修订史。

本轮新增按补充窗 Jan22 公开日期归属，原50行及其公开包络逐字保留。新5家族均5分标准，具体必要证据与仅报告处置见§4；新增0处Books写入，不把owner映射当准入。

| [Prosody-Guided Harmonic Attention for Phase-Coherent Neural Vocoding in the Complex Spectrum](https://arxiv.org/abs/2601.14472v1) | 2026-01-22 | mel条件弱化prosody/phase → F0参与harmonic attention、直接real/imag谱与phase loss → 比较条件与渲染责任；2+1+2=5 | 标准完成 | 仅报告：局部voiced-vocoder模块，未证明组件独立收益或实时SLO |
| [Diffusion Epistemic Uncertainty with Asymmetric Learning for Diffusion-Generated Image Detection](https://arxiv.org/abs/2601.14625v1) | 2026-01-22 | reconstruction confound → Laplace参数采样与noise均值拆分、非对称margin → 分开估计特征与generalization；2+1+2=5 | 标准完成 | 仅报告：近似diffusion detector sensor，不授一般uncertainty分解或LLM truth |
| [HyperNet-Adaptation for Diffusion-Based Test Case Generation](https://arxiv.org/abs/2601.15041v1) | 2026-01-22 | curated condition pairs/latent搜索受限 → final SUT loss驱动实例级HyperNet → 比较白盒适配、预算与语义保留；2+1+2=5 | 标准完成 | 仅报告：局部test generator，单次调用预算不等总算力/真实失败真值 |
| [Learning Consistent Taxonomic Classification through Hierarchical Reasoning](https://arxiv.org/abs/2601.14610v1) | 2026-01-22 | leaf正确可掩盖中间层失配 → leaf-conditioned二阶段及HCA反侧 → 同时报告leaf、条件一致性与联合正确；2+1+2=5 | 标准完成 | 仅报告：局部taxonomy评价反侧，不授普遍层级reasoning或因果控制 |
| [Qwen3-TTS Jan22 artifact：qwen-tts0.0.2](https://pypi.org/project/qwen-tts/0.0.2/) | 2026-01-22 | model流式宣称不等wrapper可流式交付 → False参数仅模拟文本流式、完整codes后decode返回 → 核实际消费接口而非参数名；2+1+2=5 | 标准完成 | 仅报告：精确公开artifact兼容边界，不提前采用Jan23技术论文 |

## 4. 证据与知识整合

### [Variance-Adaptive Muon: Accelerating LLM Pretraining with NSR-Modulated and Variance-Scaled Momentum](https://arxiv.org/abs/2601.14603v1)

采用 §3～5/Appendix A 必要机制与对照，保存 [原文 core](../_sources/daily-20260123/html-14603-v1.txt)。EMA variance 来自动量偏差；NSR/VS 先逐元素调制动量，再经 Newton–Schulz 正交化。pre/post ablation 支持这不是可交换的全局幅度调整。GPT-2 OWT 和两组 LLaMA 配置绑定数据、batch、长度、目标loss；target-loss iterations 不等于墙钟或交付成本。额外 O(mn) variance buffer、gamma 校准及 520M 小batch退步是直接反侧，不采用 latest 改题/1.33× 的结论。本次未运行代码或复现实验。

Ch28 现有 Whitening Regime 分开 covariance 与 optimizer geometry，却未解释 elementwise variance 与正交化的顺序差额；已在该节后、full-matrix grouping 前增加一个受限机制段，保留已有优化器回退。root 已实际核必要原源、owner、新增段及前后邻接，POST 通过。

### [The Flexibility Trap: Why Arbitrary Order Limits Reasoning Potential in Diffusion Language Models](https://arxiv.org/abs/2601.15165v1)

采用 §3～5/Appendix A，保存 [原文 core](../_sources/daily-20260123/html-15165-v1.txt)。同256 token/256 step等比较下，arbitrary-order 会优先绕高不确定位置，pass@1024 表示该预算探索而非真实能力上限；entropy fork 是解释性关联，不冒称所有模型的因果律。JustGRPO 固定 autoregressive factorization 用于训练概率路径，architecture不变；并行 sampler 仍可用于推理。训练比较包含额外RL与不同初始化/预算，不能与纯sampler受控比较合并；tokens-per-step 不替代 wall-clock。

Ch24 已区分 token temperature/position temperature及提交规则，但未明确训练 policy probability 与推理 sampler 的独立接口；已接在该两段后，只增加此差额，不重复综述已有顺序控制。root 已顺读新增段、前后邻接与末注，POST 通过。

### [Gaming the Judge: Unfaithful Chain-of-Thought Can Undermine Agent Evaluation](https://arxiv.org/abs/2601.14691v1)

采用 §4～6/Appendix C，保存 [原文 core](../_sources/daily-20260123/html-14691-v1.txt)。五类 CoT-only 改写固定 actions/observations；800条轨迹来自659任务，300条已有human标签、500条GPT-5 silver；50条子集只一名 annotator，不能把其中一致性外推全数据。九个judge的条件 JFR/FPR 分母不同，aware/rubric/voting/budget并不消除攻击；移除CoT或严格prompt损失success recall约10～20点。范围为受测web任务与输入协议，不证明所有VLM judge、环境真实状态或安全保证。

Ch66 已分成功/失败recall和ensemble，新增的是固定行为证据时单独改变CoT输入的控制实验及删除代价；已在该段后、环境干预前写一段。root 已实际核必要原源、owner、新增段及前后邻接，POST 通过。

日期记录原值：14603 Submitted `2026-01-21T02:41:56Z`、registered `2026-01-22T02:46:13Z`；15165 Submitted `2026-01-21T16:41:58Z`、registered `2026-01-22T03:04:45Z`；14691 Submitted `2026-01-21T06:07:43Z`、registered `2026-01-22T02:53:22Z`。[arXiv官方availability](https://info.arxiv.org/help/availability.html) 的weekday20:00 EST与final-ID不提前规则给起点，DOI registered给公开上界；表中终点在字段秒值之后一秒，包络全落窗。有限 exact-title earlier-author 检索未发现已知更早正文，不宣称证明全网不存在。精确版本 v1，不采用后续修订来回填本窗。

### [VisTIRA: Closing the Image-Text Modality Gap in Visual Math Reasoning via Structured Tool Integration](https://arxiv.org/abs/2601.14440v1)

§2～4/Table3、§5；同5000 NuminaMath原答案保留、LaTeX render与text/image/OCR控制；Qwen2.5-VL-7B SFT/LoRA用8×V100、147948 teacher-filtered SnapAsk不是人工truth。Table3 与文字对GPT的OCR decline及Qwen OCR-only优势互相不符，故只采用配对感知/推理诊断，不采用scale/OCR普遍优势。仅报告：受限合成输入与教师一致性筛选，不据此增加通用视觉读取机制。 [必要原文](../_sources/daily-20260123/html-14440-v1.txt) 

### [On the Generalization Gap in LLM Planning: Tests and Verifier-Reward RL](https://arxiv.org/abs/2601.14456v1)

§4.3/§5/§6.1～6.6；Qwen3-1.7B、41.5k IPC训练、两domain各500 holdout，匿名化/compact格式和VAL reward均保留有效性约束。RLA6000两卡FSDP每epoch约5×成本，holdout仍0是有限跨domain反侧，name/format并未控制所有符号与实例差异；不推所有规划任务普遍失败。仅报告：该domain的受控验证增量，不替换通用 planning/reward 契约。 [必要原文](../_sources/daily-20260123/html-14456-v1.txt) 

### [Towards Execution-Grounded Automated AI Research](https://arxiv.org/abs/2601.14525v1)

§2.1～2.2/§4～5/§8；只纳入 LLM pretraining/posttraining实验，不纳入领域科学应用。Protected data/eval、Implementer10并行patch+2retry取首可执行，failure0仍会混入执行器能力；nanoGPT124M FineWeb8×H100固定25min reward 与目标loss复测分开，Qwen2.5Math1.5B GRPO reward用validation非独立heldout认证。进化search的best-of-N与总GPU walltime未配平；Qwen3-30B-A3B RL提高平均却坍缩为少量idea，不能把最大观察reward当物理能力上界。仅报告：两小规模execution环境与scaffold，未建立跨scale/数据的长期新训练保证。 [必要原文](../_sources/daily-20260123/html-14525-v1.txt) 

### [Search over Self-Edit Strategies for LLM Adaptation](https://arxiv.org/abs/2601.14532v1)

§3～5.1；NTP self-edit固定模板与best2/worst2 archive，750 self-edits/iteration；Qwen8B SQuAD50train/200val，无original passage concat。Archive虽保留多样轨迹仍有collapse、恢复与再下降，未优于强rewrite，diversity不等于收益因果。仅报告：局部adaptation/search负侧，不推广为所有self-edit必失败。 [必要原文](../_sources/daily-20260123/html-14532-v1.txt) 

### [QMC: Efficient SLM Edge Inference via Outlier-Aware Quantization and Emergent Memories Co-Design](https://arxiv.org/abs/2601.14549v1)

§3～4；global outlierρ进入5bit MRAM、2/3bit ReRAM inliers与DRAM KV，噪声MSE含BER与量化Delta，training-free尺度网格。NVMain/DLRSim是模拟而非芯片部署，ρ过大导致MRAM瓶颈，额外面积与不同Jetson硬件不能合并成端到端收益。仅报告：器件/位宽joint recipe限定作者模拟条件，未建立本项目可交付硬件能力。 [必要原文](../_sources/daily-20260123/html-14549-v1.txt) 

### [Self-Blinding and Counterfactual Self-Simulation Mitigate Biases and Sycophancy in Large Language Models](https://arxiv.org/abs/2601.14553v1)

§2～5/§7；Qwen2.5-7B-Instruct/GPT4.1，人口属性反事实与60争议×presentation/user-side counterbalance，binary logits为观测对象。原history内redacted prompt仍可见未脱敏context；fresh API正确redaction输出控制可降低局部bias，但spontaneous self-call经常没调用、漏pronoun或问题。Sycophancy仍有选择性服从，增加inference/latency；不把平均bias或有利工具输出叫公平/真实意图证明。仅报告：二模型受限binary决策与工具调用实验，不新增公平性保证。 [必要原文](../_sources/daily-20260123/html-14553-v1.txt) 

### [MAS-Orchestra: Understanding and Improving Multi-Agent Reasoning Through Holistic Orchestration and Controlled Benchmarks](https://arxiv.org/abs/2601.14652v1)

§3～5；一次whole-plan，无执行中feedback；lowDoM≤1仍delegate而非SAS，iGSM五轴控制dependency/verification等结构。RL orchestrator与固定CoT subagents不等于SAS相同训练预算，未adversarial training的robustness近0，sequential任务受subagent能力限制，context与委派有成本。仅报告：受控合成任务的处置比较，不给多Agent普适收益。 [必要原文](../_sources/daily-20260123/html-14652-v1.txt) 

### [Say Anything but This: When Tokenizer Betrays Reasoning in LLMs](https://arxiv.org/abs/2601.14658v1)

§3～4；XSUM100～600词、5%target replacement、11k样本、10family，T1/topP.9/K50。不同IDs经规范化可同词，不是所有输出严格字节相同；IDs posthoc筛选未构成heldout普遍规则。采用字符/token身份分账的局部反侧，输出成功不证明internal belief。仅报告：特定detokenization/replacement probe，保留tokenizer为identity条件，不补未核的内部推理解释。 [必要原文](../_sources/daily-20260123/html-14658-v1.txt) 

### [NeuroFilter: Privacy Guardrails for Conversational LLM Agents](https://arxiv.org/abs/2601.14660v1)

§3.3/§4～6/limits；攻击者black-box、可控trajectory、知道secret存在但不知值；guardrail需activation白盒访问、角色/隐私指令。PrivacyLens493×100malicious+100benign合成、CMPL16k/40k及20+20多turn，70:30 split与layer选择；activation velocity求和是projected displacement，标签识别攻击意图不是真实泄漏。换模型/finetune需recal，context方向不同；零FP和低cost不泛化，也不授filter安全判决权。仅报告：作者受限activation sensor recipe；当前Ch72“隐私检测是Policy-bound Sensor”已实际分sensor与policy/consent，未用该局部probe重定义权限。 [必要原文](../_sources/daily-20260123/html-14660-v1.txt) 

### [INFA-Guard: Mitigating Malicious Propagation via Infection-Aware Safeguarding in LLM-Based Multi-Agent Systems](https://arxiv.org/abs/2601.14667v1)

§3三个控制、§4检测/恢复、§5关键ablation/limits、AppA；root已实际定点复核必要证据。仅隔离初始攻击者仍漏infected relay；dual-head graph识别后需分开attacker replacement与infected-response repair。邻接constraint依封闭消息传播与正确标签，至少观察一轮、有监督合成标签；Role/Mem/Plugin替换可能损任务能力。ASR混合恶意/错误，MDSR定义依任务，不外推工具/shared memory持久感染。仅报告：受限closed-graph局部remediation，未授生产安全或无损保证。 [必要原文](../_sources/daily-20260123/html-14667-v1.txt) 

### [Mirai: Autoregressive Visual Generation Needs Foresight](https://arxiv.org/abs/2601.14671v1)

§2～3/Tables1～3；ImageNet256、LlamaGen B/L/XL，80epoch控制output/internal、1D/2D，ADM50k样本。Output MTP可变差，internal2D foresight较1D改进；EMA在线或frozen bidirectional DINO只train，projection丢弃后仍causal解码。不同source/层/λ/foresight数结果不同，tSNE不是完整机制因果，教师forward与训练增量未转walltime。仅报告：visual-AR ImageNet受限目标/监督选择，不把lookahead训练当推理读取未来。 [必要原文](../_sources/daily-20260123/html-14671-v1.txt) 

### [LaVR: Scene Latent Conditioned Generative Video Trajectory Re-Rendering using Large 4D Reconstruction Models](https://arxiv.org/abs/2601.14674v1)

§3～4；CUT3R scene-state tokens由adapter压缩，与videoVAE按frame布局concat，避免硬depth point-cloud render的烘焙错误，不改变DiT结构。8×H200/15k iterations，100Pexels dynamic+50DL3DV static、33frames480×832、4目标trajectory，同caption；预训练baselines不是所有训练预算配平。k×m固定latent组/DiT量ablation支持局部折中，pose由reconstruction+alignment估计不是真实物理保证，透明动态物失败。仅报告：specific CUT3R/Wan条件recipe，未证明latents普遍优于可验证geometry。 [必要原文](../_sources/daily-20260123/html-14674-v1.txt) 

### [AdaTIR: Adaptive Tool-Integrated Reasoning via Difficulty-Aware Policy Optimization](https://arxiv.org/abs/2601.14696v1)

§3/§4.1/§5.2/limits/App证明；正确性与难度相关效率reward可使正确答案advantage负，CAS以accuracy主项并clip效率到δ|Aacc|+η。证明positive需Aacc>βη/(1−βδ)，all-correct Aacc0仍允许微小负项，不能宣称所有correct永不负。Qwen3/7B、ReToolSFT、Dapo17k/ctx4096/T1/topP.6/G16；tool-call数非latency，AIME2025/AMC切片仍可差。仅报告：受限reward/clip参数分支，不用局部recipe替换通用correctness Gate。 [必要原文](../_sources/daily-20260123/html-14696-v1.txt) 

### [DARL: Encouraging Diverse Answers for General Reasoning without Verifiers](https://arxiv.org/abs/2601.14700v1)

§4式3～6、§5～6；root实际定点原源通过。Reward是reference平均token probability加有限Δr，不是语义等价或truth，Qwen72B judge含code不等同执行真值。只采用reference-aligned探索的局部分支，有限judge与初始化/预算限制仍保留。仅报告：不扩为无verifier亦能保持正确性的长期保证。 [必要原文](../_sources/daily-20260123/html-14700-v1.txt) 

### [PCL-Reasoner-V1.5: Advancing Math Reasoning with Offline Reinforcement Learning](https://arxiv.org/abs/2601.14716v1)

4分关闭；§3～4已读但不升级机制分数。Offline难题选样与±reward乘exp(meanlogp)，不是序列policy probability/IS；SFT原666k4epochs与6068hard题筛成30215样本的offline训练未配同预算online。800steps/64Ascend910C、AIME30×32sampling、max129024，response length变长；不采用superior stability/efficiency。仅报告该local objective，不进入Books。 [必要原文](../_sources/daily-20260123/html-14716-v1.txt) 

### [HERMES: KV Cache as Hierarchical Memory for Efficient Streaming Video Understanding](https://arxiv.org/abs/2601.14724v1)

原生HTML404，精确v1 PDF pp3～11及p30 AppendixF；深层summary将pruned K先旋转到同phase后mean、V空间mean，是近似聚合非attention exact。浅层recency、深层query-agnostic anchor与跨层smoothing；A800效率/H200准确不同设备，TTFT从query receipt不含background prefill。lazy streaming与eager offline不同成本，低cache预算long offline反而退步，不能claim所有streaming无损。仅报告：特定LLaVA/video分层KV recipe，未运行代码/复现真实流成本。 [必要原文](../_sources/daily-20260123/2601.14724v1.pdf) 

### [AQAScore: Evaluating Semantic Alignment in Text-to-Audio Generation via Audio Question Answering](https://arxiv.org/abs/2601.14728v1)

4分关闭；exact-v1完整题摘与official identity/date已核。Audio问答的target Yes log-prob只改局部alignment probe，不认证场景真实或正确性；未采用headline metric superiority。仅报告该局部分数，不进入Books。 

### [Render-of-Thought: Rendering Textual Chain-of-Thought as Images for Visual Latent Reasoning](https://arxiv.org/abs/2601.14750v1)

§3～4/limits；32px renderedCoT由frozen vision teacher给训练latent，stage1 MLP MSE+CE backbone frozen，stage2 LoRA CE；inference用continuous latents而非image/vision encoder。32latent与原CoT的accuracy显著不同，H20 batch1 latency不能叫相同质量目标收益。仅报告：二小Qwen模型的视觉监督压缩分支，当前不增加通用无损压缩机制。 [必要原文](../_sources/daily-20260123/html-14750-v1.txt) 

### [Mechanism Shift During Post-training from Autoregressive to Masked Diffusion Language Models](https://arxiv.org/abs/2601.14758v1)

4分关闭；§3/§4.1/limits局部EAP-IG DreamQwen与DiffuLLaMA/Llama，IOI/Countdown overlap不同。没有控制全部pre/posttraining因素，task-specific circuit诊断不识别architecture因果；仅报告局部measurement，不改Books的AR/masked关系。 [必要原文](../_sources/daily-20260123/html-14758-v1.txt) 

### [What Makes Low-Bit Quantization-Aware Training Work for Reasoning LLMs? A Systematic Study](https://arxiv.org/abs/2601.14888v1)

§3/§4.3/limits；W3/W2 G128、exclude embedding/head，KD/SFT与GPTQ/RTN控制。Zero-RL RTN invalid collapse与KD warmup对照支持训练初始化边界，不因单局部higher score泛化；Numina/OpenR1 vsWiki反侧，Qwen.6/1.5/4B、vLLM32k/T.6/topP.95，3evaluation随机seed不是3training重复。仅报告：tested low-bit数学recipe，未证明跨domain/BF16质量与真实部署收益。 [必要原文](../_sources/daily-20260123/html-14888-v1.txt) 

### [Language-Coupled Reinforcement Learning for Multilingual Retrieval-Augmented Generation](https://arxiv.org/abs/2601.14896v1)

§3～6含§3.3；同query translations共享GRPO group，native→all→English两turn有heuristic，不是真值。答案char3recall、wrong-cluster相似度margin与clipped penalty=minweight是具体credit分支；跨语言reward相关可能继承翻译/judge偏差。仅报告：multilingual RAG局部objective，未授稳定性或正确性保证。 [必要原文](../_sources/daily-20260123/html-14896-v1.txt) 

### [SynPerf: A Hybrid Analytical-ML Framework for GPU Performance Prediction](https://arxiv.org/abs/2601.14910v1)

exact-v1 §IV～VI/V-B；手工或profiler operator分解、analytic Tensor/FMA/XU等模型+ML residual，RR scheduler与closest-hardware闭源cuBLAS近似。torch2.8/CUDA12.8/FlashInfer.4.1/SGLang.5.4/vLLM.11，11GPU中6train5unseen、warmup5/measure10，attention与GEMM config split有限support。未覆盖全部pipeline/稀有算子/端到端SLO，不采用后续PipeWeave改题；仅报告受限性能预测与不确定性。 [必要原文](../_sources/daily-20260123/html-14910-v1.txt) 

### [TIDAL: Temporally Interleaved Diffusion and Action Loop for High-Frequency VLA Control](https://arxiv.org/abs/2601.14945v1)

§III～IV；宏VLM intent缓存16、微步Euler1×4actions，lag4 motionCNN/contact等修正；增加adapter成本。Dynamic MuJoCo paused 2000trial与8static任务，9Hz是Orin profiling推导而非edge实际闭环；static退步、noMotion/onlyMotion对照和大α更差保留。仅报告：仿真action循环，不能把高action频率当新观察/安全交付。 [必要原文](../_sources/daily-20260123/html-14945-v1.txt) 

### [TempViz: On the Evaluation of Temporal Knowledge in Text-to-Image Models](https://arxiv.org/abs/2601.14951v1)

§3～5/limits；7940prompts中500 stratified样本、2机构annotator，三问分quality/subject/temporal，参考图silver且不全时态。CLIP temporal无显著相关，caption temporal负相关，decompositionalVQA/Directjudge仍有限macroF1；不把物体正确/画质作为时间正确性。仅报告：五T2I/指定judge及prompt切片的新反侧，未形成所有视觉时间评价的统一界。 [必要原文](../_sources/daily-20260123/html-14951-v1.txt) 

### [CorpusQA: A 10 Million Token Benchmark for Corpus-Level Analysis and Reasoning](https://arxiv.org/abs/2601.14952v1)

§3～4/limits；ensemble提取consensus→schema NL2SQL→execution，SQL truth不证明源文或question-to-SQL忠实。两domain人工1000each+第二LLM review非整体100%认证，Gemini RAG/Memory与DeepSeekV3 judge未匹配全部预算，human12人90min非superhuman普遍结论。仅报告：该10M corpus bench的truth lineage与长context边界，未改通用RAG原理。 [必要原文](../_sources/daily-20260123/html-14952-v1.txt) 

### [Obscuring Data Contamination Through Translation: Evidence from Arabic Corpora](https://arxiv.org/abs/2601.14994v1)

§3～4/Tables1～4；四open family LoRA相同optimizer设置，但添加Arabic proportions也增加数据量，不是总token完全匹配。MMLU accuracy与XQuAD非单调，TS-Guessing/MinK++/IDR行为与表中方向不提供二元membership；Qwen CLC所有poison级全1、IDR近chance是prompt/model collapse反侧。TACD正式limits承认非membership认证，跨language一致性可混reasoning或输入不敏感。仅报告：采用翻译不能当去污染的受限反证，不采可靠暴露所有contamination headline。 [必要原文](../_sources/daily-20260123/html-14994-v1.txt) 

### [RadixMLP -- Intra-batch Deduplication for Causal Transformers](https://arxiv.org/abs/2601.15013v1)

§3～5；同causal prefix path而非同token/position即可merge；positionwise在N' compact，attention前scatter QKV、后gather，positions/cu_seqlens保持，CPU trie与GPU batch overlap。H10080GB fp16、Qwen3-0.6B/4B/8B、TEI/Candle FA2、MSMARCO，1287requests含tokenize/batching/HTTP；vLLM.13 block32在4/8B反而更快，内存reservation差异不等于同资源比较。γ低冗余gate、long32k attention主导、autoreg仅context、indices O(N)、shape数值变化保留，不授bit-exact所有kernel或大规模training。具体差额已写入Ch43 nano-vLLM policy段之后、跨Runtime身份段之前，保留索引成本、低冗余回退及vLLM反侧；root实际必要原源/owner与修正后正文、邻接、末注POST通过。 [必要原文](../_sources/daily-20260123/html-15013-v1.txt) 

### [LogicScore: Fine-grained Logic Evaluation of Conciseness, Completeness, and Determinateness in Attributed Question Answering](https://arxiv.org/abs/2601.15050v1)

§4～5/AppB；connected Horn/entity path定义completeness，pathsteps/total conciseness；同generator由CoT再推断是determinateness，不是外部truth/entailment。Hotpot/MuSiQue/2Wiki、4H100/vLLM/T1，concisenessGPT4omini，其余同generator；gold-doc factual metrics为独立参考，人工100 transformation不认证所有输出。仅报告该logical-probe recipe，不把LM self-agreement变成proof。 [必要原文](../_sources/daily-20260123/html-15050-v1.txt) 

### [Memory Retention Is Not Enough to Master Memory Tasks in Reinforcement Learning](https://arxiv.org/abs/2601.15086v1)

§4～9；Endless Tmaze要overwrite、ColorCubes偏retain，architecture调参后固定10runs×100episode SEM。Gated Tmaze强不意味着无条件更好；ColorCubes中/极端全部0、简单task LSTM与其他差异保留，没有gate独立causal proof。仅报告：一般RL小模型受限memory反侧。实际Ch77 typed write/revise/reject以及stable/transient不能同覆写已承载选择边界，不为补该recipe强改。 [必要原文](../_sources/daily-20260123/html-15086-v1.txt) 

### [Auditing Language Model Unlearning via Information Decomposition](https://arxiv.org/abs/2601.15111v1)

§5～6/limits/AppB；RINE在base/unlearned内部表示与membership标签上估计unique/residual信息下界，TOFU/MUSE5methods3families。Requires两个checkpoint白盒和probe训练，low residual不说明信息不存在，更不等于真实black-box leakage或法律删除证书。仅报告：白盒auditing recipe。实际Ch72输入条件gate/unique memorization与独立attack/retrain审计已把行为抑制/信息sensor与删除权分开，不由该lowerbound新增删除保证。 [必要原文](../_sources/daily-20260123/html-15111-v1.txt) 

### [CLEANER: Self-Purified Trajectories Boost Agentic Reinforcement Learning](https://arxiv.org/abs/2601.15141v1)

§4～5/AppB；lookahead K与SequenceMatcher code lexical不是semantic oracle，error-context sampled correction移入purified-prefix后必须重算logprob。70/30clean/raw curriculum Qwen7B，SGLang radix只少prefix重复不免suffix compute；1/3steps不是同比例总compute。tool-onlyDPO collapse、disableSAAR小差异保留，不能宣称所有scaffold可靠。仅报告：局部轨迹净化/再计算recipe，不把self-correction签为truth。 [必要原文](../_sources/daily-20260123/html-15141-v1.txt) 

### [BayesianVLA: Bayesian Decomposition of Vision Language Action Models via Latent Action Queries](https://arxiv.org/abs/2601.15197v1)

§2～4/limits；vision-only goal shortcut与masked-language OOD对照，posterior[v,lang,Q]/prior[v,Q,lang]共享FM与likelihood-ratio proxy PMI、stopgrad prior，64queries。Two-branch train成本、inference posterior-only；CMI≤H(language|vision)非architecture因果，proxy非精确action density。16H100/40kBridge、Simpler/RoboCasa有限任务，不同config ablation不可合数，real robot/LIBERO/RoboTwin未实验。仅报告：specific VLA训练条件分支，不普遍保证语言遵循。 [必要原文](../_sources/daily-20260123/html-15197-v1.txt) 

### [Privacy Collapse: Benign Fine-Tuning Can Break Contextual Privacy in Language Models](https://arxiv.org/abs/2601.15220v1)

§3～5/limits/AppA；3000paired同prompt/utility但需要confirmation vs可自主取context，PrivacyLens493、CIMemories100自动GPT5nano、CommonSenseQA1000与AgentHarm分开，3finetune runs。闭源default1epoch与Llama LoRA10epochs非跨model预算配平；access-norm对照支持局部behavior drift，late-layer logit/steering只50场景相关非完整因果。English SFT未覆盖RL/DPO/所有隐私；不授representational damage普遍机制或安全认证。两组实验分开：synthetic paired access norms 对照与另 §4.3 empathetic/support 真实良性数据 SFT；AgentHarm/CSQA保持不是同一paired population。已在Ch72 Fine-tuning Safety Repair节首写一段并经root实际正文/邻接POST修正通过。 [必要原文](../_sources/daily-20260123/html-15220-v1.txt) 

### [PROGRESSLM: Towards Progress Reasoning in Vision-Language Models](https://arxiv.org/abs/2601.15224v1)

§2～5；240trajectories/3325observations、4embodiments，expert keyframe之间线性段插值假设smooth/monotone，不是真实completion真值。Cross-view reference与obs/text mismatch N/A，Qwen2.5VL3B两stage25kSFT20kGRPO；NSE/PRC/AFRR/UDA分母与false rejection需分账，training-free可伤small，highUDA也可过拒。仅报告：该benchmark/progress监督局部recipe，不使score取得现实任务完成权。 [必要原文](../_sources/daily-20260123/html-15224-v1.txt) 

### [Metadata Conditioned Large Language Models for Localization](https://arxiv.org/abs/2601.15236v1)

4分关闭；§4.3、31English news.5/1B、17countries4continents、equal total token；URL-only可不逊alltags，LOCO缺region未恢复。仅报告局部metadata差额，不授metadata补足真实地域事实或跨语言保证。 [必要原文](../_sources/daily-20260123/html-15236-v1.txt) 

### [The Effect of Scripts and Formats on LLM Numeracy](https://arxiv.org/abs/2601.15251v1)

§2～4/limits；21scripts identification、20translation、四large-model以及630等受限dataset，运算英文固定、digits-only换script；native operators/mapping/format hint/fewshot另协议。SI/TR与tokens-per-digit相关不识别tokenizer因果；GLMER排除low-performing model/scripts，格式输入+输出比baseline更难。只保留surface grounding下的鲁棒性反侧，未知pretrain distribution/IP-address解释是作者hypothesis。仅报告：受限算术surface/提示控制，不重推tokenizer原则。 [必要原文](../_sources/daily-20260123/html-15251-v1.txt) 

### [RayRoPE: Projective Ray Positional Encoding for Multi-view Attention](https://arxiv.org/abs/2601.15275v1)

§3～6；已知camera/ray depth+σ，uniformsegment expected encoding；CO3D/Objaverse80k FOV20～80/RE10K与Plucker/GTA/PRoPE等比较。σ/depth必要性依数据，RE10K infinity可足够，removingσ可微增PSNR，UniMatch stereo depth SqRel负侧。root已独立数学核Eq10：uniform一维平均旋转A=sinc(ωa)R(ωμ)，Ai Aj^-1幅值si/sj不等于独立相对期望si×sj；平均rotation一般非正交，不能默改inverse为transpose。该exact relative保证不采用且隔离；作者有限uncertainty smoothing/位置实验可独立成立，不因此宣布其余结论都争议。 [必要原文](../_sources/daily-20260123/html-15275-v1.txt) 

### [StableWorld: Towards Stable and Consistent Long Interactive Video Generation](https://arxiv.org/abs/2601.15281v1)

§3～4/AppE；largerwindow减drift但旧frame阻scene-change，固定earlyclean frames与ORB/RANSAC similarity形成eviction条件。Matrix9window/OpenOasis16/Hunyuan33frame块不同策略，16/10/16scenes与80/50/48长video，VBenchLong collapsed-static可虚高temporal，用户20人30video。阈值.75是受测折中，过低留旧/过高丢clean，latency+1～2%非免费，部分Ascend910B2配置非全部硬件披露。仅报告：specific生成reference-cache局部边界，不把ORB geometric相似当事实scene truth。 [必要原文](../_sources/daily-20260123/html-15281-v1.txt) 

### [Walk through Paintings: Egocentric World Models from Internet Priors](https://arxiv.org/abs/2601.15284v1)

4分关闭；exact-v1完整题摘与official身份日期已核，局部SCS与adapter比较有受限设计差额。Painting/internet-prior生成可走不意味着action-conditioned dynamics或物理真实性；不采所有world model适用保证。仅报告局部recipe，不改Books。 

### [Iterative Refinement Improves Compositional Image Generation](https://arxiv.org/abs/2601.15286v1)

§3～4/§7；STOP/BACKTRACK/RESTART/CONTINUE，budget=T×M仅generator/editor calls，critique/verification及串行walltime未匹配。三generator、ConceptMix/T2I/TIIF、弱inloop vs强final judge；main称Gemini2.5Flash而§7称FlashLite，身份冲突未解，不采用精确headline倍率/普遍最优。Qwen budget16:8×2与16×1局部不同，部分color/texture不获益，小critic退步；150prompt×3raters的人偏好不是全可靠truth。仅报告可检查的局部depth/breadth比较，不把调用数称总compute相等。 [必要原文](../_sources/daily-20260123/html-15286-v1.txt) 

### [Towards Understanding Best Practices for Quantization of Vision-Language Models](https://arxiv.org/abs/2601.15287v1)

4分关闭；§3局部BLIP2ViTg/OPT2.7B与LLaVA1.5 7B、128calibpairs、10%VQAval/GQA，componentbits2～8。GPTQ与AWQ preference可因VQA/caption/retrieval反转，compound quantization worse；ViT参数少不等于不重要。仅报告受限best-practice comparison，没有新quantizer/kernel，不外推所有VLM。 [必要原文](../_sources/daily-20260123/html-15287-v1.txt) 


### [LFS: Learnable Frame Selector for Event-Aware and Temporally Diverse Video Captioning](https://arxiv.org/abs/2601.14594v1)

精确v1 §3～5.5：LongCLIP frame特征经temporal scoring/global gate，冻结Qwen3-VL-8B的caption loss反传选择器；训练soft fused表示与推理K16分段hard selection不是同一操作。§5.5固定K16/backbone取消stratified反而低于uniform，支持保留覆盖条件，不采“仅learned score足够”。5epochs AdamW、batch1、3×A800，1588条2～3min视频的teacher captions来自Qwen3-VL-253B-A22B；ICH-CC为100video/两语各500题、由caption回答QA，和raw-video理解／人类真值不能合并。短Dream-1K的precision/recall取舍不授普遍收益；ℓ1若作用在归一化权重上不自动稀疏，不采正文未经确认的compact保证。推理SLO/完整端到端预算Not Disclosed。仅报告：受限frame-selector条件与soft/hard路径差异，不能由该领域recipe新增通用表示／采样保证，不改Books。 [必要原文](../_sources/daily-20260123/html-14594-v1.txt)

### [3D Space as a Scratchpad for Editable Text-to-Image Generation](https://arxiv.org/abs/2601.14602v1)

精确v1 §3～4/§8：GPT-5 planner、GPT-4o parser、Flux.1-dev主体、Hunyuan3D2.5 mesh、PyTorch3D depth及SIGMAGen身份条件各司其职；裁剪主体后估orientation、多视图选择camera与直接full-image orientation/rotation有局部反侧。§4受限ablation支持独立identity/depth与camera路径，不能证明3D scratchpad就是物理世界状态。870 GenAI-Bench及540 Compound prompts用VQAScore Yes概率和QAlign评价，非执行/物理真值；Idea2Img多轮/候选与本方法单轮增强非等预算，生成mesh、agent调用和identity编辑额外成本不能省略；orientation/camera改进随query而变。不能重新摆关节、复杂composition/articulation仍失败。仅报告：可编辑3D条件转接的局部recipe，不替代World Model dynamics或把可视几何升为事实；无本次通用owner差额，不改Books。 [必要原文](../_sources/daily-20260123/html-14602-v1.txt)

### [Probing Prompt Design for Socially Compliant Robot Navigation with Vision Language Models](https://arxiv.org/abs/2601.14622v1)

精确v1 §3～5/limitations：固定GPT-4o及6离散action，naive system prompt的AA低于no-system baseline，是受测prompt的局部评价反证；BERTF1/SBERT语义接近不代表ground-truth离散动作正确。SNEI325（265/60）与MUSON800（640/160）为标注图像，不是闭环实机避碰；TinyLLaVA冻结SigLIP vision、projector/LM SFT5epochs、FP16/ZeRO3/batch32，标注包含VLM与human，模型比较不升为因果prompt原则。夜间／天气覆盖不足，无在线controller/safety-envelope验证；不采所有增加prompt都会变差或动作accuracy就是现实robot安全。仅报告：保留language-vs-action及prompt配置反侧；局部静态评价不足以改写通用VLA闭环条件，不改Books。 [必要原文](../_sources/daily-20260123/html-14622-v1.txt)

### [Reconstruction-Anchored Diffusion Model for Text-to-Motion Generation](https://arxiv.org/abs/2601.14788v1)

精确v1 §3.1～3.3 Eq10/11、§4.2/4.4/4.5：motion/text encoder共享MDM decoder；motion-centric alignment的stop-grad与β=0.01以及normalized latent self-regularization是训练目标，不证明真实motion manifold。REG重建前一步motion estimate，将text预测与重建预测的差额做独立guidance，再与CFG分账。Table5的REG/CFG/组合受限对照支持文本对齐与重建质量不同，不授一般error消除。HumanML3D14616条motion/44970描述与KIT3911/6353、450k/400k训练steps/batch64/lr1e-4，50/20步推理；batch1含REG时间高于无REG（.398vs.226s，硬件Not Disclosed），早期2/4/6步REG是额外成本折中，20步对50步不同模型不是等compute。仅报告：受限text-to-motion重建guidance，不证明任意模态／physical motion正确性，现有生成owner已分训练objective与推理路径，缺少更强通用差额，不强改Books。 [必要原文](../_sources/daily-20260123/html-14788-v1.txt)

### [Towards Holistic Modeling for Video Frame Interpolation with Auto-regressive Diffusion Transformers](https://arxiv.org/abs/2601.14959v1)

精确v1 §3.2～3.4/§4.1～4.4：全低fps video是强条件，nearest-neighbor upsample+binary mask保留已知frames；Wan2.1 DiT local spatial/dense temporal attention及tiled VAE用256/stride192、20frame chunk。skip独立生成后bridge concatenation借已知未来keyframes重置条件，并非无条件online AR任意重启。Table2同unconditional VAE causal-vs-skip为有限反侧；conditional VAE是另一改动，不混合归因。LAVIB训练16k steps/batch256/60×512²，VAE10k/17×256²，Euler16steps/shift8；4K用2×80GB GPU（型号Not Disclosed）。XTest/SNU/FILM的全低fps输入与相邻frame基线条件不配平，部分baseline LPIPS更好，bridge仍有额外生成成本；不采任意长度恒定error/自由生成稳定保证。仅报告：强condition插帧的skip/bridge recipe，通用生成owner已分causal conditioning与cache窗口，此局部负载不足以新增World Model保证，不改Books。 [必要原文](../_sources/daily-20260123/html-14959-v1.txt)

### [HiNS: Hierarchical Negative Sampling for More Comprehensive Memory Retrieval Embedding Model](https://arxiv.org/abs/2601.14857v1)

改判依据是新实际反側，而非主题/owner映射：完整题摘后原以成熟hard-negative recipe关闭；非作者抽检§3.3/4.1/Table4/§5.2/7发现hard-only与移除easy的局部对照，故定点重开。精确v1数据构造hard cap2|V|、medium/easy各|V|，medium实现candidate=M\Nh可能仍含未抽hard；训练201462样本、BAAI/bge-small-en-v1.5、4×A80080GB、batch512、lr2e-5、temperature.02、step490/1.25epochs。全训练给15neg/30%-30%-40%且关闭in-batch negatives，但NoEasy/NoMedium/JustHard是否补满15、重新配比或等曝光未说明，不能假设quantity/compute匹配，更不能授所有true negatives。

Table4在LoCoMo/Mem0的joint sampling configurations为Full平均F1 .2449、NoEasy .2197、HardOnly .2233，支持hard-only/删easy不必改善该受测configuration，不识别负例类别的因果或自然比例最优。Temporal Full .0974反低于NoEasy .0998；§5.2的NoHard标签/−.0057与表行冲突，不采用其解释。规则tier、少epochs/有限benchmark、未直接测下游agent响应utility的限制保留；初版贡献关闭理由不能继续沿用。仅报告：带数量／曝光不确定性的局部retrieval采样反側，成熟retrieval owner不需为此recipe补写；不强制造Books diff。root已实际核决定性原文并通过此改判及标准完成/Only处置。 [必要原文](../_sources/daily-20260123/html-14857-v1.txt)

上述均为作者受限原源判断，未运行代码或复现实验；未披露的生产 concurrency/SLO、完整端到端质量预算写为 Not Disclosed，不由 microbenchmark/动作频率/调用数补造。非作者root已分批实际核全部50项限定命题/必要反侧及Books处置，不无差别重读无关附件。4分关闭项只要求身份/落窗/去重与不采用理由，不为达到标准审阅遍历全文。

本轮增量必要证据（Jan22自然日；原§4前述连续正文及反侧原样保留）：

### [Prosody-Guided Harmonic Attention for Phase-Coherent Neural Vocoding in the Complex Spectrum](https://arxiv.org/abs/2601.14472v1)

精确v1 HTML受限后读PDF §2–4/TableI：[必要原文](../_sources/daily-20260123/supplement-openai-core-first.txt)、[表及直接限制](../_sources/daily-20260123/supplement-necessary-fourth.txt)。Harvest提取F0参与attention，decoder给real/imag complex谱、iSTFT与unit-magnitude phase loss；这不证明预测谱总满足STFT consistency或完美phase coherence。LJSpeech1.1/VCTK、22.05kHz、FFT/window1024、hop256，AdamW2e-4/batch16、单NVIDIA GPU（型号、precision、训练epochs/总预算 Not Disclosed）。TableI F0-RMSE HiFiGAN21.6→16.8，MOS4.2→4.45、20listeners；摘要MOS+.15对应另一baseline4.3，不能混成对HiFiGAN增幅。未见单模块消融/CI及样本分母，不能唯一归因F0 attention或phase loss；实时部署是future work。仅报告：是局部voiced声码器替代，[Ch23连续表示](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md#连续表示)实际分开encoder/独立waveform decoder与reconstruction责任，此稿不足改写一般codec或整个生成范式，不改Books、未核代码/复现。

### [Diffusion Epistemic Uncertainty with Asymmetric Learning for Diffusion-Generated Image Detection](https://arxiv.org/abs/2601.14625v1)

精确v1 §3.3/4/5、Tables1–4：[核心](../_sources/daily-20260123/supplement-core-first.txt)、[对照/反侧](../_sources/daily-20260123/supplement-core-second.txt)。last-layer diagonal Laplace参数posterior，经noise重复均值后对参数求方差，结合CLIP与real类较小contrastive margin；采用的是该模型下近似特征，不采Lemma1/Eq8–10把total variance比例归parameter variance的一般等式，noise条件方差项与expectation/norm平方不能随意消去。SD1.5、t200、224²、CLIPResNet50、batch48、V100、lr1e-4；Table4无DEU/ASL76.1/90.7、DEU90.3/98.7、ASL81.7/93.8、joint91.5/99.7是ACC/AP的受限组件对照。BigGAN弱及Table2 DRCT训练人口更换将近chance推到较高ACC，不能把跨dataset全部收益归估计器。采样次数/完整预处理成本、precision、重复seed/CI Not Disclosed，不授免成本或probability校准。仅报告：sensor只支持diffusion-derived detection局部机制，不推广为LLM epistemic truth；[Ch66 Claim Sensor](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md#从-raw-score-到可定位可校准的-claim-sensor)正文明确“该probe是传感器，不是真值概率”，并要求model-specific sensor→deployment-slice calibration；[标签校准](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md#raw-score-只有经过标签校准才是概率)已承载通用采用合同，不强造Books差额。

### [HyperNet-Adaptation for Diffusion-Based Test Case Generation](https://arxiv.org/abs/2601.15041v1)

精确v1 §3/4.5–4.7/Tables1–4：[方法](../_sources/daily-20260123/supplement-necessary-fifth.txt)、[评价与限制](../_sources/daily-20260123/supplement-hynea-eval.txt)。冻结prior、复制block+zero layers与output→spatial projector，每例调HyperNet、最终image loss穿全部denoise，白盒SUT梯度；免新curated failure pairs不等免预训练或免每例训练，Driving还用已训练segmentation ControlNet。600 test cases、equal ceiling2700SUT evaluations/early-stop；REPA-E/SD/StyleGAN等不同backbone，调用数不配平FLOPs。ImageNet94.41s、CelebA220.89s而Mimicry51.87s更快；Driving diversity .094低于GIFT .102，模拟diffusion-Mimicry耗时是extrapolation不是运行。ImageNet human label preservation .787、20valid responses/Fleissκ.336，misclassification=输出变化不等真实语义失败；FID相关不替代另两域标签审查。lr提高可损质量、低lr可到20min；hardware/precision、完整cost Not Disclosed。仅报告：局部failure test generator，不将可导SUT score升为真值、普遍OOD生成或通用性能优势；[Ch24 DDPM](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#ddpm从可采样的加噪过程得到训练目标)正文明确guidance/VJP与solver均付费、生成器只拥有proposal，其特定实例调参配方不要求新增Books机制正文，原prompt/latent搜索仍共存。

### [Learning Consistent Taxonomic Classification through Hierarchical Reasoning](https://arxiv.org/abs/2601.14610v1)

实际反侧纠正了原拟“成熟SFT/RL recipe”关闭：精确v1 §1/Table2、§3、§4.1/4.3：[必要原文](../_sources/daily-20260123/supplement-taxon-necessary.txt)、[反侧及人口](../_sources/daily-20260123/supplement-taxon-final.txt)。同一VL-Taxon推理去reasoning时animal leaf稍升而HCA下降；在DirectListing leaf正确集合给GT leaf的HCA79.14→99.52，是特权诊断不是部署收益。Stage1 open-set leaf预测→Stage2 leaf条件问答；Qwen2.5VL7B、Plant3771species×10、species两半SFT/GRPO LoRA各1epoch，batch128/lr5e-5/rank64/G8/KL.4；测试similar-choice使用SigLIP distractors，非任意自由回答。Table5各model条件correct-leaf集合不同，不当matched population因果比较；generalization亦受plant-only训练/SFT collapse及较弱open-set结果约束。GT/leaf错误会传播，二次推理/训练均计费，hardware/precision/CI Not Disclosed。仅报告：叶级准确率与全层联合正确必须分账的局部反证，[Ch66聚合指标](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md#聚合指标必须能暴露不同-failure-type)正文要求counterexample slice揭露总分掩盖的失效类型；[联合可靠性](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md#组件分数不能在相关错误下直接合成系统可靠性)正文要求联合故障样本、拒绝组件准确率直接合成保证，已承载这里的通用边界，未新增普遍taxonomy reasoning能力保证，不改Books。

### [Qwen3-TTS Jan22 artifact：qwen-tts0.0.2](https://pypi.org/project/qwen-tts/0.0.2/)

仅本日公开artifact，不采用Jan23技术论文。[PyPI版本/公开上界](../_sources/daily-20260123/supplement-qwen002-date.json)与官方NewsJan22确认release，wheel SHA256807de60fd454156a68839bfd7401ebea7d5b4dd149f23b067eadf4e614bc8a5f。[精确代码必要行](../_sources/daily-20260123/supplement-qwen002-core.json)：qwen3_tts_model.py513/655/753说明non_streaming_mode=False只模拟streaming text，不启用true streaming input/generation；voice clone/design/custom wrapper先生成完整codes再decode、返回wav列表+sr，而非chunk iterator。模型声称具备流式能力≠该wrapper真正逐块输出；仅称公开wrapper限制，不否定底层架构stream能力，也不采用97ms作为此wrapper实际延迟，不把参数名当生产接口。x-vector-only忽略reftext/refcode，ICL须reftext，属于条件身份补充，选项本身不构成新机制准入。未运行GPU/完整SLO benchmark。仅报告：此版本可测试兼容边界，[Ch42 Streaming与完成](../../../../books/part-05-inference-system/42-what-happens-during-inference.md#streaming-与完成)及[指标时间边界](../../../../books/part-05-inference-system/42-what-happens-during-inference.md#指标必须绑定时间边界)已分开模型输出与客户端可见终止；[Ch24生成范式正文](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)的音频分支明确renderer/buffer费用、已播放音频不可回滚的commit边界，版本限定实现事实不改变长期合同。

## 5. 缺口与下一步

本窗终态保留项：以下隔离材料不用于正面证据，不支持Books或无遗漏断言；逐项保留定点重开条件。

原运行有效结果：无可执行普通待办；原日级独立语义验收已通过，原完成态V3、引用及限定diff检查同步于§6；不代替本輪补查验收。

- arXiv早Submitted、当前final-ID registered但缺首次公开下界的8项： [GCG Attack 14266](https://arxiv.org/abs/2601.14266v1)（Submitted2025-12-30）、[llama.cpp quantization 14277](https://arxiv.org/abs/2601.14277v1)（Jan11）、[KV learned scoring 14279](https://arxiv.org/abs/2601.14279v1)（Jan13）、[Chain-of-Memory 14287](https://arxiv.org/abs/2601.14287v1)（Jan14）、[Guided audio plan 14304](https://arxiv.org/abs/2601.14304v1)（Jan18）、[SilentDrift 14323](https://arxiv.org/abs/2601.14323v1)（Jan20 01:24Z）、[LAEP 14327](https://arxiv.org/abs/2601.14327v1)（Jan20 08:39Z）、[LURE 14330](https://arxiv.org/abs/2601.14330v1)（Jan20 10:39Z）。完整exact-v1AB与当前official metadata已实际读，潜在机制/安全信号不因日期未知排除贡献；它们早于Jan20 19Z提交，所以scheduled availability+registered不能证明全部公开包络落窗。有限ID/title/date检索、当前official abs、availability、DataCite已耗尽；14279官方repo早commit与14304 Siren Aug2025 README也不提供精确公开时刻。不无限回溯。可接受该具体正文官方首次公开公告/具有时区的author公开时刻或完整目标公告列表；到达后先重开归属，不先升级已审/入选。当前不评分、不采攻击效果或所有量化比较，必要已读片段保留到各html缓存。
- [STEAD 14778](https://arxiv.org/abs/2601.14778v1)：准入5及必要受影响审阅有效，但官方comments为NeurIPS2025 poster，已实际找到[同题同作者官方正文入口](https://proceedings.nips.cc/paper_files/paper/2025/hash/3d03800841fa1bb2f43ef1750aafcce4-Abstract-Conference.html)及OpenReview正文/官方2025日程。该具体更早公开反证阻止按本窗首次paper入选；notes日期API403 challenge后停止。原有same-denoising-round independent positions、容量与tamper恢复条件的局部审阅保留，不授跨模型安全或普遍ECC保证。可接受正文first-public证据或真本窗重要新delta，先定点裁日期/事件；不因arXiv初收录视为重要修订，不做旧新版diff。
- [Anthropic AI-resistant technical evaluations](https://www.anthropic.com/engineering/AI-resistant-technical-evaluations)（官方dateJan21无TZ）与其实际linked original_performance_takehome：core三轮harness/time confounds已读，Jan22警告[d45812f](https://github.com/anthropics/original_performance_takehome/commit/d45812f96a6740086db7f2aa78925d9a0b7389dd)说明首日低1300cycle解修改tests/N_CORES、需git diff/submit tests。仅该warning受影响内容已核，不扩全repo；commit/merge时间不等首次public，无法当确定窗内5分事件。保留具体评价反侧但不作为本日报正面证据/Books；可接受目标文章及warning实际公开公告/发布timeline，重开仅对应事件。
- Qwen3-TTS：官方Jan22release、PyPI upload给artifact公开上界，不能独自证明技术正文已在当窗公开；arXiv公告在excluded endpoint。repo created/initial commit及两个HF空恢复不消除更早author正文未知。现有§2/3/4.1/4.2必要已读不冒充本窗候选；可接受官方release-linked版本技术正文的完整public包络（或真实更早归属），重开仅该家族，不另开Qwen全站。
- 历史目录：Google Research publications、Meta Research、Moonshot Blog、Hunyuan Research All、ZAI Research、Seed Public Papers目标窗口页、MiMo Blog及Qwen Blog缺口按§2已穷尽有限可用原始入口。不以无结果/当前新列表当零命中；可接受这些明确来源的完整Jan22窗口研究列表/有日期发布链接等原始材料，分别重开受影响切片，不重跑整月/每周。
- [RayRoPE 15275 Eq10](https://arxiv.org/abs/2601.15275v1)：exact relative-expectation子命题已由root独立数学核，平均rotation非一般正交、inverse比值与独立期望乘积不等；明确不采用。该争议不扩为整家族争议，局部实验已终处置。只有作者更正公式及所需条件或可核新证明才重开此子命题，不能静默将inverse改transpose。

本轮补查停点：作者已完成14源有限尝试、19完整题摘及5新增必要审阅/Books判断；5项必要原证/Only处置与本轮六部分DAY均已非作者root实际通过，本轮无可执行普通待办；完成态校验见§6，原验收与新验收分账。候选等比数与所有新结论只支持上述有限范围。

本轮外部终态保留：Meta/Hunyuan/Google publications/Moonshot/Qwen Blog、Seed public_papers目标页及MiMo Blog的完整Jan22历史列表仍未恢复；DeepSeek/ERNIE此次新访问仅受限、原有效dated切片继续复用。可接受对应来源有日期Jan22研究列表或具名primary publication链接，重开仅该source slice。空页面/搜索无命中不支持零事件、完整Coverage或无遗漏。ZAI此次恢复的Feb2→Jan19dated切片已单独处理，不用它消除其他来源缺口。

Qwen原“技术正文”隔离保持，不与新artifact准入矛盾：paper15621按官方normal Thursday announcement归Jan23BJT不落Jan22补充窗，已确认窗外只留恢复线索，不深入读/挪入；release+wheel身份只授权Jan22artifact命题。OpenAI [Codex agent loop](https://openai.com/index/unrolling-the-codex-agent-loop) RSS Jan23明确窗外，只记录真实归属日线索，不在本日深审。本日新增不消除旧8早Submitted日期holds、AI-resistant warning首次public hold或RayRoPE Eq10子命题隔离；必要材料以后到达只重开受影响项。

## 6. 复核

原运行复核者：root（非报告作者；历史有效验收只用于原50与原Books5处）
原运行结论：通过

实际核实际主题查询与native标题查漏/停止边界，确认宽月目录不作逐项题摘/全文队列；日期公开包络、9项隔离与有限历史来源终态已验收。全部50候选的准入、§4限定必要机制／关键对照／直接反側、Books处置分批实际复核；5处窄增量原源/owner及实际正文、前后邻接、末注POST通过，Ch43位置与Ch72两组population合并错误已局部修正后重核。HiNS由原关闭改准入5只基于实际联合sampling-config反側，不因成熟原则或审阅质量改分；14778具体更早正文日期反证隔离，15275 Eq10不采用判断已独立数学核，未把子命题争议扩到其有限实验。

排除复核实际覆盖25/48：必要信号14项（14567、15232、14615、14914、15118、15075、15130、15288、14528、14738、14698、15077、15059、14260）完整题摘或决定性受影响原源核验有效复用；按来源/主题/理由层抽检11项（14290、14298、14339、14351、14446、14460、14479、14490、15282、14523、15047），覆盖repair/safety模块、benchmark人口、Agent执行分层、BBO/信任/统计judge、OCR、video指标、GPU搜索与综述。普通样本原12中14857转入候选后为11；14523已把GPU代码优化纳入主线可能性，关闭主理由改为成熟搜索/经验复用组合未新增编译正确性或执行预算边界，科学负载仅补充；15282定点metric/§5核到MLLM VQA+VMBench robot checklist、新population及新rank协议，未给旧指标same-video控制失误，具体关闭而非统一拒绝benchmark。未抽检23项（14514、14568、14569、14598、14601、14714、14722、14735、14741、14821、14874、14895、14921、14942、14949、14973、15016、15017、15124、15160、15221、15250、15260）维持作者完整题摘/当前official marks与具体原始筛选理由，不称全量独立验证；原检查及共同错误受影响集合已定点纠偏，不扩大无关附件。

机器：完成态 `python3 scripts/validate_research.py --report papers/2026/01/23/README.md` 通过；本日README的58个localrefs、与STOP/screening合计107个localrefs均missing0；限定五Books/本日报/cache的unstaged `git diff --check` 与已有staged `git diff --cached --check` 均通过。第一次完成态校验因§5“不用于／支持”措辞和§6复核短字段未单独成行而失败，已仅修可读格式后重跑通过，没有修改validator或重授证据。五Books整体diff含运行前及其他作者变更，本日仅5段+末注，不把617新增行当本日产出；保护既有MM/M/未跟踪状态，未stage、commit或push。机器不替代上述真实日级语义验收。

复核者：root（非补查报告作者；本轮补查及最终六部分DAY）
结论：通过

本轮机器（完成状态）：V3单日报校验通过；README与本轮screening合计82个本地引用missing0，新增JSON缓存全部可解析。本轮保存原件比较：原50候选表的52行（含header/separator）全部逐行保持、原§4正文作为连续完整前缀保留、原窗口字面值保持。仅本日报及daily-20260123缓存范围的unstaged与cached diff检查均通过；未stage、commit或push。先前本轮格式校验因第二source表/候选重复header产生误计，已只修新增结构后通过，未改validator、原候选或有效原审阅；机器不替代下述独立语义验收。

本轮准入校准已实际读首批14595/14936/15188/14850/14343完整题摘并通过具体关闭理由、允许14472/14625/Qwen继续标准5；后包14606/14270/14980/14855/14968/14466等代表完整题摘复核，HyNeA准入5。14610被指出leaf正确而coarse失败的新反侧后定点重开，root已实际核HCA定义、Table5条件集合、§1/Table2 GT诊断与§4.3.1同模型推理反侧，5/Only限定通过，不把共同错误扩为所有应用论文全文队列。19实际完整AB中4paper新增、15贡献前关闭；50原候选证据/评分及原§4连续正文保持有效，不重复授分或移动日期。root已实际核HyNeA §3.2–3.3/必要Tables1–3及Qwen wheel655/753/834，二者5/Only限定通过；root已实际核14472方法/训练/有限评价及14625 Eq6–15、Table4/§5.2/V100/BigGAN反側，两者5/Only限定通过；新4paper公开日期由官方availability/final-ID分配与scoped raw registered4值联合核，Qwen exact-wheel上传身份核过。root已最终实际读六部分并授予DAY：Jan22补充窗/原50与时间包络保持、14来源有限主题/query停止、19AB漏斗4paper+artifact5、5×5分标准必要证据/Only及外部隔离/重开一致；0新增Books写入，不存在POST伪完成。外部缺段不授Coverage/Evidence，不用旧状态字段代替本轮DAY。
