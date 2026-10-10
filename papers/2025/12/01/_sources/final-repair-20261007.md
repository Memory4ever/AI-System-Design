# Dec01 Huygens具名差额返修

作者：Laplace，本会话Dec01作者；非本日独立复核者Huygens。仅处理2025-12-01补充窗口2025-11-30。
执行：2026-10-07 17:51起重新加载main当前AGENTS、Prompt、研究/Report合同、每日来源/arXiv说明、ROADMAP和State本日路由，随后只加载Dec01本日材料。Aug01窄复核已收束，不把其结果授给本日。

本轮只改本日README、新增本记录与[新原件目录](final-repair-20261007/)，旧历史发现记录、独立复核及原件均不覆盖。未使用catchup，不改旧窗口/日期/评分/有效审阅、Books、State、合同或Git。依据[Huygens日级未通过](review-resume-final-20261007.md)，普通返修只有三个具名误关闭及Google有效筛选；不是重开全月库存或重读17项。

## 三项误关闭的实际返修

旧作者关闭理由保留在[原历史发现](history-discovery-20261007.md)，由以下决定事实取代，不删掉错误历史。

| 精确身份及实际阅读 | 原判断 → 新判断；最小增量与限制 |
| --- | --- |
| [2511.23220v1 ITT-Gen](https://arxiv.org/html/2511.23220v1#S4)，复用完整v1题摘，实际定点读§4～5/Table1～2，止§5；原件`tabular-v1.raw` | C→窄潜力：有限适配预算下，table snapshot+metadata构造指令、单A100的SFT与base输出有效性/分布评价形成可核边界，不能要求先有新优化器或普遍定律。§5明确base的非表格输出先过滤，fidelity仅在可用输出上计算，不等完整指令成功率；表内各任务非全面优于GPT-4o。仅保留局部适配/评价条件，不认证临床/领域能力、等预算优越、统计显著性或通用效果。未读补充实验/代码，不比较不同任务TableLlama资源。 |
| [2511.23454v1 Debate](https://arxiv.org/html/2511.23454v1#S1)，复用完整v1题摘，实际§1～2，止Definition2.14相邻说明；原件`debate-v1.raw` | C→窄理论潜力：正文直接连接AI safety via debate；裁决policy预先commit、世界状态限制可验证行动，common/private information的行动可见性不同。由此应重新检查弱judge所需的验证/信息接口，不能凭摘要未出现LLM词排除。§1.2的复杂性/误差界只是作者结果概述，后续证明未读不采用；有限行动集合和先验已知不等自由文本幻觉judge或安全保证，也不把多轮展开的表示成本消掉。 |
| [2511.23142v1 audio codec adaptation](https://arxiv.org/html/2511.23142v1)，本轮完整精确v1题摘/abs身份轻量标记，定点§2.1，止§2.2前；原件`codec-abs-v1.raw`、`codec-v1.raw` | 题名范围C→窄潜力：预训练音频codec在新模态复用受stride/采样及通道接口约束；跨通道attention与channel-specific decoder改变token时间语义与初始化/压缩选择。不是EEG临床应用准入，不授医疗结果或跨所有模态通用。保留预训练/从零对照的潜力，但结果/训练公平性未读不认证；§2.1采样率与bitrate的文字次序有不相容处，不采用具体bitrate数字。 |

三项皆**具体首次公开日未知、未评分、不列确定当窗候选、不作正面性能/安全/Books采用**。23220的ICML2025 workshop评论只能提示可能更早公开，不能用其替代具体首公开日。日期到达才按真实归属定点补相应证据；这不是把已清楚的准入潜力放回Q。当前取得这些决定事实即停止，不强迫三项整稿/附件审阅。

Huygens已经扩查相关领域标签/理论/适配/codec共同错误集合，复用该结果，不再扩大。五项旧题摘排除中的23377/23315/23397继续关闭；原十五题名侧的其他十四维持Huygens实际语义理由，其中8已由其完整读题摘、6仅题名范围核。详细身份、未检查范围和安全限制仍由其原记录承载，不称全部排除正文已审。

本批分母仍65次题名观察/45身份，8旧复用/37新身份。37新增为**20窄潜力、3完整题摘关闭、14原题名侧关闭**；14中8已补读题摘，不再写成全部只题名。原22份新题摘加本轮23142原题名侧恢复，至少23新身份完整v1题摘有直接作者读取；其余补读以Huygens实际范围复用，不冒称本作者均陪读。新增确定落窗仍0，日期集中请求从17扩为20身份，不搬旧材料。

## Google原生筛选与可核停止

本轮首先用浏览器绑定实际Google pubs入口，创建页并导航超时，工具返回`js execution timed out; kernel reset, rerun your request`（30.017秒）。没有获得DOM/UI筛选成功，不虚构HTTP状态或点击。此路径无新网络原件，失败观察只记本文件。随后官方HTTP路径成功，不把浏览器超时扩大成Google不可达。

实际入口参数**来自官方实现，而非猜year/date参数**：

- `google-pubs-default.raw`的filter元素`data-use-facet-names=""`，仅Year/Team/Research Area类别，2025 input默认未checked；没有月/日或date input。
- 同页实际加载`/gr/static/js/googleresearch.js?id=ce1a221e995a08edf74272a1419af1e4`。所存`google-filter-js.raw`中`useFacetNamesForQueryParams`仅属性字符串true时启用，`chunkSingleCategoryQueryArgs`否则生成`category=<value>`；ConfigurableList实际读取`search`并保留filter。故使用下面源生参数，不再用无效`?year=2025`。
- 两个有效查询响应都实际有`id=filter-year-2025`的**checked属性**；结果不是默认1–15/11597。这是源生筛选已执行的原始依据，不拿HTTP200本身当过滤有效。

| 新请求/UTC起止 | 实际结果/分页停止 | 权限 |
| --- | --- | --- |
| `google-pubs-default`，09:54:17.025857～09:54:18.764465 | HTTP200，325377B；只恢复控件和官方JS路径，未将默认年度库存逐篇筛选 | 默认页成功不授目标日覆盖。 |
| `google-filter-js`，09:55:19.733588～09:55:21.537995 | HTTP200，564877B；只读上述filter/search参数实现 | 参数出处，不是论文证据或页面UI成功。 |
| [native year+language model](https://research.google/pubs/?category=2025&search=language%20model)，09:55:49.941983～09:55:52.885959 | HTTP200，366460B；2025 checked、1–15/37、3页；实际核首15身份/venue年份/页面结构，止第1页，不取第2/3页，不读附件 | 第一个Toward expert-level medical QA，最后RADAR；限定主线主题的2025出版年库存，没有Nov30日列。37不是本日潜力/候选/全文队列；本次不把年度条目新增到本日分母。 |
| [native year+target-day text](https://research.google/pubs/?category=2025&search=2025-11-30)，09:57:02.629905～09:57:05.355402 | HTTP200，241656B；2025 checked、0–0/0，终页，无下一页 | 这是**日期文本搜索**而非首公开日筛选，不授Nov30无论文或零事件。 |

所有成功请求的URL、实际起止、字节、状态和SHA256在新目录逐项request JSON；未覆盖Sartre/Avicenna当时timeout/Internal Error原件。原已执行的两条官方域目标日+主线主题补检均Empty且停首轮，复用[16:12原记录](supplement-20261007/google-directory-recovery-1612.md)，不虚构新执行。Google Blog本轮既有日期段和DeepMind真实首页邻接的Sartre局部确认仍有效，不因pubs源生参数恢复而重扫。

**本窗终态保留提案**：先前普通工作“尚未执行实际filter”现在已执行并确认生效；剩余不是默认为2025即可填Nov30，而是该出版目录只提供publication year/主题索引，没有本日首次公开批次/日期。主题首页和目标日文本终页均不能认证目标日完整性，隔离其Coverage/零事件/采用权限；不无限猜日期参数、扩全年/37题名逐篇追日或把未翻年度页写外部故障。可接受重开材料是官方具名Nov30历史公开目录/公告，或具体作者首次正文日证据；到达只恢复相关身份。本提案待Huygens独立判断是否达到安全终态，作者不自签穷尽所有互联网入口。

## Books与复核交接

本轮没有具体验证到可写书的长效差额，三项不因有owner就认定已有覆盖。必要恢复路由仅供root：23220→`TRAIN-SFT`（适配/输出有效性条件），23454→`AGENT-MULTI-AGENT`（adversarial debate的裁决/信息接口），23142→`MULTIMODAL-REPRESENTATION`（codec token时空/初始化接口）。日归属与必要证据尚缺，不申请写入、不多owner复制；其他DDAM/SafeHumanoid唯一owner提案沿用有效记录。

**作者返修READY，非作者最终未返。** 请Huygens仅核这三项处置/日期隔离、排除语义与数量同步、Google源生filter及上述终态提案，再作日级裁决。原17潜力、DDAM/SafeHumanoid必要反侧、Sartre八项/撤回/Super公式/DeepMind修复未受影响，均复用，不重审。若仍未通过，指出本差额最小必要事项；不可把宽月/全年库存变强制全文队列。作者README先保持进行中；独立通过后才同步完成态V3并运行静态检查。

18:00写回后静态检查：当前main校验器对本日1份V3退出0；新记录本地链接错误0、尾随空白0，8份新request的字节/SHA256与raw逐项匹配，均HTTP200、catchup URL为0；辅助读取脚本语法检查通过，未产生pycache。只证明格式/保存一致，不代替Huygens语义裁决。原件下载不等全文阅读，决定段实际范围已逐项列明。未stage/commit/push，未执行Git写。

## 最终裁决与完成同步

Huygens已实际追加[修后最终日级裁决](review-resume-final-20261007.md#作者具名返修后的最终日级裁决)，结论通过，含明确隔离的本窗终态保留项。其定点实核三项、Google源生实现/响应/8请求保存、排除数量与README理由同步，未重审原17或Sartre。此前作者READY/最终未返是当时停点，现已由此裁决取代。

作者于18:13:35+08:00锚点后按已保存的独立结论同步本日README状态完成和§1～6当前权限。首次完成态静态检查退出1，原因仅是`结论：通过`后同一行带括号不符合完成态解析；将解释移到下一段，不改变语义裁决，重跑当前校验器1份V3退出0。README、作者返修记录及独立记录的本地链接/尾随空白检查均0。最终写后再核同样范围，不因静态通过扩大Coverage/Evidence或Books权限。

本窗普通可执行事项0；确定新增落窗0；20窄潜力及旧具名日期/历史目录/中心争议保留项继续隔离，不评分、不正面采用、不进入Books、不授无遗漏。旧窗口/候选日期/评分/有效审阅不动，本轮Books改动0，未修改State/合同/索引或执行任何Git写。此为Dec01本日闭环，不更新全局验收分母，也不启动下一日或Weekly。

### 18:30最终读回同步

按用户最新指示实际读回Huygens18:08:53+08:00最终日级PASS和18:11:07+08:00写后保护检查，README六节及来源当前普通待办均与裁决一致。精确锚点补入§6，旧作者READY及首次未通过只作历史，不作为当前状态。此前本轮再次执行本日限定`git diff --check`与当前V3均退出0；本次锚点写回后继续限定复验。独立记录不由作者修改。Aug01仍未日级通过，具体普通差额已另通知其作者；Dec01结论不授Aug01任何完成权限。
