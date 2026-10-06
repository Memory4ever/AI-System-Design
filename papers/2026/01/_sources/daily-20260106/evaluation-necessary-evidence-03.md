# Jan06 评价必要命题停点（三）

仅既有本日线索的必要精确v1原段，不扩新主题库存；三项是否最终准入/Books由root实际窄核，非日级通过。

## WildAGTEval 2601.00268v1

新增分spec与execution复杂度，assign/inject改API及相应gold，再区分gold-prefix孤立评价与真实predicted-prefix累积；拟2+2+2=6，因为评价盲区/设计反证读必要核心。实际§3/4/5/Limitations、AppendixB，原cache完整必要段。300conversations/86APIs/60scenarios是构建范围，实际stratified50用于评价；32K是潜在组合，不是全部运行。主prompt约34K specification+19Kguidelines、ReAct、每turn15step；Claude Bedrock与其他vLLM p5en，不授统一hardware/precision/线上SLO。

coreAPI set与gold exact agreement为API-call metric，supportcalls不直接计分，所以重复support与合法另一顺序不能由该分数证明正确或高效。Claude4Opus错误处理ordinal judge不是真实effect真值；AppendB主文与reference同时接受alternate error reporting。Gold-prefix对照不等free-running累计可靠性；Base*已经有dependency/ambiguous-documentation，不能叫全复杂度zero baseline。用户目标被错误替换、endpoint猜测是受限API执行实例，不授真实客户事故率。

当前Ch81 Testing 895–938 structural/outcome分账、Ch78 397–411 outcome monitor/recovery读过；root恢复后实际重读Ch66 1295–1320 WildAGTEval核心与相邻，原spec/execution分相+gold-prefix孤立与累计测试已有承载，具体Existing通过；保6分准入和标准必要证据，不新增正文，不从主题相似授NoChange。

## CSSBench 2601.00588v1

拟2+1+2=5，中文surface variation与native border拒绝测试的安全评价盲区；实际§3.1–3.4/4.1/4.3/Limitations。四curated中文变体、三task formats、十≤8B，greedy、64/256生成上限/batch16、A100/Ascend910B；不授所有中文/多模态/无限变体语义保持或更大规模鲁棒性。v2 Submitted Jan5T04:37:42Z仅版本线索，未证当窗public，不当v1审完即v2完成。

中心ORR标签冲突：§3.4定义benign/border subset被refusal比例；§4.1却说Qwen3Guard判回答是否safe的binary label作为ORR。安全回答可以是helpful或refusal，故该字段不足唯一恢复拒绝事件，CER的microfrequency加权/整体rank不作正面采用。需exact-v1 parser labels、refusal-vs-safe-helpful mapping、独立human border校准与对应ORR结果；可接受官方勘误/实现及匹配重新计分。该请求只重开ORR/CER，不否认finite clean-vs-variant测试，也不因冲突降分删除。

## YapBench 2601.00624v1

拟2+1+2=5，tokenizer-agnostic visible字符相对minimal baseline的局部measurement；实际§3.1–3.3.2/4/5.1/5.3/6/7。304英语三类别；median内uniform-category average与1000prompt bootstrap，±halfwidth只是非对称interval的显示summary，不授所有model pair显著。76OpenRouter endpoints system absent，temperature0仅可控endpoint否则provider defaults；hiddenreasoning排除/markdown排除，故character metric≠GPU/token开销。

§4明确没有correctness gate，只假设B/C trivial，因此short错误或空回答仍可能拿0 score；不能将excess-character等同已证unnecessary内容或授权缩短输出。YapTax按model tokenizer/Dec31价格扣baseline的均值，与YapIndex类别median不是同对象，亦不是端到端推理成本或实际tokenBill。Dataset internal minimal-sufficiency review无独立label人口，blankpreprocessing/subjective baseline/nonstationarity保留；年龄r.21/输出长度不识别preference-training因果。

当前Ch66格式构念/原分数/切片外代价、Ch70成本都有既有一般边界；root actual§3.2/3.3/4/7与length-bias/quality-cost论证核通过5分标准完成、仅报告可复查的metric contract（baseline+visiblechannel+normalization+categoryweights+endpoint）。没有correctness gate的visible-verbosity度量不形成更短且充分的长期保证，不复制已有质量联合验收原则；不反向降分。

## AEGIS 2601.00561v1

actual完整AB及§3.1–3.3/4.1/4.3/4.5的必要DCE/human-calibration范围，cache00561。多任务1050题/21topics/6reasoning是有界协议，atomicYN checklist经Gemini生成、manual过滤20%冗余、Gemini2.5Pro判断，平均yes不证明响应全正确。4.5只human核10%question的item agreement，Gemini90.7overall/Interleaved83.9，GPT5editing54.8；换judge×task有显著局部差异，但无统一真值/全数据盲标/重复运行校准，不把DCE名称授deterministic output。4GPU具体SKU/precision为NotDisclosed，remoteAPI另分账。

原§4.3从不同model性能推dataquality唯一因果与understanding是generation严格上界均不成立；clear vsreasoningprompt也改变ambiguity/output问题构念。2+1+2=5标准完成，仅报告checklist、judge×task及有限humanagreement这个可复查测量合同；currentCh66 110–116标签/rubric代理、267judge task competence与283agreement≠统计校准已承载长期原则，无需新写通用评价段。root actual原cache3.3/4.5及对应Ch66论点核通过，不称全附件读过。

## Quantization Self-Explanation 2601.00282v1

原源：[Can Large Language Models Still Explain Themselves? Investigating the Impact of Quantization on Self-Explanations](https://arxiv.org/html/2601.00282v1)。必要原段保留在core-2601.00282v1-selected.json：任务/解释评价协议、排名、PTQ配置、人类校准及限制。2+1+2=5；因量化后任务指标不代表解释可用性的具体设计反证，深入受影响评价命题而非全附件。

六种weights-only PTQ、7B～72B模型的任务/NLE/CFE排序不等价；BART/TIGER和perturb/CC-SHAP/self-consistency/LFR只是不同测量对象，不能推内部因果faithfulness或参数信任保证。48位英语评估者只标30条索引样本，14B模型未参加该human部分；judge agreement不等human correlation，更不授所有量化等级的解释质量。A100/H100、合计10h为所披露实验背景而非部署SLO，未知推理precision/负载边界不补造。

root实际核排名、人类样本/排除条件、judge协议及Ch49 1032–1045的aggregate→individual→distribution/workload三层验收与2159–2163任务/语言gate，认可5分受限反证OnlyReport。现正文未保证任务分数足以保解释，故不强加重复通用验收正文；不因Books处置反降准入分。此次仅修复本日已读AB遗漏的处置记录，没有扫描新窗口/主题。
