import numpy as np
from queue import PriorityQueue
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def outer_boundary(point_coordinates):
    x = point_coordinates[0]
    y = point_coordinates[1]

    if (x <= 5) and (x >= 595) and (y <=5) and (y >= 245):
        return True
    else:
        return False

def rectangular_up_obstacle(point_coordinates):
    x = point_coordinates[0]
    y = point_coordinates[1]

    if x >= 95 and x <= 155 and y>= 145 and y <= 255:
        return True
    else:
        return False
    
def rectangular_down_obstacle(point_coordinates):
    x = point_coordinates[0]
    y = point_coordinates[1]

    if (x >= 95) and (x <= 155) and (y>=0) and (y <= 105):
        return True
    else:
        return False
    
def hexagonal_obstacle(point_coordinates):
    x = point_coordinates[0]
    y = point_coordinates[1]

    if x >= 230.05 and x <= 369.95 and (((y - 165.38) - ((165.38 - 205.77)/ (230.05 - 300))* (x - 230.05)) <= 0) and (((y - 205.77) - ((205.77 - 165.38)/(300 - 369.95))* (x - 300)) <= 0) and (((y - 84.61) - ((84.61 - 44.22)/ (369.95 - 300))* (x - 369.95)) >= 0) and (((y - 44.22) - ((44.22 - 84.61)/ (300 - 230.04))* (x - 300)) >= 0):
        return True
    else:
        return False
    
def triangular_obstacle(point_coordinates):
    x = point_coordinates[0]
    y = point_coordinates[1]

    if x>= 455 and (((y - 246.18) - ((246.18 - 125)/ (455 - 515.59))*(x - 455)) <= 0) and (((y - 125) - ((125 - 3.81)/ (515.19 - 455))*(x - 515.59)) >= 0):
        return True
    else:
        False
    
def all_obstacles(point_coordinates):
    if (rectangular_down_obstacle(point_coordinates) or rectangular_up_obstacle(point_coordinates) or hexagonal_obstacle(point_coordinates) or triangular_obstacle(point_coordinates)) == True:
        return True
    else:
        return False
    
start_x_coordinate = input("Enter x coordinate of starting point \n")
start_y_coordinate = input("Enter y coordinate of starting point \n")

starting_point = (int(start_x_coordinate), int(start_y_coordinate))

while all_obstacles(starting_point):
    print("The given starting point lies in the obstacle space, enter new starting point \n")
    start_x_coordinate = input("Enter x coordinate of starting point \n")
    start_y_coordinate = input("Enter y coordinate of starting point \n")

goal_x_coordinate = input("Enter x coordinate of goal point \n")
goal_y_coordinate = input("Enter y coordinate of goal point \n")

goal_point = (int(goal_x_coordinate), int(goal_y_coordinate))
250
while all_obstacles(goal_point):
    print("The given goal point lies in the obstacle space, enter new goal point \n")
    goal_x_coordinate = input("Enter x coordinate of goal point \n")
    goal_y_coordinate = input("Enter y coordinate of goal point \n")


def move_left(source_node, list_closed, list_open):
    c2c_left = source_node[0] + 1
    parent_node_left = source_node[2]

    x_coordinate_new = source_node[2][0] - 1
    y_coordinate_new = source_node[2][1]

    node_new = (x_coordinate_new, y_coordinate_new)

    if all_obstacles(node_new) == False:
        if node_new not in list_closed:
            node_new_left = (c2c_left, parent_node_left, node_new)
            list_open.put(node_new_left)
    return list_open

def move_right(source_node, list_closed, list_open):
    c2c_right = source_node[0] + 1
    parent_node_right = source_node[2]

    x_coordinate_new = source_node[2][0] + 1
    y_coordinate_new = source_node[2][1]

    node_new = (x_coordinate_new, y_coordinate_new)

    if all_obstacles(node_new) == False:
        if node_new not in list_closed:
            node_new_right = (c2c_right, parent_node_right, node_new)
            list_open.put(node_new_right)
    return list_open

def move_up(source_node, list_closed, list_open):
    c2c_up = source_node[0] + 1
    parent_node_up = source_node[2]

    x_coordinate_new = source_node[2][0] 
    y_coordinate_new = source_node[2][1] + 1

    node_new = (x_coordinate_new, y_coordinate_new)

    if all_obstacles(node_new) == False:
        if node_new not in list_closed:
            node_new_up = (c2c_up, parent_node_up, node_new)
            list_open.put(node_new_up)
    return list_open

def move_down(source_node, list_closed, list_open):
    c2c_down = source_node[0] + 1
    parent_node_down = source_node[2]

    x_coordinate_new = source_node[2][0] 
    y_coordinate_new = source_node[2][1] - 1

    node_new = (x_coordinate_new, y_coordinate_new) 

    if all_obstacles(node_new) == False:
        if node_new not in list_closed:
            node_new_down = (c2c_down, parent_node_down, node_new)
            list_open.put(node_new_down)
    return list_open

def move_diagonal_right_up(source_node, list_closed, list_open):
    c2c_d_up_right = source_node[0] + 1.4
    parent_node_d_up_right = source_node[2]

    x_coordinate_new = source_node[2][0] + 1
    y_coordinate_new = source_node[2][1] + 1

    node_new = (x_coordinate_new, y_coordinate_new)

    if all_obstacles(node_new) == False:
        if node_new not in list_closed:
            node_new_d_up_right = (c2c_d_up_right, parent_node_d_up_right, node_new)
            list_open.put(node_new_d_up_right)
    return list_open

