num = int(input("Enter positive integer: "))
if num <= 0 :
    print("Invalid number.")
elif num == 1 :
    pass
else :
    while num%2 == 0 :
        print(2)
        num = num/2
    while num%3 == 0 :
        print(3)
        num = num/3
    while num%5 == 0 :
        print(5)
        num = num/5
    while num%7 == 0 :
        print(7)
        num = num/7
    while num%11 == 0 :
        print(11)
        num = num/11
    while num%13 == 0 :
        print(13)
        num = num/13
    while num%17 == 0 :
        print(17)
        num = num/17
    while num%19 == 0 :
        print(19)
        num = num/19
    while num%23 == 0 :
        print(23)
        num = num/23 
    while num%29 == 0 :
        print(29)
        num = num/29              