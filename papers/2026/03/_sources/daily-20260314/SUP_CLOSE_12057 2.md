# 12057：最低实际delta关闭提案，待非作者裁决

mar14_supplement；固定Mar13BJT窗口。精确v1 `SUP_NECESSARY_12057.raw/txt` GET200/449648B/2026-10-09T16:01:56.188677UTC。完整题摘/四作者/current v1/v2/v3 history在`SUP_ABS_12057.txt`，无具名撤回/纠错/先稿信号，未查尽外部版本。日级日期由root实际六份official owning/findable/注册上界/正常公告下界与ID规则夹证PASS，见`SUP_DATE_FOURTH.md`/`SUP_DATE_12057.raw`；v1Thu15:26:19UTC明确处本公告批次，不单以submitted/registered作首次公开。

实际读§2.2/§3.1–3.4 Eq5–15/Alg1全（解析B39–86），§5.1评价/配置及§5.3参数反侧和§5.4/结尾，不遍历三图像/视频附件、完整PDF/代码。理想fine y未知，实际用coarse y-tilde点的Gaussian forward kernel替代fine h；Eq12为(alpha*y-tilde−x)/sigma²−score，Eq15与noise权重lambda结合，等价于score与这个coarse kernel score的局部插值，不是学到未知fine/coarse joint q。Doob transform、Gaussian条件核与退火guidance均继承；不把不用已知退化operator/无需再训自动称新保证。

Eq13–14两固定endpoint/common forward-kernel差为alpha/sigma²*(coarse−fine)，VP low-noise增大。lambda→0本身不授最终approximation error受控或fine endpoint一致；本人的代数检查：lambda=sigma^a时加权h差尺度为sqrt(1−sigma²)*sigma^(a−2)*||coarse−fine||，a=1仍可发散，a≥2才有相应bounded/vanishing条件（这是固定点核下推断，不授完整ODE轨迹/score误差界）。论文实际使用image a5/6/7平均，video valid/invalid4/8，且§5.3 a1/3/5/7/9存在质量/忠实性两端反退，不采用一般三条lambda端点要求已充分的解释。理想endpoint保证不能移交给近似weighted sampler。

§5.1 FFHQ1000/256² FID/LPIPS、同pretrained模型；对手known-operator结果取既有DPS报告，SDEdit三个推荐t0均值vs三个a均值，不是每输入未知operator全搜索成本匹配。六/八指标优于SDEdit不授通用fine恢复；camera coarse由DepthPro/warp/nearest fill额外得，前后stage费用不能忽略。§5.4 Wan2.2仅qualitative兼容性，不证明其质量/预算对所有flow模型通用。未核hardware/precision/全runtime/concurrency/SLO、代码或复现。

拟 **1+1+2=4、已关闭/仅报告、Books0**：原文新增是单采样组件的coarse surrogate/noise-weight配置与受限任务证据，没有独立fine条件识别或新可比资源/质量可行界；h-transform与端点理论不重复计DesignDelta，系统跨界也不由image/video多任务抬分。理论资格反侧保留而不删准入潜力，不因费时/范围/Books覆盖倒推EX。若非作者实际认为该新增命题构成重要采样边界，应按真实delta重新裁定最低投入，再只比较必要owner差额；当前提案尚未独核/不正式计候选。
