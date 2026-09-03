#!/usr/bin/env bash
set -euo pipefail

repo_root="/Users/apple/Documents/Work/PycharmProject/AI-System-Design"

fetch_one() {
  local month="$1"
  local arxiv_id="$2"
  local out_dir="${repo_root}/papers/2026/${month}/_sources/arxiv-owner-replay-20260903/exact-v1"
  mkdir -p "${out_dir}"
  for route in abs; do
    local output="${out_dir}/${arxiv_id}v1.${route}.html"
    if [[ -s "${output}" ]]; then
      continue
    fi
    if ! curl --fail --location --silent --show-error \
      --retry 2 --retry-all-errors --retry-delay 2 --max-time 60 \
      --output "${output}.tmp" "https://arxiv.org/${route}/${arxiv_id}v1"; then
      printf '%s\t%s\t%s\n' "${month}" "${arxiv_id}" "${route}" >&2
      continue
    fi
    mv "${output}.tmp" "${output}"
  done
  local html_output="${out_dir}/${arxiv_id}v1.html.html"
  local pdf_output="${out_dir}/${arxiv_id}v1.pdf"
  if [[ ! -s "${html_output}" && ! -s "${pdf_output}" ]]; then
    if curl --fail --location --silent --show-error \
      --continue-at - --retry 3 --retry-all-errors --retry-delay 2 --max-time 180 \
      --output "${html_output}.tmp" "https://arxiv.org/html/${arxiv_id}v1"; then
      mv "${html_output}.tmp" "${html_output}"
    elif curl --fail --location --silent --show-error \
      --continue-at - --retry 3 --retry-all-errors --retry-delay 2 --max-time 180 \
      --output "${pdf_output}.tmp" "https://export.arxiv.org/pdf/${arxiv_id}v1"; then
      mv "${pdf_output}.tmp" "${pdf_output}"
    else
      printf '%s\t%s\t%s\n' "${month}" "${arxiv_id}" "full_text" >&2
    fi
  fi
}

export -f fetch_one
export repo_root

python3 - <<'PY' | xargs -n 2 -P 4 bash -c 'fetch_one "$0" "$1"'
import json
from pathlib import Path

root = Path("/Users/apple/Documents/Work/PycharmProject/AI-System-Design")
for month in ("04", "05"):
    summary = json.loads((root / f"papers/2026/{month}/_sources/arxiv-owner-replay-20260903/month-reconciliation.json").read_text())
    for day in summary["days"]:
        receipt = json.loads((root / day["receipt"]).read_text())
        for row in receipt["identities"]:
            if row["screening_status"] == "retained" and not row.get("prior_screening_ledger"):
                print(month, row["arxiv_id"])
PY
