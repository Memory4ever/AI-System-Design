# 03/04 剩余有限研究（作者 mar02_v3）

root原六项作者身份及独立POST保持，mar02接手后新增项由root非作者审阅。固定窗口03/03 09:00→03/04 09:00 BJT。先前有界非作者结果见V3_NONAUTHOR_BOUNDED_REVIEW_MAR02.md，不用作者接手后的判断反授其独立完成。

## 已准备项

- 00811：必要exact-v1 §3.1/Table1、3.5、4.1–4.4、5–6完成，7分。实际Ch72筛选参与者段后两段及note，root必要源→实际正文/邻接POST通过。date range03/03T09:00～12:55:27+08；原Submitted02/28T21:14:01Z、arxiv.content/findable registered03/03T04:55:26Z。
- QwenCode v0.11.1：03/03T13:08:44Z release包含PR2021，7分。四core+tests exact diff实际读，实际Ch78 provider finish门槛后两段及note，root必要primary→实际正文/邻接POST通过。PR早期created/merge不伪称本窗首次。原代码身份及必要文件见先前非作者记录。
- 01499：必要§3–5.5、§6.1–6.4/Table1–2完成，7分；date range03/03T09:00～13:11:22+08。实际Ch72 private inference现段后两段及note窄写，root必要源→实际正文/邻接POST通过。Gaussian输入RMSNorm近似、RoPE block近似、static映射界与dynamic频率实验分账；不证明全形式定理，不采摘要通用隐私/质量数字。
- GPT5.3：后实际恢复[PDF](https://deploymentsafety.openai.com/gpt-5-3-instant/gpt-5-3-instant.pdf)封面March3、§3.1/Table1–2与Hub一致；先前非作者记录中的PDF访问失败是过程状态。RSS/landing/PDF March3 vs Hub PublishedMarch2仍有首公开冲突。新增动态/分母评价条件有潜在贡献，card暂不计候选/评分/Books，精确要求官方带时区first-public或March3实际重要修订diff；模型shipped2/26不是文章首发。release core未公开新机制，不把宣传数字计贡献。
- Gemini FlashLite：完整Blog core和card安全反证读足以裁决；datePublished03/03T16:34+00。本次贡献前关闭、不评分：继承thinking budget、架构参照Pro与有利价格/FPS不足新的机制/可行性边界；safety负项、grader/query改动不可跨card比较及manual复核是必要窄关范围，不授安全保证。

## root给出的有限题摘线索（不是冻结候选池）

全部使用live exact-v1完整题摘；具体符号/名称来自原文，不继承旧retained标签。

| ID | 实际判断与下一必要读点 |
| --- | --- |
| [00349](https://arxiv.org/abs/2603.00349v1) | officialv1是EmCoop，不是root提示COOP²，先纠正身份。cognitive/primitive双时钟与cooperation过程metric可能改变失败归因，可继续窄§5/7，不采用verificationrepair理由。 |
| [00381](https://arxiv.org/abs/2603.00381v1) | pinned predicate的proof-bound envelope入transcript与explicit residual covert channel预算/组合具体有贡献；只审采用predicate/残余界所需方法和反例，不能从empirical0证明无泄漏。 |
| [00468](https://arxiv.org/abs/2603.00468v1) | snapshot构造确定性RCA交互环境与process评价盲点可继续；先区分query静态快照与真实mutating cloud数字孪生能力。 |
| [00623](https://arxiv.org/abs/2603.00623v1) | 窄[§3.1–3.4](https://arxiv.org/html/2603.00623v1)消歧后拟贡献前关闭、不评分：Thought/Action/Observation格式、LLM长元素摘要及3agent报告属现有组合，未给新完整性/诊断可靠性条件；人评报告高分不把保序转为语义faithfulness保证。 |
| [00680](https://arxiv.org/abs/2603.00680v1) | 自管理memory的effectiveness信用不同普通external retrieval，可继续方法信用与局部反证；不按摘要倍率准入。 |
| [01162](https://arxiv.org/abs/2603.01162v1) | GRPO U-statistic、variance/group-size/oracle条件是具体优化理论，可继续核目标/假设，不采用universal group-size或实际clipped GRPO无条件最优。 |
| [01960](https://arxiv.org/abs/2603.01960v1) | 完整题摘后拟贡献前关闭、不评分：online softmax/tiled KV是成熟机制，cuTile可编辑和eager速度只局部实现；原文明确production fused仍更强，未给新的可比质量资源边界。 |
| [02075](https://arxiv.org/abs/2603.02075v1) | async sustainable throughput、shift检测memory-BO、joint placement/transition MILP与sample invalidate有具体联合状态增量，可继续必要§3–5与控制预算，不采倍数。 |
| [02176](https://arxiv.org/abs/2603.02176v1) | recursive tree索引/skill DAG可不是全新原理，但identicalskillset下DAGvsflat对照可支持编排的成立条件，可继续窄对照/执行语义，不因200k目录就授scale deployment。 |

早提交00063/00188/00195/00196只在确有具体贡献时核必要日期，尚非候选。00349提示身份错不扩成全库存重审；未读旧33或1270逐项抽象，也不把父任务题名替代原题摘。原00623、01960关闭建议已发root校准，得到具体反例才定点重开。

## 新增必要证据与实际 Books

- 01162，2+2+3=7：v1 §3.1–3.2对象是当前policy条件i.i.d.、LOO居中、未clip的score-function；fullmean需G/(G−1)rescale，不含rewardstd/旧样本IS/KL。§4.1/Prop3固定N=BG的prompt间异质性与同题高阶残差取舍，§4.2的PL/平滑/步长等假设及上界最优范围分开；§5.1小模型gradient比较、§5.2有限mathRL/五运行不授universalG。Ch33已有U-statistic段331–347主题承载，但未承载对象排除及预算分账，现实际336–338窄补两段+2233note，root实际POST通过。
- 00680，2+2+3=7：v1 §4.2 Eq4–5 gold-answer长度归一likelihood减完整前史baseline，§4.3 memorytokens独得局部+全局优势；§5.3–5.5同memory辅助reward消融与Limitations跨step状态不等价偏差实际核。scorer是π_theta，不编造独立冻结evaluator；不采摘要倍率、因果/事实保证。Ch77原144–148仅masked内容信用，现前加144–146 memory-likelihood替代分支+1677note；root实际POST通过。
- 00468，2+2+2=6，标准加受影响评价边界深入：§3.1–3.3将经过注入核验的真实故障冻结为有限工具response快照，非live mutating cloud；§4.2/Table4分开TCR结构完成、rootcause三元组正确与canonicalpath匹配，路径不是全部合法解。§4.4冗余与成功只是跨模型相关，§5.3明确不能评主动修复；不授DigitalTwin或冗余因果安全。已有覆盖拟用Ch66 367–371过程compliance/outcome分账、1373–1377 frozenAPI回放vsonlineauthority，root必要源/实际NoChange通过，不制造diff。

七项日期实际字段（2026-10-01查询）：DOI API `https://api.datacite.org/dois/10.48550/arXiv.<ID>`，均原机构client=arxiv.content、state=findable。registered UTC 03/03：00349=04:44:47、00381=04:45:30、00468=04:47:32、00680=04:52:24、01162=05:03:42、02075=05:24:40、02176=05:27:02。v1 Submitted UTC依次02/27T22:28:33、02/27T23:42:37、02/28T05:04:42、02/28T14:43:02、03/01T15:56:43、03/02T17:00:22、03/02T18:46:47；均在Fri14EST后至Mon14EST前。结合官方ID公告分配/无预分配与原机构findable登记上界、公告Monday20EST，公开区间下界统一03/03BJT09，上界registered+8小时+1秒，完全落窗；不把Submitted或DOI单独当公开正文时间。不主张排除提前作者公开；当前事件页无已识别纠错要求改变v1拟命题。

## 来源变化（有限当前段）

重新实际打开Kimi Research目录19项、2/09→4/20跨本窗至2024/06/26停止，有限可见列表已检查，不将旧platform受阻当2026研究永久gap。其他必要历史子入口精确限制保留，未经实际恢复不擅授全部Coverage。没有Weekly/Live或扩日，无stage/commit/push。

## 作者续跑收据（替代上述进行中的下一步，不抹去过程）

- 01162：root已实际读 §3.2/§4 Eq9、Ch33 336–338及邻接，必要源→实际POST通过。00680：root已实际读 §4 Eq5/9、§5.2–5.4、Ch77 144–146及邻接，必要源→实际POST通过。两处note已同步，不再待写后。
- 00381：实际必要 §2–4/Alg2/Assump4.1、§6/Table1–4、§7–9，2+2+3=7。Ch72 communication edge原身份/provenance不足覆盖合法选择隐蔽信号，实际652–654两段+note2976，root实际POST通过；残余MI前提、语义/tool/env选择、抽样assurance不同及decoder经验失败非零泄漏全部保留。
- 00349：exact-v1仍为EmCoop；DataCite当前COOP²为05/27 v2标题，不能用verification-repair理由历史准入。§3、§5双时钟/all-ready joint primitive barrier、§6–7两环境/二三Agent/拓扑混合与单例feedback实际读，2+2+2=6。Ch82原对话信息新颖性未覆盖双时钟/等待诊断，实际966–968两段+note1020，root实际POST通过。非完全异步/免费walltime/统一最优。
- 02075：§4 config/input/邻接负载观测失配→invalidate/EMA warmup、§5内存PoF搜索仍OOM、§6.6单切换缓冲/求解未完成继续旧配置、§8.3–8.7匹配控制/solver成本实际读，2+2+3=7。Ch27实际911–913两段+note1203，root实际POST通过；不采用§6.5 Eq18–19完整MILP保证，流守恒疑似约束相邻总parallelism解释需澄清，只隔离该保证，不用争议补全式子。
- 02176：§2.1 active树/TopK/dormant、§2.2检索pruning/run DAG layers/artifact/用户recipe reuse、§3artifact转换/pairwise judge、§4.1–4.2 oracle相同skill却额外Opus planner/更深图更多调用实际读，2+2+2=6。Ch84实际228–230两段+note1129，root实际POST通过；不授纯DAG同总预算优势、选择即执行合法或200k实际规模。

## 早提交潜在贡献的有限日期裁决

完整live exact-v1题摘：00063为dispositions/context独立operationalization，不只是benchmark平均；00188为CSS局部空间结构与TSG轨迹冗余的GUI-KV联合分支；00195真实摘要为SkillFortify静态分析/capability/依赖lockfile，API descriptions是comments污染，不采其为摘要；00196为Talaria client-CVM执行weight-independent、cloud执行weight-dependent的ReMO可逆mask。这里只确认潜在贡献，不提前评分或Books。

三项00063/00188/00196日期隔离：Submitted UTC分别02/10T12:59:41、02/27T01:27:20、02/27T06:37:07，原机构 arxiv.content/findable registered分别03/03T04:38:13、04:41:05、04:41:16Z。当前只能支持3月ID首次公告下界可能03/02BJT09与本窗上界，不能推出03/03BJT09。API Updated-v1 03/03T01:01:36/01:04:38/01:04:53也不自动等首次公告。精确材料请求为各ID官方 first-announcement 带时区记录，或该v1原项目第一次公开记录；未到只隔离这三篇，不假称贡献负命中或整源零条。

00195关闭本窗新家族归属：arxiv v1 RelatedDOI指向 [Zenodo published record](https://zenodo.org/api/records/18787663)，实际status=published、publication_date=2026-02-26、version1.0、同标题及五核心机制，main.pdf checksum md5:7c0b306f04175a01d24429782bdd67bf；[该DOI原值](https://api.datacite.org/dois/10.5281/zenodo.18787663) client=cern.zenodo/state=findable、registered02/26T16:36:39Z。不是单created首发推断，当前没有本窗重要机制diff，不计候选/评分/Books。arxiv v2官方comments明确纠正22条参考及外部攻击数量/性质、E3变负与soundness非零FP同义；不采用v1零FP或泛化formal安全保证。
