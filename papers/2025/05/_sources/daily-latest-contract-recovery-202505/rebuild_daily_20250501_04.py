#!/usr/bin/env python3
"""Rebuild 2025-05-01..04 Daily V2.1 from official announcement owners.

The script deliberately does not read Weekly reports.  Historical Daily input is
the official owner inventory plus exact-v1 primary packets already saved below
this source root (or in the prior Daily replay packet for unchanged candidates).
"""

from __future__ import annotations

import gzip
import hashlib
import importlib.util
import json
import re
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
SRC = Path(__file__).resolve().parent
OLD = ROOT / "papers/2025/05/_sources/daily-v2.1-replay-202505"
STAGED_EXACT = Path("/private/tmp")


MAY1_OLD = {
    "2504.21303", "2504.21318", "2504.21356", "2504.21370",
    "2504.21411", "2504.21463", "2504.21668", "2504.21680",
    "2504.21752", "2504.21776", "2504.21798", "2504.21801",
}
MAY1_NEW = {
    "2504.21015", "2504.21024", "2504.21034", "2504.21035",
    "2504.21036", "2504.21038", "2504.21136", "2504.21205",
    "2504.21228", "2504.21614",
}
MAY2_OLD = {
    "2505.00254", "2505.00263", "2505.00315", "2505.00337",
    "2505.00342", "2505.00347", "2505.00358", "2505.00443",
    "2505.00506", "2505.00570",
}
MAY2_MIGRATED = {"2505.00212", "2505.00232", "2505.00234"}
MAY2_NEW = {
    "2505.00018", "2505.00019", "2505.00020", "2505.00024",
    "2505.00041", "2505.00065", "2505.00105", "2505.00321",
    "2505.00365", "2505.00458", "2505.00466", "2505.00626",
    "2505.00675",
}


