from SUP_CAPTURE import capture

for identifier in ["18316", "18980", "19090", "19096"]:
    capture("SUP_2509." + identifier + "v1.reopen.abs", "https://arxiv.org/abs/2509." + identifier + "v1", timeout=30)
for identifier in ["18316", "19090", "19096"]:
    capture("SUP_2509." + identifier + "v1.reopen.html", "https://arxiv.org/html/2509." + identifier + "v1", timeout=45)
