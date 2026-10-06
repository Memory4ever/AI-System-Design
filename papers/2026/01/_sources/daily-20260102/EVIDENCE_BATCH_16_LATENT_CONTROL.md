# Jan02 有限五项：激活干预、reward gate、动作codec、层级测量、latent依赖

最新：本五均终处置。root实际核24143 Eq7–9及128+128/64 HarmBench、keyword/Guard2与Ch15/66具体正文，24125 IV-C Eq2–5/V-D matched1200/50rollout与Ch26 151–164，24119 §3.2六MC/path gold/§4 evaluator与Ch66 367–410，三项标准Evidence与具体已有覆盖通过；不是逐step算法/ERIQ或该path gold已写入。24102 §4.2/4.3/5.4.2训练prior、GP regularization与采样covariance身份未决，5分中心终态暂缓通过，不断言实现必错或全部实测无效。GARDO必要源、owner及实际正文/邻接/末注POST通过。以下待核/提案字样为历史过程，由本段覆盖。

五完整v1题摘与具名准入已root校准：24143=2+1+2=5、24138/24125/24119各2+2+2=6、24102=2+1+2=5。作者以下必要core/评价实际读；独立Evidence/Books待root，不授全附件、代码核验或复现。DATACITE_POTENTIAL保存created原值依次Jan1T03:04:56Z/03:04:48Z/03:04:30Z/03:04:21Z/03:03:57Z，配holiday/noadvanceID下界Jan1T01Z、各created+1秒上界；完全落本窗，非注册精确公开。FACT v2 Submitted Jan1T17:42:44Z但Updated Jan5T01:23:19Z，不当本窗新事件。当前abs说明未见相关撤回标记，不展开版史。

## [Activation Steering for Masked Diffusion Language Models](https://arxiv.org/html/2512.24143v1)

Actual §3.1–3.2/Eq1–9/Alg1、§4.1–4.2/Table1/Fig5–6及§5。对比prompt均值方向在每个reverse step作投影移除：Eq7为 `h' = h - <h,v>v`，不是任意强度的方向相加。prompt、response、both及layer scope不同，不能把prompt干预说成其他logits不变。LLaDA8B-Instruct；128 harmful/128 harmless训练，64 heldout HarmBench。关键词拒答与LLaMAGuard2 safe label分开，response-only可产生空/极短输出，低关键词拒答不代表任务帮助或有害率低。未给独立utility保持；hardware/precision/完整decode-budget未在所需设置披露，不采用安全保证。

具体Existing提案：MODEL-MULTI-HEAD-ATTENTION Ch15 279–284实际承载白盒对比子空间干预、校准、副作用与独立verifier；PLATFORM-EVALUATION-SYSTEM Ch66 688–690实际承载相同人口上refusal/content compliance/harmful uplift分责。不是称Books已有本篇逐step scope公式；受限MDLM实验留报告，待root核。

## [GARDO: Reinforcing Diffusion Models without Reward Hacking](https://arxiv.org/html/2512.24138v1)

Actual §4.1–4.3/Eq3–8、§5.1–5.2/Tables1–2、§6及A.1。Eq7是批内优化proxy winrate减辅助winrate均值的相对差，选择高差样本施KL惩罚，不是已校准human truth；top10%随20步窗口调节。KL超过epsilon或100步重置reference，使local anchor改变，不能由每次KL推出离原始base的累计界。DINOv3最近邻距离只缩放正advantage。Aesthetic/ImageReward同时参与gate与所谓unseen评价，DINO同时参与训练/多样性评价；这些不是独立heldout instrument，不授无reward hacking。

必要公式定位：Eq7 `U = w_proxy - mean(w_aux)`；reference hard reset在§4.3。SD3.5Medium、512²、G24/batch6、train10/eval40步。LoRA披露冲突：§5 alpha64/rank32，A.1 alpha32/rank64，保原值不选边。辅助评分、DINO及cache成本未可据“negligible”外推；hardware/precision/部署SLO Not Disclosed。

