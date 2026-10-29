from html.parser import HTMLParser
from pathlib import Path
import sys

selected_section = next((x.split('=', 1)[1] for x in sys.argv if x.startswith('--section=')), None)

class Text(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []
        self.skip = 0
        self.abstract = []
        self.in_abstract = False
        self.title = ''
        self.section_depth = 0
        self.current_section = ''
        self.heading = None
        self.headings = []

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if tag == 'section':
            self.current_section = values.get('id', '')
            if self.section_depth:
                self.section_depth += 1
            elif values.get('id') == selected_section:
                self.section_depth = 1
        if tag in ('h2', 'h3'):
            self.heading = [self.current_section, []]
        if tag == 'meta' and values.get('name') == 'citation_title':
            self.title = values.get('content', '')
        if tag == 'blockquote' and 'abstract' in values.get('class', ''):
            self.in_abstract = True
        if tag in ('script', 'style'):
            self.skip += 1
        if tag in ('p', 'div', 'section', 'h1', 'h2', 'h3', 'h4', 'li', 'tr', 'blockquote'):
            self.parts.append('\n')

    def handle_endtag(self, tag):
        if tag in ('h2', 'h3') and self.heading:
            self.headings.append((self.heading[0], ''.join(self.heading[1])))
            self.heading = None
        if tag == 'section' and self.section_depth:
            self.section_depth -= 1
        if tag == 'blockquote':
            self.in_abstract = False
        if tag in ('script', 'style'):
            self.skip -= 1
        if tag in ('p', 'div', 'section', 'h1', 'h2', 'h3', 'h4', 'li', 'tr', 'blockquote'):
            self.parts.append('\n')

    def handle_data(self, data):
        if self.heading:
            self.heading[1].append(data)
        if not self.skip and (not selected_section or self.section_depth):
            self.parts.append(data)
            if self.in_abstract:
                self.abstract.append(data)


abstract_only = '--abstract' in sys.argv
for filename in [x for x in sys.argv[1:] if not x.startswith('--')]:
    parser = Text()
    parser.feed(Path(filename).read_text())
    print('\nFILE', filename)
    if '--outline' in sys.argv:
        for section_id, title in parser.headings:
            print(section_id, ' '.join(title.split()))
        continue
    if abstract_only:
        print(parser.title)
        print(' '.join(''.join(parser.abstract).split()))
        continue
    for line in ''.join(parser.parts).splitlines():
        line = ' '.join(line.split())
        if line:
            print(line)
