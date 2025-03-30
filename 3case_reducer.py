#!/usr/bin/python3
import sys

current_airport = None
total_delay = 0
flight_count = 0
airport_delays = []  # Store (airport, avg_delay) pairs

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue  # Ignore empty lines

    try:
        airport, delay, count = line.split("\t")
        delay = int(delay)
        count = int(count)

        if current_airport == airport:
            total_delay += delay
            flight_count += count
        else:
            if current_airport is not None and flight_count > 0:
                avg_delay = total_delay / flight_count
                airport_delays.append((current_airport, avg_delay))  # Store result

            current_airport = airport
            total_delay = delay
            flight_count = count

    except ValueError:
        continue  # Ignore invalid data

# Add the last airport's average delay
if current_airport and flight_count > 0:
    avg_delay = total_delay / flight_count
    airport_delays.append((current_airport, avg_delay))

# Sort by average delay in descending order
airport_delays.sort(key=lambda x: x[1], reverse=True)

# Print the sorted results
for airport, avg_delay in airport_delays:
    print(f"{airport}\t{avg_delay:.2f}")

