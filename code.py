import numpy as np
from queue import PriorityQueue

start_x_coordinate = input("Enter x coordinate of starting point \n")
start_y_coordinate = input("Enter y coordinate of starting point \n")

starting_point = (int(start_x_coordinate), int(start_y_coordinate))

goal_x_coordinate = input("Enter x coordinate of goal point \n")
goal_y_coordinate = input("Enter y coordinate of goal point \n")

goal_point = (int(goal_x_coordinate), int(goal_y_coordinate))

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

    if x >= 100 and x <= 150 and y>= 150 and y <= 250:
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

    if x >= 64.95 and x <= 364.95 and (((y - 162.5) - ((162.5 - 200)/ (64.95 - 300))* (x - 64.95)) <= 0) and (((y - 200) - ((200 - 162.5)/(300 - 364.95))* (x - 300)) <= 0) and (((y - 87.5) - ((87.5 - 50)/ (364.95 - 300))* (x - 364.95)) >= 0) and (((y - 87.5) - ((87.5 - 50)/ (364.95 - 300))* (x - 364.95)) >= 0):
        return True
    else:
        return False
    
def triangular_obstacle(point_coordinates):
    x = point_coordinates[0]
    y = point_coordinates[1]

    if x>= 460 and (((y - 225) - ((225 - 125)/ (460 - 510))*(x - 460)) <= 0) and (((y - 125) - ((125 - 25)/ (510 - 460))*(x - 510)) >= 0):
        return True
    else:
        False
    
def all_obstacles(point_coordinates):
    if (rectangular_down_obstacle(point_coordinates) or rectangular_up_obstacle(point_coordinates) or hexagonal_obstacle(point_coordinates) or triangular_obstacle(point_coordinates)) == True:
        return True
    else:
        return False

while all_obstacles(starting_point):
    print("The given starting point lies in the obstacle space, enter new starting point \n")
    start_x_coordinate = input("Enter x coordinate of starting point \n")
    start_y_coordinate = input("Enter y coordinate of starting point \n")

while all_obstacles(goal_point):
    print("The given goal point lies in the obstacle space, enter new goal point \n")
    goal_x_coordinate = input("Enter x coordinate of goal point \n")
    goal_y_coordinate = input("Enter y coordinate of goal point \n")


def move_left(source_node, all_obstacles, list_closed, list_open):
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

def move_right(source_node, all_obstacles, list_closed, list_open):
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

def move_up(source_node, all_obstacles, list_closed, list_open):
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

def move_down(source_node, all_obstacles, list_closed, list_open):
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

def diagonal_right_up(source_node, all_obstacles, list_closed, list_open):
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

def diagonal_up_left(source_node, all_obstacles, list_closed, list_open):
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

def diagonal_down_left(source_node, all_obstacles, list_closed, list_open):
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

def diagonal_down_right(source_node, all_obstacles, list_closed, list_open):
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




    
    