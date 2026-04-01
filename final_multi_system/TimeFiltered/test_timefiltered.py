#!/usr/bin/env python3
"""
Test script for time-filtered processors
"""

import os
import subprocess
import sys

def test_timefiltered_processor(processor_path, config_path, output_path):
    """Test a time-filtered processor"""
    print(f"\n🧪 Testing {os.path.basename(processor_path)}...")
    
    try:
        # Run the processor
        result = subprocess.run([
            'python3', processor_path,
            '--config', config_path,
            '--output', output_path,
            '--verbose'
        ], capture_output=True, text=True, timeout=300)
        
        if result.returncode == 0:
            print(f"✅ {os.path.basename(processor_path)} executed successfully")
            
            # Check if output file exists and has content
            if os.path.exists(output_path):
                file_size = os.path.getsize(output_path)
                print(f"📄 Output file: {output_path} ({file_size:,} bytes)")
                
                # Count programs
                with open(output_path, 'r') as f:
                    content = f.read()
                    program_count = content.count('<programme')
                    channel_count = content.count('<channel')
                    print(f"📊 Channels: {channel_count}, Programs: {program_count}")
                
                return True
            else:
                print(f"❌ Output file not created: {output_path}")
                return False
        else:
            print(f"❌ {os.path.basename(processor_path)} failed")
            print(f"Error: {result.stderr}")
            return False
            
    except subprocess.TimeoutExpired:
        print(f"⏰ {os.path.basename(processor_path)} timed out")
        return False
    except Exception as e:
        print(f"💥 {os.path.basename(processor_path)} error: {e}")
        return False

def main():
    """Main test function"""
    print("🚀 Testing Time-Filtered EPG Processors")
    print("=" * 50)
    
    # Define processors to test
    base_path = "/Users/ah/CascadeProjects/windsurf-project/final_multi_system/TimeFiltered"
    output_base = "/Users/ah/CascadeProjects/windsurf-project/final_multi_system/TimeFiltered/Github_TimeFiltered"
    
    # Ensure output directory exists
    os.makedirs(output_base, exist_ok=True)
    
    tests = [
        {
            'processor': f"{base_path}/multi_processor_timefiltered/multi_xml_processor_timefiltered.py",
            'config': f"{base_path}/config_timefiltered/multi_xml_config_timefiltered.txt",
            'output': f"{output_base}/epg_combined_timefiltered.xml"
        },
        {
            'processor': f"{base_path}/DOC2_timefiltered/Doc2_multi_xml_processor_timefiltered.py",
            'config': f"{base_path}/config_timefiltered/Doc2_config_timefiltered.txt",
            'output': f"{output_base}/DOC2_epg_timefiltered.xml"
        }
    ]
    
    results = []
    
    for test in tests:
        success = test_timefiltered_processor(
            test['processor'], 
            test['config'], 
            test['output']
        )
        results.append((test['processor'], success))
    
    # Summary
    print("\n" + "=" * 50)
    print("📋 TEST SUMMARY")
    print("=" * 50)
    
    passed = sum(1 for _, success in results if success)
    total = len(results)
    
    for processor, success in results:
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{status} {os.path.basename(processor)}")
    
    print(f"\n🎯 Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All time-filtered processors working correctly!")
        return 0
    else:
        print("⚠️  Some processors failed - check logs above")
        return 1

if __name__ == "__main__":
    exit(main())
