# Qwen3-ASR-Flash：作者必要证据与拟处置

作者Mendel，实际复读时间2026-10-06T14:06:05+08:00。本记录供root首批准入及证据独核，不能替代独立裁决。原FIRST中“未读性能图”是较早停点；两原图现已实际查看。没有实现核验、听音标注核验或复现。

## 身份与公开事件

本日原`QWEN_CONFIG.json`中的id `qwen3-asr-flash`，原date `2025-09-08T06:38:04.000Z`，即2025-09-08T14:38:04+08:00，完全落本日窗。对应[官方Blog](https://qwen.ai/blog?id=qwen3-asr-flash)和[token正文](https://docs.qwenlm.ai/research/qwen3-asr-flash/index.json)，本地原响应`QWEN_ASR_CONTENT.json`。不是submitted或搜索收录时间。性能原图版本标识`Qwen3-ASR-Flash-0908`，脚注API tested in August 2025。正文末尾说明服务持续更新；本次不把当前API调用映射为冻结2025权重。

## 问题、披露与未披露机制

完整正文的Key Features、Contextual Biasing、Demos及末尾服务更新说明已读。发布说明的增量是：不要求把背景材料先加工为特定hotword格式，可接受关键词、段落、混合文本，并披露语言识别及非语音拒绝接口。它可能影响ASR条件输入的设计选择，因此不能只以“多语种新服务”或已有ASR主题排除。

但正文没有解释任意格式context的编码、音频与文本冲突处理、训练目标或拒绝阈值。正文中“any length”“unrelated context hardly affects”等是厂商主张，不是本次已经证明的条件。我的推断仅是该接口值得分别测试专名收益、提示诱导错误及非语音输出，不能反写成作者公开的新算法。

## 对照、收益与反侧

原性能图`qwenasr-res4.png`实际查看，比较Gemini-2.5-Pro、GPT4o-Transcribe、Paraformer-V2、Doubao-ASR。公开集按Chinese、Chinese Accent、English、Multilingual、Entities、Lyrics分组，列出WenetSpeech/Fleurs/SpeechIO、LibriSpeech/MLS/Gigaspeech等数据来源；这里保留图的“Error Rates”口径，不自行统一所有组的CER/WER和聚合权重。

图中内部AccentHard为413条heavy accent/extreme noise语音，Qwen19.37而Doubao13.88，反驳“所有困难环境都领先”的外推。LangMix是2000条11语言随机拼接语音，不等价自然会话code-switch分布。Paraformer多语种只有5/9语言，14.18的分母与Qwen5.77不相同，不能合并为严格九语种排名。其他所列局部结果仍可保留为作者报告，不因这一反侧抹去。

原`res-csgo2.png`实际查看：同一解说转写，context可为hotwords、包含不在语音中的hotwords、自然语言队伍信息或无序统计文本，图中给出统一的专名拼写改写结果。它没有四类context各自的配对错误率、无context重复运行、错误context/无关长文干扰消融，也没有非语音拒绝的false-positive/false-negative曲线。六个Demos仅Example2有context；本次没有听音确认ground truth，不能称准确性复现。非语音拒绝只采用“厂商披露该功能”，不采用可靠性保证。

收益可以描述为官方示例展示专名转写受背景文本影响；是否因自由格式接口而优于传统biasing、是否同时保持一般识别和拒绝边界，当前材料不支持因果归因。也不能将跨模型总榜差异归因于context接口。

硬件、precision/quantization、batch、concurrency、SLO、运行时、输入输出长度限制、训练配方、重复运行及不确定性为`Not Disclosed`。图未提供成本/延迟可比条件，不采用服务效率结论；对于API能力说明这些缺项不阻止记录披露事实，但阻止性能和安全外推。

## 拟评分与Books决定

首批准入若通过，评分命题保持接口与偏置/拒绝边界的具体潜力，拟Design Delta 2 + System Reach 1 + Durability 2 = 5；不是给11语种数量或机构声望打分。不因证据较窄降分、删反侧或自行删除拟候选。必要原文、对照图、context图和直接限制已取得，足以让root判断该具体命题是否达到准入及标准审阅要求。

拟Books处置为“仅报告”：当前新增事实是版本服务接口与有限作者例子，未披露可独立保留的条件编码/拒绝机制或经过控制的适用边界。不是“已有覆盖”，也不是“没改变通用原则”式排除；不宣称任何owner现正文已经承载本项。若root认为图中的局部反侧足以修正现有具体论点，再只读对应owner及邻接提出窄差额，当前不预造Books改动。

作者侧已无缺失原图/正文等可执行证据读取；剩余普通工作为root独立首批校准及必要反馈同步、最终DAY。若原公开版本或可比context/拒绝实验以后到达，定点重开相应命题，不重扫其他源或全日题摘。
