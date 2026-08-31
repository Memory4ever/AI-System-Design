#!/usr/bin/env bash
set -euo pipefail

dest="papers/2026/05/_sources/daily-20260530/exact-v1-html"
mkdir -p "$dest"
for id in \
  2606.00160 2606.00186 2606.00257 2606.00284 2606.00299 2606.00301 \
  2606.00308 2606.00310 2606.00329 2606.00357 2606.00371 2606.00382 \
  2606.00390 2606.00392 2606.00400 2606.00414 2606.07595 2606.07612 \
  2606.19357 2606.24893 2606.28337 2605.30741 2605.30748 2605.30789 \
  2605.30790 2605.31429 2605.31557 2605.31598
do
  file="$dest/${id}v1.html"
  if [[ -s "$file" || -s "$dest/${id}v1.pdf" ]]; then
    continue
  fi
  if ! curl --silent --show-error --fail --location --max-time 60 --retry 2 --retry-delay 2 \
    "https://arxiv.org/html/${id}v1" --output "$file"; then
    rm -f "$file"
    curl --silent --show-error --fail --location --max-time 60 --retry 2 --retry-delay 2 \
      "https://arxiv.org/pdf/${id}v1" --output "$dest/${id}v1.pdf"
  fi
done
