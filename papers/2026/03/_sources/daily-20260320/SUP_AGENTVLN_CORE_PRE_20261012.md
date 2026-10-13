# AgentVLN17670：几何候选与主动深度请求 / 必要准备

resume_mar17，2026-10-12，只本03-20补03-19。原2+2+2=6、准入/day独核§30复用，不重查提交时刻或扩大池。本准备不自授PASS/Books/safe/DAY。

## 1. exact-v1必要源与停止

[HTML](https://arxiv.org/html/2603.17670v1)完整AB、§3.1–3.5/Eq1–7 L89–143与关键§4/T1–3/直接上下文反侧/§5 L144–245实际读；current abs同题九作者、单v1/19pages说明轻量实际读，无采用相关纠错信号。不展开References、代码、supplement硬件/数据recipe或图像像素。支持拟采接口及直接反側已够，停止而非假称全部19页/部署验收。

RGB-D、camera intrinsics和world pose共同支持backprojection，增量occupancy map由planning skill产生3D路径点；Eq4再将这些点投影为pixel-aligned候选供VLM语义选择，planning skill还原3D waypoint执行。无相关可行路径投影时回到Forward/Left/Right细粒度proposal再重看；这不是模型保证几何可行，pose/depth失配与微动作碰撞仍须独立controller检查。

目标显著可见后切local localization；遇空间歧义，模型先发自然语言几何问题，perception skill返回几何/语义信息作为新增文字context，再输出目标pixel，用当前depth和pose回投世界坐标。§3.5/§4.1训练数据按target visibility路由，含trajectory noise、无visual waypoint细动作fallback及多轮QA示教。几何工具请求不是仅延长内部CoT，也不是从monocular RGB发明metric尺度；示教visibility标签不自动是线上可靠检测。POSMDP把perception写成τ=0只表示不推进规划动作时间，不证明查询零wallclock或零费。

## 2. 评价与直接反側/未采范围

Qwen2.5-VL-3B，冻结vision encoder/projector；batch128/lr2e−5、8frames/640×480/FOV110，32A100训练。Habitat AgentVLN-Instruct加LLaVA-Video178K，R2R-CE/RxR-CE Val-Unseen局部评价；对照传感器/视觉底座/训练不同，参数规模小不能授同预算/同观察公平或unique因果。T1自身OS73.5低于EfficientVLN73.7；T2自身NE3.92高于3.88，不照录全指标SOTA。T3第一增量同时mapping与VLM-as-Brain调度，后叠CDFG/QA，不能全收益单归depthquery。8frames后更多context退，只有相关正文/图caption读到，未采精确最优或attention-hallucination唯一因果。

Go2+D455/RTAB-Map SLAM实际列出，pixel→world waypoint仍交path/controller。正文仅qualitative室内/外示例与Jetson local声称，必要范围未披露实机任务trial/失败分母、完整硬件精度、pipeline时延/控制deadline、碰撞/介入统计、全部CI/训练数据规模/总费；不授实时高频/普遍换LiDAR免适配或碰撞安全。depth/pose/地图更新、prompt投影、查询/QA、模型、路径/控制、训练与回归都计费。必要部署量化不采用，不因无supplement而把可证接口标blocked。

## 3. actualsole差额与最小literal PRE

sole `MULTIMODAL-EMBODIED-VLA`，[Ch26](../../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)。实际完整49–91 depth/frame→action、activeview/virtualrender、Tiaohop grid-raycast与接触proposal；151–191高低层/传统模块化/参数planner/RANGER交接已读，Ch23/25/78入口实际读。现83已承载几何映射供VLM2D表达与controller责任，不能重写成熟perspective几何作新贡献；具体差额只**目标可见性路由的导航/定位与主动几何问题→返回context→目标pixel消费**。拟原83导航grid-raycast完整段后/接触proposal前一段+static，非准备者可裁更小或specific NC，不由owner关联自动整合。

二维候选与深度映射已经存在时，新的选择还可能是何时请求哪份几何信息：导航阶段先把地图中的路径点投影成视觉候选，目标可见后转向局部定位；空间关系含糊时，模型先调用感知 skill 请求距离等信息，把返回结果加入 context 后再提出目标像素，由当前 depth/pose 回投 metric waypoint，交低层规划与控制。训练按目标可见性路由并示教问答，改变的是信息请求和行动条件，不是额外内部 CoT 创造米制尺度。[有限 RGB-D 导航分支](https://arxiv.org/html/2603.17670v1)仍依赖地图、标定、定位和工具返回；候选不可见时的细动作也只是 proposal，不签发碰撞安全。几何缺失、query误答、定位漂移或上下文过期时，应重观测、拒绝不可用目标或停机接管。多组件消融共同变化，部分指标及更长历史反退；感知/地图、投影、查询、模型与controller全部计费，较小模型和perception不推进规划时间都不等于零延迟或高频deadline已验。原几何候选接口、模块化导航及已验证controller仍是回退。<!-- source-family:SF-2026-ARXIV-2603-17670 -->

静态源注：

- `SF-2026-ARXIV-2603-17670` — [AgentVLN exact-v1](https://arxiv.org/html/2603.17670v1)必要§3/Eq1–7、§4/T1–3与上下文/部署范围及§5。仅target visibility路由、主动几何query返回context再消费为pixel/metric waypoint；保RGB-D/pose/map支持、共同消融/指标反退、工具与控制全费，不采新透视几何、线上visibility真值、完整recipe、碰撞安全或免费实时。未核supplement全部硬件、代码/像素或复现。

## 4. 待非准备者裁

交resume_review17_18一次有限Source/actualowner/原单literal与static。未授Books锁不写；写后一次非writer完整邻接及本人源注POST，普通未处理不标受阻，单篇通过不授整日DAY。

## 5. 授权后的 writer 实际回读

reader独核§46有限Source/actualsole/PRE PASS后，root实际完整邻接读回授sole Ch26本family窄锁。作者仅原single literal插当前85，静态本人注2294；写前49–97/末注、写后75–99和本人/GeCO/SAE/OmniVTA邻注完整实际回读，几何候选→visibility/主动信息请求→接触proposal衔接成立。原literal/static逐字写入，限定diffcheck0；未改其他正文或静态注，未授nonwriter POST/safe/DAY。交resume_review17_18一次完整局部与本人/邻注actualPOST。
