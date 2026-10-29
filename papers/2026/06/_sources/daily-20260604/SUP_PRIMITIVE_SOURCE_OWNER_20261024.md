# 02994 Reasoning Primitive Induction — Source / owner / PRE

作者supp_20260604_author，R2准入/Jun03联合日期已过。2+1+2=5，具体tool实现语义gap深入。exact-v1原题摘/完整TEXT89129chars实存；作者已读§3–6/AppendixC/D/F/H/I/J必要，reader对应原域已准备，不泛读无关附录。未核实现或复现。

## 必要证据

§3.1 typed pseudo-tool=(name,signature,docstring)，没有手写tasklogic，每次调用仍将args+docstring交LLM并parse；signature固定约束调用接口，不给semantic correctness。L∪finish作ReAct actionspace，非原型已经执行的外部真实函数。§3.2训练成功final-label过滤后丢action/observation，只聚Thought类别，≥m3/最多5代表/topK5合成；success标签不证明每Thought正确/faithful或无系统偏差。一次induction无weightsupdate，perfamily重新制备。

§4/5/AppJ固定75train/75val/rest，test100/106/66/100等；DeepSeekV3 greedyT0，共ReActdispatch/step-token预算，50step cap。hand-designed主表fixedpipeline，AppB.7另用ReActdispatch辅助，不能把主表差额全归库发现。main117K mean tokens vsAWM154K、CoT/PoT5–6K说明非单次免费能力提升，Together pertoken价格只按token线性变换，不walltime/hardwareSLO。AppH仅MuSR两格SC20、约21×CoT预算仍低于库，不证明全任务所有等总compute策略都劣，也未纳induction制备费。

AppC K10可使object比K5退17pp，description inprompt对correct-filtered可伤，noisyfilter上可反增；AppD三seed只MuSR，非所有tasks重复。§5/I排除airline/tax/calendar等仍保反侧：纯LLM算术链airline51→16、tax48→2.7；calendar86→70；trip全方法<10不作有利比较，不能只讲五in-scope全升。hybrid Python arithmetic airline约51.3回CoT而extraction仍有缺口，不称自动完整hybridpipeline已实现。NatPlan strictparser全0，main由同DeepSeekV3judge，GeminiLite另核296case agreement96.6仅部分cells，不独立认证所有plantruth。跨familytransfer未做。

## actual owner

F表8反侧已作者回表：murder induced41.9K>A​​WM32.0K、meeting52.5K>A​​WM26.0K；ReAct总体mean33.4K低于induced117.5K。所以主文/邻段ReAct comparable-or-larger、AWM每格更便宜不采用；只保整体AWM均值的有限比较与各cell独立账，不认证普遍计算优势。AppE296例的aggregate agreement不等逐cell完全相同或oracle真值。

三context/ROADMAP已读，AGENT-TOOL-CALLING/Ch78拥有call contract/realization。已读ToolContract完整schema/metadata分责、Skill-as-Pseudocode27955完整段与前FORTIS完整段/后WebVerbs完整段；Ch77derivedmemory与Ch79planning交接不接管调用实现。27955明确invoke只是文档notation未runtime，尚未承载**已实现的typed伪工具每次由LLM解释而非deterministicbody**以及把successfulthoughts聚成library的有效性/边界。拟在27955整段inline marker之后/网站wrapper完整段前加2段，只讲该受限调用分支，不复制memory生命周期。

## 最小PRE

完整上锚：

当Skill文档仍是自由散文时，抽象合同与具体调用语法也不宜互相替代：可把trigger、I/O和前后条件提取为typed pseudocode，同时保留父流程中的原始action templates与bindings；检索只返回parent，再将所需child合同内联，避免裸child丢失调用上下文。[Skill-as-Pseudocode的受限分支](https://arxiv.org/html/2605.27955v1#S3)中的invoke只是文档notation，不是已实现的runtime展开器。Token覆盖、语法替换和AST风险检查不证明语义等价或授权，binding提取/冲突重写仍依赖LLM；有限ALFWorld收益、20题组件对照和10题第二任务反侧也不授任意OpenAPI库普胜。构建、重写、验证与实际执行都付费，版本或绑定不能核实时回读原文、保留具体模板与人工窄合同，最终仍由可信executor检查参数、权限和真实outcome，不让较短文档自签可执行性。<!-- source-family:SF-2026-ARXIV-2605-27955 -->

拟增两段：

另一个实现分支把自然语言描述绑定到真正的调用接口，但函数体仍由模型在每次调用时解释：固定 name 与 typed I/O，将实参与 docstring 拼成提示，再解析模型返回值。这类 pseudo-tool 提供可复用的推理动作词表，不是把模型判断变成确定性代码或外部观测。可以从最终答案正确的训练轨迹提取反复出现的 thought 类别，归并后合成小型库，让同一 ReAct controller 自由组合；但只保留成功轨迹、甚至丢弃 action/observation 后抽出的频繁思路，仍可能包含错误理由和共同偏差，typed signature 只约束接口。<!-- source-family:SF-2026-ARXIV-2606-02994 -->

一项[受限原语归纳对照](https://arxiv.org/html/2606.02994v1)显示这种库可以优于产生轨迹的原策略，却不能据此宣布普遍超越教师或更便宜：每次伪工具仍付模型调用费，轨迹采集、分类合并、库合成和独立验证也要计入总预算。更大库、额外展开描述及算术密集任务均有退步，局部等采样预算控制不排除所有计算与协议替代解释。需要精确计算时保留真实确定性 helper 与独立结果检查；分布变化、描述失真或收益不足时，回退原小库、普通调用或单次推理，不由函数名、类型解析或成功 thought 自动批准语义正确性与外部 effect。<!-- source-family:SF-2026-ARXIV-2606-02994 -->

完整下锚：

当工具封装网站操作时，稳定性还取决于网站是否承担外部接口的兼容责任。API 可直接包装成 typed function，GUI 路径也可由开发者录制操作、调试 locator，再参数化输入并返回结构化结果；但当前页面中偶然稳定的选择器不是网站承诺的 public ABI。[一个有限原型](https://arxiv.org/html/2602.17245v1#S4.SS1)提出由网站显式发布 stable-public-locator、把修改视为 breaking change，并以网站 domain 拥有 verb namespace；这是接口责任提案，不是已标准化或部署到全网的协议。100项人工核验任务、10项选出的 baseline 比较及仅成功子集的时延，不能证明开放网站可靠性或总体提速，security/permission 在原文仍是 open problem。包装、回归测试、网站版本与 locator 维护均有费用，权限和 effect-time 校验仍归可信 executor；缺少网站兼容承诺、页面漂移或 wrapper 行为无法核验时，应重新验证或回退经观察的原始 GUI/API 操作，而不是让 typed signature 自签语义、安全或执行许可。<!-- source-family:SF-2026-ARXIV-2602-17245 -->

Review note拟：`SF-2026-ARXIV-2606-02994`：2+1+2=5；exact-v1 §3–6/C/D/F/H/I/J，typed伪工具每调用仍LLM解释，成功final不证各thought真；保K/description反退、arithmetic/calendar/trip负侧、局部SC20/单任务族和judge限制，所有调用与归纳制备费用计入。未核实现或复现。待实际写后复核。
