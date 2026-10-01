# Apr24 Absorber / Gist 有限非作者采用核

复核者apr02，非Apr24报告/提案作者。已实际重读当前AGENTS、三合同、统一Prompt与ROADMAP；只核两项必要official v1与当前owner及邻接，不写Books，不核整日来源/日期，不复现实验。

## 20915 Absorber：5分真实gap深入提案通过

实际读[official v1](https://arxiv.org/html/2604.20915v1) §3.1–3.3/Eq2–6/Alg1–2，§4.1–4.2/Table1、§4.6.2–4.6.3/Tables5–6。Ch22当前KV-binding段只解释历史KV在线回归及history-dependent attention等价，没有“去X学生在有限Y上对齐full-context teacher”的目标分支，支持插在该段后。隐藏状态对齐是有限teacher监督，不是未知future因果保持证明；§3.2一处teacher符号与Alg1不一致，正文应依Alg1清楚区分冻结teacher/更新学生。

短窗standard更快，latency减prefill，Table6非所有m单调。采用包已保留LoRA/teacher前向与反传成本、reset/状态身份及显式KV回退，可窄写；不采用O(1)全成本、无限容量或输出KL只更新final head的无依据解释。Llama2-7B/RTX4080SUPER及n/m/r范围只能作为受限证据，precision/并发/SLO未披露。

## 20920 Gist：6分真实gap深入提案通过

实际读[official v1](https://arxiv.org/html/2604.20920v1) §3.1–3.4/Eq5–9、§4.1–4.2/Table3及选择变体说明。Ch45当前residual/synthetic-state、learned eviction和recoverable tiering的邻接论证均已读：并未承载“训练出的gist既压缩又作query路由，选中后读取gist+保留raw KV”的分支。可插learned policy后/分层recall前，owner仍Ch45，不把gist当事实oracle。

GQA各query-head选择再union，第一层不选择，required CPT/optional selective FT和位置相关mask须共同绑定artifact。激活读取预算不等原KV总驻留，硬Top-K本身不因声明end-to-end就可微；不补造tier-placement/kernel。Full-FT均值仍更高，训练8H100不证明serving时延/并发SLO。采用包的损失/训练和回退边界成立，实际写后仍须独立验收。

结论：两项source→actual-owner窄采用通过；不是实际整合、日期Gate或日报完成。未遍历无关附录/版本史，无共享写入。

## root 实际写后核

root非两项正文作者。实际顺读Ch22:711～732及Ch45:668～690，核对上述已有效、未变的exact-v1采用条件：20915两段紧接KV-binding，明确冻结teacher/更新LoRA学生与有限Y目标，不把未知future、逐token恢复或全成本O(1)写成保证；短窗反收益、扣除Prefill的计时与状态生命周期仍在正文。20920两段连接learned selector与recoverable recall，保留CPT、gist+raw展开、GQA union、首层bypass、硬Top-K不自动可微、读取预算不等驻留容量，以及Full-FT更高与训练硬件非serving SLO。两段均是实际机制正文、不是Review notes或论文清单；前后交接自然，没有替换旧方案。两项write-after通过，不代表Apr24整日Gate通过。
