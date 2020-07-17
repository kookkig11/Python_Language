while True :
    num = int(input("Enter a number: "))
    if num == 0 :
        print("End of program, goodbye.")
        break
    elif num <= 1 :
        print("Invalid input, try again.")
        continue
    elif num > 1:
        while True :
            if num%2 == 0 and num/2 > 1 :
                print("%d is not a prime number." %num)
                break
            elif num%3 == 0 and num/3 > 1 :
                print("%d is not a prime number." %num)
                break
            elif num%5 == 0 and num/5 > 1 :
                print("%d is not a prime number." %num)
                break
            elif num%7 == 0 and num/7 > 1 :
                print("%d is not a prime number." %num)
                break
            else :
                print("%d is a prime number." %num)
                break