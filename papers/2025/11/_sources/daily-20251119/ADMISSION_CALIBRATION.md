# 2025-11-19 首批准入校准请求

作者：Dalton。状态：root已实际完成首批准入校准；不是证据审阅完成或日级 ready。

窗口：BJT `[2025-11-18T09:00:00+08:00, 2025-11-19T09:00:00+08:00)`，UTC `[2025-11-18T01:00:00Z, 2025-11-19T01:00:00Z)`。只使用本日原始发现，不用旧 Weekly 或他日候选；14 每日入口已有实际访问，覆盖尚未完成。

## 请先校准什么

1. Gemini 3 发布家族的准入只计实际 API 兼容性/正确性变化，不计新模型名、SOTA 或成熟的权限原则。
2. 下列11篇完整题摘中的局部/负证据应保留为拟准入项，而非因单组件、摘要无实验细节、Books已有主题而关闭。此清单尚未冻结；日期确认与贡献校准分开。
3. 抽检下列明确排除项，特别是 Foundry 发布与 Gemini API 变化的差别，以及领域 recipe 与真正失效边界的差别。
4. 请独立核 arXiv 原始日期字段的证据权限：本作者暂不把 DataCite `registered`/当前 `findable`、`Updated` 或常规 schedule 单独当作已核实首公开。常规公告时刻仅用于识别可能跨截止，不补造精确时刻。

## 已核实落窗的拟准入家族

### [Gemini 3](https://blog.google/products-and-platforms/products/gemini/gemini-3/)

原始发布日期 `2025-11-18T16:00:00+00:00`，来自 `google_gemini3.html` 的 JSON-LD `datePublished`；BJT 19日00:00，完全落窗。当前页面 `dateModified=2026-03-19T17:52:32.737752+00:00`，因此明确不把当前链接到的2026年5月 model card冒充2025年11月版本。

