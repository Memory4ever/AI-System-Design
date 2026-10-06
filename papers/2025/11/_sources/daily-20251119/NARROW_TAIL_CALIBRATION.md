# 19日既有窄主题请求补正：增量准入校准包

作者Dalton，执行2026-10-04T16:23–16:30+08:00。仅补正既有system/multimodal请求，不重读原11题摘、不扩全日或全月。以下未获非作者校准，不是确定当窗候选、Evidence完成或Books采用。

## 查询、分页与停止

原两请求缺advanced=1，仅返回表单；这次补上参数，每条size50/start0、hide abstracts。original-submitted范围2025-11-14至18只作发现容差，不改变本日public窗口。完整URL/执行时刻/状态在HTML.receipt.json。

- LLM OR GPU：349结果，仅首页50标题/字段，发现一般应用混入后停止，不将349变题摘队列。raw [宽请求](./arxiv_system_original_corrected.html)。收窄LLM AND GPU，实际18结果，第一页全部标题，raw [窄请求](./arxiv_system_narrow_tail.html)及extracted.json；仅支持该主题发现，不代表所有训练/推理系统。
- vision-language OR world model OR VLA OR diffusion：440结果，首页含纯物理/一般diffusion，停止宽入口。raw [宽请求](./arxiv_multimodal_original_corrected.html)。收窄精确词组vision-language AND foundation model，实际6结果，第一页全部标题，raw [窄请求](./arxiv_multimodal_narrow_tail.html)；未将通用diffusion/医学标题变全文队列，不授所有多模态分类召回。
- 在原有有界查漏ID段2511.12500至2511.13800（不含上界）内，8个新可能主线/标题含糊项恢复exact-v1完整题摘，单次id_list/max8，实际8，[原XML](./narrow_tail_abstracts_v1.xml)。NAND12860复用原校准，不重复。ID段是发现停止边界，不是public日期证明；段外标题不声称贡献已关闭/窗外。
- 当前官方abs轻检8项，raw [ABS01](./WEB_NARROW_TAIL_ABS_01.txt)、[ABS02](./WEB_NARROW_TAIL_ABS_02.txt)。未见显式withdrawn/correction声明；VOLTA有v2/v3，PIGEON和Fuse有v2，版本与核心措辞差异隔离，无标记不证明没有错误。

## 六项潜在贡献

完整题摘已实际读；只给旧约束→实际增量→待核选择，不把摘要宣传数值当准入依据。贡献通过且事件落窗后再评分。owner仅ROADMAP路由，未比较这些具体正文，不造缺口或写锁。

