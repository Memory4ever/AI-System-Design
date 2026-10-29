# FutureVLA 2603.10712v1：最小必要 Source / actual Ch26 / 受限 PRE ready

本日只补2026-03-12 BJT自然日。SUP_ABS3_10712原完整v1题摘/§19准入与§23/SUP_DATE3_10712日级夹证有效复用，十作者/唯一v1，本次实际回读current exact-v1 AB，无显示Comments/venue/撤回/纠错。SubmittedMar11T12:39:55不是公开日；registeredMar12与已核公告批次夹日，不追精确时分秒。

official exact-v1 https://arxiv.org/html/2603.10712v1 GET200/377346bytes/UTC2026-10-10T03:09:11.810752，SUP_CORE_10712.raw/txt/MANIFEST_RESULT保存。实际读§3.1–3.2完整机制/Eq1–7，§4.1–4.3正文及完整主Tables1–5、AppA1–A2完整实现/预算、A3直接Tables6–8/10/12–14、A4 Limitations，A6相关实机数据。图只读caption/正文描述，不认证像素或精确curve/Fig3与4–8数值，未采作者图中精准倍数/latent physical correlation，未展开全图/对比模型历史/代码。AppTable9与额外全样本、所有比较模型重实现细节非采用所需，不造blocked。一次bs4只读解析失败是本地未安装，已继续保存原txt读取，不安装依赖/不改共享文件。

## 实际增量与评分

单目标未来重建可能让teacher把背景/appearance也作为action-facing target→此稿把同一连续clip表示分为first-frame latent重建与action-chunk监督两流，只有motor分支查询visual，再固定clip teacher给当前观测VLA提供alignment target→需要选择何种target负责视觉保留、何种target消费未来动作时间，并分别验收teacher/student与真实控制，而不是以更多future帧自动证明motor纯度。

拟 **1+2+2=5**：D1计这一局部训练分工/条件化实现，不把cross-attention/gate/teacher distillation发明作重要新架构；R2计实际未来clip producer→当前观测student与action监督的跨训练责任；Durability2计可复用的重建target选择/未来特权与真实执行验收边界。不是借一般『teacher不等真值』抬分，具体T4/T5/T13改变是否只加多帧/如何选重建目标。actual长期具体gap触发受影响内容必要深入已完成；准备者不自签，score由非准备者实际核，若局部差额不成立不靠费用改判。

## 原协议可采用 / 不可补造

§3.1/AppA1 frozen WAN2.2 3D-VAE输入17连续224×224帧，需4N+1格式，输出1960×48；两层encoder后均分980 visual/980 motor。Visual三层Transformer仅监督重建first-frame VAE latent392×48，QueryPool+三层decoder；motor self-attention后作Q读取visual K/V，learnable scalar sigmoid gate条件化更新，迭代三次。两流之前同encoder已接完整futureclip，**first-frame target不使visual latent只含当前/静态信息，action supervision也不保证motor只含pure dynamics**，监督目标不等因果独立或物理真值。

动作监督16-chunk，OFT式两residual MLP的MAE或GR00T式FM；§3.2 teacher全部freeze，从futureclip抽Mf，而student只当前Ot+instruction，Transformer adapter把Fr→Fa，MSE alignment+actionloss，β后训cosine衰减。推理不读真实futureclip只是训练使用特权target，不等生成了真实future或每个动作可执行；adapter具体shape/removal与部署artifact未核，不声明逐步时间/零费用。

保留精确披露疑问、不补出可执行代码：Eq1第二行覆盖M'为cross-attention输出，第三行两项仍同M'，和文字『original motor+gated attended』不同；Eq5 Xτ=τX+(1−τ)ε但后文target ε−X，方向/solver约定未完整对回。本采用只描述正文/AppA一致的双目标、条件化与训练teacher/student分责，不继承精确gate公式/全FM recipe，也不由符号问题否定局部成功结果。

## 直接评价 / 反侧 / 预算

T4 WidowX GT去alignment→加alignment均值62.5→71.9；OT54.2→63.6，但**PutCarrot58.3→54.2反退**。T5 GT基线62.5；只有多帧motor58.4反退；加visual独立监督65.6；再条件化71.9。StackCube却从无交互37.5降到条件化29.2；这支持局部bundle/操作点，不证gate每任务必要或visual domination已消除。T13 last-frame68.8/first71.9；逐行last75/75/29.2/95.8、first83.3/75/29.2/100，两项提高/两项相同，不能把first-frame『strictly necessary』或pure motor由均值提高证明。

