# 13162 DiT-IC 必要原证与 Ch24 受限差额

resume_mar17，仅2026-03-17补03/16自然日。完整v1题摘/日级夹证复用SUP_AB_MULTIMODAL第4行与匹配官方DataCite/独核；当前官方abs只有v1，无已给出的撤回/勘误标记，不遍历项目。2+1+2=5，具体采样初态/监督差额深入；未写/未POST，不计safe。

## 实际必要 Source

[exact-v1 HTML](https://arxiv.org/html/2603.13162v1) §2、§3.1–3.4/Eq1–11、§4.1–4.3/Tables1–3、§5、§6–10/Table4必要机制和直接反侧；不读§11整批视觉实例/参考文献，不称图中数字已视觉核验，未核artifact/复现。

从entropy-coded结构化latent而非纯Gaussian开始，在32倍下采样空间用SANA DiT一次重建；entropy hyperprior的sigma经projection/monotone map提出空间pseudo-time，相关性不认证真实误差。冻结encoder的latent作为alignment target，同时训练DiT/decoder LoRA；不是外部teacher轨迹蒸馏，也没有证明保持multi-step原分布。Eq4中的m只是加性常数，不采用其“鼓励不同方向分离”解释。text/latent contrastive训练后用compressed-derived条件，Eq5的hat-y输入/输出记号不够给出可执行顺序，只采用部署无文本输入的受限接口，不发布精确solver。低于.01bpp原文承认latent语义可能不足。原codec仍含四步autoregressive Gaussian参数/算术解码，一次DiT不等全部pipeline一次forward。

150k图/256patch100k步骤B32与512patch60k步骤B16，§4/8两RTXPro6000而§9三天两A100口径不一，不拼总compute。Stage2前30%关闭adv/开启语义alignment，后切换；不同decoder/entropy modules/precision/预训练容量变化限制单独归因latent深度。Table1 ours .15s FP16对baseline .27s FP32不能当同precision收益；Table3 FP32 1024总.273对.34约19.7%、2048 .982对1.67约41.2%，不是正文“总体76%”；1024 codec .008对.04实际80%非表−30%，仅保表原组件测量，不授30倍普遍headline/16GB laptop/INT8质量保证。Table2去adv在PSNR/MS-SSIM甚至LPIPS/DISTS均有更好BD-rate，不能称无保真代价；Table4 CLIC KID反退。61人偏好与OCRBench pipeline均有限，感知/识别代理不证明全部原图内容无损。train/eval硬件、PyTorch2.8/CUDA12.8作者配置有披露，但完整长度、batch/concurrency/SLO、编码/训练/模型制备/量化全费未齐。

## actual owner / 两段逐字 PRE

实际Ch24 163–181（DDPM采样配置→空间restoration map→SCD历史条件）、774–798（teacher/学生状态与监督目标），Ch23 369–387 rate/consumer与Ch25开头已读。Ch23已有rate-distortion与supervision identity不承载此一次reconstruction初态/entropy-sigma接口，Ch24已有输入noise map也不包含entropy model共享sigma和frozen codec target。这是具体差额，不假NC；soleMULTIMODAL-GENERATIVE-PARADIGMS，不复制codec理论到Ch23。

拟在Ch24原171 restoration段之后/SCD历史段前插两段，仅支持局部接口。尚待非准备者必要Source/实际owner/PRE独核与root窄锁。

量化压缩的重建初态也不必是纯 Gaussian：码流解出的 latent 已携带图像结构，继续用通用多步生成链很简单，却可能重复支付并不必要的采样。另一条受限分支在较深的空间瓶颈上适配保持网格分辨率的 DiT，让 entropy model 的局部方差经可学习映射提出一次重建的 pseudo-time；冻结原 encoder 的 latent 作对齐目标，同时适配 DiT 与 decoder。它共享的是压缩模型给出的不确定性代理，不把方差认证成原图误差，也不把 encoder 对齐称为外部 teacher 轨迹蒸馏或原生成分布无损继承。[DiT-IC 的必要方法](https://arxiv.org/html/2603.13162v1)还用训练期文本—latent 对齐换部署期 latent 条件，文本 encoder 可以退出这条部署链，但训练 caption 与对齐费用并未消失。<!-- source-family:SF-2026-ARXIV-2603-13162 -->

一次 denoiser 仍要付算术解码、条件映射与 VAE 重建，深瓶颈也会把丢失细节交给生成 prior。应固定 codec/encoder/decoder、码率、精度及完整解码协议，分别检查像素、感知与内容，而不由较短反向链签发原图保真或总省费；有限对照存在感知与失真取舍、部分代理反退，不同 precision 或关闭 tiling 的组件计时不能拼成普遍速度。极低码率、文本/数字内容失真或硬件不适配时，保留更多 bits、原 codec、较保守的重建与独立内容核验；是否增加采样步数须另验，不把这条结构化初态的重建分支搬成任意生成的一步保证。<!-- source-family:SF-2026-ARXIV-2603-13162 -->

静态源注：

[^src-ditic]: [DiT-IC](https://arxiv.org/html/2603.13162v1)（2026-03-16，exact-v1）。必要审阅§2–10/Eq1–11/Tables1–4的采样初态、监督接口及直接反侧；只采用entropy-model方差代理与冻结encoder目标的一次重建分支，不采用精确条件消费recipe、普遍速度/内存或保真保证。完整费用和异精度/组件计时分开，未核artifact或复现。

若未来采用精确recipe/性能，只合并一次请求：输入到输出条件顺序、实际lambda/mapping、同precision完整encode/decode/tiling计时与训练GPU口径，接受配置/最小trace/勘误；本轮不据该未闭合部分写保证，不让它阻塞受限接口。
