# 01-16 标准单篇处置包

root已独立完整题摘准入，本文作者必要exact-v1审阅与拟处置，等待非作者实质复核，不等Books完成或日级Gate。所有已定Jan15新增candidate使用官方正常公告下界+各exactDOI公共存在上界，registered非first-public；直接原论文project轻量未见更早正文声明，非全网无早稿保证。

root已独立实际核ECOpt必要§4.1–4.3/5.3–5.4/6及Ch70 110–145/310–350，OnlyReport通过；FairToT必要§3.1.2–3.3/4.2–4.6/5.3–6及Ch66构念/truth边界，OnlyReport通过；Blackwell §3.4–3.9/Table4并复用前次质量/算术/Table15/limits核及Ch70实际比较，OnlyReport通过。保原5分/准入，TPS/User/32k冲突不删，不冒同实现Existing，不授全附件/实现复现；三篇通过不是DAY。

## ECOpt / 2601.08991v1 — 2+1+2=5，标准完成，拟仅报告

§4.1–4.3、§5.2–5.4.2、§6及Tables1–5实际读。CodeCarbon energy+quality双目标、Sobol→GP/qNEHVI是已知MOBO落地，贡献是局部proxy failure和摊销证据，而非新optimizer：CNN stride改变FLOPs不改params，简单MLP两者仍相关；NAS相关params−.12、FLOPs.26、runtime.79限制proxy。相同质量Gemma3L4优化batch其实single-energy objective，最佳batch831、2.67token/J、search18.61Wh/264.30s、4802token breakeven排除生产arrival/SLO。4models first1000BookCorpus、20wordprefix/10newtokens、无sampling/batching；OOM/CPU分页改变硬件差异，不能授跨硬件稳定排名。CodeCarbon CPU估计、GPU±5%和最高40%误差、cooling excluded；NAS不同训练预算/硬件与理论MAC对照不授SOTA或净收益。费用必须包括失败配置、train/eval与搜索，稳定固定配置直接测仍可共存。

已实际读Ch70 L110–144、L310–350，已有device/host/goal分账、profileidentity/代理失配与搜索费用，没有同qNEHVI实现；**不称Existing**，局部离线search/曲线还未提供值得写入的新稳定采用机制。日期`date08991.raw` registeredJan15T02:35:37Z，project ecopt README无更早paper release信号。

## FairToT / 2601.09250v1 — 2+1+2=5，标准完成，拟仅报告

§3.1–3.3、§4.1–4.5、Tables1–4/§5–6实际读。entity substitutions相对neutral prediction的敏感度做sentence-local variance与crosspopulationentity variance，加权风险触发3-stage再提示/ICL。global统计需要N样本×K实体，不是只看单query的无成本gate。Cθ=.25/风险.35来自验证选择；不同domain需重调。结果测prediction variance，不测分类correctness/AUROC，常数prediction也可低variance；实体差异正当含义与BT/AAV语义等价无独立认证。各template/temp/threshold非单调；deterministictemp不是普遍best。API/Llama3.1-8B/P10016GB设置、检测/再prompt/token费用都限定该toxicitypopulation。代价/语义/correctness独立门欠缺时保留原detector、人工规范/正确性检查，不把低variance签公平。

已读Ch66实际metric/scorer/规范分账上下文；**不称已有FairToT实现**。门本身有局部新实验，但仅variance风险不能为强correctivepolicy提供足够长期采用证据，拟仅报告。date09250 registeredJan15T02:41:41Z；project已读，未出现早正文声明。

## Consumer Blackwell / 2601.09527v1 — 2+1+2=5，标准完成，拟仅报告

§3.2–3.9、§4.1–4.7、§5及针对冲突AppendixA Tables15–18实际读。VAST.ai rentedbaremetal、vLLM0.12/CUDA12.9、AIPerf.3.0、GPU DCGM deviceonly、Qwen3/Gemma3/GPTOSS/W4A16/NVFP4/MXFP4、synthetic8k–64k RAG/c4–16、2k3LoRA/c16–64、shortAPIc32–256。MainTable4证明同Qwen3/NVFP4双5090 API-c64 TPS/TTFT/energy比single退；RAG容量/预算卡可反向benefit，故TP准入依workload而非自动两倍。

必要反侧：Table8 TPS/User与TPS/concurrency有明显算术错（888.8/16=55.55而57.5；410.6/64=6.42而19.5），**不照录TPS/User**；§4.6/4.7称dual5090RAG32k303TPS且<2s，与Table15实际147TPS/3116ms不符（303在16k）；只报原row不授headline。§4.5把agent2kvsAPI256不同输入的差额解释为非adapteroverhead，未固定输入adapterablation，故不能授3adaptercache消除切换费用。质量QwenNVFP4降约2pp；Gemma12B MMLU降4.07pp且GSM8K3.57pp；27B无BF16baseline、GPTOSS无pairedquality，不能全量精度保证。30Mtokens/day breakeven假设满量、GPU电费非全资源费、非等capabilitycloudAPI，不授40–200x/TCO/隐私/生产替代。

已实际读Ch70全费用/SLO/利用率分账与相邻段；本研究新局部measuredboundary值得保留但协议/核心算术与qualitypopulation不稳，不把它包装为新成本/硬件采用合同。**不称Existing**，OnlyReport拒绝强采用，不以降分逃争议；表/假设不一致明确保留。registeredJan15T02:48:07Z；论文链接repo README当前不出现更早论文正文信号。
