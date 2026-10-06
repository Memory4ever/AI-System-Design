# 2601.09089v1 minimum necessary primary

Source https://arxiv.org/html/2601.09089v1 . Only4.1/4.2/limits and decisiveC2/C3 configurations; no alltask/inventory review. First fulltext transport capped70k was not a complete appendix read; C2/C3 re-retrieved by exact headings.

## §4.1/4.2/limits

4.1
How Does Test-Time Scaling Affects Sub-token Understanding?
Figure 4:
The effects of the number of thinking tokens on the task performance. Here we evaluate DS-distill-Qwen-2.5-7B on
Biological Sequence Manipulation
with the metric of normalized similarity.
Reasoning models have shown impressive capabilities across complex tasks, including
SubTokenTest
. This success is largely attributed to test-time scaling, where models generate extended thinking traces to deliberate over difficult problems, as also reflected in the token usage metrics in Table
2
. However, recent findings suggest that overly increasing reasoning length can trigger “overthinking”, leading to performance degradation. Empirical studies across various benchmarks have shown an inverted U-shaped relationship between reasoning length and accuracy: performance improves initially but eventually declines as reasoning chains become overly redundant
(
Marjanovic et al. 2025
;
Su et al. 2025
;
Ghosal et al. 2025a
;
Yang et al. 2025b
)
.
To investigate this effect within the sub-token domain, we follow
Ghosal et al. 2025b
and implement a Test-Time Budget Control (TTBC) method. We explicitly modulate the length of the model’s thinking trace by enforcing a strict token budget,
t
exact
t_{\text{exact}}
. If a model attempts to terminate its reasoning prematurely, we inject a continuation cue (e.g., “Wait”) to elicit further deliberation; conversely, traces exceeding the budget are truncated. We evaluate this on the
Biological Sequence Manipulation
task using DeepSeek-R1-Distill-Qwen-7B, measuring performance via a length-normalized similarity score based on Levenshtein distance. The TTBC, task datasets, and evaluation methods are detailed in Appendix
C.3
.
As shown in Figure
4
, our results confirm the presence of the inverse U-shaped curve in sub-token tasks. Performance peaks at a budget of approximately 2048 tokens before suffering a significant decline at higher budgets. We identify three distinct phases in this scaling behavior: an increasing phase (256-512 tokens) where additional reasoning improves performance; a plateau phase (1024-2048 tokens) characterized by stable performance as the model conducts thorough verification; and finally a decreasing phase (exceeding 2048 tokens) where overthinking leads to redundant reasoning that degrades accuracy. Detailed error analysis are provided in Appendix
E.2
.
4.2
Do LLMs Encode Character-level Information in Hidden States?
Figure 5:
The Macro F1 results of linear probing the last token of certain token sequences. The dot line is the experimental group, and the square line is the corresponding baseline trained with shuffled labels.
We conduct an interpretability analysis to examine how LLMs encode character-level information in the hidden representations across various input formats. In
SubTokenTest
, we cover multiple text forms, including normal words, typo words (
OCR-noise
), random letters (
keystroke
) and special symbols (
map-nav
,
RSA-diff
,
Gomoku
). We aim to probe the character-level information in each layer’s hidden states given these various forms of texts.
Probing Method.
We perform linear probing on the hidden representations of Qwen-2.5-7B-Instruct. Following the observation that the last token of a sequence typically aggregates information for preceding units
(
Kaplan et al. 2025
;
Wang et al. 2025a
)
, we extract the hidden states
h
ℓ
h_{\ell}
from the final token at each layer
ℓ
\ell
as our probing targets.
We frame the character-level awareness as a multi-character count prediction task. For a given input string, we define a dataset-specific alphabet
𝒜
\mathcal{A}
of size
|
𝒜
|
|\mathcal{A}|
. The goal of the probe is to predict the “bag-of-characters” count vector
y
=
(
y
1
,
y
2
,
…
,
y
|
𝒜
|
)
∈
ℕ
|
𝒜
|
y=(y_{1},y_{2},\dots,y_{|\mathcal{A}|})\in\mathbb{N}^{|\mathcal{A}|}
, where
y
m
y_{m}
represents the frequency of character
a
m
a_{m}
in the input. For each layer, we train a linear classifier to map
h
ℓ
h_{\ell}
to these counts, modeling the task as a
(
K
+
1
)
(K+1)
-way classification problem, where
K
K
is the maximum count observed. The probes are optimized using cross-entropy loss. To ensure the probes reflect actual representation rather than label memorization, we compare performance against a baseline trained on shuffled labels.
To evaluate the layer-wise “decodability” of this information, we use the Macro-averaged F1 score. We first calculate the F1 score for each character individually by averaging across all possible count classes, and then take the uniform average across the entire alphabet. More training and evaluation details are provided in Appendix
C.2
.
Results.
As illustrated in Figure
5
, the shuffled baselines maintain F1 scores around 0.16 across all four word types, which is substantially lower than the performance of the normally trained probes, confirming the effectiveness of the linear probing method. Across all sequence types, we observe a consistent pattern in how character-level information evolves across layers. In the embedding layer, the F1 score is predictably low, as the last token has not yet integrated information from the preceding tokens. However, character awareness of the whole word sequence surges significantly within the first 2–3 layers, suggesting a rapid internal reconstruction process.
After this initial peak, awareness slightly plateaus or declines until approximately the 20th layer. For typo words, special symbols, and random letters, we observe a secondary rise in F1 scores in these deeper layers, whereas the performance for normal words remains stable. Notably, the model’s internal representations consistently retain more information for normal words and special symbols than for typo words, which in turn outperform random letters. This hierarchy suggests that the model’s character-level “vision” is heavily influenced by the text forms, which partially explains why models struggle more with non-semantic (
keystroke decoding
) or perturbed token (
OCR-noise
) tasks.
5
Conclusions
We introduce
SubTokenTest
, a comprehensive benchmark designed to assess sub-token understanding in LLMs through real-world tasks. Through comprehensive evaluation, we reveal that large-scale reasoning models mitigate sub-token errors at a high token cost, and are sensitive to reasoning budgets, while smaller models exhibit poor performance. Additionally, we identify an inverted U-shaped relationship between reasoning effort and task performance in sub-token tasks. Moreover, probing results reveal how character-level information is encoded across model layers, with sub-token awareness evolving differently depending on the input format.
Limitations
While this work provides a comprehensive benchmark for assessing sub-token understanding in LLMs, it is important to note that we do not propose solutions for the challenges identified. Our goal is to evaluate the current state of LLMs’ ability to handle sub-token information, leaving further improvements for future work.
Additionally, our interpretability analysis is limited to a linear probe that provides some intuitions into how models process sub-token information. However, this approach does not fully explain the complete circuits by which models handle sub-token data throughout the entire process. A deeper, more comprehensive analysis of these circuits remains an open direction for future research.
Ethical Considerations
This work propose a new benchmark to test the sub-token un

