# MiMo-Audio Sep19 发布单篇必要证据与Books差额

作者Meitner。Cicero已独立校准author官网Paper明确September19,2025的发布事件、准入2+2+2=6；不追hours，commit不证明public。官网日证与Sep19固定README内容身份分责，不冒充December技术报告。

## 实际读层

- `SUP_MIMO.raw`：Paper8行、Blog15完整题名/描述；第6 Paper是MiMo-Audio Sep19。
- `SUP_MIMO_SEP19_GITHUB.raw`：官方固定`3b278795224cae06bd70cb4438633b2934b8367f/README.md`实际完整Introduction/Architecture。raw.githubusercontent失败000/35保留在`SUP_MIMO_SEP19_README`，GitHub blob200替代。版本本身绑定内容，不据commit时刻声明public。
- `SUP_MIMO_DEMO.raw`：Introduction、Tokenizer、Architecture、Performance和ICL评价说明。current Demo支持实际说明，不据后来样例倒填Sep19实验。
- `SUP_MIMO_FIG_model.raw`实际视觉核图：LLM每步接patch表示，patch decoder接LLM projection，时间位置与码层作delay多head生成；四帧汇聚与图示相符，图仅示意四codebooks，不替代README八RVQ说明。
- `SUP_MIMO_FIG_comparison.raw`实际视觉核：MiMo-Instruct7B在MMAU-Pro56.8低于GeminiFlash59.2；MMAU74.9高于所列模型；BigBenchAudio S2T72.9/S2S60.2，后者低于GPT4oAudio2412 67.2。不同模型、训练人口、输入输出/评估协议，不作同预算组件消融。`benchmark`图透明黑字在当前查看器不可辨，本次不依赖其数值，不称已读；未扩全附件。

## 最小支持与不支持

固定README明确1.2B codec、25Hz八RVQ共200 codes/s；patch encoder把连续四个时间帧及其RVQ表示聚成一个LLM位置，LLM时间rate是6.25Hz，patch decoder再自回归delay产生完整25Hz RVQ。减少的是大主干sequence positions，既不删除RVQ细节也不把codec变成6.25Hz；局部encoder/decoder与codec仍计算。公开方案支持替代factorization，不要求跨家族排行榜证明该方案唯一更好。

未披露matched patch-size消融、完整训练/采样预算、硬件/precision、batch/concurrency、端到端首包或tailSLO及重复不确定性。不能从200/6.25=32的位置比宣称32倍总加速，也不采用29倍成本、全部任务胜、部署安全或fewshot能力由patch唯一导致。100M+hours、10M codec hours仅作者声明，不作数据独立审计。当前安装说明与固定Sep19说明不同，未执行代码、听测音频或复现实验。

## Books具体比较与窄共享请求

已实际读PROJECT_CONTEXT、LEARNING_PHILOSOPHY、WRITING_GUIDE、最新State仅路由、ROADMAP；Ch23当前280–348与Ch24当前718–801含完整邻接。

- Ch23 `MULTIMODAL-REPRESENTATION`的分层残差段解释RVQ前K输入/loss/部署一致，以及SlowAR时间、FastAR同帧depth；这**已有覆盖**码层身份/codec rate不授SLO的一般约束，但没有连续四帧合一个主干位置且保留完整codec的patch消费者路径。
- Ch24 `MULTIMODAL-GENERATIVE-PARADIGMS`现788附近的时间链是首codebook降采样后逐级masked refinement，非同一四帧patch内delay AR；前文Qwen主码+同帧MTP与ARIA交错rate也不是这一机制。具体长期gap是**主干时间粒度、局部decoder时间依赖与RVQ depth三者分责**，不是追加产品摘要。

提请root先协调Ch24窄owner；作者不写Books。建议在音频时间链前插入一短段：高rate codec逐帧由大主干预测本来简单，连续帧聚为patch可缩主干历史而把细粒度AR责任交局部decoder；必须共同版本化patch大小/边界、全部codebooks和decoder，codec rate并未降低。多帧聚合引入缓冲/局部autoregression与错误传播，真实收益需含codec、两个patch模块及播放提交测量；首包/质量失配时回逐帧或更小patch，不由主干位置数签发全成本/实时保证。来源绑定固定Sep19README，当前图仅补说明、不引后来数值。

该知识gap已按root最新“一段+自身SF末注”窄锁落实于Ch24音频时间链前。作者将Cicero§9已PRE两段原词合为一段，保留完整费用/边界/回退及两側邻接，不改Google或并发2026内容；写前快照对比只有自身正文和末注两处插入，无删除/替换。Cicero§10已实际回固定原证、live完整音频邻接、正文及自身注，非writer POST通过；Books实际整合1，窄范围写入结束。必要设计证据/Books PRE为§5、六部分内容PRE为§8、逐字PRE为§9；日级DAY/完成态FINAL仍待实际复核，不由局部POST代替。
