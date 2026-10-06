# 六个准入决定点的窄核心（作者，不追加发现）

来自已读有限题摘集合，root已首批共同门校准；本packet解决是否只是组合的具体决定点，不以额外读多少篇扩充候选。未来Source/owner仍需非作者实际核。

## LangMARL 2604.00722v1：core后拟EX

[v1](https://arxiv.org/html/2604.00722v1) §4.2–4.5/Eq3–8已定点读。credit=C_i=LLM(trajectory,i)，gradient=LLM(policy,credit)，aggregator/optimizer也是LLM改写policy text，明确无numeric gradients。借CTDE/MARL式子没有新增可验证credit估计/反事实分配算法；Fig4移除agent-credit的消融只说明这份模块bundle有用，未给其成立条件/新执行机制。不是因‘无硬gate’或‘不是真RL’否定价值，而是中央反馈+分role prompt迭代的成熟组合无原文基础增量。准入决定完成即止，无全文附件或评分。

## Dynin-Omni 2604.00007v1：具体增量改为词表扩展merge，拟6分

[v1](https://arxiv.org/html/2604.00007v1) §3.1/4.2/7.1/Table9已读。不是仅‘三模态统一’准入：原词表embedding/head保backbone rows，新speech rows继承Stage1，其余同形weights才interpolate，避免错把vocabulary extension作普通全参数merge。Stage1后文本/视觉严重退；shared-rows平均与all-vocabStage1在相同alpha对照中有取舍，typed-row recipe恢复部分旧能力但ASR/TTS仍显著劣于Stage1（Table9），不是零遗忘。多阶段/merge/重训都付费，modality identity与rows版本必须绑定，不从native masked/冻结codec借通用新颖性，也不宣称所有模态质量最好。

## ThinkTwice 2604.00018v1：有实际随机token同预算对照，拟5分

[v1](https://arxiv.org/html/2604.00018v1) §3/4.4–4.7已读。池保高entropy位置前prefix、重生成nexttoken再完成，§4.5同generation budget比较highest-entropy与random token，对局部quality-cost选择有具体证据，不仅与大型号API价格比较。Finished sequence需correctness checks，entropy after-think只是confidence，不认证truth；verifier实现资格和API有限logprob/full-vocab entropy对接未完整披露，不照抄部署recipe。Optuna在GSM8K train调超参、有限两math任务/两模型；未将GPT5/不同端点价格当等计算结果。已审决定性对照后仅拟局部信号，不采接近100%普遍可靠性。

## DisCo 2604.00849v1：specific signal conflict有直接反側，拟5分

[v1](https://arxiv.org/html/2604.00849v1) §3.2–3.3/4.3已读。entity text替换pronoun但保实体名给grounder定位reference；remove-TVD与remove-GRPO局部对照表明只分离identity提升相似但prompt adherence/quality降，通用IR奖励提高quality却损subject。这是分开identity/edit条件和reference-aware reward的局部取舍，不是‘GRPO+grounder’就贡献。不能由entity词消失后的attention图证明唯一因果或视觉独占；人工100pair只是该sample，更多grounder/VLM、reward训练与GRPO都付费，保持原reference回读/原条件分支。不采所有sim-control悖论已解决。

## EgoSim 2604.01001v1：具体对象更新分支，拟6分

[v1](https://arxiv.org/html/2604.01001v1) §3.2–3.3/5.3–5.5/limitations已读。实际从generated observation重建geometry、mask隔离interactive object，last-frame对象geometry合成static背景，Sim3对齐/TSDF将重叠区域更新为新state；不是只把video命名state。目标是物体操作后不在下一render还原，直接反側去object-filter出现dynamic ghosting；但qualitative图未视觉核，不称永久物理证明。20task two-clip121frame评价continuous Depth/Cam error比single更差，monocular occlusion/pose失败保留；不是部署真实action或world真值。重建、tracking、fusion、DiT与状态更新均付费，错误generated geometry会反馈，不把pipeline拼接普遍化。

## RELISH 2604.01206v1：capacity-matched对照决定保留，拟5分

[v1](https://arxiv.org/html/2604.01206v1) §3.1–3.3/C.3.3–3.6必要已读。frozen token hidden states、可学习single latent query逐层crossattend并输出scalar，training-split y normalization+Huber；不是LLM生成numeric text。参数matched MLP仍较差，改输出提取机制有具体局部证据，不仅借Perceiver组合。相关性和RMSE分开：RAIL可提高ranking却不改善scale；WMT收益比STS更大、STS大模型可tie。不能从这些对照说backbone已具‘真实numeric知识’唯一因果，frozen forward/head training仍付费。拟采用single-pass readout选择与问题粒度条件，非所有回归/算力SLO。

## 必要实验设置补读与停止

Dynin Table11仅用来限定stage/merging成本，32/40H100、batch128与多stage语料不等额外数据无费，未核全部19benchmark。DisCo §4.1/Table2：Subjects200K/FLUX、8H20、batch2/accum12、GRPO16step/12images、Qwen3-VL25k preference；DreamBench30subjects×25prompts、SAM裁subject影响测量，不是所有对象/指标真值。EgoSim §5.1：EgoDex/EgoVid各100video test、Wan14B inpainting基座/8H200及groundtruth第一帧/scene输入；two-clip20task不是长程现实控制验收。RELISH §4.1：Llama3.1-8B/Qwen3-8B/32B/Gemma3-27B、STS-B/SICK与WMT三方向；range-NRMSE/pearson/spearman、M8/dh256/L3，parameter-matched MLP与LoRA/frozen两regime分开，16sample RAIL不等single-head输入成本。

本packet除LangMARL窄EX外五项仅作者拟评分6/5/5/6/5，必要机制/对照已读到拟命题；准入/日期/Source及Books仍待相应独核，不自称已通过。extra DOI上界仅00849/01001新增两投影，另三同identity已有27投影；无需六决定点变全附件/全版本。

root 非作者实际读 00018 §4.5 同generation-budget randomtoken对照，局部选择Source通过，2+1+2=5；未授verifier实现资格、API完整熵接口或部署recipe。其它五项不由本单项回执继承PASS，00018唯一owner/PRE继续独立申请。

root 后续实际读 RELISH01206 §3 single-query latent、training-split normalization、C3.4–3.6 parameter-matched/STS tie，5分Source限定通过，继续具体owner差额而不默认两段。LangMARL00722原4.3 C_i=LLM(trajectory,i)/语言优化改prompt，无新credit估计，贡献前EX独核通过。Dynin/DisCo/Ego原方法虽root已读，直接反侧尚待核，不继承上述PASS。

后续 root actual Dynin00007 core/Table9、DisCo00849 core/4.3直接反側限定Source6/5通过，保stage merge退步与prompt adherence/identity取舍、不授万能融合/attention因果。Ego1001原Table2/5.3及必要fusion appendix实际补读通过6：121frame two-clips不授longhorizon，Depth/Cam/PSNR较single退步，generatedstate/Sim3/TSDF非现实truth；仅persistent simulated-state接口可继续owner/PRE，不授物理真实性或无限稳定。上述旧待核态只履历，当前按本具体回执，不授PRE/POST/DAY。
