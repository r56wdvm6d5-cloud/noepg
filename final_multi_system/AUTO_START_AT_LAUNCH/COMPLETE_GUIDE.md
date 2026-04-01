# Multi-XML EPG System - Complete Guide

## Overview
This system automatically fetches and combines multiple XML EPG sources into a single file, with automatic date updates and scheduled processing.

## Directory Structure
```
final_multi_system/
├── config_txt/                    # Configuration files
│   ├── multi_xml_config.txt      # XML sources configuration
│   ├── refresh_config.sh         # Manual date refresh script
│   ├── auto_refresh.sh           # Auto-refresh service (30 min)
│   ├── auto_refresh.log          # Config refresh logs
│   └── README.md                 # Configuration guide
├── multi_processor/               # Processing files
│   ├── multi_xml_processor.py    # Main XML processor script
│   ├── auto_refresh_processor.sh # Auto-processor service (30 min)
│   ├── auto_refresh_processor.log # Processor logs
│   └── README_auto_refresh.md    # Processor guide
├── add_backup/                    # Backup storage
├── Github/                        # Output directory
│   └── epg_combined.xml          # Generated EPG file
├── com.epgrefresh.plist          # Launch daemon (config refresh)
├── com.epgprocessor.plist        # Launch daemon (processor)
├── install_launch_daemons.sh     # Installation script
└── COMPLETE_GUIDE.md             # This guide
```

## Quick Start

### 1. Configure XML Sources
Edit `config_txt/multi_xml_config.txt`:
```
CHANNEL_ID|URL|DISPLAY_NAME
9256|https://epg.pw/api/epg.xml?channel_id=9256|Nat Geo HD
9220|https://epg.pw/api/epg.xml?lang=en&date=20260326&channel_id=9220|Animal Planet
```

### 2. Manual Operations
```bash
# Update dates manually
cd config_txt && ./refresh_config.sh

# Process XML manually
cd multi_processor && python3 multi_xml_processor.py --config ../config_txt/multi_xml_config.txt --output ../Github/epg_combined.xml
```

### 3. Auto-Refresh Management
```bash
# Start auto-refresh (30 min intervals)
cd config_txt && ./auto_refresh.sh start
cd ../multi_processor && ./auto_refresh_processor.sh start

# Check status
cd config_txt && ./auto_refresh.sh status
cd ../multi_processor && ./auto_refresh_processor.sh status

# Stop auto-refresh
cd config_txt && ./auto_refresh.sh stop
cd ../multi_processor && ./auto_refresh_processor.sh stop
```

## Launch Daemon (Boot Auto-Start)

### Installation
```bash
./install_launch_daemons.sh
```

### How It Works
- **Launch daemons** start scripts only at boot
- **Scripts** handle their own 30-minute intervals
- **No continuous restart loops**

### Management
```bash
# Check if services are running
launchctl list | grep epg

# Stop services
launchctl stop com.epgrefresh
launchctl stop com.epgprocessor

# Restart services
launchctl stop com.epgrefresh
launchctl stop com.epgprocessor
launchctl start com.epgrefresh
launchctl start com.epgprocessor

# Uninstall (remove auto-start)
launchctl unload ~/Library/LaunchAgents/com.epgrefresh.plist
launchctl unload ~/Library/LaunchAgents/com.epgprocessor.plist
rm ~/Library/LaunchAgents/com.epgrefresh.plist
rm ~/Library/LaunchAgents/com.epgprocessor.plist
```

## How It Works

### Auto-Refresh System
1. **Config Refresh** (every 30 minutes): Updates date parameters in URLs
2. **Processor Refresh** (every 30 minutes): Fetches XML and generates combined EPG
3. **Launch Daemons**: Start services automatically at boot

### Date Updates
- URLs with `date=` parameters are automatically updated to current date
- Format: `date=YYYYMMDD`
- Backup files saved to `add_backup/` folder

### Output
- Combined EPG file: `Github/epg_combined.xml`
- Overwrites existing file each time
- Contains all channels and programs from configured sources

## Troubleshooting

### Services Not Running
```bash
# Check process status
ps aux | grep auto_refresh

# Check logs
cd config_txt && cat auto_refresh.log
cd ../multi_processor && cat auto_refresh_processor.log

# Check launch daemon logs
cd config_txt && cat launchd.log
cd ../multi_processor && cat launchd.log
```

### No Output File
```bash
# Check if output directory exists
ls -la Github/

# Manually run processor to test
cd multi_processor && python3 multi_xml_processor.py --config ../config_txt/multi_xml_config.txt --output ../Github/epg_combined.xml
```

### Date Not Updating
```bash
# Check config file format
cat config_txt/multi_xml_config.txt

# Manually refresh dates
cd config_txt && ./refresh_config.sh
```

## Configuration Examples

### Adding New Channels
Edit `config_txt/multi_xml_config.txt`:
```
1234|https://example.com/epg.xml?channel=1234|Channel Name
5678|https://another-site.com/epg.xml?date=20260326&channel=5678|Another Channel
```

### Changing Intervals
Edit the sleep duration in scripts:
- `config_txt/auto_refresh.sh`: Change `1800` (30 minutes)
- `multi_processor/auto_refresh_processor.sh`: Change `1800` (30 minutes)

## Security Notes
- Launch daemons run as your user (not root)
- Only access files in project directory
- No network privileges beyond existing XML fetching
- Easy to disable/remove if needed

## Maintenance
- Logs rotate automatically (check file sizes periodically)
- Backups accumulate in `add_backup/` (clean old ones if needed)
- Monitor `Github/epg_combined.xml` for successful generation

## File Locations
- **Config**: `config_txt/multi_xml_config.txt`
- **Output**: `Github/epg_combined.xml`
- **Logs**: `config_txt/auto_refresh.log`, `multi_processor/auto_refresh_processor.log`
- **Backups**: `add_backup/multi_xml_config.txt.backup`
- **Launch Daemons**: `~/Library/LaunchAgents/com.epgrefresh.plist`, `~/Library/LaunchAgents/com.epgprocessor.plist`
