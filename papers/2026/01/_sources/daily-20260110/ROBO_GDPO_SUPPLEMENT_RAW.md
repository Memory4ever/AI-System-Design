# 必要评价与归一化反侧原返回

RoboVIP: Multi-View Video Generation with Visual Identity Prompting Augments Robot Manipulation (https://arxiv.org/html/2601.05241v1)
citeturn26829view0 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.05241v1","lineno":123}); Total lines: 368
L109: Accordingly, we modify the base model’s input structure by replacing the single-image padding with channel-wise concatenation of the full video sequence, which achieves a minimally invasive yet effective formulation of a video-conditioned objective. The overall model structure can be found in Fig. cite85†3 .
L110: cite86†Image: Refer to caption Figure 4: Visual Identity Curation and Processing Pipeline. Our visual identity is curated by panoptic segmentation from the large-scale robotics dataset [cite48†14 , cite57†45 , cite47†24 ], followed by several scoring criteria filters. In augmentation, we randomly select some from the pool and pack them into one image frame to serve as conditioning for our video diffusion model.
L111: ### 3.4 Visual Identity Prompting
L112: For robotic downstream tasks, we aim for a pipeline that can autonomously select appropriate and necessary visual identities without any human intervention. To achieve this, we design an agentic inference pipeline, as shown in Fig. cite87†4 , that automatically constructs a massive, rich, and diverse visual identity pool. We find that adopting a panoptic segmentation [cite88†26 ] approach is the most straightforward way to achieve this goal.
L113: Panoptic segmentation simultaneously provides mask localization and corresponding label classification. Based on the classification label, we select common objects that are needed and do not consider background-related large objects, like the table and the wall. Using these labels, we can naturally classify both tabletop objects and background elements, ultimately forming a comprehensive visual identity pool. To this end, we constitute a million-scale visual identity pool.
L114: We observe that objects obtained by straightforward segmentation are often of suboptimal quality. Moreover, some of these segmented objects are partially occluded and thus cannot serve as semantically complete visual identity references.
L115: To address this, we crop the corresponding visual identity image predicted by the panoptic segmentation model [cite89†21 ] and then apply several filtering criteria, including image quality assessment [cite90†49 ], sharpness clarity assessment, CLIP-based text–image scoring [cite74†35 ], and resolution size filtering. The CLIP text embedding is derived from the panoptic segmentation class label, serving as an effective proxy to assess the semantic completeness of each object.
L116: Unlike previous approaches that inject only a single identity reference per frame, we adopt a packing scheme to efficiently accommodate multiple visual identity references within a single frame, thereby reducing computational overhead. To prevent overfitting to fixed scale ratios, each identity image is randomly resized before encoding. During training under multi-view supervision, all visual identity references are sampled from a single view to avoid view-ambiguity in identity prompting.
L117: To incorporate visual identity prompting into the video diffusion model, we adopt a frame-wise concatenation strategy, following the design of [cite63†47 , cite91†58 ]. As illustrated in Fig. cite85†3 , before entering the video diffusion transformer, the packed identity images are first encoded by a shared causal VAE encoder [cite59†46 ] and concatenated with the latent video segmentation inputs along the frame dimension.
L118: The noisy frame latent is zero-padded for temporal alignment and then channel-wise concatenated with the conditional inputs. After the diffusion transformer processes all layers, the identity tokens are dropped and excluded from loss computation, ensuring they serve purely as contextual guidance rather than optimization targets. During inference, newly encoded identity images are injected at each diffusion timestep to continuously guide generation.
L119: ## 4 Experiment
L120: 
L121: cite92†Image: Refer to caption Figure 5: Qualitative comparisons of different models on Droid [cite47†24 ]. Our method produces temporally consistent and visually diverse results, outperforming RoboEngine [cite43†53 ], which is a single-image-based method, and Cosmos-Transfer2.5 [cite53†3 ], which struggles to generalize beyond appearance-level edge conditioning. Zoom in for the best view.
L122: ### 4.1 Video Diffusion Model Implementation Details
L123: Data Curation. For all videos, we first discard sequences that are too short (fewer than 25 frames). For overly long sequences (more than 550 frames), we perform temporal cropping to mitigate segmentation failures induced by excessively extended inputs.
L124: Since the captions provided by the original dataset are often noisy, we re-caption all videos using Qwen2.5-VL 32B [cite50†6 ], employing a multi-view vertical stitching strategy to ensure consistent and accurate textual descriptions across different viewpoints. The text prompt is composed of the scene setup and the action description. Then, for the robot and object segmentation described in the method section, we adopt OneFormer [cite89†21 ] for the panoptic segmentation.
L125: The open-vocab segmentation model is the EVF-SAM [cite81†55 ] model from RoboEngine [cite43†53 ]. The video segmentation is done by SAM2 [cite79†36 ].
L126: Training Details. We train our video diffusion models on Bridge V1 [cite48†14 ] and V2 [cite57†45 ] for the following downstream VLA tasks, which provide one to three third-person views. Further, we train Droid [cite47†24 ] for the visual quality comparisons and real-robot augmentation, which includes a wrist-mounted camera and two third-person views.
L127: To support variable-length sequences, we adopt a batch size of 1 per GPU and use gradient accumulation to achieve an effective batch size of 4 per GPU, which costs around 70GB per GPU in training. This strategy enables dynamic frame sampling without incurring unnecessary computation from padding or attention mask overhead. Since current VLA models cannot condition on long observation histories, we train on at most 49 frames.
L128: We train for 15K iterations on 8 GPUs whose per-GPU memory is 144GB, resulting in a total cumulative batch size of 32. Each view is trained at 256×256 resolution for Bridge and 320×416 for Droid. When an instance contains only a single view, the conditioning input for the missing view is zero-padded with black pixels to distinguish 255-value white pixels of the segmentation masks.
L129: In practice, we observe that generative quality correlates with the model’s pretrained resolution; therefore, the cumulative stitched width and height for multi-view must be lower than the pretrained setting. Guided by this finding, we employ the Wan2.1-I2V [cite59†46 ] 720p variant to support diverse generation settings, rather than the lower-resolution 480p model. We set the LoRA [cite82†19 ] rank to 128 and 256 for the Bridge and Droid configurations, respectively.
L130: To maximize data utilization, we randomly sample two views from the three available in Bridge V2. For Droid, we fix the wrist-mounted camera as the first view and select the second view from the two third-person perspectives.
L131: Table 1: Comparison of evaluation results on the WidowX robot in SimplerEnv. We evaluate two variants of our RoboVIP: a text-prompt–conditioned multi-view inpainting video diffusion model, and another version with additional visual identity prompting conditions (denoted as ID). Each task is performed on 100 trials. Each entry shows Grasp/Put, where Put is the conditional success rate given a successful Grasp ($\text{Put}=\text{Success}/\text{Grasp}$), and the Success column reports overall task success.
L132: Bold and underlined numbers in the Average Success column indicate the best and second-best performance.
L133: Model  | Put spoon on towel  | Put carrot on plate  | Stack green cube on yellow cube  | Put eggplant in basket  | Average
L134: --- | --- | --- | --- | --- | ---
L135: Grasp/Put  | Success  | Grasp/Put  | Success  | Grasp/Put  | Success  | Grasp/Put  | Success  | Grasp/Put  | Success
L136: --- | --- | --- | --- | --- | --- | --- | --- | --- | ---
L137: Octo [cite36†42 ] (Zero-Shot)  | 34% / 26%  | 9%  | 35% / 20%  | 7%  | 28% / 0%  | 0%  | 65% / 51%  | 33%  | 40.5% / 30.1%  | 12.2%
L138: Octo (Bridge V2 SFT)  | 52% / 41%  | 29%  | 32% / 37%  | 14%  | 47% / 4%  | 3%  | 60% / 11%  | 5%  | 47.5% / 23.0%  | 12.8%
L139: Octo+RoboEngine [cite43†53 ]  | 67% / 21%  | 14%  | 43% / 37%  | 16%  | 43% / 5%  | 2%  | 0% / 0%  | 0%  | 38.2% / 20.9%  | 8.0%
L140: Octo+RoboVIP (Text prompt)  | 59% / 7%  | 4%  | 69% / 46%  | 32%  | 55% / 9%  | 5%  | 63% / 17%  | 11%  | 61.5% / 21.1%  | 13.0%
L141: Octo+RoboVIP (Text prompt with ID)  | 59% / 63%  | 37%  | 37% / 62%  | 23%  | 47% / 15%  | 7%  | 37% / 19%  | 7%  | 45.0% / 41.1%  | 18.5%
L142: $\pi_{0}$ [cite37†7 ] (Zero-Shot)  | 52% / 63%  | 33%  | 0% / 0%  | 0%  | 28% / 7%  | 2%  | 31% / 42%  | 13%  | 27.75% / 43.2%  | 12%
L143: $\pi_{0}$ (Bridge V2 SFT)  | 57% / 63%  | 36%  | 44% / 43%  | 19%  | 30% / 7%  | 2%  | 29% / 41%  | 12%  | 40% / 43.1%  | 17.25%
L144: $\pi_{0}$+RoboEngine [cite43†53 ]  | 61% / 70%  | 43%  | 33% / 30%  | 10%  | 61% / 11%  | 7%  | 31% / 45%  | 14%  | 46.5% / 39.8%  | 18.5%
L145: $\pi_{0}$+RoboVIP (Text prompt)  | 74% / 84%  | 62%  | 52% / 40%  | 21%  | 49% / 14%  | 7%  | 36% / 64%  | 23%  | 52.75% / 55.0%  | 29%
L146: $\pi_{0}$+RoboVIP (Text prompt with ID)  | 73% / 64%  | 47%  | 49% / 41%  | 20%  | 52% / 13%  | 7%  | 53% / 70%  | 37%  | 56.75% / 48.9%  | 27.75%
L147: ### 4.2 Video Generation Results
L148: Table 2: Generative Model Comparisons on 300 test cases of Droid [cite47†24 ]. Cosmos refers to Cosmos-Transfer2.5 [cite53†3 ]. The best is highlighted.
L149: Method  | FID$\downarrow$  | FVD$\downarrow$  | LPIPS$\downarrow$  | MV-Mat.$\uparrow$
L150: --- | --- | --- | --- | ---
L151: Cosmos [cite53†3 ]  | 47.43  | 325.4  | 0.353  | 1583.4
L152: RoboEngine [cite43†53 ]  | 62.77  | 1788.8  | 0.598  | 1301.9
L153: RoboVIP (Ours)  | 39.97  | 138.4  | 0.409  | 2242.1
L154: cite93†Image: Refer to caption Figure 6: Augmented BridgeV2 Data by our RoboVIP for VLA Training. Our visual identity prompting enriches tabletop contents and introduces additional distractors to create more challenging settings for the policy model. The visual identity is randomly selected from our proposed pools. Zoom in for the best view.
L155: Our goal is to develop a scalable, plug-and-play multi-view inpainting-based generative framework that serves as an effective augmentation solution for robotic manipulation. To this end, we evaluate against Cosmos-Transfer2.5 [cite53†3 ], a video diffusion model designed for real-to-real generation, and RoboEngine [cite43†53 ], an inpainting-based approach similar to ours, on the held-out test subset of the Droid [cite47†24 ] dataset consisting of 300 test cases.
L156: We consider both a wrist-mounted view and a third-person view for augmentation. For RoboEngine, we use identical robot and object segmentation masks as our method for a fair comparison. For Cosmos-Transfer2.5, we evaluate its edge-conditioned variant, using its native 720p setup, and the model is conditioned on the same Qwen2.5-VL [cite50†6 ] captioned text prompts like ours. For our RoboVIP, we apply visual identity prompting.
L157: For all methods, we generate at most 49 frames per episode, starting from the first frame.
L158: We report standard generative video metrics: Fréchet Inception Distance [cite94†17 ] (FID), Fréchet Video Distance [cite95†44 ] (FVD), and Learned Perceptual Image Patch Similarity [cite96†54 ] (LPIPS). FID measures single-frame visual quality via distributional differences, while FVD captures temporal coherence and video-level dynamics. LPIPS quantifies image-level perceptual similarity between generated outputs and ground truth in deep feature space rather than pixel space.
L159: These metrics measure on vertically stitched inputs due to the multi-view setting. To reflect the multi-view nature of our setting, we follow prior works [cite72†33 , cite97†5 ] and evaluate cross-view correspondence by counting matched feature points between two generated views (MV-Mat.). A higher count indicates better spatial consistency and generative stability. We use GIM [cite98†38 ] as the correspondence model, keeping all confidence thresholds and hyperparameters identical to its demo configuration.
L160: As shown in Tab. cite99†2 , our method consistently outperforms prior approaches on most quantitative metrics. The improvement can be attributed to the fact that RoboEngine operates under a single-frame, single-view setting, while Cosmos-Transfer2.5 overlooks the requirements of multi-view generation. In supplementary, we will also include a human study for the visual identity prompting-oriented comparisons.
L161: As shown in Fig. cite100†5 , compared to RoboEngine, our RoboVIP performs distinguished temporal consistency. Compared to Cosmos-Transfer2.5, ours unleashes diverse scene generation, which is not limited by the pixel-aligned conditions, like edges or depth. This is thanks to our inpainting design choices. Further, none of the methods achieve multi-view consistent generation.
--------------------------------------------------------------------------------
GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization (https://arxiv.org/html/2601.05242v1)
citeturn26829view1 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.05242v1","lineno":370}); Total lines: 510
L355:   * [27] Chaoqun He, Renjie Luo, Yuzhuo Bai, Shengding Hu, Zhen Leng Thai, Junhao Shen, Jinyi Hu, Xu Han, Yujie Huang, Yuxiang Zhang, et al. Olympiadbench: A challenging benchmark for promoting agi with olympiad-level bilingual multimodal scientific problems. arXiv preprint arXiv:2402.14008, 2024.
L356:   * [28] Ganqu Cui, Lifan Yuan, Zefan Wang, Hanbin Wang, Yuchen Zhang, Jiacheng Chen, Wendi Li, Bingxiang He, Yuchen Fan, Tianyu Yu, et al. Process reinforcement through implicit rewards. arXiv preprint arXiv:2502.01456, 2025.
L357:   * [29] Dan Hendrycks, Steven Basart, Saurav Kadavath, Mantas Mazeika, Akul Arora, Ethan Guo, Collin Burns, Samir Puranik, Horace He, Dawn Song, et al. Measuring coding challenge competence with apps. arXiv preprint arXiv:2105.09938, 2021.
L358:   * [30] Yujia Li, David Choi, Junyoung Chung, Nate Kushman, Julian Schrittwieser, Rémi Leblond, Tom Eccles, James Keeling, Felix Gimeno, Agustin Dal Lago, et al. Competition-level code generation with alphacode. Science, 378(6624):1092–1097, 2022.
L359:   * [31] Rongao Li, Jie Fu, Bo-Wen Zhang, Tao Huang, Zhihong Sun, Chen Lyu, Guang Liu, Zhi Jin, and Ge Li. Taco: Topics in algorithmic code generation dataset. arXiv preprint arXiv:2312.14852, 2023.
L360:   * [32] Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Jun-Mei Song, Mingchuan Zhang, Y. K. Li, Yu Wu, and Daya Guo. Deepseekmath: Pushing the limits of mathematical reasoning in open language models. ArXiv, abs/2402.03300, 2024.
L361:   * [33] Chujie Zheng, Shixuan Liu, Mingze Li, Xiong-Hui Chen, Bowen Yu, Chang Gao, Kai Dang, Yuqiong Liu, Rui Men, An Yang, Jingren Zhou, and Junyang Lin. Group sequence policy optimization. ArXiv, abs/2507.18071, 2025.
L362:   * [34] Qiying Yu, Zheng Zhang, Ruofei Zhu, Yufeng Yuan, Xiaochen Zuo, Yu Yue, Tiantian Fan, Gaohong Liu, Lingjun Liu, Xin Liu, Haibin Lin, Zhiqi Lin, Bole Ma, Guangming Sheng, Yuxuan Tong, Chi Zhang, Mofan Zhang, Wang Zhang, Hang Zhu, Jinhua Zhu, Jiaze Chen, Jiangjie Chen, Chengyi Wang, Honglin Yu, Weinan Dai, Yuxuan Song, Xiang Wei, Haodong Zhou, Jingjing Liu, Wei Ma, Ya-Qin Zhang, Lin Yan, Mu Qiao, Yong-Xu Wu, and Mingxuan Wang. Dapo: An open-source llm reinforcement learning system at scale.
L363: ArXiv, abs/2503.14476, 2025.
L364:   * [35] Vaishnavi Shrivastava, Ahmed Awadallah, Vidhisha Balachandran, Shivam Garg, Harkirat Singh Behl, and Dimitris Papailiopoulos. Sample more to think less: Group filtered policy optimization for concise reasoning. ArXiv, abs/2508.09726, 2025.
L365:   * [36] Shih-Yang Liu, Xin Dong, Ximing Lu, Shizhe Diao, Mingjie Liu, Min-Hung Chen, Hongxu Yin, Yu-Chiang Frank Wang, Kwang-Ting Cheng, Yejin Choi, Jan Kautz, and Pavlo Molchanov. Dler: Doing length penalty right - incentivizing more intelligence per token via reinforcement learning. ArXiv, abs/2510.15110, 2025.
L366:   * [37] Josef Dai, Xuehai Pan, Ruiyang Sun, Jiaming Ji, Xinbo Xu, Mickel Liu, Yizhou Wang, and Yaodong Yang. Safe rlhf: Safe reinforcement learning from human feedback. ArXiv, abs/2310.12773, 2023.
L367:   * [38] Joel Jang, Seungone Kim, Bill Yuchen Lin, Yizhong Wang, Jack Hessel, Luke S. Zettlemoyer, Hannaneh Hajishirzi, Yejin Choi, and Prithviraj Ammanabrolu. Personalized soups: Personalized large language model alignment via post-hoc parameter merging. ArXiv, abs/2310.11564, 2023.
L368:   * [39] Yuhang Lai, Siyuan Wang, Shujun Liu, Xuanjing Huang, and Zhongyu Wei. Alarm: Align language models via hierarchical rewards modeling. In Annual Meeting of the Association for Computational Linguistics, 2024.
L369:   * [40] DeepSeek-AI, Aixin Liu, Aoxue Mei, Bangcai Lin, Bing Xue, Bing-Li Wang, Bingzheng Xu, Bochao Wu, Bowei Zhang, Chaofan Lin, Chen Dong, Chengda Lu, Chenggang Zhao, Chengqi Deng, Chenhao Xu, Chong Ruan, Damai Dai, Daya Guo, Dejian Yang, Deli Chen, Erhang Li, Fangqi Zhou, Fangyun Lin, Fucong Dai, Guangbo Hao, Guanting Chen, Guowei Li, H.
L370: Zhang, Hanwei Xu, Hao Li, Haofen Liang, Haoran Wei, Haowei Zhang, Hao sheng Luo, Haozhe Ji, Honghui Ding, Hongxuan Tang, Huanqi Cao, Huazuo Gao, Huixian Qu, Hui Zeng, Jialiang Huang, Jiashi Li, Jiaxin Xu, Jiewen Hu, JingChang Chen, Jingting Xiang, Jingyang Yuan, Jing Cheng, Jinhua Zhu, Jun Ran, Junguang Jiang, Junjie Qiu, Junlong Li, Jun-Mei Song, Kai Dong, Kaige Gao, Kang Guan, Kexin Huang, Kexing Zhou, Kezhao Huang, Kuai Yu, Lean Wang, Lecong Zhang, Lei Wang, Liang Zhao, Liangsheng Yin, Lihua Guo, Ling-Li Luo, Linwang Ma, Litong Wang, Liyue Zhang, M.
L371: S. Di, M. Y. Xu, Mingchuan Zhang, Minghua Zhang, Min Tang, Mingxu Zhou, P. Huang, Peixin Cong, Peiyi Wang, Qiancheng Wang, Qihao Zhu, Qingyang Li, Qinyu Chen, Qiushi Du, Ruiling Xu, Ruiqi Ge, Ruisong Zhang, Ruizhe Pan, Runji Wang, Runqiu Yin, Runxin Xu, Ruomeng Shen, Ruoyu Zhang, S. H.
L372: Liu, Shanghao Lu, Shangyan Zhou, Shanhuang Chen, Shaofei Cai, Shaoyuan Chen, Shengding Hu, Shengyu Liu, Shiqiang Hu, Shirong Ma, Shiyu Wang, Shuiping Yu, Shunfeng Zhou, Shuting Pan, Songyang Zhou, Tao Ni, Tao Yun, Tian Pei, Tian Ye, Tianyuan Yue, Wangding Zeng, Wen Liu, Wenfeng Liang, Wenjie Pang, Wenjing Luo, Wenjun Gao, Wentao Zhang, Xi Gao, Xiangwen Wang, Xiaoling Bi, Xiaodong Liu, Xiaohan Wang, Xiaokang Chen, Xiaokang Zhang, Xiaotao Nie, Xin Cheng, Xin Liu, Xin Xie, Xingchao Liu, Xingkai Yu, Xingyou Li, Xinyu Yang, Xinyuan Li, Xu Chen, Xuecheng Su, Xuehai Pan, Xuheng Lin, Xuwei Fu, Y.
L373: Q. Wang, Yang Zhang, Yanhong Xu, Yanru Ma, Yao Li, Yao Zhao, Yaofeng Sun, Yaohui Wang, Yi Qian, Yingpu Yu, Yichao Zhang, Yifan Ding, Yifan Shi, Yi Xiong, Ying He, Ying Zhou, Yinmin Zhong, Yishi Piao, Yisong Wang, Yixiao Chen, Yixuan Tan, Yixuan Wei, Yiyang Ma, Yiyuan Liu, Yonglun Yang, Yongqiang Guo, Yongtong Wu, Yu Wu, Yuan Cheng, Yuan Ou, Yuanfan Xu, Yuduan Wang, Yue Gong, Yuhan Wu, Yuheng Zou, Yukun Li, Yunfan Xiong, Yu-Wei Luo, Yu mei You, Yuxuan Liu, Yuyang Zhou, Z. F. Wu, Z. Z.
L374: Ren, Zehua Zhao, Zehui Ren, Zhangli Sha, Zhe Fu, Zhean Xu, Zhenda Xie, Zhen guo Zhang, Zhewen Hao, Zhibin Gou, Zhicheng Ma, Zhigang Yan, Zhihong Shao, Zhixian Huang, Zhiyu Wu, Zhuoshu Li, Zhuping Zhang, Zian Xu, Zihao Wang, Zihui Gu, Zijia Zhu, Zi-Rui Li, Zipeng Zhang, Ziwei Xie, Ziyi Gao, Zizheng Pan, Zongqing Yao, Bei Feng, Hui Li, J. L. Cai, Jiaqi Ni, Lei Xu, Meng Li, Ning Tian, R. J. Chen, Ruiqi Jin, S. S. Li, Shuang Zhou, Tianyu Sun, X. Q.
L375: Li, Xiangyu Jin, Xiaojin Shen, Xiaosha Chen, Xinnan Song, Xinyi Zhou, Y. X. Zhu, Yanping Huang, Yao Li, Yi Zheng, Yuchen Zhu, Yunxiang Ma, Zhen Huang, Zhipeng Xu, Zhongyu Zhang, Dong-Li Ji, Jian Liang, Jianzhong Guo, Jin Chen, Leyi Xia, Miaojun Wang, Mingming Li, Peng Zhang, Ruyi Chen, Shangmian Sun, Shao-Kang Wu, Shengfeng Ye, T.Wang, W. L. Xiao, Wei An, Xianzu Wang, Xiaowen Sun, Xiaoxiang Wang, Ying Tang, Yukun Zha, Ze-Na Zhang, Zhenghua Ju, Zhen Zhang, and Zihua Qu.
L376: Deepseek-v3.2: Pushing the frontier of open large language models. 2025.
L377:   * [41] Haotian Luo, Li Shen, Haiying He, Yibo Wang, Shiwei Liu, Wei Li, Naiqiang Tan, Xiaochun Cao, and Dacheng Tao. O1-pruner: Length-harmonizing fine-tuning for o1-like reasoning pruning. ArXiv, abs/2501.12570, 2025.
L378:   * [42] Daman Arora and Andrea Zanette. Training language models to reason efficiently. ArXiv, abs/2502.04463, 2025.
L379:   * [43] Jingyang Yi and Jiazheng Wang. Shorterbetter: Guiding reasoning models to find optimal inference length for efficient reasoning. ArXiv, abs/2504.21370, 2025.
L380:   * [44] Pranjal Aggarwal and Sean Welleck. L1: Controlling how long a reasoning model thinks with reinforcement learning. ArXiv, abs/2503.04697, 2025.
L381:   * [45] Jinyan Su and Claire Cardie. Thinking fast and right: Balancing accuracy and reasoning length with adaptive rewards. ArXiv, abs/2505.18298, 2025.
L382: ## Appendix A Training stability issue of GDPO without batch-wise advantage normalization
L383: 
L384: Figure 8: Training stability of GDPO with and without batch-wise advantage normalization. Runs without normalization occasionally fail to converge.
L385: 
L386: ## Appendix B ToolRL Training Prompt Format
L387: 
L388: ## Appendix C Tool Calling Reward Functions
L389: ##### Format Reward.
L390: 
L391: The format reward $\mathcal{R}_{\text{format}}\in\{0,1\}$ checks whether the model output satisfies the required structure and contains all necessary fields in the correct order:
L392: 
L393:  | $$\mathcal{R}_{\text{format}}=\begin{cases}1,&\text{if all required fields appear and are in the correct order},\\
L394: 0,&\text{otherwise}.\end{cases}$$  |  | (9)
L395: ##### Correctness Reward.
L396: 
L397: The correctness reward $\mathcal{R}_{\text{correct}}\in[-3,\,3]$ evaluates the predicted tool calls $P=\{P_{1},\ldots,P_{m}\}$ against the ground-truth calls $G=\{G_{1},\ldots,G_{n}\}$. It consists of three components:
L398: 
L399:   * •
L400: 
L401: Tool Name Matching:
L402: 
L403:  | $$r_{\text{name}}=\frac{|N_{G}\cap N_{P}|}{|N_{G}\cup N_{P}|}\in[0,1],$$  |
L404: 
L405: where $N_{G}$ and $N_{P}$ are the sets of tool names from ground-truth and predicted calls, respectively.
L406: 
L407:   * •
L408: 
L409: Parameter Name Matching:
L410:  | $$r_{\text{param}}=\sum_{G_{j}\in G}\frac{|\mathrm{keys}(G_{j})\cap\mathrm{keys}(P_{j})|}{|\mathrm{keys}(G_{j})\cup\mathrm{keys}(P_{j})|}\in[0,|G|],$$  |
L411: 
L412: where $\mathrm{keys}(G_{j})$ and $\mathrm{keys}(P_{j})$ are the parameter names of the ground-truth and predicted calls.
L413: 
L414:   * •
L415: 
L416: Parameter Content Matching:
L417: 
L418:  | $$r_{\text{value}}=\sum_{G_{j}\in G}\sum_{k\in\mathrm{keys}(G_{j})}\mathbf{1}[P_{G}[k]=P_{P}[k]]\in\left[0,\;\sum_{G_{j}\in G}|\mathrm{keys}(G_{j})|\right],$$  |
L419: where $P_{G}[k]$ and $P_{P}[k]$ are the parameter values for the ground-truth and predicted calls.
L420: 
L421:   * •
L422: 
L423: Total Match Score:
L424: 
L425:  | $$r_{\text{match}}=r_{\text{name}}+r_{\text{param}}+r_{\text{value}}\in[0,S_{\max}],$$  |
L426: 
L427: where
L428: 
L429:  | $$S_{\max}=1+|G|+\sum_{G_{j}\in G}|\mathrm{keys}(G_{j})|.$$  |
L430: 
L431: The final correctness reward is computed by finding the optimal matching between $P$ and $G$ to maximize the total match score:
L432:  | $$\mathcal{R}_{\text{correct}}=6\cdot\frac{R_{\max}}{S_{\max}}-3\in[-3,\,3].$$  |
L433: 
L434: where $R_{\max}$ denotes the total match score from the optimal matching.
L435: ## Appendix D ToolRL Hyperparameters Setting
L436: 
L437: Table 6: GDPO verl training configuration. All hyperparameter settings are kept identical to those used in ToolRL[cite52†12 ].
L438: Parameter  | Value
L439: --- | ---
L440: trainer.total_epochs  | 15
L441: data.train_batch_size  | 512
L442: actor_rollout_ref.actor.ppo_mini_batch_size  | 128
L443: data.max_prompt_length  | 2048
L444: actor_rollout_ref.actor.optim.lr  | 1.00E-06
L445: actor_rollout_ref.rollout.n  | 4
L446: algorithm.kl_ctrl.kl_coef  | 0.001
L447: ## Appendix E Math/Coding Reasoning Hyperparameters Setting
L448: Table 7: GDPO verl training configuration
L449: Parameter  | Value
L450: --- | ---
L451: data.train_batch_size  | 512
L452: actor_rollout_ref.actor.ppo_mini_batch_size  | 64
L453: actor_rollout_ref.actor.ppo_epochs  | 1
L454: data.max_prompt_length  | 1024
L455: actor_rollout_ref.actor.optim.lr  | 1.00E-06
L456: actor_rollout_ref.rollout.temperature  | 1
L457: actor_rollout_ref.rollout.n  | 16
L458: actor_rollout_ref.actor.clip_ratio_low  | 0.2
L459: actor_rollout_ref.actor.clip_ratio_high  | 0.28
L460: algorithm.filter_groups.enable  | TRUE
L461: algorithm.filter_groups.metric  | seq_reward
L462: actor_rollout_ref.actor.kl_loss_coef  | 0.0005
L463: actor_rollout_ref.actor.kl_loss_type  | mse
L464: ## Appendix F Training curves of GRPO and GDPO when training DeepSeek-R1-7B and Qwen3-4B-Instruct with $\mathcal{R}_{\text{length}}$ and $\mathcal{R}_{\text{correct}}$ on math reasoning data.
L465: Figure 9: Training behavior of GRPO and GDPO when optimizing DeepSeek-R1-7B across correctness reward, length reward, and maximum batch response length on math reasoning data. We can see that GDPO maintains improving correctness and better adherence to length constraints over GRPO. Figure 10: Training behavior of GRPO and GDPO when optimizing Qwen3-4B-Instruct across correctness reward, length reward, and maximum batch response length on math reasoning data.
L466: We can see that GDPO maintains improving correctness and better adherence to length constraints over GRPO.
L467: ## Appendix G Comparison of GRPO/GDPO finetuned DeepSeek-R1-7B models under varying length reward weights $\{1.0,0.75,0.5,0.25\}$ with and without the conditioned length reward $\tilde{\mathcal{R}}_{\text{length}}$ on math reasoning tasks
L468: 
L469: Table 8: Comparison of GRPO/GDPO finetuned DeepSeek-R1-7B models under varying length reward weights $\{1.0,0.75,0.5,0.25\}$ with the normal length reward $\mathcal{R}_{\text{length}}$ on math reasoning tasks

