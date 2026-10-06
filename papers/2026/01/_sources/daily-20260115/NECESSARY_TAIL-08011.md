Exact source: https://arxiv.org/html/2601.08011v1
Necessary bounded positions, actual original text below; not full-paper/appendix traversal.

## Text offsets 22100–31100
rphological transitions. 
 
 
 
 
 3.3 Cross-Attention Object Fusion 

 
 As shown in Figure  4 and summarized in Figure  4 , CAOF seamlessly integrates a blend object’s features into a replaced object during the diffusion process. Leveraging textual prompts for both the replaced and blend objects, CAOF locates key spatial regions in cross-attention maps and employs an Optimal Transport (OT) framework to determine blending levels. 
 
 
 Identifying Significant Positions in Cross-Attention Maps. 

 
 In multi-head cross-attention  Vaswani (2017) , each head h h produces attention weights 
 

 
 
 𝐀 ( h ) = softmax ⁡ ( 𝐐 ( h ) ​ 𝐊 ( h ) ⊤ d k ) , \mathbf{A}^{(h)}=\operatorname{softmax}\!\Bigl(\tfrac{\mathbf{Q}^{(h)}\,{\mathbf{K}^{(h)}}^{\top}}{\sqrt{d_{k}}}\Bigr), 
 
 (5) 
 
 where 𝐐 ( h ) ∈ ℝ N × d k \mathbf{Q}^{(h)}\in\mathbb{R}^{N\times d_{k}} and 𝐊 ( h ) ∈ ℝ M × d k \mathbf{K}^{(h)}\in\mathbb{R}^{M\times d_{k}} are query/key matrices, N N is the number of spatial positions, M M is the number of text tokens, and d k d_{k} is the head dimension.
