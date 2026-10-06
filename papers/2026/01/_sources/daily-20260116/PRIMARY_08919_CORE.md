# 2601.08919v1 minimum necessary primary

ExactHTML https://arxiv.org/html/2601.08919v1 . Selected actual methods/keyevaluation/directlimits only; no complete-appendix or runtime claim.

3. 
Fine-grained evaluation of LLMs-as-judges
3.1. 
Background: the INEX Wikipedia collection
The principal objective of the ad hoc track at
INEX 
(
14
; 
5
)
, the Initiative for the Evaluation of XML
Retrieval, was 
focused retrieval
: given a large collection of
semi-structured (XML) documents, and a query, to return a list of document
excerpts or passages (as opposed to full documents) that precisely
address the user’s information need.
Ground truth was created by asking assessors to mark or highlight “all,
and only, relevant text in a pool of documents” 
(
14
)
 retrieved
by participating systems for each query. As expected, systems were evaluated
on the basis of their ability to return all, and only, highlighted text.
For 2009 and 2010, the INEX ad hoc test collections were constructed using
a dump of Wikipedia from October 2008, and user queries that cover a wide
variety of topics of general interest. In order to ascertain whether
LLMs-as-judges agree with humans about which parts of a relevant document
are actually useful, we naturally turned to these collections.
3.2. 
Prompt structure
Figure 1
. 
Structure of our prompt. For Example 7, which corresponds to the
test instance, the query, narrative and document are provided; the LLM
is instructed to provide the relevant excerpts from the document. We
highlight the rationale (relevant passage) within the document for the
reader’s convenience.
When prompting LLMs, we adopt the general approach used in recent
work 
(
27
; 
28
; 
26
)
, but modify it to
obtain highlighted passages or rationales from LLMs. Following convention,
our prompt starts with a description of the task to be performed. The
principal difference (compared
to 
(
27
; 
28
; 
26
)
) is that our 
k
k
-shot
prompt includes exemplars to illustrate what we want (in the literature,
this process is referred to as 
In-Context Learning (ICL)
 
(
8
; 
7
)
, and does
not involve updating model parameters). More specifically, we provide 
k
k
query-document pairs (
k
k
 is determined by the prompt size budget). Each
pair is followed by an excerpt that is constructed by concatenating all
passages within the document that are relevant for the given query.
The important components of a prompt are shown in Figure 
1
.
Formally, let 
ℰ
=
{
(
x
i
,
y
i
)
}
i
=
1
k
\mathcal{E}=\{(x_{i},y_{i})\}_{i=1}^{k}
 denote the exemplars,
with each 
(
x
i
,
y
i
)
(x_{i},y_{i})
 representing the 
i
t
​
h
i^{th}
 input-output pair. In our
setup, each 
x
i
x_{i}
 consists of three components: the query description
(
Q
desc
Q^{\text{desc}}
), the query narrative (
Q
narr
Q^{\text{narr}}
), and the
document content (
D
D
); 
y
i
y_{i}
 (equivalently 
D
exp
D^{\text{exp}}
) is an excerpt
corresponding to the highlighted portion(s) of 
D
D
, as described above.
The test instance, denoted 
(
x
test
,
y
test
)
(x_{\text{test}},y_{\text{test}})
, has the
same structure as an input-output pair, with 
y
test
y_{\text{test}}
 being the
desired (ground truth) output. As shown in Figure 
1
, the
prompt consists of the task description, exemplars (
ℰ
\mathcal{E}
) and
x
test
x_{\text{test}}
. It is well known that the selection and ordering of
exemplars in 
ℰ
\mathcal{E}
 play a crucial role in determining the accuracy
of the predictions 
(
18
)
. We plan to undertake
a rigorous analysis of these factors in the near future.
The LLM’s prediction, 
y
^
\hat{y}
, is given by
y
^
=
LLM
​
[
(
x
1
,
y
1
)
⊕
…
⊕
(
x
k
,
y
k
)
⊕
x
test
]
,
\hat{y}=\text{LLM}[(x_{1},y_{1})\oplus\ldots\oplus(x_{k},y_{k})\oplus x_{\text{test}}],
where 
⊕
\oplus
 denotes concatenation.
