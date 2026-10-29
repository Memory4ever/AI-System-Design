# May 11 来源补充：独立复核（2026-10-18）

复核者：`/root/may11_supp_reader`；非日报作者、非 Books 写入者。唯一写入范围为本文件。报告作者为 `/root/may11_supp_author`。

## R1 — 范围与恢复依据

已完整重读当前 `AGENTS.md`、研究合同、Report V3、来源使用说明/仅每日组/arXiv 主题与恢复规则、统一 Research 入口及 ROADMAP；实际读取 `LEARNING_STATE` 的“本次恢复（2026-10-18）”129/279 入口，不继承后面的旧暂停/旧全局快照。

本次只补 2026-05-10 北京时间自然日，保留 May11 原 101 候选的日期、评分、旧小时窗与连续原 §4 有效证据。旧有效 Source/Books 写后层不重审；新增材料、具体纠错或必要证据失效才局部重开。作者正在取得本日各源真实响应，尚未形成最终新增候选或完整六节报告；本节不是 DAY/FINAL。

独立复核按实际入口、主题与分页停止范围开始，随后核全部新选及安全/纠错/设计反证项，其余明确排除按来源、主题、理由分层抽核。宽月目录不变成逐项队列，Submitted 不替代公告，周末无常规 arXiv 批次不推出全源零命中。日期组合按当前研究合同采用，不要求无法穷尽的全球先公开证明。

首查实际原件已核：OpenAI 返回 HTTP403；可见已完成的 Anthropic、DeepMind、Qwen、DeepSeek、Kimi、Hunyuan、Z.ai、Seed、ERNIE、MiMo、MiniMax 为 HTTP200，但 HTTP200 本身不授历史覆盖。Meta 原件缺失与 Google 尚运行请求仍须按实际结果记录，不作成功检查。

本次无 Books 写入许可或新段，未 stage、commit、push；不修改 README、Books、LEARNING_STATE 或其他日期。

## R2 — 四条日期线索的题摘校准与窗外边界

实际读完四份官方 abs 原件的标题、完整摘要、Submission history 与可见 Comments：[OpenIIR 09321](./SUP_ARXIV_09321_20261018.raw)、[DeformMaster 09586](./SUP_ARXIV_09586_20261018.raw)、[Absurd World 09678](./SUP_ARXIV_09678_20261018.raw)、[Electric sheep 09693](./SUP_ARXIV_09693_20261018.raw)。同时实际读 [官方公告规则原件](./SUP_ARXIV_RULES_20261018.raw) 的发号约束、完整周安排及假日段。

这些不是四个“领域无关”排除：DeformMaster 的 structured physics rollout/neural residual 与 material experts、Absurd World 的逻辑不变而现实先验改变的评价设计、Electric sheep 的 action-only supervision/中间视觉状态与少量 visual tokens，均有潜在机制或证据边界贡献。OpenIIR 的共享运行时/typed scenario contract 是潜在窄贡献线索，但是否超出领域仿真模块组合须由真实归属日核定。这里仅校准潜力，不把当前摘要或作者收益称为证据审阅完成。

四份原件的唯一 v1 提交分别为 May10 UTC 04:46:58、14:55:54、17:55:38、18:25:52，均处于 Friday 14:00–Monday 14:00 Eastern 提交段。May2026 为 EDT，官方常规最早公告界为 Monday May11 20:00 EDT＝May12 BJT，已晚于 May10 补窗。故仅排除四个 arXiv v1 事件在本窗归属，不评分、不进新候选、不额外全文深审；不据此给整个 Source Family 断言全球首次公开或宣布所有来源零项。

09321/09586 原件当前分别为 May14 v2/May20 v2，不将其当前完整摘要回填历史 v1；版本号及日期本身不证明重要修订。09678/09693 当前 v1。四页可见正文没有指明撤回、安全纠错或重要勘误信号；并非遍历全版本或代码仓库保证。可见 09586 项目链接只作具名旁路线索，若获得落 May10 的官方正文发布证据，应只重开该事件资格。

本轮还实际核 [DataCite 查询原件](./SUP_DATACITE_20261018.raw.json) 为 `total=0`；这只证明本次 registered 查询没有返回，不证明 May10 无公告、无修订或无独立发布。arXiv 日列表请求返回404，不能作为读完列表。作者已告知补读 Qwen 当前研究入口与 Hunyuan 浏览器‘全部’页，待其保存实际停止证据后再作来源级复核。本节未授 DAY/FINAL。

## R3 — Seed 分页新线索准入校准（资格/Source 尚待）

