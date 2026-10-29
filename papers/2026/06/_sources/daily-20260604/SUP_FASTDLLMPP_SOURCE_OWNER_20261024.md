# Fast-dLLM++ 02955 必要Source / actualowner / 最小两段PRE

作者supp_20260604_author，R27题摘贡献/Jun03联合日证与2+2+2=6复用，不第三AB/date。HTMLfirst exact-v1 §2–6/Alg1、A1–4/B1–2/C1已实际读，必要支持/关键反侧足够停止。完整HTML剥标并保math annotation的TEXT95525字符真存SUP_CORE_2606.02955v1_TEXT_20261024.txt；fetch曾10s返回session非失败，实际等原session exit0才保存，无工具truncation marker。后续Dream全D及更多E/F、图像像素/代码未核，不称实现/复现通过。

## 必要原证与采用权限

§3/Alg1 confidence排序后L=max(0,sum c−(n−1))，U=1−min c，取最大prefix满足L−U>delta；未通过者强制单点以进展，不等证书通过。§4.1/A1的union-bound只要求同一E、相容的真实联合P边际，任意竞争tuple至少一坐标不同所以≤U，L>U足以唯一jointmode；不需独立但不是分布exactness、正确gold答案或跨step joint轨迹证明。不采用原文“最强所有边际证书”普遍最优宣传，本文仅核该充分条件。A2 equalconfidence且f=1−delta退回factor；A3在L>0有G=F+B、B=sum(cj−cmin)≥0，异质本身不保严格加速，需差额跨decisionboundary；A4只逐prefix接受域支配，未证明另一decode轨迹整体quality或TPS支配。

§4.2 TV/KL residualdependency条件只是扩展未被算法使用，也没有实测这些真joint距离，不能把它当实际安全门。§C/B：reportedconfidence与evaluation/verifier-reference correctness不同，假设每项真候选事件prob≥max(0,reported−eta)；不截零且robustL active才得到Ghat−(n+1)eta。原实验未提供逐请求eta估计或校准保证，reference事件也非无条件开放世界真值；本稿仅采用“校准误差随集合放大，需额外证据”，不采用该C结论认证实际模型真joint或全过程。理论里的模型概率需相容真边际这一假设不能由softmax本身证明。

§5 singleH10080GB、LLaDA8BInstruct greedyargmax无temperature，block32，length256/512/1024，Prefix/Dual/NoCache声明；主表pcache，global tau.9/f.75/delta.25由development sweep选，GSM5shot/1024用8shot，MATH4/HumanEval0/MBPP3；flexibleextract、mathverify、postprocessedpass1不同协议不混。Precision、batch/concurrency、inputlength全矩阵/seed复次CI/线上SLO与exactcacheversion NotDisclosed。只换selector不加持久权重/KV不等无排序/tempbuffer/端到端开销。T1主速比对threshold而非全部对factor；GSM256factor78.1%/96TPS→77.2/103.8，MATH256threshold33.1→32.5，MBPP256threshold27.4→25.4，负侧保持。T2 1024pcache factor38.2→38.7TPS仅小增，dcache39.8→40.8；不采用主文5–20%全settings或headline37%作普遍增益。T3 LLaDAV MathVerse Fast28.6→27.9、TPS23.3→23.8，MathVista vsfullsteps59.2→56.8，不能只摘相对Fast .2pp。T3与F3 accuracy尺度不齐（表56.8/图约.33），不合并同条件强归因或靠该图定默认margin。本文有限表格足以保qualityfrontier而非无损；不为未采用数额扩核全图。§6 miscalibration/strongcoupling/仅greedy，sampling/topk open。全forward/cache/排序/prefixscan/开发sweep、回归与失败生成费用保留。

## actualowner及最小差额

ROADMAP唯一owner MULTIMODAL-GENERATIVE-PARADIGMS Ch24。实际完整读开篇/factorization/commit主线，2177–2196 earlyconvergence完整两段、pairwisecompat完整段/binding与RPD两段/marker；23/25开篇边界已读，Ch48 standalone块/targetverifier职责定点核，训练/语义生成链不复制为speculative exactsampling。全Books exact02955/Fréchetprofile未见既有samefamily，现Earlyconvergence测跨步稳定，pairwise估依赖，RPD读层内/上游熵，均未承载marginal-only整profile bound/平坦归factor与校准marginpenalty差额；不是主题相同NC或重建泛owner。

