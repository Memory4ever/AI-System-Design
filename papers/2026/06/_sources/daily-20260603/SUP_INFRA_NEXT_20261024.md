# Jun03 两项 Infra 必要审阅与有限入口恢复 — 2026-10-24

仅Jun02 BJT补查；root为本记录作者及共享Books writer，独立复核者为jun03_next_reader。旧27家族/旧日期评分和有效层不动。已重读AGENTS、当前研究/Report/来源/Prompt/ROADMAP及Books三文件。两个完整v1题摘/history/DC原字段来自[既存六份原件](./SUP_MODEL_OFFICIAL_EXTRA_AB_20261023.json)，独核R1b/c已确认准入及日期；不重做有效元数据GET。01502唯一v1 May31 23:53:24Z、arxiv.content/findable/registered Jun02 04:17:03Z；00601 v1 May30 07:58:02Z、同client/state/registered Jun02 03:55:22Z。适用日程最早Jun02 00Z与最晚界均在Jun02 BJT，不将字段改名实际公告。没有已见撤回/纠错信号，不声称全历史无改动。

## 01502 Move the Query — 必要Source与窄PRE

[exact-v1](https://arxiv.org/html/2606.01502v1)，实际读§2.1–2.3、§3的setup/数值/位置条件、§4成本式/拟合条件、§5.1–5.4及Figure4的holder容量边界。路由query不是本文新发明；新增是MLA/稀疏粒度下route/fetch/local的probe、transfer、holder compute、return、merge代价反转条件。语义fetch含位置适配/拼接，而splice-free bytes-back只是transport baseline，不能混成完全等价服务；小query-batch的host固定费用可让bytes-back更快，wire节省不签端到端赢。散选保canonical位置，不能照连续块做重定位；浮点误差核验也不是任意上下文KV可复用证明。

作者主硬件H100 SXM5/NDR200、2node×4PE、NVSHMEM26.3/IBGDA，legacy driver且无GDS；200timed/50warmup CUDA-events。MLA bf16 query576、partial512及fp32 max/denominator，M_q 1～4096；holder热点/stream/compute饱和须计。更多A40/A100/RTX Pro6000仅intranodefabric anchors，不是跨节点全硬件复验。约7%MAPE只amortized M_q≥512运输拟合，不是全服务误差或SLO。TTFT host、网络与完整model生成不同口径；未复现/核实现，不采用具体通用speedup。

评分2+2+2=6，跨worker执行原语及可复用成本条件；实际缺口按研究合同深入。唯一owner INFER-DYNAMO/Ch52，实际读distributed handoff→Hetis完整组→slice transfer，及Ch51/53职责；现有worker/head placement与传输完成未拥有每块route/fetch/local predicate。建议在Hetis完整body与其独立source marker之后、下方slice transfer标题之前插一段，不拆旧组。

拟正文：

```markdown
分派到哪个worker之后，还可按已验证可复用的远端KV块选择“搬cache、送query到holder后合并partial、或本地重算”。压缩query与稀疏块会改变两端字节比，但[受限跨实例测量](https://arxiv.org/html/2606.01502v1#S4)显示，选择还须共同结算probe、传输、holder计算、返回和online-softmax合并；host固定费用可吞掉小batch的wire优势，热门holder又会饱和。连续重定位的语义fetch须付位置适配/拼接，原位置上的稀疏选择则不能照搬这一操作；bytes-back微基准也不等已完成可消费KV。布局/位置、partial统计与数值一致性先验收，再按当前fabric和形状校准成本；profiling、索引、merge、网络与故障恢复全计费。校准失效、热点或共享资格不成立时，保留同驻、完整迁移或重算，不由较小query批准任意KV复用、总延迟或生产SLO。<!-- source-family:SF-2026-ARXIV-2606-01502 -->
```

完整上侧是Ch52以“跨worker分工还可发生在同一个Decode内部”开头的Hetis整段，加独立 `<!-- source-family:SF-2025-ARXIV-2509-08309 -->`；完整下侧为 `### 从静态 Striping 到声明式 Slice Transfer` 及其以“链路稳定、故障显式且数据对象较大时”开头的完整首段。本人注只记本篇范围/score/独核事实，未实存前不授POST。

## 00601 ScanWeaver — 必要Source与窄PRE

[exact-v1](https://arxiv.org/html/2606.00601v1)，实际读§3 affine pair/式3–8、§4–5 lowering、§6.1–6.7及§9。原语是已知仿射组合与Blelloch，不授新scan数学；新增compiler把recurrence→pair→schedule→GPU launch/shared memory作为可换schedule的表示边界。当前仅Blelloch；streaming/hybrid未来，不把当前MLIR checker称自己运行。数学结合不证明逐步float的bitwise equality，bounded与exponential参数下数值压力不同。

matched local forward recurrence与完整Mamba融合projection/gating不同；后者只structural context、非同kernel等价基准。稳态计时排编译/进程启动/加载/CUDA init，不是全费。仅single-node affine，缺完整reset/gating、backward/分布式路径；硬件型号、dtype、具体B/D与完整SLO在拟采用必要段Not Disclosed，因此不采用0.032/0.469/51.7ms为可迁移性能。额外workgroup中间态、barrier、artifact/编译费必须计，未核代码/复现。

评分2+1+2=5，单compiler局部结构与稳定适用边界；实际知识差额深入必要域。唯一owner INFER-TENSORRT-LLM/Ch49的执行表示/scan降低，而非把Ch22重复写成新模型表达力。已读Ch49 attention monoid完整两段及其IO-aware后继，Ch48/50职责和Ch22 selective SSM完整相关段；现有scan数学与成本未讲recurrence compiler IR/兼容子集与fused比较。拟插在attention-scan成本完整段后、IO-aware tile分支完整首段前：

```markdown
把依赖改写为scan的思路也能成为编译接口，而不为每一种递推手写kernel：对已知input生成的仿射transition，先规范成可组合的状态对，再选择树形schedule，降低为共享内存、barrier与显式GPU launch。[受限编译分支](https://arxiv.org/html/2606.00601v1#S4)只实现Blelloch与局部forward子集；实数结合不保证逐步浮点轨迹相同，指数参数放大的误差也须与lowering错误分开。完整Mamba的projection/gating融合并非相同算子，不能由顺序reference的倍率宣布替代生产kernel。规范化、编译/加载、workspace、同步及数值回归全计费，稳态launch不抵全生命周期成本；非仿射/reset语义、精度或短shape不合时，保留顺序reference、已验融合kernel与原执行路径，模型状态语义仍由[Ch22](../part-02-model/22-long-context.md)拥有。<!-- source-family:SF-2026-ARXIV-2606-00601 -->
```

完整上侧为“Scan 需要额外 workspace、状态读写与数值稳定处理…”整段；完整下侧为“这个 IO-aware 原则在 tile-based accelerator 上会出现另一条分支…”整段。未动Book，待独核必要Source/owner/PRE后root实际写。

## 官方模型补检的有限恢复（不授Coverage）

本轮只补旧API429后未闭的官方入口，不重抓已有效题摘。实际尝试advanced标题language model、submitted May29～Jun02有限发现查询：web cache miss、直接GET400，无结果表；不能当零命中。另官方月list cs.CL/2606首25为404，cs.AI同入口cache miss，不能推目标日零发布。

随后实际打开[官方Advanced表单](https://arxiv.org/search/advanced)核公开字段：advanced=1、classification-computer_science=y、date-date_type可选submitted_date_first或announced_date_first；公告只支持年月，不伪造日级公告筛选。按观测字段改为May29～Jun01 submitted_date_first、title四OR（language model/LLM/transformer/diffusion）、size200后GET仍400；未取得total/entries/分页，本次查询无有效执行，亦未说明原因。原API与DataCite已有效结果不受此失败否定；不循环重试、不用catchup90天代历史。这个失败不代其余普通贡献/证据/Books工作已完成。

## 七个MODEL日期保留项：本轮有限原始入口补查（2026-10-24）

本节仅恢复00024/00079/00093/00160/00003/00132/00091既有日期层，不重读技术Methods、不扩窗或新增评分。原最早公告界至registered跨日的组合仍有效地说明“尚不能限定Jun02”，不是否定arxiv.content/findable合法组合；先前API/advanced失败及停止保留，不再循环同一失败请求。

实际作两批精确身份/题名搜索：`"2606.00024" "ART"`、`"BitsMoE" "May" 2026`、`"2606.00093" "Agreement"`、`"2606.00132"`；随后`"2606.00160" DataShield`、`"2606.00003" "Learning from Mistakes"`、`"2606.00091" DLLM-JEPA`及FoLoRA精确题名/June。结果不是官方日公告分页，不作全来源Coverage依据。SciRate、papers.cool、HF、ScienceOpen等显示June2/May24/Mar25等不同口径，只作身份线索；不把抓取、submitted或索引更新日改成首次公开，也不采用第三方对论文机制的解释。

- **00024 ART**：[作者publication](https://guozhong-li.github.io/publications/)实际定位到该精确ID与标题，但只给2026，没有Jun02首次发布声明；既存v1为Apr15提交，不能从后来June编号/第三方列表消除跨日。00079 **BitsMoE**：[第一作者主页](https://zjiayu064.github.io/home/)当前news写“May/2026…available on arXiv”，是需要保留的更早公开信号，不能拿Jun02登记直接压过它；当前页只到月份且无当期存档，不能据此补造某一May日或静默重排旧候选。原v1May22/后版Sep27题名差异不用于技术采用或全版本比较。
- **00160 DataShield**：[作者代码README](https://github.com/ZJunBo/DataShield)核到精确题名/引用与脚本，但所读README没有目标Jun02首次公开声明。代码可见不等论文在当日首次公开，未以当前README的存在倒推历史发布；未遍历全部commit。
- **00003 Learning from Mistakes**：[作者project](https://lab-rococo-sapienza.github.io/LearningfromMistakes/)实际可读同题研究/visualizer/论文链接，未取得可限定Jun02的原始公开日期。搜索中的AAAI workshop/Mar25标签不是已核全球首次正文日期，不用正式发表倒移原报告。
- **00132 FoLoRA**：[当前官方abs](https://arxiv.org/abs/2606.00132)核到v1May28 21:22:31UTC、v2Sep29改题名；这仍是提交记录，不能补成公开。**00091 DLLM-JEPA** [官方abs](https://arxiv.org/abs/2606.00091)显示May24提交；**00093 Agreement Metrics** [官方abs](https://arxiv.org/abs/2606.00093)显示May25 v1、Jul31 v2。三者当前页面未给可替代目标日公告的精确首公开声明；未把当前v2摘要/技术结论写入Jun02。

上述补查没有取得足以把七项跨日区间收窄到Jun02的原始日期，也没有证明这些论文必不在Jun02。保留全部既有题摘与潜贡献，不打零分、不排除贡献、不进确定当窗候选或Books。可接受定点恢复材料是当期官方公告/列表中该ID的记录、带可靠公开日期的作者原文/历史快照，或明确首次发布/纠错声明；00079还须消歧作者May公开信号。来源材料到达只重开各项日期层，不重扫全年。当前本节是有界恢复原件与判断准备，仍待本日独立reader核对这些有限停止和隔离资格；不自行宣称七项已终态，更不让它们遮蔽其余普通发现/审阅/Books工作。

## Agent/Multi五个跨日资格项：有限原入口恢复

root仅接00189/00135/00152/00094/00096日期缺层。原题摘/潜贡献与跨日区间保留，不先全Methods。精确题名搜索两小批（Practical Agentic Systems＋May/June、PrivacyPeek、Diversity Over Frequency＋June、MIND全题；随后Tool-calling全题＋Amazon/Jun02和前两题的作者/project线索），没有取得官方日公告；搜索结果只作恢复入口，不作新日级Coverage。

- **00189**：实际打开[当前官方页](https://arxiv.org/abs/2606.00189)、[Cohen原publication页](https://wwcohen.github.io/pubs-s.html)、[共同作者publication](https://jerryyan123.github.io/publications/)与[作者代码入口](https://github.com/wwcohen/secretagent)。原页v1May29 16:02:26Z是提交；作者目录只给2026/in progress或under review，当前同名链接也可能随后续工作变动，未取到Jun02首次发布原声明。当前代码可见不是当期论文首公开证，未扩全部commit/课程内容。
- **00135**：[当前官方页](https://arxiv.org/abs/2606.00135)仍只有v1May28 22:21:47Z、后版Aug10等版本口径；官方页无具名project。有限精确题名/作者机构日期搜索没有取得可用作者发布日期，第三方Jun02标签与另一索引May28互异，均不能消解跨日，不把搜索无果当未发布。
- **00152**：从已见官方摘要进入[作者PrivacyPeek README](https://github.com/Xuan269/PrivacyPeek-Resource)，所读页面未含可限定Jun02的首次公开日期；原v1May29 04:55:12Z提交和第三方May29“released”不改称公开日。只核身份/日期，不采用当前benchmark方法或运行任何隐私探测。
- **00094**：[作者MIND project](https://xddgit.github.io/MIND/)只给Research project2026/ECCV2026，当前还有journal/one-step后续说明，未据此回填v1或Jun02首发。第三方May25/Jun09分别可能采用提交/收录口径，不采为原证。
- **00096**：实际打开[当前官方页](https://arxiv.org/abs/2606.00096)及[作者project](https://scaffolded-exploration.github.io/)，ICML2026/引用只到年份，仍不能由May25提交或Jun02 v2提交确认首次公开。未以project当前的技术表格替历史日期或把v2号码当重要当窗事件。

这些具名原入口仍未收窄原跨日区间；没有证明不在Jun02，也不支持候选/评分/Books、零命中或完整Coverage。停止重复相同API/搜索，不追所有假想渠道；定点重开需当期官方精确ID公告、作者带可靠日历的首发原文/历史快照或对应明确纠错。保留原始题摘与潜贡献，只隔离必要日期，不作贡献排除。这是本轮有限恢复事实，仍待独立核其停止/资格边界；当前其他ordinary研究不归零，不冒全日完成。

