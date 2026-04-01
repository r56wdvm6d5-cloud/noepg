#!/usr/bin/env python3
"""
Batch script to create time-filtered processors
"""

import os
import shutil

# Define processors to create
processors = [
    {
        'source': '/Users/ah/CascadeProjects/windsurf-project/final_multi_system/TV2/TV2 multi_processor/TV2 multi_xml_processor.py',
        'dest': '/Users/ah/CascadeProjects/windsurf-project/final_multi_system/TimeFiltered/TV2_timefiltered/TV2_multi_xml_processor_timefiltered.py',
        'config_source': '/Users/ah/CascadeProjects/windsurf-project/final_multi_system/TV2/TV2 config_txt/TV2.txt',
        'config_dest': '/Users/ah/CascadeProjects/windsurf-project/final_multi_system/TimeFiltered/config_timefiltered/TV2_config_timefiltered.txt',
        'name': 'TV2-Multi-XML-Processor-TimeFiltered'
    },
    {
        'source': '/Users/ah/CascadeProjects/windsurf-project/final_multi_system/TV3/TV3 multi_processor/TV3 multi_xml_processor.py',
        'dest': '/Users/ah/CascadeProjects/windsurf-project/final_multi_system/TimeFiltered/TV3_timefiltered/TV3_multi_xml_processor_timefiltered.py',
        'config_source': '/Users/ah/CascadeProjects/windsurf-project/final_multi_system/TV3/TV3 config_txt/TV3.txt',
        'config_dest': '/Users/ah/CascadeProjects/windsurf-project/final_multi_system/TimeFiltered/config_timefiltered/TV3_config_timefiltered.txt',
        'name': 'TV3-Multi-XML-Processor-TimeFiltered'
    },
    {
        'source': '/Users/ah/CascadeProjects/windsurf-project/final_multi_system/TV4/TV4 multi_processor/TV4 multi_xml_processor.py',
        'dest': '/Users/ah/CascadeProjects/windsurf-project/final_multi_system/TimeFiltered/TV4_timefiltered/TV4_multi_xml_processor_timefiltered.py',
        'config_source': '/Users/ah/CascadeProjects/windsurf-project/final_multi_system/TV4/TV4 config_txt/TV4.txt',
        'config_dest': '/Users/ah/CascadeProjects/windsurf-project/final_multi_system/TimeFiltered/config_timefiltered/TV4_config_timefiltered.txt',
        'name': 'TV4-Multi-XML-Processor-TimeFiltered'
    },
    {
        'source': '/Users/ah/CascadeProjects/windsurf-project/final_multi_system/TV5/TV5 multi_processor/TV5 multi_xml_processor.py',
        'dest': '/Users/ah/CascadeProjects/windsurf-project/final_multi_system/TimeFiltered/TV5_timefiltered/TV5_multi_xml_processor_timefiltered.py',
        'config_source': '/Users/ah/CascadeProjects/windsurf-project/final_multi_system/TV5/TV5 config_txt/TV5.txt',
        'config_dest': '/Users/ah/CascadeProjects/windsurf-project/final_multi_system/TimeFiltered/config_timefiltered/TV5_config_timefiltered.txt',
        'name': 'TV5-Multi-XML-Processor-TimeFiltered'
    },
    {
        'source': '/Users/ah/CascadeProjects/windsurf-project/final_multi_system/DOC2/Doc2 multi_processor/Doc2_multi_xml_processor.py',
        'dest': '/Users/ah/CascadeProjects/windsurf-project/final_multi_system/TimeFiltered/DOC2_timefiltered/Doc2_multi_xml_processor_timefiltered.py',
        'config_source': '/Users/ah/CascadeProjects/windsurf-project/final_multi_system/Doc2/Doc2 config_txt/Doc2_multi_xml_config.txt',
        'config_dest': '/Users/ah/CascadeProjects/windsurf-project/final_multi_system/TimeFiltered/config_timefiltered/Doc2_config_timefiltered.txt',
        'name': 'DOC2-Multi-XML-Processor-TimeFiltered'
    },
    {
        'source': '/Users/ah/CascadeProjects/windsurf-project/final_multi_system/Doc2:TV/DOC2:tvshow multi_processor/DOC2:tvshow multi_xml_processor.py',
        'dest': '/Users/ah/CascadeProjects/windsurf-project/final_multi_system/TimeFiltered/Doc2:TV_timefiltered/DOC2:tvshow_multi_xml_processor_timefiltered.py',
        'config_source': '/Users/ah/CascadeProjects/windsurf-project/final_multi_system/Doc2:TV/DOC2:tvshow config_txt/DOC2:tvshow_multi_xml_config.txt',
        'config_dest': '/Users/ah/CascadeProjects/windsurf-project/final_multi_system/TimeFiltered/config_timefiltered/DOC2:tvshow_config_timefiltered.txt',
        'name': 'DOC2:TVSHOW-Multi-XML-Processor-TimeFiltered'
    }
]

