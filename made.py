import matplotlib.pyplot as plt
import matplotlib.patches as patches

# create a figure and axis object
fig, ax = plt.subplots(figsize=(6,2.5))

# create a Rectangle object
rect = patches.Rectangle((100, 150), 50, 100, linewidth=1, edgecolor='r', facecolor='none')
rect1 = patches.Rectangle((100, 0), 50, 100, linewidth=1, edgecolor='r', facecolor='none')

# add the rectangle to the axis
ax.add_patch(rect)
ax.add_patch(rect1)

center = (300, 125)
radius = 75
num_vertices = 6
hexagon = patches.RegularPolygon(center, num_vertices, radius, linewidth=1, edgecolor='g', facecolor='none')

triangle = patches.Polygon([(460, 25), (460, 225), (510, 125)], linewidth=1, edgecolor='b', facecolor='none')


ax.add_patch(hexagon)
ax.add_patch(triangle)

# set the x and y limits of the axis
ax.set_xlim(0, 600)
ax.set_ylim(0, 250)


