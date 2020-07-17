a = int(input())
b = int(input())
c = int(input())

maxx = 0
min1 = 0
min2 = 0

if c > a and c > b:
    maxx = c
    min1 = a
    min2 = b
    if ((min1**2) + (min2**2)) == maxx**2:
        print(True)
    else:
        print(False)

elif a > c and a > b:
    maxx = a 
    min1 = b
    min2 = c
    if ((min1**2) + (min2**2)) == maxx**2:
        print(True)
    else:
        print(False)
    
elif b > a and b > c:
    maxx = b
    min1 = a
    min2 = c
    if ((min1**2) + (min2**2)) == maxx**2:
        print(True)
    else:
        print(False)