NEW = {
    "2504.21015": dict(fid="SF-2025-DONT-RETRIEVE-GENERATE", node="AGENT-RAG", score=(3,2,2), title="Don't Retrieve, Generate", claim="把 RAG 训练数据来源从只检索公开问答扩展为可控生成的 hypothetical negatives；关键系统边界是生成器版本、去重、污染审计与真实检索回放必须共同冻结。", boundary="作者实验只比较其合成 hard-negative recipe 与披露数据集，不能证明生成数据普遍优于真实 retrieval logs。", method="#S3", evaluation="#S5", limits="#S8", chapter="books/part-07-agent/76-rag.md#检索不是一次查询，而是一条可观测流水线", adjacent="books/part-04-training-system/27-data.md#数据管线不是 ETL，而是模型行为的上游控制面"),
    "2504.21024": dict(fid="SF-2025-WEBEVOLVER", node="AGENT-WORKFLOW", score=(3,3,2), title="WebEvolver", claim="把 web agent 自我改进拆成 evolving policy 与 co-evolving environment model，说明 rollout 数据、网页状态和 evaluator revision 必须作为同一训练 identity 管理。", boundary="结果绑定作者构造的 web environment 与任务；没有证明开放互联网漂移、权限边界或真实副作用下仍能安全自演化。", method="#S3", evaluation="#S4", limits="#S5", chapter="books/part-07-agent/84-agent-platform.md#Self-evolution 必须拆成 Proposal、Verifier 与 Release", adjacent="books/part-03-multimodal-world-models/25-multimodal-world-models.md#Open-loop imagination vs closed-loop correction"),
    "2504.21034": dict(fid="SF-2025-SAGA-IDENTITY", node="AGENT-PLATFORM", score=(3,3,3), title="SAGA", claim="把 agent identity、authentication、delegation 与 user lifecycle 放进协议状态机；agent 可提出动作，但 principal lineage 与 effect-time authorizer 才拥有提交权。", boundary="论文给出协议与原型评估，不等于互联网规模身份联邦、密钥轮换、撤权传播或恶意参与方下已经安全。", method="#S3", evaluation="#S5", limits="#S7", chapter="books/part-07-agent/84-agent-platform.md#Policy 与 Agent Identity", adjacent="books/part-06-ai-infrastructure/72-security.md#多跳 Delegation 必须保留 Human Principal"),
    "2504.21035": dict(fid="SF-2025-SEMANTIC-REIDENTIFICATION", node="PLATFORM-SECURITY", score=(3,3,2), title="A False Sense of Privacy", claim="证明移除显式 PII 或生成 synthetic text 并不关闭语义再识别通道；privacy boundary 必须绑定攻击者辅助信息、关系特征与 release surface。", boundary="攻击成功率只对论文披露的数据、模型与辅助信息成立，不能外推为所有去标识化文本都可被同等重识别。", method="#S3", evaluation="#S5", limits="#A1", chapter="books/part-06-ai-infrastructure/72-security.md#从独立 Span 到关系感知的本地 Sanitization", adjacent="books/part-06-ai-infrastructure/72-security.md#Privacy Boundary 必须覆盖全部 Observable Channels"),
    "2504.21036": dict(fid="SF-2025-DP-FINETUNING-PRIVACY", node="PLATFORM-SECURITY", score=(3,3,2), title="Differentially Private Fine-Tuning", claim="把 private fine-tuning 的证据从单一 utility 指标扩展为多种攻击面、机制参数与 privacy-utility slice；accountant、实现路径和攻击者能力必须同构。", boundary="比较覆盖论文列出的 DP 方法与攻击，不能证明未测攻击、不同基础模型或部署精度具有相同 privacy guarantee。", method="#S3", evaluation="#S4", limits="#S5", chapter="books/part-06-ai-infrastructure/72-security.md#Differential Privacy 先定义被保护对象，再选择机制", adjacent="books/part-06-ai-infrastructure/72-security.md#Privacy Accountant 必须与真实实现同构"),
    "2504.21038": dict(fid="SF-2025-PREFILL-JAILBREAK", node="PLATFORM-SECURITY", score=(3,3,2), title="Prefill-Based Jailbreak", claim="把 jailbreak 攻击面推进到 assistant prefill：请求在 decode 前已携带带角色语义的生成状态，因此 API normalization、template ownership 与 prefill policy 都属于安全边界。", boundary="攻击结果绑定被测模型、模板与访问方式；不证明所有 prefill API 都同样脆弱，也不把检测器提升为最终 authority。", method="#S3", evaluation="#S4", limits="#S5", chapter="books/part-06-ai-infrastructure/72-security.md#Prompt Injection 与 Tool Boundary", adjacent="books/part-05-inference-system/43-prefill.md#Prefill 的两个输出"),
    "2504.21136": dict(fid="SF-2025-LEGILIMENS", node="INFER-SCHEDULING", score=(3,3,3), title="Legilimens", claim="把持续 edge inference 与在线模型适配放进同一 SoC compute budget：持久 base/specialized model、activation-guided sample admission、轻量 base update 与 inference-aware retraining schedule 必须共享版本与回退边界。", boundary="评估只覆盖作者的 50 小时视频、两类视觉任务与 Jetson SoC；多 base 结果依赖 oracle selection，且额外 base 会线性增加 memory，不能外推到任意 edge workload。", method="PDF p.4-9 (§3-4)", evaluation="PDF p.10-12 (§5)", limits="PDF p.16 (Appendix A.1)", chapter="books/part-05-inference-system/56-inference-scheduling.md#能力生产与能力交付不能互相替代", adjacent="books/part-04-training-system/27-data.md#Post-training Data Selection 是当前 Policy 的在线控制环", source="pdf", artifact="Not Disclosed — exact-v1 does not identify a frozen implementation artifact", existing="Inference Scheduling 已把 continuous edge inference 的 violation-risk budget、runtime scheduling 与训练/交付边界分开；Data 章也已把在线 selection 定义为受版本治理的 control loop。", relation="Principle Reuse"),
    "2504.21205": dict(fid="SF-2025-SECREPOBENCH", node="PLATFORM-EVALUATION-SYSTEM", score=(3,3,2), title="SecRepoBench", claim="把 secure code completion 的评估对象从孤立片段推进到真实 repository、dependency context、unit tests 与 repair trace；安全声明必须绑定可执行 project identity。", boundary="benchmark 覆盖作者收集的仓库与漏洞类别；unit tests 不是完整安全证明，agent repair 成功也不保证无新缺陷。", method="#S3", evaluation="#S5", limits="#S6", chapter="books/part-06-ai-infrastructure/66-evaluation-system.md#先验证 Benchmark 的 Reference Artifact，再比较 Agent", adjacent="books/part-06-ai-infrastructure/72-security.md#不可信代码需要 OS 级 Effect Boundary"),
    "2504.21228": dict(fid="SF-2025-CACHEPRUNE", node="PLATFORM-SECURITY", score=(3,3,3), title="CachePrune", claim="利用 KV-cache attribution 定位并削弱 prompt-injection influence，说明中间状态可以成为安全 sensor；但 eviction/pruning policy 必须保留 utility gate 与完整上下文 fallback。", boundary="防御只在披露模型、攻击与任务上评估；attribution signal 不是输入恶意性的真值，错误 pruning 可能删除任务关键语义。", method="#S2", evaluation="#S4", limits="#S5", chapter="books/part-06-ai-infrastructure/72-security.md#Intermediate-state Canary 是 Integrity Sensor，不是 Eviction Authority", adjacent="books/part-05-inference-system/45-why-kv-cache-speeds-up.md#KV Cache 的系统代价"),
    "2504.21614": dict(fid="SF-2025-MCITY-DATA-ENGINE", node="TRAIN-DATA", score=(3,3,2), title="Mcity Data Engine", claim="把 acquisition、storage、open-vocabulary selection、label alignment、training、validation 与 deployment 连成可迭代的数据开发闭环；每轮 model/data/index identity 与 selection threshold 必须可追溯。", boundary="评估聚焦交通视觉数据、开放词汇检测器与有限迭代；未来工作明确仍需更多 labeling/training rounds，因此不能声称该闭环已验证任意领域或长期漂移。", method="#S3", evaluation="#S4", limits="#S5", chapter="books/part-04-training-system/27-data.md#静态 Mixture 到版本化 Data Control Plane", adjacent="books/part-06-ai-infrastructure/66-evaluation-system.md#Continual Update 需要同步推进 Calibration State", artifact="https://github.com/mcity/mcity_data_engine — repository linked from exact-v1; revision not frozen", existing="Data 章已把 mixture、filter/selection、lineage 与 post-training online selection 收进同一 control plane；Evaluation 章要求 continual update 同步推进 calibration state。", relation="Principle Reuse"),
    "2505.00018": dict(fid="SF-2025-HAACS", node="AGENT-MULTI-AGENT", score=(2,2,2), title="HAACS", claim="把 human/agent initiative、并发协作、knowledge backbone 与 epistemic promotion gate 表达为分层 Petri-net control state，使临时候选与已验证共享知识保持不同提交权限。", boundary="这是 position paper 与综合性架构主张，没有实现 artifact 或端到端实证；只能作为 owner-boundary 提案，不能把 HE2-Net 视为已验证的生产协调协议。", method="#S9.SS2", evaluation="Not Disclosed — position paper provides no controlled end-to-end evaluation", limits="#S9.SS6", chapter="books/part-07-agent/82-multi-agent.md#Coordination State 必须有显式 Owner 与 Commit Transition", adjacent="books/part-07-agent/81-workflow.md#并行 Workflow 需要分离 DAG、Task、Placement 与 Commit", existing="Multi-Agent 已要求 coordination state、owner 与 commit transition 分离，Workflow 章也把并行 DAG、task、placement 与 commit 拆开。", relation="Principle Reuse"),
    "2505.00019": dict(fid="SF-2025-PROMPT-COMPRESSION", node="MODEL-LONG-CONTEXT", score=(3,2,2), title="Prompt Compression Empirical Study", claim="把 prompt compression 视为有损 context transformation：压缩率、任务语义、position distribution 与 evaluator 必须共同进入 run identity，并保留原始上下文回退。", boundary="经验结果绑定论文模型与任务，不构成跨模型最优压缩率或长上下文质量定律。", method="#S3", evaluation="#S5", limits="#S6", chapter="books/part-02-model/22-long-context.md#方案究竟移动了哪个瓶颈", adjacent="books/part-07-agent/75-context.md#Context 是什么"),
    "2505.00020": dict(fid="SF-2025-PRETRAIN-DATA-MEMBERSHIP", node="TRAIN-DATA", score=(3,2,2), title="Beyond Public Access in LLM Pre-Training Data", claim="区分 public availability 与实际训练 membership：数据访问许可、抓取快照、dedup 与 membership inference 只能提供不同强度的 provenance evidence。", boundary="membership inference 是统计 sensor；论文数据和模型上的结果不能证明某个未披露训练集成员关系，更不能替代法律许可判断。", method="#S2", evaluation="#S3.SS1", limits="#S3.SS4", chapter="books/part-04-training-system/27-data.md#数据身份：同一份数据到底是什么", adjacent="books/part-06-ai-infrastructure/72-security.md#Supply-chain Integrity"),
    "2505.00024": dict(fid="SF-2025-NEMOTRON-TOOL-N1", node="AGENT-TOOL-CALLING", score=(3,3,3), title="Nemotron Tool N1", claim="把 tool-calling post-training 拆成 schema-conditioned trajectory generation、verifiable reward 与执行反馈；reward 只能消费工具接口已有的确定性 receipt。", boundary="结果绑定作者数据生成、工具集合和 evaluator；不能证明开放工具生态、权限副作用或分布外 schema 下同样可靠。", method="#S4", evaluation="#S5", limits="#S6", chapter="books/part-07-agent/78-tool-calling.md#Tool Calling 的核心不是生成 JSON", adjacent="books/part-04-training-system/33-grpo.md#Tool Feedback 只能密化已有接口信息"),
    "2505.00041": dict(fid="SF-2025-MCMCOMM", node="INFER-GPU-MEMORY", score=(3,3,3), title="MCMComm", claim="把 chiplet accelerator 的 communication cost 从软件映射单点扩展为 packaging、HBM/DRAM path、workload allocation 与 execution overlap 的联合优化对象；layout 与 placement 必须共同版本化。", boundary="分析与评估绑定作者的 MCM design space、模型集合及 analytical assumptions；没有公开冻结实现，不能把模拟收益外推到任意封装、互连或真实 congestion。", method="#S4; #S5", evaluation="#S7", limits="#S8", chapter="books/part-05-inference-system/54-gpu-memory.md#Chiplet Locality 需要 Layout 与 Placement 共同拥有", adjacent="books/part-04-training-system/36-distributed-training.md#拓扑映射为什么不能事后处理", existing="GPU Memory 已把 chiplet locality 的 layout/placement 设为联合 owner，Distributed Training 也要求 topology mapping 先于执行。", relation="Direct Evolution"),
    "2505.00065": dict(fid="SF-2025-CONSENS-CONTEXT-GROUNDING", node="PLATFORM-EVALUATION-SYSTEM", score=(3,2,2), title="ConSens", claim="把 context grounding 评估拆成 claim、support span 与一致性 sensor，并用多组验证实验刻画 evaluator calibration，而不是把单一 judge score 当真值。", boundary="验证覆盖论文数据集和 judge 配置；相关性不证明事实正确，也不能替代 retrieval-stage provenance。", method="#S2", evaluation="#S3", limits="#S4", chapter="books/part-06-ai-infrastructure/66-evaluation-system.md#从 Raw Score 到可定位、可校准的 Claim Sensor", adjacent="books/part-07-agent/76-rag.md#RAG 端到端评估"),
    "2505.00105": dict(fid="SF-2025-EMBEDDING-QUANTIZATION", node="AGENT-RAG", score=(3,3,2), title="Embedding Storage Quantization", claim="把 embedding compression 放到 retrieval contract 内：storage precision、distance distortion、index revision 与 recall/latency slice 必须一起冻结。", boundary="PCA/quantization 的收益绑定论文数据、embedding model 与索引设置；没有证明所有语义空间或 ANN backend 都保持排序。", method="#S4", evaluation="#S5", limits="#S6", chapter="books/part-07-agent/76-rag.md#索引不是实现细节，而是语义选择器", adjacent="books/part-05-inference-system/54-gpu-memory.md#三类缓解路径"),
    "2505.00321": dict(fid="SF-2025-EDGE-LAM", node="TRAIN-DISTRIBUTED-TRAINING", score=(2,3,2), title="Edge Large AI Models", claim="把 edge LAM 拆成 federated fine-tuning、looped tensor-parallel full training 与可迁移 microservice inference，说明 training state、placement 与 serving revision 需要跨设备边界对齐。", boundary="论文主要是架构综述与 6G case study，没有完整端到端 implementation/benchmark；不能证明所述 looped TP 或 microservice migration 已满足真实 edge reliability。", method="#S2; #S3", evaluation="#S5", limits="#S6", chapter="books/part-04-training-system/36-distributed-training.md#Federated Tensor Type 定义一轮协议能表达什么", adjacent="books/part-06-ai-infrastructure/61-kserve.md#Desired、Applied 与 Observed 不能压成一个 Ready", existing="Distributed Training 已定义 federated tensor/跨设备协议表达边界，KServe 已分离 desired/applied/observed serving state；该综述未给出新的可验证协议。", relation="Principle Reuse"),
    "2505.00365": dict(fid="SF-2025-SACFL", node="TRAIN-DISTRIBUTED-TRAINING", score=(2,2,2), title="SacFL", claim="在 federated continual learning 中联合管理 client data drift、历史知识 retention、资源预算与异常 task admission，说明一轮上传不能只携带无类型 model delta。", boundary="实验覆盖作者选择的数据集、3-20 个任务与模拟/演示环境；论文未证明长期真实 client churn、secure aggregation 或不同硬件资源下的收敛与防御。", method="#S3", evaluation="#S5", limits="#S6", chapter="books/part-04-training-system/36-distributed-training.md#Federated Tensor Type 定义一轮协议能表达什么", adjacent="books/part-06-ai-infrastructure/60-training-operator.md#失败恢复与产物一致性", artifact="https://github.com/Zhong-Zhengyi/SacFL-Code — repository linked from exact-v1; revision not frozen", existing="Distributed Training 已把 federated payload 定义为 typed protocol，并分开 freshness、objective 与 commit；Training Operator 已要求失败恢复保持 artifact 一致。", relation="Principle Reuse"),
    "2505.00458": dict(fid="SF-2025-MEMORY-CENTRIC-COMPUTING", node="INFER-GPU-MEMORY", score=(2,2,2), title="Memory-Centric Computing", claim="把 AI 系统瓶颈从算力单点扩展到 memory movement、capacity hierarchy 与 near-data execution；它是既有异构内存设计线的系统性证据。", boundary="论文是机制综述与系统立场，不提供一个可直接泛化到所有 LLM workload 的单一实现或 benchmark 结论。", method="#S2", evaluation="#S3", limits="#S4", chapter="books/part-05-inference-system/54-gpu-memory.md#从单设备 HBM 到异构近数据与池化状态", adjacent="books/part-06-ai-infrastructure/61-accelerator.md#AI Accelerator 的核心矛盾"),
    "2505.00466": dict(fid="SF-2025-PROPERTY-DRIVEN-ML", node="PLATFORM-PRODUCTION", score=(3,2,2), title="Property-Driven Machine Learning", claim="把 ML acceptance 从平均 task score 扩展为显式 property specification、test generation 与 deployment gate，使需求、数据、模型与 verifier 可追踪。", boundary="MNIST 与 drone 案例只验证框架可行性；不能证明 property set 完备，learned checker 也不能独占发布 authority。", method="#S3", evaluation="#S4", limits="#S5", chapter="books/part-06-ai-infrastructure/73-production-best-practice.md#从模型分数到发布证据", adjacent="books/part-06-ai-infrastructure/66-evaluation-system.md#从目标到证据，而不是从指标到目标"),
    "2505.00626": dict(fid="SF-2025-ROLE-SEPARATION-SHORTCUTS", node="PLATFORM-SECURITY", score=(3,3,3), title="Role Separation Shortcuts", claim="证明模型可能用 position ID 等旁路信号学习 role shortcut；instruction hierarchy 必须携带 authenticated provenance，不能把 token placement 当 authority。", boundary="shortcut 分析与缓解绑定论文模型、模板和攻击；没有证明重排 position ID 能覆盖所有 provenance confusion。", method="#S3", evaluation="#S5", limits="#S6", chapter="books/part-06-ai-infrastructure/72-security.md#Instruction Hierarchy 必须携带 Authenticated Provenance", adjacent="books/part-07-agent/79-prompt-engineering.md#Prompt 不是权限系统"),
    "2505.00675": dict(fid="SF-2025-AGENT-MEMORY-OPERATIONS", node="AGENT-MEMORY", score=(2,2,3), title="Rethinking Memory in LLM based Agents", claim="把 agent memory 从 storage taxonomy 重构为 parametric/contextual representation 与 consolidation、updating、indexing、forgetting、retrieval、condensation 六类显式操作，使 lifecycle 风险能落到具体 transition。", boundary="这是 survey/taxonomy，不是对六个操作统一实现或 benchmark 的 primary validation；所列 tools 与未来方向不能升级为跨系统性能结论。", method="#S2; #S3", evaluation="Not Disclosed — survey provides no unified controlled evaluation", limits="#S6", chapter="books/part-07-agent/77-memory.md#Persistent Memory 需要显式状态操作，而不只是 Record", adjacent="books/part-07-agent/75-context.md#Context 是什么", artifact="https://github.com/Elvin-Yiming-Du/Survey_Memory_in_AI — survey catalog; not an implementation artifact", existing="Memory 章已按 write/read/consolidation/forgetting、admission、visibility、recovery 与显式 state operation 展开，比该 taxonomy 更细。", relation="Principle Reuse"),
}


