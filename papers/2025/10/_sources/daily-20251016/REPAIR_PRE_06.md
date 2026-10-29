# 第六包：两个实际差额与两项具体已有覆盖

仅整体PRE提案，未SAVE。Books上下文/完整ROADMAP已重读，Ch23/Ch66实际目标完整邻接及Ch22/24、Ch65/67交接有效层复用。reader只核采用关键及完整稿，不重第一Methods；正文、独立marker、本人注整体审。两NC不写marker/注，四项均未核代码/复现。

## 12670 TerraCodec / 2+1+2=5 / MULTIMODAL-REPRESENTATION Ch23

实际必要见EVIDENCE_WRITER末，R50决定层通过。W20“全场景”收窄为§3.1/AppendixC实际块内全空间。Ch23共享token阶段VideoFlexTok完整两段已有有序register/截尾及重建与AR消费分验，没有先重排空间/通道载荷再截尾的区别。唯一插位：完整`[VideoFlexTok 的有限对照]...不由可变长度批准信息无损。`之后、完整`重建与 AR 可预测性还可由不同 token 承担...Prologue...`之前，两侧完整段已读，不插旧两段之间。Ch24不另写。

正文：

可变预算还要看被截去的token装了什么，而不只看序列变短。若每个token装一个空间位置的全部channels，直接截尾会删去整片区域；一条分支先在每个空间块内重排latent，让每个token携带一组channels并覆盖该块全部位置，再随机保留prefix，解码前按原布局还原并补齐缺失部分。[受限时序codec对照](https://arxiv.org/html/2510.12670v1#S3.SS2)由此把空间覆盖与通道细节预算分开，却不证明缺失信息已无损恢复，也不让学习到的均值或mask成为真实观测。重排身份、块/通道顺序、保留预算、熵模型与补位decoder须共同版本化；训练读取真实量化历史、推理读取已重建历史时，还要另验误差传播。Bootstrap帧与后续帧的码费分别结算，全部codec及额外可变预算训练、历史缓存、熵编解码和独立重构验收均付费；只看后续帧或token比例不能宣称全流码率、时延与SLO同幅下降，高压缩也可能弱于固定率模型。传感器/处理版本、保真或总预算失配时，保留原空间布局、固定率codec和可信原信号，不由一份checkpoint可调预算批准通用无损压缩。

独立marker：`<!-- source-family:SF-2025-ARXIV-2510-12670 -->`

本人末注：

- `SF-2025-ARXIV-2510-12670` — Herschel，Daily2025-10-16补Oct15；[exact-v1](https://arxiv.org/html/2510.12670v1) §3.1–3.2/4/5.2/A1.1/C/E3必要，2+1+2=5，块内spatial/channel载荷与prefix预算差额深入。保bootstrap/all-frame、teacher-forcing与推理补位、fixed-rate反侧/额外400K步及全费，不采全图无损/跨传感器普适或净速。R50仅准入，必要/整体PRE/SAVE/完整自读/solePOST只本日canonical实际层；未核代码/复现。

## 11822 Agreeableness / 2+1+3=6 / PLATFORM-EVALUATION-SYSTEM Ch66

整体消费Cicero R19首次必要§2–5/7及B，writer不第二Methods。366代码任务/六generator全人工标签与14validator；静态generator/validator、minority veto阈值及回归都需gold，missing修复使majority最大误差14.8→4.8，不能全归veto。

actual Ch66总体率校正完整两段已拆prevalence与TPR/FPR、人工区间/漂移，未将多数accept与经校准少数reject作为不同规则比较。唯一插位在完整`平台因此需要保留区间的来源...回退原有残差校正或human-only评估。`之后、完整`总体残差在旧流量中为零...`之前；上方SF2604-03257及下方切片校准两段均不动，实际完整邻接已读。

正文：

多个validator的集成也不能只看总体agreement：正确候选占多数时，习惯accept的成员可以取得很高precision，却几乎不会识别错误；多数accept不等于独立支持变多。可将多数规则与经gold校准的少数否决规则分开比较，同时报告正确类通过率、错误类拒绝率和最终候选人口，而不让任一高均分替两类验收。[受限代码验证对照](https://arxiv.org/html/2510.11822v1)中，否决阈值及准确率回归都需要人工标签，修复missing记账本身也改善多数基线，因此不能把全部收益归于新规则，更不是零标注保证。校准generator、validator成员/参数、标签与缺失规则应共同冻结；换generator或错误类型后，旧关系未必保持，需补代表性gold并重拟合。全部候选生成、各validator调用、人工标注、阈值选择与独立回归均付费；相关误差、静态身份或两类支持不足时，保留已校准单judge、原多数基线及独立人审，不由少数否决本身批准真实正确或任意领域可靠。

独立marker：`<!-- source-family:SF-2025-ARXIV-2510-11822 -->`

本人末注：

- `SF-2025-ARXIV-2510-11822` — Herschel，Daily2025-10-16补Oct15；整体消费Cicero R19 exact-v1 §2–5/7及B首次必要，2+1+3=6，多数/少数否决与两类校准差额深入。保366代码任务、完整gold/静态成员、missing修正基线与全部调用/标注费，不采零标签或主观领域泛化。未第二Methods/代码/复现；整体PRE/真实SAVE/完整自读/solePOST只本日canonical后到真实层。

## 12367 LLM-REVal / 2+1+2=5 / PLATFORM-EVALUATION-SYSTEM Ch66 具体NC

消费R8首次必要§6/7.1/A5。最高score-gap15对/13标注者每对2人，人稿删图/附录不是全人稿truth；polishing改style也改score，81/174是筛后issue-local revision，不是整篇质量改善率。

actual Ch66完整`参考答案可信，也不意味着judge能中性地使用它...`及独立SF2509-03419，固定任务/候选、独立审核语义保持改写、维度/gold人口，明确score-shift非错误率；后邻SF2509-13234完整段另拆正确性与可靠声明。该具体论证承担本次仅采的有限风格/判分人口反侧；本文没有新给出语义保持认证或全人稿质量测量，拟具体NC。不是按peer-review主题判覆盖，不采polishing改善真实科学质量。

## 12462 Judge bias / 2+1+2=5 / PLATFORM-EVALUATION-SYSTEM Ch66 具体NC

消费R18 III-A/B表I–III首次必要：同judge先选最高50题、迭代保>=9 biased答案、剩92题测试，人口受judge选择。GPT训练后偏clean、JudgeLM偏bias，Alpaca混合非一致退；四mitigation建议未实测。不把降分认证客观公平或独立任务能力下降。

actual同一SF2509-03419完整论证规定candidate/扰动来源、reference/rubric/判分人口共同冻结，分报有gold准确率与稳定性，不把score-shift当错误率；SF2509-13234再分内容正确与声明可靠两轴。它们具体承担本次只采的judge/protocol依赖读数及选择人口分责，未采本文训练结果为新更新机制或有效防御，拟NC。若扩采完整训练因果须另开命题，不能由本NC预授权；不制造泛泛公平段/marker。
