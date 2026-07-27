# AI Research Weekly — 2025-W40

> Coverage Window: 2025-09-29～2025-10-05
> Research Mode: Retrospective Backfill
> Accessed: 2026-07-31
> Backfilled: 2026-07-31

## Executive Summary

本周保留 1 项长期证据：DeepSeek-V3.2-Exp / DeepSeek Sparse Attention。重点是约束、机制、trade-off 与演进，不是发布热度。

## Coverage Window and Limitations

- 按官方发布日期、GitHub Release 或 arXiv v1 归档；后续修订回链首次公开周。
- Scholar、OpenAlex、DBLP 负责 discovery/去重；论文事实回到正文。Crossref 仅交叉检验 metadata。
- 历史回填不创建 Daily；Accessed 统一为 2026-07-31。
- 作者/厂商 benchmark 缺少完整 workload contract 时不外推。

## 1. 模型与研究机构

### Source Coverage

按固定机构顺序扫描国内外模型公司、研究机构与 Hugging Face Blog。

- 保留：DeepSeek-V3.2-Exp / DeepSeek Sparse Attention（2025-09-29）。

## 2. 论文与学术来源

按 arXiv → Google Scholar → OpenAlex → DBLP 扫描，回到 v1 正文核验。

- 本组无达到保留门槛的候选。

## 3. AI Infra 与工程项目

按 PyTorch → JAX → CUDA → Triton → vLLM → SGLang → Dynamo → TensorRT-LLM → Ray → KServe → Kubeflow → Kubernetes → Hugging Face → DeepSpeed → Megatron-LM → llama.cpp → ONNX Runtime → OpenXLA 扫描。

- 本组无达到保留门槛的候选。

## Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| DeepSeek-V3.2-Exp / DeepSeek Sparse Attention | 5 | 5 | 4 | 5 | 5 | 4 | 28/30 | Must Read；与 W08 NSA 和 W49 V3.2 建立完整演进 |

### Deep Analysis 1 — DeepSeek-V3.2-Exp / DeepSeek Sparse Attention

- First Public: 2025-09-29
- Status: Official experimental model + technical report
- Primary Source: https://api-docs.deepseek.com/updates
- Evolution Relationship: Direct Evolution

#### Why

NSA 证明可训练稀疏注意力方向后，真正系统门槛是把 sparse selection、kernel 和 cache state 集成到可服务模型，并保持 quality。

#### Principle and Mechanism

V3.2-Exp 将 DeepSeek Sparse Attention 用于模型并开放权重/报告；它是 NSA research mechanism 向 model/runtime contract 的一次转化。

#### Trade-off and Evidence Boundary

长上下文成本下降可能伴随 selector state、稀疏 kernel、硬件适配和质量边界；experimental model 不应覆盖 dense/MLA 路径仍适用的场景。

#### Connection and Evolution

知识树位置：第 14、22、39～41、45、46、50 章。Must Read；与 W08 NSA 和 W49 V3.2 建立完整演进。若进入 Books，将保留旧方案仍成立的条件，并区分官方事实、作者实验和跨来源推断。

## Full Source Review

### DeepSeek-V3.2-Exp / DeepSeek Sparse Attention

