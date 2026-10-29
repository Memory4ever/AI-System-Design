# OmniVLN17351：姿态绑定的分层地图摘要与符号导航消费者 / 必要准备

resume_review17_18，2026-10-12，只03-20补03-19；author明确sole必要准备，原2+2+2=6/date准入§30复用。准备者不自授Source/PRE/I/DAY，未获root锁不写Books/Report/LS。

## 1. 实际原证及停止

[exact-v1](https://arxiv.org/html/2603.17351v1)完整AB L52–57；必要III-A–C/Eq1–10 L94–158、IV-A/TI L160–189、IV-B/TII/设置/直接导航与latency L190–241、IV-C/D及V动态环境边界 L242–260实读。首次较长输出在related-work邻接截断，不据此授相关工作已读；核心和评价缺段另精确补齐，未读References/图像像素/代码或独立复现，无需更多附件。current abs8–28同题八作者/单v1无具体修订说明；精确ID/title/URL匹配的DataCite created03/19T02:30:07Z、registered02:30:08Z及已独校自然日归属复用，不把Submitted03/18作为公开日。

## 2. 支持命题与不采用的桥

扫描几何与全景分割融合后形成mesh/object/place/room/building五层DSG；room按clearance filtration的连通分量稳定plateau提议，geometry剪边与短距VLM检查是图修订，不能把VLM关系评分当物理真值。保存JSON/PLY可离线消费，不认证旧地图仍新鲜。必要范围只采用下游摘要接口，不授Eq1时序运动补偿/PH tie或阈值/剪边判据的完整可执行recipe。

III-C按当前pose把node坐标转到ego，再按轴符号/高度阈值提议octant；附近保实例细节，同room较远或跨room压缩为组/room描述。推理先筛room，再方向、功能组和对象，Actor输出room转移/转向/接近/stop符号；Critic用当前图、指令和可达性检查，不一致则replan，deterministic local policy映射到平台waypoint/setpoint，执行后更新pose/DSG。新增差额是**改变哪一级map detail进入当前动作条件**，而非一般地图、八方位、分治或安全controller的命名。共同图使Actor/Critic共享误边；旧图无实时传感器仍能生成建议，不等环境已验。

## 3. 关键评价与直接反侧

TI实室三room/44objects，层级设置给DSG+object metadata，flat只object list，同时改变信息与prompt；VI/VD描述评分不是独立运动或碰撞测试，评分者/重复/CI必要范围未披露。TII合成四room、四类别，caption20–40词模拟VLM，三tier及5–50objects；Qwen2.5-VL-Instruct累计token口径未明确完整history/输出/次数，非任意建筑与动态实境。TII最小密度.25%少量收益；global50约69.98%与AB61.7%不是可直接统一同分母headline。§IV-B3明确D4–6两方法均100%、D9自身仍80%而非无错；未读Fig7像素/未造全九场景SR数字，不采AB11.68%为某一个已匹配效应。

§IV-B4作者Python几何<10ms和12.4→3.8s平均decision，不认证完整sensor/map/filter/network/control deadline或严格logarithmic增长。实际perception/DSG onboard、LLM offboard WiFi；aerial PX4/MINCO、quadruped Unitree SDK/FAR各有不同lowlevel。实机仅定性nearest-chair示例，不补全试验分母/碰撞率；旋转85vs固定61nodes只是coverage读数，非真值recall/地图拓扑无误或无需标定。动态行人tracking/prediction仍future。hardware/precision、输入输出长度、batch/concurrency/SLO、全场景人口、seed/CI、完整map/LLM/control费用在必要范围Not Disclosed，其他已披露synthetic规模不抹掉。零shot/无task训练不消除基础模型训练、扫描、建图、图修订、摘要、工具、模型与controller费用。

## 4. actual sole owner与最小两literal提案

sole `MULTIMODAL-EMBODIED-VLA`，[Ch26](../../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)。actual完整65–104标定/主动观察/Tiaohop→AgentVLN→接触候选，以及175–191模块化controller与旧bank定位已读；Ch25/27入口确认World Model dynamics/data不接管导航map consumer。AgentVLN现85已覆盖信息请求/像素metric转换，RANGER旧bank已覆盖尺度/重新定位；尚未具体承载近实例/远room摘要如何随pose改变高层候选与符号执行条件，不复制这些成熟安全原则。拟在AgentVLN完整段后/二维接触proposal前两literal，现85后；root如移行以完整family段作锚。

导航地图中的对象和坐标完整列给模型，最便于直接回读，却会让远处与近处证据争用当前决策的上下文。一个[受限层级接口](https://arxiv.org/html/2603.17351v1)从持久的房间—功能组—对象图按当前 pose 生成自我中心方位，近处保实例细节，较远处只给组与房间摘要，再按房间、方向和对象逐步收窄候选；高层提出转房间、转向、接近或停止等符号，由独立局部规划/控制转换为本体命令。改变的是地图哪一层细节进入动作条件，非摘要或方位词创造了新观测。图、pose、分组与摘要 revision 需共同绑定；Critic 在同一图上复核只检查内部一致，不能独立认证错误边、陈旧对象或真实可通行。<!-- source-family:SF-2026-ARXIV-2603-17351 -->

这条分支把部分上下文预算转到扫描、建图、关系修订与几何摘要，保留远端模型、工具、解析和低层执行的全部费用；合成场景的 token 减少不证明严格对数增长或完整闭环加速，平均秒级决策更不签高频安全 deadline。实室描述对照同时增加结构信息，实机展示与地图对象数量也不等碰撞率或动态场景可靠性。摘要删去关键关系、pose 漂移、旧图与当前观察冲突或通信迟到时，应恢复相关对象/几何细节、重新观测与定位，必要时停止或回退原完整地图、短窗导航和已验 controller；不能由少 token、共享地图或零样本调用批准真实行动。<!-- source-family:SF-2026-ARXIV-2603-17351 -->

静态源注：

- `SF-2026-ARXIV-2603-17351` — [OmniVLN exact-v1](https://arxiv.org/html/2603.17351v1)必要III/Eq1–10、IV/TablesI–II及V直接边界。仅pose绑定的分层DSG摘要→符号导航/局部controller交接；保旧图/共同Critic资格、信息与prompt混杂、synthetic/实机定性、平均latency与完整deadline和全费用分账，不采精确建图recipe、严格log增长、物理真值/任意平台或动态安全。未核代码/图像像素或复现。

## 5. 待非准备者裁

交resume_mar17非准备者一次必要Source/actualsole/两literal及static；可具体收窄/NC/中心隔离，保原6不因费用、局部或已有主题改EX。不先safe/I，root授权窄写后另一nonwriter actualPOST；本日仍无DAY。

## 6. resume_mar17 非准备者必要裁

2026-10-12：实际独读exact-v1 III L94–158、IV L160–240及另恢复241–260（完整直接部署/扫描/动态限制），支持与直接反侧足即停止，未核代码/所有图像或复现。原两literal/static有限PASS：III-C 148–157确为当前pose上的近实例/远组与room摘要→房间/方位/对象候选→symbolic primitive→deterministic本体消费者，非VLM从无图创建新观察；旧地图和同图Critic不独立认证真实可通行。TI 175–176同时变化DSG与metadata/prompt；TII 223–225不同密度/三tier与累积token的局部条件，以及234–235两者D4–6均满分/自身D9残错实际核，未采宣传增益或严格log增长。244–260远端WiFi/不同controller、85/61节点数与未来动态条件均与近文边界一致。

实际顺读Ch26完整65–108（首次批量返回部分截断，65–77另恢复）、173–193及Ch25/27入口。现AgentVLN85拥有信息请求/像素几何交接，不拥有随pose把近/远地图细节分配给高层决策的具体消费者；RANGER旧bank边界不替代此差额。sole拟85完整后/接触proposal前两段成立，原6与date复用；不采精确建图recipe、独立安全/平台普适或零成本。root协调新窄锁后写，一次非writer实际正文/完整邻接/本人静态注POST再计I；本裁不授DAY。

## 7. 作者窄写实际回读

root新sole Ch26授权后仅原两literal写87/89/static2300，writer完整77–100及末5实际回读；AgentVLN完整后/接触proposal前衔接准确，原旧family未改，限定check0。pose/图摘要、共同Critic资格与平均秒级非deadline近文；未自计POST/I，交reader一次非writer实际完整局部/本人注再由root接纳，不改Book过程身份。
