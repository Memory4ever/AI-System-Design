# 2025-09-05 作者筛选冻结

窗口：2025-09-04T09:00:00+08:00 ～ 2025-09-05T09:00:00+08:00。实际检查2026-10-06；只本日独立发现，未继承跨日候选或Weekly。

## 有限入口与分母

`capture.py`保留四条ROADMAP主题表达：model architecture/training/attention、LLM/GPU inference/communication/kernel、multimodal foundation/world/VLA、LLM agent/retrieval/memory/safety。API submittedDate=[202509031800 TO 202509041800]仅用于发现，不当公开窗口；每条max100、asc第一页，实际39+19+20+48=126原始命中→103独立题名。原86可能相关/含糊项读取精确v1完整题摘（`exact-v1.raw`），独审仅定点重开3个题名（`exact-title-reopen-v1.raw`）全题摘：最终89=68潜力+21关闭。其余14只读题名范围外，不是14篇摘要已审，也不是全文队列。原始响应不得称当天126新论文。

官方另4家族完成核心准入：Anthropic biorisk正式1，OpenAI opportunity/DeepMind DeepLoopShaping/Moonshot K2-0905关闭3。合计93个完整题摘或官方核心筛选家族=正式1+68 arXiv潜力日期保留+24关闭。必要核心44 arXiv+Anthropic1已定点实际读，见NECESSARY_CORE；不是89/93 FullEvidence，潜力也不是默认全文/Books队列。

当前metadata轻核原86及补3的官方comment，发现并定点核06996/04104。补3 current仅19305 comment IJCNN2025，04169v2无comment、10526v1无comment，不把版本变化自动当重要修订。撤回版本只留排除链。68日期保留均未评分，均不能作正面证据/Books/覆盖保证；首公开精确事件证据恢复后才决定是否归本窗和相应审阅。

## 68项arXiv潜力（不是正式候选）

下列ID均为2509.*v1，只有itinerary为2510.24719v1。原题名/完整摘要/原submitted字段在`exact-v1.raw`，可由`inspect.py exact-v1:0-85`复查；该字段不是公告时刻。具体核心风险以NECESSARY_CORE优先，未读core的只保留摘要提出的潜力，不采用实验宣传。

