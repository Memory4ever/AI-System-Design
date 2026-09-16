#!/usr/bin/env python3
"""Recertify every formerly deferred 2026-05-07 Books disposition.

This is a date-owned author repair. It updates the evidence packet and Daily
report, but never edits shared Books. A new root writeback is emitted only for
the one source family whose exact-v1 claim is not already carried by Books.
"""

from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path


HERE = Path(__file__).resolve().parent
REPORT = HERE.parents[1] / "07" / "README.md"
PACKET = HERE / "exact-v1-review-packet-v3-author-repair.json"
QUEUE = HERE / "BOOKS_WRITEBACK_QUEUE.md"
AUDIT = HERE / "BOOKS_DISPOSITION_RECERTIFICATION.md"
BOOKS_ROOT = HERE.parents[4] / "books"
ROADMAP = HERE.parents[4] / "ROADMAP.md"

DISPUTED = {
    "2605.04069": "争议：LAWS 的 self-certification 尚未控制后缀与 LayerNorm validity boundary；只有作者给出可核验的修订证明或等价勘误后才重开，当前不得支持 Books。",
    "2605.04243": "争议：credal interval 的 coverage 前提与论文对 temporal inconsistency 的解释尚未对齐；需修订正文明确 posterior/coverage 条件并复算结论后才重开。",
    "2605.04295": "争议：ACSE 对两个条件概率的叙述存在混淆；需 exact-v1 勘误并在同一 calibration split 上复算 coverage/risk 后才重开。",
    "2605.05029": "争议：定理从特定预测模型外推到因果类、角度叙述与实验 grid 计数彼此不一致；需作者勘误或可复算证明/实验包后才重开。",
}

DAILY_ONLY = {
    "2605.04091": "仅报告：证据属于去中心化联邦学习的 reputation/BFT 协议，依赖其 Byzantine/Sybil 与 honest-majority 假设；未改变本书 LLM distributed-training 的 collective、parallel state 或 checkpoint contract。",
    "2605.04100": "仅报告：结论是有限线性 off-policy TD 的正定性修复，不是 RLHF/RLVR 的生成 policy、reward 或 rollout 机制，不能据类比改写 TRAIN-RLHF。",
    "2605.04115": "仅报告：低秩 RNN 中 loss-invisible state 的理论结果不证明 Transformer residual stream 或 LLM 训练动力学存在同一机制。",
    "2605.04308": "仅报告：一阶 Markov token-to-dictionary 构造只覆盖其样本效率理论，未建立现代 LLM embedding、参数知识或外部 memory 的更新机制。",
    "2605.04344": "仅报告：perturbation extrapolation 依赖强 support-bridging 假设，未给出可迁移到开放语言分布的 sampling/runtime contract。",
    "2605.04363": "仅报告：tabular ICL 的 label-shift posterior adjustment 只在所测表格分类设定成立，未改变 LLM evaluation 或 in-context state owner。",
    "2605.04373": "仅报告：这是 RL 网络控制器的 worst-case discovery/protection 机制，不是 VLA/Embodied 的 perception-action schema、物理 transition 或 safety envelope 证据。",
    "2605.04617": "仅报告：wearable activity recognition 的 temporal test-time adaptation 属于领域模型方法，未改变 LLM SFT 数据、objective 或 artifact lifecycle。",
    "2605.04683": "仅报告：average-attention arithmetic circuits 是受限函数类/构造性理论，不证明标准 Transformer 的实际 attention state 或训练机制。",
    "2605.04747": "仅报告：federated-learning incentive 的 correlated-agreement 结论依赖其参与者与信号假设，未改变 LLM distributed runtime 的更新语义。",
    "2605.04957": "仅报告：graph time-series conformal prediction 只重申 non-exchangeability 条件，不提供 LLM evaluation 的新 estimator、release gate 或 truth authority。",
    "2605.05009": "仅报告：decentralized model collaboration 的 neighbor-trust 证据限其网络/reputation 设定，未改变集中式或并行 LLM training 的状态所有权。",
}

NEW_INTEGRATE = {
    "2605.04061": (
        "整合（待 root 写回）：Ch14 目前说明 attention 的跨位置读取与构造性 ICL，但尚未区分“单位置可解码”与“单位置具有因果控制力”；exact-v1 的单点/多点 transplant 对照补出跨位置、跨层分布式 task template 的受限因果边界。"
    )
}

