# 11625 MedPruner：actual delta最低关闭提案

mar14_supplement，03-14只补Mar13 BJT。root完整题摘七窄P准入有效复用；SUP_DATE_STOP_NARROW.md保存实际七日级门，待非准备者独核日期，不由本提案自授。SUP_STOP_GATE_MANIFEST_RESULT.json记录exact-v1官方HTML GET200/185030B；实际读取§1–2.3/Eq1–5、§3.1–3.3完整Tables1–3及§4（inspect_source B1–61，B37–42在输出截断后定点恢复）。不读代码/全部参考/旧版本/所有阈值图曲线或临床部署；当前可见说明无具名撤回/纠错，不将v2编号本身当重要修订。

准入保留：固定token预算难适应slice信息密度→像素L1 active-anchor去相似slice，再按vision attention温度归一累积质量取最小top-k，剩余token沿VisionZip bipartite matching/clustering→局部改变3D输入的压缩预算。实际新增是这一选择器配置，不是attention mass等于诊断证据的保证、新的全系统预算协议或临床可靠性机制。**拟1+1+2=4最低关闭/仅报告Books0**：Design1针对局部压缩recipe，Reach1针对视觉输入组件，Durability2针对可复用但有限的自适应预算设计；不把借用nucleus/聚类成熟原则或可映射Ch23计重要机制。P不撤为EX，未以领域、已有Books或费时降分。必要支持与直接反侧足以判断不进一步采用，不启动owner差额/PRE。

§2.2 Eq2–3：第一slice初始anchor，像素均值L1大于γ保留并替换active anchor，小于γ过滤，等于γ未给唯一分支；像素距离是形态代理，不证明微小病灶可丢。§2.3 Eq4–5将self-attention跨head/sequence平均，softmax温度T后降序，取最小k使质量≥τ；未被选token依既有VisionZip匹配聚类再与primary concat。集中权重会减少token，不证明attention就是事实重要性或所有空间细节被保留；不补造cluster精确实现或γ/T/τ唯一生产recipe。

Tables1–3实际反侧限制宣传：MedGemma在3DRad accuracy提高但ROUGE-L/BLEU-1/4均退；AMOS-MM MedGemma保留2.46%token，38.001→35.889s，不能把97.54% token下降说成同比E2E速度收益。Qwen3-VL的AMOS-MM平均相对n-gram分数95.86%，不是全部模型质量无损。Table3 IAF-only平均92.13%；primary+redundant平均100.07%却9.586s慢于baseline9.212；完整配置99.19%/7.931s，不把另一行的>100%移给完整配置。作者Average是多种语言指标相对baseline比例的均值，不是独立诊断准确性/真实患者安全或语义完整性证据。

§3.1披露Hulu-Med-7B/MedGemma-1.5-4B/Qwen3-VL-8B，三3D数据集，8×H20；closed VQA Accuracy、open/report BLEU/ROUGE/METEOR不同协议，不合并为通用质量真值。batch/concurrency/precision/输入输出长度/SLO与重复运行不确定性必要处未披露，不补造端到端服务配置或部署认证。v1 abs写MedGemma，必要v1 HTML已写1.5；只保这精度差异，不串current-v2 GitHub/code已发布状态，也不为无未决命题全版本diff。

待非Source作者实际必要方法/关键Tables反侧及低分理由复核后正式同步；无Books写入，无DAY声明。
