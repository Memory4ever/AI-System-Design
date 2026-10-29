# 2026-05-28 补遗漏：唯一作者记录

## A1. 范围、基线与采用标准

仅补 2026-05-27 北京时间自然日，保留原报告小时窗、118 个完整旧候选行（含日期/评分）与连续旧 §4；不重建旧池，不迁移旧归属。实际补前副本为 `BASELINE_BEFORE_SUP_20261021.md`：190504 UTF-8 bytes，SHA256 `bf481b4f9f311ed94448c1908d658daa6e33d5bed2a60a83e289a1ec5c3137b1`；连续旧 §4（两个二级标题之间）135698 bytes。旧 835/118 统计只属于旧小时窗及既有审阅，不是本次自然日全量。

已完整重读当前 AGENTS、研究/Report 合同、来源每日14源与全部主题边界、Prompt、ROADMAP；LEARNING_STATE 仅最新2026路由。采用当前合同的公开日联合界，不采用旧 receipt 的 created 单字段代理。唯一作者 `/root/supp_may28_author`；独立 reader `/root/supp_may28_reader` 的实际复核记于 `SUP_REVIEW_20261021.md`。不改共享 Books/LS/index；无 stage/commit/push。

## A2. 首批全部拟准入与分层排除（待 reader 实际校准）