We average over H H heads and focus on the replaced and blend object tokens, t replaced t_{\text{replaced}} and t blend t_{\text{blend}} : 
 

 
 
 𝐚 replaced = 1 H ∑ h = 1 H 𝐀 ( h ) : , t replaced , 𝐚 blend = 1 H ∑ h = 1 H 𝐀 ( h ) : , t blend . \mathbf{a}_{\text{replaced}}=\tfrac{1}{H}\!\sum_{h=1}^{H}\mathbf{A}^{(h)}_{:\,,\,t_{\text{replaced}}},\quad\mathbf{a}_{\text{blend}}=\tfrac{1}{H}\!\sum_{h=1}^{H}\mathbf{A}^{(h)}_{:\,,\,t_{\text{blend}}}. 
 
 (6) 
 
 To identify meaningful spatial positions, we introduce two percentile thresholds, τ source \tau_{\text{source}} and τ dest \tau_{\text{dest}} . Specifically, any position i i in 𝐚 blend \mathbf{a}_{\text{blend}} whose attention weight exceeds the τ source \tau_{\text{source}} -percentile is included in the source set 𝒮 \mathcal{S} , and any position in 𝐚 replaced \mathbf{a}_{\text{replaced}} exceeding the τ dest \tau_{\text{dest}} -percentile is placed in the destination set 𝒟 \mathcal{D} . 
 
 
 Clarification. The thresholds act on different head-averaged maps and therefore induce the two index sets independently. We make this explicit with 
 

 
 
 𝒮 = { i ∈ [ N ] : 𝐚 blend ​ [ i ] ≥ q τ source ​ ( 𝐚 blend ) } , 𝒟 = { i ∈ [ N ] : 𝐚 replaced ​ [ i ] ≥ q τ dest ​ ( 𝐚 replaced ) } , \mathcal{S}=\bigl\{\,i\in[N]:\mathbf{a}_{\text{blend}}[i]\geq q_{\tau_{\text{source}}}\!\bigl(\mathbf{a}_{\text{blend}}\bigr)\,\bigr\},\qquad\mathcal{D}=\bigl\{\,i\in[N]:\mathbf{a}_{\text{replaced}}[i]\geq q_{\tau_{\text{dest}}}\!\bigl(\mathbf{a}_{\text{replaced}}\bigr)\,\bigr\}, 
 
 (7) 
 
 where q τ ​ ( ⋅ ) q_{\tau}(\cdot) denotes the τ \tau -percentile. The sets 𝒮 \mathcal{S} and 𝒟 \mathcal{D} are not a partition of the image tokens. A position can be in neither set when it is below both cutoffs, in exactly one set when it responds strongly to only one prompt, or in both sets when it responds strongly to both prompts. In the fusion step (Sec.  3.3 ), only destination positions d ∈ 𝒟 d\in\mathcal{D} are updated and they receive transported features from sources s ∈ 𝒮 s\in\mathcal{S} under the OT plan 𝐓 \mathbf{T} (Eq.  11 and Eq.  9 ). Tokens i ∉ 𝒟 i\notin\mathcal{D} pass through unchanged. If a spatial location lies in 𝒮 ∩ 𝒟 \mathcal{S}\cap\mathcal{D} , its destination slot taken from the replaced stream can still import features from its source slot taken from the blend stream because these embeddings originate from different prompt branches which avoids ambiguity. When an object phrase spans multiple text tokens, we pool their columns before thresholding and use the mean by default, while max pooling yields similar behavior in our experiments. Although we often tie the thresholds in a joint setting with τ source = τ dest \tau_{\text{source}}=\tau_{\text{dest}} to simplify usage (see Fig.  12 ), they are defined separately and can be chosen differently to trade precision and coverage. The percentile formulation makes the selection scale-free and robust across layers and prompts because it depends on rank within each map rather than absolute magnitude. 
 
 
 
 Blending Feature Embeddings in Reshaped Cross-Attention Outputs. 

 
 To effectively integrate features from the blend object into the replaced object, we begin by concatenating the per-head attention outputs along the feature dimension: 
 

 
 
 𝐎 = Concat h = 1 H ​ ( 𝐀 ( h ) ​ 𝐕 ( h ) ) ∈ ℝ N × D , \mathbf{O}\;=\;\mathrm{Concat}_{h=1}^{H}\!\bigl(\mathbf{A}^{(h)}\mathbf{V}^{(h)}\bigr)\;\in\;\mathbb{R}^{N\times D}, 
 
 (8) 
 
 where 𝐀 ( h ) ∈ ℝ N × M \mathbf{A}^{(h)}\in\mathbb{R}^{N\times M} are attention weight matrices, 𝐕 ( h ) ∈ ℝ M × d k \mathbf{V}^{(h)}\in\mathbb{R}^{M\times d_{k}} are the corresponding value matrices, D = H ⋅ d k D=H\cdot d_{k} is the total feature dimensionality, N N is the number of query positions, and M M is the number of key tokens. By consolidating multi-head outputs into a single representation, we preserve all information necessary for seamless fusion, avoiding the loss that would occur from per-head embeddings. 
 
 
 We then blend the feature vectors of the replaced object with those of the blend object under a transport plan 𝐓 \mathbf{T} . Specifically, if d i ∈ 𝒟 d_{i}\in\mathcal{D} and s j ∈ 𝒮 s_{j}\in\mathcal{S} denote destination and source positions respectively, with 𝐟 d i , 𝐟 s j ∈ ℝ D \mathbf{f}_{d_{i}},\,\mathbf{f}_{s_{j}}\in\mathbb{R}^{D} being their respective feature vectors from 𝐎 \mathbf{O} , the updated feature vector at position d i d_{i} becomes 
 

 
 
 𝐟 d i ′ = ( 1 − w 0 ) ​ 𝐟 d i + w 0 ​ ∑ s j ∈ 𝒮 T i ​ j ∑ s k ∈ 𝒮 T i ​ k ​ 𝐟 s j , \mathbf{f}_{d_{i}}^{\prime}\;=\;(1-w_{0})\,\mathbf{f}_{d_{i}}\;+\;w_{0}\,\sum_{s_{j}\in\mathcal{S}}\!\frac{T_{ij}}{\sum_{s_{k}\in\mathcal{S}}T_{ik}}\;\mathbf{f}_{s_{j}}, 
 
 (9) 
 
 where w 0 ∈ [ 0 , 1 ] w_{0}\in[0,1] controls the relative influence of the blend features, and T i ​ j T_{ij} is obtained by solving the OT problem . By treating the multi-head outputs as a whole at the full dimensionality (e.g., D = 640 D=640 ), we not only preserve complex content and style cues but also obtain a more manageable OT cost matrix (e.g., 4096 × 4096 4096\times 4096 ), avoiding the significantly larger matrices (e.g., 40960 × 40960 40960\times 40960 ) that would result from per-head processing. 
 
 
 
 Formulating the Optimal Transport Problem. 

 
 Let 𝒮 \mathcal{S} and 𝒟 \mathcal{D} denote the sets of source (blend object) and destination (replaced object) positions. The cost of transporting mass from source position j ∈ 𝒮 j\in\mathcal{S} to destination position i ∈ 𝒟 i\in\mathcal{D} is given by 
 

 
 
 C i ​ j = λ feature ​ D feature ​ ( i , j ) + λ spatial ​ D spatial ​ ( i , j ) , C_{ij}=\lambda_{\text{feature}}\,D_{\text{feature}}(i,j)\;+\;\lambda_{\text{spatial}}\,D_{\text{spatial}}(i,j), 
 
 (10) 
 
 where D feature ​ ( i , j ) D_{\text{feature}}(i,j) is the cosine distance between feature vectors 𝐟 i \mathbf{f}_{i} and 𝐟 j \mathbf{f}_{j} and D spatial ​ ( i , j ) D_{\text{spatial}}(i,j) is the Euclidean distance between their spatial coordinates. 
 
 
 We solve the entropic OT problem: 
 

 
 
 min 𝐓 ≥ 0 \displaystyle\min_{\mathbf{T}\geq 0}\quad 
 ∑ i ∈ 𝒟 ∑ j ∈ 𝒮 T i ​ j ​ C i ​ j − γ ​ H ​ ( 𝐓 ) , \displaystyle\sum_{i\in\mathcal{D}}\sum_{j\in\mathcal{S}}T_{ij}C_{ij}-\gamma H(\mathbf{T}), 
 
 (11) 
 
 
 s.t. 
 ∑ j ∈ 𝒮 T i ​ j = 1 , ∀ i ∈ 𝒟 , \displaystyle\sum_{j\in\mathcal{S}}T_{ij}=1,\quad\forall i\in\mathcal{D}, 
 
 (12) 
 
 
 
 ∑ i ∈ 𝒟 T i ​ j ≥ 1 | 𝒮 | , ∀ j ∈ 𝒮 , \displaystyle\sum_{i\in\mathcal{D}}T_{ij}\geq\frac{1}{|\mathcal{S}|},\quad\forall j\in\mathcal{S}, 
 
 (13) 
 
 where H ( 𝐓 ) = − ∑ i , j T i ​ j log T i ​ j H(\mathbf{T})=-\sum_{i,j}T_{ij}\log T_{ij} is the entropy term, and γ > 0 \gamma>0 is the regularization parameter. Entropy regularization promotes smoother transport mass across source-destination pairs. 
 
 
 
 Solving the Optimal Transport Problem with the Sinkhorn Algorithm. 

 
 The entropic regularization allows the problem to be efficiently solved using the Sinkhorn algorithm  Cuturi (2013) ; Peyré et al. (2019) ; Genevay et al. (2016) . We form the Gibbs kernel 𝐊 = exp ( − 𝐂 / γ ) \mathbf{K}=\exp(-\mathbf{C}/\gamma) and iteratively update scaling vectors 𝐮 ∈ ℝ | 𝒟 | \mathbf{u}\!\in\!\mathbb{R}^{|\mathcal{D}|} and 𝐯 ∈ ℝ | 𝒮 | \mathbf{v}\!\in\!\mathbb{R}^{|\mathcal{S}|} : 
 

 
 
 𝐮 ( k + 1 ) = 𝟏 | 𝒟 | 𝐊 ​ 𝐯 ( k ) , 𝐯 ( k + 1 ) = 1 | 𝒮 | ​  1 | 𝒮 | 𝐊 ⊤ ​ 𝐮 ( k + 1 ) , \mathbf{u}^{(k+1)}\;=\;\frac{\mathbf{1}_{|\mathcal{D}|}}{\mathbf{K}\,\mathbf{v}^{(k)}},\quad\mathbf{v}^{(k+1)}\;=\;\frac{\tfrac{1}{|\mathcal{S}|}\,\mathbf{1}_{|\mathcal{S}|}}{\mathbf{K}^{\top}\,\mathbf{u}^{(k+1)}}, 
 
 (14) 
 
 until convergence. The transport plan becomes 
 

 
 
 𝐓 = diag ⁡ ( 𝐮 ) ​ 𝐊 ​ diag ⁡ ( 𝐯 ) . \mathbf{T}\;=\;\operatorname{diag}(\mathbf{u})\,\mathbf{K}\,\operatorname{diag}(\mathbf{v}). 
 
 (15) 
 
 Finally, we use 𝐓 \mathbf

