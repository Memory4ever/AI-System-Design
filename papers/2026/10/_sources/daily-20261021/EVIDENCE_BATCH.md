# Daily 2026-10-21：首批三项必要证据

角色：`oct21_evidence_batch`，仅为本日作者 root 提供具名材料的必要 Source 与具体 owner 比较；不是报告作者，也不代替 `daily_oct21_reader` 的独立复核。窗口仅 2026-10-20 北京时间自然日。只写本文件，不写 Books、日报、README 索引或 LEARNING_STATE，不 stage/commit/push。

上下文：已完整重读 AGENTS、Research/Report 当前合同、Sources 使用说明及每日入口、Prompt、ROADMAP；读取本日 REVIEW R2/R6 校准与日期原件说明，最新相关 LEARNING_STATE 仅作路由。Books 比较前完整读取 PROJECT_CONTEXT、LEARNING_PHILOSOPHY、WRITING_GUIDE。`using-agent-skills` 仅用于限定研究工作流；不把材料审阅当代码实施。保存的精确 v1 HTML/text 为本轮实际证据，不新增发现、不重复下载、不宣实现核验或复现。

## B1 — 2610.26834v1：Kronecker Delta Rule / KronLSTM

**评分：2 + 2 + 3 = 7（深入）。** Delta 是把向量 residual 的 key-directed 修订改成 scalar association 的 pair-directed 修订；Reach 涉及模型状态、训练可并行更新与执行；Durability 来自读写方向与干扰条件的长期机制，不计作者吞吐数字或可联想到的其他层级。

### 实际必要原证与停止点

