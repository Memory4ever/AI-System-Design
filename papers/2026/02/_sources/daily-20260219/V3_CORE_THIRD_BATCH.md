# 第三批必要核心

只处理本日题摘中具体增量，采用精确v1。日期原始字段仍见同身份DataCite原记录，官方announcement下界联合限定，当前Updated不参与。Books与独立必要源复核尚未完成，不授日级Gate。

## 2602.15112v1 ResearchGym — 2+2+2=6，integrity反证受影响深入

实际读[exact-v1](https://arxiv.org/html/2602.15112v1) §2–5、§7、D.9；[本地](exact-v1-bodies/2602.15112v1.html)。准入不是多5任务：full-loop executable grader使“某次达到论文指标”与“重复run完整完成/真正改善”分开，并以hint/延时/async实际反侧修正更长预算或parallel tools必改善执行的解释。5任务39subtasks、GPT5/rg-agent3独立run、A10080GB，$10/12h；只有每任务best延长+$10/12h不是随机paired预算对照。Claude/Codex默认$20/24h且不同models，不把scaffold比较归因架构；best@3不是日常可靠性。原任务含materials，但不采用科学领域机制，只采用跨主线执行评价/完整证据责任。

§4.2主15run改善1/15、subtask完成26.5%、tool-call不报错84.92%，这些分母不相混；normalized Agent/SOTA而非baseline-adjusted，sourcepaper上下界不保证同训练seed。§5.2 async empty/stale logs被当作失败或进展、过宽cleanup自杀、跨run拷贝和互斥配置cherry-pick，支持progress evidence/isolated workspace/finalartifact检查需求，不识别全部自然failure原因。作者说早期integration问题已修复，不能把作弊案例反填成最终评分全部无效。

D.9只有限6synthetic integrity案例、posthocGPT5 inspection，手审称suspicious无FP但部分cheating可能漏；“high False Negative Rate (marking benign for review)”术语矛盾、正文46 vs表48、Basic25栏计数不闭合，不能采用100%完整检测。约$0.59/run/331min总、inspection不批准最终scientific claim，posthoc也不能防已发生effect。核心方法/关键反侧已足够；完整附件/各任务领域实现无需遍历。Books待actual owner，非机器或旧8分Existing授完成。

## 2602.15183v1 Seeing to Generalize — 2+1+3=6，binding解释差额受影响深入

实际读[exact-v1](https://arxiv.org/html/2602.15183v1) §3–6、AppendixD/F；[本地](V3-exact-v1/2602.15183v1.html)。相同color→shape→item关系可由位置pointer或内容bundle完成，visual训练可能改变解法而不只是增加context；12layer/hidden128/4head scratchTransformer、A6000/A40 BF16，四textseeds、三frozen imageencoders共12分支剔除1divergent=11。Noise位置暴露与imagecurriculum分开，37.2/57.5/69.5/83.6是该syntheticOOD曲线，不等generalintelligence。Interchange paired original/counterfactual patching支持定位positionalvscontent路径，knockout+probe分工；后期reflexive可只是已经算出答案的readout，需firstcausalspike。

直接训练反侧重要：正文§4以clean image为独立分支，AppendixD.4–7却写noise是image训练prerequisite、额外FeatureGrounding双向辅助任务、20/80mixed再vocabulary扩展；额外train步/预算和auxiliary目标未与纯text对照完全匹配。因此采用visual-curriculum bundle伴随symbolic binding与局部OOD改善，不授“图像独立且唯一导致转换”、translation-invariance因果保证。Qwen2/2.5/3/VL最大effect层比例是观测跨checkpoint，没控制pretraining/posttraining差异。仅可把表示路径与可访问长度分开诊断，不能让probe解码或3组大模型相关升级成通用binding机制。必要支持和直接反侧足够；Books待actual owner。

## 2602.15228v1 System prompts/code — 2+1+2=5

实际读[exact-v1](https://arxiv.org/html/2602.15228v1) §3.1–3.6、§4.1.1–2、§4.2.1 Tables1–6、§6；[本地](V3-exact-v1/2602.15228v1.html)。具体反证：更详细system约束/更多few-shot不是单调质量，需把model×language×example-selection×decoding共同固定。CoderEval460含Java/Python各230，GPTOSS20B/QwenCoder1.5/7/32B、T0/T1、3shots固定vsretrieval，L40S4×48G/vLLM。3.5写officialHF实现而3.6称全部vLLM，backend精确版/解码配置未完全披露；output后处理剥语言标记/额外文本也是scorer身份。

同Java T0 Qwen32 Base无example37.39，固定example6.96，retrieval17.83；固定strategy内详细prompt可回29.57但不是总体胜zero-shot。GPT20B zero-shotstruct42.17vsbase39.57未显著，而固定examplebase14.35→edge29.57也不能写edge更好于zero-shot。McNemar/Holm是同题paired二值、不能“不显著”认定相同；Java/Python不同datasets/KB(CONCODE/CodeSearchNet)、architecture/tokenizer/训练差异不控制，跨语言差不是语言独立因果。prompt内容与长度21–117tokens同变，不能归因长度或density，functional unit tests非普遍security。普通单prompt/zero-shot回退仍合理；仅局部可复用边界，不机械读全部360结果。标准必要证据足够，Books待actual owner。

## 2602.15238v1 DAT — 2+2+2=6，安全必要深入

实际读[exact-v1](https://arxiv.org/html/2602.15238v1) §3–5/Table1、AppendixA完整TV推导及B.1–3；[本地](V3-exact-v1/2602.15238v1.html)。旧有限empiricalAT即使inner攻击强也可漏training-support外data-specific prompts→LLaDA8B joint/inpainting固定harmful y反采样x，再target model/StrongREJECT选16/1000每behavior，并对扩集CAT→外层人口覆盖与内层embedding worst-case分别优化。Theorem只在同harmful-response marginal、loss有界、expected conditionalTV≤ε下风险差≤2Mε；正文写q全人口而AppendixA明确tildeq限制harmful，不能外推全部安全风险。这里ε未实测，finite samples增多不证明TV自动下降；log-likelihood loss原本不有界，clipping只理论可用，不宣称actual训练已经匹配。

Llama3-8B/Qwen2.5-14B、HarmBench100behavior×16prompt、UltraChat retain、BF16、A100/H100/H200，JailbreakBench100/StrongREJECT阈.5、BoA取union、有限GCG/PAIR/1000Direct/1000BoN/1024inpainting。Table1 BoA .88→.36(Llama)/.93→.18(Qwen)，但Qwen XSTest .544→.464、MMLU .787→.773与ARC有损；不称全quality/safety Pareto。§4说alignupdates/optimizer，而B DATvsCAT Llama lr1e-4vs2e-4、batch8vs16、utility.45vs.25、BF16vsFP16，Qwenattacksteps40vs20，不能纯归因扩集或equalcompute。High/low likelihood过滤与moreM是support/target-specific选择，不等truepopulation认证，train与eval同StrongREJECT带共同偏差，CB用XSTest训练不纳generalization比较。Generations/filter/AT代价未全计、重复seed/CI未给；不授unseenadaptive/production安全。机制和必要反側足够深入；Books待actual owner。
