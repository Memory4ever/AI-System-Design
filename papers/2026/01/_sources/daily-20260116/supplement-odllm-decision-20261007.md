# 01-16 / OD-LLM 借用算子与局部费用—质量校准

最终独立结果：root完整读此包并实际exact-v1 blocks24–34/49–71/86–93/101–110、actualCh49 83–115/1387–1430；新局部stored-size匹配/质量运行分离准入成立，1+2+2=5标准OnlyReport PASS。保留A40/batch1 vs tenprompt、CPU/dtype/backend不足，不授端侧/能耗/新operator。后文等待提案仅保留过程，不是当前普通待办；未核实现/复现，非日级Gate。

撤回原“熟悉组合即可前关”提案；等待root独立准入/必要原证/owner处置。不写Books。完整abs09306与exact-v1 html09306 blocks18–71/73–110已实际读。公告normalcohort Jan15下界＋exactDOI registeredJan15T02:42:59Z公共存在上界条件限定Jan15，非注册=首公开；当前abs/core无直接作者project更早论文发布信号，不因会议年归属。当前没有直接撤回/勘误信号，未核实现或复现。

§3.2.2 blocks24–34明说LC-Rec为basis：RQ-VAE/Sinkhorn index、explicit/implicit index语言IT均借用。§3.3是activation Gram XXᵀ Cholesky whitening，不修改tokenizer/词表；§3.4/3.5 display[48]指bib.bib68（Wang等2024 SVD-LLM，arxiv2403.07378），WS SVD/inverse factors与progressive只更新左factor承接已有压缩原则。未见新rank分配/配准算子；decorrelation≠independence、PSD不总可invert Cholesky，作者字面不授普适数学保证，不采用完整proof recipe。

实际增量候选不是借用算子，而是§4.5/4.7的新局部cost/quality对照：GPTQ4bit group128/per-channel/act-order、SparseGPT75%Linear sparsity、OD有效参数近似，以stored model size匹配；同256校准、beam/maxlen/数据split与单GPU配置。§4.1.4单A40、seq200、evaluation batch1、beam20；§4.7 ten-prompts称one batch，timesGPU17/12/5s、CPU700/620/200s，CPU身份、dtype/backend、输出长度/内部batch执行和tailSLO未披露。并非固定参数size证明内存峰值一致，也不是实际mobile/on-device部署证据；不授能耗或实时本地隐私保证。

Table3 Instruments/Games GPTQ多指标更好，OD的Arts更高；§4.5总体“GPTQ略好”不覆盖所有dataset。Table2对未压LC-Rec Games HR@5 .0876→.0838下降。§4.3 plain SVD→whitening→progressive对照只支持受限recipe，不证明新operator。§4.4 ratio.2–.8与§4.6 64–1024 calibration测试明确关闭progressive，不与完整OD更新结果混同；更大校准收集费用增加、极强压缩质量下降。§4.7只ten-prompts作者秒数，单A40并非consumer硬件，缺方差/重复、不知kernel质量与CPU配置，不能通用外推3.5x。

准入拟“低比特/稀疏size近似匹配并不等相同推荐质量与执行成本 → 同一受限协议不同压缩路径出现质量/计时分离 → 按consumer与执行artifact核压缩而非只存储bytes”。拟1+2+2=5标准，仅局部报告：新增证据比原框架/算子名称有意义，但不足改变Ch49既有artifact/质量/成本回归合同；不声称本篇同实现Existing。actual Ch49:83–115已有source-to-source/数值与workload commit、backend依赖/bytes不能代性能（Hoare本日新增仍待POST）；另已实际读1387–1430完整SVDQuant→FLRQ→activation补偿→whitening/SVD分层rank→正交字典→动态rank邻接，正文已明确共同bytes预算≠任务损失、校准/额外kernel计费、静态compression≠完整serving收益。本篇未新增该长期合同或具体新operator，保留局部对照不写书。此标准判断不因recommender领域名关闭，也不将熟悉组合当新机制；不扩过去LCRec/SVDLLM全原文。
