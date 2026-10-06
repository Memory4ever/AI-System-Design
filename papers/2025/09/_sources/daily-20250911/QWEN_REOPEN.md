# 2025-09-11 Qwen 窄重开交接

作者 Bacon；2026-10-06。仅重开本日Qwen，不重跑其他来源、七项已校准潜力或整月。已完整重读当前AGENTS/合同/来源Daily与arXiv/Prompt/ROADMAP及最新9月路由。发现来自12日独立扫描的官方站迁移恢复，按研究合同§2/7定点纠正公开归属。

## 最新：root 实际单项通过，非 DAY

root在当前会话确认实际读官方完整派生正文Introduction→References、config原始JSON精确qwen3-next对象，以及Ch22 Hybrid/Outputgate完整相关段；新增准入2+2+2=6、原UTC日期到11日04:00归属、三项机制Books NoChange已有覆盖均通过。版相关兼容、native/1M边界按必要受影响深入；实际三图仅支持作者有限趋势，不采用10x或3:1普适因果。正式日报计1家族；配置/recipe及图版本事实仅报告，不增正文。最终DAY仍由另一个非作者承担，不自授完成。

## 初次新增拟入选交接（保留依据）

[Qwen3-Next: Towards Ultimate Training & Inference Efficiency](https://qwen.ai/blog?id=qwen3-next)。官方加载JS模块969中的 `/api/page_config?code=research.research-list` 实际成功，配置直接关联标题、id与正文tokenLinks，不是搜索摘要或DataCite。`qwen-research-config.raw` 原始 `date="2025-09-10T20:00:00.000Z"`，转换北京时间2025-09-11 04:00，完全落11日窗口。[官方token JSON](https://docs.qwenlm.ai/research/qwen3-next/index.json) 返回101627 bytes，`qwen-next-content.raw` 与派生 `qwen-next-content.txt` 保留。正文明确发布Instruct/Thinking两版本。需root核date字段和本次发布事件采用，不再以旧首页漏列证明本窗未命中。

贡献：纯线性状态的recall与full attention长上下文成本冲突 → 75% Gated DeltaNet与25% gated full-attention、超稀疏MoE及稳定设计形成实际80B-A3B发布分支 → 可审阅混合状态容量/可寻址历史与训练、推理条件的联合取舍。不是将10x速度宣传直接当机制因果。作者贡献筛选拟通过，拟2+2+2=6；新增项尚未独立首批准入，既有七项校准不延伸至此。

已读Introduction、全部Key Features、Pre-training/Post-training核心及Develop/long-text限制：3:1混合；full attention输出gate、head dim256/25%partialRoPE；512expert/10routed+1shared；Zero-Centered RMSNorm+norm decay、router初始化；MTP多步一致性。训练15T取自Qwen3的36T库，GPU-hours比较Qwen3-32B与30B-A3B；不是same-active参数同预算单因素消融。不同架构、活动参数和稳定措施同时改变，不能证明3:1全局最优或每项稳定设计各自因果。仅作者结果，未复现。

必要反侧：吞吐高度依赖实现，Transformers不普遍提供MTP；部分示例需main分支/允许长上下文环境变量，不能授任意已发行runtime兼容。原始序列上限262144，1M是YaRN扩展；static YaRN可能伤短序列，不能写1M native。benchmark图配置仍需核，未披露保持Not Disclosed。`qwen-card.raw`是当前main，不冒充2025精确commit实现。

已实际读取三幅原图，文件 `qwen-next-prefill.jpg`/`qwen-next-decode.jpg`/`qwen-next-ruler.jpg`。吞吐图归一于Qwen3-32B=1，比较三个架构，4K～128K；没有hardware/precision/batch/concurrency/SLO及runtime/版本说明，不能把示例TP4当图的测量配置。图支持作者在该未完整披露条件下的相对趋势，不支持绝对token/s或单一hybrid因果。RULER表包含4K～1M：Next在192K为94.0，235B为94.5；1M为80.3 vs84.5，Avg91.8 vs92.5。不能采用“所有长度都胜过更大模型”的解读；native256K与YaRN外推必须分开。没有从图像估计值补造精确数据。

Books实际对照：`MODEL-LONG-CONTEXT` [Ch22](../../../../../books/part-02-model/22-long-context.md) 的§“Hybrid与迁移”正文781～801承载固定状态+显式读取、双状态/KV代价及recipe归因边界；§“Output gate不等于跨时间Memory gate”863～871承载GDN memory-transition与softmax output gate的差别；GDN递推501～509承载decay+定向delta更新。上述相关完整段落实际读到，不是只看关键词。邻接Ch21开头已读total/active容量分权与dynamic routing；Ch23开头表示接口已读，不将本发布写入多模态owner。拟处置“已有覆盖”限这三项实际机制；Qwen3-Next发布配置、局部作者图及未隔离的训练稳定recipe仅报告，不为历史发布重复塞入数表。无自然段拟增量/共享写入，需root首批准入与Books独核后冻结，不先授采用。

已撤回11日12:10“仅剩root DAY”停点；旧证据/校准有效。新增项必要核心/反侧和实际owner对照现已备齐交root；尚待新增日期/准入、限定Books处置和整日独立复核。不能把等待root称作者自行通过。
