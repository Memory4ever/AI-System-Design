#!/usr/bin/env bash
set -u

packet_dir="$(cd "$(dirname "$0")" && pwd)"
mkdir -p "$packet_dir/exact-v1-html"

fetch_one() {
  paper_id="$1"
  target="$packet_dir/exact-v1-html/${paper_id}.html"
  if [ -s "$target" ] && [ "$(wc -c < "$target")" -gt 1000 ]; then
    printf '%s\t%s\n' "$paper_id" cached
    return 0
  fi
  if curl -L --fail --max-time 90 --retry 2 --retry-delay 2 -sS "https://arxiv.org/html/${paper_id}v1" -o "$target"; then
    printf '%s\t%s\n' "$paper_id" html
  else
    printf '%s\t%s\n' "$paper_id" failed
    return 0
  fi
}
export packet_dir
export -f fetch_one
xargs -n 1 -P 8 bash -c 'fetch_one "$1"' _ < "$packet_dir/candidate-ids-author.txt"
