# ReLaGS17605：本20必要原证与最小PRE

resume_mar17 sole必要准备，仅03-20补03-19自然日；原2+1+2=5与同日有效准入/date复用。准备不自授Source/PRE、写锁、I或DAY，支持/直接反侧足此有限接口即停止。

## 1. 实际精确源与停止范围

[exact-v1](https://arxiv.org/html/2603.17605v1)必要§3.1–3.4/Eq1–10、§4.1–4.4/Table1–7、Appendix7实现、10直接pruning反侧/Table12、11真实GT对齐/closed-set读出协议及16静态限制实际已读。Appendix6仅335–344训练/预训练数据分责，不冒完整GNN实现；Appendix9定点358–367改变densification/GT投影人口不并主Table4。当前abs8–27同八作者单v1、CVPR2026接受，无具体重要修订信号。没有代码、图像像素、引用理论或全附件/复现。

## 2. 支持与未采用桥

已有训练好的2DGS场景，经SAM多级分组保Gaussian→superpoint→part→object层级，在共同几何身份上挂CLIP语义；不是只由语言凭空生成3D地图。主文ROFA用view相似度均值/zscore筛低值，单view或相同score会有零方差，原守护未全披露；不采精确筛选recipe/可靠性真值。MWP是所用camera/pixel的最大alpha-T贡献阈值，低训练视图贡献不保证未来不可见物无用，强剪枝Table12会崩溃。

root层关系在对象之间，子层是对象内部，跨对象parts关系主动汇到父对象；不是任意细部全连接图。SoM多帧MLLM关系标签取频率较高谓词再编码，或用外部3RScan/3DSSG监督预训练的GNN读节点几何/语义预测边embedding；两者是关系proposal而非独立真值。3D语义query从root候选按CLIP相似度下探并保候选，triplet查询共同约束subject/object候选及边谓词。该接口改变可读出粒度与检索条件，不建立action transition/因果模型。GNN无需逐场景语义再训练，不等辐射场不用训练或先验没有成本。

## 3. 关键评价、直接反侧与费用

Table1在RIO10/160类别27谓词，GNN object.68/.79低于RelationField.69/.80，predicate.79/.87对.76/.82；文字的.3/.5与原表.03/.05尺度不一致不采headline。VLM谓词.10/.35弱，不能由可渲染图推空间关系真值。Appendix11实际GT点最近Gaussian后，为每个GT对象选择IoU最大层级cluster，再按固定类别/谓词词表cosine读出；该oracle对齐/closed-label人口不证明开放实体检索或真实地图一致。Appendix7训练排RIO10测试序列明确，80epochs/RTX3090；不是泄漏指控。

Table2关系查询ScanNet++关闭densification/pruning保点-Gaussian对应，预训练GNN无需该场景新增标签但非无历史监督；不同query协议不与纯concat文字baseline当等价算力。Table3 Ramen/Waldo有更强方法，Table4原19class mIoU32.35<THGS34.39/mAcc44.52<50.74；Appendix9改densification/GT映射可改善，但须分人口。Table6更强z阈值不单调，Table12重剪枝严重损失，较轻阈值也能降低mIoU而render近同。Table7峰值32GB/7.5GB约4.27×，500MB/65MB约7.69×是storage，不能互换为7.6×显存；scene重建/语义蒸馏/graph各费用与GNN预训、SAM/CLIP、MLLM标签、设备/传感器准备须分账，完整端到端费用/SLO/置信区间未披露。只静态场景，动态更新在Appendix16仍未来工作，不签在线状态/控制安全。

## 4. actual唯一owner与差额

sole `MULTIMODAL-WORLD-MODELS`/[Ch25](../../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)。实际开篇1–29、655–690 observation/query图→ZipMap参数化静态场景→动态memory交接，以及870–904可执行transition/CodeGraph在线状态顺读；Ch23/26开篇权限交接已读。ZipMap拥有fast-weight颜色/geometry查询，不承载对象/part嵌套地址与关系edge的联合查询；CodeGraph拥有执行后在线图修订/任务谓词，不能冒作静态重建关系读出已覆盖。拟ZipMap完整source04385段后/短视频动态memory前两段，保静态derived scene estimate非事实/transition。不是新建章节或重写通用图表示。

### 正文PRE 1

静态场景的查询也可以从相机ray读出转向实体粒度和关系条件。一个受限分支在已有Gaussian重建上保存对象—部件的嵌套分组，把跨视图语义聚合到共同cluster身份，再用关系标签或外部监督预训练的图网络给边产生谓词表示。文本查询可沿层级选择对象或细部；关系查询则共同消费subject、object与边谓词，跨对象的细部关系仍被汇到父对象。这是可寻址场景估计与检索条件，不是新增真实观测、因果transition或任意细部完整关系图。<!-- source-family:SF-2026-ARXIV-2603-17605 -->

这条[有限静态关系读出](https://arxiv.org/html/2603.17605v1)把重建、分组、跨视图语义与关系消费分开，但相似度筛选和模型关系仍可能错；低渲染贡献或高语义一致性不认证几何正确。真实对象对齐后在封闭标签域读出的评价，与开放实体/关系query须分验；更多剪枝或更强筛选可损伤细部，部分原类别指标也退步。场景重建、语义encoder/分割、图预训练或模型标注、层级与边存储和查询全部付费，不把省去逐场景语义训练称为零训练或完整显存收益。动态对象、层级错配或关系证据不足时，保留原view/geometry查询、真实局部监督与新观测校正，不让静态语义图取得事实状态或动作权限。

### 静态来源注PRE

- [ReLaGS2603.17605 exact-v1](https://arxiv.org/html/2603.17605v1)：必要§3–4/Table1–7与Appendix7/10/11/16。仅静态Gaussian重建上的嵌套实体地址/关系候选查询；保外部监督、GT对齐/封闭词表评价、筛选/剪枝反侧与storage/显存/完整费用分账，不采精确ROFA守护、空间关系真值、动态transition或控制SLO。未核artifact/图像或复现。<!-- source-family:SF-2026-ARXIV-2603-17605 -->

交reader非preparer有限Source/actualowner/两literal/static裁；未root授sole锁不写。若要采用强可靠性/在线状态桥只一次请求实际筛选守护、无GT实体对齐的关系人口、动态修订与完整预算协议，不为等待这些桥否定可核静态接口。

## 5. 非准备者必要Source/owner/逐字PRE有限裁

2026-10-12 resume_review17_18以本20独立上下文实际核exact-v1 §3.1–3.4/Eq1–11、§4/Table1–7与设置、Appendix6仅335–341训练分责、7实现343–347、9仅358–367人口变更、10决定性Table12、11 GT对象最大IoU层级对齐/closed-set词表与16静态限制；current abs8–27八作者单v1/CVPR2026接受无具体重要修订。未读代码、全部附录/图像像素或复现。实际Ch25开篇1–26、647–704完整query closure→ZipMap→动态memory，及870–904可执行图/CodeGraph状态交接、Ch23/26开篇权限已读。

必要Source、actual唯一owner差额和原两literal/static有限PASS：Gaussian→嵌套cluster与语言/边谓词共享地址，GNN外部监督与SoM标注来源、query联合消费三种相似度有实际方法支持；不授causal understanding、空间关系真值、动态或动作权限。单view/零方差筛选守护未闭合、19class反退/激进剪枝与封闭标签GT对齐、storage与peak显存及全部费用均已在拟文附近，不能把无逐场景语义训练外推成无训练。原5/date复用；拟ZipMap source04385完整后/动态memory前两段不重复CodeGraph在线职责。未写Books、未actualPOST、无锁或DAY；root授权writer后只一次非writer实际完整局部与本人源注POST。

## 6. writer窄写与自读（非POST）

2026-10-12 root授soleCh25后仅原两literal与静态注实际写新685/687/static1789；writer完整677–704 ZipMap→新实体关系查询→动态memory及1783–1789本人/X-World/VectorWorld邻注实际顺读。两正文/静态注逐字相等且注唯一，限定diffcheck0。原本与并发其他family不动，不改验收identity。交resume_review17_18一次nonwriter实际POST，未获接纳不计I、不授DAY。