具体gap提案：TRAIN-RLHF Ch31 275–304有冻结KL锚点/平均slice及分布改写，尚未具体承载“相对ensemble rank仅选KL惩罚人口、reset改变anchor identity”。拟beta段后窄一段，分别保存selected population/anchor版本、累计与局部移动、辅助instrument及独立验证成本；失配回冻结ref或统一惩罚。只是受限控制分支，不采理论安全保证；待root必要源/owner授锁。

## [Unified Embodied VLM Reasoning with Robotic Action via Autoregressive Discretized Pre-training](https://arxiv.org/html/2512.24125v1)

Actual III/IV-C Eq2–10、V-A–D/TableIII/Fig7。FACT固定离散codes由VQ产生，连续FM decoder消费当步a(t)、codes与time求解，不是codes一次解出无成本动作；Euler/NFE仍有预算。ERIQ6052个reasoning QA不等执行成功。TableIII相同1200示教后，每setting50 rollout；高QA可同时有低SR，grounding近目标亦不等完整成功。重构MSE/码本容量不证闭环安全，混合预训练数据/视角也非等compute机制因果。Qwen2.5VL3B/GenieSim/AgiBotG1；hardware/precision/batch/SLO所需部分未披露。

具体Existing提案：MULTIMODAL-EMBODIED-VLA Ch26 151–157实际离散codec容量、连续FM detokenization与闭环/budget合同；161–164离散planner/连续refiner及freshness。保本作QA/action评价反侧，不称Books已有ERIQ或该VQ loss式。待root必要源/owner核。

## [GeoBench: Rethinking Multimodal Geometric Problem-Solving via Hierarchical Evaluation](https://arxiv.org/html/2512.24119v1)

Actual §3.1–3.2、§4.1/4.2/4.4/4.6–4.8、Tables4–6及C.1/C.4。Formal engine给具体proof path及六MC任务；unused premise/theorem和first faulty branch的gold绑定提供路径，不能自动替所有合法证明，也不读模型内部因果。1021题/76构型；八名博士交叉核gold，与五名human测试人群不同。直接index与CoT后的LLM/substring解析不同，CoT预算未matched；跨模型相关性不授训练哪个能力的因果收益。rotation±20/文字条件及CoT faulty-branch退步是局部反侧，不采普遍视觉/推理优越。8A10080GB；C.1 temp.95/max8192/top-p.7，API至多5网络retry；precision/concurrency/SLO未披露。

具体Books待定：PLATFORM-EVALUATION-SYSTEM Ch66 367–403实际承载合法acceptance set、过程oracle、同输出事件parser及direct/CoT paired合同。需要root判断“提供proof path gold vs所有合法解”的具名测量分责是否仍有窄gap；不得只因geometry主题当Existing，也不把engine path当唯一真值。

## [Autoregressivity in the Latent Space of a GP-VAE Language Model: An Empirical Ablation Study](https://arxiv.org/html/2512.24102v1)

Actual §3/Eq5、§4.1–4.5、§5.4–5.6、§8–10/12。原prior `N(0,K⊗I)` vs `N(0,diag(K)⊗I)`；encoder/parallelCNN decoder固定不等prior/KL objective固定。§4.3明写KL(q||GP prior)并clip cap8/beta~.35；§5.4.2又说两者same regularization toward GP。这里需区分是否只sampling时去correlation，还是训练prior也改；相同cap不修复目标身份。原短摘（§5.4.2）：“same regularization pressure toward the GP”。这影响中心归因，拟5分暂缓该命题而不否全部实测。

WikiText2/103、GPT2tokenizer、train64，作者pyramidal与TCN+两实现非第三方复现。§4.4 conditional decoder PPL不与AR marginal PPL相比较；cat_frac定义末尾持续短loop，Lmax/重复人口须绑定。GP prior logdensity是该prior一致性，不能独立证明capacity公平。GPT2评价不同并非数学上不能评NAR联合分布；作者factorization-bias解释不当已证定理。长续写到2048/3072的collapse是受限实验，不授任意长度稳定。hardware/precision/训练与生成完整预算未披露。

恢复只需精确v1实现的训练prior、KL/clip/采样covariance身份，以及同预算sample/seed协议或作者澄清；不要求重审全部附件。不写Books，root中心争议复核待。
