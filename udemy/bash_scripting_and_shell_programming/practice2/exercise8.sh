#!/bin/bash
USER_INPUTS=$@

for USER_INPUT in $USER_INPUTS
do
    if [ -f $USER_INPUT ]  # file exists and is a regular file
    then
        echo "$USER_INPUT is a regular file."
    elif [ -d $USER_INPUT ]  # file exists and is a directory
    then
        echo "$USER_INPUT is a directory."
    elif [ -e $USER_INPUT ]  # file exists
    then
        echo "$USER_INPUT exists."
    else
        echo "$USER_INPUT does not exist."

    fi
done

# example to create a symlink
# ln exercise1.sh ../exercise1.sh