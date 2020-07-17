a = int(input("Enter year: "))
b = a%4
c = a%100
d = a%400
if a <= 0 :
    print ("Invalid year.")
else :
    if b == 0 and c != 0 :
        print ("%d is a leap year." %a)
    elif d == 0:
        print ("%d is a leap year." %a)
    else :
        print ("%d is not a leap year." %a)