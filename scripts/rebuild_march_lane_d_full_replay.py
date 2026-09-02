#!/usr/bin/env python3
"""Author-side Full Replay for 2026-03-25..31.

This wrapper deliberately reuses only the evidence-packet renderer from lane C.
Its candidate denominator, Books eligibility and Stable Node routes are all
explicitly re-audited for the corrected official-announcement ownership receipt.
It never reads a Weekly and never writes shared Books.
"""

from __future__ import annotations

import re
import time
import json
from pathlib import Path

import rebuild_march_lane_c_full_replay as base


SELECTED = {
    25: """22300 22339 22350 22489 22751 22774 22858 22868 22910 23049 23149 23376""",
    26: """23528 23610 23791 23806 23914 24060 24124 24203""",
    27: """24595 24755 24775 24963 25056 25158 25685 25702 25716""",
    28: "",
    29: "",
    30: """25764 25973 25981 26074 26498 26557 26666""",
    31: """26728 26942 26993 27116 27138 27204 27287 27355 27467 27517 27624
        27819 28013 28101 28239 28565""",
}
SELECTED = {day: [f"2603.{suffix}" for suffix in value.split()] for day, value in SELECTED.items()}


INTEGRATE = """22300 22339 22350 22751 22774 22858 22868 22910 23049 23149 23376
    23528 23610 23806 23914 24060 24124
    24595 24755 24775 24963 25056 25158 25685 25702 25716
    25764 25973 25981 26074 26498 26557 26666
    26728 26942 26993 27116 27138 27204 27287 27624
    27819 28013 28101 28239 28565"""
INTEGRATE = {f"2603.{suffix}" for suffix in INTEGRATE.split()}


GROUPS = {
    "WORLDVIEW-SCALING-LAW": "22339",
    "MODEL-SELF-ATTENTION": "22300",
    "MODEL-LONG-CONTEXT": "22329",
    "MULTIMODAL-REPRESENTATION": "24680",
    "MULTIMODAL-WORLD-MODELS": "23149 23376 23497 24402 24506 25685 25716 25981 27287 27449 28489",
    "MULTIMODAL-EMBODIED-VLA": "24060 24393 24584 25661 25766 26360 26666 28565",
    "TRAIN-LORA": "26299",
    "TRAIN-RLHF": "22563 24124",
    "TRAIN-PPO": "27515",
    "TRAIN-GRPO": "23414 23871 23951 24984 28101 28204 28718",
    "TRAIN-PRETRAINING": "23998 27164 27226 28765",
    "INFER-REQUEST-LIFECYCLE": "23528 23640 26557 27960",
    "INFER-DECODE": "23914",
    "INFER-KV-CACHE": "22910 27467 27469 27819 28430",
    "INFER-SPECULATIVE-DECODING": "23483 25702",
    "INFER-TENSORRT-LLM": "22324 22774 22855 23343 23495 23566 23575 23985 24595 25011 25284 25719 26595 27624 27914 28239 28342 28405",
    "INFER-GPU-MEMORY": "27138",
    "INFER-SCHEDULING": "23888 26498 28622",
    "PLATFORM-FOUNDATIONS": "24963",
    "PLATFORM-GATEWAY": "26728",
    "PLATFORM-GPU-SCHEDULER": "22691",
    "PLATFORM-EVALUATION-SYSTEM": "22582 22744 22812 23292 23448 23509 23522 23749 23840 23848 23853 23934 24582 24621 24631 25001 25342 25711 24755 25764 25780 26337 26363 26539 26576 26648 26718 27539 27752 28005 28360 28407 28569 28590",
    "PLATFORM-TRACE": "23806 26942 28106 28551",
    "PLATFORM-SECURITY": "22341 22350 22751 22853 22868 22869 22928 23791 25056 25164 25412 26221 27148 27204 27517 27771 28013 28650",
    "PLATFORM-PRODUCTION": "27355",
    "AGENT-CONTEXT": "23527",
    "AGENT-RAG": "23049 26074",
    "AGENT-MEMORY": "22858 23013 23231 23530 23610 25097 25973 27116",
    "AGENT-TOOL-CALLING": "24709",
    "AGENT-PLANNING": "23909",
    "AGENT-REFLECTION": "24018 24639",
    "AGENT-WORKFLOW": "22367",
    "AGENT-MULTI-AGENT": "22823 24676 25928 26034 26993",
    "AGENT-MCP": "22489 24203 24703 24747 24775 24943",
    "AGENT-PLATFORM": "22447 22455 25158 27905 28010",
}


