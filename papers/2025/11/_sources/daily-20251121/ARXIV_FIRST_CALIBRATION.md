# 2025-11-21 arXiv首批增量校准

作者Dalton；2026-10-04T18:31:00+08:00。仅本日原站新取范围，不使用别日候选。首批8份具名v1原页题摘实际完整读，7个明确潜在方向、1个准入事实待最小方法段澄清；另1个当前明确撤回。均未授确定当窗，Submitted不等于公开。请root可立即定点校准，不等日级。

## 真实入口与停止

四主题API receipt完整保留实际query/start=0/max_results/UTC执行/响应：learning(35)、system(25)、agent(25)、multimodal(25)，submittedDate Nov19–20仅发现范围，不作public。learning40秒超时，其余429，无有效条目，不写零命中/读尽。learning换arxiv.org原API别名重定向export后40秒超时；缩为ti:LLM(15)仍429，停止同API空追。本日四条原站日期主题搜索在[查询原始记录](WEB_ARXIV_SEARCH_FIRST.json)，首页只返无关physics/晚日期，停止，不扩其他月份/领域。

有界补检实际新取CL月表：旧2511路由404，改官方2025-11路由200。skip350/show25只核定位身份（07457–08017），不将这些题摘入队；确认月表升序后定点skip750/show25，实际读25标题/已有comments（15304–16345），只打开下面相关项与撤回信号，不扫1527全类题摘。原HTML和receipt分别为[定位](arxiv_cl_title_corrected.html)、[目标切片](arxiv_cl_target_titles.html)。已知science标题按ROADMAP暂缓；其余更早边界/应用标题不扩全文。其他窄主题来源恢复仍有普通工作，不授全部arXiv覆盖。

## 八份完整题摘后的判断

原文：[第一批](WEB_ARXIV_ABSTRACT_FIRST.json)、[第二批](WEB_ARXIV_ABSTRACT_SECOND.json)。以下精确URL为v1；当前月表是晚版标题，TS-PEFT和SeSE标题不同，不能用月表补写v1机制或实验。这里只使用实际v1原页显示的完整摘要，必要采用前再核v1正文；没有遍历所有附件。

