# Nov21 新发现首批准入/安全与日期字段包

作者Noether；2026-10-15T17:55:00+08:00。新16个exact-v1完整题摘实际读，提案15潜力P＋1最小门M，不等正式候选/评分/Evidence/Books。请root即时转Ohm实际校准，不等待其余Source/date/主题尾；旧32有效题摘/必要反侧不重。

## 1. 入口与版本权限

本轮七机制主题Advanced，submitted_date最近提交发现输入from=Nov19/to=Nov21；客户端不自证上界排除，实际返回含Nov21 history项，只作发现。Computer Science/cross-list included、hide abstracts、size50、按首次公告倒序。真实URL/执行时间/HTTP/bytes在各SUP_ARXIV同名receipt。四带前导括号/混合短语query返回no-results后，只简化对应MODEL/LEARNING/AGENT/MULTIMODAL；不称最初四个零返回是全主题零。实际有效返回Model23/23、Learning50/58及page2八、System29/29、Agent8/8、Multimodal17/17、Generation14/14、World11/11，均有限主题发现，不成为全AB/全文队列。后者混入VLBI/medical/science等不相关标题，按语义范围止，不扩全类。CL/LG月表各skip750/show25只作有限相关标题补检，尚在实际读字段，不宣完整公告/日期。无legacy/catchup/failed API重试。

本包每项原始HTML `SUP_AB_<ID>_20261015.html` 是本轮原站精确v1/HTTP200，receipt绑定执行；完整题摘、作者、版本history与当前原comments足以核本层。下表只保最小贡献链和未证明范围，不采摘要分数。若ID不在原32就是本轮新发现，不从Nov20池搬入。

## 2. 新16完整题摘提案

| exact-v1 / 原history UTC | 原约束 → 实际潜在增量 → 可能改变的选择与权限 | 提案 |
| --- | --- | --- |
| [2511.15308](SUP_AB_2511.15308_20261015.html)；Nov19 10:19:45 | 自由语言与点云对象不完全对应 → MIT过滤不对齐对象、分层contrastive与fine stage免显式instance匹配 → 点/语言对齐不应被强制一一配对；只局部空间表示，仍需看MIT与PMC具体作用/相同数据预算，不采15%或city泛化。`MULTIMODAL-REPRESENTATION`方向 | P |
| [2511.15316](SUP_AB_2511.15316_20261015.html)；Nov19 10:30:38 | split隐藏中间feature未必保密 → feature-latent对齐与one-step inversion FM分工 → 泄露评价不能只看传统重建器；黑盒权限/少量配对与VLM评价误差须保，不能授所有split风险率。`PLATFORM-SECURITY` | P，安全 |
| [2511.15505](SUP_AB_2511.15505_20261015.html)；Nov19 14:59:11 | FPGA多PU部署切换通常绑定重配置 → 指令controller/peer同步配合连续子图映射，可runtime选择pipeline或batch分组 → 编译计划与硬件配置应分开；仅ResNet50作者实验，不宣LLM吞吐或98%/2.7x普效。`INFER-TENSORRT-LLM`执行计划方向待唯一owner | P |
| [2511.15704](SUP_AB_2511.15704_20261015.html)；Nov19 18:59:04 | 异质human ego视频仅作简单预训练 → 分in-the-wild/on-task并对齐robot适配 → 数据角色与跨具身迁移条件要分账；需核实际适配/数据配比/增量来源，不采全部语言跟随或robustness。`MULTIMODAL-EMBODIED-VLA` | P |
| [2511.16047](SUP_AB_2511.16047_20261015.html)；Nov20 05:10:12 | next-scale VAR缓存不能直接沿语言历史策略 → coarse/local scale保留与按跨scale相似度区分层 → cache预算与scale/layer角色联动；需可比quality/batch与真实attention路径，不采84.83%/60.48%或全VAR。`MULTIMODAL-GENERATIVE-PARADIGMS`与KV交接待唯一owner | P |
| [2511.16150](SUP_AB_2511.16150_20261015.html)；Nov20 08:44:47 | direct encoding略过生成条件化 → 先instruction-conditioned结构rationale，再提embedding并contrastive训练 → 生成预算是检索表示的一部分；需理由/额外token/训练控制，不采4.9%或rationale忠实因果。`AGENT-RAG` | P |
| [2511.16229](SUP_AB_2511.16229_20261015.html)；Nov20 10:55:19 | 连续视觉输入可被攻击而text safety未自然迁移 → pixel-patch/semantic双层VQ瓶颈和两阶段训练 → 离散化/对齐的受限安全设计可核；不能从量化不连续授阻断adaptive梯度或通用安全，100%/minimal overhead不采用。`PLATFORM-SECURITY` | P，安全 |
| [2511.16317](SUP_AB_2511.16317_20261015.html)；Nov20 12:47:22 | multi-view图像baking有遮挡与mesh对齐问题 → dense 3D color-point VAE/DiT、geometry branch条件控制 → texture表示与采样应保原3D对应；需跨view/质量控制和from-scratch成本，不采全部泛化。`MULTIMODAL-GENERATIVE-PARADIGMS` | P |
| [2511.16423](SUP_AB_2511.16423_20261015.html)；Nov20 14:45:59 | 多轮federated VLM通信与异质性 → class prototype Bayesian个性化、text prompt全局对齐和自适应校准的一轮分支 → 不把training-free等同无估计/通信费用；需核哪些统计/权重被估计和标注权限，不因九数据集就排/收。`TRAIN-DISTRIBUTED-TRAINING`方向待具体owner | P |
| [2511.16450](SUP_AB_2511.16450_20261015.html)；Nov20 15:16:19 | 大模型传输/内存压力 → 摘要仅给FLARE message quantization/container/file streaming → 需最小接口/变更理由说明具体何种流控、buffer或消费者约束改变；不能仅把成熟量化/分片组合当准入，也不因无全实验关闭 | M，普通待补具体实现段 |
| [2511.16467](SUP_AB_2511.16467_20261015.html)；Nov20 15:35:50 | idiom非组合语义如何处理未知 → modified path patching找跨idiom heads与augmented reception → 局部circuit可能改变组件解释；需干预/负侧而非仅activation相关，不因语言题材/局部结果关闭。`WORLDVIEW-REPRESENTATION` | P |
| [2511.16501](SUP_AB_2511.16501_20261015.html)；Nov20 16:19:41 | ODE连续ViT训练/稳定性和离散teacher轨迹存在间隙 → wellposed/stable formulation＋teacher-guided轨迹训练 → 需要区分理想ODE条件与数值模型保证，不采CIFAR提分或fewer parameters作普遍效率。`MODEL-TRANSFORMER-LAYER` | P |
| [2511.16664](SUP_AB_2511.16664_20261015.html)；Nov20 18:59:21 | 每预算模型分别重训/蒸馏昂贵 → nested weight sharing/router curriculum与Mamba group-aware弹性 → submodel可提取不等所有预算质量/运行时常数内存，须核预算分母/实际共驻；不采360x/7x。`MODEL-MOE`/压缩路由待唯一owner | P |
| [2511.16883](SUP_AB_2511.16883_20261015.html)；Nov21 01:19:34 | 单固定成本/质量目标router欠个体偏好 → 异构user/query/model交互图和新用户/model适配 → 偏好表示与模型选择是独立可学边界；模拟user/LLM judge非真实偏好真值，不采百分比。`PLATFORM-GATEWAY`方向待唯一owner | P |
| [2511.16885](SUP_AB_2511.16885_20261015.html)；Nov21 01:43:28 | discrete训练与soft概念推理分布不匹配 → 概率加权embedding混hidden并RL整个latent过程 → 需核训练/推理状态与stable claim条件；不把soft表征当人类概念真值。`MODEL-TRANSFORMER-LAYER` | P |
| [2511.16917](SUP_AB_2511.16917_20261015.html)；Nov21 03:02:10 | text/image表示和任务不统一 → painted text渲成RGB，与自然图双向pixel-space flow/同backbone → OCR/渲染可表达与输出消费权限要保，不从cycle consistency推语义正确或通用智能。`MULTIMODAL-REPRESENTATION` | P |

