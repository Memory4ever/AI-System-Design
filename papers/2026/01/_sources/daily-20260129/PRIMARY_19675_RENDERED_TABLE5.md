# Exact v1 HTML — necessary Table5 recovery

Source: https://arxiv.org/html/2601.19675v1
DOM section S4.SS5; stdlib HTMLParser removes math/svg/ltx_ERROR and renderer-only lxSVG data. This is primary HTML text recovery, not new evidence or experiment reproduction. Only Table5 numeric cells and accompanying discussion are used; renderer-only color tags are omitted.

Table 5: Ablation on different components in LoPRo under 2-bit LLaMA2-7b. ‘NA’ means non-use of such strategy. ‘OQ’ and ‘VQ’ denote use GPTQ and GPTVQ as the quantizer respectively. The last two bolded lines represent LoPRo and LoPRo_v.

| Bits | Rotation | Quant | PPL | Avg.acc |
| --- | --- | --- | --- | --- |
| 16 | NA | NA | 5.11 | 66.8 |
| 2.2 | NA | RTN | 4.0e2 | 44.1 |
| 2.2 | NA | OQ | 8.4 | 53.0 |
| 2.2 | Full | OQ | 9.49 | 51.5 |
| 2.2 | Partial | OQ | 7.39 | 57.8 |
| 2.2 | Partial | VQ | 6.53 | 61.2 |

Original discussion: Models using simple RTN within scaled low-rank quantization exhibit severe performance degradation, improved by minimizing proxy loss. Full transformation reduces accuracy to 51.5%; partial block with permutation improves measured perplexity and accuracy. Upgrading to vector quantization changes the quantizer and PPL to 6.53, not an isolated permutation ablation.

Also recovered necessary Table1 negative comparison at DOM S4.SS1: LLaMA2-7B GPTVQ effective 2.13bit PPL6.89 vs LoPRo 2.17bit PPL7.39; LoPRo_v 2.17bit PPL6.53 uses a different vector-quantized residual. Not all component combinations or scalar quantization are superior.
