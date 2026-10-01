# Apr24 五项有限非作者 source → owner 核验

复核者 apr02，非本日报及拟写正文作者。实际读取当前合同、五项 literal、下面必要官方 v1 与实际 owner 相邻论证；不重扫原始库存，不遍历附件，不写 Books/作者报告，不验日期或整日 Gate。下述 PASS 仅是具名窄采用提案，实际写后仍须独立验收。

## 21700 — Ch72：目标片段选择性与风格触发

[官方 v1](https://arxiv.org/html/2604.21700v1) III-C–E、IV-B/C 与 IV-F 的必要结果已实际读。Eq5–7 对 poison 目标片段强化、clean 同片段抑制，区别于全回答 CE；TableIII 的部分 FPR 到 26.5%，反演 camouflage 也不等后门消失。当前 Ch72 Backdoor Evaluation 已有 trigger 邻域与 training-strength 矩阵，但未承载长回答目标片段被稀释及双条件 loss 的这条责任分支。两段 literal 采用 PASS，保持提供方 LoRA/隐藏配置写权限，而非任意无权限输入；独立来源与 canary 属工程要求，不能称论文已证明有效防御。

## 20985 — Ch72：最终发布对象与相关随机轨迹

[官方 v1](https://arxiv.org/html/2604.20985v1) §5 Eq6/PLD、§6.1–6.3 及受限实证已实际读。随机只发布一个资产的混合会计与发布全部不同；该 RS 分支不要求候选独立。LC 更紧轨迹会计需独立噪声，同 run checkpoints 不满足此条件；只知 profile 时保守 composition 仍可用。实际 Ch72 DP 段已有 adjacency/composition/post-processing，未区分这两种资产发布分支。literal PASS，不能平均 epsilon、退还历史发布预算或外推 LLM utility；私有 selection 另计。此处不额外验全部证明或声称所有 LC 实现正确。

## 21590 — Ch27：支路反推三类训练输入

[官方 v1](https://arxiv.org/html/2604.21590v1) §3.1–3.3/Algorithm1、§4 Table1 已实际读。先扩条件树，再选支路反推环境、用户目标、SOP，改变训练样本状态与输入职责；强模型在 mock 中走预定支路不是现实 effect oracle。§3.2 虽叫 multi-model，实际是 Qwen3-235B 三次回答，不能写独立模型投票。当前 Synthetic data 有 generator/judge 同源与生成要求×规模，但无该 inversion 分支。literal PASS；综合两 flywheel 与训练轮次未唯一归因此组件，保存受限质量/预算和真实轨迹回退，不以用户要求创造授权。

## 21275 — Ch27：正常读取顺序与输入身份分开

[官方 v1](https://arxiv.org/html/2604.21275v1) III-B/Algorithm1、IV-A/B、V-A/C 已实际读。独立 worker 队列、固定 round-robin 分派与同序合并将次序从完成时刻移交 reader；缓存的是转换后 NumPy，不是原 bytes。实证为 Petastorm/HDFS/Ray/Horovod 推荐训练，GPU 型号未披露，MAP 变化还含辅助稳定性技巧，不外推 LLM 吞吐或全训练 bitwise。实际 Ch27 manifest/cursor 与 batch 原子发布未定义这一正常并发顺序责任。窄 literal PASS，仅作为模型无关、直接用于训练数据面的 ownership 分支；慢 worker 阻塞为采用代价判断，非作者已测 tail。故障重启/扩缩恢复另验。

## 21549 — Ch66：总体残差抵消与重加权迁移

[官方 PDF v1](https://arxiv.org/pdf/2604.21549v1) 物理页3–9的定义、条件与 LLM 实证已实际读；一次 web 公式页截图接口报错，未将失败截图当视觉核验。条件期望与群体重加权文本公式可读：支持内、标签条件规律稳定、相关群体残差归零，才有 prevalence 迁移；multi-accuracy 与更强 multicalibration 不等价。实际 Ch66 PPI 残差与 prevalence likelihood 未承载旧群体误差抵消在 reweighting 后破裂的分支。literal PASS；新类型仍有偏差、binary-label+metadata 与 probability 的 OOD 排序不同，有限拟合不保证所有未来群体。只估总体，不升级逐条 truth 或发布授权。

## 交接

五个窄 source → 当前实际 owner/literal 均 PASS，评分保持作者既有审阅强度，不新增候选或改日期。需 root 授锁后才实际写，写后以真实正文/邻接核验，不以本文件替代 Books 或日级 Gate。
