# Daily Research — 2025-09-16

**规范：** V3
**窗口：** 2025-09-15T09:00:00+08:00 ～ 2025-09-16T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-06T19:01:26+08:00

## 1. 结论

非作者日级终核通过，本日已处理到安全终态。Codex release为本窗正式1家族，root准入5分、标准审阅与仅报告裁决均通过；system card单独事件在窗外，不合并datehold。arXiv 229 条是主题提交区间线索，不是本窗新论文数；78 个相关/含糊身份进入完整题摘发现阅读，8 项具体机制/负面/安全潜力经 root 首批校准，11101/11656及11524三项错误排除已窄重开。其公开归属仍未取得可靠的本窗证明，Google Learn Your Way亦保留具体潜力和日期缺口，不应解释为零事件。正式候选1、独立确认标准审阅完成1、Books写入0。

值得继续核验的方向是动态训练 offload、attention 选维、扩散缓存验证、GUI 注入、执行轨迹训练的负面结果、reranker 日期混杂、connector 信息损失与概念擦除理论保证。部分安全/反证内容已实际定点读精确 v1，但不构成本日正面证据。Books 没有写入或正面覆盖声明，保留项不得支持性能、安全或无遗漏保证；没有复现实验。

## 2. 来源覆盖

以下只声明实际有限切片；原请求、恢复与停止依据见[来源恢复](../_sources/daily-20250916/SOURCE_RECOVERY.md)。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 官方RSS单次HTTP200共1247身份，仅筛本窗UTC区间；Codex release完整核心经root单项独核，消费者使用研究关闭，card独立窗外 | 已检查 | 此保留RSS/具名核心切片可判归属；不授全站修订无遗漏，单项通过不授DAY |
| SRC-ANTHROPIC | Research Next JSON恢复172唯一publication，按本窗只取两篇Economic Index原publishedOn，读核心说明 | 已检查 | 本窗研究目录切片为经济采纳/地理估算，未显示模型/系统机制；不授全站覆盖 |
| SRC-GOOGLE-AI | Google Research `/blog/2025/09/`实际第1/2页，最早Sep11已越下界；Learn Your Way具名原Blog完整核心补检；Pubs/DeepMind Research入口与日期补检 | 受阻 | Learn Your Way原Sep16仅日期、时区/完全落窗未定；DeepMind及无日公开字段的Pubs历史切片未恢复，不能用当前页授完整覆盖 |
| SRC-META-AI | Research入口与Sep15官方CyberSOCEval完整题摘，16lastsources | 受阻 | 测试时计算收益跨任务不一致有负面潜力；原日期无时区/首次公开未定，不采用 |
| SRC-QWEN | 原保留Blog切片加新实际page_config研究列表HTTP200原60配置；仅筛本窗原date，0命中，Next Sep10T20Z至TTS Sep21T20Z夹窗 | 已检查 | 本日独立capture见qwen-config-recovery.raw；不授全站或所有修订无遗漏，不把60条当全文队列 |
| SRC-DEEPSEEK | 实际执行主站`/updates`HTTP404并保留；官方API文档`/updates/`HTTP200，实际读取Sep22→Aug21连续更新至越下界停止 | 已检查 | 仅保留Change Log切片，没有本窗条目；不授所有论文/修订/删除历史无遗漏 |
| SRC-MOONSHOT | 官方Blog日期序列与组织入口；Sep16折扣、Sep5 K2更新夹本窗 | 已检查 | 只声明Blog保留切片；计费发布未显示模型机制增量，不扩当前仓库 |
| SRC-TENCENT-HUNYUAN | Research壳、正确publicList POST实际9条、GitHub/T1有限补检；浏览器子线程拒绝/超时 | 受阻 | API最早为2026记录，历史“全部”未恢复；不冒称空历史列表 |
| SRC-ZAI | Research实际首页15条、真实page2累计18条/hasMorefalse；原client及release notes | 受阻 | Research保留记录最早2025Dec，不覆盖本窗；发布说明夹窗不能补论文目录 |
| SRC-BYTEDANCE-SEED | Blog type2/year2025实际15条/total49，非置顶跨Aug21至Jul14停止；论文页20/242；type1 US/CN重试 | 受阻 | Blog切片已越下界，论文API total94但无列表内容；不记0论文或已读94条 |
| SRC-BAIDU-ERNIE | 技术Blog真实page1/2，Sep12PLAS/Aug14FastDeploy越过本窗下界 | 已检查 | 有限保留Blog切片；不授仓库所有历史发布覆盖 |
| SRC-XIAOMI-MIMO | 官方Paper8行，Sep19Audio/Jun4VL夹本窗；实际官方client核Blog15预加载、初显8及More仅展开，见MIMO_MORE_CHECK | 已检查 | 仅该有限目录；Blog数组无日期，不授九月删除历史/其他发布无遗漏，未把More视为未读分页 |
| SRC-MINIMAX | 原US/GitHub/Agent入口加本日独立CN Blog恢复HTTP200；实际正文13条，Oct27→Jan15跨本窗下界，停止Jan15 | 已检查 | 仅CN保留Blog切片无窗内条目；原minimax-cn-recovery.raw，不授删除历史/仓库修订或无遗漏 |
| SRC-ARXIV | submittedDate主题查询229条；系统主题补查66条全重复；lastUpdatedDate主题查218条；CL月列表1–2000/2214有界标题查漏 | 受阻 | 没有本日真实公告/单篇原首发证明。日路径无效、直2509路线404、年份月份路线可取，均保留；提交/DOI注册不作首公开 |

