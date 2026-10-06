# 02/13 安全必要证据：10148 / 10481 / 10498

以下均exact-v1、既已准入受影响深入；date batch仍待核。Source/Books尚待非作者，不授全日完成、实现核验或复现。

## [10148 COMET](https://arxiv.org/html/2602.10148v1)

5D。原准入core将实体语义迁移入视觉anchor，再用spatial pointer要求跨通道重构，而不是仅typographic text和成熟roleplay。§4九VLM，SafeBench七harmful categories及SafeBench-tiny，StrongReject/GPT4.1mini judge，5attempts；HS只对attack-success样本平均，不能与固定全样本harmfulness等同。辅助DeepSeekV3.1Terminus/Qwen3VL235BThinking/Gemini2.5FlashImage，嵌入Qwen3VL30BA3B，generationT.1；baseline推荐参数不保证等总生成/搜索compute，API revision/硬件/precision/batch/token lengths/uncertainty Not Disclosed。AdaShield-Static prepended defense与未防御两协议分开，不授所有安全系统失效。

Table4只full0.96/0.91与三个single components .66/.67、.42/.52、.24/.86，不是全部paired2×2factorial干预，attention/embedding相似度也不证明各组件因果路径。§4.4增加hop ASR升、HS降，4–6最优tradeoff不是普遍认知定律；Table5 DallE3实际generation-success与GPT4.1unsafe completion是不同分母/actor。已有Ch72 L1210–1218规范化OCR/rendered/layout+外层provenance并做跨通道组合检查，但没有spatial pointer恢复跨模态实体语义的必要检查。拟窄补来源与重构后semantic object分责、不把单通道无显式危险当最终allow；这是系统推断，不声称paper验证此defense。root可按具体owner决定是否仅报告，不以高ASR自动写书。

源：V3_QUERY_10210_10148.txt内10148 L100–145（已实际准入core），V3_EVIDENCE_10148_INITIAL.txt L149–209，V3_EVIDENCE_AFINAL_METHOD_1.txt L200–226，V3_EVIDENCE_AFINAL_CLOSE_2.txt L240–254。

## [10481 Authenticated Prompts/Context](https://arxiv.org/html/2602.10481v1)

6D。§3签名text/id/parent/policy与roottext，§4principal/seq/hashchain授权transition+workflowattestation；§5 Theorem1–4是按构造allow交/deny并/mostrestrictive的permission subset、denial继承、depth界，不是语义意图正确性或crypto confidentiality。Hashchain只能给特定可信checkpoint完整性，签名的恶意合法内容仍可污染；seq equality须不可绕过的state/current检查，不自动证明并发原子freshness。Alg1由runtime构造parent受限policy，Alg2显示inv签名+intent/tool/org intersect再检查resourceallow/deny，未直接显示逐祖先、root限制、seq/hashchain/C constraints验证；因此strongByzantine theorem需要可信构造/非绕过PEP，不把pseudo-code当任意持key恶意agent安全证明。

§7明确cannot compromise registry/crypto/provider，semanticintentvalidator只是advisory且合法权限误用不保障；6categoriesTable2没有samplecount、repetitions、benignset、FP分母、workflowcost/model/hardware/precision/batch/length。100%detection/zeroFP/1.8%overhead全文注说接受后补appendix，不能正面性能、安全或production采用。‘*credential*’匹配‘cred.txt’例还依赖未完整披露的matcher，不照录为自明定理。Root可以只采用明确定义的policy monotonicity/签名证明权限分工而非表中的semanticdrift Crypto标签。

拟具体已有覆盖：PLATFORM-SECURITY Ch72 L1617–1644实际proof artifact graph、policyfacts/attestation+actiondigest能力只认证已编码规则/现实后果非保证、key/revocation/controlplane可用性+deterministicauthorizer/failclosed、cache shape不得代替当前参数来源，足够承载本篇有限权限/证据分责；强未证保证和漏pseudo-code不进入Books。原源V3_EVIDENCE_10481_INITIAL.txt L129–178，AFINAL_METHOD_0 L140–181，AFINAL_CLOSE_0 L240–319、AFINAL_CLOSE_1 L358–419；§7 L450–455当前官方HTML限制实读，不以full评测未公开无限追附件。

## [10498 When Skills Lie](https://arxiv.org/html/2602.10498v1)

6D。威胁：attacker只appendHTMLcomment、不改visiblecleanSkill或backend；rawskill被放context而human rendered审阅隐藏comment。DeepSeekV3.2/GLM4.5Air各clean/attack/defended三个案例、benign codeformatrequest。§4 L74、Table1explicit success仅output中包含三敏感tool-name之一，没有实际读取secret或HTTPexfil；§5 L90–102 defense叙述含prompt与executor两层但结果只无proposedtools，因此不能说真实executor被测/阻断，也不能归因哪层。samples/repeats/statistics/APIrevision/hw/precision/length/batch/temperature/latency Not Disclosed；不称可靠概率或无utility损伤。

拟PLATFORM-SECURITY Ch72 L620–636已有外部logs包装→proposal/effect分责、少量手工与未真正执行，不替actualauthority。新增差额只有human-rendered审阅与model-facing raw版本是否同一artifact；需在ingestion前提供model-facingreview或版本化striphidden policy，经过strip也不授权限。这样保留原只读低风险prompt快路，但外部Skill的reviewreceipt必须绑定实际model输入。若root认为当前source不足以书稿新增，则OnlyReport保该局部visibilityfailure，不用主题同义强写。

源V3_EVIDENCE_10498_INITIAL.txt L61–125完整必要威胁、evaluation与限制。无安全代码运行、无危险工具执行。

## 10498 当前正文比较收束（作者）

实际Ch72 L620–636 logs包装与proposal/effect分开，L1210等render规范化是model语义检查，不承载human rendered review receipt与model raw artifact身份不一致。仅剩实际两surface同一version审核的差额，拟紧接输入包装段融1–2短段：审核模型真正接收的bytes/规范化版本；strip hidden改变artifact须再审核，不签allow；原样例只tool-name intention，不能称真实exfil执行或已验证executor阻断。待Ch72窄锁，范围不含10148 datehold。

最终状态同步（2026-10-04）：当窗10481具体已有覆盖已独立核；10498 Ch72实际两段/完整邻接/末注root非作者POST通过，锁释放。10148仍early-date终态保留，不计当窗候选/Books，不以已读安全附件升级日期。日级另验。
