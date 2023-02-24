# Parsing the CSV File Headers
# csv module in standard library parses lines in CSV files
import csv

# The datetime Module
# Convert the date string to an object representing the date using strptime()
# first argument = date, second argument = how the date is formatted
# Arguments table at the bottom of document
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:

    # Create a reader object
    reader = csv.reader(f)

    # next() returns the next line in the file when passed the reader object
    header_row = next(reader)

    # enumerate() function returns index of each item and its value
    #for index, column_header in enumerate(header_row):
    #    print(index, column_header)

    # Get dates and high temperatures from this file.
    # Create two empty lists on the same line
    dates, highs = [], []

    # reader object continues from where it left off and returns each line from
    # current position.
    for row in reader:
        # Convert row containing date data to a datetime object
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        dates.append(current_date)
        highs.append(high)

# Plot the high temperatures
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')

# Format plot.
ax.set_title("Daily high temperatures - 2018", fontsize=24)
# Set the default labels to be more readable
ax.set_xlabel('', fontsize=16)
# autofmt_dates() draws the date labels diagonally to prevent overlapping
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()

#       strptime() arguments
#   Argument       Meaning
#   %A             Weekday name, such as Monday
#   %B             Month name, such as January
#   %m             Month, as a number
#   %d             Day of the month as a number
#   %Y             Four digit year
#   %y             Two digit year
#   %H             Hour in 24 hour format
#   %I             Hour in 12 hour format
#   %p             AM or PM
#   %M             Minutes
#   %S             Seconds