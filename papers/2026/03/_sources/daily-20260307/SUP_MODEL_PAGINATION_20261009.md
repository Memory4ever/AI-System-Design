# MODEL 同query余页（不扩日期/主题）

原MODEL total118/start0/max100不是终态外部阻断；root要求取得同query start100/max18，本轮实际成功18/18。原始[API](SUP_TOPIC_MODEL_P2.raw)、[回执](SUP_FETCH_modelpage2.json)，不扩query或月份。18完整标题已读，以下8相关/含糊材料再实际完整读exact-v1 title+abstract。公开日恢复：site:arxiv.org "6 Mar 2026" (2603.05357 OR2603.05369 OR2603.05432 OR2603.05433)、"6 March 2026" (2603.05488 OR2603.05495 OR2603.05507)无公告命中，仍P/A日期隔离，不评分/不Books。API current revision只作发现，05433v7 CRISP标题及current收益不回写到v1 OPSDC。

| 余页18的处置 | ID/title | 具体理由/证据 |
| --- | --- | --- |
| 新P；日期隔离 | [DiSCTT](https://arxiv.org/abs/2603.05357v1) | 共识作不确定性代理，high consensus pseudo-label SFT/low consensus consensus-regularized RL分支；共识不等truth。[完整v1](SUP_ABS_05357.txt) |
| 新P；日期隔离 | [Progressive Residual Warmup](https://arxiv.org/abs/2603.05369v1) | residual scalar随depth延后warmup，训练轨迹与直接启全层不同。[完整v1](SUP_ABS_05369.txt) |
| 新EX | [Exploration-Analysis-Disambiguation WSD](https://arxiv.org/abs/2603.05400v1) | rationale-rich SFT/CoT与neighbour-word组合完成WSD；小模型不是关闭原因，题摘未揭示一般形成机制或新的可归因成立条件，zero-shot大模型与task-FT比较不证明普遍效率。[完整v1](SUP_ABS_05400.txt) |
| 新P；日期隔离 | [Ensembling LMs with SMC](https://arxiv.org/abs/2603.05432v1) | locally normalized next-token mixture偏离string ensemble，byte-level共同character space SMC允许mismatched vocab，consistent仅limit。[完整v1](SUP_ABS_05432.txt) |
| 新P；日期隔离 | [On-Policy Self-Distillation for Reasoning Compression](https://arxiv.org/abs/2603.05433v1) | 同模型concise prompt teacher与student on-policy rollout的reverseKL，不需要gold并不证明压缩保真；current v7 CRISP修订不当新家族。[完整v1](SUP_ABS_05433.txt) |
| 新P；日期隔离 | [Reasoning Theater](https://arxiv.org/abs/2603.05488v1) | activation probe/forced answer/CoT monitor观察时刻差异，easy recall与multihop不同；不从belief可读推出无必要计算。[完整v1](SUP_ABS_05488.txt) |
| 新A；日期隔离 | [Cheap Thrills](https://arxiv.org/abs/2603.05495v1) | imperfect label warmstart把surrogate送入basin后self-supervised优化，有merit criterion理论，非因应用/小模型自动EX；一般训练成立边界与项目形成范围关系仍含糊。[完整v1](SUP_ABS_05495.txt) |
| 新A；日期隔离 | [Transformer-Based Inpainting for Real-Time 3D Streaming](https://arxiv.org/abs/2603.05507v1) | spatiotemporal embedding/adaptive patch的sparse-view质量与速度条件，可能特定应用改造而非新增形成机制；日期未过不补全文。[完整v1](SUP_ABS_05507.txt) |
| 原93重复，不重计 | 2603.05421 DARK currentv3、2603.05465 HALP v1、2603.05500 POET-X currentv2 | 现有exact-v1裁决复用；API current不回填v1机制/日期/评分 |
| 标题范围外，不扩AB/fulltext | 2603.20228 Compact Lifted Relaxations for Low-Rank Optimization | convex SDP bounds for rank-constrained mathematical optimisation，无model training机制/成立条件，不能由low-rank映射LoRA准入 |
| 标题范围外，不扩AB/fulltext | 2603.05391 SpiderCat、2603.05406 Optimal Morse Matching、2603.05579 Railcar Shunting HHRL、2603.05428 qLDPC Worm Decoding、2603.05441 MIMO Detection、2603.05464 Trapped-Ion Shuttling | 量子纠错/拓扑/铁路Q-learning/通信与量子设备优化的明确范围，不按数学/theory标签笼统关闭主线理论 |

本次实际exact-v1题摘总量从93增加到101：独立核验窄修后71P+18A=89日期隔离，1W后续撤回/日期隔离，10EX（05094 v2撤回/v3当前非withdraw信号已核）、1OUT。独立mar07_admission_review实际完整读新8题摘，5P/2A/1EX通过；同query余页18/18、前三处窄理由与两后续撤回信号确认，无未修点。此文件与原[93逐项裁决](SUP_ABSTRACT_ADMISSION_20261009.md)共同构成精确队列；未新增正式候选。四topic请求有限返回标题段已筛查，完整exact-v1 AB只核101个，不声称全部query家族完整AB均审读，不证明keyword以外全学科召回。
