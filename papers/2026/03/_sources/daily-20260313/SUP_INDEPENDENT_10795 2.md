# 10795 Re-Evaluating EVMBench：独立必要 Source / 5 分 / 具体 NC

复核者：mar13_admission_review（非准备者；准备者 mar13_supplement）。仅 2026-03-13 既有 Daily 的 2026-03-12 北京时间自然日补查。启动实际重读 AGENTS、当前 Research / Report / Prompt、Sources 使用说明与 Daily / arXiv 范围、ROADMAP、本日报开头和本日 checkpoint。只写本文件，不写共享 Books / Report / State / ledger，不授 DAY。

## 实际读到哪里

先读 [SUP_EVIDENCE_10795.md](./SUP_EVIDENCE_10795.md)，再独立回 [精确 v1 HTML 原件](./SUP_CORE_10795.raw)，实际完整 §3–5（含完整 Table 1–8）和完整 §8；为分清 Detect / Exploit 任务另读 §2.1–2.3 背景与三模式定义。使用原 HTML 正文 / 表格及 math alttext 投影，非作者摘要代原证。未读攻击实现、§6 个案战术、全部历史链交易、旧版本、代码或全引用；Figures 1–4 仅有本次方法段正文 / caption，不采用未视觉读的曲线 / bars。

[manifest](./SUP_CORE_10795_MANIFEST_RESULT.json) 为 https://arxiv.org/html/2603.10795v1，GET 200、233691 bytes、2026-10-10T03:30:31.037903Z，final URL 未换版。实际回 [完整题摘与 history](./SUP_ABS3_10795.txt)：Chaoyuan Peng / Lei Wu / Yajin Zhou，同标题同 ID，仅 v1，无 Comments、withdraw / correction 可见说明。既有本 ID 完整 AB 准入与 Mar12 arXiv 日级夹证有效复用；不把 Submitted Mar11 当公开日，不重开原 EVMBench 家族或其他日期。

## 可支持的评价增量及具体收紧

原 curated 数字与 vendor scaffold 混合排序容易被外推为模型固有能力 / 全程自主审计近在眼前 → 本稿同模型的 vendor / OpenCode 对照、两种不同 outcome / 人口，以及真实事件上的限定零执行成功揭示评价身份和阶段推断失配 → 应重新核 harness、任务、人口、scorer 与执行结果，不能由发现得分替完整 effect。只采用这条测量界限，不把 26 配置 / 22 案规模、机构或金融标签当贡献。

1. **配置并非完整 Cartesian 曝光。** §3.1 文字称三模型 across all three scaffolds，但 Table 5 实际 Claude Opus4.5 / Sonnet4.5 只列 CC 与 OC，GPT5.3 只列 Codex 与 OC；三模型、GPT 四 effort 档形成六个 vendor-vs-OC 比较，不认证每模型完整 3×3。Opus4.5 OC43/120 对 CC37/120 是 5pp 单 trial 例，GPT5.3 xhigh 则 OC28 对 Codex30，不能授 OC 普遍更好或所有脚手架唯一因果。
2. **纠正准备包的一处误报。** Table 1 和 Table 4 的 Claude family 均列 Sonnet4.5 / 4.6；准备包最初据此说“Table1 4.5 / Table4 4.6 人口冲突”不成立，应删。真正的不一致在 Table 4 与 Table 8：前者 Incidents Detect 的八项包含四个 Claude、GPT5.3 high / GPT5.2 high、Gemini3.1、GLM；后者实际是两个 Claude、GPT5.3 四 effort、Gemini3.1 custom tools、GLM。不能把这两表拼成同八配置，更不能据 Table 4 给 Table 8 逐项指派完全相同权限 / 曝光。
3. **Detect 人口与 judge 边界。** §3 / Table 5 是 120 known vulnerabilities / 40 repos 的 recall score，不扣 false positives，不给 ground truth 未列的新真 finding 加分。Table 5 `Tasks w/Score>0` 的 35/38/39/40 是另一个任务分母，score 仍 /120。Table 6 的 120 个 valid modifications 全接受、错误 / injection 1–4 被接受是有限合成灵敏度切片；修改本身由 GPT5 产生，共享误例归因 test-generation flaw 是作者判断，不独立认证 99.2% 或全排名无偏。
4. **两种 Exploit 成功量不可混用。** Table 7 有 16 tasks / 24 vulnerabilities，fraction-of-target-funds 的部分分合计 `14.67/24 = 61.1%`，fully successful tasks 为 `9/16 = 56.25%`。这不是 61.1% 任务全成功率，不与原研究另运行的 72.2% 合并；Detect / Exploit 排名反转还改变人口、任务和 scorer，不直接定位唯一能力原因。
5. **20–22 graded 分母保留 missingness。** Table 8 Opus4.6 为 13/20=65%，GPT5.3 high 为 13/22=59.1%，GLM9/21，Gemini6/20。未判分原因包括 container timeout / grading failure，不能补成共同 /22 或当全模型总体发现率；“unlikely change overall ranking”是原作者判断，未给 missingness / 重复不确定性依据。
6. **0/110 不授 conditional finding 后失败。** §5.2 五配置×22 案、每案 6h timeout，未产生净利润记失败，支持该人口 / budget / API / 环境下独立 Exploit 运行零成功。§2.3、§3.2 与 §5 没有披露将本次 Detect finding 作为提示交下一阶段的 paired conditional 测试，因此不证明“已给正确 finding 后仍全失败”，也不直接推翻任何已知漏洞条件下的通用成功率。它限制的是把 curated outcome 外推到真实事件端到端能力，非永远无法利用 / 零风险。
7. **release 不是完整污染证明。** 选择 post-release incidents 是当前原件宣称的事件时间条件；没有训练 membership / 记忆直接证据，旧源 / 机制能否暴露、latest API 是否固定 revision、运行时可见内容等不能由 release 字段认证。原 §2.3 声称原 EVMBench Docker 无互联网，也不是本稿全部运行权限及预训练血缘的全面审计。保留作者更晚事件设计，不采用“contamination-free”全保证。

