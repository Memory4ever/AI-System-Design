# 11578 Hikari：必要Source与Ch23逐字两段PRE

mar14_supplement。精确[2603.11578v1](https://arxiv.org/html/2603.11578v1)，本地`SUP_NECESSARY_11578.raw`与`SUP_STREAMING_MANIFEST_RESULT.json`；七作者/Comments16pages6figures，currentv2后来IWSLT描述不替v1身份，无具名撤回/勘误/重要修订信号，不做全版diff。Mar13 day夹证`SUP_DATE_THIRD.md`/`SUP_DATE_11578.raw`实际owning/findable+ID/DOI/URL、v1Thu06:08:48UTC与同日registered上界，依官方日程下界，不单取Submitted/Registered作公开。此前2024 causal-alignment工作在本稿§2.4明确继承，新增是speech-native WAIT/time-dilation和delay-recovery接口，不给继承原理新分。

## 实际必要Source / 6分

实际§3.1–3.4机制/数据/运行、§4必要协议与Tables4–5、§5.1/5.3、§6直接限制、AppendixB Alg1全部181–209与C3 Table8全部行。无需全PDF、LLM翻译prompt、其他scale/encoder消融或代码；HTML Table3转换没给完整数值行，本轮不采用其中SOTA/全baseline统一排名，不声称它已视觉核验。**2+2+2=6标准最低**：新增speech与decoder逻辑时间固定映射、WAIT-imbalance和overwaiting训练分工，跨模态表示/可见prefix/生成成本接口；不把普通mask/ASR/SFT加分。已确认Ch23具体差额必要深入该范围。

Whisper-medium初始化，encoder causal selfattention、decoder WAIT(原tilde93)表示READ，text表示WRITE。20ms每audioembedding，decoder一logical slot对应D embeddings；crossattention只允许n≤D(m−1)。D1/2的WAIT占多数与重复过等待，D4本实验80ms slots/375decoder长度；高D降低AR forward和WAIT但压缩text容量/时序粒度，不保证任意快语速都fit。AppendixB以timestamp+独立0–200ms jitter和单调max index插target tokens，unmatchedword延期到前label后；if t_start<l才写入，溢出位置不会自动恢复，训练padding与token budget必须保存。与真实simultaneoushumanparallelcorpus不同，62.3Kh转录/LLM sentence翻译/embedding alignment以及4task均匀训练有paid supervision。

SFT采pivot并将后文text右移Δs、靠WAIT空间延期；history和人为插入WAIT的loss mask，不训练模仿等待，以70%原始+30%延期样本训练catchup。96H100/每device128/gradacc2、pretrain35K与SFT2K加成本；权重precision/全pipeline wallclock/在线arrival/concurrency/SLO及seedCI未完整披露，不认证实现或复现。Inference greedy、30s audio rolling与375text slots并保留四prompt，去旧history意味着不授无界语义保持。WAITlogit bias还能改变quality-lag曲线，policy-free仅无独立READ/WRITE模块，不是没有等待policy或external runtime。

Table5 HQ en-de selectedbase44.22BLEU/2.96lag→SFT35.74/2.08；IWSLT en-de36.61/2.93→31.56/2.30，平均差也负；低latency改善不授blanketqualityparity。Figure6“expected”latency强制reference output是oracle诊断，实际generated/CA lag和deadline不同。Table4 ASR WER8.6/19.9/16.2/54.1全逊所列强baseline；作者domain原因是解释，不证明架构唯一正确或只scale数据必修。C3 removingASR全部BLEU/lag退，支持multitask acoustic anchor但不授所有部署任务。单A100/H100 RTF figure/text仅作者负载，precision/在线SLO不能补造，D4实时batch文本不等完整服务高并发保证。

## actual owner差额

ROADMAP `MULTIMODAL-REPRESENTATION`/Ch23；actual1048–1080完整Streaming Multimodal Identity→可中断时间state及相关邻接，Ch22/24入口与Ch24 525–561 objective/commit段已读。现Hibiki training时序support、closedform输入mask与runtime commit、双KV/trigger分责已覆盖通用causality，但缺**以WAIT/text同词表输出同步READ/WRITE、D将audio时钟映射decoder slot预算、过等待人工延期但mask掉延迟模仿loss**这一speech-native可见prefix/label identity接口。不是缺泛runtimecontroller，故后文不扩实现状态机。

拟Ch23 Hibiki两段后/提前发声DDTSR前两段，root实际必要原证/PRE后才写。原sentence-level/word-aligned等待与externalpolicy均保留，Ch24仅继续接generation/commit，不跨owner重复。

## 逐字提案

流式语音还可以把“再读一点”与“输出文字”放进同一个训练词表：WAIT 表示继续消费音频，文字 token 表示提出输出；同时用因果 encoder 与 cross-attention mask 限定每个 decoder 位置能读到的音频前缀。这不是取消等待策略，而是让它与文字条件分布共同学习。一个 decoder dilation 参数把若干音频 embeddings 对应到一个逻辑输出 slot：间隔越短，对齐更细，却会让 WAIT 占据标签和 autoregressive forward；间隔越大，文字可用 slot 更少，快语速可能溢出。timestamp、alignment、dilation、prompt 占位、WAIT padding 和溢出处理应共同成为表示合同，不能把训练标签的时序对应升级为真实到达、内容正确或 runtime commit 证明。

过等待后的恢复还可单独训练：把一段文字标签向后移，制造累计 delay，但将人为插入的 WAIT 与此前历史从 loss 中屏蔽，使模型学习后续 catch-up 而不是模仿延迟；部署仍用有界音频/文字窗口，WAIT logit bias 只是质量—等待曲线的调节器。[有限语音对照](https://arxiv.org/html/2603.11578v1)中，延期微调缩短 lag 但若干翻译切片的 BLEU 退步，辅助 ASR 与 alignment、标签合成及额外训练也有成本；oracle 输出的理论 lag、generated lag、包含计算的 lag 与设备 deadline 必须分开。窗口丢失、alignment 漂移、长期 WAIT 或文字溢出时，保留外部 READ/WRITE policy、完整句等待和可复查 transcript，runtime 继续拥有交付与取消权限，不以“policy-free”或低 RTF 授予无损实时服务。<!-- source-family:SF-2026-ARXIV-2603-11578 -->

Review note拟：精确v1 §3/4/5.1/5.3/6、Tables4–5、B Alg1/C3 Table8；D/slot/WAIT训练与真实arrival分责，delaymask不模仿插入WAIT，BLEU/ASR反退/完整费用近文。root Source/PRE与actual POST待执行，无artifact核验或复现，不授普遍causaltruth/实时SLO/DAY。
## root实际必要Source / PRE结果

root独读本packet与精确v1原件已提取的§3.1完整dilation/mask、§3.2数据对齐与B完整Algorithm1、§3.3.2延期lossmask和§3.4运行、§4.1协议/§4.2 oracle区别、Tables4–5、§5.1/5.3与§6、C3/Table8。实际Ch23 streaming完整邻接已顺读，Hibiki support与后续DDTSR/closed-form可见prefix已有，但不替WAIT同词表/slot容量与人工延期loss分责；6分差额深入与逐字两段PRE通过。Table3缺数字不扩PDF排名，reference强制oracle曲线不当实际lag/CA/设备deadline，Table5 en-de退步与窗口/标签溢出均保留。

root已实际把两段插Hibiki后/DDTSR前，原正文有效内容未删，章末本人note暂待实际非writer POST。作者可真实顺读新正文、完整局部邻接及自身末注并回对原证，未授全日报完成。
