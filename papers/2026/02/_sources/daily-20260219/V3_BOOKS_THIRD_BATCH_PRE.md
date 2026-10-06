# 第三批实际 owner 比较

仅本日精确v1，必要原文与反侧见 [第三批核心](V3_CORE_THIRD_BATCH.md)。当前合同/ROADMAP与Books三份指南已实际重读；不是整合许可，不改共享Books，待root必要源/PRE。

## 15112 ResearchGym — 已有覆盖建议

root已实际核必要原源及Ch66具体正文；已有覆盖通过，无书改。

actual Ch66 L238–245 `model×benchmark×harness×environment×scorer`及comparison而非run证据单位，已明确流程/工具成功不能签改进、artifact谱系与允许treatment分责、invalid measurement/operational failure/真实negative分账、人工语义复核与有限修复不能倒填阻止。15112 task completion26.5%/nonerror84.92%/improvement1/15、async logs与cleanup/cherrypick/crossrun contamination、best-only预算延长均落在这些已有具体条件；它未建立不同可靠性机制，不为新任务包强写书。建议PLATFORM-EVALUATION-SYSTEM/Ch66 L238–245已有覆盖，保留D96synthetic detector计数/措辞争议仅不授检测保证。邻Ch65/67开头已实际读。

## 15183 Seeing to Generalize — Ch5 的位置shortcut与内容binding差额建议

实际Ch5 L215/217、209–239完整邻接及末注572经root非作者POST通过，末注同步，窄锁释放，非整日Gate。

actual Ch5 L213–221已有role/filler与entity-relation双索引、拟合/干预分责，L267–269已有形成/访问/使用分责，但没有同题内容干预对位置替换区分pointer与content路线，再用image/text curriculum bundle训练检验结构外推的具体路径。建议在role/filler后、双索引前补1–2段：paired content/permutation interventions诊断位置捷径，curriculum同时改模态/aux grounding/noise/词表和mix时只能采用bundle证据，不把视觉存在或probe预测当image-only因果。11/12branch、12layer小模型/3frozen encoders、noise/text反侧和训练增量费用近正文；未支持frontier VLM普遍泛化，旧role/行为验收共存。Ch4/6开头实际读，无结构新增。

## 15228 System Prompt Code — 已有覆盖建议

root已实际核精确v1必要源及Ch74具体正文；已有覆盖通过，无书改。

actual Ch74 L68–90 Instruction/Example/Schema分开、example质量/顺序/coverage可诱导格式，L115–138冻结model/tokenizer/template/eval/revision并覆盖成功、安全、成本，heterogeneous tasks稀释真实prompt差额原论点已在。本篇同model/function任务的rich/fixed/retrieved非单调、Java/Python与temperature/eval依赖，未建立rich描述必有效或长度密度因果，具体支持这些现有条件。建议AGENT-PROMPT/Ch74 L73、L115–138已有覆盖，无新增模板。前邻Ch73/后邻Ch75开头已实际读。原稿不同protocol/HF-vLLM ambiguity保留，不把McNemar不显著当等价。

## 15238 DAT — Ch72 攻击生成分布条件差额建议

实际Ch72 L1347/1349两段、1336–1361完整邻接及末注4154经root非作者POST通过；末注同步，窄锁释放，非整日Gate。

root已核必要原源与实际owner，以下为精确两段PRE，拟放现Atlas段后/CDI前，未写书也未持Ch72锁；待root确认当前窄锁。

只用当前攻击器找到的失败训练，在该攻击分布稳定时容易控制；但换一种攻击生成器后，训练覆盖的prompt分布可能不再代表要防御的失败。一个条件分支先抽取有害回答，再以联合inpainting生成与该回答对应的prompt，随后交给外层对抗搜索，而不是把单一模板攻击的prompt当作全部威胁人口。这里要固定两个测量对象：有害回答的边际分布，以及给定回答时prompt的条件分布。只有前者相同、loss有界，且后者相对目标分布的期望total-variation误差受控时，才有相应的平均风险差额界；它不保证每个prompt安全，也不说明未知自适应攻击已经被覆盖。[必要分布机制与假设](https://arxiv.org/html/2602.15238v1)未实测这份TV误差，不能把生成压力或局部攻击成功率当作假设成立的证据。<!-- source-family:SF-2026-ARXIV-2602-15238 -->

联合生成、目标回答筛选、内外层搜索、训练与回归都需支付成本。该研究的有限HarmBench/JailbreakBench对照中，BoA攻击指标改善仍伴随Qwen的XSTest与部分通用任务退步；正文的matched-update说明与附录的学习率、batch、效用权重、精度和攻击迭代数也未完全一致，因此不能把收益单独归于proposal分布或宣传等总预算。真实失败回放、独立验证、人工红队与effect-time gate仍然成立：当回答人口、writer或目标模型改变，TV条件无法核验，或效用退步超预算时，应重新采集和验证失败、缩小采用范围或回退已验收checkpoint，而不让生成样本拥有release权限。

actual Ch72 L1332–1353已承载on-policy failure repair、独立验证、攻击trace特权/预算、训练checkpoint与部署防线分开，但未承载由harmful response先抽y再conditional proposal x、固定y marginal下conditional TV误差限定目标risk差额的选择。建议Atlas修补段后、CDI前1–2段：联合inpainting proposal把训练失败分布构造与outer adversary search分开，风险界只same harmful marginal/bounded loss/expected conditional TV，未测ε与实际trainclipping不授保证；finiteHarm/JailbreakBench、BoA改善和Qwen XSTest/MMLU/ARC反侧及§4-vs-AppB训练配置冲突近正文。Diffusion/target filtering/inner外层搜索有成本，不宣称等总budget或所有adaptive攻击；旧真实失败采集/人工红队与effect-time gate保留，生成样本不拥有release。Ch71/73交接已读，原模型生成机制不重复推导到Ch24。
