[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] p: 1]University of Trento, Trento, Italy 2]Sun Yat-sen University, Guangzhou, China

[3] p: Feng Xue at \contribution \contribution \contribution \contribution \contribution \contribution \contribution

[4] h1: Risk-Aware World Model Predictive Control for Generalizable End-to-End Autonomous Driving

[5] h6: Abstract

[6] p: With advances in imitation learning (IL) and large-scale driving datasets, end-to-end autonomous driving (E2E-AD) has made great progress recently. Currently, IL-based methods have become a mainstream paradigm: models rely on standard driving behaviors given by experts, and learn to minimize the discrepancy between their actions and expert actions. However, this objective of “only driving like the expert” suffers from limited generalization: when encountering rare or unseen long-tail scenarios outside the distribution of expert demonstrations, models tend to produce unsafe decisions in the absence of prior experience. This raises a fundamental question: Can an E2E-AD system make reliable decisions without any expert action supervision? Motivated by this, we propose a unified framework named Risk-aware World Model Predictive Control (RaWMPC) to address this generalization dilemma through robust control, without reliance on expert demonstrations. Practically, RaWMPC leverages a world model to predict the consequences of multiple candidate actions and selects low-risk actions through explicit risk evaluation. To endow the world model with the ability to predict the outcomes of risky driving behaviors, we design a risk-aware interaction strategy that systematically exposes the world model to hazardous behaviors, making catastrophic outcomes predictable and thus avoidable. Furthermore, to generate low-risk candidate actions at test time, we introduce a self-evaluation distillation method to distill risk-avoidance capabilities from the well-trained world model into a generative action proposal network without any expert demonstration. Extensive experiments show that RaWMPC outperforms state-of-the-art methods in both in-distribution and out-of-distribution scenarios, while providing superior decision interpretability.

[7] figure: Figure 1 : Comparison between existing E2E-AD methods and RaWMPC . The first row shows the predicted trajectories, and the second row compares the core workflows. Black arrows denote test-time execution, while pink arrows indicate training-only steps. The comparison shows that prior methods often omit explicit hazard modeling and may trigger traffic violations, whereas RaWMPC uses a risk-aware world model to evaluate action consequences and select safe, compliant actions in critical scenes.

[8] h2: 1 Introduction

[9] p: End-to-end autonomous driving (E2E-AD) [ 64 , 63 , 81 , 26 , 56 ] aims to map sensor observations to control actions, e.g. , steering, throttle, and brake, without relying on hand-crafted perception, prediction, or planning modules. Compared to traditional modular pipelines [ 74 , 48 , 76 , 101 , 53 , 51 ] , E2E-AD offers a more unified representation of the driving task, enabling the policy to reason about complex interactions between the ego vehicle and dynamic environments. As such, E2E-AD has attracted growing attention due to its potential for simplified system design, joint optimization, and real-time decision-making.

[10] p: Early studies on E2E-AD [ 75 , 5 , 4 ] primarily focused on learning driving policies via reinforcement learning (RL) through online exploration. More recent research [ 95 , 6 ] demonstrated that rule-based or RL-based agents leveraging privileged information ( e.g. , bird’s-eye-view segmentation and high-definition maps) can produce superior driving decisions. Building upon these insights, state-of-the-art methods [ 64 , 63 , 81 , 28 , 90 ] generally follow an imitation learning (IL) framework as shown in Fig. 1 , where agents using only sensor inputs ( e.g. , RGB images and LiDAR) are trained to replicate the privileged experts’ behavior through knowledge distillation on both the driving policy and latent features. Although some works have attempted to enhance the driving performance via future motion modeling [ 64 , 63 , 57 , 73 ] , action-aware future prediction [ 23 , 28 , 38 , 39 ] , and the integration of large language models [ 21 , 35 , 14 , 55 ] , these approaches still adhere to the learning objective of “ driving like an expert ”, as demonstrated in Fig. 1 (a). They cannot fundamentally resolve the inherent generalization dilemma of imitation learning: Since expert demonstrations cannot cover all scenarios and situations, imitation-based policies tend to produce unpredictable and often unsafe driving behavior when encountering unseen scenarios outside of expert demonstrations. More recently, model-based RL methods [ 37 , 85 ] have emerged and attempted to improve generalization by learning environmental dynamics and planning over them. However, as illustrated in Fig. 1 (b), most of them still aim to maximize the expected reward and lack explicit modeling and sampling of rare but high-risk situations, and thus continue to struggle to guarantee safety in these scenarios.

[11] p: In this paper, we argue that “enabling an E2E-AD system to learn and proactively avoid risky actions is more important than replicating expert driving behavior verbatim” . Motivated by this perspective, we propose an E2E-AD framework that does not require any expert action supervision, called Risk-aware World Model Predictive Control (RaWMPC), as shown in Fig. 1 (c). This framework discards expert demonstrations and instead leverages a risk-aware world model to drive predictive control to overcome the generalization challenge. Different from model-based RL that trains an actor to maximize reward from imagined rollouts of a world model, the world model in RaWMPC predicts near-future states for a set of “candidate” driving behaviors and explicitly evaluates their risk, so as to select the lowest-risk candidate. To endow our world model with risk-awareness, we introduce a risk-aware interaction strategy: Starting from scratch, the model selects self-identified high-risk actions to interact with the environment, from which our world model learns to predict the consequences of diverse risky behaviors. Without any expert demonstration, our world model can reach strong performance from scratch, and can be further accelerated if a few video clips are provided by benchmarks for a light warm-up. Finally, to efficiently provide low-risk candidates at test time, we further propose a self-evaluation distillation for driving policy learning. The well-trained world model is leveraged to identify safe and risky behaviors from the sampled action space, and to distill this knowledge, via safety–risk contrastive learning, into a generative action proposal network. Experiments on Bench2Drive and NAVSIM show that RaWMPC, even without expert demonstrations, surpasses previous state-of-the-art methods, while the optional light warm-up further helps to accelerate the convergence and improve performance. More importantly, since RaWMPC learns risk-awareness from interaction rather than expert labels, it achieves substantially higher driving performance in previously unseen scenarios. Our main contributions can be summarized as follows:

[12] p: We propose RaWMPC , an E2E-AD framework with zero expert requirement. Unlike IL and MBRL methods, RaWMPC uses a world model to select low-risk behaviors from multiple candidate actions, which naturally improves the interpretability and reliability of its decisions.

[13] p: Within RaWMPC, we design a risk-aware interaction learning strategy that enables the world model to acquire risk-awareness purely from environment interaction, without any expert demonstration.

[14] p: We introduce a self-evaluation distillation scheme for driving policy learning, which provides high-quality candidate actions at test time, even outperforming policies learned directly from expert demonstrations.

[15] h2: 2 Related Work

[16] h3: 2.1 End-to-End Learning in Autonomous Driving

[17] p: Learning-based autonomous driving approaches typically follow two main paradigms: imitation learning (IL) and reinforcement learning (RL) [ 7 , 9 ] . Early studies explored RL extensively [ 75 , 5 , 4 , 59 , 93 , 32 , 52 , 2 , 22 , 58 ] for its natural capability to refine driving strategies through interactive feedback. Subsequent works [ 95 , 37 ] demonstrated that training sensor-based agents to imitate RL experts’ behavior could lead to superior performance, prompting a shift toward leveraging privileged information (e.g., BEV segmentation and HD maps) to train stronger RL experts. More recently, model-based RL has revisited this line by learning explicit dynamics/world models and performing look-ahead rollouts [ 85 ] , improving consequence-aware evaluation and sample efficiency. Nevertheless, these RL approaches are commonly driven by maximizing expected return, and they rarely provide an explicit mechanism to systematically discover and model rare-but-catastrophic outcomes, making reliable decisions in long-tail, high-risk scenarios still challenging.

[18] p: With large-scale driving datasets, imitation learning has attracted increased attention and achieved state-of-the-art performance in closed-loop autonomous driving [ 55 , 82 , 73 , 40 ] . Most IL approaches rely on collecting trajectory data and features from RL-based [ 95 , 37 ] or rule-based [ 10 , 65 ] experts using privileged information, and train sensor-based IL agents to replicate expert behaviors through knowledge distillation. A variety of research studies have explored ways to improve IL performance, such as multi-modal information fusion [ 10 , 26 , 54 ] , object motion modeling [ 64 , 57 , 63 , 30 ] , action-aware future prediction [ 23 , 28 , 38 , 39 ] , feature alignment [ 27 , 90 ] , and the integration of large language models [ 65 , 62 , 83 , 86 , 56 , 45 , 55 , 14 ] . Despite impressive results, the core objective of “driving like the expert” inherently limits generalization: expert demonstrations cannot cover all long-tail situations, and experts typically avoid dangerous behaviors, leaving IL agents with limited supervision on how to recognize and proactively avoid high-risk actions. Moreover, pure imitation often provides limited interpretability because it outputs a single action without explicitly comparing alternative actions via consequence evaluation. Motivated by these insights, we propose RaWMPC, a unified framework that replaces expert action supervision with risk-aware predictive control: it learns a risk-aware world model via a risk-aware interaction strategy that deliberately exposes the model to risky behaviors, and uses the learned model to predict and evaluate the consequences of multiple candidate actions, selecting low-risk behaviors with explicit risk evaluation.

