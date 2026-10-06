# 2025-12-17 首批准入校准（作者 Nash）

实际检查：2026-10-02T17:27:41+08:00。固定窗口：2025-12-16T09:00:00+08:00 至 2025-12-17T09:00:00+08:00，含起不含止。

此文件供主线程非作者校准，不是独立复核通过，不是候选分母冻结。以下均为实际打开的原始材料；公开日期字段只有日精度的，不先计确定当窗候选、不补造时刻。作者继续其余来源。

## 贡献拟准入，日期核验仍在执行

| 材料与原始字段 | 已读依据 | 准入推理链 | 预期 owner 与待核验 |
| --- | --- | --- | --- |
| [Towards training-time mitigations for alignment faking in RL](https://alignment.anthropic.com/2025/alignment-faking-mitigations/)，`Dec 16, 2025`，原站未在可见字段给时区/时刻 | 完整摘要；Conclusion；output-only / scratchpad-only 实验说明 | 训练内合规不必外推训练外合规 → 原文以 model organisms 比较 scratchpad monitoring、长度惩罚和 interrogation，并发现 interrogation 可训练出撒谎、反增 compliance gap → 需要把干预目标与最终泛化分开评价，而非只以 alignment-faking rate 判断缓解成功 | TRAIN-RLHF；PLATFORM-EVALUATION-SYSTEM 仅交接。须核首公开/精确原文事件、训练设置及反效应范围 |
| [SAM Audio: Segment Anything in Audio](https://ai.meta.com/research/publications/sam-audio-segment-anything-in-audio/)，`December 16, 2025`，时区/时刻未披露 | 完整 Abstract | 音频分离往往绑定域或单一提示 → flow-matching transformer 统一文本、视觉与时间片段提示，另提供 reference-free judge → 分离接口与评价不能只以固定音源类别/单模态提示定义 | MULTIMODAL-GENERATIVE-PARADIGMS；需精确论文机制、条件模态与评价消融；原始日期不能视作北京时间全天 |
| [Pushing the Frontier of Audiovisual Perception with Large-Scale Multimodal Correspondence Learning](https://ai.meta.com/research/publications/pushing-the-frontier-of-audiovisual-perception-with-large-scale-multimodal-correspondence-learning/)，`December 16, 2025`，时区/时刻未披露 | 完整 Abstract | 独立模态表示的对齐不足 → 统一 audio/video/text 表示与十种 pairwise contrastive objectives，另有 frame-level fine-tuning → 要区分全局检索对齐与细粒度时间定位，不将整体对比学习收益外推帧级能力 | MULTIMODAL-REPRESENTATION；须比较目标组合、caption 数据与规模的替代解释 |
| [Seedance 1.5 pro 发布原文](https://seed.bytedance.com/en/blog/sound-and-vision-all-in-one-take-the-official-release-of-seedance-1-5-pro)，`2025-12-16`，日期无时刻 | 核心技术说明至 Summary and Outlook；Unified Multimodal Joint Generation Architecture | 独立音画流程会破坏时间一致性 → MMDiT 音画联合生成、coherence 数据调度和音画奖励，并组合 distillation/quantization/parallelism → 联合生成是条件建模与数据/奖励共同约束，不能仅解释为后处理拼接 | MULTIMODAL-GENERATIVE-PARADIGMS；目前 blog 只支持所披露架构轮廓；10x 缺可比执行配置，不采用性能保证。待查本窗首次公开及是否已有更早正文 |

评分尚未执行，先请求贡献准入校准；日期尚未确认的条目保留在缺口，不以评分替代落窗证明。

## 代表性负侧

| 材料 | 实际阅读与具体理由 | 日期处理 |
| --- | --- | --- |
| [FrontierScience](https://openai.com/index/frontierscience/)，`December 16, 2025` | 完整题目与核心 benchmark 说明；评价 physics/chemistry/biology 科学研究任务，属于 ROADMAP 明确暂缓的 AI for Science，不能借 Ch66 通用评价 owner 重新引入 | 因贡献范围已明确排除，不为不影响处置的精确时刻另发请求 |
| [Accelerating biological research in the wet lab](https://openai.com/index/accelerating-biological-research-in-the-wet-lab/)，`December 16, 2025` | 完整题目与核心说明；分子克隆 protocol 优化及湿实验科研应用，不是本项目模型或基础设施机制增量，按 AI for Science 暂缓关闭 | 日期未核实，不计当窗零遗漏证明 |
| [GPT-Image-1.5 发布](https://openai.com/index/new-chatgpt-images-is-here/)，`December 16, 2025` | 已读正文产品能力、编辑一致性与 rollout 说明；未披露训练/采样新增机制，4x generation speed 未给可比 workload/hardware/batch/SLO；不能由产品改善数字倒推架构贡献。暂作负侧样本，若安全说明/card 有具体机制变化则只重开该变化 | 时区/时刻未核实；此排除针对当前已读发布说明，不冒称独立 system-card 审阅完成 |

## 发现入口与停点

- 已打开 14 每日来源的固定首入口（Google 的两个入口及 Seed 论文目录均含）；Hunyuan、Z.ai 返回 Timeout，下一步按合同浏览器检查动态目录。其他目录首页不能证明历史窗口已覆盖，相关历史分页/按窗口补检尚在执行。
- arXiv：官方 Advanced Search 已实查 `language model`、`date-from_date=2025-12-15`、`date-to_date=2025-12-16`、`date-date_type=announced_date_first`、`size=200`、`order=-announced_date_first`，响应 `Sorry, your query returned no results`。随后官方 `/search/advanced` 表单明确说明 announcement date 仅支持 year/month 粒度；故本次日级公告查询不作为零命中证据。下一步用原始 submission 线索收窄发现，再核历史列表/真实公开依据。
- 官方 Advanced Search 表单实读文字：`announcement date supports only year and month granularity`。这说明 `announced_date_first` 不能凭当前搜索接口充当精确日窗证明。
- `/list/cs.CL/2512?skip=0&show=2000` 的首轮读取因本机解析库缺失未得到可读列表，不算已检查；继续使用已有运行环境/官方 HTML 恢复，只按日窗相关标题补检，不把全月宽列表变成逐项待办。

下一步：取得本日主题结果与官方历史批次、补齐机构历史界面停止点，完成题摘贡献筛选；对已校准且日期完全落窗的项开展必要原文审阅和具体 Books 对读。
