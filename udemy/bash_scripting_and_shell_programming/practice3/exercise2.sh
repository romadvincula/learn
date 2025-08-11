#!/bin/bash
USER_INPUT=$1

if [ -f $USER_INPUT ]  # file exists and is a regular file
then
    echo "$USER_INPUT is a regular file."
    exit 0
elif [ -d $USER_INPUT ]  # file exists and is a directory
then
    echo "$USER_INPUT is a directory."
    exit 1
elif [ -e $USER_INPUT ]  # file exists
then
    echo "$USER_INPUT exists."$?
    exit 2
else
    echo "$USER_INPUT does not exist."
    exit 3

fi