[19] h3: 2.2 World Models

[20] p: World models approximate environment transitions under the Markov Decision Process and have demonstrated success in RL [ 18 , 20 , 34 , 46 , 77 , 79 , 17 , 19 , 75 ] by predicting future states and rewards from current observations and actions. However, applying these models to complex tasks such as autonomous driving remains challenging. Previous research [ 24 , 15 , 78 , 92 , 70 , 72 , 13 , 71 , 36 , 1 , 98 , 96 , 97 , 49 , 50 , 102 ] has mainly leveraged world models to generate controllable future driving trajectories (e.g., RGB images and 3D/4D representations) conditioned on specific actions and scene descriptions. Such predictive models can enlarge training data and increase diversity, potentially benefiting downstream imitation learning, especially for rare scenes such as traffic accidents.

[21] p: Beyond prediction, a few recent attempts have utilized world models to improve closed-loop autonomous driving performance. In particular, some works have started to connect world modeling with planning and online evaluation in driving settings [ 8 , 91 , 39 ] , while others provide high-fidelity generative platforms that enable closed-loop evaluation [ 11 , 84 , 3 ] . In particular, model-based IL methods [ 23 , 38 , 39 , 61 ] employ world models to support better imitation: LAW [ 38 ] enhances end-to-end driving by predicting future information in a latent world model to assist policy learning, and WoTE [ 39 ] performs online trajectory evaluation via a BEV world model to score candidate trajectories. More recently, model-based RL methods have drawn increasing attention. Think2Drive [ 37 ] designed a model-based RL expert to forecast action-conditioned future rewards for training a more effective critic network, and Raw2Drive [ 85 ] leveraged a world model pretrained from privileged experts to guide the learning of sensor agents. Despite these advances, most existing works still inherit supervision from experts or rewards, and they largely focus on imitation fidelity or expected-return maximization, lacking explicit mechanisms to systematically discover, model, and avoid rare-but-high-risk outcomes. In contrast, RaWMPC uses the world model as a risk evaluator within predictive control: we introduce a risk-aware interaction strategy to intentionally explore risky behaviors so that catastrophic consequences become predictable and avoidable, and we select actions by explicitly minimizing risk over multiple candidates, enhancing the interpretability, reliability, and generalization of the decision-making process.

[22] figure: Figure 2 : Overview of RaWMPC. Multi-view images 𝐈 t \mathbf{I}_{t} , ego state 𝐌 t \mathbf{M}_{t} , and candidate action sequences { 𝐀 t : t + H − 1 n } n = 1 N \{\mathbf{A}^{n}_{t:t+H-1}\}_{n=1}^{N} are encoded and rolled out by a world model over horizon H H . Three decoders predict semantic segmentation, semantic-guided traffic events, and future ego states, enabling action evaluation for predictive control. Training combines offline warm-up on logged trajectories with online simulator interaction using world-model-guided exploration.

[23] h2: 3 Method

[24] p: To demonstrate our solution, Sec. 3.1 introduces the overall network structure and pipeline of our RaWMPC. Sec. 3.2 presents our training scheme, i.e. , risk-aware interactive training, for efficient optimization. To ensure the whole E2E-AD system runs efficiently during testing, Sec. 3.3 illustrates a self-evaluation distillation method to train an action proposal network.

[25] h3: 3.1 Network Structure of RaWMPC

[26] h4: 3.1.1 Problem Setup

[27] p: We consider a closed-loop end-to-end autonomous driving (E2E-AD) setting. At each time step t t , the agent receives three inputs: a visual input 𝐈 t \mathbf{I}_{t} ( multi-view RGB images ), an ego-centric measurement 𝐌 t \mathbf{M}_{t} ( velocity and position ), and a set of candidate driving behaviors { 𝐀 t : t + H − 1 n } n = 1 N \{\mathbf{A}^{n}_{t:t+H-1}\}_{n=1}^{N} , where N N is the number of candidates and H H is the planning horizon. Each step of action consists of three values: 𝐀 = ( steer ∈ [ − 1 , 1 ] , throttle ∈ [ 0 , 1 ] , brake ∈ [ 0 , 1 ] ) \mathbf{A}=(\texttt{steer}\in[-1,1],\texttt{throttle}\in[0,1],\texttt{brake}\in[0,1]) . Based on the driving history ( 𝐈 1 : t , 𝐌 1 : t , 𝐀 1 : t − 1 ) (\mathbf{I}_{1:t},\mathbf{M}_{1:t},\mathbf{A}_{1:t-1}) , RaWMPC aims to select the best one 𝐀 n ⋆ t : t + H − 1 \mathbf{A}^{n^{\star}}_{t:t+H-1} from the candidates, so that the vehicle can move toward a destination while ensuring safety and compliance with traffic rules.

[28] h4: 3.1.2 Overview

[29] p: As illustrated in Fig. 2 , RaWMPC begins from input encoding. A visual encoder, an action encoder and an ego-state encoder are used to map 𝐈 t \mathbf{I}_{t} , { 𝐀 t : t + H − 1 n } n = 1 N \{\mathbf{A}^{n}_{t:t+H-1}\}_{n=1}^{N} , and 𝐌 t \mathbf{M}_{t} into embeddings 𝐢 t \mathbf{i}_{t} , { 𝐚 t : t + H − 1 n } n = 1 N \{\mathbf{a}^{n}_{t:t+H-1}\}_{n=1}^{N} , and 𝐦 t \mathbf{m}_{t} , respectively. Then, based on the observed states 𝐬 1 : t = ( 𝐢 1 : t , 𝐦 1 : t ) \mathbf{s}_{1:t}\!=\!(\mathbf{i}_{1:t},\mathbf{m}_{1:t}\!) , we use a world model to estimate its future state 𝐬 ^ n t + 1 : t + H \hat{\mathbf{s}}^{n}_{t+1:t+H} conditioned on each action embeddings 𝐚 n t : t + H − 1 \mathbf{a}^{n}_{t:t+H-1} . Finally, we select the action that enables the ego vehicle to advance safely while avoiding traffic infractions, by decoding 𝐬 ^ n t + 1 : t + H \hat{\mathbf{s}}^{n}_{t+1:t+H} and computing a cost value:

[30] table: \displaystyle 𝐀 ⋆ t : t + H − 1 = 𝐀 n ⋆ t : t + H − 1 , \displaystyle\mathbf{A}^{\star}_{t:t+H-1}=\mathbf{A}^{n^{\star}}_{t:t+H-1}, (1) where n ⋆ = arg ⁡ min n ∈ { 1 , … , N } C ( 𝐬 ^ n t + 1 : t + H ) . \displaystyle\text{where}\,\,\,n^{\star}=\underset{n\in\{1,\dots,N\}}{\arg\min}C\!\big(\hat{\mathbf{s}}^{n}_{t+1:t+H}\big).

[31] p: where C ⁡ ( ⋅ ) C(\cdot) denotes the cost function in the decoding process (will be detailed in Eq. ( 6 )), and n ⋆ n^{\star} is the index of optimal action. Compared to imitation learning schemes, RaWMPC offers improved interpretability and introduces an explicit mechanism for decision validation and risk mitigation.

[32] h4: 3.1.3 World Model

[33] p: In our pipeline, the world model, denoted as ℳ \mathcal{M} , is employed to predict future states given an action. Specifically, conditioned on the observed states 𝐬 1 : t = ( 𝐢 1 : t , 𝐦 1 : t ) \mathbf{s}_{1:t}\!=\!(\mathbf{i}_{1:t},\mathbf{m}_{1:t}\!) and the potential next action 𝐚 t n \mathbf{a}^{n}_{t} , the world model ℳ \mathcal{M} predicts a near-future state 𝐬 ^ t + 1 n \hat{\mathbf{s}}^{n}_{t+1} . Then, for the further-future time step { 2 , … , H } \{2,\dots,H\} , the world model recursively rolls out, which can be formalized as an autoregressive factorization:

[34] table: p ℳ ( 𝐬 ^ n t + 1 : t + H | 𝐬 1 : t , 𝐚 n 1 : t + H − 1 ) = \displaystyle p_{\mathcal{M}}(\hat{\mathbf{s}}^{n}_{t+1:t+H}|\mathbf{s}_{1:t},\mathbf{a}^{n}_{1:t+H-1})= (2) ∏ k = 1 H p ℳ ( 𝐬 ^ n t + k | ( 𝐬 1 : t , 𝐬 ^ n t + 1 : t + k − 1 ) , 𝐚 n 1 : t + k − 1 ) \displaystyle\prod\nolimits_{k=1}^{H}p_{\mathcal{M}}\Big(\hat{\mathbf{s}}^{n}_{t+k}|(\mathbf{s}_{1:t},\hat{\mathbf{s}}^{n}_{t+1:t+k-1})\,\,,\,\mathbf{a}^{n}_{1:t+k-1}\Big)

