# Making a Histogram
# a 'histogram' is a bar chart showing how often certain results occur
from plotly.graph_objs import Bar, Layout
from plotly import offline

# Rolling the Die
from die import Die

# Create a D6 and a D10.
die_1 = Die()
die_2 = Die(10)

# Make some rolls, and store the results in a list.
results = []
for roll_num in range(50_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyse the results.
frequencies = []

# Maximum result of rolling two die is 12
max_result = die_1.num_sides + die_2.num_sides

# Loop through possible values (1 through 6, etc) and count how many times each 
# appear
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualise the results.
# Plotly doesn't accept range() directly, needs to be converted to a list
x_values = list(range(2, max_result+1))

# Bar() class represents data set that will be formatted as a chart
# Must be wrapped in square brackets because a data set can have multiple
# elements
data = [Bar(x=x_values, y=frequencies)]

# Each axis can be configured in multiple ways, stored as a dictionary
# dtick controls the spacing between tickmarks. 1 tells Plotly to tick all
x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}

# Layout() class returns an object that specifies layout of graph as a whole
my_layout = Layout(title='Results of rolling a D6 and a D10 50000 times', 
    xaxis=x_axis_config, yaxis=y_axis_config)

# offline.plot() generates the plot containing data and layout objects
# accepts a name where the graph will be saved.
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d10.html')