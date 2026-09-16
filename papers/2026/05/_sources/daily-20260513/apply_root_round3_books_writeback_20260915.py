#!/usr/bin/env python3
"""Apply the root-owned 2026-05-13 Round-3 Books writeback queue.

The author agent may prepare the queue but may not edit shared Books.  This
script inserts proposition-level prose under the reviewed canonical anchors and
is idempotent by Source Family ID.
"""

from __future__ import annotations

import json
import re
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
QUEUE = HERE / "v3-root-writeback-queue.json"


INSERTS = {
    "2605.10971": (
        "逐属性 Commitment 把 Steering 时机变成状态",
        "统一 timestep 施加 steering 的前提，是各属性在去噪轨迹中的形成速度近似一致；它简单、可复算，也不会额外引入属性控制器。离散 diffusion 同时承担内容、风格与安全属性后，这个前提会失效：过早干预尚未稳定的属性会破坏流畅性，过晚干预又失去控制窗口。更稳妥的接口是由只读 probe 估计每个属性的 commitment 进度，再由调度器选择干预时点；probe 只提供观测，不能直接冻结 token 或越过最终生成策略。\n\n逐属性 schedule 用额外探测、校准和轨迹监督换取更细的可控性，也新增 probe 漂移、属性耦合和干预相互覆盖等 failure mode。属性少且形成时机稳定时，统一 schedule 仍是更便宜的基线；校准不足时应回退保守晚干预。`arXiv:2605.10971v1` 的 §3–§5 与 Appendix F 只支持作者的离散 diffusion、属性与延迟设置，不证明这一时序控制可无损迁移到任意生成模型。",
    ),
    "2605.10973": (
        "Rotation-preserving 约束把遗忘风险落到敏感方向",
        "普通 SFT 允许梯度自由重排参数空间，在目标数据充足、旧能力可重训时最直接；continual SFT 的约束变成既要适配新任务，又要保护少量对 pretrained function 敏感的方向。rotation-preserving 分支把这些方向作为受保护 state，由优化器限制更新造成的旋转，而不是把所有参数一律冻结。它改变的是可训练子空间的几何约束，不是给旧能力提供绝对不变保证。\n\n保护敏感方向可减少部分遗忘，却需要估计和保存方向、增加优化约束，并可能阻碍新任务真正需要的表征重写；方向估计失真还会保护错误子空间。旧任务不重要或分布改变很大时，普通 full SFT 仍合理；预算紧、需要独立回滚时 adapter 仍更清楚。`arXiv:2605.10973v1` 的 §3–§5 与 Appendices C–E 只证明作者模型和任务中的 adaptation–forgetting 结果，不能外推为通用最优 SFT 几何。",
    ),
    "2605.10998": (
        "Preference Data Admission 也必须检查安全能力重分布",
        "DPO 数据经过表面有害内容过滤后直接进入训练，在偏好样本与部署风险同分布时成本最低；问题是看似 benign 的偏好对仍可能改变 refusal boundary，并把安全能力在分布外重新分配。因而 admission owner 不能只检查文本内容，还要把 base model、reference policy、偏好对、训练超参数与分布外 safety slice 绑定为同一更新身份，并在发布前比较 capability access 的迁移。\n\n这种前置验收提高攻击与意外退化的可见性，却增加红队切片、对照训练和回归成本，也无法穷举未知触发。小规模、可信且不触及安全边界的适配仍可沿用普通数据审核；一旦分布外拒答显著下降，应回退隔离 adapter、缩小更新或停止发布。`arXiv:2605.10998v1` 的 §2、§4–§7 与 Appendix G 只支持作者构造的 benign-DPO 攻击和受测模型，不证明所有 benign 数据都具有同类风险。",
    ),
    "2605.11036": (
        "Agent 身份可以绑定有状态行为轨迹",
        "单轮文本 watermark 或静态签名在调用彼此独立、对手不能长期交互时足够便宜；长程 Agent 会让身份信号分散在工具选择、动作顺序和环境响应中。sequential behavioral watermark 把挑战序列、期望行为转移与累计检测统计作为 verifier state，Agent 只产生行为，独立 verifier 才拥有身份判定权。这样检测对象从一句输出变成带顺序和上下文的 trajectory contract。\n\n轨迹信号提高对单轮改写的韧性，却引入挑战设计、状态保存、误归因和适应性对手学习模式的风险，也可能改变正常任务行为。无法控制交互序列或代价过高时，应回退 artifact signing、静态 provenance 与普通行为审计。`arXiv:2605.11036v1` 的 §4–§5 和 Appendix A 只验证作者的挑战与 Agent 设置，不构成普遍身份认证或防克隆证明。",
    ),
    "2605.11061": (
        "统一 Pixel-space 仍要拆开表示与生成责任",
        "encoder、projector 与独立 image decoder 分阶段训练时，modality boundary 清楚、组件容易替换；代价是理解表示与生成表示可能长期分叉。native pixel-space 分支让统一 Transformer 同时消费和产生更接近像素的 state，使数据配比、noise/causal objective、decoder capacity 与输出 fidelity 一起成为 representation artifact identity。共享 backbone 因而减少接口，不等于理解与生成已经共享同一证据标准。\n\n统一训练能减少跨组件对齐，却扩大序列、显存和训练耦合，并把重建误差与语义误差混在同一更新路径。高分辨率成本不可接受、数据不足或只需单向理解时，离散 tokenizer 或冻结 encoder 仍更合适。`arXiv:2605.11061v1` 的 §2–§8 只支持作者的 pixel-level 架构、训练与图像评测；没有独立 limitations，也不能由其结果推出生产多模态系统的通用最优表示。",
    ),
    "2605.11128": (
        "局部校准误差会复合成序列级多样性坍缩",
        "top-k、top-p 或 temperature 假设 token 概率的相对顺序和形状足以支持逐步选择；在短输出和低歧义任务中这是合理近似。长序列会把 order miscalibration 与 shape miscalibration 持续写回 prefix：前者让候选排序错误，后者让概率质量过尖或过平，局部误差最终表现为 sequence-level diversity collapse。评测因此要同时保存 token-level calibration slice 与整段输出的覆盖、多样性和正确性，不能只调一个解码超参数。\n\n联合校准增加 reference distribution、采样次数和 evaluator 成本，也可能把任务本身的单峰答案误判为坍缩。确定性任务或严格可复现接口仍可使用 greedy/低温策略；缺少可靠 target distribution 时应报告未判定而非声称已校准。`arXiv:2605.11128v1` 的 §4–§5、相关附录实验及 Appendix J 只证明作者模型与任务上的两类误差，不给出跨 workload 的通用采样配方。",
    ),
    "2605.11186": (
        "Memory-limited Speculation 要联合规划树与驻留状态",
        "固定 draft depth 或只最大化 acceptance，在 draft/target state 都能常驻设备时容易实现；内存受限后，扩大候选树会同时增加 KV、intermediate state 与 verification batch 占用。级联自适应树把候选扩展顺序、存活概率和 memory budget 放进同一 plan，scheduler 拥有分配与裁剪权，draft 只提出候选，target verification 仍拥有 commit authority。\n\n联合规划可能提高单位内存的有效接受长度，却带来在线估计、树管理和不规则 kernel 开销；预测偏差会让高价值分支被过早裁掉。短输出、低并发或显存宽裕时，固定 verify length 仍更稳定。`arXiv:2605.11186v1` 的 §4–§6 只支持作者模型、显存和 workload 下的级联树结果，不证明 production serving 的端到端 SLO 必然改善。",
    ),
    "2605.11277": (
        "Expert Placement 必须跟随热度演化",
        "把 expert 静态放在 GPU 或 PIM 上，在 token-to-expert 分布稳定时可提前编译并减少迁移；MoE 服务的 expert 热度随任务和层变化后，会形成热点与冷门路径，静态 placement 可能让执行位置与真实负载错配。动态分支把 recent routing histogram、迁移成本和位置容量作为 placement state，由调度器决定 expert 在何处执行，router 仍只决定 token 路由。\n\n动态放置用监控和迁移换更低的热点等待，却新增分布滞后、thrashing、PIM/GPU 数值差异和恢复复杂度。负载稳定、迁移昂贵或观测窗口不足时，静态 placement 仍是正确回退。`arXiv:2605.11277v1` 的 §3–§7 只证明受测 PIM、MoE 与 trace 下的设计，不允许把作者加速数字外推到其他硬件、精度或并发。",
    ),
    "2605.11301": (
        "Answer 前 Routing 只能预测反事实效用",
        "总是调用最强多模态模型可以避免选择误差，但成本和延迟最高；基于 prompt embedding 的路由在候选模型差异稳定时更便宜。answer 前的 router 实际预测的是“若调用某模型，预期效用如何”，这是带选择偏差的 counterfactual proposal，不是已观察质量。路由状态应绑定请求表示、候选模型版本、训练反馈和校准区间，admission controller 再结合成本、SLO 与风险决定派发。\n\n这种预测减少全量试跑，却会遭遇未选模型缺反馈、分布漂移和模态特征遗漏；高风险、冷启动或校准区间重叠时应回退最强模型、并行比较或人工策略。`arXiv:2605.11301v1` 的 §2–§4 和 Appendix E 只支持作者候选池与多模态 benchmark，不证明 router score 是真实正确率或跨模型通用尺度。",
    ),
    "2605.11334": (
        "Single-call Judge Confidence 是传感器，不是 Verdict",
        "重复调用或多 judge 集成可以估计判决稳定性，但成本高；从一次结构化 reasoning 中分解 claim、evidence 与局部 verification 信号，可以形成更便宜的 confidence sensor。这个分解器只拥有不确定性观测权，最终 verdict 仍应由校准规则、独立证据和发布策略决定，并把 judge、prompt、reasoning schema 与 calibration set 绑定为版本身份。\n\n单调用估计降低成本，却共享 judge 本身的盲区：流畅但错误的 reasoning 可能产生高置信，schema 漂移也会破坏校准。高风险或域外样本应回退独立 verifier、多次采样或人工复核。`arXiv:2605.11334v1` 的 §3–§7 只支持作者 judge、任务和校准结果；没有独立 limitations，也不能把输出直接解释为事实正确概率。",
    ),
    "2605.11426": (
        "整体 Activation 相似不能证明内部能力未重排",
        "用平均 representation similarity 比较 SFT 前后模型，在变化广泛且稠密时是便宜诊断；稀疏 latent 只在特定 task/layer 激活时，整体相似度会把局部迁移淹没。评测应沿 layer、task 和 latent support 保存差异，并将这些内部 sensor 与最终行为、可干预性分别报告；probe 只描述相关结构，不能宣布模型真实推理机制。\n\n细粒度分析提高局部漂移可见性，却增加 probe 选择、多重比较和解释歧义，也可能把无害重参数化误判为能力改变。只关心最终结果或缺少可靠 intervention 时，行为回归仍是主 gate。`arXiv:2605.11426v1` 的 §3–§4 与 Conclusion/Limitations 只支持作者模型和任务上的 mechanistic observation，不证明相似 activation 意味着能力保留或 trace 忠实。",
    ),
    "2605.11491": (
        "Entropy Flow 必须在严格 On-policy 边界内治理",
        "固定 entropy bonus 把所有 token 的探索压力统一增加，在早期策略和任务同质时简单；RLVR 训练后期的 entropy collapse 可能来自 entropy-increasing 与 entropy-decreasing token update flow 失衡。控制器可以观测两类 flow，在当前 policy 的样本上调节更新权重；它拥有优化 proposal，而 verifier reward 与 policy update 语义不能被离线样本静默改写。\n\n定向调节能保留部分探索，却新增 token 分类噪声、额外统计和策略振荡；过强的 entropy-increasing 更新也会牺牲可验证正确率。样本少、估计不稳或严格复现更重要时，固定正则与早停仍是回退。`arXiv:2605.11491v1` 的 §3–§6 与文末 Limitations 只支持作者 RLVR 设置，不证明该 flow 分解适用于 off-policy pipeline 或所有奖励结构。",
    ),
    "2605.11592": (
        "Unlearnability 与 Unlearning 不能共用一个浅层遗忘分数",
        "在训练前让样本难以被记忆，以及训练后从模型中删除影响，分别管理 admission 与已写入参数的 state；两者都可能只造成 shallow dememorization，让标准 probe 看似遗忘但知识仍可由重写、微调或旁路恢复。验收应区分 prevention、parameter influence、behavioral withholding 与 relearning resistance，并为每层保存攻击预算和 retained-utility 对照。\n\n多层验收减少把拒答率当删除证明的风险，却显著增加攻击、重训和因果归因成本，而且仍无法证明对所有未来 probe 永久删除。低风险数据或可从干净 checkpoint 重训时，数据删除加重训仍是更清楚的基线。`arXiv:2605.11592v1` 的 §3–§7 与结论只支持其 taxonomy、方法和实验范围，不能把单一 benchmark 解释为通用 deletion certificate。",
    ),
    "2605.11625": (
        "Reasoning Budget 应按可解收益而非主观难度分配",
        "固定 token budget 对请求公平、延迟可预测；按模型感知的 difficulty 增配计算，则可能在无解问题上持续消耗。更合适的 scheduler state 是在给定 budget 下的 solvability 与边际收益，允许立即作答、继续推理或 fold/abstain；模型只提出这些信号，预算与发布控制仍由外部策略持有。\n\n自适应分配提高平均计算利用率，却依赖可校准的 solvability 估计，并新增误放弃可解题、对高估样本过度投入和延迟抖动。强实时 SLO、校准不足或任务成本相近时，固定预算仍更安全。`arXiv:2605.11625v1` 的 §3–§4 与 Appendix G 只支持作者任务和 budget 设置，不证明模型主观 confidence 可直接成为生产调度依据。",
    ),
    "2605.11664": (
        "Safety Assessment 与 Generation 可以分离，但 Authority 不变",
        "单一静态 filter 延迟低、行为稳定，但看不到复杂上下文；完整 agentic analyzer 能组合更多证据，却增加调用成本和可攻击控制流。inference-time safety 可以让静态 filter 处理确定性模式，把歧义请求升级给受限 analyzer，再将结构化 safety context 交给 generator；两者只拥有 assessment 权，gateway policy 仍决定 admission 与 effect。\n\n分层分析用覆盖率换 latency、上下文注入风险和 analyzer 失误，还可能让 generator 过度依赖一条错误 safety summary。低风险、模式稳定时静态规则仍合理；高风险 action 必须保留 deterministic policy 与人工审批。`arXiv:2605.11664v1` 的 §4–§6 只验证作者黑盒模型、攻击集和两类分析器，不证明开放攻击下的安全性或其他硬件上的延迟。",
    ),
    "2605.11685": (
        "删除验收必须覆盖 Representation 的 Minor Components",
        "只编辑 dominant directions 能以较小 utility 损失压低常见 probe，在攻击预算弱时是合理折中；relearning 会利用仍保留在 minor components 中的残余信息恢复目标能力。因而 unlearning artifact 要把主/次表示分量、编辑规则、relearning 攻击与 retained task 一起版本化，删除 owner 不能仅凭 dominant probe 通过发布。\n\n覆盖次要分量提高抗恢复性，却扩大编辑面、计算成本和 collateral damage，也依赖当前 decomposition 的有效性。可重训场景仍应优先数据删除与干净重训；无法证明残余已消失时应标为 unverified 而非“已遗忘”。`arXiv:2605.11685v1` 的 §3–§5 与 Appendix A 只支持作者模型、分量定义和攻击，不构成任意表示空间中的永久删除证明。",
    ),
    "2605.11750": (
        "Critical-phase Dreaming 只获得候选排序权",
        "每步都运行 world-model rollout 会超过实时控制预算，完全 reactive policy 又可能在关键转折前看不到失败。受限方案先由 trigger 判断 critical phase，再生成少量 action proposals，用 short-horizon dream evaluator 排序，最后把候选交给 runtime assurance；dream state 不拥有物理 commit 权，真实 observation 仍会覆盖想象。\n\n按关键阶段调用减少平均开销，却新增 trigger 漏检、world-model 偏差和 evaluator 自我确认；错误 dream 可能把安全动作排除。高频、不可逆或模型失配时，应回退 reactive controller、硬约束和 human override。`arXiv:2605.11750v1` 的 §3–§7 与 Appendix F 只支持作者仿真和真实机器人设置，不证明开放环境安全或长期 rollout 忠实。",
    ),
    "2605.11800": (
        "Analog CIM 的 MoE 校准要同时修 Expert 与 Router",
        "在数字执行上沿用 clean-trained router，只校准权重或 activation scale，默认噪声不会改变 expert 相对选择；analog CIM noise 会同时扰动 expert 输出和 router logits，进而放大 load imbalance。部署 artifact 因而需要把噪声模型、expert replacement、router calibration、placement 和 routing histogram 绑定在一起，校准器只能提出补偿，release gate 仍根据质量与负载证据决定启用。\n\n联合补偿提高受测噪声下的稳定性，却增加备用 expert、校准数据和硬件特定状态，也可能随芯片老化或 workload 漂移失效。噪声低、数字 fallback 充足或 router 稳定时，普通 per-expert calibration 仍更简单。`arXiv:2605.11800v1` 的 §2–§4 与结论只支持其 real-chip-calibrated noise、模型和实验，不代表所有 CIM 或生产流量。",
    ),
    "2605.12105": (
        "Agency 与 Autonomy 要拆成两个部署旋钮",
        "让 Agent 自行规划但所有 effect 都经人工确认，可以提高 agency 而保持较低 autonomy；反过来，固定流程中的自动执行可能 autonomy 高却几乎没有目标选择权。平台应分别版本化 goal/plan discretion 与 effect authority，并用 checkpoint、escalation、tool fencing、write staging 和 rollback 调节二者，而不是给任务贴一个统一“自治等级”。\n\n拆分后能按风险配置控制面，却增加 policy 组合、审计和用户心智成本，错误 checkpoint 也会制造形式审批。低风险、可逆的固定流程可保留高自动执行；目标模糊或 effect 不可逆时应收紧两轴并前移人工 commit。`arXiv:2605.12105v1` 的 §III–§V 只提供架构维度与案例，后续章节没有把它证明为合规认证或生产有效性保证。",
    ),
    "2605.12110": (
        "Sparse Attention 的 Block Size 也是 Per-head 路由状态",
        "固定 block size 让 layout、kernel 和 KV contract 可提前编译，在 head 行为近似时效率稳定；不同 head 的远程依赖与局部密度不同时，同一粒度会让部分 head 过算、部分 head 丢失上下文。adaptive branch 为每个 head 选择 block size，并让 route、mask、kernel/layout 与 KV retention 共同进入 execution identity，而不是把算法稀疏率与可实现速度分开报告。\n\n细粒度选择减少无效 attention，却增加 route metadata、kernel fragmentation、负载不均和编译缓存；错误路由还会造成不可恢复的信息遗漏。上下文短、head 差异小或硬件只优化固定 tile 时，统一 block 仍更合适。`arXiv:2605.12110v1` 的 §2–§4 与结论只支持作者模型、kernel 与硬件，不能把 headline 稀疏率直接外推为端到端 serving 加速。",
    ),
    "2605.12460": (
        "Multi-stream 把单一 Token Clock 降为接口选择",
        "单流 Decoder-only 让 thought、input 与 output 共用一个因果时钟，训练、KV 与流式协议最简单；并行工具输入、内部推理和可见输出会让单流阻塞暴露出来。multi-stream 分支为不同 stream 保持各自位置与可见性规则，再由显式 synchronization/merge point 交换状态；模型拥有 token proposal，runtime 持有 stream lifecycle、权限与外部 effect commit。\n\n并行流可以减少等待并隔离可见输出，却引入跨流因果一致性、KV/layout、训练数据格式和 monitor blind spot；错误同步可能泄漏 private thought 或产生乱序 effect。普通聊天、工具少或审计优先时，单流协议仍是可靠基线。`arXiv:2605.12460v1` 的 §2–§7 与附录只验证作者的多流训练和实验，不证明 production scheduler 一定获益，也不替代 Agent 权限控制。",
    ),
}


