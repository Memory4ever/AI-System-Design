# Apr17 V3 日期、准入与来源覆盖前置独立审计

## 范围与结论

本轮非作者审计只处理 `[2026-04-16T09:00:00+08:00, 2026-04-17T09:00:00+08:00)` 的来源停点、日期推断与有限双向准入抽样，不代替最终日级 Gate。实际读取当前 AGENTS、统一 Prompt、研究与报告合同、每日来源组，以及[正式报告](../../17/README.md)和[作者记录](v3-reopen-notes.md)。有效的既有单篇独立审计复用，不重新阅读 88 篇全文，不扫描每周来源或扩展 536 库存。

结论：14 个每日来源均有行，所列检查范围与作者记录基本一致；8 个明确外部子入口缺口不能称 Coverage 通过。88 项的日期组合支持**有据的区间推定**，没有在本轮样本中发现具体反例；这不是逐篇首次公开时刻证明。88 项表格与证据章节一一对应。不过排除项抽查发现 **14969 的关闭理由不足，须局部重开准入**，因此不能据此把当前 88 提案直接冻结。报告此时记录 39 个 Books 窄缺口提案、实际整合 0；本轮不判 Daily Complete。

## 1. 覆盖表与实际停止范围

这里审查的是作者保存的实际入口、读取范围与失败边界，不冒称本审计重新抓取了全部机构网站。复用目录成功不证明其未列出的端点也成功。

| 每日来源 | 本轮对照到的实际范围/停点 | 前置判断 |
| --- | --- | --- |
| SRC-OPENAI | News RSS April15–18 邻界；Codex Apr16T10Z、Rosalind Apr16T01Z 的原文处置；Research 历史分页未恢复 | RSS 有界检查可复用；Research 缺口保留，不能报全 Research 零更新 |
| SRC-ANTHROPIC | Research 的 publishedOn Apr14T13:01Z → Apr22T14:12:30.673Z | 该目录跨窗停点有据；不等全部作者稿覆盖 |
| SRC-GOOGLE-AI | DeepMind selected264 首屏 Apr22→Mar22；April Blog 9 项与 Apr13/21 邻界；Simula 家族重复及 neuron 范围排除 | 已读目录可复用；Google Publications 历史日级目录缺口仍在，Blog 日精度不能补造时刻 |
| SRC-META-AI | Research 历史入口尝试未取得可靠窗口停点 | 明确受阻，不应写零命中 |
| SRC-QWEN | 动态 API 40 条 Apr15T10+08→Apr18T10+08，静态60条最晚2025-12 | 官网拼接目录的有界范围可用，不推及全部作者稿 |
| SRC-DEEPSEEK | Research Jun24→Feb25、动态 Apr24→Dec1；32 个截止前非 fork 仓库 release 到尾，13 个历史 release | 已查 release 的窗口判断可复用；未扫描普通 commits 不构成隐含承诺 |
| SRC-MOONSHOT | kimi-cli release 两页各20条，1.35.0 Apr15T12:55:10Z→1.36.0 Apr17T14:10:46Z | 该 release 邻界可用；历史 Kimi Blog 缺口不能被替代 |
| SRC-TENCENT-HUNYUAN | publicList total9/list9；58 个截止前非 fork 仓库中22个 release 到尾，36个403；HY-SOAR 同家族线索 | 目录及成功子集可复用；36个 release 访问缺口明确保留 |
| SRC-ZAI | Research Apr29→Apr7→Apr1；44个截止前仓库身份，release补核403 | Research 停点可用；release 未完成，不以 CMS createdAt 或仓库创建时间断言公开时间 |
| SRC-BYTEDANCE-SEED | US论文 API page20，actual20/total242/next40，AgentWorld Apr19T16Z→LeapAlign Apr15T16Z；Blog95目录 Apr22→Apr8→Mar31 | 作者检查的这两个目录跨窗范围有据；不是242项全量逐篇或所有作者稿覆盖 |
| SRC-BAIDU-ERNIE | Blog Apr15→Feb6→2025；已知 release 2025-06-30 | 所列入口可复用；不外推普通 commits |
| SRC-XIAOMI-MIMO | Paper Jun29→Mar13→Feb3；历史Blog未恢复 | Paper目录停点可用；Blog缺口保留 |
| SRC-MINIMAX | EN May26→Mar18、CN Apr27→Mar18；当窗 CLI 1.0.8/9/10 的 release、compare 与必要 PR89/78 处置 | 成功目录与事件审阅可复用；Agent Tech Blog 缺口保留 |
| SRC-ARXIV | 536 个缓存标题作主线查漏、旧40完整题摘、有限强信号消歧；88 个提案的必要 exact-v1 已有具名独立审计 | 宽列表未被当作536篇全文队列；本轮完成日期组合核对与有限双向抽查，但14969须局部修正后再冻结 |