These predictions are generated from the LLM using a greedy decoding strategy 
(
30
)
. We stop generating the sequence once we reach a
predefined maximum length.
We then apply post-processing to the predicted output, 
y
^
\hat{y}
, as
in 
(
20
)
: regular-expression matching and filtering techniques
are employed to remove irrelevant segments of the generated output (e.g.,
prefixes such as “
Explanation:
”). Finally, the ground-truth
highlighted explanation 
y
test
y_{\text{test}}
 is compared with the
corresponding LLM-generated explanation 
y
^
\hat{y}
 to compute recall and
precision. This is described in detail in Section 
4.1
.
3.3. 
Predicting relevance at the document level
In principle, the document-level relevance prediction task could be
subsumed by the rationale-generation task. A document for which no
rationale is generated would then be labelled non-relevant. However, we
feel that this formulation of the task makes it unnecessarily difficult.
Any prompt designed for this purpose may be at least somewhat suggestive of
a trick-question. Thus, in addition to generating rationales
(described above in Section 
3.2
), we also use LLMs to predict
document-level relevance.
Our experiments in this direction serve two purposes. First, they provide
the necessary background against which the results of rationale generation
should be interpreted. Second, they make it easier to contextualize our
findings in terms of other work that has investigated LLMs-as-judges in an
IR setting. As discussed in Section 
2
, these related
studies have all considered this task, in spite of having varied
objectives.
We adopt an approach that is commonly
used 
(
27
; 
28
; 
26
; 
15
)
. The main
difference with our method for rationale generation is that we use a
zero-shot, instruction-only prompt. This prompt includes only a query, its
detailed description and narrative, and a document, and asks the LLM to
classify the document as relevant/non-relevant. For open-source models, we
obtain the LLM-predicted class probabilities, whereas for closed-source
models, we receive a simple 
yes/no
 response indicating whether the
document is relevant to a particular query.
4. 
Experimental setup
As mentioned in Section 
3.1
, we use the INEX 2009 and 2010 ad
hoc track test collections for our experiments. Both collections use the
same Wikipedia-based document collection, consisting of 2,666,190 articles.
The original INEX collection can be downloaded
from 
https://www.mpi-inf.mpg.de/departments/databases-and-information-systems/software/inex/
.
To the best of our knowledge,
1
1
            
1
            
            
          Based on personal communication with
the organizers of INEX.
 this is currently the only available source for
the INEX benchmark collection. Table 
1
 presents a
brief summary of some statistics about these datasets; additional details
can be found in 
(
14
; 
5
)
.
For our experiments, we discard all XML markup and semantic annotations
from the Wikipedia articles, and extract the plain textual content using a
standard XML parser (libxml2). A total of 115 and 107 queries
(
topics
, in TREC terminology) were created for INEX 2009 and 2010,
respectively, but out of these, 68 queries were judged for INEX 2009, while
52 queries were judged for INEX 2010. We use these 68 + 52 queries for our
experiments.
The document pools were constructed from a total of 172 runs submitted to
INEX 2009, and 148 submissions for INEX 2010. A total of 4,858 and 5,471
relevant articles, respectively, were found relevant for the 68 + 52
queries that were judged for INEX 2009 and 2010. Out of the 4,858 relevant
documents in the INEX 2009 collection, 3,339 (just under 69%) contain only
a single highlighted passage; the corresponding figure for INEX 2010 is
3,388 documents out of 5,471 (about 62%).
Table 1
. 
Statistics of the INEX adhoc datasets used in our experiments.
Dataset
#Topics
#Judg. Topics
#Rel.
#System runs
INEX 2009
115
68
4858
172
INEX 2010
107
52
5471
148
4.1. 
Evaluation metrics
Our task prompts an LLM to produce a single relevant excerpt from the
document for a given query-document pair. In contrast, the metrics used at
INEX were formulated for systems producing a ranked list of document
passages in response to each query. Thus, these metrics are not applicable
in our setting. To assess the quality of the output produced by an LLM
(denoted 
y
^
\hat{y}
 in Section 
3.2
), we compute the overlap
between the model’s outputs and the ground truth annotations (denoted
D
exp
D^{\text{exp}}
). This overlap is used to measure 
precision
 and
recall
, which respectively indicate the relevance of the generated
content, and the completeness of the information captured by the LLM.
However, some operational issues need to be addressed before the overlap
can be precisely computed.
Measuring the overlap between LLM output and ground truth
We may view the original document 
D
D
 as a sequence of characters. The
ground truth, 
D
exp
D^{\text{exp}}
, is 
necessarily
 a subsequence of 
