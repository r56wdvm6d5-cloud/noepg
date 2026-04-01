#!/usr/bin/env python3

# Extract channels from M3U and compare with EPG channels

# Channels from M3U playlist
m3u_channels = [
    "AurLife HD",
    "US COLORS Asia", 
    "US GEO KAHANI",
    "US GEO TV",
    "HarPal Geo",
    "US HUM WORLD",
    "US HUM SITARAY",
    "US B4U MUSIC (ASIA)",
    "US MTV (ASIA)",
    "US SONY SAB",
    "US SONY SET",
    "SONY TV HD",
    "UK STAR PLUS",
    "A and E Canada HD",
    "A and E HD East",
    "WKBW-DT",
    "CA ABC WEST",
    "WCVB-DT",
    "WABC-DT",
    "4seven",
    "ABC TV",
    "ABC ME",
    "Antenna TV",
    "ASPiRE HD",
    "alibi+1",
    "AWE A Wealth of Entertainment HD",
    "BBC First",
    "BBC America",
    "BBC One EastHD",
    "BBC Two HD",
    "UK BBC Three",
    "UK BBC Four",
    "BBC Drama",
    "CA BET",
    "BET HD",
    "US BET HER",
    "US BET JAMS",
    "BLAZE",
    "Bravo HD",
    "Bravo PLUS 1",
    "US BOUNCE TV",
    "US BOUNCE XL",
    "CBBC HD",
    "Toon-A-Vision",
    "CA Disney JR",
    "CA Disney",
    "US PBS East",
    "CBC Calgary HD",
    "CBC Montreal",
    "CBC Ottawa",
    "CBC Toronto HD",
    "CBC Vancouver",
    "CBC Halifax",
    "WCBS-DT",
    "CA CBS WEST",
    "US CBS",
    "True Crime Xtra",
    "True Crime",
    "Channel 4 HD",
    "Channel 5 HD",
    "Challenge",
    "CHCH-DT",
    "Citytv Calgary",
    "Citytv Montreal",
    "Citytv Toronto HD",
    "Citytv Vancouver",
    "Cleo TV HD",
    "Country Music Television (CMT)",
    "CMT HD",
    "CTV COMEDY CHANNEL",
    "ComedyCentral",
    "ComedyXtra",
    "Comedy Central HD",
    "COMEDY.TV",
    "IFC HD",
    "Comet",
    "Cottage Life HD",
    "COZI TV",
    "Crave1",
    "Crave2",
    "Crave3",
    "Crave4",
    "CTV DRAMA CHANNEL",
    "CTV Toronto HD",
    "CTV Halifax",
    "CTV Montreal",
    "CTV Two - Ottawa",
    "CTV Ottawa",
    "CTV Calgary HD",
    "CTV Vancouver HD",
    "CTV Two - Vancouver/Victoria",
    "CTV SCI-FI CHANNEL HD",
    "KVCW-DT",
    "WPIX-DT",
    "U and Dave HD",
    "Deja View",
    "DMAX",
    "DOG TV",
    "U and Drama",
    "DTour HD",
    "E! Entertainment Television Canada",
    "UK E!",
    "E! Entertainment Television HD",
    "E4 HD",
    "UK EDEN",
    "Family Entertainment Television",
    "CA FOX EAST",
    "KCPQ-DT",
    "WNYW-DT",
    "Freeform HD",
    "Fuse HD",
    "FX HD",
    "CA FXX",
    "FXX HD",
    "FYI Channel HD",
    "GET TV",
    "Global Toronto"
]

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

print("M3U CHANNELS vs EPG STATUS")
print("=" * 50)
print()

present_count = 0
not_present_count = 0

for channel in sorted(m3u_channels):
    # Clean channel name for comparison
    clean_channel = channel.replace("CA ", "").replace("US ", "").replace("UK ", "")
    clean_channel = clean_channel.replace(" HD", "").replace(" (ASIA)", "")
    
    found = False
    for epg_channel in epg_channels:
        if clean_channel.lower() in epg_channel.lower() or epg_channel.lower() in clean_channel.lower():
            found = True
            break
    
    if found:
        print(f"✅ PRESENT: {channel}")
        present_count += 1
    else:
        print(f"❌ NOT PRESENT: {channel}")
        not_present_count += 1

print()
print("=" * 50)
print(f"SUMMARY:")
print(f"✅ Present in EPG: {present_count}")
print(f"❌ Not in EPG: {not_present_count}")
print(f"📊 Total M3U Channels: {len(m3u_channels)}")
print(f"📊 Total EPG Channels: {len(epg_channels)}")
