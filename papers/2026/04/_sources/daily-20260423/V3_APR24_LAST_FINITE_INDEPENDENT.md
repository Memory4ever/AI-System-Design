# 04/23 最后有限批次的非作者复核

复核者：`apr24_close`（不是04/23作者），2026-09-30。窗口04/22 09:00～04/23 09:00北京。已重读当前AGENTS、研究/来源每日/Report合同、统一Prompt、ROADMAP及本日停点。只处理作者[最后十二项](V3_ROOT_LAST_FINITE_REVIEWS.md)、五处实际新增和[日期收口](V3_ROOT_OAI_DATE_BOUNDARY.md)；其他具名有效单篇证据/写后复核复用，不重排全文或无关附件。本文件通过的是有限包，不冒充整日日级验收。

## 十二项必要证据与处置

以下均核精确v1原始正文的必要方法、关键对照和直接反证。三项明确gap维持5分但按知识缺口深入；安全和中心争议亦按受影响命题深入，不能用低分逃避。

| Family | 独立核验位置与限定结论 | 处置 |
| --- | --- | --- |
| [19811v1](https://arxiv.org/pdf/2604.19811v1) | 正文前六页方法/访问协议：73个非程序性STEM问题的数字token计数（可重复、不含词写数字）不证明能力或风险；零计数不等于无效回答。模型共同问题覆盖和21语境变体没有形成匹配因果对照，同一模型执行/判断非独立真值。不读取或保存危险操作附件。 | 安全深入，中心构念争议暂缓；受限观察可报告，能力/保护排名不采用，不Books。 |
| [19835v1](https://arxiv.org/html/2604.19835v1) | §3.1–3.2/4.2/5.3 Tables3–4：utility-copy改变“复制谁”，与一般增加expert数量不是同一命题；复制/router/CPT预算与完整训练路线分别记账。凸OCO共享最优解/lifting假设不证明非凸训练保证。 | 知识缺口深入，MODEL-MOE Ch21两段整合通过。 |
| [19844v1](https://arxiv.org/html/2604.19844v1) | §V-B/C、VII：观察/信任/执行是同一LVLM三角色调用，不是独立验证。正常帮助与误导双分母不可只求零攻击；TableVI/VII仍有结构扰动及white-box残余，三调用不是零成本。 | 安全深入，仅报告具体实验；已有通用信任原则不冒称完整三调用防御已覆盖。 |
| [19925v1](https://arxiv.org/html/2604.19925v1) | §5.1–5.4/6.1：检测owner-referential公开披露，不证明私有工作区外泄、真实性或未同意。45/376与92/224是标记阳性内误报占比，不能写成总体FPR；置信标签不校准。六天样本、有限Twitter与观察相关性不证明人格迁移致泄漏。 | 安全深入，仅报告评价盲点，不给真实事故率或部署保护结论。 |
| [19974v1](https://arxiv.org/html/2604.19974v1) | §4.1–4.3/5.2–5.4 Tables5.2/5.3：uncertainty×correctness两轴、分位筛选及SAE residual保留；entropy-only损伤accuracy，accuracy gate独立存在。随机活跃feature对照不等于开域因果证明，多重检验未校正。 | 知识缺口深入，PLATFORM-EVALUATION-SYSTEM Ch66单段整合通过。 |
| [20012v1](https://arxiv.org/html/2604.20012v1) | §3–4 Eq2–6/5–6：固定VLM、平衡目标/通用分类器在先验条件下作density-ratio排序，不是语义真值；同母模型随机选择更可比，其他baseline并非完全同预算。有限模拟机器人、mid-train预算与非目标回归限制保留。 | 知识缺口深入，TRAIN-DATA Ch27两段整合通过。 |
| [20041v1](https://arxiv.org/html/2604.20041v1) | §3.1–3.2/4.3/5：带噪NF likelihood→AR patch初始化→输入log-density autodiff score→并行ODE；autodiff不免费。噪声小不稳/大模糊、CFG与首patch失败解释的假设性质保留。 | 标准完成，仅报告有限图像分支，不声称干净likelihood或普遍省算。 |
| [20047v1](https://arxiv.org/html/2604.20047v1) | §V-B/VI-E、AppendixH：威胁是模型提供者控制artifact，不是黑盒prompt。单/多patch预算与Gaussian反例不能合并成不可移除性；输入drop/shuffle不足完整模型生命周期保证。 | 安全深入，仅报告受限威胁/防御证据，不保存攻击配方、不Books。 |
| [20087v1](https://arxiv.org/html/2604.20087v1) | §3.2–3.3/4.1/Table1：文本质量、轨迹使用、任务outcome三层不同。固定Sonnet4.6/temp0/100轮sandbox、GPT5-mini judge；SelfK2/TeacherK3不同预算。均值31.08 vs30.44反驳自反馈总退化，usage不是utility。 | 标准完成，仅报告具体比较；不把技能文本累积说成无遗忘保证或新的通用学习法。 |
| [20090v1](https://arxiv.org/html/2604.20090v1) | §2.2–2.4/3.3、Limitations/AppendixA：I−λBBᵀ仅λ1是正交投影，实验λ.4；USS/LQS/curvature是排序/裁剪proxy。匹配ULM预算支持局部收益，模块删除改变搜索预算；翻译、hidden forward、warmup/window成本及白盒权限保留。 | 标准完成，仅报告有限跨语言控制，不给逻辑等价/真值或通用调度保证。 |
| [20136v1](https://arxiv.org/html/2604.20136v1) | §III-E/F Eq10–13、IV–V：正向uncertainty/conflict/impact utility与u<θ升级方向不一致；直接邻接union未证明传递closure。同GPT4V各角色、主要oracle人类、K5/r2与n9 p=.096不证明完整可修正性或普遍省人力。 | 中心保证深入，争议暂缓；有限角色/实验可报告，不Books。 |
| [20258v1](https://arxiv.org/html/2604.20258v1) | §4.1.3/4.2 Eq11–12、5.3/AppendixC：add目标/remove源/replace并集及阶段匹配latent blending属估计mask。最大组件可丢分离区域，基模型全局修改使union失准；latent约束不证明最终像素硬隔离。 | 标准完成，仅报告任务相关实现，不抬升为跨模态状态契约。 |

不因为安全/评价主题有旧owner而抹去19844/19925/20047的局部证据；也不把三个仅报告项伪装为具体已有完整实现。19811/20136中心争议不是访问失败：本窗可终态隔离，重开分别需要构念有效且匹配协议的独立测量、修正升级方向和依赖closure并有真实人类成本/错误评价。

## 五处真实写后

亲自读取实际段落和前后交接，不只按作者literal或marker签署。19809、20209复用已有效的具名source→owner独立记录；三新项使用上表本次必要原文核验。结论全部通过。

| Family | 实际owner/锚点 | 写后结论 |
| --- | --- | --- |
| 19835 | [Ch21](../../../../../books/part-02-model/21-moe.md)，Expert Pool后、超参数架构身份前373–375 | 复制对象utility与扩容预算两段保旧路径、proxy/CPT/非凸边界和fallback，无静默替代。 |
| 20012 | [Ch27](../../../../../books/part-04-training-system/27-data.md)，机器人分布匹配后、joint-space前589–591 | proposal与事实/动作安全分离；表示/先验/pool版本、额外成本、受限对照与回退齐，不把density ratio说成真值。 |
| 20209 | [Ch33](../../../../../books/part-04-training-system/33-grpo.md)，self-play支持集后1373–1375 | reward starvation/entropy/guide质量proxy、两消融混杂及原verifier分工保留；没有guide代替形式正确性。 |
| 19809 | [Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，Forecastability与Calibration之间483–485 | capability prediction/实际升级/fallible resolver/误升级四分母分开，强制router不算模型自省提升，成本与保守回退齐。 |
| 19974 | [Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，FailureDirection末、SingleToken前1850 | entropy×error两轴与accuracy acceptance独立，有限MCQ/SAE及无多重校正边界齐，不重复19809的升级决策链。 |

上述行号为本次读到的锚点，后续并发插段可移动；source-family identity与邻接关系是实际定位依据。此前十二个整合的有效source/实际写后不受本批变化影响，不重复审阅。

## 有界日期裁定通过，撤销19795旧dateHold

亲自读取[官方Availability](https://info.arxiv.org/help/availability.html)的ID分配、公告与延期规则、本日v1原始字段和作者日期文件最新节。接受51篇19749～20289同批的04/23 08:00～09:00+08有界推定：正常周三20EDT公告、ID在公告过程中才分配、保存v1处理集中00:00～00:34Z、未修订OAI23以及后续DOI注册共同定位。**不**把submitted、Updated、OAI或DOI created单字段改名为首次公开；不称观测精确秒或全站无延期。后来修订身份只用v1记录和未修订邻界，不从当前OAI反推。

19795原[官方字段保存](../arxiv-owner-replay-20260903/20260423/arxiv-owner-receipt.json)：submitted04/08T09:16:43Z、v1 Updated04/23T00:01:09Z、OAI23、DOI created01:50:18Z。仅定点核旧Apr09 ledger该身份：first_public_date/published均复制submitted，所谓Beijing字段仍为同一Z值；没有独立更早正文公开记录。因此撤销[V3_EVIDENCE_REVIEW](V3_EVIDENCE_REVIEW.md)开头用旧screening出现支持的日期hold，接受同批有界落窗；Eq9中心反例及争议暂缓不变，不Books，不重开整个Apr09。

20329另有Google04/22自然日的可能更早独立公开，不能用arXiv批次覆盖，继续DateHold；Seed两个自然日bucket继续隔离，不计51篇。OpenAI WebSockets原RSS04/22 10GMT即18:00+08直接落窗，不借arXiv推断。新的真实更早信号或官方延期反证只重开对应家族，不扩大日期。

## 交付界限

十二项必要证据/处置、五处真实写后、51篇批次日期与19795纠错本批通过。作者须把正式报告相应普通待办和19925误报分母同步；最终52家族报告、来源停止位置、复用有效正/负侧全覆盖和日级Gate另由非作者对最终版本确认。本文件不是作者自签，也不是全月完成。

## 最终映射时发现的五处有限补核

旧19877/19884/20032/20105必要source→owner已经有效；最终映射发现若干“root写后”实际上是作者自读，不能复用为非作者验收。因此本复核者亲自补读真实正文及邻接，不重读这四篇源码或扩大附件：

- **19877 Ch22约751–753：通过。** 前接固定hybrid校准、后接跨层表示基底。多布局是已训练placement集合，状态/layout不可互换，single-preset、切换迁移/捕图和逐请求尚未完成清楚；eager质量与graph吞吐不拼生产Pareto。
- **19884 Ch49约949–951：通过。** 前接aggregate→逐例→drift、后接精度分配。可读信号与处理失败是两分支，probe不因果，条件cohort零分不总体，增加bit/scale与所有2-bit失败不泛化，预算/回退齐。
- **20032 Ch49约129–131：通过。** 前接执行栈/WebGPU分解、后接编译计划。stall位置→寄存器/谓词/wait依赖只提出根因假设，同配置干预才验收；instrumentation、vendor/冷样本/branch误差及kernel收益不等服务收益保留。
- **20105 Ch70约319–321：通过。** 前接组件power budget、后接默认频率参考曲线。缺目标设备时结构活动预测仅筛设计点，仍离线校准；并发/通信/稀疏与L40S能效失配不越权，目标仪表和热/SLO验收及保守预算回退清楚。

**19857必要独立理论核通过窄D。** 本次实际打开[exact-v1](https://arxiv.org/html/2604.19857v1)§4.1–4.4与A.2–A.3，不遍历其余附件。Eq41/42代入Eq44时Δ恒为0（这些打印式不含ε），但Eq40用原w，不是wσk/σcomp：两样本R1=(0,1)、R2=(1,0)、w=(.75,.25)、r=(.9,1.1)不触clip时joint项.1而dec项.05，Δ仍0，故Eq46桥不成立。Eq25的固定分布差到Eq50凭空多1/√n：DS=(.5,.5)、DT=(.75,.25)、V=(1,0)差.25，KL固定有限，而Eq50右端趋零。只击这两打印证明桥，不声称全部GRPO/实证无效；Assumption2的K/G已是条件。6分深入、中心保证暂缓不Books，重开只要相应勘误/充分条件或独立可核修证明。旧日期hold由上节batch裁定替代。

这四处实际写后和一项中心理论核补齐了发现的真实普通缺口，不把作者旧PASS追认为独立审阅。
