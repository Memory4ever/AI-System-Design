# B第七组必要证据：10796 / 10809 / 10814 / 10815

四家族精确v1，准入校准和119日期交集有效结果复用；保守公开界见本日DATE说明。未核代码或复现。当前官方abs的10809窗外v2、PRISM窗外v3/v4没有明确withdraw/correction声明；PRISM v2 Submitted02/12T02:56:17Z仅为提交，不自动成为窗内public或重要修订，保留该字段，不采用后版本。10814/10815为v1。支持与直接反侧足够即止，以下待非作者必要证据/处置复核。

原始必要段：V3_BSEVENINITIAL、CORE0–3、TAIL0–3按标题次序；FIND0为必要证明/配置定位，FIND1为currentabs，EXTRA为PRISM谱/局部proxy假设。引用Source的L号是原web段，不是缓存物理行号。

## [10796 PRISM](https://arxiv.org/html/2602.10796v1)

5（2+1+2），标准；拟采用接口差额加深。§4以ShortConv得到只依赖已知input的u，模拟不可并行直接读S_(t−1)k的非线性写入；在该局部proxy上逐层GELU residual refinement，再把多分量outer-product注入B，与线性forget A分开。state-independent指A/B不消费中间recurrent state，不指网络无input条件或不用历史。rank(B)≤L，等号需分量独立；residual减δ不自动是正交化，β=Wβu也不是概率confidence，不采用任意rank-L语义正交保证。

§D谱结论首先要求β∈[0,1]、key norm≤1，但正交方向有特征值1；non-expansive不等严格fading或输入噪声总有界。D2/D3以固定invariant mode、unbiased log-normal扰动和衰减噪声方差≤Kγ²推累积variance，不是所有动态非正规transition的实际error范数保证。§E还假定标量γ∈(0,1)、ShortConv精确捕获最近w项、每项norm≤1，才有γ^(w+1)/(1−γ)尾界；不能从learnedShortConv名字推这些假设成立。G单步Lipschitz/预测gain有界也不证明多层全轨迹稳定；不将完整证明无误或普遍logT error写书。

Toy D16/V64/N128/10000steps与四recommendation任务是不同协议，不把recommendation分数当基础LLM验证。electronics的full vs L1组件反侧支持有限write refinement，其他组件并非每格大幅改善。0.13B/H20单卡throughput、2k–16k、FLA/materialized recurrence与TTT实现差异只局部kernel结果，短2k FlashAttention2仍更快；174×非同规模LLM端到端训练/serving提升。完整batch、precision、训练multi-seed/端到端成本/SLO未据披露建立，Not Disclosed，不采用宣传倍数。

拟Ch22差额：实际477–507已经明确input-conditioned affine scan、DeltaNet/GDN-2擦写分权和有损矩阵state，但尚未载“用local input proxy生成多分量非线性写入，同时transition保持state-independent”的并行接口选择。仅一段接口/一段proxy误差与cost/fallback；不移入谱强保证或吞吐数，Exact KV/原delta/hybrid共存。PRE前不写。原源CORE0 Source177–264；TAIL0 275–340；FIND0 540–618；EXTRA540–566/640–662。

## [10809 DeepImageSearch](https://arxiv.org/html/2602.10809v1)

5（2+1+2），标准。DISBench将相同外观放入用户context-dependent关系任务；YFCC个人history、57users/109467photos、从2000候选保留122query，均是筛选后任务人口，非一般图像检索召回率或真实个人全历史覆盖。人工以7annotators/IoU.91及三人adjudication核目标集合，retrieval-assisted标注不证明所有合格图片无遗漏。

ImageSeeker的metadata/view/web/memory流程不新增普遍可靠agent机制。原embedding-vs-agent比较改变了model、工具/context与预算，不能因低embedding recall证明独立编码有普适不可突破上限或把收益因果归给reasoning。same-backbone工具/记忆消融提供局部依赖：GeminiFlash36.8整体在去meta/filter/view/web/memory/compression后分别31.1/31.8/32.9/32.2/31.9/33.9，全部不认证语义可靠或context completeness；Best@k oracle F1不是可部署selector，手工选失败类型占比也不是人口因果。

