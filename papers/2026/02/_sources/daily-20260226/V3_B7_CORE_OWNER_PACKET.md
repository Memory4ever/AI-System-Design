## 2602.20558v1

https://arxiv.org/html/2602.20558v1；精确HTML原paragraph机械摘段：

A critical design choice is which model provides the reward signal during Verbalizer training. We employ a capable closed-source LLM (rather than the target Reasoner being trained) as the oracle Reasoner for several reasons. First, more powerful models provide higher-quality reward signals with better discrimination between effective and ineffective verbalizations. Second, using a fixed oracle avoids the instability of co-training both components simultaneously. Third, the oracle’s superior reasoning capabilities help the Verbalizer learn verbalizations that capture genuine preference signals rather than exploiting weaknesses in a weaker Reasoner. Empirically, we find that training with a stronger oracle leads to verbalizations that generalize better to different Reasoner architectures.

We evaluate on an industrial-scale dataset from a major streaming platform containing user viewing interactions over a three-month period. Each interaction record includes timestamp, item ID, title name, engagement type, and viewing duration. We focus on the reranking task: given a user’s interaction history (up to 100 recent interactions) and 10 candidate items, predict which item the user actually engaged with next.

Table 2 presents ablation studies. The rewrite-based approach enables emergent behaviors that discrete actions cannot capture. Removing the length reward leads to degraded performance due to over-compression or verbose outputs. Training the Reasoner on verbalized interactions substantially outperforms training on raw interactions (+92.9% vs +42.8%), validating that the Verbalizer produces a more learnable data distribution. Using ranking-based rewards fails to improve over baseline, consistent with prior discussion on LLM-based evaluation.

While the two-stage pipeline introduces additional training cost, this overhead can be mitigated in practice. The Verbalizer can be distilled or cached for efficient deployment, and the two components can be trained at different cadences. The Verbalizer captures relatively stable patterns for transforming interaction logs into effective textual representations and thus requires infrequent updates, whereas the Reasoner must adapt more rapidly to evolving user preferences and content catalogs. This decoupled training schedule is a key advantage of our modular design.

## 2602.20580v1

https://arxiv.org/html/2602.20580v1；精确HTML原paragraph机械摘段：

Using the Pythia suite, we measure the degree of PI parroting and analyze the effect of model size, pretraining timesteps, and prefix length on memorization.

In Figure 1, we present the results of our manual audit of both wimbd and R&R detection suites.
We focus solely on precision, mirroring the annotation process of previous work, where the authors manually annotated detections (Subramani et al., 2023; Elazar et al., 2023). 22
              2
              
              
              
              
              
              
              
            Not only would annotating pretraining documents be infeasible without a large pool of annotators, but also using that pool would reveal PI publicly, drastically increasing privacy risks.
We run both detectors on the entire Pile dataset and take a random sample of 1750 detections.
To improve coverage, we leverage stratified sampling, where strata correspond to the 5 different subcategories of data sources (academic, dialogue, internet, prose, and misc) of the Pile, and annotate the selected data across all PI types.
Overall, we find that R&R has a total of 483 true positives, with 99% of those having a perfect span.
This is the gold set that we use to quantify memorization.

To measure PI parroting and memorization, we use the manually annotated and curated set of detections from our R&R detection suite, which contains 483 instances of PI.
We experiment with 6 models from the Pythia suite with 160m, 410m, 1b, 1.4b, 2.8b, and 6.9b parameters, respectively.
For each instance of PI, we find its associated prefix in the Pile and truncate this to a maximum of 80 tokens.
Using this potentially truncated prefix as a prompt, we generate from the LM using greedy decoding and evaluate whether it parrots the ground truth PI instance using ParrotScore in equation 1. 44
            4
            
            
            
            
            
            
            
          This is similar to measuring  p -memorization for  p=80 .

Table 2 presents the percent of total instances that are parroted verbatim by each model.
Verbatim parroting and model size are positively correlated, and email addresses and IP addresses contribute mostly to this trend.
Both PI types are increasingly parroted: nearly 20% of all detected email addresses and more than 14% of IP addresses are exactly parroted by the two largest models.
Phone numbers have a much lower verbatim parrot rate, which is not correlated with model size, indicating that phone numbers can be challenging for LMs to memorize.

