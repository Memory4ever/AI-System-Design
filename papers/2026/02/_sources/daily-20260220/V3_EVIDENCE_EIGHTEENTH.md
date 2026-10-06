# 02/20 第十八有限包停点（执行方式审计中）

既有16346/16424/16429/16485潜力，不新增家族；用户要求审计耗时后暂停展开下一步，保存实际读到哪里，不将方法读过当Evidence完成。当前本日69终态=42整合POST+10争议隔离+4已有覆盖+13仅报告；27普通尚未闭合，本包4在其中，无Books lease/待写/POST。

位置为本日 `V3_extract_html.py < V3_REVIEW_2602.IDv1.html | awk 'NF' | nl -ba`，16485用`V3_CORE_2602.16485v1.html`。已通过先前准入/一次core可复用，不重排宽库存。

- **16346 Helpful to a Fault**：完整AB92、§3方法125–154、§4开头155–167已实际读。原singleprompt/固定成功率→sequential多phase达到harm目标与time-to-first-jailbreak→评价需分开task完成、turn exposure与攻击成本，不因只是四agent名称入选。下一只必要§4.2的censor/RMJD定义、§5比较预算与§6/7直接反侧、actualowner。尚未授实验/日期/Books。
- **16424 Verifiable Semantics**：完整AB46；认证算法尾117–139、Theorem1 140–142、coreguard定义/Prop1 143–151、drift/recert/renegotiation152–161、模拟162–192实际读。原协议语法有效不证明共同解释→共享observable event verdict/coverage与有限certified vocabulary→需限制semantic-support域而非把通信成功当理解。当前中心理论疑问：per-term约束不能自动给任意core-only decision rules同结论，相同term值但不同组合rule仍可不一致；多term联合使用也未见组合条件。Wilson普通近似interval不直接授exact有限样本保证，不能据cert名授worldtruth。下一只直接LLM协议/限制和actualowner以判中心暂缓或窄方法处置，不展开其他附件。
- **16429 TabAgent**：完整AB108–112；§3.1/3.2 143–155及160–177实际读（156–159输出截断，不能记已完整读；此前一次core143–170已有有效记录，可核实复用）。原闭集每次generative shortlist昂贵→successful-trace state/dependency features+context/candidate pointwise head→可考虑冻结外层执行，仅替head，但其605 successful CUGA、实际used tools非独立GT限定coverage。三模块名字/成熟schema checks不是准入依据。下一最小controlled结果、成本是否仅shortlist、失败/新catalog重训条件及actualowner；不按全部附录补读。
- **16485 Team of Thoughts**：完整AB58；§3 105–140实际读，与先前once-core§3/4.1/Table2/4.2校准记录复用。原按general能力/最大模型固定controller→GT validation accuracy分别测orchestration与tool类别proficiency、固定美元预算角色选择→选择需按角色而非把同一benchmark能力当协调能力。self-assessment为validation score非自报confidence，不由heterogeneous模型保证independent prior/广覆盖。下一必要§4有限role/profile对照与预算/heldout限制、actualowner；未授headline精度或latency。

## 本次真实低效与恢复说明

本包16429/16485的部分方法已在准入once-core读过，身份/命题无变化，再读相同段并非合同要求；恢复应复用，而不是再次完成一个固定全方法流程。当前多次长输出遭截断后补读局部，属于避免伪造阅读的修复，但可用先定位section、每调用小段控制输出减少这类重复。第十六三实际写后/root复核有效，本包不重审。

最近第十六Ch66与21作者实际文件操作短时冲突：21通知1–2分钟内释放，我先写Ch23并继续第十七必要源，没有阻塞sleep；释放后一次patch两个不重叠段，随后actualPOST均通过。目前无锁或等待root的可执行依赖；用户的执行方式审计是本停点原因，不宣称日级完成，也未扩大到其他日。

## 2026-10-05 fresh 恢复：必要评价与具体 owner（待 root 批次独核）

复用上文实际 core 和已通过准入，不重扫宽库存。官方 exact-v1 event 页分别定点核身份/版本；16346 当前有后续版本但未见撤回告示，v2 的 Submitted/Updated 均不能证明本窗重要修订，不以版本号自动重审。16429 仍 v1；16485 后续 v2 不回填本窗。以下日期复用本日首包官方 announcement→DOI 注册桥接：下界均 2026-02-19T09:00:00+08:00；对应 same-ID Registered 加 1 秒的上界分别 16346 **10:44:01**、16424 **10:45:51**、16429 **10:45:58**、16485 **10:47:20**，均含起点、不含终点；原 Submitted/Registered 字段保存于各 `V3_DATACITE_2602.ID.json`，不把注册当精确公告点。

### 16346v1 — Helpful to a Fault：拟仅报告，2+2+2=6，安全反侧深入

新增实际阅读 extract165–342、353–397、452–469，复用125–167方法：§4.2 的 first-event 是**tested-strategy index**，不是实际 turn、wall time 或 token。RMJD=Σ Dis(s)，数值越大表示在给定 strategy horizon 内更早/更多被攻破；同 Smax 下曲线面积不独立解决每策略成本不同。§5 的 AgentHarm 公共44 base behaviors×4 variants=176 instances，七语言中三个 target，另两个仅英语；Gemini3Pro strategy、Qwen3Next attacker/refusal/intent judges，后者4×A10080GB/vLLM；target temperature 0（GPT5.1 为1），默认 reasoning。precision、每请求端到端 latency/cost、统一实际 token/call、SLO 未披露；它们不构成本文吞吐研究。

