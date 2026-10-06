# RLM 作者窗前正文有限身份缓存

原始blog：https://alexzhang13.github.io/blog/2025/rlm/
官方dated index：https://alexzhang13.github.io/blog/page/2/ ，L11–14 October15,2025及同题核心description。
实际GET原稿：https://api.github.com/repos/alexzhang13/alexzhang13.github.io/contents/_posts/2025-10-15-rlm.md?ref=c6f7623f2e495b7464a4c8a3802f5b02fc59325e ，content base64 decoded。
有限path history：https://api.github.com/repos/alexzhang13/alexzhang13.github.io/commits?path=_posts/2025-10-15-rlm.md&per_page=30 ，15 entries终止，Oct15正文及Dec27快照只是dated public blog的辅证，不令commit=firstpublic。当前blog已2026修订，故用Dec27快照仅核先前机制身份；不当本窗完整preprint首次公开上界。

仅保存决定身份的原始段，不声称完整博客全段或全部实验审阅；下面同REPL-variable、recursive depth1、no-subcall、OOLONG/BrowseComp及cost/runtime限制均在窗前快照。v1额外Qwen/CodeQA/OOLONG-Pairs是否重要新事件待root判断。

## **Recursive Language Models (RLMs).**

A recursive language model is a thin wrapper around a LM that can spawn (recursive) LM calls for intermediate computation — from the perspective of the user or programmer, it is the same as a model call. In other words, you query a RLM as an "API" like you would a LM, i.e. `rlm.completion(messages)` is a direct replacement for `gpt5.completion(messages)`. We take a <strong>context-centric view</strong> rather than a <strong>problem-centric view</strong> of input decomposition. This framing retains the functional view that we want a system that can answer a particular <strong style="color:purple;">query</strong> over some associated <strong style="color:orange;">context</strong>:

<figure>
<center>
    <img src="/assets/img/rlm/api.png" style="width:70%; margin-bottom: 10px" alt="API">
</center>
    <figcaption style="width:70%; margin:auto"><strong>Figure 2.</strong> A recursive language model call replaces a language model call. It provides the user the illusion of near infinite context, while under the hood a language model manages, partitions, and recursively calls itself or another LM over the context accordingly to avoid context rot.</figcaption>
</figure>

Under the hood, a RLM provides only the <strong style="color:purple;">query</strong> to the LM (which we call the <strong style="color:green;">root LM</strong>, or LM with depth=0), and allows this LM to interact with an <strong style="color:#5bc0fb;">environment</strong>, which stores the (potentially huge) <strong style="color:orange;">context</strong>.

We choose the <strong style="color:#5bc0fb;">environment</strong> to be a loop where the LM can write to and read the output of cells of a Python REPL Notebook (similar to a Jupyter Notebook environment) that is pre-loaded with the <strong style="color:orange;">context</strong> as a variable in memory. The <strong style="color:green;">root LM</strong> has the ability to call a recursive LM (or LM with depth=1) inside the REPL <strong style="color:#5bc0fb;">environment</strong> as if it were a function in code, allowing it to naturally peek at, partition, grep through, and launch recursive sub-queries over the <strong style="color:orange;">context</strong>. **Figure 3** shows an example of how the RLM with a REPL <strong style="color:#5bc0fb;">environment</strong> produces a final answer.


<figure>
<center>
    <img src="/assets/img/rlm/repl.png" style="width:90%; margin-bottom: 10px" alt="API">
</center>
    <figcaption style="width:90%; margin:auto"><strong>Figure 3.</strong> Our instantiation of the RLM framework provides the root LM the ability to analyze the context in a Python notebook environment, and launch recursive LM calls (depth=1) over any string stored in a variable. The LM interacts by outputting code blocks, and it receives a (truncated) version of the output in its context. When it is done, it outputs a final answer with `FINAL(…)` tags or it can choose to use a string in the code execution environment with `FINAL_VAR(…)`.</figcaption>
</figure>

When the **root LM** is confident it has an answer, it can either directly output the answer as `FINAL(answer)`, or it can build up an answer using the variables in its REPL environment, and return the string inside that answer as `FINAL_VAR(final_ans_var)`.

This setup yields several benefits that are visible in practice:

1. The context window of the root LM is rarely clogged — because it never directly sees the entire context, its input context grows slowly.
2. The root LM has the flexibility to view subsets of the context, or naively recurse over chunks of it. For example, if the query is to find a needle-in-the-haystack fact or multi-hop fact, the root LM can use `regex` queries to roughly narrow the context, then launch recursive LM calls over this context. This is particularly useful for arbitrary long context inputs, where indexing a retriever is expensive on the fly! 
3. The context can, in theory, be any modality that can be loaded into memory. The root LM has full control to view and transform this data, as well as ask sub-queries to a recursive LM.

