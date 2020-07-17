num = int(input("Enter a number: "))
a = ''
if num <= 0 or num > 26:
    print('Invalid input, program terminates.')
else:
    while num >= 1:
        count = 0
        while count < num:
            a = chr(ord('A') + count)
            print(a, end='')
            count = count + 1
        print()
        num = num - 1
        
        
