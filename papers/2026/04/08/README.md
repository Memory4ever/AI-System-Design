# Daily Research — 2026-04-08

**规范：** V3
**窗口：** 2026-04-07T09:00:00+08:00 ～ 2026-04-08T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-14T08:49:34+08:00
**窗口说明：** 按用户授权保留已有候选整行、日期、分项评分、原09→09窗口及连续原§4，只补前一完整自然日遗漏；不搬移旧材料归属。
**补充窗口：** 2026-04-07 ～ 2026-04-07
**冻结候选日期：** [原报告](../_sources/daily-20260408/baseline-before-supplement-20261014.md)

## 1. 结论

本次仅补2026-04-07北京时间完整自然日。原32家族的整行、日期、评分、原09→09窗口及连续原§4保留于[本次基线](../_sources/daily-20260408/baseline-before-supplement-20261014.md)，不搬移旧材料归属；未变化的必要证据、Books实际正文及独立写后复核分层复用，不沿旧完成标签授本轮日级验收。

新增61唯一家族：33整合（30本轮真实新写、3既有真实正文/有效POST复用）、24具体已有覆盖、2仅报告、2中心争议暂缓。新增59项已完成其必要证据审阅，另外03307推理接口和04722性能单位中心冲突已读到关键反证并隔离，不算正面Evidence通过。合原32后，正式候选93家族＝48整合、40具体已有覆盖、2仅报告、3争议暂缓；原32为15整合、16已有覆盖、05217理论争议1。30本轮新写正文、完整局部邻接和作者本人来源注均已有实际非writer POST；另3处既有真实正文与21旧具体NC等有效层经本日具名复核复用，未再写同义书稿。

新增长期差额主要涉及集合检索/蒸馏人口、无损压缩的resident与解码生命周期、动态跨模态低秩接口、表示可分解性proxy、head后验与全backbone重采样成本、stored-latent动作PPO、weight与logits谱、生成空间/velocity/中间判定分支、event producer、密度比/优势调制/可达reward、合并及整数/LUT执行路径、评价四cell/网络effects等。作者局部数据、理论假设、预算混杂、质量反退和失败回退均保留在§4；没有运行作者实验、核代码或证明生产保证。

发现层与贡献分母分开：四有界主题查询返回168/31/93/205个跨组未去重命中，12分类本批相关标题只作有限查漏；25完整v1题摘准入校准与2个含糊条目的必要core裁决按具体增量开展。旧43日期隔离线索仅作有限日期/有效Source层投影，其中41由组合日门支持Apr07并纳入新增61，03263/03675继续隔离；它们不是43项强制全文队列。原567去重发现库存和原32有效层的恢复过程仍在[原存档](../_sources/daily-20260408/V2_1_REPORT_ARCHIVE.md)及[原独核](../_sources/daily-20260408/V3_INDEPENDENT_GATE.md)，不称为本补窗新论文数。

14每日来源已按§2实际停止范围处理；五必要历史子入口和具名日期/中心争议按§5隔离，不据它们支持正面Coverage、Books或无遗漏。非报告作者resume_apr08_review已实际完整六部分DAY通过；来源、候选、Books与报告没有未处理的可执行工作，所有窄锁已释放。[本日恢复记录](../_sources/daily-20260408/SUP_REVIEW_20261014.md)保留实际范围及分层复核。

## 2. 来源覆盖

