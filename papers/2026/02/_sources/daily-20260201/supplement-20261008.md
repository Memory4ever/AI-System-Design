# 2026-02-01 增量来源补查

作者：supplement_20260201。执行：2026-10-08T12:08:00+08:00。只补现存本日；补充窗口为 **2026-01-31 ～ 2026-01-31**（北京时间自然日，只判断日期）。原窗口、原0候选及原§4连续内容冻结；原稿保存在 [baseline](./baseline-before-supplement-20261008.md)。旧有效 Source/Books 复用，不启动 Weekly/其他日期，不 stage/commit/push。

## 1. 有限来源与停止

以下按每日清单顺序执行。当前网页不是历史快照，空响应不作阴性证据；新增读取与旧证据共同限定本日的可支持范围。未把全目录转为逐项关闭队列。

| 来源 | 实际查询与停止 | 结果与限制 |
| --- | --- | --- |
| SRC-OPENAI | RSS Jan28～Feb3邻接段，当前XML经直接请求解析，止于Jan29→Feb1跨窗；[新日期段](./supplement-openai-rss-slice-20261008.txt) | Jan31没有RSS显示项；原8案例是Feb1，原处置/归属冻结而不移动。RSS不证明全渠道完整历史。 |
| SRC-ANTHROPIC | 当前Research打开；复用原官方HTML publishedOn邻接Jan29UTC→Feb5元数据与finite_lists_final | Jan31没有已见相关事件；当前首屏不补授完整历史目录。 |
| SRC-GOOGLE-AI | DeepMind page4实际Jan/Feb片段；Research当前按年入口；一次限定Jan31模型/训练/推理查询，止于结果页 | Project Genie Jan29是窗前边界；Research历史日期切片仍缺，搜索空不是无遗漏。 |
| SRC-META-AI | 官方Research空响应；复用原relevance第3页限制；一次Jan31研究日期查询 | 无新可确认本窗事件；GRASP定点官方作者项目页无日期，另列保留。 |
| SRC-QWEN | Blog动态空响应；Jan31/January31/Jan31限定官方站一次查询 | 保留原动态历史切片缺口，不把空页/搜索空签作0发布。 |
| SRC-DEEPSEEK | 官方news研究索引实际Jan28 OCR2→Feb25 DualPath，过窗停止 | 无所见Jan31事件；不外推全部仓库历史。 |
| SRC-MOONSHOT | Platform Blog实际26项最晚2025；定点当前K2.5原文；Jan31官方域名补检 | PARL正文仍无事件日期；旧Jan29模板更新不替博客日期。 |
| SRC-TENCENT-HUNYUAN | 官方Research超时；复用原浏览器/前端API恢复路线，再POST publicList page1/1000/renderType0，code0 total9/return9，止于日期标题字段 | [当前有限字段](./supplement-hunyuan-api-20261008.json)最早publicAt Feb3；display与public分离。不证明1月历史从未存在。 |
| SRC-ZAI | Research实际Jan19 Flash→Feb2 GLM-OCR，过窗停止；原release-note有限切片复用 | 无所见Jan31条目；release历史缺段仍保留。 |
| SRC-BYTEDANCE-SEED | 官方论文目录→升序接口article_type1/year2026/count100/order_descfalse；实际20/total82,next20,has_moretrue，相关Jan29→Jan31 A²D→Feb2 SPARKLING已读，过窗停止；原type2 Blog9/23限制复用 | [当前API原件](./supplement-seed-api-20261008.json)A²D PublishDate Jan31解除整天交叠障碍；UpdateTime不作公开时间。没有读next20或给全目录零遗漏保证。 |
| SRC-BAIDU-ERNIE | 中文Blog第1页实际Jan29→Feb6，跨窗停止 | 没有已见Jan31条目；不扩第2页题摘。 |
| SRC-XIAOMI-MIMO | 官网打开；原Paper Jan8→Feb3邻接复用；一次Jan31限定查询 | Blog缺日期切片，Paper不替Blog背书；搜索空不证明0。 |
| SRC-MINIMAX | 中英文Blog当前打开，中文Jan28→Feb12邻接实际可见；原英文Jan27→Feb12及Agent列表复用 | 中英日期不统一；Agent当前列表访问失败不抹去原有效May13记录，也不证明完整历史。 |
| SRC-ARXIV | 官方availability重读；4组Jan31主线主题查询（模型/多模态/系统/Agent），二月首25 CL/DC/RO标题页各一次均失败；只把查询返回的4个相关/含糊条目作题摘查漏 | Jan31BJT无常规公告；Submitted日期不授公开。标题页失败保留，4组结果不是全学科召回。 |

当前原件按执行序为 supplement-official-0/1/2/3、supplement-finite-gaps、supplement-arxiv-themes、supplement-date-recovery、supplement-four-hits（均20261008后缀）；旧依据只复用 SOURCE_RECORD 所指定本轮证据，而不采用旧inventory/Weekly池。每周未扫描；GRASP作者页只作明确材料日期恢复，不扫描作者全站。

## 2. 首批准入校准与新线索

A²D官方Seed API ID1523/ArticleID1776927992143，PublishDate=1769788800000，表示Jan31官方显示日期；UpdateTime=1781527022000分别保留。arXiv Submitted不作为日期来源。root实际读取API与完整题摘/§2.2–2.3后确认可作待核增量（非预授Books）。

