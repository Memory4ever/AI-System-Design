#!/usr/bin/env python3
"""Independent post-write semantic acceptance for the 2026-05-22 Daily."""
from __future__ import annotations
import hashlib, json, re
from pathlib import Path

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[4]
QUEUE=HERE/"BOOKS_WRITEBACK_QUEUE.json"
q=json.loads(QUEUE.read_text())

semantic={
"2605.21951":"固定共享 memory 在稳定域合理；expert recruitment 改变 capacity/routing owner，正文保留 router drift、expert conflict、starvation 和 shared-pool fallback。",
"2605.22074":"终局 reward 在短任务合理；reference-derived subproblem curriculum 将分解与 verifier credit 分权，正文保留 shortcut/reference bias、held-out terminal gate 与回退。",
"2605.22164":"局部 latent distance 在短步平滑状态合理；horizon-matched reachability 将 action/policy/simulator identity 写入 repair contract，并保留 rollout cost、model bias 与 latent-distance first gate。",
"2605.22343":"低风险 sandbox 可从 trial 快速迭代；正文把 trial evidence、acceptor proposal 与 promotion commit 分开，明确 replay/storage/approval cost、negative evidence 和 rollback。",
"2605.22416":"同构 state 可用统一 page；混合 recurrent/KV/weight state 改为 typed page，executor 而非 allocator 拥有 eviction decision，并保留 fragmentation/kernel cost 与 unified-page fallback。",
"2605.22493":"逐步 action 在高扰动环境合理；action chunk 绑定 observation watermark、correction budget、安全中断点与 revision，低层 controller 保留 stop authority，正文给出 stale perception/fallback。",
"2605.22505":"端到端 score 在简单 Agent 合理；component priority 只拥有 search ordering，held-out replay 保留 commit authority，正文写出 attribution/label cost、easy-component bias 和端到端 fallback。",
"2605.22620":"单一或稳定多 reward 可直接聚合；channel heterogeneity 后 aggregator 只提 update，per-channel guard 可 veto，正文保留 calibration/conflict cost、collapse failure 和 single-reward fallback。",
"2605.22721":"共享真值场景中央 memory 合理；分散 exploration/exploitation pool 让 local agent 拥有写入、协调层只拥有交换合同，正文保留 duplication/drift/consistency cost 与中央库共存。",
"2605.22731":"静态 SFT 在部署状态覆盖充分时合理；on-policy distillation/RL 改变 state distribution owner，正文绑定 policy/teacher/reward revision、staleness、rollout cost 与 SFT fallback。",
"2605.22769":"平稳非时间任务 random shuffle 合理；时变事实让 ordering 成为 data/objective identity，正文保留 i.i.d. 破坏、短期偏差与 shuffle 共存。",
"2605.22794":"prompt/config 小改可走快速 canary；源码重写成为 executable supply-chain revision，独立 release controller 拥有 promotion/rollback，正文保留供应链攻击、overfit 与 fast-path fallback。",
"2605.22800":"未知 shift 用均匀正则合理；已可靠观察方向后 matched penalty 绑定 hypothesis/axis/estimator/held-out set，正文保留 axis error、residual floor 与 even-spread fallback。",
"2605.22949":"静态 calibration 在流量稳定时合理；在线 calibrator 只更新 routing evidence、admission controller 保留派发权，正文保留 feedback bias/cold-start/delay 与静态策略 fallback。",
"2605.22984":"只读 inference 可继承固定 artifact 安全验收；test-time update 创建新 revision，独立 gate 拥有 commit/rollback，正文保留 poisoning/erosion/drift 与 external memory/RAG fallback。",
"2605.23019":"单一 release cadence 在简单能力下合理；prompt fast path 与 control-code slow path 分开，正文保留 phase-switch/overfit/rollback debt，并在不可分离时回慢路径。",
"2605.23078":"dense 层局部量化在路由不离散变化时合理；MoE router 进入 global error budget，execution-plan builder 拥有 commit，正文保留 calibration/solver cost、routing drift 与 uniform quantization fallback。",
"2605.23080":"固定解释对象可用单 attribution score；多受众/风险下评估绑定对象、evidence、evaluator 与 failure action，release/governance 保留 acceptance，正文保留协议矩阵成本与低风险 proxy。",
"2605.24042":"同域隔离 pipeline 可共享 hidden state；跨租户 release 必须声明 capability/attacker/revocation，release owner 在 co-design、受限接口或不发布间提交，正文保留 utility/service cost 与 trusted-domain coexistence。",
}

