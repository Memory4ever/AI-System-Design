# 11/13 Project Fetch 单项独立审阅 ready

作者 Planck；仅此新增方向送 root 准入/证据/Books 独立审阅，不重复首批七项校准。不是日级完成。

## 日期与身份

原源：[Project Fetch: Can Claude train a robot dog?](https://www.anthropic.com/research/project-fetch-robot-dog)。官方 Research HTML 的 Next hydration 中，同一个 post 对象包含 title、slug.current=`project-fetch-robot-dog`、publishedOn=`2025-11-12T18:19:00.000Z`。本次恢复用 HTMLParser 提取 script、JSON 解析 payload 后按 slug 定点核对象，未用整页字符串邻近猜绑定。实际原始页是 [raw-anthropic.html](./raw-anthropic.html)，正文是 [raw-web-16.json](./raw-web-16.json)。

原字段 UTC 精确到毫秒，换算 BJT `2025-11-13T02:19:00+08:00`，完全落在 BJT [11/12 09:00,11/13 09:00)。这是官方发布字段授予的日期判断，不是 submitted、RSS midnight、一般 schedule 或 DataCite。当前页面未见撤回/纠错提示；只检查该事件页，不承诺历史页面从未变更。

## 新准入命题

原有可能混淆：编程辅助的硬件接入 uplift 可作为自主物理能力代理。实际新增证据：一个随机分队、两组各四人且无机器人专家的单日实验，主要优势集中于连接机器人与传感器，最终自主取球未完成。需要重新考虑：分开验收接口接入/人工辅助进展与无人闭环任务，而不把前者速度代理变成后者能力结论。拟评分 `1+2+2=5`，标准必要审阅；不计成熟闭环原则为新机制。

## 方法、评价与反侧

正文 What were we doing?/Results/Limitations/Footnote 3 已实际读取（raw-web-16 原行34–69、90–96、114）。阶段一厂商控制器，阶段二计算机连接/视频与lidar/人工软件操作，阶段三无人工指向的自主取球。7/8对6/8是阶段子任务，不是自主成功率；共同完成任务平均耗时约半，仅支持该一次两队实验。机器人型号、模型精确版本、调用预算、硬件及 latency/SLO 在必要正文中 Not Disclosed；不补造配置或复现。

- 阶段一 Claude 组恰好拿到独立控制器，对照需装手机app，而且该阶段未使用Claude；其速度差不能计模型效果。
- 对照连接受错误网络说明误导，实验者给予提示；这是已披露干预，不是纯独立对照。
- 控制程序功能不同（连续视频与间歇图像）；耗时直接比较并非相同功能质量目标。
- Claude组定位坐标翻转、切换并行方案；更多代码不等于更快收敛。
- 绿色球/绿色草造成检测混淆；近碰撞来自人的速度距离指令并由人紧急断电，不能归因模型自主攻击，也不能忽略物理安全反侧。
- 作者明确非端到端自主机器人工作测试，单日便利样本不支持未来自主时间线、普遍两倍加速或部署安全。

## 实际 owner 对照与 Books 建议

已读取 Books context、ROADMAP 与本日最新 checkpoint；具体 owner `MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)。实际读其开篇/约束段、Evaluation ladder（现行872–904）及章节交接（1205–1217），相邻 Ch25/Ch27 开篇交接；另外定点读 Ch66 EvalSpec90–125，未扫描其他月份报告。

Ch26现有正文已分别承载：proposal/controller权限分离（14）、near miss/intervention不能由平均成功替代（27）、perception→真实进展→重复成功→扰动恢复→安全→部署的评价梯级（880–894），以及真实结果须绑定robot/controller/task/initial states/trials/scorer/checkpoint/latency/safety、少量demo只证feasibility（894）。这些是本项最终拟采用边界的具体覆盖，不只是同主题。

**作者建议：已有覆盖，不新增Books正文。** 新的是本次便利样本的局部接入/人工辅助测量，不是此前未有的长期闭环机制；不借“未写uplift/Project Fetch”制造长期差额。正式报告可保留该实例与混杂，不把7/8叫自主成功。若 root 认为需额外说明“人机uplift vs autonomous capability”是现有梯级未承载的具体独立差额，可只在 Evaluation ladder 后核此一句；当前不请求实际写入或共享文件锁。

## 待 root 实际核验

仅四点：官方 post 字段绑定与落窗；局部评价命题是否准入；共同耗时/子任务分母及上述反侧是否充分收窄；Ch26这些实际段落是否足以给 Existing。准入、日期、Evidence、Books分别授予，不将单项通过称日级完成。其余首批七项不重复校准。
