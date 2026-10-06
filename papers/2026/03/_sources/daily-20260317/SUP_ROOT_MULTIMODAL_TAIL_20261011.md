# 03-17有限余项：root必要审阅与逐字PRE

复用本日已独核的完整题摘与日期，不扩发现、不重归属。root只own本笔记与经非writer PRE通过后窄Books写入；报告作者不重复读。三项未运行代码或复现实验，未授DAY。

## 12942 ReMem-VLA：2+2+2=6，具体知识缺口深入

[exact-v1](https://arxiv.org/html/2603.12942v1)实际读§3.1–3.3/Eq5–6及§4.1–4.4/T1–2、Q2与结论。新增选择不是泛称两级记忆：固定EMA快/慢更新、冻结VLM与可学习query读出分离，训练slot保整episode/reset。有限query-count matched消融支持双粒度；冻结与GRU/MLP对照仅一任务，固定forward不能证明长程credit或永久保真。POP保视觉细节而额外计费。8A100/B64/TBPTT1，Qwen3VL2B、256²双视图/chunk30/DDIM20，sim每任务100demo/100rollout与改变后的环境，UR5实机200demo/50trial；10Hz4090而近20Hz复用旧chunk，不当fresh推理频率。精度、完整P99/SLO未披露。不是lifelong记忆或普遍冻结优越。

实际owner Ch26 §Policy内部LatentMemory 616–650有curator/缓存/时寿命/反事实记忆审计，但缺非学习传播与双EMA时钟；相邻Ch25 world state与Ch27数据链不应重推policy memory。本段插在curator成本/短任务回退后、TempoFit FIFO前，唯一MULTIMODAL-EMBODIED-VLA。

逐字PRE：

快慢记忆也不必都由学得的 curator 维护。另一条 episode 内分支将冻结视觉语言主干的读出接入两组固定 EMA：一组逐帧更新，另一组只在较稀疏的 chunk 边界更新；query 与动作/图像读出仍可训练，但传播系数不由短截断梯度学习。训练时每个 batch slot 顺序消费自己的 episode，并在换 episode 时清空状态，避免把轨迹分块的方便变成历史丢失或跨任务污染。这用较慢更新减少覆写，却增加陈旧记忆；固定 forward 不等于获得长程 credit 或保留所有信息。[受限消融](https://arxiv.org/html/2603.12942v1)支持两级互补，冻结传播的对照仅覆盖单任务，重建过去观测还增加训练支路。query、connector、状态维护和回归均计费，复用旧 action chunk 提高控制频率也不是更多 fresh 推理；短任务或记忆失配时仍回无状态/短窗 policy、清空受影响状态并重新观测，不由记忆分数批准物理安全。<!-- source-family:SF-2026-ARXIV-2603-12942 -->

拟静态末注：`SF-2026-ARXIV-2603-12942`，Daily03-17补03-16；exact-v1 §3/Eq5–6、§4/T1–2/Q2及结论，2+2+2=6。只采用双EMA时钟与独立episode slot，冻结传播不保证credit/保真；控制复用非fresh频率，成本和回退近文。未核代码/复现/SLO或物理安全。

## 13032 MOCR：2+1+2=5，具体表示接口缺口深入

[exact-v1](https://arxiv.org/html/2603.13032v1)实际读§3.1–3.5及§4.1–4.3/T2–5、§6直接限制。typed region/category/payload与canonical SVG监督：自然照片raster保留，当前页文与区域SVG separate passes，非headline一遍输出。1.2B新vision＋1.5Bdecoder/多stage与SFT-mixture改变，T4同parameter checkpoint比较仍不隔离每组件；SVG优者和普通版跨任务胜负不同，T5 DocVQA/AI2D反侧；Elo重排与交换顺序不保证judge正确，render相似非原结构事实。完整hardware/precision/长度/batch/concurrency/SLO未披露，不采普遍端到端优势。科研图形仅作为程序表示人口，不扩AI for Science路线。

实际Ch23 731–751已区分caption/sceneIR的四种验收，缺异质page typed payload与不可程序化raster共存/两pass、canonicalization非真值。插在sceneIR受限证据后、graph form router前；唯一MULTIMODAL-REPRESENTATION，训练细节留TRAIN-DATA，不重推该章。

逐字PRE：

页面表示还需处理异质内容，而不是把所有区域强制改写成同一种程序。可按 region、category 和 payload 组织文本、表格及公式，把适合紧凑描述的图形转成可 render 的 SVG，不能紧凑程序化的照片则保留 raster。[受限页面模型](https://arxiv.org/html/2603.13032v1)当前仍分开执行页文解析与区域 SVG 解码，不能把统一训练误称为一次完整输出。程序目标的 canonicalization、viewBox 归一与复杂度缩减减少序列歧义，却不证明原语义或几何完整；render 相似、文字正确与下游理解须分别验收。该模型的 SVG 专门配比改善部分重建任务，但普通版仍有任务反退，跨架构和训练预算也未完全匹配。两遍解码、长程序、渲染和数据验证都有费用；原图、坐标、schema 与 renderer 身份仍需保留，结构或净收益失配时回原图/OCR/raster与专用检测，不以合法程序取代视觉事实。<!-- source-family:SF-2026-ARXIV-2603-13032 -->

拟静态末注：`SF-2026-ARXIV-2603-13032`，Daily03-17补03-16；exact-v1 §3–4/T2–5/6，2+1+2=5。只采用typed payload、raster共存与两pass/规范化边界；render非语义真值，SFT/架构混杂、质量反侧与完整成本近文。未核代码/复现或SLO。

## 13070 RAPTA/ADMCD：2+1+2=5，中心争议暂缓，不写Books

[exact-v1](https://arxiv.org/html/2603.13070v1)实际读III-A/B/Alg1–2、IV-A/B/TII及IV-D/TIII–IV/结论。训练图像区域增广与生成后的copy sensor是不同机制，不为费用缩池。必要冲突：权重正部全零时归一无guard；摘要称lightweight fusion却未给其训练/权重取得机制，“无downstream classifier训练”不等fusion无学习。IV-A 约25 exact/200style/1000非copy与IV-B 200copy/1000non分母不一致，threshold称heldout又在in-house test选，split重叠未澄清。TIV同一pair flip/occlude得.886/.748低于copy阈值.938，保持相似不等固定阈值保检出；不能照录全扰动robust。TII RAPTA底座/重训预算与匹配augment控制未闭合，CLIP分数亦退。不采用安全/版权或普遍减记忆保证。

owner候选PLATFORM-SECURITY/Ch72；不作虚假的已有覆盖，也不将中心冲突降分EX。一次精确需求：fusion参数/训练说明、独立split和分母、阈值下按扰动的检出/误报、同底座同预算RAPTA对照及全费用。可接受正式勘误/带配置标签的原表；定点重开该两模块的采用判断。当前无可读取的必要补充证明这些中心主张，不要求无限寻找artifact；尚待非作者核原证/隔离，不授正面Evidence或Coverage。
