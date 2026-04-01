#!/usr/bin/env python3

# Extract M3U links for channels present in EPG

# Channels from M3U with their stream URLs
m3u_channels_with_urls = {
    "ABC TV": "https://c.mjh.nz/abc-nsw.m3u8",
    "ABC ME": "https://c.mjh.nz/abc-me.m3u8", 
    "BBC One EastHD": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/47744.m3u8",
    "BBC Two HD": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/47745.m3u8",
    "Bravo HD": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/22562.m3u8",
    "Bravo PLUS 1": "https://i.mjh.nz/.r/bravo-plus1.m3u8",
    "CA ABC WEST": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/40780.m3u8",
    "CA CBS WEST": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/40755.m3u8",
    "CA FOX EAST": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/40709.m3u8",
    "CBC Calgary HD": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/40579.m3u8",
    "CBC Halifax": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/40570.m3u8",
    "CBC Montreal": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/40761.m3u8",
    "CBC Ottawa": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/40759.m3u8",
    "CBC Toronto HD": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/40758.m3u8",
    "CBC Vancouver": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/40757.m3u8",
    "CTV COMEDY CHANNEL": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/40746.m3u8",
    "CTV Calgary HD": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/40577.m3u8",
    "CTV DRAMA CHANNEL": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/40766.m3u8",
    "CTV Halifax": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/40595.m3u8",
    "CTV Montreal": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/40585.m3u8",
    "CTV Ottawa": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/40731.m3u8",
    "CTV SCI-FI CHANNEL HD": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/40620.m3u8",
    "CTV Toronto HD": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/40733.m3u8",
    "CTV Two - Ottawa": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/40734.m3u8",
    "CTV Two - Vancouver/Victoria": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/40736.m3u8",
    "CTV Vancouver HD": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/40732.m3u8",
    "Channel 4 HD": "https://viamotionhsi.netplus.ch/live/eds/channel4/browser-HLS8/channel4.m3u8",
    "Channel 5 HD": "https://viamotionhsi.netplus.ch/live/eds/channel5/browser-HLS8/channel5.m3u8",
    "Citytv Calgary": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/40578.m3u8",
    "Citytv Montreal": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/40598.m3u8",
    "Citytv Toronto HD": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/40752.m3u8",
    "Citytv Vancouver": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/40751.m3u8",
    "Comedy Central HD": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/15933.m3u8",
    "Crave4": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/40653.m3u8",
    "E4 HD": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/47772.m3u8",
    "True Crime": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/47754.m3u8",
    "True Crime Xtra": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/47753.m3u8",
    "US CBS": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/22560.m3u8",
    "US PBS East": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/23222.m3u8",
    "WABC-DT": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/23363.m3u8",
    "WCBS-DT": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/40756.m3u8"
}

# Channels currently in EPG
epg_channels = [
    "5",
    "A&E", 
    "ABC",
    "BBC Alba",
    "BBC One", 
    "BBC Two",
    "Bravo",
    "CBC",
    "CBS",
    "Channel 4",
    "Citytv",
    "CNBC",
    "CNN",
    "Comedy Central",
    "CTV",
    "Discovery",
    "E4",
    "ESPN",
    "FOX",
    "Fox News Channel",
    "History",
    "ITV1",
    "National Geographic",
    "NBC",
    "Newsmax",
    "NewsNation",
    "PBS",
    "Quest",
    "Sky Arts",
    "Syndication",
    "The CW",
    "TRUE CRIME"
]

print("#EXTM3U")
print()

present_count = 0

for channel_name, stream_url in sorted(m3u_channels_with_urls.items()):
    # Clean channel name for comparison
    clean_channel = channel_name.replace("CA ", "").replace("US ", "").replace("UK ", "")
    clean_channel = clean_channel.replace(" HD", "").replace(" (ASIA)", "")
    
    found = False
    for epg_channel in epg_channels:
        if clean_channel.lower() in epg_channel.lower() or epg_channel.lower() in clean_channel.lower():
            found = True
            break
    
    if found:
        print(f"#EXTINF:-1 group-title=\"TV SHOWS\",{channel_name}")
        print(stream_url)
        print()
        present_count += 1

print(f"# Total channels present in EPG: {present_count}")
