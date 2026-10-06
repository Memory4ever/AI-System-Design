# 13 日必要精确版本反侧恢复

作者：sept12_15_author；本轮独立加载13日当前规则、窗口及停点后执行。只定点读取独立校准指定的11风险信号与10439理论，不把60发现潜力转成全文队列。以下链接均精确v1 HTML；实际工具原记录为`necessary-core-web-1.json`至`necessary-core-web-6.json`，记录打开URL与正文行号。未取得完全落窗首次公开依据，以下仍是日期保留的必要风险核验，不计本窗正式候选或评分，不进入Books；不声称复现、代码核验或保证有效。

| 精确身份与原证据位置 | 读到的机制、反侧与停止理由 |
| --- | --- |
| [2509.09893v1](https://arxiv.org/html/2509.09893v1)，§4.1～4.2、§5设置/基线、§6 | 人工在waypoint标球形precision boundary，采样pose并由convergence waypoint直线运动、倒放记录后接原示范。collision-free依赖人工范围、机器人几何和物体可见；不是任意全body/contact安全。§6明确不处理contact-rich，目标不可见则失败；MILES对照去掉原contact sensing，不能把差额全部归因算法。风险边界足够，停止无关附件。 |
| [2509.09942v1](https://arxiv.org/html/2509.09942v1)，§3.4、§4.5～4.6/Table1～2 | S-GRPO奖励为编译、regex/static vulnerability pattern与think格式的0.3/0.5/0.2组合；不是已验证不存在漏洞。作者主动指出VulRate排除未编译输出，小模型低VulRate可能仅因编译失败；FullRate才同时约束功能、安全与可编译。8×H800、rollout8、五epoch及greedy评价仅作者条件，不授未知漏洞或生产保证。 |
| [2509.09955v1](https://arxiv.org/html/2509.09955v1)，§V-B、§VII-D、结尾 | 每层similarity threshold以BO搜索accuracy/FLOPs/token通信Pareto；隐私未纳入三个优化目标，仅用inversion reconstruction SSIM说明局部粗化趋势。低SSIM不是DP、语义身份不可识别或所有攻击者保证；formal隐私目标列未来工作。无须为了否定安全保证遍历所有BO推导。 |
| [2509.09970v1](https://arxiv.org/html/2509.09970v1)，§III、§IV-C/D、§V/TableIII | QEMU/虚拟RTOS执行fuzz-patch loop并记录timing、错误文本；§V明确当前是input injection与log扫描，coverage instrumentation未来。VRR92.4%、SCI/TMCS不能视为所有缺陷关闭或硬件实测WCET；物理板未来。本文的实际验证边界与较强安全宣传并存，保留反侧。 |
| [2509.10018v1](https://arxiv.org/html/2509.10018v1)，§3.1、§4.3/Table3 | NER与agent融合识别实体，private privacy box保存实体/placeholders双向映射，匿名问题出private space；语义上下文仍可能泄漏，映射箱本身是敏感资产。ARX三攻击类别测试≤0.21%是作者局部报告，不是完整自由文本LLM重识别威胁模型或DP。不由QA改善推隐私保证。 |
| [2509.10260v1](https://arxiv.org/html/2509.10260v1)，§3.1、§A.4/A.5 | consistency reward由小pretrained LLM判断CoT/最终标签一致性并门控分层标签reward；hard-positive手部样例upsample防止“有手即异常”的shortcut。主张可作具体reward/数据混杂风险，judge一致性不证明CoT忠实或reward hacking全面消除；两极少标签未进入bucket策略，保留采样边界。 |
| [2509.10278v1](https://arxiv.org/html/2509.10278v1)，§3.1/3.2及结论 | OSTF2238测试图、FantasyID1572图，通用VLM与专用SIDA/FakeShield使用不同default/detailed prompts及patch/resize协议；专用模型跨到文本篡改失败是局部检测迁移反侧。不能授KYC生产安全，也不能把模型排名差额单纯归因architecture，真实ID分布/新编辑类型未验。 |
| [2509.10298v1](https://arxiv.org/html/2509.10298v1)，§3.1～3.3、Table1/2、§5 | 正文将drop概率p的期望(1-p)ℓ+p错误写成1-p+pℓ；κ=.7下p(12)=.3却例示约.099。Table1 local Lipschitz均值/最大高于baseline；§5承认global bound未正式验证。由此不授certified robustness，也不把reported FLOPs降幅当机制因果；保留正文争议，不以日期隔离掩盖风险。 |
| [2509.14256v1](https://arxiv.org/html/2509.14256v1)，§3.2/3.3/Table1 | MPNet只用response，DeBERTa用query+response，均512token截断；Webis Native Ads 2024 held-out数据，response-only F1.511/precision.977/recall.346而另一配置F1.773。输入信息、epoch和backbone共同变，不证明某架构优越或平台全体暗广告可检测；只保留评价条件盲区。 |
| [2509.10594v1](https://arxiv.org/html/2509.10594v1)，§2.3～3.2 | 所读安全段和四pillar提供治理/oversight概念框架，没有可执行攻击-防御威胁模型或formal保证。不是普通忽略安全信号，正文检查后限定为概念性风险陈述；不宣称新防护已实现，也不据此给新增Books控制。日期潜力池保持，独立审计可决定是否具体贡献不足关闭。 |
| [2509.10401v1](https://arxiv.org/html/2509.10401v1)，§3、§4/Table1～3 | 单推理pass中LLM生成abduction、minimal action和后续3～5轮counterfactual，不实际重跑被干预agent环境。Who&When126+58样本、gpt-oss-120b同baseline、step numbering移除导致大跌；此confound提示结构锚本身承载收益。模型想象成功不建立SCM可识别因果或真实干预有效性；25%token/time overhead仅原条件。 |
| [2509.10439v1](https://arxiv.org/html/2509.10439v1)，§3.1～3.2/Theorem3.3 | 适用可微convex/L-smooth、unbiased bounded-variance oracle、各node i.i.d.同分布；inner η和outer γ联合满足ηL(1+max(γ−1,0)H)≤1/4。收敛上界区分optimization、noise和local drift，γ≤1可允许较大inner step；不自动外推nonconvex异构LLM训练、momentum稳定或通信实测加速。理论采用命题所需假设/结论已够，停止不相关证明附件。 |

以上12项保留其发现潜力但收窄安全/理论/因果权限。原文已读不等于归属日期已核；定点重开条件仍为官方announcement或作者原公开正文完全落窗依据，随后才核贡献、评分与Books。正式CAISI单项按已独立校准的6分/Ch72已有覆盖处理，当前仍待非作者DAY。