# Author synthesis is deliberately keyed by Source Family.  Exact-v1 excerpts
# stay in the packet as evidence; these four fields are the reviewer's concise
# statement of the systems delta and may not be replaced by abstract/section
# copies.
PAPER_SYNTHESIS = {
    "2603.22300": (
        "长上下文 attention 过去主要沿 sequence 轴做窗口、近似或 token pruning，代价是直接丢掉一部分 token 关系。",
        "SFA 改为稀疏化 query/key 的 feature 维，并用 IO-aware FlashSFA kernel 执行；控制权从 token admission 转到 feature-code 与 kernel layout。",
        "exact-v1 比较预训练与长序列效率，能支持所测模型和 kernel 上的 accuracy/throughput 边界；不能证明任意任务都比 sequence sparsity 更稳。",
        "feature 编码和专用 kernel 增加实现复杂度，稀疏码碰撞会损伤全局关系；中短序列或缺少 kernel 支持时 dense attention 仍合理。",
    ),
    "2603.22339": (
        "IsoFLOP 二次曲线拟合之所以流行，是因为它用少量定算力实验即可估计 compute-optimal 参数/数据配比。",
        "论文证明非对称 loss surface、偏心采样与有限 grid 会给 Approach 2 引入结构性偏差，并以直接 surface fit/variable projection 恢复五个参数的联合估计。",
        "noise-free synthetic、公开 Llama 3 IsoFLOP 数据和方法对比支持偏差方向与所报成本估计；美元换算仍依赖 MFU、价格和外推假设。",
        "直接拟合减少系统偏差，却对初始化、数值条件和实验设计要求更高；局部、近对称且只作插值时简化抛物线仍可作为廉价诊断。",
    ),
    "2603.22350": (
        "逐 action 的 deterministic gate 能清楚授权单步副作用，却看不到多个合规动作累积成的数据外泄轨迹。",
        "SRM 在 gate 外维护 session semantic centroid 与基线扣除后的 EMA risk，把历史状态交给确定性 pre-execution decision，而不是让 LLM 自报安全。",
        "80-session 多轮 benchmark 支持所测阈值下的 trajectory discrimination 与 false-positive 抑制；未证明 centroid 能覆盖语义伪装或长期分布漂移。",
        "跨 turn 状态提高检测面，也引入阈值校准、误拒和 session reset/poisoning 风险；真正无状态、低副作用调用仍可只用单步 gate。",
    ),
    "2603.22489": (
        "MCP 早期实现常把 server 注册、tool description 与执行授权视为同一信任边界，客户端因此会直接消费被污染的 capability metadata。",
        "论文用 STRIDE/DREAD 分解 host、client、LLM、server、data store 与 authorization server，再把注册校验、decision-path 检查、runtime monitoring 和用户透明度组成分层防线。",
        "五个客户端上的四类 tool-poisoning 演示能证明这些实现的具体暴露面；样本规模与版本有限，不能代表 MCP 协议或全部客户端的普遍漏洞率。",
        "分层检查降低单点失守，却增加兼容、延迟和策略维护成本；可信单 server 环境仍可采用更薄的 admission，但 execution authorization 不能省略。",
    ),
    "2603.22751": (
        "只分别审计 memory、retrieval 或 tool storage 会漏掉内部依赖如何经不同可观察输出被攻击者反演。",
        "CIPL 把目标属性、agent pipeline、可观察 channel 与 inversion attacker 统一成同一测量接口；privacy owner 从某个存储组件扩展为端到端 observable data flow。",
        "跨多类 agent pipeline 的实验支持该接口比较泄漏路径的能力；结果绑定攻击者观察权限、目标属性与 evaluator，不能给出通用隐私保证。",
        "channel-level 测量提高可比性，却需要枚举实际观察面且可能遗漏组合通道；隔离明确的单组件仍可先做局部测试，但不能据此宣称端到端安全。",
    ),
    "2603.22774": (
        "多 GPU serving 通常把慢吞吐归因于 GPU 算力或互联，默认 host CPU 只承担可忽略的调度工作。",
        "论文把 kernel launch、collective progress、tokenization 与 agentic host work 分解到 CPU allocation，显示 CPU 是维持 GPU feed 的控制面资源。",
        "多 GPU serving 配置下的 profiling 支持 CPU 配额不足会造成 launch delay、通信停顿与 GPU idle；具体幅度绑定模型、框架、CPU/GPU 拓扑和请求混合。",
        "增加 CPU 或隔离 host work 可恢复利用率，但提高成本并可能把瓶颈移到内存/互联；GPU 已饱和或 host path 很薄时继续加 CPU 无益。",
    ),
    "2603.22858": (
        "把 learned structural memory 与主模型共同训练最自然，因为表示和 memory address 可以共同适配任务。",
        "多轮 DPPN 实验暴露跨 run coordinate drift：persistent state 若依赖可旋转的 learned slot/embedding，transfer 时没有稳定身份；固定坐标只解决必要条件，仍需合适的写入与读出机制。",
        "五组实验、多个 seed 与 transfer target 支持 saturation、coordinate mismatch 和固定坐标的诊断；结果主要是受限架构上的正反例，不证明一种通用 memory 实现。",
        "固定坐标提高可对齐性，却限制表示适配并可能损失任务性能；单任务、不跨版本转移的 memory 仍可使用共同学习的坐标。",
    ),
    "2603.22868": (
        "静态 allowlist 适合已知工具图，但开放 agent 的实际 action path 由 prompt、tool result 与 runtime state 动态产生。",
        "Agent-Sentry 从合法执行学习 provenance-conditioned behavior bound，在 action 落界前检查其来源与轨迹，而不是只过滤最终文本。",
        "公开实验支持所测任务/攻击下对异常 action 的区分；学习到的 benign bound 不等同于授权真值，也未覆盖部署后的合法行为漂移。",
        "provenance bound 增加 runtime 检查与冷启动数据需求，且可能误拒新路径；静态、低变化 workflow 仍应优先显式 policy/allowlist。",
    ),
    "2603.22910": (
        "低秩 KV 压缩常把投影写进模型结构，部署后难以在显存充足时无损回到标准 full-cache 路径。",
        "EchoKV 保留 full-cache 语义，在压力出现时丢弃可重建分量并用轻量网络恢复，使 compression policy 成为 runtime 可切换状态。",
        "LongBench 与所测模型上的质量/内存结果支持按需切换；不能证明重建网络对其他架构、层或分布外长上下文稳定。",
        "可切换性减少永久架构绑定，却增加重建 compute、模型专属训练和切换一致性；容量充足、低延迟场景仍应保留完整 KV。",
    ),
    "2603.23049": (
        "RAG prefix KV reuse 能避免重复 prefill，但从缓存读取大前缀仍会落在请求关键路径并产生新的 I/O 等待。",
        "PCR 用 prefix tree 管理可复用身份，按层把 cache transfer 与 compute 重叠，并根据队列提前 prefetch；reuse owner 因而同时包含命中、传输与失效状态。",
        "RAG serving 实验支持所测命中分布下的 latency 降低；收益依赖文档复用、队列可预测性、cache 容量和互联带宽。",
        "prefetch 隐藏 I/O，却会浪费带宽、放大 stale cache 和公平性问题；低复用或突发 query 下按需 prefill 更简单。",
    ),
    "2603.23149": (
        "用视觉 world model 预演 action outcome 最直观，却在安全 steering 的每一步引入秒级生成延迟。",
        "DILLO 从 policy latent 与 planned action 蒸馏语言化 outcome predictor，并以 latent rejection sampling 在执行前筛掉高风险 proposal；它预测的是决策相关后果而非完整视觉世界。",
        "latent sufficiency 与 steering 实验支持所测 policy/task 上的 failure prevention 和 latency 优势；未证明语言摘要保留所有物理安全变量。",
        "压缩 outcome 提高实时性，却可能漏掉难以语言化的接触与几何细节；需要高保真模拟或分布外动作时视觉/物理模型仍必要。",
    ),
    "2603.23376": (
        "通用视频 likelihood 能生成逼真画面，却不会自动惩罚穿透、反重力或 action 与结果不一致。",
        "ABot-PhysWorld 组合 embodied 数据筛选、physics-aware caption、解耦 VLM discriminator 的 diffusion-DPO 与 action-map conditioning，把物理偏好和可控动作写入训练目标。",
        "Embodied-ZeroShot 与视频实验支持所测 manipulation clips 上的视觉、物理和动作一致性；VLM 判别与视频指标不能替代真实机器人闭环成功率。",
        "物理偏好提升约束一致性，却继承判别器偏差并增加数据/后训练成本；只追求开放域视频外观时通用生成模型仍更经济。",
    ),
    "2603.23528": (
        "prompt compression 常被默认视为 token 越少、能耗必然越低，但 provider 的执行路径和生成长度会改变端到端结果。",
        "论文在三个 API provider、五个 benchmark 与四档压缩率上分离质量、token 数和能耗 proxy，并用本地直接测量校准 proxy；evaluation owner 因而必须记录 provider 与压缩策略。",
        "28,421 次成功调用支持 provider-dependent 方向差异；云端能耗仍是 proxy，不能推断数据中心实际功耗或碳排。",
        "压缩可能减少输入成本，却增加摘要计算、输出长度或质量损失；短 prompt、强 prefix cache 或高质量敏感任务仍可不压缩。",
    ),
    "2603.23610": (
        "长任务只靠 transcript 重放环境，会把 UI 漂移、失败动作和多模态证据混进不可查询文本。",
        "Environment Maps 把屏幕录制与 execution trace 归并为 persistent graph，显式保存 entity、action、transition 与证据，让不同 agent 共享可更新的环境状态。",
        "长时软件 workflow 实验支持所测环境中的恢复与导航收益；图的正确性仍依赖抽取器和界面覆盖，不能视为环境真值。",
        "结构化地图减少重复探索，却引入 stale node、错误合并和权限继承；稳定、短任务仍可直接使用当前 observation。",
    ),
    "2603.23791": (
        "纯 cloud 语义防御能力强但暴露隐私并增加交互延迟，纯 edge 规则又难识别语义化 indirect injection。",
        "Cognitive Firewall 把 local visual sentinel、cloud deep planner 与 deterministic execution guard 分层：edge 先筛选，cloud 解释可疑内容，最终副作用仍由本地 policy commit。",
        "1,000 个 adversarial samples 支持所测攻击下 hybrid defense 优于 edge-only；模型、页面分布和网络条件限制外推。",
        "split defense 平衡语义能力和隐私，却引入 cloud availability、传输泄漏和跨层 disagreement；离线或高机密环境仍需纯本地 conservative guard。",
    ),
    "2603.23806": (
        "只验最终任务成功会漏掉错误路由、违规 tool call 和中途越权，因为这些程序性失败可能偶然得到正确结果。",
        "AgentPex 从 prompt/system instruction 抽取行为规则，再对完整 trace 的对话、决策与 tool event 做 rule-conditioned judgment，把 outcome 与 process evidence 分离。",
        "多类 agent trace 上的检测实验支持该审计路径；规则抽取和 judge 一致性仍受模型偏差影响，不能替代确定性 effect receipt。",
        "trace 级审计提高可诊断性，却增加存储、隐私和 judge 成本；短、确定性 workflow 仍可由显式状态机断言直接验证。",
    ),
    "2603.23914": (
        "VLM decode 若完整保存每个视觉/文本 token 的多头 KV，长图像序列会让 memory bandwidth 和容量先于算力成为瓶颈。",
        "AttentionPack 在 head 间压缩 KV，并按当前 attention 需要自适应解压，把压缩 rank 与 read path 变成逐层 runtime policy。",
        "多高分辨率/长上下文任务的质量、显存与 latency 实验支持所测 VLM 的折中；不证明相同 rank 适用于所有模态、层和硬件。",
        "attention-aware 解压节省容量，却增加 projection compute、metadata 和错误 rank 风险；视觉 token 少或 HBM 充足时完整 KV 更稳。",
    ),
    "2603.24060": (
        "冻结 VLA 在 OOD 扰动下只能重复当前 policy，既不积累失败证据，也无法解释应在何处介入。",
        "RoboHarness 在 policy 外维护正负 dual memory，以 retrieval 提供相似经验，再用 causal attribution 选择 intervention，而不修改基础权重。",
        "多类机器人扰动实验支持所测 frozen VLA 的 in-context robustness；收益依赖 memory quality 与 attribution，不能外推到未见 embodiment。",
        "外置 harness 可快速适配且可回滚，但增加 retrieval latency、memory poisoning 和错误干预；分布稳定、可重训场景仍可直接 fine-tune policy。",
    ),
    "2603.24124": (
        "多次采样的语义分歧常被当作不确定性，但 alignment 会把表达压成同一簇，使一致性不再代表知道。",
        "论文通过 base→SFT→DPO stage ablation 分离 response homogenization，并比较 semantic clustering 与 token entropy；uncertainty owner 必须记录训练阶段和信号来源。",
        "TruthfulQA、GSM8K 及多次采样结果支持 homogenization 会让 sampling-based score 失效；任务差异说明 token entropy 也不是普适置信度。",
        "更底层 entropy 保留部分信号，却可能反映措辞而非事实正确性；高风险回答仍需外部 evidence、calibration 和 abstention。",
    ),
    "2603.24203": (
        "固定模板或白盒优化的 MCP indirect injection 易被防御器识别，不能代表攻击者在黑盒 tool-response 通道中的适应能力。",
        "TIP 用 tree search 维护 payload 分支，结合 path feedback、tool-response simulation、defense-aware mutation 与 prune/early-stop，逐步寻找可执行且隐蔽的注入。",
        "多模型、场景、防御和真实 MCP case study 支持所测 search 的攻击成功与迁移；它不证明所有 tool client 均可被同样利用。",
        "自适应 search 提高覆盖也提高攻击查询成本，防御侧仍需 capability admission、response provenance 与 effect-time authorization，而不能只训练文本分类器。",
    ),
    "2603.24595": (
        "模型和 CUDA kernel 独立演进时，tensor shape、buffer extent 与 launch configuration 的隐式约定会变成难复现的 memory bug。",
        "M2K 用 HFProbe 无 GPU 跟踪模型，区分固定/用户可变参数并生成接口约束；cuKLEE 再在这些约束下符号执行 kernel，把 model-kernel contract 变成可检查 artifact。",
        "真实 LLM inference kernel 上发现 181 个未知 bug、9 个 false positive，支持该接口化验证；覆盖仍受 symbolic model 与 kernel feature 支持限制。",
        "显式约束提高 release safety，却增加 tracing、模型版本绑定和 solver 成本；简单静态 shape kernel 仍可用单元/边界测试。",
    ),
    "2603.24755": (
        "single-shot coding benchmark 会奖励眼前通过测试的 patch，却看不到架构决定如何侵蚀后续迭代。",
        "SlopCodeBench 让同一 agent 连续扩展自己先前的实现，并在 196 checkpoints 分开测 correctness、structural erosion 与 verbosity。",
        "36 个问题、15 个 agent 与开源仓库对照支持 agent code 会随迭代累积退化；任务语言、metric 与 checkpoint 设计限制泛化。",
        "长程 benchmark 更接近维护，却昂贵且指标可能偏好特定结构；局部 bugfix 仍可保留 single-shot 测试，但不能代表可维护性。",
    ),
    "2603.24775": (
        "MCP/A2A 能传 tool call 与 delegation，却未把调用者身份、可衰减权限和 completion provenance 绑定成同一可验证链。",
        "AIP 的 IBCT 把 compact signed JWT 与多跳 Biscuit/Datalog chain 分开，holder 只能收窄权限，并把 invocation context 绑定到 completion record。",
        "跨 Python/Rust、真实 MCP/A2A 与 600 次攻击评估支持所测拒绝率和低开销；不覆盖密钥泄漏、撤销传播或所有 transport。",
        "可验证 delegation 增加 key lifecycle、clock/revocation 和 policy complexity；单 hop、同一信任域仍可用较简单 token，但匿名调用不应进入高权限链。",
    ),
    "2603.24963": (
        "每个推荐模型独立定制能贴合局部目标，却让同一训练/serving 技术在大模型生态中以乘法成本传播。",
        "SMT 把可组合模型部件与适配点标准化，使 technique 与 model family 的演进从逐对维护转成模板 lineage 与受控 specialization。",
        "Meta 广告系统四个开发周期支持所测生态的工程时间、adoption throughput 与 neutral-capacity 指标；组织、模型族和生产数据不可直接外推。",
        "模板降低传播成本却可能压平真正需要专用结构的目标，并形成中心模板 blast radius；少量高异质模型仍可独立优化。",
    ),
    "2603.25056": (
        "把 system prompt 当作安全策略最便宜，但 prompt 中某个高相关启发式一旦被攻击者反转，模型会忠实执行错误假设。",
        "PhishNChips 系统扫描 model×prompt configuration，追踪 response reasoning，并用 Safetility 同时计入 recall 与 false-positive cost，把 prompt 版本变成安全评估对象。",
        "11 个模型、10 种策略与 phishing/legitimate 集合支持配置可让同一模型跨越巨大 bypass 区间；数据分布和邮件域限制结论。",
        "更具体 prompt 可提升平均检测又制造单信号脆弱性；需要外部 ground truth、ensemble 与 tool verification，不能把 prompt 固化为 reference monitor。",
    ),
    "2603.25158": (
        "人工编写 skill 难扩展，单条 trajectory 直接记忆又会把偶然步骤和局部错误固化成程序。",
        "Trace2Skill 并行归纳多条 execution trajectory，把反复出现的 failure/workaround 压缩为统一 skill directory，并在模型/任务间验证 transfer。",
        "office、math、vision QA 及跨模型实验支持部分 skill 可迁移；高增益案例不证明所有归纳规则都正确或安全。",
        "经验蒸馏减少重复探索，却引入错误归纳、适用域漂移与供应链风险；稀有高风险操作仍需人工规则和 held-out gate。",
    ),
    "2603.25685": (
        "robot world model 用真实历史 teacher forcing 训练时，部署却消费自身预测，autoregressive rollout 因分布漂移快速崩坏。",
        "论文在模型自己的 rollout state 上做 diffusion RL，用同一状态的多个可变长 future 和多视角 fidelity reward 形成相对更新。",
        "DROID 上的图像指标、pairwise 与人评支持所测 rollout 稳定性；视觉 fidelity reward 不证明动作因果或真实任务成功。",
        "on-rollout post-training 缓解 compounding error，却增加生成成本并可能 reward hack；短 horizon 或有可靠 simulator 时监督训练仍更简单。",
    ),
    "2603.25702": (
        "block diffusion 在少 denoising step 时阈值激进会损伤质量，保守又失去并行加速。",
        "S2D2 让同一 block-diffusion 模型以 block-size=1 充当 AR verifier，并用轻量 router 只在值得时验证 diffusion proposal。",
        "三个模型 family 的 accuracy-speed 实验支持所测配置优于阈值 baseline；收益绑定 router、接受率和 block schedule。",
        "self-verification 无需第二模型，却增加 mode switch、rollback 与重复 compute；小 batch 或低接受率时普通 AR/diffusion decode 仍更稳。",
    ),
    "2603.25716": (
        "只保存静态背景的 video memory 无法解释动态主体离开视野后继续运动并重新出现。",
        "HyDRA 把 static archive 与 dynamic subject track 分开，以压缩 memory token 和时空相关检索维持 hidden subject 的 identity/motion。",
        "HM-World 59K clips 与对比实验支持 exit-entry 场景的一致性收益；数据集和生成指标不能证明开放世界 object permanence。",
        "hybrid memory 改善动态连续性，却增加 entity association、stale motion 和 retrieval error；无遮挡短视频仍可用局部 context。",
    ),
    "2603.25764": (
        "coding agent 的 submit/completion rate 容易把主动提交当成功，重复给出同一错误 patch 甚至会伪装成稳定性。",
        "论文把 repeated-run submit、test-verified resolve、silent semantic failure 与应当 abstain 的 already-fixed probe 分离，使行动欲望不再拥有 correctness 真值。",
        "1,750 条 SWE-bench Verified trajectory 支持所测模型存在稳定而不可见的语义失败；它不覆盖其他代码库、工具链或更强 verifier。",
        "重复验证和 abstention 指标提高可信度，却增加执行成本且仍受测试完备性限制；低风险草稿任务可保留 completion 作为运营指标，但不能作为 release gate。",
    ),
    "2603.25973": (
        "million-token context 并不等于 agent 会在多年、跨域历史中正确保留用户偏好，短对话合成 benchmark 难暴露 interference。",
        "MemoryCD 从真实长期行为构建跨域 memory source，并分开 rating、ranking、summary、generation 任务及 long-context/外部 memory 方法。",
        "14 个模型和多种 memory method 的单域/跨域实验支持所测方法存在 transfer 与干扰差异；Amazon review 行为不是所有个性化场景的真值。",
        "真实长程 benchmark 提高生态有效性，却继承选择偏差、时间泄漏和 judge 偏差；短会话 memory 仍需更窄、可控的单元测试。",
    ),
    "2603.25981": (
        "纯 reactive policy 缺少长 horizon 规划，纯 world-model search 又会在高维 action space 中从差初值开始浪费 rollout。",
        "PiJEPA 用训练后的 Octo policy 提供 action prior，再由 JEPA latent dynamics 与 MPPI 对候选轨迹打分；policy 负责 proposal，world model 负责可达性比较。",
        "CAST navigation 上不同 encoder、baseline、位置/朝向与 latency 结果支持所测组合；不能证明 latent score 与真实环境因果完全一致。",
        "policy prior 降低搜索成本却继承 policy blind spot，world model 又可能误排 OOD action；短反应任务仍可直接 policy，强探索任务仍需更广 search。",
    ),
    "2603.26074": (
        "RAG 知识库若对所有敏感实体做同强度匿名化，会牺牲检索和回答 utility；只屏蔽显式 PII 又忽略上下文可重构风险。",
        "TRIP-RAG 先按上下文量化 entity risk，再动态选择 generalization level，并给出语义安全/不可重构分析；privacy policy 在 retrieval 前拥有变换与映射状态。",
        "多数据集 utility、privacy attack 与 ablation 支持所测阈值的折中；形式证明依赖威胁模型，不能覆盖外部背景知识或所有 linkage attack。",
        "动态匿名化保留更多 utility，却增加 risk estimator、mapping governance 与误分级；法规要求删除或极高风险字段仍应确定性移除。",
    ),
    "2603.26498": (
        "text-only scheduler 把 request cost 近似为 token 数，会让 video/image preprocessing 与 encoder 阶段造成严重 head-of-line blocking。",
        "TCM-Serve 建立 modality-aware resource abstraction，并在 preprocessing、encoding、prefill/decode 间按异质需求排序与并发，显式拥有阶段资源状态。",
        "多模态请求混合下的 latency/throughput 实验支持所测 scheduler；收益依赖视频长度、encoder、GPU 和 arrival distribution。",
        "精细分类减少大请求垄断，却增加预测误差、starvation 与跨阶段协调；同质文本 workload 仍可用现有 continuous batching。",
    ),
    "2603.26557": (
        "每次重复或近重复问题都调用强模型，能保持简单语义，却在跨用户会话中重复支付同一推理成本。",
        "MemBoost 把历史 answer 与supporting information 组织为可更新 memory，轻模型先判断复用/回答，困难或低置信 query 才升级强模型。",
        "交互 workload 的成本与质量实验支持所测 escalation policy；历史答案正确性、隐私和 drift 依赖数据与 verifier，不能把 cache hit 当真值。",
        "复用降低成本，却引入 stale answer、跨租户泄漏和错误自强化；高新鲜度或高风险 query 应绕过 memory 并重新 grounding。",
    ),
    "2603.26666": (
        "offline VLA SFT 样本高效但遭遇 deployment distribution shift，纯 online RL 又受 sparse reward 与 rollout 成本限制。",
        "VLA-OPD 在当前 policy rollout 上用 expert action 形成 dense distillation target，把 on-policy state coverage 与监督更新结合，而非等待稀疏终局奖励。",
        "机器人 manipulation 实验支持所测任务的 sample efficiency 与 capability retention；expert quality、sim/real 环境和安全覆盖限制外推。",
        "on-policy distillation 改善状态匹配，却需要可靠 expert 并可能复制其偏差；有密集真实 reward 时 RL、分布稳定时 offline SFT 仍更直接。",
    ),
    "2603.26728": (
        "LLM gateway 若把质量、成本、延迟和 issue label 分散在日志与离线表中，routing decision 无法追溯同一 evaluation contract。",
        "SEAR 定义跨 context、intent、response issue、quality 与 operational metrics 的 typed relational schema，并以一致性 link 支撑 evaluator 与 router 共享证据。",
        "论文展示 schema population 与多 provider routing 案例，能证明数据契约的可查询性；不证明约百列 schema 或自动 evaluator 在所有业务上都校准。",
        "统一 schema 提高 lineage，却带来字段维护、迟到数据和 evaluator coupling；单 provider、单指标服务仍可使用较薄 telemetry。",
    ),
    "2603.26942": (
        "只看最终视觉输出给 human feedback，会让 coding agent 无法区分几何推理错、工具程序错还是执行状态错。",
        "earned-autonomy 实验让 agent 从零构建函数库，并对比 output-only feedback 与可观察中间 action/trace；核心增量是把过程状态暴露给 verifier，而非增加模型调用。",
        "Blender 3D scene 任务中重发现 utility 但 0% full-scene success，支持输出反馈不足的诊断；单一环境不能证明所有 coding agent 都需要同样 trace。",
        "过程 observability 提高归因，却扩大日志隐私、反馈负担与可被迎合的表面；可由 deterministic tests 完整验收的短任务仍可少暴露内部 trace。",
    ),
    "2603.26993": (
        "增加 agent 和消息 hop 常被假定能自动提升规划可靠性，即使所有 agent 只重复同一模型和共同证据。",
        "论文把多 agent DAG 形式化为有限 delegated decision network，证明在没有新 exogenous signal 时它受同信息的 centralized Bayes decision maker 支配。",
        "理论结果与数值例子支持 common-evidence 边界；它不否定工具、独立传感器、异构模型或人审带来新信息的系统。",
        "集中决策减少 coordination tax，却可能成为容量与信任单点；多 agent 应以新增信息、并行执行或隔离责任为理由，而不是数量本身。",
    ),
    "2603.27116": (
        "semantic vector memory 用邻近性实现概念泛化，通常把误召回和遗忘当作可继续调参消除的实现缺陷。",
        "论文在有限局部维度的 continuous kernel-threshold memory 类中证明：提高语义连续性会不可避免地扩大 interference/false recall，容量与可分性不能同时无限提升。",
        "形式定理与 forgetting experiments 支持该模型类内的下界；不覆盖 symbolic key、外部 provenance filter 或混合 exact/semantic memory。",
        "语义 memory 获得类比与柔性检索，却必须接受干扰并配合 exact archive、namespace 与 verification；身份关键事实仍应使用显式 key。",
    ),
    "2603.27138": (
        "KV offload 若等 GPU 请求后才从 CPU 搬运或计算，会把 PCIe/CPU 等待直接暴露在 decode critical path。",
        "ScoutAttention 让 CPU 提前一层计算候选 attention，并把结果/状态与 GPU layer pipeline 重叠；offload owner 因而包含 layer-ahead schedule 和一致性。",
        "长上下文模型上的 batch、latency 与 GPU utilization 实验支持所测 CPU/GPU 平衡；结果绑定主机核数、内存带宽、PCIe 与层结构。",
        "预计算隐藏等待，却可能因 CPU 落后、错误预测或同步产生浪费；KV 可驻 HBM 或 CPU 很弱时普通 GPU attention 更好。",
    ),
    "2603.27204": (
        "agent skill 同时含自然语言、代码和配置，单独静态扫描或 LLM 判断都看不到跨 artifact 的恶意意图与副作用。",
        "MalSkills 先抽取符号 facts，再让神经模型在上下文中推理并用规则约束结论，把 registry admission 建立在多 artifact evidence graph 上。",
        "公开 skill corpus 与攻击样本的检测实验支持组合方法；覆盖依赖规则、sandbox 和标签，不能证明未知语言/运行时无恶意行为。",
        "neuro-symbolic 检查提高可解释性，却增加规则维护、动态执行成本与 false positive；可信内部 skill 仍应配合签名和最小权限。",
    ),
    "2603.27287": (
        "先生成完整未来视频再规划会让 imagination 与 action decision 脱节，早期预测误差在开环 rollout 中持续累积。",
        "Uni-World VLA 交替生成 future frame 与 ego trajectory，让每一步 action 重新条件化下一段 world state；world prediction 与 planning 共享可修订状态。",
        "自动驾驶 benchmark 支持所测模型在预测/规划指标上的联合收益；生成帧质量与闭环道路安全仍不是同一证据。",
        "交错闭环减少漂移，却增加推理延迟、状态 commit 与错误耦合；低延迟 reactive control 或高保真 simulator 仍可能分层部署。",
    ),
    "2603.27355": (
        "离线平均分、线上 telemetry 与 CI 发布通常分属不同工具，任何一个单独通过都不足以说明 LLM/RAG workload ready。",
        "readiness harness 以统一 scenario schema 聚合 workflow success、policy、groundedness、retrieval、cost 与 p95 latency，并用 Pareto frontier 形成 release gate。",
        "ticket routing、BEIR 与 Azure matrix 支持该 harness 的可复现组合判断；权重和阈值是案例配置，不是通用生产标准。",
        "统一 gate 提高发布可追溯性，却可能被错误权重或 evaluator drift 绑架；窄服务仍可使用更少指标，但必须保留独立回滚条件。",
    ),
    "2603.27467": (
        "固定逐元素 KV quantization 忽略旋转后成对向量近似落在单位圆的结构，也常把所有层分配同一 bit budget。",
        "TurboAngle 在 Walsh-Hadamard 域量化角度，并按层分别提高 K/V codebook precision，把 bit allocation 变成模型层级策略。",
        "七个 1B–7B 模型的质量与 bit-rate 实验支持所测压缩范围；一个模型未达 near-lossless，且 kernel/硬件 SLO 未充分证明。",
        "角度编码降低 footprint，却增加旋转、norm metadata 和模型校准；未支持 kernel 或需严格 exactness 时更高精度 KV 仍合理。",
    ),
    "2603.27517": (
        "agent runtime 把 shell、filesystem、browser、plugin 与 messaging 接到模型后，传统按 CVE 组件计数无法说明 trust violation 穿过哪一执行层。",
        "论文把 470 条 OpenClaw advisory 按 system layer 与 attack technique 双轴归类，并据此比较 exec policy、gateway、channel、sandbox 与 prompt 的防线责任。",
        "公开 advisory taxonomy 能证明该版本生态的缺陷分布；披露偏差、重复 advisory 和快速版本演进禁止外推为所有 agent framework 风险率。",
        "双轴分类改善 threat-model coverage，却仍是事后样本；生产系统需要 capability inventory、effect-time authorization 与可验证 patch lineage。",
    ),
    "2603.27624": (
        "低 batch edge MoE 不能把全部 expert 放入片上内存，传统 offload 又在动态 gate 下产生细粒度传输和负载失衡。",
        "Expert Streaming 在多 chiplet 共享 expert shard，并按预测的 expert trajectory 动态调度传输/执行，把 gate path、placement 与 interconnect schedule 联合优化。",
        "架构模拟/实验支持所测模型与 chiplet 参数的 latency/energy 改善；结论依赖 die-to-die 带宽、gate 分布和低 batch 假设。",
        "细粒度 streaming 减少 off-chip 等待，却增加预测错误、跨 chiplet 同步和硬件专用性；大 batch 数据中心仍可用常规 expert parallel。",
    ),
    "2603.27819": (
        "KV sequence compression 从 eviction 到 merging 都被原始 cache entry 约束，保留对象未必是最适合未来 query 的表示。",
        "KVSculpt 把压缩视为 distillation，直接优化一组更小、非原条目约束的连续 KV，使 future-query output 成为训练目标。",
        "所测模型/任务的质量-长度实验支持 learned synthetic KV 优于若干 eviction/merge baseline；优化查询分布与 offline 成本限制在线泛化。",
        "distilled KV 提高单位 slot 信息量，却可能过拟合未来 query、缺少可解释 token identity；动态未知 workload 仍可优先 eviction/merge。",
    ),
    "2603.28013": (
        "prompt injection 只报最终成功/失败，会把暴露、持久化、跨 agent relay 与真正执行混成一个二值结果。",
        "kill-chain canary 用加密 token 追踪 EXPOSED→PERSISTED→RELAYED→EXECUTED 四阶段，跨 attack surface 和 defense tier 定位防线在哪一 hop 失效。",
        "950 runs、五个模型、六类 surface 与五种 defense 支持所测 pipeline 的阶段差异；canary 可见性和场景集合不等于所有真实攻击。",
        "阶段 telemetry 提高诊断，却引入追踪状态、隐私和 canary 被识别的风险；单模型无持久状态系统仍可用更简单 outcome test。",
    ),
    "2603.28101": (
        "agentic RL rollout 按 step 排队时忽略 trajectory 的 tool-wait 与长尾上下文，造成 queueing、interference 和 inflated per-token time。",
        "Heddle 以 trajectory 为调度对象，联合决定何时继续、放到哪里以及如何组织 tool/LLM execution，使 rollout context 成为显式 runtime state。",
        "分布式 agentic RL workload 的 throughput/尾延迟实验支持所测系统；结果绑定工具延迟、模型、cluster 和训练同步策略。",
        "trajectory-aware orchestration 减少长尾，却增加 state migration、fairness 和 stale-policy 管理；同步、短 rollout 仍可使用 step-centric pipeline。",
    ),
    "2603.28239": (
        "tensor parallel inference 的 All-Reduce 在关键路径上频繁同步，GPU 发起的细粒度 in-network 操作会重复占用 switch/GPU 控制。",
        "论文把 collective schedule 移到 switch-centric controller，由网络侧聚合 shared-memory operation，而不是每个 GPU 逐元素驱动。",
        "架构评估支持所测 topology/message size 的 latency 与利用率收益；尚不能证明真实交换芯片、故障和多租户隔离下同样成立。",
        "网络拥有更多控制可减少 GPU 开销，却增加可编程 switch 状态、故障域和部署专用性；小规模或标准 collective 已足够时普通 NCCL 更可移植。",
    ),
    "2603.28565": (
        "VLA 把 observation、action generation 与 execution 串行化时，robot 会在每轮推理等待，吞吐提升也不一定满足连续控制。",
        "StreamingVLA 用 action flow matching 流式生成 chunk，并按当前状态提前触发下一 observation，使感知与执行重叠且保持可取消的更新。",
        "机器人任务的控制流畅度、latency 与 success 实验支持所测平台；不能外推到更高频控制、不同传感器或安全关键动作。",
        "streaming 降低停顿，却引入 observation staleness、chunk cancellation 与并发状态一致性；慢速或高精度动作仍可保持串行 observe-plan-act。",
    ),
}


