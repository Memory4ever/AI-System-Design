# GSU17333：坐标oracle下的参照系诊断与最小PRE

resume_mar17，2026-10-12，仅03-20补03-19。原2+1+2=5、两作者/ID/date及准入复用本日有限尾/独核§30，不改原字段。本稿准备，未自授Source/PRE/Books/safe/DAY。

## 1. 实际必要范围/停止

[exact-v1](https://arxiv.org/html/2603.17333v1)实际§2–3 L86–157、§4.1–4.4 L172–196、A.0.1–0.3 L276–334、A.1 L374–377；当前abs同题两作者/Comments preprint/history单v1轻量核。数据生成/评价核心与直接反侧足够拟采用命题，未核代码、全文参考文献、完整B–E实验/所有图，不授训练recipe或完整FT结果复现。

## 2. 所采评价接口与直接边界

相同模拟路径交换instruction/coordinates构成Instructor/Follower；Cardinal固定轴而Egocentric消费每步更新heading。Object Localization由坐标/heading生成关系，文本输入不需要视觉识别，但仍付表示读取和reference转换；测试100/任务，train3000且示教与输入表示经性能选择，非未触碰独立搜索集。导航exactmatch和关系/颜色/数量/形状overlap不是同一分数；partial形状和同义词表不认证完整坐标—属性绑定。

T1及§4.2：各VLM/LLM家族结果混合（Qwen部分空间项退，Pixtral部分升），模型规模/训练和adapter不齐；全部测试无图像，不能证明视觉输入无价值或VLM普遍没有3D能力。§4.3简单题frontier可满分但组合仍退；§4.4最初LoRA导航退后新增合成reasoning，不能授小模型同预算替代frontier。A中representation择优及术语解析、数值人口/预算有限；§A统计35+35+40不闭合，不采分布精确比例。硬件、seed/variance、完整搜索/生成/解析/调参费用与生产deadline未披露。本次仅诊断分责，不采用架构因果、无限泛化、真实动作安全或无损性能。

## 3. actual owner/交接差额

唯一PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。实际完整236–254规则提供/主动证据/VAEX：已有看见state与知道transition分离、rendering证据生产，但没有以程序提供coordinate oracle而改变参照系更新/instructor-follower接口的受限text-only测量。拟VAEX完整段之后/第一个不变量标题之前一段，不重写原规则发现或真视频测量。

Ch26入口1–32明确reference frame/embodiment/真实控制权限，仅用作交接，不能把本评分当机器人行动验收；Ch65/67本次入口实际读1–25，公平资源/观测聚合不重新定义空间任务scorer。不按空间主题映射自动整合，若独核指出已有完整承载该具体命题，可specific NC。

## 4. 待nonpreparer核的逐字PRE

当要定位“已知几何之后的规则应用”而不是视觉识别时，还可以由程序提供坐标、heading 与路径 oracle，只交换固定轴/随主体更新的参照系，以及坐标到指令/指令到终点两种接口。[受限文本grid诊断](https://arxiv.org/html/2603.17333v1)用这种分解暴露更新方向后仍按旧轴作答的切片；文本化去掉的是视觉输入需求，不是表示解析、坐标变换或真实环境约束。终点 exact match、关系与属性词 overlap 应分别保存，词集合部分命中不认证完整对象绑定。示教、表示选择、模型训练/规模和解析规则均需冻结，额外生成、oracle 与回归也计费；混合VLM/LLM对照或单任务高分不能证明视觉训练无价值、内部空间机制或物理执行安全。实际需要视觉观测时仍保留原视频/场景测量和独立坐标校准，只把该oracle切片用于区分已知几何上的规则失效。<!-- source-family:SF-2026-ARXIV-2603-17333 -->

静态源注：

- `SF-2026-ARXIV-2603-17333` — [GSU exact-v1](https://arxiv.org/html/2603.17333v1)必要§2–3/T1、§4.1–4.4、A生成与shape scorer；仅coordinate/heading oracle下的参照系和双向接口诊断。保示教/表示择优、有限任务人口、不同metric与VLM/LLM训练/规模混杂、组合失败和完整费用，不采视觉无价值、架构因果、FT普效或物理安全。未核代码、完整附件图或复现。

## 5. 待独立裁决

交具名nonpreparer必要Source/actualowner/一literal+static，不自授PASS。必要支持和直接反侧够即停，独核后才向root申请唯一Ch66 family窄锁；本稿未写、未POST/SAFE/DAY，不扩query或其他日。

## 6. root授锁后sole窄写与writer实际读回

2026-10-12 reader独核§38 Source/actualowner/原one literal/static有限PASS后，root在Gender实际POST接纳释放Ch66时授权本family。author仅原批准段写新244、static5969，不改VAEX或Gender/其他日期；实际完整232–260及末5本人/Gender/既有邻注逐字回对，VAEX证据生产→coordinate/heading oracle测规则→第一个对象不变量标题衔接保持。当前58新增→62新增仅本family四行/check0；不授视觉无价值/内部3D因果、绑定或控制安全。等待reader一次nonwriter完整邻接与静态注POST，不自授safe/DAY。
