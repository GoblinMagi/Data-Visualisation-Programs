# Plotting and Styling Individual Points with scatter()
import matplotlib.pyplot as plt

# Calculating Data Automatically
x_values = range(1, 1001)
# list comprehension generates values by looping through the x values
y_values = [x**2 for x in x_values]

plt.style.use('dark_background')
fig, ax = plt.subplots()

# Pass single x,y values (or a list) to points of interest to plot those values
# s argument to set the size of dots
# Using a Colourmap
# colourmap is a series of colours that moves from each point
# Pass list of values to c, and use cmap for a colourmap
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# Defining Custom Colours
# pass c to scatter() with the name of colour in quotation marks
# You can define colours with RGB colour model. Pass a tuple with three decimal
# values between 0 and 1. Closer to 0 produces dark colours

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)

# Set the range for each axis.
# axis() requires 4 values; minimum and maximum values for the x-axis and y-axis
ax.axis([0, 1100, 0, 1100000])

plt.show()

# Saving Your Plots Automatically
# Replace call to plt.show() with plt.savefig()
# First argument is a filename. This will be saved in the same directory
# Second argument trims extra whitespace. Omit if you want whitespace.
#plt.savefig('squares_plot.png', bbox_inches='tight')