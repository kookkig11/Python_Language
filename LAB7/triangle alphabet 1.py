num = int(input("Enter a number: "))
i = 0
x = ''
while i < num :
    if num <= 0 and num > 26 :
        print("Invalid input, program terminates.")
    else :
        x = x + chr(ord('A') + i)
        i = i + 1
        print(x)     