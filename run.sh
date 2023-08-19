#!/bin/bash

set -e
deployed=0

if [ $deployed -eq "1" ]; then
    echo "Checking for updates"
fi

docker run --rm -t --mount type=bind,source="$(pwd)/",target=/app diginomad:autoagent $@
