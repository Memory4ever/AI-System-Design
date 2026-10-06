# 2026-10-20：四项具身机制必要审阅

作者root；仅北京时间Oct19自然日。四项完整官方题摘已由root准入校准，官方RO当日列表日期沿ARXIV_SYSTEMS本日原件，不用正文Oct16提交标识替代公开日。以下是实际必要正文阅读，不是代码审计、图像检查、复现或独立验收。其余七项RO由systems_resume负责，不重复计数。

## 23378 ActiveAlign

[精确v1](https://arxiv.org/html/2610.23378v1)，实际III-A～D、IV-A～C及限制；3+2+2=7。主动观察改变的不是一张图，而是相机/机器人联合交接状态。恢复示教起点后执行AP，在示教前缀找邻近末端状态，闭环对齐再重放后缀，只保成功轨迹；部署仍使用同一AP后交给VLA。AP自身不作VLA动作训练目标，不能称端到端联合学得最优观察。

同AP、数据量/筛选/后缀/优化匹配对照支持这个交接分布适配，不证明分布相等。主LIBERO实验使用扰动起点；标准起点几乎持平，不能只报大幅收益。可行性筛选排除难状态；86/100物理适配保留，真机少量任务及Wilson区间不授一般安全。需可重置模拟器/可重建工位，换AP可能须重建数据；短chunk仍不消除接触风险。未采用硬件吞吐或deadline数字。

具体owner `MULTIMODAL-EMBODIED-VLA` Ch26：已实际读106～115主动相机/训练接口及邻接，现有主动视角不明确说明“AP接手状态必须与manipulation训练起始分布相容”。拟在主动操作两段之后补此接口，不接管Ch23表示或Ch25动力学。尚待独立必要Source/拟稿复核与Books决定。

## 23372 IMEP / Beyond Success Rate

[精确v1](https://arxiv.org/html/2610.23372v1)，实际§3～4、Limitations、F.1及G.1～G.3受影响纠错；3+2+2=7，反证与纠错深入。区分net benefit、任一结果翻转和任务事实特异性：同fact与异fact替换之差须有exact repeat、安装路径及实际读取到替换内容的检查。U与C路径不同，U−C不能说是纯数值噪声；latent置换/重采样也未认证语义fact编辑。非显著不是等效。

框架为campaign结束后整理，不能叫全程预注册。full-vision ShellGame ladder已由作者撤销Q3/Q4证据，原数字不用于内容利用结论；其他有效结果不随之删除。ChainBench202与143不同人口/manifest不合并；共享录制执行使相同正确决定有相同动作成功，不能当两份独立完整闭环证据。143重建manifest有未消除选择偏差。learned-bank的有限/未决结果不证明所有VLA不用memory。未采用硬件性能数字。

owner `PLATFORM-EVALUATION-SYSTEM` Ch66；Ch77已有无memory基线/当前可答性、oracle清洗与真实resolver分责，但这不等于同fact/异fact受控替换的内容因果归因。拟只补评价接口，不复制memory runtime；尚待具体书段与独立复核。

## 22576 Embodiment-Classifier Guidance

[精确v1](https://arxiv.org/html/2610.22576v1)，实际§2～6、主要控制/反侧；2+2+2=6，标准必要域完成。冻结flow-VLA，用两本体成功rollout的加噪action训练分类器估计密度比，将其梯度加到采样速度场；classifier不直接看图/任务，但action坐标隐含末端pose。不是零目标本体数据、不是新任务泛化，也不是更新主policy权重。

修正依赖clamp/20%cap及调w的启发式。仿真一policy一bench，同200episode与放宽步数预算；controller改变多有益、弱腕/锁腕可害，简单已知delay规则可更好，预注册“何时guide”规则未通过。多数仅一seed，五次复测含事后挑选；guided collection受一transfer task启发，不能叫纯holdout。成功样本选择、classifier训练/采样梯度及重采费用均保留；未采用吞吐/deadline数字。

owner `MULTIMODAL-EMBODIED-VLA` Ch26：现有动作codec-guidance在训练时消费GT，不是部署时从成功密度比修正冻结sampler；需要定点比较现有value/采样引导后判断最小差额。暂未写Books、未独立Source验收。

## 23566 TRACO

[精确v1](https://arxiv.org/html/2610.23566v1)，实际III-A～F/Algorithm1、IV-A～F关键对照及限制；3+2+2=7，安全变化必要深入。白盒攻击者构造期可读参数/梯度并查询target指令；部署仍给user指令。固定视觉扰动优化时反复在攻击诱导的新状态重取target行为，PGS同时关注停滞前沿与早期前缀，避免新更新毁掉先前进度；不是更改合法用户指令或授权机制。

共享50state误差对照与progress消融支持有限机制；主要baseline各自优化设置/成本不同，不归因全部ASR差额。真机每条件15trial，printed patch结果只属有限可行性。position进度不保证抓取已成功，teacher在偏离状态不会恢复时监督仍失效；追加rollout/梯度/控制成本要计。计时含加载和辅助处理，不授通用攻击成本或防御失效率。未看图像/视频、核代码或复现。

拟owner `PLATFORM-SECURITY` Ch72：只承载威胁构造如何因闭环状态反馈而改变，物理controller仍由Ch26拥有、测量由Ch66拥有。须先比较当前具体安全段后决定NC或最小整合；未写Books/未独立Source验收。

以上四项仍须非root的必要Source/具体Books决定复核，不预整日验收。没有因为阅读较多将无关RO标题全部扩成队列，也不把普通未读写成外部缺口。