BOOKS_EXISTING = {
    "WORLDVIEW-SCALING-LAW": ("为什么还需要 Scaling Law", "现稿已把 scaling law 定义为带模型族、数据、训练配方与硬件边界的规划工具，而不是无条件外推公式。"),
    "MODEL-SELF-ATTENTION": ("它付出了什么", "现稿已说明 dense self-attention 用二次 token 交互换取输入依赖的信息流，并把 FlashAttention 与模型语义分层。"),
    "MULTIMODAL-WORLD-MODELS": ("Open-loop imagination vs closed-loop correction", "现稿已区分画面生成、action-conditioned transition、persistent state 与可规划性，并要求 imagined rollout 经过校准。"),
    "MULTIMODAL-EMBODIED-VLA": ("Latency 与 control frequency", "现稿已把 observation、action chunk、control deadline 与 safety authority 分开，并保留快慢控制共存边界。"),
    "TRAIN-RLHF": ("不确定性不能只从采样分歧读取", "现稿已区分 preference/alignment 更新与事实置信度，并要求外部证据和校准承担最终判断。"),
    "TRAIN-GRPO": ("Rollout 是带版本的训练状态", "现稿已把 trajectory、tool wait、policy freshness 与训练更新视为同一 rollout contract。"),
    "INFER-REQUEST-LIFECYCLE": ("一次请求不是一次前向", "现稿已把请求拆为 admission、prefill、decode、state commit 与 fallback，并要求阶段成本可归属。"),
    "INFER-DECODE": ("Decode 的状态所有权", "现稿已把逐 token state、attention read 与提交顺序置于 decode critical path。"),
    "INFER-KV-CACHE": ("KV Cache 是带身份的运行时状态", "现稿已区分逻辑 KV 身份、物理布局、压缩/迁移与失效，完整 KV 是容量允许时的 exact baseline。"),
    "INFER-SPECULATIVE-DECODING": ("Speculation 不是 free speedup", "现稿已要求 draft、verify、accept 与 rollback 共享版本化状态，收益受接受率和验证成本约束。"),
    "INFER-TENSORRT-LLM": ("Execution Plan 可以修订，但只能在安全边界 Commit", "现稿已把 kernel、precision、layout、collective 与 backend 选择纳入可验证 execution plan。"),
    "INFER-GPU-MEMORY": ("Memory Hierarchy 与状态迁移", "现稿已把 HBM/DRAM/offload 的状态身份、传输、预取与回收放在同一容量—延迟合同中。"),
    "INFER-SCHEDULING": ("调度的是阶段、状态与 SLO", "现稿已说明 scheduler 不能只按 token 数或 FIFO，而要显式拥有资源预测、公平性与 state locality。"),
    "PLATFORM-FOUNDATIONS": ("平台控制对象必须类型化", "现稿已把 asset、workload、service 和 controller 作为可版本化平台对象，而不是每模型一套脚本。"),
    "PLATFORM-GATEWAY": ("Gateway 是策略执行面", "现稿已把能力、成本、延迟、隐私与 fallback 写成可追溯 routing contract。"),
    "PLATFORM-EVALUATION-SYSTEM": ("Evaluation Contract 决定分数能否比较", "现稿已要求 workload、样本、evaluator、重复运行与 release decision 共享证据 lineage。"),
    "PLATFORM-TRACE": ("Trace 必须恢复因果链", "现稿已区分 output、intermediate state、tool effect 与跨 agent propagation，日志本身不能等同语义证据。"),
    "PLATFORM-SECURITY": ("Canonical Action 与 Effect-time Authorization", "现稿已把 prompt、tool、memory、identity 与 side effect 放入同一授权链，模型判断只能是 sensor/proposal。"),
    "PLATFORM-PRODUCTION": ("Readiness Gates", "现稿已把离线评估、可观测性、SLO、progressive delivery 与 rollback 组合为发布证明责任。"),
    "AGENT-RAG": ("Retrieval Object 需要 Validity 与 Lifecycle", "现稿已把 query、index、retrieved evidence、cache、tenant filter 与 freshness 分开治理。"),
    "AGENT-MEMORY": ("Persistent Memory 需要显式状态操作，而不只是 Record", "现稿已区分 write/admission、semantic retrieval、exact archive、forgetting、provenance 与 rollback。"),
    "AGENT-MULTI-AGENT": ("扩展 Agent 数量之前，先测量 Coordination Tax", "现稿已要求多 agent 证明新增信息或并行价值，并把消息、共享状态、identity 与 commit 分开。"),
    "AGENT-MCP": ("MCP 不等于 Tool Authorization", "现稿已区分 protocol capability discovery、server admission、调用授权、信息流与 execution effect。"),
    "AGENT-PLATFORM": ("从 Trajectory 到 Skill 是一次受治理的 Compilation", "现稿已把 skill identity、来源轨迹、适用域、admission、版本和 retirement 纳入平台生命周期。"),
}


