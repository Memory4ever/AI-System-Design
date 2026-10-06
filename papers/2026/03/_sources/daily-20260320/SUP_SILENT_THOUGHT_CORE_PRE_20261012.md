# 03-20 Silent Thought17837：必要源与最小流式表示差额

准备者resume_mar17，2026-10-12，仅03-20补03/19自然日。已重读实际AGENTS/当前研究与Report合同、Sources使用/每日与arXiv主题、Prompt、ROADMAP/本日README/STOP/最新路由；Books的PROJECT_CONTEXT、LEARNING_PHILOSOPHY、WRITING_GUIDE与实际owner/相邻入口已读。身份/日期/2+2+2=6准入复用[九尾原packet§5](./SUP_AGENT_TAIL_ADMISSION_PREP_20261011.md)与[原DOI日字段](./SUP_FINITE_TAIL_SCREENING_20261012.md)。当前v5轻量acceptedICML说明不触发全版本diff；下面只exact-v1必要接口，不自授Source/PRE或Books通过。

## 1. 实际源范围与停止

[exact-v1 HTML](https://arxiv.org/html/2603.17837v1)：实际读§3 L98–118基线、§4 L123–166完整方法/Eq5–13、§5 L167–177训练阶段、§6–7 L178–239/T1–3关键评价与讨论。与采用直接相关的C L356–371合成/真实语音人口与打断标签、D L373–379骨干/帧率/训练配置、E L380–390预训练指标及401–407encoder/expert/synthesis反侧已读。未读references/代码/全部proof，不冒图像像素、全case study或独立实验复现；支持与直接反侧够本有限表示分支即停止。AppendixB L343–355仅在原返回中实际读到conditional ELBO文字，用来区分全局后验教师与因果prior，不采完整变分等价证明。

## 2. 真实接口与不采用的强桥

基线full-duplex听取时使用固定SIL文字表示；本分支每步文字logits经softmax对词表embedding加权，形成连续混合Z，下一步与新语音表示相加消费。不是任意previous-hidden直接循环，也不是用户音频已经含未来答案。训练global-aware expert非因果地读全段语音及assistant目标文字，输出词表分布/连续混合；说话位置用重建CE，听取位置用教师stop-gradient词表分布与模型分布的KL，另训MLP时序head/BCE。训练阶段full-target教师是监督，部署移除教师；预测说话则下一步用离散文字embedding，预测听取则用连续混合，并向语音生成支路送SIL。LLM hidden与文字条件仍被speech generator消费，不将文本隐藏状态等同外部声音已提交。

这改变listen-step表示与条件训练，不授“真正认知”的唯一因果机制。词表KL是具体训练代理，formal连续latent后验的ELBO解释不等同本文已证明所有实现满足该密度/变分等价；不采用精确理论或完整配方。原文chronological与encoder causal-conv说明仍须落实到实际可见prefix；E401明确保ASR默认context，未披露完整未来lookahead/异步arrival trace，不能用去掉全局教师就签发端到端无泄漏证明。该必要边界不阻塞有限接口本身，精确runtime因果审计另需arrival/encoder窗口/commit trace。

## 3. 关键评价、反侧、配置与全费用

FLAIR的同模型有/无latent对照比不同系统更相关；T1 TriviaQA53.8→51.2退，其他多任务增益不能抹此反侧。T2 Impatient turn-taking latency .33→.39退；T3 CANDOR turn-taking TOR94.1→93.0、latency .37→.43退，barge-in latency .35→.36亦退。外部baseline由已有论文/不同训练与回答长度拼表；不把宏均值当无损或同预算普遍优胜。部分开放质量由GPT/judge和Whisper转录评价，不是独立raw-audio内容真值；tSNE300示例不证明latent为推理的唯一因果中介。合成打断训练8token≈.64s后强制EOS，部署text EOS时audio强制SIL，训练标签时序不等真实设备停止播放deadline。

D明确Qwen2.5-7B-Instruct/Parakeet600M、冻结speech encoder/codec、LLM与encoder12.5Hz/codec25Hz、64 A80080G与BF16训练；不虚称这些ND。但推理硬件、batch/concurrency、prefix/lookahead、完整延迟分布/SLO与CI/重复训练成本未给足。E120M→600M容量/hidden对齐一起变，不授单因素原因；T5-Large与BERT近同，T5-3B小收益增加费用；MOS4.2vs4.3/小AB偏好不授所有后端等价。全局教师、530K+70K+20K小时合成/ASRQA与TTS、阶段SFT、词表混合矩阵乘、时序head、encoder/KV/codec、评测生成和judge均计费；“noadditionalinferencecost”不等全pipeline或所有deadline免费。没有代码或生产复现。

## 4. actual唯一owner及最小literalPRE

actual Ch23完整1108–1131、554–572已读；Ch22/24入口1–20已读。唯一owner `MULTIMODAL-REPRESENTATION` / [Ch23](../../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)。原full-duplex channel fusion拥有输入可见/commit分责；HibikiZero1114–1116拥有监督时序支持；WAIT1118后拥有逻辑slot/读写策略；都未承载听取位置词表混合反馈与full-target教师只训练、部署时序head选混合/离散输入的具体差额。拟**HibikiZero完整限制段1116后、WAIT分支1118前**两段，不接管生成范式/turn-runtime或新增认知章。以下未经独立Source/PRE通过，不授写入。

全双工模型在暂不发声时，也不必始终把固定的silence文字表示反馈给下一步。一个表示分支将当前文字logits的softmax分布对词表embedding加权，得到连续混合，再与新到达的语音表示一起消费；训练时用能读完整语音及目标回答的非因果教师，为听取位置提供词表分布KL监督，说话位置仍重建目标文字，另训时序head区分两种状态。这份完整回答是训练标签，不是部署已听到的内容；[Silent Thought的必要接口](https://arxiv.org/html/2603.17837v1)在部署移除全局教师，由预测时序选择下一步的连续混合或离散文字表示，听取时向语音生成支路提供silence条件。它改变的是听取期间的表示递推，不是让内部混合向量直接成为已播放声音、事实证书或输出提交许可。<!-- source-family:SF-2026-ARXIV-2603-17837 -->

这个分支仍须与实际到达的prefix、encoder窗口和语音输出时钟共同验收；去掉训练教师不自动证明所有前处理没有lookahead，也不能把词表KL代理提升为真实认知或完整变分等价。有限同模型对照中，部分知识任务、turn-taking成功率与延迟会退步，合成打断后的EOS/silence规则也不等设备实时停止保证。教师和合成数据、词表混合、时序head、encoder/KV/codec及独立质量评测都有费用；外部系统表格、宏均值或小后端偏好样本不授无损、零成本或普遍deadline。表示或时序失配时，保留固定silence、离散文字、完整句等待与保守turn-taking，实际播放、打断和commit/cancel仍由runtime决定。

静态注literal：

- `SF-2026-ARXIV-2603-17837` — [Silent Thought exact-v1](https://arxiv.org/html/2603.17837v1)必要§3–7/T1–3及C打断/数据、D配置、E直接消融。只听取位置词表混合反馈、全局教师训练/部署移除及预测时序的表示接口；保训练target非部署观测、encoder/prefix时序、KL代理非认知证明、任务/延迟反退和全费用，不授无损/零成本/端到端无泄漏或deadline；未核代码/复现。

## 5. 下一可执行位置

交具名非准备者一次必要Source/actualowner/两literal与static核；准备者不自授PASS，不写Books，root确认soleCh23窄ownership后再写。原6分不变，独核前普通待办不称外部受阻，本Report未DAY。

## 非准备者必要 Source / actual owner / PRE

root 独立恢复合同后实际读取 exact-v1 §4/Eqs5–13、Tables1–3/评价协议，以及 C 的打断标签、D 配置、E 的 encoder/教师/后端直接反侧。当前 v5 仅作轻量状态入口，不拿其后发日期或内容替换本次 v1。连续状态来自词表分布加权而非直接 hidden 循环，完整目标教师仅训练可见、时序预测切换部署输入，原证与两 literal 一致。任务及 turn-taking 反退、训练标签与物理停止的区别、默认 ASR context 未完整认证 lookahead，均已限制正面采用。

actual Ch23 1095–1140 完整局部回读：Hibiki 的监督支持后接此听取表示分支，再交 WAIT 的显式读写日程，不覆盖任一已有机制；唯一 owner 及两 literal/static 有限通过。准许作者 sole Ch23 窄写；未实际写后复核前不记整合或整日通过。

## 非 writer 实际 POST

root 实际顺读 Ch23 1108–1136 与末六行中的本人静态注和相邻 SEM 注，回对原两 literal/static 及必要原证。新增 1118/1120 保留固定 silence 的成立条件、训练完整标签与部署 prefix 分责、KL 代理与时序反退及全费用；前 Hibiki 的监督时序和后 WAIT 的读取日程没有覆盖或删改。一次实际非 writer POST 有限通过；接纳整合并释放 Ch23 窄锁，未授整日 DAY。

## 6. 已授权实际窄写与作者读回

root非preparer有限PASS及soleCh23窄锁后，resume_mar17按原两literal实际写1118/1120与自身静态注1746，SEM邻注保留。作者实际完整1108–1136及末6顺读，回原两PRE/static逐字一致；限定diffcheck0。只两段+静态注，无身份验收收据写进Books；等待root一次nonwriter实际正文/完整邻接/本人及邻注POST，不自授safe/DAY。
