import sys

from SUP_CAPTURE import capture


if __name__ == "__main__":
    mode = sys.argv[1]
    for identifier in sys.argv[2:]:
        path = "abs" if mode == "abs" else "html"
        capture("SUP_" + identifier + "v1." + mode,
                "https://arxiv.org/" + path + "/" + identifier + "v1")
