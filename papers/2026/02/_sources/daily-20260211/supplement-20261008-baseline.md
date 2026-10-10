# Daily Research — 2026-02-11

**规范：** V3
**窗口：** 2026-02-10T09:00:00+08:00 ～ 2026-02-11T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-04T08:08:08+08:00

## 1. 结论

本日以V3独立重建并获非作者整日验收，不继承旧报告“1173/35/完成”标签。新精确v1完整题摘读取54个唯一论文家族（8首批+AB1/2/3各12+安全9+AIRS-Bench1），六项按具体贡献理由关闭；冻结48个确定落窗候选家族（不是全部分类召回）。47项完成必要证据审阅、1项中心争议安全隔离；Books为42项仅报告、2项真实整合获root POST、3项已有覆盖、1项暂缓终态。root已分批通过48项处置并完成六关闭项/最终六部分日级Gate；可执行扫描/筛选/审阅/Books及独立复核剩余0。本日有限停止，来源历史缺段及日期/中心争议保留项不授正面Coverage、性能或安全保证。

重要反侧：RLVR阶段optimizer须独立对照，不把Adam优势机械外推；同步节约绑定质量与运行点，检索子群差异不能充当干预因果；多跳压缩须计partial-sum再量化、metadata/codec/HBM与质量总成本，已融入Ch36；保留clean标签的feature corruption使训练观测z下Bayes目标不必等于clean f(z)，已融入Ch5，仅uniform iid bitflip合成条件、不采用争议λ补救。Agent安全评价必须分清普通输入与白盒routing、输出再注入与有机记忆、模拟marker与实际损害、query权限与行为policy；其余局部实现/评价反侧留报告，不为缺paper recipe造书稿diff。

## 2. 来源覆盖

所有检查限定本窗及ROADMAP主线。四组官方域名Feb10主题搜索和原生入口实际返回保存于[本日目录](../_sources/daily-20260211/STOP.md)。不把搜索无命中或当前目录首页称无遗漏。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | Research原生HTTP403；Feb10域内模型/Agent主题补检命中deep research既有文章的产品更新 | 受阻 | 历史Research窗口列表未恢复；产品更新无独立研究机制，不据此断言零 |
| SRC-ANTHROPIC | Research当前目录+Feb10域内主题搜索；定点系统卡Feb10changelog及Sabotage报告 | 受阻 | 纠错/风险事件日标无可包络时区；见§5，不采安全保证 |
| SRC-GOOGLE-AI | DeepMind/Research原生当前页面+Feb10主题搜索，完整DialogLab Blog核心 | 受阻 | Blog明言UIST2025；没有本次新机制；当前目录不支持所有历史条目穷尽 |
| SRC-META-AI | Research动态零文本+官方域主题搜索；AIRS-Bench完整v1 AB | 受阻 | 原生历史尾段缺失；AIRS新20任务/排行榜本身不足贡献，日期不再无差别审计 |
| SRC-QWEN | qwenlm原生重定向与有限域内Feb10主题搜索 | 受阻 | 新旧站历史完整性不能恢复；不能声称零 |
| SRC-DEEPSEEK | 原生主页+Feb10架构/推理主题补检 | 受阻 | 当前主页不提供历史发表列表，正面历史Coverage不成立 |
| SRC-MOONSHOT | 原生Blog可读到2025-11-07及更早；Feb10主题补检 | 受阻 | Blog未收当前时期完整研究，GitHub有限恢复仅当前10/42repos，非历史release段；已隔离，不全42库扩扫 |
| SRC-TENCENT-HUNYUAN | 首查Research零文本，浏览器三次timeout/线程限制，官方域Feb10主题补检 | 受阻 | 动态“全部”历史段不能恢复；精确隔离，不拿空响应作零 |
| SRC-ZAI | 首查Research timeout；官方域Feb10主题补检 | 受阻 | Research历史段未恢复；release有限列表已读至2026-02-12 GLM5→Feb3OCR跨窗，未见本窗release但不替代历史Research Coverage |
| SRC-BYTEDANCE-SEED | Research+public_papers第1页20/242、Feb10主题补检 | 受阻 | 论文分页历史未到本窗；Research可见publication10条至Jan27→Apr11跨窗，但首页不是全242条历史，缺段隔离、不全库扩池 |
| SRC-BAIDU-ERNIE | 原生Blog现有10摘要+Feb10主题补检 | 受阻 | 无历史完整段/日期分页；不能正面Coverage |
| SRC-XIAOMI-MIMO | 原生Paper8项到2025-05-12；Feb3→Mar13跨窗无Feb10paper；Blog15项无日标+主题补检 | 受阻 | Paper当前可见列表有界已读；Blog历史完整性缺口隔离 |
| SRC-MINIMAX | 原生Blog12项，2026-02-12→2026-01-27跨窗；Feb10域内补检剔除用户托管.space页 | 已检查 | 仅此可见列表与查询范围，不宣称站点无遗漏 |
| SRC-ARXIV | 本窗四组主线语义补检、API首100停止、cs.CL月首页有限标题查漏+本日旧inventory标题线索；大模型训练/推理/Agent/多模态相关标题继续完整AB | 受阻 | 原API query为(cs.CL/LG/DC/AI) AND submittedDate:"202602090000 TO 2602102359" AND language model/Transformer/MoE/agent/GPU，终界位数错误、工具响应截断且内容窗外，整体失效隔离，不授Coverage；搜索空回应非零命中、宽列表非队列，不扩池；拟入选逐项精确v1/public包络独立恢复 |

按需来源未常规扫描：目前未触发会议、协议或runtime重要release新增发现；论文所需primary证据只定点读取，不扩整站。

轻量撤回/纠错/安全信号仅围绕本次精确AB官方页comments/submission history与已命中的事件说明；未用版本号变化自动启动全版本深审。本次没有采用已撤回版本。与采用子命题相冲突的原证分别留在§4（AgentFence、噪声λ、rePIRL、Anchored、Judge/Aegis/Steer2Adapt等），定点冻结受影响主张；Anthropic事件日期隔离见§5，不以未遇更多标记声称全站无纠错。

## 3. 候选与判断

