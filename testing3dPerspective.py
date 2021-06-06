class box1():
    x=100
    y=100
    z=100

    size = 150 #length for distance between each point

    point1 = 0,0,0 # top left front
    point2 = 0,0,0 # top right front
    point3 = 0,0,0 # bottom left front
    point4 = 0,0,0 # bottom right front
    point5 = 0,0,0 # top left back
    point6 = 0,0,0 # top right back
    point7 = 0,0,0 # bottom left back
    point8 = 0,0,0 # bottom right back



def set_points():
    x=box1.x
    y=box1.y
    z=box1.z

    size = box1.size

    #this part sets all the points x,y,x co-cords at the correct locations
    #  _____  4____6
    # |\____\  1____2
    # | |    | Middle [x,y,z]
    # |_| `  | 7____8
    #  \|____| 3____4
    #
    # the +50 is just a test to show the 'offset' of the behind points
    box1.point1 = [x-(size/2),y-(size/2),z-(size/2)] # top left front
    box1.point2 = [x+(size/2),y-(size/2),z-(size/2)] # top right front
    box1.point3 = [x-(size/2),y+(size/2),z-(size/2)] # bottom left front
    box1.point4 = [x+(size/2),y+(size/2),z-(size/2)] # bottom right front
    box1.point5 = [x-(size/2)+50,y-(size/2)+50,z+(size/2)] # top left back
    box1.point6 = [x+(size/2)+50,y-(size/2)+50,z+(size/2)] # top right back
    box1.point7 = [x-(size/2)+50,y+(size/2)+50,z+(size/2)] # bottom left back
    box1.point8 = [x+(size/2)+50,y+(size/2)+50,z+(size/2)] # bottom right back


camara_pos = [20,20,20] # I don't know how to make the points based off this
camara_angle = [45,0,0] # or this



while True:
    set_points()
    g.DISPLAYSURF.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    #draws all the lines connecting all the points .
    pygame.draw.line(g.DISPLAYSURF, (128,128,128), (box1.point1[0],box1.point1[1]),(box1.point2[0],box1.point2[1]))
    pygame.draw.line(g.DISPLAYSURF, (128,128,128), (box1.point3[0],box1.point3[1]),(box1.point4[0],box1.point4[1]))
    pygame.draw.line(g.DISPLAYSURF, (128,128,128), (box1.point2[0],box1.point2[1]),(box1.point4[0],box1.point4[1]))
    pygame.draw.line(g.DISPLAYSURF, (128,128,128), (box1.point1[0],box1.point1[1]),(box1.point3[0],box1.point3[1]))

    pygame.draw.line(g.DISPLAYSURF, (128,128,128), (box1.point5[0],box1.point5[1]),(box1.point6[0],box1.point6[1]))
    pygame.draw.line(g.DISPLAYSURF, (128,128,128), (box1.point7[0],box1.point7[1]),(box1.point8[0],box1.point8[1]))
    pygame.draw.line(g.DISPLAYSURF, (128,128,128), (box1.point6[0],box1.point6[1]),(box1.point8[0],box1.point8[1]))
    pygame.draw.line(g.DISPLAYSURF, (128,128,128), (box1.point5[0],box1.point5[1]),(box1.point7[0],box1.point7[1]))

    pygame.draw.line(g.DISPLAYSURF, (128,128,128), (box1.point1[0],box1.point1[1]),(box1.point5[0],box1.point5[1]))
    pygame.draw.line(g.DISPLAYSURF, (128,128,128), (box1.point2[0],box1.point2[1]),(box1.point6[0],box1.point6[1]))
    pygame.draw.line(g.DISPLAYSURF, (128,128,128), (box1.point3[0],box1.point3[1]),(box1.point7[0],box1.point7[1]))
    pygame.draw.line(g.DISPLAYSURF, (128,128,128), (box1.point4[0],box1.point4[1]),(box1.point8[0],box1.point8[1]))

    pygame.display.update()