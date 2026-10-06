"""Bounded primary-source retrieval; outputs are raw evidence, not acceptance."""

import argparse
import datetime
import html.parser
import pathlib
import re
import urllib.parse
import urllib.request


class Element:
    def __init__(self, tag, attrs=None):
        self.tag = tag
        self.attrs = dict(attrs or [])
        self.children = []

    def text(self):
        return " ".join(
            child.text() if isinstance(child, Element) else child
            for child in self.children
        ).strip()

    def find(self, predicate):
        result = [self] if predicate(self) else []
        for child in self.children:
            if isinstance(child, Element):
                result.extend(child.find(predicate))
        return result


class Parser(html.parser.HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Element("root")
        self.stack = [self.root]

    def handle_starttag(self, tag, attrs):
        node = Element(tag, attrs)
        self.stack[-1].children.append(node)
        if tag not in {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}:
            self.stack.append(node)

    def handle_endtag(self, tag):
        for index in range(len(self.stack) - 1, 0, -1):
            if self.stack[index].tag == tag:
                del self.stack[index:]
                break

    def handle_data(self, data):
        if data.strip() and self.stack[-1].tag not in {"script", "style"}:
            self.stack[-1].children.append(" ".join(data.split()))


def get(url):
    request = urllib.request.Request(url, headers={"User-Agent": "AI-System-Design research (bounded historical retrieval)"})
    with urllib.request.urlopen(request, timeout=90) as response:
        source = response.read().decode("utf-8", errors="replace")
    parser = Parser()
    parser.feed(source)
    return parser.root


def cls(node, name):
    return name in node.attrs.get("class", "").split()


def search(args):
    output = ["# arXiv 原始主题检索", "", "执行时间：" + datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8))).isoformat(), "", "日期字段是 submitted_date_first，仅用于发现；不证明首次公开时间。检索摘要可能为当前版，拟采用须读精确版本。", ""]
    params = {"advanced": "", "terms-0-operator": "AND", "terms-0-term": args.term, "terms-0-field": args.field, "date-filter_by": "date_range", "date-from_date": args.start, "date-to_date": args.end, "date-date_type": "submitted_date_first", "abstracts": "show", "size": "200", "order": "submitted_date"}
    if args.context:
        params.update({"terms-1-operator": "AND", "terms-1-term": args.context, "terms-1-field": "abstract"})
    start = 0
    identities = []
    while True:
        params["start"] = str(start)
        url = "https://arxiv.org/search/advanced?" + urllib.parse.urlencode(params)
        root = get(url)
        headings = root.find(lambda n: n.tag == "h1")
        output.extend(["## 页面 start=" + str(start), "", "入口：" + url, "", "响应标题：" + " | ".join(n.text() for n in headings), ""])
        rows = root.find(lambda n: n.tag == "li" and cls(n, "arxiv-result"))
        for row in rows:
            links = row.find(lambda n: n.tag == "a" and "/abs/" in n.attrs.get("href", ""))
            title = row.find(lambda n: cls(n, "title"))
            abstract = row.find(lambda n: n.attrs.get("id", "").endswith("-abstract-full"))
            small = row.find(lambda n: n.tag == "p" and cls(n, "is-size-7"))
            identity = links[0].text() if links else "UNRESOLVED"
            identities.append(identity)
            if args.print_abstracts:
                print(identity + " " + (title[0].text() if title else ""))
                print(abstract[0].text() if abstract else "ABSTRACT_NOT_FOUND")
            output.extend(["### " + identity + " " + (title[0].text() if title else ""), "", links[0].attrs["href"] if links else "", "", "日期/说明：" + " | ".join(n.text() for n in small), ""])
        nxt = root.find(lambda n: n.tag == "a" and cls(n, "pagination-next") and n.attrs.get("href"))
        if not nxt:
            output.extend(["停止依据：页面无有效 Next 链接；实际页数=" + str(start // 200 + 1) + "；原始行数=" + str(len(identities)), ""])
            break
        start += 200
    pathlib.Path(args.output).write_text("\n".join(output), encoding="utf-8")
    print("output=" + args.output + " raw_rows=" + str(len(identities)))
    for line in output:
        if line.startswith("### ") or line.startswith("响应标题"):
            print(line)


def page(args):
    root = get(args.url)
    main = root.find(lambda n: n.tag in {"main", "article"})
    content = (main[0] if main else root).text()
    print(content)
    if args.output:
        pathlib.Path(args.output).write_text("# 原始页面文本\n\n入口：" + args.url + "\n\n实际抓取：" + datetime.datetime.now(datetime.timezone.utc).isoformat() + "\n\n" + content + "\n", encoding="utf-8")


def listing(args):
    root = get(args.url)
    titles = root.find(lambda n: cls(n, "list-title"))
    ids = root.find(lambda n: n.tag == "a" and n.attrs.get("title") == "Abstract")
    headers = root.find(lambda n: n.tag in {"h2", "h3"} or cls(n, "paging"))
    print(" | ".join(n.text() for n in headers))
    for identity, title in zip(ids, titles):
        paper = identity.text().replace("arXiv:", "")
        if args.low <= paper <= args.high:
            print(paper + " " + title.text())


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    commands = parser.add_subparsers(dest="mode", required=True)
    p = commands.add_parser("search")
    p.add_argument("--term", required=True)
    p.add_argument("--field", default="abstract")
    p.add_argument("--context")
    p.add_argument("--print-abstracts", action="store_true")
    p.add_argument("--start", required=True)
    p.add_argument("--end", required=True)
    p.add_argument("--output", required=True)
    p = commands.add_parser("page")
    p.add_argument("--url", required=True)
    p.add_argument("--output")
    p = commands.add_parser("listing")
    p.add_argument("--url", required=True)
    p.add_argument("--low", required=True)
    p.add_argument("--high", required=True)
    args = parser.parse_args()
    {"search": search, "page": page, "listing": listing}[args.mode](args)
