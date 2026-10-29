# A113 — AgentJet04484首次必要 / 正式6分 / actual Ch33具体NC提案

仅本日Jun04补窗；R89–91完整题摘/准入/精确v1 Jun04联合日证有效复用，不第三。D²SD R111–112唯一actualPOST已实际读回并行政采用，新增I23＋旧Kimi1合24，本人注/Source/Report同步后V3先通过，不第三技术。AgentJet必要/正式6分/actual Ch33四组具体NC已由R113–114首次独核通过并行政采用，NC4→5、I24不变；无需Book/本人注/PRE-POST，不第三技术。

## 原件与真正读取域

`2606.04484v1`题名 *AgentJet: A Flexible Swarm Training Framework for Agentic Reinforcement Learning*，不是Jul21 v2/当前月页的Distributed题名。Submitted-v1 `2026-06-03T06:02:52Z`，exactDOI findable/arxiv.content registered `2026-06-04T01:59:40.000Z`；最早Jun04 08:00BJT至最晚09:59:40BJT完整同日，R89–91通过。原abs/notice/字段在SUP_TITLE_STOP_BATCH4_20261025.md，未见撤回/纠正信号的原层复用。

官方HTML `https://arxiv.org/html/2606.04484v1` GET200/488035bytes，原件SUP_2606.04484v1_20261025.html，SHA256 `69c7df833178b03779453b1fa9084c199b31db6d376f2768700e31391f16dbef`。实际读§1、§3.1–3.4.2/Eq1/Alg1/F1–5说明、§4、§5.1–5.4/T1–3/F7–10说明及§7结论。§2只是作者相关工作陈述不代他源已核；不展开§6自动研究/附录A/B完整prompt、图曲线像素、repo/代码/训练/复现，不采用其自动研究自主性或全部能力宣传。所采贡献仅episode→call evidence→timeline训练消费的身份接口，支持与直接反侧足即止。

## 必要支持与直接反侧

§3.1–3.2：server留model/optimizer/inference和sample pool（当前verl-based），clients运行env/agent/reward；controller client供配置启动server由Booting→Rolling。每参与server先注册episode取得server-specific及episode-specific BaseURL/APIKey，将请求路由本episode tracker；完成后交reward才进样本池，abort/timeout不等有效样本。多server各训练自己的policy，不自动使合作episode成为跨server原子事务或一致checkpoint；APIKey编码episode路由不是完整鉴权/隔离证明。客户端热替换减少任务runtime影响，不证明服务/网络/恶意client/optimizer故障均不丢进度。

§3.3 C1计完整episode B×N、C2计至少N repeats的task达B、C3再要求reward非零variance，C4/C5等all/any active client同意；这些是采样/触发人口，不保证组完整、无偏或“可靠gradient”。触发后Rolling_Post拒新claim并drain在途，再Weight_Syncing优化并向inference同步后回Rolling；“异步trigger”不等更新时任意旧episode跨版本继续或无策略滞后。未给完整lease/重试幂等/跨servercommit/版本日志及active-client失联规则，不补exactly-once恢复或全原子热更新。

§3.4.2每call timeline是message blocks数组，每块含text m、tokens x、author llm/env/user、逐token oldlogprob ℓ与loss mask μ。Alg1逆序扫描，较晚timeline可吸收与其前缀全部匹配的较短timeline，非前缀的branch不自动合并；较短块若标llm而较长标非llm，复制author/tokens/logprob。**打印Alg1没有显式同步μ**，与正文“保LLM生成token mask”要求存在接口缺口，不替作者补实现或宣布梯度保持。重复样本缩减还可能改变token/trajectory权重和reward/advantage归属，没有objective等价证明。

token模式逐块token-id严格match；默认text模式只要求text相同，Fig5 Qwen3 chat-template在新assistant轮追加后剥离旧thinking，文本仍同而token数组变。原文明确text合并以TI consistency换效率；这不只是无害tokenization drift，原behavior conditioning/坐标和loss支持均需恢复，不能把重tokenize概率当原采样概率。token相同也不足单独证明model/policy/template/历史、role/mask、reward与版本相同。算法仍可能在不一致的旧块上迁移logprob，本文只保反侧和需验的训练身份，不采“默认text合并自动无损”。

§5.4/F8只两组AppWorld前25训练步、其余条件声称相同：actor-update2160±171→346±13秒/约6.25x；LLM calls11.4±.7 vs12.6±1.0，reward曲线近似。误差条人口/独立seed CI、精确硬件/模型/precision及完整训练计时未充分披露，不能由曲线接近证梯度等价/行为无损，也不是rollout+tool+capture+merge全链6.25x，摘要1.5–10x不作为通用收益。