D
D
.
Because 
y
^
\hat{y}
 represents content generated by an LLM, it is not
guaranteed to have this property. In principle, an LLM could paraphrase
document content (e.g., to increase succinctness or clarity, as judged by
the LLM itself), or even synthesize text that is semantically a subset of
the document content without corresponding to any easily identifiable
subsequence. We hope to avoid such scenarios by setting the ‘temperature’
parameter of the LLM to 0 during rationale generation, as this is expected
to minimise the ‘creativity’ or ‘inventiveness’ of the LLM. Further, since
all the exemplars provided to the LLM are subsequences, we assume that the
output will also be in the same form. A manual inspection of some randomly
selected outputs suggests that our assumption is a safe one. However, a
more rigorous test of this hypothesis is needed.
A second issue is the following. Given a text file (either with or without
markup), any contiguous highlighted passage can be unambiguously identified
via its starting byte offset and length. Indeed, the ground truth provided
by INEX uses this format. The qrel file contains one line for each

4.1. 
Evaluation metrics
Our task prompts an LLM to produce a single relevant excerpt from the
document for a given query-document pair. In contrast, the metrics used at
INEX were formulated for systems producing a ranked list of document
passages in response to each query. Thus, these metrics are not applicable
in our setting. To assess the quality of the output produced by an LLM
(denoted 
y
^
\hat{y}
 in Section 
3.2
), we compute the overlap
between the model’s outputs and the ground truth annotations (denoted
D
exp
D^{\text{exp}}
). This overlap is used to measure 
precision
 and
recall
, which respectively indicate the relevance of the generated
content, and the completeness of the information captured by the LLM.
However, some operational issues need to be addressed before the overlap
can be precisely computed.
Measuring the overlap between LLM output and ground truth
We may view the original document 
D
D
 as a sequence of characters. The
ground truth, 
D
exp
D^{\text{exp}}
, is 
necessarily
 a subsequence of 
D
D
.
Because 
y
^
\hat{y}
 represents content generated by an LLM, it is not
guaranteed to have this property. In principle, an LLM could paraphrase
document content (e.g., to increase succinctness or clarity, as judged by
the LLM itself), or even synthesize text that is semantically a subset of
the document content without corresponding to any easily identifiable
subsequence. We hope to avoid such scenarios by setting the ‘temperature’
parameter of the LLM to 0 during rationale generation, as this is expected
to minimise the ‘creativity’ or ‘inventiveness’ of the LLM. Further, since
all the exemplars provided to the LLM are subsequences, we assume that the
output will also be in the same form. A manual inspection of some randomly
selected outputs suggests that our assumption is a safe one. However, a
more rigorous test of this hypothesis is needed.
A second issue is the following. Given a text file (either with or without
markup), any contiguous highlighted passage can be unambiguously identified
via its starting byte offset and length. Indeed, the ground truth provided
by INEX uses this format. The qrel file contains one line for each judged
query-document pair; an example is shown in Figure 
2
. Apart
from the query and document identifiers, the line contains the total amount
of highlighted text in bytes, and a list of one or more 
⟨
\langle
starting
offset, length
⟩
\rangle
 pair(s) corresponding to the highlighted
passage(s).
2
2
2
              A non-relevant document can be easily identified
because the total amount of highlighted text in it is 0.
2009001 Q0 1528075 49158 58542 126 126:28761 28893:20397
Figure 2
. 
A line from an INEX 2009 qrel file
We do not expect a general purpose LLM to be able to learn this format from
a few in-context examples; it generates only plain text as 
y
^
\hat{y}
. We
then need to map each 
y
^
\hat{y}
 to one or more substrings of the
corresponding document. For this, we employ the pattern-matching algorithm
proposed in 
(
23
)
. This algorithm identifies the
longest common subsequences (at the word level) between the document and
the LLM-generated output. Since this algorithm matches 
word
sequences, one final implementation detail involves aligning character
offsets and their corresponding word
positions.
Once the LLM’s output for a query-document pair is mapped to subsequences
of the document, it is straightforward to compute the overlap between
ground truth annotations and the LLM’s output, and in turn, recall,
precision and F
1
 scores.
