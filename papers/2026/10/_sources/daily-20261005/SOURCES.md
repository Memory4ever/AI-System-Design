# 2026-10-05：真实入口、有限停止与隔离

窗口 `[2026-10-04T09:00:00+08:00, 2026-10-05T09:00:00+08:00)`。本日独立执行；截至2026-10-05T16:05:00+08:00的当前入口检查，未扫描每周组或遍历机构历年论文。表中“窗外”只针对实际日期段，不证明互联网上无遗漏。正文/目录访问失败与未做完的证据工作分开。

| ID | 实际入口与停止依据 | 结果与限制 |
| --- | --- | --- |
| SRC-OPENAI | Research当前页由web reader成功实际读；native403另存openai.json。最新Research卡片9/29，当前首屏至9/03，均早于本窗。 | 有限当前研究页已检查；不把native403当0，不重扫全年。 |
| SRC-ANTHROPIC | 官方Research当前首10项完整列表，最新10/01，随后日期已早于窗口；anthropic.json保留。 | 已检查该有界日期段，无本窗相关卡片。 |
| SRC-GOOGLE-AI | DeepMind Research当前news与Publications第一页（30/265、1/9页），最新publication9/16；GoogleResearch Blog第1/135页12条，最新10/02。GoogleResearch pubs第1页1–15/11587为year排序2027/2026，不是首次公开排序；定点ETA原链接2609.20888 history/v2为9月窗外，PLD完整AB仅teacher reasoning patterns置systemprompt与场景数字，无新受控机制/反证。deepmind/publications/google-blog/google-pubs/google-eta-date snapshots。 | 日期明确的当前news/blog段已检查；年度pubs不作为本窗全覆盖或零命中证明。有限窗口/主题搜索没有结果，仅辅助检索，不能补成全年完整性。 |
| SRC-META-AI | Research首查reader0行；官方Blog当前第1页10卡片及LatestNews，latest7/27。Publications实际点击失败；meta-blog.json保留。 | 当前Blog切片已检查；Research/Publications目录受阻，无法支持完整研究目录覆盖，隔离为保留项。 |
| SRC-QWEN | 原qwenlm.github.io指新blog qwen.ai，实际/blog及/research reader空/native仅4字符Qwen壳；IAB Research一次30秒timeout/kernel reset。官方org当前10/59 repo有限替代，10/05两项qwen-code/D2K，余条最晚10/03。D2K README→2610.03226完整AB，按arXiv家族处理；qwen-code current nightly一页、2个有精确日期的纠错/权限PR核心定点跟读（13064/13069），首公开9/29、merge9/30；12987仅保留发现线索不作精确定窗，nightly汇总不增加新修复贡献。GitHub API必要metadata403rate-limit，不伪时区。 | Research动态目录隔离；官方替代只支持所读repo/current事件，不声称替代59项目全量。D2K由Mon5Oct current new/v1定窗，非repo Updated日期。 |
| SRC-DEEPSEEK | 官网当前V4.1Flash banner→官方API ChangeLog；web timeout后native成功取得完整16068字符，最新2026-09-10，随后8/21等已早于本窗；deepseek-updates.json。 | 已检查有序current ChangeLog日期段，访问已恢复。 |
| SRC-MOONSHOT | PlatformBlog原查web失败、native恢复；当前Blog最新2025。官方org当前10/42按Updated降序完整slice，最新kimi-code10/02；moonshot-org.json。 | 已检查两个实际current切片；repo Updated只发现信号，不作为首次公开或研究目录完整性。 |
| SRC-TENCENT-HUNYUAN | Research首查reader0行；root实际IAB隐藏tab30秒timeout/kernel reset（未看到列表）。官方org当前10/83有限替代：UniRL Updated10/05，其README News最新6月三算法；其余当前repo最晚9/25。定窗commit API403rate-limit。hunyuan.json与hunyuan-commit-window.json。 | Research“全部”动态目录未提取，明确隔离；UniRL Updated10/05身份/事件不能精确定窗，不支持本窗候选或零命中，无限commit遍历未做。 |
| SRC-ZAI | 首查官方Research reader/native timeout，后一次定点reader仍timeout；已存在浏览器创建故障，无成功目录UI。官方release-notes当前完整段最新8/26；org当前10/53按Updated降序，latest GLM-V10/02；zai.json/zai-org.json。 | Research目录受阻隔离；release/repo有限替代已检查，不能写全部Research无命中。 |
| SRC-BYTEDANCE-SEED | 官方public_papers第1/13页20/242项、latest8/18，Blog当前latest8/05；seed/seedblog.json有实际日期。 | 已检查有序当前日期段，停止窗外，不翻13页或把242项当本窗材料。 |
| SRC-BAIDU-ERNIE | 技术Blog第1/2页当前段latest5/09，ernie.json。 | 当前日期段已检查，窗外即停。 |
| SRC-XIAOMI-MIMO | Homepage全部8 Paper日期latest6/29；当前Blog 15标题/核心描述无日期，More未展开。通过官网已公开route metadata定位顶项Tool-CallRepetition官方URL，实际条目明示2026-09-27，窗外；mimo-route-dates.json、mimo-repetition-date.json保留。 | Paper日期段与当前顶项日期已检查；其余无日期Blog切片不支持零命中或全目录覆盖，不纳候选/Books，恢复需要具体官方条目日期或可用目录UI。 |
| SRC-MINIMAX | 英文Blog当前12、中文13（原minimaxi跳minimax.cn）、AgentTechBlog当前完整页，latest分别8/13、8/13、5/13；minimax/minimaxcn/minimaxagent.json。 | 三实际当前有序日期段已检查，停止窗外。 |
| SRC-ARXIV | 官方cs.CL/new Mon5Oct new63+cross50（113公告项，含replacement总185）与cs.DC/new新16作为主线有界完整题摘段；CL两个包共36完整AB，DC16完整AB。LG/CV完整title目录及AI/RO/AR/PL/OS/PF/IR/MA按attention/KV/inference/training/learning/reasoning/agent/memory/multimodal/world/VLA路由的当前title slice只作查漏线索，不作所有分类逐项队列。官方API主题日期发现query max100/start0有限20秒timeout；submittedDate只补发现，不定公开窗口。实际读题摘及判断由ADMISSION维护；D2K为官方Qwen repo触发并在currentLG新列表定点核。 | 实际有界主题发现及题摘筛选持续收口；宽title库存既不算候选也不称全量AB，API辅助检索受限，不支持任意新分类无遗漏。只审当前窗口具有具体增量的家族，不扫旧Weekly。 |

arXiv日期依据：[availability](https://info.arxiv.org/help/availability.html)明示Thursday14:00至Friday14:00 Eastern的一批在Sunday20:00公告；2026-10-04 Sunday20:00 EDT为2026-10-05T08:00:00+08:00，落本窗。当前Mon5Oct new分组、每篇精确v1/history与轻量撤回/纠错说明共同核身份；Submitted值不是公开时刻。当前完整AB无相应撤回/纠错标记的项不为证明absence而遍历全历史。

外部保留项均不作为正面Evidence、Books或“来源无遗漏”依据。动态目录恢复条件为可读官方列表/有限窗口导出或可用浏览器；Hunyuan UniRL、MiMo其余未定日Blog还需精确事件身份及公开时间。以上表格是实际有限发现范围，不是全网完整性证明。后续普通准入消歧、38项必要证据/Books与独立复核已于2026-10-05T16:49:00+08:00结束并通过日级验收，最终状态见正式日报；不把外部隔离项改记为成功获取。
