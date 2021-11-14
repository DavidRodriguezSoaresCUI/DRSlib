@echo off

echo Cleaning ./build ./source ./sphinx-build-errors.log
RD /S /Q ".\build"
RD /S /Q ".\source"
del sphinx-build-errors.log 2> NUL