#!/usr/bin/env python3
"""
Time Module Examples in Python
This script demonstrates various uses of the time module
"""

import time

def basic_time_operations():
    """Demonstrate basic time operations"""
    print("=== Basic Time Operations ===")
    
    # Get current timestamp (seconds since epoch)
    current_timestamp = time.time()
    print(f"Current timestamp: {current_timestamp}")
    
    # Get current time as a struct_time object
    current_time = time.localtime()
    print(f"Current local time: {current_time}")
    
    # Get current UTC time
    utc_time = time.gmtime()
    print(f"Current UTC time: {utc_time}")
    
    # Format time as string
    formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", current_time)
    print(f"Formatted time: {formatted_time}")
    
    # Parse time string back to struct_time
    parsed_time = time.strptime("2024-01-15 14:30:00", "%Y-%m-%d %H:%M:%S")
    print(f"Parsed time: {parsed_time}")
