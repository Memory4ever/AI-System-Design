# 2604.26694v1 X-WAM：Ch26 异步动作提交的训练支持写前包

本包供非作者做 source→actual-owner 采用核；不代表已获共享写锁、实际整合或 04/30 日级通过。来源按本批官方公告槽、连续编号与邻界作 04/30 08:00～09:00 北京有据推断，而不是把 Submitted/Updated 单字段当首次公开日志。[官方 exact-v1](https://arxiv.org/html/2604.26694v1) 的中心是 action 先于完整 future video 完成，并在训练期覆盖这条推理路径。

## 相对现章的具体差额

Ch26「World-action model」约 225–262 行已经明确 explicit video rollout 会进入 action critical path，latent prefill/direct policy、环境 observation 与低层 controller 各有权责；「Future-to-Action」又要求诊断 action 是否真正用 future latent。**缺的是**联合扩散模型让 action 在较浅去噪步结束后先提交、而 video 在已清洁 action 条件下继续生成时，训练样本须覆盖 `(video 仍噪, action 已清洁)` 的组合状态。仅把两模态各自独立采 timestep，会花训练量在推理永不到达的 `(video 更清洁, action 更噪)`，却不保证清洁 action 条件下的视频续写质量。这是 train–serve state-support 与 action critical-path 的交叉责任，不是泛称“多模态用不同步数”。唯一 owner 建议 Ch26 上述三路线之后、Future-to-Action 诊断之前；Ch24 不重复写视频扩散一般采样。

拟最窄正文（须非作者核后方可落笔）：

> 若 action 与未来 video 在同一扩散网络里联合去噪，低延迟不一定要删去可视未来：可以在较少的 `T_a` 步先形成 action proposal，交给低层 controller 依据当前 observation 和 safety envelope 决定是否执行；video 分支再完成剩余 `T_O−T_a` 步，供诊断或需要视觉未来的消费者使用。但训练不能只对两种模态各自独立抽噪声时刻。后半程的计算会看到**已经清洁的 action 与仍在去噪的视频**，所以训练分布需要显式覆盖这一条件；一种受限实现将 `t_action=0` 的 action-conditioned video 分支，与 `t_video≥t_action` 的联合分支混合。这个支持约束不等于训练连续分布与部署离散 schedule 逐点相同，也不让模型生成的 future 获得环境真值或动作执行权。
>
> 这把等待完整视频的同步方案换成更早的 action admission，同时支付多目标训练、继续生成视频、深度分支和状态一致性成本。若任务要先审可视未来、action 对尚未完成的视频质量敏感，或紧 deadline 下专用 direct VLA 更快，显式 rollout、同步联合模型和纯 policy 仍可共存。调步数时必须同时看 action latency、闭环 outcome 和后续 video/depth 质量；只看 action 步数或预测图像分数会漏掉条件分布失配。

## 必要原文与反向证据

- §3.3/Algorithm 2：`T_a<T_O`；前 `T_a` 共同去噪，随后冻结 action/state (`t_a=0`) 仅更新 video；训练 Eq(4) 混合 `t_a=0,t_O~U` 和 `t_O=t_a+(1-t_a)Beta(1.5,1)`。后者确保 `t_O≥t_a`，但**不是**证明连续训练律与有限步部署路径完全相同。
- §4.3/Table 4(b) 的相同 benchmark 微调消融**没有**整份论文的 5,800 小时预训练阶段。Decoupled-train+Async-infer 与 ANS-train+Async-infer 的 action latency 同为 1033 ms，success `67.2→67.8`，PSNR `22.60→23.46`、AbsRel `.0430→.0349`；这支持 clean-action/video-continuation 训练责任的局部效果，不是总体 full-model 79.2% 由 ANS 单因子造成。
- Table 4(a) 的 sequence-concat depth 在 PSNR/AbsRel/点云指标部分胜过 interleaved branch，却使 action latency `1888` 对 `1033` ms；不能写成所有质量维度无损。§4.3 同步联合路径 `4665` ms 是此 Wan2.2-5B/特定硬件和步数条件，不是跨 VLA 的通用实时界。固定 observation 窗、六次 earphone-packing 真机和更快专用 VLA 的成本反例应保留。
- 对照现 Ch26，较低层 controller/environment 仍分别控制物理执行与 transition 事实；论文的 action “dispatch” 不是独立安全证明。非作者需最终判断新增训练支持约束是否足以成为该章的一段长期机制；若现文已明确同一 `(clean action, noisy video)` train–serve 分支，则降 Existing/Only，不因 literal 已备自动写入。
