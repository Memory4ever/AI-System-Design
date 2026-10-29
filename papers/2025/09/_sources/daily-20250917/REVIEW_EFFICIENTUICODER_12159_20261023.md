# EfficientUICoder 2509.12159v1: claim-bounded necessary first package

## Ownership And Identity

Daily2025-09-17补Sep16 BJT。作者166明确未GET/未Methods/无在途单让，L217接受，仅本首次必要Source；177/作者136完整AB、exact-v1/day/current有效层复用，不第三。v1标题为 **EfficientUICoder: Efficient MLLM-based UI Code Generation via Input and Output Token Compression**；后版标题不回填。

- Primary: https://arxiv.org/html/2509.12159v1
- Saved: `REVIEW_SOURCE_12159V1_20261023.raw` / `.headers` / `.request.json`
- Actual single GET: 200/exit0/441688B/0.767540s.
- SHA256: `d0aeee05d1191de0495686e385d76e5b6fa4bbe2ee9719b6514b673bd736c151`.
- Request clock observations UTC2026-10-23 18:04:01–02, alreadyBJT10/24; second-resolution observations not fabricated exact request times. Filename remains this ongoing daily log convention.

## Intended Claim And Stop

Claim fixed before Methods: visual-support selection and output-code repetition suppression are different compression responsibilities, with possible loss of necessary evidence or valid structure. Core method/direct ablation, measured end-to-end cost and key counterevidence suffice. Actual read S4 core/E3–9/Algorithms1–3; S5 models/data/metrics/baselines; S6.1 direct quality Table2 and human-evaluation text/captions, S6.2 cost Table3, S6.3 ablation Table4; S7 limitations. E9 revisited only to resolve the specific suppression-direction dispute. No S3 full exploratory analysis, S6.4 parameter sweep/S6.5 cases, figure pixels, code, renderer/browser/LLM execution or reproduction. Those nonnecessary boundaries are not ordinary work or external holds.

## Mechanism And Positive Evidence

UIED proposes text/image/component boxes, merges nearby text fragments, retains containing boxes or enclosing rectangles for overlap. All-pair boundary distances become graph edges; Kruskal MST minimizes edge-length sum. This is a geometric proposal, not a proof that every semantic element survived or that distance minimizes selected pixel/token area. The actual mapping is not silently completed into a new rendering recipe.

Within the already encoded image, head-averaged CLS attention removes low-ranked tokens from selected regions and adds high-ranked tokens from unselected regions. Background color can matter although outside detected objects. This is not new observation or a semantic sufficiency certificate; fractions over different set sizes are not automatically equal token counts.

Output parsing switches at `<style>`/`<body>`, tracks CSS selector/property tuples, HTML tag/property/value/content and repeated substrings, and proposes logit modification. Counts describe repetition, not redundant semantics: legitimate cascade/fallback or repeated UI structures remain possible counterexamples, not empirically observed failures asserted here. Inline pseudocode is not a code audit.

LLaVA-v1.6 7B/34B, temperature0/fixed seed2026/max4096 output tokens, Design2Code484 screenshots and100 sampled WebCode2M short/mid/long pages are finite populations. The latter wording does not establish100 from each split. FourA80080GB server is disclosed; precision, allocation per request, batch/concurrency/tail and production SLO are not.

Table3 reports 34B Design2Code160→82s and WebCode2M173→95s, generated2041→1195 and2116→1340 tokens. Preserve these local observations. Prefill540ms is worse than Pdrop491 on Design2Code; WebCode2M596 is worse than Pdrop582/VisionZip592. FLOPs explicitly count only LLM backbone, not full encoder/UIED/MST/parser cost or measured energy. Reported inference metric is input-to-final-output, but unreported preprocessing accounting/implementation/tail cannot be invented. UIED, graph/MST, full vision encoding, attention extraction/ranking/gather, parser, complete decode/render/quality regression all cost resources.

## Key Counterevidence And Center Dispute

S5 defines compression ratio `C_compressed/C_original`:60.36% and55.86% are remaining visual token ratios, not proof55–60% removed. Under that definition removal is39.64%/44.14%. Preserve the raw values and conflicting wording rather than quietly fixing the paper.

Table2 34B WebCode2M all six quality columns are below vanilla: Block .4382<.4688, Text .7533<.8207, Position .5907<.6441, Color .5313<.5546, CLIP .7270<.7554, BLEU .2634<.2689. Design2Code34B Block/BLEU also lower. Reduced redundant-sample counts and other positive slices remain real author-reported evidence; they do not certify identical UI semantics or full code correctness. Human50+50/five-annotator majority protocol is recorded, but unviewed plot pixels do not supply exact win rates or universally validate proxy metrics.

Table4 C4 vs C0 WebCode2M7B improves several metrics and37→32s, while Block .2718<.2843/Color .4909<.5056. C3 withoutADTS takes45s, slower than C0, despite shorter visual path; C1 FLOPs20.1<full20.4 and C3 prefill136<full141. Disabling ELTC also changes RTR to another selector. Thus no all-components/all-metrics dominance or one-edge causal attribution.

The central executable suppression prescription remains disputed: E7 defines unrestricted real logits and E8 ordinary softmax/argmax; E9 multiplies penalized logits by `lambda^c` with lambda<1. For the intended positive decay0<lambda<1, a negative logit increases. Reader's finite arithmetic counterexample, not a model experiment: logits[-2,-1], penalize first by.5→[-1,-1], its softmax probability .268941→.5 rather than falling. Adding4 to both original logits preserves original probabilities, but [2,3]→[1,3] yields .119203 for the same candidate. The rule is sign/offset dependent; no original normalization/sign constraint closes that suppression claim. Do not silently substitute a different penalty, infer the actual harness has this bug, or erase measured results. A correction/sign-aware definition plus matching executed behavior is the finite reopening evidence.

## Current Owner And Proposed Decision

Proposed **2+1+2=5**, unique `MULTIMODAL-REPRESENTATION` Ch23; output-sampling mechanism hands off to Ch20, not a second Book owner. Actual Ch23 complete1180–1252 budget/support-selection and consumer/position/cost chains read, plus Ch20 complete20–48 raw-logit shift invariance and146–185 repetition-vs-grammar/order/config chain. Existing text supports general selection/penalty boundaries but does not repair this paper's E9 or prove a combined no-loss UI pipeline. No generic topic-NC and no forced new Book paragraph.

Proposed **center D / Book0** for reusable combined compression/suppression recipe; retain geometric support proposal, local quality/cost results and direct tradeoffs as limited evidence. This is not scopeEX, score reduction, denial of every input-side observation or claim of reproduced code failure. Different-role author once necessary adoption must actually decide before formal merge. Reopen only exact suppression semantics/normalization/implementation agreement, or an explicitly narrower claim supported by matched quality/full-cost evidence. No need for every parameter plot/case/repository attachment. No PRE/grant/Book save or self-signing this package.
