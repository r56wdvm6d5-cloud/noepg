#!/usr/bin/env python3

# Compare EPG channels with present_in_epg.m3u and find missing

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

# Channels in present_in_epg.m3u
m3u_present_channels = [
    "ABC ME",
    "ABC TV",
    "BBC One EastHD",
    "BBC Two HD",
    "Bravo HD",
    "Bravo PLUS 1",
    "CA ABC WEST",
    "CA CBS WEST",
    "CA FOX EAST",
    "CBC Calgary HD",
    "CBC Halifax",
    "CBC Montreal",
    "CBC Ottawa",
    "CBC Toronto HD",
    "CBC Vancouver",
    "CTV COMEDY CHANNEL",
    "CTV Calgary HD",
    "CTV DRAMA CHANNEL",
    "CTV Halifax",
    "CTV Montreal",
    "CTV Ottawa",
    "CTV SCI-FI CHANNEL HD",
    "CTV Toronto HD",
    "CTV Two - Ottawa",
    "CTV Two - Vancouver/Victoria",
    "CTV Vancouver HD",
    "Channel 4 HD",
    "Channel 5 HD",
    "Citytv Calgary",
    "Citytv Montreal",
    "Citytv Toronto HD",
    "Citytv Vancouver",
    "Comedy Central HD",
    "Crave4",
    "E4 HD",
    "True Crime",
    "True Crime Xtra",
    "US CBS",
    "US PBS East",
    "WABC-DT",
    "WCBS-DT"
]

print("EPG CHANNELS MISSING FROM present_in_epg.m3u")
print("=" * 50)
print()

missing_count = 0
found_count = 0

for epg_channel in sorted(epg_channels):
    found = False
    
    # Check for exact match
    for m3u_channel in m3u_present_channels:
        if epg_channel.lower() == m3u_channel.lower():
            found = True
            break
    
    # Check for partial match
    if not found:
        for m3u_channel in m3u_present_channels:
            clean_m3u = m3u_channel.replace(" HD", "").replace(" (ASIA)", "").replace("CA ", "").replace("US ", "").replace("UK ", "")
            if epg_channel.lower() in clean_m3u.lower() or clean_m3u.lower() in epg_channel.lower():
                found = True
                break
    
    if found:
        print(f"✅ FOUND: {epg_channel}")
        found_count += 1
    else:
        print(f"❌ MISSING: {epg_channel}")
        missing_count += 1

print()
print("=" * 50)
print(f"SUMMARY:")
print(f"✅ Found in M3U: {found_count}")
print(f"❌ Missing from M3U: {missing_count}")
print(f"📊 Total EPG Channels: {len(epg_channels)}")
print(f"📊 Total M3U Channels: {len(m3u_present_channels)}")

print()
print("CHANNELS NEEDED TO ADD TO M3U:")
print("-" * 30)
for epg_channel in sorted(epg_channels):
    found = False
    
    # Check for exact match
    for m3u_channel in m3u_present_channels:
        if epg_channel.lower() == m3u_channel.lower():
            found = True
            break
    
    # Check for partial match
    if not found:
        for m3u_channel in m3u_present_channels:
            clean_m3u = m3u_channel.replace(" HD", "").replace(" (ASIA)", "").replace("CA ", "").replace("US ", "").replace("UK ", "")
            if epg_channel.lower() in clean_m3u.lower() or clean_m3u.lower() in epg_channel.lower():
                found = True
                break
    
    if not found:
        print(f"- {epg_channel}")
