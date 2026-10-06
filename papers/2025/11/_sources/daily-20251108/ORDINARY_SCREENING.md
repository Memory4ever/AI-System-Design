# 2025-11-08 普通题摘停点

首批六v1及Google核心说明见[FIRST_CALIBRATION](./FIRST_CALIBRATION.md)。以下新增13篇完整题摘已实际读，原始summary在[收窄formation原响应](./arxiv-formation-narrow-page0.xml)，不是全53条已筛完。标题明确领域应用仅浏览范围，未把114宽表翻页或逐项全文化。

| ID / 完整标题 | 当前有限判断 |
| --- | --- |
| 2511.03808v1 / Optimizing Reasoning Efficiency through Prompt Difficulty Prediction | 潜在：内部表示轻量difficulty/correctness predictor路由最小可解模型，改变质量成本路由；不采用无条件无损；NeurIPS workshop公开身份待核。 |
| 2511.03823v1 / PLLuM: A Family of Polish Large Language Models | [必要§9/10.5已读](./nov08-pllum-necessary-body.txt)：同步可repair/revalidate；流式已交付前段不可回收，禁自动修复并中止。另有跨语言/语料构造安全评价局部反证，表32 instruct与chat差异及正文全模型概括不一致。保留具体机制/反侧待root校准，不采区域数据规模或合规保证，见[新增校准](./SECOND_CALIBRATION.md)；public原日期未核，不继续全附件。 |
| 2511.03825v1 / How Different Tokenization Algorithms Impact LLMs and Transformer Models for Binary Code Analysis | 潜在局部负证据：assembly tokenizer intrinsic效率/压缩/representational fidelity只能部分预测downstream表现，不因binary应用自动排除。BAR2025同家族早公开身份待核，不把Nov submitted当public。 |
| 2511.03830v1 / Divide, Cache, Conquer: Dichotomic Prompting for Efficient Multi-Label LLM-Based Classification | 潜在：多标签结构输出改成逐维yes/no，结合prefix共享改变短请求预算/准确率取舍。需分离24维任务性质、cache命中和蒸馏训练贡献，不把应用得分当缓存新机制。 |
| 2511.03983v1 / TwIST: Rigging the Lottery in Transformers with Independent Subnetwork Training | 潜在：并行subnetwork周期参数合并/重新采样形成可部署结构dense子矩阵；部署免恢复不是训练零成本。 |
| 2511.04000v1 / Towards Scalable Meta-Learning of near-optimal Interpretable Models via Synthetic Model Generations | 潜在：synthetic near-optimal树训练MetaTree改变真实/精确optimal树预训练预算条件，是一般学习方法，不因finance/health示例排除。 |
| 2511.04132v1 / Exploring the Feasibility of End-to-End Large Language Model as a Compiler | 潜在局部负证据：CompilerEval汇编生成低成功率/错误类型与prompt/model/reasoning效应，不能因标题系统比喻自动采用；需只核该评价失效差额，IJCNN2025可能早公开。 |
| 2511.04217v1 / The Strong Lottery Ticket Hypothesis for Multi-Head Attention Mechanisms | 潜在理论：随机MHA隐藏维O(d log(H d^1.5))高概率近似及无normalization Transformer扩展；需假设，不机械索取LLM规模bench，不外推有norm生产模型。 |
| 2511.04234v1 / Reusing Pre-Training Data at Test Time is a Compute Multiplier | 潜在评价反证：去contamination后同预训练语料检索仍提高MMLU/Math500/SimpleQA，反映参数吸收与可检索利用差额；5x是特定accuracy/scale对照，不是wall-time保证。 |
| 2511.04285v1 / RLoop: An Self-Improving Framework for Reinforcement Learning with Iterative Policy Initialization | 潜在：RL过程成功轨迹过滤RFT回初始policy再重启，保存跨step策略多样性以修正RL过拟合；需具体重初始化对象和训练预算，不以成熟RL/RFT组合单独准入。 |
| 2511.04485v1 / Q3R: Quadratic Reweighted Rank Regularizer for Effective Low-Rank Training | 已恢复[exact-v1完整题摘](./nov08-exact-v1-watch-core.txt)，不倒灌API v2：低秩预训练维持rank/objective困难，IRLS二次正则majorizes平滑logdet，引导可指定低秩矩阵。v1 ViT-Tiny/CIFAR10例60%/80%参数截断对应约1.3%/4%准确率损失，只是该模型任务，不能解释为LLM或runtime无损。潜在2+1+2=5，public及NeurIPS2025先公开身份待核；本次未展开全文/采用实验。 |
| 2511.04557v1 / Integrating Temporal and Structural Context in Graph Transformers for Relational Deep Learning | 潜在一般表示/多任务学习机制：时序跨邻居采样、latent bottleneck共同空间与disjoint label decoder，不能只凭RelBench榜首准入，也不因下游领域关闭。 |
| 2511.04598v1 / Environment Agnostic Goal-Conditioning, A Study of Reward-Free Autonomous Learning | 潜在负侧/训练方法：环境无关自主goal生成可训练各observations，但不区分goal价值导致单goal成功不稳定；保留off-policy/实验任务不同，不外推LLM或全目标可靠性。 |

新增安全事件：[OpenAI原blog](./nov08-openai-prompt-injections.txt)，[本日官方RSS](./openai-news-rss.xml)精确`Fri, 07 Nov 2025 11:30:00 GMT`即BJT19:30，完全落窗。正文完整核心已读：instruction hierarchy、安全monitors、sandbox、logged-out、sensitive site Watch Mode、确认与按需权限，最后明确未来将发布网络发送检测报告。初筛倾向关闭此解释事件：没有新对照/失效数据/发布变化，不能把成熟控制改写为新机制；安全相关必须root独立校准。原引用[Instruction Hierarchy](./nov08-openai-prior-identity.txt)日期2024-04-19、monitors引用实际跳gpt-oss-safeguard2025-10-29（不是先前口头误猜Oct21）；没有宣称旧安全研究全审或全已覆盖。Watch Mode是否此处首次新控制仍需精确旧官方说明定点核，不因文章标题纯解释直接一律关闭。

定点补核Watch Mode：原[Operator卡January23,2025及7月发布](./nov08-watch-date-core.txt)、[Operator控制核心](./nov08-exact-v1-watch-core.txt)实际读。离页/inactive暂停与active监督在旧事件原页已描述；11月7日博客未披露新控制/评价变化或新攻击反证，未来网络发送检测研究明确未发布。拟关闭此解释事件，不评分、不请求Books，不将旧卡数据重计为本窗研究；root安全相关局部校准仍待执行，不能因本次有精确RSS日期强造贡献。

最新普通停点：其余含糊题摘有限裁决完成于[TAIL_SCREENING](./TAIL_SCREENING.md)；六篇当前abs已实际取得并核comments/history，必要ThaiOCR纠错见[FINAL_LOCAL_NOTES](./FINAL_LOCAL_NOTES.md)。MiniMax tech原日期仅2026-05-13，MiMo More是内嵌第9～15项，相关旧日期缺段隔离。arXiv dated route400、旧月份route404已据实际错误纠正月表成功，仅50标题且无公告时刻后停止。作者普通来源/题摘工作已收束，root局部校准及日级复核待接；潜在日期hold不继续全部附件或全owner。
