#!/usr/bin/env bash
set -o nounset
container=$1
docker exec -it "$container" /bin/bash
