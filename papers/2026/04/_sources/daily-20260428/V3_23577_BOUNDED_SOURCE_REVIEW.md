# 2604.23577v1 RouteNLP：失败路由日志反写模型组合的必要审阅

本页仅审[官方 exact-v1](https://arxiv.org/html/2604.23577v1) §3.1–3.3、§5.1–5.3、§6/Limitations 与当前 Ch56 的 cascade、pregen value estimation、routing calibration 邻段。是作者侧贡献/Books owner 提案，不是首次公开 Gate、非作者通过、已评分候选或生产复现。

## 有增量的唯一控制环

已有 Ch56 承载请求路由与后生成升级的累积成本、校准阈值、选择偏差和实际计费。但该章目前仍把候选模型能力当既定输入：失败/升级日志只更新 router 的估计与阈值。RouteNLP §3.3/Alg.1 把升级失败先按 task 在 router representation 中聚类，按 cluster size×质量差选高优先级，生成 frontier teacher 数据定向蒸馏便宜 tier，随后**重训 router 并重新校准每 tier 阈值**。这使模型版本/训练数据、路由策略与校准集组成同一个闭环版本；便宜模型能力改变后，不能沿旧 router 或旧 conformal threshold 验收。主 owner 若采用应在 Ch56 router feedback 主线补这一责任，Ch27/28 只 handoff 训练数据/更新合同，不把训练配方放到推理章。

关键对照不是整个三模块系统对静态路由的 headline，而是 §5.1 / Appendix G 在**相同蒸馏数据量**下 random selection 与 escalation-failure clustering：benchmark cost ratio 初始 `.203`，random distillation `.184`，targeted `.159`；这支持受测条件下针对失败簇选例可能有用，不证明任意预算总成本更低（聚类、teacher 生成、重训与校准本身成本未从该比率完整扣除）。§5.3 两类生成任务各 200 样本/三名专家，胜/平/负约 `8/65/27` 与 `11/65/24`；作者自己的估计有约 8–9% 查询实质退步，不能用平均 quality retention 隐藏。§3.2 的 conformal 覆盖仅 marginal 且依赖 calibration assumptions，不拥有逐请求正确性或跨漂移 guarantee。

论文 §6/Limitations 明确：8 周约 5k queries/day 的客户服务 pilot 是 shadow deployment，**没有 A/B**；真正 failure-cluster→distill→router co-optimization 在 benchmark 数据上，而非生产失败日志上运行。Pilot 的 58% 推理费用下降、91% 接受率及 P99 数字因此不能归因到定向蒸馏环；英文、单客户服务范围，其他 finance/legal 是 benchmark。分布漂移下 violation 可从目标 5% 到 8.1%。生产新增 OCR、多轮引用失败作者用升级而非蒸馏处理，也证明“所有失败都可训练便宜 tier”不成立。模型组合或价格更换时须 versioned fallback，不把校准自适应当硬 SLO/账单承诺。

作者侧建议保留潜在 `2+2+2=6` 深入 Books-gap 提案，待非作者核 exact-v1 与 Ch56 真缺口、组合公告日期和必要证据；不立即申请共享 Ch56 锁、也不把上述成本数字写成因果服务收益。如独立对读发现 Ch56 他处已明确失败日志→定向模型更新→router/阈值全重估，则具体 Existing；若仅三成熟组件拼接但无可验证闭环对照，则 Only。不得仅因闭环一词自动 Integrate。
