# 2026-02-18 第四批准入校准

八项有限主题线索；完整题摘已实际读 exact-v1，live DataCite ID/URL/title/v1 Submitted/Created逐项绑定且 Submitted > 2026-02-13T19:00Z、<= 2026-02-16T19:00Z。日期采用官方工作日公告下界与公开Created秒bucket+1s上界的交集工作推定，Updated非first-public。正文已抓取但并非必要方法审阅完成；current-version摘要差不静默进入v1。

## 2602.13427

[exact-v1](https://arxiv.org/html/2602.13427v1)；本地原文 V3_BODY_2602.13427.txt:75–81。

完整摘要：

Abstract
Large language models (LLMs) are increasingly deployed in settings where inducing a bias toward a certain topic can have significant consequences, and backdoor attacks can be used to produce such models.
Prior work on backdoor attacks has largely focused on a black-box threat model, with an adversary targeting the model builder’s LLM.
However, in the bias manipulation setting, the model builder themselves could be the adversary, warranting a white-box threat model where the attacker’s ability to poison, and manipulate the poisoned data is substantially increased.
Furthermore, despite growing research in semantically-triggered backdoors,
most studies have limited themselves to syntactically-triggered attacks.
Motivated by these limitations, we conduct an analysis consisting of over 1000 evaluations using higher poisoning ratios and greater data augmentation to gain a better understanding of the potential of syntactically- and semantically-triggered backdoor attacks in a white-box setting. In addition, we study whether two representative defense paradigms, model-intrinsic and model-extrinsic backdoor removal, are able to mitigate these attacks. Our analysis reveals numerous new findings. We discover that while both syntactically- and semantically-triggered attacks can effectively induce the target behaviour, and largely preserve utility, semantically-triggered attacks are generally more effective in inducing negative biases, while both backdoor types struggle with causing positive biases. Furthermore, while both defense types are able to mitigate these backdoors, they either result in a substantial drop in utility, or require high computational overhead.

作者准入理由：模型builder本身可能恶意、black-box毒化假设过弱 → white-box高毒化/语义触发偏向及removal代价反侧 → 限定bias防御的威胁权限与utility预算；不把更多评测次数当贡献。 拟 2+1+2=5，最低标准；安全/设计反侧只深入受影响命题。待root准入校准与必要源审阅。

## 2602.13477

[exact-v1](https://arxiv.org/html/2602.13477v1)；本地原文 V3_BODY_2602.13477.txt:74–75。

完整摘要：

Abstract
As Large Language Model (LLM) agents become more capable, their coordinated use in the form of multi-agent systems is on the rise. Prior work has examined the safety and misuse risks associated with agents. However, much of this has focused on the single-agent case and/or setups that lack basic engineering safeguards such as access control, revealing a scarcity of threat modeling in multi-agent systems. We investigate the security vulnerabilities of a popular industry multi-agent pattern known as the orchestrator setup, in which a central agent decomposes and delegates tasks to specialized agents. Through red-teaming a concrete setup representative of industry use, we demonstrate a novel attack vector, OMNI-LEAK, that compromises several agents to leak sensitive data through a single indirect prompt injection, even in the presence of data access control . We report the susceptibility of frontier models to different categories of attacks, finding that both reasoning and non-reasoning models are vulnerable, even when the attacker lacks insider knowledge of the implementation details. Our work highlights the failure of safety research to generalize from single-agent to multi-agent settings, indicating the serious risks of real-world privacy breaches and financial loss.

作者准入理由：单agent ACL不自动覆盖中央delegation → 一个间接注入沿多agent传递且访问控制仍在 → 核数据读取权限与可外传权限是否被混为一层。 拟 2+2+2=6，最低标准；安全/设计反侧只深入受影响命题。待root准入校准与必要源审阅。

## 2602.13516

[exact-v1](https://arxiv.org/html/2602.13516v1)；本地原文 V3_BODY_2602.13516.txt:57–58。

完整摘要：

Abstract
LLM-powered agents are beginning to automate user’s tasks across the open web, often with access to user resources such as emails and calendars. Unlike standard LLMs answering questions in a controlled ChatBot setting, web agents act “in the wild”, interacting with third parties and leaving behind an action trace. Therefore, we ask the question: how do web agents handle user resources when accomplishing tasks on their behalf across live websites? In this paper, we formalize Natural Agentic Oversharing —the unintentional disclosure of task-irrelevant user information through an agent trace of actions on the web. We introduce SPILLage , a framework that characterizes oversharing along two dimensions: channel (content vs. behavior) and directness (explicit vs. implicit). This taxonomy reveals a critical blind spot: while prior work focuses on text leakage, web agents also overshare behaviorally through clicks, scrolls, and navigation patterns that can be monitored. We benchmark 180 tasks on live e-commerce sites with ground-truth annotations separating task-relevant from task-irrelevant attributes. Across 1,080 runs spanning two agentic frameworks and three backbone LLMs, we demonstrate that oversharing is pervasive with behavioral oversharing dominates content oversharing by 5 × 5\times . This effect persists—and can even worsen—under prompt-level mitigation. However, removing task-irrelevant information before execution improves task success by up to 17.9%, demonstrating that reducing oversharing improves task success. Our findings underscore that protecting privacy in web agents is a fundamental challenge, requiring a broader view of “output” that accounts for what agents do on the web, not just what they type. Our datasets and code are available at https://github.com/jrohsc/SPILLage .

作者准入理由：把泄漏只看输出文本 → click/scroll/navigation也可外显task-irrelevant偏好且prompt mitigation反退 → 重新定义动作trace隐私边界并核输入最小化代价。 拟 2+2+2=6，最低标准；安全/设计反侧只深入受影响命题。待root准入校准与必要源审阅。

## 2602.14211

[exact-v1](https://arxiv.org/html/2602.14211v1)；本地原文 V3_BODY_2602.14211.txt:58–61。

完整摘要：

Abstract
Agent skills are becoming a core abstraction in coding agents, packaging long-form instructions and auxiliary scripts to extend tool-augmented behaviors. This abstraction introduces an under-measured attack surface: skill-based prompt injection, where poisoned skills can steer agents away from user intent and safety policies. In practice, naive injections often fail because the malicious intent is too explicit or drifts too far from the original skill, leading agents to ignore or refuse them; existing attacks are also largely hand-crafted.
We propose the first automated framework for stealthy prompt injection tailored to agent skills. The framework forms a closed loop with three agents: an Attack Agent that synthesizes injection skills under explicit stealth constraints, a Code Agent that executes tasks using the injected skills in a realistic tool environment, and an Evaluate Agent that logs action traces (e.g., tool calls and file operations) and verifies whether targeted malicious behaviors occurred. We also propose a malicious payload hiding strategy that
conceals adversarial operations in auxiliary scripts while injecting optimized inducement prompts to trigger tool execution. Extensive experiments across diverse coding-agent settings and real-world software engineering tasks show that our method consistently achieves high attack success rates under realistic settings.

作者准入理由：可复用skill的辅助脚本看似可信setup → 明确约束下诱导文本触发隐藏payload并由真实trace验证 → 核skill文本/脚本的权限桥，不把自动多agent搜索本身叫安全机制。 拟 2+2+2=6，最低标准；安全/设计反侧只深入受影响命题。待root准入校准与必要源审阅。

## 2602.13515

[exact-v1](https://arxiv.org/html/2602.13515v1)；本地原文 V3_BODY_2602.13515.txt:64–67。

完整摘要：

Abstract
Many training-free sparse attention methods are effective for accelerating diffusion models. Recently, several works suggest that making sparse attention trainable can further increase sparsity while preserving generation quality.
We study three key questions: (1) when do the two common masking rules, i.e., Top-k and Top-p, fail, and how can we avoid these failures? (2) why can trainable sparse attention reach higher sparsity than training-free methods? (3) what are the limitations of fine-tuning sparse attention using the diffusion loss, and how can we address them?
Based on this analysis, we propose SpargeAttention2, a trainable sparse attention method that achieves high sparsity without degrading generation quality. SpargeAttention2 includes (i) a hybrid masking rule that combines Top-k and Top-p for more robust masking at high sparsity, (ii) an efficient trainable sparse attention implementation, and (iii) a distillation-inspired fine-tuning objective to better preserve generation quality during fine-tuning using sparse attention. Experiments on video diffusion models show that SpargeAttention2 reaches 95 % 95\% attention sparsity and a 16.2 × 16.2\times attention speedup while maintaining generation quality, consistently outperforming prior sparse attention methods.

作者准入理由：固定top-k/p在高稀疏不稳定、diffusion loss微调不一定保真 → hybrid mask与teacher distillation受控纠正 → 选择训练式稀疏路由的质量/训练/执行成本。 拟 2+2+2=6，最低标准；安全/设计反侧只深入受影响命题。待root准入校准与必要源审阅。

## 2602.13680

[exact-v1](https://arxiv.org/html/2602.13680v1)；本地原文 V3_BODY_2602.13680.txt:57–58。

完整摘要：

Abstract
Large Language Models (LLMs) encounter significant performance bottlenecks in long-sequence tasks due to the computational complexity and memory overhead inherent in the self-attention mechanism. To address these challenges, we introduce AllMem , a novel and efficient hybrid architecture that integrates Sliding Window Attention (SWA) with non-linear Test-Time Training (TTT) memory networks. AllMem enables models to effectively scale to ultra-long contexts while mitigating catastrophic forgetting. This approach not only overcomes the representation constraints typical of linear memory models but also significantly reduces the computational and memory footprint during long-sequence inference. Furthermore, we implement a Memory-Efficient Fine-Tuning strategy to replace standard attention layers in pre-trained models with memory-augmented sliding window layers. This framework facilitates the efficient transformation of any off-the-shelf pre-trained LLM into an AllMem -based architecture. Empirical evaluations confirm that our 4k window model achieves near-lossless performance on 37k LongBench with a marginal 0.83 drop compared to full attention. Furthermore, on InfiniteBench at a 128k context, our 8k window variant outperforms full attention, which validates the effectiveness of our parameterized memory in mitigating noise and maintaining robust long-range modeling without the prohibitive costs of global attention.

作者准入理由：全历史attention昂贵、纯线性memory表示受限 → SWA保local精确信息/nonlinear TTT容量并有预训练层替换路线 → 核低memory分支能保什么远程信息与迁移训练费用。 拟 2+2+2=6，最低标准；安全/设计反侧只深入受影响命题。待root准入校准与必要源审阅。

## 2602.14209

[exact-v1](https://arxiv.org/html/2602.14209v1)；本地原文 V3_BODY_2602.14209.txt:73–81。

完整摘要：

Abstract
Block diffusion LLMs are emerging as a promising next paradigm for language generation, but their use of KV caching makes memory access a dominant bottleneck in long-context settings.
While dynamic sparse attention has been actively explored, existing methods designed for autoregressive LLMs rely on approximate importance estimation and perform poorly when adapted to block diffusion.
This work identifies a key opportunity unique to block diffusion: attention at the first All- [MASK] denoising step reliably predicts important KV entries and budget requirements, enabling MAGE to perform a single exact attention pass per block and reuse it for training-free sparse denoising.
Across long-context benchmarks including LongBench and Needle-in-a-Haystack, MAGE achieves near-lossless accuracy with a fraction of the KV budget while delivering up to 3 3 – 4 × 4\times end-to-end speedup, consistently outperforming AR-oriented sparse attention baselines.
A lightweight fine-tuning strategy further strengthens
[MASK]-guided patterns with minimal cost, requiring only a few hours of training on a single NVIDIA H100 GPU for
both 1.5B and 7B models.
Keywords:

作者准入理由：AR KV估计不能直接移到block diffusion → first all-MASK exact attention一次探测并复用该block后续step索引 → 核trajectory内cache稳定条件与E2E开销；不移用后来6.82x摘要。 拟 2+2+2=6，最低标准；安全/设计反侧只深入受影响命题。待root准入校准与必要源审阅。

## 2602.14262

[exact-v1](https://arxiv.org/html/2602.14262v1)；本地原文 V3_BODY_2602.14262.txt:36–37。

完整摘要：

Abstract
We present a tightly integrated, unified near-memory GPU architecture, delivering 6–16× speedups and 6–13× energy savings across Convolutional Neural Networks, Graph Convolutional Networks, Linear Programming, Large Language models, and Ising workloads over MIAOW GPU. Features include a custom sparsity-aware near-memory circuit ( ∼ \sim 1.5× energy savings), a custom lightweight softmax circuit ( ∼ \sim 1.6× energy savings), reconfigurable compute up to INT16 with dynamic resolution update, and scalable across problem sizes. ABI enabled MI300/Blackwell yields ∼ \sim 4.5× speedup over baseline MI300/Blackwell

作者准入理由：RF/cache→ALU数据搬运能耗 → near-register/cache可重配bit/element模式与softmax近似电路 → 核LLM下精度/面积/带宽预算和simulation权限，不能当已部署Blackwell改造。 拟 2+2+2=6，最低标准；安全/设计反侧只深入受影响命题。待root准入校准与必要源审阅。

