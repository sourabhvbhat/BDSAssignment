#!/usr/bin/python
import sys
from collections import defaultdict

current_origin = None
destination_counts = defaultdict(int)

# Read input line by line
for line in sys.stdin:
    line = line.strip()
    key, count = line.split("\t")
    origin_airport, destination_airport = key.split(',')

    try:
        count = int(count)
    except ValueError:
        continue

    # If new origin airport is encountered, process the previous one
    if current_origin and current_origin != origin_airport:
        most_popular_dest = max(destination_counts, key=destination_counts.get)
        print(f"{current_origin}\t{most_popular_dest}")  # Output Origin -> Most Frequent Destination
        destination_counts.clear()

    current_origin = origin_airport
    destination_counts[destination_airport] += count

# Process last airport
if current_origin:
    most_popular_dest = max(destination_counts, key=destination_counts.get)
    print(f"{current_origin}\t{most_popular_dest}")
