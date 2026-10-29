# Sep23 补 Sep22：OpenViGA / SAMPO 必要证据首包

## 已确认的互斥范围

root提出仅两未开始必要域，作者A48明确确认让域。这里各原6分保持，只核有限机制、直接对照、训练/推理成本和关键反侧；不改日期、评分、owner、README或Books。OpenViGA已有效的root最小N→A15准入域复用，只补训练、直接数表与预算必要差额；不第三既成初筛/日期或复制原件。SAMPO由root首次取得必要精确v1正文。后交作者唯一非准备者一次actual采用，Sartre复用角色结果，不第三Source。

| 精确材料 | 原件 / 请求 | 实际原件状态 |
| --- | --- | --- |
| [OpenViGA v1](https://arxiv.org/html/2509.15479v1) | [既存raw](./SUP_ROOT_AB_NMIN_20261024_15479v1_20261012.raw) / [request](./SUP_ROOT_AB_NMIN_20261024_15479v1_20261012.request.json) | 370901B；复用既成200/exit0捕获，本次0GET/0副本 |
| [SAMPO v1](https://arxiv.org/html/2509.15536v1) | [新raw](./SUP_curl-ROOT_CORE_SAMPO_20261024_20261012.raw) / [request](./SUP_curl-ROOT_CORE_SAMPO_20261024_20261012.request.json) | 347217B；HTTP200/exit0，SHA256 `4c0665dc54eec0d10519d632733e5b955ff8f5a85eefd48f21e1a5c8d467436f`，实际请求 `2026-10-23T23:03:30.521865+00:00` |

SAMPO字节/SHA/status/exit_code已按原回执核；末尾20261012来自已有捕获工具命名，非本次请求日。唯一请求已返回exit0，无在途。结构化section/MathML读取，不核代码/运行/复现；以下未采用的样本像素/全部附录不作必要待办。

## OpenViGA：量化、预测与时间重建必须分别评价

原准入最小N的Intro、§3组件/streamlining已显示段、§4.2讨论与§5/6有效复用；本次实际完整补读§3.3各训练接口、§4.1完整数据/评价/训练设置、§4.2完整Tables2–5，B的WM训练目标/全部必要字段、C的损失说明与完整Table7。并非重新要求全Methods/所有图片；原N输出中未显示的训练部分此前未计已读，此次才补。

有限命题是：复用公开tokenizer/AR生成主干时，重建相似、分布感知和未来预测是不同消费者；语义teacher/GAN/时间decoder引入不同质量与时间支持条件。不是“开源组合本身=新架构”，也不采用控制因果或真正交互World Model保证。

原4fps/每帧256 codes加end token=257保留；原始1280×720先bilinear缩半，再center crop256×256，不保全原始驾驶视野。DINOv2 ViT-s经384维adapter对quantized表示给cosine监督，codebook/commitment另有stop-gradient，重建L1/L2/LPIPS与GAN各自改变目标。SSL非真实驾驶语义oracle；pixel好不意味着感知或预测好。

实际Table2以同配置为基准：去SSL PSNR25.75→26.31、SSIM.7630→.7794、LPIPS.1170→.1096均更好，却FID5.48→5.79、CMMD.074→.122更差；去GAN PSNR27.11/SSIM.8041更高而LPIPS.1759/FID17.97更差。不能照“每项loss都提高所有质量”选择，不能把生成/分布proxy与逐图重建混作一份真实语义分数。Table3/7把感知权重加到2时FID可继续降到3.55而PSNR24.74、CMMD.050较所选1/1的.048退步；所选超参是多目标取舍，不是普遍最优。

WM是约6.97B LWM；LoRA加linear/embedding及可训norm，仅2.39%参数更新，冻结部分bf16/可训FP32，不等前向、activation、teacher或存储全免费。teacher forcing对全部image codes算CE，线上则回用预测的indices。主文T=2/N=14与B的T=2/N=16不一致，streamlining又以16×257=4112叙述；按各原字段保留，不补成同一个已闭训练/生成长度配方。更不能从下一帧token概率推出action-conditioned物理动力学。

decoder受影响接口沿原N复用：三个相邻帧的双向时间建模改善连贯性，却需要后一个frame支持；这是额外lookahead和整组token消费，不是零延迟因果video streaming。§3.3新训练域明确先冻结TOK、三个连续真帧各自编码、VDEC联合decode，并训练3D判别器；训练后不能省去WM生成下一帧/边界处理的时间。未交完整边界/延迟实现就不补执行recipe。

直接Table4/5支持分层验收：DINOv1的FID14=14.25优于v2=14.72，而v2 CMMD14=.083/FVD14=178.97更好。只TOK+DEC转码FID14=7.19/FVD14=104.35，并非真正预测的下界保证；完整TOK+WM+DEC在top-k50为14.72/178.97。换VDEC在同k50把FVD降153.19，却FID升16.67、CMMD升.229；转码VDEC同样FVD74.29改善而FID8.85/CMMD.155较image decoder差。top-k200→1000时image decoder FID12.22→11.29改善而FVD160.48→163.80退步；选样分布与decoder共同改变，不签全部指标单调、长时正确或驾驶安全。

数据来自BDD100K，70k训练/500视频验证切片与约538k每5秒图像训练，非完整所有视野/动作/因果状态。§4.1全模型fine-tune分batch到4×H10094GB：TOK/DEC200ksteps/batch80约24h，WM28.3k/batch24约65h，VDEC100k/batch48约65h。主文单A10080GB可容的长度说明不变成整套fine-tuning单卡已跑；也不把冻结参数少/部分公共数据量小等同GAIA等同质量省费。没有matched训练预算/预训数据/完整end-to-endlatency、concurrency/SLO/重复训练CI，不从视觉展示签物理控制或服务性能。

完整费用包括公开底座/teacher、图像裁剪与编码、量化/判别器和adapter、三阶段训练、全部AR代码生成、decoder lookahead/驻留与独立重建/未来/控制评价。受限证据足以支持消费者分责及损失/decoder取舍，原2+2+2=6保持；owner具体覆盖/差额后续作者比较，未预NC/I/DAY。

## SAMPO：帧内成组预测与帧间因果是两个轴

实际完整读§3.1–3.5全部必要结构/式1–6，§4.1–4.3完整Tables1–5/必要图注文字、§5，A.1/A.2完整A–C配置/式7–8、A.3数据生成与TableD、B benchmark设置、D限制。没有看Figs4–6全部样本/曲线像素、C全定性例或核实现；不据未读曲线采用精确RL收敛倍率/全部seed表现。

有限结构：frame轴按过去frames/actions因果，当前frame按粗到细scale autoregressive；同scale tokens并行预测，不能称整个未来视频一次并行或取消AR。action线性投影加start token；训练block-causal mask、部署只查询已具备的prefix时KV复用的接口，不由“no mask needed”推广任意全矩阵无mask。scale map条件分布的写法本身也不证明任意内部依赖都已精确建模。

观测/未来不是同一token预算：观测有10个scale，未来只取较粗6/8个scale；8192 codebooks/64dim，§3.5对“share CNN backbone but parameters independently updated”的具体共享资格不完整，不自行补成同一组训练参数。Eq3未来f_t作tokenizer输入可用于训练target，不能把未知未来f_t当线上已知query；式中索引/Attention维度并非完整生成实现。A.1对未来6scale的文字与高分辨率TableA未来8scale不同，按对应配置保留，不改成统一recipe。

Motion prompt由CoTracker3 online variant在**已观察多帧**取规则grid tracks，依confidence与4帧位移过滤，overlay到观察图再加special分隔/双路输入。它是派生历史，不是未来真值或新传感器。单帧不足窗口时复制输入只能满足形状，D明确不能生成有效运动信息；没有轨迹不能靠复制恢复真实速度/方向。2%对角线门可能丢慢动作/小物体，稳定camera/背景少变化是非对称压缩假设，不推广ego-motion/场景突变。

训练未来codes的多scale CE：每scale先除其token数，λ_l=K·L_l²/ΣL_k²；相乘后每token系数为K/ΣL_k²。此代数只重新计各scale总贡献，不凭该式保证更聚焦真实dynamic区域；motion/观测权限仍另验。reward/MSE head为可选控制扩展，不自动有planner、policy或真实效果保证。

直接反侧不能略：Table1 BAIR action-free FVD65.7仍不如MAGVIT62.0；RoboNet64的LPIPS3.3不如FitVid2.4。Table4裸Hybrid207M的FVD227.4/SSIM76.4弱于AR436M的197.9/80.8，加入motion再加入temporal embedding/规模后才变好；参数/输入/目标共变，不授仅改变factorization就提高全部质量。232M与207M不同容量，也不独占motion视觉信息因果。三个规模单调指标不是经验power-law定律。

Table5单A800/batch16/BAIR：AR138M为9.05s/vid，六scale配置2.06s/vid，约4.39倍是该整个配置对照，不是同参/同训练/任意长度与并发SLO；四scale1.61s更快但FVD80.7弱于AR60.8，五scale3.27s/FVD73.1又非scale越多必更快/质量统一。六scale55.5/26.7是所测质量点，不能把最少scale的时间和六scale质量拼成同一结果。附录B所有视频PSNR/SSIM/LPIPS以每视频100候选事后取最好，FVD用所有100；不是单样本质量或部署能免费识别最好答案，生成/selector预算必须显式付。

VP2用5k/35k轨迹/三seed，Table3声称平均排除Flat Block且Simulator=100，但不是八任务原始成功率简单平均。实际用所印七个均值复算：SAMPO原始均值66.10%，分别除各Simulator均值后再平均为72.3330%；iVideoGPT相应为63.8429%/69.7309%。两种简单聚合均不能完整恢复所报72.2/70.1，故聚合/scorer口径未闭，不补造另一套精度或协议。原表差2.1只保为作者聚合报告差，不作已复算的真实成功率增益，更不是所有任务第一：Push的MaskViT82.6高于80.7，drawer/slide等也有旧方法更高。原prose“四任务最佳/其它两项第二”与八任务全表不合，不泛化宣传。MBPO/DrQ-v2合真实/合成buffer、真实ratio.5，model-rollout batch640/每200envsteps/horizon10，model另有更新频率；F5作者五seed/95%CI图是另一个受限评价，未由本次直接表格读出验证其全部curve/普遍优Dreamer。

训练A/C为8×A800/bf16、tokenizer/Transformer分别预算、pretrain/目标fine-tune多阶段；TableC如低respretrain20/24 GPUdays、高res20/11，不能只报推理forward。TableB纯Transformer B328M/L523M与主文含motion353M/548M不同，不当同一个总参数数；weightdecay重复字段.01与0/.01按对象分责，不能补统一训练配方。dataset表叙述41、列项/合成真实与采样权重/step size共同限定人口，不作“全真实所有本体”声明。

费用计tracker原预训与所有tracks/过滤、双tokenizer训练/编码、全部scale和frameforward/KV、motion附加tokens、预训练/fine-tune、100候选、planner/model-policy迭代与真实环境回归。固定视角/慢变化支持、长rollout误差累积、丢细节/追踪失准和真实动作安全须分别验；单帧/动作或压缩失配时保较完整视觉、无motion分支/原AR与可信simulator/短horizon实测。这是有限的factorization/观测与预测预算接口，原2+2+2=6保持，不签普遍因果World Model、精确recipe、净服务SLO或物理安全。owner/Books继续由作者只接新缺层，未预DAY/FINAL。
