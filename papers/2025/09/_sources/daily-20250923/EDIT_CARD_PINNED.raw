---
license: apache-2.0
language:
- en
- zh
library_name: diffusers
pipeline_tag: image-to-image
---
<p align="center">
    <img src="https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-Image/qwen_image_edit_logo.png" width="400"/>
<p>
<p align="center">
          💜 <a href="https://chat.qwen.ai/"><b>Qwen Chat</b></a>&nbsp&nbsp | &nbsp&nbsp🤗 <a href="https://huggingface.co/Qwen/Qwen-Image-Edit-2509">Hugging Face</a>&nbsp&nbsp | &nbsp&nbsp🤖 <a href="https://modelscope.cn/models/Qwen/Qwen-Image-Edit-2509">ModelScope</a>&nbsp&nbsp | &nbsp&nbsp 📑 <a href="https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-Image/Qwen_Image.pdf">Tech Report</a> &nbsp&nbsp | &nbsp&nbsp 📑 <a href="https://qwenlm.github.io/blog/qwen-image-edit/">Blog</a> &nbsp&nbsp 
<br>
🖥️ <a href="https://huggingface.co/spaces/Qwen/Qwen-Image-Edit">Demo</a>&nbsp&nbsp | &nbsp&nbsp💬 <a href="https://github.com/QwenLM/Qwen-Image/blob/main/assets/wechat.png">WeChat (微信)</a>&nbsp&nbsp | &nbsp&nbsp🫨 <a href="https://discord.gg/CV4E9rpNSD">Discord</a>&nbsp&nbsp| &nbsp&nbsp <a href="https://github.com/QwenLM/Qwen-Image">Github</a>&nbsp&nbsp
</p>

<p align="center">
    <img src="https://qianwen-res.oss-accelerate-overseas.aliyuncs.com/Qwen-Image/edit2509/edit2509_top.jpg" width="1600"/>
<p>


