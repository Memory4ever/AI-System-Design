# AFS-Search18627：诊断、可微修正与分支选择分责

resume_mar18唯一准备；仅03-21补BJT03-20，原完整AB/65项独校复用。不新query、不遍全部prompt/图/代码；未独核、未锁未写、不计safe/DAY。

## 日期与准入

实际[official abs v1](https://arxiv.org/abs/2603.18627v1)完整题摘/currentheader/history，六作者/同题，仅v1，所见无明确撤回、纠错或先公开venue信号。真实[DataCite](https://api.datacite.org/dois/10.48550/arXiv.2603.18627) findable；Submitted03-19T08:50:49Z、Updated03-20T00:44Z、created/registered03-20T02:17:07Z、Available仅月份。沿本批公开列表/字段夹证作BJT03-20有限日级归属，不冒公告精确时刻或别处从未先稿。

外部整图重生成不能局部干预→中间preview的VLM诊断生成局部条件、可微CLIP能量修正flow，再将原/修正/随机分支短程展开择优→诊断、gradient consumer和scalar选择不能互相签发可靠性。拟2+2+2=6；只给这组内部采样接口差额，不把通用反馈/搜索计DD3。

## 必要Source与直接反侧

实际[exact-v1](https://arxiv.org/html/2603.18627v1)§3.1–3.5/Eqs1–6、§4.1–4.3/Tables1–3、A.2/Algorithm1、B必要mask失败声明、C.1与C.3–5、D限制；支持与关键反侧足够即停。未核所有视觉图、完整prompt实现、代码/复现。

VLM从解码preview提议正/负概念与SAM3 mask；可微信号是CLIP差分经decoder反传，并非对黑盒VLM求梯度。保持原继续分支，与局部修正及噪声探索分支作短程模拟，VLM再评分选继续状态。最终低分可改prompt/seed重试。式1噪声0→数据1与式2噪声1→数据0不同时间口径；不采统一符号recipe。mask在latent上乘不能证明非线性decoder后的未遮像素零变化，线性clean projection亦不保证真实最终图。

Table1 Pro shape/texture仍低于AgentComp；Fast/Pro时间32.5/62.3均高于原FLUX11.7，不能说免全图重生成费用。Pro/Fast不同VLM，加入prompt优化/搜索/repair同时换预算；T3顺序去模块非等费用因果/CI。§4.3的Standard“35 steps”与§4.1的3或5/Deep15口径不齐，不采精确horizon最佳配方。C参数由同Qwen-VL-Max subset评分，非独立真值；B只在错误mask被critic降分的条件下回退，没有证明误判永不伤害。独算score偏误可选坏支，原base保留不构成质量下界。D明确VLM、decoder、tool、多分支与memory费用；hardware/precision/batch/concurrency/完整SLO、重复seed/不确定性未披露，不补造生产或latency保证。

## Actual sole owner

`MULTIMODAL-GENERATIVE-PARADIGMS`/[Ch24](../../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)：实际完整223–249的CFM/solver责任和374–395的h/MC/DOIT引导→linear-tilt→latent-text顺读；Ch23/25开篇已读，LS仅本日路由。DOIT现388是terminal reward/MC及one-step surrogate，不承载VLM语义诊断→可微local field proposal→三分支scalar选择这组分责。拟DOIT完整后、linear-tilt前一段；无Agent planner/World owner扩写，不强造一般mask原则。

## One literal PRE（待root非准备者）

引导也可以拆成语义诊断、可微修正和候选选择，而不是让一个反馈分数直接认证修改方向。一条[受限图像flow分支](https://arxiv.org/html/2603.18627v1)先将当前latent投影成可解码preview，由VLM提议局部缺陷与目标、分割器提供mask，再把CLIP正负概念能量经decoder反传到velocity；VLM本身的离散诊断并不是这条梯度。采样器保留原继续路径，另展开修正与随机探索分支，短程preview评分只决定接续哪个候选。近似preview、mask及critic均可能错，latent范围也不保证未遮像素不变；原分支存在不证明被选输出永不退步，仍需独立最终质量检验。多分支、解码、梯度、VLM/tool调用和失败重试均付费，所测路径比原FLUX更慢，部分分项不及其他基线；不同critic和搜索预算不能直接归因为修正器收益。时钟方向、solver、条件与原始状态需一起冻结，诊断、独立质量或预算未通过时保留原sampler、较保守引导或整图重生成，不从局部高分签发全局可靠、保持原分布或生产实时保证。<!-- source-family:SF-2026-ARXIV-2603-18627 -->

静态注：

- `SF-2026-ARXIV-2603-18627` — [AFS-Search exact-v1](https://arxiv.org/html/2603.18627v1)必要§3–4/Eqs1–6/Tables1–3、A.2/Alg1、B/C必要反侧与D；仅诊断→可微local field proposal→短程分支选择分责。保时间口径/preview和mask近似、critic误选、不同VLM/预算与分项反退、完整decoder/梯度/搜索/retry费用；不采精确horizon、无损或永不退步/生产保证。未核全部图、实现/复现。

交root非preparer必要Source/date/actualowner/PRE裁；无写锁，不先计safe。

## 非准备者 root Source／actualowner／literal 裁

root实际读exact-v1 §3 L111–170/Eqs1–6、§4 L173–261/T1–3、A.2/Alg1 L334–376、B mask反侧L377–399、C必要导数/评价人口L403–446与D L447–454；官方v1 abs身份/轻量状态与已有日级夹证复用。必要支持与直接反证已足，不再遍prompt、图像或代码。root实际Ch24完整370–404及225–249，与前后Ch23/25已读边界核对：h/MC/DOIT→诊断与可微consumer分责→结构化tilt之间有具体差额，不把黑盒VLM当可微reward。

原one literal/static与以上证据逐字对照通过：不采时间方向/精确horizon、不授mask外像素不变或base存在即无退步；费用/不同critic与budget及质量分项反侧近文，2+2+2=6合理。有限Source/PRE PASS。授resume_mar18 sole Ch24本family窄写，保既有文本和静态注；写后交root实际局部与本人末注POST。未写前不计safe/DAY。

## 实际 writer 写后

作者获锁后逐字one PRE/static落实Ch24正文390/本人注2475；实际完整380–404和末6/邻注顺读，回原literal/PRE一致，限定diffcheck0。保诊断、可微修正与scalar分支选择分责、mask/critic/预算反側；未修改其他family或书注人员身份。待root一次nonwriter actualPOST，未先计safe/DAY。

## root 非writer 实际 POST

root实际顺读Ch24完整384–398（blind→h→DOIT→本人390→linear-tilt→latent文本）及末6本人2475/邻注，回对one literal/static和已核原证。语义诊断、CLIP/decoder梯度与scalar选择分责准确；critic误选、mask近似、不同预算/反退与完整费用近文，未引入统一时间符号或无损保证。有限actualPOST PASS，root接纳释放Ch24；本family可安全同步，不授DAY。
