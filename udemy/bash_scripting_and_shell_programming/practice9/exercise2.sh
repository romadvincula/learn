#!/bin/bash
LINE_NUM=1
read -p "How many lines of /etc/passwd would you like to see? " MAX_LINE

while read LINE
do
    echo "${LINE_NUM}: ${LINE}"

    if [ $LINE_NUM -ge $MAX_LINE ]
    then
        break
    fi

    ((LINE_NUM++))

done < /etc/passwd
