from SUP_CAPTURE import capture

for identifier in ["17993", "18015", "18234", "18626", "19120"]:
    capture("SUP_2509." + identifier + "v1.html", "https://arxiv.org/html/2509." + identifier + "v1", timeout=45)
for identifier in ["18015", "18234"]:
    capture("SUP_2509." + identifier + "v1.abs", "https://arxiv.org/abs/2509." + identifier + "v1")
    capture("SUP_2509." + identifier + ".current", "https://arxiv.org/abs/2509." + identifier)
