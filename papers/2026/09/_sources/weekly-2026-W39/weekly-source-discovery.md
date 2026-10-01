# 2026-W39 每周来源有界发现

**窗口：** 2026-09-20T09:00:00+08:00 ～ 2026-09-27T09:00:00+08:00（含起点、不含终点）

**实际检查：** 2026-09-27T09:11:42+08:00 ～ 2026-09-27T09:37:26+08:00

**范围：** 来源注册表的 29 个每周来源；未扫描每日组、按需组或历年论文正文。
**性质：** 原始发现、日期核验和前分母贡献裁决；不是正式 Weekly、冻结候选分母、独立审阅或 Books 完成声明。后续只按本记录的具名线索继续，不启动全年目录全文队列。

执行前完整读取 AGENTS、CODEX_RESEARCH_PROMPT、RESEARCH_CONTRACT、RESEARCH_SOURCES、REPORT_CONTRACTS、ROADMAP，并查看 LEARNING_STATE 中周窗相关检查点。此文件是本执行单元唯一写入；未 stage、commit、push。09/21～27 Daily 的复用、未完成 Daily 的处置和 Books 由主执行单元负责，本发现任务没有借用旧 Complete 标签证明周窗闭环。

## 1. 查询与停止规则

官方博客先读当前目录，只打开可能相交本窗的题目及必要核心说明。已明确窗外的文章不投入证据审阅；完整 HTML 暴露历史列表并不意味着逐篇阅读历史正文。日级目录日期没有时区时，保留原字段；不能将本次抓取时刻改成公开时刻。

GitHub 发布列表统一查询 `https://api.github.com/repos/<owner>/<repo>/releases?per_page=100&page=1`，对整页记录按 `published_at` 判断窗口，而非在第一个旧 tag 处停止。NCCL 首项为 09/17 的 C++ release，但后续 nccl4py release 在窗内，正说明不能只看首页首项。精确 tag 通过 `/git/ref/tags/<tag>` 解析；annotated tag 再跟随 object 得到 commit。仅为少数核心主张打开相关 PR body，不遍历普通 PR。

下表中的“100+next”表示实际处理第一页 100 个发布后，在远早于窗起点的历史段停止；没有声称读取全部页。GitHub 的返回顺序、历史 draft 后发布、未标 release 的 RFC/研究等均使这种查询不能证明互联网上绝无遗漏。短列表没有 `Link rel=next` 时列表端点已到尾部；这也只证明该公开 endpoint 的结果。所有 API 在本轮返回 HTTP 200。

## 2. 29 个到期来源的实际覆盖

