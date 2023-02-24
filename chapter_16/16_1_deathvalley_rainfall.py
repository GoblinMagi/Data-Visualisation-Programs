import csv
from datetime import datetime
import matplotlib.pyplot as plt 

filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    dates, rain_level = [], []

    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        rain = float(row[3])
        dates.append(current_date)
        rain_level.append(rain)

plt.style.use('dark_background')
fig, ax = plt.subplots()
ax.plot(dates, rain_level, c='blue')

ax.set_title('Daily rainfall in Death Valley - 2018', fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel('Rainfall amount', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()