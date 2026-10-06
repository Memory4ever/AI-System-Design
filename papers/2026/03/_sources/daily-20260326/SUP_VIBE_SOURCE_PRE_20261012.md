# ViBe necessarySource/sole Ch24差额与两PRE

2026-10-12。精确[2603.23326v1](https://arxiv.org/html/2603.23326v1)，原2+1+3=6/03-25日级门不改。实际必要§3.1–3.4/Eq5–6、§4.1–4.5/T1–2及supplement VRAM289–294；未核全部图像/视频、code或复现。明确长期部署组合差额后深入，仅采用Relay训练与部署组合，不把其他公式检查转全附件任务。

## 支持/关键反侧与停止

§3.2/F4/Eq5–6明确低resimage先训练ΔW1，merge成W1并冻结，再训练highresimageΔW2；在线却用原W0+ΔW2，不用W1+ΔW2，不能把训练base与交付base标成同artifact。原作者解释ΔW1只模态/ΔW2只空间“decoupled”，但这不是独立表征证明：ΔW2是在含ΔW1的参数条件上训练的，移除ΔW1后的行为仍须验实际video。§3开头coarse-to-fine先原res视频后highres refinement，非单次全高res生成；“无任何video数据”只新增adaptation，base已有video训练，不消灭全部视频监督。

Wan2.2 5B(1280×704，VAE16×16×4)与14B(832×480/1280×720，8×8×4)；synthetic FLUX1.1ProUltra图2.3K、2752×1536，stage1/2各3Kiterations/singleA100/about1day，allinference A100；rank/schedule/optimizer只外库defaults，具体版本和数值不在必要HTML披露，不授已验fullrecipe。Precision、batch、concurrency、steps、尾SLO Not Disclosed；supp VRAMstage1 27.99GB/stage2 46.28/4Kinfer74.82，不是端到端延迟。§4.1文字4K3820×2176与T1 3840×2176不同，不补造统一width。60VBenchprompts×5randomseeds/35participants，指标overall只是六metrics平均，不是完整任务或安全truth。

T1subjectConsistency1080P95.5低于I-Max95.7，4Kimaging66.1低于CineScale66.3，不能整套全胜；T2去Relaybackground97.9高于full97.1、去X0subject96.3高于95.2，不借overall认证各项更优/因果完整解耦。ΔW1移除的对照/模态迁移局部可支持接口，不证明唯一最优。HFATO Eq11 degraded+noise的路径与前普通FMalpha不同，不采完整loss等价；GCLFA inward文字与Eq7扩大window/mask形式不能认证恒定receptivefield，Eq10乘mask也非完整实现证明；两者不影响只采用原Eq5–6Relay合同。§4.5few-step/I2V兼容仅示例不授零退化/净加速，pool2/4反侧和原image合成/两stage/GCLFA/reference低resvideo/refinement/VAE费用均保留。

## actual Ch24 gap/锚

actual Ch24开篇/1318–1419完整邻接已读并复用本轮前后Ch23/25开篇：12013是latentteacher数据生产和部署去codec；13448两段只subspaceshift/恢复表示；23605是AE/prior/discretedecoder独立artifact。均无“训练在W0+ΔW1上优化ΔW2，交付回原W0+ΔW2”的参数条件迁移；模态与空间压力的分阶段适配及退出第一stage是具体gap。只sole MULTIMODAL-GENERATIVE-PARADIGMS Ch24，不另重复LoRA数学owner。拟在13448完整两段（最后以“回退像素/原表示空间。”）之后、`### 连续 Latent 与离散 Token 需要分别拥有版本`之前两段+本人静态注。不移原块，未root锁/未写/无POST。

## 两逐字PRE

迁移边界也存在于适配器组合，而不只存在于 latent 空间。将视频生成器用高分辨率图像直接适配，可能同时改变模态行为与空间能力；一条分阶段替代先在低分辨率图像上训练第一适配器，合并并冻结这些权重，再在该条件上训练高分辨率的第二适配器。交付视频时却回到原主干，只加载第二适配器，不保留第一适配器。训练所依赖的参数条件与交付组合因此不同，两个增量须分别保存，不能把合并后的训练权重误发为视频 artifact；“第一项只管模态、第二项只管分辨率”仍是需要视频对照验收的解释，不是低秩相加自动提供的功能解耦。<!-- source-family:SF-2026-ARXIV-2603-23326 -->

原受限分支仍先生成低分辨率视频再细化，新增适配只用图像也不抹去主干已有的视频训练。合成图像、两阶段优化、粗视频、细化 attention 与完整编解码全部付费；综合分更高时，主体、背景或细节指标仍可能分别退步，少步与图生视频示例也不认证所有交付组合。更换主干、分辨率、adapter 组合或 attention 路径后，应重验模态一致性、质量及总预算；迁移失配时，保留原视频模型、独立超分或经过验证的完整视频适配，不因第一适配器退出部署就宣布训练成本消失或通用无损加速。

## 自身静态证据注PRE

- `SF-2026-ARXIV-2603-23326` — [ViBe exact-v1](https://arxiv.org/html/2603.23326v1)必要§3–4/Eq5–6/T1–2及supp VRAM；只采用训练W0+ΔW1条件下学习ΔW2、交付W0+ΔW2的组合合同。保指标反退/模态解耦未证、base video监督与coarse-to-fine/全费，isolated GCLFA/HFATO未闭合recipe及4Kwidth口径，不授全胜、原生单段高res/zero-cost或few-step通用无损；未核artifact/视频像素/复现。
