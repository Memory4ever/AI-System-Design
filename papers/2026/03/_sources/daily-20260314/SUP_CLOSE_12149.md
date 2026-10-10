# 12149 Linking Perception：实际局部 delta 与最低关闭提案

mar14_supplement；仅03-14/Mar13自然日。精确v1完整title/AB与八作者Yuetian Du/Yucheng Wang/Rongyu Zhang/Zhijie Xu/Boyu Yang/Ming Kong/Jie Liu/Qiang Zhu已真实读；CVPR2026 accepted不是具名已知早公开稿，不制造全网无早稿请求。SUP_INDEPENDENT_NARROW.md准入与SUP_INDEPENDENT_DATE_NARROW.md十项本ID日期实际PASS复用，arXiv日级事件Mar13；不授submitted/registered单独firstpublic。

官方exact https://arxiv.org/html/2603.12149v1 GET200/347546bytes/2026-10-10T02:02:00.663176Z，SUP_NARROW_CONFIDENCE_MANIFEST_RESULT.json及SUP_NECESSARY_12149.raw/txt。本人实际读 §3全Eq1–10/模块接口(B38–82/97–99)、主Tables1–4全部与§4.1–4.4/实现反侧(B83–156)、§4.5/结论(B157–161)、D讨论完整B325–327；A必要模型角色B231–239、B数据筛选全段B272–294已定点补读，另B240–254的T5/6部分输出不当完整表已核，不认证全prompt图像/其余表/源码/复现。长raw rg曾截断，不用其认证全附件或完整归一函数。

实际新增是original/noise成对生成后把confidence差与正确/错标签关联加入GRPO，并将其与confidence投票/专家critique/VCD组合。原P保留：局部适配/推理配置值得核，不是无贡献或仅主题；不因含hallucination、calibration或三个模块自动高分。成熟GRPO/VCD/投票/多角色复用原则不另计增量。

**Design1+Reach1+Durability2=4，最低关闭/仅报告Books0提案。** 原文新增这一组件recipe而未形成新的校准有效条件、独立perception证据权限或强计算预算选择保证；影响主要局部适配/推理配置，不把模块数量或潜在章节映射计Reach。具体扰动/置信口径与校准取舍有稳定价值2，但不为所称free lunch/根因/SOTA加分。必要身份/日期、actualdelta与下述直接反侧已充分，可停止，不展开全部benchmark或准备Books gap/PRE；不是NC新实验已吸收，不撤P/改EX。

Eq3 C是每token top-k logprobs的负均值再序列平均，不是生成token自身likelihood或独立正确性概率；正文明确C越低越确定。Eq4却用ΔC=C(original)−C(noised)及 +(2correct−1)Cnorm，Eq6以C作正票权；D又称Normalized Mean Log-Probability。必要定义没有统一交代从NMLP到高值代表高自信的方向/变换，不能补造唯一可执行reward/vote符号recipe，更不能认证原式实现已正确。若直接以原C与正α/β解释，原图更确定的预期ΔC<0会得负perception项；保留这一限定歧义，不宣称所有代码必反向或所有实验false。只读原稿不扩审未必必要代码来修复作者协议。

§3.3.4 Planner要求三模块恰好各一次，顺序只向共享vote字典贡献；没有由可靠confidence确认的skip/退出门，不能照摘要写按需少算。Voter verbal概率不是外部真值，reflection与VCD仍生成器提案，唯一专家会影响planner/voter/critic，单case纠正不证明消除全部single-point-failure。8samples/T1/topk40、三票重.5、VCD额外两图推理、Voter最多3retry，专家Gemini2.5Pro全部计费；4原/noise rollout pairs及8H100141GB BF16全参训/batch2，不是free lunch或相同总FLOPs/成本优势。serving hardware/precision/concurrency、在线SLO与完整expert/OCR/calls成本未披露。

Table2 MathVision CDRL OE18.46<base24.24而MC改善，不统一无损；CA-TTS那行OE/ALL同37.99，与其他栏及正文不能补成无误整表。Table4 Origin ECE64.57→62.24、AUC54.81→59.42以及noised AUC60.00→60.19只支持此metric局部改变，不授新环境已校准/真正知道不知道。CD方向与实际C变换关系没有完整协议，不自签观测为唯一视觉依赖因果。Training dataset1936来自六benchmark，主文称LLM pipeline而B称manual assessment，筛选具体recipe未统一；noised由CLIP attention构造，训练/噪声质量和image曝露皆treatment；未提供本命题完整配对独立性/全null上下文控制。叙述平均SOTA、scaling斜率未隔离expert额外费用/训练质量，不能推所有MLLM幻觉根因由perceptual bluntness唯一造成。

待非准备者必要原证/评分最低处置核验后才能正式；不授DAY/代码/复现，不因工作量或Books已有主题关闭。