| 精确v1 ID | 原约束→原件增量→待核设计问题 |
| --- | --- |
| 03581 | 固定always/never plan→动态plan/token成本→长程任务规划预算边界 |
| 03615 | 通用OCR vs专用pipeline→同图任务/CPU资源反侧→准确性/端侧资源不能单指标代替 |
| 03626 | 图扰动解释→局部surrogate/稳定性与faithfulness指标→解释真值需另验 |
| 03636 | world model任务评价→SCM观察/干预/反事实能力切片→预测准确不等因果控制 |
| 03646 | 统一token奖励→策略ngram层级credit→既有procedure foundation成立条件 |
| 03647 | evaluator去偏steering→非法偏好修正却合法票不稳→去偏/评价真实性分离 |
| 03695 | 多模态/task federated modules及fog/D2D配置→组件任务/资源协作→异构模型部署接口 |
| 03696 | row/column展示偏差→LLM propensity与IPS→布局/离线ranking对照条件 |
| 03730 | persona自报→受控行为任务弱/不一致→问卷变化不等行为人格 |
| 03733 | 不可微结构熵→soft range entropy/attention结构训练→margin与复杂度前提 |
| 03736 | persona表面一致→深层对话coherence测试→人口属性差异是否保持 |
| 03740 | 全CLIP参数适应→固定SVD bases改singular values→低参数表示调节接口 |
| 03746 | 推荐item串多token→item-ID单token生成→生成表示/服务代价取舍 |
| 03764 | judge与human偏差→校准/扩query评价→判别最小差异与评估方差 |
| 03768 | safety条款被topk挤出→独立index预算/hardclamp→槽位覆盖不等实际合规 |
| 03787 | RAG只看relevance→helpful/harmful池及query framing控制→证据组成/安全可靠性 |
| 03800 | 3D医疗全局特征不足→local/global alignment及semantic bank→跨模态预训练接口 |
| 03803 | prompt特征共性混杂→shared/class特征分解与swap→可执行表示组合非已证因果 |
| 03805 | 图文grounding好≠合作好→selfplay与guess-sharing控制→协调评价盲区 |
| 03809 | 单步翻译对齐/遗漏→align-then-slide与chunk指标训练→一多映射约束 |
| 03817 | 单一response policy→Persist/Refine/Concede与SoftRankPO→反思/让步选择机制 |
| 03828 | 合法catalog ID≠对语义→MCP对照validity100%仍错误12/142→provenance/semantic分离 |
| 03850 | 量化和DA选择各自优化→CMI选择与QAT/KD组合→表示选择指标/资源取舍 |
| 03867 | 字面推理benchmark遗漏语用→Drivel文化/叙事约束→评价边界与judge限制 |
| 03887 | scene动态状态混合→scale/spatial与temporal/pose分解→world representation接口 |
| 03888 | ID probe98%→clean/OOD触发词反侧→安全信号shortcut与迁移 |
| 03891 | mobile任务信息跨app→外部/内部/记忆检索接口→Agent上下文状态协作 |
| 03895 | fixed image embedding→dual online attention类别/局部全局→training-free适应接口 |
| 03918 | MTQA thought路径/树中层冗余→column/cell双轴communication及fact correction→多路径reasoning信息路径 |
| 03934 | RAG SFT遗忘→input-logit KL/response NLL分位置→不replay的保留/成本条件 |
| 03940 | text角色评价忽略声音→prosody/persona benchmark→speech表达/一致性评价 |
| 03956 | 推理只靠静态知识→world prototype检索与中间alignment→test-time知识注入 |
| 03985 | 安全方向图不能单授机制→SNIP/投影/实际break与局部finetune→可视归因的验证边界 |
| 03990 | Agent经验自由复用→外部failure predicates与约束验证→train/update/deploy的责任分界 |
| 04011 | entity embedding仅底层→mid-layer value vectors对比投影→typed实体表示接口 |
| 04018 | VLA动作直接执行→gripper关键帧监督/离散修正/历史融合→监督覆盖和延迟边界 |
| 04027 | CoT长度简单更多更好→loss/空间/复杂度理论→假设和risk上界不能授真实U形 |
| 04059 | 纯文本reasoning掩盖视觉入口→sheet-music图文对照/训练→跨模态评价混杂 |
| 04063 | reward-guided flow固定重权→自适应权重收益/方差→正态近似成立条件 |
| 04154 | attention启发式加权→线性SDE filter近似→结构/算量/对角化前提 |
| 04183 | 多agent精神健康synthetic数据→MAGneT协作与rubric→生成数据/评价接口，非真实隐私疗效 |
| 04185 | NTP串行因子化→set-block/NTP-MATP/exact-prefixKV→分布等价与并行效率区别 |
| 04198 | computer use替代RPA→相同局部流程成功/时延反侧→适应开发成本与可靠性 |
| 04213 | learned dynamics接新传感器困难→foundation dynamics+UKF观测融合→无需重训的观测接口 |
| 04243 | GUI感知不确定→MonteCarlo/IoU偏好active perception→感知预算/执行选择 |
| 04292 | 普通IFEval隐含训练格式→逆习惯指令排名反侧→一致偏好不等真实follow能力 |
| 04304 | 当前事实问题不显过时知识→review变更old/new金标→事实更新与pretraining归因边界 |
| 04310 | 固定emotion persona→MDP自适应情绪policy→交互feedback/策略目标边界 |
| 04334 | 静态geolocation leaderboard→GeoArena人类pairwise/in-the-wild→污染/现实评价接口 |
| 04343 | 人格提示是否影响行为含糊→NONE/EXPERT固定协议行为对照→局部message/action差非真实人格 |
| 04373 | 性别bias指标不一致→salience/instruction/probability vs discrete切片→分母/测量盲区 |
| 04377 | token级KV压缩改kernel/layout→PagedEviction block约束→在paging边界复用已有runtime |
| 04403 | 单模态安全输入不代表组合安全→image-oriented RMS+跨数据judge→隐蔽风险/生成judge混杂 |
| 04419 | SFT/RL目标割裂→UPG行为分布KL及verifier switch→换测度/support与surrogate边界 |
| 04439 | 固定经验memory限制解题→ArcMemo抽象/检索更新→重复任务的memory生命周期 |
| 04442 | posttrain状态难解释→base/delta activation mixture表示→训练变化的可读分解 |
| 04448 | fake-news模型图文路径弱→query-aware visual amplifier及reasoning数据→多模态表示选择，非CoT真实性 |
| 04534 | 较高bit应较稳→4/8bit任务/延迟非单调反侧→memory/质量/latency分离 |
| 05359 | speech token/scale默认泛迁移→encoder/离散化/domain组合对照→语音表示成立条件 |
| 05360 | 幻觉判断缺结构信号→ngram张量奇异特征/MLP→检测表示接口 |
| 05362 | scambait自动化utility vs privacy→FedAvg/噪声/guard强度→模拟指标非DP/真实诈骗安全 |
| 05367 | 伦理顺从提示安全→多轮dilemma攻击与失败边界→安全评价局部反侧 |
| 05378 | ICD端到端分数掩盖抽取失败→gold spans/检索与rare code分解→评价/部署覆盖区别 |
| 09700 | 单layer probe/无条件DoLa→cross-layer attention/alternative/abstain→coverage/正确率与OOD范围 |
| 12221 | learned harmful方向干预→router/orthogonal rank1命题→逐样本CEgap/routing错配假设 |
| 2510.24719 | itinerary prompt看似有效→确定约束/修改/重验→文本行程≠真实可执行旅程 |
| 10526 | 层局部观察/连续prune ratio→全拓扑GAT+binary channel mask/CMDP→模型压缩资源选择（补精确题摘/必要核心） |
| 19305 | time-only轨迹diffusion低频偏移→DWT分带+STFT cross-frequency条件→生成分布/轨迹稳定取舍（补精确题摘/必要核心） |

