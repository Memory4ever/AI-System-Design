# Sep22 增量贡献筛选与有限日期门

作者Meitner；补窗仅2025-09-21完整BJT自然日。P只指贡献潜力，未确认当日首次公开，不计正式候选/Evidence/Books。C是贡献关闭，R是范围关闭。没有按关键词、数据集名、领域名或日期未知关闭潜力。

## 入口与实际读层

本日四主题Atom各33/44/31/4，112原条目去重91身份；实际查询与停止见SUP_ARXIV_FETCH.py及四份SUP_ARXIV_*_0.request.json/raw。每组start0/max100、返回total均小于100；未扩旧172库存/68月目录、catchup或整类队列。diffusion/agent宽词带来的非主线条目只做范围判断，不送全文。

91完整题摘实际读层见SUP_DISCOVERY.json，最终22范围外项使用当前Atom版本，不授精确v1；69相关P/C均具本日精确v1.abs原件，其中版本已变者的v1完整题摘实际恢复，不混用新版数字。最终59P/10C/22R；原54P/12C/25R暂筛的共因局部修正链保留于独核§10，非全量独立Evidence。

默认未读边界：仅完整题摘/必要准入core，不核全部实验、附录、代码、artifact或复现。下表标“core”者只授下一节具体读域；未标者不授正文审阅。每个身份原件命名SUP_<完整ID>v1.abs.raw/request.json；当前版本变动者另有SUP_<完整ID>.current.raw/request.json。

## 逐项判断

除最后01219外，身份均2509前缀；完整身份仍由SUP_DISCOVERY.json及原件可复查。

