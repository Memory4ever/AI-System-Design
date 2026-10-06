# Daily Research — 2025-12-28

**规范：** V3
**窗口：** 2025-12-27T09:00:00+08:00 ～ 2025-12-28T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-02T19:42:00+08:00

## 1. 结论

14每日源按本窗独立处理，普通作者待办0。确认落窗候选0，不是零事件结论。实际arXiv语言/系统52项与Agent30项提交身份查询无next，另多模态原始查询访问失败且有限替代未恢复；月身份库只作有界相关标题补检。FoldAct、RollArt、RL故障容错、MAI-UI、diffusion discreteness与安全反证等实际线索日期隔离，未降分删掉。

必要历史外部项不支持候选、Books或覆盖通过。21新增身份中20 potential、1方法核准后关闭；另2个既有身份定点复用。无本窗可采用的Books命题、无共享书稿修改；非作者复核通过，普通可执行待办0。

## 2. 来源覆盖

独立原始记录见[SCAN.md](../_sources/daily-20251228/SCAN.md)。以下均按12/27 09至12/28 09重读原始邻接；不复用别日结论。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [Research](https://openai.com/research/)原始2026首屏/403；12/27限定官方域替代查询 | 受阻 | 12/2709至12/2809历史日目录隔离，空搜索不作零 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research)十项2026/See More同页；另重读原始Alignment Blog Dec19 Bloom/Oracles→Dec16→Dec12→Dec8→November，比较12/2709至12/2809 | 受阻 | Alignment历史切片已检查撤销该部分隔离；Research主目录缺口保留，不互相替代 |
| SRC-GOOGLE-AI | [DeepMind Blog正确page4](https://deepmind.google/blog/page/4/)原始24条Feb26至Nov25，December模型/研究字段最新Gemma Scope2 Dec19T12Z；[Research Blog2025](https://research.google/blog/2025/)Dec18→15→Nov12，比较12/2709至12/2809 | 受阻 | 两Blog历史段已检查撤销该部分隔离；publications首公开仍缺，?page=4无效不复用 |
| SRC-META-AI | [官方历史page3](https://ai.meta.com/results/?content_types%5B0%5D=publication&page=3)1/02、12/26 AdvGame、12/18、12/16，page4/Blog2邻接重读 | 已检查 | 12/26无时区精确范围不可移成本窗；潜在日期隔离 |
| SRC-QWEN | [Blog](https://qwen.ai/blog)迁移/动态空/公开组件边界原始记录，12/27限定官方日期替代 | 受阻 | 本窗完整历史目录隔离，不从旧2511复制候选 |
| SRC-DEEPSEEK | [updates](https://api-docs.deepseek.com/updates)原始12/01 V3.2与2026-04-24 V4之间，重新比本窗12/27至28 | 已检查 | 只该目录邻接，无全站零断言 |
| SRC-MOONSHOT | [Blog](https://platform.kimi.com/blog)原始26项至11/07；CLI Dec24 0.68→Dec29 0.69，比较12/27至28 | 已检查 | 本窗位于这两个目录日期之间；不沿用0.68审阅数 |
| SRC-TENCENT-HUNYUAN | [Research](https://hunyuan.tencent.com/research)原始all列表11/11全2026/最早02-03与有限浏览器恢复，12/27官方检索 | 受阻 | 本窗历史不在当前目录，隔离 |
| SRC-ZAI | [Research第二页](https://www.zhipuai.cn/zh/research?page=2)累计18条无更多，Dec21 GLM4.7→Dec10/09/08/07；[release](https://docs.z.ai/release-notes/new-released)Dec22→Jan14，比较12/2709至12/2809 | 已检查 | 修正Research漏页，发布/论文日期仍分开 |
| SRC-BYTEDANCE-SEED | [论文/Blog原始API](https://seed.bytedance.com/en/public_papers)type1实际18,total94,next20，两置顶12/15、12/02后10/21至6/25；type2采用root本次HTTP200实际18,total45,next20，五置顶12/24→18→16→02→11/27及后段至6/25；独立比较12/2709至12/2809 | 已检查 | 不沿用Nash15/49旧数、不把混合置顶当全局排序；两类型分开，目录日编码不授精确上线/arXiv公告 |
| SRC-BAIDU-ERNIE | [Blog](https://ernie.baidu.com/blog/zh/)原始2页，第一页1/08→12/23→12/09；本窗12/27至28在相邻段中 | 已检查 | 仅目录段，不把排名旧事件改归本窗 |
| SRC-XIAOMI-MIMO | [Paper/Blog](https://mimo.xiaomi.com/)原始Paper八项1/08至10/21；Blog15项无日期及有限路由恢复，重比本窗 | 受阻 | Paper段可查；Blog12/27至28历史隔离 |
| SRC-MINIMAX | [英文](https://www.minimax.io/blog)/[中文](https://www.minimax.cn/blog)原始12/13项1/27或28→12/23→10/27；[Agent](https://agent.minimax.io/docs/techblog.md)一项2026-05-13 | 已检查 | 本窗在两Blog邻接之间，Agent历史不作完整保证 |
| SRC-ARXIV | 官方三主题组submitted12/26至12/28，52/超时/30；多模态官方域有限替代；[cs.CL](https://arxiv.org/list/cs.CL/2025-12?show=2000&skip=0)763至785相关标题 | 受阻 | 必要原始日公告/多模态历史与实际相关ID首公开隔离；月身份不是日覆盖 |

## 3. 候选与判断

无确认落窗的候选。身份线索未作贡献前关闭；只有标题明确的领域应用范围负侧停止，不按关键词决定贡献。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |

## 4. 证据与知识整合

已定点补齐[21项新增身份准入判断](../_sources/daily-20251228/ADMISSION.md)：20 potential、1方法核准后范围关闭；SWE-RM/SmartSnap另定点复用同身份题摘。CoAgent经exact v1 §6.3/7.3/8.2重开watermark评价混杂与稀疏verifier漏物理事件；VULCAN经§4/6.4/9.3重开adaptive backtracking及近似collision solver可靠性边界。BioSelectTune经§3.2/4.4重开高IFD筛选遗漏负例的设计反证；Tree-Transformer经§III-B–D/IV核清单root投影加局部坐标的功率回归边界后关闭，不再用领域标签。原摘要/标题关闭理由撤销；不采用性能或安全保证、不称全文审阅完成。所有potential保留日期请求，不评分、不采用Books；已发现题摘及上述准入差额普通待办0。

相关机制/反证身份均保留SCAN：例如[RL角色故障容错](https://arxiv.org/abs/2512.22492)、[RollArt](https://arxiv.org/abs/2512.22560)、[FoldAct](https://arxiv.org/abs/2512.22733)、[CoT faithfulness](https://arxiv.org/abs/2512.22631)。这些标题或题摘入口只支持提出必要日期恢复问题，不支持模型/系统收益、安全或已完成正文审阅。

无本窗可采用Books命题，不声称“已有覆盖”；未知日期不是“仅报告”理由。恢复日期后按贡献审阅与owner实际段落/相邻比较，再交root协调，不能借目录已有主题提前关闭。

## 5. 缺口与下一步

恢复差额已同步：Seed type1/type2分别比较本窗；DeepMind正确Blog page4（最新December年度回顾12/23为既有事件回顾）及GoogleResearch2025 Blog、AnthropicAlignment已读邻接不再隔离。仍隔离的Google部分仅publications必要首公开，Anthropic部分仅Research主目录；不将Blog检查扩大为全源通过。采用root最新原始type2 18/45，而非旧15/49。

普通可执行待办0；独立核验通过。本窗终态保留项为机构历史日目录、MiMo Blog、多模态窗口查询访问及SCAN所有实际相关ID首公开。有限原始/搜索/分类列表替代仍不能完全归窗；不评分、不采用、不进Books，不支持正面证据、Books或无遗漏断言，也不支持性能/安全或Coverage/Evidence通过。重开条件：对应源历史原始分页或逐ID官方new批次、可验证且完全落窗的作者首次公开范围到达后，只重开该源/ID。

Jan前缀datehold材料不以Submitted December移回；Christmas公告批次若实际12/28 20EST，位于12/29北京09而非本窗，不从排期赋给ID、不扩January。

## 6. 复核

复核者：主线程（独立于报告作者 Feynman）。
结论：通过

实际检查14源停止范围、全部potential日期隔离、12项exact v1完整题摘、CoAgent/VULCAN/BioSelectTune/Tree-Transformer必要正文及22529范围样本，纠正过早关闭与计数。没有无差别重读所有附件；具体检查与未检查范围见[非作者复核](../_sources/daily-20251228/ROOT_ADMISSION_REVIEW.md)。无Books写后待办，格式校验仅验证结构。
