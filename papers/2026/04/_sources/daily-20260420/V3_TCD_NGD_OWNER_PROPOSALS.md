# Apr20 两项最小 source→owner 采用提案

作者：apr20_resume。这是具名有限采用提案，不是独立验收；需非作者核必要原文与当前owner后再授窄写锁。其余日报工作继续。日期联合依据见V3_DATE_RECONCILIATION.md，不借其他日报日期PASS。

## 15383 Temporal Contrastive Decoding

[exact-v1](https://arxiv.org/html/2604.15383v1)。2+1+3=6；真实Ch23内部反事实段没有音频时间尺度与encoder/decoder可见性条件，缺口深入override，不抬分。

必要源：§3.2–3.4慢路径/稳定性/gate与candidate union；§4.2–4.6 Tables1–6受限结果/组件与架构反例；AppendixA方法参数与必要AppendixB/Table7完整流水线成本。作者已实际读这些位置。§3.2 waveform blur重编码与§3.3 Eq1 state blur表述不宣称严格等价；不写具体encoder-state实现。Qwen2.5-Omni Speech70.6→69.7、非unified SALMONN53→52.8/Flamingo74.8→74.7/DeSTA61.2→60.9/MiMo74.7→74.7保留。单A80080GB/eager attention、3秒音频/100tokens、原stream KV优化复用假定：prefill2.04×、decode.99×、peak1.01×，不能推普遍零成本/实时保证。

实际owner：`MULTIMODAL-REPRESENTATION`，books/part-03-multimodal-world-models/23-multimodal-representation.md，当前“shared early prefix…late counterfactual branch”段（约811–819）之后、“感知到了，不等于行动会使用该模态”之前。当前视觉branch与末尾不确定性gate有原则覆盖但没有时间慢参考保留粗audio语义以及受架构可见性限制的新条件。Ch22长输入与Ch24生成提交交接已读；不把全模态generation归属迁来。

拟正文两段：

> 音频反事实还要选择保留什么时间结构。完全移除音频适合检验有无模态影响，却会同时删除粗语义与瞬态线索；另一条受限分支把短时间变化平滑后重新编码成慢参考，让原始与慢路径在同一文本历史下预测下一个token，再只在音频依赖较高且预测不确定的位置对小候选集合施加logit差更新。这是时间尺度对照，不把差值当声学真值，也不证明语言prior已经被消除；输出仍须通过任务grounding评价。
>
> 对照是否有用取决于decoder能否利用该时间差。受测统一audio/text decoder改善不意味着独立编码/拼接架构同样改善，最强模型的speech子集也有退步；因此不能无条件打开干预。两路编码、稳定性估计与独立KV状态增加prefill和内存成本：单A800、短音频/100token、关闭FlashAttention的对照中，memory-bound batch2 decode隐藏了部分增量，但prefill约加倍，不是全服务零成本。时间扰动损伤语义、模型接口不可见或质量/成本不合算时，应保留原始decode与外部证据对照；第49/56章另验实际执行与SLO。

## 15554 Natural gradient descent with momentum

[exact-v1](https://arxiv.org/html/2604.15554v1)。2+1+2=5；当前Ch28有局部Jacobians残差坐标，无历史函数momentum在变化tangent中的责任，真实缺口深入override。

必要源：§3.3–3.4 NGD Gram/regularization与函数空间解释；§4.2.1 Eq24–28当前Gram+cross-Gram、§4.2.2 QNHB近似条件、§4.2.3 NHB-FD、§4.3 Nesterov位置；§5–6必要回归/分类对照、成本和limitations。无需全理论附件或PDE科学应用。作者实读；projection不冒称精确parallel transport或参数化不变的global保证。MackeyGlass10sigmoid500train/500test、50realizations；XOR1800/900小型实证。FD/QNHB可慢于exact、Nesterov-FD发散需减β、line-search少迭代但更长时间；small stochastic batch/vector-valued等仍future work。不采用LLM/HPC普遍加速。

实际owner：`TRAIN-PRETRAINING`，books/part-04-training-system/28-pretraining.md，“聚合梯度与逐样本残差是不同的更新坐标”两段（约434–440）后、“Preconditioner与Gradient共享Batch时会改变估计语义”之前。当前局部pseudoinverse/SVD更新仅处理当前步的残差条件；新增历史函数变化的坐标变换。相邻Ch27经验分布与Ch29条件行为训练交接已读，不动分布式或PDE owner。

拟正文两段：

> 这种局部坐标还会随参数更新而变化，所以加入动量时必须说明保留的是参数位移还是函数变化。普通parameter momentum直接沿用旧参数方向，在局部几何变化缓慢时简单合理；函数空间分支先用旧tangent表示上一步函数momentum，再以当前与旧tangent的cross-Gram将其投影到当前tangent，用当前Gram的逆/伪逆求回参数坐标，最后合并当前自然梯度更新。这是对历史方向的重新表示，不是直接给参数动量换名称，也不是精确无误差的全局几何保证。
>
> 显式cross-Gram增加旧导数状态、矩阵估计与谱求解成本；有限差分可以用额外forward近似旧函数方向、避免保存完整旧Jacobian，而直接复用参数动量仅在两步tangent映射近似恒等时合理。小型回归/分类对照中的迭代减少不等wall-clock同比改善，近似版本有更慢和发散反例；截断/regularization、步长与动量系数都影响稳定。若估计噪声、显存或额外计算抵消收益，应回退无动量NGD或稳定的AdamW/SGD；现有证据不证明大模型随机minibatch训练加速。

两项均删除论文名仍形成问题→机制→代价/反例→回退链；只有采用通过后实际写正文与Review notes，然后交非作者真实写后核。
