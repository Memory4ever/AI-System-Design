# Sep25：已准入候选的有限必要审阅

本文件前两项为root明确接受作者A14的18993/18886首次必要域；后两项为另行明确接受A30的19199/19080，采用状态分开。作者/reader不抢相应CORE首备，已成日期、完整题摘、准入与原分复用，不第三评分/日门；只交首次必要证据，当前Books owner、README与后续整合仍归Singer。不是Books PRE、写位或日报完成。

## 2509.18993v1 CR-Net

[精确HTML v1](https://arxiv.org/html/2509.18993v1)实际200/exit0，2026-10-25T04:46:29.602687+00:00至04:46:31.514487+00:00；原件 `ROOT_CORE_2509_18993_20261025.raw` / 同名 `.request.json`，648463B，SHA256 `db63c249f11ecf4f4f9631ca53bb507450a9bda58726b586b46a3e64250c741d`。实际用标准HTMLParser保MathML alttext读取§2.1、§3–5/Eq3–10/Alg1/T1–4、B.1–2、D.2.1–6/T7–12、E.1–2/T16–17、F/T18–19。只读相关caption/prose/table文字，未核图像素、代码/训练实现或复现；未审C理论证明、全部D.1观察与D.3变体，不采用其普遍低秩定理或所有MoE/GQA结论。

### 机制、shape与采用范围

直接将每层映射限制为低秩会损失该层可输出的方向；这里改为保留同位置的上一层线性输出，再训练增量。Eq5/6第一层仍为完整矩阵；之后对同一位置P，令X为 `[s,h_in]`、A为 `[h_in,r]`、B为 `[r,h_out]`，输出为 `Y_l = c_l Y_(l-1) + (X_l A_l) B_l`，两项均 `[s,h_out]`。c由可训练beta构造。低秩只限制新增路径，完整历史路径可以保留更高秩信息；这不是冻结基座的普通LoRA，也不证明相邻层差分对任意数据/训练阶段都低秩或与完整模型行为等价。§3.1用既有模型/小文本观察提供动机，不是训练新架构的通用无损证书。

新增依赖改变反传重算。§3.3/Alg1前向保所有层输入、低秩中间XA及选定层完整Y，最后层必存；反传按L至1用当前完整Y及已存XA反求前层Y，再算该层所需activation/gradient，避免每次从头重放所有前层。这里没有取消原attention、非线性或梯度链；省下的重算换成保存XA/完整锚点及逆运算。论文所述普通GCP的二次重放是其未传递这类历史状态的朴素实现，不是所有checkpoint schedule的下界。B.1存储项写成XAB而§3.3说存完整Y，且文字正反遍历索引有不齐；采用以清楚的完整锚点/Alg1依赖为限，不据打印式补整套可执行实现。

Eq7逆除以c，仅在c非零且数值条件适合时才有实数代数逆。Eq6的 `sign(beta)(abs(beta)+epsilon)` 在通常sign(0)=0定义下，beta=0仍为0；加epsilon本身不证明所有状态可逆。这个局部代数检查不证明实现必除零，代码的零点约定未核。即使beta非零，减法消去与除小系数也会放大有限精度误差；每八层存锚点和T17观察到多数beta在.2～1只是该实验的缓解，不授任意beta、BF16或全训练梯度精确相同。E.2“beta大由新低秩主导、趋零由历史主导”的说明与Eq5/6直接系数方向相反，保此冲突，不合并成一条调参recipe。

### 控制、反侧与费用

- C4-en、LLaMA样式60M～7B为主，D.2.3另13B只40K步；max length256、global batch512、Adam，学习率八选一由前10%步验证PPL选择，低秩参数学习率再乘.25。T3引用多个基线原论文结果，不是所有方法在同一实现/调参预算内重跑。参数对齐与optimizer-state内存对齐是两个不同比较，不能混成同时同参数、同质量、同成本。
- T3 aligned-param CR-Net在350M PPL18.95仍差于full18.80，1B为15.22对full15.56；不是所有规模皆胜。T4在10K步CR23.11差于CoLA22.76，后续才反转。T10的13B40K为18.12差于full17.85；“comparable”不等同质量已达。2048长度T12只对GaLore有限比较，不授任意长上下文。rank分配和learnable beta消融提供配置选择证据，不能因挑中最佳配置认为所有配置稳定。
- 文本写512×256为13.1K tokens/batch，但乘积为131072，约131.1K；T3各小模型token预算与T7也不同。保原数与这处约十倍算术差额，不私补真实训练recipe或GPUh。T3内存主要是参数/梯度/optimizer状态，不等总峰HBM。T2把BF16/7B/B16/s256的数值与省略低阶项的理论式放一起，不能将元素计数直接称实测总bytes或更少activation本身的普遍证明。
- 吞吐对照绑定作者A10040GB、1B、B16及引用基线；正文Figure6引用与实际Figure3 caption混用，未重建曲线像素。D.2.2的1.326x/18.489x把所需步数与估算FLOPs组合，是模型化计算预算，不是完整墙钟实测。训练数据制备、8组学习率/rank/beta选择、重算、状态驻留、实现kernel及验证都计费；重复seed/不确定性、全实验GPUh与同质量端到端成本未披露。
- F为peak312TFLOPS/PCIe64GBs的PP估算，13B/70B、s4096、microbatch16、PP2/8。跨边界多传同位置历史输出使CR通信量显增，不能说低秩自动减所有通信；它也增加activation而减少权重/optimizer。T19中70B full的36.67e15/312e12约117.53秒，不是所印177.53；按同一公式与CR46.51秒也不支持所印131.02秒节省。记录内部算术冲突，不修表、不声称实PP或推理收益已验证。推理无optimizer/反传且batch不同，不能直接沿用训练估算证明serving优越。

**有限可支持命题：** 将低秩约束施加于跨层增量而非全部输出，会同时改变表达路径、activation保存/反求和跨设备状态接口；保留完整路径及重算锚点是一种有条件的质量—参数—内存分配分支。它不证明低秩无损、可靠可逆、自动可部署、普遍净加速或更小通信。数值、质量或依赖预算不合时，完整模型/普通低秩训练/更密锚点或显式保存仍合理。具体长期缺口由作者实际读owner后判断，不在本包预I/NC。

## 2509.18886v1 Confidential LLM Inference

[精确HTML v1](https://arxiv.org/html/2509.18886v1)实际200/exit0，2026-10-25T04:46:31.591000+00:00至04:46:32.137094+00:00；`ROOT_CORE_2509_18886_20261025.raw` / 同名request，186801B，SHA256 `bde6e35560efa865a9ff6ceb0ed4bcbcb4b331c1e546002e3dac885b0458fd0e`。实际完整读II–VI/VIII及TableI文字、F2–14相关caption与setup/反侧说明；未像素量化曲线、检查实现/attestation实际执行、攻击实测或复现。全部硬件/驱动/价格/可用性只属论文2025配置，不当2026当前产品事实。

### 保护边界先于百分比

SGX按进程/Gramine libOS隔离，EPC分页、enclave进出、加密内存和syscall模拟在关键路径。TDX按整VM隔离，开发接口较普通Linux兼容，但guest OS/services进入TCB；磁盘/密钥保护仍需另配，不由VM内存保护自动涵盖。两者保护对象/可信软件范围不同，不因同样低开销称安全等价。

所测H100 confidential GPU需要CPU TEE，PCIe command/kernel/data经加密认证bounce buffer；H100 HBM/NVLink在作者威胁口径下不具同样内存/链路加密属性，不能把GPU侧4–8%与CPU内存保护直接比作相同威胁下的代价。B100安全/可用性只作者当时说明和预期，没有本实验B100测量，不外推其开销。跨节点还要网络保护，host transfer、key release/attestation边界与用户明文出入口不能凭kernel在TEE内就消失；这里后几项是据保护边界推导的部署检查，不声称论文已完整实现/验证整条信任链。

论文主要是配置/性能研究，不是漏洞穷尽、侧信道抵抗或形式化机密性证明。II对HE/MPC的宽泛成本和能力对比不是同工作负载本次实测，不能据其概述宣布所有密码学方案不可用或无完整性。较小TCB与较易编程是取舍，而非CPU/GPU或SGX/TDX普遍安全排序。

### 对照人口与直接反侧

- CPU两台双socket Intel Emerald Rapids：EMR1 XeonGold6530/32核、EMR2 Platinum8580/60核，各16×32GiB DDR5；Ubuntu23.10/24.04、PyTorch2.2/2.3、transformers4.35.2/4.38.1、IPEX2.2/2.3.100与oneCCL。Gramine1.7/SGX、TDX、普通VM、bare-metal四环境，Llama2 7/13/70B为主，BF16与量化INT8。AMX/IPEX比较限定该时版本和实现，不把旧vLLM CPU表现当现框架上限。
- 每实验多次生成、至少1000输出tokens；CPU典型1024输入/128输出。吞吐用B6/beam4、逐token latency用B1/beam1，后续不同图又用不同socket/B/input；不同指标人口不能合成一个服务SLO。violin移除Zscore>3的约0.64%异常，故不能由图宣布尾延迟合格；每token统计不是独立训练/服务复现实验的置信区间。论文200ms/word阅读类比不是用户SLO或尾部保证，TTFT分解/开放并发goodput没有完整验证。
- 单socket SGX约4.8–6.15%、TDX约5.51–10.68%，TDX对普通VM约3.02–7.01%，分开虚拟化税与保护税。双socket TDX可12.11–23.81%、SGX可230%；NUMA绑定/SNC不适配可把约5%抬到42%，因此摘要“<10%”不可跨拓扑。该驱动版本未兑现NUMA/1GB hugepage设置，不是未来所有TEE不可NUMA；TCMalloc/OpenMP/最大EPC、关SNC/合适线程均为具体配置条件。
- IV-C无AMX时INT8实现缺少合适AVX路径，极端1700%延迟不能全归TEE本身；AMX同时改计算效率/数据流。batch/input增加先变compute-bound、后因KV/cache/TLB变memory-bound，开销可以反弹，不是越长越低。更多batch以单请求等待/延迟换吞吐，不自动符合在线SLO。
- GPU为Azure H100 NVL94GB、AMD EPYC9V84 host40vCPU/320GiB、Ubuntu24.04/vLLM0.8.5，confidential与non-confidential两租赁实例，无法bare-metal。Llama2 7B不同B/input下作者约4.4–7.5%，不是CPU同实现或同配置重跑，也无H100物理攻击测试。offload会增加受保护PCIe搬运；多卡/多VM RDMA/GPUdirect缺失的数字属于当时平台/引用，不是本文完整多卡实测或当前NCCL定律。
- V-D的百万tokens费用使用GCP US-East1 spot价格、CPU固定128GB/可变vCPU；CPU实际EMR2与GPU Azure测量再套该价格，不能称同云同region/on-demand全费A/B。CPU约32核后受memory限制，低B/短input可能更经济，更多B/长input可反转；价格时点、利用率、尾SLO与端到端云账单不能由这条曲线补齐。CPU/GPU可装模型容量和保护边界也不同，未有统一同安全目标/同质量/同容量的最终winner。
- VI为BEIR三检索路径（BM25/重排BM25/SBERT）及Elasticsearch都在TDX内的有限平均evaluation，作者约6–7%。这支持部分检索工作可纳同保护域的可行性，不证明完整retrieval→generator→remote工具/索引更新/访问授权的RAG系统端到端开销、隐私或回答安全。表格图标不可由纯text空cell推断，未核其图像语义。

**有限可支持命题：** 选择机密推理环境时，先固定保护对象/TCB/链路，再按计算强度、NUMA/page、受保护传输与服务工作负载测代价；不能用一个“TEE overhead”常数或单GPU结果替整系统预算。保护边界不合就需要不同部署/通道或软件信任设计，性能不合则优化放置/页/批量或选另一受信资源，而不是关掉必要保护后仍沿用原安全声明。没有强到可证明新增通用安全算法的证据；作者具体owner/已有覆盖/差额待实际比较，不在本包预结论。

## 交接

上述A14两项原件请求均已结束，无在途。交Singer实际读取上述有限必要原域并作为唯一另一角色采用；有具体异议只回影响该命题的原段，未用附件不作普通债或外阻。之后Sartre复用双角色已成链，不第三无差别Methods；新增owner/Books草稿与真实写后仍须独立检查。全部费用/反侧、打印冲突、未核范围保留，不改分、不因审阅费时或Books已覆盖而撤候选。A22/A23实际采用及R16角色闭合后来已发生；不由它们预授下列A30新域。

## 2509.19199v1 OPRL：A30新增首次必要

[精确v1](https://arxiv.org/html/2509.19199v1)，原ABS题名保Leanring/OPRL，不倒填后v3 iStar。`ROOT_CORE_2509_19199_20261025.raw/request.json`实际200/exit0、243356B/SHA256 `beda807a88efd828277f80a6ef9d6b7c88b994f682ad67c79275e5c0bef72f5c`，2026-10-25T05:22:21.819715+00:00至05:22:22.325194+00:00。实际完整读§2–4/Def3.1/Assumption3.2/Theorem3.3/Proposition3.4、Eq1–6/T1–3、§6及A–D/Alg1/T4；MathML逐式、相关caption/表与直接环境/训练说明已读，未曲线像素/代码或复现。A10日期与A12/R9原6/AB、v1/v2摘要差额复用，不新查日门或全文版史。

### 实际训练对象与更新依赖

一次环境step的a含整段reasoning加action，不是单个token。每题采N条多步轨迹，由rule/ORM终奖产生偏好pair，以DPO式更新PRM语言模型；再用PRM对各step整段action的logprob相对旧policy算隐式reward。分开规范化episode reward与全组所有step reward，按 `A_E + alpha A_S` 混合后更新actor，old snapshot再推进。这里PRM是与policy交替训练的概率模型，不是有独立逐步真值的critic。轨迹偏好约束某个总分，不唯一识别每步因果贡献；正log-ratio只是当前PRM相对旧policy更偏好该action，不证明该步真实有用。

§3.1说先更新PRM再用fresh PRM算reward，后文又称来自previous step；Alg1却先forward得到reward再更新PRM，之后用该reward更新actor。此版本时序不齐必须保留，不能补成一份已核pipeline。Eq3将R_o定义为reward之和却再取mean/std，与“组内reward集合”说明不齐；std0/变长mask也未在打印recipe完整定义，不由此断言代码必NaN。Eq6为action序列概率ratio/step平均，不直接替成所有token等权的PPO。alpha1的加法不是硬success gate：失败轨迹仍可能有正的step项，不能据消融文字说最终失败的所有步都被禁止正更新。状态、PRM/policy/old版本、参与step和归一人口须分别保存，这是采用条件推断，不冒作者实现已给完。

### 理论强保证不由打印论证成立

1. Eq2的logistic参数含beta，Assumption3.2的BT效用又除beta，之后直接匹配score到R*/beta，尺度桥未说明；不能私选一种beta约定修成已证明定理。beta0在定义允许，但后文除beta需要额外域条件。
2. Theorem3.3从static reference到old policy留下 `log pi_ref - log pi_old`；令old=当前theta，并不会让static reference自动等于它。简单单步、pi_ref(a)=.5、pi_old(a)=pi_theta(a)=.25时该项仍log2。轨迹logprob的链式求和本身不证明state-potential差、逐步无偏credit或最优policy集合不变；此打印证明不足，不以“telescoping”名字补结论。
3. Proposition3.4只假定old-policy最小概率epsilon>0，能约束log-ratio上侧，不能约束PRM趋零的负侧。二动作、old=(.5,.5)、PRM第一动作exp(-100)、beta1，第一reward约-99.307，绝对值远大于所宣log2；两分布均有效且正支持。这一有限反例否定该绝对界，不证明实验训练必不稳定。
4. 即使reward额外有界，也还需score-function/Jacobian、标准化与优化条件，不能推出所有参数梯度或交替优化统一稳定。old固定时的surrogate、同点分布KL解释与真正全轨迹梯度不是无条件同一物；ratio clipping不提供硬KL trust-region保证。本包不采用其一般gradient alignment/方差更低或稳定定理。

### 证据、反侧及总费用

Qwen2.5-(VL)-7B与Llama3.1-8B，PRM从base初始化；VisualSokoban actor为VL而PRM为文本Qwen，不能假设共享全部视觉输入接口。8A100、veRL、200步、actor lr5e-7/PRM1e-6、batch64/micro8、AdamW，无KL，alpha1/beta.05/clip.2，除PPO外每题8rollouts。WebShop/Visual默认RLOO，SOTOPIA默认GRPO，不能把全文GRPO例式当所有实验唯一实现。

WebShop规则匹配、6×6 Sokoban任务终奖/动作罚；SOTOPIA由GPT4o temp0评goal，agent temp.7，其他两任务temp.4。只优化goal不表示其余六社交维度或真实人类价值也改善。T1/T2三seed平均，T3/算法兼容F3/T4小模型单seed；evaluation选择validation最佳值，不是无选择偏差holdout。T1局部OPRL优于所列RL点可保，不能由此宣布通用强于frontier模型或所有算法/状态空间不可用。T2的6.68→7.16为+0.48分（0–10量表）、相对约7.19%，不是正文48%；6.97→7.11为+.14分，不能把差值乘100叫相对14%提升。

T3在该单seed下step奖励/分开advantage优于merged/token路径，但不能识别PRM、granularity、归一、终奖混合各自全部因果；raw Sokoban局部step penalty不是所有真实过程监督的上界。F4约105步达到原RLOO点只是更新次数/样本曲线，不含PRM新增DPO训练/打分/驻留，不能称同总费2x。F5更短episode可能节省环境步，但也改变step-normalization人口与生成token，reward先升不是已经辨识的因果credit。

保actor/PRM/old状态、8条环境/多轮tokens、终奖/LLMjudge、pair形成与PRM前向反传、全step打分、actor训练、缓存/同步/验证和选择全部费用；precision、完整engine配置、墙钟/GPUh/峰内存与同质量全成本未给，不编净加速/生产SLO。**可支持的有限机制**是复用轨迹偏好训练step评分proxy并与终局信号分别消费；中心无偏/potential/绝对reward界/统一稳定保证保持争议不采用，不能由实证补成证明。信号、分布或费用不合时保终局奖励、独立校准/人工核验与较简单RL，不以学得proxy替逐步真值。作者实际owner/Books决定仍新层。

## 2509.19080v1 World4RL：A30新增首次必要

[精确v1](https://arxiv.org/html/2509.19080v1)，`ROOT_CORE_2509_19080_20261025.raw/request.json`实际200/exit0、212471B/SHA256 `113df35de33613992a5f2a8a392ca0d3daf4595801e6739f8daa64f1a848e2c0`，2026-10-25T05:22:22.411876+00:00至05:22:23.622002+00:00。实际完整读III–VI/Eq1–9/Alg1/TI–IV及F1–4相关caption/prose；未图像素、项目演示/代码/机器人或复现。此前root项目页只日期字段，不冒Methods已审；本次首次必要独立按v1正文，不混2026 v2或当前项目更多结果。

### 模型、policy和真实执行器是不同消费者

先BC得到Gaussian policy，另训EDM式2D U-Net转移模型，以有限历史图像/动作预测下一图像；ResNet18成功分类器由expert的二值标签训练。然后冻结世界模型与classifier，在想象环境中采轨迹，用PPO更新policy/value。**世界模型输出下一观察，动作由policy输出**；它没有直接输出对任意机器人可执行的通用命令，也不因图像连贯保证碰撞/接触力/动作可达或真实safety。世界模型policy支持由已有offline数据限定，VI明确承认探索越界会使imagined rollout不准，补少量真数据只是future work，不写成已闭在线修复。

每action维在相邻bins内用two-hot线性插值作conditioning，K示例21。区间内可用加权bin恢复原标量，例如bins0/1、a=.25对应(.75,.25)，这是该表示的局部代数性质；区间外、bin边界、数值精度/单位/执行范围仍须定义，不证明learned dynamics无损。分段线性也非处处可微；线性projection并不必然有损，不能因对照较差宣所有线性编码必丢信息。普通score-function PPO并不需要穿过环境对action求导，two-hot可微不独证actor梯度稳定或policy学到真实物理因果。实数action到robot API的坐标/约束/低层控制不是由这里的编码自动给定。

Eq6的classifier输出是概率，随后文字/Alg1又把reward写为{0,1}，阈值未披露；不默补成已核校准器。value Eq9未完整写terminal/detach/GAE等实现，Alg1的L_R/L_C变量不齐，不照抄完整训练recipe或据此宣实现故障。classifier在有限真实示范上训练不证明对生成伪影/OOD状态同样可信；冻结它和world可减少目标变化，却不排除policy利用共同model/reward误差。

### 对照支持与不支持的结论

Meta-World六任务，每任务50expert+150BC+30random轨迹、每条50步；训练看4帧历史，测试自初帧递推。TI视觉指标/failed coffee-pull示例支持有限预测对照，非全部指标全胜：random FID World23.43差于iVideoGPT20.69；FID/FVD/LPIPS不证明action-conditioned counterfactual正确或实际可控。未直接验证每种接触/扰动因果。

TII三seedSR，BC仅50expert、offline RL用expert+150BC，而world转移还含random/多任务预训及rewardclassifier，不能称所有方法完全相同信息/训练算力。平均67.5对BC51.5为+16个百分点，保任务局部结果；IRASim-ft同world的test-time多候选搜索约40x是运行配置比较，不是包括world预训/PPO在内的全生命周期净费。RLPD/Uni-O4需额外在线步到某点，仅说明所测交互成本，不抹去World4RL初始expert/BC/random采集。

真实Franka Panda六任务各50人示范+50BC+50random，teleop用space mouse，之后policy优化无新增真实训练交互；评测仍每任务20次真执行，初场景/起姿固定，不是跨布局、相机/机器人迁移或自由环境安全测试。TIII put-bread-in为16/20，低于DP18/20；close drawer与DP同20/20，非全任务严格更好。TIII Gaussian行数加总72/120=60%，但表平均写68.3%；World112/120=93.3%、DP106/120=88.3%可复算，所谓+25点依赖不齐的Gaussian均值。保原数字/冲突，不替作者改总体分数或由20次成功授可靠性下界。更果断/少犹豫是作者观察，不是受控速度/安全因果。

TIV只比较actionencoding的视频预测指标，twohot在所列点较好；它本身没有给每种encoding对应的policy稳定/真机器人SR或梯度方差，不能证明twohot→稳定RL的整条归因。K/codec/模型容量和训练调参可能改变对照，全种子、置信区间与匹配compute未足。训练GPU/precision、denoise步、PPO超参/总imagined帧和端到端仿真速率在本必要域未披露，不据“real-time simulator”授实时执行。

全部真实采集/标签、BC、world及reward预训、反复diffusion采样、policy/value PPO、缓存/存储及真环境回归计费；少新增在线动作不等零物理成本或更低总GPU费。**有限可支持的长期命题**是观察转移、动作编码、学得成功信号与policy更新须分责，想象优化须回到真实执行/支持域验收，视觉逼真和编码可重建不能代替它们。越界、奖励不可校准或净收益不足时，保BC/可信原数据、已验较短想象域及受控真实核验，不以生成成功图像给robot动作许可。实际owner/已有覆盖或小gap由writer随后具体比较。

## A30新增两项交接

以上两CORE请求均真实结束、无在途；root首次有限必要准备完成，尚不等writer实际采用。交Singer唯一另一角色回各有限必要原域实际采用；Sartre随后仅角色/范围复用，不第三同Methods/GET。中心理论/安全/预算争议、局部正侧及明确未核范围一起保留，原6不改，不预NC/I/DAY；实际新Books内容仍须当前owner比较、独立PRE/root协调/真保存/唯一写后检查。

## A63新增首必要：19249 RLPT

root明确接受此前未开始的有限必要域；A61/R48完整题摘、日期、准入及2+2+2=6沿用，不第三。[精确v1](https://arxiv.org/html/2509.19249v1)原件 `ROOT_NECESSARY_19249_HTMLv1_20261025.raw` / 同名request，2026-10-25T07:40:27～07:40:35Z真实200/exit0、231258B，SHA256 `114b583da333fb9e26093bf908086d71035d98ca6321a85bb97236f9780dcfba`。实际完整读§2–4/式1–6、T1–3及F2–4直接caption、§6，另读F1caption限定scaling主张；未读全Related Work/参考文献、图像素或外部代码，没有运行训练。

有限机制是把语料切成句段，以之前内容预测下一段（ASR），或同时给前文与后一段填中间段（MSR），显式生成思考后抽取标记内的预测文本；后续原文提供参考，但**奖励仍是generative reward model对语义前缀匹配的二元判断**。它不是从文本自动取得客观真值，也不监督或验证整条思考正确。原先要求恰好一段会处罚合理跨句预测，改为与多个后续句段的语义前缀匹配；这缓解分句长度不均，却仍可能拒绝同样合理的另一续写、奖励错误原文或被judge误判。MSR训练有未来片段条件，不能说部署自回归预测也获得未来上下文；两任务的样本、提示和可见信息须区分。式4写单段参数，而实际prompt用多段reference，这个接口差别不静默抹平。

语料经过近重复、PII/污染与规则/模型过滤，并另外使用高质量数学QA；冷启动须已有NTP基座再SFT，不是替代从零预训练或零标注/零teacher依赖。SFT batch1024、LR2e-5/cosine/3epoch；RL batch512、LR1e-6、maxresponse8192、每题8次temperature1.0，用on-policy GRPO且无KL。S3 lambda只声明在(0,1)，具体ASR/MSR混合与完整clip/长度/无奖励组处理配方未充分披露；不能从期望奖励式补成可运行GRPO全实现。Judge身份/误判率、冷启动数据人口、实际训练token与GPU/precision、总预算、重复CI和完整独立污染核验在本域Not Disclosed，过滤声明不认证零泄漏或PII安全。

T1区分base→cold-start→RLPT，不能把冷启动巨大增益归给RL；Llama3.2-3B的MMLU 59.4→59.4并未增加，故“所有benchmark一致提高”不能逐项照录。尚无同额继续NTP/相同数据与生成计算的配平控制，不能由表证明RL比NTP一般更省或SFT只能记忆。T2为Qwen3-4B，64采样、temp.6/top-p.95、max32768、Math-Verify，pass@1/8与单次生成/全能力不同；RLPT+RLVR的AMC23 pass@8为93.5，低于RLVR的94.3，不是全项严格更好。额外RLPT阶段也增加预算，不能将其收益全部归为同算力探索边界扩大。F1/3只有作者趋势陈述及caption在本审阅范围，未核像素/拟合/误差带，不采用普遍power law或外推scaling定律；T3一个CoT样例不证明faithful推理、回溯机制或因果泛化。F4正文所写false positives与过严匹配的错误方向描述并不清楚，保留原口径，不私修judge错误统计。

全部语料清洗/去污染、冷启动、模型judge、八次轨迹生成/训练、ASR/MSR配比搜索、RLVR及独立回归均付费；少新人工标签不等零监督或训练净省。可保留的长期命题是**无人工问答对的原始语料也可通过明确任务变换和有偏judge产生序列级训练信号，但参考续写、语义奖励与真实能力必须分别验收**。Judge/数据支持不足时，保原NTP/SFT、受控子集或可靠verifier，不把文本中的后续句直接封为唯一正确未来。当前具体owner与是否已有覆盖由writer下一层比较，不预I/NC或整篇争议。

## A63新增首必要：18344 SubSpec

[精确v1](https://arxiv.org/html/2509.18344v1)原件 `ROOT_NECESSARY_18344_HTMLv1_20261025.raw` / request，2026-10-25T07:40:28～07:40:29Z真实200/exit0、245793B，SHA256 `ef42d058411d397e8d70a1af83a5571ee089773f8408e27c1d88550caf6542a8`。实际读§2.2/3–5、式1–3、T1–3/5及F2–5直接caption，Appendix A/B/D/E/H；未核图像素、F额外timeline、G另reasoning人口、C综述、源码或设备复现。A61/R48日门/准入/原6复用，有限命题只对应offload下的draft/target状态与全费用。

把target将offload的层另存低bit替身，组成全驻GPU的draft；target已驻GPU层共享权重，历史KV采用target已验证的状态，draft先追加、target验证时覆盖新KV。共享上下文不等于量化层产生的KV天然与target相同，也不代表可把未验证分支发布为已确认prefix；tree位置/mask、分支回滚与所有层状态须保持对应。此处draft是使用共同已验证历史的proposal过程，不能当独立完整量化模型的cache随意互换。本文给出树验证接口但没有展开完整随机拒绝/残差重采样公式或可核实现，故只按**正确target验证及状态发布的条件**保留lossless机制，不认证其随机实现已严格同分布、bitwise或任务质量已独立复现。

offload让target forward含昂贵权重传输，因而可接受更深、更贴近target的draft树以少搬几次；式3的稳态近似speedup=tau/(D*tDraft/tTarget+gamma)，增加tau也增加draft/验证成本，tau大不自动更快。树使用路径概率top-k，greedy目标下draft低温可减少深树剪掉正确路径的机会，但这是proposal选择启发，不允许把target温度一起改变仍称同一目标分布。D48/k6、HQQ4bit/group64及draft sharpening.2均为所测设置；T5 SubSpec的tau在.4/.6略高于.2，也不是越尖越好。异步预取/共享buffer隐藏部分计算传输，chunked prefill降低峰值；它们不令搬运、额外分支或编译免费。

所有主实验在RTX4090/i7-13700K/PCIe4x16/128GB DDR5，**程序限制8/12/24GB显存，不是真测不同小显存GPU**；Llama3.1-8B/Qwen2.5-7/14/32B，batch1、target温度0/.6、静态KV2048、torch.compile max-autotune。SD每数据集20例而无SD只前5例，不能当完全配对全样本时延；draft深度/驻留层数也因方法不同，不把总系统差异全归独立某一优化。Appendix H中SubSpec target decoder层全部offload，原baseline各留11/15/20层，其他draft另有不同驻留层数。T1有局部反退，例如14B greedy HumanEval 15.70<中型draft16.20，32B greedy HumanEval 7.58<小draft8.22；均值领先不等所有任务胜出。12.5倍是32B/24GB/greedy这组相对naive offload，不是高并发吞吐/TTFT/TPOT分位数或统一SLO收益；随机温度下收益及tau下降，全文“60% decrease”不当所有行一致的精确比例。五次MT-Bench重复的.101token/s标准差不覆盖全部配置/任务。

T2逐步消融共享KV、sharpening、async，但无完整因子交互/同额调参控制。T3同一8B/MT-Bench/8GB下独立HQQ模型135.84token/s显著快于SubSpec24.29，只是更改目标权重/分布；它仍是用户允许质量退让时的合理替代，不能写成所有量化必然伤害目标任务质量。最低显存约7.1GB的Qwen7B、仅4bit替身、主要dense模型都是明确边界；MoE/更低bit/新链路收益未验证，PCIe带宽进步不保证保持相对加速比。

CPU原权重、GPU替身/共享层/target历史KV、树节点与验证workspace、预取buffer均要占容量；量化制备、编译/调优、两路执行/全部搬运、prefill、树构造、target验证及独立数值/分布/质量/SLO回归全计费。若容量不够、并发使树验证昂贵、acceptance低或状态兼容不成立，保普通offload、小draft、较浅树或验收过的直接量化路径。可采用的是**在固定目标分布约束下，以proposal驻留和更深验证摊销offload，而不是任意共享两模型cache**的受限分支；当前owner具体差额仍writer新层，不预整合或实现认证。

两新首必要请求均已真实结束，准备域交Singer唯一另一角色回上述有限原域实际采用；Sartre之后角色复用，不第三同Methods/GET。未读且不支撑本拟采用命题的附件不扩为新队列；如实际出现决定采用的新反证，再具名补读。日期/原分、普通尚待owner及整日发现均不由本包自动完成。

## A78新增首必要：18629 HyperAdapt

root明确接受此前未开始的首必要，R51日期/准入及原2+1+2=5沿用。[精确v1](https://arxiv.org/html/2509.18629v1)原件 `ROOT_NECESSARY_18629_HTMLv1_20261025.raw` / request，2026-10-25T08:40:14～08:40:16Z真实200/exit0、268843B，SHA256 `04c1702a6808992d4f419e9eb6edfaabf2a57c5625c57e7b9a6565d7445e51ca`。实际完整读§2/3含Lemma1完整证明、§5/T1–3、§6与F2/4直接caption、Appendix A/T4–7；未Related Work、图像素、外部实现或训练复现。

W0为n×m，拟合左右diagonal A/B，得到W'=AW0B、ΔW=AW0B−W0，只有n+m可训练数；A/B初始identity，初始forward匹配base。这是受限乘法适配而非LoRA低秩加法，ΔW可高秩并不表示nm自由度或可更新任意方向：W0的零元素仍为零，W0=I时所有可得W'仍diagonal，不能产生LoRA rank1也可表示的非对角项；非零矩形交叉比例也受原W0约束，且两缩放间有整体尺度冗余。对角缩放不是沿原SVD基逐个任意调奇异值，不能由高rank称所有正交语义方向都已有效利用。

Lemma1的rank(ΔW)≤min(2rank(W0),n,m)由rank和不等式成立；但后文“归一Δrank/rank(W0)一定在[0,1]”不由它推出。直接有限例W0=[[1,1],[1,1]]、A=B=diag(1,2)，W'=[[1,2],[2,4]]仍rank1，Δ=[[0,1],[1,3]]的det=-1、rank2，故归一比可为2。原实验W0高rank时可能≤1，却不是一般定理；σ≥.01阈值也依赖尺度，不等普遍有效rank或性能原因。保所见rank证据，不由此否定该适配分支或私修全部理论。

T1 RoBERTa355M六GLUE任务，Hyper .2M参数均分86.4，LoRA .8M为87.8、FullFT88.2；部分baseline引用旧工作，Hyper五seed均值/SD不能自动使所有方法同环境配对。T2 Llama8B数学Hyper75.5<LoRA76.7但>rank1的66；Qwen7B的Hyper86.9反低于rank1的87，不能照录“同预算总胜rank1”。T3 Llama常识81.3比LoRA84.3低3点，Phi常识与rank1同87.9；较少训练参数是一项真实trade-off，不是相同质量普遍降本。早发布模型可能较少污染只是作者猜测，没有独立污染证据。

数学Math10K/seq512/batch256/3epoch，常识170K/seq256/batch128/2epoch；Hyper LR.003与LoRA .0001/r32/alpha64/dropout.05不同，目标Q/K/V/O/Gate/Up/Down，不能把差额完全归rank。测试temp.05/top-p.4/top-k40、数学max512/常识32；硬件、完整dtype/峰值显存/真实step或Serving时延、LLM多seedCI与全调参预算未充分披露。n+m参数不免除base读取和反传activations；静态预合并可免额外adapter运算，却要生成/存储/加载该task权重，多adapter动态切换并非本文已验证零开销。

数据制备、全部适配训练/搜索、base与activation、两侧缩放或合并副本、加载/切换、rank诊断及独立原能力/任务回归均计费。可保留长期命题为**参数效率约束可以放在变换族而非ΔW的rank，但rank、可达更新集合和任务质量须分开比较**。原方向不支持目标任务、缩放失稳或质量退步时保LoRA/更高rank、受控全量更新及已有base，不用高rank签泛化、保知识或低Serving成本。当前owner是否具体已有覆盖仍writer新层，不预I/NC。

## A78新增首必要：19189 Functional Scaling Laws

[精确v1](https://arxiv.org/html/2509.19189v1)原件 `ROOT_NECESSARY_19189_HTMLv1_20261025.raw` / request，2026-10-25T08:40:15～08:40:32Z真实200/exit0、1447547B，SHA256 `e8507257f933ce25c5e115deca264035b5772446044613ef94aa73a1e7f97822`。实际完整读§2–7、Assumptions2.1–2.3/5.1、Lemma2.4、Theorems4.1/5.2–5.4与式1–9、Appendix B.2/B.3含实用ansatz/拟合/PGD、F1–10直接caption；针对已见假设冲突另定点读LemmaE.1及噪声协方差证明、C.3误差SDE段。**未独核C/D全套定理证明或全部E辅助引理、曲线像素、代码或训练复现**，不将64页全部附件变队列。R51日期/准入/原6不重。

可核核心接口是将连续训练步τ换为累计学习率时间t=∫φdτ；在相应SDE近似中，drift在t下规范化，噪声强度由hφ/b控制。相同末学习率或相同token数不等相同累计进度/噪声注入历史，后期衰减既减少新噪声，也留有限时间消化早期误差。增大batch在固定步数和LR时并不会自动减少t，只有固定数据预算使可做步数改变时才有那项取舍；不照录“较大batch本身缩短内禀时间”的无条件解释。φ有零平台/终点时T逆的定义也须限定，不把time-change作为任意离散AdamW轨迹的恒等变换。

理论对象是固定teacher/student kernel平方损失、fresh iid在线minibatch SGD、独立Gaussian标签噪声、零初始化，只训练投影后的线性readout；M为feature数，β>1为特征谱衰减、s为teacher相对光滑度，并非直接测出的真实LLM参数/能力维度。Theorem4.1只在top-M的0<s≤2−1/β及足够大M/t，random-feature另0≤s≤1及其随机投影概率范围，给up-to-constants的SDE平均population excess risk分解，不是每seed训练loss或完整LLM理论。forgetting kernel只描述该模型的优化噪声消退，不等知识遗忘、语义memory或数据隐私擦除。

打印假设有具体不一致，不能签全套定理已证：Assumption2.1左右写tr(HA)A，而LemmaE.1的Gaussian恒等与后续噪声证明实际消费tr(HA)H。取H=I2、A=diag(1,0)，Gaussian四阶矩减HAH为diag(2,1)，不可能被任意C2·diag(1,0)PSD上界控制；E.1用H的恒等本身与此相符。只保该具名差额，不悄悄改假设再声称原打印定理成立。§4解释性ODE又把NxN的WᵀWH乘M维ν且缺teacher驱动；Appendix用N维误差u=Wᵀν−θ*才是不同变量，不能用零初始齐次ν方程重建真实学习。§5.2先定义a峰/b末，却又印a=b/K，与随后T=a(K−1)/logK所需的b=a/K相反；不补成无歧义完整schedule recipe。

§6.1/B.2的128维、σ3、B1、200次SGD是该模型内的有限检验；三系数OLS拟合均值轨迹与理论趋势实验分清，不将用FSL数值生成曲线再与FSL比较当独立真实模型验证。LLM实验是另一个**经验surrogate**：400M/1B LLaMA、20Btokens，从8-1-1 loss拟合后预测WSD/cosine；QwenMoE1B、batch288/33907step/20Btokens，先拟合再搜索单调schedule并重训比较。Appendix还报告100M–1B/10B–80B等有限扩展与部分caption约.01loss差，不等巨型预训/下游能力、跨数据分布或可靠性提升。

B.3从核积分到九参数ansatz多次近似，不是精确从SDE推得的LLM loss；单一固定M轨迹中L0与c2*M^(−sβ)均为常数，不能据该拟合独立识别全局模型容量指数或预测任意模型扩规模。10k步拟合、50k–100k PGD及其LR搜索、先验8-1-1训练和最终全部schedule训练都付费；所谓相同20B重训预算不含所有方法制备和选择成本。hardware/dtype、真实总GPUh、LLM独立seedCI、全部数据/optimizer协议在本域未充分披露；无代码/曲线像素核验，不给精确收益或SDE→离散SGD误差界。保持原benchmark/预算边界，不把σ=0/有限谱与未验证强假设外推到一切训练。

可保的是**规模规律还受schedule路径影响；把累计进度与历史噪声分账，经验拟合可作为候选schedule提案，但须独立同预算重训与任务回归**。理论完整性与实验surrogate资格分层，假设打印冲突不抹去已读经验设计，但不进入书稿强理论保证。数据、optimizer/精度或预算失配时保已验cosine/WSD、有限小模型对照和外部停止/安全检查；预测较低loss不授任意任务最优或未发生失败。

这两项root首有限必要已备且请求全部结束，交Singer唯一另一角色回有限原域实际采用及具体反侧；Sartre随后角色/范围复用，不第三相同Methods/GET。原分/日门、当前owner与最终Books判断互不代替；不要求为未采用的全套强定理另审全部附录，也不将尚可执行的已具名差额改成外部阻塞。

## A92新增首必要：18542 Symphony-MoE

root明确接受此前未开始的首必要，R51日期/准入/原6沿用。[精确v1 HTML](https://arxiv.org/html/2509.18542v1)原件 `ROOT_NECESSARY_18542_HTMLv1_20261025.raw` / request，2026-10-25T09:20:08～09:20:09Z真实200/exit0、162357B，SHA256 `aa1d688d7c9ae5541d9118728655b1285954303b3006b1b7fbd52244439c70e4`。实际完整读§3/式1–4、§4/T1–3与直接图caption及§5限制；未全Related Work、图像素、源码或训练复现。因正文多次转引关键Appendix而HTML未提供，另实际取[同v1 PDF](https://arxiv.org/pdf/2509.18542v1)，09:26:54～09:26:58Z真实200/exit0、637420B、SHA256 `0ee70ace6969b465c1637593db845cca2e591459bde644064ce0d3e40710627e`，原件 `ROOT_NECESSARY_18542_PDFv1_20261025.raw`。PDF9页，机械定位Appendix只见p4–6正文引用、p9为参考文献，没有取得所许成本/配置/额外Llama结果附录；不把定位称全文证明已读，也不将当前HTML完整等同附件齐全。

论文先按层类型合并共享backbone：共同token平均/独有token保留，Attention用SLERP，norm线性平均；各源FFN保为独立expert。用各领域5%校准数据的中间激活对anchor做Hungarian neuron matching，再成对重排up/down；之后冻结backbone/experts，只训练top2 linear router，LM+0.01balance loss，没有真实token→expert职责标签。来源限同架构，当前主要Qwen2/2.5 0.5B/1.5B各四领域派生模型，不是可任意拼接不同宽度、tokenizer或残差空间的模型。

**中心因果桥需要澄清，不正面采用“上述置换已经解决专家功能/参数空间不兼容”。** 对文中普通FFN的row-vector写法，E(x)=σ(xU)D；按其式3置U'=UP、D'=PᵀD，则对逐元素σ有σ(xUP)PᵀD=σ(xU)D，所有输入的expert函数完全不变。这保持了合法内部重命名，却没有旋转expert的residual输入/输出坐标；experts若始终分别保留，router看到的各E_i(x)也不变，相同router初始化/训练数据下其输出及梯度不能仅因这个重命名变成另一功能系统。有限例U=I2、D=diag(2,3)、P交换两列，x=(1,2)在ReLU下前后输出都(2,6)；不靠实际模型实验即可核对。标准linear CKA亦对特征列的正交置换不变，若图中差额来自其他forward或数据变化，须说清它，而非把内部matching自身作为功能specialization因果证据。

若实际SwiGLU没有同步置换gate/bias，则不再是声明的function-preserving变换；当前式3没有完整给出它们，不能私补算法后替作者证明。这个反侧不证明所有upcycling无效、表格虚构或组合模型不可能有收益；它只隔离当前**重命名→改变独立专家函数/路由可分性**的强桥。可接受的重开材料是明确实际重参数化（含gate/bias、输入输出基及shared融合中具体作用位置）和只改该操作的配对控制，不要求为了排假想情况审完整代码史。

作者T1/2整体组合平均优于所列MoE baselines，但0.5B HumanEval28.02低于code expert28.71，1.5B MMLU58.91低于general59.57，不能称所有知识/任务无损保留。T3去alignment的33.94/26.92与full44.07/35.26为作者整体对照；在上述不变性未解前，不能把全部落差归因该成对置换。SLERP/embedding/calibration每项变化亦不是通用优越定理；anchor试验/专家按固定顺序增加会改变领域和容量，不能作任意anchor或更多expert单调收益保证。OOD仅MedCQA任务分数，既不认证医学能力，也不由此证明fundamental reasoning或跨领域安全。

8V100、dense SFT2epoch；校准10.404Mtoken又用于router，cutoff2048/batch2/6epoch/LR5e-5/AdamW，缺完整precision、matching开销/存储峰、总训练token配平、独立多seedCI与端到端推理时延。表中±未交代为独立训练seed统计，不私定。训练free只修饰stage1“不更新权重的matching”，不免去校准全源forward、激活存储、assignment及后续router训练；多套源模型的预训练/SFT、融合、matching、全部expert容量、router/通信与全质量回归都计费。当前建议保原候选/分数、中心采用争议而非降分或删反例；只借用已有MoE/模型合并通则不能冒原文已验证的新长期机制，具体Books处置由writer按该采用边界判断。

## A92新增首必要：18787 AGNTCY Directory

[精确v1](https://arxiv.org/html/2509.18787v1)原件 `ROOT_NECESSARY_18787_HTMLv1_20261025.raw` / request，2026-10-25T09:20:09～09:20:10Z真实200/exit0、265559B，SHA256 `d706926537c8fafa434292d2005582914694f08d28192730d18e39010cb895b3`。实际完整读§3–8/序列图caption/存储与查询表、§10的已实现/未来界；不核全Related Work、外部OCI/DHT/Sigstore规范、全部SDK/项目代码或部署，不据“reference implementation”宣称已运行。R51日期/准入及原6不重。

拟保机制是分离两类变化：capability/taxonomy key→不可变的record CID集合，与CID→当前可取内容的registry endpoints；搬迁或复制只改第二层locator，不必重写大capability index。Record/index/delta/referrer分别作为OCI artifacts，签名/评价是独立referrer而非篡改原record；发布先push object及index，再公告索引与locator，取回后验证digest/所需签名，再由本地policy筛选。它提出的是发现/取件接口，不是Agent推理能力被证明、远端运行已授权或任务结果真实。

跨dimension按sorted posting lists相交有O(各list长度和)本地工作量，DHT查询/完整list拉取/解压/核验/后rank另费；要求skill不提供任意热门skill结果大小的硬上界。**缺domain index时将其当universal**会放宽显式过滤，不能把这样的结果仍称满足所有mandatory域约束；near-miss建议更应与严格命中分开，不直接授权限。不可变CID只保对象bytes，latest-index选择、supersession/删除和locator仍可stale；负delta不允许，移除须新pruned index，需明确读者采用哪个epoch。断网或旧缓存不能证明Agent依然可用/评价未撤回，负cache TTL又可能掩盖恢复。

内容哈希是完整性而非可信root：若恶意peer同时给出伪能力record及其自洽新CID/index，digest全部可匹配，不靠mismatch自动发现伪能力。即使签名有效，也只支持身份/内容关联，不证明标签、benchmark、实时SLO或调用授权；可选签名与honest-but-curious DHT假设不能升级对Sybil、索引投毒、回放或metadata隐私的完整防护。客户端须另核可信publisher/index、epoch/撤回、评价协议及作用范围，这些是项目推导的验收条件，不冒原文已全部实现。Sigstore/OIDC仍有信任根，不能把“去中心”说成无可信机构；current signature流程及媒体类型有illustrative/future用语，不抄成现行标准兼容配方。

§7是设计/估算，没有实测benchmark人口、hardware、QPS/并发、p95/故障恢复或总费；“list占>60%则近线性改善”“常>5:1压缩”不是受控实验结果，digest随机性也不保证delta编码总高度压缩。F(Lo−Lr)>kBCt两边的频率/时间与货币单位没有声明统一效用换算，不能当通用复制break-even判据。first-byte/manifest时间不是完整usable artifact/Agent调用延迟。Bloom/XOR prefilter只有相应集合语义正确时可省完整拉取，假阳性仍回真实内容核验，不由filter“可能有”批准能力或执行。

原文明确代价：复制付存储与egress、长尾cold miss、delta顺序/完整snapshot恢复、taxonomy版本/未知namespace、跨域权限及缓存失效；encrypted referrer、strongDHT硬化、复杂ranking等仍future。全部record/标签/评价制备与签名、索引构建/同步、posting传输与交集、对象拉取/核验、replica维护与调用前独立资格验收都计费。可保长期consumer为**能力身份、分发位置、发布者来源和实际调用资格分层，稳定内容寻址不使可变发现状态自然一致**；负例/新schema/信任或新鲜度不合时，保固定可信目录/本地已验小池、重新查询及明确不委派，不从检索结果自授effect。当前owner/已有覆盖或小gap仍writer新层，不预I或生产能力。

两首必要均已完成有限准备、无请求在途，交Singer唯一另一角色回上述必要原域实际采用及关键反侧；Sartre随后只角色/范围复用，不第三相同Methods/GET。中心争议与有限架构正侧分开，不用访问/实现缺失直接否定所有paper价值，也不以准备完成代日报DAY/FINAL。
