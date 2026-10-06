# 2025-09-10 有界初筛

作者 Mendel；仅窗口 2025-09-09T09:00:00+08:00 ～ 2025-09-10T09:00:00+08:00。当前合同为唯一准入、评分与日期规则。

## 原始入口与停止点

- `ARXIV_THEMES.json` 保留四组实际查询：语言/Transformer/MoE，多模态/World Model/VLA/Diffusion，GPU/kernel/inference/distributed，RAG/Agent/reasoning/RL；日期措辞是检索线索，不作为公开字段。`SEARCH_EXTRA.json` 保留 kernel/compiler/world/VLA 补检及具体家族日期线索。没有命中不授召回保证。
- 正确官方月入口 `/list/cs.CL/2025-09?skip=0&show=2000` 实际 200，月标题升序总 2214；只浏览 `07000–08599`，依据本日检索得到 07324/08024/07627 的提交线索，得到 83 个标题，未把全 2214 变队列。原页 `ARXIV_CL_MONTH.html`，83 个原题名 `ARXIV_NEIGHBOR_TITLES.json`。
- 其中 13 个标题明确是传统语言识别、具体领域应用或暂缓科学应用，关闭于题名层；70 个相关/含糊题名及主题查询额外 18114/08024/07627，共 73 个精确 v1 完整题摘实际读取。`ABSTRACT_REQUESTS.json` 全部 200，逐篇 `<ID>v1-abs.html`，结构化原题摘/历史/Comments 为 `ABSTRACTS_PARSED.json`。这是题摘筛选，不是全文证据审阅。
- 月列表的 07309、07829、08022、08093、08105、08150、08304 等当前题名与 v1 不同；采用身份和完整题摘以 v1 为准，不用最新题名倒写历史贡献。
- 日期恢复：官方日路径 ISO 实际 400、紧凑实际 404；官方 announced-date-first 高级查询 09/09～09/10、large language model 实际 200 空结果。记录 `ARXIV_DATE_REQUESTS.json` 和原 HTML；它不证明零公开事件。`DATE_EXTRA_WEB.json` 对 CASTLE、Falcon3-Audio、LSP、Astra 的窄检未取得可授窗内 first-public 的原始发布字段。Astra Kavli 是 arXiv 查询转录，不是原稿发布方。SimpleQA 作者 X 403、官方 Kaggle 返回空动态正文，见 `NECESSARY_DATE_WEB.json`。未以搜索 Published、Submitted、月份编号或 DOI 注册授 first-public。

## 60 个普通日期潜力项：题摘与必要局部核心成立，日期保留

下表均为 [精确 v1 原题摘](ABSTRACTS_PARSED.json) 的具体增量，不评分、不计确定候选、不宣称实验成立。需要原始公告/作者正文发布记录或可验证冻结正文支持完全落窗区间后，才重开相应身份的准入、评分和所需证据；不因局部、负面、小模型或模块组合关闭。

