# 01-16 / OpenVoxel 必要原证与owner差额

后续实际状态：root必要原证/actual owner PRE通过并授顺序窄锁；Lite actual POST通过/释放后，作者已写Ch23两段940/942及自身末注1506并实际顺读928–956完整局部邻接。root非作者实际独读928–956完整邻接/940,942新正文及自身末注POST PASS，Ch23锁释放；下文“待PRE/未写”保留原提案过程，不是当前事实。未核实现/复现，不授日级Gate。

待root独立准入/必要原证/实际owner PRE，未写Books、未授锁/DAY。exact-v1 abs09575/HTML/date与直接作者project已捕获；normalcohort公告Jan15下界＋exactDOI registeredJan15T02:49:18Z公共存在上界条件限定Jan15，非注册=首公开。project只现CVPR2026/comingsoon/正文描述，没有更早论文release日期；当前页未见不是无早稿保证。

## 改变的实际表示

§4.1–4.3/Table1–5、A必要merge/实现段、C三priormodel反侧、E直接限制已实际读。预先重建SVR scene之上，voxels的group feature只存3Dcentroid、confidence-weight和group dictionary；以每view SAM2mask与ray-hit位置平均投到3D、renderer加权累积、已有group投回新view按IoU match并重prompt合并，未匹配新ID。它改变 per-primitive learned high-dim feature 的对象关联载体，不只是caption换任务；centroid投票、IoU与90%包含合并仍heuristic，不证明真实实例或所有view一致。

DAM对每group8frame-mask caption，Qwen3VL8B把caption/query改固定category/appearance/function-or-part-of/relation模板，完整scene-map ID/center/caption输入模型选择ID，最后renderer给对应mask。几何字段+modelcaption不是完整scenegraph；“deterministic matching”不由同模板保证。E明确partquery仍回整对象、显式part-of/relations graph只future，不把中心或affordancecaption变物理事实。

## 对照、预算与必要反侧

LeRF3scenes OVS6/7/10与13/17/12objects；RefLeRF4scenes13/17/12/11objects。RES42.4高于ReferSplat29.2及作者复现24.5，但缺部分officialmodels而自行重训，不能全部唯一归因新检索对象。OVS平均66.2略高65.1，figurines60.7低于3DVLGS73.5；Mask87.2低ObjectGS88.3，非全面优。Table4累积maskmerge24.3→28、canonicalcaption36.4→canonicalquery42.4，未独立全交互/预算配平。

PyTorch/SVR、SAM2/DAM/Qwen3VL8B、RTX5090；per-scene最多150views、merge每1–5step、8frame-mask/caption、无visualICL且关CoT换快查询。所谓3min分组/caption是在已有pretrainedSVR之后；SVRscene fit、priorweights、modelrequests、全scene-map tokens、不同scene调参都付费，precision/batch/concurrency/tailSLO与重复不确定性Not Disclosed。ReferSplat作者58min在A6000，本篇复现在5090≥2h，不能跨硬件通用10x。

C：SAM→SAM2 RES30.5→42.4；captionOsprey29.3/Qwen8B33.3/DAM42.4不等inputmodalities；canonicalization/retrievalQwen3VL2B9.98%、4B35.6%、8B42.4，另Qwen2.5VL7B23.4。模型和prompt限制是实际失败，不授scene map与模型无关可靠。E：samplerate/mergefrequency scene-specific、SAM2需调；对象part合并不可逆、view-dependent query可给多对象。Scannet附加深度guideSVR/nearest25NN/50NN与GTinitializationbaseline协议不同，只不采用跨协议总优，未为该非采用命题展开全部semanticseg附录。未核代码/复现。

2+2+2=6；具体对象表示载体缺口拟深入已读够必要支持/反侧。不是省全部训练或真值objectmap。

## 实际owner与拟窄整合

Ch23 actual917–955完整native3D邻接已读：既有query-view位置、混rig、superpointtoken、readonlymesh/nativeprimitives、parttransport与4Dtrack/MLPfastweights，已经有identity非truth一般约束；尚未有从已有重建得到centroidvote实例group、caption与原view分责、partquery被instance合并吞掉的具体derived representation路径。这里只owner表示对象；不扩Ch25世界transition或Ch76通用检索。拟两段在L936独立3D reconstruction sidecar段前，待root实际PRE/锁。

已有多视图重建但只需语言定位对象时，不必立即把几何纳入统一生成模型；另一条分支在稀疏voxel之上维护指向实例中心的三维group feature、权重与ID字典，逐view把2Dmask升到3D、投回新view匹配/合并，再让消费者读取group ID、center与caption。这让共享对象从高维language field变为显式group及文本描述，却仍是由分割/重建派生的实例proposal；centroid投票和mask重叠不能认证同一真实对象，caption中的关系也不是新增物理观测。[OpenVoxel的受限对照](https://arxiv.org/html/2601.09575v1)支持这种静态读取分工，不授任意场景或query的无训练理解。<!-- source-family:SF-2026-ARXIV-2601-09575 -->

实例分组先做合并，还会丢掉后来part query需要的粒度：问相机灯仍可能返回整台相机，中心字段也未提供完整part-of图。Canonical caption/query减歧义仍依赖MLLM，较小模型甚至严重回退；需保留原view/mask、group合并来源和可重建路径，而非只存一份“稳定”文本。已有scene fitting、SAM2重prompt、caption与全map读取都付费，3min分组估计不含全部预训练/重建、也不授生产SLO。对象支持、视角/粒度或模型预算失配时，回读原图与细mask，保留learned field或专用几何工具；需要跨轮编辑时，再把revision与native几何状态交给后续接口，而不是由group ID取得几何真值权限。
