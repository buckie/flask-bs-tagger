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


if [ -d "./build" ]; then
    echo 'committing new frozen files'
    safe git add ./build/*
    safe git commit -sm "updated frozen files"
    
    echo 'begining push to github'
    safe git subtree push --prefix build origin master 
else
    barf 'Deploy failure, ./build does not exist'
fi

exit 0
    

