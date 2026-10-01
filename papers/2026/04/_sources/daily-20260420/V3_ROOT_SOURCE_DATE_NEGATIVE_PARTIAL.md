# 04/20 来源、日期与准入负侧：非作者有限复核

复核者：root；日报作者：apr20_resume。2026-09-28。本文件只记录本轮实际独立核到的边界，**不是整日 Gate 签字**，不替代其余八项单篇同行审阅或最后的自包含报告检查。

## 来源与窗口

核对正式日报 §2 的 14 个每日 Source ID 与注册表每日段，未把 Weekly 来源强加给本窗。重开 [arXiv 公告规则](https://info.arxiv.org/help/availability.html)：最终 ID 在公告过程赋予，正常 Thursday–Friday 投稿在 Sunday 20:00 Eastern 公告；2026-04-19 为夏令时，正常槽对应 04/20 08:00 北京，位于 `[04/19 09:00,04/20 09:00)`。延期仍可能发生，Submitted、Updated、OAI datestamp 和 DOI-created 无一项能单独证明逐篇首次公开。作者保存的 15314～16299 本批、前后 ID 边界与 OAI 同日/后改分层只支持有限批次推断；15483、AgentWorld 继续具名隔离，不用这条批次规则把其身份问题抹平。

独立重开 [Meta Publications 第 2 页](https://ai.meta.com/results/?content_types%5B0%5D=publication&page=2)，其有序近期段为 May 19/17/12/06/04 → Apr 16/14/09，并混有旧推荐；可以支持**所见日期段**跨窗，不支持 Research 全站、所有 release 均为零。重开 [Kimi Platform Blog](https://platform.kimi.com/blog)，目前可读页确有旧文章，不能据其 2025 最新可见项宣布 2026 全站无研究。MiMo 首页正文日期/卡片顺序仅复用作者有界记录，本次网页文本读取未独立取得可靠 04/22 原始时刻，不把它升级为首次公开证书。上述限制与 §2 的 OpenAI Research、Google Publications、Meta Research 三个具名 `受阻` 相容；它们允许隔离不可得历史目录，不允许改写为全面零命中。

## 贡献筛选正反控制

负侧定点重开 [2604.15482v1](https://arxiv.org/html/2604.15482v1) 的摘要/§2–3：论文确实将 target removal、邻域误拒与 adversarial prefilling 组合成训练目标，并非“与模型无关”；但本轮没有看到可将它的 QA 统一、anchor 和双向 top-k 蒸馏，从现有 Ch72 的删除对象、retain/恢复攻击及发布验收分账中提升为新的通用系统结论。作者前分母关闭仅作为受限方法组合判断维持，不能说多目标 unlearning 不重要。再核 [2604.15484v1](https://arxiv.org/html/2604.15484v1) §7 与 Ch76 hybrid 检索论证：同模型/不同 corpus 的局部 hybrid 结果与 BEIR 不同 encoder、预处理的 pipeline 比较不能隔离 adaptive fusion 的普遍收益；仅凭本文不改已有 lexical+dense/fusion 与 reader 分责。两项都是**有界样本**，不代表 40 项排除全部通过。

正侧对照重开 [2604.15549v1](https://arxiv.org/html/2604.15549v1) 与 Ch36：有向 mixing、broadcast 冲突时隙及收敛所需轮数共同形成受限拓扑选择，原“非大模型/无系统状态”前关闭不成立；正式日报 5 分标准、仅报告的狭义处理合理，不把半双工无线代理成本外推为 GPU fabric 加速。再核 [2604.15871v1](https://arxiv.org/html/2604.15871v1) 的 source/target/instruction 三元编辑身份：它是比较 reconstruction 与 instruction 编辑的具体协议增量，不是仅增榜单；受限数据集与蒸馏 judge 未证明跨范式普遍公平。正式日报 5 分标准、仅报告仍是可辩护的窄结论。两项日期仍依上方批次组合及作者具名字段，非逐篇公开日志。

## 剩余 Gate

本轮来源抽核、两个负例和两个正例没有重新访问全部 14 个入口，也没有审签 109 个候选的 Evidence/Books。作者已保存的 150 份题摘、109/40/1 工作分母及 26 项写后核可供最后核对；仍须收齐八项具名同行结果，核对应的正文/评分/Books 决定，抽查其余高风险排除层，并检查正式报告是否仍准确隔离三个历史目录与日期例外。未完成前保持 `进行中`。