| 身份 | 判定 | 实际新增或具体关闭理由 | 实际正文读域 |
| --- | --- | --- | --- |
| 16736 Blockchain MAS | C | 信誉/负载softmax+EMA，执行成功由预设概率采样，未检验策略虚报或新真实性条件 | core |
| 16742 SMART | P | 不确定性调探索与step/outcome训练，迎合与轨迹优化的选择变化 | 无 |
| 16743 Outage | R | 领域停电预测PCA/Poisson/Seq2Seq/LSTM，非模型形成或AI基础设施 | 无 |
| 16749 Detection Rules | P | 精度之外相对现有feed的边际TP、retry成本和heuristic鲁棒性评价 | core |
| 16750 clinical KAN | C | KAN logits→softmax/CE、单层GAM式spline和logit/PDP解释应用，无新增学习条件；撤临床标签R | core |
| 16765 Speech pathology | P | 男女差异、窄类界/大label-space下CoT退步，具体模型评价反侧 | 无 |
| 16767 DiffEye | R | 人眼注视/临床路径生成任务，未建立基础模型机制增量 | 无 |
| 16780 RAG/GraphRAG | P | 实体检索过量无关上下文及扩大rerank窗口的退化/幻觉 | 无 |
| 16788 Arabic ABSA | P | highest-loss样本中标签noise、early-positive/late-negative与转折/aspect混淆改变错误归因；撤C | PDF局部 |
| 16804 KuBERT | C | Kurdish BERT语料/情感适配，未给改变训练选择的具体机制条件 | 无 |
| 16805 MCQA bias | P | 难度相关选项token/位置偏置与confidence-adaptive logit校正 | 无 |
| 16810 nursing assessment | R | 人类护理学生临床评估，非模型形成机制 | 无 |
| 16811 Agentic video editing | P | fine/coarse索引refinement局部消融暴露细节与时间保持依赖 | core |
| 16813 CLIFS | R | 测量人类心理功能的指标，不是模型bias或系统可靠性条件 | 无 |
| 16820 DISCO | P | query/value steering分解与干预作用位置 | 无 |
| 16830 FDP | P | 各模态条件factorization使扰动下可选择优先条件 | 无 |
| 16835 topic brainstorming | R | SBERT/UMAP/HDBSCAN主题归纳应用，非当前模型机制研究 | 无 |
| 16839 Roundtable | P | 历史player/subtask/rubric可靠性表；结构题与开放proposal grader一致性反差 | core |
| 16842 DoubleGen | P | 生成目标的双重稳健性及辅助模型正确性条件 | 无 |
| 16857 ShadowServe | P | SmartNIC数据面、KV/chunk流水与loaded latency资源取舍 | 无 |
| 16858 social game robot | R | 社会机器人offline RL应用，非VLA/基础模型行动机制 | 无 |
| 16859 consciousness | R | 现象意识哲学准则，非能力形成/可核验系统机制 | 无 |
| 16861 AdaptiveGuard | P | OOD runtime检测、持续适应与旧分布保留条件 | 无 |
| 16865 direct CO solver | P | format/feasibility/optimality reward与BoN采样预算下可行性/最优性取舍；撤销首批C | core |
| 16866 seqBench | P | 逻辑深度/回退/噪声分离评价LLM顺序推理失败 | 无 |
| 16869 PhysHDR | R | HDR低层图像恢复领域模型，非生成基础模型机制 | 无 |
| 16871 HOGraspFlow | P | RGB/HOI/taxonomy条件的SE3 flow grasp，接触输入缺失及FM/diffusion局部比较 | 无 |
| 16882 DES-MoE | P | router蒸馏、expert-domain梯度隔离与渐进冻结 | 无 |
| 16889 TableR1 | P | warmup低初始化、TEDS感知与hint-conditioned训练；感知提升不自动推理提升 | core |
| 16891 LaySPA | C | 已知format/几何/GT IoU三加权奖励用于layout，基础模型比较未给新增有效性条件 | core |
| 16895 DyTA4Rec | P | 每n轮short-term更新、pattern有无自适应权重相对static BC/RRF的局部条件；撤C | core |
| 16897 PRISM | P | data-free蒸馏生成分布的precision/coverage双约束与mode-collapse机制 | 无 |
| 16900 survival ME-Mamba | R | 医学生存预测，AI for Science暂缓 | 无 |
| 16903 HiDAC | P | 分层LoRA目标隔离；instance负例训练停滞vslabel-centered稳定目标，few-shot增多退步 | core |
| 16912 OBI simulation | R | 金融人工市场agent执行算法，非模型Agent系统 | 无 |
| 16914 CUTE | P | 同四语言parallel/nonparallel语料比较改变跨语转移数据组织选择 | core |
| 16920 SwarmChat | C | 四模块命令编排与满意度，无新增执行一致性或可靠性条件 | 无 |
| 16924 audio-visual navigation | P | stereo差异意识与audio-guided dynamic fusion | 无 |
| 16929 KDeCore | P | 固定可调参数下task-agnostic/task-specific解耦和双memory | 无 |
| 16935 clinical PEFT | R | 临床预测适配，AI for Science暂缓 | 无 |
| 16944 SD-RPN | P | 从middle attention自蒸馏RoI作单pass RPN，避免重复prefill/AR等待 | 无 |
| 16952 AirQA | P | scoring-point主客观评估分权、滑窗和错误动作移除的不同作用 | core |
| 16955 quantum finance | R | 金融预测量子self-attention领域研究，非LLM形成/基础设施 | 无 |
| 16956 VidCLearn | P | 当前noise输出distillation与temporal loss，权重增加的语义/时间质量反向取舍 | core |
| 16957 remote RCNN | R | 遥感object detection领域应用，无基础模型机制关系 | 无 |
| 16963 tactile planner | R | 传统触觉反应规划，未建立VLA/模型环境预测机制 | 无 |
| 16965 TVKD | P | teacher value potential shaping与DPO原最优策略保持条件 | 无 |
| 16968 boundary activation | P | RandomCrop对象不完整的生成失效与早期边界惩罚 | 无 |
| 16972 SaSaSa2VA | P | 单SEG/稀帧瓶颈的多目标/采样增强局部机制 | 无 |
| 16973 fMRI bias | R | 脑成像人类认知分析，AI for Science暂缓 | 无 |
| 16986 VCE | P | AR image视觉对比DPO分离概念擦除/保留语义，非新版扩推 | 无 |
| 16989 PTQTP | P | 2个ternary plane分解避免mixed-precision补偿；不借新版速度 | 无 |
| 16990 speech GRPO | C | BLEU reward的GRPO语音应用与off-policy探索方向，无新增优化/有效性条件 | 无 |
| 16995 MoA-Off | P | 模态复杂度与运行状态共同决定offload时延/资源取舍 | 无 |
| 17000 adaptive overclocking | P | uncertainty/complexity动态控制reasoning alpha与实时预算 | 无 |
| 17024 weather restoration | R | 低层坏天气图像恢复，非基础生成模型机制 | 无 |
| 17030 transfer neurons | P | MLP神经元干预定位多语latent转移与推理 | 无 |
| 17037 KAHAN | P | teacher质量/事实性取舍，复杂实体下hierarchy insight/readability反向边界 | core |
| 17040 MIR | P | interleaved多图/文字配对关系的评价盲区与阶段课程 | 无 |
| 17042 OGR | P | 共享阶段目标修正分别生成reward/curriculum错配，非仅反思流程 | core |
| 17044 AgriDoctor | R | 作物诊断助手与数据，AI for Science暂缓 | 无 |
| 17047 reading MI | R | LLM辅助解释人类阅读实验，非模型形成机制 | 无 |
| 17050 GeoProto | P | 可微Nyström供新样本/learnable prototype用流形几何，周期landmark保持backbone演进同步；撤R | 无 |
| 17054 TactfulToM | P | white-lie信息不对称评价与LLM低于人的局部反侧 | 无 |
| 17057 RoboManipBaselines | C | v1统一采集/训练/评价接口，未给新机制/条件；当前limitations仅限定framework权限 | v3局部说明 |
| 17063 TSGym | P | 拆tokenization/channel/attention/Foundation Model组件归因与分布转移设计选择 | 无 |
| 17065 CardiacCLIP | R | LVEF诊断few-shot适配，AI for Science暂缓 | 无 |
| 17066 RALLM-POI | P | TF-IDF+recency DWDTW、rho敏感/冷用户异向，空间context条件；rho解释方向矛盾保留；撤C | core |
| 17068 IHiD | R | 轨迹异常检测重构，不是action-conditioned环境模型或VLA | 无 |
| 17072 SnipSnap | P | 稀疏compression format/dataflow共同搜索，而非固定格式数据流搜索 | 无 |
| 17074 affordance | P | affordance/object两层信息约束对齐foundation image/text表示 | 无 |
| 17080 CoPlanner | P | 已验证短pivot共享与长期contingency分支，修正只选单轨迹的回退盲区 | 无 |
| 17084 MoCLIP-Lite | C | frozen concat+MLP单UCF融合应用，无新增机制/同条件取舍；预计算CLIP成本不在online throughput | core |
| 17088 AlignedGen | P | DiT共享attention的位置冲突及非重叠ShiftPE索引 | 无 |
| 17096 Prompt-with-Me | C | classify/refine/mask/template及usability，未给执行可靠性/生命周期一致性新机制 | 无 |
| 17105 GRPOformer | P | 旧轨迹reference states的oldpolicy KL约束跨update漂移，非固定ref KL；撤销暂C | core |
| 17116 MCTS-EP | P | search-derived preference及strong-convex条件界，不授证明或普遍效果 | 无 |
| 17120 Stencil | P | 小模型subject适配/大冻结模型context guidance分责保留prior | 无 |
| 17131 delayed control | R | 传统非线性控制近似predictor稳定性，非foundation/world/VLA研究 | 无 |
| 17136 SAEC | P | budget复杂度阈值+confidence接受门的edge/cloud路由取舍 | core |
| 20380 ACCeLLiuM | P | string-match≠clause equivalence、MCUcompile≠runtime semantics、loop-only缺residency上文 | core |
| 20381 USB-Rec | C | PO数据构造+inference自增强的推荐应用，无具体新优化/可靠性条件 | 无 |
| 20384 R1-Fuzz | P | coverage slicing问题与distance reward耦合引导深程序探索/小模型成本 | 无 |
| 21358 fundoscopic fusion | R | 视网膜诊断MLLM融合，AI for Science暂缓 | 无 |
| 21359 influence RAG | P | context移除影响值纳入query/list/generator及代理选择，非只新reranker | 无 |
| 21360 MPDA | P | 多模态拆分使单文本filter遗漏跨模态unsafe组合，具体安全评价盲区 | 无 |
| 21361 MECW | P | advertised context与问题类型相关有效window分离，具体失败评价 | 无 |
| 22697 hyperspectral | P | hard/semi-hard negatives、fixed LEM semantic anchor/mono-vs-multilingual局部比较改变对齐选择；撤R | core |
| 22698 MASTAVN | P | joint observation与顺序跨agent temporal representation的通信/fusion机制 | core |
| 22699 uncertainty moderation | P | 高F1仍低confidence的群体偏置，conformal uncertainty评价反侧 | 无 |
| 2510.01219 concept bias | P | ICL concept-learning暴露direct-prompt不明显的quantifier bias | 无 |

