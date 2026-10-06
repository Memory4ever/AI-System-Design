# WebPII17357：视觉字段与暴露时序的有限证据

resume_mar17，仅03-20补03/19。原批5准入/date与2+1+2=5复用；适用合同与Books上下文已在本次独立恢复实际重读。此packet只准备必要Source/sole差额/PRE，不自授PASS或写权。

## 1. 精确源与实际停止

[exact-v1](https://arxiv.org/html/2603.17357v1)实际§2.2–2.4 L112–139、§3–4/T1 L144–188，以及直接标注/评价反侧B3 L314–325、C1/C3 T4/T6、D1主要对照/失败及D2–4 T12–14 L369–470和D7真实图定性限制 L493–501；不是全附录/代码或原图像素复核。current abs明确只有v1/未见纠错标记，只该必要轻量说明，不遍历史。

## 2. 采用命题与直接反侧

VLM复现真实电商layout成变量化组件，render时注入数据、DOM attributes/Range提取可见框，occlusion/clipping保留。empty/partial/full表单不同，partial是按字段序列在当前一字段中途截断、先前完整后续空，非任意真实typing/scroll/time-stream。标注含商品/订单等可联合识别属性而不仅字符串NER，局部sensor训练简并text/image二类，不输出细粒度“秘密真值”。

直接限制：三pass人工修39%布局，源文10网站与CrossCompany“11 other”人口口径不齐不采精确公司总数；B3明确newsletter email输入被策略性排除，标签集合不是所有可识别PII。含商品保守标注也会over-redact；空字段不等已经泄漏，交易值不等本场景已证明重识别。DOM gold支持复现图字段位置，不认证真实原站全秘密或reconstruction无错误。

评价split按布局/company/type与注入值隔离，非全页面/所有品牌heldout。D4 full+empty比full退（.758 vs .771），加入partial才改善；D2跨公司text AP.471显著低于image .855，平均mAP不能替每类漏检风险。T1注明Amazon full-only比较，D13另训练full+partial的full/avg不能合成同一数字；OCR基线按word而gold按field单位/排除图片，信息与目标单位不同，不授视觉唯一因果或全部OCR差。真实50未复现图只定性，静态图不测scroll/transitions/first-exposure时刻、redaction对Agent任务损伤或net upload race。

CPU约20ms仅i5/Ryzen5/OpenVINO detector，未给精确CPU/threads/precision/concurrency/tail；large312ms，单frame平均不认证30fps端到端或零泄漏。生成/人工修/训练/截图/检测/遮盖/剩余内容/网络/Agent语义损伤计全费；采原站截图在合成前有隐私责任，合成后字段多样不追溯消除原采集暴露。一次强命题请求：可核字段policy及漏标人口、绑定capture/keyboard/render/redact/upload trace的首次暴露测量与固定Agent任务质量/完整费用；不等这些才能采用有限评价接口。

## 3. actual唯一owner与差额

sole `PLATFORM-SECURITY`，[Ch72](../../../../../books/part-06-ai-infrastructure/72-security.md)。实际244–302完整runtime/statistic→privacy sensor/policy→anonymization/攻击人口→visual location链：260–280已有text span sensor/本地边界，291–299有残余重识别/非显式图像位置，未承载字段未完成的视觉候选/empty边界与transaction联合属性、field级指标和捕获到上传之间时序验收。故新差额不是泛privacy主题，未虚称NC。Ch71/73入口1–26/1–28与Ch78 411–430tool observation处理实际读；工具executor按可信本地policy消费，本文不授其action授权。

拟Ch72 Privacy Filter段完整结束/280之后、learned anonymization前插两段，沿同一sensor责任扩展pixel字段与时序，不复制GUI动作/数据训练owner或另建结构。

## 4. 两段 literal PRE 与静态注

把观测换成屏幕截图后，敏感性不仅来自已能OCR识别的完整字符串，还来自字段角色、尚在输入的片段与可联合识别的订单/商品属性。一条本地视觉sensor分支可用带字段标记的页面复现、数据注入和empty/partial/full状态训练候选区域检测，再由组织policy决定哪些区域要遮盖；空字段是可能暴露的位置，不等已经泄漏，保守商品标签也不是每张图都已证实重识别。页面、字段与输入状态、检测/遮盖revision及上传对象必须绑定，不能等完整值出现后才第一次检查，也不能由候选框直接授权后续动作。<!-- source-family:SF-2026-ARXIV-2603-17357 -->

[视觉字段检测的有限证据](https://arxiv.org/html/2603.17357v1)显示partial状态与完整表单不同，但只核合成静态电商图，不测真实滚动、键入到上传的race或Agent任务保持。按field标注的mAP不能直接合并OCR词级结果，text与image类均值也不能替细粒度漏检；标签policy有主动排除和过度遮盖边界，单frame CPU均时不认证端到端无暴露。截图、合成/人工校正、检测、遮盖与语义损伤均计费，采集到本地决策及上传之间应独立核首次暴露和剩余内容。页面状态、policy或区域不可信时，保留确定性字段遮盖、可信DOM/local路径、人工检查或不上传；高检测分数不替consent、访问控制或匿名化签字。<!-- source-family:SF-2026-ARXIV-2603-17357 -->

静态注：

- `SF-2026-ARXIV-2603-17357` — [WebPII exact-v1](https://arxiv.org/html/2603.17357v1)必要§2–4/T1、B3标注反侧、C1/C3、D1–4与D7真实图定性限制；只采用视觉字段/partial状态与privacy检测单位和时序验收边界。不采全PII、重识别真值、真实流零泄漏、Agent utility无损或生产fps；保标注policy/人口与全费，未核代码/复现。

准备后交reader非preparer必要Source/actualowner/PRE裁，未写/safe/DAY。

## 5. 限定实际写入

reader非preparer必要Source/actualowner/原两PRE/static有限PASS见本日独核§23，root明确Ch72唯一窄锁。作者仅原PRE实际283/285及静态本人4463，完整267–303及4457–4463本人/邻注实际自读，text sensor→visual field状态与时序→learned anonymization责任顺接；本family scoped实际diff仅两段+注、git diff --check 0。未授实际POST/safe/DAY，下一交reader一次非writer局部验收，不改Book注身份。