[35] p: where p ℳ p_{\mathcal{M}} denotes the conditional distribution defined by the world model ℳ \mathcal{M} . 𝐚 1 : t + k − 1 n = [ 𝐚 1 : t − 1 , 𝐚 t : t + k − 1 n ] \mathbf{a}^{n}_{1:t+k-1}=[\mathbf{a}_{1:t-1},\mathbf{a}^{n}_{t:t+k-1}] denotes a candidate action sequence containing action history.

[36] h4: 3.1.4 Semantic-Guided Decoding

[37] p: Once the world model predicts a sequence of future states, 𝐬 ^ n t + 1 : t + H \hat{\mathbf{s}}^{n}_{t+1:t+H} , three transformer decoders separately map these states to task-specific outputs: semantic segmentation, potential traffic events ( e.g. , collision), and future ego-states ( e.g. , position). In what follows, we describe these decoders using the predicted state at time step t + k t+k , i.e. , 𝐬 ^ t + k n \hat{\mathbf{s}}^{n}_{t+k} , where k ∈ { 1 , … , H } k\in\{1,\dots,H\} .

[38] p: To enable a higher-level understanding of driving scenes and provide visual explanations for predicted traffic events, we inject semantic attention from the segmentation decoder into the event decoder. The segmentation decoder adopts a standard transformer attention:

[39] table: 𝙰𝚝𝚝 𝚜𝚎𝚐 ​ ( 𝐐 c , 𝐊 c , 𝐕 c ) = 𝚜𝚘𝚏𝚝𝚖𝚊𝚡 ⁡ ( 𝚜𝚒𝚖 ⁡ ( 𝐐 c , 𝐊 c ) ) ⋅ 𝐕 c , \!\!\mathtt{Att_{seg}}(\!\mathbf{Q}_{c},\!\mathbf{K}_{c},\!\!\mathbf{V}_{c}\!)\!=\!\mathtt{softmax}(\mathtt{sim}(\mathbf{Q}_{c},\mathbf{K}_{c}))\!\cdot\!\!\mathbf{V}_{c}, (3)

[40] p: where 𝐐 c \mathbf{Q}_{c} are learnable class queries, and 𝐊 c , 𝐕 c \mathbf{K}_{c},\mathbf{V}_{c} are derived from visual tokens 𝐢 ^ t + k n ⊂ 𝐬 ^ t + k n \hat{\mathbf{i}}^{n}_{t+k}\subset\hat{\mathbf{s}}^{n}_{t+k} . In the final layer, we follow SegViT [ 88 ] to predict the one-hot semantic segmentation map 𝐘 ^ t + k n \hat{\mathbf{Y}}^{n}_{t+k} for each input class query. We then augment the event decoder by fusing its attention logits with the corresponding semantic attention logits from the last segmentation layer:

[41] table: 𝐙 e \displaystyle\mathbf{Z}_{e} = 𝐐 e 𝐊 e ⊤ , 𝐙 c = pad ( 𝐐 c 𝐊 c ⊤ ) , \displaystyle=\mathbf{Q}_{e}\mathbf{K}_{e}^{\top},\,\,\,\mathbf{Z}_{c}=\mathrm{pad}(\mathbf{Q}_{c}\mathbf{K}_{c}^{\top}), (4) E ^ t + k n \displaystyle\hat{E}^{n}_{t+k} = sigmoid ⁡ ( softmax ⁡ ( 𝐖 e ∗ [ 𝐙 e , 𝐙 c ] ) ​ 𝐕 e ) . \displaystyle=\mathrm{sigmoid}\!\left(\mathrm{softmax}\!\left(\mathbf{W}_{e}*[\mathbf{Z}_{e},\mathbf{Z}_{c}]\right)\!\mathbf{V}_{e}\right).

[42] p: where 𝐐 e \mathbf{Q}_{e} are learnable event queries, and 𝐊 e , 𝐕 e \mathbf{K}_{e},\mathbf{V}_{e} are computed from predicted future states 𝐬 ^ t + k n \hat{\mathbf{s}}^{n}_{t+k} . 𝚙𝚊𝚍 ⁡ ( ⋅ ) \mathtt{pad}(\cdot) zero-pads 𝐙 c \mathbf{Z}_{c} to match the size of 𝐙 e \mathbf{Z}_{e} , and 𝐖 e \mathbf{W}_{e} is a 1 × 1 1\times 1 convolution that fuses the concatenated logits. The output of the event decoder, E ^ t + k n ∈ [ 0 , 1 ] α \hat{E}^{n}_{t+k}\in[0,1]^{\alpha} , represents the probabilities of α \alpha event types. Finally, for the future ego-state prediction, we decode the ego token 𝐦 ^ t + k n ⊂ 𝐬 ^ t + k n \hat{\mathbf{m}}^{n}_{t+k}\subset\hat{\mathbf{s}}^{n}_{t+k} to obtain the speed and position 𝐌 ^ t + k n \hat{\mathbf{M}}^{n}_{t+k} .

[43] p: Guided by the semantic attention map, the event decoder draws more attention to regions critical to specific events. For instance, when recognizing the vehicle collision event, the model focuses more on vehicle areas, improving the accuracy and reliability of event predictions.

[44] h4: 3.1.5 Action Selection and Predictive Control

[45] p: Given the decoder outputs, we perform predictive control by evaluating each candidate action sequence over the planning horizon H H and selecting the one with the minimum predicted cost.

[46] p: Specifically, for the n n -th candidate 𝐀 n t : t + H − 1 \mathbf{A}^{n}_{t:t+H-1} , we consider (i) progress toward the target and (ii) the risk of traffic-violation events. Let 𝐩 ⋆ \mathbf{p}^{\star} be the target 3D position and 𝐩 ^ t + k n ⊂ 𝐌 ^ t + k n \hat{\mathbf{p}}^{n}_{t+k}\subset\hat{\mathbf{M}}^{n}_{t+k} the predicted ego position at step t + k t+k . We define the progress as the reduction in target distance:

[47] table: D ^ t + k n = ‖ 𝐩 ⋆ − 𝐩 ^ t + k − 1 n ‖ 2 − ‖ 𝐩 ⋆ − 𝐩 ^ t + k n ‖ 2 , \hat{D}^{n}_{t+k}=\big\|\mathbf{p}^{\star}-\hat{\mathbf{p}}^{n}_{{t+k}-1}\big\|_{2}-\big\|\mathbf{p}^{\star}-\hat{\mathbf{p}}^{n}_{{t+k}}\big\|_{2}, (5)

[48] p: We then define the predictive-control objective as:

[49] table: C ( 𝐬 ^ n t + 1 : t + H ) = ∑ k = 1 H η k ( − D ^ n t + k + ∑ j = 1 α λ j E ^ n t + k , j ) , \displaystyle\!\!\!C(\hat{\mathbf{s}}^{n}_{t+1:t+H})=\!\!\sum_{k=1}^{H}\eta_{k}(-\hat{D}^{n}_{t+k}+\!\!\sum_{j=1}^{\alpha}\lambda_{j}\,\hat{E}^{n}_{t+k,j}), (6)

[50] p: where η k = max ⁡ ( 2 − k + 1 , 1 / 8 ) \eta_{k}=\max(2^{-k+1},1/8) down-weights distant predictions to account for increasing uncertainty. We floor η k \eta_{k} at 1 / 8 1/8 to avoid vanishing contributions from distant steps, which stabilizes planning when H H is moderately large. λ j > 0 \lambda_{j}>0 reflects the severity of violation type j j ( e.g. , pedestrian/vehicle collisions receive larger weights). Finally, we select the action sequence that minimizes the horizon cost in Eq. ( 6 ), i.e. , a model-predictive control policy that favors faster progress while proactively reducing the probability of predicted violations.

[51] h4: 3.1.6 Overall Loss of RaWMPC

[52] p: The RaWMPC framework is trained in an end-to-end manner with a world model loss ℒ world \mathcal{L}_{\text{world}} , a segmentation loss ℒ seg \mathcal{L}_{\text{seg}} from SegViT [ 88 ] , ego-state loss ℒ ego \mathcal{L}_{\text{ego}} , and event loss ℒ event \mathcal{L}_{\text{event}} :

[53] table: ℒ = ℒ world + ℒ seg + ℒ ego + ℒ event . \mathcal{L}=\mathcal{L}_{\text{world}}+\mathcal{L}_{\text{seg}}+\mathcal{L}_{\text{ego}}+\mathcal{L}_{\text{event}}. (7)

