# Word Recovery 2603.10771v1：必要 Source / actual Ch11 / 中心因果资格暂缓提案

本日只补Mar12 BJT自然日，SUP_ABS3_10771/独核§19窄准入、§23日期有效复用。本次实际回读四作者/完整v1题摘/current history：v1 Mar11，v2 Aug4，无Comments纠错/撤回或明确重要修订说明，不因有v2无差别版本比较。DATE3实际Submitted11T13:49:14、created12T02:09:26/registered12T02:09:27，配官方公告批次夹Mar12，本次不用Updated或月份单独认证公开日。HTML Keywords:Machine Learning,ICML不是接受/早公开日期证据，不据泛会议词扩历史。

official exact-v1 https://arxiv.org/html/2603.10771v1 GET200/216784B/UTC2026-10-10T03:25:13.745692，SUP_CORE_10771.raw/txt/MANIFEST_RESULT保存。实际读完整§2–5、§1/Table1全表、AppA/B完整定义/直接资格说明及§7结论；另从raw MathML alttext对回原投影公式，确无norm denominator/单位方向定义，不凭txt丢公式。图只读正文/caption，未视觉Figure2–11的curve/pixel，因此不采用精确drop幅度/峰层/显著性；没有读v2或代码/复现。必要反侧已够，不造普通未读或无实现blocked。

## 增量与三维

相同字符串的canonical与character token序列不同行为，旧行为鲁棒观察不能解释内部如何补偿→此稿把原canonical token身份的hidden-state读出，与该token方向/字符组注意干预相连→需要区分身份可读、表示被损伤后的任务变化，与“内部恢复是唯一/必需中介”的因果采用资格。不是仅tokenizer主题或一般logit lens/ablation原理贡献。

拟2+1+2=5：D2计本材料新增的字符输入补偿路径与必要性边界/反证；R1只模型输入与内部局部负载，不靠tokenizer/attention/平台节点数量抬Reach；Durability2计可复用的读出单位、扰动方向与因果资格，非小模型规模/访问状态扣分。中心“causal necessary word recovery”桥接争议触发必要受影响深入；结果暂缓Books0，保候选不缩池，不把成熟投影公式或一般probe≠truth额外计分。

## 读出身份与有限正结果

§2三instruction模型Gemma2-9B/Qwen2.5-7B/Llama3.2-3B，四英文MC QA ARC-E/C/CSQA/OpenbookQA，不微调。character-level保同decoded文本，canonical每token对应字符span，但实施如何映射Unicode/特殊token及chat-template边界、样本数/截断、评分prompt、硬件/precision/batch/seeds/CI、成本和SLO在必要段Not Disclosed，不造语料全量/算力匹配。

§3 Wout读每字符hidden的top5，全位置union，与输入canonical**unique token set**交集比率；去重复，既非逐instance恢复、正确位置/次序、更非理解准确率。AppA K1/2/3/5/10/20、AppB限制原span读出保定性曲线，对全位置偶然命中的一类替代解释有帮助，但span存在/可解码仍不证明读取就是任务唯一计算中介。AppendixB set去重与重复token span如何选择未完整明确，不补造实现。§3所称universal仅所测12model-task点，不外推全LLM/语言/随机分词。

Table1直接反侧：Llama ARC-E canonical88.6下降35.8个百分点，recovery72.2；ARC-C76.6下降33.8、rec73.6；CSQA73.9下降33.4、rec57.7；Openbook77下降30.8、rec60.5。Qwen/Gemma较小下降，GemmaCSQA80.7下降5.9且recovery96.4。身份读出高不等保持能力，不能“鲁棒”变无损保证；不由负侧否定存在补偿。

## 两个中心桥接停点

1. §4定义w_t为原output embedding、公式h←h−<h,w_t>w_t，没有说明||w_t||=1或除||w_t||²。内积更新只在单位方向下是正交移除。有限h=(1,0)、w=(2,0)给h'=(-3,0)，<h',w>=−6，不是移除方向；一般< h',w>=<h,w>(1−||w||²)。这里反证的是**字面公式无额外条件就“remove contribution/preserve orthogonal”**，不是证明作者实际代码一定未normalize或任务降分伪造。精确实现/归一化到达可修该层，不推全部实测无效。
2. §4从起始层持续干预到final，early起点也增加干预层数；§5同样从起层持续mask同canonical-span全j,k（含self），把组内pre-softmax logits置−∞。原称“without affecting attention across different groups”只在未mask logits层成立：softmax分母缩小，组外概率一般增加，内容路由也改变。第一位置若无BOS/其他合法key会全mask，**但实际special/template未披露，不声称实际NaN**。所读§4–5与两Appendix没有same-duration/per-layer、等范数随机方向/乱配token方向、同mask边数/out-of-group对照或恢复救援，不能把累积扰动/注意重分配影响排除后自授“word recovery necessary/非直接character reasoning”唯一桥接。这里未要求所有机制必须用统一模板，只指出本强主张依赖的特异性未被当前对照确认；保原targeted span/方向干预与层相关的有限证据。

正文给early intervention掉分与late少影响、early5layer组内mask降低recovery，有限支持相关表示/组内通信参与计算的作者观察。不得由上述资格缺口宣称模型已无word recovery或所有字符理解无因果联系。未读曲线不填具体峰层/干预数值；精确实现可选，不是本受限处置永远等待条件。

## actual唯一owner与本次Books

MODEL-TOKENIZER Ch11，实际顺读完整1–61：tokenizer是ids离散接口、char更长但不是语言唯一词法；214–239监督单位/跨tokenizer信息计量与probe未读出不证不存在；346–362 Homotokens附加encoder/canonical target联合输入、same decoded string不授内部计算/行为等价，以及vocabulary迁移上下游。现文承载分词粒度、计算/监督、probe与语义身份资格，**未吸收本稿方向干预/组内attention的新实验或必要性定理**。Ch12只交接embedding数值，Ch14只交接mask/softmax，Ch17只交接residual读出，不以多章节映射增加owner。

中心“必需/唯一恢复中介”的因果与recipe身份尚未闭合，拟争议/暂缓Books0，而不是以主题覆盖自签新成果已吸收；不写新的强机制段或PRE/POST。不采用精确projection recipe或建议线上mask。既有canonical tokenizer及经真实任务回归的char路径继续共存，不能因恢复score而热换checkpoint输入。

## 精确重开与最小停点

只在拟采用必要性时重开：提供原token方向归一化/实际更新和层/位置协议；将读出unique/type与逐instance/位置分账；同干预预算/等范数或边数控制、恢复/其他能独立排除一般损伤的证据，及对应字符任务人口/费用。接受作者精确原方法补充或独立匹配干预原证，不要求普遍全语言证明，也不扩旧论文/完整v2或所有图。

本篇5分必要受影响内容深入已做、拟安全争议终态Books0交非准备者核；未formal、未DAY。其他有效题摘/date/局部经验保留，不把中心争议改EX/降分。
