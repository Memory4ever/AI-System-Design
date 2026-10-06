# 本20补03/19：第二批四份完整题摘与日期筛选

resume_mar17。有限既有主题查询的具名相关题名，不扩分类/全附件。四篇exact-v1官方abs完整AB、Comments/history及当前可见说明实际已读；只有题摘潜力，不授Source/Evidence/Books。所有数字未采用。

## 三份拟入选（待非作者准入校准）

- [Beyond Muon: MUD (MomentUm Decorrelation) for Faster Transformer Training](https://arxiv.org/abs/2603.17970v1)：Muon极分解多矩阵乘成本→三角 whitening/Gram–Schmidt/Gauss–Seidel 式动量去相关→重新比较每步进度与optimizer开销的time-to-quality取舍。不是把成熟orthogonality原则重新评分；AB新增替代更新及受限稳定性。拟2+2+2=6，必要审阅再核row-orthonormal固定点/局部收敛与真实训练控制，不采用protein应用作为额外贡献。v1唯一，无当前撤回纠错说明。
- [Efficient Training-Free Multi-Token Prediction via Embedding-Space Probing](https://arxiv.org/abs/2603.17942v1)：需要训练/独立draft的MTP成本→mask embedding探测候选并构造topK speculative tree/prune/parallel target verify→改变无额外训练条件下proposal/verification预算选择。拟2+2+2=6；保目标分布/验证接口及全费用待必要原证，不因AB数值授加速或无损。reader实际current-v2 Comments发现具体变化：实验由tok/s替换为相对AR speedup ratio，§3.1 mask初始化及§4 ablation改进；原作者“只有history/未见重要说明”的记录窄纠，不影响具体准入。必要源采用速度/初始化/消融时只定点核受影响v2内容并分清v1，不全版本diff；后续不能把当前AB改动当本日v1保证。
- [Only relative ranks matter in weight-clustered large language models](https://arxiv.org/abs/2603.17917v1)：weight clustering通常强调centroid精确值→固定assignment后改变centroids/统计的控制与跨层scale drift反侧→需要区别rank保存和跨层尺度一致性，不把“rank-only”当通用定律。拟2+1+2=5，对局部表示压缩设计边界，必要对照待核。v1唯一，无当前撤回纠错说明。

三篇公开日夹证沿首批已核官方ID不预发/常规公告与exactDOI登记上界：Submitted03/18分别17:37:31Z、17:14:01Z、16:55:13Z只作发现，最早可能03/19 BJT08；官方DataCite exactDOI真实HTTP200 created/registered分别03/19T02:44:55/56Z、02:44:13/14Z、02:43:37/38Z，日级上下界均03/19自然日。不补造精确公告08时，不把Submitted/Updated当firstpublic。Node fetch一次失败，curl同exact API恢复，不留必要日期访问阻塞。API链接形式为`https://api.datacite.org/dois/10.48550/arXiv.2603.<ID>`。

## CARE17946：先公开同稿信号（待独校，不计本日候选）

[CARE exact-v1](https://arxiv.org/abs/2603.17946v1)完整AB新增activation covariance factorization/非uniform rank预算/KV-parity GQA→MLA，潜力明确；accepted ICLR2026本身不作firstpublic。DataCite created/registered03/19T02:44:19Z只授arXiv本日事件。

定点触发同稿[OpenReview DVurf4kGag](https://openreview.net/forum?id=DVurf4kGag)：官方search作者条目的可读原始结果（https://openreview.net/search?content=authors&group=all&sort=cdate%3Adesc&source=forum&term=~Zhenyu_Zhang4）明确本题名/同9作者、Published26Jan2026、LastModified30Apr、ICLR2026Poster、ReadersEveryone。官方现PDF索引与ICLR proceedings完整AB同题名/同作者/三步核心身份已核；不是拿第三方‘8months’当日期。forum/PDF/attachment当前challenge，api2 exactnote真实403 ChallengeRequired；并不否定官方公开search的窗前公开身份。此记录可支持至少01/26已公开同family的日期上界，具体更早首日未确定，不授精确最早公开日。未见本次arXiv有重要修订贡献说明，因此拟不重收本日firstpaper/不评分，不展开旧稿全文或差异。

原search出现他人论文仅为身份字段定位，未作为新发现；如独核认为公开索引不能确定当时正文权限，则只隔离本family首公开，不假贡献EX。新证据指本次实质修订才定点恢复受影响内容，现不遍全部ICLR。
