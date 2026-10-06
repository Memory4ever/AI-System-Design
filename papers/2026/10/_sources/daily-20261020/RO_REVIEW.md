# 2026-10-20：四项 RO 独立必要证据复核与 Books 写入交接

仅北京时间 Oct19 自然日；不续跑历史 Daily。Source 作者 root，独立必要证据 reader `oct20_author_resume`。本文件记录已经发生的实际阅读与窄写，不是复现、全附件审计或整日验收。官方当日公开日期与完整题摘校准沿本日 ARXIV_SYSTEMS/ARXIV_ROBOTICS 的有效记录；本次独核不以 v1 页中的提交日期替代公开日。

## Source 复核结论

四项均保留作者原有准入、Score V2 与受限采用，不因现有 Books 或阅读成本缩池。

| Family / 分数 | 本次实际独立读域 | 机制、反侧与有限结论 |
|---|---|---|
| 2610.23378 / 3+2+2=7 | [exact-v1](https://arxiv.org/html/2610.23378v1) III-A–D、IV-A–C、V；本地 `ro_review_assets/html_23378.visible.txt` | AP 改变相机与机器人交接状态；恢复示教初态、执行部署 AP、早期示教前缀近邻、闭环对齐及成功后缀重放形成 manipulation 训练数据，AP 动作本身不作该 VLA 监督。匹配进度/后缀/成功筛选/数量/预算的控制支持交接适配；成功筛选不证明部署分布相等，标准初态近持平。需可重置环境/可重建工位，换 AP 可能重制数据；有限实机与短 chunk 不授安全。训练、reset、失败筛选、对齐和执行全费。 |
| 2610.23372 / 3+2+2=7 | [exact-v1](https://arxiv.org/html/2610.23372v1) §3.1–3.5、§4 关键对照、Limitations、F.1、G.1–G.3；本次网页实际返回，未伪称有完整本地缓存 | 净收益 `(b-c)/n` 与任一结果翻转 `(b+c)/n` 分开；内容归因须同 fact / 异 fact、exact repeat、安装路径与实际读取控制。C 绕过安装而 U/S/T 共用安装，U−C 不纯是数值噪声；delivery 不等内容利用，latent 编辑未认证语义事实。G.1 只撤 full-vision ladder 对 Q3/Q4 的证据，不撤全篇。202 shared execution 与143 rebuilt manifest 不混池、不当独立闭环，重建选择偏差未消除。非显著非等效、事后整理非全程预注册。 |
| 2610.22576 / 2+2+2=6 | [exact-v1](https://arxiv.org/html/2610.22576v1) §2–6、主要控制/限制；本地 `ro_review_assets/html_22576.visible.txt` | 两本体成功 rollout 的加噪 action 分类器提供密度比梯度，修正冻结 flow sampler；非零目标本体数据、非新任务泛化。无图/任务输入仍可能有 action pose 混杂，clamp/20% cap 与权重是实际启发式。弱/锁腕可退步，已知 delay 规则可更好，启用规则未通过；事后 guided collection 受 transfer task 启发，不纯 holdout。分类器训练/每步梯度/重采全费，完整延迟未受控测量。 |
| 2610.23566 / 3+2+2=7 | [exact-v1](https://arxiv.org/html/2610.23566v1) III-A–F、Alg1、IV-C/D/E/F 的必要对照与成本；本地 `ro_review_assets/html_23566.visible.txt` | 白盒构造期在攻击诱导的新状态查询 target 指令行为，刷新监督；停滞前沿与此前位置前缀共同约束固定扰动，部署 user 指令不改。共享状态/匹配抽样量支持局部机制，不把不同优化配置的全部 ASR 差归一模块；位置前缀非抓取事实，冻结 teacher 不会恢复时新 target 仍坏。梯度/状态访问/目标查询/重复 rollout/控制全费；含加载的计时及每条件15次实机不推广为通用成本或防御失效率。 |

23372 的本地抓取出现 `IncompleteRead`，只保留实际 request 结果；网页 exact-v1 已完整返回上述必要域，因此不是 Source 阻塞，不需为本地副本重读全篇。其余三项保存原始 HTML、可见文本与请求记录。均未检查图片/视频、代码或运行实验。

## 实际 owner 比较与已保存差额

先读 ROADMAP、PROJECT_CONTEXT、LEARNING_PHILOSOPHY、WRITING_GUIDE 和当前相关 checkpoint；历史暂停 checkpoint 仅路由，不作重启授权。以下节点/路径来自当前 ROADMAP。root 明确授权这三个章节的指定窄新增；其他 agent/既有 staged 内容保留。

| 事项 / owner | 实际原覆盖与差额 | 新增正文与非 writer POST 入口 |
|---|---|---|
| ActiveAlign / `MULTIMODAL-EMBODIED-VLA` | Ch26 主动相机/共享两 head 已覆盖视角选择及训练接口，但未明确 AP 终点如何成为 manipulation continuation 的训练支持；新增交接分布适配分支与对应 reset/筛选/失败边界，不接管表示或动力学。 | [Ch26](../../../../../Books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) 新112、114；完整新增/直接两侧实际读回104–124；本人注1961。 |
| Classifier guidance / 同 owner | Ch26 原语言/视觉 velocity 差分已能承载采样修正，但不等成功 rollout 的跨本体密度比修正；新增冻结 sampler 分支及 pose/成功支持/锁腕/已知规则/holdout/延迟边界。 | 同 Ch26 新990、992；完整新增/直接两侧实际读回978–1001；本人注1963。 |
| IMEP / `PLATFORM-EVALUATION-SYSTEM` | Ch66 Context knowledge/use、FACTS 与后续 RAG 已覆盖知识/使用分账，不等 memory fact 替换的受控内容归因；只补评价合同，不复制 memory runtime，也未改 root 23254 两段。 | [Ch66](../../../../../Books/part-06-ai-infrastructure/66-evaluation-system.md) 新1536、1538；完整新增/直接两侧实际读回1526–1553；本人注5222。 |
| TRACO / `PLATFORM-SECURITY` | Ch72 VLA 黑盒反馈威胁与后续 Agent 进度/停止覆盖运行时反馈；未覆盖白盒构造在自身诱导状态刷新监督、维持前缀的压力。只补威胁构造与权限/费用边界，不承诺防御，不接管 Ch26 controller 或 Ch66 测量。 | [Ch72](../../../../../Books/part-06-ai-infrastructure/72-security.md) 新3254、3256；完整新增/直接两侧实际读回3249–3270；本人注3485。 |

正文共8个自然段，各带对应 `SF-2026-ARXIV-2610-xxxxx` marker；自身 Review notes 共4条。`oct20_author_resume` 已实际顺读全部新增、完整直接两侧和本人注；这些是 writer 自检，不替代独立 Books POST。最终锚点随其他并发局部增补可能移动，SF marker 和段首为稳定定位依据。

## 状态与交接

- 四项 root 作者 Source 的独立必要域复核通过；不是代码/实现验收。
- 四项 Books 判断是具体差额后窄整合，已按 root 授权保存；writer 为 `oct20_author_resume`。root 后续已实际读回上述8段、完整直接两侧和四条本人注，确认必要原证/因果/费用/反侧与衔接、23372局部撤证及23254未改，**真实非 writer POST 通过，Ch26/66/72本次指定窄位释放**。此为 root 已成复核结果的行政同步，不是 writer 自签。
- 已执行 scoped `git diff --check`，未 stage/commit/push；并发/未纳入 diff 的内容不能靠此命令获语义或全树验收。
- MM Books 仍由 root 处理；本轮未写 LS，不签整日报 DAY，也不扩大来源或恢复历史任务。
