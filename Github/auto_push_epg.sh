#!/bin/bash

# Auto-push script for EPG combined XML file
# This script monitors the file and automatically pushes changes to GitHub

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="$(dirname "$SCRIPT_DIR")"
XML_FILE="$SCRIPT_DIR/epg_combined.xml"
LOG_FILE="$SCRIPT_DIR/auto_push.log"

# Function to log messages
log_message() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

# Function to check if file has changed
has_file_changed() {
    local current_hash=$(md5sum "$XML_FILE" | cut -d' ' -f1)
    
    if [ ! -f "$SCRIPT_DIR/.last_hash" ]; then
        echo "$current_hash" > "$SCRIPT_DIR/.last_hash"
        return 0  # First time, consider as changed
    fi
    
    local last_hash=$(cat "$SCRIPT_DIR/.last_hash")
    
    if [ "$current_hash" != "$last_hash" ]; then
        echo "$current_hash" > "$SCRIPT_DIR/.last_hash"
        log_message "File hash changed: $last_hash -> $current_hash"
        return 0  # File has changed
    fi
    
    return 1  # File hasn't changed
}

# Function to push changes to GitHub
push_to_github() {
    cd "$REPO_DIR"
    
    log_message "File changed, starting auto-push process..."
    
    # Add the updated file
    if git add "$XML_FILE"; then
        log_message "File added to git staging area"
    else
        log_message "ERROR: Failed to add file to git"
        return 1
    fi
    
    # Check if there are actually changes to commit
    if git diff --cached --quiet; then
        log_message "No actual changes detected in staged files"
        return 0
    fi
    
    # Commit the changes
    if git commit -m "Auto-update EPG combined XML file - $(date '+%Y-%m-%d %H:%M:%S')"; then
        log_message "Changes committed successfully"
    else
        log_message "ERROR: Failed to commit changes"
        return 1
    fi
    
    # Push to GitHub
    if git push origin main; then
        log_message "Changes pushed to GitHub successfully"
    else
        log_message "ERROR: Failed to push to GitHub"
        return 1
    fi
    
    return 0
}

# Main execution
log_message "Auto-push script started"

if [ ! -f "$XML_FILE" ]; then
    log_message "ERROR: EPG combined XML file not found at $XML_FILE"
    exit 1
fi

# Check if file has changed and push if needed
if has_file_changed; then
    push_to_github
else
    log_message "No changes detected in EPG combined XML file"
fi

log_message "Auto-push script completed"