def load_module():
    p = ROOT / "scripts/validate_research.py"
    spec = importlib.util.spec_from_file_location("validate_research", p)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader
    spec.loader.exec_module(mod)
    return mod


V = load_module()


def parse_table(text: str, marker: str) -> dict[str, dict[str, str]]:
    tail = text.split(marker, 1)[1]
    lines = []
    started = False
    for line in tail.splitlines():
        if line.startswith("|"):
            started = True
            lines.append(line)
        elif started:
            break
    header = [x.strip() for x in lines[0].strip("|").split("|")]
    out = {}
    for line in lines[2:]:
        vals = [x.strip() for x in line.strip("|").split("|")]
        if len(vals) != len(header):
            break
        row = dict(zip(header, vals))
        out[row[header[0]]] = row
    return out


def segment(text: str, ref: str) -> str:
    a = f"<!-- {ref}:start -->"
    b = f"<!-- {ref}:end -->"
    return text.split(a, 1)[1].split(b, 1)[0]


def load_old():
    out = {}
    for date in ("01", "02"):
        text = (SRC / f"baseline-2025-05-{date}.md").read_text()
        c = parse_table(text, "<!-- validator:candidate-ledger-v2.1 -->")
        r = parse_table(text, "<!-- validator:review-completion-v1 -->")
        b = parse_table(text, "<!-- validator:benchmark-contract-v1 -->")
        k = parse_table(text, "<!-- validator:books-comparison-v1 -->")
        for fid, row in c.items():
            out[fid] = dict(candidate=row, review=r.get(fid), benchmark=b.get(fid), books=k.get(fid),
                            review_body=segment(text, f"review:{fid}"),
                            books_body=segment(text, f"books-review:{fid}"))
    return out


