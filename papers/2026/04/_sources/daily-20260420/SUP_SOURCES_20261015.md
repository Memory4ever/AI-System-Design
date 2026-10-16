# 2026-04-20 既有 Daily 来源补充（唯一补充记录）

## R1 范围、baseline 与当前上下文

作者：supp_apr20_author；独立复核者：supp_apr20_review。2026-10-15T14:59:03+08:00 启动本日记录。已完整读取本次 AGENTS、研究合同、来源说明/Daily14/主题路由、Report 合同、统一 Prompt、ROADMAP 及 LEARNING_STATE 本日最新路由。只补北京时间 **2026-04-19 ～ 2026-04-19**，不创建新日期、不运行 Live/Weekly/其他年份；共享 Books/State/index 由 root 协调，本日不 stage/commit/push。

运行前 `papers/2026/04/20/README.md` 的工作树与 index 均相对 HEAD 无差异；baseline=HEAD，可用 `git show HEAD:papers/2026/04/20/README.md` 直接恢复逐字比较。SHA256：`779f6da85d3f11cacadd3f6483f9ac9372359c44c7c8fbfe23b6fc66b94ac80c`。冻结原小时窗口、111 个完整候选表行（含日期/评分/处置）及完整连续原 §4；不是恢复已经被有效纠偏的 V2.1 记录。本次只改本日 README 与本 SUP，不改旧证据文件或 Books。

使用 using-agent-skills 的范围控制与验证原则；按当前研究合同复用身份、窗口与判断依据未变化的有效来源层，不因重复执行生成新的全文队列。原 [V3 作者来源停点](./v3-reopen-notes.md) 的机构来源两节、[三机构原始停点复查](./V3_THREE_SOURCE_STOPPOINT_REOPEN.md)及[原日级 Gate](./V3_ROOT_DAILY_GATE_20260420.md)已实际读取；只复用其明确记载的有限目录范围，不继承旧“完成”来验收补窗。

## R2 Daily14 补窗来源检查与停止

以下复用均是 **已有本日有效目录/查询范围覆盖 Apr19 整日**，不是声称本轮重新抓取十三机构、读取全部题摘或核完所有仓库。旧停点中位于 Apr20 的事件不搬入补窗；无新增相关且日期落窗的信号，因此没有新的完整题摘或必要全文队列。

