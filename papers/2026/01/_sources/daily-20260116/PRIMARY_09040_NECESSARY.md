# Exact-v1 minimum primary: 2601.09040

Source: https://arxiv.org/html/2601.09040v1 . Only selected necessary method/evaluation/counterevidence; full fetched body is not a whole-paper review.

## Raw body offsets 10913–16800

3.1 Training setup
We study blockwise self-supervised learning (BWSSL) by splitting a VideoMAE-style video ViT encoder into KK gradient-isolated blocks. We write
f(x)=fK∘⋯∘f1(x)f(x)=f_{K}\circ\cdots\circ f_{1}(x) with h~0=x\tilde{h}_{0}=x for an input clip xx and hk=fk​(h~k−1)h_{k}=f_{k}(\tilde{h}_{k-1}).
To enforce gradient isolation, we insert a stop-gradient operator sg⁡(⋅)\mathrm{sg}(\cdot) at block boundaries:
for k<Kk<K, we pass h~k=sg⁡(hk)\tilde{h}_{k}=\mathrm{sg}(h_{k}) to the next block. Thus, losses applied at depth kk update only fkf_{k} (and its decoder) while leaving forward activations unchanged.
Following VideoMAE, we sample a binary mask on the spatiotemporal token grid and drop masked tokens before the encoder, so each block processes the variable-length sequence of visible tokens. For representation analyses (Sec. 4.1 onward), we disable masking and run the encoder on the full token sequence.
Each block kk is trained with a local masked-reconstruction loss
ℒk=ℒMAE​(dk​(hk),x,m),\mathcal{L}_{k}=\mathcal{L}_{\text{MAE}}\big(d_{k}(h_{k}),\,x;\,m\big),
(1)
where dkd_{k} is a VideoMAE-style decoder (Sec. 3.3). The mask mm is sampled once per clip and reused across all blocks to match the E2E baseline’s masking pattern.
We compare three optimization regimes:
1. 
Sequential BWSSL.
Blocks are trained in order k=1,…,Kk=1,\dots,K. At stage kk, we run up to block kk and update only (fk,dk)(f_{k},d_{k}), with earlier blocks frozen.
2. 
Simultaneous BWSSL.
Each iteration runs a full forward pass with stop-gradients at boundaries, computes {ℒk}k=1K\{\mathcal{L}_{k}\}_{k=1}^{K}, and updates each (fk,dk)(f_{k},d_{k}) using its own loss (equivalently, optimizes ∑kℒk\sum_{k}\mathcal{L}_{k} under gradient isolation).
3. 
End-to-end (E2E) baseline.
We apply the VideoMAE loss only at hKh_{K} using dKd_{K} and backpropagate through the full encoder.
For each model size, we train E2E and simultaneous BWSSL for EE epochs. Sequential BWSSL uses KK stages of EE epochs: each encoder parameter is updated for EE epochs in all regimes, but sequential training makes K​EKE passes over the dataset.
BWSSL differs from E2E in supervision placement in addition to gradient locality due the intermediate reconstruction losses.
3.2 Training objective
All regimes use VideoMAE masked video modeling [21]. Each decoder predicts tubelet-patch targets, and an MSE reconstruction loss is only computed over masked token positions (averaged over batch, masked tokens, and target dimensions). Masking is applied on the spatiotemporal token grid with tubelets of (8,16,16)(8,16,16) and a mask ratio of 90%90\%. We use temporal tubelets of 8 mainly for efficiency, reducing encoder and multi-decoder compute under high masking. We do not perform supervised fine-tuning.
Optimization is based on the VideoMAE recipe with AdamW (learning-rate 1×10−41\times 10^{-4}, cosine schedule, weight decay 0.050.05).
3.3 Network architecture
We use a 12-layer ViT with tubelet tokenization [6, 22, 1], in DeiT-Tiny and DeiT-Small configurations (embedding dim 192/384, heads 3/6) [22]. We train DeiT-Tiny for E=150E{=}150 and DeiT-Small for E=300E{=}300 epochs.
For BWSSL, we partition the encoder into either K=4K{=}4 blocks (default, matching common practice for comparability) of 3 layers or K=6K{=}6 blocks of 2 layers to probe sensitivity to partition granularity. Block 1 includes the tubelet embedding, and block KK applies the standard output LayerNorm, while blocks are otherwise identical. (We found no notable differences from inserting LayerNorm at every boundary and keep the standard formulation to match the E2E baseline.)
Each block uses a 4-layer ViT decoder, with a width of 192 and 3 attention heads (fixed across KK, model sizes, and regimes). E2E uses one decoder, whereas BWSSL uses KK. Let PencP_{\text{enc}} and PdecP_{\text{dec}} denote encoder and single-decoder parameters. Then
PE2E=Penc+PdecP_{\text{E2E}}=P_{\text{enc}}+P_{\text{dec}} and PBW=Penc+K​PdecP_{\text{BW}}=P_{\text{enc}}+KP_{\text{dec}},
so the relative increase is (K−1)​Pdec/(Penc+Pdec)(K-1)P_{\text{dec}}/(P_{\text{enc}}+P_{\text{dec}}).
Thus, larger KK can substantially increase parameters and typically also compute, despite identical encoder size. Therefore, even though credit-assignment paths are shorter, memory usage can still increase.
3.4 Training data
We train on the official UCF101 train split [19]. We use a frame-based representation as in prior work [7]. Each clip is a contiguous sequence of T=16T{=}16 frames with temporal stride s=4s{=}4 (span T​s=64Ts=64 original frames). Videos shorter than T​sTs frames are excluded. We apply random cropping to 128×128128\times 128 and random horizontal flipping. For efficiency, we subsample 30%30\% of the test split (N≈1100N\approx 1100) and use center cropping as augmentation.
4 Comparative Representation Analysis
We compare BWSSL with matched E2E training by analyzing intermediate and final representations.
Given a trained encoder partitioned into KK blocks, we record the block-boundary token representations hkh_{k} for k∈{1,…,K}k\in\{1,\dots,K\}.
When a single vector per clip is required, we form zkz_{k} by mean-pooling patch tokens.
We evaluate representations along four axes: (i) downstream performance (linear probing and retrieval), (ii) feature complexity across depth, (iii) representational change across blocks (CKA), and (iv) patch-level detail retention and robustness.
Each model is trained with 3 random initialisations. Metrics that fit an auxiliary model (e.g. linear probes) are also evaluated 3 times per trained network. Unless stated otherwise, metrics operate on zkz_{k} and token-level analyses on hkh_{k}.
4.1 Downstream task performance metrics
We evaluate frozen embeddings extracted after pretraining on UCF101.
We report three complementary metrics (Figure 2): (i) linear-probe accuracy, (ii) kNN r

