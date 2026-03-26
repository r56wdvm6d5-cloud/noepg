# Multi-XML EPG System - Setup Guide

## 🚀 Quick Start Guide

### **Step 1: Configure Channels**
Edit `multi_xml_config.txt` and add your XML sources:

```
# Format: CHANNEL_ID|URL|DISPLAY_NAME
9256|https://epg.pw/api/epg.xml?lang=en&timezone=QXNpYS9LYXJhY2hp&date=20260326&channel_id=9256|Nat Geo HD
9220|https://epg.pw/api/epg.xml?lang=en&timezone=QXNpYS9LYXJhY2hp&date=20260324&channel_id=9220|Animal Planet
```

### **Step 2: Test System**
Run the refresh script to test everything works:

```bash
./refresh_xml.sh
```

### **Step 3: Setup Auto-Refresh**
Choose one method:

**Option A: Cron Job (Recommended)**
```bash
./auto_refresh_and_push.sh --setup-cron
```

**Option B: Continuous Mode**
```bash
./auto_refresh_and_push.sh --continuous
```

### **Step 4: Use in IPTV Client**
Add this URL to your IPTV client:
```
https://r56wdvm6d5-cloud.github.io/epguk/epg.xml
```

## ✅ Verification

1. **Check output:** `cat output/dsmr_output.xml`
2. **Check GitHub Pages:** Visit the URL in browser
3. **Check logs:** `tail -f cron.log`

## 🎯 System Features

- **Multiple XML Sources** - Unlimited channels
- **Auto-Date Updates** - Always current day
- **Error Handling** - Continues if sources fail
- **Standard EPG Format** - IPTV compatible
- **GitHub Pages** - Free hosting
- **Auto-Refresh** - Every 30 minutes
- **Private Repository** - Secure source code

## 📞 Troubleshooting

**"No sources found"** - Check `multi_xml_config.txt` format  
**"Failed to fetch"** - Verify URLs are accessible  
**"Empty output"** - Check all sources failed  
**"Cron not working"** - Run `crontab -l` to verify

Your system is ready for unlimited EPG channels!
