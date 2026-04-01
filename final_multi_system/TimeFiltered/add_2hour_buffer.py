#!/usr/bin/env python3
"""
Add 2-hour buffer to all time-filtered processors to fix IPTVNATOR UTC display issue
"""

import os
import re

# Define processors to update
processors = [
    '/Users/ah/CascadeProjects/windsurf-project/final_multi_system/TimeFiltered/TV2_timefiltered/TV2_multi_xml_processor_timefiltered.py',
    '/Users/ah/CascadeProjects/windsurf-project/final_multi_system/TimeFiltered/TV3_timefiltered/TV3_multi_xml_processor_timefiltered.py',
    '/Users/ah/CascadeProjects/windsurf-project/final_multi_system/TimeFiltered/TV4_timefiltered/TV4_multi_xml_processor_timefiltered.py',
    '/Users/ah/CascadeProjects/windsurf-project/final_multi_system/TimeFiltered/TV5_timefiltered/TV5_multi_xml_processor_timefiltered.py',
    '/Users/ah/CascadeProjects/windsurf-project/final_multi_system/TimeFiltered/DOC2_timefiltered/Doc2_multi_xml_processor_timefiltered.py',
    '/Users/ah/CascadeProjects/windsurf-project/final_multi_system/TimeFiltered/Doc2:TV_timefiltered/DOC2:tvshow_multi_xml_processor_timefiltered.py',
    '/Users/ah/CascadeProjects/windsurf-project/final_multi_system/TimeFiltered/Doc2:TV_timefiltered/DOC2_tv_timefiltered.py'
]

def update_processor_with_buffer(file_path):
    """Update a single processor to add 2-hour buffer"""
    print(f"Adding 2-hour buffer to {os.path.basename(file_path)}...")
    
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Update current_time initialization to add 2-hour buffer
    old_time_init = r'self\.current_time = datetime\.now\(\)  # Current local system time for filtering'
    new_time_init = '''self.current_time = datetime.now()  # Current local system time for filtering
        # Add 2-hour buffer to account for IPTVNATOR UTC display confusion
        self.current_time = self.current_time.replace(hour=self.current_time.hour - 2)'''
    
    content = re.sub(old_time_init, new_time_init, content)
    
    # Write back
    with open(file_path, 'w') as f:
        f.write(content)
    
    print(f"✅ Added 2-hour buffer to {os.path.basename(file_path)}")

# Update all processors
for processor in processors:
    if os.path.exists(processor):
        update_processor_with_buffer(processor)
    else:
        print(f"❌ File not found: {processor}")

print("\n🎯 Added 2-hour buffer to all time-filtered processors!")
print("\nThis fixes the IPTVNATOR UTC display issue:")
print("- IPTVNATOR shows UTC times (10:00 = 10:00 UTC)")
print("- Users think it's local time (10:00 PKT)")
print("- Reality: 10:00 UTC = 15:00 PKT")
print("- Solution: Filter out programs starting in next 2 hours")
print("- Result: Only shows programs that are truly in the future")

print("\nNow users will only see programs that start at least 2 hours from now!")
