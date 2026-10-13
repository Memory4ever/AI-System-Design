# KeyframeAnchoring17651：双端条件的注意力消费 / 必要准备

resume_mar17，仅03-20补03-19，原2+1+2=5与独核§30准入/day复用，不重定公开日期。本准备不自授Source/PRE/Books/safe/DAY。

## 1. 原证停止与采用接口

[exact-v1 HTML](https://arxiv.org/html/2603.17651v1)完整AB、§3/Eq1–8 L98–144，§4/TGI人口与关键§5/T1–3/消融/直接评价反侧L145–214，S2评价L279–290、S3/T S1–3与S4局部L294–338、S5.1人口L343–363、S6/S7直接限制与人评L453–462实际读。current abs同题四作者、单v1，Comments accepted CVPR/代码released，未见采用相关纠错，不打开实现/像素视频/所有附图。网页返回References和prompt部分仅邻接，不称全文附件读完。

Wan2.1 FLF2V的first/last与中间零帧经VAE成为条件latent，UMT5 text及端图CLIP features进入context。每个cross-attention head在端点video query行的分布，经head/query平均成anchor；沿帧位置插值，再以target/current平均分布的log差作广播logit bias，分开first/last/text三cross-attention后等权平均。此anchor是当前模型的条件分配，不是端图正确对象/中间运动真值。self-attention另只改时间轴RoPE相位行的端/中scale，空间轴保留；它改变实际Q/K消费，不仅重新标注时间。高/低scale不为任意Q/K证明attention权重单调局部化，原文的局部/全局解释只作为受测设计动机，不采通用局部性定理、精确hyperparameter recipe或端图硬锁。

## 2. 评价与反侧

原14B Wan FLF2V、A6000 48GB、bf16、480×864/15FPS、tiled；seed固定但未多seed/CI。220视频经主体/运动过滤，GT中间帧抽样供GPT4.1 caption/challenge并由作者改标签，prompt可能提供端图不可见信息，因此语义成绩不是仅两端恢复真实事件。S2视觉encoder称XLM-RoBERTa-Large与主文CLIP命名不齐，不合成精确部署recipe。六VQA平均只是代理，不由投票造独立真值；12问题/20余人随机位置人评与S7 doubleblind保留，12约10%与220人口需分清，不造整体人口认证。

T3 KAB-only PSNR17.63→17.62/SSIM.6179→.6174/FID82.90→83.01/VBench9.904→9.896均反退；联合PSNR/SSIM低于ReTRo-only。T1的65-frame FVD .2820按↓优于FCVG .2938，不作为反退；25-frame S1 VBench9.991低于Wan10.103。S2/S3较大bias或scale可用更高VBench换更差其他质量，不采全质量支配；严重几何/运动畸变底座不能完全恢复。无需训练仍计三支attention、anchor统计、bias、重标相位、全部去噪/VAE与评价；latency/峰值显存/总fee/batch/concurrency/SLO未披露，不授training-free等免费。支持与直接反侧足即停止。

## 3. actualsole与差额

sole `MULTIMODAL-GENERATIVE-PARADIGMS`，[Ch24](../../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)。实际完整319–349的条件/guidance/运动接口、1715–1762 plan/event-keyframe/修订与相邻Ch23/25入口已读。现1731事件/latent插值仍未承载**同一生成时端点自己的cross-attention分布→中间帧logit bias**与**时间Q/K相位局部重标**的消费者差额；不是现有keyframe主题即可NC。拟原1731完整family marker后、诊断内容消费前一短段。不在Ch13重复RoPE推导，不在Ch25推世界动力学。

## 4. 待裁 single literal PRE

已有首尾帧仍可能对应许多中间运动，外部事件计划不是唯一补充方式：一条受限插帧分支从当前模型端点的 cross-attention 分布提取平均 anchor，沿中间帧插值，再以目标与当前分配的差异修改条件 logits；首帧、尾帧和文字分别读取后组合，self-attention 另按端部/中部重标时间 RoPE 相位，空间坐标保留。这让生成器直接消费双端线索，却不把 attention anchor 当作真实对象或运动，也不由相位 scale 证明任意权重必然更局部。[有限双端视频对照](https://arxiv.org/html/2603.17651v1)中单独 bias、部分指标和较强参数有退步，严重底座畸变仍无法完全恢复；文字还可能来自端点不可见的中间帧信息，语义得分不证两端已识别真实事件。分支 attention、anchor/bias、完整去噪、VAE与评价均计费。需要已知轨迹、几何或真实环境决策时保留显式条件和独立用途验收，短小近线性运动仍可用普通插值，语义或净预算失配时回退原双端生成，不由无需训练批准无损、物理可信或免费实时。<!-- source-family:SF-2026-ARXIV-2603-17651 -->

静态源注：

- `SF-2026-ARXIV-2603-17651` — [Anchoring/Rescaling exact-v1](https://arxiv.org/html/2603.17651v1)必要§3/Eq1–8、§4–5/T1–3与S2/S3–4直接评价/参数反侧、S5.1/S6–7。仅端点attention anchor消费与时间相位重标接口；保proxy/特权caption、质量反退/底座限制与全费用，不授硬端点、局部性定理/精确recipe、真实运动或无损实时；未核代码/图像像素或复现。

交resume_review17_18非preparer必要Source/实际owner/原single PRE与static一次裁；未授锁不写Books，不将准备或准入当safe。

## 5. 授锁后的实际窄写 / writer读回

2026-10-12 root确认20155实际POST释放Ch24后，授本family原09094完整段后/诊断消费前一literal及静态注窄锁。作者只按§4原文写，正文当前1737、本人静态注2505；实际完整1725–1751及章末7行读回，事件计划→双端条件消费→诊断内容责任衔接保持。literal逐字匹配true、正文family marker仅一处，numstat82新增→86新增仅本family4行，限定diffcheck0。原20155正文/注及其他family未改。不自授POST/safe/DAY；交resume_review17_18一次nonwriter完整局部/本人与邻注实际回读。
