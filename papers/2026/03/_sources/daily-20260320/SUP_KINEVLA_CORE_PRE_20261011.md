# KineVLA17524：受限双层动作接口 PRE

resume_mar17，2026-10-11，仅03-20补03/19；原2+2+2=6/date准入有效复用批4独核§12。准备不自授Source/PRE/safe/DAY、未写Books。

## 必要实际原证 / 停止

[exact-v1 HTML](https://arxiv.org/html/2603.17524v1)§3.1–3.3/Eq1–7/Alg1 L93–160、§4–5/T1–3 L180–224及A数据身份L256–274已实际读，必要标注例L278–291及316–336。不遍全部示例/引用/附件/代码；图4主成功图只用正文定性，不授像素数值。

粗codebook在第二阶段冻结，细residual stack新训，但共享encoder/decoder继续fine-tune；不由固定码本推出goal表示对执行变化严格不变。生成两层监督text及各自code后拼接解码同一个chunk，非两个独立controller。InfoNCE批内配对相似度是训练proxy，负例context各异，不认证条件MI真值或因果语义解耦。camera-view语言左/右与模拟EEF/实机joint action schema需各自标定。

同视觉与细粒度指令、50Ksteps/batch64/4A100、H=5比较已披露；每task50demo/20trials，3数据集不是全机器人保证。T1随机或错配reasoning干预下降支持受限依赖，不授text忠实或唯一因果；BLEU/BERTScore非控制真值。T2 96ms慢于84/86ms，不当全链latency；precision、推理hardware/batch、deadline、seed/CI与VQ预训练/标注/控制总费未披露。训练阶段共享参数及表示/监督/MI累计消融不能独立证明每部件全域收益。

## 当前具体信号定点

[current v2](https://arxiv.org/html/2603.17524v2)AB L38–40实际新增goal-invariance/execution-predictability两个目标，不称仅改名。必要受影响方法L95–123已实际核，仍见冻结粗码本/共享模块更新；精确两短语在HTML定位只AB及相邻相关论述，未取得目标公式/对应独立评价闭合。本次不采用这两新增强主张或精确新配方，也不把它们写成v1机制。一次定点重开条件：提供当前精确两目标公式、共享encoder/decoder更新下不变性的对象与独立控制评价。可分采v1可核接口，不降分/EX或假整篇NC；未采用主张不认证。

## actual owner / 差额

实际Ch26 action-facing 265–312、Action representation 460–537与25/27交接已必要读。现有GoalVLA阶段zero-padding与StyleVLA连续辅助head/部署token head不承载粗码本冻结+细残差/共享codec继续更新，以及两层文本/动作码合并消费。sole `MULTIMODAL-EMBODIED-VLA`，拟`## Action representation`后/`### 单步 action`前两段；不复制Ch23通用VQ/Ch31InfoNCE算法，不改共享他家段落。

## 两段逐字 PRE（未授权）

同一任务目标还可能规定不同的执行方式：放到同一位置，不代表抓取部位、移动路径或最终朝向可以互换。一条受限表示分支先在普通动作上训练较粗的码本，再固定粗码本和量化器，为细粒度执行示教学另一组残差码；共享 encoder/decoder 仍继续适配，因此固定码本不保证粗层表示或动作函数严格不变。语言模型监督生成目标层与执行层的文本及动作码，最终合并两层码交给同一个 chunk decoder；这里划分的是表示与监督职责，不是给两层各授一个物理 controller，也不由可读文本证明动作忠实。

[有限 KineVLA 对照](https://arxiv.org/html/2603.17524v1)把任务完成与指令中的执行约束分开验收，随机或错配 reasoning 的干预有助于检查这条条件路径，但配对对比损失与文本相似度不认证语义解耦或物理安全。语言方向绑定外部 camera frame，模拟末端 pose 与实机 joint action 又是不同消费坐标；示教/标注、两阶段 codec、额外文本与动作 token、LoRA 及闭环控制均付费，局部 inference time 不能作为 deadline。仅有受限桌面任务证据，严格 goal-invariance、当前新增目标配方和跨本体无损不采用。标定、约束遵守或预算不合格时，保留原单层码或直接 action policy、短 chunk 重新观测与可靠 controller，不用目标已完成掩盖执行方式错误。<!-- source-family:SF-2026-ARXIV-2603-17524 -->

静态源注拟文：KineVLA exact-v1 §3–5/Eq1–7/Alg1/T1–3与A必要数据口径；只双层codec/监督text-action接口与goal/执行分验。冻结码本非函数不变、相似度非真值、受限干预与速度/全费边界保留；current-v2新增强目标不采，未核代码/复现。

## 窄写 / 作者实际回读

2026-10-11，reader独核§19必要Source/actualowner/原两literalPRE/static有限PASS，root授Ch26本family窄锁。resume_mar17实际顺读当前Action representation周围477–505后按原两PRE写新486/488及唯一静态注2248；写后完整477–513前后链与末6本人/HeiSD/FASTER邻注回读，原单步/chunk/goal-padding论点未改。共享codec更新非函数不变、camera frame与action坐标、current新增强目标隔离及全费/退路近文准确，静态注不写流程身份。限定git diff --check通过，待非writer实际POST，不自行计safe或DAY。
