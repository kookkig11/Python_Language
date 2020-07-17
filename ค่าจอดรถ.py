import math
#input
h = int(input('Enter number of hours: '))
m = int(input('Enter number of minutes: '))
#process and output
if h<0 or m<0 or m>=60 :
    print ("Input Error!")
else:
    a = (h*60)+m
    b = int(math.ceil(a/60)*10-10)
    if a<=15 :
        print ("No charge, thanks.")
    elif a<=120 :
        print ("Total amount due is 10 Bahts.")
    elif a>120 :
        print ("Total amount due is",b,"Bahts.")