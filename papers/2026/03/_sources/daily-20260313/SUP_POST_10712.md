# 10712 FutureVLA：实际非 writer POST

复核者：mar13_admission_review；准备者 mar13_supplement，Books writer root。仅 Daily 2026-03-13 / 补充窗口2026-03-12 BJT。启动实际重读 AGENTS、当前 Research/Report/Prompt、Sources 使用说明与 Daily/arXiv 范围、ROADMAP、本日 README 与 LEARNING_STATE 本日停点。准入、日期、5=1+2+2与必要 Source/owner 比较复用 [本篇独核](./SUP_INDEPENDENT_10712.md)，不重开日期或异日材料。

## 实际正文与完整邻接

实际顺读 [Ch26](../../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) 当前278–298：加性 action-facing 重建完整两段 → forward/inverse 完整两段（282/284）→ 本篇新增两段（286/288）→ 导航动态区域完整两段（290/292）→ 几何 latent/路由相邻内容。实际读取 root 本篇 Review notes 完整条目1579，不凭提案或 diff 代替正文。

原 forward/inverse 无动作标签预训练、固定 forward/更新 inverse、丢弃 decoder、有限实证及 BC/controller 回退完整保留；导航定位先验、光流区域辅助监督、删除辅助 decoder、合成/标签费用和 waypoint/control 验收完整保留。新增有动作标注的双目标分支处于两者之间，区分了监督来源与目标选择，没有静默覆盖旧方案或把预测表示接管物理提交权。

## 实际回源与三修确认

本次又实际解析 [exact-v1 原响应](./SUP_CORE_10712.raw) 的完整§3/Eq1–7、AppA1–2、AppA4及完整 Tables4/5/13；其余未变的已核反侧与身份复用，不展开图像、代码或旧版本。

1. 真正写入为“视觉组的重建目标是第一帧的 latent”，没有声称 visual 完全不接动作梯度；共享早期编码、训练期未来特权与“不证明因果解耦”同时在第一段。
2. 真正写入为“分开重建与动作监督提高所测均值，再条件化进一步提高均值”。回源T5：62.5→仅多帧58.4→双监督65.6→加JVG71.9，双监督在没有JVG时已经高于基线；没有残留“必须gate才改善”的暗示。
3. 真正写入为“加入条件化的 StackCube 对照”，回源T5(c)37.5→(d)29.2，是JVG整包而非scalar gate单独对照。T4 OT Carrot58.3→54.2与已核T7任务反退未被平均收益掩盖。

T13 last/first均值68.8/71.9仅两任务提高、两任务持平；正文只称局部第一帧结果，不采用原文“strictly necessary”、pure physics或语义相似度→物理真值。Eq1覆盖M′/Eq5方向未被写成可执行公式，末注明确不采精确recipe；正文采用的是§3/AppA一致的双监督、motor查询visual、固定teacher→当前观测VLA适配与动作监督接口。

Teacher/codec训练、未来视频/动作标签、重建decoder、冻结teacher前向与student后训费用在机制旁；训练step时间没有变成控制deadline。接触真实反馈/controller与BC、显式动作监督、原policy/低层校验回退均保留，属于工程判断，不称论文实现自动安全。root将“支付监督分工”改为“划分监督职责”、清理多余空格，并将“不改推理架构”标为带引号的描述，均使语文/权限更准确，没有增删采用命题。

## 末注 / owner / 结论

实际root末注正确记录精确版本、必要范围、5分与具体gap、三处PRE准确化及双目标不等梯度/因果隔离，明确不核全部像素/代码/复现、当时POST待验、未授DAY。该待验可由writer在收到本记录后同步，不由本reader修改共享文件。

唯一owner仍是 `MULTIMODAL-EMBODIED-VLA` Ch26；此前实际Ch25/23入口核验有效，环境转移资格、3D-VAE表示与真实controller职责不变。本篇未增新章/owner或重复机制到相邻章。

**结论：10712 实际非 writer POST 通过，可释放本篇两段与root本注窄锁。** 当前三处修正与真实正文已验，不只是条件PRE通过。本次仅新增本记录，不写 Books/Report/State/共享ledger，不授日级完成。
