#!/bin/bash

# IPTV Nator Continuous Monitoring Script
# Monitors GitHub repository and automatically refreshes IPTV Nator when updates are available

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REFRESH_SCRIPT="$SCRIPT_DIR/iptv_nator_refresh.sh"
PID_FILE="$SCRIPT_DIR/.iptv_monitor_pid"
LOG_FILE="$SCRIPT_DIR/iptv_monitor.log"

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
        log_message "IPTV Nator monitoring is already running (PID: $(cat "$PID_FILE"))"
        return 1
    fi
    
    log_message "Starting IPTV Nator GitHub monitoring..."
    
    # Start the monitoring loop in background
    (
        while true; do
            # Run the refresh script
            "$REFRESH_SCRIPT"
            
            # Wait for 5 minutes before next check (GitHub updates frequency)
            sleep 300
        done
    ) &
    
    # Save the PID
    echo $! > "$PID_FILE"
    log_message "IPTV Nator monitoring started (PID: $!)"
    
    return 0
}

# Function to stop monitoring
stop_monitoring() {
    if is_monitoring_running; then
        local pid=$(cat "$PID_FILE")
        kill "$pid"
        rm -f "$PID_FILE"
        log_message "IPTV Nator monitoring stopped (PID: $pid)"
        return 0
    else
        log_message "IPTV Nator monitoring is not running"
        return 1
    fi
}

# Function to show status
show_status() {
    if is_monitoring_running; then
        log_message "IPTV Nator monitoring is running (PID: $(cat "$PID_FILE"))"
    else
        log_message "IPTV Nator monitoring is not running"
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
    once)
        log_message "Running one-time IPTV Nator refresh check..."
        "$REFRESH_SCRIPT"
        ;;
    *)
        echo "Usage: $0 {start|stop|restart|status|once}"
        echo "  start   - Start monitoring GitHub for IPTV Nator updates"
        echo "  stop    - Stop monitoring"
        echo "  restart - Restart monitoring"
        echo "  status  - Show monitoring status"
        echo "  once    - Run refresh check once"
        exit 1
        ;;
esac
