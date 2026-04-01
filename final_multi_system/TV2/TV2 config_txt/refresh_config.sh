#!/bin/bash

# TV2 Refresh script - runs TV2 multi-XML processor
# Processes TV2 channels and generates updated EPG

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROCESSOR_SCRIPT="$SCRIPT_DIR/../TV2 multi_processor/TV2_multi_xml_processor.py"
CONFIG_FILE="$SCRIPT_DIR/TV2.txt"
OUTPUT_FILE="$SCRIPT_DIR/../TV2 Github/TV2_epg.xml"

echo "Running TV2 refresh..."
echo "Config: $CONFIG_FILE"
echo "Output: $OUTPUT_FILE"

# Check if required files exist
if [ ! -f "$PROCESSOR_SCRIPT" ]; then
    echo "Error: Processor script not found: $PROCESSOR_SCRIPT"
    exit 1
fi

if [ ! -f "$CONFIG_FILE" ]; then
    echo "Error: Config file not found: $CONFIG_FILE"
    exit 1
fi

# Run the TV2 processor
cd "$(dirname "$PROCESSOR_SCRIPT")"
python3 "$(basename "$PROCESSOR_SCRIPT")" --config "$CONFIG_FILE" --output "$OUTPUT_FILE"

if [ $? -eq 0 ]; then
    echo "TV2 refresh completed successfully"
    echo "Updated: $OUTPUT_FILE"
else
    echo "TV2 refresh failed"
    exit 1
fi
