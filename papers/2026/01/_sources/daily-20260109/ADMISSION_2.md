# 第二批完整 exact-v1 题摘准入提案

原页完整摘要、版本/history见ABSTRACTS_2_RAW.txt；均已实际读完整题摘，未见撤回/纠错/安全标记，普通后续revision不自动扩审。Submitted字段仅用于发现，日期/较早原公开待核；不算当窗确定候选、Evidence或Books通过。

- 2601.04071v1 Hummingbird：闭源GPU任务无法细粒度回收时片→microsecond-scale preemption与SLO优先级调度→需重新考虑低优先级harvesting与高优先级时延的隔离边界。拟2+2+2=6；题摘数字不授硬件普适/生产SLO。v1 Submitted Jan7T16:36:19Z，v2 Feb10普通revision另时段。
- 2601.03511v1 IntroLM：外部query成功预测器引入独立输入窗口/调用→只在introspection token激活的token-conditional LoRA于prefill预测成功→需分开路由风险预测产物与原生成路径是否改变。拟2+2+2=6；须必要core核选择token/额外prefill与独立标签人口，不采matched reliability保证。v1 Jan7T01:48:17Z，后续May9版本不作本窗事件。
- 2601.03782v1 PointWorld：joint-action接口限制跨embodiment dynamics复用→将机器人动作与预测per-pixel state displacement同置3D point-flow空间→需核action几何编码是否保物理尺度/partial observation及MPC可消费条件。拟2+2+3=7；拟新增命题是state/action表示接口而非数据规模/0.1s与普适操纵保证。v1 Jan7T10:29:12Z；project页首公开线索待定点核。
- 2601.03542v1 Layer-Order Inversion：从层级解码次序推hop-aligned内部计算→later-hop answer可早于bridge decodable的局部反证→需分开可读出次序与因果计算顺序，不因probe解释框架采真实内部机理。拟2+1+3=6；长期新增反证针对该特定层级假设，非借成熟因果原则抬分。v1 Jan7T03:13:03Z，后续Aug26普通revision不作本窗事件。

root已独立实际读四份完整AB，6/6/7/6准入校准通过；未授Evidence/Books。准入后的评价可信度只在必要Evidence审阅处理，不把AB缺实验细节当贡献前拒绝。
