# Sep23 补充：SAGE 与 DiffusionNFT 的必要证据

以作者 A68 当前未开始确认和 root 随后明确接受为有效交接，不继承 A65 未被接受的提议。root 唯一首次准备两项必要证据，作者负责唯一非准备者实际采用；Sartre 后续复用此角色层，不第三原 Source。A15 的题摘、R16 日期及原各6分保持；当前 owner/Books 尚待作者，不预记整合或日级完成。

## 原件与实际读到哪里

两个精确 v1 请求均于 2026-10-23 UTC23:56:43～44 实际结束，200/exit0，无在途；原 raw 与相邻 `.request.json` 保存在本日目录：

- [SAGE 2509.15865v1](https://arxiv.org/html/2509.15865v1)：`ROOT_CORE_15865_20261024.raw`，122529 bytes，SHA256 `7bdda42ddca3b18bf0f5b467424130ca3a2d235a085b4589e3891d0ba9ba314e`。实际完整读 §2～4、Algorithms1～2、Table1 与 Figures2～4 captions/正文分析；未核图像素/生成样本或代码，不采未读曲线的精确点。
- [DiffusionNFT 2509.16117v1](https://arxiv.org/html/2509.16117v1)：`ROOT_CORE_16117_20261024.raw`，432614 bytes，SHA256 `a9d560096c54eb0f98854c212683214809c0bf870f9fc34a8c3c378ae53a2600`。实际读 §2～4/§6、Algorithm1、Table1、Appendix A 两个分布分解和两定理证明、C 实验设置。未读 B 的其它 solver/GRPO 推导、D 所有样本或曲线像素，不假装全附件/代码或复现。

## SAGE：共享的是受条件约束的生成前段，不是相同文字前缀的缓存

§2 先按文本 embedding 的两两 cosine 条件分组，同组只取一个初始噪声，用平均文本条件共同去噪到分叉点，再各自用原 prompt 条件继续。它改变了各输出的联合采样路径和相关性；语义相似不意味着各独立 conditional distribution 完全相同，不能从复用早期计算推出无损或 independent samples。也不同于 exact-prefix KV cache：相似度、group、平均条件、共享噪声和分叉位置都是新增选择。

为适应这条新路径，训练同样按 group 平均 image latents/text features。Eq3 的三部分分别是平均 latent 的噪声监督、平均条件预测与各成员预测均值之间的一致性、各成员后段普通 diffusion loss。平均 latent 是派生训练目标，不是所有成员的真实共同图片或语义充分统计；soft target 使用同一 theta，未给完整 stop-gradient 选择，不能把它补成冻结teacher或精确可复现蒸馏recipe。语义相近图片仍可有不同布局，平均条件会压缩差异，分叉后不保证全部恢复。

Algorithm1 的共享循环印为 T 到 T* 却写入 z_(t−1)，分叉初始化又取 z_T*；端点与状态命名没有完整统一。只能采用共享前段/条件分叉的有限接口，不能据此发布无歧义 off-by-one 执行配方。原文允许固定或适应相似度的分叉，但没有验证任意自适应规则正确。原训练/采样路径不能由调一个共享比例便自动互换。

§3 用 COCO2017 构造50k余组、每组2～5 prompts，建图枚举所有 cliques，训练 SD1.5 的 LoRA，单4090、20k steps/batch4、AdamW/lr1e−4。图构造/全部cliques不天然适合无界线上请求；若在线等组，还须计算相似、等待、group变动与隔离，论文未验实际服务调度。训练/测试图像及caption家族独立性、group重复及完整调参/CI未给，不能仅由随机生成的组认证泛化。

直接 Table1 所有采样均DDIM30steps/CFG7.5、相似度区间.6～.9。20%共享下，SAGE FID28.44接近普通FT独立采样28.38，但CLIP.316低.322，diversity.375远低.698；30%共享时FID27.71更低，diversity.359仍低独立组。40%共享下它相对普通FT同共享设定的FID29.21对30.66、CLIP.310对.294、diversity.325对.125较好，不能转为“所有质量保持到独立采样水平”。更多共享也有CLIP/diversity退步；同设置有限改善不证明该loss三部分分别必要或全部相似度有效。

所谓 cost saving12.7/19.1/25.5%明确按总 sampling steps 相对独立生成计，不是实测墙钟、GPU能耗、并发SLO或总训练回本。分组大小不均、CFG双分支、全部prompt编码/分组、微调和latent编码、成员逐一分叉/解码、缓存与独立图像质量检查仍付费；同一solver的step计数也不包括所有开销。未披完整precision/LoRA配置、匹配普通FT总预算/重复运行、端到端用时与真实请求分布，不补生产加速。保独立采样或更早分叉、原模型/普通FT的退路；有限支持为共享路径需匹配训练、语义/布局差异及相关性与净费一起验收，不采免费共享或不损多样性的结论。

## DiffusionNFT：把带奖励的 clean samples 送回前向目标

§2～3 的替代分支不对每个反向 transition 求 policy-gradient likelihood。旧采样策略每 prompt 生成 K 个 clean images、评价 reward，再从 clean image 人工加噪，用 reward 加权的正/负隐式 velocity 回归训练。`v_theta+ = (1−beta)v_old + beta v_theta`、`v_theta− = (1+beta)v_old − beta v_theta` 共用一个训练模型，不是分别独立训练两个正负网络；旧采样/目标网络与在线训练网络仍需状态和前向费用。负项是另一项非负平方回归，不等于直接对坏图做无限梯度上升。

这个接口允许 buffer 只存 clean sample/reward，不必保完整 denoising trajectory，并可换收集用 solver；不等于不需要 rollout 或 reward，也不证明任何有限 solver 都产生相同训练分布。后续 minibatch 仍做 forward noising、old/current模型求值及全反传，收集 solver的质量、步数、阶数/实际NFE、group与版本共同定义经验目标。

理论权限需收窄：正负分布分别按 r/(E r)、(1−r)/(1−E r) 重权旧分布，要求非退化的 0<E r<1 及支持/期望存在。正侧期望奖励比旧策略高的差为 Var(r)/(E r)，只有reward有方差才严格提高；r常数时正负均旧分布，不能用“constantly strictly improves”保证每轮进步。Theorem3.1/A.3 用同一前向核的真实 posterior mean 得到混合velocity与direction恒等式，依赖理想旧模型，不是已训练网络无误差的证明。

Theorem3.2/A.4 在无限数据/容量、理想旧velocity与固定回归权下推导逐状态最优 `v_old + (2/beta)Delta`，由二次目标配方可核。主文用 beta=alpha(x_t) 展示另一个 `v_old+Delta/beta` 目标恰到正策略，不能把状态依赖这个例子直接变成实际固定beta=.1/1、有限LoRA/EMA/经验reward下一定改善或全局最优。实用的均值中心化、clip/全局std变换只把分数压到[0,1]，不是独立校准的“最优概率”；不同group reward尺度/方差会影响标签，零std或自归一loss分母0需另给处理，原文未完整闭合。

EMA采样策略由参数混合得到，不等于数据分布按同权重线性混合，也不允许无界陈旧数据。adaptive loss 用 detached mean absolute residual 作分母，又让训练条件依赖当前模型误差；不能把理想固定平方损失定理自动套给全部自归一更新。“forward consistency”是作者组织目标的解释，不从有限回归/有限solver推得每个learned density都精确满足原前向Fokker–Planck族或真实reward保证。

§4/C 的直接设置为 SD3.5-Medium2.5B、512²，LoRA r32/alpha64/lr3e−4，每epoch48groups×24samples；单reward比较rollout10steps，多reward40steps，评价40步一阶ODE。C明确收集使用二阶ODE，故相同“10steps”不自动等同相同网络求值。多reward分阶段800+300+200+200+100=1600，而Table1列1.7k，保这一计数未闭，不私补缺失100轮。OCR另提高EMA上限.999或多reward.95，说明稳定性与收敛速度需按reward调整，不是一个普适超参。

Table1的多reward新模型与各个单reward FlowGRPO checkpoints、不同容量/分辨率的大模型不是隔离算法唯一因果的matched比较。它在所列若干proxy较高，但GenEval.94低FlowGRPO.95、OCR.91低OCR专用.92、CLIP.293与一行持平，不能称所有指标都超过；不同reward共享视觉/偏好模型来源，未训练该reward的指标也不等独立真实用户偏好/安全。另未在此读取生成样本像素，不以作者定性挑例签视觉普胜。

§4.3 的3～25倍是作者特定单reward墙钟轨迹报告，本次未核曲线像素/精确目标阈值、硬件与重跑，不采用为独立验证部署倍数。§4.4正文的负项移除迅速collapse、on-policy早快后不稳、过大EMA收敛慢及weight/solver/beta依赖，是本设置的直接反侧，不推全部RFT/LLM必崩。CFG-free是该经过奖励微调的模型分支，不是任意checkpoint免费关CFG且质量不变，缺匹配更多单组件消融/完整费用时不唯一归因implicit guidance。

完整费用包括所有group样本、reward模型/检测/OCR、数据与normalize/筛选、每个clean image对应多个时刻的noising/loss、old/current前向/反传、EMA同步、预训和LoRA、评估全调用与独立质量/多样性/旧能力回归。本必要域未披hardware/precision/batch组织、完整NFE/token/训练墙钟及并发SLO，不用较少buffer或免likelihood估计替代端到端预算。reward失真、负项/归一失稳或泛化反退时保旧checkpoint、经验证的sampler/固定更新节奏和独立验证；有限支持为正负反馈可经前向生成目标消费、采样与优化分离但仍耦合数据分布/费用，不采普遍稳定或实际每轮改善定理。

两篇必要支持和关键反侧足够即停止，不为补全可选实现/所有图另造外部hold，也不因限制删候选/降原6分。交作者唯一实际采用，Books比较仍待其当前具体owner层。
