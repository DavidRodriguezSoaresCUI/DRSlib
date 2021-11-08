#! /bin/bash
echo Rebuilding source directory
rm -r -f ./source/* 2> /dev/null
rmdir ./source 2> /dev/null
sphinx-apidoc -f --full --separate -o source ../src/DRSlib
find ./source_base -type f | xargs cp -t ./source
rm ./source/DRSlib.rst
echo Done !

echo Rebuilding HTML build
rm sphinx-build-errors.log
sphinx-build source build 2> sphinx-build-errors.log
echo Done ! See sphinx-build-errors.log file for errors/warnings.
echo Open build/index.html to see documentation
