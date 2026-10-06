# 首批核心证据（作者待非作者复核）
所有路径均本日；精确v1完整AB：feb11_calibration_exact_AB.json；完整原文清洁文本：feb11_core_calibration_raw.json。以下拟采用命题按必要章节读足，不声称复现。

## 07306 Parallel Track Transformers
准入链：每层TP同步昂贵→track在D层后统一同步→需要联合选择预训练架构、同步频率与质量，不能只换serving参数。新增命题评分2+2+2=6（底层PT已在2025 Apple Foundation Models公开，本文有新的dense/PT+D矩阵与运行测量；不是把旧架构重新计突破）。
证据§2，§3 Tables1-4：8tracks，D2/4/8；6B800Btoken，13/30B400Btoken等规模各自same recipe。6B MMLU dense .560→D8 .360，GSM8K .317→.271；30B也非无损(.630→.615 MMLU，.523→.488 GSM8K)。30B8xH100 vLLM maxbatch256吞吐，maxbatch1latency；1024input4096output throughput 5990.98→5596.01(D8)回退，而4096/128 865.2→1141.18。TensorRT variant internally implementsPT，publicopensource不支持。precision/version/SLO/concurrency未披露。采用有限同步-质量-运行点权衡，不采用全面throughput改善或无损drop-in；Books待复核后比较owner。

## 07213 Adaptive Retrieval
评分2+1+2=5，但设计反证深入受影响内容。§3-4，AppA.1/A.2：Llama3.1-8B-Instruct fp16 T0 max1024，GSM/MATH，staticCoT/adaptive提示不同；bge-m3检索200→5，正文与appendix reranker描述crossencoder/ColBERT不完全一致。CoT82.1/44.2，static75.8/42.4，adaptive83.2/50.6是作者结果。retrieval仅7%GSM/38.8%MATH，MATH难度1→5检索率14→60.4%；retrieved子群25help25hurt，未检索子群63.7不证明“禁检索造成更好”。无同题随机干预、token预算对齐或CI。采用检索闸门强烈选择偏差+静态上下文非普遍正益；不采用 causal RAG failure/普遍不检索策略。预计仅报告，因为反侧归因未定。

## 07729 SGD RLVR
评分3+2+3=8，深入§3-7+AppA.1/B/C/D相关配置。Qwen3 1.7/8B、Llama3.1-8B，数学/代码/合成RLVE，GRPO及PPO；4x96GB GH200，verl/FSDP bf16，batch256 prompt1024。Adam1e-6，SGD .1(小PPO .01)，有SGD/momentum/RMSProp ratesweep，不能比较同nominalLR。SGD有些workload匹配/更好但Qwen1.7B8K56.8<Adam58.2；RLVE5008K56.5<57.1，16K63<64.5，无seed CI。状态口径Adam FP32master+m+v=12p bytes，SGD master=4p，1.7B理论13.6GB states、peak作者15.7GB含FSDP buffer。所谓更新稀疏依赖1e-5阈值和bf16，§7明确rounding/小梯度，不是所有真实梯度本征0。采用phase-specific optimizer评估与state memory，非SGD普遍胜/所有adaptive obsolete。Books待owner实际比较。

## 08923 DynamiQ
评分2+2+3=7。§3.1-3.4/§4/§5.1-5.3/§6.1-6.2以及AppB相关topology heuristic：metadata allreduce→groupnorm/budget分配→2/4/8bit streams，hop decompress-accumulate-recompress，不在低比特整数空间直接累加；sharedrandom negativecorrelation借用已有方法，kernel fusion缓解额外HBM访问。默认group16/supergroup256/UINT8 group scale/BF16 super-scale/avg5bits。4servers8GPU（原文RTX A6000 ada48GB/NV4，保留原称不擅自改）、100GbEthernet；BERTlarge/Gemma1B/Llama1B fine-tune，batch1或4。低比特MX4/6不native，报告compute-free等流量的bestcase lower-bound TTA，不是实际执行benchmark；THC4bit local8bit accumulate避免overflow，OR union适配不原生。§5实际ring/butterfly4worker，§6 TinyBERT到64worker是simulation。5bit优于3/4bit不是压缩率越高越好，ring/butterfly误差差异受partial sum大小；AppB O(n^3)/O(n^2)是有boundedsame-distribution intuition的heuristic upper bound，不runtime扩容证明。不开源实现不阻断论文限定命题，但不声称artifact复现或生产可用。

## 08695 Noise Generalization Trap
评分3+1+3=7。§3-5：uniformrandominputs的iid bitflips、无labelnoise；sparseparity/oddmajority成功，3200randomkjunta因cleanf和Bayes-noisy f*N目标不同导致有near-opt noisy loss仍cleanerror。Prop2是随机布尔函数期望sensitivity不是所有function定律。直接中心冲突：AB称penalizing HIGH sensitivity，正文使用 -lambda I[fhat]、明确encourage higher sensitivity以逃离simpler trap，图注还有歧义。因此只采objective target mismatch/shortcut反侧，不采罚项recipe。evenmajority大noise目标gap大，罚项也失败；高bitnoise synthetic未证明自然LLM任务。Books判定须保留这种有限反例，不能机械排除理论。

## 07359 Width&Depth
拟评分2+2+2=6；最小core准入事实：§3 GPT5Medium同BrowseComp first100/same工具base/100turn上限，width1accuracy66/avg45.7turn/$102.5totalAPI/1522.6s vs width3accuracy68/23.8turn/$65.7/904.2s。不是matchedtotalcalls/tokens；不作因果效率定律。width8在max100turn仅63<width3 68；§5同限制 scheduler constant3 68 vs descending3→2→1 74、ascending63，但多数在首阶段就停，不宣称严格同cost scheduler。采用作者端到端API成本/latency观察及width非单调条件；fullBrowseComp62.2 vs GPT5High54.9不比较。无CI，BrowseComp first100/HLEfirst100受作者cost裁剪，GAIA103textonly。请求root确认该core是否达到准入，而非因成熟parallel机制/排行榜收录。

日期：六篇v1 Submitted均Fri06 19UTC到Mon09 19UTC，官方公告policy最早2026-02-10T01:00Z（Beijing09）。final-ID DataCite registered最晚04:22..05:03Z；字段仅上界、不是actualpublictime。日期包络原值已保存feb11_dates1.json；07306 prior PT机制是2025 June9独立公告及July17正文2507.13575，并非2602.07306同一正文，新增claim仍限于本文新对照。
