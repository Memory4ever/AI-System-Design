# 12245 ELIT：必要Source与具体Ch24差额，待非作者PRE

当前实际结果：root必要Source/具体owner/逐字PRE独核PASS并窄写Ch24两段；作者actual非writer完整邻接/new段/本人注回源POST PASS，见SUP_POST_12245.md，已正式同步。下文保留准备时证据/PRE，不把历史“待”当当前停止项，不授DAY。

mar14_supplement；仅Mar13BJT补充自然日。One Model, Many Budgets: Elastic Latent Interfaces for Diffusion Transformers，九作者完整v1题摘/current Comments实际读，`SUP_ABS_12245.txt`；current说明只有project page，无具名撤回/重要纠错/先稿信号，未遍历全站项目历史。日级门复用root实际六DATE owning/findable/registered上界及正常公告下界夹证通过，`SUP_DATE_FOURTH.md`，不单用Submitted/Updated。精确v1 HTML GET200/449110B/2026-10-09T16:01:56.189564UTC，`SUP_NECESSARY_12245.raw/txt` 与 `SUP_FOURTH_MINIMUM_MANIFEST_RESULT.json`。

## 采用命题与必要反侧

实际读§3.1–3.4/B23–67（含Eq1–3），§4.1–4.5/§5/B68–154、Table1–4所有必要行，直接C/D B234–257。不是全部PDF、图像曲线像素、附件K/L、代码或复现。输出仍N个spatial token：短head→learned K latent Read→大部分core blocks→Write回N→短tail。group内RW将交叉注意从O(NK)降到O(NK/G)，但N head/tail、RW、codec与多步sampler仍有成本，K减少不让全部生成成本与分辨率无关。J=K/G learned位置跨group复用，resolution增加会改N/G，不是为任意尺寸认证不变执行计划。

多budget训练每iteration随机保留每group前J-tilde个latent，同值全groups/GPUs并用于RW/core；prefix早位置被训练更多，未证明每位置可验证语义重要性，也不是每region独立选预算。仅标准RF损失，采样新旋钮来自这种训练artifact，不称existing DiT无需训练即可任意丢token。CCFG的低budget无条件branch替换full CFG branch，仍两次调用并改变velocity近似，不授原full-budget CFG分布/质量一致；同条件弱branchAG退class-alignment，CCFG饱和反侧保留。

ImageNet256/512同Transformer blocks/RF/RoPE/QK、500K steps，但baseline B256与multi-budget B384通过期望FLOPs对齐，样本/有效batch不同；额外收益不是prefix ordering唯一因果。50K主图像/10K其他评价、Euler40、CFG .25为受限population。video29frames/24fps/200K、C明确single-budget，不把图像multibudget直接授视频。Qwen-Image20B仅image stream（text仍full）；60K512+60K1024 RF+distill、真实与FLUX/SDXL合成训练付费，原CFG和本文CCFG并不严格同算子。Table3 full90.45低于原91.27，低budget88.02/属性79.84也不等质量保持。Table4不同指标的group/headcoretail最优不一致，不采用唯一16groups或67%core定律。C Jmin4/Jmax64按闭区间应61而正文写60，保留该非中心count差异，不认证精确唯一budget枚举recipe。FLOPs及相关forward-time caption不等端到端SLO；hardware/precision/重复seed/CI/完整wallclock/batch-concurrency-SLO未在必要局部确认，Not Disclosed，不照录2.7×部署加速。

拟 **2+1+2=5，标准最低，因具体owner缺口深入必要局部**：固定spatial输出不必固定denoiser内部token人口，是重要可训练预算接口2；单生成组件1；把quality/算子identity与trained预算分开的稳定约束2。Perceiver/RW、prefix drop、CFG成熟原理不重复计分，不因多架构表规模扩大reach。

## actual owner差额

实际完整顺读Ch24 117–136（diffusion迭代→卷积backbone→density路径→DDPM）、1458–1504（forward复用→serving→scheduling/critical windows→adaptive patch/copy sensor），Ch23 1198–1225的latent canvas/two-stream局部有效复用，Ch25开篇交接actual读。唯一owner `MULTIMODAL-GENERATIVE-PARADIGMS`：现129 convolution说明改变每轮主干，1494/1496 adaptive patch说明改变空间patch粒度；没有固定N输出而压缩每轮内部K人口、trained prefix与weak-CFG branch identity的接口。不是Ch23 codec第二owner，也不是platform scheduler新章。两段建议放卷积分支后、density路径诊断前；不会覆盖原spatial/卷积/全DiT方案与后续采样理论。

## 逐字PRE（尚未写Books/尚未授POST）

每轮主干还可以分开输出网格与内部计算人口：保持 N 个 spatial tokens 的短 head，从它们读取到 K 个 learned latent tokens，让主要 blocks 在 latent 空间工作，再通过 Write 回原 N 个位置并完成短 tail。分组 Read/Write 限制跨域 attention 的范围和成本，但 head、tail、跨域搬运与最终 codec 仍随输出尺寸付费，不能说完整生成成本已与分辨率解耦。若希望同一 artifact 支持多个 K，可以在训练时随机保留各组 latent 的前缀；同一轮各组共享前缀长度，使运行预算成为经过训练的接口，而不是从已有 DiT 任意删 token。早位置接受更多训练只是一种重要性组织方式，不认证每个 latent 的语义，也不是 runtime 为各区域独立分配预算。

这条分支保留输出的细网格，以内部 latent 人口换取质量/计算旋钮，却需要新的 Read/Write、分组与 prefix-budget artifact identity。[受限图像实验](https://arxiv.org/html/2603.12245v1)用相近训练 FLOPs 对齐时同时改变了有效 batch，不能把收益只归因于 prefix 顺序；大模型迁移又支付蒸馏与额外训练成本，低预算仍会损失细节和条件质量。低预算也可充当 guidance 的弱分支，但它仍需第二次模型调用，并改变原 full-budget CFG 的 velocity 近似，不保证相同采样行为；原文视频实验未验证同样的 multi-budget 合同。预算或分组未经训练、条件失配、细节退步或端到端费用不值得时，应回到完整 latent 人口、原全空间主干与已验证 guidance，而不是用较低 FLOPs 代替质量或在线 SLO 验收。<!-- source-family:SF-2026-ARXIV-2603-12245 -->