§5.3 Qwen3-8B GRPO单8GPU、每步16AppWorld+16AIME/group8，对各单任务每步32、共同163步：AppWorld specialist .68 vs混合.58，AIME均.73 vs.72/后20步.80 vs.75；混合各任务样本量少，未隔离梯度干扰，不把作者直觉解释当因果。单通用checkpoint/少run是资源取舍而非全部任务质量保持/总预算必省。§5.2三14B-LoRA vs单shared14B差1.8point还改参数量/LoRA/训练布局、未CI，不归唯一行为多样性。§5.4 F10四framework单次曲线/三个heldout集合末step90差.025，不授所有agent/协议/工具语义透明；“100步/final90”保原口径，不补标准化版本和重复运行。

故采用范围为服务端不可变call evidence与合并predicate/训练身份的具体边界，不采用成熟client/server解耦首创、所有外部故障无影响、任意多模型并行正确、自动研究可靠或全流程加速。采集/存储、tokenization/merge、环境/rollout、weightsync及被丢样本均付费；失配应隔离受影响timeline、保逐call/原始token更新和同步完整episode，不能靠更快actor backward免质量验收。

## 正式评分

Design Delta2＋System Reach2＋Durability2＝6：具体增量是opaque agent调用被重建为可训练timeline时，prefix合并谓词/author转交与behavior token/logprob/mask身份的约束及默认text合并反例，跨采样—训练边界；会改变“文本相同便能安全共享训练前缀”及只看actor speedup的选择。不按成熟client/server、框架名、能映owner或自动研究宣传加分。贡献通过不因Books已覆盖排除/降分；受影响训练身份足够深入，不扩整系统/附件。

## actual owner具体已有覆盖（拟NC，待首次reader）

唯一owner `TRAIN-GRPO` Ch33的trajectory lifecycle，而非拟改Ch32：实际打开后Ch33已有专门black-box capture/reconstruction组，比PPO迭代通用mask告警更直接。邻Ch32 iteration ordering/oldlogprob与mask及Ch34目标边界按实际owner交接读；另Ch31 numerical-TI段只作跨章责任对照，不另建owner。

1. **Ch33:1811–1841，从允许异步到lifecycle invariant/版本窗口。** Reserve→完成rollout/reward后Occupy→buffer资格→完整batch Consume→abort/retry/timeout退休；coordinator不拥有越gate权，版本组/behavior logprob一起绑定。已实际承载AgentJet episode完成入池、Rolling_Post drain与更新同步需验的边界；不需另加“clients可以替换”术语或C1–5产品列表，亦不由其声明无故障授新保证。
2. **Ch33:1961–1973，Typed Trajectory/Hierarchy of Groups。** 完整history/behavior-policy identity属于trajectory store，group builder冻结可审计membership，state相似不伪同分布；已有明确过粗/过细/variance与原trajectory/critic退路。具体承载C1计episode vsC2/3计task与混合任务/role比较人口不能互代，非泛说“有分组”。
3. **Ch33:2359–2403，Opaque Harness→Trajectory Tree完整组。** model-serving proxy保存exact input/output tokens及rollout logprob、longest-prefix reconstruction、共享prefix只计一次；harness消费text而trainer必须消费原sampling tokens，重格式化后重tokenize不得冒原轨迹。trainer拥有mask/advantage/update而proxy只拥有call evidence；绑定proxy/tokenizer/policy/harness及branch lineage，TI/credit/fullcost和whitebox退路齐全。直接覆盖AgentJet默认text等同但tokens变、author/ℓ转交而μ未显式同步与不证objective等价这一采用判断；具体算法缺口留Source反侧，不为每个打印伪代码遗漏造书稿diff。
4. **Ch33:2329–2357 partial rollout与2405起Cross-Policy reuse组。** 明确历史tokens/behavior logprob、恢复/重采角色和真实采样分母，源/目标tokenizer不同不等逐token ratio；token同名或checkpoint同名不能保原概率坐标。另Ch32:393–409完整迭代顺序和Ch31:604–609数值执行身份均已承载mask/oldprob不可重算的相邻接口，交接明确，不把同一知识再复制Ch32。

以上四组已实际读正文/完整直接语境，不按marker或主题近似签NC；同family未见既成Source链故本次首次必要仍做完。R113–114首次独核已确认必要/6分/actualowner具体已有覆盖，无新增正文/注/PRE/POST/I；Ch31数值身份现行行号为614–620，原604行号仅历史定位，不改变所读命题。后两Batch4及两cue/finite stop/DAY ordinary，不预日验；State/index/他日未改，无stage/commit/push。
