# 2026-01-02：四项新补线索的必要证据与 owner 提案

作者：jan02_new_evidence。检查时间：2026-10-07 14:02～14:11 +08:00。

范围仅 `2512.24985v1 / 2512.25073v1 / 2512.24762v1 / 2512.24965v1`；原104家族、日期、评分和有效审阅保持不动。四项完整题摘准入已由root校准；本文件完成相应最低标准审阅，并对具体Books差额定点加深，不把能映射owner或已有通用原则计入评分。未遍历无关附件、比较后续revision、运行代码或复现实验；未改README、Books、Learning State，未stage/commit/push。

## 身份、日期与轻量事件说明

四项均未出现在本日原104候选表。精确abs与HTML均已打开；HTML页头均标明对应v1，未使用latest正文。现有官方abs页面没有撤回、删除、勘误或具名安全警告；DarkEQA已有v2～v4、GaMO/OpenOneRec各有v2，仅版本号不触发比较；ShowUI仅v1。没有因后续版本出现而给v1静默升级权限。

公开日复用 `audit_jan02_dates` 的本轮独立窄核：v1提交下界落Dec30 14ET之后、Dec31 14ET之前；官方[ID规则](https://info.arxiv.org/help/arxiv_identifier.html)的announcement分配月份与[availability的不backdate规则](https://info.arxiv.org/help/availability.html)，联合[2025年末假期公告](https://blog.arxiv.org/2025/11/21/temporary-changes-to-announcement-schedule-due-to-end-of-year-holidays-2025/)，支持这四个2512身份的arXiv v1日级公开归属为北京时间 **2026-01-01**。这是规则联合推断，不是Submitted=公开、不是每篇精确公开时刻，也不声称家族全网最早时间已考古。本次所读v1正文没有作者显式更早同正文公开日期信号；未据此扩查全网。新项按补充自然日窗口处理，旧材料不搬移。

| 材料 | 新增且拟由证据支持的命题与评分 | 实际审阅 | 建议Books处置（待root非作者核） |
| --- | --- | --- | --- |
| [DarkEQA v1](https://arxiv.org/html/2512.24985v1) | 只调暗post-ISP图像不足评价低光链；RAW噪声、ISP与增强改变输入身份，QA收益须按支路/严重度分账；2+2+2=6 | 标准完成；具体输入处理链差额定点深入 | 整合提案：`PLATFORM-EVALUATION-SYSTEM` Ch66 clean/fault slice邻接；不采用真实sensor因果隔离 |
| [GaMO v1](https://arxiv.org/html/2512.25073v1) | sparse views补支持可固定pose扩FOV而非增加新pose；几何条件、同噪声mask混合与生成监督分工不同；2+2+2=6 | 标准完成；固定pose/condition与生成-重建差额定点深入 | 整合提案：`MULTIMODAL-GENERATIVE-PARADIGMS` Ch24相机生成/重建交接；不授未知几何真值 |
| [OpenOneRec v1](https://arxiv.org/html/2512.24762v1) | 扩词表后的通用语言preservation需决定学生新token如何进入旧teacher监督；显式惩罚/截断不同于discard或text-only重归一；2+2+2=6 | 标准完成；具体支持域与阶段反侧定点深入 | 整合提案：`TRAIN-SFT` Ch29扩输出词表保护原语言分布节；不授无偏KL或完全恢复 |
| [ShowUI-pi v1](https://arxiv.org/html/2512.24965v1) | GUI tool的gesture不能总当start/end原子动作；连续坐标+按键状态、短chunk执行/再观察形成不同消费接口；2+2+2=6 | 标准完成；动作schema、re-observation与replay环境差额定点深入 | 整合提案：`AGENT-TOOL-CALLING` Ch78 Tool Contract后；不授真实OS任意闭环/物理控制 |

四项DD=2各对应明确替代机制或评价边界，未用榜单提升授DD=3；SR=2只计实际跨输入/模型/消费或训练/评价边界，未把联想的全生命周期算3；Durability=2是可复用的有条件接口，而非已经成立的长期基础定律。

## 1. DarkEQA：低光 stimulus 必须带处理链身份

**必要原源位置。** 精确v1 §III-A1 Eq1～3；§III-A2 Eq4～5及Unprocessing/Noise formation/Simplified ISP；Fig2；§III-B/C Algorithm1；§IV-A/B/C、Table I；§V限制。核心已读，不仅摘要。

**原有约束→实际增量。** 从HM3D-Sem渲染sRGB得到可重复输入，便宜的noise-free支路做gamma 2.2线性化、`2^-ΔEV`缩放、再gamma编码。另一支路反tone-map/white-balance/color-correction并提取Bayer RAW，注入shot、Tukey-lambda read、row、quantization噪声，再以简化ISP重建sRGB并施加EV drop。shot分支先降光子数再ISO放大，最后亮度与EV可以分开控制。这使“同样暗”不再等于同一输入噪声/ISP条件；增量不是夜间新场景名称。

**直接边界/反侧。** 两支不仅相差noise开关：noise-free走线性RGB gamma路径，physics-motivated还走随机颜色矩阵、增益、mosaic/demosaic等。故跨支差不能全部唯一归于传感器噪声；原文未给同一unprocess/ISP内仅开关noise的完整因果对照。其RAW是从渲染sRGB推得，不是真实RAW采集；§V明确real-to-sim与详细因果分析未解决。52 scenes/3911 frames/~9.4k QA，五类multiple-choice exact-match静态perceptual primitives；不含导航policy闭环、全机器人任务或24/7生产验收。rule-based QA避免VLM生成标签依赖，不证明原HM3D数据绝无污染、无先验捷径或所有房间语义真值。

**评价/收益/代价。** Table I的Qwen3-VL-8B噪声支路L1：68.51→DarkIR增强64.27，L5：42.79→62.16；增强在不同严重度有反向效应，不是普遍增益。noise-free L1亦非所有模型下降，不照录“所有下降”绝对话。blind GPT4与GPT4o是不同模型，只作语言prior/reference，不是同模型视觉消融。Fig6阴影是跨模型min/max，不是随机seed置信区间。LLIE额外推理成本未作端到端测量；VLM硬件/precision/batch/解码预算与传感器逐级noise校准系数在必要正文中Not Disclosed，不推断SLO或真实相机故障概率。代码/数据v1承诺acceptance后release，未核artifact，不称已开源可复现。

**具体owner差额。** 已读[Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)“Clean Ranking、故障切片与可信度任务必须分账”（当前约725～739）及“Stored Label要追溯到Execution、Request与Stimulus”（约4346～4350），并核Ch65/67交接；Ch23当前约18～34拥有preprocess/representation identity。前两处已覆盖故障切片与通用provenance，**尚未承载低光EV/RAW/ISP不同路径混杂与增强须按severity配对的具体输入界限**；不以抽象主题称已有覆盖。

**建议窄写入。** 在Ch66 clean/fault slices后合并一段：post-ISP调暗适合廉价曝光压力，但不能代理全部低光噪声；若用RAW unprocessing与ISP重新渲染，应保存两支完整处理链、噪声与严重度身份，逐级比较原输入/增强后的同QA，而不把不同处理路径的差唯一归因于noise。DarkIR的受限反向结果说明视觉增强不自动批准下游QA；新增合成/标注/增强成本，真实sensor不匹配或归因不足时保留clean/EV-only基线与真实相机定点评价，明确Unknown。这里“应控制同ISP路径”是我们的评价设计推断，不宣称作者已做。只链接Ch23，RAW表示机制不在Ch66重复推导。

## 2. GaMO：固定 pose 扩 FOV 是新支持分支，不是几何证书

**必要原源位置。** v1 §4.1 Eq4、§4.2 Eq5～7/Alg1、§4.3 Eq8～9；§5.1～5.3 Tables1～4；§6 Limitations；必要Appendix B（mask执行）、C Tables5～6（3/6/9输入）、F Table8（只改intrinsics的multi-view对照）、G Table9（完整runtime）、H（遮挡失效）。未遍历无关可视化附件。

**机制。** DUSt3R point cloud→训练coarse 3DGS；同pose缩焦距`f'=0.6f`扩FOV，opacity `<0.6`产生补全mask。Plücker rays同时更新新intrinsics，RGB/CCM unproject/reproject到目标平面，再把downscaled原图放中心；生成条件不是“同pose”一句话。去噪35/25/15阶段将coarse latent加到同noise level，再按mask与生成latent混合；mask dilation逐渐收缩，R=3次re-noise/denoise给边界再修正机会。最终以原图和outpainted proposal交替监督3DGS，后者附LPIPS。无backbone finetuning **不等于整个pipeline无训练**：coarse 10k iterations及最终3k/7k refinement仍执行。

**受限支持与反侧。** 6-view Replica/ScanNet++ Table1质量局部改善；AppendixF中SEVA/MVGenMaster仅改intrinsics后训练3DGS还可低于原3DGS，支持“缩焦距本身不够”。Table3每step blending可较高PSNR却更慢且模糊，控制频率是取舍；Table4去LPIPS行PSNR25.14高于全配置24.93，不把所有模块都称全指标有益。3-view Replica本法PSNR23.81低于GuidedVD24.22（SSIM/LPIPS较好）。ScanNet++ 3/9视图人工选最大coverage，区别6-view协议。coarse误差能经mask进入生成/再训练，opacity不是geometry confidence真值；§6/H明确所有输入均遮挡、view clustered/misaligned会失败。未知区域被多视图一致地生成仍非真实geometry、persistent world state或action consequence证据。

**成本配置。** AppendixG只给本法Replica_6/office_2、6 images、512×384、单RTX4090：coarse118s、outpaint93s、refine280s，总491s。Table5/6给其他场景/方法时间，但未完整披露所有baseline等硬件/precision的独立预算匹配；25×是作者pipeline比较，不是diffusion硬件通用速度。precision/batch/concurrency/SLO及多seed不确定性Not Disclosed；输出序列/LLM长度不适用该离线图像重建任务。没有实跑artifact。

**owner与窄提案。** 已读[Ch24](../../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)现有相机条件/生成关键view→重建→dense render（约1439～1449）以及camera/depth阶段交接（1452～1460），并读Ch23/25相邻owner边界。已有生成proposal不是三维真值，但**尚未解释同extrinsics改intrinsics的FOV支持替代及同noise-level coarse latent/mask写入**。建议在生成关键视图/3DGS交接前新增相邻两段：保留new-pose扩大视角覆盖的合理旧路；当目标是原视野边缘而非换角度时，可固定pose扩FOV，把ray/CCM与中心原输入绑定新intrinsics，再以匹配噪声的coarse proposal约束生成，独立重建/geometry评价决定接受。新增coarse训练、重采样与refinement费用，完全遮挡或coarse不可靠时回真实新视角/直接几何基线，不声称fixed-pose inherently保证真实一致。

## 3. OpenOneRec：旧 teacher 不支持的新 token 不能靠丢样本掩盖

**必要原源位置。** v1 §4.1/4.2（数据混合、itemic embedding/output行先训再全参）；§5.1～5.3 Eq6～9；§3.3/3.5及§6.1；§6.4.1 Table9、§6.4.2 Tables10～12；§7限制；必要B.4 Tables13～14（不采精确mix百分比，理由如下）。不审全部八任务附件或所有Amazon表。

**实际新增分支。** 从post-trained Qwen3继承参数，新增3层8192代码空间的itemic tokens，先只训练新增embedding/必要output行，再全参co-pretrain混通用文本；混合SFT后用同scale原Qwen3 teacher做general-domain on-policy distillation。teacher没有学生扩词表的itemic坐标：§5.2并非只discard含新token的trajectory，而是在首次itemic token给teacher极小log-prob（例-1e9）并截断后缀，用clip负KL反馈，同时较高temperature探索；最后推荐Hit reward的GRPO参照蒸馏后checkpoint。该分支明确规定不支持坐标如何反馈，比“都是co-training”有具体增量。

**权限限制。** Eq6～7为作者sampled/per-token KL及clipped reward recipe，不用未明的clip阈值/gradient estimator声明无偏全词表KL或稳定收敛；teacher极小概率是训练目标选择，不是新token本身语义错误的真值。§5.2丢样本可能增加itemic概率/崩溃是作者报告，未提供独立discard/penalty充分消融，不授惩罚/截断唯一因果。只限制general-domain prompt输出新token，不禁止推荐任务合法itemic输出。

**直接评价与反侧。** Tables10/11仅该8B thinking/no-thinking、七项general benchmark的分阶段结果：thinking IFEVAL .6174→.7653（OPD），仍低于Qwen3 .8577；Rec-RL后.7634，不是完全恢复。Table12 Interactive .3461→.2419→.3458，恢复语言的阶段会损失推荐，最终仍未超过SFT该项；Label Pred/Item Understanding也非全阶段单调。no_think阶段部分分数高伴随实际违反tag产生CoT，不能只读分数认能力保持。Table9 alignment若干8B指标不升，不能照录“所有scale必要”。§7承认数据mix最优未决、CoT收益有限。B.4 Table13含类别subtotal、行weights与token budget不一致，故不发布精确通用/推荐混比或compute-optimal预算；4.3 loss-based scaling fit不自动认证能力scaling。judge/reference部分来自Gemini而非独立真实偏好；训练硬件/precision/batch、teacher/student全部预算与benchmark解码token预算在所读必要正文中Not Disclosed，不授26.8%普适迁移/生产可靠性。

**owner差额与窄提案。** 已读[Ch29](../../../../../books/part-04-training-system/29-sft.md)约422～446 Teacher/Student occupancy及“扩展输出词表时单独保护原语言分布”，并核Ch28/30交接。现有SpeakGR分支在原text词表**重归一并只采text**、forward KL保护旧语言；**没有说明保留扩词表rollout时，旧teacher不支持token的显式反馈/截断与discard population选择不同**。建议在该节内作替代分支一段，避免新建推荐专章：保留现有text-only路径的简洁；若需要主动识别general prompt误激活新token，可保留该动作在样本中的失败信号，并显式给教师无支持坐标定义惩罚/终止语义，不把样本直接扔掉后称相同目标。截断与clip改变credit/目标，附独立general-task与专用任务阶段回归、额外teacher/rollout成本；分布失配或双目标退步时保留text-only保护、普通mix/replay或专用模型。只用Table10～12支持取舍，不采用无偏/崩溃避免保证，也不把全部能力保持归因于此单组件。

## 4. ShowUI-pi：GUI gesture 中的再观察边界不能被 endpoint schema 隐藏

**必要原源位置。** v1 §3.1～3.3 Eq2～4；§4.1/4.2/4.3 Eq5～8及Fig5/6；§5 Tables1～7；必要A.2/3（跨benchmark与mixed training反侧）；B.1/2（训练配置）；C.3（replay）；D(i)/(ii)（tool能力限制）；E（planner未来工作）。不穷尽八类失败可视化或下载视频。

**动作与condition机制。** SmolVLA-450M结构、SmolVLM-2 backbone+16层flow action expert；上一action state投回VLM，当前screenshot/instruction与生成的短action chunk交替消费。输出`(x,y,m)`的坐标与mouse down/up：click是同点down/up，drag是press-hold途径后up。原式坐标不是已证明的relative Δx/Δy；flow积分变量s不是wall-clock或环境重新截图频率。预测H动作与下一观察前执行E个动作是两个参数，Table3比较H=10/20、E=1/2/5；E大时更长无反馈区间，不能把预测整chunk当无条件原子gesture。

**不采用的保证。** §4.3 Eq7明确cosine对象写为预测/GT point；它不自动等于位移方向一致、平移不变或cursor动态稳定证明。m的连续采样到合法二值状态的执行细节未完整披露，因此只采用统一schema与condition分工，不给无条件合法动作或精确部署recipe。

**评测身份与反侧。** 20k training trajectories；test505=每域101，五域含真实OS录制数据，但§3.3/C.3“online”从预测坐标匹配录制轨迹最近点（例20px容差），检索对应next screenshot，**不是实OS自由动作产生任意新状态**。offline又以oracle previous state独立预测，baseline只用第一action/endpoint，而本法用全waypoints；Eq2 prose称MSE但式为欧氏distance，Eq3命名Endpoint却逐时刻求和，不混为同一端点准确率定义。baseline online只给3 interaction steps，拒Captcha、调用错工具影响总分，不能归为唯一representation/规模因果。Table2 overall26.98仅该replay人口，OS13.11远低OpenCUA7B99.01；统一head Table5 online较高而offline78.55低于separate79.22；weights15相对10可退步，混合click+drag在OS/部分ScreenSpot域亦退步。A.2 single-screenshot VideoGUI不给实时反馈，不能算外部真闭环通过。B.1训练4H200、bfloat16、每GPU batch64无累积、1024×576 resize；推理latency/cadence/hardware/SLO、全baseline预算及seed不确定性Not Disclosed。E把text planning整合作future，不外推长程通用computer-use agent。

**owner差额与窄提案。** 已读[Ch78](../../../../../books/part-07-agent/78-tool-calling.md)Tool Contract/Proposal/执行与emulator边界（约37～56、652～658）及Ch77/79交接；Ch26闭环主干/三时间尺度（约110～128）已拥有物理action chunk与controller，不在那里复写GUI机制。Ch78当前有typed schema、权限和observation，但**尚未解释GUI pointer按键状态与chunk执行/截图cadence在同gesture内部的细粒度接口**。建议紧接Tool Contract加入GUI动作粒度段：start/end拖曳在直线无中途反馈任务上仍合理；旋转/自由轨迹则用坐标+按键状态短chunk，并显式区分prediction horizon、执行步数、下一观察，外层模型与executor仍分权。该schema增加鼠标hold状态、屏幕更新与调用成本，失焦/页面变化/反馈延迟会使未执行后缀失效；暂停、再观察与释放mouse状态是我们的runtime设计推断，不说作者已实现。replay评分只批准该近似环境的状态消费，不作为真实OS effect receipt，真实路径不足时回原受控GUI工具/人工。物理控制链接Ch26，不由数字环境论文授权机器人安全。

## 交给root的独立复核与实际写入边界

本文件为四家族必要证据作者结果，不自授Evidence/Books Gate通过。没有必要正文访问障碍，故四项没有外部材料请求；不为精确latency、可选代码或未采用headline遍历附件。当前普通待办为root必要原源/score/owner提案复核、其决定的实际Books写入及写后邻接检查；若认为具体增量已有覆盖，请指出实际承载段落，而非只用owner主题反推NoChange。

机器/范围检查：限定 `git diff --no-index --check /dev/null` 通过；四个本地owner链接已核存在。原104未编辑，所有提案仍为提案，不冒充共享Books实际落实。日级验收由root统一记录。

## POST：四项实际 Books 写入的非写入者检查

复核者：`jan02_new_evidence`；实际 Books 写入者：`root`。检查时间：2026-10-07 14:16～14:21 +08:00。结论：**通过，仅限下表四项实际写入及其邻接**。上节“待写入/提案”描述保留为写入前的历史状态，本节记录其后实际结果，不替代完整日报验收。

已重读当前 AGENTS、Books 适用的 ROADMAP/PROJECT_CONTEXT/LEARNING_PHILOSOPHY/WRITING_GUIDE 和相关 LEARNING_STATE checkpoint，并按研究合同与 Report 合同复核。逐项读取实际新增两段与完整前后段落，不只检查 diff/marker；原证身份、精确版本、拟采用命题和未决问题未变化，沿用本文件前四节的必要原源审阅，GaMO 的编码/加噪步骤另定点重开 exact-v1 §4.2/Algorithm 1。

| 实际落点 | 采用命题、原证核对与邻接结论 |
| --- | --- |
| [Ch66：低光处理链及下游评价](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，当前740～742行；`PLATFORM-EVALUATION-SYSTEM` | 已读 clean/fault 全段至新增内容及后续不确定性段。v1 III-A/Table I/V 支持 EV-only 与 RAW/ISP 分支身份、严重度配对及增强正负收益；正文未把合成 RAW 当实测传感器，未授 noise-only 因果或机器人安全。Ch23链接保留表示 owner，本节只拥有处理链验收；机制、代价、替代与反侧贴近，无冲突。 |
| [Ch24：固定 pose 扩 FOV 的生成—重建分支](../../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)，当前1449～1451行；`MULTIMODAL-GENERATIVE-PARADIGMS` | 已读前方相机条件/稀疏视图→重建→渲染的完整段落，及后方 camera×animation-time、分阶段条件交接。v1 §4.1～4.3、Algorithm 1、Tables3/4及限制支持几何条件、latent mask mixing 和 refinement 成本。初稿“图像先加噪”有域歧义，反馈 root 后实际重读修正版“图像编码成 latent 后，加噪”，匹配 Algorithm 1第6/11行；未把 fixed pose 或 opacity 当真实几何证书。 |
| [Ch29：旧 teacher 不支持坐标的反馈分支](../../../../../books/part-04-training-system/29-sft.md)，当前446～448行；`TRAIN-SFT` | 已读完整扩词表保护节的原 text-only/SpeakGR 分支、新增两段及后方共享 trace 监督权重段。v1 §5.2/Tables10～12 支持保留扩词表 rollout、首个无支持 token 惩罚/截断及通用/专用任务阶段取舍。正文保留 text-only 合理性，未把无支持等同所有任务语义错误、未授无偏全词表 KL 或单组件独立因果，也不凭“恢复”抹去专用任务反侧；owner 无重复。 |
| [Ch78：GUI 动作粒度与再观察消费接口](../../../../../books/part-07-agent/78-tool-calling.md)，当前65～67行；`AGENT-TOOL-CALLING` | 已读 Tool Contract/metadata 演进至新增内容和后续 Proposal/执行分权完整邻接。v1 §3.3/§4.1～4.2/Table3/C.3 支持坐标+按键状态、预测 horizon 与执行步数分离及录制轨迹近似 online 身份。暂停/清理按键明确是 runtime 设计要求，不冒充作者保证。初稿“不共享其安全证明”可能暗示 Ch26 已有证明，反馈 root 后实际重读修正版“接口相似不能提供物理控制的安全保证”；并读 Ch26 闭环主干/相邻限定确认跨 owner 仅链接、不外推。 |

四个外链均指向本次已读的精确 v1 HTML，两个新增跨章相对链接已解析至存在的 Ch23/Ch26 文件；新 source-family 与采用命题一一对应。四份 Books 的限定 diff 各为4行新增、0行删除，原邻接正文、旧替代分支和既有 source-family 均保留，没有静默覆盖。限定四份 Books 的 `git diff --check` 通过；证据文件追加后亦做格式检查。以上机器检查仅辅助实际语义 POST，不自授来源覆盖、原104候选或整份日报通过。

本代理仅追加本节，没有改 Books、Report、共享索引或 LEARNING_STATE，没有 stage/commit/push。四项实际写入 POST 无剩余问题；至此停止，不转入下一日。日报新增行、总数/缺口及非作者日级验收继续由 root 协调。

## 增量恢复：2512.24111v1 的 score-Jacobian guidance

恢复依据：独立负侧复核指出原“MDE任务复用既有guidance”理由遗漏了 IV-C 的实际向量变换，root 重开题摘/core 后同意准入；只处理这一具名漏项，不重开上述四项有效结果。执行时间：2026-10-07 14:28～14:35 +08:00。已重读当前 AGENTS、研究/Report 合同、每日来源使用说明、Prompt、ROADMAP、本日 README/supplement 与相关 checkpoint。

### 日期与身份的独立窄核

已打开 [abs v1](https://arxiv.org/abs/2512.24111v1) 与 [HTML v1](https://arxiv.org/html/2512.24111v1)。官方当前页仅v1，无撤回/纠错/具名安全信号；所读作者正文没有显式更早公开日期。未扩全网首发考古。

本代理实际重取 [arXiv-issued DOI 的 DataCite 字段](https://api.datacite.org/dois/10.48550/arXiv.2512.24111)：Submitted `2025-12-30T09:41:41Z`；Updated（dateInformation=v1）`2026-01-01T01:21:43Z`；created=registered `2026-01-01T03:04:10Z`；Available（v1）`2025-12`。这些字段按自身口径保留，Updated不证明有新revision，registered不直接证明公开。

实际读取 [官方2025年末假期原页](https://blog.arxiv.org/2025/11/21/temporary-changes-to-announcement-schedule-due-to-end-of-year-holidays-2025/)：Dec30无公告，Dec29 ET14～Dec31 ET14的received-and-accepted材料归Dec31 ET公告。abs下界晚于Dec29 ET14；[官方availability](https://info.arxiv.org/help/availability.html#a-note-about-arxiv-id-assignments)规定ID在首次公告时分配、不能提前提供且不可回溯月份，故2512身份排除延至Jan首次公告。联合限定 arXiv v1 的北京时间日级公开为 **2026-01-01**。这是规则与身份的联合推断，不是Submitted/Updated/registered=公开，不授逐篇精确时刻或全网家族首发。按本日补充自然日落窗，原104不搬移。

### 必要审阅与采用边界

材料：[Guided Diffusion-based Generation of Adversarial Objects for Real-World Monocular Depth Estimation Attacks](https://arxiv.org/html/2512.24111v1)。评分 **2+1+2=5**：重要的guidance替代变换、单一生成采样组件、可复用但有条件的局部接口；不将汽车领域、潜在安全影响或全部MDE pipeline升为跨层分数。标准审阅完成；因具体机制与公式争议，定点深入受影响内容。实际读 III-A～C、IV-A～C Eq7/11～13/Alg2/Fig4、V-A～D Tables I～IV、VI；不遍历无关references、视频或可选代码。

**受原文支持的最小差额。** Eq11的外部方向δ先经score Jacobian成为`J_score δ`再进入Eq13采样，而不直接消费δ；δ本身已通过clean estimate反传。因此这是额外的方向调制，不是把普通denoiser VJP改名。这里只采用该分工，不照录“语义流形方向保证”。

**公式的具体未决。** Eq12线性化用`z−δ`，Alg2第7行用`z+δ`；第8行未闭合精确JVP/差分实现、尺度及误差。局部Taylor近似须有可微性、受控步长/余项；Eq13以Jδ替代δ是新目标，不由Eq6严格等价推出。一般`J=UΣVᵀ`在右奇异坐标消费输入，再映到左坐标；把左方向直接当输入语义方向需要额外条件。即便精确score有对称Hessian，乘J也不自动构成语义投影或安全过滤。原文Fig4仅示例，learned score导数与像素/latent接口不能由此默认可信。本项不采用可执行精确算法、无损manifold或真实安全定理。

**评价、反侧与成本。** TableII同region/text对照支持受测guidance分支，但MonoDEVS的MRSR与ADMM持平；TableIII的w/o JVPG移除全部外部梯度，不能独立归因于J。CLIP-Score测文本对齐，MRSR测相对原预测的变化，均非真实几何/安全证书。459 KITTI scenes、PowerPaint-v2与五个MDE模型，不能推广全部任务；实物部分仅MonoDepth2、三场景/单对象，未验证驾驶闭环。正文未披露完整采样/预算、硬件、精度、batch、时延及seed不确定性，相关字段Not Disclosed；SLO不适用该离线验证。训练免除仍需外部梯度、score导数/额外求值及完整采样费用，没有端到端效率认证。VI的black-box/鲁棒训练仍是未来方向。

### 具体 owner 差额与窄整合提案

已实际读 [Ch24](../../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)当前约159～169行的约束采样/VJP-free guidance完整邻接，以及约299～316行的score Jacobian误差与reward guidance段。既有正文承载“denoiser VJP可作近似”和“score函数/导数误差分账”，**尚未解释外部方向已形成后再经score Jacobian调制的替代消费接口**；不因同有Jacobian/gradient术语判已有覆盖。ROADMAP owner为`MULTIMODAL-GENERATIVE-PARADIGMS`；Ch23表示与Ch25/26环境/动作边界沿用已核有效上下文，未改动。

这一差额可能承载的窄知识链是：直接外部方向在局部目标/成本已验收时仍合理；另一分支可让冻结score的局部导数再调制该方向，但这改变guidance目标，不是保真chain rule或语义投影证书。它应区分方向形成、导数变换、sampler消费及额外成本，不提供物理攻击部署recipe，也不重复开MDE/汽车安全章节。原源的符号/估计接口未闭合前，这仅是可解释机制与潜在owner差额，不授实际正面整合。

**root非作者复核后的本轮最终决定：争议/暂缓，不写Books。** 评分仍2+1+2=5，必要审阅及受影响机制深入完成；不改判贡献前关闭，不抹去可核的Jδ分支与局部实验。隔离的是Eq12/Alg2第7～8行的符号、如何估Jδ、语义子空间保证及依赖它们的采用结论；当前不以它们支撑语义/几何/安全保证，也不把TableIII当J的独立归因。后续若澄清成立，可在Ch24当前VJP-free段后重新判断窄整合；否则保留直接/较弱guidance和原sampler。

**一次具名重开需求。** 请求与`2512.24111v1`直接对应的作者勘误/说明，或仅该采样路径的对应实现，明确：(1) Eq12的minus与Alg2第7行plus到底采用哪个，如何与Eq13接上；(2) Jδ是精确JVP还是score差分，若差分其步长、缩放/归一化和误差适用条件是什么；(3) “语义子空间”到底只是Fig4观察，还是有额外假设/论证。可接受能逐项闭合这些接口的具名作者说明，不索所有附件、完整仓库、实车或新的闭环安全实验。材料到达只重开IV-C Eq12～13/Alg2与这一owner提案；版本号变化本身不触发无差别revision比较。正文已经取得，此处是中心接口争议而非访问故障。

本代理仅追加本项证据/提案，没有写Books、Report或Learning State；已有四项结果与原104均未重审/改动。独立日级验收与本项实际Books决定由root协调；本项检查结束后再次停止，不接下一日，不stage/commit/push。
