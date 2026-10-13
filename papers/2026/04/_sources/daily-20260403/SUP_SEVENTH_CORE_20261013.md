# 第七批有限余项决定性core

## 当前 root 非作者实际必要原证复核

root 实际核 TAC00445 Eq1严格P(S+>S−)、Eq2 any real S：constant S 导致I=0而strictAUC=0，未声明no-ties条件的中心争议成立；5分D/noBooks通过，不自行修改作者定理，校准不能新增score信息。FLB00455 Eq3–7全vocab初logit、weight/plausibility及Table5 onlyThe29.9/full30.7实际已核；speech00489 §3.1–3.4/Tables1–2插层/merge初始化、恢复原路径与full退步实际已核，两项各6分限定Source通过，可继续owner/PRE，不授全图/部署效力。日期 extra4 保存两个owned/findable注册Apr2上界，与现MM首次announcement下界组合；未以Submitted单独认证。该回执不授Books锁或日级完成。

四项来自原68完整题摘，决定性方法/评价/直接反侧实际读到下列范围，无新发现；未自授准入/Source或Books。

## 00445 TAC：拟2+1+2=5，公式资格需纠错独核

[v1](https://arxiv.org/html/2604.00445v1)§3～4.2/5～6.5/必要AppendixA Eq12已读。scalar MLP width32/3ReLU层+BCE+ranking，后者不proper，只有纯proper population optimum才是posterior；实际earlystop validationAUROC。低信息score不能凭确定映射恢复discrimination，作者§4Remark承认须新增信息；校准ECE好不等ranking强。本文Eq1 AUC=P(S+>S−)未计ties，却Eq2说any real S且AppendixEq12用iid严格比较1/2。**作者未声明no-ties，自己的反例**：S恒定、I(C,S)=0时strictAUC=0，界失败；需要continuous/no-ties或half-tie处理才采用，不能自替作者修公式。五instruct模型/TriviaSciQPopQA有限标签；SciQ→PopQA AUC−6.04，8label某域−51.30，noisy50%大退，不授fewshot/noisy普适可靠。仅可受限采用score保留信息与calibration/ranking分责；MLP/ranking本身成熟，能否明确新增有限验证/修正而非只通用calibration需root裁决。必要公式更正不采正面保证，不扩所有proof/code。

## 00455 FLB：拟2+2+2=6

[v1](https://arxiv.org/html/2604.00455v1)§4.1/Eq3～7/5/6.2～6.4：缓存prefill首token全vocab logit，随t的γ(1−e−λt)加到当前logits，再以当前分布βmax plausibility过滤。不是恢复imagehidden/原采样分布，cached firstlogit带syntax而非视觉truth；RoPE距离本身非一般单调衰减证明。LLaVA1.5/InstructBLIP7B、500COCO/1004AMBER、samecaptionprompt、三runrandomsampling，heldout/fullhypersearch资格有限；masknoun/onlyThe消融说明The分支更强，full Hal30.7还劣onlyThe29.9，不能把收益全归视觉。早token全词表驻留及逐步加权/筛选计费，无硬件/precision/batch/SLO不授零cost；3turn/GPT4V只局部。新替代是跨步共享固定logit prior vs每步双前向，并显式保留语法prior/visual attribution混杂，不授firstlogit最truth或通用更grounded。

## 00489 speech-depth：拟2+2+2=6

[v1](https://arxiv.org/html/2604.00489v1)§3.1～3.4/4.1～4.4/Tables1～3：旧embedding rows及旧layers冻结，新speech rows+插层可训，移除插层才恢复原路径；全模型text仍退，不能把full-model preservation说exact。标准插层output proj0初始化identity；EBranchformer两个branch共merge要[I;0]+MHSA/conv输出0，speech-only cgMLP/text绕过该branch仍消费共享新增MHSA。SmolLM2 .36/1.7B、ASR48Khr/8192、无textreplay；LoRA144/356匹配trainablebudget而非普通小LoRA。1.7B插层interleaved text60.8低69，top66.4但WER更差；Ebranch .75B vs .66B非参数matched。新取舍是modal扩容与原路径恢复分开及branch共享merge的function-preserving条件，非所有ASR/text双保证；新增layer/全部fwdback成本与text-only原head/vocab合同保留，不能恢复全部vocabsoftmax后自动声称bitwise原模型。

## 00519 LGD：贡献前EX拟（决定性core，非降分）

[v1](https://arxiv.org/html/2604.00519v1)§4.1～4.4/5.2～5.4/必要A5～A6实际：成熟current loss−ωfull-data reference loss的learnability（原文引用2022已有）、classifier diffusion guidance、nearest-sample repulsion、逐阶段retrain与κ候选Top1组合。主增量是该成熟链搬到image dataset distillation提高指标，Table7是逐组件additive收益，不提出超出既有learnability/proxy限制的新机制或失效条件。§5“loss spike更大/迭代test增益”不独立认证information overlap或语义真实，reference自认正确不等GT；所谓JS2.04/1.57量纲/定义未核，不取通用data规律。地方性三runConvNet/ResNet、DiT生成、IPC20～100并非范围外；EX不是小模型标签，而是实际组合/指标尚无新增准入命题。若root认为increment-wise测量揭示新的具体blindspot，应定点重开这个决定点，不因source已读自动给Books。κ3某IPC还低κ1、强guidance退步，均是已成熟selection/guidance调参取舍，不自己加一般机制。
