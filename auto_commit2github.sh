#!/bin/sh
##########
# clear cache file.
rm *~
git add -A
git commit -m "shell autocommit"
git push
