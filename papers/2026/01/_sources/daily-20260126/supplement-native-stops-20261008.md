# Jan26 补充来源：实际停止与权限

执行：2026-10-08 北京时间；补充窗口：2026-01-25 ～ 2026-01-25。原09:00窗口保留，但不是本轮日期筛选边界。只检查每日14入口；不检查每周组、2025、其他日或年度论文库存。原报告快照：`supplement-original-20261008.md`。

原生返回保存于 `supplement-n1/n2/n3-20261008.txt`；定点恢复与日期字段保存于 `supplement-native-final-20261008.txt`。完整题摘保存于 `supplement-abstracts-20261008.txt`、`supplement-abs-cli-20261008.txt`。辅助搜索只提供发现，不证明首公开或零发布。

| 来源 | 本轮实际范围与停止 | 有限结果与限制 |
| --- | --- | --- |
| SRC-OPENAI | Research 当前页；RSS fresh GET 403 后复用已保留原 RSS Jan20～29 切片（jan26_openai_rss.txt） | 原切片 Jan23 Codex→Jan26 Indeed 跨过Jan25，没有本日条目；Indeed 原事件不移动。当前403不称新的零发布证明。 |
| SRC-ANTHROPIC | Research Publications首屏10项Sep～Oct2026；Jan25+model定点检索第一页，无恢复历史目录 | 本日历史切片仍缺；停止。 |
| SRC-GOOGLE-AI | DeepMind Research和fresh RSS100项，最早Nov10,2025，Jan20～29仅GenieJan29；Google pubs年份字段394项仅定位；Jan25+model第一页补检 | 仅RSS日段可判断未见Jan25；pubs缺日级公开日期，不审394库存。 |
| SRC-META-AI | Research空返回；复用原官方publications page3混排边界，仅该页Feb27→Feb10→Jan2 | 不把mixed排序当完整窗口。SOAR表外作者页另行处理，不以其补齐Meta全源。 |
| SRC-QWEN | github.io停Sep2025；fresh精确同ID官方article API | extra.date Jan26与正文datePublished Jan23仍冲突，不任选字段；Jan25原blog文字不能消除冲突。 |
| SRC-DEEPSEEK | 当前首页模型卡片；复用本日原news/API-docs有限失败与日期查询 | 当日历史目录缺段，当前模型名不是当日新事件。 |
| SRC-MOONSHOT | PlatformBlog全部26项到Nov7,2025；原CLI0.87精确事件与有效关闭复用 | 0.87 Jan25公开，机制判断不变；模型/blog切片仍不完整。0.88不扩窗。 |
| SRC-TENCENT-HUNYUAN | Research文本仍空；本日已有两次浏览器尝试及org回退失败原件有效复用 | 缺“全部”历史目录；不重复无界恢复，不授零事件。 |
| SRC-ZAI | 文本入口超时后直接GET恢复15个日期条目到Dec2025，Feb2→Jan19→Jan13 | 原生日期列表跨过Jan25未见条目；不扩More的更旧年库存。 |
| SRC-BYTEDANCE-SEED | public_papers page1/13、20/242只定位；root提供精确官方API入口后本轮独立GET `publish_year=2026&order_desc=false&page_token=0&count=30`，type1 papers / type2 blog | type1 Status0，returned20、total82、next20、has_more true；只用前三日段Jan20→Jan22→Jan27，越过本窗后停止，不请求next20。type2 returned9、total23、next20、has_more true，首项Feb12已过本窗，停止。只声明该排序API日段未见Jan25，不把库存当候选或普遍无遗漏。 |
| SRC-BAIDU-ERNIE | web超时后直接GET完整第一页10条，May9→Jan29→Jan15→Jan8→Nov21,2025；分页下一2/2 | 已过本窗下界，不读page2；该列表未见Jan25。 |
| SRC-XIAOMI-MIMO | Paper8项到May2025，Feb3与Jan8邻接；Blog15无日期、More，当前首页读完 | Paper可读日期切片未见Jan25；Blog历史日期/More限制保留。 |
| SRC-MINIMAX | EnglishBlog12项日期Aug→Oct2025，Jan27 M2-her→Dec23 M2.1跨窗；中文重定向页与Agent15行shell | English可读日段未见Jan25；中文/Agent缺历史可读日段。 |
| SRC-ARXIV | availability官方规则＋AdvancedSearch官方说明（公告仅年月精度）；cs.CL/cs.DC Jan2026 list各首25请求cache miss后停止；四条Jan25模型主题查询，只抽具体相关题名回原稿 | BJT Jan25没有常规公告批次；不把Jan25 submitted buffer当public。LLM42、TensorLens、Structure三项潜力成立但未恢复官方公告日/作者早公开，日期终态隔离；MaskedDepth与LiMo完整题摘经独立校准贡献关闭，不为其无关日期再查。未扫整类、整月或catchup。 |

## 有界主题与补检停止