- **Candidate / Week / Score:** DeepSeek-V3.2-Exp / DSA / 2025-W40 / 28/30。
- **Source Family ID:** `DEEPSEEK-DSA-2025`（W08 NSA为前置research branch；W49 V3.2为同architecture后续完整报告）。
- **Source Type:** official experimental release、brief technical report、model/config/demo code、open kernels；后续同作者arXiv full report用于补足机制与实验边界。
- **First-public Date / Revision History:** V3.2-Exp 2025-09-29；demo code于2025-11-17修正indexer RoPE layout；完整V3.2报告arXiv v1 2025-12-02，不能把后续post-training结果倒灌到9月checkpoint。
- **Direct Primary Sources:** official V3.2-Exp repository/model card、`DeepSeek_V3_2.pdf` artifact、inference demo/config、DeepGEMM/FlashMLA kernels。
- **Related Primary Sources:** DeepSeek-V3.2 arXiv:2512.02556（明确声明architecture与V3.2-Exp完全相同并完整披露DSA）；W34 V3.1-Terminus、W08 NSA。
- **Access and Verification Status:** Verified for release、artifact、code/kernels、corrective update与完整同architecture DSA report；9月GitHub PDF文件存在且metadata已核，但当前环境无法直接抽取其正文。机制字段只采用12月作者full report明确确认与V3.2-Exp相同的architecture，不倒灌后续RL/agent结果。
- **Full-read Coverage:** 已阅读release/README、benchmark table、model card、demo code入口、kernel ownership与2025-11-17 correction；完整阅读arXiv full report的metadata、Introduction、DSA公式/MLA实例化、dense warm-up、sparse training、parity、long-context、inference cost、limitations及相关appendix。9月brief PDF正文为唯一未直接抽取的二进制文本。
- **Original Problem:** MLA的main attention在长序列仍近似二次增长；研究型sparse attention若不能与既有checkpoint、KV latent layout和高性能kernel兼容，无法进入可服务模型。
- **Why the Previous Design Was Reasonable:** dense MLA质量稳定、latent KV降低cache并有成熟FlashMLA；NSA等research mechanism尚需selector training、kernel与checkpoint migration证据。
- **Changed Constraint:** 128K训练/推理及大规模post-training要求将主attention成本从$O(L^2)$降到$O(Lk)$，同时尽量保留V3.1-Terminus能力与artifact兼容性。
- **Mechanism:** lightning indexer为query与历史token计算多头ReLU score，top-k选择2048个MLA latent KV；主attention仅访问选中集合。indexer自身仍$O(L^2)$但维度/heads小且可FP8；DSA基于MLA的MQA mode以便KV entry跨query heads共享。
- **State Ownership:** indexer拥有selection scores/top-k，MLA cache拥有latent KV，runtime/kernel拥有paged index与sparse gather，training pipeline分别优化indexer KL loss与main LM loss；部署者拥有dense/short-context fallback与version pinning。
- **Control Flow / Data Flow:** V3.1-Terminus 128K checkpoint → 1000-step dense warm-up仅训练indexer、拟合dense attention distribution → 15,000-step sparse continuation同时训练main model/indexer但梯度分离 → post-training → runtime index score/top-k → sparse MLA compute。
- **Implementation Details:** warm-up 2.1B tokens（16×128K/step）、LR $10^{-3}$；sparse stage 943.7B tokens（480×128K/step）、LR $7.3\times10^{-6}$、top-k 2048。TileLang为research-readable kernels，DeepGEMM/FlashMLA为高性能path。11月修复表明indexer RoPE需non-interleaved而MLA RoPE需interleaved。
- **Evaluation Setup:** 9月vendor表将V3.2-Exp与V3.1-Terminus对齐training config并比较reasoning/tool benchmarks；后续full report提供short/long parity、ChatbotArena间接偏好、AA-LCR/Fiction.liveBench与H800实际service cost estimate。评测不是跨model通用SLO。
- **Baselines / Ablations / Sensitivity:** 关键baseline为同源V3.1-Terminus；dense warm-up→sparse continuation构成migration test。缺top-k、indexer dimension、FP8、kernel、hardware topology与selector错误的完整消融；human preference为间接Elo。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** H800用于后续service cost estimate、训练序列128K与top-k 2048披露；training cluster、precision全栈、serving batch/concurrency、TTFT/TPOT与SLO不完整。
- **What the Evidence Actually Proves:** 作者完整报告证明V3.2与V3.2-Exp architecture相同，DSA通过小indexer+fine-grained selection把main attention降为$O(Lk)$，并给出从dense checkpoint渐进迁移的训练机制；开源code/kernel与后续RoPE修正证明实现细节是机制的一部分。
- **What It Does Not Prove:** 不证明总复杂度完全线性（indexer仍$O(L^2)$）、不证明所有硬件/长度更快、不证明质量严格等价、也不证明9月vendor benchmark独立复现。12月RL/agent能力不能归因或倒灌给V3.2-Exp。
- **Limitations / Threats to Validity:** selector错误可能永久丢失KV；top-k固定引入长度/任务敏感性；kernel/page layout复杂；9月brief PDF正文未直接抽取；full report主要由作者评测，成本图缺完整workload contract。
- **Trade-offs / New Failure Modes:** 主attention成本下降，但新增indexer state/compute、top-k miss、sparse gather、paged cache、layout兼容和migration training；RoPE correction显示“数学相同、layout不同”即可产生质量regression。
- **Where the Previous Design Still Applies:** 短context、selector不可靠、backend无稀疏kernel或需要全token精确交互时dense MLA仍合理；research阶段可先用readable TileLang，production才用高性能kernel。
- **Evolution Relationship:** `Direct Evolution`：NSA提出hardware-aligned sparse principle → DSA用lightning indexer/MLA/top-k完成checkpoint与kernel productization → W49以同architecture扩展post-training。后发节点不否定dense MLA。
- **ROADMAP Node:** Ch14、Ch19、Ch22、Ch39～41、Ch45～46、Ch50。
- **Target and Adjacent Chapters Read:** 已阅读 Ch13～22与Ch38～50；Ch22为mechanism/evolution主owner，Ch39～41/45～46/50只做cache/kernel/serving handoff。
- **Existing Coverage:** Ch22 provisional已有DSA路线，但必须检查是否区分indexer $O(L^2)$、top-k 2048、两阶段训练、RoPE layout failure与后续RL不可倒灌。
- **Integration Decision:** `Refine — Existing Argument`；主 owner Ch22，与 NSA→DSA staged migration 联读。
- **Changed Files or Rejection Reason:** 已复核 `books/part-02-model/22-long-context.md`；9 月 brief 访问限制保留在 Weekly。
- **Open Questions:** selector recall/quality、top-k sensitivity、indexer占比、跨硬件kernel、cache invalidation、fallback与layout conformance test仍需独立证据。

