# 2603.09883：稀疏交互条件与对象注意力偏置

root作者necessary Source/date/具体owner/PRE及实际写后均经非作者supplement_20260312复核通过，见[独立记录](./SUP_REVIEW_09883_CHILD.md)；仅计本项确认及实际整合，不授DAY。

[DISPLAY精确v1](https://arxiv.org/html/2603.09883v1)。实际§3.1–3.4、Eq1–3、§4正文/Tables1–2、Appendix0.A/0.D/0.F；只采用条件分工和受限反侧，未核视频像素、全部数据构建、代码或复现。原batch3完整题摘/current/history及owning arxiv.content/findable字段实核，submitted Mar10UTC16:40:41不是公开日，registered Mar11UTC02:24:12已可发现上界与官方最早Mar11BJT08下界夹证同日。当前v1/无可见撤回纠错信号，不声称全史。2+1+2=5，具体条件—容量接口差额必要深入，唯一MULTIMODAL-GENERATIVE-PARADIGMS。

## 支持与关键反侧

§3保留Wan2.1-14B flow/DiT、冻结原T2V，以克隆部分transformer的ControlNet-style条件分支注入；四路是wrist/box稀疏运动、masked background、object reference和visual reference。motion/bg沿channel concat，引用图同VAE编码后沿sequence concat并复制channel适配维度。稀疏box有中心/大小而无物体形状或contact/force事实；VAE共享latent不使对象身份真实。

Eq3 Object-Stressed Attention把涉及object tokens的相似logit交叉块乘α、object-object块乘α²，softmax后values没有对应α缩放。它是attention偏置，不给合法接触或几何满足硬约束；α越大不保证单调改善或信息无损。§3.4/0.A以Bernoulli丢弃motion/background部分和首帧/首尾配置训练缺条件分支；无object标注时以零reference且省box。此训练支持接口缺省，不代表任意测试缺失可补全事实。

§4/0.D比较不同baseline条件：HuMo另读音频，WanAnimate另有Nano编辑/完整骨架，VACE/Hunyuan用不同inpainting输入；不能归全部差额为OSA单一因果。Table1 LPIPS/SC/HF并非各项最优，不复制全面领先；Table2 w/oOSA是必要局部对照，w/oMTT也减少更大数据，不能隔离训练任务或数据规模唯一作用。14B条件分支、32×80G两周训练、1e-5学习率/数据标注、逐步denoising、视频输入和mask/cue/参考图处理全部计费；sparse input不等小模型或低总成本，长视频案例不认证长期稳定。完整precision、concurrency/SLO、独立seed/CI未披露，不补造。

0.F明确非刚体形变不被sparse guide建模，SAM分割复杂形状缺损会影响保形。画面质量/appearance/motion proxy不能授权physical transition、接触或机器人动作。无物体/弱motion训练也不认证未见身份的shape泛化。

## 实际owner与逐字PRE

实际Ch24 1534–1549完整camera/动画时钟→分阶段pose/depth→生成后训练交接及Ch23/25开篇：现有schedule控制强度，不承载wrist/box与对象reference的分路残差条件及object-logit偏置。拟在原camera/motion完整两段与source结束后、生成后训练标题前插两段；生成器条件主权唯一Ch24，Ch25/26不写物理保证。

控制信号还可以按它提供的信息拆开，而不让一套 dense pose 同时承担对象外观和交互位置。一个视频生成分支用腕点与不含形状的对象 box 描述稀疏运动，另给对象 reference、整场景 reference 与遮罩背景；冻结原生成主干，在克隆的条件分支中按空间/时间接口组装并注入残差。对象参考 tokens 的 attention logits 可被额外放大，使外观线索更易参与去噪；这改变条件的竞争权重，不把 box 或更强 attention 变成合法接触、形变或物理转移约束。训练时对 motion/background 条件作随机缺省，让同一接口支持编辑、首帧或首尾条件，但缺省能力仍依赖训练支持。

[受限交互视频对照](https://arxiv.org/html/2603.09883v1)支持稀疏条件与参考外观分责，不认证真实 world state、任意对象或低总成本。不同基线读取的骨架、音频及编辑结果并不相同，辅助训练又增加数据，质量指标也并非全部改善；须分别验条件遵循、对象保形、运动和最终视频。原主干虽冻结，条件分支训练、参考/遮罩构造、VAE与每步去噪仍计费，缺省/尺度/坐标和模型版本须共同绑定。非刚体、复杂形状分割或训练支持失配时，保留更密集的pose/depth、原inpainting/专用控制和独立视频验收，不用逼真画面批准实体交互或机器人动作。<!-- source-family:SF-2026-ARXIV-2603-09883 -->
