# Cheers12793：必要Source、具体owner与两段PRE

仅本17补03/16，完整AB/日级实体已准入并复用。resume_mar17实际读取[exact-v1](https://arxiv.org/html/2603.12793v1) §2.1–2.3/§3.1–3.5/Tables1–5/§5 limitations、A/Table6必要反侧；当前官方abs仅v1、未见给出的具体勘误/撤回说明，不冒称全网无信号。2+1+2=5，压缩semantic与later-detail消费者分流具体缺口深入；未核artifact/复现，独核/PRE未通过、未授锁未写。

## 原证与限制

VAE encode z1，generation zt=t z1+(1−t)z0；understanding t1，language-only t0。zt经VAE decode再SigLIP2-ViT语义提取，16×16 patch与VAE16downsample空间相配；pixel-unshuffle与channel projector使LLM空间tokens×1/4。LLM Qwen2.5-1.5B-Instruct：image bidirectional/text causal。7+3 DiT级联CFM：先从LLM compressed semantics低分辨生成，再PixelShuffle回h×w，把S(D(zt))的patch-embedding按由decoded semantics产生的空间scalar gate加进去，随后后3 blocks预测velocity。这里detail path是同当前noisy-zt的VAE解码/patch embedding，不是外部GT细节、独立高通滤波、最后原图复制或隐藏codebook。每ODE step再次VAE decode/ViT/LLM/CFM；减少LLM token不免这些成本。

Table1四stage30k/60k/65k/30k、batch512/512/512/128，512²、128A10016nodes/AdamW；VAE保持冻结，Stage1只projector/head/gate，后all exceptVAE，§3.5不冻结core不能覆盖表中例外。data83M vsTar403M≠20%完整训练费用，预训练资产/合成Flux2数据、样本混合/steps/vision与head总参数及tokens预算不同，不授同compute/同总参数或高分辨实时。precision/inferencehardware/CFGscale/ODEsteps/concurrency/tailSLO/完整合成和推理墙钟ND。

Table5小试验：aligned后858k understanding+850k generation；HFI两jointbranch可有限比较，generation GenEval .17→.30，但SEED70.0→69.8反退，且understanding-only70.8更高；不授双任务零冲突。GenEval和DPG非texture真值/全部质量，Fig5每run归一均值gate强度不证明所有trajectory单调增强/普遍语义稳定。Table2一些OCR/POPE/知觉指标不如其他baseline；Table3 counting .65低Tar.76，single .98低.99；Table4 Show-o2 overall85.02高83.48。single-image训练、规模/复杂细节不足和qual editing/multiimage例不能推一般zero-shot任务能力。

A/Table6文字称在4.6M samealignment引入reconstruction，第三row却558k&858k，与“matched4.6M”不一致，不采严格等data OCR必要性定理或具体公平幅度。可支持decoder→pretrained encoder接口和作者局部反退，不修补造条件。不把latentdecode表示叫原rawpixel observation或保证OCR恢复全部细节。

## actual owner与逐字PRE

实际Ch23 240–288连续表示、SemanticVocoder、UniCom空间/channel及consumer分流、新Hydra结构→channel bottleneck→确定性语义链与离散交接已读；Ch24生成head/AR-flow只交接，不重复拥有本接口。现UniCom理解走原feature/生成compressedlatent、Hydra串行共享，不含当前noisylatent decode→nativeViT语义压缩与同state patch在later-generation绕路。唯一MULTIMODAL-REPRESENTATION，拟在Hydra两段后/离散表示标题前插两段；不占Ch23锁，先独核/root协调。

共享语义主干还可以把细节读取延后，而不强迫压缩接口保存全部重建信息。一条图像分支先将当前VAE latent解码回像素，再用预训练视觉encoder形成语义tokens；空间重排与channel投影后，只将较短的语义序列交给语言主干。生成消费者再从同一当前latent的解码图读取patch embedding，在语义解码后的较细网格上按空间gate加入，绕过主干中的语义压缩段。这个旁路是当前采样状态的patch特征，不是外部真值细节、原图无损复制或独立高通滤波；理解的clean输入与生成的noisy状态也必须保留各自时间身份。<!-- source-family:SF-2026-ARXIV-2603-12793 -->

旁路改变的是消费者承担细节的责任，而非证明压缩没有损失。[Cheers的有限消融](https://arxiv.org/html/2603.12793v1)中，后段注入可以改善局部生成分数，却有理解切片小退；门控热图与生成judge均不能认证语义稳定或所有细节正确。每个生成step仍付VAE decode、视觉编码、主干与生成head成本，较少LLM空间tokens和较少训练samples不等于总算力、墙钟或高分辨SLO同比减少。重建与encoder接口失配、OCR/长尾细节回归或双任务预算不合算时，保留原语义feature、理解/生成双表示、直接latent路径与已验证专用decoder，并分别验收理解、重建及生成质量，不让共享接口给三个消费者互签保证。<!-- source-family:SF-2026-ARXIV-2603-12793 -->
