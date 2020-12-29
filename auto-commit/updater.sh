#!/bin/bash

FILE=./numbers
if test -f "$FILE"; then
	echo "$FILE exists"
else
	echo "$FILE does not exist"
	touch file

echo $((1 + $RANDOM % 1000000)) >> file
git add file
git commit -m "Scheduled commit"
git push

