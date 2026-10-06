# 2603.09826 — 部分可绑定对象再读位置（ready）

[VLM-Loc exact-v1](https://arxiv.org/html/2603.09826v1)。作者实际完整§3–6/Tables1–6与supplement D.1/D.2 Tables8–9文字，未核图像精数、全部dataset构造附件、repo或复现。读取同日supplement_html.py S3 S4 S5 S6 S4a stdout；current仍v1，CVPR2026状态本身不充更早公开/修订。batch3完整AB/history与owning arxiv.content/findable registeredMar11UTC02:22:51上界及official noadvance/公告下界同BJT日夹证；SubmittedMar10UTC15:48:25不单独public。

accepted首稿定点轻核：[作者主页](https://martin-liao.github.io/)Feb2026是接受news而非正文公开声明，该news实际链接arxiv2603.09826；publication同标题八作者，PDF为本地2603.09826v1.pdf但web Cachemiss，不因此追全文史或作更早证据。[正式CVPR身份线索](https://openaccess.thecvf.com/CVPR2026?day=2026-06-07)搜索返回同题八作者/June2026 proceedings，仅发现身份；未用大名单作全源覆盖/firstpublic，未见具名更早公开冲突。

2+1+2=5；唯一MULTIMODAL-REPRESENTATION，具体“partial/null绑定标签而非强制同类物体匹配”的输入/输出接口差额加深。不是因CityLoc新任务就给分，也不授实体身份/位置真值。

## 必要机制、评价与反侧

§3 maps使用KITTI360已标语义/instance/colors，stuff经DBSCAN，object仅保至少1/3points；查询由真实posecell按模板选6object，semantics/color/direction不是自然开放人类描述人口。§4.1平面假设，50×50m map→224×224 BEV；object平均RGB，前景优先；“scene graph”实际只node(index,label,pixelcentroid)，不显式边。不能写成恢复任意三维关系图或物理图真值。

§4.2 PNA训练label取同对象两观察区域centroid距离是否小于阈值（object5m/stuff15m），valid→对应node、invalid→null；推理是model自主预测，非可获得query真实pose的阈值oracle/在线Hungarian。距离筛出的是该构造有效性，未证明传感可见性或实体唯一性；共享地图/instance/坐标/阈值需共同版本化，重复类别不强制nearest。§4.3–4.4 JSON node/hint binding后同AR序列输出二维pixel position，crossentropy训练，parse不是几何约束或位置已被验证。

§5 Qwen3VL8BInstr frozen vision/language，仅所有linear LoRA r8/a16；2epochs/globalbatch4/8RTX4090/BF16/AdamW1e-4/warmup.05。Table2 partial vsfull（强迫任何同label最近node，即便超阈值）CityLocK testR5 17.81→35.91支持null接口有限效果；Table1SG+PNA32.34，BEV+SG29.79，全35.91，均是recipe效果，不独证内部空间推理或所有输入兼容。

真实反侧：T3增加color却无direction时valR5 18.74→18.28退；T4Qwen2BvalR10/R15 64.22/79.97高于8B63.66/77.77，不采用统一size单调。D1T8同CMMLocTop1retrieval下R5 40.36>37.81，但R10 51.69<51.84/R15 54.74<55.02，有限CITY收益不是每阈值/环境普胜。S5Fig4 correctassignment与error相关不是内部因果或groundtruth绑定必保证位置。CityLocC直接迁移21.37/49.12/68.26只同生成协议的跨source评价。

D2T9两RTX4090/batch1 Qwen8B .23FPS/33.65GB，2B .36FPS/8.50GB；不能当可靠实时navigation/SLO，未披露完整长度/并发/重复CI/tail/地图构建费用。semantic-instance地图、DBSCAN/投影、模板及GTlabel、LoRA训练、AR额外bindingtokens、解析与真实定位回归全付费。丢height/拥挤投影、动态对象、领域/自然查询、标注错误与未解析输出是采用边界而非本轮实测比例，不推断已实现可靠fallback。

## actual owner 与逐字PRE

作者actualCh23 986–1013完整射线/pointtokens/OpenVoxel静态group→统一mesh→partbudget邻接及Ch22/24开篇。OpenVoxel维护实例身份却没有按查询局部support允许null的binding监督/同序列位置读出；新增只接在OpenVoxel完整两段后/统一mesh之前，不覆盖其重建/粒度保留或证明场景grounding。

拟段1：

已有对象字典也不要求把语言提到的每个对象都强行绑定到当前地图。局部观察可能只覆盖描述的一部分；可将点云投成 BEV，再以 node ID、语义标签和像素中心提供实例表，训练模型先输出哪些描述可与当前 node 对应、哪些应为 null，随后再读出二维位置。这样把“是否有对应证据”显式放在坐标生成前，而不是用同类别最近对象填满全部引用；实例表、投影坐标和语言 binding 属于同一份接口身份，却仍都是待核 proposal。

拟段2：

[受限部分绑定对照](https://arxiv.org/html/2603.09826v1)以两局部区域的对象中心距离制备 valid/null 监督，推理时由模型预测，不拥有真实位置的距离 oracle。平面 BEV 和无显式边的实例表会丢高度与细节，模板查询、已有语义/实例标注也不代表自然开放描述；更好的绑定相关性不保证几何正确，原检索协议下部分距离阈值仍反退。地图构建、投影与标注、binding 监督/LoRA、额外 AR tokens 和解析、实际位置回归均计费；support 缺失、ID/坐标失配、解析失败或预算不足时，保留 null、原图/点云、专用匹配或定位工具，不让 JSON 身份和连续坐标批准导航行动。<!-- source-family:SF-2026-ARXIV-2603-09826 -->

root必要Source/date/具体owner/逐字PRE通过，作者已在Ch23 OpenVoxel完整两段后/统一mesh前写新1006/1008及本人1271。作者顺读997–1023完整局部与自身注；root非writer实际顺读998–1025完整邻接、新两段与自身末注并回必要原证，actualPOST通过，锁释放。可计本日确认新增，不授DAY。
