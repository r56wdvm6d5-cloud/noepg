#!/usr/bin/env python3

# Extract missing EPG channels from the full M3U list

# Full M3U channels with their stream URLs
full_m3u_channels = {
    "AurLife HD": "http://124.109.47.101/hls/stream1.m3u8",
    "US COLORS Asia": "http://tvappapk@s.rocketdns.info:8080/live/17510404/03225653/544093.m3u8",
    "US GEO KAHANI": "http://tvappapk@s.rocketdns.info:8080/live/17510404/03225653/544116.m3u8",
    "US GEO TV": "http://tvappapk@s.rocketdns.info:8080/live/17510404/03225653/544107.m3u8",
    "HarPal Geo": "https://jk3lz82elw79-hls-live.5centscdn.com/harPalGeo/955ad3298db330b5ee880c2c9e6f23a0.sdp/playlist.m3u8",
    "US HUM WORLD": "http://tvappapk@s.rocketdns.info:8080/live/17510404/03225653/544104.m3u8",
    "US HUM SITARAY": "http://tvappapk@s.rocketdns.info:8080/live/17510404/03225653/544105.m3u8",
    "US B4U MUSIC (ASIA)": "http://tvappapk@s.rocketdns.info:8080/live/17510404/03225653/544088.m3u8",
    "US MTV (ASIA)": "http://tvappapk@s.rocketdns.info:8080/live/17510404/03225653/544075.m3u8",
    "US SONY SAB": "http://tvappapk@s.rocketdns.info:8080/live/17510404/03225653/544066.m3u8",
    "US SONY SET": "http://tvappapk@s.rocketdns.info:8080/live/17510404/03225653/543984.m3u8",
    "SONY TV HD": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/47834.m3u8",
    "UK STAR PLUS": "http://tvappapk@s.rocketdns.info:8080/live/17510404/03225653/2170.m3u8",
    "A and E Canada HD": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/48376.m3u8",
    "A and E HD East": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/15966.m3u8",
    "WKBW-DT": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/40782.m3u8",
    "CA ABC WEST": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/40780.m3u8",
    "WCVB-DT": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/15956.m3u8",
    "WABC-DT": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/23363.m3u8",
    "4seven": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/47738.m3u8",
    "ABC TV": "https://c.mjh.nz/abc-nsw.m3u8",
    "ABC ME": "https://c.mjh.nz/abc-me.m3u8",
    "Antenna TV": "http://tvappapk@s.rocketdns.info:8080/live/17510404/03225653/544767.m3u8",
    "ASPiRE HD": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/48333.m3u8",
    "alibi+1": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/47739.m3u8",
    "AWE A Wealth of Entertainment HD": "http://tvappapk@s.rocketdns.info:8080/live/17510404/03225653/40582.m3u8",
    "BBC First": "http://tvappapk@s.rocketdns.info:8080/live/17510404/03225653/698467.m3u8",
    "BBC America": "https://bcovlive-a.akamaihd.net/7f5ec16d102f4b5d92e8e27bc95ff424/us-east-1/6240731308001/playlist.m3u8",
    "BBC One EastHD": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/47744.m3u8",
    "BBC Two HD": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/47745.m3u8",
    "UK BBC Three": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/47751.m3u8",
    "UK BBC Four": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/47742.m3u8",
    "BBC Drama": "https://amg00793-amg00793c40-rakuten-es-5444.playouts.now.amagi.tv/playlist.m3u8",
    "CA BET": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/40769.m3u8",
    "BET HD": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/22566.m3u8",
    "US BET HER": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/23356.m3u8",
    "US BET JAMS": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/23356.m3u8",
    "BLAZE": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/47746.m3u8",
    "Bravo HD": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/22562.m3u8",
    "Bravo PLUS 1": "https://i.mjh.nz/.r/bravo-plus1.m3u8",
    "US BOUNCE TV": "http://tvappapk@s.rocketdns.info:8080/live/17510404/03225653/21896.m3u8",
    "US BOUNCE XL": "http://tvappapk@s.rocketdns.info:8080/live/17510404/03225653/612207.m3u8",
    "CBBC HD": "http://tvappapk@s.rocketdns.info:8080/live/17510404/03225653/2321.m3u8",
    "Toon-A-Vision": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/40714.m3u8",
    "CA Disney JR": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/40723.m3u8",
    "CA Disney": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/40725.m3u8",
    "US PBS East": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/23222.m3u8",
    "CBC Calgary HD": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/40579.m3u8",
    "CBC Montreal": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/40761.m3u8",
    "CBC Ottawa": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/40759.m3u8",
    "CBC Toronto HD": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/40758.m3u8",
    "CBC Vancouver": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/40757.m3u8",
    "CBC Halifax": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/40570.m3u8",
    "WCBS-DT": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/40756.m3u8",
    "CA CBS WEST": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/40755.m3u8",
    "US CBS": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/22560.m3u8",
    "True Crime Xtra": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/47753.m3u8",
    "True Crime": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/47754.m3u8",
    "Channel 4 HD": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/47758.m3u8",
    "Channel 5 HD": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/47759.m3u8",
    "Challenge": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/47757.m3u8",
    "CHCH-DT": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/40754.m3u8",
    "Citytv Calgary": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/40578.m3u8",
    "Citytv Montreal": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/40598.m3u8",
    "Citytv Toronto HD": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/40752.m3u8",
    "Citytv Vancouver": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/40751.m3u8",
    "Cleo TV HD": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/48164.m3u8",
    "Country Music Television (CMT)": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/40750.m3u8",
    "CMT HD": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/23341.m3u8",
    "CTV COMEDY CHANNEL": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/40746.m3u8",
    "ComedyCentral": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/47761.m3u8",
    "ComedyXtra": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/47762.m3u8",
    "Comedy Central HD": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/15933.m3u8",
    "COMEDY.TV": "http://tvappapk@s.rocketdns.info:8080/live/17510404/03225653/77411.m3u8",
    "IFC HD": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/44202.m3u8",
    "Comet": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/48237.m3u8",
    "Cottage Life HD": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/40741.m3u8",
    "COZI TV": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/23337.m3u8",
    "Crave1": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/40656.m3u8",
    "Crave2": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/40655.m3u8",
    "Crave3": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/40654.m3u8",
    "Crave4": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/40653.m3u8",
    "CTV DRAMA CHANNEL": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/40766.m3u8",
    "CTV Toronto HD": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/40733.m3u8",
    "CTV Halifax": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/40595.m3u8",
    "CTV Montreal": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/40585.m3u8",
    "CTV Two - Ottawa": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/40734.m3u8",
    "CTV Ottawa": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/40731.m3u8",
    "CTV Calgary HD": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/40577.m3u8",
    "CTV Vancouver HD": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/40732.m3u8",
    "CTV Two - Vancouver/Victoria": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/40736.m3u8",
    "CTV SCI-FI CHANNEL HD": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/40620.m3u8",
    "KVCW-DT": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/15960.m3u8",
    "WPIX-DT": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/22466.m3u8",
    "U and Dave HD": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/47764.m3u8",
    "Deja View": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/40728.m3u8",
    "DMAX": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/47769.m3u8",
    "DOG TV": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/23212.m3u8",
    "U and Drama": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/47770.m3u8",
    "DTour HD": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/40720.m3u8",
    "E! Entertainment Television Canada": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/40719.m3u8",
    "UK E!": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/47771.m3u8",
    "E! Entertainment Television HD": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/15962.m3u8",
    "E4 HD": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/47772.m3u8",
    "UK EDEN": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/47773.m3u8",
    "Family Entertainment Television": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/48524.m3u8",
    "CA FOX EAST": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/40709.m3u8",
    "KCPQ-DT": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/40707.m3u8",
    "WNYW-DT": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/23322.m3u8",
    "Freeform HD": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/23313.m3u8",
    "Fuse HD": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/23312.m3u8",
    "FX HD": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/15918.m3u8",
    "CA FXX": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/48379.m3u8",
    "FXX HD": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/15917.m3u8",
    "FYI Channel HD": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/23308.m3u8",
    "GET TV": "http://tvappapk@s.rocketdns.info:8080/live/17510404/03225653/30928.m3u8",
    "Global Toronto": "http://kstv.us:8080/live/3Ha18eA6y4/Dirt$hip2786@/40703.m3u8"
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

# Channels already in present_in_epg.m3u
already_present = {
    "ABC ME", "ABC TV", "BBC One EastHD", "BBC Two HD", "Bravo HD", "Bravo PLUS 1",
    "CA ABC WEST", "CA CBS WEST", "CA FOX EAST", "CBC Calgary HD", "CBC Halifax",
    "CBC Montreal", "CBC Ottawa", "CBC Toronto HD", "CBC Vancouver", "CTV COMEDY CHANNEL",
    "CTV Calgary HD", "CTV DRAMA CHANNEL", "CTV Halifax", "CTV Montreal", "CTV Ottawa",
    "CTV SCI-FI CHANNEL HD", "CTV Toronto HD", "CTV Two - Ottawa", "CTV Two - Vancouver/Victoria",
    "CTV Vancouver HD", "Channel 4 HD", "Channel 5 HD", "Citytv Calgary", "Citytv Montreal",
    "Citytv Toronto HD", "Citytv Vancouver", "Comedy Central HD", "Crave4", "E4 HD",
    "True Crime", "True Crime Xtra", "US CBS", "US PBS East", "WABC-DT", "WCBS-DT"
}

print("#EXTM3U")
print()
print("# MISSING EPG CHANNELS FROM M3U")
print()

missing_count = 0

for epg_channel in sorted(epg_channels):
    # Skip if already present
    if epg_channel in already_present:
        continue
    
    # Look for matches in full M3U
    found_matches = []
    
    for m3u_channel, stream_url in full_m3u_channels.items():
        # Clean channel name for comparison
        clean_m3u = m3u_channel.replace("CA ", "").replace("US ", "").replace("UK ", "")
        clean_m3u = clean_m3u.replace(" HD", "").replace(" (ASIA)", "")
        
        # Check for match
        if (epg_channel.lower() == clean_m3u.lower() or 
            epg_channel.lower() in clean_m3u.lower() or 
            clean_m3u.lower() in epg_channel.lower()):
            found_matches.append((m3u_channel, stream_url))
    
    if found_matches:
        # Add all matching channels
        for m3u_channel, stream_url in found_matches:
            print(f"#EXTINF:-1 group-title=\"TV SHOWS\",{m3u_channel}")
            print(stream_url)
            print()
            missing_count += 1
    else:
        print(f"#EXTINF:-1 group-title=\"TV SHOWS\",{epg_channel}")
        print(f"# MISSING: No stream URL found for {epg_channel}")
        print()

print(f"# Total missing channels found: {missing_count}")
