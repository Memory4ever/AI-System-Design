#!/usr/bin/env bash
set -euo pipefail

repo_root="/Users/apple/Documents/Work/PycharmProject/AI-System-Design"
categories=(cs.AI cs.CL cs.LG cs.DC cs.IR stat.ML cs.CV cs.RO cs.SE cs.CR cs.AR cs.PF cs.OS cs.PL cs.MA cs.DB cs.NI eess.AS cs.SD)

fetch_one() {
  local month="$1"
  local category="$2"
  local out_dir="${repo_root}/papers/2026/${month}/_sources/arxiv-owner-replay-20260903/monthly-membership"
  mkdir -p "${out_dir}"
  local output="${out_dir}/${category}.html"
  if [[ -s "${output}" ]]; then
    return
  fi
  curl --fail --location --silent --show-error \
    --retry 6 --retry-all-errors --retry-delay 3 --max-time 240 \
    --output "${output}.tmp" \
    "https://arxiv.org/list/${category}/2026-${month}?skip=0&show=2000"
  mv "${output}.tmp" "${output}"
}

export -f fetch_one
export repo_root

for month in 04 05; do
  for category in "${categories[@]}"; do
    printf '%s %s\n' "${month}" "${category}"
  done
done | xargs -n 2 -P 2 bash -c 'fetch_one "$0" "$1"'
