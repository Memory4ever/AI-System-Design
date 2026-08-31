#!/bin/zsh
set -u
base="${0:A:h}"
mkdir -p "$base/exact-v1-html"
mkdir -p "$base/exact-v1-pdf" "$base/exact-v1-pdf-text"
pids=()
while IFS= read -r aid; do
  [[ -z "$aid" ]] && continue
  (
    out="$base/exact-v1-html/${aid}v1.html"
    tmp="$out.part"
    if [[ -s "$out" ]] && grep -qi '</html>' "$out"; then
      exit 0
    fi
    if curl -L --fail --silent --show-error --max-time 90 "https://arxiv.org/html/${aid}v1" -o "$tmp" && grep -qi '</html>' "$tmp"; then
      mv "$tmp" "$out"
      exit 0
    fi
    rm -f "$tmp"
    pdf="$base/exact-v1-pdf/${aid}v1.pdf"
    pdf_tmp="$pdf.part"
    if curl -L --fail --silent --show-error --max-time 120 "https://arxiv.org/pdf/${aid}v1" -o "$pdf_tmp"; then
      mv "$pdf_tmp" "$pdf"
      pdftotext -layout "$pdf" "$base/exact-v1-pdf-text/${aid}v1.txt" 2>/dev/null || true
    else
      rm -f "$pdf_tmp"
    fi
  ) &
  pids+=($!)
  if (( ${#pids[@]} >= 8 )); then
    for pid in $pids; do wait $pid || true; done
    pids=()
  fi
done < "$base/candidate-ids.txt"
for pid in $pids; do wait $pid || true; done
