#!/bin/bash
HOST="google.com"
ping -c 1 $HOST
RETURN_CODE=$?

if [ "$RETURN_CODE" -eq "0" ]
then
    echo "$HOST reachable."
else
    echo "$HOST unreachable."
    exit 1
fi

exit 0

# ping -c 1 $HOST || echo "$HOST unreachable"