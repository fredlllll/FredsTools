#!/bin/bash

if [[ -z "$INIT_RAN" ]]; then
  echo "running init"
  scriptsdir="$(dirname "${BASH_SOURCE[0]}")/scripts"
  pushd "$scriptsdir" || exit
  for file in *.sh; do
    if [ -f "$file" ]; then
      source "$file"
    fi
  done
  echo "finished init"
  popd +0 || exit
  INIT_RAN=true
else
  echo "init has already ran, skipping"
fi
