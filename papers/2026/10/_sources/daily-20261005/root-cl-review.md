# 10/05 独立证据复核：六项 CL

复核者 root；只读本日准入项 exact-v1 的必要机制、对照和反侧，非全文附件遍历。公开归属依本日官方公告与作者保存的原始字段，不以 Submitted 日期代替公开时间。

| 材料 | 已实际核查位置 | 采用边界与 Books 判断 |
| --- | --- | --- |
| [AMD](https://arxiv.org/html/2610.02856v1) | §3.1–3.2、4.1、5.1–5.2 / Table 4 | 2+1+2=5。异 sampling 双模型与三次全局 probe、按 task/direction 调节蒸馏强度；probe 参数不提交。相同温度反侧退步，固定与在线对照不在所有 backbone 上一致领先；组合均值不能归于自适应单项。仅报告实验配方；Ch29已有动态能力预算与 teacher 失配论点，不冒称已有 exact AMD。 |
| [Residual judging](https://arxiv.org/html/2610.02877v1) | §3.1–3.4、4.1、5 | 2+2+2=6。SummEval 配对面板支持质量排序与局部残差分账；拟合后残差不认证内在难度，模型失配仍是替代解释。Ch66窄补诊断边界，不采用已验证自动路由结论。 |
| [Multilingual distractors](https://arxiv.org/html/2610.02926v1) | §3–6、Hindi 人工核查 | 2+2+2=6。将答案语言、语义正确与拒答分账；exact-match 误判 script switch。Hindi 人工子集不推广到所有模型；两个 QA 设置同时换 dataset / format，不支持格式单因果或共享 tokenizer 容量定律。Ch66窄补测量反侧。 |
| [OLMo-Detect](https://arxiv.org/html/2610.02986v1) | §3–4.7、5.1–5.4 / Table 6 | 3+2+2=7。Matched / shifted nonmember 对照及去 curated-math 反侧支持混杂控制，不证明独立训练阶段因果。灰盒能力、残余重叠、被排除域与 cross-domain failure 限制泛化；AUC 不等于隐私保证。Ch72窄补审计人口与阶段控制。 |
| [Knowledge accessibility](https://arxiv.org/html/2610.03052v1) | §2–5 | 2+2+2=6。Last-query hidden state 学习中心/方向权重，5 seeds / held-out QA；重复一致也可稳定错误。跨模型 ordering 不等于中心或概率校准迁移，reasoning 较弱。仅报告受限 generation-free probe；不能当 weights 知识证书。 |
| [Reasoning-language RAG](https://arxiv.org/html/2610.03136v1) | §3–6、Tables 2–3 | 2+2+2=6。同 query / evidence / output 下改变 reasoning 语言；German 对 French 的局部改善不超过 unconstrained English。585 single-passage / 30 human multi-hop、单 fiction 域、同 family judge 与精度未披露限制推广。Ch76窄补语言轴分工，不建立强制同语默认。 |

性能/部署保证不在以上采用范围。适用条件与未披露字段由正式报告保留；未实际检查的代码与运行不宣称已核验。拟改书项已读现有 Ch66指标/judge、Ch72 membership、Ch76多语检索邻接，由日报作者窄写，root 另做实际写后检查。此文件不是整日完成证明。