清单已冻结48个家族。评分对象为新材料增量，必要审阅逐项完成或精确中心隔离；原始54完整题摘与六贡献关闭不是候选分母，支持与直接反侧足够即停，不读无关证明/附件。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Parallel Track Transformers: Enabling Fast GPU Inference with Reduced Synchronization](https://arxiv.org/abs/2602.07306v1) | 2026-02-10T01:00:00+00:00 ～ 2026-02-10T04:24:22+00:00 | 2 + 2 + 2 = 6；具体增量见§4 | 标准完成 | 仅报告：（旧PT机制后的局部D/quality/runtime验证，未授架构普遍替代） |
| [Adaptive Retrieval helps Reasoning in LLMs -- but mostly if it's not used](https://arxiv.org/abs/2602.07213v1) | 2026-02-10T01:00:00+00:00 ～ 2026-02-10T04:22:12+00:00 | 2 + 1 + 2 = 5（设计反证加深）；具体增量见§4 | 深入完成 | 仅报告：（子群选择偏差未被因果干预控制） |
| [Do We Need Adam? Surprisingly Strong and Sparse Reinforcement Learning with SGD in LLMs](https://arxiv.org/abs/2602.07729v1) | 2026-02-10T01:00:00+00:00 ～ 2026-02-10T04:34:23+00:00 | 3 + 2 + 3 = 8；具体增量见§4 | 深入完成 | 已有覆盖：TRAIN-GRPO [Ch33 optimizer transform与state](../../../../books/part-04-training-system/33-grpo.md)已要求跨recipe的有效更新/状态/质量比较，非统一nominalLR |
| [DynamiQ: Accelerating Gradient Synchronization using Compressed Multi-hop All-reduce](https://arxiv.org/abs/2602.08923v1) | 2026-02-10T01:00:00+00:00 ～ 2026-02-10T05:03:05+00:00 | 2 + 2 + 3 = 7；具体增量见§4 | 深入完成 | 整合：TRAIN-DISTRIBUTED-TRAINING [Ch36通信压缩](../../../../books/part-04-training-system/36-distributed-training.md)，multi-hop partial-sum再量化与总成本 |
| [Trapped by simplicity: When Transformers fail to learn from noisy features](https://arxiv.org/abs/2602.08695v1) | 2026-02-10T01:00:00+00:00 ～ 2026-02-10T04:57:41+00:00 | 3 + 1 + 3 = 7；具体增量见§4 | 深入完成 | 整合：WORLDVIEW-REPRESENTATION [Ch5归纳偏置](../../../../books/part-01-worldview/05-what-neural-networks-learn.md#inductive-bias为什么有限数据仍可能产生泛化)，仅目标错配诊断 |
| [On Randomness in Agentic Evals](https://arxiv.org/abs/2602.07150v1) | 2026-02-10T01:00:00+00:00 ～ 2026-02-10T04:20:44+00:00 | 3 + 2 + 2 = 7（设计反证）；具体增量见§4 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66方差与重复评测](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，T0及paired backend identity限制 |
| [SpecAttn: Co-Designing Sparse Attention with Self-Speculative Decoding](https://arxiv.org/abs/2602.07223v1) | 2026-02-10T01:00:00+00:00 ～ 2026-02-10T04:22:26+00:00 | 2 + 2 + 2 = 6；具体增量见§4 | 标准完成 | 仅报告：（局部selector/内核方案，额外开销与部署口径受限） |
| [XShare: Collaborative in-Batch Expert Sharing for Faster MoE Inference](https://arxiv.org/abs/2602.07265v1) | 2026-02-10T01:00:00+00:00 ～ 2026-02-10T04:23:25+00:00 | 2 + 2 + 2 = 6；具体增量见§4 | 标准完成 | 仅报告：（batch局部方案，质量及communication proxy边界未扩成长期保证） |
| [Cross-View World Models](https://arxiv.org/abs/2602.07277v1) | 2026-02-10T01:00:00+00:00 ～ 2026-02-10T04:23:42+00:00 | 2 + 2 + 2 = 6；具体增量见§4 | 标准完成 | 仅报告：（known-map互补view局部证据，不证明新环境/物理持久状态） |
| [W&D: Scaling Parallel Tool Calling for Efficient Deep Research Agents](https://arxiv.org/abs/2602.07359v1) | 2026-02-10T01:00:00+00:00 ～ 2026-02-10T04:25:37+00:00 | 2 + 1 + 2 = 5；局部width/budget非单调对照 | 标准完成 | 已有覆盖：AGENT-PLANNING [Ch79并行与Critical Path](../../../../books/part-07-agent/79-planning.md#依赖并行与-critical-path)已承载不保证宽度收益与query/context/配额成本；本次新增局部验证 |
| [Scout Before You Attend: Sketch-and-Walk Sparse Attention for Efficient LLM Inference](https://arxiv.org/abs/2602.07397v1) | 2026-02-10T01:00:00+00:00 ～ 2026-02-10T04:26:31+00:00 | 2 + 2 + 2 = 6；跨层sketch/walk降低选择成本，质量/运行点另核 | 标准完成 | 仅报告：（selector局部方案，80%质量/90%加速点不合并） |
| [AgentSys: Secure and Dynamic LLM Agents Through Explicit Hierarchical Memory Management](https://arxiv.org/abs/2602.07398v1) | 2026-02-10T01:00:00+00:00 ～ 2026-02-10T04:26:32+00:00 | 3 + 2 + 3 = 8；predeclared intent+短命worker隔离持久上下文，保留合法JSON注入与validator边界 | 深入完成 | 仅报告：（JSON-parsable隔离方案与component confounding，未证新强typed安全contract） |
| [Are Reasoning LLMs Robust to Interventions on their Chain-of-Thought?](https://arxiv.org/abs/2602.07470v1) | 2026-02-10T01:00:00+00:00 ～ 2026-02-10T04:28:13+00:00 | 3 + 2 + 2 = 7；保义改写/噪声/错误CoT的质量及长度反侧 | 深入完成 | 仅报告：（语义忠实度/重采样对照未定，不采内部因果/统一补救） |
| [Improving Variable-Length Generation in Diffusion Language Models via Length Regularization](https://arxiv.org/abs/2602.07546v1) | 2026-02-10T01:00:00+00:00 ～ 2026-02-10T04:30:03+00:00 | 2 + 1 + 2 = 5；length-conditioned confidence校正与逐token动态canvas | 标准完成 | 仅报告：（启发式长度代理/有限backbone与成本分母，不采无条件稳定长度保证） |
| [The Value of Variance: Mitigating Debate Collapse in Multi-Agent Systems via Uncertainty-Driven Policy Optimization](https://arxiv.org/abs/2602.07186v1) | 2026-02-10T01:00:00+00:00 ～ 2026-02-10T04:21:35+00:00 | 2 + 2 + 2 = 6（共识设计反侧加深）；具体增量见§4 | 深入完成 | 仅报告：（uncertainty/reward局部诊断，未证明正确共识） |
| [Is there “Secret Sauce” in Large Language Model Development?](https://arxiv.org/abs/2602.07238v1) | 2026-02-10T01:00:00+00:00 ～ 2026-02-10T04:22:47+00:00 | 2 + 1 + 2 = 5；具体增量见§4 | 标准完成 | 仅报告：（observational FE/compute估计，不采因果比例或通用降本） |
| [When Is Enough Not Enough? Illusory Completion in Search Agents](https://arxiv.org/abs/2602.07549v1) | 2026-02-10T01:00:00+00:00 ～ 2026-02-10T04:30:07+00:00 | 2 + 2 + 2 = 6（设计反证加深）；具体增量见§4 | 深入完成 | 仅报告：（trace judge的E/B代理与额外ledger成本，非已证完整核验） |
| [Gaussian Match-and-Copy: A Minimalist Benchmark for Studying Transformer Induction](https://arxiv.org/abs/2602.07562v1) | 2026-02-10T01:00:00+00:00 ～ 2026-02-10T04:30:25+00:00 | 2 + 1 + 3 = 6；具体增量见§4 | 标准完成 | 仅报告：（受限synthetic retrieval诊断与conditional asymptotic theorem） |
| [ViCA: Efficient Multimodal LLMs with Vision-Only Cross-Attention](https://arxiv.org/abs/2602.07574v1) | 2026-02-10T01:00:00+00:00 ～ 2026-02-10T04:30:41+00:00 | 2 + 2 + 2 = 6；具体增量见§4 | 标准完成 | 仅报告：（LLaVA重训局部read/write取舍，prefill非端到端无损） |
| [Learning to Self-Verify Makes Language Models Better Reasoners](https://arxiv.org/abs/2602.07594v1) | 2026-02-10T01:00:00+00:00 ～ 2026-02-10T04:31:10+00:00 | 3 + 2 + 2 = 7（生成/验证设计反证）；具体增量见§4 | 深入完成 | 仅报告：（局部verification→generation迁移，不采内在纠错因果/全面更优） |
| [Astro: Activation-guided Structured Regularization for Outlier-Robust LLM Post-Training Quantization](https://arxiv.org/abs/2602.07596v1) | 2026-02-10T01:00:00+00:00 ～ 2026-02-10T04:31:13+00:00 | 2 + 2 + 2 = 6；具体增量见§4 | 标准完成 | 仅报告：（PTQ准备局部重构，flat-basin近似不授全模型严格等价） |
| [SERE: Similarity-based Expert Re-routing for Efficient Batch Decoding in MoE Models](https://arxiv.org/abs/2602.07616v1) | 2026-02-10T01:00:00+00:00 ～ 2026-02-10T04:31:41+00:00 | 2 + 2 + 2 = 6；具体增量见§4 | 标准完成 | 仅报告：（calibration similarity与primary union局部质量/访存取舍） |
| [Agent-Fence: Mapping Security Vulnerabilities Across Deep Research Agents](https://arxiv.org/abs/2602.07652v1) | 2026-02-10T01:00:00+00:00 ～ 2026-02-10T04:32:35+00:00 | 3 + 2 + 2 = 7（安全深入）；具体增量见§4 | 争议 | 暂缓：（SC exposure标签与同版aggregate对立；性能/安全排序隔离） |
| [From Assistant to Double Agent: formalizing and benchmarking attacks on openclaw for Personalized Local AI Agent.](https://arxiv.org/abs/2602.08412v1) | 2026-02-10T01:00:00+00:00 ～ 2026-02-10T04:51:02+00:00 | 3 + 2 + 2 = 7（安全深入）；具体增量见§4 | 深入完成 | 仅报告：（stage触发/marker路径受限，不采完整真实损害及通用安全率） |
| [PARD: Enhancing Goodput for Inference Pipeline via ProActive Request Dropping](https://arxiv.org/abs/2602.08747v1) | 2026-02-10T01:00:00+00:00 ～ 2026-02-10T04:58:53+00:00 | 2 + 1 + 2 = 5；具体增量见§4 | 标准完成 | 仅报告：（真实RAG局部提前丢弃，DNN priority/CLT不自动迁移） |
| [Debugging code world models](https://arxiv.org/abs/2602.07672v1) | 2026-02-10T01:00:00+00:00 ～ 2026-02-10T04:33:03+00:00 | 3 + 2 + 2 = 7（设计反证）；具体增量见§4 | 深入完成 | 仅报告：（correct-action teacher forcing与BPE成因分开，不授内部执行可靠性） |
| [Blind to the Human Touch: Overlap Bias in LLM-Based Summary Evaluation](https://arxiv.org/abs/2602.07673v1) | 2026-02-10T01:00:00+00:00 ～ 2026-02-10T04:33:05+00:00 | 3 + 2 + 2 = 7（设计反证）；具体增量见§4 | 深入完成 | 仅报告：（overlap/order条件偏好，不把人类reference身份当质量真值） |
| [ParisKV: Fast and Drift-Robust KV-Cache Retrieval for Long-Context LLMs](https://arxiv.org/abs/2602.07721v1) | 2026-02-10T01:00:00+00:00 ～ 2026-02-10T04:34:12+00:00 | 2 + 2 + 2 = 6；具体增量见§4 | 标准完成 | 仅报告：（GPU metadata/UVA局部retrieval，质量预算/设备缺项不授普遍drift保证） |
| [Learning to Continually Learn via Meta-learning Agentic Memory Designs](https://arxiv.org/abs/2602.07755v1) | 2026-02-10T01:00:00+00:00 ～ 2026-02-10T04:34:58+00:00 | 2 + 2 + 2 = 6；具体增量见§4 | 标准完成 | 仅报告：（offline design搜索/静态部署局部，memory cost不是搜索/agent总费用） |
| [Rolling Sink: Bridging Limited-Horizon Training and Open-Ended Testing in Autoregressive Video Diffusion](https://arxiv.org/abs/2602.07775v1) | 2026-02-10T01:00:00+00:00 ～ 2026-02-10T04:35:27+00:00 | 2 + 1 + 2 = 5；具体增量见§4 | 标准完成 | 仅报告：固定prompt缓存维护局部验证，不授开放世界/无限时域保证 |
| [MaD-Mix: Multi-Modal Data Mixtures via Latent Space Coupling for Vision-Language Model Training](https://arxiv.org/abs/2602.07790v1) | 2026-02-10T01:00:00+00:00 ～ 2026-02-10T04:35:48+00:00 | 2 + 2 + 2 = 6；具体增量见§4 | 标准完成 | 仅报告：预定义少域/阶段模型的受限mixture估计，不授通用最优配比 |
| [Emergent Structured Representations Support Flexible In-Context Inference in Large Language Models](https://arxiv.org/abs/2602.07794v1) | 2026-02-10T01:00:00+00:00 ～ 2026-02-10T04:35:54+00:00 | 2 + 1 + 3 = 6；具体增量见§4 | 标准完成 | 仅报告：reverse-dictionary条件干预，不授所有推理共同substrate |
| [Thinking Makes LLM Agents Introverted: How Mandatory Thinking Can Backfire in User-Engaged Agents](https://arxiv.org/abs/2602.07796v1) | 2026-02-10T01:00:00+00:00 ～ 2026-02-10T04:35:56+00:00 | 3 + 2 + 2 = 7；具体增量见§4 | 深入完成 | 仅报告：mandatory prompt局部反证，不授thinking普遍伤害或披露因果 |
| [rePIRL: Learn PRM with Inverse RL for LLM Reasoning](https://arxiv.org/abs/2602.07832v1) | 2026-02-10T01:00:00+00:00 ～ 2026-02-10T04:36:52+00:00 | 2 + 2 + 2 = 6（公式纠错受影响加深）；具体增量见§4 | 深入完成 | 仅报告：专家轨迹/ORM下受限PRM对照，熵符号与reward唯一恢复不采 |
| [TodoEvolve: Learning to Architect Agent Planning Systems](https://arxiv.org/abs/2602.07839v1) | 2026-02-10T01:00:00+00:00 ～ 2026-02-10T04:37:03+00:00 | 2 + 2 + 2 = 6；具体增量见§4 | 标准完成 | 仅报告：局部meta-planner架构搜索，不授普遍Pareto最优/代码安全 |
| [Recurrent-Depth VLA: Implicit Test-Time Compute Scaling of Vision–Language–Action Models via Latent Iterative Reasoning](https://arxiv.org/abs/2602.07845v1) | 2026-02-10T01:00:00+00:00 ～ 2026-02-10T04:37:12+00:00 | 2 + 2 + 2 = 6；具体增量见§4 | 标准完成 | 仅报告：受限latent迭代/stop取舍，不以收敛代理认证动作安全 |
| [Geometry-Aware Rotary Position Embedding for Consistent Video World Model](https://arxiv.org/abs/2602.07854v1) | 2026-02-10T01:00:00+00:00 ～ 2026-02-10T04:37:26+00:00 | 2 + 2 + 2 = 6；具体增量见§4 | 标准完成 | 仅报告：已知pose的rotation回访局部证据，不授完整3D状态保证 |
| [Anchored Decoding: Provably Reducing Copyright Risk for Any Language Model](https://arxiv.org/abs/2602.07120v1) | 2026-02-10T01:00:00+00:00 ～ 2026-02-10T04:20:01+00:00 | 2 + 2 + 3 = 7；具体增量见§4 | 深入完成 | 仅报告：受限reference-KL机制；安全anchor/法律判断不采用 |
| [Rethinking Latency Denial-of-Service: Attacking the LLM Serving Framework, Not the Model](https://arxiv.org/abs/2602.07878v1) | 2026-02-10T01:00:00+00:00 ～ 2026-02-10T04:38:03+00:00 | 3 + 2 + 3 = 8；具体增量见§4 | 深入完成 | 仅报告：版本/共机负载下资源反证；不授全部serving脆弱性 |
| [The Judge Who Never Admits: Hidden Shortcuts in LLM-based Evaluation](https://arxiv.org/abs/2602.07996v1) | 2026-02-10T01:00:00+00:00 ～ 2026-02-10T04:40:48+00:00 | 3 + 1 + 3 = 7；具体增量见§4 | 深入完成 | 仅报告：cue-swap局部反证；rationale不代表内部因果认知 |
| [Position: Stateless Yet Not Forgetful: Implicit Memory as a Hidden Channel in LLMs](https://arxiv.org/abs/2602.08563v1) | 2026-02-10T01:00:00+00:00 ～ 2026-02-10T04:54:33+00:00 | 3 + 2 + 3 = 8；具体增量见§4 | 深入完成 | 仅报告：再注入/植入条件的路径；不授有机跨请求记忆 |
| [Sparse Models, Sparse Safety: Unsafe Routes in Mixture-of-Experts LLMs](https://arxiv.org/abs/2602.08621v1) | 2026-02-10T01:00:00+00:00 ～ 2026-02-10T04:55:57+00:00 | 3 + 2 + 3 = 8（安全深入）；具体增量见§4 | 深入完成 | 仅报告：白盒route干预局部反证，非普通输入可达与通用防御 |
| [On Protecting Agentic Systems’ Intellectual Property via Watermarking](https://arxiv.org/abs/2602.08401v1) | 2026-02-10T01:00:00+00:00 ～ 2026-02-10T04:50:46+00:00 | 2 + 2 + 3 = 7（安全深入）；具体增量见§4 | 深入完成 | 仅报告：可见轨迹分布水印受限，等价动作不认证全部副作用 |
| [CryptoGen: Secure Transformer Generation with Encrypted KV-Cache Reuse](https://arxiv.org/abs/2602.08798v1) | 2026-02-10T01:00:00+00:00 ～ 2026-02-10T05:00:05+00:00 | 2 + 2 + 3 = 7（安全深入）；具体增量见§4 | 深入完成 | 仅报告：半诚实GPT-2加密KV实现取舍，非恶意安全与端到端恒定成本 |
| [Aegis: Towards Governance, Integrity, and Security of AI Voice Agents](https://arxiv.org/abs/2602.07379v1) | 2026-02-10T01:00:00+00:00 ～ 2026-02-10T04:26:05+00:00 | 3 + 2 + 2 = 7（安全深入）；具体增量见§4 | 深入完成 | 仅报告：query-ACL与行为风险分层反侧，不采生产安全率/认证 |
| [Steer2Adapt: Dynamically Composing Steering Vectors Elicits Efficient Adaptation of LLMs](https://arxiv.org/abs/2602.07276v1) | 2026-02-10T01:00:00+00:00 ～ 2026-02-10T04:23:40+00:00 | 2 + 2 + 2 = 6（安全受影响加深）；具体增量见§4 | 深入完成 | 仅报告：语义basis与fewshot回归惩罚局部取舍，非lossless安全保证 |
| [Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation](https://arxiv.org/abs/2602.07338v1) | 2026-02-10T01:00:00+00:00 ～ 2026-02-10T04:25:07+00:00 | 3 + 1 + 2 = 6（设计反侧加深）；具体增量见§4 | 深入完成 | 仅报告：合成history附加信息与局部refinement，非真实用户意图恢复定理 |
| [Efficient Post-Training Pruning of Large Language Models with Statistical Correction](https://arxiv.org/abs/2602.07375v1) | 2026-02-10T01:00:00+00:00 ～ 2026-02-10T04:26:00+00:00 | 2 + 2 + 2 = 6；具体增量见§4 | 标准完成 | 仅报告：解析weight统计补偿的局部质量，非执行kernel加速/全层能量保证 |

日期不是Submitted。新增原值见[dates3](../_sources/daily-20260211/feb11_dates3.json)、[dates4](../_sources/daily-20260211/feb11_dates4.json)、[dates5](../_sources/daily-20260211/feb11_dates5.json)；首批原值见[feb11_dates1.json](../_sources/daily-20260211/feb11_dates1.json)与[feb11_dates2.json](../_sources/daily-20260211/feb11_dates2.json)，精确v1题摘历史见[首批完整AB](../_sources/daily-20260211/feb11_calibration_exact_AB.json)。官方availability policy将Fri06 19UTC～Mon09 19UTC提交的最早公告定为Mon09 20EST，即Feb10 01UTC；final-ID DataCite registered只提供latest上界，秒精度加1秒取排他终点。本次区间全落窗，不把registration或metadata Updated当真实public时刻。没有该正文更早公开信号；07306旧PT机制的2025独立公告/2507.13575是已公开知识，仅本文新增对照计本次贡献。

新增最后三项的元数据原值见[dates6](../_sources/daily-20260211/feb11_dates6.json)，沿用上述官方公告下界与registration上界包络，不以Submitted作public。

## 4. 证据与知识整合

精确v1完整核心原文：[首批](../_sources/daily-20260211/feb11_core_calibration_raw.json)与[AB1四项](../_sources/daily-20260211/feb11_first_admitted_core.json)。仅围绕下述命题读必要方法/评价/反侧，无artifact复现或生产验证声明。

### [Parallel Track Transformers: Enabling Fast GPU Inference with Reduced Synchronization](https://arxiv.org/abs/2602.07306v1)
准入链：每层TP同步昂贵→track在D层后统一同步→需要联合选择预训练架构、同步频率与质量，不能只换serving参数。新增命题评分2+2+2=6（底层PT已在2025 Apple Foundation Models公开，本文有新的dense/PT+D矩阵与运行测量；不是把旧架构重新计突破）。
证据§2，§3 Tables1-4：8tracks，D2/4/8；6B800Btoken，13/30B400Btoken等规模各自same recipe。6B MMLU dense .560→D8 .360，GSM8K .317→.271；30B也非无损(.630→.615 MMLU，.523→.488 GSM8K)。30B8xH100 vLLM maxbatch256吞吐，maxbatch1latency；1024input4096output throughput 5990.98→5596.01(D8)回退，而4096/128 865.2→1141.18。TensorRT variant internally implementsPT，publicopensource不支持。precision/version/SLO/concurrency未披露。采用有限同步-质量-运行点权衡，不采用全面throughput改善或无损drop-in。仅报告：旧PT机制的运行点验证尚不足以改变长期架构选择，不把有限D矩阵/不同质量加速当普遍取代dense，保留原TP分支；root限定处置已通过。

### [Adaptive Retrieval helps Reasoning in LLMs -- but mostly if it's not used](https://arxiv.org/abs/2602.07213v1)
评分2+1+2=5，但设计反证深入受影响内容。§3-4，AppA.1/A.2：Llama3.1-8B-Instruct fp16 T0 max1024，GSM/MATH，staticCoT/adaptive提示不同；bge-m3检索200→5，正文与appendix reranker描述crossencoder/ColBERT不完全一致。CoT82.1/44.2，static75.8/42.4，adaptive83.2/50.6是作者结果。retrieval仅7%GSM/38.8%MATH，MATH难度1→5检索率14→60.4%；retrieved子群25help25hurt，未检索子群63.7不证明“禁检索造成更好”。无同题随机干预、token预算对齐或CI。采用检索闸门强烈选择偏差+静态上下文非普遍正益；不采用 causal RAG failure/普遍不检索策略。仅报告，因为反侧归因未定。

### [Do We Need Adam? Surprisingly Strong and Sparse Reinforcement Learning with SGD in LLMs](https://arxiv.org/abs/2602.07729v1)
评分3+2+3=8，深入§3-7+AppA.1/B/C/D相关配置。Qwen3 1.7/8B、Llama3.1-8B，数学/代码/合成RLVE，GRPO及PPO；4x96GB GH200，verl/FSDP bf16，batch256 prompt1024。Adam1e-6，SGD .1(小PPO .01)，有SGD/momentum/RMSProp ratesweep，不能比较同nominalLR。SGD有些workload匹配/更好但Qwen1.7B8K56.8<Adam58.2；RLVE5008K56.5<57.1，16K63<64.5，无seed CI。状态口径Adam FP32master+m+v=12p bytes，SGD master=4p，1.7B理论13.6GB states、peak作者15.7GB含FSDP buffer。所谓更新稀疏依赖1e-5阈值和bf16，§7明确rounding/小梯度，不是所有真实梯度本征0。采用phase-specific optimizer评估与state memory，非SGD普遍胜/所有adaptive obsolete。已有覆盖：TRAIN-GRPO Ch33 optimizer/Sharding段已具体要求nominalLR跨transform不可比、phase/recipe有效更新尺度与state、Adam共存选择；相邻Ch28处理训练阶段的optimizer/data/activation耦合，Ch32 critic/PPO与Ch34离线优化不能混算。root已实际读Ch33 1130–1147及邻接，Existing通过；12p/4p只是本文限定状态口径，不强写新SGD配方。

### [DynamiQ: Accelerating Gradient Synchronization using Compressed Multi-hop All-reduce](https://arxiv.org/abs/2602.08923v1)
评分2+2+3=7。§3.1-3.4/§4/§5.1-5.3/§6.1-6.2以及AppB相关topology heuristic：metadata allreduce→groupnorm/budget分配→2/4/8bit streams，hop decompress-accumulate-recompress，不在低比特整数空间直接累加；sharedrandom negativecorrelation借用已有方法，kernel fusion缓解额外HBM访问。默认group16/supergroup256/UINT8 group scale/BF16 super-scale/avg5bits。4servers8GPU（原文RTX A6000 ada48GB/NV4，保留原称不擅自改）、100GbEthernet；BERTlarge/Gemma1B/Llama1B fine-tune，batch1或4。低比特MX4/6不native，报告compute-free等流量的bestcase lower-bound TTA，不是实际执行benchmark；THC4bit local8bit accumulate避免overflow，OR union适配不原生。§5实际ring/butterfly4worker，§6 TinyBERT到64worker是simulation。5bit优于3/4bit不是压缩率越高越好，ring/butterfly误差差异受partial sum大小；AppB O(n^3)/O(n^2)是有boundedsame-distribution intuition的heuristic upper bound，不runtime扩容证明。不开源实现不阻断论文限定命题，但不声称artifact复现或生产可用。

实际整合：TRAIN-DISTRIBUTED-TRAINING [Ch36通信压缩](../../../../books/part-04-training-system/36-distributed-training.md)，codec/HBM段后新增一段。原正文已有压缩率、误差、融合与回退，但没有receiver重建→累加partial-sum→重编码及topology error路径。只补该差异、metadata/codec/HBM/质量整体成本及有限实验/模拟边界，保持旧完整collective分支。root已实际POST正文单段、codec邻接和末注通过，锁释放。

### [Trapped by simplicity: When Transformers fail to learn from noisy features](https://arxiv.org/abs/2602.08695v1)
评分3+1+3=7。§3-5：uniformrandominputs的iid bitflips、无labelnoise；sparseparity/oddmajority成功，3200randomkjunta因cleanf和Bayes-noisy f*N目标不同导致有near-opt noisy loss仍cleanerror。Prop2是随机布尔函数期望sensitivity不是所有function定律。直接中心冲突：AB称penalizing HIGH sensitivity，正文使用 -lambda I[fhat]、明确encourage higher sensitivity以逃离simpler trap，图注还有歧义。因此只采objective target mismatch/shortcut反侧，不采罚项recipe。evenmajority大noise目标gap大，罚项也失败；高bitnoise synthetic未证明自然LLM任务。

实际整合 WORLDVIEW-REPRESENTATION [Ch5 §Inductive bias](../../../../books/part-01-worldview/05-what-neural-networks-learn.md#inductive-bias为什么有限数据仍可能产生泛化) 新段：现有augmentation语义保持/shortcut/coding几何反侧没有明确“观察z=x⊕noise、监督f(x)，给定z最优不必是clean f(z)”这一目标错配。新增该受限诊断，不静默改写旧机制；clean/noisy评测分账是本报告系统推断，额外评测成本、真实增强可保持语义和非LLM必失败边界在正文。root实际读必要原文及现owner差额后授单文件窄锁，已实核新段与前后邻接、末注POST通过；无实验复现。罚项remedy争议子命题仍隔离不采，不阻断独立一致诊断。



### [On Randomness in Agentic Evals](https://arxiv.org/abs/2602.07150v1)

旧判断是temperature0足以稳定评测；本次实际增量是固定模型/脚手架、每配置10次全500题运行的方差和早token分岔，改变小幅单run提升的证据权限，评分3 + 2 + 2 = 7，设计反证深入。精确v1 §2.1-2.4/§3.2已读：Qwen3-32B、DeepSWE-preview、Devstral2×nano-agent/R2E-Gym，默认温度与0，合计120runs/60000trajectories；本地vLLM与Mistral API部署，不同provider独立replication不是跨engine消融。Table1最小2.2至最大6.0pp range，温度0仍std0.7–1.8pp，并非所有模型sigma>1.5。两scaffold都是append-only，没有compaction；未证长轨迹长度导致方差的因果，更未定位具体GPU non-determinism来源。pass@k是任一成功的potential，pass^k全成功consistency，不能当线上可靠性lower-bound guarantee。§3.2 median-sigma1.5/80%power/normal假设的36runs为检测1pp，不是所有suite固定36准入线。作者运行没有复现。已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)41的repeated/outcome variance、281的T0远端非确定、313–317的paired差值/CI、Backend identity段的对照身份已承载该证据权限。root实际读上述正文与邻接通过；36runs只为局部power设定，不增加固定普遍门槛。

### [SpecAttn: Co-Designing Sparse Attention with Self-Speculative Decoding](https://arxiv.org/abs/2602.07223v1)

原本sparse-draft需要独立selector；新增是full-verifierattention副产物指导下次draft并在collect logits时控制HBM成本，评分2 + 2 + 2 = 6。精确v1 §3.1-3.4/§4/§5标准审阅：聚合all draft包括rejected attention比last accepted selector少后段acceptance衰减，但取所有query导致FA3开销；实际collect first draft+bonus两query，约等精度避免随gamma线性增长，不是“免费oracle”零成本。Table1 LongBench-v2 7%KV、gamma7/11示意；H100单kernel gptoss采两query仍37%attention overhead，整decode selector5.9–9.4%是不同口径。vLLM hook/proposer、page size1复用PagedAttention，logits写BF16 HBM，未核实代码/runtime。§5短输入AIME25/CodeElo平均Qwen8B输出19680，一H100NVL94GB/maxbatch128/replay稳定吞吐；长input96–120K，用两GPU PD排除prefill/maxbatch4/4/5/20，所以不等端到端TTFT/SLO改善。Qwen3-30B FP8、gptoss20B MoE MXFP4仅dense halfblocks稀疏。fullverification保留target分布的算法要求，不把draft quality或吞吐当部署正确性证明。对照同vLLM但SpecExtend改成layerwise selfspec variant，非其原separate-drafter部署；无reportedCI/SLO，version Not Disclosed。仅报告这项受限跨阶段selector/内核实现，不采普遍“零selector成本”知识修订；root限定处置已通过。

### [XShare: Collaborative in-Batch Expert Sharing for Faster MoE Inference](https://arxiv.org/abs/2602.07265v1)

token top-k不等batch expertunion小；新增batch/per-request/GPU-budget co-selection使权重访存、质量和共享选择连起来，评分2 + 2 + 2 = 6。§3-6/AppA必要对照标准审阅：sum gatingmass为modular proxy的greedy最优，不是真实accuracy最优；router-score-reliability是假设。warmup保留每token top1/2再优化batch集合，request内speculation correlation可用分层选择；均匀每层budget非全层最佳。p5en.48xlarge H100/vLLM，gptoss120B TP1，DSR1 TP8（正文称EP-aware但AppA未披露真正EP通信benchmark），precision/input-output长度/SLO/repetitions Not Disclosed。gptoss BS16 aggressivewarmup-only约50%OTPS但AIME87.5→76.67；BS4 EAGLE3 length3无warmup严重降质，少于1pp均值差不能自动叫within statistical noise，无CI。DSR1专家数/MaxGPU从25.6→8.64是proxyload，不是实测bytes/commtime3x。只采batch selection的质量-访存权衡与proxy边界；不采无损通用selector/productioncommunication保证。仅报告局部方案，不以缺少某篇recipe造Books差异；root限定处置已通过。

### [Cross-View World Models](https://arxiv.org/abs/2602.07277v1)

action-conditioned预测从单ego扩展到互补视角，不应把viewcount当正收益；本次双向view conditioning与matchedcompute/matchedexposure的非单调结果，评分2 + 2 + 2 = 6。§3-4+AppA标准审阅：4186一分钟game episodes，60→5FPS，224px，90:10split，同一known环境；输入四帧0.8s/action(dx,dy,dyaw)，CDiT-L加viewembedding到AdaLN，训练future/past12.8s，测试最多4s，4H100/H200/batch64/73epochs。没有独立几何self-consistency loss（不能照摘要转成自己想象的objective）；crossview配对训练作为表征约束是作者设计。两个view ego/BEV对比4view ego/BEV/OS/front，等compute之外另比sameview训练exposure，1257测试样本/3pred每episode、bootstrap95%CI；4view较差但exposure和view information仍纠缠，不能因果拆成单一视角信息解释。BEV静态map主导LPIPS，作者改用marker localization；2view ego→BEV median2px / marker17px，不是全局3D推理证明。单knownmap spawn/sky变动不排除部分map记忆，未见新地图transfer/realrobotclosedloop。仅报告互补view的局部budget/评价盲区，不采物理环境持久state或真实planning可靠性保证，root限定处置已通过。

### [W&D: Scaling Parallel Tool Calling for Efficient Deep Research Agents](https://arxiv.org/abs/2602.07359v1)

并行独立工具是成熟机制；本次准入2+1+2=5是同模型/工具栈下width与质量/成本/等待的非单调对照，不是BrowseComp高分本身。精确v1 §3.1/3.2/§5：GPT5 Medium，同工具，first100 BrowseComp/HLE，max100turn；BrowseComp width1为66%/平均45.7turn、100任务API+tool总价$102.5、平均walltime1522.6s；width3为68%/23.8turn/$65.7/904.2s。价格不是每任务值，少turn不等总工具调用/token匹配；无CI、不证明质量真提升。width8在此100turn下63%低于width3的68%；3→2→1递减schedule为74%，constant3为68%，但多数任务stage前已earlystop，不能解释成完全matched-budget scheduler因果。GAIA为103text-only，full BrowseComp62.2与GPT5High54.9不等reasoning budget，不用于归因。API evaluator/运行硬件/precision/provider版本/SLO Not Disclosed，不外推生产等待保证。

已有覆盖：AGENT-PLANNING [Ch79 §依赖、并行与Critical Path](../../../../books/part-07-agent/79-planning.md#依赖并行与-critical-path)已有独立subquery/ready nodes、有限工具预算、重复query/context/配额成本以及“不证明宽度越大越好”，相邻Ch78把调用视作proposal并逐项验schema/权限/effect，Ch81的plan profile保留cost-model漂移与runtime effect commit。本文只增加已承载命题的局部验证，不造缺少某篇recipe的Books差额。root实际必要原文与准入通过，root已实际读Ch79 106–129并批准Existing。

### [Scout Before You Attend: Sketch-and-Walk Sparse Attention for Efficient LLM Inference](https://arxiv.org/abs/2602.07397v1)

固定mask或各层重选KV昂贵→block均值/随机Hadamard sketch估计关系，deterministic walk组合前层及本层score再topτ→重新比较prefill/decode选择开销与质量，2+2+2=6。精确v1 §2.1–2.3/§4.1–4.4，来自[feb11_AB2_core0](../_sources/daily-20260211/feb11_AB2_core0.json)：block64，sketch64，walk exponent8，保留首末block、前2层不稀疏；CUDA sketch/Triton sparse，自定义PyTorch pipeline，singleH10094GB，greedy Llama3.1-8B/Llama3.2-1B/Qwen2-7B，LongBench与4–64KRULER。质量表在80%sparsity，Llama8B LongBench AVG47.95→47.63、passagecount10→6.53，某些局部task改善但并非无损。速度用Llama8B/batch1/90%sparsity、16–128K，相对FlashAttention，decode最高1.6x；不能把不同sparsity的质量与速度组合成同质量加速。精度/输出长度/重复数/CI/SLO/runtimeversion Not Disclosed。核心得分依据是可比稀疏比例的受限机制/overhead，不采未经必要假设核实的通用小世界理论保证；不遍历proof。仅报告局部跨层selector方案，未证跨负载稳定性/生产能力，不因名词可映射KV owner造长期书稿改动。公开registered原值见[dates3](../_sources/daily-20260211/feb11_dates3.json)，与AB2 Sat提交的公告下界包络落窗。

### [AgentSys: Secure and Dynamic LLM Agents Through Explicit Hierarchical Memory Management](https://arxiv.org/abs/2602.07398v1)

工具PI随长上下文积累→主agent先声明typed intent，raw observation只进不继承主history/userquery的短命worker，nested调用由operation validator控制→重新选择隔离单位与向上信息通道，3+2+3=8；安全深入精确v1 §4/§5.1–5.5/§6.1–6.4/§7（[核心原文](../_sources/daily-20260211/feb11_AB2_core0.json)）。重要正文收窄：设计描述schema-bounded，但实际acceptance只要求JSON-parsable object，§5.2/5.3将intent称best-effort；字符串仍可携PI，合法JSON不等typedfield或语义安全。validator不看raw output，但看tool arguments/intent，仍可受这些derived信息影响；只worker递归command触发（tool taxonomy由LLM一次分类，歧义defaultcommand），主agenttop-level不受此validator。sanitizer仅否决command后boundedrestart，read任务不全部清洗；固定错误对象不等总任务正确。

AgentDojo97user/629injection tasks、ASB10scenarios；主表GPT4omini，其他5foundationmodels有对照，但不同API/offline配置不是隔离component因果。AgentDojo baselineASR30.66%→0.78%、benign63.54→64.36，去contextisolation ASR8.62；adaptive manual1.43/PAIR2.06，BankingPAIR6.94保留非零失败，不采“eliminate persistence”普遍保证。去validator时无条件sanitization也是变化，ablation非单一checker干预。tokens baseline0.82M→3.25M（不是低于无防护/近零开销），无end-to-endlatency/SLO/CI披露；自定义benign×(1−ASR)指标不授业务净值。采用受限predeclared extraction/context隔离与commandgate。具体比较：Ch78已有parse→schema→authorization→business语义/effect分账，Ch82 Spawn段已有tainted inheritance与最小上下文/allowlist/scope检查，但这是向下传播，不冒称已精确覆盖本文向上短worker extraction。拟新增长期强typed通道却未被实际JSON-only/validator混杂支持；因此仅报告局部方案与残余风险，不写更强安全contract、也不以paperrecipe缺少造diff。日期AB2 Sat提交+DataCite registered04:26:31给本窗包络，字段原值见dates3，不把Submitted当public。

### [Are Reasoning LLMs Robust to Interventions on their Chain-of-Thought?](https://arxiv.org/abs/2602.07470v1)

CoT正确内容不保证继续生成稳定，错误插入也不必最终失败；新增固定位置七类干预的质量/长度反侧，3+2+2=7。精确v1 §3.1–3.3/§4.1–4.3/§5、D.4/D.6：九openweight 1.5–32B模型，Math/Science/Logic为通用推理评价非科学应用机制。仅选择所有模型原先答对的交集，Math先600后按常见答案downsample的最终数量表述不完全清晰，Science231/Logic326；结果不是一般题目鲁棒率。按累计characters0.1/0.3/0.5/0.7/0.9定位，双换行分step，重新采8continuations T0.6/p0.95，majority-robust要求≥5个正确，不等单run或线上保证。无matched无干预重采样对照；不同模型推荐生成设置，hardware/precision/maxoutput/SLO未披露，不把token长度当walltime。

表面保义paraphrase质量下降/少数模型变长不是一律“短60%”：Nemotron237.69%/Phi4ReasoningPlus330.68%为反侧；插随机text的1.5B长度+665.16%。所谓保义仅100人工初检及D.4每域100GPT5.1judge 92/98/93%，仍有内容改变残余，不能将全部质量差归为style/doubt因果。doubt分类400句与四人多数κ.8742只是文本标注一致性，不内部metacognition证明；插Wait的Logic Table7有负项，不是统一补救。采用实际trace干预要同时验内容/继续质量/预算的局部反证，不采CoT本身全faithful、所有噪声能恢复或训练Wait必通用增强。Ch20“格式损失”已有prompt条件与decoder mask、格式/内容质量分账及重格式化改错风险，但不冒称精确覆盖CoT中间轨迹干预。新 causal style/doubt解释被语义变化残余及缺matched resampling限制；仅报告此局部反侧，不把未识别的机制写成长期统一修复。

### [Improving Variable-Length Generation in Diffusion Language Models via Length Regularization](https://arxiv.org/abs/2602.07546v1)

固定canvas跨长度比较entropy有bias→拟合instance k、以AVGnegativeentropy−k logL作代理，exponential probe后邻域±1迭代并commit左侧一token→重新选长度探索和forward成本，2+1+2=5。精确v1 §3/§4.1–4.2/4.5–4.6/AppA/B/G：semantic compatibility与length项分解不可直接观察，long-span变化慢是拟合假设，不授已识别真实语义。stageII不是任意并行全canvas一次commit；预算MAX_GEN与停止逻辑不可从摘要理解为无限生成。

LLaDA8B/1.5/MoE7B、Dream/DreamCoder7B，HumanEvalInfilling/McEval四语言及GSM/MATH等；T0.2/p.9，原fixedmask64与dynamicMAX128是不同capacity；variablemethods尽量同adjustmentbudget但不等forwardcount，FlexMDM引用originalnumbers、DreamOn仅DreamCoder且initmask1改变运行点。AppB披露std<0.5但重复数/CI与hardware/precision/SLO不披露，不能直接授跨model可靠。AppG 1033instances forwardcalls/generatedtoken均值3.66/4.89/5.12，尾最大32.83/27.67/31.14，不是只有1forward或总时间常数；此calls只lengthsignal probing/search，tokencommit成本口径另辨。仅报告这一受限代理/动态canvas替代设计，不采本文“modest overhead/always reliable”普遍保证，不因未有paperrecipe造Books差异。精确原文在[feb11_AB2_core0](../_sources/daily-20260211/feb11_AB2_core0.json)，日期dates3包络落窗。

### [The Value of Variance: Mitigating Debate Collapse in Multi-Agent Systems via Uncertainty-Driven Policy Optimization](https://arxiv.org/abs/2602.07186v1)

多agent趋于一致不等正确→以flip、pairwise disagreement、output entropy/leave-one-out uncertainty作UDPO reward→重新选择debate的稳定/多样性压力。精确v1 §3–5及必要配置（[conditional_core](../_sources/daily-20260211/feb11_conditional_core.json)）：五backbone、GSM8K/MathQA/FOLIO，五agent/五round，reward混合稳定、agreement、system项和任务majority correctness，KL/clipping约束更新。高低uncertainty与accuracy的相关、consensus penalty收益不能分离不确定性相关与抑制正确少数：没有独立控制的错误共识/正确minority反侧，低uncertainty不是真值。hardware/precision/独立runCI/SLO未披露。只保留所测uncertainty/reward诊断，不采用共识正确性/跨模型通用防collapse策略；root已批准此限定仅报告处置。

### [Is there “Secret Sauce” in Large Language Model Development?](https://arxiv.org/abs/2602.07238v1)

同compute能力差距常被归为未公开recipe→809非reasoning模型、developer fixed effects与harmonized benchmark的观测分解→重审由公开compute估计推训练预算的证据权限。精确v1方法/robustness/eval已读（[conditional_core](../_sources/daily-20260211/feb11_conditional_core.json)）：MMLU-Pro5shot/TIGER部分作者自报，MATH0shot Epoch与4shot HF口径不完全统一；6ND compute中部分LifeArchitect估计；排除10reasoning模型、无inference compute，FE进入规则>3models/performance30或知名前沿厂商。季度控制与robustness不消除selection、数据质量、compute估计误差和未观察训练recipe混杂；80–90%描述性方差与40×不能解释为可执行因果降本。仅报告公开观测数据/估算/FE的限定诊断，不写未披露secret recipe；root已批准此限定处置。运行硬件/precision/SLO不适用于该观察分析，实际训练成本未核。

### [When Is Enough Not Enough? Illusory Completion in Search Agents](https://arxiv.org/abs/2602.07549v1)

答对不等约束核验完成→Epistemic Ledger分开可见证据E(Satisfied/Refuted/Unknown)、trace推断的B(Affirm/Deny/Unaddressed)与candidate状态→重审accuracy作为搜索停止充分条件。精确v1 §3–5、A.2/A.4/A.5及必要B段（[AB2 core1](../_sources/daily-20260211/feb11_AB2_core1.json)）：B是文本代理，不是直接读内部belief；posthoc gpt-oss120b judge定义under-verified/stagnation等指标，在线LiveLedger只把E送下一轮，ReAct同model更新、Tongyi另用gpt-oss20b。215MCP筛题取DAG width≥3/depth≥1/English，Serper/Jina top10/100turn/browse8000char；max8192/T1/p1、16A10040GB两周、vLLM eager，但baseline工具不同。GPT5判最终accuracy、gpt-oss ledger不是独立gold。人工只30题且限定少于6toolturn，93%一致/κ.74不能认证所有长轨迹。ReAct120 accuracy39.1→50.7同时UAR76.3→49.8为局部结果；ReAct20 stagnation34→42、bareassert/refutation负侧仍在。TTS强制search不匹配ledger额外LLM调用/token/时间，少turn不等净降本；SLO/precision/CI未披露。仅报告这一局部评价盲区与trace分类，不把judge状态当真实完备证据或内在信念；没有稳定、独立校验的通用停止policy差异，不强写Books配方。

### [Gaussian Match-and-Copy: A Minimalist Benchmark for Studying Transformer Induction](https://arxiv.org/abs/2602.07562v1)

离散重复token容易隐藏检索学习条件→Gaussian correlation匹配并复制successor、PTH/IH score与loss drop并发→重新比较attention/nonattention内容检索与学习动力学。精确v1 §3–4/A.1–A.2/B/C、D.4 assumptions与E.2（[AB2 core1](../_sources/daily-20260211/feb11_AB2_core1.json)）：默认2layer/小d16–32/T8–16，RTX4050/PyTorch2.6/Transformers4.49/CUDA12.4，AdamW、512batch；test128新Gaussian sequences。非attention对照参数2.47–3.10M、22.8–25.6GFLOPs为近似而非相等，2000steps同LR，扩20000steps改变cosine轨迹，finalloss可比但早期curve不直接匹配。Omniglot仅单exemplar、query复制两示例之一、随机label和disjoint class，冻backbone重新适配embedding；3×fine-tune FLOPs不包含GMC预训练总代价，不证明自然语言ICL普遍迁移。理论是noiseless exactmatch/copy、冻PTH和WV、直接优化mergedWKQ；A1–4 geometry、MSE→0/square-summable gradients及A7–9 prefactor稳定、offdiag drift、support domination均为条件，E.2坏sign mass<ε总体且ε<1/2。不证明任意GD都入该regime；某run方向仅.8–.95、全模型loss drop成因仍open。precision/重复runCI/SLO未披露或理论不适用。仅报告有限benchmark与条件性学习解释，不将已借用PTH→IH成熟机制或条件定理外推为实际LLM普遍优化规律；不遍历proof。

### [ViCA: Efficient Multimodal LLMs with Vision-Only Cross-Attention](https://arxiv.org/abs/2602.07574v1)

统一visual/text selfattention每层反复write→去visual queries/FFN、静态visual KV只于选层供text读→重新选融合深度/视觉写入/regular kernels，非新crossattention名词。精确v1 §3–5/C.4（[AB2 core1](../_sources/daily-20260211/feb11_AB2_core1.json)）：LLaVA1.5 3/7/13B，standard两阶段同iteration从scratch retrain，训练A100；TF直接冻结FFN相对质量71.2，重训99.2，不能当training-free删路径无损。ViCA7B九bench相对平均97.8%，TextVQA58.2→55.5，部分task退步；24是FLOPs equivalent visual tokens，不是实际24tokens/全compute仅4.1%。5000TextVQA/A6000/FlashAttention，7B prefill124.5→36ms约3.5×，batch8约10×forward，不报告decode/output/服务SLO，CI/precision Not Disclosed。C.4 eager显式mask与FA2.1 bottom-right causal mask导致system token稍多看visual，质量minor degradation保留，不能授语义完全等价/任意runtime兼容。仅报告此需重训的局部read/write与kernel取舍，未证其他MLLM/长多图下稳定且缺matched end-to-end quality/cost，不写无条件替代统一attention的长期结论。

### [Learning to Self-Verify Makes Language Models Better Reasoners](https://arxiv.org/abs/2602.07594v1)

生成更好不等判错更好→仅verification GRPO后回到generation的反向迁移对照→重新考虑两objective的阶段/交替分工。精确v1 §2–4及Tables1–4（[AB2 core1](../_sources/daily-20260211/feb11_AB2_core1.json)）：Qwen2.5 1.5/3/7B、DAPO17K、6math suites、verl，1000steps/B128/G8/max10240/T.6/p.95；onpolicy生成正确性由reference rule verifier提供，丢malformed/overlong/allwrong题、强制正负平衡后取B verification批，不等纯无外部generation supervision或相同采样人口/总compute。Avg@16不是best-of16；7B avg38.9→38.4而tokens4458→1152，AMC65.3→59.7/AIME25 18.1→11.7是关键反侧。GPT4.1改写1545corrupted prefixes提高恢复，不独立识别“更精准触发内部验证”因果；Table3 base/Generate加验证有退步，selfverify组局部改善但增加候选/判定预算。Init400verify+600generate与Alter1000steps不匹配实际总rollout/token，hardware/precision/CI/walltime/SLO未披露。只采有限任务生成/验证能力非对称与objective局部取舍，不能推出same-model judgement是真值、所有任务更好或端到端省75%；仅报告受限训练替代证据，不强补未识别的普遍自我纠错机制。

### [Astro: Activation-guided Structured Regularization for Outlier-Robust LLM Post-Training Quantization](https://arxiv.org/abs/2602.07596v1)

uniform weight幅度regularization忽略激活耦合→group activation norm加权L∞、layer reconstruction后接GPTQ→重选outlier压低与原质量的准备成本。精确v1 §4.1–4.3/§5.1–5.4（[AB2 core2](../_sources/daily-20260211/feb11_AB2_core2.json)）：这是PTQ预处理不是pretraining optimizer/QAT训练目标；局部quadratic与忽略interlayer的H≈2XTX假设不能授全model严格等价。LLaMA2 7/13/70B，W2A16g64/W3–4A16g128，128WT2calibration×2048token，200PGD/layer、β需调，A100；Table1部分baseline来自旧作者论文，不同训练预算/实现版本不能全部直接归因。β5e-4时PPL34.91崩溃，70B MMLU Astro66.9<Omni67.3、7B Hella72.2<Omni73.4，非全面最优。unquantized重构PPL+0.00–.02只该指标近似保真，不证明所有任务严格等价。Figure3为7B W3A16g128 total quantization time/PPL，half-time不外推部署吞吐或zero总成本；硬件数/CI/precision以W/A口径外其余Not Disclosed。仅报告此局部prepare路径与风险，保留原PTQ/未经重构权重，不把flat theorem升级为全模型无损保证；root准入纠正与限定处置均已通过。

### [SERE: Similarity-based Expert Re-routing for Efficient Batch Decoding in MoE Models](https://arxiv.org/abs/2602.07616v1)

top-k少不等batch少expert且删次expert会丢输出→校准expert activations similarity，保留batch所有topS primary、secondary只在≥ρ时转向其最相似primary且不改router weights→重新选skip与reroute的质量/访存权衡。精确v1 §3–4/B.1–B.3/C.2（[AB2 core2](../_sources/daily-20260211/feb11_AB2_core2.json)）：FineWeb400×128，Frobenius最快28s，CKA-RBF16064s是额外prepare成本。Qwen1.5-MoE/DSV2Lite/Qwen3A3B singleH20/vLLM，5000requests固定128/32、QPS8–32测TPOT；accuracy另OpenCompass八任务，model专属T/p、batch16/maxoutput1024或2048。Table3 Qwen3top2ρ.5 avg80.37<82.24、MBPP72<78.4，top1 avg64.11更差；Table1Qwen1.5top2 avg47.25<48.52，不采“各任务97%/无损”概括。ρ高减少可skip专家、speedup明显降，critical仅similarity代理并非正确性认证。prefill compute FLOPs不降、TTFT边际收益，不能把固定短input decode加速当所有阶段；precision/version/CI/SLO未披露。仅报告局部kernel/selector替代与阈值反侧，不授生产一行集成正确性、EP通信或跨校准普遍可靠。

### [Agent-Fence: Mapping Security Vulnerabilities Across Deep Research Agents](https://arxiv.org/abs/2602.07652v1)

不安全文本评价会漏动作/权限/持久state→固定Qwen2.5-32B与91HotpotQA多turn workload，trace-evidenced boundary predicates、AL区分task error与attack-linked deviation→需重审能力错误是否足以定安全break。精确v1 §3–8/§9（[AB2 core2](../_sources/daily-20260211/feb11_AB2_core2.json)）已深入必要命题：UTI/UTA/WPA/SIV/ATD，AL基于非可信内容跨trustedge；明确case规则、两人adjudication/20%sample κ.81。八archetype，SC threshold≥.30/default N≥30并提固定budget，具体frameworkversions/toolsets/budget数/替代model身份/hardware/precision/SLO未披露，artifact承诺uponacceptance不是可审实现，fixedmodel不是所有architecture因素被独立干预。

同精确v1中心冲突保留双证据：§3 Table2的DirectPromptInjection对八agent全部✓，按Table1须SC break≥.30；§8.1称A1/A2 prompt-centric SC aggregate低于.20，这与A1全八≥.30不能同时成立。§8 MSBR与ablation叙述不能修复该不一致，不能静默选有利一方或把std当CI。当前冻结本篇全部安全rates/排序/35% causal归因与Books采用；predicate定义只作为待核协议不采正面系统证明。重开只需同版官方更正的Table1/2/§8.1含聚合人口解释、或可追溯SC run traces/config；不必遍历全部攻击payload/附件。此为必要证据中心争议保留项，非普通未读。

### [From Assistant to Double Agent: formalizing and benchmarking attacks on openclaw for Personalized Local AI Agent.](https://arxiv.org/abs/2602.08412v1)

输出文本fail不等执行/持久fail→个人agent在先一步tool observation注入、后一步target skill及STM/LTM marker观察→需分账技能触发、marker写入/读取与实际损害。精确v1 §2.1–2.4/§3.1–3.2 Tables2–4（[security minimal core](../_sources/daily-20260211/feb11_security_minimal_core.json)）：blackbox用户/外部内容/serviceendpoint，排除OS/code/weight/systemprompt compromise；controlledsandbox canaries、131skills、Llama3.1-70B/Qwen2.5-7B/GPT4omini。Table2明确IPI Simulation ASR仅target skill call，RespRate任意skill；§3.2宣称actualTypeScript环境、只有tangiblepermission/exfil才success，不能用后段概括替换Table2分母。Table3/4明确Simulated、每类40cases，marker写效果filesystem验证是路径局部证据，非持久完整系统损害。N/T泛称固定但无数值、revision/precision/hardware/CI/costlatency未披露。保留prompt defenses残余trigger/marker失败，不把模拟与真实deployment混同、不把call当执行完成。只报告可核stage/marker路径及metric边界，不用这些rates授生产安全或缺recipe强写长期Books。

### [PARD: Enhancing Goodput for Inference Pipeline via ProActive Request Dropping](https://arxiv.org/abs/2602.08747v1)

已超时才drop浪费前段计算→计算后续stage预算、在当前batch前拒绝预计无效请求→重新选整pipeline goodput而非每模块FIFO指标。精确v1 §3/§4.1–4.2/§7 Table2/Fig15（[security minimal core](../_sources/daily-20260211/feb11_security_minimal_core.json)）：DNN以recent5s queue/offlinebatch profile/10k arrivals采样quantile估batchwait，λ.1是heuristic，不授弱相关CLT必适用所有请求。LLM case实际2A10080GB/vLLM0.9/LangChain，10kHotpotQA Azuretrace、Llama3-8B rewrite→FAISS483k与Tavily并行→generate，TTFT SLO5s。customproactive以rewrite/search recentavg、generate inputlen/offlineprefill估算，reactive仅过TTFT后drop；作者drop降低22%但仍17%，oracle用T0offline outputlen降至11%明确不可线上取得。continuousbatch不含DNNbatchwait、rewrite输出长度和searchtail不同，不能照搬DNN64GPU goodput或HBF/LBF优先级claim。accuracy/precision/repeatedCI/overallbusinessdropcost未披露，TTFT不是全部answerdeadline。仅报告局部LLM管线预算/drop-too-late取舍，未证开放agent效用/模型质量，避免DNN类比替代实际LLM适用证据。

### [Debugging code world models](https://arxiv.org/abs/2602.07672v1)

dense state trace失败常被称state tracking失败→S5 groundtruth action teacher forcing与local datatype分解→需拆action生成、transition/state、截断成本。精确v1 §2–4/§6/C/D（[AB3 core0](../_sources/daily-20260211/feb11_AB3_core0.json)）：CruxEval800/HumanEval723 fixedprogram+input执行探针而非新代码生成，8Kbudget；7nonstring类别各10depth5为100%不证一般语义全可靠，字符串筛25函数中15atomic≥90%、每depth100，depth2 75%→depth5 25%，另4Kbudget，人口不同不叫完全类型因果。语义保持decomposition仍仅小幅改善且膨胀trace；BPE token缺对应字符与失败一致，但未做替换tokenizer的受控因果。S5 8–128op、CWM原生trace/GPT5仅最终assignment接口不同，teacherforce每步注入正确operation仍由CWM预测state，128steps90%非100%/超128保证，正确action是oracle条件不是部署能力。model checkpoint/parameters/hardware/precision/temperature/repeatedCI/SLO及S5样本数未披露；未来开源不是已审artifact。仅报告受限failure定位与oracle诊断，不让条件state能力变成自执行/内在验证安全承诺；不将初级token机制当新普遍理论。

### [Blind to the Human Touch: Overlap Bias in LLM-Based Summary Evaluation](https://arxiv.org/abs/2602.07673v1)

judge selfprefer常被归为模型身份/质量→换序双判与reference ngram overlap切片，加入保留长短语的rephrase→重新验evaluation人口与position偏好。精确v1 §2–5（[AB3 core0](../_sources/daily-20260211/feb11_AB3_core0.json)）：WikiSum276/CNN286由95–105spaceword humanreference过滤、generated提示100word非实际全部等长；6744summaries/94Kjudgements、5generators9evaluators，GPT4omini参数未知不能采用表中8B估计。T.7、无history，换序若不同标tie并分first/last；把BLEU1/4+ROUGE1/2均值作相似度、后段用humanGT提供给rephrase扩高overlap，population与information不同，不是同质量独立干预。judge偏generated在低overlap多，positiontie在高overlap多；但没有独立humanquality评价证明humanreference必更优，也不证识别作者/参数量导致偏差；单reference、句式/content/length残余混杂保留。precision/device/重复CI/providerrevision/SLO未披露。仅报告所测choice pattern与swap/overlap切片，不能当human-touch普遍失败、可靠检测LLM或公平qualityranking的新规则。

### [ParisKV: Fast and Drift-Robust KV-Cache Retrieval for Long-Context LLMs](https://arxiv.org/abs/2602.07721v1)

CPU检索与旧centroid drift成本高→SRHT normalize/rotate的解析centroid投票+4bit校准rerank/CPU fullKV UVA只取top100→重选index/retrieval及HBM/transfer取舍。精确v1 §3–5（[AB3 core0](../_sources/daily-20260211/feb11_AB3_core0.json)）：coarse directionproxy不能保持raw-score排序，rerank的w保存原keynorm/subspace radius/α，非删norm直接等价；Haar orthogonal Beta theorem≠实际SRHT自动严格Haar，α校正为approximation不授exactattention。新tokenbuffer增量编码和CPU backingstore/metadata仍长大，unboundedgeneration不等常数总memory。Qwen3 4/8B/DSR1Llama8B，AIMEpass@8与MATH/GPQA pass@1不合并；PQ20%budget/MagicPIGdynamic/Paris100不同，部分AIME与LB低于dense：Qwen4 AIME80<86.67，Qwen8AIME73.33<83.33，LB33.07<33.59。性能另Llama3.1/Qwen8、64K–1024K不同batch可运行点，较大batch部分来自offload容量；1024K49ms vs2179为decode而非TTFT/fullcompletion，prefillbuild/offload不能略。hardware/precision/runtimeversion/outputlength/CI/SLO Not Disclosed。仅报告局部coarse-to-fine取舍，不采milliontoken无损/生产延迟保证。本窗处理v1；AB中的v2提交Tue10日16:05UTC按公告政策最早公开恰到本窗终点，不是本日事件，不由版本号追加旧新版深比较。

### [Learning to Continually Learn via Meta-learning Agentic Memory Designs](https://arxiv.org/abs/2602.07755v1)

手写memory固定store/retrieve→code general_update/retrieve设计archive、按score/visits探索，再测收集与部署分离→重选memory结构与搜索/运行成本。精确v1 §3–5/A.3/B.3/B.4（[AB3 core0](../_sources/daily-20260211/feb11_AB3_core0.json)）：GPT5medium meta、GPT5nanolow固定agent，11steps43design；greedy43steps相同design数量非相等完整model调用/rollout总费用。学习static部署减少variance，best设计再heldout测试三runsSE；GPT5mini transfer与collection70validseen→dynamicunseen只ALFWorld，不称all-domain continual在线学习。四textgames，nano平均6.1→12.3、greedy11.9vs12.4差别未授显著；miniALMA53.9平均但Baba33.3<DynamicCheatsheet38。$0.09只是memory FMs从rawlogs到存储/检索的累计费用，不包括meta设计搜索、原agent收集trajectory或最终agenttokens；bubble仅retrievedtoken proxy。Python Turingcomplete searchspace≠有限11轮能找到任意设计，sandbox/人工oversight不证自动安全。device/precision/SLO/version/独立训练replicas Not Disclosed，作者API结果非复现。仅报告offline局部设计探索，未证在线权重continual learning/任意域无预算适应，不因缺ALMA配方强造Books diff。

### [Rolling Sink: Bridging Limited-Horizon Training and Open-Ended Testing in Autoregressive Video Diffusion](https://arxiv.org/abs/2602.07775v1)

5s训练的AR视频cache用于长rollout漂移→低漂移首K历史块作sink，重编号为近邻RoPE index，再正反周期rolling语义→重选静态锚点/滑动历史维护，2+1+2=5。精确v1 §3.1–3.2/§4/Tables1–2/0.G：[AB3 core1](../_sources/daily-20260211/feb11_AB3_core1.json)。Self Forcing/Wan/CausVid、K6/S5、每block3latent、4step diffusion，无重训；固定sink稳定色彩仍flicker/repetition，rolling是within-duration内容近似重播，不真实无穷世界状态。LongLive主表不加载其1min LoRA以对齐5s训练，非各方法最佳部署全等预算。16A40/eightweeks，每dimension10prompt一次固定，1/5min clip_length2/10；repeat/CI/precision/分辨率/每步latency/SLO Not Disclosed。5min subject .9804高但human action .8710<LL .9548、dynamic .6411<.7379、appearance .1891<.2086。30min只是定性例图，正文限定single-shot固定prompt，不能持续引入新语义，cacheproperties非穷尽。仅报告局部维护/重播取舍，不授无限rollout或exposure-bias消除，不混同persistent world state。

### [MaD-Mix: Multi-Modal Data Mixtures via Latent Space Coupling for Vision-Language Model Training](https://arxiv.org/abs/2602.07790v1)

人工mixture/missing-modality难对齐→各域均值embedding构造K，共享dual alpha=(sumK+lambdaI)^−1 delta，delta计可用模态/missing零，alignment softmax配比→重选估计/训练预算，2+2+2=6。精确v1 §3/4/B.2–B.6：[AB3 core1](../_sources/daily-20260211/feb11_AB3_core1.json)。ridge consensus是构造代理而非taskloss最优；大eigenvalue被解释为signal不普遍证明。stage1.5 LLaVA每dataset512样本平均再domain平均，域内按dataset size抽样，5域2模态/6域3模态，固定非online漂移自适应。0.5/7B batch128/seq8192/LR1e−5/cosine，4500或3000steps，评价3seeds std不是训练replica CI。singleH100 embedding .58h+score .01h另计，training90/620GPUh；56%/78%/33%steps匹配平均quality非完整walltime加速。0.5B avg38→39.24但InfoVQA22.25→22.13/MMMU30→29.78，7B Realworld58.17→57.47；Qwen2B transfer不授全architecture。部分原data未发布，precision/runtime/SLO未披露。仅报告少域/阶段模型代理配比，未识别可通用修正长期mixture选择的真实最优条件，不因缺paperrecipe造diff。

### [Emergent Structured Representations Support Flexible In-Context Inference in Large Language Models](https://arxiv.org/abs/2602.07794v1)

表征相关不证明功能中介→GCCA共享子空间/等维random对照，clean→corrupt投影patch、ablate/isolate与crosscontext Procrustes→重审结构表征证据权限，2+1+3=6。精确v1 §2.1–3.2/§4.1/§6/B.1–B.3：[AB3 core1](../_sources/daily-20260211/feb11_AB3_core1.json)。pretraining-only Llama/Qwen base，THINGS1854concept reverse dictionary，20%为1–48demos/余test，5独立demo抽样与10000bootstrapCI非5次训练。SVD95%、ridge .01/rank500permutations，geometry依赖选layer/query分布。description/label/query corruption，CIE是correcttoken logprob恢复不全生成质量；Llama70B24demos中层description/label90.92/87.81%恢复，final层下降、ablating未全崩表明冗余，isolate非所有层充分。crosscontext训练query学习orthogonal transform、heldout测，不未校准任意concept迁移。hardware/precision/计算成本未披露，SLO不适用机制探针。仅报告受限任务的条件干预，不授allreasoning/唯一substrate或通用symbolic机制。

### [Thinking Makes LLM Agents Introverted: How Mandatory Thinking Can Backfire in User-Engaged Agents](https://arxiv.org/abs/2602.07796v1)

thinking默认提升agent→mandatory think函数/单行Thoughtprefix的局部失效与disclosure对照→重选用户交互/内部reasoning，3+2+2=7设计反证深入。精确v1 §3–6/Tables2–4/A.1–A.2/A.6：[AB3 core1](../_sources/daily-20260211/feb11_AB3_core1.json)。7models，Retail115/Airline50/TSPhone224，database Pass@1与milestone ROUGE/AST不合并。function highest-priority mandatory，额外调用/预算未matched；TaaP Table6 GPT5 Retail+1.74/Airline+2、gptoss Airline+16反侧，不概括allthinking伤害。≥150tokens/disclosure由GPT4.1注释，人工20trajectory/1060atomic仅DeepSeek，均值一致非全gold/causalmediation，case选think失败/nonthink成功。Table3 GPT5/Gemini长响应差未显著；cost/hardware/precision/T/maxoutput/providerrevision/repeatCI未披露。InfoDis加vanilla而非thinking×disclosure matchedfactorial，DeepSeekAirline baseline52与Table2 54.17不同，不当同对照因果反转。仅报告mandatory交互反证，不授减少披露唯一原因或普遍补救recipe。

### [rePIRL: Learn PRM with Inverse RL for LLM Reasoning](https://arxiv.org/abs/2602.07832v1)

专家step标签/可执行expert policy昂贵→IRL中policy sampling估partition，以importance correction交替训练token PRM/policy→重选监督与采样成本，2+2+2=6，受影响公式纠错深入。精确v1 §3–5/C.1–C.2：[AB3 core2](../_sources/daily-20260211/feb11_AB3_core2.json)。无需访问expertpolicy/reward不等无需expert数据：math/code各7000、Claude3.7每题4trajectory，主表ORM+PRM（1:.05/.1），algorithm1 ORM把correct policy追加pseudoexpert/只failed作policy，PRM-only另受限对照。self-normalized finite sampling非真partition/原reward唯一identifiable证明；Theorem1 soft-optimal policy明确成熟结果，不当新贡献。保留公式双证据：§3.2 Eq6 E[r]+βH 与下一行+βElogπ符号相冲突，§4另披露entropy loss .001；冻结熵补救recipe，重开只需官方Eq6/implementation entropy符号说明，不扩全部proof。Qwen3/4B两阶段math→code、PRM同base、8RTXPRO6000/VeRL，AdamW batch128/RLOO4rollouts/2epochs/2050valid挑best/greedy0shot。Table2 Qwen3MATH72.8<RLOO73/LCB27.5<SFT28.8、Qwen2.5LCB20.3<PRIME20.4；C.2去correct-pseudoexpert Minerva31.6>27.2，非所有列winner。13.3h vsPRIME14.6是3Bmath训练不含专家收集/全workflow；AppB maxprompt1535/maxresponse3000，TTS另T.8；precision/精确version/CI/SLO未披露。只报告有限importance/监督对照，不采用泛化最弱假设、无外部信号或唯一latentreward恢复与争议熵公式，不强写Books。

### [TodoEvolve: Learning to Architect Agent Planning Systems](https://arxiv.org/abs/2602.07839v1)

手写固定planner架构→PlanFactory四接口(topology/init/adapt/nav)生成code，bootstrap执行过滤、SFT+IGPO偏好以success先行/impedance成本tie-break→重选架构搜索/执行预算，2+2+2=6。精确v1 §3–5.5：[AB3 core2](../_sources/daily-20260211/feb11_AB3_core2.json)。Qwen3-14B/Gemini3Flash teacher+judge/DSV3.2executor，SFT3360/IGPO2000、context~13k，取3结构参考、Kcandidate数量/训练硬件precisionLR/重复CI/runtimeversion/SLO未披露。IGPO本体DPO logratio，impedance总cost×exp(error/stability/planningratio)为构造指标，不证明真最优；answer过滤不认证架构安全/全执行正确。Table3混pass@1/2/3与不同model不全部可比；同SmolagentsGPT5mini局部收益仍额外meta-planner/reference/search成本不同。Table4 KimiK2 WW70%但time216.59>Joy212.83/Flash164.78，DeepSearchcost.0495>.0454/time875.26>多数，GAIA323.65高；不是普遍Pareto占优。§5.5ZeroShot有IGPO但无fewshot，full增加steps/cost，数据合成/训练/失败候选总预算没matched。仅报告新code-config局部探索，不将预定义四接口翻成自主全安全architect或普遍更省，未形成可直接写Books的长期最优选择。

### [Recurrent-Depth VLA: Implicit Test-Time Compute Scaling of Vision–Language–Action Models via Latent Iterative Reasoning](https://arxiv.org/abs/2602.07845v1)

固定depth/action-token成本→8query latent scratchpad、weight-tiedrecurrent core持续注入Prelude/vision/proprio、TBPTT末8步与随机recurrence→重选latent迭代深度/stop/动作horizon，2+2+2=6。精确v1 III–V/TablesI–III：[AB3 core2](../_sources/daily-20260211/feb11_AB3_core2.json)。MiniVLA Qwen.5B/冻结DINOv2+SigLIP，64latent/512visiontokens；random lognormalPoisson均值32、noisyinit，action相邻MSE阈值只被称KL近似，不真实calibrateduncertainty或每步严格更好保证。LIBERO fixed1→8/12改善但24avg93.1→32的92.1，adaptive7.93iter92.5对12iter93；34%少recurrentstep非全VLM/actionwalltime34%。binary/linear执行horizon同时改变故非只stop控制；大阈值1e−2 avg72.1，fixed/adaptive各subtask有回退。CALVIN3.39与其他backbone/recipe不同，非14×size导致更快因果；realYAM四任务progression score而非uniform完整success，adaptivefold劣。训练预算/episodes/repetitions/hardware/precision/latency/controlHz/CI未披露；memory常量限inference scratchpad/weight而非训练allstate，operator assistance/safetythreshold留future。仅报告局部latent与深度边界，不把收敛当安全/不采无条件arbitrarilybetter或order-magnitude端到端speed。

### [Geometry-Aware Rotary Position Embedding for Consistent Video World Model](https://arxiv.org/abs/2602.07854v1)

screen-space历史难回访→intrinsic ray/local+camera rotation旋转Q/K子通道，stochasticframeaffinity topk取历史→重选几何index/texture与loopclosure取舍，2+2+2=6。精确v1 §3/§4.1–4.4/A.1/C.3–C.5：[AB3 core2](../_sources/daily-20260211/feb11_AB3_core2.json)。WAN2.2TI2V5B、480×832/61frames/batch64/LR5e−5/6k/16A100约2days，CaM/GFMC/ViewBench1:1:1；61→201frame再6k/2k稀疏训练额外计，teacherforcecleanKV训练vsgeneratedKVtest。公式ray与rot编码角度，不直接含平移/深度，looploss为问题形式并未pixel优化。10UE5same-scene，1059训练/~500kframes含rotation+translation；600独立trajectory评价仅纯rotation、16FPS/61frames，不新scene实际navigation保证。samechannels budget局部对比GTA；HY/Matrix另baseline只yaw/pitch、本文full含roll，不能当全同人口，frame Ks10/topk5/current保留，random/exclude-selected LCE .7027/.7744 vs .5609支持局部历史选择，不证明每个selected因果必需/完整物理state。180deg PSNR14.35<Sliding14.44，原RoPE替换或全通道loss更坏；k更大纹理改善但LCE在traink5最优。27.66→22.01s/iter是训练不实时inferenceSLO、precision/repeatCI未披露，全historycache/打分成本不等constantmemory。仅报告已知pose/旋转局部证据，不授完整3D/persistentworld无漂移或productionstreaming保证。

### [Anchored Decoding: Provably Reducing Copyright Risk for Any Language Model](https://arxiv.org/abs/2602.07120v1)

tokenizer不齐/双模型安全约束难落地→每步KL预算的geometric logitfusion与BPE诱导nextbyte分布→重选reference依赖/质量/执行成本，2+2+3=7安全深入。精确v1 §2–5/A.3/B.1.3/D.1–D.2/D.5：[security core0](../_sources/daily-20260211/feb11_security_core0.json)。Thm3.1条件是所有prefix真实next-tokenKL可行、shared support、预算和≤K/有限Tmax，不法律不侵权保证或任意解码后处理保持bound。主Prop3.4写≤K−δ而B.1.3实际证明≤max(0,K−δ)≤K；δ定义无≤K约束，所以只保留后者，不能静默删clamp或采用更强负数上界，定点官方Prop3.4澄清可重开。ps已知permissiveprovenance为假设，latent leakage/nonzero baseline/rare facts suppression正文明确；NCR六overlap proxy相对ps normalize、不infringement判决。16CopyBenchnovels/BiosFActScore、六base-model pairs、3samplingseeds std非CI，T.7/reppenalty1.1或1.05/Tmax200/Bmax800/n5。CPFuse本来disjoint同utility而使用不对称pair，对照失配保留。2H200140GiB timing first50prompt、batch1/3runs：token约1.1×slower；byteprefixdebt TTFB3566.8vs186.3ms、shard/tree成本大，byte限200不同800quality。precision/SLO未披露，未核可执行实现/安全anchor资料完整性。只报告受限KL机制/成本，不采用copyright-safe、generalprivacy guarantee或未独立复核的普遍最优decoder知识。

### [Rethinking Latency Denial-of-Service: Attacking the LLM Serving Framework, Not the Model](https://arxiv.org/abs/2602.07878v1)

longgeneration只测攻击自身延迟→共机CB小HOL但HBM争用与KV容量边界触发admission/preemption代价→重选资源隔离评价，3+2+3=8安全深入。精确v1 §3–7/A.1：[security core0](../_sources/daily-20260211/feb11_security_core0.json)。标准blackbox tenant/API concurrency，无weight/runtime权限，但无inputfilter；LightGBM pretrained load探测的训练标签来源/transfer误差未充分交代，不授零校准所有API。vLLM0.11.2/Qwen3-8B/Gemma12B/DS8B、single到TP2/4/8、8L40S48GB/PCIeGen4/CUDA13/PyTorch2.9/90%memory。PoissonAlpaca/ShareGPT与BurstGPT三个时段模拟，不真实全cluster/crossprocessattack验证；攻击baselines固定interval vs stateadaptive预算非完全matched，美元按GPT4omini价估非实际openmodel租赁全成本。50%以上恶意率常是性能拐点，不任意少恶意都742×。TP4降低/TP8低load可抑制反側，高load>80users再升；DSreasoning plain自身1.1s低于Extend10.99，不都更强。P99非worst-case上界，Table2标seconds却整数11046对应正文11.046，按正文ms转换不混单位；precision/inputoutput分布/RPS/repetitions/CI/SLO未披露。只报告受限version/load资源反证，不外推所有SGLang/TGI/TRT实际验证、production guarantee或通用防御；scheduler伪代码未当实际code核验，禁止部署攻击。

### [The Judge Who Never Admits: Hidden Shortcuts in LLM-based Evaluation](https://arxiv.org/abs/2602.07996v1)

judge rationale声称content-only→六synthetic元数据cue在同response交换位置、比较verdict与CAR承认→重审理由忠实证据权限，3+1+3=7设计反证深入。精确v1 §3–4/Limitations：[security core0](../_sources/daily-20260211/feb11_security_core0.json)。ELI5/LitBench各100pairs/前者length±20%，6judge/T0/p1/fixedseed，humanfilter非truequalitygold，JSON“reason”只是短可见解释非完整内部CoT。§3.7 VSR定义逐itemchange比例，Tables2/4–6却signed first-selection-rate difference；不能将净差当所有itemflip，所谓gender±6/ethnicity轻微差只局部非无偏证明。CAR未披露全自动/人工标注流程及一致性、低CAR不证明model consciously ocult/内部不知，highCAR不debias，Gemma/Qwen ELI5高但Lit低反側。source/recency/education有局部cue方向差，来自固定单轮文案无uncuedmatched/重复CI；hardware/precision/providerrevision/成本SLO未披露。只报告可见cue-swap/解释不提及的评价反侧，采用signed净差口径，冻结逐项VSR/faithfulness因果；不授judge公平性、解释可认证或某author身份真实识别。

### [Position: Stateless Yet Not Forgetful: Implicit Memory as a Hidden Channel in LLMs](https://arxiv.org/abs/2602.08563v1)

API无session不等无state载体→输出被后续重注入时携8bit编码并OR累积触发→重审derivedartifact跨请求信任，3+2+3=8安全深入。精确v1 III–V/VII-A–D：[security core0](../_sources/daily-20260211/feb11_security_core0.json)。必要前提reingestion，无weight更新/crossaccount暗memory；prompt植入需第三方systemprompt控制，finetune需训练数据/模型分发控制，organic仅future假说。GPT4o合成6000query/rejudge同GPT4o作标签×5randompriorstate=30K；prompt999各333setting/propagating/all-setactivation非实际长序列任意部署轨迹，finetune75%+41kAlpaca/test25%。success仅payload string出现非真实财损，benign10kAlpaca loss差<1%非全部utility。state精确传播仍错误，reasoning高performance非internalmechanism已核，API不可见reasoning。clean/paraphrase全移zero-width；semantic100已给targetbit生成样本joint98→95%保存，与真正模型产编码joint仅18%不同，不合成隐蔽可靠channel。hardware/precision/训练budget/APIrevision/T/CI/运行cost/SLO未披露。仅报告受控植入与再注入路径及防御取舍，不写有机记忆已存在、跨请求无载体持久或普遍不可清洗安全结论。

### [Sparse Models, Sparse Safety: Unsafe Routes in Mixture-of-Experts LLMs](https://arxiv.org/abs/2602.08621v1)

默认top-k安全不代表所有可执行route安全→固定expert权重下路由mask显著改变拒答及任务utility→重审内部routing权限与alignment覆盖，3+2+3=8安全深入。精确v1 §3/4/5、AppC/E/F/G、Table10：[security core1](../_sources/daily-20260211/feb11_security_core1.json)。RoSais以20随机mask的affirmative首token概率差定位router、再100mask搜索1/2/5层；F-SOUR逐token/layer10随机化、5次GPT4omini shadow judge restart，最后GPT4o完整unsafe judge。攻击要求白盒routing分数读取和执行时改mask，没改expert权重不等普通输入攻击可达；不是闭源API突破。四个明确checkpoint的DeepSeekV2Lite/Mixtral8x7B/OLMoE1B7B/Qwen1.5MoEA2.7（默认shared/topk，T0、原chattemplate）；JailbreakBench/AdvBench既定subset，具体subset数量未披露，不据此补造N。AppC同DeepSeek随机mask弱于RoSais，dataset route同集优化/测试与跨集结果分账：5层Jailbreak .79→.69、Adv .90→.86；不是任意数据universal。Table1 OLMoE sample-level .50→.51→.45非层数单调收益。GCG500step/64候选与TAP4×4×10、白盒其他baseline权限及预算不同，不采纯算法无条件更强。AppE禁5层各6/64expert降低GCG/TAP但不归零；AppF GSM8K基线.5610、5层攻击.3351/.3078、防御.5216/.5064有utility损失，prompt防御F-SOUR残余.90/.88。AppC A10080 timing仅1层、长度随tokenizer变化，DeepSeek~100s/Mixtral~528s非免费查询；precision/并发/ASR重复CI/SLO未披露。仅报告受限route-level诊断，冻结blackbox可达、通用脆弱/无损防御与未实测DSV3规模结论，不因安全关键词增加Books recipe。

### [On Protecting Agentic Systems’ Intellectual Property via Watermarking](https://arxiv.org/abs/2602.08401v1)

文本水印不直接覆盖Agent可见action轨迹→工具调用“等价类”分布偏置+用户pass集合可在仿制模型中留局部识别信号→重审watermark载体、sideeffect等价与归因误报，2+2+3=7安全深入。精确v1 §III/IV/V/VI/VII-A–E、TablesV–XIII：[security core1](../_sources/daily-20260211/feb11_security_core1.json)。已生成(a,r)在返回前替换action而保留最终r，不等改写后重新执行真实工具；VR厂商/PGR参数/IA版本地区/AE确认/CE copy-delete可有不同账户、权限、原子性、副作用。3673工具→207候选→LLM+execution sandbox101pass，2作者抽50无差异仅该验证范围，非所有真实工具等价。5–20pass指纹容量343B为组合数非实际已归因用户。JSD阈值+检测数≥3经验推荐，private同分布Dtest作为验证；同组阈值探索非独立校准，pass有顺序依赖且未证明联合FPR。xlam扩展30K/24Ktrain+6Ktest，Qwen3-4B/ReAct、QwenNext80A3B模拟工具、LoRA64/128/LR2e-4/4H800；DeepSeekv3.2 judge非人工gold。36正仿制、每域12负clean-finetune；50K指纹池仅12恶意模型+随机benign身份，Social定位.81/Ministral50K .87，不能称0.92–1.0普遍归因。TableV victim→imitator质量差可能reconstruction与watermark混杂，缺同样reconstructed-clean imitation对照；TableXIII δ0→5 TS .727→.671直接反侧，不能无损。替换/删token攻击F1是定位watermark tokens，不是成功去水印后模型检测率；FK仍.235且质量下降不证明任何攻击都无法清洗。GPT2 PPL相似≠任意检测器隐身。9.6/3428s、1000query仅insertion比.28%，不包括矿挖、1000GPUh仿制/完整归因、真实tool执行及全SLO；precision/训练步数、repeats数量/CI未披露。仅报告局部trace fingerprint与成本/归因边界，不采用法定IP/窃取判断、恒定隐身、全部副作用等价及上线保证。

### [CryptoGen: Secure Transformer Generation with Encrypted KV-Cache Reuse](https://arxiv.org/abs/2602.08798v1)

判别式HE批布局重处理前缀不适合AR→prefill outer-diagonal/decode inner-diagonal及mixed encryptedKV packing/延迟refresh/concat→重审安全生成的阶段layout、KV状态与交互成本，2+2+3=7安全深入。精确v1 threat model、§4.1–4.4、§5/6、Table3/4：[security core1](../_sources/daily-20260211/feb11_security_core1.json)。半诚实双参与方、client持key且不collude，排除恶意参与方/sidechannel/integrity；masked client decrypt-reencrypt刷新与HE↔MPC share转换依赖这些假设，未核artifact或安全proof复现。微软SEAL BFV/128-bit推荐、n8192/p约2^29/q约2^220 fixed-point、EzPC nonlinear；GELU仍局部4度近似，不能由MPC词称精确原浮点。GPT2base12层768/12head、CPU Threadripper3955WX16core/125GiB/Ubuntu22.04/gcc11.4、prefix64/output64–512逐token。BOLT适配以future placeholder+整prefix重处理，不是同样优化AR/cache方案，4.4–7.6×只该baseline/负载，不与plaintext实时LLM合并。Table3 PPL PTB53.65→54.64、其他两集约不变，未证明所有质量无损；Table4层总9.6→65.55s、QK .27→28.27s、部分短线性/GELU比BOLT慢，packed block/cache增长仍存在。正文“attention O(L) throughout entire decoding/constant memory”不采用：每步cache复用不消除查询所有历史K/V，总生成与cacheblock长度分账，不能由有限512观察获任意长序列保证。refresh<1%只本实验；网络RTT/bandwidth、batch/concurrency/SLO、fixed-point具体scale、重复/CI未披露。仅报告加密KV的有限实现取舍，不授恶意安全、通用端到端线性/恒定memory或生产可行性。

### [Aegis: Towards Governance, Integrity, and Security of AI Voice Agents](https://arxiv.org/abs/2602.07379v1)

数据ACL常被当整套Agent安全→同voice pipeline由raw records改query access后行为攻击仍出现→重审access权限与任务/行为policy各自防护目标，3+2+2=7安全深入。精确v1 §3.1–3.3/4/5、Tables3–8及AppA代表bank/IT prompts：[security minimal](../_sources/daily-20260211/feb11_security_minimal_core.json)。三模拟backend（bank/IT/logistics）、七QwenAudio/Omni与OpenAI/Gemini backbones、GPT4o攻击与transcript judge，同源自动judge非独立gold；五persona每scenario10attempt/≤10turn，§4称每model250interaction，Table小数的跨域/轮次聚合denominator未明确，不据此补造精确成功次数/CI。query模式Table4 auth/privacy标零是该模拟/预算观察非安全认证；privilege/poisoning/offtopic仍非零，GminiPro资源abuse .368→.480/GPT4o poison .048→.084直接反侧，并非所有metric随ACL单调改善。§3.3 leakage prose“正确拒绝”与公式“failed rejections”相反，采用Tables标为attack rates的局部方向，不采正确拒绝率或静默改公式；重开只需作者此字段/聚合分母更正。resource abuse定义offtopicinteraction比例不是实际HBM/CPU/计费DOS。human/TTS、persona切换与Grok攻击对照不同预算/人群不作同配置统一安全率；未核真实API权限实施/账户影响/部署财损。AppA有session token、auth fail自动termination/IT角色限制，但bank credit RED_TEAM_MODE auto-approve提示说明模拟policy不能借用为生产操作安全。hardware/precision/APIrevision、音频codec/TTSengine/latency/费用、重复CI未披露。仅报告数据权限不替代行为policy的局部反侧，不为新语音场景或缺recipe强加Books，不采用通用openweight更弱/认证/监管要求。

### [Steer2Adapt: Dynamically Composing Steering Vectors Elicits Efficient Adaptation of LLMs](https://arxiv.org/abs/2602.07276v1)

单独steering direction不可直接复用为task最优→冻结语义basis内fewshot组合搜索并惩罚已正确样本回退→重审basis匹配、搜索与迁移代价，2+2+2=6，安全结论受影响深入。精确v1 §3/4/6、AppA.3/A.4/A.9：[AB1 final core](../_sources/daily-20260211/feb11_AB1_minimal_final.json)。REP五BigFive或五safety轴、h+Vα/系数[-2,2]，每task12已知正确/错误平衡样本（不是随机12任意数据），BO50Sobol+350搜索/seed、每候选重新评估；五runs平均SD，Llama3.1-8B/Qwen2.5-7B/Mistral7B/A6000、九reason/safety任务。basis错用safety→reason大退、小数噪声轴未大退，局部支持语义subspace重要，不证明独立概念/所有泛化。mainEq2 Δp与AppEq7 logΔp不一致，§4注入8–24而A.9含26，不静默统一实际recipe；仅采用公开受限对照，精确objective/layers待对应官方实现/更正，不阻塞该局部Only。flip20/drop10是有限soft penalty，Σ多error gain可抵消、12 support的保留不能认证所有未见样本lossless；App所述“hard”不作形式安全保障。相关axis entanglement：bias改进可降低fairness轴；Table2 BLiMP平均-2.37%、syco-4.52%、refusal-4.50%是直接代价，不称全部语言能力保持。REP <5min/axis准备及400query搜索均额外成本，Fig5normalized gain/推理cost不等整准备+推理总成本/真实SLO；未披露precision、长度batch并发/运行时后端、误报漏拒绝分账和CI。仅报告该几模型/任务的basis/search/语言质量取舍，不采语义axis因果解耦、普遍安全无损或任意即插即用。

### [Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation](https://arxiv.org/abs/2602.07338v1)

多轮失败不一定是忘记已给facts→区分观测信息不足与execution、并引入history Refiner→Mediator重构instruction的受限对照→重审需要新增用户信息还是仅检索/扩大模型，3+1+2=6设计反侧深入。精确v1 §3–5/7、AppA：[AB1 final core](../_sources/daily-20260211/feb11_AB1_minimal_final.json)。Eq3分解假设latent intent是sufficient statistic、执行与原context近似条件独立；缺失信息不可凭空推理是条件边界，不由三model实验证明scaling加剧所有LiC。history使条件entropy不增但Eq6“≪”与足以恢复trueintent是作者假说，不能作已证strictgap。实际并非真实用户longitudinal profile：四binary tasks Code/Database/Actions/Math、合成shards改natural顺序、每task随机5history任务从test移除，failedmulti+successfulfull instruction配对，再refiner规则；附加teacher/fullprompt信息源与原baseline不相同，不采“仅架构重写而信息预算一致”的因果。GPT4omini/GPT5.2/DSv3.2Thinking、five independent generation runs，每instance1-(max-min)是稳定性非正确率/CI；合成population和prompt/token budget不可扩实际personalized用户。Table2同GPT4omini rawsummary/mem0部分任务提高或退，mediator73.9仍低Full86.9，不能完全intent恢复或排除context管理作用。Rawpair ICL质量相近但3.6×tokens支持局部压缩取舍，不等refiner采样/制备+mediator+assistant全过程时延费用；正文Oracle说明/图无足够协议，不借其名作意图gold。backend/hardware/precision/APIrevision、实验N/长度batch/T/CI和真实交互额外latency未披露。仅报告受限信息与经验重写边界，不把不可识别用户意图变成模型可认证trueintent，也不新增长期recipe。

### [Efficient Post-Training Pruning of Large Language Models with Statistical Correction](https://arxiv.org/abs/2602.07375v1)

mask质量不等剪后信号尺度保持→CVR权重variance/activationvar校正+固定mask后的column→row解析EC→重审选择与补偿分账，2+2+2=6标准。精确v1 §3/4.1–4.7/6、Tables1–5：[AB1 final core](../_sources/daily-20260211/feb11_AB1_minimal_final.json)。importance |W|·var(x)^1/4·(var(W)+ε)^(-α/2)；基于原weight均值的centered-energy ratio/clamp→两方向依次重标、reapplymask。weight统计非直接activation分布匹配；clamp/重置zero/后row改变前column意味着不采用严格同步能量保持或最优重构定理。C4 128sequence同baselinecalibration，无retrain；Llama2/3/Qwen2.5 7B–72B、50%与4:8/2:4、Wikitext2PPL/六taskzero-shotavg。Table5 Llama2: Wanda→CVR→col→row局部归因，13B5.46→5.43→5.33→5.32不自动统计显著，baselineoriginalimplementations非本次代码已实核。反侧Table1 magnitude+EC Llama2-13B PPL6.37→7.04、Llama3-8B310.68→735.39；Wanda+EC Llama3-70B2:4 9.39→54.02、CVR+EC12.00仍差原Wanda9.39；Table2 someWanda+EC胜CVR+EC，不能全面better。Table3 5.35 vs31.07s仅Llama2-13B单linear pruning/adjustment，不是所有model端到端制备或serving：未披露hardware/precision/sequence长度、batch并发/SLO、kernel稀疏执行收益、峰值HBM、repeats/CI。极高sparsity/shift仍退，limiteddecoder-only。仅报告解析补偿可低准备成本修正某些mask退化的局部事实，不采无损、全模型更优或稀疏执行必加速。

## 5. 缺口与下一步

普通可执行工作：无。

以下为本窗终态保留项，不用于正面证据、Books或无遗漏断言；取得所列材料后定点重开。

本窗可执行扫描、筛选、必要审阅、日期归并、Books落实与独立复核剩余0；root整日Gate通过后标完成。有限来源/标题线索停止点已处理，未把未读宽列表普通标题变成受阻或强制队列。六项贡献关闭：首批07543/08990、TernaryLM07374、VerifyRL07559、AIRS-Bench、PreFlect07187；具体关闭依据见[记录](../_sources/daily-20260211/feb11_minimal_contribution_closes.md)，原AB/core保留；不是因成本、Only或既有Books而缩池。

中心争议保留项：AgentFence 2602.07652v1的SC Table2与§8.1聚合不一致，完整采用边界与定点重开见§4；不用于正面安全证据/Books/无遗漏保证。

外部隔离：Anthropic系统卡Feb10纠错（MMMU-Pro70.7→70.6、frontier承诺措辞）与[Sabotage Risk Report](https://www.anthropic.com/claude-opus-4-6-risk-report)只有Feb10日标，时区/可落窗公开范围不能确认；风险正文可读但不用于本窗候选、Books、安全保证或无遗漏。恢复只需官方带时区发表字段/不跨窗口的公告包络或可信历史正文公开记录，定点本事件，不遍历所有版本。其余原生历史缺段按§2逐行隔离，不能支持“Coverage通过”，恢复只补相应窗口主题历史段。

## 6. 复核

复核者：root（非作者）

结论：通过

root分批实际核完整题摘准入、全部48候选的必要采用命题/支持与直接反侧、Books处置，含全部本次安全/纠错/设计反证候选；AgentFence中心争议只验收隔离终态，不授正面证据。实际定点核rePIRL Eq6、Anchored clamp、Judge signed净差、routing白盒权限/utility、action-equivalence副作用、半诚实/per-step与总成本、最后三项finite penalty/history额外信息/EC非严格两轴不变等受影响原证，不称无差别全部附件复现。Ch5/36两处真实正文/邻接/末注POST和07150/07729/07359具体Existing owner通过。六普通排除按范围/成熟机制/新benchmark理由分层，六份完整AB与具体理由全部实际复核，PreFlect/Ternary/Verify最小core复用；DialogLab产品Blog代表排除亦校准。root顺读最终14每日来源的真实入口/查询停止及缺段隔离、日期包络、48冻结表与六部分，确认普通可执行0，授日级Gate。未检查1173/1138旧库存或全部学科，未把抽检/保留项当全量召回。

完成态V3 schema、Markdown结构/本地refs与scoped diff-check通过；连续48行候选表与48个§4同URL标题一致。已检查本日README替换diff及两处本日Books正文/末注unstaged差额；cached范围只有Ch5/36既有历史内容，本日两个source-family标记未在cached差额中出现，原staged变更保持不动。本作者没有stage/commit/push、没有运行artifact或复现实验；格式通过不证明来源完整或语义真实。完成是本窗安全终态，不是正面Coverage/争议主张性能与安全保证。