BOOKS_SECTION_BY_PATH = {
    "books/part-01-worldview/07-scaling-law.md": "为什么还需要 Scaling Law",
    "books/part-02-model/14-self-attention.md": "它付出了什么",
    "books/part-03-multimodal-world-models/25-multimodal-world-models.md": "Open-loop imagination vs closed-loop correction",
    "books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md": "Latency 与 control frequency",
    "books/part-04-training-system/31-rlhf.md": "不确定性不能只从采样分歧读取",
    "books/part-04-training-system/33-grpo.md": "Rollout 是带版本的训练状态",
    "books/part-05-inference-system/42-what-happens-during-inference.md": "一次请求不是一次前向",
    "books/part-05-inference-system/44-decode.md": "Decode 的状态所有权",
    "books/part-05-inference-system/45-why-kv-cache-speeds-up.md": "KV Cache 是带身份的运行时状态",
    "books/part-05-inference-system/48-speculative-decoding.md": "Speculation 不是 free speedup",
    "books/part-05-inference-system/49-tensorrt-llm.md": "Execution Plan 可以修订，但只能在安全边界 Commit",
    "books/part-05-inference-system/54-gpu-memory.md": "Memory Hierarchy 与状态迁移",
    "books/part-05-inference-system/56-inference-scheduling.md": "调度的是阶段、状态与 SLO",
    "books/part-06-ai-infrastructure/57-what-is-ai-platform.md": "平台控制对象必须类型化",
    "books/part-06-ai-infrastructure/62-gateway.md": "Gateway 是策略执行面",
    "books/part-06-ai-infrastructure/66-evaluation-system.md": "Evaluation Contract 决定分数能否比较",
    "books/part-06-ai-infrastructure/69-trace.md": "Trace 必须恢复因果链",
    "books/part-06-ai-infrastructure/72-security.md": "Canonical Action 与 Effect-time Authorization",
    "books/part-06-ai-infrastructure/73-production-best-practice.md": "Readiness Gates",
    "books/part-07-agent/76-rag.md": "Retrieval Object 需要 Validity 与 Lifecycle",
    "books/part-07-agent/77-memory.md": "Persistent Memory 需要显式状态操作，而不只是 Record",
    "books/part-07-agent/82-multi-agent.md": "扩展 Agent 数量之前，先测量 Coordination Tax",
    "books/part-07-agent/83-mcp.md": "MCP 不等于 Tool Authorization",
    "books/part-07-agent/84-agent-platform.md": "从 Trajectory 到 Skill 是一次受治理的 Compilation",
}


