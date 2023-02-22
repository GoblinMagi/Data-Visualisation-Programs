# Plot the first five cubic numbers, then plot the first 5000

import matplotlib.pyplot as plt

#x_values = range(1, 6)
x_values = range(1, 5001)
y_values = [x ** 3 for x in x_values]

fig, ax = plt.subplots()

ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, linewidth=3)

ax.set_title("Cube numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

ax.tick_params(axis='both', labelsize=14)

plt.show()