四条发现查询各只处理返回第一页相关线索，原返回见themes；关键词辅助身份，不决定贡献：

1. `"January 25, 2026" ("language model" OR Transformer OR "model training") research`
2. `"2026-01-25" ("multimodal" OR "world model" OR VLA) paper`
3. `"Jan 25, 2026" ("LLM" OR GPU OR inference OR kernel)`
4. `"January 25, 2026" ("agent" OR reinforcement OR memory) model research`

精确身份查询只处理SOAR、StepDeepResearch、EfficientAgents、LanguageVAE、MDPI96；原返回见target/remaining-identities。MDPI原HTML429、直接GET403、xml失败、PDF403后停止；缺完整题摘/精确公开日与必要对照，不能继承三方Jan25为确定候选。SOAR同作者 `soar` repo404、主站path=soar bounded Jan27前commits[]、root目录不含该路径；只是该恢复位置失败，不证明未公开或没有贡献。LLM42 org repo现可读，created_at Oct23,2025仅注册字段，不作为正文首公开。最后四条指定ID/作者页日期检索未恢复原生日级日期；伪装arXiv的第三方镜像与不相关全作者列表未采用、未扩大池。

原来6家族只复用必要身份/有效结论：4贡献关闭、2必要条件隔离，0原确定候选；本轮新相关线索不是由提交库存或宽目录自动生成的逐项全文队列。新条目具体处置在报告和后续校准记录中维护。

## 完整题摘与贡献校准

本轮新相关家族10：8个完整题摘（SOAR、LLM42、TensorLens、Structure、MaskedDepth、LiMo、EfficientAgents、LanguageVAE），1个官方核心（StepDeepResearch），1个只有原源局部段落（MDPI96）。不是宽列表或搜索全部命中的审阅分母。root 独立实际校准六项潜力及具名代表排除；只对已清楚的潜力恢复必要日期，不按负面结果、小模型或成熟部件标签排除。

- LLM42 / arXiv:2601.17768v1：dynamic batching改变floating-point归约顺序，fixed-shape verify/rollback绕开非确定性而复用高效kernel；改变reproducibility与吞吐取舍，潜力成立。公开日期缺失；repo created_at仅注册，不能授public。
- TensorLens / arXiv:2601.17958v1：把attention、FFN activation、normalization与residual整个block写为条件化linear operator/tensor；潜在改变贡献定位的完整边界，不因“线性组合”关闭。公开日期缺失，停止必要恢复。
- Structure / arXiv:2601.17869v1：受控语言变换区分结构学习与组合使用；负面证据可能修正reasoning机制解释，潜力成立，不能因小实验关闭。公开日期缺失。
- MaskedDepth / arXiv:2601.17895v1：完整题摘仅把传感缺失视为mask，配合成熟depth-completion/data-curation及latent对齐声称；没有提出改变基础模型/跨模态设计判断的新成立条件。贡献关闭，日期未核不再查。
- LiMo / arXiv:2601.17815v1：完整题摘为geometric planner生成demo与规模/多样性navigation消融，仍是领域配方，未给可迁移的新成立/失效边界。贡献关闭，非因小模型。
- EfficientAgents / arXiv:2601.14192：完整题摘的组件、Pareto和指标综述没有指出新评价盲点、混杂或修正重要机制判断的反证；贡献关闭，不为日期无关问题扩查。
- StepDeepResearch：官方repo News已给Dec24,2025技术报告可读事件；Jan25第三方推荐不改变首公开。仅确认事件身份，留真实早日，不继承已审。
- LanguageVAE / arXiv:2506.19418v1：完整题摘及官方AAAI稿身份支持已有2025论文，Jan25poster/talk不是首次正文；没有重要修订信号，不比完整版本史。
- MDPI Algorithms19(2)96：具名题目为Instruction-Tuned Decoder-Only LLMs for Efficient Extreme Summarization on Consumer GPUs；局部原源说明不能代替完整摘要。HTML429/GET403/XML失败/PDF403有限恢复已停；完整题摘、原生公开日及必要核心不可得，终态隔离，不评分也不以访问失败贡献关闭。
- SOAR：作者页原生January25,2026支持blog事件；arXiv2601.18778v1 submittedJan26只支持另一个提交事件。HTML exact-v1正文出现August24,2026，隔离其Jan25版本权限；因此只定点核PDF首页、§3.2/3.3、Table4/5与B.8/9。PDF首页January27,2026，核心teacher reward=student在hard reward set的实际进步，与作者blog一致；不把后版blog/HTML数值投射Jan25。root独立必要源/PRE实际通过，采用作者Jan25机制事件、后来PDF只核精确机制，不声称Jan25已公开PDF实验；2+2+3=7深入，Ch27窄锁两段/自身末注已写，root actual POST通过，窄锁释放，root完整六部分与本记录DAY通过；依其要求补齐训练/评价条件及NotDisclosed边界后完成。
