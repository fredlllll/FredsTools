#!/bin/bash

if [[ -z "$INIT_RAN" ]]; then
  echo "running init"

  #functions
  #functions end

  scriptsdir="$(dirname "${BASH_SOURCE[0]}")/scripts"
  pushd "$scriptsdir" || { echo "can't cd into $scriptsdir"; exit; }
  for file in *.sh; do
    if [ -f "$file" ]; then
      source "$file"
    fi
  done
  echo "finished init"
  popd +0 || { echo "can't popd"; exit; }
  INIT_RAN=true
else
  echo "init has already ran, skipping"
fi
