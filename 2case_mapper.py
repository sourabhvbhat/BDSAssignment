#!/usr/bin/python
import sys

# Read input line by line
for line in sys.stdin:
    line = line.strip()
    fields = line.split(',')

    if len(fields) >= 8:
        airline = fields[1]  # Carrier (Airline)
        dep_delay = fields[6]  # DepDelay
        arr_delay = fields[7]  # ArrDelay

        # Convert delays to integers, default to 0 if invalid
        try:
            dep_delay = int(dep_delay) if dep_delay.isdigit() else 0
            arr_delay = int(arr_delay) if arr_delay.isdigit() else 0
            total_delay = dep_delay + arr_delay  # Total delay per flight

            # Emit key-value pair: Airline -> DelayTime
            print(f"{airline}\t{total_delay}")
        except ValueError:
            continue
