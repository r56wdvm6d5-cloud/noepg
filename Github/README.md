# EPG Auto-Push System

This system automatically monitors and pushes changes to the `epg_combined.xml` file to your GitHub repository.

## Files

- `auto_push_epg.sh` - Main script that checks for file changes and pushes to GitHub
- `monitor_epg_changes.sh` - Continuous monitoring script that runs in the background
- `epg_combined.xml` - The EPG data file that gets monitored
- `auto_push.log` - Log file for auto-push operations
- `monitor.log` - Log file for monitoring operations

## Usage

### Start Auto-Monitoring
```bash
./monitor_epg_changes.sh start
```

### Stop Auto-Monitoring
```bash
./monitor_epg_changes.sh stop
```

### Check Status
```bash
./monitor_epg_changes.sh status
```

### Restart Monitoring
```bash
./monitor_epg_changes.sh restart
```

### Manual Push (if needed)
```bash
./auto_push_epg.sh
```

## How It Works

1. The monitoring script checks the EPG file every 60 seconds
2. It uses MD5 hash to detect file changes
3. When changes are detected, it automatically:
   - Adds the file to git
   - Commits with timestamp
   - Pushes to GitHub repository `noepg`

## Features

- **Automatic Detection**: Monitors file changes using MD5 hash comparison
- **Logging**: All operations are logged with timestamps
- **Background Process**: Runs continuously in the background
- **Error Handling**: Logs errors and continues monitoring
- **Git Integration**: Automatically commits and pushes changes

## Requirements

- Git configured with GitHub credentials
- Internet connection for pushing to GitHub
- Write permissions to the repository

## Logs

- `auto_push.log` - Contains details of push operations
- `monitor.log` - Contains monitoring status and operations

## Troubleshooting

If auto-push fails:
1. Check the logs in `auto_push.log` and `monitor.log`
2. Verify git credentials are configured
3. Ensure you have internet connectivity
4. Check if you have write access to the repository

## Repository

- **Repository**: `https://github.com/r56wdvm6d5-cloud/noepg.git`
- **Branch**: `main`
- **File Path**: `Github/epg_combined.xml`
