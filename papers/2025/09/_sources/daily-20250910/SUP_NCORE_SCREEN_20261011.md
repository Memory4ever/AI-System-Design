# Sep10 necessary core screening

作者Meitner；本日新72身份，精确v1 HTML优先，以下只决定准入的增量/反侧/成立条件，不称全面Evidence。原件统一为 `SUP_CORE_<ID>v1_20261011.raw` 与同名 `.request.json`，33项实际200。未读附录/代码/完整版本不自动外部阻塞；潜力已清楚而仅公开日未证可以停止。无拟采用实验数字或普遍安全保证。

## 作者实际必要局部18项

| 身份 | 实际读到位置 | 实际新增与P/C理由 | 未读/未采用边界 |
| --- | --- | --- | --- |
| 2509.06830 | §4.1/3/8.2 | C：标准ViT+DINOv2 teacher/student、patch/regularizer，换大规模CT/MRI和augmentation；跨CT/MRI organ结果是此数据/领域验证，未定义独立基础表示新机制/成立条件。 | 其余clinical19任务/全部参数未穷读，单中心/2D+任务head限制保留，不授全医学能力。 |
| 2509.06902 | §3.3/3.4/4.1/4.3/5.1/5.2/6.1/6.3 | P：claim-bound numeric token与renderer-owned badge，明确exact/round/alias/tolerance策略和fail-closed。真实性/推理≠claim一致；可信标记依赖确定性parser/renderer。 | 未读sample implementation/密码扩展全证明；不授dataset真实、token召回或prompt injection全面安全。 |
| 2509.07367 | §3必要架构/规则表/验证与反馈段，§3 Px4/Px5/Px6定点完整补读；Discussion .1/.2/.3 | P：先实例SAT assignment/UNSAT DRAT验证再性能reward；单headline feedback造成SAT/UNSAT偏向，初无规则错误/退化；人工verifier与介入是自动化边界。 | 原首个宽方法输出截断后已定点补关键段，不称全§3/31页读完；全部solver细节、代码、竞赛复现未核。 |
| 2509.07430 | §4.1/4.2/5.1/6.1/6.2 | P：预采样reference把near-perfect保留与困难探索分责，forwardKL/JS generator loss免online reference；keep/explore及域外Pass@k退化是具体RL目标边界。 | theorem/全附录未核，不授一般monotonic improvement或仅divergence独立因果。 |
| 2509.07558 | §2.2/2.3/3/4.1/4.4 | P：逆长度权重在固定scale的线性无偏组合下最小方差，α折中长response信号。证明假设Var∝length、忽略token covariance及近似group-gradient独立，非真实RLVR普遍无偏。 | 当前题名VL Norm不单独重大；未核全Appendix/训练实现，不把局部方差结论扩为全GRPO失败。 |
| 2509.07595 | §3.1/3.2/3.6/4.2/6.1/6.5/6.6 | P：两级plan/context filtering的部署条件与局部反侧，漏path→dummy参数、重复写/漏写；FaaS session_id/DynamoDB/S3处理临时状态、非持久/tmp与依赖限制。实际有新失效/运行条件，不是MCP/FaaS术语即入选。 | 全three-app量表与artifact未核，不授通用正确性/成本最优；本文自己无dedicated recovery。 |
| 2509.07596 | §4.1–4.3/5，D.1/F.3 | P：保持perceived-gender的对象/背景扰动改变YGap/MaxSkew，需bias与feature-sensitivity分开；理论保持marginal假设、相对Δ分母/检测器混杂限制。 | D.1说明200 COCO人评而表列四库，不授全部库完整人验；全图像/统计未复核，无公平普遍保证。 |
| 2509.07260 | §4.3/5.1 few-shot+instruction/5.2/6 | P：FS1/3/5特定任务collapse、class-majority输出与FS10变化，是小模型提示/评价条件反侧，不靠小模型榜胜准入。实际4bit iPhone测试对非相同health checkpoint。 | 随机8:2序列split/10 mobile samples限制，SLM优于LLM与隐私/实时不采用；全distribution图像未读。 |
| 2509.07188 | §2.1/2.3 comprehension/3.3/4.4/5.1/5.2/8 | P：控制simulated user literacy/education使expressive strategy与factual稳定性分离；对话/summary comprehension作为不同outcome，模型大小不等用户适应。 | LLM PatientAgent不是真人，49case/两clinician judge agreement只局部，未采用医疗有效性/真实理解。 |
| 2509.07588 | §4.1/4.2/5.5.1/5.5.2/6 | P独核通过：masked mention→局部GAT/linearizedKG entity对齐，MLM+alignment后丢GNN；去MLM/换entity pooling及graph-vs-linear容量条件改变训练输入选择，不仅domain榜。 | InfoNCE公式显示分母索引疑点未解决，数字/机制因果不采用；未核全部task/data。 |
| 2509.07727 | §3.1/3.2.3/3.6.1/4；3.6.1已补完整 | P：expert频率不等敏感性，层位与reasoning/instruction不同退化；localnoise可以改变compress/offload选择。实际模拟Gaussian noise而非运行SZ3/CuSZp，不能把std“error bound”当确定误差上界。 | 全专家/全层量表与压缩artifact未核，不采通用层语义、safe error或加噪普遍增益。 |
| 2509.07846 | §IV/IV-A–C及V-A | P：coherently altered corpus与parametric事实冲突，large/dense scope下localgraph对vector选择可能逆转；统一query prompt去掉graph“外部知识”混杂。 | MCQ fuzzy GPT judge/事后选已有answers的branch proof-of-concept，不授在线全成本最优、真实课堂安全。 |
| 2509.08031 | §4.2/5.2/Limitations | P：同四speech task的text/audio instruction输入不同会改变reasoning量表；标准prompt/词级时序metric不能消除所有敏感性。 | 具体model配对/完整实验budget未核，9.5point与127%速度不采用，闭源rate-limit/back-end依赖保留。 |
| 2509.12235 | §3.1/3.2/4.1/4.3/6 | P：GeneralPoints改card-rule的OOD checkpoint轨迹，RL恢复SFT遗失而不超过最佳SFT且有staging边界；vector-direction干预是局部表示反侧。 | 两base/任务边界与正文8B/7B标记差、单stage/Navigation/其他RL附录未核，不能授RL永无新能力/普遍rotation机制。 |
| 2509.07642 | §3.1/4.4/5 | C：agency hidden characteristics/actions映射已有benchmark/monitoring/DoLA/RLHF，实际文献problem-solution分类，未给独立执行机制、可靠性条件或修正既有设计的证据。 | 安全例子实际核，不将概念类比当安全保证；未穷读全部literature。 |
| 2509.07759 | Introduction Contributions、§5.3/7.1/7.2/8 | C独核通过：汇总pooling/unit mismatch/结构缺失、已有paradigm及未来span+doc双标注；未发现本文新增可判定条件/独立验证，非按survey标签关闭。 | 未穷读所有被引paper/应用；如新证据指出具体新evaluation命题仅重开该段。 |
| 2509.07794 | §4.2.4/4.4.3/7.3/7.4/7.6/8 | C独核通过：grounding/capgraph/filter/distill为既有QE设计分类，ExpansionGain/AddedTerms/FacetCoverage没有定义可操作QE归因/新相关对照条件，未给具体新有效性/归因结果；不是所有概念工作都关。 | 7.6具体新评估提议已经核，未穷读全部taxonomy引用；具体新命题仅重开该段，不用日期hold遮未判。 |
| 2509.09716 | §2.3/3.2/3.3/4 | P：text-first→style→naturalness gate与多属性/变style、语言偏好条件区分语义正确和声学控制，human/judge对应不是单leaderboard。 | 相同guidelines五expert/半instructions rank相关不证judge全部可信；seed+LLMexpand分布和hallucination限制，展示音频未验。 |

