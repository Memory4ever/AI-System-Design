# arXiv：2026-10-14 Daily 的日期与有界发现

目标仅为北京时间 **2026-10-13** 完整自然日。检查于2026-10-14；不把 Submitted 日期或搜索收录时间当作公开日，不处理10-14公告批次。

## 实际入口与停止

打开各分类官方 `recent?skip=0&show=2000` 的日期导航，而不是把宽列表送入逐项审阅：

| 分类 | 实际可见日期边界 | 本次处理 |
| --- | --- | --- |
| [cs.CL](https://arxiv.org/list/cs.CL/recent?skip=0&show=2000) | Wed14 → Mon12 → Fri9 | 无Tue13批次；在日期导航停止 |
| [cs.LG](https://arxiv.org/list/cs.LG/recent?skip=0&show=2000) | Wed14 → Mon12 → Fri9；首页含完整Wed14段 | 无Tue13批次；没有翻到更旧尾页 |
| [cs.DC](https://arxiv.org/list/cs.DC/recent?skip=0&show=2000) | Wed14 → Mon12 → Fri9 | 无Tue13批次；在日期导航停止 |
| [cs.AI](https://arxiv.org/list/cs.AI/recent?skip=0&show=2000) | Wed14 → Mon12 → Fri9 | 无Tue13批次；在日期导航停止 |
| [cs.CV](https://arxiv.org/list/cs.CV/recent?skip=0&show=2000) | Wed14 → Mon12 → Fri9 | 无Tue13批次；在日期导航停止 |
| [cs.RO](https://arxiv.org/list/cs.RO/recent?skip=0&show=2000) | Wed14 → Mon12 → Fri9 | 无Tue13批次；在日期导航停止 |
| [cs.AR](https://arxiv.org/list/cs.AR/recent?skip=0&show=2000) | Wed14 → Mon12 → Fri9 | 无Tue13批次；在日期导航停止 |
| [cs.PL](https://arxiv.org/list/cs.PL/recent?skip=0&show=2000) | Wed14 → Mon12 → Fri9 | 无Tue13批次；在日期导航停止 |
| [cs.IR](https://arxiv.org/list/cs.IR/recent?skip=0&show=2000) | Wed14 → Mon12 → Fri9 | 无Tue13批次；在日期导航停止 |
| [cs.MA](https://arxiv.org/list/cs.MA/recent?skip=0&show=2000) | Wed14 → Mon12 → Fri9 | 无Tue13批次；在日期导航停止 |
| [cs.OS](https://arxiv.org/list/cs.OS/recent?skip=0&show=2000) | Web提取缓存停在Thu8 | 不以旧缓存授零命中；补开[当天new](https://arxiv.org/list/cs.OS/new)，为Wed14的5项，新/交叉/修订均标14 |
| [cs.PF](https://arxiv.org/list/cs.PF/recent?skip=0&show=2000) | Web提取缓存停在Mon12 | 不以旧缓存授零命中；补开[当天new](https://arxiv.org/list/cs.PF/new)，为Wed14的23项，不转作13日队列 |

[arXiv官方发布说明](https://info.arxiv.org/help/availability.html#on-deferred-mailings)的2026假期表列有美国周一10-12；其常规公告在美国晚间，对应北京时间翌日。列表实际缺Tue13、下一段Wed14与延期相符。这里采用实际公告日期边界，不由Submitted日期反推公开日；不声称排除作者站点或其他平台在13日提前公开正文的可能。

## 有界主题补检与日期反例

辅助Web检索三组，均限定 `site.arxiv.org "13 Oct 2026"`：

1. `large language / Transformer / mixture of experts / KV cache`；
2. `world model / vision-language / diffusion / agent`；
3. `distributed training / GPU / serving / compiler`。

这些是发现查询，不是官方公开日证明；返回混入旧论文、收录日期、镜像与站外噪声，不支持全主题召回。另开 `cs.CL/pastweek?show=2000` 与 `cs.LG/pastweek?show=2000`，日期导航仍为14→12，没有13日段；`catchup/2026-10-13`返回Internal Error，不以它证明无研究。

具体易混项：[AlignPred，2610.17970](https://arxiv.org/abs/2610.17970) 摘要页写Submitted13、v1提交13，镜像也显示13。但官方[cs.LG列表](https://arxiv.org/list/cs.LG/recent?skip=0&show=2000)将它列在 **Wed14** 段第571项；故不放入本次13日分母，不评分、不提前读正文写Books。标题与完整摘要显示其研究persistent KV的误差约束编码与CPU重建成本，属于后续真实公告日可筛线索，不以窗外为“无贡献”。

搜索返回HorizonNav/2610.13849、RARA/2610.13578及Price of Precision/2610.15629，其搜索日期并非13日公告证明，不纳入本窗；不为这些窗外线索建立逐篇深审队列。招聘、课程表、硬件价格、旧论文趋势榜和转载不支持技术证据。

## 本窗结论与限制

本次 **确认的13日arXiv公告候选0**；不是“把当天所有论文读完后0贡献”，也不是“互联网13日绝无论文”。没有通过准入的本窗arXiv家族，因而没有相应评分、Evidence或Books采用。已穷尽上述可用日期入口；OS/PF旧缓存及catchup故障隔离，不授它们正面覆盖保证。只有恢复的官方13日公告段，或明确13日首公开的作者正文及身份依据，才定点重开本窗；不改已处理其他日报。
