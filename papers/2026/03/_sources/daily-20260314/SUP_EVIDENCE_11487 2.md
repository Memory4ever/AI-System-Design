# 11487 Attention Sinks：必要审阅与具体已有覆盖

root只接本日必要Source与Books判断，不写正式报告。日期/准入复用本日首包独核，精确来源[2603.11487v1](https://arxiv.org/html/2603.11487v1)，缓存`SUP_CORE_11487.raw/.txt`。评分建议2+1+2=5，标准审阅；不以普遍softmax/no-op成熟原则计Durability3。

实际读§3.1–3.5任务、输入/输出、sup-support loss、attention模型与三个定理/主文proof sketch，以及§4局部实验和§5–6直接限制。没有宣称审了所有附录完整证明或运行代码；本处不采用定理常数、真实LLM所有sink唯一原因、非归一模型通用收益。

原任务将BOS、trigger、non-trigger标识及连续内容分开；trigger输出截至自身的非BOS均值，其他位置输出零。给定长度/维度、bounded density和足够小的support-sup输出误差，单层normalized attention的BOS mass以高概率趋近1；纯attention多层构造只保证某层/位置存在sink，不是每头/每层都如此。ReLU构造可全零且不用BOS，同时除以可见非BOS数量以完成均值任务，不能把它叫任意未缩放ReLU已和softmax等价。理论composition无MLP/residual一般性；实验扩展到有residual的有限2/4层、2/4头，L16，1000个固定trigger test例，某头无sink与存在性共存。这不是任意pretrained Transformer通用证明。当前no-op或局部均值条件不成立时，不能据本篇删除真实sink或签发language quality。

收益是区分结构上必须分配质量与语义内容读取；代价/替代是relax normalization、显式null/gate需重校准scale、训练稳定性和真实任务。论文给synthetic验证与real-model既有研究动机，未给大模型end-to-end加速、质量全局支配或在线SLO；没有运行硬件/precision/重复训练CI足以支持此类性能采用，不补成生产保证。无代码核验/复现。

实际顺读Ch14 `归一化决定质量去向，也限制 no-op`完整局部（含前节learning supervision、后续prior/null/value gate/affine mass），并读Ch13/15交接。现正文已明确“精确trigger-conditional构造迫使某位置sink、移除归一化可全零”，随即说明不代表真实每个sink/no-op或非归一Attention语言优势，并保留成熟softmax与null/register/gate的成本/共存。**采用的长期命题已由这两段具体承载，无新必要机制差额；建议已有覆盖 `MODEL-SELF-ATTENTION`，Books新写0。** 精确定理限定留在本证据而非为扩写重复插段；不是按主题相同直接NC。

作者/独立非root复核仍须实际核必要原证与此具体NC定位，再同步正式候选/§4；本文件不自授独立DAY。若将来要采用完整theorem/rate或多头一般必要性，仅定点重开相应证明，不索取全部PDF或全版本差分。
