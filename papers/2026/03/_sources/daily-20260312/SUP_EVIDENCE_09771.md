# 2603.09771 — 参考概念 token 缓存与原生读出（ready）

[Ego exact-v1](https://arxiv.org/html/2603.09771v1)。作者实际完整§3–5/Tables1–3，AppendixA、B.1–6/Tables4–9；未核图像像素、B.7、repo/复现或全部dataset附件。读取supplement_html.py S3 S4 S5 A1 A2.SS1–6，stdout。batch3完整AB/current/history与原字段actual读：owning arxiv.content/findable registeredMar11UTC02:21:32已可发现上界及official noadvance/公告最早Mar11BJT08下界同日夹证，Submitted不单独public。currentv2同AB/acceptedCVPR无可见withdraw/correction，v2Mar11提交但公开上界Mar12不回填本窗。精确题名定点搜索仅作身份/先稿轻核，CVF正式HTML访问403，搜索cvfsupplement同题五作者且为2026会议稿，不用crawl年月充先公开；未见具名更早正文冲突，不扩大conference/history。

2+1+2=5；唯一MULTIMODAL-REPRESENTATION，具体带名称的selected raw projected-visual token缓存/softprompt读出差额加深，不把Agent持久记忆或名字绑定本身给分。

## 方法、必要条件及直接反侧

§3.1–3.2每reference生成keywords、取text→visual attention；Eq3实际对words/heads/layers平均，与文字“maximizing”不一致，以公式采用平均proxy而非max实现。TopK后恢复原patch顺序，存原VP输出XR选中行，而不是将多层contextual hidden混成新向量；多reference分别选后concat，name配该concept，作为softprompt送LLM。不是新参数学习/encoder重训，不认证selected tokens全是主体或semantic identity真值。内部attention读取也不表示attention就是因果解释。

§3.3Kc=min(K,alpha*Nr/100)，alpha由同模型估计主体面积，不是segmentation truth；整数化/零集合退路未闭合，不猜代码实现。§3.4一次COCO2017 train真实singleinstance segmentation calibration，按topKpatch mask overlap选topL；B2实际Intern29/30/35/36/39。不是无标注/所有model通用层，与用户每concept零gradient须分账；旧token必须绑定encoder/projector/model/层规则与参考来源，换版本不认证直接通用cache。超context可检索只是proposal，本轮不授全部manyconcepts无损检索实现。

§4/A InternVL3 14B主、Qwen2.5VL7B、448²/tiling1、2A100 inference，RAP8A100/b6/LoRA32 finetune；Ego无gradient但参考生成/attention提取、面积估计、COCO校准和context消费仍费用。precision/生成长度/并发/seedCI/完整SLO未披露。F1由概念population P/R计算的口径与multi汇总需保留，不将混合平均等同单人口；T1/T8 multi Ego93.9/78.2对应普通harmonic85.33而表88.6，未解释aggregation，不自修或采精确普遍排名。

真实反侧：T1Thisismy single五reference InternF175.1低于一reference79.1/PeKit五78.1；T3一reference20% token F180.4低于full84.1，五reference85.7>full只同context数量而非同全部参考处理费用。T2单VQA92.3/88低于RAP97.6/90与PeKit94.6/92，runtime6.0高于PeKit5.8，不授所有性能/时间优胜。B1动态K提高F1但P81.3低于固定82.4；B4多次keywords sample五view73.4<deterministic75.1；B3五viewkeywords86.1/68.7/76.5与T1 87.2/65.9/75.1有口径差异，不拼因果。原recognition每图跨全部concept positives稀少，caption names recall不验全部描述真实性，openVQA ChatGPT judge非独立事实/人群真值。B6 2Bfalsepositives更强，能接softprompt不是所有base都有效；不据其数据否定全部tiny未来能力。

## actual owner 与逐字PRE

作者实际Ch23 667–700完整reliability→LiteEmbed→taxonomy→caption邻接，以及前轮同日Ch22/24开篇仍有效。LiteEmbed优化新的text token，有训练目标；现videoKV记忆有clip上下文但非带conceptname的原projectedtoken只读cache。拟LiteEmbed完整两段后/语言taxonomy段前补这条少参考免每概念gradient的替代分支；不改原适配路径，不给Ch77再复制。

拟段1：

新概念也不一定要先优化一个 text token。若模型已能跨参考图辨认对象，可从每张参考图生成描述词，用词到 visual tokens 的 attention 作为选择代理，保留高分 tokens 并恢复原 patch 顺序；将这些原 projector 输出与概念名称一起缓存，后续作为 soft prompt 与新图共同读入。这省下每个新概念的梯度更新和参考图重复编码，却不把 attention 高或名称相同当作主体身份真值。多视角分别提取后拼接，也仍可能保存背景、近似对象或冲突来源。

这一[受限概念对照](https://arxiv.org/html/2603.09771v1)还按模型估计的主体面积缩减 token 数，并用一次有分割标注的校准选择层；零每概念训练不等无监督、无制备或全模型兼容。模型、projector、层/选择规则、参考顺序和名称须共同版本化，面积代理和少量 tokens 不保证细节覆盖；更多参考或更小 memory 也可能使识别、VQA、precision 或 latency 退步。校准、参考描述/attention/面积提取、存储与上下文读出、检索及原任务回归均计费；误识别、来源冲突、换模型或预算不足时，保留原参考图、普通检索/完整 tokens、经核的 token/adapter 适配和拒认，不让缓存向量批准个人身份或持久事实。<!-- source-family:SF-2026-ARXIV-2603-09771 -->

root必要Source/date/具体owner/逐字PRE实际通过；作者Ch23 LiteEmbed两完整段后/taxonomy前写新683/685及本人1275，顺读675–694完整局部与自身注。root非writer实际顺读677–690完整邻接、新两段与自身末注并回必要原证/PRE，actualPOST通过，锁释放。可计本日确认，不授DAY；root实际原证范围由独核note记录，不反称其B3–6全读。
