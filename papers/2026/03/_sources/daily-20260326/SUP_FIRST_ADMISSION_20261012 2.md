# 03-26 首批准入校准

作者 supp_mar26_fresh；新增仅03-25完整北京时间自然日。旧 ModelSpec 事件行/日期/评分、09→09窗口及连续旧§4冻结；baseline见 SUP_ORIGINAL_README_20261012.md。当前未授新增Evidence/Books/日级完成。

四主题窄入口first page为84返回槽/75身份；另learning/agent_eval仅第二页各25，停止start25/max25，不转整类或所有未返页队列。实际参数、标题见 SUP_TOPIC_DISCOVERY/SUP_TOPIC_PAGE2；first-v1完整题摘与必要日期见 SUP_FIRST_EXACT_ABSTRACT_DATE、对应arXiv provider原字段见 SUP_FIRST_PROVIDER_FIELDS。

## 日级日期夹逼，而非补造公开时刻

非准备者作者已实际读取 https://info.arxiv.org/help/availability.html 的公开流程、ID/DOI仅公告流程分配、周二14点提交界→周二20点公告及QA可延迟说明。三月24日下午18Z前这6个v1的最早公开日期下界是25BJT；同ID/arXiv publisher/DOI的findable原登记上界也为25BJT，故日级区间收敛25。不将Submitted、v1Updated或registered单字段称为公告/精确时刻，不否认QA延迟；登记日期上界阻断晚一天延迟。初稿身份、当前官方撤回/纠错/修订信号仍逐项轻核。

## 拟入选及采用前仍需核验的命题

| exact-v1 | 原有约束 → 实际增量 → 重新考虑的选择 | 拟分/owner | 当前门 |
| --- | --- | --- | --- |
| 2603.23414 SortedRL | 长尾rollout与整批同步产生bubble → 长度先完成组先更新、缓存暂停长轨迹并控制staleness → 更新batch与生成batch是否必须耦合 | 2+2+3=7，TRAIN-GRPO Ch33 | 准入潜力清楚；必要方法/评价/直接反侧待阅 |
| 2603.23049 PCR | reuse命中率与多级加载分开优化 → 用pending queue前视LRU、层级CUDA流重叠和SSD预取联动 → eviction不能脱离已知将来需求/加载路径 | 2+2+3=7，INFER-KV-CACHE Ch45 | 准入潜力清楚；必要Source/PRE待阅 |
| 2603.22774 CPU | 充足GPU/graphs不保证control-side供给 → 受限CPU导致tokenization/kernel launch/通信停顿且加CPU恢复 → GPU配额应与CPU供给绑定、不能仅以GPU饱和率判能力 | 2+2+3=7，INFER-SCHEDULING Ch56 | 必须只采用v1的1.36–5.40，不能借最新摘要agentic/v3倍率 |
| 2603.23117 TRAP | 可解释CoT通常被看作诊断信号 → patch定向改变中间推理并驱动错动作 → 解释文本不自动是可信行动依据 | 2+2+3=7，MULTIMODAL-EMBODIED-VLA Ch26 | 安全反证必要深入，不由摘要采用攻击率/通用防护 |
| 2603.22858 DPPN | 持久内部路由结构需迁移 → 稳定外坐标仍不保证routing-bias迁移、learning-rate先验与结构completion分别测试 → 记忆坐标稳定性与迁移耦合方式应拆开验证 | 2+1+3=6，MODEL-LONG-CONTEXT Ch22 | 局部负结果不能按小模型/微小增益自动排除；标准+必要理论反侧待阅 |
| 2603.22871 CMM | 递归潜状态收敛/塌缩不明 → contraction/ODE或SDE与hyperspherical repulsion → 稳定推理隐状态是否可代替继续展开 | 2+1+3=6，MODEL-TRANSFORMER-LAYER Ch17 | 算法任务局部数学条件可主线；不照录『取代brute-force scaling』 |

以上6本日唯一family日期拟通过、准入待独立校准。没有因Books已覆盖排除，没有把所有主题关联当候选；正文可读的普通工作不写成外部受阻。
