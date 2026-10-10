# Prism-Δ 2603.10705v1：必要 Source / 左右子空间反侧 / actual owner ready

本日仅03-12 BJT补充自然日。完整v1题摘准入§19、日级arxiv夹证§23/SUP_DATE3_10705有效复用；9具名作者与Title **Prism-$Δ$: Differential Subspace Steering for Prompt Highlighting in Large Language Models**、AB current-v1身份本次实际回读。Comments21pages/14figures，无具名venue/撤回/纠错说明；有Aug7v2，不因版本号重做或改用current摘要，未展开差分。SubmittedMar11T12:24:45/UpdatedMar12不能单独作公开日。

原件SUP_CORE_10705.raw/txt/MANIFEST_RESULT.json：official exact-v1 https://arxiv.org/html/2603.10705v1 GET200/540327bytes/UTC2026-10-10T03:02:11.570747。实际读完整§3.1–3.3/Eq1–10/Prop1、AppC完整证明、AppD完整Algorithm1，§4实际设置、完整主Tables1–5与§5–6全部评价/直接解释、Limitations、AppE相关metric与AppH全部setup。Figures只读caption/原作者说明，不认证像素曲线；没有展开全部14fig、AppF/I–R全图例、旧steering稿、代码或v2。必要支持及直接反侧够即停，不把普通未读附件叫外部受阻。

## 增量与评分

Key-only强调可能把正负QA共有结构同时放大→本稿对uncentered正负cross-covariance差分作SVD、每head软权重，并分别编辑highlighted token的K与V→需要核差分投影真正删除哪侧共有方向，以及routing/content与质量/费用的局部取舍。

拟 **2+1+2=5**：D2计实际后训练局部干预的差分方向资格和K/V接口，R1为Attention组件，Durability2为表示左右子空间/标注对照与行为回归条件；不把成熟SVD最优性、softplus、QKV分责或19/20宣传计新基础。中心『自动消shared directions』所写条件与实际projection冲突，受影响内容必要深入已完成；拟中心争议暂缓Books0，非EX/降分/已有覆盖新实验。

## 实际机制

§3.2在answer位置抽neutral H / relevant H+ / irrelevant H−，ΩΔ=Hᵀ(H+−H−)/N，取top-k **left** singular U；Eq5与Alg1 line8明确P=U_k U_kᵀ。γ为累计singular-value占比（不自动平方能量），Eq6/Alg1 line9以mean ||r+−r−||给softplus(D−δmin)。K/V各自学习P及w，在线只对highlighted j作k'=(I+gK wK PK)k、v'=(I+gV wV PV)v。其他正交分量不变，沿所选subspace线性scale，并非固定logit bias：K影响query-dependent matching，V影响传值，后面仍原Attention与residual。

Prop1a与AppC的max ||UᵀΩΔ||F²在orthonormal U约束下由SVD成立，**本包保留**。中心问题只在Prop1b把右null映射到所选left projection的消除保证。

## 独立可算反例：右null不保证left投影为零

取d2/k1，

```text
Ω− = [[1,0],[0,0]]
Ω+ = [[1,1],[0,0]]
ΩΔ = [[0,1],[0,0]],  u_s = e1 = (1,0)^T.
Ω+u_s = Ω−u_s = e1,  ΩΔu_s = 0.
```

它满足Prop1b精确写出的shared条件，且共有分量不是两侧都零。ΩΔ的唯一非零singular value1，top-left U=e1，top-right V=e2；Eq5/Alg1实际P=diag(1,0)，所以 **Pu_s=u_s≠0**。Eq9/10在g w≠0时仍放大该方向，不是自动删除。所选γ∈(0,1]都会保留此唯一非零方向。

这也能由有限数据实现原cross-covariance，不借不允许的矩阵：N2、H=√2I、H+=√2Ω+、H−=√2Ω−，则HᵀH±/2=Ω±。Prop1本身说任意finite samples、无分布假设，没有限制cross-covariance对称，因此不能自行补成PSD。若改条件为ΩΔᵀu=0，可限制left非零子空间，但本包不替原文静默换式/改成right投影或改代码。

**只否定Prop1b→Eq5『任何SVD projection均不含shared方向』及§6据它作唯一因果解释的桥接**，不是Prop1a最大差分能量无效、所有方向都shared、原模型实际失败或局部收益造假。softplus(D)不是projection可靠性的概率证书；AppH改称retained singular-values norm是D，和Eq6/Alg1 mean difference口径不一致，精确实现待澄清。零ΩΔ时γ分母sumσ=0的guard也未给，不声称已实现crash。

