# 第二十七包：小先大后、跨域warmup与能力锁

Books/ROADMAP有效，actual Ch54 router-cache完整链、CPU/GPU分工全文、MoEpic完整段/marker及按层物化两完整段均读；Ch38同步1F1B/InfiniPipe全文及split-backward下段、跨地域BACE完整段及后KV-shared段均读；Ch72资产主体、data/artifact分权两完整段与后refusal-cliff全文均读。Ch53/55、37/39、71/73交接已读。只消费R11/R18/R17首必要，不第二Methods/实现/复现。

## 12357 MoBiLE / 2+2+2=6 / INFER-GPU-MEMORY Ch54

actual缓存/预取保原router函数，尚未承担先用裁expert小路径出token、低confidence再big fallback的近似模型路径。插完整MoEpic独立marker后、按层物化首段前。

正文：

还可先改变通常执行的模型路径，而不只搬运原router选中的权重：由较少expert的little模型先生成，低confidence时再调用big路径，并借little路由提出后续预取。[受限小先大后分支](https://arxiv.org/html/2510.12357v1#S3)允许大多数步骤少加载，却不是用完整模型逐token验证的speculative拒绝采样，不能继承相同输出分布保证。Confidence是可错控制信号，小路径选错仍可能直接提交；阈值、裁剪/模型身份、缓存/prefetch和fallback时序须共同保存并验完整质量与延迟。受测消费卡/PCIe和有限长度下仍有质量下降，架构expert数口径不齐也不能补成通用配方。全部大小模型准备、little执行、失败重做、权重/KV驻留与传输都计费；质量、状态兼容或净时延不合时保原big按需加载、已验cache和全驻留，不由较少fallback或更高tokens/s批准无损、安全与服务SLO。

独立marker：`<!-- source-family:SF-2025-ARXIV-2510-12357 -->`

本人末注：

- `SF-2025-ARXIV-2510-12357` — Herschel，Daily2025-10-16补Oct15；消费Cicero R11 exact-v1 III–V首次必要，2+2+2=6，仅little-first/confidence big fallback与little-router预取差额。保非SD精确分布、RTX4080/16GB/i5-12400/64GB/PCIe4、256/512cap/gamma.7、GSM反退与Qwen60/64对4/2口径冲突、全部双路径/重做/迁移费，不授普遍倍率/quality或KV完全一致。未第二Methods/代码/复现；PRE/SAVE/selfread/solePOST只canonical实际层。

## 12064 GeoPipe / 2+2+2=6 / TRAIN-PIPELINE-PARALLEL Ch38

actual BACE拥有跨域路径/优先级，1F1B拥有激活lifetime；未承担增加warmup深度换延迟隐藏/非阻塞通信与HBM边界的同一依赖选择。插完整BACE inline段后、跨层KV共享标题前。

正文：

跨域延迟还可用额外在途micro-batch隐藏，而不只改网络路径：在同步1F1B中增加warmup forward，并调整依赖和非阻塞通信，使后续计算覆盖较长传输。[受限跨机房流水分支](https://arxiv.org/pdf/2510.12064v1)用更多activation驻留换重叠，增加量受HBM、micro-batch和原step提交边界共同约束，不能让通信未完成的状态提前消费。有限三机房910B/OTN/PFC条件下未见重传，不授任意WAN同可靠或光网必需；bubble下降也不等相同比例iteration加速。搜索sequence length即使固定total tokens仍会改变训练样本/上下文语义，模型尺寸口径与未披精度不能由系统倍率补齐。全部warmup/激活、profile/配置搜索、通信和独立训练质量均计费；容量、可靠传输或净step收益不合时保普通1F1B、较少在途与单区域执行，不由更多重叠批准同训练语义、零额外内存或跨域SLO。

独立marker：`<!-- source-family:SF-2025-ARXIV-2510-12064 -->`

本人末注：

- `SF-2025-ARXIV-2510-12064` — Herschel，Daily2025-10-16补Oct15；消费Cicero R18 official exact-v1 PDF II-B/III/IV首次必要，2+2+2=6，仅extra warmup/改1F1B/非阻塞通信与activation容量差额。保64×910B/TP8PP8/三DC/OTN-PFC、有限无重传非任意WAN、固定tokens改seq非同语义、72B/70B冲突/precision未披及全费，不授bubble等比例step或通用可靠。未第二Methods/代码/复现；PRE/SAVE/selfread/solePOST只canonical实际层。

## 12117 LOCKET / 2+2+2=6 / PLATFORM-SECURITY Ch72

actual data/artifact与主体授权已分权，尚未承担feature拒绝adapter合并/谱归一后按认证条件切换的能力锁差额。插完整benign fine-tuning第二段后、refusal-cliff首段前；训练算法细节不跨Ch30复写。

正文：

授权还可控制本次装载哪份行为artifact，而不要求把feature名称当密码：为各feature训练拒绝adapter，合并后以spectral norm重新缩放，再按可信认证结果选择相应锁定路径。[受限能力锁分支](https://arxiv.org/html/2510.12117v1#S3)改变的是拒绝行为，不在模型内部建立客户身份认证；组合后的谱尺度可控也不证明feature独立、全部合法utility保持或对自适应攻击安全。模型/feature字典、各adapter/合并缩放、认证结果和运行时装载须共同绑定，ASR的拒绝keyword读数与SQL文本ROUGE分别不是有害行为上界或执行正确。全部锁训练、merge/SVD、每请求适配与独立组合/旧任务攻防都计费；干扰、授权或回归不足时保可信原artifact、外部最小权限与较窄能力/人工路径，不能由无密码、低ASR或可组合名称签发完整认证和永久安全。

独立marker：`<!-- source-family:SF-2025-ARXIV-2510-12117 -->`

本人末注：

- `SF-2025-ARXIV-2510-12117` — Herschel，Daily2025-10-16补Oct15；消费Cicero R17 exact-v1 §3–4/Alg1/5/6.3–6.4首次必要，2+2+2=6，仅feature refusal adapter合并/谱缩放与外部认证分责差额。保feature干扰/旧utility反侧、keywordASR与SQL-ROUGE不认证动作、有限组合/攻击、LAT/merge/SVD及每请求全费，不授无认证/完整组合安全。未第二Methods/代码/复现；PRE/SAVE/selfread/solePOST只canonical实际层。

请sole reader核三完整正文/独立marker/本人注及完整直接邻接；未SAVE/不预POST。
