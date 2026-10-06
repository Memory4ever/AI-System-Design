# 11947：精确 v1 必要审阅与最低关闭提案

root 准备；尚待非准备者复核，仅03-14补Mar13自然日。完整题摘、身份、日级归属和纯Submitted venue门的有效独核复用。官方 [exact-v1](https://arxiv.org/html/2603.11947v1) 实际 GET200/228491bytes，UTC2026-10-10T01:30:06.599040，原件 `SUP_NECESSARY_11947.raw/txt` 与 `SUP_ROOT_11947_MANIFEST_RESULT.json`；无版本diff、全会议或代码扩读。

## 实际增量与投入

主流内容中心音频适配→用层间诊断选择 LLM LoRA 层0–14、第14层加category/attribute辅助头→比较局部配方能否比全层调优更好保留副语言条件响应。新增是特定表示/层范围/辅助任务组合的实证，不把LoRA、probe、监督双头或安全原则计作新基础。拟 **1+1+2=4，最低关闭 / 仅报告，Books新写0**：局部调优实现1、单音频交互路径1、可复查的层范围/旁侧效用与语音人口边界2。不是由NC、阅读成本或论文数量倒推降分，也不因child-safety名称自动认证发布/安全合同已改变；安全结论只留受限评价，不作权限或生产证据。

实际读取 §4.1–4.3 probe/相似度/logit lens、§5全部机制/Eq9–11、§6.1–6.3训练/人口/指标与Tables2–6、§3合成安全样本及§8限制。采用 HTML blocks39–82/86–107/114–158/161–169；初次全输出截断未读部分另按blocks60–129定点恢复，未读图像pixels/代码/复现。LLM侧LoRA、audio encoder冻结；两A100/10epoch/batch128/LR8e-5/约70min，模型具体size/checkpoint、precision、输入输出长度、LoRA rank/slots、推理batch/并发/完整latency/SLO Not Disclosed，不能把时间认证为同资源全层成本比较。

## 支持与直接反侧

辅助头取第14层平均音频hidden，由题目类别真标签选择attribute头；训练总目标为SFT加0.5倍两分类损失，头在推理丢弃。可读probe/同内容相似度与最后层top1吻合不识别唯一内部功能区，固定层号不外推其他backbone。训练9000合成音频和GPT4.1条件target；评估1200记录含200个gender私测而不纳入主结果，不把全部1200当§6.2分母。

Table2 Qwen full PE-FT 的age .945低于无头 .960，Kimi gender .965低于无头 .970；两模型VoiceBench HS均低于vanilla，Table5也非每属性第14层最好。Table6 Kimi在另TTS/新speaker的PA-rate退到68.5/75；不能授一般语音人口或无损保留。PA-score是judge的{-1,0,1}均值，PA-rate是其+1比例，不是真实风险概率。70合成child queries的属性响应不证明真年龄或真实安全；gender设定仅作者简化声学标签，不授现实自我认同。

这些局部数据可检验配方和表达保留，却未证明选择层是内部唯一因果、统一属性最优、真实用户安全或更低完整成本。最低处置保留上述证据与限制，不把新实验写成已吸收；本提案不要求Books写入/PRE/POST，不授Source独核或DAY。非准备者只需核决定性原证、评分/处置，无需遍历引用文献、五图pixels或全附件。