完整T1–3支持所测Google/WidowX与LIBERO，非全部比较公平/安全：T2 GT/OT StackCube29.2/25均低GR00T-N1.5 57；T1Google VM GT Pick92.3低Villa-X98.7，OT Drawer55.6低π0 72.6；其他任务有所提高。T6 LIBERO-Plus OT Camera50.4低OFT56.4，Noise72.6低OFT75.8/π0 79；平均优势不补全部quality Pareto。T7同架构guidance GT VM Pick97.6→92.3、VA Drawer61.9→52.4，OT VA Drawer40.2→31.7，不能『consistent』写成每任务正向。T8LIBERO均值局部改善，语料有LIBERO不宣传全零样本未见环境。

T10 Franka四任务each75示教/共300、5Hz去static zero-actionframes，GT48.3→70/OT33.3→51.7，局部闭环成功有限；实机eval试次/seed/CI、完整控制时延/精确success evaluator可见必要段Not Disclosed，不从6.7%步进补造15trials。A4明确擦白板等接触任务只visual constraints不足，应增加触觉/force-torque；成功不等safe torque/力接触真值。没有读Fig3像素，不额外采用对外部baseline精确26.7%/强真实全保证。

AppA2 OXE+LIBERO15.6Mframes，single-view duplicate为two-view格式，action16；batch256 LR1e-5 warmup5000，pretrain约三天×16A100。后训Qwen3-VL-4B-Instruct、两action-head具体实现、warmup5000/βcosine，totalsteps/所有post费用/precision/concurrency/SLO未披露。T12 VQGAN3.53s/64.6→3D-VAE3.28s/71.9是teacher训练step/不同codec，不是在线controller latency或3D唯一收益。T14受扰embedding/action MSE较小只是代理对照，不证未知噪声全部不影响或pure physics。不同方法backbone与future监督budget有别，AppA3说统一reimplement却不补图所有配置为严格等资源。Encoder/teacher pretrain与forward、decoder重建、标签视频/动作、studentadapter和后训均计费；runtime仍有完整VLA/actionhead/controller。

## actual owner / 具体 gap

ROADMAP唯一MULTIMODAL-EMBODIED-VLA Ch26。实际顺读105–118 training-only3D teacher特权对象target→student/runtime动作分责；完整278–287 action-facing latent加性重建、forward/inverse两阶段预训练及其完整回退，并读相邻导航dynamic区域段入口与Ch25表示/预测章节入口。现文有『future重建不等真实action』『teacher可训练期前付』，但**没有本稿first-frame视觉target与16-action时间chunk分别监督、motor-only查询visual、冻结完整futureclip teacher→当前VLA的具体交接及T4/T5局部退步**。不是泛主题重复，不称新实验已被吸收；Ch23只交接3D-VAE shape，Ch25只交接环境预测资格，不新增另owner。

建议放在Ch26现forward/inverse两完整段（2604.16391）后、导航『重建完整未来特征也可能把大部分监督预算花在静态背景』前两段，与已有动作latent与decoder责任链共存。没有新结构。

## 逐字两段 PRE（root写前待独核）

有动作标注的未来视频也可以先支付监督分工，而不是只增加帧数或要求一个 latent 重建整段未来。一条受限训练分支将连续 clip 的编码分成两组：视觉组的重建目标是第一帧的 latent，motor 组预测对应 action chunk，并由 motor 查询视觉组、以可学习 gate 接入条件；预训练后固定这份 clip teacher，让只读当前观测与指令的 VLA 经适配表示拟合 teacher，同时继续动作监督。未来 clip 是训练期的特权 target，不是推理时可读取的真实未来；两流共享早期编码，监督分开也不能证明静态状态与纯 motor intent 已因果解耦。

[FutureVLA 的有限消融](https://arxiv.org/html/2603.10712v1#S4.SS3)中，只加多帧 motor 表示反而退步，分开重建与动作监督提高所测均值，再条件化进一步提高均值；加 guidance 的某些任务和 加入条件化的 StackCube 对照仍有反退，第一帧优于末帧的局部结果不证明所有任务都必须选第一帧。Teacher/codec 预训练、未来视频与动作标签、重建 decoder、冻结 teacher 前向及 student 后训练均计费，训练 step 时间不能当控制 deadline。Latent 相似度或受扰 MSE 也不认证物理真值，接触任务仍需真实反馈与 controller；动作或接触质量回归、特权 target 失配或完整预算不合算时，保留直接行为克隆、显式动作监督、原 policy 与独立低层校验，不以不改推理架构自签安全。<!-- source-family:SF-2026-ARXIV-2603-10712 -->

最小停点：必要支持/反侧与actual owner比较够，拟5分局部深入/PRE等待非准备者；未写Books/未formal/未DAY。不为所有图/全噪声或无代码扩永久请求。
