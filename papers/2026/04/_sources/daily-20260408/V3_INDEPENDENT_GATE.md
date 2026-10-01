# 2026-04-08 V3 独立定点复核

复核者：独立智能体 `/root/apr03`。检查日：2026-09-26。此记录不代替作者日报，也不单独宣布整日通过。

## 2604.05217v1：理论候选恢复，但中心新命题暂缓

来源：[官方精确 PDF v1](https://arxiv.org/pdf/2604.05217v1)，题名 *On the Geometry of Positional Encodings in Transformers*。已定点核首页版本身份、§3、§4 H1–H3 / Theorem 4 / proof 与 §5.2–5.3 / Proposition 6 / Algorithm 1；未遍历其他附件。以下关键式与 HTML v1 对应，不把后版内容冒充首版。

准入不能沿用“仅小模型任务，未改变runtime”的旧理由。若位置分离保证与可构造的信息几何最优解成立，会改变 Position Encoding 的机制解释与设计选择；建议 `2+1+2=5`，中心理论有效性疑问需要深入处理，不抬分。日期仍由作者对本家族的组合证据单独确认。

### 可支持的旧结论与真实 owner

PDF §3 的计算图只含 token-pair content score，不含固定 causal mask；其 permutation equivariance 应限于这种图与相容的输出处理，不能泛化为所有 decoder readout。Ch13 [Position Encoding](../../../../../books/part-02-model/13-position-encoding.md) 开头已经明确“先忽略 mask 和位置”，随后分别解释 absolute/relative/RoPE。因此该窄结论是真实已有覆盖，不需新增同义正文；不能因这部分已覆盖就取消后续理论候选。

### §4：尚未建立的连接

PDF 印刷第5页（零起点P4）的 proof 写出 `E[Σ_k c_k(E(t_k)+p)] M^T`，随后换成 `(Σ_k E[c_k] ebar_k + pΣ_k E[c_k]) M^T`。这里 `c_k` 由同一输入样本的 loss/score 导数产生，通常与 `E(t_k)` 相关；H1–H3 未给出使 `E[c_k E(t_k)]=E[c_k]E[E(t_k)]` 成立的条件。即使暂接受该分解，不同均值和两个系数不同也不直接排除多项加权和的 cancellation；order-sensitive loss 不等于所述期望导数系数必定不同。另，标准无约束可微极小点的各参数梯度为零，证明需真正推出“相等位置不可能是stationary”，不能仅陈述梯度不同便能下降。当前未建立这些桥梁，不采用全局最小点必然位置分离或其普遍训练保证。

### §5：定义与最优性有可检查反例

PDF §2 Eq.(3) / §5.2 将 `sqrt(probability)` 空间的 Euclidean Hellinger chord 当作 Fisher–Rao geodesic。两者局部相关但并非全局同一距离。例如两点质量分布的 chord 是 `sqrt(2)`，相应球面弧长不等于此值；Algorithm 1 自身仍采用 chord 距离。不能从球面曲率推出该 chord 对有限点集合不存在 Euclidean 等距嵌入：完整 sqrt-probability 坐标本身就是这种嵌入，低维限制应由 centered Gram 的 rank 判断。

PDF 印刷第6页（P5）Proposition 6 用 Gram matrix 的 Frobenius 最佳秩d近似推出 Eq.(4) 的 distance stress 最小；两项目标不等价。一个符合 Eq.(3) 的反例是三个 one-hot distributions，所有 Hellinger 距离均为 `sqrt(2)`。降到一维时 centered Gram 的一个合法首特征向量给出 `(-1/sqrt(2),0,1/sqrt(2))`，归一化 stress=`1/6`；同样一维的 `(-2sqrt(2)/3,0,2sqrt(2)/3)` stress=`1/9`，更低。计算只核该反例，不声称复现作者实验。故不能把该 spectral construction 作为作者定义下的普遍 stress 全局最优证据。它仍可作为几何诊断或初始化候选；较低 stress 不自动证明任务质量更好，论文自己也区分这点。

处置建议：本家族为 `争议 / 暂缓`，不写 Books。唯一重开条件为作者勘误或完整证明明确上述期望分解、非抵消条件与真正优化目标，并纠正 chord/geodesic 语义；不以再跑一次分类 benchmark 代替证明。既有 Ch13 的有条件 permutation 结论不受影响。

## 其他否定侧定点校准

- `2604.05066v1`：完整题摘显示 Rust/polyhedral 工具复用已有 reuse-distance / Data Movement Distance 算法；没有识别出改变现有执行计划选择的新增机制或反证。具体前分母关闭，不因未写LLM或CPU场景排除。
- [JailAgent 2604.05549v1](https://arxiv.org/html/2604.05549v1)：已核§2、§3.2、§4.4、相关消融。攻击假设是可写memory与local logprob surrogate，训练pairwise reranker再选择多个生成答案；不改原user prompt不等于不改控制面。ASR-R、轨迹攻击判定与正常任务完成率分账；结果未建立新的权限边界或通用防护失效保证，新增主要是既有memory poisoning的搜索/选择优化。Ch72行为控制权、retrieval→authority→effect gate与Run评估已承载相应窄认识，可具体前分母关闭；安全信号已实际核，不以主题已覆盖代替审查。
- [MCPShield 2604.05969v1](https://arxiv.org/html/2604.05969v1)：已核§IV、§VI-F与§VII限制。有限LTS、批准定义hash、信息流格、capability与runtime monitor是成熟原则的综合；91%是23类中21类的理论覆盖，非实际防御成功率，177k工具也是引用数据而非本法逐工具攻击实验。Ch72受限状态空间证明与Ch83跨server信息流已具体承载，未发现改变可采用设计选择的新保证，可具体前分母关闭。

以上四项不把源码未运行、实验较小、没有新owner或同主题存在当成排除依据。04943/05074的实际新机制已另通知作者恢复，不在本文件重写其作者证据。12项已落Books的新正文已逐处与必要原文及相邻段落对读，核心机制与限制成立；整日仍需作者同步恢复项、来源精确缺口与最终数量后进行最终Gate。

## 17 项已有覆盖：非作者实际正文定点核对

复核者：`/root/apr02`，2026-09-26。本人不是Apr08日报作者。本轮复用日报§4可核实的exact-version机制/评价记录，逐项对读实际owner的机制正文和相邻论证；未重新抓取14来源、未复现实验、未无差别重读全部附件，不据此宣布整日通过。对05100、05477、05432的具体语义疑问另重开官方HTML v1必要段落。以下是已有覆盖判断，不是17项新写入。

| 家族 | 实际 Books 承载的窄命题与对照 | 非作者裁决及证据边界 |
| --- | --- | --- |
| Mythos官方技术博客 | Ch72“模型辅助漏洞研究”正文分开proposal、可执行reproduction、人类severity/disclosure，并要求denominator/false-positive；Ch66“第一个不变量”及artifact/environment/trace绑定评价身份 | 已有覆盖成立；官方成功案例不证明自主发现率，模型内部机制未披露。未独立复验未公开漏洞 |
| 04978 PermissionGate | Ch72“Agent自己的Instruction、Config与Memory也是受保护资产”以semantic mutation而非syscall合法性判断，后文canonical typed action/effect-time共同授权 | 已有覆盖成立；Edit/Write改JSON且无classifier调用是路径未覆盖，不应仅计入已调用分类器的误差。Docker/shim结果不证明真实集群 |
| 05100 EditButVerify | 首轮漏定位Ch66现有“Compound Artifact需要Preservation Contract”，该正文原已要求必须保持区域及目标正确/无关破坏分账；root在其内部新增代码行为change/preservation双目标、diff/AST不足与低coverage不能直接判无效的窄分支 | **更正并完成实际新增的非作者写后复核：整合通过，不再计为已有覆盖。**独立重开HTML v1§3 RQ2/AppendixB并对读实际正文：35/39低覆盖有合理目的，4项人工核实的不足不能泛化所有coding suites，正文未伪称全面mutation实验。213全任务与91恢复可执行解分母继续分开；未复现实验 |
| 05164 AdaptiveThinking | Ch79“Tool本身有价格…”正文将belief、remaining cost/time/call budget及机会成本连入策略，保留hard cap/verification reserve和静态预算 | 已有覆盖成立；turn allocator的global hinge penalty与实际used-token记账不是hard cap或完整credit assignment。All-SubQ未来题目已知前提不转为在线事实 |
| 05080 Nidus | Ch84“Harness、Protocol与Credit都是Platform-owned Artifact”实际正文将transition/test obligation/release rule版本化，平台拥有protocol/receipt、Agent只提议mutation，并保留不完备spec | 已有覆盖成立；finite PO/daemon路径不证明外部软件或旁路完整安全，单M4部署与49 lesion有限证据不作多tenant保证 |
| 04989 SkillAttack | Ch72“Skill Poisoning的真值是Side Effect”正文已有动态环境触发隐藏路径、matched no-skill反事实、真正effect trace与未触发≠安全 | 已有覆盖成立；本篇固定skill改输入，与修改skill digest的其他威胁模型不合并ASR；sandbox/model judge边界保留 |
| 05333 GraphSkills | Ch84“Skill之间也不能只靠平面tag”正文已有typed relations、composition admission、dependency/version lock、resolved graph及permission/joint evaluation | 已有覆盖成立；reverse-PPR/budget hydration是这条合同的受限实现，不证明依赖完整或budget精确求解。依据PDF v1，不采用HTML后版数值污染；token节约不等latency节约 |
| 05250 DualDiffusion | Ch24的mutable target/provisional修正及成本模型分开committed tokens、质量、memory；Ch48“双向Mask Context”强调无分布证明时回退原blockwise denoising | 已有覆盖成立；K5 stale drafter+bidirectional KL/confidence remask不是AR exact acceptance，GSM8K退步及双模型显存限制需保留，不采“高准确率不变”宣传 |
| 05595 VLA red-team | Ch66“视频评估先确认模态与时间信息是否必要”与输入扰动有效性/诊断代理；Ch26“Prompt在闭环中也是持续生效的控制输入”保存prompt/policy初态和action-effect trace，限定sim-to-real安全 | 已有覆盖成立；no-action诊断决定语言是否必要，语义0.6/50词proxy不保证真等价，模拟多样失败不等真实风险覆盖 |
| 05292 BrokenDefault | Ch72“从Trace检查到受限状态空间验证”明确形式保证依赖有限tool/state/spec假设；模型辅助漏洞段要求最小可执行重现；Ch66“Binary Verdict通过不等于语义忠实”区分solver subset和外部语义 | 已有覆盖成立；pattern-only、SMT SAT与可达runtime exploit分账，3500主分母与另50prompt试验/7PoC不合并，SMT不是全部ground truth |
| 05432 BackdoorTool | Ch72“Search Query本身也是Public Egress Action”对private evidence→query按principal/purpose发送前审核；“Tool Metadata…”对argument级敏感数据治理；“模型建议也可能塑造未来Trigger”跨轮lineage与独立意图 | 已有覆盖成立；重开HTML v1§4.6/Limitations确认memory-read→retrieval外发与返回再诱导、保护只查chunk不查outbound的边界。跨轮累积为假设估计，Setup/Limitations guardrail版本冲突不引用统一绕过率 |
| 05397 TurnCalibration | Ch66全局ECE抵消/隐藏regime实际正文，Calibration Slice绑定deployment estimator/data条件；clean-twin后另有judge history作为evaluation state | 已有覆盖成立；turn/history是具体slice，不是新truth authority。best-of-5 seed、persuasion选择/删失与单turn概率不可泛化风险界 |
| 05172 ClawsBench | Ch66评价身份model×benchmark×harness×environment×scorer，Mock段要求记录被替换组件并真实integration校准；Outcome Witness分开终态成功和过程副作用 | 已有覆盖成立；固定mock conformance与部分skill/harness factorial不证明API完备、真实权限一致或所有harness普遍受益 |
| 05404 PTE | Ch70“Agent Trajectory的Token数必须折算为State-dependent Work”正文已经给出跨round重prefill与decode×active-KV公式、PTE proxy和实测device/wall/tool/SLO并列 | 已有覆盖成立；non-reusable KV是论文假设，不是所有tool pause事实；proxy不拥有latency/账单真值，质量/代理work关系不能作工具导致错误的因果结论 |
| 05477 ActionEffect | Ch80反馈来源表区分environment与same-model critique；正文“执行后的observation才能确认状态”、constraint-wise audit与verification-centric局部repair已承担proposal→真实观察→纠错 | 已有覆盖成立，限定长期采用为观测确认/有界修复这条命题；重开HTML v1§3.2–3.4与failure-slice段确认上一expected effect→下一screen，以及模拟错误screen unchanged。TVAE训练recipe留日报，不声称已在Books逐tag实现，也不采“消除错误”的保证 |
| 05650 VisualSpec | Ch48“Lossless Verification是分布契约”正文明确放宽acceptance产生新sampling policy，用matched-policy同时验速度与质量，保留exact路径 | 已有覆盖成立；visual cosine/PST移位匹配只是近似分支，平均视频质量不能证明target distribution保持，λ/N/两H200实验不外推SLO |
| 05887 HybridKV | Ch45“从不可逆Eviction到可恢复的分层Recall”正文已有per-head active/cold、drift signal、transfer completion可见性，policy持有head role/threshold/calibration身份 | 已有覆盖成立；text-centric分类/两级budget是受限实现。角色不是固有模型常量，错误pruning不可逆，10%nominal KV不是总HBM/并发收益 |

截至本次定点复核，16项已有覆盖的**具体长期命题**成立；05100首轮漏定位原有preservation正文，已明确更正。其代码编辑oracle细化与具体反证仍有真实增量，root写入后本人重新核必要原文及实际段落，整合通过，不重开其他16项。当前32家族为15整合、16已有覆盖、1争议。

## 最终日级验收

`/root`，2026-09-26：复用上述非作者逐篇原文/正文复核与先前实际15项写后核对，重新读取当前报告、日期reconciliation、筛选理由与来源停点。31个arXiv身份唯一，逐家族组合日期的推断性质和5项跨截点、06169更早首发例外隔离保持一致；并非以Updated单字段证明公告。14个Daily到期源没有缺行，历史Research/Publications及MiMo日期缺口保留精确恢复条件，不宣称全部入口覆盖通过。否定侧恢复和05217反例保留，不将两人同意泛化理由当准入证明。

最终32项=20深入+12标准=15真实整合+16具体已有覆盖+1理论争议。逐表检查15项所指owner正文均有对应机制，沿用实际写后审阅而非仅marker存在；05100新增两目标、diff/AST不足与低coverage边界另由apr02实际核原文和正文通过。内部链接、评分集合、来源行和限定diff检查通过。普通Evidence/Books/独立待办为0；具名外部保留项不用于Books、正面证据或无遗漏保证。日级通过，不代表实验复现或争议定理有效。
