# 12/09 两项定点恢复

记录时间：2026-10-02T19:01:02+08:00。这是作者补证，不替代非作者对 metadata/§6 的判断。

## Seed：论文与 Blog 两类原始目录

已实际读取官方 `https://seed.bytedance.com/api/get_article_list_v2?article_type=1&count=20&order_desc=true&publish_year=2025` 与 `article_type=2` 同参数入口，请求头 `x-tt-locale: US`。两次 HTTP 200，`BaseResp.StatusCode=0`。paper 实际返回18条、total94、has_more=true、next_page_token=20；Blog 实际18条、total45、has_more=true、next_page_token=20。停止第一页，未遍历94/45条库存。

逐项查看返回日期而非假定 pinned 排序：paper 的本窗邻接为 Seedance1.5pro（ID1323，PublishDate=1765728000000，2025-12-15T00:00:00+08:00）→GR-RL（ID875，1764604800000，12/02T00:00+08）；其他返回论文的日期自10/22向前。本页无12/08–09条目。

Blog pinned 顺序：SeedProver1.5（2141，1766505600000，12/24T00:00+08）→Seed1.8（1815，1765987200000，12/18T00:00+08）→Seedance（1817，1765882058000，12/16T18:47:38+08）→GR-RL（1504，1764604800000，12/02T00:00+08）→DepthAnything3（1953，1764172800000，11/27T00:00+08）；其余实际返回 Blog 为10/23至6/25。本窗邻接12/16→12/02，两类都已检查。

只支持所示官方目录段，不支持整个机构零事件；PublishDate 的午夜精度不自动证明相关论文首次公开。撤销 Seed“2025历史目录无法恢复”的过宽外部隔离，保留未显示内容覆盖边界。

## Pink Slime：旧公开论文与 arXiv v1 关系

身份：[2512.05331v1](https://arxiv.org/html/2512.05331v1)；[ACL Anthology 2025.ranlp-1.128](https://aclanthology.org/2025.ranlp-1.128/)；[出版 PDF](https://aclanthology.org/2025.ranlp-1.128.pdf)。出版页为 September 2025、1109–1117页；PDF首部是 RANLP September8–10,2025。题目、作者、完整摘要对应。出版月不提供精确 first-public 时刻，也不证明旧 Daily 已审阅。

已定点比较出版PDF与精确v1的§3数据/划分、Tables2/3、§6攻击及§6.1/6.2重放：40k抽样、9473 PS/10000 LN、cluster80/20与三次运行一致；BERT89.31/89.05、RF78.57/79.86及GPT4omini48.15/ClaudeHaiku49.55对应；定向改写条件、学习率缩为1/100、原PS50%重放与混合数据公式一致。控制/非控制改写结果及限制对应。当前官方事件页只列v1，未观察到影响本判断的勘误/撤回或独立修订声明。

改写使检测失效的反证没有被删除；但所查两份正文未发现12月归档新增的具体机制、评价或纠错。按已公开论文的后续归档关闭本次事件，不以提交日或搜索收录日重新计为首次研究。只在出现精确实质差异/修订声明时重开该家族，不扩扫RANLP全池。

作者侧两项普通补核已执行；§6仍由非作者决定是否关闭，不自行改为通过。
