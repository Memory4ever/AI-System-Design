# 📝 No Caption, No Problem: Caption-Free Membership Inference via Model-Fitted Embeddings

**Joonsung Jeon, Woo Jae Kim, Suhyeon Ha, Sooel Son\*, Sung-Eui Yoon\***

<p align="left">
  <a href="https://arxiv.org/abs/2602.22689">
    <img src="https://img.shields.io/badge/arXiv-Paper-b31b1b.svg" alt="Paper">
  </a>
  <a href="https://sgvr.kaist.ac.kr/~joonsung/MoFit/">
    <img src="https://img.shields.io/badge/Project-Page-4b8bbe.svg" alt="Project Page">
  </a>
</p>

> Official implementation of **MoFit** (ICLR 2026) — a **caption-free** membership inference attack (MIA) framework that leverages synthetic conditioning inputs overfitted to the target model's generative manifold.

<p align="center">
  <img src="https://github.com/JoonsungJeon/MoFit/blob/main/figs/teaser3.png" alt="MoFit Teaser" width="90%">
</p>

---


## 🖌️ Requirements

All experiments are tested on **Ubuntu 20.04 / 22.04** with a single **RTX 3090** GPU.

- Python 3.8
- CUDA 11.x

## 📦 Datasets

| Dataset | Source |
|---------|--------|
| Pokemon | [SecMI repository](https://github.com/jinhaoduan/SecMI-LDM) |
| MS-COCO | [HuggingFace](https://huggingface.co/datasets/zsf/COCO_MIA_ori_split1) |
| Flickr | [Kaggle](https://www.kaggle.com/datasets/adityajn105/flickr8k?select=Images) |
| LAION-mi | [HuggingFace](https://huggingface.co/datasets/antoniaaa/laion_mi) |

## 🖌️ Code Instructions

Because the supported datasets require different `diffusers` versions, we maintain two separate environments:

| Environment | Datasets | `diffusers` version |
|-------------|----------|--------------------|
| `MoFit_COCO` | MS-COCO, Flickr | `0.18.2` |
| `MoFit_Pokemon` | Pokemon, LAION-mi | `0.11.1` |

> 💡 To run MoFit on **Flickr**, follow the MS-COCO instructions.
> To run MoFit on **LAION-mi**, follow the Pokemon instructions.

---

### 1. Environment Setup

**MS-COCO / Flickr**
```bash
conda create --name MoFit_COCO python=3.8
conda activate MoFit_COCO
cd MoFit/COCO
pip install -r requirements_Pokemon.txt
pip3 install -U scikit-learn
pip install matplotlib
```

**Pokemon / LAION-mi**
```bash
conda create --name MoFit_Pokemon python=3.8
conda activate MoFit_Pokemon
cd MoFit/Pokemon
pip install -r requirements.txt
pip install matplotlib
pip install ftfy
```

---

### 2. Surrogate & Embedding Optimization

**MS-COCO / Flickr**
```bash
cd MoFit/COCO
bash MoFit_COCO.sh
```

**Pokemon / LAION-mi**
```bash
cd MoFit/Pokemon
bash MoFit_Pokemon.sh
```

**Notes**

- To optimize over **member samples**, uncomment the member-related lines in `GT_ROOT` and `MEM`. For **non-member samples**, uncomment the corresponding non-member lines instead.
- Target noise files (`.npy`) for each dataset are provided under `MoFit/data`.
- Default iteration counts:

  | Stage | Pokemon | Flickr / COCO | LAION-mi |
  |-------|---------|---------------|----------|
  | Surrogate optimization | 1000 | 1000 | 1000 |
  | Embedding extraction | 200 | 300 | 1000 |

---

### 3. Calculate Model Prediction Values

Run the prediction script for any dataset:
```bash
cd MoFit/Eval
python calculate_pred.py
```

- Set the `Use_data_model_name` variable inside `calculate_pred.py` to select the target dataset/model.
- Supported input types:
  - **Embeddings** produced by MoFit
  - **VLM-generated captions** from BLIP-2 or CLIP-Interrogator
- Pre-computed VLM captions are available in `MoFit/data/Captions`.

---

### 4. Evaluate MIA Performance

```bash
cd MoFit/Eval
```

**MS-COCO / Flickr**
```bash
python mia_th_COCO.py
```

**Pokemon / LAION-mi**
```bash
python mia_th_Pokemon.py
```

---

## 📁 Repository Structure

```
MoFit/
├── COCO/           # Scripts and configs for MS-COCO and Flickr
├── Pokemon/        # Scripts and configs for Pokemon and LAION-mi
├── Eval/           # Prediction and MIA evaluation scripts
├── Results/        # Result examples of COCO and Pokemon
└── data/
    ├── *.npy       # Target noise files
    └── Captions/   # VLM-generated captions (BLIP-2, CLIP-Interrogator)
```

---

## 🖌️Bibtex
If you find this code useful for your research, please consider citing our paper:
```
@inproceedings{
jeon2026MoFit,
title={No Caption, No Problem: Caption-Free Membership Inference via Model-Fitted Embeddings},
author={Joonsung Jeon and Woo Jae Kim and Suhyeon Ha and Sooel Son and Sung-eui Yoon},
booktitle={The Fourteenth International Conference on Learning Representations},
year={2026},
url={https://openreview.net/forum?id=KUXLrSXYPv}
}
```