| 来源 ID | 实际入口与停止位置 | 结果及限制 |
| --- | --- | --- |
| SRC-MISTRAL | [News](https://mistral.ai/news/) 当前渲染列表：87 articles，卡片及十个分页按钮同时出现在 HTML；只读最顶部日期段，最新普通卡片为 09/16，featured 融资为 09/08，在 09/10～09/08 段停止 | 可见目录无当窗条目；不是逐按钮浏览或全网无遗漏证明 |
| SRC-AI2 | [Papers](https://allenai.org/papers) 第 1 页 1–10，存在 Next；[Latest research](https://allenai.org/research) 与官方域名有界补检见下节 | Papers 只给年份 2026、会议及题摘预览，没有窗口过滤或公开日；在首屏停止并隔离目录覆盖限制，没有将十项当本周候选或扩为 all-years 题摘队列 |
| SRC-BLACK-FOREST-LABS | [Research](https://bfl.ai/research) 页面三张研究卡片至页尾；最新 2026-03-03，另为 2025-11-25、2025-05-29 | 可见研究入口无当窗条目；没有把导航中的新产品名等同当窗研究 |
| SRC-PHYSICAL-INTELLIGENCE | [主页](https://www.pi.website/)、[Blog](https://www.pi.website/blog)、[Research](https://www.pi.website/research)、裸域 `https://pi.website/` | 主页抓取失败；Blog/Research HTTP 403，裸域不可访问。官方域名定点搜索未恢复可采用本窗原文，不能记零研究或 Coverage 通过 |
| SRC-WORLD-LABS | [Research & Insights](https://www.worldlabs.ai/blog) Research 与 News 卡片均检查至其可见尾部；最新研究 Atlas 2026-09-01 | 目录没有当窗公开条目；未把旧 Atlas 再入选或读取历史正文 |
| SRC-SSI | [Updates](https://ssi.inc/updates) 三项可见更新至 Back，最新 2026-07-26；[主页](https://ssi.inc/) 的方向与 Updates 链接 | 无当窗披露；主页方向不作为已公开算法/安全证明 |
| SRC-REFLECTION-AI | [Blog](https://reflection.ai/blog) 两篇（最新 2025-10-09），再读 [News](https://reflection.ai/news) 当前十条至页尾（最新 2026-07-14） | 无可见当窗原始研究；未扩扫媒体融资、算力采购正文 |
| SRC-AMI-LABS | [Updates](https://amilabs.xyz/updates) 唯一 2026-03-10 launch；[主页](https://amilabs.xyz/) 世界模型方向 | 无当窗研究披露；团队旧成果不归为 AMI 新研究 |
| SRC-THINKING-MACHINES | [Connectionism](https://thinkingmachines.ai/blog/) 七项至页尾；最新 2026-07-31 | 可见目录无当窗条目，不把导航产品上新当方法证据 |
| SRC-PRIME-INTELLECT | [Blog](https://www.primeintellect.ai/blog) 顶部 09/23 Sandboxes → 09/17 Goodfire → 08/28 段；仅进入 [Sandboxes](https://www.primeintellect.ai/blog/sandboxes) | 当窗相交线索一项，已读全文核心，前分母贡献关闭；原显示日期缺时区，未改造成精确公开时刻 |
| SRC-SAKANA-AI | [Blog](https://sakana.ai/blog/) 09/25 award、09/24 advisor、09/18 FIG 段；打开 advisor 的核心说明 | 两个日级相交组织事件均关闭，不采纳世界模型愿景；在 09/18 停止，不读历史论文 |
| SRC-RECURSIVE | [Recent Stories](https://www.recursive.com/) 首屏及可见 stories；打开置顶 [First Steps](https://www.recursive.com/articles/first-steps-toward-automated-ai-research) 仅核日期 2026-06-11 | 唯一原始研究链接为窗外；未重新审读旧 benchmark，也未因“AI 改进 AI”排除其项目资格 |
| SRC-MIND-LAB | `https://macaron.im/mindlab` 实际重定向 `https://www.mindlab.im/`；进入 [Publications](https://www.mindlab.im/publications) 六项与 [Updates](https://www.mindlab.im/updates) 09/22→09/02 段，打开 V1.1 原文 | 09/22 Macaron-V1.1 一项核心已读并贡献关闭；Publications 最新 08/15。主页服务宣传不是研究；不扩扫 09/02 brain 应用 |
| SRC-SAND-AI | [组织](https://github.com/SandAI-org)；`/orgs/SandAI-org/repos?per_page=100&page=1&sort=created&direction=desc` 11 repo、无 next；MAGI-1/MagiAttention/MagiCompiler 的 releases，后两者 README News；进入 MAGI-2 原文核 08/05 | 当窗无新 repo 或 release；`pushed_at` 不冒充研究公开。MagiCompiler/MagiAttention 在窗内 push 不是自动贡献；README News 无当窗研究声明。vidmuse 产品插件不扩扫 |
| SRC-EVERMIND | [主页](https://evermind.ai/) EverCore 两张卡；只恢复对应 [EverMemOS](https://arxiv.org/abs/2601.02163) 和 [HyperMem](https://arxiv.org/pdf/2604.08256) 的版本身份 | 当前链接指向 01 月 v2 与 04 月 v2，明确不属本窗。未把主页无限记忆/性能宣传或重曝光当新论文；目录本身无公开日期，存在未标日期的新产品变更召回限制 |
| SRC-METR | [主页](https://metr.org/) Research 与 Risk Assessment 段；[Research](https://metr.org/research/) 可见顶部最新 08/26；在 Risk Assessment 恢复 [09/22 Opus 5.5](https://metr.org/blog/2026-09-22-claude-opus-5-5/) | 一项当窗原始评估正文已读，拟保留仅限评估 contract/证据权限，不涉及内部架构；日期与限制见下文 |
| SRC-PYTORCH | `pytorch/pytorch` releases：69、无 next；最新 v2.14.0 2026-09-02T17:40:10Z，末项 v0.1.1 2016-09-01 | 公开发布 endpoint 无窗内事件；未扫描普通 PR |
| SRC-MEGATRON-LM | [Repository](https://github.com/NVIDIA/Megatron-LM) README News 顶部 2026/05，releases 46、无 next；最新 core_v0.19.2 2026-09-18T19:40:26Z | 无该 endpoint 的窗内 release；没有把 README 月级旧条目重算本周 |
| SRC-DEEPSPEED | `deepspeedai/DeepSpeed` releases：100+next；最新 v0.19.7 2026-09-16T22:00:09Z，实际尾项 v0.5.2 2021-09-14T22:50:48Z | 本页无窗内事件；在历史段停止，未声称穷尽 next 历史页 |
| SRC-VERL | `verl-project/verl` releases：16、无 next；最新 v0.9.1 2026-09-20T07:24:43Z | 当窗一个 release 家族；Highlights 与 Breaking Changes 核心 11,131 chars 已读，少数纠错必要 PR 定点阅读，见下文 |
| SRC-VLLM | `vllm-project/vllm` releases：100+next；最新 v0.30.0 2026-09-22T05:20:54Z，尾项 v0.1.6 2023-09-08 | 当窗一个 release；核心 Highlights 已读。Fast Start 与 scale-out 的前置 PR 日期已核，不以本次 release 冒充机制首次披露；本执行单元不建议为旧机制重评分 |
| SRC-SGLANG | `sgl-project/sglang` releases：61、无 next；最新 v0.5.20 2026-09-18T22:41:33Z | 无窗内 release；不因其他项目调用其接口扩扫 PR |
| SRC-TRITON-LANGUAGE | `triton-lang/triton` releases：7、无 next；最新 v3.8.0 2026-08-28T18:25:56Z | 无窗内 release，且这是 kernel language，不是 Triton inference server |
| SRC-FLASHINFER | `flashinfer-ai/flashinfer` releases：100+next；v0.7.0 2026-09-22T01:15:03Z、rc4 2026-09-21T22:55:24Z；尾项 nightly-v0.6.12-20260525 | 两个事件归同一家族；读完整 release 核心、Autotuner v2 §1–5 与 experimental path 核心；rc4 不另立候选/分数 |
| SRC-NCCL | `NVIDIA/nccl` releases：17、无 next；首项 v2.32.3-1 09/17，页内 nccl4py-v0.6.0 2026-09-23T17:51:45Z | 一项当窗 Python binding/API 事件，release 3,052 chars 全文已读，不将它误称新 C++ NCCL release |
| SRC-HF-TRANSFORMERS | `huggingface/transformers` releases：100+next；最新 v5.17.0 2026-09-09T15:42:45Z，尾项 v4.47.1 2024-12-17 | 本页无窗内事件；历史页未遍历 |
| SRC-KSERVE | `kserve/kserve` releases：63、无 next；v0.21.0 2026-09-25T17:04:20Z、rc1 2026-09-23T01:22:23Z | 两个事件同一家族；完整变更说明与必要 PR body 已读；只保留纠错边界，不把所有 feature/依赖更新入选 |
| SRC-RAY | `ray-project/ray` releases：100+next；最新 ray-2.58.0 2026-08-23T05:42:08Z，尾项 ray-0.8.2 2020-02-24 | 本页无窗内事件；历史页未遍历 |
| SRC-MCP | `modelcontextprotocol/modelcontextprotocol` releases：9、无 next；最新 2026-07-28 2026-07-28T16:47:49Z | 无窗内正式 protocol release；未全扫议案、SDK 或普通 PR，不能声称所有潜在 RFC 无变化 |

### 入口受限的补检详情

Ai2 Papers 第 1 页实际出现 MolmoAct2、MolmoB0T、TAM、VLS、HARPA、LitPivot、Context-Aware RL、Cracks in the Foundation、Olmo Hybrid、FailSafe。只有年份/会议，未把每项列成日期请求或拟候选。Papers 自称 selection，不是完整年度发布档案；Next 未执行。在官方 Latest research 与域名补检中，最新确定日期为 BenchMIRT 09/01，Goodfire–Olmo 09/09、学生 AutoDiscovery challenge 09/14；没有据此证明 Papers 无本周新增。

实际辅助查询为 `site.allenai.org September 2026 20 21 22 23 24 25 26 Olmo Molmo training`，随后 `Ai2 September 2026 language model training` 限定 `allenai.org`；PI 为 `site.pi.website September 2026 20 21 22 23 24 25 26 research`，随后 `Physical Intelligence September 2026` 限定 `pi.website`。第一组宽查询返回了不相关域名，均未采用；第二次 PI 仍未恢复官方原文。查询非完备召回，未知日期、403 与未读分页不能改写为本窗零命中。

Sand 组织 API 无 next；新建日期最晚 MAGI-2-preview 2026-08-04T12:47:38Z，官方文章日期 08/05，明确窗外。MagiCompiler release 最新 v1.1.0 2026-07-01T13:46:03Z，2 条、无 next；MagiAttention 13 条、无 next，最新 v1.1.6 2026-09-18T05:05:44Z；MAGI-1 release 0 条。MagiCompiler README News blob `5eecd4153e5e2a07a6c73ad85461a74960949036`、MagiAttention `6961d5521b91046e5ae537a11739e10ed1fc5487`、Megatron README `b9b36bb56ad79a4c2ef3405e760dd08e6afd9314` 仅读顶部 News slice，不声称代码或历史机制全审。

## 3. 前分母关闭与日期隔离

- [Prime Sandboxes](https://www.primeintellect.ai/blog/sandboxes)：原显示 `SEP 23RD, 2026`，HTML 未取得带时区 datePublished。全文的 VM compatibility、filesystem namespace 隐藏任务 backing data、防 reward bypass、image affinity 与 immutable environment registry 属项目主线，但本篇是成熟 VM 隔离/缓存调度的产品组合，未提供足以改变这些方案排序或适用边界的受控比较。30M 使用量、便宜 3 倍与“无 VM 运维缺点”均不作为技术增量。GPU、snapshot/fork、persistent workspace 仍为未来项，不能写成已交付能力。贡献关闭，不为不影响处置的时区另立候选。
- [Macaron-V1.1 / Mint Recursive](https://www.mindlab.im/updates/introducing-macaron-v1-1-and-mint-recursive)：原 `Publish 09.22.2026`，JSON-LD 与 `article:published_time` 均只是 `2026-09-22`、无 tz。已读五阶段 SWE 数据组织、四 LoRA specialists、闭环训练与 UI4A 60-task/Chat 16-dimension 核心。它是换 base/数据和局部产品迭代；没有分离 base、训练、harness 等替代解释，不能从 60 例提高推出新机制或稳定因果边界。保留其及时收尾回退的负面事实，但不因有负面数字自动入选；前分母关闭。
- [Sakana advisor announcement](https://sakana.ai/schmidhuber/)（09/24）和 09/25 award 卡：分别为人事/研究愿景与组织奖项，没有公开新算法、机制或实验。旧 World Models、Gödel Machine 等链接不成为 Sakana 当窗新研究，不评分。
- [vLLM v0.30.0](https://github.com/vllm-project/vllm/releases/tag/v0.30.0)：确属窗内 release；精确 commit `ced6857afa0ea7b2e3f0846a62e1394e90f15607`。本轮 Highlights 包括 weight-cache daemon、HiSparse tier、模型 bring-up、MRV2、量化和部署接口变更。Fast Start [#54921](https://github.com/vllm-project/vllm/pull/54921) merged 2026-09-04T13:32:07Z（`a69e75b9b6d6a26d90b6790e2eb75b3419a47c16`）；scale-out [#54579](https://github.com/vllm-project/vllm/pull/54579) created 08/31、merged 09/02（`c00091e026709b149d80246a18928f514871c160`）。不能在本窗重讲为首次机制贡献。当前 release 的 `--enable-scale-out` opt-in 是版本兼容性事实，不证明授权完整性；本执行单元不为核心罗列/旧机制重复准入或评分。未逐项核 762 commits，主执行单元若发现确实不同的当窗重要 compatibility/correction 事件，只定点重开相关主张，不继承此局部关闭为所有变更已排除。

## 4. 需要后续独立准入/证据裁决的有限家族

以下不是自动保留整个 release，而是核心已显示具体增量或纠错后建议继续的主张。日期是 release 自身公开事件，不改写前置 PR 的公开日期；Stable Node 是建议 owner，Books 尚未对读或写入。本文件不要求正式 Weekly 按五项冻结，跨 Daily/既有 Weekly 去重与独立准入可收窄、驳回或复用。

### [verl v0.9.1](https://github.com/verl-project/verl/releases/tag/v0.9.1)：回执的“完成”必须包含 receiver 释放

原 `published_at=2026-09-20T07:24:43Z`，即 09/20 15:24:43+08；tag commit `1876b06d0a3e4e71e06230be10af14492ca8a75b`。建议 owner `TRAIN-DISTRIBUTED-TRAINING`，只取发布版本中的 IPC correctness 修正，而非整个 trainer 功能包。

Release 的 Weight-sync performance 核心指出删除 GC 前须修映射/ACK race。必要证据 [#7873](https://github.com/verl-project/verl/pull/7873) created/merged 09/15，merge `e488469bbf5d62bd921ca41ff746ad90768d2ff3`，**窗前首次披露，不称本周新算法**。旧 receiver 在释放 CUDA IPC mapping 前 ACK 最终 bucket，sender 随即 cleanup；GC 的约 433ms 偶然掩盖 race。只删 GC 会留存 2GiB bucket 至下一轮；将 final ACK 延后至映射释放后，才改变 sender 可以安全 reclaim/wake KV 的条件。这是已发布实现的保护行为变化，不是普通版本号。

PR 的 A/B/C snapshot 对照为单节点 Qwen3-0.6B、VeOmni/FSDP2、vLLM TP2、GSM8K GRPO、2GiB bucket，5 个同步轮次排 warmup；作者未填 GPU 型号，不外推速度或其他 backend。未覆盖 Megatron、TorchTitan、SGLang、SHM、LoRA、多节点或 direct large-weight 路径。本轮仅核原说明/对照，未跑实现。另 #7373 闲置 trainer GPU 借给 rollout merged 08/21、#7511 DP>1 admission gate merged 08/31，不为这两项窗前主张重评分。

### [FlashInfer v0.7.0](https://github.com/flashinfer-ai/flashinfer/releases/tag/v0.7.0)：tactic artifact 的执行边界与分布式一致性

原 `published_at=2026-09-22T01:15:03Z`（09/22 09:15:03+08），commit `4d75a33f19aaf48b44d5b1c5dbca33bc1eca5c58`。rc4 原 `2026-09-21T22:55:24Z`（09/22 06:55:24+08）仅 compare 链接，归同一家族、不增加候选。建议 owner `INFER-TENSORRT-LLM`（执行 plan/tactic），兼容发布边界只交接 `PLATFORM-PRODUCTION`，不要重复 owner。

已读 [Autotuner v2](https://flashinfer.ai/2026/09/22/autotuner-v2.html) §1–5 的方法、key、oracle/selection、failure controls 与 rank convergence。旧 device-only timer 在 eager 下漏掉 tactic-dependent host cost，可反转排名；显式 eager/graph measurement-policy 写入 environment identity，operation key 纳入 shape/layout/quant/top-k 等 extras。原子 per-entry publication 防半文件；runner validation 是**可选**，无 hook 仍沿旧 trust model，不称全部命中被验证。

独立 oracle 与三次 fresh selection 分离；eager 276、graph 281 是选 tactic 的 matched workloads，不是 E2E 请求性能。四 rank noisy control说明 local winner 可导致不同 symmetric-memory collective state；barrier+reload 采用最后有效发布结果保证一致，**不保证全局平均最优**。这会改变“缓存完整就可以复用”和“每 rank 独立调优无害”的具体选择，因此建议准入；没有复现实验或采用宣传倍数。

另读 [Experimental Path](https://flashinfer.ai/2026/09/22/experimental-path.html)：stable API 不等于 stable backend；auto dispatch/autotune 默认排除 experimental，只有 `FLASHINFER_ALLOW_EXPERIMENTAL_AUTO_BACKENDS=1` 才加入，explicit selection 警告，JIT-only 与 target-scope reference tests 不等于 stable support。这是实际选择门，不只是警告文案。Release 仍明确 SM100/103 小 batch FP8 groupwise `M<=32, scale=(1,128,128)` 可能错误，以及 GDN omitted `disable_state_update` **仍为 True**；不能写成 0.7 已修复或默认切 False。其他 MoE/model/packaging 列表不自动入选。

### [NCCL nccl4py v0.6.0](https://github.com/NVIDIA/nccl/releases/tag/nccl4py-v0.6.0)：资源生命周期与 runtime/IR 配对成为调用契约

原 `published_at=2026-09-23T17:51:45Z`（09/24 01:51:45+08），commit `893470119efc83fb6ecd4f9240efcf60c0aef6a3`。建议 owner `TRAIN-DISTRIBUTED-TRAINING`。本项是 Python/CuTe binding 事件；C++ v2.32.3-1 的公开不在本窗。

全文 Breaking Changes / Compatibility 明确 cooperative barrier session 最后操作后 `destroy()` **恰一次且所有 cooperative-group thread uniform control flow**，避免把 handle 复用仅当 Python 对象 GC；CuTe API 必须匹配 NCCL 2.32.3 的 `libnccl.so` 与 `libnccl_device.bc`，binding 不自动校验；这直接改变 device API 的安全使用边界。`ThreadScope.THREAD` raw integer 3→10，仅 enum 用户无需改。

Launch completion event 需 timing-disabled、非 interprocess CUDA event，所有 rank 要么提供要么不提供；post-launch recording 需 CUDA>=12.3。保留原名，不把“launch completion”外推为整个 collective/data transfer 已完成。ReduceCopy 等实验 API 扩展不作为普遍性能结论；只读官方契约，未验证 runtime/IR 配对或执行代码。

### [KServe v0.21.0](https://github.com/kserve/kserve/releases/tag/v0.21.0)：删除清理不能被无关 peer 的 terminal config 挡住

原 `published_at=2026-09-25T17:04:20Z`（09/26 01:04:20+08），commit `d1482554fc4f66dd41aee70e01f5174e24f265bd`；rc1 原 09/23 01:22:23Z（09/23 09:22:23+08）同一家族。建议 owner `PLATFORM-KSERVE`。

只取 release 的 [#6156](https://github.com/kserve/kserve/pull/6156) correctness 边界：created 09/08、merged 09/08（`38c11d71d25c41c67c31cb0e131ff4e55f9f362a`），不冒充当窗首次披露。旧 member finalizer 等 peer HTTPRoute 移除 backendRef，但 peer 配置 terminal failure 使 reconcile 提前返回/不重试，删除可无限等；新 cleanup 在 desired-state reconcile 前、错误独立返回，不让 `TerminalError` 吞掉 cleanup retry。范围仅 controller-owned group routes。

PR 有真实 manager/envtest regression 与 fault injection说明，不等于我们在 cluster 复现；**user-authored rule 不包含 owner backend 时可从 spec 重加 terminating peer，问题仍未解决**，不可写“所有删除均可靠”。PD [#6027](https://github.com/kserve/kserve/pull/6027) merged 08/28、signer [#6118](https://github.com/kserve/kserve/pull/6118) merged 09/03，是窗前机制；后者仅 interface/factory+unit tests，不能证明端到端签名信任链已完成。剩余 0.21 变更不因 release 自动保留。

### [METR Opus 5.5 predeployment evaluation](https://metr.org/blog/2026-09-22-claude-opus-5-5/)：评估对象与证据权限分层

原显示 `September 22, 2026`；原 HTML JSON-LD `datePublished=2026-09-22T00:00:00-07:00`。为避免把 date-at-midnight 当已验证的首次可用精确时刻，只用作者日级 PDT 区间 `2026-09-22T15:00:00+08:00 ～ 2026-09-23T15:00:00+08:00`，完全落窗。建议 owner `PLATFORM-EVALUATION-SYSTEM`，贡献及采用仍需非作者裁决；不是模型架构研究。

已读全文 Summary of evidence、Conclusions 与 independence note：10 个工作日 API、五个任务考察模型可产生的 AI-R&D acceleration；开发过程中**已经发生**的 acceleration 另来自 elevated-access team。这两件事不能共用 benchmark结论。评估是 unpaid，厂商有机会编辑文字，METR最终 sign-off；独立评价标签不等于全证据公开。

作者明确另一 team 无法共享 supporting evidence 或 reasoning，且估计时期未说明；因此不采用隐藏证据的约1.5×、不推“模型研发已显著加速”、不推 alignment/厂商 policy threshold 已验证。可继续核验的增量是本次报告显示的评价 contract/可审计性边界，而非产品能力宣传。若现有长期主张充分覆盖这些边界，关闭或具体已有覆盖均可；不能仅据该报告名称或模型上新准入。

## 5. 本发现任务的保留项与重开位置

1. **PI 入口 403**：缺窗口内可读官方目录/条目；需同一官方 URL 可读页面、官方 feed或作者具名当窗原文才能定点恢复。当前不支持候选、Books或全源无遗漏。
2. **Ai2 年级 Papers / 未读 Next**：缺窗口可定位的公开条目及日期；可接受官方带日期导出、dated research/news archive或题名对应作者 release。重开 Papers 本周相关切片，不遍历全年正文。
3. **非完备检索边界**：五个 `100+next` 发布列表在历史段停止；没有恢复隐藏 draft/re-publish 或未标 release 的研究/RFC。若出现具体当窗身份，只查该事件与受影响窗口，不写“全 GitHub 无遗漏”。
4. **候选后续**：上述有限家族是待主任务校准的源级提议，尚须跨七份 Daily 去重、独立准入、采用命题证据审阅、具体 Books 对读及必要写回。普通未做工作不是 external Blocked，也不能提前 Weekly Complete。

机器格式校验不适用于将此来源记录冒充六段正式 Report；本任务仅检查目标文件 Markdown、链接形式与 scoped diff。不存在本执行单元给自己做的独立语义通过声明。
