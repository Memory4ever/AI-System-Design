# MultihopSpatial 18892：必要评价证据与最小整合稿

root 准备，仅03-21补BJT03-20；准入由本日完整题摘独校通过。此稿待非准备者 Source/必要日期/actual owner/PRE 核验，不是已经写入或DAY。

## 精确版本与采用范围

[exact-v1](https://arxiv.org/html/2603.18892v1)。root 实际读 §3.1–3.2、§4奖励及输出接口、§5.1/Table1、§5.2–5.4/A1–A8直接解释与0.D验证、0.F限制；只采用 evaluation contract，不授训练recipe、VLA迁移数字、代码或复现。必要公开日由作者核已有有限公告/DOI，不以submitted日自动落窗。

原 MCQ 只验选项→静态图像增加目标框、按原分母计算回答且定位都通过的joint，并另报正确回答子集上的IoU→重新考虑回答准确率是否足以验证空间输出可用、条件均值是否可直接跨模型排名。建议2+2+2=6：改变具体评价对象，连接模型输出与其消费接口，不给benchmark规模/借用joint原理/机器人宣传加分。

## 必要原证、反侧与停止范围

- §3：3563 COCO/PACO-Ego4D图，4500题按1–3hop与ego/exo平衡，十人工标注与三轮交叉验证；hop是同时满足的属性/位置/关系，不验证生成推理步骤真值。人审一致性α.90不消除全部标签不确定性；共享图上的多题不等独立环境样本。
- §4/5.2：输出Answer选项＋归一化0–1000 bbox。MCQ accuracy以原题数计；Acc@50IoU要求MCQ正确**且**IoU≥.5，仍用原题数；AvgIoU仅在MCQ正确子集，模型改变则条件人口改变。训练奖励format+MCQ+(GIoU+1)/2是加法，不是joint发布门。
- Table1/§5.3–5.4：选项排名与joint定位排名不同，足以发现评价盲区；但§5.4 A4/A5明确模型native grounding接口不同，不由排序反转识别其全部捷径、内部推理缺失或规模因果。共同prompt不等相同输出能力/预算；不采用37模型普遍谁更强、推理上限、vision encoder因果或物理安全。
- §0.F静态图片边界；定位通过不证明视频时序、真实空间坐标或动作执行。标注/多输出解析/定位验证和调用均付费；输入输出长度、precision、batch、concurrency、SLO和全成本未共同披露，不能由局部benchmark给生产成本结论。正常MCQ仍适合只需要选项的用途。

## Actual sole owner 与差异

`PLATFORM-EVALUATION-SYSTEM` / Ch66。root 实际读197–247上下文及65/67开篇；现CFHR一段已有固定分母joint与条件population，但对象是Q+与多Q-的回答配对，尚未说明一个模型输出内“答对＋目标证据定位”的联合成功、native输出接口混杂和加法训练奖励不等联合验收。紧接CFHR段补一段具体消费接口，承接joint/conditional主线，不重复Ch26动作控制、不建benchmark产品节。

## 待独核的逐字 PRE 与末注

同一份回答内部也可能有两种必须同时满足的输出：选择了正确目标，不等于已经定位它。若任务还要求目标框，可在原题分母上同时报告选项准确率与“选项正确且定位重叠达阈值”的联合成功率；只在选项答对子集计算的平均 IoU 则须标为条件指标，不能把不同模型的子集当作同一人口。[受限静态图像对照](https://arxiv.org/html/2603.18892v1#S5.S2)显示两种排名可以分离，但模型原生定位接口、解析协议和标注不确定性也参与差异，不能由答对但框错直接识别内部捷径或“没有空间理解”。训练时把格式、答案和定位奖励相加，也不等发布时三个条件都已通过。增加框标注、解析与联合验证均有成本；只需文本选项时原 MCQ 仍合理，需要空间输出时保留该联合检查与固定分母，静态定位通过却不签发时序、真实坐标或物理行动安全。<!-- source-family:SF-2026-ARXIV-2603-18892 -->

末注：`SF-2026-ARXIV-2603-18892` — [MultihopSpatial exact-v1](https://arxiv.org/html/2603.18892v1) §3–4、§5.1/Table1、§5.2–5.4及0.D/0.F；仅原分母MCQ/回答且定位joint、MCQ正确子集AvgIoU与加法奖励/联合验收分责。保native grounding/解析/共享图人口/人工标签与静态图范围；不采排行榜因果、内部捷径、规模上限、VLA迁移或生产安全。未核代码/复现。

## 非准备者有限 Source / 日期 / actual owner / PRE 裁决

resume_mar18 已独立恢复本21 AGENTS/适用合同、Sources每日/arXiv、Prompt、ROADMAP与本日STOP，只核本family。实际打开official exact-v1完整AB/history/currentheader，只有project-link comment，无已见纠错/撤回/先稿会议信号；current v2 Sep4只作现页身份，不全版本diff、不采用窗外修订。实际 DataCite created2026-03-20T02:23:25Z、registered02:23:26Z/state=findable；v1Submitted2026-03-19T13:33:26Z、v1Updated2026-03-20T00:59:58Z、Available2026-03。官方本公告批次与日级注册夹证支持BJT03/20 arXiv事件限定归属，不冒精确公告或别处从未公开。

独立实际读 exact-v1 §3.1–3.2（L88–101）、§4/Eqs1–2/格式（L102–118）、§5.1/Table1关键全行/5.2–5.4（L120–229）、0.D验证/L352–374与0.F/L379–381；不展开训练recipe/VLA转移，未读代码/复现/全部图像。原分母 joint 与 MCQ正确条件AvgIoU定义准确。Table1例如ClaudeOpus45.1/3.2与Qwen4B37.8/31.0，确有answer与joint排名不同；A4/A5明确native grounding混杂，原文shortcut/全部真实理解/上限/视觉encoder归因不采。α.90不授无噪声标签，357–368对ego/rel限制与共享3563图/4500题仍保限定范围。加法reward可补偿，不能继承同时通过的发布语义。

actual Ch66完整190–245与补读226–234、Ch65/67开篇实际回对：CFHR现232段说明跨真实/多虚假回答的joint，未已有同一输出内答案与定位两接口的联合门、条件IoU及native输出协议混杂；独立具体差额成立。原逐字一段/末注与Source、sole PLATFORM-EVALUATION-SYSTEM衔接准确，保持2+2+2=6。**必要 Source/日期/actual owner/PRE 正式有限 PASS**，可由root协调窄写；未写未POST，不计safe或DAY。无需追加无关附件或给内部捷径/能力ceiling采用权限。

## 一次 nonwriter actualPOST：正式有限 PASS

resume_mar18 实际独立顺读已写 Ch66 完整210–251、新234及最后八行5932–5939含本人静态注/邻注，回有效必要Source/逐字正文PRE；新增正文literal唯一1，scoped diffcheck无输出。静态注由root将原末注的简略中文补成同义完整表达（“仅采原题分母”“选项正确子集”等），保同精确原证范围和全部采用/未采用边界，未增加科学命题或动态验收身份，不要求因文字展开再循环改注。

CFHR跨回答配对→单回答内answer/bboxjoint→indistinguishability前后衔接自然；原题分母/条件population、加法reward不等联合发布、native接口和静态限制/全费/旧MCQ退路保持，不授内部shortcut/能力ceiling/VLA安全。**一次实际POST正式有限PASS**，可root接纳释放soleCh66并计actualI；不预支日级DAY，不再重读无关源或修改静态注身份。
