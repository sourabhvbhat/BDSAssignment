#!/usr/bin/python3
import sys

for line in sys.stdin:
    line = line.strip()
    
    # Skip empty lines
    if not line:
        continue  

    fields = line.split(',')

    # Ensure that the first field (Date) exists and has the correct format MM-DD-YYYY
    if len(fields) > 0 and '/' in fields[0]:
        date = fields[0].strip()  # Extract date (MM/DD/YYYY)
        parts = date.split('/')

        # Ensure valid date format
        if len(parts) == 3 and parts[0].isdigit():
            month = parts[0]  # Extract month (MM)
            print(f"{month}\t1")  # Emit (month, 1)

