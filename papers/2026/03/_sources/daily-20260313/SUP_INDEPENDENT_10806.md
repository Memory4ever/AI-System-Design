# 2603.10806v1：03-13 单篇独立 Source / 评分 / 具体已有覆盖复核

复核者：`mar13_admission_review`；准备者：`mar13_supplement`。只处理 2026-03-13 既有 Daily 的 **2026-03-12 北京时间自然日补充窗**。恢复实际重读当前 AGENTS、Research/Report 合同、Prompt、Sources 使用说明/Daily/arXiv 范围、ROADMAP 与本日 README/路由停点；不加载其他日期候选，不改原窗口/评分/§4 前缀。本文件不是 DAY 验收。

## 原件与实际检查范围

实际读[准备包](./SUP_EVIDENCE_10806.md)、[精确 v1 官方原响应](./SUP_CORE_10806.raw)及[GET manifest](./SUP_CORE_10806_MANIFEST_RESULT.json)：`https://arxiv.org/html/2603.10806v1`，GET200、1018699 bytes，2026-10-10T03:35:20.868527Z。直接从 raw HTML 提取并顺读 **完整 §4、§5.1–5.2（Eq1、权重干预及完整 Table1）、§6.1–6.3、§8、§9、App0.F**，数学读 alttext，不以作者笔记代原件。§9 有关 adversarial experiments 的讨论文字读过，但没有审 §7 的攻击实验实现，因此不采用其效果或因果结论。只读图 2–4/7/14–16 的正文与 caption，不认证图像坐标或全部网格检出率；未读无关附录、旧版、代码或攻击操作，未复现。

[完整 v1 题摘/history](./SUP_ABS3_10806.txt)实际回读：标题 Backdoor Directions in Vision Transformers，四作者 Sengim Karayalcin / Marina Krcek / Pin-Yu Chen / Stjepan Picek，唯一显示 v1；Comments 31 pages/16 figures，无显示撤回、纠错或具名早稿信号。本篇既有准入及主独核 §23 的 Mar12 arXiv 日级夹证复用，不把 Mar11 Submitted 当公开日，不重新证明全网无早稿。

## 独立必要 Source 裁决

- §4 明确使用可下载 BackdoorBench ViT-B16、12 blocks、CIFAR10/100/TinyImageNet，三 poison rates .01/.05/.1，按模型可用性选择攻击，LF 因可用 ASR<5% 排除；.01 部分模型只有40–70%。这是受控且有选择的人口，不是全部 ViT/全部失败攻击。
- §5.1 明确已知 trigger、clean training subset 与 clean/trigger 配对，平均 activation difference 分 CLS/all-token。Eq1 用正方向 ASR 与负方向 RA 的相邻层增量选择代表方向，消费目标类和原标签的行为信息。§5/§9 都直说不是未知 trigger 现实防线；这种功能干预不认证唯一因果回路。
- 完整 T1 **只纳 baseline ASR≥.9 的33模型**（12/13/8）。总体 orthogonalization ASR97.7→6.7、RA2.1→64.7、CA82.8→82.0；CIFAR100 ASR15.9/RA51.4，CIFAR10 CA95.4→93.9。负 CLS steer 总体 RA21.3/all-token53.8。不能写完全移除、全能力保持或无数据修复；trigger distortion 是可能解释而非唯一归因。
- `W_new=W−r̂r̂ᵀW` 的本段没有给出单位归一化，代表层/方向记号又复用；因此仅隔离精确可执行投影 recipe，**不从文字缺口断言实际实现错误或否定局部干预结果**。§4 列表只在 CIFAR10 加 Blended，§5 Results 却称 CIFAR100 Blended 是唯一失败攻击：不采用该“唯一例外”分配，只保留完整 T1 的实际总体/数据集反侧；无需为此扩全附录攻击表。
- §6 的 static/分布 trigger 与 token/layer 关系是所测人口的定性诊断，.01 曲线选择及作者 alternative explanation 保留；DeiT-S/Swin-S 仅 TinyImageNet 两攻击/.1，Swin 用 token mean。不能升为所有 ViT 的层位定律。
- §8 确实不需 clean data/trigger，却需 classifier head 和 early projection weights。公式是 threshold indicator 的计数，解释句说加超阈值数值，count/sum 口径未闭合；本次不认证精确 detector recipe。top–second/std/threshold 的 `Z>3` 是此稿启发式，不是独立 clean/adaptive holdout 校准的 FPR 保证。正文/App0.F 明说 WaNet/BPP 较易、SSBA 边缘、TrojanNN 不工作、并非全部场景。**预检阴性不能证明无 backdoor。**
- §9 明说修复仍需 reverse-engineer trigger，weight-only 检测失败于多种已知攻击，完整训练控制的 adaptive 情形可绕过。约一分钟/模型仅作者局部描述；必要段未披露硬件/precision、独立 FPR 与阈值选取人口、配对 subset/重复 seed/CI 和全预处理/修复/重测费用，不推部署 SLO 或免费总审计。

**Source 受限通过**：已知 trigger 的受控功能干预，以及 weight-only 预检的访问权限/触发类型失败边界有原证。精确归一化/count-sum recipe、全检出/未知 trigger 修复、全能力保持与发布保证隔离，不以这些未采用主张支撑正面结论。支持与直接反侧已够，无额外附件请求。

## 评分与实际唯一 owner / NC

独立认可 **2+1+2=5**：D2 是同稿已知 trigger 干预到未知 trigger weight-only 预检的具体适用界/失败类型证据，不给成熟线性平均方向或 orthogonalization 发明分；R1 是视觉模型诊断局部负载，不因 security/权重与 activation 两入口膨胀跨系统范围；Durability2 是访问权限与分布验证边界。安全解释/反侧涉及拟采用判断，必要受影响深入完成，不因 NC 降分或删候选。

实际顺读 [Ch66 `PLATFORM-EVALUATION-SYSTEM`](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) **234–310 完整局部**：

- 234–262 将 model/adapter/runtime、policy/tool/environment 等放入 subject identity，不以模型名替人口身份；
- 264–266 静态权重几何必须绑定制造方法/分布、保留跨方法 holdout，预检只能提出 probe，再由匹配目标独立行为验收，不能替 release Gate；
- 268–271 内部无输出 probe 仍须模型访问、前向、训练/校准，并不把训练类别当危险能力或用阴性放行；
- 273–275 activation sensor 保留标签、层/span 与独立行为/authority 分责；完整后邻接继续到内部解释与 harness/environment，并没有把内部信号升为真值。

另实际读 Ch17 开头 residual/组件职责与 Ch72 开头资产、更新与独立行为回归入口，确认计算结构和发布权限分别交接，不新造 owner。**具体 NC / Books0 通过**：当前拟保留的是“已知 trigger 功能干预不能代未知 trigger 防御；静态/内部 sensor 绑定访问/人口并不能由阴性取得发布许可”，现 Ch66 已真实承载这一判断，不只是安全主题相似。本稿 head/early alignment 配方、trigger 类层位差异及新数据未在 Books 中被声称吸收；有限新实验证据留本日报，不为制造 diff 写入已有责任接口。无 PRE/实际 POST 需求。

重开只针对将来拟采用的未知 trigger 自动修复/全检出或发布保证：需要精确实现口径、独立 clean/adaptive/type holdout、阈值选择与真实行为保留/全费用。当前无此正面采用，普通其他项继续，本篇不授整日完成。
