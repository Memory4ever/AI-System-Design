"""Preserve reader-captured exact bytes without another network request."""
import datetime
import hashlib
import json
from pathlib import Path
import sys

from REPAIR_dates_20261021 import BASE, save


SOURCES = {
    "09001": (125, "4ed3139ccd299a3c2370472f8df505f404db9fd2ec526748c4cfaa13599a3a46"),
    "09043": (126, "8ab726dcdfce93d123b9a556b2ed45fae0a62ee9b03b0bca4ba7c56f4e8b495d"),
    "09284": (115, "b0ff8619eabba3b0764c4fc560d81e2df076705a6252cd42e4608664a9cbe6a0"),
    "09286": (119, "3c47f741cd3a808aa25ff62525fe27928e60d1bbd9030bf86617dfec6cbee5dd"),
    "09291": (141, "6f170606dac7d860e1832dda323ed9978d2bb61c51ffb1a9b66e6dd89b012368"),
    "09311": (120, "671b6b49e3951f480c18a96a9891e65f337a03ab8f177fe8caab6b1502180f5b"),
    "09310": (149, "80ebcc566360605ae53c5cbc7c216a4ec79019d6114e7aeffddbe518cdf1c4f6"),
    "09318": (121, "27d7091b5e4257347c11e82311a5c3bc90e0172447d1c02c7ac71c6ce807a103"),
    "09321": (123, "96b39842f8769f580f9ee9852cf69aea2342075e6167a868d518668666e915eb"),
    "09332": (136, "38f343ae81502d7718929ff413615231fc804e6333a5948563c288fec3b32ce0"),
    "09337": (154, "25136d0d354f51831c9e5de85dfcd6e5f954dae0bb6ea6e99700777bd5a9bae5"),
    "09372": (160, "12ecaed5e3bda204ef3f31a109d1fe4e3443f8b046398989ddadbd0934e04665"),
    "09360": (144, "dcec61471a772744c6017bf0efe2754465f886331ab2b69ba5c3eb9c5f8631f5"),
    "09396": (137, "4ef62fab84a3c21322c4431a5ebb19c42be271a97c0fe35ebe43871546bc52c7"),
    "09420": (161, "e5d20780c90ad4ae04adca48f4eb02568f7fd3d83f7b22fa61eadaeec5b7477c"),
    "09424": (163, "d4b0309cfe4f42289388c1572f9b70386d89b80e9d0bed5e383b74b1ca5efe9b"),
    "09438": (165, "10e0f4ca4fea57783ce94176ce6a372794b6579a77423e17bfac5d92b50a8624"),
    "09482": (159, "776fb07b4510f1f8c0ce200b633d3187e502d56c2bf2c346f57bbdc947cc3360"),
    "09498": (172, "0df4a57995b16526936437c07d9ce9c4aba135e857404984fee8d895f9623cc1"),
    "09505": (167, "d164107408a543d471e07b4ab5c7b1b1a5934e5c9a4e15d4159e92eef5bdbe31"),
    "09525": (168, "3fd6dad9aac66f8103c830a8a14cfa59b159b3440136f63e349a9c44128f1d02"),
    "09541": (177, "ea865ae0f2945cc6296701a521d8e15ad06e885bb31ae157fdbe151298526923"),
    "09547": (178, "42d1644696c8489f1d0fccf1d52f7902bef93d459ec99be5f24faf862f61e0c3"),
    "09560": (130, "5c7591c140bd85d3d69364aadc569fcf9e621d03ff6bbe81da7d2c737a1d30c7"),
    "09614": (173, "0a180c6bc7622019858368c285dc71f284b0f85e2c682144f12559f5ffaa98e4"),
}
for suffix in sys.argv[1:] or SOURCES:
    section, expected = SOURCES[suffix]
    ending = "v1-retry.html" if suffix == "09001" else "v1.html"
    origin = Path("/tmp/zeno-2509." + suffix + ending)
    body = origin.read_bytes()
    assert hashlib.sha256(body).hexdigest() == expected
    target = BASE / ("REPAIR_reader-html-2509." + suffix + "v1_20261021.raw")
    if target.exists():
        assert target.read_bytes() == body
    else:
        save(target, body)
        record = {"operation": "preserve_reader_capture_no_GET", "preserved_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(), "origin_path": str(origin), "original_url": "https://arxiv.org/html/2509." + suffix + "v1", "original_GET_status_reported_by_reader": 200, "reader": "Zeno", "reader_section": section, "bytes": len(body), "sha256": expected}
        save(target.with_suffix(".provenance.json"), (json.dumps(record, indent=2) + "\n").encode())
    print(target.name, len(body), expected)
