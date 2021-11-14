#! /bin/bash

echo Cleaning ./build ./source ./sphinx-build-errors.log

find ./build -mindepth 1 -delete 2>/dev/null
rmdir ./build

find ./source -mindepth 1 -delete 2>/dev/null
rmdir ./source

rm sphinx-build-errors.log 2>/dev/null