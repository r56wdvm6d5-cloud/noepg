#!/bin/bash

# Refresh script to update dates in multi_xml_config.txt
# Updates all date= parameters to current date

CONFIG_FILE="multi_xml_config.txt"
BACKUP_FILE="../add_backup/${CONFIG_FILE}.backup"

# Get current date in YYYYMMDD format
CURRENT_DATE=$(date +%Y%m%d)

echo "Updating dates in $CONFIG_FILE to $CURRENT_DATE"

# Create backup
if [ -f "$CONFIG_FILE" ]; then
    cp "$CONFIG_FILE" "$BACKUP_FILE"
    echo "Created backup: $BACKUP_FILE"
fi

# Update dates in the config file
sed -i '' "s/date=[0-9]*/date=$CURRENT_DATE/g" "$CONFIG_FILE"

echo "Updated date parameters to $CURRENT_DATE"
echo "Done!"
