#!/usr/bin/python3
import sys

for line in sys.stdin:
    line = line.strip()
    fields = line.split(',')

    if len(fields) >= 8:  # Ensure the line has enough fields
        airline = fields[1]  # Airline code (assuming 2nd column is airline)
        dep_delay = fields[6]  # Departure delay
        arr_delay = fields[7]  # Arrival delay

        # Convert delays to integers, default to 0 if invalid or negative
        try:
            dep_delay = int(dep_delay) if dep_delay.isdigit() and int(dep_delay) >= 0 else 0
            arr_delay = int(arr_delay) if arr_delay.isdigit() and int(arr_delay) >= 0 else 0
            total_delay = dep_delay + arr_delay  # Total delay for the airline

            if total_delay > 0:
                print(f"{airline}\t{total_delay}\t1")  # Airline -> Delay, Count

        except ValueError:
            continue  # Skip invalid records

