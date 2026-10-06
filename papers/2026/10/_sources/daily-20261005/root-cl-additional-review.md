# 10/05 四项必要原源与 owner 审阅

root实际读取；仅本日四项，不是整日Gate。精确v1首公开随本日官方new公告核，Submitted不作公开时间；没有运行实现或复现实验。分数为Design Delta/System Reach/Durability。

## 2610.02772 — Focused Views / FOVEATED

2+2+2=6，具体训练缺口深入。[v1 PDF](https://arxiv.org/pdf/2610.02772v1)HTML404后由官方PDF恢复，实际读页1–10的§3–4.5与Tables1–2，未遍历43页附件。Teacher-forcing中后段低loss可能借助早段事实，不认证脱离上下文后的atomic recall。每个preceding sentence使用独立Gaussian取整position偏移，只改RoPE key侧，queries与target-sentence keys不改；跨层同偏移、每step重采样，部署移除。DO期望loss与Jensen差额不自动证明每种扰动帮助；正margin另有shortcut假设。LTE先浅层atomic更新、再深层passage与anchor，不是单步同时优化保证。

Qwen2.5-7B/Llama3.1-8B、三UnFine负载/五编辑器局部对照，atomic30/30切片改善，locality29/30不等所有能力保持；完整passage和Llama一般能力有退步。Table2的ID perturbation/key-side与sentence-only/reversed order直接反侧，atomic与coherent目标不能互相代替。COIN*省略原COIN locality机制，不称全部原算法公平重现。单request事实编辑；采用段不报未读完整计算账目的性能数字，hardware/precision/concurrency/SLO未披露则不补写。

实际`TRAIN-SFT`Ch29:120–148已有loss位置、完整历史仍可见与反向路由，缺的是输入上下文依赖与离线事实使用的分账及focused-view分支。授权在mask链后窄写，编辑后的下游行为验收仍归Ch66，不扩优化理论证明。

## 2610.02819 — Text-Centric Post-Training

2+2+2=6，具体perception/reasoning训练接口深入。[v1 HTML](https://arxiv.org/html/2610.02819v1)实际§3–5、Tables4–6及AppB.1。九模型single-hop正确共同人口后组合推理仍失败；本地Qwen2.5Omni3B梯度一阶方向对照不是全局可分离定理。Thinker decoder LoRA r16/alpha32，encoder/projector冻结，SFT后GRPO；native/text同base与hyperparameters但训练数据/任务不同，不归全部收益于模态因果。Script-MCQ是数据格式比较后选择，不是原条件唯一解释。

Qwen2.5Omni7B推理mean+9.59而感知mean−.96，8×A100PCIe80GB；online GRPO input-token成本排除generated completions，GPUhours含generation/update，不以90%input reduction换算端到端成本。进一步有限nativeAV训练恢复感知且保留大部分推理，说明有条件组合而非文本全面取代AV。

实际`MULTIMODAL-REPRESENTATION`Ch23有representation/readout分责和native多目标capacity，尚未承载冻结输入接口而只更新语言推理consumer的训练分支；只补接口与分目标验收，训练算法仍handoff Ch29/33。

## 2610.02886 — Factual Poisoning 与 Derived Decisions

3+2+2=7，安全判断深入。[v1 HTML](https://arxiv.org/html/2610.02886v1)实际§2.1–2.3、§3.1–3.4、§4、§5.1–5.2。False/true数据配对训练、不同seed clean baseline；七membership probes与固定Walsh–Hadamard decoder读出组合，不把norm变化当错误生成概率。随机board依赖相同country facts，不作独立N。1000dosage八模型五seed条件中，direct事实正确不能代替derived decision；clean两seed disagreement不是校准证书。

Continued training也有共同forgetting；matchedMMLU差异未显著，不把全损害唯一归投毒。Replacement分支同预算corrective replay恢复直接事实却可保留derived failure，须与clean也接受correction的difference-of-differences分开；added-false分支多数恢复，不称投毒普遍不可修。Bushfire wording/数量factorial是另一限定案例，不外推真实组织损害。

实际`PLATFORM-SECURITY`Ch72数据/训练威胁及trigger邻域不承载这种纠事实后derived行为保留的控制；Ch66:1032的编辑后RAG conflict是另一问题，不能主题NoChange。窄写Ch72，评价成本、clean correction反侧与回退邻接保留，不新增安全充分性保证。

## 2610.02999 — OmniConfess

2+2+2=6，同轨迹modality对照具体缺口深入。[v1 HTML](https://arxiv.org/html/2610.02999v1)实际§4.1–4.4、§5.1–5.6、末limitations。冻结original candidate prefix及类替代，分别缺一个channel重算logprob/margin；free regeneration换轨迹不是相同干预。Task-specific risk选择word-expanded contiguous spans再局部替换，未选内容保留，不由该结构保证修订正确。输入dependency不等正确使用或事实蕴含；同prefix控制只消除这一轨迹变化，不消除全部混杂。

三Omni模型/六benchmark3540条；4×A40。TokenF1/GAV judge0–10不是calibrated correctness probability；binary judgment实际比baseline慢，PHD5.43vs2.23/CMM35.14vs20.64，少输出token不等低latency。三个部件局部ablation及相同修订预算支持受限机制，原candidate错误语义仍可能保留。Precision/完整batch/concurrency/SLO未披露，不补生产估计。

实际`PLATFORM-EVALUATION-SYSTEM`Ch66:1726–1732已有CoT删改与literal/compute分责，缺固定candidateprefix再干预inputchannel的具体诊断；授权一窄段接此链，spanrepair只作为后续可选消费，不把诊断owner改为生成器/真值源。

## Writeback 停点

必要原源与实际owner比较完成。oct05_daily写入后，root实际读取Ch29:138、Ch23:145、Ch72:110–112、Ch66:1732及各自邻接；四处POST通过，机制、直接反侧、成本和回退边界与上述采用范围一致。日级总Gate另验，不由本文件签发。另核02665的Ch24:280–282实际两段与邻接，通过独立原源复核限定的token embedding/readout/commit和低NFE反侧，保留旧Text VAE分支。

本轮轻量打开以上四项及六项CL（02856、02877、02926、02986、03052、03136）的当前官方abs：各仅列v1，页面未见withdrawn/retracted/erratum/corrigendum标记。原始Submission日期仍为2026-10-02 UTC，不据此改写公告公开归属，也未比较旧版本或遍历站点。该观察仅针对实际页面已有说明，不声称论文永不会撤回或存在勘误已被全网排除。
