#!/bin/bash

if [[ -z "$INIT_RAN" ]]; then
  echo "running init"

  #functions
  clone_update_repo() {
    local repo_name=$1
    local repo_url=$2
    local branch_or_commit="$(cat "$CONFIGDIR"/branches/"$repo_name")"
    pushd "$CONFIGDIR"/repos
    if [ ! -d ./"$repo_name" ]; then
      (
        git clone --no-checkout --recurse-submodules "$repo_url" "$repo_name"
      )
    fi
    pushd "$repo_name"
    git fetch
    git checkout "$branch_or_commit"
    git pull origin "$branch_or_commit"
    git submodule update --init --recursive
    popd
    popd
  }
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
