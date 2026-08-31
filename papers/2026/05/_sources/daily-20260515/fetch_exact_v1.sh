#!/bin/sh
set -eu
base_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
out_dir="$base_dir/arxiv-v1-html"
mkdir -p "$out_dir"
while IFS= read -r arxiv_id; do
  [ -n "$arxiv_id" ] || continue
  curl --fail --location --silent --show-error --retry 2 \
    "https://arxiv.org/html/${arxiv_id}v1" \
    --output "$out_dir/${arxiv_id}v1.html"
done < "$base_dir/candidate-ids.txt"
