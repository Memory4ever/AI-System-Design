# Shuffle / Probe：分别的唯一 owner 与窄 PRE 申请

必要Source已root实际独核；未授以下两处锁，不写Books。已读当前相关owner局部及相邻章节交接。

## Shuffle / TRAIN-PRETRAINING / Ch28

`books/part-04-training-system/28-pretraining.md`现§Optimizer和Batch把data order列作recipe，却未解释顺序本身的prefix variance与epoch map order项；差额不是通用‘state transition’。申请在 `## Batch、tokens 与 optimizer steps 不是同一计量` 之前加以下小节+本人静态末注，完整前锚为Architecture变化小节末段及end marker（不改）：

这提高小规模到目标规模 transfer 的可解释性，却依赖模型形状、coordinate checks 与推导假设；公式错误会表现为 activation/update scale 漂移，而不是立即报错。exact-v1 只支持 §3 推导、§4 与 Appendix B 的所测形状，且 Appendix B.2 已给出某类 coordinate check 的失败边界。架构超出校准域、rank 假设不成立或训练信号冲突时，应回退邻近规模 sweep，而不是把 μP 公式当作免调参保证。<!-- source-family:SF-2026-ARXIV-2605-15290 -->
<!-- semantic-body-binding:SF-2026-ARXIV-2605-15290:end -->

### Without-replacement 数据顺序有两种不同的误差对象

随机epoch重排在不引入额外控制时仍是清楚的baseline，但同一批样本不保证同一更新轨迹。等大小block的平均gradient满足individual variance=within-block variance+block variance；block prefix的方差常数下降，不能直接当成等样本预算下任意分块都更优。另一条条件分支从同一起点分别运行一个排列及其反序，平均两个epoch终点：在二阶可微、gradient有界、gradient/Hessian Lipschitz及固定n小步长下，order-dependent二阶项被消去，剩余顺序敏感度为O(gamma³n³)。这一平均需要两条更新路径，不等于下一epoch仅改为倒序。