D4每query freshstate、max30turns/128kcontext、search/view20条、GPT4omini压缩、各backbone default temperature，API与localvLLM混合；embedding独立MAP/Recall/NDCG@1/3/5/10与agentset EM/F1不直接拼同metric。hardware/precision/完整token/tool budget、重复run与不确定性/SLO ND。仅报告：保留context-dependent检索评价的局部盲点与筛选/工具预算混杂，未给能改变长期retriever或controller选择的受控因果/可靠性条件，不因新bench改写Books，也不称exactbench已有覆盖。原源CORE1 Source129–222；TAIL1 220–281；FIND0 479–497。

## [10814 Scratch GUI evaluation](https://arxiv.org/html/2602.10814v1)

5（2+1+2），标准。83tasks/四类及unit-test SR/partial SR，tests由LLM生成+人工refine，只覆盖声明测试而非程序完整语义verify。primitive screenshot/DOM-OCR/bbox/spatial action与composite API/pseudocode不只改变planning接口，还改变观测/actuator与visual feedback；78.31%vs14.46%跨framework不能作单因素视觉瓶颈因果。AgentS2与AWM关系随backbone变，也非通用AgentS2回归。

必要受控反侧是60个单drag atom、已知GT起点及另200个static perception任务：起点近100/end约30与primitive23.33支持有限endpoint放置问题，不证明所有GUI失败与planning无关或大模型无visuospatial能力。原webTables2/3部分cells为空，采用正文披露范围，不补空值。1280×720、Ubuntu22.04、双Xeon8280L/256GB/9RTX2080Ti为环境server，不等API模型inferencehardware；temperature搜索无匹配、各模型sampling/重复seeds/全tool预算/端到端成本ND。仅报告局部execution-granularity评价边界；新任务和接口变更未经相同观测/执行预算隔离，不为此构造普遍GUI系统瓶颈规则。原源CORE2 130–157；TAIL2 200–255；FIND0 temperature无披露。

## [10815 data-centric VLM post-training](https://arxiv.org/html/2602.10815v1)

6（2+2+2），具体评价反证受影响深入。当前初始化policy对每题G8/T.9/top-p1采样，allcorrect/allwrong归easy/hard、混合归medium；这不是题目内在或跨policy不变难度。组内二元reward全同使GRPO的reward advantage项为零，但βKL=.04时全objective梯度未必零；不能说RL自动完整删除该样本或一切RL只学medium。SFT仍对teacher答案CE，故data support/梯度人口与objective改变需要分别比较。

Qwen2.5VL3/7B先400初始化1epoch，ImageNet100类各100/RefCoco10k，LoRAr32α64/AdamWlr1e−5/B16；分subset mincount-balanced100steps。hard7B ID+7.08而ImageNetR−14.07，medium3B ImageNetR−1.38/Lisa−.12，难度组非所有OOD一致规律。full比较600steps下SFT B16 vsGRPO B128含8responses，与filter预采样虽作者纳入timing却不等total tokens/compute、相同support或KL；4.9×/3.2×不授跨配置成本保证。DC-EM RefCoco7B仍低GRPO，MiniCPM有ID退步。全参数Table5中3B ImageNetR SFT-M45.03<GRPO50.61，不写统一胜出。§6加入5%hard的同base干预与gradientnorm只支持这一data regime，norm不单独识别真实noise或证明因果语义来源。

§6.2 MMK12/GLM4.5生成6800verifiedpairs、400init/6400后训练，400steps，βKL.001，greedyT0/repetition1.1/max4096是另一reasoning协议；只multiplechoice且部分任务转换MC，不拼到分类/OOD成本。Table6两个base都标7B但正文第一段称3B，保留标注冲突，不用未确认规模签发性能事实。hardware/precision/训练seed不确定性、生产batch/SLO ND。

拟Ch29窄差额：actual651–655按difficulty分别验ID/OOD/extrapolation已承载一般原则；新增是difficulty来自初始policy采样分布、uniform outcome如何使group-relative reward项失活，而teacher CE仍保留这些样本，以及matched update≠matcheddata/token/compute。只解释data-support与algorithm attribution，不称curation替代RL/普遍难题无用，保留mixed/heldout原路径。必要原反侧已足够，不扩所有附录。原源CORE3 Source107–197；TAIL3 198–247。