未触发额外固定按需来源扫描；为具名材料打开原始证据不扩成机构/分类全站研究。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Introducing upgrades to Codex](https://openai.com/index/introducing-upgrades-to-codex/) | 2025-09-15T18:00:00+08:00 | 统一投入难兼顾短交互与长任务 → 本版本员工流量短/长生成token十分位投入变化方向相反 → 部署评价应分切片核预算与质量；2+2+1=5 | 标准完成 | 仅报告 |

arXiv日期未定发现不提前评分；这不表示本窗无贡献或无遗漏。Codex单项通过依据见[root独立记录](../_sources/daily-20250916/INDEPENDENT_CODEX_REVIEW.md)。

## 4. 证据与知识整合

[首批作者判断](../_sources/daily-20250916/FIRST_BATCH.md)和[root 独立校准](../_sources/daily-20250916/INDEPENDENT_CALIBRATION.md)保留角色差异；[78个题摘发现身份](../_sources/daily-20250916/DISCOVERY_SCREENING.md)不转成全文队列。以下为已经取得的必要反侧，均不作为本日采用链路：

- [GUI环境注入2509.11250v1](https://arxiv.org/html/2509.11250v1)：§3/§6.1区分白盒模型可见与小触发器上传权限，评价为目标action字符串ASR；§6.3跨家族LLaVA迁移为0，§6.4 LES对照数据量不同，§7仅本地隔离场景。不支持普遍黑盒生产攻击率。[实际阅读](../_sources/daily-20250916/16securitycore.json)。
- [概念擦除2509.12024v1](https://arxiv.org/html/2509.12024v1)：Theorem3.2依Bayes最优判别器；Lemma3.3从原分布独立性推任意prompt分布，尚缺条件独立性桥接；Theorem3.4理想最优判别/生成更新假设不能由有限训练达到chance准确率证明。作者标为需root定点核的理论争议，不采用“任意攻击保证”。[实际阅读](../_sources/daily-20250916/16securitycore.json)。
- [跨模态安全2509.12060v1](https://arxiv.org/html/2509.12060v1)：安全单模态组合不保证安全多模态；SRPO分支正负由最终答案函数分类，不是逐步因果正确标签。[实际定点阅读](../_sources/daily-20250916/16securitymore.json)。
- [NeuroStrike2509.11864v1](https://arxiv.org/html/2509.11864v1)：§IV-A攻击者可改神经元或使用近缘surrogate；§X-A剪除阈值变化与utility代价不能忽略；target-layer与全模型比例不可混用。不把攻击权限和损失隐去。[实际阅读](../_sources/daily-20250916/16securitymore.json)。
- [EmoBench2509.11101v1](https://arxiv.org/html/2509.11101v1)与[MALLM2509.11656v1](https://arxiv.org/html/2509.11656v1)：前者§4.2/§6.2的gated评价给局部感知/认知反证，不证因果；后者§4.2/Table1–3给格式/可见性/协议比较，部分证据来自早先Kaesberg研究；快共识不等于正确共识。已撤销样本/配置数量式关闭。[精确v1与结论](../_sources/daily-20250916/16reopencore.json)。

Books 拟增量暂无可授权写入项：缺公开归属的材料暂缓，不冒称这些材料的现有 owner 已完整对照或已覆盖；取得日期后按研究合同§6读实际论点和邻接，由root处理唯一owner及自然段落整合。

非作者终核另恢复[11524v1](https://arxiv.org/abs/2509.11524v1)具体潜力：L2D匹配测试/训练序列隐藏表示，在有限候选item推荐中绕过语言AR；题摘含局部速度/质量权衡，不因不能通用于语言解码而排除。仅日期保留，未评分或证成>10x。Google [Learn Your Way](https://research.google/blog/learn-your-way-reimagining-textbooks-with-generative-ai/)原核心显示统一个性化基底再派生多模态、专用教育图像微调及60学生局部对照；不把应用名/组件组合当排除理由，也不授通用模型正确性。原Sep16日标签不能证明完全落窗，保留在缺口。[实际原核心](../_sources/daily-20250916/LEARN_YOUR_WAY_CORE.json)。

### [Introducing upgrades to Codex](https://openai.com/index/introducing-upgrades-to-codex/)

采用2025-09-15发布核心，排除页面Sep23 API更新；[完整source/core/owner交接](../_sources/daily-20250916/CODEX_OWNER_HANDOFF.md)与[root单项独核](../_sources/daily-20250916/INDEPENDENT_CODEX_REVIEW.md)保留证据位置。短/长十分位按模型生成tokens（hidden reasoning与final output）排序，不是配对任务难度档，不能识别隐藏控制策略的独立因果。SWE-bench分母477→500不可拼接；长运行个例不是SLO，容器缓存局部中位收益不证明新算法。硬件、precision、batch/concurrency及controller/training细节Not Disclosed，未核CLI实现或复现。默认sandbox/network限制和人审建议不授生产安全。

root实际顺读`AGENT-WORKFLOW` Ch81的workflow–engine接口及long-running/external events、`AGENT-CONTEXT` Ch75的执行状态压缩约束后，裁决**仅报告，新增正文0**：发布是短/长投入的版本局部观察，没有新的预算控制、恢复协议或compaction正确性依据，不能插入Ch81长期机制。作者原自然段落建议不实施；这不是“已有覆盖”或撤销准入。正式5分标准完成保留；日级非作者复核复用此有效结论。

## 5. 缺口与下一步

**普通待办：** 无。以下为本窗终态保留项，均不支持正面证据、Books、无遗漏或性能/安全保证；不等于Coverage/Evidence通过。定点重开条件是取得对应原首发的完全落窗区间，或缺段来源官方九月归档及实际分页终点。

- arXiv具体发现身份/版本逐项在[发现表](../_sources/daily-20250916/DISCOVERY_SCREENING.md)；首批8项加11101/11656/11524为重点。缺本日官方公告或原始首发证明，不以submitted、APIpublished、DataCite注册替代。已尝试官方日路径、月列表、版本页和具名日期补检；可接受替代为原始作者发布/官方公告支持的完全落窗区间。到达后仅重开该家族日期、历史版本及必要证据，不重跑229条。
- Google Learn Your Way原Blog仅Sep16无时区，保留上述具体流水线/局部评价潜力；本次具名原Blog可读，另HTML路线未恢复可靠时刻。补得原公开字段/官方首发可完全落窗区间后，仅重开该家族日期与必要技术报告，不先泛化无命中或展开无关附件。
- Meta CyberSOCEval有Sep15官方日期与具体潜力，缺原始时区/可落窗区间及首次公开关系。原文在16lastsources；补得原首发后定点重开，不能机械要求秒级精度。Codex不再属于此日期保留项；Sep23 API更新与窗外card不冒作本窗新事件。
- DeepMind/Google Pubs、Hunyuan历史全部、Z.ai九月Research、Seed论文缺段：实际恢复/失败与停止位置见[来源恢复](../_sources/daily-20250916/SOURCE_RECOVERY.md)。可接受官方2025九月目标窗口归档或官方API有条目身份、原公开字段和真实分页终点。只重开受影响来源本窗；当前接口记录数量不证明过去没有研究。DeepSeek旧缺口由官方Change Log实际恢复撤回，MiniMax目录泛化缺口由本日CN真实跨窗切片撤回，见[窄恢复](../_sources/daily-20250916/NARROW_RECOVERY.md)。

以上外部保留项不是Coverage/Evidence通过。新可执行路由已实际执行；独立日级复核已处理筛选纠错、安全收窄和有限停止，不残留普通待办。

## 6. 复核

复核者：sept07_10_author（本日非作者日级终核；复用root有效首批校准与Codex单项独核）。

结论：通过

[实际日级独立记录](../_sources/daily-20250916/INDEPENDENT_DAY_REVIEW.md)：覆盖正式拟入选1/1（复用有效root完整证据/实际owner裁决）、必要安全反侧4项、11101/11656返修及11524误排纠错；核14来源实际有限停止与日期隔离，并补MiMo More及Google相交日标签误漏。root首批12题摘/v1身份校准复用，其余78身份不宣称全量独立准入或全文验证，宽列表未选151条不是逐项证据关闭。Books实际写入0；保留项不授Coverage/Evidence，完成限合同定义的安全终态。

V3校验通过；本日限定`git diff --check`通过（未跟踪文件的空白/本地链接另检查）。这些检查不能替代语义复核。月README、LEARNING_STATE和Books由root集中维护，未stage/commit/push。
