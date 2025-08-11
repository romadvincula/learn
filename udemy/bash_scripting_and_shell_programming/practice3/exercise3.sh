#!/bin/bash
cat /etc/shadow
STATUS_CODE=$?

if [ $STATUS_CODE -ne "0" ]
then
    echo "Command failed"
    exit 1
else
    echo "Command succeeded"
    exit 0

fi
