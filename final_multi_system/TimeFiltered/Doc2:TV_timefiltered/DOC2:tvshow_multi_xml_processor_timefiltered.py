#!/usr/bin/env python3
"""
Multi-XML Processor with Auto-Date Update
Fetches and combines multiple XML sources into one EPG file
"""

import argparse
import xml.etree.ElementTree as ET
import xml.dom.minidom
import requests
import requests.adapters
import re
from datetime import datetime, timezone
import os
import logging
from typing import List, Dict, Any
import time

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class MultiXMLProcessor:
    """Process multiple XML sources and combine them into one EPG file."""
    
    def __init__(self):
        self.channels = {}
        self.programs = []
        self.max_programs = 900  # Maximum programs cap
        self.max_programs_per_channel = 100  # Early limiting for faster loading
        
        # Setup connection pooling for faster HTTP requests
        self.session = requests.Session()
        adapter = requests.adapters.HTTPAdapter(
            pool_connections=20,
            pool_maxsize=20,
            max_retries=3,
            pool_block=False
        )
        self.session.mount('http://', adapter)
        self.session.mount('https://', adapter)
        self.current_time = datetime.now(timezone.utc)  # Current UTC time for filtering