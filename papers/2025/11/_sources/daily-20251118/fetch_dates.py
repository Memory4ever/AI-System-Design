"""Only Nov18 potential identities require original date metadata recovery."""
from collect import fetch

IDS = '''2511.11518 2511.11505 2511.11500 2511.11315 2511.11018
2511.11007 2511.10881 2511.10819 2511.10811 2511.11526
2511.11520 2511.11502 2511.11313 2511.11298 2511.11011
2511.10946 2511.11332 2511.11248 2601.08833 2511.10909'''.split()
for identity in IDS:
    fetch('datacite-' + identity + '.json', 'https://api.datacite.org/dois/10.48550/arXiv.' + identity)
