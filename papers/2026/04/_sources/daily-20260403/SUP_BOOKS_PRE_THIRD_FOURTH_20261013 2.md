# 已通过四项 Source 的逐字窄 PRE 申请

已实际重新读 PROJECT_CONTEXT/LEARNING_PHILOSOPHY/WRITING_GUIDE、LS2026 current路由；ROADMAP唯一owner及相邻章节交接已读。仅拟新正文和本人静态注，不改原段、不自行授锁；root非作者需实际owner/完整邻接/PRE核后才写。原62冻结不受影响。

## 00018：MODEL-SAMPLING / Ch20

文件 `books/part-02-model/20-sampling.md`，具体差额是已完成独立rollout之外，在单一轨迹已知高熵位置复用prefix来分配下一次生成预算。不能由当前“剪枝前缀”或“completed-trace classifier”替代这一复用/局部分叉责任。

完整左锚：

> 这条路径至少有两个不同的成功概率。`Coverage` 问正确候选是否出现在集合中；`Selection`
> 问系统能否从已有候选中识别它。`pass@N` 只能给出前者的上界，不能证明 self-verifier 能达到这个
> 上界。扩大 `N` 可能提高覆盖率，也会带来更多近似答案、相关错误和选择成本；若 selector 的辨别力
> 没有同步提高，更多样本甚至可能让最终选择更不稳定。

右锚为现完整“讨论选择器是否‘最优’之前，还要规定交付目标…”段，保持其胜率/数值reward全文。拟在两者之间仅两段：

多路径预算不一定要每次从 prompt 重新支付完整生成。若已完成的轨迹中保存了若干高 token entropy 位置之前的 prefix，可以从这些位置重新抽取下一 token，再各自完成后缀；这里分配的是“在哪里重新分叉”的预算，而不是将高熵 token 判为错误或把后缀当独立解答。局部高熵与随机位置在同 generation budget 下的有限数学对照支持这一选择分支，但共享前缀也会保留相关错误，完成后的候选仍需要单独的答案检查。<!-- source-family:SF-2026-ARXIV-2604-00018 -->

entropy 只测当前模型分布，生成后较低的熵也不是正确性验收；没有可靠 verifier 时不能以“after-think confidence”自签停止。该路径仍支付首条轨迹、prefix/cache 保留、概率读取、重生成和候选检查，不同型号或 API 价格不能当同计算预算。受测两模型、两数学任务及训练集调参不授普遍接近满分，也未恢复有限 logprob API 与完整词表 entropy 的等价实现。信号不可得、分支强相关或检查费用不合算时，保留普通完整 self-consistency、随机分叉或单路加独立 verifier。<!-- source-family:SF-2026-ARXIV-2604-00018 -->

