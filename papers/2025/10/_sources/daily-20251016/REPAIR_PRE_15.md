# 第十五包：代码依赖路由、生成式合同与有限填空评价

整体PRE/具体NC，未SAVE。Books上下文/ROADMAP及Ch77/79交接本轮actual有效；Ch78 Tool Contract完整接口/说明、符号引擎路由/函数复用两段、compile反馈/ATF与执行模拟器完整两段、callee摘要/跨文件slice、主动perception完整接口/两说明段及真实payload引用完整段均实际读。不重R6/R54/R56有效必要，不核代码/复现。两I唯一AGENT-TOOL-CALLING Ch78；一NC唯一PLATFORM-EVALUATION-SYSTEM Ch66，不复制跨owner机制。

## 12186 iCodeReviewer / 2+2+2=6

消费R6与原有效III-A–E/IV/V必要/独核§9；只采用known/unknown符号、dependency读写路由及上下文回收接口，不采soundness/线上acceptance安全率或38experts名目。Ch78现有LLM-Symbolic分解/类型→solver与callee摘要展开未承担**按当前符号/依赖状态决定分析读取与回写**。唯一插位在完整LLM-Symbolic路由段/inline SF2510-06774后、完整`描述已可见、甚至得到较高attention...`前；完整Tool Contract与路由上段、工具选择/函数复用下段已读。

正文：

仓库分析的路由还可读取“这个符号当前已知什么”，而不只匹配工具描述：维护identifier及其dependency状态，对known与unknown符号分别取得所需上下文、分配分析，把工具读取与返回的依赖写回同一状态，再回收本步不再需要的上下文。[受限代码审阅分支](https://arxiv.org/html/2510.12186v1)让分析对象、工具读写和可见context成为显式接口，而不是用专家数量证明覆盖。符号解析、repo revision、依赖/摘要来源与分析结果必须绑定；缓存里已知仍可能是错的或陈旧的，回收文字也不删除代码事实，不能由路由成功保证soundness。应分别验依赖支持、真实调用/回写、审阅结论与最终patch/原任务，缺少独立路由消融时不把全部改善归于该接口。索引/解析、全部分析/重试、状态维护和独立软件回归均付费；符号身份、上下文或结果不可信时，保完整source、静态保守分析/原小工具链与人工复核，不由更少context或缓存命中批准无漏审和安全acceptance。

独立marker：`<!-- source-family:SF-2025-ARXIV-2510-12186 -->`

本人末注：

- `SF-2025-ARXIV-2510-12186` — Herschel，Daily2025-10-16补Oct15；消费Cicero R6及本日III-A–E/IV/V/独核§9有效必要，2+2+2=6，仅known/unknown symbol及dependency读写路由/context回收差额深入。保38experts非覆盖证明、缺独立routing消融/全部费用，不授soundness/线上acceptance安全。未第二Methods/代码/复现；整体PRE/SAVE/fullselfread/solePOST仅本日canonical实际层。

## 12702 NL2Contract / 2+2+2=6

writer §3–5必要与R54 key已成。现ATF是形式statement编译/保义，outcome monitor消费预先声明合同，未承担**从NL/signature/context提出可执行pre/post wrapper并将其自身列为待验证artifact**。插完整ATF段/inline SF2510-06857之后、完整`反馈前移还可以依赖模型学习的执行模拟器...`前；原compile临时单元三说明段/ATF与后执行模拟器完整两段均读，不拆旧source-family。

正文：

需要运行前后检查时，合同本身也可先由模型提出：读取自然语言需求、函数signature与必要context，生成precondition检查和postcondition断言，再包装真实调用。[受限合同生成分支](https://arxiv.org/html/2510.12702v1#S3)把“代码是否满足候选条件”与“条件是否忠实且充分表达需求”分成两层；生成器不能同时签发后者。有限时限的符号搜索未找到counterexample、甚至返回Unknown，不是全状态soundness证明，mutation检出也不覆盖任意错误实现。原需求/实现、候选pre/post、搜索状态/超时与独立reference须共同保存，区分不必要地拒绝合法输入、漏掉错误输出和真正发现bug；reference/真precondition只在评价可用时不能搬作部署oracle。模型生成、wrapper执行、符号/随机测试、修订与独立语义审查全付费，部分post-only对照仍可更好；条件不可信、搜索不完备或调用高风险时，保人工合同、真实tests/独立review与原executor权限，不由没有反例、较多mutant被杀或可运行断言批准需求正确和软件安全。

独立marker：`<!-- source-family:SF-2025-ARXIV-2510-12702 -->`

本人末注：

- `SF-2025-ARXIV-2510-12702` — Herschel，Daily2025-10-16补Oct15；exact-v1 §3–5必要与Cicero R54 key，2+2+2=6，仅NL/signature/context→pre/post wrapper及合同自身验收差额深入。保CrossHair60s含Unknown非证明、mutant非全错误人口、14/19与14/31分母、Pynguin600s/post-only反侧及全费，不授soundness/通用安全。未核实现/复现；整体PRE/SAVE/fullselfread/solePOST仅本日canonical实际层。

## 12720 Omni-Detective/Cloze / 2+2+2=6 / Ch66具体NC提案

writer S3/5/6/A1/B1/D/E必要、R56 key有效。只采用caption→cloze的测量支持域与逐claim真实性分责；detective只读可错observer报告不等真实AV全观察，max10轮/55K–15K训练、2340video/70200cloze/30blank构题、500pairs/sevenmodels Elo相关.91非逐claim证书。wrong而非NotGiven的指标不穷尽未列虚构，teacher/训练/评价同pipeline、轮数5–6趋平与全部工具/造数/训练/人审费保留，不授无限自纠或全caption幻觉认证。

actual Ch66 SF2507-06523完整问题图/双向忠实度段明确独立问题会漏错误绑定、需原片支持、precision不补未列事实、问答器/claim图可能同错；随后VERHallu完整两段SF2601-10010分别保存event存在、方向、None/Unknown及条件分母，不以高accuracy和输入attention授真实支持。上方benchmark生成器完整链/两说明段（本轮已实际读/R66复核有效）另保存generator/filter/answerability/排除人口，具体承担本次有限cloze题目与真值的测量边界。这里只评价owner，不声称书内图问答就是本文caption→cloze算法；Ch78主动perception完整接口只交接报告provenance，不再写一份机制。拟NC，无书段/marker/注；若reader发现本次还有未被承载的新长期命题只重该差额。

请sole reader整体PRE两完整正文/marker/本人注及一具体NC，未SAVE/不预POST或日级，无全章锁/root第三批准。
