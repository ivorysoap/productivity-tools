#!/bin/bash

FILE=./file
if test -f "$FILE"; then
        echo "$FILE exists"
else
        echo "$FILE does not exist"
        touch file
fi

message="$((1 + $RANDOM % 1000000)) | $(date)"  # Random number and current dat>
echo $message >> file
git add file
git commit -m "Scheduled commit | $(date)"
git push

exit 1
