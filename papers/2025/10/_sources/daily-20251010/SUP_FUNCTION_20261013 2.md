# Oct10单篇：Function Tokens具名原研究日期与准入

2026-10-13本次已实际打开[Seed原研究详情](https://seed.bytedance.com/en/public_papers/memory-retrieval-and-consolidation-in-large-language-models-through-function-tokens)，页面明确2025-10-09、同title/三作者Shaohua Zhang、Yuan Lin、Hang Li、完整研究摘要、Venue arXiv与Download PDF2510.08203。原作者论文首页实际ByteDance Seed机构身份、同三作者邮箱与Oct9文稿日期；Seed机构自有研究栏目完整题摘/作者/原稿、独立PublishDate与UpdateTime支持Oct09自身研究披露事件，不机械要求单独Blog，也不因为目录形式永久hold。作者详情本身仍不证明arXiv announcement或互联网绝无更早原稿，不用Submitted代它。日期拟层直接交root核，不等14源。

本日US论文API实际tokens0/20/40/60/80读取各页metadata，19/15/19/19/13＝85，total94、尾has_more=false，不能冒94全部可见。仅具名316身份完整字段及AB读取，未将85正文入队；316 ArticleID316/type1/PublishDate1759939200000、同三作者/外链相符，更新时刻2026不代原发布。旧94API、当前web242/13页和具体原研究详情权限分开，不因午夜归一化或旧09:00窗口阻断补充Oct09完整自然日。

本轮实际完整读[精确v1 abs](https://arxiv.org/abs/2510.08203v1)，唯一v1、Oct9UTC13:31:20只是提交角色，非first-public；[v1 HTML](https://arxiv.org/html/2510.08203v1)真实可读，已读首页/§1/§2及§3.1前段。频率阈值近似function/content而非语言学精确分类，Gemma2-9B/SAE token-feature图是观察测量，不授所有LLM记忆机制。当前可见abs无新具名纠错/撤回说明，不证明全站无变化。

root本日实际§3已通过机构Oct09自身研究披露/完整题摘/精确v1身份与窄P、2+2+2=6，不再待日期准入。窄命题：把参数记忆当静态存储→在特定模型/SAE及训练设置中区分高频功能token的上下文特征激活与后续content监督→可能改变只按词义/频率解释参数检索与训练loss贡献的判断。Ch17 owner正确ID为MODEL-TRANSFORMER-LAYER，原误写MODEL-TRANSFORMER已纠正；需与Ch5表示解释比较后只选一个owner，不跨章重复。不是Agent外部memory，不借模型规模/假说名字准入。

## 必要Source实际已读，供root独核

本轮现实际读完精确v1§2/3.1–3.2、§4.1–4.3、§5/7及必要Appendix8/10；HTML本次HTTP200但exit28、176969/211074B partial，所需section真实可读，[raw](supplement-20261013/function-v1-html.raw)保持截断角色，不授整份成功或所有附件。Seed[原研究详情raw](supplement-20261013/function-seed-detail.raw)200/exit0保存。本篇暂无另一个具名先稿身份，不授absence-proof或继续全网考古。

采用限三个证据层，不把假说升普遍因果：Gemma2-9B三层SAE token-feature图观察、高频分类与有限上下文steering、两训练模型的条件loss轨迹。122类function token由SlimPajama/LLaMA tokenizer累计40%频率近似定义；图对任意context一次激活就连边，高频token暴露更多context，累计覆盖不等频率匹配后的独立机制贡献。三trait/精选prompt的最后newline干预展示可改变输出，不证明同位置content token不能或普遍“最预测”特征；Appendix8用同20非trait集合选最佳层再评，选择偏差/缺独立held-out保持，未跑steering。

训练1.5B仅2层与8B32层不只是参数数目差；feature counts只1.5B/第二层三checkpoint、SAE设定改变。Appendix10为对齐reconstruction score将lambda设10/4/2.5，稀疏惩罚和dictionary measurement随之变，不把feature数增长全归为模型记忆容量因果。各group条件平均loss高不等其token权重总loss/gradient支配；原文没有独立删除/重权function→content训练对照证明推动特征唯一原因。§7“preceding function tokens”与§4/5“following”方向文字冲突保留，不静默修成完整理论。root本日实际§5已读这些必要域与全部上述反侧，作者沿有效层不重读。

最终Source采用层：标准6分必要观察范围为功能token位置在受测表示中有上下文相关激活/局部可干预性，以及当前→next两类token分组的loss轨迹；具体解释性强claim已必要深入反侧。只这组条件观察，不采用所有LLM记忆唯一中枢、所有知识真实语义、全局因果优化路径或scale-free普遍律。必要Source读域与反侧沿root实际§5有效，不再待该层；中心hypothesis仍未证，此限定不抹窄P/6分、不降分或缩池。

## 实际唯一owner与中心争议暂缓提案

实际读Ch5开篇/动态状态与因果读出L14–42、表示/selection边界、平均loss人口L189、Superposition L199–217，与Ch17前后及token-path梯度L290–313；邻接Ch4/Ch6开篇交接已读。唯一owner定为WORLDVIEW-REPRESENTATION Ch5：本篇要改变的是参数知识怎样被上下文计算消费的解释，不是新增Transformer residual算子，故不改MODEL-TRANSFORMER-LAYER，不向Ch28重复写loss理论，不把Agent Memory当owner。

Ch5 L40–42已明确动态输入状态/可读不等实际使用、受控行为干预才支持局部因果；L201–207已区分稀疏投影、访问合同与输入覆盖，L217保SAE诊断非自动行为证明；L189保人口/频率/均值loss分责。它们具体承载本次安全可用的诊断资格，不是因为主题相似而声称function-token机制本身全部已有覆盖。受测频率/位置观察仍有报告价值，但原材料没有足以把“function→content是特征扩张因果驱动、function token是唯一记忆门”写入长期解释的新隔离机制。

因此拟Books处置为暂缓中心hypothesis，保本篇确定Oct09机构披露、6分及上述完成的必要观察/反侧，不造0分排除，不删除候选或改分。当前不提出Books写锁/新段：这不是以证据费时或既有覆盖缩池，而是已实际观察到暴露/测量/梯度归因与文字方向的中心缺口，不能修好原文再采用。可接受恢复是同家族原作者/独立primary给出的匹配token暴露与位置的干预、独立held-out steering、固定或对账的SAE测量，以及按出现权重/实际梯度或受控训练消融归因的证据；只重开相应命题，不要求全网absence-proof、附件全读或重跑本日Source。

本窗终态争议提案严格隔离：未证中心hypothesis不用于正面Books/因果/性能安全保证；保有效观察与当前采用边界，不让任何缺口反向使原已读层失效。此Books最终裁决待root实际核；作者不自签，无锁/写入/POST要求，未日级DAY。

root本日实际§7已通过最终Source限定、唯一WORLDVIEW-REPRESENTATION/Ch5与中心hypothesis暂缓Books决定及上述定点重开条件。保确定机构Oct09披露事件/6分/必要观察层，不删候选或改分；本篇无Books写入或POST义务，普通必要Source/owner裁决已结束，不重有效域。本轮来源与DAY仍独立普通，未增加计数。
