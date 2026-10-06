# 2025-10-03 必要核心与停止边界

作者Huygens。以下是实际有限阅读位置与判断，不是正面Evidence Gate或全论文/全附件审阅。20项必要安全/设计反侧核心与3项决定准入消歧共23篇精确v1；必要支持与反侧处理完一个命题即停。除RNG以PDF读取外，各身份使用同目录 `core-<ID>v1.raw` / `.text.txt`（HTML）；raw下载不证明已读。

| 精确v1 / 实际位置 | 能支持与不能支持的边界 |
| --- | --- |
| [2510.21740](https://arxiv.org/html/2510.21740v1) §3.1–3.2、§4.5–4.6 | 3968任务、768简单8×8散点图，三模型视觉linear probe可解坐标但LLM利用下降；不能证明绝对信息丢失。复杂图16–128点直接注入GT坐标反而下降，不是普遍修复 |
| [2510.02185](https://arxiv.org/html/2510.02185v1) §5.1、§5.4 | 1555函数、336/1311 OSS-Fuzz项目、Gemini2.5Pro、July–September；只捕获crash/noncrash，API成本是代理，小human对照不能外推所有误报 |
| [2510.01598](https://arxiv.org/pdf/2510.01598v1) §2.3–2.4、§4 | CIFAR10 GAN 10k 64×64，18.6×是class6图像LPIPS相似对；16MTJ100kHz实测1.6Mbit/s，Gbit是未来百万cell估计。没有等价LLM jailbreak实测；见[rng-pdf](rng-pdf.raw)与[实际PDF读取结果](day3rngpdf.json) |
| [2510.02194](https://arxiv.org/html/2510.02194v1) §3.1、Appendix A.2 | Qwen2.5/Llama3.1/R1distill；harm-only stage1、mixed stage2；GPT4o评分不是5即计safe，1–4伤害可能被计安全，不外推adaptive safety |
| [2510.02091](https://arxiv.org/html/2510.02091v1) §2、§3–4 | Qwen3 8B/Llama3.1 8B MMLU loglik与生成层消融；局部层角色不等所有模型depth无用定律 |
| [2510.01631](https://arxiv.org/html/2510.01631v1) §4.1–4.1.2、Limitations | 正文约600模型/70k GPUh与AB>1000/>100k不同；100M–3B、200B tokens、A10080GB、单Mistral7B生成器、n=1单轮预训练；8T是外推，未测code/dialog/safety/frontier |
| [2510.01569](https://arxiv.org/html/2510.01569v1) §4.1、Limitations、A.3 | SafetyBench11435、TRIDENT2652、insider100场景；teacher/judge均Gemini2.5Pro，SFT30007而RL20%子集；teacher知识与inverse结构收益未完全解耦 |
| [2510.01586](https://arxiv.org/html/2510.01586v1) §5.1 | 3agent拓扑、Qwen2.5 3/7B、三攻击集300；正文“4000 problems from MATH500”歧义保留，不替作者修数据。contagion轨迹不是仅终分 |
| [2510.01549](https://arxiv.org/html/2510.01549v1) §5.1、§6 | SD1.5/SDXL DDIM100×50优化；reward/quality不同，KL surrogate紧度与复杂OOD仍开放，不当reward提升等价质量 |
| [2510.01670](https://arxiv.org/html/2510.01670v1) §2.3、§3 | OSWorld90任务15步，o4mini intent judge2048；BGD意图不等实际完成危害。R1 a11y vs其余screenshots混杂；93.75%judge agreement有限子集 |
| [2510.02554](https://arxiv.org/html/2510.02554v1) §3.2–3.3、§4.1–4.2 | provider控制name/description而非schema，知工具DB与query；10轮PAIR、10任务5API、100queries/task；BSR是搜索最好结果，不是恶意动作完成率 |
| [2510.02418](https://arxiv.org/html/2510.02418v1) §4.1、§7 | 213responses/109battles/98users、5模型BrowserUse/OpenRouter；R1无图，BothBad偏好无法当成功。captcha220=20human+200synthetic；同框架排行非所有Agent能力 |
| [2510.01688](https://arxiv.org/html/2510.01688v1) §4.1、Limitations | 约8k/40医生、100profile韩语、Gemma3 4B/Qwen2.5 3B/GPT4.1mini；作者确作240样本、两位医学专家独立验证，报告Cohen kappa 0.8091、human/LLM Spearman 0.8129（p<0.0001），支持这个受限任务的评价一致性。相关性不证明广泛临床等价；Limitations仍指出医学预问诊范围、专家细微判断及跨领域外推限制。format惯性是局部失败机制，不作临床建议，不升级日期或正面Evidence |
| [2510.02230](https://arxiv.org/html/2510.02230v1) §4.1–4.2 | Qwen2.5Math1.5/7B、Llama3.2 3B、DeepScaleR40k、四bench；pass1升而pass256约300步后降，只保留样本覆盖反侧，不宣称无条件RL定理 |
| [2510.02204](https://arxiv.org/html/2510.02204v1) §4.1–4.2 | 三GUI模型、AITZ/CAGUI/AndroidControl、1800分层human样本；AgentCPM8B deterministic CoT判读与action EM不同。双expert仅保留同意/非NA，agreement有selection限制 |
| [2510.01642](https://arxiv.org/html/2510.01642v1) §III-C–D | 131k失败/56k成功、3ManiSkill任务、10frame3cam/LLaVAOV7B，replay2pose sanity；模拟恢复不等真实生产控制安全 |
| [2510.01539](https://arxiv.org/html/2510.01539v1) §4.1 | paired code/math hidden vs revealed abduction差距；未读理论假设，不宣称全OOD因果定理 |
| [2510.02209](https://arxiv.org/html/2510.02209v1) §3.1、§4.4 | 20DJIA、March3–June30/82天、32k上下文3seeds/buyhold；换JanApr与MayAug排序反转、后发布模型回顾交易存在历史知识泄漏，不当利润生产证明 |
| [2510.05154](https://arxiv.org/html/2510.05154v1) §3.1、§7 | 3000意见/4500标注/10问题、美国招募，主观比较相关中等<.4；majority/minority偏差不等所有judge失效，跨文化/主题有限 |
| [2510.01925](https://arxiv.org/html/2510.01925v1) §VI-C/D2、Appendix B | 不因survey标签排除新增实验。10模型混合official/32trial/100question的相关不具训练因果；6PRM×2policy MATH500 temp.7 beam4/MCTS4，ProcessBench排序不可靠预测下游选择，有具体评价盲区 |
| [2510.02483](https://arxiv.org/html/2510.02483v1) §1、§2.1–2.5（准入消歧） | architectural/forward/backward优化未给具体方法；8H200节点、1/2/16/32/64节点，3/30B Llama SlimPajama BF16/AdamW/ZeRO1/batch256。GPU能耗非facility；8GPU tokens2×与iteration6.44/2.38比例不同，未消除替代解释，不排除资源取舍潜力 |
| [2510.01609](https://arxiv.org/html/2510.01609v1) §III-C–D（准入消歧） | MLP softmax权重依state/recent performance、4agent加权排行与complexity三档cache/lightmodels；确有adaptive机制潜力，不按泛组合排除，未证生产LLM成本 |
| [2510.02292](https://arxiv.org/html/2510.02292v1) §3、§4.1–4.2（准入消歧） | hooks/SQLite接口之外，8模型intermediate/lastlayer双层MLP512 kfold/random label对照primitive concepts；测量表示差异潜力，不当自动机制因果解释 |

## 官方安全事件与传播事件

[OpenAI RBAC write-up](https://status.openai.com/incidents/01K6KAAN7WXN69E8JET8PYB0D5/write-up)：完整核心已读。PDT10/02 11:47–18:19事故（BJT10/03 02:47–09:19），backfill限制角色优先于既有Enterprise/Edu许可，同时Record选项可能意外开放；修配置后cache传播仍延迟，需要清除/失效处理。当前正文有多阶段backfill、gating/metrics建议，但没有正文published timestamp。页面内generic identified update `2025-10-02T19:32:00Z`在窗内；incident published_at `20:37:57.115Z`也在窗内，均不能证明后来write-up根因当时已公开。正文隔离，不进入Books，不把发生时间当公开时间。

[Google PASTA](google-collab.text.txt)：约7000rater interactions、30k模拟轨迹、SDXL/GeminiFlash候选、IQL四slates，real-only/synthetic-only不如混合与85%偏好是作者局部协议。旧2412.10419v1题摘已经描述EM/RL/slate/人工与模拟轨迹；本Blog没有辨识方法修订，不把新传播当新论文。artifact实际首次发布未证，不据AB的release措辞回填。

所有上述结果只保留“已读到这些命题与限制”的事实；没有候选日期准入/独立校准与Books正文比较，因此不声称Evidence完成、已有覆盖或无长期差额已被逐论文证明。
