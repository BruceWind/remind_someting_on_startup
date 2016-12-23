#!/bin/sh
##########
# if you clone in  ssh.
#############

# clear cache file.
rm *~
git add -A
git commit -m "shell autocommit"
git push
