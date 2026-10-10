# 单篇必要审阅/actual owner 提案

作者supp_jan15；3项决定准入均经root实际窄core确认，未授Books写锁或日级。日期原字段在[47 DOI](./increment-dates47-20261007.jsonl)：08731 registered Jan14T02:58:17Z、08816 Jan14T03:00:21Z、08682 Jan14T02:57:04Z，配合正常announcement/正式ID规则限定BJT Jan14，不把Submitted或注册单独当first-public。原文项目轻量信号见[identity](./increment-three-identity-20261007.txt)，未见更早dated完整论文；Cago无直接项目body链接，Dialogue匿名数据无独立dated稿链接，不全网追史。

必要原件：[决定事实](./increment-j15narrowfacts-20261007.txt)、[核心评价](./increment-three-eval-20261007.txt)、[核心与反侧](./increment-three-precise-20261007.txt)、[完整必要补段](./increment-three-finish-20261007.txt)。三篇不同对象，不能按同一实验模板推断。

## 08682 Lessons from the Field — 2+1+2=5 标准完成；root Evidence/已有覆盖 Ch74通过

实际§3、§4.1–4.2/Tables1–2、§5.1–5.2/Table4与Limitations：固定内部100 transcripts、core prompt内容不变而仅改special tokens，Llama3.3-70B→gpt-oss120B的accuracy/readability与completeness取舍改变；higher reasoning Med继续退步、High无关verbosity/重复。100对话/AutoEval三次重复是judge输出波动而非全部生成seed；Claude3.7验证于42人工/synthetic paired examples与4×50 transcript human A/B，只支持此内部构念。50摘要component labels可调prompt，50对话ASR13.4%WER/Whisper5%相对WER与下游preference29→53只是该pipeline观察，不授单原因/普遍40%因果。没有公开数据精细身份，hardware/precision/batch/concurrency/SLO Not Disclosed，未复现。

actual AGENT-PROMPT Ch74:16–26明确效果依赖model/tokenizer/chat-template/context/decoding；109–122的prompt_id/version+model/template+eval cohort与改一词也需offline regression/canary/rollback已具体承载迁移条件，87–92另区分CoT解释与可验证intermediate state。新内部反证不改这些长期选择，拟NoChange—Existing，不因新case名加书；报告保局部重现实验条件，非通用不可迁移定理。

## 08816 MemRec — 2+1+2=5 标准必要审阅完成；root Evidence及actual已有覆盖 Ch77通过

实际§2.1 Eq5–6、§3.1–3.5/Tables1–4、§6：即时user/item与curated immediate-neighbor memories一起batch更新，独立LM_Mem异步维护后供reader，O(1)仅调用数，token/write与stale-read/并发/隐私无保证。gpt4omini双角色、k16/Nf7、candidateN10，四推荐split与1000user研究子集、H@K/NDCG。Books消融关闭write H@1 .527→.505但H@5 .803→.814，静态curation规则与immediate-neighbor反侧保留，不能说所有rank K更强或多hop成立。estimated sequential latency/Pareto和不同backbone/config没有匹配整写读生命周期，local部署不是privacy proof；hardware/precision/batch/concurrency/SLO Not Disclosed。必要成本A/C已补足并经root验收，未读无关附录或复现。

actual AGENT-MEMORY Ch77:389明确实体/邻域是未来检索作用域与provenance/派生关系权限；409–420已有consolidation/crossrecord merge、异步维护的算力隐藏条件、active/inactive维护读写与stale退路；383/379–381已有冻结reader/constructor分工及全写读成本分账。root实际363–427完整邻接已通过具体Existing，不用主题同名作证，不写Books。

必要A.3/A.5/C/D.3补足见[cost actual](./increment-j15costactual-20261007.txt)和[tail](./increment-j15costtail-20261007.txt)：本地memory LM是A5000 24GB、vLLM FP16/temp0；云端主实验硬件/precision/batch/concurrency/SLO Not Disclosed。1800 context budget/k16/Nf7，item截断memory/user最近三item代理不是完全用户信息。Table5 Standard16.5s/9.7ktokens、Ceiling10.4s/9.7k、Local-Qwen34s/7k是sequential黑箱API/local实验，作者明确opaque cloud routing/network可能造成大model更快，不授模型本征速度。D.3 Books1k Standard的R3200/ReRank2000/W4500token=9700确含异步write，修正前提“不匹配全写读”仅指比较未匹配model/backbone/资源与queue/stale/commit成本，不能误称W全没统计。A.5只是2025年12月定价估计，local marginal含amortization/electricity，不是免费；Local variants的reader仍4o-mini，不能授全链on-prem/privacy。8.1k输入/1.6k输出不保证以后价格Pareto。root必要core及A.3/A.5/C/D.3和Ch77具体Existing通过。

## 08731 Cago — 2+1+2=5；WorldModel支持域具体 gap 深入完成，Ch25实际POST通过

已读§3.1–3.3/Alg1–2/Theorem1、§4主/5seed消融及AppD：L2/imageMSE访问计数定位demo中已掌握最远step并采附近subgoal，Go-policy从示教初态尝试到达、到达或timeout后BC-explorer延伸，真实replay训练Dreamer/RSSM，imagined训练goal policy；reset仅demo初始seed不是任意内部状态。Theorem依赖每时BC occupancy接近κ、BC分布model误差μ、完整imagined-vs-expert trajectory TVν，所得imagined model error μ+2κ+2ν；访问阈值/最终goal奖励不证明三假设成立，return界是借用成熟结果不计新分。

11模拟tasks、10/20 demos、8训练seed/100held-out初态，共享demos/seed，goal sampling与BC Explore必要消融5seeds；相同Dreamer结构却配方/goal predictor等仍变，不采单一因果。limited demo/image64²与距离proxy、初态reset/真实机器人未证；theory代表性demo假设、goal terminal不等occupancy closeness。

必要F.4/G实际补足，原件见[increment-j15costactual](./increment-j15costactual-20261007.txt)：三任务20%缺观察/0.1动作噪声/20%随机动作，5seed/100评估/1Mstep，局部demo质量扰动可保持或改善成功率；失败demo30/50%实验仍用binary成功标签仅对成功稿训练goal predictor，不能外推未标注/全失败demo。附录声称“neither imitates”不采，因为§3.3实际BC Explorer依然存在；恢复/探索直接动作与goal政策不同。G的72–155h/1M–5M环境steps不授matched速度改善；逐step×对应demo长度×metric成本，state L2 .05h/72h，image MSE 2.8–14.2h/78–155h，不能把访问字典当免费。实际checklist compute-justification L925披露8 Nvidia A100、约2.4GB memory，未说明单run/各phase分配，precision/batch/concurrency/SLO Not Disclosed。G的100×100×3例子与核心64²描述不同，不统一成单精度分辨率保证。root深入必要PRE/POST通过；只采用采集支持域接口与条件，不证明κ/ν经验成立。

actual MULTIMODAL-WORLD-MODELS Ch25:88–104已持有真transition采样/逆prior/learning-progress代理，不含**demo capability-frontier决定真实采集支持域→BC Explore延伸→imagined政策不得越可靠支持**这条具体分支；340–380有rollout误差/课程但不同sampling对象。拟在探索数据admission相邻、latent几何之前仅单段说明demo frontier/BC延伸是收集分布，不让MSE访问计数签发TV或部署安全，初态reset/demo支持不可信回归普通真实replay/count/random或短rollout。已root PRE后窄写Ch25:104–106和自身末注1651，实际POST通过且锁释放。
