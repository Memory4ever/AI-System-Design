# Apr22 首四项：有限非作者必要源→实际 owner 审阅

复核者：apr20_resume；非本日报作者 apr02。实际重读当前 AGENTS、V3 Research/Report/来源/Prompt 与 ROADMAP，再读作者必要证据提案及以下精确 v1 必要原文。仅 source→owner / 窄终态审核，不验证本日 first-public 边界、全部来源/分母、真实写后或日级 Gate；未复现实验、未写共享 Books。当前 Books 相邻命题已实际读取，不以标题映射代替差异。

## 2604.18616v1 — ARGUS: Agentic GPU Optimization Guided by Data-Flow Invariants

[官方 PDF v1](https://arxiv.org/pdf/2604.18616v1)，实际复用 daily-20260417/exact-v1-bodies 的同 ID PDF；p1 核题名，p5–8 §4–8 与 p11–12 §9.3–9.4/Table3 必要内容，p8 的 evaluation 配置。HTML404不构成全文受阻。作者旧“Semantic Debugging…”只可作解释，不用作正式原题。

**6 分、实际缺口深入的窄采用通过。** layout algebra 后逐元素 symbolic tags 检查 Q/K、P/V 角色配对，SMT 约束失败回具体反例；flow-sensitive / path-insensitive merge top、共享状态 reset、静态 block size / unrolled loops、未追踪完整 heap / global writes 都是保证范围。§8 明确 data-flow invariant 不拥有 online-softmax 等算法替换的数学正确性；编译检查、unit tests 和 profiling 必须继续分责。不能把 tag passing、memory-safe DSL 或编译成功外推任意 kernel / 数值等价 / 无 race。

200 KernelBench L1/L2 geomean .74/.88 反向、L2四个 PyTorch fallback 计失败；60非平凡问题的 ablation **同时**取消 invariants 与 compiler feedback，不独立归因全部收益给 SMT。8×MI300X192GB、ROCm7.1.1/LLVM20，至少1s warmup 后 max(100runs,5s)平均及 CUDA graphs、socket pinning；bf16 GQA 形状映射 Llama70B TP8不是真实服务验证，FP8 MoE不同配置，未披露生产并发/tail SLO。

实际 Ch49 `Kernel Verification…Model–Kernel Interface` 的 host联合约束与 symbolic thread/memory checks（1159–1178附近）、`Generated Kernel…Typed Schedule IR`（1822附近）没有承载跨 swizzle/staging 的**元素语义角色配对标签**。拟将其嵌入该 verification / typed-IR 主线最窄两段，编译期关系反馈不替数值/运行验收；维护专家优化库、top损失精度、unsupported memory 和 fallback成本须就近。owner `INFER-TENSORRT-LLM` 合理，非 Ch78 新 effect gate。通过不等实际整合。

## 2604.18791v1 — HELM: Harness-Enhanced Long-horizon Memory for Vision-Language-Action Manipulation

[官方 HTML v1](https://arxiv.org/html/2604.18791v1)，同 ID 已缓存于 daily-20260421；实际读 §3、§4.1–4.4/Eq1–2/Alg1、§5.1–5.4 Tables1–4、§6。旧库存“Why VLA Policies Fail…”不可替正式原题。

**6 分、实际输入/监督接口缺口的窄采用通过，采用前定点纠正消融文字。** episodic keyframes 被检索为 VLA prompt 条件及 SV 的 memory-conditioned input；SV y=1 表示未来5步内失败，不是当前物理 unsafe truth。CLIP support、50K rollout、labels / retrieval成本及输入concat维度文字不清保留，不采用精确实现维度。最多三次恢复只是返回记忆 checkpoint 的 goal-conditioned action proposal，不保证物理逆转；forward recovery仅模拟验证。

重要更正：Table3 full81.5、w/oSV73.1、SV w/o memory79.2。**2.3pp是 full−without-memory 的条件差，不是无memory时SV相对无SV的增量；后者按表为6.1pp。** SV完整增量8.4pp也不能与不同配置ensemble9.5pp推出更准。只支持该输入条件在受测配置增量、不能声称无memory SV几乎无效或全history无用。Table1 oracle H67.3仍优于普通H64的65.1；不从32/64上下文未达到完整HELM推更长history永远无益。

LIBERO-LONG10任务500episodes、CALVIN ABC→D、3seeds、边界±5cm/gripper flip；50K rollout匹配不等总训练compute。A100约2h/12ms-step、15%是作者条件，精度与控制实时SLO未披露，real robot属future work。现有 Ch26 `Skill Postcondition→Next-skill Readiness`（695–718附近）已区分predicate/环境truth与future-policy labels，但没有明确**过去执行记忆输入risk predictor、监督有限未来horizon**接口。最窄两段可嵌该长程/局部纠错论证；不得让learned SV替controller safety或授予物理rollback，保forward correction/safe stop及历史误检成本。owner `MULTIMODAL-EMBODIED-VLA`合理，纠正上述2.3pp表述后可写，不需重开其他有效证据。

## 2604.18860v1 — Temporal UI State Inconsistency in Desktop GUI Agents: Formalizing and Defending Against TOCTOU Attacks on Computer-Use Agents

[官方 HTML v1](https://arxiv.org/html/2604.18860v1)，同 ID 缓存于 daily-20260421；实际 §3–4 必要 threat/model/observation-action gap、§5.1–5.8/Table7–10。旧“The Gap Between Knowing and Doing…”不作正式题。

**6 分、具体保护边界深入窄采用通过。** 攻击者可在同 desktop session 执行 user-level code，非任意远程攻击权限。pre-dispatch patch SSIM / global diff / window IDs+title 不覆盖透明 DOM element / onclick变化；pre-registered unmapped window不在new-ID差中，pixel≠handler。§5.8 DOM fingerprint是未实测future layer，不能把30ms / 100%precision建议称部署防御。pre-click再截图仍不是可信 effect-time binding，不采“OS整体冻结外任何原子性都不可能”的普遍句。

Ubuntu22.04 ARM VM/VMware、Opus4.6十OSWorld任务的gap；A135、B45、C45不同分母，Table9 C44/45≈97.8%残余，Table10 44/45也97.8非99.3%。30 benign零abort是有限FPR样本，window timer的文本不一致及API模型/1920×1080/M4 host测量保留，不从平均gap或作者self-test得所有GUI防御/生产保证。三模型B success含coordinate calibration差异，并非普遍100%。

实际 Ch72 GUI grounding（966–968附近）有可信UI identity / permission但没有**像素、window registry、DOM实际接收handler三个观察面**差异；其安全控制主线允许两段窄补effect-time身份/新鲜性、sensor coverage / race / animations误报及可信DOM/OS绑定或人工fail-closed，不重复Ch78执行接口，不把未实现DOM推荐当保证。owner `PLATFORM-SECURITY`合理，通过未等真实写后。

## 2604.18995v1 — R²-dLLM: Accelerating Diffusion Large Language Models via Spatio-Temporal Redundancy Reduction

[官方 HTML v1](https://arxiv.org/html/2604.18995v1)，实际读 §4.1–4.2/Eq2–4、§5.1–5.2/Eq5/Figure5、§6.1–6.7/Table1–6。**6 分、提前finalize与筛选保证必要深入后仅报告通过。** local average confidence jointcommit、重复token取最高confidence位置、连续top1稳定且lastconfidence过阈值是三个明确heuristics，不是truth certificate；SFT block32 / complementary masks有额外self-generation / training cost。

Figure5和§6.7都写选correct responses，§6.1却称no ground truth answers，§5.1仅低冗余排序没有correct filter来源。仅隔离“无外部判断且可靠正确筛选”的保证，保留算法、训练和作者表，不能补造oracle如何实现或删除全部证据。Table1 LLaDA HumanEval40.24→36.59、Dream MATH38.08→36.88、HumanEval57.93→54.27的训练后退步原样保留；Table6正文58.6/80.0与表59.9/82.4不一致，不采用精确差额。

generation256/block32，单H200141GB平均latency与四H200其他工作分开；非vanilla全部dual-KV，使相对vanilla收益不独立归因新组件，NFE非端到端等价成本；precision/并发/tailSLO未披露。Ch24 mutable condition副本/外部commit（374附近）与 `Early convergence与highconfidence…Commit`（1130–1138附近）具体已承载跨步稳定≠jointtruth和额外状态/误提交代价。不能把本文window算法说成完整Existing；窄局部选择及受限联合训练未改变该长期责任，Only合理，不因拟Only减少必要审阅。无必要Books新增。

## 范围与结果

18616 / 18791 / 18860三项窄source→actualowner采用通过；18791正式采用/报告前纠正2.3pp消融含义，三项原题同步身份，不推倒其他有效证据。18995必要深入后Only通过。未审无关附件，未验证新实现、实际Books或本日日期/完整Gate；其余ordinary由作者继续。
