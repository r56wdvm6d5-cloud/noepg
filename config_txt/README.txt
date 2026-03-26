# Multi-XML Configuration Guide

This folder contains the configuration files and scripts for the Multi-XML Processor system.

## Files

- `multi_xml_config.txt` - Configuration file with XML sources
- `refresh_config.sh` - Script to update dates in config file
- `auto_refresh.sh` - Script to run automatic refresh every 30 minutes
- `auto_refresh.log` - Log file for auto-refresh operations

## Commands

### Manual Refresh
Update dates in config file to current date:
```bash
./refresh_config.sh
```

### Auto-Refresh Management
Start automatic refresh (runs every 30 minutes):
```bash
./auto_refresh.sh start
```

Stop automatic refresh:
```bash
./auto_refresh.sh stop
```

Check if auto-refresh is running and view recent logs:
```bash
./auto_refresh.sh status
```

Restart auto-refresh:
```bash
./auto_refresh.sh restart
```

## Configuration Format

Edit `multi_xml_config.txt` to add XML sources:
```
CHANNEL_ID|URL|DISPLAY_NAME
```

Example:
```
9256|https://epg.pw/api/epg.xml?channel_id=9256|Nat Geo HD
9220|https://epg.pw/api/epg.xml?lang=en&date=20260324&channel_id=9220|Animal Planet
```

## Usage with Multi-XML Processor

Run the processor with updated config:
```bash
python3 multi_xml_processor.py --config config_txt/multi_xml_config.txt --output output.xml
```

## Auto-Refresh Features

- Automatically updates all `date=` parameters to current date
- Creates backup of config file before updating
- Runs every 30 minutes in background
- Logs all operations to `auto_refresh.log`
- Persists across system restarts (needs manual restart after reboot)
