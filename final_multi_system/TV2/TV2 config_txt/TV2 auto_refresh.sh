#!/bin/bash

# Auto-refresh script - runs refresh_config.sh every 30 minutes
# Usage: ./auto_refresh.sh [start|stop|status]

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REFRESH_SCRIPT="$SCRIPT_DIR/refresh_config.sh"
PID_FILE="$SCRIPT_DIR/.auto_refresh.pid"
LOG_FILE="$SCRIPT_DIR/auto_refresh.log"

start_refresh() {
    if [ -f "$PID_FILE" ] && kill -0 "$(cat "$PID_FILE")" 2>/dev/null; then
        echo "Auto-refresh is already running (PID: $(cat "$PID_FILE"))"
        return 1
    fi
    
    echo "Starting auto-refresh (every 30 minutes)..."
    echo "$(date): Auto-refresh started" >> "$LOG_FILE"
    
    # Start background loop
    (
        while true; do
            sleep 1800  # 30 minutes = 1800 seconds
            if [ -f "$REFRESH_SCRIPT" ]; then
                echo "$(date): Running scheduled refresh..." >> "$LOG_FILE"
                "$REFRESH_SCRIPT" >> "$LOG_FILE" 2>&1
            fi
        done
    ) &
    
    echo $! > "$PID_FILE"
    echo "Auto-refresh started (PID: $!)"
    echo "Log file: $LOG_FILE"
}

stop_refresh() {
    if [ ! -f "$PID_FILE" ]; then
        echo "Auto-refresh is not running"
        return 1
    fi
    
    PID=$(cat "$PID_FILE")
    if kill -0 "$PID" 2>/dev/null; then
        kill "$PID"
        echo "$(date): Auto-refresh stopped" >> "$LOG_FILE"
        echo "Auto-refresh stopped (PID: $PID)"
    else
        echo "Process $PID not found"
    fi
    
    rm -f "$PID_FILE"
}

status_refresh() {
    if [ -f "$PID_FILE" ] && kill -0 "$(cat "$PID_FILE")" 2>/dev/null; then
        echo "Auto-refresh is running (PID: $(cat "$PID_FILE"))"
        echo "Log file: $LOG_FILE"
        echo "Recent logs:"
        tail -5 "$LOG_FILE" 2>/dev/null || echo "No logs available"
    else
        echo "Auto-refresh is not running"
    fi
}

case "${1:-start}" in
    start)
        start_refresh
        ;;
    stop)
        stop_refresh
        ;;
    status)
        status_refresh
        ;;
    restart)
        stop_refresh
        sleep 2
        start_refresh
        ;;
    *)
        echo "Usage: $0 {start|stop|status|restart}"
        exit 1
        ;;
esac
