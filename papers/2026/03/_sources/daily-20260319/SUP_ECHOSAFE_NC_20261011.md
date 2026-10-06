# EchoSafe 2603.15800：必要 Source 与实际已有覆盖提案

准备者 resume_mar18；仅本03-19补BJT03-18自然日的既有具名候选，不扩发现。6分（2+2+2）保持；尚未获得非准备者Source/NC通过，不计safe、无Books锁/写入/POST/DAY。

## 1. 身份、范围与停止

[current abs](https://arxiv.org/abs/2603.15800)实际完整题摘与Comments/当前history已读，仅v1、Submitted March16（不是公开日期）；Accepted CVPR2026不自证首公开。本日同批公开日夹证有限复用SUP_LATER_ADMISSION与已有独校，不追精确时刻或会议全史，旧窗口不移动。未见当前具体撤回/勘误信号，不据此声称无更正。采用[exact-v1 HTML](https://arxiv.org/html/2603.15800v1)。实际必要§3.1–3.3/4.1–4.2/Eqs1–7/5.1–5.3/Tables1–4、A.3、B.2/TableB3–B4、B.4、C文字与D限制；未核全部图像/图中prompt、项目/代码或复现。B.1表仅随必要B.2邻接可见，不认证全部单元格。支持与直接反侧已足够，不扩附件。

准入链保留：unsafe-only拒答榜单奖励过度拒绝 → 最小意图改写的safe/unsafe图文机会集与回答后insight memory → 重新考虑拒答率能否评价contextual safety，以及未经gold核验的反思能否长期复用。NC不是撤销准入，也不把成熟治理原则计新分。

## 2. 必要机制、评价及直接反侧

§3.2 L136–142：在既有六类malicious query上用GPT-5作minimal safe rewrite；Qwen-Image生成/编辑Gen、GenOCR图像。保持的是相似场景/语义，不证明像素完全相同或只有意图一个因果变量；全部合成图像的自然噪声/文化线索限制见D。Table2把较低InceptionScore称质量更好，没有充分说明其方向/多样性意义，故不采用该质量因果。ASR变化同时涉及图像构造/场景，不唯一归因于fidelity。

§3.3 L153–156：unsafe分支RR和0–5拒绝质量、safe分支AR和0–5帮助质量，CCR是两分支平均RR/AR的harmonic mean，不是同一pair两臂均正确的joint成功率。不能让总体HM掩盖某一臂/某一category错误，也不能由解释评分认证内部推理忠实。A.3只给GPT5mini/Gemini与human的Spearman .72/.74；已读文字未列校准人口/标注者数、抽样规则、CI，不授独立真值或部署错误率。

§4 Eqs2–7：每次回答后，同一MLLM读取图文query和自己回答，产生insight；用CLIP文本/图像embedding concat作context key，append(context,insight)，cosine top-k把过去insight作为后续prompt指导。无需参数训练也无需运行时gold，不意味着从错误回答自动识别可靠教训。Raw QA与derived insight身份分开；相似context没有安全意图/权限的保证。§5.1每category空bank，§5.3另跨category不reset；二者是不同state机会集，顺序/随机重复、safe-unsafe伴侣是否进入前次bank、held-out独立bank/去重、capacity/淘汰与tenant隔离未充分披露，不授终身安全提升或已排除测试信息复用。

Tables3–4三7B模型；8×RTX6000Ada48GB/default inference，precision、完整runtime和输入输出长度/batch、stream顺序/seedCI未齐。Table3 Qwen physical-harm safe AR从100降88、Sex从99.1降89；Table4 MSSBench-embodied safe100降39.21，unsafe升91.58。这些说明局部harmonic收益不等safe帮助全部保持。Qwen MME-P1688.09降1637.31、TextVQA77.73降77.01；LLaVA MME-C357.86降294.29，不照录“nearly lossless”普遍结论。

B.2/TableB4：similarity87.9/3.5对random80.8/3.0；insight87.9/3.5对rawQA76.9/2.1。支持该配方的受限内容/检索比较，不证明reflection唯一因果，内容长度/生成与全部预算等价未足。TableB3 k增加不单调（hate CCR k3=97.6、k5=96.8），top-k只控制读取条数不控制无限append。B.4仅报告额外Qwen3Guard-Gen8B筛写、约97%insights被视作safe且整体性能近不变；未披露该比例人口/判定细节/攻击污染率，不把它误写成poisoning实验、事实正确率、无污染或可跳过admission。

§5.3 1.33×平均推理时间与1.69×FLOPs只所测Qwen/benchmark口径，非固定额外deadline或全服务费用。需分账原回答、反思、CLIP encoding/检索/索引和不断增长bank维护、可选guardrail与判分/数据构造；没有独立tail、容量/删除隐私或高风险部署保证。必要prompt图未核，不补精确recipe。

## 3. 实际 sole owner 与具体 NC

实际ROADMAP定位sole **AGENT-MEMORY** [Ch77](../../../../../books/part-07-agent/77-memory.md)。完整相关邻接已读：L1–45 state与authority；L130–185失败反思/内容credit/规范经验交接；L185–235受约束read/context与授权，及Ch76/78开篇。具体承载而非仅主题相似：

- L138–150现有失败反思分支正把natural-language reflection视作待审procedural候选；低风险/verifier缺失可保留直接反思，但绑定原trajectory/source/有效期/纠正入口；同模型自述不提交真值。EchoSafe无gold self-insight是该现有分支的图文局部证据，不改变writer authority。
- L185–218现有read正区分原始episode和索引表示，按当前task/budget选择；返回source/time/confidence/supersession，recency/reuse不授正确性，跨question持久化与episode空memory不共同认证长时策略。实际涵盖context-key检索derived guideline与不同bank/reset人口的采用边界，不声称已有精确CLIP concat/top3公式/全部Echo数字。
- L129现有accept/poison分母与任务效用分账，L181双经验proxy与规范judge不拥有安全authority，实际涵盖额外guard筛写及共同偏差风险。不能因97%safe proxy就写可靠教训或永久安全。

本family的paired评价交接只定点读 **PLATFORM-EVALUATION-SYSTEM** Ch66 L879–906：L891–893已在相同task framing下拆benign/borderline/positive refusal机会集、strict/partial compliance、harmful内容与judge identity，L896–898已分input/output方向分母并保benign帮助与should-refuse两机会集/Unknown。它足够消费这里RR/AR的局部新验证；不是为同family分配第二owner，不把生物研究引用视为Echo协议真值，不声称现文已有CCR公式或此benchmark。

**提案：具体已有覆盖 NC，不写Books或源注，不强造名称/图文案例diff。** 新benchmark局部验证、顺序/reset/合成图/guardrail人口和safe帮助反退留Report；尚未证明的长期安全/无污染、lossless、真实场景因果或全费用不进入采用链。无需为这些不采用宣传提出阻塞请求；若以后出现具体复现/勘误改变既有写入authority或state评价解释，仅重开该命题。等待非准备者必要Source/实际NC裁决，不能借作者笔记预支通过。

当前终态：resume_review17_18非preparer必要Source/actualCh77具体NC正式PASS，已本日独核§1持久化，root接纳。独核定点发现相邻B2 Qwen FigStep hate safe QS为9.0、超已定义0–5尺度；本审不采用该格或普遍judge可靠性，不据此扩全表/全部附件。保6分、具体NC，不写Books/源注或虚POST；详细非作者审阅范围以本日独核实际记录为准，不授DAY。
