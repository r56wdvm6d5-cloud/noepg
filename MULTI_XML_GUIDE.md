# Multi-XML Source Guide

## 📺 Adding More XML Sources

You can now add multiple EPG XML sources and combine them into one file!

### **Configuration File: `multi_xml_config.txt`**

**Format:**
```
CHANNEL_ID|URL|DISPLAY_NAME
```

### **Example:**
```
# Your current channel
9256|https://epg.pw/api/epg.xml?lang=en&timezone=QXNpYS9LYXJhY2hp&date=20260326&channel_id=9256|Nat Geo HD

# Add more channels like this:
1234|https://example.com/epg.xml?channel=1234|Discovery Channel
5678|https://another-site.com/tv-guide.xml?channel=5678|BBC One
9012|https://third-source.com/epg?date=20260326&channel=9012|Fox News
```

### **How to Add New Sources:**

1. **Edit the config file:**
   ```bash
   nano multi_xml_config.txt
   ```

2. **Add your channel line:**
   ```
   CHANNEL_ID|FULL_URL|Channel Name
   ```

3. **Save and test:**
   ```bash
   ./refresh_xml.sh
   ```

### **Finding XML URLs:**

Common EPG XML sources:
- **IPTV providers**: Check your provider's API documentation
- **TV networks**: Often have public EPG feeds
- **Third-party services**: Many free EPG aggregators

### **URL Parameters:**
Common parameters you might need:
- `?channel=1234` - Channel ID
- `?date=20260326` - Date
- `?lang=en` - Language
- `?timezone=UTC` - Timezone

### **Example Real Sources:**
```
# UK Channels
101|https://api.freeepg.tv/epg.xml?channel=101|BBC One
102|https://api.freeepg.tv/epg.xml?channel=102|BBC Two

# US Channels
201|https://epgprovider.com/guide.xml?id=201|CNN
202|https://epgprovider.com/guide.xml?id=202|Fox News

# Custom Provider
301|https://my-iptv-provider.com/epg?ch=301&date=20260326|My Channel
```

### **Features:**

✅ **Automatic fetching** from all sources  
✅ **Error handling** - continues if one source fails  
✅ **Channel deduplication** - no duplicate channels  
✅ **Standard EPG format** - works with IPTV clients  
✅ **Auto-refresh** - works with existing cron job  

### **Testing:**

After adding sources:
```bash
# Test multi-source processing
python3 multi_xml_processor.py --config multi_xml_config.txt --output test_output.xml

# Check the output
cat test_output.xml
```

### **Tips:**

1. **Start with 2-3 sources** to test
2. **Check XML format** - all sources should be similar
3. **Monitor logs** - see which sources work/fail
4. **Update dates** - some sources need current date parameter

### **Troubleshooting:**

**"No sources found"**: Check config file format  
**"Failed to fetch"**: Verify URL is accessible  
**"Parse error"**: XML might be malformed  
**"Empty output"**: All sources failed to fetch

Your combined EPG will contain all channels from all sources!
