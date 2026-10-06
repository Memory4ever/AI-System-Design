# 2025-10-30 Independent DAY Review

复核者：Mill（非作者；作者Curie）。窗口BJT [2025-10-29 09:00,2025-10-30 09:00)。不替作者更新README，不写共享Books。

结论：通过

两项FIRST与必要Evidence、Ch5实际整合POST及作者窄变化DAY均已通过。下文旧未通过停点仅保留复核过程；以末节2026-10-05T09:00:42+08:00实际回核为准，作者可同步完成态。

## 实际复核范围

复用本次 [FIRST](FIRST_INDEPENDENT_REVIEW.md) 两确定官方披露的日期、完整core、必要控制/失败及Ch5/Ch72/Ch78正文比较；不重读所有实验附件。准入2，深入1、标准1可作最终审阅处置。OWL可仅报告，不授源码验证、攻击覆盖或性能保证。Anthropic仅采用2025 Blog已披露且Revision log未列为新增的诊断命题；2026新增prompt及修正的精确文字仍未采用。

九项必要精确v1实际核完：

- 2510.25791 core-kinetics 184–215/405–428：完整原trace顺序、答案和全序列是不同指标，合成KB/固定GPT2训练局部反侧，不是任意自然CoT因果不忠实证明。
- 2510.25616 core-vla 142–164：八任务固定动作与action-free VLM query分开；t-SNE/attention不授唯一因果、颜色保留不能独立归因机器人数据。
- 2510.24985 core-far 123–128/288–290：operand-selection部署及单FPGA/线性投影/带宽边界；软件FaR对照不授任意LLM或开放威胁端到端收益。未复核72–115攻击细节，不引用未读范围。
- 2510.25179 core-moderation 161–175/595–631/702–704：五集各100有排除人口，四模型名称正文/表格存在7B/8B差异，不需纠正为统一配置；拒答、不遵循和危险completion分账，两次reflection有成本，平均11.1s非SLO。
- 2510.26830 core-smooth 145–169：单预训练通用攻击图、10-pass、LlamaGuard7B；“latest”utility judge不完整，局部噪声选择及audio future work不证明通用防御。
- [2510.25771v1原PDF](https://arxiv.org/pdf/2510.25771v1) §5.3 pp23–24、§7.2.2 pp32–33、§7.3.1 p35：真实web恢复57页，只核这些命题。晚期test-set污染提升部分保留benchmark也损伤生成质量；35样本/四过滤器的排序实验不能归因闭源模型污染；25600/语言trigger和1000新文档仅无害语言切换。未遍历附件，当前first-public未知不正面采用。
- 2510.25117 core-unlearn 941–964：拒答、重训一致性与attack-derived记忆不同；综述安全反侧不当新防御验证，不遍历引用。
- 2510.25595 core-collab 144–180/599–602：每步四候选、30步、12学生、可恢复invalid action；Pass@1结果不包含所有采样成本，不能移为不可逆effect安全。
- 2510.25694 core-enconda 194–206：GPT4.1-mini语义判断与固定commit容器build/test/正常退出分开；诊断正确不是修复可执行，合成错误人口限制外推。

Google PPI原论文core-ppi-paper 94–155实际核KMS/access-policy/rollback-protected budget、每upload重置；TTL best effort不可验证、side channels开放。仅日名相交，论文首公开也未定，不给本窗正面Evidence/Books。StreetReader实际core-street 153–187：11人实验、350panorama、既有Gemini Live上下文功能与失误，不提供新的通用机制或比较条件；贡献关闭保留日期未核，不另请求日期。

## 来源与有限范围

实际读取14源对应request的URL、执行时间、状态、范围；原件仍保存。三Atom实际解析total/returned=27/27、4/4、19/19、唯一46；12分类有具体主题与完整12位日期，无尾页普通待办。首50官方CL相关标题仅补检，不把2666库存转队列。首公开未定仍按ID隔离。

实际核DeepSeek/news10项邻接10/21→11/01；Moonshot26卡09/16→11/06；Z.ai实际page2累计18项至12/07没有更多；Hunyuan官方结构total/list=11/11，目录历史未恢复，作者有限浏览器失败不授成功。Seed实际结构type1 token80 total94/false，含pinned旧项与末尾12月项；type2 token20 total45/true/next40及token40 false，10/22 16Z→11/26 16Z（原日名10/23→11/27）。仅这些目录段身份，不授首次公开。ERNIE实际2页日期10/16→11/07；MiMo实际async中四个2025 Paper日期，最近10/21；MiniMax主Blog10/27→12/23，独立Agent原生md2026/05/13。Google October原月Blog实际10/29→10/30→10/31；DeepMind publications实际11/04最早、page2相同；Meta/Qwen壳只按已记录有限query隔离。各历史缺段不是无事件。

Google pubs普通参数缺口由复核者已定点执行正确category=2025/search=language model：一次20秒curl HTTP000/0bytes超时、一次web不可访问，具体见FIRST。没有响应正文，不制造raw；只需作者将旧year/query误称“正确”的措辞与停点改正。年级pubs不能日级化。

窄恢复记录更新于2026-10-05T07:51:45+08:00：fresh重读本日适用上下文与停点，实际解析本日deepmind-publications.request.json的href，存在 `/research/publications/page/2/`。旧 `?page=2` 返回相同页面不能终结这个可修普通缺口。复核者本日单次正确路径curl max20，实际exit28、20.007s、HTTP000/0bytes，无响应/raw；随后本日单次web [真实page2](https://deepmind.google/research/publications/page/2/)恢复L117–120，10/30 Personhood→09/29。只处理这一日名相交标题即止，不读取余下历年清单。[原Personhood页](https://deepmind.google/research/publications/210560/)完整题摘L119–122实际读，是权责/法律人格治理框架，未建立本项目模型/执行机制贡献，关闭贡献、日期未核不另请求时刻。没有借31响应充当30执行，也不把10/30日名直接判窗外。作者应删除DeepMind目标历史段hold并同步实际窄恢复；Google pubs仍独立受限，不合并。

其余关闭分层样本共7：FIRST的25091金融组合、2511.05533 BIM接口、25817综述，加本次实际Atom完整题摘25223v3 FELA领域feature组合、2512.00020v3 Verilog综述、25760v2 spatial综述和StreetReader官方core。未发现共同理由错误；未对所有普通范围外标题或全部36题摘逐项重复核验，不把抽检称全量验证。全部具名九项安全/设计反侧均核必要core，不由样本豁免。

## 只剩以下窄工作

1. Curie按FIRST将README§1/3/4/5/6与CURRENT_STOP同步：两项最终审阅处置、OWL仅报告、Google查询实际失败/有限历史隔离，DeepMind真实page2与Personhood贡献关闭已恢复；保留Anthropic初版精确prompt未采用的版本边界。
2. root已实际将自述诊断合同两段整合到Ch5，Mill于2026-10-05T08:18:27+08:00实际核正文260/262、233–281前后机制及518末注，并核Ch4/5/6交接，Books POST结论：通过。详见 [FIRST Books POST更新](FIRST_INDEPENDENT_REVIEW.md#books-post更新2026-10-05t0818270800)。实际整合1家族，不归因其他既有脏书稿；末注待root依据本次POST同步，Mill不修改共享Books。
3. 收到以上窄变化后，只复查变化与实际Books正文/衔接、运行V3和限定链接/空白检查，再写DAY通过。未请求重扫14源、重读两官方全文或57页附件。

本窗日期/历史与未采用版本细节终态保留项不用于正面证据、Books、无遗漏或性能/安全保证。日级报告仍进行中。复核者继续31独立fresh，不等整批。

当前非作者精确停点（2026-10-05T08:18:27+08:00）：30两项FIRST/必要Evidence、九反侧、PPI、有限来源与普通可修DeepMind分页均处理完；Ch5两段/邻接/末注实际POST通过。作者README/CURRENT_STOP仍为06:10:22旧停点，未同步两项审阅及实际整合，故DAY未通过仅待作者窄变化复核。未变化证据不重跑。此前四份30/31自写复核Markdown本地引用/围栏/空白检查属于结构检查，不改语义结论。

## 作者窄变化实际POST / DAY（2026-10-05T09:00:42+08:00）

结论：通过

实际通读作者08:50:32 README六部分、CURRENT_STOP及SCREENING变化；两正式家族的7/6分、深入1/标准1、实际Ch5整合1、OWL仅报告/写入0均已准确同步。Google正确category/search的本日有限失败与DeepMind真实page2/Personhood贡献关闭分开记录；无响应不伪造raw，不再保留已可修的DeepMind普通hold。Anthropic后续精确prompt与修正文字仍未采用，日期/历史保留项不授正面证据、Books或无遗漏保证。原FIRST、九必要反侧、PPI及七分层样本未变化，复用有效核验，不重复附件。

实际重读Ch5 250–269前后及512–519末注：两段未发生机制变化，root已将518 Review note同步为Mill08:18:27非写入者POST通过，与正文和原源限定一致。旧末注待同步工作已消除；不归因其他脏书稿diff。

本次实际V3报告检查通过；本日报及本日目录共六份Markdown的本地引用/标题围栏/行尾空白检查无错误，限定git diff --check通过。以上机器检查不替代语义复核。普通研究、Books写入/POST及非作者DAY待办0；仅余作者据此更新状态/§5/§6与CURRENT_STOP、root最终验收，不需再次审相同材料。
