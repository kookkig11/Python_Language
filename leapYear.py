year = int(input("Enter year: "))
if year <= 0:
    print("Invalid year.")
elif year > 0:
    if year % 4 == 0 and year % 100 != 0:
        print("%d is a leap year." %year)
    elif year % 400 == 0:
        print("%d is a leap year." %year)
    elif year % 100 == 0:
        print("%d is not a leap year." %year)