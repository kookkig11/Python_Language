import math
num = int(input("Enter a number: "))
i = 0
a = ''
b = '2 x 1'
if num < 0 :
    print("Invalid input, program terminates.")
else :
    while i <= num :
        if i == 0 :
            print("0! = 1 = 1")
            i = i + 1
        elif i == 1 :
            print("1! = 1 = 1")
            i = i + 1        
        else :
            while i <= num :
                print('%d! = %s = %d' %(i,b, math.factorial(i)))
                a = '%d x ' %(i+1)
                b = a + b
                i = i + 1