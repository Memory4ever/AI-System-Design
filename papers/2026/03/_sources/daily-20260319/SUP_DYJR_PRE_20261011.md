# DyJR 2603.16157：必要原证 / 参照测度边界 / 拟 PRE

作者resume_mar18；仅本19补03/18自然日，2+1+2=5给recent成功buffer作为正则消费者/动态admission而非直接reward policyupdate。中心JS测度桥与知识差额必要深入。HTML失败转同[exact-v1 PDF](https://arxiv.org/pdf/2603.16157v1)，必要§3/Eq5–10/Algorithm1、§4/Tables1–2、§5.1–5.4/B Tables3–4/C Table5及结论实际读；SUP_DYJR_16157v1.pdf原件，p4实际渲染视觉核Eq7–10。未核所有图曲线、references/实现或复现。current abs仅v1/14pages3figures，无已见具体撤回/纠错；日级夹证有限复用，Submitted非public。

## 机制及中心测度边界

Buffer只存r=1且age≤M的(x,y,token-oldlogp)，按query G中正确数量Cid从高到低接纳，满足fillrate即停；20step前fill20%、之后5%，FIFO缩小而非永保所有early样本。高Cid优先不保证每难度都覆盖，近期也不认证behavior/current一致。Replay均匀取batch，online仍原GRPO，旧轨迹提供f(tokenratio)正则而非额外reward优势目标；正则依然需要current replay前向/反向，不是无梯度/无更新。

Eq8视觉确f(u)=u logu−(u+1)log((u+1)/2)，可作为合法逐token非负锚，完整未过滤旧分布下期望才有相应f-divergence解释（尺度2JS）。实际QB为成功/Cid/年龄/有限admission选择后的buffer，所存生成时某component的旧token logp不是该选择后QB的概率，也不等历史policy混合密度。逐token、旧prefix、sequence长度平均另不同完整trajectory JS，不能把Eq9自动视为精确JS(pi,QB)或[0,ln2]有界估计。最小定点反例：single-token current=old=(.8,.2)，只第一token成功，buffer QB=(1,0)；stored old ratio=1、f=0，但JS(current,QB)>0。这里否定“实际buffer分布的无偏JS”桥，不否定旧logratio正则为可优化proposal存在。原文未提供选择概率归一/mixture denominator/丢失support项，不能由过去逐tokenlogp补全。

Main数学Qwen3-4B-base/14kReinforceAdaHard、G8/prompt512/response6144，AdamW2e-5/.9/.95/WD.1/clipgrad1、32A800/TP1SP1；SQL Llama3.1-8B-Instruct/BIRD/Spider及约1k长度不是同math人口。Table1 mean@256、Minerva mean@16，GRPO/DyJR三run均值/std；SQLpass1 greedy、pass16不同，不混pass和mean。alpha.05/M8平均34.1对GRPO29.8是受限收益，alpha.2或M增大反退；M16 AIME23.6/HMMT13.6高于M8，不授所有slice新越好。DPHRL BIRDpass1 62.8>DyJR62.7，保留反側。DPHalpha.2 vsDyJR.05/DPH6of8admission、Exreplayratio.5/retire全正确query与本batch机制不同，静态参照失败/JS单因果未完全隔离。

Topk归一entropy忽略tail，rank1高不等单一语义reasoning path或真实modecollapse；C Table5 early20%→5%与一直20%34.1/34.2接近但非统计无差异/早样本永保或多样性唯一因果。训练早段entry在M8后已退库，不能把最终效果宣称持续保存早探索本体。§5.4约1638sequences/9.8M tokens计state索引，另存oldlogp/prefix/metadata和peak activation须计，float16不是合法tokenid实现保证。Figure3按ms/token rollout/update而非完整训练至quality/并发Serving，旧policy不用再forward不等current正则免费；Table3 replaybsz正文512实际样本对其“newlyadded”脚注口径未统一。Precision/exactlibrary、总步/训练停止选择、SQL重复CI与完整I/O/concurrency/SLO未披露，不授全费同GRPO、无bias或最优buffer。

## actual sole TRAIN-GRPO

实际Ch33 1500–1560完整版本/condition身份→ratio proxy→phase-replay→FIFO成本/reuse与sampling纠正；Ch32/34首18行已读。1542–1548具体已有buffer/cost/age与sampling-action分责，但无成功recentbuffer只作token-ratio正则的消费者。因此不虚NC消除新接口或中心测度争议。拟1544后/原非均匀priority前一段，待root与非preparer裁受限接口能否独立采用，未授锁/未写，不把争议当证据读取不足。

### 受限逐字一段 PRE（待采用裁决）

旧轨迹也可以只提供正则参照，而不再携带一份直接强化成功答案的 reward 优势。一条[受限动态 replay 分支](https://arxiv.org/pdf/2603.16157v1)保留近期成功轨迹和生成时的逐 token log-prob，按年龄退出 buffer，并在训练早段扩大接纳、随后收缩；当前策略重新读这些 prefix，以 current/behavior token-ratio 形成局部正则，online 组仍按原 GRPO 更新。这里的参照是被成功、难度与年龄筛选的样本及其来源 policy，不是完整旧分布；单个行为 log-prob 不提供过滤后 buffer 或历史 mixture 的密度，因此不能由逐 token 锚自动授完整序列 JS、无偏 off-policy 或语义多样性保证。保存状态、current 前向/反向与超参数搜索均付费，较强正则和更大年龄窗口可能退步；需分别保存选择人口、loss reduction 与 policy 版本，联合验收独立质量、探索和达到目标的全部训练费用。支持失配、正则过强或费用不利时，缩短/停用 replay，保留 current-only、原参照约束与直接 replay 的受控对照，不由概率排名批准能力保真。<!-- source-family:SF-2026-ARXIV-2603-16157 -->

### 静态来源注（随裁决，不预支写入）

- `SF-2026-ARXIV-2603-16157` — [DyJR exact-v1 PDF](https://arxiv.org/pdf/2603.16157v1)必要§3/Eq5–10/§4/Tables1–2/§5.1–5.4/B Tables3–4/C Table5；只recent成功buffer及token-ratio正则消费者。成功/难度/年龄选择后测度、历史mixture/逐token非完整JS、topk非语义多样性及全训练费用/反侧近文；未核全图点/实现或复现，不授无偏或生产保证。

## 非准备者必要Source/PRE：root

root实际精确v1 PDF §3/Eq5–10/Algorithm1、§4/Table1–2、§5.1–5.4、B/Table3–4和C/Table5；actualCh33 1490–1570完整staleness→ratio→phase replay→FIFO成本/priority交接及Ch32/34前置。复核f(1)=0且success选择后的QB不同原behavior、全Q期望的2JS尺度不能替代过滤后逐token估计，T2 BIRD 62.7低于DPH62.8、Table1正则/年龄反退、Table5近值非统计等价，ms/token与全训练成本、oldlogp及current前后向费用分开。有限buffer/局部正则接口不依赖中心JS或语义多样性强命题，逐字PRE与静态注保留其隔离，必要Source/具体差额/PRE通过。未核图曲线像素、代码或复现。授作者Ch33一段＋本人静态注窄锁；未actualPOST不计整合。

root非writer实际POST：顺读Ch33 1534–1558完整FIFO成本/相关性→正则消费者→非均匀priority→Agent生命周期交接及本人静态末注3186/相邻注；新1546逐字回对通过PRE，局部正则非过滤后分布JS/语义多样性和current前后向费用近文，旧fresh-only/直接replay分支保留。正文/本人注各唯一，限定diff检查通过，实际POST通过；Ch33窄锁释放，可计本项受限整合，不授本日DAY。