def move_diagonal_up_left(source_node, list_closed, list_open):
    c2c_d_up_left = source_node[0] + 1.4
    parent_node_d_up_left = source_node[2]

    x_coordinate_new = source_node[2][0] - 1
    y_coordinate_new = source_node[2][1] + 1  

    node_new = (x_coordinate_new, y_coordinate_new)

    if all_obstacles(node_new) == False:
        if node_new not in list_closed:
            node_new_d_up_left = (c2c_d_up_left, parent_node_d_up_left, node_new)
            list_open.put(node_new_d_up_left)

    return list_open

def move_diagonal_down_left(source_node, list_closed, list_open):
    c2c_d_down_left = source_node[0] + 1.4
    parent_node_d_down_left = source_node[2]

    x_coordinate_new = source_node[2][0] - 1
    y_coordinate_new = source_node[2][1] - 1  

    node_new = (x_coordinate_new, y_coordinate_new)

    if all_obstacles(node_new) == False:
        if node_new not in list_closed:
            node_new_d_down_left = (c2c_d_down_left, parent_node_d_down_left, node_new)
            list_open.put(node_new_d_down_left)

    return list_open

def move_diagonal_down_right(source_node, list_closed, list_open):
    c2c_d_down_right = source_node[0] + 1.4
    parent_node_d_down_right = source_node[2]

    x_coordinate_new = source_node[2][0] + 1
    y_coordinate_new = source_node[2][1] - 1  

    node_new = (x_coordinate_new, y_coordinate_new)

    if all_obstacles(node_new) == False:
        if node_new not in list_closed:
            node_new_d_down_right = (c2c_d_down_right, parent_node_d_down_right, node_new)
            list_open.put(node_new_d_down_right)

    return list_open

x_coordinate_visited = []
y_coordinate_visited = []

start = starting_point
goal = goal_point

c2c = 0
parent_node = None

source_nodek = (c2c, (parent_node), (start))

list_openk = PriorityQueue()
list_closedk = {}
list_openk.put(source_nodek)

while True:
    source_node = list_openk.get()

    if source_node[2] in list_closedk:
        continue

    x_coordinate_visited.append(source_node[2][0])
    y_coordinate_visited.append(source_node[2][1])

    list_closedk[source_node[2]] = source_node[1]

    if source_node[2] == goal:
        print("Goal has been reached")
        break
    else:
        move_down(source_node,list_closedk, list_openk)
        move_up(source_node,list_closedk, list_openk)
        move_right(source_node,list_closedk, list_openk)
        move_left(source_node,list_closedk, list_openk)
        move_diagonal_down_left(source_node,list_closedk, list_openk)
        move_diagonal_down_right(source_node,list_closedk, list_openk)
        move_diagonal_right_up(source_node,list_closedk, list_openk)
        move_diagonal_up_left(source_node,list_closedk, list_openk)

optimal_path = []
present_node = goal

while present_node != start:
    optimal_path.append(present_node)
    present_node = list_closedk[present_node]

optimal_path.append(start)
optimal_path.reverse()

# print(optimal_path)

optimal_path_x_coordinates = []
optimal_path_y_coordinates = []

for i in range(len(optimal_path)):
    optimal_path_x_coordinates.append(optimal_path[i][0])
    optimal_path_y_coordinates.append(optimal_path[i][1])
    
fig, ax = plt.subplots(figsize=(6,2.5))

rect = patches.Rectangle((100, 150), 50, 100, linewidth=1, edgecolor='r', facecolor='none')
rect1 = patches.Rectangle((100, 0), 50, 100, linewidth=1, edgecolor='r', facecolor='none')
center = (300, 125)
radius = 75
num_vertices = 6
hexagon = patches.RegularPolygon(center, num_vertices, radius, linewidth=1, edgecolor='g', facecolor='none')
triangle = patches.Polygon([(460, 25), (460, 225), (510, 125)], linewidth=1, edgecolor='b', facecolor='none')

ax.add_patch(rect)
ax.add_patch(rect1)
ax.add_patch(hexagon)
ax.add_patch(triangle)

plt.ylabel('Y')
plt.xlabel('X')
plt.axis([0 , 600 , 0 ,250])

plot_x = 0
plot_y = 0
plt.title("Exploring all the Visited list")
for i in range(len(x_coordinate_visited)) :
    if plot_x == goal[0] and plot_y == goal[1] :
        break
    if len(x_coordinate_visited)>100:
        plt.scatter(x_coordinate_visited[0:100] , y_coordinate_visited[0:100] , c='blue' , s=1)
        plt.pause(0.0005)
        del x_coordinate_visited[:100]
        del y_coordinate_visited[:100]
    else :
        for j in range(len(x_coordinate_visited)):
            plt.scatter(x_coordinate_visited[j] , y_coordinate_visited[j] , c='blue' , s=1)
            plt.pause(0.0005)
            plot_x = x_coordinate_visited[j]
            plot_y = y_coordinate_visited[j]
            if x_coordinate_visited[j] == goal[0] and y_coordinate_visited[j] == goal[1] :
                break

plt.title("Showing the Shortest Path")
for i in range(len(optimal_path_x_coordinates)):
    plt.scatter(optimal_path_x_coordinates[i] , optimal_path_y_coordinates[i] , c='yellow' , s=2, marker='D')
    plt.pause(0.00005)

plt.show