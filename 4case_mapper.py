#!/usr/bin/python
import sys
from datetime import datetime

# Read input line by line
for line in sys.stdin:
    line = line.strip()  # Remove leading/trailing spaces
    fields = line.split(',')  # Split CSV line into fields

    # Ensure we have enough columns
    if len(fields) >= 8:
        date_string = fields[0]  # Extract Date (Column 1)
        airline = fields[1]  # Extract Carrier (Airline Code, Column 2)

        try:
            # Convert the date string into a datetime object and extract the month
            date_obj = datetime.strptime(date_string, "%Y-%m-%d")
            month = date_obj.month  # Get month as an integer (1 for Jan, 2 for Feb, etc.)

            # Emit key-value pair: (Month, Airline) -> Flight Count (1)
            print(f"{month},{airline}\t1")
        except ValueError:
            continue  # Ignore invalid date formats