§8 还明确有限单高严重度 / 可隔离重现选择、没有 cross-chain / ZK、human ground truth 可错、大多单 trial 且无 CI / seed variance、cross-scaffold 只 Detect 三模型、OpenRouter 而非 vendor API、timeout 可为基础设施失败。引用其他研究的 47% / 46% 不作为本次模型身份错误率或假冒指控。硬件 / precision、完整 Detect timeout、全部默认权限 / revision、token / API 总费用必要段 Not Disclosed；110×6h 只是逐 run 上限，不补成实际总 660h。重建、fork、工具 / judge / 模型调用、trace 与重复审计均需计费，这一完整费用要求是复核者系统限定，不假称稿内已测。

## 评分与实际 Books 承载点

`2 + 1 + 2 = 5` 成立。D2 计有限实证对脱离 scaffold / 人口的排名与 curated-to-end-to-end 推断的设计反侧；R1 限安全 Agent evaluation 这一测量负载，不因多模型、多 vendor 或真实金融损失借跨层分；Durability2 计新正反证对具体 evaluation identity / outcome 分责的稳定验证，不把成熟“人工重要”或 benchmark 命名抬分。设计反证因此读足受影响必要段，NC 不缩候选 / 降分 / 减去已完成投入。

实际完整读 [Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 285–323 的 identity / harness / environment 与邻接、601–626 的数据 / 污染论证、1951–2020 的 artifact / execution / outcome 完整局部，而非根据标题认覆盖：

- 当前 287–291 明确 `model × benchmark × harness × environment × scorer`，prompt / tool serialization / retry / timeout 可改变观察，分责并保原 trajectory / component receipt，不能给模型脱条件排名。当前 303–311 邻接又把权限 / 不同预算及 invalid measurement / operational failure / actual negative 分开。
- 当前 601–622 不由输出 sensor 证明训练 membership，并明确训练无污染不代表工具可访问评测运行无污染；访问轨迹 / 外部状态与血缘单独审核。这实际承载 release 日期不足以签全污染保证，不仅主题关联。
- 当前 1951–1959 及 1997–2013 从静态答案到 artifact / executable verifier / environment / trace / outcome，专门写 exploit 只有真实编译、运行、触发目标才能与描述漏洞区分，N-day 须固定目标 / patch / 网络 / 时间 / 成功判据；verifier 也不是 ground truth，局部环境能力不能授普遍自主性。它承载 detect 描述与实际 effect 的具体分账，而不需要再重复一套安全场景术语。

故唯一 owner `PLATFORM-EVALUATION-SYSTEM` 的**具体已有覆盖（NC）、Books 新写 0**成立。本稿新的数值、事件 / 配置局部反证留本日证据与报告；不声称它们已写入旧正文或被书稿吸收，不将原 EVMBench 误当同事件去重。Ch72 仅风险 / effect authority 交接，无新增 owner 或 PRE。没有实际新控制责任接口要求另写两段，故无需 Books / POST。

## 最小终态

实际复读作者修后的 packet §“机制与评价条件”：不存在的 T1 / T4 Sonnet 冲突已撤销，§3.1 声称与 Table 5 实际配对范围的差异已保留，真正 T4 / T8 缺失 / 新增配置也已明记；其余受限采用未变。五个本地引用目标存在，scoped diff-check 无空白警告，本 reader 仅新增本文件，没有 stage / commit / push。

限定必要 Source、5 分与具体 NC **通过**；已修正 packet 可交 root 正式同步，Books 新写 0，无 PRE / POST。未授全污染消除、全任务最优排名、Detect 后 conditional Exploit 结论、实际代码 / 复现、生产可替代性或 DAY。必要支持与反侧已充分，在此停止，不执行漏洞或扩全链历史。若后来补齐 matched finding handoff、真实 model revision / 曝光、重复统计或 verifier 改变，只定点重开对应结论。