[Shuffle精确v1](https://arxiv.org/html/2604.00260v1)的APR实验实际每epoch只产生一个排列，按loss ratio分块、周期翻转或交错；有限凸/MLP和小Adam100epochs best-so-far训练loss对照不能当作两map平均定理已被部署，也不证明大模型Adam、非平稳数据或任意大步长获益。记录block/prefix单位、排列、步长、optimizer与两路径成本；收益或条件失配时保留普通random reshuffling与原recipe，以匹配预算的质量验证顺序选择。<!-- source-family:SF-2026-ARXIV-2604-00260 -->

完整后锚（不改）：

## Batch、tokens 与 optimizer steps 不是同一计量

设每个 optimizer step 的 global batch 为 `B_global`，有效平均 sequence tokens 为 `T_eff`：

本人末注：

- `SF-2026-ARXIV-2604-00260` — Daily2026-04-03补窗；[exact-v1](https://arxiv.org/html/2604.00260v1) §2/3.1–3.4/§4及D.2，2+2+3=7。block prefix单位、smooth bounded条件及同起点两map平均与APR单排列分责；小Adam100epochs best-so-far训练loss不授现代LLM/所有步长普适。未核artifact或复现。

## Probe / PLATFORM-EVALUATION-SYSTEM / Ch66

`books/part-06-ai-infrastructure/66-evaluation-system.md`现1116–1121明确checkpoint noisy rank与curvature proxy不能获release权；仍缺实际training checkpoint内部层sensor、初始label成本与跨checkpoint适用域。不是重写一般proxy原则。申请在TIC曲率完整段之后、FAITHFUL-OR-FABRICATED marker之前加入以下两段+本人静态末注；完整前锚不改：

更便宜的 trial 淘汰分数也可来自曲率，但必须先核它在当前模型 regime 下是否保留目标排序。TIC类代理用 population loss Hessian $H$、data gradient covariance $C$ 形成 $\mathrm{Tr}(H^{-1}C)$，model Fisher 又是另一对象；diagonal、damping 或采样近似会改变测量，不能仅凭网络被称作近NTK就把它们置为相等。[受限对照](https://arxiv.org/html/2602.23219v1)中，linear/受约束或较大d/n配置有较好相关，tiny nonlinear配置却可弱相关或反向；输出kernel的近似不保证唯一parameter，原softmax CE下通用 $H=GGN=F$ 等价也有直接反例，故不采用该理论链签发exact泛化界。一次ResNet8/CIFAR10搜索的早淘汰排名不证明所有trial，validation估计、gradient/Fisher采样、HVP和调参均付费，小模型diagonal计算倍数不等全训练省费。先与独立held-out ranking校准；curvature非正、近似或人口变化失配时，保留完整trial/validation和原checkpoint比较，不让proxy取得release真值权。<!-- source-family:SF-2026-ARXIV-2602-23219 -->

训练中反复生成答案很贵时，还可用checkpoint内部表示估计固定prompt的成功率：先用多次生成/可信task scorer的经验成功比例作标签，再训练逐层接收base hidden states的轻量decoder probe，最终sigmoid读出。Label仍由生成式评价定义，sensor只替代高频测量的一条成本路径；checkpoint、输入、sampling、scorer、layer范围与probe版本共同冻结。不能由sigmoid输出或AUROC较高授予概率校准、weight-invariant映射或release权限。

[In-training Probe精确v1](https://arxiv.org/html/2604.01025v1)在OLMo3-7B的pre/post轨迹中支持早期→后期transfer与有限任务估计；Table3仍有0.7346等AUROC，16层稍降而8层明显降。初始生成标签与probe训练要计入摊销，base每checkpoint0.78h→0.05h是后续测量成本，不是零初始化；模型族、训练阶段或任务人口改变需重新核对生成式held-out误差。排名、平均MSE与真正校准分开验收；漂移或关键切片漏测时恢复完整生成式评测与原checkpoint比较，不让便宜sensor批准模型。<!-- source-family:SF-2026-ARXIV-2604-01025 -->

完整后锚（不改）：

<!-- semantic-body-binding:SF-FAITHFUL-OR-FABRICATED-A-CAUSAL-FRAMEWORK-FOR-RATIONALIZATION-BIAS-IN-LL:start -->
Judge 给出的理由不能仅因与标签一致就当作 faithful evidence。Blind、Truth、Flip、Placebo 与 Reveal-after 等 cue
intervention 可分离 outcome anchoring、rationale anchoring 与 explanation drift；evaluation owner 保存 intervention
identity 和 tie-aware metrics，ranking 只消费已校准结果。新增成本是多臂实验和 cue-specific 外推边界；它能发现
rationalization bias，不证明隐藏推理或真实因果链已被恢复。
<!-- semantic-body-binding:SF-FAITHFUL-OR-FABRICATED-A-CAUSAL-FRAMEWORK-FOR-RATIONALIZATION-BIAS-IN-LL:end -->

本人末注：

- `SF-2026-ARXIV-2604-01025` — Daily2026-04-03补窗；[exact-v1](https://arxiv.org/html/2604.01025v1) §3.2–3.5/4.1–4.5，2+2+2=6。MC生成label、逐层submodel sensor与generation/release分责；OLMo3-7B轨迹、AUROC二值ranking非校准、0.7346 transfer/depth8反退及初始化摊销限定，不采用hidden→能力weight-invariant理论。未核artifact或复现。

## 实际授锁与非作者POST（不修改Books静态注）

root逐字PRE与actual owner邻接通过后授两处非冲突窄锁；Probe正文按root建议移除0.78h→0.05h数字，仅保后续低费与初始化摊销。作者各已写并顺读完整邻接。root nonwriter实际POST：Ch28 713–736全部邻接、719/721/723及1912本人注；Ch66 1118–1133 TIC→1123/1125→faithfulness全部交接及6143本人注。条件/配方/费用与Source一致，POST通过，Ch28/Ch66两锁释放；不授DAY，未用锁动其它family。
