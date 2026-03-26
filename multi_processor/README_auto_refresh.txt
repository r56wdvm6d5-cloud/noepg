# Multi-XML Processor Auto-Refresh

This script automatically runs the multi_xml_processor.py every 30 minutes with the latest dates and generates the latest EPG data.

## Files Used
- **Processor**: `multi_xml_processor.py` - Main Python script for processing XML sources
- **Config**: `../config_txt/multi_xml_config.txt` - Configuration file with XML source URLs
- **Output**: `../Github/` - Directory for generated EPG files

## Usage
#Start Manual Refresh

./refresh_processor.sh

### Start Auto-Refresh
```bash
./auto_refresh_processor.sh start
```
- Starts the auto-refresh process
- Runs immediately once, then every 30 minutes
- Creates and updates the `epg_combined.xml` file

### Stop Auto-Refresh
```bash
./auto_refresh_processor.sh stop
```

### Check Status
```bash
./auto_refresh_processor.sh status
```

### Restart Auto-Refresh
```bash
./auto_refresh_processor.sh restart
```

### Run Once (Manual)
```bash
./auto_refresh_processor.sh run-once
```
- Runs the processor immediately without starting the auto-refresh loop

## Features

1. **Automatic Date Updates**: The Python processor automatically updates date parameters in URLs to the current date
2. **File Replacement**: Each refresh replaces the existing `epg_combined.xml` file with the latest data
3. **Log File**: All operations are logged to `auto_refresh_processor.log`
4. **Error Handling**: Logs errors and continues running

## Output Structure
```
../Github/
└── epg_combined.xml    # Single file that gets replaced with latest data
```

## Log File
The script logs all activities to `auto_refresh_processor.log` including:
- Start/stop events
- Each refresh run
- Success/failure status
- File generation details

## Process Management
- PID file: `.auto_refresh_processor.pid`
- Background process runs continuously
- Can be stopped and restarted safely
- Survives terminal sessions (runs in background)
