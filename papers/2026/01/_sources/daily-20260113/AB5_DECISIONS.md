# Jan13 有界题摘补检判断（待非作者校准）

恢复补注：下表为最初准入提案，不替代正式日报终处置。05707与05930已按决定性机制恢复准入，故实际贡献前关闭为六项05548/05746/05874/05890/05899/05960；55完整题摘中49论文继续处理，不因Books已覆盖或本日工作量缩池。GIFT经AppendixB.2实际核为平均reward而非AND，原机制主张被收窄、原评分保持，正式README记录OnlyReport终裁。各项最新Evidence/Books与非作者范围只维护在本日README。

AB5.jsonl 的23份完整v1题摘已实际读取，不把122宽题名或跨日队列作为分母。以下是贡献判断，尚须具体公开归属；潜在项不是Evidence/Books通过。原字段来源与查询、停止见本日STOP及原记录。

## 继续定点核验的具体增量

| ID | 原约束 → 实际增量 → 待重考虑选择 | 初拟分数 |
| --- | --- | --- |
| 05461 RECOR | 独立会话/单跳检索评价 → 同一会话的历史与推理对照、隐式桥接失效切片 → 是否用静态检索指标替代多轮信息支持；不收录benchmark规模本身 | 2+1+2=5 |
| 05465 PRISMA | 终局轨迹credit难定位检索模块错误 → observation-aware residual更新Inspector的分阶段分支 → recovery策略和模块更新人口是否应分离；新残差公式需核心核，不把五角色编排当新原理 | 2+2+2=6 |
| 05549 TMRL | 语义与时间检索在统一短向量中竞争 → nested表示的时间子空间 → 截断预算是否会删掉时间可达性；适用增量限representation分账 | 2+1+2=5 |
| 05606 Conformity | 独立多样性被交互后的高置信共识替代 → 拓扑与self/social权重的wrong-but-sure反证 → 是否把更多连接/收敛当可靠性改善 | 3+1+2=6；设计反证深入相关内容 |
| 05633 GIFT | 混合任务奖励易允许单技能补偿 → 顺序任务合成AND reward → multi-objective课程是否保持原效用；不从游戏名称推出一般智能 | 2+1+2=5 |
| 05705 Logic-Parametric NLI | 固定logic silently约束可证明集合 → logic作为显式参数并比较axiom与internal formalism → verifier证明权限须绑定logic而非统一真值 | 2+2+2=6 |
| 05787 BEPA | 静态专家轨迹与learner可达性不一致 → self-roll reachable支持+按任务动态缓存 → off/on-policy指导人口与refresh成本 | 2+2+2=6 |
| 05808 EnvScaler | LLM模拟反馈未必可执行且人工sandbox难扩 → programmatic state与rule-based trajectory check → synthetic环境事实权限与验证范围；代码生成成功不等真实环境等价 | 2+2+2=6 |
| 05877 iReasoner | 只奖最终一致缺少中间信号 → trajectory internal-agreement proxy → 无gold自训练的agreement与truth是否分账 | 2+1+2=5 |
| 05903 HAPS | 请求级model选择忽略所选模型的参数配置 → 联合architecture/config搜索与共享参数生成 → 路由artifact是否含实际配置；参数含义/新机制待核心核 | 2+1+2=5 |
| 05905 NCB | point-wise self-consistency掩盖情境脆弱性 → conceptual-neighborhood干扰反证 → confidence测试应否包含语义邻域；不授internal belief真值 | 3+1+2=6；设计反证深入相关内容 |
| 05918 Deanonymizer | 去除显式身份字段仍有跨文本链接 → tool-enabled公开采访重识别案例 → 发布富文本需评估组合线索而非仅PII删除 | 3+1+2=6；隐私相关范围深入 |
| 06022 AdaFuse | 固定融合粒度在异构decode间错配 → 动态unit和不确定状态下额外候选分支 → alignment/granularity与实际搜索成本 | 2+2+2=6 |
| 05572 Multi-image | 多来源视觉token身份混淆 → learnable separator与sinusoidal image index → 表示身份如何支持变输入数；效果需保留有限生成/训练边界 | 2+1+2=5 |
| 05466 iMIST | 单turn过滤或tool表面格式被视为安全 → progressive tool-disguised攻击 → 跨turn工具内容与执行权限须独立；不按jailbreak标签授全安全威胁 | 3+1+2=6；安全相关范围深入 |

## 贡献前关闭（不是学术否定或日期归属已核）

- 05548 KEEM：题摘给的是生成式整合memory的情绪/事实dataset；没有明确新更新算法、冲突检测或可验证状态contract，不能把用户记忆主题当机制增量。
- 05707 Low-resource ASR：未见语言MICL、cross-lingual适配和acoustic hypothesis选择是当前题摘给出的受限应用；attention偏好只是关联，未提出改变通用fusion/ICL设计判断的明确新机制或反证。不是因为语言/小模型本身而排除。
- 05746 DynaDebate：路径生成角色、过程批评、工具裁决是题摘已有的设计组合；未披露新的diversity/verification机制或可迁移失效边界，不能把角色名改成control术语后准入。
- 05874 Continual Low-resource：POS code-switch与replay adapter的语言适配组合，未给新的遗忘条件或更新目标；不因包含continual learning而retain。
- 05890 StackPlanner：协调/执行分层、task与experience memory、检索和RL是题摘中成熟分工组合；缺少明确新memory-control或credit规则，不因hierarchical状态命名准入。
- 05899 TowerMind：新增轻量RTS环境、观测格式和五级benchmark；当前题摘的planning/action失效是任务级表现，未建立新的evaluation混杂或长期机制。并非排除所有环境研究。
- 05930 Predict ML Agents：当前题摘以数据分析报告、偏好预测和predict-then-verify改进ML任务收敛；不把world-model类比或速度headline当新的执行验证机制，尚无明确改变当前主线contract的增量。AI for Science当前暂缓，不由此绕行。
- 05960 Memory-as-a-Tool：把临时feedback写成file guidelines并由agent检索的熟悉分支；题摘没有新memory可置信更新、检索或执行机制，有限rubric上成本对照不自动改写系统判断。

## 独立准入校准结果

jan01_v3 已独立读取23份完整题摘：15项潜在增量准入理由通过，但尚未确认公开归属，也未授Evidence/Books。8项关闭中，05548、05874、05899、05960的具体增量不足理由通过；05746的adaptive redundancy、05890的active task-memory在题摘中尚未给出新操作或有效性条件，按这一具体边界关闭，而非仅因使用成熟组件。

05707与05930重开一次决定性方法核：前者须核unseen-language MICL如何进入hypothesis selection以及是否改变适用边界；后者须核预测代理执行与真实运行验证的人口/调用合同，不能仅因ML应用或World Model类比排除。原关闭提案不再作为最终判断；不因这些两项重扫其他材料。

独立复核若发现共同错误理由，只重开受影响项；日期、必要证据与Books按原分逐项推进，不能为省时间降分或把材料访问受阻变成贡献排除。
