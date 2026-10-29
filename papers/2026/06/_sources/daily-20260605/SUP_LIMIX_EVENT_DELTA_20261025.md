# 04485 LimiX-2M：首次必要读取中发现早发布，事件差额定点校准

作者supp_20260605_author，仅Daily2026-06-05补Jun04。R33–36有效完整题摘/精确v1 Jun04 arXiv联合日证复用；新增早公开线索须局部核去重，不否定已成立的Jun04 arXiv事件，也不把模型release日期当论文正文首次日期。

官方notice `https://arxiv.org/abs/2606.04485v1` GET200/44457bytes，实存`SUP_2606.04485_NOTICE_20261025.html`，SHA256 `d00ab2d8e23463057e175725faa8e05a9e6a346bfe1e2e40a3fb96c40e7b290f`。完整当前页未见withdrawn/removed/correction说明；v1 Jun03 06:07:33UTC，v2 Jun04 07:27:03UTC、ICML accepted为当前comment，不借v2或接受日期搬移旧事件。本文精确v1标题LimiX-2M: Mitigating Low-Rank Collapse and Attention Bottlenecks in Tabular Foundation Models。

官方HTML `https://arxiv.org/html/2606.04485v1` GET200/897422bytes，原件`SUP_2606.04485v1_20261025.html`；SHA256 `0190c4c8e4409645456ff9a72f9fa8def5662c2b9be087c8b4cb684a647414df`。首次必要读§3–4/Eq1–10、§5/T1–6关键条件与反侧、A/Prop3.1、B1–5/TheoremB1/PropB2、C1/C3/C4/C6及C7方法文字，不全表逐dataset/全refs/上游理论或复现。C4出现**作者称main experiments Sep2025、2M released Oct2025**的新firstpublic/dedup信号，不能忽略后仍把RBF/SNF和2M当本日新release评分。

## 有限恢复：仅同一模型/原报告/原实现，不研究其他2025材料

官方repo `https://api.github.com/repos/limix-ldm-ai/LimiX` GET200/7101bytes，`SUP_LIMIX_REPO_META_20261025.json`。created_at2025-08-27、default main，当前description已变并非历史逐字证明。README commit API首page30（`SUP_LIMIX_README_COMMITS_20261025.json`，GET200/150796bytes）全为2026Sep近期修改，**不继续遍历历史页**。改用明确firstpublic问题的bounded `commits?path=README.md&until=2026-06-03T16%3A00%3A00Z&per_page=5`（`SUP_LIMIX_README_BEFORE_JUN04_20261025.json`，GET200/20879bytes）定位最近pre-window README ref `9e84701974af623ebe65d4751522b1fa99c3f02b`，committer2026-03-03T02:25:17Z；其余四结果仅日期路由，不展开。

同ref README via `contents/README.md?ref=9e847019…` GET200/20832bytes，Base64原件`SUP_LIMIX_README_9e847019_20261025.json`，已完整解码实际读。News写**2025-11-10正式发布LimiX-2M**，链接2M weights和retrieval/no-retrieval配置。该官方旧文与新paper C4的Oct2025不一致，保原口径，不补统一release日；二者都指向早于Jun04的模型公开，不单独证明更早论文或每一新公式已公开。Git commit时间本身亦不当可信发布钟/逐字全球首发证明，结合作者release说明使用，不追假想渠道。

同ref tree `git/trees/9e847019…?recursive=1` GET200/20456bytes，`SUP_LIMIX_TREE_9e847019_20261025.json`，truncated=false。只选同一模型的三实现文件和README明确所链旧technical report，不审整仓库：

- `model/encoders.py` contents原件`SUP_LIMIX_ENCODERS_9e847019_20261025.json`，GET200/38234bytes，实际读145–254 RBFembedding：fixed uniform/random centers（buffer）、可选learn sigma、hard floor(log10)/sign/exponent-digit embeddings，逐kernel sigmoid gamma+tanh beta调RBF振幅后LN/projection。
- `model/layer.py` contents原件`SUP_LIMIX_LAYER_9e847019_20261025.json`，GET200/42135bytes，实际读460–501：`smf`已为sample/sequence attention→MLP→feature attention，不称此排序作为Jun04首次新release。
- `model/transformer.py` contents原件`SUP_LIMIX_TRANSFORMER_9e847019_20261025.json`，GET200/20237bytes，只核layer_arch绑定线索，不冒完整2M inference/配置/池化已审或运行。旧README模型功能/权重和现文件并不自动证明任一checkpoint采用全部可选分支。

raw.githubusercontent当前README及旧PDF各一次connection reset/000，非body空=无内容；API原件均可恢复，不冒全源访问外阻。旧PDF通过官方tree实际blob SHA `f6b4e25b340926a3d24c487e2d5d62e309b0c594`＋GitHub blob API `Accept: application/vnd.github.raw+json` GET200/5338262bytes真实恢复`SUP_LIMIX_REPORT_BLOB_20261025.bin`（内容PDF）。系统默认无pdftotext/pypdf，用已配置workspace Python/pypdf只读检索，不安装依赖/写提取副本。