## 必要core实际读到哪里

22份本日精确v1 HTML200，另16788 HTML404触发精确v1 PDF fallback。原件SUP_2509.<ID>v1.core.raw/request.json及SUP_2509.16788v1.pdf-full.raw/request.json；23个必要v1读域均不称全篇Evidence。两次部分PDF保留，不计已读完整PDF；第三200/exit0/4,171,462 bytes可完整解析35页，只读pp23–24必要域。

| 身份 | 实际section | 采用/反侧与未读边界 |
| --- | --- | --- |
| 16736 | III-C、IV-A/B/C/D、V-B、VI-C | softmax/EMA与模拟成功概率不证明truthful策略；独核实际全域，作者V-B部分输出有截断，不授作者全域逐字读；C依据III-C/IV-A–C/VI-C足够。未核代码 |
| 16749 | §4.1–4.3、5.1–5.2、6开头 | uniqueTP相对feed，不是真recall；鲁棒性heuristic、一次成本×retry；holdout人类规则对照仍任务不对称。未读全部case |
| 16839 | §2.1–2.4、3.3 | 历史表非LLM参数更新；structured/openended grader相关不同，不授confidence已校准/aggregation更正确。科学方案收益不采用；未核附录 |
| 16865 | §4.3/4.4、5.4、5.5局部 | GRPO奖励+BoN仍须检查器；feasibility增加伴optimality池变化。作者5.5尾截断，Cicero已核该域；不授全部feasible或NP-hard最优 |
| 16889 | §4.2、HC-GRPO定义、5.6、Limitations | HC是hint下binary answer+format非step-validity reward；PA感知↑不自动reasoning↑，组数/分割非预算匹配。未核全部table任务 |
| 16956 | §3、4.3 | teacher当前noise输出distill而非实际旧video replay；lambda/alpha变化有混杂，权重的语义/时间取舍局部。未核附录/复现 |
| 17105 | §2.3、setup；独核另§2.2/3.1/3.3 | historical-state policy KL不是fixed-ref，仅局部HPO稳定性潜力；作者未自行声称3.3已读，独核读层已具。无新KL理论或LLM通用保证 |
| 16811 | §3.2.4、4.3 | refinement细节/temporal依赖局部；answerer 2.0/2.5叙述不一致，数字不采用。未核其余human研究 |
| 16891 | §2.3、4.1 | format/几何/GT IoU三奖励与基础模型比较，无新成立条件；C，不是因layout字段名 |
| 16952 | §2.2、4.3 | 19函数可含主观LLM，logical组合含主观即主观；error-removal有效动作收益≠总分收益。未核全部函数/科学内容 |
| 17084 | II-C、III-C | concat frozenbackbones/MLP，offline CLIP成本排除；未证明新质量/资源边界，C。未运行/全评估 |
| 20380 | §4.3、5.4 | clause/set与MCU分母/compile分层；缺上文residency可导致正确directive但错数据移动。未核编译或全部error实例 |
| 22698 | §3.2、4.3 | 顺序agent状态/fusion局部新机制；非collaborative baseline未控制全部capacity，不授scale或安全 |
| 17042 | III-E、IV-C、IV-D1 | centralized stage目标修reward/curriculum错配；未核全部CARLA/真实车实验，不授安全/泛化 |
| 17037 | §6.1/6.2 | 不同teacher事实性tradeoff、market实体复杂度改变hierarchy收益；未核全部统计/benchmark，非金融指标本身准入 |
| 16914 | §3.5、4.4 | parallel/nonparallel同语言数据组织比较的局部P；未核全部跨语评估/翻译质量 |
| 17136 | §2.3、3.3 | 温标校准与budget百分位/置信门，max并行路径成本模型有条件；不授阈值保证可靠或全端到端成本 |
| 16903 | §3.2.3/3.2.4、6.1–6.3 | lower contrastive/upperCE隔离；负例停滞、固定label目标及more-few-shot退步局部P，不授诊断因果。未核全训练表 |
| 16895 | §2.1–2.3、3.3 | 固定long-term、short-term每n轮更新；sequence/cluster存在决定权重。未授真实用户模拟/无self-feedback漂移 |
| 17066 | §2.1–2.3、3.2 | Haversine+DWDTW与rho/稀疏用户条件；rho越大实际旧点相对权重增，与更recent解释相反。未授ALR自动合规 |
| 22697 | §2、4最小negatives/anchor/LEM对照 | train end-to-end视觉encoder与AB 0.07%参数口径待核；UMAP/flatness不证明泛化。未读其余图/证明 |
| 16750 | §4.2全定义 | KANsoftmax与单层additive spline/解释工具实际C，非clinical域R；没有新增学习理论，未读临床全部实验 |
| 16788 | PDF §6.8/6.8.1/6.8.2、§7 pp23–24 | 50 highest-loss样本/IG仅局部归因；标签noise与early-positive/转折/aspect/subword反侧P，不授位置因果或IG因果。未读全部表/全文，Arabic表未目视核 |

