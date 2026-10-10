# 2026-01-02 root 三项新证据独立复核

复核者：`audit_jan02_root_evidence`（非 root 作者）

检查时间：2026-10-07 14:09（北京时间）。结论：三项准入、评分与下述窄处置通过；不授 2026-01-02 日级通过，不验收尚未写回的 Report，也不重审或改动原 104 家族。

实际重读当前 AGENTS、研究合同、Report 合同、来源使用说明与每日分组、Prompt、ROADMAP、相关最新 checkpoint；本日只加载 supplement 文末 root 校准。日期复用 `audit_jan02_dates` 的八项窄证明：官方 ID 首次公告月份不可回溯、Dec30 假期无公告及各 v1 下界联合限定 BJT Jan01；没有拿 submitted 当公开日或追秒。实际独立重开三篇 exact-v1 HTML 与对应 abs；abs 页面没有观察到撤回标记，不以此宣称完整版本史无纠错。未读取后期 revision 或无关附件，未运行作者实现、复现实验或核验生产能力。

## 1. BNA — 2512.24445v1

准入成立：梯度统计不能单独区分误差时间结构 → loss/TD 的 EMA 诊断及门控 → 新的步幅/方向控制分支。评分 `2+2+2=6` 可保留：设计增量是可检查的诊断控制，不是借用 Adam 的成熟机制；Reach 来自 optimizer、actor/critic/exploration、meta-update 的不同控制接口，不把大模型可部署性算入分数。