[54] p: Following SegViT [ 88 ] , the segmentation term includes classification loss ℒ cls \mathcal{L}_{\text{cls}} (cross-entropy) and the binary mask loss. The mask loss consists of a focal loss ℒ focal \mathcal{L}_{\text{focal}} [ 43 ] and a dice loss ℒ dice \mathcal{L}_{\text{dice}} [ 47 ] for optimizing the segmentation accuracy:

[55] table: ℒ seg = ℒ cls + ℒ focal + ℒ dice . \mathcal{L}_{\text{seg}}=\mathbf{\mathcal{L}}_{\text{cls}}+\mathbf{\mathcal{L}}_{\text{focal}}+\mathbf{\mathcal{L}}_{\text{dice}}. (8)

[56] p: For the other three losses, we use Mean Squared Error (MSE) to supervise the ego-state and world model supervision, and take Binary Cross Entropy (BCE) loss for the event decoder:

[57] table: ℒ world \displaystyle\mathcal{L}_{\text{world}} = 1 H ​ ∑ k = 1 H ‖ 𝐬 ^ t + k − 𝐬 t + k ‖ 2 2 , \displaystyle=\frac{1}{H}\sum\nolimits_{k=1}^{H}\left\|\hat{\mathbf{s}}_{t+k}-\mathbf{s}_{t+k}\right\|_{2}^{2}, ℒ ego \displaystyle\mathcal{L}_{\text{ego}} = 1 H ​ ∑ k = 1 H ‖ 𝐌 ^ t + k − 𝐌 t + k ‖ 2 2 , \displaystyle=\frac{1}{H}\sum\nolimits_{k=1}^{H}\left\|\hat{\mathbf{M}}_{t+k}-\mathbf{M}_{t+k}\right\|_{2}^{2}, (9) ℒ event \displaystyle\mathcal{L}_{\text{event}} = 1 H ​ ∑ k = 1 H B ​ C ​ E ​ ( E ^ t + k , 𝐄 t + k ) , \displaystyle=\frac{1}{H}\sum\nolimits_{k=1}^{H}BCE(\hat{E}_{t+k},\mathbf{E}_{t+k}),

[58] p: where B ​ C ​ E ​ ( ⋅ ) BCE(\cdot) denotes the BCE loss. All the annotations 𝐬 t + k , 𝐌 t + k , 𝐄 t + k \mathbf{s}_{t+k},\mathbf{M}_{t+k},\mathbf{E}_{t+k} along the executed rollout under 𝐀 t : t + H − 1 \mathbf{A}_{t:t+H-1} are obtained from the simulator ( e.g. , CARLA).

[59] h3: 3.2 Risk-aware Interactive Training

[60] p: To enable RaWMPC to evaluate diverse actions and identify risky scenarios, we propose a two-stage risk-aware interactive training scheme, as shown in Fig. 2 . We first warm-start the world model from logged driving trajectories. Then, we refine it via online simulator interaction, intentionally collecting both good (safe, goal-directed) and bad (hazardous) rollouts to improve generalization under out-of-distribution controls and to learn rare but safety-critical events. Notably, RaWMPC does not rely on expert action labels for policy learning. The optional warm-up stage, when used, serves solely to initialize the predictive world model from observed state transitions, rather than to imitate expert actions.

[61] h4: 3.2.1 Offline World Model Warm-up

[62] p: We bootstrap RaWMPC using a small set of logged trajectories to achieve simple and basic state-forecasting capability. Given state-action sequences { ( 𝐬 t , 𝐚 t ) } t = 1 T \{(\mathbf{s}_{t},\mathbf{a}_{t})\}_{t=1}^{T} from NAVSIM or CARLA, the world model predicts the next state 𝐬 ^ t + 1 \hat{\mathbf{s}}_{t+1} and is trained with ℒ world \mathcal{L}_{\text{world}} to match the ground-truth 𝐬 t + 1 \mathbf{s}_{t+1} . We supervise the segmentation and ego-state decoders using the simulator-provided annotations. Since the warm-up trajectories contain no traffic violations, we train the event decoder with an all-zero target. In this way, only a small subset of training data (10%) is typically sufficient for warm-up, providing a reliable initialization for long-horizon rollouts and stabilizing subsequent world model optimization.

[63] figure: Figure 3 : Different action-selection ranges under three driving modes in online simulator interaction. Red denotes high cost and green denotes low cost. rand samples uniformly from all candidates, bad samples from the high-cost region, and good samples from the low-cost one.

[64] h4: 3.2.2 Online Simulator Interactive Training

[65] p: Offline warm-up data are mostly concentrated around human-like safe behaviors and thus provide limited coverage of hazardous or unconventional actions. To learn the consequences of risky behaviors, we perform world-model-guided exploration : selected simulator rollouts are fed back to refine the same world model, progressively improving prediction fidelity and risk sensitivity.

[66] p: Specifically, to ensure temporal continuity and avoid unrealistic control jitter, we sample horizon- H H action sequences (segment-wise) rather than single-step actions (step-wise). The segment-wise sampling allows sustained safe or risky behaviors to unfold and reveals their long-term consequences. At each training step, we sample N s N_{s} horizon- H H candidate action sequences { 𝐀 t : t + H − 1 n } n = 1 N s \{\mathbf{A}^{n}_{t:t+H-1}\}_{n=1}^{N_{s}} , roll out future states 𝐬 ^ n t + 1 : t + H \hat{\mathbf{s}}^{n}_{t+1:t+H} with the current world model, evaluate their costs { C n } \{C^{n}\} using Eq. ( 6 ), and rank candidates by costs.

[67] p: Modes for Interaction. We define three patterns for our risk-aware sampling strategy to select one candidate from { 𝐀 t : t + H − 1 n } n = 1 N s \{\mathbf{A}^{n}_{t:t+H-1}\}_{n=1}^{N_{s}} to execute, as shown in Fig. 3 :

[68] p: Rand samples uniformly from all candidates;

[69] p: Bad samples from high-cost candidates;

[70] p: Good samples from low-cost candidates.

[71] p: At the start of segment r r , the practical control mode is sampled according to probability:

