# LycheeMemory08382：必要Source/owner/PRE请求

Dynamic Long Context Reasoning over Compressed Memory via End-to-End Reinforcement Learning，2602.08382v1；2+2+2=6，静态latent bank与明文working state分开、gate在昂贵rewrite之前以及单向state-dependent召回失效差额深入。root完整AB/日期通过。chunk-core.json§3/4完整实际读，chunk-direct.txt必要A1–5/Algorithm1/C。不核artifact、不修一般GSPO实现。

§3 chunk4096/interleavememorytokens alpha4，comp LoRA encoder后memoryhidden作为KV-style bank；本文hidden representation与A5按各层GQA KV存储口径并非精确serialization已核，不授一般cache可移植。base frozen，comp/ gate/ reason三个LoRA不同角色；gate(Q,currentplaintextm,latentchunk)最后hidden sigmoid，>tau才调用reasoner生成更新明文m，所有bank单向扫一次，不是索引直接跳读/无限回溯。gate独立BCE而非RL policy joint：A3 rolloutsupportlabel posweight3/r16/3epochs/lr5e-5/tau.5，GT支持不代表部署知道未来证据。comp预训recon/QA/selfannotatedcreative，alpha随机2/4/8/16/r64，约160Meffectivetokens/5000steps。jointRL group12/b128/update16/KL1e-3/lr3e-5/150steps/~3days2A10080GB，strictanswerexact标签vsnormalizedsubEM评价不同，filtered32768/192val与singlepoint预算不授全局稳定。

§3.4/Algorithm1将deterministic continuousmemoryhidden写成sampleTheta~pi_comp并需jointmemory/answer probabilityratio，但必要源未定义memorysampling分布/density及如何给latent编码器importance ratio；不能据符号称jointGSPO实现已核或给gradient-through-gate guarantee。可保作者joint训练局部表结果，不借它解释唯一机制贡献；如需恢复仅请求该sampling/density/gradientroute定义，不遍历全文维修。

§4T1 gate质量在112k75.78<nogate80.47、1.75M71.09<78.12（vsMem75.78），绝非等质量加速；896k72.66<nogate75.78。T2 2Wiki28k70.3<Mem73.4，StreamingF180.8<RAG84.3。T3 top8matchedchunks recall query+memory98.5/86.3/84.1 >queryonly88.2/76.4/74.8，但embedding切1024micromax与gate不同representation/training，非唯一state因果；embedding也可条件化query，原文‘external不能利用m’只它静态baseline限制。

端到端timing2A10080GB/128samples8k–128k/gen1024/largestnonOOMbatch不同batch，包含comp+IO，128k6×Mem/3.5×nogate对应最邻112k质量不是同长度match；Table1蓝28.2×1.75M只相对nogate，不授所有servingTTFT/SLO。precision本timingND、concurrency/重复CI/SLO ND。alpha4near-lossless等于alpha2质量相近，不是raw information无损或独立statistical test；4vs2存储半仅representation条件。

A5 offlineprecomp默认，>1M可optionalJIT；1.75M/3B GQA/bf16 KV估18.1GB不含weights/activation，offload只是提出option，JIT单forward不等free/lowlatency。C128randomincorrect验证样本而非全人口：35%singlepass逆依赖（先前被gate拒，后续bridge才相关）、21%早期锚定、17%压缩实体混淆、其余27%；作者归因非受控机制因果，但作为真实failure signal必须保。O(N)依赖fixedchunk与T稀疏，本方法仍遍历所有gate，不能称documentindependent/nearconstant一般法则。

actual AGENT-MEMORY Ch77 379–403 querylocalconstructor/rawpointer/learnedcurator、153–168memorylocalcredit/GRUMem先生成candidate再discard/exit已读；新路径则queryindependentlatentbank、在rewrite前gate(Q,m,theta)，输出m仍plaintext且单向扫描早期reject不能重新变相关。具体差额存在，不由已有泛‘state-dependent检索’覆盖。Ch76/78入口actual核，Ch22是architecture历史读取owner，本文Agentmemorycontrol唯一Ch77。拟在query-local constructor段389之后、factmemory成本段前一段（读写与运行费用连续）。尚无root Source/PRE/锁，未写。

拟文：读时构造还可以先把历史按块存成压缩latent bank，让相关性判断读取query、当前明文工作记忆与候选latent块，只有过门才调用reasoner改写工作记忆。这把静态存储和动态推理状态分开，也把筛选放在昂贵candidate生成之前；不是省掉全部扫描，每个块仍需gateforward，压缩/JIT、adapter与存储IO各自付费。后续bridge实体可以让新块变得相关，却也暴露单向扫描的边界：早期被拒块不会因后来working state改变而自动重读，初期错误还可能在后续gate中自我强化。有限多跳QA支持带质量退步的成本取舍，不授latent保真或任意长context可靠；应保source块、encoder/adapter与gate版本、scan顺序、质量/预算和重新读取策略。压缩混淆实体、逆向依赖或阈值失准时回读raw块、重扫或保留无gate/原文本检索，派生working memory不能取得事实authority。

请求root实际Source及joint公式未披露边界裁决、actualowner/PRE后协调Ch77锁。
