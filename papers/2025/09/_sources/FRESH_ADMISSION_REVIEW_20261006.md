# 2025 年 9 月首批独立准入与日期复核

复核者：`/root/fresh_review`，不参与作者写作。执行日：2026-10-06。只适用于本页列出的 2025 身份，不继承 2026 的验收结果。已重读 AGENTS、CODEX_RESEARCH_PROMPT、三个 canonical 研究合同/来源、ROADMAP；未修改 Books、共享索引或 LEARNING_STATE。

## 1. 公告日期组合：批次线索与日窗归属分开

实际读取官方历史文件 `official-calendar/availability-before-20250903.md` 与 `provenance.json`。exact commit 为 `95c71658adbaa987dc2ba1105ef9c5201ecde4ce`，2025-08-06。原文说 final arXiv identifier 在 work announced 的自动处理过程中分配，不可能提前获得 identifier 或 DOI；identifier 月份不能回填。原文也给出 Eastern US 14:00 cutoff、20:00 announcement schedule，列明 2025-09-01 holiday，并说明 moderation 与 ad hoc deferred mailings。本文不把 submitted、Updated、registry created/registered 改名为 announcement。

实际解压阅读 09-03 的九项 DataCite 原始记录（八个 `<ID>.datacite.json.gz` 及 `datacite-ui.raw.gz`）。九项 v1 Submitted 都在 2025-09-02 UTC，created 在 2025-09-03 04:12–04:23 UTC。final DOI 已在 registry 存在，结合官方不能提前分配政策，支持 announcement process 最迟已经发生的上界；它本身不是正文公告时间字段。九项身份逐一匹配 DOI、arXiv URL、标题和 v1，不用其他条目的时间代替。

| 身份 | v1 Submitted（UTC） | registry created（UTC） | registry registered（UTC） |
| --- | --- | --- | --- |
| 2509.02075 | Sep 2 08:26:18 | Sep 3 04:12:01 | Sep 3 04:12:02 |
| 2509.02175 | Sep 2 10:32:58 | Sep 3 04:14:25 | Sep 3 04:14:26 |
| 2509.02333 | Sep 2 14:01:07 | Sep 3 04:18:13 | Sep 3 04:18:14 |
| 2509.02444 | Sep 2 15:48:21 | Sep 3 04:20:49 | Sep 3 04:20:50 |
| 2509.02464 | Sep 2 16:18:40 | Sep 3 04:21:18 | Sep 3 04:21:18 |
| 2509.02492 | Sep 2 16:41:07 | Sep 3 04:21:57 | Sep 3 04:21:57 |
| 2509.02510 | Sep 2 17:02:29 | Sep 3 04:22:22 | Sep 3 04:22:22 |
| 2509.02522 | Sep 2 17:22:46 | Sep 3 04:22:39 | Sep 3 04:22:40 |
| 2509.02544 | Sep 2 17:44:45 | Sep 3 04:23:11 | Sep 3 04:23:12 |

已向 root 和 09-03 作者提出尚需解决的边界：区间内只有一个**名义** scheduled slot（Sep 2 Tuesday 20:00 EDT = Sep 3 00:00 UTC），但该名义时间不能直接改写为精确首次公开时间。Daily 09-03 截止 Sep 3 01:00 UTC，registry 上界越过截止；八项 v1 Updated 在 Sep 3 01:54–02:21 UTC，02175 的 v1 Updated 更晚到 Sep 4，说明 Updated 更不能当 first public。合同 §3.3 要求日期范围完全在窗口内。应由官方批次/公开证据确定日归属；若作者采用 schedule 推导，需回答批次标签是否证明实际公开在截止前，不能用日期推断隐藏本问题。此处不是宣称实际延迟已经发生，也不要求证明世界上不存在例外。

09-01 月 namespace 只限定 first announcement 的月份；官方段落未说明该月份时区，不能默认得到 Sep1 00:00 UTC 下界。09-01 作者恢复的首条 Sep1 registry 记录仍为 `2508.21073`（created Sep1 01:18:19 UTC），是月份 UTC 推断的实际反例线索。仍须与该身份的可靠上界和公告依据组合后才判断具体日窗。submitted 只提供正文不可能更早公开的下界，不由它单独套 schedule 得出 final public。

09-03 `datacite-created-sep3-page1.json.gz` 实有 1000 条，meta total=2566、totalPages=3、page=1；该页不是完整 Sep3 registry 覆盖，更不是官方当日 arXiv announcement list。

## 2. 09-03 首批机制准入

实际读取 TopH/DCPO/PACS/AppCopilot/UI-TARS-2 的 exact-v1 abs HTML 完整摘要、版本历史；AppCopilot 另实际读取 exact-v1 PDF 提取文本 §4.2.2（L2517–2555）。以下 PASS 只通过贡献口径，不代替日期、证据审阅、Books 或整日报完成。

