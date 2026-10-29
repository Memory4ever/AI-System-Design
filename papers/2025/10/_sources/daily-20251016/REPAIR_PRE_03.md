# 第三包：writer首必要与具体Books提案

未SAVE，仅sole reader整体PRE/NC后才写；不全章锁。Books规则与ROADMAP及actualowner/完整局部/相邻交接已读，保护并发正文/注/index。

## 12633 Laminar / 2+2+2=6 / TRAIN-GRPO

actual精确v1 §3–5、§8设置/8.1/8.2/8.4，完整必要支持/反侧已读。CPU master接trainer权重后reshard、RDMA pipeline到每rollout机CPU relay，rollout独立拉取；partial/complete trajectory分池。repack仅同weight-version cohort，KV容量与roofline batch双guard，搬未完成轨迹后释放source再装新权重。不是无偏、零stale或任意故障隔离。128node/1024H80080GB、8×400Gbps、Qwen2.5 7/32/72B、2K/16K、512prompt×16/G8192/16mini/最多8tool，throughput五iteration after十warmup，非heldout能力或生产SLO。AReaL使用不同backend/训练栈与不同stale设置，不能把倍率唯一归relay。T1 repack max828s>w/o826s，平均更快不支持所有轨迹无延迟增加；状态池/CPU/RDMA传输与恢复全费。

actual Ch33“Rollout变成服务”已有环境/policy epoch/admission/失败与RLHFless迁移分责，但未承担**trainer发布、relay可得、rollout实际安装三时钟**及同版cohort约束。拟在该节首段（“当 rollout 延迟…”完整段）后、原“Rollout 服务也可借用在线推理的暂时空闲资源”段前加一段。

正文：