def insert_under_anchor(text: str, anchor: str, title: str, body: str, sf: str) -> str:
    if sf in text:
        return text
    lines = text.splitlines(keepends=True)
    anchor_index = next((i for i, line in enumerate(lines) if anchor in line and line.lstrip().startswith("#")), None)
    if anchor_index is None:
        raise SystemExit(f"anchor not found: {anchor}")
    level = len(lines[anchor_index]) - len(lines[anchor_index].lstrip("#"))
    insert_index = len(lines)
    for i in range(anchor_index + 1, len(lines)):
        match = re.match(r"^(#+)\s", lines[i])
        if match and len(match.group(1)) <= level:
            insert_index = i
            break
    subsection = "\n" + "#" * (level + 1) + f" {title}\n\n{body}\n\n<!-- semantic-body-binding:{sf} -->\n\n"
    lines.insert(insert_index, subsection)
    return "".join(lines)


queue = json.loads(QUEUE.read_text())
if len(queue["items"]) != len(INSERTS):
    raise SystemExit("queue/insert cardinality mismatch")

changed = 0
for item in queue["items"]:
    arxiv_id = item["arxiv_id"]
    sf = item["source_family_id"]
    title, body = INSERTS[arxiv_id]
    path = ROOT / item["owner_path"]
    old = path.read_text()
    new = insert_under_anchor(old, item["proposed_anchor"], title, body, sf)
    if new != old:
        path.write_text(new)
        changed += 1
    item["root_status"] = "applied_current_worktree_pending_fresh_non_author_review"
    item["root_writeback_date"] = "2026-09-15"

queue["status"] = "root_writeback_complete_pending_fresh_non_author_review"
queue["root_applied_count"] = len(queue["items"])
QUEUE.write_text(json.dumps(queue, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({"changed_files_or_blocks": changed, "applied": len(queue["items"]), "status": queue["status"]}, ensure_ascii=False))
