"""Print only named HTML sections; retain math alttext and primary raw files."""
from html.parser import HTMLParser
from pathlib import Path
import sys


class Sections(HTMLParser):
    def __init__(self, wanted):
        super().__init__()
        self.wanted = set(wanted)
        self.sections = []
        self.math_depth = 0
        self.output = []

    def active(self):
        return any(section in self.wanted for section in self.sections)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "section":
            self.sections.append(attrs.get("id", ""))
        if not self.active():
            return
        if tag == "math":
            self.math_depth += 1
            if self.math_depth == 1:
                self.output.append(" " + attrs.get("alttext", "[math without alttext]") + " ")
        if tag in ("p", "h1", "h2", "h3", "h4", "table", "tr", "figcaption", "li"):
            self.output.append("\n")

    def handle_endtag(self, tag):
        if self.active():
            if tag == "math":
                self.math_depth = max(0, self.math_depth - 1)
            if tag in ("p", "h1", "h2", "h3", "h4", "tr", "figcaption", "li"):
                self.output.append("\n")
        if tag == "section" and self.sections:
            self.sections.pop()

    def handle_data(self, value):
        if self.active() and not self.math_depth:
            self.output.append(value)


if __name__ == "__main__":
    parser = Sections(sys.argv[2:])
    parser.feed(Path(sys.argv[1]).read_text())
    print("\n".join(line.strip() for line in "".join(parser.output).splitlines() if line.strip()))