[72] table: m r = { rand , w.p. ​ ε 1 , bad , w.p. ​ ( 1 − ε 1 ) ​ ε 2 , good , w.p. ​ ( 1 − ε 1 ) ​ ( 1 − ε 2 ) , m_{r}=\begin{cases}\texttt{rand},&\text{w.p. }\varepsilon_{1},\\ \texttt{bad},&\text{w.p. }(1-\varepsilon_{1})\varepsilon_{2},\\ \texttt{good},&\text{w.p. }(1-\varepsilon_{1})(1-\varepsilon_{2}),\end{cases} (10)

[73] p: where “w.p.” means “with probability”. ε 1 \varepsilon_{1} controls broad action-space exploration, and ε 2 \varepsilon_{2} controls the fraction of risk-seeking interaction within model-guided sampling.

[74] p: Soft Candidates Selection in Three Modes. Given sorted candidate actions with costs { C n } \{C^{n}\} , we construct two cost-quantile sets: 𝒩 good \mathcal{N}_{\texttt{good}} as the bottom- K K candidates and 𝒩 bad \mathcal{N}_{\texttt{bad}} as the top- K K candidates. To avoid low-information trajectories, we filter 𝒩 bad \mathcal{N}_{\texttt{bad}} by removing degenerate rollouts ( e.g. , those caused by unrealistic excessive control jumps), yielding 𝒩 ~ bad \tilde{\mathcal{N}}_{\texttt{bad}} . In the rand mode, we randomly select the executing action sequence from all candidates.

[75] p: In the good mode, rather than deterministically selecting the minimum-cost candidate, we sample from 𝒩 good \mathcal{N}_{\texttt{good}} using a soft distribution to preserve diversity among low-cost plans and mitigate bias from imperfect model predictions:

[76] table: P ( n ∣ good ) ∝ exp ( − C n / τ g ) , n ∈ 𝒩 good . P(n\mid\texttt{good})\propto\exp(-C^{n}/\tau_{g}),\quad n\in\mathcal{N}_{\texttt{good}}. (11)

[77] p: where τ g \tau_{g} is a temperature hyper-parameter that controls the softness of the sampling distributions in the good mode, trading off greediness for diversity. This stochastic selection avoids repeatedly executing a single estimated optimum and encourages broader coverage of nominal behaviors.

[78] p: In the bad mode, instead of always executing the maximum-cost trajectory, we sample from high-cost candidates to deliberately expose the model to a spectrum of risky outcomes that are under-represented in safe logs:

[79] table: P ⁡ ( n ∣ bad ) ∝ exp ⁡ ( C n / τ b ) , n ∈ 𝒩 ~ bad . P(n\mid\texttt{bad})\propto\exp(C^{n}/\tau_{b}),\quad n\in\tilde{\mathcal{N}}_{\texttt{bad}}. (12)

[80] p: where τ b \tau_{b} is a temperature hyper-parameter. Compared to argmax selection, this soft sampling strategy prevents over-concentration on extreme or degenerate failures while still biasing interaction toward high-risk regions.

[81] p: In this way, segment-wise interaction and soft cost-based sampling bias exploration toward temporally coherent and informative safe and hazardous trajectories, enabling the world model to learn both reasonable dynamics and safety-critical consequences for risk-aware decision making.

[82] figure: Figure 4 : Self-Evaluation Distillation for Policy Learning. A cVAE is trained with RaWMPC-scored actions in a contrastive manner, pulling the condition prior toward positives and pushing it away from negatives. The well-trained decoder serves as the test-time action proposer.

[83] h3: 3.3 Self-Evaluation Distillation for Policy Learning

[84] p: After risk-aware interactive training, RaWMPC can reliably score candidate action sequences by predicting their long-horizon consequences. To reduce the cost of online optimization at test time, we distill this evaluation capability into a lightweight action proposal network, enabling efficient inference without expert demonstrations . The action proposal network corresponds to the “Guidance” module illustrated in Fig. 1 (c), and is used to generate candidate action sequences for predictive control. Our key idea is to use RaWMPC as a self-evaluator to pseudo-label sampled actions and train a generative policy via contrastive learning.

[85] h4: 3.3.1 Action Sampling and Pseudo-labeling

[86] p: Given a state history 𝐬 1 : t \mathbf{s}_{1:t} (simplified as 𝐬 \mathbf{s} ), we randomly sample N s N_{s} horizon- H H action sequences { 𝐀 t : t + H − 1 n } n = 1 N s \{\mathbf{A}^{n}_{t:t+H-1}\}_{n=1}^{N_{s}} (simplified as { 𝐀 n } \{\mathbf{A}^{n}\} ) and compute their costs { C n } \{C^{n}\} with the pretrained RaWMPC. We then form pseudo labels by ranking costs: the lowest-cost sequence is treated as a positive example 𝐀 + \mathbf{A}^{+} , and the top- K K highest-cost sequences are treated as negatives { 𝐀 j − } j = 1 K \{\mathbf{A}^{-}_{j}\}_{j=1}^{K} . This construction transfers RaWMPC’s knowledge (low-risk / high-quality actions) to the proposal network while avoiding any external supervision.

[87] h4: 3.3.2 Action Proposal Network

[88] p: Following [ 60 , 87 ] , we adopt a conditional VAE (cVAE) with an action encoder q θ ​ ( z | 𝐀 , 𝐬 ) q_{\theta}(z|\mathbf{A},\mathbf{s}) , a conditional prior p γ ​ ( z | 𝐬 ) p_{\gamma}(z|\mathbf{s}) , and a decoder p ψ ​ ( 𝐀 | z , 𝐬 ) p_{\psi}(\mathbf{A}|z,\mathbf{s}) . The decoder serves as the proposal policy at inference.

[89] p: For the positive action, we obtain a Gaussian posterior q + = q θ ​ ( z | 𝐀 + , 𝐬 ) = 𝒩 ⁡ ( μ + , diag ⁡ ( ( σ + ) 2 ) ) q^{+}=q_{\theta}(z|\mathbf{A}^{+},\mathbf{s})=\mathcal{N}(\mu^{+},\mathrm{diag}((\sigma^{+})^{2})) and train the decoder to reconstruct 𝐀 + \mathbf{A}^{+} . For each negative action 𝐀 j − \mathbf{A}^{-}_{j} , we compute q j − = q θ ​ ( z | 𝐀 j − , 𝐬 ) = 𝒩 ⁡ ( μ j − , diag ⁡ ( ( σ j − ) 2 ) ) q^{-}_{j}=q_{\theta}(z|\mathbf{A}^{-}_{j},\mathbf{s})=\mathcal{N}(\mu^{-}_{j},\mathrm{diag}((\sigma^{-}_{j})^{2})) , but do not reconstruct negatives to prevent the generator from imitating unsafe behaviors. The conditional prior is p c = p γ ​ ( z | 𝐬 ) = 𝒩 ⁡ ( μ c , diag ⁡ ( ( σ c ) 2 ) ) p^{c}=p_{\gamma}(z|\mathbf{s})=\mathcal{N}(\mu^{c},\mathrm{diag}((\sigma^{c})^{2})) .

[90] h4: 3.3.3 Contrastive Training Objective

[91] p: To address the lack of expert supervision in policy learning, we use an InfoNCE objective to make the conditional prior predictive of high-quality actions. Concretely, there are two potential contrastive formulations:

[92] p: Using p c p^{c} as the anchor, pulling p c p^{c} toward q + q^{+} while pushing it away from { q − } j = 1 K \{q^{-}\}_{j=1}^{K} .

[93] p: Using q + q^{+} as the anchor, pulling q + q^{+} toward p c p^{c} while pushing it away from { q − } j = 1 K \{q^{-}\}_{j=1}^{K} .

[94] p: We empirically found that the former often produces under-optimized trajectories. One possible reason is that negative samples are far more numerous and broadly cover the latent space, therefore p c p^{c} is easily driven to a region that is far from most negatives yet not sufficiently close to the positive. In contrast, the latter explicitly pulls p c p^{c} toward the statistical center of the positive posterior and, via q + q^{+} , indirectly separates it from the negatives, leading to more stable learning and higher-quality trajectories. Therefore, we adopt the latter design choice to define our InfoNCE objective as:

[95] table: ℒ c \displaystyle\mathcal{L}_{\text{c}} = − log ⁡ exp ⁡ ( ℓ + ) exp ⁡ ( ℓ + ) + ∑ j = 1 K exp ⁡ ( ℓ j − ) , \displaystyle=-\log\frac{\exp(\ell^{+})}{\exp(\ell^{+})+\sum_{j=1}^{K}\exp(\ell^{-}_{j})}, (13) ℓ + \displaystyle\ell^{+} = − 𝒟 ( q + , p c ) / τ , \displaystyle=-\mathcal{D}(q^{+},p^{c})/\tau, ℓ j − \displaystyle\ell^{-}_{j} = − 𝒟 ( q + , q − j ) / τ , \displaystyle=-\mathcal{D}(q^{+},q^{-}_{j})/\tau,

[96] p: where 𝒟 ⁡ ( ⋅ , ⋅ ) \mathcal{D}(\cdot,\cdot) is the Wasserstein-2 distance between Gaussians and τ \tau is a temperature.

[97] figure: Table 1 : Comparison with SOTA approaches on the closed-loop Bench2Drive benchmark on CARLA simulator. ↑ \uparrow means the higher the better. DS is taken as the primary metric in comparison and we rank all the methods accordingly, with bold indicating best performance. Method Venue Scheme DS ↑ \uparrow SR(%) ↑ \uparrow Efficiency ↑ \uparrow Comfortness ↑ \uparrow VAD [ 31 ] ICCV 2023 IL 42.35 15.00 157.94 46.01 SparseDrive [ 69 ] ICRA 2025 IL 44.54 16.71 170.21 48.63 GenAD [ 99 ] ECCV 2024 IL 44.81 15.90 - - UniAD [ 25 ] CVPR 2023 IL 45.81 16.36 129.21 43.58 MomAD [ 68 ] CVPR 2025 IL 47.91 18.11 174.91 51.20 UAD [ 16 ] T-PAMI 2025 IL 49.22 20.45 189.53 52.71 BridgeAD [ 89 ] CVPR 2025 IL 50.06 22.73 - - TCP [ 81 ] NeurIPS 2022 IL 59.90 30.00 76.54 18.08 WoTE [ 39 ] ICCV 2025 IL 61.71 31.36 - - DriveDPO [ 61 ] NeurIPS 2025 IL & RL 62.02 30.62 166.80 26.79 ThinkTwice [ 28 ] CVPR 2023 IL 62.44 31.23 69.33 16.22 DriveTransformer [ 30 ] ICLR 2025 IL 63.46 35.01 100.64 20.78 DriveAdapter [ 27 ] ICCV 2023 IL 64.22 33.08 70.22 16.01 Raw2Drive [ 85 ] NeurIPS 2025 RL 71.36 50.24 214.17 22.42 Hydra-NeXt [ 40 ] ICCV 2025 IL 73.86 50.00 197.76 20.68 HiP-AD [ 73 ] ICCV 2025 IL 86.77 69.09 203.12 19.36 RaWMPC w/o Warm-up - PC 87.34 69.62 203.25 30.95 RaWMPC - PC 88.31 70.48 206.85 32.65 Pretrained VLM-based Approach ReAL-AD [ 44 ] ICCV 2025 IL 41.17 11.36 - - Dual-AEB [ 94 ] ICRA 2025 IL 45.23 10.00 - - ETA [ 21 ] ICCV 2025 IL 74.33 48.33 186.04 25.77 VLR-Drive [ 35 ] ICCV 2025 IL 75.01 50.00 122.52 0.59 ORION [ 14 ] ICCV 2025 IL 77.74 54.62 151.48 17.38 SimLingo [ 55 ] CVPR 2025 IL 85.94 66.82 244.18 30.76

[98] h4: 3.3.4 Overall Loss of Action Proposal Network

[99] p: The total loss of our cVAE combines reconstruction, KL regularization, and contrastive loss:

[100] table: ℒ total \displaystyle\mathcal{L}_{\text{total}} = 𝔼 z ∼ q + ​ [ − log ⁡ p ψ ​ ( 𝐀 + ∣ z , 𝐬 ) ] \displaystyle=\mathbb{E}_{z\sim q^{+}}\!\left[-\log p_{\psi}(\mathbf{A}^{+}\mid z,\mathbf{s})\right] (14) + β D KL ( q + ∥ p c ) + λ ℒ c . \displaystyle+\beta\,D_{\text{KL}}\!\left(q^{+}\,\|\,p^{c}\right)+\lambda\,\mathcal{L}_{\text{c}}.

[101] p: This self-evaluation distillation trains a fast proposal policy that generates candidate action sequences consistent with RaWMPC’s evaluations, eliminating the need for expert demonstrations during policy learning.

[102] h2: 4 Experiments

[103] p: In this section, we present a comprehensive performance comparison between the proposed framework and state-of-the-art methods. We also conduct extensive ablation studies to assess the effectiveness of our predictive control approach.

[104] h3: 4.1 Benchmarks

[105] p: Following prior works [ 39 , 61 , 40 ] , we evaluate RaWMPC on two widely used benchmarks: Bench2Drive [ 29 ] and NAVSIM [ 11 ] . They are complementary: Bench2Drive provides fully interactive closed-loop evaluation in CARLA [ 12 ] with dense annotations, while NAVSIM evaluates large-scale real-world planning via a data-driven, non-reactive simulation-based short-horizon rollout with safety- and progress-aware metrics.

[106] p: Bench2Drive. Bench2Drive is a CARLA Leadboard v2 closed-loop benchmark for multi-ability stress testing under complex interactions (e.g., cut-ins, overtakes, detours, emergency braking, and give-way). Its official dataset contains ∼ \sim 2M fully annotated frames from short clips spanning 44 scenarios, 23 weather conditions, and 12 towns; the commonly used Base training set contains 1K clips. Closed-loop evaluation is performed on 220 short routes (each focused on a single scenario), enabling stable and fine-grained comparison. We report four official metrics: Driving Score (DS) , Success Rate (SR) , Efficiency , and Comfortness . DS is the primary aggregate score with penalties for safety and rule violations; SR measures successful completion; Efficiency reflects progress; and Comfortness captures motion smoothness.

[107] figure: Table 2 : Comparison with the SOTA approaches on NAVSIM test set. ↑ \uparrow means the higher the better. PDMS is taken as the primary metric in comparison and we rank all the methods accordingly, with bold indicating best performance. Method Venue Scheme NC ↑ \uparrow DAC ↑ \uparrow EP ↑ \uparrow TTC ↑ \uparrow C ↑ \uparrow PDMS ↑ \uparrow Human - - 100 100 87.5 100 99.9 94.8 DrivingGPT [ 8 ] ICCV 2025 IL 98.9 90.7 79.7 94.9 100.0 82.4 UniAD [ 25 ] CVPR 2023 IL 97.8 91.9 78.8 92.9 100.0 83.4 Latent TransFuser [ 10 ] T-PAMI 2023 IL 97.4 92.8 79.0 92.4 100.0 83.8 PARA-Drive [ 80 ] CVPR 2024 IL 97.9 92.4 79.3 93.0 99.8 84.0 TransFuser [ 10 ] T-PAMI 2023 IL 97.7 92.7 79.8 92.7 100.0 84.5 LAW [ 38 ] ICLR 2025 IL 96.4 95.4 81.7 88.7 99.9 84.6 World4Drive [ 100 ] ICCV 2025 IL 97.4 94.3 79.9 92.8 100.0 85.1 DiffusionDrive [ 42 ] CVPR 2025 IL 98.2 96.2 88.2 94.7 100.0 88.1 WoTE [ 39 ] ICCV 2025 IL 98.5 96.8 81.9 94.9 99.9 88.3 Hydra-NeXt [ 40 ] ICCV 2025 IL 98.1 97.7 81.8 94.6 100.0 88.6 UAD [ 16 ] T-PAMI 2025 IL 99.5 96.9 78.8 97.5 100.0 89.3 DriveDPO [ 61 ] NeurIPS 2025 IL & RL 98.5 98.1 84.3 94.8 99.9 90.0 GoalFlow [ 82 ] CVPR 2025 IL 98.4 98.3 85.0 94.6 100.0 90.3 RaWMPC w/o Warm-up - PC 98.3 98.2 85.3 94.5 99.9 90.5 RaWMPC - PC 98.9 98.3 86.1 95.6 99.9 91.3

[108] p: NAVSIM. NAVSIM benchmarks sensor-based planning on large-scale real-world data built on OpenScene (a planning-oriented reprocessing of nuPlan logs). The task predicts a 4-second future ego trajectory (typically 8 waypoints) given a short history (e.g., 1.5 seconds) of observations. Following prior works [ 61 , 39 ] , we use the official splits: Navtrain ( ∼ \sim 103K samples) and Navtest ( ∼ \sim 12K samples). We report NAVSIM metrics including NC , DAC , EP , TTC , C , and the primary score PDMS , where PDMS = NC ⋅ DAC ⋅ ( 5 ​ EP + 5 ​ TTC + 2 ​ C ) / 12 \mathrm{PDMS}=\mathrm{NC}\cdot\mathrm{DAC}\cdot(5\mathrm{EP}+5\mathrm{TTC}+2\mathrm{C})/12 . These metrics jointly capture safety, compliance, progress, and motion quality. All results are computed with the official toolkits and recommended splits.

[109] p: Our experiments combine offline warm-up with online simulator interaction, leveraging RaWMPC to learn predictive dynamics and risk-aware decision making. We adopt Bench2Drive for interactive closed-loop evaluation and NAVSIM for large-scale real-world generalization. We further conduct ablations to analyze key training components and strategies.

[110] h3: 4.2 Implementation Details

[111] p: Network architecture. We employ a pretrained ViT [ 66 ] as the vision encoder and use the SegViT segmentation head [ 88 ] as the segmentation decoder. BEV features are extracted from multi-view images using the query-based view transformer [ 41 ] . Following previous works [ 39 , 10 ] , the input image resolution is 1024 × 256 1024\times 256 , and the BEV feature map resolution is 256 × 256 256\times 256 . We use down-sampling factors of 32 (front-view) and 16 (BEV), resulting in 512 visual tokens 𝐢 t \mathbf{i}_{t} (256 per branch). Measurement inputs are encoded through an MLP-based encoder into 4 measurement tokens 𝐦 t \mathbf{m}_{t} , and driving actions, represented as three scalar values (steer, throttle, brake), are transformed into 3 action tokens 𝐚 t \mathbf{a}_{t} via a linear layer. We implement the world model as a transformer with 4 layers and 8 attention heads. RaWMPC predicts H = 10 H{=}10 future steps conditioned on the past 5 observed steps, and evaluates N = 10 N{=}10 candidate action sequences proposed by the distilled action proposal network (described in Section 3.3 ) using the cost in Eq. ( 6 ) during inference. During action selection, we use η k = max ⁡ ( 2 − k + 1 , 1 / 8 ) \eta_{k}=\max(2^{-k+1},1/8) to downweight distant predictions, and set the event severity weights to λ j = 10 , 15 , 30 \lambda_{j}={10,15,30} for off-lane driving, traffic-sign violations, and collisions, respectively.

[112] p: Training. RaWMPC is trained with the two-stage risk-aware interactive training strategy described in Section 3.2 . We first perform an offline warm-up using 10% of the training data (100 clips for Bench2Drive and 10K samples for NAVSIM), and then refine the model via online interaction using the proposed risk-aware training scheme. The random-sampling probability ε 1 \varepsilon_{1} is linearly annealed from 1 to 0, while the risk-sampling probability ε 2 \varepsilon_{2} is linearly increased from 0 to 0.3. We maintain a replay buffer of size 10K frames to store recent interaction data (e.g., RGB images, semantic segmentation, ego measurements, and traffic-event annotations). We use segment-wise sampling of horizon- H = 10 H{=}10 action sequences to ensure temporal continuity. In good/bad modes, we rank the N s = 50 N_{s}{=}50 candidates by cost and sample from the bottom/top- K = 5 K{=}5 sets using temperatures τ g = 0.5 \tau_{g}=0.5 and τ b = 1.0 \tau_{b}=1.0 . An episode terminates when any of the following conditions is met: (1) the ego vehicle incurs 3 collisions, (2) the ego vehicle goes off-road or remains stuck for 100 consecutive steps, or (3) the ego vehicle successfully completes the route. Across offline warm-up and online interaction, we train RaWMPC using a total of 1K clips on Bench2Drive and 100K samples on NAVSIM (comparable in scale to the official training sets for fair comparison), on four NVIDIA A100 GPUs. We use Adam [ 33 ] with an initial learning rate of 10 − 4 10^{-4} decayed to 10 − 5 10^{-5} , and a batch size of 16.

[113] p: Self-evaluation distillation. For self-evaluation distillation (Section 3.3 ), the action proposal network is implemented as a cVAE [ 67 ] with a 32-dimensional latent space. During contrastive training, we sample N s = 50 N_{s}{=}50 action sequences, treat the minimum-cost sequence as the positive example 𝐀 + \mathbf{A}^{+} , and use the top- K = 5 K{=}5 highest-cost sequences as negatives. We optimize the proposal network with the objective in Section 3.3 , using temperature τ = 0.3 \tau{=}0.3 , a KL weight schedule β : 0 → 0.1 \beta:0\rightarrow 0.1 , and a contrastive weight λ = 0.1 \lambda{=}0.1 . At inference, we sample N = 10 N{=}10 candidates from the cVAE decoder and select the final action by minimizing the predicted cost (Eq. ( 6 )) under the world-model rollout.

[114] h3: 4.3 Comparison with the State-of-the-Art

[115] figure: Figure 5 : Qualitative comparison under weather-induced domain shift ( Sunny-only → \rightarrow Rainy ). All methods are trained on Sunny-only data and evaluated in Rainy conditions. LAW [ 38 ] misses the lead vehicle, causing a severe frontal collision. WoTE [ 39 ] and SimLingo [ 55 ] reduce severity by evasive maneuvers but still collide due to degraded perception–decision reliability and weak safety-margin enforcement. RaWMPC avoids collisions by selecting the minimum-risk predictive-control action under uncertainty.

[116] figure: Table 3 : Performance comparison under domain shift. All methods are trained on either Sunny only or Sunny & Rainy data, and evaluated exclusively on Rainy scenarios. ↑ \uparrow indicates higher is better. Method Venue Scheme Training Data Tested on Rainy DS ↑ \uparrow SR(%) ↑ \uparrow LAW ICLR 2025 IL Sunny & Rainy 34.54 7.09 Sunny only 23.58 3.56 WoTE ICCV 2025 IL Sunny & Rainy 36.54 7.85 Sunny only 28.65 5.21 SimLingo (Pretrained-VLM) CVPR 2025 IL Sunny & Rainy 51.69 13.68 Sunny only 33.49 8.97 RaWMPC – PC Sunny & Rainy 53.67 14.96 Sunny only 41.36 10.83

[117] p: In this section, we compare RaWMPC with state-of-the-art end-to-end driving methods on the closed-loop Bench2Drive benchmark in CARLA and the NAVSIM test set. To reflect our main claim, we report two training settings: (i) w/o warm-up , where RaWMPC is trained without using any offline logged video, and (ii) the full setting, where a small set of logged driving trajectories is used as an optional warm start. The warm start empirically accelerates convergence and further improves final performance, while RaWMPC already surpasses prior state-of-the-art even without it.

[118] h4: 4.3.1 Evaluation on Bench2Drive

[119] p: Table 1 illustrates the closed-loop results on Bench2Drive. RaWMPC achieves the best overall performance among all compared methods, reaching 88.31 DS and 70.48 % SR in the full setting. More importantly, even without warm-up (i.e., without logged trajectories), RaWMPC still attains 87.34 DS and 69.62% SR, surpassing strong recent baselines such as HiP-AD [ 73 ] (86.77 DS / 69.09% SR) and the pretrained-VLM method SimLingo [ 55 ] (85.94 DS / 66.82% SR). In addition, RaWMPC maintains competitive efficiency and achieves higher comfortness than most high-performing closed-loop agents, indicating that the gains are not obtained by aggressive maneuvers but by more reliable decision-making.

[120] h4: 4.3.2 Evaluation on NAVSIM

[121] p: Table 2 summarizes the results on NAVSIM. RaWMPC achieves the highest PDMS of 91.3 among all learning-based methods. Without warm-up, RaWMPC still reaches 90.5 PDMS, already outperforming previous best methods (e.g., GoalFlow [ 82 ] : 90.3). The warm start further improves PDMS (90.5 → \rightarrow 91.3), consistent with the observation that a small amount of logged trajectories can accelerate convergence and improve performance, while not being required to achieve state-of-the-art results.

[122] h4: 4.3.3 Generalization under weather-induced domain shift

[123] p: To evaluate robustness beyond the training distribution, we conduct a weather-shift study where all methods are evaluated exclusively on Rainy scenarios while being trained on either Sunny only or Sunny & Rainy data (Table 3 ). A key observation is that imitation-based methods are sensitive to training-domain coverage: when rainy conditions are absent from training (Sunny-only), their performance drops notably, reflecting limited transfer to previously unseen environments. In contrast, RaWMPC achieves the best DS and SR under both training regimes, and notably still significantly outperforms strong IL baselines (LAW, WoTE) and SimLingo when trained on Sunny only ( i.e. , facing an unseen rainy target domain). Moreover, compared with SimLingo, RaWMPC exhibits substantially smaller degradation when rainy data is removed from training, indicating stronger robustness to previously unseen conditions.

[124] p: Figure 5 shows a qualitative example of this Sunny-only → \rightarrow Rainy shift. LAW fails to recognize the lead vehicle under the altered visual conditions and results in a high-severity frontal collision. WoTE and SimLingo attempt evasive maneuvers that reduce the impact relative to a direct frontal crash , yet the scene still ends in a side-swipe/rear collision. A plausible explanation is that the rainy shift degrades the reliability of the perception–decision stack, while the downstream policy does not explicitly optimize for minimum-risk clearance under uncertainty, yielding insufficient safety margins during close-proximity avoidance (e.g., inaccurate motion anticipation or mismatched ego response on wet roads). By contrast, RaWMPC explicitly evaluates the predicted consequences of candidate action sequences with a risk-aware world model and selects the minimum-risk predictive-control behavior, maintaining safe clearance under uncertainty.

[125] p: We attribute this advantage to RaWMPC’s risk-aware predictive-control formulation: instead of reproducing expert actions, RaWMPC learns risk-awareness from interaction and selects actions by minimizing predicted risk via the learned world model. Such an objective encourages transferable decision principles (e.g., maintaining safe margins and acting conservatively under uncertainty) that remain effective when appearance and dynamics change across domains. Thus, RaWMPC is less dependent on exhaustive expert action coverage for corner cases, which better matches the long-tail nature of real-world deployment where unseen scenarios are inevitable.

[126] figure: Figure 6 : Visualization of the predictive control procedure . At time t t , we show the front-view and the BEV images (with segmentation). Dashed curves indicate candidate actions and highlighted agents denote key risks. Rollouts from t + 1 t+1 to t + 5 t+5 illustrate predicted consequences, and the bottom panel reports each action’s outcomes and costs ( e.g. , collision, sidewalk intrusion, stopping distance). Scenario 1 : RaWMPC slows down, proceeds briefly, then stops for the pedestrian. Scenario 2 : RaWMPC waits briefly, then turns left to avoid both the front-left vehicle and the parked car.

[127] h4: 4.3.4 Qualitative visualization of predictive control

[128] p: We provide some visualization results of the predictive control procedure of RaWMPC in Fig. 6 . Given RGB observations and high-level navigation commands (e.g., keep going straight or merge left), our generative policy proposes a small set of candidate action sequences (e.g., keep going straight, detour, brake, and lane change). For each candidate, the risk-aware world model predicts the near-future semantic traffic state and the decoding module evaluates its consequence from both task progress and safety perspectives, including collision risk, off-lane/sidewalk intrusion risk, and progress-related penalties such as getting stuck in traffic. The final action is selected by comparing these predicted consequences and choosing the minimum-cost one under the navigation goal.

[129] p: In the first case, going straight collides with a crossing pedestrian, while detours either collide with an oncoming vehicle or drive onto the sidewalk; RaWMPC chooses slow down, straight briefly, then stop to safely stop in front of the pedestrian (instead of an overly conservative early brake). In the second case, going straight or merging left immediately causes a collision, steering right hits a parked vehicle, and stopping leads to a deadlock; thus RaWMPC selects pause briefly, then merge left for a collision-free merge. These cases demonstrate that RaWMPC can proactively avoid risky behaviors by explicitly forecasting and comparing action consequences, rather than merely following a single command or relying on a fixed fallback maneuver.

[130] h3: 4.4 Ablation Study

[131] p: In this section, we provide comprehensive ablation studies of the proposed approach using the Bench2Drive dataset.

[132] h4: 4.4.1 Analysis of Framework

[133] figure: Table 4 : Ablation study on the proposed framework. Method Metrics DS ↑ \uparrow SR(%) ↑ \uparrow Entire RaWMPC ( Ours ) 88.31 70.48 w/o Semantic Guidance 82.36 -5.95 62.69 -7.79 w/o Segmentation Decoder 70.85 -17.46 48.95 -21.53 w/o Action Selection 61.35 -26.96 30.98 -39.50

[134] p: Table 4 analyzes core components aligned with our model design (Sec. 3.1.1 ). w/o Semantic Guidance removes semantic-guided event decoding, i.e. , the fusion of semantic attention from the segmentation decoder into the event decoder. This leads to a clear drop (DS 88.31 → \rightarrow 82.36, SR 70.48% → \rightarrow 62.69%), showing that accurate safety-event prediction is crucial for risk-aware cost evaluation. w/o Segmentation Decoder further removes the segmentation decoding branch and its supervision, resulting in a large degradation (DS 70.85 / SR 48.95%), which indicates that forecasting high-level semantics is essential for reliable long-horizon rollouts. w/o Action Selection disables predictive control in Eq. ( 1 ) (bypassing cost-based ranking in Eq. ( 6 )) and directly executes the proposal/guidance output, causing the most severe collapse (DS 61.35 / SR 30.98%). This confirms that selecting actions by explicitly evaluating predicted long-horizon consequences is the key to RaWMPC.

[135] h4: 4.4.2 Analysis of Risk-Aware Training

[136] p: Table 5 evaluates the risk-aware interaction training strategy used to refine the world model. Our risk-aware sampling follows the design in Sec. 3.2 : besides random exploration, it uses the current RaWMPC to score candidate action sequences and deliberately collects both good (low-cost) and bad (high-cost) rollouts, improving coverage of rare safety-critical outcomes. Replacing it with ϵ \epsilon -greedy sampling (random with probability ϵ 1 \epsilon_{1} , otherwise only selecting low-cost rollouts) reduces performance (DS 83.86 / SR 61.74%), showing that excluding high-cost failures weakens learning of risky consequences. Pure random sampling further degrades results (DS 70.41 / SR 46.82%), indicating that unguided data collection is substantially less efficient for learning long-horizon consequences.

[137] figure: Table 5 : Ablation study on the risk-aware training. Method Metrics DS ↑ \uparrow SR(%) ↑ \uparrow Risk-aware Sampling ( Ours ) 88.31 70.48 ϵ \epsilon -Greedy Sampling 83.86 -4.45 61.74 -8.74 Random Sampling 70.41 -17.90 46.82 -23.66

[138] figure: Table 6 : Results obtained using different action supervision in policy learning. Policy Learning Data Metrics DS ↑ \uparrow SR(%) ↑ \uparrow Pos. & Neg. Actions ( Ours ) 88.31 70.48 Expert Actions 86.75 -1.56 68.25 -2.23 Only Positive Actions 83.65 -4.66 66.52 -3.96

[139] h4: 4.4.3 Analysis of Self-Evaluation Distillation

[140] p: Table 6 studies how to train the action proposal network in Sec. 3.3 . Our default setting uses RaWMPC as a self-evaluator to pseudo-label actions: the lowest-cost sequence is treated as a positive, while high-cost sequences serve as negatives, which yields the best performance (DS 88.31 / SR 70.48%). Training the proposal network only with expert actions slightly degrades performance (DS 86.75 / SR 68.25%), suggesting that self-evaluated targets align better with the predictive-control objective than direct imitation targets. Using only positive actions further drops performance (DS 83.65 / SR 66.52%), indicating that explicitly contrasting against high-risk negatives is important for preventing unsafe candidates and improving downstream selection.

[141] h4: 4.4.4 Discussion on Prediction Horizon

[142] p: Table 7 ablates the planning horizon H H used in the world-model rollout and cost evaluation (Eq. ( 6 )). Short horizons fail to capture delayed consequences, leading to poor performance (H=1: DS 57.85 / SR 28.64%; H=5: DS 74.98 / SR 49.52%). Increasing to H=10 yields the best results (DS 88.31 / SR 70.48%), as it provides sufficient look-ahead for risk assessment while keeping prediction uncertainty manageable. Further increasing to H=15 degrades performance (DS 82.34 / SR 62.38%), likely due to accumulated rollout errors that affect cost-based ranking.

[143] figure: Table 7 : Results obtained using different amounts of prediction horizon. Prediction Horizon Metrics DS ↑ \uparrow SR(%) ↑ \uparrow H=1 57.85 -30.46 28.64 -41.84 H=5 74.98 -13.33 49.52 -20.96 H=10 ( Ours ) 88.31 70.48 H=15 82.34 -5.97 62.38 -8.10

[144] h4: 4.4.5 Discussion on Warm-up

[145] figure: Table 8 : Results obtained using different amounts of offline learning data in warm-up. Warm-up Data Metrics DS ↑ \uparrow SR(%) ↑ \uparrow 0% 87.34 -0.97 69.62 -0.86 10% 88.31 70.48 20% 88.09 -0.22 70.32 -0.16 30% 86.95 -1.36 68.52 -1.96

[146] p: Table 8 ablates the fraction of offline logged trajectories used for warm-up before interactive training. In this study, we keep the total number of training samples fixed and vary only the proportion allocated to offline warm-up data. Without warm-up (0%), performance drops (DS 87.34 / SR 69.62%), suggesting that training from scratch leads to less reliable rollouts and a less stable early optimization stage. Using a small amount of logged trajectories (10%) yields the best results (DS 88.31 / SR 70.48%), indicating that a light warm-up provides useful predictive priors (e.g., basic dynamics modeling and perception decoding) that improve long-horizon rollout quality and downstream control. However, further increasing the warm-up ratio begins to degrade performance (20%: DS 88.09 / SR 70.32%; 30%: DS 86.95 / SR 68.52%). We attribute this trend to the fact that offline logged trajectories are strongly biased toward safe, human-like behaviors and contain few hazardous events. Consequently, allocating too much data to offline warm-up reduces the opportunities for subsequent online interaction to explore unconventional actions and collect safety-critical failures—especially in dangerous scenarios—which are essential for learning robust risk awareness.

[147] h4: 4.4.6 Discussion on Control Pattern

[148] p: Table 9 compares predictive control to directly optimizing a policy with model-based reinforcement learning (RL). Predictive control achieves substantially higher performance (DS 88.31 / SR 70.48%) than model-based RL (DS 73.58 / SR 51.85%). This validates the benefit of evaluating candidate action sequences via decoded future outcomes (segmentation, events, ego-states) and selecting the minimum-cost one, rather than relying on end-to-end policy optimization alone.

[149] figure: Table 9 : Ablation study on the control pattern with learned world model. Method Metrics DS ↑ \uparrow SR(%) ↑ \uparrow Predictive Control ( Ours ) 88.31 70.48 Reinforcement Learning 73.58 -14.73 51.85 -18.63

[150] h4: 4.4.7 World-Model Prediction Accuracy

[151] p: Table 10 reports the event prediction quality used by the cost function in Eq. ( 6 ). The predictor achieves high accuracy across event types (0.91–0.96) and strong recall on collision-related events (e.g., pedestrian collision recall 0.99), providing reliable signals for risk-aware evaluation. We observe lower precision for some rare events (e.g., pedestrian collision precision 0.52), reflecting a conservative tendency with more false positives; in safety-critical driving, prioritizing recall can be preferable to missing hazards.

[152] figure: Table 10 : Prediction accuracy of future traffic events with learned world model. Collision Running Traffic Sign Pedestrian Vehicle Static Accuracy 0.96 0.91 0.93 0.91 Recall 0.99 0.84 0.89 0.84 Precision 0.52 0.62 0.63 0.68

[153] h2: 5 Conclusion

[154] p: In this work, we proposed RaWMPC , a risk-aware world-model predictive control framework for end-to-end autonomous driving that does not require expert action supervision . RaWMPC learns an action-conditioned world model to roll out multiple candidate behaviors, predicts future semantics and safety-critical events, and selects actions by explicitly minimizing a risk-aware cost. To make rare-but-catastrophic outcomes predictable and avoidable, we introduced a risk-aware interaction strategy that intentionally collects both safe and hazardous rollouts, and we further proposed self-evaluation distillation to train an efficient action proposal policy using RaWMPC as a self-evaluator. Extensive experiments on Bench2Drive and NAVSIM show that RaWMPC achieves state-of-the-art performance and stronger robustness under domain shift, even without offline warm-up, showing the potential to significantly reduce the reliance on costly real-world expert demonstrations. For future work, we will explore domain adaptation and more efficient planning to better support real-world deployment and sim-to-real transfer.

[155] h2: Statements and Declarations

[156] p: Competing interests. The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

[157] p: Data availability. This work does not propose any new dataset. The datasets (Bench2Drive [ 29 ] and NAVSIM [ 11 ] ) that support the findings of this study are openly available at the URLs: Bench2Drive and NAVSIM .

[158] h2: References

[159] h2: Instructions for reporting errors

[160] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[161] p: Tip: You can select the relevant text first, to include it in your report.

[162] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[163] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
