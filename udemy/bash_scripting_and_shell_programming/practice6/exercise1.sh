#!/bin/bash

# when no files are match, skips loop entirely
shopt -s nullglob

for file in *.jpg
do
    echo "Renaming $file to $(date +%Y%m%d)${file}"
    mv $file $(date +%Y%m%d)${file}
    
done