def explicit_nodes() -> dict[str, str]:
    allowed = {aid for ids in SELECTED.values() for aid in ids}
    result: dict[str, str] = {}
    for node, suffixes in GROUPS.items():
        for suffix in suffixes.split():
            aid = f"2603.{suffix}"
            if aid in result and result[aid] != node:
                raise ValueError(f"duplicate Stable Node route for {aid}: {result[aid]} vs {node}")
            if aid in allowed:
                result[aid] = node
    return result


def roadmap_paths() -> dict[str, str]:
    text = (base.ROOT / "ROADMAP.md").read_text()
    return dict(re.findall(r"\| `([^`]+)` \| Ch\d+ \| `([^`]+)` \|", text))


def existing_review_cache() -> dict[str, dict]:
    cache: dict[str, dict] = {}
    for day in range(25, 32):
        packet = base.ROOT / f"papers/2026/03/_sources/daily-202603{day:02d}/exact-v1-review-packet.json"
        if not packet.exists():
            continue
        for item in json.loads(packet.read_text()).get("items", []):
            cache[item["primary_identifier"]] = item
    return cache


def local_sections(path: Path) -> dict[str, list[str]]:
    if path.suffix == ".html":
        parser = base.SectionParser()
        parser.feed(path.read_text(errors="ignore"))
        return parser.sections
    text = path.read_text(errors="ignore")
    # pdftotext output keeps numbered headings sufficiently well for exact
    # local section recovery.  Content before the first heading is Abstract.
    headings = list(re.finditer(r"(?m)^\s*((?:\d+\.)*\d+)\.?\s+([A-Z][^\n]{2,100})\s*$", text))
    sections: dict[str, list[str]] = {"Abstract": []}
    if headings:
        abstract = base.clean(text[: headings[0].start()])
        if abstract:
            sections["Abstract"].append(abstract)
        for index, match in enumerate(headings):
            end = headings[index + 1].start() if index + 1 < len(headings) else len(text)
            title = base.clean(f"{match.group(1)} {match.group(2)}")
            body = base.clean(text[match.end():end])
            if body:
                sections[title] = [body]
    else:
        chunks = [base.clean(part) for part in re.split(r"\n\s*\n", text) if len(base.clean(part)) > 120]
        sections["PDF Full Text"] = chunks
    return sections


