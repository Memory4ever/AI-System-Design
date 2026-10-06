"""Read bounded official commit-list payloads without treating commits as public events."""

import datetime
import html.parser
import json
import pathlib
import sys
import urllib.parse
import urllib.request


class EmbeddedData(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.active = False
        self.parts = []
        self.payload = None

    def handle_starttag(self, tag, attrs):
        if tag == "script" and dict(attrs).get("data-target") == "react-app.embeddedData":
            self.active = True

    def handle_data(self, data):
        if self.active:
            self.parts.append(data)

    def handle_endtag(self, tag):
        if tag == "script" and self.active:
            self.payload = json.loads("".join(self.parts))
            self.active = False


start, end, output, *repos = sys.argv[1:]
lines = ["# 官方 repo 精确窗口原始记录", "", datetime.datetime.now(datetime.timezone.utc).isoformat(), "", "committer/author 时间不授 first-public；只检查指定 route，无月级扩扫。", ""]
for repo in repos:
    url = "https://github.com/" + repo + "/commits/main/?" + urllib.parse.urlencode({"since": start, "until": end})
    lines.extend(["## " + repo, "", url, ""])
    try:
        source = urllib.request.urlopen(url, timeout=45).read().decode()
        parser = EmbeddedData()
        parser.feed(source)
        route = parser.payload["payload"]["commitsRefRoute"]
        lines.extend(["filters: " + json.dumps(route["filters"], ensure_ascii=False), ""])
        for group in route["commitGroups"]:
            lines.append("group: " + json.dumps(group, ensure_ascii=False))
        lines.append("raw groups=" + str(len(route["commitGroups"])))
    except Exception as error:
        lines.append(type(error).__name__ + ": " + str(error))
    lines.append("")
pathlib.Path(output).write_text("\n".join(lines), encoding="utf-8")
print("\n".join(lines))