## Evidence Level

- Official facts 只覆盖公开接口、版本、权重和文档。
- arXiv / technical report 为作者实验，默认 Experimental，未等同独立复现。
- 跨来源演进关系是本项目推断，已显式标注。

## Cross-Week Deduplication

- release、paper v1 与后续集成若日期不同，分别记录证据角色，但只建立一个 Books source packet。
- 新方案不静默覆盖旧方案；记录新增状态、成本和 failure modes。

## Knowledge Tree Position

- DeepSeek-V3.2-Exp / DeepSeek Sparse Attention → 第 14、22、39～41、45、46、50 章（Direct Evolution）

## Recommended Action

- DeepSeek-V3.2-Exp / DeepSeek Sparse Attention：Must Read；与 W08 NSA 和 W49 V3.2 建立完整演进

## Event-Date Daily Decision

历史回填不创建 Daily；证据保留在本 Weekly。

## Books Integration Decision

Books Gate 已完成。该周候选的最终 disposition 已写入各自 Full Source Review；没有评分候选的周保持 No Material Update，不为制造 diff 修改 Books。


## Ignored Noise

- 忽略转载、旧内容重发、无 primary evidence 的榜单与缺条件 benchmark。
- API alias/价格变化若不形成机制，只作为版本治理信号。

## Repository Changes

- 新增 papers/2025/weekly/2025-W40/README.md。
- DSA 候选完成最终 disposition；第 22 章已按 NSA→DSA source family 复核。

## Open Questions

- 9月brief PDF正文当前无法直接抽取；机制由作者12月同architecture全文报告核验，仍缺独立质量、fallback与跨硬件证据。

## Sources

- DeepSeek-V3.2-Exp / DeepSeek Sparse Attention — https://api-docs.deepseek.com/updates（First Public: 2025-09-29；Accessed: 2026-07-31）
- DeepSeek-V3.2-Exp repository/report/artifact — https://github.com/deepseek-ai/DeepSeek-V3.2-Exp（First Public: 2025-09-29；Accessed: 2026-07-31）
- DeepSeek-V3.2 full technical report — https://arxiv.org/html/2512.02556（v1: 2025-12-02；Accessed: 2026-07-31；仅用于同architecture DSA机制与后续边界）
