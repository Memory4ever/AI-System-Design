# DapQ 2603.11564v1：必要 Source / owner PRE

作者mar14_supplement；首包准入与日级arXiv日期已独核，复用。评分 **2+2+2=6**：future-position synthetic probe替代真实draft/训练selector；跨RoPE、Prefill和cache mutation；位置/内容与观测窗口边界可复用。标准最低深度，明确owner差额所需局部深入；不为NIAH99.5%或现成通用proxy原则加分。独立Source/PRE待root，无共享写入。

## 原文与机制

[v1 HTML](https://arxiv.org/html/2603.11564v1)保存`SUP_CORE_11564.raw/.txt`，`SUP_CORE_FIRST_MANIFEST_RESULT.json`是获取原记录。实际读§3–6/Eq1–5/Table1–4/直接Limitations、AppendixA.1必要干预设置、B.1–B.6配置与C定理条件；未遍历其它任务附表/代码/完整版本史。

§4/Fig1：给长L_p prompt追加N合成tokens，位置明确L_p…L_p+N−1，同Prefill取pseudo queries；每个query读取原prompt keys的attention累积后TopK，删除未选prompt KV和整个synthetic段，**真实decode从原L_p位置起**，不把probe当输出。所有baseline仅在Prefill压缩（§5.1），不能授long-output per-step eviction或常量总cache。默认N32，prefix/suffix例如4+28或2+30；无需真实future answer或独立训练selector，但仍新增合成tokens前向与TopK临时成本，不是无成本/0peak。

§3/Table1+A.1的GovReport一个4424token例子中同位置不同内容cos.7238，同内容不同位置postRoPE .3522；后者preRoPE .7913。Table1不是所有模型普遍命题；position处理能显著改变同一query的RoPE几何，不能据此宣称模型语义内容不重要。Figure2扩大到100随机trials仍是干预人口，不是真实未来任意task。§3.3 recall gold是**真实response queries attention TopK**（Eq1–3），不是答案因果重要/未来质量oracle。AppendixC明示fixed KV/unit queries/max key norm，有上界不能推出未归一query任意future/全网络保证，实际采用经验proxy而非定理最优。

§6.1 prefix/suffix内容实际比random/repetitive更好；§6.2 window非单调，过长未来位置及probe互读可能引入噪声；§6.3 prompt内插入受causal mask无法读全prompt，而把position搬到更远未来又失配。Limitations承认semantics非零作用、各层敏感不同。保留position/内容共同校准，不照录标题“where more than what”为通用规律。

## 评价、反侧与未披露

LongBench Llama3-8B、Qwen2.5-7B、Qwen3-8B reasoning OFF，budget64/128/256；LongBenchV2/RULER/HELMET/NIAH只作作者所述受限context评价。主Table2 Llama3 full均值48.39→DapQ25646.4/6441.81，GovReport31.03→22.25/18.46，TREC70→60.67/38.67；并非无损。NIAH99.5%只是简单needle协议单点，不能替代multi-hop/summary/longreasoning。与其它compression也非逐任务赢：Qwen3-8B/b256 Qasper32.14< SnapKV32.40；b64 GovReport17.16< H2O18.55。不因反侧排掉具体机制。

§5.3+AppendixB.6效率为Llama3.1-8B，单**H20 96GB**，native HF Transformers4.53.0/PyTorch2.6.0/FA2.7.4，不是vLLM。input8K/output150/budget256，batch1/10/20/30/40/50；Table3 b1 Full11.59t/s>DapQ10.68，b10 Full26.43<DapQ34.16，DapQ与SnapKV相近。Table4 8K TTFT1.1106s→1.1298s，128K60.8399→61.5097；不是TTFT无代价。precision、TTFT测量batch、真实到达/concurrency/SLO、重复seed/CI未披露；batch列表不是online concurrency。无实现核验/复现，不外推cache逻辑选择已有物理page回收。

## 具体 Books 差额与两段提案

owner `INFER-KV-CACHE` Ch45。复用刚实际读过的相邻Ch44/46与Ch45完整future utility路线（约730–774，LongFlow新增仅在较前位置不影响这些论点）；现有稿覆盖prompt-local、昂贵real draft、trained implicit lookahead、target sampled futures、retentionproxy/lifecycle。**尚未承载无需训练selector/真实未来生成的position-aligned synthetic probe与discard/reset接口、probe太长/内容仍有影响边界**。位置+artifact语义不是泛泛“future query重要”已有覆盖。

建议在learned implicit lookahead三段之后、`显式未来也可来自冻结target…`之前窄插（原LookaheadKV段不变，独立marker）：

> 不愿生成真实future draft或维护trained selector时，还可在Prefill临时追加少量synthetic tokens，给它们即将开始Decode的position IDs。其queries累积读取原prompt keys的attention，选出保留集合后，probe自身的KV与未选历史一起移除，真实Decode仍从原prompt终点开始；不能把probe计入交付文本或把压缩后slot序号当成新的RoPE位置。这条training-free路线利用位置对query几何的影响，但不是获得真实未来信息：attention-TopK重合只测一个保留proxy，不能保证答案的因果证据未被删。
>
> Probe内容、长度和位置仍须与model/workload共同校准。Prefix/suffix内容可能比随机tokens更好；过长probe增加前向、排序与临时状态，也可能因远期position和互读而稀释信号。放在prompt内部会受causal mask限制，移动到更远未来又可能失配，因此“位置重要”不等于内容可忽略。受限长输入、短输出的作者对照里，质量仍低于FullKV，batch1吞吐和TTFT也有代价；Prefill一次选择不解决长输出动态增长，更不证明page reclaim或在线SLO。质量/成本回归不通过时，prompt-local、trained lookahead、真实future probe与FullKV继续作为不同成本路径共存。

拟note：`2603.11564v1 §3–6/Table1–4、AppendixA.1/B.6支持位置对齐synthetic probe→TopK→discard/reset路径；GovReport/summary质量、semantics与N/window/position失配反侧保留。H20/nativeHF受限，不授在线SLO或page回收，未核artifact/复现。` 独立Source/PRE通过才root窄写，作者做实际非writerPOST。