| 材料与Submitted原字段UTC | 具体潜在准入问题及最低必要反侧 | 处置 |
| --- | --- | --- |
| [Tokenisation over Bounded Alphabets is Hard](https://arxiv.org/abs/2511.15709v1)，Nov19 18:59:56 | 旧hardness依赖无限字母表可能不适用于bytes；摘要给二元bottom-up/direct的NP-complete及无PTAS、unary direct仍hard；若证明成立，固定字母表不解除优化困难。需准确问题定义/约束/归约及P!=NP条件，不能泛化为BPE效果保证或所有tokenisation任务hard。模型基础理论直接在主线，不按无实验关闭。 | 潜在，日期未定；MODEL-TOKENIZER路由，不要求owner缺名字 |
| [Liars' Bench](https://arxiv.org/abs/2511.16035v1)，Nov20 04:29:33 | 原检测验证偏窄；按说谎理由/信念对象分层，三种检测器对某些谎言失效，尤其transcript不足判定时。局部反证可改变检测器可用边界；需belief/lie生成标签和heldout设置，不能从错误输出推定内部belief，不能把总样本数当独立性。 | 潜在，日期未定；PLATFORM-EVALUATION-SYSTEM；必要安全反侧须保留 |
| [Learning Tractable Distributions Of Language Model Continuations](https://arxiv.org/abs/2511.16054v1)，Nov20 05:17:19 | 未来约束使AR直接条件化困难；LTLA只条件化HMM latent prior、固定decoder以复用future计算，batched update免词表逐项重评分。需核exact指的是surrogate不是原LM条件分布，以及prefix复用/可比fluency与成本。不是HMM+LM组合本身准入。 | 潜在，日期未定；MODEL-SAMPLING/INFER-SGLANG待唯一owner选择 |
| [TS-PEFT](https://arxiv.org/abs/2511.16147v1)，Nov20 08:41:20 | 所有position施加PEFT可能反而损害效果；摘要明确token选择子集修改与负侧。需selector如何产生/梯度与对照保持，不能用晚标题learnable-threshold补充未读v1方法。小/局部反证可准入。 | 潜在，日期未定；TRAIN-LORA |
| [SeSE](https://arxiv.org/abs/2511.16275v1)，Nov20 11:54:12 | pairwise/概率度量漏掉语义有向结构；定向稀疏图+编码树结构熵，潜在修正UQ判别边界。需NLI/evaluator引入何种预算/标签、随机claims依赖、相对KLE对照，不把entropy分数作真实性证明。 | 潜在，日期未定；PLATFORM-EVALUATION-SYSTEM |
| [SDA](https://arxiv.org/abs/2511.16324v1)，Nov20 13:00:04 | 推理时按alignment instruction重分配概率的training-free控制，可能改变无需重训的偏好控制边界；需究竟何种steering/额外模型预算和3H评价，只看摘要数字不足正面采用，但方法潜力清楚，不因缺实验细节关闭。 | 潜在，日期未定；MODEL-SAMPLING |
| [Self-Rewriting Reasoning Reinforcement](https://arxiv.org/abs/2511.16331v1)，Nov20 13:10:52 | correctness reward欠内部过程约束；只对稳定答对的simple样本改写并同batch，试图保留原GRPO奖励信号。需选择条件/改写采样是否改变group统计、length/accuracy对照与judge混杂，不能只采短46%数字。 | 潜在，日期未定；TRAIN-GRPO |
| [ELPO](https://arxiv.org/abs/2511.16122v1)，Nov20 07:27:26 | 全摘要给voting/shared generation/different search，并称更有效算法，但未说明足以超出组合的选择规则/成立条件。只需算法生成/搜索核心判断准入，不因复杂任务或7.6分自动收；也不因ensemble成熟就自动关。 | 贡献含糊，最小方法段普通待办，不是外部受阻；日期未定 |

日期原始证据均为各原页Submission history，上表保留原字段，不当public。月ID至多支持月份，schedule不补造09:00。有限原公开日期恢复未结束时仍为普通日期工作；若原公告/作者first-public找不到，隔离具名最小请求，不扩全实验/所有owner。暂无任何确定评分或Books写入请求，未自授7/8篇入选。

## 必要撤回负侧

[Mind the Motions](https://arxiv.org/abs/2511.15887) 当前页实际L8 `This paper has been withdrawn`，L21作者称发现问题要substantial revision；L29 v1 SubmittedNov19 21:26:28，L30 v2 May15,2026 11:11:13 UTC `(withdrawn)`。摘要虽仍可读，全部该稿采用链路关闭，不评分/不进入Books；不是因访问失败、日期或小benchmark关闭。只保留撤回依据，无需读旧全文来争取准入。root须独立核此安全/纠错反侧，不能将本次撤回写成2025窗内发生。

## 当前停点

root请先校准7潜在具体问题、ELPO最小补读边界与撤回关闭；日期不确定不授当窗，不因潜在方向进入本表而自动授Books增量。可并行继续其余来源有限筛选及日期原材料恢复。没有改共享Books/索引/合同，无stage/commit/push。

## ELPO最小补读后的精确更新

[v1方法原文定位](WEB_ELPO_METHOD_LOCATIONS.json) 实际§3.2–3.4算法读到：hard-case tracker保留跨prompt错误频次/失败prompt，Bayesian EI与K-means cluster-arm UCB作preselection，voting再组合。因此不以“ensemble成熟”关闭；潜在局部差额是跨prompt失败历史的选择和预算分配边界，而不是组合名称。

必要中心反侧：[实际Algorithm6及setup](WEB_ELPO_PROTOCOL_COUNTER.json) L222–229明确把 `D_test={(q_i,a_i)}` 作为输入，并在同 `D_test` 上最小化带F1的weight objective。A.1 L347–362虽列Train&Dev/Test划分，A.2 L364–365给Doubao-pro/GPT-4o、三次平均，但未在已读核心澄清Algorithm6的test命名究竟是validation误标还是实际评测标签参与拟合。不能据此宣称真实实现已经测试泄漏，更不能采用泛化/SOTA比较；原伪码本身已产生具体评价协议争议，root请核这一必要反侧。UCB算法L195全n=0而L199直接除n，未显示initial pulls/无穷分数处理；只说明伪码未闭合，不宣称代码一定崩溃。仅必要核心，不把当前日期未定项扩为全复现实验/附件队列。

ELPO由原“准入事实含糊普通补读”改为“机制潜在清楚、日期未定且中心protocol争议”，保留前判断及新证据；不靠降低评分/缩池回避。精确重开请求：同版本首公开日期；若要正面采用泛化收益，还需训练/验证/测试与weight fitting的隔离说明或对应真实实现。不存在此证据时只能隔离，不自动变Books成熟原则修补。
