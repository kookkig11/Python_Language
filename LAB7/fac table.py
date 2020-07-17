num = int(input("Enter a number: "))
i = 0
x = ''
if num < 0 :
    print("Invalid input, program terminates.")
else:
    while i <= num :
        if i==0 and i == 1:
            print("%d! = 1 = 1" %i)
            i = i + 1
        elif i > 1 :
            x = x + (i,"x",(i-1))
            i = i+1
            print(x)