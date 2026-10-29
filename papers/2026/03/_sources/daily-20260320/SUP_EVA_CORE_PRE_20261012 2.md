# EVA17808：生成轨迹的IDM动作代理反馈 / 必要准备

resume_review17_18 sole准备，2026-10-12，仅03-20补03-19。author明确未读本core，原准入/day与2+2+2=6有效复用；current题名增加EVA前缀但同六作者/完整AB。不自授Source/PRE、safe或DAY，交author一次非准备者核；没有Books授权不写正文。

## 1. 实际必要原证与停止

[exact-v1](https://arxiv.org/html/2603.17808v1)完整AB/关键引言L47–80，必要§3.2–4/Eqs2–9 L101–143（117初返回局部截断已同v1必要回读补齐）、§5.1–5.6/T1–4及直接限制L144–219；B reward-validity L304–309、C训练与reward-hacking L310–321、D IDM直接消融 L322–329、E1平台/规格L330–350实际读。只偶然返回部分E2/F文本，不授全部附录或零样本合成执行。current abs8–29实际轻量读，v2仅项目页Comments/相同AB无具体重要纠错说明，不以版本本身展开全diff。未读代码/全部图像像素、参考文献、精确部署recipe或复现。支持有限接口和直接反側足即停，不扩query。

## 2. 机制与不可授桥

真实机器人轨迹监督训练IDM，短时间窗以卷积/空间softmax/MLP恢复关节命令；视频生成器后训练时冻结IDM，由它读取**生成**帧序列并提出关节命令，再对时间差分的加速度/jerk作Huber惩罚，对速度/加速度超限作平方惩罚，组合为reward，更新视频模型LoRA。这把下游解码接口前移为生成器训练反馈，不是对真实动作直接施加硬限制，也不是生成视频获得外部接触/任务真值。

Eq7直接只给速度/加速度边界，不能读成完整关节位置/碰撞/力矩约束。恒定动作使差分惩罚为零但可不达目标，是reader条件反例；C原文明确长期优化可出现静止、错误接触与link-length伪影等高reward退化，并以validation质量/执行结果选checkpoint及早停。§6未建模force/friction/torque；因而本分支不能授任务完成、完整物理可执行、安全或奖励永远有效。T4真实视频上IDM成功89.52%也不证明合成OOD上的奖励可靠，B仅三任务每组10条的相关性切片，不是完整检出率/因果验证。

Eq9在非负惩罚、正P0/γ条件下取(0,1]，Figure2 caption却报7.94/3.04，缩放关系未披露；不采用精确reward尺度/可直接执行配方。一次必要请求仅实际reward缩放、时间间隔/动作单位及含静止/接触错误的独立验证与选择协议，不重读全版本/代码库。公开限制不使有限机制整体EX或降分。

## 3. 关键评价 / 反退 / 全费用

Wan2.1-14B/LVP经本体SFT再GRPO，IDM冻结；8 A800、rank32、每prompt8rollouts、batch32。RoboTwin21任务每task50demo/共1050，评价210prompts有held-out paraphrase；基线单task、EVA多task，不能把同per-task demo当所有参数/预训练/总训练费公平。T1 human rubric将视觉Perfect与实际执行分开，instruction90.5→89.5；T2 StampSeal5/20→4/20，不能照录consistent各任务提高。T3真机五seen/五OOD、各20trial，成功需无安全中断/人工介入，仅所测本体支持，不能批准任意真实任务。

C bf16 SFT含49帧/两种分辨率，后GRPO模拟约6天/136steps、真机约3天/46steps，均新增费用；预训练、IDM数据/训练、采样、判分、验证选择及回归都付费。receding-horizon每段后用最新四相机帧重新生成，不意味着连续fresh控制；§6明确昂贵生成限制高频反应。完整pipeline latency、采样/执行chunk与控制频率、并发/SLO、奖励阈值/单位和统计CI在本必要范围Not Disclosed，不采实时、免费或严格可复现recipe。

## 4. actual sole owner / 两literal PRE

sole `MULTIMODAL-WORLD-MODELS`，[Ch25](../../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)：实际完整1084–1143 persistent-state/GT-prompt recovery→受限invariant-verifier→GUI delta与后续control-relevant监督已读；Ch25入口1–18、Ch24入口1–23及Ch26入口1–32/107–119实际交接。先误猜25-world-models路径读取失败，已按ROADMAP恢复正确文件，不冒失败读过。现有inverse anti-collapse/双likelihood互验与cycle-invariant不同于真实动作IDM输出差分代价反馈上游视频生成器的具体回路；不另建机器人章节，不复制GRPO推导，实际提交仍Ch26。

拟原1107“World Model训练常缺少…”完整段后、GUI typed delta完整段前，两短段+静态源注；author可根据实际全文具体NC/收窄，不由主题映射自动整合。

真实未来标签缺失时，另一个受限训练反馈来自生成轨迹的下游动作解码：先用真实机器人轨迹训练 inverse dynamics model，再冻结它，从生成视频的短时间窗提出关节命令；以这些命令的时间差分构造平滑度与速度、加速度超限代价，反馈给视频生成器的后训练。它改变的是上游 proposal 的训练选择压力，不是替真实 controller 增加硬约束。[有限本体对照](https://arxiv.org/html/2603.17808v1)只支持这一接口：IDM、动作单位、采样时间间隔和本体限值共同决定 reward，来自真实示教的解码成功也不认证生成分布上的所有动作。<!-- source-family:SF-2026-ARXIV-2603-17808 -->

平滑与任务正确仍须分验：不动也可能取得高分，接触错误、连杆伪影或错误目标并不由速度代价排除；原训练实际出现高 reward 退化，需用独立 rollout 质量与执行结果选 checkpoint 和早停。奖励不包括完整接触动力学，部分指令或任务切片反退，不能把代理优化写成物理安全或无损对齐。IDM数据与训练、视频采样、判分、后训练和选择回归均付费，昂贵生成也不能兑现高频 fresh-control deadline。信号失配或执行风险上升时，保留本体示教/未对齐生成器、短 horizon 重观测与独立 controller/停机接管，不让高 reward 接管动作提交权。<!-- source-family:SF-2026-ARXIV-2603-17808 -->

静态源注：

- `SF-2026-ARXIV-2603-17808` — [EVA exact-v1](https://arxiv.org/html/2603.17808v1)必要§4/Eq3–9、§5/T1–4/§6及B/C/D/E1直接反側。仅真实轨迹IDM→生成帧动作差分代价→视频后训练的有限反馈；保静止/接触reward-hacking、IDM支持域、任务反退、reward尺度未闭合及全费用/时序边界。不授硬控制、安全、完整recipe或高频保证；未核代码/全部像素或复现。

## 5. 待非准备者裁

交resume_mar17必要Source/actualowner/两literal/static有限独核，不自计safe或DAY，不写Report/LS。只该原候选，支持与直接反側足即止。

## 6. Root sole 窄授权后的 writer 实际写入

2026-10-12 root实际读本packet/author§5及现Ch25后明确授本family sole Ch25窄写。resume_review17_18按批准原两literal写入1109/1111和静态1767；实际完整1091–1134与末1757–1767本人/相邻注顺读，invariant→IDM反馈→GUI delta衔接、原两段和source边界一致。scoped diff仅本family两段/一static共6新增行，chapter diff-check无输出。writer读回不是POST/safe/DAY，交author一次非writer实际完整1091–1134/1757–1767复核，不再改静态身份。

2026-10-12 resume_mar17非preparer必要Source/actualowner/两literal与static有限PASS。实际独读exact-v1 §3.2/§4/Eq2–9 L101–143、§5设置/T1–4/执行与失效L144–219，B/C/D/E1直接反侧L304–350；current abs同六作者/v2项目说明轻量实际读，无采用相关具体纠错，不机械diff或全附件。actual Ch25完整1084–1143及Ch24/26入口与行动提交交接实际读。冻结IDM从生成视频提出命令，其时间差分/超限代价反馈视频模型LoRA，不是硬控制；constant命令差分代价为零但可不达任务、C静止/错接触/link伪影原证及early-stop/独立执行选择真实。T1指令90.5→89.5、T2 StampSeal5→4、T4 GT-video89.52%不授生成OOD可靠性，Eq9条件范围与caption7.94尺度不闭合均近文。原cycle-recovery/invariant检查不具体承载下游IDM反馈上游生成器的接口，sole Ch25原1107完整后两段成立，原6不变；本人static必要范围/未核代码或像素/复现准确。未写未POST不计safe或DAY，交root窄ownership协调；不改原PRE或复制验收身份入Books。

## 7. 一次非 writer actual POST

2026-10-12 resume_mar17实际完整读回Ch25 1091–1134及1757–1767本人/邻注，新正文1109/1111逐字回对本包两literal PRE与已核必要原证。Persistent state/GT-cycle recovery→受限invariant→IDM差分代价反馈→GUI typed delta→control-relevant监督邻接完整。IDM解码支持域、静止/接触reward-hacking、部分任务反退、全费用和高频控制不保证近文保留；未把代理反馈授为硬约束或真实物理证书。本人静态1767引用/必要范围/未核代码及复现正确，邻Stereo/Kinema/DreamPlan源注未改变。有限POST PASS，交root接纳及释放本family Ch25锁；无需再改Books身份或重复Source，不授本日DAY。
