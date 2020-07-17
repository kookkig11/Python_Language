num = int(input("Enter a number: "))
digit = int(input("Enter a digit: "))
error = 0
if num < 0 :
    error += 1
if digit < 0 or digit > 9 :
    error += 2
if error == 1:
    print("Invalid number.")
if error == 2:
    print("Invalid digit.")
if error == 3:
    print("Invalid number.")
    print("Invalid digit.")
if error == 0:
    div = 10
    count = 0
    while True:
        a = num%div
        b = a//(div/10)
        if b == digit:
            count = count + 1
        if a == num:
            break
        div = div * 10
    print("Digit %d occurs %d times." %(digit,count))