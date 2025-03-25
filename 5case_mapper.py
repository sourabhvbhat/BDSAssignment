#!/usr/bin/python
import sys

# Read input line by line
for line in sys.stdin:
    line = line.strip()  # Remove leading/trailing spaces
    fields = line.split(',')  # Split CSV line into fields

    # Ensure we have enough columns
    if len(fields) >= 6:
        origin_airport = fields[3]  # Extract OriginAirportID (Column 4)
        destination_airport = fields[5]  # Extract DestAirportID (Column 6)

        # Emit key-value pair: OriginAirportID -> DestinationAirportID
        print(f"{origin_airport}\t{destination_airport}")
