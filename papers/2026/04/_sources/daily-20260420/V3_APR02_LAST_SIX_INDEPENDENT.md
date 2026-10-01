# Apr20 最后六项有限非作者处置复核

复核者：apr02（非本日报作者）；2026-09-28。重新读当前 AGENTS、研究/Report 合同与统一入口。本次只核六项 exact-v1 的拟采用机制、关键评价/反证及相邻知识职责，不核整日来源/日期，不复现实验，不写 Books。以下通过仅指具名受限处置，不等于日报 Gate。

## 15648 HyperGVL — 6 分标准，仅报告：通过，需保持编码边界

实际读 [official v1](https://arxiv.org/html/2604.15648v1) §2.3–2.4、§3.1–3.5、§4/Limitations。2,400 个 meta problem 的 35 种表示产生 84,000 个样本，不是 84,000 独立问题；WiseHyGR 以 HO-Neigh 问题与已测最佳表示标签训练，8:2 划分，另测 1,000 题/任务。受限表示选择证据值得保留，不因是图任务直接拒绝；没有证明任意任务、编码或规划迁移。**“pairwise 都丢 higher-order”须收窄**：裸 V–V 邻接未保超边身份时可损失关系，但 §2.4 的 Clique Expansion 明确保留 hyperedge IDs，V–E pairwise 本身也可保高阶关系。保留实际表示比较，不把名称类别变信息损失定理。12 个 VLM 与异架构 LM/VLM比较不构成纯模态因果。当前 Ch66 对象/输入协议身份主线可消费此边界，但本 benchmark/router 未要求新的长期正文分支；6 分标准 Only 成立。

## 15657 CovAgent — 5 分标准，仅报告：通过

实际读 [official v1](https://arxiv.org/html/2604.15657v1) III–V（含 V-C/D/E）。相同 GPT-5.2、temperature .4、19 RTL design、三 runs；结构工具/反馈/上下文同时改变，不能从组合对照分离各组件因果。覆盖不足需区分方法上限与可解推理难题，是具体有效性边界；classification/排除表需人工审核，不授权自动 waiver。复杂设计仍失败，mini 也有退步。V-C 百分比与 38/35 counts 不补造共同分母，token计数也不能代全执行成本。Ch66 benchmark subject 与 scorer authority 已承载一般职责，本受限 RTL 诊断证据可报告，不把整个 pipeline 签 Existing 或写成普遍覆盖保证。

## 15794 SDFT recovery — 5 分标准，仅报告：通过

实际读 [official v1](https://arxiv.org/html/2604.15794v1) §3.2、§5.1–5.4/§6。历史/任务 teacher 与受损 student、off-policy bootstrap 后再自蒸馏是明确条件路径；Qwen2.5 3B/7B、NF4/10% FFN pruning 不能外推所有恢复。Table4 best MMLU 仍较未剪模型低 2.55pp，teacher选择存在任务 trade-off；Table6 base teacher CKA 更高却 expert teacher accuracy 更高，不可把相似度单调当性能或必要因果。训练新增预算与恢复/适配分开，科学 QA只作论文已测证据，不重开 AI for Science研究。当前 Ch29 teacher/target及行为分布主线未被这受限 recipe 推翻；标准 Only，不采用 manifold 必然恢复理论，不新增 Books。

## 15802 CHOP — 5 分标准，仅报告：通过

实际读 [official v1](https://arxiv.org/html/2604.15802v1) §2.1–2.2 Eqs1–4、§3/Tables1–2。相邻 chunks 的 LLM continuity 判断决定继承 CNM 或重新抽取，prefix作为 embedding 输入，区别于单纯固定 chunk；同 retrieval stack 保留有限比较。Top1 hit .9077 对 .8128，但生成 F1 .2760 对 .2763，Top10 F1 .4080 对 .4072，不能用召回改善证明答案质量普遍提升。Gemma12B、embedding3-large、Chroma与手册重构条件保留，prefix/CD未独立消融，全成本未证。实际 Ch76 chunking/information boundary 和 retrieval→reader 分工一般原则可解释它，但不宣称精确算法已完全覆盖；局部实现和反收益标准 Only，不强增 Books。

## 15871 UniEditBench — 5 分标准，仅报告：通过

实际读 [official v1](https://arxiv.org/html/2604.15871v1) §3.2–3.4、§4.1–4.4/Tables3–4/Limitations。710=633 image+77 video 的 triplet协议、蒸馏 judge支持受限比较，不把评分维度命名“orthogonal”当统计独立证明。Teacher-MSE不是外部真值，8B stroke .32 对 .31 的退步保留；50人“五组无重叠”与“五完整passes”文字不清不能自行补分母。Train/test隔离未说明，不据缺说明断言泄漏；BF16与建议显存有披露，latency hardware/batch等未绑定不能补造公平性能结论。Ch66 per-verifier/aggregation/authority 实际原则已明确，但此次新协议只作受限报告，不签整个实现 Existing，不采所有编辑范式公平保证。

## 15972 WORC — 5 分标准，仅报告：通过

实际读 [official v1](https://arxiv.org/html/2604.15972v1) III/Alg1、IV-A/C/E/F与TablesI/IV/IX。swarm标签→meta weight→低权重 quota提供局部分配证据，不是 derivative/因果 weak-link定位；Alg1重复采样与上游上下文有依赖。TableIV 82.2/80/80.9是同额外讨论范围的局部比较，不能当 token/总成本匹配；TableIX cost单位未绑定、混合 accuracy/F1平均及79.7→81.7与主表不同。额外算量不免费，judge人类一致不等真实贡献。实际 Ch82 边际信息价值、预算成本和 equal-budget回退已承载一般设计，不因局部quota新公式自动新增章内机制；标准 Only，不采用普遍弱链定律。

## 交付边界

六项受限 Only 均通过；15648 唯一措辞提醒是编码保真不能由“pairwise”名称判断。全部未新写书稿、未评整日日级 Gate。版本身份按所列 v1 URL绑定，未遍历无关附件或 revision史。
