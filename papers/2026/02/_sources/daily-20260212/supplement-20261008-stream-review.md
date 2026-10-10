# 2602.09396v1 必要审阅（作者准备，独立 Source 尚待）

精确身份：[Squeezing More from the Stream](https://arxiv.org/html/2602.09396v1)。完整AB准入与Feb11包络已经root实际核。评分2+1+2=5；因优化器边界与正文/算法差异定点深入，不遍历其余附件。原件：model-next-outline、stream-core2、streamtail、streamCfind。

拟采用：没有大replay并不等于不能用小固定轨迹buffer做辅助latent prediction；高度相关stream下，只将SPR当前更新对历史方向正交，仍不能解决ObGD policy更新与SGD辅助更新的冲突，作者须再对实际RL update投影。§4.1–4.3 L146–173与Table1实际反侧：strq+SPR/orth在Atari40M及MinAtar均弱于原strq，orth²才恢复；不声称SPR/单次正交普遍改善RL，更不将latent predictor当部署world-model。

机制与必要限定：SPR负cosine、stop-gradient target与共享encoder/独立head，K=5临时buffer（非零memory）；§5.3默认tau=0使target为online复制，image augmentation承担regularization，不照AB说固定独立momentum target。AppA.8 L424–426 ObGD估计只计Q-learning update L1范数，忽略SPR，mix=.5/kappa2只是作者缓冲设定。AppC Eq4给raw-gradient EMA，Alg1 L495–497却把已正交后的delta入history，不能授同一精确实现/证明；采用投影的几何分工而非具体EMA recipe或普遍稳定保证。IID→u≈g亦非由独立性自动成立，不采用此断言。

评价：Atari26（40/100Mframes）/MinAtar5M/Octax20M各5seed，Table1跨环境回报std、IQM95%CI分别理解。Table2 effective-rank与tSNE不是控制能力或因果信息度证明，DQN rank518→526很小仍有收益。buffer5的DQN对照不足以解释全部SPR收益，但不是完全机制分离。Table6 AppA.9：JAX4CPUcore/4GBRAM，DQN20.73h→SPR31.25h，QRC36.85h→SPR+orth48.66h，params/memory也增；CPU型号/precision Not Disclosed，非免费算力/生产端侧SLO。latency表strq+spr+orth标签未标orth²，不将其归到完整修复变体。§6 continuouscontrol、nonstationarity、planning为未做futurework。

Source独立复核后才owner：潜在TRAIN-PRETRAINING优化/辅助目标冲突边界；不以stream主题迁入模型能力owner。尚未读实际owner同命题，不授覆盖、不写Books。
