# Spectral schedule 19222：数据依赖噪声日程与推理时条件接口

root sole准备，仅03-21补BJT03-20。原完整题摘与有限余项准入独校可复用；固定日程按分辨率调参→原文以每图频谱限定噪声区间并在生成前条件采样日程→需要重新判断日程、denoiser条件与训练/推理身份。2+2+2=6；只给这个新接口评分，不把通用diffusion或小步加速原则算新贡献。明确差额定点深入，不扩视频/所有生成论文。

## 身份与公开归属

实际[official exact-v1](https://arxiv.org/abs/2603.19222v1)题摘/header/history：Carlos Esteves、Ameesh Makadia，v1提交2026-03-19，当前v2五月，有版本记录但无明确撤回/纠错说明。不把提交日当公开日，不全版diff。实际arXiv-issued DOI DataCite findable：v1Updated2026-03-20T01:20:09Z，created/registered同日02:31:29/30Z；Available只2026-03。与本批已核公开批次夹证只限定BJT03-20日级归属，不补公告精确时刻或认证不存在更早稿。

## 最低充分原证与边界

实际[exact-v1](https://arxiv.org/html/2603.19222v1) §3/Eqs1–5/Alg1–2、§4.1–4.5/Eqs6–24、§5.1–5.4/T1–2与§6；必要Appendix A/Eqs25–30、B.2/Eqs35–43、C/T3–4与D.1–D.3。仅围绕日程身份、可得性、对照与直接反侧，不遍参考文献、所有图像、代码或版本史；未复现。

训练由RGB图像的radially averaged power spectrum拟合两参数power law，低/高频功率与容差决定噪声上下界；uniform frequency与power-weighted frequency映射在logSNR中混合。A的推导先对独立白噪声取期望消除cross term，因此界是频谱近似/期望意义，非每个样本图像的信息量、感知损失或全分布距离保证。径向平均忽略方向/phase，monotonic power-law假设不能授任何latent/视频同律；B公式alpha=-1需极限处理，GMM参数本身也不认证每样本单调性。不作为生产精确recipe。

生成前并不知道输出的真实频谱：另训class-conditioned Gaussian mixture sampler采两参数，再条件denoiser于当前/最小/最大logSNR，guidance interval改为t。训练用clean spectrum，生成用sampled spectrum是不同可得性人口；不能说从待生成真图直接算日程，也不能部署时任意替换已训模型日程。输出频谱操纵同时改schedule/conditioning，不认证精确纹理或语义控制。

T1/§5为ImageNet单阶段pixel diffusion对照，非所有LDM/蒸馏模型胜出。§5.1称ours/SiD2指标5runs均值，D.3每评价50K生成样本/训练集参照；不当独立训练seed或人审。T2混合FID优于固定median，但IS 297.0低于median299.3；frequency-only和power-only均有取舍。移除MinMax condition、改回logSNR interval或oracle spectrum是局部对照，不认证每个调整的跨模型独立因果。§5.2/Fig3高步FID反而略退，少步优势不是单调。T1还包含不同规模/codec/求解器；最有意义是同SiD2架构/protocol的限制比较。

D.1小/重计算差patch大小，D.2每分辨率另训三分量sampler100K steps/batch128；loss bias、guidance与step仍调参。基础diffusion训练完整设备/precision、端到端latency、concurrency/SLO及总搜索费未完整披露（Not Disclosed），图像token长度不适用，分辨率/采样步与class条件另保。频谱提取/拟合、GMM训练/采样、FiLM条件与质量/参数搜索都付费，NFE不等全部时延。

## Actual owner与最小改动

重读Books背景/理念/写作及ROADMAP，唯一 `MULTIMODAL-GENERATIVE-PARADIGMS`/[Ch24](../../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)。实际140–172完整去噪目标→在线时间分配→reverse sampler，Ch23/25开篇交接已读。现有正文150说明共同目标身份，156–158是误差驱动时间采样；尚没有data-dependent谱日程与未知输出下条件采样/MinMax消费的差额。拟在150共同身份段后、instance-unlearning前一段，不复制相邻误差分箱机制或写成模型排行榜。

## One literal PRE（未授权写入）

固定噪声日程在数据尺度稳定时容易训练与复现；图像分辨率或频谱变化后，同一logSNR范围却可能在部分阶段过度破坏结构、另一些阶段只重复细节计算。一个受限分支以每图径向平均频谱拟合噪声上下界，再混合偏向频率覆盖与功率覆盖的日程。这里控制的是加噪尺度与训练人口，不是测得每个样本的语义信息；独立白噪声下的期望频谱和power-law近似，也不认证真实输出分布或感知误差。生成前没有clean图可算频谱，因此另从条件采样谱参数，并把当前与端点logSNR共同交给已训练denoiser，连同guidance时窗保持配置身份。[单阶段pixel图像对照](https://arxiv.org/html/2603.19222v1)支持这种适配接口，但高步数仍可反退，固定日程在部分指标更好，也不能推广到latent或视频。频谱拟合、额外条件采样器训练/求值、调参和完整生成都付费；条件谱失准、假设失配或质量回归时，保留已验收的固定日程、原条件模型与采样网格，而不是部署时随意换掉noise schedule来宣称无损加速。<!-- source-family:SF-2026-ARXIV-2603-19222 -->

拟本人静态注：

- `SF-2026-ARXIV-2603-19222` — [Spectrally-Guided Diffusion Noise Schedules exact-v1](https://arxiv.org/html/2603.19222v1)，必要§3–6/Alg1–2/Eqs1–24/T1–2、A、B.2、C/D。仅频谱依赖noise schedule与条件采样/端点conditioning接口；保期望/拟合假设、生成未知谱、pixel-only、高步与指标反退、调参/训练/完整费用，不授latent/video普效、全成本加速或分布保证。未核代码/复现。

交非准备者一次必要Source/date/actual owner/逐字PRE限定审阅；未写、未safe、未DAY。

## resume_mar18 非准备者必要 Source/date/owner/PRE 裁决

2026-10-12 actual独立读 exact-v1 §3/Alg1–2、§4.1–4.5/Eqs6–24、§5.1–5.4/T1–2/§6，必要 A/Eqs25–30、B.2/Eqs35–43、C/T3–4、D.1–D.3。实际 v1/current官方题摘、两作者/header/history与原DataCite日级夹证一致，当前v2五月Accepted ICML'26不等早发或撤回/纠错信号；不全版diff、不补精确公告或无先稿断言。训练clean RAPSD与生成前class-conditioned谱采样的可得性分离、当前/端点logSNR FiLM及t-guidance消费接口有直接支持。A消cross只对噪声取期望、径向power-law近似和GMM无单调保证，均未被PRE升级为样本/全分布保证；T2固定median的IS优于mixed、高步FID反退、pixel-only与loss/guidance调参及额外sampler训练费用在原稿近文。5 runs不认证独立训练重复，50K生成指标不等人审或wall-clock，未核代码/复现或无关生成附件。

actual Ch24 140–176完整去噪目标→已验像素反传分支→instance修订→误差分箱→reverse sampler与Ch23/25交接已核：共同schedule/time/param身份段没有谱依赖条件采样接口，误差分箱亦非同一机制。原one literal PRE及本人static逐字有限PASS，2+2+2=6维持；可独立采用接口而不采用完整精确recipe、PSD信息/分布或普遍加速claim。拟共同身份段后、既有像素反传/instance分支前，不覆盖已有内容。交root sole窄写/锁协调，再由本人一次nonwriter实际正文完整邻接与静态注POST；此裁定尚不计actualI/safe/DAY。

## root 实际窄写及 writer 回读

ChopGrad03-20的作者实际POST已接纳/释放同章锁后，root sole按原onePRE/static写Ch24新152、本人静态2489。实际139–175完整共同目标身份→谱日程适配→像素反传→实例修订与误差分箱顺读，并读末五行原Chop/本人注；原有效内容不改、限定diffcheck通过。末注只来源/证据范围，无动态验收身份。交resume_mar18一次实际非writer完整局部/本人注POST，未POST不计safe/DAY。
## resume_mar18 一次 nonwriter actual POST

2026-10-12 root sole按原onePRE/static落实后，本人actual完整顺读Ch24 139–175（新增152）及章末五行（本人2489/ChopGrad邻注），逐字回对原literal/static与有效必要原证。共同objective身份→谱依赖噪声与生成前条件谱→像素反传→instance修订→误差分箱/反向采样交接成立；未把clean输出可得性、期望PSD或power-law近似认证为真实分布/latent/video普效。高步/固定指标反退与全费、保原已验日程/条件/网格的回退近文，未覆盖17812或其他family。正文marker唯一、本人静态源注范围准确，限定diff-check空。实际POST有限PASS，交root接纳/释放Ch24；未授整日DAY，不修改静态身份循环。
