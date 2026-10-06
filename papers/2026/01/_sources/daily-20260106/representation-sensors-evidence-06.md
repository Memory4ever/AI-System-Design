# Jan06 已知末批表示与sensor必要证据

只处理先前完整题摘中的00352/00426/00791，不新增库存。精确v1 HTML定点检查时间在缓存；Fetched不等全部采用。root准入及处置仍待。

## OmniVaT 2601.00352v1

actual §3.1/3.4/3.5（7222字符全，含尾NOD/Eq9–12）与§4.1–4.3/5。冻结CLIP VIS/TAC/LANG，LANG训练类别辅助、learnable FrFT order/shared adapter与binary linear-node tree，NOD cosine去相关不保证统计独立/所有OOD。四dataset八domain五共同材料类别、单source→其余targets、三seed、RTX3090，Table4同modality对照及Table5/6局部消融支持受限替代；完整pipeline75.2FPS是batch16，不授30FPS sensor单请求real-time/SLO。学得fractional参数、损失/树成本与下游classifier都保身份。

3.4/Eq5–6显式使用LANG及同类global token，图3说明LANG仅training；未披露完整test去LANG路径，不凭公式猜实现。root完整AB准入校准指出原理由仅feature-space可映射Ch23过宽；actual core只有五材料classifier的FrFT/sharedadapter/linear-tree局部组合及domain指标，未改变foundation/VLA机制或sensor schema/calibration合同。作者据具体原增量纠正为贡献前关闭，root actual完整AB及§3.1/5独立校准通过；不保原拟5为正式评分；保actual材料/反证，不因费时/Books已有缩池，也不将其他foundation新表示机械排除。

## RMAAT 2601.00426v1

actual §3.2.1/3.3/3.4/4.1–4.2、Appendix D AMRB Alg1及E.2–E.3。retention scalar来自预设TotalSegments的生理仿真并乘固定M×d memory；不是动态减少state字节。§4.2去retention accuracy下降但memory同3.4GB；AMRB换standardBPTT才增加activation峰值。LRA从scratch、ListOps长度/各baseline来源不同，Pathfinder速度0.95×反收益，RTXA5000/PyTorch1.13.1/CUDA11.7且具体precision/重复计时未披露；不授普遍速度或LLM长上下文无损。

AMRB保存segment输入状态、反向重算是明确机制，但Appendix D关键链存在未决：line10只重算m'，line13对m'.backward接未来对m的gradient，未显式重建retention乘法；解释却称AD隐式含该scale。line12先L.backward没有retain_graph，而第二次line13才retain，解释与PyTorch graph释放次序不一致。未运行实现、未宣称梯度一定错误；需要精确可执行code或勘误解释detached state/retention因子/两个loss VJP及gradient累积。拟2+2+2=6保持，不以疑点降分删候选；精确梯度等价及其性能归因不得采用，其他有限表示事实可独立保留。

## Geometry of Reason 2601.00791v1

actual §3.1–3.4、Dataset/Evaluation protocol/Control1–2/accuracy解释/4.3/4.7/5.2–5.4/limits，必要B.4和D.1统计；不全读附录plots/全模型表。Attention symmetrized图+hidden-state谱能量，阈值/metric/layer需有标签校准约50example；heldout73.6–83.5%、nested82.8–85.9%，不是AB的89–95全data调优与无trainingdata共同保证。454样本初始154human valid/300model invalid，model-vs-model仅16+16、humanperturb154+40仍长度/编辑改变不唯一逻辑因果；query projection ablation改变谱，不证明谱改善能诱导有效证明或正式kernel认可。跨architecture不同model不唯一控制SWA因素。A10040GB、额外O(N³)谱计算50–200ms，不授线上sensorSLO。

中心争议：§5.3因spectral判valid/Lean判invalid的disagreement做manual correction，且每model gold valid187–205不同；没有独立blind adjudication/parser/version的统一标签，不能用按被评sensor选中的纠错样本反证其自身可靠。§3.1所有dense head质量s_h=N故Eq2 mass weighting=uniform，但Table19两行输出不同；必要实现/稀疏定义/对应data不足。§5.2说Fiedler上升=loss connectivity，与§3.3 Fiedler值越大连通越强相反，不能授health因果。拟3+1+2=6不降分；暂缓中心有效推理classifier/校正标签保证，需独立统一proof-adjudication及exact scorer/aggregation/config解释，只重开该命题，不把所有论文内容判无效。

root非作者已实际复核本文件具名中心决定性原段，受影响保证隔离终态通过；此记录不授全篇无错误/代码复现失败/性能普遍性，也不替代其余家族或日级Gate。

## 最终处置同步（2026-10-02，日级Gate待root）

当前最终处置：OmniVaT贡献前关闭经root完整AB/§3.1/5实际校准；RMAAT6与Geometry6的中心梯度/label-calibration保证安全隔离终态通过。Table19原差异未被root实际核，不作独立已确认依据；决定性Geometry处置依5.3/D1的sensor-disagreement改gold与head aggregation原定义。
