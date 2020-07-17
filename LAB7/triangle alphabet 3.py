num = int(input('Enter a number: '))
x = ''
y = ''
i = 0
if num <= 0 or num > 26:
    print('Invalid input, program terminates.')
else:
    while i < (num - 1):
        x = x + chr(ord('A') + i)
        i = i + 1
        print(x)
        if i == (num - 1):
            while num >= 1:
                j = 0
                while j < num:
                    y = chr(ord('A') + j)
                    print(y, end='')
                    j = j + 1
                print()
                num = num - 1