建议只在Earlyconvergence原两完整段后、pairwise完整段前增加以下两段与本人trueH2注；保原10980下方familymarker/15805binding/RPD及他文。无本项Book授权/未实际写，待首次独立Source/actualowner/两段PRE。

完整上锚：

并行去噪最初常用当前位置的边际置信度决定是否提前提交；它便宜，却把“这一步很确定”误写成“后续步骤不会再改变”。约束变化是多个位置共同修正时，单点高置信仍可能被后续条件关系推翻。更严格的 runtime 可以追踪一个 token 在连续 denoising steps 中是否已经稳定，把 early-convergence signal 与边际 confidence 联合用于 provisional-to-committed transition。

这会减少不必要的更新，却增加跨步状态、滞回阈值与误提交风险；稳定检测仍不是联合分布正确性的证明。检测不可靠、输出有外部副作用或 exactness 优先时，应延后到 block verifier 或完整 denoising 结束再 commit。该分支补充本章的 mutable-state 路线，不宣称它普遍优于 confidence schedule。[受限证据：arXiv:2605.10980v1]

拟增两段：

不增加 pairwise 模型时，选择器也不必把整组位置压成最弱置信度：对按置信度排序的候选前缀，分别计算“所有候选同时成立”的保守下界与任一竞争组合的上界，只有下界超过上界和选定 margin 才扩大并行提交。固定同一 evidence，且这些置信度确为同一条件联合分布的边际时，这给出所选组合是联合 greedy mode 的充分条件；它不要求独立，却不等于序列采样分布保持、最终答案正确或跨步轨迹一致。强位置相对最弱位置的置信度差额可以增加可接受余量，平坦 profile 则退回原 factor 条件；没有集合过门时的单点进展回退也不是该证书通过。

[受限 profile 选择研究](https://arxiv.org/html/2606.02955v1#S3)只更换当前 forward 的选择规则，不能因此认证底层 cache 的有效性。模型报告概率若偏离所需真实边际，须另有可核验的单侧校准余量；在不截断且下界有效的条件下，统一误差余量对大小为 n 的集合可消耗 `(n+1)η` 的 margin，但原实验未提供这种逐请求保证。单 H100 的 greedy 对照仍有代码任务和多模态准确率反退，不能把少 NFE 或较高 tokens/s 写成无损。排序、prefix scan、阈值开发、完整 denoising/cache 与质量回归均计费；校准或联合边际前提不成立、净并行收益不足时，保留保守 factor、顺序/完整去噪或另经验证的 block verifier，不让 profile 分数取得真值或线上 SLO 权限。<!-- source-family:SF-2026-ARXIV-2606-02955 -->

完整下锚：

多个位置各自具有高边际置信度，也不保证它们组成的 joint configuration 一致。一个受限分支在 commit 前加入 pairwise compatibility，并以 mean-field / fixed-point 更新修正各位置的 marginal score；它减少“单点都合理、组合却冲突”的并行提交，但增加二阶计算，且 pairwise 近似仍看不到高阶依赖。短 block、依赖弱或额外校正成本超过并行收益时，保守顺序提交与 target block verification 仍更清楚。作者在特定 discrete diffusion reasoning/code 任务上的结果只支持该近似的局部质量—延迟取舍，不提供通用 joint correctness。

<!-- semantic-body-binding:SF-2026-ARXIV-2606-15805 -->

本人trueH2注拟：`SF-2026-ARXIV-2606-02955`：Daily2026-06-04补Jun03；exact-v1 §2–6/Alg1/A1–4/B1–2/C1必要，2+2+2=6因marginal-only profile/校准余量具体gap深入。只固定E下相容真边际的jointgreedymode充分条件，非gold正确/采样exact/跨step；保单点fallback未证、条件校准与eta未测、强依赖/质量反退、greedy单H100/不同baseline及全费。不采用最强证书/通用37%宣传或图表混尺度；未核像素/代码/复现。待PRE/新授/实际POST。

