---
license: cc-by-nc-4.0
base_model:
- Qwen/Qwen3-14B
- google/siglip2-so400m-patch16-384
library_name: transformers
tags:
- multimodal
- conversational
- ncsoft
- ncai
- varco
pipeline_tag: image-text-to-text
language:
- en
- ko
---

# VARCO-VISION-2.0-14B

<div align="center">
   <img src="./varco-vision.png" width="100%" style="background-color:white; padding:10px;" />
</div>

## Introduction
**VARCO-VISION-2.0** is a multimodal AI model capable of understanding both images and text to answer user queries. It supports multi-image inputs, enabling effective processing of complex content such as documents, tables, and charts. The model demonstrates strong comprehension in both Korean and English, with significantly improved text generation capabilities and a deeper understanding of Korean cultural context. Compared to its predecessor, performance has been notably enhanced across various benchmarks, and its usability in real-world scenarios—such as everyday Q&A and information summarization—has also improved.

In addition to the 14B full-scale model, a lightweight 1.7B version is available for on-device use, making it accessible on personal devices such as smartphones and PCs. VARCO-VISION-2.0 is a powerful open-weight AI model built for Korean users and is freely available for a wide range of applications.

## 🚨News🎙️
- 📝 2025-09-12: We published the technical report of VARCO-VISION-2.0 at [link](https://arxiv.org/abs/2509.10105)
- 🛠️ 2025-08-22: We updated the checkpoint of VARCO-VISION-2.0-1.7B for improved performance.
- 📰 2025-07-28: We released VARCO-VISION-2.0-1.7B-OCR at [link](https://huggingface.co/NCSOFT/VARCO-VISION-2.0-1.7B-OCR)
- 📰 2025-07-28: We released VARCO-VISION-2.0-1.7B at [link](https://huggingface.co/NCSOFT/VARCO-VISION-2.0-1.7B)
- 🛠️ 2025-07-18: We updated the checkpoint of VARCO-VISION-2.0-14B for improved performance.
- 📰 2025-07-16: We released VARCO-VISION-2.0-14B at [link](https://huggingface.co/NCSOFT/VARCO-VISION-2.0-14B)
- 📰 2025-07-16: We released GME-VARCO-VISION-Embedding at [link](https://huggingface.co/NCSOFT/GME-VARCO-VISION-Embedding)

## Key Features
- **Multi-image Understanding**: Newly added support for multi-image inputs enables the model to analyze multiple images simultaneously and make more holistic and context-aware decisions.
- **Korean Language Specialization**: The model is further specialized for Korean, with a deeper understanding of Korean language, context, and culture. Korean text generation has been significantly improved, resulting in more natural, fluent, and accurate responses.
- **OCR with Text Localization**: Unlike typical models that only recognize and generate text from images, VARCO-VISION-2.0 can also identify the position of the text and provide bounding boxes around it. This makes it especially useful for document understanding, signage interpretation, and structured visual data.
- **Enhanced Safety**: The model now offers improved handling of harmful or sexually explicit content, ensuring safer and more reliable interactions.

<div align="center">
    <img src="./figure.png" width="100%" />
</div>

## VARCO-VISION-2.0 Family
| Model Name                 | Base Models (Vision / Language)                                                                                                               | HF Link                                                          |
| :------------------------: | :-------------------------------------------------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------: |
| VARCO-VISION-2.0-14B       | [siglip2-so400m-patch16-384](https://huggingface.co/google/siglip2-so400m-patch16-384) / [Qwen3-14B ](https://huggingface.co/Qwen/Qwen3-14B)  | [link](https://huggingface.co/NCSOFT/VARCO-VISION-2.0-14B)       |
| VARCO-VISION-2.0-1.7B      | [siglip2-so400m-patch16-384](https://huggingface.co/google/siglip2-so400m-patch16-384) / [Qwen3-1.7B](https://huggingface.co/Qwen/Qwen3-1.7B) | [link](https://huggingface.co/NCSOFT/VARCO-VISION-2.0-1.7B)      |
| VARCO-VISION-2.0-1.7B-OCR  | [siglip2-so400m-patch16-384](https://huggingface.co/google/siglip2-so400m-patch16-384) / [Qwen3-1.7B](https://huggingface.co/Qwen/Qwen3-1.7B) | [link](https://huggingface.co/NCSOFT/VARCO-VISION-2.0-1.7B-OCR)  |
| GME-VARCO-VISION-Embedding | [Qwen2-VL-7B-Instruct](https://huggingface.co/Qwen/Qwen2-VL-7B-Instruct)                                                                      | [link](https://huggingface.co/NCSOFT/GME-VARCO-VISION-Embedding) |

## Model Architecture
VARCO-VISION-2.0 follows the architecture of [LLaVA-OneVision](https://arxiv.org/abs/2408.03326).

## Evaluation
We used [VLMEvalKit](https://github.com/open-compass/VLMEvalKit) for evaluation whenever possible, and conducted our own implementations only for benchmarks not supported by the toolkit, **ensuring fair comparisons** with various open-weight models.
Please note that for certain benchmarks involving LLM-based evaluation (e.g., LLaVABench), results may not be exactly reproducible due to variations in the underlying LLM behavior.

### Korean Benchmark
| Benchmark     | InternVL3-14B | Ovis2-16B | Qwen2.5-VL-7B | VARCO-VISION-2.0-14B |
| :-----------: | :-----------: | :-------: | :-----------: | :------------------: |
| K-MMBench_DEV | **89.1**      | 86.0      | 84.7          | *87.7*               |
| K-MMStar      | **64.9**      | 29.7      | 49.3          | *63.6*               |
| K-SEED        | **78.2**      | 73.2      | 75.7          | 77.2                 |
| K-LLaVA-W     | 80.9          | 86.3      | *94.1*        | **96.5**             |
| K-DTCBench    | *87.9*        | 81.7      | 82.1          | 78.3                 |
| ***AVERAGE*** | *80.2*        | 71.4      | 77.2          | **80.7**             |

### English Benchmark
| Benchmark       | InternVL3-14B | Ovis2-16B | Qwen2.5-VL-7B | VARCO-VISION-2.0-14B |
| :-------------: | :-----------: | :-------: | :-----------: | :------------------: |
| MMStar          | **68.9**      | *67.2*    | 64.1          | 66.9                 |
| MMMU_VAL        | **64.8**      | 60.7      | 58.0          | *61.9*               |
| MathVista       | **74.4**      | *73.7*    | 68.1          | 73.2                 |
| OCRBench        | 87.7          | *87.9*    | **88.8**      | 86.9                 |
| AI2D            | *86.0*        | **86.3**  | 84.3          | 85.7                 |
| HallusionBench  | *55.9*        | **56.8**  | 51.9          | 53.2                 |
| MMVet           | **80.5**      | 68.4      | *69.7*        | 68.9                 |
| SEEDBench_IMG   | 77.5          | *77.7*    | 77.0          | **78.0**             |
| LLaVABench      | 84.4          | **93.0**  | *91.0*        | 90.2                 |
| RealWorldQA     | 69.8          | *74.1*    | 68.4          | **74.6**             |
| POPE            | **89.4**      | 87.5      | 85.9          | *89.2*               |
| ScienceQA_TEST  | **98.6**      | 95.2      | 89.0          | 93.5                 |
| SEEDBench2_Plus | 70.1          | **72.1**  | 70.7          | *71.9*               |
| BLINK           | **59.9**      | *59.0*    | 55.3          | 54.5                 |
| TextVQA_VAL     | 82.2          | *83.0*    | **85.4**      | 80.4                 |
| ChartQA_TEST    | **87.8**      | 79.1      | 80.6          | *84.2*               |
| Q-Bench1_VAL    | 76.5          | *79.2*    | 78.2          | **79.9**             |
| A-Bench_VAL     | 76.3          | **79.6**  | 75.4          | *79.5*               |
| DocVQA_TEST     | 94.1          | *94.9*    | **95.7**      | 90.9                 |
| InfoVQA_TEST    | **83.6**      | *82.8*    | 82.6          | 80.4                 |
| ***AVERAGE***   | **78.4**      | *77.9*    | 76.0          | 77.2                 |

### Text-only Benchmark
| Benchmark     | InternVL3-14B | Ovis2-16B | Qwen2.5-VL-7B | VARCO-VISION-2.0-14B |
| :-----------: | :-----------: | :-------: | :-----------: | :------------------: |
| MMLU          | **78.5**      | *78.4*    | 4.6           | 77.9                 |
| MT-Bench      | *89.3*        | 85.9      | 80.7          | **89.8**             |
| KMMLU         | 51.4          | 49.3      | 39.6          | *57.5*               |
| KoMT-Bench    | 70.1          | **79.1**  | 68.4          | *78.3*               |
| LogicKor      | 70.0          | **79.4**  | 65.5          | *74.0*               |
| ***AVERAGE*** | 71.9          | *74.4*    | 51.7          | **75.5**             |

> **Note:** Some models show unusually low performance on the MMLU benchmark. This is primarily due to their failure to correctly follow the expected output format when only few-shot exemplars are provided in the prompts. Please take this into consideration when interpreting the results.

### Korean Cultural Benchmark
| Benchmark        | InternVL3-14B | Ovis2-16B | Qwen2.5-VL-7B | VARCO-VISION-2.0-14B |
| :--------------: | :-----------: | :-------: | :-----------: | :------------------: |
| K-Viscuit        | 71.7          | **77.0**  | 70.9          | 73.7                 |
| PangeaBench (ko) | *77.2*        | *76.9*    | 76.6          | 74.5                 |
| ***AVERAGE***    | *74.5*        | **77.0**  | 73.8          | 74.1                 |

### OCR Benchmark
| Benchmark     | PaddleOCR | EasyOCR | VARCO-VISION-2.0-14B |
| :-----------: | :-------: | :-----: | :------------------: |
| CORD          | *91.4*    | 77.8    | **97.1**             |
| ICDAR2013     | *92.0*    | 85.0    | **95.7**             |
| ICDAR2015     | *73.7*    | 57.9    | **79.4**             |
| ***AVERAGE*** | *85.7*    | 73.6    | **90.7**             |

## Usage
To use this model, we recommend installing `transformers` version **4.53.1 or higher**. While it may work with earlier versions, using **4.53.1 or above is strongly recommended**, especially to ensure optimal performance for the **multi-image feature**.

The basic usage is **identical to** [LLaVA-OneVision](https://huggingface.co/docs/transformers/main/en/model_doc/llava_onevision#usage-example):

```python
import torch
from transformers import AutoProcessor, LlavaOnevisionForConditionalGeneration

model_name = "NCSOFT/VARCO-VISION-2.0-14B"
model = LlavaOnevisionForConditionalGeneration.from_pretrained(
    model_name,
    torch_dtype=torch.float16,
    attn_implementation="sdpa",
    device_map="auto",
)
processor = AutoProcessor.from_pretrained(model_name)

conversation = [
    {
        "role": "user",
        "content": [
            {"type": "image", "url": "https://huggingface.co/NCSOFT/VARCO-VISION-2.0-14B/resolve/main/demo.jpg"},
            {"type": "text", "text": "각 박스마다 한 줄씩 색상과 글자를 정확하게 출력해주세요."},
        ],
    },
]

inputs = processor.apply_chat_template(
    conversation,
    add_generation_prompt=True,
    tokenize=True,
    return_dict=True,
    return_tensors="pt"
).to(model.device, torch.float16)
generate_ids = model.generate(**inputs, max_new_tokens=1024)
generate_ids_trimmed = [
    out_ids[len(in_ids) :] for in_ids, out_ids in zip(inputs.input_ids, generate_ids)
]
output = processor.decode(generate_ids_trimmed[0], skip_special_tokens=True)
print(output)
```

<details>
<summary>Multi image inference</summary>

```python
conversation = [
    {
        "role": "user",
        "content": [
            {"type": "image", "image": "file:///path/to/image1.jpg"},
            {"type": "image", "image": "file:///path/to/image2.jpg"},
            {"type": "text", "text": "이미지 간의 유사점을 파악하세요."},
        ],
    },
]
inputs = processor.apply_chat_template(
    conversation,
    add_generation_prompt=True,
    tokenize=True,
    return_dict=True,
    return_tensors="pt"
).to(model.device, torch.float16)
generate_ids = model.generate(**inputs, max_new_tokens=1024)
generate_ids_trimmed = [
    out_ids[len(in_ids) :] for in_ids, out_ids in zip(inputs.input_ids, generate_ids)
]
output = processor.decode(generate_ids_trimmed[0], skip_special_tokens=True)
print(output)
```
</details>

<details>
<summary>Batch inference</summary>
All inputs in a batch must have the same modality structure—for example, text-only with text-only, single-image with single-image, and multi-image with multi-image—to ensure correct batch inference.

```python
conversation_1 = [
    {
        "role": "user",
        "content": [
            {"type": "image", "image": "file:///path/to/image1.jpg"},
            {"type": "text", "text": "이미지를 설명해주세요."},
        ],
    },
]
conversation_2 = [
    {
        "role": "user",
        "content": [
            {"type": "image", "image": "file:///path/to/image2.jpg"},
            {"type": "text", "text": "이 이미지에 표시된 것은 무엇인가요?"},
        ],
    },
]
inputs = processor.apply_chat_template(
    [conversation_1, conversation_2],
    add_generation_prompt=True,
    tokenize=True,
    return_dict=True,
    padding=True,
    return_tensors="pt"
).to(model.device, torch.float16)
generate_ids = model.generate(**inputs, max_new_tokens=1024)
generate_ids_trimmed = [
    out_ids[len(in_ids) :] for in_ids, out_ids in zip(inputs.input_ids, generate_ids)
]
output = processor.batch_decode(generate_ids_trimmed, skip_special_tokens=True)
print(output)
```
</details>

<details>
<summary>OCR inference</summary>

```python
from PIL import Image
image = Image.open("file:///path/to/image.jpg")
# Image upscaling for OCR performance boost
w, h = image.size
target_size = 2304
if max(w, h) < target_size:
    scaling_factor = target_size / max(w, h)
    new_w = int(w * scaling_factor)
    new_h = int(h * scaling_factor)
    image = image.resize((new_w, new_h))
conversation = [
    {
        "role": "user",
        "content": [
            {"type": "image", "image": image},
            {"type": "text", "text": "<ocr>"},
        ],
    },
]
inputs = processor.apply_chat_template(
    conversation,
    add_generation_prompt=True,
    tokenize=True,
    return_dict=True,
    return_tensors="pt"
).to(model.device, torch.float16)
generate_ids = model.generate(**inputs, max_new_tokens=1024)
generate_ids_trimmed = [
    out_ids[len(in_ids) :] for in_ids, out_ids in zip(inputs.input_ids, generate_ids)
]
output = processor.decode(generate_ids_trimmed[0], skip_special_tokens=False)
print(output)
```
</details>


## Citation
```bibtex
@misc{cha2025varcovision20technicalreport,
      title={VARCO-VISION-2.0 Technical Report}, 
      author={Young-rok Cha and Jeongho Ju and SunYoung Park and Jong-Hyeon Lee and Younghyun Yu and Youngjune Kim},
      year={2025},
      eprint={2509.10105},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2509.10105}, 
}
```
