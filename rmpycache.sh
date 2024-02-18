#!/usr/bin/env bash

cachefolders=(
    src/__pycache__
    src/api/__pycache__
    src/frontend/__pycache__
    src/oobe/__pycache__
)

rm -r ${cachefolders[*]}