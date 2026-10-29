# Daily 2025-10-05 补遗漏修复：唯一非writer复核

复核者：Rawls `01a176cd-9b08-7be1-9907-e4be757d944d`。作者：Goodall `01a176cd-26dd-72b0-a209-93da2cfa7fe4`；唯一作者交接为 [REPAIR_20261026.md](REPAIR_20261026.md)。本文件仅记录本人实际复核，不写 README、Books、State、index、合同、脚本或他日，不操作 index/commit/push，不清理副本及并发 dirty。

## R1 启动、范围与保护

2026-10-26 启动实际读取 AGENTS、当前 Research 合同、Report V3、Sources 使用说明/每日/按需/arXiv 主题边界、Prompt、ROADMAP 全文及 State 的 2025 路由与本日停点。实际读取本日 README、CURRENT_STOP、SCREENING、Curie FIRST/最终 DAY 记录、SUP_SCOPE、SUP_DATE、SUP_INDEPENDENT 的相关有效层和作者 A1/A2。不加载他日研究池，不扩 2026/Live/Weekly/八月/缺失日或 catchup。

唯一新增窗口为 BJT `2025-10-04` 自然日。启动 README SHA256 为 `be15c7a7feb47e6f5df82d1b7399ac910761ec7f6ad1c429f732d7b328381b44`；同日旧 baseline SHA256 为 `41eb38f18969fd1b36a7ef12fb24b796794dbfcc41f25a08b5d3adc2149d847a`。原小时窗、旧正式候选整行/原日期原分及连续有效 §4 保护；旧正式空表不冻结为本轮结论。启动限定 README/作者 canonical/本文件 status 为空，大规模已有 staged/unstaged 并发修改只观察、不动。

旧 Curie/root 的题摘、必要反侧与准入校准按身份、精确版本、命题不变分层复用，不认领本人重读 44/106 全部题摘、19/17 全部必要附件或实现/实验。旧日期请求中“不能用 DataCite 注册”不得覆盖当前合同允许的合法联合约束；旧 39/89 潜力及旧完成标签都不是本轮日期恢复或 DAY。旧 submitted 窗只用于发现，不是公告日召回；宽分类库存不改成全题摘/Methods/日期请求队列。

## R2 A2 首批有限校准

结论：本节限定通过，非 DAY/FINAL，不授全来源、其余日期项、Evidence 或 Books。

本人实际完整读取 `supplement-20261012/abs-2510.{02453,02630,03075,02483}v1.raw` 的精确 v1 标题、完整摘要、DOI 与现有 history。02453 的动态小 advisor/环境 reward 接口、02630 的 attention hypernetwork 生成 SVD 分量并剪奇异值输出、03075 的离散/连续目标与 conditioning 控制及 JEPA 辅助目标，均有具体待核选择；窄 P 保留，不能由主题名、作者名或性能宣传倒推贡献。03075 当前 DataCite 标题含后加副标题，不回填 v1 标题或结论。迁移/OOD、生成器总成本、额外目标/预算等仍未在本节作 Evidence 确认。

