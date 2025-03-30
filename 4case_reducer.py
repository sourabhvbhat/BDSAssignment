#!/usr/bin/python3
import sys

current_month = None
flight_count = 0
monthly_trends = []  # Store (month, count) pairs

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue  # Ignore empty lines

    try:
        month, count = line.split("\t")
        count = int(count)

        if current_month == month:
            flight_count += count
        else:
            if current_month is not None:
                monthly_trends.append((current_month, flight_count))  # Store result
            
            current_month = month
            flight_count = count

    except ValueError:
        continue  # Ignore invalid data

# Add the last month's data
if current_month:
    monthly_trends.append((current_month, flight_count))

# Sort months in ascending order (Jan to Dec)
monthly_trends.sort(key=lambda x: int(x[0]))

# Print results
for month, count in monthly_trends:
    print(f"{month}\t{count}")

