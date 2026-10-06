# 12/25 首批非作者校准

复核者：主线程（非作者）；2026-10-02。范围：作者 `ADMISSION.md` 的边界处置与 ERNIE 普通负侧；不验收本日发现完整性。

实际独立打开 [ERNIE Blog](https://ernie.baidu.com/blog/zh/)、[MiniMax Blog](https://www.minimax.io/blog) 与 [Z.ai release 目录](https://docs.z.ai/release-notes/new-released)。目录能核到分别标注 12/23、12/23、12/22 的相邻事件，不能证明该机构所有研究的历史切片已处理。

- ERNIE 目录只提供排行宣传，当前贡献前关闭理由通过。不是因为评测研究整体无价值，而是没有呈现改变评价判断的具体机制/反证。未读单篇另附正文，不把抽检当全量。
- MiniMax M2.1 的正文贡献未判断完；不得按发布日期较早就声称已有有效审阅。只将它交其真实归属日期定点处理，不能移到 12/25 计数。
- GLM-4.7 目录日期不能证明 research 目录零命中，作者保留后者可执行发现，处置正确。
- Qwen 动态页本复核访问返回空正文，未独立确认 LoRA 核心说明；此项尚未授贡献/证据验收。作者有实际读取证据时给明确段落/官方内容入口，再定点复核。

arXiv 日粒度首次公告查询空结果不是零命中证据。官方月列表实际可访问的长格式入口为 `https://arxiv.org/list/cs.CL/2025-12`；主线程只打开第一页确认可用性，不声称恢复每日批次。作者按本日主题收窄发现，不把 1302 条整月标题转成逐项队列。2025 年假日仍需历史官方依据，当前 2026 假日表不可替代。

## 后续定点检查

实际独立打开 [Qwen 官方模型卡](https://huggingface.co/Qwen/Qwen-Image-Edit-2511)，重读 Showcase 第147～151行及相邻演示。贡献前关闭理由通过：当前说明仅支持所选 LoRA 内置的产品事实，未披露新增合入机制或使通用设计选择改变的受控边界，不以成熟 merge 原理补造新增贡献；不是因 Books 已覆盖而缩池。

实际顺读 `25/README.md` 六部分和14来源表，并运行 V3 校验通过。状态正确保持进行中，§5明确还有普通可执行发现、题摘和日期工作；没有日级通过。独立抽检目前为 ERNIE 与 Qwen 两个普通负侧，尚未复核后续新增潜在材料、全部来源停止点和 Books。2025 假日原始 Blog 已由主线程直接打开，排期计算无误；仍不授任何个体 ID 实际公告。

## Kimi CLI 0.68 准入与时间

主线程实际读取官方 release 完整 body，并独立请求 GitHub 官方 releases/tags/0.68 API，HTTP 200，`published_at=2025-12-24T12:40:22Z`，对应本窗 20:40:22+08。采用公开 release 字段而非 `created_at`；日期通过。release 明确引用 ACP 客户端托管 MCP、客户端 terminal 与 OAuth 管理三项，PR479 官方 API 的 Summary/Changes 已独立读到；PR521/522 网页访问失败不等于实现不存在。

贡献准入通过，评分 2+2+2=6 可接受：新增执行位置与 capability 条件是具体兼容性/授权约束，不把 OAuth 或 RPC 当新原理。深入范围只限受影响的 MCP 接入、terminal 分支、凭据管理与必要测试，不扩全部 release。不得从标题推出隔离、权限收缩或性能已被保证。

已定点读 Ch83 `Host、Client、Server`、`MCP 不等于 Tool Authorization`，其连接/授权分离与凭据 scope 原则已有具体覆盖；Ch78 副作用/幂等性段、Ch82/84 开头也已读。唯一主 owner 应优先 `AGENT-MCP`（Ch83），Tool Calling 只作 effect 接口。实际代理执行路径是否仍有长期增量，须待精确 tag 实现核验后决定，不因主题相近提前关闭 Books。

## 精确 0.68 实现的必要源审

主线程独立通过 GitHub contents API `ref=0.68` 读到以下原始位置；raw URL 一次连接失败后用可用官方 API，未无限重试。未部署、未运行其测试或做性能实验。

- [`acp/mcp.py`](https://github.com/MoonshotAI/kimi-cli/blob/0.68/src/kimi_cli/acp/mcp.py)，blob `b3acc6df0915123780fa3693249714310d3adcf0`，`acp_mcp_servers_to_mcp_config` / `_convert_acp_mcp_server`：ACP 客户端传入 HTTP/SSE/stdio 配置，转换成 FastMCP 配置。配合 [`soul/toolset.py`](https://github.com/MoonshotAI/kimi-cli/blob/0.68/src/kimi_cli/soul/toolset.py) 183–325，blob `a6e60e7aaa780ced933feebfc5d5652038f7ecfa`，CLI 自己创建 `fastmcp.Client`、列工具与管理连接。因此不能写为 MCP 工具一律在 ACP 客户端代理执行。
- [`acp/tools.py`](https://github.com/MoonshotAI/kimi-cli/blob/0.68/src/kimi_cli/acp/tools.py)，blob `2df57f1a857ee5d09fc21151f403bcb980dc1b68`，完整 `replace_tools` 与 `Terminal.__call__`：只有 local Kaos 且客户端声明 terminal 才替换 Shell；执行前仍有 runtime approval。生命周期明确涉及 session、terminal handle、等待、timeout kill、输出/退出状态和 finally release。静态路径支持责任分离，不证明任意客户端具备隔离或可靠清理。
- 精确 tag 的 OAuth 连接队列对缺本地 token 的远程 OAuth server 标记 unauthorized，不进入 pending 连接任务。PR479 的 `reset-auth` 只调用本地 `FileTokenStorage.clear`，不能称服务端 revoke；有 token 也不等于业务动作授权。未独立跑 auth/test 命令，未验证任意 SDK/server 组合。

受影响的配置、连接、执行与凭据路径获得定点源审；最终 Books 处置、实际测试覆盖与日级来源检查仍需作者交付，不将这次实现读取扩为全日报完成。

## 非写入者 POST：Kimi CLI 0.68 / Ch83

2026-10-02T18:30:29+08:00；复核会话 `019f44db-4f09-7ee1-8754-b88e0749f3a2`。本人不是报告25作者 Feynman，也不是Books writer root。窄范围为 `SF-2025-MOONSHOT-KIMI-CLI-0-68` 的实际写后语义检查；不验收Daily25全日、不扩论文池，不修改Books或25 README metadata/§6。

实际读取Ch83当前diff和正文98–115行：五类契约原段、adapter分责段、root新增两段与随后taxonomy边界/typed adapter段；读取Host/Client/Server与生命周期上文，以及Review notes末尾新增源注。Ch82开头责任/状态/通信分解及章末“下一章MCP不定义协作策略”、Ch84开头run/policy/effect/terminal evidence与registry/MCP交接也实际对读。ROADMAP的唯一主owner为 `AGENT-MCP`；定点family检索只命中Ch83正文和本章源注，没有同family的第二Books owner。

本复核独立请求官方GitHub contents API，`ref=d5ae5b809d19086db2d823ca6f1997bd68c3db2d`，三文件均成功读到完整源码，不只复述root记录；blob与先前root源审一致：

- [`acp/mcp.py`](https://github.com/MoonshotAI/kimi-cli/blob/d5ae5b809d19086db2d823ca6f1997bd68c3db2d/src/kimi_cli/acp/mcp.py)：`b3acc6df0915123780fa3693249714310d3adcf0`。HTTP/SSE的URL/header及stdio command/args/env转换为MCPConfig，说明ACP客户端是配置来源，不能推出它执行MCP连接。
- [`soul/toolset.py`](https://github.com/MoonshotAI/kimi-cli/blob/d5ae5b809d19086db2d823ca6f1997bd68c3db2d/src/kimi_cli/soul/toolset.py)：`a6e60e7aaa780ced933feebfc5d5652038f7ecfa`。CLI创建 `fastmcp.Client`，pending连接队列进入client context/list_tools；MCPTool另经runtime approval后 `client.call_tool`。正文区分配置/连接/动作执行正确，没有把全部MCP tools写成客户端代理执行。
- [`acp/tools.py`](https://github.com/MoonshotAI/kimi-cli/blob/d5ae5b809d19086db2d823ca6f1997bd68c3db2d/src/kimi_cli/acp/tools.py)：`2df57f1a857ee5d09fc21151f403bcb980dc1b68`。完整 `replace_tools` 和 `Terminal.__call__` 已读。非local Kaos直接return；terminal capability且已存在Shell才替换，沿用原name/description/params与runtime.approval。approval拒绝在 `create_terminal` 前返回；客户端终端经ACP session/tool-call/terminal handle关联执行，不是MCP配置转换的同一条路径。

生命周期核验：`asyncio.timeout` 包住wait_for_exit，TimeoutError显式 `terminal.kill()`；随后读取current_output、truncated与exit status；finally只尝试 `terminal.release()` 并suppress Exception。因此kill不等于release，release不自动证明取消/异常后进程已停，未知执行状态不能直接重试。正文保留这些非等价性与Ch81恢复/协调交接，没有宣称该实现已提供可靠终止、exactly-once、客户端隔离或工作环境/权限等价。同一schema只保留参数接口而非backend语义，边界正确。

POST结论：通过这两段及1条源注的窄语义检查。先说明单进程合并职责为何合理，再解释外部客户端改变责任边界、采用两条受条件约束的静态路径、列清新的生命周期成本与失败回退；是对原adapter/authorization链的融合，不是release功能清单。没有把通用Workflow恢复或Platform业务验收接管为Ch83第二owner。OAuth local-cache/revoke说明仅定点沿用root先前必要源审，本文未另跑auth；不把它当新增正文机制。

实际Books diff空白检查通过；这是机器格式检查，不是POST语义依据。未部署、未运行Kimi/ACP/OAuth/cancellation测试或benchmark。源注中“写后非作者复核待完成”是root写入时的停点，本追加记录现在完成本family POST；不越权改该Books源注，也不授Daily25完成。

## 安全与反证线索的独立范围检查

主线程独立读 [ZDI-25-1032](https://www.zerodayinitiative.com/advisories/ZDI-25-1032/) 全部披露说明与时间线。其 coordinated public release 和页面更新均为 2025-12-01；GHSA 后续收录不能制造 12/24 的新披露。漏洞需要加载恶意页面或文件，不能从 RCE 标签推出所有部署必受影响。此项按原披露关闭本窗归属，不把安全线索当普通宣传排除。

另独立读以下精确 v1 的完整题摘及 submission history，校准潜在贡献而不授首公开日期、正文证据或性能保证：

- [2512.19297v1](https://arxiv.org/abs/2512.19297v1)：无需原训练数据的合成覆盖、因果引导 LoRA 合入和训练后权重调整，是 adapter 供应链风险的具体机制线索，不能以低秩或 clean adapter 合入判为安全。
- [2512.19215v1](https://arxiv.org/abs/2512.19215v1)：语义保持的代码变换可隐藏后门触发，构成“异常词模式过滤足够”的局部反证；归一化只被报告为部分缓解。
- [2512.20168v1](https://arxiv.org/abs/2512.20168v1)：输入与输出双向图像隐写针对只审可见恶意意图的安全假设；不是任意多模态产品都被攻破的证明。
- [2512.19238v1](https://arxiv.org/abs/2512.19238v1)：93 类污名身份、37 场景和三组模型/guardrail 的具体评价设计；总体偏差下降与相关因素仍存可以同时成立，不能把 guardrail 过滤通过等同公平性。

四项题摘足以保留准入信号，不能代替方法、控制与失败边界深审。Submitted 为 12/22 或 12/23，不等于公众首次可访问；与 DISCOVERY 的必要公告恢复缺口一致，保持隔离、不进入本窗确定候选或 Books。此检查没有把题摘中的攻击率或改善数字采用为已核实性能结论。

## 已发现的十三条追加线索补正

DISCOVERY 原来把下列相关标题列为“未完成贡献判断”并先隔离日期，存在普通可执行题摘未处理。主线程已实际打开每个 v1 题摘和版本历史，完成定点补正；不扩整月库存。最初打开的 PHOTON/Laser/CRAFT/KPI 页面是后续版本，随后明确改读 v1，下列判断不采用后续版本结果。

| 精确身份 | 初筛判断与待恢复问题 |
| --- | --- |
| [2512.20798v1](https://arxiv.org/abs/2512.20798v1) | 潜在：同场景直接命令与 KPI 激励分开评价，能暴露任务成功与约束遵守的分离；不从摘要违反率推断所有部署 |
| [2512.20687v1](https://arxiv.org/abs/2512.20687v1) | 潜在：底向上低频 latent 与顶向下重构改变 KV 访问粒度；v1 未使用 v2 的 recursive generation 新说法，不采用巨大吞吐数字 |
| [2512.20458v1](https://arxiv.org/abs/2512.20458v1) | 潜在：三类结构化 action 与紧凑 context register 联动，而非只加长上下文；需控制协议与压缩各自贡献 |
| [2512.20362v1](https://arxiv.org/abs/2512.20362v1) | 潜在：依赖结构视觉约束、VLM 检查、定点改写和显式停止；judge 假阳性、循环成本仍需必要正文核验 |
| [2512.20278v1](https://arxiv.org/abs/2512.20278v1) | 潜在但局部：工具发现、返回结构验证、state anchoring 与并发持久化的具体 skill 生成案例；单个 Outlook/OneDrive 案例不支持通用 production-grade 保证 |
| [2512.20184v1](https://arxiv.org/abs/2512.20184v1) | 潜在：对随机推理定义 refinement 与 quorum 早停，区分 transient agreement 与协议保证；共识安全不等于数学答案真实正确 |
| [2512.20111v1](https://arxiv.org/abs/2512.20111v1) | 潜在反证：belief bottleneck 降低历史内存却会传播更新错误，RL 对 belief 质量/长度施加信号；摘要已明确原瓶颈性能可低于全文历史 |
| [2512.20092v1](https://arxiv.org/abs/2512.20092v1) | 潜在：粗筛后学习证据 session 选择，同时奖励答案、grounding、时间一致性；需确认奖励与测试的泄漏边界 |
| [2512.20083v1](https://arxiv.org/abs/2512.20083v1) | 潜在设计反证：任务成功仍可能计划低效，以四类 metamorphic 关系检查非功能最优性；只限 AI2-THOR 条件，非全局最优证明 |
| [2512.19539v1](https://arxiv.org/abs/2512.19539v1) | 潜在：动态关键帧 memory、latent 拼接和负 RoPE 位移以 LoRA 改造单镜头生成；跨镜头一致性不能替代真实动力学正确性 |
| [2512.19432v1](https://arxiv.org/abs/2512.19432v1) | 潜在：可恢复移动环境、后端验证、澄清用户与 MCP 混合操作让 GUI 成功率不再单独代表任务能力；不用 v3 替代 v1 |
| [2512.19234v1](https://arxiv.org/abs/2512.19234v1) | 潜在：长时净收益与截止时间、费用、电量和交互约束联合评价，而非简单走到终点；仅模拟城市，不把标题 Real World 当现实部署 |
| [2512.19154v1](https://arxiv.org/abs/2512.19154v1) | 潜在：自适应保留能预测未来奖励的旧观察，相比固定 frame stacking 改变计算/记忆压力；理论收敛仍需核假设，不外推 LLM 全任务 |

十三项均保留具体贡献信号；已读题摘不是精确正文完成。原必要首次公告恢复仍缺，暂不评分为本窗确定候选，不进入 Books、不支持 Coverage/Evidence 正面断言。收到逐 ID 原始 new/RSS/email 或可核实作者首次公开范围后，只重开该身份与真实归属日。当前题摘普通待办已补正，不把未读题摘包装成外部材料缺失。

已逐行核对 DISCOVERY 与本日报十四源停止位置。独立原始抽查 Meta Publications page3，实际返回 12/26 安全博弈、12/18 水印、12/16 SAM 及混入旧置顶记录，与作者非严格排序边界相符。DeepSeek updates 本次 web 返回错误，保留此前作者原始邻接，不冒称本次独立读到。必要历史目录缺口有具名入口、有限替代与重开条件，不作本窗零事件证明。日级最终结论尚需 Ch83 写后独立检查。

## 可恢复的 Blog 范围补正与最终结论

追加复核撤销此前 Google/Seed 的过宽隔离，不以“原入口失败”跳过已知可用原始恢复路径。主线程实际独立访问以下入口：

- Seed 官方公开 API `https://seed.bytedance.com/api/get_article_list_v2?article_type=2&publish_year=2025&count=20&page_token=0&order_desc=true`，header `x-tt-locale: US`。本次实际18条、total45、has_more=true、next20，不沿用其他时刻的15/49。置顶五项分别为 Seed Prover1.5 12/24、Seed1.8 12/18、Seedance 12/16、GR-RL 12/02、DepthAnything3 11/27；随后非置顶/置顶混合下降至6/25。只检查目标邻接并停于已越过本窗的显示段，不保证全站历史全集。
- [Seed Prover1.5 官方完整核心说明](https://seed.bytedance.com/en/blog/seed-prover-1-5-advanced-mathematical-reasoning-through-a-novel-agentic-architecture)第1–2节：whole-proof/step-proof的失败压力→工具调用与可复用已核lemma→结构/局部数学检查/rubric多信号sketch奖励→递归分解和并行证明。潜在贡献成立；不采用竞赛成绩或算力收益，也不把Lean结构通过等同待证lemma已证明。它是模型/Agent推理机制，不按数学题材整体排除为AI for Science。原站路由字段与列表均为 `PublishDate=1766505600000`（12/24北京00:00日编码），`UpdateTime=1789717565000` 是后来更新。没有可核实精确上线时刻；展示整天与本窗相交而非完全落窗，保留该具名日期/历史正文缺口，不新增确定候选或写Books。不能把ID推为发布时间。
- [DeepMind `/blog/page/4/`](https://deepmind.google/blog/page/4/)实际24个条目，跨2026-02至2025-11。最新December为Google年度回顾；独立打开原文明确12/23，核心为既有事件回顾，不当新机制或12/24新增。随后Gemma Scope2、Genesis、Gemini3Flash、audio、UK两项、FACTS、作物研究，邻接与17日SOURCE_STOPS的原始日期记录相符。恢复这段Blog，不再声称DeepMind历史Blog完全不可得；Google publications的年粒度缺口仍未恢复。
- [Anthropic Alignment Blog](https://alignment.anthropic.com/)真实December段含Bloom/Activation Oracles、alignment-faking、replication、Fellows、knowledge localization，下接November；复用17日SOURCE_STOPS对应原文12/19→12/08日期观察，不把它扩为Research全目录无遗漏。最新December具名条目在本窗之前，主Research旧分页仍隔离。

Books的实际改动已由非写入者Mill定点源审和写后检查通过。当前本窗确认候选1，受影响兼容/授权证据深入完成、AGENT-MCP整合完成；追加Blog/题摘普通工作已补正。外部保留逐项隔离且有定点恢复条件，不授Coverage或Evidence正面证明。日级复核结论：通过安全终态；无全来源零事件或遗漏保证。
