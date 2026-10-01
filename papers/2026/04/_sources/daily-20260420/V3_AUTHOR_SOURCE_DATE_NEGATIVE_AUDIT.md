# 04/20 来源、日期与负侧作者定点审校（不签独立 Gate）

本轮按 `RESEARCH_SOURCES.md` 的每日段与本日 README §2 实际逐 ID 比较：两边同为十四个 `SRC-*`，集合差为空；不纳入 Weekly。逐行重读本日[原始入口与停止记录](./v3-reopen-notes.md)前部及[三入口窄复查](./V3_THREE_SOURCE_STOPPOINT_REOPEN.md)。这是对已保存原响应范围/现存官方可见段的**作者核对**，不是重抓全部历史页，更不是站点全域零发布声明。

| 来源 | 本次核到的有效停点及不能推出的结论 |
| --- | --- |
| SRC-OPENAI | 新闻 RSS 邻界 Apr21 00Z→Hyatt Apr20 00Z→Codex Apr16 10Z，Hyatt 原文只部署案例；Research 历史分页仍无可证明本窗全目录的逐条响应，维持`受阻`，不写零命中。 |
| SRC-ANTHROPIC | 已保存 Research 71 条 `publishedOn`，邻界 Apr14 13:01Z→Apr22 14:12Z/14:27Z，所见列表窗内无条；不推全站。 |
| SRC-GOOGLE-AI | [Research April Blog](https://research.google/blog/2026/04/)九项所见 Apr16→Apr21；DeepMind page3 与 selected-research 的已存相邻段跨窗；Publications 年度 771 宽列表不提供本日首公开停点，维持`受阻`，Blog 不代替 Publications。 |
| SRC-META-AI | [Publications p2](https://ai.meta.com/results/?content_types%5B0%5D=publication&page=2)近期有序段 May19→Apr16→Apr14/9，后部混排旧推荐；Research SSR 未返回可靠逐条日期，维持`受阻`，仅限已见 Publications 段。 |
| SRC-QWEN | 动态 article API 40 条 `extra.date` 邻界 Apr18 10+08→Apr22 10+08；静态/仓库不因此视为全覆盖。 |
| SRC-DEEPSEEK | 已存 News16、Research 及组织索引邻界跨窗；只复用该目录，不宣称全部 commit/release 事件为空。 |
| SRC-MOONSHOT | kimi-cli 100 releases 邻界 Apr20 16:01Z（窗后）→Apr17 14:10Z；注册 Platform Blog 26 项最晚 2025 Nov7，只限这两个入口。 |
| SRC-TENCENT-HUNYUAN | 官方 `publicList` pageSize100 实返 total9/list9，Apr23→Feb13；可选 repo 子入口 403/限流不冒充全部仓库完成。 |
| SRC-ZAI | 已存 Research 15/16 条 Apr29→Apr7/1 与 release Jun16→Apr7/Feb12；可选 GitHub 403 独立限定。 |
| SRC-BYTEDANCE-SEED | Paper API page20 20项/total242，May12→Apr8；Blog API page0 实返15/total95，Apr22 16Z→Apr8 16Z。AgentWorld 卡片 Apr19 16Z 不等于那一刻公开正文，具名隔离，不全读242。 |
| SRC-BAIDU-ERNIE | 官方 Blog 两页十项 Apr30→Apr15→Feb6，2/2 页停止；不能推出未列模型仓库无变动。 |
| SRC-XIAOMI-MIMO | Paper8 项 Jun29→Mar13，Blog 现15卡，邻正文 MiMo-V2.5 Apr22 与 V2-Pro/Omni Mar18；卡本身无可靠日期，限所见排序/正文，不能称全机构零事件。 |
| SRC-MINIMAX | EN/CN Blog 12/13 条及 cli26 releases，cli 邻界 Apr26 01:40Z→Apr17 20:51Z；Agent Tech Blog 只有可见 May13 单页，仍限入口。 |
| SRC-ARXIV | 原 owner 收据实有447个跨分类去重身份（首15314/末16299），其中330同日 OAI direct、117后改/代理；不是447候选。150完整题摘／109工作候选／40具名前闭／15483隔离。原 OAI `cs` 04/20响应已存，不能把其734个 metadata header 当本项目贡献分母。cs.AR整月目录只补检，cs.CL原请求429限流，不能写全网无遗漏。 |

## 首公开联合链的本轮复查

重新读[arXiv 官方 availability](https://info.arxiv.org/help/availability.html)：投稿到公开有质控间隔，永久 ID 在 announcement 自动分配且不能倒填；Sunday Eastern 20:00 是常规公开槽，2026 holiday表不含 Apr19/20。这个 Sunday 20:00 EDT 对应 Apr20 00:00 UTC/08:00 北京，在本日报 `[Apr19 09, Apr20 09)` 内。再核原 owner receipt 实际 `identities.length=447`、first `15314` 的 v1 Updated `00:00:05Z`、last `16299` 的 `01:04:41Z`、330/117 分层；原 OAI `ListIdentifiers` 的 Apr20 datestamp 可定点见 15521、15621、15741、15760、15871 等，15622/15794 当前没有同日 OAI direct，其旧 receipt 是 DataCite initial-created 代理，仍需依公布时赋 ID、相邻批、v1 Updated 与全批 OAI共同推断，而非把代理字段单独改名 first-public。此前[联合链细节与具名隔离](./V3_DATE_RECONCILIATION.md)继续有效；本次未发现需要把新恢复七项迁日的官方早发反证，但这不是七篇逐个首次公开证书。15483 同 family 早发及 Seed AgentWorld 卡片仍隔离；若找到更早可靠公开正文，仅重开具名 family，不全版比较。

## 负侧分层作者样本及反向对照

从当前40关闭中取不同理由层，不以关闭率为目标。范围一般系统抽 [15475 NeuroMesh exact-v1 题摘](https://arxiv.org/abs/2604.15475v1)：异构空地机器人、Zenoh、GPU/CPU推理与 reduce/broadcast 抽象属机器人协作执行栈，未给 foundation/VLA 平台的新模型状态或推理控制条件；不能因框架名/“GPU”入本书。成熟逻辑抽 [15727 exact-v1 题摘](https://arxiv.org/abs/2604.15727v1)：五代数不变量/弱链规则是已知 possibilistic weakest-link 的 LLM scaffold 与性质测试；题摘的“能防推理不一致”不是新模型验证权威，不从100 properties 反推真实任务正确性。旧非作者已有 15475/16088/15343/15911/16070/16108 的定点核和15648/16056新闭源核，未把这些 PASS 转给未核项。

新关闭的原 peer 冲突抽 [15657 CovAgent exact-v1](https://arxiv.org/html/2604.15657v1) 与 [15802 CHOP exact-v1](https://arxiv.org/html/2604.15802v1)：前者不可达 coverage 与模型失败分账已有 Ch66 对应，且组合工具不分原因；后者的 top1 retrieval 提升而 generation F1 0.2760<0.2763，缺 prefix/CD 单独消融，难让索引 recipe 变可迁移答案合同。[15972 WORC](https://arxiv.org/html/2604.15972v1) 的低权重 quota 不识别 causal weak link、token 总预算未配，[15756 TTL](https://arxiv.org/html/2604.15756v1) 的文本 prefix/伪标签 bank 未给比已有在线适配污染责任新的保护条件，故维持具体关闭；原实验事实和负面数字均保留在[逐项裁决](./V3_NEGATIVE_11_AUTHOR_ADJUDICATION.md)。

反向正侧样本配对 [15549](./V3_15549_SCOPE_REOPEN_AUTHOR.md) 的无线冲突时隙×有向 mixing 联合选择、[15622](https://arxiv.org/html/2604.15622v1) 的低频语义/高频执行双时钟、[15871](https://arxiv.org/html/2604.15871v1) 的跨编辑接口三元语义比较、[15741](https://arxiv.org/html/2604.15741v1) 的更多 sensor 信号反退。它们也受小模型、受限任务或未匹配成本限制，但仍提供具体可选择对象/评价有效性条件，因此不能把“局部”作为关闭硬门槛。新增七恢复及四维持都还需非作者逆向核；本文件不代表40负侧全审或109候选全审。

同批再从不同新关闭家族抽四项官方 exact-v1 必要段并比对实际 owner：

- [15482 多目标 unlearning](https://arxiv.org/html/2604.15482v1) §3/§5.3：统一数据表示、邻域 anchor 与双向 top-k logit 蒸馏共同改动；Table2 以 DUET/BILD 替换有有限退步，但不独立识别三目标平衡中的唯一新约束。Ch72 已明确目标删除、邻域误拒、攻击恢复与 retain utility 分账，本文的三目标联合 recipe 未给新 artifact 发布权或超出现有测试矩阵的验收条件；继续具名前闭，不因为安全主题自动 Deep。若后有同预算/同训练数据的干预揭示旧合同漏项再重开。
- [15484 vstash](https://arxiv.org/html/2604.15484v1) §3/§6–7：SQLite/FTS5/vector/RRF 及 IDF 自适应 fusion 属可行本地检索实现；作者也保留 post-RRF 三种重排负结果。Table5 小语料中 hybrid 并非所有指标优于 vector（例如 NDCG@10 .803<.832），BEIR 不同 encoder、fine-tune、cutoff 不可合成融合独立收益。Ch76 已有 dense/lexical hybrid 与 query/index/reader 分账，此文未给新稳定适用条件；维持前闭，不把本地优先作为硬拒理由。
- [16145 Training Time Prediction](https://arxiv.org/html/2604.16145v1) §II–IV/脚注1/Fig2：图算子按实际 dtype profile 再合 DP/TP/PP，作者脚注明确预测量是 single iteration time，而非到质量阈值的 job ETA。8×H100 的有限 precision 对照说明静态 FP32 baseline 会错，但 Ch36 已要求目标硬件、dtype、step critical path profile 与漂移回退；没有新跨层控制或被改变的部署选择，维持前闭，不因“训练系统”词准入。
- [15873 Listener–Speaker](https://arxiv.org/html/2604.15873v1) §3–5/Table1/Table5：speaker 与 listener 的 task framing、提示和解析率不匹配；Claude Sonnet listener 仅5%可解析等故障影响角色分数，Table1 条件差又有正负反向。Ch66 已要求 scorer/prompt/parser 入 Evaluation Identity，此文不能以不等价信息集或小任务现象修正“judge≠generator”的既有命题，故维持前闭；不因语用领域或模型大小硬排，若同题同接口可解析配对反向再重开。

上述四项同属当前净新18前闭，并非四项独立同行 PASS；作者抽样发现其具体旧关闭理由在所读范围内仍成立，未外推其他14项。

**当前交接：**来源状态为11`已检查`+3`受阻`，不是14个无缺口；正式分母109/40/1，单篇 Evidence→owner 具名余19（root 新核15780/16067/15789/15726），七个作者恢复的准入与负侧分层、联合日期/十四来源的独立 Gate 待另一人。作者继续按受限证据修正具体问题，不称 `Complete`。
