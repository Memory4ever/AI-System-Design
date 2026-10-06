# 2603.09714 — MUGEN必要Source与Ch23两段差额（Source/PRE/actualPOST通过）

[exact-v1](https://arxiv.org/html/2603.09714v1)。第二包完整题摘已root独核。作者实际§2–6全部必要文字/Tables1–3；没读Figure3曲线像素，不采用66/48/80%或精确scaling曲线为已独算，没核data/code、复现或完整prompt。fresh官方abs/current v2/Interspeech2026，题摘同v1/无withdrawn或已见纠错；July接受非早于March的先稿依据，不把版本号/接受本身作重要修订或窗内新事件。

原SUP_EXACT_BATCH2.json字段/fresh回读一致：Mar10UTC14:22:22提交在announcementdeadline前，官方availability/noadvance最早Mar11BJT08为下界；owning arxiv.content/findable DOI registeredMar11UTC02:20:08已经可发现上界同BJT03-11夹证，不用Submitted/Updated/注册单独public，待root实核。

2+1+2=5，因具体Ch23 gap拟定点深入：单录音信息可读不保证多候选联合比较/位置绑定→同生成数的candidate permutation/remap majority相对固定顺序SC改进→多音频输入身份与预算、proxy投票/真实声学比较分责。新增是有条件的多候选排列接口/评价边界，不给成熟CoT/SC/benchmark数量加分，亦不采内部容量瓶颈因果。

## 必要机制、评价与直接反侧

§2 35tasks/1750实例，5候选/10tasks另有reference共6输入、7语义/非语义维度；9250clips均8.60±8.79sec。公开语料为主、部分属性可控合成且作者手检、人工instruction、distractors有意在目标属性变化：策展选择题不是连续自然声场或说话者属性真值/用户授权。§3 vLLM openmodels默认greedy、Voxtral .2/.95、Gemini3Pro T1低/高thinking，ASR Whisperlargev3＋Gemini只保文本语义；Haiku4.5 20251001/T0抽答案，400随机99%与人工agreement限该population，不认证全部gold/部署准确率。主表给95%CI但必要主文未给全部interval估计/重复运行协议，APSC表没CI/seed/variance。

Table2语义强非语义弱局部现象支持分切片，ASR+LLM高thinkingoverall30.06高于若干end-to-endopen模型，却缺speaker/music等信息；不能由平均榜单判专用encoder/所有native模型无用，model/decoding/info不同也不作严格单因果。时长/temporal相对弱不证明唯一内部perception瓶颈。

§4.2去一个nongold option，instruction不变、排除ranking3tasks仅32人口，candidate由5→2；正确目标保持但干扰项、总时长/声学token、选择复杂度与chance1/n一起变，不能由Acc(n)/Acc2消除所有混杂或断言fundamentalcapacity内部因果。本轮只采用输入数量应单独验收的设计边界，不采用Fig3精确曲线点或思考不能补任何扩展问题的定律。

§5.1 APSC每次随机candidate order、输出映回原index后majority；固定顺序SC和APSC都10response，Qwen T.2/GeminiT1，APSC每10permutation各1。要保持reference/candidate identity与原任务含义的映射是本书工程条件：不将有真实顺序语义的录音任意换序，不把position编号当clipidentity。表述“10permutation”没交代是否无放回/重复处理/平票规则，不补造全执行recipe。Table3 APSC对SC Qwen30.69vs28.00、GeminiLow73.94vs70.06、High74.97vs72.74；CoT Qwen28.57低于原28.69，但高于SC28.00，不能把更多语言思考认作额外声学信息或必提升。APSC+CoT GeminiLow74.40/High75.26有局部收益，6.74是accuracy绝对百分点非相对6.74%；有限受测model不授排列不变或所有组合更准。

与SC相同10generation数不等完全walltime/cache/编码费用，且对single-pass本身仍有10路前向/多次音频编码、聚合及CoT token费用；训练free≠推理free。硬件/precision/精确opencheckpoint/vLLM版本、Geminiendpoint漂移、输入长度cap/truncation、总token/latency/费用/并发/SLO未明确，不授在线实时/同成本通用最佳。APSC改善可来自位置分散等多个因素，没counterfactual逐candidate同内容处理足以唯一识别decoder/encoder瓶颈。不用optionaldata/code缺失阻止有限原文机制，但没运行不能称复现。

## actual owner与逐字PRE提案

唯一owner `MULTIMODAL-REPRESENTATION`，[Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)。actual143–168完整局部（taskprojector→gatepack→音素接口→MAEB→多层readout→单/多事件filter→发音接口），以及Ch22/24开篇交接已读；Ch23opening此前actual有效复用。现155/157分开encoder信息/层读出任务，159分开query过滤和联合关系，141是visual logits变体合成而非音频candidate majority，未承载“无顺序语义候选集合换序→原clip索引映回→同采样预算聚合”的binding接口。拟159空间音频filter后/161生成发音控制前两段，保留连续声学/真实顺序输入旧分支。

能读出一段录音的属性，还不表示能在多段候选之间保持比较与身份绑定。当任务把录音视为候选集合，而不是一条有真实时间顺序的连续输入时，应分别保存 reference、candidate 的原始身份、展示位置与选择约束。一个不重训的分支对同一集合作多次排列，每路回答先映回原候选身份，再聚合选择；它改变的是输入呈现与决策提案，不改音频内容，也不能把多数结果当声学真值。[必要排列机制](https://arxiv.org/html/2603.09714v1#S5)相对同生成数的固定顺序 self-consistency 提供有限支持；reference 关系、位置措辞或实际时序无法保持时，不能直接套用换序。
<!-- source-family:SF-2026-ARXIV-2603-09714 -->

多候选还要按数量、语义内容、说话者、韵律、时长和环境声分别验收，不能用单录音平均分签联合理解。[有限多音频对照](https://arxiv.org/html/2603.09714v1#S4)中，减少候选同时减少干扰与随机猜错机会，因此候选变少后准确率提高不独证内部容量瓶颈；更多 CoT 也未必改善真实声学比较。排列聚合与固定顺序多采样具有相同生成数，仍须计全部音频编码、前向、生成和映回聚合费用，不由 training-free 或百分点增益承诺实时能力。投票不稳、任务具有不可打乱的顺序或预算不足时，保留原顺序单路输入、明确的候选比较及独立声学/人工核验，不以更一致的选择替代正确性。
<!-- source-family:SF-2026-ARXIV-2603-09714 -->

拟本人末注：SF-2026-ARXIV-2603-09714，Daily2026-03-12补查，exact-v1§2–6/Tables1–3，2+1+2=5；Ch23多候选order/remap identity缺口深入。限无真实顺序语义集合及同10generation有限对照，候选数量/chance/干扰混杂、投票非gold、额外编码/生成费用近正文；不采用Fig3精确曲线/内部容量因果、普遍排列不变、完整执行recipe/实时SLO或代码复现。root必要Source/date/owner逐字PRE与actualPOST待核，不授DAY。

实际后续：root已核v1§2–6/Tables1–3、原DOI及official announcement夹证、Ch23 143–174完整局部和Ch22/24开篇，必要Source/date/两段逐字PRE通过，授窄锁。作者实际写Ch23新161/164与本人1592末注，实际顺读151–184完整局部及本人注，回原证/限定diff通过；非writer root actualPOST待核，不能预记DAY。Table3已按身份纠正Low74.40/High75.26，不由无身份双数顺序混用。

实际POST：root非writer实际151–184完整局部、新161/164与本人末注并回对v1§2–6/Tables1–3通过；原filter完整、候选集合换序/身份映回→生成发音接口衔接、chance/CoT/费用/真实时序禁换与原单路回退一致，Ch23窄锁释放，不授DAY。