| 身份 | 独立判定与原始增量 | 证据边界 |
| --- | --- | --- |
| TopH 2509.02510 | 准入 PASS：将 truncated sampling 写为 entropy-constrained minimum divergence，并给出等价 mass maximization 与 greedy 选择，值得核验分布整体熵约束能否改变 min-p 单 top-token confidence 的截断取舍。 | 摘要的 NP-hard、25.63%、LLM judge 不作为独立验证；须核 exact-v1 的熵定义、求解近似与同预算质量对照。 |
| DCPO 2509.02333 | 准入 PASS：token prior probability 相关的动态 clipping 和跨累计 steps 的 smooth advantage standardization，针对固定 clip/同分组零梯度两条路径。 | 不由 benchmark 汇总推出任一组件独立造成收益；zero-gradient 定义、优化偏差、组件消融待正文。 |
| PACS 2509.02522 | 准入 PASS：把 outcome reward 当 label，在 policy-parametrized score 上用 cross entropy，经 gradient analysis 连接 PG 与 implicit actor/critic coupling。 | 不将 pass@256 当单次可靠性，不从摘要推出监督学习普遍替代 RL；score/梯度成立条件和基线预算待正文。 |
| AppCopilot 2509.02444 | 从泛模块组合排除改为准入 PASS：bbox 外点击投到最近 widget center；以 frame perceptual hash 记录失败的已校正点击，再次命中则绕过校正执行原坐标。补偿器自身重复错误提供可定位的机制与 fallback 分支。 | 原文依赖有效互动会带来 UI state change 的假设；hash/坐标 identity、反馈有效性与独立消融未核，不承诺语义正确、fallback 安全或普遍终止。 |
| UI-TARS-2 2509.02544 | 原题摘支持进入定点方法核验：multi-turn RL stability、hybrid environment 与 sandbox 不是仅凭模块名即可 PASS 的新机制结论。 | 尚未在本次读取正文，需作者指出稳定训练/环境可靠性的具体增量后独立验收。 |

AppCopilot 原来仅依据题摘中的 CoT/planning/multi-agent/full-stack 泛列表排除，补读方法已揭示具体增量；该代表样本不能继续作为组合即排除的终判。已通知作者和 root，采用链仍受日期与有效性边界约束。

## 3. 09-01 有界贡献校准

实际读取作者 `01/_sources/admission-calibration.md` 和下列保存的完整 current 题摘（00030 为 exact-v1）。校准 7 条潜在正线索与 3 条代表排除，不冒充全窗候选分母或 exact-v1 全量验收。

- 00027 参数携带数据/导出时 layer-wise fine-tune 防护：主线关系成立，医疗仅为实验负载；adaptive attack 和效用边界待正文。
- 00031 forward-only zeroth-order QAT、冻结/预量化状态：具体资源设计分支成立；当前 v2 的手机/8GB claims 不得转用为 v1 事实。
- 00036 diffusion→flow velocity 重参数化及 residual variation suppression：少 NFE solver 的具体分支成立；current AAAI26/v2 与 exact-v1 分开。
- 00046 谱分布统计与 Gaussian/Pareto LoRA 初始化塑形：可核验的初始化增量成立，不把相关统计宣称因果规律。
- 00072 同源资料的问题构造改变时间性能曲线：设计反证线索成立，但 current v4 的 LiveCodeBench/影响函数不能替代 v1；v2 withdrawn、v3/v4 恢复需实际原说明处理，不采用被撤回版本。
- 00079 token uncertainty report 回授、阈值触发一次 refinement：选择性反馈分支成立，成本质量协议待核，不能从摘要推广 production。
- 00105 compression algorithm/rate/device placement 联立选择：KV storage hierarchy 的实际设计分支成立，v1/current v2 分开。

代表排除暂通过：00038 将 declarative prompt optimisation 适配 SLR 且题摘未给新机制/边界；00030v1 专用手势/拼写/唇读 predictor + 轻量 fusion + LLM 的摘要只证明任务收益，未给新异步融合适用条件；00071 RTL DCG diffusion/修补/MCTS 的摘要没有直接支撑大模型生成主线的设计边界。排除判定针对这些原题摘，不能推广成所有 SLR、异步多模态或图生成研究的门槛。

## 当前状态

已核材料的贡献校准可以继续逐项推进。日期链仍有上述具体待解边界，未验收任一 Daily 完成。无冻结候选数、无 Books 完成声明。本页将按新证据追加，不由旧 receipt 默认通过。

## 4. 09-02 exact-v1 校准补充

实际读取 `02/_sources/source-screening.md` 及其八份完整 `.abstract.txt`，未将这个局部样本当本日候选分母。