## 21项arXiv关闭

| v1 ID | 完整题摘或决定准入的实际核心理由 |
| --- | --- |
| 04324 | OVGrasp把开放词汇VLM、intent融合和exoskeleton接入；15objects/10participants成绩未新增接口成立条件/可归因控制边界 |
| 03793 | SAMVAD角色、RAG、计划/评估的法律模拟配方，没有新执行或可靠性机制 |
| 04139 | query expansion/summary/BERT soft prompt组合，仅领域retrieval指标，无新成立条件 |
| 03893 | VLM pseudo-parts与dense pixel contrastive做correspondence；没有新增foundation接口或受控泛化反证 |
| 03827 | policy选择与既有ABM社会模拟，未给模型系统的新机制/评价盲区 |
| 03995 | recursive TKGQA+multipath聚合、Hits改进，没有新控制/故障成立条件 |
| 03903 | DiT text/mask/box chest-Xray数据与分数，只领域数据配方，不引科学应用回主线 |
| 04162 | FPGA综述归纳既有部署取舍，未给原创新控制或实测失效边界 |
| 07996 | world-model综述分类既有方法，未给新的受控评价盲区/机制条件 |
| 03871 | trust/reasoning综述截止June30的组织与总结，无新增原始反侧或成立条件 |
| 03890 | FaMA工具和流程声称98%/2x，未新增执行契约、条件或可归因机制 |
| 03962 | Italian/Ladin翻译/filter/backtranslation新资源与指标，未新增模型机制条件 |
| 04152 | TAGAL迭代agentic表格合成/feedback已有流程组合，只数据成绩不够准入 |
| 03972 | LlamaPro/MSG与balance102B MoAI采用既有方法，未披露新控制条件 |
| 03658 | 已有PCA16D/diffusion/scene表示配方，sparse route增加未来信息未隔离；root定点核心认可，不按车辆/小模型排除 |
| 04549 | §5–6概述既有ROME近正交/线性条件，illustrative实验非新增证明/机制；root核心认可 |
| 04537 | 共享GPT4o/prompt/memory群体行为模拟没有分离所宣称pretraining内在动机，未新模型接口/受控反侧 |
| 04250 | 临床Bayes adverse-event超先验/患者trial设计科学应用，未改变模型形成/LLM系统评价/Infra；作者/独审发现，root完整题摘FIRST认可 |
| 06996 | current官方arXiv Admin撤回article；旧v1仍可下载不授有效候选，保留原始排除依据，不声称全实验虚假 |
| 04104 | 精确v1因许可权利withdrawn；current v2 November恢复VoR不是当窗版本，不删除有效later家族 |
| 04169 | 补完整v1题摘：classification LiRA适配与DTS forecasting攻击，LSTM/NHiTS user/record MIA和horizon/population趋势；echo LLM是类比，未给可迁移模型系统条件或新privacy-unit机制，root FIRST认可贡献关闭；不是原题名泛标签关闭 |

