from matplotlib import pyplot as plt

def DDA(x0, y0, x1, y1):
    # Find absolute differences
    dx = abs(x0 - x1)
    dy = abs(y0 - y1)

    # Find maximum difference
    steps = max(dx, dy)

    # Calculate the increment in x and y
    xinc = dx / steps
    yinc = dy / steps

    # Start with 1st point
    x = float(x0)
    y = float(y0)

    # Make a list for coordinates
    x_coordinates = []
    y_coordinates = []

    for i in range(int(steps) + 1):
        # Append the coordinates in respective list
        x_coordinates.append(x)
        y_coordinates.append(y)

        # Increment the values
        x = x + xinc
        y = y + yinc

    # Plot the line with coordinates list
    plt.plot(x_coordinates, y_coordinates, marker="o", markersize=1, markerfacecolor="green")
    plt.show()

if _name_ == "_main_":
    # Coordinates of 1st point
    x0, y0 = 20, 20

    # Coordinates of 2nd point
    x1, y1 = 60, 50

    # Function call
    DDA(x0, y0, x1, y1)

# dnkbdhjbdhba