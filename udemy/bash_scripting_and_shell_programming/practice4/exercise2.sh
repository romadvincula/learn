#!/bin/bash

function file_count() {
    local lookup_dir=$1

    if [ -d $lookup_dir ]  # check if directory exists
    then
        # count files in dir (including dirs)
        local num_files=$(ls $lookup_dir | wc -w) 
    else
        echo "$lookup_dir does not exist."
        return 1
    fi

    echo "${lookup_dir}:"
    echo $num_files
}

file_count /etc
if [ $? -eq 0 ]
then 
    file_count /var
fi
if [ $? -eq 0 ]
then
    file_count /usr/bin
fi