## Text offsets 32700–38450
nting. 
 
 
 Figure 6 : SASF Flowchart: Self-Attention Style Fusion incorporates style prompts by injecting high-frequency details via DSIN and substituting textual Key/Value matrices, ensuring fine-grained style modulation during the diffusion process. 
 
 
 
 
 
 
 Ukiyo–e 
 Renaissance 
 Baroque 
 Low-Poly 
 
 
 
 
 
 
 
 
 
 Figure 7 : Stylistic renderings reshape fabric texture and accessories while pose and setting remain unchanged. The original knight is replaced by Albert Einstein , blended with a nobleman concept, and then rendered in four distinct styles. Each style reinterprets the garments in a unique way: Ukiyo-e replaces the surcoat with a patterned kimono, complete with an obi sash and a lacquered katana; Renaissance introduces brocaded velvet, gilt medallions, and a scholar’s cap; Baroque presents deep hued silk enriched with heavy gold embroidery and filigreed weaponry; Low-Poly abstracts every surface into planar facets and simplifies folds and metallic highlights. 
 
 
 Detail-Sensitive Instance Normalization. 

 
 Let 𝐅 replaced , 𝐅 style ∈ ℝ N × D \mathbf{F}_{\text{replaced}},\mathbf{F}_{\text{style}}\in\mathbb{R}^{N\times D} be the latent embeddings (i.e., token-wise feature maps) of the replaced and style objects, respectively. We first perform an AdaIN step on the replaced features: 
 

 
 
 𝐅 replaced ′ = ( 𝐅 replaced − μ rep σ rep ) ​ σ style + μ style , \mathbf{F}_{\text{replaced}}^{\prime}\,=\,\left(\frac{\mathbf{F}_{\text{replaced}}\,-\,\mu_{\text{rep}}}{\sigma_{\text{rep}}}\right)\,\sigma_{\text{style}}\;+\;\mu_{\text{style}}, 
 
 (16) 
 
 where ( μ rep , σ rep ) (\mu_{\text{rep}},\sigma_{\text{rep}}) and ( μ style , σ style ) (\mu_{\text{style}},\sigma_{\text{style}}) are the channel-wise means and standard deviations of the replaced and style embeddings. This aligns global statistics (mean and variance) to match the target style, but by itself may overlook subtle, higher-frequency stylistic cues. 
 
 
 Next, DSIN applies a small 1D Gaussian smoothing filter along the token dimension to decompose both 𝐅 replaced \mathbf{F}_{\text{replaced}} and 𝐅 style \mathbf{F}_{\text{style}} into low-frequency (LF) and high-frequency (HF) components: 
 

 
 
 𝐅 LF = 𝐅 ∗ 𝐊 , 𝐅 HF = 𝐅 − 𝐅 LF , \mathbf{F}^{\mathrm{LF}}\,=\,\mathbf{F}*\mathbf{K},\quad\mathbf{F}^{\mathrm{HF}}\,=\,\mathbf{F}\;-\;\mathbf{F}^{\mathrm{LF}}, 
 
 (17) 
 
 where 𝐊 \mathbf{K} is a 1D Gaussian kernel of size k = 2 ​ m + 1 k=2m+1 and width  σ \sigma . Intuitively, 𝐅 LF \mathbf{F}^{\mathrm{LF}} captures coarse variations (slower changes across tokens), while 𝐅 HF \mathbf{F}^{\mathrm{HF}} isolates the finer details. DSIN then injects a fraction α \alpha of the style HF difference directly into the AdaIN output: 
 

 
 
 𝐅 replaced ′′ = 𝐅 replaced ′ + α ⁡ ( 𝐅 style HF − 𝐅 replaced HF ) . \mathbf{F}_{\text{replaced}}^{\prime\prime}\,=\,\mathbf{F}_{\text{replaced}}^{\prime}\;+\;\alpha\,\bigl(\mathbf{F}_{\text{style}}^{\mathrm{HF}}\;-\;\mathbf{F}_{\text{replaced}}^{\mathrm{HF}}\bigr). 
 
 (18) 
 
 
 
 When DSIN applies a 1D Gaussian kernel 𝐊 \mathbf{K} along the token dimension, it acts as a low-pass filter in the frequency domain: larger σ \sigma broadens the kernel’s passband, yielding a narrower high-frequency (HF) residual 𝐅 HF \mathbf{F}^{\mathrm{HF}} and thus a subtler style injection. Conversely, smaller σ \sigma captures more mid- and high-frequency components, accentuating textural details (e.g., brushstrokes) in the final output. The injection fraction α \alpha then scales the amplitude of these style-specific HF cues. In effect, σ \sigma and α \alpha together provide a powerful mechanism for tuning the granularity and prominence of style features. 
 
 
 Unlike prior approaches such as Huang & Belongie (2017) or Chung et al. (2024) that apply AdaIN globally or only at the initial noise level for DDIM inversion, our DSIN is applied at every self-attention layer throughout the denoising process. This repeated application ensures the progressive and layer-wise infusion of fine-grained stylistic features, enabling multi-scale texture adaptation without disrupting the overall structure. 
 
 
 
 Key/Value Substitution. 

 
 Following the DSIN framework, we first construct the Query, Key, and Value matrices for self-attention. We then substitute the Key and Value channels of the target (replaced) object with those of the style source: 
 

 
 
 𝐊 tar ← 𝐊 sty , 𝐕 tar ← 𝐕 sty . \mathbf{K}_{\mathrm{tar}}\;\leftarrow\;\mathbf{K}_{\mathrm{sty}},\qquad\mathbf{V}_{\mathrm{tar}}\;\leftarrow\;\mathbf{V}_{\mathrm{sty}}. 
 
 (19) 
 
 
 
 Since the self-attention output is computed by weighting the Value vectors using Query-Key dot products, replacing the Key and Value matrices of the replaced region with those from the style prompt allows style features to dominate the attention updates. This substitution imposes the texture and local patterns of the style onto the replaced object, leading to strong stylistic transformations. 
 
 
 While Chung et al. (2024) apply this substitution using Key/Value representations extracted from an image-based style encoder, our approach instead derives these from textual prompts. Specifically, we construct the Key/Value matrices from the text prompts of both the replaced object and the style source, enabling a text-driven style transfer mechanism without requiring image-based features. 
 
 
 Importantly, although this substitution offsets the effect of DSIN modulation in the Key/Value branches for the replaced object (since it is overwritten by style-derived features), DSIN-modified features remain intact in the Query branch. This asymmetry allows DSIN to still influence the attention outputs via its role in comput

