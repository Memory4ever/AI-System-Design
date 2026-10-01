# Apr17 最后七项 source → owner 独立复核

复核者：`apr17_final_batch_review`（非报告作者）。范围只有第十二小批七项，不扩展原始库存，不验收整日来源覆盖、分母冻结、Books 实际写入或日级 Gate。读取当前 AGENTS、研究合同、Report 合同、统一 Prompt、作者提案，并重新打开七份官方 exact-v1 HTML 的必要方法、评价及直接反证；对读实际目标论点。未复现实验。非交互子任务不增加跨模型复核。

## 逐项结论

### 2604.15010v1 — 修正一处事实后通过：5分，标准审阅，仅报告

[原文](https://arxiv.org/html/2604.15010v1) §3、§4–8、Table2、AppendixG 支持小模型上的受限定位与干预证据，不支持通用层数门槛或永久不可纠错。L24–25 skip 提升而 L22–25 skip 下降，未测试的层块不能补成确定机制。**89个 CounterFact pair 的条件是同一 Llama 3.2 1B 正确预测 original 与 counterfactual 两个答案；不是两模型均正确。** §8明确未做 Gemma 事实召回扩展。作者 notes 和 README 的该句需同步修正。

对读 Ch66“Interpretability Graph 只有 Diagnostic Authority”的原始干预、paired patching 与诊断权限边界：受限复制值得保留，但现有论点不需据此升级成通用架构结论。“仅报告”不表示论文无机制贡献，也不把整个新配方伪称已有覆盖。

### 2604.15086v1 — 通过：6分，知识缺口深入审阅，Ch23窄整合提案

[原文](https://arxiv.org/html/2604.15086v1) §3.3 将参考音频路径去位置编码、简化局部时间模块，另注全局音色，目标是参考音色而非参考时间轴。Ch23现有双流音频表示与 modality domination 未讲这条有选择的 conditioning 责任划分；`MULTIMODAL-REPRESENTATION` 是合理 owner。

Table9比较双条件路径的存在与否，**并未单独消融时间信息抑制模块**；可解释设计，不可声称该模块已被因果证明带来同步收益，更不能声称统计独立或完全去时间。L0 CLIP-only 较优及小规模主观样本边界保留。实际写入宜限于表示分工及代价，Ch24接生成机制，不再复制整套框架。待写后复核。

### 2604.15093v1 — 通过：6分，知识缺口深入审阅，Ch29窄整合提案

[原文](https://arxiv.org/html/2604.15093v1) §3.2、§4.1、Table3、B.2 明确由进展监测触发 expert 介入；SFT只监督 expert 步骤，输入保留 learner 错误历史。Ch29“Loss 位置与 Corruption Support”分清监督位置，GUI流水线分清可见状态，却未明确这条“失败状态可见、失败动作不作模仿目标”的恢复监督分支，`TRAIN-SFT` 窄补成立。

同轨迹数不等于同 teacher/monitor 计算预算，Table3也未单独隔离 loss mask 的因果作用；监测仍为模型判断，非环境真值。半极差非置信区间，指令相似度不证明零污染。不要将论文名已出现当作已有覆盖；第26章消费部署动作与环境后果。

### 2604.15097v1 — 通过：5分，标准审阅，仅报告

[原文](https://arxiv.org/html/2604.15097v1) §4.1–4.3比较经验表示与近似匹配的提示预算，不只是科学应用指标；故研究 Agent 经验接口的窄命题可准入，不恢复 AI for Science 路线。Gene在 Pro 上低于无指导，互补经验组合也会退步；结构扰动实验不等于真实在线编辑验证。

Ch77 procedural memory 已保留 derived/advisory state、来源、适用范围与重新评价的控制边界。本次新包装对照可以保留受限反证，不必为此新增机制节；不能声称其全部经验格式已由书稿覆盖，也不能由提示包装授予 Workflow policy 权限。

### 2604.15148v1 — 通过：6分，知识缺口深入审阅，Ch33窄整合提案

[原文](https://arxiv.org/html/2604.15148v1) §2.2–2.4、Table2、§3.3.2以 gold-answer 长度归一 logp 比较真实与批内随机 document/refinement，对 query token 叠加局部信号，其余保留终局 advantage。Ch33 policy-implied value、prefix scorer 与一般局部 credit 未具体承载这个训练期检索代理，`TRAIN-GRPO`窄补成立。

随机批内替换只近似匹配长度/结构分布，非逐样本严格配对；改 document 与 refinement，故不是纯 query 因果识别。all-fail仍有代理不等真值；deadzone、负值衰减及 query length normalization 的代价/失效保留。Ch76拥有 evidence validity，不将此训练代理改写成推理时置信度或检索事实验收。待写后复核。

### 2604.15163v1 — 通过：5分，标准审阅并定点收窄保证，仅报告

[原文](https://arxiv.org/html/2604.15163v1) §2.3、§3.2–3.5、§4.3：原库执行聚类取两个代表，再生成区分数据，Pandas为模型生成的 proxy。Eq4是理想区分覆盖条件；实现只检查所选二者，不证明全查询语义覆盖。执行确定性不等语义正确性，格式归一还可能丢有意义差异。

Ch66自然语言需求/input domain/reference/test oracle 分权及 reference/matcher 覆盖论点已有该采用边界。MDD是值得审阅的具体检验 recipe，可仅报告，不能宣布通用正确性证明，也不必反向否定其全部经验收益。深入保证相关部分是限域工作，不改变5分评分。

### 2604.15171v1 — 通过：5分，标准审阅，仅报告

[原文](https://arxiv.org/html/2604.15171v1) §III–IV、TableI、Fig9为不同正则提供20次训练及残差/生成指标/时间的对照；小规模实验直接研究生成目标有效性，不因 MNIST 排除。FP配方学习率不同，宽误差范围与强正则残差退化不能写成质量等效或方程约束唯一致效。

Ch24 score regularity、数值假设与 solver 验证已保留理论条件和经验质量分账的原则，但未完整承载此配方。保留受限负面证据而仅报告合理；不采用§III-B将条件噪声导数直接当边缘 score 通用恒等式的解释，不由 proxy residual 签署发布质量。

## 日期与完成边界

本日原始 receipt 的七项 v1 Updated 为 `2026-04-17T00:51:06Z`、`00:55:34Z`、`00:56:04Z`、`00:56:13Z`、`00:58:13Z`、`00:59:33Z`、`00:59:50Z`。核对字段和值，不将其重命名为首次公开；作者采用的官方槽、连续ID、OAI及邻界联合推定仍须参加整日独立日期检查。本文件不单独认证08～09归属，不认证其余81项。

三项知识缺口只通过 source → owner 提案，**尚未验收实际 Books Integration**。四项仅报告可以取得上述受限审阅结果；15010修正事实后再关闭。没有共享写入，也没有 stage、commit 或 push。
