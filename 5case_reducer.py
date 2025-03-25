#!/usr/bin/python
import sys

current_airport = None
destination_set = set()

# Read input line by line
for line in sys.stdin:
    line = line.strip()
    origin_airport, destination_airport = line.split("\t")

    # If a new airport is encountered, process the previous one
    if current_airport and current_airport != origin_airport:
        print(f"{current_airport}\t{len(destination_set)}")  # Output (Airport -> Unique Destinations)
        destination_set.clear()  # Reset for new airport

    current_airport = origin_airport
    destination_set.add(destination_airport)

# Process last airport
if current_airport:
    print(f"{current_airport}\t{len(destination_set)}")
