minute = int(input("Minutes before due: "))
temp = float(input("Temperature: "))
rain = str(input("Is it raining (y/n)? "))
day = minute//1440
if minute % 1440 >= 720 :
    day = day + 1
else:
    print(">>> %d days before due." %day)
    if day>=0 and day<2 :
        print(">>> I will do the assignment.")
    elif day>=2 and day<=5 :
        if temp>40 :
            print(">>> I will not do the assignment.")
        elif temp>25 :
            if rain=='y' or rain=='Y' :
                print(">>> I will not do the assignment.")
        elif rain=='n' or rain=='N' :
                print(">>> I will do the assignment.")
    elif day>5 :
        print(">>> I will not do the assignment.")