When presenting aggregate figures in the next section, we compute averages
at both the macro and micro levels. The micro-averages are calculated by
directly averaging over 
all
 query-document pairs (4,858 pairs for
INEX 2009, and 5,471 pairs for INEX 2010), without grouping these pairs by
query. For macro-level evaluation (see Equations 1 and 2), we first
calculate the average value of a measure across all query-document pairs
for each query 
Q
Q
. The mean of these values across all judged topics,
i.e., of 68 values for INEX 2009, and 52 values for INEX 2010, is reported.
(1)
Precision
macro
=
1
|
Q
|
​
∑
q
=
1
|
Q
|
Precision
q
\displaystyle\text{Precision}_{\text{macro}}=\frac{1}{|Q|}\sum_{q=1}^{|Q|}\text{Precision}_{q}
(2)
Recall
macro
=
1
|
Q
|
​
∑
q
=
1
|
Q
|
Recall
q
\displaystyle\text{Recall}_{\text{macro}}=\frac{1}{|Q|}\sum_{q=1}^{|Q|}\text{Recall}_{q}
(
|
Q
|
|Q|
 denotes the total number of judged topics).
4.2. 
Models used
For extracting relevant / explanatory segments from documents, we employed
Llama 3.1
8B-Instruct
3
3
3
https://ai.meta.com/blog/meta-llama-3-1/
 and
GPT-4.1-mini
4
4
4
https://platform.openai.com/docs/models/gpt-4.1-mini
.
According to 
https://platform.openai.com/docs/models
, GPT-4.1 is
OpenAI’s smartest non-reasoning model, and GPT-4.1 mini is a “smaller,
faster version of GPT-4.1”. It thus represents a good choice for us, given
our budgetary constraints.
Following standard practice, for the document-level relevance
prediction task, the parameters of Llama 3.1 8B-Instruct were configured
as 
top-
k
=
50
k=50
 and 
temperature
=
3.0
=3.0
. For
explanation extraction using this smaller model, the settings were 
temperature
=
1.0
=1.0
, 
top-
k
=
50
k=50
, and 
top-
p
=
1.0
p=1.0
. For GPT-4.1-mini,
a much larger and potentially more creative model,
we set the 
temperature
 to 
0
0
 and 
top-
p
p
 to 
1
1
,
enabling more deterministic outputs. In preliminary experiments with
reasoning-oriented models such as
GPT-5
5
5
5
https://platform.openai.com/docs/models/gpt-5
 and
DeepSeek-Reasoner
(DeepSeek-V3.1-Terminus)
6
6
6
https://api-docs.deepseek.com/guides/reasoning_model
,
we observed that these models demonstrate explicit reasoning traces when
identifying relevant segments within documents. However, they often fail to
accurately highlight the exact spans of relevant tokens suited to our task.
Furthermore, as document length increases, their consistency in
highlighting relevant portions deteriorates. Investigating how reasoning
models can be better leveraged for this task remains an important direction
for future work.
5. 
Experimental results
As discussed in Se

5.2. 
Main results
Next, we turn to our main results, which focus on the fine-grained
evaluation of LLMs-as-Judges via rationale generation. As described in
Section 
3
, we employ in-context learning (ICL) to identify
and highlight the relevant portions of each document in a query-document
pair. Note that document lengths vary substantially in the Wikipedia
corpus. For instance, the smallest relevant document in INEX 2009 is 204
bytes, while the largest is 159,845 bytes. To account for this variation,
we construct three distinct sets of exemplars based on the length of the
document. In the first exemplar set (Exemplar
1
), the documents are very
short; in the second set (Exemplar
2
), longer documents are randomly
sampled for inclusion in the prompt; and in the third set (Exemplar
3
),
the documents are of intermediate length. We fix the exemplar budget to 
k
=
6
k=6
 for all three exemplar sets. The precision (P), recall (R), and F
1
scores at both the macro and micro levels are reported in
Table 
4.1
 for the Llama-3.1-8B and GPT-4.1-mini models.
Table 4
. 
Performance of three exemplar configurations (Exemplar
1
, Exemplar
2
, and Exemplar
3
) on the INEX 2009 and INEX 2010 datasets for Llama-3.1-8B and GPT-4, respectively. We report both macro- and micro-level evaluations using Precision (P), Recall (R), and F
1
 scores on these two collections.
Model
INEX 2009
INEX 2010
Macro
Micro
Macro
Micro
P
R
F
1
P
R
F
1
P
R
F
1
P
R
F
1
Exemplar
1
 (Llama-3.1-8B)