**Relationship to test-time inference scaling.** We are particularly excited about this view of language models because it offers another axis of scaling test-time compute. The trajectory in which a language model chooses to interact with and recurse over its context is entirely learnable, and can be RL-ified in the same way that reasoning is currently trained for frontier models. Interestingly, it does not directly require training models that can handle huge context lengths because **no single language model call should require handling a huge context**. 

**RLMs with REPL environments are powerful.** We highlight that the choice of the **environment** is flexible and not fixed to a REPL or code environment, but we argue that it is a good choice. The two key design choices of recursive language models are 1) treating the prompt as a Python variable, which can be processed programmatically in arbitrary REPL flows. This allows the LLM to figure out what to peek at from the long context, at test time, and to scale any decisions it wants to take (e.g., come up with its own scheme for chunking and recursion adaptively) and 2) allowing that REPL environment to make calls back to the LLM (or a smaller LLM), facilitated by the decomposition and versatility from choice (1).

We were excited by the design of CodeAct<d-cite key="wang2024executable"></d-cite>, and reasoned that adding recursive model calls to this system could result in significantly stronger capabilities — after all, LM function calls are incredibly powerful. However, we argue that RLMs fundamentally view LM usage and code execution differently than prior works: the **context** here is an object to be understood by the model, and code execution and recursive LM calls are a means of understanding this context efficiently. Lastly, in our experiments we only consider a recursive depth of 1 — i.e. the root LM can only call LMs, not other RLMs. It is a relatively easy change to allow the REPL environment to call RLMs instead of LMs, but we felt that for most modern “long context” benchmarks, a recursive depth of 1 was sufficient to handle most problems. However, for future work and investigation into RLMs, enabling larger recursive depth will naturally lead to stronger and more interesting systems. 

<details>
<summary><strong>The formal definition (click to expand)</strong></summary>
Consider a general setup of a language model $M$ receiving a query $q$ with some associated, potentially long context $C = {[c_1,c_2,…,c_m]}$. The standard approach is to treat $M(q,C)$ like a black box function call, which takes a query and context and returns some `str` output. We retain this frame of view, but define a thin scaffold on top of the model to provide a more <strong>expressive</strong> and <strong>interpretable</strong> function call $RLM_M(q,C)$ with the same input and output spaces.

Formally, a recursive language model $RLM_{M}(q, C)$ over an environment $\mathcal{E}$ similarly receives a query $q$ and some associated, potentially long context $C = [c_1,c_2,…,c_m]$ and returns some `str` output. The primary difference is that we provide the model a tool call $RLM_M(\hat{q}, \hat{C})$, which spawns an isolated sub-RLM instance using a new query $\hat{q}$ and a transformed version of the context $\hat{C}$ with its own isolated environment $\hat{\mathcal{E}}$; eventually, the final output of this recursive callee is fed back into the environment of the original caller.

The environment $\mathcal{E}$ abstractly determines the control flow of how the language model $M$ is prompted, queried, and handled to provide a final output. In this paper, we specifically explore the use of a Python REPL environment that stores the input context $C$ as a variable in memory. This specific choice of environment enables the language model to <strong>peek at</strong>, <strong>partition</strong>, <strong>transform</strong>, and <strong>map</strong> over the input context and use recursive LMs to answer sub-queries about this context. Unlike prior agentic methods that rigidly define these workflow patterns, RLMs defer these decisions entirely to the language model. Finally, we note that particular choices of environments $\mathcal{E}$ are flexible and are a generalization of a base model call: the simplest possible environment $\mathcal{E}_0$ queries the model $M$ with input query and context $q, C$ and returns the model output as the final answer.

</details>


### Limitations.

We did not optimize our implementation of RLMs for speed, meaning each recursive LM call is both blocking and does not take advantage of any kind of prefix caching! Depending on the partition strategy employed by the RLM’s root LM, the **lack of asynchrony** can cause each query to range from a few seconds to several minutes. Furthermore, while we can control the length / “thinking time” of an RLM by increasing the maximum number of iterations, we do not currently have strong guarantees about controlling either the total API cost or the total runtime of each call. For those in the systems community (*cough cough*, especially the [GPU MODE](https://www.youtube.com/@GPUMODE) community), this is amazing news! There’s so much low hanging fruit to optimize here, and getting RLMs to work at scale requires re-thinking our design of inference engines.


