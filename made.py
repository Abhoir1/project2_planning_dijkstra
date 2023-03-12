def hexagonal_obstacle(point_coordinates):
    x = point_coordinates[0]
    y = point_coordinates[1]

    # if x >= 235.05 and x <= 364.95 and (((y - 162.5) - ((162.5 - 200)/ (235.05 - 300))* (x - 235.05)) <= 0) and (((y - 200) - ((200 - 162.5)/(300 - 364.95))* (x - 300)) <= 0) and (((y - 87.5) - ((87.5 - 50)/ (364.95 - 300))* (x - 364.95)) >= 0) and (((y - 87.5) - ((87.5 - 50)/ (364.95 - 300))* (x - 364.95)) >= 0):
    #     return True
    # else:
    #     return False

    # v1 = (235.05 - 5, 162.5 + 5)
    # v2 = (300, 200 + 5)
    # v3 = (364.95 + 5, 162.5 + 5)
    # v4 = (364.95 + 5, 87.5 - 5)
    # v5 = (300, 50 -5)
    # v6 = (235.05 - 5, 87.5 - 5)

    # # if x>=v1[0] and x<=v3[0] and y<v2[1] and y>=v5[1]:
    # line1 = (y - v1[1]) - ((v1[1] - v2[1])/ (v1[0] - v2[0]))*(x - v1[0])
    # line2 = (y - v2[1]) - ((v2[1] - v3[1])/ (v2[0] - v3[0]))*(x - v2[0])
    # line4 = (y - v4[1]) - ((v4[1] - v5[1])/ (v4[0] - v5[0]))*(x - v4[0])
    # line5 = (y - v5[1]) - ((v5[1] - v6[1])/ (v5[0] - v6[0]))*(x - v5[0])
        
    # if line1<=0 and line2 <=0 and x <= 364.95+5 and line4 >=0 and line5 >= 0 and x >= 230.05:
    #     return True
    # else:
    #     return False
    if x >= 230.05 and x <= 369.95 and (((y - 167.5) - ((167.5 - 205)/ (235.05 - 300))* (x - 235.05)) <= 0)
    
x = input("x \n")
y = input(" y \n")

coordinates = (int(x), int(y))

print(hexagonal_obstacle(coordinates))