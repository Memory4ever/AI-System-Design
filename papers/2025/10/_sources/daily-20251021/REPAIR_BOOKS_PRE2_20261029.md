# B4–8 完整 Books PRE 提案

仅以下新自然段、独立marker与本人完整末注；未写Books。实际已读owner/完整两侧，Ch5并读Ch4/6开篇，Ch23/25并读Ch24/26，Ch72并读Ch71/73；Books上下文已重载。请sole reader先确认必要证据/key，再整体PRE；无全章锁，无root第三批准，无State/index写入。不是为方法名称缺席造差额。

## B4 15106 / PLATFORM-SECURITY Ch72

文件：`books/part-06-ai-infrastructure/72-security.md`。插在“从边界隔离到受限条件下的可证明执行”末尾现有双曲几何完整段后、`#### Proof of Equation Satisfaction 不等于 Proof of Expended Work`前。当前有参数margin球和密码关系证明，但没有按声明训练输入局部重算末层作为update一致性sensor的分支。

完整新增正文：

训练更新也可先做局部一致性复算，而不为完整训练建立密码电路：从同一前checkpoint、声明batch、seed、optimizer与硬件出发，冻结早层，只重算末部参数，再与报告更新比较，并用诚实run校准差异阈值。[PoTS的受限分支](https://arxiv.org/html/2510.15106v1#S3)将末层敏感性用作可疑update的sensor，不是完整训练轨迹证明，也不证明所有后门已被排除；阈值通过不能替代全模型独立行为测试。冻结早层使连续多步误差积累，LoRA不更新被核末层时也可能不适用；所测Llama需要更高投毒比例才明显偏离，不采统一低比例可检出。声明数据/随机性/数值环境与checkpoint须共同绑定，复算、校准、checkpoint存储与安全回归都付费；异构硬件、长段训练或阈值支持不合时，保留完整重算/可信训练记录、原checkpoint与独立审计，不从局部距离签发训练正确或生产安全。

独立marker：

`<!-- source-family:SF-2025-ARXIV-2510-15106 -->`

完整本人末注：

- `SF-2025-ARXIV-2510-15106` — Daily2025-10-21补Oct20；Lorentz R5首次exact-v1§3/4.1/4.2/5，writer只核LM-head反例/多步与LoRA限制，2+1+2=5；具体局部训练重算sensor差额深入。0.5–1.5B/singleH100/seq128，10%BPR不覆盖Llama、50%反侧保留；不采用密码证明/任意训练全安全/全流程3x。未核实现或复现。

## B5 15041 / MULTIMODAL-WORLD-MODELS Ch25

文件：`books/part-03-multimodal-world-models/25-multimodal-world-models.md`。在现有spring粗校准/共享stiffness residual完整段及独立`SF-2026-ARXIV-2606-16202`marker后、以“生成器还可以补充simulator的资产供给”开始的原完整段前。原段是已设spring模型的参数残差；新差额是从观测同时学低维handle变形基与能量的状态接口，不混为材料参数唯一辨识。

完整新增正文：

若显式spring拓扑还未给出，也可先从观测形变学习较低维的可操纵状态：由静止几何生成handle权重，用handle变换重建观测，再学习各向异性能量来约束这些自由度。[GDGen的受限分支](https://arxiv.org/html/2510.15041v1#S4)同时学习表示与近似动力学，不是只拟合一个固定simulator的参数残差；只有降低观测能量会退化到零stiffness，须另加倒数能量/噪声等约束，而这些正则也不证明真实材料可辨识或形变基严格正交。Handle可驱动渲染不等接触已正确，碰撞仍需外加处理，布料/毛发也不在其支持内。几何/轨迹恢复、基与能量训练、全部交互求解及独立未来轨迹/接触回归都计费；短预测或视觉拟合不足以签发长期物理控制。观测、形变族或接触支持不合时，保留已校准显式模型、逐对象辨识与真实反馈，不让低维可编辑性替真实动力学验收。

独立marker：

`<!-- source-family:SF-2025-ARXIV-2510-15041 -->`

完整本人末注：

- `SF-2025-ARXIV-2510-15041` — Daily2025-10-21补Oct20；writer首必要exact-v1§4.1/4.2/Alg1/5.1/5.3/T2–3/6，Lorentz R15 key，2+1+2=5，handle-basis/energy共同学习差额深入。保零stiffness退化/1E、collision外置、20frame/cloth-hair禁界、对照能力/费用差异；partial267224/310904不冒全附录，不修N(1,0)/Chamfer render为完整recipe。未核像素/实现或复现。

## B6 15227 / MULTIMODAL-REPRESENTATION Ch23

文件：`books/part-03-multimodal-world-models/23-multimodal-representation.md`。在可变长度duration-token完整段及独立`SF-2025-ARXIV-2509-04685`marker后、以“细粒度speech tokens也可以继续保留”开始的原完整段前。原来分时长/内容与局部/全局步长；没有“训练多码、部署少码但重训decoder”的资产兼容分支。

完整新增正文：

减少线上语音码数还可通过改变训练与消费的分工，而不立即把encoder压成同样少的码：先用更多残差码本训练声学表示，再选较少码供语言模型消费，固定encoder/quantizer，仅重新训练对应decoder。[LongCat-Audio-Codec的受限TMUL分支](https://arxiv.org/html/2510.15227v1#S4.SS3.SSS2)把共享token资产与特定还原器分开，不能直接删码后沿用任意旧decoder。平均重构误差改善仍可能伴少量音频识别退步，语义与声纹的消费质量须分验；16.67Hz单元加三帧lookahead也不是完整首包或对话延迟。多码预训、少码decoder训练、原声与语言任务回归和完整波形生成均计费，单说话者适配的相似度不授未见身份泛化。码数、声学细节、延迟或语言质量失配时，保留原完整码本、已匹配decoder与显式分块，不从更短token流批准语音无损或净加速。

独立marker：

`<!-- source-family:SF-2025-ARXIV-2510-15227 -->`

完整本人末注：

- `SF-2025-ARXIV-2510-15227` — Daily2025-10-21补Oct20；Lorentz R11首必要exact-v1§3/4.1–4.2/4.3.2/4.3.4，writer核TMUL完整T4及少量识别反侧，2+1+2=5，token资产/decoder兼容差额深入。保500K小时等阶段预算不同、180ms非端到端、single-speaker非通用声纹，未核实现或复现。

## B7 15804 / WORLDVIEW-REPRESENTATION Ch5

文件：`books/part-01-worldview/05-what-neural-networks-learn.md`。在原有效性/plausibility完整段及独立`SF-2025-ARXIV-2510-06700`marker后、`## 什么叫“好的表示”`前。现有probe/干预资格解释不覆盖“共现真值潜变量怎样借norm变成可线性读出信号”的构造及失败条件。

完整新增正文：

可读方向的形成还可能来自训练语料的共现结构，而不是模型另有独立真值监督：若两条事实的真假由共同潜变量控制，识别第一条的状态就有助于预测第二条。一个[受限单层构造](https://arxiv.org/html/2510.15804v1#S4)在正交embedding、均匀attention和特定权重结构下，使一致事实的分量相消、范数更小，再经normalization改变后续预测的锐度，并产生可线性分离的真假信号。它解释一种可能机制，不证明真实模型有统一truth轴或探针知道外部事实；全真语料且允许学习attention时，模型可改为忽略前文，合成实验便不再出现相同信号。共现假设、架构、训练动态、probe人口与下游消费必须分开核验，有限真实LM steering改变概率也不是事实纠错保证。构造数据、训练、选层/probe和干预回归都付费；语料机制或行为支持不足时，保留原模型、外部事实证据与更窄受控实验，不让可读性取得真实性的所有权。

独立marker：

`<!-- source-family:SF-2025-ARXIV-2510-15804 -->`

完整本人末注：

- `SF-2025-ARXIV-2510-15804` — Daily2025-10-21补Oct20；writer首必要exact-v1§3/4/5.1–3/6，2+1+2=5，具体共现/norm构造差额深入。只采用构造/条件与ρ1可学习QK失败，不认证全部proof或真实LLM统一truth方向；保5seed合成/平衡probe、CounterFact128/选层steering、style混杂和全费。未核实现或复现；独立key/PRE以本日sole reader实际记录为准。

## B8 15455 / PLATFORM-SECURITY Ch72

文件：`books/part-06-ai-infrastructure/72-security.md`。在现有Tool Response Data-minimization完整双段及`SF-2026-ARXIV-2606-00152`marker后、`### App-local Context Namespace 阻止普通 Writer 获得跨 App Authority`前。旧段按schema字段确定性裁剪；差额是本地全UI按布局分块、cloud按需补取的暴露/费用合同，不提升模型的权限。

完整新增正文：

当上游是缺少稳定schema的UI时，最小披露也可先由本地可见的布局分块提出：本地模型保留全屏，只向cloud发送当前子任务相关block，不足时再补其他块。[CORE的受限协作分支](https://arxiv.org/html/2510.15455v1#S3)减少的是跨边界上传的候选内容，不使本地模型、子任务摘要或history天然私密；语义选择可能漏掉必要上下文，也可能最终传出全屏。暴露比较须固定same-action/same-screen人口，少元素与较少真实敏感信息不是同一结论，自动敏感标签不替权限审核。局部对照成功率仍低于全cloud，减少cloud推理时间还伴端到端时延上升、cloud token未必减少。全本地推理、分块/交互、失败补取与独立隐私/任务回归都计费；布局、选择或总预算不合时，保确定性字段过滤、经授权的局部视图与人工澄清，不从少上传签发隐私、安全执行或净加速。

独立marker：

`<!-- source-family:SF-2025-ARXIV-2510-15455 -->`

完整本人末注：

- `SF-2025-ARXIV-2510-15455` — Daily2025-10-21补Oct20；writer首必要exact-v1§3/4.1/4.2T1–2成本尾/6，2+2+2=6，本地UI→cloud增量披露差额深入。保same-action/screen筛选、自动敏感标签、media/payment不减暴露、成功率反侧与约1.5–1.66×端到端时延，局部7–9B/Ollama4090D与手机执行分责。不授DP/完整权限或SLO；partial178260/395489必要主体已到，未核实现/复现。独立key/PRE以sole reader实际记录为准。