0.4501
0.6793
0.4997
0.5634
0.6681
0.6113
0.3547
0.6658
0.5136
0.5172
0.6480
0.5753
Exemplar
1
 (GPT-4.1-mini)
0.6231
0.7146
0.6415
0.6185
0.7162
0.6638
0.5774
0.7425
0.6234
0.6117
0.7494
0.6736
Exemplar
2
 (Llama-3.1-8B)
0.4622
0.7152
0.5176
0.5226
0.7055
0.6004
0.3684
0.6912
0.5312
0.4691
0.6962
0.5605
Exemplar
2
 (GPT-4.1-mini)
0.5740
0.7988
0.6432
0.5784
0.8091
0.6746
0.5074
0.8263
0.6019
0.5282
0.8364
0.6475
Exemplar
3
 (Llama-3.1-8B)
0.3967
0.5945
0.4387
0.5052
0.6096
0.5525
0.3371
0.6079
0.4472
0.4572
0.5962
0.5175
Exemplar
3
 (GPT-4.1-mini)
0.6210
0.6644
0.6182
0.6107
0.6664
0.6373
0.5887
0.6753
0.6080
0.6142
0.7023
0.6553
Performance on the smaller LLM
We begin our analysis with the results obtained using the smaller model, Llama-3.1-8B. For this model, the maximum generation length is configured to match the length of each document.
Overall, Exemplar
2
 yields the highest precision and recall scores across
both the INEX 2009 and INEX 2010 collections, consistently outperforming
the other exemplar configurations across all macro- and micro-level
measures (we do not conduct statistical significance testing, as our objective is not to design or optimize an algorithm for exemplar selection).
Specifically, at the macro level, the precision, recall, and F
1
 scores are 
0.4622
0.4622
, 
0.7152
0.7152
, and 
0.5176
0.5176
 for INEX 2009, and 
0.3684
0.3684
, 
0.6912
0.6912
, and 
0.5312
0.5312
 for INEX 2010.
At the micro level, the corresponding values are 
0.5226
0.5226
, 
0.7055
0.7055
, and 
0.6004
0.6004
 for INEX 2009, and 
0.4691
0.4691
, 
0.6962
0.6962
, and 
0.5605
0.5605
 for INEX 2010.
In general, the micro-level precision scores are higher than their macro-level counterparts. This difference arises because micro-level measures assign uniform weight across all query–document pairs, whereas macro-level measures assign equal weight to each query.
Consequently, queries with only a few relevant documents—and correspondingly lower precision—tend to reduce the overall macro-level performance.
It is noteworthy that the recall scores are generally higher than the precision values.
To further investigate this trend, we examine the ratio between the lengths
of the generated rationales and the corresponding full document lengths.
Figure 
3
 presents the histograms of these ratios for both collections using Exemplar
2
.
For INEX 2009, the model highlights more than half of the document in 3,922 out of 4,858 cases (approximately 
80.7
%
80.7\%
), whereas for INEX 2010, this occurs in 3,808 out of 5,471 cases (approximately 
69.6
%
69.6\%
).
This observation indicates a tendency of the model to over-highlight document content, thereby inflating recall scores.
In the limiting case where the model highlights the entire document, the recall would trivially reach 
1.0
1.0
.
(a)
Histogram showing the fraction of each document that is highlighted for INEX 2009.
(b)
Histogram showing the fraction of each document that is highlighted for INEX 2010.
Figure 3
. 
Distribution of generated content lengths relative to document lengths across INEX 2009 and 2010 using Exemplar
2
.
Performance on the larger model.
Next, we analyze the performance of the larger model (GPT-4.1-mini) for the three exemplar sets.
Due to budget constraints, the maximum generation length for this larger model was limited to 
8192
8192
.
This value was chosen based on the empirical distribution of ground-truth highlighted chunk lengths, ensuring coverage of almost all observed document fractions.
When transitioning from Llama-3.1-8B to GPT-4.1-mini, we observe a clear improvement in precision, which in turn leads to higher F
1
 scores.
Specifically, on INEX 2009, the highest macro-level precision increases from 
0.4622
0.4622
 to 
0.6231
0.6231
 (a relative gain of 
34.8
%
34.8\%
), while the micro-level precision improves from 
0.5226
0.5226
 to 
0.6185
0.6185
 (an 
18.3
%
18.3\%
 increase).
A similar trend is observed for INEX 2010, indicating the expected performance gains with a larger and more parameter-rich model.
Interestingly, while Exemplar
2
 consistently outperformed the other configurations with Llama-3.1-8B, GPT-4.1-mini exhibits a different trend—Exemplar
