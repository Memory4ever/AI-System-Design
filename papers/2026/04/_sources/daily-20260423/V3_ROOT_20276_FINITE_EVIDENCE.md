# 04/23 定点证据：2604.20276v1

本笔记是 root（04/23 日报作者）的必要证据与 Books 提案，不是独立复核或本窗日期 Gate。[官方 exact-v1](https://arxiv.org/html/2604.20276v1) 已实际读 §2、§3.1、§3.3、§4.1–4.5、§5.1–5.2 与 Appendix A 的例外；[身份页](https://arxiv.org/abs/2604.20276v1)显示 v1 submitted `2026-04-22T07:24:53Z`，但投稿时间本身不证明首次公开。最终落窗仍须核官方公告批次。

**问题与旧方案。** 比较不同层的 nearest-neighbor ratio/TwoNN/Gride 读数，可以观察表征几何变化；它低成本、可跨层画图，却容易被误叫作底层流形的真实 intrinsic dimension，进而把早层读数上升解释为表达自由度真的增加。论文给出有条件的反证：对固定确定性、在相关输入测度上 Lipschitz 的映射，§3.1 的 pushforward pointwise dimension 逐层不增；标准 dot-product attention 在无界域并非全局 Lipschitz，hard top-k/argmax 的不连续分支也不能直接套用。**不采用** Appendix B 对任意非紧支持集的 Hausdorff 维度单调断言：其证明把 `f(supp μ)` 与 `supp(f#μ)` 直接等同，忽略后者可能多出的闭包点；非紧正整数支持可经 1-Lipschitz 映射成稠密有理像，使 pushforward 支持为 `[0,1]`。这一反例仅否定该更强的支持集表述，不否定 §3.1 的 pointwise 结论；紧支持或像闭合是可能恢复该分支的额外条件。给定有限词表和有限 token 序列，离散支持的经典维度甚至为零；这说明该数学对象对实际容量可能并不有用，不等于模型没有丰富表示或连续放松下仍为零。

**机制与评价边界。** 作者在 WikiText 10k prompts 的 Llama-3.1-8B、Mistral-7B-v0.3、Pythia-6.9B 最后 token hidden states 上观察到 Gride 读数早层上升；邻近距离一起变大、比例趋近 1 可产生该读数，固定 hidden width 不能解释层内上升。与 von Neumann entropy 曲线相似只提供可能的 variance-spread 解释，§5.2 明言理论连接及可靠替代 estimator 尚待研究。此论文没有证明所有表征指标无用、没有证明各种输入度量下的语义容量，也没有给出将读数用于模型发布/路由的受控收益。Appendix C 报告 LLM/ViT 抽取使用 T4；不涉及生产并发/SLO。

**Owner 比较与待决。** `MODEL-EMBEDDING` Ch12 已明确 TwoNN 可被短范数 hub 扭曲、裁剪后的低读数不等真实维度；`MODEL-TOKENIZER` Ch11 交付有限离散 token identity，Ch13 才引入位置。现有 Ch12 尚未把“估计器统计量”和“所定义的真实维度”分开到该程度，因此可能有一条长期测量边界的窄增量，而非新增生成/训练机制。拟评分 2+2+2=6、深入核实后决定是否在 Ch12 当前内在维度段前后补一段；不得把论文的‘所有层真实维度不增’当作无条件 Transformer 定理，也不得以此否定现有 embedding-hub 经验。需非作者先核贡献准入、定理适用域、owner 实际缺口；通过后才协调写 Books 并做写后复核。当前不记 Integrate、不签日级 Gate。

**后续实际状态（2026-09-28）。** [apr02 非作者必要复核](V3_APR02_20276_FINITE_INDEPENDENT.md)认可窄 owner gap、同时指出 Appendix B 的非紧支持反例；root 已只写受限测量边界到 [Ch12](../../../../../books/part-02-model/12-embedding.md)，[apr20_resume 非作者实际写后复核](V3_APR20_20276_CH12_WRITE_AFTER_INDEPENDENT.md)通过。上述“待决”段保留研究时序，不再代表 Books 尚未写；04/23 日期与整日 Gate 仍未通过。

**04/23 日期有界重核。** 本地原始 `arxiv-owner-replay-20260903/20260423/arxiv-owner-receipt.json` 把该 ID 记为 v1 提交 04/22 07:24:53Z、v1 metadata update 04/23 00:33:34Z、DataCite 初建 04/23 02:01:41Z、arXiv OAI 当前 datestamp 04/23；相邻 `2604.20274` 的 v1 metadata update 04/23 00:33:22Z、DataCite 初建 02:01:38Z。arXiv 官方 [availability schedule](https://github.com/arXiv/arxiv-docs/blob/develop/source/help/availability.md) 的周三 20:00 美东公告对应北京时间周四 08:00。日期判断只取**精确 v1 + 官方常规公告批次 + 邻近 ID + OAI/DOI 原字段**的合取：有据推断在 04/23 08:00～09:00 本窗；提交、metadata update、DOI、OAI 任一字段都不是逐篇公开日志，若存在 moderation/defer 个案则须重开。该有界归属不替代本日其他家族的日期审查或日 Gate。
