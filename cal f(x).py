import math
x = float(input("Enter x : "))
if x < 0 :
    f = math.sqrt(x**2 + 1)
elif x == 0 :
    f = x
elif x > 0 and x <= 99 :
    f = 3*(x**2) - (1-x)**2
elif x > 99 :
    f = 2*(x**3) - x/(math.sqrt(x+1))
print ("f(%.2f) = %d" % (x,math.ceil(f)))