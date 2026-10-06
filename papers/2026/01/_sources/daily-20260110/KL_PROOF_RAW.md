# Jan10 KLJudge 必要原源

仅exact-v1拟采用KL条件分支及关键理论反侧；缓存为原web返回，不替代作者推断或代码复现。

Revisiting Judge Decoding from First Principles via Training-Free Distributional Divergence (https://arxiv.org/html/2601.04766v1)
citeturn26875view0 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.04766v1","lineno":365}); Total lines: 432
L276:   * Li et al. (2025) Yuhui Li, Fangyun Wei, Chao Zhang, and Hongyang Zhang. 2025. Eagle-3: Scaling up inference acceleration of large language models via training-time test. In arXiv:2503.01840.
L277:   * Luo et al. (2025) Xianzhen Luo, Yixuan Wang, Qingfu Zhu, Zhiming Zhang, Xuanyu Zhang, Qing Yang, and Dongliang Xu. 2025. Turning trash into treasure: Accelerating inference of large language models with token recycling. In ACL.
L278:   * Naveed et al. (2025) Humza Naveed, Asad Ullah Khan, Shi Qiu, Muhammad Saqib, Saeed Anwar, Muhammad Usman, Naveed Akhtar, Nick Barnes, and Ajmal Mian. 2025. A comprehensive overview of large language models. In ACM Transactions on Intelligent Systems and Technology, volume 16, pages 1–72. Association for Computing Machinery.
L279:   * Oliaro et al. (2024) Gabriele Oliaro, Zhihao Jia, Daniel Campos, and Aurick Qiao. 2024. SuffixDecoding: Extreme speculative decoding for emerging ai applications. In arXiv:2411.04975.
L280:   * OpenAI et al. (2024) OpenAI, Aaron Jaech, Adam Kalai, Adam Lerer, Adam Richardson, Ahmed El-Kishky, et al. 2024. Openai o1 system card. In arXiv:2412.16720.
L281:   * Pope et al. (2023) Reiner Pope, Sholto Douglas, Aakanksha Chowdhery, Jacob Devlin, James Bradbury, Jonathan Heek, Kefan Xiao, Shivani Agrawal, and Jeff Dean. 2023. Efficiently scaling transformer inference. In Proceedings of Machine Learning and Systems.
L282:   * Servedio et al. (2025) Giovanni Servedio, Alessandro De Bellis, Dario Di Palma, Vito Walter Anelli, and Tommaso Di Noia. 2025. Are the hidden states hiding something? Testing the limits of factuality-encoding capabilities in LLMs. In ACL.
L283:   * Sun et al. (2025) Shengyin Sun, Yiming Li, Xing Li, Yingzhao Lian, Weizhe Lin, Hui-Ling Zhen, Zhiyuan Yang, Chen Chen, Xianzhi Yu, Mingxuan Yuan, and Chen Ma. 2025. Scaling up, speeding up: A benchmark of speculative decoding for efficient LLM test-time scaling. In arXiv:2509.04474.
L284:   * Wang et al. (2025) Jikai Wang, Zhenxu Tian, Juntao Li, Qingrong Xia, Xinyu Duan, Zhefeng Wang, Baoxing Huai, and Min Zhang. 2025. Alignment-augmented speculative decoding with alignment sampling and conditional verification. In Proc. Conf. Empirical Methods in Natural Language Processing.
L285:   * Wang et al. (2024) Yubo Wang, Xueguang Ma, Ge Zhang, Yuansheng Ni, Abhranil Chandra, Shiguang Guo, Weiming Ren, Aaran Arulraj, Xuan He, Ziyan Jiang, Tianle Li, Max Ku, Kai Wang, Alex Zhuang, Rongqi Fan, Xiang Yue, and Wenhu Chen. 2024. MMLU-Pro: A more robust and challenging multi-task language understanding benchmark. In Advances in Neural Information Processing Systems.
L286:   * Xia et al. (2024) Heming Xia, Zhe Yang, Qingxiu Dong, Peiyi Wang, Yongqi Li, Tao Ge, Tianyu Liu, Wenjie Li, and Zhifang Sui. 2024. Unlocking efficiency in large language model inference: A comprehensive survey of speculative decoding. In ACL.
L287:   * Yang et al. (2025) An Yang, Anfeng Li, Baosong Yang, Beichen Zhang, Binyuan Hui, et al. 2025. Qwen3 technical report. In arXiv:2505.09388.
L288:   * Yoon et al. (2025) Kanghoon Yoon, Minsub Kim, Sungjae Lee, Joonhyung Lee, Sunghyeon Woo, Yeonjun In, Se Jung Kwon, Chanyoung Park, and Dongsoo Lee. 2025. Selfjudge: Faster speculative decoding via self-supervised judge verification. In arXiv:2510.02329.
L289:   * Zhao et al. (2024) Yao Zhao, Zhitian Xie, Chen Liang, Chenyi Zhuang, and Jinjie Gu. 2024. Lookahead: An inference acceleration framework for large language model with lossless generation accuracy. In Proc. ACM Conf. Knowledge Discovery and Data Mining.
L290:   * Ziashahabi et al. (2025) Amir Ziashahabi, Yavuz Faruk Bakman, Duygu Nur Yaldiz, Mostafa El-Khamy, Sai Praneeth Karimireddy, and Salman Avestimehr. 2025. Reject only critical tokens: Pivot-aware speculative decoding. In arXiv:2511.00351.
L291: ## Appendix A Appendix
L292: ### A.1 Proof of Theorem cite68†4.1 L293: To facilitate the derivation, we first review the notation and setup. Let the target and draft logits be $z_{t}:=W_{t}h_{t}+b_{t}$ and $z_{d}:=W_{d}h_{d}+b_{d}$ respectively, with corresponding probability distributions $P_{t}:=\mathrm{softmax}(z_{t})$ and $P_{d}:=\mathrm{softmax}(z_{d})$. We define the concatenated hidden representation $x:=[h_{t};h_{d}]\in\mathbb{R}^{2d}$ and the logit difference vector $\delta:=z_{t}-z_{d}$.
L294: Consequently, $\delta$ is affine in $x$ and is given by $\delta=Mx+c$, where $M:=[W_{t},-W_{d}]$ and $c:=b_{t}-b_{d}$. For any vocabulary indices $i,j\in\{1,\dots,V\}$, the pairwise logit-gap difference is defined as $\Delta_{ij}(x):=(z_{t}(i)-z_{t}(j))-(z_{d}(i)-z_{d}(j))$, which yields the $\Delta_{ij}(x)=\delta_{i}-\delta_{j}$. This linear primitive $\Delta_{ij}(x)$ serves as the basis for our analysis.
L295: ###### Proof Sketch of Theorem cite68†4.1 .
L296: We ground the analysis in the affine primitives $\Delta_{ij}(x)$. By expanding the KL divergence via the Fisher information metric (§cite32†A.1.1 ), we decompose the divergence into a weighted quadratic aggregation of these primitives (§cite33†A.1.2 ). We subsequently demonstrate that discrete ranking inconsistencies necessitate boundary-crossing deviations (§cite34†A.1.3 ), thereby enforcing a quantitative lower bound on the divergence (§cite35†A.1.4 ).
L297: Finally, we prove that the linear classifier’s decision surface forms a linear superposition of this same primitive basis (§cite36†A.1.5 ), confirming that both mechanisms regulate the same logit-space deviations. ∎
L298: #### A.1.1 KL as a Bregman divergence and Fisher second-order approximation
L299: 
L300: We define the log-sum-exp potential $A(z):=\log\sum_{i=1}^{V}e^{z_{i}}$, which satisfies $\nabla A(z)=p$ and $\nabla^{2}A(z)=\mathrm{diag}(p)-pp^{\top}$ for $p=\mathrm{softmax}(z)$.
L301: 
L302: ###### Lemma A.1 (KL as a Bregman divergence).
L303: 
L304: Let $p=\mathrm{softmax}(z)$ and $q=\mathrm{softmax}(z^{\prime})$. Then $D_{\mathrm{KL}}(p\|q)=A(z^{\prime})-A(z)-\nabla A(z)^{\top}(z^{\prime}-z)$.
L305: ###### Proof.
L306: 
L307: By the log-softmax identities $\log p_{i}=z_{i}-A(z)$ and $\log q_{i}=z^{\prime}_{i}-A(z^{\prime})$, we have:
L308:  | $\displaystyle D_{\mathrm{KL}}$  | $\displaystyle(p\|q)=\sum_{i}p_{i}\left(\log p_{i}-\log q_{i}\right)$  |
L309:  |  | $\displaystyle=\sum_{i}p_{i}\left[(z_{i}-A(z))-(z^{\prime}_{i}-A(z^{\prime}))\right]$  |
L310:  |  | $\displaystyle=(A(z^{\prime})-A(z))\sum_{i}p_{i}-\sum_{i}p_{i}(z^{\prime}_{i}-z_{i})$  |
L311:  |  | $\displaystyle=A(z^{\prime})-A(z)-\nabla A(z)^{\top}(z^{\prime}-z),$  |  | (4)
L312: 
L313: where the last step follows from $\sum_{i}p_{i}=1$ and the fact that $\nabla A(z)=p$. ∎
L314: ###### Lemma A.2 (Second-order expansion around $z_{d}$).
L315: 
L316: Let $P_{d}=\mathrm{softmax}(z_{d})$, $P_{t}=\mathrm{softmax}(z_{t})$ and write $z_{t}=z_{d}+\delta$. Conditioned on accepted prefixes in speculative sampling, the two models are close so that $\|\delta\|$ is small (large discrepancies are rejected and do not contribute). Then $D_{\mathrm{KL}}(P_{t}\|P_{d})=\frac{1}{2}\,\delta^{\top}F(P_{d})\,\delta+O(\|\delta\|^{3})$, where $F(P_{d})=\nabla^{2}A(z_{d})=\mathrm{diag}(P_{d})-P_{d}P_{d}^{\top}$.
L317: ###### Proof.
L318: Applying Lemma cite104†A.1 with $p=P_{t}$ and $q=P_{d}$, and noting $z_{d}-z_{t}=-\delta$, we have the identity $D_{\mathrm{KL}}(P_{t}\|P_{d})=A(z_{d})-A(z_{t})+P_{t}^{\top}\delta$. We expand $A(z_{t})$ to the second order as $A(z_{t})=A(z_{d})+P_{d}^{\top}\delta+\frac{1}{2}\delta^{\top}F(P_{d})\delta+O(\|\delta\|^{3})$.
L319: Similarly, expanding $P_{t}$ to the first order gives $P_{t}=P_{d}+F(P_{d})\delta+O(\|\delta\|^{2})$, which implies $P_{t}^{\top}\delta=P_{d}^{\top}\delta+\delta^{\top}F(P_{d})\delta+O(\|\delta\|^{3})$. Substituting these expressions into the KL identity leads to the cancellation of linear terms, yielding $D_{\mathrm{KL}}(P_{t}\|P_{d})=\frac{1}{2}\delta^{\top}F(P_{d})\delta+O(\|\delta\|^{3})$. ∎
L320: ###### Corollary A.3 (KL’s quadratic form controlled by a linear map of the concatenated state).
L321: 
L322: Recall that $\delta=z_{t}-z_{d}$ and $\delta=Mx+c$ with $x=[h_{t};h_{d}]$. Combining the second-order expansion in Lemma cite105†A.2 with $\delta=Mx+c$, we obtain
L323: 
L324:  | $$D_{\mathrm{KL}}(P_{t}\|P_{d})\approx\frac{1}{2}\,(Mx+c)^{\top}F(P_{d})\,(Mx+c).$$  |  | (5)
L325: 
L326: #### A.1.2 Pairwise form: KL as a Fisher-weighted sum of primitives
L327: ###### Lemma A.4 (Pairwise decomposition of the Fisher quadratic form).
L328: 
L329: Let $p\in\mathbb{R}^{V}$ satisfy $p_{i}\geq 0$ and $\sum_{i=1}^{V}p_{i}=1$, and let $F(p)=\mathrm{diag}(p)-pp^{\top}$. Then for any $\delta\in\mathbb{R}^{V}$,
L330: 
L331:  | $$\frac{1}{2}\,\delta^{\top}F(p)\,\delta=\frac{1}{4}\sum_{i=1}^{V}\sum_{j=1}^{V}p_{i}p_{j}\,(\delta_{i}-\delta_{j})^{2}.$$  |  | (6)
L332: ###### Proof.
L333: 
L334: Expand the left-hand side using $F(p)=\mathrm{diag}(p)-pp^{\top}$, we have
L335: 
L336:  | $\displaystyle\delta^{\top}F(p)\,\delta$  | $\displaystyle=\delta^{\top}\mathrm{diag}(p)\,\delta-\delta^{\top}(pp^{\top})\delta$  |
L337:  |  | $\displaystyle=\sum_{i=1}^{V}p_{i}\delta_{i}^{2}-\bigl(p^{\top}\delta\bigr)^{2}$  |  | (7)
L338:  |  | $\displaystyle=\sum_{i=1}^{V}p_{i}\delta_{i}^{2}-\Bigl(\sum_{i=1}^{V}p_{i}\delta_{i}\Bigr)^{2}.$  |  | (8)
L339: 
L340: Expand the right-side pairwise sum, we have
L341:  |  | $\displaystyle\sum_{i=1}^{V}\sum_{j=1}^{V}p_{i}p_{j}(\delta_{i}-\delta_{j})^{2}=\sum_{i,j}p_{i}p_{j}(\delta_{i}^{2}+\delta_{j}^{2}-2\delta_{i}\delta_{j})$  |
L342:  |  | $\displaystyle=\sum_{i,j}p_{i}p_{j}\delta_{i}^{2}+\sum_{i,j}p_{i}p_{j}\delta_{j}^{2}-2\sum_{i,j}p_{i}p_{j}\delta_{i}\delta_{j}$  |
L343:  |  | $\displaystyle=2\sum_{i}p_{i}\delta_{i}^{2}-2\Bigl(\sum_{i}p_{i}\delta_{i}\Bigr)^{2},$  |  | (9)
L344: 
L345: where the last equality follows from Eq. (cite106†8 ). Dividing both sides by $4$ yields Eq. (cite107†6 ). ∎
L346: ###### Corollary A.5 (KL as quadratic aggregation of $\Delta_{ij}$).
L347: 
L348: Combining Lemma cite105†A.2 and Lemma cite108†A.4 with $p=P_{d}$ and $\Delta_{ij}(x)=\delta_{i}-\delta_{j}$, we have $D_{\mathrm{KL}}(P_{t}\|P_{d})\approx\sum_{i=1}^{V}\sum_{j=1}^{V}\alpha_{ij}\,\Delta_{ij}(x)^{2}$, where $\alpha_{ij}:=\frac{1}{4}\,P_{d}(i)\,P_{d}(j).$
L349: #### A.1.3 Top-K inconsistency and boundary-crossing primitive
L350: The discrete supervision signal used for classifier training is defined through the consistency between the target and draft models’ top-K prediction sets. Since LLMs assign most of the probability mass to a small subset of tokens, agreement of the top-K sets corresponds to similar generation behavior, whereas disagreement serves as an indicator of divergent outputs.
L351: A top-$k$ inconsistency implies the existence of a pair of logits whose pairwise difference crosses the ranking boundaries, yielding a lower bound on the primitive $\Delta_{ij}(x)$. Let $T_{k}(x)$ and $D_{k}(x)$ denote the index sets of the largest $k$ logits under $z_{t}$ and $z_{d}$, respectively. Let $z_{t}^{(k)}$ and $z_{d}^{(k)}$ denote the $k$-th largest logit values of $z_{t}$ and $z_{d}$.
L352: Denote the top-$k$ margins by $\gamma_{t}^{(k)}=z_{t}^{(k)}-z_{t}^{(k+1)}$ and $\gamma_{d}^{(k)}=z_{d}^{(k)}-z_{d}^{(k+1)}$.
L353: ###### Proposition A.6 (Top-$k$ inconsistency implies a boundary-crossing pairwise gap).
L354: 
L355: If $T_{k}(x)\neq D_{k}(x)$, then there exist $i\in T_{k}(x)\setminus D_{k}(x)$ and $j\in D_{k}(x)\setminus T_{k}(x)$ such that $\Delta_{ij}(x)\geq\gamma_{t}^{(k)}+\gamma_{d}^{(k)}$.
L356: ###### Proof.
L357: 
L358: Since $T_{k}(x)\neq D_{k}(x)$, both $T_{k}(x)\setminus D_{k}(x)$ and $D_{k}(x)\setminus T_{k}(x)$ are non-empty. Select any $i\in T_{k}(x)\setminus D_{k}(x)$ and $j\in D_{k}(x)\setminus T_{k}(x)$. For $z_{t}$, $i\in T_{k}(x)$ implies $z_{t}(i)\geq z_{t}^{(k)}$, and $j\notin T_{k}(x)$ implies $z_{t}(j)\leq z_{t}^{(k+1)}$, we have
L359: 
L360:  | $$z_{t}(i)-z_{t}(j)\geq z_{t}^{(k)}-z_{t}^{(k+1)}=\gamma_{t}^{(k)}.$$  |  | (10)
L361: For $z_{d}$, $j\in D_{k}(x)$ implies $z_{d}(j)\geq z_{d}^{(k)}$, and $i\notin D_{k}(x)$ implies $z_{d}(i)\leq z_{d}^{(k+1)}$, we have
L362: 
L363:  | $$z_{d}(i)-z_{d}(j)\leq z_{d}^{(k+1)}-z_{d}^{(k)}=-\gamma_{d}^{(k)}.$$  |  | (11)
L364: 
L365: Combining the above inequalities Eq. (cite109†10 ) and Eq. (cite110†11 ) gives $\Delta_{ij}(x)\geq\gamma_{t}^{(k)}+\gamma_{d}^{(k)}$. ∎
L366: Top-$k$ inconsistency therefore ensures the existence of a boundary-crossing primitive $(i,j)$ whose logit-difference gap exceeds the sum of the target and draft margins. This provides the link between the discrete supervision condition and a continuous deviation in the primitive space, which is used in Appendix cite35†A.1.4 to establish a lower bound on the KL divergence.
L367: #### A.1.4 From boundary-crossing primitives to a KL lower bound
L368: Proposition cite111†A.6 established that a top-$k$ mismatch implies the existence of a boundary-crossing primitive $(i,j)$ whose pairwise logit-difference satisfies $|\Delta_{ij}(x)|\geq\gamma_{t}^{(k)}+\gamma_{d}^{(k)}$. Meanwhile, Corollary cite112†A.5 expresses the KL as a Fisher-weighted quadratic aggregation over all such primitives. Combining these two facts shows that the presence of a boundary-crossing primitive induces a quantitative lower bound on the overall KL divergence.
L369: ###### Proposition A.7 (Boundary-crossing primitive implies a KL lower bound).
L370: 
L371: If for some index pair $(i,j)$ we have $|\Delta_{ij}(x)|\geq\gamma_{t}^{(k)}+\gamma_{d}^{(k)}$, then based on the quadratic expansion in Lemma cite105†A.2 , $D_{\mathrm{KL}}(P_{t}\|P_{d})\ \gtrsim\ \alpha_{ij}\bigl(\gamma_{t}^{(k)}+\gamma_{d}^{(k)}\bigr)^{2}$, where $\alpha_{ij}=\tfrac{1}{4}P_{d}(i)P_{d}(j)$.
L372: ###### Proof.
L373: 
L374: From Corollary cite112†A.5 , dropping the non-negative terms for pairs other than $(i,j)$ yields $D_{\mathrm{KL}}(P_{t}\|P_{d})\approx\sum_{u,v}\alpha_{uv}\Delta_{uv}(x)^{2}\geq\alpha_{ij}\Delta_{ij}(x)^{2}\geq\alpha_{ij}(\gamma_{t}^{(k)}+\gamma_{d}^{(k)})^{2}$. ∎
L375: 
L376: This yields a lower bound on the KL divergence, showing that any top-$k$ inconsistency enforces a separation between the two predictive distributions.
L377: #### A.1.5 Why a linear classifier trained on “importance” aligns with KL screening
L378: 
L379: The subsequent lemma writes $\Delta_{ij}(x)$ explicitly as an affine function of $x$.
L380: 
L381: ###### Lemma A.8 (Affine form of the primitives).
L382: 
L383: For any $i,j\in\{1,\dots,V\}$ there exist $a_{ij}\in\mathbb{R}^{2d}$ and $\kappa_{ij}\in\mathbb{R}$ such that $\Delta_{ij}(x)=a_{ij}^{\top}x+\kappa_{ij}$.
L384: ###### Proof.
L385: Let $e_{i}\in\mathbb{R}^{V}$ denote the $i$-th standard basis vector. By definition, $z_{t}=W_{t}h_{t}+b_{t}$ and $z_{d}=W_{d}h_{d}+b_{d}$, hence $z_{t}(i)=e_{i}^{\top}(W_{t}h_{t}+b_{t})$ and $z_{d}(i)=e_{i}^{\top}(W_{d}h_{d}+b_{d})$. Therefore $z_{t}(i)-z_{t}(j)=(e_{i}-e_{j})^{\top}(W_{t}h_{t}+b_{t})$ and $z_{d}(i)-z_{d}(j)=(e_{i}-e_{j})^{\top}(W_{d}h_{d}+b_{d})$.
L386: Subtracting the two identities gives $\Delta_{ij}(x)=(e_{i}-e_{j})^{\top}W_{t}h_{t}-(e_{i}-e_{j})^{\top}W_{d}h_{d}+(e_{i}-e_{j})^{\top}(b_{t}-b_{d})$. Define $a_{ij}:=\bigl[\,W_{t}^{\top}(e_{i}-e_{j});\,-W_{d}^{\top}(e_{i}-e_{j})\,\bigr]$ and $\kappa_{ij}:=(e_{i}-e_{j})^{\top}(b_{t}-b_{d})$. Using $x=[h_{t};h_{d}]$ yields $\Delta_{ij}(x)=a_{ij}^{\top}x+\kappa_{ij}$. ∎
L387: ###### Proposition A.9 (Representation of the classifier in the primitive basis).
L388: Let $\mathrm{Cls}(x)=\sigma(w^{\top}x+b)$ be a linear classifier trained on the concatenated representation $x$. In LLMs, the vocabulary size $V$ is typically much larger than the hidden dimension $d$ ($V\gg d$). Consequently, the set of primitive direction vectors $\{\,a_{ij}\mid i,j=1,\dots,V\,\}$ forms an overcomplete frame that effectively spans the feature space $\mathbb{R}^{2d}$.
L389: The classifier’s weight vector $w$ can therefore be expressed as a linear combination of primitives $w=\sum_{i=1}^{V}\sum_{j=1}^{V}\beta_{ij}\,a_{ij}$ for a set of coefficients $\{\beta_{ij}\}$. Accordingly, the classifier is equivalent to $\mathrm{Cls}(x)=\sigma\!\left(\sum_{i=1}^{V}\sum_{j=1}^{V}\beta_{ij}\,\Delta_{ij}(x)+b^{\prime}\right)$, for an adjusted bias term $b^{\prime}$.
L390: This representation indicates that the decision surface can be well characterized by a linear combination of the primitives $\Delta_{ij}(x)$.
L391: ###### Proof.
L392: 
L393: Because the set $\{\,a_{ij}\mid i,j=1,\dots,V\,\}$ effectively spans the feature space $\mathbb{R}^{2d}$, the classifier weight vector $w$ admits the expansion $w=\sum_{i=1}^{V}\sum_{j=1}^{V}\beta_{ij}a_{ij}$. Substituting the affine form of each primitive from Lemma cite113†A.8 , we obtain
L394:  | $\displaystyle w^{\top}x $  | $\displaystyle=\Bigl(\sum_{i=1}^{V}\sum_{j=1}^{V}\beta_{ij}a_{ij}\Bigr)^{\top}x =\sum_{i=1}^{V}\sum_{j=1}^{V}\beta_{ij}(a_{ij}^{\top}x)$  |
L395:  |  | $\displaystyle=\sum_{i=1}^{V}\sum_{j=1}^{V}\beta_{ij}\bigl(\Delta_{ij}(x)-\kappa_{ij}\bigr).$  |  | (12)
L396: By defining the bias $b^{\prime}:=b-\sum_{i=1}^{V}\sum_{j=1}^{V}\beta_{ij}\kappa_{ij}$, the classifier can be rewritten in terms of $\Delta_{ij}(x)$ as $w^{\top}x+b=\sum_{i=1}^{V}\sum_{j=1}^{V}\beta_{ij}\,\Delta_{ij}(x)+b^{\prime}$, which yields $\mathrm{Cls}(x)=$ $\sigma\!\left(\sum_{i=1}^{V}\sum_{j=1}^{V}\beta_{ij}\,\Delta_{ij}(x)+b^{\prime}\right)$. ∎
L397: Corollary cite112†A.5 provides the second-order primitive expansion of the KL divergence. Together with Proposition cite114†A.9 , this yields the following formal juxtaposition in the primitive coordinate system
L398: 
L399:  | $$\left\{\begin{aligned} &D_{\mathrm{KL}}(P_{t}\|P_{d})\approx\sum_{i=1}^{V}\sum_{j=1}^{V}\tfrac{1}{4}\,P_{d}(i)P_{d}(j)\Delta_{ij}(x)^{2},\\[6.0pt]
L400: &\mathrm{Cls}(x)\ \equiv\ \sigma\!\left(\sum_{i=1}^{V}\sum_{j=1}^{V}\beta_{ij}\,\Delta_{ij}(x)+b^{\prime}\right),\end{aligned}\right.$$  |
L401: The first line corresponds to a weighted quadratic aggregation of the primitives $\Delta_{ij}(x)$, whereas the second line represents a linear aggregation over the same primitive basis, demonstrating that the classifier operates directly on the fundamental components of the KL divergence. Consequently, the structural correspondence asserted in Theorem cite68†4.1 is formally established.
L402: cite115†Image: Refer to caption Figure 12: Accuracy and MAT on GSM8K for Llama-3.2-1B-Instruct and Llama-3.1-8B-Instruct (with Qwen3-Max as the annotator). Figure 13: Prompt for critical-token annotation, using Qwen3-Max as the LLM annotator. Figure 14: Example of Qwen3-Max annotation on the GSM8K (Question ID: 5), with [ERROR$\_$START] and [ERROR$\_$END] marking critical tokens in the draft model’s erroneous solution.
L403: ### A.2 Additional Experiment Details
L404: We conduct experiments on four benchmarks: GSM8K and MATH-500-Hard for math reasoning, MMLU-Pro for broad-coverage knowledge and reasoning, and LiveCodeBench for code generation. GSM8K consists of grade-school math word problems that require multi-step numerical reasoning. We additionally evaluate on MATH-500-Hard, which we construct by selecting all Level-5 problems from MATH-500, to introduce a math distribution that differs from GSM8K and is substantially more challenging.
L405: MMLU-Pro is a more difficult variant of MMLU spanning a wide range of subjects. LiveCodeBench focuses on algorithmic code generation with execution-based evaluation. To manage end-to-end decoding cost, we run evaluation on held-out subsets. For GSM8K, we evaluate on 400 examples from the test split, while AutoJudge training uses the full GSM8K training split. For MMLU-Pro, we evaluate on 100 examples.
L406: For LiveCodeBench, we partition the dataset into five folds, use four folds to train the AutoJudge classifier, and reserve the remaining fold as the shared test set for all methods. All experiments are run on NVIDIA A6000, L40, and V100 GPUs. For fair and consistent throughput reporting, all vLLM speed measurements are conducted on 8$\times$V100.
L407: ### A.3 Potential of LLM Annotation
L408: Given the limitations of labor-intensive manual annotation and the high computational overhead of heuristic mining, a natural alternative is to leverage an LLM as a surrogate annotator to provide supervision for judge training. In this appendix, we explore the feasibility of using Qwen3-Max^{1}^{1} 1 cite116†https://qwen.ai/blog?id=qwen3-max†qwen.ai as an automatic labeler to identify logic-pivoting tokens in erroneous generations.
L409: We construct an annotation set from the GSM8K training split by first filtering for instances where the target model produces a correct final answer while the draft model produces an incorrect one. From this subset, we then sample 2,000 examples.
L410: For each problem, we provide Qwen3-Max with the problem statement, the draft model’s erroneous output, and the target model’s verified correct answer, prompting it to highlight the specific words or tokens in the draft output that lead to the incorrect final answer (i.e., error-triggering or logic-pivoting tokens). The detailed prompt is shown in Figure cite117†13 . We then use these token-level annotations to train a lightweight linear classifier following the same training methodology as AutoJudge.
L411: In total, the annotation cost is approximately 2M tokens (about $10).
L412: The results in Figure cite118†12 indicate that the judge trained on Qwen3-Max-labeled data consistently underperforms the judge trained with AutoJudge-mined labels in the low-performance-loss regime (upper-left region of the curve). In other words, although LLM annotation is substantially cheaper than counterfactual rollout-based mining, its supervision does not yield a more accurate token accept/reject rule when decoding requires high precision (i.e., minimal quality degradation).
L413: This gap suggests a key limitation of LLM-based annotation in our setting. This issue is also mentioned in cite51†Bachmann et al. (2025) : using LLMs for this purpose proved to be too imprecise. Qwen3-Max may highlight tokens that look suspicious from a general semantic perspective, but these tokens are not always the ones that flip the final outcome of the generation.
L414: As a result, the labels can be informative but less well aligned with what judge decoding needs, especially in the high-precision regime where a small amount of label noise can noticeably worsen the quality–speed trade-off. Please refer to Figures cite119†14 -cite120†15 for annotation examples.
L415: Figure 15: Example of Qwen3-Max annotation on the GSM8K (Question ID: 68), with [ERROR$\_$START] and [ERROR$\_$END] marking critical tokens in the draft model’s erroneous solution.
L416: 
L417: Experimental support, please cite121†view the build logs for errors. Generated by cite122†L A T E xml†math.nist.gov .
L418: ## Instructions for reporting errors
L419: 
L420: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:
L421: 
L422:   * Click the "Report Issue" () button, located in the page header.
L423: 
L424: Tip: You can select the relevant text first, to include it in your report.
L425: Our team has already identified cite123†the following issues†github.com . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.
L426: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a cite124†list of packages that need conversion†github.com , and welcome cite125†developer contributions†github.com .
L427: 
L428: We gratefully acknowledge support from our major funders, cite126†member institutions†info.arxiv.org , , and all contributors.
L429: cite127†About†info.arxiv.org · cite128†Help†info.arxiv.org · cite129†Contact†info.arxiv.org · cite130†Subscribe†info.arxiv.org · cite131†Copyright†info.arxiv.org · cite132†Privacy†info.arxiv.org · cite133†Accessibility†info.arxiv.org · cite134†Operational Status (opens in new tab)†status.arxiv.org L430: 
L431: Major funding support from

