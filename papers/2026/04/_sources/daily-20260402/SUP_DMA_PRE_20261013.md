# DMA 窄 PRE（未写 Books）

Owner `MULTIMODAL-GENERATIVE-PARADIGMS`，`books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md`。reader实际S4–6 Source5；作者实际S4–6方法/评价/直接限制，[原件](SUP_RESUME_CORE_2603-29239v1_20261013.json)。root已窄核current v1 Submitted03-31/2603公告月复合门归04-01BJT；CVPR接受/June发表本身不是早公开证。当前Ch24 actual316–344中externalreference MMD、prototype negative bank与首t多seedstate融合尚未承载逐t h-consensus生成prototype，只申请外部MMD后一个新段+本人注；不重写相邻论点。

## 完整拟局部

~~~~markdown
reference 还可以是一组目标样本，而非单个条件或轨迹历史。只希望提高某类输出概率时，分类器/CFG guidance 仍是直接分支；需要拟合有限参考人口的模式与比例时，可以在 reverse sampling 中加入 empirical MMD 梯度：生成 batch 内的排斥项维持分散，reference attraction 项推动分布匹配，prompt×latent product kernel 再让相关文本条件加权参考样本。这里 reference 编码、kernel/带宽、batch 和 guidance schedule 都成为 sampler state，batch 内 coupling 也不等于独立单样本条件更新。[受限方法与图像对照](https://arxiv.org/html/2601.08379v1)支持这条替代接口，但 iid reference 与有界平滑条件下的 cross-term 集中界只约束梯度估计，不证明有限求解器或 decoder 输出已服从目标 law。参考稀疏、kernel 失配与高维估计仍可能退步；reference 编码/驻留和成对 kernel work 增加费用，training-free 不等于免费。质量、覆盖或净预算不可信时，应增加已验收参考、重校准，或回退原 guidance/专用适配，不让 distribution matching 名称接管最终语义验收。<!-- source-family:SF-2026-ARXIV-2601-08379 -->

如果目标不是匹配整个分布，而是生成同一条件下的一个概念原型，还可让多个种子的去噪轨迹收敛：每个时间步先平均所选内部层的表示，再分别优化当前noisy latent靠近该均值，随后由原DDIM推进；达到cutoff后只做普通去噪，最终才用VAE解码。[DMA的受限方法](https://arxiv.org/html/2603.29239v1)避免把不可直接解码的feature均值当图像，却也会压掉少数mode，原型稳定并不等于恢复真实概念分布或模型bias真值。外部encoder聚类后再回到各latent分组，需要另校准conditioning；TI/LoRA与不同CFG/训练预算的比较不独占mode恢复因果，也不证明clusters给定后无偏。内部层、时间网格、seed人口、cutoff和condition都应冻结，大量latent优化、完整采样、聚类及适配均计费，same-seed pool不等总预算。模式覆盖、层语义或代理representativeness不可靠时，保留普通样本分布、逐簇检查与独立人工锚点，不用一个清晰的平均原型替代多样性或公平性验收。<!-- source-family:SF-2026-ARXIV-2603-29239 -->

增加 guidance 条件也不等于约束更强。单一明确类别时，固定安全 reference 便宜且可解释；多个有害类别的 noise 差分方向在同一 latent 和 timestep 上可能对立，简单组合会稀释本应压低的类别。一条受限分支每步分别求各 keyword 条件的 guidance，与当前 prompt 的差分比较 cosine，只把最相符的一类交给原安全 steering；它改变 reference 选择而不重新训练 denoiser。文本投影另有选择接口：比较各有害子空间的 projection residual，再只采用所选子空间，不能与 latent 时间动态选择当作同一实现。
~~~~

## 当前尾部后仅追加本人注

~~~~markdown
- `SF-2026-ARXIV-2603-29239` — Daily2026-04-02补04-01；[DMA exact-v1](https://arxiv.org/html/2603.29239v1)必要§4–6，2+1+2=5；逐t内部h均值/各noisylatent优化→DDIM→cutoff普通采样与prototype分责。保RV5.1/K1000/N300/20steps/cutoff10/CFG7/RTX4080约10h、12concept代理/少数mode抑制、CLIP聚类和TI/LoRA混配/无偏未证；same-seed不等全预算、不授概念bias真值或通用h层。未核artifact/像素或复现。
~~~~

root逐字PRE/当前邻接通过前不写，窄锁只限新段/本人注；写后nonwriter实际POST另做。
