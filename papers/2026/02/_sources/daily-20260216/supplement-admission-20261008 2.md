# 2026-02-16 补查首批准入校准

范围：补充 2026-02-15 ～ 2026-02-15，北京完整自然日；原候选0、原窗口及原§4冻结。执行时间2026-10-08T16:20～16:31+08:00。
作者：supplement_20260216；尚未独立验收。

## 原件与有限入口

[west](supplement-entry-west-20261008.json)、[east](supplement-entry-east-20261008.json)、四组date-search原件分别保留14条实际query；[native](supplement-native-dates-20261008.json)保留OpenAI RSS邻接pubDate与Anthropic/Zhipu官方HTML日期上下文；[signals](supplement-specific-signals-20261008.json)、[originals](supplement-specific-originals-20261008.json)为具名原始恢复。
日期搜索停在工具返回结果，不授完备性；主题语义不是关键词命中率或owner映射。未展开全年目录、每周来源或其他Daily候选。

## 全部拟新增：0

截至首包没有已确认落补充自然日且通过准入的新增家族；不是宣称全网0贡献。下列一项贡献潜力明确但本日不采用：

- **SkillJect，arXiv:2602.14211v1**。官方完整题摘已读（originals，L9–20）；原先技能文档/脚本被合并为可信能力 → 以执行trace闭环优化隐蔽skill攻击并把payload藏在辅助脚本 → 可能改变仅审文档的供应链防护选择，属于PLATFORM-SECURITY潜在增量，不因摘要无实验细节排除。搜索索引的2026-02-15是提交/抓取run date，不是公开日。官方v1 history给出的提交为15 Feb16:09UTC，即北京时间02/16，已晚于补充窗；arXiv公开流程晚于提交，不能把它算作Feb15公开。定点cs.CR月列表恢复cache miss，没有反推公开日期；作者当前仓库无Feb15公开证据且已用3月后版本。实际首次公开日及是否存在更早作者发布尚未确认，作为窗外恢复线索，不在本日报评分/全文/Books采用，不指定其他日报归属。复核需核此下界判断与“未把submitted当public”边界。当前官方v1事件页无撤回/纠错标记，历史后续v2/v3仅身份信息，不审后续正文。

## 分层代表排除及理由

1. **MemGUI-Bench Feb15 adopted by Mobile-Agent-v3.5**：官方README的具体事件仅为既有bench被采用与Easy任务27.1%新榜单；没有新的协议、盲区诊断、可比失败条件或机制解释。不能因benchmark主题或已有Books覆盖排除；这里按这次事件实际增量不足关闭。旧Feb03/09首次发布不重新审。本日不采用宣传数字，后继June Agent/revision不混入Feb15。
2. **open-terminal 0.2.3 / 0.2.2，CHANGELOG Feb15**：官方完整本次变更说明已读。0.2.3把已有endpoints经stdio/streamable HTTP包装为可选MCP服务；0.2.2明确strip字面null参数防客户端422。不是新执行、隔离或权限机制，也未提供可修正长期正确性判断的证据；窗口中这两个具体变化不准入。旧02/14 unauth temporary URLs、JSONL/offset状态不是本日新增，不外推为安全已审。若出现具名安全公告或本次权限语义变化再定点重开。
3. **nanobot Feb15 OAuth provider接入线索**：仅第三方镜像日期/标题，官方当前README已改写；所述变更是既有provider兼容性接入，不呈现新权限边界或长期机制。按该明确增量不足关闭，不宣称旧版本代码/安全已核；02/13 security hardening属窗外版本线索、不以fix标签扩大本日审阅。
4. **OpenAI社区用户计费/开源呼吁与MCP discovery故障更新**：完整核心帖子已读，只是建议或单用户未诊断问题，无因果机制/可比证据；不以机构domain授官方研究权限。MCP Inspector成功不证明服务根因，不能将用户归因照录为已确诊设计反证。
5. **MiMo材料R&D / Meta DINO领域应用标题**：领域应用，不重新开放暂缓AI for Science；官方目录只是有界查漏，未形成全文队列。
6. **日期伪线索**：Seed2.0官方02/14与Leaderboard截至02/16、Qwen3.5快照名02/15与官方News02/16，不是Feb15首次公开的证据。原需要精确时刻的旧保留不沿用为新要求；本轮只核公开日期。

## 公告例外与停点

arXiv availability L172–200实际读：Friday/Saturday无公告，Sunday02/15 20EST=北京时间02/16，Feb15补充窗不含常规新稿/replacement/withdrawal/cross-list批次；2026 holiday表无Feb15。status首屏和两条有限日期异常query未恢复本窗异常公告，搜索返回噪声不授阴性权限；没有具体异常线索需开分类队列。不据arXiv无批次授机构零发布。

待主任务独立校准以上全部拟新增0、SkillJect日期线索及理由分层代表项；作者继续完成有限源恢复、具体请求和六部分写回，不把普通pending当外部blocker。

## 新窄query校准补充

独立精确Google日期query另恢复Dingle/Hutter《Simplicity and Complexity in Combinatorial Optimization》，正式公开Feb15核实。完整题摘与决定准入的§5/7及§4范围段实际读后，按本稿新增只有组合最优解描述复杂度/算法概率采样等待次数、忽略样本生成成本与不可算prior、模型学习关联只是引用既有工作，未获得直接改变本项目模型学习/设计的命题而贡献前关闭。不因理论/非LLM关键词拒收。root实际同读这些必要位置并于本轮明确同意，见supplement-20261008.md及dingle-xml原件；不继续PDF/全部证明/现有Ch4比较。原首包0仅阶段，全部有限来源结束后本轮确定新增0。