本人静态注末尾追加一条：`SF-2026-ARXIV-2604-00018` — Daily2026-04-03；[exact-v1](https://arxiv.org/html/2604.00018v1)§3/4.4–4.7，2+1+2=5，仅采用高entropy prefix分叉的同budget局部选择；保相关错误/原entropy接口资格/verification及全部费用，不授truth或通用可靠性，未核实现/复现。

## 00421：MODEL-MOE / Ch21

文件 `books/part-02-model/21-moe.md`，唯一差额是 router score 可由 backbone 现有坐标直接提供；当前独立linear/子空间/Gaussian router未表达“无额外router参数≠无routing学习”。完整左锚：

> `g_e(x)` 是选中 expert 的路由权重，可能在 top-k 集合内重新归一化。不同架构可使用 top-1、top-2 或其他 routing，稳定问题都是“谁被选中、权重多少、负载怎样”。

右锚现完整“Linear router 保留输入在方向上的符号…”段，保留子空间路由全过程。之间拟仅两段：

产生 expert logits 也不一定需要新增 `W_r`：当 expert 数为 E 时，可以将当前 hidden state 最后 E 个坐标直接作为路由分数，继续执行原 Top-k 和权重聚合。省掉的是独立 projection 的参数，backbone 仍端到端更新这些坐标，因此无参数 router 不等于 routing 没有学习；content representation 同时承担选择信号，也使两种用途更紧地耦合。<!-- source-family:SF-2026-ARXIV-2604-00421 -->

这条有限替代在小型 GPT-2、8 experts/Top-2 和无 auxiliary loss 的训练对照中可以工作，但固定随机 projection 也有竞争力，WikiText perplexity 27.4 仍高于 learned router 的26.7。省下的约0.07M参数只占约520.81M模型很小一部分；较高的跨token路由entropy不是每batch负载、capacity admission 或通信均衡的保证，早期仍可能集中于少数 experts。训练预算、选择统计和完整 dispatch 成本需分别验收；hidden 坐标耦合、负载或质量回归时，保留独立 linear router、均衡约束与原容量限制，不由移除一层参数签发部署收益。<!-- source-family:SF-2026-ARXIV-2604-00421 -->

本人静态注末尾一条：`SF-2026-ARXIV-2604-00421` — Daily2026-04-03；[exact-v1](https://arxiv.org/html/2604.00421v1)§2–4/Tables1–2，2+1+2=5，仅采用last-E hidden routing与骨干学习分责；保fixedrandom/质量反侧、小参数份额、非batch均衡与完整费用，未核代码/复现。

## 00666：MULTIMODAL-GENERATIVE-PARADIGMS / Ch24

文件 `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md`，在“Masked Diffusion 的训练预算可以按 Locality 重分配”内，完整左锚：

> 这种加速依赖 locality bias，可能削弱远程依赖和全局一致性。现有实验不能证明任意语言或长上下文任务都受益；长程 slice 回归时，应回退均匀 mask、混合采样或显式增加远程依赖样本。

右锚现完整“预测预算也可以围绕离线标注的关键 span 重分配…”段，不删teacher关键span/双view全文。之间拟仅两段：

训练可见关系也可以由另一个模型的顺序代理来组织：先以 AR teacher 在干净 causal prefix 上的 token NLL 做全训练人口分位数分桶，再让较高 NLL 的桶更早进入带随机门槛的结构化 mask；上下文与尚后桶仍分别按小概率/大概率遮罩。这里借用的是便宜、可复用的 AR 条件困难度，不是观测当前 diffusion model 实际反向轨迹；只将少量训练样本切换到该结构，原 denoising objective 保留，不能把训练桶顺序直接当部署最优 reveal schedule。<!-- source-family:SF-2026-ARXIV-2604-00666 -->

[有限训练对照](https://arxiv.org/html/2604.00666v1)中结构样本占10%、两类遮罩率为.05/.95；随机分桶本身已有收益，困难度排序的额外差额须与它分开。s1K上 LLaDA/Dream 的 LoRA32、1024长度、30epochs及8A100设定不授所有任务提高，HumanEval与GSM存在低于原模型的反侧；更大 distillation数据与不同epoch也不是等预算。AR评分、数据构造和target训练全部计费，0.6GPUh只属整理、tokens/step不是端到端墙钟。teacher困难度失配、质量或完整费用不合算时，保留均匀/混合mask、原locality与独立验收的部署顺序。<!-- source-family:SF-2026-ARXIV-2604-00666 -->

本人静态注末尾一条：`SF-2026-ARXIV-2604-00666` — Daily2026-04-03；[exact-v1](https://arxiv.org/html/2604.00666v1)§3/Alg1/4.1–4.4，2+2+2=6，仅采用AR-NLL桶到corruption可见关系的训练接口；保随机桶反侧、task回归、teacher与target预算/TPS口径，不授真实困难/最优揭示顺序，未核实现/复现。

## 00055：MULTIMODAL-EMBODIED-VLA / Ch26

文件 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md`，完整左锚：

> 若希望在一个新 episode 内调整已有 VLA，而不是增加独立 RL head，另一条分支让学得的 progress sensor 直接成为 LoRA 更新的 reward consumer：每步用进度差 `r_t=p_t-p_{t-1}`，在所给 value-free 配置中以 `A_t=r_t` 进入 clipped policy 更新，而非估计长程价值。[有限 test-time adaptation](https://arxiv.org/html/2601.06748v1#S3)因此改变的是部署期间哪些参数收到何种反馈；sensor 的进度不是环境成功真值，ratio clipping 也不保证保留原 SFT prior 或物理安全。遮挡、阶段错认与非单调进度会奖励错误动作；有限模拟及九项真实任务不支持所有任务增益。进度模型前向、episode 内更新、间隔/步数搜索和策略重置均付费，LoRA 状态少不等控制闭环免费；proxy 或闭环回归时应停止适应，保留静态 policy、独立 controller 与人工接管。<!-- source-family:SF-2026-ARXIV-2601-06748 -->

右锚现完整“若人工纠正针对flow生成的action chunk…”段，保其同噪声/endpoint/gate边界。之间拟仅两段：

昂贵的视觉进度信号也可以只负责训练初始化，而不持续进入在线reward。当 reward 取 running maximum 的增量时，一次虚假的高峰会抬高历史上界，使后续真实进步长期得不到增量；一个有限分支在完成 rollout 后，用排除当前点的邻窗median抑制孤立峰，再以平滑进度形成 value warm-up 标签。窗口包含未来 observation，因此它是离线轨迹处理，不是运行时 causal progress sensor；初始化之后停止查询VLM，PPO再用稀疏任务成功与policy self-certainty继续训练。<!-- source-family:SF-2026-ARXIV-2604-00055 -->

self-certainty 的 uniform-to-policy KL 只奖励模型分布变得确定，不认证动作正确或世界模型可信，权重过大会遗忘或坍缩。SPOC/CHORES的有限模拟与阶段对照支持“修正peak污染、分开昂贵初始化和后续reward”的分工，Fetch/RoomVisit仍有低于其它方法的切片，不能宣称所有任务更强或已获现实控制安全。VLM轨迹、滤波、200K warm-up和后续20M/50M训练均计费；窗口与阶段独立因果、完整VLM省费也未证明。进度不可信、certainty代理失配或闭环回归时，保留稀疏真实成功、原value学习与已验policy/controller，不让低训练成本替代动作验收。<!-- source-family:SF-2026-ARXIV-2604-00055 -->

本人静态注末尾一条：`SF-2026-ARXIV-2604-00055` — Daily2026-04-03；[exact-v1](https://arxiv.org/html/2604.00055v1)III-A–D/IV-A–E/Alg1/TableIII，2+2+2=6，仅采用spurious running-max峰与离线value初始化/后续reward分责；保future窗口、certainty非truth、task反侧/全部训练费用，不授物理安全，未核实现/复现。

## 授权状态

四 item Source已由root实际独核，本PRE尚未通过；只申请上述四不冲突family的具体插入范围与本人静态注。每篇写后分别给root实际位置/完整邻接供nonwriter POST，不自授日级。

## 实际授权与写后独核回执

root 实际全文PRE/当前owner精确锚与完整局部论证通过，授四item各两段与本人注。作者按逐字PRE落实，实际正文/完整邻接/本人注均顺读、限定diff-check通过。root随后逐篇真实nonwriter POST通过：00018 Ch20 345–364/本人注711；00421 Ch21 61–78/注1072；00666 Ch24 621–639/注2679；00055 Ch26 358–374/注2418。旧完整锚及后续机制保留，proxy/预算/反侧近正文；四窄锁已释放，可同步真实Integration，不授DAY。上段旧申请态仅保留履历，当前以上实际回执为准。