STING最多10 strategies×10 turns，X-Teaming最多5 strategies；Table1另给 STING5 与 X5 同策略上限的 AHS，但两者 jailbreak 定义不同，作者明示不比较ASR。因此不授 headline 纯机制因果倍数，也不能称所有内部调用预算匹配。AHS是每instance跨实际策略取最大，ASR是judge认定全phase完成；二者不同。未成功在Smax右删失，KM/Greenwood曲线仅此有限攻击分布；有限语言hazard并不单调。Urdu/Telugu人工子样本 refusal P/R=0.96/0.71（83）、intent=1/0.97（56），不等全部judge无误；benign capability 对照只排除一个局部替代解释。原§7 GPT5.1 medium较high安全、stronger adaptive attackers仍future，均保留。

实际比较 **PLATFORM-EVALUATION-SYSTEM Ch66:2005–2019** 的 risk(N)、首次time-to-compromise/survival/hazard 和 threat-model限制，**3894–3900** 的 observation horizon/删失，以及 **4122** 的turn/retry/strategy/judge预算：已经承载拟保留的长期判断，不声称覆盖STING全部配方或RMJD名称。此次特定面积指标与局部多语言结果不足以更改这些设计选择，拟**仅报告**，不为补metric名称改书；安全测量实际证据保留，不改判贡献排除。

### 16424v1 — Verifiable Semantics：争议 / 暂缓终态（root 已单篇独核）

精确复用 [单篇 semantic checkpoint](V3_16424_SEMANTIC_BOUNDARY_CHECKPOINT.md) 的实际§5.3/6.1与Ch82/83比较；其结尾已有root原源100–225/owner实际独核通过。单词值一致不能给任意不同decision rules同结论；组合与Wilson finite-sample保证桥接未修复。toy同Qwen两LoRA、六词→两词和50heldout events只作描述，不采用51%普遍收益。评分沿2+1+2=5，中心深入审阅的争议终态，不写Books；重开只需共享执行规则、组合失败条件及正确统计命题/假设，不展开全部revision/附件。同步README该项不等待重复独核，不授整日Gate。

### 16429v1 — TabAgent：拟窄整合，2+2+2=6

复用143–177 actual core；补读147–178、Table1/§4.3/§5/§6的320–381。训练数据只含605个成功CUGA任务，label是canonical成功解实际used tool set，不是所有有效动作的独立GT；task-level5fold，所有同task feature/synthetic保持同fold，stochastic baseline每task5seed。每candidate10synthetic；same-e5 DSR real/+synth作为retrieval对照，显示closed-set pointwise head可替shortlisting接口。Real+synth P@R并非单调，Spotify0.70→0.61，novel tool composition约4%测试任务generative更好。CodeAct文本与CUGA rich features来源同时不同，SHAP不证明唯一feature因果。

2.682ms/巨大倍数是**head per-read**，不等完整Agent：TabSchema extraction、catalog scoring、feature refresh、45s MAC Pro CPU训练、synthetic生成/审阅需分账；正文headline95%/85–91%无足够匹配成本权限，本轮不引用。runtime硬件细项、precision/batch/concurrency/端到端SLO Not Disclosed。不能继承成功trace为当前tool version/新目录授权，fallback检测与新工具覆盖正式标准仍future。

实际 **AGENT-TOOL-CALLING Ch78:190–205** 已有检索→shortlist→schema exposure及可修订frontier；**150–165** 参数工具分支与**528** recall/confusion不承载从成功trace的state/dependency到pointwise discriminative head的替代接口。拟在schema version段后增加一窄段：固定可枚举目录中，保留外层执行链，把历史trace的schema/state/dependency特征与candidate身份输入小head；评分只是shortlist proposal，版本/权限/effect检查不迁入head。明确成功trace标签不穷尽所有有效tool，novel composition、catalog drift需回退generative/explicit schema；成本分为feature生成/训练和局部head/整链。不是新结构候选。

### 16485v1 — Team of Thoughts：拟窄整合，2+1+2=5

复用§3 105–140和once-core§4.1/4.2；补读140–327。七model families、math/code fivebench；tool context20k math/4096 code，orchestrator16384。Table2用$0.02/0.03→provider-specific token caps，AIME2024选DeepSeek、MBPP+选GPT5Mini，故是成本受控**非相同token**。Table3最多两个active tools：AIME self93.33/ orch90/random90，MBPP+ self83.33=orch83.33/random82.27；GT-question+trace自评不是online无GT信心，更不独立真值。没有充分重复run/区间、model pricing时点/全部calibration预算、独立heldout切分、hardware/precision或wall-latency证据；Pareto/十倍不采用。

实际 **AGENT-MULTI-AGENT Ch82:234–252** 已peer posterior/context/outcome和bounded exploration，但未解释同模型的**worker solving与coordinator aggregation角色分别离线校准**。拟在该段后加一窄桥：在稳定pool与可核validation下，按任务族分别测求解/聚合；GT-based profile为带版本离线依据，不是自报confidence或授权，固定$预算仍有不同token和profiling费用；短任务、漂移或profile不可靠保single-agent/固定小pool+verifier。不能因异构family推prior独立，也不声称整个algorithm已有覆盖。

以上16346/16429/16485仅拟处置，必要原源/actual owner尚待root独核；16429/16485尚未写Books，无write lease/POST。普通剩余项不是终态保留。

以上为送审时快照。root必要原源/actual owner独核通过：16346仅报告，16424复用单篇独核争议隔离；16429与16485取得具体窄锁后，已分别写入Ch78:201与Ch82:254。root实际核Ch78:182–213/末注759及Ch82:234–267/末注1054，POST通过，锁释放。该四项由69推进到73终态，不授整日完成。
