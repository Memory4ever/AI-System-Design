Exact source: https://arxiv.org/html/2601.08128v1
Necessary bounded positions, actual original text below; not full-paper/appendix traversal.

## Text offsets 14100–17500
 response given partial history. Like the memory benchmarks, these evaluation criteria instead require the AI system to have a full conversation, after which the AI system’s performance across the conversation as a whole is evaluated. For example, AutoPal  [ 3 ] , evaluates the agent on criteria such as naturalness, affinity, and personalization. We also adopt some of these criteria into our benchmark, although whereas these criteria are typically evaluated by humans, we synthetically evaluate them using a larger model. 
 
 
 
 
 3 Problem Formulation 

 
 ‘Edge’ device is a relative term that captures a wide range of devices. In the field of robotics, even an RTX 4090 or 3090 can be considered an edge device  [ 19 ] . Here we define edge devices to have much weaker capabilities. Specifically, we test using the NVIDIA Jetson Orin Nano Super 8GB  [ 14 ] , enforcing the following set of assumptions on our system: 
 
 1. 
 
 Memory constraints: Under the assumption of only 8GB of VRAM, devices can fit only small, quantized models. This becomes even more challenging if developing a full pipeline with additional models, such as a STT and TTS. To balance these challenges while also maximizing the intelligence of our LLM model, we opt to use a 7B parameter model with int4 quantization. 
 
 2. 
 
 Compute constraints: Edge devices have orders of magnitude less compute available than cloud devices. Increasing context window or running parallel requests will quickly hit memory limits and increase latency. 
 
 3. 
 
 Real-time constraints: Responsiveness matters for a natural companion UX. Studies show that human conversations with faster response times are rated as more enjoyable and related to increased feelings of social connection   [ 26 ] . Average human response time in English is 236 ms with a standard deviation of 519 ms  [ 23 ] . Therefore, we aim to minimize perceived latency wherever possible, unless at a very high cost to quality. Any such exceptions will be clearly noted in the paper. 
 
 4. 
 
 Limited Context Window: On such devices, we cannot make use of the full context window even for these smaller models. Fig.   2 illustrates the average time to first token (TTFT) latency for Qwen 7B. We attempt to replicate realistic conditions in our latency testing, for implementation details refer to Appendix Section   C.1 . Beyond 10k tokens, llama-server begins to run out of memory due to the computational resource limits of the Jetson. However, long before it reaches that point, smaller context windows would be necessary to maintain reasonable latencies. To achieve a goal of even ∼ \sim 5s, context windows smaller than ∼ 2500 \sim 2500 tokens would be necessary. Human-like latencies of ∼ 2 \sim 2 s would require limits of ∼ \sim 1000 tokens. Similarly, Fig.   2 shows that a similar context window threshold would be needed to maintain a reasonable tokens/sec output as well. 
 
 
 
 
 
 Figure 1 : Average TTFT across input token sizes on NVIDIA Jetson. We use Qwen2.5-7B-Instruct (int4) GGUF  [ 25 , 27 ] using llama.cpp  [ 7 ] for requests with varying input token size, taken over 5 trials. 
 
 
 Figure 2 : Average tokens/sec across input token sizes on NVIDIA Jetson. Same settings are used. 
 
 
 
 Given the above set of assumptions, the system could run on even cheaper hardware than the Jetson, as a 7B int4 model can even be run on a good qu

