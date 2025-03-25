#!/usr/bin/python
import sys

# Read input line by line
for line in sys.stdin:
    line = line.strip()
    fields = line.split(',')

    if len(fields) >= 6:
        origin_airport = fields[3]  # OriginAirportID
        destination_airport = fields[5]  # DestAirportID

        # Emit key-value pair: OriginAirportID -> DestAirportID
        print(f"{origin_airport},{destination_airport}\t1")
