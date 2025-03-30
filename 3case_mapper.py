#!/usr/bin/python3
import sys

for line in sys.stdin:
    line = line.strip()
    fields = line.split(',')

    # Ensure the row has enough columns
    if len(fields) < 8:
        continue

    airport = fields[4].strip()  # Origin Airport
    dep_delay = fields[6].strip()  # DepDelay
    arr_delay = fields[7].strip()  # ArrDelay

    try:
        dep_delay = int(dep_delay) if dep_delay.lstrip('-').isdigit() else None
        arr_delay = int(arr_delay) if arr_delay.lstrip('-').isdigit() else None

        # Ignore negative delays and None values
        if dep_delay is not None and dep_delay >= 0 and arr_delay is not None and arr_delay >= 0:
            total_delay = dep_delay + arr_delay
            print(f"{airport}\t{total_delay}\t1")  # Emit: airport \t delay \t count

    except ValueError:
        continue  # Ignore lines with conversion errors