def repair_saved_full_text(review: dict) -> dict:
    path = base.ROOT / review["body_path"]
    if not path.exists() or path.stat().st_size < 1000:
        return review
    sections = local_sections(path)
    paper_title = review["title"]
    aid = review["primary_identifier"].split(":", 1)[1].removesuffix("v1")
    overrides = base.SECTION_OVERRIDES.get(aid, {})
    method_title, method_evidence = base.choose_section(
        sections, "method", paper_title, "Method", overrides.get("method"),
    )
    eval_title, eval_evidence = base.choose_section(
        sections, "evaluation", paper_title, "Evaluation", overrides.get("evaluation"),
    )
    limit_title, limit_evidence = base.choose_section(
        sections, "limitations", paper_title, "Limitations", overrides.get("limitations"),
    )
    kind = "HTML" if path.suffix == ".html" else "PDF"
    url = f"https://arxiv.org/{'html' if kind == 'HTML' else 'pdf'}/{aid}v1"
    suffix = f"{kind} — §{{title}} [facet={{facet}}]; {url}; {review['body_path']}; sha256:{base.sha(path)}"
    missing = {
        "method": method_evidence.startswith("Not Disclosed"),
        "evaluation": eval_evidence.startswith("Not Disclosed"),
        "limitations": limit_evidence.startswith("Not Disclosed"),
    }
    def loc(title: str, evidence: str, facet: str) -> str:
        if evidence.startswith("Not Disclosed"):
            return f"Not Disclosed — exact-v1 {kind} lacks a role-specific {facet} section; {url}; {review['body_path']}; sha256:{base.sha(path)}"
        return suffix.format(title=title, facet=facet)
    review.update(
        method_evidence_excerpt=method_evidence,
        evaluation_evidence_excerpt=eval_evidence,
        limitations_evidence_excerpt=limit_evidence,
        method_locator=loc(method_title, method_evidence, "method"),
        evaluation_locator=loc(eval_title, eval_evidence, "evaluation"),
        limitations_locator=loc(limit_title, limit_evidence, "limitations"),
        claim_boundary=(
            f"只支持 arXiv:{aid}v1 §{method_title} 的机制与 §{eval_title} 的公开 workload；"
            f"§{limit_title} 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。"
        ),
        access_status="accessible" if not any(missing.values()) else "review_pending_missing_role_locator",
        result="complete" if not any(missing.values()) else "blocked",
        missing_review_roles=[role for role, value in missing.items() if value],
    )
    return review