两代表 C 按旧有效层复用：02483 完整摘要虽称 attention/MLP 优化，但旧 root 实际 §1–3 necessary 未披露可辨新改变，标准 Llama/AdamW/BF16/ZeRO1 与吞吐/MFU 表不提供可归因新机制或质量/资源边界；非因未开源、硬件或体裁关闭。[FOIA](https://academy.openai.com/public/resources/managing-foia-requests-with-custom-gpts-2025-10-04) 旧实际核心说明为 approved-source 检索、人工敏感审阅/释放权与起草组合，未给新的执行或评价条件；不认领本人重看视频或确认 2025 正文逐字不变。两项不评分；未从宣传性能构造正式候选。

本人实际读作者保存的 [2025 规则](REPAIR_RULE_ARXIV_2025_20261026.raw)，并独立成功请求同一固定 commit 的 raw 官方原文；GitHub 页面 web cache miss 不改称原文不可得。该版本明确公告前不能给最终 ID、不能加速公告；Thu 14:00 至 Fri 14:00 ET 对应 Sun 20:00，moderation 可延迟。另实际打开 [DataCite 官方字段定义](https://support.datacite.org/docs/what-is-the-difference-between-the-created-and-registered-date-in-the-datacite-rest-api)：registered 为 findable 时进入 global handle，created 仅建记录，两者不混用。

实际解析三份 DataCite 原 JSON，逐项同 DOI、`relationships.client.data.id=arxiv.content`、`state=findable`、registered 均成立；与各精确 v1 history 的唯一 v1 提交记录核对如下。New York 此时 EDT UTC-4，三提交均在上述 Thu/Fri 截止段，故共同 L=`2025-10-06T00:00:00Z`，BJT Oct06 08:00。

| 身份 | v1 提交 UTC | registered 原字段 U | 本人判断 |
| --- | --- | --- | --- |
| [2510.02453v1](https://arxiv.org/abs/2510.02453v1) | 2025-10-02T18:02:39Z | [2025-10-06T01:28:09.000Z](REPAIR_DC_02453_20261026.json) | L≤U，全区间 BJT Oct06，本日 O |
| [2510.02630v1](https://arxiv.org/abs/2510.02630v1) | 2025-10-03T00:15:59Z | [2025-10-06T01:32:32.000Z](REPAIR_DC_02630_20261026.json) | L≤U，全区间 BJT Oct06，本日 O |
| [2510.03075v1](https://arxiv.org/abs/2510.03075v1) | 2025-10-03T15:02:27Z | [2025-10-06T01:43:20.000Z](REPAIR_DC_03075_20261026.json) | L≤U，全区间 BJT Oct06，本日 O |

这是公告日的有限联合推断，不将 registered 改名为实际公开时刻，不证明全球首次正文或历史逐字内容。现有 history 未见影响本窗口的早稿/撤回线索；后续正常版本不引发无限史查。三项本日排除可以停止，不评分、不展开窗外 Methods、不比较 Books，不创建 Oct06 或移动旧正式候选。

本节不是本日正式候选“原分校准”：三 P 实际窗外，旧正式 0，尚无应评分的本日新增项。后续若有实际拟入选项，全部逐项校准具体增量/原分；代表 C 目前仅覆盖技术报告与官方流程示例，未核其余排除集合，不称全量排除通过。

## R3 已实际检查的发现原件

本人实际解析 [model](REPAIR_DISC_MODEL_20261026.json)、[agent](REPAIR_DISC_AGENT_20261026.json)、[multimodal](REPAIR_DISC_MULTI_20261026.json)、[system](REPAIR_DISC_SYSTEM_20261026.json) 四原响应的 `links.self`、`meta` 与 data，检查对应 headers 为 200。查询为 `client-id=arxiv.content`，registered UTC `[2025-10-03T16:00:00Z TO 2025-10-04T15:59:59.999Z]`，即本补窗；四组均 `page[size]=100`、page1、total0、totalPages0、data 空，无 next。

实际表达式含 language model/models、LLM/LLMs、transformer/transformers、mixture of experts、foundation model/models；agent/agents、tool use/calling、RAG、retrieval augmented/连字符形式、agent memory/planning；multimodal、vision language/连字符形式、world model/models、vision language action/VLA、diffusion model/models、flow matching；large model/models、GPU/GPUs、accelerator/accelerators、kernel/kernels、model serving、distributed training、model parallel、inference scheduling。不由单一单数关键词代表全部主题；这四组也不声称覆盖所有新命名机制或所有公告日。

[邻日正控](REPAIR_DISC_POSITIVE_20261026.json)实际 self 是同 model 表达式、Oct06 UTC registered 区间、size1，total190、page1且有 next；仅读取 1 条 `10.48550/arxiv.2510.03223`，不把 190 扩成邻日队列、全题摘或本日命中。正控只能支持查询确实能返回，不证明注册日等于公告日或原始发布日。

本人另用标准 HTML 解析读取 [CL](REPAIR_LIST_CL_NEAR_20261026.raw)、[CV](REPAIR_LIST_CV_NEAR_20261026.raw)、[DC](REPAIR_LIST_DC_20261026.raw) 三原件的全部实际返回标题/身份，各25。CL/CV 为 2025-10 月目录 skip200/show25（201–225），总数2666/2884；DC 为同月 skip0/show25（1–25），总数341。只核这75次题名出现，不称75唯一或全部范围外；月页无本日分组，当前标题也不能回填精确 v1。已识别其中 reasoning/reward/context/表示/生成/训练/serving 的相关线索，但尚待作者具名处置，不能靠月 ID 或周末口号一并关闭。早先 day 参数 400/无效月份路径 404 的 raw/headers 只是失败，不作零命中。

本节为实际观察，尚不授发现层整体闭合或其余候选排除；待作者交接真正停止与相关身份日期/贡献边界再只核变化，不要求把三个月库存逐项关完。

## R4 A3 下界恢复与 A4 新观察

结论：A3 的128个旧潜力 **arXiv 首公告事件**本日排除通过；不授所有渠道首公开已核，不取消具名早稿/修订线索，不是全量 Evidence/Books/DAY。

本人按 SUP_DATE 的精确89身份读取原件并独立解析：52份本地精确 v1 HTML history、34份定点旧 `exact-v1.raw` Atom 与3份 `titles-supplement-exact.raw` Atom（02613/02774/02838），均恢复到同精确 v1，无缺失。范围为 UTC `2025-10-02T18:02:39` 至 `2025-10-03T17:59:56`，89项无一落在 Thu18Z–Fri18Z 之外。按 R2 已核适用公告规则，每项 L 都为 BJT Oct06 08:00，已晚于补窗，足够排除 **该 arXiv 事件**；无须再向89项逐项索登记 U。05156/06240/15926/15927/21740/2511.11579 等晚 ID 的原提交记录也实际纳入解析，没有用 ID 月份推日期。此处不说它们都实际 Oct06 公告，延期只使事件更晚。

对原 SCREENING 39项，本人独立解析37份本地 history 与新取03689/03751精确页，39项无缺失、均 UTC Oct04（00:24:44–23:38:18）；与89集合交集0。按 Fri14:00–Mon14:00 ET 规则，共同 L=BJT Oct07 08:00。另实际读取新两份精确页的完整题摘、comments/history：03689 的单模态监督/梯度冲突及解耦adapter潜力、03751 的部署前地图参考集适配条件仍保留；接受注记不证明早正文。旧39贡献/反侧层不因 arXiv O 被降成 C，也不授局部实验真实性。

本节128是身份与日期原字段的结构化全量核对，不是128篇题摘或附件独立重读。37份跨日 Atom 只定点读取本日同身份的 id/version/published 元数据；published 保留提交口径，仅用于最早界，不改名为公开日。不加载他日当前研究池、不移动归属、不创建后日报告。

A3 单列的02561精确OpenReview、03727 thesis、03799旧workshop、15926 April家族仍保留不同渠道/事件边界；尚未在本节确认其新恢复原件或终态。作者已明确03799作者入口仍普通可核，不可一并归零。02526/02569/02742接受或后发表线索按旧有效限制保留，无具体当窗早正文信号不无限史查。

本人另实际解析第五组 [MECHANISM](REPAIR_DISC_MECHANISM_20261026.json) 的 self/meta：同本窗/主体、size100、page1、total0、无 next，含 low-rank/low rank adaptation、LoRA、state space model/models、linear attention、attention mechanism/mechanisms、mixture-of-experts/MoE、parallel training、collective communication、KV cache/caches。由四组补为五组是新增有限发现，不补造早先本人已核五组的记录。A4 四个新命名精确 v1 和另一 CL 导航切片尚未在本节签完成；R3 三原页的75题名层不重读、不扩全月。

## R5 A5 必要校准与有限来源收束

结论：A5 的具名日期分责、03315窄 P/精确日期保留、有限来源停止与本日无可采用新增命题通过；不是全 Coverage/Evidence，也不是 DAY/FINAL。

本人实际解析32份 `REPAIR_TITLE_DC_<ID>_20261026.json`，逐项核同 DOI/精确 ID、arxiv.content、findable、唯一 `Submitted/v1`、registered 原精度；按已核2025规则与 America/New_York 时区独立复算 L≤U，32项无冲突。25项 L=Oct06 08:00 且 U=Oct06，6项 U早于Oct04，03315唯一跨日。00183/00207/00606/00991完整区间在Oct02；01256/01260为Sep26至Oct03，虽非单日但全早于补窗，足够判本日 O，不能编造其唯一公开日。其余25项及精确身份与作者 A5 三组名单一致；02878/02930属于已有明确贡献关闭，不因补读元数据改造成新 P 或新的日期义务。

本人实际完整读四个新命名精确 v1 的题摘/history（作者只对03315认领全AB，双方范围不混）：02752困难度/能力边界的自反馈训练、02912跨空间crop分配视觉token保留、03191码本/维度/子空间分解的图像表示均有可辨潜力，但其 arXiv 最早界已晚于补窗，未因小模型/局部实验或省审阅关闭贡献，也不采其百分比。03315的稳定分母、单 calibration text、第一层 GPT2-Small 上下文线性近似与未激活神经元发现符合窄 P；固定token分布/broad且弱content heads条件必须保留，未证明跨分布近似、普遍可解释或可控。

03315同精确history与DataCite的 v1提交=`2025-10-01T00:29:39Z`，L=BJT Oct02 08:00，registered U=`2025-10-07T02:46:57.000Z`，BJT Oct07 10:46:57；完整区间跨目标日。本人实际核原JSON中的 Updated/Available/version 不替代公告日，不依靠单个早L或晚U判O。实际核 exact-search 原请求与发现的 OpenReview `OIcNvCOpoB`；原API为403 ChallengeRequired，本人又独立实际打开 [精确forum](https://openreview.net/forum?id=OIcNvCOpoB)，仍重定向人机核验，不是成功公开note。搜索PDF同摘要/相对索引日期不证历史首日。精确03315日期保留可以隔离：不列已确认当窗候选、不评分、不为日期未知的明确 P 扩全Methods/owner；只待同v1官方日公告、合法更紧完整bounds或同正文真实发布日。这不是“没有潜力”或“0命中”。

四具名他渠道边界本人有限核回：03799作者原HTML目标行确为同题/Asghari与Nenno、ECML AIMLAI2024并连同arXiv，不给正文上网首日；不凭旧会名或搜索PDF判断本日归属。03727原响应为空，但headers实际为202 Accepted、`x-amzn-waf-action=challenge`/Content-Length0，故不是成功学位论文记录，也不是普通200空内容证明无论文。02561原JSON明确精确note N2UmSTFFUV的403 challenge；同旧有效forum/PDF停止复用，不反复同路径。TeLLMe旧April原件/旧三机制的有效身份层复用，新URAM/streaming/decode-attention差额不能倒灌April或本日。四项分别保留具体同正文首日/修订身份恢复条件，不因128个arXiv O被一并解锁；无采用则不假称Evidence或Books已完成。

来源方面实际再次读完旧SUP_SOURCES十四行及A5的复用/新增范围，复用的是旧真实页数、语言、末页/失败与限制，不认领本人再次解析全部机构数组或正文。新OFFICIAL原JSON的四组域名/目标日期查询已实际读取；返回包含社区、现代目录及窗外结果，不是严格目标窗零结果，更不是完整官方目录。Google page2新headers为空，与作者记录超时一致，不能授成功页面。DeepSeek/Moonshot/Seed两type末页/ERNIE两页旧有效有限层保留；OpenAI Research、Google必要历史段、Meta、Qwen Sep23→Nov13、Hunyuan2025语言段、ZAI Oct段、MiMo未标日Blog与MiniMax历史缺段仍外部限制，不授完整覆盖。

对新检索发现的 Updating GPT-5，本人实际独立打开官方release页，只读Oct03完整短节及Oct06/Sep29邻界，再定点比较10-04同事件行与对应证据段。确为同一已处理安全路由版本事实，2+1+1=4/原处置保持，不在本日重复评分或借此重审他日池/Books。厂商同等表现/更快主张未提供可采用协议，不从重复事件增造本日正面证据。Anthropic CyberDefenders同事件去重沿用旧有效层，不说Oct04没有事件。按需保持精确作者/出版/两OpenReview身份，无每周组或全会议扫描。

分层抽样与未核范围：本轮新完整AB实际为首批4、Curie恢复2和标题补检4，合10份（均不计正式Evidence），代表C为02483与官方FOIA按有效necessary复用；全部当前拟当窗新增只有03315这一个待日期潜力，已实际校准。其余旧C/安全反侧按不变有效层复用，没有宣称重新全量复核17C/4C、全部附件或所有月目录。32元数据和128日期结构核对是不同层，其中02878/02930与旧范围有交集，不相加成160唯一论文。没有新落窗可采用命题，因此当前无需书稿PRE或具体NC比较，不以未读正文判“已有覆盖”，不强造diff。

## R6 唯一实际 DAY

结论：通过。对象为作者 A6 已保存、A7 四单元窄同步后的本日完整六节；当前实际 README SHA256=`6fda8b9f935a6b94386009f93bc03b3ac262934d95ea9633e84cc4b377bc8946`。这是本轮 DAY，不是完成态 FINAL，也不授全 Coverage/Evidence 或全球无遗漏。

本人实际完整通读 A6 的 `c9a2c3b4a967ae87fb57d4ee66684038671287cd2df5a49bdba0d8e980649f6b` 六节，逐节核本轮结论/来源停止、候选空表的实际原因、连续旧证据与新边界、具名外部保留、复核身份和未完成字段。发现 §2 AIES/U-LAG 沿用旧日期请求措辞，与当前 A5/§5 停止边界不清；作者 A7 仅修四个来源 gap 单元，本人实际读回 AIES/IndiCASA/ASRU/U-LAG 四行及实际 diff，旧身份/接受/后发表限制保留，arXiv O 不被扩大成全球首日结论，无具体Oct04早正文/修订不新增无限请求。其余已读整体复用，不第三审原源或附件。

当前六节已区分五组 registered 发现、月目录有限相关标题、128旧潜力 arXiv 下界、32补检日期与03315跨日。旧有效贡献/安全反侧保留，03315不因查询0/小模型被排除；03315、四他渠道与必要历史段均不进入当窗正式候选、正面Evidence、Books或无遗漏/安全性能断言，恢复条件具名。无新经本窗准入采用命题，Books无提案/写入、无具体NC谎报，无SAVE/POST待核；不是用户限定仅报告。

实际机器/范围检查：V3通过；本轮 README/作者canonical/本人review 的 working及cached限定 `git diff --check` 均通过，A7后working与V3再次通过。三个Markdown实际本地链接65个目标均存在；本文新增记录会自然改变链接计数，不沿用作者64作固定配额。原小时窗逐字一致；原§4在 `## 4. `后正文3898B连续前缀保持（包含该标题前缀即作者3904B），候选表仍无原行/原分变化，H2恰为六节。已实际检查README全部diff，没有Books写入待验。机器只验可判定接口，不代R2–R5语义与本节DAY。

作者报告本日 sources 广范围 cached 检查有原已暂存副本 `baseline-before-supplement-20261012 2.md:73` EOF空行；本人未将其当本轮错误或擅修/unstage，也不声称广范围cached/全树清洁。本人限定三个文件的cached检查确实通过。旧副本与大规模并发修改继续保护。

## R7 唯一实际 FINAL

结论：通过。2026-10-26 依用户指示同模型/同推理设置只接 R6 后缺层，未覆盖模型或 effort；R1–R6 的研究与完整 DAY 有效复用，不第三 Research、六节或附件。作者 A8 已真实保存完成态并完成 QA 后，本人才执行本节，未预签。

实际本日 README 完成态 SHA256：`821097e2712589d05abe9e67d54dbb4de18aedb4a950b3cc5b6c86a3c6d79b7c`。本人实际读回 A8 和完成态 header、§1完成说明、§4新增边界、§5普通待办/外部隔离、§6真实R6与QA边界。再将这些完成字段在内存反向还原为 R6 原文，所得 SHA256 精确为 `6fda8b9f935a6b94386009f93bc03b3ac262934d95ea9633e84cc4b377bc8946`。因此本次变化确实仅为 header 状态/时间及 §1/4/5/6 的真实完成同步；§2 A7四行、§3、连续旧§4、所有来源/身份/贡献/日期判据与外部隔离没有夹带改动，不重读已经验收的六节。

本人实际重跑完成态 V3 通过；三个本轮Markdown的 working/cached 限定 `git diff --check` 均通过；67个本地引用目标无缺失、行尾空白0、41份本轮JSON均可解析、H2仍为六节。机器不替代R1–R6语义判断。限定status为 README 仅unstaged、两个canonical untracked；本人只写本review，未写README/Books/State/index/他日/合同/脚本，未stage/unstage/commit/push或清副本。广范围cached旧副本EOF警告仍按R6/A8保留，不声称全树干净。

本轮确定新增候选0、Books提案/写入0，没有待核SAVE/POST或具体NC冒认。普通研究/作者保存/QA/独核剩余0；03315精确v1日期、四具名他渠道/旧家族与机构必要历史段、arXiv发现范围局限继续作为本窗已隔离外部保留，恢复条件沿已验收§5。完成不授全Coverage/Evidence、零事件、全球无遗漏或性能/安全保证，不声称实验复现。只向root交本节FINAL、上述actualhash与余项，不增加年度或启动后日。

## 当前停点

R7唯一实际FINAL已通过，对应完成态actualhash如上；普通剩余0。R1–R6不重开，外部保留与精确恢复条件不变。作者不必为同步本FINAL再改README制造新hash；root据本节与实际保存态接收，不等第三批准/额外回执。本人不写State、不计年度、不启动后日。