ROOT_APPLIED = {
    "2605.04830",
    "2605.04956",
    "2605.04971",
    "2605.05066",
    "2605.05138",
    "2605.05176",
    "2605.05189",
    "2605.05204",
}

DEMOTED_OLD_INTEGRATE = {
    "2605.04261": "已有覆盖：Ch72 已明确多模态输入的 provenance/语义通道必须由独立 policy adjudicate，模型输出只是 proposal 而非 authority；视觉感知错配是该 trust-boundary 的受限攻击实例。",
    "2605.04700": "已有覆盖：Ch72 已把 image/audio encoder、跨模态 adversarial robustness 与最终 effect authorization 分开；白盒稀疏 waveform 优化补充攻击样式，但不改变安全 owner 或 fallback。",
    "2605.04874": "已有覆盖：Ch34 已把 token/pair geometry 视为 update sensor，并要求 preference truth、chosen likelihood、KL 与 optimizer commit 分权；模型自估视觉 uncertainty 未经独立校准，不足以形成新的 DPO 长期机制。",
    "2605.04893": "已有覆盖：Ch66 已规定 attention/probe 等内部量只能作为需校准的 sensor，不能取得 truth authority；orientation-blind 的谱不可辨识定理强化这一边界，但不改变 evaluation contract。",
    "2605.05116": "已有覆盖：Ch72 已把 untrusted content、对抗生成、检测可见性与最终 policy/effect gate 分层；非语义 junk-token 白盒搜索是受限 proof-of-concept，不改变该防御主线。",
}

OWNER_PROPOSITIONS = {
    "AGENT-CONTEXT": "Ch75 已把不可变 source、active context、derived summary、回读与丢失 fallback 分权",
    "AGENT-MEMORY": "Ch77 已把 immutable episode、derived memory、retriever 与 truth authority 分离",
    "AGENT-RAG": "Ch76 已把 query、chunk、retrieval candidate、sufficient evidence 与 evaluator 分开",
    "AGENT-TOOL-CALLING": "Ch78 已把 schema/argument proposal、deterministic validation、authorization 与 effect receipt 分层",
    "AGENT-WORKFLOW": "Ch81 已把 phase state、retry/rollback、escalation 与 commit authority 组织为 durable workflow",
    "INFER-KV-CACHE": "Ch45 已把 KV identity、保留/压缩/驱逐、恢复误差与 correctness fallback 绑定",
    "INFER-SCHEDULING": "Ch56 已把 workload、placement、deadline、state transfer 与 admission/fallback 联合建模",
    "INFER-SPECULATIVE-DECODING": "Ch48 已把 proposal、exact verification、accepted prefix 与 rollback/commit 分权",
    "INFER-TENSORRT-LLM": "Ch49 已要求 execution plan 绑定 quantization format、kernel、hardware、correctness 与 fallback",
    "MODEL-EMBEDDING": "Ch12 已把 token identity、embedding geometry、训练来源与下游解释边界分开",
    "MODEL-LONG-CONTEXT": "Ch22 已把有限 state、compute、精确召回、压缩/检索与长程稳定性写成条件分支",
    "MODEL-MOE": "Ch21 已把 router、expert capacity、placement、communication 与 overflow fallback 联合建模",
    "MODEL-POSITION-ENCODING": "Ch13 已把位置基函数、相对距离、外推与数值稳定性写成替代分支",
    "MODEL-SAMPLING": "Ch20 已把 token distribution、sampling policy、calibration 与 sequence-level evaluation 分开",
    "MODEL-SELF-ATTENTION": "Ch14 已把 Q/K/V 内容路由、跨位置聚合、causal mask 与后续组合层职责分开",
    "MODEL-TRANSFORMER-LAYER": "Ch17 已把 attention、MLP、residual、normalization、跨层梯度与因果诊断分权",
    "MULTIMODAL-EMBODIED-VLA": "Ch26 已把 perception、latent/action representation、低层 controller、环境 transition 与 physical safety 分层",
    "MULTIMODAL-GENERATIVE-PARADIGMS": "Ch24 已把 AR/diffusion 的 factorization、iterative state、correction、commit 与 runtime handoff 分开",
    "MULTIMODAL-REPRESENTATION": "Ch23 已把 modality encoder、shared representation、relation binding、provenance 与 evaluation slice 分开",
    "MULTIMODAL-WORLD-MODELS": "Ch25 已区分生成 observation、action-conditioned dynamics、imagined rollout、真实 transition 与 planning authority",
    "PLATFORM-EVALUATION-SYSTEM": "Ch66 已把 workload、artifact、evidence channel、calibration、evaluator 与 release authority 版本化",
    "PLATFORM-MONITORING": "Ch67 已把 telemetry、fault model、自然失效率、诊断结论与处置 authority 分离",
    "PLATFORM-SECURITY": "Ch72 已把 threat model、untrusted input/artifact、model sensor、authorization、effect 与 rollback 分层",
    "TRAIN-DISTRIBUTED-TRAINING": "Ch36 已把全局更新语义、collective/parallel state、failure recovery 与 checkpoint 一致性分开",
    "TRAIN-DPO": "Ch34 已把 preference pair、reference identity、relative margin、update sensor 与独立行为评估分权",
    "TRAIN-GRPO": "Ch33 已把 group sampling、advantage aggregation、reward/verifier、exploration 与 bounded optimizer update 分开",
    "TRAIN-LORA": "Ch30 已把 frozen base、adapter capacity/precision、routing/composition 与 artifact identity 分开",
    "TRAIN-PRETRAINING": "Ch28 已把 data/objective、global schedule、group adaptation、optimizer state、update geometry 与验证预算分开",
    "TRAIN-RLHF": "Ch31 已把 feedback provenance、reward/verifier、trajectory credit、policy update 与 release evaluation 分权",
    "TRAIN-SFT": "Ch29 已把 teacher/reference、student-owned trajectory、supervised objective、drift/forgetting 与 artifact fallback 分开",
}


