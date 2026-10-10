# 2603.09740 — 全失败组的过程代理与局部教师分责（必要审阅与实际POST通过）

[Let's Reward Step-by-Step: Step-Aware Contrastive Alignment for Vision-Language Navigation in Continuous Environments exact-v1](https://arxiv.org/html/2603.09740v1)。作者实际完整 §3–5/Eq1–16/Tables1–5、Appendix0.A/0.B/0.C（Alg1–2、TableS1–2）；首次合读输出被截断的 §3 已单独重读完整，不将下载等同审阅。未核曲线像素、全部其余附录、代码或复现。batch3 完整题摘/current/history/owning arxiv.content/findable registeredMar11UTC02:20:46 上界和已实际官方 no-advance/announcement 最早 Mar11BJT08 下界夹同日，Submitted/Updated 单独非公开；current v1、无具名撤回纠错或更早先稿冲突，不证明全史。

2+1+2=5，唯一 TRAIN-GRPO；具体 all-failure 过程组选择与 anchor 局部教师/BC 的训练接口差额加深，不为 VLN 换任务、借用感知模型或笼统过程 reward 给分。

## 必要机制、反侧与采用范围

§3.1/Qwen3-0.6B 将 instruction 切 landmarks；CLIP global、GroundingDINO 高置信、SAM mask 的局部 CLIP 组合 Eq1，Eq2 对超过 softthreshold .2 的分数取轨迹均值。硬阈值 .25 与连续2步 landmarkadvance 用于选所谓 divergence，而不是新观测的失败真值。Eq3 firstzero、Alg1 一旦低分将后续 mask 全置0，且无低分 sentinel Eq3 为T+1/Alg1为T；Eq3 的 > 与 Alg1 的 < 在相等时有不同处理，保留差异不冒充统一实现。

反例边界不依赖额外实现：正确向远处地标移动且暂不可见，det不足、global sim .5、w1 .3 ⇒ S=.15<.25，就可首步标 divergence；因此 firstzero≠精确因果错误，保守称代理切点。正文/0B文字 SAM3 与 Alg1 SAM2 身份冲突，需对实现重开而非自填版本。mask黑背景、confidence/IoU与语义相似均可有共同错误，不以grounded命名认证correctprefix。

Mixed组保原 outcome（STOP+距目标3m）GRPO，用div/T>.5 的失败轨迹，在模拟器可恢复prefix状态时最多3次suffix重采，成功才BC新suffix、不递归；非实体动作撤销。Eq5含div的prefix与valid严格小于div之间边界不闭合，只有必要state/action边界确定后才可实施。无repair时 Eq15 分母空集合处理未披露，不将形式损失授可执行recipe。

全失败时选最高processscore的失败 anchor（不是成功positive），以actionLCS及scoregap挖hardneg，m+1子组归一；margin小乘κ=.5、只把负优势乘s=.5，anchor的代理prefix作BC，而div处contrastive positive来自**模拟器最短路径teacher action**。没有traineddomainPRM并不等无需教师/环境特权。单纯subgroup至少2不保证有非零variance：同score仍全0；正负缩放不保持零和，如+1/−1缩成+1/−.5，不授原outcome梯度等价或无噪声保证。

S4/0C Habitat/MP3D R2R-CE与RxR-CE、LLaVA-Video-8B正文与Video-LLaVA-8B TableS2身份差异，8A6000/BF16/DDP/max4096；SFT2epochs/globalB16约36h，RFT1epoch约24h。SFT文字10%warmup与表.03、constant与cosine不合，保留不自修。独立seed/CI、完整auditor/resampling吞吐与部署concurrency/SLO未披露。

T2 outcome-only相对SFT的R2R OS62.5→55.3反退；T4 K8→16 SR60.3→60.1/RxR60.3→59.9，repairs3→5 SR60.3→60.0/RxR60.3→60.1，更多rollout/repair非单调。T1 extra-data R2R SR64.7与正文62.7冲突，不采统一精数；现有主指标多改善只支持该有限recipe，不隔离每模块因果或证明隐式mapping胜显式多传感。73%所谓validprefix由同auditor派生，非独立人类或真实路径正确率，未核FigS1/S2像素。instruction解析、det/mask/CLIP每步、Krollout/重采/模拟器状态/teacher、reference/KL/BC/contrast与回归全部计费；不从同epoch称matchedcompute或通用recovery。

## actual owner 与逐字 PRE

actual Ch33 583–618 完整 DynamicSampling→固定bounds anchor→目标正anchor→DYPO全错teacher→EGPO→保持/时钟分支，Ch32/34开篇。已有段落承载重新分流与teacher共错，却不承载同一失败组内以视觉过程代理挑失败anchor、另在单切点引入simulatorteacher并仅BC代理prefix的具体接口。拟DYPO两完整段之后/EGPO之前两段；不覆盖原组或物理controller，不给Ch26复制训练loss。

拟段1：

全错组也可以保留自采轨迹，而把过程代理和局部教师分开用：由指令地标的视觉相似、检测与遮罩提议轨迹排序及切点，从失败组挑选过程分数较高的 anchor 和相似难负例，作子组相对更新；只对 anchor 的代理前缀施加行为克隆，在切点另用模拟器最短路径的局部 action 作对比监督。存在终局成功时仍让 outcome 主导，符合代理前缀条件的失败才作有界 suffix 重采，成功后补局部监督。这不是把最高分失败重标成成功，也不是恢复实体动作；重采需要可恢复的模拟器状态与明确 action 边界。

这一[受限导航训练对照](https://arxiv.org/html/2603.09740v1)没有训练独立领域 PRM，却仍依赖感知评分与模拟器教师。未见地标、共同感知错误或阈值失配可把正确移动截为失败，first mismatch 不认证精确错误点；相同过程分数也可能没有子组相对信号，负向缩放改变信用总量而非无偏恢复。增加 group 或重采次数并不持续改善，代理分数与真实成功须分别验收。逐步感知、rollout/重采、状态恢复、局部教师、reference与辅助目标及回归均计费；过程支持、恢复接口或净收益不足时，保留可靠 outcome、原 Dynamic Sampling、经核教师或保守跳过，不用代理前缀批准真实导航安全。<!-- source-family:SF-2026-ARXIV-2603-09740 -->

root必要Source/date/owner/逐字PRE已实际通过，作者按窄锁在Ch33 DYPO两完整段后/EGPO前写两段并顺读完整局部及本人注；root非writer实际599–616完整邻接、新605/607和本人2575末注回对有效Source/PRE，actualPOST通过、锁释放，见[本日独立裁决](./SUP_INDEPENDENT_REVIEW_20261009.md#09740必要sourcedate具体owner与逐字pre及实际写后通过)。这些行号是当次实际复核位置，不把后续共享章节位移当重审；本次仅将已通过状态同步到日报第37项，不重复发现/计数，不授DAY、实现或复现。
