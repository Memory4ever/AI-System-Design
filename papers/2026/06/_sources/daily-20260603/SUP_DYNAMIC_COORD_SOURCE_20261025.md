# 00804：策略映射的局部负证据，不是通用路由定律

仅06-03补Jun02。当前AGENTS/Research与Report合同/Prompt、Sources每日/arXiv/恢复、ROADMAP及本日停点已重读；R62完整v1题摘/Jun02联合日证有效复用。[当前官方abs](https://arxiv.org/abs/2606.00804)显示Jun04 v2，未见撤回/勘误信号；[精确v1](https://arxiv.org/html/2606.00804v1)此次实际读§3–7完整方法/主评价/直接反侧、§8结论与§A具名失败说明，以及§B统计单位和§C failure-code定义；不逐行审所有重复案例/附录大表、代码、法律实体正确性或复现实验。访问2026-10-25 BJT，不采用v2或为版本号比较旧新。

## 必要支持与不支持

30 curated enterprise任务＝6行业×5类，四strategy（单Agent/consensus/debate/synthesis）×3重复×4model arms共1440outputs；预注册只有Qwen/Sonnet/Gemma三臂，OpenAI是后加auxiliary。不是1440独立任务，不能把同一task三个重复作为额外任务召回。主要judge是Sonnet，且亦是generator；具体完整model revision、agent数量/每strategy提示和迭代次数、相同token/API预算、精度/硬件/完整长度、费用/端到端SLO未充分披露，Not Disclosed，不补默认值。

§3–4原strict winner/CI假说不成立：只有Qwen PC3的预测策略相对最佳其他策略CI正，优势.025仍低于预设.10。Task×rep为paired unit，重采样/置换seed20260527、5000次；同task重复/同family model相关性尚限制普遍推断。后来采用post-hoc绝对差≤.10的near-best读法，在Sonnet judge观察矩阵中成立，不等预先校准的线上非劣界，更不证明动态router胜过任一固定策略的equal-cost系统。文中并未实现并评测完整learned/router控制器；成本/判类误差也不在质量均值里。

§5 PC4所有四model下单Agent均值最高，人工制定/模型judge的failure编码把62条显著落后协调输出都标citation-overreach；这是其rubric下的输出差异，不独立认证真实法规/义务或聚合是唯一因果。PC2表的debate在四臂都不是exact-best，后提“adversarial→debate、balanced→consensus/synthesis”并未由子类新受控试验直接证成，不能照录为部署规则。H2 KendallW按15个model×class配对，均值差近零/区间跨零；语言与行业共同改变，不授越南语与英语无真实差异，也不从raw spread推ranking一致。

§7另有480个rep1 outputs第二GPT5.1judge，r=.40只是有限一致性；作者把相关低说成calibration offset而非random disagreement没有充分桥（常数平移本身不改变Pearson相关）。更重要：该节明说near-best为13/15、两个PC4miss，并给OpenAI aux单Agent排序翻转，§8却称在独立judge每个pair皆within .10，两者冲突。保明确表/13of15反侧，不采“near-best对所有judge稳定/所有arm单Agent最佳”等扩大headline。所需重开仅作者纠正此表述/匹配judge分层的完整原始结果；现证据足收窄，不为未知扩全代码/网页。局部负证据本身未被这条矛盾消除，不用删整篇或降分规避。

## 正式拟分与actual Books比较

2+1+2=5：D2为固定任务类映射的失效边界/协调伤害局部反证；Reach1限协调策略选择与结果判据，不借六行业或四模型加到全生命周期；Durability2为可复用策略校准问题。纠正原强策略映射和拟长期判断，已深入受影响域；不是把后验near-best宣传当高分，也不因NC降低分数。

唯一`AGENT-MULTI-AGENT` / Ch82。实际完整读“先建立单Agent Baseline”的同源相关错误/总费/单Agent+verifier与parallel-tools对照段，以及“扩展Agent数量之前先测Coordination Tax”末架构测量清单与task-topology matching完整交接，另读“多Agent拓扑必须先通过Equal-budget Pareto Admission”完整两段和“Delegation应由任务状态与不确定性触发”完整router权衡段。Ch81 workflow与Ch83协议的节点分工沿当前ROADMAP有效，不把策略实验塞进协议owner。

现正文明确要求实际任务切片的协调净收益/预算与错误放大验证，保单Agent/确定性验证/较小workflow、router误判和选择偏差；没有把某任务类别固定映射为必胜策略。拟长期命题“类型标签不够证明最佳拓扑，局部协调可反退，选择须保单Agent与equal-budget回退”已被这些具体段落完整承载。本文未支持一个可新增的通用routing-law，具体.10后验容差/行业排序只是Report局部证据。因此提案具体已有覆盖，不是事件duplicate/主题相近；保原准入、5分、全部正反侧，不为例子/论文名再造正文/Review note。

首次必要/拟分/actual owner具体NC尚待唯一独核，未写Books/Report或预NC生效/DAY。新增结论、共享Book零改动与来源/全日完成分别判断。