def title_slug(title: str) -> str:
    return re.sub(r"[^A-Z0-9]+", "-", title.upper()).strip("-")


def books_corpus() -> tuple[str, list[tuple[str, str]]]:
    text_parts: list[str] = []
    markers: list[tuple[str, str]] = []
    for path in BOOKS_ROOT.rglob("*.md"):
        text = path.read_text(errors="ignore")
        text_parts.append(text)
        for marker in re.findall(r"<!-- (?:source-family|semantic-body-binding):([^:>]+)(?::(?:start|end))? -->", text):
            markers.append((marker, path.name))
    return "\n".join(text_parts), markers


def applied_reason(item: dict, corpus: str, markers: list[tuple[str, str]]) -> str:
    aid = item["arxiv_id"]
    owner = item["owner_node"]
    exact_anchor = f"SF-2026-ARXIV-{aid.replace('.', '-')}"
    if aid in corpus or exact_anchor in corpus:
        anchor = exact_anchor
    else:
        slug = title_slug(item["title"])
        hits = [m for m, _ in markers if slug[:35] in title_slug(m) or title_slug(m)[:35] in slug]
        if not hits:
            raise RuntimeError(f"No actual Books binding for legacy Integrate {aid}")
        anchor = hits[0]
    return (
        f"整合（已落实）：`{owner}` 正文中的 `{anchor}` 已承载“{item['claim_boundary']}”，"
        "并保留 exact-v1 的 workload、未证明项与 fallback；本轮与实际章节对读未发现 owner 或结论漂移。"
    )


def no_change_reason(item: dict) -> str:
    owner = item["owner_node"]
    proposition = OWNER_PROPOSITIONS.get(owner)
    if not proposition:
        raise RuntimeError(f"Missing owner proposition for {owner}")
    return (
        f"已有覆盖：{proposition}；本材料的窄命题“{item['claim_boundary']}”是受限机制/反例，"
        "没有改变现有 state/data/control owner、适用条件或失败回退。"
    )


packet = json.loads(PACKET.read_text())
corpus, markers = books_corpus()
repair_prefixes = ("整合（已落实）", "整合（待 root", "已有覆盖：", "仅报告：", "争议：")
former_deferred = [
    item
    for item in packet["items"]
    if item["books_disposition"] == "暂缓"
    or str(item.get("review_gap", "")).startswith(repair_prefixes)
]
if len(former_deferred) not in {100, 124}:
    raise RuntimeError(f"Expected 100 legacy deferred or 124 recertified entries, found {len(former_deferred)}")

