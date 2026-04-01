# TVMaze EPG Generator

A Python script that generates XMLTV format Electronic Program Guide (EPG) data using the TVMaze API.

## Features

- Fetches TV schedule data from multiple countries
- Generates XMLTV format compatible with media center applications
- Configurable channels, countries, and date ranges
- Error handling and logging
- Rate limiting to respect API limits
- Clean HTML description parsing

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the script:
```bash
python tvmaze_epg.py
```

## Configuration

The script can be customized by modifying the configuration in the `main()` function:

```python
custom_config = {
    'timezone': pytz.timezone("US/Eastern"),  # Timezone for scheduling
    'days': 3,                                 # Number of days to fetch
    'countries': ["US", "GB", "CA"],           # Countries to fetch data for
    'target_channels': ["ABC", "NBC", "CBS"],  # Specific channels (empty = all)
    'base_url': "https://api.tvmaze.com/schedule",
    'request_delay': 0.1,                       # Delay between API calls
    'output_file': "epg.xml"                   # Output filename
}
```

## Output

The script generates an `epg.xml` file in XMLTV format that can be used with:
- Kodi
- Plex
- Jellyfin
- Other media center applications

## API Usage

This script uses the TVMaze API which is free and doesn't require authentication. However, please be respectful of their service:
- The script includes rate limiting
- Don't make excessive requests
- Cache results when possible

## Supported Countries

- US (United States)
- GB (United Kingdom) 
- CA (Canada)
- AU (Australia)
- NZ (New Zealand)

## Error Handling

The script includes comprehensive error handling for:
- Network connectivity issues
- API rate limiting
- Invalid data parsing
- File writing errors

All errors are logged with timestamps for debugging.

## Example Output

```xml
<?xml version='1.0' encoding='utf-8'?>
<tv generator-info-name="TVMaze EPG Generator" generator-info-url="https://www.tvmaze.com/api">
  <channel id="ABC.US">
    <display-name>ABC</display-name>
    <country>US</country>
  </channel>
  <programme start="20240401200000 -0400" stop="20240401210000 -0400" channel="ABC.US">
    <title>Show Title</title>
    <desc>Show description here...</desc>
    <category>TV Show</category>
  </programme>
</tv>
```
