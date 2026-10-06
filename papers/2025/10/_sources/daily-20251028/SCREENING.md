# 2025-10-28 有限筛选与必要反侧

作者Curie；BJT [10/27 09:00,10/28 09:00)。原响应仅作复查材料，不自动等于已读。

## 入口与停止

14源首查及可执行恢复均为本日独立请求，URL/UTC检查时刻/错误见各request.json。DeepSeek首查后实际/news/，研究列表10项10/21 OCR→11/01 LPLB、动态09/29→12/01邻接即止；不以主页壳hold。Google原October Blog只读10/27 coach与10/29邻接，原pubs并未被Blog替代。Z.ai原Research后实际page2，18项末尾12/07且没有更多，不拿首15条作末页。Seed最初误用type参数400，保留错误；更正article_type并使用x-tt-locale:US后type1/year2025/count20/token80升序尾段total94/has_more=false，10/22→12/02邻接；type2 token20含10/23→11/27，token40为12月且has_more=false/total45。不是以缺sub_article_list宣称零。

arXiv三个查询均12分类(CL/LG/DC/AI/AR/PL/OS/PF/IR/MA/CV/RO)，submittedDate:[202510241800 TO 202510271800]只是名义周一批次发现线索：model标题transformer/MoE/language model与training/attention/reasoning/optimization；system语言模型与标题inference/kernel/cache/serving/parallel；agent标题agent/multimodal/world model/VLA/diffusion且language/foundation/vision-language或world-model限制。start0/max100，返回56/16/42，去重99，只是提交范围库存。各总数小于100故停止，不翻全年/整类。cs.CL月首页50仅相关标题查漏，2666月库存不是全文队列。官方公告节律说明及历史查询未提供这些ID首公开时刻；DataCite/submitted/API published均不能代替公告。本日不将其列确定候选或评分。

## 已读完整题摘的贡献潜力

以下按当前API精确身份读题摘，v2/v3仅用于定位，不能冒充首版事件；潜力不因主题已有覆盖或小模型关闭。各组均因历史日期未证实而隔离，重开只需官方历史公告/完全落窗bounds，再读对应事件精确版。

- 计算/部署：2510.21956线性attention前后向CUDA；21970 T4四比特减VRAM但dequant变慢，不能只看压缩量；22101大context语义模型部署；23649 LRQK缓存近似定位；22317 kNN LM索引取舍；23652连续层gate与endpoint调优；22467低秩Jacobian/error-feedback；22489任务敏感pruning校准；22556语义分块KV预算搜索；22641 VLM草稿特征投机；23346 block-diagonal LoRA以表达约束免额外TP通信。均可能改变具体质量/资源选择，不因局部实验排除。
- 表示/生成/优化：21986稀疏→密集DiT；22171隐藏/输出不确定性选择；23658 diffusion unpaired preference；22838风格/语义分离；22852 clean encoder/noisy decoder与cache；22926仅被噪声替换token loss；22931非exchangeable CP；22936压缩token保留3D位置；22956长上下文tag定义；23006 ICL知识/上下文作用比较；23095 MHRoPE频率/位置；23254 prior mixture理论；23497文本教师多模态on-policy需SFT冷启；23588 invertible NF+AR像素潜变量；22706实例/几何统一表示；23506情感rationale与预测一致性目标。未把作者抽象数值当性能证实。
- Agent/评价：22571对象状态一致性；22758声学线索understand/reason/generate评价；22443目标推断MC与开放生成差距；22475反事实persona解码；22009端云复杂度升级；22694按query选检索模态；22732经验地图与模拟look-ahead；22775不执行测试的patch reward；22781决策树meta-orchestrator；22898工具泛化stress-test；22967长文claim权重/辩论；23038工具执行judge RL；23258多时间尺度world model+diffusion探索；23272功能/静态/交互视觉reward；23509逻辑约束导航；23691原生键鼠统一动作空间；23595 proposer/solver/judge共演化；23601成功轨迹生成可重用MCP工具。均日期隔离，不给正面Evidence。

## 分层排除

Google10/27 personal health coach原core(google-health.txt 118–194)实际读：时序/对话数据、三个agent与SHARP评价；目前披露为健康应用及既有编排，未给改变通用模型/系统选择的新执行机制或可比边界。不是仅凭标题排除，也不当医疗建议，日名时区未核实后按贡献关闭。OpenAI本窗政策机会文章按明确政策标题关闭，无模型机制。

完整题摘样本：2510.22389医学论文质量评价、22964地理应用综述按暂缓AI for Science关闭；22235原办公室流程排除理由经Peirce R-CGOT纠正，完整题摘明确CGoT与agent携带另一agent的机制潜力，恢复日期隔离，不评分；22763翻译迭代重要性pruning未见超出现有迭代裁剪的机制/条件；22909 offload多目标综述和23587自治等级taxonomy仅分类整理；23477 tutor rubrics、22798手写表达评分SFT/RL应用尚未披露足以修正一般评价/训练判断的混杂或条件。其他明确金属、疾病、基因、城市预测等标题只按领域应用关闭，不称读摘要。潜在negative、安全或含糊标题不在这层关闭。

## 必要安全/反侧core

这些不是本窗已完成候选，而是防止漏掉纠错信号的定点检查。均保留精确v1及日期隔离，不写安全保证；支持/限制足够即停，不遍历全部附录。

