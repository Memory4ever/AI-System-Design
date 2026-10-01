# 04/22 2604.18724v1 独立定点审计

审阅者：root，非本日日报作者。2026-09-28 重新打开[官方身份页](https://arxiv.org/abs/2604.18724)和[精确 v1 正文](https://arxiv.org/html/2604.18724v1)，对读当前 `PLATFORM-EVALUATION-SYSTEM` Ch66 的分布、重复样本、原始 generation 与聚合证据段。此审计只裁决单家族，不签全日日级 Gate。

旧 04/21 `screening-ledger-final.tsv` 曾把该家族泛化前关闭；这不能证明 V3 准入正确。v1 §5 把多个输出的 token 路径合为 graph、保留原始输出；§6.2 的配对研究中 graph 对相对多样性判断优于 list（平均准确率差 +0.12，95% CI 0.03～0.21，n=36），但 list 对单分布细节与细粒度两分布比较分别更好（graph 差 -0.057、-0.10）。这是“概览压缩改变人工检验任务”的受限证据，值得以 `Design Delta 2 + System Reach 1 + Durability 2 = 5` 标准审阅；并非 graph 总体更准或任何发布 Gate 已验证。§8 的实验室界面、样本量增大形成 hairball、混合界面未受控比较与未部署限制保留。

Books Decision：`Weekly/Daily Only`。Ch66 已规定按分布与重复样本保存原始 generation/trajectory，不让聚合值替代原始 evidence；具体 token-graph UI 是该已立论点的一个受限呈现选择，尚不足以新增长期机制正文或让可视化取得 scorer authority。若后续独立评价显示某种界面改变真实发布判断的可靠性，定点重开 owner 差异，而非凭主题相似永久排除。

日期只作有界归属判断：arXiv 身份页 v1 submitted `2026-04-20T18:22:31Z`，v2 submitted `2026-04-22T18:21:57Z`；本地本窗官方批次/连续身份 receipt 另含 v1 metadata updated `2026-04-22T00:04:21Z`、DataCite created `2026-04-22T01:59:54Z`。后者已晚于本窗北京时间 09:00 截点，只能是滞后的身份记录，绝不能用于证明落窗；metadata updated 也不是单独的首次公开证明。v2 不能倒置 v1 owner；须与官方 announcement slot 合用，若日级终核不能确认 04/22 08:00–09:00 北京时间公开区间，则保留 Date Hold，不据提交日偷偷归于 04/21。未发现仅靠 revision 编号即可重开 v2 的机制/纠错信号。本次独立核同意恢复本日工作候选及窄 Only，反对将旧前关闭标签或一个元数据字段当最后 Gate。
