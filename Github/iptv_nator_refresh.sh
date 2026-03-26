#!/bin/bash

# IPTV Nator Auto-Refresh Script
# This script monitors GitHub repository for EPG updates and refreshes IPTV Nator

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="$(dirname "$SCRIPT_DIR")"
GITHUB_URL="https://github.com/r56wdvm6d5-cloud/noepg.git"
RAW_XML_URL="https://raw.githubusercontent.com/r56wdvm6d5-cloud/noepg/main/Github/epg_combined.xml"
LOCAL_XML_FILE="$SCRIPT_DIR/epg_combined.xml"
LOG_FILE="$SCRIPT_DIR/iptv_refresh.log"
LAST_UPDATE_FILE="$SCRIPT_DIR/.last_github_update"

# IPTV Nator paths (adjust these based on your IPTV Nator installation)
IPTV_NATOR_CONFIG_DIR="$HOME/Library/Application Support/IPTV-Nator"
IPTV_NATOR_DATA_DIR="$HOME/Library/Application Support/IPTV-Nator/data"

# Function to log messages
log_message() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

# Function to get remote file hash
get_remote_hash() {
    curl -s "$RAW_XML_URL" | md5sum | cut -d' ' -f1
}

# Function to get local file hash
get_local_hash() {
    if [ -f "$LOCAL_XML_FILE" ]; then
        md5sum "$LOCAL_XML_FILE" | cut -d' ' -f1
    else
        echo ""
    fi
}

# Function to download latest XML from GitHub
download_latest_xml() {
    log_message "Downloading latest XML from GitHub..."
    
    if curl -s -o "$LOCAL_XML_FILE" "$RAW_XML_URL"; then
        log_message "Successfully downloaded XML file"
        return 0
    else
        log_message "ERROR: Failed to download XML from GitHub"
        return 1
    fi
}

# Function to refresh IPTV Nator
refresh_iptv_nator() {
    log_message "Refreshing IPTV Nator..."
    
    # Method 1: Kill and restart IPTV Nator (if running)
    if pgrep -f "IPTV-Nator" > /dev/null; then
        log_message "Stopping IPTV Nator..."
        pkill -f "IPTV-Nator"
        sleep 2
        
        log_message "Starting IPTV Nator..."
        open -a "IPTV-Nator"
        sleep 3
    fi
    
    # Method 2: Trigger refresh by updating config (alternative approach)
    if [ -d "$IPTV_NATOR_CONFIG_DIR" ]; then
        # Touch the config directory to trigger refresh
        touch "$IPTV_NATOR_CONFIG_DIR"
        log_message "Triggered IPTV Nator refresh via config update"
    fi
    
    # Method 3: Copy XML to IPTV Nator data directory
    if [ -d "$IPTV_NATOR_DATA_DIR" ]; then
        cp "$LOCAL_XML_FILE" "$IPTV_NATOR_DATA_DIR/epg_combined.xml" 2>/dev/null
        log_message "Updated IPTV Nator data directory"
    fi
    
    return 0
}

# Function to check for updates
check_for_updates() {
    local remote_hash=$(get_remote_hash)
    local local_hash=$(get_local_hash)
    
    if [ -z "$remote_hash" ]; then
        log_message "ERROR: Could not fetch remote file hash"
        return 1
    fi
    
    if [ "$remote_hash" != "$local_hash" ]; then
        log_message "Update detected! Remote hash: $remote_hash, Local hash: $local_hash"
        
        if download_latest_xml; then
            refresh_iptv_nator
            echo "$remote_hash" > "$LAST_UPDATE_FILE"
            log_message "IPTV Nator refresh completed successfully"
            return 0
        else
            log_message "ERROR: Failed to download updated XML"
            return 1
        fi
    else
        log_message "No updates detected"
        return 0
    fi
}

# Main execution
log_message "IPTV Nator auto-refresh script started"

# Check if this is the first run
if [ ! -f "$LAST_UPDATE_FILE" ]; then
    log_message "First run - downloading initial XML file"
    if download_latest_xml; then
        refresh_iptv_nator
        get_local_hash > "$LAST_UPDATE_FILE"
        log_message "Initial setup completed"
    else
        log_message "ERROR: Initial setup failed"
        exit 1
    fi
else
    check_for_updates
fi

log_message "IPTV Nator auto-refresh script completed"
