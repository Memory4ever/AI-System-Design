# 02/20 第七批有限必要包：16229 / 16284 / 16299 / 16305

root已完整AB准入校准及本包必要原源/actual owner PRE；四项实际窄写正文、完整邻接及自身末注POST通过，四锁释放。实际正文位置为Ch25:282、Ch45:690、Ch76:422、Ch23:113；下文拟写说明保留为PRE时依据，不是当前未写状态。阶段累计28项必要处置、20项真实整合POST通过，不授全日。定位统一为 `V3_extract_html.py < V3_REVIEW_2602.<ID>v1.html | awk 'NF' | nl -ba`。未核代码或复现，支持/关键反侧足够即停止，不扩全附件。

## 当前说明与日期

4个 `V3_CURRENT_ABS_2602.<ID>.html` 完整AB/Comments/history实际读。16229/284/305当前v2，16299当前v4；Comments只有MICE EMNLP/BAT ICML接受说明，原页未见具体纠错/撤回信号。不因版本号遍历全部revision，也不以后来接受事件改首公开。全部采用精确v1，MICE currentAB改为FLOPs down2.5×不代换v1 TITAN-V latency。

| ID | v1 Submitted UTC | 同ID Registered UTC | 北京公开区间（官方bridge推定，含起不含止） |
| --- | --- | --- | --- |
| 16229 | 2026-02-18T07:08:14Z | 2026-02-19T02:41:16Z | 2026-02-19T09:00:00+08:00 ～ 2026-02-19T10:41:17+08:00 |
| 16284 | 2026-02-18T09:06:53Z | 2026-02-19T02:42:34Z | 2026-02-19T09:00:00+08:00 ～ 2026-02-19T10:42:35+08:00 |
| 16299 | 2026-02-18T09:30:29Z | 2026-02-19T02:42:54Z | 2026-02-19T09:00:00+08:00 ～ 2026-02-19T10:42:55+08:00 |
| 16305 | 2026-02-18T09:37:20Z | 2026-02-19T02:43:03Z | 2026-02-19T09:00:00+08:00 ～ 2026-02-19T10:43:04+08:00 |

原值实际读同ID `V3_DATACITE_2602.<ID>.json`；Registered+1秒依首批官方正文announcement/DOI bridge作上界，Created仅raw，不把Updated-v1授公告时间。

## [Factored Latent Action World Models](https://arxiv.org/html/2602.16229v1)

2+2+2=6，具体owner差额拟深入。实际§4（132–231）VQVAE/FSQ按数据集预训，slot attention+per-slot causal temporal attention；IDM输入全部当前slots与本slot后态，FDM输入全部当前slots与本slot latent action，**允许状态耦合**而限制动作读入，不是独立物理dynamics。Gaussian KL限制action容量，aggregate residual+当前feature，factorizer/IDM/FDM联合训练，非把已有物体slots贴名。§5（242–278）匹配总latent容量d与K×d/K及相同encoder架构，MultiGrid/Procgen/nuPlan各域；§5.1（278–290）先由未见的GT后续frame反推动作再rollout，不能称无条件未来预测或可部署控制；Procgen GT只含player，不是全实体oracle。

§5.2（502–518）4agent中2共享动作时K3合组 vs独立动作K4，DCI probe对应性不证明因果entity辨识。§5.3（571–601）1M专家交互frames+1k/10k带标签action decoder，1k Starpilot不优于BC，不能授action-free端到端控制。§5.4/Appendix C.4（987–1049）全后态/all-actions耦合变体预测近似同样好（MultiGrid PSNR56.5 vs56.3），但DCI disentanglement0.91 vs0.79/informativeness0.93 vs0.58；completeness反而0.91 vs1.00，不能所有表示指标全面优越。无temporal attention变体预测/绑定均退化，尚非所有domain共同单因素结论。§6（616–624）encoder/离散action-decoder限制；理论因果/物理安全不适用，hardware/precision/seeds在拟采用核心位置Not Disclosed，不引用速度。

actual `MULTIMODAL-WORLD-MODELS` [Ch25](../../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md):259–281已有inverse anti-collapse、外部effect坐标及非辨识；382–390已有persistent object address/content，不等per-slot动作入口。**差额是all-current-state耦合与per-factor-action访问限制可以分开，并用近同预测/不同factor读出对照检验结构**，不是“worldmodel可分解”口号。拟一段接latent action/effect 281后、operator-structured前，保留共因动作会合slot/GT后态与带标签decoder、额外slot/IDM代价、monolithic/coherent fullstate旧分支。未写；不复制对象地址论证。

## [Fast KV Compaction via Attention Matching](https://arxiv.org/html/2602.16284v1)

2+2+2=6，具体owner差额拟深入。实际§2（111–147）拼接时局部normalized output以block unnormalized mass加权，**只拟合块内输出不够**；q=0时T→t无bias不能匹配mass，新增scalar beta并保持logical长度/RoPE新token位置。任意query精确拟合不可能自动由有限参考queries保证。§3（148–252）repeat-prefill/self-study/context-prefill产生referencequeries，按层onpolicy顺序补已压缩层query漂移；selectedkeys上beta=log NNLS非负weight、V用LS；**NNLS和OMP不全closed-form**，保留keys来自原KV集合，最终V可改变。非均匀head预算根据10context loss曲线greedy exchange，假设近似head可分离。KV-chunk先fullprefill再compact；text-chunk独立prefill+RoPE移相不恢复跨chunkconditioning。

