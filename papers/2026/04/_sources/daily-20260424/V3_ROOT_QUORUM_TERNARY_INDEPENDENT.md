# Apr24 quorum / ternary execution 两项有限独立核

root，非报告/提案作者。恢复后实际重读当前AGENTS/合同/写作方法及ROADMAP，有限核原始v1关键方法、直接反证和实际owner邻接；不验整日来源/日期，不复现实验。

## 21428：7分深入，Ch36窄采用通过

[exact-v1](https://arxiv.org/html/2604.21428v1) §3.2/Alg1～2、§3.3及§5.4～5.5实际核。syncer对fragment只等minimum K，独立learner继续计算；满足最低到场量后用通信/计算重叠的slack作为有界grace，争取更多到场贡献，而非等全员barrier。`tokens×(tokens/steps)`是作者权重，不是普通token平均，也不是无条件公正权重。参数fragment覆盖/reset与outer update不同于单一集中式optimizer step。

实际Ch36:1340～1364异步跨站、staleness与角色切换，Ch35恢复合同：已有canonical state/provenance但未解释minimum quorum与bounded grace如何把可用性和贡献采样分开。可在跨站聚合后以两段补此条件分支，保source revision/steps/tokens、恢复与optimizer状态，不重复Ch35 checkpoint完整清单。不将double-buffer slack写成永远正数，迟到权重、样本偏差及局部load balancing都须独立验收，slack不足或一致性优先时保全员同步/更小grace。

§3.3百万chip是故障模拟；§5.4 Table5 caption TPUv6e/v5p、正文v5e/v5p的歧义真实存在。K1无grace质量明显退步；有grace的MMMU12.2仍低同步19.3，因此不能写每slice无损或集中式语义等价。§5.5有限dense/MoE规模的比较不证明任意巨大集群稳定收敛。只采用聚合/状态分工，不采用百万卡实训、普遍100% goodput或生产SLO保证。写后另验。

## 20913：5分因实际缺口定点深入，Ch49窄采用通过

[exact-v1](https://arxiv.org/html/2604.20913v1) §3/Alg1、§5.1/§5.4～5.5实际核。ternary正负bit mask通过BMI2 pext及AVX-512 masked add/sub，解码同一packed weights后在widely-linear八子GEMV复用mask/activation并保register累加；末端scale仍乘法，不是全模型无乘法。Ch49:720～741已讲dequant/product-LUT，795～821有SIMD/LUT layout，但缺“低位宽执行也可走无LUT条件加减，多子算子共享解码”这一并列选择，可以放LUT后，不否定旧分支。

实际§5.1与Table6限Xeon8558P48核、Fairy2i-W2与Llama2-7B不同模型、2bit packed/FP32accum和至少128生成token。29.6倍比较1thread dense与48thread ternary，不作同线程因果收益；H200自写CUDA的130倍退步不证明任何GPU低位width皆无收益。§5.5同线程fused/unfused提供较窄共享解码/activation/屏障成本证据，但不能把分解百分比当普遍可加。正文保ISA/shape/寄存器压力、scale、质量及执行artifact约束，不采用全模型无乘法/近无损/通用CPU优越或生产SLO。Ch50仍拥有request engine协调，Ch49只拥有执行计划。写后另验。

两项通过的是source→actual-owner窄采用，不是实际整合或整日Gate；日期缺口与当前版本事实分别由日报作者处理。

## root 实际写后复核

实际顺读 Ch36 跨地域聚合→21428两段→GPU角色迁移，及 Ch49 product-LUT→20913两段→量化 probe。两项真实正文写入通过：quorum/slack/grace、到场偏置、非普通 token 权重、百万芯片模拟及 TPU/质量限制均保留；ternary 条件加减保留末端 scale 乘法、ISA/shape/寄存器限制与线程混杂，不否定所有 GPU。机制 owner 分别为训练聚合与执行计划，checkpoint/request 控制只作具体 handoff。相邻衔接通过，不是实验复现或日级 Gate。

## SPIRE 20849：source→当前owner窄采用通过

root实际读取官方v1 PDF §3.1–3.2、§4.1–4.3及Table1，并顺读Ch76 chunk/parser证据单元与late-interaction段。树/path-set选择身份与embedding global view、reader local view分离是具体缺口；延迟展开与路径合并可承接parser unit，但须绑定document revision、parser和path，不能当跨修订稳定或支持真值。

Hotpot原block与embedding helpful比例分别336/1514、479/2225，不能写所有分支改善；SPIRE 538/822测的是helpful citation比例，不是答案准确或support完备。两数据集各400题、1000-token预算，filter与judge模型及改encoder混杂限制已在作者notes，不外推生产SLO。两段有条件采用通过，Ch76与20日LogicLoc仅协调写序；实际写后、日期与日级Gate不预支。

实际写后：root顺读Ch76 parser evidence unit→新增选择身份/视图分離两段→late-interaction预算，真实body与Review锚点均在。revision/parser绑定、延迟展开的预算/维护成本、helpful非truth、Hotpot反例与固定chunk共存紧随机制，不存在只记“已吸收”而无正文的情况。非作者实际写后通过；未复现，未日级Gate，Ch76写锁释放。
