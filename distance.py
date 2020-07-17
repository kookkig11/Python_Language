import math
while True:
    print("<<Point a>>")
    xa = int(input("Enter x coordinate: "))
    ya = int(input("Enter y coordinate: "))
    print("<<Point b>>")
    xb = int(input("Enter x coordinate: "))
    yb = int(input("Enter y coordinate: "))
    if xa == 0 and ya == 0 and xb == 0 and yb == 0 :
        print("Goodbye")
        break
    else:
        print("Distance between (%d, %d) and (%d, %d):" %(xa,ya,xb,yb))
        
        distance = math.sqrt((xa-xb)**2 + (ya-yb)**2)
        print("Euclidean distance is %.2f." %distance)
        
        xdistance = abs(xa) + abs(xb)
        ydistance = abs(ya) + abs(yb)
        print("Horizontal distance is %d." %xdistance)
        print("Vertical distance is %d." %ydistance)         
        
        if xa > xb :
            h = 'west'
        elif xa < xb :
            h = 'east'
        else :
            h = ''
        
        if ya > yb :
            v = 'south'
        elif ya < yb :
            v = 'north'
        else :
            v = ''
        
        if xa==xb and ya==yb :
            way = 'nowhere'
        else :
            if v == '' or h == '' :
                way = v + h
            else:
                way = v + '-' + h
        print("We are going %s." %way)