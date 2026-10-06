# 第八批 actual owner PRE

必要原源见[V3_CORE_EIGHTH_BATCH](V3_CORE_EIGHTH_BATCH.md)。root已独立复核全部六项：15515 Ch31:406、15756 Ch72:2841（每层新增2m trigger坐标、R为原输出及目标范数界）、15513 Ch77:55、15549 Ch26:488的实际正文/完整邻接/末注POST通过；四窄锁已释放。15654 Ch72 memory-origin具体Existing通过，No Change；15602中心C3→Th4.3条件化证明冲突精确终态隔离，不写证书，重开需修复该证明。非日级Gate。

## 15513 HIMM — AGENT-MEMORY / Ch77 窄差额建议

actual Ch77 L43–53 external durable state与persistent worldreference/近期context分账，mapper估计不可升格事实；Ch25 L450–460 map更新/校正与局部submap仍属环境估计，均未有保留semantic observation/time/pose而检索时才投影到地图，避免全量融合alignment累错的具体选择。拟Ch77该worldreference段后最多1段，topK+visual检验也只是受限read policy；GT轨迹/答案产生rule并非无标签在线，Qwen两项反侧及未披露topK/费用/HW/CI保留。存储与检索对齐付费，pose不可靠仍回退直接观察，旧在线融合地图与短时context合理，不新建WorldModel路线。

## 15549 DEWM — MULTIMODAL-EMBODIED-VLA / Ch26 窄差额建议

actual Ch26 L23–26物理约束/中止、L475–489 State ownership/currentbelief/controller/outcome与monitoring分账承载动作权界限，但尚缺interaction phase绑定expectedpostcondition→动作反馈及post几何验证才提交derived DBstate→按阶段差额修belief的具体闭环。拟Stateownership后最多1段，补memory commit不物理回滚/几何检查不是动力学安全。GT perception仿真与CAD已知类别/实机诱导failure、callcounts非tokenlatency、CS bundle局部对照/ERT没独立消融及中心N60vs20叙述精度在notes保留；perception污染或phase不可信重新观测/停机，旧直接reactive/短chunk与独立controller不覆盖。若root判已有精确覆盖则No Change，不因数据库实现堆段。

## 15515 — TRAIN-RLHF / Ch31 具体差额建议

actualCh31 L256–269 reward/gradient ownership、L396–401 update方向sensor/KL/fallback已读，缺参数依赖probe作reward时stopgradient policygradient vs直接backprop probe的不同优化路径；不是普通rewardhacking或探针主题映射。拟RewardHacking方向段邻近最多1–2段：原/训后model对同文本的probe对照分policy evasion与representation drift，stopgradient无直接probe激励不等不漂移，独立heldoutcode outcome非一般honesty。highKL/alpha局部/alpha100退化、followup接口/分类差阈值与probe开销近正文。Ch30/32相邻交接有效复用，训练owner不接管deploymentsecurity。

## 15602 — PLATFORM-SECURITY / Ch72 暂缓精确证书建议

actualCh72 L410–434 DP邻接/经验攻击/发布分布分责，L2599–2611 datasetinfluence/重训参照与曲率成本，L514–538真实accountant同构/经验下界已经承载formalcertificate≠有限logitdistinguisher。ridge个体sensitivity Gaussian calibration是实际机制差额，但C3条件化后用独立Gaussian推理未补证，故不写新certified分支；拟本次暂缓精确Th4.3保证，报告保留strongconvex/learnnoise/point依赖校准提案和受限异质性结果，等独立证明或修正版定点重开C3→Th4.3。非证据弱EX，不授deep empirical ε为正式保证；若root能核通条件步骤则再定point机制PRE，不重复全史。

## 15654 — PLATFORM-SECURITY / Ch72 具体Existing建议

actualCh72 L1422–1444 memoryoriginclaim低于effectreceipt、同source放大、跨时刻sleeper需要写入provenance/权限/expiry以及隔离/回退具体承载；Ch77 L66–104 writer proposed→validate→pending/active治理有效复用。Zombie标准web→summary/reflection/rawhistory→memorywrite→futuretool的受限机制提供现论点验证，复制/多carrier是攻击实现细节，不独立补段/攻击配方。300exposure/20trigger、benignutility缺失/普通writer接受率不可泛化保留；不把所有商业agent或现实case叙述授实际事故。

## 15756 — PLATFORM-SECURITY / Ch72 具体数值contract差额建议

actualCh72 L2830–2840 loadtimehash/transformchain/执行前commit身份已读，只解决执行对象绑定；未承载layerlocal δ检查依赖proversupplied previousstate与global输出误差不可合成的数值contract。拟这段后1段：function-equivalent2m trigger网络、有限R/g/线性final/ReLU/l∞/adversary选error的具体反例，稳定性/全图误差预算须另证。既有identity/签名不被覆盖，不反原sumcheck特定协议，不当FP16随机误差或现协议实测攻击，globalcertifier成本未披露。Ch71/73交接已实际读，不建新结构。