## 非作者实际15局部有效层

Cicero实际官方精确HTML读到的位置/判断全文见[独核§4/5](SUP_INDEPENDENT_20261011.md#4-新72题摘与首批必要局部校准)，作者已实际回读该表并保存33 raw/request；不伪称作者二次全文。

| 身份 | 实际section与新增 | P/C与边界 |
| --- | --- | --- |
| 2509.06870 | §3/4/6 mixture ablation | P，hard minority-wrong+easy人口决定aggregator recovery，不授所有majority劣或通用效率。 |
| 2509.06952 | §4.1–4.3/5.1–5.3/8 | P，comprehension与production中CoT/RSA收益不同、self-preference judge；100stimuli单轮不授所有协作。 |
| 2509.07485 | §3/4.4/4.5/6/AppC | P，nonAR anchor score/order-vs-ID perturbation，多view过多退化；不授100x端到端。 |
| 2509.07463 | III-C/D、IV-D/E、V | P，frozenVLM输入blend的日夜/shift失效条件；100scene/颜色text不足不授collision安全。 |
| 2509.07238 | §3.3–3.5/3.7/4/5.4/5.6 | C，实际无model inference仅模拟估算，generic grid无新机制/成立条件；不因数字不可信降有贡献者。 |
| 2509.07488 | §3.4/4.4/5.2/6 | P，direction/sequence metric盲点与vision-only/frozenLM崩；不授导航保证。 |
| 2509.07274 | §2.2/2.3/3.2/4.1/6 | P，LOO human比对/None系统错，早期历史低可靠；current统计correction概述不等v1实施后续DSL。 |
| 2509.06858 | §2.1/2.3/3.3/3.4/4 | P，interaction/bias分离及framing/attractor条件；拟合不是真人社会因果。 |
| 2509.06883 | §3/5/6 | P，regurgitation高METEOR/gold缺图与claim、self-refine幻觉；人工少例不授排名普遍反转。 |
| 2509.06938 | §2.3/2.5/4/5 | P，乱序concept/SAE+PLS关联与选中高hallucination组干预；HHEM非人工真值，不授普遍causal detector。 |
| 2509.06941 | §2.2/3/4.1/6 | P，RL unsolved diversity转移衰退、naiveUCB train/test不一致与bonus hacking mask；非普遍RL伤害。 |
| 2509.06838 | §4/4.1/4.2 | P，Persian六维总体强不掩safety局部弱；本地文化规约≠全安全，不授training原因。 |
| 2509.06953 | §3/6 | P，static expert/kinematic BC对dynamic碰撞，privilegeddistill+点云goal调节；Panda/点云边界。 |
| 2509.07184 | §4/5/7 | P，pretrained高维embedding使unknown-k内部指标失真，normalization/reduction改变可用性；非全无监督。 |
| 2509.07133 | §2/3/4 | P，adaptProportion feedback/invalid与去偏取舍；global removal可优于personal，不授隐私/所有personal优。 |

33必要局部是准入层，只有官方Seedream单篇取得标准Evidence/Books处置。三项校准P/C/C实际通过，光学同题六作者旧公开命题处置见[逐项筛选](SUP_SCREEN_20261011.md)。未读附件与未复现不称外部受阻；日期门后不扩大全文。准入普通待办0，来源/六部分行政及独核由README维护。
