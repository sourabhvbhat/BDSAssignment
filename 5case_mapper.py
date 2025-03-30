#!/usr/bin/python
import sys

# Read input line by line
for line in sys.stdin:
    line = line.strip()  # Remove leading/trailing whitespace

    if not line or line.startswith("Date"):  # Skip empty lines and header
        continue

    fields = line.split(',')

    if len(fields) >= 6:  # Ensure valid data
        origin_airport = fields[2].strip()  # OriginAirportName
        dest_airport = fields[4].strip()  # DestAirportName

        # Emit both origin and destination airports with a count of 1
        if origin_airport:
            print(f"{origin_airport}\t1")
        if dest_airport:
            print(f"{dest_airport}\t1")

