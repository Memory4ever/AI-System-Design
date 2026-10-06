# MULTI-VQGAN / VICL / Vad-R1-Plus 必要证据提案

精确v1已核日期与准入，本包只有必要method/eval及直接counter。缓存2601.IDv1-method/fuse/fusion/eval/counter-necessary.txt，author actual读；待root终裁，无复现，不以recipe未写造长期gap。

## 10107 MULTI-VQGAN — 拟5标准Only

[原文](https://arxiv.org/html/2601.10107v1)§3.1–3.3 Eq4–19/4.1–4.4/D3。单promptpool一次融合易丢差异→相似度top/bottom与all三个组frozenpromptproducer、allmainQ读取high/lowguideKV的中间8–14blockcrossattention→局部表示fusion位置/producer分支替代。DRL借用不能证明相似度bins识别独立generativefactors或causaldisentanglement；中间layer功能为hypothesis非普遍语义分工。

先CONDENSER fusedprompt lossalignment+CE/frozenMAEVQGAN，再训练MULTI+decoder；MAEVQGAN是否frozen随阶段，不能笼统全frozen。K8/16对应4/4或8/8、LR.05/10epoch/batch16/V100，precision/seed Not Disclosed。PASCAL5i/VOC/ImageNet/COCO→Pascal有限split，ablation1/2/4/8/16groups并非架构容量和预算相同；randomguide/onlyhigh/onlylow/crossattnavg/backbonefrozen局部controls不证明DRL因果。11block/7range最优是局部配置；单branch减少内存/额外三encoder成本不能由accuracy替代。Only局部fusion实例，不授通用新foundation机制/精确Existing，无Books。

## 10117 VICL — 拟5标准Only

[原文](https://arxiv.org/html/2601.10117v1)§3.1–3.4 Eq3–25/4.4/4.6/C3。固定layout与semanticfusion混合→先trainfusion，再freeze fusion+MAEVQGAN学八layoutadapter，选四后supportqueryswap共同FT→布局适配与producer语义训练分阶段的可核替代。Attention图像权复用labels/Adapterresidual/bottleneck成熟本身不计原创；swap用prediction作为newsupport会带伪标签error，非真reversible/防shortcut因果。

**§3.3明确按heldout testset排序top4再finetune**，不自行改validation，未确认与finaltest是否same，不能授无selectionleakage或泛generalization；不同布局selection成本额外。Fusion最多150epoch(seg/det)/10(color)、八MLP各10、joint10/N2/batch16/SGD.03/V100/λ.6；precision/seed未披露。MAEVQGAN/CONDENSER pretrained/baseline mix、componentablation和MLP7.7%params/.02%GFLOPs是相对fusion不是全E2E，timing获益只局部。仅报告接口分工与evaluationboundary，不冒exactExisting/长期gap，无Books。

## 10165 Vad-R1-Plus — 拟5必要安全/设计反证深入Only

[原文](https://arxiv.org/html/2601.10165v1)III-B/C reward/IV-A settingsmetrics/IV-C2 rewardablation/IV-D1/3–5。只答案reward可用少数frame猜异常→abnormal删自己predictedinterval再问期望变normal奖励，normal随机删开头/结尾后变abnormal负奖→具体reward证据依赖检验，需与causal真值分开。删片同时改变时序/时长/context，original异常位置可能错，trimmed“只normal”未经独立保证；samepolicy自检不认证干预causal/真实safetyrisk。

Qwen2.5VL7B SFT1epoch→A2GRPO1000steps/group4/16frame/max128×28×28，teacherQwenVLMax frame16间隔描述形成PerCoAct，riskLow/Medium/High匹配标签+depthstagetags而非calibratedprobability。hardwareprecision/总SFTRLbudget Not Disclosed；tagcount深度不等实际推理足够。tableV reward组合有局部质量/consistency改善，但riskshortcut早期非SFTreward稍高、outputlength/SFTpretrain共同变化不授groundedcausal。judge/referencelexical/embedding/LLM分层不是物理真值或action授权；Double/TripleRight额外category一致亦非reliability证明。保留具体设计反证/检验局限，仅报告受限实例，无Books/精确Existing，不扩大到所有videoanomaly科学应用。