实际§4（252–359）Qwen3-4B/Llama3.1-8B/Gemma3-12B；QuALITY50 context/5–8k、LongHealth4×60k/100问。Cartridges QuALITY只Qwen20预选子集，不能和全50无条件比较；100×时Cartridges LongHealth更好。§4.3/Table1（286–311）单H200 Gemma12B60k，FP32拟合/BF16存储，不做quant；selfstudy139s/OMP565s/fastOMP104s，context-prefill7s，不能把“seconds”当所有设置。varlen engine/padding/disaggregation是未落地成本，§6（350–358）online/重复推理 future；reference heldout logp不是答案truth/任意后续query保证。不采50×为生产收益。

actual `INFER-KV-CACHE` [Ch45](../../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md):636–643已有tail分子/分母联合归一，685–689已有连续syntheticKV优化、querydistribution与fallback；308–314已有修复cacheconsumer。但**缺少压缩整块KV时以scalar bias拟合mass、V另拟合output，使其与未压缩futureblock拼接的权限**，并不是缺OMP配方。拟一自然段接continuous syntheticKV 689后、learned eviction前，条件化referencequery支持/层间漂移/fit与不规则layout成本，FullKV/原tail方案保留。未写。

## [MICE: Minimal Interaction Cross-Encoders for efficient Re-ranking](https://arxiv.org/html/2602.16299v1)

2+1+2=5，实际owner差额拟深入。§3（119–200）mask before softmax；通过重训mask限制CLS读doc、doc读query，early query/doc各自编码，再交互层冻结doc，只保doc→query crossattention、query selfattention、CLS读query。不是训练后随便删attention：offtheshelf施mask退化。§4.1/4.3（719–745、1080–1107）MiniLM33M12layer/Ettin17M7/Ettin32M10，MSMARCO MarginMSE相同teacher125k steps/b32/LR7e-6/5k warmup，dev1k bestcheckpoints+5seeds；TREC19/20与13BEIR固定BM251000候选。Ettin32 OOD46.4 vs48.2原crossencoder负侧，不授全部域保持，标准ColBERT110M不与MiniLM同capacity混比。

§4.4/Table5（1107–1146）同MiniLM、512doc/b128/100forward/TITAN-V12GB，MICE无precomp241ms vscross470ms；precomputed113ms含减少层/参数26.3M，不能唯一归交互裁剪。精度未披露，这不是完整queryencoding/索引刷新/在线服务SLO。§5（1151–1155）**fullindex与first-stage retrieval未实现**；删queryselfattentionranking崩溃，缩维randominit劣于layerprune，不能把固定doc升级零交互。模型小不排实质reranker机制，仍不借它授LLM能力因果。

actual `AGENT-RAG` [Ch76](../../../../../books/part-07-agent/76-rag.md):418–428已有rerank成本和single-vector共享retrieval/listwise目标；431–442已有head readout/前向截断，但不承载**冻结doc的单向crossattention，query自交互继续保留，重训与仅mask移除的边界**。拟一自然段接420后/utility训练分支前，带上有限OOD反退、缓存/索引费用与未firststage、普通crossencoder/lateinteraction共存。未写。

## [BAT: Better Audio Transformer Guided by Convex Gated Probing](https://arxiv.org/html/2602.16305v1)

2+1+2=5，设计评价反側与owner差额拟深入。实际§4（111–194）冻结encoder all-layer特征L2normalized，softmax层权重convexmix、10k可学习prototypes，patch min/max+CLS similarities到linearclassifier；**probe本身也学习容量**，不是不用标注的表征真值。Table1 AS20k reportedFT SSLAM40.9>EAT40.2；作者复现39.97<40.28、CGP34.62<35.20，AS2M reproducedFT又SSLAM47.69>EAT47.61，故不能宣称所有task/metric次序都反转。用公开weights原FTrecipe仍没复现reportedpeak只支持这个协议，不证明原文作弊。

§5（194–255）AS2M1,932,574×10s/16k，b48×16maskviews400k steps，采用BF16而非FP16，并去旧loss8e4系数；不同pipeline/core目标不能全归gate。§5.2/Table3 MLP/EOB×gate2×2：无gate EOB mAP低但F1高，gate后EOB在两指标更好；attention sinks解释为hypothesis，不授已因果。§5.3/Table4/Fig4 CNN→6layerViT decoder把task信息peak中层→后层，额外decoder容量/训练预算不免费。§6（378–384）相同旧FT超参、BAT91M vsEAT/SSLAM88M，作者明确**later-is-better不普遍**；最终模型SC2 linearprobe BAT72.83与EAT72.68接近，ESC50 linearprobe BAT87.25低于SSLAM88.00，不由综合SOTA所有条件授优越；ESC50 CGP大于FT也只局部。AppB（848–850）主要A100，development4090，probe seeds/预算不确定性Not Disclosed；代码uponacceptance/request未核，不追无关repo。

actual `MULTIMODAL-REPRESENTATION` [Ch23](../../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md):111已有MAEB目标信息×分类/聚类readout，不用重复这个口号。**新的具体条件是同一冻结模型的任务信息可能位于中间层，probe层可见性/容量和pretrain decoder负担会改变评价对象**，缺少该层边界不是缺CGP配方。拟最多一段接111后音频接口主线，保留probe非truth、later非通则、alllayer/decoder额外预算及final-only probe合理低成本分支；不沿BAT改造列模块。若root判断现111已足以承载这项条件，只报告明确反侧，不强造diff。未写。
