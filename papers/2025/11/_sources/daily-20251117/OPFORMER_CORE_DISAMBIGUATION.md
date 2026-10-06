# OPFormer Exact-v1 Scope Disambiguation

Carver按root独立校准的具体歧义定点补读，2026-10-04。不是重复root31份AB抽检或全66实验审阅。

[原HTML v1](core-2511.12614v1.html)HTTP200，receipt实际UTC12:22:20。实际读§1贡献、§2相关设计、§3.1/3.2/3.3与§4.1评价对象；未扩附录/BOP全部结果/代码。HTML页头16Nov仍不是public时间证据。

## 决定范围的事实

§1和§3.1：输入为RGB检测crop、camera intrinsics及CAD或带known poses多视图图像；model-free onboarding仍用准确姿态图像训练Instant-NGP，再渲染RGB/depth/NOCS模板。它不是在无几何监督下形成一般空间知识。

§3.2.1：frozen ViT-L DINOv2 with registers，trainable weight adapter聚合24层patch descriptors。§3.2.2确有具体3D RoPE：模板NOCS `(x,y,z)`使q/k在每6维的三个2D子空间旋转，再跨模板self-attention；这比“只把既有foundation模型换应用名字”具体，不应抹掉机制。§3.2.3为image/template双向cross-attention，但没有text/action模态或general VLM objective。§3.2.4由template voting、six neighbors、dual-softmax threshold、已知depth提取对应点，经PnP/RANSAC产出6D pose。

§3.3训练是2M GSO/ShapeNet合成图片的template↔image patch contrastive/focal correspondence；§4.1全部验证目标是BOP unseen-object 6D localization/detection，指标VSD/MSSD/MSPD的AR/AP。没有实际模型通用表征形成、语言条件动作、环境状态反馈、failure-envelope或跨任务可靠性结论。这里只核评价对象，不采用效率/排名数字。

## 作者建议 / 非作者待裁决

建议从范围边界potential改为**本项目范围关闭**：新3D-RoPE/inter-template matching机制服务已知几何条件的pose correspondence，实际新增目标/验证仍是特定视觉6D估计；现有Ch13/23/26能联想到它，不足以自动建立本阶段foundation/multimodal/action主线增量。不是因小模型、CV类别、frozen backbone或未读全附件而关闭。

root若认为该object-coordinate RoPE本身提供可保留的一般表示/位置机制边界，争点已缩至§3.2.2及其实际适用/验证范围；请独立裁决，只重开此点。当前作者尚不授关闭独立通过/日级完成，也不写Books，原66初步potential统计保留，待root明确裁决再同步漏斗与日期请求。