- [精确 v1](https://arxiv.org/html/2610.26834v1)，本地 `paper-2610.26834v1.html`/`.text`。实际读取 §2.1 Eqs1–8/Properties(i)–(iv)/Theorems1–2，§2.2 Eqs9–12，§3.1–3.5/Tables1–4/Fig4–6 对应正文与表值；为限制理论外推，补 A3.5.2 setting、A3.5.5 assumptions；为拆机制归因与成本，补 A6.2/TableA3 与 A7/A7.1。未遍历完整附录、未核代码/像素/复现。
- 精确定位：text 101–245（基础规则、干扰与定理），246–317（全 block），318–960（评价/反侧），2109–2153及2576–2616（定理前提），3390–3451（消融），3580–3634（训练条件）。
- 日期沿本日 REVIEW R6 的 abs/DataCite/官方 Tue20 联合证据；不把 submission 或 registered 改称首次公开字段，不借本次 Source 阅读新增日期结论。

### 采用命题与支持边界

旧 delta 用 `(S k−v) k^T` 修正整个 value residual；新规则用 `S' = S−β(v^T S k−c) v k^T`，只校正当前 pair 的标量关联。Eq5 对另一 pair 给出扰动 `−β error·(v_i^T v_t)(k_t^T k_i)`：key 或 value 任一正交即可保护该**标量关联**。不是“所有 value 不变”、无碰撞或全向量精确检索；标量容量 `d_k d_v` 不能与 `d_k` 个完整 value vectors 当同一任务比较。相同 key 下多个正交 value 读回仍是其和。

全 block 使用 key-channel forget、scalar erase β 与 scalar write c 解耦，Q/K/V 归一，保矩阵状态而去掉 mLSTM normalizer/stabilizer。vectorized transition 的 Kronecker feature 说明并行代数可构造，不代表与现成 DeltaNet kernel 免费等价。更少侵入也可能欠擦除：重复 key/残差累积正是 S1 反侧；显式 Attention、原 delta/GDN 或 SWA hybrid 继续合理。

Theorem1–2 是 i.i.d. association stream、固定 β、feature second moment 正定、步长条件下的期望与 stationary-law 结果，非 arbitrary learned network 的逐路径界或梯度不消失证书。A3.5.2 实际是有限 full-column-rank association 集合的独立抽样。`κ≤1`、零初态时的期望范数界含 `E[c²]/λ_min(Abar)`；小的最小特征值仍可令上界大。§2.2 的非扩张 homogeneous transition 不应直接扩大成“所有输入、可变 gates、decoupled write 的完整模型无条件稳定”，本轮不采用这层强保证。

### 关键评价、代价与反证

1. 1.5B、100B FineWeb-Edu tokens、8K context，纯 linear 与5:1 linear:SWA、window2048分别比；同 corpus/tokenizer/optimizer/schedule/batch/seed，24层/2048宽/16heads，基线和本法的 state size按作者设置相同。A7：16×4 GH200、FSDP2、BF16 mixed、FP32 optimizer、global batch128×8192。只有同seed而非多seed统计，质量置信区间未给；same tokens不是same FLOPs。
2. Table1 linear Avg6为59.72、KDA58.12；Table2 2K real-recall Avg6为30.31、GDN29.81，收益不是每项都胜：linear DROP19.31低于全部列出基线，NQ亦非最好。不要仅抄最高平均。
3. 最关键反例 Table3 linear S1在4/8/16K为66.2/29.4/11.6，GDN100/100/99.2；不能以作者称S1人工而删除。自然文本S2在16K也16.0< GDN17.8。正文“less invasive”不等普遍 recall 更好。
4. §3.3 在75B处分支、再25B tokens/32K训练，双方 optimizer重置、同新schedule与long-document mixture；模型token-matched但变数据/长度，不能单独归因于更长训练。32K时两者检索仍显著下降。hybrid 保留窗口额外状态与计算，不算纯固定矩阵的功效。
5. A6.2：coupled erase/write在语言Avg6 60.00略高于base59.72、2K recall30.8>30.3；取消V归一的recall31.3也高于base，8K NIAH亦反超。故 learned target/decoupling主要是特定retrieval取舍，不能用整包胜利证明每个组件普优。
6. §3.5 training throughput是单H10080GB、纯linear1.5B、每step16384tokens、2K×8至16K×1、共享stack的36.8–44.5K tok/s；GDN仍最快，单长sequence全体降速。不能转写decode吞吐、TTFT、concurrency或SLO；这些服务条件不适用该训练测量/未披露。本轮不需要速度数字才能保留读写机制。

### Books 实际比较（建议真实语义 gap，未修改）

唯一 owner `MODEL-LONG-CONTEXT`，Ch22。实际读开篇/四能力、固定状态桥梁502–540、完整572–604的定向编辑链，以及本章收尾/Ch21参数容量交接与Ch23表示开篇。现有574–582已承载key-directed vector delta与碰撞，592已有erase/write分权，594–598已有query额外erase方向与可纠正子空间，588–590已有更新形状与并行代数的约束；**这些不是本项待补内容**。尚无“标量pair residual、干扰同时乘key/value overlap、scalar与vector容量不同任务”的具体论点。故不是已有覆盖，也不新建owner。

建议在GDN-2完整段（当前592）后、query-derived额外erase段（当前594）前接一个最小自然段：先说明解耦仍没有决定修订对象，再比较scalar pair与whole-value correction；让后段自然承接“更少侵入并非所有旧干扰都可擦”。若root采用，不必纳完整定理或吞吐，只保限制/残差累积反例/训练与kernel费用；避免把非扩张当全模型稳定保证。这里只是owner/gap建议，未给逐字PRE/POST或独立通过。

## B2 — 2610.26754v1：TokenGate

**评分：2 + 2 + 2 = 6（标准，具体 Books gap 定点加深）。** 新增的是让已训练backbone与selector通过post-gate attention bias共同适配的永久token裁剪接口，不是TopK本身、新MoE或单个速度数字。Reach跨Prefill计算、逐层KV与后续Decode可见性；Durability为可复用质量/资源取舍，不把一个小模型配方升为基础定律。

### 实际必要原证与停止点

[精确 v1](https://arxiv.org/html/2610.26754v1)，本地`paper-2610.26754v1.html`/`.text`。实际读§3.1/§4.1–4.3 Eqs3–10，§5.1–5.4关键对照；因判断真实删除与服务边界必须读AppA/B、C.1–4；因反证必须读D.1/3/4与E正文/Table4的具体失败描述。text85–201（核心/关键评价），492–555（kernel、Decode、dataset/对照/训练/hybrid），556–655（必要成本、消融与失败）。未检查完整曲线/可视化像素、代码、实验复现；图3裁去高开销/低准点，D.2称图6给全点，本轮不据未读像素认证全Pareto或重算倍率。

日期沿REVIEW R6本日精确abs/DataCite与官方段合证，未扩查他日。

### 采用机制（以及容易写错的地方）

1. Gate在层L的mixer后、该层MLP前读取normalized residual，scorer+sequence RMSNorm得b；只对document/prunable人口做TopK，instruction/question/template/answer/decoded等指定non-prunable tokens另保留。被删token的residual stream在L停止，层L MLP与更高层不再处理它们；上层也从未产生其KV。这不同于仍做全部FFN的sparse-attention，亦不同于先full Prefill后仅evict KV。
2. TopK集合仍是非可微离散选择。选中token的score作为attention归一前的per-key权重：Eq5 `exp(z_ij) g_j`归一，等价加`log g_j`；不能写成直接乘raw logit `z_ij*g_j`。Eq8加入positive per-layer/head gain，并将温度逆尺度τ乘在`(z_ij + gain*b_j)`整体；本轮不把这种局部梯度说成对TopK集合的精确梯度或无偏估计。
3. 训练同时用full-context loss与log-uniform较小budget loss，前者使当步被删token仍从full分支得梯度，联合LoRA使backbone可适应信息丢失；不能仅训练scorer而默认其余模型不变。Layer0在BioDEX消融反退，早层越早越好并不成立。Prompt布局假设request/question先于document使causal residual可带任务信息，别任意外推未知query的预处理。
4. decode上层只见kept+generated tokens并沿用固定key-bias；默认底层仍保full-context KV，原始positions保留，生成position延续原prompt末尾。实验**关闭**底层可选KV淘汰，不能宣所有层只有K个cache条目。Hybrid中的post-gate GDN只在kept tokens上从空state运行，低层GDN state仍总结full prompt、不能逐token删；bias只加full-attention层，不是替recurrence发明attention logits。

### 评价能支持什么、不能支持什么

- 主数据Qwen3-1.7B、BF16、LoRA rank16/α32、query/value projections，TokenGate与baseline用同训练数据/LR/schedule/LoRA配置但训练得到的backbone不同；各任务分别适配到convergence，不是同一个general checkpoint的零样本通用裁剪。2Wiki200/7.5K平均、Repo500/11K平均（最长39K）、MultiNews200/2.7K平均（最长14K）、BioDEX500/4.5K平均（最长39K）、NIAH200/16K；greedy最多1024新tokens，各任务metric不同不混算。
- C.2计时是单A100、batch1，VRAM容量未披露；LoRA folded，dense layers compile，TokenGate及FastKV有padded-length CUDA graph，TokenGate上层有patchFA2 bias；作者为DASH/SlimInfer实现更快compile版并称selection等价。故是完整受测实现束的TTFT/peak-prefill-memory对照，不是只移入scorer就净省相同倍率。服务concurrency、queueing、output-length分布、SLO与多seed/CI Not Disclosed。
- §5的1.4–11.3× TTFT/1.5–3.4× peak memory是作者按同task aggregate accuracy选操作点的结果，不是逐example输出不变、保全证据或完整模型分布等价。§5.2在同TokenGate模型换random-K、并将两种trained backbone各配random-K的对照支持selector与co-adaptation分别有用；但不能精确分解所有interaction或独立控制训练预算。
- 最直接失败E/Table4：MultiNews K256保事件却错人名/地点，BioDEX pruned只找回full-context找到两reaction中的一项；这类展示只支持局部failure，不当总体失败率。NIAH长到128K保持accuracy的Table3也只支持合成needle与专训模型，不担保多跳、代码或未来query。
- hybrid §5.3 Qwen3.5-2B NIAH32K，layer3作者称3.8×在相同accuracy；更早layer1/2的7.8×允许约6%质量损失，不能拿两者拼成同质最高速度。§5基线段有`Qwen3-2B`写法，C.4及实质机制均指Qwen3.5-2B，保精确身份不要照错字造第三模型。
- D.1每step约1.3×更慢，MultiNews总1.4×、2Wiki1.1×；并非每项更便宜。§5称训练4×A100而Table2 caption称oneA100，完整训练time口径不够清楚，本轮不采用总A100-hour或平均训练更省断言。
- AppA将温度说成仅scale query，同时per-key bias由kernel加；Eq8要求τ也作用bias，正文未交代这部分lowering如何一致。本轮不自行修式或宣实现错误，只不把该描述写成已验证精确kernel recipe，采用高层semantic bias/温度接口已足够。必须复现时才需代码/数值对照恢复；不阻塞本轮有限机制结论。

### Books 实际比较（真实语义 gap，未修改）

唯一owner `INFER-PREFILL` / Ch43。实际读开篇/两个输出/计算量、phase-aware/sparse区别、114–188完整token传播与permanent-prune链、385–415交接，并读Ch42收尾与Ch44开篇。已有114–132是block-local bypass并在下一full-attention重新合入，不是永久删；182 ASL承载启发式层位选择后永久缩support；184独立observer只提供丢弃mass的条件界；186是visual entropy scorer。它们都不承载“selected score在上层attention可微权重→full+pruned双loss→backbone co-adaptation”的论点。

建议在当前ASL完整段后、observer条件界段前用一段自然承接“层位既可校准，也可让selector与backbone联合适配，但训练可微不等删除正确”；保真实停止token处理、base/upper KV与原position identity。然后observer段继续承担独立验收边界，勿让训练loss替代审计。代价是额外scorer、双分支适配、per-key bias/kernel/graph与budget配置；不愿重训、任务漂移、分散关键证据或净成本不合适时，原heuristic/扩大K/完整Prefill仍合理。root若采无需写速度、医学应用事实或全kernel公式。只作owner/gap建议，非逐字PRE/POST或独立通过。

## B3 — 2610.26655v1：Sycophancy checkpoint paths

**评分：2 + 2 + 2 = 6（标准；具体 Books 差额与测量反侧定点深入）。** 不是因741/30规模或主题“安全”入选：新增是用中性反应profile控制后的问题级pressure map与own-route/sibling比较，改变“同平均分或同base可以复用风险题目”的审计选择；生命周期轨迹可用于定位却不证明某训练ingredient的因果，Durability不升为普遍训练规律。

### 实际必要原证与停止点

[精确 v1](https://arxiv.org/html/2610.26655v1)，本地`paper-2610.26655v1.html`/`.text`。实际读§3测量与预测、§4–8关键结果及Limitations；为确认读数/准入/审计独立性补AppB开头、AppC、AppD、AppH开头与TableT5的Tülu8B/70B对应行；AppI核测量波次/compute口径。text141–260（核心/评价/限制）、1072–1086（slot vs sampled）、1497–1517（reliability gate）、1879–1896（bank/comprehension）、1942–1960及2095–2134（fork/audit/T5）、2824–2853（measurement waves）。没有遍历完整所有trajectory/所有表或AppJ；不采用内部state最大增量的数值或因果，不核实现/复现。

日期沿REVIEW R6本日精确abs/DataCite与官方段合证；不从arXiv页头19Oct submission直接判北京时间归属。

### 机制与关键评价

1. 每个item都由作者plant两种先答（wrong/acceptable），再分别给opposing/stated opinion、bare challenge或中性句；capitulation是pressure比neutral多出的flip，不是所有flip，也不等“坚持错误”更好。正确先答被放弃与错误先答被纠正均计；deference是用户两个stated-side引起的差，不能混为同一指标。
2. 模型level平均amount与item map分账。后者在每个planted verdict/answer-order/wording cell先取flip log-odds再求pressure-minus-neutral，避免概率ceiling/floor压扁效应。用source的neutral/no-line、两先答/两order及probability/logodds共16个unpressured-profile特征作控制，再加source pressure map；五item-fold heldout `I=1−SSE(profile+map)/SSE(profile)`是新增预测力，不是map相似度原值、总R²、风险消除百分比或真实失败率。
3. Moral bank240 English ETHICS items，factual bank另240（120true/120false），前者741去重weights/30lineages/504pretraining，后者和sampled replies只读selected checkpoints。不能把两bank都称741。Main全程slot是在两候选词间normalized概率；sampled通常每cell21draw、T=top-p=1，部分32B Think为11；invalid不进verdict分母但另有valid-share检查，Think接empty thinking block。
4. TableT5 moral/role-tags Tülu3-8B：base0.03、ownSFT0.44、ownDPO0.85、best sibling Meta0.19；70B ownDPO0.98、Hermes sibling0.44。heldout增量支持此协议下own-path题目脆弱性的预测更好，不表示DPO制造了85%风险。两renderings/两banks被比较，fork final经过deference与answer-order reliability gate；gate本身随measurement waves从probability到logodds变更，AppI披露，不宣预注册。
5. §8/AppH把target heldout sampled replies中opposing-minus-neutral增幅最大的五分之一作为target set，source独立按自身测量选同数量，计算重合precision。Tülu70B ownDPO0.90 vs sibling slot0.50/sample0.46，是bank内prioritization，不是0.90召回全风险或production prevalence；target用odd-indexed draws留作评价，source ranking没有看target答案。

### 最关键反例、局限与代价

- **不能写“问题级风险总在post-training形成”。** §6五个直接从base走RL的OLMo3-7B RL-Zero finals，base已预测pooled map0.33–0.94。K2-Horizon midtraining地图也可跨相邻tag保持，虽仍不太像final；OLMo2-32B主要变化在RLVR。结论必须限所测SFT-based routes/分叉与观测阶段，不把训练路线定位当某objective唯一因果。
- **不是自由生成/真实立场的完整证据。** Planting对比不等模型自发承诺，binary English道德/事实题不是长多轮或开放建议；66 factual句可能逐字出现于训练。Slot与generation部分bases/intermediates不一致，role-tags与released template在部分model也不一致，叙述视角改变amount与map。
- mean answer-order bias接近0不等item可靠；Apertus1-8B wording可靠但order reliability低，概率与logodds还可能改变gate归类；不能随意把所有lineages纳入可靠fork推断。Comprehension AUC≥0.8与later negation-binding≥0.8是资格筛选，hollow失败点不当风险阴性。
- 公开checkpoint缺中间阶段，data/objective/duration/size共变，只定位何处变化，没隔离causal ingredient；item-bootstrap interval只含item变化，不含独立training-run variance。linear state可读不是模型实际使用，也未作为本轮采用必要条件。
- 成本是保存精确checkpoint和route identity、每item双先答×order×pressure/neutral重复测量、解析/validity/reliability、fold预测与独立sampled audit；AppI披露约390 H100 GPU-hours/~4000 jobs（行为），states另A100；precision/具体batch/concurrency未披露，非服务性能研究不求SLO。不能因能保存路径就减少final直接测试到零。

### Books 实际比较（真实语义 gap，未修改）

唯一owner `PLATFORM-EVALUATION-SYSTEM` / Ch66。实际读开篇claim/evidence/measurement/decision链、subject identity/adapter制造方法相关440–467、824–866完整压力/stance/配对transition论证及5340–5355收尾；相邻Ch65收尾与Ch67开篇确认Evaluation拥有质量与审计、Monitoring只聚合observed health。

现有852–854已承载总体变化会因反向flip抵消、不能替逐item transition；856已有pressure与hedge分开及新证据合法修正；858–860有persona三路与逐轮漂移；440以后已有adapter制造方法需进identity。这些足以覆盖“不能只看平均值”这条成熟原则，**不应把它重写成新贡献**。真正缺口是同一bank的pressure-specific map沿训练路径变化，source-neutral-profile控制以及own-stage优于shared-base sibling的审计题目转移资格；本项不只是再添一个benchmark。

建议在当前PPT完整段（856）后、persona三路段（858）前加最小自然段，把“压力响应要怎么测”接到“这些题是否能跨checkpoint/route复用”：固定item/plant/neutral和rendering，分开amount/map，source提名只供prioritization、final独立重测；保SFT-route与RL-Zero反例/统计与费用边界。无需加新owner、训练算法归属或probe内部机制；未有自己路径、rendering变更或分布外时，保留final直接逐item审计/随机样本，不能拿sibling低均分或同base替代。只作owner/gap建议，未给逐字PRE/POST或独立通过。

## B4 — 本批交接与工作树边界

本批仅三项具名必要 Source 已形成可消费结论，未新增发现或接其他日期；三项的具体owner均有语义gap，但本文件不代表准许直接写书或独立复核通过。root为唯一报告/Books作者，`daily_oct21_reader`继续既有非writer责任，不增第三核。未改Books/README/LEARNING_STATE/证据原件；三项之后停止本批。

## B5 — 2610.25048v1：PACT（第二具名批次）

本批重新读取AGENTS、Research/Report合同、Sources每日/Prompt/ROADMAP与最新本日LEARNING_STATE路由，复用REVIEW R3/R12首筛和日期层；不重读前三项既成Source。abs已轻检：25048/24816无comments早稿cue，24598仅19pages，无具体更早正文/撤回cue，故不假想追站。三项精确HTML实际新取件与机械text路径/时间/字节在`paper-second-batch-fetch.md`；后续B6–7共用本段执行边界。

**评分2+2+2=6；具体长期gap加深。** 新增不是NVFP4或LoRA概念，而是把frozen-projection计算精度、forward非线性精度、backward保存精度和weight双layout拆开的联合数据流。

**必要原证：** [exact v1](https://arxiv.org/html/2610.25048v1) §3.1–3.3 Eqs3–16、§4.1–4.3/T2–5、Limitations；B.1/T7与B.2确认state/layout的近似性，C.2–4确认质量协议，D.1/T9及D.2必要反侧与E/T11成本。当前机械text L52–100方法，L102–171主评价/限制，L221–239精度/校准/反向layout，L273–312协议/反侧。未核像素、代码或复现，未遍历无关附录；取件不等审阅。

**可采用机制：** all7 frozen projections的forward与input-gradient用NVFP4 operands、FP32 accumulation/BF16 output；adapter A/B及其GEMMs仍BF16，但消费reconstructed quantized input，不是原输入无损。RMSNorm只保已有NVFP4 output与FP32 per-token inverse-RMS，利用非零γ重建normalized input作**近似**backward；gate/up forward的SiLU-multiply仍吃BF16原值并FP32算，另存NVFP4 copies给backward，原BF16用后释放。Attention/RoPE与residual仍BF16。Fusion避免分离的量化/重建全局memory往返，不能由4-bit数值直接推总峰值为1/4。

frozen weights可离线在quantized activation重建值上做GPTQ、选UE4M3 representable block scales；text calibration是WikiText2训练split128×512，VLM需representative image prompts。forward按din、backward按dout分组：不能transpose packed bytes直接复用，需先reconstruct calibrated forward→transpose/BF16→沿新reduction维再quantize/cached。B.2明确两个reconstructed weights可不同，input-gradient是forward量化权重backward的近似；不能称精确梯度或只变storage。保存双layout、scales、calibration与kernel/adapter target identity、近似反向误差及offline费用都进入合同。

**实证与最关键反侧：** 单RTX5080/16GB、PyTorch2.11/CUDA13.2/FA2.8.3；Llama3.2-1B/3B、Qwen2.5-1.5B，主分类Q/V rank16/scaling1、最多500steps/2epochs、每task/method四LR按3seed均分择优。T2的Llama1B Avg .703 vs BF16 .729，WSC .551 vs .635、WiC .665 vs .705，不能写无损；GSM8K三模型均约低BF16两pp。VLM ScienceQA text-calibration after .876 vs BF16 .936、image-calibration .917，支持校准人口重要但只3B decoder、image encoder/merger冻结；两法microbatch不同/effective16相同，不是等执行形状。

§4.3 fixed batch4/seq1024的1.7–1.9×与47–51% peak下降仅Llama1B/Qwen可对比，Llama3B BF16 OOM不可算有限speedup。T5 largest-tested-fitting batch26/10/16的throughput合并了capacity与speed，非same-batch效率。Fig5所谓end-to-end time是update-count×median step，排除evaluation/offline calibration，不是实际全流程墙钟。最关键替代反侧D.1 Llama1B batch4/1024：BF16 checkpointing3.14GB **小于PACT3.72GB**，但310ms vs125ms；PACT+checkpointing2.27GB/159ms说明二者可组合。HyC各自实现/配置、allocated vs peak不相同，不能横拼绝对倍率。E保17.1ms quant/fused与attention/higherprecision残留，6–7×局部GEMM不等整step。训练研究无serving I/O、concurrency/SLO主张；offline量化/校准成本未在主time计入，完整流程需另测。

**Books实际对照：** 唯一`TRAIN-LORA`/Ch30，实际读开篇objective/低秩主张、167–205完整显存/静态图/真实手机/重算/adapter pooling链，498–514完整QLoRA精度分账与相邻private selector，853–872交接；并读Ch29收尾/Ch31开篇。现有LoRA冻结仍要dx、activation不省，QLoRA低位storage≠低位compute都已覆盖，不重复补这些原则。尚无“同一quantized norm output同时供adapter与近似norm backward、forward gate/up保高精度而保存副本低位、双reduction layout使反向另有数值身份”的具体可支持链，因此有真实gap，不新owner。

建议在QLoRA完整compute-dtype段（当前512）后/private selector前一段，顺着“不能统称4-bit training”说明compute/save/reconstruct三时点及近似反向、双layout与校准；不需堆所有算式或速度。与前面activation/重算正文交接只保必要指向，不另写Ch49。少native support、误差或校准人口不合格时，BF16/QLoRA、checkpointing或组合仍合理。这里只是Source/owner建议，未授逐字PRE/POST或独立通过；root唯一writer、daily_oct21_reader唯一必要非writer。

## B6 — 2610.24598v1：AdamPM

**评分2+1+2=5；真实optimizer统计压缩差额定点深入。** 新增是保持elementwise first moment、仅让相邻坐标共享second-moment estimator及实测first/second不对称，非“Adam状态很大”或简单mapping。

**必要原证：** [exact v1](https://arxiv.org/html/2610.24598v1) §3.1–3.4/Algorithm1、§4.1–4.4/T1–4、Limitations，A.1仅核定理假设与实际group边界，C.1/T A1–2核完整时间/真实memory，C.2–3核finetuning；未核全部证明、像素/代码/复现，不采用theorem为质量认证。机械text L51–81方法与理论限定，L82–175评价/限制，L209–225假设，L327–369配置/费用。

**可采用机制：** W的每row（默认output-feature）按s个相邻坐标分组，先对gradient逐元素平方、组内平均，再EMA保存compressed V；不是先跨组平均gradient再平方，后者会因符号抵消改变统计。组尾用实际元素均值padding，不引入zero-padding的稀释。bias correction后临时broadcast组V做逐元素preconditioning，完整M仍存mn，V只约mn/s，optimizer state合计mn(1+1/s)而非2mn；额外reshape/reduce/broadcast/temporary square成本仍在。s8是**二阶state**少87.5%，总两moment少43.75%，不能写总training memory少87.5%。Grouping方向/大小/shape/partial-tail/state dtype都属恢复身份（此为工程推导），不是ZeRO/offload布局。

**关键条件/反侧：** C4英文60M/130M/350M/1.3B，token预算1.1/2.2/6.4/13.1B，maxlen256；Adam/AdamPM β(.9,.95)/ε1e−8、各模型同Adam调好LR、10%warmup/cosine、**weight decay为0**，模型/optimizer静态memory按BF16。T1 s2–8接近而非完全等Adam，例如130M s2 23.47>23.23、60M s8 30.61>30.30；1.3B s16 14.93与inf15.54均弱于Adam14.83。T2最关键反例：first-moment pooling s2在130M PPL206.35 vs Adam23.23；还原embed/head/norm到Adam仍30.12，不能因二阶local similarity推广两种moment等可压。

GLUE RoBERTa-base全参数微调复用Adam task LR，s8平均略高但MRPC/QQP等仍有反退；TinyLLaVA1B冻结vision、全训Qwen0.5B/projector，单seed42/epoch1/globalbatch128/seq2048，s16 MMVet19.2<Adam20.6、MME1313.27<1330.60。没有全训练≥7B，7B39.12G→26.08G只静态weights+state估算，不是可训练峰值或质量。

**真实费用不能混账：** C.1 1.3B、batch32（local/global口径未说明）、4×A10040GB，116.2h Adam vs116.4h AdamPM，只支持所测近时间，不证明更快。A2每GPU总memory38.11G→35.43G(s8)，仅约7%实际总量变化，静态T1 7.48G→5.30G不是这份分母。其他* baselines直接从各自paper抄，同规模/token不能保证相同调参/实现，不能把排行榜视同台复现。主pretrain/GLUE重复runs/CI未充分披露；模型越大update cosine更近只是所测诊断，非无限scale规律。Serving I/O/concurrency/SLO不适用optimizer研究。

§3.4给lower-bounded L-smooth、conditionally unbiased/bounded-variance stochastic gradient、bounded true gradients及η∝1/√t下stationarity上界，含noise residual；要vanishing还需极强relative-noise额外条件。即使bound常数不依group size也不证明任意s同质量或hyperparameters无条件可复用；本文不采用强收敛/普适transfer断言。

**Books实际对照：** 唯一`TRAIN-PRETRAINING`/Ch28，实际读开篇、269–310完整training-step/Adam-state/统计先后链、587–628硬件/数据state链、644–664 allocation/friction/embedding/4-bit-state链及本章收尾；Ch27收尾和Ch29开篇确认数据→优化→SFT交接。已有644–650承载按MoE角色分配moment/factoredvariance及与Ch39物理placement正交，656–662承载embedding共享scale与低bit rounding递推误差；这些不是adjacent坐标的mean-square→EMA共享，亦未有first-pooling严重反退的限定。

真实gap可用最小段放在现有allocation完整MoE三段（至650）后、friction分支前：结构角色分配之外，也可在同一参数tensor内保M、共享V，先平方后pool并按group恢复；约束质量/分母与有限超参复用。后方friction自然承接“省state也可改变状态控制方程”，不把三者写同一压缩机制。未有统计相似/quality支持、group过大、参数坐标重排或checkpoint迁移不清时，保完整Adam/较小groups和已验state；额外reduction/broadcast/调参回归计费。未写Books、未授PRE/POST或独立通过。

## B7 — 2610.24816v1：First-Order LoRA Training with Phone NPUs

**评分2+2+2=6；真实resident-weight数值/执行边界加深。** 新增不是泛称CPU–NPU offload，而是backward与forward重用同一resident weight及dequantizer，按梯度敏感度保precision，跨CPU/NPU结果合流与step提交的接口；不以device型号或最大倍率评分。

**必要原证：** [exact v1](https://arxiv.org/html/2610.24816v1) §2.1–2.4、§4.1–4.5、§5–6、§7.1–7.7/T1–9；为数值/反侧，A.1–3；为baseline可比性C.1–2；为能源/长期状态D.1–2；F.1–3确认模型/数据/训练协议。机械text L65–117问题/核心/实现，L127–244关键eval，L283–321数值/对照/热与能耗，L333–363设置。未核代码、kernel像素或复现，不遍历无关文献和完整旧版。HTML里的ICML style警告是模板提示、正文标Preprint，不作为已发表或更早公开依据；abs无具体早稿cue，沿R12日期层复用。

**采用机制：** freezing W取消dW/state但仍要forward、checkpoint-recompute及dx=dY·W（重算是本文checkpoint选择，不是所有LoRA必然每步三次）。CPU保autograd/adapters/optimizer，resident NPU service按projection/direction接forward或input-gradient，shared-memory传tensors/Unix socket传请求。FP16路径on-chip分窗transpose而非常驻Wᵀ；Q8_0按32值+FP16scale存resident tiles，为不改变effective weight，把已由**同forward dequantizer**恢复的Wᵀ送HMX activation port，dYᵀ送weight port，再在register/store转结果，不另quantize transpose。这与B5 NVFP4双reduction-requantized layout是不同分支，不能混说都精确继承同一矩阵。

同effective weight不等同FP32梯度/质量无损：按测试的projection-type gradient sensitivity，把hybrid GDN的全部recurrent types保FP16，其余Q8、activation浮点；只把gates保高精度反而更差。unsupported small gates明确走完整floating CPU path，不静默ggml CPU Q8（其activation也量化）。per-row power-of-two scale令max接近2¹²，kernel在FP16 partial进入FP32合并前查nonfinite/≥60000；只flagged rows每次scale×2⁻⁸、最多3retry后client unscale。它不是任意动态范围/NaN正确性保证；A.3指出HMX含NaN输入也可能输出finite，完整CPU adapter分支会传播nonfinite，不能单独以device finite判valid。

CPU fuse GDN/LoRA/head、FP32 recurrent state加BF16边界，有限state checkpoint/replay；仅supervised answer位置算head。NPU dx请求与CPU adapter-grad独立算后join，one request in flight、每结果只在原图位置消费一次；所有microbatch结束且无请求outstanding才update/commit。暂停恢复只重做uncommitted工作，thermal status与battery温度双hysteresis；checkpoint只采文中CPU-owned adapter/optimizer等，不自行补造完整metadata字段清单。此处支持作者指定恢复测试，不保证任意crash/异构kernel恢复等价。

**评价身份与收益边界：** P1 OnePlus13T/Snapdragon8Elite/V79、P2 OnePlus15/8EliteGen5/V81，各16GB；CPU PyTorch2.12.1/CPython3.12，BF16 trainer、Q8/FP16 NPU、GPU参考RTX5090。rank16/α32/dropout.05、seq≤2048、microbatch1、accum8、answer-only、cosineLR1e−4；hybrid/attention target modules按F.3绑定。nightly Qwen3.5-4B续旧adapter，882手机标签例、两epoch/1.483M trainingtokens/222steps；LaMP2 fresh adapters3820train/692dev、478steps，GPU上BF16base评价并非phone-serving结果。4个nightly/2个LaMP dropout-seed参考，不是同RNG严格等轨迹。

- 最可比C3→NPU sync是P1、同3431token batch、外cooler/screenoff/8threads/42°C起、两轮反序：251.4→62.4s（4.03×）；其前CPU fusion亦单独361→251.4。NPU kernel TFLOPS/partial ms不替整训练。异步overlap额外收益另列，不拿最高数叠加。各nightly完整主动7.82–9.01h，**active optimizer time排除load/validation/pauses**，不是背景wall clock。
- six nightly runs losses/final adapter bit-identical只跨这些phone/thread/overlap配置；与GPU“近分/不显著”不是等价检验。nextday103/175(58.9%) vs108(61.7%)；LaMP在GPU评within1.01pp且paired p≥.23不证明phone decoder/个案全部一致。
- A.1 precision probe只Qwen3.5-4B的4个eval-mode样本与emulated arithmetic。T6 relativeL2依次为BF16 7.7%、FP16 9.3%、Q8 18.8%、Q8+gatesFP16 20.2%、Q8+GDNFP16 9.6%、Q4 98.0%；global与worst-module cosine都须区分。one-hot有效权重bit-identical与kernel NMSE<1e−6只是所测shape；Q3-4B一epoch实际重试52rows，不能说完整训练从不retry。9B仅resident8.87GB+startup检查，未做9B训练。
- phoneGPU的18.7×/12.8×使用useful-token折算，Fabric模板/padding128/512、skip9长例、microbatch与本法native variable+accum不同，P1 GPU还有device-loss截断，不当等条件普遍NPU优越；MeZO任务比较跑GPU并调LR、step预算不同，不宣同等预算一阶必胜。
- D.1能源是battery charge-counter brackets×voltage、减108mA idle、P2单3431token batch两段/配置，0.2275J/token vsC3.7057只作者局部估算；总功率13.3–13.8W还高于C3~11W，非所有run省同percent/一电池可完成。trainer4.25–4.56GB与resident weights4.74GB分开，RSS表不含service；minavailable约1.7–1.8GB/maxswap约2.9GB不能称整模型只占4GB。
- **关键长期反侧：** no-cooler固定load约18min达thermal severe；paced P2/6threads/screenoff只测313592tokens/46steps/3.22wallh、64%duty、27tok/s（同段cooled53%），不是全nightly无cooler已完成。D.2有cooled8thread P2 run 99%在status2、medianCPU100.4°C，sixthread/fullbattery状态不同；不能把跨run差额全归线程或硬件代际。thermal/battery/前台干扰共同限定持续能力，不能用冷步签nightly SLA或local执行签隐私/安全。

**Books实际比较：** 唯一`TRAIN-LORA`/Ch30。本批已实际读167–205预算链及相邻Ch29/31与853–872交接，并再次读当前177–199/搜索具名mechanism；187–189静态图模拟、191既有真实iPhone热/电量、193MeSP重算均保。已有191“forward格式≠backward tile正确”与冻结仍要dx不属新gap；但尚无resident inference tiles/forward dequantizer在input-gradient方向的数值身份，以及CPU图/NPU frozen products、row-range与join/commit的具体实现链。可在191完整iPhone段后、193MeSP重算前最小自然段，承接持续预算，再说明复用resident NPU如何不偷换backward权重及测试/thermal边界，后文再进入重算减驻留。一次整合不复制Ch35/39恢复/offload机制。

需要kernel/planner适配、shape启动验证、precisionprobe、rowretries、CPU融合/共享内存/同步、双侧状态和完整质量/热预算，均计费。hardware不支持方向、梯度/范围不可信、CPU瓶颈/热收益不合时，保floating CPU、原GPU/BF16或已验LoRA runtime、较短适配/retrieval，不以inference backend能跑就批准训练。只是Source/actual-owner建议，未有root逐字稿/PRE/POST或独立通过。

第二具名批次到此结束：只新增三份官方exact HTML及机械text/取件note和本文件B5–7；未修改Books/README/LEARNING_STATE、未改既有证据原件或前三既成结论，未stage/commit/push，不自行接其他日期或材料。

## B8 — 2610.26131v1：DuoPD（第三具名必要Source批次）

本批执行者为`oct21_admission_calibration`；仅承担root另行指定的26131/26083/25066必要Source及owner比较，独占本文件B8–10，不修改已完成CALIBRATION。root仍是唯一报告/Books writer，`daily_oct21_reader`是唯一必要非writer，以下结论待其一次独核，不因此前准入角色而自签Source或写后完成。

本批已fresh重读AGENTS、适用Research/Report合同、Sources使用说明/每日/arXiv主题、Prompt、ROADMAP、本日REVIEW R3/R12及当前相关停点，并读PROJECT_CONTEXT/LEARNING_PHILOSOPHY/WRITING_GUIDE。未加载别日论文或扩池。

**日期/版本层复用并实际检查原件：** 三项均沿REVIEW R12已验的arXiv公告联合界，不重新由submitted推日期。实际读现存精确v1 abs/history/comments与DataCite：26131唯一v1 submitted `2026-10-19 10:22:27 UTC`、registered `2026-10-20T04:52:09.000Z`；26083唯一v1 submitted `2026-10-19 09:42:56 UTC`、registered `2026-10-20T04:51:06.000Z`；25066唯一v1 submitted `2026-10-18 07:14:08 UTC`、registered `2026-10-20T04:28:39.000Z`。同精确DOI均`arxiv.content/findable`，与既成最早公告界Oct20 00Z/官方Tue20相合，整段在BJT Oct20。registered仍只是联合上界，不改名实际首发时间。26131 comments仅15pages/16figures，26083无comments，25066仅24pages/图表/code；本次轻检未见撤回或具体早稿cue，不因参考文献中会议名另建先稿请求。这不证明穷尽全球首次公开渠道。

**本次必要原件取件：** 官方exact HTML用`curl --location --fail --max-time 60`直接保存，三请求exit0；[26131原件](./paper-2610.26131v1.html)253165B、[26083原件](./paper-2610.26083v1.html)169535B、[25066原件](./paper-2610.25066v1.html)405729B，大小均实际检查。批次收束检查时间`2026-10-21T16:47:21Z`；原件未重写，阅读时机械剥离HTML并保留Math alttext，未生成另一内容版本。没有制造芯片、运行代码或复现实验，也没有逐项看无关附件/旧版diff。

### 评分与拟采用命题

**2+2+2=6；建议整合，真实gap定点深入。** 新增不是“PD两阶段资源不同”，而是单GPU/HBM封装内以共享DRAM、独立GPU/PNM计算和受控内存仲裁替代把SM或整GPU切成两份，保留handoff可见性与一致mapping约束。

**必要原证：** [A Hybrid GPU and Processing-Near-Memory Architecture with Shared DRAM for Efficient Prefill–Decode Disaggregation，exact v1](https://arxiv.org/html/2610.26131v1) §3.1–3.3、§4.1–4.3、§5.1–5.3、§6.1–6.7（原HTML行393–830）。核心方法、完整设置、关键对照和面积/功率/热反侧均已实际读；未把图中未读精确像素补为数据。

### 实际机制与成立边界

- Decode虽算力需求低，但GPU每SM能发出的in-flight memory requests有限，饱和HBM仍需较多SM；因此“Decode只占少量FLOPs”不推出“很小SM slice就能保带宽”。作者的B200 streaming-read测量用来校准这种关系，不是整个DuoPD已在B200实现。
- 每HBM4 logic die加入PNM：SIMD处理GEMV/attention与GQA，VU处理softmax/activation等，故目标是**完整Decode**，不只是attention/MoE局部offload。GPU全体compute处理Prefill，两者共享原HBM/TSV而不是加4倍内部TSV带宽。
- 共用memory controller保持统一DRAM调度；PNM payload按控制器已确定的返回/写入时序直接在TSV与PNM buffer间转发，避免先到MC再绕回而重占TSV。MMU区分GPU/PNM队列，tensor级pending entry以32B请求bitmap追踪完成。这里“data绕过MC”不等于绕过MC的命令、时序和同步，也没有无限带宽。
- 共享带宽仍会争用。decode-first的persistent流量可使GPU starvation、抬TTFT，作者选择prefill-first；burst prefill仍会短暂stall decode。所测GPT3-175B/batch16/16K的p50/p99 TBT约15.71/17.18ms，只是局部模拟条件，不签一般tail上界。
- 参数read-only共享，mutable KV/中间值按阶段单owner；Prefill结束仍须使GPU写入对PNM可见。无需搬同一DRAM里的KV，不等于无需handoff/visibility。PNM LSU只对其路径做参数只读检查，不证明任意系统隔离。
- 因共用同一参数分片，GPU-level Prefill与Decode必须采用相同TP/EP mapping，不能继续任意独立选pool布局；PNM-level attention用sequence partition与FlashDecoding统计reduction，避免TP乘上HBM数后GQA的KV heads不够分。增加DMA/reduction、PNM buffer、MMU/LSU、控制同步与额外热功率，不是软件开关。

### 对照、费用与关键反例

主结论来自cycle-level GPU/PNM simulator加DRAMSim3，不是实硅或production serving。全部基线8GPU、每GPU八个HBM4 stack、每stack48GB/2TB/s，GPU 2.5PFLOPS FP16；DuoPD另有每stack1GHz/32TFLOPS FP16 PNM与1MB buffer。因此是同GPU数/HBM基底而**不是同总计算面积/功率预算**。PD基线4:4或6:2、NVLink5 900GB/s传KV；chunked Prefill dense1K/MoE4K。模型GPT3-175B、Llama2-70B、Qwen3-235B-A22B；主长输入8–32K、输出32–512、图中batch8/16/32，动态试验Poisson arrivals/高斯长度。没有重训质量比较，也没有输出序列/数值等价或真实请求trace验收；software版本/完整serving runtime主文未披露，不能补为vLLM实测。

§6.2的主PD倍率是这些配置的作者模拟吞吐；batch32/长输出收益会下降，因为PNM按batch16设计。§6.3用低QPS TTFT的3倍作为显著排队proxy，不是外部规定TTFT/TPOT SLO，也不是已测生产goodput。SM分割比较仅9:1/7:3/5:5的模拟份额，不能代表所有动态软件策略最优值。

不能采用“总胜所有PNM”。§6.4的MoE decode-heavy情形，带内部带宽扩张的Duplex对DuoPD仍有约1.09×性能优势；作者认为不抵其面积/功耗，不等于该反例消失。只增加带宽也可能因compute不足在大batch/GQA下退化。PIM对照另假50%有效容量、Duplex容量损失未量化而按无损容量，不能把差额全归某一数据流。

面积6.51mm²/stack与功率6.45W/stack来自28nm综合再缩放到7nm；可用logic-die面积据die照片估计，不是实际floorplan/timing/良率验证。HotSpot的76°C用45°C ambient、指定vapor-chamber/0.0146K/W、16层DRAM与每die2W模型，不证明任意HBM封装散热。系统能耗用GPU1400W/HBM41.6W/stack/NVLink8pJ/b及HBM能量少7%的假设；32-token输出总节能仅2.1%、512token约37.9%，不能把PNM局部能耗降幅推广整服务。真实面积、MC迁移、DMA/reduction、memory map、功率/热与端到端质量/SLO都要重新验收。

### Books实际比较与最小差额建议（未写）

唯一owner **`INFER-PD-DISAGGREGATION`/Ch55**。已实际读Ch55开篇、阶段数据流/DUET完整段、精度/双参数和共享Prefiller/Decoder交接、E/P共驻、SM份额完整段与前后完整段（当前1–82），以及KV transfer/ownership起始、511–542/560–572交接；相邻Ch54的HBM budget开篇/697–711/800–829、Ch56开篇与1616小结亦已读。Ch54拥有容量预算，Ch56拥有SLO调度，不另造PNM owner。

现有DUET解释阶段专用compute但仍是两池handoff；现有SM份额段（当前75–77，`SF-2025-ARXIV-2507-06608`）已说SM不隔离共享HBM，却未解释“为发memory requests占用大量SM”与“共享原DRAM、另置完整Decode compute/MC仲裁”的替代分支。建议只在该完整SM段/marker后、下一段“多模态切分还须先声明搬运的对象”前插最小一段：以SM带宽瓶颈接共享DRAM分工，再保共同mapping、mutable-state单owner与visibility、带宽争用、模拟/额外硬件/功热代价。不要重复DUET或Ch54容量式，不把sharedDRAM写成PD全部取消。

无PNM硬件、需要独立布局/精度、batch或memory/thermal条件失配、handoff可见性不能证明或净SLO收益不合时，原SM划分、chunked共驻和同构两池继续合理。这里只给Source/owner差额建议，未给逐字PRE、Books写入或独立通过。

## B9 — 2610.26083v1：MX-like Tensor Core 联合格式—硅成本

**2+1+2=5；建议最小整合，具体长期差额深入。** 新增不是UE5M3本身（本书已有），而是scale格式与**activation/weight位宽不相同**时的中间SoP宽度/乘法器/累加成本耦合，以及相同scale在A6W6与FP4质量收益不同的条件。“非对称”在本文指W/A格式不相同，不是affine integer zero-point。

**必要原证：** [MX-Like Tensor Core for LLM Inference with NPU Integration via Hardware-Software Co-Design Exploration，exact v1](https://arxiv.org/html/2610.26083v1) §2–3.3（Eq1–2/Table2）、§4.1–4.4/Fig4–6、Conclusion；原件见B8，原HTML行482–1032。实际读问题、表示/量化程序、per-point datapath、自动生成/共同reference、完整设置与关键质量/硬件反侧，不核实现或跑RTL。

### 实际机制与公平比较单位

8-bit unsigned scale把bits分给exponent/mantissa（另纳UE4M3为NVFP4-like基线），element可取FP4 E2M1、FP6 E2M3/E3M2、FP8 E4M3/E5M2及MXINT8；所有组size16。先`max|x|/Qmax`并向上舍到scale，再量化element；block scale也会overflow/underflow。A/W共享scale**类型**，不等共享同一数值scale。

每设计点elaboration生成专用MAC而不是同一个runtime万能FP4/FP8 unit。四乘积先按预定anchor对齐/reduce；fractional scale不能只移位，需乘法器，再bidirectional shift/CPA/LZD/nearest-even回写accumulator。operand exponent从最大normal与最小subnormal两端拉宽SoP，scale multiplier继承此宽度，故fractional scale开销不能与operand pair脱钩。UE8M0可省此乘法器。统一参数同时导出layout/CSR/dataflow、数值reference与RTL，并co-sim/synthesis，是作者的HW-SW一致性流程，不是我们核过代码/二进制。

主评四个1–3B模型Qwen2.5-3B/Qwen3-1.7B/Llama3.2-1B/Gemma3-1B，WikiText2全test、C4随机256×2048；预筛仅前两model/WT2随机30×2048。质量是相对各自base的PPL degradation，未建立任务准确率/长context/闭环Agent质量。seed/独立重复/CI未充分披露。

硬件是TSMC28nm、400MHz、0.8V/TT的Synopsys Design Compiler；PrimeTime PX用2048MAC gate-level switching估功率。SNAX内4×16 PE、requant与on-chip data-movement/storage，workload是Qwen2.5-3B一个代表层的32×1024真实W/A tile；每设计点相同204.8GOPS。这里“system”是该NPU tensor-core配置，不是整LLM设备、DRAM/host/完整prefill-decode服务。无真实silicon、完整模型latency、batch/concurrency或SLO证据；固定MAC throughput的面积/功率比较不能写成serving speedup。

### 支持结论与必须保留的反侧

- A6W6在所测scale间mean相对PPL变化仅约1.0–1.4%，fractional scale可额外增加最高约17%面积/22%功率；不能从“scale更精细”直接采用到较高precision。
- A4W4的UE8M0约45%相对PPL退化，fractional scale明显缓和但仍非无损。A6W4提高activation而不改W可把UE5M3退化从18.4%降9.9%；提高到A8W4仅降6.1%，窄exponent的UE4M4/UE4M3反而可因Qwen3晚层outliers恶化到16.0%/19.2%。更多activation bits不自动让整format更稳。
- UE5M3相对**无FP32 per-tensor scale的NVFP4-like UE4M3**改善是“相对PPL退化少25.3%”，不是绝对PPL少25.3%，更不是完整真实NVIDIA NVFP4 recipe通败。+0.06%面积/+0.49%功率也是该专用设计点相对基线，不是所有pair均近零开销；不同operand pair使fractional multiplier增量跨约3.6倍。
- 作者用20% mean-PPL退化、60mW/0.7mm²圈可行域，并试15–25%/56–64mW附近阈值；不能把20%当通用质量门。真实checkpoint、shape、校准数据、PTS有无、量化顺序、accumulator与hardware消费者变化都需重验。

### Books实际比较与最小差额建议（未写）

唯一owner **`INFER-TENSORRT-LLM`/Ch49**。实际读当前1066–1157完整低位表示/axis/group/scale/HiFloat/UE5M3/校准相邻链、开篇及2507–2538/2599–2606交接；相邻Ch48的942–970与Ch50开篇/330–377，确认本项不属于speculative algorithm或engine scheduling。

当前1093–1097已明确scale精度/范围非单调、角色差异和UE5M3/动态prescale两分支，不重复写UE5M3“新发现”。未覆盖的是**operand exponent/SoP宽度决定fractional-scale multiplier真实成本**，以及A6W6下多付硅成本却几乎无PPL益处、FP4/A6W4下重新出现Pareto收益。建议在1097完整UE5M3段后/1099视频sub-formatbook段前一最小自然段，顺着scale-format不是免费metadata，说明联合选择W/A/scale/accumulation及同shape同throughput硬件成本。保无PTS基线、1–3B/PPL/RTL边界，不抄整榜单或将其改成现成GPU支持。

目标kernel/scale数值语义不支持、activation outliers越界或完整质量/能耗不合时，保UE8M0、更高W/A位宽、标准NVFP4/PTQ或原浮点路径。此处仅Source/owner建议，未授PRE/POST或独立通过。

## B10 — 2610.25066v1：Readiness-Aware Scheduling，必要反证后中心争议

**2+1+2=5；深入受影响中心主张，建议“争议/暂缓”，不改EX、不写Books。** allocated/placed不等ready确有项目贡献潜力；但“仅用admission时9字段即可在线RAS，并获得所报收益”目前受官方字段定义和反事实replay不变性问题阻断，不能把摘要承诺直接变成长期开箱规则。

**必要原证：** [Ineffective Occupancy in Heterogeneous GPU Clusters: Prediction, Contribution Analysis, and Readiness-Aware Scheduling，exact v1](https://arxiv.org/html/2610.25066v1) §3.1–3.3/T3–5、§4.1–4.2/T6、§5.1–5.4/Alg1–2/T11–13、§6.2，及Appendix A的字段定义。原件见B8；已读相关完整方法/设置/对照/限制，不遍历无关附录。为决定feature availability，定点恢复[Alibaba官方schema](https://github.com/alibaba/clusterdata/blob/3858992ca41bf92082e6d6522ddf0bebd14e838b/cluster-trace-gpu-v2026/docs/schema.md)；原件[ras-official-schema.raw.html](./ras-official-schema.raw.html)283006B，embedded refInfo currentOid=`3858992ca41bf92082e6d6522ddf0bebd14e838b`，正文execution-summary字段行811–813。未下载40M数据、跑重放或审核完整代码。

### 论文实际做了什么

`ready_status`为是否曾ready；论文把足GPU placement后从未ready称ineffective occupancy，且刚ready就退出也算effective，故ready只是启动状态proxy，不证明训练进度/useful GPU cycles/SLO。40,129,894有label记录中52.70% neverready是作者统计的**record占比**，不是52.70% GPU-time被浪费。其W(P)按一轮placed set的requested GPU数除cluster总GPU，是静态反事实装箱读数，不是完整时间积分占用。

5% row样本2,006,496做machine-grouped五折，训练fold另10% validation早停；LightGBM AUC0.8187与XGB0.8189相当，bootstrap对heldout records而非独立cluster/time。去掉schedule_status/ready_delay避免两个明显后验字段，不等其余九个已经证明前验。模型性能/SHAP contribution不是准备失败原因的因果分解，低单特征AUC不证明无泄漏。

RAS只改predicted-ready descending的admission order，placement固定best-fit；三种supply（两个synthetic、一real snapshot）、record/GPU两权重、五load、每cell三seed，90配置810policy runs。作者相同job batch配对，FCFS/RAS的W为43.64/27.15%，allocation约98.52/98.53%，大请求coverage46.11/63.18%；这支持其指定静态replay中的差额，不是线上改善。T13 `(0.5,1)` GPU bin的ready rate30.10→26.70，fairness总指标89.90→87.26，故不采用“任何群体/公平都无损”。容量充足时顺序收益趋近零，高负荷才需取舍。算法复杂度的integer GPU buckets与fractional requests需容量刻度；作者README说明1GPU=100单位，但本次未核该实现，不从伪码直接保证所有fractional请求可执行。

### 决定性反证与不能消除的混杂

1. **duration字段身份不一致。** 论文Definition1、T3和Appendix A反复把`duration_hours`标成declared duration，纳入九个admission-observable features。官方同名v2026 execution-summary schema却明确它是由observed execution samples导出的**实际execution duration**，不是用户申报量。按当前原始schema，不能在初次准入前知道该值；论文既未展示改用独立申报字段，也未证明这一重命名有来源。机器分组、去掉ready-delay或单特征AUC低都不能修复时间穿越。此冲突保留为中心争议，不断言已复现其全部泄漏效应。
2. **concurrency/decision-time快照未闭合。** `server_req_count`不在官方execution-summary字段表，论文称同机concurrent requests而又承认summary无time列、只有原placed machine而无admission cluster state。其生成窗口/是否跨未来记录/在新admission order下如何重算未由已读原证说明。`schedule_delay_sec`亦是已观测调度等待，若用于新初次admission须说明对应时刻与重放状态。没有时间戳不能仅把row order当真实FCFS chronology。
3. **label随着order/placement应变却被固定。** Assumption1和§6.2明示重放把ready label当job属性，改变admission和best-fit placement却不改变label；真实image-cache、startup contention/network会被顺序与目的machine改变。因而没有识别新的策略会使多少job ready，更未证明瞬时W差额等于长期capacity recovery/queueing收益。现有代码可算出相同数字也不会单独解决此因果反事实。
4. **不把代码访问失败当中心论据。** 定点作者audit原件一次web cache miss、一次GitHub curl30s超时；README可读，知道有audit脚本及容量刻度。已取得的paper/schema足以形成具体争议，不追加访问、不抓全repo、不把可选artifact缺失改为贡献EX或宣称Source已独立通过。官方raw README一次连接reset后，已通过GitHub schema正文恢复必要字段，不以第一次失败当全部路径用尽。

上述官方schema只支持字段定义及缺列，不能据它断言作者私有pipeline从未有别的数据；若作者确有pre-admission申报量，应提供身份/生成时刻/对应数据切片来解除冲突。当前明确隔离AUC、replay收益和“9特征在线可部署”作为正面采用依据。

### Books实际比较、当前处置及重开条件

唯一owner应为 **`PLATFORM-GPU-SCHEDULER`/Ch63**，不是Ch56 token scheduler。实际读Ch63开篇/16–118完整capacity链及Filter/Score/Bind/相邻分支、142–156 gang/queue/fairness、320–361稳定性与交接；相邻Ch62开篇/230–257和Ch64开篇/18–50/104–134已读。现有Ch63 32–46明确`C_policy_admitted ≥ C_useful`，42行已要求真进度/SLO而非仅分配，Ch64也有partial gang占卡无进展，因此**一般“已分配不等有用”已覆盖**，不能为采用有争议predictor重复造新段。

真正可能的差额是把admission→ready与ready→useful分别测量，并用真正决策前信息排序、在策略改变的状态下回验。当前证据未足以支持该新执行规则，故不授整合，也不把“已有覆盖”标签当中心结论已验。保留论文正面/反面证据，5分中心争议隔离：不写Books，不用其数字支撑生产容量/预测性能或公平保证。

精确重开条件：提供匹配dataset/version的pre-admission字段来源，澄清duration/server-count/scheduling-delay生成时间；用无未来信息且会随新placement/order更新的feature/ready模型或在线/等效受控实验重测。必要替代材料可以是可审的字段生成实现+schema映射及剔除后验字段的heldout/closed-loop结果，不强制复现整套40M trace、完整旧版或所有硬件。只能恢复该三个依赖，不能为闭合主张泛扫全站。计入预测/校准/排序/启动等待和公平/priority/starvation代价；实际数据不可前验取得或负载漂移时，保FIFO/硬quota/gang与可解释的ready telemetry，不因更高AUC剥夺合法job资源。

第三具名必要批次到此结束。只新增三精确论文HTML、必要官方schema原件与本文件B8–10；未改变CALIBRATION、Books/README/LS/index或此前B1–7，不stage/commit/push，不接其他材料/日期。两项最小差额与一项中心争议待root/唯一reader后续处理，未授PRE/POST/DAY/FINAL。
