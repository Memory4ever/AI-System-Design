# 首三项整体 PRE 提案（未写 Books）

Writer Herschel；只以下正文/独立marker/本人末注。适用Books上下文及三个owner实际段/相邻章节已读。reader R5首必要真实消费，不重Methods；旧Rex正文/注不改。当前未发现精确位置冲突，无全章锁，不请求root第三技术批准。reader请整体核完整新增、完整两侧与注，批准后writer才真实SAVE。

## 12157 / AGENT-REFLECTION Ch80 / 2+2+2=6

位置：在“同一模型可能在 generation 与 critique 中重复同一盲点。External tests 和 environment outcomes 通常比自由文本‘再想想’更可操作。”原段后、“反馈还可以带不同的写入权限”原段前。保两侧全文不变。

正文：

反思次数还须与验证错误类型分开：把错误答案误放行，会使修复循环过早停止；把正确答案误拒绝，则可能丢掉已正确的候选并继续付费。两者不能用一个总验证准确率抵消，更频繁地反思也不保证二者同时下降。[简化Transformer的受限对照](https://arxiv.org/html/2510.12157v1)显示，强化学习可以增加反思并改善部分域内结果，却只改变两类错误的取舍，未获得同样的域外改善；其简化状态和无限预算条件不授真实LLM的收敛或正确性保证。应分别保存原候选是否正确、接受/拒绝、修改后结果与全部尝试预算；缺独立真值时这些仍是待核信号，而非自产标签。验证、重生与训练均付费，误放行、误改或净收益不稳时保留原候选、有限重试与外部验收，不由反思频次或自评通过批准提交。

独立marker：`<!-- source-family:SF-2025-ARXIV-2510-12157 -->`

本人末注：

- `SF-2025-ARXIV-2510-12157` — Herschel，Daily2025-10-16补Oct15；[exact-v1](https://arxiv.org/html/2510.12157v1) §4/Theorem1、§5.1–5.2，由Cicero R5首必要交付，2+2+2=6。仅两类verification错误/反思频次与预算分责；保正文符号倒置、简化/无限预算和ID/OOD界，不采一般LLM保证。未核代码/复现；整体PRE、真实SAVE/自读与sole actualPOST以本日canonical实际后到层为准。

## 12185 / MULTIMODAL-REPRESENTATION Ch23 / 2+1+2=5

位置：在SF-2026-ARXIV-2606-11400独立marker后、“选择语音 encoder 的层之前”原段前；上方完整邻接为“选好声学窗口之后”与“受限三事件定位对照”两段及marker，不改。

正文：

即使模型能说对事件类别，也应另验它把事件放到了哪个时间：预测减真实时间的有符号误差衡量偏早或偏晚，绝对误差衡量定位距离，正负误差抵消不表示定位准确。[受限音频聊天模型测量](https://arxiv.org/html/2510.12185v1)还表明，长度、事件位置与类型会改变偏差；已知目标事件的oracle提示和只保留有效时间输出的计分人口，不能替代未知事件发现或把无效输出视为成功。原声/时间原点、事件标签、输出解析与valid/invalid分母应共同保存，语义正确、signed偏差和绝对距离分别验收，不由attention可视化批准唯一原因。重复编码、提问与独立声学核验都计费；定位或格式不可靠时保留原音频、专用定位器及显式未知，不以总体接近零的偏差签发时间保真。

独立marker：`<!-- source-family:SF-2025-ARXIV-2510-12185 -->`

本人末注：

- `SF-2025-ARXIV-2510-12185` — Herschel，Daily2025-10-16补Oct15；[exact-v1](https://arxiv.org/html/2510.12185v1) §2–3.1、§3.2.3/§4必要，由Cicero R5首必要交付，2+1+2=5，具体测量差额深入。仅signed TBI/absolute MAE、语义/时间与valid-only分母分责；保oracle事件、模型/位置/长度人口，不采attention因果或统一倍率。未核代码/复现；整体PRE、真实SAVE/自读与sole actualPOST以本日canonical实际后到层为准。

## 12266 / TRAIN-LORA Ch30 / 2+1+2=5

位置：在SF-2026-ARXIV-2601-06356第二段末marker后、“在比较路由器之前，还应先确认专家之间究竟共享什么”原段前；两侧完整原段不改。

正文：

从已有adapter库复用能力时，还可以先按整段输入选候选adapter及其容量，再在每个token内选择成对的rank-one分量，而不训练一套新router或总是启用完整模块。[一条受限两级检索分支](https://arxiv.org/html/2510.12266v1)以序列表示的Gaussian匹配提出库内候选，随后按token响应细选分量；选库、分配rank和实际激活是不同决策，某一候选相关性界不证明token输出正确，也不允许分别打乱配对因子的列/行身份。应共同保存base/adapter库、序列encoder与统计人口、成对分量索引、缩放及两级选择规则；未闭合的Top-k取整不补成执行配方。离线统计、全投影/打分与动态batch组织均付费，原吞吐也有反退，training-free不等净加速。库支持、路由或完整质量/费用不合时，保留显式任务选择、完整adapter或静态rank，不由少激活分量批准无损适配。

独立marker：`<!-- source-family:SF-2025-ARXIV-2510-12266 -->`

本人末注：

- `SF-2025-ARXIV-2510-12266` — Herschel，Daily2025-10-16补Oct15；[exact-v1](https://arxiv.org/html/2510.12266v1) §2–3.4/§4.1–4.3/§5，由Cicero R5首必要交付，2+1+2=5，具体接口差额深入。仅序列选库/容量与token成对ROC激活分责；保Gaussian前提、Top-k取整未闭与吞吐反退/全费，不采普遍质量和净速。local HTML partial与web实际必要层分账，未核代码/复现；整体PRE、真实SAVE/自读与sole actualPOST以本日canonical实际后到层为准。
