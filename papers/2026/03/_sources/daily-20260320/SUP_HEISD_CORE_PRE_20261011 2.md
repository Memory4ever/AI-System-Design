# HeiSD17573：必要原证 / actual owner / PRE

root准备，只接03-20补03-19自然日；准入与日级身份复用reader独核§12。2+2+2=6针对动作历史检索/learned draft切换、verify-skip与动作分组接受的条件接口，不给通用SD或机器人应用主题新分。未写Books、未自授通过或DAY。

## 必要 exact-v1 与直接反侧

[HTML](https://arxiv.org/html/2603.17573v1) §3–7/Eqs1–8/Alg1/Tables3–6，必要Appendix C.3/D/E.4的payload、时序与动作schema实际读；没有读全部图片/相关论文或核代码、复现。

- AR VLA七动作tokens的greedy输出是基准；检索历史图像相似action与小模型draft分支不同。过去窗口的curvature radius与累计displacement经训练suite min–95percentile裁剪归一后融合，提议下一步检索或drafter，不是未来真实trajectory的oracle。参数和suite归一身份须一起校准。
- 检索库按task分40 collections，frozen双view DINOv2/SigLIP视觉特征，payload含episode/step/action与三步next_actions，不能叫开放未知任务泛化或无离线示教。检索后相近lm-head feature可跳target verify，离线阈值/距离在任务结果后更新；跳过的proposal实际直接执行，保持target law的经典验收已被改变。
- XYZ组、rotation组与gripper单独构树；不同retrieval可混组但gripper不混，组index-bias和单token-bias允许偏差，gripper零偏差只是与reference一致，不证明接触安全。全链拒绝回target生成；该回退不补偿已经执行的动作。
- Alg1 minS=0同时要求minS>S>T、i+d范围及else写Bt=True不构成可直接抄用的自洽代码，正文不用它的精确更新recipe。训练/历史统计与代理接口可受限采用，不能把伪码当实现已验证。
- A100+Xeon4410T/OpenVLA/LIBERO4×10tasks每task50trials，Table3 HeiSD比AR Goal73<77、Spatial78<82.8、Long47<54.4，Object71<71.2；speed提高不证明同成功率Pareto。Table5只有hybrid1.05×，主要收益包含skip/relaxed（acceptance统计把未verify全算接受），不能把长AL当target正确率。
- 实机AgileX PIPER/10Hz示教，joint delta与绝对gripper schema另适配；三类有限任务Table4 SR均低于fine-tuned基线。训练drafter2A100×8h、DB/视觉编码/CPU↔GPU/检索/校准/实机collect与后训练均付费。§6.1“negligible (>100ms)”与Appendix5.13ms不能拼成完整deadline；Table6整批时间不授线上单step尾延迟。precision、服务batch/concurrency、完整control SLO及实机trials/不确定性ND。不采diffusion不能speculation等泛化文字，也不因速度批准actuation。

## Actual唯一 owner 与差额

`MULTIMODAL-EMBODIED-VLA` Ch26实际1320–1418：动作敏感压缩→gate freshness→提前退出/去噪/cache。Ch25/27开篇以及Ch48有损acceptance完整925–955实际读。现有gate与approximate SD没有解释**过去运动窗口选检索或drafter、跳验证/组容差改变动作生成reference合同**；物理consumer与错误执行边界由Ch26 owns，Ch48不再重写。

拟在Ch26闭环可靠性gate两段后、提前退出标题前两段，让“gate只提风险”自然接“历史运动proxy只能提速度路径”。

## 两段逐字 PRE（待非准备者）

完整 policy 逐步重算在接触状态复杂或动作不可逆时仍是可靠基线；动作片段高度重复后，还可在历史检索与小模型草稿之间选择。先从过去运动窗口估计曲率与累计位移，用经示教分布校准的代理提议本步走哪条路径，再从同任务历史 observation–action 记录取候选，或由 drafter 续写。这里历史轨迹与当前观测只是 proposal 的来源：窗口较直或视觉特征相近，不等于下一段动作已被环境认证。库的 task、encoder、action schema、轨迹位置与归一化参数共同构成消费身份；任务失配、突变或接触阶段不能沿用旧窗口的路由判断。<!-- source-family:SF-2026-ARXIV-2603-17573 -->

进一步跳过 target 验证，或允许 position/rotation 组在容差内接受，就把严格生成参照改成了动作质量与成本的近似取舍，不再继承[经典投机解码](../part-05-inference-system/48-speculative-decoding.md)的分布保证。Gripper 与参考一致也不能批准实际接触安全。[受限 AR-VLA 对照](https://arxiv.org/html/2603.17573v1)的加速伴随若干模拟任务与实机成功率退步，且“接受长度”包含跳过验证的候选；历史库、视觉编码、草稿训练、检索通信、阈值校准与现场示教都付费。质量、身份或 control deadline 无法验收时，回退 target 重算、短 horizon 与原 controller；动作仍逐步经过独立安全约束，不能等整段执行后才用任务成功更新代理，更不能把重生成当作已经撤回物理 effect。

## 静态注 PRE

- `SF-2026-ARXIV-2603-17573` — [HeiSD exact-v1](https://arxiv.org/html/2603.17573v1) §3–7/Alg1/Tables3–6及必要C–E；只采用历史运动proxy→检索/drafter与skip/组容差的近似动作分支。伪码更新冲突、不同action schema、AR/真机质量反退、未验证候选计AL和完整费用保留；不授exact target law、任务/机器人无条件迁移、实时或安全保证，未核代码/复现。

## 非准备者必要核（resume_mar17，2026-10-11）

独立实际 exact-v1 §3–7 L120–317/Alg1/Eqs4–8/Tables1–6，C.2–3 L451–474、D L475–501、E.4–5 L536–547已读；未将返回references或全部图像算审阅，不开代码/复现。L247明确skip直接执行，L205–209组树与gripper零偏差、L316–317明确不考虑输出分布变化，故近似分支与经典exact合同区分成立。Table3/4 AR/实机SR反退、Table5 hybrid单独1.05×与AL包含未验证候选均核实；伪码minS/else冲突不采recipe。示教库40task与过去窗口/套件95百分位归一真实，既非未来oracle也非开放任务认证。

笔记配置窄澄清：E.5 L544对实机server明确bfloat16/FlashAttention2/greedy，L545–546序列化推理请求并有HTTP client-server/CAN映射；不能统称precision全未披露。模拟部分precision、线上控制deadline/tail/独立seed和总费用仍未闭合。该精度澄清不影响无数字两PRE；额外DB/编码/草稿训练/现场采集/校准成本不能由5.13ms平均检索或整批T6认证。

actual Ch26 1320–1380完整动作表示→压缩→gate→提前退出/缓存链与Ch25/27入口、Ch48 925–955有损acceptance交接实际读。现gate不承载过去运动窗口选历史/drafter及skip/组容差改变动作参照合同的具体差额，sole MULTIMODAL-EMBODIED-VLA适当。原两literal PRE和静态注逐字回证据，质量/身份/control deadline与独立controller近文，回退不撤销既物理effect明确；有限Source/actualowner/PRE PASS，原6不变。需root窄ownership与一次非writer actualPOST；此处未写未POST，不计I或DAY。

## 非writer实际POST（resume_mar17，2026-10-11）

root窄写后，非writer实际完整Ch26 1344–1378/new1356/1358、2238–2242本人/FASTER邻注读回，逐字PRE与已核Source一致。压缩action-sensitive→freshness gate→历史运动proposal→近似动作参照→提前退出的完整链自然，classicexact不继承/gripper非安全/AR与真机SR反退/全费用、既执行effect不可撤销均近文；唯一静态注仅源与必要范围/边界。限定diffcheck0，局部actualPOST PASS，可root接纳释放窄锁，不授全日DAY/代码复现。
