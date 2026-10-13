# 必要局部证据与处置（进行中，待非作者核）

以下精确v1已完整题摘校准；日级首次arXiv夹证原字段在SUP_DATACITE_BATCH/OFFICIAL_SUPPLEMENT，不把Submitted/registered当公开时刻。精确ID/同稿去重尚须完成新增批次。

## 12465 TaxBreak：2+2+2=6，深入必要证据，拟已有覆盖

[原v1](https://arxiv.org/html/2603.12465v1) §II–VII实际读。§III三层framework translation/CUDA-library front-end/kernel-launch floor+HDBI为实际增量，不借一般profiling自评分；HDBI是device-active对device-active+orchestration的工作比，非GPUutil或墙钟因果分解。隔离null replay、匹配kernel的fallback对dynamic/autotuned/synchronization-heavy可错；device-active可能重叠。§IV–VI有限dense/MoE/eager/FA2、单H100/H200与不同Xeon/BF16/PyTorch2.10/CUDA12.6/实际batch/length配置，并非生产并发/SLO保证。FA2能降低绝对总延迟同时降低HDBI，ratio不是优化目标；跨CPU/GPU组合不能承诺单独CPU因果。

实际Ch49 L173–183顺读，177段已经承载三层host税、HDBI、trace诊断不拥有request admission/placement/revision、instrumentation及硬件/软件改变比例、粗profile仍可合理，唯一owner INFER-TENSORRT-LLM；必要Source与已有覆盖判断经reader通过，不制造重复段落。原“精确拆”超出replay能力，root授原177两处及本注窄锁，已改为baseline三层估计、HDBI非墙钟或精确因果分解。review_mar17_18非writer实际169–188完整邻接/new177及本人注POST通过；末注现2851已更新真实POST，最终定点复读待同步。不采用论文更广普适host-bound或额外核心收益，optional artifact未核不称复现，不授DAY。

## 12582 RTD-Guard：修正仅traditionalNLP EX，2+1+2=5，安全反侧深入

[原v1](https://arxiv.org/html/2603.12582v1) §4.2/5–10必要核心实际读。旧拟EX只因BERT/NLP范围不是有效理由；reader实际§4.2/5独读接受classifier分支准入。已偏移label下WIR定位可能失真，RTD排序不读取victim内梯度，top-k5 mask后对原predictedclass测两query squared-confidence-shift。RTD只是替换不协调信号，非对抗语义真值；threshold以验证集校准，非完全无校准。

§6–8三BERT classifier/IMDB AGNews Yelp、四TextAttack词替换非adaptive攻击，ELECTRA-large无finetune、k/干预方式/模型规模消融；安全反侧未证明对知道detector的自适应攻击、跨语言或LLM注入。作者3090/2444 AGNews TextFooler runtime35.3s对victim8.9s，不是免费两query：含RTD forward、mask、二次API，约四倍该局部baseline；batch/precision/concurrency/tailSLO Not Disclosed，不能推production。§10明确语言匹配限制和生成式LLM防御只是futurework。拟只采用token选择信号vs被攻击label的局部分支，必要Source/现有Ch72具体覆盖比较尚ordinary，未写Books。

## 12683 Self-convergence：候选最低关闭提案，1+1+1=3，不是贡献EX

[原v1 PDF](https://arxiv.org/pdf/2603.12683v1) §3–5/P6–14必要实验设计/结果已实际读，不能因摘要未解释训练原因直接EX。443章两studyguide旧摘要、同prompt/API，T0三/T1五改写；按文本做词组SPR并在模型间比较。负结果在T1局部版本较高长词组重合，T0最新5.2部分相反且GPT5无T0；同knowledge-cutoff版本亦可不同。局部重复模式是可记录新增事实，但对象仅闭源版本、有限文学改写和指定词组度量，不是任意多样性机制/语义创新或全部模型退化；未知训练数据和未干预的版本共变不授synthetic-data因果。

保留初拟1+1+1=3理由：新增设计变化局部版本行为、单输出负载、版本相关上下文，而非给借用的一般“能力不保证diversity”原则计Durability。相同temperature数字不匹配各版本输出分布，输出长度亦不同；组内重复/SD不是独立训练重复，精确API snapshot、未披露decoding参数或修改不借后续版本回填。不因因果归因缺失抹去局部负结果，已关闭/仅报告其版本上下文，不进入Books；review_mar17_18独读exact-v1 PDF §3–5/P6–14、SPR定义P4及上述局部反向，最低关闭/版本上下文PASS，不是贡献EX或工作量降分。v2 metadata仅说明版本存在，不自行证明重要修订，本次不借v2替v1。
