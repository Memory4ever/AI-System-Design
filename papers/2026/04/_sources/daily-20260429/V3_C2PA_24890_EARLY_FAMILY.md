# 2604.24890v1 C2PA 白皮书：同家族早公开的有界日期／贡献核

本核仅为 2026-04-29 Daily 的作者侧逆向查漏，不把 arXiv v1 页所写 `27 Apr`、ePrint 的 `received` 或文件落库时间单独当作首公开；不重读全部技术论文与后来版本。目标身份为 [arXiv exact-v1](https://arxiv.org/html/2604.24890v1)，题为 *Verifying Provenance of Digital Media: Why the C2PA Specifications Fall Short*。它在 Executive Summary 明说自己是同团队详细研究 [ePrint 2026/804](https://eprint.iacr.org/2026/804) 的非技术摘要，正文反复将发现和修复建议归于该 study。

早于本窗的可直接观察公开内容是 [UMBC Cyber Defense Lab 的 2026-02-20 公开讲座页面](https://cisa.umbc.edu/verifying-provenance-of-digital-media-security-analysis-of-c2pa-and-its-implementation/)；[UMBC 公共活动流](https://my3.my.umbc.edu/groups/cybersecurity?mobile=off)将同题讲座公告列为 **2026-02-15 17:17** 发布。讲座页不只列同家族题名、作者与日期：公开摘要已逐项写出 C2PA 2.2 规格／验证器／Pixel 10／RFC3161 形式分析、签名与可信时间戳不达一致、同一对象多时间戳、验证器不一致、证书撤销、排除范围及签名防篡改≠内容真实性等核心结果和边界，并提供录影入口。这里据**官方公共公告＋公开摘要文本**确认核心研究贡献已于本窗前可见；不声称本轮验证了录影的实际发布时间或每一技术细节。ePrint 页面所列 `2026-04-23: received` 只说明投稿接收日，不能独证当日可公开获取；即使不用这个字段，UMBC 页面已构成独立早公开链。

arXiv 白皮书可见的 2.3／2.4 与 Pixel 10 Pro 更新是一种受限状态更新：其 §Conclusion／Recommendations 称 2.3 纳入部分建议、2.4 尚未解决其担忧；没有识别出新攻击机制、改变证明责任或独立评价实验，不能把已公开核心研究换题为本窗新贡献。安全层面的有效事实仍应保留：签名保护 claim 的部分断言，不等于真实性；时间戳绑定、证书撤销、验证器一致性与排除范围属于独立保证。原白皮书关于所有版本和产品的广泛结论是作者主张，不沿本摘要推断所有实现都可被同一方式实际攻破。

**本日处置：** `new_in_window=No`（同家族核心公开摘要最迟在 02/15 官方讲座公告可见；本篇为其摘要性白皮书），从原「贡献潜在安全纠错」移入第三项**已证早公开隔离**。无需为本日按 9 分法评分、Books Decision 或逐段重演详细论文；真正首次公开应由更早日期另行归属。106 份已读完整题摘工作账由 `62 潜在＋42 贡献前闭＋2 早公开隔离` 改为 `61＋42＋3`，非正式冻结当窗候选分母。若发现白皮书有独立于上述研究的本窗新中央保证／受控反证，按具体段落重开，不反向取消既有安全证据。
