# VectorWorld17652：初始化历史与按需场景补齐 / 必要准备

resume_mar17，2026-10-12，仅03-20补03-19。原2+2+2=6与本日独核§30准入/day复用；不将Submitted当公开日。不自授Source/PRE、safe或DAY，不写Books/LS。只拟采用policy输入资格与保留旧tile的补齐接口，不展开全附件、代码、版本史或新发现。

## 1. 实际必要原证与停止

[exact-v1](https://arxiv.org/html/2603.17652v1)完整AB/current同四作者单v1轻量说明已实际核；§3.1–3.6/Eq1–10 L248–386、§4/T1–3与直接解释/影响L387–453实际读。拟采用命题需要的A3 mask/A4 motion code L692–702、A10 filters L836–840、A12/Alg2 L916–962、A13/T7 L963–991、A14.1–2/T8–9 L992–1038、A14.4/T11–12 L1063–1107、A14.5–6/T13–15 L1108–1172、A15.4 timing L1211–1221与A16限制L1239–1252实际定点读。部分请求连带返回邻表/参考文献/TOC，不授全1268行或所有图像/附录/证明；两次anchor只回首页后改精确line恢复必要段。支持与关键反侧够即停，未核artifact、复现或全部像素。

## 2. 真实接口与不能跨的桥

生成64m×64m lane/agent异质vector-graph tile，agent static state为[x,y,speed,cosθ,sinθ,length,width]，另有type与body-frame短运动polyline。数据历史经当前SE(2)逆变换、按最近弧长截断/重采样，static阈值可置零；motion-aware sigmoid gate融合static/motion embedding进入Gaussian VAE。生成后的motion code在初始化确定性展开为pseudo-history填NPC policy context；这是合成初始化上下文，不是观测到的真实前史，也不是已证明所有policy输入落训练分布。A4保持body-frame motion code、只对static/lane做tile全局变换的接口明确；不采用未给出的完整pseudo-history时间插值recipe。

接近边界触发下一tile补齐：encode当前/边界条件，clamp已存在latent，采frontier，decode/merge/stitch后推进ego planner与NPC；A3 True明确条件token固定、目标零velocity/noise。已有tile来自生成场景，不因被叫observed就变真实世界观测；latent固定不证decode后所有几何/拓扑自动严格不变。Edge-conditioned logit bias/value gate是学习关系路径，不是硬图合法性validator。Interval MeanFlow支持有限少步选择，JVP/时间参数的完整精确配方与通用理论不采用，不能把一step等同所有CFG/backend只有一次forward。

ΔSim的finite k-disk token另加continuous residual，Eq9只按token kinematic cost减logit，DKAL使centered logits与cost对齐。有限soft penalty不能把不合法token概率严格置零，residual也可能改变最终运动；A16明示极端动作无strict feasibility。A10另有lane去重/compaction、碰撞/offroad agent删除等deterministic filters；这些改生成/评价人口，不能把最终validity独归attention或MeanFlow，filter费用也不能消失。仅sandbox simulation，不直接部署真实车辆。

## 3. 关键对照、反侧与全费用

Waymo/nuPlan有限评价，T1 nuPlan FD .98差于ScenDream-L .67，T8多项JSD/topology退，不采全面保真改善。T9 snapshot→concat降低init collision但staticL1 .012→.017；门控支持局部接口取舍。Gated与ours两行四个布尔开关同为✓却指标不同，未披露差额，不授唯一gate因果或精确recipe。T2 online cold/warm同1000m rows jerk16.6→9.6、success47.6→51.4、offroad6.9→7.0；§4.2却称42→78，不能引用该success宣传或照录所有项改善。T2短200m与长1000m不同人口不能直并。

T11 full one-step480GPUh与FM320GPUh、T12一step5.6ms/EPD.269 vs12step31ms/.110，速度以质量和额外训练换取；不采无损一step。A14.6真实有200m跨backend评价，不说全无独立backend，但训练同100k episodes的GPUh分别64/480/160，不能称同总预算；1km panel只VectorWorld本backend，不能据其声称开放真实交通迁移或所有长期稳定。T13 hybrid去DKAL比discrete-only ADE低而latacc5.5→12.5，full residual物理违规仍非零，精度不等可行性。

H20训练FP32，VAE8GPU/60ksteps、generator8GPU/100k、NPC4GPU/10k；GPU同步tile计时只latent sampling+一次VAEdecode，排data loading及optional filters，不含整闭环的planner/NPC、re-encode、stitch、状态管理或实际effect。CFG两支、JVP训练与选择均计费。完整runtime硬件/precision/batch/concurrency、tail deadline、seed/CI、filters分母和完整训练/运行总费在拟采用范围Not Disclosed，不采≈6ms整闭环保证。A16缺curb/boundary/细traffic semantics、one-step marginal gap/extreme maneuvers必须近文保留。

## 4. actual唯一owner与两literal PRE

sole `MULTIMODAL-WORLD-MODELS`，[Ch25](../../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)。实际完整737–800的causal streaming/historybank、945–1005 evaluation/tradeoff与1067–1134 persistent-state/feedback邻接已读，Ch24/26入口也实际读。现1095 point-cache/1101 state累错未具体承载**合成motion code填下游policy前史**与**固定旧graph latent只补frontier再进入reactive simulation**；不是因worldmodel主题就必写。拟1101完整后/GT cycle-feedback前两段，Root同章若另family插入只顺读新邻接定位，不改它们。通用MeanFlow归Ch24、真实action controller归Ch26，不复制其推导。

场景生成还要满足下游 policy 的输入形状，而不只生成一张合理快照。若 reactive policy 消费短运动历史，可让每个 agent 的静态状态另带 body-frame motion code，由门控融合进入场景 VAE；初始化时再把生成的 code 展开为短 pseudo-history 填入 policy context。这改变的是模拟器的冷启动接口，不是恢复真实过去。[受限向量场景分支](https://arxiv.org/html/2603.17652v1)还在接近 tile 边界时保留已有 graph latent，只采样 frontier，再解码、拼接供 ego planner 与 NPC 推进；已有生成场景与新补齐都仍是 simulator state，不能因作为下一轮条件而获得真实 observation authority。<!-- source-family:SF-2026-ARXIV-2603-17652 -->

这个分支把历史资格、场景结构和行为可行性分开验收：运动门控与关系 attention 是学习路径，latent clamping 不保证所有解码几何严格不变，有限 kinematic logit penalty 与连续 residual 也不是硬物理 gate。原系统另有去重、碰撞/offroad过滤，中心线表示遗漏部分道路约束；少步生成仍有质量退步，长 horizon 碰撞和违规未归零。Tile 计时只覆盖采样与一次 decode，不含加载、可选过滤和整个控制闭环，VAE、JVP训练、CFG、NPC与状态拼接均付费。初始化、seam或行为支持失配时，保留记录历史、可信日志/显式 simulator、较短 rollout和独立可行性检查；sandbox里的局部迁移不能签发真实车辆安全或fresh-control deadline。<!-- source-family:SF-2026-ARXIV-2603-17652 -->

静态源注：

- `SF-2026-ARXIV-2603-17652` — [VectorWorld exact-v1](https://arxiv.org/html/2603.17652v1)必要§3/Eq1–10、§4/T1–3、A3–4/A10/A12–13/T7、A14相关T8–15、A15.4/A16。仅motion-code合成初始化与保旧latent的frontier补齐接口；保伪历史非观察、soft penalty/residual/filters、表文冲突与质量反退、表示遗漏和计时/全费边界。不采完整MeanFlow/行为recipe、唯一因果、物理安全或整闭环实时保证，未核代码/全部像素或复现。

## 5. 待非准备者裁

交resume_review17_18有限必要Source/actualowner/原两literal与static裁；非准备者可改判更小差额/具体NC或中心隔离，但不因工作量改变原6。尚未Books授权或实写，不计I/safe/DAY。

## 6. 授权后的实际 writer 回读

reader独核§47有限Source/actualsole/原两literal及static PASS后，root实际packet/当前Ch25邻接读回并授sole窄锁。作者仅两literal写当前1107/1109，静态本人1779；写前1095–1140、写后1097–1135和1771–1779本人/邻注完整回读。持久状态错误→合成policy前史/frontier→GT cycle训练反馈衔接成立，未改EVA/TAPESTRY或其他正文。原两literal/static逐字写入，章numstat68/0→74/0仅本family六新增行，限定diffcheck0。未授nonwriter POST、safe或DAY，交reader一次实际完整局部和本人静态注POST。