## 14项只读题名的范围外停止

03653 sensing-network GPU、03666 microgrid RL、03741 gaze dashboard、03939 Ethereum图fraud、03961 remote-sensing fusion、04066教育Arabic chatbot概览、04077叙事领域分类、04153 CNN FPGA review、04173车辆detector hardware综述、04180 annotation工具、04277 elastic rods GPU、04362 parking temporal predictor、05363 SAS科学应用、25198 SELFIES分子diffusion：题名已有所得对象/方法主线范围差，无LLM/foundation/system桥线索；只记题名范围外，不凭此宣称已读其摘要或全学科覆盖。原10526/19305/04169按genericNN/普通RL/timeseries的题名关闭不足，经独审反例只重开这3完整题摘；两恢复、一具体贡献关闭，不扩其余14。

## 官方4家族

- [Anthropic biorisk](https://www.anthropic.com/research/biorisk)：评价proxy/现实能力差与precautionary ASL3有具体LLM安全measurement贡献，非科学应用。独审发现正文article:published_time/JSON-LD datePublished/visible time dateTime一致2025-09-05T00:00Z，root实际独核认可08:00BJT当窗事件，正式1、2+2+2=6，安全判断深入受影响内容。dateModified2026-07-08另列当前版本，未授所有现存文字冻结2025；root亲读Ch66/72实际proxy/outcome、refusal/uplift、治理/有效性分离正文后，仅报告：本篇受限案例未披露新classifier机制，无Books改动。
- [OpenAI opportunity](https://openai.com/index/expanding-economic-opportunity-with-ai/)：完整官方文章/RSS09-04T11:30Z，jobs/certifications/workforce计划，不新增LLM机制或发布安全合同，关闭。
- [DeepLoopShaping](https://deepmind.google/research/publications/145314/)及[博客](https://deepmind.google/blog/using-ai-to-perceive-the-universe-in-greater-depth/)：RL频域reward控制LIGO噪声，科学应用且无foundation系统桥，关闭。
- [Kimi K2-0905](https://platform.kimi.com/blog/posts/kimi-k2-0905)：context/速度及tokenEnforcer输出格式是产品API事实，未披露新的constrained decoding机制/兼容失败边界，关闭；root FIRST要求不能借成熟原则给新增机制高分。

## 日期保留与独立权限

submitted不等公开。合法`catchup` cs.CL/cs.CV+date2025-09-05+include_abs=True真实HTTP400正文明确过去90天限制（`catchup-cl/cv.raw`）；原日期型list400与month archive404不能单独授90天理由，月表尝试不变成全月研究。缺精确公告/当时v1冻结，68arXiv潜力均不拟定本窗正式候选，晚ID06996等已另排撤回；09700/12221/2510.24719/10526/19305等尤其不按submitted字段移动日期。Anthropic先前仅配置日期hold已被具体出版字段新证据撤销，不继承旧hold。

root FIRST仅记录实际已核范围：20题摘（14关闭+03658/04343/03828/04534/04537等必要信号以其消息定义）+8潜力；后续04343/03658/04549定点核心、04250完整题摘、04534/03828限定改判和两撤回状态。它不替代全部潜力的DAY。作者读过所有86完整题摘，未自授独立通过。

后续root实际独核Anthropic全文/出版字段/Books；以及本日reopen原件三个完整v1摘要，认可10526/19305恢复、04169按具体主线条件关闭。作者实际追加3题摘+2必要核心，最终89题摘，不把仅下载04169 HTML404当外部必要正文受阻或已读核心。
