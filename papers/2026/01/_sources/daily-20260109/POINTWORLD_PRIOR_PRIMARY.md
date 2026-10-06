# PointWorld 窗前正文身份定点核

2026-10-02 实际 GET 两个官方 GitHub API（HTTP200），不是从 repository creation 或 authored commit 时间推 first-public：

- run https://api.github.com/repos/point-world/point-world.github.io/actions/runs/20761798422 ：name=`pages build and deployment`，head_sha=`e55cb6915faafb983ec628da44148add97b9a651`，created_at=`2026-01-06T20:54:38Z`，updated_at=`2026-01-06T21:00:05Z`，status=`completed`，conclusion=`success`；官方run页 https://github.com/point-world/point-world.github.io/actions/runs/20761798422 。这是成功网页部署的公开上界线索，不虚构最早分钟。
- contents https://api.github.com/repos/point-world/point-world.github.io/contents/index.html?ref=e55cb6915faafb983ec628da44148add97b9a651 ：path=`index.html`，blob_sha=`e0aa26cead965883a98c57a2ab3f31d8e1c932e8`，download_url=`https://raw.githubusercontent.com/point-world/point-world.github.io/e55cb6915faafb983ec628da44148add97b9a651/index.html`。实际base64 decode该exact原HTML，按p/h1–3提取必要原文，非current page倒推。

## 当时原文必要摘段

> PointWorld predicts full-scene 3D point flow from partially observable RGB-D captures and robot actions (represented as 3D point flow). Trained on a large-scale dataset consisting of 500 hours interactions with high-quality custom 3D annotations, PointWorld enables zero-shot planning for in-the-wild manipulation tasks. We will release the code, data, and pre-trained checkpoints.

> We introduce PointWorld, a large pre-trained 3D world model that unifies state and action in a shared 3D space as 3D point flows: given one or few RGB-D images and a sequence of low-level robot action commands, PointWorld forecasts per-pixel displacements in 3D that respond to the given actions. By representing actions as 3D point flows instead of embodiment-specific action spaces (e.g., joint positions), this formulation directly conditions on physical geometries of robots while seamlessly integrating learning across embodiments.

> NOTE: The model operates on voxel-downsampled (1.5 cm) point clouds. For visual clarity, we upsample the predictions and and the ground truth by applying the same displacement to all points within each voxel. The green color in ground truth visualization indicate the points that are inaccurate due to occlusion (from 2D trackers used to provide annotations). Note that these points are not used to supervise the model, hence it's often observed that the model predicts better than the ground truth for occluded point flows after training.

原文另外同摘要明确2M trajectories/500hours与0.1s模型forward（不采用其性能宣言），末段有MPC diverse skills/no task-specific training。故本次拟准入的**shared3D action/state接口本身**已有完全窗前公开正文上界≤Jan6T21:00:05Z，早于Jan09起点Jan8T01Z；arXiv DOI日期区间只能界arXiv事件，不改变该正文首次归属。

提案：窗前首次公开关闭，不评分、不为Jan09写Books。已经实际读v1必要方法/评价保留EVIDENCE_2，不冒称全部v1实验亦已窗前公开；当前官方页没有必要勘误/安全/重要变化事件标识。普通新arXiv收录不自动准入重要revision。待root原run+exactHTML独立身份复核，尚未日级验收。
# 非作者结果：root fresh GET官方run20761798422与contents exactSHA，实际读完整摘要shared3D state/action/FK及500h和voxelannotation。具体拟贡献的窗前公开上界通过；不把commit/created当首次分钟、不授全arXiv结果旧公开，不写Jan09Books。
