# 2604.24801v1：04/27 完整作者 PDF 早公开，04/29 不重复收录

先前[第一批完整题摘逆向准入](./V3_REVERSE_TITLE_ABSTRACT_BATCH1.md)把《Architecture Determines Observability in Transformers》恢复为 04/29 潜在，是对贡献的判断，不是 first-public 证明。本轮打开[官方 arXiv exact-v1](https://arxiv.org/html/2604.24801v1) §2–5、§7 与作者直接链接的[官方仓库 `v3.3.0` release](https://github.com/tmcarmichael/nn-observability/releases/tag/v3.3.0)，为日期消歧只读必要论文首页/关键段和 release 事件。未展开全附件、未复现实验。

## 身份与公开事件

[GitHub release API 原始事件](https://api.github.com/repos/tmcarmichael/nn-observability/releases/tags/v3.3.0) 给 `published_at=2026-04-27T02:15:28Z`（北京 **04/27 10:15:28**，在本日 `[04/28 09,04/29 09)` 之前），附属 `adot-202604-v3.3.0.pdf` 的 `created_at=2026-04-27T02:14:32Z`、`updated_at=02:14:33Z`、约 1 MB。release body 明说本版改摘要/正文，**没有实验结果变化**，并附完整 PDF；这不是仓库创建时间、commit 时间或 DOI 代理的孤证。实际只读打开该[作者发布的 PDF](https://github.com/tmcarmichael/nn-observability/releases/download/v3.3.0/adot-202604-v3.3.0.pdf)，31 页首页标题、作者、摘要和核心数值与 arXiv v1 相同。两份 PDF 均 31 页，抽取正文总长 `115351` 与 `115462` 字符，文本相似度约 `0.9993`；这只是身份/重要修订消歧，不当作实验复现或排版逐字相同证明。arXiv v1 §Reproducibility 自己亦写对应 tag `v3.3.0`。04/29 arXiv 公告因此是**同一完整正文的后续发布平台**，没有本窗重要新修订信号；本论文的首公开至少早至 04/27 release，04/29 不计首次候选。GitHub release 的 `published_at` 与确实可取的完整 asset 联合证明公开事件，而非单用 asset `created_at`。

## 保留的有效技术证据与排除边界

贡献初筛仍可能成立于真实 04/27 归属日：定义为冻结模型中 mid-layer 线性 probe 对逐 token loss 的可读性，在 max-softmax confidence 与 activation norm 控制后用 partial Spearman 测量，再以 final-layer MLP 的预测作额外 output control。13 模型中 confidence 吸收原 probe 信号平均 `57.7%`；Pythia 同一训练家族的 `(24 layers,16 heads)` 三个配置点约 `0.10`，其他六个配置 `0.21–0.38`，checkpoint 轨迹呈训练后擦除，说明内部风险传感器可用性不能由“有 hidden states 可读取”自动推出。但 Pythia 同 recipe 仍有参数、学习率/batch 等随规模变化；跨 Qwen/Llama/Mistral 是观察性，不证明可仅改 layer/head 因果修复。定点反证更强：§5 Table 8 在 20% flag rate 的独占 catch 对 GPT-2 随机 ranker 基线仅 `14.4%` 对 `13.0%`，不能把“10.9–13.4% all errors”写成纯净增益；TruthfulQA 的**流畅且高置信错误**子集，probe AUC `0.499/0.568/0.556` 近随机。它只支持该种 per-token loss 传感器的受限可观测性，不证明事实真值、内部自知、纠错、实际 release gate 或跨模型通用阈值。

若在正确归属日审 Books，实际 [Ch66 风险传感器段](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)已写 hidden-state probe/外部证据权责，却未明确「训练/架构会擦掉原本可探测的信息」这一前置监测可行性 Gate；这可以由该日另作 source→owner/独立核，**不是 04/29 的共享 Books 授权**。本日只保留身份、贡献与早公开反证，不评分、不列 04/29 候选、不改 Ch66。

账目：同一 106 篇已读完整题摘中，此项从此前潜在 63 移至已证早公开日期隔离。04/29 作者**工作态**改为 `62 潜在+42 贡献前闭+2 已证早公开隔离`（另一项为 25779），仍非冻结来源/正式候选分母，也未获非作者整日 Gate。04/27 是否已有此家族由 04/27 owner 依据其实际窗口/来源决定；本日不改他日文件。
