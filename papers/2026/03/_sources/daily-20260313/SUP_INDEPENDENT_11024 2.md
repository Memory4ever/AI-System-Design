# 2603.11024v1：解释资格必要Source与具体NC独核

仅03-13既有Daily补Mar12自然日；复核者 mar13_admission_review，准备者root。恢复实际重读AGENTS/current Research/Report/Prompt、Sources使用/Daily/arXiv范围、ROADMAP及本日停点；大输出截断的Report/Sources段另行恢复，不把未见输出算读过。日期与此前完整题摘准入有效复用，本项不重开旧新版或跨日，不写共享Book/Report/State/mainledger。

## 身份与实际阅读

实际读[准备包](./SUP_ROOT_SOURCE_11024.md)、[完整精确v1题摘/history](./SUP_ABS3_11024.txt)、[精确官方原响应](./SUP_ROOT_CORE_11024.raw)，以及`SUP_ROOT_FIVE_MANIFEST_RESULT.json`对应记录：`https://arxiv.org/html/2603.11024v1` GET200/158063B/2026-10-10T04:21:07.091767Z。题名Does AI See like Art Historians? Interpreting How Vision Language Models Recognize Artistic Style、九作者对应；Comments12pages/12figures，无所见撤回/纠错/具名先稿。history存在后v2/v3，不据版本号自行重审或继承其机制进Mar12。

实际原件范围完整§3/Table1人口、§4.1–4.4/Table2/Eq1–3、§5.1–5.3、§6.1–6.3两个人审及直接反侧、§7；相关figure只读正文/caption，不认证所有像素或曲线精点。现文实际顺读Ch5 33–45、180–206、270–313及309–317具体“信息存在/可读/使用”完整段；Ch66已有EvalSpec/人工锚点资格交接复用10990本轮已读121–148，不另立机制owner。

## 原证裁决与采用资格

- **实际增量**：概念能预测模型输出并不自动取得人类语义解释身份→继承Semi-NMF，用艺术/建筑有限输入概念对末prompt token hidden作缩放增减、匹配10等范数随机方向，再单独评价专家coherence与作品/风格relevance→必须把可读、局部输出使用和专家认可分开。原先按艺术领域词排除会漏掉此解释资格；本次不借Semi-NMF、稀疏分解成熟原理给新增分。
- **人口与提取**：§3两个WikiArt人口各2500图/5styles，Architecture1500图/5styles，每图4×4 patches；§4在指定层对输出风格首token相关residual做Semi-NMF，V≥0、L1/列范数约束与threshold选择。probe预测的是模型响应style，而非独立真值，模型常猜相同style会使probe更易；.95 raw/.85 binary不能单独证明可靠解释。§5.1的ground-truth style本身与专家共识不一致，不把WikiArt标签等同唯一人类真值。
- **干预边界**：§4.3选择当前top3 activated concepts，在末prompt token hidden加减αaᵢvᵢ，α包含负boost与正suppress，匹配10均匀随机同范数方向。Eq2/3测的只是style首token logit/logprob，不是完整风格名称联合概率或重新生成分类成功；没有实证tokenizer冲突就只说该测量不认证完整名称。匹配随机支持局部方向差异，不证明唯一circuit、自然语义身份或完整任务正确性。§5.3 mean1.14styles logit下降、拟合R².96、correlation slopes只能按该受限对象保留。
- **patch/full反侧**：§4.4直接将patch字典用于full输入出现non-sparse、近乎全激活和不连贯；作者提出分开full/patch decomposition、二值化/OR聚合/共现P(patch|full)。这是明确输入域失配，不授任意视觉输入可迁移；本次不采用新的full→patch可执行接口，故无需扩实现/附录。
- **人审真实分母**：第一研究六位本团队专家、128concept分两批、每concept三人看24高激活patch，majority≥3者93/128=73%，Krippendorff α=.52。这是专家coherence而非所有概念客观semantic truth。第二五专家/50预选case，每style7正确3错误，**最多两个activated concepts、其余nonactivated随机控制**，非每case固定两top。正文报告80个selected concepts中5不reflected、8对model-prediction不relevant（10%）；不把90%读为模型90%正确解释或全自然人口表现。正文§6.2.1的model/user对应Fig11b/a，与caption标a/b相反，精确panel-target映射不认证；保留正文有限人数/分母/观察，不靠未视觉图补断言。
- **解释与成本**：§6.3形式/明暗对比解释是作者与专家可能原因，不证明模型独特心理或唯一内部语义；Realism/Romanticism混叠与局部details偏置保留。分解、层/阈值扫描、干预强度与额外随机forward、专家标注都付费；必要段未披露完整hardware/precision/墙钟/运行SLO，不补造生产总成本或免人工保证。

## 评分与具体已有覆盖

**受限Source通过；2+1+2=5通过。** D2为这篇具体控制/专家反侧支持的解释有效性条件，R1为单表示诊断组件，Durability2为可读/当前使用/人类解释资格的稳定区分；不借成熟算法、可联想到的全平台或无实现费用抬分，亦不因NC改变准入或减少已完成必要审阅。

**具体NC/Books0通过，只限本次采用命题。** 唯一owner `WORLDVIEW-REPRESENTATION` [Ch5](../../../../../books/part-01-worldview/05-what-neural-networks-learn.md)：当前40段明确activation可预测标签只是可读、受控下游改变才开始支持使用；Superposition段明确probe/patching/sparse decomposition只观察投影、不能升为完整因果；“从可读出到机制”阶梯及其上下文明确correlation→decodability→localized intervention→downstream change→跨context/model复验、局部效果非完整机制；概念注入段保存随机概念/注入时机、输入复述与干预损伤控制，不让生成解释自己签正确性；后续“信息存在、可读与被使用”又要求外部target、fresh probe与行为验收，并分output scores和最终选择。这里真实承载本次解释权限，不是因主题或paper名称相似判已有覆盖。

艺术域的93/128、80个概念与完整实验数字没有被现章吸收，本次不声称已写新验证。full→patch接口及强解释因果未采用，不将其假装由泛NC承载。Ch66仅拥有人口/专家judge资格交接，不夺机制owner。本项无需PRE/POST或Books修改；支持与关键反侧足够即停，只有未来拟采用新mapping/跨域自然解释时才定点重开相应机制与consumer。

本文件不授正式Report同步、实际Book验收或DAY，不stage/commit/push。
