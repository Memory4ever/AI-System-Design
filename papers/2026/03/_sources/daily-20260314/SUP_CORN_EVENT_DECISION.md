# Cornserve 12118 / 2512.14098 同家族事件门

本轮作者mar14_supplement；非作者最终事件校准待root。只核首包明确的record-and-replay差额，未全PDF/版本diff/全部实验重审。

实际原件：`SUP_CORE_12118.raw`精确2603.12118v1，`SUP_EARLY_CORN_CORE.raw`精确2512.14098v1，`SUP_EARLY_CORN_ABS.raw`及`SUP_EARLY_CORN_REPO.raw`。当前稿§2.2（inspect_source B54–57）与先稿§5.2（B202–204、B234）直接对读：

- 当前record phase把unit task调用替换为placeholder，matching object ID恢复请求subgraph/data dependencies，dispatcher执行，replay phase同invoke方法返回real result。
- 先稿§5.2已经写出同一record mock results→按mock object匹配subgraph和dependencies→Task Dispatcher→replay real results流程，且显式说record不执行模型计算。
- 当前deterministic request-conditioned control flow、record/replay同路由的限制已由先稿§5.2末段明确；先稿还保留“两次invoke不能有side effects”。当前文没有可核的此次新增保证或此前失效边界纠正。loops/branches并非本次新增；先稿§5.2 Listing2已含replayable_choice例子。
- 当前§1/§3的3.81×throughput、5.79×tail数字已在先稿完整题摘；本次新ID不形成新family。当前references[8]明确引用旧Cornserve正文为planner来源。官方repoProject News明示2025/11/14 release；该版本声明只作公开线索，不据此认证代码实现。旧arXiv2512编号按官方ID分配规则即表示2025-12首次arXiv公告，足以排除同机制在2026-03-13首次公开，不须追旧精确时分秒。

裁决建议：**同家族旧机制重呈现，贡献前关闭本次事件**；不评分、不新增候选/Books，不声称旧研究没有贡献或所有后续版本绝无新增。没有完整比较当前所有模型支持/应用/API，也不把该未查范围转成深审队列；首批准入所指的决定性record-and-replay增量已被先稿直接否定。未来若有具体新增兼容性/实现约束或新质量资源命题，再定点恢复真实事件而不是新ID自动准入。

root 独立事件复核通过：实际读当前精确v1的 Record-and-Replay Execution 完整局部及2512.14098v1 §5.2从runtime record、mock result matching、dispatcher、replay到双调用副作用/同请求deterministic限制的完整局部；先稿Listing2还已有replayable_choice与loop/branch说明。第一包所指接口差额不是此次新增。两稿既有性能数字同源身份已核，不因此重审旧全文实验；只关闭本次这个重呈现事件，无新评分/Books，无日级验收。首次解析工具缺少可选bs4，已用标准HTML解析读取原件，不算正文受阻。
