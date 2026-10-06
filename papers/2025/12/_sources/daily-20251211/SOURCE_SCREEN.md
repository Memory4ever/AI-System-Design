# 12/11原始发现与停止记录

2026-10-02T19:54:40+08:00作者反馈修正。Seed本日独立选择12/10–11相邻范围paper12/15→12/02、Blog12/16→12/02；两类各实际18条、total94/45、next20，pinned逐项日期核，不续全年队列，原始接口见[09补证](../daily-20251209/TARGETED_REPAIR.md)。DeepMind实际正确入口[page/4](https://deepmind.google/blog/page/4/)的24条December/November段，本日选择UK合作12/10与AISI12/11；复用实际核心合作/未来工作说明，不新增训练或执行机制。Alignment实际December六项向下到November两项，本日独立选择SGTM12/08至Fellows/Replication12/12间邻接；该段已处理，不代替Anthropic其他Research组。撤销下文过宽历史未恢复表述，不推全源零事件。

实际检查2026-10-02T18:23:49+08:00起。窗口[2025-12-10T09:00:00+08:00,2025-12-11T09:00:00+08:00)。这不是完成收据。

## 十四源与原始目录邻接

独立执行四组官方域查询：OpenAI/Anthropic/DeepMind/Research/Google Blog；Meta/Qwen/DeepSeek/Kimi；Hunyuan/ZAI/Seed；ERNIE/MiMo/MiniMax。每组使用 `("December 10, 2025" OR "2025-12-10")`+model/research/training（中文源日期同式）。搜索有限结果不是无遗漏。

复用的是[实际官方目录原始字段](../daily-20251210/HISTORICAL_DIRECTORY.md)，本日选择邻接为：Meta12/01→12/12；DeepSeek12/01原文；Kimi11/06最新；Hunyuan全部十一项至2026/02/03，无2025段；ZAI本轮首查超时但搜索恢复Research首屏15项末项12/10 TTS与12/09 ASR，并实际读TTS/ASR原文，release12/10 ASR与12/11 Phone；Seed12/02→2026/01/27精选、papers第一页20/242未恢复历史；ERNIE12/09→12/23；MiMo10/21→2026/01/08；MiniMax10/27→12/23两语目录/Agent导航。OpenAI/Anthropic/Qwen仍滚动/动态历史缺口。组织当前有限替代不证明历史零。

本轮另读[Google Research12月档案](https://research.google/blog/2025/12/)实际六项：12/03、04、10、12、15、18。只选择相交12/10 Urania，非全月候选扫描。其June v1完整题摘与blog核心匹配旧DP pipeline，未发现本篇新机制/修订事件；博客解释不重复入选，非宣称旧论文已审。Gemini TTS完整核心与May原文对照，负侧见准入记录；原始NewsArticle.datePublished=2025-12-10T17:00:00+00:00（BJT12/11 01:00），不影响贡献前关闭。

ZAI-TTS必要日期与固定稿见EVIDENCE_BOOKS。ASR原始time=2025-12-09T16:00:00.000Z，晚恢复路由Daily10，非本窗重复计数。当前架构规格图片文件名2026-01-26，不能当2025精确图；定点恢复由10原始记录承接。

## arXiv主题与有界列表

四主题查询：language model/MoE/RL；LLM inference/distributed training/KV cache；world model/VLA/block diffusion；Agent memory/tool/reasoning。官方域限定，after:2025-12-09 before:2025-12-12只帮助发现，不解释为first-public。另检索Dec10表达。命中METRO、LLaDA2、PRISM等，不用搜索Date代替公告。

实际官方2025-12列表：CL skip275/show50（276–325，07538–09434）；LG skip575/show50（576–625，06982–07569）与skip625/show50（626–675，07624–08093）；DC skip50/show25（51–75，07792–09963）；AI skip250/show50（251–300，08366–10100）；CV skip725/show50（726–775，06330–06783）偏早仅定位，再取skip925/show50（926–975，08227–08542）；AR skip50/show25（51–75，07312至14661），只补目标邻接DCO/ODMA，后段为晚边界定位，不进入整月队列。反馈扩查仅重新读取原CL/DC/CV三段相关标题，新增精确题摘33项（含原表已有10项的定点重读），处置见下表，不扩全年或整月库存。

链接形式为 `https://arxiv.org/list/<category>/2025-12?skip=<n>&show=<n>`。浏览相关标题，范围外医学/临床记录、材料/蛋白/遥感领域应用等按标题明显范围外关闭；没有把列表逐项强制读题摘。Metric-Fair Prompting07608原按领域/成熟prompt关闭撤销：Popper实际§3/Table2、§4、§6证明有跨item耦合、结果不稳定及prompt声明不等硬Lipschitz约束的潜在边界，保留而不授理论或普适公平保证。

以下73个精确v1实际完整题摘已读，潜在增量保留，不因日期失败降分或删除；还不是确定本窗候选/证据完成。部分current标题与v1不同，表以v1身份为准。

| 原始身份 | 潜在具体增量 | 当前处置 |
| --- | --- | --- |
| [2512.10054v1](https://arxiv.org/abs/2512.10054v1) | v1 SNC notes动态bus的并行decode | 完整题摘；首new公告未恢复，隔离，不评分/不采用 |
| [2512.15745v1](https://arxiv.org/abs/2512.15745v1) | 已知datehold LLaDA2三阶段block WSD转换 | 完整题摘；首new公告未恢复，隔离，不评分/不采用 |
| [2512.06989v1](https://arxiv.org/abs/2512.06989v1) | FFN多头设计与SRAM融合核 | 完整题摘；首new公告未恢复，隔离，不评分/不采用 |
| [2512.07011v1](https://arxiv.org/abs/2512.07011v1) | 精确QK后按块跳过value计算 | 完整题摘；首new公告未恢复，隔离，不评分/不采用 |
| [2512.07092v1](https://arxiv.org/abs/2512.07092v1) | 冻结backbone的人格向量；t-SNE不证明正交/安全 | 完整题摘；首new公告未恢复，隔离，不评分/不采用 |
| [2512.07112v1](https://arxiv.org/abs/2512.07112v1) | 分块optimizer moment折叠和残差修正 | 完整题摘；首new公告未恢复，隔离，不评分/不采用 |
| [2512.07173v1](https://arxiv.org/abs/2512.07173v1) | 置信度联调diffusion block/step/词表 | 完整题摘；首new公告未恢复，隔离，不评分/不采用 |
| [2512.07175v1](https://arxiv.org/abs/2512.07175v1) | NCE绝对目标与self-play差值退化 | 完整题摘；首new公告未恢复，隔离，不评分/不采用 |
| [2512.07222v1](https://arxiv.org/abs/2512.07222v1) | function-word差分attention与局部攻击反证 | 完整题摘；首new公告未恢复，隔离，不评分/不采用 |
| [2512.07287v1](https://arxiv.org/abs/2512.07287v1) | v1 SIT-Graph：边上状态摘要+工具依赖 | 完整题摘；首new公告未恢复，隔离，不评分/不采用 |
| [2512.07374v1](https://arxiv.org/abs/2512.07374v1) | LoRA梯度解码跨模型unlearning | 完整题摘；首new公告未恢复，隔离，不评分/不采用 |
| [2512.07375v1](https://arxiv.org/abs/2512.07375v1) | negative-only LoRA unlearning | 完整题摘；首new公告未恢复，隔离，不评分/不采用 |
| [2512.07419v1](https://arxiv.org/abs/2512.07419v1) | 量化proxy自动搜索与prompt优化 | 完整题摘；首new公告未恢复，隔离，不评分/不采用 |
| [2512.07558v1](https://arxiv.org/abs/2512.07558v1) | Koopman latent exploration | 完整题摘；首new公告未恢复，隔离，不评分/不采用 |
| [2512.07612v1](https://arxiv.org/abs/2512.07612v1) | 数据quantile比较/选择性重复/curriculum | 完整题摘；首new公告未恢复，隔离，不评分/不采用 |
| [2512.07687v1](https://arxiv.org/abs/2512.07687v1) | 多模态内部层动态hallucination探测 | 完整题摘；首new公告未恢复，隔离，不评分/不采用 |
| [2512.07783v1](https://arxiv.org/abs/2512.07783v1) | 受控pre/mid/RL与能力边缘反证 | 完整题摘；首new公告未恢复，隔离，不评分/不采用 |
| [2512.07832v1](https://arxiv.org/abs/2512.07832v1) | 控制ID表现后OOD相关仍依模型不同 | 完整题摘；首new公告未恢复，隔离，不评分/不采用 |
| [2512.08082v1](https://arxiv.org/abs/2512.08082v1) | 最小局部context及长程token boost | 完整题摘；首new公告未恢复，隔离，不评分/不采用 |
| [2512.08123v1](https://arxiv.org/abs/2512.08123v1) | calibrated软后缀攻击 | 完整题摘；首new公告未恢复，隔离，不评分/不采用 |
| [2512.08131v1](https://arxiv.org/abs/2512.08131v1) | calibrated PPO后缀攻击 | 完整题摘；首new公告未恢复，隔离，不评分/不采用 |
| [2512.08545v1](https://arxiv.org/abs/2512.08545v1) | 空间curriculum和选择oracle的Hanoi局部条件 | 完整题摘；首new公告未恢复，隔离，不评分/不采用 |
| [2512.08777v1](https://arxiv.org/abs/2512.08777v1) | 不流畅judge下on-policy低资源语言对照 | 完整题摘；首new公告未恢复，隔离，不评分/不采用 |
| [2512.08786v1](https://arxiv.org/abs/2512.08786v1) | group reward历史表现自适应聚合 | 完整题摘；首new公告未恢复，隔离，不评分/不采用 |
| [2512.08819v1](https://arxiv.org/abs/2512.08819v1) | depth growth残差流/层使用反证 | 完整题摘；首new公告未恢复，隔离，不评分/不采用 |
| [2512.08892v1](https://arxiv.org/abs/2512.08892v1) | SAE特征选择的RAG faithfulness探测 | 完整题摘；首new公告未恢复，隔离，不评分/不采用 |
| [2512.08943v1](https://arxiv.org/abs/2512.08943v1) | 检索噪声与answer-centered compressor训练 | 完整题摘；首new公告未恢复，隔离，不评分/不采用 |
| [2512.09212v1](https://arxiv.org/abs/2512.09212v1) | proxy-policy冲突的定点human feedback | 完整题摘；首new公告未恢复，隔离，不评分/不采用 |
| [2512.09238v1](https://arxiv.org/abs/2512.09238v1) | head预算离线校准+在线redundancy selection | 完整题摘；首new公告未恢复，隔离，不评分/不采用 |
| [2512.09277v1](https://arxiv.org/abs/2512.09277v1) | METRO激活专家均衡而非tokens | 完整题摘；首new公告未恢复，隔离，不评分/不采用 |
| [2512.09472v1](https://arxiv.org/abs/2512.09472v1) | universal worker预热/placement/memory switch | 完整题摘；首new公告未恢复，隔离，不评分/不采用 |
| [2512.08242v1](https://arxiv.org/abs/2512.08242v1) | MI300X FSDP频率损失的跨层profiling | 完整题摘；首new公告未恢复，隔离，不评分/不采用 |
| [2512.08365v1](https://arxiv.org/abs/2512.08365v1) | 算子级差分能耗定位software waste | 完整题摘；首new公告未恢复，隔离，不评分/不采用 |
| [2512.08366v1](https://arxiv.org/abs/2512.08366v1) | v1 DuSAR双策略fitness反思 | 完整题摘；首new公告未恢复，隔离，不评分/不采用 |
| [2512.08411v1](https://arxiv.org/abs/2512.08411v1) | hybrid dynamics分mode专家与正交目标 | 完整题摘；首new公告未恢复，隔离，不评分/不采用 |
| [2512.08743v1](https://arxiv.org/abs/2512.08743v1) | 41模型single-agent强不授multi-agent强 | 完整题摘；首new公告未恢复，隔离，不评分/不采用 |
| [2512.08826v1](https://arxiv.org/abs/2512.08826v1) | matched base生成差值的LoRA检索表示 | 完整题摘；首new公告未恢复，隔离，不评分/不采用 |
| [2512.08923v1](https://arxiv.org/abs/2512.08923v1) | 同内容跨模态/OCR已正确仍不一致 | 完整题摘；首new公告未恢复，隔离，不评分/不采用 |
| [2512.09331v1](https://arxiv.org/abs/2512.09331v1) | BatANN查询状态迁移而非scatter gather | 完整题摘；首new公告未恢复，隔离，不评分/不采用 |
| [2512.09386v1](https://arxiv.org/abs/2512.09386v1) | 新增策略单独predictor的continual router | 完整题摘；首new公告未恢复，隔离，不评分/不采用 |
| [2512.09829v1](https://arxiv.org/abs/2512.09829v1) | 故障RL搜索/coverage与面积代价 | 完整题摘；首new公告未恢复，隔离，不评分/不采用 |
| [2512.09897v1](https://arxiv.org/abs/2512.09897v1) | one-time teacher subgoal学生部署 | 完整题摘；首new公告未恢复，隔离，不评分/不采用 |
| [2512.06353v1](https://arxiv.org/abs/2512.06353v1) | DiT mixed precision tree search/structured branch | 完整题摘；首new公告未恢复，隔离，不评分/不采用 |
| [2512.06376v1](https://arxiv.org/abs/2512.06376v1) | raw生成驾驶视频可能损害perception | 完整题摘；首new公告未恢复，隔离，不评分/不采用 |
| [2512.06421v1](https://arxiv.org/abs/2512.06421v1) | next-scale自生context的student-forcing | 完整题摘；首new公告未恢复，隔离，不评分/不采用 |
| [2512.06562v1](https://arxiv.org/abs/2512.06562v1) | surrogate identity latent与continual utility | 完整题摘；首new公告未恢复，隔离，不评分/不采用 |
| [2512.06674v1](https://arxiv.org/abs/2512.06674v1) | I2V multimodal协调攻击的安全信号 | 完整题摘；首new公告未恢复，隔离，不评分/不采用 |
| [2512.06759v1](https://arxiv.org/abs/2512.06759v1) | 视觉chain verification/控制language cues | 完整题摘；首new公告未恢复，隔离，不评分/不采用 |
| [2512.07647v1](https://arxiv.org/abs/2512.07647v1) | top-k tail mass/output误差与Gaussian假设 | 完整题摘；首new公告未恢复，隔离，不评分/不采用 |
| [2512.07667v1](https://arxiv.org/abs/2512.07667v1) | 同总强度depth steering分配对照 | 完整题摘；首new公告未恢复，隔离，不评分/不采用 |
| [2512.07782v1](https://arxiv.org/abs/2512.07782v1) | window recurrence的gate contraction | 完整题摘；首new公告未恢复，隔离，不评分/不采用 |
| [2512.07805v1](https://arxiv.org/abs/2512.07805v1) | group相对position与cacheability | 完整题摘；首new公告未恢复，隔离，不评分/不采用 |
| [2512.07818v1](https://arxiv.org/abs/2512.07818v1) | RNN next-token对bounded discriminator的理论边界 | 完整题摘；首new公告未恢复，隔离，不评分/不采用 |
| [2512.07843v1](https://arxiv.org/abs/2512.07843v1) | trie并行推理与训练runtime co-design | 完整题摘；首new公告未恢复，隔离，不评分/不采用 |
| [2512.07850v1](https://arxiv.org/abs/2512.07850v1) | SABER mutation级失败和benchmark修订信号 | 完整题摘；首new公告未恢复，隔离，不评分/不采用 |
| [2512.07853v1](https://arxiv.org/abs/2512.07853v1) | 多模态分层峰值HBM预测 | 完整题摘；首new公告未恢复，隔离，不评分/不采用 |
| [2512.07855v1](https://arxiv.org/abs/2512.07855v1) | log-domain sparse attention硬件 | 完整题摘；首new公告未恢复，隔离，不评分/不采用 |
| [2512.07884v1](https://arxiv.org/abs/2512.07884v1) | GSPN microlaunch→2D fused kernel | 完整题摘；首new公告未恢复，隔离，不评分/不采用 |
| [2512.08061v1](https://arxiv.org/abs/2512.08061v1) | learnable positive kernel linear attention | 完整题摘；首new公告未恢复，隔离，不评分/不采用 |
| [2512.08228v1](https://arxiv.org/abs/2512.08228v1) | visual/logical两正交chain验证 | 完整题摘；首new公告未恢复，隔离，不评分/不采用 |
| [2512.08240v1](https://arxiv.org/abs/2512.08240v1) | v1 continuous/detail+discrete/semantic混合压缩 | 完整题摘；首new公告未恢复，隔离，不评分/不采用 |
| [2512.08269v1](https://arxiv.org/abs/2512.08269v1) | ego/exo视频geometry-guided attention | 完整题摘；首new公告未恢复，隔离，不评分/不采用 |
| [2512.08282v1](https://arxiv.org/abs/2512.08282v1) | VLM mass/3D velocity的V2A条件；非实测物理真值 | 完整题摘；首new公告未恢复，隔离，不评分/不采用 |
| [2512.08374v1](https://arxiv.org/abs/2512.08374v1) | pre-norm视觉范数不对称更新 | 完整题摘；首new公告未恢复，隔离，不评分/不采用 |
| [2512.08410v1](https://arxiv.org/abs/2512.08410v1) | query-guided视频chunk/retrieval共用 | 完整题摘；首new公告未恢复，隔离，不评分/不采用 |
| [2512.08477v1](https://arxiv.org/abs/2512.08477v1) | 无噪reference token位置映射与遮罩 | 完整题摘；首new公告未恢复，隔离，不评分/不采用 |
| [2512.08511v1](https://arxiv.org/abs/2512.08511v1) | 共享参数subagent隔离context | 完整题摘；首new公告未恢复，隔离，不评分/不采用 |
| [2512.08524v1](https://arxiv.org/abs/2512.08524v1) | progressive PHM替换与distillation | 完整题摘；首new公告未恢复，隔离，不评分/不采用 |
| [2512.08529v1](https://arxiv.org/abs/2512.08529v1) | GUI裁剪coordinate不稳定、多视图聚类 | 完整题摘；首new公告未恢复，隔离，不评分/不采用 |
| [2512.08537v1](https://arxiv.org/abs/2512.08537v1) | AR/diffusion entropy与联合distillation | 完整题摘；首new公告未恢复，隔离，不评分/不采用 |
| [2512.07312v1](https://arxiv.org/abs/2512.07312v1) | dataflow-guided shared cache替代SPM | 完整题摘；首new公告未恢复，隔离，不评分/不采用 |
| [2512.09427v1](https://arxiv.org/abs/2512.09427v1) | LPDDR随机访问约束下bucket分配 | 完整题摘；首new公告未恢复，隔离，不评分/不采用 |

## 反馈恢复与有界受影响集合

以下18项依据Popper实际完整精确v1题摘/必要局部正文校准恢复；不是作者冒称重新全读18份正文。每项潜在贡献保留，均缺个体first-public，不评分、不用于Books/覆盖。原表73项中Confessions另作旧事件关闭。

| 精确v1 ID | 具体潜在增量/边界 |
| --- | --- |
| 2512.07544 | MoCoRP对persona关系的NLI约束，非仅换角色描述 |
| 2512.07777 | 内部incoherence probe与输出失败可分离，reasoning不能自动修复 |
| 2512.08404 | annotation F1与下游prevalence偏差不等价 |
| 2512.08944 | 外部/内部hallucination reward及abstain分离 |
| 2512.09148 | GraphRAG path attention与semantic诊断；不是因果证明 |
| 2512.09292 | 16子群detector交互偏差，不把平均分授跨群可靠 |
| 2512.09309 | 多云shard不呈完整graph，不能推无collusion隐私 |
| 2512.09685 | 异步straggler/TTA与组同步、CPU/带宽取舍 |
| 2512.09946 | ELANA §2.2–2.5：raw cache/SSM、prefill不启CUDA graph而decode启用、局部batch时延、100ms功率采样窗口及多GPU求和；不是HF/NVML组合即关闭 |
| 2512.09957 | CloudFix SMT形式约束的有限正确性范围 |
| 2512.09963 | GoodSpeed draft/verifier accepted-token goodput和log utility的稳态假设 |
| 2512.08329 | 图像保护的结构扰动更易检测，非仅任务涨分 |
| 2512.08445 | ID子集解释OOD不确定性；submodular gradient不授faithfulness |
| 2512.08478 | VisionaryGaussian逐帧measurement不等action dynamics |
| 2512.08486 | diffusion时变concept intervention的有限因果权限 |
| 2512.08503 | ReasonBreak geolocation隐私的局部反证 |
| 2512.08505 | NoisyCLIP noisy-latent早期proxy不等真实生成质量 |
| 2512.07608 | Metric-Fair跨item配对/冲突、baseline及prompt公平声明的限制 |

作者实际新增33份精确v1题摘：07571、07583、07666、07801、08094、08440、08480、08646、08777、08786、08814、08892、09149、09212、09222、09386、08005、08365、08725、08309、08317、08325、08330、08358、08406、08477、08498、08506、08524、08529、08534、08535、08537。其中10项身份/潜在命题与原表相同，不重复增加家族。新增保留如下，日期隔离权限同上：

| 精确v1 ID | 原文具体潜在增量 |
| --- | --- |
| 2512.07571 | speech token lasso选择接LLM；随机audio token也有益，不能把收益全归task选择 |
| 2512.07666 | frozen LLM外部code-graph bridge避免架构改写/长prompt，代价待核 |
| 2512.08094 | sign segment/embedding与CPU DP对齐跨语言，接口分解替代end-to-end绑定 |
| 2512.08440 | gender-ambiguous上下文contrastive attribution与阈值，相关不证明模型因果 |
| 2512.08480 | 显式reasoning perspectives约束的局部训练对照，不授所有推理可靠 |
| 2512.08646 | questionnaire结构与生成方式改变人类对齐/计算代价，不是新增UI准入 |
| 2512.09149 | persona强度/模型家族psychometric response差异；不把模型回答当人类心理真值 |
| 2512.09222 | persistent concept替代全history重放；42%明确仅模拟prototype，不作生产性能 |
| 2512.08309 | infinite diffusion seed一致/random access/constant memory约束，非普通terrain应用 |
| 2512.08317 | product-manifold curvature/OT改变dataset distillation误差界，假设需核 |
| 2512.08325 | noise-free flow监督区分photon noise与micro-motion，条件生成路径新取舍 |
| 2512.08330 | point-cloud unordered条件下diffusion指导contrastive表示，非任务名即可关闭 |
| 2512.08358 | camera/foreground运动分离与新对象稠密tracking，非action transition证明 |
| 2512.08406 | video masklet/occlusion补全修正逐帧SAM3D不一致，无重训不等零额外成本 |
| 2512.08498 | uncalibrated multi-camera初始化/BA与冗余Gaussian sampling、频率调度 |
| 2512.08506 | continuous occupancy-function latent diffusion接口与噪点条件，不授物理一致保证 |
| 2512.08535 | GPT-image多视角不一致→structure-aligned synthesis/geometry-texture策略区分 |

2026-10-02T20:19:36+08:00同步Popper实际必要正文校准，撤销原六项负侧中的三项关闭。作者此前读完整题摘；下列必要正文位置与发现复用非作者原始审阅，不冒称作者重新全读正文。新增23项最终为20项潜在保留、3项具体负侧；日期仍隔离，不评分、不用于Books或覆盖。

| 精确材料 | 恢复的具体潜在增量与边界 |
| --- | --- |
| [2512.07583v1](https://arxiv.org/pdf/2512.07583v1) | 必要pp26–29 Comparison/Step5将人attention error与模型上下文不全/二元ontology错误分账，并联动修正提示语境与分类边界；保留局部评价诊断反证，不把无独立holdout的循环提升当通用准确率。 |
| [2512.08814v1](https://arxiv.org/html/2512.08814v1) | §3.3–3.5/§4.3–4.5有label-conditioned离线问卷软监督、question-conditioned MLP experts及可靠性/重要性权重；Table2子维度退步不能被总F1遮盖。合成回答非人的心理真值，推理不调LLM不等训练成本为0。 |
| [2512.08534v1](https://arxiv.org/html/2512.08534v1) | 训练/fusion、Table1/Ablation将mask/sketch的空间条件与reference/text语义路径分责，具去模态对照及含糊sketch/参考冲突失效；输入模态不齐限制归因，但不足以因AdaIN或油画场景关闭。 |

剩余三项完整题摘负侧保留：07801明确研究agenda与未来挑战，未披露可支持的执行机制或实证；08005只MPI热传导/HPCG的CXL.mem工具链，未建立模型训练/推理关系；08725仅big-data/FaaS云环保simulation，没有模型负载或改变模型系统选择的机制。它们不是学术否定。恢复范围仅本次有界集合，详见[非作者原始记录](./ROOT_ADMISSION_REVIEW.md)。

## Confessions旧公开关系关闭

2026-10-02T19:54:40+08:00作者实际读[12/03官方博客](https://openai.com/index/how-confessions-can-keep-language-models-honest/)核心/limits、[原CDN稿](https://cdn.openai.com/pdf/6216f8bc-187b-4bbb-8932-ba7c40c5553d/confessions_paper.pdf)pp1/3/4/8/9/10及[精确v1](https://arxiv.org/html/2512.08093v1)题摘/§1/2/4：同名同作者、独立confession reward不改变main-answer reward、弱judge实验与能力不足false-negative限制对应。CDN稿共33页，不冒称全读或逐字一致；当前HTML/原PDF有局部表述差异，未识别独立新机制/本窗重要修订，按旧公开后归档关闭该事件，不采用新性能数。12/03日标签足以排本窗旧事件，不恢复其精确旧first-public时刻、不声称旧日报已审。撤回08093的统一必要日公告请求；剩余日期项不受此关系关闭影响。

## 必要首公开外部隔离

已读[官方日期窄恢复](../ARXIV_DATE_RECOVERY.md)的实际历史Git/API/OAI/RSS及失败范围；不重复日粒度announcement空接口。官方月列表仅恢复身份，Submitted/API published/OAI version date仍不授日；列表编号相邻不授批次。LLaDA2的Submitted Dec10与大ID相互提示datehold，更不能排期硬推。此轮缺匹配ID/v1的实际new公告或等效公众可用证据，有限可用方法已穷尽后安全隔离；不支持零事件、Coverage/Evidence通过或Books采用。

重开精确点：表中对应ID/v1的官方new公告，批次label时区与晚间实际slot有定义；或首正文公众时刻/完全落窗范围。边界09:00等于右端时归下一Daily。日期恢复后才准入评分并读必要正文；现有题摘不会被“已审完”标签替代。
