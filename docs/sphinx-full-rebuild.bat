@echo off

echo Rebuilding source directory
RD /S /Q ".\source"
sphinx-apidoc -f --full --separate -o source ../src/DRSlib
copy /Y ".\source_base\*" ".\source\"
del ".\source\DRSlib.rst" 2> NUL
echo Done !

echo Rebuilding HTML build
del sphinx-build-errors.log 2> NUL
sphinx-build source build 2> sphinx-build-errors.log
echo Done ! See sphinx-build-errors.log file for errors/warnings.
echo Open build/index.html to see documentation

pause
