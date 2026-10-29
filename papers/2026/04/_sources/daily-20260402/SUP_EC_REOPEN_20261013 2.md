# EC-Bench `2603.29943v1` — 决定准入的必要原文

原Batch4拟EX仅以新dataset/相关性不足作理由，root指出finalcount可能漏instance/timeevidence的评价盲区，已局部重开，不要求所有benchmark因果干预。作者已实际完整必要§3/4和短§5，[原件](SUP_EC_DECIDER_20261013.json)；未看22模型所有视频、附录或代码。拟改准入 `2+1+2=5`，待root实际决定，不从费时改分/缩池。

## 原约束 → 实际对象 → 拟改选择

最终数值只验聚合结果，不验哪些实例/何时支持；§3.1明确要求Enumeration列完整相关instance set（漏/重计分）与原timeline evidence spans，Counting输出int也要求spans。§3.4另以list TP/FP/FN→precision/recall/F1、count exact/MAE与temporal IoU分别消费annotations，是可改变评价输入/对象的接口，不只是metric名字。§4.4实例显示generic category代替具体列表、worldknowledge代替6:54真实visual list，可定位对象/证据错误；不声称原文展示了每个“count恰对但证据错”的全部因果路径。数据由Gemini初生成、人类改与第二annotatorcrosscheck，非不可错goldtruth。

## 必要界限/反側

152video>30min，1699openquery，timestampframes+Whisper-large-v3 transcripts，非纯video/任意长context结论。主表各model64/80/128frames与context适配不同，不作严格等成本rank。§3.4Enum是F1，而§4T2/caption统称accuracy，必要metric口径不闭，不采用其exactEnum百分比作所有正确实例证明。

LLMjudge100Enum人工相关ρ=.8233，不证明所有item语义/重复匹配、otherpopulation可靠。tIoU将multi-spans合并成singleinterval，只整体支持范围，不认证逐instance匹配、gap、顺序或causal过程faithfulness；未核代码具体union/hull实现。Enumeration-first四model在同数据上count/MAE改善，但额外output/token/search预算未披露，不将它独立归因为grounding或免费capacity；frame128→512后收益不单调是受限反側。跨模型ρ=.692及span/quality相关不证明bottleneck因果，作者“primarilygrounding”解释收窄。

拟只保finalanswer/instance/temporal支持对象分离及测量边界，不采用新bench规模=贡献、最高rank=生产能力、partiallabel/整体tIoU=完整过程正确。Books尚未比实际owner，不自动整合/已有覆盖；normalSubmitted与conference/project早公开定点日门仍必要，未先加确定新增分母。
