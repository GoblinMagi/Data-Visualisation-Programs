import csv

import matplotlib.pyplot as plt
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'data/world_fires_1_day.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    lat_index = header_row.index('latitude')
    lon_index = header_row.index('longitude')
    bri_index = header_row.index('brightness')

    lats, longs, brights = [], [], []

    for row in reader:
        lats.append(float(row[lat_index]))
        longs.append(float(row[lon_index]))
        brights.append(float(row[bri_index]))

data = [{
    'type': 'scattergeo',
    'lon': longs,
    'lat': lats,
    'marker': {
        'size': [0.04*bright for bright in brights],
        'color': brights,
        'colorscale': 'Hot',
        'reversescale': True,
        'colorbar': {'title': 'Brightness'},
    },
}]

title = 'World Fires over 1 Day'
my_layout = Layout(title=title)

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='world_fires.html')