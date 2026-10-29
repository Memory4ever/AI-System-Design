# A115 — SaliMory04120首次必要 / 正式6分 / actual Ch77最小PRE提案

当前落实：R115–116必要层与原稿有效；root本轮按角色pair构造/分差与bank资格校准整合门槛通过后窄授，原两段已保存于Ch77同bank完整段后/masking完整段前，简洁来源注在真H2 Review notes下。root R117唯一实际写后通过，I25生效；以下“未SAVE/待核”均为准备时快照，不重开已成层。写前快照 `/private/tmp/salimory-0605-save.S3KEam/ch77-before.md`，实际新增与完整直接两侧/简注已自读，原同bank更强控制保留。

仅Daily2026-06-05补Jun04 BJT自然日，R89–91完整题摘/收窄准入/精确v1联合日期及官方notice有效复用，不第三。AgentJet R113–114实际读回并仅行政采用具体NC，30正式已处置=24I/5NC/1DistIL争议；该行政态已实际调用validate_research.py的V3入口单独通过。没有Book新授权，以下两段只是首次必要/actualowner/PRE准备，未签reader通过、SAVE、POST或新I/DAY。

## 精确原域与停止

原文：[SaliMory: Orchestrating Cognitive Memory for Conversational Agents v1](https://arxiv.org/html/2606.04120v1)。本次官方HTML GET200，317410bytes；本地`SUP_2606.04120v1_20261025.html`，SHA256=`7ba6a267889e6809ada8664f00d13a218ae1419a1eda0c23a23a2abe4e4a8c81`。页头arXiv2606.04120v1/02Jun2026是提交口径，不当公开日；R91 Submitted-v1 Jun02 18:31:50Z与findable/arxiv.content exact DOI registered Jun04 01:51:45Z联合最早公告界，完整区间Jun04 08:00–09:51:45BJT同日，复用而不重做日期。v2 Aug24内容不采用。

实际读§1、§3.1–3.5/Eq1–6、§4、§5.1–5.5/T1–3/F1–4文字caption及分析、B.1/T4数据与构造、B.2 Alg1、B.3–4 judge与错误人口、B.5/T6超参、C直接限制，因奖励定义需要定点读E.2/E.3完整评分输入/规则。没有读取图像像素、D全补充、E.1全prompt、代码或复现实验，未将论文打印算法当实现通过。支持与直接反侧足停止，不扩其它Methods/附件。页内Code当时只写“To be released”；可选代码不阻塞所采论文层设计，也不据此签未公开的loss实现。

## 支持与精确反侧

1. **角色与状态。** §3.1–3.2把源utterances派生为factual/preference/working三bank。offline filter→顺序booster更新，runtime utilizer产query-conditioned profile，再交另一冻结generator。三角色使用同一πθ、不同prompt，不是三个参数独立模型。三bank和认知命名本身不单计贡献；过滤后的writer若已丢原信息，下游profile不能凭较高reward补事实。
2. **奖励与共享GRPO。** Eq1 R1=accuracy×(1+λp personalization)，不适用时只accuracy；accuracy低时抑制装饰错误，不认证现实真值。Eq2 γ=factuality×(1−vagueness)，R2=−λpen(1−γ)+λbonγ；Eq3 R3含profile utility μ及带recall权重的filter precision/recall。Alg1第8步仍按每episode四rollouts总reward组归一，不能说主GRPO已经完全角色隔离。filter ground-truth标签的标注构造未在必要域清楚披露，不能补成无监督或在线可得。
3. **具体新增。** §3.4 booster winner/loser只看R2而非总reward，辅助contrastive信号由abs(R2w−R2l)加权；utilizer只看μ排名，并要求两rollout memory-entry集合Jaccard>τsim才建pair。Eq5将两角色辅助loss相加，Eq6叠加总reward GRPO；§3.5声称辅助仅路由booster/utilizer，filter由GRPO学习。必要域没有打印完整contrastive likelihood/margin公式、pair采样/去重与空集合协议，不能补标准DPO或实现recipe。这里所采是pair selection/role trace loss接口，而非声称已解决全部信用分配。
4. **关键反证：相似≠相同输入/因果隔离。** §3.4称gate保证差额严格来自utilizer，但T6 τsim=0.15远低于1；Jaccard较高仍可有不同的关键entry，亦未保证query、source/版本、bank顺序与语义相同。gate只是pair人口启发式，不能排尽上游信息差与采样混杂。不同角色的trace辅助loss仍更新共享πθ，不等于参数独立、无相互干扰或每个模块“只获得自己挣得的梯度”。这是本项目根据原机制的限定，不给原文补新定理；已有真实同bank比较比此软gate更强的输入控制条件要保留。
5. **奖励打印差额。** §3.3称λpen=3×λbon，T6实际.5/.3≠3；只采用pen>bonus，不采具体3倍。E.2空memory指定vague0/factual1，按Eq2空库也可得最大R2，故R2本身不能保证覆盖/“遗漏永远更好”；须保R1/heldout召回与源核验，不声称作者已经观测reward hacking。E.3含gold answer、memory、conversation作judge输入，是训练/评价代理，部署不能偷带gold；“faithful to source utterance”不是用户说法的现实真值或consent。
6. **关键受限对照。** T2(a) R1only QA65.8/Good30.6，+R2为69.2/35.7，+R3为72.9/39.8；T2(b) GRPOonly68.6/26.8，booster only69.1/29.5，utilizer only71.7/35.9，both72.9/39.8。支持此配方辅助信号的局部效用；未单独消融Jaccard gate、gap weighting/阈值/共享参数干扰，不证明因果隔离或所有任务dense reward必需。EMA训练曲线先后不证bottom-up因果链。T1 full72.9与Mem-R1 62.7为+10.2points，vs最高zero-shot70.9只+2points；Good39.8 vs MemR1 16.3为+23.5points，不能不指分母照抄“超过SOTA10%/所有bad几乎根除”。Bad仍1.4%。
7. **人口/评价/成本。** §4 trainable Qwen3.5-9B、frozen Qwen3-235B-A22B、GPT4o judge；zero-shot manager为Gemini3flash，异模型比较不是纯架构消融。B1原QA1529＋Llama生成且专家复核1108新QA=2637，T4写28users/60-20-20 split、§4原LoCoMo描述10users，未说明split按用户还是QA，不能签严格user-heldout/无泄漏或无条件10用户人口。Good由三阶段judge在personalizable响应人口评分；gated earliest-error是诊断规则不是反事实归因，“16.4% memory error”不冒只在失败内比例。T6八A100/group4/batch8/5epochs/inner4，但precision、独立seed/CI、各消融完整训练token/费用未披露。T3的76×formation、1.2→.26sec runtime同时对比异manager/model，未闭API/网络/batch/长度完整计时，不是同硬件纯机制加速或生产SLO。C明确所有奖励依赖GPT4o/API偏差且booster顺序随salient turns线性增长；28天内部流未公开/样本规模及干预不清，只支持所报受限结果，不证真实终身/权限安全。

## 正式增量评分

Design Delta2＋System Reach2＋Durability2＝**6**：从单一总reward跨filter/write/utilize混发信用，新增按R2/μ分别建角色偏好对、带上游bank相似人口gate并叠加共享GRPO的具体训练接口；改变writer/reader比较输入与loss路由的设计及验收，不按陪伴场景、三bank名称、Meta身份或全局分数提分。跨持久memory生产与query-time消费，pair状态与共享参数边界可长期复用。actual长期gap触发只深入受影响信用分配域；支持与关键反侧已足，不因此全篇/全附件。

## actual owner 与最小差额

Owner=`AGENT-MEMORY`，actual `books/part-07-agent/77-memory.md`，不是把GRPO通用算法复制Ch33或把judge taxonomy复制Ch66。本次实际读Ch77开篇/typed write风险与§Outcome Reward→Content-level Credit完整相关组，邻Ch76/78实际开篇/ROADMAP交接；现有§Memory Read入口也核。

- Ch77:183–194已有memory-span辅助advantage、gold likelihood/实体重构广播与proxy非因果，不需重复“更密reward更好”。
- Ch77:196–199已有冻结writer/reader分责、同dialogue construction与**共用一个bank** retrieval比较和不把bank缺失算reader错误；这组更强状态控制须保护，不以SaliMory软相似gate替代。
- Ch77:201–205完整counterfactual/masking组已有global＋local信用/全部评分费与authority边界；207–215 update/exit和retrieval-count/step-ID分账亦已有。
- 尚缺的最小接口不是generic role attribution，而是**同一共享policy内，用不同role-specific分数建辅助偏好对时，pair筛选条件与输入bank的近似一致并不使梯度参数独立**。相近memory可以比较但必须保上游差异和状态身份，不能用“stage reward/causal gate”名义签已隔离。可在Ch77:199完整同bank比较段后、201完整masking段前仅加以下两段；本项仍待reader首次必要/score/actualowner/PRE，root fresh窄授前不写。

### 完整上锚（当前Ch77:199）

同一manager同时学习写入与检索时，应先拆开bank未保存必要信息与reader未找到信息。可在训练中用有标注来源的record集合让固定answerer估计bank可答性，再交替比较同dialogue的construction rollouts与共用一个bank的retrieval rollouts；bank proxy也无法答时，不把retrieval失败当作reader负例，并从组统计和loss同时排除。按触发事件对齐信用、沿update/delete lineage追到后续修改者，能减少两stage共同变化的混淆，却不是相同state反事实或真值归因；它依赖证据标签、answerer/judge并支付额外建库、评分与lineage成本。缺标签、proxy失配或共享policy回归时，保留outcome-only、固定writer/reader及原episode，不由被排失败制造更高表面成功率。 [受限原文](https://arxiv.org/html/2610.29671v1)。<!-- source-family:SF-2026-ARXIV-2610-29671 -->

### 两段literal PRE提案（未SAVE）

共享一个模型处理filter、writer与query-time utilizer时，总reward的组内优势仍可能把下游偶然成功同时奖励给上游。一个条件分支在主GRPO之外另建角色偏好对：writer只按源忠实性与具体程度组成的memory-quality分数选优劣，并按分差加权；utilizer只按query-profile效用选优劣，另用两份上游bank的entry集合相似度筛选比较人口，再对相应角色生成的trace施加辅助loss。[SaliMory的受限配方](https://arxiv.org/html/2606.04120v1#S3.SS4)提供的是角色分数、pair资格和loss归属接口，不是三个独立模型，也没有取消总episode reward。

相似bank不等于相同信息：较低Jaccard阈值仍可放过关键entry不同的pair，不能保证profile差额只来自utilizer；角色trace的loss分开也不使共享参数独立或免于相互干扰。比较应保留query、source/bank版本与实际输入差额，不能靠“causal gate”名称代替同bank控制。受限消融支持辅助偏好训练的局部效用，却未单独隔离相似度gate及其阈值的收益；judge、gold与标签构造、多rollout、pair评分和顺序建库都计费，异模型时延不授纯机制加速。监督不可靠、pair失配或共享policy回归时，保留outcome-only、固定writer/reader和原episode回读，不让较高memory reward取得事实写入或用户授权。<!-- source-family:SF-2026-ARXIV-2606-04120 -->

### 完整下锚（当前Ch77:201）

只用最终 QA reward 训练 memory policy 成本低，也适合短链路、固定 schema 和容易人工检查的任务；但它不能回答某段中间 memory content 是否真正帮助了最终答案。一个实验性分支是固定 retrieval/answer interface，对 memory token 或 span 做 masking/counterfactual scoring，把对 answer score 的变化映射为 local process reward，再与 global outcome reward 合并。它把“这次答对了”推进为“哪些被写入的内容可能贡献了这次答案”，从而给 admission、update、compress 与 discard 更稠密的学习信号。

## 交接状态

本项首次必要/正式6分/actual Ch77最小两段PRE ready，待唯一reader首次核原域/score/owner/literal；**未写任何Books/本人注，I24保持**。RAMPART04628、EvalStop04145、MultiSPIN04581与finite title stop/最终六节/DAY仍ordinary，不等本项POST扩Methods或NAV，不预普通0/终态。State/index/其它日未动，无stage/commit/push。
