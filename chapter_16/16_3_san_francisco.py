import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'data/3245179.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []

    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[-2])
        low = int(row[-1])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

plt.style.use('dark_background')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')
ax.plot(dates, lows, c='blue')

ax.set_title('Daily Temperatures for San Fransico - 2018', fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel('Temperatures (F)', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()