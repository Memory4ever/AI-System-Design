from SUP_CAPTURE import capture

for identifier in ["17978", "18005", "18053", "18058", "18415", "18917", "19087", "21379", "22703"]:
    capture("SUP_2509." + identifier + "v1.html", "https://arxiv.org/html/2509." + identifier + "v1", timeout=45)
