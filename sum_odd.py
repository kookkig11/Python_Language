x = int(input())
div = 10
odd = 0
if x>=0 and x <= 4000000000:
    if x%2 == 0 :
        print(-1)
    else :
        while True:
            a = x%div
            b = a//(div/10)
            div = div * 10
            if b%2 != 0 :
                odd = odd + b
            if a == x :
                break
        print("%d" %odd)
else:
    print("Invalid Number.")