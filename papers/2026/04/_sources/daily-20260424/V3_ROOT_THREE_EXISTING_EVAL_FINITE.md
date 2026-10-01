# 2026-04-24 三项 Evaluation「已有覆盖」的有限非作者复核

复核者 root；原日报与证据作者 apr01。实际重新打开三篇官方 exact-v1 的必要方法、结果与反证，并对读 `PLATFORM-EVALUATION-SYSTEM` Ch66 的现有论点。这里仅判断三项拟 `No Change — Existing Coverage`，不替代其余候选、来源、日期和整日报 Gate。各论文的作者实验都不是生产部署或独立复现。

## 2604.21505v1：需求歧义与合法多解

[官方 v1](https://arxiv.org/html/2604.21505v1) §4.1/5.1–5.4 将 1,304 个 function-level task 扩为四类歧义输入，比较原测试接受率、同题多输出功能冲突，以及检测、定位、澄清三个不同动作。原测试只按原始解释评分，不能证明其它合理解释都错；同题输出相异也不是功能错误率。GPT-4 judge 的 50 人工样本 96% agreement 与表 6 约半数 precision 只支持受限自动判别，不形成在线可靠澄清 Gate。

Ch66 已明确说明固定 reference/test suite 只适合可信单解任务；开放需求、多种合法实现需额外语义审计、反例和不确定项处理；其分层 evaluator 还把 deterministic verdict、残余 semantic judge 与人工裁决分权。这个现有命题足以承载本篇长期判断，但未收录 Orchid 的全部歧义分类或六模型数值。维持 2+1+2=5，标准审阅，具体已有覆盖；不把作者“强模型退化更明显”外推为普遍趋势，不新增 Books。

## 2604.21192v1：具身进展与危险事件的不同分母

[官方 v1](https://arxiv.org/html/2604.21192v1) §III–IV 采用 B1K Challenge 的 50 任务背景，但安全结果只选 20 个中等难度场景；重跑两套公开 checkpoint，原 Q-score 看终态，sQ/seQ 又按对象状态和 support-object subgoal 惩罚，并单列 target/non-target violation。8 位专家的 500 个视频统计是“某任务是否出现该失败类”，不是全部事件频率。两 policy 成功率低、危险发生机会少，故少违规不能证明安全；seQ-Oracle 把 support subgoal 置 1 只是受限上界。task-scope 外的物体风险和真实环境均未测。

Ch66 已有具身 EvalSpec 主线：低能力不能冒充安全，attempt→near-hazard→terminal 要分账，且要记录机会、模拟状态和 controller/safety envelope handoff。该判断与本篇新的 score 构造不同，但已经承担长期可迁移的评价边界；不能声称整个 sQ/seQ 算法已进书。维持 2+2+2=6，深入审阅，具体已有覆盖；不新增 Books。

## 2604.21276v1：群体差距收窄不等音频公平改善

[官方 v1](https://arxiv.org/html/2604.21276v1) §2–5 测九种 ASR、多个群体切片及音频 mask/silence；在严重退化时，相对群体差距可缩小而绝对 WER 同时升高，重复插入还须作为单独失败类型计数。论文将不同模型的 audio bottleneck 与错误形态相关联，但模型训练语料、decoder 和输入通道共同变化，不能把 audio compression 认作唯一因果。英语朗读、Fair-Speech/LibriSpeech 等受限设置不支撑多语、自然会话或线上 SLO 结论。

Ch66 的压缩发布论证已经要求同时看绝对质量、群体切片、相对差距和更好群体是否退化，并对音频有损压缩设置原输入配对的 worst-family release gate。本篇采用的是**输入音频 mask/瓶颈**，不等于书中权重剪枝、量化的机制；复核只确认二者共享的测量判断已有 owner，不说实验配置已吸收。维持 2+2+2=6，标准审阅，具体已有覆盖；该模型比较和重复类型作为日报受限案例，不新增 Books。

三项既有覆盖均是命题层的 `No Change`，不是全文所有数字或算法已在书中。首次公开归属沿日报保存的官方公告槽、相邻身份和 exact-v1 有界推断；本次没有取得逐篇原始公告日志，不能用 arXiv Submitted/Updated 单字段替代。余四项拟已有覆盖及其它日级 Gate 工作仍开放。