权重服务还应分开三只时钟：trainer已提交新参数、host relay已收到完整可读副本，以及某个rollout真正安装该版本。可先把权重交给CPU master重分片，再向各生成节点的CPU relay传播，让rollout在自己的安装边界取用，而不让每次发布等待所有生成者。[受限异步实现](https://arxiv.org/html/2510.12633v1)还把未完成轨迹只在同权重版本组内repack，按目标KV容量和可承受decode batch共同判断搬运资格；同版仅是必要条件，缓存布局、位置与完整状态仍要核验。发布完成不让旧轨迹自动变on-policy，释放生成资源也不批准trainer接纳陈旧或不完整group。Relay/版本驻留、部分轨迹池、迁移与失败恢复均付费，平均提速仍可伴最长轨迹变慢；副本未就绪、版本/状态失配或收益不抵搬运时，保留原生成者、完整权重快照和同步交付，不由后台传输批准无偏训练或全故障无损恢复。

独立marker：`<!-- source-family:SF-2025-ARXIV-2510-12633 -->`

本人末注：

- `SF-2025-ARXIV-2510-12633` — Herschel，Daily2025-10-16补Oct15；[exact-v1](https://arxiv.org/html/2510.12633v1) §3–5/§8设置/8.1–8.2/8.4必要，2+2+2=6。仅发布/relay可得/安装三时钟与同版本repack双容量guard；保陈旧/完整group、异栈对照、max延迟反侧及全费，不采无偏/任意容错/净倍率。未核代码/复现；整体PRE/真实SAVE/完整自读/sole actualPOST据本日canonical实际后到层。

## 12635 MemAct / 2+2+2=6 / TRAIN-GRPO 具体已有覆盖提案

actual exact-v1 §2.1–2.3/Alg1、§3.1–3.4/T1完整必要：memory编辑破坏append-only，按编辑边界恢复各段实际生成history，只mask新token，整trajectory advantage分给采样segments。prompt内round-robin Nseg/Ntraj与group std=0 guard未闭不补recipe；继承终奖不证明每段独立成功或无偏。DeepSeekV3.1生成成功traj制SFT，6epochs/之后8traj16segment/35toolturn/H100，Input成本/Function Calls不含内部memory动作；RL多hop均分.567仍低SearchR1 .572，不采普胜/完整净成本。

actual Ch33:372 SUPO完整现文明确“旧history动作不能换summary条件作on-policy”“共享原reward多段不是独立样本”“采样history/summary版本/旧policy重算/mask归约”与费用/完整history退路，紧邻上下段亦读。本次可采用的fracture/实际conditioning/mask/终奖身份被同一具体论证承载；MemAct的round-robin recipe未采，故不追加正文/marker/注，拟具体NC。不是因为名字相似或普通没读。

## 12773 Dr.LLM / 2+1+2=5 / MODEL-LAYER

actual精确v1 §3–5/§6.1/完整T4及§6.5相关：冻结base，每layer小MLP读window pooled前层hidden提出skip/execute/repeat一次；MCTS离线按gold找短正确path→focal监督，train时teacher-forced路由/推理greedy。数据4K来自约961K forwards不免费，原Alg空π/成功条件不补完整recipe。A10040GB/BF16/router4h与offline search预算分开；模型LLaMA3.2-8B族标记与8B身份不齐，Table4 OOD多退、6.3净时间未采用，不将所有accuracy/layer变化作一般LLM保证。KV共享/重复层正确性未有完整证明，不采fully compatible原断言。

Ch17已有对计算过的residual更新插值及跨层history读取，但没有把**执行零/一/两次block**和**只改已计算更新幅度**分清。唯一MODEL-LAYER，插于原“Residual不能保证任意深网络稳定，却显著改变了优化条件。”后、原“保留 identity 也允许对已经计算出的层更新…”完整段前（源码原句整行须按实际读到的“即使…”所在完整段定位），不修改公式/原段。

正文：

恒等路径还允许选择是否执行整个block，而不只在执行后缩小更新：冻结旧权重，让轻量router读取前层状态，为本层提出跳过、执行一次或重复一次，得到输入相关的有限深度路径。[受限监督路由分支](https://arxiv.org/html/2510.12773v1)用离线搜索出的正确路径教router，这些标签依赖已知答案和搜索人口，不是线上最优路径真值；训练时按标签执行、部署时按自身决定执行，也会改变后层router看到的状态。重复同一block不等免费增加新知识，跳过也不保持原模型函数；路径、router和每次block调用的KV身份须共同验收，不能从相同hidden shape推出缓存兼容。全部离线搜索、router训练/读取及重复计算均付费，域外质量有反退；路径、缓存或总预算不合时，保留原单次完整层栈与独立质量检查，不由较少平均执行层或冻权重批准无损和净加速。

独立marker：`<!-- source-family:SF-2025-ARXIV-2510-12773 -->`

本人末注：

- `SF-2025-ARXIV-2510-12773` — Herschel，Daily2025-10-16补Oct15；[exact-v1](https://arxiv.org/html/2510.12773v1) §3–5/6.1/T4/6.5必要，2+1+2=5，block执行身份差额深入。仅零/一/两次执行与已计算residual缩放分责；保gold搜索/teacher forcing、KV未闭、模型身份与OOD反退/全费，不采无损或普遍缓存兼容。未核代码/复现；整体PRE/真实SAVE/完整自读/sole actualPOST只本日canonical实际后到层。

## 12586 Pixel Space / 2+2+2=6 / MULTIMODAL-GENERATIVE-PARADIGMS

actual exact-v1 §3–4设置/4.1–4.2相关、AppendixC完整T10–11：clean-view contrast与同PF-ODE轨迹邻时刻representation consistency预训encoder，去projector后接随机decoder end-to-end pixel去噪/一致性训练；后者另以冻结预训encoder评输出/clean给辅助对比目标。不是后版There is No VAE，也不把VAE完全过时。预训600K/480ep＋finetune1M/800ep DM或700K/560ep CM，FP16/ImageNet/8H200预训费用均入账；作者因预训小时低于一次sdVAE训练而比较表只记finetune，不等matched生命周期预算。C中温度固定.1的CM46.44优于推荐schedule46.99；loss去除消融支持局部路径，不证明语义真实或所有flow时钟可直接复用。无复现/代码核。

actual Ch24 RAE段已有“冻结语义latent生产+单独decoder/denoiser”替代VAE，但不承担**为pixel denoiser预训可读噪声表征、随后端到端更新而非固定latent空间**。唯一Ch24，插于现有RAE完整段及SF-2025-ARXIV-2510-11690独立marker之后、下一个原段之前；writer写前fresh核完整邻接，reader须整体核本完整稿/marker/注。

正文：

也可以不把去噪过程移到固定latent，而先为像素去噪器预训可在不同噪声时刻读取的encoder：一边对clean增强视图做对比学习，一边约束同一预设轨迹相邻时刻的表示，再去掉projector、接新decoder并端到端训练像素输出。[受限像素生成分支](https://arxiv.org/html/2510.12586v1)因此不同于冻结语义encoder后学习另一份latent动力学；一致性训练还可用冻结的预训encoder提供辅助读数，但同源feature接近不认证像素细节、语义真值或任意轨迹保真。噪声日程/时钟、对比人口、温度及冻结/更新阶段须一起保存，不能把一条温度schedule当全部配置的稳定保证。预训、完整去噪/一致性适配、辅助encoder和guidance/采样全计费，省去VAE资产不等省去表示训练；表征、像素质量或总预算不合时，保留重构VAE、已验latent路径或原像素训练，不由较好FID或一次预训小时比较批准普遍替代和净加速。

独立marker：`<!-- source-family:SF-2025-ARXIV-2510-12586 -->`

本人末注：

- `SF-2025-ARXIV-2510-12586` — Herschel，Daily2025-10-16补Oct15；[exact-v1](https://arxiv.org/html/2510.12586v1) §3–4相关/C完整T10–11，2+2+2=6。仅噪声可读encoder预训后端到端pixel生成与固定latent分工；保同源辅助/温度反侧/阶段时钟与全生命周期费，不借后v2/v3改名或采普遍VAE替代/净速。未核代码/复现；整体PRE/真实SAVE/完整自读/sole actualPOST只本日canonical实际后到层。

## 12245 MoRA / 2+2+2=6 / TRAIN-LORA 具体NC提案

完整消费R6必要/旧SIDE有效层，未重复Methods。actual Ch30“条件适配还可以改变权重本身…”/“条件生成器还可以直接读取指令的token结构…”及后续BΦA跨模态生成三完整段，已承担冻结base、由输入经hypernetwork生成临时增量、不能静态merge、generator/packing成本和旧新消费者分验。MoRA把输入换graph nodes、learned queries生成instance A/shared B，是已覆盖的条件增量carrier实例；本次不采用化学性能或qkvof未闭recipe，Table4冻base仍旧能力退步也被现有双侧回归论点覆盖。拟具体NC，不改书、不因分子场景改C。

## 12217 HALF — 最低决定域完成，C撤回为窄P提案

actual §5/§6.3.1–6.3.3：并非只新severity分组。原有6200+ SAD空拒答被低fairness计入，作者自己承认failure是safety filtering而非直接demographic bias；同一“fairness”标量混合拒答coverage与有效回答偏差，可改变测量解释。o4mini与三standard平均跨医疗/教育方向反转不隔离reasoning因果，3.2-1/3与3.1-8更非controlled scale，不采用原因归结。最低层足，改P：2+1+2=5，PLATFORM-EVALUATION-SYSTEM，后续只读取需要的score/invalid规则及actualowner。当前不能把普通待核转H，也尚未签Books处置。
