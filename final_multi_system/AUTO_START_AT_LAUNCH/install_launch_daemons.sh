#!/bin/bash

# Install launch daemons for auto-refresh services
# This will make the services start automatically at boot

echo "Installing EPG refresh launch daemons..."

# Stop existing services
echo "Stopping existing services..."
cd config_txt && ./auto_refresh.sh stop 2>/dev/null
cd ../multi_processor && ./auto_refresh_processor.sh stop 2>/dev/null
cd ..

# Copy plist files to LaunchAgents
echo "Installing launch daemons..."
cp com.epgrefresh.plist ~/Library/LaunchAgents/
cp com.epgprocessor.plist ~/Library/LaunchAgents/

# Load the launch daemons
echo "Loading launch daemons..."
launchctl load ~/Library/LaunchAgents/com.epgrefresh.plist
launchctl load ~/Library/LaunchAgents/com.epgprocessor.plist

# Start the services
echo "Starting services..."
launchctl start com.epgrefresh
launchctl start com.epgprocessor

echo "Launch daemons installed and started!"
echo "Services will start scripts at boot, which will then refresh every 30 minutes."
echo ""
echo "To check status:"
echo "  launchctl list | grep epg"
echo ""
echo "To stop services:"
echo "  launchctl stop com.epgrefresh"
echo "  launchctl stop com.epgprocessor"
echo ""
echo "To uninstall:"
echo "  launchctl unload ~/Library/LaunchAgents/com.epgrefresh.plist"
echo "  launchctl unload ~/Library/LaunchAgents/com.epgprocessor.plist"
echo "  rm ~/Library/LaunchAgents/com.epgrefresh.plist"
echo "  rm ~/Library/LaunchAgents/com.epgprocessor.plist"
