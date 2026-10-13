# 13173 Semantic Invariance 必要原证与中心测量隔离

resume_mar17，仅本17补03/16自然日。完整v1题摘与原匹配DOI日级夹证复用SUP_AB_THIRD第5行/独核；不是用科学问题的领域指标重新引入AI for Science。准入实际针对等义变换/推理评价有效性，2+1+2=5，中心测量桥深入。当前abs v2为venue accepted Comments，未给撤回/勘误；只对具体中心桥读取v2受影响§3，不全稿diff。

## 必要 Source

[exact-v1](https://arxiv.org/html/2603.13173v1)实际§3定义/七类与identity/Eqs1–6、§4/§4.1、§5/Tables2–4、§6直接限制；v2仅§3中contrastive负控制与MAD同一口径。未核全部图像像素、所有作者问题、代码或复现。19问题/8域、5易10中4难；Nebius单次decode/每问题变换、T.7/topP.95/max1024，MiniLM句向量测与参考解的cosine差。LLM/rule生成并有manual-validation声明，但没有本轮独立变换保真、标注人数/协议或完整样本记录。单次identity与单次变体不能识别抽样随机性和变换效果，作者§6自己承认single-inference不捕获分布。

关键中心边界一：§3.0.3前段/摘要将八种统称semantic-preserving，后段140–142明确contrastive是semantic-altering负控制；Eq6集合只排identity，未明示排contrastive，而结果最强退化在contrastive。这不是“未发现控制”，而是原文已承认负控制、其汇总分母/有效MR映射仍不闭合。v2受影响段保留同口径，venue Comments不认证修复。不能把改题意的响应差授等义推理不稳定。

关键中心边界二：与同一参考的cosine差近0不推出两解语义等价。条件向量例参考e=(1,0)，两个单位回答向量(.6,.8)/(.6,-.8)均score .6但相互cosine=-.28；这是本轮测量分析，不说真实模型必产生这两向量。StepScore每候选step独立max参照允许重复匹配，完整trace cosine不证明逻辑正确/内部faithful，错误不变也可高stability。

关键中心边界三：Table3“scale inversion”不能推广成各家族所有指标。GPT120b MAD .143低20b .211、stability64.5%高27.0%、similarity.772高.527；Hermes大模型stability67.1%高小50.7%，与相关文字相反或指标混合。本轮必要独算：若表百分比是19×7非identity的等权实例比例133，则79.6/67.1/69.7/27.0/64.5五值均没有任何整数计数四舍五入匹配；19×8=152却分别对应121/102/106/41/98。只提示需要分母解释，不反推实际必含identity或所有数据错误。各变体共用问题和baseline，U/KW未说明cluster/paired控制；19问题、模型/服务端配置和不同架构/训练混杂不能推出参数规模因果。

作者有限条目/稳定性线索保留，不签普遍model-family选择/安全agent/ensemble收益或全费用。HW/precision/batch/concurrency/SLO及实际输出长度、参考/变换/encoder制备与重复成本未齐。到此必要支持与中心反侧足够，不展开全部题集/附录。

## 实际 owner / 安全处置提案

实际Ch66 315–343规则/alias与配对subject、1060–1078 oracle、1085–1125 trace与SAGE variant/verifier及Context支持域完整局部已读。solePLATFORM-EVALUATION-SYSTEM；已有SAGE生成/保真verifier、oracle和trace资格不等本19问题/negative-control/聚合桥已闭合，不能用一般已有覆盖假NC。题意/分母及排名争议决定中心反证是否成立，不绕它写通用metamorphic常识。

建议保持5分中心争议终态隔离，Books暂缓/不写；不作正面Evidence/Coverage、语义不变性/性能/安全保证，不降分EX。等待非准备者必要Source与隔离独核，未正式通过前不计safe。只请求一次：有效等义变体与contrastive/identity分账、Table3逐项分母与原配对结果、独立答案/保真核及重复decode基线；接受精确更正、带配置原表或最小trace，只定点重开本family，不求整repo或全部领域评价。
