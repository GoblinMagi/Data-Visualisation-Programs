# Plotting a Simple Line Graph
import matplotlib.pyplot as plt 

# Hold the data that we plot
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

# Generate a plot using subplots()
# fig represents the entire figure or collection of plots generated.
# ax represents a single plot
fig, ax = plt.subplots()

# Using Built-in Styles
plt.style.use('seaborn-v0_8')

# Changing the Label Type and Line Thickness
# linewidth parameter controls thickness of the line that plot() generates
# plot() assumes first data point has x-coord of 0
# Override this by providing input and output values
ax.plot(input_values, squares, linewidth=3)

# Set chart title and label axes.
ax.set_title("Square numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis='both', labelsize=14)

# Open the viewer and display the plot
plt.show()