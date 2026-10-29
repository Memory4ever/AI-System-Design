from SUP_CAPTURE import capture

# Reopened ambiguous titles only; this is not the remaining discovery inventory.
for identity in "13539 13621 13706 13892 13591 13736 13827 13857 13861".split():
    capture("SUP_BOUNDARY_V1_" + identity,
            "https://arxiv.org/abs/2509." + identity + "v1")
    capture("SUP_BOUNDARY_CURRENT_" + identity,
            "https://arxiv.org/abs/2509." + identity)
for identity in "13591 13736 13857".split():
    capture("SUP_BOUNDARY_CORE_" + identity,
            "https://arxiv.org/html/2509." + identity + "v1")
