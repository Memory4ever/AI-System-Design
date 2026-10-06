# 2026-02-13 来源遗漏补查：原件、停止与判断

补查日2026-10-08；用户授权北京2026-02-12自然日（00:00至次日00:00左闭右开）。原09:00至次日09:00窗口、112候选行/日期/评分和连续第4节冻结，以supplement-20261008-baseline.md为原始基线；作者不自授完成。当前合同入口已完整读，LS只作本轮路由，不写共享checkpoint/索引。

## 查询与有限停止

14来源本轮实际范围见README第2节补查表。原件文件nativeA/nativeB/native-metadata/seed-corrected/native-recovery/native-tail/new-recovery/core-final；前者解析的Seed ExternalLinkList为null属于字段读取错误，seed-corrected为实际复发正确请求，不把null解释成无论文。Hunyuan本次返回total=9/list=9，不使用先前运行11作为本次数量。

Seed papers: article_type=1,count=20,publish_year=2026,order_desc=true,page_token=60,locale=us,x-tt-locale=US。实际sub_article_list=19,total=82,next=80,has_more=true，十九具名稿实际日期夹住Feb12，STOP而非全82/全242。仅TwD id1391官方PublishDate1770825600000换算北京Feb12；FLAC1770912000000为Feb13，不读正文。Blog article_type=2,count20,token空，实际14/total19,next空/has_more=false；返回不一致隔离，不能由空next签全19召回。

Qwen retrieval API type=qwen_ai,lang=en-US，只id/title/extra.date，40项实际Feb10→Feb16夹窗，没有Feb12；不读40正文。Hunyuan POST publicList pageNum1/pageSize12/renderType0，只六字段，9/9中GradLoc publicAt在Feb13、下一项Feb3，STOP不读窗外。OpenAI RSS1255条仅Feb元数据定位Spark，不读1255正文；Spark、M2.5、Seedance2与DeepThink有效旧贡献关闭复用，不重复审。

arXiv先误用Feb11–12两个UTC日和optimization等较宽词，start0/max100，model total355首100；意识到范围过宽停止，不分页，不据此授coverage或形成题摘队列。随后改公告可能日对应submittedDate[202602101900 TO 202602111859]，四主题（语言模型/系统/LLM-agent/多模态VLA）各start0/max200，实际total/list分别136/136、13/13、73/73、33/33，首尾metadata与查询URL在arxiv-narrow-titles.json。只标题对原112与旧有效159判别，255含跨主题重复，非255份完整题摘/候选/排除。具体标题才进入完整v1题摘：14项见new-abstracts.json；TwD由官方目标目录另发现。日期恢复new-dates.json中14项Datacite具名原字段，Submitted不视作public。只有10765同北京日上下界成立。

检索与日期复检具体保存queries、specific-date-search、new-recovery、date-search2/3。外部二手结果只发现线索，不用作primary日期/机制。Google错误archive路径及ZAI网页timeout记录保留；Google正确2026/02目录和ZAIHTTP200目标日期段已安全恢复，不把首次失败当终态。

## 具名准入与日期处置

