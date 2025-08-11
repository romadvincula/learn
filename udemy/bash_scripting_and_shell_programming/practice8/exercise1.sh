#!/bin/bash
# logger -s -p user.info "Hello, random number is $RANDOM"

log_random_number() {
    local MESSAGES=$@
    for message in $MESSAGES
    do 
        logger -s -i -t randomly -p user.info "Hello, random number is $message"

    done
}

log_random_number $RANDOM $RANDOM $RANDOM