## C2/C3 raw

{"positionsC2": [1727, 45667, 71565], "positionsC3": [1857, 45691, 78679], "length": 115936, "C2": "C.2\nNumber Linear Probe\nGoal.\nThe aim of number linear probe is to study where a pretrained language model encodes\ncharacter-count information\nabout an input string.\nLabel construction.\nLet\n\ud835\udc9c\n=\n{\na\n1\n,\n\u2026\n,\na\nM\n}\n\\mathcal{A}=\\{a_{1},\\ldots,a_{M}\\}\nbe a dataset-specific alphabet of size\nM\n=\n|\n\ud835\udc9c\n|\nM=|\\mathcal{A}|\n,\nand let\ng\n:\n\u03a3\n\u2217\n\u2192\n\u03a3\n\u2217\ng:\\Sigma^{\\ast}\\rightarrow\\Sigma^{\\ast}\nbe a preprocessing function (e.g., lowercasing or\nUnicode confusable normalization).\nFor an input string\nw\nw\n, we define its bag-of-characters count vector\ny\n(\nw\n)\n\u2208\n\u2115\nM\ny\nm\n(\nw\n)\n=\n\u2211\nc\n\u2208\ng\n\u2061\n(\nw\n)\n[\nc\n=\na\nm\n]\ny(w)\\in\\mathbb{N}^{M}\\quad y_{m}(w)\\;=\\;\\sum_{c\\in g(w)}\\mathbf{1}\\!\\left[c=a_{m}\\right]\\\\\nm\n\u2208\n{\n1\n,\n\u2026\n,\nM\n}\nm\\in\\{1,\\ldots,M\\}\n(7)\nLet\nK\n=\nmax\nw\n\u2208\n\ud835\udc9f\n\u2061\nmax\nm\n\u2208\n{\n1\n,\n\u2026\n,\nM\n}\n\u200b\ny\nm\n\u200b\n(\nw\n)\nK\\;=\\;\\max_{w\\in\\mathcal{D}}\\max_{m\\in\\{1,\\ldots,M\\}}y_{m}(w)\n(8)\ndenote the maximum count observed in the dataset\n\ud835\udc9f\n\\mathcal{D}\n.\nRepresentations.\nLet\nLM\n\\mathrm{LM}\nbe a frozen pretrained causal language model with\nL\nL\nlayers.\nGiven a tokenized and padded version of\nw\nw\n, let\nt\n\u2061\n(\nw\n)\nt(w)\ndenote the index of the\nfinal\nnon-padding token\n.\nWe extract, for each layer\n\u2113\n\u2208\n{\n0\n,\n1\n,\n\u2026\n,\nL\n}\n\\ell\\in\\{0,1,\\ldots,L\\}\n, the\nlast-token\nhidden state\nh\n\u2113\n\u200b\n(\nw\n)\n=\nH\n\u2113\n\u200b\n(\nw\n)\nt\n\u2061\n(\nw\n)\n\u2208\n\u211d\nd\nh_{\\ell}(w)\\;=\\;H_{\\ell}(w)_{t(w)}\\in\\mathbb{R}^{d}\n(9)\nwhere\nH\n\u2113\n\u200b\n(\nw\n)\n\u2208\n\u211d\nT\n\u00d7\nd\nH_{\\ell}(w)\\in\\mathbb{R}^{T\\times d}\nis the layer-\n\u2113\n\\ell\nhidden-state sequence\n(\n\u2113\n=\n0\n\\ell=0\ncorrespond to the embedding layer),\nT\nT\nis the padded sequence length,\nand\nd\nd\nis the hidden size.\nLinear probing.\nFor each layer\n\u2113\n\\ell\n, we train a\nlinear probe\nthat predicts the per-character counts from\nh\n\u2113\n\u200b\n(\nw\n)\nh_{\\ell}(w)\n.\nWe model each character count as a\n(\nK\n+\n1\n)\n(K+1)\n-way classification:\nz\n\u2113\n,\nm\n\u200b\n(\nw\n)\n=\nW\n\u2113\n,\nm\n\u200b\nh\n\u2113\n\u200b\n(\nw\n)\n+\nb\n\u2113\n,\nm\n\u2208\n\u211d\nK\n+\n1\nz_{\\ell,m}(w)\\;=\\;W_{\\ell,m}h_{\\ell}(w)+b_{\\ell,m}\\in\\mathbb{R}^{K+1}\n(10)\nwhere\nW\n\u2113\n,\nm\n\u2208\n\u211d\n(\nK\n+\n1\n)\n\u00d7\nd\nW_{\\ell,m}\\in\\mathbb{R}^{(K+1)\\times d}\nand\nb\n\u2113\n,\nm\n\u2208\n\u211d\nK\n+\n1\nb_{\\ell,m}\\in\\mathbb{R}^{K+1}\nare learned parameters.\nThe predicted count for character\na\nm\na_{m}\nis\ny\n^\nm\n\u200b\n(\nw\n)\n=\narg\n\u2061\nmax\nk\n\u2208\n{\n0\n,\n\u2026\n,\nK\n}\n\u200b\nz\n\u2113\n,\nm\n\u200b\n(\nw\n)\nk\n\\hat{y}_{m}(w)\\;=\\;\\arg\\max_{k\\in\\{0,\\ldots,K\\}}\\;z_{\\ell,m}(w)_{k}\ny\n^\n\u200b\n(\nw\n)\n=\n(\ny\n^\n1\n\u200b\n(\nw\n)\n,\n\u2026\n,\ny\n^\nM\n\u200b\n(\nw\n)\n)\n\\hat{y}(w)=\\bigl(\\hat{y}_{1}(w),\\ldots,\\hat{y}_{M}(w)\\bigr)\n(11)\nObjective.\nLet\n\u03b1\nm\n,\nk\n>\n0\n\\alpha_{m,k}>0\ndenote a class-imbalance weight for character\na\nm\na_{m}\nand count class\nk\n\u2208\n{\n0\n,\n\u2026\n,\nK\n}\nk\\in\\{0,\\ldots,K\\}\n.\nWe optimize a weighted cross-entropy objective over all characters and all samples:\n\u2112\n\u2113\n=\n\ud835\udd3c\nw\n\u223c\n\ud835\udc9f\n\u200b\n[\n1\nM\n\u200b\n\u2211\nm\n=\n1\nM\n\u03b1\nm\n,\ny\nm\n\u200b\n(\nw\n)\n\u22c5\nZ\n\u2113\n,\nm\n]\n\\mathcal{L}_{\\ell}\\;=\\;\\mathbb{E}_{w\\sim\\mathcal{D}}\\left[\\frac{1}{M}\\sum_{m=1}^{M}\\alpha_{m,y_{m}(w)}\\cdot Z_{\\ell,m}\\right]\nZ\n\u2113\n,\nm\n=\n\u2212\nlog\n\u2061\n[\nsoftmax\n\u2061\n(\nz\n\u2113\n,\nm\n\u200b\n(\nw\n)\n)\n]\ny\nm\n\u200b\n(\nw\n)\nZ_{\\ell,m}=-\\log\\bigl[\\mathrm{softmax}\\!\\left(z_{\\ell,m}(w)\\right)\\bigr]_{y_{m}(w)}\n(12)\nWe train\nf\n\u2113\n=\n{\n(\nW\n\u2113\n,\nm\n,\nb\n\u2113\n,\nm\n)\n}\nm\n=\n1\nM\nf_{\\ell}=\\{(W_{\\ell,m},b_{\\ell,m})\\}_{m=1}^{M}\nindependently for each layer\n\u2113\n\\ell\nwhile keeping\nLM\n\\mathrm{LM}\nfrozen.\nMetrics.\nWe evaluate layer-wise decodability using:\nMacro-averaged F1\n, computed per character and then averaged across characters detailed as below:\nFor each sample\ni\n\u2208\n{\n1\n,\n\u2026\n,\nN\n}\ni\\in\\{1,\\dots,N\\}\n, let the ground-truth count vector be\ny\n(\ni\n)\n\u2208\n{\n0\n,\n1\n,\n\u2026\n,\nK\n}\nM\ny^{(i)}\\in\\{0,1,\\dots,K\\}^{M}\nand the probe prediction be\ny\n^\n(\ni\n)\n\u2208\n{\n0\n,\n1\n,\n\u2026\n,\nK\n}\nM\n\\hat{y}^{(i)}\\in\\{0,1,\\dots,K\\}^{M}\n. For each character\na\nm\n\u2208\n\ud835\udc9c\na_{m}\\in\\mathcal{A}\n, define the confusion matrix\nC\n(\nm\n)\n\u2208\n\u2115\nV\n\u00d7\nV\nC^{(m)}\\in\\mathbb{N}^{V\\times V}\nwhose entries count how often the true count is\nt\nt\nand the predicted count is\np\np\n:\nC\nt\n,\np\n(\nm\n)\n=\n\u2211\ni\n=\n1\nN\n[\ny\nm\n(\ni\n)\n=\nt\n\u2227\ny\n^\nm\n(\ni\n)\n=\np\n]\nt\n,\np\n\u2208\n{\n0\n,\n\u2026\n,\nK\n}\nC^{(m)}_{t,p}\\;=\\;\\sum_{i=1}^{N}\\mathbf{1}\\!\\left[y^{(i)}_{m}=t\\;\\wedge\\;\\hat{y}^{(i)}_{m}=p\\right]\\quad t,p\\in\\{0,\\dots,K\\}\n(13)\nFor each class\nc\n\u2208\n{\n0\n,\n\u2026\n,\nK\n}\nc\\in\\{0,\\dots,K\\}\n, define:\nTP\nm\n,\nc\n=\nC\nc\n,\nc\n(\nm\n)\n\\mathrm{TP}_{m,c}\\;=\\;C^{(m)}_{c,c}\nPred\nm\n,\nc\n=\n\u2211\nt\n=\n0\nK\nC\nt\n,\nc\n(\nm\n)\n\\mathrm{Pred}_{m,c}\\;=\\;\\sum_{t=0}^{K}C^{(m)}_{t,c}\nTrue\nm\n,\nc\n=\n\u2211\np\n=\n0\nK\nC\nc\n,\np\n(\nm\n)\n\\mathrm{True}_{m,c}\\;=\\;\\sum_{p=0}^{K}C^{(m)}_{c,p}\n(14)\nFollowing the implementation, precision and recall are computed\nper class\n:\nPrec\nm\n,\nc\n=\nTP\nm\n,\nc\nPred\nm\n,\nc\nRec\nm\n,\nc\n=\nTP\nm\n,\nc\nTrue\nm\n,\nc\n\\mathrm{Prec}_{m,c}\\;=\\;\\frac{\\mathrm{TP}_{m,c}}{\\mathrm{Pred}_{m,c}}\\quad\\mathrm{Rec}_{m,c}\\;=\\;\\frac{\\mathrm{TP}_{m,c}}{\\mathrm{True}_{m,c}}\n(15)\nThen the per-character macro precision and macro recall are the uniform averages over classes:\nP\nm\n=\n1\nV\n\u200b\n\u2211\nc\n=\n0\nK\nPrec\nm\n,\nc\nR\nm\n=\n1\nV\n\u200b\n\u2211\nc\n=\n0\nK\nRec\nm\n,\nc\nV\n=\nK\n+\n1\nP_{m}\\;=\\;\\frac{1}{V}\\sum_{c=0}^{K}\\mathrm{Prec}_{m,c}\\quad R_{m}\\;=\\;\\frac{1}{V}\\sum_{c=0}^{K}\\mathrm{Rec}_{m,c}\\qquad V=K+1\n(16)\nThe per-character F1 is computed from\nP\nm\nP_{m}\nand\nR\nm\nR_{m}\n, and\nmacro-averaged F1\nF\n\u200b\n1\nmacro\nF1_{\\mathrm{macro}}\nis the uniform averages over characters:\nF\n\u200b\n1\nm\n=\n{\n2\n\u200b\nP\nm\n\u200b\nR\nm\nP\nm\n+\nR\nm\nif\n\u200b\nP\nm\n+\nR\nm\n>\n0\n0\notherwise\nF1_{m}\\;=\\;\\begin{cases}\\dfrac{2P_{m}R_{m}}{P_{m}+R_{m}}&\\text{if }P_{m}+R_{m}>0\\\\[8.0pt]\n0&\\text{otherwise}\\end{cases}\n(17)\nF\n\u200b\n1\nmacro\n=\n1\nM\n\u200b\n\u2211\nm\n=\n1\nM\nF\n\u200b\n1\nm\nF1_{\\mathrm{macro}}\\;=\\;\\frac{1}{M}\\sum_{m=1}^{M}F1_{m}\n(18)\nExperiment configurations.\nWe conduct number linear probing on Qwen2.5-7B-Instruct, keeping all base-model parameters frozen. We probe\nall\nlayers (layer\n0\n0\nto layer\n28\n28\n, including the embedding output and every transformer block), and we always extract the hidden representation at the\nfinal non-padding token\nposition.\nOur\nNormal dataset\ncontains\nN\n=\n39,831\nN=39{,}831\nEnglish words (cleaned from\nSCOWLv2\n\u2020\n\u2020\n\u2020\nhttps://github.com/en-wl/wordlist\n, a database on English words).\nPerturbed dataset\nreplaces each ASCII character in the normal dataset with a Unicode confusable counterpart with per-character probability\n0.9\n0.9\n(the same in the\nOCR-noise canonicalization\ntask);\nRandom dataset\nreplaces each word with a uniformly sampled lowercase string of identical length (over\na--z\n); and\nSpecial dataset\nreplaces each word with a uniformly sampled string of identical length from the symbol alphabet\n_PGO#Xo+=.B*-@%&\n\u02c6.\nFor every dataset variant, we additionally run a\nshuffle baseline\nin which the extracted representations are randomly permuted across samples to break input\u2013label alignment, yielding\n8\n8\ntotal runs.\nWe use the same train/test split for all runs with a\n0.9\n/\n0.1\n0.9/0.1\nratio, seeded by 20250315.\nFor each layer, we train an independent\nlinear probe\n(depth\n=\n1\n=1\n) with AdamW for\n200\n200\nepochs, batch size\n8192\n8192\n, and learning rate\n10\n\u2212\n3\n10^{-3}\n.\nTable 6:\nNumber linear probe experiment configurations.\nComponent\nSetting\nBase model\nQwen2.5-7B-Instruct\n(frozen)\nProbed layers\nAll layers\n\u2113\n\u2208\n{\n0\n,\n\u2026\n,\n28\n}\n\\ell\\in\\{0,\\ldots,28\\}\n(layer 0 for embedding)\nRepresentation\nHidden state at the\nfinal non-padding token\nposition\nTrain/test split\n0.9\n/\n0.1\n0.9/0.1\nProbe\nLinear probe (depth\n=\n1\n=1\n), trained independently per layer\nOptimizer\nAdamW\nEpochs\n200\n200\nBatch size\n8192\n8192\nLearning rate\n10\n\u2212\n3\n10^{-3}\nRandom Seed\n20250315\n20250315\n", "C3": "C.3\nTest-Time Budget Control (TTBC)\nGoal.\nOur goal is to study\ntest-time budget control\n(TTBC) for reasoning models by\nexplicitly controlling the length of the model\u2019s thinking trace\nat inference time, and to quantify how task accuracy changes as a function of the enforced thinking-token budget.\nFormulation.\nEach evaluation instance consists of an input prompt\nx\nx\nand (when available) a reference answer\ny\ny\n.\nWe prompt the model to produce a response that decomposes into a\nthinking segment\nz\nz\nand a\nfinal answer segment\na\na\n.\nLet\n\u03c4\n\u2061\n(\n\u22c5\n)\n\\tau(\\cdot)\ndenote the tokenizer mapping text to a token sequence.\nThe\nthinking-token budget\nis the length of the thinking segment in tokens:\nT\n\u225c\n|\n\u03c4\n\u2061\n(\nz\n)\n|\nT\\;\\triangleq\\;|\\tau(z)|\n(19)\nFormally, given\nx\nx\n, the model (with parameters\n\u03b8\n\\theta\n) produces a variable-length thinking trace\nz\n=\n(\nz\n1\n,\n\u2026\n,\nz\nT\n)\nz\\;=\\;(z_{1},\\ldots,z_{T})\n(20)\nfollowed by an answer\na\na\n.\nA\nTTBC controller\n\ud835\udc9e\n\\mathcal{C}\nspecifies an intervention rule that induces (i) a\nstopping time\nT\n\ud835\udc9e\n\u200b\n(\nx\n)\nT_{\\mathcal{C}}(x)\nfor the thinking phase and (ii) a controlled distribution over thinking traces.\nWe denote the resulting controlled thinking distribution by\np\n\u03b8\n,\n\ud835\udc9e\n(\nz\n1\n:\nT\n\u2223\nx\n)\np_{\\theta,\\mathcal{C}}(z_{1:T}\\mid x)\n, where\nT\n=\nT\n\ud835\udc9e\n\u200b\n(\nx\n)\nT=T_{\\mathcal{C}}(x)\n.\nAfter the controller terminates the thinking phase, the answer is generated conditional on the prompt and the realized thinking trace:\nz\n1\n:\nT\n\u223c\np\n\u03b8\n,\n\ud835\udc9e\n(\nz\n1\n:\nT\n\u2223\nx\n)\na\n\u223c\np\n\u03b8\n(\na\n\u2223\nx\n,\nz\n1\n:\nT\n)\nz_{1:T}\\sim p_{\\theta,\\mathcal{C}}(z_{1:T}\\mid x)\\qquad a\\sim p_{\\theta}(a\\mid x,z_{1:T})\n(21)\nFor each run, the realized thinking-token count\nT\n=\n|\n\u03c4\n\u2061\n(\nz\n)\n|\nT\\;=\\;|\\tau(z)|\n, the answer-token count\nA\n=\n|\n\u03c4\n\u2061\n(\na\n)\n|\nA\\;=\\;|\\tau(a)|\n,\nand task performance computed from the extracted answer content are recorded.\nExperiment configurations.\nWe evaluate TTBC mechanisms by\nExact Thinking Tokens\n, which enforces a strict thinking-token budget\nt\nexact\nt_{\\mathrm{exact}}\n.\nIf the model attempts to stop before reaching\nt\nexact\nt_{\\mathrm{exact}}\n, the controller injects the continuation cue (\n\"Wait\"\n) to elicit more thinking; if the model exceeds the remaining budget, the thinking trace is truncated such that the final thinking length satisfies\nT\n=\nt\nexact\nT=t_{\\mathrm{exact}}\n. After the thinking segment is terminated by the TTBC rule, the system transitions to answer generation process.\nTo be specific, we run TTBC on the\nBiological sequence manipulation\ntask (with sequence length set to 20), evaluating a fixed set of exact thinking budgets\nt\nexact\n\u2208\n{\n256,512\n,\n1024\n,\n2048\n,\n4096\n,\n8192\n,\n16384\n}\nt_{\\mathrm{exact}}\\in\\{256,512,1024,2048,4096,8192,16384\\}\ntokens. We report\nlength-normalized similarity score\nr\nnorm\nr_{\\mathrm{norm}}\nbased on the Levenshtein distance\nd\nlev\n\u200b\n(\ny\n^\n,\ny\n)\nd_{\\mathrm{lev}}(\\hat{y},y)\n:\nr\nnorm\n\u200b\n(\ny\n^\n,\ny\n)\n\u225c\n1\n\u2212\nd\nlev\n\u200b\n(\ny\n^\n,\ny\n)\nmax\n\u2061\n{\n|\ny\n^\n|\n,\n|\ny\n|\n}\nr_{\\mathrm{norm}}(\\hat{y},y)\\;\\triangleq\\;1-\\frac{d_{\\mathrm{lev}}(\\hat{y},y)}{\\max\\{|\\hat{y}|,|y|\\}}\n(22)\nwhere\n|\n\u22c5\n|\n|\\cdot|\ndenotes sequence length.\nTable 7:\nTTBC experiment configurations on biological sequence manipulation.\nComponent\nSetting\nModel\nDeepSeek-R1-Distill-Qwen-7B\nThinking segment\n<think> </think>\nAnswer segment\n<answer> <answer>\nContinuation cue\n\u201cWait\u201d\nThinking budget\n{\n256,512\n,\n1024\n,\n2048\n,\n4096\n,\n8192\n,\n16384\n}\n\\{256,512,1024,2048,4096,8192,16384\\}\ntokens\nTemperature\n0\n0\nSamples\n100\n100\nThink length limit\n32000\nAnswer length limit\n2048\nRandom seed\n0\n0\nAppendix D\nSupplementary Experiment Results\nD.1\nDetails of Reasoning Model Budget\nWe list the detailed comparison of the performance of o4-mini (low) and o4-mini (high) in Figure\n20\nand Table\n8\n.\nWe define three key metrics to quantify the trade-offs: (1)\nRelative Reasoning Token Change (RRTC)\nmeasures the percentage reduction in reasoning tokens when switching from high to low budget, calculated as\nRRTC\n=\n(\ntokens\nhigh\n\u2212\ntokens\nlow\n)\n/\ntokens\nhigh\n\u00d7\n100\n%\n\\text{RRTC}=(\\text{tokens}_{\\text{high}}-\\text{tokens}_{\\text{low}})/{\\text{tokens}_{\\text{high}}}\\times 100\\%\n; (2)\nRelative Performance Change (RPC)\nquantifies the performance impact, computed as\nRPC\n=\n(\nperf\nhigh\n\u2212\nperf\nlow\n)\n/\nperf\nhigh\n\u00d7\n100\n%\n\\text{RPC}=(\\text{perf}_{\\text{high}}-\\text{perf}_{\\text{low}})/{\\text{perf}_{\\text{high}}}\\times 100\\%\n; (3)\nReasoning Ratio Retention\nindicates the proportion of reasoning capacity retained in the low budget setting, defined as\nRR\nlow\n/\nRR\nhigh\n\u00d7\n100\n%\n\\text{RR}_{\\text{low}}/{\\text{RR}_{\\text{high}}}\\times 100\\%\n, where RR denotes the reasoning ratio.\nFor most tasks, decreasing reasoning tokens leads to an obvious decline in o4-mini\u2019s performance. However, we observe that in certain tasks, such as Keystroke and Safety-mask, reducing reasoning tokens does not result in a substantial performance drop. This suggests the presence of overthinking issue, where the model allocates more computational resources than necessary for optimal performance.\nFigure 20:\nRelative changes in reasoning tokens, performance, and reasoning ratio retention between o4-mini (high) and o4-mini (low) across benchmark tasks. Bars show relative reductions in reasoning tokens (tan) and performance (blue), while the red line indicates reasoning ratio retention.\nTable 8:\no4-mini (high/low) Performance, Avg. Completion Tokens, and Reasoning Ratio\nBenchmark Task\nScore\nAvg. Completion Tokens\nReasoning Ratio\no4-mini (high)\no4-mini (low)\no4-mini (high)\no4-mini (low)\no4-mini (high)\no4-mini (low)\nOCR-noise\n47%\n20%\n3325\n619\n75.3%\n31.2%\nTable\n59%\n34%\n23276\n2436\n94.6%\n60.2%\nBio-seq\n98%\n86%\n3768\n1447\n90.1%\n75.9%\nCipher & Decipher\n38%\n14%\n24118\n3404\n98.3%\n84.4%\nSafety-mask\n88%\n86%\n3563\n895\n93.1%\n72.7%\nGomoku (linear)\n97%\n77%\n10816\n1827\n97.0%\n75.0%\nGomoku (diagonal)\n97%\n42%\n15259\n2310\n95.7%\n80.7%\nMap-Nav(Sokoban)\n89%\n74%\n1423\n1076\n71.6%\n65.8%\nMap-Nav(FrozenLake)\n87%\n79%\n890\n751\n60.4%\n55.3%\nRsa-diff (Avg. F1 score)\n0.9456\n0.5760\n7237\n2744\n99.1%\n81.5%\nTree (Tree Structure)\n95%\n83%\n3914\n1694\n94.3%\n89.2%\nTree (Tree Path)\n90%\n72%\n20"}

