# DP-SGD 10237 受影响理论必要证据提案

终裁：root实际adversary/proof核，通过5受影响深入中心Disputed隔离。不得将以下提案的Only改写视作定理已修有效；中心finite statement与domain采用暂停，proof路径仅限定说明。Formal92/105、13普通（同时PnP终裁）。

精确[原文](https://arxiv.org/html/2601.10237v1) §4.1–4.3/§6.1–6.2 Eq13/17/20–30 与 §7/8，缓存 adversary/proof/boundary-necessary.txt。拟5受影响理论/设计反证深入，仅报告，待root实际核定；不授普遍隐私学习不可行、实际攻击/复现或新Books长期gap。

原用sampling/大数据直觉希望强privacy兼顾utility→one-epoch randomshuffle的whole-update worstcase f-DP对照，给定所有其他样本clippedgradient和batchsize辅助知识，从batch noisyupdate重建Nth贡献→需要重新审查“加大数据自动抹平worstcase distinguishability”的局部假设。zero-out adjacency与有效Nth梯度norm=C、fullperupdate轨迹而非仅最终weights、M固定轮数、Gaussiannoise机制都是限制，不能推广部署eavesdropper或任何DP算法。

用maxcoordinate suboptimal test得到f_sub≥f_shuf，再由pointdistance≤sep(f_sub)≤sep(f_shuf)推lowerbound。**有限M公式反侧**：Theorem6.1写M≥1和无修正下界，而§6.2实际proof Eq29/30含(1−ε_M)，ε_M=2/(M√(4πlnM))，原文明确为了rigor保留proof但statement省略。lnM要求M≥2；不能把删掉正修正因子的强有限bound当已证。不自行修作者statement。本窗只记录源内矛盾和含修正的受限proof路径，不采用generic唯一noise floor/最优privacyutility定理。若需要准确有限定理，须作者修正statement/domain或给删除因子的额外论证；不无界附录追查。

§7 clean σ=0优选optimizer固定到noise，clipping C在chosenσ优化；JAX Privacy/perexampleclip/noise once logicalbatch/microbatch32、CIFAR/SVHN/AGNews/ResNet/ViT/encoder-only，epoch1/10/25及shuffle/Poisson。不是每noise最佳预算matchedutility，也不能用multi-epoch accuracy替代oneepoch定理延拓；§8作者承认有限multi-epoch sep仍open。本文限于above shuffle，不采用未核Poisson扩展或ε/δappendix公式，不照录foundationmodel生产预算/noise阈值预测。硬件仅DAS-6 acknowledged、precision/完整seed/实际SLO未披露；没有实验复现。理论受限条件与有限statement冲突可安全仅报告，既不删有效反证也不假定全体DP-SGD失败。
