# 尾六最小逐字稿

Source/date复用READER2_REVIEW；本文件不代替literal PRE或实际POST。

## 04510 / Ch24

锚点：CacheScope完整段后、提示感知cache分支前。

逐字正文：

Cache 的终态均方误差、落入哪个 mode 与层内 feature drift 还是三种不同目标。[一个受限几何分析](https://arxiv.org/html/2610.04510v1)将 constraint-map 的切向／法向分量分开，在等权双 Gaussian、精确 Tweedie estimator 与指定归一化协方差下讨论冻结估计的 MMSE 和 nearest-mode flip；half-SNR 只是该模型下的简界，flip 连续变化，所谓 safe 一侧仍可能出错，不是任意 diffusion cache rollout 的安全阈值。深度 stride 的 upper-envelope 排序另需 unit-gain、随深度排序的 β 与 κ 小于临界值等条件；实际 drift 更小还需 transversality，不能从 noise schedule 自动推出。部署仅按 timestep／block 复用，并未测量当前 constraint geometry 或 κ，也没有在线认证约束。核验假设所需的 geometry／score 诊断、stride 选参与缓存驻留、刷新和质量回归均须另计成本；假设或输出质量未核时保留密集刷新及 full computation，不能把这一条件理论改写成普遍正交安全或科学任务质量保证。<!-- source-family:SF-2026-ARXIV-2610-04510 -->

逐字本人注：

- `SF-2026-ARXIV-2610-04510` — [exact-v1](https://arxiv.org/html/2610.04510v1)，Daily2026-10-07/Oct6窗，2+2+2=6；仅§3/A.1–A.6通用几何理论与假设，不采用科学应用效果；reader2 R2-24/25必要Source/date/owner通过，literal PRE/实际POST另记，未核代码或复现。

## 04540 / Ch25

锚点：Imagined rollout开篇误差与反馈段后、“有限离线数据下”规划段前。

逐字正文：

缩短想象的 attention 序列，还要区分一个时间 position 与它承载的状态维数。[DreamFormer 的受限分支](https://arxiv.org/html/2610.04540v1)将每时刻 64×32 的 categorical latent 展平成 2048 维，配合 action MLP 作为一个序列位置，不是一个整数或无损状态；训练期以 horizon32 的 growing KV 推进想象，部署却只消费 context16 的真实历史而不作 imagination。减少 query-key 对数不等减少全部 encoder、latent、reward／policy 与训练费用，也不等实测 wall-clock；扩大 latent 同时改变 entropy／KL schedule，消融不能独占归因容量。Posterior 的夹爪已可能模糊，预测小物体继续漂移，仿真任务也不认证真机控制。状态足够性、历史长度或净质量—成本未过时，保留多位置 latent、更丰富观察与短 horizon 真实反馈，不由一个 position 的紧凑接口批准动态充分性。<!-- source-family:SF-2026-ARXIV-2610-04540 -->

逐字本人注：

- `SF-2026-ARXIV-2610-04540` — [exact-v1](https://arxiv.org/html/2610.04540v1)，Daily2026-10-07/Oct6窗，2+2+2=6；reader2 R2-26必要Source/date/owner，方法/主消融/费用/限制；literal PRE/实际POST另记，未核代码或复现。

## 04585 / Ch25

锚点：next-step对same-step监督完整段及2603-02765 marker后、稀疏waypoint时间监督段前。

逐字正文：

让 predictor 读取历史，也不能使一个不含运动的 target 自动成为完整 dynamics state：若单帧观察仅为 configuration q 的函数，而速度不能由 q 决定，则拟合该帧 target 本身无法辨识速度。[受限 JEPA 运动对照](https://arxiv.org/html/2610.04585v1)把 pose 与无 bias 的差分 motion targets 分支，并分别 regularize；它仍以前端三帧构造输入，不能与单帧当相同观察预算。该结构指出 target 可辨识性与 predictor memory 的不同职责，不证明任意空间／时间解耦；正面 planning 主要在 synthetic 环境，多帧或 GRU 在多种环境仍更好，Reacher 照片也是仿真，某些 motion probe 接近 chance。越过 GT 的 branch 分数或只重训 GRU 的 seed 分析，都不授更准确或 TI 更稳定。额外历史、差分目标、分支训练与完整规划计费；目标缺关键信息或多步质量反退时，保留 RSSM、多帧 target、更完整状态与真实观测，不由低维预测损失认证物理充分性。<!-- source-family:SF-2026-ARXIV-2610-04585 -->

逐字本人注：

- `SF-2026-ARXIV-2610-04585` — [exact-v1](https://arxiv.org/html/2610.04585v1)，Daily2026-10-07/Oct6窗，2+2+2=6；reader2 R2-27必要Source/date/owner，理论/方法/主反侧及C/D.4；literal PRE/实际POST另记，未核代码或复现。

## 04607 / Ch26

锚点：GuidedVLA完整段后、接入接触信号段前。

逐字正文：

训练期的未来状态监督还可读取同一 policy 产生的 action chunk，以 GT 相机标定、语义及实例监督比较当前／未来预测 depth 几何，再以 soft closure 回传共享 VLA；部署删除 future queries，不因此在线预测、挑选或 refine 动作。[ForeAct3D 的受限分支](https://arxiv.org/html/2610.04607v1)只预测 background／robot／object 三类 segmentation，以 staticity、rigidity 与末端运动学分别约束，不输出 instance identity，也不施加物理 hard constraints。Ground-truth instance ID 与同像素点配对后作 Kabsch，并非材料点对应，大运动或形变会失效；predicted-mask 路径仍依赖 GT ID，CALVIN Recall@2cm 从92.8降至65.9的反侧不能省。有限真机成功率与局部几何一致性不认证接触、反事实真值或安全 SLO；三维标签、点配对、未来分支训练与实机回归均计费。几何／实例支持不足时保留直接 action supervision、更完整观察及独立 controller，不把训练时软闭合当作部署时动作授权。<!-- source-family:SF-2026-ARXIV-2610-04607 -->

逐字本人注：

- `SF-2026-ARXIV-2610-04607` — [exact-v1](https://arxiv.org/html/2610.04607v1)，Daily2026-10-07/Oct6窗，2+2+2=6；仅v1非Oct9 v2，reader2 R2-28必要Source/date/owner，§3–5/T1–5/A.3/A.7；literal PRE/实际POST另记，未核代码或复现。

## 04659 / Ch26

锚点：Action chunk开篇open-loop exposure段后、较长chunk边执行边检查段前。

逐字正文：

Action chunk 的物理时间顺序还应与训练时的 reveal order 分开。固定部署仍按 left-to-right 产生动作时，可以在训练辅助目标中随机给定已知 action subsets、保留 chronological prefix，再预测其余位置；physical-time embedding 保留动作身份，content 按采样 reveal rank 的非严格≤边界、query 以严格<边界限制，防止目标从自身泄漏。[PermVLA 的受限等 compute 对照](https://arxiv.org/html/2610.04659v1)检验的是这种 CAP 训练正则，不是 chain rule 新发现，也不是部署任意重排行动。Order agreement 可由独立 slots 平凡实现，不是控制真值；参考主要为单 seed，改 horizon 的结果不能拼成 CAP 归因，M4／K8 与 diffusion 扩展的反侧及缺匹配控制仍保留。Subset／mask构造、训练与全部闭环回归计费；因果mask、chunk质量或预算不合时，保留普通 LTR 训练、短chunk与真实反馈，不能让训练顺序一致性签发动作安全。<!-- source-family:SF-2026-ARXIV-2610-04659 -->

逐字本人注：

- `SF-2026-ARXIV-2610-04659` — [exact-v1](https://arxiv.org/html/2610.04659v1)，Daily2026-10-07/Oct6窗，2+2+2=6；reader2 R2-30必要Source/date/owner，方法/等compute/A.9–10与控制反侧；literal PRE/实际POST另记，未核代码或复现。

## 04767 / Ch25

锚点：VLA-MBPO完整两段（2603-20607）后、失败人口RaWMPC段前。

逐字正文：

另一种减少 planning horizon 的分支把一段可执行 skill 而非每个控制周期作为 transition：flow policy 的 seed、object code 或带 preconditions／effects 的 label 指定动作程序，world model 预测其 settled endpoint，再由同一 planner 比较可行性与目标代价。[受限 flow-skill 实验](https://arxiv.org/html/2610.04767v1)仍依赖示教与 skill segmentation；object code 需要稳定对象身份，从 proposal 移除 preconditions／effects bundle、而 action label 保持的对照不识别单独 precondition 因果。Seed 压缩的 validity 从57%降至30%，oracle 最优计划获低预测 cost 而 beam 会剪掉必要中间移位，这提示 ranking／search 瓶颈，却不证明 world model 全部正确；主要结果用 GT pose，感知三视角避免完全遮挡，physical-time 对齐不是 wall-clock 成本。各模型数据量和 CEM 预算也不同，全部 skill 训练、候选解码、validity、预测与搜索均计费。技能不适用、对象身份或排序失配时，保留更细动作模型、可靠技能与短horizon真实反馈，不由 settled endpoint 代理或少transition批准完整过程安全。<!-- source-family:SF-2026-ARXIV-2610-04767 -->

逐字本人注：

- `SF-2026-ARXIV-2610-04767` — [exact-v1](https://arxiv.org/html/2610.04767v1)，Daily2026-10-07/Oct6窗，2+2+2=6；reader2 R2-31必要Source/date/owner，§III–V及skill validity/search/oracle反侧；literal PRE/实际POST另记，未核代码或复现。