| 线索 | 完整题摘支持的具体差额 | 日期/处置 |
| --- | --- | --- |
| TwD 2602.11731 / Seed1391 | 自然语言/OCR不能保拓扑→关系DSL/虚拟grid/确定性renderer→可检查结构而非像素随机图；2+1+2=5 | 官方Feb12事件，root准入通过；标准必要审阅；Books已有覆盖 |
| Forge中文稿 | 全FIFO尾阻塞/FFFO按完成偏置→限制可消费i..i+W-1，窗口内乱序、头消费才滑动→吞吐与到场分布折中；2+2+2=6 | CN页Feb12、HF原文Feb13、ENFeb14分离；root准入通过；必要受影响深入，Books窄差额PRE/实际POST通过，锁释放 |
| 10765 Collaborative Threshold Watermarking | 独立client signal聚合稀释、单方持完整key→shared方向+threshold shares+SecAgg协作inner product→collective验证权限而非无条件防移除；2+2+2=6 | 日期原件交叉同北京Feb12，root准入/日期通过；Books采用所需受影响深入，Books窄差额PRE/实际POST通过，锁释放 |
| 11212 Elastic Memory | 历史压缩与检索耦合→HiPPO在线固定state+polynomial sampling→独立检索bias选择 | 下界Feb12/created上界Feb13跨日；只日期隔离，完整AB潜在贡献不作EX |
| 11217 Magic Correlations | pretrain排名不等SFT排名→跨阶段accuracy/confidence相关协议→基准和scale下transfer可靠性分验 | createdFeb13，必要日期隔离；不因negative关闭 |
| 11220 RL Rewriting | fixed prompt rewrite分布/多样性失配→QA对齐+diversity reward受hard consistency gate→SFT forgetting取舍 | createdFeb13，必要日期隔离 |
| 11224 Agent-Diff | trace/调用格式不等外界结果→统一API sandbox的state-diff contract→等效行动评价 | createdFeb13，必要日期隔离 |
| 11236 ABot-M0 | actions并非任意denoise对象→Action Manifold直接clean预测→VLA训练目标选择 | createdFeb13，必要日期隔离；不因robot应用标签关闭 |
| 11241 Active Zero | 静态视觉集限制selfplay边界→Searcher/Questioner/Solver主动环境采样→数据前沿反馈选择 | createdFeb13，必要日期隔离；不自动视为组件组合EX |
| 11246 LRH features | linear表示不等linear可读→两种accessibility下容量界差额→probe与feature容量不混用 | createdFeb13，必要日期隔离 |
| 13320 MCP Martingale | 信息失真不能仅假设指数累积→martingale条件集中界→grounding/依赖边界选择 | createdFeb17，必要日期隔离；非因理论/negative关闭 |
| 15897 GHOST | gradient inversion下token身份暴露→语义可分但embedding接近shadow token→privacy/utility边界 | createdFeb19，必要日期隔离；非因局部关闭 |
| 2603.02227 Routing Absorption | learned gate与QKV co-adapt→matched random gate反证+posthoc失效→routing归因分验 | finalID首次公告月March，arxiv事件窗外；不因negative排除 |
| 2604.09560 Diffusion-Attention | attention/diffusion conditional几何关系 | finalID首次公告月April，arxiv事件窗外；不把Feb11提交当公开 |
| 15055 ACP | 身份/SLA/federation目标，但完整AB未形成可识别执行机制/边界差额（空百分比不是主要排除理由） | 贡献关闭root代表校准通过；不展开core |
| 10359 Beyond Calibration CT | 临床固定队列比较与病理分层，无新增通用评估接口或成立条件 | 科学应用范围关闭root代表校准通过；不是因local/negative |

日期隔离9项只保留具体official first-public原件缺口，重开需same-v1公告、作者公开正文/初public事件日；并无普通未读core队列。上述日期跨日不能按created假定后日，也不能按Submitted假定Feb12。March/April只能支持该arxiv事件月，不声明所有平台绝无早版。

10765上下界原件：abs v1 Submitted Feb11 11:51:41UTC；arxiv官方availability L172/175/183：只公告时赋finalID，Tue14–Wed14 EST最早Wed20EST=Feb12 01UTC；DataCite DOI created Feb12 03:01:53UTC说明finalID已存在，上界北京11:01:53，交集北京09:00至11:01:53完全Feb12。Updated Feb12 01:43:48只佐证，不直接public。NoFeb11holiday。date-rules.txt/new-dates.json保留原件。

## 必要证据与STOP

