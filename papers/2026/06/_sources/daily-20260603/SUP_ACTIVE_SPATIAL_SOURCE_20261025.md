# 02459 Active Spatial：必要证据 / 六分 / Ch23最小提案

仅Jun03补Jun02。当前AGENTS/Research/Report/适用Sources/统一入口/ROADMAP与本日停点已按恢复读取；R62完整题摘/准入/联合日证有效复用，不第三。v1 Jun01 16:30:56Z提交至同日精确DOI登记的合法组合限定Jun02 BJT，非提交日直接归窗。[当前abs](https://arxiv.org/abs/2606.02459)唯一v1、Accepted ICML2026、所见无撤回/勘误；接受标记不构成另一个body公开事件。

实际读[exact-v1 HTML](https://arxiv.org/html/2606.02459v1)§3–6、式1–10/T1–5及F4/F6的文字分析；首次§4.2 reward截断已单独完整补读，不冒已读未见公式。未核图像素/全部示例、代码或实机/复现。采用表示—可执行检查分工，必要支持与反侧已足停止。

输入为给定有限视图集合V及自然语言视图变换E。所谓active exploration是模型按当前map/query选择retrieve(i)，不是在真实环境移动相机。统一top-down的2D对象位置/朝向和camera位置/方向由同一VLM逐观察更新，直到stop或Tmax，再答题；dynamic表示更新估计，不是已学真实动态transition或可信SLAM。

SAC把自然语言空间关系转成返回bool的Python表达式，在当前模型map s_t上eval。SFT的retrieval/map/SAC三类冷启动使用GT map、合成与强proprietary VLM/人工示例；RL总轨迹reward为final-correct gate乘(1+w*(retrieval+map+SAC))。retrieval信号还用正确答案Y及metadata，map分数比GT，SAC是已生成map上的成立比例。它不为每步产生独立世界真值，也不是每个token有自己的已证因果credit；最终错时总0不能证明所有reward hacking被排除，代码能跑也不证明自然语言翻译忠实、地图正确或无无意义True。没有结论依赖任意Python执行权限，实际部署仍需受限DSL/沙箱及输入验证，本次不执行SAC。

Qwen2.5-VL3B全参数SFT/RL、8×A10080GB，LR1e-5/1e-6、SFT22h/RL1天、batch128/G8；training MindCube10k、test Tiny1050 MCQ/最多4图，Rotation200/Among600/Around250。完整precision、长度/采样、重复CI/完整教师预算未统一披露；测试20min不是单请求SLO/真实机器人deadline。主80.5%为有限总体，Among81.0反低于3DThinker81.8，不能采“所有子集均改善”；同题不等所有基线训练预算一致。T2 reward逐项移除同时改变奖励范围/有效输出人口，支持组合必要性而非唯一空间状态因果。

T3 133个答对仍有map位置错误，占全部正确约15.7%；定位/答案须分验，不据最终正确批准全部中间状态或作者“robust”解释唯一成立。20格78.76差于10格80.48，细化不是单调好。F6文字说去Y损7.6/纯outcome损11/去gate损3.8，本次只采用定性监督/门控作用，不授实图精确曲线。EmbodiedBench模拟下Common/Complex降到0、平均仅6.3→6.7；加语言模型同时改变系统，不能据此证明唯一语言瓶颈/真实导航安全。造数/标注、教师、全视图编码/读取、map更新、代码生成/检查、训练/rollout与独立坐标/答案验收全付费。

正式Design Delta2 + System Reach2 + Durability2 = 6：增量是将空间表示维护与可执行关系检查接入按需视觉消费/训练反馈，改变“自然语言中间推理只能整体打分”的选择；不是动物类比、MCQ榜或任意agent组合加分。存在具体小gap，深入采用域，不全附件。

唯一 `MULTIMODAL-REPRESENTATION` / [Ch23](../../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)。实际完整读SGCoT轨迹消费、视频bbox/外观筛选、2603.23404房间对齐文本表示两段、其后多视图分组两段与situation/BEV监督两段；Ch22/24开篇交接亦读。现文已拥有估计坐标/原视频读取、map不是真值和答案/定位分验，尚未具体承载按需取视图→更新共同map→把空间声明变成map上可执行谓词及其“只证map内部相容”的边界，不能主题NC，也不因无marker硬I。GRPO目标的通用归一归Ch33，此处不重复算法。

拟位在2603.23404房间对齐文本的完整成本/反退段后、`离线多视图重建保留全体图像共同 attention`完整段前。先从一次性空间描述接出交互式按需map/关系consumer，再回另一路几何重建；原两段尚待独立PRE，未授写/SAVE/POST/I/DAY。

### 原两段PRE

空间描述不一定要在看完所有图像后一次生成，还可成为下一次读取的状态。给定有限视图及其变换描述，可让模型按问题选择下一张图，持续更新同一俯视坐标中的对象和相机位置/朝向，再把空间关系写成可在这份map上求值的布尔谓词。[一项受限空间推理分支](https://arxiv.org/html/2606.02459v1#S4)用配对map与关系代码监督冷启动，并将关系检查与视图/地图监督用于后续训练。这里新增的是表示更新与关系消费的接口；按需读取已有图片不是机器人真实移动，Python返回True也只说明谓词与当前估计map相容，不认证视觉事实或自然语言翻译正确。

因此map、关系代码和最终答案要分别验收，不能让同一模型产生的地图再为自己的推理签真值。该训练依赖真实答案/map等监督，最终答案门控不证明没有reward hacking；答对仍可伴坐标错误，更细网格也未改善质量。受限多视图问答优势没有迁成通用具身能力，模拟导航的部分语言任务反而归零。教师造数、视觉读取、map更新、代码检查和全部训练/回归均付费；视图关系、实体或几何支持不足时，保留原图回读、可信定位/受限规则与Unknown，不让可执行表示取得真实世界状态或行动权限。<!-- source-family:SF-2026-ARXIV-2606-02459 -->
