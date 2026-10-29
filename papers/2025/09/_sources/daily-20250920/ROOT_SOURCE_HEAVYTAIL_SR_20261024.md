# 双层重尾优化与超分数据蒸馏：两项首次有限必要审阅

仅Daily2025-09-20补Sep19BJT。作者174明确确认两必要首域未开始、无CORE/Methods/在途，root本轮明确接受后首次准备；原14952六分、14777五分及已成AB/日门复用，不重新决定日期或评分。writer下一唯一另一角色回下述原域实际采用，reader后仅角色复用；不预Books或DAY。

## 原件与审阅范围

| 材料 | 原件及请求 | 实际结果 |
| --- | --- | --- |
| [Stochastic Bilevel Optimization with Heavy-Tailed Noise exact-v1](https://arxiv.org/html/2509.14952v1) | `ROOT_CORE_14952_20261024.raw/.request.json` | GET 2026-10-24T04:54:21.152146+00:00，200/exit0，1190707 bytes，SHA256 `70069c3f0a9cd0661490510e326029fc95f82f146ff8baebf2e39fc344711f27` |
| [Dataset Distillation for Super-Resolution without Class Labels and Pre-trained Models exact-v1](https://arxiv.org/html/2509.14777v1) | `ROOT_CORE_14777_20261024.raw/.request.json` | GET 2026-10-24T04:54:43.965535+00:00，200/exit0，128954 bytes，SHA256 `a6a6e77e0ae1f1327eebe29e130c99d00dd90c0adb3dc87718f60d7421eb79b1` |

14952实际读§1 Eq1–6/直接T1–2、§3完整假设/定义/代理界、§4/5两算法与四个主定理陈述、§6所有三个直接实验及F1–3文字caption、§7。未审全部附录证明、图像素、代码或复现，不认证全部定理常数/最优证明。14777实际读II-A/B/C所有方法/式1–6、III-A–E全部设置/直接T1–3及F3文字caption、IV限制；不看生成图像素或代码，不声称SR训练复现。请求均已收尾。

## 14952：把内层误差和外层重尾方向分开处理

双层问题不是将两个loss普通相加：外层评价f(x,y*(x))，内层先对固定x求g的最小值。精确hypergradient含交叉Hessian和逆Hessian；所借前人penalty reformulation用f+lambda(g−g*)及两个内层解，把显式二阶需求换成内层逼近误差与penalty偏差。这个代理本身不是本文首创；新增是在p阶中心矩有界、方差可无界条件下组织clipping/normalization及其分析。

Alg1内层分别clipped-SGD追踪z的g最优和y的penalized最优，并warm-start下一外步；外层以M样本估计f_x+lambda(g_x(y)−g_x(z))，同一zeta用于两g项，然后把该不精确方向归一化更新x。内层 clipping限制异常幅度，外层 normalization限制每步长度，但不恢复无偏hypergradient、正确方向或全局最优；方向质量仍取决于两内层误差/批量与penalty。Alg2对非凸—强凹minimax直接内层clipped ascent/外层normalized descent，不再承担一般双层的penalty代理，不能把两种复杂度或收敛对象混写。

§3假设必须近文保留：双层g在y全局强凸、梯度及Hessian Lipschitz，f在y Lipschitz/二次可微、外目标下有界；minimax在y强凹/平滑。oracle对原f/g无偏且有统一p∈(1,2]中心矩界；p=2回到有界方差，p<2允许无界方差但不是所有重尾/有偏/相关噪声自动合格。未知LLM训练并不因梯度偶有尖峰满足这些前提；普通深网内层不据此强凸。

Th4.1/5.1陈述的是随机输出点的期望梯度范数，不是全局解/任务泛化；epsilon-stationary仍可鞍点或差局部点。双层SFO主阶epsilon^{−(4p−2)/(p−1)}在p=2为epsilon^-6，minimax主项为epsilon^{−(3p−2)/(p−1)}在p=2为epsilon^-4，且5.1还有kappa²/epsilon²项；p趋近1复杂度恶化。它是oracle调用阶，隐藏常数/条件数/所有内层K、外层M及T共同付费，不是GPU秒。minimax通过可分离目标给sigma/epsilon下界对应，不授kappa或所有双层维度完整最优；§7明确双层重尾lower bound仍未来工作。

**不照录完整理论调参recipe。** 4.2步长写B_K但后定义B_y,t/B_z,t，lambda又用未在该处闭合的R；R0范数/平方及R_y/R_y²、clipping指数也与4.1不同。最重要的是Th4.2印出的结论为向量梯度的时间平均，没有norm，不能由可能相消的向量平均推出平均梯度范数小或随机输出高概率stationarity；5.2则明确平均范数。两者保原区别，不私补缺符号或宣称附录整体错误。Alg1/2归一化也未给g_x=0分支，符号表/常数/完整实现仍不作为本次可执行配方。有限采用可止于分层处理机制与上述条件，精确高概率双层结论须作者澄清/相关证明再定点重开，不要求先遍所有证明才保机制。

§6.1人为加居中Pareto噪声alpha=1.2/1.5/1.8，20次独立run、按SFO calls匹配；p矩应取p<alpha，不将alpha直接当有界的p阶矩。F1 caption明确alpha1.5/1.8与Clipped-SGDmax近乎重叠，不支持处处严格胜者。Eq12声明y为标量、随后K却构造成d×d，维数文字未闭，不补生成代码。§6.2为TF-IDF101631维逻辑回归/learnable正则，不是LLM全参训练；内外步数及lambda/lr搜索已另付费，HVP比一阶oracle的单次成本不能省略。§6.3 GPT2-124M/Alpaca52K、8:2切分、训练target替空字符串的corruption，batch64/lambda1000；这是有界实例，不证明真实梯度满足p-BCM或内层强凸，也不识别只靠重尾鲁棒造成的全部收益。未披硬件/dtype/总墙钟/显存/SLO与大规模多seed统计不补造，图caption不代曲线数值重算。

保全部oracle、两内层状态、批量外梯度、选参/重复run、超参训练与独立质量回归费用。前提或内层误差不可信时保普通clipping/基线、较简单固定超参和独立留出评价；不能从本理论签发PPO/GRPO稳定、任意LLM调参收敛或净加速。后续只比较实际训练目标/双层更新owner，不由应用名单建立普适保证。

## 14777：无人工类标签不等无预训练先验，少训练样本不等完整质量保持

流程先以HR patch与bicubic↓4再↑4的PSNR筛低于阈值的patch，再用预训练CLIP ViT-B/32特征k-means作pseudo classes；适配预训练DiT/DiffFit，以真实latent memory的最小相似度与合成memory的最大相似度分别提出代表性/多样性目标，再添高频项。最终HR样本直接从适配生成器采样，LR由bicubic↓4产生，交不同SR架构重新训练。这样不依赖预训练**SR模型**或人工class labels，但仍依赖CLIP、diffusion/codec历史先验；标题不扩成无任何预训练模型。阈值23dB取原patch分布median，k=7还借OST七类先验，不能叫完全无类知识。

低bicubic重构PSNR只是被该退化抹去细节的代理，不是普遍任务信息量；CLIP簇不是真实类别/恢复等价类。采样HR→bicubic LR限定退化人口，不自动覆盖真实相机噪声/未知blur，也不认证被还原细节曾真实存在。三阶段将生成器制备与最终SR学习解耦，可供多架构消费，但不证明有限合成池保持全部原分布/旧模型函数。

II-B式3–5将argmax/argmin（参数解）写成相加的标量loss，正负/执行目标未闭；z_t−epsilon_theta的简式也未显式给噪声日程系数，不可直接当精确clean latent。最大化与bicubic版本的差能奖励伪纹理，非真实高频恢复证明。memory采样、更新/stop-gradient、cosine零范数与最终采样配额实现不补造；不照录完整可执行loss配方、不据印式断言代码实际错误。

直接T1：RealESRGAN在420合成图SSIM .6451高GSDD .6273，但LPIPS .4482劣.3512；更大合成集并不每项单调，RealSR从140到280 SSIM .6335→.6302。T3 threshold crop的SSIM在420 .6139低random .6164，LPIPS三个规模全劣random（如.4644>.4562），反驳“阈值筛选各项始终更好”；完整distillation虽SSIM三档更高，280/420 LPIPS .4495/.4482仍劣random .4449/.4445。只看平均/一指标不能唯一归因高频项、聚类或diffusion，因为没有逐一关闭各组件且匹配完整预算的控制。

T2全部四架构的各有限池均仍低FULL对应PSNR/SSIM；SRFormer70图26.73 vs FULL27.05为.32dB局部差，且SSIM .7157<.7297，不是99.32%数据删除无损。HiTSR420为26.82/ .7212，仍低FULL27.71/.7548；架构可用不等所有容量/任务保持。F3视觉只是示意，未看像素不认证分布或纹理真实性。原文未给seed/CI，声称threshold、k、loss权重稳健没有相应独立sweep表，不补成已验通用区间。

设置OST10324/300test，512²、DiT适配70epochs/b8/Adam1e-3，单RTX3090约4h适配+1h SR vs11h FULL是作者该配置claim，缺合成池大小对应、原checkpoint预训/CLIP编码/筛选聚类/采样及全部架构的端到端总费和matched-quality说明，不当同质完整效率证明。全部原数据处理、pretrained资产、memory驻留、生成器训练与采样、每个SR模型重训/评估及参数选择都计费；model-independent consumer不等随时不重训换架构。质量、退化域或总预算不合时保原始HR/LR、简单随机/阈值选择与原分布训练，另验perceptual/像素质量和真实消费者；有限机制可留报告并由writer比较现有唯一owner，不强行增加Books或降候选分数。
