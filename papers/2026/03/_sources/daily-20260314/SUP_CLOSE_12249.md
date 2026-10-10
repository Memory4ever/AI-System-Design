# 12249 SciMDR：局部数据构造接口最低关闭提案

mar14_supplement；只03-14补充Mar13 BJT。完整精确v1题摘/六作者及metadata题名差异保留；SUP_INDEPENDENT_NARROW.md非准备者决定core窄P与root实际§4决定段复核有效复用，不因Science标题排除，也不把Science领域任务收益重新引入当前路线。SUP_INDEPENDENT_DATE_NARROW.md实际10/10日期包赋本ID Mar13 arXiv日级归属，后v2不证明重要修订，不全版本diff。没有已知具名早公开正文信号。

## 实际最低必要增量

官方exact-v1 https://arxiv.org/html/2603.12249v1 GET200/353166bytes/2026-10-10T01:31:36.135265Z，SUP_NARROW_CORE_MANIFEST_RESULT.json与SUP_NECESSARY_12249.raw/txt。作者本次直读§4.1–4.3/B94–104、§5.1/B111–119与完整Table3/B120–129、§5.4–5.6/完整Table5–7/B143–164、§6/B165–166；identity与具体judge来源§3.2/B70–71，必要A1截取B224–229。范围足够结束最低实际delta，不读全部Science benchmark/图pixel/所有prompt示例/代码/附件。曾取175–229混入引用段，不将引用浏览作必要Source已核声明。

确实的接口是：先标原文figure-reference，只给text抽claim；再给visual由同generator核是否有visual correlate并分TQA/MQA，VQA另由图生成。Claim先有结论，backward生成问题/rationale；每QA绑定claim的text/visual位置，再用Section/Table等identifier填模板，prepend Information Localization至reasoning。最终fullDoc+question监督localization+reasoning+answer。它比只是给现成QA换上下文多一个显式定位标注recipe，准入保留，不撤P/改EX。

但programmatic保证仅是**模板与存储identifier转写确定**，不是claim真、完整evidence map、定位因果正确或reasoning忠实的验证约束；视觉核验仍同生成器，answer先给的rationale不能反证shortcut。新增可复查的是这份局部标注/监督组织方案，不是新的grounding verifier、跨来源执行协议、重要权限/安全约束或完整因果保证。300K/20K、领域专家benchmark/Scientificassistant能力不是本项目评分命题；成熟provenance绑定/CoT/同源重标原则也不另算新机制。

Table5 same-source SPIQA重标50K/twoepochs控制来源与条数，CharXiv和SPIQA-A改善但ChartQA25.5<原SPIQA26.3，不能由同source证明全部tokens/teacher/rationale量及定位的唯一因果；五倍长answer不是五倍reasoning深度。§5.5去localization49.1→22.8与去reasoning16.9支持本受测训练recipe的有效性，但改变监督内容/长度，没有单独评价真实定位groundtruth或匹配alltokens预算。原文误指Table7而实际ablationTable6，不合并为新实验。§5.6原base32.9oracle/19.8standard/12.8fullPaper是输入暴露改变、最多8图/6段vs全稿，不能唯一归噪声或所有长context支持正确。

实际主要Qwen2.5-VL7B分VQA/TQA一epoch再MQA一epoch、LM训练/vision/projector冻结，SPIQA oneepoch不能当等总supervision预算；16K最大输入含图文、最多8图512²。50K比较LLaVA1.5-7B全组件训，与上述freeze不同，不混为同model机制。judgeGPT5mini/训练generatorGPT5.1、humanbenchmark标注不是独立faithfulness或所有真值证明。hardware/precision、完整teacher/OCR/rollout费用与serving并发SLO未在最低必要段披露，Not Disclosed，不造降本。Table3 SPIQA-C47.3<base48.9保留，不采用全slice无损。

## 分数与关闭理由（待非准备者实际独核）

**Design1+Reach1+Durability2=4；已关闭/仅报告提案，Books新写0。** 1是实际局部claim绑定与定位模板监督配置，非“没有贡献”；1是当前数据构造/适配组件而非跨系统授权或新执行机制；2是具体支持集/局部标注与fullDoc重新定位的稳定取舍价值，不给借用通用原则和Science任务分数加分。必要身份/日期、core准入与以上局部delta/反侧已够本分数最低关闭，不扩所有科学题目及附件，不因费用/访问/已有书篇而缩池。

不作NC“新实验已吸收”或整合请求，不需owner写锁/PRE/POST；原局部recipe收益保留，不为达到4分要求普遍定理或更多匹配实验。待root非准备者必要原证/评分与范围裁决后才能正式同步；本项不授DAY、实现或复现。
