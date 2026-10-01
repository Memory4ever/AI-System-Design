# Apr20 五项有限非作者处置复核

复核者：apr02（未写本日报告或对应 Books）。检查时间：2026-09-27T21:25:43+08:00。

实际重读当前 AGENTS、研究/Report 合同与统一入口，复用未变化的 ROADMAP 路径。范围仅为 15579/15583/15609/15618/15622 的必要官方 v1 方法、关键评价和处置；未复现实验、未核全日日期/来源、未遍历附录或版本史，不构成日 Gate。Books 没有修改。

## 15579：6 分保护深入，窄已有覆盖通过

[官方 v1](https://arxiv.org/html/2604.15579v1)，实际 §4.3、§5.1.2–5.1.4、§5.2/Tables4–7。确定性工具检查和模型判断的权限不同，原政策加强/弱化也不等于原义自动保留。MedAgentBench 34 可实现要求只新增 23；签名增参后的 baseline replay 不是完全 matched schema。零违反仅由同一套已实现 predicate 的阻断及测量支持，未覆盖未知政策。Utility 的非显著变化不证明等价或无损，原始模型/任务范围需保留；未披露延迟/precision/SLO 不补造。

实际对读 Ch72 `Policy-as-Data` 的 model sensor→deterministic executor、owner/version/fallback，以及 `Containment 不能只看最终是否发生攻击` 的 effect/utility/efficiency 联合验收。它们完整承载拟采用的责任边界；不声称全部六类检查或作者 benchmark 已被 Books 承载。2+2+2=6、定点保护深入、已有覆盖这一窄决定 PASS。

## 15583：5 分标准仅报告通过

[官方 v1](https://arxiv.org/html/2604.15583v1)，实际 §3.1.4、§3.2–3.3、§4.4–4.6。Prefix KV 复用限固定 chunk/template/model 的 query suffix，不能仅哈希 token 就推跨环境 exact。按 query 长度归一的 contrast attention、窗口平滑/合并是可操作的局部选择方案，attention 差值不是语义真值。QuALITY 的实际 token 预算不完全 matched；缓存命中后 query 时间与 RAG embedding 时间不是同一端到端分母。未提供硬件/precision/SLO 不编造。

实际 Ch75 压缩保真与 break-even 主线要求 query-specific 信息、总成本及错误边界；本稿给出受限实现与验证，不改变上述长期责任，亦不把算法整体说成已有覆盖。2+1+2=5、标准完成/仅报告 PASS。

## 15609：5 分标准仅报告通过，公式边界保留

[官方 v1](https://arxiv.org/html/2604.15609v1)，实际 §3.2–3.3/Eq1–3、§4.1–4.2/Table8、AppendixE。Remote full-probability 接口不等 label-only；仅通过 local branch 回传的是 tractable proxy，不是远端输入导数在数学上为零。Table8 的无稳定化退步与局部 KL/filter 改善支持有限配方，不证明每个组件普遍必要。RTX3090 与 API 延迟假设下的摊销不能推出尾延迟 SLO。

AppendixE 中 uniform local distribution 不会对任意 remote distribution 令 JS 为零（JS 为零须两分布相同），这一解释不能采用，但不否定局部实测。实际 Ch29 临时适配/受控更新责任没有被该视觉输入配方替代；不将医学样例恢复为领域任务。2+1+2=5、标准仅报告 PASS。

## 15618：5 分标准仅报告通过

[官方 v1](https://arxiv.org/html/2604.15618v1)，实际 §3/Eq1、§4/Table1–2。Medoid 选择真实程序，而逐 test-input 的 mode 可能并无单个程序实现；功能共识不是 correctness oracle。实验用了 benchmark 提供的真实 test inputs，不能改称已证明自造测试同样可靠。Mean@64 的改善与 best@64/再次 FMV 的下降并存，不能写成无条件递归自改进。Bootstrapped SE 非多 seed 等价检验；执行 N×K 和生成预算不能消失。

这是受限 selector/TTRL 结果，保留机制及反证即可，不需为仅报告另造 Books 原理。2+1+2=5、标准仅报告 PASS。

## 15622：6 分标准仅报告通过，精确 v1 合同不被后稿覆盖

[官方 v1](https://arxiv.org/html/2604.15622v1)，实际 §3.2–3.3/Algorithm1、§4、§6.2–6.4、必要 AppendixA/D.3。该版是 scene 近邻与已有 scene accuracy lookup 的 subnet 选择，不是后续 learned selector；高频 edge/低频 cloud 与 semantic filtering 分工成立，但 accuracy fraction 不构成未见场景的在线保证。Class filtering 可漏真类；粗类任务与细类指标不可合并。Ethos-U55 7nm/560MHz 测量包含 wrapper/subnet switching 的平均开销，不包含完整端云网络及 LLM 能耗，不能推整机电池或实时控制保证。

保留这条受限调度/语义支持分支，当前证据不足以支持稳定动态保护合同，且不声称所有实施细节已在 Books。2+2+2=6、标准仅报告 PASS。未作后续版本全文比较。

## 交付范围

五项必要证据与现有处置一致：1 窄已有覆盖、4 仅报告。没有新增 Books 提案、实际写入或日级 Gate；作者可同步单篇独立结果，仍须继续普通待办与本日终核。