# Introduction
This September, we are pleased to introduce Qwen-Image-Edit-2509, the monthly iteration of Qwen-Image-Edit. To experience the latest model, please visit [Qwen Chat](https://qwen.ai)  and select the "Image Editing" feature.
Compared with Qwen-Image-Edit released in August, the main improvements of Qwen-Image-Edit-2509 include:
* **Multi-image Editing Support**: For multi-image inputs, Qwen-Image-Edit-2509 builds upon the Qwen-Image-Edit architecture and is further trained via image concatenation to enable multi-image editing. It supports various combinations such as "person + person," "person + product," and "person + scene." Optimal performance is currently achieved with 1 to 3 input images.
* **Enhanced Single-image Consistency**: For single-image inputs, Qwen-Image-Edit-2509 significantly improves editing consistency, specifically in the following areas:
  - **Improved Person Editing Consistency**: Better preservation of facial identity, supporting various portrait styles and pose transformations;
  - **Improved Product Editing Consistency**: Better preservation of product identity, supporting product poster editing；
  - **Improved Text Editing Consistency**: In addition to modifying text content, it also supports editing text fonts, colors, and materials；
* **Native Support for ControlNet**: Including depth maps, edge maps, keypoint maps, and more.


## Quick Start

Install the latest version of diffusers
```
pip install git+https://github.com/huggingface/diffusers
```

The following contains a code snippet illustrating how to use `Qwen-Image-Edit-2509`:

```python
import os
import torch
from PIL import Image
from diffusers import QwenImageEditPlusPipeline

pipeline = QwenImageEditPlusPipeline.from_pretrained("Qwen/Qwen-Image-Edit-2509", torch_dtype=torch.bfloat16)
print("pipeline loaded")

pipeline.to('cuda')
pipeline.set_progress_bar_config(disable=None)
image1 = Image.open("input1.png")
image2 = Image.open("input2.png")
prompt = "The magician bear is on the left, the alchemist bear is on the right, facing each other in the central park square."
inputs = {
    "image": [image1, image2],
    "prompt": prompt,
    "generator": torch.manual_seed(0),
    "true_cfg_scale": 4.0,
    "negative_prompt": " ",
    "num_inference_steps": 40,
    "guidance_scale": 1.0,
    "num_images_per_prompt": 1,
}
with torch.inference_mode():
    output = pipeline(**inputs)
    output_image = output.images[0]
    output_image.save("output_image_edit_plus.png")
    print("image saved at", os.path.abspath("output_image_edit_plus.png"))

```

## Showcase

**The primary update in Qwen-Image-Edit-2509 is support for multi-image inputs.**

Let’s first look at a "person + person" example:  
![Person + Person Example](https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-Image/edit2509/%E5%B9%BB%E7%81%AF%E7%89%8719.JPG#center)

Here is a "person + scene" example:  
![Person + Scene Example](https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-Image/edit2509/%E5%B9%BB%E7%81%AF%E7%89%8720.JPG#center)

Below is a "person + object" example:  
![Person + Object Example](https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-Image/edit2509/%E5%B9%BB%E7%81%AF%E7%89%8721.JPG#center)

In fact, multi-image input also supports commonly used ControlNet keypoint maps—for example, changing a person’s pose:  
![ControlNet Keypoint Example](https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-Image/edit2509/%E5%B9%BB%E7%81%AF%E7%89%8722.JPG#center)

Similarly, the following examples demonstrate results using three input images:  
![Three Images Example 1](https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-Image/edit2509/%E5%B9%BB%E7%81%AF%E7%89%8723.JPG#center)  
![Three Images Example 2](https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-Image/edit2509/%E5%B9%BB%E7%81%AF%E7%89%8724.JPG#center)  
![Three Images Example 3](https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-Image/edit2509/%E5%B9%BB%E7%81%AF%E7%89%8725.JPG#center)

---

**Another major update in Qwen-Image-Edit-2509 is enhanced consistency.**

First, regarding person consistency, Qwen-Image-Edit-2509 shows significant improvement over Qwen-Image-Edit. Below are examples generating various portrait styles:  
![Portrait Styles Example](https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-Image/edit2509/%E5%B9%BB%E7%81%AF%E7%89%871.JPG#center)

For instance, changing a person’s pose while maintaining excellent identity consistency:  
![Pose Change with Identity Consistency](https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-Image/edit2509/%E5%B9%BB%E7%81%AF%E7%89%872.JPG#center)

Leveraging this improvement along with Qwen-Image’s unique text rendering capability, we find that Qwen-Image-Edit-2509 excels at creating meme images:  
![Meme Image Example](https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-Image/edit2509/%E5%B9%BB%E7%81%AF%E7%89%873.JPG#center)

Of course, even with longer text, Qwen-Image-Edit-2509 can still render it while preserving the person’s identity:  
![Long Text with Identity Preservation](https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-Image/edit2509/%E5%B9%BB%E7%81%AF%E7%89%874.JPG#center)

Person consistency is also evident in old photo restoration. Below are two examples:  
![Old Photo Restoration 1](https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-Image/edit2509/%E5%B9%BB%E7%81%AF%E7%89%8717.JPG#center)  
![Old Photo Restoration 2](https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-Image/edit2509/%E5%B9%BB%E7%81%AF%E7%89%8718.JPG#center)

Naturally, besides real people, generating cartoon characters and cultural creations is also possible:  
![Cartoon & Cultural Creation](https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-Image/edit2509/%E5%B9%BB%E7%81%AF%E7%89%8715.JPG#center)

Second, Qwen-Image-Edit-2509 specifically enhances product consistency. We find that the model can naturally generate product posters from plain-background product images:  
![Product Poster Example](https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-Image/edit2509/%E5%B9%BB%E7%81%AF%E7%89%875.JPG#center)

Or even simple logos:  
![Logo Generation Example](https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-Image/edit2509/%E5%B9%BB%E7%81%AF%E7%89%8716.JPG#center)

Third, Qwen-Image-Edit-2509 specifically enhances text consistency and supports editing font type, font color, and font material:  
![Text Font Type](https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-Image/edit2509/%E5%B9%BB%E7%81%AF%E7%89%8710.JPG#center)  
![Text Font Color](https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-Image/edit2509/%E5%B9%BB%E7%81%AF%E7%89%8711.JPG#center)  
![Text Font Material](https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-Image/edit2509/%E5%B9%BB%E7%81%AF%E7%89%8712.JPG#center)

Moreover, the ability for precise text editing has been significantly enhanced:  
![Precise Text Editing 1](https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-Image/edit2509/%E5%B9%BB%E7%81%AF%E7%89%8713.JPG#center)  
![Precise Text Editing 2](https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-Image/edit2509/%E5%B9%BB%E7%81%AF%E7%89%8714.JPG#center)

It is worth noting that text editing can often be seamlessly integrated with image editing—for example, in this poster editing case:  
![Integrated Text & Image Editing](https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-Image/edit2509/%E5%B9%BB%E7%81%AF%E7%89%876.JPG#center)

---

**The final update in Qwen-Image-Edit-2509 is native support for commonly used ControlNet image conditions, such as keypoint control and sketches:**  
![Keypoint Control Example](https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-Image/edit2509/%E5%B9%BB%E7%81%AF%E7%89%877.JPG#center)  
![Sketch Control Example 1](https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-Image/edit2509/%E5%B9%BB%E7%81%AF%E7%89%878.JPG#center)  
![Sketch Control Example 2](https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-Image/edit2509/%E5%B9%BB%E7%81%AF%E7%89%879.JPG#center)



## License Agreement

Qwen-Image is licensed under Apache 2.0. 

## Citation

We kindly encourage citation of our work if you find it useful.

```bibtex
@misc{wu2025qwenimagetechnicalreport,
      title={Qwen-Image Technical Report}, 
      author={Chenfei Wu and Jiahao Li and Jingren Zhou and Junyang Lin and Kaiyuan Gao and Kun Yan and Sheng-ming Yin and Shuai Bai and Xiao Xu and Yilei Chen and Yuxiang Chen and Zecheng Tang and Zekai Zhang and Zhengyi Wang and An Yang and Bowen Yu and Chen Cheng and Dayiheng Liu and Deqing Li and Hang Zhang and Hao Meng and Hu Wei and Jingyuan Ni and Kai Chen and Kuan Cao and Liang Peng and Lin Qu and Minggang Wu and Peng Wang and Shuting Yu and Tingkun Wen and Wensen Feng and Xiaoxiao Xu and Yi Wang and Yichang Zhang and Yongqiang Zhu and Yujia Wu and Yuxuan Cai and Zenan Liu},
      year={2025},
      eprint={2508.02324},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2508.02324}, 
}
```