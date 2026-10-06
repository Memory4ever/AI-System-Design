{{< figure src="https://qianwen-res.oss-accelerate-overseas.aliyuncs.com/qwen3max-banner.png" width="100%" alt="Qwen3 Main Image" >}}



{{< button href="https://chat.qwen.ai" label="QWEN CHAT" external=true >}}

{{< button href="https://www.alibabacloud.com/help/en/model-studio/models#c2d5833ae4jmo" label="API" external=true >}}

{{< button href="https://discord.gg/yPEP2vHTu4" label="DISCORD" external=true >}}




## Introduction



Following the release of the Qwen3-2507 series, we are thrilled to introduce Qwen3-Max — our largest and most capable model to date. The preview version of Qwen3-Max-Instruct currently ranks third on the Text Arena leaderboard, surpassing GPT-5-Chat. The official release further enhances performance in coding and agent capabilities, achieving state-of-the-art results across a comprehensive suite of benchmarks — including knowledge, reasoning, coding, instruction following, human preference alignment, agent tasks, and multilingual understanding. We invite you to try Qwen3-Max-Instruct via its API on Alibaba Cloud or explore it directly on Qwen Chat. Meanwhile, Qwen3-Max-Thinking — still under active training — is already demonstrating remarkable potential. When augmented with tool usage and scaled test-time compute, the Thinking variant has achieved 100% on challenging reasoning benchmarks such as AIME 25 and HMMT. We look forward to releasing it publicly in the near future.




## Qwen3-Max-Base



The Qwen3-Max model has over 1 trillion parameters and was pretrained on 36 trillion tokens. Its architecture follows the design paradigm of the Qwen3 series, incorporating our proposed global-batch load balancing loss.



- Training Stability: Thanks to the MoE (Mixture of Experts) architecture design of Qwen3, the pretraining loss curve of Qwen3-Max remains consistently smooth and stable throughout training. The entire training process proceeded seamlessly without any loss spikes, eliminating the need for strategies such as training rollback or adjustments to data distribution.

- Training Efficiency: Optimized by PAI-FlashMoE’s efficient multi-level pipeline parallelism strategy, the training efficiency of Qwen3-Max-Base significantly improved, achieving a 30% relative increase in MFU (Model FLOPs Utilization) compared to Qwen2.5-Max-Base. For long-context training scenarios, we further employed our ChunkFlow strategy, which delivered a 3x throughput improvement over context parallelism, enabling training with a 1M-token context length for Qwen3-Max. Additionally, through multiple techniques including SanityCheck, EasyCheckpoint, and scheduling pipeline optimizations, the time loss caused by hardware failures on ultra-large-scale clusters was reduced to one-fifth of that observed during Qwen2.5-Max training.




## Qwen3-Max-Instruct



The preview version of Qwen3-Max-Instruct has secured a top-three global ranking on LMArena text leaderboard. The official release further elevates its capabilities — particularly in coding and agent performance. On SWE-Bench Verified, a benchmark focused on solving real-world coding challenges, Qwen3-Max-Instruct achieves an impressive score of 69.6, placing it firmly among the world’s top-performing models. Moreover, on Tau2-Bench — a rigorous evaluation of agent tool-calling proficiency — Qwen3-Max-Instruct delivers a breakthrough score of 74.8, surpassing both Claude Opus 4 and DeepSeek V3.1.



{{< figure src="https://qianwen-res.oss-accelerate.aliyuncs.com/Qwen3-Max/Qwen3-Max-Instruct-text_arena.png" width="100%">}}



{{< figure src="https://qianwen-res.oss-accelerate.aliyuncs.com/Qwen3-Max/Qwen3-Max-Instruct.png" width="100%">}}




## Qwen3-Max-Thinking (Heavy)



The reasoning variant of Qwen3-Max, named Qwen3-Max-Thinking, is demonstrating extraordinary performance. By integrating a code interpreter and leveraging parallel test-time compute techniques, it achieves unprecedented reasoning capabilities — most notably attaining perfect 100-point scores on the challenging mathematical reasoning benchmarks AIME 25 and HMMT. We are currently engaged in intensive training of Qwen3-Max-Thinking and look forward to delivering it to you soon.



{{< figure src="https://qianwen-res.oss-accelerate.aliyuncs.com/Qwen3-Max/Qwen3-Max-Thinking-blog.jpg" width="100%">}}




## Develop with Qwen3-Max



Now Qwen3-Max-Instruct is available in [Qwen Chat](https://chat.qwen.ai), and you can directly chat with the powerful model. Meanwhile, the API of Qwen3-Max-Instruct (whose model name is `qwen3-max`) is available. You can first [register an Alibaba Cloud account](https://account.alibabacloud.com/register/intl_register.htm) and activate Alibaba Cloud Model Studio service, and then navigate to the console and create an API key.



Since the APIs of Qwen are OpenAI-API compatible, we can directly follow the common practice of using OpenAI APIs. Below is an example of using Qwen3-Max-Instruct in Python:
{{< code src="./code/d935249f-041e-406f-aa57-18973d134d0a.py" lang="python" >}}
}}




## References




[^1]: Qwen3 Technical Report, arXiv


[^2]: Demons in the detail: On implementing load balancing loss for training specialized mixture-of-expert models, ACL25


[^3]:  Efficient Long Context Fine-tuning with Chunk Flow, ICML25




## Citation



Feel free to cite the following article if you find Qwen3-Max helpful.
{{< code src="./code/69150ffa-2816-4585-9283-f117947d48c9.txt" lang="" >}}
}}