# 2604.22879v1：跨域 Sidecar 的受限机制与隐私保证隔离

固定窗口 `[2026-04-27 09:00, 2026-04-28 09:00) +08:00`。本页继[早段作者准入](./V3_EARLY_FOUR_EXACT_V1_TRIAGE.md)，定点重开[官方 exact-v1](https://arxiv.org/html/2604.22879v1) §4.1–4.8、§5.1–5.3 与 §6，并对读 [Ch72 多 Agent 来源→sink policy 正文](../../../../../books/part-06-ai-infrastructure/72-security.md)。日期仍须本窗公告组合独立核；此页不是冻结候选、评分或 Books 采用。

现有 Ch72 已有跨委派 source/delegation/memory→不可逆 sink 的 provenance 重建和确定性授权。本文确实提出一个不同于中央汇总图的**组织数据边界实现**：各域 sidecar 独占局部 graph，跨域 token 携 `src_id/taint/constraint/signature` 而非原图，sink 前由源 sidecar 对其私有图回答 policy predicate；这把全局语义重建拆成带签名来源引用、远端谓词可用性和本地 effect 前授权。若组织间原图不可汇聚，这是一条可采用的窄系统分支；但其成立依赖实体映射、token/provenance 完整、sidecar 诚实/可用、policy 编码与查询/撤销 epoch，不能把语义 taint 判别当权限本身。

主要证据来自 PhantomEcosystem 200 个合成情境（160 attack/40 legitimate），Python/gRPC/NetworkX/Redis sidecar、单 A100；§5 Table 5 的 `.93` precision/`.96` recall 只支持该机会集和实体 mapper，不能推跨企业真实 incident rate。§4.8.4 Theorem 4.6 用计算型 ZK 模拟性质直接推 `I(G;View)≤H(b)≤1 bit` 的 Shannon mutual-information 界；这一步缺信息论等价证明，data-processing inequality 不能直接套在仅“计算不可区分”的两个 view 上。即便单次只返回 boolean，§6 自承认自适应多次 predicate 查询可通过交集泄露更多，故 1 bit 更不能当整个会话保证。ZKP/TEE/HE 分支只按各自已实现/测量范围报告；§4.8.1 的 circuit setup/proof generation 另有显著成本，不能用普通 boolean query 时延代表加密模式。

作者侧建议：保留**跨域图不汇总时的源域谓词查询和 sink 前授权**为贡献线索，安全命题触发深入必要审阅；将上述无条件 Shannon 上界与任何“隐私零泄露”整体采用明确隔离，未获独立数理复核前不把它写作 Books 保证。若最后仅能证明该 sidecar 只是 Ch72 既有 provenance→effect 分层的受限实现、没有新的长期跨域状态/失效责任，可转 Only/具体前分母关闭；若有增量，Ch72 是唯一主 owner，Ch66 仅 handoff 评测。需 root 的非作者贡献/争议裁决和日期有界确认后才评分或请求 Ch72 锁。
