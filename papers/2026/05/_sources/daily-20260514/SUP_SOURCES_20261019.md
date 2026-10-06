# 2026-05-14 增量来源补查（2026-10-19）

## A1. 本日范围与运行前基线

作者：`/root/may14_supp_author`；独立 reader：`/root`。

- 仅补 `2026-05-13 ～ 2026-05-13` 北京时间完整自然日。原窗口 `2026-05-13T09:00:00+08:00 ～ 2026-05-14T09:00:00+08:00`、130 条既有候选行、原日期评分及连续原 §4 保护，不迁移旧归属，不从 Weekly 反推。
- 运行前完整原件：`baseline-before-supplement-20261019.md`。本次此前无 SUP；旧 Round6 reconciliation 对 128 arXiv + 2 官方家族的有效审阅层定点复用，不再研究原候选池。原 714 宽 inventory 仅为查漏线索，不是逐项摘要或全文队列。
- 已完整加载本日 AGENTS、Research/Report 合同、统一 Prompt、Sources 使用说明/每日/arXiv主题/恢复及 ROADMAP；LS 只作 2026 来源补查路由。
- 范围仅本日 README、本 SUP、必要本日原始记录；不改共享 LS、索引、公共合同或脚本。Books 只在 root 协调逐字稿/窄位且必要独核后写；不 stage/commit/push。
- 使用 using-agent-skills 的范围/核验纪律；写作风格检索工具不可用，遵循用户明确的项目写作合同，不作额外跨应用检索。

## A2. 发现与首批校准（未完成）

具名跨日线索只复用身份/原件：INSET `2605.12305v1`，上日未评分/未读全文/未采用；本日原候选无该 ID。已实际读其完整题摘、版本史与同 DOI DataCite 原字段（见相邻日 `sup-raw-20261018/2605.12305v1-abs.html`、`2605.12305-datacite.json`；此精确复用不构成扫描邻日池）。

日期：唯一 v1 提交 `2026-05-12T15:54:49Z`；依 May12 EDT 14:00 cutoff 与20:00公告最早界为 May13 08:00 BJT；同精确 DOI、登记方 arxiv.content、state=findable、registered=`2026-05-13T02:46:12.000Z` 给 May13 10:46:12 BJT 最晚界；全区间同一 May13自然日。Seed官网 May12题摘是早摘要事件，不证明当日完整论文已公开。尚待独立准入校准，不把时间下界/登记字段改写成实际发布时间。

准入提案：多图输入分离导致指代与视觉目标长距离绑定 → 把参考图特征直接插入对应语义槽，配合15M交错指令数据 → 需要重新考虑多模态conditioning的线性化与局部性，拟归 `MULTIMODAL-REPRESENTATION`。潜在机制明确，实验可信度/反侧待必要Source，不用摘要缺细节排除。

### A2.1 首批准入提请（全文尚未展开）

1. **INSET / 2605.12305v1**：按上述具体增量拟准入；D2+R2+U3=7，审阅目标是语义槽内插图的表示机制、受控比较能否将收益归因于布局，以及复杂多图指令边界，不提前采用宣传数字。原候选无该ID。
2. **OpenAI TanStack response（官方 May13事件）**：已实际读官方完整核心说明与当前 amendment，RSS `Wed, 13 May 2026 00:00:00 GMT` 落May13BJT。旧原则是隔离凭证与验证软件来源，实际新增事实是依赖污染经两个员工开发环境接触代码签名材料，在一类已分阶段部署的防护尚未覆盖设备上发生；响应组合为撤销身份/轮换凭证、停止旧证书新notarization、复核既有签名及有期限客户端迁移。拟准入D2+R2+U2=6，安全约束变化须深入核受影响域；不把厂商“未发现”写成无妥协证明、不把当前June26 amendment当May13当时已知。本次curl Cloudflare失败，官方全文由web原页成功返回，RSS原件本日保存；不是必要证据受阻。
3. **Google Cloud proxy-model SQL blog（May13）拟排除**：已读官方完整机制与评价说明，定点点击其明确唯一SIGMOD论文 `2603.15970`；v1为Mar16、当前v6为Apr14，无May修订。Blog自述为论文tl;dr，所述logistic-regression over embeddings、online/prepare-offline、heldout fallback、reasoning/extreme-selectivity failure均为旧论文内容，未标新mechanism/release delta。属于本日新解释文章而非新贡献事件；不评分、不重研究旧论文。两页原始入口：`https://cloud.google.com/blog/products/data-analytics/more-than-100x-faster-and-cheaper-llm-powered-sql-queries-with-proxy-models`、`https://arxiv.org/abs/2603.15970`。curl超时后web官方页成功，不称无命中。
4. **Anthropic Research**：实际官方完整嵌入publication数据的相邻条目仍为May08 teaching-claude-why和May14 17:06Z policy文章（北京时间May15）。May13无Research事件。搜索命中的business/browser-use指南属于使用建议，不是模型/Agent研究新增证据；不沿events/product目录扩池。

待root首批准入校准后展开必要Source。其他每日来源与arXiv主题发现继续，原始宽命中不自动进入摘要队列。

### A2.2 root首批准入校准（实际完成）

root已实际读INSET精确v1完整题摘/history与同DOI包络、TanStack官方全文/RSS、Google proxy完整core与所链旧版本。INSET准入通过，但作者拟7分把单模型conditioning及recipe扩写成跨系统/认知基础，纠正为 **2+1+2=5** 标准；必要方法、同骨干同数据布局消融与复杂指令反侧仍须读足，有真实owner gap则深入受影响域，不因5免Books。这是准入期命题纠正，不以省工作降分。TanStack **2+2+2=6** 与安全必要深入通过；Google tl;dr具体排除通过。只重开INSET具名generic evaluator closure，不扩全旧池。可以开始两项必要Source/owner。

## A3. 本日发现的实际边界（持续更新）

- arXiv API 按 submitted `202605111800 TO 202605121800` 的**恢复线索**检索，提交不是公开证据。三个主题式请求原样存在各自XML feed title/self URL：model在cs.CL/cs.LG的language/foundation/Transformer/MoE；system在cs.DC/AR/PL/OS/PF的LLM/GPU/Transformer；agent在cs.AI/IR/MA的LLM/language/agent/retrieval。首响应model201（当前200，余1待恢复）、system19（已到尾）、agent264（当前200，余64待恢复）；尚未覆盖多模态主题。只相关标题浏览，不把条目总量当新论文数、逐项关闭或全文队列。
- 原05-13完整baseline的163候选与本日128 arXiv候选**只机械提取ID作事件去重**，291唯一ID，不读邻日候选论文。第一次误选919-byte行政SUP_BASELINE，随即纠正为`baseline-before-supplement-20261018.md`完整原件；未基于错误计数作研究或处置。
- 只对具名INSET定点读旧筛选：05-13旧`v3-active-ledger.json`以“只建立任务数据/evaluator，未改变evaluation identity/release gate”关闭；这与原摘要明确的语义槽内插图机制不符，构成本次重开具体理由，不宣称其旧排除有效。其他旧层不因此整池重开。
- 从上述主题相关标题中，另定点完整题摘核 `11125 / 11134 / 11215 / 11222 / 12070 / 12227 / 11869 / 11887`；前六已补精确v1 abs，后两仍待版本资格核。当前只是准入事实检查，未称全文Source已完成、未预定数量/整合配额；正文访问还未展开。
- 机构已读取本日原件：OpenAI RSS、Anthropic Research完整嵌入历史publication、Qwen旧home→当前qwen.ai/blog动态壳、DeepSeek home→updates、Kimi Blog、HunyuanResearch动态壳+公开JS、ZhipuResearch、Seed论文页+公开分页、ERNIE、MiMo主页、MiniMax英文Blog。Qwen动态目录/Hunyuan全部列表/Seed目标段及Google/Meta和MiniMax中文/Agent尾仍可执行，不隔离为终态。
- arXiv错误日路径`/list/cs.CL/2026-05-13`返回invalid period；`/2605`返回invalid year；已恢复`/2026-05?show=2000`官方月列表（CL2844、LG6573，当前首2000）。月宽列表仅作有界标题补检，未逐条处理，未宣布其分页已遍历；后续限定潜在May13ID段核主题，不用整月条目补队列。

## A4. INSET 必要Source / owner比较 / 最小逐字稿（待root独核）

### A4.1 实际必要证据

精确原件：`sup-raw-20261019/2605.12305v1.raw`（148287 bytes，完整HTML），已实际读 §3.1–3.3、§4.1–4.5、Tables1–2、Figure2–7 captions 与结论。准入后按具体Ch23 gap深入受影响域，不遍历参考文献或无关实现。

- §3.1：BAGEL式理解/生成双Transformer支路；参考图的semantic ViT features在指令对应短语位置展开，不在开头集中放图再靠编号回指。另删除输入图VAE features以减少copy-paste；这与位置机制是两个可分别比较的选择，不混为“原生token就优越”。双阶段guidance先增强文本相对visual-only的影响，再全局CFG；不能把图像/文字差异全归布局。
- §3.2：10M静态图合成（global caption、instance mask/caption、LLM重写+图文mapping）与5M视频源帧crop→目标帧状态变化配对；视频构造显式过滤近静态样本，使identity与state change分开学习。合成质量和过滤仍是依赖，不认证真实grounding。
- §3.3/4.1：InterleaveBench参考实体来自DreamBench++，2–5张图、人工过滤指令；图像一致性1–5归一化，文本一致性预生成binary VQA，均Doubao-Seed-1.6评。Baseline需重写为image-first/indexed格式，跨模型/闭源主表并非机制隔离。
- §4.1：BAGEL 7B+7B初始化，除VAE外full FT；image/video/edit/T2I sampling `0.2:0.2:0.1:0.5`、AdamW β=.9/.95、LR2.5e-5、50k steps、最大1024分辨率、每rank约30k序列、shift3.0。GPU/精度/batch/并发/运行SLO及重复seed不披露；本工作不是serving benchmark，不补填硬件。
- §4.5/T2明确image placement比较使用同一训练数据；Image First总体image/text=.86/.66，INSET=.93/.75；w/o video=.91/.60，w/VAE=.82/.56。支持受限多图下布局/数据/feature选择分责，不证明任一单因素解释全部主表收益。
- 反侧：§4.3/T1全文承认对闭源text consistency仍偏低（INSET overall .75，对GPT4o .81、Seedream4 .85），image metric较高不等任意指令更好；对象数2–5不证明无界长指令/长图组。未给真实多样部署、production safety、通用semantic-locality theorem或独立复现。HTML仅有他人FLUX引用库，未把它冒充INSET artifact；未核代码。

### A4.2 实际owner与完整局部邻接

已加载Books三公共文件、ROADMAP及LS；实际比较Ch23“阶段三/阶段四”375–438、“Shared self-attention”781–848全部局部论证与“Native3D”1487–1513；并核Ch22结尾交接与Ch24开头。现有Shared首段已经要求mask/position/type/packing、强调打包邻近≠语义邻近；后接query-conditioned mask辅助监督、二次读点云及channel索引对应，不承载**参考图特征在指令内对应语义槽展开与image-first/indexed的可比较替代**。多图source index/RoPE段拥有图归属/坐标，不拥有指令conditioning布局，因此保唯一owner Ch23、只补一局部段，不改Ch24生成过程或Ch27数据细节。

### A4.3 拟逐字正文（一段）

建议插在Ch23 Shared self-attention首段之后、辅助空间监督段之前；marker `SF-2026-ARXIV-2605-12305`：