实际核心说明：[开发者发布说明](https://blog.google/innovation-and-ai/technology/developers-tools/gemini-3-developers/)，原始抓取见 `WEB_GEMINI_DEVELOPER.txt`，L262–263、L292。多轮请求原有思考状态传递约束 → 官方宣布更严格的 thought-signature 验证，并新增 thinking level/media resolution 参数、允许 hosted grounding/URL context 与 structured output 组合 → 需要核验客户端状态携带与原有工具/输出组合的兼容性，而非只升级模型名。

暂定评分 `2 + 2 + 1 = 5`；兼容性/正确性变更无论分数均定点深入。`AGENT-CONTEXT` 暂作状态携带命题的 owner；工具组合不因此重复计家族。还需核必要参数语义、有效/无效签名条件与版本绑定。client-side bash仅是模型提出命令；hosted server-side bash当时为 early-access partners，GA coming soon，不能写成普遍可用或生产安全保证。未开始 Books 比较。

## 完整题摘拟准入，尚不冒充已确定当窗候选

共同原始依据：`first_batch_abstracts.xml`，官方 API `id_list`11个精确v1，`start=0,max_results=20,totalResults=11`。所有11份完整标题与摘要已实际读完；其中 API `published`与Submitted相同，不能直接用作公开时间。

| 身份与精确版本 | 约束/原判断 → 摘要实际增量 → 待核选择 | 暂定评分/必要审阅 |
| --- | --- | --- |
| [STEP: Success-Rate-Aware Trajectory-Efficient Policy Optimization](https://arxiv.org/abs/2511.13091v1) | 均匀任务采样且失败轨迹连带惩罚正确中间动作 → 平滑逐任务成功率驱动重采样、成功率加权优势、step-level GRPO → 固定采样预算下轨迹/步骤信用与难任务分配是否可解耦 | 2+1+2=5；标准，须核同采样预算对照及分组件收益 |
| [Souper-Model: How Simple Arithmetic Unlocks State-of-the-Art LLM Performance](https://arxiv.org/abs/2511.13254v1) | 同构模型均匀权重平均可能抹掉类别专长 → 利用低相关benchmark类别簇挑expert并非均匀合并 → 候选模型与合并权重选择是否应按异质能力而非总体分数 | 2+1+2=5；标准，须核选择集/测试集、搜索成本与泛化；Meta官方11月18日日期无时区仍不单独定窗 |
| [On the Brittleness of LLMs: A Journey around Set Membership](https://arxiv.org/abs/2511.12728v1) | 高级推理成绩不足以支持基础集合概念稳定性 → 跨提示、语义结构、顺序、模型的受控大规模失败映射 → 是否需基础等价变换探针补足评估盲区 | 2+1+2=5；标准，局部负证据准入，不采用摘要的普遍“理解”推断 |
| [Donors and Recipients: On Asymmetric Transfer Across Tasks and Languages with Parameter-Efficient Fine-Tuning](https://arxiv.org/abs/2511.13368v1) | 单个语言/任务LoRA收益不等于全目标能力收益 → 匹配任务跨语言正迁移、其他任务附带退化及donor不对称 → PEFT评估是否应显式区分任务/语言两条迁移轴 | 2+1+2=5；标准，核基线和全目标矩阵，负证据不排除 |
| [Catastrophic Forgetting in Kolmogorov-Arnold Networks](https://arxiv.org/abs/2511.12828v1) | 局部样条支撑可能被误读为固有抗遗忘 → 理论支撑重叠/内在维度条件与高维实验反证、KAN-LoRA编辑 → 局部参数化的保留收益何时失效 | 2+1+2=5；标准，核理论假设和高维反例，不要求普遍定律 |
| [Uni-MoE-2.0-Omni: Scaling Language-Centric Omnimodal Large Model with Advanced MoE, Training and Data](https://arxiv.org/abs/2511.12609v1) | 每token固定expert计算不能表达跨模态所需容量差异 → shared/routed/null experts动态capacity → 条件计算是否可用null路径控制计算而非只加expert | 2+2+2=6；标准，只审该命题及消融，不为85项benchmark全读附件 |
| [WebCoach: Self-Evolving Web Agents with Cross-Session Memory Guidance](https://arxiv.org/abs/2511.12997v1) | 存储历史不保证跨session有效使用 → condenser、episodic store与similarity/recency Coach，在runtime hook条件注入建议 → 历史指导应何时被触发而非全部塞入context | 2+1+2=5；标准，须核hook实际新增与同预算收益；若只是既有组合不能借成熟memory原则抬分 |
| [Visual Room 2.0: Seeing is Not Understanding for MLLMs](https://arxiv.org/abs/2511.12928v1) | 感知高分可能遮蔽认知步骤失败 → 350样例逐级6问题、17任务、10模型定位两类能力落差 → 是否可分解多模态评估而非单看总分 | 2+1+2=5；标准，核问题依赖、控制与局部范围，不采用Chinese Room哲学普遍结论 |
| [Dissecting and Re-architecting 3D NAND Flash PIM Arrays for Efficient Single-Batch Token Generation in LLMs](https://arxiv.org/abs/2511.12860v1) | single-batch decode容量/带宽约束 → H-tree flash PIM阵列及LLM tiling/mapping → NAND PIM是否提供不同存储/延迟可行性 | 2+2+2=6；标准，先核模拟/真实硬件、容量与预算可比，不当生产实现 |
| [Mitigating Length Bias in RLHF through a Causal Lens](https://arxiv.org/abs/2511.12573v1) | reward可能混淆质量与长度 → 同内容变长度/同长度变内容的反事实干预 → reward质量信号能否与verbosity区别 | 2+1+2=5；标准，核反事实构造有效性，非仅重复“相关不等因果” |
| [Live-SWE-agent: Can Software Engineering Agents Self-Evolve on the Fly?](https://arxiv.org/abs/2511.13646v1) | 离线scaffold开发成本且固定执行策略 → bash-only agent在当前任务runtime修改自身scaffold → 在线策略修改收益是否区别于额外test-time搜索 | 2+2+2=6；标准，核模型版本、token/调用预算和固定scaffold对照，不照录75.4/45.8 |

每篇有限日期恢复的原始值见 `<id>_datacite.json`及receipt；SoCE为 `soce_datacite.json`。例如STEP Submitted `2025-11-17T07:43:15Z`、v1 Updated `2025-11-18T02:29:42Z`、registered `2025-11-18T04:39:47.000Z`；SoCE Submitted `2025-11-17T11:13:34Z`、v1 Updated `2025-11-18T02:42:17Z`、registered `2025-11-18T04:43:28.000Z`。Available只有月份。DataCite恢复不是原始公告；拟准入论文需要实际公告或足够强的首公开上下界，不能单靠推定schedule授09:00精确首公开。

轻量修订信号：SoCE已有v2，Donors有v2/v3，UniMoE有v2，WebCoach有v2，Live-SWE有v2/v3，均为窗外修订；目前只读v1题摘，尚待当前官方abs页检查是否有影响原结论的纠错/撤回，不声称所有项“无标记”。

## 独立日期/版本保留

[Generative UI](https://research.google/blog/generative-ui-a-rich-custom-visual-interactive-user-experience-for-any-prompt/)：官方blog显示November18但时区/时刻未取得；不能当BJT整天。贡献拟准入 `2+2+2=6`：模型生成完整HTML/CSS/JS交互页，配合工具、提示与postprocessors；预缓存、忽略生成时间的偏好实验给出质量收益，同时1–2分钟延迟限制改变静态markdown与交互UI的选择。已打开原始22页[PAGEN稿](https://generativeui.github.io/static/pdfs/paper.pdf)，见 `WEB_DATE_PAPER_03.txt`；只是先校准必要机制/限制，不称标准审阅完成。

重要版本差异：原始稿/官方blog的44% expert-comparable不能与当前project页50%、ELO变化、2026年arxiv2604.09577混用。当前GitHubrepo creation在2025年6月不能证明原始paper当时公开。2次blog HTML直抓连接超时后停止同路径；web实际能读正文。下一步仅恢复官方精确日期或首公开区间、绑定原始稿版本，不扩全日全文队列。

## 代表性排除项及负侧写

- [Claude now available in Microsoft Foundry and Microsoft 365 Copilot](https://www.anthropic.com/news/claude-in-microsoft-foundry)：实际读核心说明，见 `WEB_INITIAL_CORE.txt`。新渠道public preview、Entra/Azure账单复用与已有Claude能力；明确Global Standard当时可用、US Data Zone coming soon。未公开新训练/runtime机制或新的已验证可靠性条件，暂贡献关闭；不得把“迁到平台”自动改写为新Agent机制。日期Nov18未精确核，因贡献关闭不再为日期深追。请校准是否确有局部兼容性新约束被漏收。
- [Microsoft, NVIDIA, and Anthropic announce strategic partnerships](https://www.anthropic.com/news/microsoft-nvidia-anthropic-announce-strategic-partnerships)：全文核心说明是投资、算力容量承诺、未来架构合作意向；未公开实现的codesign不能作为已有机制，关闭。见 `WEB_DISCOVERY_01.txt`与本日web原文记录。
- [Anthropic partners with Rwandan Government and ALX to bring AI education to hundreds of thousands of learners across Africa](https://www.anthropic.com/news/rwandan-government-partnership-ai-education)：实际核心是Socratic mentor/培训覆盖、使用及满意度，没有新增训练/评价机制；应用采用不自动成为Agent贡献，关闭。原始标题与正文见 `WEB_INITIAL_CORE.txt` L11–L31，日期未精确核不影响此处关闭。
- [Classification of Hope in Textual Data using Transformer-Based Models](https://arxiv.org/abs/2511.12874)：完整题摘在 `arxiv_language_advanced.extracted.json`；BERT/GPT2/DeBERTa二元/多类情绪分类的指标与训练时间，未见foundation模型形成机制或可比预算下通用边界；领域分类应用关闭，不按“小模型”排除。
- [NeuroLex: A Lightweight Domain Language Model for EEG Report Understanding and Generation](https://arxiv.org/abs/2511.12851)：完整题摘同上；EEG报告span-corruption、SFT与领域摘要/QA提升，当前AI for Science/医学应用范围暂停，不能借Data/Evaluation owner重引入。

上述排除不是当日完整关闭集。须保留题摘全值，日期未核者不冒充精确窗口材料。所有性能数字均尚未采用为报告正面证据。

### TDD+CI12823：撤销原关闭，潜在贡献日期隔离

[exact-v1](https://arxiv.org/html/2511.12823v1)完整题摘及§3–6由root实际核，见[负侧独立裁决](NEGATIVE_INDEPENDENT_REVIEW.md)。测试/编译反馈使小模型增强与大模型不同配置之间出现局部比较，跨语言收益依模型改变，不能因TDD/CI成熟自动关闭。原“未见组合失效条件或新执行保证”不足以否定潜在小模型/跨语种推理预算边界，现撤销关闭，不计确定落窗候选。

98%是best20B/best120B结果比值，不是绝对准确率；公开单测、隐藏评测、至多五次修复和单函数任务限制保留，未控制matched端到端预算，不授普遍替代或资源节省。原Submitted/API submission同值不认证public，本次没有有效首公开下界；最小请求是exact-v1实际官方公告/完全落窗的可靠首公开上下界。日期隔离不授Evidence/Books，不扩全methods/附件/owner；18篇潜在论文计数已包含此项。

## 入口、停止与普通待办

- arXiv：带submittedDate的API实际返回被改写的日期query及2026年记录，`arxiv_language.xml`/`arxiv_date_diagnostic.xml`无效；另一次500，不能记零命中。advanced submitted_date是most-recent而非首次公开，375结果只读首页作发现，不称375题摘关闭。announced_date_first的18～19查询空结果与已知SoCE相冲突，不授coverage。CL月表1527条只作原始查漏线索，实际有界标题区间2511.12500≤id<2511.13800；不将全表变题摘/全文队列。11个已知ID精确v1恢复止于单批total11。
- Seed：GET2个article_type各page_token0,count20,publish_year2025,order_desctrue,x-tt-localeUS，实际每页18项。type2是Blog（45总数）、type1是publications（94总数），文件名不能代替内容身份；pinned另看，has_more均true,next20。当前非pinned首项已在10月，置顶11月27也窗外；保留分页边界，尚需有限下页核单调/停止，不能称已全历年覆盖。
- Hunyuan：Research web动态空、IAB尝试有限失败，按用户接口线索POST publicList page1,size20,renderType0；实际total9为2026英文blog切片，不是2025 Research恢复。保留具体历史目录缺口，不把9条空窗当零命中。
- 普通可执行：Zhipu查看更多至目标月份；OpenAI/Anthropic/Qwen/DeepSeek有限历史原源补检；MiMo剩余博客段；arXiv其它主线窄主题与官方相关标题有界补检；11项实际公开边界、当前abs纠错轻检；准入校准通过后才展开受影响证据及Books比较。
- 外部保留尚未授终态：失效arXiv日期索引、Hunyuan2025 Research缺段、Generative UI原始日期/版本。只列具体替代要求，不反复空路径，不影响其他已可执行项继续。

Books实际写入0；owner正文与相邻尚未比较，不授已有覆盖/长期缺口。月索引、共享Books、LEARNING_STATE、ROADMAP及合同均未改；不stage/commit/push。

## 通知后继续的无关来源检查

- Seed两个page_token20实际取得。type2实际18项，首个非pinned为2025-06-17T16:00:00Z；type1实际20项，首个非pinned为2025-06-19T16:00:00Z。两页均has_more=true,next40，所有日期比目标更早；结合page0的置顶单核和下降序列，止于20，不追全年尾部。仅支持这个目录的目标日期区间检查，不证明已删除/未展示历史绝无遗漏。原始页及 `seed_page_boundaries.json`保留全部身份/日期，未把这些旧标题转为题摘队列。
- Zhipu Research恢复：本轮IAB不指定visible参数仍30秒超时；release notes实际读到2025-12-08→2025-09-30边界，目标窗口无release entry，但不能替代Research的查看更多缺段。恢复条件是Research本日历史段或可核的官方列表接口，不重复同一超时路径。
- MiMo剩余Blog段实际读完，见 `WEB_MIMO_TAIL.txt`：仍有More，标题无日期；Paper8条的2026-01-08→2025-10-21边界可核，Blog不能授无遗漏。
- arXiv官方advanced表单实际说明announcement date只支持year/month粒度，见 `arxiv_advanced_form.html`。因此之前18～19日级announcement过滤空响应属于不支持的查询，不是0命中，也不笼统怪索引。表单支持 `submitted_date_first`；仅以original submission日期作窄主题发现线索，再独立恢复公开边界。3个未带advanced参数的query仅回表单，无搜索执行，不计coverage；补正的language-model查询仍是本日普通停点。

## root实际首批准入校准（2026-10-04，本轮用户回传）

复核者：root，非作者。实际读完整 `first_batch_abstracts.xml` 的11份exact-v1题摘和Gemini developer核心tool/parameter/signature段。

结论：11个具体准入问题可继续相应标准审阅，日期未定不授确定当窗。Gemini 3 API兼容性/严格signature变化方向通过，命题限当时版本参数协议；bash proposal不是执行授权，early-partner hosted bash不是GA。KAN理论/局部负证据在模型学习主线，不按小模型排除。

特别限制：WebCoach不能把memory组合自身或38B vs4o比较当机理，必须核runtime hook实际新增及可比条件；SoCE需隔离benchmark选模型/调权与测试分数泄漏。日期API上界跨09:00不能据此证明窗外；继续有限恢复，真正不可得才隔离，不补造精确时刻。需要Books时只给现有owner具体差额，不造配方缺位。

本次不覆盖论文标准/深入证据、实际公开日期、Books正文/写入或日级验收；代表性排除未获具名实际抽检确认，不声称全量已过。language-model original-submitted补正query实际503结果，首页有later-announced材料，只为发现，未变503项题摘/全文队列。

## root后续单项与恢复协调反馈（2026-10-04）

root已实际核Gemini HTML身份/日期、developer目标段、精确两notebook关键cells、Ch75/78正文，OnlyReport倾向接受；正式notes未回传，不自授最终通过。其余11项仍保留完整题摘准入理由，已读必要证据见 [EVIDENCE_NOTES](./EVIDENCE_NOTES.md)，不是只停在摘要，也不因日期不定扩全部实验附件。有限日期恢复后明确潜在项可精确隔离，不正面采用、不写Books；这不是贡献缩池。中心纠错/冲突必要反侧仍核，普通work精确停点见 [AUTHOR_STOP](./AUTHOR_STOP.md)。

后续已实际读 [Gemini非作者正式记录](./GEMINI_INDEPENDENT_REVIEW.md)：仅此家族必要Evidence/OnlyReport通过；不授日级。11项有限日期恢复后的隔离、Donors必要中心修订处理，以及已有有限补检新命中的Codex-Max外生user-edit RL训练方向均在 [AUTHOR_STOP](./AUTHOR_STOP.md)；后者待root新准入校准，日期未定不评分/不正面采用，不重开首批11份abstract。