1. [MiniMax Agent Team: Built for Long-Running Tasks and Continuous Evolution](https://www.minimax.io/blog/minimax-agent-team-long-running-1779893953)，官方 May27；长任务由模型自判完成的模糊边界 → Team Engine 明示 producing / verifying / done、验证失败唤醒生产者与运行中补充提示 → 交付门由外部状态机承担而非 Worker 自报；2+2+2=6，标准审阅，具体已有覆盖 `AGENT-WORKFLOW`（Ch81 State Machine，Ch82 Supervisor/Worker 和 Ch84 run/context/terminal 分责交接）。角色分工本身不是新增贡献。全文读取 §3、§3.1–3.4、§4 hard problems、§6；保留通信/整合/上下文成本、验证循环上限与人审边界；没有对照实验证明可靠性/ROI，未来开源不是已核 artifact。原件 `SUP_minimax_team_20261021.html`。
2. [Private analytics via zero-trust aggregation](https://research.google/blog/private-analytics-via-zero-trust-aggregation/)，官方 May27博客披露事件（不是 Willow 首次论文）；多轮在线/TEE保密单点 → 一次贡献提交、委员会解密协助及DP噪声、attestation执行身份 → 遥测数据面在明文访问和执行证明间重新分责；2+2+2=6，安全边界触发必要深入，具体已有覆盖 `PLATFORM-MONITORING` Ch67 §“隐私约束会改变可观测性的数据平面”。必要证据：正文 The challenge、A tale of two protections、Encryption meets isolation、The cryptographic engine with one-shot efficiency、Private analytics for SafetyCore。客户端委员会仍有额外参与，one-shot不是全协议无交互；TEE侧信道/密码假设、未披露DP参数和性能数字，SafetyCore将采用不是效果已证。官方 HTML curl恢复失败，web工具实际完整读回；当前采用命题不依赖旧 Willow 全文证明。
3. [Building self-improving tax agents with Codex](https://openai.com/index/building-self-improving-tax-agents-with-codex/)，官方RSS May27 07:00 GMT（May27 15:00 BJT）；生产修正混合偏好/工作流噪声 → reviewed grouped findings 才转 bounded eval和只读provenance/可写产品表面分离 → 限定自改进任务入口与人审责任；拟2+2+2=6，标准审阅，待具体owner比较。不是因税务应用本身准入，不采用7,000 returns/97%等非对照指标为机制效应。原始正文已通过web工具读 §The problem、three-part loop、steps1–3、How to use、Expanding；限定自动化仅extraction/mapper，架构/发布/最终税务审批仍属人。待reader准入校准及具体owner。

分层代表排除/线索：

- OpenAI [Warp’s big bet on building open source with GPT-5.5](https://openai.com/index/warp/)：实际读 Oz orchestration、persistent memory/subagents、handoff/evals 与末段 early/experimental；目前仅产品应用和宏观愿景，无足以改变长任务设计选择的新机制/受控边界证据；EX-contribution，不强行为收入数字追配置。
- OpenAI [Cisco and OpenAI redefine enterprise engineering with Codex](https://openai.com/index/cisco/)：RSS确认May27，但正文读取需恢复，尚未因标题硬排；不计已关闭。
- OpenAI [Election information and safeguards in 2026](https://openai.com/index/election-safeguards-2026/)：实际读原文初始段及当前明确Oct20 update；选举可靠来源、现有C2PA/SynthID、滥用治理部署说明，机制引用之前已公开来源，未见本窗新的模型/系统设计增量；EX-contribution，Oct20修订不冒May27内容。
- Google DeepMind 当前 /blog/page/2/ 与 /3/：science条目（药物/aging/liver/ALS/WeatherNext）按 ROADMAP 明确暂缓，标题范围明确不逐篇扩读；模型/系统标题仍核具体日。不是“Google无命中”。
- Seed publications当前首20（实际18可见），May29 Task-Focused、May26 More Expressive Feedforward / Scale Vectors夹住May27；仅此research目录无May27条目，尚需Blog入口。
- Qwen official retrieval 返回40 articles、顺序非日期排序，实际读取全组extra.date；May29 Qwen-VLA邻近且无May27，不以首条结束。
- arXiv 错误入口 `SUP_arxiv_lm_20261021.html` 用了latest submitted date且截断，已撤出正面coverage；纠正 `submitted_date_first` May22–26 language model 得580（第1页200完整），后发ID说明提交不等于公告；宽结果仅线索，不转580逐项队列。复合字符串OR在advanced单个term返回无命中，不能当完整系统/多模态覆盖；当前API为 `Rate exceeded.`，announced_date_first日级表单明确报错，均保留失败原件，正在有限可执行恢复。

## A3. 来源实际入口与停点（进行中）

2026-10-21 本次实际抓取原件均以 `SUP_` 为前缀，文件名即source标识。OpenAI Research curl403后官方全站RSS恢复（1303项，按明确GMT转换目标BJT日，May27四条）；Anthropic research index200，完整可见research列表仅晚于May27，内嵌news相邻May22不能冒research历史覆盖；DeepMind真实page2/3已恢复；Research May2026博客web成功（May27隐私聚合），pubs首15没有月日字段须独立隔离。Meta research连接超时，限定May27官方站search未恢复精确材料，尚待替代。DeepSeek首页、Kimi platform blog、Hunyuan Research+publicList、Z.ai Research、Seed public papers、ERNIE Blog、MiMo、MiniMax Blog均已实际抓原件，不沿旧no-hit标签自动通过。Hunyuan publicList total9且list9，renderType0为全部实际请求，publicAt/displayPublishTime需分别解释；MiMo当前首页仅paper/blog锚点，不能当日期目录。

普通待办：完成14来源有限停点，arXiv日期/去重与必要题摘，本批准入校准、必要Source/具体owner、六部分合并、DAY/保存完成态FINAL。真实历史目录/日期资格缺失需精确隔离，不用进行中项充终态保留。

## A4. Tax AI 具体 owner 差额与最小正文

当前 `AGENT-PLATFORM` Ch84 §Feedback 与演化已有“平台闭环”及“不应把成功/失败 trajectory 直接自动写入 global memory 或训练集”，后承双时间尺度skill/参数演化；Ch83拥有协议协商/调用而非任务改进准入。已读项目背景、学习理念、写作指南、ROADMAP及最新路由，目标论证与协议章交接，不改变既有source绑定。reader R4确认缺口是“纠正值先辨噪声/责任，聚合review后才生成工程任务”与只读原证据/可写产品面分离；不是泛泛加一条self-improve例子。root已协调本窄位。

拟在上述 global-memory 段之后、双时间尺度段之前加两段（6分因明确知识缺口深入受影响机制）：

> 人的修正也不能直接当作待修复的产品错误。一个最终值与 Agent 预测不同，可能来自抽取或映射失败、尚未支持的行为，也可能只是操作者偏好、上游沿用值或正常工作流噪声。平台应先保存源材料、带引用的中间字段、提交结果和人的改动，把差异变成可审阅的记录；只有经复核、聚合成重复且可行动的问题，才生成带代表输入、期望输出和成功条件的有界工程任务。这样把“收集反馈”与“准许修改”分开，代价是专家复核和证据管线，而不是把任何 correction 都放大成自动改代码的触发器。
>
> 改进任务的环境还要分开可写的产品表面与只读的生产原证据：Agent 可以检查 trace、schema、mapper 和 grader，在隔离工作区提出局部修改，并运行目标评价与较宽的回归；它不能为了通过检查改写原始案例，也不因此取得发布权。证据含糊或无法安全自动处理时，回交产品团队；架构取舍、上线和最终业务审批仍由对应人类 owner 承担。OpenAI 与 Thrive 的 Tax AI 案例支持这种受限产品层的工程闭环，但其季内任务构成在变化且没有可比的无闭环对照，不能把观察到的完成率增长归因于某一个组件，更不能推成任意 Agent 能安全自主改进。<!-- source-family:SF-2026-OPENAI-TAX-AI-LOOP -->

本人 note 拟记录官方RSS May27 07:00GMT及必要核心位置、无对照/任务构成变化、人审与只读证据边界，未核artifact/未复现；只在实际POST后声明写后通过。

## A5. 实际 Books POST 与 arXiv 首批题摘校准包

Tax AI 两段已经写入 Ch84（加入 reader 要求的“在这种批量反馈自动转任务的路径中”限定），本人末注亦已保存；reader R6实际读取正文、完整局部前后衔接与本人注通过，窄锁释放。此有效层不重复行政PRE。

### 日期恢复方法的具体检验

六主题 original-submission May25–26 的完整有限入口（LM p1+p2、transformer、diffusion、agent、GPU、world model）共463个去重线索；这里既有日期待核，也有明确范围外，不是463候选或逐项关闭队列。对这些具名精确DOI分七批 OR lookup，原件 `SUP_datacite_discovered_0_20261021.json` 至 `_6_20261021.json`，共70×6+43=463，只用于恢复日期字段及定位相同身份，不以注册日期单独准入或形成论文池。156个registered上界落May27 BJT，不等于156确认候选。276个registered最晚界早于窗口（不会倒推确切公开日），其余按当前官方 announced month/具名范围处置，不由later registration单独排日。

方法具名有效实例：MobileExplorer `2605.26546v1`，官方abs唯一v1=`2026-05-26 04:53:53 UTC`，官方正常公告最早界为May26 20:00 EDT，即May27 08:00 BJT；DataCite精确DOI、client=`arxiv.content`、state=`findable`、registered=`2026-05-27T02:11:50Z`为May27 10:11:50BJT最晚界，区间一致且全落May27。原件`SUP_datacite_26546_20261021.json`及官方abs链接。反例`2605.26112` registered=`2026-05-26T03:55:00Z`，不把它当本日公告证明。此前registered范围query为0属于不支持的检索，不作无命中；月目录先错误2605已纠正2026-05但响应截断，不授日期列表完成。

### 第一批30条完整题摘后的准入潜力（未完成必要Source/日期）

以下全部题目/完整摘要来自本日bounded官方HTML的 `abstract-full` 到段落结束，已纠正嵌套高亮span截断问题。不是仅读搜索短句，也没有将读完摘要当深审完成。

| ID | 旧约束 → 实际新增 → 可能改变的选择 | 初筛 |
| --- | --- | --- |
| 26546 MobileExplorer | 长VLM reasoning空档 → 并行UI probe+两级回退+结构记忆 → 端侧延迟与副作用恢复分责 | IN，6，日期具名合证通过 |
| 26542 ChainCaps | 单工具许可不能阻止组合洗权 → value携sink-specific预算并intersection衰减 → proxy-visible explicit flow的composition gate | IN，7，trusted manifest质量关键反侧 |
| 26539 FuzzPilot | 热路径昂贵推理 → plateau时离线JSON recipe+微型验证再promotion → 控制器收益不能归因于未获采纳LLM proposal | IN，5，N5/饱和cJSON负面归因证据 |
| 26530 LexGuard | 法律should-change/should-not-change与SMT应用 → 尚未建立超越领域规则应用的新机制/通用边界 | EX贡献，非因没有改善分数 |
| 26521 Structural Coverage | E2E成功不能测声明路径覆盖 → typed协调图生成obligations与runtime witness → 语义成功之外的结构测试充分性 | IN，6 |
| 26508 Actuarial Runtime | 拆分action可规避风险计量 → 固定safe-default+underwriting边界/潜势望远镜 → 有界预算gate的假设与跨边界限制 | IN，6，理论必要假设待读 |
| 26503 Uncertainty Gaussian Map | VLN观察忽略几何/语义/外观不确定 → 扰动+Fisher显式入3D value map → 探索/动作的感知可靠性条件 | IN，6 |
| 26500 Open-set Gaussian Map | 场景地图欠几何/语义 → online pseudo-lidar+open-set grouping+多粒度action → 可变场景表示/决策接口 | IN，6 |
| 26497 AuthGraph | provenance单视角无clean授权基线 → 隔离intent graph对齐execution provenance → 参数来源级校验 | IN，7，拒绝直接采用绝对information-theoretic宣传 |
| 26494 MiniMax-M2 | agent RL长轨迹pipeline → windowFIFO/prefix-tree/white-black-box分责与artifact reward → 调度和训练推理解耦 | IN，6，同家族旧Forge/M2事件须定点去重 |
| 26457 Verus-SpecGym | 形式证明不保证spec忠于需求 → exec_spec+官方/对抗测试 → verifier成功与任务语义分责，judge遗漏26% | IN，6 |
| 26448 Constitutional arms races | 对抗共演化依赖fitness/seed → 独立评分无对抗压力与低seed模式回归 → 评价函数与mutation搜索可靠性 | IN潜力，6，原文核条件 |
| 26437 LLM-human strategic baselines | 人类/LLM策略相似不等机制相同 → 有限理性基线检验 → 具体增量待题摘校准 | 待校准，非默认IN |
| 26418 DRL autoscaling | 基线未校准可虚增RL收益 → 六算法对calibrated rule，时变负载条件 → 有界controller收益归因 | IN潜力，6，是否直接本项目系统切片待校准 |
| 26403 Aligned simulator | 多轮RL静态上下文分布偏移 → 校准simulator交互rollout → 用户模拟器外推边界 | IN，6；Ch31具名正文可定点NC |
| 26397 Autistic communication | persona rewrite下沟通风格与社会群体表征评估，未见模型/系统设计选择新机制 | EX贡献；不以敏感主题本身排除 |
| 26394 Text-to-SQL memory | 简单stateless与复杂memory因子混杂 → working/episodic/semantic三向消融 → memory复杂度非单调 | IN，6 |
| 26357 Fast/slow SF | abrupt task切换偏向plasticity → gradual drift下多时间尺度SF consolidation → continual adaptation优先级 | IN潜力，6，非因小模型排除 |
| 26352 RICE-PO | 最终reward混淆latent reasoning credit → uncertainty action锚点+counterfactual和residual gate → 检索互动训练监督资格 | IN，6 |
| 26343 MechRL | 每behaviour重搜circuit → 跨12行为训练可迁移edge-removal policy → 可学习搜索与size/cost反侧 | IN，6，GPT2-small有限机制不拒收 |
| 26329 JobBench | 人类想delegation而非经济价值选题；新任务/排行榜但未给可改变机制/失效归因的增量 | EX贡献 |
| 26321 Anchor | 多源生成task/oracle漂移 → 单constraint-spec共同生成可解任务与verifier → benchmark一致性生命周期 | IN，6；Ch66具名段可定点NC |
| 26316 E3C | ego动态遮挡与场景混合 → 3D memory+ego/exo解耦与persistent token → 控制与场景持久性分责 | IN，6 |
| 26302 AgingBench | day1 benchmark忽略derived-state老化 → 四机制+paired probes定位pipeline阶段 → 长期评价修复目标 | IN，6；Ch84具名段需对读真实机制 |
| 26298 Sandlock | container/VM成本与wrapper弱边界 → 静态kernel policy+窄dynamic supervisor → 无root隔离与rollback限制 | IN，6，安全域必要深入；Ch72具名正文 |
| 26297 Workload | 长prompt不等agent多轮 → cache复用后decode/KV长期状态+tool时序实测 → 容量评价工作负载合同 | IN，6；Ch66具名正文 |
| 26289 Stateful Inference | 独立请求重算 → persistentKV+radix+lookup speculation → delta成本与baseline真实cache资格 | IN，6；Ch45具名正文，性能归因需反侧 |
| 26286 Delay Compensation | 一般MARL延迟状态估计plugin，题摘未建立foundation/模型驱动行动主线新的关系 | EX范围，非‘非LLM一律排’ |
| 26278 Coalition Free Energy | 车辆轨迹合作game的precision adaptation，未建立当前foundation/系统机制直接增量 | EX范围 |
| 26275 SPEAR | APE固定优化器 → code-as-action分析evalDataFrame+rollback/guard floor → optimizer的证据表面与回退资格 | IN，6 |

尚未将上述潜力当本日最终候选或证据完成；独立reader首批实际校准后继续受影响集合。其余题摘与有界同义入口仍普通可执行。

## A6. 第二批完整题摘与同义线索（待实际校准）

又完整读65条可能相关题摘；标题清楚属于医学、化学、天文、一般数学/交通/工业识别等的其余线索不因含AI/Transformer送入贡献队列，身份仍在官方原始HTML。以下是具体机制/边界潜力，不以能映射章节或抽象术语代替准入；IN不等于日期/Source/Books已完成。

| ID | 初筛与具体依据 |
| --- | --- |
| 26269 AgentSecBench | IN6：三个security game将注释与真实projection/channel closure分开，exact-marker不冒semantic安全 |
| 26256 POLAR | IN5：semantic/episodic多模态图追踪跨interaction更新的个性化对象指代，需核是否只是组合收益 |
| 26252 GEM | IN6：record correctness与state-trajectory correctness及四operator/六条件，需核理论假设与prototype边界 |
| 26239 Sentinel | IN5：foundation communication与classical planner分责，dynamic constraints下replan条件；非仅新场景 |
| 26203 AgentSociety | IN6：liquid delegation/information disclosure激励兼容与marginal contribution routing，核均衡假设 |
| 26195 CyberEvolver | IN5：四层scaffold+trace诊断+population beam的局部归因，安全域核必要边界不当攻击推广保证 |
| 26186 SetupX | IN6：non-invertible修复用LIFO snapshot与独立prosecutor/judge区分setup失败/仓库bug |
| 26178 ATOM | IN5：离线stable backbone+query-conditioned可预算节点，不以‘像原子’命名准入 |
| 26177 RepoMirage | IN6：语义保留repo扰动揭示exploration drift，E2E patch成功不等结构reasoning |
| 26174 Cross-section cliff | IN6：固定文档缺陷/seed、改变orchestration诊断跨section缺陷与criterion shift；拒绝universal外推 |
| 26538 Scheduled Style | IN5：layer/time style-strength与ControlNet近独立、调度方向反侧，Pareto而非单点数字 |
| 26535 RecFM | EX范围：科学动力学emulation按AI for Science暂缓，不借Flow节点引回 |
| 26491 LAIR | IN6：组内centered advantage+quadratic implicit reward约束，核closed-form条件与pairwise对照 |
| 26470 TriPS | IN5：DC/CFG/stochasticity的时间相互作用与control schedule，不把GRPO名字当贡献 |
| 26460 AnchorDiff | IN5：semantic anchor与structural graph传播拆分以抑制MM-DiT concept leakage，核confusable concept反侧 |
| 26449 CAT | IN6：各尺度marginal realism不等同sample trajectory refinement，跨尺度一致性regularization |
| 26391 Garment Particles | EX贡献：closed garment生成/缝制编辑特化表示+flow组合，目前未显示可改变当前foundation表示设计的边界 |
| 26353 DecoupleGen | IN5：rare-context合成维持original-distribution/verification约束，需核shortcut与有效性归因 |
| 26332 BEAP | IN6：黑盒正常语言prompt评估unlearning残留、held-out evaluator+失败query全计；安全域深入 |
| 26282 MBDPO | IN6：search-policy与value policy错位，latent diffusion score-field使训练/搜索对齐，非仅扩大world model |
| 26266 Jensen KV bias | IN6：量化key经exp凸性增attention mass、per-score expectation校正；核二阶近似及quality/memory代价 |
| 26230 GARD | IN5：foundation reconstructor内部geometry-aware feature去噪而非RGB去噪，需核泛化/成本 |
| 26478 SDPG | IN5：trajectory perturbation替代大batch on-policy render，核训练费/样本/视觉control可比条件 |
| 26461 MPS resilience | IN6：可隔离fault的open-driver intervention与其他fault warm standby分层，不把恢复当fault全隔离 |
| 26384 GridPilot | IN6：three-timescale+deterministic bypass与facility-meter PUE校正，3V100证据不冒MW部署 |
| 26537 Conceptual Steganography | IN6：reasoning策略层channel耐paraphrase，策略感知paraphrase反侧，不授任意隐写 |
| 26526 Openweight defenses | IN6：仅finetuning威胁模型漏abliteration/prefill，ART仍残留风险；安全域深入 |
| 26520 InterSketch | IN5：tool sketch/text交错与step reward，核reflection/extra compute混杂 |
| 26501 MMAS | IN5：黑盒跨modal joint perturbation/gradient一致性与访问假设，必要原文定点核‘query-only’是否自洽 |
| 26498 Verilog-Evolve | IN5：versioned promotion包含simulation/synthesis/timing proxy及skill验证，不把proxy当芯片PPA |
| 26489 SoSD | IN6：normalized singular谱早稳而权重继续变，simplified Transformer loss界的假设与现代pretrain解释 |
| 26485 OmniInteract | IN6：真实无future audiovisual trigger/response-window，offline能力不等在线及时交互 |
| 26484 Extra-Merge | IN6：merged而非raw checkpoints的rank1低通/外推，核模型规模与最优方向限定 |
| 26454 Unlearning function | IN6：knowledge/toxicity不同内部目标，非统一擦除loss；核两个新objective的可比性 |
| 26441 Game VTG | EX范围/贡献：传统weakly supervised temporal grounding任务的game-score模块，不是foundation/VLA机制新边界 |
| 26433 SurfaceLoRA | IN6：同输入的exported final-token与pooled artifact隐私不互代，主线data surface边界而非医疗应用收益 |
| 26431 Minimalist phase | IN5：UD probe target外syntactic sign reversal与不改target-string的activation patch；小局部representation证据 |
| 26421 HydraPrompt | EX贡献：synthetic-image detection的asymmetric prompts+contrastive组合，未见通用foundation设计新条件 |
| 26415 Rescue Effect | IN6：CLIP方向alignment随INT8层噪声崩坏，early exit在双向救援/损害tradeoff下校准 |
| 26414 PAL robustness | IN5：paired symbolic perturbations下code execution未胜CoT且p=.096；不因负面/单model排除 |
| 26400 Search summaries plans | 待定点：抽象仅框架与实施计划，无具体可改变选择的增量，需有限核心补读再决定 |
| 26399 OmniGF | IN5：离散language与连续spatial branch分责，multi-person共享scene表示；核非仅加模块 |
| 26380 VisualNeedle | IN6：crop-black反事实剥离视觉tool内容，核工具收益是否真正依赖中间evidence |
| 26366 FEPoID | IN5：旧layer-selection准则失败与intrinsic-dim first-peak/截断，核selection与test信息泄漏 |
| 26365 Cultural steering | IN5：scenario/tokenprob与activation steering揭示维度纠缠，核probe/judge及‘culture’过度解释 |
| 26362 Structured knowledge | IN6：FF grounding失败与attention shortcut区分，核表/graph跨task相关与干预因果分界 |
| 26356 RAG in-context GD | IN6：linear attention精确等价与nonlinear分布依赖边界，冻结generator interface forward update |
| 26339 QAM-W | IN6：2D codec结构/rotation/scaling在5–6bpw适用，严格4bpw不胜QTIP反侧 |
| 26322 OmniToM | IN5：belief extraction/7dim label拆开actor knowledge-access，终答准确不等belief正确 |
| 26315 Staged Competence | IN5：difficulty sampling与reference update的DPO OOD条件，核数据量/overrefusal对照 |
| 26293 CroCo | IN6：英文reward用于多语within-language排序/on-policy data必要，offpolicy/online无增益反侧 |
| 26279 MPMMine | EX范围：传统mathematical-program constraint acquisition目录/工具，NL artifact并不自动成foundation方法研究 |
| 26248 UNSL | IN6：多轴同时变动functional form与extrapolation条件，核域/fit与heldout预算 |
| 26246 Bridge Garden | IN6：hard/soft KD差别不是teacher matching，曝光偏移与exact/flexible steps的hybrid选择 |
| 26242 Introspection | IN6：input-only控制与内部/输入扰动区分检验privileged access，不把会答题当二阶表征 |
| 26241 RoMo | EX贡献：新motion数据与taxonomy/工具，题摘未给具体改变设计的已发现blindspot或新data机制 |
| 26236 DuoGesture | EX贡献：gesture-specific双stream/gate/biomech组合与任务收益，未建立当前foundation系统新边界 |
| 26232 UniMVU | IN5：instruction-conditioned inner/whole-modality gating与time-aligned fast-slow，核相关性不冒因果 |
| 26184 GAC | IN6：混合gradient MSE上界以noise/disagreement确定SFT-RL权重，practical smoothing/cap及prior分账 |
| 26176 PitchBench | IN5：受控pitch声源/时长/notation变化揭示audio perception评价盲点，不只是新增排行榜 |
| 26175 InfoQuant | IN6：小range+充分dispersion而非只抑outlier，PSOT/selector与低bit适用条件 |
| 26355 EGA/MoPE | IN5：salience与locality互补的小模型反例，single-seed与two-runs措辞需核，不外推scale |
| 26368 PaGeR | EX贡献：perspective foundation移植panorama+mixed training，题摘主要是领域适配/多指标改善，无新通用机制条件 |
| 26486 LongCat1.5 | IN5潜力：8NFE distill与audio encoder/data/RLHF工程tradeoff，必要成本/quality core核实后定界 |
| 26379 LeJEPA identifiability | IN6：stationary additive-noise latent下Gaussian唯一性/近似界与planning，理论必要假设深入 |

有界同义补检已实际执行original May25–26：vision language60、VLA8、MoE8、RAG19、kernel35、communication52、long context24，全部到唯一页末；新增59个去重线索，其中18个registered上界落May27，仅恢复线索不授日期。进一步完整题摘读取：26519 R3（global frame导致streaming漂移→relative regression/训练置信与pose aggregation，IN6）、26371 CARL（local-dynamics/action序列对齐可重用skill，IN5潜力）、26525 ReCA（有限generator context递归分配/structured state而非lossyframe chaining，IN6）、26496 Dense2MoE（Roofline下剪attention并复用MLP upcycle，IN6）、26476 FAB-Bench（领域RAG context曲线诊断是否新混杂证据，待准入校准）、26200 WorkflowClosure（AI for Science自动研究按ROADMAP暂缓，EX范围，不借通用workflow节点引回）。其余新增的数学、器件、通信定位或非foundation机器人条目仅标题范围排除，不默认逐项审阅。

## A7. 首轮独立校准差额与已读必要 Source

独立reader已实际读全部A5/A6拟IN及分层代表EX完整题摘，按来源/主题/理由复核。修正：26418 genericHPA无具体ML工作负载/状态切片，EX范围；26437残差重命名及corpus-retrieval必然性未由推导/证据支持，四tests仍计划，EX贡献；26256 POLAR/26239 Sentinel/26353 DecoupleGen/26498 Verilog-Evolve/26399 OmniGF仅现有组合/领域适配未给新增条件，EX贡献。26397不得沿A5 current-v2题摘评价v1 psychometric weighting；reader正回v1限定，v2仅修订信号不倒灌。26195 CyberEvolver、26520 InterSketch、26400 SearchSummaryPlans、26486 LongCat1.5、26476 FAB仅补决定准入的有限片段，不预授Source队列。26200不能因auto-research字样当AI for Science硬排，改为只核audit是否有具体新failure evidence；未核前不记EX最终。

### 26289 Stateful inference — necessary exact-v1 read, comparative claim disputed

实际读取 `SUP_26289_v1_20261021.html` §2成本、§3.1–3.5（sequence pool、cell-budget/grouped prefill、radix metadata alias、delta save、render/token caches）、§4全部、§5全部、§6.1–6.2。采用机制限定：单统一context中固定sequence pool，精确token-prefix命中后共享KV页并只forward增量；KV/radix驻留、exact-prefix及单GPU限制真实。metadata alias不意味着radix查找/CPUtokenization免费（§3.3 trie查询仍O(m)）。不把response cache与KV cache混为一类。

关键反侧：§4.3说vLLM APC与SGLang RadixAttention启用，却§5解释两baseline每轮full-prefill，且用“no caching of any kind”描述依赖KVprefix reuse的主结果；没有给命中/失效/eviction测量或两机制独立消融，vLLM使用浮动latest image不固版本。L40S48GB、Llama3.1-8B BF16、32k、greedy/max128、6/35turn生成式合成workflow，2.1×/4.2×perturn与约2×E2E均仅作者表1/2，不能证明普遍baseline inferior或归因于stateful session本身；C8 tail无完整p99表/运行配置。拟保6分中心比较争议/暂缓，不降分或由已有Books覆盖抹除反侧；不用于正面性能保证。Ch45现§“Agent跨轮复用…”343附近已承载条件化O(delta)、驻留代价/失效及不授普适改善，不需要为未证比较加写。

### 26297 Agentic workloads — exact-v1 necessary read

实际读取`SUP_26297_v1_20261021.html` §3全部、§4轨迹/失败长尾、§5缓存/时延/PrefillDecode、§6工具类别/时序/表1–2。Qwen3.6-27B与Gemma4-31B，thinking/instant，Claude Code/Harbor，五benchmark（DABStep/SWEPro各sample100）；2×H100NVL/TP2、vLLM0.20.0/OTEL+Jaeger与peragent key gateway关联。披露precision未见，Not Disclosed。关键观察是resident KV无capacity eviction的理想化条件下cached tokens占绝大多数，raw input/output比53.9–559.8不等新增prefill负担，append/output1.5–7.3；84.6–99.5%实测cache命中与decode主导不外推内存压力/并发场景。GemmaInstant ADE Edit失败95.4%与786turn是具体失败路径，不当所有模型任务规律；Agent/TaskOutput慢且增token，Bash/Edit更易失败，两者分账。§6GAIA持续探索为“早读后写”反例，Bash里ls等也说明intent类型粗分类会错。

拟6分深入/具体NC：Ch66正文4793（family26297）已经承载cache identity/KV lifetime/tool pauses/decode distribution及五benchmark/GemmaQwen有限证据，不把本报告当新实验复现；正文无全局cache比例保证。必要Source与具体NC待reader实际核。

### 26298 Sandlock — exact-v1 safety boundary necessary read

实际读取 `SUP_26298_v1_20261021.html` §3–4全部、§5必要COW/TOCTOU责任、§6全部、§8全部。核心是static input-independent policy编译Landlock/seccomp，而syscall-time destination/argv/HTTP/effect由窄notification supervisor处理；child exec前ready握手，参数复制后on-behalf而非让kernel重读child pointer；ABI6/Linux6.12最低，不满足拒启动，DNS固定且无wildcard，HTTPSACL需opt-in sandboxCA，只有endpoint不等HTTPsemantics。Resource limit只是virtual-address/syscall accounting+cooperative SIGSTOP/CONT，非cgroup kernel强隔离（mainstack等未计）。COW只有filesystem，network效果无法回滚；kernel vuln/sidechannel/resource exhaustion outscope，多租户恶意负载推荐microVM。

§6 Ryzen5500U/8GB/Linux6.18，startup20次warm后median、Redis7 100krequests/C50/256B五次median±SD；5ms与75krps限static rules，on-behalf echo256B 20→55μs/p99 33→114μs不能被‘零开销’遮盖；Docker性能比是rootful，feature表比较rootless，不合并。十个deny/allow只是确定性microcheck，不是安全证明；未核artifact或复现。6分受影响安全深入。

Ch72现3123唯一family26298段已有commit前OS enforcement、profile identity、兼容/rollback/fallback，但未讲清“static-kernel / dynamic-broker最早可判点”及COW不能undo network这条必要责任链。拟最小1段整合而非宣称已有完全覆盖；待root协调具体窄位、reader必要Source/逐字措辞与唯一实际POST。不因‘仅工具实现’缩池或预写未经授权位置。

## A8. 日期/版本实核差额与 Sandlock 最小措辞

作者已实际核全部已下载current abs的history/comments。26500同题同作者同摘要已由reader定点官方CVF ICCV2025早稿确认，EX-date；26503明确ICLR2026早稿线索待OpenReview；26501 AAAI2026信号待官方proceedings。26508 Comments明确`previously posted on SSRN (id 6761960)`，其arxiv最早/最晚界只证明arxiv公告落May27，不证明全球firstpublic；立即撤回全球资格已通过声明、暂停Ch84新段，必要Source读到的定理假设/反侧不删除。不是把更早公开信号藏起来，也不以不完整本窗资格先加候选。

Kimi官方[What's New](https://www.kimi.com/code/docs/en/kimi-code/whats-new.html#v0-4-0-may-27-2026)实际May27 v0.4.0三条：plugin package捆绑Skills/MCP、session export、cwd外read-only不再approval；v0.1声明与旧Python/uv kimi-cli为TS/Node重写、配置不兼容，故不套用旧CLI1.x身份/代码。1+2+2=5，受影响安全审批条件必要深入/仅报告；只采发布事实不采未来currentconfig为May27实现，不证明read-only保密或插件权限隔离。reader实际完整原段校准通过；原件`SUP_kimi_whatsnew_20261021.html`。

Sandlock Source/Ch72具体差额已reader实核。root协调的拟窄位仅在当前family26298段后、Windows分责段前，加如下单段及本人note（未获锁不写）：

> 实现这类边界时，应选择最早能够可靠判定的执行点，而不是把所有操作都交给运行时回调。输入无关的路径、端口与系统调用规则可先编译成内核策略；依赖当前目的地址、参数或 HTTP 内容的判断才交给窄 supervisor，无法消除竞争或语义不匹配时拒绝执行。Sandlock 的具体分支对网络参数先复制、验证，再由 supervisor 代执行，避免内核重读可变的 child 指针；`execve` 参数检查则使用停住相关执行的单独路径，不能笼统视为同一种代执行。这个拆分减少热路径干预，却仍受最低 Landlock ABI、工具兼容和 supervisor 成本约束；其 COW 只覆盖文件系统，不会撤销网络副作用，协作式资源计量也不能代替 cgroup 或 microVM 的对抗隔离。<!-- source-family:SF-2026-ARXIV-2605-26298-supp -->

本人note只记录必要§3–6/8、ABI floor、网络/exec路径区别、local Linux静态微评测及on-behalf额外成本、无网络undo/非对抗resource cap，未跑代码/未复现；POST由本日非writer reader唯一实际执行，不预支日级验收。

## A9. 资格排除与新必要 Source（继续）

26508由reader实际恢复SSRN官方同题完整摘要，Posted20May2026/DateWrittenMay14，safe-default/no-splitting/authority premium/adaptive envelope已披露；26503官方ICLR proceedings同题同九作者/摘要/24页与Apr25 poster已早于May27公开；26500官方CVF ICCV2025同稿。三者均EX-date，不把arxiv首次公告冒全球firstpublic，不追无关全史，26508 Ch84窄位已释放。26501作者实际恢复[AAAI出版方](https://ojs.aaai.org/index.php/AAAI/article/view/37388)，同题同作者同摘要，DOI10.1609/aaai.v40i5.37388，Published2026-03-14，EX-date。

Sandlock Ch72指定单段与本人note已实际写入；reader唯一真实POST完整新增、直接前后与本人note通过，窄锁释放，不预日级DAY。

### 26538 Scheduled Style — exact-v1 necessary read

实际读取§3–7全核心、Tables1–3/图注（未看像素）。无训练/无新增参数，只让StyleID query-preservation gamma随6decoder层/50steps变化，并独立接depth-ControlNet。20COCO×40WikiArt=800pair，512²、SD1.4/DDIM50、RTX3090；扩SD1.5/2.1同族，其他方法旧报指标非全重跑。反向schedule与gamma固定0.5/0.75对照支持局部时序/强度取舍；仅三种fixed gamma构造的离散frontier，不能宣称已穷尽连续最优。关键反侧：combined FID16.285/LPIPS0.564对fixed0.5的16.572/0.561，LPIPS实际较差，正文“strictly better on both”不成立；ControlNet只部分恢复内容，未证明数学orthogonality或可免联合搜索。sqrt初始下降比linear快，不能照录‘cos/sqrt均初始更gentle’因果。5分标准完成，拟采用‘注入时间/层与内容几何控制需联合验证Pareto而非单数’有限证据，不采用普遍正交/严格dominance。owner待具体对比及reader独核。

### 26491 Diffusion-LAIR — exact-v1 necessary read

实际读取§4–6、A1–2全部推导、C全部消融与E限制。prompt组PickScore softmax减1/N为零和signed weight，linear implicit reward+lambda/N二次项；独立s坐标的唯一极值Nw/(2lambda)成立，但神经网络共享参数并不保证达到它。有限list range不能推出生成分布KL；额外full-support bounded extension及ELBO log-ratio近似只给surrogate tilted distribution，不是真实trainedmodel的hardKL。SD1.5/SDXL/ PickV2，2/3A100，报告24/140GPUhours，其他H100论文‘5x’不作同硬件加速；Parti/HPD五同seedsample，评价含同源PickScore及其他reward非独立human study。官方baselinecheckpoint/DSPO自训/GenEval借Sun2026结果分开；缺matched group-vs-pair同预算因果，N2–30及tau消融仅100prompts且非单调。6分标准+理论假设必要深入，采用loss与条件性bounded-target而非人类偏好/噪声鲁棒保证；具体owner待核。

## A10. 发现封口、来源停止范围与普通剩余

发现不再扩大：六主主题463与七同义新增59，共522去重线索；全部有限query页尾已取到，不将522当候选队列。完整题摘的A5/A6及代表EX已独核；有限6项含糊贡献按下段决定，不因Source费时改变准入。当前arxiv API Rate exceeded、announced exact-day表单不支持、csCL月页传输截断，不补造直接May27公告。官方cutoff+精确v1+arxiv.content/findable/registered合界支持May25 18Z后至May26 18Z前提交者的May27公告；早于cutoff者跨日，不能由注册上界抬早界。26539、26203、26195、26186、26178、26177、26174、26184、26176、26175均保日期资格，有限恢复不成功时隔离，不先深审/当零命中；清楚EX不另追日期。26357有同题ICLR2026 OpenReview PDF、26246有同题ICML2026官方检索线索，正在有限firstpublic核验，不用索引日期代原始公开。

14来源停止范围（A2/A3早期过程态由本节具体结果覆盖，正式六部分仍待合并）：

| 来源 | 本次实际停止位置与结果 | 限制 |
| --- | --- | --- |
| OpenAI | 官方RSS1303项按GMT换BJT目标日四条，Tax准入；Warp/Cisco/Election完整核心已由作者及reader实际读后EX贡献 | Election Oct20更新不倒灌May；Research403不冒全站无遗漏 |
| Anthropic | research当前列表及alignment/interpretability/frontier-red-team官方团队历史页到May邻界；具名May27 coding-agents-social-sciences全文调查1260人EX贡献/应用，Milan组织新闻EX | engineering/history子层未恢复，不授该缺段正面coverage |
| Google | DeepMind真实blog/page/2、/3到May/Apr/Mar；相关具名AIpointer/Genie/transparency均May12/19；Research May月blog May27privacy准入 | pubs首15/11626无月日、year2026的421不是May27列表；pubs历史日级层未恢复；旧May28小时窗缺口与本轮May27分开 |
| Meta | 官方research超时/空响应及限定May27官方site查漏没有精确正文 | 历史列表不可回放，不授no-hit |
| Qwen | 实际GET官方retrieval40 articles全部extra.date，非日期排序，May19/20→May29邻界无May27 | 只对40实际API切片有效，不追全部正文 |
| DeepSeek | 官方当前研究首页、限定May27具名搜索未恢复事件 | 当前V4.1页面不等历史全收；历史目录缺段 |
| Moonshot | platform blog当前截至2025不能代2026；官方Kimi Code CLI What'sNew实际v0.4 May27三变更及v0.1身份迁移，5分Only | 只审批触发变化，不证隔离/保密；不套legacy PythonCLI |
| Hunyuan | 正确host publicList POST pageNum1/pageSize100/renderType0，total9/list9全title与三时间字段读完，无字段May27 | 时间字段互不等价，9当前项不保证历年全收 |
| Z.ai | 官方Research完整当前dated目录，May20 ZCube/Jun16 GLM5.2邻界 | 当前dated slice，不泛化所有GitHub变更 |
| Seed | publications首20实际18卡，May26两条/May29一条；正确header US、article_type2/count100/publish_year2026 blog API实际15项，has_morefalse/token空，无May条 | blog total20与实际15不相等，保当前语言/内容变体缺段，不猜漏5条归属 |
| ERNIE | 官方datedBlog首末分页到May9/Apr30/Apr15及更早，无May27 | 限技术blog当前历史切片 |
| MiMo | 实际router8paper直达，日期Mar13/Feb3/Jan8及2025、Jun29；6blog中May30/Jun8/Jun10/Sep27四date实际恢复，均窗外 | v2flashblog和v2.6material页面未渲染日期，不以旧‘全部无日期’继续隔离已恢复部分，残两页不给日级no-hit |
| MiniMax | 官方当前13 dated列表到May27/26与Jun邻界，AgentTeam准入 | 角色分工非新增贡献，未来开源非artifact |
| arXiv | 上述六主题+七同义全页线索，有界相关题摘、精确ID日期和necessary版本，发现封口 | 不是完整学科/全延迟公告召回；具名跨日/早稿资格及实际列表失败精确隔离 |

普通剩余：准入通过但必要Source未完成的具名集合仍沿A5/A6，不新增扫描；reader接26546/542/521/497/457/397必要域及Agent两条26269/26252，作者接其余。已下载不算已审；26457/26542/26497真实Books已写等待或已到reader唯一POST，实际事实以其R12续记为准。Tax/Sandlock真实POST有效，未重做；六部分合并、逐项具体Books处置、DAY与保存完成态FINAL均尚普通，不能用本节冒日级完成。并发index staged原件保留，本方未stage/commit/push。

## A11. 六项含糊贡献的有限核心与 TriPS 必要 Source

- 26486 LongCat1.5：实际§3.4/4/5.4有shared DiT+Generator/FakeScore LoRA切换、base real-score，避免三同构backbone同时驻留，非仅8NFE营销。8NFE对base50steps×3passes=150NFE明确损humanlikeness/lipsync/diversity、换稳定性，未给匹配硬件VRAM数；拟IN5限定角色共享与代价，待reader校准及其他必要方法/评价，不授Source完整。
- 26520 InterSketch：实际§3.3/4.3/C1–3，quantifiable GT-action score与GT-conditioned VLM sufficiency两种step证据接口，反思错误token mask；拟IN5待校准。Eq7归一差额在logprob负分母时可反向、s0=s1=0未闭，不能照录正确credit保证；四项samebase ablation有局部收益但未提供全token/调用成本控制，图中turn少不等E2E快。准入事实已够，不能以坏公式直接排除潜在贡献。
- 26400 SGSS：实际§3–5全部，XUX以read-prefix质量期望给top-heavy分、跨summary pooledsections以JSD评coverage，再加权；不只是未来计划。可复查的新指标提议，拟IN5仅报告，实证/用户阅读分布/标签与权重可靠性全未来，自己的section自动perfect/重复section会影响pool，不当groundtruth或真实体验；待reader有限校准。
- 26476 FAB：实际§4/5.3–4/8.3，只200行业QA随configured4–32K context与outputcap共同变化，max4snippets且未报actualtokens；高分直接归attentionfilter/parametricknowledge/12Kcriticalmass，未新测这些机制。没有超出既有more-context非单调/领域曲线的具体新边界，建议EX贡献；不是仅因无显著性/访问困难排除。
- 26200 WorkflowClosure：实际§4–5/B全部audit21，strong/weak依scalar/internal/no-standing-community规则重分类公开流程，无新执行失败、混杂识别或独立验证，建议EX贡献，不再沿A6错误AIforScience范围理由；四domainScience反例只作原论文论证，不引入本项目候选。
- 26195 CyberEvolver：实际§2/3.5有限决定域有selective-verbatim、最多3placeholder原observation回填、score仅同代sibling相对排序与逐层validate/revert，较通用beam更具体，拟IN5但v1May25 16:26:59Z早cutoff，先资格hold不深审；1.7MB HTML本次传输只734KB不称全原件已得，不追攻击示例/载荷附录。

TriPS26470实际§3–6及E2/F6，5分：DC/CFG方向冲突与随机性的有限诊断→两种受限日程搜索，Bernstein-Beta只保证range不保证monotonic（正文承认局部非单调）。100calibration与test disjoint、A100/最高200iters/group4，FFHQ1000/DIV2K800、SD3.5M768²/28NFE、SD1.5 512²/50NFE；PSNR/感知reward权衡与三轴vs单轴支持局部搜索选择，非全指标支配。三种guidance不是新增网络质量真值，cosine与KID不证明exact manifold；完整search+inference计费，F6十样本部分solver慢，不能以同NFE冒等费。只采用局部联合校准、不采用Eq9普适精确梯度或通用单调最优规律；必要TheoryA4待拟采用公式需要时才读，现不采用该式。具体owner待核。

## A12. Quantization 与 upcycling 必要 Source

作者实际26266 exact-v1§4–6全核心/Table1与effectivebit/latency：独立零均匀key噪声使未归一exp项期望增，log-MGF逐score扣减在此模型下修正的是partition项期望，**不是E(softmax ratio)精确无偏**；Taylor取variance/2、小噪声近似，强bit可过修/注意力集中token少时失效，非均匀biased要重推。MAGI4.5B16step/window5→2、SkyReels1.3B50step/window5、HYWorld8B4step，per-token INT2/g32、FP8scale+BF16zero共2.75effectivebits（QVG2.52另protocol），只有current未量化与history量化的混合读；VBenchLong前30%prompts及HY10官方pairs不是全量，BF16参考fidelity不是任务correctness。FlexAttention MAGI约5%额外E2E相对quantbaseline，50%cachebytes例不等GPU总内存/所有生成加速；单token decode headroom小。6分必要理论假设深入。当前Ch45 1276innergrouping/near1642误差witness只量化layout与实际error低秩补偿，未承载exp Jensen期望补偿；可能最小一段在innergrouping尾/before CacheGeometry，待reader必要Source与具体gap/root协调，不提前写。

26339 QAM-W exact-v1作者实际§3–6/Limitations及J4：单位row经sign-Hadamard、相邻2D/scale+jointLloydcodebook、row norm/packing与AWQ式scaling，joint2D与polar等pairbits非byteidentical。主跨model只MLPgate/up/down，attention/head BF16，5.5bpw非整modelbpw；MLP+attention扩展另人口，LMhead仍未动。A10080GB/20h整个研究、TinyLlama1.1/Qwen2.5-3B/Mistral7B及Llama2 7/13B，WikiText16K/PPL、pairedKL4K与six-task limit300/500，MMLU每subject300；±0.2pp不作严格equivalence，std/CI含人口限制。5.5bpw只是不同工作点：strict4bpw QTIP好于QAM；3.5bpw Qwen不竞争。pairGaussian经验假设，orthogonal本身不使Gaussian；不采用codec上界推出observedKL排名必然，未读无关完整证明。所有weights恢复BF16再matmul，无fusedkernel，不能把码本L1/bytes比叫推理加速或kernel已验。6分标准完成，采用codec/consumer/完整bit accounting取舍，具体Ch49owner待比；现未授NC。

26496 Dense2MoE exact-v1作者实际§3–6全核心/Tables1–3：相邻decoder输出与MLP输入cos+norm条件分组，保首attention、其他MLP成heterogeneous expert与router，可skip；225B continualpretrain/N6Top1/loadbalance，0.5/1.5/7B Qwen2.5/Llama2。norm与cos仅校准选择，不数学保证知识保留/全部输入无shift；原GLU命名公式up/gate反常不照录。大部表ms是Thor-U peakFP16/带宽下Roofline估算，B1/In1000/Out50；不能叫已测physicalbound或真实完整延迟。正文另报seed307.5→271ms empirical而主table195.87→174.95不同口径，未给真实engine/kernel/precision/repeats，不能混算共同Pareto。static N6约1.66B/3.32GB大于seed.5B，active.42B不等resident小；增加N6→10成本+60%且分数饱和，MMLU/CMath/ARC等局部回退、NonPruneUC均分更高保留。拟6分中心efficiency/knowledge-perfect争议，潜在heterogeneous upcycle可说明但不授净部署收益；必要baseline/CPT等费资格未闭，若不能有限恢复则本窗争议隔离，不用降分变普通EX。具体Ch21/servingowner待核。

## A13. Grounding、分层生成与几何表示必要 Source

26460 AnchorDiff作者实际v1§4–6全部/T2–6与直接限制：MM-DiT概念attention最大点仅定位seed，row-wise image-attention cosine的top2% gate与output-feature cosine权重传播结构，不以完整dense概念map当mask。SD3Medium/3.5Large1024²/4096tokens/midpoint、RTX4090约.52s每concept含160propsteps，仍需inversion/多pass/取图/图驻留，不作端到端生成费用。1272混synthetic/real confusable images/2842conceptpairs，Qwen2.5VL定位+SAM2mask/人工检查，非真实groundtruth绝对无误；foreground-only IoU与wholeimage标准指标不同。gate去掉崩、Wcos去掉仍近似，部分AP/NAR更好，太长prop泄漏、单anchor漏disconnected同类实例；anchor89–90%本就有错。§5.1 SD3.5 graph layers10/23与后文23/31不合，不照录固定recipe；不称单seed/matching图semantic解耦/所有实例覆盖。5分标准完成，采用semantic initialization vs structural propagation及有限spillover反侧，具体Ch23owner待比。

26449 CAT作者实际v1§3–4/6–7全核心/Eq1–3/T1–5/F3–9图注：多尺度marginal realism并不约束同一sample粗细轨迹；blockdiagonal D不跨scale，G中间pre-resize输出与最终输出加scaleweightedMSE，早粗级弱权重。ImageNet256/SDVAE、B/M/H gen133/261/960M、D96M、batch512/lr2e-4、lambda.1、50Kiter20epochs，FID50K相同trainstats；sameconfig有/无cons与lambda0/.1/1支持局部必要取舍，过强更差。最终output是自产anchor不是真实细节groundtruth，不能从跨scale一致认证语义/分布完全对；onegeneratorforward只inference，训练D+cons全付费。跨论文iMF800epochs/GAT60等预算/模型不同，16.7x GFLOPs非实际walltime/公平硬件或每维更好，部分IS较弱；fullscale-D对照同时删除cons与mask，不能完全独立归因二者。6分标准+长期marginal-vs-trajectory缺口深入，具体Ch24现scale/preview段不承载GAN same-sample监督链，最小正文待reader Source及root协调。

26230 GARD作者实际v1§3–5（截断方法已单独完整补读）、T1–5/B3–4：冻结DA3reconstructor，在第18/40layer内feature而非RGB/VAE denoise，再经后层给geometry与另训RGBdecoder。degradedfeature+.3noise→cleanfeature flow，clean DA3估depth/pose生成pointcloud-correspondence attentiontarget（非传感真值），条件source先验+alignment共变，T4 alignment单用可退，source先验时才增。Hypersim/TartanAir syntheticmotionblur/train最多4views/H100FP32/10epochs/globalbatch8，test10views5DA3sets可30/50，Euler50步；‘single forward’不是oneNFE/无迭代/实时，单纯换geometryspace不普遍保真实几何。DA3-vsVAE samearchitecture较强但其data/support/容量与cleanbackbone假设保留；仍弱于cleanHQ（有些setting乃至其他baseline），稀疏大视角/motionblur之外未证。5分标准完成；采用恢复空间应按下游geometryconsumer与支持共同选，不让像素好看自签3D；Ch23具体owner待核。

## A14. SDPG/GridPilot 与版本恢复实际层

26478 SDPG作者实际v1§3–7全核心，5分标准：N条rendered nominal视轨迹旁M条state-only扰动aux评return，基于固定nominal actionsequence估Gaussian-smoothed surrogate再监督policy，不backprop真实sim、不重复视觉policy评估；代价仍NM物理rollout、critic privileged低维state与短horizon/重置。Gaussian恒等仅smooth目标及delta/sigma重标，不原始return或一般closedloop任意policy无偏；有共享network/固定O条件，Eq3缺1/2与claimstep要另核不照录精确更新倍数。Genesis/VisualMuJoCo/64renderenv、RTX4080，DrQv2/Dreamer3自优化code、distillation；PPO48–50GB是4096env估算，非同protocol实测。Go2 depth两小时sim2real为所示terrain非安全/一般迁移证明，seed敏感/偶发不稳、丢rollout每iter与simulation主成本保留。只采视觉处理与aux动作搜索分离，不以‘halfbackward’或64vs4096授普遍端到端2x/4x；Ch26/31具体owner待比。

26384 GridPilot作者实际v1§3–7全核心，6分必要控制/成本边界：200HzGPU/1Hzhost/hourlycluster与out-of-band C/SCHEDFIFO/isolatedcore绕Python调度，facility-meter PUE而非boardpower定义验收。3V100SXM2 32GB、driver580.65.06/CUDA12/NVML12/Ubuntu24.04，FP32GEMM/Resnet50B1FP16/bursty，E7 90trials只syntheticUDP→95%capsetpoint，约97ms/最大101.1ms并非严格sub100ms，Pythonp99>250ms不推广同语言必然。内环telemetry100Hz不足单独认证200Hz硬实时；SCHEDFIFO假设下TLA liveness不证OS/NVML及时性。E4bursty11.08%超5%需保留，不由‘diagnostic’改写成验收成功；MW/E8是M100trace+syntheticCI+PUE模型replay，未实测cooling/TSO资格/多天supervisory E5（仅design）。CI×PUE deferral/现实cooling解释为模型选择，不当真实碳节约与50MW部署。完整控制/telemetry/未来rebalance费用，低负载PUEfloor可抵消board收益；具体Ch63 power调度/设施meter分责待核，不扩金融规则或当前国家grid法规。

当前事件页轻量版本检查已执行（A8旧现字段实际读有效）；新增current HTML只为必要版本信号/域：26461v2、26526v2、26332v2、26431v3、26380v2、26366v3、26293v2、26242v2、26519v2、26371v2已获取，26489current v1。其中26489/26380/26293传输25s超时保部分原件，不声称全current已取；方法/评价必要片段可先读，确缺部分再有限原始替代。没有复扫整个release或全部版本，也不因v2号码单独算本日重要修订。

## A15. MPS 精确受影响修订与已成事实

日期措辞校正：本节及A14中的Oct2均指current-v2的Submitted字段`2026-10-02T05:50:49Z`，不是已证公开日；只用当前精确版本核影响原采用命题的修订，不把它另记May或Oct2公开事件，不扩10月恢复。Books正文已明写“当前v2（10月2日提交）”。

26461作者实际current-v2§4–8全核心/T2–7及v1§5–6定点对比。**重要修订而非版本号码**：v1在dummy mapping后直接SIGKILL，并以fault硬件暂停推断safe termination；current-v2明确只有出错stream停止不够，新增RoF+PoR：先disable sharedTSG所有channel schedule、请求preemption并确认pending，再dummy mapping/replay，额外fault继续service直到preemption completion；此为process所有stream的barrier，随后daemon终止target、不再enabletarget、恢复survivors。v2三次SASS witness/multistream表显示RoF无PoR会继续另一stream，完整分支才止；这直接限制v1充分隔离结论，不能把Oct2新增实现/试验倒灌May首次版本。

current范围为可达MMU9种（7传播+2CE本已contained）；SM5种归closedRM/GSP/无channel归因，只能surviving GPU上独立context standby恢复，不是fault隔离，device thermal/reset outscope。app决定哪些weights/KV/latents可复用及metadata safe boundary，不从物理页仍在推出语义未损；faultingclient污染自身state应丢弃。VMM持独立物理引用+外MPSstandby/privatecontext约600MiB，发布checkpoint稳态约1%代价，time-sharing诊断窗口/终止faultclient后再回MPS全生命周期。current A600048GB/driver580.95.05/CUDA13/Qwen2.5-14B/vLLM（精度未披露）/顺序batch128 ShareGPT/maxout256；355ms outage与H100 fault-to-catchup28/48ms不同指标/不同hardware不可合。diffusionQwenImage1024²/28steps第14注入、Resnet50另protocol；9+5deterministic fault tests非任意fault/攻击tenant安全证明。r610 staticSMpartition属后续说明，不当May对照。6分必要修订深入，Ch63现family26461两段仅一般fault-domain/recovery，拟最小段补process barrier+survivingstate条件，待reader实际安全域及root窄位。

reader R12后续真实POST事实：26457、26542、26497、26521、26252、26491、26546均通过完整新增/直接完整两侧/本人note，窄位均释放；连同Tax/Sandlock共9项实际整合，不预DAY。26289 Source/Ch45独核6中心对照争议暂缓、26297 currentv2必要cache/tool域+Ch66具体NC6通过（Sep新thrashing数据不倒灌May）；26321 Source及Ch66共有constraint-spec/generator/verifier alignment具体NC6通过；26302 Source及Ch84纵向/checkpoint与Ch77干预矩阵具体NC6通过；26394 Source/Ch77条件矩阵与content/length匹配具体NC6通过。26448有限toyfitness/噪声实例6Only；26397v1 reference加权绝对threshold与ranking分账5Only，v2rewrite不倒灌；26403 human-vsoracle校准/比较协议中心冲突6暂缓。MechRL26343 current-v2六月把singlehead改edgepruning，Mayv1采用对象是单头policysearch；据实际v1命题修准入维度为2+1+2=5（非因时间/Books降分），仅报告小GPT2单头/probe有限实例，不采初筛currentedge跨行为宣传或priming称零条件泛化。所有旧118评分不动。

## A16. 必要安全域：隐写、open-weight与unlearning评价

26537 Conceptual Steganography作者实际v1§2–4.9/Limit全部核心，6分安全深入。公开CoT中的reasoning behavior存在/缺席作为carrier，matched lexicalbaseline仅换carrier；受控compromisedsender/共享codebookreceiver，不是自然形成合谋或真实内部CoT忠实。四model/MATH500+GPQA198/seed42，singlepipeline同model各role与heldoutMiMo换role，preparaphrase/no-paraphrase对照保留；robustness不是stealth（未训detector），无informationcapacity证明。最多约4.4–6.4bits每CoT只是当前分step，message/bit/step三个指标不混；多strategy相互干扰、换paraphraser可大退，strategy-aware已知carrier的defense只一strategy/GPQA/三model且仍有残余。NoCot短cap/提示未必真禁止reasoning、截断计错使‘必须公开CoT才能保性能’不成立；下游再答给partialreasoning不证原内部因果。DeepSeek stepcount repair有rawtokenization问题，只有prefix保守修复，不把修复数字当raw也不外推性能。APImodel/精度硬件ND，不采通用sanitization失败或隐藏不可检测；只采语义保留paraphrase可能保留更高层carrier的audit边界，Ch72具体owner待比，未核攻击payload/像素/artifact或真实外传。

26526 Openweight defenses作者实际v1§4–5全核心与current-v2§2/4–5/A4。6分安全深入，仅检验finetune-tamper保护不自动覆盖非finetune权重编辑/输出prefill两类权限，不给攻击recipe。v1三bench Llama1/3/8与Qwen/Gemma1–2B，HH上SEAM2000/TAR750outer+4–16inner，HarmBench13Bjudge/AlpacaROUGE+关键词refusal不是独立真实有害/全utility；best-per-evalprompt跨层/强度选择不是固定single-shot、candidate search全费。ART v1只有Gemma1B加200step，ASR残49/64/55%与baseline低风险不同，benignrefusal/utility有反退，梯度/内层selectededit不是普遍minimax证明。current-v2（10月6日提交）新增budget/valsplit/singlefixededit benign与8B多defense/fine-tune组合Table8，只作后续支持不倒灌May首次；评价judge还改BeaverDam7B，不能与v1同分母合并。未披露hardware/precision/seeds与全部budget；保攻击族以外未知，拒绝行为恢复≠harmfulknowledge消除、不能从有限类反例证明所有开权安全不可能。Ch72具体NC/最小差额待比。

26332 BEAP作者实际current-v2§III–V/AblationD全部核心及v1§3.1–3.2/§4.1定点原采用权限。query-only定义针对victim，独立offtheshelfencoder不是访问victimencoder，不能因使用CLIP直接否认blackbox；自然语言多signal搜索+semantic词汇只是评价探测面，cosine近邻非已证残余物理representation。v1 SD1.4/safetyfilter禁/最高200I2P，DeepSeekV3.1/最大100生成query，每search用同NudeNet/DINO/IR/Aesthetic评价，无heldout检测器；current-v2（10月5日提交）新增OpenNSFW2/ResNet50heldout、UDA whiteboxbenchmark/失败按fullbudget等是后续改变，不能把97.8%/32.1query作为May原结果。current quality/IR仍searchobjective，ASRAll与概念ASR分开，successful-search平均iter不是全attempt平均；增加Q改变总预算，几项w/oEG反而更好，语法可读/较低gibberish不等不可检测。50 golfball exploratory不代表所有object，classifier hit不证明永久knowledge/internals，旧任务safe-filter外权限不外推在线产品。6分安全深入待v1必要主表/直接限制及reader具体owner，不预Source完成；已有current必要层不删，不重复无关附录。

## A17. 两类 Unlearning 与导出隐私面

26454作者实际v1§4–7/Limit全核心/Eq4–6/T1/图注（未看曲线像素），6分必要unlearning边界深入。cosine替L2只限制方向不保norm、randomtarget并非knowledge删除；toxicity用各层frozen logisticprobe dot²抑direction，layerprobe间cos低是表示读出变化不因果识别语义function。四7–8B模型/WMDPbio+cyber/WikiTextretain/MMLU、ParaDetoxforget/TRuST标签probe与同TRuSTclassifier检测RealToxicity；两目标不同数据/监督/评价，不能把收益唯一归因‘knowledge vs toxicity根本机制不同’。α所谓REINFORCE欠采样policy/reward/outer协议明细，不照录bestpossible自动平衡recipe；Llama危险knowledge S=0灾难点不可藏、各层loss上升与多层非单调反侧保留。新metric是chancecorrected两分数乘积不等Pareto/真实安全，MCQ猜测不等知识消失、classifier低分不证open attack鲁棒；硬件/精度/seed主文ND，完整额外probe/层搜索/训练/测试费。拟仅报告具体function-target选择实例，Ch72现删除对象与probe/不认证knowledge真值链待reader具体比，不能强授全普适配方。

26433 SurfaceLoRA作者实际v1§3–7全核心/T1–2/F1–2/H选点规则。6分安全深入，**不采医疗效果/行政race为生物真值**。同一prompt pre-generation final-token与meanpool是不同exportedartifact，固定backbone/LMhead/decoder，只GRL+LoRA/adversary；后置LR/MLP不同于trainingadversary，patientdisjoint193470/21552/24445，balancedaudit20k/2.5k/2.5k五类chance.2；原realworldprior不由balanced赋予。末token训练1024prompt/1536full/greedycap256，BF16/TF32、singleGPUprocess（硬件型号ND），固定seed/2000steps/lambda6grid。validationonly选LRgap≤.025最高ROUGEL或minimumleakagePareto，不test选；MLP不是selectionadversary、near-chanceCI含.2不证明零信息/未知attack等价/DP。lasttok小gap不转移meanpool(.32/.30)、更长训练回升(.206→.228)、meanpooltarget也未到chance，输出ClinicalBERT仍.299/.616且gold同源相关；ROUGE/BERT/clinicalNER不证临床保真，Neutral meta-term mention不是genuineidentity泄漏。选择、额外promptforward、探针fit/lambda+checkpoint搜索全费；只有exactexport/目标label/攻击者资格的局部门，拟Ch72 representation/privacy surface约702附近最小差额或具体NC待reader，未核原数据/代码/复现。
## A18. 已成 POST、精度修正与有限新 Source

CAT26449、GridPilot26384-supp指定reader真实完整新增/两侧/本人note POST已通过并释放，连同A15后RICE26352、Forge26494、E3C26316、MPS26461-supp、Jensen26266，共16项真实整合通过。Surface26433与ConceptualSteg26537已按reader必要Source/owner/逐字稿与root指定窄位实际保存Ch72各一段＋本人note，尚待唯一真实POST，不预日级验收。

26454精度修正：reader实际AppendB给two epochs/up to4 NVIDIA RTX A6000/about1h perrun，RL lr1e-2/main5e-5/Adam；A17的“主文硬件ND”不代表附录未披露，precision/seed仍ND。26526 current-v2只有新增T8/A4使用BeaverDam7B与heldout，§4/T1–7仍HarmBench13B，不写整个current judge已换；其他v1/current边界保留。

26332 BEAP追加实际v1§4.2–4.3/4.5/T1–2/4全部必要主表与直接反侧：同NudeNet/DINO/IR/aesthetic兼作搜索目标与评测，无heldout detector；w/oEG在SD presence99vs95及MACE All44vs42可优于full，不授embedding阶段单调必要。successful-search迭代均值不含全部失败预算，Oct current才另改全budget；旧SD1.4关闭safetyfilter的诊断不外推在线产品。至此作者必要v1/current域充分，不追payload，待独立Source/owner。

26282 MBDPO作者实际v1§3–6、AppendC4证明与A1.6完整总费T2–3。6分潜在model-based trust-region新机制，但中心理论争议：contrastive跨state负例并不一般等uniform action，E=−log行为密度须neg-density correction；future state的normalizer C(z_h)依赖动作，近似C(z_h)≈C(z_t)不能由short horizon直接证明。C4受KL约束最优为β exp(G/η)，而实现exp[(G−ηE)/κ]在η≠κ时是β^(η/κ)先验，不同于定理主张，不能把同一个exact optimizer/monotonic improvement授给实际目标。world/value近似、有限self-normalized MC/score matching均不继承真实环境无偏/安全。online A80080GB，offline H20010Msteps/1.7–340M，visual5seeds/ablation3，precision ND；A1.6十episode评估多项约1.4–2x更慢（并非训练步一概快），η过高及340M scaling可退。拟6中心争议暂缓、不正面写Books；重开需一致prior/temperature证明、模型偏差与完整同费对照，非索更多无关案例。

26414 PAL robustness作者实际v1§5–7全部。5分标准有限负验证：同ClaudeHaiku4.5/1000 paired样本，CoT97.9→96.6、PAL97.2→95.5、SBSC96.4→95.0，break/fix分开，代码执行不自动修正形式化错。但prompt/system/prefill/15turnerrorfeedback共同变化，1k来自100原题改写有重复聚类，bug后两次执行有API时漂；temp0不授deterministic snapshot。χ²跨组独立假设与同题配对/聚类不合，p=.096非等价检验，不能宣称所有tool无收益/模型不推理。完整调用/成本/训练污染未控，hardware/precision API ND。拟仅报告有限高ceiling反例，不把实验外推通用PAL原则；待reader实际Source/具体owner。

26489 SoSD作者实际v1§3–6主论证/经验全读，理论必要Append证明尚普通：单层单头/fullbatchGD/nontrainable classifier与strict norm increase等条件；normalized singular-value shape不限制singular-vector rotation，需核Theorem4.9从spectrum change控制loss的证明是否额外限定固定vectors。lr/WD/Muon联合变化是局部相关而非通用因果，主文承认较低SoSD非性能指标。尚不采“普遍kinetic bottleneck”正证，继续有限核心证明，不为此扩全附录。
## A19. 训练轨迹、在线交互与表示诊断必要 Source

26484 Extra-Merge作者实际v1§4–6/B全必要配置、C3关键假设与PCA证明域（不声称完整全部理论）。6分：4个merged checkpoint PCA定向＋validation line search可作有限替代分支；8x4090/2H100、GPT124M–1.55B/FineWeb10B、Llama.5/2B C4约105B，BF16；Pythia12B FP16/0shot四task以同均分作search indicator，非独立heldout测试收益，.59pp不当equivalence/实训效率。主文一律WD.1与B各GPT 0/.125有差，以精确配置保留；没有seed/repeat/全searchwalltime。river理论假设straight1D、IIDmountainnoise/stationary/eigengap+concentration，不由相邻滑窗EVR>94认证globalmanifold/实训guarantee。收集/K²innerproduct/每个线搜评估与artifact成本不免费，validation收益非free lunch。Books具体owner待reader。

26485 OmniInteract作者实际v1§3–5/Limit/A2–4全部必要层。6分：250录像/1430slots含192interruption，lateststart分配、early/core wordlevelsplit，softTP/FP/FN+无FNinterrupted，与NOR/PAQ/conditionalspill/NCCS分账；softIA-QTF1不是传统F1，静默可在interruptionglobal无罚，不单一总分授continuity。原audio/video按时间回放无future，不是真人闭环interactive live；4native接口/GPT4o judge，无独立人评校准/硬件精度/运行repeat完整披露。MiniCPM offline全video vsonline信息集与执行模式共同改变，纯quality差不唯一识别full-duplex负担。1QnA TTS vs1Q1A自然语音、Chinese日常/Englishmath范围保留；不凭外部judge称无偏。拟Ch66多阶段时序evaluation具体NC/最小差额待核。

26415 Rescue作者实际v1§3–8全部核心/T1–4。6分：dynamicINT8仅visionLinear、textFP16，ViTB/32/ImageNet/RTX3090，SSA训练128117/3epochs＋独立5000gate，再25pointthreshold选择；3runs unconstrainedseed。947rescue/710loss是prediction配对分账，不是noise唯因：trainedheads/teacher与routing共同，factorial能限定局部routing增量但非√N噪声理论，patchtokens不独立/同distributed噪声未知。量化误差ratio52%不叫noise超过signal，MSE/cos相关不认证普遍深层有害；声明zero-shot只classprompt，不是无监督未见ImageNetlabels。FLOPs按exitdepth估算不含head/gate实际walltime，动态quantize Linear的GPU实现/路径未核不授3090核加速，低位tensorbytes不当端到端收益；只保有限gate选择与false-exit tradeoff，跨backbone未来。具体Books待比。

26431作者实际v1§3–4/6/Limit与currentv3§3–6必要变化。5分仅报告倾向：Mayv1 UD probe r64/13base1–27B/English3kstrings/cluster1000/FDR，本身是UD label限定的结构读出下界，canonical层仍finite对比峰值选点，不能当独立无选择估计。v1直接patch被测embeddedsubject再读包含该word的距离，几何变化不证明真实behavior依赖/MinimalistPhase唯一机制；currentv3改matrixverbpatch/双向、sameverb与breadthfirst人口，后续新证据不倒灌May。RTXPRO6000Blackwell/<2h，precision ND；English词形/词类与标签解释保留，不能用13模型重复证明理论grammar真。未核artifact/行为任务。

26365作者实际v1§3–7/A必要配置。5分标准仅报告倾向：600scenario/300优化300test、tokenA/Bprob与activationmean差/四层grid，T4 FP16/18GPUh/seed42，Llama3B/Qwen4B/Gemma4B。主文Gemini2.5Flash vsA1.5生成身份不合，country mean最近category并非mode，binarylogit不是绕开safety得到真实隐文化。E=.7–.9cross-axis shift不由WVS r=.474证明同latentfeature/人类社会因果；法律/工作选项混规则与价值，未做通用能力alignmenttax，PPL自生成128tokens不等流畅性/安全。层/强度/数据费全计，不把α.2默认泛化或architecture rigidity作因果。

26362作者实际v1§3–9全部核心。6分表示/结构attention vsoutputhidden对照可作为有限诊断，但oracle核心S与支持E按goldanswer/shortestpath/tableanswercell定义，不能线上无GT直接调用，也不能从penultimate residualcos定位FFN语义失效。MetaQA1hop5k/20triples、37.5k train80/20 XGBoost/Llama2/Qwen2.5 7Bgreedy；硬件精度/repeat ND，EM或F1≥.3标签不等真实完整hallucination。弱correlation不自证互补因果，Q3最高在1hop与WTQ，2hop反Q4最高，不能表述统一单一failure；支持集oracle与额外每triple编码/全attention存储不是免成本single inference。拟仅报告有限oracle-conditioned detector，不采semanticgrounding必要/充分或mechanistic因果；待readerSource/owner。
## A20. 有界指标、检索适配与理论限定

26489完整官方v1重取成功[原件](./SUP_26489_v1_complete_20261021.html)，作者实际AppendC证明全读。6中心争议：Eq81给δ≤constη||G||/τ，反向只能给梯度lower；Eq143–144由ε=O(η/τ)把τ^-p upper换O(ε^p)不成立，上界不可逆用。Q/K混项化同τK也未见相等条件；strict norm increase不保证发散，spectrum稳定不限制vectors rotation。只保小模型经验相关，不授普遍kinetic bottleneck/以谱差认证loss瓶颈；重开要有效双侧关系、参数条件或修正定理，非读更多无关lemma。

26366 FEPoID作者实际v1§3.5–6/A，currentv3§3–5/A逐段规范化比较完全相同，受影响域复用（不是号码当重要）。6标准：TwoNN ID firsteffectivepeak仅经验层选择、FST取首句末token，不识别语义真值/天然最优层；9k/1k trainval/test固定、QA10samplesT1另bestT.1（不称deterministic）/30tokens，summary130token；probe仍监督MLP，‘supervision-free’仅选层/FST而非全detector。Table4 FEPoID/ID计算不含同样需训练的MLP全部成本，baseline ValLoss含training，不授10秒E2E；硬件/precision/repeat必要域ND。Firstsentence可能遗漏后文纠错/长summary，FST改基线输入亦改被判对象，不普遍将末token低效归唯一EOS噪声。具体owner待reader。

26380 VisualNeedle作者实际v1§3–5/A1–2及currentv2所有changed核心段（页面partial但必要主文完整）。6标准：300curated/9API/20turnfreshagent，cropblack保toolprotocol和图尺寸，不固定adaptive后续轨迹；保initialfullimage，黑图OOD变化不单独证明因果纯视觉依赖。v1称所有diagnostics3runs，current明确textonly/cropblack once，不能沿用3run置信；main无/有tool3runs有效，后current targetcoverage分析不倒灌May。Gemini3.1Pro兼受测与fallbackjudge，‘independent’是接口分责非独立真值；不同模型tokenbudget/reasoning/resize共同不同，human majority3/Pass3不直接对单API公平能力排序。全部crop/extra画像/重试/判断费，hardwareprecAPI ND；具体Ch66介入诊断/Ch78consumer责任待比。

26356 RAG-GD作者实际v1§3–7/A/G/H。6标准：无softmax/线性平方loss存在性构造只one gradient shift，不是现代frozenLLM内部等价；实际固定BM25/E5 top5与NF4 Qwen7B/Llama8B，每层QKV rank16LoRA，3goldanswer support EOS编码均值→MLP低秩update，offline autograd1/5/10SGD target蒸馏，推理无backward不等无adaptation/无成本。PopQA/Bamboogle未训练、baseadapter同retrievalcache，HyperTuning同architecture对照支持局部target差；部分LlamaBM25 Bamboogle退，7bench平均非全taskdominance，exactmatch/F1非truth。A10080GB，adapter50–60min、predictor1.5/4/7h、whole50GPUh；3support前向/retrieval/updateinstall、全部离线生成目标费不能隐藏。低秩两个checkpoint差可rank≤2r，预测r是受限近似，主文没有全误差/鲁棒门保证；noisyretrieval未来。具体Ch76 generator-evidence接口适配vsretrieverselection分责待比，不给自动更新许可。

26248 UNSL作者实际v1§2/4–6、App8–10/13–14必要域。6标准：multivariatebrokenpower+additive/reciprocal bottleneck/overfit/hyperparameter对称的可拟合族，不是世界唯一普适规律；训练观察点内再train/val选n/S/λ，holdoutcircle未参与拟合、20seed20kKFACJAX以trainloss选seed。32任务中仅部分优，统计rootstandardlogerror公式是点误差SE变换非跨trainingseed CI，异构既有run/硬件精度不统一，不合并成模型训练收益。100+seed parity与noiseless模拟说明离hyperbreak够近才外推，不保证未观测新regime；same supremalexpressivity不等finitebudget参数量/optimization完全matched。全部数据获得/多fit搜索/误差校准付费，不以更灵活曲线签预算。只拟保有限外推model及validation条件，具体Ch7 owner待reader。

## A21. Belief、curriculum与 world-identifiability 的必要域

26322 OmniToM作者实际v1§3–7/B4。6标准：895stories/22343beliefs七label，extraction vsprovidedgoldbelief labeling两任务非E2E链，全部故事可见非在线信息追踪；truth/access/source属性分责可诊断endpoint掩盖。21storycalibration/ClaudeSonnet4.5标大benchmark/GPT5judge72.03%humanagreement，stage1 overlap83.72是review无reconciliation比例非独立extractor精确F1，Stage2 92.23严格3annotator agreement仅calibration；1K人时不等895全人核。Matchcount>0两向二值并未天然消除所有duplicatecredit，fullschema1step高分不证明真实ToM。A10080GB/按需4bit/~48h每openmodel，closedAPI精度ND，无repeatCI充分；仅有限模型可见belief-statebenchmark，具体Ch66分阶段label/semanticjudge人口待比。

26315 StagedCompetence作者实际v1§4–6/D/F/G必要安全域（不追载荷）。6标准深入：same cleanedGPT4omini选择的DPO pairs，base stochasticreply vsMiniLM256截断safe/unsafecos margin排序，stage3reference更新＋stage内sqrtpool放宽，固定totalsteps但Yi4vs5epochs与sampling重复人口保留。A600048GB/LoRA16qv/max1024/batch32，precision/训练repeat ND；abliterated起点不等完整生产base安全。GPT4omini同时clean/eval可能同偏，rawchosen安全/帮助label不等同，该案例不把所有PKU/HH标签反转当事实。低unsafe logprobteacherforced200轨迹不独立识别deepalignment机制，GCGtransfer对固定旧base优化非adaptive每defense人口。AppendF Yi MMLU63.5→59.4及XS1.2→3.6反退，不能‘能力无损/无过拒’；50%Qwen退，数据省非完整费用/普遍越大越危险。具体Ch34 curriculum/reference与安全gate待比，保实证命题不排除。

26379 LeJEPA identifiability作者实际v1§3–7、AppendB/D/G必要证明/边界。6分理论核心争议：OU jointGaussian同ρ下Hermite线性identifiability条件命题可以限用；一般independent/stationary/additivenoise并不推出m(z)线性OU，非线性保Gaussian测度的m仍可能；AppendB把离散加性噪声直接换continuous-time reversibleconstantdiffusion/SLgenerator，需额外嵌入/正则条件才有Gaussian uniqueness。规划主定理要求cost state-only O(n)invariant+已知pushforward，D1 goal同时旋转/一般LQR矩阵协变不是原state-only不变条件，encoder定理不学action-conditioned dynamics。Lean关键Hermite、polar、pushforward等axiomatized，零sorry不是作者实际构建复现/全premise机器证明。有限合成OU与DMC jointangle trajectory同时违反Gaussian/anisotropy/wrapping，无唯一因果；5seed合成/3seedReacher/30startgoal，hardware/precision此必要域ND，不外推物理控制。拟中心泛化争议暂缓，不把restrictedOU升级真实worldmodel/安全，重开需缩窄准确假设/有效generalconverse与相容controller合同。
## A22. 多语偏好、反事实自省与条件表示的标准层

26293 CroCo作者实际v1§2–5/D/Limit和currentv2必要changedcore。6标准：64candidate/RM withinlanguage排序+selfgeneration DPO与SFT/MaxR对照，EuroLLM9B/aya3B/20k每语，训练lr SFT2e-4 vsDPO5e-6(40倍)与objective共同变，不能唯一归contrastiveness/翻译噪声抵消。offpolicy仅aya→Euro且quality同时变，不证明不论supplier的provenance唯因；online16 vsoffline64只Danish，不授externalRM online必败。currentv2新增Magistraljudge使aya部分语种变负、againstGemma只English趋势，judge差不由mRewardBench平均单项直接废掉负评；该后续验证不倒灌May v1。MI250x8/node、~8000GPUh、vLLM.15/TRL.28/LoRA16qkvo+MLP、precision ND；benchmark3seed不等所有训练多seed与小gain equivalence，翻译/RM/sample/调参全费。具体owner待比。

26355作者实际v1§2–5/T1–2，5标准仅报告倾向。EGA softattention乘sigmoidgate再归一＋learned Gaussian-windowed additive PE，TinyShakespearechar/6layer/≤6M/T256/5ksteps/单seed，两session EGA差.011不能当多seed确认；主联合gain.119局部有意义，但MoPE单独退，jointinteraction不证明非重叠信息/真正spectralenergy。linear w·x非Parseval quadraticenergy，Eq10把pre-softmaxscore乘gate与Eq5 post-softmaxweight乘gate不等价；μσ归一化轴未明，逐j projection自身causal不认证全gate无future。无已核code不宣称实际泄露，也不照录可部署recipe/zero-cost、ALiBi=zerofrequency或uniquegeneralization。只保有限salience/locality组合负正对照，不将物理wavelet类比当模型机制，hardware/precision ND。

26242作者实际currentv2§3–5/Limit与v1§4–6必要原事件差段。6设计反证必要深入：inputembedding probe可以预测LR/PCA/BD label，与randomrelabel及三类input/hidden/control干预提醒binaryreport不能独证独立二阶introspection。BD probe450train vs原ICL30与15splits并非公平样本效率；layer/strength/prompt按复现binary选再250/concept，存在选点/概念大异方差，Gemma持续steering与其他仅prompt不同，不能概括所有模型/所有metacognition无能力。v1 I(t;y)低I(h(t);y)高若fixed deterministich需外生随机干预，否则DPI不容该形式，不采用其generaltest；current弱化定义、不应倒灌为May已无此问题。hardware/precision ND，fullgrid/replay费；具体Ch8/Ch66测量目标owner待比，不从三分类失败推出理论无意识。

26232 UniMVU作者实际v1§3–6/T1–4/6–7与必要setup（大tool输出截断的4.2–4.6正文另补完）。5标准：sharedcontrolsummary、instruction→modalityattention withinstream与acrossstream分两级归一，残差O+βwO只增权不harddrop，absentmask只已支持modalitysubset；恢复instructionembedding不等LLM后层可信隔离。0.5/7B/frozenencoder+LoRA/2H200，单task80/91h、shared81/93h非免费reuse；precision/repeat ND。componentablation仅MusicAVQA，joint多任务容量/数据mix与head共同变，7Bshared部分AV低于PAVE，不由几例attention score证明唯一因果/解释性/原始sensor可信。所有encoder/fusion全tokenattention/门和训练费；局部条件融合实例待reader具体Ch23 NC/Only，不赋任意新模态plugplay能力。

26371 CARL作者实际v1§3–6/A/B、currentv2核心§3–6规范化含表全同，可复用必要域。5标准：近专家offline state-goal与k步actionseq contrastive只是local-dynamics bisimilarity的heuristic，不保证任意action/状态同动力；k内随机goal和全k动作对齐、末尾repeatpad/ humanoidstride4保实现人口。5room toy encoder看过allrooms，不能称全系统unseen；20room4train16test另人口。OGBench8seedstate/4seedpixel/20episode，RTX5000/~4/10h每run/~10kGPUh，precision ND；mainrepresentation10→100共变（附录对照为有限替代，非全task相等），horizon/auxweight equal-effortsweep成本。teleport/visualhumanoid/部分cube负/零，UMAP与nearestneighbors不认证实体排列/组合泛化；只保data-support条件下skillreuse的有限替代，具体Ch26 owner待reader。
## A23. 作者普通必要 Source 收口：最后四项

26519 R3作者实际v1§3–5/C/F/J及currentv2核心changed域（只引文/重复词微调，拟采用机制未变）。6标准：relativepairhead separateR/Tconfidence+boundedbank/novelty/staleness20/cap100，originframe1仍固定、relativeedge不免全球frame/error；c*residual−αlogc的learnedconfidence非校准概率/independent可靠性证。reject需先backbone再删KV，不是无需计算的前置sensor，3calframe/3rejectreset有误拒，bridge3–10需重跑+metricdepth scalar可漂。六48GBGPU/BF16/~110M trainable/372Mmodel/4–32trainviews，specifichardware ND；main noreset1000不授无限stream，J实示eventualdrift、无rawpast重看。target+loss同时变，streamSintelATE略退；fullcontext去causalmask+posegraph非免费同执行，人工distractor10seed非open安全，12–30FPS需绑定实际protocol不采宣传。具体Ch25 relativeobservation/持久geometry owner待reader。

26525 ReCA作者实际v1§3–6/E/F/I/M/Q必要配置及反侧。6标准：frozenvideo G外部anchor/intent/generated provenance＋context-budget slice/structuredrefresh/localrepair，Qwen3.6Plus同时plan/allocate/extract/verifier，q_support/freshness是模型估计/设计评分非观测真值；生成一致性可自我强化，localregenerate后伪代码未显式再refresh不当commit完整性证明。20prompt/80longvideos/46rater至少3每cell，独立model-familyGPT5.5judge非independentGT；sequentialcomponentablation不等独立factorial，未给全重试/每callbudget匹配。Table2 wallminutes ÷平均shotduration恰RTF，不是3–5min整片输出时长，不能授整体18–22%效率；Theta(N/W τG+Dτop)遗漏有依赖leaf生成的DτG下界，Q虽补文字承认也不能把主式当保证。硬件/precision/全部tokenAPI费ND，samebackbone不等同总生成预算；只保有界controller提案，不采实现最优/必然摆脱contextcollapse。具体Ch25生成状态≠外部事实边界待比。

26520 InterSketch补齐作者v1§3.1–3.2/§4.1–4.2，与A11§3.3/4.3/C形成必要完整。5标准：92kproceduralsynthetic＋错误tool参数返回Err不更新图/错误tokenmask、36kRL由8rollout success1/8–7/8筛，Qwen3VL8B/视觉冻结/SFT2epoch32klen/RLgroup8batch128/async15turn32kresponse，hardwareprecision/repeat ND；posthocVLM看before/after解释非真实内推理，筛选排全成功/失败改变人口。GTaction指标与GPT4o GTconditionedsufficiency只训练期证据，Eq7负logprob归一方向/0分母不采用recipe/正确credit保证；SFT/RL/reflection/stepreward都有成本和confounding，不以turn少推速度，TIR51.8对base22.3为29.5pp非“30%relative”且并非全subtask胜。拟仅报告有限监督接口验证，reader必要决定域已核，其余Source配置待其实际收口。

26486 LongCat1.5补齐作者v1§3.1–3.3/§4/§5.1–5.3，与A11§3.4/5.4形成必要完整。5标准：sharedDiT base realscore＋Generator/FakeScore LoRA角色切换只减少同构常驻，不等实测完整VRAM或端到端快；8NFE vs50step×3passes150NFE明确humanlikeness single3.389→3.336/harmony44.2→45反退，stability12.3→4.3为有限取舍，不能‘without sacrifice’。508imageaudio/770crowd13240ratings/10experts，singlemulti不同支持子集、blindAB非全部评价随机独立，母数据curation/Whisper1.5B/perframeRL/multiclip共同变不归一因。hardwareprecision/wholebudget ND，400step停点/1:5G-Fake更新/Whisper时序对齐与所有evaluator费用保留，不采exactGRPO最优或physicalgroundtruth；拟仅报告有限蒸馏角色共享与cost-quality实例，具体owner待reader。

作者必要Source普通剩余0；这**不是**全体候选/Books或DAY完成。独立reader仍需滚动核A20–23具名项、具体NC/Only/争议与确有差额的窄位，再将新增判断融入原六部分。来源A10有界扫描已封；必要资格的跨日/早稿信号和中心争议继续隔离，不把这些或ordinary reader工作混写为Coverage/Evidence通过。

## A24. 六部分合并、早正文重复改判与冻结实测（14:19+08）

原评分对象校正：FEPoID26366、OmniToM26322、Staged26315的初筛均1+2+2=5，A20/A21把审阅投入转述成6是笔误，正式候选恢复原5；深度实际工作有效，不按处置后验降分。ChainCaps26542/AuthGraph26497仍2+3+2=7，跨权限与多生命周期组合的问题未因受限采用变成局部reach。Mobile26546主owner是AGENT-TOOL-CALLING Ch78，不是Ch26（报告生成前已更正）。

26494具体重复披露改判：作者与独立reader均实读[MiniMax-AI官方HF文](https://huggingface.co/blog/MiniMax-AI/forge-scalable-agent-rl-framework-and-algorithm)的Published Feb13,2026与§3.1，head window W=.3N/只取窗口内已完成/窗口外等待/队首消费后推进已逐项相同，§2/3.2相关分责也已见；不是凭旧M2模型名推重复。当前本轮仅拟采用windowFIFO无May新差额，所以改为重复披露关闭，不再列新候选；不声称整篇报告全球first或逐字相同。保留此前Source/已做POST历史，root明确授精确撤本轮Ch31新增单段+本人note，作者实际撤回，reader已唯一完整恢复POST通过，原cluster/其他并发family和交接均保持。

26242 root授Ch66 2603-18280两完整段后/量化自报前的最小反证段与本人注，作者实际保存，reader已实际新增/直接完整两侧/本人注唯一POST通过。因而净真实新I=21：此前21－Forge1＋26242 1；不是21又另计撤回。其余有效20项不重新审阅。最后四项Source/Books仍普通滚动；26486已reader标准Only通过，余26525/26520/26519不预验。

本次确定新增67＝63arxiv+4机构；与旧118合185（此前186口误更正）。已融原六部分；同一单表原118行在前、新67在后。基线实际SHA256 bf481b4f9f311ed94448c1908d658daa6e33d5bed2a60a83e289a1ec5c3137b1，190504 bytes；原118完整行各恰好一次/原序、原小时窗和旧§4连续原块保持。按标题含尾换行切出的完整旧§4是135703 UTF8 bytes（以前135698是不同剥尾口径，不据口径差冒修改）；实际substring为true。同内容原BASELINE及供当前校验器命名识别的[冻结档](./baseline-before-supplement-20261021.md)逐字相同，不新造第二份事实。当前185行、491本地链接零缺失；V3已实跑通过，限定cached/unstaged diff-check通过，但不能替代剩余reader/六节DAY/完成态FINAL。并发staged变化保留，本方未stage/commit/push。

### 日期联合依据的实际精确字段

以下63项均实际核唯一v1、当前事件版本/早稿信号及exact DOI；raw批量DataCite在本目录SUP_datacite_discovered_0…6_20261021.json和SUP_datacite_synonym_0_20261021.json（个别单ID原件同目录），不是把全注册记录当queue。所有列示v1严格在May25 18Z后至May26 18Z前，按2026适用官方公告/发号规则最早界May27 00Z；每项registered为当日02xxZ，且身份client/state吻合，整区间同BJT May27。没有用created/registered/Submitted单项冒公开，也不证明不存在全球更早正文；具名更早稿已另排/保留。

- 2605.26546：[官方事件页](./SUP_26546_abs_20261021.html)唯一v1=Tue, 26 May 2026 04:53:53 UTC；exact DOI registered=2026-05-27T02:11:50Z，client=arxiv.content，state=findable。
- 2605.26542：[官方事件页](./SUP_26542_abs_20261021.html)唯一v1=Tue, 26 May 2026 04:44:59 UTC；exact DOI registered=2026-05-27T02:11:44Z，client=arxiv.content，state=findable。
- 2605.26538：[官方事件页](./SUP_26538_abs_20261021.html)唯一v1=Tue, 26 May 2026 04:39:40 UTC；exact DOI registered=2026-05-27T02:11:38Z，client=arxiv.content，state=findable。
- 2605.26537：[官方事件页](./SUP_26537_abs_20261021.html)唯一v1=Tue, 26 May 2026 04:38:56 UTC；exact DOI registered=2026-05-27T02:11:37Z，client=arxiv.content，state=findable。
- 2605.26526：[官方事件页](./SUP_26526_abs_20261021.html)唯一v1=Tue, 26 May 2026 04:18:42 UTC；exact DOI registered=2026-05-27T02:11:22Z，client=arxiv.content，state=findable。
- 2605.26525：[官方事件页](./SUP_26525_abs_20261021.html)唯一v1=Tue, 26 May 2026 04:16:56 UTC；exact DOI registered=2026-05-27T02:11:21Z，client=arxiv.content，state=findable。
- 2605.26521：[官方事件页](./SUP_26521_abs_20261021.html)唯一v1=Tue, 26 May 2026 04:07:55 UTC；exact DOI registered=2026-05-27T02:11:15Z，client=arxiv.content，state=findable。
- 2605.26520：[官方事件页](./SUP_26520_abs_20261021.html)唯一v1=Tue, 26 May 2026 04:07:49 UTC；exact DOI registered=2026-05-27T02:11:14Z，client=arxiv.content，state=findable。
- 2605.26519：[官方事件页](./SUP_26519_abs_20261021.html)唯一v1=Tue, 26 May 2026 04:03:38 UTC；exact DOI registered=2026-05-27T02:11:13Z，client=arxiv.content，state=findable。
- 2605.26497：[官方事件页](./SUP_26497_abs_20261021.html)唯一v1=Tue, 26 May 2026 03:20:23 UTC；exact DOI registered=2026-05-27T02:10:41Z，client=arxiv.content，state=findable。
- 2605.26496：[官方事件页](./SUP_26496_abs_20261021.html)唯一v1=Tue, 26 May 2026 03:19:04 UTC；exact DOI registered=2026-05-27T02:10:39Z，client=arxiv.content，state=findable。
- 2605.26491：[官方事件页](./SUP_26491_abs_20261021.html)唯一v1=Tue, 26 May 2026 03:09:24 UTC；exact DOI registered=2026-05-27T02:10:28Z，client=arxiv.content，state=findable。
- 2605.26489：[官方事件页](./SUP_26489_abs_20261021.html)唯一v1=Tue, 26 May 2026 03:03:24 UTC；exact DOI registered=2026-05-27T02:10:26Z，client=arxiv.content，state=findable。
- 2605.26486：[官方事件页](./SUP_26486_abs_20261021.html)唯一v1=Tue, 26 May 2026 02:54:12 UTC；exact DOI registered=2026-05-27T02:10:21Z，client=arxiv.content，state=findable。
- 2605.26485：[官方事件页](./SUP_26485_abs_20261021.html)唯一v1=Tue, 26 May 2026 02:49:47 UTC；exact DOI registered=2026-05-27T02:10:20Z，client=arxiv.content，state=findable。
- 2605.26484：[官方事件页](./SUP_26484_abs_20261021.html)唯一v1=Tue, 26 May 2026 02:48:34 UTC；exact DOI registered=2026-05-27T02:10:18Z，client=arxiv.content，state=findable。
- 2605.26478：[官方事件页](./SUP_26478_abs_20261021.html)唯一v1=Tue, 26 May 2026 02:35:08 UTC；exact DOI registered=2026-05-27T02:10:10Z，client=arxiv.content，state=findable。
- 2605.26470：[官方事件页](./SUP_26470_abs_20261021.html)唯一v1=Tue, 26 May 2026 02:27:30 UTC；exact DOI registered=2026-05-27T02:09:58Z，client=arxiv.content，state=findable。
- 2605.26461：[官方事件页](./SUP_26461_abs_20261021.html)唯一v1=Tue, 26 May 2026 02:18:53 UTC；exact DOI registered=2026-05-27T02:09:46Z，client=arxiv.content，state=findable。
- 2605.26460：[官方事件页](./SUP_26460_abs_20261021.html)唯一v1=Tue, 26 May 2026 02:17:29 UTC；exact DOI registered=2026-05-27T02:09:45Z，client=arxiv.content，state=findable。
- 2605.26457：[官方事件页](./SUP_26457_abs_20261021.html)唯一v1=Tue, 26 May 2026 02:12:48 UTC；exact DOI registered=2026-05-27T02:09:41Z，client=arxiv.content，state=findable。
- 2605.26454：[官方事件页](./SUP_26454_abs_20261021.html)唯一v1=Tue, 26 May 2026 02:10:55 UTC；exact DOI registered=2026-05-27T02:09:37Z，client=arxiv.content，state=findable。
- 2605.26449：[官方事件页](./SUP_26449_abs_20261021.html)唯一v1=Tue, 26 May 2026 02:01:11 UTC；exact DOI registered=2026-05-27T02:09:30Z，client=arxiv.content，state=findable。
- 2605.26448：[官方事件页](./SUP_26448_abs_20261021.html)唯一v1=Tue, 26 May 2026 02:01:08 UTC；exact DOI registered=2026-05-27T02:09:28Z，client=arxiv.content，state=findable。
- 2605.26433：[官方事件页](./SUP_26433_abs_20261021.html)唯一v1=Tue, 26 May 2026 01:38:13 UTC；exact DOI registered=2026-05-27T02:09:05Z，client=arxiv.content，state=findable。
- 2605.26431：[官方事件页](./SUP_26431_abs_20261021.html)唯一v1=Tue, 26 May 2026 01:36:41 UTC；exact DOI registered=2026-05-27T02:09:02Z，client=arxiv.content，state=findable。
- 2605.26415：[官方事件页](./SUP_26415_abs_20261021.html)唯一v1=Tue, 26 May 2026 00:45:46 UTC；exact DOI registered=2026-05-27T02:08:40Z，client=arxiv.content，state=findable。
- 2605.26414：[官方事件页](./SUP_26414_abs_20261021.html)唯一v1=Tue, 26 May 2026 00:44:49 UTC；exact DOI registered=2026-05-27T02:08:39Z，client=arxiv.content，state=findable。
- 2605.26403：[官方事件页](./SUP_26403_abs_20261021.html)唯一v1=Tue, 26 May 2026 00:25:12 UTC；exact DOI registered=2026-05-27T02:08:24Z，client=arxiv.content，state=findable。
- 2605.26400：[官方事件页](./SUP_26400_abs_20261021.html)唯一v1=Tue, 26 May 2026 00:08:21 UTC；exact DOI registered=2026-05-27T02:08:20Z，client=arxiv.content，state=findable。
- 2605.26397：[官方事件页](./SUP_26397_abs_20261021.html)唯一v1=Tue, 26 May 2026 00:05:16 UTC；exact DOI registered=2026-05-27T02:08:15Z，client=arxiv.content，state=findable。
- 2605.26394：[官方事件页](./SUP_26394_abs_20261021.html)唯一v1=Mon, 25 May 2026 23:52:15 UTC；exact DOI registered=2026-05-27T02:08:11Z，client=arxiv.content，state=findable。
- 2605.26384：[官方事件页](./SUP_26384_abs_20261021.html)唯一v1=Mon, 25 May 2026 23:14:52 UTC；exact DOI registered=2026-05-27T02:07:57Z，client=arxiv.content，state=findable。
- 2605.26380：[官方事件页](./SUP_26380_abs_20261021.html)唯一v1=Mon, 25 May 2026 23:01:05 UTC；exact DOI registered=2026-05-27T02:07:52Z，client=arxiv.content，state=findable。
- 2605.26379：[官方事件页](./SUP_26379_abs_20261021.html)唯一v1=Mon, 25 May 2026 22:56:26 UTC；exact DOI registered=2026-05-27T02:07:50Z，client=arxiv.content，state=findable。
- 2605.26371：[官方事件页](./SUP_26371_abs_20261021.html)唯一v1=Mon, 25 May 2026 22:39:14 UTC；exact DOI registered=2026-05-27T02:07:39Z，client=arxiv.content，state=findable。
- 2605.26366：[官方事件页](./SUP_26366_abs_20261021.html)唯一v1=Mon, 25 May 2026 22:28:23 UTC；exact DOI registered=2026-05-27T02:07:33Z，client=arxiv.content，state=findable。
- 2605.26365：[官方事件页](./SUP_26365_abs_20261021.html)唯一v1=Mon, 25 May 2026 22:20:52 UTC；exact DOI registered=2026-05-27T02:07:31Z，client=arxiv.content，state=findable。
- 2605.26362：[官方事件页](./SUP_26362_abs_20261021.html)唯一v1=Mon, 25 May 2026 22:08:59 UTC；exact DOI registered=2026-05-27T02:07:27Z，client=arxiv.content，state=findable。
- 2605.26356：[官方事件页](./SUP_26356_abs_20261021.html)唯一v1=Mon, 25 May 2026 22:04:54 UTC；exact DOI registered=2026-05-27T02:07:18Z，client=arxiv.content，state=findable。
- 2605.26355：[官方事件页](./SUP_26355_abs_20261021.html)唯一v1=Mon, 25 May 2026 22:04:31 UTC；exact DOI registered=2026-05-27T02:07:17Z，client=arxiv.content，state=findable。
- 2605.26352：[官方事件页](./SUP_26352_abs_20261021.html)唯一v1=Mon, 25 May 2026 21:56:29 UTC；exact DOI registered=2026-05-27T02:07:13Z，client=arxiv.content，state=findable。
- 2605.26343：[官方事件页](./SUP_26343_abs_20261021.html)唯一v1=Mon, 25 May 2026 21:32:57 UTC；exact DOI registered=2026-05-27T02:07:00Z，client=arxiv.content，state=findable。
- 2605.26339：[官方事件页](./SUP_26339_abs_20261021.html)唯一v1=Mon, 25 May 2026 21:28:46 UTC；exact DOI registered=2026-05-27T02:06:55Z，client=arxiv.content，state=findable。
- 2605.26332：[官方事件页](./SUP_26332_abs_20261021.html)唯一v1=Mon, 25 May 2026 21:11:59 UTC；exact DOI registered=2026-05-27T02:06:45Z，client=arxiv.content，state=findable。
- 2605.26322：[官方事件页](./SUP_26322_abs_20261021.html)唯一v1=Mon, 25 May 2026 20:45:08 UTC；exact DOI registered=2026-05-27T02:06:31Z，client=arxiv.content，state=findable。
- 2605.26321：[官方事件页](./SUP_26321_abs_20261021.html)唯一v1=Mon, 25 May 2026 20:44:17 UTC；exact DOI registered=2026-05-27T02:06:30Z，client=arxiv.content，state=findable。
- 2605.26316：[官方事件页](./SUP_26316_abs_20261021.html)唯一v1=Mon, 25 May 2026 20:13:16 UTC；exact DOI registered=2026-05-27T02:06:23Z，client=arxiv.content，state=findable。
- 2605.26315：[官方事件页](./SUP_26315_abs_20261021.html)唯一v1=Mon, 25 May 2026 20:13:06 UTC；exact DOI registered=2026-05-27T02:06:21Z，client=arxiv.content，state=findable。
- 2605.26302：[官方事件页](./SUP_26302_abs_20261021.html)唯一v1=Mon, 25 May 2026 19:55:12 UTC；exact DOI registered=2026-05-27T02:06:03Z，client=arxiv.content，state=findable。
- 2605.26298：[官方事件页](./SUP_26298_abs_20261021.html)唯一v1=Mon, 25 May 2026 19:51:30 UTC；exact DOI registered=2026-05-27T02:05:57Z，client=arxiv.content，state=findable。
- 2605.26297：[官方事件页](./SUP_26297_abs_20261021.html)唯一v1=Mon, 25 May 2026 19:45:21 UTC；exact DOI registered=2026-05-27T02:05:56Z，client=arxiv.content，state=findable。
- 2605.26293：[官方事件页](./SUP_26293_abs_20261021.html)唯一v1=Mon, 25 May 2026 19:30:45 UTC；exact DOI registered=2026-05-27T02:05:51Z，client=arxiv.content，state=findable。
- 2605.26289：[官方事件页](./SUP_26289_abs_20261021.html)唯一v1=Mon, 25 May 2026 19:27:49 UTC；exact DOI registered=2026-05-27T02:05:45Z，client=arxiv.content，state=findable。
- 2605.26282：[官方事件页](./SUP_26282_abs_20261021.html)唯一v1=Mon, 25 May 2026 19:06:51 UTC；exact DOI registered=2026-05-27T02:05:36Z，client=arxiv.content，state=findable。
- 2605.26275：[官方事件页](./SUP_26275_abs_20261021.html)唯一v1=Mon, 25 May 2026 19:01:10 UTC；exact DOI registered=2026-05-27T02:05:26Z，client=arxiv.content，state=findable。
- 2605.26269：[官方事件页](./SUP_26269_abs_20261021.html)唯一v1=Mon, 25 May 2026 18:53:22 UTC；exact DOI registered=2026-05-27T02:05:17Z，client=arxiv.content，state=findable。
- 2605.26266：[官方事件页](./SUP_26266_abs_20261021.html)唯一v1=Mon, 25 May 2026 18:51:59 UTC；exact DOI registered=2026-05-27T02:05:13Z，client=arxiv.content，state=findable。
- 2605.26252：[官方事件页](./SUP_26252_abs_20261021.html)唯一v1=Mon, 25 May 2026 18:22:42 UTC；exact DOI registered=2026-05-27T02:04:53Z，client=arxiv.content，state=findable。
- 2605.26248：[官方事件页](./SUP_26248_abs_20261021.html)唯一v1=Mon, 25 May 2026 18:15:27 UTC；exact DOI registered=2026-05-27T02:04:48Z，client=arxiv.content，state=findable。
- 2605.26242：[官方事件页](./SUP_26242_abs_20261021.html)唯一v1=Mon, 25 May 2026 18:07:49 UTC；exact DOI registered=2026-05-27T02:04:39Z，client=arxiv.content，state=findable。
- 2605.26232：[官方事件页](./SUP_26232_abs_20261021.html)唯一v1=Mon, 25 May 2026 18:02:20 UTC；exact DOI registered=2026-05-27T02:04:25Z，client=arxiv.content，state=findable。
- 2605.26230：[官方事件页](./SUP_26230_abs_20261021.html)唯一v1=Mon, 25 May 2026 18:01:05 UTC；exact DOI registered=2026-05-27T02:04:22Z，client=arxiv.content，state=findable。

以上日期字段只作本轮可复查的联合约束，不建立额外候选/完成账本。原题/当前v1标题按实际版本保留，尤其26397/26431/26232不能以current rewrite标题替原事件。官方事件页轻量当前修订信号均已核，具体受影响域在逐项Source笔记，后续事实不倒灌May。

## A25. 全部必要层与书稿落实收口，交六节 DAY

末三实际独核已收：26520五分标准Only（Ch78调用边际收益/单片段充分性/生成图来源已有，不固化有限step监督配方）；26525六分标准Only（Ch25 persistent/derivedbank边界下有限language-controller提案，support/allocation无独立资格）；26519六分因pair-relative边/全局融合实际差额深入，root授Mem3R完整两段后最小1段及本人注，作者实际保存，reader完整新增/完整前后/本人注唯一POST通过，窄位释放。

现新增67=22真实Books整合/10具体已有覆盖/29仅报告/6中心争议；22新I覆盖13唯一owner、23正文段（Tax2，其余21各1），均一次真实非writer POST通过。Forge回收已实际恢复POST，未冲销其他有效层。27深入完成/34标准完成/6争议；评分5分20/6分45/7分2。作者与reader Source/具体Books/POST普通剩余0；日级仍待正式DAY及作者保存完成态后有限FINAL，不用本节冒日级通过。

正式六部分已同步全部67处置、自包含22个分层EX（3OpenAI+19arxiv）及六具名修订/早稿信号，明确522非逐项全复核与未检查范围；§5列表空行已修。原118完整行/原序/日期评分和连续旧§4保持，V3/本地引用/限定两层diff继续实测后交DAY，不扩其他日、索引或LS。

## A26. 实际 DAY 通过与作者保存完成态

指定reader已保存R23实际完整六部分DAY通过；不是本作者替代独立判断。作者于2026-10-21T14:37:25+08:00保存README状态‘完成’，同步§1/§5/§6消除普通待办声明，§6实际结论为通过，并保留12资格/6中心争议/来源历史子层的精确隔离，不给正面Coverage/Evidence或Books权限。63个新§4链接已按DAY修正引用标签，去掉错配A数字，原必要原文/采用与反侧未变化。

完成态V3已实际重跑通过，报告与作者SUP限定cached/unstaged diff-check通过；原118整行/有效日期评分/原序、原小时窗和连续含尾旧§4保持。净67新家族/22真实Books整合（13owner、23正文段）/10具体NC/29仅报告/6争议，普通Source/Books/POST0。作者仅保存既成结果，当前交指定reader有限FINAL字段/局部读回，未预写该结果。FINAL只结束该保存态，不新增行政PRE/第三读；未接其他日、不改LS/索引/合同，不stage/commit/push，已有并发index状态保持。