TwD exact-v1 §3.2/3.3/3.4/4.1/4.3/5/Table2/Limitations：sign固量/虚量、VL关系、HBVB聚合与虚拟grid；Render确定IR→图，不认证IR原文真值。Eq5实际以t,s为条件，不将render反馈图本身当已实现自动核验闭环。任务同域bar-algebra监督，composite(chrF+SSIM+judge)非数学answer正确率；teacher/judge同源过滤，numerical consistency仍弱，没有matched移除DSL但保同数据监督的baseline。限bar模型。原图、schema、renderer、parse/structure/answer分验与额外训练/IR/render成本是可采用边界；不授数学exactness和通用闭环。23章663–665完整邻接已经具体覆盖，无需重复Books。支持足够STOP，不读全附录/全部源码。

Forge CN§1/2/3.1–4：W窗口限制rank，不限制policy年龄或等候walltime；最慢head未消耗时窗口仍阻塞，不能称彻底消灭HoL或unbiased sampling。原文全局滑动未给跳过/超时/丢弃恢复协议；工程运行须另约定但不能冒充作者已实现。公开黑盒框架图不隔离windowedFIFO相对FIFO/FFFO的same-budget因果，prefix40倍为另一机制且硬件/预算不够，决不移植成调度收益；CISPO/CM/PD/MTP列出但不另立未审候选。36现1264后有arrival重权/freshness而无bounded消费窗，拟两段有限差额。STOP，不全扫服务代码或所有claims。

10765 exact-v1 §3/4/5/6：共同方向shares相加，per-round global scale使加性保持；≥t可SecAgg计算weighted inner product而不明文合完整key，<t不能从shares恢复key；该crypto权限不证明攻击不能从公开checkpoint估方向或蒸馏移除。当前whitebox honest-but-curious+IID ResNet18三数据集/K4–128/3seeds与naive独立keybaseline；c不同需结合utility frontier，不沿用headline小损失（正文/表accuracy有差异）；distillation明确可移除、强adaptive无理论下界，LLM/非IID/恶意训练未验。两次SecAgg、vector shares/setup与校准成本，拒绝/Unknown及provenance/访问控制回退。72现191/3070–3099无collective验证权限/共享方向差额，拟两段窄补。STOP，未读全部crypto证明与附件。

## 写前比较与独立关口

已在开始Books判断前重读ROADMAP、PROJECT_CONTEXT、LEARNING_PHILOSOPHY、WRITING_GUIDE、LS本轮路由；实读23章645–674，36章1240–1310，72章170–209/3070–3099及必要相邻章节开篇。TwD拟NoChange已有覆盖；Forge→TRAIN-DISTRIBUTED-TRAINING，10765→PLATFORM-SECURITY拟具体差额，已向root发必要证据/PRE请求，未授权不写共享。Source/PRE/POST/DAY全部由root实际独立审，原验收不代替本补查。

上文写前比较保留当时停点，不代当前状态。当前已获root实际3新增准入/必要Source、10765同日日期、TwD具体已有覆盖、9跨日日期隔离/两窗外ID月边界及ACP/CT代表关闭；两项PRE/窄锁后各写2段及自身末注，作者完整邻接已顺读，root实际POST通过、两锁释放。Forge Ch36 1272/1274与1262–1282、末注1846；10765 Ch72 193/195与187–203、末注3226。root实际六部分DAY通过，普通剩余为0；不以真实外部日期缺口冒充待读核心。

准确baseline说明：启动时README scoped status clean；初次读取的大输出在生成快照时带截断占位，该快照已按同一clean HEAD无截断完整恢复（127155字符），没有从HEAD替换dirty报告。当前原112行逐字保留、原§4完整连续保留、原09:00窗口不变均实际比较通过；6主节/14源/115候选及当前1份V3校验通过，限定diff-check通过。README270本地引用实际均存在。10765为了Books采用已在原同版本§3–6/Alg2的threshold/共有scale/inner-product、白盒威胁与攻击反侧范围完成受影响深入，报告标深入完成；这不是新全文附件队列，初始标准审阅之后的owner比较与采用边界深化均已由root实际PRE/POST核。旧46Books证据不重复审；未复现、不写LS/index、无stage/commit/push。root实际DAY已通过，本日结束，不自行接其他日。
