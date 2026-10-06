# 2025-09-03：准入校准与公开日期边界

作者：`daily_20250903`；检查时间：2026-10-06。此页是恢复笔记，不是完成日报。
目标窗口为 `[2025-09-02T09:00:00+08:00, 2025-09-03T09:00:00+08:00)`，即 UTC `[2025-09-02T01:00:00Z, 2025-09-03T01:00:00Z)`。

## 已实际读取的首批原始材料

以下九项都已取得并逐项读完 exact-v1 官方摘要和 submission history，原文在同目录 `<ID>v1.abs.html.gz`。
当前版本 API 的摘要仅用于发现；PACS 的 v3 摘要已经改变数字和实验范围，没有拿它替代 v1。
九张官方摘要页没有显示 withdrawal/erratum/correction 说明；这只描述本次页面实际可见内容，不证明完整历史中不存在纠错。

| 家族 / exact-v1 | 准入时需要核验的具体增量 | 本轮实际进度 |
| --- | --- | --- |
| [Top-H / 2509.02510v1](https://arxiv.org/abs/2509.02510v1) | min-p 只用最高概率 token 表达 confidence；材料以 entropy-constrained mass maximization 定义截断集合、提出 greedy 解，需要核验其约束和失败边界怎样改变采样设计 | `fresh_review` 独立准入通过；日期未证实，未评分、未进入证据完成或 Books |
| [DCPO / 2509.02333v1](https://arxiv.org/abs/2509.02333v1) | 固定 PPO/GRPO clip 与同奖励标准化可能产生无效梯度；材料提出 token-prior 相关 clip 和跨 step reward 标准化，需要核验两项机制及收益归因 | `fresh_review` 独立准入通过；日期未证实，未评分、未深审 |
| [PACS / 2509.02522v1](https://arxiv.org/abs/2509.02522v1) | 以 outcome reward 作 label、policy 参数化 score 的交叉熵实现 implicit actor/critic coupling；需要核验与 policy gradient 的等价条件和稳定性代价 | `fresh_review` 独立准入通过；只保留 v1 的 pass@256/AIME2025 声明作为待验证作者主张，未采用比较数字 |
| [AppCopilot / 2509.02444v1](https://arxiv.org/abs/2509.02444v1) | action 校正器可能自己制造重复失败；§4.2.2 提供 nearest-widget 投影和按 frame perceptual hash 缓存失败校正后回到原点的 fallback | 原先题摘只罗列模块而拟排除；补读后恢复准入，`fresh_review` 独立确认；日期未证实，未评分、未采用性能或终止保证 |
| [UI-TARS-2 / 2509.02544v1](https://arxiv.org/abs/2509.02544v1) | 长交互 rollout 的尾部等待与 credit assignment；材料提出 streaming 完成轨迹训练、stateful 环境与不同 policy/value GAE 系数，需要分离已有异步设计和本篇新增的长序列边界 | 摘要完整读完，v1 HTML 方法及训练动态相关段落初读；准入尚未独立校准，非深入完成 |
| [SpecEval / 2509.02464v1](https://arxiv.org/abs/2509.02464v1) | developer specification、model output、developer evaluator 的三方一致性作为必要 baseline，可能揭示自家 judge 与规范不一致的评价盲点 | 完整 v1 摘要已读；需要核验 evaluator bias、prompt generation 和 statement identity，未评分 |
| [RocketScience / 2509.02175v1](https://arxiv.org/abs/2509.02175v1) | 对象定位能力不能直接证明相对空间推理能力；作者声称 disentanglement 显示 bottleneck 在 spatial reasoning，需要核验受控分离与 reasoning budget | 完整 v1 摘要已读；不是因负面结果或窄任务排除，未独立校准 |
| [GRAM-R² / 2509.02492v1](https://arxiv.org/abs/2509.02492v1) | unlabeled self-training 如何使 generative reward model 产生 reward rationale；需要核验是否有具体机制超出一般 self-training 以及 preference label/rationale 的归因 | 完整 v1 摘要已读；尚待定点方法判断，不把“强 baseline 更好”自动当准入证据 |
| [Length Control / 2509.02075v1](https://arxiv.org/abs/2509.02075v1) | instruction tuning 的长度遵循被定位到更深层 component，英语/意大利语呈现不同 attention/MLP 贡献；可能收窄语言无关的指令遵循解释 | 完整 v1 摘要已读；需要核验 attribution 是否支持因果机制，未独立校准 |

## AppCopilot 改判的实际依据与反证

已取得 [exact-v1 PDF](2509.02444v1.pdf)；可检索正文为 [PDF text](2509.02444v1.pdf.txt)。准入补读到 §4.2.2、印刷页 55–56，提取文本约 L2517–2555：

模型 click point 位于任一检测 bbox 内则保留原点；落在所有 bbox 外才改到距离最近 widget 的中心。对同一 screenshot 的 perceptual hash，记录曾经不能产生交互的 corrected coordinates；再次匹配失败记录时 bypass correction，执行原始点。这个增量属于 action compensator 对自身错误的反馈分支，不能从“mobile agent 很复杂”推导出来。

原文用“有效交互应造成界面状态变化”作为假设。因此界面不变不等于动作无效，frame hash 也不保证语义状态身份；坐标记录与原点/校正点的匹配细节仍需核验。nearest widget 不保证用户意图正确，original-point fallback 不构成安全保证，更没有证明全局终止。

额外已读 §5.4、p65 的 cross-device 边界是 asynchronous collaboration，real-time synchronization 留作 future work；§6.1、pp66–67 选择 8B backbone 形成经济 cloud service，fully on-device 是未来路线。因此不采用“已实现完全端侧部署/零延迟”的叙述。

## 两项机构贡献排除

日期来自复用的 [OpenAI 官方 RSS raw](../../01/_sources/openai-rss.raw.gz)，正文是本目录的独立新抓取。

| 身份 | 原始日期值 | 本次排除依据 |
| --- | --- | --- |
| [Building more helpful ChatGPT experiences for everyone](https://openai.com/index/building-more-helpful-chatgpt-experiences-for-everyone/) | RSS `pubDate=Tue, 02 Sep 2025 04:00:00 GMT`，即 12:00 BJT，落窗 | 已读核心正文 `Leveraging reasoning models for sensitive moments` 与 `Parental Controls`：sensitive-context routing 和家长控制是 “soon / within the next month”的计划，所引 deliberative alignment 是已有方法。原文也明确 real-time router 已 recently introduced、长会话 in-app break reminders 已 rolled out；这两个已有功能没有各自的本窗新事件日期，也未披露新检测机制、受控评价或具体行为增量，故不据此恢复为本窗研究候选。未来安全安排没有被冒称已生效，也没有概括成全文不存在实际保护功能。原文为 `openai-helpful.raw.gz/.txt` |
| [Statsig acquisition / CTO of Applications](https://openai.com/index/vijaye-raji-to-become-cto-of-applications-with-acquisition-of-statsig/) | RSS `pubDate=Tue, 02 Sep 2025 11:00:00 GMT`，即 19:00 BJT，落窗 | 已读公司公告正文：收购、人员任命、A/B testing 能力和整合目标；没有新增 AI 训练/推理/评价机制或足以改变设计的证据。原文为 `openai-statsig.raw.gz/.txt` |

`fresh_review` 已独立读取 helpful 正文并通过上述限定后的排除；Statsig排除仍待其正文抽检。本页不声称报告已通过最终复核；AppCopilot 的初拟排除已经撤销。

## 日期原字段与不可采用的推断

DataCite 由 arXiv 注册的 DOI 元数据是辅助身份和时间线，不能把 `Submitted`、`Updated`、`created` 或 `registered` 改名为 `first public`。
UI-TARS-2 packet 是 `datacite-ui.raw.gz`，其他八项为 `<ID>.datacite.json.gz`。原始响应保留了 `dateType/dateInformation`，以下时间均为 UTC 原值。

| ID | v1 `Submitted` | v1 `Updated` | DOI `created` | DOI `registered` |
| --- | --- | --- | --- | --- |
| 2509.02510 | 2025-09-02T17:02:29Z | 2025-09-03T02:19:29Z | 2025-09-03T04:22:22.000Z | 2025-09-03T04:22:22.000Z |
| 2509.02333 | 2025-09-02T14:01:07Z | 2025-09-03T02:09:43Z | 2025-09-03T04:18:13.000Z | 2025-09-03T04:18:14.000Z |
| 2509.02522 | 2025-09-02T17:22:46Z | 2025-09-03T02:20:24Z | 2025-09-03T04:22:39.000Z | 2025-09-03T04:22:40.000Z |
| 2509.02444 | 2025-09-02T15:48:21Z | 2025-09-03T02:15:37Z | 2025-09-03T04:20:49.000Z | 2025-09-03T04:20:50.000Z |
| 2509.02544 | 2025-09-02T17:44:45Z | 2025-09-03T02:21:08Z | 2025-09-03T04:23:11.000Z | 2025-09-03T04:23:12.000Z |
| 2509.02464 | 2025-09-02T16:18:40Z | 2025-09-03T02:17:10Z | 2025-09-03T04:21:18.000Z | 2025-09-03T04:21:18.000Z |
| 2509.02175 | 2025-09-02T10:32:58Z | 2025-09-04T14:42:53Z | 2025-09-03T04:14:25.000Z | 2025-09-03T04:14:26.000Z |
| 2509.02492 | 2025-09-02T16:41:07Z | 2025-09-03T02:18:25Z | 2025-09-03T04:21:57.000Z | 2025-09-03T04:21:57.000Z |
| 2509.02075 | 2025-09-02T08:26:18Z | 2025-09-03T01:54:46Z | 2025-09-03T04:12:01.000Z | 2025-09-03T04:12:02.000Z |

历史 [official availability policy](../../_sources/official-calendar/availability-before-20250903.md) 说明 final ID/DOI 在 announcement process 分配、不可提前获取；也说明 “typically”、moderation delays 与 ad hoc deferrals。九项 submission 到 registration 之间都只有一个名义公告 slot：`2025-09-02T20:00:00-04:00 = 2025-09-03T00:00:00Z = 08:00 BJT`。本轮曾提出“唯一 slot 可给个体精确公开时间”的假设。

`fresh_review` 已独立反驳这个精度提升：所有 actual metadata 上界都为 04:12–04:23Z，超过 Daily 截止 01Z；它们最多证明 DOI 在其间已分配，不能排除该批正文在名义 slot 后延迟至截止以后公开。`Updated v1` 也不是 first-public，而且 RocketScience 的 v1 Updated 明显晚于 registration，说明此字段不能填补该缺口。故此假设不采用，九项都继续 date hold，不是已确认的当窗候选。

## 作者仓库与更早公开材料的关系

只针对摘要直接链接的作者仓库读取了当前 repo metadata、截止前 README commit history 和对应 immutable README。

| 家族 | 实际恢复的记录 | 当前可支持范围 |
| --- | --- | --- |
| Top-H | `ErfanBaghaei/Top-H-Decoding` repo `created_at=2025-08-15T00:43:23Z`；README commit `b78b1be13fd6485b73b3d2172dec0d10b892ed57` 的 committer `2025-08-22T05:00:04Z`；对应 README 已有同名论文题目、ECMD/ECMM、entropy cap 与 greedy mechanism | 说明需要检查早期同族正文，不得假定 arXiv 是整个家族首次公开；Git committer date 与 repo created 都不证明该 snapshot 当时已 public，也不按它们直接重归属 |
| PACS | repo `created_at=2025-08-08T13:40:41Z`；README 首次返回的 commit `4c987b47052434ce8fa14f57ec1534bcb04be305`，committer `2025-09-02T16:54:41Z`，message `init repo`；README 已有相同 PACS 机制、59.78% pass@256、verl fork 说明，但 arXiv badge 链接为空 | 它是需要核 public release/push 或作者发布说明的同族线索，不能把 commit date 当公开时间 |
| AppCopilot | repo `created_at=2025-08-27T07:47:20Z`；截止前最后 README commit `8edb38a298fc3ca26beae03bfafa70b9c6ebfdab` 的 committer `2025-09-02T15:27:33Z`，此前还有 Aug27 README edits；snapshot 包含同名系统说明 | 需要核原始 paper/artifact 的实际公开事件；不把 repo birth、普通 README edits 或当前 push 时间当论文首次公开 |
| UI-TARS | `bytedance/UI-TARS` 是 Jan19 已有仓库；截止前本次最多读取 10 条 README history，最晚为 May21 | 仅能说明这份 README 路径未在所取切片展示 UI-TARS-2 的公开事件；不是全组织或全部路径的 no-hit 结论 |

原始文件是 `github-{toph,pacs,app,ui}.raw.gz`、`{toph,pacs,app,ui}-readme-before-end.json.gz` 与三份 `*-readme-before-end.md`。不需要重扫仓库全历史；恢复时只追同稿/同机制的明确发布事件。
