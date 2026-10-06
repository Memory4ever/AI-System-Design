# 2025-09-26 必要精确版本证据边界

作者 Archimedes；实际读取发生于 2026-10-06。本文按当前研究合同 §3–5 保存定点安全/反侧阅读，不授日期准入、评分或 Books 采用。原始 HTML 为同目录 `<ID>v1.html`，可审文本块为 `<ID>v1-blocks.json`；块号是该派生数组的零起点位置，不替代原论文节号。抓取记录见 [necessary-v1-fetch.json](./necessary-v1-fetch.json)。只读下列必要内容，未核验实现、未复现实验，不称全文读完。

| 精确版本 | 实际证据位置 | 可支持与不可支持 |
| --- | --- | --- |
| [2509.20461v1](https://arxiv.org/html/2509.20461v1) | §3 Eq.7–11、定理假设，§6；块45–62、136–140 | Conformal extractive summary 的句子重要性覆盖依赖 exchangeability、标注与分数条件；不是抽象式生成的临床正确性保证。实证仅两类真实数据及派生数据，长文/段落扩展未得到同等验证。 |
| [2509.20639v1](https://arxiv.org/html/2509.20639v1) | §IV；块129–160 | guardrail 的签名规则与 ML release 可分离，冻结版本、shadow 对照和 FP/recall/flag delta gate 提供具体更新路径；厂商架构说明不证明零日免疫或独立生产事故率。 |
| [2509.20680v1](https://arxiv.org/html/2509.20680v1) | §3、§5及限制；块27–50、127–167 | 恶意 FL client 只需看到跨轮 global model，不需读取其他 client 私有模型；跨轮 logit 差可增强抽取。零先验与已知前80%文本两种攻击合同不同；ROUGE-L/BERTScore 是代理。DP/noise、LoRA、KL 等缓解有效用/泄露取舍，研究仅 fine-tuning，不扩到全部 FL/pretraining/RLHF。 |
| [2509.20792v1](https://arxiv.org/html/2509.20792v1) | §3–4、Table1；块28–60 | FOSC early-stop PGD curriculum 与 TRADES/cosine clean-adv objective 是实际机制；四个 CLIP 分类、4-shot、PGD 条件下的收益不能变成所有攻击保证。UCF clean accuracy 80.44→71.85 的损失保留，不能照录“无显著 clean 损失”。 |
| [2509.20838v1](https://arxiv.org/html/2509.20838v1) | §2、§4、§7；块22、43–44、133、146 | 本地改写依赖用户给定隐私 span，测试也假设 span 已知；3.07% token reconstruction 不是语义隐私概率，隐式线索和域外提示仍可能泄露。成本附录仅定位到标题，不声称其成本实测已核。 |
| [2509.20977v1](https://arxiv.org/html/2509.20977v1) | §3、§5及限制；块43–45、58–60、149 | CLUE 用 CNF/SAT 约束 preserve/forget/conflict neurons，区别于直接遮蔽；WMDP、SafeRLHF及指定 retain tests 仅局部证据。多目标冲突与实际 fine-tuned forgetting 不由静态 circuit 成功自动保证；未逐步验 SAT 证明。 |
| [2509.20998v1](https://arxiv.org/html/2509.20998v1) | §2–3、§5；块29–63、89–105 | CORE 用人工核的 DFA/gold path 区分终态正确与执行路径；删除保持状态的读取但保留有害尝试，PC/PC-KTC 与 HarmFree/PrefixCrit 各有定义。14 个合成 world、平均10 tasks 与有限模型不证明真实生产安全；BFCL legal slice 的 State100% 与 PC0.408、平均3.1有害动作是具体评价反例。 |
| [2509.21011v1](https://arxiv.org/html/2509.21011v1) | §III–V；块28–30、39、41、45、49、59、68、92、106、109–110 | AutoMalTool 攻击 MCP package 描述，目标是参数/结果解释，不只是工具选择；搜索与模拟由 LLM oracle/evaluator 参与。3 servers/53 tools、筛选后247+117+130 tasks、有限优化迭代只支持两类攻击；不证明 exfiltration、shadowing 等全部风险或真实部署率。 |
| [2509.21029v1](https://arxiv.org/html/2509.21029v1) | §3–4及限制；块43–45、86–89、91、93、134、136 | FORCE 对 feature/frequency over-reliance 的攻击有具体归因对象；source LLaVA1.5-7B、32/255 perturbation、2/255 step、0/100-query budget 必须绑定。8 targets及商业模型100/100/20子集、substring/HarmBench judges不构成普遍攻击率。相对70%不是70个百分点。 |
| [2509.21054v1](https://arxiv.org/html/2509.21054v1) | 精确v1题目、§3及 mitigation；块4、38–39、60–65、85–87、98–99 | v1为 *Disagreements in Reasoning: How a Model's Thinking Process Dictates Persuasion in Multi-Agent Systems*，不是最新v3 *Reasoning or Rambling*。MMLU与主观任务的 target 设定、thinking mode 与长度条件可读；未独立隔离语义 padding 的因果，不借后版新命题倒填首版。 |
| [2509.21155v1](https://arxiv.org/html/2509.21155v1) | §2、§4、§6、§8；块4、30–32、75–79、111–132 | syntactic-domain 偏移的 semantic-preserving/breaking 区别是潜力；方法需知道训练数据域。OLMo2-7B/1000 WildJailbreak 的 refusal40→2.5%不能视为同量 harmful success；GPT4o-mini 的 Flan 来源假设与推测保留，未验证 reasoning/CoT-trained 条件。 |
| [2509.21173v1](https://arxiv.org/html/2509.21173v1) | v1题目、§3–4与限制；块32、34、57、60–61、67、90–96、111–113 | v1标题限定 CLIP，不借v6泛化为全部VLM。仅量化 visual encoder、WIT/LAION、CC3M proxy、fake quant/QAT/PTQ。4-bit collapse、校准在不同pretraining来源上反转、复杂ImageNet-R/A与CounterAnimals伪相关退化均保留；8-bit局部改善不是普遍可靠性收益。未核真实kernel运行成本。 |
| [2509.21192v1](https://arxiv.org/html/2509.21192v1) | 方法、实验与限制；块23、25、27、29、35–39、48–49、86 | GEP用 BioGPT 健康聊天、100k中插入1000合成姓名/症状、已知姓名+whitebox GCG trigger；disease-string match 是代理，freestyle也针对相同条目。不能把它称为未知真实PII的通用恢复率，数据不均衡与trigger可过滤保留。 |
| [2509.21008v1](https://arxiv.org/html/2509.21008v1) | 方法、实验、攻击及限制；块69–70、76–77、85–90、110、120 | SNCE是SD1.4的单SAE top-k text-embedding干预；NudeNet阈值0.6与adversarial0.45、CS/FID3k有不同评价身份。P4D仍ASR42.6%、Ringbell6.32%，因此不采用“阻止有害生成”的保证。 |
| [2509.21243v1](https://arxiv.org/html/2509.21243v1) | 方法、配置、实验与限制；块28、42–52、76–77、99、104–105 | RetoVLA 创建learnable register queries与gated K/V，不是免费复用现有register；500M SmolVLM2、16layers、100ksteps、batch64、2registers的条件保留。全局gate不自动是每请求动态策略；精细任务取舍与大型模型/动态环境未验证，不外推实机平均50.28→67.42%。 |
| [2509.21268v1](https://arxiv.org/html/2509.21268v1) | §3–4、§7、AppendixA.4；块17–28、47–52、59–63、111–112、138、200–203 | MMR1的OVS p(1-p)+TDS、uniform mixture/周期重评分是实际采样机制，增加评估成本。理论先假设 gradient-norm²≥c_min reward variance；A.4仅说明whitening/importance ratio/clipping后常数重缩放及O(ε)bias，未给独立可用的任意token-GRPO保证。保留局部采样潜力，不采用“更高reward variance必然更大GRPO进步”。 |

## 表外必要机制

[LMSYS GB200 PartII](https://lmsys.org/blog/2025-09-25-gb200-part-2/) 的 Methods、Experiments、precision comparison、Future Work 已实际读，原文见 [lmsys.html](./lmsys.html)，可读抽取见 [lmsys.html.text.json](./lmsys.html.text.json)。FP8 KV与NVFP4 weights/dispatch共同改变memory/batch/EP规模，host offload在紧耦合CPU-GPU带宽下可缩小prefill EP；combine overlap还涉及TMA store wait与release signaling。它不是仅把H100换GB200的倍率贡献。

但端到端对照的kernel/strategy、EP balance、batch均不同，作者明示非纯precision ablation；4k ISL batch768、2k batch1408，后者降到768约慢10%。early-access CuTe DSL bugfix当时未公开，MTP overlap仍是未来工作。本文不授实现核验、可复现性或通用SLO。原Blog只有 `September 25, 2025` 无时区，日期依赖仍隔离。

## 日期与权限

以上 arXiv 精确v1不因提交字段而获得first-public。官方availability页实际读到moderation可延迟1–4天或更长，因此不能把deadline schedule套成逐篇公开日期；原页保存在 [arxiv-availability.html](./arxiv-availability.html)。恢复逐篇官方公告或原作者公开正文的完全落窗边界后，只重开该家族。上述必要反侧即使暂不进入候选也保留，不通过降分、删反证或改名关闭潜力。
