#! /bin/bash

sh ./sphinx-clean.sh 2>/dev/null

echo Rebuilding source directory
sphinx-apidoc -f --full --separate -o source ../src/DRSlib
find ./source_base -type f | xargs cp -t ./source
rm ./source/DRSlib.rst
echo Done !

echo Rebuilding HTML build
sphinx-build source build 2> sphinx-build-errors.log
echo Done ! See sphinx-build-errors.log file for errors/warnings.
echo Open build/index.html to see documentation
