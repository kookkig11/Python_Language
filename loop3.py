x = int(input())
summ = 0
i = 1
while True:
    i = i + 1
    a = input("Next value (y/n)? ")
    if a=='y':
        x = int(input())
    if a=='n':
        break
    if i>=i-3:
        summ = summ + x
print("\nSum is %d." %summ)