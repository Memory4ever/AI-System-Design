# LifeSim：exact-v1必要增量与最低处置提案

mar14_supplement准备，仅03-14补Mar13 BJT。完整原Atom题摘及精确v1 ABS/三作者/无当前具名早稿说明见SUP_FINAL_NARROW7.md；正常公告规则与SubmittedMar12T16:49:34Z、owning arxiv.content/findable RegisteredMar13T02:12:03Z夹Mar13 arXiv事件日，日级与准入尚待非准备者独核。SUP_CORE_STOP_12152.raw官方exact-v1 GET2001353354B，2026-10-10T03:45:45.864343Z。

实际必要阅读：§2–3 B17–108（包括Table2所有行B51–68及评价/配置）、§5 B105–132/Table3–4行为校准和直接反侧、§7–8 B147–154结论/限制、Appendix D B409–429指标定义及E.1 B434人审协议。B431/B435长prompt未完整展示、不用其中实施细节；未读全部案例/附录、代码或图像像素，不称复现。

准入窄命题：只用显式请求评价个性化助手会漏掉未直接说出的需求 → 本稿把BDI生成的意图清单、环境轨迹和跨事件固定偏好组织成显式/隐式两种任务及recognition/completion/profile recovery测量 → 可以局部检验助手在该模拟人口中是否漏识别/漏完成预先设定的隐式目标。不是因1200新条目、人格术语或“long-horizon”标题收录。拟1+1+2=4/已关闭/仅报告Books0：Design1限模拟器与该checklist评价配置，BDI、记忆、情绪、derived profile均明确复用既有方案；Reach1限文本个性化对话，Durability2限评价人口/目标身份和两种测量的可复用约束，不给借用的成熟原则或泛化真人认知机制加分。未识别改变长期记忆/授权/澄清策略的重要机制或有效性定律，故无需owner/Book/PRE，仍保留窄P，不改EX/NC。

§2用长/短belief、九个desire检索/rerank/softmin采intent，以及带时间地点天气的3374真实mobility轨迹/251POI组织合成事件。环境轨迹真实不使合成latent意图成为真人隐藏需求真值；1M profile来自SocioVerse/AlignX组合，不是1M真人连续交互。用户engine用记忆感知与情绪推断，语义阈值.7是本配置，不是偏好真值或新的心理因果机制。

§3/AppendixD预定义最多五个explicit/implicit checklist目标：每次assistant response前预测意图、episode合并后由LLM判与清单匹配；completion也由LLM判回答是否足够完成清单，均非真实环境成功receipt。三judge平均（GPT4o 2025/11/20、Qwen3-32B、Llama3.1-70B-Instruct）只支持该scorer人口。120用户×10事件=1200 scenario、八生活domain；single最多20turn，long最多3turn，100用户的固定历史由Qwen32B用户与DeepSeekChat助手生成、1–10事件/>14Ktokens。不能把不同预算或合成历史直接认作相同真人long-horizon协议。

Table2各模型在该协议的implicit recognition/completion低于explicit，只支持受限checklist盲区，不外推所有真人需要、策略因果或越多澄清越好。profile-memory是事件后总结，正文报告Gemma12B/Qwen14B局部改善、Llama8B/Gemma27B平或略退；没有一致无成本长期保留保证。Table3以300合成scenario评用户engine，实际真人仅30sample×3英语annotator。去情绪后人审context relevance仍96.2等于full，故正文“all dimensions drops”并非所有表格cell严格下降，不借该消融签全部模块因果。

Table4只150个single-scenario模拟结果的人/judge agreement：.77/.84/.81、均值.80；第一项恰.77而非全部严格>.77，也不是对long-history或真人latent意图真值的校准。E.1是三名英语熟练硕士学生、20RMB/h和随机打乱评分，不是真人长期用户trial。生成轨迹、模拟用户、多次assistant、三judge及profile-summary均有调用费用，未认证matched成本/SLO。§8仅日常文本、缺高风险domain与multimodal cues，公开结果不支持普遍长期个性化/心理fidelity。支持与直接反侧已足以最低判断，停止无关附件；待非准备者核必要原件/日期/评分后才formal。
