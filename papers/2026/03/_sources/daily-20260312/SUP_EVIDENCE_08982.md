# 2603.08982 — SVG-EAR：误差路由与共归一化的centroid补偿

作者 mar12_model_continue，2026-10-09。实际[exact-v1](https://arxiv.org/html/2603.08982v1) §4–6/Eq1–8/Table1，必要§7归一化假设/§8核状态/§10配置；非全部附件、代码/复现或图数。batch4冻结题摘准入/本日独核日期复用，owning arxiv.content/findable registeredMar11UTC02:02:39与公告下界同BJT03-11，Submitted03-09不作公开日。Current v2同题摘无withdraw/具名纠错或先稿信号，不比全版。

**2+1+2=5，当前gap深入。Owner MODEL-SELF-ATTENTION/Ch14**，不是因video应用放Ch24。Actual Ch14 120–138尾mass/DSA/SLA2、490–510算子改变/MonarchRT完整局部和Ch13/15入口；Ch24生成器性能/缓存局部1380–1450作分责。SLA2是两条各自归一输出+learned gate，MonarchRT是结构因子+适配训练；当前不拥有原query配key centroid、cluster count进入同一softmax分母、按近似误差而非mass分exact块。拟SLA2完整段后单段，不重复kernel owner。

§4 Q/K flashkmeans并排列，块级mask=1原QK,V，mask=0仍原query配key centroid，聚合value mean且乘cluster size；exact和centroid在同一normalizer，不是单独归一再加两output、不是删除尾mass或exact dense。选择probe用query centroid分别测各key/centroid的exp-logit误差，value-aware Eq8再加value差，成本O(Cq Nkd)；greedy error/blockarea分exact预算。解的是未归一proxy/0-1knapsack近似，greedy非全局最优，块area非实际kernel成本，normalizer耦合可破坏排序。§7“approximately unchanged”无定量tolerance、两处M=0互矛盾、Eq13指数误写/17–19分母Zi²当pseudo-probability、20局部norm误跳全局δq，不采用完整定理常数或asymptotically tight；attention-map界即使修复也非value output/多层/最终视频无损证书。§8伪码E初额外Y²/acc起点未闭合，概念支持共归一化但不授实现通过。

§5 Wan2.2A14B720p I2V/T2V与Hunyuan13B720p，VAE后21/33frames每帧3600tokens；各50randomsamples、VBench增强prompt。PSNR/SSIM/LPIPS对full output而非真实视频；ImgQual/SubCons为proxy。Table1 WanI2V EAR29.759/1.61×，Turbo28.344/1.77×，不是同时29.759和1.77；T2V24.995/1.59×、Turbo23.940/1.75×；Hunyuan31.043/1.93×但ImgQual.659低dense.665、SubCons.903低.904。Wan T2V ImgQual.706低SVG.712，非全质量支配。§10不同top-p/.85vs.9、warm10/50vs15/50、cluster预算变化，比较完整配置非唯一routing因果；EAR/SVG2同前层dense、50steps不授全层都稀疏。文称E2E inference ratio但硬件/precision/inferencebatch/完整endpoint/CI/SLO未披露，6.5%与13.74×为作者图文不独核图精数、不迁移生产。聚类/排列、probe、centroid、routing、fused-kernel和densewarm/decoder全部计费；不将parameter-free升为零开销。§6不测DiT外推广。

## 逐字 PRE

> 省略的块还可以用 centroid 保留近似贡献，而不先删除再独立补一条输出。一个受限分支聚类 Q/K，为未精算的块让原 query 读取 key 与 value 的 cluster mean，并把 cluster 大小计入与精确块共同的归一化；再用 query centroid 探测各块的近似误差，按误差与块面积之比分配 exact 预算。这与按 attention mass 选块、或两条归一输出经 learned gate 混合不同，未归一误差只是排序 proxy，归一化耦合和 value 差仍可使它失准。[有限视频对照](https://arxiv.org/html/2603.08982v1)支持质量—计算取舍，不授最优路由或 dense 输出等价，部分质量退步且更快配置会降低保真。聚类、排列、探测、centroid 聚合与专用核均付费；分群、归一化或真实净收益不稳时，应扩大 exact 预算、保留成熟 sparse 分支或回退 dense Attention，具体 IO 与缓存执行仍由 runtime owner 验收。<!-- source-family:SF-2026-ARXIV-2603-08982 -->

末注只证据：exact-v1上述局部，5分gap深入；normalizer前提与印刷/伪码未闭合，不采定理常数/exact实现/全SLO，EAR/Turbo与quality反侧分账。Source/date/actualowner逐字PRE待独核，无必要external，未写Books，不授DAY。

本次实际必要Source/date/评分5/当前owner逐字PRE经mar12_independent_continue独核通过，root授指定单段与本人末注窄锁。作者已实际写Ch14新134/注643，顺读120–145；diff --check通过，锁已释放。root实际顺读Ch14完整120–145、本人643注与逐字PRE回对，actual正文/完整邻接及本人注POST通过；不授DAY。；无需外部补件。
