# 02/20 Books 首批 PRE：16052 与 16603

作者 feb20_v3；尚未修改共享 Books，申请两个真实文件窄段 ownership。已实际读 AGENTS Books规定、ROADMAP、PROJECT_CONTEXT、LEARNING_PHILOSOPHY、WRITING_GUIDE、最新相关checkpoint；读以下具体owner主线/前后衔接及Ch47末段/49开篇、Ch55末段/57开篇。原始证据见[V3_EVIDENCE_FIRST](V3_EVIDENCE_FIRST.md)，精确v1当地HTML已保留。

## 16052（2+2+2=6；exactness反侧深入）

Owner INFER-SPECULATIVE-DECODING；books/part-05-inference-system/48-speculative-decoding.md。
实际覆盖：§Lossless Verification给acceptance rule变化会改law；§MoE verification target-expert expansion讲proposal-only驻留替代、full target验证；§MoE Verifier的Expert Budget应对齐真实提交概率（当前933起）讲commitmentweighted selector/effectiverank/保root自然top-k，已有一般成本与完整路由fallback。
差额不是再写“expert union昂贵”：tree-wide fixedB直接改target routing的truncation/substitution两个分支及它们与lossless的区别尚未承载；其uniformrouter-mass也正好是后文加commitmentweight的基线，不能让读者默认那个机制从一开始就有位置权重。

拟在现有933标题后、现有commitment-weighted论证前融入两段（非章末）：
1. 树验证的expert union会使更长draft树触及HBM；完整路由/减树在exact要求下合理。允许质量近似时，可以各层sum router mass/topB；漏名单expert截断到零或名单内替换topk。改变verifier不是draft裁剪，classicacceptance只对应修改后的target，不承诺原targetlaw；qualitytol不是exact。
2. 此选择付出2–3%作者selection开销、部署budget校准及长尾质量；Oracle要跑全专家不可当真实加速，smalltree/highbatch专家共用可能抵消收益。作者single-request FP16 A100/3MoE/5task/80sample、T1five-seed及matchedbatchedbaseline只能支持局部取舍；T1EAGLEq=1原实现偏差不以同偏差证明无损，要求exact回全路由/适应proposal。接下段commitmentweight，但保位置加权仍可能rerouting。

末注只追加证据精确版本、所读§3–4/§6/A–C必要片段及反侧，不宣称复现。

## 16603（2+2+2=6；既有机制实际覆盖＋遗漏安全条件深入）

Owner INFER-SCHEDULING；books/part-05-inference-system/56-inference-scheduling.md。
实际覆盖352–382：原iteration调度→fixedchunk效率矛盾→operatorcompletion保存状态→event-driven与SLOslack→executor恢复/反侧→streamingcontext，两粒度原则已承载。本日不新增一个FlowPrefill小节或搬宣传数字。
细小但真正安全差额：TP各rank若暂停于不同communication点会deadlock；operator本身仍不可中止，超长operator必须与chunk并用。已有“恢复状态可证实”过于泛称，尚无该具体条件。

拟在现有“scheduler只拥有...”段前半融入两句：抢占检查由每operator轻信号承担，完整排序/选batch仅由arrival/completion事件触发；TP必须在同步iterationcounter到同一边界才共同暂停，不能独立暂停rank。末尾补单operatorruntime下界和极长prompt结合chunk，原回退同质/弱HoL/event高成本论证保留。不会写作者4.5ms为hardbound，不复制5.6x宣传。原FlowPrefill末注（1576）窄同步上述具体证据及随机token/不同SLO的有限条件。

请root独立核必要源与owner差额及拟文，认可后授窄锁再实际写；POST实际正文/前后/末注另验。
