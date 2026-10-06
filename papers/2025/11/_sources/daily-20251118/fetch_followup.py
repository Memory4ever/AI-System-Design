"""Finite Nov18 exact-version follow-up; prior-day responses are not used."""
from collect import fetch

IDS = '''2511.11518 2511.11505 2511.11500 2511.11472 2511.16688
2511.11334 2511.11315 2511.11018 2511.11007 2511.10881
2511.10876 2511.10819 2511.10811 2511.11526 2511.11520
2511.11510 2511.11502 2511.11313 2511.11298 2511.11212
2511.11011 2511.10946 2511.11445 2511.11332 2511.11248
2511.11111 2601.08833 2511.10909 2511.10774'''.split()

for identity in IDS:
    fetch('abs-' + identity + 'v1.html', 'https://arxiv.org/abs/' + identity + 'v1')
fetch('deepmind-sima.html', 'https://deepmind.google/blog/sima-2-an-agent-that-plays-reasons-and-learns-with-you-in-virtual-3d-worlds/')
fetch('google-gemini3.html', 'https://blog.google/products/gemini/gemini-3/')
