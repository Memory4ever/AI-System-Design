# 2025-11-12 第二批独立准入校准

复核者Codex / Ohm；作者Noether，author != reviewer。实际工具clock 2026-10-04T20:40:43+08:00。本日治理fresh加载见[FIRST](FIRST_INDEPENDENT_REVIEW.md)，本批只12原源/窗口，不继承其他日池。

**本批结论：16个完整exact-v1题摘的具体潜力通过；公开日期仍隔离，不是16个确定当窗候选或Evidence/Books完成。** 作者可以沿该有限范围收束日期保留与必要反侧，不要求全实验/全部owner。GPT-5.1同家族RSS落窗另已通过，不能把本批Atom权限套给官方RSS，也不能反过来给本批造日期。

## 1. 实际入口校准

亲读[原第一轮query/执行](12-arxiv-query.json)、[收窄query/执行](12-arxiv-narrow2.json)，submitted区间只作可能公告线索。模型首条all主题总282而仅取60，见过宽停止后用title/形成机制查询45；system9、MM/Agent57未满60的单页止点有效，不扩全282或月1527题摘/全文。该停止不等于全学科召回，也不由先前宽查询证明所有主题已查完。

实际结构化解析[batch1 XML](arxiv-exact-v1-batch1.xml)：16个唯一entry，ID均v1；16个完整题名/摘要及本返回comments逐项亲读。没有拿current题名或v2+摘要替代v1；本返回所见comments未显示撤回，不声明完整版本史无信号。常规schedule只给公告批次可能范围，Atom published依然提交，不补每项09:00精确公开。作者保存月表部分响应不能授完整公开列表；必要历史日期恢复有限失败可隔离，不重试全月。

## 2. 十六潜力的最小权限

| v1身份 | 实际题摘后的独立判断 |
| --- | --- |
| 2511.05811 MOSS | 两级global/local microscale与weight scale预测确有精度/更新成本设计方向；34%及7B对照还只是AB，不授训练稳定性普遍率。 |
| 2511.06010 MoSKA | unique/shared上下文的跨请求GEMV→GEMM路径不是仅共享缓存名字；538.7x严格限high-sharing workload，不能当普通单请求增速。 |
| 2511.06029 Lethe | layer budget加多轮decode relevance/recency修剪确有长生成路径方向；不是只prefill压缩收益，2.56x不授SLO或所有reasoning任务。 |
| 2511.06605 DMA Collectives | v1原名及MI300X大/小消息性能、能耗、同步代价的方向成立；小消息4.5x/2.5x慢到优化后的局部结果必须分开，不倒灌DMA-Latte新名。 |
| 2511.06174 LUT-LLM | activation-weight coquantization、centroid search/2D lookup及缓存安排给具体FPGA memory-compute分支；AMD V80定制模型与GPU对照不授全GPU普遍替代。 |
| 2511.06134 Maestro | CLPO把decision gradient与rationale listwise objective分开，准入不只中央/执行角色换名；6%平均/10%best未授独立可比效果。 |
| 2511.06411 SofT-GRPO | Gumbel随机性/soft embedding及重参数化给训练路径差额；Pass@1 .13%与Pass@32 2.19%不可合成单样本稳增。 |
| 2511.07317 RLVE | 程序化可验证环境按policy调整difficulty分布提供具体信号取舍；400环境人工工程代价不忽略，1.5B局部不因规模关闭。 |
| 2511.07372 Curriculum Tree | uniform-branching/states-conditioned tree与相邻stage complexity条件是理论准入锚点；指数到多项式不能离开该模型外推一般CLM训练。未核全证明。 |
| 2511.07378 Length Generalization | synthetic state-tracking代数/attention concentration和递归self-training保证是模型形成条件方向；不将常深Transformer结论变成无限真实任务能力。NeurIPS full-version原comment需保持事件身份，不能Submitted赋日。 |
| 2511.07482 AAPP | 动态pruning保护alignment相关channel是具体质量/资源潜力；50%refusal不等安全保证，必要反侧见第三批。 |
| 2511.06212 RAG-targeted attack | meaning-preserving retrieved描述扰动损伤具体缓解输出，保留LLM证据链局部负侧；不采IoT领域防护普遍结论或真实攻击防御安全。 |
| 2511.06606 SPUR | FOA四通道rotation-aware/listener-centric表示保留空间参照，超过泛“adapter新任务”关联；sim/real与非空间能力代价尚未核实。 |
| 2511.06136 OCWM | reconstruction/prediction/OOD好而控制差、interaction latent drift是明确表示→policy反侧；只AB所支持方向，不归因所有控制失效。 |
| 2511.07416 PhysWorld | 视频重建physical world、object-centric residualRL把视觉轨迹接到执行动作，主线直接相关；zero-shot实际机器人只是任务范围，不授安全包络。 |
| 2511.07399 StreamDiffusionV2 | online逐帧deadline/SLO-aware调度、rollingKV和跨去噪/层pipeline给具体生成runtime方向；两个FPS分别绑定14B/1.3B与四H100，不说所有配置无条件near-linear。 |

## 3. 关键安全增补与剩余工作

AAPP本轮实际读[原v1](safety-aapp-v1.html)Methods至Conclusion：Table1与紧邻prose数值冲突、FLOPs估算及语言能力下降的toxicity混杂均已核，不能仅refusal率当“安全保留”。还见Fig2“更接近harmful时fires”的叙述与正文`KL_harm-KL_safe >= tau_margin`分支需区分；距离越小才越近，原核心没有给本批可核阈值符号/代码解释，不能把二者无条件等同为已验证risk detector。这是新增限定，不要求日期held项为此遍历代码/全附件；保留潜力、只不正面采用该门控正确性。第三批将汇总受影响权限。

本批没有评分为确定候选，没有核16项全部methods/实验/owner或写Books，未扩大公开恢复。其余ORDINARY_SCREENING的118题摘/关闭层还不是本批全部通过，需按实际潜力与分层关闭继续必要独立校准；不能用本16通过给134全体盖章。日级仍未通过，正式README/完整来源终态与六部分待作者ready后实际核。