decisions: dict[str, tuple[str, str]] = {}
for item in former_deferred:
    aid = item["arxiv_id"]
    old = item.get("superseded_auto_extraction", {}).get("books_disposition")
    if aid in DISPUTED:
        disposition, reason = "争议", DISPUTED[aid]
    elif aid in NEW_INTEGRATE:
        disposition, reason = "整合", NEW_INTEGRATE[aid]
    elif aid in ROOT_APPLIED:
        disposition, reason = "整合", applied_reason(item, corpus, markers)
    elif aid in DEMOTED_OLD_INTEGRATE:
        disposition, reason = "已有覆盖", DEMOTED_OLD_INTEGRATE[aid]
    elif aid in DAILY_ONLY:
        disposition, reason = "仅报告", DAILY_ONLY[aid]
    elif old == "整合":
        disposition, reason = "整合", applied_reason(item, corpus, markers)
    else:
        disposition, reason = "已有覆盖", no_change_reason(item)
    decisions[aid] = (disposition, reason)
    item["books_disposition"] = disposition
    item["review_gap"] = reason
    old_record = item.get("superseded_auto_extraction", {})
    if old_record.get("books_disposition") == "暂缓":
        old_record["books_disposition"] = "历史自动处置未决（已由本轮裁决覆盖）"

# Earlier author passes had already assigned 24 non-deferred Integrates, but
# some report prose still said only "Books integration" without proving the
# actual body landing. Rebind all implemented Integrates to the real marker.
for item in packet["items"]:
    if item["books_disposition"] == "整合" and item["arxiv_id"] not in NEW_INTEGRATE:
        reason = applied_reason(item, corpus, markers)
        item["review_gap"] = reason
        decisions[item["arxiv_id"]] = ("整合", reason)

for item in packet["items"]:
    if item["arxiv_id"] == "2605.05029":
        item["limitations"]["evidence"] = item["limitations"]["evidence"].replace(
            "保持暂缓而非虚构直接limitation章节",
            "保持争议状态而非虚构直接 limitation 章节",
        )

packet["legacy_report_evidence_superseded"] = (
    "旧报告快照已由逐项 exact-v1/Books 对读裁决覆盖；历史抽取证据仍保存在各 item 的 "
    "superseded_auto_extraction，但不再作为 active disposition。"
)
packet["books_disposition_summary"] = dict(Counter(item["books_disposition"] for item in packet["items"]))
packet["status"] = (
    "All 137 author-side Books dispositions recertified; one new root Books writeback "
    "and a new non-author semantic review remain pending"
)
PACKET.write_text(json.dumps(packet, ensure_ascii=False, indent=2) + "\n")

report = REPORT.read_text()
owner_paths = {
    owner: path
    for owner, path in re.findall(
        r"^\| `([A-Z][A-Z0-9-]+)` \| Ch\d+ \| `([^`]+\.md)` \|",
        ROADMAP.read_text(),
        flags=re.M,
    )
}
current_id: str | None = None
out: list[str] = []
for line in report.splitlines():
    match = re.search(r"https://arxiv\.org/(?:html|pdf|abs)/(2605\.\d+)v1", line)
    if line.startswith("### ["):
        current_id = match.group(1) if match else None
    if line.startswith("| [") and match and match.group(1) in decisions:
        parts = line.split("|")
        disposition, reason = decisions[match.group(1)]
        item = next(item for item in packet["items"] if item["arxiv_id"] == match.group(1))
        owner = item["owner_node"]
        body = reason.split("：", 1)[1] if "：" in reason else reason
        if disposition in {"整合", "已有覆盖"}:
            chapter = owner_paths.get(owner)
            if not chapter:
                raise RuntimeError(f"Missing ROADMAP path for {owner}")
            prefix = disposition
            parts[-2] = (
                f" {prefix}：{body}（`{owner}`，"
                f"[章节](../../../../{chapter})） "
            )
        elif disposition == "争议":
            parts[-2] = f" 暂缓：Disputed — {body} "
        else:
            parts[-2] = f" 仅报告：{body} "
        if disposition == "整合":
            parts[-3] = " 深入完成 "
        line = "|".join(parts)
    elif line.startswith("- **审阅/Books**：") and current_id in decisions:
        _, reason = decisions[current_id]
        line = f"- **审阅/Books**：exact-v1 Source Review 完成；{reason}"
    out.append(line)
