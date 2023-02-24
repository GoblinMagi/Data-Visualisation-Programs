import csv
from datetime import datetime
import matplotlib.pyplot as plt

#filename = 'data/3245179.csv'
#filename = 'data/death_valley_2018_simple.csv'
filename = 'data/sitka_weather_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    date_index = header_row.index('DATE')
    high_index = header_row.index('TMAX')
    low_index = header_row.index('TMIN')
    name_index = header_row.index('NAME')

    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
        try:
            high = int(row[high_index])
            low = int(row[low_index])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
            name = row[name_index].title()

plt.style.use('dark_background')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')
ax.plot(dates, lows, c='blue')

title = f"Daily Temperatures for {name}. - 2018"
ax.set_title(title, fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel('Temperatures (F)', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()