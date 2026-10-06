# 11/14 SIMA2 / Cyber：有限证据与 Books 处置 ready

作者 Planck。日期/准入沿用 [root 实际校准](FIRST_INDEPENDENT_REVIEW.md)；不重复该层。此包申请两项必要证据、反侧与具体 Books 处置复核。实际 Books 写入0，未声明独立 Evidence 或日级通过。

## SIMA2

[官方 Blog](https://deepmind.google/blog/sima-2-an-agent-that-plays-reasons-and-learns-with-you-in-virtual-3d-worlds/)，核心见 [raw-web-15](raw-web-15.json)，原生日期见 [HTML](raw-sima2.html)。采用 `datePublished=2025-11-13T18:55:00+00:00`；后来dateModified不证明内容从未改动。

实际 L147–148 与 L300–306 披露先人类示教、再由Gemini给任务与估计reward，把自玩经验用于后续代agent。采用这个训练路径，不采用reward是真值、全流程无人工/零示教或自动持续上线。L266–270明确用扩展的新评价集合重测SIMA1，不能拼旧论文成绩；held-out游戏和L273–274生成环境展示也不能证明物理迁移。L324–325的长程目标核验、短记忆/低延迟取舍及精细动作限制收窄了通用能力主张。没有matched总训练预算或独立reward可靠性证据，不保留量化因果收益。

官方同路径 technical report 实际 [GET200](raw-sima2-report.pdf.request.json)，[PDF](raw-sima2-report.pdf) 封面2025-12-05，CreationDate/ModDate Dec5，存储Last-Modified Dec8；web工具此前因33MB失败见 [raw-web-16](raw-web-16.json)。只读身份、完整摘要和相关训练线索，未把Dec稿细节倒填Nov13。两次有界恢复查询见 [raw-web-17](raw-web-17.json)：官方Nov13报告查询与arXiv精确题名只得到当前博客/2512.04797线索，停止继续追完整附件。原Nov13稿仅在需要其具体优化、筛选或预算结论时重开；不是整个Blog家族被阻断。

评分 **2+2+2=6**，作者标准审阅范围是以上有限训练路径。Books建议 **仅报告**：`MULTIMODAL-EMBODIED-VLA` 的 [Ch26](../../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) 现有“数据演进”已分示教、派生label及provenance，“生成环境本身也是版本化训练状态”已保留生成/课程/消费policy身份与真实物理验证边界；Ch25开篇区分想象与真实状态。SIMA Blog提供有意义的新虚拟环境训练实例，但当前有限说明尚未给出可移植的新筛选/优化机制来改变这条长期链。没有因为Ch26缺SIMA产品名要求整合，也不把teacher估计非真值这个成熟原则重新计分。若root认为代际经验闭环本身构成独立短段差额，可指出具体位置后协调，不以“仅报告”删去本日准入或反侧。

## Anthropic Cyber case

[官方事件页](https://www.anthropic.com/news/disrupting-AI-espionage)，[raw-web-05](raw-web-05.json) 与 [HTML](raw-anthropic-cyber.html)。采用 `datePublished=2025-11-13T16:00:00.000Z`；后续修改字段保留。

采用 L36–38 报告的人工目标/决策点与将恶意过程拆成看似正常子任务、不给模型完整目的这一失效路径。L43的80–90%只是厂商工作量估计，不是端到端成功或无人完成率；L44虚构credentials、公开信息误报及L49仅Claude可见性限制推广。L56–59明确Nov14纠正原请求速度，废弃“千次/秒”，也不用更正后的节奏推导自主能力。

两当前官方PDF均带Nov17 attribution变更，原始web结果见 [raw-web-05](raw-web-05.json)、[raw-web-06](raw-web-06.json)。现版的细致跨session状态/阶段实现和修订归因不能认证Nov13原件；本日不采用其确定国家归因或具体跨session架构。安全及纠错受影响范围已深入读核心流程、反侧与changelog，不扩读攻击操作细节或MCP全站发布。

评分 **2+2+2=6**；安全/纠错触发深入审阅，但只支持被报告的组合语义失效，不认证独立因果/跨模型发生率。Books建议 **已有覆盖**，唯一owner `AGENT-PLATFORM`：[Ch84](../../../../../books/part-07-agent/84-agent-platform.md) 的“快速演进的Skill/Tool Layer不能拥有Primitive Effect Authority”实际规定proposal与独立effect enforcement，并明确语义风险不能表达时拒绝/人工/只读；“Policy与Agent Identity”拥有delegation、approval与credentials；相邻Ch83只拥有连接协议，不能代替授权。该case强化为什么模型安全判断不拥有副作用授权，不需要复制安全原则或给MCP强加新机制。**不声称现有primitive policy已能识别所有总体恶意意图**；这项未证明边界随报告保留，Existing不是安全解决。

## 独立核验请求

请root只核以上最小采用命题、后续原件隔离、评价反侧，以及SIMA仅报告 / cyber具体已有覆盖是否成立。Sparse的训练连接约束差额另见 [单项包](SPARSE_EVIDENCE_OWNER_READY.md)，不重复。若有实际Books增量，需root协调共享写入和非写入者POST；本作者不写Books/shared state。