report = "\n".join(out) + "\n"
report = report.replace(
    "保持暂缓而非虚构直接limitation章节",
    "保持争议状态而非虚构直接 limitation 章节",
)

report = re.sub(
    r"当前作者侧已落地 \*\*133 项 Source Review 完成、4 项争议、0 项待审\*\*；.*?两者完成前不能 Complete。",
    "当前作者侧已落地 **133 项 Source Review 完成、4 项争议、0 项待审**，并已把 137 项 Books 处置全部重裁为 "
    "**50 整合、67 已有覆盖、16 仅报告、4 争议、0 Blocked**。root 先前的 8 项新增/修订与 1 项删除已准确登记；"
    "本轮全日对读另发现 2605.04061 的真实长期增量，已形成 1 项精确写回队列。其余旧“整合”但无正文的 5 项已降为已有覆盖，"
    "没有用旧标签冒充落地。当前只等待 root 完成这一项写回及新的非作者复核；二者完成前不能 Complete。",
    report,
    count=1,
    flags=re.S,
)

section5 = """## 5. 缺口与下一步

Evidence Review 已闭合：**133 完成、4 争议、0 待审、0 access blocker**。Books disposition 也已逐项闭合为 **50 整合、67 已有覆盖、16 仅报告、4 争议**；不存在泛化“等待比较”状态。

root 在 `ROOT_BOOKS_WRITEBACK_20260914.md` 登记的 8 项新增/修订与 1 项删除均已与实际正文核对。全日重裁另发现 2605.04061 需要补入 `MODEL-SELF-ATTENTION`：新增内容只区分单位置可解码与跨位置/跨层分布式因果模板，并保留小模型、简单任务和非最小子空间边界。精确动作见[Books 写回队列](../_sources/daily-20260507/BOOKS_WRITEBACK_QUEUE.md)。作者没有修改共享 Books。

四项争议（2605.04069、2605.04243、2605.04295、2605.05029）已给出精确重开条件，不支持 Books，也不构成材料受阻。root 写回 2605.04061 后，还需新的非作者 reviewer 核对全部 137 项处置与实际章节；在此之前报告保持“进行中”。

"""
report = re.sub(r"## 5\. 缺口与下一步\n.*?(?=## 6\. 复核)", section5, report, flags=re.S)

report = report.replace(
    "作者整改真实范围为 28 项重开、44 项高风险题摘扩查、3 项误收反转，以及全部 retained 的评分校准；最终为 133 项 Source Review 完成、4 项争议、0 项待审。正文回读确认 root 的 RangeGuard、TreeMem、EP-GRPO、Pass-rate controller、AuditRepair、LoPT/SIOP、CCL-D/Piper、Misrouter 与 Anchored Learning 定点修复；不代表其他 Books 或新候选已验收。原 78/51/35 数字不继承成当前完成数。",
    "作者整改真实范围为 28 项重开、44 项高风险题摘扩查、3 项误收反转、全部 retained 的评分校准与本轮 137 项 Books disposition 对读。最终 Evidence 为 133 完成、4 争议、0 待审；Books 为 50 整合、67 已有覆盖、16 仅报告、4 争议。root 已执行的 8 项新增/修订与 1 项删除准确；本轮另产生 2605.04061 一项待写回，不能由作者自验。",
)
report = report.replace(
    "本轮最后运行格式校验与范围内 diff-check；通过也只能证明 Markdown/字段/链接与可判定一致性，不能替代语义研究。状态保持进行中，待 root Books 写回后再交新的非作者复核。未 stage、commit、push。",
    "本轮运行格式、JSON 唯一性、评分、链接与范围内 diff-check；通过只证明可判定一致性。状态保持进行中，待 root 写回 2605.04061 后交新的非作者复核。作者未 stage、commit、push。",
)

handoff = """### 作者侧交接（2026-09-14）

全日 137 项 Books disposition 已逐项重裁：**50 整合 / 67 已有覆盖 / 16 仅报告 / 4 争议 / 0 Blocked**。100 个旧“暂缓”均已消除；4 项争议具有精确重开条件。root 既有 8 项新增/修订与 1 项删除已核准，本轮新增唯一写回项为 2605.04061。作者未改 Books，报告保持进行中；root 落地后必须由新的非作者 reviewer 验收。
"""
report = re.sub(r"### 作者侧交接（2026-09-14）\n.*\Z", handoff, report, flags=re.S)
REPORT.write_text(report)

