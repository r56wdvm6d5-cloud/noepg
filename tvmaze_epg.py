import requests
from datetime import datetime, timedelta
import pytz
import xml.etree.ElementTree as ET
import re
import time
import logging
from typing import List, Dict, Optional

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# CONFIGURATION
TIMEZONE = pytz.timezone("US/Eastern")
DAYS = 7  # One week of data
COUNTRIES = ["US", "GB", "CA", "AU", "NZ"]
# Expanded list of channels from TVMAZE API
TARGET_CHANNELS = [
    # US Major Networks
    "ABC", "NBC", "CBS", "FOX", "The CW",
    
    # US News Channels
    "CNN", "Fox News Channel", "MS NOW", "NewsNation", "CNBC",
    
    # US Cable Channels
    "ESPN", "Comedy Central", "Bravo", "A&E", "History", "Discovery", 
    "National Geographic", "PBS", "Syndication", "NFL Network",
    
    # US Premium Networks (HBO, STARZ, etc.)
    "HBO", "HBO2", "HBOMax", "STARZ", "Showtime", "Showtime Encore",
    "Cinemax", "Epix", "Flix", "The Movie Channel",
    
    # UK Channels
    "BBC One", "BBC Two", "BBC Alba", "ITV1", "Channel 4", "E4", "5",
    "Sky Arts", "BBC iPlayer", "ITVX",
    
    # UK Streaming/Web Channels
    "Channel 4", "TRUE CRIME", "Quest",
    
    # Australian Channels (when available)
    "ABC", "Seven Network", "Nine Network", "Network 10", "SBS",
    
    # New Zealand Channels (when available)
    "TVNZ", "Three", "Prime", "Māori Television",
    
    # Canadian Channels
    "Global", "CTV", "CBC", "Citytv"
]
BASE_URL = "https://api.tvmaze.com/schedule"
REQUEST_DELAY = 0.1  # Delay between requests to respect rate limits
OUTPUT_FILE = "epg.xml"

