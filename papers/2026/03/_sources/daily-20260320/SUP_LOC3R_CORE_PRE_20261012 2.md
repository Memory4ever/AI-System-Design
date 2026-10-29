# Loc3R18002：空间监督与语言定位消费者

## root实际写入（待非writer POST）

reader必要Source/actualCh23/原两PRE/static有限PASS后，MM-OVSeg该文件锁已释放；root sole本family仅原两literal写在VGG-T3完整段后、Token Hierarchy前，本人静态注章末。实际1154–1170及末三顺读、限定diffcheck0，旧数据及邻注保留；写者不自POST/I/DAY，交reader一次完整局部邻接与本人/邻注实际核验。

root sole准备；本20补03-19自然日，既有2+2+2=6及日期不变。未自授Source/PRE独核或写入。

## 必要原证

[exact-v1](https://arxiv.org/html/2603.18002v1)实际§3/Eq1–13、§4.1/4.2定位协议与QA metrics、§4.3/T6–8、0.C效率及0.I–J直接失效边界；current仍同v1，无具体撤回/纠错。不核全影片、未采用全部成绩或代码复现。

冻结CUT3R生成逐帧camera token，MLP投影后前置于SigLIP视觉token，不读所有geometry特征；训练LLM/投影与heads，以groundtruth depth/pose生成首帧锚定、重力对齐BEV的空间监督。视觉hidden读出xy Gaussian NLL；文本situation之后的Pos/Ori hidden另以position NLL、yaw bins圆周标签/KL监督，与语言CE共训。后续答案读取hidden，不是把外部预测数字再喂入，也不能据方差头断言校准不确定性或唯一因果使用。该离线视频内部表征不提供跨任务persistent map/环境transition。

LLaVA-Video7B、32帧384²、16V100、globalB64/1epoch4.2k；training用depth/pose标签而inference不取GT。定位metric用GT首帧pose只作旋转/平移对齐；不是全球绝对坐标或无监督系统。719样本/67室内景定位与QA多metrics分账，T6–7消融是更小训练人口，不混main结果；T8更多geometry tokens反退。0.C4090fp16/32帧的2.6s是TTFT加geometry而非完整回答SLO；预计算、额外encoder、标签/对齐、训练与质量校准都付费。0.I可定位正确答错、定位错答对；BEV丢高度，32帧漏证据，静态室内不外推动态/户外。尺度prior不是标定真值、NLL不自证校准。

## actual owner与差额

sole `MULTIMODAL-REPRESENTATION`/[Ch23](../../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)。实际1148–1164轨迹consumer、分组共同首帧与VGG-T3可查询scene fitting完整邻接、开篇表示契约及Ch25开篇video/transition分责已读。现重建/fastweights不承载空间监督→语言situation定位hidden→答案consumer这一差额；不另造WorldModel状态或物理action owner。拟VGG-T3完整段后、Token Hierarchy前两段，待MM-OVSeg本family Ch23 POST释放及reader非preparer核。

## 正文PRE

场景能够重建或被查询，仍不等于语言模型学会了“从指定位置朝某方向看”。一条受限分支保留逐帧视觉token，只把预训练几何模型的camera token投影后前置；训练时用有深度和位姿标签的重力对齐BEV监督视觉hidden的平面位置，再以文本situation后的专用hidden监督位置和yaw，与语言目标共同训练。后续答案可以读取这些hidden，但不是把外部坐标当已验证事实喂回模型；几何先验、空间标签、定位读出与答案消费者各有不同权限。<!-- source-family:SF-2026-ARXIV-2603-18002 -->

[空间监督的有限对照](https://arxiv.org/html/2603.18002v1#S3)区分训练用真实深度/位姿、推理用估计的camera prior以及评价时的坐标对齐；无推理GT不等无监督或已知全球位置。BEV会丢失高度，固定帧数会留下盲区，位置方差也不自动是校准风险；定位正确仍可能答错，答对亦可能绕过错误定位。额外几何编码、标签制备、投影与联合训练、缓存和回归都计费，首token局部时延不是完整回答SLO。应分别验坐标/视点、答案与成本；动态场景、覆盖或尺度不可靠时，保留原视频回读、显式几何/定位工具与Unknown，不把静态室内表征当持久世界状态或物理行动许可。

## 静态注PRE

- `SF-2026-ARXIV-2603-18002` — Daily `2026-03-20`补查；[Loc3R exact-v1](https://arxiv.org/html/2603.18002v1)必要§3–4/0.C/0.I–J；2+2+2=6。仅camera prior、BEV/situation监督与答案hidden消费者；保GT训练/评价对齐分责、平面/yaw/静态室内限制、定位与QA不互证、geometry反退与全部费用，不采校准方差、全球坐标/完整3D、persistent state、真实控制或SLO。未核代码或复现实验。

## resume20_reader_new非准备者必要Source/actualowner/PRE裁

实际exact-v1 §3/Eq1–13（126–203）、§4.1配置（206–210）、4.2定位协议/坐标对齐与QA分指标（214–234/292–297）、4.3/T6–8（305–339）、0.C（492–501）、0.I–J（570–584）及current同六作者单v1读；不需遍历全帧、所有成绩/可视化或其他附录来支持两PRE，无artifact/复现。

CUT3R冻结/逐帧camera token经MLP前置而非注入所有geometry，LLM/heads/projections可更新；空间监督视觉hidden GNLL读出2D BEV，首帧锚定/gravity-aligned、真实depth/pose用于训练。situation后Pos/Ori hidden位置GNLL与36yaw bins圆周target/KL/语言CE，答案可causal读取hidden并不证明唯一依赖或将外部预测数字喂回。GNLL方差、相似的QA/定位相关切片不认证calibration。评价仅GT首帧旋转/平移对齐、无scale拟合，与inference无GT分责成立，不授全球绝对位姿。

主设置32frames384²/16V100/4.2ksteps/B64，定位719samples共享67indoor scenes；定位xy/yaw threshold、QA ngram/数值/多选/GPT不同对象不拼统一准确率。T6/7更小训练人口不混headline；T8加geometry分支反退也改变token与projection预算，不授唯一冗余因果。0.C 4090fp16/TTFT+一次1.2s几何，总2.6s与20.3GB只是局部；预计算/cache不取消原制备/维护。0.I正确定位/错QA和错定位/正确QA分别暴露非互证，0.J BEV高度/32帧盲区/静态indoor范围与全部标签/几何/训练/decoder/回归成本保持。

实际Ch23完整1153–1175轨迹消费→分组共同首帧完整两段→VGG-T3完整scene fitting→Token Hierarchy及有效开篇/Ch24/25分责复用；不将只camera input或可查询scene当该监督已有覆盖。soleCh23最小差额为BEV视觉监督→situation定位hidden→后续答案consumer，拟VGG-T3完整段后两段；旧scene fitting权限与新label/hidden权限衔接成立，不造第二owner/持久WorldModel。**必要Source/actualowner/原两literal/static有限PASS**，原6/date保持；rootsole窄锁后才可写，待一次actual非writerPOST，不预I/DAY。

## resume20_reader_new一次非writer实际POST

rootsoleCh23实际写入后，复用有效Source/PRE，不重核源；本人实际完整1150–1176（camera/track→SGCoT→组共同首帧完整两段→VGG-T3完整→本两段→Token Hierarchy完整入口）及末7/本人与MM-OVSeg等局部邻注顺读。原两literal/static机械逐字唯一各1（1164/1166/1856），本family六新增与此前已验多family分账，cached/unstaged限定check0。camera/GT训练/评价对齐分责、hiddenconsumer非外部坐标、GNLL非校准、QA/定位不互证、静态indoor/高度/覆盖限制和全费保持；前后旧段无权限覆盖。**一次有限actualPOST PASS**，交root接纳释放Ch23，不改static身份或自计I/DAY，原6/date保持。