def main() -> None:
    base.SELECTED = SELECTED
    base.DURABLE_CANDIDATES = {aid for ids in SELECTED.values() for aid in ids}
    base.INTEGRATE_SUGGESTIONS = INTEGRATE
    base.NODE_OVERRIDES = explicit_nodes()
    base.NODE_PATH.update(roadmap_paths())
    base.PAPER_SYNTHESIS.update(PAPER_SYNTHESIS)
    base.DISPOSITION_OVERRIDES.update({
        aid: ("Integrate" if aid in INTEGRATE else "No Change — Existing Coverage")
        for ids in SELECTED.values() for aid in ids
    })
    base.SECTION_OVERRIDES.update({
        "2603.22300": {"method": [r"^3\s+sparse feature attention$"], "evaluation": [r"^4\.3\s+benchmarking"], "limitations": [r"^7\s+conclusion and limitations$"]},
        "2603.22339": {"method": [r"^8\.2\s+variable projection"], "evaluation": [r"^8\.3\s+method comparison"], "limitations": [r"^9\.1\s+limitations$"]},
        "2603.22350": {"method": [r"^3\.2\s+session behavioral centroid", r"^3\.4\s+risk accumulation"], "evaluation": [r"^5\.2\s+evaluation protocol", r"^5\.3\s+results"], "limitations": [r"^6\.3\s+limitations$"]},
        "2603.22489": {"method": [r"^4\.\s+tool poisoning architecture", r"^4\.2\.\s+secure mcp client"], "evaluation": [r"^5\.2\.\s+testing procedure", r"^6\.1\.\s+attack matrix"], "limitations": [r"^7\.4\.\s+threats to validity"]},
        "2603.22774": {"method": [r"^v\s+understanding the cpu bottlenecks"], "evaluation": [r"^iv\s+cpu bottleneck", r"^iii\s+multi-gpu system evaluation"], "limitations": [r"^vi-c\s+limitations$"]},
        "2603.22858": {"method": [r"^3\s+architecture", r"^10\.2\s+the coordinate system problem"], "evaluation": [r"^7\.5\s+results: aligned distillation", r"^9\.2\s+results$"], "limitations": [r"^10\s+the convergent diagnosis", r"^13\s+implications"]},
        "2603.22910": {"method": [r"^3\.1\s+overview of echokv"], "evaluation": [r"^4\.2\s+main results"], "limitations": [r"^6\s+conclusion$"]},
        "2603.23049": {"method": [r"^4\.\s+system design$", r"^4\.1\.\s+system overview"], "evaluation": [r"^6\.1\.\s+experimental methodology"], "limitations": [r"^8\.\s+conclusion$"]},
        "2603.23149": {"method": [r"^3\s+distilled language action world model"], "evaluation": [r"^4\.4\s+proactive policy steering"], "limitations": [r"^5\s+limitations$"]},
        "2603.23376": {"method": [r"^3\.2\s+physical preference alignment", r"^3\s+method$"], "evaluation": [r"^5\.3\s+evaluation results"], "limitations": [r"^6\s+conclusion$"]},
        "2603.23791": {"method": [r"system architecture", r"cognitive firewall", r"three-stage"], "evaluation": [r"experimental evaluation"], "limitations": [r"limitations", r"discussion"]},
        "2603.23806": {"method": [r"agentpex", r"methodology", r"system overview"], "evaluation": [r"experimental", r"evaluation"], "limitations": [r"^5\.\s+discussion"]},
        "2603.23914": {"method": [r"^3\s+methodology$"], "evaluation": [r"^4\.2\s+comparisons", r"^4\s+results$"], "limitations": [r"^5\s+conclusion$"]},
        "2603.24203": {"method": [r"^iv-c\s+tree-structured optimization"], "evaluation": [r"^v-b\s+experimental setup", r"^v-c\s+results"], "limitations": [r"^viii-b\s+limitations"]},
        "2603.24595": {"method": [r"model2kernel", r"making the model-kernel interface"], "evaluation": [r"^5\s+evaluation$"], "limitations": [r"^6\s+limitations"]},
        "2603.24755": {"method": [r"design principles", r"benchmark design"], "evaluation": [r"^3\s+experimental setup"], "limitations": [r"^6\s+conclusion$"]},
        "2603.24775": {"method": [r"completion blocks and trust model", r"invocation-bound"], "evaluation": [r"^5\s+evaluation$"], "limitations": [r"^7\s+limitations$"]},
        "2603.24963": {"method": [r"standard model template", r"system design", r"method"], "evaluation": [r"^4\s+experimental design"], "limitations": [r"^6\.3\s+limitations"]},
        "2603.25056": {"method": [r"^3\s+experimental design$", r"^3\.1\s+threat model"], "evaluation": [r"^5\.2\s+cross-model", r"^6\.6\s+adversarial validation"], "limitations": [r"^7\.6\s+limitations$"]},
        "2603.25158": {"method": [r"trace2skill", r"framework", r"method"], "evaluation": [r"^3\.1\s+experimental setup"], "limitations": [r"^6\s+conclusion$"]},
        "2603.25685": {"method": [r"reinforcement learning", r"method"], "evaluation": [r"^4\s+experiments$"], "limitations": [r"^5\s+conclusion$"]},
        "2603.25702": {"method": [r"s2d2", r"self-speculation", r"method"], "evaluation": [r"^5\s+experiments$"], "limitations": [r"^6\s+conclusion$"]},
        "2603.25716": {"method": [r"hybrid memory", r"hydra", r"method"], "evaluation": [r"^5\.1\s+experiment setup"], "limitations": [r"^6\s+conclusion$"]},
        "2603.25764": {"method": [r"study design", r"method", r"measurement"], "evaluation": [r"benchmark", r"results"], "limitations": [r"limitations", r"discussion", r"conclusion"]},
        "2603.25973": {"method": [r"^2\s+task settings", r"^3\s+dataset analysis"], "evaluation": [r"^4\.3\s+memory methods", r"^4\s+experiments$"], "limitations": [r"^5\s+conclusion$", r"^limitations$"]},
        "2603.25981": {"method": [r"^3\.4\s+policy-guided mppi", r"^3\s+method$"], "evaluation": [r"^4\.2\s+baselines", r"^4\.3\s+results"], "limitations": [r"^5\s+conclusion$"]},
        "2603.26074": {"method": [r"^4\.1\s+design and workflow", r"^4\s+methods$"], "evaluation": [r"^5\.2\s+main results"], "limitations": [r"^7\s+limitation$"]},
        "2603.26498": {"method": [r"modality-aware scheduling", r"system design", r"method"], "evaluation": [r"^4\.\s+evaluation"], "limitations": [r"^4\.4\.\s+discussion"]},
        "2603.26557": {"method": [r"^2\.2\s+overview of memboost", r"^2\s+memboost"], "evaluation": [r"^3\.2\s+results", r"^3\s+experiments"], "limitations": [r"^4\s+conclusion$"]},
        "2603.26666": {"method": [r"on-policy distillation", r"method", r"framework"], "evaluation": [r"^4\s+experiments$"], "limitations": [r"^6\s+conclusion$"]},
        "2603.26728": {"method": [r"^3\.\s+the sear framework"], "evaluation": [r"^6\.2\.\s+evaluation performance", r"^6\.3\.\s+routing performance"], "limitations": [r"^8\.\s+future work"]},
        "2603.26942": {"method": [r"^3\.1\.\s+experimental setup"], "evaluation": [r"^3\.2\.2\.\s+finding 2", r"^3\.2\.\s+results"], "limitations": [r"^4\.\s+discussion"]},
        "2603.26993": {"method": [r"^2\s+delegated decision model"], "evaluation": [r"^7\s+numerical experiments"], "limitations": [r"^8\s+conclusion$"]},
        "2603.27116": {"method": [r"^methods$", r"mathematical framework"], "evaluation": [r"forgetting experiments", r"tested interventions"], "limitations": [r"^discussion$", r"implications for system design"]},
        "2603.27138": {"method": [r"^3\.\s+design of scoutattention"], "evaluation": [r"^4\.3\.\s+performance evaluation"], "limitations": [r"^5\.\s+conclusion$"]},
        "2603.27204": {"method": [r"^4\.\s+methodology"], "evaluation": [r"^5\.\s+evaluation"], "limitations": [r"^6\.\s+discussion"]},
        "2603.27287": {"method": [r"interleaved", r"method", r"framework"], "evaluation": [r"^4\.1\s+experimental setup", r"results"], "limitations": [r"^5\s+conclusion$"]},
        "2603.27355": {"method": [r"^2\s+system overview"], "evaluation": [r"^5\s+experiments$", r"^6\s+validation"], "limitations": [r"^8\s+limitations"]},
        "2603.27467": {"method": [r"^3\.1\s+angular quantization", r"^3\s+method$"], "evaluation": [r"^4\.7\s+competitive comparison", r"^4\.3\s+per-layer"], "limitations": [r"^6\s+conclusion$"]},
        "2603.27517": {"method": [r"^4\s+security taxonomy", r"^2\s+modeling system architecture"], "evaluation": [r"^3\s+corpus overview", r"^5\s+multi-layer"], "limitations": [r"^6\s+defense discussion"]},
        "2603.27624": {"method": [r"^iv\s+fse-dp", r"^v-a\s+scheduling algorithm"], "evaluation": [r"^vi-c\s+end-to-end evaluation"], "limitations": [r"^vii\s+conclusion$"]},
        "2603.27819": {"method": [r"^3\.2\s+loss function", r"^3\s+method$"], "evaluation": [r"^5\.1\s+main results", r"^4\s+experimental setup"], "limitations": [r"^6\s+analysis: limits", r"^8\s+conclusion"]},
        "2603.28013": {"method": [r"^3\.2\s+kill-chain stages", r"^3\s+benchmark design"], "evaluation": [r"^4\.1\s+exposure", r"^4\s+results$"], "limitations": [r"^7\s+limitations$"]},
        "2603.28101": {"method": [r"^4\s+trajectory-level scheduler", r"^5\s+trajectory-aware placement"], "evaluation": [r"^7\.1\s+overall performance", r"^7\s+evaluation$"], "limitations": [r"^8\s+discussion$"]},
        "2603.28239": {"method": [r"^3\.\s+design and implementation"], "evaluation": [r"^4\.5\.\s+llm tp inference", r"^4\.\s+evaluation"], "limitations": [r"^6\.\s+conclusion$"]},
        "2603.28565": {"method": [r"^4\.1\s+state-based modeling", r"^4\s+method$"], "evaluation": [r"^5\.2\s+experimental results"], "limitations": [r"^7\s+conclusions$"]},
    })
    base.NARRATIVE_LENS.update({
        "WORLDVIEW-SCALING-LAW": ("按单次拟合曲线外推最省实验成本。", "拟合器、采样点和固定计算预算会系统性改变所谓最优规模。", "scaling experiment 的数据、拟合与决策证据", "只在同一模型族、数据和计算协议内仍可复用局部曲线。"),
        "MODEL-SELF-ATTENTION": ("dense attention 保留完整 token 交互。", "长度增长令二次计算和显存成为主瓶颈。", "attention feature 的选择、稀疏化与精度边界", "中短序列或强全局依赖仍应保留 dense attention。"),
        "MULTIMODAL-REPRESENTATION": ("所有视觉 token 等价进入后续层，语义最直接。", "视频和高分辨率输入使冗余 token 主导延迟和显存。", "token identity、选择和模态对齐状态", "token 数量可控或细节不可丢失时全量表示仍成立。"),
        "TRAIN-LORA": ("单 adapter 独立训练和部署最易归因。", "多任务合并要求保持子空间覆盖并处理方向冲突。", "adapter 子空间、合并权重与回退版本", "任务单一或需强隔离时独立 adapter 更稳健。"),
        "TRAIN-PPO": ("固定 reference 与 clipped update 提供可控策略改进。", "长 rollout 和自模仿改变了旧策略数据的价值。", "rollout 来源、ratio、replay 与 freshness", "在线数据充足且策略漂移可控时标准 PPO 仍成立。"),
        "INFER-REQUEST-LIFECYCLE": ("把一次请求视为同质前向路径，接口最简单。", "长度、模态、压缩与硬件差异使成本沿阶段分化。", "请求阶段、状态身份、路由与成本归属", "同质短请求仍可使用统一执行路径。"),
        "INFER-DECODE": ("逐 token decode 保持状态提交清晰。", "多模态与长序列使 attention memory 和带宽主导每步成本。", "decode 状态、memory access 与提交顺序", "短输出和小 batch 下普通 decode 仍是可靠基线。"),
        "INFER-TENSORRT-LLM": ("通用算子图优先可移植性和实现简单。", "量化、kernel fusion 与异构硬件要求执行计划显式化。", "kernel、precision、layout 与执行计划 owner", "模型较小或硬件多变时通用 runtime 仍更易维护。"),
        "INFER-GPU-MEMORY": ("全部活跃状态驻留 GPU，访问路径最短。", "上下文和并发超过 HBM 容量后必须引入层级放置。", "HBM/DRAM 状态放置、迁移与预取", "状态可装入 HBM 且延迟敏感时全驻留仍最佳。"),
        "PLATFORM-FOUNDATIONS": ("单团队脚本可快速交付模型服务。", "模型族、环境和团队增长要求资产与控制面契约稳定。", "资产、workload、service 与 controller ownership", "单一团队和短期实验仍可保留轻量脚本。"),
        "PLATFORM-GATEWAY": ("静态 endpoint 路由在模型与流量同质时足够。", "能力、成本、隐私和负载差异要求语义化路由。", "请求分类、策略、fallback 与路由证据", "单模型单租户仍可直连后端。"),
        "PLATFORM-PRODUCTION": ("离线测试通过后人工发布最直观。", "RAG/agent 的行为依赖外部状态，要求 CI gate 与可回滚证据。", "evaluation evidence、release gate 与 rollback", "低风险离线工具仍可采用简化发布流程。"),
        "AGENT-CONTEXT": ("原始上下文完整拼接最少派生状态。", "长度、成本和信息稀释要求压缩与选择。", "context 选择、压缩、provenance 与失效", "短上下文或证据必须逐字保留时原始拼接更合适。"),
        "AGENT-RAG": ("请求时检索可把知识与模型权重分离。", "生产负载引入索引、缓存、隐私和证据归属。", "query、index、retrieval result 与 serving cache", "知识稳定且规模小时参数化知识或简单检索仍可用。"),
        "AGENT-TOOL-CALLING": ("单次函数调用只需 schema 和返回值。", "多步工具链要求训练、状态和失败恢复可验证。", "tool proposal、参数、执行结果与后续状态", "单工具、只读调用仍可保持薄接口。"),
        "AGENT-REFLECTION": ("一次生成后直接执行，短任务中延迟最低。", "长链推理和环境反馈要求显式检测错误并决定重试或停止。", "critic evidence、修订状态、预算与停止条件", "可验证一步任务仍可直接执行而不引入反思循环。"),
        "AGENT-MULTI-AGENT": ("单 agent 保持上下文与责任集中。", "任务分解和并行协作引入通信、归责与一致性成本。", "角色、消息、共享状态与失败归属", "任务耦合紧或协调成本高时单 agent 仍更可靠。"),
        "AGENT-PLATFORM": ("把 agent 当进程内 loop 能快速试验。", "技能、长期运行和外部动作要求 runtime control 与生命周期治理。", "agent identity、skill、execution state 与控制面", "短时、无外部副作用的 loop 仍可轻量实现。"),
    })
    cached = existing_review_cache()
    original_review_one = base.review_one

    def review_one(row: dict, src: Path) -> dict:
        key = f"arXiv:{row['arxiv_id']}v1"
        review = dict(cached[key]) if key in cached else original_review_one(row, src)
        review = repair_saved_full_text(review)
        aid = row["arxiv_id"]
        review["stable_node_id"] = base.NODE_OVERRIDES[aid]
        review["problem"], review["method_text"], review["evaluation_text"], review["limitations_text"] = PAPER_SYNTHESIS[aid]
        if review.get("withdrawn"):
            raise RuntimeError(f"withdrawn source remained selected: {aid}")
        if review["result"] != "complete":
            review["books_disposition"] = "Blocked / Unverified"
            review["review_route"] = "deep"
        else:
            review["books_disposition"] = "Integrate" if aid in INTEGRATE else "No Change — Existing Coverage"
            review["review_route"] = "deep" if aid in INTEGRATE else "standard"
        return review

    base.review_one = review_one
    original_owner_proposition = base.owner_proposition
    def owner_proposition(path: str, row: dict) -> tuple[str, str]:
        heading, proposition = original_owner_proposition(path, row)
        manuscript = (base.ROOT / path).read_text(errors="ignore")
        if heading != "章节主命题" and base.clean(proposition) in base.clean(manuscript):
            return heading, proposition
        # A long section can make the generic ranker miss every paragraph.  In
        # that case recover an actual current section and paragraph rather than
        # emitting the synthetic ``章节主命题`` fallback into the writeback queue.
        preferred = BOOKS_EXISTING[base.NODE_OVERRIDES[row["arxiv_id"]]][0]
        headings = list(re.finditer(r"^#{2,4}\s+(.+)$", manuscript, re.M))
        ordered = sorted(
            headings,
            key=lambda match: (base.clean(match.group(1)) != preferred, match.start()),
        )
        for match in ordered:
            current = base.clean(match.group(1))
            if re.search(r"review notes?|sources?|references?|evidence", current, re.I):
                continue
            next_start = next((item.start() for item in headings if item.start() > match.start()), len(manuscript))
            body = manuscript[match.end():next_start]
            for raw in re.split(r"\n\s*\n", body):
                paragraph = base.clean(raw)
                if 80 <= len(paragraph) <= 1400 and not paragraph.startswith(("- ", "* ", "|", "```", "<!--")):
                    return current, paragraph[:700]
        raise RuntimeError(f"no current manuscript proposition found for {row['arxiv_id']} at {path}")
    base.owner_proposition = owner_proposition
    original_first_heading = base.first_heading
    def first_heading(path: str) -> str:
        preferred = BOOKS_SECTION_BY_PATH.get(path)
        manuscript = (base.ROOT / path).read_text(errors="ignore") if (base.ROOT / path).exists() else ""
        actual = {base.clean(match.group(1)) for match in re.finditer(r"^#{1,4}\s+(.+)$", manuscript, re.M)}
        return preferred if preferred in actual else original_first_heading(path)
    base.first_heading = first_heading
    required = {aid for ids in SELECTED.values() for aid in ids}
    missing_routes = required - set(base.NODE_OVERRIDES)
    extra_routes = set(base.NODE_OVERRIDES) - required
    if missing_routes or extra_routes:
        raise RuntimeError(f"route table mismatch missing={sorted(missing_routes)} extra={sorted(extra_routes)}")
    raw_total, records, receipt = base.load_records()
    # The v2 ownership receipt contains one registered category identity whose
    # local DataCite shard lacks the Submitted field expected by lane C's
    # legacy loader.  The lane-D inventory has already joined its title,
    # abstract and created-backed owner, so merge it instead of silently
    # shrinking the raw denominator.
    for day in range(25, 32):
        ledger_path = base.ROOT / f"papers/2026/03/_sources/daily-202603{day:02d}/screening-ledger-updated-v1-replay.json"
        for row in json.loads(ledger_path.read_text())["identities"]:
            # Lane C predates the created/registered-backed ownership receipt
            # and filters on the receipt's compact ``status`` field.  Preserve
            # the authoritative lane-D identity instead of dropping a record
            # merely because DataCite omitted the provenance-only Submitted:v1
            # date (2603.28015 is the known March example).
            recovered = dict(row)
            recovered.setdefault("status", recovered.get("announcement_recovery_status"))
            recovered.setdefault("owner_report_date", recovered.get("report_date"))
            recovered.setdefault("registry_updated_v1_utc", recovered.get("updated_v1_utc_announcement_recovery_lead"))
            recovered.setdefault("submitted_v1_utc", recovered.get("submitted_v1_utc_provenance_only"))
            records.setdefault(row["arxiv_id"], recovered)
    raw_total = receipt["record_count"]
    for day in range(25, 32):
        base.render_day(day, raw_total, records)
        time.sleep(0.25)


if __name__ == "__main__":
    main()
