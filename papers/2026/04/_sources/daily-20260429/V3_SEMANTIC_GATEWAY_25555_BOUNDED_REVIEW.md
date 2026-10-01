# 2604.25555v1 Semantic Gateway：有限探索不等于形式安全证明

04/29 V3 作者侧必要审阅，非独立 Gate。核[官方 exact-v1](https://arxiv.org/html/2604.25555v1) §6.3–8.3、§9–12 与真实 [Ch72 Canonical Action／Effect-time Authorization](../../../../../books/part-06-ai-infrastructure/72-security.md)；本项已在旧 60 的潜在线索内，**不增减**当前 `106＝67 潜在＋39 前闭` 工作账。首页 04/28 日标签不独证首次公开；正式归窗待本日窄公告链及以下更早实现公开例外审。

**先于本窗的同题 artifact 日期例外：**论文 §8.4 自引的[作者 PoC 仓库](https://github.com/PeyranoDev/semantic-gateway-poc)现时 GitHub API 给 `created_at=2026-04-27T20:16:03Z`、`visibility=public`；[最初 commit `1efca4b`](https://github.com/PeyranoDev/semantic-gateway-poc/commit/1efca4bf0a9e541577ba050e5f4e57ce367bdb68)的 committer 同时刻（北京 04/28 04:16，本窗开始前约 4 小时 44 分），当次增加 141 行 README 和整套 PoC。初版 README 已明写同一论文完整题名、Semantic Firewall/RBAC/EPA/fuzzer 组件，初版 fuzzer 注释已陈述 `AcceptSharingRequest` bug 与“修后 100% correspondence”。这足以触发**可能较早公开同家族核心 artifact**；但当前 `visibility=public` 与 commit 时间不能单独证明 04/28 04:16 时已经对外公开，仓库也可能由私有后转公开。若无历史公开切换/独立索引时刻，保持本项首次公开归属 **Unknown／安全隔离**，不拿 04/29 arXiv 批次自动作为同家族首次公开，不为排除去遍历所有提交/版本。该日期问题与下文原文中央保证有效性分别记录。

## 可保留的机制与实验

论文组合入口 semantic firewall、tool-level RBAC、out-of-band human approval、基于可用工具集合的 enabledness 抽象状态图与定向随机 fuzzing。§6.3 Def1 把 enabled-tool 集合作抽象状态，§7.1 的 invariant harness 对可达转移寻找具体反例。§8 的公开 PoC 是 **12 个 MCP-style tools、12 条 regex firewall、纯 Python RBAC/TF-IDF router、确定性 mock 可替代 planner**；§8.3 的 seed42 日志在 buggy Document Sharing 图第 52 次找到 `accept_sharing_request` 重复作用的一个越权转移，修正图随后 500 次未见同一 invariant 失败。§10.5 另报 100 seeds 的发现次数中位数 52、范围 12–143。此证据可支持“在给定图、性质与探索策略下找到了该构造反例”，不能抹去可复现 PoC 的局部价值。

§9–10 还描述另一个 200 tools（120 read/60 write/20 critical）的模拟金融文档设置、10,000 初始 intent、最多 500,000 随机序列、Llama3-8B/GPT-4o/A100 等；它与离线 12-tool/500-iteration PoC 不是同一实现规模。Table3 的传统 REST 安全分母标 `N/A (theor.)`，不能读成等价系统下 0% vs 100% 的真实攻击对照；`920→145 LoC` 与 `16→3 days` 只属于此案例的工程估计，不证明 REST 本身不可安全部署或 MCP 因果节省。

## 中央保证的窄争议

摘要与 §10–11 将 500,000 随机序列的“100% hidden-transition discovery”、修正后图对设计图的“100% correspondence”及 PoC 500 次零失败，提升为**严格必要、完整形式验证、修正既必要又充分、所有 real-state compromise 为零**。这一步未被所给实验支持：要有全量发现率，必须先有独立枚举的真实隐藏转移分母；文中可核的是一个 seeded BOLA edge 与有限性质。500 次未发现只给该采样/性质的阴性结果，不是不可达证明，形式化的 enabledness 等价也没有替真实 resource ownership 与 effect 的完整状态表示背书。§12 自己承认 >200 交叉工具时两小时 timeout、严格密码学前提使 fuzzer 难进入某些分支、仅模拟金融文档。因而隔离的是**印刷的全覆盖/充分性/必要性及跨企业保证**，不是断言 PoC 实际未运行、规则必有泄漏或定向 fuzzing 无用。

Ch72 已把 IAM/RBAC、gateway、tool-local validation、canonical action、真实 effect 前授权和 outcome receipt 分账；也已有 guided fuzzer 用 assertion failure 作反证或 specification repair 的原则。这里没有足以新增 Books 的授权机制：EPA/fuzzer 属这些机制的一个测试实现，不能因论文以“形式”命名便取代 Ch72 的 effect owner。作者侧拟 `Design Delta 1 + System Reach 2 + Durability 2 = 5/9`；由于中央安全保证会误导发布判断，请按合同的 safety/correction override 作**窄深入／Disputed** 证据审阅，Books 暂为 `No Change — Existing Coverage`。**日期未通过时这些仅是同家族纠错证据，不得作为 04/29 正式正面候选计入。**需非作者定点核摘要、§8.3、§9–12 与 Ch72 上述相邻命题，并对早于本窗的 repo 初版公开状态作具名裁决；其通过不代签整日 Gate。若后续提供与抽象图独立的完整具体状态/性质证明及对照，方可重新评价中央保证。
