# Jun03 MODEL B5：必要Source与actual-owner提案

仅补2026-06-02 BJT自然日；本作者范围01755/01695/01666/01635/01556/01509/01464/01451/01436。已重读AGENTS、当前研究/Report合同、Sources Daily/arXiv/恢复、Prompt、ROADMAP、2026 State本日块与最新路由。准入与联合日证复用[原B5](SUP_MODEL_B5_20261024.md)及[独核R22–29](SUP_NEXT_REVIEW_20261024.md)，不第三抄题摘/日期；B4与本日55既成层不重做。PROJECT_CONTEXT/LEARNING_PHILOSOPHY/WRITING_GUIDE已重新加载。只own本记录与必要原件，不写Report/State/Books/index，不stage/commit/push。

## 首段当前notice轻量核

2026-10-24实际打开官方[01755 abs](https://arxiv.org/abs/2606.01755)、[01695 abs](https://arxiv.org/abs/2606.01695)、[01666 abs](https://arxiv.org/abs/2606.01666)，读取title/AB/comments/history/正文入口。三页均唯一v1，所见页面无withdrawn/removed/erratum标记；01666 Comments为Accepted at ICML2026，不用会议标签证明机制。此核仅当前页面观察，不证明无任何纠错；余六notice尚未核，不以HTML能打开替代它。

## 01695 CANARY — 必要Source就绪 / 2+2+2=6

**日期：** 复用R22/R28已核Jun02联合区间：唯一v1 Jun01 05:01:01Z，精确DOI `10.48550/arxiv.2606.01695`在既存arxiv.content查询下findable、registered Jun02 04:21:44Z；submitted/registered均不单独改名公开。

[exact-v1](https://arxiv.org/html/2606.01695v1)，[本次HTML原件](SUP_MODEL_B5_SOURCE_2606.01695v1_20261024.html)。实际读§3–6，采用命题只限checkpoint差分检测：原先生成未显害不等无污染 → 可信base与candidate的同prompt末token同层hidden差，经base-trained SAE/过滤noise方向后取重构norm² → 增加whitebox候选审计信号，但不能给安全发布证书。D2为新的检测接口/条件，Reach2横跨checkpoint/探针/发布，Durability2是可复用验收分责；不按headline满分或SAE可解释加分。虽6分标准，安全相关解释与直接反侧已深入必要域，不遍历代码/附件。

§3/Eq2：`Δh=h_tuned−h_base`，`S=||Dec(mask(Enc(Δh)))||²`；SAE用base中层activation训练，mask按amplification下最负变化识别style/noise特征。10–30个domain-relevant unlabeled prompts，base/candidate各一次forward，加一次SAE训练和clean base→benign-tuned reference分布；不是“完全无需可信参考/准备或阈值”。具体K/训练集量/完整阈值与独立shift校准未由主文充分披露，不补成完整运行recipe。FVE .74–.88不是SAE语义faithfulness证书，norm异常也不独立认证harm。

主实验M1 Qwen2.5-.5B，M2 Llama3.2-1B、M3 SmolLM2-1.7B SFT，M4 Gemma2-2B RLHF作crossarchitecture；有害医疗文本仅此通用污染检测的测试人口，不采用医学知识/疗效，不扩AIforScience。rate1–20%，same-domain/同模型各rate相同hyperparameter，作者bootstrap1000，主claim1%AUROC1只在M1主实验，不是四架构统一1%。T1“output detected”定义为generation-LDA harm rate>5%，不是所有输出防御不可能检测。§5.2 per-prompt0.96与LogitKL0.96持平，与checkpoint detection/污染率的population不同，不合并分母。干净μ+2σ阈值本身不在任意分布保证FPR<2.5%，需近Gaussian/实际校准；零FP与AUROC不等全安全。

**直接反侧：** §5.6 M3在5%仅约.82，M4在10%才报告1；§5.7 rank4 LoRA evasion .815–.862，不能把它称self-defeating就消除未检测风险。§6 Gaussian且经验c/σ的detection-limit公式不是任何输出方法都不可达到的fundamental floor。可信base失效、合法能力/风格更新、domain shift与frontier规模尚未证明。hardware/precision/完整训练与采样预算、部署length/batch/concurrency/SLO未充分披露，不能把two-forward成本写零。SAE训练、双checkpoint驻留/求值、noise选择、参考校准与独立攻防回归计费。

**不采用链：** Eq3为`h_tuned+α·Δh_filtered`，T3却将α0的5×generation归因noise removal，按该显示式α0应无注入；独立mask到底作用于哪份state未闭。因此不采5×放大、手术70→10/no-perplexity-penalty或完整detect-to-fix保证，不把其未闭合妨碍本来可独立支持的检测接口；具体恢复条件是能对齐α0实际干预位置/执行映射的作者说明或对应实现，当前不依赖此支撑Books。未核代码或复现。

### actual-owner比较与最小PRE（尚未授写）

唯一owner `PLATFORM-SECURITY` / [Ch72](../../../../../books/part-06-ai-infrastructure/72-security.md)。实际读“从资产与信任边界开始”完整局部至artifact/内部mask/优化安全交接及Ch71/73开篇；全文定点找精确ID/标题无既存family。现有data-label与行为gate分责、内部mask定位/修复，但尚无可信base差分的无害输出之前检测信号及clean参考资格。Ch66拥有测量校准但不重复供应链安全机制，Ch35保存checkpoint不是判断安全。建议在benign微调两段完整结束后加一个自然段。

上锚完整直接段：
> [Benign fine-tuning 的作者实验](https://arxiv.org/html/2601.12460v1)只覆盖所测七个模型、270 QA 与受限生成/评价条件；knowledge/attitude 的线性 probe 是表示相关读出，不能证明拒绝机制的唯一内部因果，也不能把作者解释提升为必要充分条件。商业服务中有时需要两阶段更新且原因未明；50个 Alpaca 问题的局部效用评分更不能保证一般能力没有退化。因而更新仍需独立的安全与效用回归、必要的人审及发布回退，付出额外评价和版本管理成本；缺行为证据时保留原 artifact、限制更新或不发布，不能让训练数据的安全标签继承为部署许可。

拟融合段：
> 若可信base与待发布checkpoint都可白盒读取，还可先在同一无标签探针上比较同层末token hidden差，用base训练的稀疏字典过滤已识别的style/noise方向，再以差分重构量相对干净微调参考提出告警。这增加的是生成未显害时的候选审计信号，不是独立harm真值；“无标签”仍需可信base、字典/选层与clean参考。[CANARY的受限对照](https://arxiv.org/html/2606.01695v1#S5)里，跨架构高方差和低rank适配都会弱化检测，LogitKL也可达到相同逐prompt排序；未告警不等未污染，Gaussian近似阈值不授未知shift误报保证。双checkpoint求值/驻留、字典训练、noise选择与独立攻防/效用回归均计费；参考不可信、人口或质量失配时，隔离候选、保留已验artifact及输出/effect gate，不由异常分数或解释性特征签发部署安全。<!-- source-family:SF-2026-ARXIV-2606-01695 -->

下锚完整直接段：
> 数据和更新位置之外，优化规则也属于待验的安全身份：为维持可塑性或寻找较平损失区而加入的干预，不会自动继承原模型的抗后门性质。一个[受限DRL对照](https://arxiv.org/html/2605.14587v1#S5)在相同攻击框架中比较不同训练干预，发现SAM在已有policy被恶意post-training的设置下可同时降低所测sharpness、提高触发后目标动作成功率，部分组合又进一步放大攻击；从头训练的结果却弱得多。因此平坦、clean任务效用、触发行为和更新阶段须分别验，不能把“更稳定训练”当作去后门证明。这里攻击者仍须有污染transition/重发checkpoint的权限，有限PPO/小MLP和已知触发实验不推出任意LLM优化器的风险率；梯度方向图与有同向/曲率假设的局部近似，也不识别唯一普遍因果。不同任务sharpness量纲和其他成因尚未校准，低值或尖峰均不能直接变成自动检测阈值。额外优化求值、污染/对照训练、多seed、触发与良性回归全计费；变更optimizer或组合后应绑定新artifact重新验收，证据不足时保留可信未污染版本、数据/产物隔离和独立行为gate，而非只按loss几何批准发布。<!-- source-family:SF-2026-ARXIV-2605-14587 -->

## 01755 TriAlign — 必要Source就绪 / 2+1+2=5

[exact-v1](https://arxiv.org/html/2606.01755v1)，[HTML原件](SUP_MODEL_B5_SOURCE_2606.01755v1_20261024.html)。当前abs已核，联合日期沿R22–28：唯一v1 Jun01 06:19:52Z至精确DOI arxiv.content/findable registered Jun02 04:23:11Z，公告区间全Jun02 BJT，不重抓。实际读§3–6/Eq1–9/T1–3，必要AppendixA.1辨目标桥，不读全prompt/全persona表或代码。5分只给客观答案、风格与跨group交互反馈的训练接口；D2条件监督/反馈构造，Reach1局部后训练，Durability2可复用真值/偏好分责，不给MARL名义或普遍公平加分。

8个socialgroup-conditioned实例（同policy）最多4turn，state=(question,group,自己历史)，environment比较同题jointresponses后给各自反馈；offline轨迹含当前action后的future reward，不是多个独立模型训练后多数投票。部署仅单实例(question,group)，不带交互committee。Eq9 `truth+λpref·pref−λcons·|truth−组平均truth|`，标签必须先有独立truth资格；groundtruth来自LogicQA/SimpleQA/LIMO/StereoSet训练任务，模型prompt实现truth/pref/environment，GPT4o合成人设偏好rubric标签/评分。客观reference与stylejudge不是“universal truth”的新发现，一致错答也不能被认作truthful。

拟采用具体机制为先冻结跨group jointresponse/反馈/历史与客观reference，再用离线未来回报提出动作重加权，三项目标独立验收。**不采用完整NSW理论最优/权重配方保证：** Eq5权重`exp(A/β)(Q+ε)^(λ/β)`要求Q+ε>0（A1明列），ε小并不对任意负reward自动保证；Q较高本身还放大第二因子，不能仅凭名字断言专门提高worstgroup。主文A按跨groupσ归一化，A1式18却是未归一Q−V，原全轨迹NSW到逐action logQ也非已证明等价；不补造普遍fairness或收敛保证，不把本命题视完整实现核验。恢复该理论链须明确return正域、标准化与temperature，以及全trajectory到perstate目标映射。

Qwen3-4B-Instruct2507 fullFT3epochs、lr1e-5/batch16/accum4、2×A10080GB/ZeRO3，T.7采数/T0评估，2seeds均值。作者称trainingbased可比成本，但完整generation/teacher/personaaugment/judge调用与token预算未齐，不授等总预算；deployment长度/batch/concurrency/SLO未披露。T3移NSW或consistency均退支持有限bundle，不识别唯一原因。直接反侧T2 explicitMMLUPro fullMean.831但Std.045/Gap.074/CV.055，弱于多基线且相对baseStd.058改善不等各公平指标全面最优；T1 explicitAIME mean.467低于2Step.482、implicitStereoSetCV.029也弱于SFT.012，不采三目标全优/所有group公平。未复现，无当前已见撤回/勘误。

### actual-owner/PRE（尚未授写）

唯一owner `TRAIN-RLHF` / [Ch31](../../../../../books/part-04-training-system/31-rlhf.md)，已读pluralisticaggregation整局部和sharedsafety交接、Ch30/32开篇；全文定点精确ID/标题无既存family。已有历史groupreward加权、jury/skill分责，不含同题客观reference下多persona未来交互轨迹；Ch82不接管后训练reward，Ch66可消费分组测量但不复制训练机制。插在Federated平均与自适应聚合之间。

上锚完整直接段：
> Federated RLHF 用平均 group reward 聚合更新，在群体偏好近似同质且每组信号质量相当时简单有效；群体对齐程度、样本量和历史收益不同后，平均会让多数或高分群体持续主导，直接取最差群体又可能牺牲整体可用性并放大噪声。

拟融合段：
> 个性化还须区分客观题的参考答案与表达风格，而不能只把各persona的偏好reward平均。一个离线分支让同一policy的多个group条件实例回答同题，环境比较joint responses后反馈，再将每个action及其后续回报冻结为训练轨迹；客观正确、跨组差异和风格满意分别计分，部署仍由单个条件实例作答。[TriAlign的有限对照](https://arxiv.org/html/2606.01755v1#S4)支持这种数据/反馈接口，不让模型judge、群体共识或NSW名称认证真值与worst-group保证；部分显式偏好切片仍有准确率或公平指标反退。离线权重另须核return正域、标准化与目标映射，全部persona合成、交互、judge和训练计费；参照、群体代表性或回归不合时，保独立客观验证、显式style约束与原policy，不由平均满意度批准事实一致或普遍公平。<!-- source-family:SF-2026-ARXIV-2606-01755 -->

下锚完整直接段：
> 自适应 pluralistic aggregation 可以根据每个 group 的历史 alignment reward 调整 PPO 使用的群体 reward 权重。在这里的实现分支中，服务器生成回答并广播给群体；客户端用冻结的偏好预测器和本地 few-shot 数据产生逐回答 reward，服务器聚合这些 reward vectors，再更新中央 policy。这不是客户端参数更新的联邦平均。聚合 owner 必须保存 group identity、reward/evaluator revision、历史窗口、权重变化和 fairness/utility decision；客户端提供评价信号，不能自行改变全局公平目标。收益是把 worst-group 与 overall alignment 放入同一显式 trade-off，代价是 group 定义错误、历史漂移、权重振荡和隐私泄露；原始偏好数据不出本地，也不等于返回的 reward 已有差分隐私保证。

## 01666 DOT-MoE — 必要Source就绪 / 2+2+2=6

[exact-v1](https://arxiv.org/html/2606.01666v1)，[HTML原件](SUP_MODEL_B5_SOURCE_2606.01666v1_20261024.html)，当前abs已核；沿R22–28联合日证（v1 Jun01 04:19:16Z、精确DOI arxiv.content/findable registered Jun02 04:21:03Z）为Jun02。实际读§3–4，必要D/E/H/J及4.3.2，不扩attention附录/代码。D2联合优化expert分组与tokenrouting，Reach2训练离散surrogate/部署切片接口，Durability2容量/负载与真实成本分责；不借成熟Sinkhorn/STE全算法新颖加分。

DenseFFN dffn神经元分E组，每组s且sE=dffn；learnedaffinity经logdomainSinkhorn形成soft运输（row1/col s），greedy按soft entries递降在未分配且容量未满时做hard二值分组。**strictcapacity是neuron→expert结构容量，不是token runtime capacity/负载平衡保证**；在线token由另一linearroutersoftmax/topk选择。assignment与router forwardhard、backward各自softSTE，非hard目标真实无偏梯度。训练先dense intermediateactivation后乘R·Mᵀ mask模拟sparse，不等训练已省denseFFN；冻原dense权重，只训assignment/router，KLteacher+CE+zloss+loadbalance。收敛后抽取finalM，以gate/up对应行、down对应列物化expert；部署不再Sinkhorn/STE，不能由mask模型可跑直接称sparsebackend已核。

Llama2-7B/Llama3-8B/Qwen2.5-7B、8H100、Dolmino-mix；alignment3500steps(<3h Llama3)，随后1.2BtokenFT与7B变体分开。s128、E86/112/148等，主文“25%FFNsparsity”实际示例k22/28/37约为E的1/4，与术语通常“75%关闭”容易相反，采用时只写activefraction，不照抄sparsity口径。T2 dense与sparse质量仍差，Llama3 1.2BFT avg67.8 vs dense79.4、7B后71；Llama2 Hella53.9仍弱于PrunerZero54.7；不采无损或普遍90%retention。J同E8/top2、同1.2BFT对照仍有收益，说明不是仅finegranularity；但不证明全部优化单组件因果。H alignment开销较dense trainingstep约15%，主要CPUrounding/copy，Sinkhorn约2%；两阶段budget不能隐去。4.3.2 vLLMfusedMoE在相同activefraction下专家粒度throughput近稳，具体完整dtype/length/SLO未齐，不授任意topology/硬件或端到端省费。未核实现/复现，无当前已见撤回/勘误。

### actual-owner/PRE（尚未授写）

唯一owner `MODEL-MOE` / [Ch21](../../../../../books/part-02-model/21-moe.md)，实际读“组合兼容DenseExperts与同Checkpoint破对称”完整组、邻接统计模块objective段，Ch20/22开篇；全文精确ID/标题无同family。既有activation聚类/SVD初始化与EMAteacher未联合neuron分配/route；方法不是Ch49通用pruning，也不在Ch36写第二套模型语义。插在旧破对称两段完整之后，下一节部署模块objective之前。

上锚完整直接段：
> 它把初始化选择与校准分布、rank 和 teacher 目标绑定，增加聚类/矩阵分解、校准前向与后续蒸馏成本；破对称也可能先损伤 dense 基线。作者的 CLIP ViT、八 expert / Top-2 实验中，ensemble 蒸馏单独使用并非各指标都改善，组合消融不能证明低 router entropy 就代表正确语义或真实吞吐。输入远离校准域、近似造成退步或 teacher 成本不合算时，复制初始化后联合训练、普通 upcycling 或现有独立专家组合仍应保留；训练 owner 再验质量和负载，而不是由初始化几何替运行时作性能承诺。<!-- source-family:SF-2026-ARXIV-2604-13508 -->

拟融合段：
> 同一dense FFN也可以不先冻结神经元分组：用带均衡边际的运输松弛学习neuron→expert affinity，greedy抽出等大小hard groups，再让另一token→expert router与分组共同接受输出重构/蒸馏目标。这里的capacity只限制每expert的神经元数，不保证token负载；hard forward借soft backward的STE也不是无偏梯度。[DOT-MoE的受限转换](https://arxiv.org/html/2606.01666v1#S3)先在完整dense激活上mask训练，再按gate/up行与down列物化expert，训练mask省active数不等已省dense计算。运输/rounding、校准和继续FT均计费，原dense质量仍有缺口；部署是否受益另由fusedkernel、实际activefraction与请求预算验收。分组、surrogate或关键任务不合时，保固定分组、普通upcycling与原dense，不由严格结构容量批准运行负载均衡或无损提速。<!-- source-family:SF-2026-ARXIV-2606-01666 -->

下锚完整直接标题：
> ### 从统计 Expert 偏好到可部署模块，需要改变 Objective

## 2026-10-24后五项恢复（首篇即交）

已重读当前AGENTS/研究/Report合同、Daily/arXiv/恢复规则、Prompt/ROADMAP及2026本日State路由。前三01695/01755/01666沿root SAVE与R33唯一POST、OptCC沿R35，不第三审；01635由root独占，本作者不读。当前只01556/01509/01464/01451/01436。2026-10-24实际逐页打开五项官方无版本abs，均唯一v1，所见title/AB/comments/history无withdrawn/removed/erratum标记；01556/01509 comments为ICMLaccepted，01464为underreview，01451为submitted NGENAI，01436为25pages5figures，不以发表标签作贡献证明。日期/准入复用R22–28与B5表，不第三抓元数据；这些页面检查不授没有任何纠错的全网保证。

### 01509 ProbMoE — 必要Source与Ch21最小PRE / 2+1+2=5

[exact-v1](https://arxiv.org/html/2606.01509v1)，[原件](SUP_MODEL_B5_SOURCE_2606.01509v1_20261024.html)；实际读§3–7/Eq3–9/T1–2/§7.1消融，未核全证明/代码/复现。日期沿有效联合证据Jun02（v1 Jun01 00:16:36Z、同DOI arxiv.content/findable registered Jun02 04:17:12Z，全区间Jun02 BJT），不把登记叫实际公开。D2为有基数约束的subset分布与marginal-surrogate训练接口、Reach1单router组件、Durability2可复用forward/backward/部署分责；不为成熟DP或STE加分。

以sigmoid(r_i)独立Bernoulli乘积为底，条件于|S|=k后sample k-hot；softmax(r)另决定expert输出权重，并非把独立sigmoid当combineweights。DP求Z_k为O(Nk)工作，所谓logdepth只在perfectparallel前提。训练mask的forward是samplez，backward通过exactconditionalmarginal与softmaxweight走STE；精确的是该分布边际，不是非线性sampledloss的true/unbiasedgradient。Eq6明确求导时固定非选择(1−p)因子，不能对同一coupledsigmoid参数直接套字面偏导；Eq8全expert表达与实际sparseexpert执行的梯度实现未核，故不发布其全gradientrecipe或“训练成本与普通MoE相同”。部署Exactk用MAP（等k下为toplogits），训练sample与部署MAP同基数但非同分布。Dynamic-k先采k∈预设range再条件采S，部署range-MAP；不等globalcompute硬预算或任意token容量安全。

OLMoE1B7B(64experts/top8)与Qwen1.5MoEA2.7B(routed60/top4，shared4不改)，沿DenseMixer任务/数据/协议，GSM exactmatch、Law/Translation/Summary LLMjudge、MBPP/MMLUharness不同指标，不混一个accuracy。§7.1仅OLMoE/GSM的forward×backward四配置、3seeds支持组合收益；T1 QwenGSM53.29低于DenseMixer54.97/Conventional53.30，OLMoEMBPP22.8低于DenseMixer24.4，MMLU保留也非全优。T2 Dynamick用较少experts但GSM分别−1.82/−4.29；活跃数不代表壁时。主文所读域hardware/dtype/完整训练费、输入输出/服务batch/concurrency/SLO未齐，不补造净吞吐。DP/采样、router梯度、所有expert训练与全任务回归计费。

唯一owner `MODEL-MOE` / [Ch21](../../../../../books/part-02-model/21-moe.md)，已读route训练信号组与前后、Ch20/22开篇。全文定点搜五ID无既存family；当前budget随机Topk exposure段改变的是k预算且推理回固定k，不承载固定k subset概率/边际surrogate差额。建议在该组开头一般训练信号之后加入一自然段；不是把五Methods攒齐才交。

上锚完整直接段：
> 改变容量组织后，下一问是 router 如何学会使用它。基础 auxiliary loss 只限制负载集中；计算是否值得、expert 是否获得有效训练以及输出贡献多少，需要不同证据。先分清训练信号，再讨论从 batch 内统计、历史状态或外部记忆产生路由的分支。

拟融合段：
> 固定k也不必在训练时总选同一组最高logits：可以把独立Bernoulli选择条件化为恰含k个expert的subset分布，前向采样k-hot集合，反向以该条件分布的精确边际作为STE代理，同时保留combine权重的梯度。精确边际不等非线性任务loss的真实无偏梯度，基数相同也不使训练采样与部署MAP成为同分布。[ProbMoE的受限对照](https://arxiv.org/html/2606.01509v1#S4)支持将选择与估计器联合比较，仍有任务弱于普通路由；扩为range-k后，较少activeexperts也可损数学质量。DP、采样、router/expert更新与实际dispatch均计费，range另须满足runtime容量与负载合同；代理、质量或净费用不合时，保固定Top-k/原训练信号，不从路由更多样或expert数更少批准语义与吞吐。<!-- source-family:SF-2026-ARXIV-2606-01509 -->

下锚完整直接段：
> Router与expert也不是两份独立学习的几何：在固定当前选择、未跨Top-k边界的反传中，两者的输入侧梯度都包含当前hidden方向，但系数不同，实际optimizer并不保证它们同向或语义一致。一条[受限constructive分支](https://arxiv.org/html/2605.12476v1#S6)不训练router权重，改为对已分配token的hidden均值维护centroid EMA，以cosine加负载bias选expert；去掉trainable参数没有去掉路由状态。它在单配置中降低MaxVio，却损失perplexity，辅助loss对照还同时改变z-loss，不能归为全部均衡梯度必然破坏specialization。Centroid、bias、归一/空集合保护、刷新和全部训练均需独立验收计费；输入几何、质量或负载失配时，保留原learnedrouter、已核balance与固定Top-k，不由较低负载proxy批准吞吐或专家语义。<!-- source-family:SF-2026-ARXIV-2605-12476 -->

### 01556 TwinQuant — 已读必要域与精确停点（未owner/PRE通过）

[exact-v1](https://arxiv.org/html/2606.01556v1)，[原件](SUP_MODEL_B5_SOURCE_2606.01556v1_20261024.html)。当前absnotice复用本节已核，不重复GET；日期沿R22–28（v1Jun01 02:02:12Z、同DOI arxiv.content/findable registeredJun02 04:18:25Z，联合全Jun02 BJT）。实际读§4.1–4.3/Eq4–11、§5.1–5.7/T1–3、§6；未读AppendixA全理论/全kernelprofile/代码或复现。根节点新令本阶段释放槽，此处保存已读，不扩余三。

拟评分 **2+2+2=6**：D2双分量按postquantization而非real-valued SVDenergy联合重参数化，Reach2离线产物/双段kernel执行接口，Durability2组件数值与中间traffic约束。不是为所有manifold理论或通用“量化不等于快”加分，仍待reader按采用命题确认。

**已足识别的机制：** W=UV+R，activation全局orthogonalQ、lowrank内部invertibleG令U'=Q⁻¹UG、V'=G⁻¹V、R'=Q⁻¹R，原未量化乘积可保持，但分别量化X/U/V/R后误差不同；不把局部linearidentity授全网Norm/RoPE consumer等价。主文Q1/Q2保正交以便RMSNorm邻接吸收，G限rank内部坐标而不是任意跨norm变换。分stage训globalQ→冻结Q训G→jointrefine，calibrationoutputreconstruction直接优化分量量化友好性，不由SVD截断尾能量 alone决定。Theorem4.1基于noise独立、近似误差分解及flatteninggain，任意变换gain可≤1；不采用“任意Q/G必然降低量化误差”或未核proof/所印η逗号式作为精确保证。GL的polar/Cholesky参数化还须明确正域/数值保护，未核实现不补成完整稳定recipe。

**kernel必要接口：** lowrank先4bitGEMM形成INT32中间H，在chip内估scale/requantize/pack为4bit供第二段GEMM；同一量化X给lowrank与residual，register累积/共同epilogue后FP16输出，一次globalstore。省掉H全局写回/重载不等没有H中间舍入误差；U/V/R/scales/rank与repacking必须绑定consumer，不能只把“双路W4”当两个普通GEMM免费相加。

**评价与直接反侧：** Llama3 3/8B、Qwen3 4/8/14/32B；WikiText2 128×2048校准、group128/rank128，sixzeroshot/harness和WikiPPL。RTX4090 24GB+Xeon6430、L20 48GB+Xeon8457C；速度Llama3-8B input1024/output256、各batch，相对FP16 TensorRT-LLM约1.63–1.8×/1.32–1.73×只这些平台/条件，完整并发/SLO/所有runtimeversion未齐不补。质量表SVDQuant对照rank32而speed对照rank128，不拼成统一匹配预算优势。T1 W4A4Qwen14B avg72.8/PPL11.8弱于FlatQuant73.1/11.4；W4A8若干切片也弱于FlatQuant，FP16质量仍有gap。T2 rank128→256小幅改善却lowrankmemory/latency约翻倍；3.5–7.3%额外storage和3.8–8.2%latency是relative该分量口径，不是全部服务费用。三stagecalibration、双分量额外权重/scales、H重数量化与专用kernel付费；§6明确MoE/多模态/ultralongcontext待验证，不授跨平台/全模型nearFP16或生产ready。

**精确下一步：** 尚未比较Ch49实际“分布诊断/lowrank补偿/执行kernel”正文与前后交接，故不预判整合或已有覆盖，不给PRE。必要Source拟采用应只限“联合postquant误差目标与H onchip requant consumer”并保上述rank对照/反侧；无需遍历其余附件，除非actualowner差额要求具体公式。原件已保存有效，不重复GET。余01464/01451/01436只currentnotice+有效AB/date，尚未Methods/评分/owner。01635留root，不列本人待办。

## 阶段交接与普通停点

### 01556 root首次独立必要采用与owner差额（2026-10-24）

root独立打开同一exact-v1，实际读§4.1–4.3 Eq4–11、§5.1–5.7/T1–3、§6；与上述准备者两角色必要采用完成，非第三Source。确认两种坐标变换只保持量化前线性乘积，Q的正交吸收资格不同于rank内部G；INT32 H须onchip重估scale/requant/pack再给第二低bit GEMM，单epilogue不抹中间舍入。6分命题限postquant共同目标与双段执行接口；原noise独立近似/η显示问题不作为理论保证，rank32质量/rank128速度不合成同预算胜。Qwen14B/FlatQuant反侧与dense差距、group128/rank、4090/L20平台和全部准备/packing费保留，未核附录全证明、代码或复现。

root实际读Ch49 SVDQuant/Nunchaku完整组、rank选择两段、LoRaQ完整段与下方activation-channel补偿两段，Ch48/50职责沿既存上下文；精确01556/TwinQuant无现正文。LoRaQ已拥有分量量化/同账，但其lowrank activation仍FP16；尚无rank内部可逆坐标联学与INT32→packed lowbit中间consumer。仅补这具体差额，不重写成熟PTQ/低秩原理。唯一INFER-TENSORRT-LLM Ch49，建议LoRaQ完整段后/同格式activation channel补偿完整段前一自然段；既有前后完整段保留，后接仍是不用lowrank的替代分支。

拟融合单段（尚未独立PRE或授写）：
> 当低秩分支的中间激活也要降到低bit时，分解误差、分量量化误差和可执行数据流须一起选择，而不能只最小化实数SVD的残差能量。一条[双分量分支](https://arxiv.org/html/2606.01556v1#S4)保持全局坐标变换的正交资格，在低秩内部另学可逆坐标，以校准后的共同输出误差选择两分量；它们量化前代数等价，不保证量化后无损或任意非线性consumer都可吸收。第一段低bit GEMM产生的INT32中间值仍须在片上重估scale、重数量化并pack，才可被第二段消费，再与residual共同epilogue；省掉中间global traffic不等没有舍入或额外计算。校准优化、两分量/scales、packing和kernel适配全计费，部分任务仍弱于较简单PTQ，质量对照和速度对照也不能混用不同rank。没有匹配consumer、质量或完整请求净收益时，保留高精度低秩激活、固定分解与原量化执行，不由两路都叫4bit批准免费融合、无损或生产SLO。<!-- source-family:SF-2026-ARXIV-2606-01556 -->

下锚以“补偿分支也不一定要使用更高精度或低秩矩阵”开头的完整activation-channel段；上锚以“低秩修正自身也可以量化”开头的完整LoRaQ段，均已实际读。本人真H2注只记实际必要与独立采用/实际保存状态。下一仅需非writer对新单段与上述完整实际owner做一次PRE，Source两角色不重复；待实际保存后唯一POST，不预I/DAY。

首三01695/01755/01666据root通知已实际SAVE/R33唯一POST，既成层复用不第三审；OptCC亦R35且不归本作者。01635现root独占。当前01509必要Source/actualCh21/PRE已就绪交root，尚未Source/PRE通过；01556已读必要方法/评价/反侧与拟6分、原件及精确owner停点已保存，尚未actualowner/PRE。余01464/01451/01436仅当前notice与有效AB/date，无Methods/评分/owner完成声明。按root本轮有界要求现在释放槽给reader核01509和root01635，不扩余三Methods，不碰其他infra/四定义/日期。共享Report仍进行中，年度153/279不预增，无本作者Books新授权，不自签I或DAY。

## B5余三恢复：01464首篇必要包（2026-10-24）

本节覆盖上节行政停点中的过时待办：据root本轮直接通知，01509/01635/01556均已R37–42真实Source、actualowner、Books保存及唯一POST闭合；不第三审。当前只续01464/01451/01436，不读其他日期，旧notice/AB/date继续有效。已重读当前AGENTS、研究/Report合同、Sources使用说明/Daily/arXiv/恢复、Prompt、ROADMAP、本2026 State与精确停点；owner提案前重读PROJECT_CONTEXT/LEARNING_PHILOSOPHY/WRITING_GUIDE。无共享Books授写，不据本准备包预记整合、Source通过或DAY。

### 01464 Cross-lingual Self-Consistency — 必要Source与Ch33最小PRE / 2+1+2=5

[exact-v1](https://arxiv.org/html/2606.01464v1)，[已存HTML](SUP_MODEL_B5_SOURCE_2606.01464v1_20261024.html)，当前官方abs notice沿上节有效观察复用，不重复GET。准入与联合日证沿R22–28/B5表：唯一v1 `2026-05-31 21:48:26Z`，同DOI `10.48550/arxiv.2606.01464`、arxiv.content查询限定/findable与registered `2026-06-02T04:16:09Z`；适用公告规则所得最早界Jun02 00Z至登记最晚界整个落Jun02 BJT，不把submitted或registered改名实际公开时间。本轮实际读§3/Eq4–9、§4、§5/Table1、§6.1–6.4/Tables2–4及Limitations；不遍历附录、代码或复现实验。

**评分与采用范围。** Design2为将每语言答案经验分布对齐到单参考语言或跨语言混合目标、改变reward接口；Reach1限后训练reward/采样组件，不借翻译、GRPO或“多语言”标签升级跨系统；Durability2为语言能力不均时目标人口/等价性与独立正确性分责。总5，标准审阅已读足上述机制/对照/代价；因现有Ch33缺具体target-population差额，拟采用部分定点深入，不采用跨模型普遍有效或全部推理能力扩张。

**机制与身份。** 同一语义题生成L种语言的平行prompt，每语言采N份reasoning/answer；最终答案须先归一到共享canonical form（本文数值parser），才有跨语言相等可比性。每语言经验答案频率为p_l，单rollout reward是`log q(y)`而非gold correctness；默认q为各语言p_l等权平均，另对照本语言q=p_l及English参考。English分支用`max(p_en,0.01)`避免log0，floor后式子未重新归一，不发布其为通用精确概率recipe。混合池包括当前语言及其采样，非独立teacher。原英文题由同一模型self-translate获得平行题，省的是人工parallel标签/外部翻译器，不是无需平行输入、无需模型知识或无需验证题意保持；翻译错、canonical/parser错与多语言共同错误均可产生较高reward，不给真实过程或答案签字。

**设置、对照与关键反侧。** 1k GSM8K train英文题；Qwen2.5-Instruct1.5/7/14B为主，Llama3-8B另作相应对照。VeRL/GRPO、每步32平行题集/320语言prompt、每语言每题32rollouts、160steps、minibatch64、KL.001、lr1e-6、T.4、4×A100；高temperature有不稳定观察。正文训练称10语言，主MGSM表有英文加10译种，不能把表列数默改成训练精确人口。主MGSM250题，OOD为mGPQA/MMath/PolyMath；Qwen的S1/LIDR由作者用官方代码重训，表中其他Llama方法的已发表数字不作同模型同预算因果。Table1平均1.5B33.1→40.9、7B44.2→59.3、14B55.2→76.9，但1.5B英文52.4→50.3、7B斯瓦希里19.8→17.6，不能称每语言或强弱语言gap全改善。§6.3/Table4的7B English-target61.0高于combined59.6，故“多语言均权池一定优于强语言”被直接限定；Table4 combined59.6与主Table1的59.3不同，不静默合并成同一run或精确全局差额。§6.4人工平行题在MGSM另做25%train/75%eval，数据划分与主实验不同，只作该设定观察，不归因纯翻译质量。

S1生成更长、Maj@8接近Maj@32以及平均accuracy提高都不证明总计算更低；自翻译、L×N生成、解析/混合、全部训练与独立题意/正确性回归均计费。所读域precision、完整训练wallclock/总费、各对照严格同预算、服务输入输出长/batch/concurrency/SLO、训练seed不确定性未完整披露（部署SLO非本文机制主张），不补为净加速。Limitations限sub20B与有限多语基准，不外推更大模型、任意开放输出或非可验证任务；没有运行代码/复现。

### 01464 actual-owner/PRE（仅提案，尚未授写或独核通过）

唯一owner `TRAIN-GRPO` / [Ch33](../../../../../books/part-04-training-system/33-grpo.md)。实际读reward来源至无标签group/变体完整组与直接前后，Ch32/34开篇职责；精确01464/标题无既存family。Latent-GRPO已有同错/独立验收，CoVerRL已有多数伪标签同源验证，TTVS已有同答案改写与混合共识，所以不重写这些成熟警戒。尚无“平行语言canonical answer→p_l→q_target，English与全语言池化权衡”的具体学习接口；只增一段接在TTVS后，后接带安全标签的表示读出分支，不让Ch66接管reward、也不把selftranslation另建Ch27第二owner。

上锚完整直接段：
> 无标签训练还可以改变问题人口，而不只反复修订同一题的回答：先以当前多数答案作为改写条件，生成声称同答案的变体，再分别按每题共识与跨变体混合共识形成更新信号。原题的 agreement 比例可以筛选探测组，变体长度上限却不能验证语义等价，两个共识也可能共享原伪标签错误。[TTVS 的受限流程](https://arxiv.org/html/2604.08468v1)因此需要同时记录原题、答案 anchor、变体/过滤谱系及每种 group 的人口，不把“accuracy-driven”名称当真实正确性。探测、改写、顺序 original/variant/mixed rollout 与训练全计费，同一步32条和相近显存不证明同总计算；test-time adaptation 与未接触目标题的 held-out 能力也必须分验。改写失真、共错或费用失配时，保留原同 prompt GRPO、可信 gold/outcome 或无更新推理，不由更一致的变体认证推理规律已经内化。<!-- source-family:SF-2026-ARXIV-2604-08468 -->

拟融合单段：
> 变体也可来自同题的不同语言：先将各语言最终答案归一到共享形式，再由每语言rollout频率形成答案分布，以全语言均权混合或一个参考语言的分布给每条答案赋log频率reward。[受限跨语言对照](https://arxiv.org/html/2606.01464v1#S3)改变了目标人口，不增加独立真值；自翻译只省人工平行标签，不能验证题意保持，多个语言仍可能共同答错。强语言目标在一个7B对照中优于均权池，平均改善也伴随个别语言反退，故语言池、canonical/parser、采样数及policy身份须与reward一起保存。自翻译、各语言多次生成、解析与训练全计费，少量投票接近多量投票不等总成本更低；翻译、共错、弱语言或净质量失配时，保已验单语言目标、可信outcome或无更新推理，不由跨语言更一致批准正确性与普遍迁移。<!-- source-family:SF-2026-ARXIV-2606-01464 -->

下锚完整直接段：
> 无标签的组内表示一致性之外，有安全标签时还能显式训练另一份读出：取最后一个reasoning token的hidden state，经projection得到归一化表示，以safe、unsafe和rethink三个prototype作contrastive监督，再用安全标签及终局文本judge校准一个表示分数。随后把prototype几何reward、最终回答的文本reward与两路分数的一致性共同加入GRPO。这里改变的是学习信号与测量接口，不是读出了全部内部推理；prototype接近、head自报安全与最终回答通过judge仍是三种不同证据。<!-- source-family:SF-2026-ARXIV-2603-17305 -->

**本阶段停止/交接：** 01464单篇必要证据与具体最小owner/PRE包现已保存交root，仍待非作者实际必要Source/逐字PRE，不预I、Books写入或DAY。01451/01436仅已核currentnotice/完整题摘准入/联合日证，未Methods/评分/owner，是普通下一步非外部受阻；不为等其齐全延迟本篇交接。Report/State/index及Books均未由本作者改动，年度153/279不变，无stage/commit/push。

## B5最后两项恢复：01451首篇必要包（2026-10-24）

据root直接通知，01464已真实SAVE/R45 actualPOST闭合，不第三审。本轮已重读AGENTS、当前研究/Report合同、Sources使用/Daily/arXiv/恢复、Prompt、ROADMAP与本2026当前route；本文件旧行政停点由本节覆盖。只续01451/01436，不复制旧AB/date层；Books上下文三文与actualowner相邻已读。无Books新授、Report/State/index均不写；本日仍进行中，年度153/279不预增。

### 01451 Before and After Temperature — 必要原证就绪，中心测量争议 / 2+1+2=5

[exact-v1](https://arxiv.org/html/2606.01451v1)，[已存HTML](SUP_MODEL_B5_SOURCE_2606.01451v1_20261024.html)。notice沿本文件已核当前官方abs（唯一v1、所见无withdraw/erratum、submitted NGENAI）有效复用，不重复GET。准入/联合日证沿R22–28/B5表：v1 `Sun, 31 May 2026 21:13:47 UTC`、同DOI `10.48550/arxiv.2606.01451` 的arxiv.content查询限定/findable、registered `2026-06-02T04:15:51Z`，适用规则最早公告界Jun02 00Z至登记最晚界整个落Jun02 BJT；不把submitted/registered叫实际公开时间。未发现需要重开该日期层的证据。

实际读§3.1–3.5/Table1、§4.1–4.7/Eq1、§5.1–5.5/Table2/Fig1–4正文说明、§6–7；未检查图像像素、原始logits、代码或复现。评分针对原准入的具体测量增量，**Design2**为在同一步观测未加温与加温分布/截断头、检验该诊断的有效边界，**Reach1**限采样读出组件，**Durability2**为分布变换、条件prefix与被测行为的测量资格；总5，不因发现内部矛盾降分或缩池。原始核心采集/比较存在下述直接冲突，受影响域定点深入后保存争议，不把候选或Books临时标成已有覆盖来绕过。

**设置与可读机制。** 单Llama3.1-8B-Instruct、FP16、单L4 24GB/GCP；500英文开放prompt＝168 WritingPrompts/166 AUT/166 HellaSwag续写，每题各生成T=.3/.8/1.5一条、max_new_tokens300/default chat template。三条独立AR轨迹从首步后prefix分歧，不是同prefix的三个实际续写counterfactual。每步记录raw logits的topK，T=.3/.8用K100、T1.5用K200；采样token若不在头部就append，再对所保存支持归一，构造p=softmax(z)、q=softmax(z/T)。同一保存支持上的数学变换可精确计算，不因此成为完整词表的原p/q或实际sampler分布；追加已采token还使记录支持依赖所采结果，不能称无偏完整分布测量。

指标包括KL/JS/TV/Hellinger、top1/margin/chosen probability、达到累计α的最小n_α，以及q留在p的α前缀集合上的质量；逐response取mean/median/p10/p90/max等。正温度保持排名，top1 identity change全0确为退化项，T1 divergence全0也不测creativity。离散top-n_α集合通常会overshoot α，Eq1在T1应是该集合真实p质量（≥α），不是文字所称必恰等α。§4.5既称重归一头又说“captured topK head sums less than α”时censor，须交代是完整支持mass还是条件头mass，不能混同。前后分布可由一次模型forward logits计算，但捕获、搬运、存储、统计/聚合与两judge/人审仍收费，不采“零额外inference cost”作为端到端性能事实。

**核心直接冲突与采用隔离。** §3.3以T1.5的top200需保留≥.95 mass解释capture充分，但Table1却给149222个位置/131927次append，即88.41% actual sample在top200之外；T.8为0.09%、T.3为0。若该mass与actual sample真来自同一q及同一支持，需要原始采样/mass记录解释这一强烈失配，不能同时据此接受capture充分与实际sampler身份；这不是声称有限随机样本逻辑上绝不可能。完整sampler的top-p/top-k/processor与概率质量分母未在所读域明确，不能自行假设隐藏filter、把raw与post mass互换或删除这个反侧来补齐。§3.4/Limitations另称条件头q为actual sampled distribution、跨温度exact apples-to-apples，但K及prefix已变、头外高append率又未解释，所以精确全分布泄漏、跨温度诊断优势和无偏普适测量均不采用。该矛盾影响中心采集资格，不是网络/材料访问故障；原文已足识别，不无限追索可选附件。

**经验声明保留为作者报告，不作采用证据。** gpt4o/Gemini2.5pro对全500题三响应按coherence-first creativity排序，随机presentation；前三150题由三位共同作者盲temperature标签、固定A/B/C排序，第三人仅147题。两种panel不是客观独立真值，人均pairwise相关.771也不是不可超越ceiling；ensemble对human-majority相关.832不能推出judge unbiased、独立或某judge“更安全”。Table2 topfeature n90(p)p10与LLM/human相关.918/.870，正文说强信号主要来自T1.5失连贯；T.3/.8该feature均1.0，未区分两个连贯regime的细粒度创造性。多feature×聚合器按同数据rank选择、每温度每题仅一trace、变化的prefix/捕获支持，均阻止把这份排名解释为机制单独因果或heldout通用创造力检测。本文的有限负面边界可说明作者自己的headline并不等于coherent regime识别；在采集资格澄清前，不将精确相关/13pp leakage写进Books或正面报告。

### 01451 actual-owner判断 / 暂缓，无正面PRE提案

唯一可能owner `MODEL-SAMPLING` / [Ch20](../../../../../books/part-02-model/20-sampling.md)。实际读Temperature→Top-k完整局部、processor顺序、长程行为/校准误差组及直接前后；Ch19/21开篇职责已核。精确ID/题名无现family。当前正文已明确正温度只改相对概率不改排名、截断再归一、processor身份及prefix闭环；熵预算段还明确topN条件量不是完整分布同量尺、熵非连贯真值。故这些成熟原则不借本文再写一份；尚未成立的新层是其pre/post捕获特征对creativity的具体经验优势，不由主题相关或单模型高相关强行造diff。Ch66可消费判分/人口边界，但不复制sampler测量机制。

现有具体承载段（非本次新增，不以此掩盖争议）：
> Temperature 不改变 logits 排名，只改变相对概率。`tau -> 0` 的极限接近 greedy，但实现通常不会真的除以 0，而是使用专门 greedy path。

> 一次低概率选择会改变之后全部 logits。Sampling 因此不只是最终输出层的小装饰，而是在自回归闭环中持续改变状态轨迹。

> 不存在全任务通用的最佳参数。代码生成、创意写作、事实问答、结构化 JSON 和 Agent tool arguments 对随机性的容忍不同。

**拟处置为中心争议/Books暂缓，待独核，不是Source通过或终态DAY。** 单次定点重开条件：能够对齐同一步raw logits、完整raw/postnormalizer、捕获集合/append后的支持及实际sampler processors的原始记录或作者明确纠错，解释top200≥.95 mass与88.41%头外采样，并明确α宽度/censor的分母；若恢复经验优势，再需固定支持/条件或明确区分prefix效应，并在两个coherent regime/独立人口验证。不要求整库代码或先复现全实验；目前不采用其全概率/creativity/净性能正面保证，没有任何新书段可授写。请reader仅核这些必要争议与现owner，不重做AB/date/notice或01464。

**有界交接：** 01451单篇必要Source与actualowner争议包已保存即交root；01436尚只有效notice/AB/date，未Methods/评分/owner，属普通可继续项。为给同日reader释放槽，不等待01436齐备，也不预记本项I或NC。未动Books/Report/State/index，无stage/commit/push。

## 01436 root必要Source与实际owner提案（2026-10-24）

本节接替上节01436普通停点；01451独核R52已确认中心测量争议/5分、Books暂缓，不重做其Source。01436沿有效完整题摘与R22–28日证：唯一v1 `2026-05-31T20:15:12Z`，同DOI `10.48550/arxiv.2606.01436` 的arxiv.content/findable registered `2026-06-02T04:15:30Z`，适用公告规则最早Jun02 00Z至登记最晚界整个落Jun02 BJT；不称提交/登记为实际公开时刻。轻量notice沿此前官方abs已核的唯一v1、所见无撤回/勘误，未出现重开信号。

root实际打开[exact-v1 HTML](https://arxiv.org/html/2606.01436v1)，读§3.1–3.4/Eq1–5、§4.1–4.4/Table1–3、§5–6、A.1及B.1–B.3；已存[同版本原件](SUP_MODEL_B5_SOURCE_2606.01436v1_20261024.html)。不遍历无关附录、图像像素、代码或复现。**拟评分2+1+2=5**：新增的是经验全正确组内的质量排序/训练接口及其迁移失效边界，Reach限离线偏好/排名组件，不借“数据饱和”扩成全生命周期突破。

**机制与旧方案。** 饱和仅指当前模型同题8个样本全对，不是总体成功率必为1；二元correctness在这些样本内没有胜负差异，普通SFT仍有非零学习信号且实际改善。作者在同一正确样本池内用两种proxy排序：逐unordered pair比较、胜率聚合的自judge/强Qwen3-30B judge，或每token完整词表熵的平均再取倒数（有epsilon floor）；不是所选token的NLL、真实过程标签或校准正确率。DPO取最高/最低proxy构成chosen/rejected，全部同分则跳过、局部tie随机；另一σ-RRHF分支对按reward有序的response pair，以长度归一loglikelihood的hinge作rank loss、sigmoid(reward gap)加权，另有最高分response的未归一SFT anchor及lambda。改变proxy量尺会改变权重，不能把gap解释成校准效用；排序项需同题8份同一device batch，gradient accumulation不能替代这项组内相遇条件。GRPO接入只是§5未来工作，不宣称已实现新on-policy RL。

**评价与直接反侧。** Qwen3-1.7B-Base为主，chain sum目标池6–10 terms/digits，同池8份generation用于各法；strict池3–6且排除6/6，另一GSM8K为2302饱和train题。B.1明确held-out chain-sum 200题和GSM8K test1319题，每题8份、T.6/top-p.95/max2048、Math-Verify答案等价；该等价检查不验证每步推理。B.3为LoRA rank32/alpha64/dropout.05、AdamW、1/2/4epoch与LR/批大小/β或lambda sweep，按held-out validation pass@1选checkpoint；不是同等总预算保证，也不自行补造train/validation/test完整生成种子与去重实现。Table1 base pass@1 10.63→SFT19.38，而inverse-entropy σRRHF29.25，差18.62是百分点不是相对提升18.6%；strict对照22.35亦高于base但不证明任意easy→hard迁移。Table2 GSM8K self-judge σRRHF55.43低于base67.83，强judge DPO75.52、entropy DPO71.17；Table3 instruct起点84.32而entropy DPO82.13。质量proxy不是普遍更好、基础模型上的entropy优势不能迁移认证instruct。§4.3相对强judge的相关只说明对该judge的对齐，不是独立真值；不为采用质性反例抄成普遍性能优势。

题目筛选/8路生成、全部pair judge的平方比较或全词表熵、LoRA训练、超参/选点及独立回归全计费。同样generation pool不证明judge、训练、总token费用或净质量等价；所读域具体GPU、训练precision、所有seed/repeat与总wallclock为Not Disclosed，不补硬件/服务batch、concurrency或SLO保证（本文非服务吞吐主张）。只保局部机制与这些真实反退，不采“正确数据已经没用”或“熵即推理质量”的全称；可用gold/普通SFT在proxy失准或收益失配时仍合理。

**实际owner与最小差额。** 已读ROADMAP/Books三文、Ch34开篇至pair身份与Silent Forks完整组、后续data-quality/参考答案与统计偏差分支，以及Ch33/35开篇交接。唯一 `TRAIN-DPO`，不是把未来GRPO搬到Ch33。Ch34已有同outcome的行为规则pair（Silent Forks）和judge非真值，但没有“当前采样经验全对→同正确样本以judge/全词表entropy排序→base/instruct/任务反退”的具体数据资格分支；精确ID/题名无既有family。拟一自然段接Silent Forks完整正文及其source marker之后、OSCAR完整视觉描述段之前，原前后不改，不另建小节或全章新owner。

拟融合单段（尚未独核PRE/授写）：
> 同题多次采样全部答对时，二元正确性也可能失去组内排序信号，但这只是有限样本的经验饱和，不等总体成功率为1，更不等SFT已无梯度。另一条[受限离线分支](https://arxiv.org/html/2606.01436v1#S3)在这些正确回答中，用成对judge的胜率或整段平均token词表熵的倒数提出质量次序，再构造DPO pairs，或以加权排名loss加最高分回答的SFT anchor训练；后者须让同题候选在同一比较组内相遇。这增加的是质量proxy，不是真实过程标签；自judge在GSM8K可使结果低于原base，inverse-entropy在instruct起点也会反退，因此饱和判据、生成policy、排序器和独立目标评价须一并保存。筛选、多路生成、成对比较或全词表熵、训练与选点全计费，不能用同一候选池冒充同总预算。proxy或目标人口失配时，保留普通SFT、可信偏好与原checkpoint，不从“全对”认定数据无用，也不从低熵认证正确推理或通用easy-to-hard收益。<!-- source-family:SF-2026-ARXIV-2606-01436 -->

直接完整上锚为Ch34“若备选动作在当前oracle下确实有相同outcome”整段及其2610-24949 marker；直接完整下锚为“视觉描述的偏好也可由当前policy在句级树中生成”OSCAR整段及2605-00323 marker，二者已实际读。true-H2 Review notes仅补本项必要域、反侧和真实状态。下一请同日reader首次独立Source/实际owner/原单段PRE；准备好的单篇立即交接，不等待其他48项，未预I或DAY。
