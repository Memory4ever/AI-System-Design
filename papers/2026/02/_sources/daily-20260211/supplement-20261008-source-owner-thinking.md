# Thinking States：必要Source与单owner差额/PRE请求

身份：2602.08332v1，2+2+2=6，已root AB/本批Feb10BJT上下界核验。不存在目前可核更早项目正文事件；不采用当前会议标签为first-public日。仅本家族，无artifact/复现。

原件：`supplement-20261008-thinking-core.json`完整§3/4；`supplement-20261008-thinking-direct.json`官方v1 Appendix A.1/A.2与Alg1、A.3及实际A.5预算条件（工具必要段扩展返回，不把参考文献作证据）。

## 作者实际采用范围

§3.1深层chunk→轻量T生成自然语言→C压成c×d状态→下一chunk浅层相加；auxiliary thought tokens不追加主backbone context，但仍付额外head/压缩/生成成本、原causal KV照用。§3.2 gold chunk thoughts不仅监督T，也teacher-force C出的state，消去跨chunk BPTT以并行训练；不授部署gold history或所有训练免费。

§3.3/A.2 prefill假定后续state trivial、找到最早非trivial边界、仅此前H/KV固定并重算suffix；R+1只是该假定/一致生成的轮次，非固定TTFT，Alg1 hat0/EOS和索引呈现不作为本次已核执行契约。本文不说明随机generation的RNG等价，故不授任意随机采样路径严格同分布。

§4 Qwen2.5-Base .5B/1.5B task fine-tuning，A10080GB作者walltime；GSM CoT60.50、Thinking42.22/2.66×，比Coconut32.65/3.14×更准却更慢，不能“CoT相同质量更快”。2Hop FK54.91vs54.79/1.19×、PK43.05vs43.07/1.23×，小差值不判显著。Parity/Vars训至ID100%并不匹配训练总步费；NoCoT/CoT的数据接口也不同，反向不能认证纯架构因果。A.5.3 forward/backward计时batch1,L128非完整制备成本；GSMteacher alignment375101/385620、标注过滤额外费，不是完全相同监督权限。precision/服务batch并发/SLO/CI未披露。

直接反侧§4.4 chunk过小/过大皆退、c8局部最优；更多deepshallowlayers提高质量却缩小加速；§4.5尾部问具体quantity时早state可算错目标，前置question42.22→48.65仍低CoT；作者归因于causal+state组合，不独立认证全失败原因或双向必补救。thought可见不等faithful内部轨迹。

## 实际owner差额

MODEL-TRANSFORMER-LAYER Ch17当前511–539完整已读：533/535是新增continuous input positions，537是past高→低投影旁路；549–555（本日Adaptive）是2Dmask/reach。均尚未解释“可监督auxiliary自然语言→固定state→后续原input位置”及gold-state并行训练/线上chunk等待的责任差异。Ch16/18交接已实际读，目标Ch17，不另写训练章/Prefill副本。

拟一段放535后/537前，保原continuous input和projection分支。未获Source/PRE/写锁，未写Books。

## 最小拟文

跨位置反馈还可把可监督的中间思考留在辅助模块，而不追加主模型的输入位置：读取一个 input chunk 的深层表示，由轻量 head 生成自然语言 thoughts，再压成固定大小的状态，加到下一 chunk 的浅层表示。这样以状态递归替代主上下文中的思考 token，但仍运行辅助生成、压缩和原 causal KV 路径。训练若已拥有逐 chunk 对齐的 gold thoughts，可以先压成 gold states 并 teacher-force 各位置，消去跨 chunk BPTT、并行计算 backbone；线上没有 gold history，chunk 之间仍要等待实际状态。预设后续状态为空再固定最早有效边界、重算后缀，只在空状态足够稀疏时改善 prefill，轮数不等 TTFT。有限 Qwen task fine-tuning 的 GSM 质量仍低显式 CoT；问题目标直到尾部才揭晓时，早期状态还会追错量。对齐教师、附加模块与重算都增加费用，thought 可见也不认证内部忠实性；监督缺失、目标晚揭晓或净成本不合算时，保留原 fixed stack、连续输入反馈与可独立验证的显式 CoT。

拟正文链接 exact-v1#S3，note绑定§3/4/A.1–3/A.5.3；root实际Source/PRE后才申请Ch17一段+自身末注窄锁。