实际证据：[exact-v1](https://arxiv.org/html/2512.24445v1) §3 Eq1–7、§4 Eq10–19 / Algorithm1、§5–6 的控制接口、§7–8、Appendix A.1–A.3 / B。标准机制与评价审阅完成；针对稳定/下降命题作了额外局部理论复核。

可采用：标量统计调制既有一阶更新的机制描述，且 Eq13–15 确实只缩小基础标量 learning rate。不可采用：因此整个更新范数从不放大、必然下降、通用收敛或任务质量收益。这是不同对象，不能互相替代。Appendix A.3 的投影不增范数解释缺条件。

复核者推导：令一维 `g=m=1`、`s=-0.5`、`tau=0.5`，Eq16 得 `g_tilde=1+0.25/(1+epsilon)>1`。EMA 的历史 alignment 可以为负而当前内积为正；反例在 Appendix B 的代表性 tau 范围内。另令 `tau=2`、正 alignment 接近1即可反转方向；§4 仅给 `tau>=0`，没有把代表性范围变成理论假设。一般 smoothness 只给 `L(theta-alpha*u)<=L(theta)-alpha*<grad L,u>+L*alpha^2*||u||^2/2`，门控上界不能自动供应正的内积项。

§7 只有代表性诊断曲线，§8 承认 EMA 滞后与 distributed aggregation 未充分探索。没有任务级质量/预算匹配实证；模型、数据、硬件、精度、训练预算与 seed 未充分披露，记 `Not Disclosed`；训练 SLO 不适用。

Books：**仅报告**，不写 `TRAIN-PRETRAINING` [Ch28](../../../../../books/part-04-training-system/28-pretraining.md)。已读该章 training-step、统计顺序与 optimizer 论证：现有正文区别名义 scale、有效更新与任务验收，但没有因此宣布本篇 BNA 已有覆盖。此新诊断配方目前只有可检查启发式，稳定与效果命题不成立到足以改变长期设计选择；保留机制记录，不因无完整实验删掉候选。重开只需对应方向/预条件条件的有效证明，或可比任务评价，不索全附件。

## 2. GD=EM — 2512.24780v1

准入成立：试图把软分配从解释性类比提升为学习机制关系 → 可能改变为何模型学习的解释。`2+1+3=6` 可保留；因中心理论争议深入复核，而非靠降分关闭。

实际证据：[exact-v1](https://arxiv.org/html/2512.24780v1) §2.2–2.3、§3 Eq4–5 / §3.2、§4.1 Eq6、§4.2–4.3。Eq4–5 的 LSE 导数恒等式正确；不能冻结这条恒等式或全部责任加权解释。

必须保留作者自限：§3.2 末尾将 implicit EM 限定为 responsibility-weighted updates，不包含 coordinate-ascent EM 或收敛保证。与此同时，§3.2 前文称 backward 就是 M-step，§4.1 再称与 classical EM 的 fixed points / path 一致，形成内部张力，不能只引用强表述或只引用自限。

复核者直接求导：Eq6 `-log(sum(exp(-d)))` 对距离的导数为 `+r`，正文打印 `-r`；§4.3 `d_y+log(sum(exp(-d)))` 应为 `1[j=y]-r_j`，正文打印相反符号。以单 Gaussian 均值为例，当前责任为1，GD 更新是 `mu_new=mu+eta*(x-mu)`，而 §2.3 的精确 M-step 是 `mu_new=x`；一般 eta 下不同。因此责任权重出现不能证明参数更新即 argmax M-step 或相同路径。反例与恒等式都是本次复核者推导，不声称作者实验反证。

Books：**争议 / 暂缓**，只隔离符号、精确 M-step、路径等价和必然 Bayesian 训练推论，不用作正面长期证据。owner 为 `WORLDVIEW-WHY-MODELS-LEARN` [Ch4](../../../../../books/part-01-worldview/04-why-models-learn.md)，attention 交接为 `MODEL-SELF-ATTENTION` [Ch14](../../../../../books/part-02-model/14-self-attention.md)。已读梯度更新及 softmax/Value 论证；不宣称主题相似即覆盖，本篇剩余正确恒等式也不单独构成其新增机制的证实。重开需精确勘误与目标、参数更新、M-step 条件一致的推导；若只采用弱责任加权解释，应明确不是经典 EM 等价。

## 3. AdaGReS — 2512.25052v1

准入成立：固定 relevance/redundancy 权重 → 候选池统计及预算预期容量校准 beta → 预算选择的新启发式分支。`2+1+2=5` 可保留；对拟保证深入复核，不因理论争议否定全部启发式或降分排除。

实际证据：[exact-v1](https://arxiv.org/html/2512.25052v1) §3 Eq1–7 / Algorithm1、§4.1–4.3 Eq18–26、§5.1–5.2 与结论。§3.1 声明非负 similarity；在该假设及固定非负 beta 下 Eq18 已精确满足次模，不需要 small redundancy 才近似成立；次模本身不等于单调。

复核者推导：`Delta(x|A)-Delta(x|B)=beta*sum_{c in B\A} sim(x,c)>=0`；但边际本身仍可负。§4.2.3 把正 RHS 写成负是直接符号矛盾。若改允许 signed cosine，§4.3.2 只给 `sim<=delta` 上界及边际差上界，不能推出 Eq21 所需下界 `Delta_A-Delta_B>=-epsilon`。这是新增补充反证，不依赖外部 textbook。

须保留作者自限：§4.2.4 承认 cardinality 保证不能直接迁移到 token knapsack；但 §4.3.4 Eq26 又授 standard-greedy 保证，没有补足单调与 cost 选择条件。Eq5–6 推出的 beta 分母是 `(k_bar-1)*mean_sim`，Eq7 另多 `/2`，稳定 epsilon 也没有进入式。Algorithm1 的 `continue` 不改变候选集或剩余预算，过长最高正边际项可被无限重复选择；这是 literal 伪码风险，不指控未读实现。

§5.1 对照匹配已选 chunk 数，不等于 variable-length token / 完整成本匹配；IOU 与代表性 GLM-4.5-air 答案只支持有限评价，不能当作近最优证明。硬件、精度、batch、concurrency、SLO 未披露，记 `Not Disclosed`。没有将其 drug 应用本身引入 AI for Science；这里准入对象始终是 RAG 选择机制。

Books：**争议 / 暂缓**，隔离校准推导、可终止算法与近最优保证；启发式机制仍可在 Report 说明，局部评价不因理论失效而删除。owner 为 `AGENT-RAG` [Ch76](../../../../../books/part-07-agent/76-rag.md)，交接为 `AGENT-CONTEXT` Ch75。已读 Ch76 的 retrieval metric 与 reranking/packing 论证，不以已有去重/预算主题冒充覆盖新 beta 校准；必要新机制本身仍待一致说明，故不写 Books。重开需一致精确公式与 similarity/cost 假设、可终止选择过程及与之相符的保证；不要求无关 production 全栈材料。

## 4. 范围与验收边界

三项归属 Jan01、评分和审阅路径复核可接受。BNA 标准完成（理论局部加深）/仅报告；EM、AdaGReS 争议/暂缓，只能作为明确隔离的终态保留项，不是其正面中心结论 Evidence Gate 通过。三项没有共享 Books 改动，也没有以“已有覆盖”省略实际差异判断。

本次只创建该独占文件；未修改 Report、supplement、Books、README 索引、LEARNING_STATE，未 stage/commit/push。原 104 家族、其余四项新证据、全来源覆盖和最后 Report 写回均不在本次验收范围。root 须把作者自限与上述窄边界反映进 Report，再由对应日级复核覆盖实际写回。

独占文件检查：`git diff --no-index --check /dev/null <本文件>` 无空白错误；四个 Books 本地目标均存在，Markdown 标题/段落/链接人工检查完成。没有运行完整 Report validator；上述结构检查不替代语义复核或日级验收。

## 5. 本轮增量日级独立验收（2026-10-07）

复核者仍为 `audit_jan02_root_evidence`，本轮 Report / Books 作者为 `root`。本节不重审原104家族，只复用其未变化的日期、分数和有效处置；当前总表实际111材料行，104旧行加7新行（旧行中102为HTML、另2分别为abs/PDF，不将链接形态误计为家族缺失）。

已实际读本日README的新增结论、14源覆盖、新7行及证据、最终缺口与复核；supplement的完整15题摘、来源查询/分页停点及root校准；`new-evidence-20261007.md`四项证据和非写入者POST。三项原证复核复用本文件§1–3；其余四项精确版本、拟采用命题与未决问题未变，复用必要原源审阅及root PRE，不要求重读全部附件。

### 已通过的窄范围

- 七项新增行目前评分为6/6/6/6/6/6/5，日级日期均Jan01；4整合、1仅报告、2中心争议隔离，Report采用范围与既有原证相符。MS-SSM23824与Self-Critique24103保持潜在贡献/日期保留，不评分不写Books，不借摘要/全文可读性绕过日期。
- 已实际读Ch66 726–750、Ch24 1437–1465、Ch29 429–456、Ch78 42–76的新增两段及完整前后论证，并检查四份限定diff。DarkEQA保存曝光/RAW/ISP支路与严重度分账；GaMO明确图像编码latent后匹配噪声/mask；OpenOneRec区别text-only与无支持token反馈/截断；ShowUI-pi区分gesture horizon、执行步数及replay。四处旧分支、限定、替代与独占owner均保留，来源不能授予的几何/传感器/无偏KL/真实OS保证均没有进入正文。
- 14个到期每日源没有漏行，来源组没有扩成每周扫描。Qwen/Hunyuan所复用原响应实际重读结构/日期字段：60项及最大date=Dec23、total9/list9与publication/display字段分开。仅为本日来源证据检查，不验收其他日期。其他源复用完整限定入口/停止依据，Google/Meta以及arXiv旧ID重要revision历史切片仍明确隔离。MiMo/MiniMax无具名本窗遗漏时不索全机构历史；不把这些有限当前目录变成历史无删除证明。
- 六项负侧完整题摘与具体理由逐条检查；其中SliceLens24592、MDE24111实际额外重开精确v1 HTML决定性core。HOLOGRAPH24478、DynaFix24635、LiftingVision24404、VQ-video24547为题摘/理由复核，不冒称六篇全部原源全文复核。SliceLens已存在instance-level先行方案，当前增量是关系假设/grounded筛组的任务方法；本次可保留其贡献前关闭，不以视觉领域或小模型标签拒绝，也不把VLM置信趋势当因果证明。

### 暂未通过的具体问题

**MDE24111的贡献前关闭理由不足，须定点重开。** 实际[exact-v1](https://arxiv.org/html/2512.24111v1) IV-C Eq11–13 / Algorithm2明确指出普通外部梯度注入会使diffusion轨迹偏离生成支持，再将更新从`score-gamma*delta`改成`score-gamma*J_score*delta`。这是可检查的生成guidance方向替代机制，不仅是在MDE换任务。成熟JVP数学的复用不能独自证明没有design delta；semantic方向保证/物理攻击泛化尚未证实属于后续证据限定，不能据此贡献前关闭。应先核这条生成机制的准入及实际公开日期；它未包含已有八项独立Jan01窄证明，不能直接继承其日期。若落窗不明则保留具名datehold，若确认则按最低审阅处理，不扩其余负侧或整日来源。未要求正文无关的全附件/真实车辆安全证明。

另发现两项可执行报告收尾：§2导语仍称六组历史缺口，须与§5目前只保留Google/Meta同步；SRC-ARXIV应自包含本轮257/116/93/143、3/2/1/2页到`start+len=total`和15具名题摘停点，而不是只显示旧缓冲统计。作者已开始同步该两处；最终还需核当前文本。七行新增表前空行/comment终止旧GFM表，新增行必须带独立表头，不能只靠校验器认出竖线文本。

当前日级结论：**未通过（仅MDE准入/日期与报告收尾可执行问题待处理）**。四项实际Books写入POST已通过；其余有效结果不回滚。报告最终状态、统计及机器验收由root写回，本代理只更新本文件，不stage/commit/push，不接下一日。

### MDE 必要日期条件的独立窄核

上文未通过是改判前停点，不撤销四项有效 Books POST。定点实际重开[abs v1](https://arxiv.org/abs/2512.24111v1)，提交下界为2025-12-30 09:41:41 UTC；实际重读[availability](https://info.arxiv.org/help/availability.html)的ID在announcement分配、不提前分配、不backdate、月为首次announcement月规则及ET公告时段。该下界排除Dec29 ET批次；复用`audit_jan02_dates`此前已实际核验的[2025年末假期公告](https://blog.arxiv.org/2025/11/21/temporary-changes-to-announcement-schedule-due-to-end-of-year-holidays-2025/)中Dec30不公告、Dec31仍公告，再以2512首次公告月份排除Jan首次批，可唯一定位Dec31 ET，即BJT **2026-01-01**日级公开归属。其下界不同于原八项的Dec30 14ET后区间，本次证明已补这一步，不能机械继承八项证明。

此结论为官方规则联合推断，不是submitted=公开，也不授精确公开秒或全网最早版本证明。作者所报DataCite Updated/created/registered不构成必要公开时刻，只能作相容信息。假期页本次重开429、DataCite接口web不可达，未冒称本代理此次新读成功；这里明确复用具名独立审阅已成功核验的假期事实，不因当前抓取限制扩大材料请求。

### MDE 必要证据、评分与实际 owner 决定的独立复核

已读`new-evidence-20261007.md`新增MDE证据全节，并再实际重开exact-v1 IV-C Eq11–13/Algorithm2、V-B TableII及V-C TableIII和相邻解释。**2+1+2=5、标准必要审阅加受影响内容深入可采。** Eq11的δ已从clean estimate反传，Eq13再消费`J_score δ`，额外方向变换成立；不能把它降回贡献前关闭。Eq12以minus线性化、Algorithm2第7行以plus扰动、第8行仅回指Eq12，确实未闭合精确JVP/差分估计接口；乘Jacobian不是自动的语义投影。TableII同region/text对照保留局部支持，但MonoDEVS与ADMM的MRSR持平；TableIII去JVPG分支移除整个外部梯度，不独立识别J调制贡献。上述反证未被扩大为全部实验证伪。

已实际读Ch24 153–172和296–319的完整必要邻接。VJP-free段解释denoiser导数近似，score-Jacobian段解释函数/导数误差，均不能仅因共同术语就宣称已承载“形成外部方向后，再经score Jacobian调制”的替代消费接口。`MULTIMODAL-GENERATIVE-PARADIGMS`的这个潜在差额须保留，未见实际MDE Books写入，不冒充POST或已有覆盖。

**root的最终争议/暂缓、不写Books决定通过窄复核。** 当前保留可解释的额外Jδ变换及局部实验，隔离Eq12/Algorithm2第7～8行的符号与估计接口、语义子空间保证及依赖它们的采用结论；不冻结成熟导数数学、不称全机制无效，也不要求真实车辆闭环或所有附件。具名重开只需该版本作者说明/勘误或对应采样实现闭合上述接口，随后重新判断Ch24窄整合。正文取得后形成的中心争议不是访问受阻或普通未读待办。

报告独立新增表头已实际看到补齐；§2两机构措辞及本轮四主题257/116/93/143、3/2/1/2页停止统计亦已实际核到，前述三项格式/来源自包含问题解除。仍待作者同步MDE后的总表112及15线索最终互斥分区8新增/5关闭/2datehold、§5/§6，未因此重审旧104。

### 本轮增量日级最终结论

**通过——仅限2026-01-02本轮遗漏补充的日级语义验收，复用原104既有有效验收，不重授原源全文复核或全网零遗漏保证。** 本结论覆盖上文先前“未通过/待同步”的中间停点；其发现、反证与改判记录保留。

作者完成后实际窄读README §1/2/3、本轮§4、§5/6及supplement最终分区补正：15具名完整题摘最终为**8新增确定家族＋5贡献前关闭＋2具名日级日期保留**；当前表**112材料行/112唯一ID**，末8依次为24445/24780/24985/25073/24762/24965/25052/24111，公开日期均Jan01。新增分数依次6/6/6/6/6/6/5/5，**4实际Books整合＋1标准仅报告＋3中心接口/理论争议暂缓**，与上述必要审阅、四处实际正文/邻接POST和MDE恢复一致。旧104材料行的内容、顺序、日期、分数和有效证据维持原处理；仅移除表内两个截断空白，连续接8新行，不声称旧排版从未修改。实际结构检查最终从§3首材料至末材料逐行连续均为表格行，没有重复header，BNA已恢复。

14到期每日源有限入口、分页/跨界与stop均有本轮依据；四主题本轮统计已自包含且与旧统计分开。Google/Meta必要历史日级切片及arXiv旧ID重要revision公开覆盖仍隔离；MS-SSM23824/Self-Critique24103两个日期保留项未评分、不进Books。只要求本窗具名版本/公告和受争议命题的必要材料，不新增泛化全年/全机构历史快照、全部附件或全仓库请求。争议不授正面保证，也不撤销有效恒等式、自限、启发式或局部实验；仅报告BNA不冒称具体已有覆盖。没有剩余普通可执行研究/Books工作。

限定Report和四份实际Books的`git diff --check`实际通过；本代理另实际核112行、112唯一ID、末8顺序及8个日级日期和连续GFM结构。未以机器检查替代语义验收，未自行运行完整validator；root所报validator通过单独归属于作者机器结果。作者接下来仅需按本结论写回本轮通过状态/检查时间、必要checkpoint及最终机器复检；这不是未审材料或未落实Books，不等于本代理已经写回共享文件。

本代理只编辑本独占审计文件，没有写Report、Books、共享索引或Learning State；未stage/commit/push，不接下一日。