class TVMazeEPG:
    def __init__(self, config: Optional[Dict] = None):
        self.config = config or {
            'timezone': TIMEZONE,
            'days': DAYS,
            'countries': COUNTRIES,
            'target_channels': TARGET_CHANNELS,
            'base_url': BASE_URL,
            'request_delay': REQUEST_DELAY,
            'output_file': OUTPUT_FILE
        }
        self.programs = []
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': 'TVMaze-EPG-Generator/1.0'})

    def clean_html(self, raw_html: str) -> str:
        """Remove HTML tags from descriptions"""
        if not raw_html:
            return ""
        clean = re.compile("<.*?>")
        return re.sub(clean, "", raw_html).strip()

    def fetch_schedule_for_date(self, country: str, date: str) -> List[Dict]:
        """Fetch schedule for a specific country and date"""
        url = f"{self.config['base_url']}?country={country}&date={date}"
        
        try:
            logger.info(f"Fetching: {country} {date}")
            response = self.session.get(url, timeout=30)
            response.raise_for_status()
            
            time.sleep(self.config['request_delay'])
            return response.json()
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching {country} {date}: {e}")
            return []
        except ValueError as e:
            logger.error(f"JSON parsing error for {country} {date}: {e}")
            return []

    def parse_program_data(self, item: Dict, country: str) -> Optional[Dict]:
        """Parse individual program data from API response"""
        show = item.get("show", {})
        network = show.get("network")
        
        if not network:
            return None
        
        channel_name = network.get("name")
        
        # Filter by target channels if specified
        if self.config['target_channels'] and channel_name not in self.config['target_channels']:
            return None
        
        airtime = item.get("airtime")
        airdate = item.get("airdate")
        
        if not airtime or not airdate:
            return None
        
        try:
            dt_str = f"{airdate} {airtime}"
            start = datetime.strptime(dt_str, "%Y-%m-%d %H:%M")
            start = self.config['timezone'].localize(start)
        except ValueError as e:
            logger.warning(f"Date parsing error: {e}")
            return None
        
        duration = item.get("runtime") or 60
        stop = start + timedelta(minutes=duration)
        
        summary = self.clean_html(show.get("summary") or "")
        
        return {
            "channel": f"{channel_name}.{country}",
            "title": show.get("name", "No Title"),
            "desc": summary,
            "start": start,
            "stop": stop,
            "country": country,
            "original_channel": channel_name
        }

    def fetch_schedule(self) -> List[Dict]:
        """Fetch schedule for all configured countries and days"""
        programs = []
        total_requests = len(self.config['countries']) * self.config['days']
        current_request = 0
        
        for country in self.config['countries']:
            for i in range(self.config['days']):
                date = (datetime.utcnow() + timedelta(days=i)).strftime("%Y-%m-%d")
                current_request += 1
                
                logger.info(f"Request {current_request}/{total_requests}")
                
                data = self.fetch_schedule_for_date(country, date)
                
                for item in data:
                    program = self.parse_program_data(item, country)
                    if program:
                        programs.append(program)
        
        logger.info(f"Total programs fetched: {len(programs)}")
        return programs

    def create_xmltv(self, programs: List[Dict]) -> None:
        """Create XMLTV format file from programs"""
        if not programs:
            logger.warning("No programs to write to XML")
            return
        
        tv = ET.Element("tv")
        tv.set("generator-info-name", "TVMaze EPG Generator")
        tv.set("generator-info-url", "https://www.tvmaze.com/api")
        
        # Add channels
        channels_added = {}
        for prog in programs:
            channel_id = prog["channel"]
            if channel_id not in channels_added:
                channel = ET.SubElement(tv, "channel", id=channel_id)
                display_name = ET.SubElement(channel, "display-name")
                display_name.text = prog["original_channel"]
                
                # Add country info
                country_elem = ET.SubElement(channel, "country")
                country_elem.text = prog["country"]
                
                channels_added[channel_id] = True
        
        # Add programs
        for prog in programs:
            start_time = prog["start"].strftime("%Y%m%d%H%M%S %z")
            stop_time = prog["stop"].strftime("%Y%m%d%H%M%S %z")
            
            programme = ET.SubElement(tv, "programme", {
                "start": start_time,
                "stop": stop_time,
                "channel": prog["channel"]
            })
            
            title = ET.SubElement(programme, "title")
            title.text = prog["title"]
            
            desc = ET.SubElement(programme, "desc")
            desc.text = prog["desc"]
            
            # Add additional metadata
            category = ET.SubElement(programme, "category")
            category.text = "TV Show"
            
            # Add episode info if available
            if prog.get("episode"):
                episode_num = ET.SubElement(programme, "episode-num")
                episode_num.text = prog["episode"]
        
        # Pretty print XML
        ET.indent(tv, space="  ")
        tree = ET.ElementTree(tv)
        tree.write(self.config['output_file'], encoding="utf-8", xml_declaration=True)
        logger.info(f"XMLTV file saved as: {self.config['output_file']}")

    def generate_epg(self) -> bool:
        """Main method to generate EPG"""
        try:
            logger.info("Starting EPG generation...")
            
            programs = self.fetch_schedule()
            
            if not programs:
                logger.warning("No programs fetched!")
                return False
            
            self.create_xmltv(programs)
            logger.info(f"✅ EPG generation complete. Programs: {len(programs)}")
            return True
            
        except Exception as e:
            logger.error(f"Error during EPG generation: {e}")
            return False

def main():
    """Main function with example usage"""
    # Custom configuration example with expanded channels
    custom_config = {
        'timezone': pytz.timezone("US/Eastern"),
        'days': 7,  # One week of data
        'countries': ["US", "GB", "CA", "AU", "NZ"],  # All supported countries
        'target_channels': [
            # US Major Networks
            "ABC", "NBC", "CBS", "FOX", "The CW",
            
            # US News Channels
            "CNN", "Fox News Channel", "MS NOW", "Newsmax", "NewsNation", "CNBC",
            
            # US Cable Channels
            "ESPN", "Comedy Central", "Bravo", "A&E", "History", "Discovery", 
            "National Geographic", "PBS", "Syndication", "NFL Network",
            
            # US Premium Networks (HBO, STARZ, etc.)
            "HBO", "HBO2", "HBOMax", "STARZ", "Showtime", "Showtime Encore",
            "Cinemax", "Epix", "Flix", "The Movie Channel",
            
            # UK Channels
            "BBC One", "BBC Two", "BBC Alba", "ITV1", "Channel 4", "E4", "5",
            "Sky Arts", "TRUE CRIME", "Quest",
            
            # Canadian Channels
            "Global", "CTV", "CBC", "Citytv"
        ],
        'base_url': "https://api.tvmaze.com/schedule",
        'request_delay': 0.1,
        'output_file': "epg.xml"
    }
    
    # Create EPG generator instance
    epg_generator = TVMazeEPG(custom_config)
    
    # Generate EPG
    success = epg_generator.generate_epg()
    
    if success:
        print("🎉 EPG generation completed successfully!")
    else:
        print("❌ EPG generation failed. Check logs for details.")

if __name__ == "__main__":
    main()
