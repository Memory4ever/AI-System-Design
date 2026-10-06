import json
import sys
import urllib.request
import html
import re

url = sys.argv[1]
try:
    response = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=25)
    raw = response.read().decode('utf-8', 'replace')
    clean = re.sub(r'<(script|style)\b[^>]*>.*?</\1>', '', raw, flags=re.S | re.I)
    clean = html.unescape(re.sub(r'<[^>]+>', '\n', clean))
    text = '\n'.join(line.strip() for line in clean.splitlines() if line.strip())
    print(json.dumps({'url': url, 'status': response.status, 'text': text}, ensure_ascii=False))
except Exception as error:
    print(json.dumps({'url': url, 'error': str(error)}))
