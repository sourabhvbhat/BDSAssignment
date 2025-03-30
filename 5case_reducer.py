#!/usr/bin/python
import sys

airport_count = {}

# Read each key-value pair from the mapper
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    airport, count = line.split("\t")

    if airport in airport_count:
        airport_count[airport] += int(count)
    else:
        airport_count[airport] = int(count)

# Sort airports by number of connections in descending order
sorted_airports = sorted(airport_count.items(), key=lambda x: x[1], reverse=True)

# Print sorted results
for airport, count in sorted_airports:
    print(f"{airport}\t{count}")