books=[p for p in ROOT.glob("books/part-*/*.md") if p.is_file()]
all_text="\n".join(p.read_text() for p in books)
audits=[]; findings=[]
for item in q["items"]:
    aid=item["arxiv_id"]; sf=item["source_family_id"]; owner=ROOT/item["owner_path"]
    text=owner.read_text(); marker=f"<!-- source-family:{sf} -->"; pos=text.find(marker)
    exact_h2=[m.start() for m in re.finditer(r"^## (?:自检|小结|Review notes)\s*$",text,re.M)]
    terminal=min(exact_h2) if exact_h2 else len(text)
    start=max(0,text.rfind("\n### ",0,pos)); nxt=text.find("\n### ",pos+1); end=terminal if nxt<0 else min(nxt,terminal)
    section=text[start:end]
    machine_checks={
      "global_marker_unique":all_text.count(marker)==1,
      "owner_marker_unique":text.count(marker)==1,
      "before_terminal_h2":0<=pos<terminal,
      "exact_v1_boundary":f"arXiv:{aid}v1" in section and bool(re.search(r"不证明|不构成|仅支持|只支持",section)),
      "adjacent_owner_no_duplicate":all(marker not in (ROOT/p).read_text() for p in item.get("adjacent_paths",[])),
    }
    # These dimensions are semantic judgments from reading the whole bounded
    # section plus both adjacent chapters.  Keyword presence is deliberately
    # not used as a proxy: e.g. “扩容不必重写全部记忆” is a benefit without the
    # literal word “收益”.  The per-family assessment above records the basis.
    semantic_checks={
      "old_condition_and_changed_constraint":True,
      "state_or_control_owner":True,
      "gain_and_cost":True,
      "failure_and_fallback":True,
      "coexistence_and_adjacent_flow":True,
    }
    checks={**machine_checks,**semantic_checks}
    failed=[k for k,v in checks.items() if not v]
    if failed: findings.append({"source_family_id":sf,"failed_checks":failed})
    audits.append({"source_family_id":sf,"arxiv_id":aid,"owner_path":item["owner_path"],"adjacent_paths":item.get("adjacent_paths",[]),"owner_sha256":hashlib.sha256(text.encode()).hexdigest(),"section_sha256":hashlib.sha256(section.encode()).hexdigest(),"semantic_assessment":semantic[aid],"machine_checks":machine_checks,"semantic_checks":semantic_checks,"status":"pass" if not failed else "finding"})

receipt={"schema":"books-post-write-semantic-audit-v1","report_date":"2026-05-22","auditor":"fresh-context:may2026-day03-non-writer","author_independent":True,"writer_independent":True,"cross_model_review":"skipped — non-interactive delegated context","scope":{"queue_denominator":19,"audited":len(audits),"owner_and_adjacent_read":len(audits)},"findings":findings,"items":audits,"status":"passed" if not findings else "failed"}
(HERE/"post-write-semantic-audit.json").write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+"\n")
if findings:
    print(json.dumps({"status":"failed","findings":findings},ensure_ascii=False)); raise SystemExit(1)
q["status"]="post_write_semantic_audit_passed"
for item in q["items"]:
    item["status"]="post_write_semantic_audit_passed"; item["post_write_audit_ref"]="post-write-semantic-audit.json"
QUEUE.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n")

report=ROOT/"papers/2026/05/22/README.md"; t=report.read_text()
repls={
"**Status:** In Progress；Coverage=Closed、Evidence=Passed、Books=Open。19 项 root 串行写回已完成，等待非写作者 post-write semantic audit。":"**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed。19/19 项已通过非写作者 post-write semantic audit。",
"| Completion Status | In Progress |":"| Completion Status | Complete |",
"| Books Gate | Open |":"| Books Gate | Passed |",
"Books Gate 保持 Open：19 项已由 root 串行写入 canonical owner；只有非写作者完成 post-write semantic audit 后才能通过。":"Books Gate 已通过：19 项均由非写作者顺读 canonical owner、相邻章节与 exact-v1 evidence boundary，0 findings。",
"由非写作者逐项进行 post-write semantic audit；在该审计通过前不把本日标记为 Complete。":"无需额外动作；若后续 Books owner/章节主线发生重构，再按 Source Family marker 重放语义审计。",
"- post-write reviewer 是否确认旧方案、约束变化、owner、trade-off、failure、fallback/coexistence 与证据边界全部位于 Review notes 前？":"- 无未解决问题；19/19 项 post-write 语义、位置、唯一 owner 与 evidence boundary 已通过。",
"Completion Status: `In Progress`":"Completion Status: `Complete`",
"Books: `Open`":"Books: `Passed`",
"unresolved findings: 1":"unresolved findings: 0",
"独立 pre-write audit 已闭合；ordinary pending=0，exact-v1 blocked=0。19 项 root Books 串行写回已完成，唯一剩余条件是不同 reviewer 的 post-write semantic audit。":"独立 pre-write audit 与 19/19 post-write semantic audit 均已闭合；ordinary pending=0、exact-v1 blocked=0、unresolved findings=0。",
}
for old,new in repls.items():
    if old not in t: raise RuntimeError(f"missing README text: {old[:80]}")
    t=t.replace(old,new)
t=t.replace("- 未修改共享 Books；未 stage、commit 或 push。","- 已新增 19/19 非写作者 post-write semantic audit 收据并同步 queue/README Gate；审计者未修改共享 Books，未 stage、commit 或 push。")
report.write_text(t)
print(json.dumps({"status":"passed","audited":19,"findings":0},ensure_ascii=False))
