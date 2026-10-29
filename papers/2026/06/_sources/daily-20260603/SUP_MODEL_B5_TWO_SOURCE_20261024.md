# Jun03 B5 两项：root必要Source与最小owner提案

仅本日补Jun02；前52家族有效层不重做，本两项尚未独立复核、未入表/落书。完整题摘及组合日证见[本批提案](./SUP_MODEL_B5_20261024.md)，不靠title正则准入。以下实际原始HTML读域与判断足够支撑拟采命题，不声称全附录、实现或复现完成。

## 01850：压缩后的分类不确定性，非模型自知证书

[exact-v1](https://arxiv.org/html/2606.01850v1)，root实际读§3.1、§4、§5.1–5.7/Table1–2与直接反侧。每题六选项，另加拒答/none，Halu数据以随机其他题候选补齐；12模型跨家族1–70B，每任务2000例、一半calibration一半test，LAC/APS与三prompt均值，alpha=.1。8H100、max input2048；FP16/weight-onlyW4A16/activationW4A4与50%unstructured/20%structured，不是同资源压缩强度。batch、concurrency、完整模型压缩校准预算和SLO未由本必要域披露；只读option-letter logits，不是自由生成事实置信度。

同准确率附近可有不同set size；规模、方法与任务有反侧，70B不是保险。Table1 Qwen3-8B SliceGPT的SS1标为degenerate、coverage约12%，故不能由集合变小授更可信；正文泛称distribution-free也不取消§3.1交换性。不同模型/压缩artifact各自calibration，不证明原dense阈值可直接移植，也没有证明SS阈值能签安全release。必要采用仅accuracy、empirical coverage和set size分账，并对失败校准拒绝解读；不采用一般scale定律/普遍uncertainty tipping point或特定安全位宽。拟2+2+2=6，quantization artifact与评价接口的边界。

实际owner `INFER-TENSORRT-LLM` Ch49，已读“量化验收不能只看平均分”完整主论证、三层图、逐例agreement/diagnostics完整段、稀有词完整后段与后续Ch66交接；现有同样强调accuracy不足，但未具体分开经压缩后的预测集合大小与覆盖资格。Ch48开篇的target-law职责、Ch20 sampling主线亦已读，不在这里另推conformal理论。

拟仅在完整“逐例agreement说明决策是否发生交换…”段后、稀有词“逐例质量还可把…”完整段前插入：

> 如果下游还消费不确定性，保持 top-1 准确率也不能代签其接口。固定分类任务与压缩 artifact 后，可分别量测校准预测集的经验覆盖率和集合大小：前者检查目标是否仍被覆盖，后者才在覆盖合格时描述剩余标签歧义。[受限压缩对照](https://arxiv.org/html/2606.01850v1#S4)显示，两者与准确率并不同步，甚至出现集合很小却覆盖崩塌的退化配置；“更自信”不能据此批准可靠。它只覆盖有限多选协议，交换性条件不延伸到任意分布漂移或自由生成事实。校准样本、阈值与全部评估调用均计费；换模型、精度或输入域后重新验证，覆盖不合格时保留原 artifact、提高精度或明确拒答，不让平均分或小集合代替验收。<!-- source-family:SF-2026-ARXIV-2606-01850 -->

## 01682：likelihood scorer的chunk控制，非exact speculative

[exact-v1](https://arxiv.org/html/2606.01682v1)，root实际读§3/Eq1–4、§4.1–4.8/Table1–5/Limitations与主要反侧。小模型每轮k8/16/32、T.7取chunk，大模型仅算候选条件likelihood；CGS减小模型likelihood，不生成大模型答案。EOS提前时仍可短于L，所以“fixed length”不能扩成所有候选必严格同长。chunk选出后commit不是保持原target law的接受/残余采样，不能由contrastive名字移交Ch48 exactness。

Qwen1.5→32B、Llama1→70B与扩展Qwen7→72B、vLLM、五math任务；AMC40/AIME30仅三seed，其余有限单设，不补造统计CI。§4.3 matched guidance只在k8按平均干预次数从L10/20/50/100选最近，计数仍有明显差额且scorer模型/每轮长度不同，**非matched FLOPs、GPU时间或SLO**；§4.6另一L20固定口径不混同。Qwen MATH有CGS低于PRM的反侧，后验BoN随k增亦可退。主张短trace不免全部废弃候选/两模型打分/驻留和串行commit费用；hardware、precision、完整输出cap/并发/真实延迟未由必要域充分披露，不授免费/净速度。

拟2+1+2=5，只新增生成中likelihood选择的长度/时点边界，不给成熟PRM思想加分。actual owner `MODEL-SAMPLING` Ch20，已读Parallel Sampling的Coverage/Selection完整开头、LTM逐token/概率质量分支及其marker、后续链/答案likelihood完整段及其marker；现有两支没有说明off-the-shelf scorer的固定chunk及长度归一仍有bias。Ch19 cache角色与Ch21开篇/Ch48分布权属作为相邻职责，不重复推导。

拟仅在LTM完整marker之后、以“候选已经生成后，选择器还可分别读取整条链…”开头的完整段前插入：

> 生成中选择也可以以固定上限的 token chunk 为单位：小模型提出若干续写，大模型只计算它们的条件 log-probability，再按大模型分数或两模型分差选一段继续；EOS 仍可提前结束，所以边界例外需保留。这与事后选整条链、按自然步骤评分及保持 target 分布的 speculative verification 都不同。[受限 chunk 对照](https://arxiv.org/html/2606.01682v1#S4)中，长度归一仍未消除自然步骤的长度偏好，较短固定 chunk 改变了干预时点，但 likelihood 不是逻辑正确性。相近干预次数不等相同打分算量或延迟，较短最终轨迹也未结清全部废弃候选和双模型驻留。生成、评分、缓存及每轮串行提交均计费；概率接口、质量或完整预算不合时，保留普通单路、整条候选加独立 verifier 或已验 PRM，不从无需新训练批准免费推理或原分布不变。<!-- source-family:SF-2026-ARXIV-2606-01682 -->

最终采用（非重做有效层）：01850必要Source/6分与日证通过，但reader R23实际定位Ch66 `PLATFORM-EVALUATION-SYSTEM` 的同family alias `SF-COMPRESSION-UNCERTAINTY`及“Compression Release必须同时验收Accuracy与Calibrated Uncertainty”完整首两段，已承载同样本accuracy/coverage/setsize、calibration failure、artifact/score/target、交换性/shift与回退；故撤回上方Ch49新增PRE，具体已有覆盖，不搬旧06-02日期、不降分、不造diff。01682则经R24必要/owner/精确PRE通过，root真存Ch20指定段及本人注，reader R25唯一实际POST通过生效释放。两项未授完整DAY；上方未采用PRE只是可追溯原提案，不可按它再次写书。

后补原域的明确限制：01850 §5.7只支持多选、固定alpha .1/50–50划分，不采用“W4A16 safest default”为跨任务发布规则；01682 Limitations只测math和同family pairs，更校准的变长评分仍未比较，GSM8K最终CGS173tokens还长于small-greedy159。缩短是相对PRM的有限比较，不签所有基线更短。
