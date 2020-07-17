h = int(input("Enter height: "))
w = int(input("Enter width: "))
i = 1
if h <= 0 or w <= 0 :
    print("Invalid input, program terminates.")
else:
    while i <= h:
        if i%2 == 1 :
            print('* '*w,end='')
        elif i%2 == 0 :
            print(' *'*w,end='')
        print()
        i = i + 1