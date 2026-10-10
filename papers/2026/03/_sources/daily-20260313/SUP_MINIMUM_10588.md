# 10588 exact-v1：最低投入关闭提案（非贡献EX）

Does LLM Alignment Really Need Diversity? An Empirical Study of Adapting RLVR Methods for Moral Reasoning。此前完整v1题摘、窄贡献与DATE3日级Mar12独核有效，不撤销潜力准入。九作者，SubmittedMar11T09:45:30Z/registeredMar12T02:05:10Z，Updated不是依据；当前v1 history无具名venue/withdraw/correction。

官方 https://arxiv.org/html/2603.10588v1 ，SUP_CORE_10588.raw/txt与SUP_CORE_10588_10592_MANIFEST_RESULT保存GET200/189703bytes/UTC2026-10-10T02:20:54.881641。实际读§3 Eq1–3必要目标、§4.1–4.2全部setup/构造、Table1完整两模型/Public+Theory/Score@1与Avg@8、§4.3相关解释/semantic选择与§4.4/§5边界（txt420–1020）；第一次组合输出末尾截断未认证Table2全部response，后来只读必要990–1020及§3，不要求所有案例/像素。未复现/代码/全references。

实际新增是同一MoReBench reward construction下，DAPO等与FlowRL局部比较反对“moral标签天然需要distribution matching”；不是新RLVR/GRPO、rubric加权或训练judge方法。拟 **2+1+1=4，已关闭/不进一步采用，Books仅报告0**：有限训练方案取舍证据2，单policy优化组件1，双模型单benchmark且参数/预算资格未闭合只版本相关价值1。不是主题EX、争议删候选或已有覆盖新实验；不因费用或未读降分，最低证据已足以支持不采用更强长期命题。

Qwen2.5-7B-Base/Llama3.1-8B-Instruct；local Qwen3-1.7B judge由多模型候选+GPT5 rubrics标签SFT。GPT5 agreement Public87.07%/Theory69.21%不是human价值真值；正/负rubric分别归一后相减，不认证多观点/少数人偏好，judge制备/全部rollout/评分/训练费用仍有。硬件/precision/batch/steps/训练与生成预算、KL/FlowRL temperature具体配置、seed/CI/test、数据拆分/判别器训练样本数 Not Disclosed，不能称已等资源或统计“不显著”。

Table1 DAPO QwenPublic@1/.Avg8 .67/.67与Flow .60/.61，Theory .76/.72 vs .65/.65；LlamaPublic .69/.72 vs .61/.60，Theory .74/.76 vs .72/.70，局部正侧成立。Flow也高于PPO/GRPO，不能把全部mode-seeking都更优；正文“rankings highly consistent”与Public QwenRFPP .65/.65高于Flow不符，保原行，不泛化算法属性。正文gain/Score1/Avg8一处混述，用Table1原值不补造算术。

另Eq1 reward-minus-KL与Eq3 reverseKL到exp(beta r)/Z并非天然互斥的数学目标族：固定reward/reference合适时KL展开含−beta E[r]+KL项，Eq3未含reference且实际估计器/预算不同，所以不擅宣布本文每配置相同算法；只不授标签本身普遍mode seeking vs coverage定理。该解释不新增评分成熟KL原则。

§4.3每题500高reward响应、all-MiniLM-L6-v2→t-SNE，六展示case聚类不是真实道德支持拓扑/普遍unimodality，更非representation/selection唯一因果；未看图像或补造cluster数。§5作者自己限定reward定义/engineering、fewbench、onlyFlowRL，保原有限负侧。Score@1/Avg@8不是coverage或多数/少数价值指标。

只记录当前局部comparison/选择资格，不进一步Books或请求更广义道德证明。root非准备者实际必要主文/完整Table1及六case选择核通过，独立校准为1+1+2=4：局部recipe D1/单组件R1/可复用配置D2。上方原2+1+1提案留作判断变更记录；单benchmark/未披露seed属于证据边界，不能作为Durability扣分。正式最低关闭/仅报告Books0，不授DAY；原准入/date保留。未来本ID修订给独立population/可比预算与实际diversity验证再重开对应命题，不构造外部材料阻塞或全历史请求。
