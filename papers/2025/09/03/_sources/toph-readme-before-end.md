# Top-H Decoding

**Top-H** is a **training-free** decoding method that balances **creativity** and **coherence** in open-ended text generation by **constraining entropy** at each step. It solves an **entropy-constrained mass maximization** problem with an efficient greedy procedure, yielding robust, high-temperature generations that remain coherent.

> 📄 This repository accompanies our paper:
> **Top-H Decoding: Adapting the Creativity and Coherence with Bounded Entropy in Text Generation**

---

## 🧭 Table of Contents
- [Overview](#-overview)
- [Key Features](#-key-features)
- [Results Summary](#-results-summary)
- [Installation](#-installation)
- [Reproducing Paper Results](#-reproducing-paper-results)
- [Method Details](#-method-details)
- [Tuning & Tips](#-tuning--tips)
- [Citation](#-citation)
- [Contact](#-contact)

---

## 🚀 Overview

Classic truncated sampling (temperature, top-k, top-p, **min-p**) trades off diversity vs. coherence but often ignores the **shape** of the next-token distribution. **Top-H** makes this trade-off explicit by **upper-bounding the entropy** of the truncated distribution relative to the original model distribution — exploring more when the model is unsure, and tightening when it is confident.

At a glance:
- Formulates **Entropy-Constrained Minimum Divergence (ECMD)** and proves equivalence to **Entropy-Constrained Mass Maximization (ECMM)** (NP-hard).
- Introduces a **greedy** approximation (**Top-H**) with a simple **termination guarantee** controlled by an entropy scale **α**.
- Delivers strong empirical gains over **min-p** and **top-p**, especially at **higher temperatures**.

---

## 🧠 Key Features

- 🛠 **Training-free & model-agnostic** — drop-in decoding; no fine-tuning.
- 🎛 **Entropy-aware truncation** — caps randomness via **H(q) ≤ α·H(p)**, recalculated **every step**.
- 🧮 **Theory-backed** — ECMD ⇔ ECMM (NP-hard); practical greedy rule with early-stop criterion.
- 🔥 **Robust at high temperature** — maintains coherence where min-p/top-p degrade.
- 🧪 **Wide evaluation** — creative writing (e.g., Alpaca-Eval, MT-Bench) and QA (GPQA, GSM8K).

---

## 📊 Results Summary

- On creative writing benchmarks, **Top-H** outperforms SoTA alternatives by **up to 25.63%**, while preserving consistency.
- On reasoning datasets (**GSM8K**, **GPQA**), Top-H remains robust at elevated temperatures.

### Example (from paper)

| Benchmark / Model / T           | min-p | top-p | **Top-H** |
|:---------------------------------:|:------:|:------:|:----------:|
| **GSM8K** — LLaMA-3.1-8B — T=2 | 13.72 |  2.65 | **39.35** |
| **GPQA** — Phi-3-Mini — T=2     | 23.44 | 18.53 | **30.80** |

> See the paper for full tables, settings, and ablations.

---

## 📦 Installation

```bash
git clone https://github.com/your-org/top-h-decoding.git
cd Top-H-Decoding
pip install -r requirements.txt
```

---

## 🔬 Reproducing Paper Results

### AlpacaEval
```bash
bash alpaca_evaluate.sh
```
### LM Evaluation Harness

1. Clone the [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) repository:
   ```bash
   git clone --depth 1 https://github.com/EleutherAI/lm-evaluation-harness
   cd lm-evaluation-harness
   pip install -e .
   ```
2. Replace the huggingface.py file from this repo into the lm-evaluation-harness repo:
   ```bash
   cp -f ./Top-H-Decoding/huggingface.py ./lm-evaluation-harness/lm_eval/models
   ```
3. Run the evaluation script:
   ```bash
   bash lm_evaluate.sh
   ```

## 🤖 Inference with Top-H Decoding

This section demonstrates how to perform inference using a **Top-H decoding strategy** with Hugging Face models.
You can easily create an instance of `TopH_LogitsProcessor` and pass it to `model.generate()`.

### Example

```python
from logit_processor import *
from transformers import AutoModelForCausalLM, AutoTokenizer

# Choose your model
model_name = "meta-llama/Llama-3.1-8B-Instruct"

# Load model and tokenizer
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="auto",
    torch_dtype="auto"
)
model.eval()
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Create Top-H logits processor
lp = TopH_LogitsProcessor(temperature=0.3)

# Define prompt
prompt = """Write a creative story about time moving backwards."""
input_ids = tokenizer(prompt, return_tensors="pt")["input_ids"].to(model.device)

# Generate output
output = model.generate(
    input_ids=input_ids,
    temperature=0.3,
    logits_processor=[lp],   # inject custom processor
    top_p=None,              # disable nucleus sampling
    max_new_tokens=512
)

print("output:\n")
print(tokenizer.decode(output[0], skip_special_tokens=True))
```
## 📐 Method Details
-----------------

* **ECMD** (conceptual): minimize divergence (e.g., JSD) between the model’s original distribution **p** and a truncated distribution **q**, under an entropy cap **H(q) ≤ α·H(p)**.

* **Equivalence**: ECMD ⇔ **ECMM** (maximize retained probability mass subject to the same entropy bound).

* **Complexity**: ECMM is **NP-hard**; **Top-H** uses a **greedy** accumulation over sorted tokens, with a **stop rule** when adding the next token would exceed the entropy budget.

* **Adaptivity**: The threshold **α·H(p)** is **recomputed at each time step**, so Top-H loosens up when the model is uncertain and tightens when confident.


## 🔧 Tuning & Tips
----------------

* **α (entropy scale)**: primary knob.
  * Lower α → **tighter**, more coherent, shorter candidate sets.
  * Higher α → **looser**, more diverse, longer candidate sets.
  * We commonly use **α ≈ 0.3–0.5**.
* **Temperature**: Top-H plays well with **higher T**; entropy constraint maintains coherence.
* **Fallback**: In rare numerical edge cases selecting no tokens, fall back to argmax or include top-1.

## 📎 Citation
-----------

If you use Top-H in your research, please cite:

```bibtex
@article{,
  title   = {},
  author  = {},
  year    = {2025},
  note    = {Preprint}
}
```


## 📫 Contact
----------

For questions or collaboration, reach out:

- **Seyedarmin Azizi** — [seyedarm@usc.edu](mailto:seyedarm@usc.edu)
- **Erfan Baghaei Potraghloo** — [baghaeip@usc.edu](mailto:baghaeip@usc.edu)
