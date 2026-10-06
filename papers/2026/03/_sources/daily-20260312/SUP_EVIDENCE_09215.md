# 2603.09215 — SPAR-K必要Source与Ch24差额（Source/PRE/actualPOST通过）

[exact-v1](https://arxiv.org/html/2603.09215v1)，题名SPAR-K: Scheduled Periodic Alternating Early Exit for Spoken Language Models。第二包root实际完整AB/current准入通过。currentv2 Aug27窗外/题摘同v1，仅页数变化无已见重要纠错/撤回，采用本窗v1，不因版本号扩读v2全部或倒填。

## 身份日期与实际必要范围

SUP_EXACT_BATCH2.json原v1 TueMar10 05:39:03UTC提交；official no-advance finalID/DOI及deadline规则下界earliest Tue20EDT=Mar11BJT08，arxiv.content owning/findable DOI registeredMar11UTC02:08:10上界同03-11BJT，夹证arxiv日，不用Submitted/Updated/registration单独作公开。具体现页未见accepted先稿信号；日期请root原字段独核。

作者实际v1§1/3/4.1必要定义与Table1、§4.2完整/§5完整含Table2、AppB.1全部，未把AB或页面可打开当Source。拟评分2+1+2=5：交错text/speech条件深度选择重要分支，单生成器组件，稳定的输出类型/状态与费用约束；Ch24具体gap触发受影响内容深入。支持与直接反侧已足够，不展开无关引用。

## 窄机制与状态条件

§4.1 oracle先完整生成autoregressive history，再每位置用浅层head输出speech组装音频；未用这些浅层speech回馈。Table1 GLM浅16层top1一致19.14%但UTMOS2.922vsfull40的3.004，只支持“精确codec-ID一致不是相同感知proxy的必要条件”线索，不能从teacher-history实验授真实shallow autoregression可靠。§4.1/5明确固定shallow自回馈质量崩，不能静默用oracle隐藏distribution shift。

§4.2：文本全部full-depth，speech chunk按K2 even/odd或K3 full+两shallow固定节奏；每chunk重新按position决定，尾subgroup不足K有固定fullposition，不能把固定K理解为跨全输出绝对周期。frozenbackbone上对18k VoiceAssistant400K实例完整生成teacher distributions，CE拟合layer-specific LM head；这不是training-free/noextraheadstate。

§4.2.3明确跳过深层使早退位置deep KV缺失，下次full-depth step同时把之前位置的missingKV与当前生成位置parallel补算，类似prefill；不是直接复制浅层KV冒充deep，也不是full-depth一步能把先前已输出speech改回target分布。具体catch-up算子/逐层依赖/FFN/取消时机未披露实现，不能补造为免费KV填充或精确cache recipe。退出层计数只记录发出token的depth，不包括所有后续补算工作；真实FLOPs、壁钟、首包/尾延迟与cache峰值均未披露（本书分析），不以11%计数签速度。

## 评价与直接反侧

§5 Step-Audio2mini28layer，text:speech1:4，temp.7/top-p.9；GLM4Voice40layer，13:26，greedy。不同backbone/sampling不合并single-controlled定律。layerheadtraining18k伪标签及holdout MOS/WER选择exit层；budget/epochs/hardware/precision/batch/concurrency/seed/CI Not Disclosed。

四English数据AlpacaEval、LlamaQuestions、TriviaQA、WebQuestions。音频合成→Whisperlargev3 ASR→GPT4omini判QA正确或Alpaca LLMjudge0–100，UTMOSv2是预测MOS非真人MOS；ASR-WER是speech对同模型已输出text的一致性，既非外部答案准确也非全部语音质量。Mean列平均混合三个accuracy与一个judge分数，称平均分/代理而非统一accuracy。

Table2 Stepfull54.22mean/MOS3.710/WER1.51，Triple22 mean55.29/MOS3.668/WER1.51、speechmeanexit25 vs28；固定25层mean50.13/MOS3.058/WER3.40，entropy26策略mean41.51/MOS1.651/WER11.01。GLMfullmean52.37/MOS2.982/WER4.31；Triple37 mean51.94/MOS2.909/WER5.77（0.43平均分绝对下降约0.82%相对，不写0.82pp）；Even36 mean50.83/WER5.36更退，Odd36 mean50.35/WER5.06更退。Conf36 mean52.89高于SPAR的G4/5/6但WER7.62，不能说所有confidence策略无效；baseline阈值大规模tune，AppB .5/.1增加选择预算。

文本Even36退出GLMmean18.43（MOS2.979仍接近full2.982，说明感知proxy不能替语义），text-confidence+speechEven mean48.61亦退。具体任务切片LlamaQA/TriviaQA等有退步，平均不授各任务收益。粗深度降低最多speech11%/5%不等完整生成stepwall-clock。现原证不足以证明无auxcompute、完整MOSSLO或分布保真，只保留有损schedule的质量—资源proposal。

## actual owner差额与逐字PRE（下列为原提案，已由root写入）

唯一owner `MULTIMODAL-GENERATIVE-PARADIGMS`：[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)，当前686–727完整局部已读，及Ch23/25开篇。706思维speech交错与716ARIA prefix-rate都管理输出次序/状态，却不承载speech与text的不同depth、per-layerhead及missingdeepKV回填。Ch17结构跳层泛化边界与Ch48verification责任定点读过，不把未经target验收earlyexit称speculation。拟插ARIA two paragraphs/comment之后、speech粗细时间链之前。正式逐字提案：

输出节奏之外，交错生成还可以为不同 token 类型选择不同执行深度，而不改变 codec 的时间层级。一个有损替代分支让文本保持完整 Transformer 深度，语音位置按固定周期在浅层输出与完整执行之间交替；冻结基座后用完整模型的输出分布训练浅层 prediction head，再以独立质量切片选择退出层。teacher history 上浅层 codec token 不同却有相近感知代理，只提供可试的线索，不证明这些 token 回馈后仍稳定。[必要方法](https://arxiv.org/html/2603.09215v1#S4.SS2)还要在后续完整步骤补算早退位置缺失的深层 KV；周期执行不会把先前已发出的 token 改成完整模型采样，也不继承第48章 target verification 的分布保证。<!-- source-family:SF-2026-ARXIV-2603-09215 -->

这用训练与保存额外 head、选择周期及补算 cache，换取发出部分语音 token 时较浅的路径。[有限对照](https://arxiv.org/html/2603.09215v1#S5)中，固定浅层自回馈和部分 entropy 策略会退化，但某个 confidence 配置仍保留更高语义分数；周期方案也有任务退步，预测 MOS 接近不代表答案正确。平均退出层降低只统计 token 发出的深度，不等包括 KV 补算、语音渲染与排队的 FLOPs 或墙钟加速。head、codec、退出层与周期应共同定义生成身份，并分别验收文本语义、speech–text 对齐、音质和完整成本；误差积累、状态回填或质量预算不成立时，保留全深度生成、经校准的 confidence 分支或独立 speech decoder，不把同一 shallow policy 直接用于文本。<!-- source-family:SF-2026-ARXIV-2603-09215 -->

拟本人末注：`SF-2026-ARXIV-2603-09215` — Daily2026-03-12补查；exact-v1§4.1/4.2/5/AppB.1，2+1+2=5，text/speech条件depth与缺失deepKV具体差额深入。oraclehistory不等真实shallowfeedback，额外18kheadtraining/cache补算与选择费用近正文；仅exitdepth不授wall-clock，预测MOS/WhisperWER/GPTjudge与语义分账，GLMconfidence优均分与任务反侧保留。v2窗外不倒填，未核实现/复现，hardware/precision/完整budget/seed/CI/SLO Not Disclosed。必要Source/逐字PRE待非作者实际核，root写后须非writer actualPOST，不授DAY。

## 实际落地与POST

root实际精确v1§4.1–4.2、§5.1–5.4、Tables1–2必要Source及原日期字段夹证、逐字PRE通过；未称本轮额外独读AppB.1或代码。root已写Ch24新720/722两段及本人2315末注。非writer supplement_20260312实际顺读704–732完整局部、上述新段与自身末注，并重新实际回对官方v1§4.2全部、§5全部含Table2，actualPOST通过：额外head训练、teacher-history与真实反馈、deepKV补算不改已发token、exitdepth不等完整成本、confidence及任务反侧与代理分账均与原证一致；ARIA prefix-rate与时间粗细链的旧消费者仍共存。末注已请求root同步通过状态，未触及其他Books。这里更新原提案的实际状态，不删除旧待核措辞原记录，不授DAY、实现或复现。