旧PDF共61页，第一页自标2025-11-10、arxiv2509.03505v2/Nov7，已有2M及benchmark排名；第4页§2.1给two-layer MLP数值嵌入，是原report机制上下文，不据此断言2M采用同一MLP。首次检索含LimiX2M通用词导致大量结果页文本输出截断，**没有把那些表的输出当已审2025研究/当前证据**；随后只以RaBEL/RBF/radial/exponent/rank-collapse定点术语与§2机制判原报告是否已披露同一新增数学/模块，不分析其余结果或跨日候选。保旧PDF为同家族首公开/去重原证，不补跑2025日报/原score/旧Book链。

## 本文可能独立的新差额（尚待首次事件校准，不预正式分母）

不能沿用R33最初“RBF tokenizer＋SNF是Jun04新发布”的宽说法。新arXiv论文事件仍在Jun04，其潜在独立增量应收窄到可检查的新解释/边界，而不是同名模型和既有代码发布：

1. §3/A Prop3.1共享affine scalar且无positional信号的输入rank≤2、纯attention rank≤2/MH≤H+1；B1针对**pre-LN** feature内跨样本居中rank≤1，feature-only additive offset被取消。ID能区分列，不扩大这种value variation。LN后可在二维affine支集变化，B2只第一层同feature sample attention的每输出Jacobian≤2H，堆叠上界≤2HN且不超过列数N的自然上界，不称全模型低秩/线性本征维/任务能力定理；不能把数值点云rank等同单scalar流形维。后续非线性/residual/跨feature mixing不在同一无条件界。
2. §4.2新文写quantile初始化center/局部bandwidth可学、soft exponent bin与两个positive shared scalar缩center/width；**与早公开代码的hard decimal exponent/逐kernel amplitude gamma-beta不一致**。只能采用论文提出的数学分支，不能说旧artifact实现/验证了它，也不能把前后不同gate下的benchmark强归新公式。Finite bins/自由learned bin embedding亦不自动给严格scale equivariance；原代码数据归一化/guard细节不全，不补部署recipe。
3. §4.3 SNF排序已早公开；这次文字把它与readout消费/attention pooling连成解释，结构存在可达路径不等每个attention计算对prediction有非零贡献/不可删。§5.5文本SNF又写SFN/括号术语混乱，保精确§4.3的S→N→F，不补统一实现。DAG热图相关不证因果邻居/一般图结构发现。

T5同2M/SNF训练仅替tokenizer的shallow数值rank58.41→78.62、rank@99 13.94→25.35等是具体有限诊断，不直接得语义保真/压缩/速度保证。T1 SVD r192→50 AUC.9177→.9143、r20 .8985/r5 .7674保退化，低rank可容忍不等无害或模型所有宽度冗余。T2若干任务MLP/Periodic仍更好，不采普胜；T6 BCCOREG2M6.52差于TabPFNv2 6.39、TabArenaREG AutoGluon3.46优于2M4.54，反对“全部第二/全面压ensemble”。C1 64/16/20、Optuna100、15seed用于baseline规则，foundation称full dataset但完整episode/model train预算/精确preprocess拟合人口未全，不当总训练费公平已证。C6只900sample×60feature synthetic classification、EPYC9354/RTX4090、三run均值，GPU171.40 vs352.60ms、CPU17257.34 vs51950.08ms不是实际服务SLO；precision/ensemble/cache/完整length/memory时点不全。C4新TabPFN2.5只是post-release targeted sanity，不假定全11suite/同seed覆盖。

## 当前停点与下一次独核精确问题

实际补充的精确术语检索结果：旧PDF对RaBEL、RBF、radial、exponent、rank collapse、sample-attention、feature-attention均为0命中。这只说明这些原字符串未命中，受断词/旧命名限制，不冒全文语义无同机制证明；采用的是旧代码已正面展示RBF/smf与新文数学/门控不同的具名对照。当前README实际V3通过，限定diff --check及新记录no-index空白核无诊断；机械不代事件/贡献语义校准。

PF-CBM R81–82已实际完整读回，唯一actualPOST生效/newI17＋旧Kimi1合18，Report/本人注/Source仅行政同步，旧pending按真实I转整合后实际V3通过，不第三技术。04485仅有首次必要材料/早公开定点恢复及**待校准的收窄事件差额**；尚未正式评分、未加候选行、无Books/PRE/注/I，不将普通事件判定冒日期外阻或终态隔离。

请本日独立reader一次定点判断：旧release/原report/实现已披露到哪层；新Jun04论文的B1/B2解释与不同soft/shared-gate定义是否提供独立足够贡献，或只是既有机制重述而应本窗排除。不能因模型早weights就自动否定论文新分析，也不能因新arXiv日期就重新收旧release。若准入新差额，再只对该命题评分/actual owner最小稿；若已有有效同事件则具名复用，保本次原证与原R33层不相关的其他结果。

此有限恢复到足够提问/差额已停止，不再查全2025/全repo历史/镜像。actual Ch12输入接口宽度/非线性生成/维度读数完整组已作候选owner读入，但不据“能映owner”先收，尚未定最终NC/融合。最后本项判定、有限官方title stop与完整六节/DAY仍ordinary；不等其他日期，不预日完、不动State/index、未stage/commit/push。本bounded作者阶段保存后交root/reader释放槽，非暂停本日。
