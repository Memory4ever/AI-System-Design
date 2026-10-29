# 01285：知识型视频的事实与可用性评价

## 范围和首次必要审阅

仅06-03补Jun02自然日，AGENTS和当前研究/Report合同、Daily来源/Prompt已重读；Book三约束、ROADMAP及actual Ch66与邻65/67交接已读。R62完整题摘/具体准入有效，不据旧marker断言已审重复。精确[Knowledge-Intensive Video Generation v1](https://arxiv.org/html/2606.01285v1)，本轮实际读§3–5/T1–6与A.1/A.4/A.5；未看例图像素、全部gallery/实现或复现。[当前官方事件页](https://arxiv.org/abs/2606.01285)实际开，v1 May31 15:11:07Z、v2 Sep28，所见无撤回/勘误，后版不倒填。

日证沿R62及[已存精确导航](./SUP_MULTI_NAV_20261023.json)：适用EDT公告/发号最早Jun02 00Z，同一DOI `arxiv.content/findable/registered=2026-06-02T04:11:53Z`限定最晚界，整个区间在Jun02 BJT；不把提交/登记单字段改名公开、不重复GET。原小时窗/已有候选日期保持。

## 采用命题、评价条件与反侧

候选新增的是生成视频的事实精度与用途完成不等于画质：先提取可核文本claim，以参数知识标Correct/Incorrect/Uncertain；另判相关、完整、清楚。所提FactP是逐item正确claim占全部claim的比例再宏平均，既不测缺失步骤，也不验证文本所述确被画出。Text+Video/Image比较只给同一文本claim添加定位片段，不自动成为独立真值；正文承认text-only会漏视觉grounding。图像更逼真、outline文字正确均不保证生成阶段不引入实体/步骤错误，例子只作有限失效观察，不识别普遍内部因果。

1080是prompt库，不是本次全量实验；实际七模型只54 prompts、每类3，目标约60秒，短片模型用规划/末帧接续拼接，Helios因实现问题用不同模式。全部规划/提取/判分共用Gemini3.1ProPreview温度0，有同源偏差，非独立world-knowledge oracle；参考人类视频另选54题，不是同题人机因果比较。A.1仅10A100资源说明，不补造精度/分辨率/并发/端到端SLO或总费用。

人工108对、6人每对仅1人，分组限制对比且强制二选；自动tie给半分。这是特定pair人口的偏好一致性，非逐claim正确率、校准置信或标注一致率，无独立重复/区间不称普遍显著。T3 text-only更同意人工但更高FactP，也可能正因漏视觉grounding；不能推荐删除原视频证据。HelpS显示式与0–10尺度/百分比口径未统一，完整公式不采用，不私修为可复现指标。全部生成、规划、视频取样、提取、验证与人工均计费；不足时回原视频/必要时段/外部文档和Unknown，不让自动总分签真实操作安全。

评分提案2+1+2=5：新增是单评价组件的具体盲区证据/替代分账，不借video模型数量或一般安全原则扩大Reach；必要反侧已足，停止全附件。R62初拟Ch24是路由而非owner判定；实际长期评价机制由 `PLATFORM-EVALUATION-SYSTEM` Ch66承载。

## 实际owner比较：提议已有覆盖，待首次独核

并非只因都叫评价而NC。已实际读这些完整论证及直接两侧：

- Ch66约1299的视频生成meta-evaluation完整段：短片/画质相关不自动授长视频scorer资格，控制退化/人筛人口和真实错误分别验。
- 1319–1327目标状态/过程与对象、动作、场景、观感分维；自然caption的逐claim原视频支持、Unknown/时间错位，以及原子/组合绑定和precision未补遗漏的完整组。已承载画质、步骤可用性和视觉支持不能互代，不能由outline正确批准所生成内容。
- 4567起Evidence Trail完整组/2602-11509：claim支持/coverage与答案正确性分别验，保modality/时间、实际支持及外部独立核验，已有textual truth不能替代画面grounding的具体机制，而非只一条泛泛“不保真”。
- 5302 Judge Agreement完整两段：population/scale/abstain/pooling/metric身份与excluded fraction、人工误差和区间分责，已覆盖108对偏好一致不等逐claim真值/部署能力；186用途→EvalSpec亦不让画质成为教学/操作成功定义。

新基准的具体模型排名、小样本/共用judge和text-only反侧留Report证据即可；未发现独立可采用却缺owner正文的长期机制，不重复追加新benchmark摘要或表格。提议具体已有覆盖/No Change，无正文/Review note/PRE/POST写入；尚未经本项非writer必要/actualowner核验，不预NC通过或DAY。其余16项仍普通，下一00515尚未必要。