Recall that we are measuring  p -memorization, which is highly dependent on the prefix length  p .
In all preceding experiments, we set this number to at most 80 tokens.
To measure how the prefix length affects ParrotScore , we experimented with reducing  p  to 40, 20 and 10 tokens.
This is the maximum size of the prefix that precedes the target PI in the original document.
The lower part of Figure 3 indicates that ParrotScore is positively correlated with the prefix length, but, even with a token prefix of 10 tokens, the 6.9b model can parrot, achieving an average ParrotScore of 0.34.
This indicates that models memorize PI rampantly and can be prompted with short prompts to parrot PI.

Carlini et al. (2021) explore how language models like GPT-2 tend to memorize specific training examples, including PI, and that this can correlate with data frequency and model size.
Other work investigate model forgetting, especially tailored to memorized examples throughout training Jang et al. (2023); Jagielski et al. (2023); Carlini et al. (2022).
Our work builds upon these: we quantify character-based PI parroting for the first time and analyze how model size, steps of pretraining, and prefix length affect it, further substantiating the claim that larger, better trained models tend to memorize and parrot more heavily. See Wei et al. (2025) for an overview of memorization in deep learning.

Annotating personal information is time-consuming. Since the data is private, out-sourcing the annotation process should not be done because it could expose PI. As a result, the sets we can annotate are small.
Previous work annotated only a few hundred examples (Subramani et al., 2023; Elazar et al., 2023), whereas we annotated 1750 total detections. We hope that larger studies can be more comprehensive in annotating without exposing privacy risks.
Most modern language models do not have open pretraining data, so figuring out what data a model has seen can be challenging.
As a result, we focused on using the Pythia model suite because it was one of the only models that had a variety of model sizes, checkpoints during pretraining, and open pretraining data.
OLMo also has different model sizes, checkpoints and open pretraining data (Groeneveld et al., 2024), but Dolma (Soldaini et al., 2024), its pretraining corpus, contains a PI filtering and anonymization step using the wimbd detectors.

Here, we look at the impact of pretraining steps and prefix length on memorization. In Figure 3, we find that the models parrot even when only halfway through training. The Pythia models are trained for 143,000 steps, and even from 70,000 steps as mentioned before, ParrotScoreremains constant. Additionally, prefix length is highly correlated with ParrotScore. However, even with as little as 10 tokens in the prefix, PI memorization is rampant, indicating severe risk.

Here, we measure how each constituent part of a type of PI is verbatim parroted by each model.
To do this, we first parse IP addresses (IPv4) into their four constituent groups separated by a period (e.g. 8.8.8.8 turns into [8,8,8,8]). Each of these 4 groups are measured separately. A candidate generation that produces “12.8.8 abcd” will turn into [12, 8, 8 abcd, “”] and comparing that to 8.8.8.8 will lead to verbatim parroting of only group 2. We parse email addresses into two groups: the username and domain separated by the symbol ‘@’ because email addresses are usually separated into these two groups. We parse phone numbers into two groups: area code and the rest of the digits following that. Since we are only considering US/Canada phone numbers that always start with 1, we did not emphasize splitting out the country code.
We measure verbatim parroting for all model sizes at the 143,000 iteration checkpoint for a prefix length of 80. This is an extension of Table 2, where we report the percent of instances that are verbatim parroted.

## Actual owner books/part-07-agent/75-context.md

### 原文件L194–201
派生视觉接口不只用于原生图像，也能承载旧文本 observation：逐项渲染较老的工具结果，actions 与近期 observation 仍保留文本，而不是将全部历史改成像素。它改变 consumer 的输入接口，不改变证据身份；搜索服务已生成的摘要，渲染后仍是摘要，不会恢复成原网站事实。原文本、引用与恢复入口仍须保留，stale/fresh 分界与表示选择共同决定当前可见视图。

POINTS-Seeker exact-v1 需要训练 consumer 适应混合表示，并支付渲染、图像编码与原文恢复成本；有限对照中全部转图像反而较差，token 减少不能直接外推为端到端时延或证据无损。长轨迹与模型、任务变化须重测；短轨迹、逐字协议或适配不足时，直接携带文本仍合理。这是与 active slots 并行的表示分支，不是删除原始 artifact 的授权。
<!-- semantic-body-binding:SF-2026-ARXIV-2604-14029:end -->