| v1 身份 | 原约束 → 实际潜力 → 可改变的局部判断 |
| --- | --- |
| [07006](https://arxiv.org/abs/2509.07006v1) | 偏好不等于可配置政策 → 原则自动 reward、GRPO 与 policy-as-code → 政策训练与运行治理衔接，医疗案例不自动排除通用机制。 |
| [07017](https://arxiv.org/abs/2509.07017v1) | 神经符号推理的解释/伸缩冲突 → 谱模板、图算子、proof-guided 训练 → 学习表示与可解释推理替代设计。 |
| [07098](https://arxiv.org/abs/2509.07098v1) | GUI 长程/新 UI 失败 → 单次专家轨迹、verifier/backtracker → 示范约束与中断恢复；不把“避免错误”当保证。 |
| [07135](https://arxiv.org/abs/2509.07135v1) | 非英语考试评价只看准确率 → 重复一致性/顺序/可读性实测 → 局部 evaluator 与重复性边界，不采医学结论。 |
| [07139](https://arxiv.org/abs/2509.07139v1) | 多语 ASR 总指标掩盖方言 → 200+语言/口音分层与动态评价 → 语言覆盖与数据分布边界。 |
| [07149](https://arxiv.org/abs/2509.07149v1) | 活跃 circuit 不等于可靠 → Jacobian/sheaf inconsistency 与 Gaussian EI 的单次白盒评分 → 可检验的不确定性定义；原文明确 LLM 任务实证延期。 |
| [07163](https://arxiv.org/abs/2509.07163v1) | reranker 被初始 top-k 锁住 → 近邻图按 reranker 引导搜索、固定 100 文档预算 → 检索/重排预算分配。 |
| [07190](https://arxiv.org/abs/2509.07190v1) | 数值不确定性解释不透明 → uncertainty level 触发 Prolog 原则与解释 → 响应策略替代；等级来源/信任校准尚须核。 |
| [07253](https://arxiv.org/abs/2509.07253v1) | 单条件查询测不到复杂检索 → 多约束任务且最强模型 query rewrite 反而退化 → 重写收益不是普遍正值。 |
| [07282](https://arxiv.org/abs/2509.07282v1) | 组合泛化难观察 → bijective Gumbel-Sinkhorn head 与 early exit → 小 Transformer 的归纳偏置/层级解码解释。 |
| [07301](https://arxiv.org/abs/2509.07301v1) | 旧 key 固定只含旧上下文 → 随已见上下文更新旧 key 且保 AR、并行等价式 → 静态 KV 假设与训练/解码取舍。 |
| [07308](https://arxiv.org/abs/2509.07308v1) | cosine 不区分跨模态状态 → basis-vector metric，noun 分类收益但 adjective 对照不确定 → 表示/度量的成立边界。 |
| [07309](https://arxiv.org/abs/2509.07309v1) | 长生成质量点估计无区间 → 输入输出黑盒预测连续指标与预测区间 → instance-level evaluator 不确定性。 |
| [07311](https://arxiv.org/abs/2509.07311v1) | 答案式 SFT 数据选择依赖 prompt → 层内表示熟悉度挑数据 → 数据选择的内部信号替代。 |
| [07324](https://arxiv.org/abs/2509.07324v1) | Attention 深层局部化/熵塌陷 → 一步 belief propagation、多跳 GTD → 小模型 attention refinement，未外推尺度。 |
| [07370](https://arxiv.org/abs/2509.07370v1) | 人格表达与通用能力/安全互损 → persona adapter 与动态 MoE 路由 → 个性化后训练的能力保持条件。 |
| [07389](https://arxiv.org/abs/2509.07389v1) | 静态语言测试不测交互习得 → 人造语言反馈，100 响应仍未建对话 → 交互学习评价的负面边界。 |
| [07399](https://arxiv.org/abs/2509.07399v1) | 小 LM 不擅长 KG 遍历 → 外部轻量探索模块替代 LM 遍历 → 规划/检索职责分离。 |
| [07403](https://arxiv.org/abs/2509.07403v1) | 短 EI 测试不含长上下文噪声 → 约 8777-token 六任务与上下文内检索 → 长交互情绪评价盲区/组合收益条件。 |
| [07414](https://arxiv.org/abs/2509.07414v1) | 后训练依赖额外数据 → 竞争式语言自对弈 RL → 数据依赖与目标构造替代；不是不依赖已有 pretraining。 |
| [07450](https://arxiv.org/abs/2509.07450v1) | 跨视角模型单模态且无解释 → 多视角 satellite 对齐及 reasoning dataset → 多模态表示替代与解释正确性待核。 |
| [07475](https://arxiv.org/abs/2509.07475v1) | 幻觉验证分数未校准 → frozen NLI+meta-classifier、OOF 与 precision-constrained abstention → 验证/拒答阈值条件。 |
| [07506](https://arxiv.org/abs/2509.07506v1) | PyTorch 翻译队列不等于已有 CUDA 优化 → SGLang CUDA、生成/测试/profile 协作 → 正确性与 kernel 优化负载边界。 |
| [07526](https://arxiv.org/abs/2509.07526v1) | 默认复杂 audio connectors/curriculum 必要 → 公共数据单阶段与消融 → audio model 训练复杂度的局部反证。 |
| [07553](https://arxiv.org/abs/2509.07553v1) | OS agent 在不可信 GUI 过执行 → 训练 meta-knowledge 决定主动询人 → 执行/升级权限的可靠性条件。 |
| [07555](https://arxiv.org/abs/2509.07555v1) | 多跳 KE 跳过编辑事实 → edited-fact/case guided decomposition → 记忆颗粒度失配与检索修正。 |
| [07666](https://arxiv.org/abs/2509.07666v1) | 语义页面检索忽略逻辑关联 → page graph+小 VLM traversal → 多页 DocQA 的检索条件，不按组合关闭。 |
| [07730](https://arxiv.org/abs/2509.07730v1) | 多类 RE 漏语义、逐二类代价高 → grouping/extraction/decision → 训练样本发现的质量/计算取舍待核。 |
| [07755](https://arxiv.org/abs/2509.07755v1) | watermark 的检测/连贯指标漏 factuality → 低熵重权导致实体退化、人工验证 → watermark 的局部质量/可追溯取舍。 |
| [07768](https://arxiv.org/abs/2509.07768v1) | 认为大模型 ICL 足够 → 五语言十数据集，小模型 FT 常优于 ICL → adaptation 选择局部反证。 |
| [07817](https://arxiv.org/abs/2509.07817v1) | knowledge type 固定且意图/输出混杂 → provisional probe 选择知识类型、意图中间信号 → multimodal context 路由选择。 |
| [07820](https://arxiv.org/abs/2509.07820v1) | 思考预算固定 → critic 周期 certainty threshold 停止 → 预算/准确率与多 seed 可靠性边界。 |
| [07829](https://arxiv.org/abs/2509.07829v1) | 低资源文学翻译小模型能力不足 → synthetic data、两阶段 tuning/adapter compression 与成本评价 → 小模型/大模型局部替代边界待核。 |
| [07869](https://arxiv.org/abs/2509.07869v1) | prompt brittleness 被视作模型独有 → 同样说明变动的人/模型对照 → 标签到格式变化与 typo/order 的不同敏感性。 |
| [07908](https://arxiv.org/abs/2509.07908v1) | 创作评价掩盖人物属性差异 → 性别/文化条件下叙事属性反证 → generation fairness 的具体条件。 |
| [07925](https://arxiv.org/abs/2509.07925v1) | token uncertainty 忽略语义结构 → dependency graph/hierarchical pooling → 校准特征的替代，数字待实证核。 |
| [07966](https://arxiv.org/abs/2509.07966v1) | 表格视觉 reasoning 数据有限 → cross-model inspiration+jury 筛选 → synthetic dataset 的多样性与跨 benchmark 泛化待核。 |
| [07968](https://arxiv.org/abs/2509.07968v1) | SimpleQA label/topic/重复污染 → 1000 问清洗、source reconciliation/autorater 修改 → parametric factuality 测量边界。 |
| [07969](https://arxiv.org/abs/2509.07969v1) | RL 固定轮数压制长探索 → over-turn masking、冷启动轨迹 → 训练上限与推理可伸缩的代价归属。 |
| [07980](https://arxiv.org/abs/2509.07980v1) | 难题 RL 冷启动不形成 parallel thinking → easy SFT→hard RL、中期探索 scaffold → curriculum 与最终策略机制。 |
| [08000](https://arxiv.org/abs/2509.08000v1) | open weights 可被 fine-tune 抹除安全 → 激活条件 adversary LoRA 的双层优化 → tamper resistance 的权重攻击边界。 |
| [08010](https://arxiv.org/abs/2509.08010v1) | 单次 judge–advisor 与 agreement/switch 比率假设二元、可分贡献 → v1 §5.1–5.2指出迭代共写、部分语义采纳及主观任务不满足这些测量前提 → 轨迹/结果/信息源使用等评价单位的概念性盲区；非作者恢复潜力，不要求先有实验才能准入，不授安全效果。 |
| [08075](https://arxiv.org/abs/2509.08075v1) | persona 被单独归罪于 false refusal → 16 模型/任务/九 paraphrase 控制 → persona effect 的混杂纠正。 |
| [08093](https://arxiv.org/abs/2509.08093v1) | 语义类别只是模仿的假设 → iterated ICL color category、IB compression → 学习归纳偏置局部机制。 |
| [08105](https://arxiv.org/abs/2509.08105v1) | encoder+LLM LRL reasoning 落后 → bilingual→task curriculum 与 DoRA → model stacking 的训练条件。 |
| [08146](https://arxiv.org/abs/2509.08146v1) | bias 不转移到 adapted model 的假设 → prompt/few-shot 参数下持续 transfer → prompt debias 的有效性反证。 |
| [08150](https://arxiv.org/abs/2509.08150v1) | 整任务 one-shot 不可靠 → classical algorithm 中只调用 LM elementary oracle → 分解执行与局部错误传播。 |
| [08182](https://arxiv.org/abs/2509.08182v1) | XML syntax 不等于交互收敛 → lattice monotonicity/fixed point、contraction 假设 → 协议理论条件待验证，未授真实模型收敛。 |
| [08217](https://arxiv.org/abs/2509.08217v1) | 把标签差异当 spam → subjective annotation filtering 扭曲分布 → 数据可靠性/多样性的具体负面取舍。 |
| [08304](https://arxiv.org/abs/2509.08304v1) | 内容相似不等于覆盖 → QA answerability 的 inclusion/overlap，判别式优于生成式 → semantic coverage 评价选择。 |
| [08315](https://arxiv.org/abs/2509.08315v1) | uniform KV budget 忽略层/任务 → evolutionary downstream 多目标 layer allocation → 压缩/质量/搜索预算边界。 |
| [08358](https://arxiv.org/abs/2509.08358v1) | synthetic toxicity 可替人标的假设 → lexical diversity gap、训练下降 → 合成数据在敏感生成的局部失效。 |
| [08381](https://arxiv.org/abs/2509.08381v1) | 多任务 structured outputs 默认大模型/大量数据 → 1B+少样本 LoRA 实测 → 小模型训练投入的局部可行性。 |
| [08438](https://arxiv.org/abs/2509.08438v1) | synthetic speech 与固定 triplet order → 真人数据、多 order 与 latent relation prompts → cross-modal alignment 与数据真实度条件。 |
| [08480](https://arxiv.org/abs/2509.08480v1) | 从人类默认 agreement 推断 LM → 跨语言 no 偏向与语义同意脱钩 → 测试响应格式混杂。 |
| [08484](https://arxiv.org/abs/2509.08484v1) | persona 等于群体代表的假设 → 六 open 模型三条件，abstraction/stereotype 差异 → persona representativeness 的反证。 |
| [08486](https://arxiv.org/abs/2509.08486v1) | HHH 多目标与 MoE 路由不校准 → calibrated expert routing → alignment/latency/memory 取舍待核。 |
| [08494](https://arxiv.org/abs/2509.08494v1) | capability/RLHF 等于支持 human agency → 六维 benchmark 的不同开发者反向表现 → alignment evaluator 盲区。 |
| [08541](https://arxiv.org/abs/2509.08541v1) | English reference 自然高质且 multilingual pair 可靠 → 双层 consistency preference 选择 → DPO 数据噪声与跨语言目标。 |
| [18114](https://arxiv.org/abs/2509.18114v1) | decode shard skew 监测代价 → BlueField-3/DPU telemetry 与网络检测可行性研究 → 监测卸载与控制反馈；摘要是 study goals，不是已部署系统。 |

## 完整题摘后的 12 项关闭

- 07122：已有 NeSy 框架的技术刻画/比较，原题摘不提供新的 foundation-model 学习、执行边界或控制机制。
- 07142：LLM 作为 topic-model 指标工具，新增结论针对 topic taxonomy/semantic drift，不是 LLM 或主线检索系统的新机制/评价反证。
- 07177：能源 corpus+既有 Llama SFT，领域 QA 提升；没有新增训练机制或可比资源边界。
- 07471：六非洲语言的既有 back-translation/switch-out；传统 MT 应用指标，不是 foundation model/data 新有效性条件。
- 07512：为化学/材料等自然科学 entity recognition 选择 demonstration，按 ROADMAP 科学应用暂缓，不经 Data 回引。
- 07627：epitope/TCR 序列生成与 binding 指标，AI for Science 暂缓。
- 07889：共享任务的既有 LoRA、平衡数据、voting、多 temperature；只有应用排名，未新增校准/公平性失效证据或控制机制。
- 07909：position paper 倡议 inverse problems 寻 scaling laws，题摘无具体新 scaling 定律、可判定条件或实现证据；不按“理论”排除。
- 08024：LLM summary+caption+Transformer 用于气候 stance 分类，只有应用任务指标，没有基础模型形成或 multimodal system 新条件。
- 08025：COLIEE 任务的 BM25/BERT/embedding/LLM ensemble 排名，原题摘没有模块归因或重要失效边界。
- 08345：用 generative LM 原型评分作文 subtraits，仅领域评价相关性，不显示本项目模型/系统新评价盲区。
- 08463：非作者补读精确v1 §3–4、§5.1与结论/限制；attack target × edit granularity分类整合已有AFC攻击与通用标准化评价倡议，未建立新的攻击机制或某个具体评价前提为何失效的新增可判定条件。关闭这一实际贡献边界，不因survey标签或无实验一概排除，也不据此声称AFC安全。

## 撤回信号

08022 的 v1 完整题摘有 population-aware alignment 贡献潜力。精确v1原页只说后续版本撤回，版本历史v1为09/09 09:25:08UTC、无withdrawn标记；v2为09/16 03:06:45UTC，明确withdrawn。实际读 v2 `Comments`：作者要求部分必要修改后重投，v2无PDF。不把v2标记自动扩成v1官方撤回，也不把安全信号抹去。v1现为潜力日期/撤回影响未决：人口/地域对齐差异及轻量微调的增量尚需原first-public与撤回原因的影响范围，现不入选、不评分、不进Books。此处与上方60普通日期项合为61潜力，73=61保留+12关闭；原59/13/1及60/13分类保留于旧交接但不再作最新分母。原始记录 `WITHDRAWAL_08022v2.html` / `NECESSARY_DATE_WEB.json`保留，2026 v3不自动恢复2025 v1权限，不为此遍历无关版本正文。

## 13 个明确标题层关闭

07188（临床 discharge communication 应用）、07274（议会迁移辩论分析）、07459（Candy Speech 共享任务应用）、07462（临床 stigmatizing lexicons）、07588（biomedical representation 科学应用）、07622（clinical document summary）、07801（科学全文 entity/relation extraction）、07998（Omotic word-level language ID）、08032（scientific literature discovery）、08355（英语考试模板回答检测）、08596（BioASQ RAG 科学应用）、07170（civil legal intake ensemble 应用）、07202（EEG neurocognitive 应用）。没有虚构读取其完整题摘；本次无已见相关撤回/安全纠错信号。

## 官方事件负侧

SafetyKit 的官方 RSS 原值 `Tue, 09 Sep 2025 10:00:00 GMT` 对应本窗 09/09 18:00 BJT，题名/事件链接一致；核心全文 `SAFETYKIT_CORE.json` 已读。按 fraud/prohibited-content 分类选择 GPT-5/4.1、RFT、Deep Research/CUA，内部政策检索后生成 structured flags，是客户执行案例；95% accuracy、16B token/day 和视觉提高数字未披露 sample/evaluator/运行配置/预算/CI/消融。没有实际新执行协议、兼容性控制、可靠性成立条件或受控评价边界，关闭的是具体披露不足以建立新增贡献，而非“Agent 组合都关闭”。没有复现或人工核验客户数据。
