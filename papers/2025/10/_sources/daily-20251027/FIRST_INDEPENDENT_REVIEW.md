# 2025-10-27 FIRST 独立校准

复核者：Peirce / Codex，非作者Curie；继承当前模型。窗口：`[2025-10-26T09:00:00+08:00,2025-10-27T09:00:00+08:00)`。
fresh实际读取AGENTS、研究合同、来源使用说明/每日组/arXiv主题、Report合同、统一Prompt、ROADMAP及最新10月checkpoint；只加载本日README、CURRENT_STOP、FIRST_CALIBRATION、SCREENING和下述原件。未读08/09或其他日池，未修改作者文件/Books/index/state。

**校准已完成：当前M2小包不满足贡献准入，不能授拟1+2+2=5。日期与版本限定通过，代表排除/潜力保留在下述实读范围通过。不是DAY通过，也不是要求所有附件重跑。**

## 1. M2日期、版本与最小贡献

实际打开[原Blog](https://www.minimax.io/blog/minimax-m2-en-1748600000)L70–125的完整核心、读回本日minimax-m2.raw/txt，并以JSON解析原HTML的NewsArticle：datePublished/dateModified均`2025-10-27T00:00:00.000Z`，即BJT08:00落窗。只授权发布文章事件；前周末测试不证明权重首次公开，不由此倒填首公开或同事件已审。

该core明确算法/认知进展留待后续披露。已实际说明的是产品用途、服务价格/速度、模式和现成部署支持；“新增开放配置供选择”本身未给出改变模型/系统设计的机制或成立边界。价格是服务政策，TPS/倍数未绑定硬件、精度、batch、并发、输入输出/SLO或可比评价条件。这里不是一个已清楚的新机制只缺实验可信度，而是当前准入链尚无可支持的具体增量；不能借成熟MoE、plan-act-verify或通用质量/成本权衡凑分。

实际读本日[官方HF main原card](m2-card.raw)的完整说明/评价口径/部署参数：230B total/10B active、各scaffold/8-run与thinking-history要求均是当前main，不是已锁定的10/27初始artifact；top_k40与原Blog20不一致。现card的激活量与“更小内存/更稳尾延迟”推断也没有控制其他配置的因果证据。它不能补证当窗新授权机制或新的质量/资源边界。没有遍历版本史、部署代码或复现实验；未核图片中所有排行榜数值，因为不作正面性能采用。

**R-M2（普通窄同步）：** 把当前发布文章从拟候选移到原始筛选记录，写明上述具体缺少增量的理由；候选/审阅/Books进度同步为0，不保留5分或把未校准当外部hold。无候选Books No Change是没有可采用命题，不是整书已有覆盖；作者原owner比较可保留为背景，但不能冒称本复核者已验收其全部owner正文。若作者认为另有具体新机制，提交具名原证与精确版本/事件，不必重读全card或找全互联网历史。这是基于已读core的改判，不因深审成本、访问受阻或Books覆盖缩池。

## 2. 查询、日期与代表性排除

实际解析三个原请求URL/Atom，12位范围为`202510231800 TO 202510241800`，start0/max100/ascending；model43、system11、宽agent70。窄agent六分类加foundation/LM条件真实返回19/19；这些是提交线索，不是27公开事件分母，也不是必须逐项关闭112篇的队列。月cs.CL原请求仅skip0/show50查漏，未授2666库存审完。当前summary v2/v3与v1提交日期不提供first-public；可具体隔离，不用名义日程强授日界。

独立从原Atom读完整题摘六份：2510.21425v1（符号整合四维分类）、2510.21890v3（diffusion教材）、2510.21566v2（carrier/store/audit蓝图）、2510.21443v1（requirements模型规模负面比较）、2510.20976v1（MOF模型）、2510.21228v1（急救模拟）。前两归纳材料与蓝图在已读题摘没有明确的新设计证据，按此有限范围关闭，不称历史v1/全文均无价值；MOF按暂缓AI for Science、急救按领域流程/临床指标关闭。requirements比较保留数据集与模型规模的潜在反证，不以小模型/局部结果排除；仍不授首公开归属。

未检查其余全部明确领域项/所有截断题摘，抽样不称全量排除验收。日期缺口是潜力保留，不是零命中。

## 3. 七项必要安全/设计反侧，实际已读范围

本轮实际打开以下七份精确v1原HTML，独立读本日完整abs题摘/版本与必要core；不只接受SCREENING已读标签，不遍历所有PDF/附录。全部仍日期隔离，不计已完成候选Evidence，不给安全效果或Books采用：

- [Self-Jailbreaking](https://arxiv.org/html/2510.20956v1)：§3.2–3.3、§4.1–4.2、§5–6。500 thinking tokens、StrongReject313、GPT-5检测/人工250；s1.1-7B的向量/steering与50条多任务安全训练有具体范围。识别有害不等拒绝；修复后安全输出仍可含self-jailbreaking traces，不能声称现象完全移除。
- [AgentBound](https://arxiv.org/html/2510.21236v1)：§3.1–3.3、§4.3及§5。manifest→runtime scope→Docker执行边界；安装在网络限制施加前，hostname转IP不能等同URL路径授权；manifest仍需人工审，冷启动与steady-state成本分开。设备细粒度控制部分是未来companion设想，不当全权限已实现。
- [Behavior-Aware Sampling](https://arxiv.org/html/2510.21885v1)：§3、§4.1–4.4、§8；T1 refusal/分类多样性，Llama2-7B LoRA、20k Alpaca、L40S与三个自动安全/拒绝评价。abs0.5%与HTML摘要0.05%冲突确实存在，保留核对，不选择有利数字；scorer与单数据规模限制不能抹去。
- [NeuroGenPoisoning](https://arxiv.org/html/2510.21144v1)：§3.1–3.3及相关§4.1设置。white-box推理activation/IG与遗传优化，实验用直接context注入隔离retriever噪声；不是黑盒生产RAG端到端必然攻破，也不是已验证防御。
- [EU-Agent-Bench](https://arxiv.org/html/2510.21524v1)：§2–2.1；60人工prompt增强600、首turn工具参数rubric、七checkpoint/温度0.7/每请求十次；未调用必要tool的trial排除，不能把条件legal-rate当任务端到端合法完成率。只核评价协议，不授法律或合规保证。
- [ColMAD](https://arxiv.org/html/2510.20963v1)：§2.2–2.3、§4.1。竞争说服/伪证反侧、quote验证与合作条件；Bayes judge/有界LLR的理论设定不等任意LLM保证，三任务/温度0/judge选择有效范围保留。未用后续v2替v1结论。
- [Multi-turn Training](https://arxiv.org/html/2510.21339v1)：§3–5。Qwen2.5-3B/GSM8K/55epochs，UACR/ULCR/UADR与基本incorrect反馈；Pass@8和8-turn区分，单turn下降不外推所有闭环Agent或丰富反馈环境。

## 4. 交接边界

本日当前作者稿仍1拟候选/待校准，尚未实际落实R-M2，本复核者不代填。日报V3实跑1份通过，仅格式一致性。FIRST范围不包含十四来源DAY完整复核或最终Books/写后验收；源目录存有真实原件与请求，不把文件存在当实际审完。之后作者同步0候选/处置后，只复查改动并继续尚未验收的有限来源，不重复本节有效七core。

由主任务将本文件转交Curie；当前工具无可寻址Curie入口，未冒称已直接发送。之后fresh推进28，不让M2窄同步阻塞无关日期。无stage/commit/push。
