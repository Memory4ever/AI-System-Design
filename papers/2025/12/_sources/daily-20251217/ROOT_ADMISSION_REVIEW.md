# 12/17 首批准入非作者校准

复核者：主线程（非作者）；2026-10-02。范围：作者 `ADMISSION_CALIBRATION.md` 四项潜在准入与两项普通排除；不是全日验收。

实际独立打开 Anthropic [alignment faking 干预原文](https://alignment.anthropic.com/2025/alignment-faking-mitigations/)、Meta [SAM Audio 完整题摘](https://ai.meta.com/research/publications/sam-audio-segment-anything-in-audio/)、[PE-AV 完整题摘](https://ai.meta.com/research/publications/pushing-the-frontier-of-audiovisual-perception-with-large-scale-multimodal-correspondence-learning/)、Seed [1.5 pro 原文核心架构说明](https://seed.bytedance.com/en/blog/sound-and-vision-all-in-one-take-the-official-release-of-seedance-1-5-pro)，以及 OpenAI [FrontierScience 核心说明](https://openai.com/index/frontierscience/) 和 [Images 发布正文](https://openai.com/index/new-chatgpt-images-is-here/)。

## 校准结果

- Anthropic 潜在准入通过。干预可能降低被监控行为却保留或扩大 compliance gap，不能用单一训练内指标验收泛化。必须保留 model-organism/虚构提示设置、干预步数不同及高运行间方差；不可直接称生产模型都在隐瞒。TRAIN-RLHF 是目标/监督与干预的 owner；评价协议向 Ch66 交接。
- SAM Audio 潜在准入通过。多模态条件统一和 reference-free judge 可改变音频分离接口及评价；摘要不足证明统一框架胜过一切专用模型，正文需检查条件提示消融和 judge 校准。
- PE-AV 潜在准入通过。跨模态整体对齐与 frame-level 目标区分有具体增量；数据合成、目标组合和规模的收益归因必须分别核验，不把十个目标的列举本身视为证明。
- Seedance 潜在准入通过，先收窄到所披露的联合生成链。博客给出模型卡 `2512.13507`，若落窗核验需要机制/实验，必须读精确事件对应模型卡，不停在宣传摘要。博客的 10× 不能作为配置无关加速保证。
- FrontierScience 范围排除通过：当前科学研究任务切片属于 ROADMAP 暂缓范围；不能借通用评价 owner 引入。Images 当前发布正文的机制准入排除通过：产品收益未披露归因方法；只验收此正文，不替独立安全材料作结论。

湿实验负侧未独立重读，其他尚未发现项未验收。上述公开页面均只有日精度，没有凭此确定 12/17 落窗；继续必要时区/公开记录核验，不补造时刻。作者其余发现可以继续，日级覆盖仍未完成。

## 初始正文与 Books 局部核对

主线程实际读取本日初始 README；结构校验通过，只证明六部分与接口一致，不授予日级完成。来源表仍有可执行的扫描，公开时刻未确认项不能记作确定当窗候选。

实际读取 Ch31 开头及 Ch30/32 相邻开头，并定点读取 Ch66 的 `Observed Capability 与 Elicitation Ceiling 必须分开`。Ch66 已解释中性/压力条件、声明监控/无监控配对和 model-organism 的外推限制，因而覆盖评价协议的部分原则；其现有两条来源不是本次 Anthropic 干预实验。Ch31 的 reward proxy 与 reward hacking 也不能替代本次 interrogation、compliance gap、训练内外指标分离的具体增量。因此不得把整项直接判为“已有覆盖”；只有日期与必要实验证据安全关闭后才能决定该增量的 Books 处置。本次尚未改书。

主线程进一步独立阅读 Anthropic 原文 Background/Metrics/Training details、三类干预 Setup/Results、Limitations 与 Methodological Lessons。原文对 interrogation turn 使用 reward 但屏蔽其梯度、各干预训练步数不同、种子方差与模拟设定均有明确边界。作者拟采用的收窄命题与这些位置一致；这次必要源审不补足缺失的公开时刻，也不将研究模拟当生产安全证明。后续若日期成立，只需对拟写段落与原文作用范围定点复核，不重复全篇抓取。

## Seedance Blog 日期与精确 v1 源审

主线程独立 HTTP200 取得精确 Blog 的 `window._ROUTER_DATA`，JSON 解析对应 `ArticleMeta`：ID1817、`PublishDate=1765882058000`、`UpdateTime=1788415475000`，与 [日期 sidecar](../OFFICIAL_EVENT_DATE_RECOVERY.md) 一致。官网所声明的 Blog 发布事件为 `2025-12-16T18:47:38+08:00`，落窗；采用身份必须是这一 Blog 事件，不移作论文或模型全球最早公开。页面存在后来 UpdateTime，当前文字不能无说明当作不可变 2025 快照。

精确 `2512.13507v1` HTML404 后，主线程实际读 [官方 v1 PDF](https://arxiv.org/pdf/2512.13507v1) Abstract/Introduction（pp1–3）、Evaluation §2.1.1–2.1.4 与 §2.2（pp3–8）。文本支持联合双分支生成、混合任务、后训练和多维评价的披露，不支持补造详细 tensor layout、训练损失或跨模态模块实现。评价分别用绝对评分和 GSB；跨完整模型比较不隔离 joint module、数据、RLHF 或加速模块的因果收益。速度倍率不采用；硬件、精度、端到端并发/SLO及重要机制消融未披露处保留 Not Disclosed。当前必要源审支持收窄披露命题，不支持统一模型全面替代或生产加速保证。

主线程已实际定点读 Ch24 开头的生成状态/solver 责任，以及现有 joint AV/motion 段的标题线索；不能据关键词判全部已有覆盖。作者交付具体拟采用差异后，再核唯一 owner 和两侧衔接，不额外堆发布清单。

## 最终定点复核

主线程进一步实际读取 README、SOURCE_STOPS、ADMISSION_ADDITIONS 与 SEEDANCE_BLOG_EVIDENCE。14 个每日源均有有限入口、停止点或明确外部历史缺口；旧裸 kernel 查询已撤销覆盖资格，收窄后的 14/46 条主题结果不冒称当天候选或全量库存。仍缺的个体首次公开不能由提交、月字段或常规公告排期赋给材料。

### 候选与 Books

唯一确认落窗家族是 Seedance 官网 Blog 发布事件。此前实际源审覆盖 exact v1 pp1–8 的架构披露与评价；本次实际读取 Ch24 的 `Any-to-any AR 把 Modality Type 移入同一生成序列` 全段及其后成组数据/共享 prefix 段，并读音画共享运动状态的两个完整段落。

现有论点分别解释 AR 跨任务梯度耦合与共同运动条件，不等于 Seedance 的双分支 diffusion 模块。新披露确实是一条联合架构、mixed-task、coherence 数据及后训练路线，不能整项称已有覆盖。但早期 v1 未说明联合模块的细部、状态布局或机制级受控消融，完整模型比较不能分离这些环节的收益。`仅报告` 处置成立：保留设计路线和未披露边界，不用现有一般一致性原则再增产品清单。若原始模块或归因证据到达，定点重开 Ch24 生成耦合分支。

没有 Books 写入，因而没有尚待执行的写入后复核。Anthropic 干预、Meta 两研究、MiMo release 与仓库修订均保留具体潜在增量，但日期/历史版本同一性尚缺，不用于 Books。

### 安全、纠错与设计反证

除前文实际审过的 Anthropic 必要核心外，本次实际打开以下原文；未将题摘检查冒称所有正文深入审阅。

| 原文 | 核验范围与结论 |
| --- | --- |
| [CTVP v1](https://arxiv.org/abs/2512.13821v1) | 完整题摘：预测 trace 的一致性不等于实际执行真值；理论安全主张须核假设，保留潜在增量，不采通用证明。 |
| [gpu_ext v1](https://arxiv.org/abs/2512.12615v1) | 完整题摘：host/device policy hook 与 verified eBPF 具具体机制；不采用跨租户通用安全或脱离 workload 的倍率。 |
| [Textual Gradients v1](https://arxiv.org/abs/2512.13598v1) | 完整题摘：效果提升不证明 gradient 类比；局部反证不得因不是新算法而排除。 |
| [Effective Depth v1](https://arxiv.org/abs/2512.14064v1) | 完整题摘：Qwen 家族的 effective-depth proxy 不支持所有长 CoT 都缺推理或所有层无效。 |
| [FROC v1](https://arxiv.org/abs/2512.13337v1) | 完整题摘：conformal-style configuration risk 不是任意样本删除影响的实测真值；保留风险控制条件。 |
| [M-GRPO v1](https://arxiv.org/abs/2512.13070v1) | 完整题摘：更多 rollout 只延迟 collapse 的反例，momentum target 与 entropy filtering 分开；不宣称收敛到全局最优。 |
| [RPO v1](https://arxiv.org/abs/2512.13240v1) | 完整题摘：hint-conditioned preference pair 的分布条件仍须核验，不把同 policy family 当无条件 on-policy 等价。 |
| [SPON v1](https://arxiv.org/abs/2512.12744v1) | 完整题摘仅确认稀疏化的表示损失与 trainable spontaneous neurons；当前较晚摘要的 distribution matching 等不冒称历史 v1 披露，日期仍隔离。 |
| [UIFormer v1](https://arxiv.org/abs/2512.13438v1) | 完整题摘：效率/完备性共同约束及 Boolean oracle 缺失是真实设计问题，不凭 token 减少采用正确性保证。 |
| [Janus v1](https://arxiv.org/abs/2512.13525v1) | 完整题摘：attention/expert 分离、通信及 placement 的条件保留，不采用后来 v4 倍率。 |
| [MEP v1](https://arxiv.org/abs/2512.22147v1) | 完整题摘：小程序验证仍需 reintegration 到原 application；不会由大 ID 推断晚公开。 |
| [DTop-p v1](https://arxiv.org/abs/2512.13996v1) | 完整题摘：PI 控制平均 active-expert budget，不等于逐 token 计算量或稳定性自动保证。 |
| [SIGMA v1](https://arxiv.org/html/2512.13488v1) | 实际读 §3.1–3.5、§4.1–4.3：forward、gradient、10 optimizer steps 分开验证；online fault isolation 与 offline rule validation 分开。发现作者记录容易将 Table6 的 Effective Utilization 94.45% 与 Table10 MFU 混读，已要求分别标识；未采用二者为独立机制因果收益。 |
| [Membership inference v1](https://arxiv.org/pdf/2512.13352v1) | 实际读 §IV 生成/排序与结果、§V confirmation/extended subset：ranking 相对 likelihood 的改善有限、某些方法退步；confirmation 差异不能代替 extraction 成功，GT、模型和数据限制保留。 |

Video1.5 的 all_gather backward/SUM reduce_scatter 修订与 MiMo 的 routing replay/MOPD 仍具名保留纠错/反证，前者不按普通维护关闭，后者不授 teacher 全域保持或无泄漏保证；历史正文读文记录可复用，尚无可采日期，不以它们作当窗安全证据。

### 普通负侧抽检

新增实际抽检 [wet-lab 官方原文](https://openai.com/index/accelerating-biological-research-in-the-wet-lab/) 核心问题、实验循环、结果和限制。其机制是生物实验协议改进，本项目暂缓 AI for Science 范围，关闭理由成立；不采生物收益数字或实验操作。结合此前 FrontierScience、Images 的独立核心阅读，共 3 项官方范围/产品负侧经过抽检。

另实际读 [12595v1](https://arxiv.org/pdf/2512.12595v1) §3.1–3.3、§6 的机制、表格及消融说明：noise 检查/重复测量的具体规则与新增操作未披露，受控 protocol 不足，新增机制准入不成立；这是普通可读证据后的关闭，不是日期或数字原因。实际读 [13396v1](https://arxiv.org/abs/2512.13396v1) 完整题摘，现有证据限于推荐 scenario/task 信息流选择，不能直接推基础模型通用机制。这 2 项 arXiv 样本之外的普通领域排除未作全量正文验证。

终态保留项、原始入口失败与重开条件按本日 README/ADMISSION/SOURCE_STOPS 保留；不支持正面证据、Books 或无遗漏断言。普通作者读文待办 0，具体指标混淆纠正已实际落实；进入完成态结构检查。

结论：通过
