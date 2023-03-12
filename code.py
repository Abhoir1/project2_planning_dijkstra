import numpy as np
from queue import PriorityQueue

# Defining the obstacles

def outer_boundary(point_coordinates):
    x = point_coordinates[0]
    y = point_coordinates[1]

    if (x <= 0) and (x >= 300) and (y <=0) and (y >= 250):
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

    if (x >= 100) and (x <= 150) and (y>=0) and (y <= 100):
        return True
    else:
        return False
    
def hexagonal_obstacle(point_coordinates):
    x = point_coordinates[0]
    y = point_coordinates[1]

    # if x >= 235.05 and x <= 364.95 and (((y - 162.5) - ((162.5 - 200)/ (235.05 - 300))* (x - 235.05)) <= 0) and (((y - 200) - ((200 - 162.5)/(300 - 364.95))* (x - 300)) <= 0) and (((y - 87.5) - ((87.5 - 50)/ (364.95 - 300))* (x - 364.95)) >= 0) and (((y - 87.5) - ((87.5 - 50)/ (364.95 - 300))* (x - 364.95)) >= 0):
    #     return True
    # else:
    #     return False

    v1 = (235.05 - 5, 162.5 + 5)
    v2 = (300, 200 + 5)
    v3 = (364.95 + 5, 162.5 + 5)
    v4 = (364.95 + 5, 87.5 - 5)
    v5 = (300, 50 -5)
    v6 = (235.05 - 5, 87.5 - 5)

    # if x>=v1[0] and x<=v3[0] and y<v2[1] and y>=v5[1]:
    line1 = (y - v1[1]) - ((v1[1] - v2[1])/ (v1[0] - v2[0]))*(x - v1[0])
    line2 = (y - v2[1]) - ((v2[1] - v3[1])/ (v2[0] - v3[0]))*(x - v2[0])
    line4 = (y - v4[1]) - ((v4[1] - v5[1])/ (v4[0] - v5[0]))*(x - v4[0])
    line5 = (y - v5[1]) - ((v5[1] - v6[1])/ (v5[0] - v6[0]))*(x - v5[0])
        
    if line1<=0 and line2 <=0 and x <= 364.95+5 and line4 >=0 and line5 >= 0 and x >= 230.05:
        return True
    else:
        return False
    
def triangular_obstacle(point_coordinates):
    x = point_coordinates[0]
    y = point_coordinates[1]

    # if x>= 460 and (((y - 225) - ((225 - 125)/ (460 - 510))*(x - 460)) <= 0) and (((y - 125) - ((125 - 25)/ (510 - 460))*(x - 510)) >= 0):
    #     return True
    # else:
    #     False
    v1 = (460 - 5, 225 + 5)
    v2 = (500 + 5, 125)
    v3 = (460 - 5, 25 - 5)

    line1 = (y - v1[1]) - ((v1[1] - v2[1])/ (v1[0] - v2[0]))*(x - v1[0])
    line2 = (y - v2[1]) - ((v2[1] - v3[1])/ (v2[0] - v3[0]))*(x - v2[0])

    if x>= 455 and line1 <=0 and line2 >=0:
        return True
    else:
        return False
    
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
            node_new_d_up_left = (c2c_d_down_left, parent_node_d_down_left, node_new)
            list_open.put(node_new_d_up_left)

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

print(optimal_path)

optimal_path_x_coordinates = []
optimal_path_y_coordinates = []

for i in range(len(optimal_path)):
    optimal_path_x_coordinates.append(optimal_path[i][0])
    optimal_path_y_coordinates.append(optimal_path[i][1])
    