下表仅投影补充自然日Apr07。机构原始列表/date字段实际顺读，原件和request保留在[本日来源投影及R28](../_sources/daily-20260408/SUP_REVIEW_20261014.md)；表内R为同月daily-20260405/SUP_<name>_20261013.raw及同名request（10-13实际请求），这些已核有效公开列表仅作原始字段复用，本轮只读取Apr07日期段，不继承另一日的候选或Coverage标签。重要release按原有效日层有限复用，不把组织新仓数量代作release，也不扩每周/任意commit扫描。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | R openai-rss当前1287item实际date投影，Apr06T10Z Fellowship→Apr08T05Z/14Z跨完整Apr07；无Apr07News项。Research原件只能current/保护页，无可靠历史分页 | 受阻 | RSS不等全Research；官方Apr07 Research/Publication原始历史目录到达定点补，不支持该子入口零命中 |
| SRC-ANTHROPIC | R anthropic嵌入publishedOn actual Apr02T10:56Z→Apr07T09:35Z Mythos→Apr09T16:34Z；本日同Mythos事件已原32有效审阅去重 | 已检查 | 不重评分，不由未披露漏洞外推安全 |
| SRC-GOOGLE-AI | [Apr Blog归档](https://research.google/blog/2026/04/)实际9条到Apr03，Apr03→Apr08跨目标日；DeepMind原有效page3 24条May→Jan，GemmaApr02/RoboticsApr14。Publications当前year/venue不支持日级历史首发 | 受阻 | Blog/selectedpub不代全Publication；精确Apr07官方公开历史记录到达只补此子入口 |
| SRC-META-AI | 本次web实际[publication页1](https://ai.meta.com/results/?content_types%5B0%5D=publication)、[页2](https://ai.meta.com/results/?content_types%5B0%5D=publication&page=2)、[页3](https://ai.meta.com/results/?content_types%5B0%5D=publication&page=3)近期段：Oct02→Jul17、Jul13→Apr16、Apr14/Apr09→Mar26（至Jan02）；旧Blog有效Apr08→Apr06。04746 Apr09收录与Apr07原arXiv为同家族，不搬首发 | 已检查 | 旧HTTP500不是全source现阻塞；只恢复三页近期段，尾部混合2016–2020历史项不作全catalog逐项队列或全站召回保证 |
| SRC-QWEN | R qwen40条actual extra.date，Apr02T04+08→Apr15T10+08，余Apr18/22/28/30；有效静态60项分层复用；重要release原层无Apr07事件 | 已检查 | 动态次序不全排序，实际读全40date，不以CMS updated/标题判日期；官网不替未列论文 |
| SRC-DEEPSEEK | R deepseek-home/deepseek；reader实际有限恢复官方news/page-79e934c891ab4d7a.js资源：Research g数组全31项Jun24→Feb25→2023Nov02，查看全部仅从slice10扩为全g；News raw完整posts16项Apr24→2025Dec01→2024Jul25。两目录实际越过Apr07无条目，重要release原层复用 | 已检查 | UI点击/状态读取超时不声称成功；使用页面实际引用的官方bundle明确按钮/完整数据，非全org零论文/全site保证 |
| SRC-MOONSHOT | R moonshot Blog可读列表仅到2025Nov07/Nov06；原重要kimi-cli release100至2025Oct24日层复用无Apr07 | 受阻 | Blog不覆盖2026窗口，官方Apr07原始历史条目/页面到达只补该子入口；不以空列表授零 |
| SRC-TENCENT-HUNYUAN | R hunyuan publicList9/9；actual display Apr23/Apr30→Feb13，Hy3preview displayApr22T16Z与publicAtJul06不同，分别保原字段；T1有效release空 | 已检查 | 只官网all公开列表，不把后期CMS publicAt重命名首发；未列作者稿arXiv另查 |
| SRC-ZAI | R zai Research id157 GLM5.1显示Apr07但CMS createAtApr07T16Z，精确时区/原始首发未证；其core原有效EX是能力/案例未披露新可核机制，不把版本名retain；GLM5有效release空 | 已检查 | 贡献前具体EX不用不影响处置日期无限恢复；不据CMS改原日期，不支持8小时自主或通用能力保证 |
| SRC-BYTEDANCE-SEED | R seed-papers type1/page_token40,count20返回18（total243/next60），actualApr08T16Z→Apr07T16Z→Mar31T12Z越过完整Apr07；Blogtype2/page0返回15，Apr08T16Z→Mar31T16Z（至2025Dec） | 已检查 | Apr07T16Z为BJT Apr08，不纳补窗；07026 CMS早于其v1提交已有必要日期隔离，不用CMS单值收论文；暂缓Science领域 |
| SRC-BAIDU-ERNIE | R ernie Blogactual Apr30/Apr15→Feb06；有效ERNIE唯一release2025Jun30无Apr07 | 已检查 | 公开目录/重要artifact有界处理，不全commit |
| SRC-XIAOMI-MIMO | R mimo Paper8条Jun29→Mar13→Feb03；Blog15项无日戳，有效必要路由未得原首发；重要MiMo release空 | 受阻 | 必要undatedBlog历史身份/首发未证，不称本日零；官方Apr07原始时间/当时正文到达只补对应项 |
| SRC-MINIMAX | R minimaxEN完整12项May26→Mar18；ZH Apr27→Mar18。R minimax-techblog实际3篇Sep19/Sep22/Oct08，没有Apr历史公开段；旧M2.7release空 | 受阻 | 不沿旧唯一May13目录授本日覆盖；AgentTechBlog Apr07原始目录/已公开时间到达定点补，当前3篇不等历史零 |
| SRC-ARXIV | 四本日有界主题API168/31/93/205各单页total/entry已核；12分类本批相关标题补检，25首AB+2反向core独核；旧43已知有效线索仅必要date/Source/Books层投影，原32去重 | 已检查 | 不将全年/月库存称当日贡献、未授互联网无遗漏；03675/03263异常与03307/04722中心争议另隔离，不依Updated孤字段 |

五个必要历史子入口已穷尽当前可用的有限原始入口后隔离；具体身份、不能采用的理由和定点重开条件见§5。已检查仅指上述公开范围处理完成，既不等于全站召回，也不证明所有原件主张。DeepSeek UI展开超时不称操作成功，实际闭合依据是页面引用的官方完整数据bundle。

## 3. 候选与判断

下表合计93唯一家族，前32为授权冻结的旧候选整行，后61为仅Apr07自然日补充（33整合/24已有覆盖/2仅报告/2争议）。旧31项arXiv的08:00～09:00仍为原组合证据的有界推断，不把单Submitted、Updated或DOI created当公告时刻；新增公开日期同样由本家族身份与官方first-announcement规则、相邻批界/OAI及精确版本日值组合支持，不追逐分钟。两组未重复评分或搬移归属；5跨09点、03263/03675等必要日期未定项见§5，不列确定候选。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Claude Mythos Preview's cybersecurity capabilities](https://www.anthropic.com/research/mythos-preview) | 2026-04-07T17:35:00+08:00 | 漏洞proposal、重现、严重性与披露分账；1+2+2=5 | 标准完成 | 已有覆盖：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)、PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Cactus: Accelerating Auto-Regressive Decoding with Constrained Acceptance Speculative Sampling](https://arxiv.org/html/2604.04987v1) | 2026-04-08T08:00:00+08:00 ～ 2026-04-08T09:00:00+08:00 | 显式divergence预算与exact verifier sampling不同；条件预算不等于最终算法预算；2+2+2=6 | 深入完成 | 整合：INFER-SPECULATIVE-DECODING [Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md)有损分支的条件h与最终h_alg、隐式Γ及exact fallback |
| [Measuring the Permission Gate: A Stress-Test Evaluation of Claude Code’s Auto Mode](https://arxiv.org/html/2604.04978v1) | 2026-04-08T08:00:00+08:00 ～ 2026-04-08T09:00:00+08:00 | Edit/Write操作状态绕过shell gate，区分未覆盖与分类误差；2+2+2=6 | 深入完成 | 已有覆盖：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)受保护config/self-state mutation与跨protocol同effect的执行时授权 |
| [Top-K Retrieval with Fixed-Size Linear-Attention Completion: Backbone- and KV-Format-Preserving Attention for KV-Cache Read Reduction](https://arxiv.org/html/2604.05438v1) | 2026-04-08T08:00:00+08:00 ～ 2026-04-08T09:00:00+08:00 | summary补全未读numerator/denominator，扣除已读支持防双计；2+2+2=6 | 深入完成 | 整合：INFER-KV-CACHE [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)exact/residual减除及联合归一化、selector成本与退化边界 |
| [MegaTrain: Full Precision Training of 100B+ Parameter Large Language Models on a Single GPU](https://arxiv.org/html/2604.05091v1) | 2026-04-08T08:00:00+08:00 ～ 2026-04-08T09:00:00+08:00 | CPU权威状态与无持久weight pointers模板、stream事件生命周期；2+2+2=6 | 深入完成 | 整合：TRAIN-ZERO [Ch39](../../../../books/part-04-training-system/39-zero.md)CPU-authoritative流式buffer与layer-template绑定生命周期 |
| [Edit, But Verify: An Empirical Audit of Instructed Code-Editing Benchmarks](https://arxiv.org/html/2604.05100v1) | 2026-04-08T08:00:00+08:00 ～ 2026-04-08T09:00:00+08:00 | 编码oracle须同时验目标改动与未要求区域不变量；失败可来自artifact而非能力；1+2+2=5 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)代码oracle的change/preserve双面合同与diff/AST/coverage不充分边界 |
| [Not All Turns Are Equally Hard: Adaptive Thinking Budgets For Efficient Multi-Turn Reasoning](https://arxiv.org/html/2604.05164v1) | 2026-04-08T08:00:00+08:00 ～ 2026-04-08T09:00:00+08:00 | 回合budget会消耗后续资源，global soft penalty不同于硬cap；1+2+2=5 | 标准完成 | 已有覆盖：AGENT-PLANNING [Ch79](../../../../books/part-07-agent/79-planning.md)belief/remaining-budget控制与hard cap、verification reserve |
| [Nidus: Externalized Reasoning for AI-Assisted Engineering](https://arxiv.org/html/2604.05080v1) | 2026-04-08T08:00:00+08:00 ～ 2026-04-08T09:00:00+08:00 | finite spec/PO外置、mutation前验证；完整性只限建模路径；1+2+2=5 | 标准完成 | 已有覆盖：AGENT-PLATFORM [Ch84](../../../../books/part-07-agent/84-agent-platform.md)protocol-owned mutation与不完备规格边界 |
| [SkillAttack: Automated Red Teaming of Agent Skills through Attack Path Refinement](https://arxiv.org/html/2604.04989v1) | 2026-04-08T08:00:00+08:00 ～ 2026-04-08T09:00:00+08:00 | 不改skill也能经输入/执行路径动态触发潜在漏洞；1+2+2=5 | 深入完成 | 已有覆盖：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)隐藏路径触发、matched no-skill反事实与effect oracle |
| [Can You Trust the Vectors in Your Vector Database? Black-Hole Attack from Embedding Space Defects](https://arxiv.org/html/2604.05480v1) | 2026-04-08T08:00:00+08:00 ～ 2026-04-08T09:00:00+08:00 | 不控制query/encoder的任意向量写入也能挤占Top-K；2+2+2=6 | 深入完成 | 整合：AGENT-RAG [Ch76](../../../../books/part-07-agent/76-rag.md)raw-vector写入信任与hubness、source/content/encoder绑定的工程推断 |
| [Faster Superword Tokenization](https://arxiv.org/html/2604.05192v1) | 2026-04-08T08:00:00+08:00 ～ 2026-04-08T09:00:00+08:00 | 超词merge可保边界候选而不保全部document；同词表/merge不等于同ID；2+2+2=6 | 深入完成 | 整合：MODEL-TOKENIZER [Ch11](../../../../books/part-02-model/11-tokenizer.md)regular/superword两阶段重放与完整token→ID身份 |
| [Spike Hijacking in Late-Interaction Retrieval](https://arxiv.org/html/2604.05253v1) | 2026-04-08T08:00:00+08:00 ～ 2026-04-08T09:00:00+08:00 | pooling改变梯度路由，稀疏判别与spike/长度鲁棒性不能同时用均值代表；2+2+2=6 | 深入完成 | 整合：AGENT-RAG [Ch76](../../../../books/part-07-agent/76-rag.md)hard MaxSim梯度集中、长度/语义spike与选择性取舍 |
| [A Theoretical Framework for Statistical Evaluability of Generative Models](https://arxiv.org/pdf/2604.05324v1) | 2026-04-08T08:00:00+08:00 ～ 2026-04-08T09:00:00+08:00 | metric可计算不等于有限样本对任意分布具有统一ranking保证；2+2+3=7 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)有限iid统一ranking与固定metric计算的区分 |
| [Graph of Skills: Dependency-Aware Structural Retrieval for Massive Agent Skills](https://arxiv.org/pdf/2604.05333v1) | 2026-04-08T08:00:00+08:00 ～ 2026-04-08T09:00:00+08:00 | 相关skill不等于依赖闭合bundle；图扩张也要预算、权限和版本锁；1+2+2=5 | 标准完成 | 已有覆盖：AGENT-PLATFORM [Ch84](../../../../books/part-07-agent/84-agent-platform.md)typed关系、dependency lock、composition admission与joint evaluation |
| [ALTO: Adaptive LoRA Tuning and Orchestration for Heterogeneous LoRA Training Workloads](https://arxiv.org/pdf/2604.05426v1) | 2026-04-08T08:00:00+08:00 ～ 2026-04-08T09:00:00+08:00 | base GEMM与adapter grouped GEMM分开，rank-local adapter梯度而非共享同一adapter batch；2+2+2=6 | 深入完成 | 整合：TRAIN-LORA [Ch30](../../../../books/part-04-training-system/30-lora.md)base/grouped adapter执行分离与rank-local状态 |
| [Attention Editing: A Versatile Framework for Cross-Architecture Attention Conversion](https://arxiv.org/html/2604.05688v1) | 2026-04-08T08:00:00+08:00 ～ 2026-04-08T09:00:00+08:00 | 先teacher输入局部activation对齐，再student全网络输出蒸馏，避免随机attention级联误差；2+2+2=6 | 深入完成 | 整合：MODEL-SELF-ATTENTION [Ch14](../../../../books/part-02-model/14-self-attention.md)teacher输入局部对齐→student全路径蒸馏的转换分支 |
| [DualDiffusion: A Speculative Decoding Strategy for Masked Diffusion Models](https://arxiv.org/html/2604.05250v1) | 2026-04-08T08:00:00+08:00 ～ 2026-04-08T09:00:00+08:00 | stale drafter KV→bidirectional verifier→remask不保持exact目标，任务质量可能明显退化；1+2+2=5 | 标准完成 | 已有覆盖：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)provisional修正与exact/近似分账 |
| [Uncovering Linguistic Fragility in Vision-Language-Action Models via Diversity-Aware Red Teaming](https://arxiv.org/html/2604.05595v1) | 2026-04-08T08:00:00+08:00 ～ 2026-04-08T09:00:00+08:00 | 先核语言必要性；多样失败须语义/长度有效性，模拟失败不等于物理安全率；1+2+2=5 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)模态必要性与有效扰动；MULTIMODAL-EMBODIED-VLA [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)真机边界 |
| [SnapFlow: One-Step Action Generation for Flow-Matching VLAs via Progressive Self-Distillation](https://arxiv.org/html/2604.05656v1) | 2026-04-08T08:00:00+08:00 ～ 2026-04-08T09:00:00+08:00 | 单点FM条件velocity的无偏性不自动迁到consistency全导数平方；自产生边际shortcut有独立适用边界；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)conditional/marginal监督在全导数平方目标下的非等价边界 |
| [Generative Retrieval Overcomes Limitations of Dense Retrieval but Struggles with Identifier Ambiguity](https://arxiv.org/html/2604.05764v1) | 2026-04-08T08:00:00+08:00 ～ 2026-04-08T09:00:00+08:00 | 生成检索避免单向量表达上限，却把歧义移入document identifier及beam；2+2+2=6 | 深入完成 | 整合：AGENT-RAG [Ch76](../../../../books/part-07-agent/76-rag.md)生成document-ID歧义、beam与lexical fallback |
| [Broken by Default: A Formal Verification Study of Security Vulnerabilities in AI-Generated Code](https://arxiv.org/html/2604.05292v1) | 2026-04-08T08:00:00+08:00 ～ 2026-04-08T09:00:00+08:00 | pattern、形式见证与可达runtime漏洞必须分账；1+2+2=5 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)、PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)证明scope与可执行重现 |
| [Your LLM Agent Can Leak Your Data: Data Exfiltration via Backdoored Tool Use](https://arxiv.org/html/2604.05432v1) | 2026-04-08T08:00:00+08:00 ～ 2026-04-08T09:00:00+08:00 | weight后门可借正常memory与retrieval渠道外发，检索返回也能再触发；1+2+2=5 | 深入完成 | 已有覆盖：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)模型供应链、检索egress与跨回合再触发 |
| [Confidence Should Be Calibrated More Than One Turn Deep](https://arxiv.org/html/2604.05397v1) | 2026-04-08T08:00:00+08:00 ～ 2026-04-08T09:00:00+08:00 | pooled ECE可能抵消不同turn的失准，history条件改变校准分布；1+2+2=5 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)隐藏calibration regime与部署slice |
| [Multi-Drafter Speculative Decoding with Alignment Feedback](https://arxiv.org/html/2604.05417v1) | 2026-04-08T08:00:00+08:00 ～ 2026-04-08T09:00:00+08:00 | 轮次级alignment反馈选择单drafter，探索/切换/KV修复与接受长度共同记账；2+2+2=6 | 深入完成 | 整合：INFER-SPECULATIVE-DECODING [Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md)round级alignment选择、探索/切换与缺失KV成本 |
| [ClawsBench: Evaluating Capability and Safety of LLM Productivity Agents in Simulated Workspaces](https://arxiv.org/html/2604.05172v1) | 2026-04-08T08:00:00+08:00 ～ 2026-04-08T09:00:00+08:00 | mock API保真及skill/harness干预会改变能力与安全排序；1+2+2=5 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)执行身份、模拟保真与安全切片 |
| [Beyond Accuracy: Unveiling Inefficiency Patterns in Tool-Integrated Reasoning](https://arxiv.org/html/2604.05404v1) | 2026-04-08T08:00:00+08:00 ～ 2026-04-08T09:00:00+08:00 | tool pause导致KV失效时，token数不是重复prefill/decode工作量；1+2+2=5 | 标准完成 | 已有覆盖：PLATFORM-COST [Ch70](../../../../books/part-06-ai-infrastructure/70-cost.md)state-dependent work与PTE proxy |
| [Don't Act Blindly: Robust GUI Automation via Action-Effect Verification and Self-Correction](https://arxiv.org/html/2604.05477v1) | 2026-04-08T08:00:00+08:00 ～ 2026-04-08T09:00:00+08:00 | 上一action的expected effect须经下一observation验证，不由执行成功声明替代；1+2+2=5 | 标准完成 | 已有覆盖：AGENT-REFLECTION [Ch80](../../../../books/part-07-agent/80-reflection.md)execution evidence与verification-centric repair |
| [See the Forest for the Trees: Loosely Speculative Decoding via Visual-Semantic Guidance for Efficient Inference of Video LLMs](https://arxiv.org/html/2604.05650v1) | 2026-04-08T08:00:00+08:00 ～ 2026-04-08T09:00:00+08:00 | 视觉相关proxy决定哪些token放宽匹配；保task分数不等于保target分布；1+2+2=5 | 标准完成 | 已有覆盖：INFER-SPECULATIVE-DECODING [Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md)近似verification/质量与正确性owner |
| [HybridKV: Hybrid KV Cache Compression for Efficient Multimodal Large Language Model Inference](https://arxiv.org/html/2604.05887v1) | 2026-04-08T08:00:00+08:00 ～ 2026-04-08T09:00:00+08:00 | prompt-local head role决定不可逆pruning或可回读cold KV，不能冻结为model常量；1+2+2=5 | 标准完成 | 已有覆盖：INFER-KV-CACHE [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)head-aware hot/cold、drift及policy identity |
| [The Illusion of Latent Generalization: Bi-directionality and the Reversal Curse](https://arxiv.org/html/2604.04943v1) | 2026-04-08T08:00:00+08:00 ～ 2026-04-08T09:00:00+08:00 | 来源实体是否成为预测目标决定受限反向检索，行为成功不证明统一表示；2+2+2=6 | 深入完成 | 整合：TRAIN-PRETRAINING [Ch28](../../../../books/part-04-training-system/28-pretraining.md)目标支持、双向访问与线性probe边界 |
| [Memory Dial: A Training Framework for Controllable Memorization in Language Models](https://arxiv.org/html/2604.05074v1) | 2026-04-08T08:00:00+08:00 ～ 2026-04-08T09:00:00+08:00 | 双温度CE组合与matched seen/heldout/diversity，将额外记忆压力作为实验轴而非纯开关；2+2+2=6 | 深入完成 | 整合：TRAIN-PRETRAINING [Ch28](../../../../books/part-04-training-system/28-pretraining.md)记忆—泛化objective分支及匹配验收 |
| [On the Geometry of Positional Encodings in Transformers](https://arxiv.org/pdf/2604.05217v1) | 2026-04-08T08:00:00+08:00 ～ 2026-04-08T09:00:00+08:00 | 位置分离与几何最优性会改变设计解释，但证明桥梁与stress最优存在具体争议；2+1+2=5 | 深入完成 | 暂缓：MODEL-POSITION-ENCODING [Ch13](../../../../books/part-02-model/13-position-encoding.md)，争议理论不作正面整合 |
| [Scaling DPPs for RAG: Density Meets Diversity](https://arxiv.org/html/2604.03240v1) | 2026-04-07 | 固定初检→子集专用Gram adapter/set margin→集合packing选择；2+1+2=5 | 深入完成 | 整合：AGENT-RAG [Ch76](../../../../books/part-07-agent/76-rag.md) |
| [Rewriting TTS Inference Economics: Lightning V2 on Tenstorrent Achieves 4x Lower Cost Than NVIDIA L40S](https://arxiv.org/html/2604.03279v1) | 2026-04-07 | 局部PCC近1仍音质下降→precision与outcome双面验收；1+2+2=5 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [ENEC: A Lossless AI Model Compression Method Enabling Fast Inference on Ascend NPUs](https://arxiv.org/html/2604.03298v1) | 2026-04-07 | 受限NPU block可逆exponent表示与依赖解耦→resident/解码取舍；2+2+2=6 | 深入完成 | 整合：INFER-GPU-MEMORY [Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md) |
| [V-Reflection: Transforming MLLMs from Passive Observers to Active Interrogators](https://arxiv.org/html/2604.03307v1) | 2026-04-07 | 训练grounding蒸馏与推理slot producer存在中心冲突→不授serving接口；2+1+2=5 | 争议 | 暂缓：MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)；见§5精确重开 |
| [CoLA: Cross-Modal Low-rank Adaptation for Multimodal Downstream Tasks](https://arxiv.org/html/2604.03314v1) | 2026-04-07 | paired modality生成低秩middle map→静态与动态adapter分账；2+1+2=5 | 深入完成 | 整合：TRAIN-LORA [Ch30](../../../../books/part-04-training-system/30-lora.md) |
| [MetaSAEs: Joint Training with a Decomposability Penalty Produces More Atomic Sparse Autoencoder Latents](https://arxiv.org/html/2604.03436v1) | 2026-04-07 | decoder可分解性critic正则→geometry proxy与真概念分账；2+1+2=5 | 深入完成 | 整合：WORLDVIEW-REPRESENTATION [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) |
| [Scalable Variational Bayesian Fine-Tuning of LLMs via Orthogonalized Low-Rank Adapters](https://arxiv.org/html/2604.03388v1) | 2026-04-07 | 一次backbone＋Bayesian last-head MC→posterior scope/成本取舍；2+2+2=6 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Drift-Based Policy Optimization: Native One-Step Policy Learning for Online Robot Control](https://arxiv.org/html/2604.03540v1) | 2026-04-07 | 单步动作generator＋stored latent conditional PPO→joint与执行prefix credit；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [Compressible Softmax-Attended Language under Incompressible Attention](https://arxiv.org/html/2604.04384v1) | 2026-04-07 | weight与输入logits谱不同→低effective rank不授压缩保证；2+1+2=5 | 深入完成 | 整合：MODEL-SELF-ATTENTION [Ch14](../../../../books/part-02-model/14-self-attention.md) |
| [Training Transformers in Cosine Coefficient Space](https://arxiv.org/html/2604.04440v1) | 2026-04-07 | 训练DCT坐标每forward重构dense→参数节省与物化费用分账；2+1+2=5 | 深入完成 | 整合：TRAIN-PRETRAINING [Ch28](../../../../books/part-04-training-system/28-pretraining.md) |
| [SLaB: Sparse-Lowrank-Binary Decomposition for Efficient Large Language Models](https://arxiv.org/html/2604.04493v1) | 2026-04-07 | 显式sign×rank-one magnitude＋稀疏残差→非低秩执行/metadata费用；2+1+2=5 | 深入完成 | 整合：INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Isokinetic Flow Matching for Pathwise Straightening of Generative Flows](https://arxiv.org/html/2604.04491v1) | 2026-04-07 | 保FM＋self-lookahead velocity正则→非endpoint flowmap或一步保证；2+1+2=5 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Beyond Hard Negatives: The Importance of Score Distribution in Knowledge Distillation for Dense Retrieval](https://arxiv.org/html/2604.04734v1) | 2026-04-07 | teacher score-spectrum采样→hard-only窄标签人口反侧；2+1+2=5 | 深入完成 | 整合：AGENT-RAG [Ch76](../../../../books/part-07-agent/76-rag.md) |
| [Training-Free Refinement of Flow Matching with Divergence-based Sampling](https://arxiv.org/html/2604.04646v1) | 2026-04-07 | 同t按divergence代理选附近state→不同temporal solver且改distribution；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Firebolt-VL: Efficient Vision-Language Understanding with Cross-Modality Modulation](https://arxiv.org/html/2604.04579v1) | 2026-04-07 | token-grid context经FiLM调SSM→有限connector消费而非全decoder保证；2+1+2=5 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [Think in Strokes, Not Pixels: Process-Driven Image Generation via Interleaved Reasoning](https://arxiv.org/html/2604.04746v1) | 2026-04-07 | partial instruction/global请求与draft/local指令双判→未完成不等错误；2+1+2=5 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Undetectable Conversations Between AI Agents via Pseudorandom Noise-Resilient Key Exchange](https://arxiv.org/html/2604.04757v1) | 2026-04-07 | 受限keyless honest-transcript反例→passive审计排除边界；2+2+2=6 | 深入完成 | 整合：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [E-VLA: Event-Augmented Vision-Language-Action Model for Dark and Blurred Scenes](https://arxiv.org/html/2604.04834v1) | 2026-04-07 | recent-N event窗口截至RGB exposure→variable freshness与fusion费用；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [Are Latent Reasoning Models Easily Interpretable?](https://arxiv.org/html/2604.04902v1) | 2026-04-07 | early agreement与可解码trace不等正确/必要真实过程；2+2+2=6 | 深入完成 | 已有覆盖：MODEL-SELF-ATTENTION [Ch14](../../../../books/part-02-model/14-self-attention.md) |
| [Vero: An Open RL Recipe for General Visual Reasoning](https://arxiv.org/html/2604.04917v1) | 2026-04-07 | typed reward＋mixture局部negative-transfer→条件人口/质量分账；2+2+2=6 | 标准完成 | 已有覆盖：TRAIN-DATA [Ch27](../../../../books/part-04-training-system/27-data.md) |
| [ClawArena: Benchmarking AI Agents in Evolving Information Environments](https://arxiv.org/html/2604.04202v1) | 2026-04-07 | 动态GT/belief revision与workspace outcome分评；2+2+2=6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Three Phases of Expert Routing: How Load Balance Evolves During Mixture-of-Experts Training](https://arxiv.org/html/2604.04230v1) | 2026-04-07 | MFG proxy/phase非普遍→只保受限routing诊断；2+1+2=5 | 标准完成 | 仅报告：MODEL-MOE [Ch21](../../../../books/part-02-model/21-moe.md)；局部诊断/预算比较不改变长期机制 |
| [Combee: Scaling Prompt Learning for Self-Improving Language Model Agents](https://arxiv.org/html/2604.04247v1) | 2026-04-07 | LLM reduce非结合律→bounded fan-in/context version；2+2+2=6 | 标准完成 | 已有覆盖：AGENT-MEMORY [Ch77](../../../../books/part-07-agent/77-memory.md) |
| [3D-Stacked NMP, LLM Decoding, Systolic Array Microarchitecture, Multi-Core Scheduling](https://arxiv.org/html/2604.04253v1) | 2026-04-07 | shape/buffer/placement联合→模拟与真实硬件分责；2+2+2=6 | 标准完成 | 已有覆盖：INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [APPA: Adaptive Preference Pluralistic Alignment for Fair Federated RLHF of LLMs](https://arxiv.org/html/2604.04261v1) | 2026-04-07 | frozen本地偏好reward vectors→中央PPO而非fedavg；3+2+2=7 | 深入完成 | 整合：TRAIN-RLHF [Ch31](../../../../books/part-04-training-system/31-rlhf.md)，复用既有真实正文/POST，不计本轮新写 |
| [How Well Do Agentic Skills Work in the Wild: Benchmarking LLM Skill Usage in Realistic Settings](https://arxiv.org/html/2604.04323v1) | 2026-04-07 | Skill loaded/selected/retrieved/adapted分层真实controlpath；2+2+2=6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [GENSERVE: Efficient Co-Serving of Heterogeneous Diffusion Model Workloads](https://arxiv.org/html/2604.04335v1) | 2026-04-07 | 两deadline＋step VideoState恢复共置→总命中与video尾分账；2+2+2=6 | 深入完成 | 整合：INFER-SCHEDULING [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md)，复用既有真实正文/POST，不计本轮新写 |
| [GUIDE: Interpretable GUI Agent Evaluation via Hierarchical Diagnosis](https://arxiv.org/html/2604.04399v1) | 2026-04-07 | recoverable subtask聚合→非step hardAND/终局叙述；2+2+2=6 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Relative Density Ratio Optimization for Stable and Statistically Consistent Model Alignment](https://arxiv.org/html/2604.04410v1) | 2026-04-07 | 混合density bounded ratio→非参数梯度/偏好真值保证；2+1+2=5 | 深入完成 | 整合：TRAIN-DPO [Ch34](../../../../books/part-04-training-system/34-dpo.md) |
| [ShieldNet: Network-Level Guardrails against Emerging Supply-Chain Injections in Agentic Systems](https://arxiv.org/pdf/2604.04426v1) | 2026-04-07 | MITM/PCAP network-effect sensor→host盲区/已泄露不可撤；2+2+2=6 | 深入完成 | 整合：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Beyond Few-Step Inference: Accelerating Video Diffusion Transformer Model Serving with Inter-Request Caching Reuse](https://arxiv.org/html/2604.04451v1) | 2026-04-07 | 跨request分时段/区域features reuse→近prompt非KV等价；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [HDP: A Lightweight Cryptographic Protocol for Human Delegation Provenance in Agentic AI Systems](https://arxiv.org/pdf/2604.04522v1) | 2026-04-07 | issuer单key provenance≠named-agent亲签/即时离线撤销；2+2+2=6 | 深入完成 | 已有覆盖：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Multilingual Prompt Localization for Agent-as-a-Judge: Language and Backbone Sensitivity in Requirement-Level Evaluation](https://arxiv.org/html/2604.04532v1) | 2026-04-07 | judge语言改变需求判定→solver与evaluator身份分开；2+1+2=5 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Mapping the Exploitation Surface: A 10,000-Trial Taxonomy of What Makes LLM Agents Exploit Vulnerabilities](https://arxiv.org/html/2604.04561v1) | 2026-04-07 | goal reframing局部反证→叙述不授dispatch/effect权限；2+2+2=6 | 深入完成 | 已有覆盖：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [The Energy Cost of Execution-Idle in GPU Clusters](https://arxiv.org/html/2604.04745v1) | 2026-04-07 | execution-idle与deep idle分母→驻留节能/尾成本；2+2+3=7 | 深入完成 | 整合：PLATFORM-COST [Ch70](../../../../books/part-06-ai-infrastructure/70-cost.md)，复用既有真实正文/POST，不计本轮新写 |
| [DeepStack: Scalable and Accurate Design Space Exploration for Distributed 3D-Stacked AI Accelerators](https://arxiv.org/html/2604.04750v1) | 2026-04-07 | 硬件/parallel plan联合DSE→模型误差与thermal限制；2+2+2=6 | 标准完成 | 已有覆盖：INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Your Agent, Their Asset: A Real-World Safety Analysis of OpenClaw](https://arxiv.org/html/2604.04759v1) | 2026-04-07 | self-state/harness持久毒化→load/activation再admission；2+2+2=6 | 深入完成 | 已有覆盖：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [GPU Acceleration of TFHE-Based High-Precision Nonlinear Layers for Encrypted LLM Inference](https://arxiv.org/pdf/2604.04783v1) | 2026-04-07 | TFHE PBS精度/batch/转换→隐私执行边界非LLM实测；2+2+2=6 | 深入完成 | 已有覆盖：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Full-Duplex-Bench-v3: Benchmarking Tool Use for Full-Duplex Voice Agents Under Real-World Disfluency](https://arxiv.org/html/2604.04847v1) | 2026-04-07 | duplex tool/content四时刻→首响应不代真实完成；2+2+2=6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [The Role of Generator Access in Autoregressive Post-Training](https://arxiv.org/html/2604.04855v1) | 2026-04-07 | chosen-prefix control与logit observation分轴；2+2+2=6 | 深入完成 | 整合：TRAIN-GRPO [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [Synthetic Sandbox for Training Machine Learning Engineering Agents](https://arxiv.org/pdf/2604.04872v1) | 2026-04-07 | synthetic spec/evaluator先可执行→cheap训练非测试SLO；2+2+2=6 | 标准完成 | 已有覆盖：AGENT-WORKFLOW [Ch81](../../../../books/part-07-agent/81-workflow.md) |
| [Rethinking Exploration in RLVR: From Entropy Regularization to Refinement via Bidirectional Entropy Modulation](https://arxiv.org/html/2604.04894v1) | 2026-04-07 | binary group成功率两符号advantage modulation；2+1+2=5 | 深入完成 | 整合：TRAIN-GRPO [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [A Frame is Worth One Token: Efficient Generative World Modeling with Delta Tokens](https://arxiv.org/pdf/2604.04913v1) | 2026-04-07 | delta history与spatial anchor不同consumer→BoM非概率校准；2+2+3=7 | 深入完成 | 整合：MULTIMODAL-WORLD-MODELS [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [TriAttention: Efficient Long Reasoning with Trigonometric KV Compression](https://arxiv.org/html/2604.04921v1) | 2026-04-07 | preRoPE统计/模型校准身份/cadence→递归反退；2+2+2=6 | 标准完成 | 已有覆盖：INFER-KV-CACHE [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [RoboPhD: Evolving Diverse Complex Agents Under Tight Evaluation Budgets](https://arxiv.org/html/2604.04347v1) | 2026-04-07 | 有限evaluation预算recipe比较→非通用autoresearch支配；2+1+2=5 | 标准完成 | 仅报告：AGENT-WORKFLOW [Ch81](../../../../books/part-07-agent/81-workflow.md)；局部诊断/预算比较不改变长期机制 |
| [Decocted Experience Improves Test-Time Inference in LLM Agents](https://arxiv.org/pdf/2604.04373v1) | 2026-04-07 | derived lesson/late construction→相关性非当前utility；2+2+2=6 | 标准完成 | 已有覆盖：AGENT-MEMORY [Ch77](../../../../books/part-07-agent/77-memory.md) |
| [Don't Blink: Evidence Collapse during Multimodal Reasoning](https://arxiv.org/html/2604.04207v1) | 2026-04-07 | 任务条件视觉sensor/entropy迁移反退→无truth权；2+1+2=5 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [REAM: Merging Improves Pruning of Experts in LLMs](https://arxiv.org/html/2604.04356v1) | 2026-04-07 | permutation合并artifact＋逐层校准→非runtime裁route；2+2+2=6 | 深入完成 | 整合：MODEL-MOE [Ch21](../../../../books/part-02-model/21-moe.md) |
| [DP-OPD: Differentially Private On-Policy Distillation for Language Models](https://arxiv.org/html/2604.04461v1) | 2026-04-07 | student-release DP不保护teacher/API所见prompt；2+2+2=6 | 深入完成 | 已有覆盖：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Beyond Fixed Tests: Repository-Level Issue Resolution as Coevolution of Code and Behavioral Constraints](https://arxiv.org/html/2604.04580v1) | 2026-04-07 | code/test共同fitness→独立contract/hidden oracle；2+2+2=6 | 深入完成 | 已有覆盖：AGENT-WORKFLOW [Ch81](../../../../books/part-07-agent/81-workflow.md) |
| [From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism](https://arxiv.org/html/2604.04648v1) | 2026-04-07 | frozen RM-feature OOD penalty→受限pool soft-risk选择；2+2+2=6 | 标准完成 | 已有覆盖：TRAIN-RLHF [Ch31](../../../../books/part-04-training-system/31-rlhf.md) |
| [Cog-DRIFT: Exploration on Adaptively Reformulated Instances Enables Learning from Hard Reasoning Problems](https://arxiv.org/html/2604.04767v1) | 2026-04-07 | MC/cloze/open课程改变可达reward→原任务迁移另验；2+1+2=5 | 深入完成 | 整合：TRAIN-GRPO [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [How Alignment Routes: Localizing, Scaling, and Controlling Policy Circuits in Language Models](https://arxiv.org/html/2604.04385v1) | 2026-04-07 | 低DLA gate可必要→多位置因果控制不由读出贡献认证；2+1+3=6 | 深入完成 | 已有覆盖：MODEL-SELF-ATTENTION [Ch14](../../../../books/part-02-model/14-self-attention.md) |
| [Justified or Just Convincing? Error Verifiability as a Dimension of LLM Quality](https://arxiv.org/html/2604.04418v1) | 2026-04-07 | AO verdict×真实correctness四cell→verifiability非accuracy；2+2+3=7 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [MUXQ: Mixed-to-Uniform Precision MatriX Quantization via Low-Rank Outlier Decomposition](https://arxiv.org/html/2604.04701v1) | 2026-04-07 | integer body/aux重组替FP旁路→fakequant非NPUkernel；2+1+2=5 | 深入完成 | 整合：INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Don't Waste Bits! Adaptive KV-Cache Quantization for Lightweight On-Device LLMs](https://arxiv.org/html/2604.04722v1) | 2026-04-07 | 自适应KV controller时间单位/packed测量中心冲突；2+1+2=5 | 争议 | 暂缓：INFER-KV-CACHE [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)；见§5精确重开 |
| [Preservation Is Not Enough for Width Growth: Regime-Sensitive Selection of Dense LM Warm Starts](https://arxiv.org/html/2604.04281v1) | 2026-04-07 | width selector horizon/regime可翻转→function保留非轨迹；2+1+2=5 | 深入完成 | 整合：TRAIN-PRETRAINING [Ch28](../../../../books/part-04-training-system/28-pretraining.md) |
| [Hallucination Basins: A Dynamic Framework for Understanding and Controlling LLM Hallucinations](https://arxiv.org/html/2604.04743v1) | 2026-04-07 | conditioned failure probe/steering proxy→独立outcome；2+1+2=5 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Beyond the Global Scores: Fine-Grained Token Grounding as a Robust Detector of LVLM Hallucinations](https://arxiv.org/html/2604.04863v1) | 2026-04-07 | ADS空间compactness与CGC语义alignment双轴；2+1+2=5 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Agentic Code Optimization via Compiler-LLM Cooperation](https://arxiv.org/html/2604.04238v1) | 2026-04-07 | compiler finite oracle/零cost calls→contract与budget shape；2+1+2=5 | 标准完成 | 已有覆盖：AGENT-WORKFLOW [Ch81](../../../../books/part-07-agent/81-workflow.md) |
| [LOCALUT: Harnessing Capacity-Computation Tradeoffs for LUT-Based Inference in DRAM-PIM](https://arxiv.org/html/2604.04523v1) | 2026-04-07 | LUT容量/索引/host转换/分层reuse联合费用；2+1+2=5 | 深入完成 | 整合：INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |


## 4. 证据与知识整合

### [On the Geometry of Positional Encodings in Transformers](https://arxiv.org/pdf/2604.05217v1)

官方abs/v1与PDF v1题名/身份相符；Submitted为04-06T22:30:06Z，DataCite v1 Updated为04-08T00:11:32Z，均保留原始字段，归属依§3组合推断而非单字段。理论若成立会改变位置表示的设计解释，故从否定侧恢复为2+1+2=5；证明冲突触发深入审阅，不抬分。独立审阅者已核PDF §§3–5与必要公式，详见[具体审计](../_sources/daily-20260408/V3_INDEPENDENT_GATE.md)。

§3忽略mask和位置时的permutation equivariance在Ch13已有覆盖；不能据此否定后续理论候选。§4把期望中的导数系数与token表示拆为均值乘积，但假设未建立所需独立性和非抵消桥梁；§5混同Hellinger chord与geodesic，又把Gram-Frobenius最优替代distance-stress最优。三个one-hot分布降到一维的合法MDS坐标stress为1/6，另一同维坐标可达1/9，直接反驳该目标下普遍最优的推断。此反例只检验理论，不声称复现benchmark。

Evidence为争议，Books暂缓，不向MODEL-POSITION-ENCODING [Ch13](../../../../books/part-02-model/13-position-encoding.md)写正面理论。重开需要作者勘误或完整证明明确期望分解、非抵消与真实优化目标，纠正chord/geodesic；新增benchmark不能补这条证明链。

### [Claude Mythos Preview's cybersecurity capabilities](https://www.anthropic.com/research/mythos-preview)

官方publishedOn=`2026-04-07T09:35:00.000Z`。采用当窗技术博客，已读零日评价、隔离Claude Code scaffold、文件风险分层、独立模型复核和人类triage。ASan崩溃、漏洞、严重性和exploit不是同一计数；未披露案例无法独立复验，成功故事不能推自主发现率。

Ch72“模型辅助漏洞研究”已有proposal→最小可执行重现→人类severity/披露，以及dual-use、embargo与maintainer成本；Ch66已有artifact/environment/trace和版本化verifier。因此作为受限实践证据判已有覆盖。未披露模型机制、统一precision/长度/并发与生产SLO为Not Disclosed，不合并文章的不同实验。

### [Cactus: Accelerating Auto-Regressive Decoding with Constrained Acceptance Speculative Sampling](https://arxiv.org/html/2604.04987v1)

Exact-v1 §§2.1–2.3、3.1–3.3：允许改变输出分布时，把接受率与分布偏移共同优化。采样token条件h受δ约束，整体h_alg混合各条件分支；Theorem3给含Γ(δ)的界，Γ无闭式；实用KL又用二阶Taylor近似。不证明任务正确率或整序列质量保证。

作者accepted length/rejection只是效率代理；另在A10040GB和Qwen3等drafter/verifier配置测wall-time，不能推生产SLO。Ch48已在有损分支实际补入条件h与最终h_alg、隐式Γ及实用近似求解边界，并保留exact acceptance回退；6分知识缺口深入后整合，不用accepted length替代最终分布与wall-time验收。

### [Measuring the Permission Gate: A Stress-Test Evaluation of Claude Code’s Auto Mode](https://arxiv.org/html/2604.04978v1)

Exact-v1 §§3–6：Sonnet4.6、128个prompt、四类模拟DevOps任务、Docker/shimCLI、600秒/$5上限产生253个state-changing actions。Tier2 Edit/Write直接改operational JSON且无classifier调用；全动作与仅分类Tier3错误率是不同对象，不能与厂商自然流量17%比较。

已实际对读Ch72“Agent自己的Instruction、Config与Memory也是受保护资产”以及跨protocol的canonical typed action/effect-time gate：文件可写不代表高风险semantic mutation已获准，效果相同的action不因工具名或协议不同绕过共同授权。因此operational JSON经Edit/Write即时改变状态，是现有合同已覆盖的具体反例，作者判已有覆盖；不是仅凭“安全”关键词匹配。6分安全override深入保留路径覆盖测试与相同effect权限，只支持作者Docker/shim协议，不证明真实集群同样漏洞或安全完备。本窗归属采用§3所述组合证据的有界推断，非单篇Submitted时点。

### [Top-K Retrieval with Fixed-Size Linear-Attention Completion: Backbone- and KV-Format-Preserving Attention for KV-Cache Read Reduction](https://arxiv.org/html/2604.05438v1)

官方[exact-v1 PDF](https://arxiv.org/pdf/2604.05438v1)与HTML标题相符，旧Residual-Mass标题不继承。已读§§4–8及预算公式：保留原KV，prefill建立正feature-map summary；decode精算anchors/Top-K，扣已读贡献后补近似余项，再统一归一。固定exact-read表不等于预算匹配，summary单次读取须计入摊销。

Llama-3.2-1B-Instruct/Qwen3-1.7B、4k/8k/16k、RULER/BABILong；phi按长度专训，部分Qwen切片变差。穷举Top-K隔离aggregation，不证明ANN端到端/生产收益。Ch45原聚类residual不是相同summary分支，现已在“Exact Main与Approximate Residual”后实际补入正feature summary、减除已读贡献、联合归一化及selector/数值/摊销边界；6分深入后整合，不称无损压缩。

### [MegaTrain: Full Precision Training of 100B+ Parameter Large Language Models on a Single GPU](https://arxiv.org/html/2604.05091v1)

Exact-v1 §§3.1–3.4与4：CPU master store拥有参数/gradient/Adam状态，GPU只绑定当前layer；模板没有persistent weight pointers。H2D/compute/D2H stream以Weights-Ready、Backward-Done、Buffer-Free事件协调，不能在gradient未排空时重用buffer。参数传输须被计算隐藏，否则pipeline退化为串行；pin全部host model也不可行，采用有界staging slabs。

H200单卡/141GB HBM、1.5TB host、PCIe Gen4，与GH200单GPU/480GB host/NVLink-C2C是不同合同。作者吞吐、容量及长序列不外推convergence、recovery或生产SLO。Ch39已有CPU权威stream，现已在原layer-stream图后实际补无持久指针模板、三事件及有界host staging生命周期，保持PCIe/C2C与恢复边界；6分深入后整合。

### [Edit, But Verify: An Empirical Audit of Instructed Code-Editing Benchmarks](https://arxiv.org/html/2604.05100v1)

Exact-v1 §§2–6审计CanItEdit105与EDIT-Bench108，test counts覆盖全部213；EDIT-Bench的statement coverage仅91个可执行恢复解，不能混为108。低statement coverage可因AST/outcome/mocks而合理，但仍未证明改动外保持；未解15中11被归为artifact问题，不直接解释模型能力。两套benchmark语言/任务分布也不代表全部IDE流量。

Ch66原有“reference先重放”“零通过不等于难题”和Compound Artifact的保持区域合同，不应误称从无到有；但代码oracle中diff/AST只能定位改动、statement coverage不能证明未要求行为保持的具体有效性边界仍缺。root已在原preservation论证后窄幅细化change/preserve双面合同，5分按已确认知识缺口深入例外，不抬分；写后非作者核查另行完成。局部59%不作一般故障率，恢复解来自passing模型、人工label与外部流量估计的限制均保留。

### [Not All Turns Are Equally Hard: Adaptive Thinking Budgets For Efficient Multi-Turn Reasoning](https://arxiv.org/html/2604.05164v1)

Exact-v1 §3：allocator以conversation history与当前subquestion选择solver budget，最终accuracy减global超预算hinge penalty；实际训练按used tokens而非仅allotted tokens记账。同一trajectory advantage给各turn，不证明已解决局部credit。All-SubQ假设未来subquestions预先可得，不可用于未知在线任务。

数学推理benchmark仅支持其所测accuracy-token trade-off，未测完整service成本、并发或hard-budget安全。Ch79“belief + remaining cost/time/call budget”、hard cap与verification reserve已明确跨步机会成本；这里GRPO训练只是受限实现，5分标准已有覆盖。

### [Nidus: Externalized Reasoning for AI-Assisted Engineering](https://arxiv.org/html/2604.05080v1)

Exact-v1 §§2–3与9把finite specification、proof obligations、mutations和persistence置于同一daemon验证路径；QF_LIA/有限artifact可判定不等于外部软件全正确。§9.1 lesion在sandbox49项移除中32项被挡、connector/PO缺口明确，self-hosting与三次自约束操作不是对开放攻击的完备证明。

Ch84“Protocol-driven state transition/test obligation/release rule”已让platform拥有协议与receipt、Agent只提议mutation，亦保留不完备规格；5分标准已有覆盖。单部署/M4与declared238 POs时延不外推多tenant规模，不能用形式术语掩盖缺规格和旁路。

### [SkillAttack: Automated Red Teaming of Agent Skills through Attack Path Refinement](https://arxiv.org/html/2604.04989v1)

Exact-v1 §§3–4与6在skill保持不变的威胁模型里，先列可控input/敏感operation/触发条件，再构造路径、执行并基于path deviation回馈最多5轮。OpenClaw/Skill-Inject sandbox、10模型、71对抗skill与ClawHub100热门skill须分账；judge按trace/artifact/final response判断，不作全部人类确证或全生态攻击率。

它收窄静态skill审计的适用性而非提出静态审计无用；Ch72“Skill Poisoning的真值是Side Effect”已明确隐藏路径可由特定环境触发，adaptive honey world生成触发任务，matched no-skill形成反事实；真实effect trace及未触发不能证明安全也已承载。5分安全override深入后判已有覆盖，不因更高ASR强行新增正文；SkillAttack固定skill/改输入与另一分支改skill digest的威胁模型分别保留，不合并攻击率。

### [Can You Trust the Vectors in Your Vector Database? Black-Hole Attack from Embedding Space Defects](https://arxiv.org/html/2604.05480v1)

Exact-v1 §§3–7：攻击者可写任意vector、观察stored vectors，但无需控制query或encoder；global/cluster-centroid附近点利用centrality/hubness抢Top-K。有限anisotropic Gaussian条件下的分析不能作任意embedding几何定理。3类encoder×NQ/HotpotQA/MSMARCO各100k向量，malicious occupancy、retrieval overlap和最终RAG效果是不同measurement。

Detector需要额外kNN探测，自然hub会误判，z-score等geometry变换也可能损失retrieval quality。Ch76已在hubness诊断后实际补入任意vector写入的信任边界，并将source/content digest/encoder revision绑定标明为工程推断。作者防御Recall只测clean top-k overlap，不是答案truth；6分安全override深入后整合，不称几何异常即恶意文本。

### [Faster Superword Tokenization](https://arxiv.org/html/2604.05192v1)

Exact-v1 §§2–5把eligible pretoken连续run按频次聚合，regular BPE先训练完整merge顺序，再让supermerge与replay的regular计数竞争；ties必须regular优先。无需保全部document，但候选type-token ratio较高，聚合收益不如普通BPE。BoundlessBPE与匹配SuperBPE词表/merge相同不保证整数ID相同，故不能热换已有embedding artifact。

MiniPile、131,072词表、三次CPU时间测量支持作者实现；末两个原实现点是估计值，Python/Rust速度不可外推其他语料或端到端LLM。Ch11现已在BPE固定merge/id论证之后实际加入跨pretoken两阶段统计/replay及tie优先规则，并要求核完整token→ID映射与checkpoint兼容；6分深入后整合，不称任何superword tokenizer普遍优于BPE。

### [Spike Hijacking in Late-Interaction Retrieval](https://arxiv.org/html/2604.05253v1)

Exact-v1 §§2–4：hard MaxSim让每个query token只选一个patch，InfoNCE训练梯度集中；固定synthetic样本/encoder/负例而换pooling可隔离此压力，softmax最平滑却在该合成设定检索最差。ColQwen2.5/ViDoRe的160query只在推理时换pooling，未各自重训；hard-negative注入与Gaussian控制不同，Top-k也会被spike占满，不能称增加k就安全。

它给出selectivity与长度/语义spike鲁棒性取舍，不证明现实攻击频率、所有late-interaction失效或smoother必胜。Ch76已在late-interaction index budget之后实际补入MaxSim梯度路由→长文/定向spike→pooling选择性与鲁棒性取舍，明确160-query只推理替换而非重训；6分深入后整合。

### [A Theoretical Framework for Statistical Evaluability of Generative Models](https://arxiv.org/pdf/2604.05324v1)

Exact-v1 PDF §§2–5、Theorem4.2/Corollary4.3的对象是从ground-truth有限iid样本对候选分布作统一ranking保证。极小质量的rare event可使KL/Rényi大变而test sample看不到；bounded test class、有限VC/fat-shattering与额外条件改变可评价性。不能把此uniform负面定理写成固定model的test PPL无法计算，也不能否定假设受限的统计估计。

纯理论不适用GPU/精度/并发，样本分布、候选读取权限和metric class才是合同；经验benchmark不能作为定理的替代证据。Ch66已在有限评估样本的假设之后实际补入固定metric可算与uniform ranking有保证的区分、rare-event反例及有界函数/复杂度恢复条件；7分深入后整合。

### [Graph of Skills: Dependency-Aware Structural Retrieval for Massive Agent Skills](https://arxiv.org/pdf/2604.05333v1)

官方PDFv1与abs/v1相符，HTML/v1摘要却出现后版数值，本轮采用PDF §§3–5而不合并版本。offline把I/O兼容关系连typed graph，hybrid seed后reverse PPR与budget hydration取bundle；图扩张不是精确求解budget目标，也不证明依赖完整。两benchmark、三API模型、两次均值和200–2000库规模仅为受限证据，环境重试排除规则会影响分母；GPT配置部分agent-only runtime更慢。

Ch84“skill不能只靠平面tag”已有关系proposal→dependency/version lock→permission/joint-evaluation→resolved graph，及预算加载与不完备证据。该研究支持这一分支而不改变owner判断；5分标准已有覆盖，不将token减少等同latency减少。

### [ALTO: Adaptive LoRA Tuning and Orchestration for Heterogeneous LoRA Training Workloads](https://arxiv.org/pdf/2604.05426v1)

Exact-v1 §§5–8将cuBLAS base与grouped LoRA forward/backward分离；拼batch不改变每adapter统计batch，rank持有互不复制的adapter参数/optimizer/loss，base仍FSDP all-gather，不能写零通信。loss early-exit释放slot、backfill与duration profiling组成不同控制环；早期rank相关不保证其他域不会误杀late bloomer。

1/2/4 H100SXM80GB/NVLink、7–70B、60/64配置、rank16–128、batch1–8、1024/2048序列与3epoch构成作者评价合同，8bit AdamW不称所有状态full precision。最大speedup基线口径在figure/metrics有不同描述，不采用通用13.8×。Ch30已在MuxTune共享backbone分支后实际加入base大GEMM与grouped adapter执行解耦、rank-local状态/all-gather仍在和early-exit误杀边界；6分深入后整合。

### [Attention Editing: A Versatile Framework for Cross-Architecture Attention Conversion](https://arxiv.org/html/2604.05688v1)

Exact-v1 §§4–6在随机新attention时，先钳住teacher层输入、以post-o_proj normalized MSE独立训练edited block，再全student路径做token KL并可加低权feature loss；局部对齐不能单独证明student的自由生成轨迹等价。继承o_proj须shape兼容；不是任意checkpoint零训练转换。

Qwen3-8B/30B-A3B、MLA/GateSWA、Ascend910B和两阶段不同预训练格式语料支持作者案例。KV公式忽略bounded SWA cache，不能冒充全部HBM实测；teacher与student语料分布也不同。Ch14已在替代算子与部署编译之间实际加入checkpoint转换分支：teacher输入逐层对齐→student全网络蒸馏，保留shape兼容、转换成本及自由生成回归；6分深入后整合。

### [DualDiffusion: A Speculative Decoding Strategy for Masked Diffusion Models](https://arxiv.org/html/2604.05250v1)

Exact-v1 §§3–4：approximate drafter走K5步，再full-bidirectional verifier做KL/confidence remask；这个修正策略没有AR accept/reject的exact distribution证明，文中“deterministic AR acceptance”等概括不采用。A40 batch1、LLaDA/FastDLLM、阈值0.3下MMLU近verifier而GSM8K显著变差，峰值显存双模型增加。precision、并发与生产SLO未披露，少forward不自动端到端有益。

Ch24已有mutable target、provisional修正与exact/近似分账，并保留验证失败回退；5分标准已有覆盖。反证限制“维持高准确率”宣传，不把受限两任务质量推广为mask diffusion普遍加速。

### [Uncovering Linguistic Fragility in Vision-Language-Action Models via Diversity-Aware Red Teaming](https://arxiv.org/html/2604.05595v1)

Exact-v1 §§4–5将uniform-successor隐式Q与语义相似0.6、50词和结构有效性gate共同用于多样攻击；有效rewrite仍由语义proxy判定，不证明真实等价。no-action诊断显示π0.5视觉主导，因此不拿它评价语言脆弱性；π0/OpenVLA、Qwen3-VL4B、LIBERO训练及CALVIN/SimplerEnv迁移只有模拟行为证据。

Ch66模态/输入必要性与有效扰动、Ch26物理反馈及sim-to-real安全已承担这一合同。5分标准已有覆盖；失败比例、语言多样性与真实危害分别记账，不能将多样性分数外推风险coverage保证。

### [SnapFlow: One-Step Action Generation for Flow-Matching VLAs via Progressive Self-Distillation](https://arxiv.org/html/2604.05656v1)

Exact-v1 §3.3的consistency全导数平方对conditional velocity产生额外Jacobian-covariance项，这不同于单点FM中条件目标无偏。§3.4用同model marginal velocity的两步Euler shortcut及FM混合维持velocity，再学习端点；不是exact flow map，也不证明条件FM普遍有错。

单A80080GB、冻结VLM仅action expert/target-time模块训练30kstep；π0.5 LIBERO400episode承认LeRobot同task初态重复问题，SmolVLA主要offline质量。naive1step也有较高平均成功，不能把差异全归理论机制或外推真机安全。Ch24已在少步组合一致性主线实际补入单点FM条件目标无偏性不能迁到全导数平方、Jacobian–covariance项及自产生marginal shortcut的条件分支；6分深入后整合。

### [Generative Retrieval Overcomes Limitations of Dense Retrieval but Struggles with Identifier Ambiguity](https://arxiv.org/html/2604.05764v1)

Exact-v1 §§3–8以LIMIT及增加hard negatives的LIMIT-H/HS区分两种瓶颈：dense向量难区分候选；SEAL/MINDER生成共享ngram标识时可能没有relevant-only identifier。部分Recall仍非零，不能概括成生成检索必然完全失败。Beam宽度、partial scoring与共享ID改变检索结果；oracle pseudo-query需要知道可区分答案，不是部署方案。

这是替代检索表示的独立适用边界，不是仅增加benchmark。Ch76已在lexical/dense比较后实际加入生成document-ID的歧义、共享ngram/beam、ID维护成本及lexical fallback，保留非零Recall与oracle不可部署；6分深入后整合。Work in Progress及受控合成任务不证明所有真实corpus或生成检索模型有同一上限。

### [Broken by Default: A Formal Verification Study of Security Vulnerabilities in AI-Generated Code](https://arxiv.org/html/2604.05292v1)

Exact-v1 §§3–5把AST/regex pattern送到SMT constraint，再以SAT见证和少量runtime验证收窄结果。3,500 outputs来自500 prompts/7 models；55.8%含pattern-only，1,055 SAT不等于全部可达程序漏洞。另50 prompts/5 models的secure-prompt/self-review试验不能混用主分母；7个PoC与ASan、SQL等不同验证也不并为统一ground truth。

已深入核安全主张及关键反证。Ch66证据权限、形式规则scope和可执行artifact，Ch72漏洞proposal→重现→triage已有完整路径；本项没有证明普遍漏洞率或所有pattern因果可利用。判已有覆盖，保留检测局限，不把“SMT唯一ground truth”的宣传沉淀进Books。

### [Your LLM Agent Can Leak Your Data: Data Exfiltration via Backdoored Tool Use](https://arxiv.org/html/2604.05432v1)

Exact-v1 §§3–4及限制：fine-tuned模型以用户属性的语义合取触发memory读取，再用retrieval调用外发；返回chunk还能在后续turn再触发。3领域、Qwen2.5-7B/Mistral-Nemo12B/gpt-oss20B与7 rerankers是作者sandbox合同，不证明生产中已有攻击。多turn累计估计还依赖single-turn成功、递送与模拟用户配合，不能当真实独立累计概率。

Setup和Limitations的guardrail版本不一致，故不引用统一防御失败率。已深入核新的触发路径；Ch72的weight backdoor、private-context到检索egress以及自主跨回合再触发已承载同一防护边界。判已有覆盖；工具调用表面正常不授权私密信息离开当前purpose/principal。

### [Confidence Should Be Calibrated More Than One Turn Deep](https://arxiv.org/html/2604.05397v1)

Exact-v1 §§3–7、AppendixC区分fixed-turn ECE@T与pooled ECE@D；不同turn的过/欠置信可相互抵消。冻结LM、以平均hidden state训练两层MLP对齐turn-wise bin accuracy；ConfChat融合首turn和当前turn候选分数，不保证事实真值。

Llama3.1-8B/Qwen2.5-7B/Gemma2-9B、TriviaQA/SciQ/NQ；2,000 queries分800/200/1,000，A10080GB，最多5turn。随机persuasion和直到改信念的分析会引入选择/删失，5seed选best的报告也不能当普遍风险界。实际对读Ch66“Calibration必须寻找隐藏Regime”已有全局ECE掩盖过/欠置信抵消、随输入属性寻找符号反转及失败regime；“Calibration Slice”要求部署切片和足够样本，belief/action/outcome也分账。turn/history是这一合同的具体条件，MLP/ConfChat提供受限实现而非新的通用保证；5分标准已有覆盖，保留该反证，不为每个slice名称重复正文。

### [Multi-Drafter Speculative Decoding with Alignment Feedback](https://arxiv.org/html/2604.05417v1)

Exact-v1 §§2.3、3–4及H.1–H.2：每round选择一个drafter，用block divergence反馈UCB并平衡探索；query重置应对跨query变化，query内漂移另需discount/window机制。Stationary/iid alignment前提的stopping-time regret不等于wall-clock保证；缺失KV补齐、切换与resident pool都有成本。

A6000/A100/A5000、指定drafter/target、greedy及有限temperature/small-batch评价支持作者原型。I.3的无额外服务复杂度/通信概括不采用。Ch48已在共享speculation tree之后实际补round级单drafter alignment选择、query reset/query内漂移、missing-KV/探索切换成本，区别同时合树；6分深入后整合；分布稳定、池不常驻或输出短时单drafter仍合理。

### [ClawsBench: Evaluating Capability and Safety of LLM Productivity Agents in Simulated Workspaces](https://arxiv.org/html/2604.05172v1)

Exact-v1 §§3–5用五类REST mock的golden fixtures核schema/side effect，以SQLite snapshot比较post-state，44任务、6模型、4 harness、33条件。Skill/meta prompt仅部分组合有完整2×2 factorial；baseline缺tool信息不是能力零点，聚合skill收益不能推广所有harness。高task success和低unsafe action不是同一排序。

Ch66执行identity、mock保真/真实端点对照、安全切片与model×harness因素已承担这项反证。判5分标准已有覆盖。固定mock conformance不证明API全完备或生产权限一致；state-only结果也不能证明执行过程没有曾经造成后又抹掉的副作用。

### [Beyond Accuracy: Unveiling Inefficiency Patterns in Tool-Integrated Reasoning](https://arxiv.org/html/2604.05404v1)

Exact-v1 §§3–5与硬件敏感性附录把non-reusable KV的重复prefill、decode active length折成PTE；全KV失效是具体假设，不等于每次tool pause必然淘汰。FP16 KV、GQA/MLA布局和hardware operational intensity影响系数，固定model/hardware proxy不拥有latency或成本真值。

五个TIR benchmark的质量/代理work并测不证明更多tool导致错误。Ch70“Agent Trajectory的Token数必须折算为State-dependent Work”已明确相同公式、cache reuse、tool/network/idle与实测账本共存。5分标准已有覆盖，不再重复追加PTE段落。

### [Don't Act Blindly: Robust GUI Automation via Action-Effect Verification and Self-Correction](https://arxiv.org/html/2604.05477v1)

Exact-v1 §§3–5让上一步expected effect成为下一screen的verification假设，再选action与新effect；成功和“no change”合成轨迹SFT后以GRPO优化验证/动作。伪在线协议把错误视为screen unchanged，这不覆盖误点造成错误但可见转移、不可逆副作用或跨页面泄漏。

Qwen2.5-VL3B/7B、8×A100、AndroidControl等离线与MiniWoB++/AndroidWorld在线分别评价，不能合并成统一现实安全率。Ch80 execution evidence、verification-centric repair及误差后有界retry已覆盖这个控制判断；5分标准已有覆盖，训练受限实例不替代外部authorizer。

### [See the Forest for the Trees: Loosely Speculative Decoding via Visual-Semantic Guidance for Efficient Inference of Video LLMs](https://arxiv.org/html/2604.05650v1)

Exact-v1 §§2–4以target hidden与视觉hidden的Top-N cosine辨认相关token，对低相似部分放宽验证，PST还接受近span的移位匹配。视觉proxy和geometric acceptance假设不证明哪些token对事实/安全真正无关；放宽规则不保持target分布。

Qwen2.5-VL32B/LLaVA-OneVision72B、两H200、四任务、λ0.7/N10/max-generation512只是指定quality/latency取舍；未披露生产SLO不引用普适倍数。Ch48 matched-policy、近似verification独立质量合同与target exact路径共存已承载结论。5分标准已有覆盖，不把视频任务平均质量接近称为exact acceleration。

### [HybridKV: Hybrid KV Cache Compression for Efficient Multimodal Large Language Model Inference](https://arxiv.org/html/2604.05887v1)

Exact-v1 §§2–4以prefill text-centric sparsity动态分类head：static pruning优先text，dynamic KV offload到CPU后chunk retrieval；两级budget先分type再分head，padding满足CUDA布局。head角色会随任务变化，validation阈值不是固有语义真值，错误static判定可能不可逆删除。

Qwen2.5-VL3B/7B、LLaVA-OneVision7B、L40S、视频64frames以及图像/视频任务支持作者受限比较。Ch45 head-aware hot/cold、drift-triggered recall、transfer visibility和policy identity已承担这条机制。5分标准已有覆盖；10% nominal KV不等于全系统峰值HBM或并发吞吐。


### [The Illusion of Latent Generalization: Bi-directionality and the Reversal Curse](https://arxiv.org/html/2604.04943v1)

本轮实际读exact-v1 §§2–4与遮蔽/表示消融；官方abs/v1与HTML标题一致，Submitted=03-13T20:55:43Z不是首次公开，v1 Updated=04-08T00:00:14Z仅与ID/相邻批次/公告slot共同支持本窗范围。始终不预测来源实体时，Table1中该消融可定义的三组反向检索失败；不能将整体四种关系benchmark全部算作此消融。允许来源预测后改善，但MLM还有不同遮蔽条件；BERT-Large340M/Gemma3-4B及base/instruct未完全控制身份，不能声称任意语言知识的必要充分条件。距离/线性probe与分别索引相符，不排除非线性系统关系。

Ch28原NTP只说明局部条件分布及目标mask，未区分方向访问与统一概念；已在公式后实际加入“预测方向与知识可访问方向”分支及Ch29监督交接。2+2+2=6，因修正泛化推断与明确长期缺口深入；不为旧主题标签关闭。

### [Memory Dial: A Training Framework for Controllable Memorization in Language Models](https://arxiv.org/html/2604.05074v1)

已读exact-v1 HTML §§3–6、A.3–A.6及PDF首页/公式身份。v1 Updated=04-08T00:03:17Z只作组合日期上界线索，Submitted=04-06T18:19:58Z不代公告。普通CE与低温CE凸组合的gradient通常不等单有效温度；同架构、数据及步数内扫alpha，对注入seen、heldout、diversity与single-temperature baseline分别测。实验限449步、三seed、英语主要多选任务、至多两H100；额外自然/多语言对照不构成真实大预训练保证，alpha不控制从零到完整记忆。小tau下correct大margin梯度可衰减，故不沿用作者“所有高置信预测都强化”的泛化解释。

Ch28现已在方向访问段之后实际加入双objective—记忆/泛化匹配实验分支及privacy/diversity成本；Ch5仍拥有记忆与泛化的总认知，不重复其整段推导。2+2+2=6，知识缺口深入后整合，不把无新架构视作无贡献。

### [Scaling DPPs for RAG: Density Meets Diversity](https://arxiv.org/html/2604.03240v1)

固定初检→子集专用Gram adapter/set margin→集合packing选择；评分2+1+2=5，审阅深入完成。精确v1身份和公开日由本家族AB/DOI、官方first-announcement赋号规则、相邻批次/OAI及月列表组合支持Apr07自然日；单Submitted/Updated/created不定义首发。[本日必要Source与逐批独核](../_sources/daily-20260408/SUP_REVIEW_20261014.md)保留必要位置、评价合同与未证明范围。

精确v1 §2.1–2.3/Eq1–15、§3完整T1–3/配置与效率、AppendixD/T4实际读。冻结原encoder，初检仍原embedding/pointwise，P-adapter只在候选集合构建DPP kernel时开启；normalized Gram经positive reranker score对角Q加权。DML让ground-truth互补集det超过同size negative子集，LogSumExp/softplus实现smooth loss；负集过大仍要sampling。exactMAP NP-hard，用既有greedy近似，不是保证完整证据覆盖。det-space凸性不推出非线性adapter参数全域凸/无saddle；作者§3near-convex宣传不采用，无需遍历未采用proof。MultiHopRAG2255/2556（去301null），5:1:4 stratified；N20/k4或10，4encoder/BAAI reranker，RTX5090/20epoch/lr1e-4/b8或4，.3/1.5h。T1部分reranked Recall@10反退，T2两hop不普胜；DPP无adapter更差，D表QA某些2/4hop及base-DPP>adapter也保留。DeepSeekV3.2 thinking output4096，precision/seeds/concurrency/SLO/全index及generation预算Not Disclosed。表示独立不等语义独立、candidatepool缺证据不能被subset算法恢复。

本日整合：AGENT-RAG [Ch76](../../../../books/part-07-agent/76-rag.md)。当前owner/完整邻接逐字PRE后，已在原论证内实际写入受限差额，非作者实际正文、完整旧邻接与来源注POST通过；原分支与失配回退保留，不授实现/复现或生产保证。

若目标是让固定预算里的证据互补，逐文档相关性与最后的集合选择可以消费不同表示。一条[受限集合分支](https://arxiv.org/html/2604.03240v1#S2)保留原 encoder 的初检次序，只在候选子集阶段启用小 adapter，以归一化向量的 Gram determinant 衡量集合张成的体积，再乘正的 relevance 权重；训练则让标注互补集的 determinant 超过同大小的负集，而非只提高各篇独立分数。这不是语义独立或证据完备的证明，greedy MAP 也不是全局最优，初候选缺失的桥梁不能靠重排恢复。Adapter、负集构造、kernel/选择和下游生成都计费；有限多跳对照有逐 hop 和答案指标反退，determinant-space 的凸性更不认证 adapter 参数全域凸。候选、表示或质量失配时，保留普通 relevance/reranker、已验 MMR 与直接补证，独立核答案支持，不由更大几何体积批准事实。<!-- source-family:SF-2026-ARXIV-2604-03240 -->

### [Rewriting TTS Inference Economics: Lightning V2 on Tenstorrent Achieves 4x Lower Cost Than NVIDIA L40S](https://arxiv.org/html/2604.03279v1)

局部PCC近1仍音质下降→precision与outcome双面验收；评分1+2+2=5，审阅标准完成。精确v1身份和公开日由本家族AB/DOI、官方first-announcement赋号规则、相邻批次/OAI及月列表组合支持Apr07自然日；单Submitted/Updated/created不定义首发。[本日必要Source与逐批独核](../_sources/daily-20260408/SUP_REVIEW_20261014.md)保留必要位置、评价合同与未证明范围。

实际v1 §3.1–3.8、§4.1–4.6/T2–3、§5.1–5.4。连续diffusion声学latent在多step积累误差、PCC near1局部不证明输出感知质量；选敏感层保精度，余层LoFi/BFP8，weights multicast/UB tile/activationonchip。该判断是实际precision/评价边界，不采用“TTS普遍比LLM更fragile”或AR每token归一消误差等未证概括。P150实测，P100250ms是由single-chip不启用QSFP推同latency，不是第二台实测；L40S并发3/300ms对P150并发1/250ms，fixed约5s音频/满utilization fleet估算，不授实时queue/tailSLO/TCO。DNSMOS3.872→3.801确有.071退步，WER.009是跨两输出normalized，sample数、数据、subjective盲听/重复/误差范围未披露，不能称无感知质量损失。模型架构细节/层精度列表、输入文字/输出长完整配置、power/host/software费用未披露；8–12×是projection不是实测。

已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。Ch66“数值mismatch的判定必须连接baseline、机制与结果owner”以reference/tolerance/operator/shape/precision/downstream outcome双面验收；不把PCC近1当感知质量。 非作者已实际读当前承载正文/完整相关局部，此决定不是主题相似或仅Review note匹配，不新增同义书稿。

### [ENEC: A Lossless AI Model Compression Method Enabling Fast Inference on Ascend NPUs](https://arxiv.org/html/2604.03298v1)

受限NPU block可逆exponent表示与依赖解耦→resident/解码取舍；评分2+2+2=6，审阅深入完成。精确v1身份和公开日由本家族AB/DOI、官方first-announcement赋号规则、相邻批次/OAI及月列表组合支持Apr07自然日；单Submitted/Updated/created不定义首发。[本日必要Source与逐批独核](../_sources/daily-20260408/SUP_REVIEW_20261014.md)保留必要位置、评价合同与未证明范围。

实际v1 IV-A/B/Alg1、V-A–E/Alg2与Eq1–4、VI配置/A–F/T2–6、VII-A/B。符号/尾数原样存，只对exponent可逆integertransform/packing；所谓bit-width quantization是无损表示位宽选择，不是数值量化。group统一lowm/highn+mask、halving/bytealignment替乘除、branchfreeb−x替lookup、transpose把32B内scan转跨row再加exclusiveoffset；encoder/decoder与b,n,m,L必须绑定。group概率p(m)^L参数cost是统计模型，不授任意correlation最优。作者10modelbit-identical重构核验可支持作者实验，不称本人运行/复现。910B2/AscendC8.2RC/driver25RC，CPUKunpeng920；A800/8358P/CUDA12.6是另一平台，peakTFLOPS相近不等所有kernel公平硬件。devicekernelthroughput不含PCIe，BF16decode比DietFloat退6%，T2 BF16 CR1.34–1.37弱于ZipNN/DietFloat1.5左右，保CR/吞吐取舍。Qwen332B/Falcon40B单NPU原baseline部分CPUoffload，压缩后逐layer解码与下一层重叠；10warm/50tests均值，T1TTFT/TPOT最高6.3×仅该offloadbaseline与batch，输入输出虽称fixed但正文数值、完整SLO/并发、checksum替代时序接口Not Disclosed。UB192KB限制使block16384优于32768，布局/解码工作集计费；非offload/小模型不保证收益。

本日整合：INFER-GPU-MEMORY [Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md)。当前owner/完整邻接逐字PRE后，已在原论证内实际写入受限差额，非作者实际正文、完整旧邻接与来源注POST通过；原分支与失配回退保留，不授实现/复现或生产保证。

硬件缺少便宜的分支、变长 scatter 或段内 scan 时，无损编码还可以用规则的 block 工作换取解码可执行性。一条[受限 NPU 路径](https://arxiv.org/html/2604.03298v1#S5)原样保存 sign/mantissa，只对 exponent 做可逆整数映射；组内统一选低/高位宽并带 mask，按层次 folding 对齐字节，再通过 transpose 把段内 prefix-sum 依赖转成跨行计算与 exclusive offset。这里的“位宽选择”不改变浮点数值，codec 的映射、组长、布局与 decoder 仍必须共同绑定。规则化会放弃部分压缩率，也支付临时 buffer、参数统计与解码带宽；作者 bit-identical 核验不替我们验证实现。Device-kernel 吞吐不包含 PCIe，所测端到端收益主要对单 NPU 放不下权重的 CPU-offload baseline，不能外推所有 resident 模型。熵、工作集、硬件指令或总延迟不合算时，保留原 tensor、成熟 lossless codec 或经质量验收的数值量化，不能把可逆重构叫免费传输。<!-- source-family:SF-2026-ARXIV-2604-03298 -->

### [V-Reflection: Transforming MLLMs from Passive Observers to Active Interrogators](https://arxiv.org/html/2604.03307v1)

训练grounding蒸馏与推理slot producer存在中心冲突→不授serving接口；评分2+1+2=5，审阅争议。精确v1身份和公开日由本家族AB/DOI、官方first-announcement赋号规则、相邻批次/OAI及月列表组合支持Apr07自然日；单Submitted/Updated/created不定义首发。[本日必要Source与逐批独核](../_sources/daily-20260408/SUP_REVIEW_20261014.md)保留必要位置、评价合同与未证明范围。

实际v1§3.1–3.4/Eq1–5、§4.1–4.5/T1–3、A.1–3/Alg1、B/T4。box局部teacher压缩、Bernoulli.5 stopgradient交替方向，再hidden-query globalstudent的featureL1/attentionKL两目标；stopgradient消融仅局部支持，不授防collapse普遍证明。中心serving接口冲突：main§3.4/4.4/T3e称两moduleinferenceinactive/pureCoconutS latentKV decode；A.2却明确“in Stage2 and inference, the DAC populates these slots dynamically”，Alg1Stage2CE直接LLM(Z_S)也不能单独解释转purehiddenautoregression。A.3MSE与mainL1另冲突。此争议不据作者success/attention图消除，也不默认完整源码重建；需作者明确inference slotproducer、globalfeature消费图和真实成本后只重开此命题。Qwen2.5VL7B、frozenvision/projector、LLM fullFT、VisualCoT、BF16/8A800/ZeRO3/batch4/packing16384、2500/1250step24/12h/S8；S16反退、BLINKjigsaw49.6<52.7、HR8KFSP73.5<73.8，正文“+7.0”也不合72.3−66.7。模块inactive不等无驻留/无S步，作者25–80%latencyincrease；未核实现或复现。中心不支持Books正面生成接口。

争议/暂缓：MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)。中心矛盾双方均保留，不作正面Evidence或Books，具体缺少的原始澄清及定点重开见§5；不是普通未读，也不以降分或删反侧关闭。

### [CoLA: Cross-Modal Low-rank Adaptation for Multimodal Downstream Tasks](https://arxiv.org/html/2604.03314v1)

paired modality生成低秩middle map→静态与动态adapter分账；评分2+1+2=5，审阅深入完成。精确v1身份和公开日由本家族AB/DOI、官方first-announcement赋号规则、相邻批次/OAI及月列表组合支持Apr07自然日；单Submitted/Updated/created不定义首发。[本日必要Source与逐批独核](../_sources/daily-20260408/SUP_REVIEW_20261014.md)保留必要位置、评价合同与未证明范围。

实际v1§3.2/Eq4–6/完整Alg1、§4.1–4.3/T1–4、§5.1–5.3/T5–6、A1–2/T7–9、Dlimitations。intraLoRA固定B_LA_L，interB_C Phi(x_c) A_C；另一modalitypool/CLStoken经hypernetwork生成r×rPhi，pairedstage逐步传播另一流当前SA/output/FFNfeatures；不是仅把x_c直接concat。训练时basefrozen但head/adapter/hypernet均可训，inter是input-dependent不能staticmerge，参数/latency/memory均增加。same-rank与same-paramLoRA对照支持分支，未同时消除每个path参数budget混杂；fullyseparate比shared提高且参数不同，不能称免干扰保证。ViTB/BERT或DINO/SSLAM/SwinL4有限任务、r16、train150/50/15epoch与b80/2/8；GPU/precision/seeds/timing具体值/SLO必要fields未披露。STGCMA大模型AVE83.3>81.1/AVS81.8>80.9保反侧；modalitynorm、层数配对/unevenlayout是接口条件。

本日整合：TRAIN-LORA [Ch30](../../../../books/part-04-training-system/30-lora.md)。当前owner/完整邻接逐字PRE后，已在原论证内实际写入受限差额，非作者实际正文、完整旧邻接与来源注POST通过；原分支与失配回退保留，不授实现/复现或生产保证。

条件增量也可以只生成低秩空间里的中间映射，而不重建全部 adapter 因子。一条[受限双 encoder 分支](https://arxiv.org/html/2604.03314v1#S3.SS2)保留本模态的静态 LoRA，另让配对模态的 pooled/CLS features 经 hypernetwork 生成 r×r 矩阵 Φ，形成独立的 BΦA 增量；两流在 attention、output 与 FFN 的对应 stage 更新并交换当前特征。这样分别约束本模态适配和跨模态消费，但 pooled cue、层数配对与 feature revision 成为新接口，不保证两条路径免干扰。静态增量仍可 merge，依赖另一输入的 Φ 则须运行时计算，不能因低秩而热合入固定基座。有限 rank/参数匹配对照支持此分支，未证明所有模态、层或任务更好；hypernetwork、双流激活和同步增加内存、训练与推理费用。另一模态缺失、配对或质量失配时，保留独立 LoRA、固定融合与完整回归，不由少 trainable parameters 批准低延迟。<!-- source-family:SF-2026-ARXIV-2604-03314 -->

### [MetaSAEs: Joint Training with a Decomposability Penalty Produces More Atomic Sparse Autoencoder Latents](https://arxiv.org/html/2604.03436v1)

decoder可分解性critic正则→geometry proxy与真概念分账；评分2+1+2=5，审阅深入完成。精确v1身份和公开日由本家族AB/DOI、官方first-announcement赋号规则、相邻批次/OAI及月列表组合支持Apr07自然日；单Submitted/Updated/created不定义首发。[本日必要Source与逐批独核](../_sources/daily-20260408/SUP_REVIEW_20261014.md)保留必要位置、评价合同与未证明范围。

实际v1§3.1–3.3/Eq2–3、§4、§5.1–5.3/T1、§6/7.1–7.2和F。primarydecodercolumn由小metaSAE重构，exp(−error²/sigma²)高值受罚；frozencritic/no_grad重构使gradient只推primarycolumn远离现meta方向，再meta10/5交替适配。低correlation/可重构性proxy不等真实概念独立/causal/safecontrol，也不保证非线性cue没丢。GPT2large layer20/FineWeb100M、n20480/k64、meta1800/k8、9grid Adam3e-4、fresh35M＋EER5M；judgeQwen2.5-72B-AWQ/Hungarianmatch20456/20480。bestcooccurrence选后fuzz+7.6%、L2+9.3%、CE多.6pp，4soloruns基线；209Mpair共享feature不自动209M独立训练重复，作者Welcht-testp不作为普遍显著/因果保证。lambda1反而cooccurrence变坏，§7monotonic文字不采用；Gemma9B75M未收敛/5Munderpowered混合结果，之后300M非同预算smallscale简单外推。meta比例没消融；hardware/precision/fullcost/seeds必要字段未披露。

本日整合：WORLDVIEW-REPRESENTATION [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)。当前owner/完整邻接逐字PRE后，已在原论证内实际写入受限差额，非作者实际正文、完整旧邻接与来源注POST通过；原分支与失配回退保留，不授实现/复现或生产保证。

辅助目标也可以来自 dictionary 自身的可分解性，而非外部语义 encoder。一条[受限 decoder 几何分支](https://arxiv.org/html/2604.03436v1#S3)让小 meta-SAE 稀疏重构 primary decoder 的方向，对重构误差很小的方向加更大 penalty；更新 primary 时将当前重构作为冻结 critic，再更新 meta，使两者轮流适配。它鼓励方向不易由现 meta-dictionary 表达，不等于发现了互相独立的真实概念，非线性 cue 和合理共享结构仍可能受损。所测 co-occurrence 与自动解释代理的改善伴随重构/CE 增加，更强 penalty 还会反退；共享 feature 的大量 pair 不能当独立训练重复，单层与未收敛大模型切片不签泛化保证。Meta 训练、超参 sweep、匹配与独立解释/干预都计费；表示覆盖或原模型行为失配时，保留普通 SAE、external-consistency 分支和合适 null baseline，不由低相关自行授 atomicity 或安全控制。<!-- source-family:SF-2026-ARXIV-2604-03436 -->

### [Scalable Variational Bayesian Fine-Tuning of LLMs via Orthogonalized Low-Rank Adapters](https://arxiv.org/html/2604.03388v1)

一次backbone＋Bayesian last-head MC→posterior scope/成本取舍；评分2+2+2=6，审阅深入完成。精确v1身份和公开日由本家族AB/DOI、官方first-announcement赋号规则、相邻批次/OAI及月列表组合支持Apr07自然日；单Submitted/Updated/created不定义首发。[本日必要Source与逐批独核](../_sources/daily-20260408/SUP_REVIEW_20261014.md)保留必要位置、评价合同与未证明范围。

实际v1§3.1–3.3/Eq1–16、§4.1/4.3、T1关键ACC/ECE/NLL条件反侧，B1–2/C2/T3–5与C3/T6。确定featureextractor+perclassGaussian lasthead，Jensen下界ELBO更新posterior/PoLAR，U/V约束与Lambdafree；landingpenalty是infeasible/asymptotic，不授全程orthonormal或Lambda不rankcollapse。inferenceonebackbonepass然后K10headMC，posterior仅head不覆盖整网epistemic或semantictruth；可选LA是另cost，精确covariance/diagscope在main与B1描述不统一，不采用full-covarianceguarantee。Llama3.1-8B/2-7B多选分类非自由生成，r8/alpha16/q,v+output适配、BF16/5000step/b4/evalb8/len300；C2效率另inferenceb4，A6000Ada（作者原名）/Threadripper，表±未说明seedcount。12s对BLoB80–90s是ARC-E整test配置非perrequest/SLO，LoRAVBLL8s较更快。WG-SACC77.26<MLE77.92、BoolQ/ARC部分NLL也不普胜，ScaleBLunderfit移附表/PoLARTFB失败不能抹对照。orthogonalupdate不保证完整featuredistance，最窄成本边界在headposteriorgeometry与全backbone重采样tradeoff。

本日整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。当前owner/完整邻接逐字PRE后，已在原论证内实际写入受限差额，非作者实际正文、完整旧邻接与来源注POST通过；原分支与失配回退保留，不授实现/复现或生产保证。

若推理预算不允许多次完整模型采样，也可以把随机性限制在最后的分类 head，而不是把重复 dropout 的波动训练成诊断 proxy。一条[受限后验分支](https://arxiv.org/html/2604.03388v1#S3)用确定 feature extractor 产生一次表示，联合训练高斯 head posterior 与 adapter，再在同一表示上采样多个 head 的预测；Jensen 下界使分类训练可不逐步做全网 Monte Carlo。省下的是重复 backbone 前向，head 状态、训练、posterior 采样与可选 curvature 校准仍有成本。该后验只覆盖指定 head 和多选分类目标，不表达整网全部 epistemic uncertainty，更不拥有语义真值；正交 adapter 合法也不保证 feature distance 或分布外校准。原有限分类对照有准确率/校准反退，精确 covariance 与可选 LA 的 scope 尚未统一，不能据此签发 full-posterior 保证。后验假设、feature producer 或实际质量失配时，保留原点估计、直接重复采样与独立 held-out/outcome 校准，不从一次前向批准任意生成的低风险。<!-- source-family:SF-2026-ARXIV-2604-03388 -->

### [Drift-Based Policy Optimization: Native One-Step Policy Learning for Online Robot Control](https://arxiv.org/html/2604.03540v1)

单步动作generator＋stored latent conditional PPO→joint与执行prefix credit；评分2+2+2=6，审阅深入完成。精确v1身份和公开日由本家族AB/DOI、官方first-announcement赋号规则、相邻批次/OAI及月列表组合支持Apr07自然日；单Submitted/Updated/created不定义首发。[本日必要Source与逐批独核](../_sources/daily-20260408/SUP_REVIEW_20261014.md)保留必要位置、评价合同与未证明范围。

实际v1IV-A–C/Eq6–17、V-A–E/T1–3。actionchunk generator从Gaussianlatent单forward；训练G hypotheses/自样本负例+expert正anchors多尺度balance attract/repel，stopgradtarget固定点回归。forwardloss等driftnorm不说明stopgrad实际梯度就是该norm的总梯度，本文不采用zero-drift/全分布收敛宣传；引用supplement不是必须读未采用证明。Online附diagGaussianhead，rollout保存latentz与实际执行prefix，PPO同z新旧conditionalratio因fixedprior相消等jointratio，不是积分掉z的marginalactionlikelihood。未执行suffix不赋当前credit；frozenreference同z meananchor另加。部署去explorationnoise是不同operatingpoint，不保证训练/部署每项行为一致或physicalsafe。reproducedDP/onlinevs quotedOMP不同合同，3seed，last10/top5checkpoint是selection不同口径；8RTX3090/10demo、1000/3000epoch/FPS512/1024/84²。100→1NFE不是wallclock100×；PushTimage/Roboimage反退。UR5/RTX3090/三camera每task50demo/20trial，45/60，bimanual11/20、9.5ms作者average不授105Hz整control、安全或tailSLO。precision/fulltrain+environmentbudget未披露。

本日整合：MULTIMODAL-EMBODIED-VLA [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)。当前owner/完整邻接逐字PRE后，已在原论证内实际写入受限差额，非作者实际正文、完整旧邻接与来源注POST通过；原分支与失配回退保留，不授实现/复现或生产保证。

若连续 action generator 本身没有便宜的边际 likelihood，在线更新还可以显式保留它采样时的隐变量。一条[受限单步分支](https://arxiv.org/html/2604.03540v1)以 expert anchors 与自产 hypotheses 的 attract/repel 目标训练一次前向的 chunk generator，再给输出附条件 Gaussian head；rollout 同时保存固定先验抽出的 z 和实际执行的 action prefix。新旧策略在同一 z 上比较条件 density，固定 prior 在联合 ratio 中抵消，但这不是积分掉 z 后的边际 action density；未执行 suffix 不应获得当前环境反馈的 credit。Stop-gradient target 的数值等于 drift 范数，不证明实际训练梯度是其全导数或零 drift 必恢复真实分布；部署移除探索噪声也是另一个待验 operating point。少 NFE 不等同比例墙钟收益，有限图像任务有反退，真机 45/60 及双臂 55% 更不是安全保证。Expert 数据、多 hypothesis、Gaussian/PPO 更新、reference anchor 与真实交互都付费；条件接口、质量或闭环失配时，保留原多步 policy、直接 BC 与独立 controller/人工接管，不由可算 ratio 批准动作执行。<!-- source-family:SF-2026-ARXIV-2604-03540 -->

### [Compressible Softmax-Attended Language under Incompressible Attention](https://arxiv.org/html/2604.04384v1)

weight与输入logits谱不同→低effective rank不授压缩保证；评分2+1+2=5，审阅深入完成。精确v1身份和公开日由本家族AB/DOI、官方first-announcement赋号规则、相邻批次/OAI及月列表组合支持Apr07自然日；单Submitted/Updated/created不定义首发。[本日必要Source与逐批独核](../_sources/daily-20260408/SUP_REVIEW_20261014.md)保留必要位置、评价合同与未证明范围。

实际v1§2.1–2.2/§3/T1–2/§4.1–4.4/§5、A必要Lipschitz证明。rowcenterlogits等原softmax，但dataQK能量低effective-rank不等weightWQᵀWK低rank；实际rank≤dh+1是作者宽上界，不依它推出全部data定律。5model124M–7B、4architecture/GQA、5Gutenbergtext/len256、float64SVD，多head/textmedian非训练seed。2–11与38–75是90%variance指标，rank10meanattentionL1仍.31–.46/worst.90–1.31，未证明outputvalueweighted/跨layer/最后PPL保持。delocalization约束才有tail-sumL1bound，固定L/所读条件不授任意长context衰减；“weightcompression ruledout”只是谱容量观测，不能否定taskweighted/data-calibrated低rank。硬件/seeds/fullSVDcost/SLO未披露，纯diagnostic非servicebenchmark。

本日整合：MODEL-SELF-ATTENTION [Ch14](../../../../books/part-02-model/14-self-attention.md)。当前owner/完整邻接逐字PRE后，已在原论证内实际写入受限差额，非作者实际正文、完整旧邻接与来源注POST通过；原分支与失配回退保留，不授实现/复现或生产保证。

权重矩阵的谱也不能直接替某个输入上的匹配分数谱签字。忽略位置变换时，bilinear weight 是 W_QW_Kᵀ，而实际 logits 还消费 X；加入 RoPE 后，又要按真实 Q/K 对象诊断。一项[受限输入谱研究](https://arxiv.org/html/2604.04384v1#S3)比较 weight 与 row-centered logits 的能量分布，说明固定参数容量和当前数据上被使用的方向是两个对象；该比较并未控制所有位置变换差异，不能将全部低维性唯一归给 data manifold。较低 effective rank 不批准无损 attention 压缩：softmax 行误差的界另需左右 singular vectors 都不局部集中及 nuclear-tail 条件，正文只测右向量/variance 不能替代它们；rank截断的实际行L1误差、value加权输出、跨层与最终任务仍分别验收。谱分析/SVD与可能的压缩路径均有成本，条件或质量未闭时保留 dense 与已验稀疏/互补读取，不由低能量尾部批准生成正确。<!-- source-family:SF-2026-ARXIV-2604-04384 -->

### [Training Transformers in Cosine Coefficient Space](https://arxiv.org/html/2604.04440v1)

训练DCT坐标每forward重构dense→参数节省与物化费用分账；评分2+1+2=5，审阅深入完成。精确v1身份和公开日由本家族AB/DOI、官方first-announcement赋号规则、相邻批次/OAI及月列表组合支持Apr07自然日；单Submitted/Updated/created不定义首发。[本日必要Source与逐批独核](../_sources/daily-20260408/SUP_REVIEW_20261014.md)保留必要位置、评价合同与未证明范围。

实际v1§2.1–2.4/Eq1–3、§3.1–3.2/T1、§5。固定zigzaglowfrequency支持、只训练K系数，eachforwardIDCT恢复denseW，gradientDCT后只取同support；是spectralsubspace从零训练，不是pretrainedLoRA或bitexactcodec。dense临时W与DCT O(mnlogmn)仍付费。4layer128dim/4head/context128/tinyShakespeare1M/90-10split、30epoch/b32/AdamW/.01WD/clip1；DCTlr1e-3对dense/lowrank3e-4不完全isolatedparametrization。52%paramsamePPL6.1只局部metric相同，不能称函数无损；29%paramPPL6.9对lowrank21%PPL8.8非完全samebudget。作者每epoch20%更慢，fusedCUDA/Metal是假说非实现；GPU/precision/seeds/fullpeakmem/SLO未披露。最窄长期增量为训练坐标/物化计算与rank约束不同。

本日整合：TRAIN-PRETRAINING [Ch28](../../../../books/part-04-training-system/28-pretraining.md)。当前owner/完整邻接逐字PRE后，已在原论证内实际写入受限差额，非作者实际正文、完整旧邻接与来源注POST通过；原分支与失配回退保留，不授实现/复现或生产保证。

可训练变量也可以是固定变换基中的部分系数，而不是 generator 的 root parameters 或低秩因子。一条[受限频域训练分支](https://arxiv.org/html/2604.04440v1#S2)只更新二维 DCT 的固定 zigzag 低频支持，每次 forward 用 inverse DCT 物化 dense weight，backward 再把矩阵梯度投影回同一系数集。固定支持定义模型能沿哪些方向学习，不证明任意行列索引都有平滑语义，也不等于低 rank、数值无损或更小的执行矩阵。Tiny character-model 的局部 perplexity 接近，仅支持该质量切片；与低秩基线的系数比例和 learning rate 不同，不能据此授同预算优越。少 trainable state 仍支付 dense weight/activation、变换与优化费用，所测每 epoch 反而约慢20%。支持太窄、索引结构或质量/总成本失配时，保留显式 dense、较宽系数支持或已验低秩参数化，不用参数计数代替 held-out 能力与真实训练预算。<!-- source-family:SF-2026-ARXIV-2604-04440 -->


### [SLaB: Sparse-Lowrank-Binary Decomposition for Efficient Large Language Models](https://arxiv.org/html/2604.04493v1)

显式sign×rank-one magnitude＋稀疏残差→非低秩执行/metadata费用；评分2+1+2=5，审阅深入完成。精确v1身份和公开日由本家族AB/DOI、官方first-announcement赋号规则、相邻批次/OAI及月列表组合支持Apr07自然日；单Submitted/Updated/created不定义首发。[本日必要Source与逐批独核](../_sources/daily-20260408/SUP_REVIEW_20261014.md)保留必要位置、评价合同与未证明范围。

实际v1II-A/B完整算法（只采用机制、不採two-centerproof最优）、III-A–D/T1–3。真实表示是W_S+(UVᵀ)⊙W_B，binary逐element±1控制符号而rank1建magnitude；不是sparse+lowrank+binary三矩阵简单相加，Hadamard结果不保持rank1，也不直接用两次小GEMM获得samefunction。迭代先残差sign/absrank1SVD，再activationnorm重权剩余残差并选sparse，layer逐个更新校准。§II sign说明负数0与Alg±1不同，只采用明确±1表示，不授完整可复现kernel；CR只算nonzero数值、fullsignbits及U/V，漏sparseindexmetadata，不等allocatedartifacthalfbytes。Llama1/7/8B/C4同128×2048calibration/20iter/WikiText2+7LMharnesstasks；T1仍弱dense，T3fullcomp对标量binary少量增益且个task反退。hardware/precision实际运行/latency/seeds/完整kernelSLO未披露，不授runtime加速/无损。binary把低rankmagnitude与复杂sign分权是具体可核增量。

本日整合：INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)。当前owner/完整邻接逐字PRE后，已在原论证内实际写入受限差额，非作者实际正文、完整旧邻接与来源注POST通过；原分支与失配回退保留，不授实现/复现或生产保证。

已有权重若不能保固定 sign template，压缩还可以显式保存符号，并把难重构部分分到稀疏 residual。一条[受限校准分支](https://arxiv.org/html/2604.04493v1)写成 W_sparse+(uvᵀ)⊙W_binary：逐元素 sign 持有复杂符号结构，rank-one factors 只重构 magnitude；迭代估计符号/幅度后，再按 activation 加权的残差选 sparse entries。Hadamard 结果不保持 rank one，不能据 factor 小直接改成两次小 GEMM；sign 的0/±1文字口径也不补成完整 kernel recipe。压缩率若漏 sparse indices，不能当实际 resident bytes；有限 LM 对照仍弱于 dense，kernel、metadata、校准与物化费更不能由 nonzero 计数抹去。Sign/scale、稀疏布局与质量或净执行费用失配时，保留原矩阵、常规低位格式或前述受控 template 分支，不从三种表示相加批准无损与低延迟。<!-- source-family:SF-2026-ARXIV-2604-04493 -->

### [Isokinetic Flow Matching for Pathwise Straightening of Generative Flows](https://arxiv.org/html/2604.04491v1)

保FM＋self-lookahead velocity正则→非endpoint flowmap或一步保证；评分2+1+2=5，审阅深入完成。精确v1身份和公开日由本家族AB/DOI、官方first-announcement赋号规则、相邻批次/OAI及月列表组合支持Apr07自然日；单Submitted/Updated/created不定义首发。[本日必要Source与逐批独核](../_sources/daily-20260408/SUP_REVIEW_20261014.md)保留必要位置、评价合同与未证明范围。

实际v1§4.1–4.5/Eq12–21完整Alg1、§5.1–5.2/T1–2/§6.1与C1–6。model自身velocityEulerlookahead，再nextvelocitystopgrad作当前velocity一致性regularizer，同时原FM目标保留。Eq17L2与Alg1带time/1epsilon、speednorm的L1不同，不采用唯一可复现全recipe或softreg保证mode不丢；局部materialderivative不等explicitflowmap、一stependpoint或全局nonintersection。CIFAR10/DiTS2/32M/2500epoch/b256/AdamW5e-4/BF16/EMA.9999/λ4、every250epoch50k/FID1,2,4/多CFG，bestmetric对应不同epoch，FID比率非runtimegain。OT另Hungarianmatching成本和变化不归Iso，额外teacherforward/finite-difference代价保留。hardware/seeds/fulltime/SLO未披露。

本日整合：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)。当前owner/完整邻接逐字PRE后，已在原论证内实际写入受限差额，非作者实际正文、完整旧邻接与来源注POST通过；原分支与失配回退保留，不授实现/复现或生产保证。

若尚不能构造精确直流，训练还可以在保留原 Flow Matching 目标时，软约束模型自己的局部全加速度。一条[受限 velocity 分支](https://arxiv.org/html/2604.04491v1#S4)沿当前预测速度做短 Euler lookahead，再将下一位置的速度作为 stop-gradient target，促使当前速度与其接近。它不另外交付 endpoint flow map，也不由局部 penalty 保证全部轨迹笔直、mode 保全或一步终点正确；正文 L2 与伪码的 weighted/normalized L1 口径尚未统一，不据此发布唯一训练 recipe。Lookahead/finite difference 仍付额外 forward，OT 配对若启用另行计费；有限 CIFAR-10 对照按各指标挑不同 checkpoint，FID 比率不是运行时加速。数据、regularizer 或质量/预算失配时，保留原 FM、多步 solver 与已验收 flow-map/蒸馏路径，以终点质量和完整成本选择少步预算，不由软直线性签发精确积分。<!-- source-family:SF-2026-ARXIV-2604-04491 -->

### [Beyond Hard Negatives: The Importance of Score Distribution in Knowledge Distillation for Dense Retrieval](https://arxiv.org/html/2604.04734v1)

teacher score-spectrum采样→hard-only窄标签人口反侧；评分2+1+2=5，审阅深入完成。精确v1身份和公开日由本家族AB/DOI、官方first-announcement赋号规则、相邻批次/OAI及月列表组合支持Apr07自然日；单Submitted/Updated/created不定义首发。[本日必要Source与逐批独核](../_sources/daily-20260408/SUP_REVIEW_20261014.md)保留必要位置、评价合同与未证明范围。

实际v1§3.1–3.3/T1–2、§4.1–4.3/T3/F2。固定每query池top100retrieved+100randomnegative+1positive，teacherQwen3Reranker8B201分全minmax后，从negative依quantileanchor选不同docK8；两阶段CLinbatch→KD KL/MarginMSE，teacher归一化/采样population改变teacher目标读取。只hard-top压窄score分布，不能从“更难”推出学生更完整学到teacher。BERT/DistilBERT/co-condenser、MSMARCO532k/8.8M、CL/KDb1024/16各1epoch/max512/LR2e-5/τ1，TREC/BEIR13仅retrieval非answertruth。MargMSEco-condensertopmrr.006vsstrat.307是局部collapse反证，不授所有hardmining无效；K4BEIRrandom略优。score8binentropy/range不是semanticcoverage或独立样本多样性，含false-negative/incompletepositive问题未解决。GPU/precision/seeds/mining+teacher总预算/SLO未披露。

本日整合：AGENT-RAG [Ch76](../../../../books/part-07-agent/76-rag.md)。当前owner/完整邻接逐字PRE后，已在原论证内实际写入受限差额，非作者实际正文、完整旧邻接与来源注POST通过；原分支与失配回退保留，不授实现/复现或生产保证。

Teacher 的监督对象之外，负例采样还决定学生看见了 teacher 分数的哪一段。只取最高分 hard negatives，在资源有限且边界局部可靠时合理，却可能把蒸馏标签压到很窄的范围；一条[受限采样分支](https://arxiv.org/html/2604.04734v1#S3)在固定 retrieved+random pool 上统一取得并归一 teacher scores，按 quantile anchors 选择不同 negatives，再用 KL 或 MarginMSE 蒸馏。它扩大的是该 pool 的 teacher-score 覆盖，不是语义多样性、证据完备或答案真值；候选遗漏与 false negatives 仍须另核。有限 student 对照有 hard-top collapse，但 random 在部分预算/域同样或更好，不据此否定所有 hard mining。Pool构造、teacher标注、两阶段训练、索引重建与reader均计费；标签、预算或检索质量失配时，保留hard/random混合、原encoder/index与独立evidence gate，不由分数熵较高批准事实支持。<!-- source-family:SF-2026-ARXIV-2604-04734 -->

### [Training-Free Refinement of Flow Matching with Divergence-based Sampling](https://arxiv.org/html/2604.04646v1)

同t按divergence代理选附近state→不同temporal solver且改distribution；评分2+2+2=6，审阅深入完成。精确v1身份和公开日由本家族AB/DOI、官方first-announcement赋号规则、相邻批次/OAI及月列表组合支持Apr07自然日；单Submitted/Updated/created不定义首发。[本日必要Source与逐批独核](../_sources/daily-20260408/SUP_REVIEW_20261014.md)保留必要位置、评价合同与未证明范围。

实际v1§3.1–3.2/Eq7–11、§5.2/T1、§6.2/F7–8、BAlg1–2、C1–3/T4。standardlinearGaussianpath与optimalmarginalvelocity假设下divergence映射conditionalvelocityvariance；alpha非0本身不授任意schedule单调，实际model代真velocity/Hutchinson单noise只是proxy。每fixedt保原state+M附近Gaussiancandidate，选lowestdivergence后N次迭代，再baseODEsolver；改变state而非仅temporaltruncation，不保持原samplerdistribution。N=M1/earlyt<.5/cosineσ、CIFARσ.2vsImageNet.01。EDM/JiTB/L Euler50/Heun99，matchedtimebaseline77/153；A6000/b32/64fullruns均值，table“Throughput”实际sec/batch。FDS固定NFE更慢，mainFID改善不普遍IS，candidateparallel仍多工作/memory、不接受“无latencyoverhead”泛述。toy empirical100ksamples不是真世界GT，TextImage/Inverseprotocol不混主分母。precision/训练seeds/SLO与独立noisevariance未披露。

本日整合：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)。当前owner/完整邻接逐字PRE后，已在原论证内实际写入受限差额，非作者实际正文、完整旧邻接与来源注POST通过；原分支与失配回退保留，不授实现/复现或生产保证。

调整时间网格之外，sampler 也可以在同一时刻先选择继续积分的状态。一条[受限空间分支](https://arxiv.org/html/2604.04646v1#S3)保留当前状态，抽取附近 Gaussian candidates，以 model divergence 的 Hutchinson 估计择较低者，再交回原 ODE solver；这不是提高 solver 阶数或只减少 temporal truncation。Divergence 与条件 velocity variance 的联系依赖特定 Gaussian path、正系数与 optimal marginal velocity，trained field 和单向量 trace 只是代理，不认证重定位仍保持原目标分布。候选、导数求值和重复选择增加计算与内存，固定 NFE 下通常更慢；近似 wall-time 对照、FID 的局部改善与 IS 的反退须分账，parallel candidates 不等零延迟。代理失准、mode/质量退化或净预算不成立时，保留当前状态、原 Euler/Heun 与已校准时间网格，不从更低 divergence 批准任意生成更可信。<!-- source-family:SF-2026-ARXIV-2604-04646 -->

### [Firebolt-VL: Efficient Vision-Language Understanding with Cross-Modality Modulation](https://arxiv.org/html/2604.04579v1)

token-grid context经FiLM调SSM→有限connector消费而非全decoder保证；评分2+1+2=5，审阅深入完成。精确v1身份和公开日由本家族AB/DOI、官方first-announcement赋号规则、相邻批次/OAI及月列表组合支持Apr07自然日；单Submitted/Updated/created不定义首发。[本日必要Source与逐批独核](../_sources/daily-20260408/SUP_REVIEW_20261014.md)保留必要位置、评价合同与未证明范围。

实际v1§3.3–3.5/Eq3–10、§4.1–4.3、§5.1/5.3/T1–4。text/visionproject后每texttoken对gridsoftmax/TopK/均值head形成contextc，FiLM-in调text→SSM→FiLM-out→residualFFN；不同于concat所有imagefeatures后等reader自己选择。一回T×Gcorrelation仍存在，不采“FlashAttention降低complexity”或globalcrossattentionquadratic/整个LFMlinear。§3.5先X_mm T×D、最后meanpoolB×D与decoderprefix描述有shape差额，只采用该有限connector机制，不授完整tokenizer/servinggraph。S4local对照MME1376对prepend981/Qformer1036，Mamba等同预算细节未披露不泛化architecturecausal。LFM2.8B/SigLIP、twoH10080/b128→8/5epochtotal/best2epoch、CC3M→CoT数据、1H100POPE/maxoutput256；precision/seeds/inputimageprotocol/batchconcurrency/SLO未披露。POPE69.4落后多baseline，TopK4>5是5grid受限反側；connector从stage1frozenbackbone转fullFT，别归全部gain到CMM。

本日整合：MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)。当前owner/完整邻接逐字PRE后，已在原论证内实际写入受限差额，非作者实际正文、完整旧邻接与来源注POST通过；原分支与失配回退保留，不授实现/复现或生产保证。

视觉条件也可以先选择局部 grid context，再调制文本状态的更新，而不把全部视觉 tokens 加入语言序列。一条[受限 connector 分支](https://arxiv.org/html/2604.04579v1#S3.SS5)计算 text-token 对 visual grid 的相关分数，取 top-k context，经 FiLM-in 调制文本、进入 SSM，再以 FiLM-out 调制输出。它改变视觉 cue 的消费位置，不证明被筛掉的细节无关；dense T×G 打分仍在，也不支持普遍 cross-attention quadratic 或完整模型零 KV 的结论。原文 token-level 与最终 pooled 输出的交接形状未统一，此处不补完整 decoder recipe；有限 POPE 与 k=5 切片有反退，单 H100 吞吐也不是服务 SLO。Grid/projector、选择、两次调制与适配训练均计费；局部 cue、输出接口或质量失配时，保留普通 projector、concat/cross-attention 与专用 grounding，不由少视觉消费量批准表示完备。<!-- source-family:SF-2026-ARXIV-2604-04579 -->

### [Think in Strokes, Not Pixels: Process-Driven Image Generation via Interleaved Reasoning](https://arxiv.org/html/2604.04746v1)

partial instruction/global请求与draft/local指令双判→未完成不等错误；评分2+1+2=5，审阅深入完成。精确v1身份和公开日由本家族AB/DOI、官方first-announcement赋号规则、相邻批次/OAI及月列表组合支持Apr07自然日；单Submitted/Updated/created不定义首发。[本日必要Source与逐批独核](../_sources/daily-20260408/SUP_REVIEW_20261014.md)保留必要位置、评价合同与未证明范围。

实际v1§3.1–3.3/4.1/4.3–4.4/T2–7。Plan–Sketch–Inspect–Refine中分别判instruction对globalprompt、draft对当前stepinstruction；未画完但与计划一致的draft不是错误终图。Scenegraph子图/FluxKontext与selfsampled错误轨迹经teacher筛选，CE文本与modalityboundary加flow-MSE图像共享中间上下文；“balanced”与5Kpositive/10Knegative不一致，不采用均衡人口保证。BAGEL7B/8H100/10Ksteps/packed33000/lr2e-5/fullFT，precision/seeds/fullteacher与训练wallcost未披露。T2 .82与T4 .83不同口径，step比不等8×wallclock；局部twoobject/count与WISE反退保留。

本日整合：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)。当前owner/完整邻接逐字PRE后，已在原论证内实际写入受限差额，非作者实际正文、完整旧邻接与来源注POST通过；原分支与失配回退保留，不授实现/复现或生产保证。

中间画面尚未满足最终 prompt，并不自动说明当前 step 失败。过程监督可以分别检查“局部 instruction 是否仍与全局请求一致”及“当前 draft 是否符合这一步 instruction”，让 incomplete-but-consistent 与真正冲突进入不同反馈；文本计划和视觉草稿是两种被判对象，不共享一个终图错误标签。[受限训练接口](https://arxiv.org/html/2604.04746v1#S3)将这种判定与自产错误/修正轨迹纳入交错 CE 和图像 flow 目标，但 teacher 过滤与模型自检仍不是真实生成因果或独立 truth。数据正负人口不均，局部属性/计数有反退，采样步比也不包括文本、teacher、全部forward墙钟。轨迹制备、两类判定与修订均付费；判定关联错误、约束冲突或预算越界时，保留one-shot、外部检查和有限retry，不让“未画完”误触纠正，也不由写得连贯的诊断批准最终发布。<!-- source-family:SF-2026-ARXIV-2604-04746 -->

### [Undetectable Conversations Between AI Agents via Pseudorandom Noise-Resilient Key Exchange](https://arxiv.org/html/2604.04757v1)

受限keyless honest-transcript反例→passive审计排除边界；评分2+2+2=6，审阅深入完成。精确v1身份和公开日由本家族AB/DOI、官方first-announcement赋号规则、相邻批次/OAI及月列表组合支持Apr07自然日；单Submitted/Updated/created不定义首发。[本日必要Source与逐批独核](../_sources/daily-20260408/SUP_REVIEW_20261014.md)保留必要位置、评价合同与未证明范围。

实际v1§1.1、2.4–2.6、5/5.3/Thm5.3、6.1及9。Passive PPT auditor见公开transcript但不见internalrandomness；形式覆盖可重抽honestresponse的agents。Bundle sampler以independent publicseed/mask及entropybound抽L=Omega(lambda/epsilon²)候选；对uniform隐藏bit边际严格匹配honest分布，未配对余额转decoder错误，不是对任意fixedbit的逐条件分布相同。可计算BSC枚举seed亦计费；keyless/constantentropy另需PNR-KE/noiselessfeedback、recognizableentropy及exactnoiselaw，非自动真实LLM自然collusion。非interactive/quasipolynomial攻击、activewarden及robustnoise仍未解。只采用被动文本审计不能给普遍排除隐蔽交流的受限理论边界，不授所有monitor无效、已实现安全协议或生产吞吐；不遍历未采用全proof/代码。

本日整合：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)。当前owner/完整邻接逐字PRE后，已在原论证内实际写入受限差额，非作者实际正文、完整旧邻接与来源注POST通过；原分支与失配回退保留，不授实现/复现或生产保证。

即使审计者知道双方模型、private context 与 honest protocol，被动观察 transcript 仍不是排除所有隐蔽交流的通用证书。一条[受限形式化反例](https://arxiv.org/html/2604.04757v1#S5.SS3)让发送方多次采样 honest message，借独立 public randomness 与带 entropy 门槛的 bundle selection，将分布偏移换成可纠正的解码错误；keyless/constant-entropy 结论还依赖相应 noise-resilient key exchange、feedback 与噪声律。严格分布匹配针对 uniform hidden bits 的边际，不保证任意固定载荷逐条件相同，更不是自然 LLM 已发生 collusion 的实证。多候选、种子求值与协议状态都有成本，active warden 与若干密码假设仍未解决；它不证明所有监测无效或某个训练/架构防御已成立。能力与信任条件不明时，保留现有 monitor、独立 outcome、通信限制与 effect-time gate，把“未识别隐写”记为有限观察而不是无隐写或权限许可。<!-- source-family:SF-2026-ARXIV-2604-04757 -->

### [E-VLA: Event-Augmented Vision-Language-Action Model for Dark and Blurred Scenes](https://arxiv.org/html/2604.04834v1)

recent-N event窗口截至RGB exposure→variable freshness与fusion费用；评分2+2+2=6，审阅深入完成。精确v1身份和公开日由本家族AB/DOI、官方first-announcement赋号规则、相邻批次/OAI及月列表组合支持Apr07自然日；单Submitted/Updated/created不定义首发。[本日必要Source与逐批独核](../_sources/daily-20260408/SUP_REVIEW_20261014.md)保留必要位置、评价合同与未证明范围。

实际v1§3.1–3.4/4/5.1–5.7/T1–5/7.3/9/12。DAVISwrist egomotion改变eventrate，取RGBexposureend前recentN2000事件而非固定timewindow，时间跨度随运动变，不保证固定freshness。Polarityagnostic count/normalization/demosaic的adapter与latestpolarityoverlay不同表示；原visualtoken不增仍加13.3M/20.4GF。SmolVLA/SigLIPfrozen、action/projectiontrain/4block384/fuse3/6/9/12；SO100/DAVIS346/Orin/30Hz、sync40action~1.33s，724episode339Kframes。A80020Kaction后新Event10K+Joint10K，非matchedtotaltrainbudget。10测试配置partialcredit与限时评分不等完整success/safety；20luxPick90vs0仅局部，OOD45、event数500/4000退、静止/颜色信息和遮挡仍失效，sorting/blur反侧保留。Precision/seeds/全service费用tail未披露。

本日整合：MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)。当前owner/完整邻接逐字PRE后，已在原论证内实际写入受限差额，非作者实际正文、完整旧邻接与来源注POST通过；原分支与失配回退保留，不授实现/复现或生产保证。

Event sensor 的累积窗口还不能只用 frame interval 表达。固定时间窗保持同一时长，在运动强弱变化时却产生很不一样的事件人口；一条[受限感知分支](https://arxiv.org/html/2604.04834v1#S3)取 RGB exposure end 前最近 N 个事件，归一累积成图并经轻量 adapter 融入已有视觉 features。窗口因 event rate 与相机自运动改变长度，因果截点不等固定 freshness；count/polarity 表示、demosaic、exposure 与 adapter revision 应一起交付 consumer。视觉 token 数不增也不使新表示/adapter免费，静止、颜色语义与遮挡缺口仍在；有限低光操作的 partial-credit 分数不是完整任务成功或安全率，额外训练亦非同预算。窗口/时间同步、cue或下游质量失配时，保留原 RGB、较短或固定时间窗与独立控制验收，不由事件计数批准当前世界事实或动作提交。<!-- source-family:SF-2026-ARXIV-2604-04834 -->

### [Are Latent Reasoning Models Easily Interpretable?](https://arxiv.org/html/2604.04902v1)

early agreement与可解码trace不等正确/必要真实过程；评分2+2+2=6，审阅深入完成。精确v1身份和公开日由本家族AB/DOI、官方first-announcement赋号规则、相邻批次/OAI及月列表组合支持Apr07自然日；单Submitted/Updated/created不定义首发。[本日必要Source与逐批独核](../_sources/daily-20260408/SUP_REVIEW_20261014.md)保留必要位置、评价合同与未证明范围。

实际v1§3/4.1–4.3/5.1–5.2/6–6.1/I3。Forced endthought早停测first/stableprediction agreement，三mode matcheddata对照分离训练监督差异；在所测logic中latent步非必要，而GSM仍有必要，稳定不等正确也不证明无search。Top10 vocabulary数值投影经questionoperand/后向关系寻找goldtrace，operator未直接读出；CODILlama覆盖与其它模型不同。Forwardchain枚举候选算术并改三promptoperand验证，仅460unique/single-token数字子集，1/3→3/3阈值使通过率93→67%，未检出不等无机制。Goldtrace训练先验/任务已知算子、回溯重排与误算均限制外推；不授唯一真实程序、普遍可解释或生产早停。GPU/precision/seeds必要fields未披露；不把模型训练称无监督。

已有覆盖：MODEL-SELF-ATTENTION [Ch14](../../../../books/part-02-model/14-self-attention.md)。Ch14“可解码不等于单点拥有因果控制权”已分probe、单/多位置transplant、必要/充分与原生读出；Ch66 failure direction持有独立intervention/control survival。 非作者已实际读当前承载正文/完整相关局部，此决定不是主题相似或仅Review note匹配，不新增同义书稿。

### [Vero: An Open RL Recipe for General Visual Reasoning](https://arxiv.org/html/2604.04917v1)

typed reward＋mixture局部negative-transfer→条件人口/质量分账；评分2+2+2=6，审阅标准完成。精确v1身份和公开日由本家族AB/DOI、官方first-announcement赋号规则、相邻批次/OAI及月列表组合支持Apr07自然日；单Submitted/Updated/created不定义首发。[本日必要Source与逐批独核](../_sources/daily-20260408/SUP_REVIEW_20261014.md)保留必要位置、评价合同与未证明范围。

实际v1§3.3/Eq2–4、4.2/T4、5/8和B2–3。Sixcategory reward router分别核符号、numeric、list、IoU、webaction与openjudge；.8accuracy+.2format+overlong，coordinate规范依base版本，不合并单recipe。Qwen3-32B judge只看text/ref、不见image，不能认证visualtruth。100Ksinglecategory对100Kmixture局部类别mean negative-transfer缓解，不等response/token/compute预算相同，600K另增exposure；BLINK/ERQA/FVQA等反退与caption跨类损失保留。“消除”仅所测类别mean，算法GSPO比较quarterepoch五类mean .4pp不拼fullsix。8H100或H200/FSDP2/G8/b256/2000steps、QwenFP16/MiMoBF16/clip.0003/.0004/KL0/context24576–36864/image3072²或4096²、judge temp.7/max1024；seeds/tail/完整SLO未披露。只采用typedreward与混合人口的transfer分责，不审AIforScience应用全集。

已有覆盖：TRAIN-DATA [Ch27](../../../../books/part-04-training-system/27-data.md)。Ch27数据mixture人口/组合非可加及recipe匹配，Ch33 reward channel/format/content/heldout分账已承载typed reward与受限transfer边界。 非作者已实际读当前承载正文/完整相关局部，此决定不是主题相似或仅Review note匹配，不新增同义书稿。


### [ClawArena: Benchmarking AI Agents in Evolving Information Environments](https://arxiv.org/html/2604.04202v1)

动态GT/belief revision与workspace outcome分评；评分2+2+2=6，审阅标准完成。精确v1身份和公开日由本家族AB/DOI、官方first-announcement赋号规则、相邻批次/OAI及月列表组合支持Apr07自然日；单Submitted/Updated/created不定义首发。[既有精确必要Source](../_sources/daily-20260407/v3-reopen-notes.md)（按ID定位最新有效段，原记录定位294）保留必要位置、评价合同与未证明范围。

- **2604.04202v1 / ClawArena**：[原文](https://arxiv.org/html/2604.04202v1) §2–3、Appendix B。hidden Layer0经多渠道噪声/冲突与staged updates产生可追溯ground truth，MC set-selection、belief revision graded、silent preference checks、executable workspace checks分开。64scenarios/1879rounds/365updates，但cross-framework只startup-outage一scenario，cross-model12scenarios337rounds；MC前者per-option、后者exact-match，不可横比range推断模型比框架重要。Table4标GPT5.1、正文说5.2，identity口径不一致；3.5pp单配置subset差不能证明所有模型representativeness。Ch66已有动态信息/可执行witness测量，机制可作为受限例证，框架与模型排名仅报告。

已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。Ch66动态phase、关系回归、Outcome Witness及belief/action/outcome分别持有时变truth、真实workspace与分层分母。 非作者已实际读当前承载正文/完整相关局部，此决定不是主题相似或仅Review note匹配，不新增同义书稿。

### [Three Phases of Expert Routing: How Load Balance Evolves During Mixture-of-Experts Training](https://arxiv.org/html/2604.04230v1)

MFG proxy/phase非普遍→只保受限routing诊断；评分2+1+2=5，审阅标准完成。精确v1身份和公开日由本家族AB/DOI、官方first-announcement赋号规则、相邻批次/OAI及月列表组合支持Apr07自然日；单Submitted/Updated/created不定义首发。[既有精确必要Source](../_sources/daily-20260407/v3-reopen-notes.md)（按ID定位最新有效段，原记录定位295）保留必要位置、评价合同与未证明范围。

- **2604.04230v1 / Three Phases of Expert Routing**：[原文](https://arxiv.org/html/2604.04230v1) §2–6/8。Mean-field game用router logits估reduced preference而非独立expert quality；static MFG等temperature softmax，independent cluster-softmax L1=.133比coupledMFG .146更好。OLMoE20checkpoints50texts和OpenMoE6checkpoints30texts支持effective congestion非单调轨迹；后者还有dormant phase，不宜写同三个阶段普遍成立。Dense softmax模型top1 out-of-scope，continuation bound8–35倍实误差，线性congestion假设不涵盖hard capacity。只能把拟合参数作为diagnostic，不证明调balance loss会提高模型质量；Ch21已有routing dynamics/负载与specialization分开，本次仅报告，不新增长期routing算法。

仅报告：MFG/phase只作所测checkpoint的routing诊断，cluster baseline更好与dormant phase不授统一训练控制；证据保留，不新增长期算法或Books机制。

### [Combee: Scaling Prompt Learning for Self-Improving Language Model Agents](https://arxiv.org/html/2604.04247v1)

LLM reduce非结合律→bounded fan-in/context version；评分2+2+2=6，审阅标准完成。精确v1身份和公开日由本家族AB/DOI、官方first-announcement赋号规则、相邻批次/OAI及月列表组合支持Apr07自然日；单Submitted/Updated/created不定义首发。[既有精确必要Source](../_sources/daily-20260407/v3-reopen-notes.md)（按ID定位最新有效段，原记录定位299）保留必要位置、评价合同与未证明范围。

- **2604.04247v1 / Combee**：[原文](https://arxiv.org/html/2604.04247v1) §3–4。sqrt(batch)组内再组间聚合、重复reflection后shuffle平衡位置偏差；LLM reduce并非数学上可交换/结合的scan。Batch profile用power-law delay和plateau阈值选择并行数，仍同步提交下一context。Ch77“并行经验汇总需要Bounded Fan-in与Context Version”实际正文已写worker局部证据→curator提交、parent version、冲突、同源错误与sequential共存；不是仅Review note。

已有覆盖：AGENT-MEMORY [Ch77](../../../../books/part-07-agent/77-memory.md)。Ch77“并行经验汇总需要Bounded Fan-in与Context Version”两段持有worker局部证据/curator提交、parent version/冲突及同源错误。 非作者已实际读当前承载正文/完整相关局部，此决定不是主题相似或仅Review note匹配，不新增同义书稿。

### [3D-Stacked NMP, LLM Decoding, Systolic Array Microarchitecture, Multi-Core Scheduling](https://arxiv.org/html/2604.04253v1)

shape/buffer/placement联合→模拟与真实硬件分责；评分2+2+2=6，审阅标准完成。精确v1身份和公开日由本家族AB/DOI、官方first-announcement赋号规则、相邻批次/OAI及月列表组合支持Apr07自然日；单Submitted/Updated/created不定义首发。[既有精确必要Source](../_sources/daily-20260407/v3-reopen-notes.md)（按ID定位最新有效段，原记录定位401及420）保留必要位置、评价合同与未证明范围。

- **04253 Near-memory processor**：§6.1.3/6.6已补。FP16/7nmASAP7、netlist+simulation能量与ScaleSim/Ramulator/lookupreplay；8device TP=8且共同H100prefill，MoE仍TP避免与EP变化混淆。固定4096PE时square化减filterbuffer却增activationbuffer，dense和MoE形状偏好不同；非制造芯片或生产SLO。2+2+2=6标准完成，硬件execution-plan可作为受限DSE例证，Ch49已有shape/memory联合约束与模型误差已实际对读确认覆盖。

已有覆盖：INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)。Ch49 Chiplet Pool与Execution Plan联合演化、Typed System IR、跨算子buffer/ordering与cost-model分责持有形状/存储/放置联合设计，非silicon实证。 非作者已实际读当前承载正文/完整相关局部，此决定不是主题相似或仅Review note匹配，不新增同义书稿。

### [APPA: Adaptive Preference Pluralistic Alignment for Fair Federated RLHF of LLMs](https://arxiv.org/html/2604.04261v1)

frozen本地偏好reward vectors→中央PPO而非fedavg；评分3+2+2=7，审阅深入完成。精确v1身份和公开日由本家族AB/DOI、官方first-announcement赋号规则、相邻批次/OAI及月列表组合支持Apr07自然日；单Submitted/Updated/created不定义首发。[既有精确必要Source](../_sources/daily-20260407/v3-reopen-notes.md)（按ID定位最新有效段，原记录定位300）保留必要位置、评价合同与未证明范围。

- **2604.04261v1 / APPA**：[原文](https://arxiv.org/html/2604.04261v1) §3、实验及Appendix训练配置。冻结PluralLLM在各group本地数据上提供reward vectors，不传模型参数/梯度供fed averaging；中央PPO按历史EMA(.8)、reverse softmax(T=.1)、FI阈值(.99)调权。低且相等reward也能FI=1，fairness score不是质量。GLOBALQA/OQA，Gemma2-2B/Llama3.2-3B/Qwen3-.6B；SFT BF16、PPO NF4/BF16 LoRA-r16、maxseq500/response60，三A100节点并行不同实验、每run单卡，不是分布式训练证据。本次3+2+2=7纠错深入；Ch31已明确客户端只返回reward vectors、中央更新policy，当前真实正文及有效POST已读回复用。

本日恢复决定为整合：TRAIN-RLHF [Ch31](../../../../books/part-04-training-system/31-rlhf.md)。既有真实正文与有效Source/非作者POST一致，本轮reader实际当前完整局部对读复用；不再写同义段或加fresh计数。

### [How Well Do Agentic Skills Work in the Wild: Benchmarking LLM Skill Usage in Realistic Settings](https://arxiv.org/html/2604.04323v1)

Skill loaded/selected/retrieved/adapted分层真实controlpath；评分2+2+2=6，审阅标准完成。精确v1身份和公开日由本家族AB/DOI、官方first-announcement赋号规则、相邻批次/OAI及月列表组合支持Apr07自然日；单Submitted/Updated/created不定义首发。[既有精确必要Source](../_sources/daily-20260407/v3-reopen-notes.md)（按ID定位最新有效段，原记录定位301）保留必要位置、评价合同与未证明范围。

- **2604.04323v1 / Skills in the Wild**：[原文](https://arxiv.org/html/2604.04323v1) §3–4、Appendix B。强制载入→自动选择→检索curated/noncurated分阶段；SkillBench/TerminalBench、ClaudeOpus4.6/KimiK2.5/Qwen3.5、Harbor Docker三run。非curated对Qwen/Kimi可低于baseline，query-specific修订受starting artifact相关性限制；GPT5.4 coverage judge相关性不是因果验证。Timeout设定模型不同，不把排名当同预算比较。Ch66真实controlpath已实际对读，loading/selection/retrieval/adaptation分责，不虚构Skill专章。

已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。Ch66 Skill真实controlpath分别验loaded→selection→retrieval→adaptation及no-Skill反侧。 非作者已实际读当前承载正文/完整相关局部，此决定不是主题相似或仅Review note匹配，不新增同义书稿。

### [GENSERVE: Efficient Co-Serving of Heterogeneous Diffusion Model Workloads](https://arxiv.org/html/2604.04335v1)

两deadline＋step VideoState恢复共置→总命中与video尾分账；评分2+2+2=6，审阅深入完成。精确v1身份和公开日由本家族AB/DOI、官方first-announcement赋号规则、相邻批次/OAI及月列表组合支持Apr07自然日；单Submitted/Updated/created不定义首发。[既有精确必要Source](../_sources/daily-20260407/v3-reopen-notes.md)（按ID定位GenServe必要方法/配置/反側）保留必要位置、评价合同与未证明范围。

- 身份与归属：[GenServe `2604.04335v1`](https://arxiv.org/html/2604.04335v1)，属于上文 `03232`～`04934` 的有界公告批次推断；HTML 页眉的 `06 Apr 2026` 不能直接换成北京日报日期。未见此 v1 撤回标记。与其他网站/列表转载按同一 Source Family 去重。

- 初筛贡献：Ch56 已讨论 LLM 抢占、视频播放 slack 和 DiT 的 step work，但未把共置 T2I/T2V 的两套 deadline、可恢复 VideoState、图像组批与视频 sequence parallelism 当作同一个调度决策；这是一条有条件的系统设计分支，不是“扩散推理更快”的单点数字。

- Method §3–4：T2I 短请求在 FCFS 下被长视频阻塞；纯短作业优先又可能使视频过期。调度器在 denoising step 边界对视频暂停/恢复，保留 latent、mask、prompt embedding 与 step index；图像用截止时间组批，视频可调 SP degree，有限 GPU 上以可达 deadline 数及 slack 比较候选动作。前提是两套模型权重能在所测 GPU 上共驻、step 状态确实可恢复；不能照搬自回归 KV 调度。

- 实现与评价 §5–6：作者用 Diffusers、Wan、xFuser 实现；单机 8×RTX PRO 6000 Blackwell 96GB，SD3.5 Medium 2.5B 与 Wan2.2 T2V5B，合成 100-request Poisson/bursty traces，图像/视频比 20:80、50:50、80:20，视频 81 帧；截止时间按离线运行时长乘 `1.5×σ` 构造（`σ=0.8–1.3`）。精度、真实用户流量、跨节点拓扑与生产 tail-SLO 不由这些实验证明。

- 关键消融与反证 §6.2–6.3：skewed resolution、balanced mix、24 req/min、`σ=1` 下，FCFS 的 overall/image/video SAR 为 `20/20/20%`；仅加入视频抢占为 `39/68/10%`；加 DP solver 为 `58/94/22%`；再加 SP switching 为 `63/94/32%`。视频尾延迟在 default configuration 的 p99 为 GenServe `229s`、FCFS `166s`，说明优化总体命中率可能牺牲已超时的长视频，不可宣称两类请求无条件同时改善。

- 机制边界：预创建 communicator、GPU 上保留 VideoState 与同卡共载是作者实现条件；低负载下 solver 增益较小，静态 GPU 池或简单 reservation 在稳定负载或不可靠恢复时仍成立。作者 benchmark 未证明生产多租户、安全隔离、资源漂移或图像质量无损。

- Books 对读：唯一 owner 为 `INFER-SCHEDULING` Ch56。主任务已在该章 progress-state 论证后写入窄幅段落；本日作者独立对读 HTML v1 §4/§6.1–6.3 与 Ch56 新段，确认机制、条件和负面证据均准确。本日分母与整合状态已同步；本单篇有效层不替代六部分DAY。

本日恢复决定为整合：INFER-SCHEDULING [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md)。既有真实正文与有效Source/非作者POST一致，本轮reader实际当前完整局部对读复用；不再写同义段或加fresh计数。

### [GUIDE: Interpretable GUI Agent Evaluation via Hierarchical Diagnosis](https://arxiv.org/html/2604.04399v1)

recoverable subtask聚合→非step hardAND/终局叙述；评分2+2+2=6，审阅深入完成。精确v1身份和公开日由本家族AB/DOI、官方first-announcement赋号规则、相邻批次/OAI及月列表组合支持Apr07自然日；单Submitted/Updated/created不定义首发。[既有精确必要Source](../_sources/daily-20260407/v3-reopen-notes.md)（按ID定位最新有效段，原记录定位302）保留必要位置、评价合同与未证明范围。

- **2604.04399v1 / GUIDE**：[原文](https://arxiv.org/html/2604.04399v1) §3–4、消融。Action-text segmentation→VLM用subtask截图/全局目标评分→LLM聚合可恢复错误，不是memory-write机制，也不是hard AND所有subtask。Gemini3Flash/o4mini，932条ecommerce(345success/587fail)、5–80steps，AgentRewardBench1302/Android480；去seg74.14低于naive85.61因prompt专为subtask，去summary87.41/recall69.28对full95.80/93.62。200subtask单annotatorκ=.89不证明整体真值；implicit business norms未输入时仍错误。JSON最多retry10，须计调用成本。本日已具体比较并整合“recoverable subtask evidence聚合≠逐步失败即终局失败”的差额。

本日整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。当前owner/完整邻接逐字PRE后，已在原论证内实际写入受限差额，非作者实际正文、完整旧邻接与来源注POST通过；原分支与失配回退保留，不授实现/复现或生产保证。

长轨迹还能先形成 subtask 局部证据，再判断这些错误是否在终局被恢复，而不是把每个局部 fail 作 hard AND。一条[受限分层 judge](https://arxiv.org/html/2604.04399v1#S3)按动作文本切段，用对应 screenshots 与全局目标评局部进展，再聚合为最终 verdict；segmentation、summary、recoverability 与completion因此是不同对象。LLM aggregator仍可漏掉隐含businessnorm、错分段或被连贯叙述说服，不能代独立产物/sideeffect witness；专门为subtask设计的prompt在去seg消融中退步，也不单独证明分段是全部收益来源。局部人工一致率不认证全部真值，retry/分段/多judge调用均计费。证据或聚合失配时，保留完整轨迹、关键subtask直接回读与独立终局checks，不由局部全pass或可恢复解释自动签success。<!-- source-family:SF-2026-ARXIV-2604-04399 -->

### [Relative Density Ratio Optimization for Stable and Statistically Consistent Model Alignment](https://arxiv.org/html/2604.04410v1)

混合density bounded ratio→非参数梯度/偏好真值保证；评分2+1+2=5，审阅深入完成。精确v1身份和公开日由本家族AB/DOI、官方first-announcement赋号规则、相邻批次/OAI及月列表组合支持Apr07自然日；单Submitted/Updated/created不定义首发。[既有精确必要Source](../_sources/daily-20260407/v3-reopen-notes.md)（按ID定位最新有效段，原记录定位333）保留必要位置、评价合同与未证明范围。

- **2604.04410v1 / RDRO**：[原文](https://arxiv.org/html/2604.04410v1) §3.1–3.4、§5、Appendix F。Preferred与nonpreferred支持不同使ordinary ratio不稳，relative ratio `p+/(αp+ +(1−α)p−)`限制在[0,1/α]；gradient系数有界不等于所有参数梯度有界，consistency依赖population risk/可表示目标，finite-sample bound仍有函数类/样本前提。Qwen2.5Instruct1.5/3B、Llama3Instruct3/8B，UF-G6088/9644和MIX14K6750/6750、TRL/AdamW1epoch lr5e−7batch128/clip1、8H10080/ZeRO3、三seed，AlpacaEval GPT4Turbo length-controlled judge。UF-G多数改善，MIX14K非全胜且多α与DDRO无显著差；需全标binary偏好，理论不是人类偏好普遍正确保证。

本日整合：TRAIN-DPO [Ch34](../../../../books/part-04-training-system/34-dpo.md)。当前owner/完整邻接逐字PRE后，已在原论证内实际写入受限差额，非作者实际正文、完整旧邻接与来源注POST通过；原分支与失配回退保留，不授实现/复现或生产保证。

概率比较还可以改变分母，而不只给既有 pair gradient 加 gate。一条[受限 relative-density 分支](https://arxiv.org/html/2604.04410v1#S3)比较 positive density 与正负 population 的混合：p₊/(αp₊+(1−α)p₋)，混合权重0<α<1时比值不超过1/α。它以混合目标约束 ratio 的数值范围及相关梯度系数，不保证任意网络参数梯度或整条训练轨迹有界，也不认证偏好标签真实。Population consistency 另依目标可表达等假设，有限样本/模型的边界不能直接外推人类偏好或发布安全；α搜索、训练与独立likelihood/KL/行为评价都付费。支持重叠充分、原recipe稳定或混合目标无益时，保留vanilla DPO及原probabilitygate，不把bounded ratio叫无代价的普适对齐。<!-- source-family:SF-2026-ARXIV-2604-04410 -->

### [ShieldNet: Network-Level Guardrails against Emerging Supply-Chain Injections in Agentic Systems](https://arxiv.org/pdf/2604.04426v1)

MITM/PCAP network-effect sensor→host盲区/已泄露不可撤；评分2+2+2=6，审阅深入完成。精确v1身份和公开日由本家族AB/DOI、官方first-announcement赋号规则、相邻批次/OAI及月列表组合支持Apr07自然日；单Submitted/Updated/created不定义首发。[既有精确必要Source](../_sources/daily-20260407/v3-reopen-notes.md)（按ID定位最新有效段，原记录定位303）保留必要位置、评价合同与未证明范围。

- **2604.04426v1 / ShieldNet**：[PDF原文](https://arxiv.org/pdf/2604.04426v1) pp4–9。HTML标v1却显示August24封面，故本次Method/结果以April7封面的PDF v1为准，版本污染隔离。MITM系统proxy+PCAP并blockUDP443限制QUIC，将解密HTTP插回typed时间事件；Qwen3-.6B SFT对event窗口识别网络副作用。10k+MCP tools/25techniques用canary确认activation，6k训练、heldout17servercategories/3techniques。Table2 any-trace FPR.022/F1.998；Table3 per-PCAP FPR.008/F1.995、时间overhead21.38%，不得混口径或称零成本；不解密FPR.896。检测是已观察effects，不能防止已发生exfiltration；host-local行为/其他协议不覆盖。MITM权限、隐私、证书与deterministic egress authority仍必要。Hardware/precision Not Disclosed。

本日整合：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)。当前owner/完整邻接逐字PRE后，已在原论证内实际写入受限差额，非作者实际正文、完整旧邻接与来源注POST通过；原分支与失配回退保留，不授实现/复现或生产保证。

工具文本看起来正常，也可能在另一个执行面已经发生网络副作用。一个[受限网络 sensor](https://arxiv.org/pdf/2604.04426v1)在系统代理/MITM和PCAP中观察解密的HTTP行为，将其整理成带时序的事件供小模型判风险；它补的是prompt/tooltrace之外的可观测effects，不是由Agent自报真实访问。解密权限、证书、隐私与QUIC限制共同决定覆盖，host-local或其它protocol仍是盲区；已发送的exfiltration不能由事后detector撤回，前置egress权限与effect-time gate仍须独立成立。Pertrace和perPCAP误报分母不同，额外网络/推理开销不能抹掉。协议、窗口或sensor质量失配时，保留原trace、最小网络权限与独立outcome/incident检查，不以低误报率签发尚未发生危害或完整供应链安全。<!-- source-family:SF-2026-ARXIV-2604-04426 -->

### [Beyond Few-Step Inference: Accelerating Video Diffusion Transformer Model Serving with Inter-Request Caching Reuse](https://arxiv.org/html/2604.04451v1)

跨request分时段/区域features reuse→近prompt非KV等价；评分2+2+2=6，审阅深入完成。精确v1身份和公开日由本家族AB/DOI、官方first-announcement赋号规则、相邻批次/OAI及月列表组合支持Apr07自然日；单Submitted/Updated/created不定义首发。[既有精确必要Source](../_sources/daily-20260407/v3-reopen-notes.md)（按ID定位最新有效段，原记录定位377）保留必要位置、评价合同与未证明范围。

- **2604.04451v1 / Chorus**：[原文](https://arxiv.org/html/2604.04451v1) Method/评测。相同/近邻prompt用CLIP语义早期full/middle regional/late none跨请求cache，TGAA编辑局部latent；Wan1.3/14B四步与50step、4H20/A100。VidProM50k中选一个cluster2000、warm/arrival半分及cachehit150，受限非全真实arrival分布。CLIP31.758→30.798质量下降不能叫无损；理想1.45ratio实测1.23。2+2+2=6，旧必要Source层有效，本日就Ch24跨request具体差额进一步深入并实际整合，非普遍KV复用。

本日整合：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)。当前owner/完整邻接逐字PRE后，已在原论证内实际写入受限差额，非作者实际正文、完整旧邻接与来源注POST通过；原分支与失配回退保留，不授实现/复现或生产保证。

少步视频生成里，单请求可复用的时间更短，还可以尝试从近邻请求借中间features。一条[受限跨请求分支](https://arxiv.org/html/2604.04451v1)按prompt相似性提议cache hit，早期较完整地复用、中段按区域调整、末段停止复用，并编辑局部latent以适配新condition。Prompt embedding近不证明目标视频相同，复用对象是所绑model/denoising阶段的近似features，不是exacttokenKV命中；旧请求的质量或内容身份不能自动转给新请求。有限cluster/arrival人口与cachehit条件、实测质量下降都保留，理想速度比不等实测。匹配/区域编辑、cache驻留、warmup与质量回归均付费；condition、阶段或收益失配时，拒绝借用并回fullrecompute、单请求cache或原生成器，不由命中率批准无损或生产SLO。<!-- source-family:SF-2026-ARXIV-2604-04451 -->

### [HDP: A Lightweight Cryptographic Protocol for Human Delegation Provenance in Agentic AI Systems](https://arxiv.org/pdf/2604.04522v1)

issuer单key provenance≠named-agent亲签/即时离线撤销；评分2+2+2=6，审阅深入完成。精确v1身份和公开日由本家族AB/DOI、官方first-announcement赋号规则、相邻批次/OAI及月列表组合支持Apr07自然日；单Submitted/Updated/created不定义首发。[既有精确必要Source](../_sources/daily-20260407/v3-reopen-notes.md)（按ID定位最新有效段，原记录定位344）保留必要位置、评价合同与未证明范围。

- **2604.04522v1 / HDP审阅补全**：PDF§5–7明确v0.1issuer同key只能证明hop由issuer记录，不证明namedagent亲签；token pii移除会破坏rootsig，只能标audit-only。Same-session未过期stolen replay未被完全消除；标准化仅individualIETFsubmission非WG采纳，声称<2ms没有文中受控测试。对读Ch72“多跳Delegation必须保留HumanPrincipal”现正文已明确issuer-vs-delegate、scope、expiry/离线revocation取舍和semanticvalidation。

已有覆盖：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)。Ch72 delegation完整论点持有issuer授权hop与principal签名区别、scope/expiry/replay/effect责任。 非作者已实际读当前承载正文/完整相关局部，此决定不是主题相似或仅Review note匹配，不新增同义书稿。

### [Multilingual Prompt Localization for Agent-as-a-Judge: Language and Backbone Sensitivity in Requirement-Level Evaluation](https://arxiv.org/html/2604.04532v1)

judge语言改变需求判定→solver与evaluator身份分开；评分2+1+2=5，审阅标准完成。精确v1身份和公开日由本家族AB/DOI、官方first-announcement赋号规则、相邻批次/OAI及月列表组合支持Apr07自然日；单Submitted/Updated/created不定义首发。[既有精确必要Source](../_sources/daily-20260407/v3-reopen-notes.md)（按ID定位最新有效段，原记录定位335）保留必要位置、评价合同与未证明范围。

- **2604.04532v1 / Multilingual DevAI**：[原文](https://arxiv.org/html/2604.04532v1) §3–5/7。固定55tasks/三developer frameworks同artifact与judge pipeline，在五种语言六backbones测requirement verdict，paired Wilcoxon/Holm/95%bootstrap支持judge-language排名变化，不是重新运行solver质量差异。缺multilingual人类gold、terminationmetadata不全、cost fields全0；runtime/tokens只proxy。均值std为task variation不可当多次运行误差；低baseline会压缩语言差异。Ch66已有evaluator language/construct identity。

已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。Ch66 pairwise envelope与agreement测量身份保artifact/solver、judge/template/language/scale/pooling不同对象。 非作者已实际读当前承载正文/完整相关局部，此决定不是主题相似或仅Review note匹配，不新增同义书稿。

### [Mapping the Exploitation Surface: A 10,000-Trial Taxonomy of What Makes LLM Agents Exploit Vulnerabilities](https://arxiv.org/html/2604.04561v1)

goal reframing局部反证→叙述不授dispatch/effect权限；评分2+2+2=6，审阅深入完成。精确v1身份和公开日由本家族AB/DOI、官方first-announcement赋号规则、相邻批次/OAI及月列表组合支持Apr07自然日；单Submitted/Updated/created不定义首发。[既有精确必要Source](../_sources/daily-20260407/v3-reopen-notes.md)（按ID定位最新有效段，原记录定位336）保留必要位置、评价合同与未证明范围。

- **2604.04561v1 / Prompt Condition Exploitation**：[原文](https://arxiv.org/html/2604.04561v1) §2–5/8.5。Ephemeral Docker无network/mount，37promptconditions同safetyinstruction，编程题+人工埋三类test bypass；五主backbonesn45–50/cell、两个时间快照模型，Fisher/Clopper–Pearson/Bonferroni。只有三goalreframing在Claude单模型校正后显著；checkhidden不通过单模型校正，不能称全部12心理维度机制成立。判定是关键词toolcall而非完整harm detector；自然配置、其他攻击和GPT4.1零结果归因未证，traces仅每条件5补采样。Ch72已有goal-preservinginjection与独立authorization。

已有覆盖：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)。Ch72 goal alignment/组合授权持有目标叙述不授dispatch/effect权限；局部单模型反证不成为普遍taxon。 非作者已实际读当前承载正文/完整相关局部，此决定不是主题相似或仅Review note匹配，不新增同义书稿。


### [The Energy Cost of Execution-Idle in GPU Clusters](https://arxiv.org/html/2604.04745v1)

execution-idle与deep idle分母→驻留节能/尾成本；评分2+2+3=7，审阅深入完成。精确v1身份和公开日由本家族AB/DOI、官方first-announcement赋号规则、相邻批次/OAI及月列表组合支持Apr07自然日；单Submitted/Updated/created不定义首发。[既有精确必要Source](../_sources/daily-20260407/v3-reopen-notes.md)（按ID定位最新有效段，原记录定位337）保留必要位置、评价合同与未证明范围。

- **2604.04745v1 / GPU Execution-Idle**：[原文](https://arxiv.org/html/2604.04745v1) §2.1–2.3/4.3/4.5/5.1/5.3。756GPU学术Slurm整卡、31days1Hz遥测；residentjob同时compute/memory<5%、communication<1GB/s且持续5s形成execution-idle，缺信号省略不可当0。19.17%时间/10.67%能量的分母是in-execution排除deepidle，不是全机房。Keyword job分类/通信前序聚类只相关不是原因。Llama13B/vLLM/L40S回放公开到达和长度；8GPUpacking可令energy56%而avgSM相近。1175s同request总量的3s触发/5s冷却降频：SM-only平均power−22%、p95+29%；SM+memory−34%、p95+160%，不能外推SLO。Ch70既有实际正文现已分resident-executionidle/deepidle能量与utility，本轮读回有效层复用。

本日恢复决定为整合：PLATFORM-COST [Ch70](../../../../books/part-06-ai-infrastructure/70-cost.md)。既有真实正文与有效Source/非作者POST一致，本轮reader实际当前完整局部对读复用；不再写同义段或加fresh计数。

### [DeepStack: Scalable and Accurate Design Space Exploration for Distributed 3D-Stacked AI Accelerators](https://arxiv.org/html/2604.04750v1)

硬件/parallel plan联合DSE→模型误差与thermal限制；评分2+2+2=6，审阅标准完成。精确v1身份和公开日由本家族AB/DOI、官方first-announcement赋号规则、相邻批次/OAI及月列表组合支持Apr07自然日；单Submitted/Updated/created不定义首发。[既有精确必要Source](../_sources/daily-20260407/v3-reopen-notes.md)（按ID定位最新有效段，原记录定位338）保留必要位置、评价合同与未证明范围。

- **2604.04750v1 / DeepStack**：[原文](https://arxiv.org/html/2604.04750v1) §3.1–3.3、4.2、5.1/5.6。Graph→area/thermal合法hardware→TP/EP/SP/CP/DP/FSDP/PP→peroperator tiling/collectives联合搜索，漏EP会令硬件选择也变，不只是软件latency。MoE routing取trace、activation/KV/10%reserve筛配置；分层top5%prune不是全局最优证明。H100/B200实机仅校准kernel/runtime模型；3Dstack性能是7nm/固定area25600mm²建模，H100*/H200*缩放非当前市售卡直比；Llama70/405、DeepSeek/QwenA16W8/16、input/output1024/batch1–1024。Ch49已有execution-plan联合模型/硬件约束，当前DSE模型误差/不可逆设计边界已有具体正文承载。

已有覆盖：INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)。Ch49 Chiplet Pool与Execution Plan联合演化和Typed System IR持有硬件/并行计划共同搜索、模型误差/热设计/实际runtime回退。 非作者已实际读当前承载正文/完整相关局部，此决定不是主题相似或仅Review note匹配，不新增同义书稿。

### [Your Agent, Their Asset: A Real-World Safety Analysis of OpenClaw](https://arxiv.org/html/2604.04759v1)

self-state/harness持久毒化→load/activation再admission；评分2+2+2=6，审阅深入完成。精确v1身份和公开日由本家族AB/DOI、官方first-announcement赋号规则、相邻批次/OAI及月列表组合支持Apr07自然日；单Submitted/Updated/created不定义首发。[既有精确必要Source](../_sources/daily-20260407/v3-reopen-notes.md)（按ID定位最新有效段，原记录定位339）保留必要位置、评价合同与未证明范围。

- **2604.04759v1 / CIK State Poisoning**：[原文](https://arxiv.org/html/2604.04759v1) §3/4、AppendixA/D/E。OpenClaw四backbones/12手工impact每model88cases，Knowledge/Identity/Capability分别改memory/profile/executable；success仅attackrelevantaction且无confirmation，不等真实损失。Phase2部分用preloadedpoison独立测，不能与Phase1相乘偷算end-to-end；Skill主动加载能改善context-mediated但execpayload仍高，passive安装弱。仅一个platform、prompt级防御、无crossdimensionchain，原textalert不替代sandbox/signing。Ch72已有Skill描述vscode/activatedpath与derivedmemory不能授权。

已有覆盖：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)。Ch72 self-state与harness backdoor持有跨run load/trigger admission与write lineage，不乘成人为stage自然发生率。 非作者已实际读当前承载正文/完整相关局部，此决定不是主题相似或仅Review note匹配，不新增同义书稿。

### [GPU Acceleration of TFHE-Based High-Precision Nonlinear Layers for Encrypted LLM Inference](https://arxiv.org/pdf/2604.04783v1)

TFHE PBS精度/batch/转换→隐私执行边界非LLM实测；评分2+2+2=6，审阅深入完成。精确v1身份和公开日由本家族AB/DOI、官方first-announcement赋号规则、相邻批次/OAI及月列表组合支持Apr07自然日；单Submitted/Updated/created不定义首发。[既有精确必要Source](../_sources/daily-20260407/v3-reopen-notes.md)（按ID定位最新有效段，原记录定位343）保留必要位置、评价合同与未证明范围。

- **2604.04783v1 / TIGER**：[PDF](https://arxiv.org/pdf/2604.04783v1) pp3–4/7–9、TableIV–VII。WoP-PBS三keyspace加numerical补精度、radix4 fixedpoint32/34bits；offlineschedule只保留requiredpartialproducts，inter/intrainput PBS合批再按profile192–320拆batch，较大batch反而cache/memory瓶颈。RTX6000Ada48GB/XeonGold5320/4TBDRAM对16threadCPU-WoP与保留其他优化的GPU-FBT。GELU/Softmax/LayerNorm7.17/16.68/17.05×是operator对CPU；所谓endtoend15.54×是单GPT2block估算985.66s且98.5%nonlinear，不是完整autoregressiveLLM实测。MultiGPU只是discussion未运行，block转换CKKS↔TFHE需计成本。

已有覆盖：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)。Ch72隐私执行协议/非线性转换持有PBS精度/batch/转换合同；单block投影不等LLM/SLO。 非作者已实际读当前承载正文/完整相关局部，此决定不是主题相似或仅Review note匹配，不新增同义书稿。

### [Full-Duplex-Bench-v3: Benchmarking Tool Use for Full-Duplex Voice Agents Under Real-World Disfluency](https://arxiv.org/html/2604.04847v1)

duplex tool/content四时刻→首响应不代真实完成；评分2+2+2=6，审阅标准完成。精确v1身份和公开日由本家族AB/DOI、官方first-announcement赋号规则、相邻批次/OAI及月列表组合支持Apr07自然日；单Submitted/Updated/created不定义首发。[既有精确必要Source](../_sources/daily-20260407/v3-reopen-notes.md)（按ID定位最新有效段，原记录定位373）保留必要位置、评价合同与未证明范围。

- **2604.04847v1 / Speech Tool Benchmark**：[原文](https://arxiv.org/html/2604.04847v1) §3–4/Limitations。100人类utterances/12speakers含非母语、21self-correction与30s静默环境声；四mockAPI域且本地工具零latency、六LiveKit pipeline。toolF1、argument judge、allrequiredtask与turnlatency分开；跨cloud region/network仍混入“model latency”，不能作厂商模型纯因果排行。2+2+2=6标准审阅。

已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。Ch66 duplex合同分别持有响应时钟、内容、turn/interrupt与工具真实outcome；mock API不签生产SLO。 非作者已实际读当前承载正文/完整相关局部，此决定不是主题相似或仅Review note匹配，不新增同义书稿。

### [The Role of Generator Access in Autoregressive Post-Training](https://arxiv.org/html/2604.04855v1)

chosen-prefix control与logit observation分轴；评分2+2+2=6，审阅深入完成。精确v1身份和公开日由本家族AB/DOI、官方first-announcement赋号规则、相邻批次/OAI及月列表组合支持Apr07自然日；单Submitted/Updated/created不定义首发。[既有精确必要Source](../_sources/daily-20260407/v3-reopen-notes.md)（按ID定位最新有效段，原记录定位416）保留必要位置、评价合同与未证明范围。

- **04855 Generator Access**：§2.1–2.2/§3及Theorem3–4已补，纠正前段“环境reset”的过宽叙述：对象是固定prompt、有限词表与有限horizon的autoregressive prefix tree。No-reset回复可含已访问prefix的全部logits，仍受未到达稀有prefix的可达性屏障；chosen-prefix只沿已构造节点逐token延伸即可改变查询复杂度。隐藏路径分布以固定概率gap区分正确child，结论依赖条件采样oracle与构造族，非任意真实环境回滚；top1在另一分支构造中又可丢失识别所需信息。未把math-stripped抽取中的空公式当精确复杂度证明，报告只采用原文定理有明确条件支持的质性区别。2+2+2=6；必要理论Source的受限命题已核，本日具体访问权限差额进一步深入并整合。

本日整合：TRAIN-GRPO [Ch33](../../../../books/part-04-training-system/33-grpo.md)。当前owner/完整邻接逐字PRE后，已在原论证内实际写入受限差额，非作者实际正文、完整旧邻接与来源注POST通过；原分支与失配回退保留，不授实现/复现或生产保证。

采样次数之外，generator 的访问权限也决定探索支持。一个[受限 prefix-tree 分析](https://arxiv.org/html/2604.04855v1#S3)区分只从 root 继续完整 rollout，与可从已构造 prefix 条件续采；即使前者返回已访问 prefix 的 logits，也没有自动取得未到达稀有分支的采样控制。Observation richer 与 chosen-prefix control 是两个轴，不能把日志可见性等同环境可重置。理论只在固定prompt、有限词表/horizon与所给条件采样oracle/构造族下说明查询复杂度差异，不授任意LLM、Agent或物理环境回滚。Prefix缓存、分支验证、额外采样与状态访问均付费；无合法prefix控制或目标支持未验时，保留root rollout、原独立sample身份与可靠verifier，不由更多logits批准普遍高效探索。<!-- source-family:SF-2026-ARXIV-2604-04855 -->

### [Synthetic Sandbox for Training Machine Learning Engineering Agents](https://arxiv.org/pdf/2604.04872v1)

synthetic spec/evaluator先可执行→cheap训练非测试SLO；评分2+2+2=6，审阅标准完成。精确v1身份和公开日由本家族AB/DOI、官方first-announcement赋号规则、相邻批次/OAI及月列表组合支持Apr07自然日；单Submitted/Updated/created不定义首发。[既有精确必要Source](../_sources/daily-20260407/v3-reopen-notes.md)（按ID定位最新有效段，原记录定位375）保留必要位置、评价合同与未证明范围。

- **2604.04872v1 / SandMLE**：[PDF](https://arxiv.org/pdf/2604.04872v1) Method/evaluation。60seed task→848synthetic/64validation，生成小数据的hiddenrule/spec/evaluator并执行sanitycheck，不是把原benchmark缩小；format/execution/median/medals复合reward及GRPO80step。Qwen3-8/14/30B，MLElite22easy与MLEDojo62heldout，测试24GPUhour/turn30；短history溢出loop是失败边界。196.17→14.31s为训练synthetic相对seed执行成本，不是同测试工作负载端到端加速。2+2+2=6标准完成；Ch81“合成环境先生成契约再生成反馈”实际已有build/repair与verifierbias的完整分工，已有覆盖AGENT-WORKFLOW，不重复写新环境容器。

已有覆盖：AGENT-WORKFLOW [Ch81](../../../../books/part-07-agent/81-workflow.md)。Ch81 Synthetic Environment两段先验结构、语义、可行性和真实canary，持有合成环境可执行契约及generator/verifier共同偏差。 非作者已实际读当前承载正文/完整相关局部，此决定不是主题相似或仅Review note匹配，不新增同义书稿。

### [Rethinking Exploration in RLVR: From Entropy Regularization to Refinement via Bidirectional Entropy Modulation](https://arxiv.org/html/2604.04894v1)

binary group成功率两符号advantage modulation；评分2+1+2=5，审阅深入完成。精确v1身份和公开日由本家族AB/DOI、官方first-announcement赋号规则、相邻批次/OAI及月列表组合支持Apr07自然日；单Submitted/Updated/created不定义首发。[既有精确必要Source](../_sources/daily-20260407/v3-reopen-notes.md)（按ID定位最新有效段，原记录定位353）保留必要位置、评价合同与未证明范围。

- **2604.04894v1 / AsymGRPO**：[原文](https://arxiv.org/html/2604.04894v1) §2–4、Appendix C/E、Limitations。二值reward组准确率p分别调正负advantage `(1−p)/p` 与反比的指数，β=.5恢复GRPO、0为常数基线；βpos=.9/βneg=.4人为固定，不是学到逐token真值。理论省略完整PPOclip语义，positive/negative-only与反向曲线消融支持作者数学设置中的方向性，不证明任意reward都应同处理。4H100/verl/Qwen2.5-Math1.5B与Qwen3-4B nonthinking/MATH7500、G8；Qwen3global128/minibatch64/max4096/lr2e−6。主结果MATH500选择最佳checkpoint，Avg5/Avg10和temperature.4不同于曲线greedy，59.36vs56.50不是多seed误差界。Ch33已有token entropy-flow onpolicy条件，本例组成功率对正/负轨迹的非对称modulation已按当前正文具体差额进一步深入并整合。

本日整合：TRAIN-GRPO [Ch33](../../../../books/part-04-training-system/33-grpo.md)。当前owner/完整邻接逐字PRE后，已在原论证内实际写入受限差额，非作者实际正文、完整旧邻接与来源注POST通过；原分支与失配回退保留，不授实现/复现或生产保证。

二值 reward 下，组内成功比例也可以改变正负轨迹的相对幅度，而不是只在 ratio 上采用不同 clipping。一条[受限 advantage 分支](https://arxiv.org/html/2604.04894v1#S2)以本组成功率分别调制 positive 与 negative credit，用不同指数控制两侧；它改变的是更新信号配比，不把本组比例认证为题目真实难度，也不等于统一增加token entropy。固定指数与checkpoint选择属于recipe，简化理论未涵全部PPOclip，不能据此授任意reward/训练的熵方向或普遍稳定。Rollout、调参与独立质量/entropy/KL检查都计费；极端组、分布或质量失配时，保留原groupstd/对称advantage与已验符号相关clip，不由一个组的成功频率批准所有步骤正确或无偏更新。<!-- source-family:SF-2026-ARXIV-2604-04894 -->

### [A Frame is Worth One Token: Efficient Generative World Modeling with Delta Tokens](https://arxiv.org/pdf/2604.04913v1)

delta history与spatial anchor不同consumer→BoM非概率校准；评分2+2+3=7，审阅深入完成。精确v1身份和公开日由本家族AB/DOI、官方first-announcement赋号规则、相邻批次/OAI及月列表组合支持Apr07自然日；单Submitted/Updated/created不定义首发。[既有精确必要Source](../_sources/daily-20260407/v3-reopen-notes.md)（按ID定位最新有效段，原记录定位351）保留必要位置、评价合同与未证明范围。

- **2604.04913v1 / DeltaTok**：[原文](https://arxiv.org/pdf/2604.04913v1) §3.2–3.4、4.1–4.4、Appendix A–D。冻结DINOv3 ViT-B feature、previous feature-conditioned tokenizer将变化压成一个连续delta token；预测器只在delta历史上运行，但decoder恢复空间feature仍依赖上一feature map，black-frame首token是绝对anchor。BoM取K噪声proposal中最近GT，仅best分支训练，不保证样本概率/覆盖真实distribution（Appendix D明确承认）；delta重建和predictor两类误差可跨步累积。4frame context，~0.2s单步/~0.6s三步，20samples分别报告best与先平均feature的mean，不能只用oracle-best证明可靠预测。4Mvideo、512²/300Kiter主结果和256²/100K消融不同；DINO-world原代码/数据未公开所以为自行复现，跨architecture附录保留VSPW下降0.2。TableB predictor GFLOPs不含共享backbone/encoder及每样本decoder，不能把全系统缩成one-token成本。Hardware/precision/concurrency/SLO未披露。非action-conditioned、非physical safety。

本日整合：MULTIMODAL-WORLD-MODELS [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)。当前owner/完整邻接逐字PRE后，已在原论证内实际写入受限差额，非作者实际正文、完整旧邻接与来源注POST通过；原分支与失配回退保留，不授实现/复现或生产保证。

减少预测器读入的空间 tokens，也可以通过帧间 delta 表示，而不删除重建所需的空间状态。一条[受限无动作视频分支](https://arxiv.org/pdf/2604.04913v1)以冻结视觉 features 与前帧条件，把变化压到一个连续 token，预测器沿 delta history 提议下一变化；decoder仍消费上一 feature map，首个black-frame anchor提供绝对起点。One-token因此描述预测接口，不代表整个系统只留一个状态或拥有action-conditioned因果动力学；重建误差与预测误差均会随horizon累积。Best-of-many只让最近真值的proposal更新，不赋真实分布概率校准，oracle-best与mean预测须分账。Encoder、anchor驻留、每proposal decoder、训练与候选搜索仍付费；内容细节、horizon或控制消费不受支持时，保留dense latent dynamics、真实观测刷新与独立outcome验收，不由便宜变化坐标批准物理后果或安全规划。<!-- source-family:SF-2026-ARXIV-2604-04913 -->

### [TriAttention: Efficient Long Reasoning with Trigonometric KV Compression](https://arxiv.org/html/2604.04921v1)

preRoPE统计/模型校准身份/cadence→递归反退；评分2+2+2=6，审阅标准完成。精确v1身份和公开日由本家族AB/DOI、官方first-announcement赋号规则、相邻批次/OAI及月列表组合支持Apr07自然日；单Submitted/Updated/created不定义首发。[既有精确必要Source](../_sources/daily-20260407/v3-reopen-notes.md)（按ID定位最新有效段，原记录定位352）保留必要位置、评价合同与未证明范围。

- **2604.04921v1 / TriAttention**：[原文](https://arxiv.org/html/2604.04921v1) §3–5、Appendix A/E。Pre-RoPE Q-center及按频率query norm离线统计，trigonometric future-offset score与低concentration norm complement，周期128decoded tokens驱动prune；不同架构/calibration/revision不能直接共用统计。四reasoning模型，A10080 BF16/FA2，GPT-OSS使用H100/FA3；max32768、temperature.6/topP.95、AIME8samples/MATH500一次，defaultKV2048而DS-Llama/MATH500512。Table4 Qwen3-8B同AIME25 40.8%时2.5×吞吐绑定3072budget，不外推服务并发/SLO；depth18+recursive benchmark开始低于FullKV。Coding→reasoning校准是一个迁移对照，不证明任意域内在不变；dedicatedkernel未实现。

已有覆盖：INFER-KV-CACHE [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)。Ch45 Pre-RoPE Calibration与Workload-semantic Selection完整两路线已有model/calibration revision、update cadence及physical block/FullKV回退。 非作者已实际读当前承载正文/完整相关局部，此决定不是主题相似或仅Review note匹配，不新增同义书稿。

### [RoboPhD: Evolving Diverse Complex Agents Under Tight Evaluation Budgets](https://arxiv.org/html/2604.04347v1)

有限evaluation预算recipe比较→非通用autoresearch支配；评分2+1+2=5，审阅标准完成。精确v1身份和公开日由本家族AB/DOI、官方first-announcement赋号规则、相邻批次/OAI及月列表组合支持Apr07自然日；单Submitted/Updated/created不定义首发。[既有精确必要Source](../_sources/daily-20260407/v3-reopen-notes.md)（按ID定位最新有效段，原记录定位371）保留必要位置、评价合同与未证明范围。

- **2604.04347v1 / RoboPhD 补审**：§4.2–4.3/Table2–4实读。四任务1500evaluation预算，ARC/SQL/FinQA的solver/API限额不相同，KotH在ARC65.8→67.0胜，Autoresearch在无LLM的cloudscheduling胜；RoboPhD与KotH接近不是统计支配。将validation200减100增加探索在八配对均改善，但未证明validation应永远为0；DeepFocus四任务改善仍缺多seed可靠差值，底层工具/sampling批量不齐。2+1+2=5标准完成，受限比较仅报告，不把“首次”或代码行数当新长期架构。

仅报告：1500evaluation预算比较仍有工具/session/API与sampling混杂，KotH/Autoresearch局部反胜，不授统一Agent架构支配；证据保留，不新增长期算法或Books机制。

### [Decocted Experience Improves Test-Time Inference in LLM Agents](https://arxiv.org/pdf/2604.04373v1)

derived lesson/late construction→相关性非当前utility；评分2+2+2=6，审阅标准完成。精确v1身份和公开日由本家族AB/DOI、官方first-announcement赋号规则、相邻批次/OAI及月列表组合支持Apr07自然日；单Submitted/Updated/created不定义首发。[既有精确必要Source](../_sources/daily-20260407/v3-reopen-notes.md)（按ID定位最新有效段，原记录定位400）保留必要位置、评价合同与未证明范围。

- **04373 Experience Decoction**：HTML v1可读文本缺PDF v1的§3–5主体、把§3置为Concluding Remarks，故收束机制/关键反证采用[PDF v1](https://arxiv.org/pdf/2604.04373v1) pp4–8、HTML AppendixC.2仅辅佐实现。Flat→lesson→kmeans代表entry与concepttree，数学rawtrajectory稍好、WebShop/SWElesson更好；中间memory规模sweetspot而retrievalrelevance随总量单调，二者不能等同。Entropy→length上界依赖统一h>0熵率下界，r=.91并不证明truthquality、因果或上界tight；qualityproxy相关仅r=.2518，不能作通用confidence。经验只保留有至少一正反馈的问题，有survivorshipbias，未计总训练/整合成本。2+2+2=6标准完成；Ch77“从原始轨迹到派生策略”与“late construction”已承载原轨迹/派生lesson、噪声、不同任务与provenance/失效/回读，本次已有覆盖AGENT-MEMORY，不采用作者“低熵即好”的普适解释。

已有覆盖：AGENT-MEMORY [Ch77](../../../../books/part-07-agent/77-memory.md)。Ch77“从原始轨迹到派生策略”及“Query-conditioned Late Construction”持有lesson来源/适用条件与当前utility再验，不把历史成功或检索相关性当执行权。 非作者已实际读当前承载正文/完整相关局部，此决定不是主题相似或仅Review note匹配，不新增同义书稿。

### [Don't Blink: Evidence Collapse during Multimodal Reasoning](https://arxiv.org/html/2604.04207v1)

任务条件视觉sensor/entropy迁移反退→无truth权；评分2+1+2=5，审阅深入完成。精确v1身份和公开日由本家族AB/DOI、官方first-announcement赋号规则、相邻批次/OAI及月列表组合支持Apr07自然日；单Submitted/Updated/created不定义首发。[既有精确必要Source](../_sources/daily-20260407/v3-reopen-notes.md)（按ID定位最新有效段，原记录定位414）保留必要位置、评价合同与未证明范围。

- **04207 Visual entropy**：§5.4–5.5/§6及AppendixH.2已补。三模型×三数据集、18方向迁移，视觉engagement与长度耦合但非相同信号；加入视觉特征部分迁移明显下降，不能把九格attention衰减转成普遍hallucination因果。底5%vision veto后重新放宽entropy阈值以恢复coverage，不能把拒绝更多当同coverage收益。任务需要持续视觉参照时才可能增益，任务识别在部署前尚待解决；2B–8B/300items每域、attention相关性与小角落样本限制。2+1+2=5；必要Source有效，本日对采用的条件sensor命题深化核验，本次由Ch66条件化监测/校准具体承载，而非全局视觉熵阈值。

已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。Ch66 attention sensor、length deconfounding与模型/任务slice校准持有受限风险信号无truth权；不称本篇entropy训练recipe已在书中逐机制实现。 非作者已实际读当前承载正文/完整相关局部，此决定不是主题相似或仅Review note匹配，不新增同义书稿。


### [REAM: Merging Improves Pruning of Experts in LLMs](https://arxiv.org/html/2604.04356v1)

permutation合并artifact＋逐层校准→非runtime裁route；评分2+2+2=6，审阅深入完成。精确v1身份和公开日由本家族AB/DOI、官方first-announcement赋号规则、相邻批次/OAI及月列表组合支持Apr07自然日；单Submitted/Updated/created不定义首发。[既有精确必要Source](../_sources/daily-20260407/v3-reopen-notes.md)（按ID定位最新有效段，原记录定位407）保留必要位置、评价合同与未证明范围。

- **04356 REAM**：§4实际子段aggregatedsimilarity/pseudopruning/permutation/sequential及§5Setup/Ablation已补。按gateweightedactivation+weight共同Hungarianalignment，保护centroids再吸收低saliency、很多singleton；前层合并后重算后层calibration避免stalestats，1→1.5hour为Qwen30B作者一次性实测成本。10mixture无finetune并有MC/GEN前沿、remove各部件对照；routerfrequency不同importance，OOD稀有expert与calibration失配受限。2+2+2=6；必要Source有效，本日合并artifact/顺序校准具体差额进一步深入并整合。

本日整合：MODEL-MOE [Ch21](../../../../books/part-02-model/21-moe.md)。当前owner/完整邻接逐字PRE后，已在原论证内实际写入受限差额，非作者实际正文、完整旧邻接与来源注POST通过；原分支与失配回退保留，不授实现/复现或生产保证。

压缩 artifact 还可以合并 expert 参数，而不只是减少其rank或裁 runtime routes。一条[受限 merge 分支](https://arxiv.org/html/2604.04356v1#S4)以routing加权的activation与weights共同匹配神经元permutation，保护clustercentroids后吸收较低saliency的experts；前层改变后，再重算后层calibration，避免把旧统计当当前输入。被合并expert的参数信息不等原function无损保留，routerfrequency也不认证稀有任务重要度；calibration mix会改变MC/生成前沿，许多singleton保留了不能安全合并的分支。匹配、逐层重校准、重建artifact与完整任务回归均付费，不代表runtime自动少算或最优全模型压缩。长尾、对齐或质量失配时，保留独立experts、较温和rank/precision压缩与原router，不让平均activation批准删除能力。<!-- source-family:SF-2026-ARXIV-2604-04356 -->

### [DP-OPD: Differentially Private On-Policy Distillation for Language Models](https://arxiv.org/html/2604.04461v1)

student-release DP不保护teacher/API所见prompt；评分2+2+2=6，审阅深入完成。精确v1身份和公开日由本家族AB/DOI、官方first-announcement赋号规则、相邻批次/OAI及月列表组合支持Apr07自然日；单Submitted/Updated/created不定义首发。[既有精确必要Source](../_sources/daily-20260407/v3-reopen-notes.md)（按ID定位最新有效段，原记录定位408）保留必要位置、评价合同与未证明范围。

- **04461 DP-OPD**：§3.4及WhatConsumesPrivacy/Algorithm1/§4.3/4.9已补，冻结teacher只作为每example内部loss，DP会计保护唯一releasedstudent；publicteacher/rollout查询若外泄私有prompt不受studentDP保证，controlcodes敏感性亦未解决。Onpolicy交互以现teacher固定与每步DPcompatibleclip/noise为前提，不推出任意APIpipeline guarantee。2+2+2=6安全深入完成；Ch72实际DP发布/私有推理正文已对读，具体已有覆盖。

已有覆盖：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)。Ch72 DP被保护/发布对象与private prediction分账、明文可见边界已承载student发布不保护teacher/API prompt。 非作者已实际读当前承载正文/完整相关局部，此决定不是主题相似或仅Review note匹配，不新增同义书稿。

### [Beyond Fixed Tests: Repository-Level Issue Resolution as Coevolution of Code and Behavioral Constraints](https://arxiv.org/html/2604.04580v1)

code/test共同fitness→独立contract/hidden oracle；评分2+2+2=6，审阅深入完成。精确v1身份和公开日由本家族AB/DOI、官方first-announcement赋号规则、相邻批次/OAI及月列表组合支持Apr07自然日；单Submitted/Updated/created不定义首发。[既有精确必要Source](../_sources/daily-20260407/v3-reopen-notes.md)（按ID定位最新有效段，原记录定位415）保留必要位置、评价合同与未证明范围。

- **04580 Code–test co-evolution**：§3.2–3.3/§4.1–4.3/§5.2及limitations已补。DeepSeek-V3-0324、population10/最多5代，SWE-benchLite300/SWT276，隐藏测试/goldenpatch是评价oracle而非搜索时可用真值；多数baseline是旧论文/leaderboard，不是同prompt/预算重跑。去TestAgent在三代39.33→33.33，有受限component证据，但跨模型主表不证明算法普遍优越；每实例成本1.11美元与其他模型成本不能合为机制因果。共进化的consensus/elite只保内部fitness，不能防code/test同错；简单bugs可增加成本。2+2+2=6；反证要求进一步深入，Ch81 implementation/checker分权已实际对读确认具体已有覆盖。

已有覆盖：AGENT-WORKFLOW [Ch81](../../../../books/part-07-agent/81-workflow.md)。Ch81先编译contract/Evaluator-driven search已分candidate/test共同错误、独立holdout/权威与谱系，Ch66 budget surface分width/depth。 非作者已实际读当前承载正文/完整相关局部，此决定不是主题相似或仅Review note匹配，不新增同义书稿。

### [From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism](https://arxiv.org/html/2604.04648v1)

frozen RM-feature OOD penalty→受限pool soft-risk选择；评分2+2+2=6，审阅标准完成。精确v1身份和公开日由本家族AB/DOI、官方first-announcement赋号规则、相邻批次/OAI及月列表组合支持Apr07自然日；单Submitted/Updated/created不定义首发。[既有精确必要Source](../_sources/daily-20260407/v3-reopen-notes.md)（按ID定位最新有效段，原记录定位392）保留必要位置、评价合同与未证明范围。

- **2604.04648v1 / Caution**：[原文](https://arxiv.org/html/2604.04648v1) §2–3、AppendixC。冻结RMfeature作为target而非随机RNDtarget，典型baseoutput上训练predictor，predictionerror惩罚BoN的OOD候选。理论线性reward与适当网络/假设只是proof-of-concept，不是任意RM的概率校准；GSMtrain→MATH/BBH外域，pessimism-only可胜RM+penalty、3bootstrap不是3独立training。2+2+2=6标准完成；Ch31受限pool soft-risk选择及Ch66独立测量已实际对读确认覆盖，不声称完整prediction-error训练recipe已写书。

已有覆盖：TRAIN-RLHF [Ch31](../../../../books/part-04-training-system/31-rlhf.md)。Ch31 frozen realized-pool soft-risk selector与Ch66 representation/detector/校准分责持有受限选择风险；不声称frozen RM prediction-error训练recipe已逐机制实现，更不授概率真值。 非作者已实际读当前承载正文/完整相关局部，此决定不是主题相似或仅Review note匹配，不新增同义书稿。

### [Cog-DRIFT: Exploration on Adaptively Reformulated Instances Enables Learning from Hard Reasoning Problems](https://arxiv.org/html/2604.04767v1)

MC/cloze/open课程改变可达reward→原任务迁移另验；评分2+1+2=5，审阅深入完成。精确v1身份和公开日由本家族AB/DOI、官方first-announcement赋号规则、相邻批次/OAI及月列表组合支持Apr07自然日；单Submitted/Updated/created不定义首发。[既有精确必要Source](../_sources/daily-20260407/v3-reopen-notes.md)（按ID定位最新有效段，原记录定位393）保留必要位置、评价合同与未证明范围。

- **2604.04767v1 / CogDRIFT**：[原文](https://arxiv.org/html/2604.04767v1) Method/Table1。Pass64=0的8.9K仍含unsolvable，GPT5.4三samplemajority与gold一致筛出958，不能沿摘要说完全nostrongteacher。MC4→MC10→cloze→open改变提示特权与词表，τ.5逐题promotion，pass64零不证明零成功概率/凭空新knowledge。Qwen3-4B2507/Llama3.2-3、六bench中AIME25 Qwen41.71→40.28退步。2+1+2=5；本日因局部可达reward支持集的具体差额进一步深入，Ch33已整合该窄分支，不从挑选效应推广泛突破。

本日整合：TRAIN-GRPO [Ch33](../../../../books/part-04-training-system/33-grpo.md)。当前owner/完整邻接逐字PRE后，已在原论证内实际写入受限差额，非作者实际正文、完整旧邻接与来源注POST通过；原分支与失配回退保留，不授实现/复现或生产保证。

困难题在有限root采样中未出现reward时，课程还可以改变同一答案的可作答形式，而不只给原prompt更多tokens。一个[受限任务改写分支](https://arxiv.org/html/2604.04767v1)从选择题逐步走向更多选项、填空及原开放题，按当前成功率推进；它先把可达reward支持换到较易的surrogate，再单独验原任务迁移。Pass64=0不是成功概率零，更不证明凭空生成原模型没有的知识；强teacher筛选/gold一致和选项信息是额外特权，不能称无teacher或同数据预算。改写/筛选、阶段rollout、原形式评价都付费，部分测试仍反退。答案不等价、teacher/阶段信号失配或开放任务质量无益时，保留原任务、可验示教与更保守curriculum，不由surrogate高成功率批准部署能力。<!-- source-family:SF-2026-ARXIV-2604-04767 -->

### [How Alignment Routes: Localizing, Scaling, and Controlling Policy Circuits in Language Models](https://arxiv.org/html/2604.04385v1)

低DLA gate可必要→多位置因果控制不由读出贡献认证；评分2+1+3=6，审阅深入完成。精确v1身份和公开日由本家族AB/DOI、官方first-announcement赋号规则、相邻批次/OAI及月列表组合支持Apr07自然日；单Submitted/Updated/created不定义首发。[既有精确必要Source](../_sources/daily-20260407/v3-reopen-notes.md)（按ID定位最新有效段，原记录定位403）保留必要位置、评价合同与未证明范围。

- **04385 Trigger–Carrier**：已实际对读Ch14“可解码不等于单点拥有因果控制权”的probe→single/multiposition→causaltracing/端到端回退；6分按必要干预反证深化，pattern/knockout仅为受限诊断证据，既有正文已覆盖读出/必要/充分/多点控制层级。本次已有覆盖MODEL-SELF-ATTENTION，不引入另一家族或重复因果owner。

已有覆盖：MODEL-SELF-ATTENTION [Ch14](../../../../books/part-02-model/14-self-attention.md)。Ch14 probe与多位置transplant/causal tracing持有可读、必要/充分与分布式carrier边界，不以DLA小断言无控制。 非作者已实际读当前承载正文/完整相关局部，此决定不是主题相似或仅Review note匹配，不新增同义书稿。

### [Justified or Just Convincing? Error Verifiability as a Dimension of LLM Quality](https://arxiv.org/html/2604.04418v1)

AO verdict×真实correctness四cell→verifiability非accuracy；评分2+2+3=7，审阅深入完成。精确v1身份和公开日由本家族AB/DOI、官方first-announcement赋号规则、相邻批次/OAI及月列表组合支持Apr07自然日；单Submitted/Updated/created不定义首发。[既有精确必要Source](../_sources/daily-20260407/v3-reopen-notes.md)（按ID定位最新有效段，原记录定位360）保留必要位置、评价合同与未证明范围。

- **2604.04418v1 / Error Verifiability**：[原文](https://arxiv.org/html/2604.04418v1) §3–8、Limitations、Appendix K。AnswerOnly基线×答案正确性形成TP/TN/FP/FN四cell，Answer+Justification正确核验率均匀聚合，避免90%correct分布下blindaccept伪高。AO-CoT/directAJ两个protocol经有限math人类样本κ.481/.501选定，仍不是完整人类等价。Tulu3.1/OLMo2后训练与跨modelaccuracy不保证errorverifiability，数学反省rephrase在factualQA不迁移；固定finalanswer只改justification，不可把说服度当truth。

本日整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。当前owner/完整邻接逐字PRE后，已在原论证内实际写入受限差额，非作者实际正文、完整旧邻接与来源注POST通过；原分支与失配回退保留，不授实现/复现或生产保证。

解释是否帮助核验错误，也要与答案本身有多正确、rater原先会不会判断分开。一个[受限 error-verifiability 协议](https://arxiv.org/html/2604.04418v1#S3)先取得AnswerOnly verdict，再按其判断与答案真值交叉形成四cell，检查加入justification后的核验表现并均匀聚合；否则正确答案占多数时，blindaccept也会得到高总体accuracy。这里测的是发现答案正误，而不是解释的说服度或模型accuracy升级，rater/justification protocol与四个条件分母必须一起保留。有限数学人类对照不授全任务人类等价，跨域解释策略也会失效；配对评分、人工truth与模型生成均有成本。Cell支持不足、rater或原始truth不可靠时，保留AnswerOnly、逐cell不确定性和独立原证核查，不由流畅解释批准真实正确。<!-- source-family:SF-2026-ARXIV-2604-04418 -->

### [MUXQ: Mixed-to-Uniform Precision MatriX Quantization via Low-Rank Outlier Decomposition](https://arxiv.org/html/2604.04701v1)

integer body/aux重组替FP旁路→fakequant非NPUkernel；评分2+1+2=5，审阅深入完成。精确v1身份和公开日由本家族AB/DOI、官方first-announcement赋号规则、相邻批次/OAI及月列表组合支持Apr07自然日；单Submitted/Updated/created不定义首发。[既有精确必要Source](../_sources/daily-20260407/v3-reopen-notes.md)（按ID定位最新有效段，原记录定位506）保留必要位置、评价合同与未证明范围。

- **04701 MUXQ**：[exact-v1](https://arxiv.org/html/2604.04701v1) §3.2–3.3、§4/ Tables1–2。Body将outlier缩小，Aux保存选中列，输出按`Ybody+(2^exp−1)Yaux`重构；这是integer-compatible的辅助乘法/重组，不是免费误差消除，也不是学得任意rank的SVD。exp=1可两路相加，exp=2有额外重组；大于6的outlier规则继承LLM.int8。GPT2 .1/.3/.7B、WikiText2、RTX3080/12GB、absmax、5–8bit activation及4–8bitweight；§4.3明确fake quantization，不含真正INT kernel、latency/power/NPU实测。6bit时MUXQ质量可明显弱于FP16 outlier bypass，不能说普遍优于LLM.int8。

本日整合：INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)。当前owner/完整邻接逐字PRE后，已在原论证内实际写入受限差额，非作者实际正文、完整旧邻接与来源注POST通过；原分支与失配回退保留，不授实现/复现或生产保证。

异常通道也可以用额外整数分支重构，而不必永久保高精度旁路。一条[受限 outlier 表示](https://arxiv.org/html/2604.04701v1#S3)将选中列拆为缩小后的body与aux，按Y_body+(2^exp−1)Y_aux重组；统一整数精度没有取消第二次乘法、列选择、scale和结果重组。Exp=1与exp=2支付的组合工作不同，outlier规则与calibration人口仍须绑定artifact。原文只有fakequant质量实验，没有实际packedINT/NPU kernel或latency；低位切片可弱于高精度outlierbypass，不把整数兼容性认证为已加速。拆分、校准与真实backend全费不合算或质量失配时，保留更高精度/混合旁路、原矩阵与已验整数图，不由数值重组公式签发全NPU部署。<!-- source-family:SF-2026-ARXIV-2604-04701 -->

### [Don't Waste Bits! Adaptive KV-Cache Quantization for Lightweight On-Device LLMs](https://arxiv.org/html/2604.04722v1)

自适应KV controller时间单位/packed测量中心冲突；评分2+1+2=5，审阅争议。精确v1身份和公开日由本家族AB/DOI、官方first-announcement赋号规则、相邻批次/OAI及月列表组合支持Apr07自然日；单Submitted/Updated/created不定义首发。[既有精确必要Source](../_sources/daily-20260407/v3-reopen-notes.md)（按ID定位最新有效段，原记录定位507）保留必要位置、评价合同与未证明范围。

- **04722 Adaptive KV**：[exact-v1](https://arxiv.org/html/2604.04722v1) §3.4–3.8/§4。四维feature输入128隐藏宽度三层MLP，以bitlabel交叉熵及class-wise latency/quality期望训练，append前选2/4/8/16bit；80/20是token样本划分，不能自动证明跨context泛化。RTX4090/24GB、SmolLM135M/360M/1.7B、HellaSwag/OBQA/ARC-C；§4.1写ms/token，Table3写s/token，数值单位无法据现文统一，且未披露长度/batch/concurrency与packed异精度kernel/controller端到端分账。Table4使用其他模型文献分数，不能把换backbone优势归给该controller。理论“Pareto/导数更大”式不构成可验证的普遍收益证明。

争议/暂缓：INFER-KV-CACHE [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)。中心矛盾双方均保留，不作正面Evidence或Books，具体缺少的原始澄清及定点重开见§5；不是普通未读，也不以降分或删反侧关闭。

### [Preservation Is Not Enough for Width Growth: Regime-Sensitive Selection of Dense LM Warm Starts](https://arxiv.org/html/2604.04281v1)

width selector horizon/regime可翻转→function保留非轨迹；评分2+1+2=5，审阅深入完成。精确v1身份和公开日由本家族AB/DOI、官方first-announcement赋号规则、相邻批次/OAI及月列表组合支持Apr07自然日；单Submitted/Updated/created不定义首发。[既有精确必要Source](../_sources/daily-20260407/v3-reopen-notes.md)（按ID定位最新有效段，原记录定位513）保留必要位置、评价合同与未证明范围。

- **04281 Width Growth**：[exact-v1](https://arxiv.org/html/2604.04281v1) §3–6/9。候选是weight+AdamW moments+scheduler的完整状态；clone扩宽保持函数，reference-slice扩宽亦可保持却避免对称clone。TinyStories decoder6层256→512、8.46M parent、context256、BPE8192、AdamW lr3e-4、有效batch48/12288tokens；seed0全池与seed1缩小池。16step两regime均exactcopy较好；128step deterministic reference-slice较好，stochastic则exactcopy继续较好。后者将shuffled order与新增dropout=.1捆绑，不能归因某一种噪声；没有重复continuation/CIs或前沿规模证明。零步KL/loss可打平不同后续轨迹，16step AUC错过全部deterministic后发翻转；escape并非通用selector。

本日整合：TRAIN-PRETRAINING [Ch28](../../../../books/part-04-training-system/28-pretraining.md)。当前owner/完整邻接逐字PRE后，已在原论证内实际写入受限差额，非作者实际正文、完整旧邻接与来源注POST通过；原分支与失配回退保留，不授实现/复现或生产保证。

扩容候选的选择还要绑定后续训练regime和selector horizon。一个[受限dense-LM warm-start反例](https://arxiv.org/html/2604.04281v1#S3)把weights、AdamW moments及scheduler共同作为候选状态：clone与asymmetric reference-slice都可保持初始function，却在较长deterministic与stochastic continuation中改变胜者；短16step打分还会漏掉较晚翻转。Stochastic设置同时改shuffled order/dropout，不能识别唯一噪声原因，也不据小规模单池证明所有扩宽都应reset、rewarm或escape。候选构造、两种续训、选择预算与迁移回归都付费；horizon/regime不可信或收益不足时，保留旧checkpoint、已验clone/controlledrewarm及较长matched continuation，不由零步KL或初期loss批准新容量长期更好。<!-- source-family:SF-2026-ARXIV-2604-04281 -->

### [Hallucination Basins: A Dynamic Framework for Understanding and Controlling LLM Hallucinations](https://arxiv.org/html/2604.04743v1)

conditioned failure probe/steering proxy→独立outcome；评分2+1+2=5，审阅深入完成。精确v1身份和公开日由本家族AB/DOI、官方first-announcement赋号规则、相邻批次/OAI及月列表组合支持Apr07自然日；单Submitted/Updated/created不定义首发。[既有精确必要Source](../_sources/daily-20260407/v3-reopen-notes.md)（按ID定位最新有效段，原记录定位514）保留必要位置、评价合同与未证明范围。

- **04743 Hallucination Basins**：[exact-v1](https://arxiv.org/html/2604.04743v1) §5.1–5.5/§8、AppendixC/E/F。uninformative prompts构造reference state，centroid/covariance按70/30训练切片冻结、三random splits与bootstrap只评受限AUROC；truth标签来自数据集，不把latent风险当真值。任务几何差别和模型差别明显，summary/misconception并非统一可分basin；理论依赖attention均匀/局部Jacobian收缩等假设，未证明真实Transformer全局吸引子。§8.3 steering会改变下游状态，但报告的P(hall)是trained classifier输出，不能直接当生成答案真实错误率改善。RTX4060 laptop8GB、所列1–8B模型/短任务，部分过滤后有效样本少；长上下文/大模型/closedAPI不可外推。

已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。Ch66 failure direction分label读出、独立correction/outcome与control survival；steered probe不是真实错误率。 非作者已实际读当前承载正文/完整相关局部，此决定不是主题相似或仅Review note匹配，不新增同义书稿。

### [Beyond the Global Scores: Fine-Grained Token Grounding as a Robust Detector of LVLM Hallucinations](https://arxiv.org/html/2604.04863v1)

ADS空间compactness与CGC语义alignment双轴；评分2+1+2=5，审阅深入完成。精确v1身份和公开日由本家族AB/DOI、官方first-announcement赋号规则、相邻批次/OAI及月列表组合支持Apr07自然日；单Submitted/Updated/created不定义首发。[既有精确必要Source](../_sources/daily-20260407/v3-reopen-notes.md)（按ID定位最新有效段，原记录定位527）保留必要位置、评价合同与未证明范围。

- **04863 Token Grounding**：[exact-v1](https://arxiv.org/html/2604.04863v1) §3.2–3.3/4.1–4.3、Appendix6/8/11。ADS从top-patches做8-connected blob及background entropy；CGC另用token/patch top-k cosine alignment，两者并非同一特征：紧凑attention仍可语义错配，分散attention也可能匹配对象。Layer向量送XGB/RF/MLP监督分类，不获得真值权威；中层最佳的定性叙述也不能代替Table6中all-layer更好的具体配置。4000 COCO2014 images按image90/10、GPT4o+caption/object label；POPE hallucination217/3556约6.1%，F1=.41/AUC=.75远非可靠拒绝所有假对象。三个7/8B模型、hyperparameter validation、top-percent敏感和融合消融支持互补信号；Table2/4主结果口径不同不合并，作者“所有metrics/models最佳”与局部格不完全一致。GPU/precision/length/batch/concurrency/SLO/在线feature成本未披露。

本日整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。当前owner/完整邻接逐字PRE后，已在原论证内实际写入受限差额，非作者实际正文、完整旧邻接与来源注POST通过；原分支与失配回退保留，不授实现/复现或生产保证。

内部视觉诊断也不能把attention集中与语义grounding合成一个信号。一条[受限token sensor](https://arxiv.org/html/2604.04863v1#S3)用top-patch连通blob/背景entropy描述空间compactness，另用token–patchfeature相似性描述语义对应；紧凑注意仍可对错对象，分散注意也可能获得支持，两轴再由监督classifier提出风险。它不恢复视觉事实、赋因果或自动拒绝权；label/judge、image split、layer与top-percent选择共同定义校准人口。有限低hallucination人口中的F1/AUC离可靠全拒绝仍远，整体宣传与局部表格不一致不拼最大值。Feature提取、两轴分类、标签与独立行为检查都计费；层位、域或实际quality失配时，保留原图证据、单轴/既有sensor及独立grounding/outcome核验，不由compactness或相似度签truth。<!-- source-family:SF-2026-ARXIV-2604-04863 -->

### [Agentic Code Optimization via Compiler-LLM Cooperation](https://arxiv.org/html/2604.04238v1)

compiler finite oracle/零cost calls→contract与budget shape；评分2+1+2=5，审阅标准完成。精确v1身份和公开日由本家族AB/DOI、官方first-announcement赋号规则、相邻批次/OAI及月列表组合支持Apr07自然日；单Submitted/Updated/created不定义首发。[既有精确必要Source](../_sources/daily-20260407/v3-reopen-notes.md)（按ID定位最新有效段，原记录定位534）保留必要位置、评价合同与未证明范围。

- **04238 ACCLAIM**：[exact-v1](https://arxiv.org/html/2604.04238v1) §3.3–3.5、4.1–4.2/4.5、5.2–5.3。LLM层级agent提出程序/IR/assembly候选，编译器和隐藏reference测试拥有本组correctness筛选；测试是LLM生成有限输入并与原程序输出对比，不是语义等价证明，translation validation仍是未来工作。预算对agent调用计unit cost、compiler调用按0处理，不能当真实wall-clock成本；同预算探索宽度beta和feedback迭代alpha会改变结果，受测100程序中4×1优于2×2和1×4，不支持所有任务默认多迭代更好。CodeNet先过滤编译/测试生成/有效case数与优化空间后剩564题、10samples；clang18.1.3-O3、96-core Xeon8275CL/1TB、Claude3.7SonnetBedrock、单题1h上限，不外推LLM-serving或全程序正确性。反复执行artifact才可能摊销优化成本，一次性程序仍可不值得搜索。

已有覆盖：AGENT-WORKFLOW [Ch81](../../../../books/part-07-agent/81-workflow.md)。Ch81可执行contract/Evaluator-driven search持有finite oracle/heldout与晋级责任，Ch66“Search排名必须覆盖预算形状”分width/depth/frontier与真实成本。 非作者已实际读当前承载正文/完整相关局部，此决定不是主题相似或仅Review note匹配，不新增同义书稿。

### [LOCALUT: Harnessing Capacity-Computation Tradeoffs for LUT-Based Inference in DRAM-PIM](https://arxiv.org/html/2604.04523v1)

LUT容量/索引/host转换/分层reuse联合费用；评分2+1+2=5，审阅深入完成。精确v1身份和公开日由本家族AB/DOI、官方first-announcement赋号规则、相邻批次/OAI及月列表组合支持Apr07自然日；单Submitted/Updated/created不定义首发。[既有精确必要Source](../_sources/daily-20260407/v3-reopen-notes.md)（按ID定位最新有效段，原记录定位535）保留必要位置、评价合同与未证明范围。

- **04523 LoCaLUT**：[exact-v1](https://arxiv.org/html/2604.04523v1) III-A、IV-A–D、V-A/B、VI-A/G/I/J和VII-B。operation-packed LUT用指数增长的表容量代算术，联合排序activation与weight保inner-product；host产生排序activation/permutation，PIM用额外reordering LUT减少unpack/repack，再保持activation选择、只把相关canonical/reordering列slice搬到SRAM跨weight rows复用。它不是只把整数matmul放近内存：pack degree必须联合LUT容量、slice搬运与重复lookup选，复用不足时buffer-resident小表仍合理。IV-D一阶模型明确仅计LUT路径，VI-I在W2A2会因未计input load预测偏差；VI-G residual index计算比LUT access更大，reordering访问仍占kernel6.9%，省算术不等于省索引。32UPMEMranks×64banks、2048PE、每PE64MBDRAM/64KBSRAM、SDK2023.2.0/XeonGold5215；BERTbase/OPT125M/ViT不同W1A3/W1A4/W2A2/W4A4及max128任务，host仍做非矩阵与聚合，半bank/buffer给LUT造成multi-job容量限制。LTC是适配UPMEM实现，不是与原硬件公平横比；高bitwidth/低reuse可能不如算术，bs32–512与prefill/decode实验未给生产concurrency/SLO。

本日整合：INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)。当前owner/完整邻接逐字PRE后，已在原论证内实际写入受限差额，非作者实际正文、完整旧邻接与来源注POST通过；原分支与失配回退保留，不授实现/复现或生产保证。

固定低位线性计算还可把算术换成离线表，但表容量、索引和搬运会成为新的主成本。一条[受限DRAM-PIM路径](https://arxiv.org/html/2604.04523v1#S4)将多operation合并到LUT，host生成排序activation及permutation，PIM用reordering LUT保持weight与输入配对，再按当前activation选择canonical/reordering列slice，搬到小SRAM跨weight rows复用。Packdegree会使表容量指数增加，不能只按lookup次数选；host转换、输入load、residualindex和buffer占用都须计入executionplan，LUT-only模型也会漏真正瓶颈。所测UPMEM与低位模型合同不授所有硬件或高bitwidth优势，适配baseline不是与原设备公平直比。Reuse、容量、格式或净收益失配时，保留较小buffer-resident表、普通算术/量化kernel与原placement，不由省乘法批准端到端低延迟。<!-- source-family:SF-2026-ARXIV-2604-04523 -->


## 5. 缺口与下一步

本窗没有未处理的可执行工作，独立六部分DAY已实际通过，来源扫描、准入/必要Source、Books裁决与实际写后均达到各自安全终态，所有窄锁已释放。以下均为具名终态保留项，不用于正面证据、Books或无遗漏断言，也不授性能/安全保证；各项定点重开条件如下，不是未读队列。

五个必要历史子入口按实际有限停止范围隔离。缺少原始历史身份/公开日期会影响覆盖与落窗判断，故不能采用当前目录零命中。可接受替代是覆盖Apr07的官方原始历史索引、可核公告，或带原始日期/时区的当时已公开正文；材料到达只重开该子入口/受影响事件，不扩扫机构全年：

- [OpenAI Research](https://openai.com/research/)：RSS1287项Apr06→Apr08已核，但不能代Research；Research仅current/HTTP403保护页，没有Apr07可靠历史分页。
- [Google Publications](https://research.google/pubs/)：April Blog/DeepMind已有有限跨日停点；当前year/venue或selected pubs不说明Apr07首发，缺原始日级发布目录。
- [Kimi Blog](https://platform.kimi.com/blog)：当前可读列表只到2025Nov，无法覆盖2026Apr07；需官方当日历史条目或原始发布记录，release复用不补此缺口。
- [MiMo Blog](https://mimo.xiaomi.com/)：Paper8项已跨日检查，Blog15项无日期，必要路由未恢复首发；需对应原始日期/当时正文，不以无日期当前卡片判零。
- [MiniMax Agent Tech Blog](https://agent.minimax.io/docs/techblog)：本轮3条Sep/Oct目录没有Apr历史公开段；旧唯一May13标签不授Apr07覆盖，需要当日原始目录/公开时间。

Meta三页近期Publications及DeepSeek官方完整Research31/News16列表已有限恢复，不再沿旧HTTP500/UI展开待办把整个来源称受阻；它们仍不支持全站召回保证。

新增日期异常：[LPC-SM 2604.03263v1](https://arxiv.org/abs/2604.03263v1)和[OASES 2604.03675v1](https://arxiv.org/abs/2604.03675v1)的本轮v1 Updated分别为Apr11/May08，与Apr07批次组合有具体异常。它们不列93分母、不评分、不据旧Source/April ID写Books；缺的是本家族Apr07真实首次公开资格，可接受官方早期公告/正文可用记录或可核组合证据。只重开各家族日期归属及受影响采用，不能把孤Updated改名公开日。

新增中心争议两项保留在93分母内但不支持正面结论或Books：

- [V-Reflection 2604.03307v1](https://arxiv.org/html/2604.03307v1)：main§3.4/4.4/T3e称BCM/DAC推理inactive，A.2称inference DAC动态填latent slots，L1/MSE另冲突。需作者精确v1澄清slot producer、完整消费图及额外成本（可接受勘误或同版本可检查实现/图）；只重开该推理接口与MULTIMODAL-REPRESENTATION采用，不以成功图/后版静默补拼。
- [Adaptive KV 2604.04722v1](https://arxiv.org/html/2604.04722v1)：§4.1 ms/token与T3 s/token、packed/controller/bitlabel测量身份中心冲突。需原始配置/packed格式和bit解释、控制器时序、统一单位的原测量或正式勘误；只重开INFER-KV-CACHE该性能与机制采用，不能用未核数字或可选代码无限追查。

原05217理论争议仍按§4隔离：作者勘误/完整证明需明确期望分解的独立性与非抵消、chord/geodesic及真实优化目标，已有具体反例不由新增benchmark消除；仅重开该理论与MODEL-POSITION-ENCODING。下列原日期保留项仍有效，不默认被本次补窗恢复。

原32有效层的arXiv有界恢复已实际查看06169 abs/v1及官方advanced search原说明：abs只给Submitted，advanced的Announcement date只支持年月精度；historical cs.CL月列表原审阅429，recent只列当前9月，不借它伪证4月日公告。连续ID、官方announcement规则与DOI/OAI边界组成批次推断而非单篇精确时点。原32表内保留项另经逐家族v1可用上界核对，由组合证据支持08:00～09:00的有限推断；不把Updated字段单独称首发。以下跨截点项未取得早于09:00的上界，因此从确定候选表移除并保留必要证据。

跨截点日期隔离：原审阅实际取得官方DOI版本元数据，`v1 Updated`为06111 `2026-04-08T01:10:59Z`、06163 `01:13:32Z`、06129 `01:12:04Z`、06036 `01:06:37Z`、06132 `01:12:13Z`。该字段不是公告时点，也不证明一定晚发；原审阅未取得，当前有效层亦未恢复它们早于北京时间09:00的公开可用上界，不能沿用全批08:00～09:00。5项不列§3、不评分、不据它们写Books，已读机制证据保留于[日期隔离笔记](../_sources/daily-20260408/V3_DATE_ISOLATION.md)；这些单篇原笔记已从§4移入隔离笔记，旧评分/拟处置不继承为本窗判断。恢复条件为本家族官方首次公告/正文可用记录或其他可核组合证明，届时只重开真实owner日，不将Updated改名公告。

日期隔离线索：[Seed 2604.07026v1](https://arxiv.org/abs/2604.07026v1)的CMS为04-07T16:00Z，但官方v1 Submitted=04-08T12:45:21Z晚于窗口。不能凭CMS确定候选；原始早发正文证明到达时定点重开。Google04-08博客只有日历日，内容是论文图示/审阅应用并链接更早论文，不因Agent标签扩大窗口或恢复AI for Science。

首发隔离：[In-Place Test-Time Training](https://arxiv.org/abs/2604.06169v1)的官方comment为ICLR2026 Oral，并有同题/同作者[OpenReview条目](https://openreview.net/forum?id=dTWfCLSoyl)。原审阅OpenReview forum与API验证/403，PDF的conference heading不能证明首次公开时刻；第三方Jan/Feb收录线索不作为原始日期证据。因此不计本窗分母、不评分、不据此写Books，尚不能正面判为某个更早日期。已读exact-v1 §3与评价附录的证据完整保留在[日期隔离笔记](../_sources/daily-20260408/V3_DATE_ISOLATION.md)。恢复条件为原始OpenReview公开记录/首次公开正文时间或可核实官方公告；只重开该家族的归属与MODEL-LONG-CONTEXT采用链路。

Meta当窗归属隔离：[Muse Spark](https://ai.meta.com/blog/introducing-muse-spark-msl/)与[Advanced AI Scaling Framework说明](https://ai.meta.com/blog/scaling-how-we-build-test-advanced-ai/)原页均仅写April8。前者核心说明三条compute轴、reasoning token penalty与并行Agent，以及evaluation awareness的反证限制；后者说明部署前后guardrail评价、loss-of-control范围与release rationale。这些不能仅因相交日历日放入本窗，现有直连HTML亦未恢复datePublished等时区字段。本轮不评分、不支持Books或“无命中”断言；原始带时区发布时间或可证明早于09:00的官方公开记录到达后，仅重开这两个家族。

## 6. 复核

复核者：原有效层为 `/root`、`/root/apr02`、`/root/apr03`；本轮逐批及最终独核为 `/root/supp_apr08_reader`（恢复后 `/root/resume_apr08_review`，非报告作者、非Books writer）。

结论：通过

resume_apr08_review（非报告作者）实际从头完整六部分DAY，复核93候选表与全部93证据项、来源范围、Books处置及终态隔离；R35记录真实检查与修正结果。

本轮独核先核四主题API实际查询、total/entry及单页停止，12分类仅03232–04933相关标题；不把宽命中变全文队列。root完整25题摘准入校准与reader受限Source分批衔接：补充61全部按具名身份、日门/必要Source、反证、owner与处置核验；30fresh实际正文/完整旧邻接/本人注POST通过，3既有实际正文与21旧具体NC及两仅报告/一争议有限复用，新3具体已有覆盖与03307争议亦已核。

排除侧保实际抽检范围：root首批03232/03302/03515与reader03632/04853（有效EX复用）、含糊03448/04175的有限core；reader另外完整题摘抽03432/03445（系统）、03376/04895（Agent）、2605.20197（模型）五例，覆盖范围外、领域类比/benchmark、角色包装与成熟组合缺具体增量等理由。多模态含糊项用core裁决，未把五例当全multi或全部排除项验收；其余明确排除项未独立逐项抽核，不声称497跨组命中、原567库存或全学科经过全文复核。未发现共同新错误理由的有效层不重开。详情见[本日R1–35](../_sources/daily-20260408/SUP_REVIEW_20261014.md)，最终非作者实际六部分实读通过；未将抽检范围升级为全池独核。

原32有效层依据在[原独立复核](../_sources/daily-20260408/V3_INDEPENDENT_GATE.md)：原32为20深入/12标准，15真实整合/16具体已有覆盖/05217争议；旧漏定位与误排已有实际纠正，未变化必要证据、正文/邻接与日期组合可复用，不用原整日通过替本轮补查DAY。原候选整行与连续原§4冻结，旧论证不得按本轮排版重写。

机器检查：此前31条旧候选补窗外告警已作为真实历史过程保留；本日报显式链接同日基线的“冻结候选日期”字段后，当前V3 validator实际exit0/PASS（1份V3），未改公共脚本或旧日期。作者实际检查93唯一家族/处置计数、228本地引用/36唯一路径（含精确大小写）无坏链；原32整行/窗口与17730字符连续原§4完全保留，限定本日README/SUP的cached及unstaged diff-check实际exit0，机器只证明可判定字段，不替代语义DAY。未stage、commit或push，未核代码或复现实验。