## Text offsets 42984–45100
 7 Limitations and Future Work 

 
 Ability of Large Model to Play a Child : For our specific AI toy use case, we have Claude attempt to play the role of a child. We acknowledge that it does not do a perfect job at playing this role. Many responses feel longer and more sophisticated than a realistic child response. Responses often feel too long for a voice conversation and sometimes contain long enumerated lists. Sometimes Claude creates conversation ending situations when playing the child, such as having the child go to bed, after which it will no longer respond to messages other than by responding with messages such as “*still sleeping soundly*\n\n*calm, rhythmic breathing*\n\n*resting peacefully*” . While we believe that the benchmark does a reasonable job of testing the system, we admit that there is future work that could be done to perfect the user model, especially for use cases involving Children. 
 
 
 
 Benchmark Memory Metrics : While we test memory capabilities to some extent with our generated QA task, there are question types such as Multihop or Aggregation questions that have been shown to cause models and memory systems to struggle, and are commonly used in related benchmarks   [ 11 , 8 ] . These question types are difficult to generate automatically, and have been omitted. The benchmark could be further improved and made more challenging by finding ways to synthetically generate those question types. 
 
 
 
 Other Benchmark Aspects : While we believe 100k conversations, split across 10 sessions of 10k each, is sufficient for testing performance, the benchmark could be made more realistic by varying session lengths. Although 100k conversations represents a significant amount of interaction, further work could explore even longer simulations, to test an AI Companion’s performance over months worth of content as opposed to weeks. 
 
 
 We could also simulate the passage of time over the sessions, i.e. treating each subsequent session as taken on the following day. This would allow us to test system mechanics such as forgetting memories over time. 
 
 
 
 8 Conclusi

## Text offsets 98436–101850
 C.1 Latency testing 

 
 For all latency testing, we use llama.cpp commit 9a3ea685b.

 
 To replicate realistic conditions, the trials use an existing simulated conversation [refer to section 5 for additional details] and insert messages into a simple ‘summary’ system prompt until the token count surpasses the desired test token count. While this means the number of input tokens is not exact, we check to confirm it varies by no more than 150 tokens. Additionally, we run a simple unrelated prompt on llama.cpp before starting the testing for ‘warmup’ purposes to ensure nothing is being loaded in specifically on our first request. Finally, we also insert a randomly generated uuid into the system prompt to invalidate any kv-caching of prior messages. This invalidation is necessary for a realistic simulation, since in a real system the system prompt will likely be constantly changing, with items like short and long term memories being inserted into the system prompt.

 
 
 
 
 Figure 7 : Latency chart showing average TTFT on NVIDIA Jetson with unrealistic ‘perfect’ caching. 
 
 
 Although it is difficult to illustrate what latencies with caching would look like without assuming a given system structure (i.e. how many past tokens are cached vs new, etc.), we attempt to shed at least some light on this question by rerunning our prior set of trials without invalidation the cache ( Fig.   7 ), using default llama.cpp caching. So for example, for the 7500 input token point on the chart, we would effectively be running 5000 cached tokens (the prior threshold, as indicated by the previous point on the chart) + 2500 new input tokens.
This is intended to try and anticipate discussion of a hypothetical situation where we could insert all necessary dynamic information (memories, etc.) at the end of the chat messages (such as via another system message) instead of in the single system message at the beginning of the chat messages. Qwen 7B (int4) cannot handle this well in our experience, but perhaps a more intelligent model would be able to better handle this. Regardless, the chart attempts to show that even with caching, context windows would still need to be limited to a similar degree to achieve good latency. 
 
 
 We note that for all trials, there seems to be some unexpected behavior where the ∼ 500 \sim 500 tokens latencies consistently seem to be worse than the ∼ 1000 \sim 1000 tokens latencies. We assume this is due to some peculiarities with the hardware or llama.cpp settings, and do not explore this further as that is not the focus of this paper. 
 
 
 
 C.2 Memory Post Processing 

 
 C.2.1 Overview 

 
 One of the ideas we experimented with was an additional memory post-processing step. However, we ultimately didn’t include it since the tiny qwen model struggled to meaningfully post-process the memories the way we wanted. However if we had a more powerful model, we’d likely incorporate a post-processing step to this effect. 
 
 
 With that said, the idea was that each individual new memory (including modified memories generated for an overwrite/merge) would go through an additional temporal post-processing step to make memories with specific dates easier for the model to understand. Our tiny, quantized Qwen model often has issues reasoning over dates, such that even if we tell Qwen when a memory was extracted and the current date, it may respond to the use
