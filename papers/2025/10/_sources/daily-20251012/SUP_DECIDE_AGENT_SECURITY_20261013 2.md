# Oct12 四最低门与必要安全反侧

作者Kierkegaard。只FOURTH四最低N和CommandSans已具名安全claim，不扩24全文。原件链接/精确v1如下；所有方法读取不执行代码、工具或payload，不授日门/评分/Books。root本日[独核§11](SUP_INDEPENDENT_20261013.md)已actual五v1完整必要节点/表及redteam通过：四最低2P2C，FOURTH9P3C无N。下文作者提案保留原读域，不再待最低核。

## 09567 lakehouse：作者N→具体C

[v1 HTML](SUP_CORE_2510.09567_20261013.raw)200/exit0，实际完整§III/TableI、IV-A/B与V。存在真实执行/权限，而非纯状态术语：API-mediated I/O/RBAC、隔离无网FaaS/包白名单、transactional run/data branch、去merge-main权及owner提供`Branch→bool`核输出后merge。原“proof”自身说明不是formalproperties，而是业务输出predicate；只NumPy2/pandas2错包修复prototype，全面实验与massive parallelism明确未做。

原证呈这些成熟隔离/branch/tests/人工merge的应用组合，未引入新验证规则或受控一般失效条件，故贡献C，不因框架名/无Books差额/实验少关闭。必要反侧保留：通过业务predicate不能证明任意code/依赖safe或无silentbugs；凭RBAC/key、禁止agentmerge及平台无网等条件才有该隔离范围，不以“no disruption”单样例签所有生产数据安全。没有将宣称Snowflake/dbt不支持agentrepair视为实际匹配比较。

## 09093 web exfiltration：作者N→窄P

[v1 HTML](SUP_CORE_2510.09093_20261013.raw)200/exit0，实际§III/IV、VI-A–D/VII；首次联合输出VI-B少量截断后单独完整补读VI-B/A。真实sink由HTTP端捕获预置secret，外部恶意网页通过同web工具触发RAG私有读取再外部请求；测试强制投喂攻击页，绕SEO，只有base model安全、没有额外guard。本文不复述可执行模板/不发请求。

窄P不以已有2023payload本身算新：**扰动会降低payload可读/可解码性，总体ASR可下降而成功绝对数增，不能把低ASR当安全层改进**。原VI-B指出binary无法解码、改变文本语义/指令清晰度会降低成功；12converter与base分母不同，top20 best模板选择不是平均真实攻击人口。该测量/consumer反侧可修正对防御评估的解释，非新通用攻法。

不采用“reliably exfiltrate”/供应商或scale因果结论：未与真实SEO、不同ACL/工具能力/更多防御层匹配；secret/GET捕获与token/output判断分责，分母/预算不统一，极低成功可来自模型无法理解攻击而非policy可靠。当前v2只2026修订角色，不替v1。没有真实公司数据或实际攻击执行。

## 09781 AuraGen/Safiron：作者N→窄P及必要安全限制

[v1 HTML](SUP_CORE_2510.09781_20261013.raw)200/exit28，277702/预期365707bytes部分body；实际完整§2/4、§6.1/6.2及完整Tables1–2、§7/AppA/AppD。联合§4输出截断后单独完整补读；原§4在§5前闭合、AppD在E前显式闭合，未用partial尾/完整附件。

原算法为formatadapter＋SFT/GRPO风险分类。P不是成熟GRPO/数据规模：

- **评价人口的层层选择与目标差异**：AppD所谓Harmful Detection Precision实际Eq2分母是真实harmful集合H、即该子集检出率而非PPV；Risk Cat Eq3只已检出的Hdet，Explanation Eq4只category正确的Hrisk并由LLMjudge判。不能把三个条件率当全trajectory正确或真实安全。奖励不含explanationquality，category改善只是共变，不证faithful rationale。
- **同model训练/过滤操作点不一**：Table1 Classifier对Baseline总体.939→.951、riskcategory.556→.602/exp.488→.537，但harm检出.918→.915；Table2 SFT→GRPO overall.956→.949而harm.939→.973，多个consumer不能同用“all更好”。Threshold AVG/ALL筛选可丢有用样本，非单纯curation越严越安全；hard-only/比例配方反侧见§6.1，不用规模不足删潜力。
- §6.1写easy:hard从1:1到1:3却称稀释hard，比例与文字方向不一致；不替作者倒序或作可执行recipe，不由此删上述测量潜力。
- trajectory按§2是**尚未执行的计划序列**。AppA每系统50harmful/50harmless由两human修改并crossvalidate，测试risk labels/adapter格式，不是实际不可逆动作执行或真实生产伤害率。adapterGPT4omini stylejudge与end-to-end安全也不同，>90%不能外推allagent安全。

只采用这些可迁移过滤/训练/测量资格，未签基础guardrail生产可靠/解释faithful。预防不可逆动作仍须真实execution授权与监控证据，不把所有强claim提升为已核。

## 10049 ALLOY：作者N→具体C

[v1 HTML](SUP_CORE_2510.10049_20261013.raw)200/exit0，实际§3.4.1–3.4.3与完整§7.1–7.2。DOM日志/metadata→三agent context/action/synthesizer JSON DAG；Identifier用semanticplaceholder替literal，第二agent填新intent；template转Python函数，Playwright-MCP agents共享SQLiteSession、Kahn层级并发与lastnode结果。存在真实pipeline，不称没有工程。

原读域仍是成熟PBD/LLMgen/placeholder/taskDAG执行组合，未有新binding/校验/执行可靠性规则或受控一般条件；原12人用户偏好/易用性结果不单授foundation系统增量，故C。限制明确只有线性示例、conditions/loops/errorrecovery未来；§3描述prompt含precondition不等runtime enforce，共享session并发不证状态隔离。DOM trace可含credentials/private内容，隐私redaction只future，未采用隐私/安全保证；不因HCI或web限定自动关闭。

四门作者提案2P2C，FOURTH拟9P3C无N，待rootactual；不回写成已过。

## 08829 CommandSans：已P必要安全反侧

[v1 HTML](SUP_CORE_2510.08829_20261013.raw)200/exit0，实际完整§2/4.1–4.3、§5.1/Table1–5与§5.2/Table6、AppA7必要说明。只信任user、攻击者控制tooldata不含训练/directprompt；tokenlabel区分human-directed与AI-directedinstruction，BFCL/OpenOrca GPT4注释/每run人工100不是全真值。encoder不followinginstruction不等无adversarialtagging；CS*新增5431恶意synthetic并augmentation0→20%，不同于原只benign训练CS。

Table1 Claude无attack utility88.66→84.54，Gemini79.38→68.04（CS）/74.23（CS*）；attack下Gemini64.59→63.12/59.01，并非all无utility损。BIPIA CodeQA恶意code残留且synthetic CS*可退，SEP BERT/ROUGE/ExactMatch只是内容相似proxy；ASB ASR†由是否移除注入字符串估计，**不是攻击目标实际执行**，IRR也非unsafe行为率。不同benchmark不能合并为普遍安全。

人类redteam白盒代码/目标和逐token反馈但weights隐藏；只单恶意email/固定userquery/两目标。tokenizer扰动与third-party compliance semanticreframing实际绕过，CS*是事后针对训练不能证明所有未来adaptive attack；原“1% (1/360)”口径不自行改成统一率。Table6/human挑战与AgentDojo不同population。保持token级sanitization潜力，仅这些必要限制通过前提，不授contextagnostic/无需校准/无utility损或所有tooldata安全。
