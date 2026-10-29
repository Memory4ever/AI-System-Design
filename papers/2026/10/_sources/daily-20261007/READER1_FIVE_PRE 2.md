# 五项最小逐字稿

Source/date/owner复用READER_REVIEW §17；未获literal PRE前不写Books。

## 06174 / Ch66

锚点：内部可分性及输出验收原两段后，“解释工具对内部组件的描述”前。

逐字正文：

内部线索能否被模型读出，还可固定同一文本，在不同量化 precision 上共享一个 readout adapter，检查它是否识别量化 method 的 fingerprint。这比只测线性 probe 多了一层可训练读出，但不是模型自然知道自己处于何种数值状态。[受限量化自报对照](https://arxiv.org/html/2610.06174v1)中，共享 LoRA 可学习已见配置，换未见 method 或 group size 却失败，完整精度也仍会误报异常；因此内部可读不授权跨配置自知，更非内省因果证明。简短回答偏差与普通任务轻退要和识别率并报；activation、adapter训练、留出校准和行为回归全部计费。配置变动或任务回归未过时保留外部 artifact identity、直接行为测试与 Unknown，不用内部 sensor 代签可靠自诊断。<!-- source-family:SF-2026-ARXIV-2610-06174 -->

逐字本人注：

- `SF-2026-ARXIV-2610-06174` — [exact-v1](https://arxiv.org/html/2610.06174v1)，Daily2026-10-07/Oct6窗，2+2+2=6；§2–5及method/group-heldout、brevity/普通任务反侧；reader1 §17必要Source/date/owner通过，literal PRE/实际POST另记，未核实现/复现。

## 06204 / Ch28

锚点：“换规模时，学习率外推也需要适用域”两段及end marker后、“不知道训练终点时”前。

逐字正文：

固定 learning rate 的跨规模 RL 对照，也不能把某个小模型收益较少直接解释成固有学习能力边界。[受限卖方训练对照](https://arxiv.org/html/2610.06204v1)中，三倍学习率改变早期收益和尺度差，而训练 run、架构与 FLOPs 尚未全部匹配；64个 scenario seed clusters 的重采样不等多个训练 seed。进一步提高至十倍学习率时，改善集中在部分对手，并伴格式退化；两个 buyer 与训练/评价 scaffold、accept处理的变化不足以识别普遍 family 效应。固定 recipe 仍可作受控基准，但能力归因应另付局部 sweep、训练重复和对手/协议回归成本，保留无可检测差异不等价的边界；质量或费用不合时保留原配方与模型，不由单48GB能装下推断 Serving 更便宜或通用规模定律。<!-- source-family:SF-2026-ARXIV-2610-06204 -->

逐字本人注：

- `SF-2026-ARXIV-2610-06204` — [exact-v1](https://arxiv.org/html/2610.06204v1)，Daily2026-10-07/Oct6窗，2+2+2=6；§3–6/A协议，LR与size归因/单seed/cluster和buyer反侧；reader1 §17必要Source/date/owner通过，literal PRE/实际POST另记，未核实现/复现。

## 06325 / Ch30

锚点：端侧模拟对照完整段后、“在保持原LoRA函数”MeSP段前。

逐字正文：

真实手机还会把单步可行性变成持续热与电量预算：冻结低位基座仍要计算 input gradient，forward格式可用不保证反向 tile、bounds 与实际 dispatch 正确；[单台 iPhone 的持续训练测量](https://arxiv.org/html/2610.06325v1)将冷启动、完整训练与热状态分账，冷步166 token/s不代表长run的83–89，所试 pause/burst反而减少每小时更新。能耗来自电量档位减idle估算，满电987 records仍未完成，不授任意history一电池训练。七任务多在server评价，手机仅复核movie-tagging，近平均分与7.8%逐题不同并存，非输出等价。Runtime正确性、持续训练、充电/前台资源与手机质量均计费；热、完整预算或任务未过时保留检索、较浅adapter或普通runtime，不由能运行与单步峰值批准端侧训练收益或隐私保证。<!-- source-family:SF-2026-ARXIV-2610-06325 -->

逐字本人注：

- `SF-2026-ARXIV-2610-06325` — [exact-v1](https://arxiv.org/html/2610.06325v1)，Daily2026-10-07/Oct6窗，2+2+2=6；§2–7/9持续热/电量/phone质量，MLX PR4051八月已公开不重计kernel；reader1 §17必要Source/date/owner通过，literal PRE/实际POST另记，未核代码/复现。

## 06329 / Ch27

锚点：OP-Mix完整两段/end marker后、“双语词汇干预”前。

逐字正文：

另一条 mixture 分支只读取当前所选 source 的 minibatch loss，用折扣统计、effective count 和 UCB 追踪随模型变化的较差 source，不为每轮重新评价全部历史人口。省掉 replay 和逐source specialists，也让未选 source 的反馈陈旧；采样器必须保存平滑、探索及统计状态。[DUCB-OGD 的受限分析](https://arxiv.org/html/2610.06329v1)在凸loss、有界域与指定步长等条件下讨论逐时刻 worst-source regret，不认证非凸 AdamW/GRPO 最优；实作还采用随机 index、DEMA和强制探索。Worst-source改善可伴平均分退步，代理baseline及排除specialists的局部计时不代表完整比较。全部采样控制、统计checkpoint、训练与held-out回归都付费；陈旧反馈、均值质量或净费用不合时保留静态mixture与真实小规模sweep，不让UCB提案自签最优配方。<!-- source-family:SF-2026-ARXIV-2610-06329 -->

逐字本人注：

- `SF-2026-ARXIV-2610-06329` — [exact-v1](https://arxiv.org/html/2610.06329v1)，Daily2026-10-07/Oct6窗，2+2+2=6；§2–5/B/D，stale-source/有效计数与凸界/实现/mean反侧；reader1 §17必要Source/date/owner通过，literal PRE/实际POST另记，未核代码/复现。

## 06212 / Ch84

锚点：Idle Time可取消Speculation完整局部后、下一标题前。

逐字正文：

Idle window中的能力学习还需把投资与实际复用分开：只有qualified、publish并真正被使用的产物才获得复用收益，durable progress、停止ack、memory释放与真实capacity-ready不是同一时刻。保留服务 runtime 状态用驻留换较短return time；冷恢复费用也可能使等待更长窗口优于立即开工。[LearnSched 的受限模型](https://arxiv.org/html/2610.06212v1)只在准确有限transition、价值与safe actions下保证rollout不退，不能给未知arrivals硬SLO。所测960个warm情景全部持平、rollout仍有13例未达DP，实机部件测量不等在线控制器验收。Failed、unpublished、unused投资和GPU/host驻留都计费；收益预测、ready时延或资源安全未过时保留不启动、costed-window基线与前台优先，不以command ack或少token替代可复用能力及资源归还。<!-- source-family:SF-2026-ARXIV-2610-06212 -->

逐字本人注：

- `SF-2026-ARXIV-2610-06212` — [exact-v1](https://arxiv.org/html/2610.06212v1)，Daily2026-10-07/Oct6窗，2+2+2=6；§2–7投资/reuse-window/durableprogress/ready与有限模型、warm全tie反侧；reader1 §17必要Source/date/owner通过，literal PRE/实际POST另记，未核实现/复现。
