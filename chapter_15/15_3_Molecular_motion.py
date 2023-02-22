import matplotlib.pyplot as plt 
from random_walk import RandomWalk

while True:
    rw = RandomWalk(5_000)
    rw.fill_walk()

    plt.style.use('Solarize_Light2')
    fig, ax = plt.subplots(figsize=(15,9))

    point_numbers = range(rw.num_points)

    ax.plot(rw.x_values, rw.y_values, linewidth=3)

    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break