实际解析 [Seed publications 第二页原件](./SUP_SEED_PUBLICATIONS_20_20261018.raw)，读完 ID1667 的标题与完整摘要：*Towards Robust Sequential Decomposition for Complex Image Editing*，外链 `2605.09233`。原字段 `PublishDate=1778342400000`，可复算为 May10 BJT；这是 Seed 目录的日期，不是 arXiv 公告日期、全球最早正文或历史逐字内容证明。`UpdateTime` 与 `ArticleID` 也不重命名为公开日期。

准入校准通过为潜在窄贡献：单步编辑易误解析复杂指令、顺序编辑又累计误差 → 统一 in-context 框架比较范式，并构造可控复杂度的合成任务及分解训练 → 需要重新判断何时保留分解、如何约束跨步误差以及合成能力迁移条件。不是因为属于图像编辑就排除，也不是仅以“新数据集/更高分”准入；尚未核正文，不能采用摘要中的 robust improvements 或 sim-to-real 结论。

本页实际 `has_more=true / next_page_token=40 / total=86`，不是“列表已读完”。作者须以实际日期顺序与页内停止位置限定覆盖，或处理必要后页。尚待官方正文/具体日期资格及必要证据，本节不授候选归属、Source、Books 或 DAY。

R2 补记：之后实际读完 [09321 精确 v1 题摘](./SUP_ARXIV_09321_V1_20261018.raw) 与 [09586 精确 v1 题摘](./SUP_ARXIV_09586_V1_20261018.raw)，其潜力判断保持；没有将当前 v2 原件冒称 v1。

## R4 — 09233 资格有限恢复后安全隔离

实际读回 [Seed1667 官方详情](./SUP_SEED1667_20261018.raw)：页面显示 `2026-05-10`，正文只有 ABSTRACT，Download PDF 唯一外链指向 `arxiv.org/abs/2605.09233`。其日期支持官方目录/摘要条目的日期角色，不能把摘要页改称已公开研究正文。

实际读完 [09233 精确 v1 abs](./SUP_ARXIV_09233_V1_20261018.raw) 的完整题摘/history：v1 `Sun, 10 May 2026 00:23:05 UTC`，按 R2 同一官方规则最早 May12 BJT；current v2 为 Jun1，版本号不证明本窗重要修订。另核 [当前已恢复正文的外链](./SUP_09233_CORE_20261018.raw)，没有具名项目/代码早正文入口；[CVF 官方页](./SUP_09233_CVF_20261018.raw) 只有2026 proceedings及 BibTeX June，不证明 May10 公开。

接纳一次精确资格外部保留，不以日期问题降贡献、无意义打分或假称完整 Source。可接受替代证据为 May10 的作者/机构完整正文及可复查发布日期原件，或能够明确约束该正文公开日期的原始记录；届时只重开本项。现在不进确定候选、不进 Books、不作为正面 Coverage/Evidence 或无遗漏依据。没有新的具名渠道信号，不为排除所有想象中的早稿继续无限检索；其余本日来源与报告工作正常继续。

## R5 — 实际来源范围与分层抽核通过（尚非 DAY）

已完整读取作者 [A1–A5](./SUP_SOURCES_20261018.md)，逐行核其14个每日源及实际触发的09233 CVF单篇，未扫描周频组。查询修正/失败/停止范围已公开：错误末界返回Oct的查询不采用；宽1044首30只作入口校正；随后四类各首8不是整类队列或全量初筛。独立实际解析四份 `SUP_THEME_MODEL/MULTIMODAL/SYSTEMS/AGENT` 原件的query、32个ID/title/published，确认各页止8且32条published均为May10 UTC提交字段，最早常规公告在补窗后；不能把total或当前v2/v3算入本日候选。

安全题名 `2605.09822 Oracle Poisoning`、`2605.09773 Exploitation Without Deception` 与系统设计线索 `2605.09735 KV-RM`、`2605.09681 Forcing-KV` 的元数据角色也在上述实际核验内。本轮未以“低价值/无贡献”排除这些信号，而是只排它们的本次 arXiv v1 事件落May10；不由仅标题推安全结论，也不对窗外材料强制全文。五个实际完整题摘身份已在R2–R4全核，新增确定候选0，故没有被漏掉的新选Source/Books工作。

独立实际解析Seed论文API token0/20两页全部38条日期/title及pinned标记，顺序跨过May10至Apr15，p20虽 `has_more=true` 但已越窗，允许有界停止，不要求40。精确May10条1667已R3/R4处理；THEMol、TDDFT等题名明确科学应用仅作范围外标题样本，不读全文，也不把38项都宣称完整题摘筛选。网页 `?page=2` 伪翻页与实际API恢复已分清。

