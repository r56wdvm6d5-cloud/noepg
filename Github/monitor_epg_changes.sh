#!/bin/bash

# Continuous monitoring script for EPG file changes
# This script runs in the background and monitors file changes

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MONITOR_SCRIPT="$SCRIPT_DIR/auto_push_epg.sh"
PID_FILE="$SCRIPT_DIR/.monitor_pid"
LOG_FILE="$SCRIPT_DIR/monitor.log"

# Function to log messages
log_message() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

# Function to check if monitoring is already running
is_monitoring_running() {
    if [ -f "$PID_FILE" ]; then
        local pid=$(cat "$PID_FILE")
        if ps -p "$pid" > /dev/null 2>&1; then
            return 0  # Monitoring is running
        else
            rm -f "$PID_FILE"  # PID file is stale, remove it
        fi
    fi
    return 1  # Monitoring is not running
}

# Function to start monitoring
start_monitoring() {
    if is_monitoring_running; then
        log_message "Monitoring is already running (PID: $(cat "$PID_FILE"))"
        return 1
    fi
    
    log_message "Starting EPG file monitoring..."
    
    # Start the monitoring loop in background
    (
        while true; do
            # Run the auto-push script
            "$MONITOR_SCRIPT"
            
            # Wait for 60 seconds before next check
            sleep 60
        done
    ) &
    
    # Save the PID
    echo $! > "$PID_FILE"
    log_message "Monitoring started (PID: $!)"
    
    return 0
}

# Function to stop monitoring
stop_monitoring() {
    if is_monitoring_running; then
        local pid=$(cat "$PID_FILE")
        kill "$pid"
        rm -f "$PID_FILE"
        log_message "Monitoring stopped (PID: $pid)"
        return 0
    else
        log_message "Monitoring is not running"
        return 1
    fi
}

# Function to show status
show_status() {
    if is_monitoring_running; then
        log_message "Monitoring is running (PID: $(cat "$PID_FILE"))"
    else
        log_message "Monitoring is not running"
    fi
}

# Main script logic
case "${1:-start}" in
    start)
        start_monitoring
        ;;
    stop)
        stop_monitoring
        ;;
    restart)
        stop_monitoring
        sleep 2
        start_monitoring
        ;;
    status)
        show_status
        ;;
    *)
        echo "Usage: $0 {start|stop|restart|status}"
        echo "  start   - Start monitoring EPG file changes"
        echo "  stop    - Stop monitoring"
        echo "  restart - Restart monitoring"
        echo "  status  - Show monitoring status"
        exit 1
        ;;
esac