1
 and Exemplar
3
 achieve comparable or even superior performance relative to Exemplar
2
.
This observation aligns with prior findings by 
18
, who argued that prompts effective for smaller models may not necessarily yield the same benefits when scaled to larger models within the same family.
Needle in haystack observation
We further analyze the interaction between document length, the fraction of ground-truth relevant content, and the fraction of model-generated highlights with respect to precision.
We sort all query–document pairs by document length and partition them into bins.
For each bin, we compute and plot the precision score, the average fraction of ground-truth relevant content, and the average fraction of generated highlights.
Figure 
4
 presents these histograms for the INEX 2009 collection using Exemplar
2
.
The number of bins was determined using 
Rice’s Rule
(
10
; 
24
)
 as 
k
=
2
​
n
1
/
3
k=2n^{1/3}
, where 
n
n
 is the number of observations.
Additional plots generated using the GPT-4.1-mini model on INEX 2010 are presented in Appendix 
A
.
As observed in Figure 
4
, when only a small fraction of the document is relevant (e.g., bins 
10
10
–
15
15
 and around 
25
25
), the precision scores tend to be lower.
This trend becomes particularly evident for longer documents, where the model struggles to identify the small relevant portions accurately.
Figure 4
. 
Distribution of document length vs precision, document length vs fraction of gold chunks, document length vs fraction of generated portions for
the INEX 2009 dataset using Exemplar
2
 with Llama-3.1-8B model. The number of bins was determined using Rice’s Rule (
k
=
2
​
n
1
/
3
k=2n^{1/3}
).
Contiguous vs discontiguous chunks.
We divide the relevant set into two subsets: one containing documents in which the relevant content appears as a single, contiguous chunk, and the other containing documents having multiple, disjoint passages with relevant information. We observe that LLMs tend to struggle more when a document has discontiguous, relevant chunks. This behavior is consistent across both models. For instance, Llama-3.1-8B achieves a macro-level precision of 
0.4691
0.4691
 on the discontiguous set, while this increases to 
0.5462
0.5462
 on the contiguous set for INEX 2009 with Exemplar
2
. Similarly, GPT-4.1-mini obtains macro-level precisions of 
0.4951
0.4951
 and 
0.6163
0.6163
 on the discontiguous and contiguous sets, respectively, using Exemplar
2
. We observe similar trends across oth

Hallucination.
Recall that each test case is included (with a blank Explanation field) in
the prompt as Example 7. We observe that the Llama-3.1-8B model sometimes
generates an 
Example 8
 in addition to the expected rationale. This
superfluous content is eliminated during post-processing, and is not
reflected in the reported figures. However, it may be regarded as a sign of
hallucination, and is observed for Exemplar
2
 in 665/4,858 cases
(approximately 13.6%) in INEX 2009, and in 880/5,471 cases (approximately
16%) in INEX 2010 (for other exemplar sets, similar or even higher
proportions were observed). In contrast, such behavior is not observed in
GPT-4.1-mini across either collection.
Anecdotal analysis.
The authors of this paper noted that only a single query in the INEX 2009 collection involves finding images of specific objects or entities. Specifically, the description of this query is “Find images of sunflowers painted by Vincent van Gogh” (query ID: 2009065). The narrative version of the query is provided below:
Being a Dutch post-impressionist artist, Vincent van Gogh produced many paintings that are now very popular, well-known, and valuable. His painting style has significantly influenced the development of modern art. Among his works, I particularly appreciate the various depictions of sunflowers for their vibrant colors, which express emotions typically associated with the life of sunflowers. I would like to find relevant sunflower paintings as images in documents so that I can enjoy their simplistic beauty. To be relevant, the sunflower must be presented as an image and painted by Vincent van Gogh. Sunflower images created by others are irrelevant.
As this collection consists exclusively of 
text
 documents, we do not explicitly handle image-based content. If an LLM is nevertheless able to infer or identify such image-related references, it would constitute a noteworthy success for the 
LLMs-as-Judges
 paradigm. For this particular query, the highest achievable precision for GPT-4.1-mini is 
0.4972
0.4972
, while that for Llama-3.1-8B is 
0.2462
0.2462
. Interestingly, the Llama-3.1-8B model attains a much higher recall of 
0.9039
0.9039
, compar
