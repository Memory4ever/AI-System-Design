# 03-20补03/19：原有限标题查询尾项初筛

作者resume_mar17，2026-10-12。仅原四query及已记录同义变体的相关/含糊标题；不新增query、不把全部分类变全文队列。当前41家族实际Books整合已接纳，但来源初筛未结束，不作最终分母或DAY。此处只维护尚未归并的题摘、日期和具体准入依据，不是Source/PRE验收。

## 九Agent尾项必要日字段

实际本次逐条HTTP200打开以下DataCite exact DOI，标题及URL与具名家族匹配。created/registered均如下UTC，Submitted仅作发现，不作为公开日期。沿用本日已实际核的arXiv官方availability约束：ID/DOI不预发，注册时间是公开上界；这些Submitted03/18的首次v1事件之最早可公开日与03/19登记上界均落03/19北京时间自然日。不是追求精确时刻，也不证明其他稿此前未公开；17823已有出版方03/14同稿，优先按窗前处理。具体light current和先稿身份见reader原九项准备。

| id与元数据入口 | 匹配题名 | created UTC | registered UTC |
| --- | --- | --- | --- |
| [2603.17973](https://api.datacite.org/dois/10.48550/arxiv.2603.17973) | TDAD: Test-Driven Agentic Development - Reducing Code Regressions in AI Coding Agents via Graph-Based Impact Analysis | 2026-03-19T02:44:59.000Z | 2026-03-19T02:45:00.000Z |
| [2603.17884](https://api.datacite.org/dois/10.48550/arxiv.2603.17884) | DebugLM: Learning Traceable Training Data Provenance for LLMs | 2026-03-19T02:42:51.000Z | 2026-03-19T02:42:52.000Z |
| [2603.17837](https://api.datacite.org/dois/10.48550/arxiv.2603.17837) | The Silent Thought: Modeling Internal Cognition in Full-Duplex Spoken Dialogue Models via Latent Reasoning | 2026-03-19T02:41:44.000Z | 2026-03-19T02:41:45.000Z |
| [2603.17831](https://api.datacite.org/dois/10.48550/arxiv.2603.17831) | RPMS: Enhancing LLM-Based Embodied Planning through Rule-Augmented Memory Synergy | 2026-03-19T02:41:36.000Z | 2026-03-19T02:41:36.000Z |
| [2603.17829](https://api.datacite.org/dois/10.48550/arxiv.2603.17829) | CodeScout: An Effective Recipe for Reinforcement Learning of Code Search Agents | 2026-03-19T02:41:33.000Z | 2026-03-19T02:41:34.000Z |
| [2603.17823](https://api.datacite.org/dois/10.48550/arxiv.2603.17823) | Discovering Decoupled Functional Modules in Large Language Models | 2026-03-19T02:41:24.000Z | 2026-03-19T02:41:25.000Z |
| [2603.17787](https://api.datacite.org/dois/10.48550/arxiv.2603.17787) | Governed Memory: A Production Architecture for Multi-Agent Workflows | 2026-03-19T02:40:33.000Z | 2026-03-19T02:40:34.000Z |
| [2603.17781](https://api.datacite.org/dois/10.48550/arxiv.2603.17781) | Facts as First Class Objects: Knowledge Objects for Persistent LLM Memory | 2026-03-19T02:40:25.000Z | 2026-03-19T02:40:25.000Z |
| [2603.17775](https://api.datacite.org/dois/10.48550/arxiv.2603.17775) | CoVerRL: Breaking the Consensus Trap in Label-Free Reasoning via Generator-Verifier Co-Evolution | 2026-03-19T02:40:16.000Z | 2026-03-19T02:40:17.000Z |

日期只支持本次arXiv事件归属。尚未确认的新先稿信号另核；八个潜力提案待作者非准备者完整题摘/决定准入核心独校，不由上述字段给分或授Evidence。

## 原尾第一明确潜力批22（待非作者准入校准）

这些具体增量仅完整题摘阶段，分数是提案；下面owner为候选主线定位，不自动Books。全部exact DOI HTTP200 id/title/url已实际匹配，created/registered原字段及current轻量说明见随后JSON；均03/19UTC登记，沿用本日官方availability必要下界夹证推断03/19BJT首次arXiv事件，不能据此清除明确先稿信号。CVPR/ICME/WWW accepted本身不授旧稿日期；具体正文信号才定点恢复。current Identity题摘明确multisubject binding/sharedidentity/caption；STAS新增padding/残差缩放解释，FMER明确tanh/ESS条件，均只定点受影响方法/评价，不机械全版本diff。未采用摘要性能/安全/无损数字。

| 身份 | 原约束→实际增量→设计选择 | 评分提案 | 候选owner |
| --- | --- | --- | --- |
| [Identity-as-Presence2603.17889v1](https://arxiv.org/abs/2603.17889v1) | 单人外观/音色条件不能保证多人身份配对→成对AV identity注入与分阶段数据→需核跨模态同对象绑定和modality imbalance条件 | 2+2+2=6 | MULTIMODAL-REPRESENTATION |
| [ProbeFlow2603.17850v1](https://arxiv.org/abs/2603.17850v1) | 固定FM solver预算忽略动作复杂度→初始/lookahead速度cosine选择积分步→需核proxy与actioncriticalpath/成功率/全费取舍 | 2+2+2=6 | MULTIMODAL-EMBODIED-VLA |
| [GeCO2603.17834v1](https://arxiv.org/abs/2603.17834v1) | time-conditioned轨迹固定积分→stationary action velocity与收敛退出→需重核生成训练/迭代停止和fieldnorm诊断资格 | 2+2+2=6 | MULTIMODAL-EMBODIED-VLA |
| [STAS2603.17825v1](https://arxiv.org/abs/2603.17825v1) | DiT大activation不只是坏outlier→时空边界/早去噪分布及定点缩放→需核padding/残差更新与生成质量适用性 | 2+1+2=5 | MULTIMODAL-GENERATIVE-PARADIGMS |
| [ChopGrad2603.17812v1](https://arxiv.org/abs/2603.17812v1) | recurrent视频VAE像素loss使全序列反传存储增长→localwindow截断→需核梯度近似与pixel优化memory/质量成立条件 | 2+2+2=6 | MULTIMODAL-GENERATIVE-PARADIGMS |
| [EVA2603.17808v1](https://arxiv.org/abs/2603.17808v1) | 视觉自洽rollout经IDM可能不可执行→实轨IDM诱导速度/加速度/jerk及本体约束reward→需分验视频proposal和动作可执行奖励 | 2+2+2=6 | MULTIMODAL-WORLD-MODELS |
| [TAPESTRY2603.17735v1](https://arxiv.org/abs/2603.17735v1) | 通用视频不能保全旋转几何→显式mesh多模态条件与遮挡二次生成→需核几何载荷/生成和UV或3DGS消费的共存边界 | 2+2+2=6 | MULTIMODAL-WORLD-MODELS |
| [SynRL2603.17693v1](https://arxiv.org/abs/2603.17693v1) | 视频题可能单帧可答/teacher时间错误→代码生成temporalprimitive与framegold→需核数据人口和真正时序能力而非样本数量排行 | 2+2+2=6 | TRAIN-DATA |
| [AgentVLN2603.17670v1](https://arxiv.org/abs/2603.17670v1) | VLM2D语义与3D waypoint/单目尺度失配→几何投影为pixelprompt、主动depthquery及visibility路由→需核观测请求与行动条件 | 2+2+2=6 | MULTIMODAL-EMBODIED-VLA |
| [VectorWorld2603.17652v1](https://arxiv.org/abs/2603.17652v1) | historyless初始化/连续tile生成/动力学累积失配→motion-gatedVAE、vectorgraph one-stepMeanFlow及NPC shaping→需核policy输入/生成成本和闭环评价 | 2+2+2=6 | MULTIMODAL-WORLD-MODELS |
| [S-VGGT2603.17625v1](https://arxiv.org/abs/2603.17625v1) | 全局attention长capture平方增长→scenegraph软分scene且共享reference独立处理→需核拼接几何/结构冗余和token法组合取舍 | 2+2+2=6 | MULTIMODAL-REPRESENTATION |
| [KeyframeAnchoring2603.17651v1](https://arxiv.org/abs/2603.17651v1) | 固定端点未指定中间语义路径→keyframe attention bias与temporalRoPE rescale→需核端点/文字条件的时间节奏与一致性取舍 | 2+1+2=5 | MULTIMODAL-GENERATIVE-PARADIGMS |
| [GSU2603.17333v1](https://arxiv.org/abs/2603.17333v1) | 视觉识别错误混入空间推理评价→textgrid去感知后测referenceframe/3Dcoords→需核视觉经验是否真正转移空间规则 | 2+1+2=5 | PLATFORM-EVALUATION-SYSTEM |
| [BiasRecBench2603.17417v1](https://arxiv.org/abs/2603.17417v1) | 排行把偏好合理化与质量最优混合→校准qualitymargin并注入contextbias→需核推荐agent有理由却选错的评价盲区 | 2+1+2=5 | PLATFORM-EVALUATION-SYSTEM |
| [RAMP2603.17891v1](https://arxiv.org/abs/2603.17891v1) | uniformbits忽略层敏感/预算→SAC层统计配置与ScaleFolding/Norm补偿→需核跨模型bit选择和表示→artifact执行边界 | 2+2+2=6 | INFER-TENSORRT-LLM |
| [FMER2603.17685v1](https://arxiv.org/abs/2603.17685v1) | diffusion在线RL反传长solver/entropy困难→advantageweightedCFM镜像代理与tanh密度修正→需核不用solver反传的策略优化成立条件 | 2+2+2=6 | TRAIN-PPO |
| [Ruyi2.52603.17311v1](https://arxiv.org/abs/2603.17311v1) | 多尺度独立训练/端云raw传输/响应级RL冗余→sharedbackbone共训、IB派生传输与binaryprefix更新→需核同family多个接口各自成立边界不授隐私/加速保证 | 2+2+2=6 | TRAIN-PRETRAINING |
| [OmniVLN2603.17351v1](https://arxiv.org/abs/2603.17351v1) | 密集3D或平铺objects超context且视野碎片→五层DSG/持续拓扑与egocentric3Doctant多粒度提示→需核几何压缩后的定位/行动消费者 | 2+2+2=6 | MULTIMODAL-EMBODIED-VLA |
| [FineViT2603.17326v1](https://arxiv.org/abs/2603.17326v1) | coarsecaption/低native分辨率丢局部细节→globaldense预训练后localcaptionLLM对齐→需核视觉encoder能力形成的人口/目标与MLLM消费 | 2+2+2=6 | MULTIMODAL-REPRESENTATION |
| [VLM2Rec2603.17450v1](https://arxiv.org/abs/2603.17450v1) | VLM embedding SFT会放大modalityimbalance→弱模态contrastive惩罚与拓扑保持→需核训练目标改变而非仅推荐排行 | 2+1+2=5 | MULTIMODAL-REPRESENTATION |
| [MCoT-MVS2603.17360v1](https://arxiv.org/abs/2603.17360v1) | reference+修改文本的全图embedding混入不该保留语义→retained/removed/target描述驱动patch/instance选择→需核生成解释到retrieval表示接口非CoT真值 | 2+1+2=5 | MULTIMODAL-REPRESENTATION |
| [FloorPlan-VLN2603.17437v1](https://arxiv.org/abs/2603.17437v1) | 无全局prior需繁琐指令→floorplan+aligneddualviews与conciseinstructions→需核先验特权/失真与执行路径边界 | 2+1+2=5 | MULTIMODAL-EMBODIED-VLA |

### 原42必要匹配date字段

```json
[
  {
    "id": "17311",
    "status": 200,
    "title": [
      {
        "title": "Ruyi2.5 Technical Report"
      }
    ],
    "url": "https://arxiv.org/abs/2603.17311",
    "created": "2026-03-19T02:29:09.000Z",
    "registered": "2026-03-19T02:29:10.000Z"
  },
  {
    "id": "17328",
    "status": 200,
    "title": [
      {
        "title": "A Progressive Visual-Logic-Aligned Framework for Ride-Hailing Adjudication"
      }
    ],
    "url": "https://arxiv.org/abs/2603.17328",
    "created": "2026-03-19T02:29:34.000Z",
    "registered": "2026-03-19T02:29:34.000Z"
  },
  {
    "id": "17326",
    "status": 200,
    "title": [
      {
        "title": "FineViT: Progressively Unlocking Fine-Grained Perception with Dense Recaptions"
      }
    ],
    "url": "https://arxiv.org/abs/2603.17326",
    "created": "2026-03-19T02:29:30.000Z",
    "registered": "2026-03-19T02:29:31.000Z"
  },
  {
    "id": "17301",
    "status": 200,
    "title": [
      {
        "title": "WINFlowNets: Warm-up Integrated Networks Training of Generative Flow Networks for Robotics and Machine Fault Adaptation"
      }
    ],
    "url": "https://arxiv.org/abs/2603.17301",
    "created": "2026-03-19T02:28:55.000Z",
    "registered": "2026-03-19T02:28:56.000Z"
  },
  {
    "id": "17333",
    "status": 200,
    "title": [
      {
        "title": "Grid Spatial Understanding: A Dataset for Textual Spatial Reasoning over Grids, Embodied Settings, and Coordinate Structures"
      }
    ],
    "url": "https://arxiv.org/abs/2603.17333",
    "created": "2026-03-19T02:29:41.000Z",
    "registered": "2026-03-19T02:29:42.000Z"
  },
  {
    "id": "17351",
    "status": 200,
    "title": [
      {
        "title": "OmniVLN: Omnidirectional 3D Perception and Token-Efficient LLM Reasoning for Visual-Language Navigation across Air and Ground Platforms"
      }
    ],
    "url": "https://arxiv.org/abs/2603.17351",
    "created": "2026-03-19T02:30:07.000Z",
    "registered": "2026-03-19T02:30:08.000Z"
  },
  {
    "id": "17419",
    "status": 200,
    "title": [
      {
        "title": "Caging the Agents: A Zero Trust Security Architecture for Autonomous AI in Healthcare"
      }
    ],
    "url": "https://arxiv.org/abs/2603.17419",
    "created": "2026-03-19T02:31:46.000Z",
    "registered": "2026-03-19T02:31:46.000Z"
  },
  {
    "id": "17386",
    "status": 200,
    "title": [
      {
        "title": "PJB: A Reasoning-Aware Benchmark for Person-Job Retrieval"
      }
    ],
    "url": "https://arxiv.org/abs/2603.17386",
    "created": "2026-03-19T02:30:58.000Z",
    "registered": "2026-03-19T02:30:58.000Z"
  },
  {
    "id": "17450",
    "status": 200,
    "title": [
      {
        "title": "VLM2Rec: Resolving Modality Collapse in Vision-Language Model Embedders for Multimodal Sequential Recommendation"
      }
    ],
    "url": "https://arxiv.org/abs/2603.17450",
    "created": "2026-03-19T02:32:33.000Z",
    "registered": "2026-03-19T02:32:33.000Z"
  },
  {
    "id": "17417",
    "status": 200,
    "title": [
      {
        "title": "Is Your LLM-as-a-Recommender Agent Trustable? LLMs' Recommendation is Easily Hacked by Biases (Preferences)"
      }
    ],
    "url": "https://arxiv.org/abs/2603.17417",
    "created": "2026-03-19T02:31:43.000Z",
    "registered": "2026-03-19T02:31:44.000Z"
  },
  {
    "id": "17360",
    "status": 200,
    "title": [
      {
        "title": "MCoT-MVS: Multi-level Vision Selection by Multi-modal Chain-of-Thought Reasoning for Composed Image Retrieval"
      }
    ],
    "url": "https://arxiv.org/abs/2603.17360",
    "created": "2026-03-19T02:30:20.000Z",
    "registered": "2026-03-19T02:30:21.000Z"
  },
  {
    "id": "17437",
    "status": 200,
    "title": [
      {
        "title": "FloorPlan-VLN: A New Paradigm for Floor Plan Guided Vision-Language Navigation"
      }
    ],
    "url": "https://arxiv.org/abs/2603.17437",
    "created": "2026-03-19T02:32:14.000Z",
    "registered": "2026-03-19T02:32:14.000Z"
  },
  {
    "id": "17474",
    "status": 200,
    "title": [
      {
        "title": "Revisiting Cross-Attention Mechanisms: Leveraging Beneficial Noise for Domain-Adaptive Learning"
      }
    ],
    "url": "https://arxiv.org/abs/2603.17474",
    "created": "2026-03-19T02:33:07.000Z",
    "registered": "2026-03-19T02:33:08.000Z"
  },
  {
    "id": "17507",
    "status": 200,
    "title": [
      {
        "title": "QuantFL: Sustainable Federated Learning for Edge IoT via Pre-Trained Model Quantisation"
      }
    ],
    "url": "https://arxiv.org/abs/2603.17507",
    "created": "2026-03-19T02:33:55.000Z",
    "registered": "2026-03-19T02:33:56.000Z"
  },
  {
    "id": "17520",
    "status": 200,
    "title": [
      {
        "title": "PCA-Seg: Revisiting Cost Aggregation for Open-Vocabulary Semantic and Part Segmentation"
      }
    ],
    "url": "https://arxiv.org/abs/2603.17520",
    "created": "2026-03-19T02:34:14.000Z",
    "registered": "2026-03-19T02:34:15.000Z"
  },
  {
    "id": "17475",
    "status": 200,
    "title": [
      {
        "title": "Humans and transformer LMs: Abstraction drives language learning"
      }
    ],
    "url": "https://arxiv.org/abs/2603.17475",
    "created": "2026-03-19T02:33:09.000Z",
    "registered": "2026-03-19T02:33:10.000Z"
  },
  {
    "id": "17470",
    "status": 200,
    "title": [
      {
        "title": "VirPro: Visual-referred Probabilistic Prompt Learning for Weakly-Supervised Monocular 3D Detection"
      }
    ],
    "url": "https://arxiv.org/abs/2603.17470",
    "created": "2026-03-19T02:33:02.000Z",
    "registered": "2026-03-19T02:33:02.000Z"
  },
  {
    "id": "17510",
    "status": 200,
    "title": [
      {
        "title": "Interpreting Context-Aware Human Preferences for Multi-Objective Robot Navigation"
      }
    ],
    "url": "https://arxiv.org/abs/2603.17510",
    "created": "2026-03-19T02:33:59.000Z",
    "registered": "2026-03-19T02:34:00.000Z"
  },
  {
    "id": "17625",
    "status": 200,
    "title": [
      {
        "title": "S-VGGT: Structure-Aware Subscene Decomposition for Scalable 3D Foundation Models"
      }
    ],
    "url": "https://arxiv.org/abs/2603.17625",
    "created": "2026-03-19T02:36:44.000Z",
    "registered": "2026-03-19T02:36:44.000Z"
  },
  {
    "id": "17570",
    "status": 200,
    "title": [
      {
        "title": "FoMo X: Modular Explainability Signals for Outlier Detection Foundation Models"
      }
    ],
    "url": "https://arxiv.org/abs/2603.17570",
    "created": "2026-03-19T02:35:25.000Z",
    "registered": "2026-03-19T02:35:26.000Z"
  },
  {
    "id": "17652",
    "status": 200,
    "title": [
      {
        "title": "VectorWorld: Efficient Streaming World Model via Diffusion Flow on Vector Graphs"
      }
    ],
    "url": "https://arxiv.org/abs/2603.17652",
    "created": "2026-03-19T02:37:22.000Z",
    "registered": "2026-03-19T02:37:23.000Z"
  },
  {
    "id": "17605",
    "status": 200,
    "title": [
      {
        "title": "ReLaGS: Relational Language Gaussian Splatting"
      }
    ],
    "url": "https://arxiv.org/abs/2603.17605",
    "created": "2026-03-19T02:36:16.000Z",
    "registered": "2026-03-19T02:36:16.000Z"
  },
  {
    "id": "17651",
    "status": 200,
    "title": [
      {
        "title": "Anchoring and Rescaling Attention for Semantically Coherent Inbetweening"
      }
    ],
    "url": "https://arxiv.org/abs/2603.17651",
    "created": "2026-03-19T02:37:21.000Z",
    "registered": "2026-03-19T02:37:22.000Z"
  },
  {
    "id": "17527",
    "status": 200,
    "title": [
      {
        "title": "Mirror Descent on Riemannian Manifolds"
      }
    ],
    "url": "https://arxiv.org/abs/2603.17527",
    "created": "2026-03-19T02:34:24.000Z",
    "registered": "2026-03-19T02:34:25.000Z"
  },
  {
    "id": "17692",
    "status": 200,
    "title": [
      {
        "title": "Can Blindfolded LLMs Still Trade? An Anonymization-First Framework for Portfolio Optimization"
      }
    ],
    "url": "https://arxiv.org/abs/2603.17692",
    "created": "2026-03-19T02:38:18.000Z",
    "registered": "2026-03-19T02:38:18.000Z"
  },
  {
    "id": "17670",
    "status": 200,
    "title": [
      {
        "title": "AgentVLN: Towards Agentic Vision-and-Language Navigation"
      }
    ],
    "url": "https://arxiv.org/abs/2603.17670",
    "created": "2026-03-19T02:37:47.000Z",
    "registered": "2026-03-19T02:37:48.000Z"
  },
  {
    "id": "17735",
    "status": 200,
    "title": [
      {
        "title": "TAPESTRY: From Geometry to Appearance via Consistent Turntable Videos"
      }
    ],
    "url": "https://arxiv.org/abs/2603.17735",
    "created": "2026-03-19T02:39:18.000Z",
    "registered": "2026-03-19T02:39:19.000Z"
  },
  {
    "id": "17685",
    "status": 200,
    "title": [
      {
        "title": "Flow Matching Policy Optimization with Mirror Descent and Entropy Constraints"
      }
    ],
    "url": "https://arxiv.org/abs/2603.17685",
    "created": "2026-03-19T02:38:08.000Z",
    "registered": "2026-03-19T02:38:09.000Z"
  },
  {
    "id": "17693",
    "status": 200,
    "title": [
      {
        "title": "Learning Transferable Temporal Primitives for Video Reasoning via Synthetic Videos"
      }
    ],
    "url": "https://arxiv.org/abs/2603.17693",
    "created": "2026-03-19T02:38:19.000Z",
    "registered": "2026-03-19T02:38:20.000Z"
  },
  {
    "id": "17655",
    "status": 200,
    "title": [
      {
        "title": "Interpretable Cross-Domain Few-Shot Learning with Rectified Target-Domain Local Alignment"
      }
    ],
    "url": "https://arxiv.org/abs/2603.17655",
    "created": "2026-03-19T02:37:27.000Z",
    "registered": "2026-03-19T02:37:27.000Z"
  },
  {
    "id": "17782",
    "status": 200,
    "title": [
      {
        "title": "Exploring parameter-efficient fine-tuning (PEFT) of billion-parameter vision models with QLoRA and DoRA: insights into generalization for limited-data image classification under a 98:1 test-to-train regime"
      }
    ],
    "url": "https://arxiv.org/abs/2603.17782",
    "created": "2026-03-19T02:40:26.000Z",
    "registered": "2026-03-19T02:40:27.000Z"
  },
  {
    "id": "17812",
    "status": 200,
    "title": [
      {
        "title": "ChopGrad: Pixel-Wise Losses for Latent Video Diffusion via Truncated Backpropagation"
      }
    ],
    "url": "https://arxiv.org/abs/2603.17812",
    "created": "2026-03-19T02:41:09.000Z",
    "registered": "2026-03-19T02:41:10.000Z"
  },
  {
    "id": "17825",
    "status": 200,
    "title": [
      {
        "title": "Steering Video Diffusion Transformers with Massive Activations"
      }
    ],
    "url": "https://arxiv.org/abs/2603.17825",
    "created": "2026-03-19T02:41:27.000Z",
    "registered": "2026-03-19T02:41:28.000Z"
  },
  {
    "id": "17808",
    "status": 200,
    "title": [
      {
        "title": "EVA: Aligning Video World Models with Executable Robot Actions via Inverse Dynamics Rewards"
      }
    ],
    "url": "https://arxiv.org/abs/2603.17808",
    "created": "2026-03-19T02:41:03.000Z",
    "registered": "2026-03-19T02:41:03.000Z"
  },
  {
    "id": "17761",
    "status": 200,
    "title": [
      {
        "title": "Evidence Packing for Cross-Domain Image Deepfake Detection with LVLMs"
      }
    ],
    "url": "https://arxiv.org/abs/2603.17761",
    "created": "2026-03-19T02:39:56.000Z",
    "registered": "2026-03-19T02:39:57.000Z"
  },
  {
    "id": "17813",
    "status": 200,
    "title": [
      {
        "title": "M2P: Improving Visual Foundation Models with Mask-to-Point Weakly-Supervised Learning for Dense Point Tracking"
      }
    ],
    "url": "https://arxiv.org/abs/2603.17813",
    "created": "2026-03-19T02:41:10.000Z",
    "registered": "2026-03-19T02:41:11.000Z"
  },
  {
    "id": "17889",
    "status": 200,
    "title": [
      {
        "title": "Identity as Presence: Towards Appearance and Voice Personalized Joint Audio-Video Generation"
      }
    ],
    "url": "https://arxiv.org/abs/2603.17889",
    "created": "2026-03-19T02:42:58.000Z",
    "registered": "2026-03-19T02:42:59.000Z"
  },
  {
    "id": "17952",
    "status": 200,
    "title": [
      {
        "title": "Gender Disambiguation in Machine Translation: Diagnostic Evaluation in Decoder-Only Architectures"
      }
    ],
    "url": "https://arxiv.org/abs/2603.17952",
    "created": "2026-03-19T02:44:28.000Z",
    "registered": "2026-03-19T02:44:29.000Z"
  },
  {
    "id": "17840",
    "status": 200,
    "title": [
      {
        "title": "Video Understanding: From Geometry and Semantics to Unified Models"
      }
    ],
    "url": "https://arxiv.org/abs/2603.17840",
    "created": "2026-03-19T02:41:48.000Z",
    "registered": "2026-03-19T02:41:49.000Z"
  },
  {
    "id": "17850",
    "status": 200,
    "title": [
      {
        "title": "ProbeFlow: Training-Free Adaptive Flow Matching for Vision-Language-Action Models"
      }
    ],
    "url": "https://arxiv.org/abs/2603.17850",
    "created": "2026-03-19T02:42:03.000Z",
    "registered": "2026-03-19T02:42:04.000Z"
  },
  {
    "id": "17834",
    "status": 200,
    "title": [
      {
        "title": "Generative Control as Optimization: Time Unconditional Flow Matching for Adaptive and Robust Robotic Control"
      }
    ],
    "url": "https://arxiv.org/abs/2603.17834",
    "created": "2026-03-19T02:41:40.000Z",
    "registered": "2026-03-19T02:41:41.000Z"
  },
  {
    "id": "17891",
    "status": 200,
    "title": [
      {
        "title": "RAMP: Reinforcement Adaptive Mixed Precision Quantization for Efficient On Device LLM Inference"
      }
    ],
    "url": "https://arxiv.org/abs/2603.17891",
    "created": "2026-03-19T02:43:01.000Z",
    "registered": "2026-03-19T02:43:02.000Z"
  }
]
```

### 本22current官方abs轻量原字段

```json
[
  {
    "id": "17889",
    "status": 200,
    "title": "Title: Identity as Presence: Towards Appearance and Voice Personalized Joint Audio-Video Generation",
    "comments": "",
    "abstract": "Abstract: Recent advances in video synthesis have enabled realistic integration of real individuals, driving demand for identity-aware generation. While emerging methods support joint appearance and voice injection in audio-visual models, they primarily focus on single-subject settings. Multimodal identity integration across multiple subjects remains limited, and precise alignment between visual and vocal identities in multi-subject scenarios remains underexplored. We present Identity-as-Presence, a unified framework for joint personalized audio-video generation. An automated data curation pipeline constructs identity-labeled audio-visual pairs for single- and multi-subject scenes. A unified identity injection mechanism then binds paired appearance and voice through shared cross-modal identity binding and subject-anchored captions. A multi-stage training strategy further leverages large-scale unimodal data alongside scarce paired clips to mitigate modality imbalance. Experiments show superior audio quality, video fidelity, and audio-visual consistency, with stronger multi-subject binding than the compared methods. For more details and qualitative results, please refer to our webpage: \\href{ this https URL }{Identity-as-Presence}."
  },
  {
    "id": "17834",
    "status": 200,
    "title": "Title: Generative Control as Optimization: Time Unconditional Flow Matching for Adaptive and Robust Robotic Control",
    "comments": "18 pages, 6 figures",
    "abstract": "Abstract: Diffusion models and flow matching have become a cornerstone of robotic imitation learning, yet they suffer from a structural inefficiency where inference is often bound to a fixed integration schedule that is agnostic to state complexity. This paradigm forces the policy to expend the same computational budget on trivial motions as it does on complex tasks. We introduce Generative Control as Optimization (GeCO), a time-unconditional framework that transforms action synthesis from trajectory integration into iterative optimization. GeCO learns a stationary velocity field in the action-sequence space where expert behaviors form stable attractors. Consequently, test-time inference becomes an adaptive process that allocates computation based on convergence--exiting early for simple states while refining longer for difficult ones. Furthermore, this stationary geometry yields an intrinsic, training-free safety signal, as the field norm at the optimized action serves as a robust out-of-distribution (OOD) detector, remaining low for in-distribution states while significantly increasing for anomalies. We validate GeCO on standard simulation benchmarks and demonstrate seamless scaling to pi0-series Vision-Language-Action (VLA) models. As a plug-and-play replacement for standard flow-matching heads, GeCO improves success rates and efficiency with an optimization-native mechanism for safe deployment. Video and code can be found at this https URL"
  },
  {
    "id": "17812",
    "status": 200,
    "title": "Title: ChopGrad: Pixel-Wise Losses for Latent Video Diffusion via Truncated Backpropagation",
    "comments": "Project website: this https URL",
    "abstract": "Abstract: Recent video diffusion models achieve high-quality generation through recurrent frame processing where each frame generation depends on previous frames. However, this recurrent mechanism means that training such models in the pixel domain incurs prohibitive memory costs, as activations accumulate across the entire video sequence. This fundamental limitation also makes fine-tuning these models with pixel-wise losses computationally intractable for long or high-resolution videos. This paper introduces ChopGrad, a truncated backpropagation scheme for video decoding, limiting gradient computation to local frame windows while maintaining global consistency. We provide a theoretical analysis of this approximation and show that it enables efficient fine-tuning with frame-wise losses. ChopGrad reduces training memory from scaling linearly with the number of video frames (full backpropagation) to constant memory, and compares favorably to existing state-of-the-art video diffusion models across a suite of conditional video generation tasks with pixel-wise losses, including video super-resolution, video inpainting, video enhancement of neural-rendered scenes, and controlled driving video generation."
  },
  {
    "id": "17850",
    "status": 200,
    "title": "Title: ProbeFlow: Training-Free Adaptive Flow Matching for Vision-Language-Action Models",
    "comments": "",
    "abstract": "Abstract: Recent Vision-Language-Action (VLA) models equipped with Flow Matching (FM) action heads achieve state-of-the-art performance in complex robot manipulation. However, the multi-step iterative ODE solving required by FM introduces inference latency that precludes responsive physical control. While current acceleration efforts optimize the Vision-Language Model (VLM) backbone, the action head bottleneck remains overlooked. To address this, we propose ProbeFlow, a training-free adaptive inference framework tai- lored for continuous robotic control. By evaluating geometric trajectory complexity via the cosine similarity between initial and lookahead velocity vectors, ProbeFlow dynamically sched- ules integration steps to prune redundant network evaluations. On the MetaWorld benchmark, it accelerates action decoding by 14.8x (reducing average steps from N = 50 to 2.6) and cuts end-to-end system latency by 2.8x without compromising the manipulation success rate. On the long-horizon LIBERO benchmark, the probe automatically allocates a denser schedule to navigate semantic bottlenecks, effectively resolving the flow solver delay. Real-world physical deployments confirm that ProbeFlow successfully mitigates action decoding latency while ensuring execution stability, offering a highly practical solution for low-latency continuous generative policies."
  },
  {
    "id": "17825",
    "status": 200,
    "title": "Title: Steering Video Diffusion Transformers with Massive Activations",
    "comments": "",
    "abstract": "Abstract: In this work, we study the role of Massive Activations (MAs), which are rare, high-magnitude spikes confined to a few fixed hidden dimensions in video diffusion transformers (DiTs). We uncover a structured positional hierarchy: MA magnitudes peak at first-frame tokens and recur at the spatial boundary tokens of latent frames, with this pattern being most pronounced during early denoising. We trace this organization to an encoding asymmetry of the video VAEs, whose causal temporal padding and zero spatial padding cause the first latent frame and frame borders to carry reduced content load. Elevated MAs consistently align with these lower-content structural positions. To understand their function, we analyze intermediate representations and find that MAs act as implicit rescalers of residual computation: enlarging MAs suppresses the corresponding self-attention and feed-forward updates, while erasing them amplifies these updates. Together, these observations suggest that MAs serves as a token-level rescaler of residual computation, which video DiTs deploy unevenly, placing the strongest damping at the encoding-asymmetric structural positions. Motivated by this native rescaling behavior, we propose Structured Activation Steering (STAS), a training-free technique that steers MAs at the observed structural positions toward a scaled, model-derived reference during early denoising. STAS requires no additional forward passes and consistently improves video quality and temporal coherence across text-to-video models with negligible overhead."
  },
  {
    "id": "17693",
    "status": 200,
    "title": "Title: Learning Transferable Temporal Primitives for Video Reasoning via Synthetic Videos",
    "comments": "",
    "abstract": "Abstract: The transition from image to video understanding requires vision-language models (VLMs) to shift from recognizing static patterns to reasoning over temporal dynamics such as motion trajectories, speed changes, and state transitions. Yet current post-training methods fall short due to two critical limitations: (1) existing datasets often lack temporal-centricity, where answers can be inferred from isolated keyframes rather than requiring holistic temporal integration; and (2) training data generated by proprietary models contains systematic errors in fundamental temporal perception, such as confusing motion directions or misjudging speeds. We introduce SynRL, a post-training framework that teaches models temporal primitives, the fundamental building blocks of temporal understanding including direction, speed, and state tracking. Our key insight is that these abstract primitives, learned from programmatically generated synthetic videos, transfer effectively to real-world scenarios. We decompose temporal understanding into short-term perceptual primitives (speed, direction) and long-term cognitive primitives, constructing 7.7K CoT and 7K RL samples with ground-truth frame-level annotations through code-based video generation. Despite training on simple geometric shapes, SynRL achieves substantial improvements across 15 benchmarks spanning temporal grounding, complex reasoning, and general video understanding. Remarkably, our 7.7K synthetic CoT samples outperform Video-R1 with 165K real-world samples. We attribute this to fundamental temporal skills, such as tracking frame by frame changes and comparing velocity, that transfer effectively from abstract synthetic patterns to complex real-world scenarios. This establishes a new paradigm for video post-training: video temporal learning through carefully designed synthetic data provides a more cost efficient scaling path."
  },
  {
    "id": "17808",
    "status": 200,
    "title": "Title: EVA: Aligning Video World Models with Executable Robot Actions via Inverse Dynamics Rewards",
    "comments": "Project page: this https URL",
    "abstract": "Abstract: Video generative models are increasingly used as world models for robotics, where a model generates a future visual rollout conditioned on the current observation and task instruction, and an inverse dynamics model (IDM) converts the generated frames into executable robot actions. However, current video world models lack explicit executability constraints. As a result, visually coherent rollouts may still violate rigid-body and kinematic consistency, producing unstable or infeasible control commands when decoded by an IDM. We refer to this mismatch between visual generation and physically executable control as the executability gap. While this gap can be mitigated at inference time using techniques such as rejection sampling, such approaches are inefficient due to the high cost of video generation. In this paper, we leverage the executability gap as a training signal and introduce Executable Video Alignment (EVA), a reinforcement-learning post-training framework for aligning video world models. EVA trains an inverse dynamics model on real robot trajectories and repurposes it as a reward model that evaluates generated videos through the action sequences they induce, encouraging smooth motions measured by velocity, acceleration, and jerk while penalizing actions that violate embodiment constraints. Importantly, the reward remains informative even when generated videos contain severe visual artifacts, since such artifacts typically translate into unstable or out-of-bound actions. Experiments on the RoboTwin benchmark and a real bimanual robot show that EVA reduces embodiment-specific artifacts in generated rollouts and improves downstream task execution success."
  },
  {
    "id": "17652",
    "status": 200,
    "title": "Title: VectorWorld: Efficient Streaming World Model via Diffusion Flow on Vector Graphs",
    "comments": "Under Review",
    "abstract": "Abstract: Closed-loop evaluation of autonomous-driving policies requires interactive simulation beyond log replay. However, existing generative world models often degrade in closed loop due to (i) history-free initialization that mismatches policy inputs, (ii) multi-step sampling latency that violates real-time budgets, and (iii) compounding kinematic infeasibility over long horizons. We propose VectorWorld, a streaming world model that incrementally generates ego-centric $64 \\mathrm{m}\\times 64\\mathrm{m}$ lane--agent vector-graph tiles during rollout. VectorWorld aligns initialization with history-conditioned policies by producing a policy-compatible interaction state via a motion-aware gated VAE. It enables real-time outpainting via solver-free one-step masked completion with an edge-gated relational DiT trained with interval-conditioned MeanFlow and JVP-based large-step supervision. To stabilize long-horizon rollouts, we introduce $\\Delta$Sim, a physics-aligned non-ego (NPC) policy with hybrid discrete--continuous actions and differentiable kinematic logit shaping. On Waymo open motion and nuPlan, VectorWorld improves map-structure fidelity and initialization validity, and supports stable, real-time $1\\mathrm{km}+$ closed-loop rollouts (\\href{ this https URL }{code})."
  },
  {
    "id": "17670",
    "status": 200,
    "title": "Title: AgentVLN: Towards Agentic Vision-and-Language Navigation",
    "comments": "19pages, 4 figures",
    "abstract": "Abstract: Vision-and-Language Navigation (VLN) requires an embodied agent to ground complex natural-language instructions into long-horizon navigation in unseen environments. While Vision-Language Models (VLMs) offer strong 2D semantic understanding, current VLN systems remain constrained by limited spatial perception, 2D-3D representation mismatch, and monocular scale ambiguity. In this paper, we propose AgentVLN, a novel and efficient embodied navigation framework that can be deployed on edge computing platforms. We formulate VLN as a Partially Observable Semi-Markov Decision Process (POSMDP) and introduce a VLM-as-Brain paradigm that decouples high-level semantic reasoning from perception and planning via a plug-and-play skill library. To resolve multi-level representation inconsistency, we design a cross-space representation mapping that projects perception-layer 3D topological waypoints into the image plane, yielding pixel-aligned visual prompts for the VLM. Building on this bridge, we integrate a context-aware self-correction and active exploration strategy to recover from occlusions and suppress error accumulation over long trajectories. To further address the spatial ambiguity of instructions in unstructured environments, we propose a Query-Driven Perceptual Chain-of-Thought (QD-PCoT) scheme, enabling the agent with the metacognitive ability to actively seek geometric depth information. Finally, we construct AgentVLN-Instruct, a large-scale instruction-tuning dataset with dynamic stage routing conditioned on target visibility. Extensive experiments show that AgentVLN consistently outperforms prior state-of-the-art methods (SOTA) on long-horizon VLN benchmarks, offering a practical paradigm for lightweight deployment of next-generation embodied navigation models. Code: this https URL ."
  },
  {
    "id": "17735",
    "status": 200,
    "title": "Title: TAPESTRY: From Geometry to Appearance via Consistent Turntable Videos",
    "comments": "",
    "abstract": "Abstract: Automatically generating photorealistic and self-consistent appearances for untextured 3D models is a critical challenge in digital content creation. The advancement of large-scale video generation models offers a natural approach: directly synthesizing 360-degree turntable videos (TTVs), which can serve not only as high-quality dynamic previews but also as an intermediate representation to drive texture synthesis and neural rendering. However, existing general-purpose video diffusion models struggle to maintain strict geometric consistency and appearance stability across the full range of views, making their outputs ill-suited for high-quality 3D reconstruction. To this end, we introduce TAPESTRY, a framework for generating high-fidelity TTVs conditioned on explicit 3D geometry. We reframe the 3D appearance generation task as a geometry-conditioned video diffusion problem: given a 3D mesh, we first render and encode multi-modal geometric features to constrain the video generation process with pixel-level precision, thereby enabling the creation of high-quality and consistent TTVs. Building upon this, we also design a method for downstream reconstruction tasks from the TTV input, featuring a multi-stage pipeline with 3D-Aware Inpainting. By rotating the model and performing a context-aware secondary generation, this pipeline effectively completes self-occluded regions to achieve full surface coverage. The videos generated by TAPESTRY are not only high-quality dynamic previews but also serve as a reliable, 3D-aware intermediate representation that can be seamlessly back-projected into UV textures or used to supervise neural rendering methods like 3DGS. This enables the automated creation of production-ready, complete 3D assets from untextured meshes. Experimental results demonstrate that our method outperforms existing approaches in both video consistency and final reconstruction quality."
  },
  {
    "id": "17625",
    "status": 200,
    "title": "Title: S-VGGT: Structure-Aware Subscene Decomposition for Scalable 3D Foundation Models",
    "comments": "7 pages, 5 figures. Accepted by ICME 2026",
    "abstract": "Abstract: Feed-forward 3D foundation models face a key challenge: the quadratic computational cost introduced by global attention, which severely limits scalability as input length increases. Concurrent acceleration methods, such as token merging, operate at the token level. While they offer local savings, the required nearest-neighbor searches introduce undesirable overhead. Consequently, these techniques fail to tackle the fundamental issue of structural redundancy dominant in dense capture data. In this work, we introduce \\textbf{S-VGGT}, a novel approach that addresses redundancy at the structural frame level, drastically shifting the optimization focus. We first leverage the initial features to build a dense scene graph, which characterizes structural scene redundancy and guides the subsequent scene partitioning. Using this graph, we softly assign frames to a small number of subscenes, guaranteeing balanced groups and smooth geometric transitions. The core innovation lies in designing the subscenes to share a common reference frame, establishing a parallel geometric bridge that enables independent and highly efficient processing without explicit geometric alignment. This structural reorganization provides strong intrinsic acceleration by cutting the global attention cost at its source. Crucially, S-VGGT is entirely orthogonal to token-level acceleration methods, allowing the two to be seamlessly combined for compounded speedups without compromising reconstruction fidelity. Code is available at this https URL ."
  },
  {
    "id": "17891",
    "status": 200,
    "title": "Title: RAMP: Reinforcement Adaptive Mixed Precision Quantization for Efficient On Device LLM Inference",
    "comments": "",
    "abstract": "Abstract: Post training quantization is essential for deploying large language models (LLMs) on resource constrained hardware, yet state of the art methods enforce uniform bit widths across layers, yielding suboptimal accuracy efficiency trade offs. We present RAMP (Reinforcement Adaptive Mixed Precision), an off policy Soft Actor Critic framework that learns per layer bit width assignments to minimize perplexity under a global bit budget. The policy conditions on an 11 dimensional embedding of activation statistics, weight properties, and structural descriptors, enabling zero shot transfer across model families and scales. To enable stable sub 4 bit quantization, we introduce Scale Folding, a preconditioning technique that migrates activation outliers into weights via per channel scaling and normalization layer compensation. A quality prioritized reward with asymmetric penalties and budget cliffs drives rapid convergence. On Llama 2 7B, RAMP achieves 5.54 perplexity at 3.68GB (3.65 effective bits), outperforming uniform 4 bit AWQ (5.60 at 3.90 GB) and GPTQ by 6% in size and 1% to3% in quality. Critically, a policy trained only on Llama 2 7B generalizes zero shot to Llama 2 13B and Mistral 7B, often surpassing target specific training, supporting the hypothesis that quantization sensitivity is primarily architectural. The HALO pipeline exports allocations to GGUF format for kernel free inference on CPUs, GPUs, and edge devices, retaining 99.5% of FP16 commonsense reasoning performance."
  },
  {
    "id": "17417",
    "status": 200,
    "title": "Title: Is Your LLM-as-a-Recommender Agent Trustable? LLMs&#39; Recommendation is Easily Hacked by Biases (Preferences)",
    "comments": "",
    "abstract": "Abstract: Current Large Language Models (LLMs) are gradually exploited in practically valuable agentic workflows such as Deep Research, E-commerce recommendation, and job recruitment. In these applications, LLMs need to select some optimal solutions from massive candidates, which we term as \\textit{LLM-as-a-Recommender} paradigm. However, the reliability of using LLM agents for recommendations is underexplored. In this work, we introduce a \\textbf{Bias} \\textbf{Rec}ommendation \\textbf{Bench}mark (\\textbf{BiasRecBench}) to highlight the critical vulnerability of such agents to biases in high-value real-world tasks. The benchmark includes three practical domains: paper review, e-commerce, and job recruitment. We construct a \\textsc{Bias Synthesis Pipeline with Calibrated Quality Margins} that 1) synthesizes evaluation data by controlling the quality gap between optimal and sub-optimal options to provide a calibrated testbed to elicit the vulnerability to biases; 2) injects contextual biases that are logical and suitable for option contexts. Extensive experiments on both SOTA (Gemini-{2.5,3}-pro, GPT-4o, DeepSeek-R1) and small-scale LLMs reveal that agents frequently succumb to injected biases despite having sufficient reasoning capabilities to identify the ground truth. These findings expose a significant reliability bottleneck in current agentic workflows, calling for specialized alignment strategies for LLM-as-a-Recommender. The complete code and evaluation datasets will be made publicly available shortly."
  },
  {
    "id": "17651",
    "status": 200,
    "title": "Title: Anchoring and Rescaling Attention for Semantically Coherent Inbetweening",
    "comments": "Accepted to CVPR 2026; Code is released at this https URL",
    "abstract": "Abstract: Generative inbetweening (GI) seeks to synthesize realistic intermediate frames between the first and last keyframes beyond mere interpolation. As sequences become sparser and motions larger, previous GI models struggle with inconsistent frames with unstable pacing and semantic misalignment. Since GI involves fixed endpoints and numerous plausible paths, this task requires additional guidance gained from the keyframes and text to specify the intended path. Thus, we give semantic and temporal guidance from the keyframes and text onto each intermediate frame through Keyframe-anchored Attention Bias. We also better enforce frame consistency with Rescaled Temporal RoPE, which allows self-attention to attend to keyframes more faithfully. TGI-Bench, the first benchmark specifically designed for text-conditioned GI evaluation, enables challenge-targeted evaluation to analyze GI models. Without additional training, our method achieves state-of-the-art frame consistency, semantic fidelity, and pace stability for both short and long sequences across diverse challenges."
  },
  {
    "id": "17333",
    "status": 200,
    "title": "Title: Grid Spatial Understanding: A Dataset for Textual Spatial Reasoning over Grids, Embodied Settings, and Coordinate Structures",
    "comments": "preprint",
    "abstract": "Abstract: We introduce GSU, a text-only grid dataset to evaluate the spatial reasoning capabilities of LLMs over 3 core tasks: navigation, object localization, and structure composition. By forgoing visual inputs, isolating spatial reasoning from perception, we show that while most models grasp basic grid concepts, they struggle with frames of reference relative to an embodied agent and identifying 3D shapes from coordinate lists. We also find that exposure to a visual modality does not provide a generalizable understanding of 3D space that VLMs are able to utilize for these tasks. Finally, we show that while the very latest frontier models can solve the provided tasks (though harder variants may still stump them), fully fine-tuning a small LM or LORA fine-tuning a small LLM show potential to match frontier model performance, suggesting an avenue for specialized embodied agents."
  },
  {
    "id": "17351",
    "status": 200,
    "title": "Title: OmniVLN: Omnidirectional 3D Perception and Token-Efficient LLM Reasoning for Visual-Language Navigation across Air and Ground Platforms",
    "comments": "",
    "abstract": "Abstract: Language-guided embodied navigation requires an agent to interpret object-referential instructions, search across multiple rooms, localize the referenced target, and execute reliable motion toward it. Existing systems remain limited in real indoor environments because narrow field-of-view sensing exposes only a partial local scene at each step, often forcing repeated rotations, delaying target discovery, and producing fragmented spatial understanding; meanwhile, directly prompting LLMs with dense 3D maps or exhaustive object lists quickly exceeds the context budget. We present OmniVLN, a zero-shot visual-language navigation framework that couples omnidirectional 3D perception with token-efficient hierarchical reasoning for both aerial and ground robots. OmniVLN fuses a rotating LiDAR and panoramic vision into a hardware-agnostic mapping stack, incrementally constructs a five-layer Dynamic Scene Graph (DSG) from mesh geometry to room- and building-level structure, and stabilizes high-level topology through persistent-homology-based room partitioning and hybrid geometric/VLM relation verification. For navigation, the global DSG is transformed into an agent-centric 3D octant representation with multi-resolution spatial attention prompting, enabling the LLM to progressively filter candidate rooms, infer egocentric orientation, localize target objects, and emit executable navigation primitives while preserving fine local detail and compact long-range memory. Experiments show that the proposed hierarchical interface improves spatial referring accuracy from 77.27\\% to 93.18\\%, reduces cumulative prompt tokens by up to 61.7\\% in cluttered multi-room settings, and improves navigation success by up to 11.68\\% over a flat-list baseline. We will release the code and an omnidirectional multimodal dataset to support reproducible research."
  },
  {
    "id": "17450",
    "status": 200,
    "title": "Title: VLM2Rec: Resolving Modality Collapse in Vision-Language Model Embedders for Multimodal Sequential Recommendation",
    "comments": "",
    "abstract": "Abstract: Sequential Recommendation (SR) in multimodal settings typically relies on small frozen pretrained encoders, which limits semantic capacity and prevents Collaborative Filtering (CF) signals from being fully integrated into item representations. Inspired by the recent success of Large Language Models (LLMs) as high-capacity embedders, we investigate the use of Vision-Language Models (VLMs) as CF-aware multimodal embedders for SR. However, we find that standard contrastive Supervised Fine-Tuning (SFT), used to adapt VLMs for embedding generation and inject CF signals, can amplify inherent modality imbalance: optimization becomes dominated by one modality while the other degrades, ultimately undermining recommendation accuracy. To address this, we propose VLM2Rec, a VLM embedder-based framework for multimodal sequential recommendation designed to promote balanced modality utilization. Specifically, we introduce Weak-modality Penalized Contrastive Learning to mitigate gradient imbalance during optimization and cross-modal Relational Topology Regularization to preserve geometric consistency between modalities. Experiments show that VLM2Rec consistently improves over strong baselines in both accuracy and robustness across diverse scenarios."
  },
  {
    "id": "17685",
    "status": 200,
    "title": "Title: Flow Matching Policy Optimization with Mirror Descent and Entropy Constraints",
    "comments": "",
    "abstract": "Abstract: Balancing policy expressiveness with the exploration-exploitation trade-off is a core challenge in online Reinforcement Learning (RL). While Stochastic Differential Equation (SDE)-based diffusion policies can represent complex, multimodal action distributions, they suffer from two critical limitations: their stochastic reverse processes render entropy intractable (necessitating heuristic exploration), and computing policy gradients through long denoising chains is expensive and unstable. In this work, we show that ODE-based flow matching inherently resolves these issues by enabling both simulation-free policy optimization and tractable entropy computation. Building on this, we introduce Flow Matching Policy Optimization with Mirror Descent and Entropy Constraints (FMER). Our framework exploits this insight in three ways. First, we theoretically establish that minimizing an advantage-weighted conditional flow matching loss acts as a simulation-free surrogate for policy mirror descent. This steers the velocity field toward high-value regions while entirely avoiding backpropagation through the ODE solver. Second, we derive an analytic entropy objective that corrects for the density distortion caused by the $\\tanh$ transformation (mapping an unbounded latent space to bounded actions), thereby facilitating principled maximum-entropy optimization. Finally, we dynamically tune the mirror descent temperature based on the effective sample size to enforce a robust trust region during training. Empirical evaluations demonstrate that FMER achieves superior performance on the challenging sparse-reward FrankaKitchen environment, while maintaining competitive results across standard dense-reward MuJoCo benchmarks."
  },
  {
    "id": "17311",
    "status": 200,
    "title": "Title: Ruyi2.5 Technical Report",
    "comments": "",
    "abstract": "Abstract: We present Ruyi2.5, a multimodal familial model built on the AI Flow framework. Extending Ruyi2&#39;s &#34;Train Once, Deploy Many&#34; paradigm to the multimodal domain, Ruyi2.5 constructs a shared-backbone architecture that co-trains models of varying scales within a single unified pipeline, ensuring semantic consistency across all deployment tiers. Built upon Ruyi2.5, Ruyi2.5-Camera model is developed as a privacy-preserving camera service system, which instantiates Ruyi2.5-Camera into a two-stage recognition pipeline: an edge model applies information-bottleneck-guided irreversible feature mapping to de-identify raw frames at the source, while a cloud model performs deep behavior reasoning. To accelerate reinforcement learning fine-tuning, we further propose Binary Prefix Policy Optimization (BPPO), which reduces sample redundancy via binary response selection and focuses gradient updates on response prefixes, achieving a 2 to 3 times training speedup over GRPO. Experiments show Ruyi2.5 matches Qwen3-VL on the general multimodal benchmarks, while Ruyi2.5-Camera substantially outperforms Qwen3-VL on privacy-constrained surveillance tasks."
  },
  {
    "id": "17326",
    "status": 200,
    "title": "Title: FineViT: Progressively Unlocking Fine-Grained Perception with Dense Recaptions",
    "comments": "",
    "abstract": "Abstract: While Multimodal Large Language Models (MLLMs) have experienced rapid advancements, their visual encoders frequently remain a performance bottleneck. Conventional CLIP-based encoders struggle with dense spatial tasks due to the loss of visual details caused by low-resolution pretraining and the reliance on noisy, coarse web-crawled image-text pairs. To overcome these limitations, we introduce FineViT, a novel vision encoder specifically designed to unlock fine-grained perception. By replacing coarse web data with dense recaptions, we systematically mitigate information loss through a progressive training paradigm.: first, the encoder is trained from scratch at a high native resolution on billions of global recaptioned image-text pairs, establishing a robust, detail rich semantic foundation. Subsequently, we further enhance its local perception through LLM alignment, utilizing our curated FineCap-450M dataset that comprises over $450$ million high quality local captions. Extensive experiments validate the effectiveness of the progressive strategy. FineViT achieves state-of-the-art zero-shot recognition and retrieval performance, especially in long-context retrieval, and consistently outperforms multimodal visual encoders such as SigLIP2 and Qwen-ViT when integrated into MLLMs. We hope FineViT could serve as a powerful new baseline for fine-grained visual perception."
  },
  {
    "id": "17360",
    "status": 200,
    "title": "Title: MCoT-MVS: Multi-level Vision Selection by Multi-modal Chain-of-Thought Reasoning for Composed Image Retrieval",
    "comments": "Accepted by The Web Conference 2026 (WWW2026)",
    "abstract": "Abstract: Composed Image Retrieval (CIR) aims to retrieve target images based on a reference image and modified texts. However, existing methods often struggle to extract the correct semantic cues from the reference image that best reflect the user&#39;s intent under textual modification prompts, resulting in interference from irrelevant visual noise. In this paper, we propose a novel Multi-level Vision Selection by Multi-modal Chain-of-Thought Reasoning (MCoT-MVS) for CIR, integrating attention-aware multi-level vision features guided by reasoning cues from a multi-modal large language model (MLLM). Specifically, we leverage an MLLM to perform chain-of-thought reasoning on the multimodal composed input, generating the retained, removed, and target-inferred texts. These textual cues subsequently guide two reference visual attention selection modules to selectively extract discriminative patch-level and instance-level semantics from the reference image. Finally, to effectively fuse these multi-granular visual cues with the modified text and the imagined target description, we design a weighted hierarchical combination module to align the composed query with target images in a unified embedding space. Extensive experiments on two CIR benchmarks, namely CIRR and FashionIQ, demonstrate that our approach consistently outperforms existing methods and achieves new state-of-the-art performance. Code and trained models are publicly released."
  },
  {
    "id": "17437",
    "status": 200,
    "title": "Title: FloorPlan-VLN: A New Paradigm for Floor Plan Guided Vision-Language Navigation",
    "comments": "",
    "abstract": "Abstract: Existing Vision-Language Navigation (VLN) task requires agents to follow verbose instructions, ignoring some potentially useful global spatial priors, limiting their capability to reason about spatial structures. Although human-readable spatial schematics (e.g., floor plans) are ubiquitous in real-world buildings, current agents lack the cognitive ability to comprehend and utilize them. To bridge this gap, we introduce \\textbf{FloorPlan-VLN}, a new paradigm that leverages structured semantic floor plans as global spatial priors to enable navigation with only concise instructions. We first construct the FloorPlan-VLN dataset, which comprises over 10k episodes across 72 scenes. It pairs more than 100 semantically annotated floor plans with Matterport3D-based navigation trajectories and concise instructions that omit step-by-step guidance. Then, we propose a simple yet effective method \\textbf{FP-Nav} that uses a dual-view, spatio-temporally aligned video sequence, and auxiliary reasoning tasks to align observations, floor plans, and instructions. When evaluated under this new benchmark, our method significantly outperforms adapted state-of-the-art VLN baselines, achieving more than a 60\\% relative improvement in navigation success rate. Furthermore, comprehensive noise modeling and real-world deployments demonstrate the feasibility and robustness of FP-Nav to actuation drift and floor plan distortions. These results validate the effectiveness of floor plan guided navigation and highlight FloorPlan-VLN as a promising step toward more spatially intelligent navigation."
  }
]
```

另20项不随22自动准入；具体明确EX/范围外与决定准入消歧分开处理。已有摘要原字段不等Source完成，也不因已抓宽标题承诺逐项全文。


## 作者原有限尾42条完整题摘原字段

下面为原既有title池指定相关/含糊项逐条exact-v1官方abs实际HTTP200完整AB与current字段读取（只元数据，不是HTML方法全审）。原接口返回的Comments/history如实保留，Submitted不授公开日期；数字未经Source，不授正确性或性能。机械恢复截断的17474/17450/17419/17952仅重抓这四exactv1，未扩query。如此保留初筛依据，不把本42行自动列成候选或全文队列；具体判断随后在此记录，日期对拟入选项必要核。

```json
[
  {
    "id": "17301",
    "status": 200,
    "title": "Title: WINFlowNets: Warm-up Integrated Networks Training of Generative Flow Networks for Robotics and Machine Fault Adaptation",
    "abstract": "Abstract: Generative Flow Networks for continuous scenarios (CFlowNets) have shown promise in solving sequential decision-making tasks by learning stochastic policies using a flow and a retrieval network. Despite their demonstrated efficiency compared to state-of-the-art Reinforcement Learning (RL) algorithms, their practical application in robotic control tasks is constrained by the reliance on pre-training the retrieval network. This dependency poses challenges in dynamic robotic environments, where pre-training data may not be readily available or representative of the current environment. This paper introduces WINFlowNets, a novel CFlowNets framework that enables the co-training of flow and retrieval networks. WINFlowNets begins with a warm-up phase for the retrieval network to bootstrap its policy, followed by a shared training architecture and a shared replay buffer for co-training both networks. Experiments in simulated robotic environments demonstrate that WINFlowNets surpasses CFlowNets and state-of-the-art RL algorithms in terms of average reward and training stability. Furthermore, WINFlowNets exhibits strong adaptive capability in fault environments, making it suitable for tasks that demand quick adaptation with limited sample data. These findings highlight WINFlowNets&#39; potential for deployment in dynamic and malfunction-prone robotic systems, where traditional pre-training or sample inefficient data collection may be impractical.",
    "history": "Submission history From: Shadan Golestan [ view email ] [v1] Wed, 18 Mar 2026 02:55:02 UTC (1,043 KB)"
  },
  {
    "id": "17311",
    "status": 200,
    "title": "Title: Ruyi2.5 Technical Report",
    "abstract": "Abstract: We present Ruyi2.5, a multimodal familial model built on the AI Flow framework. Extending Ruyi2&#39;s &#34;Train Once, Deploy Many&#34; paradigm to the multimodal domain, Ruyi2.5 constructs a shared-backbone architecture that co-trains models of varying scales within a single unified pipeline, ensuring semantic consistency across all deployment tiers. Built upon Ruyi2.5, Ruyi2.5-Camera model is developed as a privacy-preserving camera service system, which instantiates Ruyi2.5-Camera into a two-stage recognition pipeline: an edge model applies information-bottleneck-guided irreversible feature mapping to de-identify raw frames at the source, while a cloud model performs deep behavior reasoning. To accelerate reinforcement learning fine-tuning, we further propose Binary Prefix Policy Optimization (BPPO), which reduces sample redundancy via binary response selection and focuses gradient updates on response prefixes, achieving a 2 to 3 times training speedup over GRPO. Experiments show Ruyi2.5 matches Qwen3-VL on the general multimodal benchmarks, while Ruyi2.5-Camera substantially outperforms Qwen3-VL on privacy-constrained surveillance tasks.",
    "history": "Submission history From: Jiawei Shao [ view email ] [v1] Wed, 18 Mar 2026 03:13:06 UTC (379 KB)"
  },
  {
    "id": "17326",
    "status": 200,
    "title": "Title: FineViT: Progressively Unlocking Fine-Grained Perception with Dense Recaptions",
    "abstract": "Abstract: While Multimodal Large Language Models (MLLMs) have experienced rapid advancements, their visual encoders frequently remain a performance bottleneck. Conventional CLIP-based encoders struggle with dense spatial tasks due to the loss of visual details caused by low-resolution pretraining and the reliance on noisy, coarse web-crawled image-text pairs. To overcome these limitations, we introduce FineViT, a novel vision encoder specifically designed to unlock fine-grained perception. By replacing coarse web data with dense recaptions, we systematically mitigate information loss through a progressive training paradigm.: first, the encoder is trained from scratch at a high native resolution on billions of global recaptioned image-text pairs, establishing a robust, detail rich semantic foundation. Subsequently, we further enhance its local perception through LLM alignment, utilizing our curated FineCap-450M dataset that comprises over $450$ million high quality local captions. Extensive experiments validate the effectiveness of the progressive strategy. FineViT achieves state-of-the-art zero-shot recognition and retrieval performance, especially in long-context retrieval, and consistently outperforms multimodal visual encoders such as SigLIP2 and Qwen-ViT when integrated into MLLMs. We hope FineViT could serve as a powerful new baseline for fine-grained visual perception.",
    "history": "Submission history From: Peisen Zhao [ view email ] [v1] Wed, 18 Mar 2026 03:39:04 UTC (20,140 KB)"
  },
  {
    "id": "17328",
    "status": 200,
    "title": "Title: A Progressive Visual-Logic-Aligned Framework for Ride-Hailing Adjudication",
    "abstract": "Abstract: The efficient adjudication of responsibility disputes is pivotal for maintaining marketplace fairness. However, the exponential surge in ride-hailing volume renders manual review intractable, while conventional automated methods lack the reasoning transparency required for quasi-judicial decisions. Although Multimodal LLMs offer a promising paradigm, they fundamentally struggle to bridge the gap between general visual semantics and rigorous evidentiary protocols, often leading to perceptual hallucinations and logical looseness. To address these systemic misalignments, we introduce RideJudge, a Progressive Visual-Logic-Aligned Framework. Instead of relying on generic pre-training, we bridge the semantic gap via SynTraj, a synthesis engine that grounds abstract liability concepts into concrete trajectory patterns. To resolve the conflict between massive regulation volume and limited context windows, we propose an Adaptive Context Optimization strategy that distills expert knowledge, coupled with a Chain-of-Adjudication mechanism to enforce active evidentiary inquiry. Furthermore, addressing the inadequacy of sparse binary feedback for complex liability assessment, we implement a novel Ordinal-Sensitive Reinforcement Learning mechanism that calibrates decision boundaries against hierarchical severity. Extensive experiments show that our RideJudge-8B achieves 88.41\\% accuracy, surpassing 32B-scale baselines and establishing a new standard for interpretable adjudication.",
    "history": "Submission history From: Weiming Wu [ view email ] [v1] Wed, 18 Mar 2026 03:46:30 UTC (743 KB)"
  },
  {
    "id": "17333",
    "status": 200,
    "title": "Title: Grid Spatial Understanding: A Dataset for Textual Spatial Reasoning over Grids, Embodied Settings, and Coordinate Structures",
    "abstract": "Abstract: We introduce GSU, a text-only grid dataset to evaluate the spatial reasoning capabilities of LLMs over 3 core tasks: navigation, object localization, and structure composition. By forgoing visual inputs, isolating spatial reasoning from perception, we show that while most models grasp basic grid concepts, they struggle with frames of reference relative to an embodied agent and identifying 3D shapes from coordinate lists. We also find that exposure to a visual modality does not provide a generalizable understanding of 3D space that VLMs are able to utilize for these tasks. Finally, we show that while the very latest frontier models can solve the provided tasks (though harder variants may still stump them), fully fine-tuning a small LM or LORA fine-tuning a small LLM show potential to match frontier model performance, suggesting an avenue for specialized embodied agents.",
    "comments": "preprint",
    "history": "Submission history From: Risham Sidhu [ view email ] [v1] Wed, 18 Mar 2026 03:57:30 UTC (235 KB)"
  },
  {
    "id": "17351",
    "status": 200,
    "title": "Title: OmniVLN: Omnidirectional 3D Perception and Token-Efficient LLM Reasoning for Visual-Language Navigation across Air and Ground Platforms",
    "abstract": "Abstract: Language-guided embodied navigation requires an agent to interpret object-referential instructions, search across multiple rooms, localize the referenced target, and execute reliable motion toward it. Existing systems remain limited in real indoor environments because narrow field-of-view sensing exposes only a partial local scene at each step, often forcing repeated rotations, delaying target discovery, and producing fragmented spatial understanding; meanwhile, directly prompting LLMs with dense 3D maps or exhaustive object lists quickly exceeds the context budget. We present OmniVLN, a zero-shot visual-language navigation framework that couples omnidirectional 3D perception with token-efficient hierarchical reasoning for both aerial and ground robots. OmniVLN fuses a rotating LiDAR and panoramic vision into a hardware-agnostic mapping stack, incrementally constructs a five-layer Dynamic Scene Graph (DSG) from mesh geometry to room- and building-level structure, and stabilizes high-level topology through persistent-homology-based room partitioning and hybrid geometric/VLM relation verification. For navigation, the global DSG is transformed into an agent-centric 3D octant representation with multi-resolution spatial attention prompting, enabling the LLM to progressively filter candidate rooms, infer egocentric orientation, localize target objects, and emit executable navigation primitives while preserving fine local detail and compact long-range memory. Experiments show that the proposed hierarchical interface improves spatial referring accuracy from 77.27\\% to 93.18\\%, reduces cumulative prompt tokens by up to 61.7\\% in cluttered multi-room settings, and improves navigation success by up to 11.68\\% over a flat-list baseline. We will release the code and an omnidirectional multimodal dataset to support reproducible research.",
    "history": "Submission history From: Jianping Li [ view email ] [v1] Wed, 18 Mar 2026 04:26:30 UTC (9,092 KB)"
  },
  {
    "id": "17360",
    "status": 200,
    "title": "Title: MCoT-MVS: Multi-level Vision Selection by Multi-modal Chain-of-Thought Reasoning for Composed Image Retrieval",
    "abstract": "Abstract: Composed Image Retrieval (CIR) aims to retrieve target images based on a reference image and modified texts. However, existing methods often struggle to extract the correct semantic cues from the reference image that best reflect the user&#39;s intent under textual modification prompts, resulting in interference from irrelevant visual noise. In this paper, we propose a novel Multi-level Vision Selection by Multi-modal Chain-of-Thought Reasoning (MCoT-MVS) for CIR, integrating attention-aware multi-level vision features guided by reasoning cues from a multi-modal large language model (MLLM). Specifically, we leverage an MLLM to perform chain-of-thought reasoning on the multimodal composed input, generating the retained, removed, and target-inferred texts. These textual cues subsequently guide two reference visual attention selection modules to selectively extract discriminative patch-level and instance-level semantics from the reference image. Finally, to effectively fuse these multi-granular visual cues with the modified text and the imagined target description, we design a weighted hierarchical combination module to align the composed query with target images in a unified embedding space. Extensive experiments on two CIR benchmarks, namely CIRR and FashionIQ, demonstrate that our approach consistently outperforms existing methods and achieves new state-of-the-art performance. Code and trained models are publicly released.",
    "comments": "Accepted by The Web Conference 2026 (WWW2026)",
    "history": "Submission history From: Xuri Ge [ view email ] [v1] Wed, 18 Mar 2026 04:49:19 UTC (10,498 KB)"
  },
  {
    "id": "17386",
    "status": 200,
    "title": "Title: PJB: A Reasoning-Aware Benchmark for Person-Job Retrieval",
    "abstract": "Abstract: As retrieval models converge on generic benchmarks, the pressing question is no longer &#34;who scores higher&#34; but rather &#34;where do systems fail, and why?&#34; Person-job matching is a domain that urgently demands such diagnostic capability -- it requires systems not only to verify explicit constraints but also to perform skill-transfer inference and job-competency reasoning, yet existing benchmarks provide no systematic diagnostic support for this task. We introduce PJB (Person-Job Benchmark), a reasoning-aware retrieval evaluation dataset that uses complete job descriptions as queries and complete resumes as documents, defines relevance through job-competency judgment, is grounded in real-world recruitment data spanning six industry domains and nearly 200,000 resumes, and upgrades evaluation from &#34;who scores higher&#34; to &#34;where do systems differ, and why&#34; through domain-family and reasoning-type diagnostic labels. Diagnostic experiments using dense retrieval reveal that performance heterogeneity across industry domains far exceeds the gains from module upgrades for the same model, indicating that aggregate scores alone can severely mislead optimization decisions. At the module level, reranking yields stable improvements while query understanding not only fails to help but actually degrades overall performance when combined with reranking -- the two modules face fundamentally different improvement bottlenecks. The value of PJB lies not in yet another leaderboard of average scores, but in providing recruitment retrieval systems with a capability map that pinpoints where to invest.",
    "history": "Submission history From: Guangzhi Wang [ view email ] [v1] Wed, 18 Mar 2026 06:08:06 UTC (28 KB)"
  },
  {
    "id": "17417",
    "status": 200,
    "title": "Title: Is Your LLM-as-a-Recommender Agent Trustable? LLMs&#39; Recommendation is Easily Hacked by Biases (Preferences)",
    "abstract": "Abstract: Current Large Language Models (LLMs) are gradually exploited in practically valuable agentic workflows such as Deep Research, E-commerce recommendation, and job recruitment. In these applications, LLMs need to select some optimal solutions from massive candidates, which we term as \\textit{LLM-as-a-Recommender} paradigm. However, the reliability of using LLM agents for recommendations is underexplored. In this work, we introduce a \\textbf{Bias} \\textbf{Rec}ommendation \\textbf{Bench}mark (\\textbf{BiasRecBench}) to highlight the critical vulnerability of such agents to biases in high-value real-world tasks. The benchmark includes three practical domains: paper review, e-commerce, and job recruitment. We construct a \\textsc{Bias Synthesis Pipeline with Calibrated Quality Margins} that 1) synthesizes evaluation data by controlling the quality gap between optimal and sub-optimal options to provide a calibrated testbed to elicit the vulnerability to biases; 2) injects contextual biases that are logical and suitable for option contexts. Extensive experiments on both SOTA (Gemini-{2.5,3}-pro, GPT-4o, DeepSeek-R1) and small-scale LLMs reveal that agents frequently succumb to injected biases despite having sufficient reasoning capabilities to identify the ground truth. These findings expose a significant reliability bottleneck in current agentic workflows, calling for specialized alignment strategies for LLM-as-a-Recommender. The complete code and evaluation datasets will be made publicly available shortly.",
    "history": "Submission history From: Zichen Tang [ view email ] [v1] Wed, 18 Mar 2026 06:50:48 UTC (1,181 KB) [v2] Fri, 20 Mar 2026 13:11:53 UTC (1,181 KB)"
  },
  {
    "id": "17419",
    "status": 200,
    "title": "Title: Caging the Agents: A Zero Trust Security Architecture for Autonomous AI in Healthcare",
    "abstract": "Abstract: Autonomous AI agents powered by large language models are being deployed in production with capabilities including shell execution, file system access, database queries, and multi-party communication. Recent red teaming research demonstrates that these agents exhibit critical vulnerabilities in realistic settings: unauthorized compliance with non-owner instructions, sensitive information disclosure, identity spoofing, cross-agent propagation of unsafe practices, and indirect prompt injection through external resources [7]. In healthcare environments processing Protected Health Information, every such vulnerability becomes a potential HIPAA violation. This paper presents a security architecture deployed for nine autonomous AI agents in production at a healthcare technology company. We develop a six-domain threat model for agentic AI in healthcare covering credential exposure, execution capability abuse, network egress exfiltration, prompt integrity failures, database access risks, and fleet configuration drift. We implement four-layer defense in depth: (1) kernel level workload isolation using gVisor on Kubernetes, (2) credential proxy sidecars preventing agent containers from accessing raw secrets, (3) network egress policies restricting each agent to allowlisted destinations, and (4) a prompt integrity framework with structured metadata envelopes and untrusted content labeling. We report results from 90 days of deployment including four HIGH severity findings discovered and remediated by an automated security audit agent, progressive fleet hardening across three VM image generations, and defense coverage mapped to all eleven attack patterns from recent literature. All configurations, audit tooling, and the prompt integrity framework are released as open source.",
    "comments": "Keywords: agentic AI security, autonomous agents, healthcare cybersecurity, zero trust, prompt injection, HIPAA, Kubernetes security, OpenClaw",
    "history": "Submission history From: Sri Saikat Maiti [ view email ] [v1] Wed, 18 Mar 2026 06:54:47 UTC (15 KB)"
  },
  {
    "id": "17437",
    "status": 200,
    "title": "Title: FloorPlan-VLN: A New Paradigm for Floor Plan Guided Vision-Language Navigation",
    "abstract": "Abstract: Existing Vision-Language Navigation (VLN) task requires agents to follow verbose instructions, ignoring some potentially useful global spatial priors, limiting their capability to reason about spatial structures. Although human-readable spatial schematics (e.g., floor plans) are ubiquitous in real-world buildings, current agents lack the cognitive ability to comprehend and utilize them. To bridge this gap, we introduce \\textbf{FloorPlan-VLN}, a new paradigm that leverages structured semantic floor plans as global spatial priors to enable navigation with only concise instructions. We first construct the FloorPlan-VLN dataset, which comprises over 10k episodes across 72 scenes. It pairs more than 100 semantically annotated floor plans with Matterport3D-based navigation trajectories and concise instructions that omit step-by-step guidance. Then, we propose a simple yet effective method \\textbf{FP-Nav} that uses a dual-view, spatio-temporally aligned video sequence, and auxiliary reasoning tasks to align observations, floor plans, and instructions. When evaluated under this new benchmark, our method significantly outperforms adapted state-of-the-art VLN baselines, achieving more than a 60\\% relative improvement in navigation success rate. Furthermore, comprehensive noise modeling and real-world deployments demonstrate the feasibility and robustness of FP-Nav to actuation drift and floor plan distortions. These results validate the effectiveness of floor plan guided navigation and highlight FloorPlan-VLN as a promising step toward more spatially intelligent navigation.",
    "history": "Submission history From: Kehan Chen [ view email ] [v1] Wed, 18 Mar 2026 07:22:48 UTC (11,392 KB)"
  },
  {
    "id": "17450",
    "status": 200,
    "title": "Title: VLM2Rec: Resolving Modality Collapse in Vision-Language Model Embedders for Multimodal Sequential Recommendation",
    "abstract": "Abstract: Sequential Recommendation (SR) in multimodal settings typically relies on small frozen pretrained encoders, which limits semantic capacity and prevents Collaborative Filtering (CF) signals from being fully integrated into item representations. Inspired by the recent success of Large Language Models (LLMs) as high-capacity embedders, we investigate the use of Vision-Language Models (VLMs) as CF-aware multimodal encoders for SR. However, we find that standard contrastive supervised fine-tuning (SFT), which adapts VLMs for embedding generation and injects CF signals, can amplify its inherent modality collapse. In this state, optimization is dominated by a single modality while the other degrades, ultimately undermining recommendation accuracy. To address this, we propose VLM2Rec, a VLM embedder-based framework for multimodal sequential recommendation designed to ensure balanced modality utilization. Specifically, we introduce Weak-modality Penalized Contrastive Learning to rectify gradient imbalance during optimization and Cross-Modal Relational Topology Regularization to preserve geometric consistency between modalities. Extensive experiments demonstrate that VLM2Rec consistently outperforms state-of-the-art baselines in both accuracy and robustness across diverse scenarios.",
    "history": "Submission history From: Junyoung Kim [ view email ] [v1] Wed, 18 Mar 2026 07:46:30 UTC (547 KB) [v2] Wed, 12 Aug 2026 10:19:22 UTC (1,867 KB)"
  },
  {
    "id": "17470",
    "status": 200,
    "title": "Title: VirPro: Visual-referred Probabilistic Prompt Learning for Weakly-Supervised Monocular 3D Detection",
    "abstract": "Abstract: Monocular 3D object detection typically relies on pseudo-labeling techniques to reduce dependency on real-world annotations. Recent advances demonstrate that deterministic linguistic cues can serve as effective auxiliary weak supervision signals, providing complementary semantic context. However, hand-crafted textual descriptions struggle to capture the inherent visual diversity of individuals across scenes, limiting the model&#39;s ability to learn scene-aware representations. To address this challenge, we propose Visual-referred Probabilistic Prompt Learning (VirPro), an adaptive multi-modal pretraining paradigm that can be seamlessly integrated into diverse weakly supervised monocular 3D detection frameworks. Specifically, we generate a diverse set of learnable, instance-conditioned prompts across scenes and store them in an Adaptive Prompt Bank (APB). Subsequently, we introduce Multi-Gaussian Prompt Modeling (MGPM), which incorporates scene-based visual features into the corresponding textual embeddings, allowing the text prompts to express visual uncertainties. Then, from the fused vision-language embeddings, we decode a prompt-targeted Gaussian, from which we derive a unified object-level prompt embedding for each instance. RoI-level contrastive matching is employed to enforce modality alignment, bringing embeddings of co-occurring objects within the same scene closer in the latent space, thus enhancing semantic coherence. Extensive experiments on the KITTI benchmark demonstrate that integrating our pretraining paradigm consistently yields substantial performance gains, achieving up to a 4.8% average precision improvement than the baseline.",
    "comments": "Accepted by CVPR 2026 Findings",
    "history": "Submission history From: Chupeng Liu [ view email ] [v1] Wed, 18 Mar 2026 08:23:55 UTC (24,329 KB) [v2] Fri, 20 Mar 2026 13:20:01 UTC (24,329 KB)"
  },
  {
    "id": "17474",
    "status": 200,
    "title": "Title: Revisiting Cross-Attention Mechanisms: Leveraging Beneficial Noise for Domain-Adaptive Learning",
    "abstract": "Abstract: Unsupervised Domain Adaptation (UDA) seeks to transfer knowledge from a labeled source domain to an unlabeled target domain but often suffers from severe domain and scale gaps that degrade performance. Existing cross-attention-based transformers can align features across domains, yet they struggle to preserve content semantics under large appearance and scale variations. To explicitly address these challenges, we introduce the concept of beneficial noise, which regularizes cross-attention by injecting controlled perturbations, encouraging the model to ignore style distractions and focus on content. We propose the Domain-Adaptive Cross-Scale Matching (DACSM) framework, which consists of a Domain-Adaptive Transformer (DAT) for disentangling domain-shared content from domain-specific style, and a Cross-Scale Matching (CSM) module that adaptively aligns features across multiple resolutions. DAT incorporates beneficial noise into cross-attention, enabling progressive domain translation with enhanced robustness, yielding content-consistent and style-invariant representations. Meanwhile, CSM ensures semantic consistency under scale changes. Extensive experiments on VisDA-2017, Office-Home, and DomainNet demonstrate that DACSM achieves state-of-the-art performance, with up to +2.3% improvement over CDTrans on VisDA-2017. Notably, DACSM achieves a +5.9% gain on the challenging &#34;truck&#34; class of VisDA, evidencing the strength of beneficial noise in handling scale discrepancies. These results highlight the effectiveness of combining domain translation, beneficial-noise-enhanced attention, and scale-aware alignment for robust cross-domain representation learning.",
    "history": "Submission history From: Zelin Zang [ view email ] [v1] Wed, 18 Mar 2026 08:28:14 UTC (3,011 KB)"
  },
  {
    "id": "17475",
    "status": 200,
    "title": "Title: Humans and transformer LMs: Abstraction drives language learning",
    "abstract": "Abstract: Categorization is a core component of human linguistic competence. We investigate how a transformer-based language model (LM) learns linguistic categories by comparing its behaviour over the course of training to behaviours which characterize abstract feature-based and concrete exemplar-based accounts of human language acquisition. We investigate how lexical semantic and syntactic categories emerge using novel divergence-based metrics that track learning trajectories using next-token distributions. In experiments with GPT-2 small, we find that (i) when a construction is learned, abstract class-level behaviour is evident at earlier steps than lexical item-specific behaviour, and (ii) that different linguistic behaviours emerge abruptly in sequence at different points in training, revealing that abstraction plays a key role in how LMs learn. This result informs the models of human language acquisition that LMs may serve as an existence proof for.",
    "comments": "EACL 2026",
    "history": "Submission history From: Jasper Jian [ view email ] [v1] Wed, 18 Mar 2026 08:30:20 UTC (4,310 KB)"
  },
  {
    "id": "17507",
    "status": 200,
    "title": "Title: QuantFL: Sustainable Federated Learning for Edge IoT via Pre-Trained Model Quantisation",
    "abstract": "Abstract: Federated Learning (FL) enables privacy-preserving intelligence on Internet of Things (IoT) devices but incurs a significant carbon footprint due to the high energy cost of frequent uplink transmission. While pre-trained models are increasingly available on edge devices, their potential to reduce the energy overhead of fine-tuning remains underexplored. In this work, we propose QuantFL, a sustainable FL framework that leverages pre-trained initialisation to enable aggressive, computationally lightweight quantisation. We demonstrate that pre-training naturally concentrates update statistics, allowing us to use memory-efficient bucket quantisation without the energy-intensive overhead of complex error-feedback mechanisms. On MNIST and CIFAR-100, QuantFL reduces total communication by 40\\% ($\\simeq40\\%$ total-bit reduction with full-precision downlink; $\\geq80\\%$ on uplink or when downlink is quantised) while matching or exceeding uncompressed baselines under strict bandwidth budgets; BU attains 89.00\\% (MNIST) and 66.89\\% (CIFAR-100) test accuracy with orders of magnitude fewer bits. We also account for uplink and downlink costs and provide ablations on quantisation levels and initialisation. QuantFL delivers a practical, &#34;green&#34; recipe for scalable training on battery-constrained IoT networks.",
    "history": "Submission history From: Charuka Herath [ view email ] [v1] Wed, 18 Mar 2026 09:08:28 UTC (591 KB)"
  },
  {
    "id": "17510",
    "status": 200,
    "title": "Title: Interpreting Context-Aware Human Preferences for Multi-Objective Robot Navigation",
    "abstract": "Abstract: Robots operating in human-shared environments must not only achieve task-level navigation objectives such as safety and efficiency, but also adapt their behavior to human preferences. However, as human preferences are typically expressed in natural language and depend on environmental context, it is difficult to directly integrate them into low-level robot control policies. In this work, we present a pipeline that enables robots to understand and apply context-dependent navigation preferences by combining foundational models with a Multi-Objective Reinforcement Learning (MORL) navigation policy. Thus, our approach integrates high-level semantic reasoning with low-level motion control. A Vision-Language Model (VLM) extracts structured environmental context from onboard visual observations, while Large Language Models (LLM) convert natural language user feedback into interpretable, context-dependent behavioral rules stored in a persistent but updatable rule memory. A preference translation module then maps contextual information and stored rules into numerical preference vectors that parameterize a pretrained MORL policy for real-time navigation adaptation. We evaluate the proposed framework through quantitative component-level evaluations, a user study, and real-world robot deployments in various indoor environments. Our results demonstrate that the system reliably captures user intent, generates consistent preference vectors, and enables controllable behavior adaptation across diverse contexts. Overall, the proposed pipeline improves the adaptability, transparency, and usability of robots operating in shared human environments, while maintaining safe and responsive real-time control.",
    "history": "Submission history From: Subham Agrawal [ view email ] [v1] Wed, 18 Mar 2026 09:14:05 UTC (6,379 KB) [v2] Tue, 12 May 2026 12:59:22 UTC (6,377 KB)"
  },
  {
    "id": "17520",
    "status": 200,
    "title": "Title: PCA-Seg: Revisiting Cost Aggregation for Open-Vocabulary Semantic and Part Segmentation",
    "abstract": "Abstract: Recent advances in vision-language models (VLMs) have garnered substantial attention in open-vocabulary semantic and part segmentation (OSPS). However, existing methods extract image-text alignment cues from cost volumes through a serial structure of spatial and class aggregations, leading to knowledge interference between class-level semantics and spatial context. Therefore, this paper proposes a simple yet effective parallel cost aggregation (PCA-Seg) paradigm to alleviate the above challenge, enabling the model to capture richer vision-language alignment information from cost volumes. Specifically, we design an expert-driven perceptual learning (EPL) module that efficiently integrates semantic and contextual streams. It incorporates a multi-expert parser to extract complementary features from multiple perspectives. In addition, a coefficient mapper is designed to adaptively learn pixel-specific weights for each feature, enabling the integration of complementary knowledge into a unified and robust feature embedding. Furthermore, we propose a feature orthogonalization decoupling (FOD) strategy to mitigate redundancy between the semantic and contextual streams, which allows the EPL module to learn diverse knowledge from orthogonalized features. Extensive experiments on eight benchmarks show that each parallel block in PCA-Seg adds merely 0.35M parameters while achieving state-of-the-art OSPS performance.",
    "comments": "Accepted by CVPR2026",
    "history": "Submission history From: Jianjian Yin [ view email ] [v1] Wed, 18 Mar 2026 09:26:43 UTC (4,951 KB)"
  },
  {
    "id": "17527",
    "status": 200,
    "title": "Title: Mirror Descent on Riemannian Manifolds",
    "abstract": "Abstract: Mirror Descent (MD) is a scalable first-order method widely used in large-scale optimization, with applications in image processing, policy optimization, and neural network training. This paper generalizes MD to optimization on Riemannian manifolds. In particular, we develop a Riemannian Mirror Descent (RMD) framework via reparameterization and further propose a stochastic variant of RMD. We also establish non-asymptotic convergence guarantees for both RMD and stochastic RMD. As an application to the Stiefel manifold, our RMD framework reduces to the Curvilinear Gradient Descent (CGD) method proposed in [26]. Moreover, when specializing the stochastic RMD framework to the Stiefel setting, we obtain a stochastic extension of CGD, which effectively addresses large-scale manifold optimization problems.",
    "history": "Submission history From: Jiaxin Jiang [ view email ] [v1] Wed, 18 Mar 2026 09:31:39 UTC (24 KB) [v2] Thu, 11 Jun 2026 06:25:43 UTC (24 KB)"
  },
  {
    "id": "17570",
    "status": 200,
    "title": "Title: FoMo X: Modular Explainability Signals for Outlier Detection Foundation Models",
    "abstract": "Abstract: Tabular foundation models, specifically Prior-Data Fitted Networks (PFNs), have revolutionized outlier detection (OD) by enabling unsupervised zero-shot adaptation to new datasets without training. However, despite their predictive power, these models typically function as opaque black boxes, outputting scalar outlier scores that lack the operational context required for safety-critical decision-making. Existing post-hoc explanation methods are often computationally prohibitive for real-time deployment or fail to capture the epistemic uncertainty inherent in zero-shot inference. In this work, we introduce FoMo-X, a modular framework that equips OD foundation models with intrinsic, lightweight diagnostic capabilities. We leverage the insight that the frozen embeddings of a pretrained PFN backbone already encode rich, context-conditioned relational information. FoMo-X attaches auxiliary diagnostic heads to these embeddings, trained offline using the same generative simulator prior as the backbone. This allows us to distill computationally expensive properties, such as Monte Carlo dropout based epistemic uncertainty, into a deterministic, single-pass inference. We instantiate FoMo-X with two novel heads: a Severity Head that discretizes deviations into interpretable risk tiers, and an Uncertainty Head that provides calibrated confidence measures. Extensive evaluation on synthetic and real-world benchmarks (ADBench) demonstrates that FoMo-X recovers ground-truth diagnostic signals with high fidelity and negligible inference overhead. By bridging the gap between foundation model performance and operational explainability, FoMo-X offers a scalable path toward trustworthy, zero-shot outlier detection.",
    "comments": "24 pages, 9 figures",
    "history": "Submission history From: Simon Klüttermann [ view email ] [v1] Wed, 18 Mar 2026 10:22:51 UTC (3,081 KB)"
  },
  {
    "id": "17605",
    "status": 200,
    "title": "Title: ReLaGS: Relational Language Gaussian Splatting",
    "abstract": "Abstract: Achieving unified 3D perception and reasoning across tasks such as segmentation, retrieval, and relation understanding remains challenging, as existing methods are either object-centric or rely on costly training for inter-object reasoning. We present a novel framework that constructs a hierarchical language-distilled Gaussian scene and its 3D semantic scene graph without scene-specific training. A Gaussian pruning mechanism refines scene geometry, while a robust multi-view language alignment strategy aggregates noisy 2D features into accurate 3D object embeddings. On top of this hierarchy, we build an open-vocabulary 3D scene graph with Vision Language derived annotations and Graph Neural Network-based relational reasoning. Our approach enables efficient and scalable open-vocabulary 3D reasoning by jointly modeling hierarchical semantics and inter/intra-object relationships, validated across tasks including open-vocabulary segmentation, scene graph generation, and relation-guided retrieval. Project page: this https URL",
    "comments": "Accepted at CVPR 2026",
    "history": "Submission history From: Abdalla Arafa [ view email ] [v1] Wed, 18 Mar 2026 11:18:23 UTC (13,563 KB)"
  },
  {
    "id": "17625",
    "status": 200,
    "title": "Title: S-VGGT: Structure-Aware Subscene Decomposition for Scalable 3D Foundation Models",
    "abstract": "Abstract: Feed-forward 3D foundation models face a key challenge: the quadratic computational cost introduced by global attention, which severely limits scalability as input length increases. Concurrent acceleration methods, such as token merging, operate at the token level. While they offer local savings, the required nearest-neighbor searches introduce undesirable overhead. Consequently, these techniques fail to tackle the fundamental issue of structural redundancy dominant in dense capture data. In this work, we introduce \\textbf{S-VGGT}, a novel approach that addresses redundancy at the structural frame level, drastically shifting the optimization focus. We first leverage the initial features to build a dense scene graph, which characterizes structural scene redundancy and guides the subsequent scene partitioning. Using this graph, we softly assign frames to a small number of subscenes, guaranteeing balanced groups and smooth geometric transitions. The core innovation lies in designing the subscenes to share a common reference frame, establishing a parallel geometric bridge that enables independent and highly efficient processing without explicit geometric alignment. This structural reorganization provides strong intrinsic acceleration by cutting the global attention cost at its source. Crucially, S-VGGT is entirely orthogonal to token-level acceleration methods, allowing the two to be seamlessly combined for compounded speedups without compromising reconstruction fidelity. Code is available at this https URL .",
    "comments": "7 pages, 5 figures. Accepted by ICME 2026",
    "history": "Submission history From: Xinze Li [ view email ] [v1] Wed, 18 Mar 2026 11:42:55 UTC (1,054 KB)"
  },
  {
    "id": "17651",
    "status": 200,
    "title": "Title: Anchoring and Rescaling Attention for Semantically Coherent Inbetweening",
    "abstract": "Abstract: Generative inbetweening (GI) seeks to synthesize realistic intermediate frames between the first and last keyframes beyond mere interpolation. As sequences become sparser and motions larger, previous GI models struggle with inconsistent frames with unstable pacing and semantic misalignment. Since GI involves fixed endpoints and numerous plausible paths, this task requires additional guidance gained from the keyframes and text to specify the intended path. Thus, we give semantic and temporal guidance from the keyframes and text onto each intermediate frame through Keyframe-anchored Attention Bias. We also better enforce frame consistency with Rescaled Temporal RoPE, which allows self-attention to attend to keyframes more faithfully. TGI-Bench, the first benchmark specifically designed for text-conditioned GI evaluation, enables challenge-targeted evaluation to analyze GI models. Without additional training, our method achieves state-of-the-art frame consistency, semantic fidelity, and pace stability for both short and long sequences across diverse challenges.",
    "comments": "Accepted to CVPR 2026; Code is released at this https URL",
    "history": "Submission history From: Tae Eun Choi [ view email ] [v1] Wed, 18 Mar 2026 12:11:02 UTC (36,876 KB)"
  },
  {
    "id": "17652",
    "status": 200,
    "title": "Title: VectorWorld: Efficient Streaming World Model via Diffusion Flow on Vector Graphs",
    "abstract": "Abstract: Closed-loop evaluation of autonomous-driving policies requires interactive simulation beyond log replay. However, existing generative world models often degrade in closed loop due to (i) history-free initialization that mismatches policy inputs, (ii) multi-step sampling latency that violates real-time budgets, and (iii) compounding kinematic infeasibility over long horizons. We propose VectorWorld, a streaming world model that incrementally generates ego-centric $64 \\mathrm{m}\\times 64\\mathrm{m}$ lane--agent vector-graph tiles during rollout. VectorWorld aligns initialization with history-conditioned policies by producing a policy-compatible interaction state via a motion-aware gated VAE. It enables real-time outpainting via solver-free one-step masked completion with an edge-gated relational DiT trained with interval-conditioned MeanFlow and JVP-based large-step supervision. To stabilize long-horizon rollouts, we introduce $\\Delta$Sim, a physics-aligned non-ego (NPC) policy with hybrid discrete--continuous actions and differentiable kinematic logit shaping. On Waymo open motion and nuPlan, VectorWorld improves map-structure fidelity and initialization validity, and supports stable, real-time $1\\mathrm{km}+$ closed-loop rollouts (\\href{ this https URL }{code}).",
    "comments": "Under Review",
    "history": "Submission history From: Chaokang Jiang [ view email ] [v1] Wed, 18 Mar 2026 12:13:30 UTC (14,680 KB)"
  },
  {
    "id": "17655",
    "status": 200,
    "title": "Title: Interpretable Cross-Domain Few-Shot Learning with Rectified Target-Domain Local Alignment",
    "abstract": "Abstract: Cross-Domain Few-Shot Learning (CDFSL) adapts models trained with large-scale general data (source domain) to downstream target domains with only scarce training data, where the research on vision-language models (e.g., CLIP) is still in the early stages. Typical downstream domains, such as medical diagnosis, require fine-grained visual cues for interpretable recognition, but we find that current fine-tuned CLIP models can hardly focus on these cues, albeit they can roughly focus on important regions in source domains. Although current works have demonstrated CLIP&#39;s shortcomings in capturing local subtle patterns, in this paper, we find that the domain gap and scarce training data further exacerbate such shortcomings, much more than that of holistic patterns, which we call the local misalignment problem in CLIP-based CDFSL. To address this problem, due to the lack of supervision in aligning local visual features and text semantics, we turn to self-supervision information. Inspired by the translation task, we propose the CC-CDFSL method with cycle consistency, which translates local visual features into text features and then translates them back into visual features (and vice versa), and constrains the original features close to the translated back features. To reduce the noise imported by richer information in the visual modality, we further propose a Semantic Anchor mechanism, which first augments visual features to provide a larger corpus for the text-to-image mapping, and then shrinks the image features to filter out irrelevant image-to-text mapping. Extensive experiments on various benchmarks, backbones, and fine-tuning methods show we can (1) effectively improve the local vision-language alignment, (2) enhance the interpretability of learned patterns and model decisions by visualizing patches, and (3) achieve state-of-the-art performance.",
    "comments": "CVPR 2026",
    "history": "Submission history From: Yaze Zhao [ view email ] [v1] Wed, 18 Mar 2026 12:20:21 UTC (19,433 KB) [v2] Sun, 22 Mar 2026 04:49:26 UTC (19,436 KB)"
  },
  {
    "id": "17670",
    "status": 200,
    "title": "Title: AgentVLN: Towards Agentic Vision-and-Language Navigation",
    "abstract": "Abstract: Vision-and-Language Navigation (VLN) requires an embodied agent to ground complex natural-language instructions into long-horizon navigation in unseen environments. While Vision-Language Models (VLMs) offer strong 2D semantic understanding, current VLN systems remain constrained by limited spatial perception, 2D-3D representation mismatch, and monocular scale ambiguity. In this paper, we propose AgentVLN, a novel and efficient embodied navigation framework that can be deployed on edge computing platforms. We formulate VLN as a Partially Observable Semi-Markov Decision Process (POSMDP) and introduce a VLM-as-Brain paradigm that decouples high-level semantic reasoning from perception and planning via a plug-and-play skill library. To resolve multi-level representation inconsistency, we design a cross-space representation mapping that projects perception-layer 3D topological waypoints into the image plane, yielding pixel-aligned visual prompts for the VLM. Building on this bridge, we integrate a context-aware self-correction and active exploration strategy to recover from occlusions and suppress error accumulation over long trajectories. To further address the spatial ambiguity of instructions in unstructured environments, we propose a Query-Driven Perceptual Chain-of-Thought (QD-PCoT) scheme, enabling the agent with the metacognitive ability to actively seek geometric depth information. Finally, we construct AgentVLN-Instruct, a large-scale instruction-tuning dataset with dynamic stage routing conditioned on target visibility. Extensive experiments show that AgentVLN consistently outperforms prior state-of-the-art methods (SOTA) on long-horizon VLN benchmarks, offering a practical paradigm for lightweight deployment of next-generation embodied navigation models. Code: this https URL .",
    "comments": "19pages, 4 figures",
    "history": "Submission history From: Zihao Xin [ view email ] [v1] Wed, 18 Mar 2026 12:43:47 UTC (6,864 KB)"
  },
  {
    "id": "17685",
    "status": 200,
    "title": "Title: Flow Matching Policy with Entropy Regularization",
    "abstract": "Abstract: Diffusion-based policies have gained significant popularity in Reinforcement Learning (RL) due to their ability to represent complex, non-Gaussian distributions. Stochastic Differential Equation (SDE)-based diffusion policies often rely on indirect entropy control due to the intractability of the exact entropy, while also suffering from computationally prohibitive policy gradients through the iterative denoising chain. To overcome these issues, we propose Flow Matching Policy with Entropy Regularization (FMER), an Ordinary Differential Equation (ODE)-based online RL framework. FMER parameterizes the policy via flow matching and samples actions along a straight probability path, motivated by optimal transport. FMER leverages the model&#39;s generative nature to construct an advantage-weighted target velocity field from a candidate set, steering policy updates toward high-value regions. By deriving a tractable entropy objective, FMER enables principled maximum-entropy optimization for enhanced exploration. Experiments on sparse multi-goal FrankaKitchen benchmarks demonstrate that FMER outperforms state-of-the-art methods, while remaining competitive on standard MuJoco benchmarks. Moreover, FMER reduces training time by 7x compared to heavy diffusion baselines (QVPO) and 10-15% relative to efficient variants.",
    "history": "Submission history From: Ting Gao [ view email ] [v1] Wed, 18 Mar 2026 13:00:20 UTC (5,814 KB) [v2] Thu, 19 Mar 2026 17:21:12 UTC (12,220 KB) [v3] Tue, 26 May 2026 11:44:07 UTC (12,847 KB)"
  },
  {
    "id": "17692",
    "status": 200,
    "title": "Title: Can Blindfolded LLMs Still Trade? An Anonymization-First Framework for Portfolio Optimization",
    "abstract": "Abstract: For LLM trading agents to be genuinely trustworthy, they must demonstrate understanding of market dynamics rather than exploitation of memorized ticker associations. Building responsible multi-agent systems demands rigorous signal validation: proving that predictions reflect legitimate patterns, not pre-trained recall. We address two sources of spurious performance: memorization bias from ticker-specific pre-training, and survivorship bias from flawed backtesting. Our approach is to blindfold the agents--anonymizing all identifiers--and verify whether meaningful signals persist. BlindTrade anonymizes tickers and company names, and four LLM agents output scores along with reasoning. We construct a GNN graph from reasoning embeddings and trade using PPO-DSR policy. On 2025 YTD (through 2025-08-01), we achieved Sharpe 1.40 +/- 0.22 across 20 seeds and validated signal legitimacy through negative control experiments. To assess robustness beyond a single OOS window, we additionally evaluate an extended period (2024--2025), revealing market-regime dependency: the policy excels in volatile conditions but shows reduced alpha in trending bull markets.",
    "comments": "Accepted at the ICLR 2026 Workshop on Advances in Financial AI (FinAI). 18 pages, 7 figures",
    "history": "Submission history From: Joohyoung Jeon [ view email ] [v1] Wed, 18 Mar 2026 13:09:11 UTC (339 KB)"
  },
  {
    "id": "17693",
    "status": 200,
    "title": "Title: Learning Transferable Temporal Primitives for Video Reasoning via Synthetic Videos",
    "abstract": "Abstract: The transition from image to video understanding requires vision-language models (VLMs) to shift from recognizing static patterns to reasoning over temporal dynamics such as motion trajectories, speed changes, and state transitions. Yet current post-training methods fall short due to two critical limitations: (1) existing datasets often lack temporal-centricity, where answers can be inferred from isolated keyframes rather than requiring holistic temporal integration; and (2) training data generated by proprietary models contains systematic errors in fundamental temporal perception, such as confusing motion directions or misjudging speeds. We introduce SynRL, a post-training framework that teaches models temporal primitives, the fundamental building blocks of temporal understanding including direction, speed, and state tracking. Our key insight is that these abstract primitives, learned from programmatically generated synthetic videos, transfer effectively to real-world scenarios. We decompose temporal understanding into short-term perceptual primitives (speed, direction) and long-term cognitive primitives, constructing 7.7K CoT and 7K RL samples with ground-truth frame-level annotations through code-based video generation. Despite training on simple geometric shapes, SynRL achieves substantial improvements across 15 benchmarks spanning temporal grounding, complex reasoning, and general video understanding. Remarkably, our 7.7K synthetic CoT samples outperform Video-R1 with 165K real-world samples. We attribute this to fundamental temporal skills, such as tracking frame by frame changes and comparing velocity, that transfer effectively from abstract synthetic patterns to complex real-world scenarios. This establishes a new paradigm for video post-training: video temporal learning through carefully designed synthetic data provides a more cost efficient scaling path.",
    "history": "Submission history From: Songtao Jiang [ view email ] [v1] Wed, 18 Mar 2026 13:10:47 UTC (2,372 KB)"
  },
  {
    "id": "17735",
    "status": 200,
    "title": "Title: TAPESTRY: From Geometry to Appearance via Consistent Turntable Videos",
    "abstract": "Abstract: Automatically generating photorealistic and self-consistent appearances for untextured 3D models is a critical challenge in digital content creation. The advancement of large-scale video generation models offers a natural approach: directly synthesizing 360-degree turntable videos (TTVs), which can serve not only as high-quality dynamic previews but also as an intermediate representation to drive texture synthesis and neural rendering. However, existing general-purpose video diffusion models struggle to maintain strict geometric consistency and appearance stability across the full range of views, making their outputs ill-suited for high-quality 3D reconstruction. To this end, we introduce TAPESTRY, a framework for generating high-fidelity TTVs conditioned on explicit 3D geometry. We reframe the 3D appearance generation task as a geometry-conditioned video diffusion problem: given a 3D mesh, we first render and encode multi-modal geometric features to constrain the video generation process with pixel-level precision, thereby enabling the creation of high-quality and consistent TTVs. Building upon this, we also design a method for downstream reconstruction tasks from the TTV input, featuring a multi-stage pipeline with 3D-Aware Inpainting. By rotating the model and performing a context-aware secondary generation, this pipeline effectively completes self-occluded regions to achieve full surface coverage. The videos generated by TAPESTRY are not only high-quality dynamic previews but also serve as a reliable, 3D-aware intermediate representation that can be seamlessly back-projected into UV textures or used to supervise neural rendering methods like 3DGS. This enables the automated creation of production-ready, complete 3D assets from untextured meshes. Experimental results demonstrate that our method outperforms existing approaches in both video consistency and final reconstruction quality.",
    "history": "Submission history From: Yan Zeng [ view email ] [v1] Wed, 18 Mar 2026 14:02:09 UTC (28,232 KB)"
  },
  {
    "id": "17761",
    "status": 200,
    "title": "Title: Evidence Packing for Cross-Domain Image Deepfake Detection with LVLMs",
    "abstract": "Abstract: Image Deepfake Detection (IDD) separates manipulated images from authentic ones by spotting artifacts of synthesis or tampering. Although large vision-language models (LVLMs) offer strong image understanding, adapting them to IDD often demands costly fine-tuning and generalizes poorly to diverse, evolving manipulations. We propose the Semantic Consistent Evidence Pack (SCEP), a training-free LVLM framework that replaces whole-image inference with evidence-driven reasoning. SCEP mines a compact set of suspicious patch tokens that best reveal manipulation cues. It uses the vision encoder&#39;s CLS token as a global reference, clusters patch features into coherent groups, and scores patches with a fused metric combining CLS-guided semantic mismatch with frequency-and noise-based anomalies. To cover dispersed traces and avoid redundancy, SCEP samples a few high-confidence patches per cluster and applies grid-based NMS, producing an evidence pack that conditions a frozen LVLM for prediction. Experiments on diverse benchmarks show SCEP outperforms strong baselines without LVLM fine-tuning.",
    "history": "Submission history From: Yuxin Liu [ view email ] [v1] Wed, 18 Mar 2026 14:22:45 UTC (455 KB)"
  },
  {
    "id": "17782",
    "status": 200,
    "title": "Title: Exploring parameter-efficient fine-tuning (PEFT) of billion-parameter vision models with QLoRA and DoRA: insights into generalization for limited-data image classification under a 98:1 test-to-train regime",
    "abstract": "Abstract: Automated behavior classification is essential for precision livestock farming but faces challenges of high computational costs and limited labeled data. This study systematically compared three approaches: training from scratch (ResNet-18, ViT-Small), frozen feature extraction, and parameter-efficient fine-tuning (PEFT) of the DINOv3 foundation model (6.7 billion parameters). We evaluated QLoRA and DoRA across multiple configurations varying rank (8, 16, 64) and target modules (q_proj versus all-linear layers). With 2,160 verified training images, we assessed generalization of our model on 211,800 test samples, which is essentially a 98:1 test-to-train ratio. Results demonstrated that PEFT substantially outperformed alternatives, where the best QLoRA configuration (all-linear layers and rank=64) achieved 83.16% test accuracy with only 2.72% parameters (183.0M) in 5.8 hours, compared to 72.87% for ResNet-18 (16.8 hours), 61.91% for ViT-Small (18.7 hours), and 76.56% for frozen DINOv3 (17.5 hours). DoRA achieved comparable accuracy (83.14%) but with longer training time (11.0 hours). Notably, increasing adapter capacity consistently improved generalization while simultaneously not causing overfitting: reducing rank from 16 to 8 decreased test accuracy from 78.38% to 77.17%, while expanding from q_proj-only to all-linear layers with rank=64 improved accuracy from 78.38% to 83.16%. This suggests underfitting, instead of overfitting, is the primary challenge when adapting foundation models to agricultural imagery. Our findings provide guidelines for deploying billion-parameter vision models with PEFT in agricultural livestock applications.",
    "history": "Submission history From: Haiyu Yang [ view email ] [v1] Wed, 18 Mar 2026 14:46:07 UTC (3,901 KB)"
  },
  {
    "id": "17808",
    "status": 200,
    "title": "Title: EVA: Aligning Video World Models with Executable Robot Actions via Inverse Dynamics Rewards",
    "abstract": "Abstract: Video generative models are increasingly used as world models for robotics, where a model generates a future visual rollout conditioned on the current observation and task instruction, and an inverse dynamics model (IDM) converts the generated frames into executable robot actions. However, current video world models lack explicit executability constraints. As a result, visually coherent rollouts may still violate rigid-body and kinematic consistency, producing unstable or infeasible control commands when decoded by an IDM. We refer to this mismatch between visual generation and physically executable control as the executability gap. While this gap can be mitigated at inference time using techniques such as rejection sampling, such approaches are inefficient due to the high cost of video generation. In this paper, we leverage the executability gap as a training signal and introduce Executable Video Alignment (EVA), a reinforcement-learning post-training framework for aligning video world models. EVA trains an inverse dynamics model on real robot trajectories and repurposes it as a reward model that evaluates generated videos through the action sequences they induce, encouraging smooth motions measured by velocity, acceleration, and jerk while penalizing actions that violate embodiment constraints. Importantly, the reward remains informative even when generated videos contain severe visual artifacts, since such artifacts typically translate into unstable or out-of-bound actions. Experiments on the RoboTwin benchmark and a real bimanual robot show that EVA reduces embodiment-specific artifacts in generated rollouts and improves downstream task execution success.",
    "comments": "Project page: this https URL",
    "history": "Submission history From: Ruixiang Wang [ view email ] [v1] Wed, 18 Mar 2026 15:02:19 UTC (13,845 KB) [v2] Tue, 24 Mar 2026 17:12:47 UTC (15,547 KB)"
  },
  {
    "id": "17812",
    "status": 200,
    "title": "Title: ChopGrad: Pixel-Wise Losses for Latent Video Diffusion via Truncated Backpropagation",
    "abstract": "Abstract: Recent video diffusion models achieve high-quality generation through recurrent frame processing where each frame generation depends on previous frames. However, this recurrent mechanism means that training such models in the pixel domain incurs prohibitive memory costs, as activations accumulate across the entire video sequence. This fundamental limitation also makes fine-tuning these models with pixel-wise losses computationally intractable for long or high-resolution videos. This paper introduces ChopGrad, a truncated backpropagation scheme for video decoding, limiting gradient computation to local frame windows while maintaining global consistency. We provide a theoretical analysis of this approximation and show that it enables efficient fine-tuning with frame-wise losses. ChopGrad reduces training memory from scaling linearly with the number of video frames (full backpropagation) to constant memory, and compares favorably to existing state-of-the-art video diffusion models across a suite of conditional video generation tasks with pixel-wise losses, including video super-resolution, video inpainting, video enhancement of neural-rendered scenes, and controlled driving video generation.",
    "history": "Submission history From: Dmitriy Rivkin [ view email ] [v1] Wed, 18 Mar 2026 15:04:57 UTC (36,513 KB) [v2] Tue, 7 Apr 2026 18:00:52 UTC (26,834 KB)"
  },
  {
    "id": "17813",
    "status": 200,
    "title": "Title: M2P: Improving Visual Foundation Models with Mask-to-Point Weakly-Supervised Learning for Dense Point Tracking",
    "abstract": "Abstract: Tracking Any Point (TAP) has emerged as a fundamental tool for video understanding. Current approaches adapt Vision Foundation Models (VFMs) like DINOv2 via offline finetuning or test-time optimization. However, these VFMs rely on static image pre-training, which is inherently sub-optimal for capturing dense temporal correspondence in videos. To address this, we propose Mask-to-Point (M2P) learning, which leverages rich video object segmentation (VOS) mask annotations to improve VFMs for dense point tracking. Our M2P introduces three new mask-based constraints for weakly-supervised representation learning. First, we propose a local structure consistency loss, which leverages Procrustes analysis to model the cohesive motion of points lying within a local structure, achieving more reliable point-to-point matching learning. Second, we propose a mask label consistency (MLC) loss, which enforces that sampled foreground points strictly match foreground regions across frames. The proposed MLC loss can be regarded as a regularization, which stabilizes training and prevents convergence to trivial solutions. Finally, mask boundary constrain is applied to explicitly supervise boundary points. We show that our weaklysupervised M2P models significantly outperform baseline VFMs with efficient training by using only 3.6K VOS training videos. Notably, M2P achieves 12.8% and 14.6% performance gains over DINOv2-B/14 and DINOv3-B/16 on the TAP-Vid-DAVIS benchmark, respectively. Moreover, the proposed M2P models are used as pre-trained backbones for both test-time optimized and offline fine-tuned TAP tasks, demonstrating its potential to serve as general pre-trained models for point tracking. Code will be made publicly available upon acceptance.",
    "history": "Submission history From: Qiangqiang Wu [ view email ] [v1] Wed, 18 Mar 2026 15:06:22 UTC (3,370 KB)"
  },
  {
    "id": "17825",
    "status": 200,
    "title": "Title: Steering Video Diffusion Transformers with Massive Activations",
    "abstract": "Abstract: Despite rapid progress in video diffusion transformers, how their internal model signals can be leveraged with minimal overhead to enhance video generation quality remains underexplored. In this work, we study the role of Massive Activations (MAs), which are rare, high-magnitude hidden state spikes in video diffusion transformers. We observed that MAs emerge consistently across all visual tokens, with a clear magnitude hierarchy: first-frame tokens exhibit the largest MA magnitudes, latent-frame boundary tokens (the head and tail portions of each temporal chunk in the latent space) show elevated but slightly lower MA magnitudes than the first frame, and interior tokens within each latent frame remain elevated, yet are comparatively moderate in magnitude. This structured pattern suggests that the model implicitly prioritizes token positions aligned with the temporal chunking in the latent space. Based on this observation, we propose Structured Activation Steering (STAS), a training-free self-guidance-like method that steers MA values at first-frame and boundary tokens toward a scaled global maximum reference magnitude. STAS achieves consistent improvements in terms of video quality and temporal coherence across different text-to-video models, while introducing negligible computational overhead.",
    "history": "Submission history From: Xianhang Cheng [ view email ] [v1] Wed, 18 Mar 2026 15:24:12 UTC (22,247 KB) [v2] Sun, 23 Aug 2026 10:05:23 UTC (50,671 KB)"
  },
  {
    "id": "17834",
    "status": 200,
    "title": "Title: Generative Control as Optimization: Time Unconditional Flow Matching for Adaptive and Robust Robotic Control",
    "abstract": "Abstract: Diffusion models and flow matching have become a cornerstone of robotic imitation learning, yet they suffer from a structural inefficiency where inference is often bound to a fixed integration schedule that is agnostic to state complexity. This paradigm forces the policy to expend the same computational budget on trivial motions as it does on complex tasks. We introduce Generative Control as Optimization (GeCO), a time-unconditional framework that transforms action synthesis from trajectory integration into iterative optimization. GeCO learns a stationary velocity field in the action-sequence space where expert behaviors form stable attractors. Consequently, test-time inference becomes an adaptive process that allocates computation based on convergence--exiting early for simple states while refining longer for difficult ones. Furthermore, this stationary geometry yields an intrinsic, training-free safety signal, as the field norm at the optimized action serves as a robust out-of-distribution (OOD) detector, remaining low for in-distribution states while significantly increasing for anomalies. We validate GeCO on standard simulation benchmarks and demonstrate seamless scaling to pi0-series Vision-Language-Action (VLA) models. As a plug-and-play replacement for standard flow-matching heads, GeCO improves success rates and efficiency with an optimization-native mechanism for safe deployment. Video and code can be found at this https URL",
    "comments": "10 pages, 6 figures",
    "history": "Submission history From: Runhan Huang [ view email ] [v1] Wed, 18 Mar 2026 15:27:17 UTC (4,130 KB) [v2] Sun, 26 Apr 2026 06:47:15 UTC (4,911 KB)"
  },
  {
    "id": "17840",
    "status": 200,
    "title": "Title: Video Understanding: From Geometry and Semantics to Unified Models",
    "abstract": "Abstract: Video understanding aims to enable models to perceive, reason about, and interact with the dynamic visual world. In contrast to image understanding, video understanding inherently requires modeling temporal dynamics and evolving visual context, placing stronger demands on spatiotemporal reasoning and making it a foundational problem in computer vision. In this survey, we present a structured overview of video understanding by organizing the literature into three complementary perspectives: low-level video geometry understanding, high-level semantic understanding, and unified video understanding models. We further highlight a broader shift from isolated, task-specific pipelines toward unified modeling paradigms that can be adapted to diverse downstream objectives, enabling a more systematic view of recent progress. By consolidating these perspectives, this survey provides a coherent map of the evolving video understanding landscape, summarizes key modeling trends and design principles, and outlines open challenges toward building robust, scalable, and unified video foundation models.",
    "comments": "A comprehensive survey of video understanding, spanning low-level geometry, high-level semantics, and unified understanding models",
    "history": "Submission history From: Zhaochong An [ view email ] [v1] Wed, 18 Mar 2026 15:31:47 UTC (2,664 KB)"
  },
  {
    "id": "17850",
    "status": 200,
    "title": "Title: ProbeFlow: Training-Free Adaptive Flow Matching for Vision-Language-Action Models",
    "abstract": "Abstract: Recent Vision-Language-Action (VLA) models equipped with Flow Matching (FM) action heads achieve state-of-the-art performance in complex robot manipulation. However, the multi-step iterative ODE solving required by FM introduces inference latency that precludes responsive physical control. While current acceleration efforts optimize the Vision-Language Model (VLM) backbone, the action head bottleneck remains overlooked. To address this, we propose ProbeFlow, a training-free adaptive inference framework tai- lored for continuous robotic control. By evaluating geometric trajectory complexity via the cosine similarity between initial and lookahead velocity vectors, ProbeFlow dynamically sched- ules integration steps to prune redundant network evaluations. On the MetaWorld benchmark, it accelerates action decoding by 14.8x (reducing average steps from N = 50 to 2.6) and cuts end-to-end system latency by 2.8x without compromising the manipulation success rate. On the long-horizon LIBERO benchmark, the probe automatically allocates a denser schedule to navigate semantic bottlenecks, effectively resolving the flow solver delay. Real-world physical deployments confirm that ProbeFlow successfully mitigates action decoding latency while ensuring execution stability, offering a highly practical solution for low-latency continuous generative policies.",
    "history": "Submission history From: Zhou Fang [ view email ] [v1] Wed, 18 Mar 2026 15:38:29 UTC (1,717 KB) [v2] Sat, 3 Oct 2026 04:52:18 UTC (4,620 KB)"
  },
  {
    "id": "17889",
    "status": 200,
    "title": "Title: Identity as Presence: Towards Appearance and Voice Personalized Joint Audio-Video Generation",
    "abstract": "Abstract: Recent advances have demonstrated compelling capabilities in synthesizing real individuals into generated videos, reflecting the growing demand for identity-aware content creation. Nevertheless, an openly accessible framework enabling fine-grained control over facial appearance and voice timbre across multiple identities remains unavailable. In this work, we present a unified and scalable framework for identity-aware joint audio-video generation, enabling high-fidelity and consistent personalization. Specifically, we introduce a data curation pipeline that automatically extracts identity-bearing information with paired annotations across audio and visual modalities, covering diverse scenarios from single-subject to multi-subject interactions. We further propose a flexible and scalable identity injection mechanism for single- and multi-subject scenarios, in which both facial appearance and vocal timbre act as identity-bearing control signals. Moreover, in light of modality disparity, we design a multi-stage training strategy to accelerate convergence and enforce cross-modal coherence. Experiments demonstrate the superiority of the proposed framework. For more details and qualitative results, please refer to our webpage: \\href{ this https URL }{Identity-as-Presence}.",
    "history": "Submission history From: Yingjie Chen [ view email ] [v1] Wed, 18 Mar 2026 16:13:48 UTC (24,362 KB) [v2] Mon, 23 Mar 2026 04:54:14 UTC (24,362 KB) [v3] Wed, 25 Mar 2026 03:39:26 UTC (24,362 KB) [v4] Fri, 7 Aug 2026 05:51:08 UTC (10,510 KB)"
  },
  {
    "id": "17891",
    "status": 200,
    "title": "Title: RAMP: Reinforcement Adaptive Mixed Precision Quantization for Efficient On Device LLM Inference",
    "abstract": "Abstract: Post training quantization is essential for deploying large language models (LLMs) on resource constrained hardware, yet state of the art methods enforce uniform bit widths across layers, yielding suboptimal accuracy efficiency trade offs. We present RAMP (Reinforcement Adaptive Mixed Precision), an off policy Soft Actor Critic framework that learns per layer bit width assignments to minimize perplexity under a global bit budget. The policy conditions on an 11 dimensional embedding of activation statistics, weight properties, and structural descriptors, enabling zero shot transfer across model families and scales. To enable stable sub 4 bit quantization, we introduce Scale Folding, a preconditioning technique that migrates activation outliers into weights via per channel scaling and normalization layer compensation. A quality prioritized reward with asymmetric penalties and budget cliffs drives rapid convergence. On Llama 2 7B, RAMP achieves 5.54 perplexity at 3.68GB (3.65 effective bits), outperforming uniform 4 bit AWQ (5.60 at 3.90 GB) and GPTQ by 6% in size and 1% to3% in quality. Critically, a policy trained only on Llama 2 7B generalizes zero shot to Llama 2 13B and Mistral 7B, often surpassing target specific training, supporting the hypothesis that quantization sensitivity is primarily architectural. The HALO pipeline exports allocations to GGUF format for kernel free inference on CPUs, GPUs, and edge devices, retaining 99.5% of FP16 commonsense reasoning performance.",
    "history": "Submission history From: Saurabh Jha [ view email ] [v1] Wed, 18 Mar 2026 16:16:28 UTC (9,471 KB)"
  },
  {
    "id": "17952",
    "status": 200,
    "title": "Title: Gender Disambiguation in Machine Translation: Diagnostic Evaluation in Decoder-Only Architectures",
    "abstract": "Abstract: While Large Language Models achieve state-of-the-art results across a wide range of NLP tasks, they remain prone to systematic biases. Among these, gender bias is particularly salient in MT, due to systematic differences across languages in whether and how gender is marked. As a result, translation often requires disambiguating implicit source signals into explicit gender-marked forms. In this context, standard benchmarks may capture broad disparities but fail to reflect the full complexity of gender bias in modern MT. In this paper, we extend recent frameworks on bias evaluation by: (i) introducing a novel measure coined &#34;Prior Bias&#34;, capturing a model&#39;s default gender assumptions, and (ii) applying the framework to decoder-only MT models. Our results show that, despite their scale and state-of-the-art status, decoder-only models do not generally outperform encoder-decoder architectures on gender-specific metrics; however, post-training (e.g., instruction tuning) not only improves contextual awareness but also reduces the masculine Prior Bias.",
    "history": "Submission history From: Chiara Manna [ view email ] [v1] Wed, 18 Mar 2026 17:26:36 UTC (10,127 KB)"
  }
]
```


## 原42剩余20完整题摘：作者贡献判断提案（2026-10-12，待非准备者校准）

实际完整exact-v1 AB已读；current每条官方abs HTTP200 title/AB/Comments/history轻量读取（Comments实际class包含mathjax，第二次正确恢复，不用第一次空匹配冒称无说明）。以下16仅具体潜力2+1+2=5提案、4项具体EX提案，不自动加入候选、不授Source/Books。必要日字段复用上面42 exact DOI/availability夹证；17475 EACL2026有决定归属信号须定点确认，不用accepted当firstpublic。17605/17655/17520 CVPR、17470 Findings只后发venue现有说明，无已见窗前正文日期，不扫全部venue。17527v2/17655v2/17470v2/17510v2仅history，不机械diff；真正受影响claim再核。

| 身份 | 原约束→原文增量→会改变的选择 | 提案/候选主线 |
| --- | --- | --- |
| [PEFT-DINOv317782v1](https://arxiv.org/abs/2603.17782v1) | 少样本常按降低adapter容量抑制过拟合→rank/target-module对照呈capacity增大仍改善test generalization→需核哪些人口是underfit而非套用small-data必须小adapter | 2+1+2=5；TRAIN-LORA |
| [M2P17813v1](https://arxiv.org/abs/2603.17813v1) | 静态DINO对应不适合视频点追踪→VOS弱标签局部Procrustes/foreground与边界约束→需核representation预训练怎样获得时序对应 | 2+1+2=5；MULTIMODAL-REPRESENTATION |
| [SCEP17761v1](https://arxiv.org/abs/2603.17761v1) | 整图LVLM语义会掩盖微小操纵cue→语义簇内CLS差异/频谱/残差评分保少量patch→需核frozen LVLM输入选择与局部证据/质量成本条件 | 2+1+2=5；MULTIMODAL-REPRESENTATION |
| [CC-CDFSL17655v1](https://arxiv.org/abs/2603.17655v1) | 少目标域标签对CLIP局部对齐比全局更坏→双向patch/text循环及semantic anchor→需核域迁移时局部表示校准条件 | 2+1+2=5；MULTIMODAL-REPRESENTATION |
| [ReLaGS17605v1](https://arxiv.org/abs/2603.17605v1) | object-centric3D语言表示或每scene训练难支持relation→多视图语言对齐的hierarchical Gaussians/scenegraph→需核场景表示与关系消费者的训练/资源取舍 | 2+1+2=5；MULTIMODAL-WORLD-MODELS |
| [PCA-Seg17520v1](https://arxiv.org/abs/2603.17520v1) | costvolume串行class/spatial聚合互扰→双流并行及pixel权重/正交约束→需核VLM表示融合可否避免串行更新干扰 | 2+1+2=5；MULTIMODAL-REPRESENTATION |
| [GPT2-abstraction17475v1](https://arxiv.org/abs/2603.17475v1) | 词项行为与类别抽象可能误作同步→next-token divergence训练轨迹先类别后词项/突变→需核模型能力形成的先后与评价粒度；EACL先稿信号待必要归属核 | 2+1+2=5；TRAIN-PRETRAINING |
| [DACSM17474v1](https://arxiv.org/abs/2603.17474v1) | crossattention跨域内容与style/scale迁移混合→Q与KV角色假说和定点扰动/cross-scale匹配→需核训练扰动对表征不变性的成立条件，非先授Q内容/KV风格定律 | 2+1+2=5；MODEL-SELF-ATTENTION |
| [PJB17386v1](https://arxiv.org/abs/2603.17386v1) | 总体检索平均分掩盖投资决策→domain异质性比module增益大且queryunderstanding+rerank反退→需核检索模块收益非可加与分层诊断 | 2+1+2=5；PLATFORM-EVALUATION-SYSTEM |
| [VirPro17470v1](https://arxiv.org/abs/2603.17470v1) | 确定性类别prompt不能表示instance场景差异→ROI条件多Gaussian prompt/contrastive→需核条件prompt分布与视觉弱监督representation，不授其方差是真uncertainty | 2+1+2=5；MULTIMODAL-REPRESENTATION |
| [GenderDisambiguation17952v1](https://arxiv.org/abs/2603.17952v1) | LLM整体MT更好未必性别上下文更好→PriorBias测量及decoder-only/encoder-decoder/IFT反对照→需核architecture和posttraining收益的分项条件 | 2+1+2=5；PLATFORM-EVALUATION-SYSTEM |
| [BlindTrade17692v1](https://arxiv.org/abs/2603.17692v1) | ticker记忆与survivorship可误授LLM信号→标识匿名化/negative-control与regime测试→需核评价数据泄漏/记忆负控制，不采交易收益或financial建议 | 2+1+2=5；PLATFORM-EVALUATION-SYSTEM |
| [FoMo-X17570v1](https://arxiv.org/abs/2603.17570v1) | PFN零样本outlier scalar缺diagnostic且MCdropout昂贵→同simulator prior训练附加severity/uncertainty heads→需核单forward诊断代理与真实epistemic uncertainty资格 | 2+1+2=5；MODEL-FFN |
| [RiemannianMD17527v1](https://arxiv.org/abs/2603.17527v1) | EuclideanMD geometry不能直接覆盖orthogonal-weight约束→重参数化RMD/stochastic Stiefel CGD→需核矩阵受限模型训练的geometry与收敛条件，非普遍优化更好 | 2+1+2=5；TRAIN-PRETRAINING |
| [QuantFL17507v1](https://arxiv.org/abs/2603.17507v1) | 量化更新通常依赖EF/额外状态→pretrained初始化的集中更新允许轻bucket→需核初始化与通信量化quality/budget共存条件，小数据集本身不EX | 2+1+2=5；TRAIN-DISTRIBUTED-TRAINING |
| [WINFlowNets17301v1](https://arxiv.org/abs/2603.17301v1) | 连续flow-policy inflow估计依赖先训predecessor retrieval→随机warmup/双网络共享replay共训→需核policy/learned predecessor共同漂移及fault适应条件，不是RAG检索 | 2+1+2=5；MULTIMODAL-EMBODIED-VLA |

### 具体排除提案与实际决定范围

- [VideoUnderstandingSurvey17840v1](https://arxiv.org/abs/2603.17840v1)：完整题摘只组织geometry/semantic/unified既有文献与趋势，未给改变已有解释的新增机制、适用边界或诊断反证；非综述一概EX。
- [CagingAgents17419v1](https://arxiv.org/abs/2603.17419v1)：完整题摘后安全定点§4.1–4.4、§5.1–5.3及§6.4/§8.1–8.2：新实证是VM凭证散落/权限与配置漂移，四层K8s本身§6.4为迁移target；原威胁来自引用的既有redteam，成熟sandbox/proxy/allowlist/untrusted标注与privileged-auditor限制未新增model-execution失效边界或独立attack-validation。对本主线目前是部署组合与现有安全原则实例，不以healthcare词或组合形式自动EX；保AB声称全部已部署和真实target区分/安全声明未授。
- [ContextMORLNavigation17510v1](https://arxiv.org/abs/2603.17510v1)：完整题摘后二次§3/§4.1–4.3 Eq3–7：VLM生成scene JSON，LLM更新文字rule，再LLM译数值MORL preference；所谓nonnegotiable基线只另给LLM提示，未给新增约束消费/validation/失败处理机制或控制可靠性条件。本文采用既有MORL的新用户偏好场景/组合并报告component/user/robot指标，未识别足以改变主线解释的增量，不以robot应用或safe字眼单独EX。
- [RideJudge17328v1](https://arxiv.org/abs/2603.17328v1)：完整题摘后二次§5L187–202：视觉alignment→expert-CoA SFT→DAPO及0.2–0.8难度人口，ordinal reward仅按预测与gold label rank距离赋分/format加权；新域数据/专家协议组合+既有等级reward shaping，不提出改变reward/credit归因条件的机制或设计反证。88.41/与大底座域准确率不单独准入，未因尚无完整d配方而EX；保原多模态ordinal问题价值，但不借通用reward成熟原则加分。

决定准入的二次正文范围：SCEP v1II入口L52–79；RMD v1§1L34–62说明orthogonal-weight/Stiefel直接关系；WINFlowv1§3.2–3.3 L88–109确认predecessor retrieval/双训练接口；DACSM v1III L94–126确认crossdomain Q/KV训练对象；VirPro v1§3.1–3.2 L93–120确认ROI条件mean/variance。仅消歧，不授关键评价/理论/完整实现Source通过。Caging安全原coreL202–217/241–291/304–306/342–347与ContextMORL L102–169、RideJudge L187–202如上实际读，足以判断所声称增量后停止，未读全部附件/代码/旧修订。源链接为官方精确版本；网页包装wordlim限制不改变研究范围，以上均自己的限定判断，不复制原稿段落。

### 17475 exact EACL 同稿信号的必要日期核验（2026-10-12）

作者实际打开[出版方单条](https://aclanthology.org/2026.eacl-long.32/)完整题摘及作者：Humans and transformer LMs: Abstraction drives language learning，Jasper Jian/Christopher D Manning；同GPT-2 small、next-token divergence与抽象先于词项的AB身份一致。出版字段仅March2026；PDF搜索可见March24–29是会议区间，不当正文首次公开日期。精确Crossref DOI `10.18653/v1/2026.eacl-long.32` HTTP200匹配同题/两作者，published与published-print只有2026年，created `2026-03-23T20:23:46Z` 不证明firstbody，更没有窗前正文日期。

只核该exactXML路径的有限导入信号：[GitHub commits exact path、截止03/24](https://api.github.com/repos/acl-org/acl-anthology/commits?path=data/xml/2026.eacl.xml&until=2026-03-24T00:00:00Z&per_page=10)实际HTTP200返回一条 `4bf88869f5d590175a60923cc709cbd1f59cc4b5`，时间 `2026-03-20T18:00:25Z`、Ingest EACL2026。该commit的contents API HTTP200但encoding=none（size1385451），并非空原证；一次转其[精确blob](https://api.github.com/repos/acl-org/acl-anthology/git/blobs/99a90fcdd5cfdeae592c8b0c0f264ea94dfed5db) HTTP200/base64，实际读取paper id32完整title/两作者/pages752–765/完整AB/url2026.eacl-long.32/bibkey，身份如上。raw入口单次transport失败已由官方blob恢复，不当日期受阻。

此有限信号只显示精确出版方条目导入03/20、Crossref创建03/23，没有新的窗前公开正文证据；**XML ingest与Crossref created均不证明全球firstpublic**，不据此授03/20出版首日或重置arXiv归属。原exact arXiv DOI/availability03/19自然日夹证仍有效，可保本日首次arXiv论文事件候选5分；若以后取得真正窗前同稿正文发布日期，只定点重开此family。必要同稿信号够证即停，不遍EACL全列表/全部历史；交非准备者定点final日期校准，未自授Source/Books或DAY。



