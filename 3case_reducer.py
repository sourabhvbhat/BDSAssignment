#!/usr/bin/python
import sys

current_date = None
total_delay = 0
flight_count = 0

# Read input line by line
for line in sys.stdin:
    line = line.strip()
    date, delay = line.split("\t")

    try:
        delay = int(delay)
    except ValueError:
        continue

    # If new date is encountered, process the previous one
    if current_date and current_date != date:
        avg_delay = total_delay / flight_count if flight_count else 0
        print(f"{current_date}\t{avg_delay}")  # Output Date -> Avg Delay
        total_delay = 0  # Reset for new date
        flight_count = 0

    current_date = date
    total_delay += delay
    flight_count += 1

# Process last date
if current_date:
    avg_delay = total_delay / flight_count if flight_count else 0
    print(f"{current_date}\t{avg_delay}")
