# 2025-11-03 首批校准 ready

窗口BJT `[2025-11-02T09:00:00+08:00,2025-11-03T09:00:00+08:00)`。本日fresh重读AGENTS、两合同、来源使用说明/每日/arXiv、Prompt、ROADMAP；无既存本日停点，未沿用02候选或Weekly。14来源重新请求记录在本目录，未把跨日transport身份当Coverage。

## 首批已交Ohm独立校准

root独立复核反馈：11/03首批已交Ohm独立校准，作者可以继续未受影响的有限来源工作。尚未收到Ohm实际判断，不能记录准入或日级通过。

| 身份 | 实际本日材料/具体判断 | 独立核验点 |
| --- | --- | --- |
| [Reversal Invariance in Autoregressive Language Models, 2511.00341v1](https://arxiv.org/abs/2511.00341v1) | 完整题摘已读：主张CLM目标对整语料反转的likelihood不变，并据此质疑时间方向学习。原有AR目标是否学习方向依赖 → 声称目标的结构对称性 → 若正确会修正训练目标解释，潜在Owner TRAIN-PRETRAINING/MODEL-DECODER-ONLY，不是最终owner裁决。 | 潜在贡献明确，不以无benchmark排除；但题摘不能证明同一参数化模型/最优分布/链式分解三者等价。root先核该具体理论增量是否值得标准/深入审阅；不能直接把抽象chain-rule成熟结论计Durability3。必要首公开日期另核，未确认本窗，暂不入§3/不评分/不入Books。 |
| cs.CL标题 `Fine-Tuning DialoGPT on Common Diseases in Rural Nepal for Medical Conversations`, 2511.00514 | 本日官方25标题切片，标题明确为医疗对话应用，尚无模型系统机制线索；没有相关安全/纠错标记线索。Ohm额外核原生完整摘要通过此范围判。 | 范围关闭：既有方法的领域应用未建立当前模型系统贡献，不是所有医学方法一概暂缓；不强制读全文。 |
| cs.DC标题 `Towards Portability at Scale: A Cross-Architecture Performance Evaluation of a GPU-enabled Shallow Water Solver` | 本日官方25标题切片，GPU浅水求解器，不是模型计算。 | 范围关闭：硬件关键词不建立AI系统贡献，不抽象映射为GPU scheduler。 |
| Seed ID261电池研发AI Lab合作标题 | 本日重新取得type2 p20官方列表，标题为机构合作/电池R&D。 | 范围关闭，不因合作“AI Lab”准入。 |

## 日期事实与未决（仅定点）

- `.00341v1` arXiv原字段 `[v1] Sat, 1 Nov 2025 00:51:46 UTC`，是Submitted，不是公开。
- 本日定点DataCite原字段 `created=2025-11-04T03:56:24.000Z`、`registered=2025-11-04T03:56:25.000Z`；dates：Submitted=`2025-11-01T00:51:46Z`，Updated/v1=`2025-11-04T01:13:58Z`，Available/v1=`2025-11`。注册/Updated不能独自授first public；上界在03窗后，不能用它证明窗外owner，亦不能授当窗准入。
- 官方availability实际请求已存；本日regular announcement无内部截点，DST后的Sun20ET对应03窗结束09BJT，恰在终点不含；这是schedule边界，不补造该篇实际时刻。
- 下一可执行点：有限官方历史公告/作者首公开检索；若仍不能得到完全落窗证据，单篇终态隔离，不授Evidence/Books/Coverage。没有全月/fulltext队列。

## 实际入口和卡点

本日`fetch-native.mjs`已完成22原始请求，google-pubs/meta HTTP fetch失败后有web原源回退；Seed type1/type2各p0/p20；Hunyuan新publicList total9仍最早2026；Z.ai page2 hasMore=false仍最早12/07。Qwen迁移无历史文本、MiMo旧Blog日期切片缺失等须写本日具名终态，不当零命中。实际请求时间、status、URL、body和字节数均在同名receipt。

普通可做：原始窗口筛选收口、`.00341`有限日期恢复及必要准入消歧、六部分日报、机器/新文件检查；独立待验为Ohm首批校准结果及后续非作者日级验收。没有Books写入；长期采用需要原证据+context/owner/邻接差额，名字缺位不是理由。同一题摘的理论信号不授权无条件训练方向等价；同参数模型的loss、方向特定参数族的最优值与链式分解恒等式必须分开核验。

原始材料：`RAW_PRIMARY_AND_FINITE_END.json`、`date-00341.json`与receipt、`arxiv-cl-title-slice.html`/`arxiv-dc-title-slice.html`与receipt、`RAW_DISCOVERY_01.json`/`02.json`及本日native文件。官方宽月列表仅25+25标题查漏，不变全类题摘队列。

## 实际Ohm独立校准追加（2026-10-04）

已实际读取 [INDEPENDENT_CALIBRATION_NOTES.md](INDEPENDENT_CALIBRATION_NOTES.md)：1项潜在准入通过，中心理论采用未通过；2项领域负侧原生完整摘要范围关闭通过，Seed ID261未独立核。证明跳步是将词表重标号等变性用于序列反转，未保因果条件输入；bigram反例为复核者算术检查，不是论文实证。作者已在03日报§4并列原文主张与该反证，不采用无条件训练方向等价，不为争议改写成无贡献。

已有限完成本日日期恢复和来源收口，见 [进行中日报](../../03/README.md) §2/5：00341日期与中心理论分别具名终态隔离；有材料只重开受影响层。此校准不授14源总Coverage、Books或日级通过。前文“尚待Ohm”是历史交付状态，以本追加为当前。

## 非作者首批校准返回（2026-10-04T15:23:29+08:00）

复核者：Codex独立复核者（本任务独立分工，非Carver作者）。结论：**潜在准入校准通过，中心理论采用不通过；Carver按具体修正续有限工作**。实际原源、反例及未检查范围见[独立校准notes](./INDEPENDENT_CALIBRATION_NOTES.md)。

- `.00341v1`完整摘要与必要定义/假设已亲读。§4.5从词表重标号等变性跳到序列反转，没有证明同一有限CLM的前缀条件函数等价；已记录可正规化bigram反例。不得把链式法则、理想熵率相同升级为有限参数训练目标/学习曲线等价或CLM方向盲。无自身benchmark不是排除理由，但当前中心命题不能作正面采用。
- 公开日期继续保留，未独立重验或伪定首公开；不评分、不列确定当窗候选、不入Books。Carver续有限日期恢复与报告收口时保留本反证；日期到达不自动解决中心争议，材料采用需合法映射/完整证明或精确收窄后的修订证据。
- 医疗聊天`2511.00514v1`与浅水求解器`2511.01001v1`均额外核完整摘要，范围关闭通过；前者是既有模型领域微调，后者不是模型计算。不是一概排除医疗方法研究或GPU系统研究，亦未授领域性能/安全结论。
- 本轮未独立核Seed合作样本或14来源总体覆盖；首批校准卡点已交回，不代表日级验收。无需扩大25+25标题切片为题摘队列、另造修正理论或等待全月才能继续本日普通有限工作。
