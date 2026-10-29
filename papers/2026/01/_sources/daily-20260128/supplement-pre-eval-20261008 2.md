# Ch66 — 两家族 Source / PRE（待独立确认）

Root已释放Jan27窄写并授权本日两家族各两段+自身note；尚未写。Owner PLATFORM-EVALUATION-SYSTEM。恢复后实际再读Judge推断/PPI两段与前后、fairness framing/Contextual StereoSet/多属性干预交接、Ch65小结/Ch67开篇。旧PPI承载随机同人口gold residual与estimated weight不确定性，未承载query目标/doc预测粒度与query cluster；旧公平framing控制yes/no极性与context stereotype selection，未承载同一demographic属性不同cue不测同一构念且偏向可逆。

## 18486v1

拟分数3+1+3=7，构念有效性反证深入。作者已读§3–6/Limitations；peer必要SOURCE实际读Methods/Results/B runtime/C probe。501 base场景扩增，U.S. Black/White×binarygender，三模型，开放3seed/GPT单seed。cue-conditioned behavior不是内部bias因果；无答案GT。Figure3跨cue方向逆转；固定情境与readability回归不能消全部混杂。日期exact-v1 Jan26提交+官方最终ID/schedule与Jan27deposit上界联合，尚须peer实际确认该ID。

拟插入：现有公平framing SF2602.04306段后/Contextual StereoSet前，以下两段：

人口属性也不能只用一种提示线索定义。名字、方言、对话历史和显式类别标签，可能指向同一被研究的 demographic group，却同时改变语言风格、情境与模型可推断信息；同一名字列表内结果稳定，不证明这些 cue 可以互换。[人口提示构念的受限对照](https://arxiv.org/html/2601.18486v1#S4)在配对场景中观察到跨 cue 的差异大小与方向均会变化。因此 evaluation identity 应保存场景、cue 类型、具体实例与答案映射，并分别报告 cue-conditioned response contrast，不能把其中一个平均差异称为模型唯一的“内在偏差”。

这项证据来自美国 Black/White 与二元 gender 的501基础场景扩增及三个模型，开放模型三seed、闭源GPT一次；没有回答真值，不能由组差证明真实伤害、正确性或内部因果。Readability 与 prompt 回归只能检查部分替代解释，模型对类别的行为probe也不读出内部表征。多cue矩阵增加生成、解析与人工构念审核成本；任务确实固定某cue时可保留该协议，但跨人口或部署公平性声明须明确范围、补独立标签与风险评价。对应关系不可靠时报告分歧与Unknown，而不是选一个较低差异的cue自签公平。<!-- source-family:SF-2026-ARXIV-2601-18486 -->

## 18777v1 PRECISE

拟分数2+2+2=6，具体统计单位owner缺口深入。作者/peer实际读Method Eq1–3、ESCI与production setup、50gold repetitions/Analysis/Appendix calibration。线性P@K期望不需doc independence，非线性不可照套；gold复用calibration、estimated λ同gold调参不授有限样本unconditional unbiased。日期Jan26提交+最终ID/schedule+Jan27deposit联合尚须peeractual该ID。

拟插入：旧PPI两段及其SF2609.35815 marker后、人工富集gold人口段之前：

检索排序的残差校正还要先对齐统计单位。LLM judge 通常预测 query–document relevance，发布问题却可能是每个 query 的 P@K：先把其 top-K 文档的预测相关概率求平均，再在随机抽取的同人口 query 上，用真实 P@K 与预测 P@K 的残差修正大量未标注 query 的均值，例如 λ·mean(pred_unlabel)+mean(gold−λ·pred_gold)。线性 P@K 的期望可这样聚合，不需要把同一query内的文档假装独立；若改用非线性排名指标，就须重新推导，不能照搬文档 Bernoulli 乘积。抽样、方差与区间也应保留query及其相关文档的共同单位，而不是把top-K文档当K份独立人工锚点。

[PRECISE的必要对照](https://arxiv.org/html/2601.18777v1)在美国ESCI仅保留Exact/Irrelevant并排除不足K的query，另以100个gold与8400个未标注production Body queries作受限评价；这不是任意judge/人口只标100题便足够的证明。标注者协议与部署query人口、judge版本、K和相关标签定义共同决定估计对象，gold并不自动拥有真值；用同一gold拟合isotonic calibration并调λ时，额外不确定性与未明确的交叉拟合需保留，不采用无条件有限样本无偏保证。调用、随机人工标注、校准和query-cluster推断均计费；人口或指标改变时应补随机gold、保守区间或回退人工估计，不从匿名商业A/B及点估计签发一般排名收益。<!-- source-family:SF-2026-ARXIV-2601-18777 -->
