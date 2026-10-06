"""Three additional exact-v1 cores explicitly requested by root."""
from collect import fetch

for suffix in ['12414', '11612', '12635']:
    identity = '2511.' + suffix
    fetch('core-' + identity + 'v1.html', 'https://arxiv.org/html/' + identity + 'v1')
