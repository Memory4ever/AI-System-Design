# Backdoor Directions in Vision Transformers 2603.10806v1：最小必要 Source / 实际 Ch66 / NC 提案

只处理03-13既有日报的Mar12 BJT补充自然日。准备者mar13_supplement，待非准备者审。本ID完整v1题摘与准入§19、日级公开夹证§23有效复用；本轮实际回AB：四作者、唯一v1、Comments31pages/16figures，无可见纠错/撤回/具名先稿信号。DATE3的arxiv.content/findable、created/registered Mar12T02:10:15及原Submitted Mar11T14:13:48已回原值，公开日由既有公告下界+注册上界夹证，不单拿Submitted/Updated或月字段。

原件 https://arxiv.org/html/2603.10806v1 ，SUP_CORE_10806.raw/txt及MANIFEST_RESULT：GET200、1018699B、UTC2026-10-10T03:35:20.868527。实际读完整§4、§5.1/5.2（代表层Eq1、完整Table1和权重干预）、§6.1–6.3静态/分布特征的必要对照、完整§8和§9 Discussion/Limitations、App0.F文字及14–16caption。首页问题/假设直接读过；§7 adversarial探针只见与边界相关解释，不采用其效果/因果结论。图仅正文/caption，未视觉读16图/精确grid坐标，不读全部附录cosine表/代码/旧稿、不复现或设计攻击。支持与直接反侧已足，停止扩大。

## 实际增量、最低评分

已知trigger的方向干预能调制backdoor，不应被直接用作未知trigger部署防线→本稿同一受控ViT人口分开known-trigger activations/weights干预与只读head/early weights的未知trigger预检，并显示后者按trigger类型系统性失效→采用诊断时必须分清数据/trigger权限与negative结果，不能由无数据预检阴性或已知trigger修复给release签字。

拟2+1+2=5：D2计具体已知触发机制到无需触发信息的检测边界/失败类型证据，**不计成熟平均方向、orthogonalization、线性representation原则为新增发明**；R1是视觉模型诊断局部负载，不因security标签或activation/weights两个操作借多层分；Durability2是所需访问权限和分布适用界，不以模型尺寸/可访问/正文长度升降。安全解释与设计反侧触发受影响必要深入已完成。拟实际Ch66具体已有覆盖Books0，不称本篇新干预/数据已吸收，不因已有覆盖降分或删候选。

## 必要机制与直接反侧

§4采用公开BackdoorBench的pretrained ViT-B16/12 blocks，CIFAR10/100/TinyImageNet；三poison rates .01/.05/.1，依据可下载模型选择攻击类型，LF因可用ASR<5%被排。这个选择不是全ViT/全部失败攻击人口；.01部分仅40–70%。§5完整知道trigger和backdoored training data，clean/trigger配对在每层取平均activation差，分CLS或all-token。作者明确这不是现实未知trigger防御。

Eq1按正steer ASR与负steer RA相邻层增量选代表层，有监督目标类/原标签与选择开销；正负干预与去方向能支持该设置中的功能影响，不能唯一定位所有因果回路。weight orthogonalization改初始embedding和attention/MLP output；公式W−r̂r̂ᵀW没有在这段明确r̂单位归一化，与原平均差/代表层记号不能自动补成精确可执行recipe。本次不采用精确投影实现、不据此否定实际代码或全部干预结果，也不需追旧引用原稿。

完整T1只汇总baseline ASR≥.9的33模型（12/13/8），不是全部可下载人口。总体ASR97.7→6.7、RA2.1→64.7、clean accuracy82.8→82.0；CIFAR100仍ASR15.9/RA51.4，CIFAR10 clean95.4→93.9。不能写完全移除、全能力保持或未知trigger有效。CLS负steer总体RA21.3，而all-token53.8，修后64.7仍非clean82.0；trigger图像失真只是作者可能解释，不是唯一原因。独核另发现§4仅CIFAR10列Blended，但§5 Results把CIFAR100 Blended说成唯一失败；不采用该“唯一例外”的攻击/数据分配，不扩全部附录，完整T1负侧不变。

§6静态patch/全图pattern更依赖位置、early all-token可调而CLS晚；分布触发各patch可感知并较早聚合。不同攻击/层、.01不成功模型被图排除的选择保留，不把qualitative趋势变所有ViT定律。DeiT-S/Swin-S只TinyImageNet两攻击/.1，Swin无CLS用token均值，不认证所有架构。

§8无需clean数据/trigger，但要完整classifier head与早层output weights。原score公式是阈值指示函数的数量，解释句却说把超阈值值相加；count/sum口径未统一，本次不采用精确detector执行配方。top与second差除剩余score std和t的max，Z>3只原启发式，不是已校准normal-null/FPR证书；阈值×layers grid没有独立未知部署选择/holdout假阳性人口。图7正文说WaNet/BPP容易、SSBA边缘、TrojanNN不工作；App0.F再次明确不是全部攻击或场景。**这种预检阴性不能证明无backdoor**，不用未视觉grid坐标推精确检出率。

§9已明确known-trigger分析不能直接现实防御，修复仍需reverse-engineer trigger；weight-only方案对多种已知攻击失败，full-training adaptive攻击可绕过，约一分钟每模型只是作者局部描述。硬件/precision、完整检测阈值选择/独立FPR、paired subset大小/seed/CI、全预处理/修复与重复验证费用必要段Not Disclosed；不用这个分钟数推部署SLO或低成本总审计。此处只记录公开的防御适用界，不提供trigger植入/绕过步骤、攻击提示或实际操作。

## 实际唯一 owner 与具体 NC

ROADMAP唯一PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)实际完整234–289局部已顺读：subject包含完整model/adapter/runtime身份；静态adapter权重几何信号必须绑定制造方法/分布与holdout，方法间可反转；预检只能提出probe，由匹配目标的独立行为测试验收，阴性不取得release Gate。无输出内部探针仍有前向/校准与模型访问成本，不把训练类别当真实危险能力；activation sensor随后保标签/层/span与authority分责。这个实际正文承载当前拟采用的访问/人口/静态预检不代behavior/release判断，不是只看安全主题。

本篇head/early projection对齐的局部新sensor配方和受控trigger类差异不要求新增长期controller或责任接口；具体新实验在本日保留，**未称现书稿含其新数据或已吸收trigger方向结论**。Ch72负责风险/发行权限，Ch17负责组件计算，均只handoff，不另owner/多章写。拟5分必要深入、具体已有覆盖Books0；无PRE/POST需求。非作者须实际核Source、score及现文承载后才formal。

最小重开：若声称可实际未知trigger自动修复/全检出或release，需精确归一化与count/sum实现、独立clean/adaptive/type holdout、阈值选取与真实行为保留/全费用原证；仅达到具体资格才重开，不要求遍历全部攻击历史。普通其他项继续；本篇ready非formal、非DAY。