旧tool observation也可压成soft tokens而不是图像，保留native tool envelope、assistant actions与近期原文本；这只是读取接口，逐字工具参数仍应回读原source。训练同一个adapted decoder读compressed view时，还需另在full-text view对原base分布作anchor：前一项教新表示读取，后一项限制旧接口行为漂移，不能由重建loss好推出工具策略没变。两个view按assistant-token身份而非压缩后的绝对位置对齐；若只缓存top logits与一个tail bucket，约束的是粗化分布，不是全部tail行为。

[受限latent-observation对照](https://arxiv.org/html/2609.31430v1)中，更好literal recall或更强teacher仍可能降低任务成功，默认近期窗口也比uncompressed base退步。扩大硬文本窗口改变quality、encoder驻留和KV预算；observation由text移成soft时还会使旧prefix从变更点失效，encoder缓存与decoder prefix复用要分别计账。受限窗口/并发优势相对同adapted fulltext，且排去最后长任务tail，不能叫全轨迹总成本或可靠性保证。Anchor是软约束而非task certificate；无足够behavior回归、原文可完整驻留或必须逐字时，保留原base/fulltext、较大近期窗口和可恢复source，再按实际task/latency预算选择。<!-- source-family:SF-2026-ARXIV-2609-31430 -->

### 原文件L247–253
Summary、extractive compression 和 structured state 都可减少 token。压缩函数可写为：

```text
C'_t = compress(C_t, task, budget)
```

目标不是最短，而是保留对未来决策充分的信息。摘要可能丢失 exception、否定、数字和 provenance；递归摘要还会累积漂移。

### 原文件L263–275
压缩准入还要算总时间，而不只是比较压缩前后的 token 数：同一请求上，`T_compressor + T_target(compressed) < T_target(original)` 才有时延收益；还要同时验实际压缩率、答案质量和压缩器的显存占用。短输入、便宜的目标模型或较慢的压缩器会使前处理吞掉 prefill 节省；长输入、可摊销的压缩结果或受限显存则可能改变选择。这个 break-even 随目标模型、硬件、长度、批量与并发重算，不能用单一压缩比例作为通用策略。现有作者实验只覆盖所测 LLMLingua 分支、模型/设备与任务，未建立生产尾延迟或任意证据保真保证。<!-- source-family:SF-2026-ARXIV-2604-02985 -->

压缩容量也不必只依赖原文长度。一个受限分支让 query-aware encoder 读取分块 Context，由其末端 hidden-state probe 估计相关内容长度 `L_hat`，再以 `k=min(L_hat/r,k_max)` 决定 soft-token slots，并把兼容 K/V 交给目标 reader。它把固定 slot 数变成 query-adaptive capacity，但相关长度不是充分证据，也不证明压缩结果可供任意 reader 使用。Teacher 相关标注、encoder/probe 与 ratio/max policy 都须保存身份，额外 encoding、probe 和质量回归也要计入 break-even；[局部压缩对照](https://arxiv.org/html/2602.03226v1)显示短输入可能因 slots 过少而退步，不支持“压得越短越好”。长度估计失配、必要细节被丢掉或总成本不合算时，应扩大 slots、回读原文或退回固定容量/未压缩输入。
<!-- source-family:SF-2026-ARXIV-2602-03226 -->

重复日志还可以走另一条分支：不概括含义，而把重复子串替换为短标记并附字典。此时应把字典、标记和说明一并计入目标 tokenizer 的输入预算，并区分两个接口：软件按规则还原原文，以及模型直接在编码态完成任务。前者可以是确定性的 codec 合同，后者仍依赖模型是否正确查表、保持跨行关系并执行目标分析；可逆编码本身不会把这种能力一并交付。<!-- source-family:SF-2026-ARXIV-2604-13066 -->

因此，解压 exact match、字符相似度与目标任务正确性要分开验收，不能把较高的字符串重建分数当作日志诊断或跨记录推理的保证。作者的重复日志实验支持字典表示具有压缩空间、所测模型能够在部分协议下重建文本，但没有验证目标 analytics，也没有证明解压是所有语义任务的能力下界。重复度低、字典开销大、目标任务依赖未验证的编码态操作时，原文或先由软件解码再调用模型仍合理；高风险记录的原始 artifact 和逐字约束不能因 codec 可逆而移交给模型猜测。

"充分"必须相对于未来任务定义，而不是压缩器自认为语义相似。跨 session handover 可以按三层保存：必须逐字保真的决策、约束与授权；对已知 future-query family 足够的统计量；以及无法安全归约、可供以后回读的原始 observation。理论上最小状态只需保持未来 target distribution，但开放 Agent 通常不知道未来 query，也无法证明自动摘要已经达到 predictive equivalence，所以高风险或任务未知时不能删除原文。

这种分层用较小 handover state 换 writer bias、任务分布假设和错误归约风险；短会话、存储便宜或证据不可约时，完整 transcript 仍更透明。`arXiv:2608.14528v1` 在 exogeneity 等假设下给出 deterministic sufficient handover 的理论刻画及 Gaussian/nonparametric regression 上下界，不证明开放 Agent 能自动知道未来问题、可靠抽取最小状态或忠实保留决策。


## Actual owner books/part-06-ai-infrastructure/72-security.md

### 原文件L47–49
最小披露还有一条容易遗漏的边界：把秘密改写成含糊表达，不一定比完全不提更安全。若无防御时模型本来不会提及某个私人主题，加入“用可接受的抽象表达代替细节”的提示反而可能产生新的可推断线索；减少完整泄漏和增加局部泄漏可以同时发生。因而隐私防御不能只比较总泄漏率，还应逐私人项记录从不提及、局部暗示到完整披露的转移，并与无该提示的同场景基线对照。[受限证据：AgentSocialBench §4.2.4、Appendix D](https://arxiv.org/html/2604.01487v1#S4.SS2.SSS4)

作者合成社会协作场景中的组合提示与模板盲 judge 支持这个受限风险，不独立证明每个提示组件的因果贡献，也没有证明统一禁言能兼顾所有任务。若协调确实需要相关信息，应由权限与最小披露策略决定允许提供什么，而不是让模型自行把敏感主题换词；若任务无需它，避免提及更稳妥。该选择增加任务可用性与隐私之间的冲突，仍需独立的隐私边界、收件人和任务效用评测，不能把抽象语言评分当作无泄漏证明。

### 原文件L279–285
### Membership Signal 必须先通过可识别性审计

以目标文本的低 loss 判断其进入过训练集，在成员与对照来自同一分布、重复次数可核验时，是便宜的 privacy sensor；但
文本知名度、文体流畅度、编辑质量和语域变化也会降低 loss。若对照只是删除或改写一个词，检测器可能学到“哪句话更像
作者会写的”，而不是数据成员身份。审计必须先绑定 corpus/version、目标的可验证出现次数、模型与 precision、register-
matched controls 和 attacker access，再在作品内或来源内中心化 nuisance variation；未通过 identifiability 的 signal 只能
触发进一步调查，不能形成删除、泄漏或合规 verdict。

### 原文件L295–295
黑箱 chat API 不能直接读取任意输入的 likelihood 时，还要改变 query 本身：把完整 canary 放进“请复述”会混入 echo 指令效应，一条更窄分支只提供属性值的两个字符或数字前缀，让模型完成片段，并以同 probe 的 generic-subject baseline 减少常见值先验。[受限 fragment-completion 审计](https://arxiv.org/html/2602.17483v1)用五种句式与20个随机前缀形成竞争；能取得 token log-probability 时计算校准分数，否则只能聚合 top-completion votes，两者不是同一 likelihood 估计量，集中度也不等事实正确或训练 membership。前缀仍提供条件信息、可暴露敏感值线索，并可能把多词值截成头词，不能签发隐私保证。同 Llama-3.1-8B 的 raw/chat 对照只显示局部结果变化，出生地和职业反退且措辞更敏感；主评语义匹配阈值0.60与该验证0.75也不属于同一协议。Prefix数、句式、baseline、输出过滤、匹配粒度和模型 revision 须共同绑定，多轮query与身份真值治理均付费；接口或ground truth不足时保留“条件关联/真实性未知”，回退可核 raw-score、受控canary与provenance，而不把 famous/synthetic 差额或高集中度当作真实记忆证书。<!-- source-family:SF-2026-ARXIV-2602-17483 -->