- ZeroQAT/A-FloPS/AdaptCache：exact-v1 与前述机制关系一致，准入 PASS pending date/正文；ZeroQAT v1 的实际增量为 forward-only 梯度估计及 jointly learned quantized weights/clipping thresholds/equivalent transformations，v1 摘要没有 current v2 手机与 8GB 结果。
- Learn to Shard 2509.00217v1：联合 coarse parallelism degrees 与 per-operator sharding 搜索，elite-history attention policy 是可定位的增量，准入 PASS pending date/正文。原摘要与 Megatron heuristics 相比只为 1.06×，不能用 metaheuristic 基线 3.5× 抬升为普遍生产收益；硬件、SLO、搜索预算与跨策略比较待核。
- 2509.00072v1，精确题名 **Beyond Memorization: Reasoning-Driven Synthesis as a Mitigation Strategy Against Benchmark Contamination**：v1 实际为 20,277 papers 合成 1,643 multi-step QA 的纵向评价，未见显著 cutoff 附近衰减；与此前直接抽题研究比较仅支持评价信号失效的核验，不是同源问题改写的受控因果证据。当前 v4 改题为 Test of Time，其同源转换/影响函数是变化了的中心证据，已向两位作者明确纠正，不用其解释 v1。
- MODE 2509.00100v1：贡献排除 PASS，原摘要 cluster/centroid/top-cluster routing 在 100–500 chunks 的收益与粒度/召回取舍没有超出成熟粗索引原则的具体新边界；不因负载小而排除。
- UDR 2509.00244v1：贡献排除 PASS，custom editable strategy wrapper 和 minimal/expansive/intensive UI 示例未给新增执行约束或失效证据。
- Brain-inspired replay 2509.00047v1：范围内，不能凭 CIFAR-100、小模型或负面结果关闭。摘要提供 internal replay 单独/加 SI 的 forgetting 与 initial-task accuracy 代价，以及 likelihood/reconstruction/silhouette/UMAP 的 latent overlap 线索，足以进入定点核验这是否新增可信的表示失效边界。尚不能由这些摘要断言 overlap 造成 accuracy 损失；作者应核相对原 BIR/SI 是否超出既有 stability/plasticity 复述，证据若不支持再明确关闭。

09-02 来源笔记准确区分 API submission metadata、可见目录与未读分页；仅 HTTP200 的 Meta/Hunyuan 品牌空壳没有记零。Google 46 页在此前记录时尚未抓完，后续机械抓取已完成，676标题的日期/语义仍待办；DeepSeek 展开、Seed 年份/页、MiniMax 真分页仍为待办。OpenAI Sep2 helpful 的 RSS 原值为 Sep2 04:00 GMT，明确晚于 09-02 窗结束 Sep2 01:00 UTC，应交真实 09-03 归属核验；此阶段尚未读该文正文，后续独立抽检见最终 checkpoint 记录。

## 5. 09-02 checkpoint 独立事实复核

实际读取 `02/_sources/RESUME_CHECKPOINT_20261006.md`，独立核原始 OpenAI gzip XML 与解析记录、Anthropic 原始解析目录、Google 抓取日志/title JSON。原始 RSS 正确解压到 XML，1247 items，无 `rel=next`；1247 pubDate 均可解析，09-02 UTC 日窗内为零，前一项 Aug28 10:00 UTC、后一项 Sep2 04:00 UTC helpful。只证明该完整 RSS 所呈现的本窗记录，无全站绝无遗漏声明。Anthropic 174 目录记录，最早 2021-12-01、最新 2026-10-01，Aug27 与 Sep5 边界吻合，只覆盖 Research。

Google 46 条实际请求日志，各 page1–46 为 GET200；title JSON 为 676 条，作者保留 filter677 差额未核及尚未逐项日期/语义的事实，没有伪造候选。两个作者 MD 内部链接实际存在，09-02 README 不存在。

结论：**09-02 受协调停止的恢复 checkpoint 事实复核通过，Daily 研究未完成。** 此通过不关闭 arXiv actual 公告日缺口，不将 holiday mailing 延期推成 actual zero，也不把 Meta/Hunyuan 空壳或未读目录记零。普通可执行待办仍在，作者没有宣称工作穷尽、评分、冻结候选、Books 完成或完整 V3 验收。

后续增量实际读 `2509.00072v1-abs.html.gz` 与 `2509.00072v2-abs.html.gz`：v1 原题为 Beyond Memorization，页首只说 newer version withdrawn；v2 页首 This paper withdrawn、No PDF、Withdrawn/no license，history 为 Oct6 2025 14:10:14 UTC，原页未给撤回原因。后续 v3/v4 恢复不自动消除该真实纠错信号。作者修后两个 MD 版本/标题事实通过；不把 v1 自身或整个 family 说成已撤回，不采用 v4 主张支持 v1，撤回理由仍是后续正面采用前的必要问题。

后续最终三日报恢复点事实复核见 [FRESH_CHECKPOINT_REVIEW_20261006.md](FRESH_CHECKPOINT_REVIEW_20261006.md)。09-03三页 registry 已完成机械恢复，原 §1 page1 的说明只描述该首屏校准时点；最终为2566 unique身份，仍未成为日窗池。OpenAI两文正文抽检及实际已存在保护行为限定均已核；没有将未来敏感路由计划当作已生效，也没有把全篇概括为无实际保护行为。
