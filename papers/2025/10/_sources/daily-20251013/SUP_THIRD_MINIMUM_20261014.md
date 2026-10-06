# 第三批两个最低决定域

最新root独核§7已actual MOJO IV-A/B/Algo2/V-C/TIV/VI/VII与ImCoref3.1/4.3/T5/limits/T18，通过两最低窄P；第三12现在9P3C、无N，不重有效域。下文末待root只是准备历史，其他日期/测量/Books权限不被该层授予。

作者Kierkegaard；两个exact-v1原HTML真实200/exit0，读取本文具名最小域；代码/fuzz/prompts不运行。原首输出MOJO中段截断，随后重新完整读取IV-B全部，不能用截断冒完整；ImCoref T18另独立完整显示。只准入裁决提案，日门/score/Books另权限。

## 2510.10179v1 MOJOFuzzer：N→窄P提案

[原HTML](https://arxiv.org/html/2510.10179v1)、[saved196445bytes](SUP_CORE_2510.10179_20261014.raw)。实际IV开始/IV-A必要data和seed说明、IV-B完整含Algo2、V-C完整TIV、VI/VII。没有重述或执行代码/payload。

成熟prompt/seed bank＋two-stage syntax/bug SFT不是新名准入。原具体分支把code-level seed mutation与prompt-level再生成分责，模型生成“有效API/可执行语法/语义作用”三层不等；TIV FT-alone比HM-alone对hallucination减少明显更大，GPT4的mutation score相近但API常错，代码复杂度/调用数优先不是测试消费资格。这一反馈选择指标与生成能力的反侧可保窄P，而非13bugs/编译器名字。

须保中心分支争议：文字说高score Half(code)/低score Full(prompt)，score=N_API＋complexity buckets；Algo2在FuzzingTest失败时<=50走SeedMutation、>50走PromptMutation，与该方向不同；成功>50仅register。未披露score1–5具体值/归一或FuzzingTest成功的统一bug/valid口径，不能静默写成正确配方。IV-A/B明确LLAMA2-13B领域syntax/bugs finetune，所以“zero-shot environment”不授无目标领域数据/无训练。TIV三metric并非端到端未知bug/全安全，V-C HaluEval-inspired detector未提供这里所需独立truth/样本分母/重复不确定性。保狭窄测量与分支角色，不采完整recipe、全自动/不幻觉或全预算净优。

## 2510.10241v1 ImCoref：N→窄P提案

[原HTML](https://arxiv.org/html/2510.10241v1)、[saved467554bytes](SUP_CORE_2510.10241_20261014.raw)。实际完整3.1、4.3/T5、Limitations以及AppF完整T18，未阅所有附件。

原相邻独立chunks直接拼接不能传前段信息，LBM用前段SEP hidden作为carrier，broadcast-concat→FC或MHA→residual+Norm调制后一chunk，left-to-right且只independent策略。具体跨段carrier/消费位置与quality-resource条件可保，而非Checker-Splitter泛RAG/agent组合。SEP瓶颈不等full-context/cache状态或所有长程关系完整；MHA两个参数未说明Q/K/V shape，不自行补实现。

T18独立/overlap/LBM实际对照：OntoNotes AvgF1 81.4/82.1/83.1FC/83.6MHA、baseline84.3；LitBank76.5/78.4/79.0/79.1、baseline79.2。不是恢复无损/所有segment优于fullcontext；增加3M/9M参数及训练/推理时间。4.3/T5 mention P/R与cluster AvgF1分开，C-CeS减去不改mention指标却影响coref，不能将syntactic mention正确当clustertruth。eta增到.6后F1plateau但inference费继续增，具体消费范围比全量LLM核更有效；两个数据集/此encoder的局部条件，不外推foundation architecture。全文不因为传统NLP或已有FC成熟组件关闭。

第三12提案现9P3C无N，等待root两域实际独核，不预签。其余必要偏差反侧仍普通，旧有效层不重。
