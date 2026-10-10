# 10641 adjusted agreement：必要命题与窄owner差额

[exact-v1](https://arxiv.org/html/2601.10641v1)，首8完整题摘潜力独判已过。拟2+1+2=5标准，因已确认长期measurement gap，深入受影响充分条件与构造反侧，不要求全部无关文献/附录。实际已读§2.1–2.4（count/null/adjustment定义）、§3.1–3.3/Thm3.4/Cor3.5–3.6与Prop3.7构造、§4.1。原件increment-aeq-null-core2/3和increment-first3-core4，必要核心L95–139、147–279。理论不机械要求hardware/bench：N有限count构造，收益是解释权前提，不是性能数字；实现/复现未核。

采用范围：对观测n生成null M^n，adjustment中用的期望与normalizer若在每个null support上不变，才由本文充分条件得到exact null mean0；standardization的正variance条件同时保留。不是必要条件、不能因不满足而判任何特定metric无效；§4.1明确finite exact失败仍可能有有用asymptotic。Permutation fix observed marginals虽data-driven可满足条件，不能泛化所有data-driven不可用。Thm3.4同时变换index和maximum，只常数域内coeff，不把任意max固定1套一般等价。M^n→M^{tilde n}重拟null后嵌套期望不自动tower collapse。

反例已核：u1~Binom(N,u1/N)，S=u1²、maxN²时baseline=u1+(N−1)u1²/N，interior调整为−u1/[N²+(N−1)u1]，null平均非0且以端点0 convention最多0；u1=1,N2的AS=−1/5、二次AS=−1。另S=u1，每个重拟baseline等其observed u1，标准化恒0（interiorvariance正），不具unitvariance。用于反驳“调整公式名字便签发上述性质”，不宣称Cohenκ/ARI全部失效、非0即错误分类或agreement等truth。论文容许不同endpoint convention，但本次不把全部AppendixA结果另推广，核心反例够用。

日期限定：DataCite Submitted Jan15T18:01:26Z、Updated-v1 Jan16T01:58Z、registered正式ID Jan16T03:00:18Z原字段已保存。正常无提前发布条件下official availability最早announcement Jan16T01Z、正式ID不晚于注册已存在，两界BJTJan16；提交/注册都非单独firstpublic证明。正文可见文献为既有方法不是本篇明确早正文信号。发现同命题早稿时精准隔离/重要增量重开，不移原日。

实际owner PLATFORM-EVALUATION-SYSTEM Ch66。作者实际顺读4399–4432的JudgeAgreement：population+scale+missing+pooling+metric身份、边际slice及非truth；760–782现有permutationnull构念分层；二者都未承载观测诱导null重拟与support常数条件。拟仅在JudgeAgreement两段后补一短段：机会校正须保存null生成/固定属性/重拟规则和normalizer，不只metric名称；给上述有限反例作为资格警告，support条件不明保原observed agreement与人工锚/明确Unknown，不宣布普通permutation路径失效。重复resampling/null fitting计费是工程推断非论文benchmark，不写通用运行费用或统一新的调整算法。独立source/日期/actual差额PRE待验收，Books写前仍需root窄锁；没有修改书稿。
