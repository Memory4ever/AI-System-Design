# PowerFlow18363：必要 Source / actual owner / 最小 PRE（待非准备者）

仅本03-21补BJT03-20自然日；准入和日级夹证复用SUP_FIRST_ADMISSION具名原字段。作者resume_mar18，未授非准备者PASS、Books锁、实际POST或DAY。精确原证为[2603.18363v1 HTML](https://arxiv.org/html/2603.18363v1)；不比较后来版本/不核代码或复现。

## 必要实际审阅与支持边界

实际§3.1–3.3/Eqs1–10、§4.1–4.3/Table1、A.1–A.2、C.1–C.2和Table2、E已读：固定base整条response密度提出alpha-power目标，再用长度归一TB residual与prompt末hidden→3层MLP的logZ'估计器共同训练policy。训练获得的采样器不同于部署逐token调温；冻结base评分、额外normalizer、轨迹生成/权重更新并非免费或纯推理替换。拟2+2+2=6：整序列密度目标→长度修正后的目标身份→训练与部署采样分责是新增机制，非“似然不等正确”成熟原则加分。

关键数学边界：Eq7/8把prompt级Z改为Z'^L，因此零残差对应p_base(y)^alpha / Z'^L，而非Eq1纯alpha-power；Eq9另含长度乘入的格式惩罚。§3.3 L161和E L447–449自己承认跨长度mode ranking不保持，不能采用摘要/§4.2的严格ranking、多模态结构保持或“完全消除长度偏差/length invariant”。不同长度L1/L2的比值新增Z'^(L2−L1)，可变排序；固定长度才取消这项。裁剪detach importance ratio也不是一般无偏off-policy证明；Eq4 equilibrium期望梯度或有限参数训练收敛不由机制描述授予。提高原模型密度可能提高共同错误，flatten可能增加不连贯输出；不把Cook复杂性或识别生成不对称当correctness证明。D的有限输出、唯一mode、精确期望迭代定理不是本有限LLM训练结论，未采用/不继续补全proof。

评价：18k NuminaMath queries过滤长度/潜在泄漏；创意300训练/200测试prompt，非全开放生成。Reasoning T=top-p=1，avg@16是逐题16样本平均准确率，不是pass@16或majority；创意30样本，T=.8而High-temp1，BGE语义余弦/ROUGE-L与Qwen3-plus judge只是代理；推理strategy judge DeepSeekV3.2亦非正确轨迹oracle。训练batch128/N16，reasoning采样T1/creativity.7，LR按模型/用途不同，alpha4/2/.5、clip低.2高.28；normalizer dropout.1，额外base scoring/16rollouts/调参与judge费用保留。设备、precision、最大长度、更新总token/wall/GPU-time、并发、重复seed/CI未披露，不授端到端省费。

直接反侧：T1 QwenMath7B均值42.17<GRPO42.38，MATH78.1<GRPO78.4/TTRL80.4，Olympiad40.1<GRPO42.5，AIME2420<GRPO22.7；QwenMath1.5B AIME2410.8<EMPO12.3/GPQA28.3<EMPO29.5；LlamaGPQA30.2<Intuitor/GRPO30.5。T2 Qwen3B poem judge.4675<Instruct.4678，semantic diversity.2085<VS.302且ROUGE-L.1544<自己的instruct.2024不等全部方法最佳；总体提升不认证全任务或保持所有指令能力。E明确多数RLIF/One-shot用外部checkpoint配方不同，inhouseGRPO声称配置匹配但未等全token/cost；不能将全部收益归纯目标或宣优于监督。C.2 base在Olympiad大n256追平/超过仅受限支持采样效率解释，不证明全LLM能力上限。

## actual sole owner 与差额

唯一TRAIN-GRPO/[Ch33](../../../../../books/part-04-training-system/33-grpo.md)。实际读50–85完整reward来源→参数依赖梯度→Latent-GRPO→同题baseline，675–711 verifier条件、1200–1285诱导分布/蒸馏及1360–1418 rollout接口；Ch31/32/34开篇交接实际读。现Ch33 L66–74已解释参考答案似然、长度归一和无verifier hidden一致性，但没有冻结base整序列密度→learned长度normalizer的无外部答案采样器目标。既有Sept诱导teacher/student分布分支保持共同目标，反而须与本长度重设目标区分，不能假NC或覆盖现有段落。拟放L74 latent成本反侧后、L76“组采样的关键…”前；一段作为reward替代目标，不重复Ch20采样公式。

## 逐字 PRE（未写）

没有外部答案时，也可以不为每条 rollout 构造“正确性 reward”，而是把冻结 base 的整序列密度作为拟合对象：以幂指数提出 sharpen 或 flatten 方向，再共同训练采样 policy 与 prompt 条件的归一估计器，将昂贵的分布拟合移到训练阶段。长度进入这里不是中性的缩放；一条[长度修正的受限分支](https://arxiv.org/html/2603.18363v1)将 log-density mismatch 按长度归一，并把归一项改为随长度累乘，因而跨长度的目标排序已改变，不能仍称严格保持原幂分布、完全消除长度偏差或获得正确答案。格式惩罚、采样支持与训练权重也应作为目标身份保存。原密度可能偏爱共同错误，扁平化又可能释放不连贯输出；局部数学和创意评价有任务反退，外部 checkpoint 对照与相同步骤不等全预算匹配。冻结模型评分、normalizer、rollout、调参与独立质量检查都付费，普通解码不代表训练免费。目标或质量失配时，保留可靠 outcome reward、已验证监督与原模型采样，而不让更高似然或更多样输出替答案签发正确性。<!-- source-family:SF-2026-ARXIV-2603-18363 -->

## 静态源注 PRE（未写）

- SF-2026-ARXIV-2603-18363：[PowerFlow v1](https://arxiv.org/html/2603.18363v1)，必要审阅§3/Eqs1–10、§4/Table1、A/C关键配置与直接反侧、E；采用仅冻结base密度与长度修正目标/训练采样分责，不采纯幂分布保持、完全length invariance、正确性/收敛/普遍创意或省费保证。未核实现、未复现；normalizer/base评分/采样/评价全费和原outcome/监督退路近文保留。

## root 非准备者必要 Source / owner / PRE 复核

实际原版本§3.2–3.3/Eqs2–10、§4.1/Table1、A.1–A.2、C/Table2和E相关配置及关键反侧；实际 Ch33 完整45–82与 Ch32/34开篇交接，回对原一段 PRE。Eq7/8与E明确长度 normalizer 改变跨长度排序，原 PRE 不采用摘要的严格幂分布/完全长度不变宣传；Table1 QwenMath7B均值42.17低于GRPO42.38、Table2 Qwen3B诗歌judge及diversity反侧、外部checkpoint与未匹配全部训练费用均限定充分。现有参考答案似然和hidden一致性段没有该冻结base密度→联合学习长度normalizer的目标接口，sole TRAIN-GRPO成立，原6分不变。有限 Source/PRE 通过；可窄写原一段及自身静态注，不增加其他附件审阅或授予 POST/DAY。

## 作者实际窄写（待 root actual POST）

按root sole Ch33本family锁写原一段新74与本人静态注3202，作者完整60–86与末五行本人/邻注已实际顺读，补去仅排版leading-space后逐字PRE一致；marker/static各一，scoped diffcheck空。Latent一致性→冻结base密度目标/长度改变→同题group衔接完整，旧机制未覆盖；待root一次nonwriter实际POST，不预支safe或DAY。

## root 实际非 writer POST

实际顺读 Ch33完整60–88、末五行本人源注并回对有效 Source/原 PRE：hidden一致性之后引入冻结base的密度拟合，再回到同题group条件，衔接没有把新目标误作新的真值。正文和静态注各一，长度改排序、局部反退、训练/评分全部费用与可靠outcome/监督/原采样退路近文完整；限定 diff 检查空。实际 POST 通过，释放本 family Ch33 窄锁，可同步整合，不授 DAY。