## Text offsets 51550–60300
ons. 
 
 
 
 
 4.3 Ablation Study 

 
 Ablation Study on CAOF. 

 
 To examine how CAOF controls the fusion strength, we vary the blending coefficient w 0 ∈ [ 0.1 , 0.9 ] w_{0}\in[0.1,0.9] (Eq.  9 ) and record the CLIP similarities for the original (O), replaced (R), and blend (B) prompts. Figure  10 illustrates the variation of CLIP scores with w 0 w_{0} . The curves clearly demonstrate CAOF’s effectiveness in adjusting blending strength. As w 0 w_{0} increases beyond 0.6, the influence of the blend object prompt P b P_{b} significantly rises, while the influence of the replaced object prompt P r P_{r} remains high until w 0 w_{0} exceeds 0.8, after which it decreases rapidly. Concurrently, the influence of the original object prompt P o P_{o} remains consistently low throughout, aligning with our goal to replace the original object with the replaced object while blending in the blend object to the desired extent. Qualitative frames in Fig.  11 corroborate the numerical trend, showing a smooth morph from “mostly replacement” to “mostly blend” without geometric break-down. 
 
 
 
 SASF Ablation. 

 
 SASF relies solely on textual prompts for style specification, prompting us to measure style blending performance through CLIP ^ S \hat{\text{CLIP}}_{S} , the normalized similarity between the generated image I g I_{g} and the style object prompt P s P_{s} . As shown in Table  2 , CAOF+SASF attains a substantially higher CLIP S of 0.2161 than CAOF’s 0.1976, indicating that SASF effectively injects the desired style features. 
 
 
 
 
 
 
 
 
 
 Method 
 BOM ↑ \uparrow 
 CLIP R ↑ \uparrow 
 CLIP B ↑ \uparrow 
 1 − 1- LPIPS O ↑ \uparrow 
 
 
 
 NoneOT 
 0.1429 
 0.1984 
 0.2891 
 0.8304 
 
 CAOF 
 0.2500 
 0.2014 
 0.2937 
 0.8292 
 
 
 Table 3 : OT ablation: CAOF vs. NoneOT. 
 
 
 
 
 
 
 α \alpha 
 σ \sigma 
 LV ↑ \uparrow 
 GC ↑ \uparrow 
 HFS ↑ \uparrow 
 
 
 
 0.5 
 2.5 
 271.8709 
 79.9853 
 5.27 × 10 9 5.27{\times}10^{9} 
 
 0.5 
 0.5 
 253.3316 
 79.7168 
 5.06 × 10 9 5.06{\times}10^{9} 
 
 0.2 
 2.5 
 266.9800 
 80.0325 
 5.21 × 10 9 5.21{\times}10^{9} 
 
 0.2 
 0.5 
 241.8779 
 76.5979 
 4.97 × 10 9 4.97{\times}10^{9} 
 
 0.0 
 – 
 244.2984 
 68.8580 
 4.90 × 10 9 4.90{\times}10^{9} 
 
 
 Table 4 : DSIN texture metrics versus α \alpha and σ \sigma . 
 
 
 
 
 Ablation on the joint percentile thresholds τ source , τ dest \tau_{\text{source}},\,\tau_{\text{dest}} . 

 
 CAOF builds the source set 𝒮 \mathcal{S} and destination set 𝒟 \mathcal{D} by thresholding head-averaged cross-attention responses of the blend and replaced prompts. Positions above the τ source \tau_{\text{source}} percentile in the blend map enter 𝒮 \mathcal{S} and those above the τ dest \tau_{\text{dest}} percentile in the replaced map enter 𝒟 \mathcal{D} . Sweeping the joint threshold τ source = τ dest ∈ { 0 , 10 , … , 90 , 99 } \tau_{\text{source}}=\tau_{\text{dest}}\in\{0,10,\ldots,90,99\} exposes a precision vs. coverage trade-off that directly governs how CAOF redistributes features. Figure  12 plots CLIP cosine scores for the original prompt P o P_{o} , the replaced prompt P r P_{r} , and the blend prompt P b P_{b} . Three observations follow from the measured curves. 
 
 
 First, P b P_{b} peaks at a mid to high threshold: the best blend alignment occurs at 60 % 60\% where P b = 0.2530 P_{b}=0.2530 and remains competitive at 70 % 70\% with P b = 0.2371 P_{b}=0.2371 . Around this regime spurious low-confidence tokens are removed yet all salient parts of the object remain in 𝒮 \mathcal{S} and 𝒟 \mathcal{D} . The feature and spatial terms then rank candidate correspondences cleanly and the transport plan concentrates mass on semantically consistent matches, so the fused vectors carry the right identity and geometry. 
 
 
 Second, very high thresholds shrink coverage and favor replacement: when τ source , τ dest \tau_{\text{source}},\tau_{\text{dest}} are pushed to 80 % 80\% and beyond, the sets collapse to a handful of extreme tokens. Coverage drops and CAOF touches only tiny regions, so the CFG-TE replacement signal dominates the denoising trajectory. Empirically P r P_{r} rises from 0.1719 0.1719 at 60 % 60\% to 0.2361 0.2361 at 99 % 99\% , while P b P_{b} falls sharply to 0.1592 0.1592 – 0.1623 0.1623 . 
 
 
 Third, low thresholds dilute semantic precision: at 0 % 0\% – 50 % 50\% the sets admit many background or off-object positions. The plan must spread mass across numerous weak matches and the averaged multi-head vectors mix in non-relevant content, which reduces blend fidelity. This explains the drop from P b = 0.2413 P_{b}=0.2413 at 20 % 20\% to P b = 0.2137 P_{b}=0.2137 at 50 % 50\% . 
 
 
 Throughout the sweep the original content remains suppressed, with P o P_{o} staying low in the range 0.1221 0.1221 – 0.1585 0.1585 . Taken together these trends justify the default τ source = τ dest ∈ { 0.6 , 0.7 } \tau_{\text{source}}=\tau_{\text{dest}}\in\{0.6,0.7\} . This window removes noise while preserving spatial coverage, maximizes P b P_{b} near its peak, keeps P r P_{r} strong enough for reliable replacement and maintains low P o P_{o} . The ablation therefore confirms that mid to high joint percentiles are critical for stable and semantically faithful blending under CAOF. 
 
 
 Figure 12 : Joint percentile threshold ablation. CLIP cosine scores for P O P_{O} , P R P_{R} , and P B P_{B} as the joint threshold τ source = τ dest \tau_{\text{source}}=\tau_{\text{dest}} varies. The blend score P B P_{B} peaks at 60 % 60\% . Very high thresholds shrink 𝒮 \mathcal{S} and 𝒟 \mathcal{D} excessively and favor replacement ( P R P_{R} ) over blending, while low thresholds admit non-relevant vectors that dilute the fused signal. Moderate thresholds balance precision and coverage. 
 
 
 
 OT Ablation. 

 
 To disentangle the contribution of the Sinkhorn solver, we replace it with a naïve NoneOT variant that line-up source and destination tokens by index and applies a fixed α \alpha -blend, thereby ignoring both feature similarity and spatial proximity. As summarised in Table  3 , removing Optimal Transport slashes BOM from 0.2500 to 0.1429. The loss is driven almost entirely by lower alignment scores ( CLIP R and CLIP B ), while the perceptual term − LPIPS O 1\!-\!\text{LPIPS}_{O} remains virtually unchanged. In other words, a uniform blend preserves low-level appearance but often allocates the wrong blend features to the wrong spatial regions, degrading semantic coherence. The cost-aware Sinkhorn plan redistributes those features toward geometrically and visually compatible destinations, yielding a markedly more faithful fusion without sacrificing overall image fidelity. 
 
 
 
 DSIN Ablation. 

 
 Laplacian Variance (LV)  Pertuz et al. (2013) , GLCM Contrast (GC)  Haralick et al. (1973) , and FFT High-Frequency Sum (HFS)  Gonzalez & Woods (2008) show that textural richness depends on the joint choice of the residual-mixing weight α \alpha and the Gaussian width σ \sigma , rather than on α \alpha alone. Raising α \alpha strengthens the amplitude of the injected high-frequency residual, but this extra energy is useful only if σ \sigma is large enough to confine the smoothing kernel to genuinely low frequencies; with α = 0.5 \alpha=0.5 the wider kernel σ = 2.5 \sigma=2.5 yields the highest LV, GC, and HFS, whereas the same α \alpha combined with the narrow kernel σ = 0.5 \sigma=0.5 loses mid-range structure and drops all three scores. Conversely, keeping α \alpha moderate at 0.2 still improves over pure AdaIN ( α = 0 \alpha=0 ), yet the gain is larger when σ = 2.5 \sigma=2.5 than when σ = 0.5 \sigma=0.5 . These trends confirm that α \alpha governs how much fine detail is transferred while σ \sigma sets the frequency band that will be regarded as “detail”; optimal texture emerges when both parameters are tuned together, explaining the peak at α = 0.5 , σ = 2.5 \alpha=0.5,\ \sigma=2.5 in Table  4 and the visibly crisper result in Figure  13 . 
 
 
 
 
 
 
 
 
 
 Figure 13 : Pixel-art edit of “robot → \rightarrow knight” blended with “Thanos”. Left: α = 0 \alpha=0 , right: α = 0.5 , σ = 2.5 \alpha=0.5,\ \sigma=2.5 . 
 
 
 
 
 
 5 Conclusion 

 
 We introduced TP-Blend, a training-free framework that performs object replacement, object blending, and style fusion within a single diffusion denoising run. By separating the content and style prompts, TP-Blend grants independent control over semantic structure and appearance. Cross-Attention Object Fusion employs an optimal-transport plan to place blend-object features in spatially and semantically consistent regions, while Self-Attention Style Fusion injects high-frequency texture through detail-sensitive instance normalisation and text-driven key-value substitution.
