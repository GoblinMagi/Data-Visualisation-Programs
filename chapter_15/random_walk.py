# Random Walks
# A 'random walk' is a path that has no clear direction but is determined by a 
# series of random decisions.

# Creating the RandomWalk() Class
# Requires 3 attribues, variable to store number of points, and two lists to
# store x and y coordinate values of each point

# Import choice() to decide what move to make each step
from random import choice

class RandomWalk:
    """A class to generate random walks."""

    def __init__(self, num_points=5000):
        """Initialise attributes of a walk."""
        self.num_points = num_points

        # All walks start at (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    # Choosing Directions
    def fill_walk(self):
        """Calculate all the points in the walk."""

        # Keep taking steps until the walk reaches the desired length.
        # Loop until walk is filled with correct number of points.
        while len(self.x_values) < self.num_points:

            x_step = self.get_step()
            y_step = self.get_step()

            # Reject moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the new position.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

    # 15-5 Refactoring
    def get_step(self):
        """Determine direction and distance for each step."""
        # Decide which direction to go and how far to go in that direction.
        # Direction, either right or left
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        return direction * distance