| 来源 | 补窗实际依据、停止点 | 结果与权限边界 |
| --- | --- | --- |
| SRC-OPENAI | 复用本日 RSS April21→Hyatt April20 00Z→Codex April16 10Z 可见段；Apr20 00Z=BJT Apr20，非补窗。 | 所见 News 段无补窗项；Research 历史分页仍受阻，不能推全 Research 零发表。 |
| SRC-ANTHROPIC | 复用 Research 71 个 publishedOn 的 April14→April22 两侧停点。 | 该公开目录跨过 Apr19 完整日，未产生新增；不外推全站。 |
| SRC-GOOGLE-AI | 复用 Google Research April Blog 完整9项 April16→21，DeepMind blog p3 七项 April15→22 与 selected-research264项 March22→April22。 | 可见目录跨窗无新增；Publications年度771宽目录缺日级首公开，仍受阻，不展开宽库存。 |
| SRC-META-AI | 复用本日可读 Publications p2 近期 May19→April16→April14/9 停点。 | 可见有序段无新增；Research 首页仍缺可靠逐条历史日期，受阻；旧年混排不作全域证明。 |
| SRC-QWEN | 复用官方动态 API 完整40项 extra.date 的 April18 10:00+08→April22 10:00+08。 | Apr19 整日无目录项；April18 事件不移日，不推全仓库无 release。 |
| SRC-DEEPSEEK | 复用本日本来明确保存的 News16条 April24→December1、Research June24→February25。 | 可见官方目录跨补窗无新增；组织39项不证明全部 commit/release。 |
| SRC-MOONSHOT | 复用注册 Platform Blog 当前26项/latest2025-11-07；kimi-cli100 releases 的 1.36 April17 14:10:46Z→1.37 April20 16:01:36Z。 | 注册 Blog 与该 release 范围无补窗项，不推未列研究/其他仓库零事件。 |
| SRC-TENCENT-HUNYUAN | 复用 publicList POST pageNum1/pageSize100/renderType0、total9/list9 的 April23→February13。 | “全部”研究目录范围无补窗项；可选仓库403/503不作全 release 覆盖。 |
| SRC-ZAI | 复用官方 Research15/16项 April29→April7→April1、release June16→April7→February12。 | 可见目录跨窗无新增；部分 GitHub403仍只隔离可选入口。 |
| SRC-BYTEDANCE-SEED | 复用 papers type1/count20/desc/page20 实际20项、next40/more，近窗 April21 16Z→AgentWorld April19 16Z→LeapAlign April15 16Z；Blog type2/page0 nested15项 April22 16Z→April8 16Z，已跨左界。 | AgentWorld CMS April19 16Z=BJT April20，不是 Apr19 补窗候选；保旧窗口日期/正文隔离，不重新评分或借后来论文证明提前公开。其余可见段无新增。 |
| SRC-BAIDU-ERNIE | 复用 Blog2页10项、2/2终页 April30→April15→February6。 | 可见技术 Blog 跨窗无新增，不外推未列材料。 |
| SRC-XIAOMI-MIMO | 复用 Paper8项 June29→March13；Blog 相邻官方正文 MiMo-V2.5 April22→V2-Pro/Omni March18。 | 当前可见排序段跨窗无新增；不因卡片无日期写零命中，也不推站外无事件。 |
| SRC-MINIMAX | 复用 EN/CN Blog12/13项跨窗段、cli26 releases终页 1.0.12 April26 01:40:29Z→1.0.11 April17 20:51:17Z。 | Blog及该仓可见段无新增；Agent Tech Blog只有May13单页、历史字段不足，终态保留，不据此断言整个机构零事件。 |
| SRC-ARXIV | 本轮实际重开[官方 availability](https://info.arxiv.org/help/availability.html) 的 Announcement Schedule 与2026 holiday段：Eastern Fri/Sat无常规公告，Sunday20:00EDT对应 **BJT Apr20 08:00**，不是 Apr19。Apr19整日没有正常公告槽，规则适用于new/replacement/withdrawal/cross-list事件；April19不在列举假日。 | 常规公告检查结束，不把 Submitted Apr19、旧447标题/150题摘或Apr20公告111家族搬入补窗。非公告的站外更早正文不能由此排除；已知官方机构源另按各自行检查。 |

本轮辅助重开 `https://arxiv.org/list/cs.CL/2026-04?skip=0&show=2000` 返回429，不能记为零命中；在官方常规公告规则已足以划定空槽时，不为12分类重新抓整月宽列表。主题仍限 CL/LG/DC/AI、CV/RO、AR/PL/OS/PF、IR/MA 对应模型/多模态/训练/推理/平台/Agent主线，而非分类全量关闭队列。Seed Research 当前可读featured段 April22→April15（中间无April19），仅作可见官方入口核对，不替代已有精确分页停点；Qwen `/blog` 当前网页抽取无正文，不把空响应算覆盖，仍只复用上述实际完整API范围。

## R3 准入与证据、Books 处置（待独立复核）

补窗确定新增候选 **0**，新的完整题摘 **0**、新的必要证据审阅 **0**、新的 Books 写入 **0**。这不是从周末推全网零发表，而是现有有效机构停点确覆盖 Apr19、常规公告无槽，未发现须进入题摘准入的窗内新身份。无新首批正反材料集合，不人为恢复V2旧候选；校准重点是入口/日期边界、旧结果复用范围及潜在误收 AgentWorld。原111家族、26整合/13已有覆盖/54仅报告/18中心争议及原38前闭/1身份隔离不变。

OpenAI Research历史分页、Google Publications日级、Meta Research历史逐条日期继续为本窗终态覆盖保留；MiniMax Agent Tech Blog历史字段不足及各机构未列材料不能用于正面证据、Books或无遗漏。可接受重开是对应官方可读历史目录/存档出现Apr19具体材料，或可靠当日官方原文/公告；只重开该来源/家族的真实归属，不扩整年或Weekly。原AgentWorld、π0.7及18中心争议保留原§5精确条件，不借补查解除其限制。没有可执行但被改名外部受阻的普通待办。

## R4 实际 ADMISSION/Source 通过与六节保存

supp_apr20_review 2026-10-15 实际完整读取 R1–3，对本日 V3 原来源机构两节、三源停点和旧 Gate 核范围/时间，独立重开官方 availability 核 Announcement Schedule：Apr19 BJT无normalbatch、Sun20ET属Apr20。其实际裁决为：14来源齐，复用范围跨Apr19整日、有限停点不继承旧完成；0新增的有限结论通过，无新正反样本队列，不重开旧111或38有效前闭；AgentWorld CMS April19 16Z已是BJT Apr20，不能加入补窗。OpenAI/Google/Meta/MiniMax TechBlog的历史不足与arXiv429辅助停点均明确限权；不可概称“五个必查主源失败”，也不授完整Coverage/Evidence或无遗漏。

已保存 README 六部分补窗内容，原连续§4未插字。首次校验报111项窗外，诊断为V3校验器需要显式`冻结候选日期`原档案字段，不能只用HEAD哈希；未修改评分/日期或校验程序。按其现有接口用apply_patch保存[逐字原档案](./baseline-before-supplement-20261015.md)，SHA256与R1完全一致，并链接到header后重跑V3通过；这项修复受debugging-and-error-recovery技能的先定位根因/保存证据约束影响。

实际机械验证：baseline完全等于HEAD；111个完整候选行逐字相等；原小时窗口不变；完整连续原§4为70173字符且逐字相等；正式README226个本地引用、83唯一路径、0missing。README/SUP/baseline的限定unstaged与cached diff-check均通过，未触碰预先存在的index/并发内容。这些只验证格式/冻结，不替代actualDAY或保存完成态actualFINAL。

## R5 actualDAY通过与保存完成态

supp_apr20_review 实际读取保存的六节受影响内容、完整HEAD差额、R1–4及原来源/Gate有效层，2026-10-15 actualDAY通过：§1补窗0与旧111分开；§2 Daily14及跨Apr19停点/权限自包含；§3不迁移旧日期、不恢复有效排除；§4连续原文逐字不改、旧证据/Books按有效层复用；§5普通研究待办0、外部历史/身份/争议隔离及重开明确；§6未借旧PASS代签本轮。独立实跑V3与限定cached/unstaged检查通过，baseline SHA、111完整行、原小时窗、完整§4均一致（70173不含标题，含标题70186，口径差非内容差）。

作者据此串行同步完成态及DAY行政文字，不新开机制审阅或改Books。15:04:05+08观察README为MM、SUP为AM，系并发index变化；本作者/reader均未stage，不操作或覆盖index，不宣称index未变/干净。当前保存完成态待唯一actualFINAL实际读回。

## R6 保存完成态 actualFINAL 实际通过

supp_apr20_review 2026-10-15 实际读回完成字段（完成、Apr19补窗、原小时窗、baseline链接）、§1/5/6行政差额与R5后，actualFINAL通过：保存态与已通过DAY一致，只同步已发生DAY/普通0与并发index限权，没有新增机制、候选或Books主张。独立实跑完成态V3、README/SUP/baseline限定cached及unstaged diff-check通过。验收范围仍是14来源有限停点、补窗0新增/0Books、原111及原§4有效层复用；历史目录、身份与争议不授完整Coverage/Evidence或无遗漏。

本段只行政归档真实FINAL消息，不引入重复FINAL循环。作者/reader本日ownership均释放、无Books窄锁、无普通待办；reader退出，不接别日。本方未stage/commit/push，State/索引与并发修改保留，由root接纳本日后fresh路由后日。
