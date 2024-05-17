#!/bin/bash

pushd "$(dirname "${BASH_SOURCE[0]}")" || exit
source init/init.sh

target_image=%%project_name%%:latest
dockerfile=%%project_name%%.dockerfile

docker build "$@" -f $dockerfile --tag $target_image .

popd +0 || exit