| 精确v1 | 最小拟核命题 | 反侧/限定问题 |
| --- | --- | --- |
| [T-SAR13676](https://arxiv.org/abs/2511.13676v1) | ternary CPU memory-LUT瓶颈→SIMD寄存器动态LUT并改ALU→是否改变低比特存储/算术实现选择；INFER-TENSORRT-LLM | 核硬件修改及模拟/实测、precision/质量与baseline，不称现有CPU软件可直接部署；峰值不等端到端 |
| [MACKO13061](https://arxiv.org/abs/2511.13061v1) | 中等非结构稀疏的索引开销抵消收益→format+GPU SpMV协同→50%稀疏的memory/执行边界是否变化；INFER-GPU-MEMORY | 核格式、GPU/model/pruning/质量与dense对照，不以1.5x或所有生产负载泛化准入 |
| [KForge13274](https://arxiv.org/abs/2511.13274v1) | CUDA/Metal优化反馈不直接互换→生成与profiling解释的反馈职责、跨平台参考transfer→profile到rewrite是否新增可核路径；AGENT-REFLECTION | 双agent/编译feedback组合自身不足；核实际传递、fixed-budget单agent/transfer消融和正确性，不因摘要无实验细节关闭 |
| [VOLTA12638](https://arxiv.org/abs/2511.12638v1) | 随机测试不能证明优化kernel等价→受限GPU程序类的形式equivalence checker→优化验收能否提高为受限证明；INFER-TENSORRT-LLM | 核program class、浮点/并行假设与unsupported回退，非任意CUDA保证；v2提交Nov18不直接作公开事件 |
| [PIGEON13207](https://arxiv.org/abs/2511.13207v1) | 高层VLM频率/低层连续动作不匹配→PoI选择+snapshot与planner接口产生RLVR数据→语义策略与动作频率/监督接口是否变化；MULTIMODAL-EMBODIED-VLA | 核具体PoI/奖励资格，不借通用层级控制；v2扩充raw grounding/实机声明不回填 |
| [Beyond Mimicry13630](https://arxiv.org/abs/2511.13630v1) | 单点选择易被解释为稳定偏好→trade-off强度/切换点/时间horizon局部失稳→偏好一致性测量应否条件化；PLATFORM-EVALUATION-SYSTEM | 只核行为与条件反侧，不采内部architecture/真实主观偏好；核scenario/prompt与重复/检验，负面局部证据不自动排除 |

## 两项代表性拟排除

- [FLOWER13357v1](https://arxiv.org/abs/2511.13357v1)：完整摘要是SQL实体关系采样/推断/可视化；LLM仅作data-storytelling比较，没有foundation-model训练/推理/平台机制具体增量。拟范围关闭，不以GPU/LLM关键词准入。当前单v1，无显式相关纠错/安全说明；日期不定不影响该范围判断，不另追日期。
- [FuseSampleAgg13645v1](https://arxiv.org/abs/2511.13645v1)：摘要是GraphSAGE一/二hop sampling+mean聚合融合、index replay，Reddit/OGB，不直接承载LLM模型计算问题；拟不由general CUDA类比准入。当前v2题名转KG refresh，51x headline转FP32 tuned DGL 2.24–3.48x，不能自动称纠错/撤回，也不以LLM-assisted extraction倒推v1贡献。请root核是否漏掉可直接支持基础模型计算的共享机制；若出现实际纠错反证仅读受影响对照，不先全附件。两版性能均未采用/评分/Books。

## 日期原字段

API exact-v1 published=updated：T-SAR17日18:32:03Z；MACKO17日07:10:37Z；KForge17日11:46:43Z；VOLTA16日15:09:14Z；PIGEON17日10:19:13Z；Beyond17日17:41:48Z；FLOWER17日13:23:24Z；Fuse17日17:57:18Z，均为2025-11。当前abs submission history一致，但这些不是public；搜索只给originally-announced November月份。

六潜在项未确认落窗，不计确定候选、正面证据/Books。最小替代为各精确v1实际官方公告或可靠首公开上下界完全落窗。随后实际逐项DataCite有限恢复，原JSON/receipt在下表；Available仍仅2025-11，Updated/registered不认证public。共同失效日级announcement/API过滤不再空重试，不展开实验附件或盲搜所有作者项目。以精确v1公告/可核发布快照为替代，有材料才重开对应项。宽请求失配已纠正，不用HTTP200授Coverage。

| ID | v1 Updated原UTC | registered原UTC | 原JSON |
| --- | --- | --- | --- |
| 2511.13676 | 2025-11-18T03:07:11Z | 2025-11-18T04:53:54.000Z | [T-SAR](./2511.13676_tail_datacite.json) |
| 2511.13061 | 2025-11-18T02:28:30Z | 2025-11-18T04:39:07.000Z | [MACKO](./2511.13061_tail_datacite.json) |
| 2511.13274 | 2025-11-18T02:43:43Z | 2025-11-18T04:43:55.000Z | [KForge](./2511.13274_tail_datacite.json) |
| 2511.12638 | 2025-11-18T02:04:28Z | 2025-11-18T04:29:25.000Z | [VOLTA](./2511.12638_tail_datacite.json) |
| 2511.13207 | 2025-11-18T02:38:32Z | 2025-11-18T04:42:26.000Z | [PIGEON](./2511.13207_tail_datacite.json) |
| 2511.13630 | 2025-11-18T03:04:56Z | 2025-11-18T04:52:47.000Z | [Beyond](./2511.13630_tail_datacite.json) |

VOLTA v2 Submitted为2025-11-18T05:20:44Z、Updated为2025-11-19T01:26:27Z；上界跨09不能反证窗外，版本号/措辞变化不直接授重要修订。v1/v2首次公开均不确定，只有实际事件证明到达才重开，不能回填v3结论。两拟排除的完整题摘与当前修订信号需root分层核，不冒称已非作者关闭。
