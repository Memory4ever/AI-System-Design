# 02/20 首批准入校准请求

作者：feb20_v3；窗口：2026-02-19T09:00:00+08:00～2026-02-20T09:00:00+08:00。已实际重读 AGENTS、Research/Report 合同、来源说明/每日/arXiv、Prompt、ROADMAP 和最新相关 checkpoint。旧 V2.1 完成标签不复用；435条旧库存仅作查漏线索，不成为全量逐项队列。完整题摘取自本日 `inventory.json`，必要时恢复 exact v1 官方摘要。以下只授潜力判断，不授证据、日期或 Books。

## 拟入选潜力

| ID | 原约束→实际增量→具体选择 | 拟评分/审阅 | 日期边界 |
| --- | --- | --- | --- |
| 2602.16052 MoE-Spec | draft tree触发过多MoE专家→每层限制验证专家容量而非只减树深→重新比较保分布验证与质量/吞吐折中，不能默认exact | 2+2+2=6，涉及精确保证反侧，深入受影响机制 | Submitted 02-17 22:02:36Z最早Wed20ET、登记02-19 02:37:05Z上界；待原字段核验 |
| 2602.16246 Proxy State-Based Evaluation | 确定性backend昂贵→从全轨迹推导proxy state、按场景约束判goal与hallucination→评估是否能以代理状态替代事实状态并保留评价可信度 | 2+2+2=6；必要标准证据及owner差额 | Submitted 02-18 07:49:47Z，登记02-19 02:41:40Z，待核 |
| 2602.16313 MemoryArena | recall和single-session分开测→跨session明确依赖前次动作/反馈的任务揭示LoCoMo高分不能预测agent任务表现→memory评价加入未来决策效用而非仅回忆 | 2+2+2=6；设计反证深入受影响评价 | Submitted 02-18 09:49:14Z，登记02-19 02:43:13Z，待核 |
| 2602.16444 RoboGene | 真实采集昂贵且生成指令不可行→任务多样性采样+物理约束反思+人反馈，真实18k轨迹对下游VLA泛化评价→任务生成要由可执行性和数据收益共同选 | 2+2+2=6，标准；若具体长期差额则深入 | Submitted 02-18 13:29:43Z，登记02-19 02:46:18Z，待核 |
| 2602.16520 RLM-JB | 单次guard被长文/跨块隐藏攻击绕过→有界规范化、分块全覆盖和跨块信号合成→分块安全检测需检验组合覆盖而非独立块安全 | 2+2+2=6，安全深入受影响机制 | Submitted 02-18 15:07:09Z，登记02-19 02:48:12Z，待核 |
| 2602.16603 FlowPrefill | 小chunk响应快但效率低→operator边界抢占与arrival/completion事件调度解耦→不必把可抢占粒度绑到调度频率 | 2+2+2=6，标准；具体机制长期差额深入 | Submitted 02-18 16:57:45Z，登记02-19 02:50:19Z，待核 |
| 2602.16708 Policy Compiler for Secure Agentic Systems（PCAS exact-v1） | prompt policy不能保因果历史约束→动态事件图recursive backward slice与独立reference monitor→执行许可需依authenticated principal/完整观测及手写policy，不借后来FORGE名证明本窗 | 2+2+2=6，安全深入受影响保证 | Submitted 02-18 18:57:12Z，Registered上界见V3_EVIDENCE_FIRST，官方公告下界桥接，不以Created当正文公开 |

## 日期保留但仍有贡献潜力

- 2602.15945 CE-MCP：原AB提出16类attack taxonomy，但实际§6.3只试四个攻击，不把分类数当实验覆盖数；采用exception-mediated injection导致已有write/admin capability被重新生成程序误用的有限新路径，不授sandbox escape。Submitted 02-17 19:03:08Z（Tue14:03ET）只给公告最早下界；已结合同ID arXiv-issued DOI Registered上界与官方ID/DOI流程推定完全落窗，见V3_EVIDENCE_FIRST与V3_BOOKS_SECURITY_PRE，不沿旧标签。
- 2602.15831 A2H：可解析Human Card及跨消息媒介寻址可能改变agent联系人的identity/discovery接口，不因模块成熟直接排除；Submitted 2025-12-31和登记02-19之间无法唯一确定首公开窗，隔离不进入确定候选。

## 代表排除拟判断

- 2602.15832 PICQ-drama：完整摘要是在戏剧对话choice题辨识missing persona维度及LLM/人差异，未显示可改变foundation model学习或agent执行/记忆/评价设计的具体机制；不是因小数据而排除。日期不确定无须为该判断再恢复。
- RoboGene/RLM-JB 不以“成熟组合”排除：它们分别给出可执行任务多样性和跨块payload覆盖的可核收益/失效界；细节可信度属于证据阶段。

尚须恢复14每日来源及有界主题发现、候选冻结、必要正文与Books判断。初筛不等于Evidence完成。
