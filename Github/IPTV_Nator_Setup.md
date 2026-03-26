# IPTV Nator Integration Configuration

## Overview
This system automatically keeps your IPTV Nator EPG data synchronized with your GitHub repository.

## Files Created
- `iptv_nator_refresh.sh` - Downloads latest XML and refreshes IPTV Nator
- `monitor_iptv_nator.sh` - Continuous monitoring service
- `iptv_refresh.log` - Log file for refresh operations
- `iptv_monitor.log` - Log file for monitoring operations

## Setup Instructions

### 1. Configure IPTV Nator
In IPTV Nator, set your EPG source to:
```
file:///Users/ah/CascadeProjects/windsurf-project/final_multi_system/Github/epg_combined.xml
```

### 2. Start the monitoring service
```bash
./monitor_iptv_nator.sh start
```

### 3. Test the integration
```bash
./monitor_iptv_nator.sh once
```

## How It Works

1. **GitHub Monitoring**: Checks your GitHub repository every 5 minutes
2. **Hash Comparison**: Compares remote and local XML file hashes
3. **Auto Download**: Downloads updated XML when changes are detected
4. **IPTV Nator Refresh**: Automatically refreshes IPTV Nator with new data

## Features

- **Real-time Updates**: Monitors GitHub for EPG changes
- **Automatic Refresh**: Updates IPTV Nator without manual intervention
- **Multiple Refresh Methods**: 
  - Restarts IPTV Nator application
  - Updates config files to trigger refresh
  - Copies XML to IPTV Nator data directory
- **Error Handling**: Logs all operations and handles network issues
- **Lightweight**: Minimal resource usage

## Commands

### Start Monitoring
```bash
./monitor_iptv_nator.sh start
```

### Stop Monitoring
```bash
./monitor_iptv_nator.sh stop
```

### Check Status
```bash
./monitor_iptv_nator.sh status
```

### Manual Refresh
```bash
./monitor_iptv_nator.sh once
```

### Restart Monitoring
```bash
./monitor_iptv_nator.sh restart
```

## Configuration Options

### Check Interval
Default: 5 minutes (300 seconds)
To change: Edit `sleep 300` in `monitor_iptv_nator.sh`

### IPTV Nator Paths
Default paths are set for macOS:
- Config: `~/Library/Application Support/IPTV-Nator`
- Data: `~/Library/Application Support/IPTV-Nator/data`

Adjust these in `iptv_nator_refresh.sh` if your installation differs.

## GitHub Repository
- **Repository**: `https://github.com/r56wdvm6d5-cloud/noepg`
- **Raw XML URL**: `https://raw.githubusercontent.com/r56wdvm6d5-cloud/noepg/main/Github/epg_combined.xml`

## Troubleshooting

### IPTV Nator not updating
1. Check if IPTV Nator is running
2. Verify the file path in IPTV Nator settings
3. Check logs in `iptv_refresh.log`

### Network issues
1. Test GitHub connectivity: `curl -I https://github.com`
2. Check if raw XML URL is accessible
3. Verify internet connection

### Monitoring not working
1. Check status: `./monitor_iptv_nator.sh status`
2. Review logs: `tail -f iptv_monitor.log`
3. Restart service: `./monitor_iptv_nator.sh restart`

## Integration with Auto-Push System

This works seamlessly with your existing auto-push system:
1. EPG file updates → Auto-push to GitHub
2. GitHub monitoring detects changes → Downloads new XML
3. IPTV Nator automatically refreshes with latest data

The complete automation cycle ensures your IPTV Nator always has the most current EPG data.
