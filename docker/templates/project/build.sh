#!/bin/bash

CONFIGURATION="${1:-prod}"
CONFIGDIR=$(realpath ./configurations/"$CONFIGURATION")

pushd "$(dirname "${BASH_SOURCE[0]}")" || exit
. init/init.sh

target_image=%%project_name%%:latest
dockerfile=%%project_name%%.dockerfile

docker build "$@" -f $dockerfile --tag $target_image --build-arg="CONFIGURATION=$CONFIGURATION" . || exit

popd +0 || exit
