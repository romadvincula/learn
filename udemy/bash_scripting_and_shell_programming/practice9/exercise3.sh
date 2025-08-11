#!/bin/bash

while true
do
    echo "1. Show Disk Usage. "
    echo "2. Show system uptime."
    echo "3. Show the users logged into the system."
    read -p "What would you like to do? " COMMAND
    echo ""
    case "$COMMAND" in
        1)
            df -h
            ;;
        2)
            uptime
            ;;
        3)
            who
            ;;
        q)
            break
            ;;
        *)
            echo "Invalid option."
            ;;
    esac
    echo ""  # print blank line after iteration
done