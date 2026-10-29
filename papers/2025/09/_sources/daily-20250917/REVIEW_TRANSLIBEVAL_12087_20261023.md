# TransLibEval12087必要首包：拟五分/唯一Ch66具体NC

Lovelace；作者162明确L独占→212实际接受。177/136既成AB/day/current复用。仅首次必要域，包成后交作者一次不同角色必要采用，不selfsign正式家族。

## 命题与停止点

本次拟采用命题：library-free代码翻译人口不能认证第三方库迁移；目标API/参数语义与可执行行为须在相合目标环境分验，编译成功、逐test/整suite通过及人工判断“有用库”不是同一对象；IR与检索均有条件失败，不能按一个总体榜替换原Direct/原实现。

核心方法是构造三语言对应任务/测试、六种translation输入、四类不同判据；直接对照为同任务Direct与IR/检索、原library-free人口的不同边界；成本/反侧包括人工构造/译测、检索与额外生成、筛掉难对齐样本、假API/错平台/抽象遗漏及有限测试。上述证据已足够限定命题并作具体owner判断，**不再扩查非必要图像素、21页失败报告、全prompts、repo或可选实现**；未核这些不是普通缺层/外阻，不冒实现或复现。

## 原件与实际读取

`REVIEW_SOURCE_12087V1_20261023.raw/.headers/.request.json`单次200/exit0/619901B/3.295316s，SHA256 `6c762cd4f362e82220c657bd433f92f434f57a39354d55c83b544083ad6c8407`。观察Oct23 17:15:01–05UTC，BJT已Oct24，不变研究窗/文件名。

actual S3–8、E1–4/T2–6、正文直接对照与F1–5caption；此为已发生读取范围，不作为后续5–6分全表配额。原v1主标题与AB早已使用TransLibEval的命名层不回填后来新内容。未图像素/21页独立失败报告/代码、完整prompts、实际compiler/库安装/测试或LLM调用复现。未核图中的精数/全模型策略排序不作我们的正面采用；正文作者报告与已读表可按其有限角色保留，无新必要请求。

## 方法、人口与四类测量

53Python库每库4method=212人工任务，每个一个class/一个method、primitive入参出参、无comments；两工程师制备/核300personhours，五人分语言译代码和tests、仲裁200hours，排除12个难以达成一致/库差异大的任务，最后200平行样本。它是人为可对齐方法级人口，非完整repo/任意对象类型或全部实际依赖；排最难项不能外推无对应API的任务。

Direct→直接译；三IR分别先CoT/pseudocode/summary再生成；RA(method)先生成query、RA(name)用方法名+target语言，再取StackOverflow top1post/top3answers。检索/IR均改变可见内容、生成与调用预算，不是相同总费单变量；票数高/命名相似不授目标API语义/正确性。

CSR是全部program的compile比例，PR按全部tests加权，CA按program整suite全过，LDA是人审import及调用能否提供所需功能。PR/CA权重不同，CA某处高PR不自动代数错误。有限tests同source/counterpart的参考也不证明所有输入行为等价；LDA不认证参数/schema、编译/执行或真实效果全过。

7模型六方向/六策略，temperature0/n1但仍可能随机；只C++→Python Direct子集三重复的有限变动不能认证所有策略/方向稳定。表3商用模型参数/MoE/RoPE条目仅本文描述，未作厂商证实，不采用架构或规模因果。精确API checkpoint/依赖与编译器版本、全预算/环境未齐，不补稳定deployment身份或今天服务行为。

## 局部支持与关键反侧

T4 Direct全模型均CSR55.09/CA32.19/PR36.82；Python→C++36.14/16.14/14.97，Python→Java36.21/13.50/19.57，C++→Python84.64/60.50/69.63，Java→Python74.29/48.29/55.64。方向差只这份构造/模型人口，不能把另library-freebenchmark的41.63/61.03/54.49下降直接归全部TPL单一因果；任务、tests与API难度共同变。GPT4o平均75.42/42.67/48.27高本集部分模型，但不同训练/接口/未知参数不证明“大/商用总更好”或架构原因。

S5.2的RA(name)错把服务端handle_request检到Android例、IR抽象漏实现细节支持需验target语境的反侧；Figure3未像素核，不采其全部策略精确排序/通用最佳。T5的LDA直接提供交叉反例：C++→Python Direct57.14而RA(method)33.33，Java→Python Direct71.43而RA(method)38.10/IR(CoT)47.62，IR(summary)76.19；Python→C++ RA(name)47.62高Direct38.10，但都非全功能保证。C++→Java Direct66.67高IR(pseudo)47.62/RA(name)38.10。新方法不是统一替代Direct，也不由LDA提升授同一比例CA提升。

LDA人工756按模型/方向/策略分层、两labeler/四评估者κ.71/70hours，只其二值判据支持。95%/5%样本设计不授每小stratum独立充分/全 population无偏。GPT4o失败分类4831case/360hours、token/statement粒度可一program多类；A类79.58%等是所给错误标签人口，不是79.58%所有翻译/所有模型真实事故率，细分类均非独立因果。正文后称Direct/CoT各1600–1700及其它策略count与4831如何归并未闭，不擅拼新的总数；T6全已读数字不为此补code。API错用/源语言API残留、参数类型/返回值、syntax/不完整生成与runtime均保类别，静态不报不等运行安全。

DataAvailability明确dataset/code准备中，不把论文里的repo引用当可运行artifact；可选代码未核不阻塞本限定观察。mutation/self-refresh是计划，不授实际data-leakage-free或全原训练未见。未执行库安装/原失败case/脚本，不采已复现或生产可靠。

## 评分、具体owner与全费

拟 **2+1+2=5 / 唯一PLATFORM-EVALUATION-SYSTEM Ch66 / 具体NC Book0**：新增只是受限库迁移评价盲区/方向与策略取舍，成熟翻译/IR/RAG或库名不加分，不因现书覆盖撤P。

actual当前Ch66完整815–829已有跨语言**语法/可执行实现/算法分验、真实目标语言和库版本独立测试**，TransFuzz具体将API触发context与oracle关系/目标前提分开，不让相似API或迁移器自签语义；782–790保test与requirement/revision/环境及missingcoverage，已有800–805完整功能/结构分母有效层复用。它们具体承载本命题，不只是code主题相同。Ch76代码dependencyclosure/真实重跑只交接，不双owner。

本文未验证新的可靠库语义映射/targetoracle生成或依赖控制机制需替换该链，故拟NC；局部新负例/正例留报告，强模型/策略因果不由旧书替证。保原代码/reference、目标版本独立tests、较窄Direct/人工库映射、未知时不通过，不为所有translation任务造统一自动方案。

构造/翻译/review共500personhours、人工LDA70/错误分类360hours是不同任务费用，不随意相加成每次runtime；所有retrieval/query、IR与最终生成、失败编译/执行、测试等价核验、人工标签和独立功能回归全计费。硬件/precision、各API输入输出预算、网络与检索状态、concurrency/fulltail/净费未披不补；模型默认项/较高CA不是SLO或免费reliability。

有限重开只相合目标库/类型/异常语义的新受控映射，独立oracle或相同目标manifest和总预算下改变设计选择的证据；图像素/长失败附件未核本身不触发重开，更不作为普通待办。本包只交作者一次必要采用，未正式自签、不写Book。
