# 2026-04-24：每日来源范围的独立对账

复核者：root；2026-09-29。对照当前 `docs/RESEARCH_SOURCES.md` 每日组、正式日报 §2 与本日 `V3_INSTITUTION_NOTES.md` 的入口、停止依据、未覆盖面。本记录是**已保存证据的范围对账**，不是把历史站点重新实时抓取一遍，也不证明外部站点全量无遗漏。

当前每日组 14 个 ID 在正式日报 §2 各出现一次：13 个机构入口与 `SRC-ARXIV`。状态分成两类：`SRC-ANTHROPIC / QWEN / TENCENT-HUNYUAN / ZAI / BYTEDANCE-SEED / BAIDU-ERNIE / MINIMAX / ARXIV` 八项对其列出的有限入口已检查；`SRC-OPENAI / GOOGLE-AI / META-AI / DEEPSEEK / MOONSHOT / XIAOMI-MIMO` 六项明确保留目录、日期或正文缺口，没有把访问失败、空正文或旧首页判零命中。未发现每日组漏行或把每周来源要求混入本日报的情况。

独立检查的关键停止/隔离边界：

- Hunyuan `publicList` 明列 `pageNum=1,pageSize=100`、9/9，且邻接的 Hy3-preview 页面日期在本窗开始前，不能按04/23自然日挪进09点窗口；该 API 目录的 9/9 不等于全机构所有未列研究。
- Seed 的 Publications 与 Blog 是两个不同类型的列表；正文保存了各自页数、total 和邻界，且将置顶问题与 `21921` 的早目录线索单独处理。列表的午夜日期可能只有日粒度，不能伪作精确首发时刻。
- OpenAI RSS 的公告时刻可定位 GPT 家族，但 RSS 不能覆盖 Research/Index 历史分页；当前 system card 含后发更新，不当作04/23不可变原稿。Google Research Blog 与 DeepMind Blog 的月页不替 Research Publications。Meta 空正文、Moonshot 旧 Blog、MiMo 无日期 Blog 都已单独标成限制。
- DeepSeek V4-preview 的04/24日历日与本窗相交，未证明09点前公开。它只在日期终态保留项，不评分或纳 Books。其它已检查机构的仓库 `created` 列表均只作新 artifact 线索，不宣称旧仓库 release 或私转公已穷尽。
- arXiv 的 951 submitted API 库存是宽查漏材料，496为有界标题身份，162为题摘语义层；三者均不是冻结候选分母。跨分类去重和日期例外另审；不能用这个来源对账直接批准85个 arXiv 工作家族的当窗日期。

结论：来源**行与已记录有限范围**可对账，外部六项仍为明确的终态覆盖限制，不支持“14源全可访问”“本窗零遗漏”或 Daily Complete。整日还需对候选准入、date-family、负侧样本和最终 Books 处置作独立语义验收；本记录仅关闭“是否漏了 Required Daily ID”这一小项。