## 完整主表与必要评价边界

§4/AppH五Base/PT模型Qwen3 4/8/14B与Gemma3 4/12B，GPT4o生成100QA pairs/200triplets抽方向，逐model/benchmark heldout gain/γ/δ sweep，greedy输出64/32/128tokens。H20 144GB单GPU，BiasBios/CounterFact batch256、Pronoun batch1；Table4性能另batch10/平均4362tokens。precision、完整输入分布/并发/SLO/端到端校准累计GPU成本Not Disclosed。

BiasBios first5000与500validation subset的确切隔离索引未给；CounterFact0–5000validation/5000–10000test，边界点文字未细说；Pronoun500/500。不能把所有scope说成独立人群或真实用户指令安全。Lost-in-middle NQ30passages/7gold位置/强调4–25中部/60输出，非所有长上下文任务。

**Table1全表**保留对应指标，具体直接反侧：Gemma3-12B BiasBios key92.22/dual91.94高于Original91.32，但低于asterisk92.90/PASTA94.72/SEKA93.04；有局部提高也不能宣称领先所有比较。CounterFact Gemma3-4B paraphrase key96.24/dual96.01低于SEKA98.83；Gemma3-12B dual Efficacy93.40/Paraphrase91.86低于SEKA98.86/99.27。Qwen BiasBios三个配置dual都略低key。Pronoun Gemma3-4B dual90.16/91.68高于key89.08/90.58，局部互补可保，不推K+V普遍更好。19/20口径只作者所选model×benchmark汇总，不代表全列metric胜出。

**Table2全表**Qwen4/8B：key92.38/89.62，dual92.36/89.12，V-only82.44/79.16；independent+softplus91.52/88.90，differential+uniform91.42/88.22，both-removed91.44/88.50。差分单项在这两条都比both-removed略退，联合软权重出现局部收益，支持bundle取舍、不用单消融证明shared方向必消。**Table3全表**Gemma12B key54.43低于SEKA55.57，dual55.57才打平；其余选配提高仍不覆盖所有金标位置/自然语言。

**Table4全表**Original1.180s/26.39GB，SEKA1.194/26.43，key1.481/26.41，dual1.502/26.43：FlashAttention作者兼容与小memory增量不等无延迟，key/dual约1.26×。AppH offline方向构建3–8min每model、validation5–8gain值与额外forward/projection、cache identity及重校准均计费。

**Table5全表**Qwen4B BiasBios：Vanilla Acc79.80/Fluency4.638/Cons.116，SEKA90.92/3.681/.112，key92.38/4.134/.127，V-only82.44/4.666/.121，dual92.36/4.116/.125；dual这操作点fluency/consistency反而低key，不能说加Value在此总改善fluency。AppE Eq11定义mean log probability≤0，表却全给正数，精确sign/metric转换未披露；故只保作者表中操作点，不把『流畅度代价减半』升格为独立语言质量或自然语言保真。Consistency是generated/input hidden cosine，不是真值/忠实。

§6局部子集方差/检验只是作者摘要描述，未读AppJ/K原统计细节，**不采p<.001/全配置统计可靠保证**。Limitations实际gK须逐任务/model验证，Gemma12B Pronoun需要负gain，不能默认highlight必放大有益语义。restrict system-level highlighting只是作者风险建议，不认证错误高亮/注入误导有安全屏障；没有展开攻击操作或用户认证链。

## actual owner与拟终态

ROADMAP唯一 **MODEL-SELF-ATTENTION Ch14**。实际完整40–121 Q/K/V投影→缩放→mask→softmax与Value读取局部，以及120–129路由权重≠知识贡献，当前正文明分matching/传值，Value norm/方向及干预身份需与任务验收区分。Ch15实际1–34与74–103说明多头不同子空间和output mixing，是headweight交接，不接管单head K/V读写协议；Ch22只交接长上下文真实回读。现Ch14没有吸收本稿差分cross-covariance/left-right null新结论与实验，不能说新实验已有覆盖；原通用QKV原则也不作稿件新增基础。

拟candidate保留，5分必要受影响内容深入/中心方向消除资格争议、暂缓Books0。没有两段PRE/POST需求；不把中心未成立定理变成新书稿机制。重开只需精确side/投影条件或改正版本、D/γ/metric单位与实现一致性，以及在相同数据/预算下消除shared的独立干预对照；保留有限准确率结果，不要求证明所有steering失效或重扫整个旧领域。当前准备者不自签，交root非准备者实际核后才formal。
