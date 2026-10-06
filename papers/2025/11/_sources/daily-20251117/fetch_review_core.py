"""Only eleven Nov17 safety/counterevidence identities requested by root."""
from collect import fetch

IDS = '''12712 12497 12487 12381 12149 10899 10909 11601
11733 11313 11520'''.split()
for suffix in IDS:
    identity = '2511.' + suffix
    fetch('core-' + identity + 'v1.html', 'https://arxiv.org/html/' + identity + 'v1')
