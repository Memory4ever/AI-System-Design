# ABot-PhysWorld necessarySource / sole Ch25 两PRE

2026-10-12，作者独占准备，[2603.23376v1](https://arxiv.org/html/2603.23376v1)，原2+2+3=7/date25不动。actual首份正文§2–3/Eq1–2、§4–5/T1–3、§6；HTML重复同稿尾部不是新增版本不重读。封面DateMarch20不是另一可核首次公开事件，不借它覆盖已核官方v1/公开日身份。未核code、所有图片/视频或复现。

## 拟采用接口与直接反侧

Wan2.1I2V14B全SFT三百万clip五具名dataset，经flow/CLIP一致性、Qwen3VL图动作对齐和hierarchical采样、Qwencaption；这些自动清洗与物理叙述不是可校准真实physics/causal truth。DPO阶段Qwen3VL32BThinking只初图+instruction提task-specific checklist，Tier1veto/Tier2细分+正负问题；Gemini3Pro用video/CoT逐项评分，多轮knockout/loser bracket挑有限N池优劣，不是全域最优，N/具体margin/问答人审误差未披露。生成问题和评判分两model减少自评同一角色依赖，却不能“prevent hallucination/单票证明fatal物理”或消除共同偏差。标准DiffusionDPO借用不计新数学，LoRA64冻结主干/临时关adapter算reference省第二套参数，不等**zero additional memory**/零额外计算；同base参考仍需求值。

Action7D pose/gripper（dual14）经camera内外参把position投2Dcenter、rotation三轴成彩箭头以长度含depth、opacity编码gripper/左右channel，再由每五DiT复制的contextbranch→zeroConv residual读入，A2V冻结backbone。Zero初始无信号是初始化事实，训练后仍能改输出，不证明物理prior功能不变或通用cross-embodiment。投影依赖标定/深度编码/occlusion，2Dmap并非URDF/可行域约束/真实future。与physical preference分责：条件载荷编码动作身份，judge只提训练偏好，真实transition仍无权由video/VLM证明。

评价必要反侧：174PBench robot videos/886QA，BridgeV2/AgiBot/OXE与训练有同source，不能授全training-independent；EZS初图NanoBanana或VLM改背景，描述由VLM拟动作/物理叙述，未披露最终样本数、独立人审GT/重复seed/区间。评判Qwen3VL提问→Qwen2.5VL72B答、30–50%negative，S_v问答对checklistGT一致不是接触动力学真值；训练Qwen3VL同族proposer使heldout自动judge仍可能共享偏差，不能由换model消除自评或由合成combo标签认证所有OOD。T1 DPO domain.8785→.9306但quality.7678→.7676/MS.9916→.9908/SC.9406→.9355等退步，不采no perceptual sacrifice保证；T2只OurModel无独立DPO行，不拿其数全归因DPO。T3 200从A2V数据sample，train/test独立划分未披露；PSNR/SSIM与YOLO2D gripper nDTW不是完整姿态/contact/闭环，§6明示固定视角/无closedloop，真实deploymentfuture。

128H20训练cluster；TI2V480×832/81frames/6Ksteps/globalB128/lr1e-5；DPO BF16/rank64/β5000/perdevice1/500steps×100epochs；A2V16B/20K/lr5e-5，所有阶段硬件分配/完整walltime及inferGPU/precision/steps/concurrency/SLO Not Disclosed。不把训练cluster当infer配置；3M清洗/重采样/caption、所有N候选与双judge/tournament、reference/FM、context训练/推理/视频VAE与外部评估全计费。仅采用动作map条件与模型角色分开的偏好接口，不授严格physics、unique机制归因、完整OOD、zerooverhead、安全/实时。

## actual Ch25具体差额/窄锚

actual Ch25完整100–156（预测/噪声进展→simulator→PhysRVG训练仲裁→场景几何）、473–516持久state，913–961 Evaluation/readout/WildWorld/geometry及1258–1306 action fidelity/cross-embodiment→URDFgeometry→ReasonExecuteRender；Ch24/26开篇亦实际读。原group offset门是GT/FM仲裁，原URDF+视频reward为显式几何约束，两者未承载“标定7D命令的2D多channel动作载荷+独立生成问题/评判roles形成有限偏好”的具体交接。sole MULTIMODAL-WORLD-MODELS Ch25，DPO通用数学保Ch34，不新增双owner。

拟cross-embodiment完整原段末“硬件差异大或控制频率严格时，专用模型仍更可靠。”与marker SF2608-18077之后、下一“当目标从‘看起来像执行’变成‘确实服从给定动作’…”URDF段之前，两PRE+本人静态证据注，保全部原块。未独核/root锁/写入/POST。

## 两逐字PRE

规范化的动作请求也可以先变成与观察对齐的空间载荷，而不直接把一个机器人的命令向量塞进视频条件。一个受限分支用相机标定投影末端位置，将姿态轴、深度与夹爪开度编码为多通道 action map，再由并行条件块残差读入冻结的视频主干；零初始化只说明起始没有额外信号，不保证训练后原功能无损。这个载荷把动作坐标的消费位置明确化，却仍是二维条件，遮挡、深度编码或标定错误都可能让它与真实可行的转移脱节。<!-- source-family:SF-2026-ARXIV-2603-23376 -->

外观和接触缺陷还可以作为另一路偏好监督：先由一个模型根据初态与请求提出具名物理问题，再由另一个模型读取候选视频评判，在有限池内选成对样本更新生成器。问题生成、视频判断与动作条件因而有不同职责，但跨模型和单票否决都不认证问答正确或物理规律；自动 checklist 的一致率、二维夹爪轨迹和合成初态不等于真实闭环 outcome。[受限对照](https://arxiv.org/html/2603.23376v1)仍有视觉指标反退、评价人口和独立划分未披露，固定视角且没有闭环验证。清洗与制备、所有候选/双模型评判、参考求值、适配和条件推理均计费；评分、标定或动作支持失配时，保留原监督生成、显式几何/可靠 simulator 与真实 observation，不让偏好高分取得 transition 或控制安全权。

## 自身静态证据注PRE

- `SF-2026-ARXIV-2603-23376` — [ABot-PhysWorld exact-v1](https://arxiv.org/html/2603.23376v1)必要§2–6/Eq1–2/T1–3；仅标定动作的2D多channel条件与proposer/scorer分责的有限偏好训练接口。保自动问答非physics真值/同族偏差、zeroinit非无损、指标反退/人口划分未披露、固定view无closedloop与制备/N候选/参考/训练推理全费；不授严格physics、通用OOD、安全或实时，未核code/全部图视频/复现。