当前17057v3官方comments明确新增Limitations，own精确v3 HTML的VIII已实际读：Linux/机器人覆盖限制、高seed variance/少real trials、未做mixed sim/real、humanoid固定腿不支持whole-body。该后续修订不倒填v1或补窗；未形成本次新增候选，不从“added limitations”自动推出实质新机制。原v1仅五句framework摘要C保持，后续新具体设计/纠错可定点重开。

## 当前说明与公开日期门

SUP_CURRENT_LIGHT.json保存69相关官方事件页的title/comments/dateline/submission-history/withdrawn及可见说明；27已变版本用当前abs请求，42当前仍v1复用own精确页。当前comments/可见说明实际逐项轻读，未见官方撤回/勘误/纠错公告；17057新增limitations已另核，会议accepted、版本变化或摘要安全术语不自行算重要修订。未遍历全部版本史或站外纠错，不把regex返回notice等同官方纠错。

69请求身份全有200 abs原件；当前page history只记录submitted/revised而非public。所有拟P的首次公开日仍未由这些字段确认。12分类精确日列表均400 Invalid time period；advanced首请求上下界同日不合法，窄修至09-22后无结果且页面明示announcement只支持year/month；无结果不能证明Sep21零公开。SUP_WEB_DATE_DISCOVERY.json仅有限官方搜索/身份恢复，不代公开日。已完成这些有限官方入口后59P精确隔离，不为日期未知追加所有方法/代码/作者全站，也不补造小时。

恢复条件：目标ID的官方当批公告/列表，或作者原始正文首次公开日/完整落窗区间；取得后只核该身份日期及必要Evidence/owner，不重跑所有目录。59P未评分、未记本窗候选、未采用Books，不是59项Evidence通过。10C/22R日期未核实但不影响当前关闭，不另建日期请求。

首批16736/16865暂C历史原件SUP_FIRST_20261012.md保留不改；独核后16736必要core确认C，16865撤C为P。17105/16903/KAHAN/OGR等曾有仅成熟组合的暂判已由实际具体机制/反侧局部更正；未把日期hold或深读费用当降池理由。最终独核与行政差额仍待Cicero实际DAY/FINAL。
