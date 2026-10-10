# VideoWorld2：必要命题审阅，待实际Source

原件 https://arxiv.org/html/2602.10102v1 ，root完整AB准入、日期包络已实际通过。拟2+2+2=6：重构code承载外观混杂→pretrained VDM承载外观、multi-frame latent/code与stop-gradient coarse-motion guidance分责→重新判断video-only latent预训练的可转移性，而非生成画面即因果world-state。

作者必要已读§3.1–3.2、§4.1–4.2、§5.1–5.5/Tables1–3、§8/Table4与评价器说明。dLDM先warm-up原重构，再用projection/causal cross-attention把code送VDM；旧decoder输出走stop-grad的ControlNet-like motion条件，joint trainable VDM不等frozen prior。AR预测离散future-code；CALVIN执行动作仍需真实action标签和新增MLP head，非纯无标注video zero-shot控制。causal mask仅表示时间可见性，不识别真实动作因果。

Table3(a) VDM/stop-grad/control的受限组合对照支持所测职责，但非完备factorial不授外观完全剥离或唯一因果解释；随机VDM崩溃、冻结31.7低于full68.8是额外预训练/适配反侧。N4→8 paper68.8→65，codebook1000→4096/64000 paper68.8→50.4/29.4，T93→177 CALVIN1.87→1.79，更多容量/历史不是单调收益。§5.4 22k CALVIN latent pretrain+2k action labels的1.87低于22k action oracle2.36；OpenX1.3M+22k action的2.88不是无action标签。Video-CraftBench7h/~9.5kclip与~150test，DINOv2 evaluator使用train/test与各方法generated的手审标注帧，任务判据与LPIPS/SSIM视觉分别测，不能当独立真实手工执行。没有跨物体/现实机器人安全保证。

配置Cosmos AR4B+DiT2B、93frame480px/16fps、默认N4/codebook1000；dLDM1e5iter B128、AR5e4 B256，其预训练和联合adapt均计费；hardware/precision/inferencewallclock/concurrency/SLO/总训练GPUh Not Disclosed，不采用通用效率倍率。拟owner需在Source后核当前Ch25/26实际知识链，可能已有覆盖；没有owner授权或Books写入。代码未运行/实验未复现。
