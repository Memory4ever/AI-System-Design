# 12/09 首批准入非作者校准

复核者：主线程（非作者）；2026-10-02。实际读取作者 `ADMISSION_CALIBRATION.md`，并独立打开 [ILVR 精确 v1](https://arxiv.org/abs/2512.05665v1) 与 [Greek Government Decisions 精确 v1](https://arxiv.org/abs/2512.05647v1) 的完整题摘和版本历史；临床应用 `2512.05537v1` 定点访问同样 Cache miss。

- ILVR 潜在准入理由通过：反复像素编码与静态压缩状态的代价不同，交错生成动态 latent cue、teacher 选择监督有具体机制变化，不能当成换名字的 CoT 排除。此为初筛校准，不证明性能收益；精确 v1 方法应确认推理时是否还需 helper images，以及选择机制、压缩量和预算的消融。原文 v1 只给 `2025-12-05T12:09:39Z` 提交，不授 12/09 落窗。
- Greek 语料普通负侧通过：原题摘呈现领域语料、抽取与基线 RAG，未形成能改动通用模型/系统判断的独立机制或反证。不是因为领域数据或小实验天然没有贡献。日期不影响此关闭。
- 临床应用只按标题暂作范围判断，未核完整题摘；不把访问失败变成内容排除证明。没有明显相关反证/安全信号时无需为这条标题线索展开全文。
- SignRoundV2 和 EtCon 的潜在贡献尚未由本复核打开原文；不得把本批通过扩为它们的证据审阅、真实归属或已有覆盖验收。

实际复核为一项潜在准入和一项普通负侧；其余未检查范围如上。全日十四源、历史公开证据、其他潜在材料和 Books 仍在执行，不授日级完成。

## 触发日期定点核验与初稿检查

实际打开 [SGLang issue 14691](https://github.com/sgl-project/sglang/issues/14691)，读取原始问题与配置，并通过官方 GitHub API `https://api.github.com/repos/sgl-project/sglang/issues/14691` 成功返回 HTTP200：`created_at=2025-12-09T03:22:07Z`，北京时间 **12/09 11:22:07**，在本日09:00右端之后，应路由 **12/10**。问题中 12/08 的运行日志不是公开时间；未把报告者的断言失败当官方已确认缺陷，也未读取后续评论替代原始事件。

已经发生的触发要留此精确关闭/路由依据，不必在 12/09 深入机制审阅；它不阻塞本日。12/10 需按该日合同独立判断其是否改变版本正确性边界，不能预先声称前日报已有有效审阅。

实际顺读 `09/README.md` 全部六部分和14来源表，V3校验通过（结构，不是语义）。当前正确保持进行中；其他来源/题摘及必要日期普通待办仍存在，没有日级完成。

## 第二批题摘校准

主线程独立打开下列精确 v1 的完整题摘与版本历史。四项的 Submitted 都不是首次公开，不授本日归属。

- [Expert Personas](https://arxiv.org/abs/2512.05858v1)：潜在贡献通过。六模型、两客观题基准与无 persona 对照能反证“加入专家身份就普遍提高事实准确率”的设计捷径；需保留 Gemini 2.0 Flash 例外及语气功能不在测量目标，不能把标题外推为 persona 一概无用。owner `AGENT-PROMPT`。
- [SEA-SafeguardBench](https://arxiv.org/abs/2512.05501v1)：潜在贡献通过。native-authored/human-verified 与翻译式安全数据覆盖的区别可改变多语言 guardrail 验收边界；不只因为新 benchmark 名称准入。必要安全源审应核场景构造、标注、切片及英语对照，不能由排名推出所有 SEA 部署不安全。owner `PLATFORM-EVALUATION-SYSTEM`，安全执行交 Ch72。
- [M4-RAG](https://arxiv.org/abs/2512.05959v1)：潜在贡献通过。固定可复验检索环境中较大 VLM 可能因 RAG 退化，是对“模型更强且检索更多必然更好”的局部反证；需核模型大小与检索器、提示、语言、图像条件是否可比，不外推为大模型不需要 RAG。v2 已到 2026，不混用。owner `AGENT-RAG`。
- [Dynamic Alignment](https://arxiv.org/abs/2512.05464v1)：已进一步独立读精确 HTML §2/§3/§5。当前是 gpt-oss-20b、固定合成集、CA 自奖励与 GRPO 的原型；CA win-rate 排除了交换位置后不一致的 judge 结果，不能当全部题的无条件成功率。与替代自改进方法的比较、component ablation、human/multi-judge 与 reward drift 仍列未来工作，不能当已证实的新安全保证。若拟准入只是换价值名称加现有 self-rewarding/GRPO，应贡献前关闭；如另有具体改变设计判断的机制或受控反证，先明确该独立命题，不以安全相关标题自动增池。本次不授整项 Evidence/Books。

这些是潜在贡献与排除边界校准；本日其他普通工作及必要日期尚未关闭。

## 本次独立非作者终审：未通过

复核者：Codex 独立非作者验收者，本次用户指定的 12/09 审阅会话；不是作者 Plato，不冒称前两批的主线程身份。检查时间：2026-10-02T18:23:31+08:00。只审窗口 [2025-12-08T09:00:00+08:00, 2025-12-09T09:00:00+08:00)，不提前审 12/10–12/16。本节追加，保留上述实际校准与历史停点。

### 来源与安全终态

已读 AGENTS、RESEARCH_CONTRACT、REPORT_CONTRACTS、RESEARCH_SOURCES 使用说明/每日要求、CODEX_RESEARCH_PROMPT、ROADMAP、LEARNING_STATE 相关检索与最新边界，以及本日 README、SOURCE_SCAN、FINAL_SCREEN、BOOKS_PROPOSAL 和本记录。LEARNING_STATE 未取得本日专属 checkpoint，不以其他月份完成记录代替本日。没有执行每周来源扫描。

逐行检查 14 来源及查询/停止理由。实际定点打开 OpenAI Research、Anthropic Research、Google pubs、Meta Research、Qwen 新 Blog、DeepSeek、Kimi Blog、Hunyuan Research、ZAI Research、Seed papers、ERNIE 中文 Blog、MiMo、MiniMax 中文 Blog/Agent Tech，以及本日 arXiv 精确材料。当前入口与作者描述的滚动、动态、超时/空正文限制大体一致，但不能据此认证作者过去每一查询均已执行。没有找到新材料不授“零事件”。本轮没有无差别重放每个失败请求或扩成机构全年论文池。

**发现 A：Seed 的历史目录隔离过宽，仍有可执行原始恢复。** 官方 [papers 页](https://seed.bytedance.com/en/public_papers) 可读；浏览器本次也超时，但本机原始 HTML 可取得。沿该页公开的 `main.897993d4.js`，实际识别 `/api/get_article_list_v2`、`article_type`、`publish_year`、`count`、`order_desc`、`page_token` 与 `x-tt-locale`；不是猜测接口或把失败 URL 当扫描证据。

- 论文请求：[官方接口](https://seed.bytedance.com/api/get_article_list_v2?article_type=1&count=20&order_desc=true&publish_year=2025)，请求头 `x-tt-locale: en`。HTTP200、StatusCode0；`total=94`、`has_more=true`、`next_page_token=20`。返回的可见论文为 18 项，只读目标窗相邻条目即停止：Seedance 1.5 pro 的 `PublishDate=1765728000000`（UTC12/14 16:00，即 BJT12/15 00:00）与 GR-RL 的 `1764604800000`（BJT12/02 00:00）之间没有显示本窗条目。未将返回的窗外科学材料转为待逐项筛选队列，未继续 token20 或全量94项。
- Blog 请求：[官方接口](https://seed.bytedance.com/api/get_article_list_v2?article_type=2&count=8&order_desc=true&publish_year=2025)，同一语言头。HTTP200、StatusCode0；`total=45`、`has_more=true`、`next_page_token=8`。可见返回6项；目标邻接为 Seedance 发布说明 `1765882058000`（UTC12/16 10:47:38）与 GR-RL `1764604800000`（BJT12/02 00:00）。不继续 token8 或全量45项。
- 这些是**当前官方历史目录字段及其显示邻接**，不是逐篇 first-public 保证，更不是全源无遗漏。但已直接否定 SOURCE_SCAN/FINAL_SCREEN/README 所说的“2025历史目录未恢复、有限替代已穷尽”。普通动作是同步已恢复的历史停点与剩余边界，不要求无限寻源。

**发现 B：Pink Slime 的必要原始发表线索尚未收束。** 本次读 [2512.05331v1 原始题摘](https://arxiv.org/abs/2512.05331v1)，其中明确提示 `Published in RANLP 2025`。有限标题检索后，实际打开 [ACL Anthology 原始条目](https://aclanthology.org/2025.ranlp-1.128/)，标题、作者与题摘相符，出版字段 `September 2025`，原始 PDF 链接可见。它仍支持“改写可能破坏检测”的潜在反证，但该线索不能被总括进“全部arXiv v1的必要原始first-public入口已穷尽”。需有限核验既有公开稿与 v1 的事件/版本关系、是否确有本窗实质新事件，然后关闭为窗外线索或保留具体仍缺的公开依据；不由出版月补造首次公众时刻，不冒称9月报告已审。未打开整个RANLP论文池。

### 原始题摘校准

FINAL_SCREEN 潜在表为52个精确ID，不是确定落窗候选分母。ILVR、persona、SEA-Safeguard、M4-RAG 的身份/拟命题未变，按本记录此前原始读取与限定命题复用4项；Greek、Dynamic Alignment 的负侧与临床仅标题边界、SGLang `created_at` 路由亦只复用相应层，不授 Evidence 或当窗日期。

**新增48项均实际读官方 `https://arxiv.org/abs/<ID>v1` 完整题摘**（网页工具或本机HTTP取得原HTML后只提取 title/abstract），没有用 FINAL_SCREEN 的作者概括充当原文。逐项对应如下，日期未授前仅保留潜在增量，不评分、不正面采用：

| 分层 | 本次实际读取的新增精确ID | 校准边界 |
| --- | --- | --- |
| 量化、执行与预算 | 04746、05033、05325、05409、06443、05542、05134、05597、05746、05754 | 分别核层敏感度/scale、相对优势路由、probe+conformal、格式/硬件、并行LUT、reward/agreement、cache计划、结构MTP、单Hadamard及联合稀疏；不从摘要授生产收益或普遍加速 |
| 学习、编辑与优化 | 04753、04987、05105、05318、04545、04555、04748、04844、05387、05591、05865、05962、05802 | 保留训练/推理轨迹错位、环境构建、logit蒸馏、CoT配比反效果、连续编辑、任务采样、输入适配、源语冻结、自批评训练、entropy约束、可解释稀疏、精度/多样性与持续定制；不因小模型或负面结果关闭 |
| Context、检索与执行 | 04550、04868、05012、05732、05100 | 保留树形压缩、最小S-expression与完成、对比证据表示、conformal类别缩减及结构reward；CER临床评价不自动排除其通用表示机制，但没有验证跨域因果收益 |
| 安全、评价与设计反证 | 04838、05331、05379、05681、05700、05145、05809、05853、05651 | 实际核混合作者/对抗检测、改写反证、匿名后自偏好恢复、噪声标签、指标融合、自训练judge、random-verifier/想象信息瓶颈、跨图序列攻击及EXIF自监督；不把隐私/安全/归因标题当保证。VRSA页可见v2，未将v2混入v1或仅因修订号要求整篇比较 |
| 多模态表示、生成与物理行动 | 05150、05198、05385、05391、05394、05422、05513、05546、05564、05774、05693 | 分别核self-adversarial flow、像素等价latent合成、浅层pruning失效、tile压缩、latent谱、并行多层融合、回答/定位分离、中层attention干预、物理视频条件、按需像素证据及异构动作专家；医学标签不自动排除LoC-Path通用压缩机制，ProPhy不升级为真实dynamics证明 |

表内短ID均加前缀 `2512.`、版本 `v1`；10+13+5+9+11=48。安全/反证组逐项原始校准，不以分层抽样代替其读取。这里核的是“原文有没有该潜在命题及应保留什么边界”，不是完成48项必要全文审阅或证明其所有新颖性/实验。

普通负侧新增实际抽检 [ArtistMus](https://arxiv.org/abs/2512.05430v1)、[Bengali ToT](https://arxiv.org/abs/2512.05580v1)、[Classic Author GRPO](https://arxiv.org/abs/2512.05747v1)、[FedGMR](https://arxiv.org/abs/2512.05372v1) 四份完整题摘。前三项目前分别是领域语料/标准RAG、既有ToT的任务评价、任务风格reward；没有仅凭领域名称、实验小或单数字否定贡献。FedGMR 的 mask-aware异步聚合/收敛是真实机制，但受测FL问题及FEMNIST/CIFAR10/ImageNet100尚未建立当前大模型主线关系，不据distributed关键词入池；本次没有全读其证明。与复用的Greek/Dynamic两项合计六项具名普通负侧，临床条目另外只保留标题判断，不算完整摘要样本。其他宽列表明确范围外标题未全量抽检，不称全学科召回。

### 必要证据与 owner

独立实际读 [ILVR v1 HTML](https://arxiv.org/html/2512.05665v1) §3.1–3.3/§4.1/§4.3、Tables1–3及Figure4文字说明：hidden-state作为下一embedding；helper images用于训练teacher目标；selection结合intent/local history/前latent；第二阶段去teacher与alignment loss。只有三格component对照，不能拆成完整因子归因；K收益非单调，未核生产端到端速度或复现实验。已对读 Ch23实际canvas段、Ch24生成路径和Ch25 imagined/authoritative边界，认可 `MULTIMODAL-REPRESENTATION` owner，确认canvas段不等于完整覆盖ILVR。日期仍缺，草案暂缓，无Books写入。

GLM官网Blog本轮空正文，固定历史README经[官方contents API](https://api.github.com/repos/zai-org/GLM-V/contents/README.md?ref=e111410bc94b90fe19703ec89e07919b6cbbc49b) HTTP200取得，blob `8a667d7bf262646d1f5574a63469f142146196a4`；实际读News、GLM-4.6V Model Overview和Remaining Issues。native视觉工具输入/返回区别于文本序列化，可保留潜在表示/接口增量；旧2507.01006不授4.6V新技术报告。实际读 [AutoGLM官方说明](https://autoglm.z.ai/blog/?embed=0) 的虚拟手机/回放干预/开源工具链与限制，以及Ch78真实执行合同；私有部署/隔离宣称不能当隐私和权限实现已证实。两者日级标签/commit仍不授first-public，未恢复历史代码实现，不进入Books。

### 普通待办与未检查边界

**普通待办2项：** A同步Seed已恢复的有界历史目录、替换过宽受阻表述；B完成Pink Slime可用原始发表稿的有限事件/版本核验并同步处置。需要作者/root更新SOURCE_SCAN、FINAL_SCREEN及README正文§2/§5等依赖判断，本会话按授权不改这些位置。不得保持“作者普通待办0”并直接宣布日级完成。修复后只重开A/B及相应正文一致性，不推倒其余有效校准。

本次没有证明全部机构历史目录完整，没有全量复放作者历史查询，没有逐篇恢复52项first-public；没有全读48项论文正文/附录/代码、没有实验复现，没有复核未就绪日期，没有Books修改或写后整合验收。已真正穷尽可用必要原始入口的日期保留项可以安全结束，并非Coverage/Evidence通过；本次未通过由上述**可执行项**触发，不是要求所有外部日期等待到达。

机器检查：本日V3格式校验通过；限定文件Markdown/本地链接、原追加内容完整保留、README §1–5不变与空白检查通过。机器检查不代替语义验收。本会话只改本日README metadata/§6和本文件追加；未stage/commit/push，不动Books、月index、state或其他日期。

### 独立身份补充

用户随后明确指定本次非作者 agent 身份为 **Popper**；此前“Codex独立非作者验收者”描述指同一本次验收者，不是作者Plato，也不是既有root校准者。README §6已使用独立的 `复核者：Popper` 与 `结论：未通过` 行，未用共同chat ID作身份。原始检查范围、两个普通缺口和旧追加记录均保留；没有因更名增加通过范围。

## 关闭理由必要正文复核补充

复核者：Popper（同一本次独立非作者agent）。
结论：未通过

2026-10-02T19:09:00+08:00。用户提供27 HiFi-RAG误关闭作为风险提示；本次不审/改27，只重开09四个实际抽检负侧中受“摘要没控制/成熟组合/局部任务”理由影响的项。上述旧追加保留，**当前普通差额为A/B/C三组**；A Seed同步、B Pink Slime事件关系不变，新增C为四项潜在保留及边界同步。未增加确定落窗候选，不要求所有外部first-public恢复。

| 精确v1与实际必要位置 | 修正后的潜在命题与限制 |
| --- | --- |
| [ArtistMus 2512.05430v1](https://arxiv.org/html/2512.05430v1) §4.2/4.3、§5 Tables4/6和分析 | 固定1024 token budget比较chunk/Top-K，固定base/训练设置QA FT的contextual成绩退步，RAG输入会造成instruction-following失败；不能只按领域语料/成熟RAG关闭。保留测量与训练/检索条件反证，数值和普适因果未独立验证。 |
| [Bengali ToT 2512.05580v1](https://arxiv.org/html/2512.05580v1) IV-C/D/E、TableI、V/VI | 1024上限、Groq API、final-answer-only评价；高/medium推理及shot数并非单调，8B ToT下降。保留预算/模型条件下的局部负侧，不接受“模型小必不能ToT”的普适因果，也不把Colab硬件当API实际backend；不同位置模型名/开闭源表述不一致，不能直接采用性能定论。 |
| [Classic Author GRPO 2512.05747v1](https://arxiv.org/html/2512.05747v1) §5、Table3、reward setup、beta段 | 风格reward较高但完整性仍较差，弱judge内容分多为0.75/zero variance，多奖励加权与beta稳定性存在实际条件；不能只按写作任务/成熟GRPO关闭。保留proxy饱和和reward取舍信号，不把同reward训练/评价当独立人类质量证明。 |
| [FedGMR 2512.05372v1](https://arxiv.org/html/2512.05372v1) §3、§4.1/4.2、Algorithms1/2 | 缺失坐标不应当有效zero参与均值；初期降密度平衡更新频率，后期容量瓶颈触发restoration并增加时延；直接涉及异构分布式训练取舍，不能仅因非LLM数据集排除。保留机制及test-set触发评价泄漏风险待核，不声称已读完整收敛证明、全部ablation或LLM生产扩展。 |

作者/root的C动作：在FINAL_SCREEN/README §1–5把四项从普通关闭改为潜在保留，记本次实际正文位置/限制与精确事件状态；只检查同一有界段受共同理由影响的集合。潜在不等新颖性已证、评分、Evidence完成或Books采用；日期仍缺可安全隔离。本次通过修正关闭理由，而不是放宽准入标准。Greek/Dynamic旧校准、ILVR原始/owner和其他未变化身份继续定点复用，不全篇重读。

Popper接管metadata/§6和完成态校验，作者处理§1–5差额；09仍进行中，不等待其修正才推进ready10/11。最终机器检查在§6汇总，不改变未通过结论。

## 作者补证的独立验收更新

复核者：Popper（独立非作者agent，非Plato，非共同chat ID）。
结论：未通过

2026-10-02T19:24:00+08:00。本段取代此前A/B/C普通差额数量，不删除原追加。作者TARGETED_REPAIR及SOURCE_SCAN/FINAL_SCREEN/README对应补证已读；A/B关闭，当前只剩C一组普通动作。

A：实际原始Seed paper/Blog显示字段与本日邻接匹配作者新增记录。US/count20实际18/18、total94/45、next20；此前en/count8 Blog6是另一请求切片，不能混拼数量，也不要求复原Nash另次49计数。显示目录范围可安全处理，未显示库存及论文first-public仍不认证；作者已撤销过宽历史隔离。

B：本次实际打开[出版PDF](https://aclanthology.org/2025.ranlp-1.128.pdf)9页及[精确v1 HTML](https://arxiv.org/html/2512.05331v1)，对读§3数据/划分、Tables2/3、§6/6.1/6.2攻击/重放、§8限制。40k抽样、9473/10000、cluster80/20/三次运行、检测表、定向改写、1/100学习率与50% replay、控制/非控制及原分布退步均对应。正文把89.31称F1的表文差异在两版均存在，未当12月新增纠错。所查命题未发现12月实质增量，旧公开后归档关闭合理；这不是全字节同一或旧Daily已审的保证，不删除改写使检测退步的原反证。

C仍执行：四项05430/05580/05747/05372v1保留局部负侧/设计信号，作者同步FINAL_SCREEN与§1–5及同一有界段共同理由扩查；日期未授可安全隔离，不因负面、局部或成熟组合再次机械关闭。机器格式通过不授本日完成。

范围说明：验收者只改metadata/§6与本文件追加；§1–5的并行变化来自作者且保留。旧机器检查“正文不变”指当时验收补丁不写正文，不代表后续作者没有修改。最新V3/链接/空白及保留追加检查见§6；未stage/commit/push。

## 四项恢复同步实际验收

复核者：Popper（同一独立非作者agent，不是Plato）。
结论：未通过

2026-10-02T19:57:07+08:00。实际读作者最新FINAL_SCREEN表05430/05580/05747/05372及“有依据普通负侧”纠正、README §5；四项均准确保留本次必要正文校准的具体局部机制/negative和限制，撤销旧关闭，未授日期/评分/Books。作者明确复用Popper方法段而非冒称自身全读，本部分通过。A/B既有source identity与采用命题未变，定点复用，不再次全篇阅读。

C普通只剩同一有界段共同理由受影响集合的有限扩查收束，不能继续写“四项尚未同步”；作者§5也已明确剩此一组。不把日期隔离重开成全面全文审阅。最后收束报告时§5应显式“终态保留项”、不支持正面证据/Books/无遗漏断言及精确重开条件，避免10已实际出现的完成态措辞校验缺口；这不是重新索取所有外部firstpublic。

本追加与README metadata/§6更新不改§1–5/Books/index/state；机器检查如下补记，语义仍未通过。

本日进行中V3/本地引用校验及09–12限定diff空白检查实际通过；作者正文保留，机器通过不授内容完成。

## C有界扩查实际验收与精确二项修复

复核者：Popper（主线程委派的独立非作者agent，不是作者Plato或Books写入者root）。
结论：未通过

2026-10-02T20:15:20+08:00实际读FEEDBACK_C及§1/5最新同步；新增63项精确v1原始完整可读题摘全部独立HTTP200取得，未用作者数目代替原文。57项潜在机制/反证保持，日期隔离不评分/Books，原四项正文恢复已正确同步。原CL167–218/LG451–525/CV601–675/DC25–40受影响集合已有限收束，locator不扩队列。剩余普通只是一组二项负侧修正，不再要求重复63项或重开所有日期。

交Plato逐项修复：

- [04578 LexGenius精确v1](https://arxiv.org/html/2512.04578v1)实际必要§5.5/Table5/Appendix E：同四个Qwen对CoT/SFT/RAG/GRPO有局部退步，测试/训练与retrieval corpus分割有说明。保留“增强策略不保证获益”的潜在反证，不能关闭为只有legal inventory；模型版本/数据预算混杂尚未核，不采其“架构限制/原因”解释或GRPO普遍保证。
- [04759 CALAMITA精确v1](https://arxiv.org/html/2512.04759v1)实际必要§3.2–3.3/§4.2.1：生成输出解析/可接受边界改变分数；异质metric category平均与row-wise min-max为不同测量对象，后者依赖参与模型池，多category不加总。保留这些评价合同潜在，不关闭为只有community/harmonized pipeline。没有重读全部95子任务或旧2024公开史；若要按旧事件关闭，须明确这份December稿与早期必要方法/新增error analysis的对应，不从会议年份自动排除。

其余04765/05179/05243/06250完整题摘未识别可改变本项目通用机制/判断的本次增量，具体负侧保留，不因规模/非LLM数据集关闭。SGTM已有精确v1安全潜在与官方相交日标签，仍具名终态，不硬授09。作者完成二项恢复与README§5同步后，Popper接实际同步核与完成态校验。未改§1–5/Books/index/state，旧追加保留。

## 最终日级独立验收

复核者：Popper（主线程委派，独立于作者Plato与Books写入者root）。
结论：通过

检查时间：2026-10-02T20:26:03+08:00。实际重读最新README §1–5及FEEDBACK_C两项恢复，最终59项潜在/4项具体负侧与本会话实际63项v1题摘、LexGenius/CALAMITA必要正文校准对应。此前四项误关恢复、Seed有限18/18邻接和Pink Slime必要版本关系均已同步；ILVR实际owner不同机制保留，没有主题相近即判覆盖。普通待办0，metadata完成。旧作者交接待验措辞保留，以本节非作者最终结论为准。

所有first-public/动态历史缺段仍按具名终态不采用、不入Books、不支持Coverage/Evidence通过或无遗漏；无需把真正穷尽的历史隔离再列普通待办。未核全站/全月、全部论文正文/附录/代码、所有公众时间或实验；没有Books写入。完成态V3格式/本地引用实际通过，限定diff空白通过，最终补丁前后§1–5逐字一致。本次只改metadata/§6并追加本记录，不stage/commit/push。
