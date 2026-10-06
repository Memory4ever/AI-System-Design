# 2026-01-30 第四批 RL 与安全必要证据

精确v1；作者审阅，root必要命题/直接反侧实际复核通过，均局部OnlyReport。本文不运行代码或授生产保证。

## [Inherited RM values / 2601.20838](https://arxiv.org/html/2601.20838v1)

2+2+2=6，设计反侧深入。96–119、241–273：10领先RewardBench Llama/Gemma RM，54正负prompt、BigTwo263/MFD2040词，mixed-effects/多重检验，用共同token子集避免部分tokenizer差；价值词rank不是完整人类价值或实际RLHF政策。对pretrained/instruct logprob与新RM沿训练观察，Llama3.2 3B vsGemma2 2B不同大小/架构/pretrain均有混杂，不能隔离某pretrain机制因果。控制same LoRA r32/a64、AdamW1e-5、batch16、seq1024、2epochs/固定seed，Skywork80k、UF13/26/53/106k；checkpoint1000steps。两轴差缩小但原80k不闭合，~100k可减Llama/Gemma差，Qwen与GRM保generative regularizer反侧不随数据充分闭合；GRM632k为他人产物非samecontrolled，机制待核。硬件/重复trainCI Not Disclosed。仅报告：词级评价说明init family与RM objective不能由RewardBench rank或配对数量自动消除，不授模型价值本体/普遍100k阈值；具体机制尚未披露，不改书主干。

## [DenseGRPO / 2601.20218](https://arxiv.org/html/2601.20218v1)

2+2+2=6。§4/5 158–244/371–407、Appendix631–659：每中间latent用n步ODE完整还原后reward，相邻reward差group归一作步advantage；noise强度按正负reward balance离线校准后固定，不是训练中online调噪。n1可差于FlowGRPO，不证明任意clean-domain评价准确：ODE路径特定潜在回报不是counterfactual真实因果credit。SD3.5M，三task GenEval/PickScore/OCR、train10step/eval40step、G24/512²/KL.04或.01、16A100、LoRA32/a64、AdamW3e-4/batch144。20trainsteps n1/2/t成本11/13/19GPUh；同时间图显示局部收益，不能只报same steps或免费dense reward。CoCA改造成Flow版本非原实现直接比较；DrawBench alternate评估及B4有rewardhack：count/OCR改善可能图质差。没有human safety/生产SLO，precision/重复CI未披露。仅报告：此flow训练的reward-domain误差、调噪与compute代价边界，尚非所有denoising目标适用的可靠credit理论。

## [SDPO / 2601.20802](https://arxiv.org/html/2601.20802v1)

2+2+2=6。§2 154–177/214–239/271–307，code§4 450–491、Table6 601–641、TTT679–708、limits748–765、hardware1836–1840：当次策略feedback-conditioned teacher stopgrad，用logitKL自蒸馏，无额外teacher generation但需teacher logprob；top100+tail节省logits内存，EMA/初teacher插值+JS稳定。LCBv6 131问题train publictests为private随机50%子集，Qwen3默认8B，4rollout验证48.8vsGRPO41.2局部，不与榜单他模型不同协议直接比；Qwen2.5 1.5B可劣于GRPO。Table6环境+同batch成功解互补，只有solutionsteacher42.4但student36.8/entropy.07，加原attempt也偏teacher、降低探索。TTT hard19/veryhard9按任何方法512steps/5seeds至少成1次预选，bootstrap90%仅5seeds；discovery budget不含梯度全算力，不能认为未选不可解所有问题皆改善。4GH200378GB CUDA12.8/Pytorch2.7/FSDP2/vLLM，wallclock排initialization/validation；小模型短rollout开销更大，misleading/uninformative反馈可失败。仅报告：具体feedback-owner与selfteacher容量/探索条件，未在通用‘反思必纠错’成熟原则上强制造diff；科学domain只说明方法评价范围，不纳入AIforScience应用链。

## [DrainCode / 2601.20615](https://arxiv.org/html/2601.20615v1)

2+2+2=6，安全深入。III/IV 129–198、V199–225/530–581、VI922–931：攻击需可污染检索库、源模型梯度，hypothetical-query对待检索code近似实际query；1–3样本使被retrieve为必要触发，不是无检索/用户权限系统普遍漏洞。EOS/diversity/KL proxy+multi-position/buffer mutation，KL放loss指导，不是已证明输出非trigger位置完全不可区分/功能等价。RepoEval373/1.7Mfiles、Odex945/34kdocs，BM25/context2048/output1024、两A10080GB，10mutationiter/64candidate；source2code+2general。NVML GPU energy/latency不含CPU/memory、平均请求非SLO/concurrency，无安全非劣保证。黑盒transfer也有最多9%Pass1降低，与summary95–99%accuracy/‘preserve’不一致，不能抄‘准确率不变’。poisonprep216/53.2s对760/185.9为攻击自身成本不是受害服务加速；10repeat固定seed残差未全面CI。仅报告：具体检索注入可保一些tests却浪费资源的可行性风险，不授所有retrieval/future防御失效、攻击完美语义保留。
