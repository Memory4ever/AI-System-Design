# Daily Research — 2025-12-08

**规范：** V3
**窗口：** 2025-12-07T09:00:00+08:00 ～ 2025-12-08T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-02T20:38:20+08:00

## 1. 结论

14每日源按本日原始邻接独立有界处理，0个已证明完全落窗的家族，不表示零事件。按Mill实际原文差额撤回00602/04988/06645的关闭，15个arXiv潜在家族与GLM-4.6V/AutoGLM共17个具名保留项，15项完整题摘/必要核心后贡献前关闭；另有明确窗外版本下界。BSFA的全QK后省value work、DAG-Shapley的条件缓存复用、SRPG的重建泄漏边界及新增三项窄反证均保留，不照录性能/安全保证。作者重开归并和正式同步已做，普通待办0，已由Mill独立局部核验并完成日级验收，结果见§6；公开日期、历史目录及精确release缺口安全隔离，不授其准入/Evidence/Books，也不以隔离本身授日级通过。没有共享Books改动或整合完成声明。

## 2. 来源覆盖

实际查询、分页/邻接、逐项处置与必要核心见[本日原始记录](../_sources/daily-20251208/WINDOW_REVIEW.md)。固定历史目录复用原始字段，不从前日报结论套完成。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 本轮RSS403；原始1243项相邻Dec4 19GMT/Dec8 00、04、06GMT；正确Virgin官方访谈核心 | 已检查 | 本窗相交的企业采用访谈贡献前关闭，不授全站召回 |
| SRC-ANTHROPIC | 原始publicationList Dec4 17Z/Dec18邻接 | 已检查 | 不宣称冻结历史或全机构无遗漏 |
| SRC-GOOGLE-AI | 原始2025Blog第1页Dec4/Dec10、DeepMind第3页Dec3/Nov21 | 已检查 | 只声明目录主题范围 |
| SRC-META-AI | 原始第4页Dec12/Dec1/Nov19至Nov10 | 已检查 | 收录不授首次公开 |
| SRC-QWEN | 旧Sep23/新站空及部署/README有限替代 | 受阻 | 2025旧目录隔离 |
| SRC-DEEPSEEK | 正确API Docs Dec1/2026 release邻接 | 已检查 | 错误news重定向不恢复历史正文 |
| SRC-MOONSHOT | 原始26项Overview Nov7及Nov6 changelog | 已检查 | 不扩日常仓库提交 |
| SRC-TENCENT-HUNYUAN | Research失败、All API11项全2026 | 受阻 | 2025旧Research隔离 |
| SRC-ZAI | 原始All两页15/18项至Dec7/8；本轮对象144/145、官方card/AutoGLM Blog及README | 受阻 | 午夜式日编码/迁移字段不授上线，当前artifact非2025冻结 |
| SRC-BYTEDANCE-SEED | 原始2025paper首20至Dec2/Oct22、Blog首20至Dec2/Nov27，前界Dec15/16 | 已检查 | 限该入口邻接，PublishDate日编码不补时刻 |
| SRC-BAIDU-ERNIE | 原始第2/2页至Nov7、Nov21/Dec9邻接 | 已检查 | 无全机构零事件保证 |
| SRC-XIAOMI-MIMO | 原始Paper8项、Blog15项与HSS/Safety部署路由 | 受阻 | 无date/旧More历史缺口隔离 |
| SRC-MINIMAX | 原始英中13项Oct27/Dec23邻接 | 已检查 | 无具名触发，不扩Tech Blog |
| SRC-ARXIV | 四组Dec7主线主题查询、cs.OS首段23标题/cs.MA首25标题及具名v1 | 受阻 | 月身份/提交不授first-public，个体日精度隔离 |

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |

尚无可列为确定落窗的家族；潜在项置§5，不伪造时刻、评分或Evidence完成。

## 4. 证据与知识整合

[本日原始记录](../_sources/daily-20251208/WINDOW_REVIEW.md)保留BSFA Algorithm1及Table1、SRPG双流融合、HiveMind coalition剪枝/functional determinism的必要核心与关键反证。全文片段已读不等于当日准入或证据验收。GLM native visual tool payload与AutoGLM开放device adapter/data backend分工保留为release机制线索；当前README版本不能反填历史隐私/权限。