- 2510.22014v1：core-transfer §3.1–3.2与§5末干预(395–403)：refusal方向与suffix转移；Llama3.2仅20提示，两种regularizer生成预算不等，小相关及作者judge不证明普遍攻击成功率。
- 2510.22084v1：core-bias §4、§5.1、§6.4(123–145、159起、209–214)。20职业/20属性合取任务，SFT/DPO学习率、样本/目标不同；单fine-tuned Llama3.1-8B、英文Western taxonomy，不能采用“任何DPO无法逻辑组合”普遍断言。
- 2510.22085v1：core-mimicry §3.4.3、评价(182–191、215–235)、§6(473–481)，529训练/200 AdvBench测试、reframing token预算不同；人工主判、自动歧义复核，主要GPT-OSS-20B且跨模型差异，不外推生产风险。
- 2510.22422v1：core-collective 45–54及Discussion90–96，预计算概率policy、W=2、同构population、有限memory；规模效应不能当任意协作agent规律。
- 2510.22620v1：core-backbone §3.2(219–236)，10快照、947用户、194331攻击，强攻击部分未公开、刻意不加外部防御；不证明端到端agent危险率。
- 2510.22768v1：core-persuasion §3.2–3.3(110–118)和评价/标注片段，GPT-4o口头agreement或logit偏好是proxy，不是实际行动；静态persuader控制与作者自评保持有限范围。
- 2510.22535v1：core-offside §4.1(257–267)、§4.3末与Conclusion(746起、764–769)；Qwen2.5-VL 3B/7B、五种unlearning、LoRA/H200；generation遗忘不等classification不可恢复，足球rumor数据只支持局部多模态遗忘反例。未采用输出截断中间细节。
- 2510.22362v1：core-concept §3.4、§4.1(128–142)、§6/Limitations(174–192)：注入CoT与方向投影受mode shift、未表达计算限制；easy/hard是因果作用划分，不是通用题目难度或CoT真实保证。
- 2510.22455v1：core-music §3–4(233–251)，audio/MIDI替换揭示感知瓶颈，CoT/LogicLM收益依模态与schema；不能以符号高分认定原生听觉能力。
- 2510.22993v1：core-icl §3实验128–138及§5(406–410)，四次shuffle，简单技能例不自然实现组合，ExpCoT需技能/步骤对应；未测GPT5或复杂assistant，不普遍否定ICL。
- 2510.22785v1：core-clip §4.1(665–675)、Conclusion(893–899)：多视角/语义一致性测试时防御在CLIP及PGD-10等有限威胁模型；不是任意安全关键部署保证，也不纳入其医学应用支线。
- 2510.23182v1：core-social §4首(148–160)、§4.3(265–269)、Limitations325–330：312人工标注、单人baseline、中文；CoT reply退化与过程分数分账，不能把“超人类社会能力”扩大。
- 2510.23682v1：HTML404后实际web恢复原PDF(另保存chimera-pdf.raw)，§3.1–3.2 pp6–8及§6.3 pp30–31。Guardian验证/clip有限价格和预算规则，不验证全部Agent行为；simulator非市场真值、single seed、Chimera与baseline prompt不同、额外调用3–5倍延迟，不能归因成prompt无关生产安全。仅保留设计潜力与这些反侧，未审所有35页。
- 2510.23074v2 Fast-MIA完整题摘：共享logprob缓存与batch是实现效率，不由加速本身授privacy/copyright判定；无新攻击/安全主张待采用，按局部实现潜力日期隔离，不扩读全代码。
- 2510.22823v1完整题摘：六模型跨语言分类把alignment/scale因果混在不同模型身份；不采用“alignment决定而非scale”的普遍解释，任务为humanitarian领域分类，保持该局部反侧，不当项目长期结论。

## OpenAI单家族必要core

实际web读两篇原Blog及Hub原HTML(openai-card.txt 1–220)，本窗是10/27披露而非10/03release。旧/新模型、专家/自动/线上人口分开。Hub表1 extremism .933→.925，表4 SimpleQA accuracy .46→.44、hallucination .49→.52，保留非单调反侧；新emotional/mental taxonomy是retrospective。Blog专家一致率71–77%与低base-rate估计仍有不确定性。FIRST实际通过后，作者复用有效原证完成受影响安全评价深入收束1家族，Peirce已通过正式受限Evidence变化，采用仅测量身份/人口/非单调比较边界，不授生产伤害率、全面改善或训练因果。必要命题到此为止，不逐读GPT5附件。2026-10-05T07:49:00+08:00同步root及Peirce具体已有覆盖/No Change裁定：Ch66 EvalSpec、测量仪器身份与evidence revision已承载回溯重测边界；历史PRE提案1、最终新差额0、实际写入0，无需POST，仅待DAY本次文字变化回核，非自审完成。

R-CGOT同步：实际从arxiv-system.raw结构化读取2510.22235v1完整题摘。API published原值`2025-10-25T09:39:39Z`只作提交发现线索，不给first-public权。恢复机制潜力后，只待官方历史公告/完全落窗bounds；取得则定点读CGoT方法/对照。旧“无新可迁移执行差额”理由撤销，未以未读方法代排除，不增加正式候选或正面Evidence。
