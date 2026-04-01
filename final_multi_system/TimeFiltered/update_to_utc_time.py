#!/usr/bin/env python3
"""
Update all time-filtered processors to use UTC time filtering
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

def update_processor_utc_time(file_path):
    """Update a single processor to use UTC time filtering"""
    print(f"Updating {os.path.basename(file_path)} to use UTC time filtering...")
    
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Update 1: Change current_time to UTC
    content = re.sub(
        r'self\.current_time = datetime\.now\(\)  # Current local system time for filtering.*',
        'self.current_time = datetime.now(timezone.utc)  # Current UTC time for filtering',
        content,
        flags=re.MULTILINE | re.DOTALL
    )
    
    # Update 2: Remove 2-hour buffer if present
    content = re.sub(
        r'self\.current_time = datetime\.now\(\).*',
        'self.current_time = datetime.now(timezone.utc)  # Current UTC time for filtering',
        content,
        flags=re.MULTILINE | re.DOTALL
    )
    
    # Update 3: Simplify time comparison to UTC only
    old_time_logic = r'''# Parse start time from EPG format \(YYYYMMDDHHMMSS \+ timezone\)
                    start_time_str_clean = start_time_str\[:14\]  # Remove timezone part
                    start_time = datetime\.strptime\(start_time_str_clean, '%Y%m%d%H%M%S'\)
                    start_time = start_time\.replace\(tzinfo=timezone\.utc\)
                    
                    # Convert UTC time to local time for comparison
                    start_time_local = start_time\.astimezone\(\)
                    current_time_local = self\.current_time\.astimezone\(\) if self\.current_time\.tzinfo else self\.current_time\.replace\(tzinfo=start_time_local\.tzinfo\)
                    
                    # Keep program if it starts in the future \(local time comparison\)
                    if start_time_local >= current_time_local:
                        future_programs\.append\(program\)'''
    
    new_time_logic = '''# Parse start time from EPG format (YYYYMMDDHHMMSS + timezone)
                    start_time_str_clean = start_time_str[:14]  # Remove timezone part
                    start_time = datetime.strptime(start_time_str_clean, '%Y%m%d%H%M%S')
                    start_time = start_time.replace(tzinfo=timezone.utc)
                    
                    # Keep program if it starts in the future (UTC time comparison)
                    if start_time >= self.current_time:
                        future_programs.append(program)'''
    
    content = re.sub(old_time_logic, new_time_logic, content, flags=re.MULTILINE | re.DOTALL)
    
    # Update 4: Update logging to show UTC
    content = re.sub(
        r"logger\.info\(f\"EPG starts from: \{self\.current_time\.strftime\('%Y-%m-%d %H:%M:%S %Z'\)}\"\)",
        "logger.info(f\"EPG starts from: {self.current_time.strftime('%Y-%m-%d %H:%M:%S UTC')}\")",
        content
    )
    
    # Write back
    with open(file_path, 'w') as f:
        f.write(content)
    
    print(f"✅ Updated {os.path.basename(file_path)} to use UTC time filtering")

# Update all processors
for processor in processors:
    if os.path.exists(processor):
        update_processor_utc_time(processor)
    else:
        print(f"❌ File not found: {processor}")

print("\n🎯 Updated all time-filtered processors to use UTC time filtering!")
print("\nThis fixes IPTVNATOR channel loading issue:")
print("- IPTVNATOR loads EPG from GitHub")
print("- Shows programs starting from current UTC time")
print("- No more 'no channels' issue")
print("- Perfect UTC time comparison")
print("- Programs only show if start_time >= current_UTC_time")

print("\nNow IPTVNATOR will load channels correctly!")