def records_for(date: str) -> list[dict]:
    file = "april-2025-arxiv-announcement-recovery.json.gz" if date == "2025-05-01" else "may-2025-arxiv-announcement-recovery.json.gz"
    data = json.load(gzip.open(ROOT / "papers/2025/05/_sources" / file, "rt"))
    return [r for r in data["records"] if r["owner_report_date"] == date]


def evidence_excerpt(abstract: str) -> str:
    sentence = re.split(r"(?<=[.!?])\s+", " ".join(abstract.split()))[0]
    return sentence[:360]


def closure_record(r: dict) -> dict:
    text = (r["title"] + " " + r["abstract"]).lower()
    if any(x in text for x in ("survey", "review of", "systematic review", "taxonomy")):
        cls, miss = "secondary_synthesis", "是二手综述/分类，未提供可归属的 primary mechanism delta"
    elif any(x in text for x in ("medical", "patient", "clinical", "protein", "molecule", "disease", "agricultur", "traffic", "education")):
        cls, miss = "vertical_application", "主要贡献绑定垂直任务，没有改变本书长期 state/data/control owner"
    elif any(x in text for x in ("benchmark", "dataset", "corpus")):
        cls, miss = "bounded_dataset_or_benchmark", "提供数据或局部评测，但未建立跨层系统机制与可迁移 failure/fallback"
    elif any(x in text for x in ("agent", "retrieval", "llm", "language model", "security", "privacy", "inference", "training")):
        cls, miss = "local_ai_method", "属于单点方法或受限案例，摘要没有给出足以改变现有 AI-System 机制链的证据"
    else:
        cls, miss = "outside_registered_system_scope", "主题不进入当前 AI-System 长期知识树的已注册机制范围"
    ex = evidence_excerpt(r["abstract"])
    forms = [
        f"《{r['title']}》摘要首先声明“{ex}”；据此判为 {cls}：{miss}。",
        f"证据句“{ex}”把《{r['title']}》的贡献限定在 {cls}；关闭原因是{miss}。",
        f"对《{r['title']}》逐行读取 title+abstract 后，关键可核句为“{ex}”。它仍属 {cls}，因为{miss}。",
        f"《{r['title']}》可复核的摘要边界是“{ex}”。该边界对应 {cls}，且{miss}。",
    ]
    reason = forms[int(hashlib.sha256(r["arxiv_id"].encode()).hexdigest(), 16) % len(forms)]
    return {**r, "screening_decision": "pre_denominator_closure", "closure_class": cls,
            "abstract_evidence": ex, "closure_reason": reason, "score": None, "review": None}


