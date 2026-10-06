# Memento-Skills18743：必要原证与具体 PRE

准备者/拟writer root，仅03-21补03-20自然日；本日已有准入与日期夹证复用，不改旧窗口/候选。当前合同、ROADMAP和Books学习/写作上下文实际重读。拟2+1+2=5，只给 skill retrieval 的训练目标与消费接口差额，不给旧Memento2 read/write原则、通用反思或模型无参数更新本身新分。尚未独核或写入。

## 必要原证与直接反侧

[exact-v1 PDF](https://arxiv.org/pdf/2603.18743v1) §2.1–2.4、Figure9、§3.1/Figures10–12和§3.2实际读；[HTML](https://arxiv.org/html/2603.18743v1)多处只有空标题，缺router/evaluation正文，故仅补对应PDF，不遍教学对话、安装示例或旧Memento2证明。未核代码或复现。

- §2.3以约8k skills中约3k seeds，从name/description生成正例和同主题但不适用的hard-negative goals，judge读取全skill过滤；训练Qwen3-Embedding-0.6B，多正InfoNCE把skill与goal关联。合成judge标签不是实际执行成功概率；文中loss对同skill跨query归一化，policy对同query跨skill归一化，不能仅凭softmax形似授InfoNCE与one-step optimal Q/policy的严格等价或校准。只采用对比训练的有限路由接口，不采收敛桥。
- §2.4 BM25+dense+score-aware RRF/可选crossencoder是检索实现；stars>500与description hash过滤只限定作者catalog，不证明成熟、安全、近重复语义去重或完整来源。140 synthetic queries的Recall与real trajectory route hit/judge success分开；真实trajectory数量、重复/CI、具体配置未披露。Fig9文字Qwen Recall@1 .54而图柱标 .53不照数值；Qwen→Memento judge success .79→.80，不能把router hit改善说成同幅端到端收益。
- §2.1失败后单skill credit归因→rewrite/discovery→synthetic unit-test/rollback→至多K feedback retries；Judge显式用真实答案a*，不是部署无oracle保证，成功率也不是因果credit或授权。底层LLM不更新≠router不训练/全流程零成本。write/edit和catalog变化须重新检验路由适用性（工程边界），自动test不保证任意副作用安全。
- §3.1 GAIA validation165拆100train/65test，HLE1130拆788/342；Gemini-3.1-Flash，GAIA最多3 reflective retries，full与禁全部skill optimisation的Read-Write对照。作者称test unseen，但反馈/库冻结/各test是否可继续write的完整评测协议未披露，不把“heldout”当独立无污染证书；rewrite/discovery/库增长/teacher反馈同时变化，不能归因单router或单mutation。GAIA most train skills未在test触发，明确transfer有限；HLE同subject复用不是任意跨域泛化。
- §3.2 coverage radius/LLM competence/retrieval error理论借Memento2；t-SNE图与饱和曲线不实测半径、因果分离或证明现实无界库收敛，不扩读旧理论以替其补证明。教学对话的93.5%/p99 195ms不作实验。完整构建、合成goal/judge、router训练、索引/rerank、rewrite/test/retry均计费；硬件、precision、servingbatch/concurrency、token/API费用/SLO、seed/CI未披露，不授生产收益。

## Actual sole owner 差额

`AGENT-MEMORY` Ch77：实际Read183–232、procedural621–675、Skill710–748及1734–1785，Ch76/78交接；现有语义/通道路由、过程skill/检索范围与独立mutation gate，尚缺**从skill的描述生成目标/同主题hard-negative、训练执行相关选择，再把retrieval命中与完整trajectory成功分账**。只补Read中SelRoute两段后、通用score(m)前，不重复read/write旧原则或把router训练归第二owner。

## 两段逐字 PRE

检索程序化 skill 时，语义相关还不等于当前目标下的行为适用。固定词面或通用 embedding 在目录小、描述准确时最容易维护；任务共享术语却需要不同步骤时，可以从 skill 的名称与描述生成候选目标，另造同主题但不适用的 hard negatives，再由读取完整 skill 的 judge 筛选，训练对比式 router。这里学到的是受标注分布约束的选择分数，不是已校准的执行成功概率；检索器只提出 skill，当前状态、前置条件、权限与结果验证仍决定能否消费它。<!-- source-family:SF-2026-ARXIV-2603-18743 -->

这种分支把部分选择成本移到数据构建和 router 训练，也新增合成标签偏差、库更新失配、索引与重排费用；应分别测检索命中、真实轨迹成功和跨任务迁移，不能由更高 Recall 推出同幅端到端收益。[受限 Memento-Skills 对照](https://arxiv.org/pdf/2603.18743v1)同时改写和扩展技能库，GAIA 中多数训练期 skill 未在测试触发，不能把总提升只归于 router，或由库增大和曲线饱和认证普遍收敛。单个合成测试也不授自动编辑安全；反思、重写、judge、回归与重试均计入完整成本。标注、库版本或适用范围无法核验时，保留静态 skill、原轨迹和直接检索，交当前 workflow 独立验收，而不是以历史成功率批准执行。

## 静态源注 PRE

- `SF-2026-ARXIV-2603-18743` — [Memento-Skills exact-v1 PDF](https://arxiv.org/pdf/2603.18743v1) §2.1–2.4/Figure9、§3.1–3.2/Figures10–12；仅合成目标/同主题hard-negative的有限对比路由及检索—轨迹—迁移分账。标注代理、InfoNCE/policy归一化差异、库增长与rewrite组合、GAIA有限transfer、feedback/冻结协议和全构建/使用费保留；不采校准Q/最优收敛、零训练费或自动编辑安全，未核实现/复现。

待非准备者Source/actualowner/逐字PRE，未授锁/写入/计safe，不授DAY。

## 非准备者必要 Source / actual owner / PRE（正式有限通过）

resume_mar18 独立重载本日适用合同与 Books 上下文，实际回对 exact-v1 PDF §2.1–2.4/Figure9、§3.1–3.2/Figures10–12，actual Ch77 180–236、620–675、709–748及1734–1785的读取、过程/typed skill与mutation gate；Ch76/78交接已有有效实际读可复用。两个逐字 PRE 与静态注正式有限 PASS。对比式技能选择的输入/标注接口确有差额，不为旧 read/write 原则或已有独立 commit gate 重复加分；2+1+2=5成立，初6只按该具体新增命题纠正，不因审阅成本或争议降分。

训练归一化跨 query、消费策略跨 skill 的差异不支持严格 Q/InfoNCE 等价，但不阻止对比路由的受限接口；label 与当前执行权限/成功概率分开。GAIA最多三次反馈重试、full同时开启全部优化、训练多数 skill 不触发测试以及HLE同subject复用，均不能识别单router因果或任意跨域迁移。§3.2借旧Memento2半径界并用t-SNE/饱和解释现实收敛，此桥不采用，不为其补旧proof；PRE不依赖该桥仍成立。库增长、反馈冻结协议、合成标签/测试与全部构建使用费用已就近保留，不授无oracle部署、自动编辑安全、零费或生产SLO。

此处只授 Source/PRE；root协调唯一窄锁与实际写后，仍须一次非writer完整正文/邻接/本人静态注 POST，未计safe或DAY。

## 一次 nonwriter actual POST（正式有限通过）

root据非准备者正式PASS窄写原两段及本人静态注；resume_mar18实际完整Ch77 180–218（bounded retrieval/表示分路→SelRoute→新对比skill选择→通用score/current authorization）、末9行本人静态注及邻注逐字回对已核原PRE。当前正文实际196/198（root先前197/199仅行号误差），两段与静态注内容一致。标注代理不授执行成功概率，检索—真实trajectory—迁移分账、GAIA有限transfer/库增长联合混杂、合成测试不授编辑安全、全部构建/使用费用与旧静态/直接检索/workflow独立验收准确；未引入Q等价、旧收敛或零费。限定diffcheck空，正式有限actualPOST PASS；请root接纳释放，可正常归并实际I，不授DAY，不递归改书静态注身份。
