# SCD：必要命题审阅，实际Source/PRE/POST通过

原件：[2602.10095v1](https://arxiv.org/html/2602.10095v1)。root完整AB准入/日期层通过。拟2+2+2=6；旧逐denoising step反复causal history→once-per-frame causal encoder固定context与framewise decoder→可重新选择历史摊销与质量损失，非仅architecture组合。

必要已读§4.1–4.2/5.1–5.3/Eq5–7、§6.1–6.2/Table1–3及§7直接限制。context含历史帧/控制，encoder帧内双向、帧间因果，decoder每步将fixed context与noisy current frame token-concat后只帧内attention；两者联合next-frame训练，context噪声增强是另一个训练/negative-guidance分支，不由分离自动获得。高分辨率迁移又把current高噪声帧(训练top20%)/纯高斯(推理)输入encoder，25层encoder加first5+last5 decoder共35层，需重新训练与self-rollout蒸馏，不能把低分辨率clean-history配方照搬为所有迁移。

关键证据：Table1–2低分辨率single H100 sec/frame取舍，decoder加深质量可升而时延更大；Table3 H10080GB/batch1、832×480、1.6B SCD相对1.3B SelfForcing 11.1vs8.9FPS/.29vs.45s，但VBench semantic79.60vs80.30且参数/architecture非完全等budget，包含首帧额外算力，不能称等质量/普遍1.3倍/生产goodput。precision/concurrency/SLO/训练总GPUh Not Disclosed；只采用披露采样下受限latency与quality方向。§7末10步中层相似性降至约.8、深层跨帧attention仍非零，说明分离是近似，不授context为充分统计量、原joint分布无损或真实world-state。训练/蒸馏、fixed-context维度、历史KV与首帧费用保留；质量失准时回全causal diffuser/更深decoder或保守步数。代码未运行。

owner MULTIMODAL-GENERATIVE-PARADIGMS Ch24生成与sampling，而非因果world-model：root实际原HTML必要124–264方法/迁移/表1–3/直接反侧及当前owner/Ch23/25交接确认once-per-frame与stepwise分工差额，Source/PRE通过。两自然段写于Ch24 DDPM采样推导后161/163，自身末注2275；作者151–175完整邻接顺读，root实际正文、完整151–175及自身末注POST通过，窄锁释放。单项通过不授本日DAY。