> 当一条生成指令同时引用多张图，输入的线性化顺序本身也是条件化设计。把参考图集中前置、再让文字按编号回指，易于复用原有接口，却要求模型跨较长距离完成对象与属性绑定；另一条分支在对应文字短语附近展开参考图的语义特征，让视觉内容直接占据指令中的语义槽。这里改变的是参考条件的读取布局，不认证图中对象、关系或后续生成结果。此选择还应与输入feature和训练支持分开：删除像素级VAE条件可能减少直接粘贴，视频跨帧配对则训练保留身份并改变状态，二者不等于位置调整的免费附带收益。[INSET的受限BAGEL对照](https://arxiv.org/html/2605.12305v1#S4.SS5)在相同训练数据的image-first消融中支持布局分支，但仅测2–5张参考图及作者judge，文字一致性仍低于部分闭源模型；合成数据、全参数适配与guidance都计费，不能由局部图像一致性推出通用长指令优势。布局或质量未验时，保留显式图编号、较少参考图与原条件化路径。

拟本人Review note：`SF-2026-ARXIV-2605-12305` — Daily05-14补May13；exact-v1 §3.1–3.3/4.1/4.3/4.5/Tables1–2，2+1+2=5，指令内视觉语义槽vsimage-first具体gap受影响域深入；保同数据消融人口、ViT/VAE与video变化分责、闭源文字反侧、合成/FT/guidance全费及有限2–5图/judge，不授通用绑定/真实grounding或SLO，未核实现/复现。root必要Source/逐字PRE与实际POST尚待。

## A5. TanStack 必要Source / owner比较 / 最小逐字稿（待root独核）

### A5.1 实际必要证据与时间分责

官方RSS本日原件给May13 00:00Z，2026-05-13BJT。已实际读官方全文“what happened”及FAQ的受影响凭证、部署中预防配置与notarization/撤销边界；当前页面June26 amendment显式标后修订，采用事件的Jun12原段与current amendment分开，不以当前页面证明May13每字内容。

作者披露两个设备，受影响repo含产品签名材料，成功外传仅有限凭证；隔离设备/身份、撤会话/轮换repo凭证、限制deployment、block旧证书新notarization与检查既有notarization/发布制品。仍有效的旧notarization和迁移到新证书的客户端是不同对象，因此延迟完整撤销以避免合法更新被破坏，且声明若出现滥用可提早撤销。minimumReleaseAge等控制当时仍分阶段部署，两设备未覆盖。没有公开独立forensic报告/全量攻击数据；“未发现customer/code影响或恶意签名”仅厂商调查边界，不是全局无侵入证明。没有性能benchmark，模型/精度/并发等不适用；当前具体客户端版本和改期不进入Books。

### A5.2 owner / 邻接与差额

实际读Ch72 Supply-chain1209–1268全部局部（来源/限制lineage→requirement→optimization→prompt）、“从文件哈希到可执行来源链”2638–2664，以及Incident2267–2275，并核Ch71末交接/Ch73开头。现有2638段承载registry/namespace/发布者签名，但没解释**签名材料自身暴露后阻止新签发/公证与允许旧合法制品迁移的不同边界**；Incident段是通用逐步remediation状态机，未有发布信任迁移具体分支。拟Ch72 Supply-chain标题下新增一段（lineage正文之前），不重写现有签名或incident原则。

### A5.3 拟逐字正文（一段）

> 发布者签名与发布链的可信性也要分开：合法签名能证明某个key参与了签发，不能证明持有该key的开发环境没有被上游依赖污染。签名材料可能暴露后，阻止旧key产生新的可信发布、核查已签发制品、让合法客户端迁移到新key，以及最终撤销旧信任，是不同的处置阶段；立即撤销可能切断正常下载与更新，延迟撤销又保留残余风险，需由事件证据和平台方约束决定。[OpenAI披露的TanStack事件](https://openai.com/index/our-response-to-the-tanstack-npm-supply-chain-attack/)中，停止新的notarization、复核既有记录与证书轮换并用，且预防性配置当时尚未覆盖所有员工设备；控制已开始部署不等于全资产已生效。这里保留的是发布信任迁移与防护覆盖的边界，不把厂商“未发现恶意签名或客户数据影响”升级为无妥协证明。新增制品核验、客户端兼容与迁移监测均有成本；覆盖或取证不完整时继续隔离、限制发布并保留人工incident command，原有来源校验和最小权限仍须共存。

拟本人Review note：`SF-2026-OPENAI-TANSTACK-RESPONSE-MAY13` — Daily05-14补May13；官方RSS/原事件核心/当前amendment分责，2+2+2=6安全约束必要深入。仅采用签名信任分阶段迁移与防护deployment coverage，保厂商调查边界、可用性代价和独立取证缺失；不采当前改期为历史事实、不授无妥协/平台通用安全，未核实现/独立复现。root必要Source/逐字PRE与实际POST尚待。

### A5.4 独立纠偏：具体已有覆盖，A5.3提案撤销

root实际检查Ch72 **1280–1316** 后发现作者A5.2漏读同一Supply-chain节的后续具体正文；作者现已实际完整读回该段。1306前后的TanStack end-to-end恢复链已经列dependency/device→credential/repository→artifact/signature→revoke/rotate/rebuild→client upgrade/quarantine→residual risk；其后Axios两完整段明确分开build/sign能力，并已经解释block新notarization→新证书→迁移→最终撤销、立即/延迟代价和Unknown。这正是A5.3拟重复之机制，不是只主题相似。**A5.3逐字稿与本人Review note不执行，Ch72本项不写。** 6分/安全必要深入完成保留，Books改判`已有覆盖—PLATFORM-SECURITY`，本次只提供防护分阶段未覆盖两个设备这一受限个案验证；不据此降分或删候选。以rootR2为独立Source/具体NC依据，原有效内容不变。

### A4.4 INSET实际窄写（待POST）

root实际必要Source、当前Shared首段/完整辅助mask双段及Ch22/24交接后通过A4.3逐字PRE，授权该唯一位置一正文段+本人Review note。作者已实际保存Ch23 **786正文 /1857本人注**，完整读回Shared首段、新段、辅助mask后双段及本人注，限定diff-check通过；root非writer实际POST尚待，未先计生效。

### A4.5 INSET实际POST通过

root R3已实际非writer读取保存的新正文、完整两侧与本人注并POST通过，Ch23窄位释放。当前本次已生效 **1整合+1具体已有覆盖**（INSET/TanStack）。作者只行政同步本人注既成状态，不对其他正文加写。

## A6. 后续具名准入（题摘层，不是原池重跑）

首批校准后，对本日主题标题中八条具名线索定点核题摘。旧163候选事件已去重，以下未在旧候选表；仅为确认重复/处置层，读取旧05-13 ledger同ID并发现前六在`revision_or_non_owner_route_isolation`，并无有效Source/Books，不能冒充已审重复。其generic“无跨层SLO/owner重新分配”“只有task/evaluator”理由不承载当前贡献门槛；具体重新检查的是下面机制，不扩查其全部191隔离项或484关闭项。

| 精确身份 | 已读题摘的约束→实际增量→选择 | 评分提案/下一步 |
| --- | --- | --- |
| `2605.11125v1` Language Modeling with Hyperspherical Flows | 连续FLM在vocab维one-hot上流动昂贵且欧氏噪声无语义邻域 → 小维unit-sphere embedding沿切向velocity旋转、CE训练 → 选择latent几何/生成路径，并需在可验证reasoning而不只GenPPL检验；v1完整题摘实读 | 2+1+2=5；标准必要方法/评价及低温反侧，date原件已取待核 |
| `2605.11134v1` Spurious Correlation Learning…Tie Training | 偏好数据更多可能不消除虚假特征 → log-linear人口目标中mean bias与causal-spurious correlation两通道、equal-utility tie正则 → 需要改变数据对构造而非只扩量；v1完整题摘实读，不把log-linear定理外推任意LLM | 2+1+3=6；标准理论假设/结果与neural反侧；若纠正具体owner论点再深入 |
| `2605.11215v1` ReCoVer | 故障后降DP/重启可能改变microbatch和梯度轨迹 → fault-tolerant collective+step内恢复+survivor quota保持每iteration microbatch → 并行调度与统计训练语义联合验收；v1完整题摘实读 | 2+2+3=7；深入协议不变量/故障注入对照/不支持范围，date原件已取待核 |
| `2605.11222v1` ADMM-Q | greedy GPTQ在sub4bit可能reconstruction差 → combinatorial ADMM连续重建与离散量化分裂、penalty/precondition/local-search → 量化内层solver与外层rotation/scale解耦比较；v1完整题摘实读 | 2+1+2=5；标准solver/收敛假设/同设置表，不能用单PPL准入数字代替机制 |
| `2605.12070v1` Missing Old Logits… | 异步partial rollout丢historical train logits，使train-infer discrepancy与policy staleness ratio混合 → snapshot/dedicated old-model/interrupt三exact路线与approximate EWMA → 明确选择保历史状态还是近似修正；v1完整题摘实读 | 3+2+2=7；深入ratio语义/实现tradeoff/approx反侧，不把后版标题摘要套v1 |
| `2605.12227v1` Combining On-Policy Optimization and Distillation… | SFT exposure/sparse GRPO/dense OPD目标不同 → dGRPO在student rollout并用outcome advantage与teacher dense指导 → 调整训练目标而非仅增加长上下文数据；v1题名与后版不同，已实读v1完整题摘 | 2+1+2=5；标准确切loss/独立组件消融/short-context反侧 |
| `2605.11869` FIS-DiT | few-step时step-cache机会耗尽 → frame interleaving跨层刷新不同frame subset → 帧维稀疏而非增加step reuse；当前摘要完整实读 | 暂为待准入事实：需精确v1题摘与日期，不评分/不展开Source |
| `2605.11887v1` Qwen-Scope | 官方SAE release覆盖四种model-dev用途，但题摘主要是suite与既有操作归纳 → 尚不清楚新增机制/可修正边界 → 只补决定准入所需关键说明 | 尚不评分，不因机构release自动候选；不为库目录全读代码 |

原共同generic理由仅是局部重开线索，不将所有旧排除判错。新事件日期未核前不进入确定候选表。

### A6.1 root后续校准与六日证实际通过

root R3实际逐读前六精确v1全题摘/history及同DOI DataCite；11125/11134/11215/11222/12070五项按5/6/7/5/7准入通过。六个精确v1提交均在May11 18Z后至May12 18Z前，结合公告下界May13 08BJT与findable/arxiv.content登记最晚界，均限定同一May13自然日：11125 registered02:17:11Z、11134 02:17:24Z、11215 02:19:23Z、11222 02:19:33Z、12070 02:40:29Z、12227 02:44:18Z。原字段在本日对应DataCite原件，未把submitted/updated字段冒充公开时刻。ReCoVer的microbatch数恒定并非无条件梯度等价，须核AppendixF。

12227不先入选/评分：root要求只补loss及对应消融决定准入，不能因GRPO+teacherOPD和新LongBlocks自动P，也不能仅因组合自动C。作者已实际定点读精确v1 **§3.1/Eq6、§4.3/Fig4–6**，未扩全附录：Eq6就是标准clipped GRPO outcome项减student-rollout前缀的teacher reverse-KL，原文明确承认Agarwal2024已提出RLHF+OPD；Fig4同SFT warmstart/同RLbudget支持该任务中两项并用更稳定，Fig5更强external teacher优于self teacher，Fig6 β=0至.5范围最高在.5。它没有额外的状态耦合、longcontext特有阈值/恢复机制，所谓“峰值”也是所测区间右端，不证明可复用最优β。**提请具体C**：新增是该LongBlocks/有限模型组合的受控验证，尚未显示改变既有dense-teacher+outcome设计或成立/失效边界；新数据/任务和更好曲线本身不足长期增量。不因已有Books主题覆盖、访问或工作量关闭；root待独核该小域裁决。原A6的5分仅作者提案，未生效。

## A7. 11125 / 11215 必要Source及具体owner差额（待root）

### A7.1 球面FLM 11125（5分）

精确v1 HTML已实际读§3–4、§7及B.6；不是摘要补写。§3中每token用learned unit-normalized codebook、uniform-sphere噪声经SLERP到目标；单纯velocity MSE可使learned endpoints塌缩，故用CE学categorical posterior，再以posterior权重混合各endpoint的切向log-map速度，solver后argmax。Exact/stochastic/top-k是速度近似分支，posterior本身仍为learned approximation。High-dim早期one-hot collapse促使截断噪声区间；阈值Eq16依random spherical codebook，只是principled heuristic，不是已学embedding的严格最优阈值。adaptive schedule与S-arch另付费、不混为几何唯一收益。

评价：Sudoku48k/2k、8层512dim、180步；TinyGSM约11.8M合成→GSM8K执行生成Python验证，12层768dim、250k步batch512；OWT12层1M步，GPT2 tokenizer/context1024。T=1/1024steps时top1 18%追平MDLM，但T=.1时MDLM/Duo33–36%、本法约18%，ARgreedy63.3%，所以不是平替。OWT GenPPL–entropy Pareto仍Duo最好，不能由GenPPL推出推理正确。B.6：BF16、TinyGSM8H100/OWT16H100，S-arch更慢且GPUh高于vanilla；单run，bootstrap仅testpopulation不是重复训练不确定性。未核代码/复现，不采生产speedup。

实际Ch24 §“球面路径”419–421已覆盖SLERP/tangent/exponential-map的一般几何；§“连续文本”560–570已覆盖CEposterior/噪声预算及one-hot支持。**最小差额不是再讲球面更好，而是learnable spherical token endpoints下CE→posterior加权切向速度，保持训练/采样/离散读出接口，并把高维早饱和与heuristic truncation分开。**拟只补连续文本局部一段，Source和实际owner独核未授写。

### A7.2 ReCoVer 11215（7分）

精确v1实际§4.1–4.4/Alg1、§5、A.1和AppendixF完整证明域。ULFM agree/shrink只处理membership，不保证失败collective buffer，须bucket pre-reduce snapshot+monotonic world epoch rewind，再按统一membership重约。minor/major/spare在每iteration贡献数之和保持B、用同B归一；不是只改DPsize后让survivors平均。TP/PP或FSDP shard内任一rank失败使完整replica成为原子失效单位，至少一个**完整replica**存活，不是至少一GPU。

关键反侧：AppendixF明确**非step-for-step/bitwise复现**。等价依deterministic模型在给定θ下、disjoint且每iteration不重复的microbatch、effectively infinite且不lap的**exchangeable**数据stream；failed shard丢弃、survivor推进，只有该人口前提才可称换shuffle后同分布。非IID分区、failure与数据相关、重复/遗漏或优化器状态不可信时，B恒定不足够，须checkpoint。ULFM/MPI typed failstop不自动涵盖silent corruption/整个controlplane失败。

评价：C4/LLaMA-style7B，512A10040GB、128nodes×4、NVLink/Slingshot；初64replicas、GA128、B8192；260step loss对照，256GPU losses每5iter随机GPU的deterministic injected schedule，全部发生gradient sync。与checkpoint比较另用128GPU/32nodes、GA8，sweep N2–64且于interval中点注故障；effective tokens/(runtime×aliveGPU)不等固定容量aggregate吞吐，无故障时MPI与未overlap的损失保留。没有真实生产fault corpus或hyper-scale验证。论文appendix披露forkPyTorch2.9/OpenMPI5.0.8/Nanotron，但本次未核实现/复现。

实际Ch36 Failure段1042–1110已经覆盖SPARe完整原shard冗余、fail-tolerant reduction的survivor人口边界、FT-HSDP异步追赶及committed-step内存恢复。**具体差额**是不同于SPARe保留原样本的exchangeable replacement，以及failure-during-allreduce的bucket+world-epoch rewind、B-count/共同membership的联合条件。拟在SPARe与条件化reduction分支之间补一段（后者已有“允许失败贡献缺席≠保持原batch”可自然衔接）；未授写。

### A7.3 两项最小逐字PRE（待root）

11125：Ch24现LangFlow两完整段之后、bitstream段之前；已实际读其连续文本552–571完整两侧、较前球面段及Ch23结尾/Ch25开头交接。拟一段：

> 连续文本的端点还可以与生成器一起学习，而不展开成词表维one-hot：每个token映到单位球面，以SLERP构造噪声到目标的路径，用交叉熵学习categorical posterior，再以这些概率混合通向各token端点的切向速度，最终离散读出。这不同于直接对可学习端点回归速度，后者存在端点塌缩的平凡解；posterior加权仍是学得的近似，不能称真实分布已精确恢复。高维球面上posterior可能很早变尖，因而可截断训练噪声范围，把预算留给更含糊的状态；由随机codebook推导的阈值只是启发式，不是已学embedding的通用最优点。[受限语言Flow对照](https://arxiv.org/html/2605.11125v1#S3)改善先前连续方法，但低温下仍明显落后离散diffusion与AR，球面backbone还增加训练时间。Codebook、schedule、速度近似与完整solver都须连同质量/多样性验收；预算或质量不合适时，保留欧氏latent、离散diffusion或AR，不从球面几何推出语义、推理或速度普胜。

拟本人注：`SF-2026-ARXIV-2605-11125` — Daily05-14补May13；exactv1 §3–4/7/B6，2+1+2=5，小差额受影响域深入。只采learned spherical token endpoints/CE后验加权切向速度与截断资格，保random-codebook heuristic、低温/AR反侧、单run与完整训练/solver费；不授精确marginal、通用语义或加速，未核代码/复现。必要独核/实际POST待。

11215：Ch36现SPARe两完整段/marker之后、survivor reduction段之前；已实读1042–1110完整故障局部、Ch35末交接与Ch37开头。拟一段：

> 若训练合同允许保持统计分布而不要求补回失败分区的原样本，另一条分支可给幸存完整replica重分microbatch配额，使每次optimizer更新仍接纳B项并按同一B归一。数量不变还不够：发生在all-reduce中的故障可能留下不同membership的部分和，须保存bucket归约前快照及world epoch，回退受影响bucket，再在共同成员集合下重新聚合。[ReCoVer的受限协议](https://arxiv.org/html/2605.11215v1#S4)把这两层联合起来，spare先执行但不贡献梯度，必要时晋升或增加幸存者工作；其同分布主张还依赖可交换、未循环的数据stream与不重复计入，不是重现原run的每步或bitwise轨迹。它增加快照、冗余计算、失败共识和重约费用，MPI后端与失去overlap也可损无故障效率；按alive GPU归一的有效吞吐不能替代固定集群总吞吐。非IID分区、故障与数据相关、silent corruption或已无可信完整replica时，B恒定不能授权继续，仍须恢复可信状态或回committed checkpoint。

拟本人注：`SF-2026-ARXIV-2605-11215` — Daily05-14补May13；exactv1 §4/Alg1、§5/A1.1/F，2+2+3=7。只采共同world-epoch bucket rewind与B贡献配额、exchangeable replacement分责，保完整replica、无限不lap/disjoint条件、非bitwise、注入failstop人口及alive-GPU归一口径/总费，不授非IID或任意故障等价，未核实现/复现。必要独核/实际POST待。

## A8. 11134必要Source与理论/表格反侧（待root）

精确v1实际读§3–7/H及F.3受影响LLM消融。Log-linear local-small-margin、feature causal/spurious分解、moment/Schur可逆条件下，Eq5把population spurious方向分为均值bias与cross-cov leakage；更多同人口样本只降低estimation，若population bias仍在则不消除shift风险。Tie construction以equal-utility、Δcausal=0、spurious有variance、randomize双方向labels，使额外curvature只加spurious block；near-tie质量与可得性仍是依赖，非无需oracle。

**不照录无条件保证：** theorem4.1的“μs≠0或Σcs≠0就必θs≠0”过强，Eq5两个项可抵消；正文6.1“causal更新不变”也不能从额外block-curvature推出，因为Σcs耦合令θc随θs变化。这里只采两通道与合格tie的数据构造，不能说任意tie都去偏/不伤causal/任意shift误差必降。理论假设、给定utility与自然真实utility不同，H明确规模与tieoracle限制。

F.3是Llama3.2-1B-Instruct/LoRA单epoch合成hotel，informative random_extreme与standard_monotonic近零spurious variance为关键正/失败对照，30%ties；预算/precision/hardware与seed数未具体披露，不能补造CI。T2 strict-suppressed总体74.00低于两个option子集74.48/77.81，简单weighted平均无法解释，不采用精确总体提升作强证；IND HotelA从89.54→88.02下降，不能说所有子群无损。受限反转/压制相关下的方向改善与noninformative无收益支持构造资格，不授生产普胜。

当前Ch34已有pair来源、label/generator residual校正与selection coverage，但尚未实际对读完整局部，不提前宣称gap/NC。候选6分保留，因理论/表格反侧深入受影响域，未靠降分或generic争议删项。root需独核拟采用的窄机制及中心争议是否应只报告/暂缓。

## A9. ADMM-Q 11222（5分）必要Source / owner / 逐字稿（待root）

实际读精确v1 §3.1–3.6/Alg1、§4.1–4.2/T1–4、§5限制、AppendixB完整refresh和D必要设置/成本/消融T5–7，未为收敛命题扩读完整C证明。局部Hessian-weighted layer reconstruction+ridge，diagonal precondition后由连续W-update（H+ρI的分解复用）、quantized D-projection和dual V更新组成；T300/ρ增长与最多5轮pair local search增加离线成本。§3.6的收敛只解释满足惩罚schedule下iterates/feasibility，不采用global optimum或所有动态grid保证。

关键refresh：旧grid来自denseweights，continuous target移走后可重拟grid；AppendixB只接受不增当前D-update距离的refresh，同时补dual，并**至多一次accepted refresh**。不能泛化为任意多次改scale也不影响收敛。Rotation/activation/KV路径不变，只换weight quantizer；nominalbit与runtimekernel仍另验。

评价：Qwen3 1.7–32B weight-only，Qwen/Llama1B/8B的SpinQuant W2/3/4A4KV4及SmoothQuantW2/3/4A8；WikiText2/C4/PTB和9-task lm-eval。Calibration代表性/Hessian近似是限制，仅denseAR，不含MoE/diffusion/ViT。W4 Qwen8B的PPL更好但0shot68.14<68.93GPTQ，Qwen32B .6914<.6998，T6无local search W3 WikiPPL9.93优于full10.06，不能说各组件每项有益。T5离线32B117.73min对GPTQ33.97min，GPU峰也更高。GPU环境范围L40/A100/H100/H200、具体每行卡未绑定，不补造同型号服务速度；Serving T4仅W8A8、2000Wikitext sequences/batch100、800prefill+256decode、same-node，并且GPTQ/本法近同speedup，不能拿W2质量结果签低bit kernel或推理更快。未核代码/复现。

实际Ch49 PTQ/QAT1119–1144完整局部与二阶1467–1510完整局部已读：已有diagonal weighted scale regression、顺序GPTQ residual补偿与SchurReplay，未覆盖joint continuous/discrete solver或其有限refresh-state consistency。拟唯一owner `INFER-TENSORRT-LLM`，在diagonal收缩的两完整段之后、现“二阶近似也不必与更新策略一起冻结”之前插一段（本段与原顺序方案共存），待root核窄位，不先写。

拟逐字正文：

> 校准曲率既定后，求解量化权重也不必逐列永久提交。另一条离线分支把全部连续权重与量化副本拆开：前者降低Hessian加权重构误差，后者投影到离散网格，以dual更新协调二者，再作有限离散局部搜索；这允许重新考虑早期的联合舍入，却增加矩阵分解、迭代状态和准备时间。[ADMM-Q的受限实现说明](https://arxiv.org/html/2605.11222v1#S3)还区分continuous target移动与grid更新：其refresh只接受当前投影目标不变差的网格，并同步调整dual，至多接纳一次，不能解读成任意改scale仍有同样收敛保证。局部可行性或重构更好不等全模型最优，部分任务与消融仍反退；同量化格式的线上执行速度也基本不因离线solver改变。校准代表性、数值条件或准备预算不足时，保留顺序GPTQ、简单舍入或较高精度，并让最终artifact单独通过质量与kernel验收。

拟本人注：`SF-2026-ARXIV-2605-11222` — Daily05-14补May13；exactv1 §3–5/Alg1/T1–4、B/D必要域，2+1+2=5，joint solver/有限grid-refresh具体gap深入。保at-most-one acceptance/dual consistency、局部feasibility非globalopt、W4质量反退、离线时间/峰memory与W8A8 serving口径分责，不授低bit现成kernel或线上增速，未核实现/复现。独立Source/PRE/POST待。

### A8.1 root实际中心争议裁决

root已实际读§3/4/6、5.4/7、F.3必要表/模型训练及H，确认Eq5抵消、Σcs耦合与T2总体/子组矛盾。保6分候选、受影响域深入完成，Books为**暂缓—中心争议**；不绕过中心矛盾只摘一般tie构造制造新段，也不外推所有tie方法无效。重新采用需要更正的充分假设/命题、可核原始分组与重复结果；争议项不进入Books或正面性能保证。

## A10. Missing Old Logits 12070（7分）必要Source / owner / PRE（待root）

精确v1已实际读§3–6，另定点§6.4/6.5、B/H；未因HTML尾扩读全部附件。μ_v是inference behavior，π_v是同weights版本的training forward，二者不保证同policy。总比值π_current/μ_old可拆成π_current/π_old（staleness）与π_old/μ_old（train-infer discrepancy）；partial rollout跨多个更新时历史π_old缺失，任意proxy虽代数消去，两个分量却不再各自具有所称语义，改变mask与clip的实际边界。

三条精确恢复路线分别是：保历史snapshot并reload到trainer；独立old-model资源同步历史版本、流水求值；更新前interrupt所有partial rollout、在尚驻留旧trainer上补logprob再恢复。它们分别增加历史状态/IO切换、resource partition/通信、同步停顿和进度干扰，不可把oldlogits当免费metadata。EWMA参数模型是近似而非historical mixture；β≈W/(W+2)是center-of-mass匹配，不是最优证明。active-token fraction在mask/clip后低于.9则reset当前policy只是所测heuristic，mask/clip即使有精确oldlogits也仍需联合校准。

评价限Qwen3-4B/30B-A3B、τ² retail/airline/telecom与Vita instore/delivery；max version lag3，尽量无额外epoch staleness。ROLL基线及任务split公开，完整hardware/precision/resource/hyperparameter未披露，不补造SLO。专用old-model在1:2资源比的overlap284比single305快，但1:3时254比237反慢，不能从overlap功能推出全程净收益；EWMA不reset会失败，snapshot也非所有任务最高分。没有重复CI与完整端到端资源归因；作者代码链接存在但本次未核实现/复现。

实际owner比较：Ch32“为什么需要旧策略概率”213–255已完整读，定义current/old ratio及implicit-density/reuse人口；训练迭代367–390也明确oldlogprob不能用新模板覆盖。Ch33 1733–1788完整policy identity局部已有checkpoint/precision/scale/kernel identity与特定clip接口，因此**不再补一般train-infer不同**。新差额只在Ch32单一ratio释义之后：historical training density与实际behavior的分工、partial rollout下精确恢复三路线，以及proxy因子不继承纯staleness/discrepancy解释。拟唯一`TRAIN-PPO`，不抢Ch33运行时身份owner；尚无授权。

拟在Ch32“当rho_t=1…”完整段之后、现“这个写法要求能够计算action的policy density”之前补一段：

> 旧概率还要说明来自哪条前向路径。同一weights版本的training policy与实际inference behavior可能因数值路径不同；总current/behavior比值可拆为current/历史training与历史training/behavior两项，分别观察版本陈旧和两栈差异。异步partial rollout若跨更新，保存behavior log-prob并不等于保存每段历史training log-prob。[Missing Old Logits的受限对照](https://arxiv.org/html/2605.12070v1#S4)比较保历史snapshot后重载、独立old-model求值、更新前中断partial rollout并补算三种精确路线，分别支付状态与IO、专用资源、同步停顿费用。若改用当前或平滑policy作proxy，两个因子虽仍代数相消，其单项已不再是纯staleness或纯train-infer discrepancy；由它们决定的mask和clip也会改变。EWMA参数平均不是历史policy分布的精确混合，经验reset阈值不是有效性证明；质量、版本归属或净费用失准时，保留可核历史density、收紧异步窗口或回同步rollout，不由可计算比值签发无偏更新与普遍稳定。

拟本人注：`SF-2026-ARXIV-2605-12070` — Daily05-14补May13；exactv1 §3–6/B/H必要，3+2+2=7。只采historical training density/behavior分责、三精确恢复路线与proxy分解语义，保EWMA/reset启发式、mask/clip耦合、resource-ratio反退与完整费用；不授无偏或生产普遍收益，未核实现/复现。独立Source/owner/PRE/POST待。

## A11. 机构有限恢复差额（继续执行）

Qwen：一次猜测`/api/v2/article`请求超时，不把猜测当真实入口。随后实际从主页已观察969.js的44467模块取得`cy=/api/v2/article/retrieval`，39759 axios没有baseURL，p_home-index调用的type=qwen_ai/language=en-US已核；fresh同源GET实际success=true，40条`data.articles`，原件`qwen-retrieval-en.json`。已逐读40条date/path/title，目标相邻Apr30 Qwen-Scope→May19 LiveTranslate，无May13条目；无分页字段，只签本次en-US投影，不签历史未删/全目录无遗漏。动态浏览器先前65秒超时并重置，必要公开接口现已恢复，不沿用May06完成结论。

11887出现具体早稿线索：Qwen-Scope API extra.date为Apr30，但内嵌官方canonical旧HTML article:published_time/JSON-LD为Apr29 12+08，四用途/14SAE/7models与本日题摘核心同；正文直接链接`https://qianwen-res.oss-accelerate.aliyuncs.com/qwen-scope/Qwen_Scope.pdf`。已完整读该官方核心说明，尚需只核此具名PDF是否同完整稿及早稿资格/本次独立增量；不以当前mutable日期直接授完整稿Apr29已公开，也不直接把May13 arXiv当首次公开。

Seed：fresh`get_article_list_v2` page_token20/count20，`x-tt-locale: US`取20条并到May10/May7后停止（next40不翻）。无locale时异常只返回Apr22一条，不能当目标覆盖。精确1621/MMProLong元数据PublishDate1778601600000为May13BJT，完整官方摘要已读：7B 32K→128K，长文VQA对OCR、balanced-length对target-length、retrieval-heavy配比与少量reasoning、instruction-format长文保短能力，是具体训练recipe/成立条件，不因新任务关闭。其13831v1论文公告在May14BJT是不同事件；须核官网是否只有摘要、以及本日摘要事件可由哪些完整方法/评价支撑，不能只用窗外论文日期把摘要事件写无贡献。

11887具名PDF已取并只读前2页身份/目录：标题/完整摘要与本日v1一致、35页，封面明确2026-04-30，CreationDate/ModDate均Apr30；metadata不是公开证据，但与官方旧dated blog直接PDF指针组成具体更早完整稿线索。正文包含§2–9全部四用途而非宣传sheet；只为身份恢复，不先声称所有必要Source已审。本机pdftotext缺失、默认Python无pypdf，已用产品内置依赖只读取该PDF，未安装包/写公共工具。待root确认早稿资格，不因访问/机制已知自动C。

## A12. 多模态主题的有限准入题摘（待独核，不是全文队列）

本日多模态API52条主题标题只作线索；旧291家族去重后，从模型表示/生成/World/VLA具体机制选择22条完整题摘阅读，不将52或所有月列表变成逐项关闭义务。下列原始题摘在本日对应feed/current页面；存在后版者现已补读精确v1（11367/11459/11567/11596/11817/11871/12163/12271/12325/12369），不以v2/v4反填v1。没有撤回/勘误信号；12271与12369等后版版本号不单独构成新修订队列。以下拟准入均只是待日期/独核的提案，未计Source完成；实验细节不足不是排除理由。

| 身份 | 完整题摘所载具体约束 → 增量 → 拟重新考虑的选择 | 拟评分/处置 |
| --- | --- | --- |
| 2605.11107v1 Birds… | CLIP/SigLIP前景/背景shortcut难分 → 在控制合成pretraining中检测线性additivity并分离foreground/background影响 → 修正VLM spurious-feature归因及是否必须非线性解释；不把合成结果当真实debias | 2+1+2=5，待独核 |
| 2605.11367v1 3D-Belief | 单一未来图像不表达部分观测不确定性 → 显式3D多假设belief与sequential update → 选择可供navigation消费的belief而非只render；摘要没有具体update方程，先补决定性§3而不直接全Source | CLARIFY，不先评分 |
| 2605.11459v1 Pace-and-Path | action chunk修正混合速度与路径偏移 → 以正交二次目标分离沿路径速度与空间offset → 可选有限低层chunk后处理而非重训VLA | 2+1+2=5，待独核 |
| 2605.11479v1 Discounted Liveness | VLA离线value对长程termination风险不易校准 → conservative Bellman固定点与有限horizon truncation给discounted liveness → 判断可用离线policy-evaluation标量的资格与失效 | 2+1+2=5，待独核；证明假设须核 |
| 2605.11567v1 Dynamic Execution Commitment | 并行draft action不等都可执行 → 组内一致性选择候选、低共识时conditional-invariance验证并仅提交连续verified prefix → 调整chunk commit horizon；共识非物理安全 | 2+1+2=5，待独核；v1仅将来release代码 |
| 2605.11596v1 HorizonDrive | teacher-forced历史使流式rollout误差累积 → 在corrupted prediction history上训练SRR teacher，再长horizon distill到bounded-memory student → 把teacher可rollout性先于少步学生 | 2+1+2=5，待独核 |
| 2605.11616v1 AFFORDMEM | frozenVLM小区域affordance与inscene空间查询不足 → RGBaffordance exemplar与场景3Dgraph双层memory → 是否具有新更新/消费边界而不仅拼已有memory组件尚不明 | CLARIFY，先决定性机制，不先评分 |
| 2605.11808v1 ARS/RVE | LVLM对对象relation有hallucination，现attention未必关注关系证据 → relation-sensitive heads/区域增强视觉编码 → 根据关系判断需求重分感知支持；不是VLA action-policy，sensitivity未自动是因果责任 | 2+1+2=5，待独核 |
| 2605.11817v1 GridS | discrete视觉token pruning难端到端且破坏空间支持 → 连续salient coordinates/differentiable interpolation → 学习采样网格替代硬pruning；<10%只是摘要配置 | 2+1+2=5，待独核 |
| 2605.11871v1 h-control | hard-replacement相机guidance与prior难平衡 → 同noise-level上unobserved complement的block-conditional pseudo-Gibbs refinement并按patch混合指示freeze → 在观测条件采样而非仅调guidance；conditional-law保证须核假设/近似 | 2+1+2=5，待独核 |
| 2605.12038v1 OmniHumanoid | paired motion不足、unpaired embodiment含appearance混杂 → shared pairedmodel加unpaired adapter并branch-isolated attention → 将motion与appearance的训练人口/gradient路径分开 | 2+1+2=5，待独核 |
| 2605.12163v1 SCOLAR | 长latent CoT不必更多information，≥128×pool可能只等placeholder → full-hidden detransformer一次生成独立锚定visualtokens，配套3stage/ALPO → 重新考虑latent token监督/AR依赖而非只加长；因果归因与组件费用待核 | 2+1+2=5，待独核 |
| 2605.12167v1 MoLA | imaginedvideo rawframes到action信息冗余/缺因子 → pretrained IDM mixture提取semantic/depth/flow action latents → 选择面向action的imagined接口而非rawframe再规划 | 2+1+2=5，待独核 |
| 2605.12271v1 V2V-Zero | text serialization丢视觉spec的结构/字形 → visualspec page不是edit target，直接冻结VLM final hidden替换generator textcondition → 复用已有VLM条件空间开放spec输入而非重新训练图像编辑 | 2+1+2=5，待独核；attention质量不作因果证明 |
| 2605.12325v1 VIP | spatial DINO.txt仍有text ambiguity → alias expansion+visual-guided distill/saliency aggregate → 新耦合或失效条件尚未与普通组件组合分开 | CLARIFY，只补决定性机制，不先评分 |
| 2605.12369v1 GuidedVLA | actiondecoder靠隐式监督易用shortcut → 不同attention heads接受人工object/spatial/temporal factor辅助监督 → 选择显式factor specialization而非仅扩动作数据；不是training-free | 2+1+2=5，待独核 |
| 2605.12496v1 CausalCine | 多镜头streaming需要transition与boundedmemory → native shottransition训练、content-relevance KV选择、fewstepdistill分阶段 → 选择跨镜头状态保留而非固定window | 2+1+2=5，待独核 |
| 2605.12586v1 3DPrimitives | 直接spatial QA与同模型可生成spatialcode可能不一致 → CodeCoT后解析自身ThreeJS场景构成selfFT信号 → 比较表示/读出瓶颈而非把可渲染代码自动当真实空间truth | 2+1+2=5，待独核 |
| 2605.12587v1 TrackCraft3R | frameanchored videoDiT受pixel时间绑定 → referenceanchored dense3Dpointtracks、双latent/temporalRoPE LoRA对齐 → 复用video生成先验但替换运动坐标与conditioning接口 | 2+1+2=5，待独核 |

另三完整题摘的代表排除提案（不评分）：11363v1 PresentAgent2将research→slides→narrationvideo组织为single/discussion/interaction，未指出新execution/failure条件或控制机制，不以产品模式/benchmark自动准入；12053v2 Giskard将semantic statechart与kinematic MPC用于八平台，完整题摘未建立模型能力形成或foundation-policy接口的新增联系，不借纯控制场景反引Foundation主线；12090v1 World Action Models survey给taxonomy/overview，题摘无修正关键评价盲区或新的机制/反证，不因术语覆盖新owner。独核可按实际机制纠正，不能用这些代表排除声称全部52已证无贡献。

### A12.1 实际独立题摘校准

root已实际独读22条完整题摘：上列16个5分提案准入，通过层仅为机制/反证入口，不是全文证据；三CLARIFY仍只读决定性方法；三代表C题摘抽检通过。作者11808先前把LVLM relation误写为VLA/action，已在上表纠正，不能按动作policy扩读/写入。FIS11869精确v1题摘/history/date组合亦已root实际读准入5分，必要同设评价继续。11887具名早完整稿资格隔离，不假称无贡献。MMProLong为May13独立官网摘要公告5分候选提请，后到13831v1只能佐证已公告命题，不搬动论文首次正文日期、不引入未公告新事实；root当前待实际官网core核。

### A7.4 已保存两窄段与实际POST差额

按root R4授位，11125 Ch24现576正文/2403本人注、11215 Ch36现1077正文/1933本人注已实际保存；正文逐字A7.3、独立marker各一，self-read完整直接前后与本人注、限定diff-check通过。root现实际POST已通过11125并释放，其余注只同步既成状态。

11215新段自身通过，但root actualPOST在旧1258–1280发现`10501/11215`双binding compound段仍要求failure-free sample-order/RNG复现；不是只加新段可消解的矛盾。作者已实际读该两完整旧段/diagram/旧binding，旧独立11215注不存在（只有本次新注）。因此重开**该具体旧归因**，不推倒其他Source或全章审计，待A13最小纠正通过后完成POST。

### A9.1 ADMM-Q实际窄写（待POST）

root实际§3–5/Alg1/T1–4、完整B refresh、D成本/消融，及现Ch49两段diagonal shrinkage/后顺序补偿/SchurReplay与逐字A9通过，已授该唯一远端窄位。作者现实际保存1494正文/2538本人注，完整直接两侧/新段/本人注self-read及限定diff-check通过；未称完整C证明已核，未改May15另一窄位或其他段。root非writer actualPOST待。

12227 root已实际精确v1完整§3.1/Eq6、§4.3/Figs4–6后接受A6.1具体C：保同warmstart/预算的局部验证，不把直承既有teacherKL+GRPO写成新耦合，不评分/不列候选。

## A13. 11215旧compound归因矛盾的最小修正PRE（待root）

现Ch36“Compound Section”1251–1280完整局部已实际读：opening解释不同section参数规模/forward-backward/activation与配置差别有效；旧双binding内混入“failure-free run随机与梯度边界”、固定RNG/data identities、重放unfinished logicalmicrobatches及全轨迹sampleorder，不能由ReCoVer的exchangeable replacement证明。保10501对compound config的有效机制，去除11215这一处双binding/不支持的共同引用（本次新1077段保唯一11215），不静默删除一般配置/commit边界；替换双binding内两段和diagram为以下最小闭合论证，opening与后planner段不动：

> 更细的runtime先把每个compound section编译为已准入execution config，再把它们绑定到同一个iteration identity；重配置须遵守预先声明的训练语义，而不能仅按剩余工作量推断一次更新已经等价：
>
> ```text
> section graph + shape / activation profile
> → admitted per-section execution configs
> → declared logical microbatch and update contract
> → execute forward/backward sections
> → commit one optimizer step only after invariant validation
> ```
>
> 这样把性能计划接到更新语义上：planner可以改变placement、parallel degree或schedule，却不能静默改变effective batch、gradient归一或optimizer commit。若本次合同要求保留原sample order与RNG，恢复就必须另有能守住它们的证据；前文ReCoVer在可交换数据流下的同分布替换不能授权failure-free轨迹复现。Compound规划用section profile、plan epoch与状态检查换取不同section不被一套最坏配置绑住；profile漂移、算子含不可重放副作用、训练合同或状态无法保持时，回退单一静态plan与可信committed checkpoint。配置规划的受限证据不提供任意故障模型或bitwise equivalence保证。[Compound工作负载的受限依据](https://arxiv.org/abs/2605.10501v1)。

拟保10501 start/end原marker，移除11215旧start/end与共同末引，11215本次新注追加该纠正范围及actualPOST待；不改其他来源的Review notes。未获该纠正窄位前不写。

### A13.1 实际纠正保存与非writer POST

root授A13逐字窄修后，作者已实际替换两段/diagram并移除11215旧双binding与共同末引，保10501 config机制、其原binding、前opening与后planner；完整局部和本人注已self-read，限定diff-check通过，未新授10501证据升级。root R6现已实际非writer新1077段与其邻接、旧compound完整opening/替换两段diagram/后planner和本人注POST通过，Ch36释放。12070 Ch32实际A10原逐字段/本人注保存后，root R6完整新段/直接两侧/本人注POST通过释放；11222已R5 POST通过释放。当前真实有效为**5整合/纠正＋1具体已有覆盖＋1中心争议终态**，不是本日已DAY。作者只同步本人注既成事实，不重复原证/无变化段落。

## A14. BAP 11107（5分）必要Source / 日期 / 具体owner与PRE（待root）

实际精确v1 §3–5、F完整anchor反侧、J完整scene-retention反侧、M.3完整Waterbirds配置/重复与成本；未遍历全部13附录。原题摘中的linearadditivity不是新定理，真正采用的具体分支是两阶段：冻结teacher对同一个segmented foreground在K随机背景的composites求embedding平均/归一为实例anchor，student再将M新背景映到该anchor。平均前景/背景线性可加仅approx；LLN/iid给residual variance方向，非零共同背景均值经归一不自动证明任意任务纯前景或完美去bias，不能抄“strictly necessary”成普遍定理。

M.3：Waterbirds源CUB排除val/test重叠、Places365 50类背景；N5000/K10/M5，224²，batch128，30epochs，AdamW5e-6/wd.01/10%warmup+cosine；singleL40S/BF16，完整11routines/两个backbones约12GPUh，不是无成本pretrain。CLIP/SigLIP2 ViTB16，NICO++用CLIPConvNeXt-W。五独立顺序run的全局seed继续推进，含headinit/shuffle/composites随机性；CounterAnimal主表10run而F3run，各自保口径，不混成统一CI。

§4同data/composites与compute预算的CE control优于许多旧baseline，BAP在所测WGA多数进一步增益，但COCO95 SigLIP2 data-matched WGA76.2>BAP75.8，NICO Bike/Motorbike AVG87.2>BAP85.9，不能全优。T3一行AFR AVG56.8<WGA68.6的总体/最差子组关系不一致，不采该竞争行证明排序；BAP自己的anchor/scene反侧与关键CEcontrol仍可有限采用。F随机正交classanchor在ID仍WGA90.2而CounterAnimal11.7/7.1，表明压背景不等保OOD语义；该ablation同时把实例anchor改为两class targets，不能当单因素严格necessity。J背景场景辨别严重退化，如ocean.81→.01，backgroundinvariance是牺牲背景读出的任务选择。§5只适用可空间分离的shortcut，object内部spurious不能由此处理；mask粗糙/背景分布仍是依赖。未核代码/复现，不把gender伪标签当人类属性真值，不引科学应用。

日期：官方topic-multimodal原始Atom精确ID v1、published/updated=`2026-05-11T18:13:05Z`（原v1提交字段），晚于May11 18Z cutoff；最早May13 08BJT。同DOI `10.48550/arxiv.2605.11107`、findable/arxiv.content、registered=`2026-05-13T02:16:44.000Z`最晚May13 10:16:44，联合整区间同May13，不把Atom published改称实际公开时刻；尚待root日期独核。

实际owner Ch23 95–121完整局部已读，既有ST-STORM两支content/style分责与结构感知factor支持不等本法的**随机背景teacher实例anchor→student不变性→保语义/背景读出反侧**。拟在ST-STORM完整两段后、现“文本条件还可以只在训练时生产表示增强”前补一段；Ch22末/Ch24开头交接沿本次INSET已实际读且未变层复用。唯一`MULTIMODAL-REPRESENTATION`，具体gap深入，不另写训练章。

拟逐字正文：

> 当背景确实是某类对象识别的nuisance，还可以把不变性目标做成教师产生的实例锚：先把同一分割前景放到多个随机背景，用冻结encoder的平均表示生成anchor，再训练student将更多背景变化映到该anchor。[BAP的受限对照](https://arxiv.org/html/2605.11107v1#S3)借近似可加性减弱背景相关，而不是精确拆出因果前景；随机背景分布、分割质量及teacher语义都仍是依赖。只用随机class targets也能压低所测ID背景影响，却损害OOD读出，说明不变性与保语义是不同验收；完整方法又明显牺牲场景背景辨别，不能迁移为VLM全能力无损去偏。合成、teacher锚、student适配与下游验证均付费，部分同数据control或平均准确率仍更好；若背景本来承担关系/环境语义、shortcut在对象内部或净质量失配，保留原encoder、较弱不变性或分别监督的专用读出，不以高worst-group分数批准所有消费者。

拟本人注：`SF-2026-ARXIV-2605-11107` — Daily05-14补May13；exactv1 §3–5/F/J/M3必要，2+1+2=5，teacher实例anchor→student不变性具体gap深入。保approxadditivity/iid、anchor反侧多变化、背景读出损失/对象内部shortcut不适用、同data/computecontrol与反退、L40S/BF16/重复人口和全费；不采T3异常AFR排序或通用因果去偏，未核实现/复现。独立Source/date/owner/PRE/POST待。

## A15. 三CLARIFY实际决定性方法（待root准入）

作者已只读各精确v1 HTML完整§3，尚未展开其必要评价/附录/Books：

- `2605.11367v1.html` §3.1/Eq2、§3.2–3.4：3DGS场景表示分`observed z_o`与`imagined z_i`，新观测只扩大observed、丢弃旧imagined并重采样，避免把先前想象伪装成观察；两view训练U-ViT/MVS式3DGS与CLIP semantic head，渲染供navigation。具体gap是显式观察/假设状态更新，而非“belief”命名，拟2+1+2=5。Eq1写法不当完整Bayes证明，constant-perstep不等constant-memory；Source未完成。
- `2605.11616v1.html` §3.2“Memory construction/recall”及§3.3：crossscene不是普通appearance exemplar，而是已有标注3D affordance投影/深度一致性过滤后category-level operable-region overlay，类别exactmatch召回；inscene candidate以visibility支持合并、graph与orthographic IDs另解query spatial qualifier，最后返回candidateID。具体变化是类别先验与当前实例的不同身份/消费边界，不是双memory名字，拟2+1+2=5；categoryprior不等当前GT，Wilson/merge资格必要时后核，Source未完成。
- `2605.12325v1.html` §3.2–3.4，特别Eqs3–6/筛选段：LLM aliases扩名可能破坏类间判别，故用DINO multi-layer affinity random-walk前后activation一致性为VG代理、以高激活patch跨类entropy为SC代理，同时优于canonical才保留；score在整个testset均值求得，是transductive适配而非免费对新域固定词表。后softaggregation另付费。具体变化是双代理约束prompt-selection及更多aliases可能失效的边界，不是任意module拼接，拟2+1+2=5；代理非geometric/semantic truth，未读评价/Source未完成。

已告root原件精确位置，待其actual决定性机制校准，不先把三项计候选或Source完成。

### A14.1 BAP实际窄写（待POST）

root实际必要§3–5/F/J/M3、日期组合与Ch23完整ST-STORM两段/后文本辅助两段及A14逐字PRE通过并授位。作者已按原稿保存Ch23现112正文+本人注/独立marker，完整直接两侧与本人注self-read、限定diff-check通过，非writer actualPOST待。A14中原摘要阶段“合成结果不当真实debias”边界继续保留，但Source现明确还包含CounterAnimal/NICO++自然图有限转移验证，不能反向误称只做合成；不因Source更丰富扩大采用范围。

## A16. Pace-and-Path 11459（5分）必要Source / 日期 / owner / PRE（待root）

实际精确v1 §3–4、A1.1假设/A1.4 clamping/A1.6分解、A4完整设置、G1完整限制。每chunk的近常量translation Δp、近恒定目标速度、可相加小旋转下，将tracking quadratic拆成沿计划方向的pace α与剩余path offsets；只改xyz，rotation/gripper承继原policy。§3.2公式对cosθ<0不可直接用：A1.4明确α clamp至1，full disturbance转path，因此orthogonal/sequential-exact只限未触边界的可行分支。零Δp、一般扰动或任意方向不获全局最优/无条件稳定；主文δ尾值的φ指数与小数表示不一致，不采该数值配方。主文Kexec公式可到T，但A4实际Heff10/βgate不同，不采用一个精确通用horizon recipe或iff v=0保证。

A4是重要反侧：velocity来自**simulator ground-truth object position一阶差分**，Δp优先来自realizedTCP历史而非原chunk，首chunk用action均值×controllerfactor .04。Oracle噪声sentinel绕过Bayesian shrink；tracker confidence分支未有真实平台验证。MoveBench是同一xArm6 pick族、10motionregimes、10k示教/460kframes，非十种操作语义；四backbones依各recipe先fine-tune，同一backbone±PPC才是较近对照。单H200141GB每backbone≤48h，eval单RTXA600048GB每method约2h/1000trials，20Hz模拟时间不等真实端到端deadline，precision未披露。

DynamicVLA真实async streaming无法在同步SAPIEN忠实复现，本文用2envsteps重推近似，故主表不能证明PPC原理胜真实异步栈。100trials×10regimes、seeds0–99隔开demo，aggregate Clopper–Pearson是trial人口CI不是重复模型训练。T1 π0.5 teleport60→53、Smol uniform-easy76→69，T2去cos的irregular74.7>full68.7；不能说全部组件/全部切片必要。Latch降低irregular长openloop但非安全证明，主要simoracle收益不授真实tracker/遮挡/多目标/接触安全；无复现/代码核验。

日期：本日精确v1 abs完整题摘/history已读，v1=`2026-05-12T03:17:59Z`，后v2May14不反填；sameDOI findable/arxiv.content registered=`2026-05-13T02:25:25Z`，最早May13 08BJT、最晚10:25:25，同May13。root已实际DC，下层v1history待其定点读，不用feedv2代版本史。

实际Ch26 §“Action Chunk时间契约”1197–1211完整局部已读：已有缩horizon、attention/candidate-uncertainty提出prefix，未承载**外部motion测量在chunk内分pace/path translation补偿**。拟唯一`MULTIMODAL-EMBODIED-VLA`，在候选covariance horizon两完整段之后、Safety envelope标题之前补一段；Ch25末/Ch27开头交接已读，不改原controller权责。

拟逐字正文：

> 缩短执行prefix之外，若另有可核的目标motion估计，还可以在chunk内部提出translation补偿：在计划位移非零、目标与计划在短窗内近似准静态时，沿计划方向的扰动调pace，剩余扰动以正则化path offsets修正，而不重训VLA或改gripper/rotation。[Pace-and-Path的受限分支](https://arxiv.org/html/2605.11459v1#S3)只在可行未clamp条件下有正交分解；反向运动需clamp并把残差转path，不能把无约束公式当任意扰动的最优controller。改变执行cadence的EMA latch也只是经验抑制持续不稳，不认证安全。原评价主要用simulator真值位移供velocity、同一pick族，真实tracker/occlusion链未验，部分motion与消融仍反退；外部估计、修正与重观测全计费，20Hz仿真时间不等物理deadline。测量失效、扰动快变、接触或多目标超出支持时，停用补偿、缩短chunk并回已验controller/停机接管，不让更平滑的proposal获得动作提交权。

拟本人注：`SF-2026-ARXIV-2605-11459` — Daily05-14补May13；exactv1 §3–4/A1.1/1.4/1.6/A4/G1必要，2+1+2=5，motion-conditioned pace/path与horizon分责具体gap深入。保clamp/非零Δp/准静态可行域、oraclevelocity与realizedTCP、模拟pick/真实tracker未验、async基线不忠实/切片反退和全费；不采通用closedform/horizon recipe/稳定安全，未核实现/复现。rootSource/date/owner/PRE/POST待。

## A17. Discounted Liveness 11479（5分）必要Source与中心资格（待root）

实际精确v1 §IV–VII全部、A/B完整相关证明及C设置。方法不读取policy本体，仅其offlineepisodes/成功或timeoutlabels；先从成功episode计算anchor value，再以它bootstrap目标函数，在timedout但embedding近已成功state的轨迹中回传较乐观value，缓和人为截断被当必败。Eq3 Jensen只给特定finitehorizon/min-target的偏保守不等式，Eq7是discounted surrogate；NN以视觉相近代同state不是精确图，也不自动有真实semanticdistance或successprobability。Eq9/10把goal value定-1，但全状态Eq7若直接在goal用也不保持-1，须终端clamp/非terminal更新限定；本次不照录未闭的完整Bellman/steps-to-go配方。A/B的tabular contraction不证明NN training收敛或所有policy人口保守。

评价：LIBERO π0/bowl250time-out、Square diffusionpolicy200、各200train/100test/50:50success-timeout；Franka clothhumanteleop150train/20test/50:50，human不是固定stochasticpolicy已知、观察标签也有噪声。SigLIP2+proprio5layerMLP512/GELU/LayerNorm，batch512/5000epochs/PERbuffer10k；γ .993/.993/.99，baselineγ与rewardscales各异，不能视同数学目标完全匹配。5trainingseeds，Alexander–Govern/Welch+BH .05；hardware/precision/完整训练与推理cost未披露，不补造SLO。Successmetric只取最终单调成功subtrajectory、failuremetric只timedouts人口，composite均值不是全episode success或calibrated safety。

§VII明确反侧：bootstrapping在recoverable动作丰富时帮助较大，但总使failuremetric较差；visualalias把真正不可恢复状态错误贴近success时，会制造乐观，Square recovery缺失时收益小。反例成功poorgrasp也可能先被误报failure。有限encoder变体/数据量结果不授任意representation稳定；外部execution/safety/实机恢复未由value证明。未核代码/复现，不看曲线像素/精确未给图数字。

Date：精确v1 Atom原提交`2026-05-12T03:54:30Z`（ID明确v1）与sameDOI findable/arxiv.content registeredMay13 02:25:56Z，公告下界May13 08BJT至10:25:56，同May13，root已实际DC层。实际Ch26 evaluation1318–1360已读：已有offline corrective-neighborhood、真实成功/安全/终态分母，没覆盖**success-anchor纠正timeout pessimism与visualalias乐观风险**；前进度部分442–449是online LoRA/runningpeak warmup而非该offlineconsumer。待root判断目标边界未闭应暂缓，还是只采已被受限实验支持的timeout-bootstrap/falseoptimism分支；不绕过理论矛盾签完整liveness保证。尚无逐字稿/写位。

## A18. Dynamic Execution Commitment 11567（5分）必要Source / owner / PRE（待root）

实际精确v1 §3–6及A完整2H inpainting/Alg1。K8候选在kinematic累积pose而非rawdelta variance中按locally-timealigned distance聚类，mass×compactness选mode/medoid；共识只排验证顺序，非correctness。对每位置固定较高共识位置/固定顺序prefix分别inpaint重解，全部2H queries拼batch，一次actionexpert调用；Alg1明确仅取∀i≤l双check均过的最长连续prefix，Eq11只看末项不照抄。首位置失败导致空集合的fallback没定义，不补闭合可执行recipe。模型自一致与kinematic integration不是真实transition、形式verification或physicalsafety。

π0/π0.5/GR00T，RLinf配置，LIBEROH10/ManiSkill8/MetaWorld5，GR00T5；δ按各动作维原denormalization std、不验binarygripper，RTX4090，precision/内存/统计seedCI未披露。四Piper实机task各50teleopdemo、训练H20/30Hzrobot，20trial而StackCube30；真实control30Hz不等model485.6ms完整SLO。StackCube83.3低于fixed15的86.7、部分LIBEROsubsuite反退；遮挡缺证据和subcmcontact误差不能由自一致修复。

关键成本反侧：T7 Original216.2ms/6.3action约34.3ms/action，A3 485.6/9.7约50.1ms/action；仅同报口径归一已不支持“更长horizon就净省推理”。这是作者数据复算，非实际本机benchmark。K8 draft+2H验证虽可batched singlecall，compute/memory随样本数/长度增加，forwardcalls和replan数不能替总wallclock。T6K4/8/16 latency467.2/485.6/503.6，quality有小差额；不授constantwork或生产净加速。未核代码/复现。

日期：本日精确v1 abs已实际全题摘/history，v1May12 05:52:58Z，后v2–4不反填，sameDOI findable/arxiv.content registeredMay13 02:28:05Z，联合同May13。官方当前代码release不回填v1“将release”。

实际Ch26 horizon1197–1211的AutoHorizon/MCuncertainty完整段与1067–1085的prefixinpainting continuation局部均读：前者只提prefix，后者固定已提交prefix补suffix，不承载**未执行draft的双context re-decode→连续通过前缀**；现SpecVLA是执行后oneprimitive逆动作补偿，非本次执行前自一致。唯一`MULTIMODAL-EMBODIED-VLA`，拟在candidateentropy两完整段后、A16 Pace-and-Path之前补一段；A16未保存前不抢窄位，待root协调。

拟逐字正文：

> 未执行的action draft还可以先经模型内重解，而不只从attention或样本方差决定长度。候选动作先积分为轨迹，在较集中模式内取medoid；随后分别固定高共识位置与顺序prefix，对每位置做inpainting重解，只保留双检查都通过的连续前缀。[A3的受限验证](https://arxiv.org/html/2605.11567v1#S3)检查的是同一模型在两种条件下的自一致，不是实际未来状态或接触安全；共同偏错、遮挡及精度不足仍可失败，首位置不过时也需显式拒绝/重观测，不能跳去后续通过位置。K份draft和2H份验证可合batch，却增加算力与驻留；作者单调用latency增幅超过所报horizon增幅，较少replans不自动等净省墙钟。阈值、inpainting支持或完整费用失配时，保留固定保守prefix、短chunk与真实反馈，由独立controller决定提交，不把“verified”名字当形式或物理保证。

拟本人注：`SF-2026-ARXIV-2605-11567` — Daily05-14补May13；exactv1 §3–6/A必要，2+1+2=5，双context自重解/连续prefix具体gap深入。保Alg1非Eq11末项捷径、空prefix未闭、kinematic/自一致非truth、K/2H batch与T7复算成本反侧、实机小trial/精度遮挡失败；不授常数work/净加速/安全，未核代码/复现。独立Source/date/owner/PRE/POST待。

## A19. HorizonDrive 11596（5分）必要Source / owner / PRE（待root）

实际精确v1 §4–6完整，补§4.1、A/B/C全部必要控制/设置/评价协议。先标准GT-history conditionaldrivingmodel，再以自身rollout degradedhistory与GTfuture作SRR：局部boundary pred→GT blend由w0→8，global从晚严重drift边界向早边界采样，先学修复；再让同样经过SRR的teacher与student做TRD，teacherT11/K40固定window多步滚动、studentK10/4steps/N20，每五studentchunks匹配长teacher区间并backprop，免长horizon同时驻留但总rollout成本不消失。Noise-truncated CFG另分支，不能把全部收益都归teacher初始化。

Wan2.1-1.3B双向骨干、VAE时间压缩4→1经重训，layouttokens+actionAdaLN；100h私有driving base40k+nuScenes10k，SRR10k，TRD200steps。Base96×5090/SRR64×5090/TRD32×5090，bf16与96/64/32batch；2000step cache-refresh/late→earlyN10→4不是每步freshonlineRecovery。T5TRD总200steps却阈值decay至step400，不能照录完整schedule为可执行recipe。NuScenes700train/150val各~20s，minute展示仅qualitative。单5090 chunk10frame 1.8s@256×512或5.8s@384×768，仅约5.6/1.7generationFPS，不授real-time controlSLO/闭环驾驶安全。

T1 generalworldmodels无drivingcontrol，只能visualreference；T2既有drivingmodels沿各原论文条件/clip/horizon，不同协议不严格排名。最接近T1bottom三anti-drift方案同backbone/data/control重训，但按各原recipe不等相同总compute。T3teacher/student初始化的因子对照支持先修teacher，student-onlySRR反让FID/ARE/DTW坏；teacher-onlyDTW也反退，N1→4 FVD135.35→139.28并非随长度单调，EarlyCFG DTW3.13优于Delayed3.27。ARE/DTW来自VGGT估pose、非真实物理law；FID/FVD/VBench不认证actioncausality。未给重复seed/CI，未核代码/复现，不扩Hclosedloop附件为已读。

日期：精确v1 abs已实际题摘/history，May12 06:22:16Z；sameDOI findable/arxiv.content registeredMay13 02:28:49Z，联合May13。原公告无更早稿具名信号。

实际Ch25 481–501与876–913完整局部已读：已有selfcontext/梯度图、长teacher短student、WorldPlay history匹配及过度自产导致teacher失准；未覆盖**在蒸馏前先用degradedhistory→GTfuture修复teacher、再以teacher自身固定window rollout监督**。拟唯一`MULTIMODAL-WORLD-MODELS`在WorldPlay完整段后/“从规则检索到学习式ContextQuery”前一段，不把driving数据或控制细节复制Ch26。Ch24末/Ch26开头交接待写前补实际读。

拟逐字正文：

> 蒸馏前还应核teacher在部署型历史上是否可靠，而不只让student经历自己的误差。一条分支先用teacher自产的退化history预测录制GTfuture，在边界混合与采样课程中学习恢复；再让这个rollout-capable teacher按固定窗口连续生成，分段监督较短chunk的少步student。[HorizonDrive的受限消融](https://arxiv.org/html/2605.11596v1#S5.SS3)支持teacher初始化的作用，但student-only适配、较长训练展开和CFG设置并非每项指标更好。固定窗口限制同时驻留，不免除teacher多步、student rollout、critic、cache-refresh及视频/codec重训成本；离线恢复也不是运行时新取得的观察。其质量与动作轨迹指标限nuScenes和估计pose，长达分钟仅展示，低分辨率单卡生成FPS不签交互deadline或真实驾驶安全。Teacher支持、history身份或净质量失配时，保留短rollout/原蒸馏、重新训练teacher并用真实observation校正，不让更稳定视频成为环境真值。

拟本人注：`SF-2026-ARXIV-2605-11596` — Daily05-14补May13；exactv1 §4–6/A/B/C必要，2+1+2=5，teacher先恢复/固定window rollout distill具体gap深入。保私有预训与VAE重训、条件/预算不同、初始化/展开/CFG反退、T5schedule未闭、VGGTproxy与生成FPS/控制分责、全费；不授在线Recovery/分钟定量/真实驾驶安全，未核代码/复现。独立Source/date/owner/PRE/POST待。

### A17.1 actual owner差额与最小逐字PRE（待root）

root已实际IV–VII/C支持窄经验timeout-anchor/falseoptimism分支，不采未闭全状态goal边界配方。作者实际Ch26 1318–1360与442–449完整局部比较，现offline corrective-neighborhood是**失败动作→正支持纠正目标**，runningpeak是**离线平滑→onlineRL初始化**；本项是**offline policy进度value目标的timeout重新标记**，consumer/目标不同。拟唯一`MULTIMODAL-EMBODIED-VLA`在Evaluation ladder中“videoquality/pose/offlineerror只能证明局部、真实trial绑定”完整段之后、Nativegoal终态稳定两段之前补一段。Ch25末/Ch27开头交接已实际读。

拟逐字正文：

> Offline policy评价还须分开“观察到失败”与“预算到时仍未完成”。一条受限分支先以成功episodes形成value anchors，再让它们bootstrap超时轨迹的目标：视觉/本体状态若接近已有成功路径，可向其前驱传播较乐观的进度，减少人为截断被当成永久失败。[Discounted-liveness的有限对照](https://arxiv.org/html/2605.11479v1#S5)支持这种恢复行为较多时的取舍，但视觉相近不等同一可恢复state，alias会把真失败也乐观化，failure识别指标因而退步。Value/goal的终端边界与steps-to-go转换还需另验，不能照未闭的全状态递推批准liveness或success概率保证。这里增加编码、两阶段拟合、replay及校准费用；所报success指标只涵盖最终单调子轨迹，不等全episode成功率，更不赋予动作安全权。支持稀疏、alias严重或目标边界不清时，保留原timeout标签及unknown、直接结果评价和独立controller，不由更好的composite均值批准继续执行。

拟本人注：`SF-2026-ARXIV-2605-11479` — Daily05-14补May13；exactv1 IV–VII/A–C必要，2+1+2=5，timeout-anchor进度value/falseoptimism具体gap深入。保目标终端边界与steps-to-go未闭、tabular/NN分责、success子轨迹/failure人口不并、representationalias与failuremetric反退、5seed/三case/全费；不采完整Bellman配方/真实liveness/安全，未核实现/复现。root必要Source窄域已支持，owner/PRE/POST待。

### A16.1 PPC实际窄写（待POST）

root实际§3–4/A1.1/1.4/A4/G1、v1history与date、当前完整horizon局部/逐字PRE通过后授位。作者已按A16原稿保存Ch26现1213单段/本人注/独立marker，完整covariance两段、新段、Safety后完整两段与本人注self-read，限定diff-check通过；一个误加空白随正式patch同步恢复，未留额外重排。非writer actualPOST待。11107本注已仅同步既成POST。

## A20. Relation-aware Visual Enhancement 11808（5分）必要Source / owner / PRE（待root）

实际精确v1 §3–4/§6/Limitations、B.1 contrastpipeline、C全评价与E必要消融。再次确认是**LVLM关系幻觉**而非VLApolicy。GPT5改动actionverb（尽量换不同bodypart）、自动复核+人工screen构造同image/twoquery配对，按视觉attention归一Frobenius差ARS排序heads；高ARS topK与低ARS bottomK各选topm tokens，做setdifference mask，再对该层allheads pre-softmax加β|score|强化。高敏感也有背景，低敏感有重叠，差集只定义所增强人口，不是真实actionregion/因果责任。

五LLaVA/InstructBLIP/ShareGPT4V7B或13B、MMRel/RBench/AMBER，额外POPE；greedy/seed55，K5/β1，α LLaVA.05而QFormer InstructBLIP.5。高β退步、selectionratio跨架构不同，不能把一个K/α变成固定真值。Objectbaseline主要为物体幻觉设计，不是matching relation专用强基线；T4POPEadversarial Acc83.65低于VAF83.72/F182.45低于VAF83.05，不能全优。GPT5mini openendedjudge仅0–10代理、涨幅小（如7.84→7.91）无重复CI；不能推一般生成质量无损。逐headmask相较random只支持选中heads对所测任务重要，不证明真实relation已定位。

未披露hardware/precision/batch/IOlength/SLO与ARS calibration人口和runtime复用策略，‘negligible’latency图不包括可核的contrast生成/双前向/筛选全成本，不能借公开代码未核就补具体offline部署配方。需要内部head访问与选层、对closedAPI不可用；baseline forward与新增编辑均须回归。未核代码/复现/图像像素，不因热图更聚焦授因果。

Date：topic-multimodal原始Atom精确ID v1/published原提交`2026-05-12T09:03:19Z`，sameDOI findable/arxiv.content registeredMay13 02:34:08Z，全区间May13，待root独核该组合。

实际Ch23 177–204完整局部已读，已有ViT聚合/attention-vsnorm、ObjectDINO Q/Q K/K V/V聚类选head→foreground，未有**同图verbcontrast的query-sensitivity排序→高/低head区域差集→原decoder pre-softmax写回**；不重复generic attention不是因果。拟在ObjectDINO两完整段后、“局部读出还可以只从冻结生成模型的多噪声…”前单段，唯一`MULTIMODAL-REPRESENTATION`；Ch22末/Ch24开头未变交接沿本次已读层复用。

拟逐字正文：

> 关系问答还可以按query的受控变化选择可写回的视觉attention，而不是仅按原图feature聚类。对同图只替换action verb，比较各head的视觉attention差异；再把高敏感heads支持而低敏感heads未共同选中的tokens作为增强候选，对原层pre-softmax scores重加权。[RVE的受限对照](https://arxiv.org/html/2605.11808v1#S3)因此分开contrast诊断与生成干预：敏感不等真实关系区域，差集也不认证因果，所有heads共同强化仍可能遗漏必要context。选层/比例依架构、增强过强可退步，部分物体基线仍更好；contrast生成、筛选与额外前向都应计入全成本，不能只用一次编辑后的latency报价。内部访问、contrast有效性或消费者质量不可靠时，保留原attention、外部grounding/真实局部监督与独立答案校验，不由热图或judge小幅改善批准通用无幻觉。

拟本人注：`SF-2026-ARXIV-2605-11808` — Daily05-14补May13；exactv1 §3–4/6/Limit/B1/C/E必要，2+1+2=5，verbcontrast sensitive/nonsensitive差集→pre-softmax干预具体gap深入。保LVLM非VLA、contrast筛选/双前向未知全费、head/热图非因果、跨架构α/β反退/POPE反侧、单seed/judge小涨幅和内部访问，不授无幻觉/免费部署，未核实现/复现。独立Source/date/owner/PRE/POST待。

### A18–A20 实际保存与POST差额

11567 Ch26 covariance完整两段后/PPC前、11596 Ch25 WorldPlay完整段后/ContextQuery前，均按授位原逐字稿/本人注保存，完整直接两侧与本人注self-read，限定diff-check通过；Ch25写前补读Ch24末/Ch26开头。11479按A17.1原窄经验段保存Ch26 videoquality/trial后/Nativegoal前，未自修论文理论。root已实际非writer三项全部完整新增/完整直接前后/本人注POST通过，窄位释放；11459此前亦实际POST通过，作者仅同步这些本人注既成状态。11808按A20已保存Ch23现201一段/独立marker/本人注，完整ObjectDINO两段、新段、后weak-supervision完整段与注self-read、限定diff-check通过，root actualPOST待。当前已实际**10整合/纠正、1NC、1中心争议**；11808不提前计生效。

## A21. GridS 11817（5分）必要Source / owner / PRE（待root）

实际精确v1 §3–5、J完整限制，A/B设置、F matched-downsampling、I retention定义。Densevision features先全编码、globalpool→MLP sigmoid预测K连续grid坐标，bilinear从四邻features取加权和，再加coordinateencoder位置送VLA，与actiontaskloss联合FT。可微接口替代硬selection，**不恢复原图不存在的subpixel细节**、不保证任意spatialcue无损；降低后consumer序列不免除visionencoder与pool/MLP/interpolation费用。主文将可微/训练自由度与严格geometry/纯噪声过滤混说，不采用唯一因果或证明所有posttraining剪枝必差。

同K16/fullFT的F对照优于random/topK，支持联合可学sampling在此配置有效，但同时改变coordinatelearning/pos/interpolation，不独立归因单一bilinear。LIBERO π0/π0.5，4suites40tasks；ALOHA50demo/task、三seed≥300episodes，两taskscripted/human分账；SO100RGB-only D435/D405与SmolVLA，83/74/75demo，50ksteps/batch16/RTX3090；真机21OODscenarios不等足量独立population，精确trial分母与CI未完整给。B中π0batch32/π0.5batch128，不能把单T4batch128训练速比与任意backbone预算等同；precision未披露。

关键反侧：真机K4 0%/OOD0、K8 28.5/19.1、K16 61.9/38.1、K32 19/0，预算不是越小越好或唯一16常数；LOra适配低于dense8.3%，证明接口改变需要更广consumer适配，不能叫freeplug-in。π0.5K4 Spatial98.4→97.4，ALOHA scriptedInsertion91.4→86.9；T2“平均87.0”与未分权四列不当统一episode均值，正文只用明确task/cost口径。I“retention”仅densefeature对任一sampledfeature的maxcos，不是MI/充分性、语义完整或grounding证明。主表completion-time含执行路径，非单forward；Pro6000/32language token/modelprofiling单batch约1.2×、large128batch到3.2×，与训练2.9/3.4×不得拼成线上单请求收益。未核代码/复现。

日期：精确v1 abs已实际history May12 09:08:42Z，后v2不反填；sameDOI findable/arxiv.content registeredMay13 02:34:21Z，联合May13。待root实际日期层核。

实际Ch23“固定预算”917–945完整局部读：CLASP/Gaze离散region或tokens读，MetaCompress以稠密P合并且consumer冻结，不承载**tasktrained continuouscoordinates→局部bilinear features+pos、consumer需fullFT/LoRA失配**。Ch26 1603–1628 action-sensitivecompression只定义闭环容忍度、不拥有resampler算法；故唯一`MULTIMODAL-REPRESENTATION`，拟MetaCompress两完整段后/perturbation诊断前一段。Ch22末/Ch24开头沿本次未变已读交接复用，不扩VLA章重复写。

拟逐字正文：

> 压缩也可以学习连续读取坐标，而不只在原token中做硬选择或稠密合并：dense视觉feature仍先完整计算，再由全局摘要预测少量坐标，以邻近feature的bilinear插值取样并添加坐标编码，与实际consumer的任务loss共同适配。[GridS的受限VLA对照](https://arxiv.org/html/2605.11817v1#S3)支持这种接口选择，但插值不恢复未编码的细节，max-cosine retention也不认证信息完整或真实几何。该输入分布改变需要训练预算，所测LoRA反低于dense，不能把full-FT结果当免费hotplug；真机过低token预算全失败，更多token也会退步。完整编码、坐标预测、采样/适配与闭环回归均付费，单batch墙钟收益远小于大batch训练/吞吐比。空间细节、consumer适配或净费用失配时，提高保留量并回原grid/dense或已验证selector，按实际任务验收，不由较少tokens批准无损语义与动作安全。

拟本人注：`SF-2026-ARXIV-2605-11817` — Daily05-14补May13；exactv1 §3–5/A/B/F/I/J必要，2+1+2=5，continuouscoordinate/resample/consumer适配差额深入。保全denseencode、局部插值非细节恢复、maxcos非信息证、fullFT/LoRa及K失败/反退、task/大batch/训练和请求墙钟分责、全费；不授通用geometry/无损/物理安全，未核实现/复现。独立Source/date/owner/PRE/POST待。

### A21.1 actual保存与既成差额

11808已由root实际完整新增/ObjectDINO完整前侧/weak-supervision完整后侧/本人注POST通过释放，本人注仅同步既成状态。11817 root已实际Source/date/完整MetaCompress与扰动诊断局部、A21逐字PRE通过授位；作者按原稿保存唯一单段/marker/本人注，完整两侧self-read与限定diff-check通过，actualPOST待。当前实际11整合/纠正，TanStack1具体NC；中心争议另见11134与下项，不把待POST算生效。

## A22. h-control 11871（5分）必要Source / 中心争议终态

实际exactv1 §3、§4、§6、C.2/E与G/H/I.1必要评价。Eq8对未观测位置重新加噪、观测位置pin到对应noised条件，Eq9却用确定性的clean denoiser输出；C.2借DAE随机reconstruction条件分布的stationary-law结论，并未给出额外随机reconstruction核。Score-optimal只保证conditional mean，不能替代conditional sample。bounded反例：X为[-1,1]均匀分布、Z为非退化Gaussian corruption，原目标人口下X'=E[X|Z]，由total variance有Var(X')=Var(X)−E Var(X|Z)<Var(X)，故一次转移即不保持目标分布；fullsupport和有界性不修复。更直观N(0,1)、σ=.5时chain=.5x+.5ε稳态variance1/3而非1；这不是指控所有Gibbs或pin-and-denoise无效。E的Polyak平均进一步集中mean，不能当精确posterior sample。未扩读全部证明，不替作者修完整kernel。

正证保留：同Wan2.2TI2V5B的training-free对照、RealEstate200场景/49帧与DAVIS28×3轨迹/49帧，A40 mixed precision；MegaSAM pose/单Sim3对齐是代理，失败pose按同法排除但主表未逐row给分母，不能补。50outersteps/controlwindow2–5/J10/CFG4。G的全720×1280单A40 7.13frames/min低于TTM12.99，其他架构/分辨率不可统一排名；T3加入平均的RRE/RTE反退、freeze-only FVD同382.26，非全部更好。§6明确globalattention下即使freeze patch仍全部forward，不授patch冻结等墙钟跳算；I.1错误depth可导向错误camera，prior不是geometry truth。实验证据不能补理论law资格。

日期：精确v1 history May12 09:51:04Z，sameDOI findable/arxiv.content registeredMay13 02:35:40Z，组合全May13，root已实际核。保2+1+2=5与受影响域深入，不降分/不排除；**暂缓—中心争议，不写Books**。root实际§3/4.2/6/C2并接受上述bounded方差反例。重开仅需作者明确随机conditional reconstruction kernel或更正定理/假设与可核不变分布论证；未到前不绕中心摘一般pin-denoise造书段，不作positive evidence/性能保证。

## A23. OmniHumanoid 12038（5分）必要Source / owner / PRE（待root）

实际exactv1 §3–6/A.3：共享motion-conditioning分支，target embodiment的LoRA仅在denoising QKV；一向attention允许denoiser读condition，condition不读target。先冻DiT训各appearance LoRA，再冻appearance、按batch轮换对应LoRA训共享motion；新embodiment只训其LoRA、共享motion冻结。阻断forward外观回流不等所有梯度因果隔离。仍先用paired多embodiment数据学习共享motion，新target unpaired不等整套paired-free。因果student按ref/cond/tgt序列不读未来，teacher-forcing DSM后self-forcing VSD+GAN，50→4steps有quality代价。

数据是10humanoids/700Humoto motions/100Unity scenes，Blender骨架对应与共同camera/layout制7200pairs；heldout G1 synthetic50video与real50human/online robot视频无paired GT。Wan2.2TI2V5B/rank64/2H200、每卡batch1/10ksteps/AdamW2e-4，precision和完整timing长度未披露；1080p30FPS数据不是serving。Gemini3Flash judge代理/no repeatedseed CI，T1 realoverall8.39低于KlingO1 8.53，不授全胜；T2 fullteacher .10FPS低于去decouple .21FPS，student4.96FPS但质量均低于fullteacher。Decoupled消融同时去mask/rolling/stages，不能把收益唯一归mask；没有动作policy、物理可行性或robot部署证明，未核代码/复现。

日期：topic Atom精确v1 publishedMay12 12:21:11Z、sameDOI findable/arxiv.content registeredMay13 02:39:43Z，全区间May13，待rootactual。实际Ch24 1696–1721完整Sim2Real两段/前pixel迁移/后LatentReuse及前128–146 ref/history局部已读：旧文拥有锚点制paired数据→部署referenceadapter，不拥有**paired sharedmotion训练→unpaired新target appearanceadapter**的参数/条件分责。唯一MULTIMODAL-GENERATIVE-PARADIGMS，拟在Sim2Real完整两段后、LatentReuse标题前一段，非Ch26动作控制或Ch30通用LoRA。未授不写。

拟逐字正文：

> 外观迁移还可以把共享运动条件与目标外观适配分开训练：先以成对多主体视频学习motion branch，再冻结它，仅用新主体的非成对视频适配目标denoising分支。Condition只向target提供信息、不能反读target的单向attention，加上分阶段冻结与按主体加载adapter，限定各阶段消费的状态；这不等梯度因果隔离，也不抹去共享运动原先的paired监督。[OmniHumanoid的受限对照](https://arxiv.org/html/2605.12038v1#S3)支持这一迁移分工，但消融同时改变多项训练条件，外观/动作judge不认证骨架、接触或物理可行性；输出仍是视频而非机器人动作。共享motion、各adapter、骨架/相机条件与训练阶段须分别保留，制备/适配和完整生成都计费；少步因果student以质量换速度，不由较高FPS签控制deadline。新主体支持、运动保持或净质量失配时，保留原paired适配、显式motion条件与完整teacher，不以unpaired target适配宣布无配对学习或真实具身迁移。

拟本人注：`SF-2026-ARXIV-2605-12038` — Daily05-14补May13；exactv1 §3–6/A3必要，2+1+2=5，paired共享motion→unpaired目标appearance具体gap深入。保单向forward非因果梯度隔离、多项消融/teacherstudent质量成本、synthetic与judge人口、video非action与全费，不授paired-free/物理可行性/控制deadline，未核实现/复现。Source/date/owner/PRE/POST待。

## A24. FIS-DiT 11869（5分）必要Source / owner / PRE（待root）

实际exactv1 §3–5/Table1–3全部：fewstep时interstepcache可用相邻state太少，改同一次forward的frame稀疏计算。首末frame始终anchor，中间按stride循环offset，各层轮换anchor；每module在短序列求值后线性插值回完整frames，下一module仍完整接口。原‘exact DiT computation’只指稀疏上下文上真正求值，不等原fullframe attention输出；Fig3的误差基于feature magnitude norm，再取差，不界定vector方向/最终语义。低CV热图选middleblocks，head/tail与末denoisestep完整；校准不因training-free消失。

同Wan2.2A14B LightningLoRA4steps/H20与HunyuanVideo1.5 8B distilled8steps/L20，81frames/100VBenchprompts、后者各配referenceimage，480/720p，FlashAttention。Precision/batch/concurrency、warmup/重复计时CI、完整latency是否含codec未披露，不填onlineSLO。默认Tea/MagCache不触发仅限所测fewstep配置，force阈值每model/res调；不是证明所有cache失效。T2相同stride而只换固定/轮换anchors，近似相同latency下质量更好，是最近对照；T3去block或step保护更快但quality更坏，固定阈值不是严格risk保证。T1Balanced多项CLIP/VBench仍微降、Hunyuan叠force降至.7865<.8065，不能全无损/组合总更好。计算/重构/调度/全codec均计费；无代码核验/复现。

日期精确v1 historyMay12 09:49:36Z与sameDOI findable/arxiv.content registeredMay13 02:35:37Z全May13，root已实际核。实际Ch24 1675–1705完整dynamicpatch/mixedgrid/nonuniformgrid/JiT两段与后少步teacher两段，及1750–1880cache完整局部已读：旧有空间anchor逐渐增集/时间reuse，未承载**fewstep内frameanchor跨层轮换，使每位置周期真求值**。唯一MULTIMODAL-GENERATIVE-PARADIGMS，拟JiT完整两段后、‘因此，直接把已有sampler…’前一段，不复制Ch49kernel章。

拟逐字正文：

> Few-step视频缺少足够相邻去噪状态时，还可以在一次forward内部按frame分配计算：保首末frame，其余位置跨层轮换作为anchors，在稀疏上下文上求值后插值回完整序列，再交下一模块。[FIS-DiT的受限同stride对照](https://arxiv.org/html/2605.11869v1#S4.SS3)支持避免同一位置持续被跳过，但轮到真求值也不等原full-frame attention，feature幅度接近更不保证方向或语义无损。敏感头尾blocks与末步保完整，用校准和较小稀疏率约束误差；所测去保护更快却损质量，与inter-step cache叠用也会反退。它不保存历史featurecache，却仍付gather、重构、调度、校准及完整生成/codec费用，单卡81帧结果不签实时SLO。运动细节、时序质量或净费用失配时，缩stride、扩大完整blocks/steps，回full-frame求值，不由周期刷新或training-free批准lossless。

拟本人注：`SF-2026-ARXIV-2605-11869` — Daily05-14补May13；exactv1 §3–5/T1–3必要，2+1+2=5，fewstep内frameanchor轮换具体gap深入。保稀疏上下文真求值非原全attention、magnitude误差非语义界、保护/组合反退、100prompts/单卡/计时口径unknown及全费；不授lossless/实时SLO，未核代码/复现。root日证已核，Source/owner/PRE/POST待。

## A25. SCOLAR 12163（5分）必要Source / owner / PRE（待root）

实际exactv1 §3–5、A–D/G–I必要：trigger后读取LLM中间层完整sequence hidden，two-layer selfattention detransformer一次产生与原visiongrid同数的辅助feature、gatedresidual后加入上下文。是共同生成而非各latent统计独立，也未取得新外部观测；A.1从L到Nv的最终选择/投影形状未闭，不补可执行recipe。SFT先配准原/aux图的deltafeatures reconstruction，再weightedtrigger NTP，再teacherforcing概率700steps由1→0；GPT4o CoT与必要性过滤有选择偏差。RL缓存连续eaux为固定条件、只对两段离散texttokens做ratio/GRPO+triggerreward，C明确detransformer无直接RL梯度；‘implicit cooperative’不是连续state的无偏policygradient或收敛证明。

Qwen2.5VL7B visionencoder/projector冻结、LLM+branch训练；210kSFT/10kRL，SFT8H200 batch1/acc16/maxseq16384/maxvis6000，RLbatch256/G8/maxresponse4096/54steps；GPUhours是每epoch近似，precision/完整latency未给。G的多模型结果部分引用不同recipe，星号非统一重训；H只有60sample judge选层预研，不是完整端到端layer对照。I明确当前丢Phase1KV全序列重算，不能把未来KVappend优化算现部署。T1 RL后V*84.29→83.77且HR8低于Monet68，VisualPuzzlesoverall34.42低于Monet35.02、Algo低于原backbone；不授alltask/best。T3 placeholder替换比完全禁用更坏说明分布干预破坏，不证明真实视觉语义或faithful reasoning。D所谓IG是线性projectionresidual、t>500只取256rank，更非Shannon信息/独立因果；越长latent不单调、过池化失败，完整重算/多阶段训练/paired制备全付费。未核代码/复现。

日期：精确v1 historyMay12 14:13:08Z、sameDOI findable/arxiv.content registeredMay13 02:42:45Z，组合全May13，待rootactual。实际Ch23 1785–1838完整canvas段、CrystaL两段及后write/read诊断两段：旧文将latent路径变训练接口，却未有**完整hidden一次回写inputgrid辅助视觉state、trigger与连续branch更新分责**。拟唯一MULTIMODAL-REPRESENTATION，在CrystaL完整两段后→ObjectHallucination标题前一段；不复写RL章通用GRPO。

拟逐字正文：

> 连续中间态也可以由当前完整sequence的hidden一次提出，而非逐token自回归延长：在离散trigger后，用小型attention branch产生与原视觉grid对应的辅助features，和原features残差融合，再继续回答。[SCOLAR的受限对照](https://arxiv.org/html/2605.12163v1#S3)提示过度池化或无效填充会破坏consumer，但线性投影残差不是信息量，填充后退步也不证明faithful视觉推理；一次共同生成不等各位置独立。配准辅助图、先重建后trigger再逐渐使用自产state，需要分阶段训练；所述RL将连续state缓存为固定条件，只更新离散文本策略，不是给branch直接policy-gradient。原实现还全序列重算KV，制备、branch和新增context均计费，较长latent不自动更好或更快。辅助state、原任务或净费用失配时，保留原视觉输入、短latent/可读trace与外部grounding，不把自产feature当新观察或事实证明。

拟本人注：`SF-2026-ARXIV-2605-12163` — Daily05-14补May13；exactv1 §3–5/A–D/G–I必要，2+1+2=5，fullhidden单次辅助grid/离散trigger分责gap深入。保形状未闭不补recipe、RL无branch直接梯度、projection非信息/placeholder非faithfulness、pooling与task反退、KV重算/全费；不授独立latent/新观察/速度，未核实现/复现。Source/date/owner/PRE/POST待。

## A26. MoLA 12167（5分）必要Source / owner / PRE（待root）

实际exactv1 §3–5/A.1–3/A.5、A.6具名failure/quality/precision段。SVD先以human+robot视频FT，再各自预训三个IDM：current/future RGB经8queries/4layer768 transformer+VQ128×32，均重构futureRGB，另由冻结DepthAnythingv2/SAM2/CoTracker3产生depth/semantic/flow代理监督。部署不再运行这些aux decoders/foundationlabelers，而由RGB current+**自产future**抽三份codes，与futurevisualfeatures共同condition actionhead；frozenSVD、IDM+10stepflowactionhead联合下游FT。不是三份实测modalities、不是只用codes/不用future，也不由离散bottleneck获得因果/物理可执行保证。A5明确worldmodel+head、非VLMcentric，没有LLM高层reasoning。

SVD1.53B/256²/16frames、8H100视频预训5days、IDM16h/下游20h，precision未披露。CALVIN ABC-D、LIBERO90pretrain后各suiteFT、Plus10,030tasks；部分baseline引用不同预训预算、*说明前后混合，不授统一重跑因果排名。T5近同组件增IDM与A2T13 singleRGB/sharedmultiloss较近对照，但多branch总容量/预训未匹配，flowonly首任务95.6低于baseline95.9，不宣称所有指标单调。A2T14same/noisy-current替future支持所测online未来线索，非一般可辨识性。

UR5e双D455/D405共1000demo五task、每task50trials、每trial最多20attempts，success是该预算内完成不是一次尝试；表仅两ID/两OOD列、完整五任务分母不能补。MoLAavg73低于π.5 77.5，lighting64<π.5 74；相对VPP62支持有限差额不全VLA胜出。高精度45%未给完整分母只定性，意外翻倒/抓错难自纠正，wrongfuture可污染codes/action。4090 T8 CALVIN部件和约101.04ms而T10总129.6ms，真机部件101.90ms，显然module sum非完整deadline；5/10runs只是计时重复，不是训练seedCI。one-step4.55 vs10step4.56，未来更像真不单调改善控制。训练、三个IDM、生成与action采样全付费，无代码核验/复现。

日期：topic原精确v1 publishedMay12 14:15:16Z，sameDOI findable/arxiv.content registeredMay13 02:42:51Z，组合全May13待rootactual。实际Ch26 1586–1613完整latent-algebra两段/后SAE干预与predictive EMA段、1725–1744future→IDM示教局部，以及Ch25 latentreference/slotfactor段比较：旧文不承载**自产future→按辅助modality分别预训的inverse VQ mixture→joint actionhead**。唯一MULTIMODAL-EMBODIED-VLA，拟latent-algebra完整两段后→‘可解释的潜在方向…’前一段，不复制Ch25通用dynamics。

拟逐字正文：

> 自产future接入控制时，还可以先经过分责的inverse-action接口，而不直接把预测帧交action head。多个RGB inverse模型分别以depth、semantic和flow代理目标预训，各自将当前/预测后态压成离散codes；下游冻结视频生成器，联合适配这些codes的producer与action head，后者仍同时读取future视觉features。[MoLA的受限对照](https://arxiv.org/html/2605.12167v1#S4.SS4)支持这种分工，却未匹配所有分支容量与预训费用，也不是取得三种新实测模态；VQ、代理重构与未来画质均不认证可执行或因果动作。错误future会污染接口，意外状态下仍难及时自纠正，真机收益也非胜出全部VLA。视频、码本、辅助标签producer、动作schema与适配阶段须共同绑定，全部生成/训练/采样计费，部件latency之和不替完整控制deadline。未来或码本支持失配时，保留直接视觉条件、真实动作监督、短horizon和原controller，不由更像动作的latent越过真实反馈与安全层。

拟本人注：`SF-2026-ARXIV-2605-12167` — Daily05-14补May13；exactv1 §3–5/A1–3/A5及A6必要反侧，2+1+2=5，onlineimaginedfuture→specializedIDM mixture/actionhead gap深入。保代理非实测/非因果、容量预算/表与attempt人口、真机π.5反侧、wrongfuture/纠错失败、module sum非总latency及全费；不授可执行latent/安全/真实deadline，未核实现/复现。Source/date/owner/PRE/POST待。

## A27. V2V-Zero 12271（5分）必要Source / owner / PRE（待root）

实际exactv1 §3–6/A/C–E/I必要：visualspec page是用户约束文档、仅进VLM visionencoder，**不是供VAE重构的edit source**。Frozen QwenImage2512/Qwen2.5VL7B final L28hidden，ImageHSonly直接取图像位置；FullFinal另greedy生成reasoning后teacherforcing再算一次统一context的finalhidden，concatvisual+reasoning注入promptslot。内部state必须可读，非blackboxAPI任意把image换string。VideoHunyuan1.5按原pipeline倒数第三层并pad/truncate，不能统一“所有必须最后层”。无weightupdate≠免费：VLM解码/全recompute/更长condition/渲染与全denoise均计费。

GenEval全553×4=2212 main .85低于reproducedtext .86/official .87，且two/count/attr等反退；diagnostic102×4=408的71.57→86.77仅模式对照，150tokens最佳，full553则200优一点，不能混分母。Template偏描述/大font/height比例导致崩退，需绑定render/层/模板/tokenbudget而不单identity。95%attention只一个inlinecolor样本/选blocks，266/466visualtokens，不授全部任务因果或不经文字；cosine/tokenmaxR@1也非信息theorem。A文本检索pool controls显著变差，purecolor近chance，保反侧。

SimpleV2V七类22prompt×4、1024²/30step/CFG4/seed42/200tokens，Qwen3VL32B judge min(Q,A)代理/noCI，32.7仅强于部分open models，pose13.3/sketch16.6失效，商业模型更好。Video616个33frame480p/20step/seed42，judge取8uniformframes覆盖时间范围，不是逐帧全视频motion/temporal验证，20.15低于image。Hardware/precision/batch/concurrency/SLO未披露，未核script/代码/复现。

日期精确v1historyMay12 15:35:34Z与sameDOI findable/arxiv.content registeredMay13 02:45:22Z，组合May13待rootactual。实际Ch24 249–282完整condition混合/cleanreference/UniVidX/SCD局部及1469–1471featurebridge两段比较：旧文是denoisercleanreference或有训featurebridge，不含**直接复用既有VLM→DiT trained conditionhidden读spec page**。拟唯一MULTIMODAL-GENERATIVE-PARADIGMS，cleanreference 2506.24085完整段/独立marker后、UniVidX段前一段。

拟逐字正文：

> 视觉条件还可以是一份要解释的specification page，而非待保真的edit source：在已有VLM-conditioned生成器中，让原视觉encoder读取布局、色块或示意，再把兼容的VLM hidden states交原DiT条件槽。可另生成reasoning tokens并统一重算visual/文字hidden后共同注入，但这不是把页面只翻译成文本。[V2V-Zero的受限对照](https://arxiv.org/html/2605.12271v1#S3)支持复用这一接口，不保证任意层或模型兼容；模板、字体、render比例、层和token预算均影响结果，单样本attention比例不授因果。全量GenEval仍略低原文字路径，结构/pose控制与video时序评价更未闭。渲染、VLM解码和重算、更长条件及完整采样都计费，无新训练不等免费或黑盒API可用。接口、结构遵循或净费用失配时，保留原text prompt、显式结构控制或已验图像编辑，不把可读取的hidden当真实几何或全场景条件语言。

拟本人注：`SF-2026-ARXIV-2605-12271` — Daily05-14补May13；exactv1 §3–6/A/C–E/I必要，2+1+2=5，specpage→兼容VLMconditionhidden gap深入。保非edit source/非blackbox、full/subset分母、单例attention非因果、layer/render/预算反退、8framejudge非完整时序与全费；不授通用兼容/几何/免费，未核实现/复现。Source/date/owner/PRE/POST待。

## A28. GuidedVLA 12369（5分）必要Source / owner / PRE（待root）

实际exactv1 III–VI、C/D/F/G/J/L/M/P/Q必要：在action attention旁路内分head：object平均attention对stage mask的mass作负log，skill对futurehorizon软标签分布作KL，depth指定head仅读冻结DA3 small下采样KV、不是同一个depthloss。原action主链仍在，复制的controlbranch经zero投影残差；只保证训练初态同函数，后续与adapter不保证无损。Object/skill标签Qwen3VL+SAM2传播+人工纠正，depth部署encoder仍付费；不是trainingfreeplug-in或三条独立因果通路。D的skill‘accuracy’是正确类概率均值并用额外loss调target，非硬分类准确率或无混杂干预；objectmass与noise替depth也是代理。tSNE分簇不认证decoupling。

π0/3viewSigLIP224²/PaliGemma2B/actionexpert300M/H50，LIBERO先无指导FT再guided，8H200globalbatch64/mixed训练、4090视觉bf16/actionfp32；RoboTwin8task各1000demo、4H200/batch16/30k、每task100rollouts。六真机task各约50demo、2H200、每setting20trials、120s上限/1sdwell，20Hzchunk插值50Hz并等joint convergence4s timeout，不是model20Hz实时。Scene只加3–5不遮目标/不堵路径distractors，lighting不致视觉歧义，各shift不组合；不是开放世界或化学安全流程，heatbeaker仅放置器皿/网架。Hardware如上但完整latency/重复训练seedCI未披露，不补净速度。

核心T1 full language62.6<π0 63.1、noise85.2<skillonly88.4、Object80.9<objectonly82.5，不能allfactor/all切片更好；F层3quartile优于alllayer但长任务部分另setting更好，不固定‘越多指导越好’。Closest sharedheadmixture同设对照支持分配，仍不授语义因果解耦。P是**baseline失败**案例，不改称本文已证明消除所有碰撞/phasecollapse；Q手工factor选择domain依赖/force未覆盖。完整标注/DA3/旁路/训练/闭环回归计费，未核代码/复现。

日期精确v1historyMay12 16:38:40Z、sameDOI findable/arxiv.content registeredMay13 02:47:47Z，全May13待rootactual。实际Ch26 370–392完整mediator三段、12772完整旁路段与后CRAFT/posebottleneck两段：旧旁路未覆盖**在同一action旁路内按head分object/softskill监督与depth专属KV入口**。唯一MULTIMODAL-EMBODIED-VLA，拟12772完整段后→CRAFT段前一段。

拟逐字正文：

> 同一action旁路内部还可以按head分配不同的条件与监督：一组以阶段对象mask约束attention mass，一组以未来短窗的soft skill分布监督读出，另一组只读取深度encoder产生的K/V，再经零初始化投影汇回原主链。[GuidedVLA的受限对照](https://arxiv.org/html/2605.12369v1#S3)支持区别这种分配与所有heads混合所有目标，但注意力集中、probe或tSNE不认证因果解耦，零初态也不保证训练后行为无损。Mask/skill仍需模型标注与人工纠正，depth encoder在部署保留；手工factor可能遗漏接触与未知阶段，部分语言和单head切片仍更好。标签制备、辅助encoder、旁路、训练及实机回归全部付费，20Hz动作表示/50Hz插值不等模型实时deadline。Factor支持或闭环质量失配时，保留原policy、普通旁路/更完整观察与独立controller，不让更可分的heads取得物理提交权。

拟本人注：`SF-2026-ARXIV-2605-12369` — Daily05-14补May13；exactv1 III–VI/C/D/F/G/J/L/M/P/Q必要，2+1+2=5，action旁路headfactor/KV入口gap深入。保soft概率非accuracy/heatmap非因果、人工与DA3全费、语言/单head反退、受限shift/20trial与执行时钟分责；不授training-free/安全/实时，未核实现/复现。Source/date/owner/PRE/POST待。

## A29. CausalCine 12496（5分）必要Source / owner / PRE（待root）

实际exactv1 §3–5/B–D：先以multi-shot长序列2N clean/noisy teacherforcing调causal，再ODEinit/DMD+GAN成4step；per-shot text交叉attention只读当前caption。每层framekey spatialmean与chunkqueries mean打分top5历史frames，保近3chunks；cache存未旋转K，query时把选中memory/近窗/current重新compact RoPE，不能write-time固定rotate。Bound只限一次attention人口，描述符对**全部**旧frames打分、完整历史KV保存/检索仍增长，原文未给淘汰策略，不能说totalmemory/routework常数。Content相近不是entity/physicalstate真值。

Wan2.1T2V14B、832×480、100k约15s/241frame多shot、64H800训练。与1.3B等baseline参数/预训不齐，100Gemini2.5Pro五shotprompt常规集与另100memory-reappearance集分开；DINO/CLIP/ViCLIP/TransNetV2是proxy。T1background.9675<selfforcing.9717，T2text/intershot低于HoloCine；T3nomemorySCA.9772>routing.9745且sink美学更好，B4steptext/intershot低于50stepbase。T3skipcausaltuning还同时移除longmultishotdata，不能唯一归训练order。48ODE与B50step口径不同不补统一recipe；C GAN只有定性对照。D8H20016FPS仅分布式生成，precision/batch/concurrency/end-to-endSLO/重复seedCI未披露，不授消费卡或完整交互实时。Coffee跨cut细对象/手/奶流不连续明确，不把叙事身份当worldstate；全数据/teacher/critic/cache/search/codec计费，未核代码/复现。

日期精确v1Atom May12 17:59:51Z、sameDOI findable/arxiv.content registeredMay13 02:50:55Z，全May13待rootactual。实际Ch24 109–146完整recurrent/Helios/ShotStream/VACE/Gloria/FramePreservation邻接：旧shotstream按边界重采旧shot与caption，不承载**content查询选旧frame、未旋转K query-timecompactRoPE与全history费用**。唯一MULTIMODAL-GENERATIVE-PARADIGMS，拟ShotStream完整两段后→‘外部参考条件…’前单段，不复制Ch25persistentstate。

拟逐字正文：

> 跨shot参照也可以按当前chunk的内容检索，而不只在边界均匀重采：每层以framekey和chunkquery摘要选择少量旧frames，与近窗共同参与attention；cache保未旋转K，在每次读取后给选中memory、近窗和当前chunk重新分配训练范围内的位置。[CausalCine的受限对照](https://arxiv.org/html/2605.12496v1#S3)支持这一条件接口，但固定attention人口不使全部历史KV、摘要检索与存储成为常数，content近也不保证实体或物理状态相同。长multi-shot causal训练先于少步蒸馏的比较还改变数据/teacher支持，局部质量与cut指标仍有反退；跨cut细物体与接触连续性明确失败。数据、全history、检索/重定位、teacher/critic和codec均计费，多GPU生成FPS不签完整交互SLO。召回、状态连续或总预算失配时，保留较长近窗、显式reference/shot采样与较短生成，不由bounded attention或叙事一致性批准persistent world state。

拟本人注：`SF-2026-ARXIV-2605-12496` — Daily05-14补May13；exactv1 §3–5/B–D必要，2+1+2=5，contentframe routing/未旋转K与query-timeRoPE gap深入。保bound只attention非全KV/检索work、训练order/data混杂、指标反退/跨cut物理失败与全费；不授常数totalmemory/worldstate/生产实时，未核实现/复现。Source/date/owner/PRE/POST待。

## A30. 3D-Belief 11367（5分）必要Source / actual具体NC提案（待root）

A15决定性§3已由root实际准入5，本次补actual exactv1 §3–5/8.2/9–10必要评价：observedGS随新RGB/pose累积，imaginedGS每次舍弃重采，不把自产补全递归当新增观测；3hypotheses渲染候选路径，semanticqueries打分、A*执行短prefix重观测。3DGS是派生估计非原始事实、sample人口不是已校准Bayes posterior；Eq1不作为完整Bayesianfilter recipe。Observed pool仍增长，不把短pair训练变常数整套内存/计算。静态world限定，不授动态接触状态。

一H10080G/batch1/250k训练，初始化DFoT/MVSplat，混合SPOC/RealEstate/DL3DV/Habitat与CLIP/DINO/VGGT辅助监督；各baseline训练/硬件不同（oursH100、其他多数A100），2.14s/step非公平纯模型加速。3DCORE233object/263room/474permanence，语义/物体seg部分Gemini、IoU只双方已知cells，returnrender指标非完整physicalstate。Sim135unseenhouses但episode表SR对应分母不统一披露，不补；T8episodeWilson/bootstrap非训练seedCI，SPL区间大量重叠、SEL40.24低于Gemini41.47。Ablation人口SR45.83与main59.17不同，singlehypothesis35.14不可跨表直接量化成main收益。Real5objects×3starts、成功55.56 vs23.08没有完整相同trial分母/CI，不补；实际§9.2.2虽然声称RGBonly，却用senseddepth对preddepth按sequence robustscale，不能写纯RGB metric真实闭环。模型precision/batch/完整pipeline latency未完整披露，未核实现/复现。

日期v1historyMay12 00:42:27Z，sameDOI findable/arxiv.content registeredMay13 02:23:09Z全May13待rootactual。实际Ch25 560–612完整objectmemory/observed→belief→imagined与supersession、LiveWorld离屏imagined非观测；722–748 Stateownership完整、1484–1500 hypothetical/observation-backedcorrection完整局部已读。当前正文已明确Worldmodel拥有**ephemeral predictedstates**、不得把预测写observed，belief由新observation reconcile/supersede，hypothetical与observation-backed字段分离；本项具体resampleGS是这些合同的静态3D实现验证，未发现需另加长期规则的差额。拟**已有覆盖—MULTIMODAL-WORLD-MODELS Ch25上述三处**，无新增书段/注，不把主题相同当NC：对应采用命题恰是imagined可抛弃、新obs优先与sampling不能自证事实，原具体论点已完整承载。保5分及必要深入，不为NC降分；请rootactual必要证据与owner确认。

## A31. AffordMem 11616（5分）必要Source / owner / PRE（待root）

actual exactv1 §3–5/A/B：query拆contextpart labels与spatialqualifier。跨scene bank由**source场景标注3D类点**投影回其自身帧、depthmedian/MAD过滤+convexhull/top20中心/距离选视角，作为categoryprior maskedexemplars，不是往target套GT。Exactlabel检索后Qwen3VL32B正core/负connectedpart boxes，SAM3仅消费positive；target posedRGBD多view投票/DBSCAN产生3D candidates、centroid/AABB/partof图和topdownnodeID+crop再选qualifier匹配实例。类别prior只帮粒度，当前scene candidates才承载实例；VLM/node/geometry均为派生，不授操作可达或物理成功。Eq5所谓Wilsonlowerbound未完整定义，仅nfg/nvis>.7不照配方。

SceneFun3D230scenes、split0 30/split1 200反向bank，sourceannotation与target不重叠但**有标注先验**，不写annotationfree。SAM3单A10080GB，语言推理hardware/precision/batch/完整调用量/latencySLO未披露；平均1800RGBD/scene。T1priorbaseline引用各论文不同protocol，AffordMem AP50 20.13<TASA26.9/AffordBot20.91。消融在按fullmethod强/中/失败分层选的subset而非随机全场景，T2去AP的AR50 38.02>full37.19，T4K5 AR50>20，更多bank也可退。T3MGGrounding同时含VLM/正负prompt/bank，A声称无maskVLM更好却该表仅SAM3vsMGbundle，不能归bank单因果。Exactstring陌生类无prior、static/dynamic未验、scenegraph只几何不含材质/状态；所有预制/标注/投影/LLM/SAM/融合计费，无robotexecution/代码核验/复现。

日期v1 Atom publishedMay12（具体time见原topic精确v1，待下方逐字段回读）+sameDOI findable/arxiv.content registeredMay13 02:29:19Z，需核uniquev1下界。actualCh23 1555–1595完整OpenVoxel两段（part被merge丢失）、后对象/邻居/全局分路两段与partialbinding两段，缺**sourcecategorypartprior与targetscenequalifier实例选择分责**。唯一MULTIMODAL-REPRESENTATION，拟OpenVoxel完整两段后→‘实例身份明确之后…’前单段，非Ch77通用memory/Ch26控制。

拟逐字正文：

> 细部指代还须把“哪类部位可操作”与“当前场景究竟是哪一个”分开：从其他已标注场景投影制备类别级part示例，先帮助视觉模型提出小部位；再由当前多视图RGB-D融合出实例候选，以位置、parent关系和空间qualifier选择node。[AffordMem的受限对照](https://arxiv.org/html/2605.11616v1#S3)因此不把source类别prior当target实例GT，也不让同类外观替代ordinal/关系条件。该分工仍依赖标注bank、分割、pose/depth与语言解析，exact-label未见类可能无prior；消融同时改变部分grounding路径，不能授每组件唯一因果。预制示例、投影/融合、多个模型读取与选择均付费，局部分割/AP不证明接触可用或机器人执行。类别/实例支持、空间对应或净费用失配时，保留原视图与细mask、显式候选及Unknown/专用几何核验，不由图或“memory”名字取得物理动作权限。

拟本人注：`SF-2026-ARXIV-2605-11616` — Daily05-14补May13；exactv1 §3–5/A/B必要，2+1+2=5，sourcecategoryprior/targetinstancequalifier gap深入。保有annotation非targetGT、投票式未闭、bundle消融/AR反侧、受限subset/静态类支持与全费；不授bank因果/无标签/robotexecution，未核实现/复现。Source/date/owner/PRE/POST待。

## A32. VIP 12325（5分）必要Source / owner / PRE（待root）

actualexactv1 §3–5/A/B1–2/C必要：frozenDINOv3 ViTL+dino.txt adapter，以GPT5每类20aliases（cos<.7先删），用多层DINOaffinity randomwalk前后activation的softIoU一致性VG与高actpatch跨类entropySC两代理；alias必须相对canonical同时VG更高/SC更低。**整个testset**求均值、仅act≥.4且有高act的image才计，各alias有效人口不同，是transductive而非单请求在线泛化。Canonical保留，按globalresponse softmax重权aliasmaps再logsumexp；不是可靠语义共识/最优alias或真实geometry。

八natural/urban+四remote测试；resize短边336/City560、window224/stride112；4090、precision/batch/完整新testset延迟未披露，单seed重复CI未给。MainTable1 VOC73.2<CorrCLIP74.8/Context41.2<44.2，非alltask优势；T3直接加aliases均值38→37.6、Object31.4→28.6，过滤后才改善；B1categorydescriptor过滤后仍差、C confusablewall/lowres未闭。视觉自校正+新backbone+alias/aggregation顺序组合，和CLIP异底座对比不能唯一归aliasfilter；GTmasks只用于featurediagnostics需与无maskselection分开。A1所谓offline distillation其实先读完整testimages，可cachemaps再aggregation报Table1成本；旧testset100ms/1650MB不能报价未来单新query，GPT5生成/全set编码、affinity驻留/筛选/聚合全费。无代码核验/复现。

日期v1historyMay12 16:08:18Z+sameDOI findable/arxiv.content registeredMay13 02:46:42Z全May13待rootactual。ActualCh23 206–259完整CC-CDFSL两段/类原型校准/PRMaGIC与transductive原型等近文已读：现是有label局部对齐或无label支持更新读出，不拥有**canonical-relative双代理筛选文字alias与测试集合人口**。唯一MULTIMODAL-REPRESENTATION，拟CC-CDFSL完整两段后→‘冻结多模态编码器时…’前一段。

拟逐字正文：

> 不更新视觉权重时，密集读出也可以先筛选类别文字，而不直接吸收所有生成的同义描述。比较每份alias的activation在视觉affinity传播前后是否一致、以及高激活区域的跨类entropy，只保留相对canonical同时改善两代理的候选，再保canonical并聚合。[VIP的受限对照](https://arxiv.org/html/2605.12325v1#S3.SS3)显示未经筛选的扩词可退步，但这些代理不是geometry/语义真值，低激活和无激活图被排除还改变每个候选的评分人口。原筛选读取整个testset，属于transductive条件；不能把已缓存该集合的map聚合成本，报价为对未来新query免费的在线推理。文字生成、全组编码/affinity、筛选和最终聚合都计费，易混类与低分辨率仍可能失败。集合访问、类别支持或净质量失配时，保留原canonical/模板、较简单读出和真实局部监督，不由更多aliases或较低entropy批准无损语义与通用泛化。

拟本人注：`SF-2026-ARXIV-2605-12325` — Daily05-14补May13；exactv1 §3–5/A/B1–2/C必要，2+1+2=5，canonical-relative双proxyaliasfilter gap深入。保全testsettransductive/.4与不同有效人口、proxy非truth、未筛扩词/descriptor与主表反侧、旧cached cost不授futureonline及全费；不授无损语义/通用部署，未核实现/复现。Source/date/owner/PRE/POST待。

## A33. MMProLong May13官方公告（5分）后到必要佐证 / owner / PRE（待root）

家族事件只有Seed May13官方完整摘要公告，root已actual核心/独立日期通过；后到`2605.13831v1`不是May13首稿，不搬提交/公开日。现仅把该精确后到正文作为公告已披露**VQA优于OCR、长度分布/任务混合、短能力保留与训练长度外泛化**的必要方法/评价佐证，不把新恢复出的数据生产细节另算May13贡献。actualv1 §3–7/8/9.1–3/11.4/14.1–3/14.7/15必要，其余视频/所有附件无关域未扩读。

Qwen2.5VL7B由32→128K、每recipe固定5B（二进制）token/global4M32seq，mRoPE1e6→4e6；VeOmniFA/Ulysses2FSDP4、实际64H20、约2.9kH20h属单run训练，precision/完整生成judge/data费用未披露。VQA与OCR不同目标/response长度且OCR额外5B SFT，不等总compute匹配；VQA强于所测OCR路线，不证明OCR无价值。Lengthpoolnative对longbiased近同token而非同unique覆盖，Table14 extractmulti128K长偏55.84略高native55.77，平均+0.1不授全切片或显著。8:2混合是小grid验证结果非通用最优，0shortmean66.47→65.48，MMMU/MathVista/OCR退，不能‘无损短能力’；shortmix20%均值更好但长降，40%是折中。roPE8e6某单数据更好但均值反退，不照固定普适倍数。

MMLongBench v1.1 macro跨三dataset/两length、简单答案binary/listF1 judge不检查中间推理，模型judge版本与完整inferenceHW/precision/token budget未全披露，未给重复trainingseed/CI。256/512K是在左右padding负文档扩长度，不是原生复杂依赖长文；不能把训练外分数直接泛化真实512K跨页推理。100QA人工抽查97correct有限非全数据真值；PDF SHA去重不能排近重复/改写污染。Qwen3VL8B本来256K/100BLongPT且额外SFT/RL，仅recipe转移不是再次窗口扩展。保posterior/cost/所有性能广告边界，未核实现/复现。

actualCh27 132–174完整mixture/监督权重与1233–1246完整长上下文支持/干扰两段、后文档双侧门两段；Ch26交接此前已读、Ch28开头1–42补读。旧长窗数据是文本support/distractor动态选择，不拥有**多模态VQA/OCR目标×lengthdistribution×短长混合的固定token取舍**。拟唯一TRAIN-DATA，长上下文支持/干扰完整两段后→PerturbedDocuments原binding前单段，不在Ch22重复序列实现/Ch23视觉表示。

拟逐字正文：

> 多模态长窗还要联合选择监督任务与长度分布，而不只把样本拉到目标上限。[Seed的May13公告](https://seed.bytedance.com/en/public_papers/training-long-context-vision-language-models-effectively-with-generalization-beyond-128k-context)提出以长文档VQA、较分散的训练长度和偏检索的任务混合校准图文距离；[后到精确正文的必要对照](https://arxiv.org/html/2605.13831v1#S5)仅佐证这些已公告命题：同token下优于所测OCR路线，不等OCR普遍无用或总compute完全相同；更多近上限样本、推理比例或短样本也不单调更好。纯长VQA仍有短任务退步，混入短数据是质量折中，某个比例不是通用配方。数据制备、所有recipe搜索、长窗训练与judge均计费，训练外padding长测不认证任意更长文档依赖。任务、长度支持或短能力回归失配时，保留原OCR/短数据、较宽length分布与独立短长评价，不由上下文上限或平均分宣布无损长窗能力。

拟本人注：`SF-2026-SEED-MMPROLONG` — Daily05-14补May13独立官方摘要公告5分；后到13831v1仅§3–7/8/9.1–3/11.4/14.1–3/14.7/15必要佐证公告已披露命题，非May13首稿。2+1+2=5，VQA/OCR×length/shortmix差额深入。保同token非完整compute、切片反退/短能力损、padding外推与judge/污染边界、全费；不授普适ratio/无损/任意512K，未核实现/复现。官方事件准入/date已实际通过，Source/owner/PRE/POST待。

### A34. 日期与有限发现尾的恢复清单（仍进行中）

root已actual同May13有效日期：11367/11616/12167/12271/12325/12369/12496；其中11616原API精确v1 published=updated=`2026-05-12T06:44:47Z`，12167=`14:15:16Z`、12496=`17:59:51Z`，均是Atom原提交字段，不把未取abs的API写成完整网页history。A31尚待下方v1字段回读的日期待办由此关闭。11367具体NC实际通过生效。11817/12038/FIS/SCOLAR实际POST通过，相关窄位释放，未变化证据不第三重复。

12586/12587跨日资格隔离：sameDOI findable/arxiv.content registered实际May14 02:12:10/12Z，虽v1submitMay12 17:57:21/17:59:27Z，下界May13上界May14不可截取；fresh官方cs.CV月目录8218bytes拦截页不作日证，定点搜索SciRate提示May14仅线索。重开需直接官方May13公告或能缩定日期的原始早正文证据；不计本日确定候选/Source，不展开全文，不代May15搬日。

本日仍可执行的具名Source/Books：MoLA12167、V2V12271、GuidedVLA12369、CausalCine12496、AffordMem11616、VIP12325、SeedMMProLong的各A26–33必要原证/owner/PRE已准备，root独核与所需窄写/实际POST尚未完成；当前不是受阻。下一批发现仅既取model201/system19/agent264去原291身份后的相关标题有界浏览所得20项完整题摘：11182/11396/11609/11613/11689/11726/11854/12288/12476/12483/11212/11374/11416/11739/12058/12258/11853/11946/12233/12334。仅决定题摘准入，不预授Source、不将其余宽列表转队列。机构到期有限入口已完成，历史无法恢复段按实际原件隔离，不扩站/整月。后续将本日志真实层合入README六部分；旧130候选与原§4保护，不重做旧714。

## A35. 有限发现尾20项完整题摘准入提请（Source未展开）

已实际读所列20完整题摘：当前Atom有新版的14项额外取并**只读精确v1 HTML title/abstract**，不能把新版题摘当v1；其余11609/11613/11689/12476/12258/12233原Atom当前v1 published=updated可复查完整题摘。本轮不是旧130/714全文队列。每项拟2+1+2=5，日期sameDOI均findable/arxiv.content registeredMay13已actual核，具体uniquev1史还在有限恢复，不先宣布全部date完成。

| ID | 约束→完整题摘的实际增量→可能改变选择（均待root独立准入） |
| --- | --- |
| 11182 | OPD不稳定不能只归dense信号不足→TopK reverseKL偏梯度与instance-specific PI部署缺失分开→选择stopgrad/teacher适配与PI类型，非所有selfdistill都失败。 |
| 11396 | Muon正交化对方向误差敏感→norm/主奇异分量单独量化与μlaw密区精度→优化器state量化不能照搬outlier保护；‘误差只改奇异值不旋方向’需理论核，不采摘要保证。 |
| 11609 | 特权答案自蒸馏压deliberation→反号divergence+teacherentropycollapse gate→何时不应模仿teacher局部置信，非通用antiKL最优。 |
| 11613 | feedbackpMI可由输入无关shortcut提高→batchcontrastive teacherbaseline隔离input-specific分量→densecredit不等当前input贡献；posteriorcompatibility假设待核。 |
| 11689 | MoE各旋钮被孤立调参→2000runs expertcount/granularity/shared/dropless交互与active-budget条件→优先调哪些变量是具体可复用边界，不因仅局部模型或经验性排除。 |
| 11726 | dLLM训练blocksize非仅推理粒度→跨domain最佳训练block冲突、sample-levelblock选择→固定block训练可能损多域；41k数据/7算法名非单独准入。 |
| 11854 | dLLM randommask训练不见easy-to-hard顺序→自产轨迹entropy Boltzmann pairwiserank→保完整decode能力与少步压缩目的分开。 |
| 12288 | sequence BradleyTerry未给perprefix最优→token-level模型/Bregmanratio+statebaseline或归一化→怎样从sequencepairs训练局部policy及其假设，而非直接宣称原最优性。 |
| 12476 | auxiliarybalance会改routerexpert几何→input-directedgradient共历史/aux破耦与onlineKmeans router反证→不能把balance与specialization独立选择，质量代价待核。 |
| 12483 | 同size student直接稀疏RL可能弱→同teacher RL前后迁移排序反转、forwardKLwarmup+OPD后studentRL条件→scarcelabels投在哪个consumer是具体条件证据，不采‘大teacher永远好’或仅四模块加法。v1只math，不采新版code实验。 |
| 11212 | GUI history饱和可能是重复patch预算而非无用→相邻screenshot learnedselector保空间结构→同预算history是否有益需重验，不由46%/3%数字本身准入。 |
| 11374 | frozenembedding不必无testtimecompute→v1程序搜索归结query/topKdocsoftmaxcentroid插值→no-weight retrievalconsumer可替代重训；**current题摘已改成12Paretoprograms/144而非v1单algebra/259，具名实质修订信号须必要域对比，不复述v1 allfamily/alltask保证**。 |
| 11416 | continuedPT默认全参/训深→定位层敏感/执行位置后浅训深冻对照→layerallocation具体反证，‘深层普遍稳定’不直接采用。 |
| 11739 | OPD少step非只dense稳定→早期update低rank/最终subspace对齐、adaptiveextrapolation→训练加速可分更新方向与实际loss，3×需全费及反证。 |
| 12058 | sequenceprob聚合固定造成collapse/稀疏signal权衡→Höldermean p连续调梯度集中/variance→annealp何时有意义；理论strictvariance须假设核。 |
| 12258 | objecthallucination只看visualembedding可能误读→instructiontokenvisualreadout+local/contextscores→detector取哪个state与对象上下文一致性；不是泛泛两score组合。 |
| 11853 | divergence spike后错误续文可又lowdiv→以spike锚自适应creditsegment而非逐token继续信用→teacher差异不能逐点解释错误责任。 |
| 11946 | skill passrate不变可能掩行为和费用变化→同task有/无skilltrace按phase对齐、SIP标注→饱和人口与模板复制/额外artifact/恢复代价分账；不是仅新增benchmark。 |
| 12233 | blanket拒绝env指令也可假robust→同task必要cue+irrelevantdistractor双条件、六防御权衡→agent reliability须同时验恰当使用与越权，不以拒绝率替完成；安全设计反证深入。 |
| 12334 | world/reward task-specificFT妨碍复用→taskfreebehaviorworld+offtheshelfVLMreward、dualnoise过滤→是否能零task适配模型地训练policy及filter共错边界，非任务名换皮。 |

上述只把有具体增量的具名项提独立校准，未按性能或机构/新名字准入，未读必要方法/对照就算Source。机构/已处理topic的有限发现到此停止，不扩其余宽命中；当前普通尾是这20项的独核准入/日期和通过后必要Source，再与既有7项PRE收敛。尚无本轮DAY/FINAL。

## A36. 到期来源有限停止范围汇总（发现封口，非无遗漏证明）

本轮机构原件均在`sup-raw-20261019/`，下表并入README时仍须自包含依据/缺口。A3/A11的“待恢复”是历史运行点，由本汇总实际结果取代，不把旧进度句误作现待办；未恢复的历史段不支持正面Coverage/Evidence/Books。

| 来源 | actual入口 / 停止范围 | 本窗结果与保留限制 |
| --- | --- | --- |
| SRC-OPENAI | 官方RSS May13两item与TanStack官方完整core，当前June26 amendment另标 | TanStack新家族6分/Source与Ch72具体NC已实际通过；WindowsSandbox为原候选同事件复用，不新计。厂商未发现不授无侵入。 |
| SRC-ANTHROPIC | Research完整嵌入publication，May8→May14 17:06Z相邻窗口 | 本日Research显示无May13事件；后者May15BJT。不扩product/business使用指南。 |
| SRC-GOOGLE-AI | DeepMind Research fresh core及解压sitemap，Googlepubs官方完整当前首15/11622；具体May13官方proxy Blog及所链旧arxiv | proxy解释文章具体C，论文v1Mar16/v6Apr14无新机制release。DeepMind sitemap lastmod非pubdate；Google当前按year目录不恢复May13完整段，finite站点定日搜索无返回仅辅助限制；保历史research目录缺段，重开需官方日期列表/快照，不以搜索空白证明零。 |
| SRC-META-AI | research curl reset后web原页fresh仅headline/0正文行，定点May13官方域搜索 | 未恢复历史可读目录；有限入口隔离，不称不适用或无事件。重开需可读官方历史列表/具体May13原文。 |
| SRC-QWEN | 旧home跳新blog；浏览器一次超时65s后停止。观察公共chunk定位969.js中的 `/api/v2/article/retrieval`，sameorigin公开GET type=qwen_ai/language=en-US成功40articles，全部40date/title/path已读，Apr30→May19无May13 | 当前投影无该日blog，不证明历史不可删改。11887 QwenScope官网Apr30条及直链完整35pagePDF明确Apr30早稿信号，cover/title/abstract身份实读，未读全文机制；本日首公开资格隔离，不是无贡献C。需要dated早稿/重要v1delta才重开，不为排所有发布渠道无限恢复。 |
| SRC-DEEPSEEK | home→updates当前完整事件序列，Apr24→Jul31相邻 | 当前无May13项；历史更改不可排，非全站研究零事件保证。 |
| SRC-MOONSHOT | Kimi Platform Blog静态目录最新仍Nov7 2025 | 当前无法恢复May13历史slice，未假称本日不存在或随之全GitHub扫史。重开需当日原文/官方dated历史。 |
| SRC-TENCENT-HUNYUAN | Research全部动态列表按观察公开POST publicList，en9/zh11合11唯一题名/日期全部读；页码1/pageSize1000无隐藏下一页信号 | 相邻May21/Apr30等无May13 displaydate；display与实际published有月级错位，不能作为全历史首公开零证明。按可用目录处理，缺immutable历史证。 |
| SRC-ZAI | 官方Research完整当前分类目录Apr29→May20，官方release-notes全部可见headingsAug26/Aug18/Jun16/Apr7/Feb12/Jan14/2025Dec/Sep | 未见May13当前目录/release；不把当前功能倒填。历史移除段不可排，重开需具体datedresearch/release原文。 |
| SRC-BYTEDANCE-SEED | publicpapers首20至May26，观察公开API page_token20/count20并带x-tt-locale:US得到20项/total246/next40，全部读至May10/May7停止，不取older页40；article detail MMProLong完整main摘要/作者/venue/PDF | May13 MMProLong独立摘要事件候选5，后到paper只必要佐证；INSET官方May12摘要与May13paper日期分责。无locale时异常Apr22单行不作覆盖；AIscience窗外不纳。 |
| SRC-BAIDU-ERNIE | 官方blog首10项从May9到Apr30，page2已到2025不继续 | 当前目标段无May13事件，不追历年库。 |
| SRC-XIAOMI-MIMO | 官方home完整Paper8项 June29→Mar13→Feb；Blog15可见cards无date | Paper当前无May13；Blog历史日期段不可恢复，不能由undatedcards证明零。重开需dated官方blog/原文，不补造时间。 |
| SRC-MINIMAX | EN12cardsMay26/27→Mar18；ZH13cardsMay25→Apr27；Agenttech3项Sep19/22/Oct8当前目录 | 主blog两locale目标段无May13；Agenttech历史slice未恢复，非不适用/零。重开需当日dated技术条目，不全站追史。 |
| SRC-ARXIV | May11 18Z–May12 18Z submitted恢复线索，model201（首200+尾1重复核）、system19、agent264（首200+尾64）、multimodal52；原始Atom自URL保主题/页界。相关标题有界浏览后只选A6/A12/A15/A35具名完整题摘；旧291ID机械去重 | 贡献门独立校准后才Source；当前26确定新家族的日证/Source/Books分层沿A4–33推进，后20题摘只待准入。CL/LG月首2000只补潜在May13ID段标题，不全月审；CV日期恢复拦截非覆盖。12586/87跨日资格、Qscope早稿资格保留不记本日确定候选，不由submitted发号顺序推全部日证。 |

表外实际触发：DataCite/arxiv官方availability只定点恢复候选日期，非固定全站；GoogleCloud具体官方Blog仅检验新贡献；无本轮会议正式批次/协议release触发，不扫Weekly组。所有机构到期入口处理到上述有限安全终态；来源历史缺段不授完整Coverage或无遗漏，尚可执行工作集中在已列具名准入/必要Source/写后和报告合并，不再扩大机构发现。

### A35.1 uniquev1日期层已由作者实际补齐（独立待）

14个有新版项精确v1 abs页全部成功并实际读uniquev1史（本日相应`2605.<id>v1-abs.html`）；六个原Atom当前v1且published=updated。20个v1提交均在May11 18Z后至May12 18Z前，同DOI findable/arxiv.content registered全部May13 02:18:33–02:50:36Z；组合最早May13 08BJT与各精度最晚10点多同一May13自然日，不改字段成实际pubtime。11374 v2May13 00:56Z提交是后版本史事实，不取其替v1；必要版本纠正仍待Source独核。所有原件可复查、无withdrawn标记信号，未来升级内容不回填本日。

### A28–29 actual保存（POST待）

rootactual必要Source/date/完整owner局部及原逐字PRE通过后，作者已窄写Guided12369于Ch26 12772后/CRAFT前、CausalCine12496于Ch24ShotStream两段后/外部参考前，各唯一单段/marker/本人注，完整直接两侧与注self-read、限定diff-check通过；actual非作者POST待，不预计生效。MoLA12167/V2V12271已由root实际POST通过释放，日志/本人注只同步既成行政状态。

## A37. 发现最终封口与独立后批准入实际通过

root已实际逐读A35全部20精确v1完整题摘，确认各有具体机制/反证增量，按各2+1+2=5准入，不等Source完成。12258只核instruction-position读出改变detector这一窄问题，不用两score组合自授效果；11374仅当前具名revision受影响程序/全task声称必要比较，非全版本；12483 exactv1只有math，不引入新版code。

确定本轮新增家族**46**（首26+后20），不含12586/87跨日资格、11887早稿资格、12227具体C或旧130。后20作者日期合证已逐字段actual，root独立日期层在核，不先称全通过。所有机构与topic发现至此封口，不扩任何其余宽列表；没有数量/保留率目标。本日尚余可执行：后20 necessarySource/实际owner/最低Books；AffordMem/VIP/Seed已各按root授位原稿窄写self-read通过但非writerPOST待，前19实际整合与2NC/2争议有效；报告六节合并及DAY/保存态FINAL尚未做，不以当前进度停工或称完成。

## A38. Many Faces OPD 11182（5分）必要Source / owner / PRE（待root）

actual exactv1 §3–7、A1–2/A4–8/A22–23必要。主要采用独立可核的**截词表RKL梯度合同**：固定当前prefix及TopK集合，fullvocab Σq∇logq=0，而未归一support仅ΣSq=mass，+1项不会抵消。Stop-logq改变为surrogate、support重归一只匹配内部相对概率且丢总mass、sampledtokenPG信号稀疏，三者不可都称exact fullRKL。A4明确忽略rollout-score term，局部梯度不等整个onpolicy objective无偏；A5 sampledtoken推导把trajectory乘积简化为同t项未保return-to-go跨项，**不采用该完整梯度recipe**。SGLang当时token_ids_logprob单flatlist需跨position union，T×union费用不等T×K；intersection是换support的近似，未核具体API代码，不宣称现版本仍相同。

正反：Qwen3 1.7/4/8/14B，OpenThoughts/DAPO，10RTXPro6000Blackwellserver；OPD/OPSD64prompt×1、4096rollout，GRPO32×8/8192，不因same sampling文字就补同token/总compute。Evaluation16k/T1/topP.95，optimizerAdam/2e-6，OPDprecision未披露（SFTwarmup另4卡BF16/FA2/2epochs）。K5/20 unnormcollapse vsstopgrad/renorm近设对照支持局部故障；nonthink/think、teacher强化/SFT都须分版本，early快不等最终ceiling。A22GPQA198 deterministicprefixcontinuation teacher123correct→91，40wrong/8improved，但format98.48→78.79%且strictparser，无法将全部下降唯一归reasoningstate。A8 eval截断偏差、预算与RLceiling反侧保留，无多trainingseedCI/完整wallclock。

PI理论额外限定：§5.2 Eq11是**给定同x**对I条件分布取几何均值，不能因不同题x各有不同I就证明instance-specific PI必然不可蒸馏；若I=f(x)，D(I|x)为点质量，该公式没有跨不同x强行平均。经验数学PI受限失败有效，但不作全部OPSD能力不可能或该推导已解释原因的书段。主文sharedrule成功与math失败并存，不用此缺口否定TopK独立可核机制。未核实现/复现。

Date原件已列A35.1，root独立date待。actualCh29 324–347 tailmass/DRKL完整两组、455–476PI与GUI段、557–573StableOPD/tokenpopulationselection完整局部；Ch28intro已读/Ch30开头沿此前未变交接复用。现有文区分词表与token位置/normalization，但没有**unnormalized截词表mass梯度残项与三个surrogate不同目标**。拟唯一TRAIN-SFT，在DRKL完整两段后→cross-tokenizer蒸馏前一段；不把PI不可能论或错误完整PG移入Ch33。

拟逐字正文：

> 在每个已采prefix上截词表，还会改变reverse-KL的梯度而不只是省logits：全词表的常数项因概率总和为一而抵消，未归一TopK支集的总质量仍依赖student参数，这个残项便不再为零。[Many Faces OPD的受限对照](https://arxiv.org/html/2605.11182v1#S6.SS1)支持局部稳定化，但停止log-prob梯度得到surrogate，支集内重归一丢弃总mass，sampled-token policy-gradient又只保稀疏信号，不能都叫原full-vocabulary目标的精确实现。集合、normalization、detach与rollout处理须共同绑定，改用两模型TopK交集也改变支持；跨位置查询union还可能交回显存收益。Teacher前向、全部rollout、概率与验证费用仍在，局部不崩溃不证明事实、完整on-policy无偏或最终能力优势。支持过窄、质量或总预算失配时，扩大支集、保全词表/已验采样目标与可信SFT，不由较低KL批准通用稳定。

拟本人注：`SF-2026-ARXIV-2605-11182` — Daily05-14补May13；exactv1 §3–7/A1–2/A4–8/A22–23必要，2+1+2=5，unnormalizedTopKmass梯度/不同surrogate具体gap深入。保局部非全onpolicygradient、PI条件x不能跨题平均/A5不采、prefixparser混杂、rollout预算/ceiling与union全费；不授PI不可能/稳定无偏/净加速，未核实现/复现。Source/date/owner/PRE/POST待。

## A39. 既成状态同步与后批三个必要Source/PRE

root R12–14实际通过：首26＝22实际整合/纠正、TanStack与11367两具体NC、11134与11871两中心争议终态；Afford/VIP/Seed actualPOST已过释放，旧A34/A37的待POST句只属历史。后20的精确v1/同DOI组合日期也已root逐项实际通过，同May13BJT，禁止重复GET日期/扩发现。11182 root必要Source/完整DRKL邻接与A38逐字PRE已实际通过，作者已保存唯一单段/本人注并顺读完整局部，actualPOST待；作者A22等与root实际读域在注内分开。

### A39.1 MuonQ 11396：有限经验分支，不采精确保方向

作者actual exactv1 §3–4/6、A1/A3/A6必要。将gradient和momentum单位化后，poweriteration warmstart抽top-k分量，U列/S行与residual分别量化、μlaw细化近零bin，NS5再产生更新。三强句隔离：elementwise量化U列/S行仍可改变向量方向，不能保证只改singularvalues；单位化G/M改变跨step相对权重，极近loss曲线不是相同方向/动力学证明；等范数误差不推出独立、零均值、各向同性。保这些不是否定有限经验分支。

GPT2small124M/Medium/Large、LLaMA350M/1.1B，FineWeb1/5/10/6.4/13.1Btokens，8/32A100 BF16mixed，AdamW仍管embedding/head。T7把名Muon32 bitwidth写16，不能补造全FP32recipe。T3同small1Btoken组合PPL40.9仍高baseline36.4；主表四model Avg均低Muon32（41.7<42.6/43.3<43.8/42.2<43.3/45.2<47.1），不照录无损；A3aligned40.93<across41.30局部支持granularity，rank增大换memory；7.3×仅optimizerstate，不等全训练HBM/墙钟。poweriteration/NS、metadata/scale与全部搜索/回归付费，frontier/distributed与完整cost未验。root已实际§3/4/A3独核支持此窄边界，作者额外域不冒称root已读。

actualCh28 616–632完整state/friction/embedding/4bitAdam两段和1201–1219完整preconditioner→SOLO两段→Gauge交接；Ch27/29交接沿本日已读未变复用。现文没有**正交化前按dominant奇异分量量化并分配dense-center bins**这条state表示分支；非物理offload或inference量化。拟唯一TRAIN-PRETRAINING，SOLO完整两段及endmarker后→Gauge标题前单段。

拟逐字正文：

> Momentum随后还要经过近似polar map时，量化误差应同时按重构与更新方向验收，而不只保护大数值。一个受限分支先归一当前gradient与历史momentum，再用warm-start power iteration分离主奇异分量，对U列、缩放后的右分量行及residual分别编码，并以μ-law在密集近零区分配更多精度。[MuonQ必要对照](https://arxiv.org/html/2605.11396v1#S4.SS2)支持有限模型中的state质量—内存取舍，却不保证逐元素量化只改奇异值；归一也改变跨步相对权重，loss接近不是原动力学等价。主表仍有质量损失，state压缩比不是全训练HBM或加速。分解、正交近似、scales、格式和全部校准需保存并付费；谱结构、质量或恢复失配时，保留高精度momentum、较细分组或既有AdamW，不由方向相似批准普适无损训练。

拟本人注：`SF-2026-ARXIV-2605-11396` — Daily05-14补May13；作者exactv1§3–4/6/A1/A3/A6必要，2+1+2=5，polar前state分量编码gap深入；root实际§3/4/A3必要层有效，其他作者域分开。保elementwise仍旋向/归一改跨步权重/非独立各向同性、T2/T3质量损、state非总HBM与分解全费；未核实现/复现，owner/PRE/POST待。

### A39.2 AntiSD 11609：单侧ascent与teacher-entropy hysteresis

作者actual exactv1§3/4全部/A1–2与A3模板说明、E；root已actual§3/4.1/4.3/B/D1/E必要，未混作者全域。Student自有rollout，在同prefix特权参考+binaryassessment teacher给logratio u，加入−.5(softplus(u)−log2)优势和GRPO；deliberation侧正优势上界log2/2，shortcut侧负无界，非双侧bounded。batchteacherentropy median低于.93warm基线停anti项、回到warm才重启；5步warmup/固定阈值不是免校准。Sameparameters不保证teacher/noPI两forward来自同一joint/marginal，真实PMI需兼容假设；A1L3有限terminalpotential未统一常数，不采用其‘任意scalarreward最优policy不变’，正文E也限定local非全局。

5个Qwen/Olmo4–30B，DAPO17k200steps，32problems×8/32k训练，eval32k或thinking64k、T.7/topP.95，8H20/node与30B多node、precision未披露。T1 best-mean snapshot与first-reach2–10×steps不是净墙钟/最终稳定；MinervaOlmoThink45.8<GRPO46.4。NoGate Qwen早好后崩、Olmo存活甚至最高，阈值.90/.95反侧，不授everycomponentnecessity。NoTeacher亦改整个信号非独立因果，tokenword颜色不认证正确reasoning。额外teacherforward/entropy/rollout及verifiedreference全费，无trainingseedCI。保GRPO+可信SFT/普通distill共存。

actualCh29 688–707完整tokenallocation/teacherentropy FKL两段、signed routing完整两段及后diffusion两段。旧signed按studententropy/gap局部路由；本分支统一ascent形状+batchteacherentropy滞回停开是具体另一条件机制，不重复原forkrouting。拟唯一TRAIN-SFT，signed两段endmarker后→少步diffusion前单段。

拟逐字正文：

> 反向监督也可以不逐token选择fork，而在有可靠参考的同一student轨迹上，给teacher相对压低的token增加单侧有界优势，并用JSD导出的softplus形状惩罚相反一侧；负优势仍可无界，不能称双侧稳定保证。由于ascent不会在靠近teacher时自动终止，[AntiSD的有限实验](https://arxiv.org/html/2605.11609v1#S3.SS2)以batch teacher-entropy的warmup基线设置停开滞回：接近坍塌先关闭辅助项，恢复基线才重启，terminal verifier仍决定GRPO方向。两次forward的log-ratio不自动具有真实PMI或因果信用解释，低熵也非正确性。无门禁在部分模型早快后崩、另一些不需要门禁，较少steps与best快照非净训练降本；teacher、entropy、参考与全部rollout均付费。信号、阈值或独立质量回归失配时，关闭ascent，保留verifier-only、普通蒸馏或可信SFT，不把局部反蒸馏当通用规则。

拟本人注：`SF-2026-ARXIV-2605-11609` — Daily05-14补May13，作者exactv1§3/4/A1–2/A3模板/E必要；rootactual§3/4.1/4.3/B/D1/E必要域另列。2+1+2=5，JSDascent+teacherentropyhysteresis gap深入，保单侧bounded/PI兼容/terminalpotential不采、bestcheckpoint/step非全费、nogatemodelconditional与Minerva反侧；未核实现/复现，owner/PRE/POST待。

### A39.3 CREDIT 11613：input-generic teacher校正，不等因果信用

作者actual exactv1完整§3–4/A训练配置/C–F必要。额外sample同batch其他x′，保持原prefix/反馈z，用teacher logprob均值作输入通用分量并减λ；实际teacher-onlysurrogate，不是减fullratio，其序列和有额外anti-generic surprisal。E(logp)不同logE(p)，Jensen只给单侧上界不保所有shortcut被抑；samebatch不是独立全D保证。posteriorcompatibility是显式假设；E只100goldbalanced、强制answerletter4D投影，OLMo20%不兼容，不把teacherfidelity差解释成假设免检；不证全词表/中间prefix。F的causal条件及Z=O特殊例并非主实验（LCB测试IO/errors、ToolAlpaca期望call），不采用因果credit宣称。A3 EMAteacher与studentgap保持，非全消除bias。

Qwen8B/OLMo7B，8H20 verl/FSDP、precision未披露，LCB131题2025Feb–May、halfprivate作训练feedback/fullprivatevalidation（非独立heldouttest），ToolAlpaca4046/68；SCI应用不扩入项目，仅原作者横向评价。32×8rollout/18944token，LCB RKLteacherTop20、otherJSDTop100、EMA.01，λ.1/C1。每5step验证best，bootstrap只prompt variance非训练seed；LCB48.1→49.8、467→472s在该配置约1%，C16至765s/49.4，非通用negligible。λ>.1退化；think-only早57.1后26.7，solutiononly较稳；思维/通用token可视化不唯一因果。全部contrastiveforward/teacher/rollout/selection费用保留。

actualCh29 458–478完整privileged18734、OPRD全段、GUI与后targetwindow/critique；当前区分监督权限/entropy但没有**同prefix/z、置换input估genericteacher部分，以及teacher-only与fullratio差额**。拟唯一TRAIN-SFT，在18734完整段后→OPRD段前，不与11182远处冲突。

拟逐字正文：

> 同一反馈提高token概率，也可能只奖励跨题通用模板。可固定当前student prefix与反馈、将输入替换为同batch其他问题，估计teacher的input-generic log-prob，再从原局部优势减去其一部分。[CREDIT必要域](https://arxiv.org/html/2605.11613v1#S3.SS3)采用的是teacher-side surrogate，不是完整contrastive log-ratio；平均log与log平均不同，保留的额外surprisal也使它不等无偏互信息或因果信用。Bayesian解释要求两种forward兼容同一joint，answer-letter投影通过不证明任意中间prefix成立。较大校正强度会反退，额外contrastiveforward、teacher、rollout与选择均付费，一次小开销不授所有部署免费。负例、反馈或质量回归不可靠时，减弱/关闭校正、保留普通反馈蒸馏与可信target，不把input-specific proxy当正确性或因果根因。

拟本人注：`SF-2026-ARXIV-2605-11613` — Daily05-14补May13，作者exactv1§3–4/A配置/C–F必要，2+1+2=5，同prefix/z置换input的teacher-side校正gap深入；保posteriorcompatibility/投影非全局、teacher-only多surprisal/Jensen单侧、非causalcredit、LCB训练validation重叠/seed与全费。未核实现/复现，rootSource/owner/PRE/POST待。

## A40. 四项necessary Source / actual owner / 最小逐字PRE（均5分）

A39三项已按root批准唯一自然段/marker/本人注保存并顺读完整直接邻接、限定diff-check通过，非writerPOST待；11182actualPOST已通过释放。后续不重复其日期或原证。

### A40.1 MoE configurations 11689

作者actual exactv1§3全部/§5、A1–A2.2及C1必要，非全附录域。10–300Mactive/至6.6Btotal、约20token/activeparameter，batch512/context2048、Adam与数据mixture固定，A40/L40/L40S/H200混硬件，32000+9500GPUh（含初搜）。按activeFFN参数匹配是算术proxy，不包括router/dispatch/通信与相同wallclock；precision未披露。固定active预算下大inactive容量多有效、固定total时granularity有最佳区，纯dense拆细不复现；shared/generalist占用相同active预算后不必更好、两个heterogeneouspool只是有限插值未证明全部异质。10/20M加训练token才接近50M，非单独规模阈值。Dropless在高expert数不总优；lossfreebiasγ=.001在高n过粗，aux小但无bias最差而其他近似，非所有balance不重要。C1仅一个50M dense+一个MoE各5seed，不能给2000run统一低方差保证，且该MoE平均CE5.70>dense5.38，不隐去反例。Hellaswag/CE和generalcapability分开，不采通用推荐g=.25/n越大越好/真实加速。

actualCh21 255–291完整budget/heterowidth与428–449完整hyperparameteridentity/activationratio、130–182balance/capacity已读，Ch20/22交接1–25。已有预算坐标但缺**固定total与active的共享/拆细反例及bias步长随expertcount变化**这组有限证据。拟唯一MODEL-MOE，现total/active小节“小中规模搜索中拟合出的exponent…”完整段后→“同宽expert让GEMM…”前一段，非新标题。

拟逐字正文：

> 调整expert组织还要分开固定active与固定total两种比较。[一次有限配置扫描](https://arxiv.org/html/2605.11689v1#S3)中，增加inactive容量可以获益，但将原dense FFN拆细、在相同active预算中加入always-active generalist，或改成所测两种宽度池，并不自动改善质量；最佳granularity也随总预算与有效规模变化。Active FFN参数匹配不是完整FLOPs或墙钟匹配，较小模型的反侧还随训练token预算改变。高expertcount下固定bias增量可能过粗，dropless收益也可饱和，不能据此宣布balance无关或sharedexpert普遍有害。全部sweep、常驻权重、路由和通信仍付费；预算、数据或执行形状改变时，保留dense、同宽固定pool与邻近规模校准，不将局部最佳配置当跨规模配方。

拟本人注：`SF-2026-ARXIV-2605-11689` — Daily05-14补May13，exactv1§3/5/A1–A2.2/C1必要，2+1+2=5；actual预算/activationratio/balance局部有具体有限反证gap。保activeFFN非完整等费、shared/hetero/densegranularity反例、smalltokenbudget/highn bias与dropless边界、5seed仅两配置/CE反侧；未核实现/复现，rootSource/owner/PRE/POST待。

### A40.2 Router–expert coupling 12476

作者actual exactv1§2–6/8/A–B必要。固定当前topK/可微区域时router和expertinputmatrix梯度都具有scalar×x的形式，但scalar不同，有限batch/AdamW更新不保证同向/质心等价。AppA Eq19忽略softmax交叉项，补全它仍是某scalar×x但不是原给scalar；不能把该错误系数抄为完整recipe。aux未masksoftmax可向未选expert给梯度但βj并非任意输入永远非零，负/不同scalar不保证共享mean必然collapse。aux对照同时Switchloss+zloss vs bias，不能唯一因果归aux一项。gateactivationρ.43是所测correlation非语义/功能真值。

单1B/9层、64routedTop6+2shared、d1024/width512、OLMoEmix约50B/21kstep、2.36Mtoken/AdamW/peak.001、H100或MI325X node、precision未披露。Kmeans cosinecentroidEMA.99+selectionbiasγ.001不学习routerparams但仍保存全部centroid/bias和刷新，非无状态；T1末checkpoint C4PPL21.01>Lossfree20.40/aux20.54、Pile12.09>11.76/11.82，MaxVio.037<.084/.526是明确质量—均衡tradeoff，无速度/seedCI。§2fi按KB归一target1/N，§6fi/targetK/N写法需统一，空expertmean和normguard未全闭，不补成可运行算法；paper自称constructivetest非practicalrouter。方法局部与实证可有限采用，不授普适几何/消除collapse。

actualCh21 449–479完整modalitymask、TopKexposure两段、load/teacher及后historyrouter局部；已有globalbalance/explicitsequencehistory不拥有**无trainablerouter、按assigned当前hidden EMA更新centroid的constructive分支**。拟MODEL-MOE，在引入“改变容量组织后…”完整opening后→modalitybalance段前一段；保neartext质量损和gradientclaim限制，不造完整实施recipe。

拟逐字正文：

> Router与expert也不是两份独立学习的几何：在固定当前选择、未跨Top-k边界的反传中，两者的输入侧梯度都包含当前hidden方向，但系数不同，实际optimizer并不保证它们同向或语义一致。一条[受限constructive分支](https://arxiv.org/html/2605.12476v1#S6)不训练router权重，改为对已分配token的hidden均值维护centroid EMA，以cosine加负载bias选expert；去掉trainable参数没有去掉路由状态。它在单配置中降低MaxVio，却损失perplexity，辅助loss对照还同时改变z-loss，不能归为全部均衡梯度必然破坏specialization。Centroid、bias、归一/空集合保护、刷新和全部训练均需独立验收计费；输入几何、质量或负载失配时，保留原learnedrouter、已核balance与固定Top-k，不由较低负载proxy批准吞吐或专家语义。

拟本人注：`SF-2026-ARXIV-2605-12476` — Daily05-14补May13；exactv1§2–6/8/A–B必要，2+1+2=5，assignedhidden centroid分支gap深入。保cross-Jacobian原系数不采、AdamW非scalarx/β非永非零、aux+z混杂、T1质量损、fi单位/emptyguard未闭不照recipe；全state/全费近文，未核实现/复现，rootSource/owner/PRE/POST待。

### A40.3 Block-R1 11726

作者actual exactv1§2–6全部、C3–5/D4–5/D7/F必要。Trainingblock改变rollout law/groupadvantage，不仅inferencesize；offline teacherLLaDA2mini16B与studentLLaDA8B对6个block4–128各Q=1rollout，按rewardgap最大分配sample，过滤全easy/teacher全zero/teachermax不胜；maxgap是冻结teacher–student代理不是实际学习增量或oracle最优。固定θ且domainargmaxdisjoint的定理是定义下直观不等式，不证优化后所有θ/训练必冲突。BCS Wasserstein测gap选择分布，不是直接domainrewardmax，亦非独立因果。主表将过滤/数据/奖励与块一起变动，不见完全固定选中数据只换block的主ablation，不能独归block。C5两个RLalg支持特定fixedblock多域退步，保关联。

4MI300X192GB，BF16+4bit/LoRA128α64、32baselineblock、L256/T128、seed42/5000steps每100eval且每domain择best（不是单可部署最佳checkpoint），部分model支持10backbone非全同budget；Q1选择noise/teacher跨architecture与offline2NSQ全生成费；原表T2增量算术有误（GSM83.70−80.74=2.96非1.67，KK53.29−50.14=3.15），不采印刷Δ和Oracle部署收益。Inferenceb1是另一阶段，当前traininglabel不提供部署真label，无总wallclock/多seedCI。

actualCh24 764–780完整positiontemperature两段/固定ARpathRL完整段/后teacherlayout段；旧路径只固定训练顺序而没有**offline sampleblock标签改变RL轨迹分布**，与推理动态分块分责。拟MULTIMODAL-GENERATIVE-PARADIGMS，2601.15165完整段后→traininglayout段前单段；优化器公式仍交Ch33，不复制。

拟逐字正文：

> 训练时的block大小也不是纯推理吞吐旋钮：它改变同一prompt的rollout分布、reward和组内优势。一个[受限多域分支](https://arxiv.org/html/2605.11726v1#S4)离线在若干block下比较冻结teacher与student的rewardgap，为每个训练sample固定一个block标签；推理期动态分块仍是另一份选择。最大gap不等实际学习增量，单次rollout选择有噪声，固定参数下域偏好冲突也不证明重新优化后必然冲突。原比较共同改变过滤、数据与奖励，不能把全部收益唯一归给block；逐域best快照也不是同一个部署artifact。Teacher/student全候选生成、标签、训练和decode回归均付费；标签陈旧、质量或净预算不成立时，保留固定小块、原单域/多域配方与独立推理校准，不把offline oracle当线上可得。

拟本人注：`SF-2026-ARXIV-2605-11726` — Daily05-14补May13，exactv1§2–6/C3–5/D4–5/D7/F必要，2+1+2=5，sampleblock训练标签与rolloutlaw gap深入；保Q1gap非学习oracle、数据/过滤/奖励混杂、fixedθ非训练必冲突、domainbest非共同checkpoint、T2Δ误与完整offline费，未核实现/复现，rootSource/owner/PRE/POST待。

### A40.4 TABOM 11854

作者actual exactv1§2–4/A–C必要。生成trajectory上的local32newtokenwindow，除了重建其内容，以hinge要求早揭示token在自身原状态读出的entropy低于晚揭示者，非新独立planner/非压缩步数。§3理想Boltzmann只定建模prior而非从greedy过程推导；先后状态entropy会随context改变，不保证globalmonotone；只matchingordering不充分matchingnormalized概率，rank目标是surrogate，不能采Lemma1/‘exactKL/Boltzmannmatching’。NELBO并非必然不能表示条件结构，低selfCE不证manifold/barrier因果，TDS只entropyvariance非正确难度/知识边界。

Dream7B/LLaDA8B，SD trajectories约3.8kcode/5.1kmath与GT不同人口（codequery17kvs18k段也冲突不唯一recipe），LoRA16q/v、8GPU型号/precision未披露、batch4/device、5epochs/best、γ/λ任务grid，W32。BaselinesSD/dInfer/T3D同SD数据较可比，T5localranking相对maskonly部分收益，但globalrankingMBPP58.20<58.70/MATH40.2<41.2；localHuman58.54高于baseSD57.92，不能误记为反退。主Dreamcode IFEval55.45<NoSFT56.56，math56.19<56.56，不能说OODallretained。2tokenparallelMATH34.4<SDS34.8，Human45.73<SDS47.56，非全预算最好。Cbestwindow单独84.08/60.37与T3不同不合并。轨迹/多状态forward与entropy/ranking O(W²)、全部tuning费，无同质量净速/多seedCI。

actualCh24 724–742完整teacherorder+gold、T3D配对段、后PUMA两完整段。缺**用local SD揭示顺序约束模型自身entropy ranking而不学单独planner/少步映射**，拟唯一本章，T3D完整段后→PUMA段前单段，不重述T3D内容监督。

拟逐字正文：

> 已配对的self-distilled轨迹还可用于局部entropy排序，而不另训练位置planner或把多步压成一步。固定一个含若干新揭示token的窗口，在其原轨迹状态读取各位置的预测熵，以pairwise hinge偏好较早揭示者，同时保留窗口内容重建。[TABOM有限对照](https://arxiv.org/html/2605.11854v1#S3.SS2)支持这项局部正则；揭示先后不是跨状态全局难度真值，排序一致也不足以匹配Boltzmann概率或证明原KL最优。窗口过宽、部分任务和高并行切片仍退步，GT与self-generated不同人口也限制归因。轨迹采集、多状态forward、entropy、成对比较与调参均付费；顺序、内容或质量预算失配时，关闭ranking、保留普通重建/gold监督与完整保守decode，不由熵差认证正确提交或新知识。

拟本人注：`SF-2026-ARXIV-2605-11854` — Daily05-14补May13，exactv1§2–4/A–C必要，2+1+2=5，SDlocalentropy ranking gap深入；不采Boltzmann推导/ordering足够分布匹配/globalmonotone、TDS非truth，保GT/SD人口差、best/grid与IFEval/parallel反侧、全费，未核实现/复现，rootSource/owner/PRE/POST待。

## A41. 最后12项必要Source分层收敛（不扩发现，owner/PRE后接）

11726/11854按A40获授窄位真实保存、完整直接邻接及本人注self-read通过，actualPOST待。其余9项作者必要Source如下；12288/12483/11212由root实际先读必要域，避免第三重复，作者只在下述具名范围复用，不冒称本人读完。均保持2+1+2=5/May13既成日期，不因处置改分。

### A41.1 11374 frozen retrieval：具名重要修订收窄

作者actual v1§3–4/5.1–2/5.4–5/6/7/H；首批§3/4到5.2与6/H输出可读，5.1–2/5.4–5另完整补读，不以截断段标全读。仅针对已发现v5重要修订fresh取`2605.11374v5.html`并实际完整§3–4/结论/limitations（未全v2–4）。v1是259program/90round/17families、6universalcell gate+FiQA nongating、softcentroid参数搜索、80%/99%devtest局部收益；Nano50query/13tasks中j-v5nano均值−.30而文称两meanspositive，smallHotpot−3.24 p=.014，v1 T3/T4SC数也不统一，不照alltask/allfamily或‘每个substrate必归一algebra’。V1首轮检索topKweightedcentroid→queryinterpolate→再检索原理与classicalPRF近，搜索只有限生成不证明exhausted/globalceiling/随机ensemble必败；bootstrap不消已反复选择偏差，1×encoder非零第二ANN。L4CPU局部12.53→13.27ms仅对应单cell，不泛化。

v5已实质改144generation/144program/12Pareto、14discoverytasks(46–438docs)→19heldout×4encoder/988cells，MLXfp16 AppleSilicon，Opus4.6proposer；namedRocchio/MaxSim inspirations明确，不是自主无先验重发现；复杂program跨granularity/zscore/RRF/centroid，不再仅一algebra。固定LexHybridRRF54%win、并有多loss，oraclefrontier52/76不当部署selector；significantwins5–7 vs7losses也非普胜。Cost(c)把query+doc额外encode聚合，offlineindex可摊销不保证productionshortlist直接泛化、99kcorpus/多并发未一概验。Newheadbaseline只小容量/14task，不能宣布retraining轴都不transfer。仅采用frozenencoder可调局部表示/scoreprogram、搜索/部署与独立验证分账的窄结论，当前修订是必要反证不是新增May13事件；owner实际比较待，不先制造增段。

### A41.2 11416 LayerTracer

作者actual exactv1§3–5/Limitations/A1全部与C2。Tasktoken为模型自身finalargmax非gold，逐层共用LMhead的relativeprobchange与contexttoken残差置零引起的JSadjacentrelativechange是两种诊断；Ratio>0几乎所有非精确相等层，既不自动continuousinterval也非‘执行功能’证明。Contextzeroing敏感不推出parameterplasticity/deep稳定因果，relativeJS分母近零可放大。实际训练按固定half split，不是由诊断搜到最优边界；C2只alignment score非多边界真实CPT消融。主T1/T2fullbaseline四域恰同数值，隔离未经更正的跨bench合并，不推工业recipe。

Qwen710M CPT CCI262Btoken1epoch/4096/BF16/global64、8H200，tunedAdamW3e−5；CEval/CMMLU只有中文validation，generate16token正文deterministic与A4temperature.95口径保差异不补随机采样。五重复零std是重复同deterministiceval，不是5trainingseed。halfshallow训/深冻有限比分质量较好，但冻结深层仍反传到浅层不省全部backward；141hvs112/107h从optimizer至save排除load/init与诊断成本，无任意规模训练规律。保原fullFT、任务相关层分配与heldoutretention回退；actual owner待。

### A41.3 11739 EffOPD

作者actual exactv1§2–4/C/D2/F4必要（§3.3尾部单段截断，仅采用已明确公式/§4完整，不声称全理论F5）；RLandOPD比较训练rollout16/20k vsOPD1/16k、student1024不同，不是只loss变化或总compute相同。局部SVD/toprank与moduleupdate诊断支持特定参数几何，不授MLP唯一reasoningowner、tSNE因果或KL下降直接因果。终稿norm用于早checkpoint扩大是oracle诊断，不是部署可得未来范数。实际EffOPD在2^nsteps用相邻exponentialcheckpoint displacement试2k(k1..5)外推，50trainexamplesvalidation非真正heldout，逐个非降接纳/首失败停止；不是每步无条件加LR。大scale/F4β>1.2退步；方向更早接近终稿不保证沿线全局有效。

1.5/4/14/32B Qwen、Euruscode/DeepMath103k、8/32H20、OPDprecision正文D先RLFloat16但未单列OPDdtype（不混补）、1024×1/16k/vallength32samplingT1。报告3×是约10vs30–40steps；作者F7c墙钟曲线称同时间优势但未给完整run数字/teacher训练与全部搜索费，不能兑现通用加速。外推后的optimizerstate同步/旧检查点语义未全闭，不造可执行resume保证。保全部candidateeval/teacher/rollout/储存与回退vanillaOPD，未核代码/复现。

### A41.4 12058 HölderPO

作者actual exactv1§3–5、I1/I3/I4必要。将tokenratio聚为powermeanρp，∇ρ=ρΣsoftmax(p log r)∇logπ，p=0权重uniform/±p分别偏高/低ratio。是sequenceclipped surrogate而非trajectoryIS，p=1+sequenceclip不等完整tokenclipGRPO。Ratio高低仅policy相对old变化非正确性/可靠信心；固定r的weightentropy/mean单调可成立，不能移给训练中变化的r/θ。Variance上界是i.i.d trajectory/有界score条件的二阶矩上界，不等实际variance随p严格单调；同组GRPOadvantage相关时independence另验。I4从E crossdot=0不能任意把依赖轨迹的A/ρ/W提出期望，也不能把secondmoment称proportionalvariance；p→−∞ HHI有tie时1/m非必1，boundedHHI不叫无界指数增长，最低点可在−∞，不采finitep*保证。Thm3 pstat=plow时strictV(plow)<V(pstat)自相矛盾，且跨训练分布不能用fixedratio界证明global收敛/必优schedule。

4H100、Qwen2.5math1.5/7B/R1Distill7B及Qwen3，MATH8523/8rollouts cap3000、每轮1024traj/8minibatch128，greedy一次pass1；precision/总runwallclock未披露，无trainingseedCI。p2→−2math平均54.9，但MATH82.2<GRPO83.4、Oly45.3<PMPO46.7；ALFWorld1→−1优2→−2，范围需任务校准，不叫所有stage动态必最优。保外部baseline配置区别、全部rollout/调p/回归费。采用连续ratio-aggregation梯度分配这一独立可核mechanism，不采用错误variance theorem；owner待。

### A41.5 12258 Instruction Lens

作者actual exactv1§4–5、A3–6必要。采用窄问题是logitlens读哪类state：penultinstruction已消费image，比仅visionpatchstate在若干模型更可区分；Cafe=maxinstructionobjectprob去乘localvisualsimilarity，另选topminstruction均值与generatedobjectstate距配confidence，ω混合。不是图像objecttruth，alpha2不保证任意hidden距所得score正，softmax概率无校准保证；synonym/representationdrift与firstsubtoken会漏语义。A6 InstructBLIP visualreadoutAUROC80>instruction72是直接架构反侧，不能宣称instruction必过滤更好，Qformer融合位置改变可读信息。

5个7/8B MLLM，COCO/Objects365/CLEVR各5000image3samplingseeds、greedymax512/DRIVE-PG199RPOD32GB、precision未披露；CHAIR labelmatching/synonym非全部事实，POPE平均3sampling/二元问答非关系全覆盖；T3InstructBLIP有其他detectorAUROC更高。T4组合相对localproxy改善但部分组合反退，不据组合本身准入；longinstructionAUROC↑但LLaVAhallucinationrate25.51>22.34、AUPR↓95.46<96.38，检测不等减少生成幻觉。InsLen104.5/564.5ms高于GLSIM95.2/537.2且生成1870/19550特定人口，非free/实时SLO；投影/保存hidden与threshold500val全费，未核实现/复现。owner需比actualCh23已有读出，不先判新gap。

### A41.6 11853 GEAR

作者actual exactv1§4–5/A/B1/C2–5/D必要。实际sampled logstudent−logPIteacher可负，不是每token非负完整RKL；normalize[0,1]未给constanttrajectoryguard。高ratio触发span、entropy首次超过onset1.5结束，span沿用onset分数，余位置保自己的；无终止时endguard未闭不造完整算法。Sign-aware W=.9+.2w在[.9,1.1]（默认），只保advantage符号，不保其均值恰1、低variance或正确causalcredit；分歧/entropy不是错误责任。

Qwen3base4/8B，math5k/ToolRL4k，VeRL128batch×8/2epochs/H100，4B每epoch8H100约26h(math)/10h(tool)，precision/完整length未披露，evalmathT.6/topP.95Mean16，AST/milestone/endtoend分开。T2samevariant segment/trigger/entropytoolbounds支持局部差额；T1 8B MATH.740<ARPO.742/OPSD+RL.719等不能全泛化保证；无repeatCI、cost只是comparable非完整净价。PI需要可靠reference，proxy未来未证。全部teacherforward、entropy/span、rollout/tuning付费；未核代码/复现，owner待。

### A41.7 11946 Counterfactual Trace Auditing

作者actual exactv1§3–5/7–8。49skilltasks/同Sonnet4.5各with/without一次，matchedtask/model只descriptive contrast非因果estimand，sampling/platform未控。FSM五phase+emptyphase16tasks整体Implementation，DTW仅phase type/intentTFIDF≥.5，one-sidedrecover专记with-onlytargets防漏额外artifact；五SIP可多label，522是divergence-labelpair非独立轨迹/概率。手写threshold.5/约50pilot，无humanvalidatedgold，不能把SA/CB类别自动等同真实不安全。Case1唯一pass退.2但九divergence没有SIP触发，taxonomy不穷尽；surfacecopy有时真实helpful，case3并非一律destructive。

696divergences/49、37ceiling的80%SIP、平均pass+.34pp与1.91×token是跨task描述；median1.09×，单gitlab22.24×主导middlemean，ratio均值非总tokens配对比。r1不估within-taskvariance，midn10/floorn2无普适skill效果；tokenusage不等wallclock/费用/正确性，extraartifact也不自动越权。实际phasefallback排除后upfront79%而非84%全population，不能合并。采用评价接口而非新taxonomy/Agent行为推荐；owneractual待。

### A41.8 12233 Task Alignment Benchmark（安全设计反证深入）

作者actual exactv1§2–5/A/F/G1/H全部必要。任务移除必要细节再在同surface恢复cue+无关directive，保原verifier；cueutil只在baseline可解且实际观测cue人口，resistance另条件于distractorseen，U×R只是组合score非同trialjointpassrate，不跨不同人口直接乘成安全率。Surfaceappearance marker只证明进context，不能保证阅读/使用；abstraction最强model失败不推所有弱model不可能。89原任务剔6仍solvable→83，早repro部分仍89、judge814trials与83×10=830不同，按实际各分母不补造统一全成功coverage。A1cue/distractor共同cell未要求oraclesolve，人工四author60/89需修，有限construction非天然正确。

Terminus2/tmux/Harbor.1.45、6–200min、3runs，CPUhost2EPYC/756GB，hostedAPI与internalH100/vLLMprecisionND，exactmodelaliases仅作者报告，不推平台当前实际。D distractor+cue比alone可更容易被遵循；SICsanitizer在GPTmini执行.65→.03但task.36→.01，TaskShield一model例外.33/.36不transfer。六adapter非各原全系统：PromptArmor复用SICprompt、Spotlight只delimit、Firewall默认无minimizer、TaskShield只tooloutput/reconstructedprompt；不宣称六产品普遍无效。Defense额外judge/rewrite/latency费用不得省，binary/media低执行可因读不出，不认证更安全。G1judge95.3%只validateddistractorartifact，cueuse未groundtruth验证，LLMjudge非权限oracle。采用必要cue/无关指令双测与防御抑制utility反证，不采U×R安全保证；未核代码/复现，owner待。

### A41.9 RAW-Dream 12334

作者actual exactv1§3–4/A1全部/B/C3必要。Taskagnostic WM/reward不等policy无taskdata：LIBERO90SFT+noiseplay，目标suite仍1demo/taskSFT，real3demo/task；WM/co-train/IDFT区分，不把co-train叫零targetdata。Wan1.3B actionAdaLN/causaltemporal、context6+anchor、progressiveanchornoise只inference控制ghosting不是physicalcertificate。DNV仅原判成功的actionsequence用独立diffusionnoise再生成+同VLM复判，reject disagreement不是验证真实物理，两次同错可过/真实随机成功可被拒；A2以可信mean替reward使flaggedadv0、>2flaggeddropgroup/allconstantdrop，scale改变不自动不影响optimization，组筛选也改变训练人口。

OpenVLA-OFT categorical而非原L1head、8actionchunk，WM256²/2latentstates×5UniPCeval、contextnoise/100ksteps训练；8H200/RL约2days、precisionND，Qwen3VL8B或32B按suite不同、4FPS/5votes≥4/T.7。Co-trainGoal58.4<zero60.2、Objectzero47.2仅+0.8；OnlineRL1/10steps vsWM20/50并非同训练compute。T3DNV局部支持、C3早步并非全好(ZeroObject@10 49<53.2/ZeroLong21<21.2、coSpatial@20 66.6<67.2)，1.3×仅WMstage非总训练。Breal10k/suitevalidator与训练分开但rewardGoalF135/Longprecision62限制；Robometer是in-domain参考非真实oracle。实机4task×30trials单policy训练无CI，50→71.7不是安全/泛task保证。WM/VLM同bias、全部replay/投票/teacher与训练费保留；未核视频/实现/复现，owner待。

### A41.10 TBPO 12288中心争议；root独核域复用

作者先实际§3–4，root实际补§3.1/4/5.1/5.3/A3证明/B1/C3。Eq11把两个token各.5的偏好连乘为prefix偏好，则方向各.25、和.5，不满足binarycomparison归一；Theorem4.4用实际sequence样本转prefix权重依赖该失效measure。Theorem4.3另需fullsupport/真实w/identifiability，sufficientcapacity不补缺数据与真baseline。没有发现独立于该失效measure、且超出现有cross-prefix baseline的可采新机制；不能只摘‘不同prefix要校正’绕过中心。保5分/受影响域深入/争议暂缓，不写Books；实测评价为作者surrogate结果，不采其tokenoptimality或等价可训练目标保证。重开需更正一致的prefix比较概率/measure与可核训练objective、fullsupport/weight识别条件或独立不依赖错误measure的新证据；不否定所有token级偏好方法。

## A42. 最后11项 actual owner 与逐字PRE / 具体NC（Source按A41及root具名域）

root实际POST已通过11689/12476/11726/11854，全部窄位释放，现30I/2NC/3中心争议（12288终态已接纳）。以下仅请求窄位，不提前写入。相关交接：Ch23/25和Ch28/29/32已本日实际读，Ch33邻Ch32/34、Ch66邻实际Ch65KAI/67、Ch72邻实际Ch71/73、Ch76邻Ch75/77开头在本批补读；误猜旧65/71文件名未读成功后已用rg解析真实路径再读，不作为新路由或修改ROADMAP。

### A42.1 11374 / AGENT-RAG

actualCh76检索表示347–359完整single/multivector两段及producer共享段、613–639完整reranking/共享参照和多种表示候选，旧文讨论重训encoder/adapter与换reranker，没有**保持encoder不变、由初检近邻重构query再检索并分离搜索选择与部署**。拟intro末`multivector-retrieval-expressivity-cost` marker后→“检索表示的producer…”前单段。V5修订只收窄v1，不把后稿新结果倒填May13原事件。

拟逐字正文：

> 固定encoder也不等只能执行一次cosine：先取原query的近邻，将其预计算向量按相似度加权成centroid，再与query插值、归一并重新检索，是一条不更新权重的PRF分支；坏近邻也会把query带偏。程序搜索还可组合粒度与score操作，但搜索所用labels、frontier选择与部署时固定程序必须分账。[原有限机制](https://arxiv.org/html/2605.11374v1#S4.SS1)不能继承为所有任务或family普胜，[具名重要修订](https://arxiv.org/html/2605.11374v5#S4)已改用多程序及独立transfer，仍有大量退步，事后oracle不等可用selector。额外ANN、centroid、可能的重编码、搜索与索引更新均付费，encoder-call比也非总延迟；候选污染、迁移或净质量不合适时，保留原cosine/lexical-hybrid、较小反馈强度与独立相关性验证，不由几何自洽认证答案支持。

拟本人注：`SF-2026-ARXIV-2605-11374` — Daily05-14补May13，2+1+2=5，作者v1§3–4/5.1–2/5.4–5/6/7/H及具名v5§3–4/结论/limits必要差额；不全版本重审。只采fixedencoder反馈query/搜索部署分责，保v1数字/means矛盾与v5多frontier/heldoutlosses、oracle/label/总费；未核实现/复现，rootSource/owner/PRE/POST待。

### A42.2 11416 / TRAIN-PRETRAINING

actualCh28 348–367完整residualschedule、922–960完整四策略以及1011–1031完整moduleSNR两段/后clipping交接。旧文指出无普适深度LR并解释actuator，却未承载**CPT可反向冻结深层的有限反例与hidden诊断不能授trainability**。拟四种策略后“另外第17章…”完整段后→“哪些情况下值得引入m_l”标题前单段，明确freeze非LR，不重排。

拟逐字正文：

> 层级适配还可以改变哪些参数参与更新，而不只乘learning rate。一次[有限continued-pretraining对照](https://arxiv.org/html/2605.11416v1#S5)在特定中文语料与小模型上发现，训练浅半、冻结深半可优于反向分配或全参；它是固定分割的经验反例，不是“深层普遍稳定”的规律。逐层LM-head读出与把context hidden置零后的相对JS变化，只测该读取和扰动，不能直接认证参数塑性、执行功能或最优split；重复确定性评价的零方差也非训练稳健性。冻结深层仍需把梯度传回浅层，完整forward、诊断、优化和保留能力回归都付费。数据、架构或独立质量失配时，保留full训练、原分组适配与任务相关校准，不由一张层热图批准通用冻结方案。

拟本人注：`SF-2026-ARXIV-2605-11416` — Daily05-14补May13，作者exactv1§3–5/Limit/A1/C2必要，2+1+2=5，固定shallowtrain/deepfreeze有限反例gap深入；保TP/LS非参数塑性、split非最优、T1/T2及generation口径、重复eval非trainingCI、forward/backward与全费；不授通用层功能，未核实现/复现，rootSource/owner/PRE/POST待。

### A42.3 11739 / TRAIN-SFT

actualCh29 539–574完整offlinecorrection、mixtureoccupancy两段、StableOPD两段和后tokenpositionselection两段，未找到外推/AlphaOPD/ExOPD正文。缺**参数位移方向与幅度分离并用实际验证门接纳外推**，非迁移teacher内容。拟StableOPD两段后→“同一studentrollout上，覆盖哪些prefix…”前单段；不把finalnorm oracle写入实际算法。

拟逐字正文：

> On-policy监督的总费用还可从更新轨迹减少，而不只删监督token：若相邻checkpoint的参数位移在早期已较稳定，可在指数间隔提出沿该位移的几个更大候选，逐个以小验证集接纳非降者、遇到首次退步就停止。[EffOPD的有限方法](https://arxiv.org/html/2605.11739v1#S4)使用训练样本作这道轻量门，不保证独立泛化；事后把早期更新放大到终稿范数只是oracle诊断，不能当线上已知尺度。过度外推仍退步，方向相似、较低KL与小集不降均非正确性或全局稳定。候选求值、teacher/rollout、checkpoint及optimizer-state衔接都需验收计费，较少steps不自动兑现全费节省；方向漂移、验证不足或恢复语义不明时，放弃外推并保留原OPD/最近有效checkpoint，不由局部几何替独立任务回归。

拟本人注：`SF-2026-ARXIV-2605-11739` — Daily05-14补May13，作者exactv1§2–4/C/D2/F4必要，2+1+2=5，extrapolation验证门gap深入；保futurefinalnorm仅oracle/50train非heldout、过量scale退步、RL/OPD预算不同、state桥与全费，不授全局稳定或固定净速；未核F5全部/实现/复现，rootSource/owner/PRE/POST待。

### A42.4 12058 / TRAIN-GRPO

actualCh33 785–819完整GSPO/stepbalanced、长度外乘、双clippedsurrogate及两级ratio段，已区分聚合与clipping但没有**连续powermean改变内部token梯度分配**。拟GSPO首完整段后→“混合GUI与code行动…”前一段。主采用独立梯度恒等式，A41不成立的variance/global保证不入书。

拟逐字正文：

> 聚合ratio本身也可连续变化：以power mean将一条回答的正token-ratios压成ρₚ，其未裁剪梯度为ρₚ乘各token score-gradient的加权和，权重正比rₜᵖ；p=0均匀、正p偏高ratio、负p偏低ratio。这是[HölderPO的局部接口](https://arxiv.org/html/2605.12058v1#S3.SS1)，不是trajectory joint IS，sequence clipping下p=1也不等原token-clipped GRPO。Ratio变化不认证正确或关键token，固定ratios下较小二阶矩上界也不证明训练中实际variance/收敛单调；理想正交假设不能略去相关权重。衰减p是需校准的经验分支，部分任务/端点仍退步，全部rollout、schedule搜索和质量回归付费。支持、数值或净质量失配时，保留原GRPO/GSPO与固定聚合，不把动态schedule签成普遍稳定保证。

拟本人注：`SF-2026-ARXIV-2605-12058` — Daily05-14补May13，作者exactv1§3–5/I1/I3/I4必要，2+1+2=5；只采powermean局部梯度分配gap，保sequenceclip不同/非jointIS、同组依赖、weightedorthogonality/secondmoment非variance与strictendpoint缺口、任务/端点反侧/全费，未核全部proof/实现/复现，rootSource/owner/PRE/POST待。

### A42.5 12258 / MULTIMODAL-REPRESENTATION

actualCh23 1838–1865完整SCOLAR→write/readcircuit两段→relationtoken与fullsequencepatch两段；旧文不把可读信号当truth，仍缺**image-conditioned instruction位置可作对象detector读出及Qformer反例**。拟circuit两完整段后→“表示经过contextualencoder后…”前单段，不与RVE干预/层热图混。

拟逐字正文：

> 幻觉sensor还要比较从哪类token读信息：已消费图像的instruction hidden states可能比原image-patch states更便于读出对象，但不表示语言位置拥有新的观察。一个[受限detector分支](https://arxiv.org/html/2605.12258v1#S4)以instruction的object-token读出调节局部视觉分数，再比较选中instruction states与生成对象state的一致性；logit lens、同义词与first-subtoken规则都影响结果，概率与表示接近不是事实校准。Q-Former架构存在image读出更好的反侧，较长指令检测更好也可同时生成更多幻觉，检测与修复不能合并。Hidden保存、词表投影、阈值和完整生成均付费；架构、读出或旁侧质量失配时，保留image/外部grounding、原输出与独立对象标签评价，不由某位置AUROC批准无幻觉或实时SLO。

拟本人注：`SF-2026-ARXIV-2605-12258` — Daily05-14补May13，作者exactv1§4–5/A3–6必要，2+1+2=5，instruction-vs-image读出窄gap深入；保Qformer反侧、proxy/synonym/firsttoken与alpha非正保证、长指令HR↑/非修复、全费/latency非SLO；未核图像/实现/复现，rootSource/owner/PRE/POST待。

### A42.6 11853 / TRAIN-GRPO

actualCh33 414–435完整集合内credit/OSPO完整段、Cliff两段及后diffusion内部credit；不同于subsetoracle/单首错teacher，本项缺**logratio触发、entropy终止span并按优势符号调制**。拟OSPO完整段后→“一个较粗的process分支…”前单段，不改原Cliff机制。

拟逐字正文：

> 不查询全部子集时，还可由特权teacher差异提出span边界：sampled token的student–teacher log-ratio触发片段，以相对onset的entropy变化结束，再把onset分数传播给片段，其余位置保原分数；按trajectory advantage符号作小幅正权调制。[GEAR有限消融](https://arxiv.org/html/2605.11853v1#S4)支持这种分段与逐点加权的差别，但sampled log-ratio不是逐token非负KL，分歧/熵也不识别真实错误责任。正权只保优势符号，不保均值恰一、无偏梯度或低方差；常量归一及找不到终点的guard还需实现明确。Teacher、entropy、span、全部rollout和校准均付费，稀疏标注少不等总训练免费。参考不可靠、片段失配或质量回归时，关闭调制，保留outcome-only、可信过程监督与原完整回答优势，不由更细credit自证正确。

拟本人注：`SF-2026-ARXIV-2605-11853` — Daily05-14补May13，作者exactv1§4–5/A/B1/C2–5/D必要，2+1+2=5，divergencetrigger/entropyend span gap深入；保logratio非KL/非causal、正权非均值或variance保证、empty/constantguard与全费、局部反侧，无实现/复现，rootSource/owner/PRE/POST待。

### A42.7 11946 / PLATFORM-EVALUATION-SYSTEM

actualCh66 1388–1449完整proactivity/clarification、tool信息利用及trajectory六检查项/后KnowledgeSurface两段；已有成功/副作用分层，缺**with/without skill按phase/intent对齐并追回仅一侧artifacts，用饱和人口显示行为差额**。拟trajectory六检查项后→KnowledgeSurface标题前一段，标签只诊断不做新本体。

拟逐字正文：

> 功能pass-rate已接近上限时，附加skill仍可能改变读写路径与费用。可在同task/model的with/without条件下对齐phase与intent，再比较targets、内容和执行结果；还须单独追回只在一侧创建的artifacts，避免对称对齐把额外动作漏掉。[CTA的有限配对](https://arxiv.org/html/2605.11946v1#S3)说明这种测量差额，不把一次匹配run当因果估计：规则phase、模板复制与SIP标签均未独立校准，标签数也非独立失败次数。原唯一退分例甚至未被五类规则命中，不能由零告警认证无影响。成对执行、trace保存、对齐与人工校准都付费，token比例不等总时延；随机性、harness或标签不可靠时，保留重复独立运行、原pass/side-effect检查与人工审计，不因通过率不变判skill无成本或无风险。

拟本人注：`SF-2026-ARXIV-2605-11946` — Daily05-14补May13，作者exactv1§3–5/7–8必要，2+1+2=5，matchedphase/intent+unilateralartifact gap深入；保r1描述非因果/未校准FSM-SIP、ceiling/mid分母/oneunlabelledfail、tokenratio非总费，无artifact/复现，rootSource/owner/PRE/POST待。

### A42.8 12233 / PLATFORM-SECURITY：具体已有覆盖提请

actualCh72 866–900完整framing两段、GoalAlignment的ReasAlign两完整段、后跨步组合授权两完整段及Deny前交接。现**“保持用户意图…区分外部文本中的有用信息与企图重定向任务的指令，而不是将所有外部instruction一概删除”**明确承担cue/irrelevant分责；下一完整段把较低ASR与良性SEP98.9→98.0反退、teacher/judge成本和独立effectgate同时保留。TAB双条件utility损失是该既有合同的新有限验证，U/R不同机会集及乘积非joint在A41必要报告，不新增权限或过滤机制。拟5分/安全设计反证深入完成/具体NC，不加段/注；不因同主题判NC，而是实际两原段已同时承载有用信息、越权、误删utility与授权分责。Defenseadapter不是原全产品已在报告注明，无需复制六防御详情到Books。root必要Source/NC实际核待。

### A42.9 12334 / MULTIMODAL-WORLD-MODELS

actualCh25 985–1003完整horizon/结构certificate两段、WoVR完整段和后predictionerror标题；已有真实轨迹起点/模型刷新不拥有**只对imaginedpositive独立noise重放并以同VLM拒分歧的局部门**。拟WoVR完整段及其独立marker后→PredictionError标题前一段，普通GRPO数学仍归Ch33，不复制到VLAcontroller。

拟逐字正文：

> 不为每个目标重训WM/reward时，可先从同embodiment的广泛行为学习action-conditioned模型，再由现成VLM评价想象轨迹；目标policy仍可能需要few-shot示教，不能把WM的zero-shot叫整条系统零目标数据。[RAW-Dream受限分支](https://arxiv.org/html/2605.12334v1#S3.SS2)只对初判成功的action序列换独立diffusion noise重放，若同VLM两次判定不同，就不给该轨迹优势；这筛的是模型—judge一致性，不是真实物理可靠性，两次同错仍可通过。筛组与方差归一改变训练人口，部分早期切片和新对象仍失效。重放、VLM投票、anchornoise、训练与真实回归全计费，WMstage约1.3倍不等总费用；支持或奖励失配时，减少想象、补真实数据/验证并保留原SFT与短horizon，不由逼真或复判一致批准动作安全。

拟本人注：`SF-2026-ARXIV-2605-12334` — Daily05-14补May13，作者exactv1§3–4/A1/B/C3必要，2+1+2=5，positiveactiondualnoise/同VLM筛组gap深入；保WMzero非policyzero/共错非physical、constant/flaggroup人口、早步/Goal/Object反侧、onlinecompute未配平与全费，无视频/实现/复现，rootSource/owner/PRE/POST待。

### A42.10 12483 / TRAIN-SFT（root必要Source复用）

rootactual exactv1§3/4/5/6/E必要一次有效，作者未重复；保固定student/labels非总compute、teacherRL/FKL/OPD全费、14BAIME25 OPDonly19.5>bridge19.2、SE只题目、79.3vs78.5局部非普适、只mathsamevocab。actualCh29 388–398完整historicalteacher覆盖、budgetmode两段、teacher可教性校准两段、后跨模态分布段；现有校准改变teacher可复制性，但未承载**稀疏标签给teacher还是student的条件分配+FKL→OPD桥**。拟teacher可教性两完整段后→跨模态分支前单段，非新RL体系。

拟逐字正文：

> 同一student的稀疏标签预算还可先用于训练较强teacher，再以forward-KL warmup把student接到可学习区域，随后在student自有prefix做OPD，最后另验是否还需要student RL。[有限数学对照](https://arxiv.org/html/2605.12483v1#S5)支持这条上游reward与下游dense监督的条件分工，却不证明标签永远应全部上移：部分切片OPD-only更好，student继续RL仍可能补teacher偏差。固定student与标签数不是匹配teacher训练/所有rollout的总compute，SE也不是训练种子不确定性。Teacher RL、两阶段桥、词表概率与后续RL均付费，KL小不等原能力无损；teacher转移不良、warmup/预算或独立质量失配时，保留直接student RL、普通SFT/OPD及原checkpoint，不从局部数据分配排序推出普适upstream原则。

拟本人注：`SF-2026-ARXIV-2605-12483` — Daily05-14补May13，rootactual exactv1§3/4/5/6/E必要Source复用，作者仅actualowner/最小PRE。2+1+2=5，reward投向/两阶段bridge gap深入，保samevocab/math-only、局部OPDonly反侧/题目SE/非同总compute与teacher全费，未核实现/复现，rootowner/PRE/POST待。

### A42.11 11212 / MULTIMODAL-REPRESENTATION（root必要Source复用）

rootactual exactv1§4/5/6/C/D/G必要Source有效，作者未重复。RTS三层MLP比较相邻原图同位置feature、OmniParser regionIoU训练label；window首图全保，后图保原position；所有图完整encoder，文本history全累积，每k独立训。NoDrop同filtered训练推理关闭不是untouchedbaseline；onlineOmniParser更好但558–572ms vsRTS22–23只filter非全推理，singleimage切片反退、9image步数长、3evalrun非3trainingseed/precision和完整inferHWND保留。actualCh23 964–994完整不规则相邻feature删选两段、GUIPruner完整段、后DyGeo两段；缺**screen邻帧同位置特征可学冗余+窗口首锚的训练/推理分责**，不是encoder内剪枝/几何voxel/简单resize。拟GUIPruner完整段后→DyGeo开始前一段，保先denseencode与总history非constant。

拟逐字正文：

> 连续截图还可先比较相邻原图的同位置features，由受监督的小selector判断哪些区域值得重复送给语言consumer；每个window首图完整保留，后图删选仍使用原空间position。这条[RTS有限分支](https://arxiv.org/html/2605.11212v1#S4)先完整编码所有图，并针对稀疏history适配模型，不是复用旧KV或让总context常量化，文本行动与推理history仍增长。OmniParser的跨帧region对应只是训练label代理，界面移动、小控件和短history仍有反退；同filtered训练后关闭drop也不是未经改动的基线。全部视觉encode、selector、window重锚、适配和完整生成均付费，filter局部毫秒不签全链SLO；对应或任务质量不可靠时，增大保留、回到完整截图/均匀预算与已核history，不由重复外观认证证据冗余。

拟本人注：`SF-2026-ARXIV-2605-11212` — Daily05-14补May13，rootactual exactv1§4/5/6/C/D/G必要Source复用，作者actualCh23邻接/最小PRE；2+1+2=5，adjacentpositionfeature/windowanchor gap深入，保denseencode/全文本增长、NoDrop训练身份、sameproxy非truth、singleimage反侧和filter非全费，未核实现/复现，rootowner/PRE/POST待。

## A43. 全部46项研究/Books安全终态（六节归并进行中）

root已实际完成R17–20并通知：12288保5分/中心争议终态；12233必要Source和Ch72完整GoalAlignment→组合授权实际对读，具体NC通过；A42十项各唯一新增正文、完整直接两侧和本人注实际POST通过，10窄位全释放。先前30整合的有效POST不重跑，作者只同步本人纯注既成状态，不冒称读过root全部原域；12483/11212必要Source是root独立实际读、作者复用并做owner/PRE。A41/A42中的待核/待写句均为历史停点，不是当前可执行尾。

本次确定新增**46家族＝40真实整合/局部纠正＋3具体已有覆盖（TanStack/3D-Belief/TAB）＋3中心争议（11134/11871/12288）**。40项都保必要反侧/全费用与共存回退，不授论文全部理论、任意模型安全/加速或生产能力；3争议保原5/6评分、不因中心失效删候选，不绕争议摘通用原则造Books段。14唯一Books owner实际写入，全部本日窄位释放；NC不新增段/注。尚未做本次日级DAY/保存完成态FINAL，不声称日报完成。

发现/日期已封口且独核有效，**不再GET日期或展开其他宽命中**。A36为本次来源有限范围；其中“后20待准入/当前26”等进度由A37–43实际结果取代。机构历史段、11887早稿资格、12586/87跨日和三中心争议继续隔离，不支撑正面Coverage/Evidence/Books或无遗漏。当前可执行尾仅原六部分合并、冻结/链接/格式验证、root整日DAY、通过后保存完成态与actualFINAL。原130整行/日期评分、小时窗与连续原§4保留，不扩Weekly/Live/2025，不改LS/索引或其他日；不stage/commit/push。

## A44. 六部分归并及实际机器检查，待root DAY

当前README已将A36有限来源范围、46逐项日期/评分/有限采用与具体owner处置融入原六部分；原Round6结论明确仅历史修复范围，旧130整行保留，连续原§4后新增46证据而非替换有效旧块。新增46=40I/3具体NC/3中心争议；首公开资格11887和12586/87不混入确定候选，外部slice与中心反例精确终态隔离。root R1–20是实际非作者依据，尚未冒称本次DAY通过。

原基线仅用apply_patch Move规范重命名为`baseline-before-supplement-20261019.md`，内容不变、无overwrite；README/SUP旧引用已同步，reader无旧链接依赖。顶端显式冻结候选日期引用该原件，不动任何旧日期/评分。V3初检发现旧日期未获freeze引用及补检单元格并列链接的纯格式问题后已修，未改合同/脚本。实际重跑V3通过；freeze验证原130整行各一次、合176，原小时窗与含标题606256 Unicode code points（正文606239）/606478 UTF-16 units连续旧§4保持；265本地引用0missing、固定六H2；40整合binding各一次/本人注POST通过，14唯一写入owner。README/SUP/基线限定cached及unstaged两层diffcheck通过；rootR20已查七尾Books两层diff，本方未stage/commit/push。工具不证明语义或全网覆盖。

当前只待root完整六部分DAY，通过后保存完成态，再做actualFINAL；没有普通Source/owner/写后尾，不重做有效层或扩研究。

## A45. root R21实际DAY通过，完成态保存待actualFINAL

root已完整实际读本次六部分、46新增表行与46证据处置，265引用/41路径0missing；原130整行、原小时窗及606239正文字符连续旧§4、V3和两层限定diffcheck实际通过。全部普通研究/Books差额0，40I/3具体NC/3中心争议终态不变，全部本日Books锁已释放，未重做有效层。

作者仅行政同步README头部完成态、§1/§5/§6及时间`2026-10-19T09:21:44+08:00`，有效研究正文和旧130/原§4未改。当前完成态已保存，等待root真实读回actualFINAL，未冒称该步骤已发生。无stage/commit/push，不改LS/索引/其他日，不自行接下一日。