## Raw body offsets 23912–28550

5 Results
Our analysis of loss dynamics and representational characteristics across blocks revealed a number of distinct observations.
BWSSL VideoMAE on ViT backbones converges and approaches E2E representation quality.
Across all settings, our BWSSL setup converged reliably.
MSE losses in the final-layer reconstruction were on par or slightly better in sequential BWSSL compared to E2E training. Simultaneous BWSSL typically yielded slightly higher MSE losses (Figure 2c).
On downstream proxies, BWSSL remained close to E2E in both linear probing and retrieval mAP (Figure 2a,b), with only small residual gaps, showing overall comparable linear accessibility of task-relevant information and the semantic structure of the embedding space.
For DeiT-Tiny, the gap was ≤0.02\leq 0.02 in linear-probe accuracy and ≤0.015\leq 0.015 in mAP, while for DeiT-Small, ≤0.04\leq 0.04 and ≤0.02\leq 0.02, respectively.
These consistent small gaps are in line with prior BWSSL results [18, 24].
Sequential and simultaneous training yield similar representations despite different loss dynamics.
Simultaneous BWSSL reconstruction loss often plateaus after early blocks (Figure 4a), whereas sequential BWSSL shows more consistent improvement across depth. Since blocks are trained sequentially and then frozen, later blocks typically achieve better scores.
Despite these differences, representation quality is nearly identical: across model sizes, block splits, and evaluation settings, sequential and simultaneous BWSSL usually differ by <0.01<0.01 in linear-probe Acc. and mAP (Figure 2a,b), with neither variant consistently outperforming the other.
This similarity holds for depth-resolved evaluations (differences are typically within run-to-run variability): feature-complexity probes (Figure 3), representational similarity of blocks (Figure 4), and patch-level analyses (Figure 5).
Finer block granularity shows no notable effect on reconstruction loss.
For both investigated model sizes, increasing the block granularity from four to six blocks did not significantly affect the final layer reconstruction loss, although the scores were overall slightly lower for DeiT-Small (Figure 2c).
Representation quality of embeddings in the last module showed only small but consistent reductions with 6 modules (Figure 2a,b):
Retrieval mAP typically decreased by less than 0.01, and linear-probe accuracy by less then 0.02. Often, differences overlap within run-to-run variability. (Figure 2a,b)
BWSSL training promotes earlier linear access to higher-complexity information.
Independent of model size, BWSSL decodes better than E2E at matched depth for relational and action targets (Figure 3b,c), suggesting that BWSSL makes mid- and high-level features linearly accessible in earlier layers.
At the same time, E2E training shows a stronger improvement with deeper modules and higher linear probe accuracy for low label complexity  3a).
We thus see a shift in where higher-complexity targets are linearly accessible. BWSSL emphasizes accessibility in early modules, whereas E2E training gains more from later modules.
Low-complexity targets remain linearly decodable under BWSSL.
Prior work on supervised blockwise learning reported losses of task-relevant information in early blocks with negative downstream effects [23, 17].
In our self-supervised setting, E2E indeed yields higher low-level decoding than BWSSL at matched depth (Figure 3a), but the disadvantage is modest:
it is largest in the first block (about 0.020.02 in accuracy) and does not systematically increase with depth, indicating only a small overall reduction in low-level linear accessibility.
The depth-wise trend depends on model size. For DeiT-Small, low-level decoding is nearly constant across blocks for both regimes, with an approximately stable gap. For DeiT-Tiny, decoding decreases with depth for all regimes, and the E2E-BWSSL gap narrows in later blocks as performance drops. Overall, we see no systematic amplification of low-level linear decodability decrease with depth under BWSSL.
BWSSL shows diminishing late-block gains alongside increasing inter-block similarity.
While early blocks improve embedding quality under BWSSL, later blocks offer little and sometimes negative additional gains.
In particular, the block 3→\to4 transition yields near-zero (and occasionally negative) marginal improvements in linear-probe performance (Figure 3) and MSE Loss (Figure 4a).
This is unlikely to be simple task saturation. Early BWSSL embeddings already approach the final BWSSL scores, yet still lag behind E2E indicating clear headroom that later BWSSL blocks fail to 

