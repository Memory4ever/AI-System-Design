# RFM 与 RELISH：逐篇具体 owner 差额 / 单段 PRE

root 必要Source各5分已实际通过；日期316 EXTRA3、1206原27上下界。已读当前Books公共上下文/LS路由、两目标完整局部论证与相邻开篇交接。各只申请一段及本人静态注，不默认两段；未授锁不写。

## 00316 / WORLDVIEW-REPRESENTATION / Ch05

文件 `books/part-01-worldview/05-what-neural-networks-learn.md`。ROADMAP唯一节点为WORLDVIEW-REPRESENTATION（不新建owner）。已有equivariance可降有效维度与有限偏置/泛化反侧，但没有具体train-partition symmetry把迭代特征卡在held-out fixed points的more-data非单调机制。

完整左锚正文与marker：

> 不过，这个量只拥有几何诊断权，不能接管泛化验收权。它依赖渐近样本、流形与群作用、充分优化等强假设，生成模型推导还集中于 DDIM 或线性高斯设置；估计过程本身也可能需要多个样本规模和多次模型拟合。若真实数据不存在所假设的对称性，或 intrinsic-dimension 估计与实际分布外表现不一致，就应回退到切片、反事实、held-out 与 distribution-shift evaluation，而不是把 representation gap 当作任意现代网络的通用 generalization error。
> <!-- semantic-body-binding:SF-2026-ARXIV-2605-21692:end -->

右锚完整：

> 因此，“模型学到了正确特征”不能只靠总体 accuracy 证明。需要构造切片、反事实、扰动和跨分布评估，检查模型究竟利用了什么相关性。

之间拟一段：

有益的任务对称性，也不能与训练划分偶然形成的对称性混为一谈。在一类用Mahalanobis kernel和梯度外积迭代更新feature matrix的受限代数任务中，reflection-invariant训练partition配合特定初始matrix，会让未见fixed points持续难以泛化；增加同一结构的样本未必解开它，删除少量点破坏该划分对称反而改善。这里的限制属于Gaussian/quadratic kernel、one-hot任务与指定群orbit/初始化，不是所有Transformer grokking必须删数据或破除不变性。[具体构造与对照](https://arxiv.org/html/2604.00316v1)因此要求将数据partition、initial feature与学习器共同纳入泛化诊断，而不是只按训练占比预测能力；kernel求解、梯度统计和重训练仍付费。真实任务无法验证这些条件时，保留语义保持增强、独立划分与普通held-out/OOD验收，不由局部反例签发通用数据选择策略。<!-- source-family:SF-2026-ARXIV-2604-00316 -->

本人末静态注一条：`SF-2026-ARXIV-2604-00316` — Daily2026-04-03；[exact-v1](https://arxiv.org/html/2604.00316v1)§2.1/3/Finding3.1/Table1/4/Finding4.1，2+1+2=5，仅partition symmetry/特定kernel初态到fixed-point泛化停滞的资格；保finite algebraic构造/经验vs收敛分责/全部费用，不授LLM删数据配方或普遍grokking，未核实现/复现。

## 01206 / MODEL-DECODER-ONLY / Ch18

文件 `books/part-02-model/18-decoder-only.md`。现词表projection/weight tying只解释next-token输出，latent reasoning的readout是推理内部验证；没有冻结decoder的token表示转single-pass supervised scalar head替代numeric-text生成及不同head/targetscale资格。唯一差额不挪到Evaluation重复头机制。

完整左锚：

> 模型用同一组词表坐标完成输入 lookup 与输出评分。是否共享取决于 checkpoint，不能把它当作 decoder-only 必然条件。

右锚 `## 从 logits 到 token 还差一步`，其后现全vocab/nextlogits/tokenloop全文保留。之间拟一段：

Decoder的hidden state也可以服务于非文字输出，但必须更换并训练目标读出，而不是让词表概率自动成为数值预测。一个受限回归分支冻结LLM token表示，以一个可学习latent query反复cross-attend这些状态，再输出scalar；训练split上的target normalization和Huber loss属于这份任务head，不能在测试人口重估尺度。与参数匹配MLP的有限对照支持该读出选择，ranking reward还可能改善相关排序而不改善RMSE，WMT和STS也有收益差异，故不能说backbone天然拥有通用精确数值知识。冻结前向、head训练/优化与多次候选ranking都计费；任务、尺度或完整预算失配时，保留简单linear/MLP readout、普通numeric-text输出与独立回归验收，不由一个任务head替代标准next-token生成接口。 [必要机制与反侧](https://arxiv.org/html/2604.01206v1)。<!-- source-family:SF-2026-ARXIV-2604-01206 -->

本人末静态注一条：`SF-2026-ARXIV-2604-01206` — Daily2026-04-03；[exact-v1](https://arxiv.org/html/2604.01206v1)§3.1–3.3/4.1/C3.3–3.6，2+1+2=5，仅single-query scalar readout与next-token/targetscale接口分责；保parameter-matched/STS tie、ranking≠RMSE和冻结前向/训练/候选费用，不授数值真值或全任务/SLO，未核实现/复现。

PRE/锁尚未授权；写后各发actual正文、完整邻接与本人注供root非writerPOST，非日级完成。

root actual两PRE/Ch05 147–179和Ch18 154–188完整交接通过，授各单段+本人注；作者逐字实写并顺读完整邻接/自身注，限定diff通过：RFM Ch05 169（162–178）注683，RELISH Ch18 169（153–188）注441。root随后实际各正文/完整左右段/本人注nonwriter POST PASS，有限kernel和任务head资格保留，旧文完整；两锁释放，可同步真Integration，不授DAY。上段申请态只履历。
