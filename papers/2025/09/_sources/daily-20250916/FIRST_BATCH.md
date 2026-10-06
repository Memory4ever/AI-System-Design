# 2025-09-16 首批准入交接（作者 Tesla，待 root 校准）

仅本日窗口 `2025-09-15T09:00:00+08:00` 至 `2025-09-16T09:00:00+08:00`。依据当前 RESEARCH_CONTRACT §3–6 与 REPORT_CONTRACTS §3.6；本文不另定义规则，不授准入或完成。

## 可复查发现

- `arxiv-theme.xml`：官方 API，submittedDate `[202509121800 TO 202509151800]`，题名主题 language model / Transformer / foundation model / diffusion / world model / vision language / GPU / LLM / agent；start=0，max_results=300，ascending；返回229条、单页已到 totalResults。它是提交区间线索，不是公开区间或全文队列。跨出目标主题的条目不扩大队列。
- 初次手工编码请求返回75935条总量且响应把日期结束值变成2509151800，未作为有效扫描或数量依据；改用上述实际保存的请求。此前输出没有完整保存，不冒称原件齐全。
- `arxiv-cl-month.html`：官方 2025-09月身份列表，1–2000/2214，未读其余月份材料，也不称全月检查；月表无逐日公告字段。`arxiv-cl-day.html` 的日期路径返回 Listing requires subject and valid time period parameters，不当作空公告。
- 官方入口与补检原文见 official-*.html、16official*.json、web-initial.json、16date.json。只恢复本日附近线索，当前页不是历史完整目录。

## 拟保留潜力（尚缺公开归属，不是正式当窗候选）

| 身份 | 原约束 → 摘要实际增量 → 待重考虑选择 |
| --- | --- |
| 2509.11076v1 | 固定operator序列的swap计划失效 → 在线profiling与执行匹配适应动态序列 → 何时能在eager训练用offload替代recompute。精确v1题名Chameleon，当前API题名SmartSwap不可替代历史稿。 |
| 2509.11155v1 | attention点积维度成本 → 校准SVD投影与query幅值选维 → 计算节省与KV降维边界。 |
| 2509.11628v1 | 扩散步间依赖 → forecast-then-verify特征缓存 → 可靠性判据是否真正控制质量/误差；不是LLM分布精确验证的自然延伸。 |
| 2509.11250v1 | 固定触发器位置评价失真 → 动态网站环境与attention引导攻击 → GUI注入的评价威胁模型需重选。 |
| 2509.11686v1 | execution trace应改善代码语义 → 摘要报告SFT/test-time增益有限 → 不能把可读执行轨迹自动当成有效训练信号。最新索引v3只作发现，原版本仍需核。 |
| 2509.11353v1 | reranker应按相关性排序 → 人工日期扰动的recency bias → 元数据与内容相关性需分开评价。 |
| 2509.11986v1 | connector能保持视觉能力的默认判断 → 邻域与重建检验定位信息损失 → 表示对齐评价不能只看最终VQA指标。 |
| 2509.12024v1 | heuristic概念删除无保证 → MI独立性/收敛/泄漏上界主张 → 须核理论假设与有限训练机制的桥接，不直接采用保证。 |
| OpenAI GPT-5-Codex release/card | 动态thinking与执行边界公开事实、477→500任务评价口径变化 → 预算及benchmark分母必须单独绑定；blog未披露训练配方。日期仅September15且时区不明，待可落窗区间。 |

## 代表性非候选判断供抽查

- 2509.10682v1：完整题摘为威胁分类和防护映射综述，未在题摘指出修正具体机制/混杂的新增证据；不是因为是综述一律排除。
- 2509.11656当前v3：完整题摘为MAD配置与评价框架，144种配置本身不构成新增设计取舍证据；如果原v1给出交互反证，定点重开。
- 2509.11524v1：完整题摘为推荐候选item的hidden-state匹配，领域目标空间换为候选集合；不支持通用LLM语言解码加速，范围切片停止，不否定其推荐学术价值。
- 2509.11101当前v3：350个情感案例的层级benchmark，题摘未指出足以改变模型/系统设计的混杂或可复用机制；v1若有设计反证需重开。
- Anthropic Economic Index：地理/企业采纳和自动化比例，不是模型能力形成或执行机制研究；保留经济背景，不进本项目候选。
- Claude4.1 card Sep15 changelog为CBRN合作方致谢（原文线索），无机制/安全结论变化；不以更新标签自动深审全卡。

## root 必须裁决

1. 独立核上述准入与排除依据，日期不能用submitted/DOI注册伪造首公开。
2. 是否取得本日官方公告或作者原始首发证据；仅有版本提交不能授本日candidate。
3. 后续正式候选证据、Books决定与日级复核仍归root。作者继续可用来源，不等待全五日结束才交接。

## 11:48 作者窄重开结果

root 已在相邻 `INDEPENDENT_CALIBRATION.md` 留独立首批校准；不把该结果当日期或完成批准。

- 11101：精确 v1 题名为 EmoBench-Reddit，不是当前索引的 Seeing is Not Understanding。v1 HTML完整摘要包含九个模型的感知/认知落差；§4.2 是感知正确率超过75%才评认知的 gated protocol，§6.2/Table1 是任务层级差异，不能推出感知导致认知的因果关系。撤销“350样本即无贡献”的关闭理由，保留评价反证潜力。abs 页标识 v2 withdrawn，但没有标识 v1 withdrawn；不把后版撤回标签自动搬到 v1，也不采用后版结论。日期未确认，未评分。
- 11656：v1 §4.2/Table1–3有响应格式、信息可见性、决策协议的局部实验，AppendixE给Llama3 8B/70B与3/5次重复。不是只有144配置目录；撤销原关闭。响应格式与任务交互是实际潜力，但voting/consensus结果部分引自Kaesberg2025，不能当全新证据家族；更快达成共识不等于更可靠。日期仍未确认。
- 10682仅关闭题摘未提出新增机制/混杂纠正的本次综述切片；11524仅关闭“据此宣称通用语言解码加速”的命题，其有限候选item替代输出设计保留原摘要，不因为应用领域自动否定。

精确原文与实际定点阅读保存在 `16reopen.json`、`16reopencore.json`、`16finalcore.json`；未复现。

## 12:26 新路由窄恢复：请root校准Codex release

见`NARROW_RECOVERY.md`及原RSS。Codex release首公开字段`Mon, 15 Sep 2025 10:00:00 GMT`已证明落窗；card的00:00 GMT窗外，旧表合并datehold已失效。核心说明已实际重读，拟准入理由：统一预算难同时适配短交互和长执行 → 此发布公开任务自适应thinking及短/长employee traffic相反资源分配、评价由477到500的分母变化 → 预算收益与可靠性评价须按任务分位和分母分开，不能照录单个节省比例。拟2+2+1=5，版本相关且控制策略未披露，不把成熟沙箱原则计新机制分。实际安全边界只限联网/审批/人工review公开事实，是否触发深入受影响内容请root裁决。未扩展全文或Books采用，未自授准入/完成。

同时完整核心关闭OpenAI消费者使用研究：实际增量是人口/使用分类和经济采纳，不是能力形成或执行机制。DeepSeek主站updates404保留，官方API Change Log实际恢复Sep22→Aug21，撤销“只首页shell且无可用历史”的旧判断。
