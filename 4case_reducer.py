#!/usr/bin/python
import sys

current_key = None
flight_count = 0

# Read input line by line
for line in sys.stdin:
    line = line.strip()
    key, count = line.split("\t")  # key = "Month,Airline"

    try:
        count = int(count)
    except ValueError:
        continue  # Ignore invalid data

    # If a new key (Month, Airline) is encountered, process the previous one
    if current_key and current_key != key:
        print(f"{current_key}\t{flight_count}")  # Output (Month, Airline) and Flight Count
        flight_count = 0  # Reset for new key

    current_key = key
    flight_count += count

# Process last key
if current_key:
    print(f"{current_key}\t{flight_count}")
