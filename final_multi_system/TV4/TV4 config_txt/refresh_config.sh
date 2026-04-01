#!/bin/bash

# TV4 Refresh Script - Runs the multi-XML processor
# This script is called by auto_refresh.sh to update the EPG data

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROCESSOR_SCRIPT="$SCRIPT_DIR/../TV4 multi_processor/TV4 multi_xml_processor.py"
CONFIG_FILE="$SCRIPT_DIR/TV4.txt"
OUTPUT_DIR="$SCRIPT_DIR/../TV4 Github"
OUTPUT_FILE="$OUTPUT_DIR/TV4_epg.xml"
LOG_FILE="$SCRIPT_DIR/refresh.log"

echo "$(date): Starting TV4 EPG refresh..." >> "$LOG_FILE"

# Check if required files exist
if [ ! -f "$PROCESSOR_SCRIPT" ]; then
    echo "$(date): ERROR - Processor script not found: $PROCESSOR_SCRIPT" >> "$LOG_FILE"
    exit 1
fi

if [ ! -f "$CONFIG_FILE" ]; then
    echo "$(date): ERROR - Config file not found: $CONFIG_FILE" >> "$LOG_FILE"
    exit 1
fi

# Create output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

# Run the multi-XML processor
echo "$(date): Running TV4 multi-XML processor..." >> "$LOG_FILE"
cd "$(dirname "$SCRIPT_DIR")"

if python3 "$PROCESSOR_SCRIPT" --config "$CONFIG_FILE" --output "$OUTPUT_FILE" >> "$LOG_FILE" 2>&1; then
    echo "$(date): TV4 EPG refresh completed successfully" >> "$LOG_FILE"
    echo "$(date): Output saved to: $OUTPUT_FILE" >> "$LOG_FILE"
    
    # Get file size for logging
    if [ -f "$OUTPUT_FILE" ]; then
        FILE_SIZE=$(du -h "$OUTPUT_FILE" | cut -f1)
        echo "$(date): Output file size: $FILE_SIZE" >> "$LOG_FILE"
    fi
else
    echo "$(date): ERROR - TV4 EPG refresh failed" >> "$LOG_FILE"
    exit 1
fi

echo "$(date): TV4 refresh process finished" >> "$LOG_FILE"
