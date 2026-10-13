# AccelAes 2603.12575v1：必要原证与 owner 差额

root 本日限定读取 https://arxiv.org/html/2603.12575v1 的 §3.1–3.4、§4.1–4.3/Table1–4、§5、A.1–A.4，及直接反侧 C.5/D；不遍历其他附件，不核代码或声称复现。日期准入复用本日有效结果。2+1+2=5，具体 attention mask 同时控制空间计算与 guidance 的架构边界，标准以上定点深入。尚未获得非准备者 PRE，不授写入或 DAY。

## 实际机制及证明范围

34 个固定美学词 anchor 经 CLIP-L14 相似度 threshold 0.60 选 prompt token；warmup 聚合 cross-attention 后 percentile 形成单次区域 mask。它是语义相关 proxy，不是客观重要性或人类偏好真值。Lumina 分支仅选区 Q 工作、仍从完整当前 hidden 计算全局 K/V；区内 FFN 更新而背景使用最新全算锚点缓存，并 scatter 回完整形状。同 mask 再分配 region-wise CFG。另有全局输出 prediction 的 StepCache extrapolation，须与空间分支分别说明。

关键反侧：A.3/C.5 中 SD3-Medium 因 joint image-text 处理、matched-latency 稳定性退步，关闭 spatial CFG；FLUX.1-dev 主要使用 StepCache，不支持相同 SkipSparse。Table4 的 cache-only 速度和主配置 SD3/FLUX 相同；不能把三 backbone headline 当三次完整空间机制验证。Lumina 局部消融仍不能证明各指标单调优势：Table1 TaylorSeer Edge 高于 full；cache-only ImageReward 也低于 dense。Table1/2 的 full 美学分数不一致，隔离该数，不从其推导保证。

评价合同：Pick-a-Pic 10,000 prompts × 3 固定 seeds，同模型相同 prompts/seeds；Lumina 30 steps、SD3/FLUX 28 steps、1024²；single RTX5090，batch1，Lumina/FLUX BF16、SD3 FP16。作者 end-to-end 含 VAE 和 CFG passes，单次 CLIP 声称 <0.05s 仍是成本。Concurrency/SLO 未披露；代理审美分数非人工偏好与提示语义真值。warmup/mask/gather/guidance/state/cache 费用及选择失配须共同验收，不授通用生产吞吐或无损。

## 唯一 owner 与逐字 PRE

已实际顺读 Ch24 1395–1502：近似 output cache、trajectory-conditioned mutable set、block-specific warmup refresh 均有，但没有把语义区域同时作为计算人口与 guidance 控制条件的架构依赖分支。放在固定/动态 mask 分支完整两段后、跨请求 semantic donor 前，与已有 block-specific refresh 后文构成不同替代分支。唯一 `MULTIMODAL-GENERATIVE-PARADIGMS`，不复制入 Ch23/49。

> 固定区域选择也可以读取 prompt 的特定语义，而非只看整幅 sample 的变化。一条受限图像分支先用词义 anchor 选出条件 token，再从 warmup cross-attention 构造区域 mask；选区只重算 query 与 FFN，attention 仍读取完整当前状态的 K/V，背景 FFN 复用最近全算锚点。相同 mask 还可以分配区域 guidance 强度：计算人口与条件放大共享选择，却不具有相同权限，注意力相关既不证明背景无需更新，也不证明所选区域就是人类偏好的真值。单次 mask 简单且形状稳定，代价是区域移动、条件失配和 gather/cache 成本；最大复用期与完整重算仍须保留。

> 这类空间策略不能和整步 prediction cache 混成一种可迁移加速。受限实现中，joint image–text 架构关闭区域 guidance，另一个 backbone 主要只采用整步缓存；它们的速度不能反证空间选择普遍有效。需要分别验收区域选择、guidance 和时间复用，以及完整生成的语义、细节、费用与质量反侧，不能由审美 proxy 提升授无损。定位失准、空间放大不稳定或稀疏费用不划算时，保留统一 guidance、只做已校准的时间复用，最终回完整 denoiser；旧方案并未被一张语义 mask 取代。<!-- source-family:SF-2026-ARXIV-2603-12575 -->

末注保存以上 exact-v1/受限架构、测量协议、数字冲突和未核代码边界；实际 POST 身份只能真实发生后填写。
