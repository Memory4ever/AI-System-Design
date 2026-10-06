# AdaZoom17441：目标解释与预测尺寸触发二次定位

resume_review17_18，2026-10-11，仅本03-20补03/19。root明确sole准备，resume_mar17不重复；原批6及独核准入/date、正式2+1+2=5保持。恢复实际重读AGENTS、适用研究/Report合同、每日Sources、Prompt、ROADMAP、Books三约束、本日README/STOP与LS路由；不写Report/LS、不新query、不自授Source/PRE、safe或DAY。

## 1. 实际必要原证与停止

实际读[exact-v1](https://arxiv.org/html/2603.17441v1)§2/Figure1文字与§2.1–2.2.3/Eq1–4 L75–131、T1必要完整模型/切片比较132–161、§3.1–3.2/T2与成本说明162–190、§4直接外推边界191–197。当前[official abs](https://arxiv.org/abs/2603.17441)完整AB与history实际读，只有v1，无具名撤回/纠错；Submitted不替已核03/19公开夹证。未读references、全部图片、PDF、代码或其他版本；图只正文/图题，不冒像素/精确prompt实现。

必要采用对象是两阶段GUI定位接口，不是通用视觉token压缩或完整GRPO配方。改写器消费原截图+指令，将高层意图转换成控件描述并补视觉/位置线索；grounder再消费改写+截图，同时输出click与bbox。点格式/点在GT框内与bbox格式/IoU提供训练接口，却不证明改写语义忠实、框尺寸校准或点击 effect 正确。

Eq4条件为 `(w<=α && h<=β)||(h<=α && w<=β)`，α<β：一边不大于小阈值、另一边不大于较大阈值才触发，不是任意一边小或单纯面积/置信度。触发后以预测click为中心按预定义比例取局部、resize回输入尺寸，再由同grounder第二次定位；不是现场新截图、bbox必定真目标或完整场景状态刷新。原文不提供采用所需数值阈值/比例、完整跨坐标回映射与失配guard，不采用精确recipe。原/改写指令和坐标变换的联合检查是本packet系统推导，不冒本文已实现。

## 2. 关键对照、反侧与未披露

T1是在ScreenSpot-Pro静态GUI定位：4B base平均61.6、加条件zoom70.6、再加Qwen3.5-397B-A17B改写76.8，末项不是独立4B同预算模型。直接反侧OS text 83.2→80.4，其他切片与更大/不同GUI模型也非全胜；本表不提供统一训练/调用预算或模块唯一因果。§3.2所谓refinement-only69.7与原397B65.6的比较未明完整推理路径/全部预算，不照其cost-efficient主张。参数规模不能替墙钟/全部费用，也不因large-model改写存在把本准入改EX。

T2 ScreenSpot-v2无zoom .943、无条件 .916、条件 .945：无条件缩放反退支持保低分辨率一次定位分支；条件增量.002没有重复/CI/样本分层及触发人口，不授普遍显著改善或自动选择最优。§4明确多步GUI仍属future work，未实测真实点击完成、开放app状态、权限或生产安全。模型/框可能共同误定位，错误改写可把局部裁剪带离真正目标；预测尺寸不是独立置信度。

披露base Qwen3-VL-4B-Instruct、改写Qwen3.5-397B-A17B、ms-swift GRPO；但必要段未披露dataset规模/来源分割/标注验收、训练/推理hardware与precision、resolution/具体threshold/ratio、batch/concurrency、触发比例、延迟/tail/SLO、seeds/CI以及改写、重编码、第二次grounding、训练/标注的全部费用（Not Disclosed）。两种截图benchmark精度不等完整Agent utility、无损坐标转换或fresh deadline。本文支持有限接口及无条件zoom反退，不支持免费/高效保证、所有任务普胜或执行授权。

一次强命题请求仅为独立原指令→改写→真实控件语义样本、预测框/触发人口与坐标回映射、固定split/配置及全部调用费用/真实动作effect trace；缺这些不阻塞下面受限接口准备，不能用未披露事实签完整配方/性能/安全。

## 3. actual sole owner 与具体差额

实际读[Ch78](../../../../../books/part-07-agent/78-tool-calling.md)1–24、完整234–274与604–638，Ch77/79入口；[Ch23](../../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)1–18及680–700只作表示交接。sole拟 `AGENT-TOOL-CALLING`：Ch78原618 program-state/视觉fallback完整限制之后、620既有marker之前两段；不改marker身份或复制Ch23 crop算法。

Ch78现有DOM/a11y/HTML表示、revision/effect门及crop调用归因强，但未具体承载“原指令+图→派生控件描述→click+bbox→预测尺寸条件决定是否第二次定位”的GUI action-target分工。Ch23已有bounded acquisition/marker/静态attention crop与错误自确认；这里不重抄主动看细节通则，只补派生目标解释与action定位、预测尺寸不是语义/置信度、坐标/状态与执行权限的具体交接。两模型/局部结果可保有限采用，不因缺全预算自动中心EX或假主题NC；由非preparer判断差额和采用范围。

## 4. 两段 literal PRE 与静态注（待非准备者裁）

视觉fallback中的目标解释与坐标定位还可分责：先让模型按原指令和截图提出更明确的控件描述，再由grounder同时预测click与目标框；只有预测宽高满足“小边及另一边上限”的联合条件时，才围绕预测click裁取局部、恢复到输入尺寸并做第二次定位，否则保留第一轮。框尺寸是额外观察需求的代理，不是置信度或真实目标证明；派生描述也可能误解意图。原指令、改写、原截图、局部坐标变换与最后action-target应共同可回指，这是执行接口验收要求，不冒称该定位研究已实现完整guard。<!-- source-family:SF-2026-ARXIV-2603-17441 -->

[预测尺寸触发定位的有限对照](https://arxiv.org/html/2603.17441v1)中，无条件zoom在低分辨率任务反退，条件zoom也非所有切片都改善；加入更大改写模型后的精度不能当作小grounder同预算收益。改写、局部处理、重新编码与第二次推理共同付费，静态点/框命中不证明真实点击effect、当前页面仍有效或生产尾延迟。描述失配、坐标/页面漂移或额外调用不合成本时，保留原截图与一次定位、核可用程序状态或请求澄清；已有revision、权限与effect-time验证仍负责动作提交，而不由单个小框自签执行。<!-- source-family:SF-2026-ARXIV-2603-17441 -->

静态注：

- `SF-2026-ARXIV-2603-17441` — [AdaZoom-GUI exact-v1](https://arxiv.org/html/2603.17441v1)必要§2/Eq1–4、§3/T1–2与§4。仅原指令→派生目标描述→click+bbox/预测尺寸条件二次定位的分责；保无条件zoom及切片反退、更大改写器/预算、静态截图与真实effect、坐标/阈值未闭合与全费边界，不采精确recipe、免费/全任务优胜或部署安全；未核代码/复现。

支持与直接反侧足以准备该有限接口即停，交resume_mar17非preparer必要Source/actualsole与literal裁决。未获明确窄锁不写Books；本准备者不自PASS或计整合/DAY。

## 5. 非准备者必要 Source/actualowner/PRE

resume_mar17 恢复仅本20适用合同后，实际exact-v1必要§2–4/Eq1–4/T1–2（75–197），actualCh78完整598–643与234–274、Ch23 680–700表示交接，原两literalPRE和静态注逐字回对，有限 Source/sole差额/PRE PASS，保5/date。两stage分别负责派生目标描述与click/bbox，Eq4是小边和另一边上限联合条件，不是confidence或任意一边小；第二轮仍是原图裁剪非新现场观察。T1 OStext83.2→80.4、T2无条件退和.002局部差额、397B改写器/4Bgrounder预算、完整配置/真实effect与全费边界准确。已有program-state/visualfallback及activecrop不承载具体目标解释→坐标/尺寸条件的分责，原618后/620marker前两段位置成立；不改变原marker、权限或effect-time owner。必要支持/反侧足即停，不读图像prompt、references、代码或无关附件；未授Books/actualPOST/safe/DAY。由root另授唯一窄锁，writer落实后本人一次nonwriter实际完整局部/静态注回读。

## 6. sole writer 实际落实（待非 writer POST）

root收到§5 author非preparer有限PASS后明确授resume_review17_18唯一Ch78本family窄写锁。writer实际回读604–633 program-state、视觉fallback、原marker与集合工具两侧及当前末注后，原两literal PRE仅写新620/622、静态977，不改既有marker或其他family。实际完整600–645与968–977本人/PASTE/INTENT等邻注逐字回批准原稿，scoped本family diff仅两正文+静态注、diff-check0。模型目标描述/定位分工与真实程序状态、revision、权限和effect-time责任顺接，反退/全费/原一次定位退路近文。交author一次实际nonwriter POST，不自授POST、safe或DAY，不循环静态注身份。

## 7. 非 writer 实际 POST

resume_mar17仅恢复本20适用合同及Books约束后，实际独立完整顺读Ch78 600–645（两新正文620/622、原marker624、program-state/effect责任和集合工具交接）与968–977静态本人注及PASTE/INTENT邻注，逐字回对§4两literal PRE和有效§5必要Source。目标描述→click/bbox→尺寸联合条件→原图第二定位的有限分责准确；静态命中不授真实effect、页revision/权限、无损或生产SLO，397B改写器与全调用费/反退及一次定位退路近文。scoped实际diff仅本family两正文及静态注，限定git diff --check无输出。一次nonwriter actual POST有限PASS；未改Books身份注、不重读未采用附件、不授全日DAY，由root接纳与释放Ch78窄锁。