## Raw body offsets 31922–35900

6 Discussion
Why can BWSSL remain near-competitive without long-range error propagation?
BWSSL approaching E2E on our transfer proxies is notable but consistent with prior work showing that strong representations can emerge under BWSSL [18], so we do not attribute competitiveness to a single factor in our setup. Masked reconstruction provides dense per-block supervision: each block must output an embedding from which its decoder can reconstruct, discouraging interfaces that drop reconstruction-relevant cues. Transformer residual streams may further stabilize this depth-wise interface, making later refinement easier.
The remaining gap to E2E is plausibly due to missing global coordination: E2E can align early representations with the final embedding geometry, whereas BWL can converge to locally sufficient but not globally optimal interfaces.
How does BWSSL reshape the low-level ↔\leftrightarrow high-level accessibility profile across depth?
BWSSL shifts high-level decodability earlier, likely because intermediate reconstruction losses reward early integration of non-local structure. Low-level decodability is only slightly reduced, consistent with redistribution or possibly slightly lower detail retention, rather than a strict trade-off. Mechanistically, this might be driven by supervision placement rather than gradient isolation per se.
What determines when block granularity helps?
Increasing granularity introduces more boundaries but smaller per-block updates. This can make handoffs smoother (less chance of a large, irreversible jump in one module), while limiting how much new structure each block can build. In our setup, this trade-off appears to depend on model size.
A likely moderator is decoder strength: Since each block has its own decoder, the local objective can be met either by improving the embedding or by relying on decoder capacity. With decoder depth held fixed, increasing the number of modules makes decoders effectively stronger relative to each (shallower) block, favoring representations that require more relative decoder strength to reconstruct without reliably becoming more transfer-friendly.
Why do later modules sometimes add little beyond earlier representations?
High consecutive similarity together with near-zero (or negative) marginal gains suggests that late BWL modules often operate in a “reuse-and-refine” mode rather than “re-encode”. Two non-exclusive mechanisms are consistent with this pattern.
First, interface limitation: if an early module converges to an embedding that is sufficient for its local decoder but does not expose cues needed for downstream improvements, later modules can only transform what is already represented and may be unable to recover missing information. This implies a one-way constraint: locally adequate early interfaces can cap later gains.
Second, local-objective stabilization: even when relevant cues are present, a module may find it locally optimal to preserve incoming geometry because any exploratory change is immediately penalized by its own decoder. This also predicts schedule-dependent loss curves: in sequential training, later decoders can reduce reconstruction loss mainly by learning to decode an already-usable upstream embedding, without requiring large representational changes. In simultaneous training, the decoder’s input embedding keeps moving during co-optimization, which can blunt late loss improvements even when final transfer proxies are similar.
Why does model size interact with BWL in our setup?
BWL is closer to E2E in DeiT-Tiny than in DeiT-Small on our proxy metrics, with corresponding differences in token-level diagnostics. A likely driver is a capacity-ratio change: the decoder is fixed, while the encoder size depends on the model, so the local reconstruction bottleneck is relatively much tighter in DeiT-Small. This alters what boundary embeddings must encode (and thus what is passed to the next block).
Finally, the performance gap of
