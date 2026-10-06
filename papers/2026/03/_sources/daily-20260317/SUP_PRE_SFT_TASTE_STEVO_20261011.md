# 三家族必要证据与逐字PRE（独核与实际POST通过，不授DAY）

执行日期2026-10-11，仅补03/16BJT。原exact-v1完整AB与官方DOI字段分别在SUP_AB_FIRST与SUP_DATACITE_BATCH，Fri13常规最早公告与arxiv.content注册上界同落03/16只授首次arXiv日级夹证，不等于注册即公开或排除独立先稿。以下Source与Books均为作者提案，不将AB校准当必要Evidence通过。

## 12397：TRAIN-SFT / Ch29 mask-policy后、trace选择前

[精确v1](https://arxiv.org/html/2603.12397v1)：必要§3/4/limitations、Appendix A/B实际读；固定QA而重写trace，QT与T-only、think/no-think评价提供局部反证。7049样本为合成，Appendix A L329作者声明专家逐triplet审核/修改丢弃；人数、一致性与独立审校原证未披露，未验证作者审校过程，不能说“未人工审校”。same hyperparameters/equalsteps但不同监督tokens，不授等totalcompute或自然CoT忠实性因果结论。Qwen3 0.6–14B及EM/Deception/TRAIT/DarkBench/MACHIAVELLI行为评价仅其协议，limitations L282未评价事实准确性、instruction-following及真实对抗输入；无数学/知识效果评价、无复现。评分2+2+2=6，安全行为反侧深入。现Ch29的mask alignment与监督位置选择没有固定答案、轨迹内容改变行为分布这一具体分支；Ch28/30交接不接管SFT目标。review_mar17_18指出先前数学/知识、未人工核验措辞无原证，已原§3.3/limitations/A读回窄改，不掩盖误判。

拟插在现“必须记录loss mask policy”之后、长轨迹监督选择之前，逐字两段：

监督位置正确仍不能认证被监督内容正确。长答案包含最终结果和中间轨迹时，保持同一问题与最终答案、只改变轨迹内容，是区分两路监督的一个受限对照：最终答案不变，不意味着行为分布或跨任务泛化不变。只训练QA、完整QTA、QT或无问题/答案的T-only，是不同内容与条件接口，不能用同一个“用了trace”混称；这里也不是选择性loss mask已得到实验验证。完整可信demonstration仍是直接基线，不能由Q/A保持一致就把其中迎合、误导或不安全轨迹当作无害填充。<!-- source-family:SF-2026-ARXIV-2603-12397 -->

[固定QA的必要对照](https://arxiv.org/html/2603.12397v1)在合成轨迹及有限Qwen3家族中发现，改写轨迹后的多种行为评价不沿同一方向变化，部分变化在no-think输出模式仍存在；这不证明自然产生的CoT普遍忠实或不忠实，也不是所有训练预算已匹配的因果定律。相同步数与超参并不匹配不同轨迹的监督token数或总compute；作者声明专家审校，不等于我们已验证其人数、一致性或数据过程，生成器与judge仍可能引入偏差，真实对抗鲁棒性也未评价。数据构造、轨迹/答案loss分账和独立行为回归均付费；轨迹审核或预算控制不足时，保留可信demonstration、单独检查答案与行为，必要时回到普通response-only或经核验的完整trace，不由单项平均分批准训练产物。<!-- source-family:SF-2026-ARXIV-2603-12397 -->

## 12350 TASTE：MULTIMODAL-REPRESENTATION / Ch23 TADA后、参考音色前

[精确v1](https://arxiv.org/html/2603.12350v1)：必要§2/3全方法/评价与消融实际读。CTC提供在线预测文本坐标，声学分支补细节，causal unit与vocoder限制缓冲；训练先oracle再预测文本joint，§3.3.2实际使用FSQ、无显式codebook，不按模块名VQ回填传统码本。英文Emilia400h+LibriTTS600h、固定ASRencoder/CosyVoice2vocoder，twoH100/batch128/各5epoch为训练；§3.1.1 streaming metrics单A100，precision/streaming batch/concurrency/SLO Not Disclosed。HubertWER、UTMOS预测、TDNNspeaker、MFA时长不是语义/人听真值。长形87同speaker拼接平均223.6s不是自然会话；10–30s window/FCL从已available chunk计时不等原音频零等待，SLM RTF是外部13B吞吐估算，非实际SLM端到端计时。主码率不配对，matched150bps消融并非感知指标全胜；外部ASR亦增费用。评分2+2+2=6。现Ch23拥有semantic/acoustic streams及真实transcript CTC/Viterbi；差额是先预测文本坐标的在线边界，不复制Ch24采样。

拟TADA段后、参考音色小标题前逐字两段：

在线输入未必已有可靠transcript，因此文本索引还可以由轻量CTC头从当前声学特征预测，再与补充声学细节的量化表示共同交给消费者。这个分支将“真实文本对齐后消费”改成“预测文本坐标后消费”：训练先用oracle文本隔离声学路径，再切到预测文本联合优化；因果unit decoder与vocoder使分块输出成为可能，却不消除ASR错误、分块边界、聚合窗口或消费者缓冲。CTC词表、预测头、声学量化配置与chunk配比须绑定，未校验的文本坐标不能升级为真实内容。<!-- source-family:SF-2026-ARXIV-2603-12350 -->

[TASTE的受限语音证据](https://arxiv.org/html/2603.12350v1)仅支持披露的英文重构/流式协议；低码率匹配消融不是所有指标全胜，同speaker拼接长音频也不代表自然长对话。ASR WER、预测听感与声纹/时长代理须分别解释，外部ASR增加费用；估算语言模型吞吐不等于实测完整speech-language-model延迟。训练切换、两路表示与逐块解码均计费，文本识别、波形或时序回归时，保留真实transcript对齐、固定-rate codec或等待完整输入的原分支；表示层声明可消费身份，Ch24继续拥有生成路径，不由causal标签批准实时SLO。<!-- source-family:SF-2026-ARXIV-2603-12350 -->

## 13215 StEvo：MULTIMODAL-WORLD-MODELS / Ch25 hidden-state evidence后、OpenSchema前

[精确v1](https://arxiv.org/html/2603.13215v1)：必要§3–5实际读。225任务六类，两阶段：Control的observation遮挡成功与action启动成功共同通过，失败过滤后才Evolution的progress/physics/coherence，故后者conditional分母；不是“看懂初始观测”的独立Observation层。Gemini3.1Pro同族specialists，stateprogress三次unanimous，其他majority，自动判别非物理真值。180随机视频3人注释只核agreement，physics agreement非绝对groundtruth。Table2/3字段群体/简单配对均值并非透明一致，不抄配对数字；仅采用控制前提与状态推进分账/局部定性失败。评分2+2+2=6，具体设计反证深入。现Ch25受控hidden-state intervention已区分画面/状态，但没有遮挡/启动两个Control checks→Evolution条件评价分账。review_mar17_18指出先前三层措辞借错观测识别含义，已原§3.1–3.2定点读回修正。

拟旧2608.30692 source-family之后、OpenSchema标题之前逐字两段：

只保存场景不意味着它能在不可见时继续演化。一个受限评价分支先检查两个Control前提：指定动作是否真正启动过程，观测控制是否在过程中持续完整遮挡或移出目标；两者通过后，才分别检查不可见期间的状态progress、物理plausibility与前后coherence。它把“根本没有启动或没有成功停止观测”与“已启动但隐藏期间停止/倒退/不合理”分账，却同时改变后阶段分母。只在通过Control的样本上测得的Evolution成功，不是全部任务的端到端成功率；系统比较须同时报告原任务数、Control通过数和条件/无条件指标，不能让过滤失败样本变成世界状态可靠的证据。<!-- source-family:SF-2026-ARXIV-2603-13215 -->

[StEvo的必要协议](https://arxiv.org/html/2603.13215v1)在有限视频生成模型、六类任务中分开Control与Evolution，自动specialists与少量人审支持局部评价一致性，不提供物理真值或真实闭环控制验证。同一模型的多次judge也不是独立外部证据，遮挡状态、物理合理性和二元阈值仍有误差；追加judge、条件过滤与人审均有费用。不同表的群体与分母不明确时，不合并成配对提升；需要真实状态或安全承诺时，保留受控intervention/可测环境反馈和明确abstain，不由连贯画面或后阶段高条件分数替代完整transition contract。<!-- source-family:SF-2026-ARXIV-2603-13215 -->

当前三处necessary Source/actualowner/逐字PRE已由review_mar17_18正式局部通过；root授窄锁后真实写入Ch29 148/150与注1458、Ch23 332/334与注1680、Ch25 495/497与注1711。作者完整局部顺读/限定diff-check通过；review_mar17_18非writer实际POST顺读Ch29 134–165/注1458、Ch23 321–346/注1680、Ch25 479–513/注1711，回对必要原证与逐字PRE，完整邻接/owner交接/限制保留全部通过。三注已更新实际POST身份/范围，reader定点最终复读通过并通知root释放锁；不授DAY。先前校准错误与修正原证保持上文，不以写入代替验收。
