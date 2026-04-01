#!/usr/bin/env python3
"""
EPG Streaming Server for GitHub Pages
Streams EPG content like the original source
"""

import urllib.request
import sys

def stream_epg():
    """Stream EPG content directly"""
    try:
        # Stream from original EPG source
        with urllib.request.urlopen('https://epg.pw/xmltv/epg_GB.xml') as response:
            # Set headers for streaming
            sys.stdout.write('Content-Type: application/xml\n\n')
            sys.stdout.flush()
            
            # Stream content in chunks
            while True:
                chunk = response.read(8192)
                if not chunk:
                    break
                sys.stdout.buffer.write(chunk)
                sys.stdout.flush()
                
    except Exception as e:
        sys.stdout.write(f'Error: {e}')

if __name__ == "__main__":
    stream_epg()