# Template for adding time filtering
time_filtering_code = '''
        self.current_time = datetime.now(timezone.utc)  # Current UTC time for filtering
'''

filter_method_code = '''
    def filter_future_programs(self) -> None:
        """Filter out programs that have already aired (start time before current time)."""
        original_count = len(self.programs)
        future_programs = []
        
        for program in self.programs:
            start_time_str = program.get('start')
            if start_time_str:
                try:
                    # Parse start time from EPG format (YYYYMMDDHHMMSS + timezone)
                    start_time_str_clean = start_time_str[:14]  # Remove timezone part
                    start_time = datetime.strptime(start_time_str_clean, '%Y%m%d%H%M%S')
                    start_time = start_time.replace(tzinfo=timezone.utc)
                    
                    # Keep program if it starts in the future
                    if start_time >= self.current_time:
                        future_programs.append(program)
                except (ValueError, TypeError) as e:
                    # If we can't parse the time, keep the program (safe fallback)
                    future_programs.append(program)
                    logger.warning(f"Could not parse start time '{start_time_str}' for program, keeping it: {e}")
            else:
                # If no start time, keep the program (safe fallback)
                future_programs.append(program)
        
        filtered_count = len(future_programs)
        removed_count = original_count - filtered_count
        
        self.programs = future_programs
        logger.info(f"Time filtering: {original_count} -> {filtered_count} programs (removed {removed_count} past programs)")
        logger.info(f"EPG starts from: {self.current_time.strftime('%Y-%m-%d %H:%M:%S UTC')}")
'''

process_sources_update = '''
            # Apply time filtering first
            self.filter_future_programs()
            
            # Apply program limiting
            self.limit_programs_equally()
'''

for proc in processors:
    print(f"Processing {proc['name']}...")
    
    # Read source file
    with open(proc['source'], 'r') as f:
        content = f.read()
    
    # Add timezone import
    content = content.replace(
        'from datetime import datetime',
        'from datetime import datetime, timezone'
    )
    
    # Add current_time to __init__
    content = content.replace(
        '        self.session.mount(\'https://\', adapter)',
        '        self.session.mount(\'https://\', adapter)\n        self.current_time = datetime.now(timezone.utc)  # Current UTC time for filtering'
    )
    
    # Add filter method before limit_programs_equally
    content = content.replace(
        '    def limit_programs_equally(self) -> None:',
        filter_method_code + '\n    def limit_programs_equally(self) -> None:'
    )
    
    # Update process_multiple_sources to call filter_future_programs
    content = content.replace(
        '            # Apply program limiting\n            self.limit_programs_equally()',
        '            # Apply time filtering first\n            self.filter_future_programs()\n            \n            # Apply program limiting\n            self.limit_programs_equally()'
    )
    
    # Update generator name
    content = content.replace(
        "generator-info-name', 'Multi-XML-Processor'",
        f"generator-info-name', '{proc['name']}'"
    )
    
    # Update source info name
    content = content.replace(
        "source-info-name', 'Multi-Source-EPG'",
        f"source-info-name', '{proc['name']}-Source-EPG'"
    )
    
    # Write to destination
    with open(proc['dest'], 'w') as f:
        f.write(content)
    
    # Copy config file
    shutil.copy2(proc['config_source'], proc['config_dest'])
    
    print(f"✅ Created {proc['name']}")

print("🎉 All time-filtered processors created successfully!")
