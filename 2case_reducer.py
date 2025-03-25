#!/usr/bin/python
import sys

current_airline = None
total_delay = 0

# Read input line by line
for line in sys.stdin:
    line = line.strip()
    airline, delay = line.split("\t")

    try:
        delay = int(delay)
    except ValueError:
        continue

    # If new airline is encountered, process the previous one
    if current_airline and current_airline != airline:
        print(f"{current_airline}\t{total_delay}")  # Output Airline -> Total Delay
        total_delay = 0  # Reset for new airline

    current_airline = airline
    total_delay += delay

# Process last airline
if current_airline:
    print(f"{current_airline}\t{total_delay}")
