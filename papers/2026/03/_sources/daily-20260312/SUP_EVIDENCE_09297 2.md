# 2603.09297 — TA-Mem必要Source与Ch77具体已有覆盖（非作者通过）

[exact-v1 PDF](https://arxiv.org/pdf/2603.09297v1)。官方HTML404后精确PDF可读，作者实际§III全文、§IV全文及TableI、§V限制；未核Figures2/3曲线像素或代码。root此前准入决定core已读III/IV，不需重复无关References。current轻核仍v1/comment空/无withdrawn或已见纠错，未见accepted先稿，不扩无关历史。

必要日期字段在SUP_EXACT_BATCH3.json，fresh回读一致：Mar10UTC07:27:01提交落announcementdeadline批次，owning arxiv.content/findable DOI registeredMar11UTC02:10:06已可发现上界＋official no-advance finalID/DOI最早公开Mar11BJT08下界同BJT03-11。只以组合夹证，不以注册/Submitted/Updated单独public，待root独核。

2+1+2=5：固定topK/静态workflow不表达跨episode按需探索→多索引工具读取在iteration budget下的有限质量/费用与终止代理→按任务切片验收读取预算而非把工具自停当完整支持。索引/toolloop成熟不作为新机制加分，准入只保留具体预算/适用条件证据。

§III抽取topic chunks与summary/keyword/person/fact/event/时间，保存raw消息起止及conversationtimestamp；三类stringkeys、event/fact cosineTopK、personprofile供Agent选择，空命中可查询availablekeys。每QA cache已见page/profile避免重复content回Context，不是事实去重/索引正确性证明；原始消息与时间有助回核，但不能保证抽取不偏、人物一致或最新事实真实。

§IV LoCoMo10长conversation/1986全问题，quality排除adversarial而tooldistribution仍纳入；GPT4omini抽取与retriever、MiniLML6embedding、TopK5、最大7轮。TableI temporal F1 55.95较强，但multiHop35.62低于Mem0 38.72、open26.42低于28.64、single44.87低于MemoryOS48.62；因此不采用“全部baseline普遍胜”。token3755也高于Mem01764/A-Mem2520；基线配置/总抽取索引维护与各读取budget并未统一披露，不能同总预算因果归唯一toolloop。

§IV.D作者称4轮后收益/花费趋平与97.73%问题已经finalized，本轮未独读Fig3像素，不把曲线精确极值当已独算。重要定义是其success指Agent在预算前自行决定不再toolcall，不是gold答案正确或检索证据完整。最高7轮仍增加尾部调用/latency；token指标不含完整抽取/索引/端到端墙钟、可支付费用或SLO。§V承认prompt-sensitive抽取与loop延迟，未验证更大/多模态人口。固定512/25%overlap、semantic与LLMchunking同时受抽取prompt影响，F1 44.34对43.73但BLEU38.34低于38.39，也不授必优。seed/CI、硬件/precision/闭源endpoint精确revision、全budget与数据污染检查Not Disclosed。

唯一owner `AGENT-MEMORY`，[Ch77](../../../../books/part-07-agent/77-memory.md)。作者actual181–254与255–292完整局部、Ch77/78开篇及此前实际Ch76开篇交接已读：184–191按需通道/重复索引费用与简单路径共存；204–213读取前authorization、task/tokenbudget、raw/source/time和派生索引非真值；255–280 anchor→预算扩展→identitydedup→packing完整读链、controller与factauthority/Context预算分责和flat/fullContext回退；286–288按未满足subgoal探索及真实终止与policy标签分开、明确budget/Unknown/空集合规则。后者正承载“tool自停不等证据充分、有限多轮增加费用”的具体预算边界，前者承载multi-index/缓存回原文。该论文有限条件证据强化原判断，不新增需长期展开的索引/tool组合机制，拟已有覆盖/No Change而非EX或外部hold；无需为制造diff写段。必要Source/日期与具体NC待非作者核，不授实现/复现或DAY。

实际独核：root实读精确PDF§III/IV全部关键文字/TableI/§V、原日期夹证字段和Ch77 181–218/249–293具体正文，接受5分标准Source与具体已有覆盖。IV.D success为自停非gold正确、任务退步/费用反侧及预算/终止/Unknown已承载，不采用Fig3精确曲线或matched预算因果，无Books新写，不授DAY。