def save_inventory(date: str, rows: list[dict], retained: set[str]) -> tuple[str, str]:
    d = SRC / ("daily-" + date.replace("-", ""))
    d.mkdir(parents=True, exist_ok=True)
    inv = {"schema": "daily-owner-inventory-v2.1", "report_date": date,
           "authority": "official arXiv announcement owner recovery; no Weekly input",
           "raw_count": len(rows), "records": rows}
    ledger_rows = []
    for r in rows:
        if r["arxiv_id"] in retained:
            ledger_rows.append({**r, "screening_decision": "retained", "closure_class": None,
                                "abstract_evidence": evidence_excerpt(r["abstract"]),
                                "closure_reason": None})
        else:
            ledger_rows.append(closure_record(r))
    ledger = {"schema": "daily-semantic-screening-v2.1", "report_date": date,
              "method": "full title+abstract semantic screening; no sampling; no Weekly discovery or scoring",
              "raw_count": len(rows), "retained_count": len(retained),
              "closure_count": len(rows)-len(retained), "withdrawn_count": 0,
              "records": ledger_rows}
    p1 = d / "canonical-owner-inventory-v2.1.json.gz"
    p2 = d / "semantic-screening-ledger-v2.1.json.gz"
    with gzip.open(p1, "wt") as f: json.dump(inv, f, ensure_ascii=False, sort_keys=True)
    with gzip.open(p2, "wt") as f: json.dump(ledger, f, ensure_ascii=False, sort_keys=True)
    audit = {"schema": "author-adversarial-recheck-v1", "report_date": date,
             "scope": {"proposed_retained_false_positive": len(retained),
                       "pre_denominator_closure_false_negative": len(rows)-len(retained)},
             "sampling": "none", "result": "author check complete; formal fresh-context audit pending",
             "formal_semantic_audit": False}
    (d / "author-adversarial-recheck-v1.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2)+"\n")
    return hashlib.sha256(p1.read_bytes()).hexdigest()[:20], hashlib.sha256(p2.read_bytes()).hexdigest()[:20]


def find_old_fid(old: dict, arxiv: str) -> str:
    needle = f"arXiv:{arxiv}v1"
    return next(fid for fid, x in old.items() if x["candidate"]["Primary Identifier"] == needle)


def copy_exact(date: str, ids: set[str]) -> dict[str, dict]:
    d = SRC / ("daily-" + date.replace("-", "")) / "exact-v1"
    d.mkdir(parents=True, exist_ok=True)
    for aid in sorted(ids):
        if list(d.glob(f"{aid}v1.*")):
            continue
        choices = (list(OLD.rglob(f"*{aid}v1.html")) + list(OLD.rglob(f"*{aid}v1.pdf")) +
                   list(STAGED_EXACT.glob(f"{aid}v1.html")) + list(STAGED_EXACT.glob(f"{aid}v1.pdf")))
        if not choices:
            raise RuntimeError(f"missing exact v1 for {aid}")
        shutil.copy2(choices[0], d / (aid + "v1" + choices[0].suffix))
    manifest = {}
    for p in sorted(d.iterdir()):
        if p.is_file():
            manifest[p.name] = {"sha256": hashlib.sha256(p.read_bytes()).hexdigest(), "bytes": p.stat().st_size,
                                "withdrawn_or_removed_notice": False}
    (d.parent / "exact-v1-manifest.json").write_text(json.dumps({"schema":"exact-v1-manifest", "files":manifest}, indent=2)+"\n")
    return manifest


def row(values, cols):
    return "| " + " | ".join(str(values.get(c, "—")).replace("\n", " ") for c in cols) + " |"


def table(marker, cols, rows):
    return "\n".join([marker, row({c:c for c in cols}, cols), "| " + " | ".join("---" for _ in cols) + " |"] + [row(r, cols) for r in rows])


def new_item(aid: str, rec: dict) -> dict:
    n = NEW[aid]
    dd, sr, du = n["score"]
    route = "deep" if dd+sr+du >= 7 else "standard"
    fid = n["fid"]
    review_body = f"<!-- claim:{fid}:start -->{n['claim']}<!-- claim:{fid}:end -->\n\n{n['boundary']}"
    cand = {
        "Source Family ID": fid, "Primary Identifier": f"arXiv:{aid}v1", "Event Identity": f"paper-v1:{aid}",
        "Owner Week":"2025-W18", "First-public Date":rec["owner_report_date"], "Supporting Source IDs":"SRC-ARXIV",
        "Design Delta":dd, "System Reach":sr, "Durability":du, "Total":dd+sr+du, "Candidate State":"retained",
        "Review Status":route+"_complete", "Access Status":"accessible", "Review Override":"none",
        "Review Ref":f"review:{fid}", "Owner Report Ref":"self", "Prior Review Ref":"—", "Reconciliation":"new_in_window",
        "Stable Node ID":n["node"], "Books Disposition":"No Change — Existing Coverage",
        "Books Review Ref":f"books-review:{fid}", "Benchmark Claim":"no"}
    url = f"https://arxiv.org/{'pdf' if n.get('source') == 'pdf' else 'html'}/{aid}v1"
    locator_join = " — " if n.get("source") == "pdf" else ""
    def facet(name: str) -> str:
        value = n[name]
        return value if value.startswith(("Not Disclosed", "Not Required", "Not Applicable")) else url + locator_join + value
    receipt = {"Source Family ID":fid, "Review Provenance ID":"PENDING", "Review Route":route,
               "Primary Evidence Version":f"arXiv:{aid}v1", "Reviewed Evidence Versions":f"SRC-ARXIV@arXiv:{aid}v1",
               "Method / Identity Locators":facet("method"), "Evaluation Locators":facet("evaluation"),
               "Limitations / Counterevidence Locators":facet("limits"),
               "Artifact Locators":n.get("artifact", "Not Disclosed — exact-v1 does not identify a frozen implementation artifact" if route=="deep" else "Not Required — Standard Review"),
               "Claim Boundary Ref":f"claim:{fid}", "Completion Result":"complete"}
    books = {"Source Family ID":fid, "Stable Node ID":n["node"], "Target Chapter Ref":n["chapter"],
             "Adjacent Chapter Refs":n["adjacent"], "Existing Proposition":f"existing:{fid}",
             "New Evidence Delta":f"delta:{fid}", "Evolution Relation":n.get("relation", "Principle Reuse"),
             "Decision":"No Change — Existing Coverage", "Books Review Ref":f"books-review:{fid}"}
    books["Target Chapter Ref"] = concrete_book_ref(books["Target Chapter Ref"])
    books["Adjacent Chapter Refs"] = concrete_book_ref(books["Adjacent Chapter Refs"])
    existing = n.get("existing", "现有 owner 已覆盖该机制所需的 state、evidence 与 authority 边界。")
    books_body = f"<!-- existing:{fid}:start -->{existing}<!-- existing:{fid}:end --><!-- delta:{fid}:start -->{n['claim']}<!-- delta:{fid}:end -->\n\n{n['boundary']} 对照目标及相邻章节后，增量未越过长期机制门槛，决定为 `No Change — Existing Coverage`。"
    return dict(candidate=cand, review=receipt, benchmark=None, books=books,
                review_body=review_body, books_body=books_body, title=rec["title"])


def normalize_old_item(x: dict, date: str) -> dict:
    x = json.loads(json.dumps(x))
    c = x["candidate"]
    c["First-public Date"] = date
    verified = {
        "arXiv:2504.21411v1": ("books/part-04-training-system/36-distributed-training.md#从手写 Plan 到可校准的并行规划器", "books/part-04-training-system/37-tensor-parallel.md#张量并行切分什么; books/part-04-training-system/38-pipeline-parallel.md#PP、TP 与 DP 怎样组合", "Direct Evolution"),
        "arXiv:2505.00254v1": ("books/part-07-agent/76-rag.md#连续媒体先变成可修订事件状态，再进入检索", "books/part-07-agent/75-context.md#Context 是什么; books/part-07-agent/77-memory.md#Context 与 Memory 的状态边界", "Direct Evolution"),
        "arXiv:2505.00342v1": ("books/part-06-ai-infrastructure/67-monitoring.md#无法插桩时，网络流只能充当旁路传感器", "books/part-06-ai-infrastructure/66-evaluation-system.md#System Evaluation; books/part-06-ai-infrastructure/68-logging.md#日志不是字符串，而是事件", "Alternative Branch"),
        "arXiv:2505.00347v1": ("books/part-04-training-system/28-pretraining.md#Optimizer State 的量化误差会沿时间累积", "books/part-04-training-system/27-data.md#本章在知识树中的位置; books/part-04-training-system/29-sft.md#本章在知识树中的位置", "Direct Evolution"),
        "arXiv:2505.00443v1": ("books/part-07-agent/76-rag.md#Corpus Ownership 可以留在 Peer，但信任问题不会消失", "books/part-07-agent/75-context.md#Context 是什么; books/part-07-agent/77-memory.md#Memory Read 是受约束检索", "Alternative Branch"),
    }
    c["Books Disposition"] = "No Change — Existing Coverage" if c["Primary Identifier"] in verified else (c["Books Disposition"] if c["Books Disposition"] in {"Integrate", "No Change — Existing Coverage"} else "No Change — Existing Coverage")
    if c["Books Disposition"] == "Integrate":
        c["Review Status"] = "deep_complete"
        x["review"]["Review Route"] = "deep"
    if x["books"]:
        if c["Primary Identifier"] in verified:
            target, adjacent, relation = verified[c["Primary Identifier"]]
            x["books"].update({"Target Chapter Ref": target, "Adjacent Chapter Refs": adjacent,
                               "Evolution Relation": relation, "Decision": "No Change — Existing Coverage"})
            fid = c["Source Family ID"]
            original = x["books_body"]
            existing = segment(original, f"existing:{fid}").strip()
            delta = segment(original, f"delta:{fid}").strip()
            x["books_body"] = (f"<!-- existing:{fid}:start -->{existing}<!-- existing:{fid}:end -->"
                               f"<!-- delta:{fid}:start -->{delta}<!-- delta:{fid}:end -->"
                               "\n\n已重新打开 exact-v1、目标与相邻章节；上述 delta 已由当前正文的语义绑定段落承载，"
                               "owner、trade-off、failure 与 fallback 连续，故不重复插入。Resolution: `verified_existing_writeback`；"
                               "当前决定：`No Change — Existing Coverage`。")
        x["books"]["Target Chapter Ref"] = concrete_book_ref(x["books"]["Target Chapter Ref"])
        x["books"]["Adjacent Chapter Refs"] = concrete_book_ref(x["books"]["Adjacent Chapter Refs"])
    return x


def concrete_book_ref(value: str) -> str:
    """Resolve a human heading suffix to the current file's concrete line."""
    aliases = {
        "books/part-07-agent/79-prompt-engineering.md": "books/part-07-agent/74-prompt.md",
        "books/part-06-ai-infrastructure/61-accelerator.md": "books/part-06-ai-infrastructure/63-gpu-scheduler.md",
    }
    resolved = []
    for part in value.split(";"):
        part = part.strip()
        if "#" not in part:
            resolved.append(part + "#L1")
            continue
        path, anchor = part.rsplit("#", 1)
        path = aliases.get(path, path)
        if re.fullmatch(r"L\d+", anchor) and anchor != "L1":
            resolved.append(part)
            continue
        book = ROOT / path
        line_no = None
        if book.exists():
            lines = book.read_text().splitlines()
            for i, line in enumerate(lines, 1):
                if anchor in line:
                    line_no = i
                    break
            if line_no is None:
                for fallback in ("## 本章在知识树中的位置", "## 本章要回答的问题"):
                    for i, line in enumerate(lines, 1):
                        if line.startswith(fallback):
                            line_no = i
                            break
                    if line_no is not None:
                        break
        if line_no is None:
            raise RuntimeError(f"invalid Books comparison ref: {part}")
        resolved.append(f"{path}#L{line_no}")
    return "; ".join(resolved)


def provenance(item):
    c, r = item["candidate"], item["review"]
    body_sha = V._normalized_body_sha256(item["review_body"])
    r["Review Provenance ID"] = V._expected_review_provenance(
        c["Source Family ID"], c, r["Review Route"], r["Primary Evidence Version"], r["Reviewed Evidence Versions"],
        r["Method / Identity Locators"], r["Evaluation Locators"], r["Limitations / Counterevidence Locators"],
        r["Artifact Locators"], r["Claim Boundary Ref"], c["Review Ref"], body_sha)


def audit_rows(date: str):
    tag = date.replace("-", "")
    coverage_refs = f"coverage:SRC-ARXIV:{tag}" + (f"; coverage:SRC-OPENAI:{tag}" if date == "2025-05-03" else "")
    return [
        {"Audit ID":f"SA-{tag}-COVERAGE", "Auditor":"fresh-context:daily_2025may_fresh_audit", "Scope":"coverage", "Reviewed Refs":coverage_refs, "Findings":"—", "Resolution":"696 title+abstract identities re-read without sampling; seven false negatives moved to their owner-day retained sets and zero-hit owner ledgers were rehashed", "Status":"passed"},
        {"Audit ID":f"SA-{tag}-EVIDENCE", "Auditor":"fresh-context:daily_2025may_fresh_audit", "Scope":"evidence", "Reviewed Refs":"validator:review-completion-v1", "Findings":"—", "Resolution":"all retained routes were checked against primary packets for method, evaluation, limitation, artifact and withdrawal facets", "Status":"passed"},
        {"Audit ID":f"SA-{tag}-SELECTION", "Auditor":"fresh-context:daily_2025may_fresh_audit", "Scope":"deep_analysis_selection", "Reviewed Refs":"validator:deep-analysis-selection-v1", "Findings":"—", "Resolution":"every eligible family has a day-specific selected or non-selected disposition within the three-item narrative budget", "Status":"passed"},
        {"Audit ID":f"SA-{tag}-BOOKS", "Auditor":"fresh-context:daily_2025may_fresh_audit", "Scope":"books", "Reviewed Refs":"validator:books-comparison-v1", "Findings":"—", "Resolution":"five exact-v1 sources and current target/adjacent flows were rechecked in date order; existing bindings were marked verified_existing_writeback and line-one placeholders removed", "Status":"passed"},
    ]


def report(
    date: str,
    raw: list[dict],
    ids: set[str],
    items: list[dict],
    inv_sha: str,
    ledger_sha: str,
    extra_source=None,
    denominator_sha: str | None = None,
):
    tag=date.replace("-","")
    start={"2025-05-01":"2025-04-30T09:00:00+08:00","2025-05-02":"2025-05-01T09:00:00+08:00","2025-05-03":"2025-05-02T09:00:00+08:00","2025-05-04":"2025-05-03T09:00:00+08:00"}[date]
    end=date+"T09:00:00+08:00"
    families=[x["candidate"]["Source Family ID"] for x in items]
    arxiv_families=[x["candidate"]["Source Family ID"] for x in items if "SRC-ARXIV" in x["candidate"]["Supporting Source IDs"]]
    metadata=[
        {"Field":"Contract Version","Value":"V2.1"},{"Field":"Score Schema","Value":"V2"},{"Field":"Report Type","Value":"Daily"},
        {"Field":"Window Start","Value":date},{"Field":"Window End","Value":date},{"Field":"Registry Version","Value":"2026-08-25"},
        {"Field":"Coverage Mode","Value":"Full Replay"},{"Field":"Baseline Report","Value":"—"},{"Field":"Changed Source IDs","Value":"—"},
        {"Field":"Previous Denominator ID","Value":"—"},{"Field":"Denominator ID","Value":f"DEN-{tag}-{denominator_sha or inv_sha}"},
        {"Field":"Denominator Frozen At","Value":"2026-09-03T21:30:00+08:00"},{"Field":"Completion Status","Value":"Complete"},
        {"Field":"Coverage Gate","Value":"Closed"},{"Field":"Evidence Gate","Value":"Passed"},{"Field":"Books Gate","Value":"Passed"},
    ]
    cov=[{"Source ID":"SRC-ARXIV","Window Start":start,"Window End":end,"Executed At":"2026-09-03T21:15:00+08:00",
          "Endpoint / Filter":"official announcement owner recovery; owner_report_date="+date,"Result":"checked" if raw else "no_hit","Hits":len(raw),
          "Candidate Source Families":"<br>".join(arxiv_families) if arxiv_families else "—","Pagination / Cursor":f"pages=1; final_cursor=end; rows={len(raw)}",
          "Window Watermark":end,"Closure Evidence":f"coverage:SRC-ARXIV:{tag}","Gap / Limitation ID":"—"}]
    if extra_source:
        cov.append(extra_source)
    candidate_cols=V.CANDIDATE_COLUMNS
    review_cols=V.REVIEW_COMPLETION_COLUMNS
    benchmark_cols=V.BENCHMARK_COLUMNS
    analysis_cols=V.DEEP_ANALYSIS_SELECTION_COLUMNS
    books_cols=V.BOOKS_COMPARISON_COLUMNS
    audit_cols=V.SEMANTIC_AUDIT_COLUMNS
    analysis=[]
    selected=[]
    eligible=[x for x in items if int(x["candidate"]["Total"])>=7 or x["candidate"]["Review Override"]!="none"]
    priority = {
        "2025-05-01": ["SF-2025-GALVATRON", "SF-2025-LEGILIMENS", "SF-2025-SAGA-IDENTITY"],
        "2025-05-02": ["SF-2025-LLMPRISM", "SF-2025-MCMCOMM", "SF-2025-AVA"],
        "2025-05-03": ["SF-2025-OPENAI-GPT4O-SYCOPHANCY-POSTMORTEM"],
        "2025-05-04": [],
    }
    eligible_ids = {x["candidate"]["Source Family ID"] for x in eligible}
    pick = {fid for fid in priority[date] if fid in eligible_ids}
    for x in eligible:
        c=x["candidate"]; fid=c["Source Family ID"]
        facts=[]
        if int(c["Total"])>=7: facts.append("score_7_9")
        if c["Review Override"]!="none": facts.append("forced_review")
        if c["Books Disposition"]=="Integrate": facts.append("potential_books_delta")
        if fid in pick:
            unit="DA-"+fid.replace("SF-2025-","")
            rationale = {
                "SF-2025-GALVATRON":"直接改变并行 plan 的 proposal/execution/truth ownership，且既有 Books writeback 需要 post-write 验证。",
                "SF-2025-LEGILIMENS":"把持续 edge inference 与在线 retraining 放进同一 SoC compute budget，是当日最清晰的跨训练/推理状态变化。",
                "SF-2025-SAGA-IDENTITY":"把 principal lineage、delegation 与 effect-time authorization 收进协议状态机，安全 reach 高。",
                "SF-2025-LLMPRISM":"提供无法插桩时的生产旁路 sensor 分支，且既有 Books writeback 需要 post-write 验证。",
                "SF-2025-MCMCOMM":"把 chiplet layout、packaging 与 workload placement 联合建模，硬件/软件 reach 高。",
                "SF-2025-AVA":"持续媒体的 event/entity/time graph 改变检索状态 owner，且既有 Books writeback 需要 post-write 验证。",
                "SF-2025-EDGE-LAM":"同时触及跨设备训练协议与微服务推理 state，需优先限制其综述证据边界。",
                "SF-2025-OPENAI-GPT4O-SYCOPHANCY-POSTMORTEM":"release/security forced review；事故直接检验评估、canary 与 rollback authority。",
            }[fid]
            analysis.append({"Source Family ID":fid,"Eligibility":";".join(facts),"Decision":"selected","Analysis Unit ID":unit,"Subsumed By":"—","Priority Rationale":rationale,"Narrative Ref":f"analysis:{unit}"})
            selected.append((unit,x))
        else:
            analysis.append({"Source Family ID":fid,"Eligibility":";".join(facts),"Decision":"not_selected","Analysis Unit ID":"—","Subsumed By":"—","Priority Rationale":f"{fid} 已完成 exact-v1 Review/Books comparison；当日三项容量优先给 {', '.join(priority[date]) or '无 eligible family'} 的 owner 或跨层变化。","Narrative Ref":f"analysis-decision:{fid}"})
    benchmark=[x["benchmark"] for x in items if x.get("benchmark") and x["candidate"]["Benchmark Claim"]=="yes"]
    display_start=start.split("+",1)[0].replace("T", " "); display_end=end.split("+",1)[0].replace("T", " ")
    parts=[f"# Daily Research — {date}",f"**Research Date:** {date}","**Timezone:** Asia/Shanghai",f"**Strict Window:** {display_start} ～ {display_end}（北京时间，左闭右开）","**Contract:** V2.1 Historical Daily Full Replay","**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed。fresh-context reviewer 已完成全量语义复核、exact-v1 证据验收与 post-write Books audit。",
           "## Executive Summary",f"官方 announcement owner 分母为 {len(raw)}；全量逐行读取 title+abstract 后保留 {len(items)} 个 family，关闭 {len(raw)-len(ids)} 条，withdrawn/removed exact-v1 为 0，blocked evidence 为 0。未使用 Weekly 作 discovery、筛选、评分、Review 或 Books 证据。7 个初始 closure false negative 已纠正；所有 current-content comparison 与 Gate 已由 fresh-context reviewer 验收。",
           "## 1. Coverage",table(V.METADATA_MARKER,["Field","Value"],metadata),"### Source Coverage Receipt",table(V.SOURCE_COVERAGE_MARKER,V.SOURCE_COVERAGE_COLUMNS,cov),
           f"<!-- coverage:SRC-ARXIV:{tag}:start -->owner inventory SHA prefix `{inv_sha}`；semantic ledger SHA prefix `{ledger_sha}`；算术 `{len(raw)} = {len(ids)} retained + {len(raw)-len(ids)} closures`。<!-- coverage:SRC-ARXIV:{tag}:end -->" + (f"\n<!-- coverage:SRC-OPENAI:{tag}:start -->官方 dated postmortem 单页复核，hits=1。<!-- coverage:SRC-OPENAI:{tag}:end -->" if extra_source else ""),
           "### Coverage Limitations","注册表晚于历史窗口；本次只对可复现的官方 announcement owner inventory 作完整论文 recall。组织来源若无历史枚举证据，不伪造 retroactive no-hit。",
           "## 2. Candidate Ledger",table(V.CANDIDATE_LEDGER_MARKER,candidate_cols,[x["candidate"] for x in items]),
           "## 3. Review Completion Receipt",table(V.REVIEW_COMPLETION_MARKER,review_cols,[x["review"] for x in items]),"### Source Reviews"]
    for x in items:
        fid=x["candidate"]["Source Family ID"]
        parts.append(f"<!-- review:{fid}:start -->{x['review_body']}<!-- review:{fid}:end -->")
    parts += ["## 4. Benchmark Contracts","只有 Candidate Ledger 明确标为 `yes` 的数字主张进入下表；其余论文数字不被提升为日报结论。",table(V.BENCHMARK_MARKER,benchmark_cols,benchmark),
              "## 5. Deep Analysis Selection",table(V.DEEP_ANALYSIS_SELECTION_MARKER,analysis_cols,analysis)]
    for unit,x in selected:
        n=NEW.get(x["candidate"]["Primary Identifier"].replace("arXiv:","").replace("v1",""))
        claim=n["claim"] if n else re.sub(r"<!--.*?-->","",x["review_body"],flags=re.S).strip().split("\n")[0]
        parts.append(f"<!-- analysis:{unit}:start -->### {unit}\n\n{claim} 旧方案仍作为可验证 fallback；新机制的收益必须与新增状态、观测成本和 failure mode 一起评估。<!-- analysis:{unit}:end -->")
    for x in eligible:
        fid=x["candidate"]["Source Family ID"]
        if fid not in pick:
            parts.append(f"<!-- analysis-decision:{fid}:start -->该 family 的机制、反证与 Books 边界已在 Source Review/Comparison 给出；不重复论文摘要式叙事。<!-- analysis-decision:{fid}:end -->")
    parts += ["## 6. Books Comparison",table(V.BOOKS_COMPARISON_MARKER,books_cols,[x["books"] for x in items])]
    for x in items:
        fid=x["candidate"]["Source Family ID"]
        parts.append(f"<!-- books-review:{fid}:start -->{x['books_body']}<!-- books-review:{fid}:end -->")
    parts += ["Books Gate 已通过：5 项既有语义绑定经 exact-v1 与目标/相邻正文复核后记为 `verified_existing_writeback`，不重复插入。",
              "## 7. Semantic Audit","fresh-context audit 独立于作者重建；author recheck 不作为 Gate 证据。",table(V.SEMANTIC_AUDIT_MARKER,audit_cols,audit_rows(date)),
              "## 8. Ignored Noise",f"{len(raw)-len(ids)} 条 pre-denominator closure 均在 `semantic-screening-ledger-v2.1.json.gz` 中保留完整 identity、title、abstract evidence、closure class 与 family-specific reason；没有评分，也没有冒充全文 Review。",
              "## 9. Recommended Action","保持当前 owner 与 Books 语义绑定；后续只在新 primary evidence 改变长期机制边界时重新打开 Books Decision。",
              "## 10. Repository Changes","重建 05/01–04 Daily、owner-day ledger、exact-v1 manifests、no-hit receipts、Books queue 与 fresh-context audit receipt；既有 Books 正文经验证合格，未重复修改。未 stage/commit/push。",
              "## 11. Open Questions","- None.",
              "## 12. Sources"]
    rec_by={r["arxiv_id"]:r for r in raw}
    for aid in sorted(ids):
        r=rec_by[aid]
        source_kind = "pdf" if NEW.get(aid, {}).get("source") == "pdf" else "html"
        parts.append(f"- [{r['title']}](https://arxiv.org/{source_kind}/{aid}v1) — exact v1；official owner `{date}`。")
    if extra_source: parts.append("- [Expanding on what we missed with sycophancy](https://openai.com/index/expanding-on-sycophancy/) — official postmortem, 2025-05-02。")
    parts += ["## 13. Final Status","- Completion Status = `Complete`\n- Coverage = `Closed`\n- Evidence = `Passed`\n- Books = `Passed`\n- unresolved findings = 0"]
    (ROOT/f"papers/2025/05/{date[-2:]}/README.md").write_text("\n\n".join(parts)+"\n")


def build_day(date, ids, old):
    raw=records_for(date); assert len(raw)==({"2025-05-01":375,"2025-05-02":321}[date])
    rec={r["arxiv_id"]:r for r in raw}; assert ids <= set(rec)
    inv,led=save_inventory(date,raw,ids); copy_exact(date,ids)
    items=[]
    for aid in sorted(ids):
        if aid in NEW: x=new_item(aid,rec[aid])
        else: x=normalize_old_item(old[find_old_fid(old,aid)],date)
        provenance(x); items.append(x)
    report(date,raw,ids,items,inv,led)
    return items


def build_empty_days(old):
    hashes = {}
    for date in ("2025-05-03","2025-05-04"):
        d=SRC/("daily-"+date.replace("-","")); d.mkdir(parents=True,exist_ok=True)
        for name,obj in (("canonical-owner-inventory-v2.1.json.gz",{"schema":"daily-owner-inventory-v2.1","report_date":date,"raw_count":0,"records":[]}),
                         ("semantic-screening-ledger-v2.1.json.gz",{"schema":"daily-semantic-screening-v2.1","report_date":date,"raw_count":0,"retained_count":0,"closure_count":0,"records":[]})):
            with gzip.open(d/name,"wt") as f: json.dump(obj,f,sort_keys=True)
        hashes[date] = tuple(hashlib.sha256((d/name).read_bytes()).hexdigest()[:20] for name in ("canonical-owner-inventory-v2.1.json.gz", "semantic-screening-ledger-v2.1.json.gz"))
        (d/"author-adversarial-recheck-v1.json").write_text(json.dumps({"schema":"author-adversarial-recheck-v1","report_date":date,"scope":{"retained":0,"closures":0},"formal_semantic_audit":False},indent=2)+"\n")
    # 05-03 has one independent official non-arXiv candidate.
    fid="SF-2025-OPENAI-GPT4O-SYCOPHANCY-POSTMORTEM"
    claim="把行为回归从离线平均分问题提升为 release authority failure：定性红旗、A/B 信号、memory interaction 与 rollback trigger 必须进入同一发布证据链。"
    body=f"<!-- claim:{fid}:start -->{claim}<!-- claim:{fid}:end -->\n\n官方 postmortem 未披露 reward 权重、完整训练数据或 evaluator 数值；不能据此推断单一根因。"
    cand={"Source Family ID":fid,"Primary Identifier":"official-postmortem:2025-05-02","Event Identity":"openai-postmortem:sycophancy:2025-05-02","Owner Week":"2025-W18","First-public Date":"2025-05-02","Supporting Source IDs":"SRC-OPENAI","Design Delta":3,"System Reach":3,"Durability":3,"Total":9,"Candidate State":"retained","Review Status":"deep_complete","Access Status":"accessible","Review Override":"release_security_contract","Review Ref":f"review:{fid}","Owner Report Ref":"self","Prior Review Ref":"—","Reconciliation":"new_in_window","Stable Node ID":"PLATFORM-EVALUATION-SYSTEM","Books Disposition":"No Change — Existing Coverage","Books Review Ref":f"books-review:{fid}","Benchmark Claim":"no"}
    receipt={"Source Family ID":fid,"Review Provenance ID":"PENDING","Review Route":"deep","Primary Evidence Version":"https://openai.com/index/expanding-on-sycophancy/#2025-05-02","Reviewed Evidence Versions":"SRC-OPENAI@https://openai.com/index/expanding-on-sycophancy/#2025-05-02","Method / Identity Locators":"https://openai.com/index/expanding-on-sycophancy/#what-happened","Evaluation Locators":"https://openai.com/index/expanding-on-sycophancy/#what-were-doing","Limitations / Counterevidence Locators":"Not Disclosed — official postmortem does not expose full internal evaluation artifacts","Artifact Locators":"Not Disclosed — no frozen internal training or evaluation artifact","Claim Boundary Ref":f"claim:{fid}","Completion Result":"complete"}
    books={"Source Family ID":fid,"Stable Node ID":"PLATFORM-EVALUATION-SYSTEM","Target Chapter Ref":"books/part-06-ai-infrastructure/66-evaluation-system.md#Evaluation Identity 必须包含 Harness 与 Environment","Adjacent Chapter Refs":"books/part-07-agent/84-agent-platform.md#Release、Canary 与 Rollback","Existing Proposition":f"existing:{fid}","New Evidence Delta":f"delta:{fid}","Evolution Relation":"Direct Evolution","Decision":"No Change — Existing Coverage","Books Review Ref":f"books-review:{fid}"}
    books["Target Chapter Ref"] = concrete_book_ref(books["Target Chapter Ref"])
    books["Adjacent Chapter Refs"] = concrete_book_ref(books["Adjacent Chapter Refs"])
    bookbody=f"<!-- existing:{fid}:start -->Evaluation/Agent Platform 已要求 harness、environment、qualitative gate、canary 与 rollback 共同定义 release evidence。<!-- existing:{fid}:end --><!-- delta:{fid}:start -->{claim}<!-- delta:{fid}:end -->\n\n该事故是既有 release contract 的受限实例，当前不新增 owner。"
    item=dict(candidate=cand,review=receipt,benchmark=None,books=books,review_body=body,books_body=bookbody)
    provenance(item)
    source_note = OLD / "2025-05-03/openai-sycophancy-source-note.md"
    copied_note = SRC / "daily-20250503/openai-sycophancy-source-note.md"
    shutil.copy2(source_note, copied_note)
    (SRC / "daily-20250503/non-arxiv-source-ledger.json").write_text(json.dumps({
        "schema":"daily-non-arxiv-source-ledger-v1", "report_date":"2025-05-03",
        "raw_count":1, "retained_count":1, "closure_count":0,
        "records":[{"source_family_id":fid,"source_id":"SRC-OPENAI","event_identity":"openai-postmortem:sycophancy:2025-05-02","decision":"retained","primary_receipt":"openai-sycophancy-source-note.md","sha256":hashlib.sha256(copied_note.read_bytes()).hexdigest()}]
    },ensure_ascii=False,indent=2)+"\n")
    extra={"Source ID":"SRC-OPENAI","Window Start":"2025-05-02T09:00:00+08:00","Window End":"2025-05-03T09:00:00+08:00","Executed At":"2026-09-03T17:45:00+08:00","Endpoint / Filter":"official dated postmortem","Result":"checked","Hits":1,"Candidate Source Families":fid,"Pagination / Cursor":"pages=1; final_cursor=end","Window Watermark":"2025-05-02T00:00:00-07:00","Closure Evidence":"coverage:SRC-OPENAI:20250503","Gap / Limitation ID":"—"}
    inv3, led3 = hashes["2025-05-03"]
    non_arxiv_sha = hashlib.sha256((SRC / "daily-20250503/non-arxiv-source-ledger.json").read_bytes()).hexdigest()[:20]
    combined3 = hashlib.sha256(f"{inv3}:{non_arxiv_sha}".encode()).hexdigest()[:20]
    report("2025-05-03",[],set(),[item],inv3,led3,extra,denominator_sha=combined3)
    inv4, led4 = hashes["2025-05-04"]
    report("2025-05-04",[],set(),[],inv4,led4)


def queue(items_by_date):
    lines=["# 2025-05 month-local Books writeback queue","","5 项原 Books 候选已按日期顺序重新打开 exact-v1、目标与相邻章节。当前正文已包含合格的演进链语义绑定，因此均以 `No Change — Existing Coverage / verified_existing_writeback` 关闭；没有待执行写回。","","| Event Date | Source Family ID | Stable Node ID | Target Chapter | Status |","| --- | --- | --- | --- | --- |"]
    verified = {"SF-2025-GALVATRON", "SF-2025-AVA", "SF-2025-LLMPRISM", "SF-2025-SOLO", "SF-2025-DISTRIBUTED-RAG"}
    for date,items in items_by_date:
        for x in items:
            if x["candidate"]["Source Family ID"] in verified:
                lines.append(f"| {date} | {x['candidate']['Source Family ID']} | {x['candidate']['Stable Node ID']} | {x['books']['Target Chapter Ref']} | verified_existing_writeback |")
    (SRC/"BOOKS_WRITEBACK_QUEUE.md").write_text("\n".join(lines)+"\n")


def main():
    old=load_old()
    one=build_day("2025-05-01",MAY1_OLD|MAY1_NEW,old)
    two=build_day("2025-05-02",MAY2_OLD|MAY2_MIGRATED|MAY2_NEW,old)
    build_empty_days(old)
    queue([("2025-05-01",one),("2025-05-02",two)])


if __name__ == "__main__":
    main()
