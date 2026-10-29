# 2026-03-03 增量来源补查

作者：supplement_20260303。执行：2026-10-09 Asia/Shanghai（raw抓取完成至2026-10-08T20:09:51Z）。只own本日README及本目录；不修改Books、索引或LEARNING_STATE，不stage/commit/push。依用户增量授权保留原窗口、原0候选及连续原§4；新增检查2026-03-02完整自然日。原正文存于[baseline](./baseline-before-supplement-20261009.md)，旧停点不授本轮日期权限。

## 一、十四每日入口与停止点

raw原件均为本目录`SUP_<名称>.raw`及对应headers（必要恢复例外单列）。curl仅负责保存原件；下述为实际读完的有限日期段，不授机构全史保证。未扫描每周来源或未经触发的按需来源；不做arXiv catchup/无效advanced日范围重试。

| 来源 | 原入口/实际动作与停止 | 结果及限制 |
| --- | --- | --- |
| SRC-OPENAI | [RSS](https://openai.com/news/rss.xml)1257item，实际解析Mar01–04邻接段；[GPT safety](https://deploymentsafety.openai.com/gpt-5-3-instant/safety)完整官方HTML；[DoW](https://openai.com/index/our-agreement-with-the-department-of-war/)curl challenge后web原稿L20–30与更新分隔线 | RSS Mar02无item仅限feed；HTML Published March2按官方日纳本轮，不拿RSS覆盖HTML。DoW Mar02是同家族重要修订，原03-01已明确不采用此段。[SUP_DOW_WEB.txt](./SUP_DOW_WEB.txt)为可读原稿工具结果，curl不算成功正文。 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research)SUP_ANTHROPIC.raw嵌入Publications；实际publishedOn相邻02/25T20:02Z→03/05T19:59:21.508Z | 该目标段无03/02目录事件；不只据首屏十条、不外推未列入目录事件。 |
| SRC-GOOGLE-AI | [DeepMind](https://deepmind.google/research/)当前页；[pubs](https://research.google/pubs/)curl超时后web1–15/11600和year筛选；March2官方主题检索 | 当前Research无March历史cursor，pubs只有year精度/当前15条，不能授本日覆盖。Gemini Flash-Lite原官方Mar03证据冻结，不属本轮Mar02补充窗；缺的是本日历史主题段，不再请求时区。 |
| SRC-META-AI | [Research](https://ai.meta.com/research/)curl连接reset，一次web恢复0行；March2官方域主题检索 | 历史主题段仍受阻。搜索无相关条目不能证明零研究。 |
| SRC-QWEN | [新blog](https://qwen.ai/blog)curl壳/一次web0行；原有效Qwen3.5官方repo Mar02与9B/2B核心关闭复用 | 原小尺寸家族EX理由不变；新blog必要历史段未恢复。Code原Mar03汇总本轮窗外，旧PR不重审。 |
| SRC-DEEPSEEK | [updates](https://api-docs.deepseek.com/updates)SUP_DEEPSEEK.raw完整日期日志02目标邻接2025/12/01→2026/04/24 | 该日志段无03/02事件；不授隐藏研究覆盖。 |
| SRC-MOONSHOT | [Kimi Research](https://www.kimi.com/en/blog)SUP_MOONSHOT.raw完整可见19条到2024/06/26；邻接02/09→04/20 | 当前目录无03/02条目。补检forum Jan30 thread的Mar02用户429回帖不是本日研究/新版本发布，不采社区猜测机制。 |
| SRC-TENCENT-HUNYUAN | [Research](https://hunyuan.tencent.com/research)壳；按[已核页面实际API](../V3_HUNYUAN_LIST_RECOVERY.md)一次POST publicList，pageNum1/pageSize20/renderType0，accept-language zh，SUP_HUNYUAN_PUBLICLIST.raw | code0,total11/list11全lang=zh；display邻接02/13→04/23，无03/02。publishedAt与display不能互换为first-public；不扩窗外正文，有限中文目录已读完。 |
| SRC-ZAI | [Research全部](https://www.zhipuai.cn/zh/research)SUP_ZAI.raw时间排序，邻接02/21→03/15 | 该段无03/02条目，不点击更多扩旧年。 |
| SRC-BYTEDANCE-SEED | [Research](https://seed.bytedance.com/en/research)SUP_SEED.raw出版邻接Jan27→Apr11；[papers](https://seed.bytedance.com/en/public_papers)SUP_SEED-PAPERS.raw首20/242,Page1/13,到May14 | Research有限段无03/02；papers动态目标历史cursor未恢复，242库存不作AB队列。 |
| SRC-BAIDU-ERNIE | [Blog](https://ernie.baidu.com/blog/zh/)SUP_ERNIE.raw首页，邻接Feb06→Apr15 | 已读目标邻接段，无03/02，首页目标段已足，不翻更早页。 |
| SRC-XIAOMI-MIMO | [Paper/Blog](https://mimo.xiaomi.com/)SUP_MIMO.raw Paper8条Jan08→Feb03→Mar13及Blog15条标题 | Paper目标段无03/02；Blog无日期且末尾More，不能当完成历史段，保留具体cursor限制，不把15条窗外标题变成全文队列。 |
| SRC-MINIMAX | [Research Blog](https://www.minimax.io/blog)SUP_MINIMAX.raw完整可见12条至2025Oct27，邻接Feb14→Mar18 | 目标段无03/02，有限目录已读完，不扩商业News。 |
| SRC-ARXIV | 四主题查询与同义补检（下列）；[cs March1–50](https://arxiv.org/list/cs/2026-03?skip=0&show=50)SUP_ARXIV-MAR.raw只浏览相关标题；18新exact-v1完整题摘、旧3有效题摘复用且当前页轻量标记 | March membership不是公开日；18新最终分16潜力/2贡献关闭，旧3必要公开日仍缺；四有争议关闭一次core后两项撤销EX，止于准入决定，不用Submitted/updated/ID替代date，不读全文绕date。 |

实际主题检索第一轮4个query：`site:arxiv.org "March 2 2026" ("language model" OR Transformer OR MoE OR "reinforcement learning")`；同日期加`(multimodal OR "world model" OR "vision-language-action")`；同日期`(LLM OR GPU) (kernel OR compiler OR parallel OR memory OR serving)`；同日期`(agent OR retrieval OR tool) (language OR LLM)`。web返回Empty search results，不是本日零命中。一次同义补检为`site:arxiv.org <LLM training MoE / multimodal world model VLA / GPU parallel kernel serving / agent retrieval tool memory> "2026-03-02"`，唯一可见返回OntoPlan2610.07649（Oct06，窗外）；不扩全文。主题覆盖cs.CL/LG/DC/AI及CV/RO、AR/PL/OS/PF、IR/MA约定主线，搜索局限明确保留；没有十二分类穷尽声明。

机构有界辅助查询为：`site:openai.com OR site:deploymentsafety.openai.com "March 2, 2026" research model safety`、`site:ai.meta.com "March 2" "2026" research`、`site:research.google OR site:deepmind.google "March 2" "2026" model`、`site:seed.bytedance.com OR site:qwen.ai OR site:mimo.xiaomi.com "2026-03-02"`；第二组为`site:anthropic.com/research "March 2, 2026"`、DeepSeek官方域同日、Kimi/Moonshot同日research、混元/ZAI/MiniMax/ERNIE官方域同日。可见线索GPT/DoW和窗外/非研究社区帖，其余无可采用新线索；只负责发现、不证明覆盖。Qwen/混元动态入口通过已有官方证据/API完成相应有限恢复，其余缺必要历史段精确隔离。

## 二、新完整题摘与准入链

以下每项精确v1完整题摘原件为`SUP_ABS_<ID>.raw`。本次仅能核Submitted/版本提交史，不能确认03/02first-public，因此潜力不评分、不算候选/Evidence完成、不进Books。不因为局部/负面/理论或小模型而排除。原3日期潜力不重复全文投入。18新和旧3当前官方页未见withdrawn/deleted/erratum公告；不等于核完整版本史。

| ID / 简称 | 具体增量与本项目判断 |
| --- | --- |
| 2603.00024 Personalization | personalization对affective/epistemic alignment作用不同且role调方向，token/demographic控制信号修正同一种sycophancy评分；潜力。 |
| 2603.00025 TAB-PO | 近相同偏好与semantic token稀疏导致margin/gradient稀释→token参考优势+conditional barrier→结构化token-critical preference目标；潜力，不因医疗样本排其通用优化命题。 |
| 2603.00029 Anisotropy | massive dimensions由须抑制outlier变domain-critical detector→幅值识别/局部steering→全维steering替代边界；潜力，相关不自动因果。 |
| 2603.00031 GRIP | global/local选样割裂→RAP cluster deficit预算+length-rectified prior→长尾数据配比选择；潜力，3×宣传未证。 |
| 2603.00039 CARE | 多judge共享混杂→显式quality/confounder潜变量及identifiability条件→不能盲投票；理论/局部潜力。 |
| 2603.00042 LittleBit2 | heavy-tail low-rank binary潜力被spiky latent损失→rotation+Joint-ITQ→低比特几何前置；潜力，zero-overhead未核。 |
| 2603.00045 CoDD | parallel factorization barrier→tractable联合概率层→并行token依赖/质量成本边界；潜力。 |
| 2603.00048 MOSAIC | 单MFT未充分测伦理行为→多维问卷/游戏对照的不足信号→construct coverage需验证；潜力而非新增库存自动采用。 |
| 2603.00049 BiJEPA | 单向latent预测→双向cycle和norm控制爆炸→对称表示稳定性替代；潜力，toy只限定范围。 |
| 2603.00054 ExpertDivergence | MoE专家同质→domain-label JSD路由目标→specialization预训练选择；潜力。 |
| 2603.00061 PII fine-tune | benign domain SFT仍破拒答→NoPII/PII/role-swapping控制及泄漏→安全/隐私验收须双侧；负面潜力。 |
| 2603.00063 Dispositions | benchmark observable score不等稳定disposition→独立操作context变量及counterfactual映射→construct解释边界；概念/理论潜力，未证普遍失效。 |
| 2603.00070 CertaintyValidity | discrete {-W,0,+W}架构下ambiguity/CI迁移→certainty×validity分账与局部停止边界→confidence不被accuracy遮蔽；潜力，不采83%为普遍常数。 |
| 2603.00059 Synthetic surveys | 多模型synthetic population一致偏离真人反常识关系→simulated-user相合不等真实人口→模拟evaluation外推边界；负面潜力，社会样本非普遍定律。 |
| 2603.00016 AR robot teaching | 36人只测baseline AR human培训；LLM multi-agent是future integration提案，没新执行/安全/可靠性机制或实际验证。明确范围/贡献关闭。 |
| 2603.00021 Graph docs | 既有sliding-window/GAT在文档classification/summarization的任务表示应用，未指向foundation学习/生成/系统的新边界；范围关闭，不否认领域价值。 |
| 2603.00051 LitBench | 原题摘初判库存式EX；一次core§3.2–3.3式2给三层LLM生成concept平均embedding替代title/abstract召回，修正原未见新检索表示的判断，撤销EX→潜力/date隔离，不采领域score外推。 |
| 2603.00058 PaperRepro | 原execution/evaluation分工成熟workflow命题不准入；一次core§5.1.1给112实例审计中13错项、unsupported package item/report越specified范围/label错误三类，新增评价反证，撤销整家族EX→窄潜力/date隔离；不采工作流自动保证。 |

## 三、日期与必要证据恢复

旧ActMem2603.00026、SimpleTool2603.00030、Attn-QAT2603.00040只复用有效完整题摘；本轮SUP_CURRENT三页轻量无撤回/纠错信号。本窗必要first-public仍无：月页仅March、abs仅Submitted，不能给本轮零命中。不得套旧09:00或DataCite登记。18新页同样已一次有界date恢复停止；16潜力和上述旧3共19身份请求一次精确ID的官方首公告列表/订阅邮件或作者带日期公开原文，非时分秒。取得后只核03/02归属与版本，再必要审阅；不全月重扫。2明确EX无影响处置的date请求。

Gemini Flash-Lite官方March3明确在补充窗外，旧时区请求只冻结为旧范围历史，不作为本轮恢复条件。GPT HTML明确March2，PDF封面March3与RSS正式blog日不同，不否决HTML日级事件；本轮不补造instant，区别HTML safety与后续发布。

## 四、正式候选必要审阅与Books建议

GPT safety HTML官方当前原文§2将评估subject注明2/26 shipped revision，比较值是旧模型当时latest版本，不拿此前card不同版本数值直接比较。§3.1说明hard production-derived population故error rate不是平均真实流量；dynamic mental-health/self-harm/emotional reliance模拟下一轮依模型回应，而非固定历史只验末答。采用not_unsafe明确消息分母，不把“any assistant response”描述自行换算为conversation安全概率。厂商称self-harm/sexual内容相对5.2回退，graphic violence/violent illicit回退低统计显著；线上未见self-harm增加不抵消离线反证，系统guardrail是厂商缓解意图，不是效果证明。生成器、样本量、judge详细实现/硬件/批量/并发/SLO为Not Disclosed；本命题非推理性能，不引用HealthBench领域指标。安全实际评价变化按6分深入受影响内容，未复现、未核实现。

已读Books权威上下文、Ch66开头/邻接Ch65与Ch67交接、Ch66现行551–558 trajectory/history、2679–2681 response-conditioned模拟、3278–3292 offline-online关系。已有内容承载轨迹/干预/数据分布及阶段不替代，却未明确末答vs消息比例vs整段事件分母。因此建议唯一owner PLATFORM-EVALUATION-SYSTEM，在原逐条/整段轨迹段后一段短补；root负责协调实际写入与非写入者POST，作者不修改Books。第一批准入已由root实际§3.1独读通过。

DoW Mar02更新只采用官方L20–30的新增合同边界，Feb28原控制栈家族已有有效03-01仅报告审阅且明确排除该新段；本次重要修订不重复评分。commercially acquired PII明确被纳domestic surveillance禁用叙述、NSA等服务需新agreement，是公开许可事实，未披露系统如何识别/执行/检验这些约束。与Ch72原信任/控制/验证分工没有新可迁移机制，最终仅报告，不采官方“不能发生”安全保证、不作法律合规判断、不新改Books。root准入/必要证据及日级复核通过。

## 五、独立复核与验证

四有争议EX的原件是`SUP_CORE_<ID>.raw`。00016实际§2.3–2.4限定尚未实施的pedagogical架构；00021实际§3.1–3.2是文档GAT的SWA替换/既有过滤程序，非foundation组件新机制。00051与00058上述core导致撤销整家族EX；保留原判与改判依据，16潜力/2EX由root继续校准，不把下载算全文完成。

root已实际核GPT官方§2/3.1、DoW L20–30及分隔线和受影响FAQ，准入/必要证据通过。root写Ch66两段及自身末注后，作者以非Books写入者实读实际551–555及完整邻接（旧2602.22775模拟段→新两段→history干预/Registry交接）和Review notes首bullet，实际POST PASS；消息/末答/整段分母、模拟与固定共存、困难人口/offline-online及subject版本均准确，无性能或真实安全保证。未改Books，只记录实际结果。

root已实际读新18完整题摘，16潜力/2EX准入校准通过；又核00051§3.3式2与00058§5.1.1三个错标owner支持撤销EX，00016§2.3–2.4及00021文档SWA应用EX通过。不把四core下载或准入校准称18篇全文审阅。

本日V3结构/一致性及本地引用通过，限定README/本目录unstaged及cached diff-check通过；原窗口相等、原0候选冻结新增2、原§4连续前缀保持。旧来源覆盖表原件在baseline，正式§2仅当前14行，避免机器/读者混合旧新分母。

最终root非报告作者全部六部分DAY PASS：实际十四有限source表/原件停止（含RSS1257无Mar02item只限feed、混元zh11/11）、全部18新AB、四决定core与改判16潜力/2EX、19必要公开日隔离，两确定事件日期/受影响证据及Ch66实际两段/邻接/末注/非writerPOST，原0/window/连续§4均核。未核宽库存全量、隐藏历史，不授全Coverage/Evidence或无遗漏。仅本日完成、普通待办0，不领他日，不改索引或State；未stage/commit/push。
