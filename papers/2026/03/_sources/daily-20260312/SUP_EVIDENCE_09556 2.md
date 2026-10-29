# 2603.09556 — 多音频接口的主流保留与旁路融合（Source/date/PRE/actualPOST通过）

[ALARM: Audio-Language Alignment for Reasoning Models exact-v1](https://arxiv.org/html/2603.09556v1)。作者actual完整§2.1/2.2/3/4/5、Tables1–5文字，S2早次截断的CA/P/E与S3已定点完整恢复；未核Fig3 radar像素、代码或复现。root原batch3完整AB窄准入已过。current仍v1/Submitted to Interspeech2026、完整题摘同原，无已见撤回/纠错或先公开信号，不扫venue或旧参考稿。

原batch3 actual arxiv.content owning/findable registeredMar11UTC02:16:25为已可发现上界；SubmittedMar10UTC12:03:25配actual官方availability noadvance最终ID/DOI与最早Mar11BJT08下界，同一BJT日夹证03-11；不由Submitted/Updated/注册单独作公开。

拟2+1+2=5；具体融合接口gap必要深入，唯一MULTIMODAL-REPRESENTATION。采用固定primary连续流与互补压缩流分路、真实负侧及target-provenance边界，不授纯声学grounding、所有条件无损或免费冻结。

## 必要机制、target与原文冲突

§2.1现有文本metadata生成20候选问题，用同Qwen3-30B-A3B-Instruct2507FP8再过滤metadata可答/不暴露文本措辞，uniform取一。冻结4B Thinking基座先从metadata生成R0，再自rewrite推理与答案成“我听到”style，rephrasing thinking预算1536；rewrite内部thinking不进入target，但原生成推理经改写仍监督audio adapter。metadata可答不证明raw audio可辨，听觉措辞不把文字derived标签变观察真值；同模型生成两次不证明conditional distributions相同。Table2只是例子，无必要controlled self-rephrase/真声学干预消融，不采“保持分布/grounding已证”。HeySQuAD转录问题例外不rewrite，合成/filter与heldout分别计费。

§2.2 frozen encoders/LLM，层softmax加权：Whisper语音、W2VBERT2通用、MuQ音乐、SSLAM环境音。多层读取、50→25Hz conv(除MuQ25Hz用MLP)不是encoder重新学缺失细节。CA固定Whisper→W2V→MuQ→SSLAM，每次2层crossattention上一输出query，最终25Hz；P保留25Hz Whisper主流，其他三encoder各20 Perceiver tokens成60固定prefix，附trainable分界；P不能只按25Hz计算总长度。E inference-only把独立训练CA25Hz及Whisper-Instruct25Hz时间拼接，Ie/I1/I2分源prompt形成50Hz，不是训练joint50Hz，也不是证明两个独立实际decoder passes。175Hz只是四流naive时间拼接预算，不是原所有单encoder基线成本；多encoder提取并未省掉。

§3 CA预训练各singleencoderadapter后冻结除fusion外，all数据1epoch；P冻结Whisper-Instruct单路并从零训Perceivers，E用这两既有模块。数据random10%按instance分val，HeySQuAD官方split；是否speaker/录音派生组、共享来源与benchmark contamination完全隔离未独证。一般effectivebatch64/2epochs(另述singleencoderbatch32)、AdamW1e-4/cos1500warmup/4H200；CA1epoch/P与单路不同训练人口和初始化，故并非仅融合算子单因素matched。precision/训练seedCI/全预制时长/峰值memory/完整latency并发SLO NotDisclosed。

## 关键评价、直接反侧与费用

Table3 MMSU5000/47tasks：Whisper-Instruct perception38.2/reason73.6/overall55.3，CA39.6/68.3/53.5，P38.4/74.2/55.8，E45.4/78.3/61.3；更丰富融合可损语义，E有限恢复，但不能由不同训练/容量归唯一压缩损失。Table5 MMAU v05.15.25 1kmini/9ktest，E speech77.2/73.7强；soundCA66.4/61.1高于E64.0/59.1，musicCA57.2/53.3 vsE54.8/54.2亦混合，MMAR1k E48.7低于Whisper-Instruct49.1。不是每任务/领域新方案最佳；跨模型数据与decoder/预算差异不授200x token→200x总费或普遍榜单当前胜。

Table4文本74.0/86.1/65.8与冻结4B一致仅支持保持纯文本原路径的有限读数；冻结权重不保证audio prefix/prompt改变条件时无干扰，也不认证bitwise图/全部文本能力。原其他模型full-finetune退步不足以证所有必须冻结。§4.3明确单encoder不同数据/epoch/接口组合，AIRBench文字MIDI-pitch单MuQ仍优；不采用Fig3精确点数或非matched因果。§5承认fusion需要按domain选择，支持有限分支停止，不遍历参考系统全文/附件。

metadata制备/问题生成与过滤/两次selftarget、四encoder及多层activation、各adapter预训练/fusion、60prefix或50Hz reader input、长thinking和独立任务回归全计费。冻结只省参数更新，不省全forward、到adapter的backward或部署encoder；tokenrate不能代完整设备性能。

## actual owner 与逐字 PRE

作者actualCh23 64–101 encoder/projector及covariance/readout、136–172接口/深层adapter→音素→MAEB/probe/filter/MUGEN，Ch22/24开篇。已有MAEB encoder信息身份和closed-gate原图边界，不拥有“fixed primary不被共同CA覆盖，互补流单独压缩/拼接”的具体audio融合分支。拟仅Ch23 gated-deepadapter完整段后/音素接口前两段；保留全部现有机制。

拟段1：

多种 audio encoder 的互补信息也不必先压成同一条流：共同 cross-attention 可以减小入口长度，却可能同时削弱原语音内容接口。另一条分支保留经过既有 adapter 的连续语音主流，只把音乐、环境声等互补 encoder 压成定长旁路，再以明确边界和来源顺序交给同一 frozen reader；也可以把已训练的融合流与主流并列输入，以更长入口换信息保留。Encoder/层选择、时间压缩、旁路 slots、融合顺序、分界 prompt 和各 adapter checkpoint 共同定义接口，不能由维度对齐或更多 encoder 宣布所有声学信息无损。

拟段2：

这种分路用额外表示和 reader tokens 换局部质量：[必要融合对照与直接反侧](https://arxiv.org/html/2603.09556v1)中，共同压缩的语音推理会退步，保留主流及并列分支在部分任务恢复，但环境声、音乐或其他推理切片仍可能更差，训练人口和初始化不同也不能只归融合算子。固定旁路 slots 要加在主流长度上，多 encoder 与更低合计 token rate 不消除编码、adapter 制备、融合、长输出及回归费用。冻结 reader 只在复用原纯文本路径时避免权重变化，不保证新音频前缀无干扰；从文本 metadata 自生成再改写成听觉口吻的 target 仍是派生监督，措辞不能证明 raw audio 真值。应分别验收语音内容、非语音感知、纯文本与总预算；旁路丢细节、源身份不可信或质量—成本失配时，保留原单 encoder、专用 readout 或连续配对适配，不让更自然的 trace 代替 grounding。<!-- source-family:SF-2026-ARXIV-2603-09556 -->

实际自身末注与写后：2603.09556 exact-v1§2–5/Tables1–5必要机制与直接反侧，2+1+2=5具体primary/sidefusion gap深入；P固定60额外tokens/E inference-only50Hz、合成target非rawtruth、真实任务反退与完整费用保留。root非作者必要Source/date/PRE通过，作者实际写Ch23新151/153与本人1259后顺读；root非writer实际读143–171完整局部及自身注actualPOST通过，锁释放。不授全图/代码/复现或productionSLO，未授DAY。
