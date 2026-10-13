# Generative3D RL18532：必要Source/date/actual sole owner/PRE

resume_mar18准备；仅本03-21补BJT03-20，原65完整AB/root准入校准复用。尚未非preparer Source/PRE，无锁未写、不计safe/DAY。

## 身份/增量/拟评分

[official exact-v1](https://arxiv.org/abs/2603.18532v1)完整原题摘/currentheader/history实际核，四作者Andrew Choi/Xinjie Wang/Zhizhong Su/Wei Xu；v1Submitted03/19T06:22:11Z。官方cached页latestv3 Sep21，真实[DataCite](https://api.datacite.org/dois/10.48550/arXiv.2603.18532)当前version4含Sep29 v4，不能将后来标题/方法投射March或为version号遍历diff。所见页无明确withdraw/correction/accepted先稿信号；仅采用exactv1。DOI statefindable/created与registered03/20T02:14:52Z、v1Updated03/20T00:37:37Z、Available仅2026-03，沿本批官方公开日/DOI夹证限定BJT20 arXiv事件，不冒精确公告或其他地方从未先公开。

窄人工scene易高训练成功却覆盖不足→生成环境扩大场景分布，在固定批量下训练内拟合与留出成功反向变化→scene数量与训练内成功不能独立决定迁移配置。拟2+2+2=6，仅这项受限训练分布—动作部署边界，不给成熟domain randomization、借来的ReinFlow/PPO或局部成功数字重复新分。

## 必要原证/评价/直接反侧

实际[exact-v1 HTML](https://arxiv.org/html/2603.18532v1)§3 L79–107/Eqs1–7；§4 L108–165（包括可读完整Table2）、§5限制L166–172；A L227–280/训练和randomization/成功谓词，B L281–298/TableB1，C L299–320/TableC1与残余失败。不读所有100scene目录、定性rollout/代码、无关foundation候选或后版本。

- §3：GPT4o task→background/context/distractors/manipulationtarget/robot及ON/IN scenegraph，EmbodiedGen/ManiSkill3构造交互scene；GPT4o QA/几何一致性筛选只是proposal过滤，不是校准物理证书。C在所有自动检查之后仍只有85%人工检查可直接使用，剩余scale/initialplacement/unstable对象失败；自动缩物体适配74mm夹爪与降mesh分辨率又改变任务/接触支持。不能采“无人工干预自动全合法”。
- π0来自第三方BridgeV2 checkpoint；VLM LoRA+actionexpert全调、noise/value heads也训练，8 RTX6000 Ada/5days。生成scene库100；三种随机50scene子集，各N1/3/10/25/50取固定顺序首N训练，各有三run；complement50为对应OOD，full100只有一run。每scene100episodes；不是无限世界、独立全部scene组合或所有task泛化。
- §4文字明确固定batch/mini-batch下N增大使每scene采样约1/N，训练成功下降而complement OOD和另一SE场景表现改善；不能把高训练成功当宽域配置优者。N与对象/背景/任务实例共同变化，只支持受测采样方案的breadth取舍，不认证特定scene语义因果或普遍单调最优。主文把50集合H_i称training scenes，但N<50时它还包含未训练实例，故不照抄精确“ID94.3→78.9”或全列分类。
- HTML Table1仅nicematrix-placeholder，未恢复原行/颜色分母。officialPDF web超体积、三次有限真实GET timeout所得部分PDF无法解析，未称实际读Table1；本PRE不采该表精确ID/OOD/TF或独立单调数值。§4正文的训练内与留出定性分账、可读Table2/B1/C1已支持拟采用有限命题；若后来需要准确表列/数字，须定点恢复Table1而非扩大附件，当前不把无关精确数字缺失列必要外部阻塞。
- 实机只比较πpre与N100，12scene×两policy各10trial=240，不包含N1/3/10/25/50的实机多样性消融。21.7→75成功同时改变RL、K10→1、VLM/actionhead及随机化与控制条件，不能全归scene多样性。DFR/SFR非互斥，不能sum成完整失败分布；Table2 scene3 TF6.1→12.2、scene6 7.8→11.1反退，不用均值证明全部更快。TF成功条件分母/少成功任务未披露统一规则，性能仍局部。
- sim-real同时依赖生成质量、domain randomization及gravitycompensation/PD controller；多数targetpose低trackingerror是作者实测条件，不授无需sysid/未随机delay普遍安全。这里只pick-place，articulated/tool/multistage明确futurework。
- A在VLM冻结下collapse、s=.2用于power-scaled likelihood ratio的经验稳定，Eq6非原生importance ratio，不采用unbiased PPO或稳定保证。B的K1优于K2/4仅单run、约2–2.5points；Gaussian策略不采“所有RL不需multimodality”，0.073s compiled forward不等全部闭环deadline。控制5Hz/C4本身不签传感→执行尾延迟。
- C顺序RTX4090从头生成46.8±5min/scene、旧asset库复用约2min只是不同资产起点；含QA/retry平均1.37acceptedasset，不能遗漏被拒/人工修正/生成API、8GPU训练和实机采集/标定/controller费用，也不采论文“有效无限数据/最低人工”完整账单。未核实现/复现/全图像点值。

## Actual sole owner和具体差额

sole `MULTIMODAL-EMBODIED-VLA`/[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)。实际完整809–824列sim-real gap和general domainrandomization，820已有simulationbreadth+realcalibration组合，并未承载固定scene采样预算下训练内成功与留出泛化反向排序；原822是冻结statebase后真实residual分支，共存而非取代。另实际1538–1553生成环境版本资产/validator/物理authority已覆盖，不为scenegraph或QA名强造新段。Ch25/27开篇实际读，生成环境不是预测transition本体或一般dataquota。拟soleCh26 820完整后/822真实residual前一段，以breadth验收取舍为新增；不在Ch25或Ch33重复density/PPO基础。

## 一段literal PRE（待非准备者）

扩大模拟分布还需要把训练内拟合与留出泛化分开，而不是按训练成功率选择场景数量。[一项受限生成场景对照](https://arxiv.org/html/2603.18532v1)从任务描述构造对象与空间关系，生成可交互环境并过滤部分无效配置，再以固定 batch 和 mini-batch 在不同数量场景上更新同一预训练 VLA；场景变多使每个场景获得的样本变少，训练成功降低，却改善了受测留出集合的成功。这提供的是给定任务、采样和预算下的 breadth—拟合取舍，不是所有场景越多越好，也不把自动 QA 批准为真实接触或安全真值。实机只比较未适配模型与完整场景集适配模型，同时改变 RL、生成步数和参数更新，不能把全部实机提升归因于多样性；少量拾放任务之外的关节、工具和长流程仍未验证，部分任务完成时间也退步。场景与对象生成、失败重试和人工修正、训练、随机化、标定、真实试验及 controller 都付费，资产库复用的分钟数不等从零生成或端到端成本。应同时冻结环境资产、训练采样方案、留出人口与控制配置，分别验训练内适配、模拟留出和真实任务；生成分布、接触或 tracking 支持失配时，保留人工冻结场景、真实校准与保守 controller，不用高训练成功或更广模拟库代替物理闭环。<!-- source-family:SF-2026-ARXIV-2603-18532 -->

静态注：- `SF-2026-ARXIV-2603-18532`：[exact-v1](https://arxiv.org/html/2603.18532v1)必要§3–5/Eqs1–8、Table2与A/B/TableB1/C/TableC1；仅固定采样预算的scene breadth/训练内拟合/留出泛化分账，不采HTML缺失Table1精确列值或全列单调，也不把实机pre-vs-full对照归因单一多样性。保QA后残余失败/scale与controller条件、K/参数更新混杂、时间反退、有限拾放与全部生成/人工/训练/实机费用；未核代码/全部scene图像/复现或安全。

请root非preparer最低充分核日期/支持命题/直接反侧/actualowner/PRE；未自授锁或safe/DAY。

## 非准备者必要 Source / actual owner / PRE（2026-10-12）

root 实际核 exact-v1 §4 训练人口、固定 batch/mini-batch 的每场景采样稀释、训练成功与留出结果区别，Table2 的完整任务/两policy接口与直接时间反退；原数据人口和 v1 日期夹证复用有效记录。这里只采正文明确的受测 breadth—拟合取舍，不把缺行 Table1 的精确数值、所谓所有 ID 或单调最优当已核。实机仅 pre-vs-full，同时改变优化和采样，不能证明 scene 多样性单一归因；QA、有限任务、控制与完整费用限制近文保留。支持与直接反侧足够该有限命题即停止，不为不采用的数字重取大 PDF。

实际 Ch26 803–832 完整 sim-to-real / domain randomization / real residual 交接已核，当前通用 breadth 段缺固定采样下训练与留出验收反向排序。one literal/static 有具体差额且与原证相容，必要 Source/owner/PRE PASS，6分保持。授 resume_mar18 sole Ch26 在通用 simulation breadth 完整段后、real residual 前窄写 one PRE 与本人注；须与另一天 Ch26 写者串行协调，写后 root 一次实际 POST，不预授 I/DAY。

## 非写入者实际 POST（2026-10-12）

root 实际顺读 Ch26 810–837、再次核819–832完整局部和本人末注：one literal/static 与批准稿一致，通用 randomization/breadth 与后续真实 residual 的成立条件均保留。训练内适配与留出泛化分验、实机优化/采样混杂、有限任务、时间反退和全费用在机制附近，没有把更广模拟库、QA 或训练成功率升级为接触真值或安全。Giga 的另日有效新增及末注未覆盖。必要原证有效裁决复用；实际 POST **PASS**，root 接纳该 family 为实际整合并释放 Ch26 窄锁，未授整日 DAY。

## 作者实际窄写（待非 writer POST）

root确认03-20 Giga的Ch26锁释放后，明确授权本family原one PRE/static；先前“两段”消息口误已定点更正，未扩写。resume_mar18按原literal实际落实Ch26新824、本人静态注2266；作者顺读完整803–835及末9行，原PRE/静态注逐字相同、限定diff-check0。保存通用breadth与真实residual两侧及Giga原正文/注，不改其他family。已交root一次nonwriter实际POST，当前尚不计safe/I/DAY。