本轮只复用[Mill实际精确v1局部阅读](../_sources/daily-20251208/ROOT_ADMISSION_REVIEW.md#负侧分层与精确普通差额)，不重复有效全源或冒称作者新增全文审阅：[AgentODRL00602](https://arxiv.org/html/2512.00602v1) workflow/Table2的orchestrator语义得分80.22低于固定Splitter84.02/Rewriter88.07，但tokens46.2M低于47.9M/49.5M，提供路由质量/成本取舍；SHACL只校syntax，不授authorization，LLM Jury不授真实intent。[04988](https://arxiv.org/html/2512.04988v1) Appendix I及共同实验条件中LLama平均低于fixed-policy baseline，环境skill training虽非模型更新，仍是模型能力/reward评价负侧；不授同token预算、因果或现实经济结论。[06645](https://arxiv.org/html/2512.06645v1) IV-b/c及V中降低traffic demand在部分60/80%RV配置反增碰撞，取消左转在4S+10U总体反增，保留MARL controller干预反证；14intersection/single-direction模拟不授现实通用安全。三项均重开为窄potential，未取得first-public，不进入确定集合、评分或Books采用。

Books暂缓：实际对读`INFER-PREFILL` [Ch43](../../../../books/part-05-inference-system/43-prefill.md)约62–155行与Ch42/44交接，已有approximate discovery/selection/fallback，但不是“exact QK后省PV”分支的具体覆盖。日期恢复后可在dense FA/discovery交接处补局部草案：保留全QK只减少value/softmax work，仍改变dense归一化语义；校准target k不等于固定执行预算，需结算QK/selection及质量回退。精确原始证据/owner/条件草案已给主线程，不冒称整合完成。

## 5. 缺口与下一步

作者三项重开归并及集合同步已做，普通可执行项0，已由Mill独立局部核验通过，日级结果见§6。VLCs04320、AgentNet++00614、BiRouter00740、SocialDriveGen01363、DMAS02410、Network Sheaves03248、AsymPuzl03466、SRPG03694、SEMI-CTDE04653、DSCP05447、HiveMind06432、BSFA07011、新增AgentODRL00602/劳动市场04988/碰撞分析06645以及GLM-4.6V/AutoGLM共17个潜在家族均为本窗终态保留项，贡献前关闭集合15项：不用于正面证据、不进入 Books、不支撑无遗漏或性能/安全保证。每项原始链接、具体增量、限制和停止范围在[原始记录](../_sources/daily-20251208/WINDOW_REVIEW.md)；隔离不计Coverage/Evidence通过，也不是零事件。

必要恢复只请求一次：精确v1历史new公告/RSS/email或可核首次正文；Z.ai原始上线时刻/完全落窗区间及当时card/adapter/confirmation协议；Qwen/Hunyuan/Z.ai/MiMo的2025原始目录邻接。材料到达只重开该家族真实归属日与拟采用命题，不全月扩扫。未来提交下界9项另留身份，不属于本窗，不要求本窗深审。

## 6. 复核

复核者：Mill，agent ID `01a0fc18-6d14-7b60-9ba1-b6b579aaef3e`；非作者Gibbs，非Books写入者root。

结论：通过

实际重读本日适用AGENTS、研究/Report合同、每日源分组、Prompt、ROADMAP与相关路由state，只加载本窗README/WINDOW_REVIEW及定点原始身份。14源原始分页、邻接与有限停点逐项核；不宣称本轮重新访问全部14站。固定历史目录复用有效原始字段与我此前同身份实访记录，不复用别日报完成结论。独立原生取得cs.OS首23标题/总23、cs.MA首25标题/总211；未翻后页。确定落窗分母0，不是零事件或完整召回。

全部12个arXiv potential精确v1完整题摘独立读取，GLM-4.6V复用07同身份官方card/对象144有效实核，AutoGLM独立读取对象145字段、原Blog与当前官方README。重点实际读BSFA §4/Algorithm1及§5/Table1、SRPG IV-B1–3/V、AgentNet++ §3.1–3.5/4.2/5.2/6、DMAS IV/V、HiveMind剪枝及functional determinism：exact QK不授dense Attention；target k不授固定density；重建接触原始X、prompt不授隐私隔离；composition援引不补知识敏感度/secure aggregation协议；密码身份不授内容正确；temp0不授全部功能确定性。AutoGLM的device执行、推理backend、确认/人工接管须分责，当前Harmony/iOS与迁移字段不反填2025 frozen release。无runtime测试或复现。

负侧实际读取17个arXiv关闭项完整题摘和正确Virgin官方访谈；05983原站重叠信号与2506.06837v1完整题摘核去重，不当withdrawal。安全/含糊关闭必要核心定点读00520/00602/01610/02682/03180/04988/06645 HTML，02561 HTML404后读精确v1 PDF §2.3/3/4。普通负侧按OS运行时、存储、compiler、科学输出与金融应用分层；不全量全文或扩大两首段库存。01610确有Controller/白名单/PodManager分责，不以“无控制”关闭；其未给新受控权限/一致性failure，窄组合关闭仍可保留。EZYer只有LLM评分和未来人工评估限制，未见新受控反例，亦不授质量保证。

已实际定点核作者修复：00602路由质量/token成本对照、04988 Appendix I的LLama低于fixed-policy负侧、06645 IV-b/c与V的安全干预反向结果均撤回原关闭、归并窄potential；WINDOW_REVIEW与正式§1/4/5的集合、普通计数及终态限制同步一致。复用本身份上轮已实际取得的精确v1核心，不重复未变来源。普通差额0；15个arXiv加GLM/AutoGLM共17个潜在家族、15项关闭，确定落窗分母仍0，三重开不增加Evidence。准确原始位置与历史差额见[本日实际复核](../_sources/daily-20251208/ROOT_ADMISSION_REVIEW.md)。

新增条件Books proposal仅BSFA：实际对读唯一INFER-PREFILL Ch43 Sparse Prefill/Dense FA→discovery，及Ch42 phase/SLO、Ch44 Decode依赖；全QK后舍value/normalizer是具体分支缺口，不是主题相近覆盖。日期未授，不正面写Books，不授整合完成。外部终态保持具名恢复及真实日重开，不计Coverage/Evidence或无遗漏。日级语义通过，完成态V3及链接检查结果另记于本日复核，不替代实际语义；未改共享Books/state，未stage/commit/push。
