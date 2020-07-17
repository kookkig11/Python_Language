c = 0
div = 10
x = int(input())
while True :
    if x>=0:
        a = x % div
        b = x//div
        div = div * 10
        c = a + b
    else:
        break
print(c)