外部缺口准确为 OpenAI Research、Google Publications、Meta Research、Moonshot Blog、Hunyuan 的36个 release、Z.ai release、MiMo Blog、MiniMax Agent Tech Blog，共8个来源行的子入口。它们是被隔离的限制，不支持“无遗漏”或候选正面证据。恢复条件是取得相应官方带日期目录或缺失 release 响应，仅重开受影响入口/事件。arXiv 准入修正及实际 Books 写入属于普通可执行工作，不能混入这8个外部缺口。

## 2. 日期组合的支持与限度

[arXiv 官方 availability 规则](https://info.arxiv.org/help/availability.html)说明，永久 ID 随公告过程分配，不能提前生成；通常周日到周四20:00美国东部时间公告。Apr16 周四20:00 EDT 对应 Apr17 00:00 UTC / 08:00北京时间。审核与公告延迟可能存在，因此 submitted 仍不等于公开日。

实际将正式 §3 的88个身份联至[原始字段缓存](../arxiv-owner-replay-20260903/20260417/arxiv-owner-receipt.json)：每项都存在，自身 `v1_updated_timestamp_revision_metadata_only` 范围为 `2026-04-17T00:00:20Z`～`00:59:50Z`。其中30项当前 OAI datestamp 晚于 Apr17 或为空；不能据当前 OAI 后改字段移动 owner。缓存两端为14154的 `00:00:07Z`、15174的 `00:59:56Z`；15180为 `01:00:24Z`，另有14152/14188/14240后改字段，均由作者另行隔离。

| 抽核身份 | 原始 submitted，非首次公开 | 自身 v1 Updated，非首次公开 | 当前 OAI | 日期判断 |
| --- | --- | --- | --- | --- |
| 14170 | Mar25T06:57:49Z | Apr17T00:00:28Z | Apr17 | 提前提交但 Apr 永久身份及该批早字段支持本窗推定，不归 Mar25 |
| 14769 | Apr16T08:29:48Z | Apr17T00:36:24Z | Apr17 | 与公告槽、连续身份及邻界共同支持本窗推定 |
| 15171 | Apr16T15:48:40Z | Apr17T00:59:50Z | Apr17 | 同上，接近上界但自身字段未跨截点 |
| 15174，边界而非候选 | Apr16T15:51:16Z | Apr17T00:59:56Z | May5 | 后日 OAI 不独立推翻早段；只用作联合边界，不由此准入 |
| 15180，外部隔离身份 | Apr16T16:03:13Z | Apr17T01:00:24Z | Apr17 | Updated 已跨截点，也不能仅凭它机械认定次日首次公开 |

这不是单用 Updated 的推理：永久 ID 的公告分配语义、同批连续身份的早段分布、官方公告槽及可得 OAI/邻界相互支持，足以将现88项保留为有依据的 `[08:00,09:00)` 区间推定。它仍依赖“这些早段身份属于相应公告批次”的假设，不声称每个身份的成功公开日志或历史 membership 已逐篇恢复，也不对后改/跨界项沿用同一判断。

本轮实际重新打开官方 availability、14170/14769/15171 的 exact-v1 abstract，以及14154/15174等边界与准入抽样入口；论文正文只定点检查下节的必要消歧。14514 abstract 的一次重新获取未成功，未将它算作 live 核验成功。作者另报有限官方历史列表尝试 Timeout/Cache miss 与 export 镜像不可达，本审计未冒称自己重新完成列表抓取。缺 membership 快照本身不自动推倒以上组合支持；若后续出现具体早于窗口的正文可得记录、公告延期或身份批次反例，只隔离受影响项，不重读所有全文。

## 3. Raw、候选身份与审阅对应

独立读取并实算：§3为88行、88唯一 arXiv 身份；§4为88个对应标题段、88唯一身份；两侧 missing/extra 均为空，88均能在原始536身份缓存中找到。旧536与另一 submitted 库存1059不是两个可相加的本日论文数，缓存旧 owner 解释失效；此次只使用其题摘和明确语义的原始版本字段。

88/536约16.4%仅是“提案数/宽发现库存”的描述，不是全536完整语义筛选后的合格率，也不是评分基线。其余448个身份不自动等于448项完整前分母关闭，更不等于448篇无贡献；实际工作是标题主线查漏、有限题摘与必要消歧，不能补造全量摘要阅读。88项具名单篇审计可复用，但新的负样本纠错需处理后才能确定最终分母。source→owner通过和actual Integration仍分别计数。

## 4. 双向准入抽样

### 三个保留项

- **14170，保留 PASS。** 完整题摘的信号是 persistent evidence pool 与 deficiency-driven query。复用已通过的必要 PDF 审计及正式§4：Irrelevant 搜索记忆约束下一次 query，不能混同 contradiction factual evidence；相关性 confidence 不等正确概率。实际 Ch76 的 gap 是这两类状态责任的窄分工，而不是“RAG相关”即准入。
- **14769，保留 PASS。** 复用[既有独立审计](V3_ORDINARY_NINE_FINAL_INDEPENDENT_AUDIT.md)的 §III/Eqs6–13与实际 Ch28 比较：为可复用初始化主动训练 templates、目标 scalers 与解除约束后训练分别承担状态；不是任意 checkpoint 免费扩形。原目标形状固定的约束确实改变了初始化接口，有限实验不等全规模迁移保证。
- **15171，保留 PASS，Only不改。** 复用[既有独立审计](V3_FINAL_BATCH_INDEPENDENT_AUDIT.md)的 §III–IV/TableI/Fig9：更小的 FP residual 不必对应更高感知质量，约束收益与 penalty 成本须分测。它直接提供生成目标选择的受限反证，不因 MNIST、小模型或最终不写 Books 而排除；也不采用作者未经支持的普遍 score 恒等解释。

### 四个排除侧样本

- **14178，关闭 PASS。** 本轮重新打开[exact-v1](https://arxiv.org/html/2604.14178v1)，只核 III-C/IV-B、VI-A/B。实际评价为1800合成日的 LSTM+attention 六/七类活动预测；新增类别来自修改已知生成规则后再训练。评价对象不能支持被宣称的 LLM 自主认知模块学习/真实任务 outcome 新边界。不是因模拟或小模型直接排除，而是具体机制与评价的连接不足。
- **15003，关闭 PASS。** 本轮重新打开[exact-v1](https://arxiv.org/html/2604.15003v1) §3.2–3.6/4.1，核 learned template、VAE round-trip、motion surrogate 和 confidence-weighted 反 warp。贡献是受限图像来源恢复/视频取证工作点，不能变成 cryptographic origin、生成物全真实性或新基础模型控制合同；关闭理由不依赖“CV无关”。
- **14154，范围关闭 PASS。** 实际读[官方 v1 abstract](https://arxiv.org/abs/2604.14154v1)及缓存完整题摘，内容为五类传感器融合、老人风险评分与三级通知。它没有提出大模型训练、推理、基础模型表示或 Agent 权限状态的新机制；一般 edge/cloud、confidence、privacy 词汇不能替代项目贡献。无需为排除追查完整发表史或全文。
- **14969，原关闭 REOPEN。** 本轮重新打开[exact-v1](https://arxiv.org/html/2604.14969v1) §3/Algorithm1、§4、§6，并只用 D.6 消歧静态对照。新增任务进入后重评旧模型 skill vectors；active/global task archive 分别承担当前难度与历史 novelty/选择参照，模型群体表现又控制任务变体。这是具体反馈接口，不能仅因 mature merge 或未证明 selector 正确而抹去。D.6拿 generation5 进度估计静态终态，不证明等预算共演化因果；Coverage OR不等可执行答案选择，固定 scientist/同base seeds也限制外推。

14969 的最窄主线连接是 `TRAIN-DATA` [Ch27](../../../../../books/part-04-training-system/27-data.md)“静态 Mixture 到版本化 Data Control Plane”及“Coverage Contract”段：当前已经承载 policy-relative difficulty、生成/验证分权和 held-out 边界，尚未具体说明双archive和新增任务后旧模型能力参照的重评接口。[Ch28](../../../../../books/part-04-training-system/28-pretraining.md)已有 weight artifact 组合也不是该分工。建议恢复有限候选审阅，初步 `2+1+2=5`；它是否需要窄 Books 修改仍由实际采用命题决定，本审计不直接签署 Integration。只重开此抽中的家族，不由一个反例扩成536逐篇全文审阅，也不推倒原88项有效单篇证据。

## 5. 可交接状态与验证

前置结果是：来源行与记录范围对应；8外部缺口保持隔离；88日期支持有边界的联合推定；88身份/§4映射一致；抽样3 retained PASS、4 preclosure中3 PASS/1局部REOPEN。需作者处理14969的准入、证据与处置后再确定最终分母。原39个Books提案仍需实际写入及写后复核，随后由最终非作者审查报告整体，不把本文件当日级验收。

本轮仅新增本审计，未修改正式报告、Books、其他日期或全局 checkpoint；未 stage、commit、push。身份联表、Markdown链接/围栏及本文件 whitespace 检查均为本轮实际执行的静态检查，不证明全站覆盖或整日报闭环。

### 14969 局部纠错交接

作者随后基于同一必要证据提出恢复 `2+1+2=5`、标准完成、仅报告。本审计认可这一**窄处置**：承认新增任务使旧模型 skill reference 必须重评的真实接口，不再用 mature combination 一句排除；同时保留 D.6 早停代理、Coverage/selector 分离、BoN 负例、固定 scientist 与 same-base 限制。现 Ch27 的版本化 observer/active set/held-out 原则不足以称整份共演化配方完整 Existing，但也无需为了这份局部配方自动再写一个 Books gap。其 `00:49:08Z` 仍只参加上述组合日期推定。

Only 是基于所支持内容与证据限度的判断，不是因共享 Books 等待写锁而逃避 Integration。预计修正后的 `50深入+35标准+4争议=89` 与 `39待实际Books+17已有覆盖+29仅报告+4争议=89` 算术一致。

这表示该局部准入/证据处置建议通过，不表示此时已经实查正式表完成89项同步。前文88身份联表是同步前的真实快照；作者若添加14969，最终复核只需检查该项新增表/§4一一对应与相应总数，不重读原88篇。整日报 Books 与日级 Gate 的待办不因此消失。

### 正式89项同步后定点验证

作者落盘后，本审计实际读取新增14969表行与§4正文：三维评分5、标准完成、Only；双archive/旧模型重评接口、gen5 static代理、Coverage/BoN分离、负例与成本限制均与已核原文和窄处置一致，没有用泛“已吸收”或完整Existing替代内容。独立再次实算正式表89行/89唯一身份、§4 89段/89唯一身份，missing/extra为空；实际状态为50深入、35标准、4争议，39待实际Books、17已有覆盖、29Only、4争议。此次只验证新增差异，不复审原88篇。

恢复14969后的确定性结构与局部处置无新增矛盾，前文准入REOPEN已由本项修正解决；14来源/8外部子入口隔离与日期联合推定的前置结论仍有效。实际Books仍0，最终整体验收尚待，本审计不将内部写锁协调未回复升级为外部材料受阻，也不判Daily Complete。
