import numpy as np

# Defining the obstacles

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

def outer_boundary(point_coordinates):
    x = point_coordinates[0]
    y = point_coordinates[1]

    if (x <= 0) and (x >= 300) and (y <=0) and (y >= 250):
        return True
    else:
        return False
    
def all_obstacles(point_coordinates):
    if (rectangular_down_obstacle(point_coordinates) or rectangular_up_obstacle(point_coordinates) or hexagonal_obstacle(point_coordinates) or triangular_obstacle(point_coordinates)) == True:
        return True
    else:
        return False
    
