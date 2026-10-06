# 02/13 CFOUR：10993 / 10996 / 10999 / 11008

四项准入已root校准，均在119逐项落窗交集中，沿公告下界/created上界，不用submitted替public。exact-v1必要源读至具体支持/直接反侧停止。当前abs见V3_CFOURLAST3：10993当前v2(02/19)，其余v1；已有header/comments/history未见withdraw/correction标记，不遍历revision或无关附录。原返回CFOURINITIAL/CORE1–3/MORE0、2、3/LAST0–3/TAIL0–1/ALGO3；未复现、未核code。作者必要4项完成，root独立Source/PRE尚待。

## [LoRA-Squeeze](https://arxiv.org/html/2602.10993v1)

2+1+2=5，标准与拟长期rank接口深入。INITIAL §3/Alg2 L141–201、MORE0 L208–278：先高rank训练，再对AB的task delta截断；QR(A)、QR(B^T)使r_src²小核R_A R_B^T承载奇异谱，不必物化m×n。LAST2 D406–441的有限代数支持exact SVD等价；RSVD仍有近似/随机差别，Frobenius最佳不等任务无损。Post/Cont/逐阶段In分开：Cont还有target-rank refinement，In固定总步数按rank分配且可每stage至少200步，不是固定FLOPs。

Gemma3主要4B IT、1B/12B补点，13text/10VL，vision与projection冻结；B8/L1024、10k或15k步、Adafactor1000warmup与逐rank LR grid，RSVD oversample10/2iteration。Table1高到1极端压缩均值77.32<直接90.08，+700恢复90.09；In-min90.51但部分PIQA等低于直接。高rank/source-targetgap与任务均限制收益，不把spectral energy当任务知识证明。低SEM必要声明见B，实际随机运行数量/完整paired significance未采用；hardware、precision、端到端wallclock/总搜索compute、serving batch/concurrency/SLO、rank变化的alpha/optimizer-state迁移Not Disclosed。矩阵复杂度是粗估算，不是运行加速。

Books整合：TRAIN-LORA [Ch30](../../../../../books/part-04-training-system/30-lora.md) L183/185将训练rank与部署rank解耦、小核重参数化融入rank取舍；精确谱分解与RSVD分开，谱不等任务无损，极端压缩/继续训练与搜索成本、alpha/shape及训练状态身份保留。root已实际读177–195正文/邻接和末注778，非作者POST通过，窄锁释放。

## [Numerical representations in communicating artificial agents](https://arxiv.org/html/2602.10996v1)

2+1+2=5，标准完成拟Only Report。CORE1 L56–125：shared pretrained ViT不是从零无数概念证明；LSTM离散channel或fixed-line sketch/hinge loss，小numerosity主要1–5、补1–20，图像总黑面积5–10%并same/diff实例控制。三seed局部communication/entropy图支持“所测协作可拟合精确class code，却不保证unseen interpolation/extrapolation组合规则”；continuous部分abovechance但collapse sketch，不能概括全部泛化零。Dot面积控制不识别所有视觉纹理/spacing，span仍相关；并未干预compositionality以建立其causal必要性。未披露完整训练步数、hardware/precision/总compute或CI；LLM与人类语言普遍结论均不采用。仅保留局部coordination≠systematic generalization反侧，无Foundation/Agent真实通信新增接口，不声称其实验已有正文完整覆盖；不因局部模型小而撤已校准准入。

## [CLI-Gym](https://arxiv.org/html/2602.10999v1)

2+1+2=5，标准完成拟Only Report。CORE2 L121–170：gold可运行image+tests→agent Dockerfile/code perturb→重建并核failed/pass-to-pass tests→issue；新增环境逆向数据生成分支，不把S=(base,Dockerfile,code)或test通过视完整状态/语义正确。LAST0 L315–356：tests命令无法执行时全记F2P，需与实际全部test失败区分；291过滤去<20steps和cached-git/Conda捷径，仍无所有shortcut guarantee。Dockerfile再执行提供有限重复条件，不保证可变remote dependency的永久determinism。

29repo/1655instances、2.3B生成tokens，417→291success；48k SWE预训练和CLI阶段拆分。OpenHands同接口、greedy T0/128k，训练100k YaRN、B16(32B)、LR2e−5/1e−5、5%warmup、best10/15/20epoch；hardware/precision/seedCI及validation identity Not Disclosed。Table5无SWE时raw33.8>filtered32.4，有SWE时filtered38.9>raw36.4，但raw10与filtered15epoch按best配置，不能仅归data质量。hint同104条22.8<nohint23.0，full291提升是产量/数据预算变化；固定100轨迹repo diversity有局部支持，bestepoch预算不等。训练后context overflow更多是直接代价。只报告可执行environment-inversion recipe及有限人口，测试/语义/预算边界已有系统原则不授本篇算法全部已覆盖；无新保证进入Books，不把大数字视训练/生产效率。

## [ROCKET](https://arxiv.org/html/2602.11008v1)

2+1+2=5；必要数学/配置反侧深入，作者拟**争议 / Books暂缓**而非用Only遮住中心global-optimal预算保证。CORE3 §3 L109–170：calibration-whitened EVD basis→coefficient per-column threshold+global refill→ridge左因子重拟合，importance |c|×||L^-1b||^.5；finite option profile以original weight relative Frobenius误差作knapsack proxy，非真实任务损失。该有限替代机制可报告，但Cholesky whitening须L^T L=Gram的orientation与可逆/regularization条件，source chol未给方向；不采所有重建等距。

**中心可判冲突**：main L157–160 cost为kept参数、约束≤预算；ALGO3 L378/397仍计nnz kept，却L406删低cost高error而保高cost低error，L410取k≥预算。LAST1 C507–512又pruned/retained混写和≥sink；它不是同一个≤kept预算的Pareto/可行域，不能授权原全局最优或准确满足预算。重开仅需纠正kept/pruned坐标、正确支配/终点与精确离散状态实施证据；不扩全证明或代码库。AppB norm-nonincreasing本身不能推出任意operator近似误差≤1；只实际hardmask且正交残差分解有局部界，inverse whitening不保证original space同界。

支持/反侧：RefinedWeb固定256校准、dense QKVO/MLP而不embed/head，20–50%compression无healing对照；Table7 same20%局部uniform45.4→allocation52.4，但仍<dense57.6，不证明代理最优为任务最优。Table4“65.75平均”实为RWQA列65.75，五列平均非此数；20%是compression并非剩20%size。不照录普遍90%质量。LAST1 D514–539：Macko用于大/稀疏MLP，attention native更快，QKV/gate-up融合；Qwen8B B1/context256 throughput26.74等仅作者局部，precision/硬件不明确，SLO/重复/完整生成长度ND；环境表只Llama1B A10040/EPYC，不转给Qwen吞吐。healing与training-free分账；MoE≥128experts profile/DP扩展明确困难。有限实验可支持替代压缩分支，不进入Books或正面最优/无损/生产加速保证，中心争议精确保留。

累计作者96/112=90必要证据+6低分关闭，剩16普通。本批4项必要证据与处置root独立通过，LoRA实际POST已通过，ROCKET中心暂缓；累计30家族实际Books POST通过，不授日级。
