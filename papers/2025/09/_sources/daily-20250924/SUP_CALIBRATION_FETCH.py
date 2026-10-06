from SUP_CAPTURE import capture

for identifier in ["18588", "18638", "18796"]:
    capture("SUP_2509." + identifier + "v1.calibration.abs", "https://arxiv.org/abs/2509." + identifier + "v1", timeout=30)
    capture("SUP_2509." + identifier + ".calibration.current", "https://arxiv.org/abs/2509." + identifier, timeout=30)
for identifier in ["18588", "18796"]:
    capture("SUP_2509." + identifier + "v1.calibration.html", "https://arxiv.org/html/2509." + identifier + "v1", timeout=45)
