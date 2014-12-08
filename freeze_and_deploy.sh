#!/bin/sh

# The classic -- three finger claw technique
shout() { echo "$0: $*" >&2; }
barf() { shout "$*"; exit 111; }
safe() { "$@" || barf "cannot $*"; }

if [ -r "./freeze.py" ]; then
    echo 'Begining Freezing Process'
    safe python freeze.py 
else
    barf 'freeze.py is missing!'
fi


if [ -d "./gh-pages" ]; then
    echo 'committing new frozen files'
    safe git add ./gh-pages/*
    safe git commit -sm "updated frozen files"
    
    echo 'begining push to github'
    safe git subtree push --prefix gh-pages origin master 
else
    barf 'Deploy failure, ./gh-pages does not exist'
fi

exit 0
    

