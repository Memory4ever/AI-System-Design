# 11548 GUI auxiliary reasoning exact-v1 必要首包

准备者Lovelace，作者明确单让并本人接受后的唯一首必要Source；交Bernoulli一次不同角色采用，不selfsign。

## 原件与范围

[exact-v1](https://arxiv.org/html/2509.11548v1)，[raw](./REVIEW_SOURCE_11548V1_20261023.raw)、[headers](./REVIEW_SOURCE_11548V1_20261023.headers)、[request](./REVIEW_SOURCE_11548V1_20261023.request.json)。200/exit0/150271B/.888835s/SHA4eabb75dfc8ffdd4621a75b6f976329aa9fb6e89743cc6575ad29d8ae00e182d。实际完整S2–4/E1–5/T1全部四benchmark行、全部ablation文字及F1–3正文/caption已读；无附录。未图像素/精确plot读数、全prompt/代码/GUI执行或复现，不GET currentMethods/后版，145 AB/current/day有效不第三。

必要原正文现明确：**Mark-Grid Scaffold名称已在v1 S2.2/T1、方法正文亦写Marked-Grid Scaffold**，不是2026后版才有。此前103/145仅AB差额中“未见后版命名”不能升级为v1正文不存在，现以实际正文校正这一局部推断；不影响身份/公告日、原P或新后版Gemini3.1Pro/95.20%不可回填。不是重读AB/追全版本。

## 拟原5与证据边界

拟2+1+2=5，只明确坐标/离散编号的图像输入与空间输出接口、粗细两次重读的设计选择；非GUI题材/高百分点或oracleattention上界加分。原P维持，不因应用域/未全胜/缺实现撤P。

PointingGame从输入instruction末token到image tokens的attention逐层各head均值，reshape/resize至原图，取argmax，再用GTbox检查。E5对层指标union与“逐样本找最优层”是使用GT选择的诊断oracle，不是模型可自行选层的在线grounder，也非全部表示信息或真实能力的严格上界。层数越多机会越多、head平均/resize/目标框面积都会影响命中；较高pointing不独自定位坐标输出瓶颈或证明图像已被正确理解。正文说七模型比较但T1/caption明确只有四开放模型可pointing，SigLip无语言输出只此项，不给闭源attention读数或与其direct同预算比较。

CoordinateScaffold把旧row/col符号改成实际x/y坐标；AxisGrid在四边给100unit刻度并叠网格（ablation又写100pixel，坐标单位须锁定）；MarkedGrid把连续输出改成8x8cell-ID：先预测对象四极值cell形成粗框，crop后短边resize512、重加grid，再同时给原图预测框和crop，第二次四ID后由其中心算坐标。这是两阶段输入/输出协议，不是单次同图只加格子、独立新观察或实际工具点击。前框漏目标会传后crop，遮挡/离散化/resize坐标回映与同原screen身份须验；符号中心与真实控件边界不总等同，GT只是评价不进入在线selector。Ablation文字说5x5/twozoom最高，8x8/onezoom折中作默认，只保作者有限报告，不未看图填精数/净最优。

T1四benchmark/七模型的全部支持与反侧保：Gemini ScreenSpot-v2 direct**5.66**→Mark72.09，正文用5.50借了ScreenSpot栏，不能静默互换；Pointing各开放模型仅oracle诊断。Qwen SS50.24→Mark26.34、SSv2 47.56→28.38、UI26.61→15.44下降，Pro2.15→2.59局部反升，故不是其所有benchmark均退或训练grounding必不需要辅助。Coordinate Pro Gemini1.77<direct2.02、GPT.25<1.27、Claude.70<1.20也保，Axis Pro Gemma4B.06<.13；不能由多数格子的改善给所有场景保证。训练差异/规模/encoder使Gemma/Qwen gap不可直接定位唯一缺乏grounding训练cause。

四dataset是ScreenSpot1272、v2纠标同规模、Pro1581/23app/3OS、UI1477指令元素；平台/分辨率与标注资格约束不能合成独立重复。未全prompt/template、精确APIrevision/解码配置、渲染字体/线宽/原图resize/坐标归一、失败解析/重复seed/CI与完整预算，不能认证72.09可在当前服务复现、已实现坐标回映/可达交互或真实多步成功。PointingGT选层、白盒attention驻留、绘图/图像重编码、两阶段生成/裁剪/额外crop和原图、失败重试与独立控件核验全付费，不因zero-shot/noFT签零监督成本/轻量净SLO；本地或远端真实点击仍须独立工具权限/当前屏幕状态与实际结果验证。

## 当前唯一owner拟具体NC

actual当前MULTIMODAL-REPRESENTATION Ch23完整260–282 probe/可恢复-可访问-可表达、Grid2Matrix读出与完整274/276编号输入/逐框consumer两组，480–507完整preprocess/grid配置/原图回读、外部选区与2509.04243 crop训练/回映组，2216–2238完整局部probe/干预单位边界已读。现文具体区分GT/受训probe可读与模型已自行使用、显式坐标接口；274完整段明说原图/标记规则/跨区域归属/输出协议共同保存，绘图与更长提示全费，标记遮挡/失配回原图/明确坐标/专用读出或不加标记。498/500完整组区分区域读取、裁剪/resize坐标映射与最终点落框，预测框不签真实点击/多步安全。

上述已具体承载本新局部证据可采用的稳定接口：**标记的输入可见性/输出坐标协议、原screen与crop映射及诊断oracle/部署行为分验**，不是只同GUI/视觉主题。因此拟原5/标准完成/唯一Ch23具体NC Book0；T1与两阶段recipe的有限描述留报告，不为新增8x8参数另写书，更不从高oraclepointing宣布潜在能力已全部具备。Ch78只交接动作/权限，不新立第二owner。若要采用普遍潜在上界/唯一瓶颈、精确效率或自动点击时，才定点相合选层规则/非GTselector、冻结渲染/输出/预算控制与真实执行结果或具名修订；不需要全repo/所有图或第三AB/day。
