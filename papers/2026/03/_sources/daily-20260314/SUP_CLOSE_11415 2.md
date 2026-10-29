# 11415 BLooP：最低投入关闭与原文配置反侧

mar14_supplement；精确[2603.11415v1](https://arxiv.org/html/2603.11415v1)，缓存`SUP_NECESSARY_11415.raw`/`SUP_ROUTING_DECODE_MANIFEST_RESULT.json`。两作者、完整题摘/唯一v1、当前Comments LREC2026已实际核；没有具名先稿/纠错/撤回信号，未来会议名不单独证明此前正文公开。owning/findable官方DOI/URL/arxiv.content、registered Mar13 01:55:03UTC与Thu01:14:19UTC v1，结合既有official日程/非预分配规则夹证Mar13BJT，不单以注册/提交作first-public。

原copying需要额外训练/attention→当前token查source intra-sentence bigram后给所有续接token同常数logit boost→局部training-free解码配置。**1+1+2=4**：hash lookup+constant boost是source-conditioned局部选择规则，不引入新事实认证、任务正确性条件、可迁移校准或资源边界；不把复制/采样分责、引用不等truth等成熟原则、新名称或task指标关联加分。窄准入保持，最低投入关闭不是因summarization应用、已有Books或效率安排撤候选。

实际§3.1–3.2 Eq1–4全部、§4.2必要hyperparameter/calibration、§5.1–5.3直接评价反侧/§6.3及B Implementation：提升仅在上一输出token与candidate属于source bigram时加alpha，内部候选集合argmax次序不变，不等完整conditional distribution不变，也不验证relation/truth。先看未boost argmax newline/EOS时不promotion，intra-sentence/tokenizer/stop规则绑定操作点。source也可有错误或正确片段错拼，未给source correctness认证。不同beam/alpha按CNN/DM约1100validation BARTScore调参，training-free不等无校准/compute或严格无标注。

Table1 alpha3/4/6与B声明grid整数−8至2不一致，§5.3/B138又明确称negative alpha，与§3 positive promotion未统一；作者已实际回读该段，原差异保留，不认证已还原精确最佳参数或实现。AppendixB vLLM0.6.1、temp0 deterministicbeam、不同maxprompt64K/4K/2K及A6000一GPU/35GBRAM；O(1) hash查找不是候选更新、beam expansion和总生成恒定成本，未给matched端到端开销。50样本人评faithfulness18/74/8、informativeness48/0/52、readability0/100/0不支持普遍无质量损失；Table2/3若干ROUGE反退，BARTScore与source truth分开。仅记录相关decoder机制，不把SciTLDR论文域效果当暂缓science研究重引入。

**已关闭/仅报告、Books0**；无artifact核验/复现，不授标准实证、普遍faithfulness或无损提速。mar13_admission_review实际必要原证/身份日期和上述具体关闭理由独核通过，见本日SUP_INDEPENDENT_REVIEW_20261009.md；配置差异是保留证据而非另开全代码/版本调查，不授DAY。
