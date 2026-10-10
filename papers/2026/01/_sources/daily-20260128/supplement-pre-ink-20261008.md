# Jan28 InK joint-objective PRE — 待字面核

18129 v1作者actual §2.3–2.4/2.5.2、§3.1–3.4/Tables8–11/限制；peer已必要Source独核。只采GRPO rollout数据与独立domain rawtext CE人口分开、Bernoulli批调度联合目标；不是OPD整体regionalrecipe或知识因果。2+2+2=6，具体长期joint objective缺口深入。OPD可报告full/top10局部反侧，8B4/8H100冲突隔离；CE额外token/compute未匹配、ρλ无独立消融、teacher/judge与Base/Instruct身份近限定。

Owner TRAIN-GRPO Ch33。作者actual 当前940–978 既有抽象trace→R1-Zero→分阶段SFT/RL与蒸馏三分支完整邻接、Ch32/34开篇。现有讲阶段性的general SFT补能力，未承载同一RFT update从独立rawtext人口注入next-token目标的区别。拟两段插在“从DeepSeekMath到R1”节前，作为joint objective与随后分阶段配方交接，无新小节。

## 拟正文

训练目标的分工还可以在同一步发生，而不只按 SFT/RL 阶段交替。若当前任务所需原始知识在 base 中薄弱，可让一组问答 prompts 产生 GRPO rollouts，同时从独立领域原文采样 next-token loss；一个受限分支用 Bernoulli batch 开关与显式权重把后者加入 policy loss。原文不提供当前 rollout 的 action reward，也不先把它改写成唯一参考答案；它改变训练支持和联合目标，而不是证明 outcome reward 自己创造了新知识。两个数据人口、loss 标度、抽样概率与 token/compute 预算应分别记录。<!-- source-family:SF-2026-ARXIV-2601-18129 -->

[Thai 领域必要对照](https://arxiv.org/html/2601.18129v1#S3)支持该局部分支：原文式辅助目标优于问答式辅助目标，固定检索环境中也有收益，但额外 CE token/compute 未做等预算分离，开关概率与权重也没有独立消融。检索来自静态 FAISS/top-three search/read，准确率由作者 judge 评估；跨任务均分保持不等每项无退步，不能把它推广成跨语言知识注入或无遗忘保证。原文 forward/backward、数据审校与 retain 测试都付费；语料可信度、联合目标冲突或成本不合适时，纯 GRPO、明确分阶段的继续预训练/SFT 与外部检索仍合理，下一节的 R1 多阶段分工不因此被联合目标替代。
