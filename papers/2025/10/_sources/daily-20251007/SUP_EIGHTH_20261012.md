# 2025-10-07 04069单项机制与临床反侧重开

作者Ptolemy。只从既有218身份的30标题止中重开04069，未新增查询/分类/日期范围；其余29不扩。实际精确[2510.04069v1](https://arxiv.org/abs/2510.04069v1)完整题名、摘要和可见history：Diffusion Low Rank Hybrid Reconstruction for Sparse View Medical Imaging；仅v1 Oct05提交记录可见，提交不是first-public，未将不存在的comments内容补造。abs/core均HTTP200/exit0完整保存，见[supplement](supplement-20261012/)及各request。

## 1. 最终贡献判定：C

完整AB实际声明NCSN++/SDE先验、anisotropic TV、nuclear norm、ADMM、2D slice、FFT与tensor-parallel，不能仅以medical标题关闭。本人实际读HTML **II完整method/Alg1、III-1至III-8完整实验各段及TablesII–V、IV结论**，未称全文/附录/图像渲染；决定依据如下。

- 原文披露的生成模型是既有NCSN++/VE-SDE及U-Net，ADMM拆分image/gradient/patch矩阵变量，以soft-threshold和SVT更新。这里LoRA指patch核范数低秩正则，不是模型参数PEFT LoRA。具体增量仍为该CT反问题的现成先验与正则组合，未披露可识别的新模型学习/表示机制或改变当前主线选择的一般条件。
- FFT-PCG加速既有线性子问题，Alg1为PCG求解、denoised图像作初值；所读方法/实现没有新增tensor layout、分片/通信或模型计算接口的算法。III-8标准CG替换对照23→103ms只per-iteration，质量指标近似不变；这是所列应用加速观察，不是新并行机制、2000步端到端延迟或服务SLO。不是因为组件成熟就一律排除，而是本稿没有建立超出领域重建指标的机制/成立条件增量。
- 强理论/临床争议不能反过来替代贡献判断。以下只隔离采用：Eq2含diffusion prior而Eq3没有；Alg1通过PCG初值使用denoiser，不能由普通凸ADMM结论直接授该整链单调下降/O(1/k)。P(x)为patch展开而x-step的adjoint/形状对应未说明，未替作者修公式或读完整证明。

## 2. 实际临床与评价反侧

III-1/4所述三公开数据集被处理为256×256 slices，由Radon生成2/4/8均匀稀疏投影并可加Gaussian噪声，不等真实稀疏低剂量设备或前瞻临床。III-2只PSNR/SSIM；所读实验没有病灶检出、reader study或临床结局验证，不能从三数据集/纹理保留推出diagnostically reliable/broad clinical applicability。2D slice策略及真实数据来源不授3D诊断安全。

TableV轴向SSIM：8views TV-LoRA .853低于TVzz .880和Chung .874；4views .832低于.849/.858；2views .794低于.798/.801。不是所有方向/度量均胜出，也不能把PSNR提高与SSIM选择混为统一临床收益。III-7已承认8views轴向弱项，其他宣传仍不采用。未渲染Fig1/2，不声称视觉病灶保持已独核。

**C依据具体成熟组合与领域指标未建立新主线机制/一般条件**，不是medical关键词、缺实验、上述公式争议或审阅成本。必要强安全/理论反侧已实际处理；未核公开日不影响此C，不再索其first-public，不评分、不进入Books。出现具体新增学习/并行接口或能改变主线选择的可核条件，才定点重开，不扩其余题名。

root实际§12已读完整v1题摘/history及II/Alg1、III-3/5/7/8、IV并裁C通过；读层与本人完整III分开，未回填为root全III或全论文。原128有效准入不重读。更新129当前AB=100P28C1O，60复用=52P7C1O，189题摘身份层=152P35C2O，另29作者标题止，仍218。root另读04478 Atom完整AB只是独核范围样本，不冒作者extra exact-v1。
