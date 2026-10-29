# 06284首次必要／正式拟5／actual owner与最小单段PRE

作者jun06_continue，2026-10-25，只Daily2026-06-06补Jun05。R29完整AB/Jun05联合资格/首次准入复用，不第三日期、题摘或扩87NAV。首次拟2+1+2=5：设计2给goal-directed路径当前frontier而非语义/可执行全菜单的替代，reach1只菜单暴露组件，durability2给相关/可执行/当步goal贡献分责；不重复奖励经典STRIPS/BFS或一般最小权限。

## 必要与直接反侧

实际读[exact-v1](https://arxiv.org/html/2606.06284v1)§3–9、Alg1、Table1–4及直接caption；未核图像素、代码或复现。工具合同为description/required变量R/produced变量E及可选cost/risk；state是已知变量availability集合，success是goal变量集合已包含。基本transition为s并E，单调累积、不表示删除effect、实体值冲突、权限或现实API结果。§4从合同搜索到goal的路径，BFS返回首条最短步数路径的当前可执行frontier；cost可选不使FIFO BFS自动最小成本，也不支持所有同优frontier并集或完整因果识别。

Expose目标相关但当前未需/虽可执行但不达goal者不是permission deny；正确参数/authorization/effect仍由executor外门负责。主受控实验frontier只有一个tool，LLM仍负责参数，不能把低wrong-tool全当独立model reasoning改进。无路径与goal已到均可返回空，harness必须区分终止/失败；原实验无路径算filterfailure，clarify/检索fallback只是§4/8.3部署扩展建议，未实测uncertainty/recovery证明。

102 synthetic tasks、100synthetic tools、calendar/email/files各34，固定gold chain、已给初始/goalstate，每task-tool deterministic mock；每步直接给当前symbolicstate、不需完整history，max6步。四API模型Nova2Lite/ProPreview、Claude3.5Haiku/Sonnet4，六filter共2448 task-method-model runs，不是2448独立任务/重复seed。Controls all100、keyword5/10、state-aware、fullminimalpath、frontier；keyword不是强semanticretrieval，故不由此排除所有embedding/filter替代。

Table4 fullcausalpath与CMTF同aggregate success .99，1.9对1.0 tools/step；只支持减暴露/部分误选的局部取舍，不是frontier普遍更高成功。Wrongtool依唯一goldnext，替代合法路径也可能罚；NovaLite与Sonnet4 alltools已1.00成功，不能称所有model成功提高。叙述NovaLite alltools有wrong/premature同时1.00success，须按总goal与中间错误不同label解释，不造无副作用。Table4 stateaware无premature仍.65success，说明目标推进与这份过早动作proxy不同；单工具强约束不证明真实安全。Tokens从24569→2405为本人口含失败/轨迹变化平均，不是等成功/等latency总降本。

§8.3/9明确依赖准确state、goal、precondition/effect，合同不齐可过度过滤；openended/multiobjective与unexpectedtoolfailure需更宽recoveryset。未测真实API/auth/latency/partialresult，不授生产可靠或安全严重性。实际provider精确snapshot、全decoding参数/重复CI、统一费用/时延及filter搜索CPU账未披露不补；offline合同制备/验证、BFS搜索、statetracking、模型tokens、tool执行及独立outcome/权限回归全费。不由training-free当免费；支持和直接反侧足够，止核心/无附件扩读。

## actual owner与最小gap

已实际读唯一`AGENT-TOOL-CALLING` Ch78模型proposal→executor闭环、ToolContract字段与metadata不可信、FORTIS最小权限完整段、紧接SkillPseudocode合同binding段、符号SMT前置条件完整段、exposure机会校正段；Ch79形式precedence/状态可执行两完整段与Ch77/79开篇交接已核。既有相关不等invoke、最小权限不等实际执行、可满足不授授权和菜单规模机会基线均保持，不算新机制。但现有正文没有从已知R/E和goal搜索一条可达路径、只暴露其当步frontier的菜单策略；Ch79历史precedence prior不是按当前goal的菜单收窄，因此一般“可执行/权限检查”不能硬NC。

拟最小单段置Ch78 FORTIS完整段及2605.09163 marker后、Skill-as-Pseudocode完整段前。只补goal-directed当前frontier及单调变量/恢复边界，不另推完整planner；若reader发现真实等价覆盖则具体NC优先。未SAVE，先独核必要/5/actualgap/PRE再root本轮fresh窄授。

## 原单段PRE

最小权限也不等于当步最有用：多个工具都可执行时，还可用当前已知变量、目标变量和工具前置条件/产出合同搜索一条到目标的路径，只向模型展示这条路径的当前前沿，而不提前展示整条未来工具链。[受限菜单对照](https://arxiv.org/html/2606.06284v1#S4)把暴露选择与参数生成分开，前沿收窄可减少选择负担，却不发现环境中的真实因果；单调累积变量与唯一gold链也不能代表删除effect、等价替代解或现实权限。合同缺失、状态不确定或工具失败时，过窄菜单可能阻断恢复，应区分目标已到与找不到路径，保澄清/诊断或较宽检索集合；这些是采用边界，不是原实验已验证的鲁棒扩展。合同制备、路径搜索、状态跟踪与全部调用/回归均计费，仍由可信executor检查参数、权限和真实effect，不以更少暴露工具批准执行。<!-- source-family:SF-2026-ARXIV-2606-06284 -->

本人注拟：`SF-2026-ARXIV-2606-06284` — jun06_continue，Daily2026-06-06补Jun05；R29AB/date/准入复用，2+1+2=5/唯一AGENT-TOOL-CALLING Ch78。exact-v1 §3–9/Alg1/T1–4必要，只nominal合同/goal路径当前frontier菜单；保单调变量非完整effect、BFS非cost最优、唯一gold/单tool限制、mock/六步/四API人口、fullpath成功持平与recovery未验、全费。不授真实因果、权限或生产净收益；未核图像素/代码/复现。PRE/rootfresh/真SAVE/唯一POST按后到事实记，不预I/DAY。

## 既成采用（2026-10-25，仅行政同步）

R30首次必要/正式5/actualCh78/原单PRE通过后，**writer为root**：root fresh读完整两锚，亲自实际保存原单段与整注；jun06_continue未SAVE Books、不冒作者写入。[R32唯一actualPOST](SUP_REVIEW_20261025.md#r32--cmtf-06284唯一actual-post)真实通过，I12生效/窄位释放。前文PRE/拟态只保历史过程；仅同步既成事实，不第三必要/正文，不授DAY。
