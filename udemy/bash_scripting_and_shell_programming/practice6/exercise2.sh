#!/bin/bash

read -p "Please enter a file extension: " INPUT_EXT
read -p "Please enter a file prefix: " INPUT_PREFIX

if [ -z $INPUT_PREFIX ]  # if value has length zero
then
    INPUT_PREFIX=$(date +%Y%m%d)  # default prefix of yyyymmdd
else
    INPUT_PREFIX=${INPUT_PREFIX}-
fi

# echo $INPUT_EXT
# echo $INPUT_PREFIX

# when no files are match, skips loop entirely
shopt -s nullglob
for file in *.${INPUT_EXT}
do
    echo "Renaming $file to ${INPUT_PREFIX}${file}"
    mv $file ${INPUT_PREFIX}${file}
    
done