| 线索 | 完整题摘/核心后的判断 | 处置 |
| --- | --- | --- |
| A²D / 2602.00759v1 | outcome-only探索低信息→proxy评价训练decomposer、条件hint探索与无hint内化→重新考虑训练信号来源及脚手架依赖 | 确定新增1家族；2+1+2=5，标准最低投入，实际因具体owner差额/目标式不一致定点深入。 |
| HyperOffload / 2602.00748 | runtime局部offload→IR显式cache操作与图依赖传输调度→编译期远端内存路径有潜在机制 | abs与有限题名日期搜索只有Submitted；没有Jan31官方先行公开证据，日期保留不评分。当前v2不作本窗精确版本采用。 |
| GRASP / 2602.00475 | 串行rollout与不稳state梯度→lifted virtual-state/噪声/stop-state-gradient→长horizon规划计算取舍有潜在机制 | 官方作者项目页有核心但无事件日期，有限查到后期PMLR而非Jan31公开；日期保留不评分，不读全文队列。 |
| NetWorld / 2602.00558 | shared latent/two-hot/inverse dynamics与现成classifier-guided diffusion/MF在无线三任务组合，只报领域指标/扩展性，未识别到改变基础模型/LLM系统设计的独立机制或受控失效边界 | root实际完整题摘校准后贡献前关闭，不因cs.NI标签关闭；不需日期请求或全文投入。 |
| Hope Speech / 2602.00613 | 在希望言论检测场景用RoBERTa/XLM-R并报告F1/accuracy，未提出架构/训练或系统合同变化 | 贡献前关闭；不因Transformer关键词准入，不额外追日期。 |

## 3. A²D必要证据、反侧与STOP

精确[HTML v1](https://arxiv.org/html/2602.00759v1)与当前abs仅v1无撤回标记。已实际读§2.2–2.3、§3.1/Table1、§3.3/Table2–3与guidance反侧、App7格式条件及App8/Alg1；不遍历无关引用/附件。原件为 supplement-a2d-primary/core/ablation-algorithm-20261008.json。

decomposer与proxy来自相同backbone，质量reward是proxy多次尝试至少一正确，乘格式reward后用GRPO训练；该reward衡量给定proxy下的可解性，不认证每个子问题正确。冻结得到的子问题离线标注训练集。reasoner先作无hint rollout；平均正确率低于k1时另采带hint解答，仅保留有限正例，再在不含子问题的question+diversity-prompt条件下训练，常规RLVR与辅助IDL并存。部署无hint需要独立评价，不是所有hint生成自动内化。

§3.1训练prompt上限2048、response6144、batch128/minibatch32、32 rollouts、temperature/top_p均1；四个3–8B模型、八个数学benchmark，作者称重复评价8次报均值，不能称8独立训练seed。Table1提供GRPO64对照并未显示完整decomposer/proxy/hint预算匹配；无完整hardware/precision/wall-clock/concurrency/SLO/evaluator实现披露（Not Disclosed，SLO不属于本文优化对象）。不采用免费探索、同总成本或生产收益断言。

Table2去guidance-removal/selection/diversity会退化，§3.3.3持续将hint塞入训练与测试可能依赖提示；这支持有限协议下“探索条件与学习条件分开”的局部判断，不认证内部因果。Table1 Qwen2.5-7B OMATH-H由GRPO2.9降到A²D1.8，Table3 REINFORCE++ MATH500由73.6降72.7，不能称每任务普胜。

Eq3/5称NLL但正文是π而无log；App8第31行只引用Eq5，没有给独立log定义或修复，也未明确无正例时分母/空集处置。该精确数学配方隔离，不照抄、不自行加log纠正文献。正文可采用条件采样/正例筛选/去hint接口事实；可执行exact objective须作者勘误/精确实现才定点重开。非必要artifact缺失不阻止上述有限文字机制审阅。必要机制、评价与直接反侧已足够，STOP。

## 4. Books差额与独立层级

已读Books所需项目上下文、学习/写作合同及ROADMAP owner；Ch33实际POPE/PrefixRL段已拥有人工/外部prefix仅conditioning、suffix更新、guided→unguided部署与预算边界，scaffold段已有注入退火。尚未拥有proxy训练独立decomposer，再对低无hint成功率题作guided-positive/no-guidance辅助训练的责任分离。root实际精确v1必要源与Ch33邻接核查后Source/owner PRE通过，授权Ch33唯一两段＋自身末注窄锁。实际两段已写Ch33 L415/417及源注L3078（行号为写后核查时），作者顺读完整L405–429邻接与自身末注；[PRE拟文](./supplement-owner-pre-20261008.md)保留写前判断，实际正文按root意见中文化并固定proxy Qwen2.5-7B身份。未碰Ch32/34或公共文件。root非作者实际POST通过、窄锁释放；六部分DAY也由root非作者实际通过，范围见§5，不由作者自授。

## 5. 精确停点

有界发现已停止，NetWorld/Hope Speech两项贡献前关闭（root实际完整题摘校准），HyperOffload/GRASP两项必要日期保留；确定新增1 A²D必要源与owner PRE通过、实际两段写入完成。root非作者实际独读新415/417两段、405–433完整邻接与自身末注，POST通过，窄锁释放；Report六部分差额已合并，root已实际逐项检查六部分/14源有限停止与限制/全部新增1必要精确v1/两潜在日期保留/两完整题摘关闭，DAY通过。普通待办0，本日结束。13新JSON合法、11日报本地引用0缺失、原窗口/原0候选/原§4连续字节保留、完成态V3与限定cached/unstaged diff-check通过，不替代独立语义验收。外部日期/历史切片限制不伪造0命中；后续仅据新必要原件定点重开身份，不扩下一日。未改index/state/公共合同，不stage/commit/push。
