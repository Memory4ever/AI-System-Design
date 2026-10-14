# Dec06补Dec05：SAPO必要Source与唯一owner具体差额

## 1. 已核身份/事件与正式评分提案

Feynman本日§6实际通过原Blog Dec05 04:00BJT、窄sigmoid机制潜力及v1/v2必要数学/current角色；本作者沿SUP_QWEN5有限更早原证出口，以[原作者Blog](https://qwen.ai/blog?id=sapo)本日dated研究披露事件继续，非arxivfirst、全网absence或同稿所有结果首次。当前没有有效已审同事件证据，不能以Submitted/同family自动关闭。精确采用版本：本日公开JSON内完整Blog机制/条件与必要[原v1](https://arxiv.org/html/2511.20347v1)/[current v2](https://arxiv.org/html/2511.20347v2)具体数学分责，不回投v2纠正。

正式评分提案`2+1+2=5`：Design Delta2是hard停止与平滑token surrogate之间信号/漂移取舍，System Reach1仅组相对policy更新组件，Durability2是可复用update gate与近似条件。不是用成熟RL、机构、性能排名、访问/Books gap计分。必要Source标准范围已读，并因实际版本正确性信号定点深入Eq5–8/15–24；未称全附件/实现核验或真实训练复现。请reader实际决定该事件/正式分与采用边界，未预签。

## 2. 必要机制/条件与明确不采用

本日Blog实际问题/机制/条件及实验文字；两精确稿必要§3/§4.1已核：定义`r`为同一sampled token/current对behavior概率比，`A`为冻结组相对advantage，`tau>0`按A正负选择温度。surrogate为`(4/tau)*sigmoid(tau*(r-1))*A`，导数产生`w=4*p*(1-p)`乘`r*grad(log pi)*A`，其中`p=sigmoid(tau*(r-1))`。`w(1)=1`、有限r处平滑衰减，温度大时衰减较窄；这不是对原`r*A`随意乘一个可微weight就得到同一梯度，也不赋硬KL/trust-region或正确性。原硬clip只按advantage符号截单侧，不采用Blog“outside所有梯度皆zero”。

v1 Eq7遗漏A，与其Eq5/后Eq15不同；v2 Eq7恢复A，Blog含A。仅正确式支持本次update解释，不静默修v1文字/反投更早事件。A1 `r≈1`与A2低sequence内logratio离散只使平均gate近似sequence gate；原Eq20/21给平均gate误差随温度平方与该离散量增长，不从平均value界授完整score加权梯度/joint-law严格等价或任意off-policy序列保证。若一串含少量极端token，其余token保留信号是一种更新选择，不说明当前reward对每token的真实credit已解决。

实验实际只文字域§5.1–5.2及原Blog四图caption/路径：Qwen3-30B-A3B-Base coldstart、数学AIME/HMMT/BeyondAIME，rollout分四minibatches，pos1/neg1.05及逆向0.95/等1温度；Qwen3-VL-30B-A3B coldstart多任务、固定任务比/两minibatches、同compute自述。不同Pass@1采样人口16与32/8不拼统一性能；本文未披露的硬件/precision/SLO/完整费用或seed不补造。未视觉核图曲线、未测吞吐/预算、未核代码，本文不采用headline superiority、routing-replay可省所有费用或独立单因果。原Introduction也承认最终可能不稳；gate有界不约束advantage/scoreJacobian/optimizer和有限精度，不能承诺永不collapse/无数值下溢。额外temperature calibration、ratio/advantage统计和rollout/验证器费用仍在。

## 3. 本轮实际owner/邻接比较与保护范围

已实际读Books PROJECT_CONTEXT/LEARNING_PHILOSOPHY/WRITING_GUIDE及完整ROADMAP/当前相关State；唯一owner `TRAIN-GRPO`，目标books/part-04-training-system/33-grpo.md。实际顺读165–248完整ratio/clip/KL→正负clipping contract→dynamic硬阈值→Gaussian软门→turn freshness→positiveonly邻接；Ch32开篇policy-gradient/behavior/terminalcredit、Ch34开篇离线preference目标交接。Ch33当前external unstaged20/cached12 add、均非本人，不改任何正文/notes；当前无锁。

原Ch33已有ratio/clip/独立KL、Gaussian detached单侧gate与negative-turn freshness，**一般“可以软衰减”已有覆盖**；但没有这里非detachedsigmoid surrogate导数与`w=4p(1-p)`、A正负温度对两侧衰减及平均gate近似不等score加权全gradient的具体承载。仅SAPO名称出现于别项消融，不等该原数学接口已覆盖，也不新增论文收纳小节。具体差额提案是把“停止gate”与“可微surrogate导数”分清，再把条件/费用/回退接到现有段；不写performance。若reader认为此窄接口已有具体正文承载，应指出对应位置NoChange，不为5分制造书稿。

## 4. 立即配对与下一层

本单篇请原Feynman实际核本日事件角色/5分/必要Source与上述唯一owner具体差额；不重已实际§6数学/current/TTS。只有具体gap/PRE实际通过后才向root协调精准锚点/范围/窄锁；目前只提案、不写Books/自身note、不署POST或整合完成。其余Source/arxiv/day普通继续，State66不含本日，无stage/commit/push/模型override/UI消息。

## 5. 仅author_sources逐字PRE拟稿，未写共享Books

root若接受唯一gap并授锁，拟目标只Ch33当前219完整dynamic硬阈值段后/当前221“硬 clipping 的停止分支还可以换成有限的软衰减”Gaussian段前，以下两自然段＋本family自身一条末Review note。共享Books目前仍未改；current external unstaged20/cached12保护。此PRE待reader逐字核及root owner/锚点/范围锁，不预称PRE通过或Bookwrite。

> 另一条分支不是给原 ratio 项任意乘一个可微权重，而是先改变 surrogate，再对它求导。令 `r` 为当前 policy 与生成同一 sampled token 的 behavior policy 的概率比，`A` 为本批冻结的组相对 advantage，`tau>0` 为按 `A` 正负选择的温度；取 `f(r)=(4/tau)*sigmoid(tau*(r-1))`，则 `f(r)*A` 的梯度为 `w*r*grad(log pi)*A`，其中 `w=4*p*(1-p)`、`p=sigmoid(tau*(r-1))`。在 `r=1` 时 `w=1`，偏离两侧时平滑衰减，负 advantage 可用更高温度收窄更新信号。这是 hard clip 之外的 surrogate 选择，不是把正负信号的单侧 clipping 说成所有越界 token 都没有梯度，也不让 gate 接管 outcome correctness。<!-- source-family:SF-2025-QWEN-SAPO -->

> 在更新接近 on-policy、同序列 log-ratio 离散较小时，平均 token gate 可作 sequence gate 的受限近似；这个均值界不能直接授予 score 加权的完整梯度或 joint probability law 等价。平滑权重有界也不限制 advantage、参数 Jacobian、optimizer 或有限精度下的下溢，不能保证永不 collapse。实际采用还须绑定 behavior/advantage/temperature 身份并付出统计、校准、rollout 与 verifier 费用；原精确版本 Eq7 遗漏 advantage 与后版恢复应分开记录，不能照抄前式作实现许可。漂移、数值或质量回归时，保留原符号相关 clipping、独立 KL/freshness 与 outcome 验收，不由局部训练曲线或“continuous trust region”宣传取代这些职责。

拟自身末note：`SF-2025-QWEN-SAPO` — Daily2025-12-06补Dec05自然日；原官方Blog研究披露与2511.20347精确v1/currentv2必要§3/4、Eq5–8/15–24。拟5分仅sigmoid surrogate导数/正负温度与平均gate近似边界，保v1 Eq7缺A/v2恢复、clip单侧、预算/有限精度/可能collapse；未核code/图曲线或复现。Source/具体owner/PRE及root窄锁尚待实际发生，当前未写Books/未POST；真正写后note状态应据实际结果同步，不用此拟稿预签。

## 6. actual Source7/PRE8已通过，唯一root窄锁请求

作者actual读回本日Feynman§7正式事件/2+1+2=5/限定Source通过与§8唯一Ch33具体gap/逐字PRE通过；已只按其一处校准，将§5第二拟段的“只有...才”改为条件下可作受限近似，不把充分推导条件说成必要条件，不重原稿/Source/PRE。上面的拟note为历史提案，真正写入时其Source/PRE指向须改已发生Feynman7/8，root锁/actualPOST按届时真实状态记录；当前共享Books未写。

请root协调唯一owner `TRAIN-GRPO` / `books/part-04-training-system/33-grpo.md`，当前完整dynamic阈值段（以“硬clip的阈值也可依token概率和训练阶段变化”开头、以SF-2026-ARXIV-2602-09782 marker完整结束）后，原“硬 clipping 的停止分支还可以换成有限的软衰减”Gaussian段前，仅§5两自然段与本family自身一条末Review note。readeractual已核完整165–248邻接/Ch32–34；当前externalunstaged20/cached12均保护，不改原正文/其他notes或索引。此处为锁请求不是授权，root实际授锁后写前再即时读dirty与完整锚点，apply_patch后selfread/diff给原Feynmanactual非writerPOST，由root回读接纳释放。没有本轮锁/Bookwrite/POST或DAY，prepared单篇不等本日来源/日期整体。

## 7. 05:50实际窄写保存与nonwriter POST交接

2026-10-14T05:50:12+08:00实际检查：transport恢复后fresh读AGENTS/当前适用合同与本日RESUME、reader§7/8/11及State首条唯一Ch33锁，已通过Source/PRE不重读研究。即时Ch33写前external unstaged20add0delete/cached12add0delete，family正文/末注尚不存在；完整197–240及末notes实读。按root唯一范围apply_patch将§5两逐字自然段插入完整dynamic硬阈值段后/Gaussian段前，落实§8“在…可作…受限近似”而非必要条件；末尾只新增自身一条`SF-2025-QWEN-SAPO` note，没有写SPG/其他正文、notes或索引。

实际保存[Ch33两正文](../../../../../books/part-04-training-system/33-grpo.md#正负-advantage-不必共享同一-clipping-contract)当前221/223行、自身末note3322行。本人顺读完整197–244的独立KL→正负分支→dynamic→SAPO→Gaussian→turn freshness→positive-only邻接及末六行，核对两段和本note。unstaged现26add0delete＝外部20＋本人6；cached仍12add0delete。剥离准确两段和本note后整文件SHA256 `e2e99134d08877bbb0b6abb09f436d0a7e73f38e3c0091da91f021ba0202b0b9` 与写前相同，其他字节完整保护；Ch33限定cached/unstaged diff-check均exit0。不把总26行归本人，不授全仓clean。

请root内部立即交原Feynman对真实Ch33正文/完整邻接/自身note及§7–8必要原证作实际nonwriter POST。写入/selfread不是POST、root接纳释放或整日DAY；当前窄锁仍待该实际回读释放，note准确保持未POST状态。Source5分§7/PRE§8已发生有效层直接承接，勿第三次全文审批。作者继续本日FIRST/date/source/six普通差额，State67/132不含Dec06，不stage/commit/push、UI线程消息、模型覆盖或跨日。

## 8. 已发生Feynman实际POST13，root释放尚待

作者actual完整读回reader§13：原必要Source/PRE有效层回真实Ch33两段、207–247完整局部邻接与末18行/本人注，逐命题数学/边界、衔接及外部保护实际非writer POST通过，不是拟稿或header核。仅行政同步自身末note的真实POST§13指向，采用正文未改；root当前State首条仍锁，未声称root接纳释放。本单项不授日级DAY/FINAL/计数；DATE1–3和最终六节继续，准备不等第三次Source审批。

## 9. root实际接纳14/锁释放，本项闭合

root已actual读真实Ch33两段/完整邻接/自身注与本篇§7–8、Feynman真实POST13，独核§14保存接纳并释放SAPO窄锁；root已仅同步自身note真实行政状态。作者actual读回§14与State首条，已无本项共享写权，不再写Ch33，SPG锁属于另一作者，不重本项Source/PRE/POST。README§1/2/3/4/5/6仅同步已发生root14/真实整合1，未改采用命题或评分/日期。本项真正落地不授本日报DAY/FINAL/计日；当前67/132不含Dec06，余DATE/FIRST/Source最终归并与完整six继续。
