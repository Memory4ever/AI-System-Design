# Oct23：两项七分候选的必要证据

窗口Oct22 BJT自然日，2026-10-23访问；root准备Source与PRE，非writer reader独核，未获批不写Books。身份/本日公告关联复用ARXIV有效层，当前HTML顶部Oct21为提交日期，不搬候选。29435为3+2+2=7、30074为2+2+3=7，沿原正式评分；原始研究非复现。只核以下必要域，不声称全附件或artifact已审。

## R1 — [Events, Not Pixels](https://arxiv.org/html/2610.29435v1)

实际读exact-v1 §3–8、Tables1–3及方法/反侧文字；不采用需supplement才能复核的精确总体比例、规则阈值或生产性能。贡献是定位规划return误差，不是重复“视觉质量不等控制质量”：同初始context、同recorded actions配对真实/想象轨迹，用冻结memoryless reward/termination detector逐transition读出。替换时交付完整真实帧对，未选pair仍用预测，不把半真实/半预测pair送detector；event邻域、等数量random、非event complement和all-real四组分开。收益相对原return误差衡量，event比random的差额才隔离定向选择，不能仅看patch后变好。它是对固定reader的离线读出干预，不重生成后续轨迹，也不等部署时能获得未来真实帧。

关键反侧：event mask依赖真实reward/termination，邻域扩展影响时序结论；reward-event detector在独立collection过F1门，termination未同样gated，all-real仍有末步/检测残差。部分组合为non-event-dominated，使用自身reward head还可改变个别归因。误差大的MSE/SSIM/LPIPS帧选择不必命中decision事件；扩大对齐容忍度仍漏不等认定世界中绝无该事件，只是未被此reader读出。diffusion替代与MSE baseline更新数不同；同diffusion网络改成确定性loss仍保留收益，故不把修复归成随机采样必需。规划比较仅在通过可靠性规则的人口下核固定八plan，不能推新planner或真实闭环成功率。真实replay/标签、detector、四路patch、训练和规划回归均收费；硬件/完整SLO未采用。

actual owner：Ch25已用PatchWorld readout改善却成功退步、几何与policy evaluation分责解释视觉/规划不等，但未有transition-pair event/random/complement/all-real归因接口。唯一`MULTIMODAL-WORLD-MODELS`，拟在“转移准确率不等于规划可用性”下原三完整段后（末句“不能独自承担规划可用性的发布门”）、“Repair Metric必须与Rollout Horizon对齐”标题前加入一段，保旧training-only world tokens分支不变；Ch24生成与Ch26真实反馈交接复用。

PRE：

> 要定位规划误差，也不能只挑视觉重建最差的帧。可固定初始观察与同一动作序列，用独立验过的冻结reader从真实/想象的相邻帧对读return，再分别替换真实事件邻域、等数量随机位置、非事件补集和全部位置；只有event相对random的额外改善才说明误差集中，而all-real残差仍属于reader和读出协议。[受限transition诊断](https://arxiv.org/html/2610.29435v1)发现看似同样清晰的少数事件足以改变候选排序，但这是有真实未来标签的离线干预，不是在线修复或因果动力学证书；邻域、termination检测、误事件与非事件反侧都须保留。真实replay、标注/reader和全部规划回归均付费；reader或任务支持不足时，保原预测指标、真实闭环验证和较短horizon，不由更清晰帧或一项patch分数批准行动。

## R2 — [Graph-Structured Distributed Block Optimization](https://arxiv.org/html/2610.30074v1)

实际读exact-v1 §2–5必要定义、§3 gain-retention的Thm1/2及完整证明、§6.1–6.4、6.5–6.7/7；不采用全球收敛率、assignment LP/最优deadline或补充材料中的另实验为Books结论。理论命题要求有限block、可精确求值F和已知factor scopes，依赖图保守覆盖所有共同factor；相同冻结base逐一验证且只保非负gain。独立集内每factor至多被一改动影响，才有gain精确相加；fractional cover权重总量Λ和每点覆盖≥1，通过最大支持集≥加权均值给保留至少1/Λ总单项gain。tight构造用正交互惩罚和fractional LP对偶，不是LLM任意语义任务的界。普通κ-coloring仅1/κ；fractional计算可能昂贵，最大权独立集每轮也须求解。漏边破证，多边保守降并行。完整union可另验捕获正交互；只保单项有益仍可困在需要联合上坡的状态，不把单轮bound升为必达全局最优。

直接评价反侧：小修复任务单Agent全成功且费用/建模时间更低；验证费用计入后紧预算下保守合并亦可能不及naive。三轮held-out接口迁移中全部并行规则均未完整解题，首轮fractional优势也未保证末轮保留。输出tokens不在input-token-equivalent cost内；repair latency是假设同时启动、分stage验证延迟的model，不是集群实测。road/timetabling同池fractional胜fixed coloring，但adaptive ordinary达到相同gain，不能归独有算法优势。route实测是在人工诱导C5、exclusive route锁+可抢占chunk前提，immutable snapshot并行搜索/只串行commit不在比较；route质量可退。依赖证书、所有singleton/union/full checks、通信、求解与失败调用均计费。未知真实依赖或不完备测试时，符号certificate不是语义安全证明。

actual owner：Ch82 Verification与Aggregation的SF2610-28286两段已解释同色可加/联合重核与single-block trap，不再重复这些机制或全球收敛。新差额仅为“保留多少单项gain”的有限证书与最坏界、可重用cover和普通coloring计算取舍。拟在该两段完整marker后、少数反证标题前一段；图不是通信topology，不在平台scheduler重复。

PRE：

> 兼容合并还可给出一条有限的收益保留界：若有限block目标能按已知依赖精确分解，每份proposal都在同一base上独立验证为非负gain，则独立集内的gain才可相加。让若干兼容集以总权重Λ覆盖所有block、每个block覆盖权重至少一，选择gain最大的支持集，就能保住至少总单项gain的1/Λ；普通κ-coloring对应1/κ。[受限合并理论](https://arxiv.org/html/2610.30074v1)不把测试通过变语义真值，漏掉真实依赖会使证书失效，保守多边则降低并行；求更紧cover也增加计算。另验联合candidate可利用正交互，但单项有益筛选仍可能困在需要共同修改的局部状态。求图/求解、单项与联合检查、通信和全部调用均付费；目标或依赖未知时保串行、小型普通分组和完整任务验收，不由无文本冲突或理论比例承诺真实完成时间与全局最优。
