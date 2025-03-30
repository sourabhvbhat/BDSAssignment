#!/usr/bin/python3
import sys

current_airline = None
total_delay = 0
flight_count = 0
airline_delays = []  # Store (airline, avg_delay) pairs

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue  # Ignore empty lines

    try:
        airline, delay, count = line.split("\t")
        delay = int(delay)
        count = int(count)

        if current_airline == airline:
            total_delay += delay
            flight_count += count
        else:
            if current_airline is not None and flight_count > 0:
                avg_delay = total_delay / flight_count
                airline_delays.append((current_airline, avg_delay))  # Store result

            current_airline = airline
            total_delay = delay
            flight_count = count

    except ValueError:
        continue  # Ignore invalid data

# Add the last airline's average delay
if current_airline and flight_count > 0:
    avg_delay = total_delay / flight_count
    airline_delays.append((current_airline, avg_delay))

# Sort airlines by average delay in descending order
airline_delays.sort(key=lambda x: x[1], reverse=True)

# Print sorted results
for airline, avg_delay in airline_delays:
    print(f"{airline}\t{avg_delay:.2f}")

