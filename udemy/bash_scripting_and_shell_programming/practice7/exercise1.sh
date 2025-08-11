#!/bin/bash
# must have /tmp/sleepwalkingserver file

COMMAND=$1

case "$COMMAND" in
    start)
        echo "start"
        /tmp/sleepwalkingserver &
        ;;
    stop)
        echo "stop"
        kill $(cat /tmp/sleepwalkingserver.pid)
        ;;
    *)
        echo "Usage sleepwalking start|stop"
        exit 1
        ;;
esac