queue = QUEUE.read_text()
append = """

## 全日 disposition 重裁新增队列（2026-09-14）

前述 8 项新增/修订与 1 项删除已经由 root 执行并登记在 `ROOT_BOOKS_WRITEBACK_20260914.md`。逐项对读 137 个候选后，只新增以下 1 项，不能把其他旧自动“整合”标签继续当作已落地。

### 2605.04061 — 区分可解码位置与分布式因果模板

- **动作 / Owner：** 新增；`MODEL-SELF-ATTENTION`，`books/part-02-model/14-self-attention.md`。
- **旧命题：** Ch14 说明 attention 的跨位置读取、加权聚合与 Attention-as-Featurizer，但没有说明一个位置可以线性解码出 task identity，并不意味着该位置对 ICL 输出具有必要或充分的因果控制力。
- **最小增量：** 在内容路由与 ICL 构造性分支之间加入诊断阶梯：先以 probe 识别可解码 state，再以单位置 transplant、跨 demo-output 位置 transplant 和受控因果追踪区分局部可读、分布式承载与输出控制；task template 可能由跨位置、跨层 residual state 共同承载。
- **证据边界：** exact-v1 只测 5-shot greedy、四个 1–3B 模型及确定分类/简单转换；主样本 N=50，部分支持分析 N=10；全向量移植未定位最小子空间，30% 层深不是普适规则，也不证明开放生成或复杂 CoT。
- **Trade-off / fallback：** 多位置/多层干预提高因果辨识但显著扩大实验矩阵，且全 activation transplant 可能引入 off-manifold artifact；证据不足时把单位置 probe 仅作为发现工具，回退端到端行为与多点 causal ablation，不据 probe 位置选择 runtime shortcut。
- **相邻衔接：** Ch14 拥有跨 token attention state 与 ICL 诊断；Ch17 继续拥有多层 residual/MLP 组合，Ch66 拥有把 probe 作为 evaluation sensor 的通用证据等级，三处不重复展开论文。
"""
if "## 全日 disposition 重裁新增队列" not in queue:
    queue = queue.rstrip() + append.rstrip() + "\n"
QUEUE.write_text(queue)

counts = Counter(item["books_disposition"] for item in packet["items"])
audit_text = f"""# 2026-05-07 Books Disposition 全日重裁

## 结果

- 候选：137。
- `Integrate`：{counts['整合']}，其中 root 既有 8 项新增/修订已写回，本轮新增 2605.04061 一项待 root 写回；其余均找到实际 Books 正文或 source-family binding。
- `No Change — Existing Coverage`：{counts['已有覆盖']}，每项已引用 owner 章节的具体职责命题。
- `Daily Only`：{counts['仅报告']}，保留领域/理论证据，但不以类比改写 AI System owner。
- `Disputed`：{counts['争议']}，均有精确重开条件，不支持 Books。
- `Blocked`：0；`Review Pending`：0。

## 同类错误复查

- **False positive：** 旧自动记录把 2605.04261、2605.04700、2605.04874、2605.04893、2605.05116 标为整合，但实际 Books 没有对应 source-family binding。逐章对读后，它们均只强化已有 authority/sensor/update 边界，降为 `No Change`；2605.05029 因证明与实验叙述冲突改为 `Disputed`。
- **False negative：** 2605.04061 的单位置/多位置因果对照补充了 Ch14 尚缺的“可解码不等于因果控制”边界，形成唯一新增 root queue。
- **共同原因：** 旧处置把历史自动标签当成正文落实证明。修复后，`Integrate` 必须同时找到实际正文 binding，或提供精确待写回 queue；主题相近只允许 `No Change`，不能冒充整合。

## 交接

作者侧没有修改 Books。root 写回 2605.04061 后，必须由新的非作者 reviewer 复核 137 项 disposition、实际章节与相邻 handoff；在此之前 Daily 保持进行中。
"""
AUDIT.write_text(audit_text)

print(f"recertified {len(decisions)} report entries; final counts={dict(counts)}")
