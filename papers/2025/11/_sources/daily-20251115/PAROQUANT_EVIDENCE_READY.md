# 11/15 ParoQuant 必要Evidence与具体Books处置

作者Planck；准入及6分已由[Ohm](FIRST_INDEPENDENT_REVIEW.md)通过，日期使用[DATE_RECOVERY](DATE_RECOVERY.md)保守BJT [Nov14 09:00,Nov15 03:05:54)，不是DataCite注册上界。exact-v1 [实际原HTML](raw-paroquant-v1.html) §4.1–4.3、§5.1–5.3/Tables1–5与A.3/A.4已实际核；没有运行代码/复现。

## 最小支持与关键反侧

可逆权重变换只是旧代数前提。新增选择是每128通道group内每轮最多64个互不重叠Givens pairs，8轮顺序叠加channel scale；轮内无依赖才可并行，跨轮仍不能交换。kernel按token/group/pair并行，activation shared memory、indices/angles registers，多轮一次加载融合。Eq9按原浮点层输入X与前层量化后的X'输出loss校准；两阶段先角度/scale、再权重及quantizer参数微调，不把全部质量差额归于rotation本身。

W4A16、linear group128；Llama2/3/3.1、R1-distill与Qwen3若干模型。H200离线校准2048混合WikiText/C4/RedPajama、Pile64验证选择，2048seq、seed0、两阶段各10epochs；70B调整batch与学习率。Table4 Llama3-8B C4中8IR+scale由7.35到stage2后7.27，说明微调贡献不能抹掉；Table5更多IR的MMLU-Pro并非每步单调，0/2/4/8为69.6/69.4/69.4/70.1。第一层k_proj的10%pair观察不授全网络等效。

Table3/A.4在同Transformers路径仅替换linear/transform/dequant，Paro使用AWQ W4A16 GEMM+自有transform，PyTorch2.6、compile max-autotune/CUDA Graph，batch1 RTX A6000/6000Ada/4090分别保留。不等生产并发/SLO；输入/输出长度、测量重复不确定性未披露，不能补写。**A6000 Qwen3-1.7B AWQ320→Paro278 tokens/s是13.125%吞吐降低，等tokens延迟增加约15.11%**，不满足概括的“<10%”全模型保证；4B176→160也有9.09%吞吐降低/10%等tokens延迟增加。准确率与离线成本分开，QTIP vector与Paro linear也非同quantizer归因。

因此标准Evidence完成的结论是：该作者范围支持用有限独立pair层/scale换W4A16质量与在线变换成本的条件选择，不采用普遍<10%、长CoT累积是唯一因果、全层10%等效或生产服务保证。原2+2+2=6保持，不因为Books选择或访问状态改分。

## Books决定与实际owner

**仅报告**，请root独立核最终选择。再次实际读`INFER-TENSORRT-LLM` [Ch49](../../../../../books/part-05-inference-system/49-tensorrt-llm.md)的“Rotation Scope与Quantization Group必须共同进入Numeric Plan”L1170–1210：已明确rotation scope/group/metadata/kernel成本共同版本化、校准与在线cost分账、更简单rotation与高精度回退；“顺序程序拥有语义，Parallel Annotation拥有Schedule”承载dependency先行。现有正文不逐名列Paro算法，亦不声称任意rotation免费，本材料是具体可实现分支及新局部验证，不要求改变现有长期设计原则。将参数、反侧与测量边界保留日报，不在共享Book再插一篇算法摘要。

若root认为pair-independent轮内与跨轮顺序是必需的具体缺口，精确备选位置为原rotation scope/group段后，而非章末收纳；只能窄说明有限pair层的并行合法性与多轮表示能力/在线成本，必须保留上述反侧。当前未提出强制写入、未改共享Books，独立Evidence/Books最终核尚未返回。
