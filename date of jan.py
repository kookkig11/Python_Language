day = input()
date = int(input())

if day == 'Sunday' :
    num = 1
elif day == 'Monday' :
    num = 2
elif day == 'Tuesday' :
    num = 3
elif day == 'Wednesday' :
    num = 4
elif day == 'Thursday' :
    num = 5
elif day == 'Friday' :
    num = 6
elif day == 'Saturday' :
    num = 7
else :
    num = 0

if num == 0 :
    print("ERROR")
elif date < 1 or date > 31 :
    print("ERROR")
else :
    while date >= 7 :
        date = date - 7
    out = (date - 1) + num
    
    if out > 7:
        out = out - 7
    
    if out == 1 :
        print("Sunday")
    elif out == 2 :
        print("Monday")
    elif out == 3 :
        print("Tuesday")
    elif out == 4 :
        print("Wednesday")
    elif out == 5 :
        print("Thursday")
    elif out == 6 :
        print("Friday")
    elif out == 7 :
        print("Saturday")