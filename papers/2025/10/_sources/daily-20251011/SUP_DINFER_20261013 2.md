# dInfer 首版事件：限定Source与Ch24两段PRE

最新实际结果：root独核§7已实际完整顺读新增两段/mutable cache至Block Cache及Commitment邻接/本人note和diff，非writer POST通过并释放锁；作者仅行政同步自身note，正文未改。dInfer实际整合1可归日报，本日DAY/其余Source仍普通。下文待POST/未写均原准备阶段记录，当前以本段为准，不重Source或Books正文。

当前实际层：root独核§5必要Source/反侧、§6两段PRE通过，授Ch24指定两段及自身末注窄锁。作者实际写前读当前1482–1502/完整末尾及unstaged diff，既有2026差额12新增0删保留；只插下面两段（credit已窄修“当前提交判断”）与自身末注，现待root非writer实际POST/锁释放。下文“未批准/未写”仅原提案阶段，不是当前停点；本篇不预签POST或DAY。

作者Kierkegaard，本日只补2025-10-10自然日。root本日[独核](SUP_INDEPENDENT_20261013.md)§4已实际通过原作者Oct10首版framework release/精确v1完整题摘/2+2+2=6窄P。公开日是[官方News](https://github.com/inclusionAI/dInfer)的实现发布事件，不是arXiv announcement/全网论文first；v1 Submitted Oct9只提交角色。后版SGLang/LLaDA2/batch32不倒填。

## 必要证据与采用边界

原件：[精确v1 HTML](https://arxiv.org/html/2510.08666v1)、[本日保存](SUP_DINFER_v1_20261013.raw)，curl200/exit0/size_download184919，`--compressed`保存正文不与传输计数作同长度保证。作者实际读取S2/Algo1、S3、S4.1–4.2/Table1–2及AppA.1/B.1/B.2/D/Table3–6必要域；root已实际读取S2/Algo1、S3–4/T1–2、AppA–D/T3–6并提供独立反侧，未用headline代证。

1. 迭代manager、decoder与cache资格分开。Algo1中ShouldUpdate/Update、forward和decode-commit不是同一步；vicinity在mask及邻近位置重算KV，block完成再全refresh。双向依赖下已填token的representation仍受新条件影响，中间缓存仍近似，block末刷新不倒证此前采样exact。
2. Credit AppB.2 Eq1对各位置/类别保留衰减credit，当轮argmax另加当前概率的gamma次方；Eq2将`alpha log(1+C)`加到logits，再softmax得到新分布。阈值/top-k等外层规则可不换，但p→tilde-p已经改变概率输入，非原模型target distribution保持。beta抑制旧信号不保证阻止持续同错，current-block限制也不签正确性。
3. IterSmooth AppA.1只在仍masked位置使用`p_t W_emb`，将全词表期望embedding按有界alpha加到mask embedding，下一forward消费上一轮未提交的分布信号。原设置输入embedding与输出projection不weight-tied；使用原矩阵/不新增训练参数不等于零projection、buffer和校准费用。只改单步embedding接口不证明联合分布exact，重复错误也能被携带。
4. Hierarchical AppB.1分割mask spans、confidence允许时在每region推进；理想log级路径不是无条件复杂度或真实请求latency。该分支与credit可分别选，不把所有组件默认叠加最优。

## 对照、收益与反侧

S4.1六任务CRUX-O/LCBv6/MBPP/HumanEval/GSM8K/IFEval；8H800、PyTorch2.9dev20250831、vLLM0.10.1、batch1、生成1024/block64。TPF/TPS分子均first-EOS前tokens，不是完整服务并发/SLO或跨tokenizer等工作量；precision/完整端到端成本与独立复现Not Disclosed。Fast-dLLM无cache阈值0.9与dInfer credit+smoothing、有cacheDual与vicinity+smoothing+threshold分别比较，算法/缓存同时变化，不归因单一模块。

Table1headline10x是dInfer with-cache680.71对Fast without-cache63.61，跨cache组合；同cache比较680.71对110.98，也不证明每项质量/同分布。Table2 TD另训、hierarchical配置，平均质量52.72低于非TD with-cache53.96，IFEval/MBPP/LCB等退步不能隐去；多步teacher/蒸馏预付不消失。Table3明确无cache=credit+smoothing、有cache=threshold+smoothing+vicinity、TD有cache=hierarchical+smoothing+vicinity三套，不声称三解码器同时最优。Table5 credit51.56低于threshold53.96、Table6 credit48.89低于hierarchy52.72；保配置依赖和局部退步，不采同质量/无损/通用生产倍速。没有安装、跑代码或复现实验，当前repo与Oct10artifact同字节未核且非必要采用门。

## 唯一owner与具体差额

`MULTIMODAL-GENERATIVE-PARADIGMS` / [Ch24](../../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)。作者已读当前masked起段及跨轮/commit讨论、Cache可变状态与1472–1518完整邻接；root实际读masked开头/cache附近及1510–1555。现有正文已覆盖mutable response、身份/距离门与full refresh、controller commitment；不以没有框架名当gap。具体未承载的是：未提交的上一轮**概率分布**如何分别成为decoder logit prior或masked input embedding carrier，并与仍近似的KV刷新分责。runtime compile/CUDAGraph/TP+EP仅本次Source背景，不平行追加框架章/写通用runtime原理。

以下是两段自然衔接PRE，尚未批准/写入。请求仅在Ch24“进一步的近似分支只复用 token identity…”及其2608.08086 source marker之后、“Block Cache 可以…”之前插两段；不改前后两段、不动其他Review notes。还需root实际PRE/具体范围锁；无锁不得写。

### 拟正文第一段

跨轮复用还可以保存尚未提交的预测分布，而不只保存 K/V。保守 confidence 门槛只看本轮预测，接口简单，却会反复丢弃未达门槛位置的信号。一条受限分支为当前 block 内的每个位置和候选 token 累积衰减 credit，仅给本轮 argmax 加入当前概率的幂，再把 `alpha log(1 + credit)` 加到当前提交判断的 logits；另一条分支只对仍 masked 的位置，将上一轮概率分布乘输入 embedding 矩阵，按有界权重加到 mask embedding 后再次 forward。前者改变 decoder 的概率输入，后者改变 predictor 的输入载体；即使阈值或 top-k 规则没有换，也不再保证原 target distribution。历史一致性不是正确性，衰减也不能排除持续同错；未提交的预测只能作为可撤销的辅助状态，不能自行取得事实或 commit 权限。

### 拟正文第二段

这些概率与 embedding 状态还不能替代 cache 刷新：mask 及邻近位置重算、block 完成再全刷新，只是以局部计算换中间近似，已填 token 不等于其 K/V 永久不变。[首版必要对照](https://arxiv.org/html/2510.08666v1)针对无 cache、带 cache 与另训蒸馏模型选择了不同解码组合；credit 在带 cache 配置也有质量退步，headline 倍率又跨了缓存条件，不能把组件相加或少 forward 当成同质量无损。输入/输出矩阵不共享时的词表投影、credit buffer、阈值校准、刷新与蒸馏预付均计入预算。联合质量、原概率接口或净成本不满足要求时，关闭历史辅助、恢复原 mask/decoder 与完整重算，必要时采用更保守的逐位置提交。<!-- source-family:SF-2025-DINFER-FIRST-RELEASE -->

### 拟本人Review note（未预签）

`SF-2025-DINFER-FIRST-RELEASE` — Daily2025-10-11补Oct10自然日；官方首版release日名与2510.08666v1必要S2/Algo1、S3–4/T1–2、AppA.1/B.1–2/D/T3–6，2+2+2=6。仅probability→credit logit prior / masked expected-input carrier / approximate refresh分责；保p→tilde-p、同错累积、non-weight-tied投影费用、三套配置/TD另训及质量退步，不授原分布exact/同质量无损/通用倍率。未核首版全部代码或复现；PRE/实际POST仍待独立发生，正文当前未写。

## 当前普通余项

本篇必要Source已整理供root独核，Books两段PRE/锁/实际POST未发生。其余十二源、arXiv有界新差额/日门/current信号与六部分DAY仍普通；本篇准备好不等全包，计数由root维护54/132，本日未验收。
