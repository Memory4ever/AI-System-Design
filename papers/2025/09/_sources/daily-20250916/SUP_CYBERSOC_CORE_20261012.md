# Sep16 CyberSOCEval必要核心

作者Meitner。官方publication Sep15日标签与标题/完整题摘已读；当前official下载26页PDF是Date Sep15/Revised Nov6，不倒填早版。精确2509.20166v1 HTML原件HTTP200，header arXiv Sep24、author Date September15；当前abs v2无withdraw/correction comment，v1 submitted Sep24/v2 Nov10不能覆盖更早的官方事件。采用Sep15官方事件与未标修订的v1必要证据，日期/版本关系交Cicero实际独核，不用提交时间证明公开。

准入潜力：通用推理优势不必迁移到新任务，输入更多模态也不必单调获益；原文有实际text/image/both局部反侧，不仅增加网络安全题库或leaderboard。作者已实际读v1 §3、§4、§5.1–5.5与Appendix D；不穷举26页或代码。

§3 malware609 MCQ使用Windows Hybrid Analysis日志，Llama3.2 90B合成题再专家编辑；TI588题/45报告，Llama4 Maverick/3.2生成及专家验证，逐页图像、少量纯视觉题。multiple-correct必须全且仅选正确集合。§4逐模型修改prompt保输出可解析，provider默认temperature/topP/thinking，无等预算同模型TTS干预，Figure8/9分母为parsable responses。因此跨模型思考优势未显不能证明训练原因、预算无效或新Scaling定律；准确率仅作者本协议结果，不外推SOC真实成功率。

§5.2 text-only通常优于image-only，both近似或低于text；数据偏文本，纯视觉题少。Figure11文字描述给具体案例：六模型image-only均正确，text-only仅o3，both仅o3/4o/Gemini2.5pro三者，支持该样例冗余文本可干扰图像，不支持所有模态组合普遍退化。未像素读所有figure，不采用未见图精确数。

§5.1文件detonation代理不涵盖真实fileless/资产外传等全部攻击；§5.3安全特定推理训练是作者假说非已控因果；§5.4 MCQ非自由任务/行动，合成Llama题存在模型偏置风险，组织分布不同。Appendix D signature描述截50字符可能失多命令信息，hash映射为unique字母主要处理tokenization；full/filtered无一般统计显著差不等价于语义无损。未核代码或复现，无生产安全保证。

Books实际核验：作者已实际读MULTIMODAL-REPRESENTATION Ch23 704–733贡献与当前可靠性两gate/冲突/弃权或单模回退、988–1002模态支配；PLATFORM-EVALUATION-SYSTEM Ch66 244–269评价identity及894–916response-rate/conditional-vs-unconditional质量。Cicero实际§3独核官方Sep15事件、精确v1必要§3–5及对应owner/邻接通过。评分2+1+2=5（标准+受影响反侧/安全深入），不是机构/题库数量加分。最终仅报告/Books新写0：本篇新采用是特定SOC协议的跨模型与输入局部观察，未公平干预思考预算/提出新containment或融合可靠性控制规则；不改变已有评价对象/分母或双gate长期链。上述现有论点可解释边界，不替本实验认证，更不把其原则冒成本篇发明。无共享长期gap；不撤销准入、不冒已有覆盖。