其他来源分层抽核：实际原件核OpenAI403与Google/Meta缺响应头，不授历史覆盖；Qwen旧站重定向/Next与当前壳均不证明无项；Kimi最新实际2025-11-07，不能覆盖2026；Z.ai原件可见May20/Apr29相邻，MiniMax原件可见May26/Mar18相邻，ERNIE原件May9与精确release路径，均只支持相应有限列表；Anthropic原件May14字段未被当成May10，动态目录缺段保留。MiMo、DeepSeek与DeepMind按首查原件/作者明确未恢复历史切片接纳安全限制，不把有限抽核称全来源全项验证。

Hunyuan11条浏览器观察按作者保存的实际返回记录接纳为有限目录证据，非下载壳；本复核者尝试重新选择该已有页面时收到 `transport closed before response`，没有独立重获UI，不冒称自己看到了11条。这不为安全隔离的有限来源限制增添正面无遗漏断言，也不启动无限重试。未重读旧101候选及有效 Source/POST；本次无Books新增/改判，尚无须Books新写后核验。作者仍须完成六节归并，之后分别做DAY与真实保存态FINAL。

## R6 — 六部分 DAY 实际通过

实际读取已保存 README 的开头与§1–6：§1增补0与旧101/42整合/57已有覆盖/2仅报告分责，§2为当前14每日源＋1实际CVF触发＋补检共16行，§3不提前收资格未知或搬旧日期，§4原有效链复用，§5具名资格/来源缺段/窗外线索分开，§6本次独核与历史独核分开。R2–R5五个题摘与实际查询、全部新安全题名信号、分层样本的结论均已归并；09233不是贡献关闭，也不支持正面覆盖或Books。

DAY结论：通过。本轮确定新增0，新增Source采用/Books写入0，没有未处理的实质研究或Books普通待办。历史缺段及09233资格已完成有限恢复并安全隔离，不能把它们当成Coverage/Evidence通过或无遗漏。旧101有效Source/实际POST层不重做。

本复核者独立实际执行V3通过；核baseline为203869 bytes且逐字等于HEAD；101原候选完整行与原表逐字相同；旧§4全块连续存在（去两端换行正文110103字符，含原分隔换行提取110105字符）；§1–6各一，216个本地引用0缺失；README/作者SUP/本独核限定cached与unstaged `diff --check`通过。以上只证明机械不变量，语义判断由前述实际复核承担；不声明全仓clean或未读对象已审。

已请作者在完整旧§4后补一短句，说明本次没有新Evidence采用/Books改动、资格判断见SUP/§5，避免旧“本轮28”在当前报告里脱离历史范围；不改旧连续块。随后同步header/§1/§5/§6及SUP普通完成状态。尚待真实保存态FINAL；本节不以“已准备好”代保存，也不提前计入全局完成数。

作者随后修正Seed Blog US页行政计数为15。复核者实际解析 `SUP_SEED_BLOGS_0_US_20261018.raw` 确认数组长度15、total20、has_more=false；token20无sub_article_list，不能改称20条已读。README与SUP已读回实际更正，不改变DAY语义结论。

## R7 — 真实保存完成态 FINAL 通过

实际读回作者 `2026-10-18T19:09:27+08:00` 保存的 README：header为完成；§1/§5/§6已按R6 DAY实核同步，无新增确定候选/评分/Books写入；旧§4后已真实增补本次范围说明且旧块连续保留；09233资格/机构与arXiv历史切片均仍明确隔离，不授正面Coverage/Evidence或无遗漏。§2仍14Daily＋CVF单篇＋补检共16行，Seed Blog数已为15。原历史结论保持历史角色，没有把旧42整合算成本次新写。

本复核者实际再次运行V3通过；101原完整候选行逐字不变、旧§4全块仍连续；新增范围说明后本地引用为217且0missing；本日README/作者SUP/本独核限定cached与unstaged `diff --check`通过。没有检查或声称全仓工作树clean，也不由这些机器检查替代R2–R6语义结论。

FINAL结论：通过，可接纳May11本日来源补充到安全终态；实质普通研究/Books/独核待办0，所有本日ownership与未使用Books位置释放。本次仅补May10自然日，不接May12或其他日期；未stage、commit、push。作者可将报告及SUP的“保存态待FINAL”纯状态文字同步为本节实际通过，不重做Source/PRE/POST或另建完成收据；具体外部保留及重开条件不改变。
