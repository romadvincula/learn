#!/bin/bash

function file_count() {
    local files=$(ls .)
    local num_files=$(ls . | wc -w)
    echo $num_files

}

file_count