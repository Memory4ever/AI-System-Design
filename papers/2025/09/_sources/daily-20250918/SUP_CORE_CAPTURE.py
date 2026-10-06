from SUP_CAPTURE import ROOT, capture

# Only identities whose full abstract left admission dependent on a method fact.
identities = "13557 13588 13712 13735 13762 13773 13603 13957 14030 14033 14063 14104 13279 13634".split()
for identity in identities:
    name = "SUP_CORE_" + identity
    if not (ROOT / (name + ".raw")).exists():
        capture(name, "https://arxiv.org/html/2509." + identity + "v1")
name = "SUP_CORE_AQUA"
if not (ROOT / (name + ".raw")).exists():
    capture(name, "https://arxiv.org/html/2510.21722v1")