原潜力足以进入必要证据阶段，准入P不等现在要全读全部实验；尚缺必要公开/修订资格不能评分或列确定当窗。每项current轻检/必要日期仍按本轮实际返回分责，未授全部current已核。

## 3. 必要日期原字段口径

上述fresh search cards把16883/16885/16917列Submitted20Nov；同本轮精确v1 title/citation/history分别Nov21 01:19:34、01:43:28、03:02:10UTC，原字段口径不同、时区/展示绑定未立，不断言站点日期错误；原值并存不择有利字段，citation_online_date不当public。16501与16664虽historyNov20，转换已在本轮BJT日后；不从submitted直接授首次公开或撤掉可能更早渠道责任。search recently-submitted只是发现，originally announced仅月份。不得据search卡强授当窗，精确版本必要公开/重大修订日期仍普通归并，不把候选数当本窗数。

## 4. 新重要安全/撤回优先项

实际本轮读[2509.10518当前](https://arxiv.org/abs/2509.10518) L8、18–30（[保存原件](SUP_WEB_SAFETY_FIRST_20261015.raw)）：官方withdrawn，作者comments明确significant errors；当前v2history为Nov21 00:59:21UTC、首v1Sep3。退出本次采用/评分/Books，保留原摘要存在不争取旧全文准入，不把撤回当访问故障或造假指控。search卡Submitted20与当前v2Nov21原字段冲突保留；本次撤回状态不是Nov20发生日证明。请Ohm实际核此必要反侧/关闭链，未扫全历史采用别名或共享Books，不自行删他人内容。

[2511.15992v1 Sleeper detector](https://arxiv.org/abs/2511.15992v1)完整题摘已在同原件实际读：safe baseline的SBERT drift与canary一致性双信号有受限检测设计潜力，不能以旧组件组合自动关闭；拟P，非100%precision/首个实用/zeroFP与生产实时保证。需要最小实际决策组合/评估人口才能决定增量是否仅串现成阈值，后续普通最小门；其v1historyNov20 02:42:41UTC与searchSubmitted19冲突保留，不由摘要或时间直接入选。该单篇不包含在§2的16计数，随后具体门另归并。
